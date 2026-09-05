#!/usr/bin/env python3
"""One-time consolidation of the legacy source ledgers into research/LEDGER.md.

Parses the heading-and-bullet ledger (phase 1) and the table ledgers (phases
1.1, 1.2, 2, 3 and the portfolio audit), deduplicates sources by shared URL,
assigns stable SRC identifiers in order of first appearance, and emits the
unified ledger with a legacy-identifier map and a collision register. It does
not alter any legacy ledger; banners are added separately.
"""
from __future__ import annotations

import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

ID_RE = re.compile(r"^`?([A-Z]{1,5}-\d{2,3}|S\d{2})`?$")
URL_RE = re.compile(r"https?://[^\s)\]>]+")
HEADING_RE = re.compile(r"^### ([A-Z]{1,5}-\d{2}) — (.+)$")

LEDGERS = [
    ("research/packets/2026-09-04-phase-1-adversarial-review/SOURCE-LEDGER.md", "phase 1"),
    ("research/packets/2026-09-04-phase-1-adversarial-review/PHASE-2-SOURCE-LEDGER.md", "phase 1.1"),
    ("research/packets/2026-09-04-phase-1-adversarial-review/D-03-SOURCE-LEDGER.md", "phase 1.2 (D-03)"),
    ("research/packets/2026-09-04-phase-2-foundations/SOURCE-LEDGER.md", "phase 2"),
    ("research/programs/prose/PORTFOLIO-PROSE-CANDIDATE-AUDIT.md", "phase 2 portfolio audit"),
    ("research/packets/2026-09-04-phase-3-behavioral-probes/SOURCE-LEDGER.md", "phase 3"),
]

CLASS_RULES = [
    (r"github\.com/jjjjguevara|api\.github\.com|jjjjguevara/", "5.4 repository observation"),
    (r"arxiv\.org|doi\.org|aclanthology\.org|escholarship\.org|cl\.cam\.ac\.uk|microsoft\.com/en-us/research", "5.2 peer-reviewed / archival research"),
    (r"zed\.dev|learn\.microsoft\.com|anthropic\.com/engineering|crfm\.stanford\.edu", "5.3 industrial / SOTA practice"),
    (r"fgbueno\.es", "5.1 primary text (philosophical source, used as analytic comparator)"),
    (r"w3\.org|rfc-editor\.org|ietf\.org|spec\.commonmark\.org|spec\.openapis\.org|spdx\.github\.io|tei-c\.org|cidoc-crm\.org|ifla\.org|ica\.org|researchobject\.org|nanopub\.net|slsa\.dev|in-toto|cloudevents|git-scm\.com|sqlite\.org|postgresql\.org|datomic\.com|xtdb\.com|dolthub\.com|prosemirror\.net|yjs\.dev|automerge\.org|tree-sitter|pandoc\.org|vale\.sh|redocly\.com|diataxis\.fr|eur-lex|nist\.gov|owasp\.org|github\.com/(openai|UKGovernmentBEIS|gastownhall|cloudevents|in-toto)|doc\.ic\.ac\.uk", "5.1 primary specification / documentation"),
]


def classify(urls: list[str], source: str, legacy_id: str = "") -> str:
    if re.match(r"^(AMN|PF|DD|R)-", legacy_id):
        return "5.4 repository observation"
    text = " ".join(urls) + " " + source
    for pattern, label in CLASS_RULES:
        if re.search(pattern, text):
            return label
    if "`jjjjguevara/" in source or "GitHub Actions" in source:
        return "5.4 repository observation"
    return "unclassified (assign manually)"


def split_row(line: str) -> list[str]:
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return cells


def parse_tables(text: str):
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].startswith("|") and i + 1 < len(lines) and re.match(r"^\|\s*:?-{2,}", lines[i + 1]):
            header = split_row(lines[i])
            i += 2
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            yield header, rows
        else:
            i += 1


def parse_headings(text: str):
    entries = []
    current = None
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if m:
            current = {"id": m.group(1), "title": m.group(2), "bullets": OrderedDict()}
            entries.append(current)
            continue
        if line.startswith("## ") or line.startswith("# "):
            current = None
            continue
        if current is not None and line.startswith("- "):
            key, _, value = line[2:].partition(":")
            current["bullets"][key.strip()] = value.strip()
    return entries


def main() -> int:
    root = Path(sys.argv[1]).resolve()
    out = root / "research/LEDGER.md"
    records = []  # dicts: ledger, label, legacy_id, source, version, establishes, limitation, urls
    repo_rows = []
    for rel, label in LEDGERS:
        text = (root / rel).read_text(encoding="utf-8")
        for entry in parse_headings(text):
            b = entry["bullets"]
            source = b.get("Source", entry["title"])
            establishes = "; ".join(v for k, v in b.items() if k in ("Supports", "Relevance", "Use", "Used for"))
            records.append(dict(ledger=rel, label=label, legacy_id=entry["id"], source=source, version="",
                                establishes=establishes, limitation=b.get("Limitation", ""), urls=URL_RE.findall(source)))
        for header, rows in parse_tables(text):
            h = [c.lower() for c in header]
            if not rows:
                continue
            if h[:2] == ["source", "immutable revision"]:
                for r in rows:
                    if len(r) >= 3:
                        repo_rows.append(dict(ledger=rel, label=label, source=r[0], ref=r[1], use=r[2]))
                continue
            for r in rows:
                if not r or not ID_RE.match(r[0]):
                    continue
                legacy_id = ID_RE.match(r[0]).group(1)
                cells = r + [""] * (5 - len(r))
                if len(header) >= 5:
                    source, version, establishes, limitation = cells[1], cells[2], cells[3], cells[4]
                elif len(header) == 4 and any(k in h[2] for k in ("ref", "immutable")):
                    source, version, establishes, limitation = cells[1], cells[2], cells[3], ""
                else:
                    source, version, establishes, limitation = cells[1], "", cells[2], cells[3]
                records.append(dict(ledger=rel, label=label, legacy_id=legacy_id, source=source, version=version,
                                    establishes=establishes, limitation=limitation, urls=URL_RE.findall(source)))
    # union-find over shared URLs
    parent = list(range(len(records)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    by_url: dict[str, int] = {}
    for idx, rec in enumerate(records):
        for url in rec["urls"]:
            key = url.rstrip("/").lower()
            key = key.replace("https://www.dolthub.com/docs/", "https://docs.dolthub.com/")
            key = re.sub(r"https://eur-lex\.europa\.eu/eli/reg/2016/679.*", "https://eur-lex.europa.eu/eli/reg/2016/679", key)
            if key in by_url:
                parent[find(idx)] = find(by_url[key])
            else:
                by_url[key] = idx
        if not rec["urls"]:
            key = "text:" + re.sub(r"\W+", " ", rec["source"]).strip().lower()
            if key in by_url:
                parent[find(idx)] = find(by_url[key])
            else:
                by_url[key] = idx
    groups: OrderedDict[int, list[int]] = OrderedDict()
    for idx in range(len(records)):
        groups.setdefault(find(idx), []).append(idx)
    unified = []
    for n, (rootidx, members) in enumerate(groups.items(), 1):
        first = records[members[0]]
        legacy = [f"{records[m]['label']} `{records[m]['legacy_id']}`" for m in members]
        unified.append(dict(id=f"SRC-{n:03d}", source=first["source"], version=first["version"],
                            establishes=first["establishes"], limitation=first["limitation"],
                            cls=classify(first["urls"], first["source"], first["legacy_id"]), legacy=legacy, members=members))
    for k, r in enumerate(repo_rows, len(unified) + 1):
        unified.append(dict(id=f"SRC-{k:03d}", source=r["source"], version=r["ref"], establishes=r["use"],
                            limitation="", cls="5.4 repository observation",
                            legacy=[f"{r['label']} repository-evidence row (no legacy ID)"], members=[]))
    # legacy map and collisions
    legacy_map = []
    seen: dict[str, set[str]] = {}
    for u in unified:
        for m in u["members"]:
            rec = records[m]
            legacy_map.append((rec["label"], rec["ledger"], rec["legacy_id"], u["id"]))
            seen.setdefault(rec["legacy_id"], set()).add(u["id"])
    collisions = sorted((lid, sorted(ids)) for lid, ids in seen.items() if len(ids) > 1)

    def cell(s: str) -> str:
        return s.replace("|", "\\|").replace("\n", " ").strip() or "—"

    lines = []
    lines.append("# j-editorial — Unified source ledger\n")
    lines.append("Status: **canonical source registry for all research programs**  ")
    lines.append("Created: **2026-09-04**, by consolidating the five legacy ledgers and the portfolio audit table  ")
    lines.append("Rule: **new research cites `SRC-###` identifiers only; identifiers are never reused or renumbered**\n")
    lines.append("## Rules\n")
    lines.append("- A source establishes only what its row says. Its presence selects nothing.")
    lines.append("- Add a new row at the end for a new source; never edit an identifier. Correcting a row is a normal edit; superseding a source adds a row and notes the supersession.")
    lines.append("- The `Class` column follows the evidence taxonomy in `RESEARCH.md` section 5. Classes were assigned mechanically by host during consolidation and are provisional until a program author confirms them.")
    lines.append("- The legacy ledgers remain frozen inside their packets. Their identifiers were file-scoped and collide across files; the map below resolves each `(ledger, legacy ID)` pair to one unified identifier.")
    lines.append("- A digest without retrievable bytes is a claim, not evidence. Rows that bind private repositories give repository, path, and immutable ref; verification requires authorized access.\n")
    lines.append(f"## Sources ({len(unified)} rows)\n")
    lines.append("| ID | Source | Version / date / ref | Class | Establishes | Limitation | Legacy IDs |")
    lines.append("|---|---|---|---|---|---|---|")
    for u in unified:
        lines.append(f"| `{u['id']}` | {cell(u['source'])} | {cell(u['version'])} | {cell(u['cls'])} | {cell(u['establishes'])} | {cell(u['limitation'])} | {cell('; '.join(u['legacy']))} |")
    lines.append("\n## Collision register\n")
    lines.append("Legacy identifiers that named different sources in different ledgers. Any citation of these identifiers in a legacy document must be read against the ledger that document names at its top.\n")
    lines.append("| Legacy ID | Unified IDs it resolved to |")
    lines.append("|---|---|")
    for lid, ids in collisions:
        lines.append(f"| `{lid}` | {', '.join(f'`{i}`' for i in ids)} |")
    lines.append("\n## Legacy identifier map\n")
    lines.append("| Legacy ledger | Legacy ID | Unified ID |")
    lines.append("|---|---|---|")
    for label, ledger, lid, uid in sorted(legacy_map, key=lambda t: (LEDGERS.index(next(l for l in LEDGERS if l[0] == t[1])), t[2])):
        lines.append(f"| {label} — `{ledger}` | `{lid}` | `{uid}` |")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    summary = dict(records=len(records), unified=len(unified), repo_rows=len(repo_rows), collisions=collisions,
                   unclassified=[u["id"] for u in unified if u["cls"].startswith("unclassified")])
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
