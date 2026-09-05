# prose — Results

Entries are dated and cite their packet. Verdicts use the vocabulary of `RESEARCH.md` section 3.

## 2026-09-04 — Phase 2: candidate audit and D-01P

Packet: [`2026-09-04-phase-2-foundations`](../../packets/2026-09-04-phase-2-foundations/README.md)  
Pre-registration: none  
Executed by: bootstrap agent session; validated by: none; red team: none

### What ran

Source-system audit with twelve pinned records `PF-01` to `PF-12`, seed findings `PORT-F01` to `F06`, three alternative resolutions, and the `D-01P` decision packet accepted verbatim by the owner. See [`PORTFOLIO-PROSE-CANDIDATE-AUDIT.md`](PORTFOLIO-PROSE-CANDIDATE-AUDIT.md).

### Gate decomposition

| Obligation | Verdict | Evidence |
|---|---|---|
| Bounded artifact, purpose, rights, and evidence boundary | PASS | audit sections 1, 4, 5, 11 |
| Owner acceptance with preserved statement | PASS | "Yes proceed with A." |

## 2026-09-04 — Phase 2: prose fixture

Packet: same  
Pre-registration: none  
Executed by: bootstrap agent session; validated by: same lineage; red team: none

### What ran

`validate_portfolio_prose_fixture.py` over the 22-transaction fixture; `P-01` to `P-12` pass; the committed result reproduces byte-for-byte at the new path on 2026-09-04. See [`PORTFOLIO-PROSE-EXPERIMENT.md`](PORTFOLIO-PROSE-EXPERIMENT.md).

### Gate decomposition

| Obligation | Verdict | Evidence |
|---|---|---|
| Exact real checkpoint chain bound | PASS | `P-02`; independently re-verified below |
| Two real operation families without unique-gold claims | PASS | `P-03` |
| Representation of qualified evidence, disputed finding, three remedies, privacy branch, counterfactual staleness, goal-versioned readiness, separate authorities | NARROW | `P-04` to `P-12` verify author-written fields; the validator hard-codes transaction identifiers |
| Reviewer disagreement remains inspectable | NARROW | `P-07` compares two recommendation strings written by the fixture author for synthetic actors |
| Built-output parity, reader task, grader reliability, independent substantiation | DEFER (not executed) | packet section 9 |

### Evidence retention

| Record | Digest | Bytes committed at | Class after review |
|---|---|---|---|
| `evidence:prose-guard:e1` | `adbe4573…` | nowhere; the record states the tool was not re-executed | claim (5.8) |
| `evidence:fact-guard:e2` | `a5f68558…` | nowhere; same | claim (5.8) |
| `evidence:pinned-source:e0`, `owner-profile:e3` | `d6baf29b…`, `98ea7b05…` | nowhere | claim; the underlying blobs are pinned separately and verifiable |
| `evidence:review-a:e4`, `review-b:e5` | `85c3db06…`, `2255c555…` | nowhere; synthetic | scenario, not evidence |

## 2026-09-04 — Independent verification during the review

Packet: [`2026-09-04-restructure-program-major`](../../packets/2026-09-04-restructure-program-major/README.md)  
Executed by: review session independent of the fixture author; method: `git cat-file`, `git rev-parse`, `git log` in the local clone; class 5.4

### Observations

- Commit `1c93b60e…` and blob `d56c560f…` exist; the blob is the About page at that commit.
- Checkpoint blobs `e11905e3…` at `f66fa3d1…` and `5d3d5007…` at `900483708d…` resolve.
- The About page has no commits after the pin; the checked-out branch has 154 later commits elsewhere.
- The audit dates the prose-audit commit 2026-08-17; the local author date reads 2026-08-16. The difference is a time-zone or committer-date effect and was not resolved; it is a small instance of the named-times problem the framework studies.

### Gate decomposition

| Obligation | Verdict | Evidence |
|---|---|---|
| Pinned identities resolve | PASS | observations |
| Fixture claims about history | PASS with one date discrepancy noted | |

## Open gates

`PR-G1` and `PR-G2`, tracked in Beads under epic `j-editorial-cz0`.
