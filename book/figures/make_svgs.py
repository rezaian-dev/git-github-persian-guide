#!/usr/bin/env python3
"""Crisp technical diagrams for the Git & GitHub Persian Guide."""
from pathlib import Path

OUT = Path(__file__).parent


def save(name: str, svg: str) -> None:
    (OUT / name).write_text(svg.strip() + "\n", encoding="utf-8")
    print("wrote", name)


save(
    "three-trees.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 280" width="860" height="280">
  <defs>
    <linearGradient id="g1" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#fff7ed"/><stop offset="100%" stop-color="#ffedd5"/>
    </linearGradient>
    <linearGradient id="g2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ecfeff"/><stop offset="100%" stop-color="#cffafe"/>
    </linearGradient>
    <linearGradient id="g3" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f0fdf4"/><stop offset="100%" stop-color="#dcfce7"/>
    </linearGradient>
  </defs>
  <rect width="860" height="280" rx="18" fill="#0f172a"/>
  <text x="430" y="36" text-anchor="middle" fill="#fdba74" font-family="DejaVu Sans, sans-serif" font-size="15" font-weight="700">Git three trees</text>
  <!-- boxes -->
  <rect x="40" y="64" width="220" height="170" rx="14" fill="url(#g1)" stroke="#fb923c" stroke-width="2"/>
  <rect x="320" y="64" width="220" height="170" rx="14" fill="url(#g2)" stroke="#22d3ee" stroke-width="2"/>
  <rect x="600" y="64" width="220" height="170" rx="14" fill="url(#g3)" stroke="#4ade80" stroke-width="2"/>
  <text x="150" y="94" text-anchor="middle" fill="#9a3412" font-family="DejaVu Sans, sans-serif" font-size="16" font-weight="700">1. Working Tree</text>
  <text x="430" y="94" text-anchor="middle" fill="#155e75" font-family="DejaVu Sans, sans-serif" font-size="16" font-weight="700">2. Index / Staging</text>
  <text x="710" y="94" text-anchor="middle" fill="#166534" font-family="DejaVu Sans, sans-serif" font-size="16" font-weight="700">3. Repository</text>
  <text x="150" y="122" text-anchor="middle" fill="#7c2d12" font-family="DejaVu Sans, sans-serif" font-size="12">files on disk</text>
  <text x="430" y="122" text-anchor="middle" fill="#164e63" font-family="DejaVu Sans, sans-serif" font-size="12">next commit draft</text>
  <text x="710" y="122" text-anchor="middle" fill="#14532d" font-family="DejaVu Sans, sans-serif" font-size="12">immutable object history</text>
  <text x="150" y="168" text-anchor="middle" fill="#431407" font-family="DejaVu Sans Mono, monospace" font-size="11">auth.ts  ·  README.md</text>
  <text x="430" y="168" text-anchor="middle" fill="#083344" font-family="DejaVu Sans Mono, monospace" font-size="11">staged: auth.ts</text>
  <text x="710" y="168" text-anchor="middle" fill="#052e16" font-family="DejaVu Sans Mono, monospace" font-size="11">commit 9f3a…  HEAD</text>
  <text x="150" y="204" text-anchor="middle" fill="#9a3412" font-family="DejaVu Sans Mono, monospace" font-size="11">git add</text>
  <text x="430" y="204" text-anchor="middle" fill="#155e75" font-family="DejaVu Sans Mono, monospace" font-size="11">git commit</text>
  <text x="710" y="204" text-anchor="middle" fill="#166534" font-family="DejaVu Sans Mono, monospace" font-size="11">git log / show</text>
  <!-- arrows -->
  <path d="M262 140 L316 140" stroke="#fdba74" stroke-width="3" fill="none" marker-end="url(#a)"/>
  <path d="M542 140 L596 140" stroke="#67e8f9" stroke-width="3" fill="none"/>
  <polygon points="310,134 322,140 310,146" fill="#fdba74"/>
  <polygon points="590,134 602,140 590,146" fill="#67e8f9"/>
</svg>
""",
)

save(
    "objects.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 300" width="860" height="300">
  <rect width="860" height="300" rx="18" fill="#0f172a"/>
  <text x="430" y="34" text-anchor="middle" fill="#fdba74" font-family="DejaVu Sans, sans-serif" font-size="15" font-weight="700">Git objects  ·  commit → tree → blob</text>
  <rect x="40" y="60" width="200" height="90" rx="12" fill="#1e293b" stroke="#f97316" stroke-width="2"/>
  <text x="140" y="88" text-anchor="middle" fill="#fb923c" font-family="DejaVu Sans Mono, monospace" font-size="13" font-weight="700">COMMIT</text>
  <text x="140" y="110" text-anchor="middle" fill="#e2e8f0" font-family="DejaVu Sans, sans-serif" font-size="11">tree 4c2e…</text>
  <text x="140" y="128" text-anchor="middle" fill="#94a3b8" font-family="DejaVu Sans, sans-serif" font-size="11">parent a91b…</text>
  <path d="M240 105 L310 105" stroke="#f97316" stroke-width="2"/>
  <polygon points="304,99 316,105 304,111" fill="#f97316"/>
  <rect x="316" y="60" width="220" height="210" rx="12" fill="#1e293b" stroke="#22d3ee" stroke-width="2"/>
  <text x="426" y="88" text-anchor="middle" fill="#67e8f9" font-family="DejaVu Sans Mono, monospace" font-size="13" font-weight="700">TREE (snapshot)</text>
  <text x="426" y="118" text-anchor="middle" fill="#e2e8f0" font-family="DejaVu Sans Mono, monospace" font-size="12">100644 blob  src/app.ts</text>
  <text x="426" y="142" text-anchor="middle" fill="#e2e8f0" font-family="DejaVu Sans Mono, monospace" font-size="12">100644 blob  README.md</text>
  <text x="426" y="166" text-anchor="middle" fill="#e2e8f0" font-family="DejaVu Sans Mono, monospace" font-size="12">040000 tree  docs/</text>
  <text x="426" y="202" text-anchor="middle" fill="#94a3b8" font-family="DejaVu Sans, sans-serif" font-size="11">each commit is a full snapshot</text>
  <text x="426" y="222" text-anchor="middle" fill="#94a3b8" font-family="DejaVu Sans, sans-serif" font-size="11">of the entire file tree</text>
  <path d="M536 130 L610 90" stroke="#4ade80" stroke-width="2"/>
  <path d="M536 150 L610 170" stroke="#4ade80" stroke-width="2"/>
  <rect x="612" y="58" width="208" height="70" rx="12" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="716" y="86" text-anchor="middle" fill="#bbf7d0" font-family="DejaVu Sans Mono, monospace" font-size="13" font-weight="700">BLOB</text>
  <text x="716" y="108" text-anchor="middle" fill="#dcfce7" font-family="DejaVu Sans, sans-serif" font-size="11">contents of app.ts</text>
  <rect x="612" y="148" width="208" height="70" rx="12" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="716" y="176" text-anchor="middle" fill="#bbf7d0" font-family="DejaVu Sans Mono, monospace" font-size="13" font-weight="700">BLOB</text>
  <text x="716" y="198" text-anchor="middle" fill="#dcfce7" font-family="DejaVu Sans, sans-serif" font-size="11">contents of README.md</text>
  <text x="430" y="286" text-anchor="middle" fill="#64748b" font-family="DejaVu Sans, sans-serif" font-size="12">hash = SHA-1 or SHA-256  ·  content-addressed</text>
</svg>
""",
)

save(
    "dag.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 260" width="860" height="260">
  <rect width="860" height="260" rx="18" fill="#0f172a"/>
  <text x="430" y="32" text-anchor="middle" fill="#fdba74" font-family="DejaVu Sans, sans-serif" font-size="15" font-weight="700">Commit DAG  ·  branch pointers</text>
  <!-- main line -->
  <line x1="80" y1="140" x2="760" y2="140" stroke="#fb923c" stroke-width="4"/>
  <!-- feature -->
  <path d="M280 140 C 320 140, 340 70, 400 70 L 520 70 C 560 70, 580 140, 620 140" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <!-- commits -->
  <circle cx="120" cy="140" r="16" fill="#fb923c"/><text x="120" y="144" text-anchor="middle" fill="#0f172a" font-family="DejaVu Sans Mono, monospace" font-size="9" font-weight="700">A</text>
  <circle cx="220" cy="140" r="16" fill="#fb923c"/><text x="220" y="144" text-anchor="middle" fill="#0f172a" font-family="DejaVu Sans Mono, monospace" font-size="9" font-weight="700">B</text>
  <circle cx="400" cy="70" r="16" fill="#38bdf8"/><text x="400" y="74" text-anchor="middle" fill="#0f172a" font-family="DejaVu Sans Mono, monospace" font-size="9" font-weight="700">D</text>
  <circle cx="520" cy="70" r="16" fill="#38bdf8"/><text x="520" y="74" text-anchor="middle" fill="#0f172a" font-family="DejaVu Sans Mono, monospace" font-size="9" font-weight="700">E</text>
  <circle cx="400" cy="140" r="16" fill="#fb923c"/><text x="400" y="144" text-anchor="middle" fill="#0f172a" font-family="DejaVu Sans Mono, monospace" font-size="9" font-weight="700">C</text>
  <circle cx="620" cy="140" r="18" fill="#4ade80" stroke="#bbf7d0" stroke-width="2"/><text x="620" y="144" text-anchor="middle" fill="#052e16" font-family="DejaVu Sans Mono, monospace" font-size="9" font-weight="700">M</text>
  <circle cx="740" cy="140" r="16" fill="#fb923c"/><text x="740" y="144" text-anchor="middle" fill="#0f172a" font-family="DejaVu Sans Mono, monospace" font-size="9" font-weight="700">F</text>
  <!-- labels -->
  <rect x="690" y="168" width="90" height="28" rx="8" fill="#7c2d12"/>
  <text x="735" y="187" text-anchor="middle" fill="#fed7aa" font-family="DejaVu Sans Mono, monospace" font-size="12">HEAD</text>
  <line x1="735" y1="168" x2="740" y2="156" stroke="#fdba74" stroke-width="2"/>
  <rect x="80" y="188" width="80" height="26" rx="8" fill="#9a3412"/>
  <text x="120" y="206" text-anchor="middle" fill="#ffedd5" font-family="DejaVu Sans Mono, monospace" font-size="11">main</text>
  <line x1="120" y1="188" x2="120" y2="156" stroke="#fb923c" stroke-width="2"/>
  <text x="400" y="48" text-anchor="middle" fill="#7dd3fc" font-family="DejaVu Sans Mono, monospace" font-size="11">feature/login</text>
  <text x="620" y="188" text-anchor="middle" fill="#86efac" font-family="DejaVu Sans, sans-serif" font-size="11">merge commit</text>
  <text x="430" y="244" text-anchor="middle" fill="#94a3b8" font-family="DejaVu Sans, sans-serif" font-size="12">a branch is only a pointer — moving it is cheap</text>
</svg>
""",
)

save(
    "merge-rebase.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 320" width="860" height="320">
  <rect width="860" height="320" rx="18" fill="#0f172a"/>
  <text x="215" y="32" text-anchor="middle" fill="#fb923c" font-family="DejaVu Sans, sans-serif" font-size="14" font-weight="700">git merge</text>
  <text x="645" y="32" text-anchor="middle" fill="#38bdf8" font-family="DejaVu Sans, sans-serif" font-size="14" font-weight="700">git rebase</text>
  <line x1="430" y1="20" x2="430" y2="300" stroke="#334155" stroke-width="1"/>
  <!-- merge -->
  <line x1="50" y1="160" x2="360" y2="160" stroke="#fb923c" stroke-width="4"/>
  <path d="M140 160 C 170 160, 190 90, 230 90 L 290 90 C 320 90, 330 160, 350 160" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="80" cy="160" r="12" fill="#fb923c"/>
  <circle cx="140" cy="160" r="12" fill="#fb923c"/>
  <circle cx="230" cy="90" r="12" fill="#38bdf8"/>
  <circle cx="290" cy="90" r="12" fill="#38bdf8"/>
  <circle cx="230" cy="160" r="12" fill="#fb923c"/>
  <circle cx="350" cy="160" r="14" fill="#4ade80"/>
  <text x="215" y="230" text-anchor="middle" fill="#cbd5e1" font-family="DejaVu Sans, sans-serif" font-size="12">history is preserved</text>
  <text x="215" y="250" text-anchor="middle" fill="#94a3b8" font-family="DejaVu Sans, sans-serif" font-size="11">a new merge commit</text>
  <text x="215" y="278" text-anchor="middle" fill="#86efac" font-family="DejaVu Sans, sans-serif" font-size="11">safe on shared branches</text>
  <!-- rebase -->
  <line x1="480" y1="160" x2="800" y2="160" stroke="#fb923c" stroke-width="4"/>
  <circle cx="510" cy="160" r="12" fill="#fb923c"/>
  <circle cx="570" cy="160" r="12" fill="#fb923c"/>
  <circle cx="650" cy="160" r="12" fill="#fb923c"/>
  <circle cx="720" cy="160" r="12" fill="#38bdf8"/>
  <circle cx="790" cy="160" r="12" fill="#38bdf8"/>
  <text x="720" y="140" text-anchor="middle" fill="#7dd3fc" font-family="DejaVu Sans Mono, monospace" font-size="10">D'</text>
  <text x="790" y="140" text-anchor="middle" fill="#7dd3fc" font-family="DejaVu Sans Mono, monospace" font-size="10">E'</text>
  <text x="645" y="230" text-anchor="middle" fill="#cbd5e1" font-family="DejaVu Sans, sans-serif" font-size="12">linear, clean history</text>
  <text x="645" y="250" text-anchor="middle" fill="#94a3b8" font-family="DejaVu Sans, sans-serif" font-size="11">commits are rewritten</text>
  <text x="645" y="278" text-anchor="middle" fill="#fda4af" font-family="DejaVu Sans, sans-serif" font-size="11">never rebase a shared main</text>
</svg>
""",
)

save(
    "github-flow.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 220" width="860" height="220">
  <rect width="860" height="220" rx="18" fill="#0f172a"/>
  <text x="430" y="34" text-anchor="middle" fill="#fdba74" font-family="DejaVu Sans, sans-serif" font-size="15" font-weight="700">GitHub Flow  ·  modern team default</text>
  <g font-family="DejaVu Sans, sans-serif" font-size="12" text-anchor="middle">
    <rect x="24" y="70" width="140" height="78" rx="12" fill="#1e293b" stroke="#fb923c" stroke-width="2"/>
    <text x="94" y="104" fill="#fdba74" font-weight="700">1. Branch</text>
    <text x="94" y="124" fill="#cbd5e1" font-size="11">from main</text>
    <rect x="188" y="70" width="140" height="78" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="258" y="104" fill="#7dd3fc" font-weight="700">2. Commit</text>
    <text x="258" y="124" fill="#cbd5e1" font-size="11">small change</text>
    <rect x="352" y="70" width="140" height="78" rx="12" fill="#1e293b" stroke="#a78bfa" stroke-width="2"/>
    <text x="422" y="104" fill="#c4b5fd" font-weight="700">3. Pull Request</text>
    <text x="422" y="124" fill="#cbd5e1" font-size="11">discussion + CI</text>
    <rect x="516" y="70" width="140" height="78" rx="12" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <text x="586" y="104" fill="#fde68a" font-weight="700">4. Review</text>
    <text x="586" y="124" fill="#cbd5e1" font-size="11">Approve</text>
    <rect x="680" y="70" width="156" height="78" rx="12" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
    <text x="758" y="104" fill="#bbf7d0" font-weight="700">5. Merge → main</text>
    <text x="758" y="124" fill="#dcfce7" font-size="11">Deploy</text>
  </g>
  <text x="430" y="190" text-anchor="middle" fill="#94a3b8" font-family="DejaVu Sans, sans-serif" font-size="12">main is always deployable  ·  short-lived branches  ·  PR is the gate</text>
</svg>
""",
)

save(
    "actions-flow.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 240" width="860" height="240">
  <rect width="860" height="240" rx="18" fill="#0f172a"/>
  <text x="430" y="32" text-anchor="middle" fill="#fdba74" font-family="DejaVu Sans, sans-serif" font-size="15" font-weight="700">GitHub Actions  ·  event to deploy</text>
  <rect x="30" y="70" width="150" height="70" rx="12" fill="#1e293b" stroke="#fb923c" stroke-width="2"/>
  <text x="105" y="100" text-anchor="middle" fill="#fdba74" font-family="DejaVu Sans, sans-serif" font-size="13" font-weight="700">Event</text>
  <text x="105" y="120" text-anchor="middle" fill="#cbd5e1" font-family="DejaVu Sans Mono, monospace" font-size="10">pull_request</text>
  <rect x="220" y="70" width="150" height="70" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="295" y="100" text-anchor="middle" fill="#7dd3fc" font-family="DejaVu Sans, sans-serif" font-size="13" font-weight="700">Workflow</text>
  <text x="295" y="120" text-anchor="middle" fill="#cbd5e1" font-family="DejaVu Sans Mono, monospace" font-size="10">ci.yml</text>
  <rect x="410" y="50" width="130" height="50" rx="10" fill="#1e293b" stroke="#a78bfa" stroke-width="2"/>
  <text x="475" y="80" text-anchor="middle" fill="#c4b5fd" font-family="DejaVu Sans, sans-serif" font-size="12">Job: lint</text>
  <rect x="410" y="112" width="130" height="50" rx="10" fill="#1e293b" stroke="#a78bfa" stroke-width="2"/>
  <text x="475" y="142" text-anchor="middle" fill="#c4b5fd" font-family="DejaVu Sans, sans-serif" font-size="12">Job: test</text>
  <rect x="580" y="70" width="110" height="70" rx="12" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
  <text x="635" y="100" text-anchor="middle" fill="#fde68a" font-family="DejaVu Sans, sans-serif" font-size="13" font-weight="700">Checks</text>
  <text x="635" y="120" text-anchor="middle" fill="#cbd5e1" font-family="DejaVu Sans, sans-serif" font-size="11">required</text>
  <rect x="720" y="70" width="110" height="70" rx="12" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="775" y="100" text-anchor="middle" fill="#bbf7d0" font-family="DejaVu Sans, sans-serif" font-size="13" font-weight="700">Merge</text>
  <text x="775" y="120" text-anchor="middle" fill="#dcfce7" font-family="DejaVu Sans, sans-serif" font-size="11">or Deploy</text>
  <text x="430" y="210" text-anchor="middle" fill="#94a3b8" font-family="DejaVu Sans, sans-serif" font-size="12">OIDC to cloud  ·  env secrets  ·  immutable releases</text>
</svg>
""",
)

save(
    "undo-map.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 260" width="860" height="260">
  <rect width="860" height="260" rx="18" fill="#0f172a"/>
  <text x="430" y="32" text-anchor="middle" fill="#fdba74" font-family="DejaVu Sans, sans-serif" font-size="15" font-weight="700">Undo map  ·  which command, which tree?</text>
  <g font-family="DejaVu Sans, sans-serif" font-size="12">
    <rect x="30" y="58" width="190" height="150" rx="12" fill="#1e293b" stroke="#fb923c" stroke-width="2"/>
    <text x="125" y="88" text-anchor="middle" fill="#fdba74" font-size="14" font-weight="700">Working Tree</text>
    <text x="125" y="118" text-anchor="middle" fill="#e2e8f0">git restore file</text>
    <text x="125" y="142" text-anchor="middle" fill="#e2e8f0">VS Code Discard</text>
    <text x="125" y="166" text-anchor="middle" fill="#94a3b8" font-size="11">restores the file</text>
    <rect x="235" y="58" width="190" height="150" rx="12" fill="#1e293b" stroke="#22d3ee" stroke-width="2"/>
    <text x="330" y="88" text-anchor="middle" fill="#67e8f9" font-size="14" font-weight="700">Index</text>
    <text x="330" y="118" text-anchor="middle" fill="#e2e8f0">git restore --staged</text>
    <text x="330" y="142" text-anchor="middle" fill="#e2e8f0">Unstage in VS Code</text>
    <text x="330" y="166" text-anchor="middle" fill="#94a3b8" font-size="11">removes from staging</text>
    <rect x="440" y="58" width="190" height="150" rx="12" fill="#1e293b" stroke="#a78bfa" stroke-width="2"/>
    <text x="535" y="88" text-anchor="middle" fill="#c4b5fd" font-size="14" font-weight="700">Last commit</text>
    <text x="535" y="118" text-anchor="middle" fill="#e2e8f0">git commit --amend</text>
    <text x="535" y="142" text-anchor="middle" fill="#e2e8f0">git reset --soft HEAD~1</text>
    <text x="535" y="166" text-anchor="middle" fill="#94a3b8" font-size="11">if not pushed yet</text>
    <rect x="645" y="58" width="185" height="150" rx="12" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
    <text x="737" y="88" text-anchor="middle" fill="#86efac" font-size="14" font-weight="700">public history</text>
    <text x="737" y="118" text-anchor="middle" fill="#e2e8f0">git revert</text>
    <text x="737" y="142" text-anchor="middle" fill="#e2e8f0">revert the PR</text>
    <text x="737" y="166" text-anchor="middle" fill="#94a3b8" font-size="11">never rewrite public history</text>
  </g>
  <text x="430" y="236" text-anchor="middle" fill="#fda4af" font-family="DejaVu Sans, sans-serif" font-size="12">golden rule: if others saw it, revert — never reset</text>
</svg>
""",
)

save(
    "vscode-keymap.svg",
    """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 280" width="860" height="280">
  <rect width="860" height="280" rx="18" fill="#0f172a"/>
  <text x="430" y="32" text-anchor="middle" fill="#fdba74" font-family="DejaVu Sans, sans-serif" font-size="15" font-weight="700">VS Code map  ·  where Git lives</text>
  <rect x="40" y="56" width="48" height="190" rx="8" fill="#020617" stroke="#334155"/>
  <text x="64" y="90" text-anchor="middle" fill="#94a3b8" font-size="9" font-family="DejaVu Sans, sans-serif">Explorer</text>
  <rect x="46" y="118" width="36" height="36" rx="6" fill="#ea580c"/>
  <text x="64" y="140" text-anchor="middle" fill="#fff" font-size="11" font-family="DejaVu Sans, sans-serif">Git</text>
  <circle cx="76" cy="124" r="7" fill="#ef4444"/>
  <text x="76" y="127" text-anchor="middle" fill="#fff" font-size="8" font-family="DejaVu Sans, sans-serif">3</text>
  <rect x="100" y="56" width="240" height="190" rx="8" fill="#020617" stroke="#f97316" stroke-width="2"/>
  <text x="220" y="82" text-anchor="middle" fill="#fdba74" font-family="DejaVu Sans, sans-serif" font-size="13" font-weight="700">SOURCE CONTROL</text>
  <rect x="118" y="96" width="204" height="28" rx="6" fill="#1e293b" stroke="#475569"/>
  <text x="220" y="115" text-anchor="middle" fill="#64748b" font-family="DejaVu Sans, sans-serif" font-size="10">Message (Ctrl+Enter)</text>
  <rect x="118" y="134" width="204" height="32" rx="6" fill="#ea580c"/>
  <text x="220" y="155" text-anchor="middle" fill="#fff" font-family="DejaVu Sans, sans-serif" font-size="12" font-weight="700">Commit</text>
  <text x="220" y="188" text-anchor="middle" fill="#cbd5e1" font-family="DejaVu Sans, sans-serif" font-size="11">Changes  ·  3 files</text>
  <text x="220" y="210" text-anchor="middle" fill="#86efac" font-family="DejaVu Sans Mono, monospace" font-size="10">M  src/auth.ts</text>
  <rect x="360" y="56" width="460" height="190" rx="8" fill="#020617" stroke="#334155"/>
  <text x="590" y="92" text-anchor="middle" fill="#e2e8f0" font-family="DejaVu Sans, sans-serif" font-size="13" font-weight="700">Editor + Diff + Terminal</text>
  <text x="590" y="124" text-anchor="middle" fill="#94a3b8" font-family="DejaVu Sans Mono, monospace" font-size="12">Ctrl+Shift+G   open Source Control</text>
  <text x="590" y="152" text-anchor="middle" fill="#94a3b8" font-family="DejaVu Sans Mono, monospace" font-size="12">Ctrl+Shift+`   integrated terminal</text>
  <text x="590" y="180" text-anchor="middle" fill="#94a3b8" font-family="DejaVu Sans, sans-serif" font-size="12">Status bar: current branch + Sync</text>
  <text x="590" y="214" text-anchor="middle" fill="#fdba74" font-family="DejaVu Sans, sans-serif" font-size="12">Daily Git without leaving the editor</text>
</svg>
""",
)

print("done")
