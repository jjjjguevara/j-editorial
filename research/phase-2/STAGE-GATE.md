# Phase 2 foundations gates

Date: **2026-09-04**  
Overall verdict: **pass-with-constraints**  
Implementation authorization: **not granted**  
Persistence/ADR authorization: **not granted**  
Dataset research: **not executed**

## 1. Gate summary

| Gate | Verdict | Scope |
|---|---|---|
| `BOOTSTRAP-P2-FOUNDATIONS-G0` | **pass-with-constraints** | Technical/foundational event–fluent and Amnesia proof |
| `BOOTSTRAP-P2-PAIRED-DOMAIN-G1` | **pass-with-constraints** | General-prose representation fixture and technical/prose co-gate |

Neither gate is a bootstrap-exit, implementation, persistence, dataset, or model-training gate.

## 2. G0 — technical/foundational question

Did the accepted D-02R/D-03/D-04/AMN-01 directions produce a coherent, falsifiable technical foundation with reproducible evidence and explicit limitations, without making an architectural or dataset decision implicitly?

**Yes, within the bounded technical fixture.**

Passing evidence:

- D-03 is a logical research direction rather than a storage decision.
- The Editorial Construction Space axes operate as cross-cutting dimensions.
- The typed vocabulary survived explicit reduction attempts.
- Amnesia product/docs evidence is pinned to immutable refs and blob identities.
- Positive, adverse, unknown, and unevaluated states remain distinct.
- The machine-readable technical fixture contains 13 causal transactions, five source bindings, three fluents, and four versioned projections.
- The standard-library validator passes E-01 through E-10.
- Representation/history and security/authority requirements are explicit.

## 3. D-01P owner decision

The artifact-selection hold is closed by [`D-01P-ACCEPTANCE.md`](D-01P-ACCEPTANCE.md):

```text
Option A accepted
repository: jjjjguevara/sci-jjjjguevara
commit:     1c93b60e75ce60203295a988b8125d44e6acb6bc
path:       src/pages/about.astro
blob:       d56c560fc63569b471cc4e81a65daf52568fe754
route:      /about
```

Supporting portfolio records are evidence/norms only. Research use is limited to details already intentionally present on the pinned public About page and bounded source/history metadata. Field Notes, unpublished records, external-provider disclosure, source mutation, and dataset use remain excluded.

## 4. G1 — paired-domain question

Did the accepted D-01P prose target produce a falsifiable general-prose fixture, and does the common logical vocabulary survive comparison with the Amnesia technical-reference fixture without conflating their graders or overstating the evidence?

**Yes, for representation adequacy, with evaluation-science and implementation constraints still open.**

Passing evidence:

- the prose fixture binds three exact real About-page checkpoints;
- two real history operations remain distinct and are not treated as unique gold answers;
- owner-attested source state, internal consistency, and independent substantiation remain separate;
- a disputed prose finding spans constructive, referential, and pragmatic/governance concerns;
- three potentially acceptable remedies remain explicit;
- synthetic reviewer disagreement remains unresolved and non-blocking under the accepted goal version;
- project style rules retain scope and owner exception authority;
- truth/support and disclosure permission remain separate;
- a redacted synthetic privacy branch preserves disposition while disclosing no real private detail;
- a counterfactual profile change reopens an unchanged About page;
- different reducer/goal versions derive different readiness at the same state;
- only the owner has disclosure and release authority;
- the prose validator passes P-01 through P-12;
- the paired manifest passes C-01 through C-07 and binds both independent results immutably.

## 5. Executed results

### Technical

```text
status:                    pass
E-01..E-10:                passed
input_file_sha256:         cba015d96b8ca0331c48dbfb96a2d29408883167ca4bb4af7b84f3cffdffff82
canonical_research_sha256: 4035f6f544c08e6c8878b0e0bbc0a2a696a48501feab0f1ea554ae74c4450e8c
```

### General prose

```text
status:                    pass
P-01..P-12:                passed
input_file_sha256:         9c24cf03065f69aacaed4375c9830feeec0a78c8277e3a07c0b8f299147b4eb2
canonical_research_sha256: 74e0e3282596fd7ade8607c9a0ef40b82e096ad98840e157407e0c6b972f012e
```

### Paired domain

```text
status:                    pass-with-constraints
C-01..C-07:                passed
manifest_file_sha256:      087bdcfa2959a678deb0fd4953596f6250e6e6be7f38b16b8a71e91a66f80ce5
canonical_research_sha256: 46a0eb9f6f6e955df749677673a85f680dc710af5041ddbf921bce2762c38cd7
```

## 6. Current gate matrix

| Gate or question | Status | Reason |
|---|---|---|
| D-01P artifact selection | **closed / accepted A** | Exact `/about` target and privacy/evidence boundary recorded. |
| General-prose representation co-gate | **pass-with-constraints** | P-01–P-12 pass; empirical prose quality remains outside the validator. |
| Cross-domain vocabulary validation | **pass-with-constraints** | C-01–C-07 pass across deterministic technical and disputed prose cases. |
| Amnesia runtime/build evidence | **open** | No isolated authenticated checkout; deploy-capable workflow was not re-run. |
| Portfolio built/live equivalence | **open** | Source is pinned; isolated build and production-response equality were not established. |
| Target identity under real edits | **open** | Symbolic/text selectors and synthetic movement remain; real re-anchoring tests are required. |
| Empirical reader task | **open** | No recruited reader population, protocol, or observed task outcome. |
| Human/model grader reliability | **open** | No annotation study, calibration, agreement, error analysis, or meta-evaluation. |
| Independent biography substantiation | **not authorized / open by policy** | Owner-attested and internally consistent records are not external proof. |
| Persistence bake-off | **ready, not executed** | Workload exists; no substrate experiment ran. |
| Production security gate | **open** | Baseline only; no implementation or adversarial execution. |
| Dataset architecture/research gate | **closed** | No corpus, labeling, split, preference, or training work is authorized. |
| Bootstrap exit gate | **closed** | Representation proof alone is insufficient for exit. |

## 7. Research released

The two gates release only the following research:

1. isolated Amnesia build/type-check/focused-test reproduction;
2. isolated portfolio source/build/live-equivalence checks within the accepted data boundary;
3. real target-resolution and re-anchoring experiments;
4. event/fact/checkpoint import-export prototypes used only for substrate comparison;
5. the common representation/history bake-off workload;
6. empirical reader-task and annotation/adjudication protocol design;
7. deterministic/human/model grader calibration and meta-evaluation;
8. goal-contract and eval-instance refinement against both executed slices;
9. a later D-03R/representation ADR packet based on executed workloads.

## 8. Research still prohibited

- production framework implementation;
- accepting a persistence or representation ADR from these fixtures alone;
- treating either fixture JSON as a canonical production schema;
- source-repository edits, pull requests, deployment, or publication;
- external-provider disclosure of private source or personal data without a separate accepted boundary;
- model-training dataset research, corpus construction, labeling, split generation, preference extraction, fine-tuning, or training;
- treating editorial history as automatic ground-truth preference data;
- claiming that P-01–P-12 validate prose quality or that C-01–C-07 validate a model grader.

## 9. Review boundary

The Phase 2 branch and draft pull request now contain an executed paired-domain decision packet. Human review may:

- accept the results as a research foundation;
- narrow claims or released work;
- return the fixtures with findings;
- require additional evidence before merge;
- reject the common representation hypothesis.

Merge or approval does not independently open implementation, persistence, dataset, training, or bootstrap-exit gates.
