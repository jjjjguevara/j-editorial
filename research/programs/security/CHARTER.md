# Security, authority, privacy, and erasure — Charter

Slug: `security`  
Alias: `BR-SEC`  
Beads epic: `j-editorial-8dd`  
Lifecycle: **BOOTSTRAP-SCOPED**  
Controlling contract: `BOOTSTRAP.md`; method: `RESEARCH.md`

## 1. Authority and status

A baseline exists; no control has been tested. The baseline is sufficient to constrain research fixtures and insufficient for any production, provider, or publication claim.

## 2. Mission

Define trust zones, the authority matrix, the command/event security boundary, prompt-injection controls, integrity and provenance controls, disclosure rules, retention, and erasure semantics, then test them.

## 3. Why the program is separate

Imported content cannot grant authority, and append-only history conflicts with erasure; both cut across every other program.

## 4. Decisions or specification questions it informs

`BOOTSTRAP.md` ADR queue items 45 to 49.

## 5. In scope / out of scope

In scope: the ten threat scenarios; authority for read, retrieve, propose, apply, accept, publish, export, delete, retention change, provider disclosure.  
Out of scope: legal determinations.

## 6. Dependencies on other programs

Runs in parallel; gates `representation`. Downstream: `model-training-data` (held).

## 7. Hypotheses under attack

- H1. Model output can recommend but never authorize. Status: stated; untested.
- H2. Erasure can be represented as declared replay loss without misleading audit semantics. Status: represented in fixtures; SQLite probe shows logical deletion is not erasure.

## 8. Required current / SOTA reconnaissance

OWASP prompt-injection and agent-security guidance, NIST AI RMF, GDPR Article 17 are in the ledger; re-date at execution.

## 9. Required primary-source classes

Class 5.1 for guidance and regulation; 5.5 for fault tests.

## 10. Comparison set

Keyword filters (rejected); structured message separation; typed tool schemas with session authority; human approval for consequential actions.

## 11. Experiments or bake-offs

`SEC-G1`: execute `SEC-T01` to `SEC-T10` against a research harness and document which controls fail.

## 12. Representative workloads or fixtures

The erasure branches in both fixtures; the opaque-block round-trip in Phase 3 (trivial).

## 13. Scale and budget analysis

Not applicable yet.

## 14. Security, privacy, licensing, governance

This program is that concern.

## 15. Interoperability and migration

Provider terms and retention must be recorded per disclosure.

## 16. Deliverables

Threat model; authority matrix; deletion and redaction tests; control failure register.

## 17. Falsification criteria

A control is rejected if any threat scenario produces an authority transition from content or model output.

## 18. Gate criteria

- `SEC-G1` `j-editorial-8dd.1`: authority and hostile-content fault tests.

## 19. Downstream ADR or specification candidates

Sensitive-data classification; erasure semantics; executable-grader sandbox; hostile-content boundary.

## 20. Residual risk and revisit policy

A content hash can be linkable and therefore sensitive.

## 21. Independence declaration

Baseline by the same lineage; no adversarial execution.
