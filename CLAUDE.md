# Project Instructions for AI Agents

This file provides instructions and context for AI coding agents working on this project.

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:6cd5cc61 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

## Agent Context Profiles

The managed Beads block is task-tracking guidance, not permission to override repository, user, or orchestrator instructions.

- **Conservative (default)**: Use `bd` for task tracking. Do not run git commits, git pushes, or Dolt remote sync unless explicitly asked. At handoff, report changed files, validation, and suggested next commands.
- **Minimal**: Keep tool instruction files as pointers to `bd prime`; use the same conservative git policy unless active instructions say otherwise.
- **Team-maintainer**: Only when the repository explicitly opts in, agents may close beads, run quality gates, commit, and push as part of session close. A current "do not commit" or "do not push" instruction still wins.

## Session Completion

This protocol applies when ending a Beads implementation workflow. It is subordinate to explicit user, repository, and orchestrator instructions.

1. **File issues for remaining work** - Create beads for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **Handle git/sync by active profile**:
   ```bash
   # Conservative/minimal/default: report status and proposed commands; wait for approval.
   git status

   # Team-maintainer opt-in only, unless current instructions forbid it:
   git pull --rebase
   git push
   git status
   ```
5. **Hand off** - Summarize changes, validation, issue status, and any blocked sync/commit/push step

**Critical rules:**
- Explicit user or orchestrator instructions override this Beads block.
- Do not commit or push without clear authority from the active profile or the current user request.
- If a required sync or push is blocked, stop and report the exact command and error.
<!-- END BEADS INTEGRATION -->


## Build & Test

There is no product code yet. The quality gates are the research reproduction checks:

```bash
python3 research/tools/check_links.py .
python3 research/programs/event-state/tools/validate_event_fluent_fixture.py research/programs/event-state/fixtures/amnesia-notes-event-fluent.json
python3 research/programs/prose/tools/validate_portfolio_prose_fixture.py research/programs/prose/fixtures/portfolio-about-event-fluent.json
python3 research/packets/2026-09-04-phase-3-behavioral-probes/tools/run_experiments.py --output /tmp/behavioral-probes.json
python3 research/tools/render_registry.py --check   # requires bd; verifies RESEARCH.md registry matches the tracker
```

Passing them shows internal consistency and reproduction of recorded digests, not any research claim.

## Architecture Overview

Pre-implementation repository under the `ADVERSARIAL-REVIEW-REQUIRED` gate. `BOOTSTRAP.md` is the controlling contract, `RESEARCH.md` the research method, `ROADMAP.md` the hypothesis register. Research lives under `research/` in a program-major layout: `research/programs/<slug>/` holds each program's charter, results, fixtures, and tools; `research/packets/` holds frozen execution records; `research/decisions/` holds owner decisions with verbatim statements; `research/LEDGER.md` is the only source ledger new work may cite. Start at `research/README.md`.

## Conventions & Patterns

- Read `BOOTSTRAP.md` before proposing any structure or code; the implementation gate is closed.
- Research method rules in `RESEARCH.md` sections 21 to 28 apply to every new fixture, validator, or result: pre-register before authoring, keep fixture author, validator author, and red team in separate sessions, commit raw bytes beside every digest, label agent reading as expert or secondary evidence and never as deterministic, use only the five gate verdicts, and maintain the coverage matrix.
- Controlling documents are never edited by CI or scripts; superseded text is preserved verbatim; owner decisions are recorded with their exact words in `research/decisions/DECISION-LOG.md`.
- Beads is the program registry: one epic per program labeled `research-program`, one task per gate labeled `gate`. Render the `RESEARCH.md` registry with `research/tools/render_registry.py` after tracker changes.
- Packets under `research/packets/` are frozen; only links and superseded banners may change.
