# Portfolio prose companion candidate audit

Status: **candidate decision packet / owner scope required**  
Program: `BR-PROSE` preflight  
Candidate source system: `jjjjguevara/sci-jjjjguevara`  
Inspected source ref: `1c93b60e75ce60203295a988b8125d44e6acb6bc`  
Research cutoff: **2026-09-04**  
Implementation authorization: **not granted**  
Dataset research: **not executed**

## 1. Decision result

The portfolio repository is a strong source system for the general-prose half of D-01C, but the whole website is not an appropriate first artifact boundary.

The site contains several different editorial objects and authorities:

- homepage positioning and catalogue copy;
- biography and chronology;
- résumé and machine-readable records;
- technical case studies;
- research summaries;
- product demonstrations;
- privacy and contact copy;
- protected Field Notes routes;
- executable metadata, tests, and deployment behavior.

Treating all of these as one prose artifact would make failures difficult to interpret. A claim could fail because of biography, project parity, interface behavior, structured data, privacy policy, access control, or site architecture. That would weaken the paired proof rather than broaden it.

**Recommended D-01P scope:** use the public About page as the canonical prose target and treat the portfolio's approved brief, canonical profile, résumé record, history, and validation scripts as contextual evidence and norms.

```text
Target artifact:
  repository: jjjjguevara/sci-jjjjguevara
  commit:     1c93b60e75ce60203295a988b8125d44e6acb6bc
  path:       src/pages/about.astro
  blob:       d56c560fc63569b471cc4e81a65daf52568fe754
  route:      /about

Supporting records, not target prose:
  docs/personal-site-creative/creative-brief.md
  docs/personal-site-creative/prose-audit-2026-08-16.md
  src/data/profile/canonical.yaml
  src/data/resume.ts
  scripts/personal-site-creative/verify-visible-prose.mjs
  scripts/portfolio-remediation/verify-facts.mjs
  docs/portfolio-remediation/evidence-ledger.yaml
```

This is a recommendation awaiting explicit owner confirmation. It is not yet D-01P acceptance.

## 2. Pinned source ledger

| ID | Source | Ref / identity | Supported observation | Limitation |
|---|---|---|---|---|
| `PF-01` | `jjjjguevara/sci-jjjjguevara` `master` | commit `1c93b60e75ce60203295a988b8125d44e6acb6bc` | Current inspected repository state and source-tree boundary. | Moving `master` is reconnaissance only; formal fixtures must retain this immutable ref or deliberately select another. |
| `PF-02` | `src/pages/about.astro` | blob `d56c560fc63569b471cc4e81a65daf52568fe754` at `PF-01` | Current About-page prose, chronology, working-context claims, and HTML structure. | Astro source mixes prose with presentation markup; a prose projection must identify what is evaluated. |
| `PF-03` | `docs/personal-site-creative/creative-brief.md` | blob `8a2ea661cedfb9124050acf56e6a0142168c9ebe` | Approved site purpose, writing fingerprint, anti-style rules, About-page requirements, recruiter-scanning constraint, and machine/visible-fact consistency requirements. | A product-specific brief; not a universal editorial prior. |
| `PF-04` | `src/data/profile/canonical.yaml` | blob `486d6d4f3e686e3348bb689b0ad7297b49cc8aab` | Owner-approved chronology, education, location, languages, and positioning record. | Repository-owner attestation, not independent documentary verification. |
| `PF-05` | `src/data/resume.ts` | blob `c226de4e03defc763278d167766ffbbdcff219bf` | Machine-readable résumé facts and positioning used elsewhere on the site. | Duplicates some profile/About facts; agreement can reflect common authorship rather than independent corroboration. |
| `PF-06` | commit `900483708d74e83c5f4acd3b308127f7fa430117` | 2026-08-17 | Real prose audit replaced vague career positioning, inferential framing, defensive disclaimers, keyword copy, and British/American inconsistencies; added a regression check. | Commit acceptance does not prove every replacement uniquely optimal. |
| `PF-07` | commit `ddf0bcee6dc95d1deac016d8e47ee286d5c04055` | 2026-08-18 | Removed decorative About-page eyebrow and section-index labels while preserving content and hierarchy. | Establishes a design/edit decision, not universal evidence against labels. |
| `PF-08` | `scripts/personal-site-creative/verify-visible-prose.mjs` | blob `3610e83ebe799f4d41ba5e9541e55fbdab21cb97` | Curated deterministic checks for prohibited rhetorical patterns, decorative labels, stale provenance language, and spelling conventions. | Regex checks can produce false positives/negatives and cannot establish clarity, truth, or audience fitness. |
| `PF-09` | `scripts/portfolio-remediation/verify-facts.mjs` | blob `efb5cfc7b149763f64376416ab03552a64d4a426` | Guard for required canonical facts and title-inflation/disclaimer regressions. | Checks presence in the canonical profile, not evidence authenticity or every visible projection. |
| `PF-10` | `docs/portfolio-remediation/evidence-ledger.yaml` | blob `8e3175310eefd452a60faca9799a30381ef4f6f2` | Declares professional facts as an approved owner-supplied profile and records evidence limits for projects. | Sparse ledger; it does not independently verify employment or education. |
| `PF-11` | `src/pages/sitemap.xml.js` | blob `ef8c301667e6249fdea76e32987c8f573d757059` | `/about` is included in the public sitemap. | Sitemap inclusion does not prove current deployment equivalence. |
| `PF-12` | `src/middleware.ts` | blob `16d4d9ffd75ba2355a2b47199f3e90dacc3cbd27` | Special private/no-store/noindex handling applies to protected Field Notes descendants, not `/about`. | Source inspection does not replace production-response verification. |

## 3. Why the About page is a valid general-prose counterweight

The About page differs materially from the Amnesia API-reference slice.

| Amnesia technical reference | Portfolio About page |
|---|---|
| Callable signatures and runtime behavior dominate. | Biography, chronology, professional identity, and working context dominate. |
| Many obligations can be type-checked or executed. | Some facts can be cross-checked, but emphasis, sequence, tone, sufficiency, and privacy require judgment. |
| Product source is an external referent for documentation claims. | The person and their records are referents; several claims begin as owner attestation. |
| One correct signature may be uniquely determined. | Several accurate and audience-fit phrasings or structures may be defensible. |
| Security language concerns capability behavior. | Safety concerns include title inflation, misleading implication, unnecessary personal disclosure, and résumé-style self-positioning. |

The page also has genuine editorial history rather than a constructed before/after pair. `PF-06` and `PF-07` preserve two distinct operation families:

1. semantic/rhetorical rewriting under an approved writing brief; and
2. structural/presentational simplification without changing the underlying biography.

These are useful because neither operation can be graded only by textual similarity to the accepted output.

## 4. Candidate goal contract

> At the pinned portfolio revision, the About page enables a professional reader to understand Josué Guevara's chronology, current technical/editorial practice, education, and working context accurately and efficiently, while preserving appropriate uncertainty and privacy and avoiding title inflation, résumé-keyword prose, defensive self-validation, and manufactured rhetorical effects.

### Audience

Primary:

- recruiters and hiring decision-makers scanning professional facts;
- technically informed readers evaluating the work and its author.

Secondary:

- prospective collaborators or clients seeking concise working context.

The secondary audience is a hypothesis to test, not a reason to introduce conversion-copy conventions rejected by the brief.

### Scope

In scope:

- the visible textual content and semantic heading/list structure of `src/pages/about.astro`;
- agreement with the pinned owner-approved profile and résumé records;
- the approved portfolio writing brief and its About-page requirements;
- prior About-page revisions that reveal editorial decisions;
- source-versus-built-output equivalence once an isolated build is available.

Out of scope:

- redesigning the full portfolio;
- scoring the subject's career or employability;
- verifying private employment, academic, identity, or immigration records;
- ingesting protected Field Notes or private career-archaeology content;
- evaluating Amnesia/Doc Doctor implementation claims through this prose fixture;
- optimizing conversion, SEO ranking, or keyword density;
- model-training dataset construction.

## 5. Evidence and fact-check boundary

The initial fixture should distinguish three evidence levels:

```text
Level A — source-state fact
  The pinned page/profile/resume contains a particular claim.

Level B — internal consistency
  The same owner-approved fact agrees across the About page,
  canonical profile, résumé record, structured metadata, and dates.

Level C — independently substantiated biography
  External documentary evidence establishes the underlying claim.
```

Phase 2 can establish Levels A and B. It must not imply Level C without separately authorized evidence.

Candidate factual authority:

- the owner is authoritative for intended public disclosure and first-person account;
- `src/data/profile/canonical.yaml` is the current repository fact register;
- the résumé record is a projection/parallel representation, not independent proof;
- external evidence, when later authorized, may support or contradict the internal register;
- a human release decision must retain whether a claim is owner-attested, internally consistent, independently verified, disputed, or intentionally omitted.

## 6. Applicable norms

The fixture should bind, not universalize:

1. the approved creative brief's writing fingerprint;
2. its About-page content requirements;
3. its anti-style rules;
4. factual agreement between visible and machine-readable representations;
5. American-English convention selected by the project;
6. ordinary accessibility and semantic-HTML requirements;
7. privacy minimization appropriate to a public professional biography.

The regex prose checker is one deterministic grader for a narrow subset. It is not the canonical interpretation of the creative brief.

## 7. Seed findings and test cases

### PORT-F01 — duplicated factual authority can drift

The About page hard-codes chronology and education while the repository also has canonical profile and résumé records. Current agreement does not remove the architectural risk that one changes without the others.

Test:

- change an effective date in a fixture copy of the canonical profile;
- leave About unchanged;
- record an external-referent/profile event without an About edit;
- require the unchanged page to become stale under the relevant obligation.

This mirrors the Amnesia unchanged-doc/product-change case in a biographical domain.

### PORT-F02 — owner attestation is not independent verification

The evidence ledger describes professional facts as owner supplied. A grader must not upgrade internal consistency to externally verified truth.

Test statuses:

```text
owner-attested
internally-consistent
independently-verified
contradicted
disputed
intentionally-undisclosed
unknown
```

### PORT-F03 — working-context prose remains summary rather than demonstration

The creative brief asks the site, where possible, to make collaboration inspectable through:

```text
disagreement or constraint
  -> workshop/review process
  -> decision
  -> resulting artifact or system
```

The current page mostly lists that workshops, planning sessions, retrospectives, peer review, and distributed work occurred. Those statements may be accurate while remaining weak evidence for the intended reader outcome.

This is not automatically a defect. The short page may deliberately defer proof to project interiors. The goal contract must decide whether the About page must demonstrate working context directly, link to evidence, or only orient.

### PORT-F04 — accepted rhetoric is not a unique gold answer

The 2026-08-17 audit replaced vague and self-interpreting prose with concrete chronology and mechanisms. The accepted replacement is useful evidence of project norms, but several other rewrites could satisfy the same norm.

A valid eval must therefore grade obligations such as factuality, directness, scope, and audience fit rather than exact match to the accepted text.

### PORT-F05 — decorative-label removal is preference under a project rule

The 2026-08-18 commit removed labels such as `About`, `Biography`, `Working context`, and `Records` while retaining headings and prose. This is a legitimate accepted operation under the site's visual grammar; it is not universal proof that such labels are always bad.

### PORT-F06 — privacy can make omission the correct operation

A proposal may be factually true yet unsuitable for a public biography—for example, adding a private address, personal contact channel, unneeded employer detail, or protected Field Notes material.

The model must represent:

- truth or support;
- disclosure permission;
- audience need;
- privacy risk;
- rejection or redaction;

without collapsing them into one quality value.

## 8. Multiple defensible resolutions

For `PORT-F03`, at least three resolutions are plausible:

### Resolution A — retain the concise summaries

Treat the About page as orientation. Add no extra narrative; require project pages to carry detailed evidence.

Strength: preserves scanning speed and privacy.  
Risk: working-context claims remain weakly inspectable from the page itself.

### Resolution B — add one or two compact decision episodes

Replace selected generic context entries with brief concrete examples following constraint → process → decision → outcome.

Strength: shows rather than labels collaboration.  
Risk: length, confidentiality, and unequal emphasis may distort the page.

### Resolution C — add evidence links rather than prose expansion

Keep the summaries, but connect selected claims to public case-study sections or decision records.

Strength: maintains semantic zoom and gives interested readers proof.  
Risk: linked evidence may be technical, incomplete, or inaccessible and may make the About page dependent on another artifact.

The fixture must retain these as alternatives until an authorized reviewer selects, combines, or rejects them. Textual distance from the historical accepted page is not an adequate grader.

## 9. Candidate grader allocation

| Obligation | Primary method | Adjudication / limitation |
|---|---|---|
| Pinned text and structure | parser/source extraction | built-output comparison once available |
| Cross-record factual agreement | deterministic field/date comparison | agreement is not independent verification |
| Time-sensitive freshness | deterministic effective-time rule | owner decides acceptable precision and update interval |
| Prohibited prose patterns | existing regression rules plus focused tests | human review handles context and false positives |
| Title inflation | deterministic forbidden-claim checks | owner/career record authority resolves ambiguous titles |
| Chronology clarity | structured reader task | several valid orders and phrasings may pass |
| Working-context sufficiency | human review against goal | retain disagreement; do not use exact-match grading |
| Tone and rhetorical directness | structured rubric with cited spans | model judge prohibited from release authority until meta-evaluated |
| Privacy/disclosure | policy checks plus owner decision | truth does not imply permission to publish |
| Accessibility/semantic hierarchy | HTML/build/accessibility checks | does not establish prose quality |

## 10. Event–fluent trace to test

```text
PortfolioCheckpointBound(P0)
CreativeBriefActivated(N0)
ProfileRecordBound(F0)
        │
        ▼
ProseAndFactChecksExecuted
        │
        ▼
FindingsRecorded(
  rhetorical,
  structural,
  factual-consistency,
  audience-fit,
  privacy
)
        │
        ├── AlternativeRewriteProposed(A)
        ├── AlternativeRewriteProposed(B)
        └── EvidenceLinkingProposed(C)
        │
        ▼
OwnerReviewRecorded(
  accept | combine | reject | abstain,
  rationale,
  privacy boundary
)
        │
        ▼
CandidateAboutCheckpointMaterialized(P1)
        │
        ▼
ChecksReexecuted + HumanTaskObserved
        │
        ▼
ProfileFactChangesEffective(F1)
        │
        ▼
UnchangedAboutPageBecomesStale
```

One finding may simultaneously be factual, epistemic, normative, pragmatic, operational, and release-relevant. This supplies the non-technical cross-domain test required by D-02R and D-03.

## 11. Privacy and rights boundary proposed for acceptance

Selecting this candidate should authorize research-only use of:

- text already intentionally exposed on the public About route;
- bounded private-repository source and commit metadata needed to reconstruct the editorial history;
- the owner-approved profile/resume records only as internal consistency evidence;
- fixture-local transformations that do not modify or deploy the portfolio.

It should not authorize:

- copying protected Field Notes or other private narrative material into J-Editorial;
- exposing private repository source beyond bounded research evidence;
- importing email, addresses, credentials, personal identifiers, or unpublished career records;
- treating biography edits as preference labels or training truth;
- dataset research, corpus construction, model training, or external-provider disclosure;
- portfolio mutation, pull requests, deployment, or publication.

## 12. Alternatives considered

### A — About page only — recommended

Target `src/pages/about.astro`; use the brief, profile, résumé, history, and validators as evidence.

Why favored:

- bounded artifact and goal;
- clearly non-reference prose;
- real revisions under explicit norms;
- factual plus subjective obligations;
- manageable privacy surface;
- multiple valid editorial outcomes;
- avoids repeating the Amnesia technical-reference problem.

### B — Homepage plus About as one profile-narrative bundle

Adds cross-page consistency and positioning, but introduces multi-artifact identity and makes the first prose experiment harder to diagnose.

Use later as a generalization test after A.

### C — Entire public portfolio

Rejected for the first slice. It mixes biography, technical reference, product claims, research, interface behavior, structured data, access control, privacy, and release mechanics. It should become a later collection-level test, not the D-01P seed artifact.

### D — Protected Field Notes or incident narratives

Rejected absent separate authorization. They introduce access, confidentiality, personal-data, source-evidence, and publication-boundary concerns that are unnecessary for the first prose co-gate.

## 13. Pivotal owner decision

```text
D-01P-PORTFOLIO:
  A — accept src/pages/about.astro as the prose target;
      supporting portfolio records are evidence/norms only
  B — use homepage + About as a bounded profile-narrative bundle
  C — reject the portfolio and select another fixture strategy

Research-only private-source/history access:
  yes | restricted: ...

Public-personal-data boundary:
  use only details already present on /about | narrower: ...
```

**Research recommendation:** `A`, with research-only private-source/history access and the public-data boundary limited to details already present on `/about`.

Acceptance releases the bounded prose fixture and cross-domain falsification work only. It does not release implementation, persistence selection, ADR acceptance, portfolio mutation, dataset research, or PR #2 merge.
