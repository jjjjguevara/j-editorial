#!/usr/bin/env python3
"""Check relative Markdown links across the repository.

Reports links whose target file or directory does not exist. Anchors are not
verified. URLs with a scheme and pure in-page anchors are skipped. Exit status
is 1 when any link is dangling, so the check can run as a quality gate.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
SKIP_DIRS = {".git", ".delta", "node_modules", ".beads"}


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    dangling: list[str] = []
    checked = 0
    for path in sorted(root.rglob("*.md")):
        if SKIP_DIRS & set(path.relative_to(root).parts):
            continue
        text = path.read_text(encoding="utf-8")
        for match in LINK.finditer(text):
            target = match.group(2)
            if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            file_part = target.split("#", 1)[0]
            if not file_part:
                continue
            resolved = (path.parent / file_part).resolve()
            checked += 1
            if not resolved.exists():
                rel = path.relative_to(root).as_posix()
                dangling.append(f"{rel}: [{match.group(1)}]({target})")
    print(f"checked {checked} relative links in {root}")
    for row in dangling:
        print("DANGLING " + row)
    return 1 if dangling else 0


if __name__ == "__main__":
    raise SystemExit(main())
