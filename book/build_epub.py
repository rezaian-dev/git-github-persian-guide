#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build RTL EPUB from markdown chapters + figures."""
import html as htmlmod
import pathlib
import re
from markdown_it import MarkdownIt
from ebooklib import epub

ROOT = pathlib.Path(__file__).parent
CH_DIR = ROOT / "chapters"
FIG_DIR = ROOT / "figures"
OUT_EPUB = ROOT.parent / "docs" / "pdf" / "Git-GitHub-Persian-Guide.epub"

md = MarkdownIt("commonmark", {"html": True}).enable("table")

CALLOUT = {
    "note": "نکته",
    "tip": "نکته حرفه‌ای",
    "warn": "هشدار",
    "danger": "اشتباه رایج",
    "interview": "سؤالات مصاحبه",
    "project": "مینی‌پروژه",
    "exercise": "تمرین",
    "summary": "جمع‌بندی",
    "compare": "مقایسه",
}


def parse_chapter(path):
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    meta, body = {}, raw
    if m:
        for ln in m.group(1).split("\n"):
            if ":" in ln:
                k, v = ln.split(":", 1)
                meta[k.strip()] = v.strip()
        body = m.group(2)
    meta.setdefault("num", path.stem[:2])
    return meta, body


def preprocess(text: str) -> str:
    lines = text.split("\n")
    out, i = [], 0
    while i < len(lines):
        if re.match(r"^\s*- \[[ xX]\] ", lines[i]):
            out += ["", ""]
            while i < len(lines) and re.match(r"^\s*- \[[ xX]\] ", lines[i]):
                out.append(re.sub(r"^(\s*)- \[[ xX]\] ", r"\1- ☐ ", lines[i]))
                i += 1
            out.append("")
            continue
        m = re.match(r"^:::\s*([a-z]+)(?:\s+(.*))?$", lines[i])
        if m:
            typ, title = m.group(1), (m.group(2) or "").strip()
            if typ in ("cols", "col", "steps"):
                out.append("")
                i += 1
                continue
            title = title or CALLOUT.get(typ, "")
            out += ["", f"**{title}**", ""]
            i += 1
            continue
        if lines[i].strip() == ":::":
            out.append("")
            i += 1
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


files = sorted(CH_DIR.glob("*.md"))
chapters = [(*parse_chapter(f), f) for f in files]

book = epub.EpubBook()
book.set_identifier("git-github-persian-guide-2026-1.0.0")
book.set_title("مرجع جامع Git و GitHub — از صفر تا فوق‌پیشرفته با VS Code")
book.set_language("fa")
book.add_author("محمدرضا رضائیان")
book.add_metadata("DC", "description", "مرجع فارسی Git و GitHub ۲۰۲۶ در ۳۶ فصل؛ CLI و Source Control در VS Code")
book.add_metadata("DC", "publisher", "Persian Developer Handbook")
book.add_metadata("DC", "rights", "CC BY-NC-SA 4.0")
book.set_direction("rtl")

style = """
body { font-family: Tahoma, "Segoe UI", sans-serif; direction: rtl; text-align: right; line-height: 1.9; color: #1e293b; }
h1 { font-size: 1.7em; color: #c2410c; border-bottom: 2px solid #ea580c; padding-bottom: 8px; }
h2 { font-size: 1.3em; color: #0f172a; margin-top: 1.4em; }
h3 { font-size: 1.1em; color: #1e293b; }
pre { background: #1e293b; color: #f8f8f2; padding: 12px; border-radius: 8px; overflow-x: auto; direction: ltr; text-align: left; font-size: 0.9em; white-space: pre-wrap; }
code { background: #fff7ed; color: #7c2d12; padding: 1px 5px; border-radius: 4px; direction: ltr; unicode-bidi: isolate; }
table { border-collapse: collapse; width: 100%; margin: 12px 0; }
th { background: #ea580c; color: #000; padding: 8px; text-align: right; }
td { border-top: 1px solid #e2e8f0; padding: 7px; }
blockquote { border-right: 3px solid #fdba74; background: #fff7ed; padding: 8px 12px; border-radius: 6px; margin: 12px 0; }
img { max-width: 100%; height: auto; }
.figcap { font-size: 0.9em; color: #64748b; text-align: center; }
"""
css = epub.EpubItem(uid="style", file_name="style/style.css", media_type="text/css", content=style.encode("utf-8"))
book.add_item(css)

cover_path = ROOT / "cover-bg.jpg"
if cover_path.exists():
    cover_data = cover_path.read_bytes()
    book.set_cover("images/cover.jpg", cover_data)

added_imgs = set()


def embed_images(html_body: str) -> str:
    def repl(m):
        src = m.group(1)
        name = pathlib.Path(src).name
        path = FIG_DIR / name
        if not path.exists():
            path = ROOT / src
        if path.exists() and name not in added_imgs:
            data = path.read_bytes()
            mime = "image/png" if path.suffix.lower() == ".png" else (
                "image/jpeg" if path.suffix.lower() in (".jpg", ".jpeg") else "image/svg+xml"
            )
            item = epub.EpubItem(uid=f"img-{name}", file_name=f"images/{name}", media_type=mime, content=data)
            book.add_item(item)
            added_imgs.add(name)
        return f'<img src="images/{name}" alt="{htmlmod.escape(m.group(2) or "")}"/>'
    return re.sub(r'<img\s+src="([^"]+)"\s+alt="([^"]*)"\s*/?>', repl, html_body)


epub_chapters = []
for meta, body, path in chapters:
    title = re.sub(r"<[^>]+>", "", meta.get("title", ""))
    num = meta.get("num", "")
    html_body = embed_images(md.render(preprocess(body)))
    full_html = (
        f'<html dir="rtl" lang="fa" xmlns="http://www.w3.org/1999/xhtml">'
        f'<head><meta charset="utf-8"/><title>{htmlmod.escape(title)}</title>'
        f'<link rel="stylesheet" href="style/style.css"/></head><body>'
        f"<h1>{htmlmod.escape(num)} — {htmlmod.escape(title)}</h1>{html_body}</body></html>"
    )
    c = epub.EpubHtml(title=f"{num} — {title}", file_name=f"ch_{num}.xhtml", lang="fa")
    c.content = full_html
    c.add_item(css)
    book.add_item(c)
    epub_chapters.append(c)

book.toc = tuple(epub_chapters)
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())
book.spine = ["nav"] + epub_chapters

OUT_EPUB.parent.mkdir(parents=True, exist_ok=True)
epub.write_epub(str(OUT_EPUB), book, {})
print(f"EPUB written -> {OUT_EPUB} ({OUT_EPUB.stat().st_size // 1024} KB) — {len(epub_chapters)} chapters")
