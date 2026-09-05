# paired-synthesis — Results

Entries are dated and cite their packet. Verdicts use the vocabulary of `RESEARCH.md` section 3.

## 2026-09-04 — Phase 2: paired-domain co-gate

Packet: [`2026-09-04-phase-2-foundations`](../../packets/2026-09-04-phase-2-foundations/README.md)  
Pre-registration: none  
Executed by: bootstrap agent session; validated by: same lineage; red team: none

### What ran

`validate_paired_domain.py` over the manifest and the two slice results; `C-01` to `C-07` pass; the committed result reproduces byte-for-byte at the new paths on 2026-09-04. See [`PAIRED-DOMAIN-RESULT.md`](PAIRED-DOMAIN-RESULT.md).

### Gate decomposition

| Obligation | Verdict | Evidence |
|---|---|---|
| Both slice results bound immutably | PASS | digests in the manifest |
| `C-01` to `C-07` cross-domain obligations | NARROW | each check verifies that the referenced `E-*` and `P-*` checks passed and that the manifest's conclusion strings match expected values; the underlying checks are NARROW in their programs |
| Non-overstatement of conclusions | PASS | the manifest's own conclusion fields say "not-established", "not-executed", "not-selected", "not-authorized", "not-passed" where appropriate |
| Generality of the vocabulary | NARROW | two same-owner, same-author artifacts; expressibility shown by construction |
| Contract-case coverage | RETURN-WITH-FINDINGS | three of fourteen shared cases uncovered, three trivial; see [`COVERAGE.md`](COVERAGE.md) |

### What this entry does not establish

Empirical reader performance, grader reliability, runtime behavior, or a production architecture, as the packet itself states.

## Open gates

`PS-G1` and `PS-G2`, tracked in Beads under epic `j-editorial-c8r`.
