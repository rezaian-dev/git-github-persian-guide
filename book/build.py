# -*- coding: utf-8 -*-
"""
Build script: Markdown chapters  ->  styled HTML  ->  PDF (WeasyPrint)
Design: Git & GitHub Persian Guide — Vazirmatn + JetBrains Mono
"""
import re, html, pathlib, sys, time
from markdown_it import MarkdownIt
from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer
from pygments.formatters import HtmlFormatter
from weasyprint import HTML

ROOT = pathlib.Path(__file__).parent
CH_DIR = ROOT / "chapters"
OUT_PDF = ROOT.parent / "docs" / "pdf" / "Git-GitHub-Persian-Guide.pdf"
OUT_HTML = ROOT / "build" / "book.html"

PARTS = {
    "1": ("بخش یکم", "بنیادها و مدل ذهنی Git"),
    "2": ("بخش دوم", "کار روزانه، VS Code و GitHub"),
    "3": ("بخش سوم", "پیشرفته، امنیت، CI و Production"),
    "4": ("بخش چهارم", "کارگاه، نکات طلایی و مصاحبه"),
}

CALLOUT_TITLES = {
    "note": "نکته",
    "tip": "نکته حرفه‌ای",
    "warn": "هشدار",
    "danger": "اشتباه رایج",
    "interview": "سؤالات مصاحبه (با پاسخ)",
    "project": "مینی‌پروژه",
    "exercise": "تمرین",
    "summary": "جمع‌بندی فصل",
    "compare": "مقایسه",
}

FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")

md = MarkdownIt("commonmark", {"html": True, "typographer": False}).enable("table").enable("strikethrough")

PRINT_MODE = "--print" in sys.argv
MAX_CODE_LINES = 42
BOOK_VERSION = "1.0.0"
EDITION = f"نسخه ۲۰۲۶ · ویرایش {BOOK_VERSION.translate(FA_DIGITS)}"
COVER_EDITION = "نسخه ۲۰۲۶"
formatter = HtmlFormatter(nowrap=True, noclasses=True, style="bw" if PRINT_MODE else "monokai")

def render_fence(self, tokens, idx, options, env):
    tok = tokens[idx]
    info = (tok.info or "").strip()
    lang = info.split(" ")[0] if info else "text"
    m = re.search(r'title="([^\"]*)"', info)
    title = m.group(1) if m else ""
    code = tok.content.rstrip("\n")
    try:
        lexer = get_lexer_by_name(lang)
    except Exception:
        lexer = TextLexer()
    body = highlight(code, lexer, formatter)
    body = re.sub(r'<span style="color: #ed007e; background-color: #1E0010">', '<span style="color: #f8f8f2">', body, flags=re.I)
    nlines = code.count("\n") + 1
    cls = "code"
    if nlines > MAX_CODE_LINES:
        raise SystemExit(f"code block '{title or lang}' has {nlines} lines (> {MAX_CODE_LINES}); split it")
    if "nohead" in info:
        return f'<div class="{cls} bare"><pre>{body}</pre></div>\n'
    label = html.escape(title) if title else (lang.upper() if lang != "text" else "")
    head = (
        '<div class="code-head"><span class="dots"><i></i><i></i><i></i></span>'
        f'<span class="fname">{label}</span></div>'
    )
    return f'<div class="{cls}">{head}<pre>{body}</pre></div>\n'

md.add_render_rule("fence", render_fence)

def render_table_open(self, tokens, idx, options, env):
    return '<div class="tbl-wrap"><table>'

def render_table_close(self, tokens, idx, options, env):
    return "</table></div>"

md.add_render_rule("table_open", render_table_open)
md.add_render_rule("table_close", render_table_close)

def render_heading_open(self, tokens, idx, options, env):
    tag = tokens[idx].tag
    if tag in ("h2", "h3"):
        return f'<{tag}><span class="hx"><span class="hx-t">'
    return f"<{tag}>"

def render_heading_close(self, tokens, idx, options, env):
    tag = tokens[idx].tag
    if tag in ("h2", "h3"):
        return f"</span></span></{tag}>\n"
    return f"</{tag}>\n"

md.add_render_rule("heading_open", render_heading_open)
md.add_render_rule("heading_close", render_heading_close)

def convert_tasklists(text: str) -> str:
    lines = text.split("\n")
    out, i = [], 0
    while i < len(lines):
        if re.match(r"^\s*- \[[ xX]\] ", lines[i]):
            out += ['<div class="checklist">', ""]
            while i < len(lines) and re.match(r"^\s*- \[[ xX]\] ", lines[i]):
                out.append(re.sub(r"^(\s*)- \[[ xX]\] ", r"\1- ", lines[i]))
                i += 1
            out += ["", "</div>"]
            continue
        out.append(lines[i]); i += 1
    return "\n".join(out)

def preprocess(text: str) -> str:
    text = convert_tasklists(text)
    out = []
    stack = []
    for line in text.split("\n"):
        m = re.match(r"^:::\s*([a-z]+)(?:\s+(.*))?$", line)
        if m:
            typ, title = m.group(1), (m.group(2) or "").strip()
            if typ == "cols":
                out.append('<div class="cols">')
                out.append("")
                stack.append("cols")
                continue
            if typ == "col":
                cls = "col"
                mm = re.match(r"^(good|bad)\s+(.*)$", title)
                if mm:
                    cls += " " + mm.group(1)
                    title = mm.group(2)
                out.append(f'<div class="{cls}"><div class="col-title">{html.escape(title)}</div>')
                out.append("")
                stack.append("col")
                continue
            if typ == "steps":
                out.append('<div class="steps">')
                out.append("")
                stack.append("steps")
                continue
            title = title or CALLOUT_TITLES.get(typ, "")
            out.append(f'<div class="callout callout-{typ}"><div class="callout-title">{html.escape(title)}</div>')
            out.append("")
            stack.append("callout")
            continue
        if line.strip() == ":::": 
            out.append("")
            out.append("</div>")
            if stack:
                stack.pop()
            continue
        out.append(line)
    return "\n".join(out)

def parse_chapter(path: pathlib.Path):
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    meta = {}
    body = raw
    if m:
        for ln in m.group(1).split("\n"):
            if ":" in ln:
                k, v = ln.split(":", 1)
                meta[k.strip()] = v.strip()
        body = m.group(2)
    meta.setdefault("num", path.stem[:2])
    return meta, body

FIGURE_OPEN = r'<div class="(?:code|tbl-wrap|cols|flow|facts|diagram|steps|shot)[ "]'
_P_BEFORE_FIGURE = re.compile(r'<p>((?:(?!</p>).)*?)</p>(\s*)(?=' + FIGURE_OPEN + ')', re.S)
_P_BEFORE_LIST = re.compile(r'<p>((?:(?!</p>).)*?[:：])</p>(\s*)(?=<(?:ul|ol)[ >])', re.S)
_LIST_BEFORE_FIGURE = re.compile(r'</(ul|ol)>(\s*)(?=' + FIGURE_OPEN + ')')

def keep_with_next(html_body: str) -> str:
    html_body = _P_BEFORE_FIGURE.sub(lambda m: f'<p class="keep-next">{m.group(1)}</p>{m.group(2)}', html_body)
    html_body = _P_BEFORE_LIST.sub(lambda m: f'<p class="keep-next">{m.group(1)}</p>{m.group(2)}', html_body)
    html_body = _LIST_BEFORE_FIGURE.sub(lambda m: f'</{m.group(1)}>{m.group(2)}', html_body)
    html_body = re.sub(r'<li>((?:(?!<li>).)*?)</li>\n</(ul|ol)>(\s*)(?=' + FIGURE_OPEN + ')',
                       lambda m: f'<li class="keep-next">{m.group(1)}</li>\n</{m.group(2)}>{m.group(3)}', html_body, flags=re.S)
    return html_body


def wrap_keep_blocks(html_body: str) -> str:
    """Keep a checklist and the following «فصل بعد» on one page."""
    return re.sub(
        r'(<div class="checklist">[\s\S]*?</div>)\s*(<p><strong>فصل بعد[\s\S]*?</p>)',
        r'<div class="keep-block">\1\2</div>',
        html_body,
    )

def render_chapter(meta, body):
    num = meta["num"]
    cid = f"ch-{num}"
    html_body = wrap_keep_blocks(keep_with_next(md.render(preprocess(body))))
    lead = f'<p class="lead">{md.renderInline(meta["lead"])}</p>' if meta.get("lead") else ""
    title_html = md.renderInline(meta["title"])
    fa_num = str(int(num)).translate(FA_DIGITS)
    run_title = html.escape(meta.get("short") or re.sub(r"<[^>]+>", "", title_html))
    return f"""
<section class="chapter" id="{cid}">
  <div class="chapter-head">
    <span class="chapter-num">{num}</span>
    <h1 class="chapter-title" data-num="{num}" data-label="فصل {fa_num} · {run_title}">{title_html}</h1>
  </div>
  {lead}
  {html_body}
</section>
"""

GIT_MARK = """<svg viewBox="0 0 32 32" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" rx="8" fill="#F05032"/><path fill="#fff" d="M22.4 14.7l-5.1-5.1c-.3-.3-.8-.3-1.1 0l-1.1 1.1 2.2 2.2c.4-.2.9-.1 1.2.3.4.4.5 1 .2 1.5l2.1 2.1c.5-.2 1.1-.1 1.5.3.6.6.6 1.5 0 2.1-.6.6-1.5.6-2.1 0-.4-.4-.5-1.1-.3-1.6l-2.1-2.1v5.2c.1.1.3.2.4.3.6.6.6 1.5 0 2.1-.6.6-1.5.6-2.1 0-.6-.6-.6-1.5 0-2.1.1-.1.3-.3.5-.3v-5.3c-.2-.1-.3-.2-.5-.3-.4-.4-.5-1.1-.3-1.6l-2.2-2.2-5.7 5.7c-.3.3-.3.8 0 1.1l8.4 8.4c.3.3.8.3 1.1 0l8.3-8.3c.3-.3.3-.8 0-1.1z"/></svg>"""


def cover_html():
    return f"""
<section class="cover">
  <div class="cover-inner">
    <div class="cover-kicker">VERSION CONTROL HANDBOOK</div>
    <div class="cover-logos">
      <span class="cover-logo git"><img src="git-icon.svg" alt="Git"/></span>
      <span class="cover-and">&amp;</span>
      <span class="cover-logo gh"><img src="github-mark.svg" alt="GitHub"/></span>
    </div>
    <h1 class="cover-title">مرجع جامع و حرفه‌ای</h1>
    <p class="cover-sub"><span class="ltr">Git</span> و <span class="ltr">GitHub</span> — از صفر تا سطح فوق‌پیشرفته با <span class="ltr">VS Code</span></p>
  </div>
  <div class="cover-author"><div class="cover-author-card">
    <img src="author-sq.png" alt="محمدرضا رضائیان"/>
    <div class="ca-text">
      <div class="ca-name">محمدرضا رضائیان</div>
      <div class="ca-role">نویسنده و گردآورنده</div>
      <div class="ca-tag">مرجع فارسی Git و GitHub برای جامعهٔ توسعه‌دهندگان</div>
    </div>
  </div></div>
  <div class="cover-foot"><div class="cover-foot-row"><span>{COVER_EDITION}</span><span class="ltr">Git 2.51+ · GitHub 2026 · Actions · Rulesets</span></div></div>
</section>
"""


def toc_html(chapters):
    items = []
    cur_part = None
    for meta in chapters:
        p = meta.get("part", "1")
        if p != cur_part:
            cur_part = p
            pn, pt = PARTS[p]
            items.append(f'<div class="toc-part"><span class="toc-part-name">{pn}</span> · {pt}</div>')
        ref = f'#ch-{meta["num"]}'
        items.append(
            f'<a class="toc-item" href="{ref}">'
            f'<span class="toc-row"><span class="toc-num">{meta["num"]}</span>'
            f'<span class="toc-title">{md.renderInline(meta["title"])}</span>'
            f'<span class="toc-leader"></span><span class="toc-page" data-ref="{ref}"></span></span>'
            f'</a>'
        )
    return f"""
<section class="toc">
  <h1 class="toc-heading">فهرست مطالب</h1>
  {''.join(items)}
</section>
"""

def closing_html():
    return f"""
<section class="closing">
  <div class="closing-card">
    <div class="closing-kicker">پایان مرجع</div>
    <h1>حالا تاریخچه را تو می‌نویسی 🚀</h1>
    <p>اگر این کتاب برایتان مفید بود، آن را با تیم‌تان به اشتراک بگذارید. Git فقط فرمان نیست؛ مدل ذهنی زمان، همکاری و کیفیت است.</p>
    <div class="closing-tags"><span>Git 2.51+</span><span>GitHub 2026</span><span>VS Code</span><span>Actions</span><span>Rulesets</span></div>
    <div class="closing-links">
      <div><span class="lbl">گیت‌هاب</span><a class="ltr" href="https://github.com/rezaian-dev">github.com/rezaian-dev</a></div>
      <div><span class="lbl">مرجع JavaScript</span><a class="ltr" href="https://github.com/rezaian-dev/javascript-persian-guide">javascript-persian-guide</a></div>
    </div>
    <div class="closing-author">گردآوری و تدوین حرفه‌ای · {EDITION}</div>
  </div>
</section>
"""

def build(pdf=True):
    t0 = time.time()
    files = sorted(CH_DIR.glob("*.md"))
    chapters = []
    sections = []
    for f in files:
        meta, body = parse_chapter(f)
        chapters.append(meta)
        sections.append(render_chapter(meta, body))
        print(f"  parsed {f.name}: {meta['title']}")

    css = (ROOT / "style.css").read_text(encoding="utf-8")
    if PRINT_MODE:
        css += "\n" + (ROOT / "style-print.css").read_text(encoding="utf-8")
    doc = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head><meta charset="utf-8"/>
<title>مرجع جامع و حرفه‌ای Git و GitHub</title>
<meta name="author" content="محمدرضا رضائیان"/>
<meta name="description" content="مرجع فارسی Git و GitHub ۲۰۲۶ — از صفر تا سطح فوق‌پیشرفته با تمرکز روی VS Code"/>
<meta name="keywords" content="Git, GitHub, VS Code, Persian, فارسی, Actions, edition {BOOK_VERSION}"/>
<style>{css}</style>
</head>
<body>
{cover_html()}
{toc_html(chapters)}
{''.join(sections)}
{closing_html()}
</body></html>"""
    OUT_HTML.parent.mkdir(exist_ok=True)
    OUT_HTML.write_text(doc, encoding="utf-8")
    print(f"HTML written ({len(doc)//1024} KB) in {time.time()-t0:.1f}s")
    if pdf:
        t1 = time.time()
        OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
        out = ROOT / "Git-GitHub-Persian-Guide-Print.pdf" if PRINT_MODE else OUT_PDF
        HTML(string=doc, base_url=str(ROOT)).write_pdf(str(out))
        print(f"PDF written -> {out} in {time.time()-t1:.1f}s")

if __name__ == "__main__":
    build(pdf="--html" not in sys.argv)
