# Source rechecks

Inspected 2026-09-05 through the web reader. These are rechecks of entries in the [single source ledger](../../LEDGER.md), not a second ledger or a new SOTA survey. The stable source identities remain `SRC-###`. Live pages are access-date references, not archived source bytes; no new webpage digest or archival-retention claim is made. Interpretation is expert judgment, not deterministic validation of the proposed design. No full copyrighted source is copied here.

| Existing source | Inspected scope | Use and limit in this review |
|---|---|---|
| `SRC-013` — [W3C Web Annotation Data Model](https://www.w3.org/TR/annotation-model/) | Recommendation; body/target, selectors, states, media-type applicability | Supports separating annotation identity from target selection/state. It does not guarantee identity after arbitrary edits or authorize an operation. AR-05. |
| `SRC-014` — [W3C PROV-O](https://www.w3.org/TR/prov-o/) | Entity/activity/agent and derivation/attribution relations | Provenance relations are useful priors; source authority, independence, and truth remain separate judgments. AR-05/07. |
| `SRC-089` — [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785.html) | Invariant JSON representation and serialization requirements | A declared profile matters for portable hashes. This review neither selects JCS nor claims the current tools implement it. AR-05. |
| `SRC-092` — [OWASP AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) | Least privilege; high-impact action integrity; untrusted input; data protection | Motivates external authorization and binding approval to the executed parameters. Guidance is not a passed security test. AR-12. |
| `SRC-114` — [Git update-ref](https://git-scm.com/docs/git-update-ref) | Expected old object and reference-transaction behavior | A bounded example of pre-state checking, not proof of atomicity across editorial state, files, and external effects. AR-06. |
| `SRC-116` — [SQLite secure_delete](https://www.sqlite.org/pragma.html#pragma_secure_delete) | Deleted-content handling and limitations | Current database behavior cannot establish deletion across external copies, checkpoints, exports, or backups. No legal compliance finding follows. AR-13. |
| `SRC-117` — [Howcroft et al., INLG 2020](https://aclanthology.org/2020.inlg-1.23/) | Official abstract and bibliographic metadata only | Supports defining evaluation constructs/reporting explicitly; neither the full paper corpus nor a statistical-power prescription was inspected. AR-10. |
| `SRC-119` — [Anthropic, 2026-01-09](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Tasks/trials, graders, outcomes, and evaluation limitations | Primary industrial guidance for separating outcomes from traces and grader behavior. It does not validate a j-editorial benchmark or justify universal thresholds. AR-09/10/11. |

## Repository evidence inspected

All paths below refer to commit `360d6ed15fbee7d38dc659f8324763bf637b3924`, unless this packet explicitly marks proposed wording:

- `BOOTSTRAP.md`, `RESEARCH.md`, `ROADMAP.md`, and all program `CHARTER.md`/`RESULTS.md` records for documentary scope and outstanding gates.
- `research/decisions/DECISION-LOG.md` and `PR-3-RECONCILIATION.md` for recovered decisions and their qualifications.
- `research/programs/paired-synthesis/COVERAGE.md` for missing/trivial/declarative experimental coverage.
- Phase 1 adversarial and next-phase contracts, Phase 2 stage gates, Phase 3 behavioral and alignment records, and the program-major restructure packet for the prior review boundary.
- Existing reproduction/registry workflows and their raw artifacts for source acquisition and native tracker read-only verification.

These are the user's repository records, not independent confirmations of the research claims they describe. No newly retrieved private Amnesia, portfolio, or Doc Doctor content is disclosed in this packet.
