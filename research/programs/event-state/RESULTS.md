# event-state — Results

Entries are dated and cite their packet. Verdicts use the vocabulary of `RESEARCH.md` section 3. Restatements of earlier packet verdicts were made on 2026-09-04 during the restructure from the packets' own evidence and limitation lists.

## 2026-09-04 — Phase 1.2: D-03 event/state review

Packet: [`2026-09-04-phase-1-adversarial-review`](../../packets/2026-09-04-phase-1-adversarial-review/README.md)  
Pre-registration: none  
Executed by: bootstrap agent session; validated by: none; red team: none

### What ran

Literature synthesis of Moore machines, statecharts, event calculus, event structures, causal order, Datomic and XTDB models, and event-sourcing guidance; a worked Amnesia trace; sixteen falsification tests written before the fixture. See [`D-03-EVENT-STATE-REVIEW.md`](D-03-EVENT-STATE-REVIEW.md).

### Gate decomposition

| Obligation | Verdict | Evidence |
|---|---|---|
| Withdraw the three-exclusive-layers reading | PASS (argumentative) | review section 2 |
| Distinguish event, fluent, datum, transaction, checkpoint, projection | PASS (argumentative) | review section 5 |
| Owner acceptance of the shape with preserved statement | RETURN-WITH-FINDINGS | last preserved owner words are "research further before locking"; see decision log |

## 2026-09-04 — Phase 2: event–fluent experiment

Packet: [`2026-09-04-phase-2-foundations`](../../packets/2026-09-04-phase-2-foundations/README.md)  
Pre-registration: partial; the sixteen tests pre-date the fixture, the encoding protocol does not  
Executed by: bootstrap agent session; validated by: same lineage; red team: none until Phase 3

### What ran

`validate_event_fluent_fixture.py` over the 13-transaction fixture; checks `E-01` to `E-10` pass; committed result reproduces byte-for-byte at the new path on 2026-09-04.

### Gate decomposition

| Obligation | Verdict | Evidence |
|---|---|---|
| `E-01` to `E-10` expressibility | NARROW | each check verifies that author-written fields hold author-chosen values; cardinalities and transaction identifiers are hard-coded in the validator |
| Fixture integrity | RETURN-WITH-FINDINGS | Phase 3 showed the validator accepts unknown actors, backwards fluents, missing checkpoints, and undeclared subjects |
| Candidate-model comparison | RETURN-WITH-FINDINGS | a strong/medium/weak feature table, which the next-phase contract states cannot pass a gate |

### Evidence retention

| Record | Digest | Bytes committed at | Class after review |
|---|---|---|---|
| `evidence:static-contract:e1` raw checker output | `902116ab…` | nowhere | claim (5.8) |
| `docs:d1-fixture` corrected documentation fragment | `cac4b18e…` | nowhere | claim (5.8) |
| `product:p1-counterfactual` | `c819f360…` | nowhere; synthetic by design | scenario, not evidence |

The fixture bytes are hash-pinned and were not modified; reclassification lives here.

## 2026-09-04 — Phase 3: behavioral probes

Packet: [`2026-09-04-phase-3-behavioral-probes`](../../packets/2026-09-04-phase-3-behavioral-probes/README.md)  
Pre-registration: none  
Executed by: bootstrap agent session; validated by: CI reproduction; red team: the probes themselves red-teamed the Phase 2 validators

### What ran

Semantic guard with mutation audit (`M-*`), four encodings round-tripped and replayed at 35 heads (`R-*`), synthetic causal probes (`C-01` to `C-04`). Reproduced locally on 2026-09-04 at the restructured paths: 67 of 67 checks; digest equivalent to the original up to input path keys, see [digest-equivalence.json](../../packets/2026-09-04-restructure-program-major/results/digest-equivalence.json).

### Gate decomposition

| Obligation | Verdict | Evidence |
|---|---|---|
| Referential and causal integrity guard | PASS (bounded to the fixture format) | `M-1-*`, `M-2-*` |
| Information preservation across four encodings | PASS (trivial) | the encodings are re-nestings of one dictionary through one interpreter; round-trip equality is guaranteed |
| Discrimination between candidate models | RETURN-WITH-FINDINGS | none observed; the stated preference for the hybrid is unsupported by executed evidence |
| Causal reducer semantics on synthetic cases | PASS (bounded) | `C-01` to `C-04` |

## Open gates

`ES-G1` and `ES-G2`, tracked in Beads under epic `j-editorial-t2j`.

## 2026-09-04 — PR #3 provenance reconciliation

The earlier missing-owner-statement finding is supplemented by [recovered conversation context](../../decisions/PR-3-RECONCILIATION.md). Retrieval reports acceptance of the revised D-03 shape for the next research stage. The original transcript was not independently exported or authenticated; the receipt records that limitation. This is an administrative record correction, not an empirical gate verdict. `ES-G1` and `ES-G2` remain open; the earlier experiment limitations are unchanged.
