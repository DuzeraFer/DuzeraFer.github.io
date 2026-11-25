import json
import os
import re
import subprocess
import sys
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
MEDIA = re.compile(r"\.(jpg|jpeg|png|webp|gif|avif|svg|mp4|webm|mov)$", re.I)


def git(*args):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    try:
        p = subprocess.run(("git",) + args, cwd=ROOT, env=env,
                           capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        return 1, "git %s timed out after 120s" % args[0]
    return p.returncode, (p.stdout + p.stderr).strip()


def asset_list():
    out = []
    for base, _, files in os.walk(os.path.join(ROOT, "assets")):
        rel = os.path.relpath(base, ROOT).replace("\\", "/")
        for f in files:
            if MEDIA.search(f):
                out.append(f"{rel}/{f}")
    return sorted(out)


def safe_dest(dest, name):
    parts = [p for p in dest.replace("\\", "/").split("/") if p not in ("", ".", "..")]
    if not parts or parts[0] != "assets":
        raise ValueError("destination must be inside assets/")
    name = re.sub(r"[^\w.\-]+", "-", name).lower().lstrip(".")
    if not name or not MEDIA.search(name):
        raise ValueError("unsupported file type")
    return "/".join(parts + [name])


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *a):
        if "/api/" in (self.path or ""):
            sys.stderr.write("%s\n" % (fmt % a))

    def reply(self, code, obj):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def read_body(self):
        return self.rfile.read(int(self.headers.get("Content-Length") or 0))

    def do_GET(self):
        if self.path.split("?")[0] == "/api/assets":
            return self.reply(200, {"assets": asset_list()})
        return super().do_GET()

    def do_POST(self):
        route = self.path.split("?")[0]
        try:
            if route == "/api/save":
                data = self.read_body()
                if b"window.SITE" not in data[:64]:
                    return self.reply(400, {"error": "that does not look like data.js"})
                with open(os.path.join(ROOT, "data.js"), "wb") as fh:
                    fh.write(data)
                return self.reply(200, {"ok": True})

            if route == "/api/upload":
                rel = safe_dest(self.headers.get("X-Dest", ""), self.headers.get("X-Name", ""))
                full = os.path.join(ROOT, *rel.split("/"))
                os.makedirs(os.path.dirname(full), exist_ok=True)
                with open(full, "wb") as fh:
                    fh.write(self.read_body())
                return self.reply(200, {"path": rel})

            if route == "/api/publish":
                msg = self.read_body().decode("utf-8").strip() or "Update site content"
                code, out = git("status", "--porcelain")
                if code:
                    return self.reply(500, {"error": out})
                if not out:
                    return self.reply(200, {"ok": True, "message": "Nothing to publish — no changes."})
                git("add", "-A")
                code, out = git("commit", "-m", msg)
                if code:
                    return self.reply(500, {"error": out})
                code, push = git("push")
                if code:
                    return self.reply(500, {"error": push})
                tail = push.splitlines()[-1] if push else ""
                return self.reply(200, {"ok": True, "message": ("Published — " + tail) if tail else "Published."})
        except Exception as exc:
            return self.reply(400, {"error": str(exc)})

        return self.reply(404, {"error": "unknown endpoint"})


class Server(ThreadingHTTPServer):
    allow_reuse_address = False


def listen(port):
    for p in range(port, port + 10):
        try:
            return Server(("127.0.0.1", p), Handler), p
        except OSError:
            print(f"Port {p} is busy (another editor window?) — trying {p + 1}.")
    raise SystemExit("No free port between %d and %d." % (port, port + 9))


if __name__ == "__main__":
    srv, PORT = listen(PORT)
    url = f"http://127.0.0.1:{PORT}/editor.html"
    print(f"Portfolio editor  {url}\nSite              http://127.0.0.1:{PORT}/\nCtrl+C to stop.")
    if "--no-open" not in sys.argv:
        webbrowser.open(url)
    srv.serve_forever()
