# Research tree

This directory holds every research artifact of the bootstrap. It is organized by **program**, with frozen **packets** for each execution run, one **ledger** of sources, and one **decision log**. `RESEARCH.md` at the repository root defines the method; `BOOTSTRAP.md` remains the controlling contract.

```text
research/
  README.md          this map
  LEDGER.md          unified source ledger; new work cites SRC-### only
  decisions/         owner decisions with verbatim statements and acceptance records
  programs/<slug>/   living state of one research program
    CHARTER.md         question, scope, dependencies, falsification, gates
    RESULTS.md         dated result entries, gate decompositions, evidence reclassifications
    COVERAGE.md        contract-case coverage matrix (where the program owns one)
    fixtures/ tools/ results/   program-owned executable material
  packets/<date>-<name>/   frozen record of one execution run: README, gates, reproduction, ledgers
  templates/         charter, pre-registration, results-entry, and coverage templates
  tools/             repository-wide checks: link check, registry rendering
```

## Programs

| Slug | Alias | Title | Lifecycle |
|---|---|---|---|
| `frame-domain` | BR-FRAME / BR-DOM | Editorial Construction Space and typed domain distinctions | ACTIVE |
| `event-state` | BR-EVENT-STATE | Causal event–fluent editorial state | ACTIVE |
| `amnesia` | BR-AMN | Amnesia technical-reference proof | ACTIVE |
| `prose` | BR-PROSE | General-prose proof on the portfolio About page | ACTIVE |
| `paired-synthesis` | paired-proof synthesis | Paired technical-reference and general-prose synthesis | ACTIVE |
| `goal-priors` | BR-GOAL / BR-PRIORS | Goal contracts and normative priors | BOOTSTRAP-SCOPED |
| `representation` | BR-REP | Representation, targeting, and authority | ACTIVE |
| `history` | BR-HIST | History and persistence | BOOTSTRAP-SCOPED |
| `evaluation` | BR-EVAL | Evaluation science | BOOTSTRAP-SCOPED |
| `security` | BR-SEC | Security, authority, privacy, and erasure | BOOTSTRAP-SCOPED |
| `doc-doctor-integration` | BR-INT-DD | Doc Doctor consumer and migration boundary | PLACEHOLDER |
| `model-training-data` | DG-00..DG-14 | Model-training dataset architecture, engineering, and governance | HELD PLACEHOLDER |

The authoritative registry is the Beads tracker; `RESEARCH.md` section 17 is rendered from it with `research/tools/render_registry.py`.

## Packets

| Packet | Content |
|---|---|
| [`2026-09-04-phase-1-adversarial-review`](packets/2026-09-04-phase-1-adversarial-review/README.md) | Phases 1, 1.1, 1.2: adversarial review, owner-decision holds, next-phase contract, legacy ledgers |
| [`2026-09-04-phase-2-foundations`](packets/2026-09-04-phase-2-foundations/README.md) | Phase 2: gates, reproduction instructions, legacy ledger |
| [`2026-09-04-phase-3-behavioral-probes`](packets/2026-09-04-phase-3-behavioral-probes/README.md) | Phase 3: behavioral probes, cross-program results, runner, contract-alignment record |
| [`2026-09-04-restructure-program-major`](packets/2026-09-04-restructure-program-major/README.md) | This restructure: file map, link rewrite, ledger consolidation, digest equivalence |
| [`2026-09-05-bootstrap-contract-review`](packets/2026-09-05-bootstrap-contract-review/README.md) | Independent static contract review; 14 findings, full question/ADR routing, proposed amendments, and retained validation evidence; no gates released |

Packets are frozen. Their documents keep the verdict vocabulary they were written with; the program `RESULTS.md` files restate each gate in the unified vocabulary of `RESEARCH.md` section 3.

## Reproduction

```bash
python3 research/tools/check_links.py .
python3 research/programs/event-state/tools/validate_event_fluent_fixture.py research/programs/event-state/fixtures/amnesia-notes-event-fluent.json
python3 research/programs/prose/tools/validate_portfolio_prose_fixture.py research/programs/prose/fixtures/portfolio-about-event-fluent.json
python3 research/packets/2026-09-04-phase-3-behavioral-probes/tools/run_experiments.py --output /tmp/behavioral-probes.json
```

Passing these commands establishes internal consistency of hand-authored fixtures and reproduction of recorded digests. It does not establish any research claim; see the program results for what each gate did and did not show.
