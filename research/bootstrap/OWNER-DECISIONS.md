# Owner decisions required to continue bootstrap

Status: **pivotal product decision hold**  
Decision authority: **repository owner**  
Implementation gate: **remains closed**

These questions cannot be answered safely as incidental implementation details. Each answer changes the framework's proof obligations and research sequence.

Record answers in the form:

```text
D-01: A | B | C
D-02: A | B | C
D-03: A | B | C
D-04: A | B | C
Narrowing or additional constraint:
```

## D-01 — What is the first end-to-end product proof?

### A — Bounded Markdown API-reference slice

Use one versioned OpenAPI description and one Markdown reference document. Exercise goals, obligations, findings/gaps, evidence, operations, history, deterministic graders, human review, and release policy.

**Advantages**

- strongest available objective oracle;
- directly compatible with docs-as-code;
- enough subjective surface to test human judgment;
- bounded fixture and clear failure cases;
- natural path into Doc Doctor after the core contract is proven.

**Risk**

The framework may overfit API/reference documentation unless a different second slice is required early.

### B — General Doc Doctor Markdown slice

Start from the current Doc Doctor ontology and a general prose document.

**Advantages**

- immediate product continuity;
- direct test of the existing user workflow;
- broader editorial concerns appear immediately.

**Risk**

Weak/subjective ground truth can make it difficult to distinguish ontology failure from grader disagreement. Existing scalar and stub assumptions may become accidental architecture.

### C — Paired API-reference and general-prose slices

Develop both as co-equal first proofs.

**Advantages**

- stronger early evidence of generality;
- catches technical-doc overfitting.

**Risk**

Doubles ontology, fixture, prior, grader, and adjudication complexity before the core semantics are stable.

**Research recommendation:** **A**, with B as the first generalization gate rather than an independent late product.

## D-02 — What is the semantic center?

### A — Gap-centered

`Gap` is the primary editorial object. Obligations and findings are represented through gap types and resolution state.

**Consequence:** closest to Doc Doctor, but positive evidence, waivers, disputes, and neutral observations require awkward gap semantics.

### B — Obligation/Finding-centered

Goal contracts define `Obligation` records. Artifact review produces general `Finding` records. `Gap` is an adverse/unresolved finding family or a projection over unsatisfied obligations.

**Consequence:** more explicit model; supports positive, negative, uncertain, waived, and disputed observations without redefining all of them as deficits.

### C — Event-centered

An append-only event stream is primary; artifact states, obligations, findings, gaps, and release status are projections.

**Consequence:** strongest audit orientation but makes event evolution and projection correctness foundational before the domain is stable.

**Research recommendation:** **B**, with first-class operations/events but not event sourcing as an assumed implementation.

## D-03 — Which authority model should representation research optimize?

### A — Source-first

Exact source files are canonical. Semantic structures are derived and disposable.

**Consequence:** simplest exact-source and Git story; weaker stable identity and semantic editing.

### B — Structured-first

A typed tree/graph is canonical. Markdown and other formats are projections.

**Consequence:** strongest semantic operations; greatest exact-round-trip and extension-loss risk.

### C — Split authority by concern

Exact source snapshots are authoritative for artifact representation. A separate semantic record is authoritative for goals, obligations, findings, evidence, provenance, operations, and evals. Mappings are versioned and can be stale/ambiguous.

**Consequence:** most honest fidelity boundary; adds reconciliation and consistency work.

**Research recommendation:** **C**.

## D-04 — What is the minimum historical guarantee for the first slice?

### A — Accepted checkpoints only

Record imported state, selected checkpoints/releases, and diffs.

**Consequence:** easiest Git-compatible proof; cannot reliably recover why a state changed or connect an accepted edit to evidence.

### B — Explicit semantic operations plus checkpoints

Record meaningful proposed/accepted/rejected editorial operations, their pre/post state, actor/authority, evidence, verification, and resulting checkpoints. Do not retain every keystroke.

**Consequence:** supports causal evaluation and agent training/eval evidence later without requiring live collaboration.

### C — Continuous edit history

Capture every edit/delta with stable identity and collaboration semantics, including between checkpoints.

**Consequence:** strongest replay/collaboration capability; likely requires CRDT/operation-log research and substantially expands the first product.

**Research recommendation:** **B**.

## Effects of the answer

After the answer is recorded, phase 2 can:

- revise `BOOTSTRAP.md`, `ROADMAP.md`, and `RESEARCH.md`;
- scope-revise—but not execute—the model-training data charter;
- define the accepted first ontology and goal-contract research slices;
- create the representation/history/evaluation/security research charters;
- create the native Beads dependency graph when a compatible `bd` environment is available;
- define representative experiments and acceptance criteria;
- keep ADRs and implementation blocked until those program gates pass.

No answer releases the implementation gate by itself.
