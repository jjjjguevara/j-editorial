# D-01P acceptance — portfolio About page as the general-prose companion

Status: **accepted research fixture / execution authorized**  
Owner acceptance: **2026-09-04**  
Owner statement: **“Yes proceed with A.”**  
Accepted antecedent: [`PORTFOLIO-PROSE-CANDIDATE-AUDIT.md`](PORTFOLIO-PROSE-CANDIDATE-AUDIT.md)  
Implementation gate: **closed**  
Persistence/ADR gate: **closed**  
Dataset research: **held**

This record translates the owner's selection of Option A into bounded research authority. It closes the artifact-selection hold in the candidate audit. The audit remains the pre-decision evidence record; this document is the controlling D-01P scope record.

## Accepted target

```text
repository:  jjjjguevara/sci-jjjjguevara
commit:      1c93b60e75ce60203295a988b8125d44e6acb6bc
path:        src/pages/about.astro
blob:        d56c560fc63569b471cc4e81a65daf52568fe754
route:       /about
projection:  visible text and semantic heading/list structure
```

The target is one public professional-biography artifact. The homepage, résumé page, project pages, research pages, product demonstrations, privacy/contact pages, Field Notes, protected Field Notes descendants, and private career-archaeology records are not part of the target.

## Supporting evidence and norms

The following may be inspected and bound to immutable identities as contextual evidence or applicable norms. They are not additional target prose:

- `docs/personal-site-creative/creative-brief.md`;
- `docs/personal-site-creative/prose-audit-2026-08-16.md`;
- `src/data/profile/canonical.yaml`;
- `src/data/resume.ts`;
- `scripts/personal-site-creative/verify-visible-prose.mjs`;
- `scripts/portfolio-remediation/verify-facts.mjs`;
- `docs/portfolio-remediation/evidence-ledger.yaml`;
- the bounded About-page history needed to reconstruct the accepted semantic rewrite and later structural simplification.

These records have different authority. A creative brief establishes project norms. A repository fact record establishes the owner's intended canonical representation. A résumé is a parallel projection, not independent corroboration. A validator establishes that a particular executable rule ran, not that the prose is globally good. Historical acceptance establishes an owner-controlled decision, not a unique gold answer.

## Goal contract

> At the pinned revision, the About page enables a professional reader to understand Josué Guevara's chronology, current technical/editorial practice, education, and working context accurately and efficiently, while preserving appropriate uncertainty and privacy and avoiding title inflation, résumé-keyword prose, defensive self-validation, and manufactured rhetorical effects.

Primary audiences:

- recruiters and hiring decision-makers scanning professional facts;
- technically informed readers evaluating the work and its author.

Secondary audience:

- prospective collaborators or clients seeking concise working context.

Hard requirements:

- chronology accuracy;
- consistency with the pinned owner-approved profile and résumé representations;
- no title inflation;
- privacy minimization;
- project-scoped prose directness;
- usable semantic heading/list structure.

Audience scanability and working-context sufficiency remain important but non-blocking under this first goal version. A stricter later contract may treat them differently, but a projection change must not rewrite the historical target or silently manufacture a defect.

## Evidence boundary

The research must retain three levels:

```text
A — source-state evidence
    A pinned page or record contains a claim.

B — internal consistency
    Owner-approved repository representations agree.

C — independent substantiation
    External documentary evidence establishes the underlying biography.
```

D-01P authorizes Levels A and B. It does not authorize inspection of private employment, education, identity, immigration, address, credential, or contact records for Level C. Internal agreement must not be described as independent verification.

## Review and release authority

- The owner may accept, reject, waive, authorize disclosure, and release.
- Research agents may inspect pinned source, record observations, construct bounded fixtures, and propose alternatives.
- Deterministic checkers may record rule results.
- Synthetic reviewer scenarios may exercise disagreement handling but have no release authority.
- Model or synthetic reader output must not be converted into release authority merely because it produces a score or recommendation.

## Privacy and rights boundary

Research-only use is authorized for:

- text and personal details already intentionally present on the pinned `/about` page;
- bounded source/history metadata required to reconstruct the relevant editorial transitions;
- fixture-local synthetic changes and redacted placeholders that do not assert or expose a real private detail.

The following remain prohibited:

- protected Field Notes or private career-archaeology ingestion;
- unpublished personal, employment, academic, identity, immigration, contact, address, credential, or financial records;
- disclosure of private source or personal data to an external model/provider without a separate accepted boundary;
- treating truth, support, audience value, and permission to disclose as one property;
- copying real private details into a public fixture;
- portfolio mutation, pull requests, deployment, or publication.

## Research authorized by this acceptance

- construct the bounded About-page event–fluent/checkpoint fixture;
- encode the two observed history operations without treating either accepted text as unique gold;
- test qualified evidence and internal-consistency states;
- retain several potentially acceptable remedies for a disputed prose finding;
- retain reviewer disagreement and owner deferral without forcing consensus;
- test privacy rejection/redaction using synthetic placeholders only;
- test a counterfactual profile change that makes an unchanged page stale;
- validate the fixture deterministically;
- compare the result with the Amnesia technical-reference fixture for representation adequacy.

## Not authorized

This acceptance does not select or authorize:

- production framework implementation;
- a persistence engine, event store, database, CRDT, schema, serializer, API, or package structure;
- an accepted representation/history ADR;
- a prose-quality benchmark or leaderboard;
- a reliable human/model prose grader;
- model-training dataset research, corpus construction, labeling, preference extraction, fine-tuning, or training;
- use of historical edits as automatic positive/negative preference labels;
- modification of `jjjjguevara/sci-jjjjguevara`.

## Stage boundary

D-01P closes only the prose-artifact selection gate. The fixture and paired-domain comparison must still execute and survive review. Even a passing representation co-gate cannot establish empirical reader success, grader reliability, independent biographical truth, live-site parity, or a production architecture.
