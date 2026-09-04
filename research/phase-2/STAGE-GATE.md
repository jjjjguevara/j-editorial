# Phase 2 foundations gate

Gate: `BOOTSTRAP-P2-FOUNDATIONS-G0`  
Verdict: **pass-with-constraints**  
Date: **2026-09-04**  
Implementation authorization: **not granted**  
Persistence/ADR authorization: **not granted**  
Dataset research: **not executed**

## 1. Gate question

Did the accepted D-02R/D-03/D-04/AMN-01 directions produce a coherent, falsifiable technical foundation with reproducible evidence and explicit limitations, without making an architectural or dataset decision implicitly?

**Yes, within the bounded technical fixture.**

## 2. Passing evidence

- D-03 acceptance is recorded as a logical research direction rather than a storage decision.
- The Editorial Construction Space axes operate as cross-cutting dimensions.
- The typed vocabulary survived explicit reduction attempts.
- The Amnesia product/docs evidence is pinned to immutable refs and blob identities.
- Positive, adverse, unknown, and unevaluated states remain distinct.
- The machine-readable fixture contains 13 causal transactions, five source bindings, three fluents, and four versioned projections.
- The standard-library validator passes E-01 through E-10.
- Representation/history requirements and an implementation-neutral bake-off workload are defined.
- Security, authority, disclosure, prompt-injection, retention, and erasure constraints are explicit.
- Source mutation, deployment, backend selection, ADR acceptance, and dataset research did not occur.

## 3. Constraints and non-passes

The following are not passed:

| Gate | Status | Reason |
|---|---|---|
| Amnesia runtime/build evidence | **open** | No isolated authenticated checkout was available; the deploy-capable workflow was not re-run. |
| Target identity under real edits | **open** | The current fixture uses symbolic/text selectors and a synthetic correction; real movement/rewrite tests remain. |
| General-prose co-gate | **blocked by owner artifact selection** | D-01 requires a non-reference prose companion. |
| Cross-domain ontology validation | **open** | Only the technical-reference half has executed. |
| Persistence bake-off | **ready, not executed** | Workload exists; no compatible tool environment/substrate experiment ran. |
| Evaluation-science gate | **open** | Human/model grader calibration and meta-evaluation remain downstream. |
| Production security gate | **open** | Baseline only; no implementation or adversarial execution. |
| Bootstrap exit gate | **closed** | Full paired proof and later decision packets are incomplete. |

## 4. Research released

This gate releases the following research-only work:

1. isolated Amnesia build/type-check/focused-test reproduction;
2. real target-resolution and re-anchoring experiments;
3. event/fact/checkpoint import-export prototypes used only for substrate comparison;
4. the common representation/history bake-off workload;
5. goal-contract and eval-instance refinement against executed evidence;
6. the general-prose companion fixture after D-01P;
7. a later D-03R/representation ADR packet based on both proof slices.

## 5. Research still prohibited

- production framework implementation;
- accepting a persistence ADR;
- treating the fixture JSON as a canonical production schema;
- source-repository edits or deployment;
- external-provider disclosure of private source without a separate accepted boundary;
- model-training dataset research, corpus construction, labeling, or training;
- treating editorial history as ground-truth preference data.

## 6. Next pivotal decision — D-01P

The next co-gating research stage requires the exact general-prose artifact.

### A — Existing public-facing prose artifact

Provide a repository/path for an essay, explanatory article, case narrative, or other general-audience prose artifact under the owner's control.

Required metadata:

- immutable ref/path;
- intended audience and purpose;
- rights;
- factual/evidence boundary;
- applicable style/norms;
- review authority;
- private-data exclusions.

**Research recommendation: A.** It supplies real history and a strong contrast to the Amnesia reference slice.

### B — Temporary Doc Doctor research prose

Use:

```text
jjjjguevara/doc-doctor/
docs/research/ui-ux/AI Editing Tool UI UX Research.md
```

This is immediately available but remains technical/research prose, so it is a weaker test of general editorial applicability.

### C — Purpose-built bounded prose fixture

Create a controlled article with deliberate factual, structural, rhetorical, citation, ambiguity, and alternative-resolution cases.

This gives strong experimental control but weaker real-world history and adoption evidence.

## 7. Required answer

```text
D-01P: A + repository/path | B | C
Audience/purpose:
Review authority:
Private-data or rights constraint:
```

This answer will release the prose research fixture. It will not release implementation, persistence, ADR, or dataset research.
