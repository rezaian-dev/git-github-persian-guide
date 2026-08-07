#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The chapter selector (فهرست فصل‌ها) for the online edition's web bar.

A shadcn/ui Select, rebuilt in vanilla CSS/JS so the static HTML edition can
carry it: a trigger with the chapter placeholder, a popover grouped by part
with a check on the active chapter, full keyboard support (arrows, Home/End,
Enter, Escape) and outside-pointer close. `chapter_select()` derives the items
from the book's own print TOC markup, so the print TOC stays the single source
of truth and the two can never disagree.
"""
from __future__ import annotations

import re

SELECT_CSS = """
/* --- chapter select (shadcn/ui Select, vanilla) --- */
html { scroll-padding-top: 70px; }
.bar-c { display: flex; align-items: center; gap: 10px; min-width: 0; }
.select { position: relative; }
.select-trigger { display: inline-flex; align-items: center; gap: 8px; min-height: 36px; padding: 7px 11px;
  font-family: inherit; font-size: 12.5px; font-weight: 700; color: #e2e8f0; cursor: pointer;
  background: #16223a; border: 1px solid rgba(255, 255, 255, .16); border-radius: 9px;
  transition: color .16s, border-color .16s }
.select-trigger:hover { color: #fff; border-color: rgba(249, 115, 22, .65) }
.select-trigger[aria-expanded="true"] { color: #fff; border-color: #f97316 }
.select-value { max-width: 210px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap }
.select-value.ph { color: #94a3b8; font-weight: 600 }
.select-chevron { width: 15px; height: 15px; flex-shrink: 0; opacity: .75; transition: transform .18s }
.select-trigger[aria-expanded="true"] .select-chevron { transform: rotate(180deg) }
.select-pop { position: absolute; top: calc(100% + 8px); inset-inline-start: 0; z-index: 120;
  width: min(380px, 88vw); max-height: min(64vh, 500px); overflow-y: auto; overscroll-behavior: contain;
  padding: 6px; border: 1px solid rgba(255, 255, 255, .14); border-radius: 13px; background: #0f172a;
  box-shadow: 0 26px 64px rgba(2, 6, 23, .5); animation: pop .16s ease }
.select-pop[hidden] { display: none }
.select-pop::-webkit-scrollbar { width: 8px }
.select-pop::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, .16); border-radius: 8px }
@keyframes pop { from { opacity: 0; transform: translateY(-6px) scale(.98) } to { opacity: 1; transform: none } }
.select-label { padding: 9px 10px 4px; font-size: 11px; font-weight: 800; letter-spacing: .03em; color: #fb923c }
.select-item { display: grid; grid-template-columns: auto 1fr auto; align-items: center; gap: 9px;
  padding: 8px 10px; border-radius: 8px; cursor: pointer; font-size: 13px; font-weight: 600; color: #cbd5e1 }
.select-item .n { font-family: var(--mono, ui-monospace, monospace); font-size: 10.5px; font-weight: 700; color: #fdba74 }
.select-item .t { min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap }
.select-item .t .ltr { display: inline }
.select-item .check { width: 15px; height: 15px; visibility: hidden; color: #fb923c }
.select-item.hl { background: rgba(255, 255, 255, .08); color: #fff }
.select-item[aria-selected="true"] { color: #fff }
.select-item[aria-selected="true"] .check { visibility: visible }
@media (max-width: 640px) { .select { display: none } }
"""

READER_JS = """(() => {
  const root = document.getElementById('jump');
  if (!root) return;
  const trigger = root.querySelector('.select-trigger');
  const value = root.querySelector('.select-value');
  const pop = root.querySelector('.select-pop');
  const items = [...root.querySelectorAll('.select-item')];
  let hl = -1;
  const setHl = (i) => {
    hl = i;
    items.forEach((it, k) => it.classList.toggle('hl', k === i));
    if (i >= 0) {
      // scroll the highlighted row inside the popover only — never the page
      const el = items[i], t = el.offsetTop, b = t + el.offsetHeight;
      if (t < pop.scrollTop) pop.scrollTop = t - 8;
      else if (b > pop.scrollTop + pop.clientHeight) pop.scrollTop = b - pop.clientHeight + 8;
    }
  };
  const setOpen = (o) => {
    pop.hidden = !o;
    trigger.setAttribute('aria-expanded', o ? 'true' : 'false');
    if (o) {
      const cur = items.findIndex((it) => it.getAttribute('aria-selected') === 'true');
      setHl(cur >= 0 ? cur : 0);
    } else setHl(-1);
  };
  const pick = (it) => {
    items.forEach((o) => o.setAttribute('aria-selected', o === it ? 'true' : 'false'));
    value.textContent = it.querySelector('.t').textContent;
    value.classList.remove('ph');
    setOpen(false);
    trigger.focus();
    history.replaceState(null, '', it.dataset.value);
    document.querySelector(it.dataset.value)?.scrollIntoView({ block: 'start' });
  };
  trigger.addEventListener('click', () => setOpen(pop.hidden));
  items.forEach((it) => {
    it.addEventListener('click', () => pick(it));
    it.addEventListener('mousemove', () => setHl(items.indexOf(it)));
  });
  document.addEventListener('pointerdown', (e) => {
    if (!pop.hidden && !root.contains(e.target)) setOpen(false);
  });
  document.addEventListener('keydown', (e) => {
    if (pop.hidden) {
      if ((e.key === 'ArrowDown' || e.key === 'ArrowUp') && document.activeElement === trigger) {
        e.preventDefault(); setOpen(true);
      }
      return;
    }
    if (e.key === 'Escape') { setOpen(false); trigger.focus(); }
    else if (e.key === 'ArrowDown') { e.preventDefault(); setHl((hl + 1) % items.length); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); setHl((hl - 1 + items.length) % items.length); }
    else if (e.key === 'Home') { e.preventDefault(); setHl(0); }
    else if (e.key === 'End') { e.preventDefault(); setHl(items.length - 1); }
    else if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); if (items[hl]) pick(items[hl]); }
  });
})();"""

FA = "۰۱۲۳۴۵۶۷۸۹"

OLD_NAV = """
<nav class="web-bar" aria-label="نوار نسخه آنلاین">
  <a href="../">بازگشت به سایت</a>
  <span>نسخه آنلاین HTML · ویرایش ۱.۰.۰</span>
  <a href="../pdf/Git-GitHub-Persian-Guide.pdf">دانلود PDF</a>
</nav>
"""


def fa_num(s: str) -> str:
    return "".join(FA[int(c)] if c.isdigit() else c for c in s)


def chapter_select(html: str) -> str:
    """Derive the grouped select items from the book's own print TOC markup."""
    out: list[str] = []
    chunks = re.split(
        r'<div class="toc-part"><span class="toc-part-name">(.*?)</span>\s*·\s*(.*?)</div>', html
    )
    for i in range(1, len(chunks) - 2, 3):
        pname, psub, body = chunks[i], chunks[i + 1], chunks[i + 2]
        out.append(f'<div class="select-label">{pname} · {psub}</div>')
        for m in re.finditer(
            r'<a class="toc-item" href="#(ch-\d+)"><span class="toc-row">'
            r'<span class="toc-num">(\d+)</span><span class="toc-title">(.*?)</span><span class="toc-leader">',
            body,
        ):
            href, num, title = m.group(1), m.group(2), m.group(3)
            out.append(
                f'<div class="select-item" role="option" id="jump-{href}" data-value="#{href}" aria-selected="false">'
                f'<span class="n">{fa_num(num)}</span><span class="t">{title}</span>'
                f'<svg class="check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" '
                f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg></div>'
            )
    return "".join(out)


def new_nav(html: str) -> str:
    """The web bar with the chapter select between the two links."""
    return f"""
<nav class="web-bar" aria-label="نوار نسخه آنلاین">
  <a href="../">بازگشت به سایت</a>
  <div class="bar-c">
    <div class="select" id="jump">
      <button type="button" class="select-trigger" aria-haspopup="listbox" aria-expanded="false" aria-label="پرش به فصل">
        <span class="select-value ph">فهرست فصل‌ها…</span>
        <svg class="select-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
      </button>
      <div class="select-pop" role="listbox" aria-label="پرش به فصل" hidden>{chapter_select(html)}</div>
    </div>
    <span>نسخه آنلاین HTML · ویرایش ۱.۰.۰</span>
  </div>
  <a href="../pdf/Git-GitHub-Persian-Guide.pdf">دانلود PDF</a>
</nav>
"""


def transform(html: str) -> str:
    """Apply the whole overlay to a built book.html: bar, css and js."""
    assert OLD_NAV in html, "web-bar block not found"
    html = html.replace(OLD_NAV, new_nav(html), 1)
    html = html.replace("</head>", f"<style>{SELECT_CSS}</style>\n</head>", 1)
    html = html.replace("</body>", f"<script>{READER_JS}</script>\n</body>", 1)
    return html
