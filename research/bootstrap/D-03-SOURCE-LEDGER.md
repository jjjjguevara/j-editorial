# D-03 event/state source ledger

Status: **research evidence / no architectural authority**  
Research cutoff: **2026-09-04**  
Scope: Moore-style state, orthogonality, event/fluent distinctions, causal order, temporal facts, event sourcing, and event envelopes  
Dataset research: **not executed**

This ledger supplements [`SOURCE-LEDGER.md`](SOURCE-LEDGER.md) and [`PHASE-2-SOURCE-LEDGER.md`](PHASE-2-SOURCE-LEDGER.md). A source establishes only the pattern or limitation stated below.

## 1. Sequential and orthogonal state models

| ID | Source | Version/date | Use | Limitation |
|---|---|---|---|---|
| `EVT-01` | E. F. Moore, [“Gedanken-Experiments on Sequential Machines”](https://doi.org/10.1515/9781400882618-006), in *Automata Studies* | original 1956; reissued 2016 | Historical basis for state machines whose observable outputs are associated with state. Supports testing `S' = δ(S,e)` and `Y = λ(S)` as a narrow formal analogy. | A classical finite deterministic machine is too restrictive for open-ended artifacts, evidence, branches, and human adjudication. |
| `EVT-02` | David Harel, [“Statecharts: A Visual Formalism for Complex Systems”](https://doi.org/10.1016/0167-6423(87)90035-9) | 1987 | Extends conventional state machines with hierarchy, concurrency/orthogonality, and communication. Supports simultaneous active dimensions rather than one exclusive state label. | Reactive-system formalism; it does not define editorial facts, provenance, source fidelity, or authority. |
| `EVT-03` | W3C, [State Chart XML (SCXML) 1.0](https://www.w3.org/TR/scxml/) | Recommendation, 2015 | Defines parallel states and run-to-completion processing: one event can be processed independently across active child regions and trigger several transitions in one macrostep. | Standardizes executable state-machine notation, not an editorial ontology or history store. |

## 2. Events, fluents, and normative state

| ID | Source | Version/date | Use | Limitation |
|---|---|---|---|---|
| `EVT-04` | Robert Kowalski and Marek Sergot, [“A Logic-based Calculus of Events”](https://doi.org/10.1007/BF03037383) | *New Generation Computing* 4(1), 1986 | Establishes a logic for events, time, database update, and narratives, including new information about the past. Supports separating occurrences from the conditions they initiate or terminate. | Logic-programming formalism; practical persistence, source checkpoints, and editorial authority remain external. |
| `EVT-05` | Andrew D. H. Farrell, Marek J. Sergot, Mathias Sallé, and Claudio Bartolini, [“Using the Event Calculus for Tracking the Normative State of Contracts”](https://doi.org/10.1142/S0218843005001110) | 2005 | Models normative state as the aggregate of normative relations and variables that hold at a time, with contract events changing that state. Strong analogue for obligations, permissions, waivers, and violations. | Contract domain and deontic vocabulary do not settle prose quality, rhetoric, evidence sufficiency, or editorial release. |

## 3. Causality, conflict, and concurrency

| ID | Source | Version/date | Use | Limitation |
|---|---|---|---|---|
| `EVT-06` | Glynn Winskel, [*Event Structures*](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-95.html) | Cambridge Technical Report 95, 1986 | Represents processes as event occurrences plus causal-dependency relations; supports histories that are not merely one arbitrary interleaving. | Denotational concurrency model, not a product data model or persistence specification. |
| `EVT-07` | Leslie Lamport, [“Time, Clocks, and the Ordering of Events in a Distributed System”](https://www.microsoft.com/en-us/research/publication/time-clocks-ordering-events-distributed-system/) | 1978 | Establishes a partial “happened-before” order. Supports distinguishing causally ordered editorial acts from concurrent reviews or branches. | Logical ordering does not supply semantic conflict resolution, authority, or exact wall-clock truth. |
| `EVT-08` | Marc Shapiro, Nuno Preguiça, Carlos Baquero, and Marek Zawirski, [“Conflict-Free Replicated Data Types”](https://doi.org/10.1007/978-3-642-24550-3_29) | 2011 | Formal precedent for state-based and operation-based replicated data types and convergence under concurrent updates. | Convergence does not mean editorial correctness, agreement, or authorized merge. No CRDT is selected. |

## 4. Facts, transactions, and multidimensional data

| ID | Source | Version/date | Use | Limitation |
|---|---|---|---|---|
| `EVT-09` | Datomic, [Introduction and Information Model](https://docs.datomic.com/) | inspected 2026-09-04 | Treats the database as immutable atomic facts (“datoms”); a datom carries entity, attribute, value, transaction, and assertion/retraction status. Demonstrates that one fact can retain several dimensions and provenance. | Vendor-specific database model; total transaction order, universal schema, and storage trade-offs may not fit editorial branches or large artifacts. |
| `EVT-10` | Datomic, [Transaction Model](https://docs.datomic.com/transactions/model.html) and [Transaction Data](https://docs.datomic.com/transactions/transaction-data-reference.html) | inspected 2026-09-04 | Transactions atomically accrue sets of facts and are themselves reified for provenance. Supports one editorial act changing multiple dimensions in one indivisible transaction. | Declarative fact accrual is not equivalent to domain events; retractions and erasure require separate policy analysis. |

## 5. Event sourcing and projections

| ID | Source | Version/date | Use | Limitation |
|---|---|---|---|---|
| `EVT-11` | Microsoft Azure Architecture Center, [Event Sourcing pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing) | updated 2026-03-28 | Defines append-only domain events, replay/rehydration, materialized views, snapshots, intent-rich events, and optimistic concurrency. Documents benefits and substantial schema, query, consistency, and migration costs. | Architecture guidance, not proof that event sourcing is appropriate here. Explicitly warns against indiscriminate adoption. |
| `EVT-12` | CNCF CloudEvents, [CloudEvents Specification](https://github.com/cloudevents/spec) | stable core 1.0.2; inspected 2026-09-04 | Separates event occurrence data from context metadata and supplies an interoperable envelope precedent. | Transport/interoperability specification; it does not define domain semantics, causal replay, or editorial validity. |

## 6. Temporal interpretation

| ID | Source | Version/date | Use | Limitation |
|---|---|---|---|---|
| `EVT-13` | XTDB, [Bitemporality](https://v1-docs.xtdb.com/concepts/bitemporality/) | XTDB 1.x documentation, inspected 2026-09-04 | Distinguishes transaction/recording time from valid/effective time and permits retroactive or proactive valid-time assertions. Supports late discovery of product changes and later corrections. | Vendor-specific implementation; two times may still be insufficient for observation, decision, and publication semantics. |

## 7. Existing J-Editorial sources reused

The D-03 review also relies on:

- `STD-01` — W3C PROV-DM/PROV-O for entities, activities, agents, derivation, and attribution;
- `STD-02` — W3C Web Annotation for targets, selectors, resource state, and motivations;
- `STD-03` — SHACL for separating constraints, data, and validation-result records;
- `HIST-08` through `HIST-10` — Delta/DeltaDB as comparator evidence for operation-level identity and between-commit history;
- `AMN-01` through `AMN-09` — pinned Amnesia Docs and product observations.

These identifiers resolve in [`PHASE-2-SOURCE-LEDGER.md`](PHASE-2-SOURCE-LEDGER.md).

## 8. Evidence rules

- “Event” is not assumed to mean command, fact, message, transaction, delta, or checkpoint.
- A state-machine formalism does not imply finite enumerated editorial states.
- A transaction's atomicity does not prove its assertions are true or authorized.
- A total storage order must not erase causal concurrency or branch alternatives.
- Replay is relative to event schema, reducer, external evidence, and projection versions.
- A vendor pattern or database demonstrates a design possibility, not a selection.
- No source authorizes dataset construction or model training.
