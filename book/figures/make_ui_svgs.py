#!/usr/bin/env python3
"""Crisp vector UI illustrations — designed panels, not photos of monitors."""
from pathlib import Path

OUT = Path(__file__).parent


def save(name: str, svg: str) -> None:
    (OUT / name).write_text(svg.strip() + "\n", encoding="utf-8")
    print("wrote", name, "bytes", len(svg))


# --------------------------------------------------------------------------- VS Code SCM empty
save(
    "vscode-scm-empty.svg",
    r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 620" width="1100" height="620">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1b2332"/><stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="s" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#020617" flood-opacity=".45"/>
    </filter>
  </defs>
  <rect width="1100" height="620" rx="18" fill="#020617"/>
  <rect x="24" y="24" width="1052" height="572" rx="14" fill="url(#bg)" filter="url(#s)"/>
  <!-- titlebar -->
  <rect x="24" y="24" width="1052" height="36" rx="14" fill="#0b1220"/>
  <rect x="24" y="46" width="1052" height="14" fill="#0b1220"/>
  <circle cx="48" cy="42" r="6" fill="#f87171"/><circle cx="68" cy="42" r="6" fill="#fbbf24"/><circle cx="88" cy="42" r="6" fill="#34d399"/>
  <text x="550" y="47" text-anchor="middle" fill="#94a3b8" font-family="DejaVu Sans, sans-serif" font-size="13">git-lab  —  Visual Studio Code</text>
  <!-- activity bar -->
  <rect x="24" y="60" width="52" height="536" fill="#020617"/>
  <rect x="32" y="78" width="36" height="36" rx="8" fill="#1e293b"/>
  <rect x="32" y="126" width="36" height="36" rx="8" fill="#ea580c"/>
  <circle cx="62" cy="132" r="8" fill="#ef4444"/><text x="62" y="136" text-anchor="middle" fill="#fff" font-size="9" font-family="DejaVu Sans, sans-serif">0</text>
  <text x="50" y="150" text-anchor="middle" fill="#fff" font-size="9" font-family="DejaVu Sans, sans-serif">Git</text>
  <rect x="32" y="174" width="36" height="36" rx="8" fill="#1e293b"/>
  <rect x="32" y="222" width="36" height="36" rx="8" fill="#1e293b"/>
  <!-- scm panel -->
  <rect x="76" y="60" width="300" height="536" fill="#0b1220"/>
  <text x="92" y="88" fill="#e2e8f0" font-family="DejaVu Sans, sans-serif" font-size="13" font-weight="700">SOURCE CONTROL</text>
  <text x="348" y="88" fill="#64748b" font-family="DejaVu Sans Mono, monospace" font-size="11">Ctrl+Shift+G</text>
  <rect x="92" y="108" width="268" height="40" rx="8" fill="#111827" stroke="#334155"/>
  <text x="106" y="133" fill="#64748b" font-family="DejaVu Sans, sans-serif" font-size="13">Message (Ctrl+Enter to commit)</text>
  <rect x="92" y="158" width="268" height="36" rx="8" fill="#ea580c"/>
  <text x="226" y="181" text-anchor="middle" fill="#fff" font-family="DejaVu Sans, sans-serif" font-size="14" font-weight="700">Commit</text>
  <text x="92" y="220" fill="#94a3b8" font-family="DejaVu Sans, sans-serif" font-size="12">CHANGES</text>
  <rect x="92" y="236" width="268" height="120" rx="10" fill="#111827" stroke="#1e293b" stroke-dasharray="5 5"/>
  <text x="226" y="288" text-anchor="middle" fill="#64748b" font-family="DejaVu Sans, sans-serif" font-size="13">Working tree clean</text>
  <text x="226" y="310" text-anchor="middle" fill="#475569" font-family="DejaVu Sans, sans-serif" font-size="11">no files to commit</text>
  <text x="92" y="390" fill="#64748b" font-family="DejaVu Sans, sans-serif" font-size="11">Initialize only if .git is missing</text>
  <rect x="92" y="406" width="268" height="32" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="226" y="427" text-anchor="middle" fill="#fdba74" font-family="DejaVu Sans, sans-serif" font-size="12">Initialize Repository</text>
  <!-- editor -->
  <rect x="376" y="60" width="700" height="496" fill="#0f172a"/>
  <rect x="376" y="60" width="700" height="32" fill="#020617"/>
  <rect x="392" y="66" width="160" height="22" rx="6" fill="#1e293b"/>
  <text x="412" y="82" fill="#94a3b8" font-family="DejaVu Sans Mono, monospace" font-size="11">README.md</text>
  <text x="408" y="120" fill="#64748b" font-family="DejaVu Sans Mono, monospace" font-size="13"># Git Lab</text>
  <text x="408" y="148" fill="#cbd5e1" font-family="DejaVu Sans Mono, monospace" font-size="13">Working tree is clean.</text>
  <text x="408" y="176" fill="#64748b" font-family="DejaVu Sans Mono, monospace" font-size="13">Save files to see them in Changes.</text>
  <!-- status bar -->
  <rect x="376" y="556" width="700" height="40" fill="#ea580c"/>
  <text x="396" y="581" fill="#fff" font-family="DejaVu Sans, sans-serif" font-size="13">⎇  main</text>
  <text x="500" y="581" fill="#ffedd5" font-family="DejaVu Sans, sans-serif" font-size="12">✓  synced</text>
  <text x="980" y="581" fill="#fff" font-family="DejaVu Sans Mono, monospace" font-size="12">UTF-8  ·  LF</text>
</svg>
""",
)

save(
    "vscode-scm-commit.svg",
    r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 640" width="1100" height="640">
  <rect width="1100" height="640" rx="18" fill="#020617"/>
  <rect x="20" y="20" width="1060" height="600" rx="14" fill="#0f172a"/>
  <rect x="20" y="20" width="1060" height="36" rx="14" fill="#0b1220"/>
  <rect x="20" y="42" width="1060" height="14" fill="#0b1220"/>
  <circle cx="44" cy="38" r="6" fill="#f87171"/><circle cx="64" cy="38" r="6" fill="#fbbf24"/><circle cx="84" cy="38" r="6" fill="#34d399"/>
  <text x="550" y="43" text-anchor="middle" fill="#94a3b8" font-family="DejaVu Sans, sans-serif" font-size="13">feat/auth  —  Visual Studio Code</text>
  <rect x="20" y="56" width="52" height="564" fill="#020617"/>
  <rect x="28" y="120" width="36" height="36" rx="8" fill="#ea580c"/>
  <circle cx="58" cy="126" r="8" fill="#ef4444"/><text x="58" y="130" text-anchor="middle" fill="#fff" font-size="9" font-family="DejaVu Sans, sans-serif">3</text>
  <rect x="72" y="56" width="310" height="564" fill="#0b1220"/>
  <text x="88" y="84" fill="#e2e8f0" font-family="DejaVu Sans, sans-serif" font-size="13" font-weight="700">SOURCE CONTROL</text>
  <rect x="88" y="100" width="278" height="44" rx="8" fill="#111827" stroke="#f97316"/>
  <text x="102" y="128" fill="#fdba74" font-family="DejaVu Sans Mono, monospace" font-size="12">feat(auth): add JWT refresh flow</text>
  <rect x="88" y="154" width="278" height="36" rx="8" fill="#ea580c"/>
  <text x="227" y="177" text-anchor="middle" fill="#fff" font-family="DejaVu Sans, sans-serif" font-size="14" font-weight="700">Commit  ·  Ctrl+Enter</text>
  <text x="88" y="216" fill="#94a3b8" font-family="DejaVu Sans, sans-serif" font-size="11">STAGED CHANGES</text>
  <rect x="88" y="226" width="278" height="36" rx="8" fill="#14532d"/>
  <text x="104" y="249" fill="#86efac" font-family="DejaVu Sans Mono, monospace" font-size="12">M   src/auth.ts</text>
  <text x="88" y="286" fill="#94a3b8" font-family="DejaVu Sans, sans-serif" font-size="11">CHANGES</text>
  <rect x="88" y="296" width="278" height="36" rx="8" fill="#1e293b"/>
  <text x="104" y="319" fill="#fdba74" font-family="DejaVu Sans Mono, monospace" font-size="12">M   src/api.ts</text>
  <rect x="88" y="338" width="278" height="36" rx="8" fill="#1e293b"/>
  <text x="104" y="361" fill="#7dd3fc" font-family="DejaVu Sans Mono, monospace" font-size="12">U   README.md</text>
  <text x="88" y="400" fill="#64748b" font-family="DejaVu Sans, sans-serif" font-size="11">Stage Selected Ranges = git add -p</text>
  <!-- diff -->
  <rect x="382" y="56" width="698" height="528" fill="#0f172a"/>
  <rect x="382" y="56" width="698" height="32" fill="#020617"/>
  <text x="400" y="77" fill="#86efac" font-family="DejaVu Sans Mono, monospace" font-size="12">src/auth.ts  +24  −6</text>
  <rect x="398" y="104" width="666" height="28" fill="#052e16"/>
  <text x="410" y="123" fill="#86efac" font-family="DejaVu Sans Mono, monospace" font-size="13">+  export async function rotateToken(t: string) {</text>
  <rect x="398" y="132" width="666" height="28" fill="#052e16"/>
  <text x="410" y="151" fill="#86efac" font-family="DejaVu Sans Mono, monospace" font-size="13">+    const next = await api.refresh(t);</text>
  <rect x="398" y="160" width="666" height="28" fill="#052e16"/>
  <text x="410" y="179" fill="#86efac" font-family="DejaVu Sans Mono, monospace" font-size="13">+    return next;</text>
  <rect x="398" y="188" width="666" height="28" fill="#052e16"/>
  <text x="410" y="207" fill="#86efac" font-family="DejaVu Sans Mono, monospace" font-size="13">+  }</text>
  <rect x="398" y="228" width="666" height="28" fill="#450a0a"/>
  <text x="410" y="247" fill="#fca5a5" font-family="DejaVu Sans Mono, monospace" font-size="13">-  return token;</text>
  <rect x="398" y="256" width="666" height="28" fill="#1e293b"/>
  <text x="410" y="275" fill="#94a3b8" font-family="DejaVu Sans Mono, monospace" font-size="13">   export function login(user: User) { ... }</text>
  <rect x="382" y="584" width="698" height="36" fill="#ea580c"/>
  <text x="400" y="607" fill="#fff" font-family="DejaVu Sans, sans-serif" font-size="13">⎇  feat/auth  ↑ 1</text>
  <text x="560" y="607" fill="#ffedd5" font-family="DejaVu Sans, sans-serif" font-size="12">3 changes  ·  1 staged</text>
</svg>
""",
)

save(
    "vscode-git-graph.svg",
    r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 640" width="1100" height="640">
  <rect width="1100" height="640" rx="18" fill="#020617"/>
  <rect x="20" y="20" width="1060" height="600" rx="14" fill="#0f172a"/>
  <rect x="20" y="20" width="1060" height="40" fill="#0b1220" rx="14"/>
  <text x="550" y="46" text-anchor="middle" fill="#e2e8f0" font-family="DejaVu Sans, sans-serif" font-size="15" font-weight="700">SOURCE CONTROL GRAPH</text>
  <!-- lanes -->
  <text x="48" y="84" fill="#fb923c" font-family="DejaVu Sans Mono, monospace" font-size="11">main</text>
  <text x="120" y="84" fill="#38bdf8" font-family="DejaVu Sans Mono, monospace" font-size="11">feat/auth</text>
  <text x="220" y="84" fill="#4ade80" font-family="DejaVu Sans Mono, monospace" font-size="11">hotfix</text>
  <line x1="56" y1="96" x2="56" y2="580" stroke="#fb923c" stroke-width="4"/>
  <path d="M56 220 C 56 220, 90 220, 128 260" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <line x1="128" y1="260" x2="128" y2="430" stroke="#38bdf8" stroke-width="4"/>
  <path d="M128 430 C 90 470, 56 470, 56 470" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <path d="M56 340 C 90 340, 200 340, 220 360" fill="none" stroke="#4ade80" stroke-width="4"/>
  <line x1="220" y1="360" x2="220" y2="500" stroke="#4ade80" stroke-width="4"/>
  <path d="M220 500 C 140 530, 80 530, 56 530" fill="none" stroke="#4ade80" stroke-width="4"/>
  <!-- commits -->
  <g font-family="DejaVu Sans Mono, monospace" font-size="13">
    <circle cx="56" cy="130" r="10" fill="#fb923c"/><text x="280" y="136" fill="#e2e8f0">a91b77  chore: bootstrap repository</text><text x="900" y="136" fill="#64748b">2d ago</text>
    <circle cx="56" cy="180" r="10" fill="#fb923c"/><text x="280" y="186" fill="#e2e8f0">c22e10  docs: add README</text><text x="900" y="186" fill="#64748b">2d ago</text>
    <circle cx="56" cy="220" r="10" fill="#fb923c"/><text x="280" y="226" fill="#e2e8f0">d8aa01  feat: project skeleton</text>
    <circle cx="128" cy="300" r="10" fill="#38bdf8"/><text x="280" y="306" fill="#7dd3fc">9f3a1c  feat(auth): add JWT refresh flow</text><rect x="820" y="290" width="70" height="20" rx="6" fill="#7c2d12"/><text x="855" y="305" text-anchor="middle" fill="#fed7aa" font-size="10">HEAD</text>
    <circle cx="128" cy="350" r="10" fill="#38bdf8"/><text x="280" y="356" fill="#7dd3fc">b44c90  test(auth): rotate token cases</text>
    <circle cx="220" cy="400" r="10" fill="#4ade80"/><text x="280" y="406" fill="#86efac">e11f02  hotfix: 500 on empty token</text>
    <circle cx="128" cy="430" r="10" fill="#38bdf8"/><text x="280" y="436" fill="#7dd3fc">aa0192  docs(auth): sequence diagram</text>
    <circle cx="56" cy="470" r="12" fill="#c4b5fd"/><text x="280" y="476" fill="#ddd6fe">m7e21a  merge: feat/auth  (#42)</text>
    <circle cx="56" cy="530" r="12" fill="#4ade80"/><text x="280" y="536" fill="#bbf7d0">k90c11  merge: hotfix  (#43)</text>
    <circle cx="56" cy="580" r="10" fill="#fb923c"/><text x="280" y="586" fill="#fdba74">HEAD → main</text>
  </g>
</svg>
""",
)

save(
    "vscode-merge-conflict.svg",
    r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 640" width="1100" height="640">
  <rect width="1100" height="640" rx="18" fill="#020617"/>
  <rect x="20" y="20" width="1060" height="600" rx="14" fill="#0f172a"/>
  <rect x="20" y="20" width="1060" height="40" fill="#7f1d1d"/>
  <text x="40" y="46" fill="#fecaca" font-family="DejaVu Sans, sans-serif" font-size="14" font-weight="700">MERGE EDITOR  ·  src/auth.ts  ·  1 conflict</text>
  <!-- 3 columns -->
  <rect x="36" y="80" width="330" height="420" rx="10" fill="#0b1220" stroke="#38bdf8"/>
  <text x="201" y="108" text-anchor="middle" fill="#7dd3fc" font-family="DejaVu Sans, sans-serif" font-size="13" font-weight="700">INCOMING  ·  feat/auth</text>
  <rect x="52" y="124" width="298" height="48" rx="8" fill="#082f49"/>
  <text x="68" y="154" fill="#7dd3fc" font-family="DejaVu Sans Mono, monospace" font-size="13">return rotate(token);</text>
  <rect x="385" y="80" width="330" height="420" rx="10" fill="#0b1220" stroke="#fb923c"/>
  <text x="550" y="108" text-anchor="middle" fill="#fdba74" font-family="DejaVu Sans, sans-serif" font-size="13" font-weight="700">CURRENT  ·  HEAD / main</text>
  <rect x="401" y="124" width="298" height="48" rx="8" fill="#431407"/>
  <text x="417" y="154" fill="#fdba74" font-family="DejaVu Sans Mono, monospace" font-size="13">return token;</text>
  <rect x="734" y="80" width="330" height="420" rx="10" fill="#052e16" stroke="#4ade80"/>
  <text x="899" y="108" text-anchor="middle" fill="#86efac" font-family="DejaVu Sans, sans-serif" font-size="13" font-weight="700">RESULT</text>
  <rect x="750" y="124" width="298" height="48" rx="8" fill="#14532d"/>
  <text x="766" y="154" fill="#bbf7d0" font-family="DejaVu Sans Mono, monospace" font-size="13">return rotate(token);</text>
  <text x="750" y="200" fill="#86efac" font-family="DejaVu Sans, sans-serif" font-size="12">Accept Incoming selected</text>
  <!-- buttons -->
  <rect x="36" y="520" width="200" height="40" rx="8" fill="#1e293b" stroke="#38bdf8"/>
  <text x="136" y="545" text-anchor="middle" fill="#7dd3fc" font-family="DejaVu Sans, sans-serif" font-size="12">Accept Incoming</text>
  <rect x="252" y="520" width="200" height="40" rx="8" fill="#1e293b" stroke="#fb923c"/>
  <text x="352" y="545" text-anchor="middle" fill="#fdba74" font-family="DejaVu Sans, sans-serif" font-size="12">Accept Current</text>
  <rect x="468" y="520" width="200" height="40" rx="8" fill="#1e293b" stroke="#a78bfa"/>
  <text x="568" y="545" text-anchor="middle" fill="#c4b5fd" font-family="DejaVu Sans, sans-serif" font-size="12">Accept Both</text>
  <rect x="684" y="520" width="220" height="40" rx="8" fill="#15803d"/>
  <text x="794" y="545" text-anchor="middle" fill="#fff" font-family="DejaVu Sans, sans-serif" font-size="12" font-weight="700">Mark as Resolved + Stage</text>
  <text x="36" y="590" fill="#94a3b8" font-family="DejaVu Sans, sans-serif" font-size="12">Ours = HEAD   ·   Theirs = branch being merged   ·   never Accept Both blindly</text>
</svg>
""",
)

save(
    "vscode-pr-ext.svg",
    r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 640" width="1100" height="640">
  <rect width="1100" height="640" rx="18" fill="#020617"/>
  <rect x="20" y="20" width="1060" height="600" rx="14" fill="#0f172a"/>
  <rect x="20" y="20" width="52" height="600" rx="14" fill="#020617"/>
  <rect x="28" y="80" width="36" height="36" rx="8" fill="#1f6feb"/>
  <rect x="72" y="20" width="300" height="600" fill="#0b1220"/>
  <text x="88" y="56" fill="#e2e8f0" font-family="DejaVu Sans, sans-serif" font-size="13" font-weight="700">PULL REQUESTS</text>
  <rect x="88" y="76" width="268" height="88" rx="10" fill="#111827" stroke="#1f6feb"/>
  <text x="104" y="104" fill="#58a6ff" font-family="DejaVu Sans Mono, monospace" font-size="12">#42  feat(auth): JWT refresh</text>
  <text x="104" y="126" fill="#86efac" font-family="DejaVu Sans, sans-serif" font-size="11">● Open   ·   3 files   ·   +128 −24</text>
  <text x="104" y="148" fill="#94a3b8" font-family="DejaVu Sans, sans-serif" font-size="11">rezaian-dev  →  main</text>
  <text x="88" y="192" fill="#94a3b8" font-family="DejaVu Sans, sans-serif" font-size="11">CHECKS</text>
  <text x="104" y="216" fill="#4ade80" font-family="DejaVu Sans Mono, monospace" font-size="12">✓  lint</text>
  <text x="104" y="238" fill="#4ade80" font-family="DejaVu Sans Mono, monospace" font-size="12">✓  test</text>
  <text x="104" y="260" fill="#4ade80" font-family="DejaVu Sans Mono, monospace" font-size="12">✓  build</text>
  <rect x="88" y="286" width="268" height="36" rx="8" fill="#15803d"/>
  <text x="222" y="309" text-anchor="middle" fill="#fff" font-family="DejaVu Sans, sans-serif" font-size="13">Approve</text>
  <rect x="88" y="332" width="268" height="36" rx="8" fill="#1e293b" stroke="#f87171"/>
  <text x="222" y="355" text-anchor="middle" fill="#fca5a5" font-family="DejaVu Sans, sans-serif" font-size="13">Request Changes</text>
  <!-- editor comment -->
  <rect x="372" y="20" width="708" height="600" fill="#0f172a"/>
  <text x="392" y="56" fill="#94a3b8" font-family="DejaVu Sans Mono, monospace" font-size="12">src/auth.ts</text>
  <text x="392" y="92" fill="#cbd5e1" font-family="DejaVu Sans Mono, monospace" font-size="13">  42    const next = await api.refresh(t);</text>
  <rect x="392" y="110" width="660" height="110" rx="10" fill="#111827" stroke="#334155"/>
  <text x="412" y="140" fill="#c4b5fd" font-family="DejaVu Sans, sans-serif" font-size="12">Comment on line 42</text>
  <text x="412" y="164" fill="#e2e8f0" font-family="DejaVu Sans, sans-serif" font-size="12">nit: rename to rotateTokens for plural expiry.</text>
  <rect x="412" y="178" width="120" height="28" rx="6" fill="#1f6feb"/>
  <text x="472" y="197" text-anchor="middle" fill="#fff" font-family="DejaVu Sans, sans-serif" font-size="11">Add Comment</text>
  <text x="392" y="260" fill="#64748b" font-family="DejaVu Sans, sans-serif" font-size="12">Pending comments are local until Submit Review</text>
</svg>
""",
)

save(
    "github-repo.svg",
    r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 640" width="1100" height="640">
  <rect width="1100" height="640" rx="18" fill="#0d1117"/>
  <rect x="0" y="0" width="1100" height="56" fill="#010409"/>
  <circle cx="36" cy="28" r="12" fill="#e6edf3"/>
  <text x="58" y="34" fill="#e6edf3" font-family="DejaVu Sans, sans-serif" font-size="16">github</text>
  <text x="320" y="34" fill="#e6edf3" font-family="DejaVu Sans, sans-serif" font-size="15">rezaian-dev  /  git-github-persian-guide</text>
  <rect x="860" y="14" width="90" height="28" rx="8" fill="#21262d" stroke="#30363d"/>
  <text x="905" y="33" text-anchor="middle" fill="#e6edf3" font-family="DejaVu Sans, sans-serif" font-size="12">Star  128</text>
  <rect x="960" y="14" width="110" height="28" rx="8" fill="#238636"/>
  <text x="1015" y="33" text-anchor="middle" fill="#fff" font-family="DejaVu Sans, sans-serif" font-size="12">Code ▾</text>
  <!-- tabs -->
  <text x="40" y="88" fill="#e6edf3" font-family="DejaVu Sans, sans-serif" font-size="14" font-weight="700">Code</text>
  <line x1="36" y1="96" x2="86" y2="96" stroke="#f78166" stroke-width="3"/>
  <text x="120" y="88" fill="#8b949e" font-family="DejaVu Sans, sans-serif" font-size="14">Issues  4</text>
  <text x="230" y="88" fill="#8b949e" font-family="DejaVu Sans, sans-serif" font-size="14">Pull requests  1</text>
  <text x="400" y="88" fill="#8b949e" font-family="DejaVu Sans, sans-serif" font-size="14">Actions</text>
  <line x1="20" y1="104" x2="1080" y2="104" stroke="#21262d"/>
  <!-- files -->
  <rect x="28" y="120" width="720" height="490" rx="12" fill="#0d1117" stroke="#21262d"/>
  <rect x="28" y="120" width="720" height="44" fill="#161b22"/>
  <text x="48" y="148" fill="#e6edf3" font-family="DejaVu Sans Mono, monospace" font-size="13">main  ·  36 chapters  ·  128 commits</text>
  <g font-family="DejaVu Sans Mono, monospace" font-size="13" fill="#58a6ff">
    <text x="56" y="190">README.md</text>
    <text x="56" y="224">LICENSE</text>
    <text x="56" y="258">src/</text>
    <text x="56" y="292">docs/</text>
    <text x="56" y="326">.github/</text>
  </g>
  <g font-family="DejaVu Sans, sans-serif" font-size="12" fill="#8b949e">
    <text x="420" y="190">hero, badges, path</text>
    <text x="420" y="224">CC BY-NC-SA 4.0</text>
    <text x="420" y="258">chapters · build.py</text>
    <text x="420" y="292">pdf · assets</text>
    <text x="420" y="326">workflows</text>
  </g>
  <!-- about -->
  <rect x="768" y="120" width="304" height="490" rx="12" fill="#0d1117" stroke="#21262d"/>
  <text x="788" y="156" fill="#e6edf3" font-family="DejaVu Sans, sans-serif" font-size="16" font-weight="700">About</text>
  <text x="788" y="188" fill="#8b949e" font-family="DejaVu Sans, sans-serif" font-size="13">Persian Git &amp; GitHub handbook</text>
  <rect x="788" y="208" width="70" height="22" rx="11" fill="#13233a"/>
  <text x="823" y="224" text-anchor="middle" fill="#58a6ff" font-family="DejaVu Sans, sans-serif" font-size="11">git</text>
  <rect x="866" y="208" width="90" height="22" rx="11" fill="#13233a"/>
  <text x="911" y="224" text-anchor="middle" fill="#58a6ff" font-family="DejaVu Sans, sans-serif" font-size="11">github</text>
  <rect x="964" y="208" width="80" height="22" rx="11" fill="#13233a"/>
  <text x="1004" y="224" text-anchor="middle" fill="#58a6ff" font-family="DejaVu Sans, sans-serif" font-size="11">persian</text>
  <text x="788" y="270" fill="#e6edf3" font-family="DejaVu Sans, sans-serif" font-size="13">★ 128   🍴 24   👁 310</text>
  <text x="788" y="304" fill="#8b949e" font-family="DejaVu Sans, sans-serif" font-size="12">CC BY-NC-SA 4.0</text>
  <text x="788" y="336" fill="#8b949e" font-family="DejaVu Sans, sans-serif" font-size="12">Default branch  main</text>
</svg>
""",
)

save(
    "github-pr.svg",
    r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" width="1100" height="680">
  <rect width="1100" height="680" rx="18" fill="#0d1117"/>
  <text x="36" y="48" fill="#e6edf3" font-family="DejaVu Sans, sans-serif" font-size="22" font-weight="700">feat(auth): add JWT refresh flow</text>
  <rect x="36" y="64" width="70" height="24" rx="12" fill="#238636"/>
  <text x="71" y="81" text-anchor="middle" fill="#fff" font-family="DejaVu Sans, sans-serif" font-size="12">Open</text>
  <text x="120" y="82" fill="#8b949e" font-family="DejaVu Sans, sans-serif" font-size="13">#42  ·  rezaian-dev wants to merge 4 commits into main from feat/auth</text>
  <text x="36" y="120" fill="#e6edf3" font-family="DejaVu Sans, sans-serif" font-size="14">Conversation</text>
  <line x1="36" y1="128" x2="140" y2="128" stroke="#f78166" stroke-width="3"/>
  <text x="170" y="120" fill="#8b949e" font-family="DejaVu Sans, sans-serif" font-size="14">Commits  4</text>
  <text x="290" y="120" fill="#8b949e" font-family="DejaVu Sans, sans-serif" font-size="14">Checks  3</text>
  <text x="400" y="120" fill="#8b949e" font-family="DejaVu Sans, sans-serif" font-size="14">Files changed  3</text>
  <line x1="20" y1="140" x2="1080" y2="140" stroke="#21262d"/>
  <rect x="36" y="160" width="720" height="90" rx="10" fill="#161b22" stroke="#238636"/>
  <text x="56" y="198" fill="#3fb950" font-family="DejaVu Sans, sans-serif" font-size="16" font-weight="700">This branch has no conflicts with the base branch</text>
  <text x="56" y="226" fill="#8b949e" font-family="DejaVu Sans, sans-serif" font-size="13">Merging can be performed automatically.</text>
  <rect x="36" y="268" width="720" height="150" rx="10" fill="#161b22" stroke="#21262d"/>
  <text x="56" y="304" fill="#e6edf3" font-family="DejaVu Sans, sans-serif" font-size="14" font-weight="700">All checks have passed</text>
  <text x="56" y="336" fill="#3fb950" font-family="DejaVu Sans Mono, monospace" font-size="13">✓  CI / lint</text>
  <text x="56" y="362" fill="#3fb950" font-family="DejaVu Sans Mono, monospace" font-size="13">✓  CI / test</text>
  <text x="56" y="388" fill="#3fb950" font-family="DejaVu Sans Mono, monospace" font-size="13">✓  CI / build</text>
  <rect x="36" y="436" width="720" height="70" rx="10" fill="#161b22" stroke="#21262d"/>
  <text x="56" y="478" fill="#e6edf3" font-family="DejaVu Sans, sans-serif" font-size="14">1 approval  ·  0 requested changes  ·  conversations resolved</text>
  <rect x="36" y="524" width="220" height="44" rx="8" fill="#238636"/>
  <text x="146" y="552" text-anchor="middle" fill="#fff" font-family="DejaVu Sans, sans-serif" font-size="14" font-weight="700">Squash and merge</text>
  <rect x="780" y="160" width="284" height="400" rx="12" fill="#0d1117" stroke="#21262d"/>
  <text x="800" y="196" fill="#e6edf3" font-family="DejaVu Sans, sans-serif" font-size="14" font-weight="700">Reviewers</text>
  <text x="800" y="228" fill="#3fb950" font-family="DejaVu Sans, sans-serif" font-size="13">✓ teammate</text>
  <text x="800" y="272" fill="#e6edf3" font-family="DejaVu Sans, sans-serif" font-size="14" font-weight="700">Labels</text>
  <rect x="800" y="288" width="70" height="22" rx="11" fill="#0e4429"/>
  <text x="835" y="304" text-anchor="middle" fill="#3fb950" font-family="DejaVu Sans, sans-serif" font-size="11">feat</text>
  <text x="800" y="350" fill="#e6edf3" font-family="DejaVu Sans, sans-serif" font-size="14" font-weight="700">+128  −24</text>
  <text x="800" y="380" fill="#8b949e" font-family="DejaVu Sans, sans-serif" font-size="12">src/auth.ts   src/api.ts   README.md</text>
</svg>
""",
)

save(
    "github-actions.svg",
    r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 640" width="1100" height="640">
  <rect width="1100" height="640" rx="18" fill="#0d1117"/>
  <text x="36" y="48" fill="#e6edf3" font-family="DejaVu Sans, sans-serif" font-size="22" font-weight="700">CI</text>
  <text x="90" y="48" fill="#8b949e" font-family="DejaVu Sans, sans-serif" font-size="14">.github/workflows/ci.yml   ·   pull_request</text>
  <rect x="36" y="72" width="80" height="24" rx="12" fill="#238636"/>
  <text x="76" y="89" text-anchor="middle" fill="#fff" font-family="DejaVu Sans, sans-serif" font-size="12">Success</text>
  <text x="132" y="90" fill="#8b949e" font-family="DejaVu Sans, sans-serif" font-size="13">Run #128  ·  feat/auth  ·  1m 12s</text>
  <!-- pipeline -->
  <rect x="36" y="130" width="200" height="90" rx="12" fill="#161b22" stroke="#238636"/>
  <text x="136" y="168" text-anchor="middle" fill="#3fb950" font-family="DejaVu Sans, sans-serif" font-size="16" font-weight="700">✓ lint</text>
  <text x="136" y="194" text-anchor="middle" fill="#8b949e" font-family="DejaVu Sans Mono, monospace" font-size="12">12s</text>
  <line x1="236" y1="175" x2="276" y2="175" stroke="#238636" stroke-width="3"/>
  <rect x="276" y="130" width="200" height="90" rx="12" fill="#161b22" stroke="#238636"/>
  <text x="376" y="168" text-anchor="middle" fill="#3fb950" font-family="DejaVu Sans, sans-serif" font-size="16" font-weight="700">✓ test</text>
  <text x="376" y="194" text-anchor="middle" fill="#8b949e" font-family="DejaVu Sans Mono, monospace" font-size="12">38s</text>
  <line x1="476" y1="175" x2="516" y2="175" stroke="#238636" stroke-width="3"/>
  <rect x="516" y="130" width="200" height="90" rx="12" fill="#161b22" stroke="#238636"/>
  <text x="616" y="168" text-anchor="middle" fill="#3fb950" font-family="DejaVu Sans, sans-serif" font-size="16" font-weight="700">✓ build</text>
  <text x="616" y="194" text-anchor="middle" fill="#8b949e" font-family="DejaVu Sans Mono, monospace" font-size="12">22s</text>
  <line x1="716" y1="175" x2="756" y2="175" stroke="#238636" stroke-width="3"/>
  <rect x="756" y="130" width="220" height="90" rx="12" fill="#0e4429" stroke="#3fb950"/>
  <text x="866" y="168" text-anchor="middle" fill="#3fb950" font-family="DejaVu Sans, sans-serif" font-size="16" font-weight="700">required checks</text>
  <text x="866" y="194" text-anchor="middle" fill="#8b949e" font-family="DejaVu Sans, sans-serif" font-size="12">Ruleset on main</text>
  <!-- log -->
  <rect x="36" y="250" width="1028" height="360" rx="12" fill="#010409" stroke="#21262d"/>
  <text x="56" y="284" fill="#8b949e" font-family="DejaVu Sans Mono, monospace" font-size="12">job: test</text>
  <g font-family="DejaVu Sans Mono, monospace" font-size="13">
    <text x="56" y="320" fill="#3fb950">✓  Set up job</text>
    <text x="56" y="348" fill="#3fb950">✓  actions/checkout@v4</text>
    <text x="56" y="376" fill="#3fb950">✓  actions/setup-python@v5</text>
    <text x="56" y="404" fill="#3fb950">✓  pip install -r src/requirements.txt</text>
    <text x="56" y="432" fill="#3fb950">✓  python src/build.py --html</text>
    <text x="56" y="460" fill="#8b949e">  HTML written (243 KB)</text>
    <text x="56" y="500" fill="#3fb950">✓  Complete job</text>
  </g>
</svg>
""",
)

print("ui svgs done")
