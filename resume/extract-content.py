import html
import json
import pathlib
import re

HERE = pathlib.Path(__file__).parent


def text_of(fragment):
    s = re.sub(r"<b>(.*?)</b>", r"**\1**", fragment, flags=re.S)
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = s.replace("·", " · ")
    s = re.sub(r"[ \t]+", " ", s)
    return s.strip()


def grab(pattern, source, flags=re.S):
    m = re.search(pattern, source, flags)
    return text_of(m.group(1)) if m else ""


def parse(path):
    src = path.read_text(encoding="utf-8")
    doc = {
        "name": grab(r'<div class="name">(.*?)</div>', src),
        "role": grab(r'<div class="role">(.*?)</div>', src),
        "description": re.search(r'name="description" content="(.*?)"', src).group(1),
        "contact": [l for l in grab(r'<div class="contact">(.*?)</div>', src).split("\n") if l],
        "sections": [],
    }

    for block in re.findall(r'<section class="sec[^"]*">(.*?)</section>', src, re.S):
        sec = {"h": grab(r"<h2>(.*?)</h2>", block)}
        if 'class="sec break"' in src[: src.index(block)][-40:]:
            sec["pageBreak"] = True

        summary = re.search(r'<p class="summary">(.*?)</p>', block, re.S)
        if summary:
            sec["para"] = text_of(summary.group(1))

        jobs = []
        for job in re.findall(r'<div class="job">(.*?)</div>\s*</div>\s*(?=<div class="job">|$)', block + " ", re.S):
            pass
        for job in re.split(r'<div class="job">', block)[1:]:
            title_html = re.search(r'<div class="title">(.*?)</div>', job, re.S)
            if not title_html:
                continue
            raw = title_html.group(1)
            at = grab(r'<span class="at">(.*?)</span>', raw)
            title = text_of(re.sub(r'<span class="at">.*?</span>', "", raw, flags=re.S))
            jobs.append({
                "title": title,
                "at": at.lstrip("— ").strip(),
                "date": grab(r'<div class="meta">(.*?)</div>', job),
                "bullets": [text_of(li) for li in re.findall(r"<li>(.*?)</li>", job, re.S)],
            })
        if jobs:
            sec["jobs"] = jobs
        else:
            bullets = [text_of(li) for li in re.findall(r"<li>(.*?)</li>", block, re.S)]
            if bullets:
                sec["bullets"] = bullets

        skills = []
        for sk in re.findall(r'<p class="skill">(.*?)</p>', block, re.S):
            m = re.match(r"\s*<b>(.*?)</b>\s*&mdash;\s*(.*)", sk, re.S)
            if m:
                skills.append([text_of(m.group(1)), text_of(m.group(2))])
        if skills:
            sec["skills"] = skills

        row = re.search(r'<div class="row">\s*<div>(.*?)</div>\s*<div class="meta">(.*?)</div>', block, re.S)
        if row:
            sec["row"] = [text_of(row.group(1)), text_of(row.group(2))]

        if not any(k in sec for k in ("para", "jobs", "bullets", "skills", "row")):
            body = re.search(r"</h2>\s*(.*)", block, re.S)
            if body:
                sec["para"] = text_of(body.group(1))

        doc["sections"].append(sec)

    return doc


def mark_breaks(path, doc):
    src = path.read_text(encoding="utf-8")
    broken = {
        grab(r"<h2>(.*?)</h2>", block)
        for block in re.findall(r'<section class="sec break">(.*?)</section>', src, re.S)
    }
    for sec in doc["sections"]:
        sec.pop("pageBreak", None)
        if sec["h"] in broken:
            sec["pageBreak"] = True


def parse_letter(path):
    raw = path.read_text(encoding="utf-8")
    blocks = re.split(r"\n-{3,}\n", raw)
    header = [l.strip() for l in blocks[0].strip().splitlines() if l.strip()]
    body = blocks[1].strip() if len(blocks) > 1 else ""
    paras = []
    for block in re.split(r"\n\s*\n", body):
        if not block.strip():
            continue
        if block.lstrip().startswith("- "):
            for item in re.split(r"\n(?=\s*-\s)", block):
                text = re.sub(r"^\s*-\s+", "", item)
                paras.append({"t": " ".join(text.split()), "tight": False, "bullet": True})
            continue
        lines = [l.strip() for l in block.strip().splitlines()]
        if len(lines) <= 3 and all(len(l) < 45 for l in lines):
            for i, line in enumerate(lines):
                paras.append({"t": line, "tight": i < len(lines) - 1, "bullet": False})
        else:
            paras.append({"t": " ".join(block.split()), "tight": False, "bullet": False})
    return {"header": header, "paragraphs": paras}


out = {}
for lang, f, letter in (
    ("en", "resume-en.html", "cover-letter-en.md"),
    ("pt", "resume-pt.html", "cover-letter-pt.md"),
):
    p = HERE / f
    doc = parse(p)
    mark_breaks(p, doc)
    doc["letter"] = parse_letter(HERE / letter)
    out[lang] = doc

(HERE / "resume-content.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8"
)

for lang, doc in out.items():
    secs = ", ".join(s["h"] + ("*" if s.get("pageBreak") else "") for s in doc["sections"])
    print(f"{lang}: {len(doc['sections'])} sections -> {secs}")
    print(f"{lang}: letter, {len(doc['letter']['paragraphs'])} paragraphs")
