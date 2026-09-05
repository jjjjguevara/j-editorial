# Owner decision log

Status: **authoritative index of owner decisions and their provenance**  
Rule: **a decision is recorded as accepted only where the owner's own words are preserved; otherwise it is a recorded direction awaiting confirmation**  
Related: [`OWNER-DECISIONS.md`](OWNER-DECISIONS.md) (question packets), the two addenda, and the acceptance records in this directory

This log exists because decision authority thinned across the bootstrap phases: early decisions carry the owner's words, later ones carry only an agent's summary. Under `RESEARCH.md` section 21 no controlling document may be revised on the strength of a decision that lacks a verbatim owner statement.

## Provenance qualification — PR #3

D-01, D-03 acceptance, and D-04 now have recovered conversation excerpts. [The reconciliation receipt](PR-3-RECONCILIATION.md) records their reported timestamps and the retrieval limitation. These rows do not claim independently authenticated transcript bytes, do not introduce new decisions, and do not amend the accepted research scope. The prior missing-statement findings are preserved below rather than silently erased.

## Decisions

| ID | Date | Question | Owner statement (verbatim) | Recorded direction | Record | Provenance |
|---|---|---|---|---|---|---|
| `D-01` | 2026-09-04 | First end-to-end proof | Recovered excerpt in [PR #3 reconciliation](PR-3-RECONCILIATION.md#d-01--source-turn-2026-09-04t073521z) | C: paired technical-reference and general-prose proof; `jjjjguevara/amnesia-docs` is the technical half | [`BOOTSTRAP-DECISION-ADDENDUM.md`](BOOTSTRAP-DECISION-ADDENDUM.md) | Prior acceptance recovered through conversation retrieval; original transcript not independently archived. |
| `D-02` | 2026-09-04 | Semantic center | *not preserved* | Research further; do not select `Gap`, `Finding`, `Obligation`, or `Event` prematurely; study Bueno's gnoseological space | [`BOOTSTRAP-DECISION-ADDENDUM.md`](BOOTSTRAP-DECISION-ADDENDUM.md) | Paraphrased. Superseded by `D-02R`. |
| `D-02R` | 2026-09-04 | Editorial Construction Space plus typed plural records as phase-2 hypothesis | "For D-02, yes this is the right direction. (A)" | A accepted as a research hypothesis only | [`BOOTSTRAP-DECISION-ADDENDUM-2.md`](BOOTSTRAP-DECISION-ADDENDUM-2.md), [`D-02-ACCEPTANCE.md`](D-02-ACCEPTANCE.md) | Verbatim. |
| `D-03` (challenge) | 2026-09-04 | Representation authority: three layers versus event-stream state | "For D-03, wouldn't it make sense to conceptualize each as an event on an event stream (Moore-machine model)? We might be negating the possibility of a single editorial "datum" having multiple dimensions at the same time. It might be deeper than a flawed scalar, or a vector analogue. We should research further before locking." | Research hold; compare event-first, fact-first, event–fluent, and checkpoint+journal models | [`BOOTSTRAP-DECISION-ADDENDUM-2.md`](BOOTSTRAP-DECISION-ADDENDUM-2.md) | Verbatim. |
| `D-03` (acceptance) | 2026-09-04 | Causal event–fluent shape accepted as research direction | Recovered excerpt in [PR #3 reconciliation](PR-3-RECONCILIATION.md#d-03--source-turn-2026-09-04t085312z) | Accepted for the next research stage, not as a persistence architecture | [`D-03-ACCEPTANCE.md`](D-03-ACCEPTANCE.md) | Prior acceptance recovered through conversation retrieval; original transcript not independently archived. Scientific and architecture gates remain open. |
| `D-04` | 2026-09-04 | Minimum history guarantee | Recovered excerpt in [PR #3 reconciliation](PR-3-RECONCILIATION.md#d-04--source-turn-2026-09-04t073521z) | B **for now**: meaningful semantic operations plus checkpoints; backend-neutral | [`BOOTSTRAP-DECISION-ADDENDUM.md`](BOOTSTRAP-DECISION-ADDENDUM.md) | Prior acceptance recovered through conversation retrieval; original transcript not independently archived. |
| `AMN-01` | 2026-09-04 | Research-only use of the private Amnesia product repository as oracle | "AMN-01 - yes, (A). The corpus of docs is in development, so it's a good source for faulty references and trackable updates and editorial improvements." | A accepted for read, checkout, build, type-check, focused-test, and CI use; no mutation | [`BOOTSTRAP-DECISION-ADDENDUM-2.md`](BOOTSTRAP-DECISION-ADDENDUM-2.md), [`AMNESIA-ORACLE-AUTHORIZATION.md`](AMNESIA-ORACLE-AUTHORIZATION.md) | Verbatim. |
| `D-01P` | 2026-09-04 | General-prose companion artifact | "Yes proceed with A." | A: `jjjjguevara/sci-jjjjguevara/src/pages/about.astro` at commit `1c93b60e…`, blob `d56c560f…` | [`D-01P-ACCEPTANCE.md`](D-01P-ACCEPTANCE.md) | Verbatim. |
| `PR-2-MERGE` | 2026-09-04 | Merge Phase 2 and continue | "Ok, you can merge and continue with the next phase. Continue executing the contract." | PR #2 merged at `0d24e787…`; Phase 3 executed on a branch | [Phase 3 publication manifest](../packets/2026-09-04-phase-3-behavioral-probes/PUBLICATION-MANIFEST.json) | Verbatim. This statement did not authorize CI-authored edits to `BOOTSTRAP.md`; see `RESEARCH.md` section 21. |
| `REVIEW-1` | 2026-09-04 | Independent review of phases 1–3 | "Review the results of the Bootstrap run we just executed for j-editorial. Challenge all assumptions made that might be scientifically or epistimically unsound. Push back on anything that might've been left untouched for this phase of the repo work. Propose a path forward to continue the work, whether to execute the research immediately, or to dive deeper in the RESEARCH.md shape so that we have a better structure for the downstream work." | Review delivered in session; findings summarized in the restructure packet | [Restructure packet](../packets/2026-09-04-restructure-program-major/README.md) | Verbatim. |
| `RESTRUCTURE-1` | 2026-09-04 | Apply the proposed restructuring | "Please apply the reestructuring proposed." | Program-major layout, unified ledger, decision log, method rules, Beads registry; no research claims, no implementation, no dataset work | [Restructure packet](../packets/2026-09-04-restructure-program-major/README.md) | Verbatim. Does not release the implementation, persistence, ADR, dataset, or bootstrap-exit gates. |

## How to confirm a paraphrased decision

Add the owner's statement to the row, change the provenance cell to "Verbatim", and reference the commit or message where it was made. Until then, documents that depend on the decision should say "recorded direction" rather than "accepted".

## What no decision above authorizes

- production implementation, schemas, APIs, packages, or agents;
- selection of a persistence engine, event store, database, CRDT, serialization, or language;
- acceptance of an ADR;
- model-training dataset research, corpus construction, labeling, or training;
- mutation of `amnesia`, `amnesia-docs`, `sci-jjjjguevara`, or Doc Doctor;
- release of the `ADVERSARIAL-REVIEW-REQUIRED` gate.

## Superseded provenance assessments — before PR #3 reconciliation

These are the original rows, preserved verbatim. Their missing-record assessments describe the repository before conversation-context recovery, not an absence of historical owner approval. The retrieval qualification above remains current.

| ID | Date | Question | Owner statement (verbatim) | Recorded direction | Record | Provenance |
|---|---|---|---|---|---|---|
| `D-01` | 2026-09-04 | First end-to-end proof | *not preserved* | C: paired technical-reference and general-prose proof; `jjjjguevara/amnesia-docs` is the technical half | [`BOOTSTRAP-DECISION-ADDENDUM.md`](BOOTSTRAP-DECISION-ADDENDUM.md) | Paraphrased by the recording agent. Confirmation requested. |
| `D-03` (acceptance) | 2026-09-04 | Causal event–fluent shape accepted as research direction | *not preserved* | Accepted as research direction; not a persistence architecture | [`D-03-ACCEPTANCE.md`](D-03-ACCEPTANCE.md) | **Provenance gap.** The record states the owner accepted the shape but preserves no owner statement. The last preserved owner words on D-03 are "research further before locking". Treat as a recorded direction until the owner confirms in this log. |
| `D-04` | 2026-09-04 | Minimum history guarantee | *not preserved* | B for now: meaningful semantic operations plus checkpoints; backend-neutral | [`BOOTSTRAP-DECISION-ADDENDUM.md`](BOOTSTRAP-DECISION-ADDENDUM.md) | Paraphrased ("Choose B for now, given current access to the Delta client"). Confirmation requested. |
