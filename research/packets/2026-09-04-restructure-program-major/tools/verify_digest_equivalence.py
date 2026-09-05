#!/usr/bin/env python3
"""Show that the post-restructure Phase 3 run equals the original run up to input path keys.

The runner keys its input digests by repository path, so moving the fixtures changed
the experiment digest. This script maps the new input keys back to the original
paths, recomputes the digest with the runner's own encoding, and compares every
other section of the experiment record verbatim.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


def encoded(value) -> bytes:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def main() -> int:
    original = json.load(open(sys.argv[1], encoding="utf-8"))
    rerun = json.load(open(sys.argv[2], encoding="utf-8"))
    key_map = json.load(open(sys.argv[3], encoding="utf-8"))["moves"]
    reverse = {new: old for old, new in key_map.items()}
    exp_new = rerun["experiment"]
    remapped = dict(exp_new)
    remapped["inputs"] = {reverse.get(k, k): v for k, v in exp_new["inputs"].items()}
    sections = {
        s: (original["experiment"][s] == exp_new[s])
        for s in ("checks", "legacy_validator_mutations", "representation_measurements", "target_results")
    }
    inputs_equal = remapped["inputs"] == original["experiment"]["inputs"]
    recomputed = hashlib.sha256(encoded(remapped)).hexdigest()
    result = {
        "original_experiment_sha256": original["experiment_sha256"],
        "rerun_experiment_sha256": rerun["experiment_sha256"],
        "rerun_digest_with_original_input_keys": recomputed,
        "digests_equivalent_up_to_input_paths": recomputed == original["experiment_sha256"],
        "sections_identical": sections,
        "input_digests_identical_after_key_mapping": inputs_equal,
        "checks_passed": [original["checks_passed"], rerun["checks_passed"]],
        "environments": {"original": original["environment"], "rerun": rerun["environment"]},
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    Path(sys.argv[4]).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0 if result["digests_equivalent_up_to_input_paths"] and all(sections.values()) and inputs_equal else 1


if __name__ == "__main__":
    raise SystemExit(main())
