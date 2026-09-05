# Owner decisions required to continue bootstrap

Status: **accepted research directions / D-03 research hold / one fixture decision open**  
Decision authority: **repository owner**  
Implementation gate: **remains closed**  
Dataset research: **held**

The first owner response is preserved in [`BOOTSTRAP-DECISION-ADDENDUM.md`](BOOTSTRAP-DECISION-ADDENDUM.md). The second response is preserved in [`BOOTSTRAP-DECISION-ADDENDUM-2.md`](BOOTSTRAP-DECISION-ADDENDUM-2.md).

## 1. Recorded decisions and directions

| ID | Recorded direction | Status |
|---|---|---|
| `D-01` | **C** — paired technical-reference and general-prose proof; `jjjjguevara/amnesia-docs` is the first technical-reference use case. | Accepted direction; prose artifact unresolved. |
| `D-02` | Research Gustavo Bueno's gnoseological space and other approaches rather than select `Gap`, `Finding`, `Obligation`, or `Event` prematurely. | Completed as the D-02R decision packet. |
| `D-02R` | **A** — use the Editorial Construction Space plus typed plural records as the falsifiable phase-2 research hypothesis. | Accepted as research direction only; not an ontology, schema, or persistence decision. |
| `D-03` | Research whether editorial history is better modeled as a Moore-style multidimensional state transition system over typed events, rather than as three independent layers. | Research further; no architecture selected and no owner answer requested yet. |
| `D-04` | **B for now** — retain meaningful semantic operations plus checkpoints. | Provisionally accepted, backend-neutral. |
| `AMN-01` | **A** — use pinned `jjjjguevara/amnesia` source and execution as the product oracle for the Amnesia Docs proof. | Accepted for research-only read, checkout, build, type-check, focused test, and CI use. |

## 2. Binding interpretation of D-02R

D-02R accepts a **research hypothesis**, not a production ontology:

- the Editorial Construction Space is a completeness scaffold;
- its constructive, referential, and pragmatic/governance axes are non-exclusive;
- one editorial datum may participate in several axes and relations simultaneously;
- the typed record family is a set of distinctions to test, not a requirement for one class, table, file, service, or store per type;
- `Gap` remains a derived adverse/unresolved view unless falsification tests establish otherwise;
- `EditorialEpisode` remains a candidate causal and evaluative envelope.

[`D-02-ACCEPTANCE.md`](D-02-ACCEPTANCE.md) records the limits of this acceptance.

## 3. D-03 research hold

The prior three-concern formulation—

1. artifact/source state;
2. editorial-semantic records;
3. derived projections/evaluations—

must not be interpreted as three physical or mutually exclusive layers.

The active D-03 question is whether a better account is:

```text
typed occurrences and transactions
        │
        ▼
multidimensional editorial state
        │
        ▼
state-derived projections and evaluations
```

The research must distinguish:

- an **event or occurrence** from a condition that continues to hold;
- a **fluent/fact/assertion** from the transaction that records it;
- an **atomic editorial transaction or episode** from each of its constituent facts;
- a **checkpoint** from a semantic projection;
- a storage order from causal order, branching, concurrency, and conflict;
- event time, valid/effective time, observation time, decision time, and recording time;
- a Moore-style output function from command handling and side effects.

The current favored research hypothesis is a **causal event–fluent editorial state machine**, not pure event sourcing. It is documented in [`D-03-EVENT-STATE-REVIEW.md`](../programs/event-state/D-03-EVENT-STATE-REVIEW.md).

A later `D-03R` packet may be issued only after the Amnesia trace and the required counterexamples are executed. No D-03 owner decision is requested now.

## 4. D-01P — What is the general-prose companion?

### A — Existing public-facing prose artifact

Use a real essay, explanatory article, case narrative, or other general-audience prose artifact from a repository controlled by the owner. Record the exact repository/path, audience, purpose, rights, evidence boundary, and review authority.

**Research recommendation: A.**

### B — Doc Doctor research article as a temporary fixture

Use `jjjjguevara/doc-doctor/docs/research/ui-ux/AI Editing Tool UI UX Research.md` initially.

This permits immediate integration work but weakly tests generality because the artifact remains technical/research prose.

### C — Purpose-built bounded prose fixture

Author a controlled article with deliberate evidence, structural, ambiguity, and alternative-rewrite cases.

This gives clean experimental controls but weaker real-history and adoption evidence.

## 5. Accepted AMN-01 boundary

Research may use `jjjjguevara/amnesia` and `jjjjguevara/amnesia-docs` at immutable refs to:

- inspect source and history;
- check out repositories in an authorized execution environment;
- build and type-check;
- run focused tests and CI;
- compare documentation claims with product types, exports, runtime wiring, tests, and observed behavior;
- preserve raw outputs and construct evaluation fixtures from faulty references, corrections, and editorial improvements.

This authority does not permit source mutation, pull requests, releases, deployment, production changes, or model-training corpus construction. The complete boundary is in [`AMNESIA-ORACLE-AUTHORIZATION.md`](AMNESIA-ORACLE-AUTHORIZATION.md).

## 6. Current answer format

Only D-01P currently requires an owner answer:

```text
D-01P: A + repository/path | B | C
Narrowing or additional constraint:
```

No answer releases the implementation gate, accepts an ADR, selects persistence, activates dataset research, or merges PR #1.
