# Validation and evidence boundary

These are **tooling/integrity checks**, not a scientific gate PASS. The review supplies no newly pre-registered experiment, independent implementation validator, participant result, model-grader calibration, or backend measurement.

## Acquisition and source pin

The GitHub connector retrieved the merged source through the existing read-only reproduction workflow, run `33947494690`, artifact `9963782116`. Its archive SHA-256 was verified as `d24ac1db0cf668053d170d7bf9515ddf7095a7d2bbbe03345cb838a390c7b4c7`; the enclosed checked-source archive was verified as `8175fb67c5c0a2d6354d9d1c2830f57cd9dc90c100b5d339676d47822c3733c1`. The recorded source commit was `360d6ed15fbee7d38dc659f8324763bf637b3924`. The extracted BOOTSTRAP bytes reproduce Git blob `26c35a75d9d9fb81402a2705d5a0cf09099c310e`.

The native registry artifact was retrieved from run `33947494705`, artifact `9963783708`, archive SHA-256 `d5329cfd16cc479d7e9feae3ca70a61a22b13d51d43c1e67c7b1601c05d00aa2`. Its source commit matches the base. Both its before/after tracker ref and the subsequent live connector read resolve to `ca183ab6331adf1e51b5d533b6c5628a07b2fa1a` at `refs/dolt/data`. The historical workflow reported native registry success without writes. These CI archives expire on 2026-09-08; they are acquisition receipts, not permanent storage promises. Canonical source remains the named repository commit, and tracker authority remains the native Dolt ref. No full source or database archive is added to this packet.

## Reproduction

Run from the repository root:

```bash
python3 -m unittest discover -s research/tools/tests -v
python3 research/tools/check_links.py .
python3 research/programs/event-state/tools/validate_event_fluent_fixture.py research/programs/event-state/fixtures/amnesia-notes-event-fluent.json --output /tmp/event-state-review.json
python3 research/programs/prose/tools/validate_portfolio_prose_fixture.py research/programs/prose/fixtures/portfolio-about-event-fluent.json --output /tmp/prose-review.json
python3 research/programs/paired-synthesis/tools/validate_paired_domain.py research/programs/paired-synthesis/fixtures/paired-domain-proof.json /tmp/event-state-review.json /tmp/prose-review.json --output /tmp/paired-review.json
python3 research/packets/2026-09-04-phase-3-behavioral-probes/tools/run_experiments.py --output /tmp/behavioral-review.json
python3 research/tools/verify_migration.py research/packets/2026-09-04-phase-3-behavioral-probes/results/behavioral-probes.json /tmp/behavioral-review.json research/packets/2026-09-04-restructure-program-major/move-map.json
python3 research/tools/render_registry.py --check
```

The local run used Python 3.13.5, not the base CI's Python 3.12.3. Exact environment and raw stdout/stderr are in [raw-validation.txt](raw-validation.txt). The three fixture validation JSON outputs reproduce the already committed result bytes; their hashes/locations and the behavioral/migration comparisons are retained there. Frozen tools may emit legacy `pass-with-constraints`; that string is retained as historical tool output and is not the review verdict.

Local native `bd prime` and `render_registry.py --check` cannot succeed because the executable `bd` is absent. The latter must fail closed, not be bypassed with a fabricated database, imported JSONL, or edited generated registry. Fresh PR CI must run the existing native-registry workflow; its outcome is reported on the PR rather than anticipated here.

## Integrity review

The local diff is limited to BOOTSTRAP, RESEARCH, the owner decision log, the research navigation map, and this new packet. No existing packet, fixture, validator, program charter/result, workflow, source ledger, Beads database, or generated registry region is modified. Replaced controlling text is retained verbatim in BOOTSTRAP 32.5 and RESEARCH 29. All 47 original review questions and 52 original decision-queue items are reproduced exactly in the coverage matrix. The check counts establish traceability, not semantic completeness.

[Integrity manifest](integrity.json) records reviewed file digests, source comparisons, scope-preservation checks, and the unchanged behavioral experiment fingerprint. Its own enclosing commit is the publication identity; no circular self-hash or future commit SHA is claimed. The PR's actual head and CI results are the external revision receipt. No merge or research gate closure is authorized by a green run.
