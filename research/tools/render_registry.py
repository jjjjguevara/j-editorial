#!/usr/bin/env python3
"""Render the RESEARCH.md registry from native Beads; --check never writes.

The document's directory selects the tracker, not the caller's working directory.
Malformed or incomplete tracker reads fail closed rather than erasing programs.
No command here changes issues or synchronizes a remote. Rendered edits still
require the controlling-document review prescribed in RESEARCH.md section 21.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

BEGIN = "<!-- BEGIN GENERATED REGISTRY -->"
END = "<!-- END GENERATED REGISTRY -->"


class RegistryError(ValueError):
    """The tracker cannot safely render the committed program registry."""


def bd(root: Path, *args: str) -> list[dict]:
    result = subprocess.run(
        ["bd", *args, "--json"], cwd=root, text=True, capture_output=True,
        check=True, timeout=60,
    )
    data = json.loads(result.stdout)
    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list) or any(not isinstance(row, dict) for row in data):
        raise RegistryError("bd returned neither issue objects nor an issue list")
    return data


def metadata(issue: dict) -> dict:
    raw = issue.get("metadata")
    if isinstance(raw, str):
        raw = json.loads(raw)
    if raw is None:
        return {}
    if not isinstance(raw, dict):
        raise RegistryError(f"{issue.get('id', '?')}: metadata is not an object")
    return raw


def text(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip() or any(c in value for c in "|`\r\n"):
        raise RegistryError(f"missing or unsafe {field}")
    return value


def complete_metadata(root: Path, issue: dict, required: set[str]) -> dict:
    meta = metadata(issue)
    if not required.issubset(meta):
        issue_id = text(issue.get("id"), "issue id")
        shown = bd(root, "show", issue_id)
        if len(shown) != 1 or shown[0].get("id") != issue_id:
            raise RegistryError(f"{issue_id}: show did not return the requested issue")
        meta = metadata(shown[0])
    if not required.issubset(meta):
        raise RegistryError(f"{issue.get('id')}: missing metadata {sorted(required - meta.keys())}")
    return meta


def render(root: Path) -> str:
    epics = bd(root, "list", "--label", "research-program", "--all", "-n", "0", "--flat")
    # Child tasks can inherit their parent's labels; only program epics qualify.
    epics = [e for e in epics if e.get("issue_type") == "epic" and "gate" not in (e.get("labels") or [])]
    if not epics:
        raise RegistryError("no research-program epics; refusing an empty registry")
    rows = []
    slugs: set[str] = set()
    issue_ids: set[str] = set()
    gate_ids: set[str] = set()
    for epic in epics:
        eid = text(epic.get("id"), "epic id")
        if eid in issue_ids:
            raise RegistryError(f"duplicate issue id: {eid}")
        issue_ids.add(eid)
        meta = complete_metadata(root, epic, {"program_slug", "alias", "lifecycle", "charter", "results"})
        slug = text(meta["program_slug"], "program_slug")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug) or slug in slugs:
            raise RegistryError(f"invalid or duplicate program slug: {slug}")
        slugs.add(slug)
        for field, filename in (("charter", "CHARTER.md"), ("results", "RESULTS.md")):
            expected = f"research/programs/{slug}/{filename}"
            if meta[field] != expected or not (root / expected).is_file():
                raise RegistryError(f"{eid}: {field} must resolve to {expected}")
        gates = bd(root, "list", "--parent", eid, "--all", "-n", "0", "--flat")
        open_gates: list[str] = []
        closed_gates: list[str] = []
        for gate in gates:
            if "gate" not in (gate.get("labels") or []):
                continue
            gid = text(gate.get("id"), "gate issue id")
            if gid in issue_ids:
                raise RegistryError(f"duplicate issue id: {gid}")
            issue_ids.add(gid)
            gmeta = complete_metadata(root, gate, {"gate", "program_slug"})
            name = text(gmeta["gate"], "gate alias")
            if gmeta["program_slug"] != slug or name in gate_ids:
                raise RegistryError(f"{gid}: wrong program or duplicate gate alias {name}")
            gate_ids.add(name)
            status = text(gate.get("status"), "gate status")
            (closed_gates if status == "closed" else open_gates).append(name)
        rows.append((slug, text(meta["alias"], "alias"), text(meta["lifecycle"], "lifecycle"),
                     eid, text(epic.get("status"), "epic status"), sorted(open_gates), sorted(closed_gates)))
    programs = root / "research/programs"
    documented = {p.name for p in programs.iterdir() if p.is_dir() and
                  ((p / "CHARTER.md").exists() or (p / "RESULTS.md").exists())}
    if slugs != documented:
        raise RegistryError(f"tracker/program directory mismatch: tracker-only={sorted(slugs - documented)}, documents-only={sorted(documented - slugs)}")
    lines = [
        "| Program | Alias | Lifecycle | Beads epic | Epic status | Open gates | Closed gates | Charter | Results |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for slug, alias, lifecycle, eid, status, og, cg in sorted(rows):
        lines.append(
            f"| `{slug}` | {alias} | {lifecycle} | `{eid}` | {status} | {', '.join(f'`{g}`' for g in og) or '—'} | "
            f"{', '.join(f'`{g}`' for g in cg) or '—'} | [charter](research/programs/{slug}/CHARTER.md) | [results](research/programs/{slug}/RESULTS.md) |"
        )
    lines.extend(["", f"Rendered from `bd list` by `research/tools/render_registry.py`; {len(rows)} programs. Edit the tracker, not this table."])
    return "\n".join(lines)


def split_registry(content: str) -> tuple[str, str, str]:
    if content.count(BEGIN) != 1 or content.count(END) != 1:
        raise RegistryError("exactly one BEGIN/END registry marker pair is required")
    if content.index(BEGIN) > content.index(END):
        raise RegistryError("registry markers are reversed")
    head, rest = content.split(BEGIN, 1)
    current, tail = rest.split(END, 1)
    return head, current, tail


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", default="RESEARCH.md", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        path = args.file.resolve()
        head, current, tail = split_registry(path.read_text(encoding="utf-8"))
        block = render(path.parent)
        if args.check:
            if current.strip() == block.strip():
                print("registry up to date")
                return 0
            print("registry out of date", file=sys.stderr)
            return 1
        path.write_text(f"{head}{BEGIN}\n{block}\n{END}{tail}", encoding="utf-8")
        print(f"registry rendered into {path}; review the diff before committing")
        return 0
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        detail = exc.stderr if isinstance(exc, subprocess.CalledProcessError) else str(exc)
        print(f"registry unavailable or invalid: {detail}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
