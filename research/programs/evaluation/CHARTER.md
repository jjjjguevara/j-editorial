# Evaluation science — Charter

Slug: `evaluation`  
Alias: `BR-EVAL`  
Beads epic: `j-editorial-k4f`  
Lifecycle: **BOOTSTRAP-SCOPED**  
Controlling contract: `BOOTSTRAP.md`; method: `RESEARCH.md`

## 1. Authority and status

A protocol proposal exists. No participants, model trials, labels, calibration, or meta-evaluation exist. No model judge may affect any gate until this program passes `EV-G1`.

## 2. Mission

Define objective, human, and model grader contracts that produce valid obligation-level evidence in both slices, and the adjudication, reporting, and statistical rules around them.

## 3. Why the program is separate

Construct validity, reliability, calibration, and disagreement are measurement questions distinct from what is being measured.

## 4. Decisions or specification questions it informs

`BOOTSTRAP.md` ADR queue items 30 to 35 and 41 to 44; the review exit criterion "a defined first eval-instance contract".

## 5. In scope / out of scope

In scope: eval-instance contract; grader taxonomy; human procedure; model-judge meta-evaluation; statistical reporting; cost and infrastructure separation.  
Out of scope: dataset construction (held program); benchmark publication.

## 6. Dependencies on other programs

Upstream: `history`, `amnesia`, `prose`, `frame-domain`. Downstream: `paired-synthesis`, `model-training-data` (held).

## 7. Hypotheses under attack

- H1. Obligation-level observations are more diagnostic than page-level scores. Status: supported by cited literature; untested here.
- H2. Deterministic checks, human judgment, and model judgment answer different obligations. Status: argued; untested.

## 8. Required current / SOTA reconnaissance

Judge meta-evaluation and human-evaluation reproducibility sources are in the ledger; re-date at execution and add at least one reader-study instrument used in production documentation work.

## 9. Required primary-source classes

Class 5.2 for methodology; 5.6 for human judgments; 5.5 for executed graders.

## 10. Comparison set

Exact match; rubric; pairwise preference; reader task completion; deterministic checks; model judge with meta-evaluation.

## 11. Experiments or bake-offs

`EV-G1`: a small pilot comparing deterministic, human, and model graders on both slices against independently obtained judgments, with the stress tests listed in [`EVALUATION-PROTOCOL.md`](EVALUATION-PROTOCOL.md) section 5.

## 12. Representative workloads or fixtures

Both program fixtures; the obligation tables in the amnesia and prose audits.

## 13. Scale and budget analysis

Participant count, compensation, stopping rule, and model cost must be declared in the pre-registration; none exists.

## 14. Security, privacy, licensing, governance

No private source or personal data to an external provider without a separately accepted boundary.

## 15. Interoperability and migration

Eval records should be exportable as per-instance observations before aggregation.

## 16. Deliverables

Eval-instance contract; grader taxonomy; adjudication protocol; meta-evaluation report; reporting contract.

## 17. Falsification criteria

A grader is rejected for gate use if it disagrees with independent judgment beyond a pre-registered bound, fails the adversarial stress tests, or cannot abstain.

## 18. Gate criteria

- `EV-G1` `j-editorial-k4f.1`: grader reliability pilot and adversarial meta-evaluation.

## 19. Downstream ADR or specification candidates

Eval-instance contract; grader selection policy; model-judge meta-evaluation policy; metric and statistical policy.

## 20. Residual risk and revisit policy

Agreement is not accuracy; shared bias produces agreement. Revisit after the pilot.

## 21. Independence declaration

The protocol is a proposal by the same lineage as the fixtures. Nothing has been measured.
