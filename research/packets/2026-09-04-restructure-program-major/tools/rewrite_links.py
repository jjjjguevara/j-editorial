#!/usr/bin/env python3
"""One-time link and path rewrite for the 2026-09-04 program-major restructure.

For every Markdown file, each relative link is resolved against the file's
location before the move, mapped through move-map.json, and re-relativized
from the file's location after the move. Repository-root path strings that
appear as plain text or inline code are then replaced, followed by the four
renamed directory prefixes. The script prints every file it rewrote and every
link it could not resolve. It performs no other edit.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path, PurePosixPath

LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
SKIP_DIRS = {".git", ".delta", "node_modules", ".beads"}


def norm(path: str) -> str:
    return PurePosixPath(os.path.normpath(path)).as_posix()


def main() -> int:
    root = Path(sys.argv[1]).resolve()
    plan = json.load(open(sys.argv[2], encoding="utf-8"))
    moves: dict[str, str] = plan["moves"]
    reverse = {new: old for old, new in moves.items()}
    dir_renames: dict[str, str] = plan["directory_renames"]
    report: list[str] = []
    for path in sorted(root.rglob("*.md")):
        if SKIP_DIRS & set(path.relative_to(root).parts):
            continue
        new_rel = path.relative_to(root).as_posix()
        old_rel = reverse.get(new_rel, new_rel)
        old_dir = str(PurePosixPath(old_rel).parent)
        new_dir = str(PurePosixPath(new_rel).parent)
        original = path.read_text(encoding="utf-8")
        text = original

        def substitute(match: re.Match[str]) -> str:
            label, target = match.group(1), match.group(2)
            if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                return match.group(0)
            file_part, sep, anchor = target.partition("#")
            if not file_part:
                return match.group(0)
            old_abs = norm(file_part) if old_dir == "." else norm(f"{old_dir}/{file_part}")
            new_abs = moves.get(old_abs, old_abs)
            for old_prefix, new_prefix in dir_renames.items():
                if old_abs.rstrip("/") == old_prefix.rstrip("/"):
                    new_abs = new_prefix.rstrip("/")
            if not (root / new_abs).exists():
                report.append(f"UNRESOLVED {new_rel}: ({target}) -> {new_abs}")
            new_target = PurePosixPath(os.path.relpath(new_abs, "." if new_dir == "." else new_dir)).as_posix()
            return f"[{label}]({new_target}{sep}{anchor})"

        text = LINK.sub(substitute, text)
        for old, new in sorted(moves.items(), key=lambda kv: -len(kv[0])):
            text = text.replace(old, new)
        for old, new in sorted(dir_renames.items(), key=lambda kv: -len(kv[0])):
            text = text.replace(old, new)
        if text != original:
            path.write_text(text, encoding="utf-8")
            report.append(f"REWROTE {new_rel}")
    print("\n".join(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
