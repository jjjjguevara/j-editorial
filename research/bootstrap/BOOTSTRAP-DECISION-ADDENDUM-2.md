# Bootstrap decision addendum 2 — D-02R, D-03, and AMN-01

Status: **owner directions recorded / research-only authority / implementation blocked**  
Date: **2026-09-04**  
Controlling gate: **`ADVERSARIAL-REVIEW-REQUIRED`**  
Dataset-research execution: **held**  
Applies to: `BOOTSTRAP.md`, draft PR #1, and the bootstrap research packet

This addendum records the owner's second response. It supplements [`BOOTSTRAP-DECISION-ADDENDUM.md`](BOOTSTRAP-DECISION-ADDENDUM.md). It is not an ADR, schema, storage selection, implementation authorization, dataset authorization, or release of the bootstrap gate.

## 1. Owner response

> For D-02, yes this is the right direction. (A)
>
> For D-03, wouldn't it make sense to conceptualize each as an event on an event stream (Moore-machine model)? We might be negating the possibility of a single editorial "datum" having multiple dimensions at the same time. It might be deeper than a flawed scalar, or a vector analogue. We should research further before locking.
>
> AMN-01 - yes, (A). The corpus of docs is in development, so it's a good source for faulty references and trackable updates and editorial improvements.

## 2. Decision status

| ID | Owner direction | Status | Binding consequence |
|---|---|---|---|
| `D-02R` | Choose **A**. | **Accepted as phase-2 research hypothesis** | Test the Editorial Construction Space and typed plural record family across the paired proof. Do not treat acceptance as an ontology, schema, store, or event-sourcing decision. |
| `D-03` | Test an event-stream/Moore-machine account that preserves simultaneous dimensions; research further before locking. | **Research hold** | Withdraw any implication that source, semantic, and projection authority are mutually exclusive records or physical layers. Compare event-first, fact/datom-first, event–fluent hybrid, and checkpoint+journal models. |
| `AMN-01` | Choose **A**. | **Accepted for research-only use** | Pinned Amnesia source, checkout, build, type-check, focused tests, and CI may serve as product evidence. The evolving docs history may be used as an evaluation and architecture fixture. |

## 3. D-02R limits

Option A authorizes a candidate language of distinctions:

- artifact and representation;
- purpose and goal contract;
- norm, obligation, and constraint;
- assertion, finding, evidence, and referent;
- target and selector;
- operation, actor, role, and authority;
- decision, outcome, verification, release, and episode.

These distinctions may be represented as event payloads, facts/fluents, relationships, projections, or some combination. The choice does not require one persisted object per term.

The three Editorial Construction Space axes are cross-cutting. A datum may be simultaneously:

- a constructive unit or operation;
- referentially bound to evidence or a product state;
- pragmatically situated under an actor, dialogue, norm, and authority.

No axis owns the datum exclusively.

## 4. D-03 correction

The earlier phrase “three authority concerns” remains useful only as a set of questions:

1. what establishes exact material/source state?
2. what establishes editorial claims, norms, acts, and decisions?
3. what outputs are derived and reproducible?

It must not imply three databases, services, streams, object hierarchies, or mutually exclusive layers.

The new candidate must test:

```text
state transition:
  S' = δ(S, event)

state-derived output:
  Y = λ(S)

heterogeneous state:
  S = material × goal × normative × epistemic
      × operational × authority × release × retention
```

This is Moore-style only at the level where outputs are functions of current state. Command acceptance, event production, external observations, and side effects may require different semantics. The research therefore uses “Moore-style extended state machine,” not “classical Moore machine,” until the restrictions are justified.

## 5. AMN-01 boundary

Accepted research operations are defined in [`AMNESIA-ORACLE-AUTHORIZATION.md`](AMNESIA-ORACLE-AUTHORIZATION.md). Formal results must pin immutable repository refs and tool/environment versions.

The docs history may supply:

- stale or false references;
- source/product mismatches;
- corrections and errata;
- readiness changes;
- alternative edits;
- review and release decisions;
- regressions and reopened findings.

These records are evaluation fixtures and architecture evidence. They are not automatically labels, demonstrations, preference data, or model-training truth.

## 6. Remaining hold

D-01P—the exact general-prose companion—remains unresolved. D-03R is not yet an owner question; it will be produced only after the event/state experiments.

No part of this response authorizes implementation, accepts an ADR, selects a backend, activates dataset research, or merges PR #1.
