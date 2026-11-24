const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  BorderStyle, LevelFormat, PositionalTab, PositionalTabAlignment,
  PositionalTabLeader, PageBreak, ExternalHyperlink,
} = require("docx");
const fs = require("fs");
const path = require("path");

const INK = "0D0D0C";
const DIM = "35332F";
const META = "6B665E";
const RULE = "D6D2CB";
const FONT = "Arial";

const BODY = 18;
const SMALL = 17;
const LABEL = 16;
const TITLE = 21;
const NAME = 42;

const LINK = /([\w.+-]+@[\w-]+\.[a-z]{2,}|(?:[\w-]+\.)+(?:com|io|net|org|dev|app|br)(?:\/[^\s,;)"]*)?)/gi;
const IS_LINK = new RegExp(`^(?:${LINK.source})$`, "i");

function href(t) {
  return t.includes("@") ? `mailto:${t}` : `https://${t}`;
}

function runs(text, base = {}) {
  const out = [];
  for (const part of String(text).split(/(\*\*[^*]+\*\*)/g)) {
    if (!part) continue;
    const bold = part.startsWith("**") && part.endsWith("**");
    const body = bold ? part.slice(2, -2) : part;
    for (const piece of body.split(LINK)) {
      if (!piece) continue;
      const link = IS_LINK.test(piece);
      const run = new TextRun({
        text: piece,
        bold: bold || base.bold === true,
        font: FONT,
        size: base.size || BODY,
        color: base.color || INK,
        characterSpacing: base.characterSpacing,
        allCaps: base.allCaps,
        underline: link ? {} : undefined,
      });
      out.push(link ? new ExternalHyperlink({ children: [run], link: href(piece) }) : run);
    }
  }
  return out;
}

function sectionHeading(text) {
  return new Paragraph({
    spacing: { before: 280, after: 120 },
    keepNext: true,
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: INK, space: 4 } },
    children: runs(text, { bold: true, size: LABEL, allCaps: true, characterSpacing: 14 }),
  });
}

function jobLine(title, at, date) {
  const children = [
    ...runs(`**${title}**`, { size: TITLE }),
    ...runs(` — ${at}`, { size: TITLE, color: DIM }),
  ];
  if (date) {
    children.push(new TextRun({
      children: [new PositionalTab({
        alignment: PositionalTabAlignment.RIGHT,
        relativeTo: "margin",
        leader: PositionalTabLeader.NONE,
      })],
    }));
    children.push(new TextRun({
      text: date, font: FONT, size: LABEL, color: META,
      allCaps: true, characterSpacing: 10,
    }));
  }
  return new Paragraph({ spacing: { before: 180, after: 60 }, keepNext: true, children });
}

function bullet(text) {
  return new Paragraph({
    numbering: { reference: "bul", level: 0 },
    spacing: { after: 50, line: 250 },
    children: runs(text),
  });
}

function para(text, opts = {}) {
  return new Paragraph({
    spacing: { after: opts.after === undefined ? 60 : opts.after, line: 250 },
    children: runs(text, opts),
  });
}

function skillLine(label, value) {
  return new Paragraph({
    spacing: { after: 60, line: 250 },
    children: [
      ...runs(label, { bold: true, size: LABEL, allCaps: true, characterSpacing: 10 }),
      ...runs(` — ${value}`),
    ],
  });
}

function rowLine(left, right) {
  return new Paragraph({
    spacing: { after: 60, line: 250 },
    children: [
      ...runs(left),
      new TextRun({
        children: [new PositionalTab({
          alignment: PositionalTabAlignment.RIGHT,
          relativeTo: "margin",
          leader: PositionalTabLeader.NONE,
        })],
      }),
      new TextRun({
        text: right, font: FONT, size: LABEL, color: META,
        allCaps: true, characterSpacing: 10,
      }),
    ],
  });
}

function build(d) {
  const kids = [];

  kids.push(new Paragraph({
    spacing: { after: 40 },
    children: runs(d.name, { bold: true, size: NAME, allCaps: true, characterSpacing: -6 }),
  }));
  kids.push(new Paragraph({
    spacing: { after: 140 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 6 } },
    children: runs(d.role, { bold: true, size: LABEL, allCaps: true, characterSpacing: 18 }),
  }));
  for (const line of d.contact) {
    kids.push(para(line, { size: SMALL, color: DIM, after: 20 }));
  }

  for (const sec of d.sections) {
    if (sec.pageBreak) kids.push(new Paragraph({ children: [new PageBreak()] }));
    kids.push(sectionHeading(sec.h));
    if (sec.para) kids.push(para(sec.para));
    for (const j of sec.jobs || []) {
      kids.push(jobLine(j.title, j.at, j.date));
      for (const b of j.bullets) kids.push(bullet(b));
    }
    for (const b of sec.bullets || []) kids.push(bullet(b));
    for (const s of sec.skills || []) kids.push(skillLine(s[0], s[1]));
    if (sec.row) kids.push(rowLine(sec.row[0], sec.row[1]));
  }

  return new Document({
    creator: d.name,
    title: `${d.name} — ${d.role}`,
    description: d.description,
    numbering: {
      config: [{
        reference: "bul",
        levels: [{
          level: 0,
          format: LevelFormat.BULLET,
          text: "•",
          alignment: AlignmentType.LEFT,
          style: {
            paragraph: { indent: { left: 200, hanging: 170 } },
            run: { color: "8C8780", font: FONT, size: BODY },
          },
        }],
      }],
    },
    styles: {
      default: {
        document: { run: { font: FONT, size: BODY, color: INK } },
      },
    },
    sections: [{
      properties: { page: { margin: { top: 850, bottom: 737, left: 907, right: 907 } } },
      children: kids,
    }],
  });
}

function buildLetter(d) {
  const L = d.letter;
  const kids = [];

  kids.push(new Paragraph({
    spacing: { after: 40 },
    children: runs(L.header[0], { bold: true, size: 26 }),
  }));
  for (const line of L.header.slice(1)) {
    kids.push(para(line, { size: SMALL, color: DIM, after: 20 }));
  }
  kids.push(new Paragraph({
    spacing: { before: 120, after: 260 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 6 } },
    children: [],
  }));

  for (const p of L.paragraphs) {
    kids.push(new Paragraph({
      numbering: p.bullet ? { reference: "bul", level: 0 } : undefined,
      spacing: { after: p.bullet ? 70 : p.tight ? 0 : 200, line: 280 },
      children: runs(p.t),
    }));
  }

  return new Document({
    creator: d.name,
    title: `${d.name} — ${d.role} — Cover Letter`,
    numbering: {
      config: [{
        reference: "bul",
        levels: [{
          level: 0,
          format: LevelFormat.BULLET,
          text: "•",
          alignment: AlignmentType.LEFT,
          style: {
            paragraph: { indent: { left: 260, hanging: 200 } },
            run: { color: "8C8780", font: FONT, size: BODY },
          },
        }],
      }],
    },
    styles: { default: { document: { run: { font: FONT, size: BODY, color: INK } } } },
    sections: [{
      properties: { page: { margin: { top: 1100, bottom: 1100, left: 1100, right: 1100 } } },
      children: kids,
    }],
  });
}

const DATA = require("./resume-content.json");

(async () => {
  const jobs = [
    ["en", "Eduardo-Fernandes-Resume.docx", build],
    ["pt", "Eduardo-Fernandes-Curriculo.docx", build],
    ["en", "Eduardo-Fernandes-Cover-Letter.docx", buildLetter],
    ["pt", "Eduardo-Fernandes-Carta-de-Apresentacao.docx", buildLetter],
  ];
  const outDir = process.argv[2] || path.join(__dirname, "out");
  fs.mkdirSync(outDir, { recursive: true });
  for (const [lang, file, make] of jobs) {
    const buf = await Packer.toBuffer(make(DATA[lang]));
    fs.writeFileSync(path.join(outDir, file), buf);
    console.log(`${file}: ${(buf.length / 1024).toFixed(0)} KB`);
  }
})();
