#!/usr/bin/env python3
"""Render the RESEARCH.md program registry from the Beads tracker.

Beads is the authoritative registry. This script reads every epic labeled
`research-program`, counts its gate tasks by status, and rewrites the block in
RESEARCH.md between the BEGIN/END GENERATED REGISTRY markers. Run it after any
tracker change that affects programs or gates. With --check it exits 1 when the
committed block differs from the rendered one and writes nothing.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

BEGIN = "<!-- BEGIN GENERATED REGISTRY -->"
END = "<!-- END GENERATED REGISTRY -->"


def bd(*args: str) -> list[dict]:
    out = subprocess.check_output(["bd", *args, "--json"], text=True)
    data = json.loads(out or "[]")
    return data if isinstance(data, list) else [data]


def metadata(issue: dict) -> dict:
    raw = issue.get("metadata")
    if isinstance(raw, str):
        try:
            return json.loads(raw or "{}")
        except json.JSONDecodeError:
            return {}
    return raw or {}


def render() -> str:
    epics = bd("list", "--label", "research-program", "--all", "-n", "0", "--flat")
    # Child tasks inherit their parent's labels in Beads; only epics are programs.
    epics = [e for e in epics if e.get("issue_type") == "epic" and "gate" not in (e.get("labels") or [])]
    rows = []
    for epic in epics:
        meta = metadata(epic)
        if not meta:
            shown = bd("show", epic["id"])
            meta = metadata(shown[0]) if shown else {}
        slug = meta.get("program_slug", "?")
        alias = meta.get("alias", "?")
        lifecycle = meta.get("lifecycle", "?")
        gates = bd("list", "--parent", epic["id"], "--all", "-n", "0", "--flat")
        gates = [g for g in gates if "gate" in (g.get("labels") or [])]
        open_gates = sorted(metadata(g).get("gate", g["id"]) for g in gates if g.get("status") != "closed")
        closed_gates = sorted(metadata(g).get("gate", g["id"]) for g in gates if g.get("status") == "closed")
        rows.append((slug, alias, lifecycle, epic["id"], epic.get("status", "?"), open_gates, closed_gates))
    rows.sort()
    lines = [
        "| Program | Alias | Lifecycle | Beads epic | Epic status | Open gates | Closed gates | Charter | Results |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for slug, alias, lifecycle, eid, status, og, cg in rows:
        lines.append(
            f"| `{slug}` | {alias} | {lifecycle} | `{eid}` | {status} | {', '.join(f'`{g}`' for g in og) or '—'} | "
            f"{', '.join(f'`{g}`' for g in cg) or '—'} | [charter](research/programs/{slug}/CHARTER.md) | [results](research/programs/{slug}/RESULTS.md) |"
        )
    lines.append("")
    lines.append(f"Rendered from `bd list` by `research/tools/render_registry.py`; {len(rows)} programs. Edit the tracker, not this table.")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", default="RESEARCH.md", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    text = args.file.read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        print("registry markers missing", file=sys.stderr)
        return 2
    head, rest = text.split(BEGIN, 1)
    current, tail = rest.split(END, 1)
    block = render()
    new_text = f"{head}{BEGIN}\n{block}\n{END}{tail}"
    if args.check:
        if current.strip() == block.strip():
            print("registry up to date")
            return 0
        print("registry out of date", file=sys.stderr)
        return 1
    args.file.write_text(new_text, encoding="utf-8")
    print(f"registry rendered into {args.file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
