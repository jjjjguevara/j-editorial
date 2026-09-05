# Paired technical-reference and general-prose result

Status: **cross-domain representation proof passed with constraints**  
Manifest: [`fixtures/paired-domain-proof.json`](fixtures/paired-domain-proof.json)  
Validator: [`tools/validate_paired_domain.py`](tools/validate_paired_domain.py)  
Result: [`results/paired-domain-validation.json`](results/paired-domain-validation.json)  
Technical slice: [`EVENT-FLUENT-EXPERIMENT.md`](../event-state/EVENT-FLUENT-EXPERIMENT.md)  
Prose slice: [`PORTFOLIO-PROSE-EXPERIMENT.md`](../prose/PORTFOLIO-PROSE-EXPERIMENT.md)  
Dataset research: **not executed**

## 1. Co-gate question

Does one logical J-Editorial vocabulary represent both:

1. a technical API-reference contradiction dominated by source parity and executable behavior; and
2. a public professional biography dominated by qualified facts, rhetoric, structure, audience judgment, privacy, and several defensible resolutions?

**Yes, for representation adequacy, with important open evaluation and implementation constraints.**

## 2. Contrast between the slices

| Technical reference | General prose |
|---|---|
| Product interfaces and source signatures are primary referents. | A person, owner-approved records, and intended public disclosure are referents. |
| Static contradictions can be high-confidence and largely deterministic. | Factual consistency may be deterministic while sufficiency and rhetoric require adjudication. |
| A correction can often be verified against an interface contract. | Several rewrites or structural resolutions may satisfy the same goal. |
| Runtime and developer-task evidence remain absent. | Empirical reader-task and calibrated-grader evidence remain absent. |
| External product change can stale unchanged documentation. | External profile change can stale an unchanged biography. |
| Security concerns include capability behavior and source parity. | Safety includes title inflation, misleading implication, privacy, and disclosure authority. |

The common shape is not “all editorial problems are the same.” The common shape is that exact material checkpoints, causal transactions, time-scoped conditions, observations/evidence, obligations, authority-bearing decisions, and versioned projections remain distinct while domain-specific graders vary.

## 3. Cross-domain obligations

| Check | Claim | Result |
|---|---|---|
| `C-01` | Both slices preserve exact checkpoints, causal transactions, fluents, and derived versioned projections. | passed |
| `C-02` | One typed vocabulary represents deterministic parity and disputed prose judgment without conflating grader methods. | passed |
| `C-03` | Historical acceptance remains evidence rather than a unique gold answer; alternatives and authority remain explicit. | passed |
| `C-04` | External referent change can alter correctness/readiness while artifact bytes remain unchanged. | passed |
| `C-05` | Norm applicability, evidence qualification, privacy, and release authority remain distinct from observations and edits. | passed |
| `C-06` | The proof is limited to representation adequacy; runtime, empirical reader performance, and grader reliability remain open. | passed |
| `C-07` | Neither slice selects persistence, a production schema, a corpus, or model-training use. | passed |

## 4. Deterministic result

```text
status:                    pass-with-constraints
manifest_file_sha256:      087bdcfa2959a678deb0fd4953596f6250e6e6be7f38b16b8a71e91a66f80ce5
canonical_research_sha256: 46a0eb9f6f6e955df749677673a85f680dc710af5041ddbf921bce2762c38cd7
```

Bound fixture inputs:

```text
technical: cba015d96b8ca0331c48dbfb96a2d29408883167ca4bb4af7b84f3cffdffff82
prose:     9c24cf03065f69aacaed4375c9830feeec0a78c8277e3a07c0b8f299147b4eb2
```

The paired validator does not replace the E-01–E-10 and P-01–P-12 validators. It verifies immutable result bindings, cross-domain obligation references, and the non-overstatement boundary.

## 5. Supported logical model

The paired result supports continuing to research:

```text
typed identity-bearing editorial data
+ exact material checkpoints
+ causal event transactions
+ time-scoped facts / fluents
+ observations and evidence with method/version/uncertainty
+ explicit obligations, proposals, authority, decisions, and outcomes
+ versioned derived projections
```

The Editorial Construction Space remains useful as a cross-cutting completeness test. A single datum may participate in constructive, referential, and pragmatic/governance relations at once. The axes are not exclusive storage buckets.

## 6. Required refinements

The paired proof adds or strengthens these requirements:

1. **Disclosure is independent of truth.** A supported or possibly true claim can still be unauthorized or unnecessary to publish.
2. **Blocking status is goal-versioned.** A finding can be non-blocking under one accepted goal and blocking under a stricter projection without changing the historical observation.
3. **Disagreement must remain inspectable.** Reviewer identity/role, instructions, evidence, rationale, and authority cannot be replaced by an averaged score.
4. **Accepted text is not automatic preference truth.** Historical acceptance may reflect one valid resolution, local style, timing, or compromise.
5. **Grader method is obligation-specific.** Deterministic checks, source execution, reader tasks, human adjudication, and model judgments answer different questions.
6. **Empirical outcomes require their own events and evidence.** “Readable,” “clear,” or “useful” cannot be inferred solely from a valid representation fixture.
7. **Erasure can intentionally break exact replay.** The system must record replay limits instead of silently retaining prohibited payloads.

## 7. Reductions rejected across both slices

- one scalar quality score as canonical state;
- one universal `Gap` object for every observation, condition, decision, and positive result;
- exact-text similarity as the primary prose grader;
- historical before/after pairs as automatic rejected/chosen training preferences;
- one universal source of truth across runtime, documentation, biography, norms, and release authority;
- model judgment as a substitute for deterministic evidence or owner disclosure authority;
- semantic replay as a substitute for exact material checkpoints;
- a passing representation test as proof of a production architecture.

## 8. Conclusions

```text
typed vocabulary generalization:  supported-with-constraints
event–fluent/checkpoint shape:     supported-for-further-research
prose grader reliability:          not established
empirical reader task:             not executed
production architecture:           not selected
persistence ADR:                   not authorized
dataset research:                  not authorized
bootstrap exit:                    not passed
```

## 9. Work released by this result

Research-only work may proceed on:

- human-reader task design and annotation/adjudication protocol;
- deterministic-versus-human-versus-model grader calibration and meta-evaluation;
- real target movement/re-anchoring tests;
- isolated source/build parity checks for the accepted fixtures;
- the common representation/history substrate bake-off;
- a later D-03R/representation decision packet grounded in both slices.

The result does not release production implementation, a persistence decision, dataset research, training, or merge of the Phase 2 PR.
