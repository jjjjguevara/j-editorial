# Phase 3 — behavioral integrity, targeting, and evaluation protocols

Status: **executed bounded research / review packet / production hold**  
Authority: owner instruction to merge PR #2 and continue the contract  
Base: `0d24e78713ed7a2c04810ce9961e5c28ab3da096`  
Branch: `research/bootstrap-phase-3-representation-evaluation`  
Research cutoff: **2026-09-04**  
Dataset research: **not executed**

PR #2 is merged. Its artifact-selection decisions are not reopened. This phase
moves beyond declarative fixture checks to executable causal and corruption tests.
It also performs the controlling-document consistency work previously specified
in `research/bootstrap/NEXT-PHASE-CONTRACT.md`.

## Authority boundary

D-01C, D-02R, D-03, D-04B, AMN-01 and D-01P-A remain accepted research directions.
No production representation, backend, language, package, API or ADR is selected.
Amnesia and the portfolio remain unchanged. No protected Field Notes, unpublished
personal records, model-provider calls, dataset curation or training are included.

The archived source of J-Editorial is public. Only bounded About/API fragments
needed for the targeting experiment are included. Whole private source trees,
credentials and installed dependency archives are not added to the research packet.

## Evidence map

| Artifact | Role |
|---|---|
| `RESULTS.md` | Method, results, negative evidence, alternatives and limitations |
| `EVALUATION-PROTOCOL.md` | Proposed goal, prior, grader and adjudication contracts; no empirical study claims |
| `SOURCE-LEDGER.md` | Primary sources and exact repository provenance |
| `STAGE-GATE.md` | Bounded pass, unresolved gates and released research |
| `fixtures/target-fragments.json` | Four pinned fragments; not a training or benchmark corpus |
| `tools/run_experiments.py` | Standard-library behavioral probes on unchanged Phase 2 inputs |
| `tools/align_contracts.py` | Four-file allowlisted, hash-guarded owner-decision alignment |
| `results/behavioral-probes.json` | Actual checks, observed/expected results, inputs and environment |
| `results/contract-alignment.json` | Exact before/after identities for controlling documents |

## Reproduction

From repository root, with Python 3.11+ and Git installed:

```bash
python3 research/phase-3/tools/run_experiments.py --output /tmp/je-phase3.json
```

Expected: **67/67 bounded checks**, `pass-with-constraints`, experiment digest:

```text
323ad6f84a3fde8175e2ed99d8754cd45357d3c7841d4f4c67af210e2c8c05aa
```

The stable experiment digest excludes environment version strings but includes
all observed/expected values, source input digests and measured representation
sizes. Each run records its environment separately. This is Python sorted-key
compact JSON, not RFC 8785 canonicalization or an authenticity signature.

Temporary Git/SQLite stores are deleted when the runner exits. No network or paid
provider is used by the experiment. The GitHub execution transport separately
uses pinned Actions to obtain a public checkout and retain bounded artifacts.
Initial run `33913135453` independently reproduced all three retained Phase 2
results byte-for-byte. That validates reproduction, not empirical prose quality.

`align_contracts.py --apply` refuses an unexpected old hash, transforms only four
explicit paths, and verifies exact expected new hashes. It is idempotent after
alignment. No dataset charter content is researched: only its status and upstream
dependency terminology are aligned.

## Research is not task tracking

Beads remains the native task authority. Results, gates and this evidence map are
not substitute task records. The separate native-tracker probe installs verified
Beads/Dolt releases in an ephemeral runner and attempts `bd prime`, `bd bootstrap`,
`bd list` and `bd ready` without creating issues or pushing tracker state. Its exit
codes, not the Actions job's green indicator, determine tracker accessibility.
