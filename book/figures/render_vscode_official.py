#!/usr/bin/env python3
"""VS Code Git UI on the user's real navy Windows chrome — full window + detail zooms."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = Path(__file__).parent
BASE = Image.open(OUT / "vscode-real-scm.png").convert("RGBA")
W, H = BASE.size

SIDE_L, SIDE_R = 48, 316
ED_L, ED_T, ED_R, ED_B = 317, 36, 1674, 969
ST_T, ST_B = 970, 1002
MSG = (72, 99, 307, 126)
SYNC = (72, 134, 307, 161)
FILES_Y = 172
GRAPH_Y = 930

NAVY = (6, 6, 33, 255)
EDITOR = (0, 0, 31, 255)
TITLE = (16, 25, 44, 255)
MSG_BG = (24, 31, 47, 255)
SYNC_BG = (43, 60, 93, 255)
TEXT = (204, 212, 224, 255)
WHITE = (232, 238, 247, 255)
MUTED = (139, 148, 163, 255)
SEL = (30, 58, 95, 255)
QP_BG = (22, 30, 48, 252)
QP_IN = (30, 38, 56, 255)
ADD_BG = (18, 48, 32, 255)
ADD_FG = (129, 184, 139, 255)
DEL_BG = (58, 22, 26, 255)
DEL_FG = (241, 92, 92, 255)
M_COL = (226, 192, 141, 255)
U_COL = (115, 201, 145, 255)
C_COL = (241, 92, 92, 255)
BLUE = (59, 142, 234, 255)
LINE = (36, 46, 66, 255)
ORANGE = (234, 88, 12, 255)
YELLOW = (240, 198, 80, 255)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def clone():
    return BASE.copy()


def to_rgb(im):
    rgb = Image.new("RGB", im.size, (11, 18, 32))
    if im.mode == "RGBA":
        rgb.paste(im, mask=im.split()[-1])
    else:
        rgb.paste(im)
    return rgb


def save(im, name):
    rgb = to_rgb(im) if im.mode == "RGBA" else im.convert("RGB")
    path = OUT / f"{name}.png"
    rgb.save(path, "PNG", optimize=True)
    print("png", name, rgb.size)
    return rgb


def zoom_save(im, name, box, scale=2.7):
    c = to_rgb(im).crop(box)
    w, h = c.size
    c = c.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
    return save(c, name)


def rr(d, box, fill, r=5, outline=None):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline)


def txt(d, xy, text, f, fill=TEXT):
    d.text(xy, text, font=f, fill=fill)


def fill_editor(im, color=EDITOR):
    ImageDraw.Draw(im).rectangle((ED_L, ED_T, ED_R, ED_B), fill=color)


def fill_sidebar_body(im):
    ImageDraw.Draw(im).rectangle((SIDE_L + 1, FILES_Y, SIDE_R - 1, GRAPH_Y), fill=NAVY)


def set_message(im, message, color=WHITE):
    d = ImageDraw.Draw(im)
    rr(d, MSG, MSG_BG, r=4)
    txt(d, (MSG[0] + 8, MSG[1] + 5), message, font(SANS, 12), color)


def set_button(im, label):
    d = ImageDraw.Draw(im)
    rr(d, SYNC, SYNC_BG, r=4)
    f = font(SANS, 13)
    bbox = d.textbbox((0, 0), label, font=f)
    tw = bbox[2] - bbox[0]
    txt(d, ((SYNC[0] + SYNC[2] - tw) // 2, SYNC[1] + 5), label, f, WHITE)


def file_row(d, y, letter, name, letter_col):
    txt(d, (72, y), name, font(MONO, 12), TEXT)
    txt(d, (SIDE_R - 28, y), letter, font(SANS_B, 12), letter_col)


def set_status(im, branch, sync=""):
    d = ImageDraw.Draw(im)
    d.rectangle((46, ST_T, 420, ST_B), fill=TITLE)
    label = branch if not sync else f"{branch}    {sync}"
    txt(d, (52, ST_T + 8), label, font(SANS, 12), TEXT)


def tab_bar(d, filename):
    d.rectangle((ED_L, ED_T, ED_R, ED_T + 36), fill=(8, 12, 28, 255))
    rr(d, (ED_L + 8, ED_T + 6, ED_L + 8 + 12 * len(filename) + 28, ED_T + 34), (14, 22, 42, 255), r=4)
    txt(d, (ED_L + 18, ED_T + 12), filename, font(SANS, 12), WHITE)


def shadow_panel(im, box, radius=6):
    overlay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(overlay)
    x0, y0, x1, y1 = box
    sd.rounded_rectangle((x0 + 4, y0 + 6, x1 + 8, y1 + 10), radius=radius, fill=(0, 0, 0, 90))
    overlay = overlay.filter(ImageFilter.GaussianBlur(6))
    im.alpha_composite(overlay)
    d = ImageDraw.Draw(im)
    rr(d, box, QP_BG, r=radius, outline=LINE)
    return d


def draw_diff(d, x, y, with_hunk_bar=False):
    if with_hunk_bar:
        txt(d, (x + 12, y), "Stage Change   |   Stage Selected Ranges   |   Discard Change",
            font(SANS, 12), BLUE)
        y += 28
    rows = [
        (MUTED, "    40  export async function login(user: User) {"),
        (MUTED, "    41    const token = await api.sign(user);"),
        (DEL_BG, DEL_FG, "    42    return token;"),
        (ADD_BG, ADD_FG, "    42    return rotateToken(token);"),
        (ADD_BG, ADD_FG, "    43  }"),
        (ADD_BG, ADD_FG, "    44"),
        (ADD_BG, ADD_FG, "    45  export async function rotateToken(t: string) {"),
        (ADD_BG, ADD_FG, "    46    return api.refresh(t);"),
        (MUTED, "    47  }"),
    ]
    f = font(MONO, 14)
    for row in rows:
        if len(row) == 2:
            fill, color, line = None, row[0], row[1]
        else:
            fill, color, line = row
        if fill:
            d.rectangle((x, y - 2, ED_R - 24, y + 20), fill=fill)
        txt(d, (x + 12, y), line, f, color)
        y += 24
    return y


def badge(d, xy, n, scale=1):
    r = int(11 * scale)
    x, y = xy
    d.ellipse((x - r, y - r, x + r, y + r), fill=ORANGE)
    f = font(SANS_B, int(13 * scale))
    s = str(n)
    bb = d.textbbox((0, 0), s, font=f)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    d.text((x - tw / 2, y - th / 2 - 1), s, font=f, fill=(255, 255, 255, 255))


# ---------------------------------------------------------------------------
# Full-window scenes (real chrome)
# ---------------------------------------------------------------------------
save(clone(), "vscode-scm-empty")

im = clone()
set_message(im, "feat(auth): add JWT refresh flow")
set_button(im, "Commit")
fill_sidebar_body(im)
d = ImageDraw.Draw(im)
file_row(d, FILES_Y, "M", "src/auth.ts", M_COL)
file_row(d, FILES_Y + 24, "M", "src/api.ts", M_COL)
file_row(d, FILES_Y + 48, "U", "README.md", U_COL)
fill_editor(im)
d = ImageDraw.Draw(im)
tab_bar(d, "src/auth.ts")
txt(d, (ED_L + 20, ED_T + 48), "WORKING TREE  ·  src/auth.ts", font(SANS, 11), MUTED)
draw_diff(d, ED_L + 8, ED_T + 78)
set_status(im, "feat/auth", "1 ahead")
save(im, "vscode-scm-commit")
COMMIT = im.copy()

im = clone()
d = shadow_panel(im, (420, 86, 1260, 340), radius=8)
rr(d, (436, 102, 1244, 134), QP_IN, r=4)
txt(d, (448, 108), "Select a branch to checkout to...", font(SANS, 13), WHITE)
items = [
    (False, "main"),
    (True, "feat/auth  (current)"),
    (False, "fix/token-expiry"),
    (False, "origin/main"),
    (False, "+ Create new branch from..."),
    (False, "+ Publish Branch..."),
]
y = 148
for sel, label in items:
    if sel:
        d.rectangle((436, y - 4, 1244, y + 22), fill=SEL)
    txt(d, (456, y), label, font(SANS, 13), WHITE if sel else TEXT)
    y += 28
set_status(im, "feat/auth", "1 ahead")
save(im, "vscode-branch-picker")

im = clone()
d = shadow_panel(im, (420, 86, 1260, 300), radius=8)
rr(d, (436, 102, 1244, 134), QP_IN, r=4)
txt(d, (448, 108), "Git: Create Branch from...", font(SANS, 13), WHITE)
d.rectangle((436, 148, 1244, 174), fill=SEL)
txt(d, (456, 152), "main", font(SANS, 13), WHITE)
txt(d, (456, 180), "origin/main", font(SANS, 13), TEXT)
txt(d, (456, 208), "HEAD", font(SANS, 13), TEXT)
rr(d, (436, 244, 1244, 276), QP_IN, r=4)
txt(d, (448, 250), "feat/auth", font(SANS, 13), (156, 220, 254, 255))
save(im, "vscode-create-branch")

im = clone()
set_message(im, "Merge branch 'feat/auth'")
set_button(im, "Commit (merge)")
fill_sidebar_body(im)
d = ImageDraw.Draw(im)
txt(d, (72, FILES_Y), "Merge Changes", font(SANS_B, 12), C_COL)
file_row(d, FILES_Y + 26, "C", "src/auth.ts", C_COL)
fill_editor(im)
d = ImageDraw.Draw(im)
tab_bar(d, "src/auth.ts")
txt(d, (ED_L + 20, ED_T + 48),
    "Accept Current Change   |   Accept Incoming Change   |   Accept Both Changes   |   Compare Changes",
    font(SANS, 12), BLUE)
y = ED_T + 82
f = font(MONO, 14)
for fill, color, line in [
    (DEL_BG, DEL_FG, "<<<<<<< HEAD"),
    (DEL_BG, DEL_FG, "    return token;"),
    (None, MUTED, "======="),
    (ADD_BG, ADD_FG, "    return rotateToken(token);"),
    (ADD_BG, ADD_FG, ">>>>>>> feat/auth"),
]:
    if fill:
        d.rectangle((ED_L + 8, y - 2, ED_R - 24, y + 20), fill=fill)
    txt(d, (ED_L + 20, y), line, f, color)
    y += 26
set_status(im, "main", "merging")
save(im, "vscode-merge-conflict")
CONFLICT = im.copy()

im = clone()
fill_editor(im)
d = ImageDraw.Draw(im)
tab_bar(d, "Graph")
txt(d, (ED_L + 20, ED_T + 48), "SOURCE CONTROL GRAPH   ·   Incoming / Outgoing", font(SANS_B, 12), MUTED)
commits = [
    ((115, 201, 145, 255), "e11f02", "hotfix: empty token", "main"),
    ((156, 220, 254, 255), "9f3a1c", "feat(auth): JWT refresh", "feat/auth  HEAD"),
    ((197, 134, 192, 255), "m7e21a", "Merge pull request #42", ""),
    ((226, 192, 141, 255), "a91b77", "chore: bootstrap", ""),
]
gx, gy = ED_L + 48, ED_T + 88
for i, (col, sha, msg, ref) in enumerate(commits):
    cy = gy + i * 48
    d.ellipse((gx - 8, cy - 8, gx + 8, cy + 8), fill=col)
    if i < len(commits) - 1:
        d.line((gx, cy + 9, gx, cy + 40), fill=col, width=3)
    txt(d, (gx + 28, cy - 9), sha, font(MONO, 14), col)
    txt(d, (gx + 120, cy - 9), msg, font(SANS, 14), WHITE)
    if ref:
        rr(d, (gx + 470, cy - 12, gx + 470 + 10 * len(ref) + 18, cy + 16), (28, 48, 78, 255), r=8)
        txt(d, (gx + 480, cy - 7), ref, font(SANS, 12), BLUE)
txt(d, (ED_L + 20, ED_B - 48),
    "Right-click  ·  Checkout  ·  Cherry Pick  ·  Revert  ·  Create Branch  ·  Reset Current Branch to Here",
    font(SANS, 13), MUTED)
save(im, "vscode-git-graph")
GRAPH = im.copy()

im = clone()
d = ImageDraw.Draw(im)
d.rectangle((SIDE_L + 1, 40, SIDE_R - 1, GRAPH_Y), fill=NAVY)
txt(d, (64, 50), "PULL REQUESTS", font(SANS_B, 12), WHITE)
txt(d, (64, 78), "#42  feat(auth): JWT refresh", font(SANS, 12), BLUE)
txt(d, (64, 100), "Open  ·  3 files  ·  +128  -24", font(SANS, 11), MUTED)
txt(d, (64, 128), "Checks", font(SANS_B, 12), WHITE)
txt(d, (64, 154), "lint", font(SANS, 12), U_COL)
txt(d, (64, 176), "test", font(SANS, 12), U_COL)
txt(d, (64, 198), "build", font(SANS, 12), U_COL)
rr(d, (72, 230, 307, 258), SYNC_BG, r=4)
f = font(SANS, 13)
tb = d.textbbox((0, 0), "Approve", font=f)
txt(d, ((72 + 307 - (tb[2] - tb[0])) // 2, 236), "Approve", f, WHITE)
fill_editor(im)
d = ImageDraw.Draw(im)
tab_bar(d, "src/auth.ts  ·  Pull Request #42")
txt(d, (ED_L + 20, ED_T + 50), "src/auth.ts  ·  line 42", font(MONO, 12), BLUE)
draw_diff(d, ED_L + 8, ED_T + 80)
card = (ED_L + 80, ED_T + 300, ED_L + 620, ED_T + 430)
d = shadow_panel(im, card, radius=6)
txt(d, (card[0] + 16, card[1] + 14), "Comment", font(SANS_B, 12), (197, 134, 192, 255))
txt(d, (card[0] + 16, card[1] + 42), "nit: rename to rotateTokens for plural expiry.", font(SANS, 13), TEXT)
rr(d, (card[0] + 16, card[1] + 84, card[0] + 150, card[1] + 112), SYNC_BG, r=4)
txt(d, (card[0] + 36, card[1] + 90), "Add Comment", font(SANS, 12), WHITE)
set_status(im, "feat/auth", "1 ahead")
save(im, "vscode-pr-ext")

im = clone()
set_message(im, "feat(auth): add JWT refresh flow")
fill_sidebar_body(im)
d = ImageDraw.Draw(im)
file_row(d, FILES_Y, "M", "src/auth.ts", M_COL)
d = shadow_panel(im, (300, 70, 640, 400), radius=6)
rows = [
    "Fetch",
    "Pull",
    "Pull (Rebase)",
    "Push",
    None,
    "Stash  →  Stash (Include Untracked)",
    "Pop Latest Stash",
    None,
    "Commit  →  Undo Last Commit",
    "Discard All Changes",
]
y = 86
for label in rows:
    if label is None:
        d.line((316, y + 4, 624, y + 4), fill=LINE, width=1)
        y += 14
        continue
    color = C_COL if label.startswith("Discard") else TEXT
    txt(d, (320, y), label, font(SANS, 13), color)
    y += 26
set_status(im, "feat/auth", "1 ahead")
save(im, "vscode-stash-sync")
MENU = im.copy()

im = clone()
d = ImageDraw.Draw(im)
d.rectangle((SIDE_L + 1, 40, SIDE_R - 1, GRAPH_Y), fill=NAVY)
txt(d, (64, 50), "EXPLORER", font(SANS_B, 12), WHITE)
txt(d, (64, 82), "src/auth.ts", font(MONO, 12), BLUE)
txt(d, (64, 104), "src/api.ts", font(MONO, 12), TEXT)
txt(d, (64, 126), "README.md", font(MONO, 12), TEXT)
txt(d, (64, 168), "TIMELINE  ·  auth.ts", font(SANS_B, 11), MUTED)
txt(d, (64, 196), "9f3a1c  feat(auth): JWT refresh", font(SANS, 12), U_COL)
txt(d, (64, 216), "today 11:42  ·  Git", font(SANS, 11), MUTED)
txt(d, (64, 244), "Local History  ·  11:18", font(SANS, 12), BLUE)
txt(d, (64, 264), "unsaved edit", font(SANS, 11), MUTED)
fill_editor(im)
d = ImageDraw.Draw(im)
tab_bar(d, "src/auth.ts")
draw_diff(d, ED_L + 8, ED_T + 56)
save(im, "vscode-timeline")

# Initialize (no repo)
im = clone()
d = ImageDraw.Draw(im)
d.rectangle((SIDE_L + 1, 40, SIDE_R - 1, GRAPH_Y), fill=NAVY)
txt(d, (64, 52), "SOURCE CONTROL", font(SANS_B, 12), WHITE)
txt(d, (64, 88), "The folder currently open doesn't", font(SANS, 11), MUTED)
txt(d, (64, 106), "have a Git repository.", font(SANS, 11), MUTED)
rr(d, (72, 140, 307, 172), SYNC_BG, r=4)
txt(d, (92, 148), "Initialize Repository", font(SANS, 12), WHITE)
rr(d, (72, 184, 307, 216), (28, 48, 78, 255), r=4)
txt(d, (98, 192), "Publish to GitHub", font(SANS, 12), WHITE)
txt(d, (64, 240), "Or open a folder that already", font(SANS, 11), MUTED)
txt(d, (64, 258), "contains a .git directory.", font(SANS, 11), MUTED)
save(im, "vscode-scm-init")
INIT = im.copy()

# Staged vs Changes
im = clone()
set_message(im, "feat(auth): add JWT refresh flow")
set_button(im, "Commit")
fill_sidebar_body(im)
d = ImageDraw.Draw(im)
txt(d, (72, FILES_Y), "Staged Changes", font(SANS_B, 12), WHITE)
file_row(d, FILES_Y + 24, "M", "src/auth.ts", M_COL)
txt(d, (72, FILES_Y + 58), "Changes", font(SANS_B, 12), WHITE)
file_row(d, FILES_Y + 82, "M", "src/api.ts", M_COL)
file_row(d, FILES_Y + 106, "U", "README.md", U_COL)
fill_editor(im)
d = ImageDraw.Draw(im)
tab_bar(d, "src/auth.ts")
txt(d, (ED_L + 20, ED_T + 48), "INDEX  ·  staged  ·  src/auth.ts", font(SANS, 11), MUTED)
draw_diff(d, ED_L + 8, ED_T + 78)
set_status(im, "feat/auth", "1 ahead")
save(im, "vscode-scm-staged")
STAGED = im.copy()

# Hunk staging
im = clone()
set_message(im, "feat(auth): add JWT refresh flow")
set_button(im, "Commit")
fill_sidebar_body(im)
d = ImageDraw.Draw(im)
file_row(d, FILES_Y, "M", "src/auth.ts", M_COL)
fill_editor(im)
d = ImageDraw.Draw(im)
tab_bar(d, "src/auth.ts")
draw_diff(d, ED_L + 8, ED_T + 52, with_hunk_bar=True)
set_status(im, "feat/auth")
save(im, "vscode-scm-hunk")
HUNK = im.copy()

# Commit dropdown
im = clone()
set_message(im, "feat(auth): add JWT refresh flow")
set_button(im, "Commit  ▾")
fill_sidebar_body(im)
d = ImageDraw.Draw(im)
file_row(d, FILES_Y, "M", "src/auth.ts", M_COL)
d = shadow_panel(im, (72, 168, 340, 340), radius=6)
for i, (lab, col) in enumerate([
    ("Commit", WHITE),
    ("Commit & Push", TEXT),
    ("Commit & Sync", TEXT),
    ("Undo Last Commit", TEXT),
    ("Amend", TEXT),
]):
    yy = 180 + i * 28
    if i == 0:
        d.rectangle((80, yy - 4, 332, yy + 20), fill=SEL)
    txt(d, (92, yy), lab, font(SANS, 13), col)
save(im, "vscode-scm-commit-menu")
CMENU = im.copy()

# Rebase in progress
im = clone()
fill_sidebar_body(im)
d = ImageDraw.Draw(im)
txt(d, (72, FILES_Y), "Rebase in progress", font(SANS_B, 12), YELLOW)
file_row(d, FILES_Y + 26, "C", "src/auth.ts", C_COL)
rr(d, (72, FILES_Y + 60, 180, FILES_Y + 88), SYNC_BG, r=4)
txt(d, (88, FILES_Y + 66), "Continue", font(SANS, 12), WHITE)
rr(d, (190, FILES_Y + 60, 300, FILES_Y + 88), (58, 22, 26, 255), r=4)
txt(d, (214, FILES_Y + 66), "Abort", font(SANS, 12), C_COL)
fill_editor(im)
d = ImageDraw.Draw(im)
d.rectangle((ED_L, ED_T, ED_R, ED_T + 36), fill=(64, 48, 12, 255))
txt(d, (ED_L + 16, ED_T + 10), "Rebasing feat/auth onto origin/main   ·   resolve conflicts, then Continue",
    font(SANS, 13), YELLOW)
tab_bar = None
txt(d, (ED_L + 20, ED_T + 52),
    "Accept Current Change   |   Accept Incoming Change   |   Accept Both Changes",
    font(SANS, 12), BLUE)
y = ED_T + 86
for fill, color, line in [
    (DEL_BG, DEL_FG, "<<<<<<< HEAD"),
    (DEL_BG, DEL_FG, "    return token;"),
    (None, MUTED, "======="),
    (ADD_BG, ADD_FG, "    return rotateToken(token);"),
    (ADD_BG, ADD_FG, ">>>>>>> origin/main"),
]:
    if fill:
        d.rectangle((ED_L + 8, y - 2, ED_R - 24, y + 20), fill=fill)
    txt(d, (ED_L + 20, y), line, font(MONO, 14), color)
    y += 26
set_status(im, "feat/auth", "REBASING")
save(im, "vscode-scm-rebase")
REBASE = im.copy()

# Multi-repo SCM
im = clone()
d = ImageDraw.Draw(im)
d.rectangle((SIDE_L + 1, 40, SIDE_R - 1, GRAPH_Y), fill=NAVY)
txt(d, (64, 50), "SOURCE CONTROL", font(SANS_B, 12), WHITE)
txt(d, (64, 78), "REPOSITORIES", font(SANS, 11), MUTED)
txt(d, (64, 104), "v  git-lab     feat/auth", font(SANS, 12), WHITE)
txt(d, (80, 126), "M  src/auth.ts", font(MONO, 12), M_COL)
txt(d, (64, 160), ">  docs-site   main", font(SANS, 12), MUTED)
txt(d, (64, 184), ">  hotfix-500  hotfix/500", font(SANS, 12), MUTED)
txt(d, (64, 220), "Each folder is its own Git repo.", font(SANS, 11), MUTED)
txt(d, (64, 238), "Worktrees appear as extra roots.", font(SANS, 11), MUTED)
save(im, "vscode-scm-multirepo")
MULTI = im.copy()

# ---------------------------------------------------------------------------
# Detail zooms — these fill the PDF width so SCM text is readable
# ---------------------------------------------------------------------------
# Anatomy of real empty SCM (top of panel + git icon)
an = clone()
d = ImageDraw.Draw(an)
# badges in original coordinates (before zoom)
badge(d, (28, 148), 1)     # activity git
badge(d, (300, 52), 2)     # Source Control title
badge(d, (300, 112), 3)    # message
badge(d, (300, 148), 4)    # Sync Changes
zoom_save(an, "vscode-scm-anatomy", (0, 32, 340, 220), scale=3.05)

zoom_save(clone(), "vscode-scm-empty-zoom", (0, 32, 340, 200), scale=3.05)
zoom_save(COMMIT, "vscode-scm-commit-zoom", (0, 32, 980, 380), scale=2.15)
zoom_save(STAGED, "vscode-scm-staged-zoom", (48, 36, 316, 320), scale=2.9)
zoom_save(HUNK, "vscode-scm-hunk-zoom", (317, 36, 1400, 360), scale=1.85)
zoom_save(CMENU, "vscode-scm-commit-menu-zoom", (48, 36, 360, 360), scale=2.7)
zoom_save(MENU, "vscode-scm-menu-zoom", (48, 36, 660, 430), scale=2.15)
zoom_save(CONFLICT, "vscode-scm-conflict-zoom", (48, 36, 1280, 320), scale=1.85)
zoom_save(GRAPH, "vscode-scm-graph-zoom", (317, 36, 1500, 360), scale=1.85)
zoom_save(INIT, "vscode-scm-init-zoom", (48, 36, 316, 300), scale=2.9)
zoom_save(REBASE, "vscode-scm-rebase-zoom", (48, 36, 1280, 340), scale=1.85)
zoom_save(MULTI, "vscode-scm-multirepo-zoom", (48, 36, 316, 280), scale=2.9)
zoom_save(clone(), "vscode-scm-status-zoom", (0, 958, 620, 1004), scale=3.2)

print("done")
