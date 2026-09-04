# J-Editorial bootstrap adversarial review

Status: **PHASE 1.2 / D-02R AND AMN-01 ACCEPTED / D-03 EVENT–STATE RESEARCH HOLD**  
Repository base: **`fdfffb0da4eabd7c3db7d303013e0777db149e82`**  
Research cutoff: **2026-09-04**  
Controlling contract: **`BOOTSTRAP.md`**  
Repository gate: **`ADVERSARIAL-REVIEW-REQUIRED`**  
Implementation authorization: **not granted**  
Dataset-research execution: **not performed**

## Purpose

This directory records execution of the J-Editorial bootstrap contract before architecture or implementation. Phase 1 challenged the initial product model. Phase 1.1 selected the paired-proof direction, researched the semantic center, and audited the Amnesia technical slice. Phase 1.2 records D-02R and AMN-01 acceptance and reopens D-03 around event, state, time, concurrency, and multidimensional editorial data.

## Current result

- D-01 selects a paired technical-reference and general-prose proof.
- `jjjjguevara/amnesia-docs` is the technical half; the exact prose artifact remains open.
- D-02R accepts the Editorial Construction Space plus typed plural records as a **falsifiable research hypothesis**.
- Its three axes are non-exclusive analytic coordinates, not storage layers.
- AMN-01 authorizes pinned, research-only use of the private Amnesia product repository as an executable oracle.
- The changing Amnesia Docs corpus may supply faulty-reference, correction, and improvement episodes.
- D-03 remains open. The current research candidate is a causal event–fluent state machine with multidimensional state, transactions, checkpoints, and projections.
- D-04 still provisionally requires meaningful semantic operations plus checkpoints.
- The implementation, ADR, persistence, and dataset-research gates remain closed.

## Work completed

### Phase 1

1. inspected the live repository and controlling documents;
2. audited Doc Doctor as prior art rather than normative specification;
3. tested the domain model against annotation, provenance, history, evaluation, security, and erasure standards;
4. compared representation and persistence strategies without selecting one;
5. stress-tested technical, subjective, branching, policy-version, deletion, and hostile-content cases;
6. opened draft PR #1 at the required owner-decision hold.

### Phase 1.1

1. recorded D-01C, the D-02 research instruction, the D-03 dependency, and provisional D-04B;
2. translated Gustavo Bueno's gnoseological space cautiously into an editorial completeness scaffold;
3. compared that scaffold with provenance, annotation, constraint, policy, textual, archival, assertion, and discourse models;
4. separated analytic coordinates from canonical persisted record semantics;
5. derived a typed-pluralism hypothesis and retained `Gap` as a candidate projection;
6. inspected pinned `amnesia-docs` and `amnesia` states;
7. found real API-documentation parity conflicts in `commands.notes` and `expandCapabilities`;
8. defined the candidate Amnesia goal contract, obligation families, graders, and history episode.

### Phase 1.2

1. recorded owner acceptance of D-02R option A;
2. recorded research-only AMN-01 option A authorization;
3. rejected any implication that the three D-03 authority concerns require separate or exclusive layers;
4. researched Moore machines, statecharts, Event Calculus, event structures, causal order, temporal fact ledgers, event sourcing, and bitemporal records;
5. separated events, fluents/facts, transactions/episodes, checkpoints, and projections;
6. proposed a causal event–fluent state-machine hypothesis for falsification;
7. added an Amnesia transition trace and D-03 experiment gate;
8. preserved D-01P and the later D-03R decision rather than filling them implicitly.

## Work deliberately not performed

This work did not:

- implement framework code, schemas, APIs, adapters, editors, servers, or graders;
- modify `amnesia-docs`, `amnesia`, or Doc Doctor;
- select Git, Dolt, PostgreSQL, Datomic, XTDB, DeltaDB, a CRDT, event sourcing, a language, or a framework;
- accept an ADR;
- change or release the bootstrap gate;
- merge or modify `main`;
- acquire, generate, transform, label, split, benchmark, or train on a model-training dataset;
- treat repository history or accepted edits as model-training truth;
- manually edit `.beads` data.

## Artifact map

| Artifact | Role |
|---|---|
| [`SOURCE-LEDGER.md`](SOURCE-LEDGER.md) | Phase-1 repository, standard, evaluation, persistence, and security evidence |
| [`ADVERSARIAL-REVIEW.md`](ADVERSARIAL-REVIEW.md) | Phase-1 findings, stress tests, and initial recommendations |
| [`BOOTSTRAP-DECISION-ADDENDUM.md`](BOOTSTRAP-DECISION-ADDENDUM.md) | First owner response and its limits |
| [`BOOTSTRAP-DECISION-ADDENDUM-2.md`](BOOTSTRAP-DECISION-ADDENDUM-2.md) | D-02R acceptance, D-03 challenge, and AMN-01 authorization |
| [`D-02-SEMANTIC-CENTER-REVIEW.md`](D-02-SEMANTIC-CENTER-REVIEW.md) | Bueno translation, alternatives, and original D-02R packet |
| [`D-02-ACCEPTANCE.md`](D-02-ACCEPTANCE.md) | Binding interpretation and limits of accepted D-02R option A |
| [`D-03-EVENT-STATE-REVIEW.md`](D-03-EVENT-STATE-REVIEW.md) | Moore-style, event–fluent, transaction, causality, time, and replay research |
| [`D-03-SOURCE-LEDGER.md`](D-03-SOURCE-LEDGER.md) | Primary and official sources for the D-03 review |
| [`AMNESIA-DOCS-SLICE-AUDIT.md`](AMNESIA-DOCS-SLICE-AUDIT.md) | Pinned technical-use-case audit and concrete parity findings |
| [`AMNESIA-ORACLE-AUTHORIZATION.md`](AMNESIA-ORACLE-AUTHORIZATION.md) | Accepted research-only source and execution boundary |
| [`PHASE-2-SOURCE-LEDGER.md`](PHASE-2-SOURCE-LEDGER.md) | Sources added during phase 1.1 |
| [`OWNER-DECISIONS.md`](OWNER-DECISIONS.md) | Accepted directions, active research holds, and remaining owner question |
| [`NEXT-PHASE-CONTRACT.md`](NEXT-PHASE-CONTRACT.md) | Original research fan-out and gates |
| [`PHASE-1.2-EXECUTION-ADDENDUM.md`](PHASE-1.2-EXECUTION-ADDENDUM.md) | Changes to the next-phase graph after D-02R and AMN-01 acceptance |

## Active research boundary

`BR-FRAME`, `BR-DOM`, `BR-AMN`, `BR-SEC`, and the new D-03 event/state experiments may proceed as research. `BR-PROSE`, paired synthesis, and any claim of framework generality remain blocked by D-01P.

D-03 is not ready for an owner architecture choice. The next packet must test whether the candidate model can preserve:

- one datum with simultaneous dimensions;
- event occurrence versus enduring state;
- atomic multi-dimension transitions;
- positive, adverse, uncertain, and disputed findings;
- branch, merge, conflict, and causal concurrency;
- valid/effective time versus recorded time;
- deterministic replay across reducer/schema versions;
- exact source checkpoints and external referents;
- erasure without fictitious history;
- non-deterministic human and model observations.

## Tracking constraint

The repository requires Beads as the durable tracker. The available runtime still lacks compatible `bd` and `dolt` execution against the repository's Dolt-backed store. No direct database or JSONL mutation has been made. The native fan-out procedure remains specified in `NEXT-PHASE-CONTRACT.md` and must run in a compatible checkout.

## Resume condition

The next immediate owner input is D-01P. D-03R will be issued only after the event/state experiments produce evidence. Controlling-document revision must preserve D-02R and AMN-01 verbatim while keeping D-03, implementation, persistence, ADR, and dataset research behind their explicit gates.
