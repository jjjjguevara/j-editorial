# Representation and history requirements — Phase 2 result

Status: **research result / workload defined / no substrate selected**  
Programs: `BR-REP` reconnaissance, `BR-HIST` reconnaissance  
Depends on: accepted D-02R and D-03 shape; executed technical fixture  
Dataset research: **not executed**

Source identifiers resolve in [`SOURCE-LEDGER.md`](../../packets/2026-09-04-phase-2-foundations/SOURCE-LEDGER.md).

## 1. Decision boundary

This phase does not ask “Which database is best?” It asks:

> What must any representation and history implementation preserve so that the accepted editorial model remains truthful, reproducible, queryable, erasable where required, and portable?

The answer must precede a backend bake-off.

## 2. Required logical components

### 2.1 Material checkpoint

Binds an exact artifact or external-evidence state:

```text
checkpoint identity
repository/object locator
immutable commit or content digest
path/resource identities
format/media type
capture method and environment
availability and rights
erasure/retention status
```

A checkpoint establishes identity and retrievability, not semantic correctness.

### 2.2 Event transaction

Records one accepted historical claim that an occurrence or atomic set of occurrences was recorded:

```text
transaction identity and type
causal parents
subject/stream and branch
command/proposal correlation
actor, role, authority
targets
event/effective/observation/decision/recording times
schema and reducer versions
evidence and checkpoint references
state effects
retention classification
```

An event is immutable as a historical assertion. Later contradiction, correction, invalidation, or redaction requires another record or an explicit retention operation.

### 2.3 Fluent/fact

Represents what holds over a state/time interval:

```text
subject
predicate/dimension
value or polarity
valid interval
asserted or derived status
initiating/terminating transactions
evidence and method
confidence/uncertainty
authority and applicability
```

A fluent is not required to be physically persisted if it can be reproduced deterministically and cheaply. A persisted fluent must declare whether it is primary, cached, or derived.

### 2.4 Projection

Produces a versioned view:

```text
input state head(s)
projection/reducer version
goal/norm/evidence versions
output
raw supporting records
execution environment
created time
determinism/reproduction status
```

Gap fields, readiness summaries, aggregate scores, dashboards, and reports are projections.

### 2.5 Target/selector resolution

Targets need more than line/character offsets. The candidate locator is a bundle:

```text
resource/checkpoint identity
semantic or symbolic identifier where available
structural path
text quote + bounded context where legally permissible
position/range hint
parser/normalization version
resolution result and confidence
ambiguity candidates
supersession/deletion relation
```

`REP-01`, `REP-03`, `REP-04`, `REP-05`, and `REP-06` establish that no single selector works across every representation and edit pattern.

## 3. Authority model

“Source,” “semantic,” and “projection” remain useful authority categories, but not physical layers.

| Question | Required authority |
|---|---|
| Which bytes existed? | Material checkpoint/content identity |
| Did a checker run? | Event transaction plus execution provenance |
| Is the check correct? | Evidence, method, validation, and possibly adjudication |
| Does an obligation apply? | Goal/norm version plus applicability rule |
| Was a proposal accepted? | Decision event by an authorized actor |
| Is the document ready? | Versioned projection plus release authority |
| Did the external product behave this way? | Pinned observation; internal history alone is insufficient |
| Can a deleted payload be replayed? | Retention record; never infer availability from an event ID |

No one category is universal ground truth.

## 4. Ordering and time requirements

### 4.1 Causal order

The logical history must support a DAG:

- zero or more causal parents;
- siblings representing independent or alternative work;
- explicit conflict;
- merge/adjudication with multiple parents;
- correlation across streams/repositories;
- supersession and reversal.

A durable store may assign a total sequence number. That number is an implementation order, not necessarily the editorial causal order. `EVT-06` and `EVT-07` support this distinction.

### 4.2 Named times

At minimum:

| Time | Meaning |
|---|---|
| event time | when the occurrence happened |
| valid/effective time | when the condition or rule applied |
| observation time | when an actor/tool observed it |
| decision time | when authority accepted/rejected/waived |
| recording/transaction time | when the ledger stored it |
| publication time | when a checkpoint became released |

Two physical columns may implement several of these only if semantic names and derivation remain unambiguous. `EVT-04` and `EVT-10` support late and retroactive knowledge.

## 5. Replay contract

The word “replay” must be qualified.

| Replay class | Promise |
|---|---|
| Event validation replay | Re-evaluate envelope integrity and causal references. |
| Semantic state replay | Reapply a named reducer version to available transactions. |
| Projection replay | Regenerate a named projection using pinned inputs and environment. |
| Material replay | Retrieve exact source bytes from a content identity/checkpoint. |
| External-observation replay | Re-run an external test/tool if its dependencies remain available. |
| Historical interpretation | Retain what an older reducer/projection reported, even when a newer interpretation differs. |

Prohibited claim:

```text
semantic event replay == exact source reconstruction
```

Erasure, unavailable dependencies, nondeterministic models, changed external services, and expired credentials can make some replay classes impossible. The ledger must state which class failed.

## 6. Schema/reducer evolution

The design must support:

- immutable event identities;
- explicit event-schema version;
- reader/upcaster version where used;
- reducer version;
- projection version;
- preserved original payload or digest where permissible;
- retained old projection output where legal/audit requirements demand it;
- migration reports rather than silent reinterpretation;
- ability to run two reducer versions over one history and compare outputs.

A migration that rewrites all old events in place would destroy the distinction between original history and later interpretation unless the rewrite itself is preserved as a migration event with old content identities.

## 7. Erasure and redaction

Append-only history does not override privacy and rights obligations. A candidate erasure operation must be able to:

- remove or cryptographically render inaccessible the protected payload;
- remove derived indexes, embeddings, caches, search stores, and exports where applicable;
- retain only permissible identity, authorization, causal, and digest metadata;
- declare whether the digest itself creates linkage or re-identification risk;
- record that exact replay is unavailable;
- prevent projections from silently rehydrating deleted data;
- propagate deletion to external providers and replicas where required;
- distinguish legal hold from ordinary retention.

The Phase 2 fixture models only the semantic disclosure, not a complete compliant deletion implementation.

## 8. Backend-exit contract

Before a substrate can be accepted, it must demonstrate export of:

1. exact material checkpoint locators and digests;
2. event transaction envelopes;
3. causal parent/branch/merge graph;
4. fluent/fact records or enough versioned logic to reproduce them;
5. goal/norm/authority/evidence references;
6. projection definitions and retained outputs;
7. schema/reducer/projection versions;
8. retention/erasure records and known replay loss;
9. ordering and temporal metadata;
10. opaque extension payloads without corrupting core semantics.

The export must be independently readable without the selected database server. A vendor snapshot alone is insufficient.

## 9. Candidate substrate roles

The candidates are not mutually exclusive; each may fill one role.

| Candidate | Natural role | Strength | Unresolved burden |
|---|---|---|---|
| Git | exact artifact checkpoints and interchange | Content addressing, branches, ubiquitous tooling | Semantic transactions/querying, between-commit edits, erasure |
| Dolt | versioned relational domain records | SQL, commits, branches, diff/history tables | Row identity/schema semantics, operation intent, large payload strategy |
| PostgreSQL + append journal | transactional semantic ledger and projections | Mature transactions, constraints, indexing, logical decoding | Branch/DAG semantics, temporal/event conventions, external checkpoint store |
| Temporal fact database | valid/system-time fact queries | Late knowledge and retroactive correction | Event intent, ecosystem, portability, branch semantics |
| Event store | domain transaction history | Intent-rich append log, optimistic concurrency, replay | Schema evolution, projection lag, migration/erasure, exact material states |
| CRDT/Automerge/Yjs | collaborative source operations and relative anchors | Convergence, change DAGs or resilient positions | Authority, semantic truth, persistence maturity, payload growth |
| DeltaDB/Delta | fine-grained edit/conversation history comparator | Claimed operation identity and between-commit context | Private-beta interface, durability, licensing, deployment, portability, independent testing |
| Object store/content-addressed blobs | large evidence/checkpoint payloads | Immutable objects, digest verification, lifecycle policies | Semantic index, transactions, branch/authority model |

A likely architecture may compose several roles. Composition itself carries synchronization and failure risks and must be tested rather than assumed.

## 10. Workload for the bake-off

Every candidate or composition must execute the same workload:

1. import the Phase 2 event–fluent fixture;
2. reconstruct state at every transaction head;
3. retrieve exact docs/product checkpoints or report authorized unavailability;
4. query one finding across all simultaneous roles;
5. query all events/facts affecting one obligation;
6. branch three remedies from one parent and adjudicate them;
7. record late knowledge with effective and recording times;
8. replay under two reducer versions without overwriting either result;
9. move/rewrite/delete a target and report resolution/ambiguity;
10. redact an evidence payload and remove derived indexes;
11. recover from an interrupted transaction/projection update;
12. export and import into a neutral test harness;
13. verify digests and causal graph integrity;
14. measure query latency, write amplification, storage growth, and operational complexity;
15. demonstrate backend exit without losing declared semantics.

## 11. Acceptance metrics

A backend comparison must report at least:

- semantic coverage;
- exact-checkpoint fidelity;
- transaction atomicity;
- causal DAG support;
- temporal query support;
- target-resolution behavior;
- replay/versioning behavior;
- erasure effectiveness and residual data;
- corruption/recovery behavior;
- export completeness;
- vendor/service dependency;
- deployment and operations burden;
- storage and query cost;
- migration cost;
- security boundary;
- licensing and long-term availability.

No aggregate score may conceal a failed hard requirement.

## 12. Current recommendation

Adopt the **event–fluent + exact-checkpoint model as the workload contract**, not as a physical architecture.

Keep these options open through the bake-off:

```text
A. event ledger + checkpoint store + projections
B. temporal fact store + explicit transaction/causal records + checkpoint store
C. relational journal + causal graph + checkpoint store
D. checkpoint-first system with a smaller semantic journal
E. a composition involving a CRDT or DeltaDB when independently testable
```

The first three appear most capable of satisfying the logical model; the fourth remains the simplicity control; the fifth remains experimental.

## 13. Gate result

Representation/history reconnaissance is sufficiently specified to begin an implementation-neutral bake-off in a compatible environment. It is not sufficient to accept an ADR or select a backend.
