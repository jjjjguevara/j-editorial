# D-03 acceptance — causal event–fluent editorial state

Status: **accepted research direction / not a persistence architecture**  
Owner acceptance: **2026-09-04**  
Accepted antecedent: `research/bootstrap/D-03-EVENT-STATE-REVIEW.md`  
Implementation gate: **closed**  
Dataset research: **held**

The owner accepted the revised D-03 shape as adequate and authorized the next research stage. This record translates that acceptance into bounded research authority.

## Accepted logical shape

Phase 2 may test the following model:

```text
typed occurrences and atomic transactions
        │
        ▼
heterogeneous, multidimensional editorial state
        │
        ├── time-scoped facts / fluents
        ├── exact material checkpoints
        ├── causal branch and merge relations
        └── versioned projections
```

A Moore-style distinction remains useful:

```text
decide(State, Command)
  -> Accepted Event Transaction
   | Rejection
   | Abstention

evolve(State, Event Transaction, Reducer Version)
  -> New State

project(State, Projection Version)
  -> Gap / Readiness / Evaluation / Report View
```

The accepted direction includes these invariants:

1. the Editorial Construction Space axes are cross-cutting, not mutually exclusive partitions;
2. one identity-bearing editorial datum may participate in several dimensions and relations simultaneously;
3. an occurrence is distinct from a condition that continues to hold;
4. a transaction may atomically affect several state dimensions;
5. exact material state requires a checkpoint or content identity and cannot be manufactured by semantic replay;
6. storage order must not erase causal independence, branches, conflict, or merge;
7. projections are derived, versioned views rather than canonical truth;
8. evidence and observations do not become true merely because they were recorded;
9. authority to observe, propose, accept, publish, or erase remains explicit;
10. replay limitations caused by nondeterminism, unavailable external systems, or erasure must be disclosed.

## Research now authorized

The following non-implementation work may proceed:

- formalize the candidate event, fluent, transaction, checkpoint, and projection distinctions;
- construct bounded architecture/evaluation fixtures;
- execute deterministic fixture validators;
- inspect pinned Amnesia and Amnesia Docs evidence under `AMNESIA-ORACLE-AUTHORIZATION.md`;
- compare event-first, fact-first, event–fluent, and checkpoint+journal models;
- derive representation, temporal, causal, migration, and backend-exit requirements;
- conduct security, authority, retention, and erasure analysis;
- prepare later ADR decision packets without accepting an ADR.

## Not accepted

This decision does not select or authorize:

- event sourcing as the product's storage architecture;
- one global event stream;
- a relational, graph, document, temporal, or CRDT database;
- Git, Dolt, PostgreSQL, DeltaDB, Datomic, XTDB, Automerge, Yjs, or another substrate;
- an event schema, reducer framework, API, package structure, or production serializer;
- the claim that every domain concept must be encoded as an event;
- the claim that a deterministic replay is always possible;
- source-repository mutation;
- model-training dataset research or training.

## Stage boundary

This acceptance closes the D-03 conceptual question for entry into Phase 2 foundations. It does not close the later architecture decision. A future representation/history gate must be based on executed workloads and failure tests, not on the attractiveness of the event-stream analogy.
