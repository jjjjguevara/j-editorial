# Paired technical-reference and general-prose synthesis — Charter

Slug: `paired-synthesis`  
Alias: paired-proof synthesis (next-phase contract section 4)  
Beads epic: `j-editorial-c8r`  
Lifecycle: **ACTIVE**  
Controlling contract: `BOOTSTRAP.md`; method: `RESEARCH.md`  
Decisions relied on: `D-01` (paraphrased), `D-01P` (verbatim)

## 1. Authority and status

The paired proof is co-gating: success on one slice cannot stand in for the other. The Phase 2 co-gate covered representation adequacy only. No generality claim beyond that is made.

## 2. Mission

Bind the technical and prose slices under one vocabulary, decide what the pair does and does not establish about generality, and own the contract-case coverage matrix.

## 3. Why the program is separate

Generality is a claim about the pair, not about either slice; someone has to be accountable for not overstating it.

## 4. Decisions or specification questions it informs

Whether the vocabulary can be called general; readiness of the bootstrap adversarial gate; the roadmap's generality hypothesis (`ROADMAP.md` section 15.8).

## 5. In scope / out of scope

In scope: cross-slice obligations `C-01` to `C-07`; the fourteen shared minimum cases; the fifteen Stage 0 proof obligations; the synthesis decision packet.  
Out of scope: grader reliability (owned by `evaluation`), persistence (`history`).

## 6. Dependencies on other programs

Upstream: `amnesia`, `prose`, `evaluation`, `goal-priors`. Downstream: `doc-doctor-integration`, `model-training-data` (held).

## 7. Hypotheses under attack

- H1. One typed vocabulary represents both slices without conflating grader methods. Status: supported by construction on two same-owner artifacts.
- H2. The pair covers the contract's shared minimum cases. Status: rejected as stated; three cases have no coverage and three are trivial. See [`COVERAGE.md`](COVERAGE.md).

## 8. Required current / SOTA reconnaissance

None beyond the slices' own.

## 9. Required primary-source classes

Class 5.5 experimental results from both slices; 5.6 adjudication once available.

## 10. Comparison set

Single-slice generality claims (rejected by the contract); the paired representation co-gate (executed); paired empirical evaluation (not executed).

## 11. Experiments or bake-offs

`PS-G1`: add waiver, failed-operation-with-no-post-state, and abstention cases to both slices under pre-registration and re-run the co-gate. `PS-G2`: the synthesis decision packet, issued only with PASS, NARROW, RETURN-WITH-FINDINGS, DEFER, or REJECT verdicts per obligation.

## 12. Representative workloads or fixtures

[`fixtures/paired-domain-proof.json`](fixtures/paired-domain-proof.json) binding both slice results by digest.

## 13. Scale and budget analysis

Not applicable.

## 14. Security, privacy, licensing, governance

Inherited from the slices.

## 15. Interoperability and migration

Not applicable.

## 16. Deliverables

Coverage matrix; co-gate results; synthesis packet.

## 17. Falsification criteria

The generality claim is rejected if a case required by the contract cannot be represented in either slice, or if the slices require incompatible canonical models.

## 18. Gate criteria

- `PS-G1` `j-editorial-c8r.1`: cover waiver, failed operation, and abstention in both slices.
- `PS-G2` `j-editorial-c8r.2`: paired synthesis decision packet.

## 19. Downstream ADR or specification candidates

Domain glossary acceptance; bootstrap exit readiness.

## 20. Residual risk and revisit policy

Both artifacts belong to the same owner and author. Revisit when an independently owned artifact enters either slice.

## 21. Independence declaration

The manifest, validator, and results share the slices' author lineage. The validator checks that referenced checks passed and that conclusion fields contain expected strings; it does not re-evaluate semantics.
