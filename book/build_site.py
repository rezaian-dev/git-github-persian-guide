#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate GitHub Pages assets: banners, previews, online book copy."""
from __future__ import annotations

import io
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont
import cairosvg
import pypdfium2 as pdfium

from reader_select import READER_JS, new_nav

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
DOCS = REPO / "docs"
ASSETS = DOCS / "assets"
WEB = ASSETS / "web"
BOOK = DOCS / "book"
PDF = DOCS / "pdf" / "Git-GitHub-Persian-Guide.pdf"
JS_FONTS = Path("/home/user/javascript-persian-guide/docs/assets/fonts")


def svg_png(path: Path, size: int) -> Image.Image:
    data = cairosvg.svg2png(url=str(path), output_width=size, output_height=size)
    im = Image.open(io.BytesIO(data)).convert("RGBA")
    return im


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def rounded(im: Image.Image, radius: int) -> Image.Image:
    mask = Image.new("L", im.size, 0)
    d = ImageDraw.Draw(mask)
    d.rounded_rectangle((0, 0, im.size[0] - 1, im.size[1] - 1), radius, fill=255)
    out = im.copy()
    out.putalpha(mask)
    return out


def draw_dag(draw: ImageDraw.ImageDraw, w: int, h: int) -> None:
    nodes = [
        (int(w * 0.10), int(h * 0.72), 7),
        (int(w * 0.22), int(h * 0.58), 8),
        (int(w * 0.34), int(h * 0.70), 7),
        (int(w * 0.46), int(h * 0.48), 9),
        (int(w * 0.58), int(h * 0.62), 8),
        (int(w * 0.70), int(h * 0.42), 7),
        (int(w * 0.82), int(h * 0.55), 8),
        (int(w * 0.90), int(h * 0.38), 6),
    ]
    edges = [(0, 1), (1, 2), (1, 3), (3, 4), (3, 5), (5, 6), (6, 7), (4, 6)]
    for a, b in edges:
        x1, y1, _ = nodes[a]
        x2, y2, _ = nodes[b]
        draw.line((x1, y1, x2, y2), fill=(240, 80, 50, 55), width=2)
    for x, y, r in nodes:
        draw.ellipse((x - r, y - r, x + r, y + r), fill=(240, 80, 50, 160), outline=(253, 186, 116, 200), width=2)


def make_hero() -> None:
    """Compact README banner — 1280×400 (introductory, not a book cover)."""
    w, h = 1280, 400
    im = Image.new("RGB", (w, h), "#070b14")
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    # glows
    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((-180, -220, 420, 280), fill=(240, 80, 50, 70))
    gd.ellipse((860, -80, 1480, 420), fill=(88, 166, 255, 50))
    glow = glow.filter(ImageFilter.GaussianBlur(70))
    overlay = Image.alpha_composite(overlay, glow)
    d = ImageDraw.Draw(overlay)
    # grid
    for x in range(0, w, 48):
        d.line((x, 0, x, h), fill=(148, 163, 184, 18), width=1)
    for y in range(0, h, 48):
        d.line((0, y, w, y), fill=(148, 163, 184, 18), width=1)
    draw_dag(d, w, h)

    git = svg_png(ROOT / "git-icon.svg", 220)
    gh = svg_png(ROOT / "github-mark.svg", 200)
    # GitHub mark is black — put on white-ish disk
    git_badge = Image.new("RGBA", (132, 132), (0, 0, 0, 0))
    bd = ImageDraw.Draw(git_badge)
    bd.rounded_rectangle((0, 0, 131, 131), 32, fill=(255, 255, 255, 255))
    git_r = git.resize((88, 88), Image.Resampling.LANCZOS)
    git_badge.alpha_composite(git_r, (22, 22))
    gh_badge = Image.new("RGBA", (132, 132), (0, 0, 0, 0))
    bd = ImageDraw.Draw(gh_badge)
    bd.rounded_rectangle((0, 0, 131, 131), 32, fill=(1, 4, 9, 255), outline=(255, 255, 255, 40), width=2)
    # invertocat may be black; composite white version
    gh_w = Image.new("RGBA", gh.size, (255, 255, 255, 0))
    px = gh.load()
    wp = gh_w.load()
    for y in range(gh.size[1]):
        for x in range(gh.size[0]):
            r, g, b, a = px[x, y]
            if a > 8:
                wp[x, y] = (255, 255, 255, a)
    gh_r = gh_w.resize((78, 78), Image.Resampling.LANCZOS)
    gh_badge.alpha_composite(gh_r, (27, 27))

    overlay.alpha_composite(git_badge, (72, 134))
    overlay.alpha_composite(gh_badge, (228, 134))
    d = ImageDraw.Draw(overlay)
    d.ellipse((196, 186, 216, 206), fill=(7, 11, 20, 255), outline=(251, 146, 60, 255), width=3)
    d.line((198, 196, 214, 196), fill=(251, 146, 60, 255), width=3)

    jb_reg = ROOT / "fonts" / "JetBrainsMono-Regular.ttf"
    jb_bold = ROOT / "fonts" / "JetBrainsMono-Bold.ttf"
    vz_bold = ROOT / "fonts" / "Vazirmatn-ExtraBold.ttf"
    d.text((400, 78), "PERSIAN DEVELOPER HANDBOOK", font=font(jb_reg, 18), fill=(253, 186, 116, 255))
    d.text((400, 118), "Git  &  GitHub  2026", font=font(jb_bold, 54), fill=(248, 250, 252, 255))
    d.text((400, 192), "Zero → staff-level  ·  CLI  ·  VS Code Source Control", font=font(jb_reg, 22), fill=(203, 213, 225, 255))

    # metric chips
    chips = ["36 chapters", "PDF + EPUB", "Online edition", "CC BY-NC-SA 4.0"]
    x = 400
    y = 250
    fchip = font(jb_reg, 15)
    for label in chips:
        bbox = d.textbbox((0, 0), label, font=fchip)
        tw = bbox[2] - bbox[0]
        d.rounded_rectangle((x, y, x + tw + 28, y + 34), 17, fill=(15, 23, 42, 210), outline=(240, 80, 50, 140), width=1)
        d.text((x + 14, y + 8), label, font=fchip, fill=(248, 250, 252, 255))
        x += tw + 40

    d.text((400, 318), "github.com/rezaian-dev/git-github-persian-guide", font=font(jb_reg, 16), fill=(148, 163, 184, 255))

    out = Image.alpha_composite(im.convert("RGBA"), overlay).convert("RGB")
    WEB.mkdir(parents=True, exist_ok=True)
    webp = WEB / "readme-hero.webp"
    out.save(webp, "WEBP", quality=88, method=6)
    out.save(ASSETS / "readme-hero.jpg", "JPEG", quality=90, optimize=True)
    print("hero", webp, out.size)


def make_social() -> None:
    """GitHub social preview — 1280×640 per docs.github.com."""
    w, h = 1280, 640
    im = Image.new("RGB", (w, h), "#070b14")
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((-200, -240, 520, 360), fill=(240, 80, 50, 80))
    gd.ellipse((740, 80, 1500, 780), fill=(88, 166, 255, 55))
    glow = glow.filter(ImageFilter.GaussianBlur(80))
    overlay = Image.alpha_composite(overlay, glow)
    d = ImageDraw.Draw(overlay)
    for x in range(0, w, 56):
        d.line((x, 0, x, h), fill=(148, 163, 184, 16), width=1)
    for y in range(0, h, 56):
        d.line((0, y, w, y), fill=(148, 163, 184, 16), width=1)
    draw_dag(d, w, h)

    git = svg_png(ROOT / "git-icon.svg", 280)
    gh = svg_png(ROOT / "github-mark.svg", 240)
    git_badge = Image.new("RGBA", (168, 168), (0, 0, 0, 0))
    bd = ImageDraw.Draw(git_badge)
    bd.rounded_rectangle((0, 0, 167, 167), 40, fill=(255, 255, 255, 255))
    git_badge.alpha_composite(git.resize((112, 112), Image.Resampling.LANCZOS), (28, 28))
    gh_badge = Image.new("RGBA", (168, 168), (0, 0, 0, 0))
    bd = ImageDraw.Draw(gh_badge)
    bd.rounded_rectangle((0, 0, 167, 167), 40, fill=(1, 4, 9, 255), outline=(255, 255, 255, 45), width=2)
    gh_w = Image.new("RGBA", gh.size, (255, 255, 255, 0))
    px, wp = gh.load(), gh_w.load()
    for y in range(gh.size[1]):
        for x in range(gh.size[0]):
            r, g, b, a = px[x, y]
            if a > 8:
                wp[x, y] = (255, 255, 255, a)
    gh_badge.alpha_composite(gh_w.resize((100, 100), Image.Resampling.LANCZOS), (34, 34))
    overlay.alpha_composite(git_badge, (96, 210))
    overlay.alpha_composite(gh_badge, (292, 210))

    jb_reg = ROOT / "fonts" / "JetBrainsMono-Regular.ttf"
    jb_bold = ROOT / "fonts" / "JetBrainsMono-Bold.ttf"
    d.text((96, 88), "rezaian-dev  ·  open handbook", font=font(jb_reg, 22), fill=(253, 186, 116, 255))
    d.text((520, 188), "Git & GitHub", font=font(jb_bold, 72), fill=(248, 250, 252, 255))
    d.text((520, 278), "Persian handbook  ·  2026 edition", font=font(jb_reg, 28), fill=(226, 232, 240, 255))
    d.text((520, 338), "CLI  ·  VS Code Source Control  ·  Actions  ·  Rulesets", font=font(jb_reg, 20), fill=(148, 163, 184, 255))
    d.rounded_rectangle((520, 400, 760, 446), 12, fill=(240, 80, 50, 255))
    d.text((546, 412), "36 chapters  ·  free", font=font(jb_bold, 18), fill=(255, 255, 255, 255))
    d.rounded_rectangle((776, 400, 1048, 446), 12, outline=(148, 163, 184, 90), width=2)
    d.text((798, 412), "PDF  ·  EPUB  ·  HTML", font=font(jb_reg, 18), fill=(226, 232, 240, 255))

    out = Image.alpha_composite(im.convert("RGBA"), overlay).convert("RGB")
    ASSETS.mkdir(parents=True, exist_ok=True)
    dest = ASSETS / "social-card.jpg"
    out.save(dest, "JPEG", quality=90, optimize=True)
    print("social", dest, out.size, dest.stat().st_size)


def make_cover_hero() -> None:
    src = Image.open(ROOT / "cover-bg.jpg").convert("RGB")
    # book cover ratio ~ 0.7
    WEB.mkdir(parents=True, exist_ok=True)
    for w, name in ((864, "cover-hero.webp"), (720, "cover-hero-720.webp"), (480, "cover-hero-480.webp")):
        h = int(w * src.size[1] / src.size[0])
        im = src.resize((w, h), Image.Resampling.LANCZOS)
        im.save(WEB / name, "WEBP", quality=86, method=6)
        print("cover", name, im.size)


def make_author() -> None:
    src = Image.open(ROOT / "author-sq.png").convert("RGB")
    im = src.resize((320, 320), Image.Resampling.LANCZOS)
    WEB.mkdir(parents=True, exist_ok=True)
    im.save(WEB / "author.webp", "WEBP", quality=85, method=6)


def make_favicon() -> None:
    git = svg_png(ROOT / "git-icon.svg", 128)
    bg = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
    d = ImageDraw.Draw(bg)
    d.rounded_rectangle((0, 0, 127, 127), 28, fill=(255, 255, 255, 255))
    g = git.resize((92, 92), Image.Resampling.LANCZOS)
    bg.alpha_composite(g, (18, 18))
    for s in (32, 64, 128):
        bg.resize((s, s), Image.Resampling.LANCZOS).save(ASSETS / f"git-logo-{s}.png")


def make_previews() -> None:
    doc = pdfium.PdfDocument(str(PDF))
    # cover, toc, a VS Code chapter page, a code-ish chapter, workshop-ish
    picks = {
        "preview-cover": 0,
        "preview-toc": 1,
        "preview-chapter": 8,
        "preview-code": 18,
        "preview-workshop": min(len(doc) - 3, 130),
    }
    WEB.mkdir(parents=True, exist_ok=True)
    (ASSETS).mkdir(parents=True, exist_ok=True)
    for name, idx in picks.items():
        page = doc[idx]
        bitmap = page.render(scale=1.35)
        im = bitmap.to_pil().convert("RGB")
        jpg = ASSETS / f"page-{name.replace('preview-', '')}.jpg"
        im.save(jpg, "JPEG", quality=82, optimize=True)
        thumb = im.copy()
        thumb.thumbnail((420, 600), Image.Resampling.LANCZOS)
        thumb.save(WEB / f"{name}.webp", "WEBP", quality=80, method=6)
        print("preview", name, "page", idx + 1, thumb.size)


def copy_fonts() -> None:
    dest = ASSETS / "fonts"
    dest.mkdir(parents=True, exist_ok=True)
    for f in JS_FONTS.glob("*.woff2"):
        shutil.copy2(f, dest / f.name)
    if (JS_FONTS / "OFL.txt").exists():
        shutil.copy2(JS_FONTS / "OFL.txt", dest / "OFL.txt")


def copy_book() -> None:
    html_src = ROOT / "build" / "book.html"
    if not html_src.exists():
        print("skip book copy; run build.py --html first")
        return
    if BOOK.exists():
        shutil.rmtree(BOOK)
    BOOK.mkdir(parents=True)
    html = html_src.read_text(encoding="utf-8")
    web_css = (ROOT / "style-web.css").read_text(encoding="utf-8") + SELECT_CSS
    nav = new_nav(html)
    html = html.replace("<body>", "<body class=\"web-edition\">" + nav, 1)
    html = html.replace("</head>", f"<style>{web_css}</style>\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n</head>", 1)
    html = html.replace("</body>", f"<script>{READER_JS}</script>\n</body>", 1)
    (BOOK / "index.html").write_text(html, encoding="utf-8")
    for name in ("cover-bg.jpg", "git-icon.svg", "github-mark.svg", "author-sq.png"):
        shutil.copy2(ROOT / name, BOOK / name)
    shutil.copytree(ROOT / "fonts", BOOK / "fonts")
    fig_dest = BOOK / "figures"
    fig_dest.mkdir()
    used = set()
    for p in (ROOT / "chapters").glob("*.md"):
        text = p.read_text(encoding="utf-8")
        for line in text.splitlines():
            if "src=\"figures/" in line:
                fname = line.split("src=\"figures/")[1].split('"')[0]
                used.add(fname)
    for fname in used:
        src = ROOT / "figures" / fname
        if src.exists():
            shutil.copy2(src, fig_dest / fname)
    print("book copied", (BOOK / "index.html").stat().st_size, "figures", len(used))


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    WEB.mkdir(parents=True, exist_ok=True)
    make_hero()
    make_social()
    make_cover_hero()
    make_author()
    make_favicon()
    make_previews()
    copy_fonts()
    copy_book()


if __name__ == "__main__":
    main()
