# Goal contracts and normative priors — Charter

Slug: `goal-priors`  
Alias: `BR-GOAL` / `BR-PRIORS`  
Beads epic: `j-editorial-wd2`  
Lifecycle: **BOOTSTRAP-SCOPED**  
Controlling contract: `BOOTSTRAP.md`; method: `RESEARCH.md`

## 1. Authority and status

Nothing executed. Goal contracts exist as prose inside two fixtures and a proposed record shape exists in the evaluation protocol. No schema, decomposition rule, or precedence rule has been tested.

## 2. Mission

Define how purpose, audience, scope, obligations, waivers, accepted uncertainty, and release policy are expressed and decomposed, and how guides and rules are scoped, licensed, versioned, put in precedence, excepted, and applied.

## 3. Why the program is separate

Obligations are the unit every grader binds to; if goal decomposition is weak, every evaluation is weak.

## 4. Decisions or specification questions it informs

`BOOTSTRAP.md` ADR queue items 7, 12, 13, and 14; the review exit criterion "a defined first goal-contract slice".

## 5. In scope / out of scope

In scope: contract requirements; decomposition into addressable obligations; ambiguity handling; norm identity, version, scope predicate, strength, exceptions, precedence authority, licensing boundary; waivers.  
Out of scope: importing proprietary style-guide text.

## 6. Dependencies on other programs

Upstream: `frame-domain`, `amnesia`, `prose`. Downstream: `representation`, `evaluation`, `paired-synthesis`.

## 7. Hypotheses under attack

- H1. A free-text purpose can be compiled into addressable obligations without losing intent. Status: untested.
- H2. Precedence among norms is contextual and must not be a hard-coded ladder. Status: argued in `BOOTSTRAP.md` section 10.3; untested.

## 8. Required current / SOTA reconnaissance

Constraint-level evaluation work (`MCJudgeBench`, `RubricEval`), ODRL policy modelling, and contract-monitoring event calculus are in the ledger; re-date at execution.

## 9. Required primary-source classes

Class 5.1 for policy and rights standards; 5.2 for constraint-level evaluation; 5.6 for editorial adjudication of ambiguous obligations.

## 10. Comparison set

Free-text goal; templated contract; compiled obligation graph; policy-language encoding.

## 11. Experiments or bake-offs

Decompose both fixture goals into obligation records in two independent sessions and measure disagreement; encode one waiver and one norm conflict in each slice.

## 12. Representative workloads or fixtures

`goal:api-reference-v1` and `goal:portfolio-about-v1` inside the fixtures; the three prose norms.

## 13. Scale and budget analysis

Not yet specified.

## 14. Security, privacy, licensing, governance

Licensing determination is required before any guide-derived rule is committed; see `BOOTSTRAP.md` section 10.4.

## 15. Interoperability and migration

Candidate mappings to ODRL and SHACL result vocabularies; not written.

## 16. Deliverables

Goal-contract requirements; decomposition rules; prior record contract; precedence and exception cases; paired examples.

## 17. Falsification criteria

Rejected if independent decomposition of the same goal disagrees materially and the disagreement cannot be represented, or if norm conflicts cannot be represented without silent normalization.

## 18. Gate criteria

- `GP-G1` `j-editorial-wd2.1`: goal-contract and prior-contract review.

## 19. Downstream ADR or specification candidates

Goal-contract schema; normative-prior registry; precedence and conflict rules; style-guide licensing policy.

## 20. Residual risk and revisit policy

Weak goals make weak evaluations; revisit after `GP-G1`.

## 21. Independence declaration

The only material is author-written fixture prose and a protocol proposal from the same lineage.
