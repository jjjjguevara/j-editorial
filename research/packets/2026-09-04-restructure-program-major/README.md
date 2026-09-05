# Restructure packet — program-major layout, unified ledger, decision log, method rules

Date: **2026-09-04**  
Branch: `research/restructure-program-major`, based on the Phase 3 head `8e8fd5dd…` (which includes the merged Phase 2 at `0d24e787…`)  
Owner basis (verbatim): "Please apply the reestructuring proposed."  
Beads: epic `j-editorial-7f2` with nine tasks `j-editorial-7f2.1` to `.9`  
Research claims made: **none**. Implementation, persistence, ADR, dataset, and bootstrap-exit gates: **unchanged, closed**

## 1. What this packet did

It applied the nine restructuring items proposed in the 2026-09-04 independent review of bootstrap phases 1 to 3 and accepted by the owner:

1. program-major layout with frozen packets;
2. pre-registration rule;
3. independence rule;
4. evidence-retention and method-label rules;
5. one source ledger with stable identifiers;
6. one gate vocabulary with obligation decomposition;
7. coverage matrices;
8. Beads as the program registry with a rendered table;
9. controlling-document discipline.

It also reclassified, in program results only, evidence records whose digests point at no committed bytes, and restated every earlier gate verdict in the unified vocabulary. Fixture bytes, committed validator results, and the verdict text of frozen packets were not changed.

## 2. Review findings that motivated it

Recorded here so the basis survives the session that produced it.

- Confirmation by construction: one lineage wrote hypotheses, fixtures, and validators in one day; validators hard-code the fixture's identifiers and cardinalities; no check could fail.
- No discriminating power: four "representation alternatives" were re-nestings of one dictionary through one interpreter.
- Evidence pointing at nothing: digests for raw checker output, the corrected documentation fragment, and prose evidence records with no committed bytes.
- Method mislabeled: an agent reading files through a connector recorded as a tool with `deterministic-high` confidence.
- Synthetic disagreement and same-owner artifacts presented as generality evidence.
- Three of fourteen contract cases uncovered, three trivial, with no matrix to show it.
- Source identifiers colliding across ledgers (`HIST-08`, `EVT-05`, `EVT-08`, `EVT-09`, `EVT-10`, `REP-03`, `REP-04`, `REP-06`, `SEC-01`, `SEC-03`, and others).
- Decision provenance thinning: `D-03` acceptance with no preserved owner statement; a CI bot rewriting the controlling contract and deleting the original formulation.
- Beads never used across three phases despite the contract requiring it; the runtime oracle never executed although the source clones exist locally.

## 3. File map

The complete old-to-new map is [`move-map.json`](move-map.json); every move used `git mv`, so history follows each file. Summary:

| Destination | Content |
|---|---|
| `research/programs/frame-domain/` | D-02 review; frame/domain result |
| `research/programs/event-state/` | D-03 review; event–fluent experiment; Amnesia fixture, validator, result |
| `research/programs/amnesia/` | slice audit; oracle experiment |
| `research/programs/prose/` | candidate audit; prose experiment; fixture, validator, result |
| `research/programs/paired-synthesis/` | paired result; manifest, validator, result; coverage matrix |
| `research/programs/representation/` | representation/history result; target fragments |
| `research/programs/evaluation/` | evaluation protocol |
| `research/programs/security/` | security baseline |
| `research/programs/model-training-data/` | held charter |
| `research/programs/{goal-priors,history,doc-doctor-integration}/` | new charters and results only |
| `research/decisions/` | both addenda, `D-02`, `D-03`, `D-01P` acceptances, owner decisions, Amnesia authorization, new decision log |
| `research/packets/2026-09-04-phase-1-adversarial-review/` | Phase 1 README, adversarial review, next-phase contract, 1.2 addendum, three legacy ledgers |
| `research/packets/2026-09-04-phase-2-foundations/` | Phase 2 README, stage gate, reproduction, legacy ledger |
| `research/packets/2026-09-04-phase-3-behavioral-probes/` | Phase 3 README, stage gate, results, legacy ledger, publication manifest, runner, alignment script, results |

New repository-wide files: `research/README.md`, `research/LEDGER.md`, `research/templates/*`, `research/tools/check_links.py`, `research/tools/render_registry.py`, one `CHARTER.md` and `RESULTS.md` per program, `research/programs/paired-synthesis/COVERAGE.md`.

## 4. Verification

| Check | Result |
|---|---|
| Files moved with `git mv` | 50 |
| Markdown files whose links were rewritten | 27; every relative link resolved against its old location, mapped, and re-relativized |
| Relative links checked after rewrite | 91, none dangling |
| Historical GitHub URLs pinned to old commits | 2 were touched by the path rewrite and restored to their original paths |
| Phase 2 validators at new paths | technical, prose, and paired results byte-identical to the committed files |
| Phase 3 runner at new paths | 67 of 67 checks; experiment digest `7cabdb92…` versus original `323ad6f8…`; [`results/digest-equivalence.json`](results/digest-equivalence.json) shows the digests are equal once input path keys are mapped and every other section is identical |
| Legacy ledgers consolidated | 150 rows from six sources into 125 unified rows plus 5 repository-evidence rows; 25 legacy identifiers registered as collisions |
| Workflows | write-permission publish workflow removed; reproduction workflow generalized to all research paths with a link check and digest comparison; tracker probe made manual |

## 5. Tools in this packet

- [`tools/rewrite_links.py`](tools/rewrite_links.py): the one-time link and path rewrite.
- [`tools/build_unified_ledger.py`](tools/build_unified_ledger.py): the one-time ledger consolidation. `LEDGER.md` is now hand-maintained; do not re-run this over it.
- [`tools/verify_digest_equivalence.py`](tools/verify_digest_equivalence.py): the Phase 3 digest equivalence proof.

## 6. What changed in frozen packets

Only relative links and repository-path strings inside them, the superseded banner at the top of each legacy ledger, and the paths inside the Phase 3 runner, whose original blob `4ee5855c…` is recorded in its header comment. The Phase 3 publication manifest and alignment script still name pre-restructure paths and hashes; they are historical records and were not edited.

## 7. Known consequences

- The original Phase 3 digest no longer reproduces at the new paths; the post-restructure result file beside it does, and the equivalence proof links them.
- The reproduction workflow now compares against the post-restructure digest read from the committed result, not a hard-coded value.
- `bd` is required to render or check the registry; CI does not run that step.
- The `D-03` acceptance is flagged in the decision log as lacking a preserved owner statement. Confirming it is one line from the owner.

## 8. What this packet did not do

No research claim was made or changed. No fixture, validator, or committed result was modified. No Amnesia, portfolio, or Doc Doctor source was touched. No dataset work. No commit, push, or tracker synchronization was performed by the restructuring session; the branch was left staged for owner review.
