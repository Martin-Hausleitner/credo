#!/usr/bin/env python3
"""E2E-Verifikation der OpenHuman-Integration + Diagramm-Features.
Prueft: interne Links/Anchor, cal.com->cal.rs, OpenHuman-Konsistenz, Mermaid-Bloecke.
Exit 0 nur wenn ALLE Checks gruen sind."""
import re, sys, pathlib, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
fails, checks = [], []

def norm_anchor(a):
    """GitHub-robuste Normalisierung: URL-decode, U+FE0F (Variation-Selector)
    und fuehrende/abschliessende Hyphen entfernen, damit Emoji-Encoding-
    Unterschiede zwischen GitHub und diesem Pruefer nicht falsch failen."""
    a = urllib.parse.unquote(a)
    a = a.replace("️", "")
    return a.strip("-").lower()

def ok(name, cond, detail=""):
    checks.append((cond, name, detail))
    if not cond: fails.append(f"{name} :: {detail}")

def slug(heading):
    # GitHub-Slug: lowercasen, Nicht-Wort/Space/Hyphen droppen, dann JEDES
    # Space einzeln zu Hyphen (NICHT kollabieren) -> "a — b" wird "a--b".
    s = heading.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)          # drop emoji/punctuation (em-dash faellt weg, Spaces bleiben)
    s = re.sub(r"\s", "-", s)               # jedes Whitespace-Zeichen -> 1 Hyphen
    return s.strip("-")

def headings_of(text):
    out = set()
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            out.add(norm_anchor(slug(m.group(2))))
    return out

# ---- load files ----
readme = (ROOT / "README.md").read_text(encoding="utf-8")
plan = (ROOT / "docs/openhuman-integration.md").read_text(encoding="utf-8")

# ---- 1. cal.com fully replaced by cal.rs ----
ok("cal.com entfernt (README)", "cal.com" not in readme, f"{readme.count('cal.com')} Treffer")
ok("cal.rs vorhanden (README)", "cal.rs" in readme, f"{readme.count('cal.rs')} Treffer")

# ---- 2. OpenHuman integration present + cross-linked ----
ok("OpenHuman im README", readme.count("OpenHuman") >= 8, f"{readme.count('OpenHuman')} Erwaehnungen")
ok("Plan-Doc verlinkt in README", "docs/openhuman-integration.md" in readme)
ok("OpenHuman-Sektion existiert", "OpenHuman als Personal-/Edge-Schicht" in readme)
ok("Plan verlinkt zurueck auf README", "../README.md#" in plan)

# ---- 3. Mermaid blocks render-ready ----
mm = re.findall(r"```mermaid\n(.*?)```", readme, re.S)
ok("Genau 1 Mermaid-Block im README", len(mm) == 1, f"{len(mm)} Bloecke")
if mm:
    d = mm[0]
    ok("Diagramm: 9 Ebenen (subgraphs)", d.count("subgraph ") == 9, f"{d.count('subgraph ')} subgraphs")
    ok("Diagramm: Write-Gate sichtbar", "Write-Gate" in d)
    ok("Diagramm: Happy-Path-Spine (==>)", d.count("==>") >= 7, f"{d.count('==>')} dicke Kanten")
    ok("Diagramm: cal.rs-Knoten", "cal.rs" in d)
    ok("Diagramm: kein cal.com", "cal.com" not in d)
    ok("Diagramm: balancierte subgraph/end", d.count("subgraph ") == len(re.findall(r"^\s*end\s*$", d, re.M)),
       f"{d.count('subgraph ')} subgraph vs {len(re.findall(r'^\\s*end\\s*$', d, re.M))} end")

# ---- 4. architecture.mmd in sync ----
arch = (ROOT / "docs/architecture.mmd").read_text(encoding="utf-8")
ok("architecture.mmd hat OpenHuman", "OpenHuman" in arch)
ok("architecture.mmd hat cal.rs", "cal.rs" in arch)
ok("architecture.mmd kein Tailscale (stale-Check)", "Tailscale" not in arch)
ok("architecture.mmd: 9 Ebenen", arch.count("subgraph ") == 9, f"{arch.count('subgraph ')} subgraphs")

# ---- Plan-Schritt 1: Memory-Bruecke in target-stack.md ----
tgt = (ROOT / "docs/target-stack.md").read_text(encoding="utf-8")
ok("Schritt 1: Memory-Bruecke-Sektion", "Memory-Bruecke" in tgt and "Write-Gate" in tgt)
ok("Schritt 1: Vault->Gate->pgvector-Fluss", "OpenHuman Vault-Chunk" in tgt and "pgvector Embedding" in tgt)
mem_types = ["Decision", "Project", "Person", "Meeting", "Task", "Source", "Runbook"]
missing_types = [t for t in mem_types if t not in tgt]
ok("Schritt 1: alle 7 Memory-Typen gemappt", not missing_types, f"fehlt: {missing_types}")
ok("Schritt 1: Memory-Modi referenziert", all(m in tgt for m in ["proposed-write", "approved-write", "read-only"]))

# ---- Plan-Schritt 2: Composio-Untrusted-Regime im Bridge-Runbook ----
runbook = (ROOT / "docs/matrix-ops-runbook.md").read_text(encoding="utf-8")
ok("Schritt 2: Composio-Untrusted-Sektion", "Composio-Untrusted-Regime" in runbook and "MCP-Untrusted-Regime" in runbook)
ok("Schritt 2: OSS-Migrationsziel definiert", "Migrationsziel" in runbook and "OSS-Migrationsziel" in runbook)
ok("Schritt 2: Migrations-Tabelle (Connector-Klassen)",
   all(k in runbook for k in ["Chat / Messaging", "Mail", "Kalender", "Dev / Issues", "Storage / Files"]))
ok("Schritt 2: Untrusted-Regeln (Audit/Sanitize/Scope)",
   all(s in runbook for s in ["sanitizen", "run_id", "Kill-Switch", "ambient Secrets"]))

# ---- 5. internal links resolve (files + anchors) across README + docs ----
md_files = [ROOT / "README.md"] + sorted((ROOT / "docs").glob("*.md"))
link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
broken = []
for f in md_files:
    text = f.read_text(encoding="utf-8")
    local_anchors = headings_of(text)
    for target in link_re.findall(text):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        path_part, _, anchor = target.partition("#")
        anchor = norm_anchor(anchor) if anchor else ""
        if path_part == "":                      # same-file anchor
            if anchor and anchor not in local_anchors:
                broken.append(f"{f.name} -> #{anchor}")
            continue
        dest = (f.parent / path_part).resolve()
        if not dest.exists():
            broken.append(f"{f.name} -> {path_part} (missing file)")
            continue
        if anchor and dest.suffix == ".md":
            if anchor not in headings_of(dest.read_text(encoding="utf-8")):
                broken.append(f"{f.name} -> {path_part}#{anchor}")
ok("Alle internen Links/Anchor aufloesbar", not broken, "; ".join(broken) if broken else "")

# ---- 6. rendered proof artifacts exist ----
ok("proof PNG existiert", (ROOT / "proof/architecture-diagram.png").exists())
ok("proof SVG existiert", (ROOT / "proof/architecture-diagram.svg").exists())

# ---- report ----
print("=" * 64)
print("E2E-VERIFIKATION: OpenHuman-Integration + Architektur-Diagramm")
print("=" * 64)
for cond, name, detail in checks:
    mark = "PASS" if cond else "FAIL"
    line = f"[{mark}] {name}"
    if detail: line += f"  ({detail})"
    print(line)
print("-" * 64)
total, passed = len(checks), sum(1 for c, _, _ in checks if c)
print(f"{passed}/{total} Checks bestanden")
sys.exit(1 if fails else 0)
