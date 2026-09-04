# D-03 event/state review — beyond layers, scalars, and vector analogues

Status: **research synthesis / D-03 hold / not an architecture**  
Research cutoff: **2026-09-04**  
D-02R: **A accepted as research hypothesis**  
D-04: **B provisionally accepted**  
AMN-01: **A accepted for research-only use**  
Implementation: **blocked**  
Dataset research: **not executed**

Source identifiers resolve in [`D-03-SOURCE-LEDGER.md`](D-03-SOURCE-LEDGER.md) and [`PHASE-2-SOURCE-LEDGER.md`](PHASE-2-SOURCE-LEDGER.md).

## 1. Executive result

The owner's D-03 objection is valid.

The provisional language of three authority “layers” risks two category errors:

1. treating material source state, editorial semantics, and derived evaluation as mutually exclusive containers; and
2. treating an editorial datum as if it must occupy one scalar position or one vector coordinate at a time.

A stronger research hypothesis is:

```text
Causal event–fluent editorial state machine

typed occurrences and atomic transactions
  evolve heterogeneous, multidimensional state;

facts/fluents express what holds across intervals;

content-addressed checkpoints bind exact material states;

versioned projections expose source, semantic,
evaluation, and readiness views;

causal parentage preserves branches, concurrency,
conflict, and merge.
```

This is not yet a choice of event sourcing, database, serialization, reducer framework, or physical topology.

## 2. The core correction: axes are not layers

The accepted Editorial Construction Space has constructive, referential, and pragmatic/governance axes. Those axes classify relations and participation. They do not partition records.

A single finding such as “the documented `commands.notes.getNotes()` signature omits the required `bookId` parameter” can simultaneously be:

- a typed assertion by a checker;
- evidence against a parity claim;
- an adverse finding under a goal-contract obligation;
- the output of an observation operation;
- targeted to a documentation node and product symbol;
- situated in a review dialogue;
- governed by release and authority rules;
- a cause of a readiness-state change.

Splitting these roles into three “truth layers” would duplicate identity, create reconciliation work, and obscure the fact that they concern one editorial datum.

The correct invariant to test is:

> One datum may carry or participate in multiple dimensions and relations at the same time, while each assertion about it retains source, actor, authority, time, and confidence.

This is a product-state or relational structure, not a Euclidean vector. No addition, magnitude, direction, norm, or distance is implied.

## 3. What a Moore-style model contributes

A Moore-style machine separates transition from observation:

```text
S' = δ(S, e)
Y  = λ(S)
```

where:

- `S` is current editorial state;
- `e` is an accepted event or occurrence;
- `δ` evolves state;
- `Y` is an output or projection determined by state;
- `λ` produces that projection.

This is useful for claims such as:

- readiness is derived from current obligations, findings, waivers, evidence, and policy;
- a gap field is a projection of unresolved adverse conditions;
- a document dashboard is an output of state rather than canonical truth;
- two projection versions may expose the same underlying state differently.

However, a literal classical Moore machine is too narrow:

- editorial state is open-ended and data-bearing, not a small finite set;
- commands may be invalid, rejected, or ambiguous;
- human and model judgments can produce alternatives rather than one deterministic next state;
- branches and concurrent reviews create several valid successor states;
- external product changes occur outside the editorial machine;
- side effects and newly emitted events can depend on both current state and input.

The working term should therefore be **Moore-style extended state machine**, supplemented by statechart, event-calculus, and causal-history concepts. [EVT-01, EVT-02, EVT-03]

## 4. Orthogonal state solves the simultaneity concern

Statecharts extend conventional state machines with hierarchy, concurrency/orthogonality, and communication. SCXML's parallel-state semantics makes the key point concrete: when a parallel parent is active, all child regions are active; one event is processed across those regions and can trigger distinct transitions before the macrostep completes. [EVT-02, EVT-03]

For J-Editorial, a candidate state is a heterogeneous product:

```text
S =
  MaterialState
  × GoalState
  × NormativeState
  × EpistemicState
  × OperationalState
  × AuthorityState
  × ReleaseState
  × RetentionState
```

Example state after discovering an API mismatch:

```text
MaterialState:     docs checkpoint D0 unchanged
GoalState:         API-reference goal G1 active
NormativeState:    signature-parity obligation unsatisfied
EpistemicState:    adverse finding F1 supported by product evidence
OperationalState:  remediation not yet proposed
AuthorityState:    maintainer decision pending
ReleaseState:      parity=full unsupported / review reopened
RetentionState:    raw checker output retained
```

One accepted transaction may change epistemic, normative, operational, and release regions atomically while leaving the material region unchanged.

This answers the owner's concern more directly than three layers: **simultaneous dimensions live in one state configuration**.

## 5. Events are not everything that exists

An event-stream design becomes distorted if every concept is forced into “event.”

The research must distinguish at least five categories.

### 5.1 Occurrence/event

Something happened:

- a product commit became available;
- a checker ran;
- a reviewer asserted a finding;
- an operation was accepted;
- a checkpoint was published.

An event is past-tense and immutable as a historical claim. Its record may later be contradicted, redacted, or superseded, but it is not edited into a different occurrence.

### 5.2 Fluent or time-scoped fact

Something holds during a time or state interval:

- obligation O1 is applicable;
- finding F1 is unresolved;
- reviewer R has delegated authority;
- checkpoint D0 is the current candidate;
- release state is blocked;
- an evidence object supports an assertion.

Event Calculus explicitly separates events from fluents they initiate or terminate. Work on contract monitoring similarly represents normative state as relations and variables holding at a particular time, changed by events. [EVT-04, EVT-05]

### 5.3 Atomic fact or datum

A fine-grained assertion relates an identified subject, predicate/dimension, value, transaction, and assertion/retraction status.

Datomic's datom model is a useful comparator because one immutable fact carries entity, attribute, value, transaction, and added/retracted dimensions, while a transaction atomically accrues a set of facts and can itself carry provenance. [EVT-09, EVT-10]

The lesson is not “use Datomic.” It is that a single editorial act can preserve several atomic assertions without reducing the act to one scalar status.

### 5.4 Transaction or episode

One causally coherent editorial act may contain several changes:

```text
transaction T17:
  finding F1 asserted
  obligation O1 marked unsatisfied
  parity claim P1 marked unsupported
  release assessment moved review -> blocked
  raw evidence E9 linked
```

Those are several state effects under one actor, authority, cause, and atomic decision boundary.

`EditorialEpisode` may group several transactions and observations into a larger unit, such as “identify, correct, and verify the notes-reference mismatch.”

### 5.5 Checkpoint and projection

A checkpoint binds exact material state, such as repository, commit, path tree, build artifact, or content hash.

A projection is derived:

- current unresolved gaps;
- readiness score;
- reviewer dashboard;
- evaluation report;
- source-to-semantic index.

A projection may be regenerated; an exact historical checkpoint cannot be replaced by a newly rendered equivalent without declaring the substitution.

## 6. A better command/event boundary

Commands, proposals, and events should not be conflated.

A candidate functional boundary is:

```text
decide:
  State × Command
    -> Accepted Event Transaction
     | Rejection / Abstention

evolve:
  State × Event Transaction
    -> New State

project:
  State × Projection Version
    -> View / Evaluation / Readiness Output
```

Examples:

- `ProposeCorrection` is a command.
- `CorrectionProposed` is an event only after the proposal is recorded.
- `AcceptCorrection` is a command requiring authority.
- `CorrectionAccepted` is an event.
- `PatchApplicationFailed` is an event even though no material post-state exists.
- `SignatureParityObserved` is an observation event, not proof that the observation is correct.
- `FindingSupported` is a state relation derived or asserted from evidence under a versioned method.

This separation lets invalid or unauthorized commands fail without rewriting history and lets rejected proposals remain evaluable.

## 7. The stream cannot be merely linear

A physical log may serialize writes, but editorial causality is not always one total sequence.

Examples:

- two reviewers assess the same checkpoint independently;
- a docs correction and product API change occur on separate repositories;
- two valid rewrites branch from one prose paragraph;
- one branch accepts a waiver while another resolves the underlying problem;
- a merge adjudicates rather than simply interleaves both histories.

Lamport's happened-before relation and event structures support representing causal dependence separately from arbitrary wall-clock or storage ordering. Event structures also preserve conflict and concurrency as first-class relations. [EVT-06, EVT-07]

A candidate event envelope therefore needs:

```text
event_id
event_type
stream_or_subject_id
parent_event_ids[]
branch_id
caused_by / correlation_id
actor / role / authority
target_ids[]
event_time
valid_or_effective_time
observed_at
recorded_at
schema_version
reducer_version
payload_or_payload_ref
evidence_refs[]
checkpoint_refs[]
retention_class
```

The parent relation may form a DAG. Merge/adjudication events may have multiple parents. A total storage sequence may coexist for durability, but it must not erase causal independence.

CRDT research may help with convergent text and operation transport, but convergence cannot decide editorial truth, authority, or acceptable resolution. [EVT-08]

## 8. Time is multidimensional too

At minimum, D-03 must test:

- **event time** — when the underlying occurrence happened;
- **valid/effective time** — when a fact, norm, or product condition applied;
- **observation time** — when an actor or tool observed it;
- **decision time** — when authority accepted, rejected, or waived it;
- **recording/transaction time** — when the ledger learned it;
- **publication time** — when a checkpoint was released.

Bitemporal systems distinguish valid time from transaction time and permit later records about earlier or future effective states. That is a strong baseline, but editorial work may require more named times rather than overloading two columns. [EVT-13]

Example:

```text
product behavior changed:  June 10
docs remained unchanged:   June 10–20
checker observed mismatch: June 18
finding recorded:          June 18
correction accepted:       June 19
docs published:            June 20
```

Collapsing this into one timestamp would prevent accurate staleness duration, response-time, and causal evaluation.

## 9. Event sourcing is a candidate, not the conclusion

Event sourcing offers attractive properties:

- intent-rich append-only history;
- replay and state reconstruction;
- materialized projections;
- snapshots/checkpoints;
- auditability;
- optimistic concurrency.

It also creates significant burdens:

- event and reducer schema evolution;
- projection lag and eventual consistency;
- expensive rehydration;
- migration lock-in;
- correction through compensating events rather than mutation;
- privacy and erasure conflicts;
- replay dependence on external services and nondeterministic graders;
- risk that low-level deltas become a meaningless change log.

Current architecture guidance explicitly treats event sourcing as a complex, selective pattern rather than a universal default. [EVT-11]

D-03 must therefore compare four candidates.

| Candidate | Canonical emphasis | Strength | Principal risk |
|---|---|---|---|
| Pure event-first | domain-event stream | clear intent and replay | enduring facts and external truth become awkward; replay/versioning burdens |
| Fact/datom-first | temporal atomic assertions/retractions | multidimensional data and provenance | operations, causal intent, and branch episodes may become indirect |
| Event–fluent hybrid | occurrences/transactions plus time-scoped facts and checkpoints | preserves what happened and what holds | larger semantic model and reconciliation discipline |
| Checkpoint + journal | exact source states plus operation audit | source fidelity and simpler migration | journal may be insufficient for full semantic reconstruction |

**Current research preference:** event–fluent hybrid with causal parentage and exact checkpoints. This preference is provisional and must survive the experiments.

## 10. Candidate model

The candidate is named only for research:

> **Causal Editorial Event–Fluent Model**

### 10.1 Ledger

Stores typed occurrences or atomic transaction envelopes, immutable identities, causal parents, temporal metadata, actor/authority, targets, evidence/checkpoint refs, and schema versions.

### 10.2 Reducer/evolution function

A versioned function applies accepted events to state:

```text
S_n = evolve(reducer_v, parent_state(s), event_n)
```

Invalid historical events are not silently skipped. A failed or rejected operation becomes an explicit outcome.

### 10.3 Multidimensional state

State contains heterogeneous components rather than one refinement number or numeric vector. Components may be normalized or projected internally, but their simultaneous relationships remain queryable.

### 10.4 Fluent/fact view

Represents conditions that hold, their provenance, applicability, polarity, confidence, and temporal interval. Positive, adverse, uncertain, conflicting, waived, and unevaluated states remain distinct.

### 10.5 Material checkpoints

Bind exact artifact and external-evidence states using immutable repository refs, hashes, and environment records. Semantic replay does not manufacture source bytes.

### 10.6 Projections

Versioned functions generate gaps, scores, readiness, reports, indexes, dashboards, and eval instances. Historical projection output may be retained when exact audit or nondeterministic computation requires it.

### 10.7 Causal graph

Preserves branch, conflict, concurrency, supersession, reversal, merge, and adjudication independently of storage order.

## 11. Worked Amnesia trace

AMN-01 authorizes use of pinned product evidence and the evolving docs history. A minimal trace for `commands.notes` can be:

### T0 — bind the oracle

```text
DocsCheckpointBound(D0 = amnesia-docs@5d8aa677...)
ProductCheckpointBound(P0 = amnesia@4d0d1efe...)
GoalContractActivated(G1)
```

State effects:

- material docs/product checkpoints become addressable;
- the API-reference goal and parity obligations become applicable;
- no finding is implied yet.

### T1 — execute checks

```text
ParityCheckExecuted(
  docs=D0,
  product=P0,
  checker=C1,
  environment=ENV1,
  raw_output=E1
)
```

The occurrence records that a check ran. It does not alone say the result is true.

### T2 — record one multidimensional finding transaction

```text
FindingTransactionRecorded(
  finding=F1,
  target_docs=commands-notes.md#getNotes,
  target_product=NotesCommands.getNotes,
  claim="documented signature omits required bookId",
  polarity=adverse,
  evidence=E1 + pinned source,
  obligation=O-signature-parity,
  confidence=deterministic-high,
  actor=C1,
  authority=checker-observation-only
)
```

Atomic state effects:

- epistemic: F1 exists and is supported;
- normative: O-signature-parity is unsatisfied at D0/P0;
- operational: remediation is open;
- release: `parity: full` is unsupported;
- material: D0 remains unchanged;
- authority: release disposition remains pending.

This is one datum with many dimensions, not several unrelated layer copies.

### T3 — branch on correction

```text
Branch A: CorrectDocumentationProposed(...)
Branch B: ChangeProductSurfaceProposed(...)
Branch C: ParityClaimDowngradeProposed(...)
```

All may be valid proposals. They share parents but are not forced into one total semantic order.

### T4 — adjudicate and apply

```text
ProposalAccepted(A, authority=maintainer)
DocumentationOperationApplied(A, pre=D0, post=D1)
DocsCheckpointMaterialized(D1)
```

The accepted transaction can update workflow, authority, and material state together.

### T5 — verify and project

```text
ParityCheckExecuted(D1, P0, C1, ENV1, E2)
VerificationRecorded(F1, resolved)
ReleaseAssessmentRecorded(readiness=reviewable)
```

The gap and readiness views are Moore-like projections of the resulting state. The exact raw outputs remain evidence.

### External-change variant

If product state moves from P0 to P1 while docs remain D1, a new `ProductCheckpointObserved(P1)` event may reopen an obligation or finding without any documentation edit. This tests whether state change is driven by referent events as well as source-edit events.

## 12. Replay constraints

Replay is only meaningful relative to:

- event schema version;
- reducer/evolution version;
- goal and norm versions;
- selector/target resolver version;
- external evidence checkpoints;
- grader/tool/model version and environment;
- retention/redaction state.

For deterministic domain transitions, the system should reproduce state exactly.

For human or model judgments, the system may only reproduce the recorded observation unless the original environment and model are available. Rerunning can create a **new observation event**, not overwrite the old result.

If reducer version 2 interprets old events differently, both must remain expressible:

```text
state as originally computed under reducer v1
state recomputed under reducer v2
```

Silent retrospective reinterpretation would falsify the audit history.

## 13. Erasure boundary

Immutable events conflict with deletion and privacy requirements when payloads contain sensitive material.

The model must test:

- content-addressed payload indirection;
- redaction/tombstone events;
- deleting or crypto-shredding payloads while retaining permissible metadata;
- index and projection cleanup;
- explicit `replay_incomplete` or `payload_erased` status;
- retention of causal and authority identity only where lawful and authorized.

It must never claim complete replay after required evidence has been erased.

## 14. Falsification tests

Reject or narrow the candidate if it cannot represent:

1. one event updating several orthogonal state regions atomically;
2. one datum participating in all three Editorial Construction Space axes;
3. an event that changes epistemic/release state but not material state;
4. a material checkpoint change with no implied quality improvement;
5. an enduring obligation or finding without emitting repeated pseudo-events;
6. late discovery of an earlier product change;
7. concurrent reviewer findings with neither falsely ordered nor collapsed;
8. alternative valid branches and an authority-bearing merge;
9. an operation failure with no post-checkpoint;
10. a waiver that changes release state without making the adverse finding false;
11. reducer/schema evolution without silent historical mutation;
12. a nondeterministic grader rerun as a new observation;
13. payload erasure with honest replay limitations;
14. exact source reconstruction where semantic projection is lossy;
15. source, semantic, and eval views from one underlying state without identity duplication;
16. export to another backend without changing domain meaning.

## 15. Revised D-03 decision boundary

D-03 should no longer ask “which of three layers is authoritative?”

A later D-03R packet should ask:

> Which combination of event occurrences, time-scoped facts/fluents, atomic transactions, material checkpoints, and projections is minimally sufficient to preserve exact source state, multidimensional editorial meaning, causal history, authority, and reproducible evaluation?

The candidate options should be populated only after experiments. The current provisional primary is the causal event–fluent hybrid.

## 16. Consequences for D-04

D-04B remains compatible:

- meaningful editorial operations become typed event transactions;
- accepted, rejected, failed, waived, and abstained outcomes remain explicit;
- exact material states are checkpoints;
- every keystroke remains out of scope;
- finer-grained Delta/CRDT histories may be linked later as subordinate evidence.

D-04B does not itself prove that the event stream is the sole system of record.

## 17. Non-conclusions

This review does not:

- choose event sourcing;
- require a classical finite Moore machine;
- make every editorial concept an event;
- select Datomic, XTDB, Git, Dolt, PostgreSQL, DeltaDB, or a CRDT;
- require one global linear stream;
- select JSON, JSON-LD, RDF, SQL, or another serialization;
- define a production schema or API;
- resolve D-03R;
- authorize implementation or dataset research.
