# amnesia — Results

Entries are dated and cite their packet. Verdicts use the vocabulary of `RESEARCH.md` section 3.

## 2026-09-04 — Phase 1.1: technical-slice audit

Packet: [`2026-09-04-phase-1-adversarial-review`](../../packets/2026-09-04-phase-1-adversarial-review/README.md)  
Pre-registration: none  
Executed by: bootstrap agent session; validated by: none; red team: none

### What ran

Reading of pinned documentation and product files through a repository connector; findings `AMN-F01` to `AMN-F04`; candidate goal contract, obligations, and grader allocation. See [`AMNESIA-DOCS-SLICE-AUDIT.md`](AMNESIA-DOCS-SLICE-AUDIT.md).

### Gate decomposition

| Obligation | Verdict | Evidence |
|---|---|---|
| Bounded surface and pinned refs identified | PASS | audit sections 3 and 5 |
| Contradictions found | PASS (by reading, class 5.4 observation recorded by an agent) | `AMN-F01`, `AMN-F02` |
| Authorization boundary defined | PASS | superseded by [`AMNESIA-ORACLE-AUTHORIZATION.md`](../../decisions/AMNESIA-ORACLE-AUTHORIZATION.md) |

## 2026-09-04 — Phase 2: oracle experiment

Packet: [`2026-09-04-phase-2-foundations`](../../packets/2026-09-04-phase-2-foundations/README.md)  
Pre-registration: none  
Executed by: bootstrap agent session; validated by: same lineage; red team: none

### What ran

Static findings `AMN-P2-F01` to `F04`, positive findings, a blocked runtime attempt, a synthetic correction used only in the fixture, and an obligation-specific precedence rule. See [`AMNESIA-ORACLE-EXPERIMENT.md`](AMNESIA-ORACLE-EXPERIMENT.md).

### Gate decomposition

| Obligation | Verdict | Evidence |
|---|---|---|
| Docs and product refs pinned to immutable identities | PASS | blob identities in the packet ledger |
| Static signature and synchrony contradiction | PASS as observation; method reclassified | recorded as tool `j-editorial-static-contract-observer 0.1.0` with confidence `deterministic-high`; no such executable exists and no type check ran. Class 5.6/5.7 agent reading until `AMN-G1` executes |
| Positive findings retained separately | PASS | experiment section 4 |
| Runtime build, type-check, focused tests | DEFER (not executed) | environment lacked an authenticated checkout; the owner's machine has one |
| Built-site and source equivalence | DEFER (not executed) | |
| Developer task | DEFER (not executed) | |

### Evidence retention

The raw checker output digest `902116ab…` has no committed bytes; see [`event-state/RESULTS.md`](../event-state/RESULTS.md). The `Docs Deploy` run `33239050109` is recorded as failed with cause unknown.

## 2026-09-04 — Independent verification during the review

Packet: [`2026-09-04-restructure-program-major`](../../packets/2026-09-04-restructure-program-major/README.md)  
Pre-registration: none  
Executed by: review session independent of the fixture author; method: reading `git show` output from local clones; class 5.4

### What ran

```bash
git -C ~/Documents/Builds/amnesia-docs show 5d8aa677793cc2b4734106bb21e6118f0cc5a2aa:src/content/docs/api/reference/commands-notes.md
git -C ~/Documents/Builds/amnesia show 4d0d1efec4ee4958db504cb56bcf47dfbc19b92a:apps/amnesia/src/api/types.ts
git -C ~/Documents/Builds/amnesia show 4d0d1efec4ee4958db504cb56bcf47dfbc19b92a:apps/amnesia/src/api/security/capabilities.ts
git -C ~/Documents/Builds/amnesia-docs log 5d8aa677793cc2b4734106bb21e6118f0cc5a2aa..HEAD -- src/content/docs/api/reference/commands-notes.md
git -C ~/Documents/Builds/amnesia diff --stat 4d0d1efec4ee4958db504cb56bcf47dfbc19b92a..HEAD -- apps/amnesia/src/api/
```

### Observations

- The documentation page declares `readiness: shipped`, `parity: full`, states that all methods are asynchronous, and lists `getNotes()` without parameters.
- The pinned public interface declares `getNotes(bookId: string): Note[]`, synchronous, and `getNote`, `getNoteForHighlight`, and `searchNotes` likewise synchronous.
- `expandCapabilities` returns `Set<Capability>`; the documentation declares `Capability[]`.
- The documentation page has no commits after the pin; the local docs branch head is the pinned commit.
- The product repository has 47 commits after the pin on the checked-out branch with no change under `apps/amnesia/src/api/`.

### Gate decomposition

| Obligation | Verdict | Evidence |
|---|---|---|
| Contradiction reproduced by an independent reader | PASS (reading, not execution) | observations above |
| Counterfactual product change has occurred | REJECT for the pinned range | API directory unchanged |

### What this entry does not establish

Runtime behavior, build success, or that the interface is the supported public contract. It remains class 5.4 reading.

## Open gates

`AMN-G1` and `AMN-G2`, tracked in Beads under epic `j-editorial-47m`.
