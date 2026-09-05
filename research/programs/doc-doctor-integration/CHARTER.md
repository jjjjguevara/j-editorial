# Doc Doctor consumer and migration boundary — Charter

Slug: `doc-doctor-integration`  
Alias: `BR-INT-DD`  
Beads epic: `j-editorial-vht`  
Lifecycle: **PLACEHOLDER**  
Controlling contract: `BOOTSTRAP.md`; method: `RESEARCH.md`

## 1. Authority and status

Placeholder. The Phase 1 inheritance audit is the only material. No Doc Doctor fixture exists, and the roadmap's Stage 2 hypothesis has received no evidence.

## 2. Mission

Map current Doc Doctor stubs, refinement, vectors, quality calculations, and Git milestones onto the framework vocabulary without making them core truth, and record incompatibilities and a rollback plan.

## 3. Why the program is separate

Doc Doctor is prior art and the intended first downstream integration; it must be evidence against the framework where it disagrees.

## 4. Decisions or specification questions it informs

`ROADMAP.md` Stage 2 gates A and B; `BOOTSTRAP.md` review exit criterion "a narrowly scoped first end-to-end use case" once the paired proof is synthesized.

## 5. In scope / out of scope

In scope: mapping, incompatibility ledger, fixture adapter design, rollback plan.  
Out of scope: modifying Doc Doctor; extraction of crates; any implementation.

## 6. Dependencies on other programs

Upstream: `paired-synthesis`. Downstream: bootstrap adversarial gate.

## 7. Hypotheses under attack

- H1. Doc Doctor's concepts map to the vocabulary without application-specific escape hatches. Status: untested; the Phase 1 audit lists twelve behaviors with candidate treatments.

## 8. Required current / SOTA reconnaissance

Re-inspect Doc Doctor at a new pinned commit; the Phase 1 inspection used `655c176f05a864887f03e0b392550ba2155a2e26`.

## 9. Required primary-source classes

Class 5.4 repository observation.

## 10. Comparison set

Bulk rename of crates (rejected by the roadmap) versus concept-by-concept review.

## 11. Experiments or bake-offs

Encode one real Doc Doctor editorial history in the vocabulary; this may double as the independent material for `FD-G1`.

## 12. Representative workloads or fixtures

None yet.

## 13. Scale and budget analysis

Not yet specified.

## 14. Security, privacy, licensing, governance

Existing telemetry was not collected with training reuse rights; see the dataset charter section 31.

## 15. Interoperability and migration

The whole program is a migration question.

## 16. Deliverables

Mapping; incompatibility ledger; fixture adapter design; rollback plan.

## 17. Falsification criteria

The framework is returned if common Doc Doctor editorial states require application-specific hacks.

## 18. Gate criteria

- `DD-G1` `j-editorial-vht.1`: Doc Doctor mapping and incompatibility ledger.

## 19. Downstream ADR or specification candidates

Import adapter boundary; Doc Doctor extraction boundary.

## 20. Residual risk and revisit policy

The paired proof replaced Doc Doctor as first proof without a roadmap revision entry; the `ROADMAP.md` revision table now records it.

## 21. Independence declaration

No material beyond the Phase 1 audit table.
