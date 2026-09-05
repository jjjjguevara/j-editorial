#!/usr/bin/env python3
"""Apply narrowly scoped, hash-guarded owner-decision alignment. No dataset research.

The four allowlisted documents retain all unrelated material. This is a plain
one-time research maintenance script, not a packed payload or product generator.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BEFORE = {'BOOTSTRAP.md': '2d229b87861818f6c4040ce7baf1915fd2bd43c053b979f371510314305dedc2', 'ROADMAP.md': 'ded38a1409c81d42052b8f31b6a99c4a36b2f3235764840627bb97f35cfeb701', 'RESEARCH.md': 'ea7ed1971e56bd9dfce9e3633a3cf577d589d9e407846df26551608534463221', 'research/model-training-data/CHARTER.md': 'e4063d9f962029ab02363509d35d9a5c30be29b35a310e9fabec08b50e9f928b'}
AFTER = {'BOOTSTRAP.md': '60c2f0b973973b4e0207aa57c8025a8cf9c62a29881e0ce7f4999dbd7e9f49cf', 'ROADMAP.md': 'fe8b3118de44849a1b47f3a979c7c8d5a704b8a5affb328e30bde72134326542', 'RESEARCH.md': 'fefdd89c3a821c7245a47e3574c5182fea312a4128a27e2954421f9f1491bb5b', 'research/model-training-data/CHARTER.md': '55f5ade747be352cf0702179dcb80d49941b207611d7d766510673a9b86a1bfe'}

ACCEPTANCE = '''## Accepted research scope — 2026-09-04

The owner's accepted directions supersede older candidate wording in this document:

- D-01C: Amnesia API reference and portfolio About prose are co-gating research slices.
- D-02R: the Editorial Construction Space is a cross-cutting analytic scaffold;
  typed plural records are logical distinctions, not mandatory separate objects.
- D-03: causal event transactions, time-scoped facts/fluents, exact checkpoints,
  and versioned projections are the accepted research shape, not a storage choice.
- D-04B: meaningful semantic operations plus checkpoints; keystroke capture is optional.
- AMN-01: pinned product inspection and isolated tests are permitted, without source mutation.
- D-01P: only `sci-jjjjguevara/src/pages/about.astro` at the accepted immutable revision
  is target prose; supporting profile/brief/history records are evidence or norms.

Scope authorities: [D-03 acceptance](research/phase-2/D-03-ACCEPTANCE.md),
[D-01P acceptance](research/phase-2/D-01P-ACCEPTANCE.md), and
[Phase 2 gates](research/phase-2/STAGE-GATE.md). PR #2 was merged at
`0d24e78713ed7a2c04810ce9961e5c28ab3da096` following owner approval.

Phase 3 tests behavioral integrity, targeting, representation alternatives and
research protocols. It does not select production representation, persistence,
a programming language, or an ADR. The implementation gate remains closed.
Model-training dataset research is explicitly held for a separate session.

'''


def one(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"expected one replacement anchor: {old[:90]}")
    return text.replace(old, new, 1)


def section(text: str, start: str, end: str, body: str) -> str:
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError("section anchors are not unique")
    a, b = text.index(start), text.index(end)
    if b <= a:
        raise ValueError("section order changed")
    return text[:a] + body.rstrip() + "\n\n" + text[b:]


def transform(path: str, text: str) -> str:
    if path == "BOOTSTRAP.md":
        text = one(text, "## 0. How to read this contract", ACCEPTANCE + "## 0. How to read this contract")
        text = section(text, "## 3. Core system hypothesis", "## 4. Bootstrap invariants", '''## 3. Accepted research hypothesis

The current research model is:

`Goal + Norms + Exact Artifact Checkpoints + Typed Editorial Data + Evidence + Causal Transactions + Time-scoped Conditions + Versioned Projections`

One datum may simultaneously participate in constructive, referential, and
pragmatic/governance relations. These are not mutually exclusive storage layers.

`decide(S, command) -> proposed/accepted transaction | rejection | abstention`

`evolve(S, transaction, reducer_version) -> S'`

`project(S', goal_version, projection_version) -> findings/gaps/readiness/report`

An observation records that an evaluator produced a result; it does not by itself
make the conclusion true. An obligation is not a finding, and an accepted proposal
is not proof of a successful operation. A condition may hold between events.
Exact source reconstruction requires available material checkpoints.

`GapField = unresolved adverse findings or unsatisfied applicable obligations`

Gap is a derived view under a particular goal, norm, evidence and interpretation,
not the universal ontology root. Historical transitions still retain before/after,
intent, evidence, authority, outcomes, rejection, failure and uncertainty.

The logical shape is authorized for falsification research only. Physical event-first,
fact-first, event–fluent and checkpoint+journal alternatives remain open. Semantic
replay, portable encoding and storage-order independence require execution evidence.''')
        text = section(text, "### 6.1 Provisional direction: structured editorial state", "### 6.2 Representation requirements to test", '''### 6.1 Research direction: authority by concern

Exact material state, editorial-semantic assertions and derived projections answer
different authority questions over one multidimensional state. They do not require
three stores, three exclusive layers, or a structured-first canonical document.

Source-first, structured-first, and composed representations remain alternatives.
Stable identity, source fidelity, opaque-syntax preservation, reconciliation and
migration evidence must precede a physical representation decision.''')
        text = one(text, "### 8.2 Quality vector\n\nThe current direction favors multidimensional observations over a canonical scalar. Candidate dimensions include:", "### 8.2 Heterogeneous quality observations\n\nThe current direction preserves typed multidimensional observations. Neither a scalar nor vector arithmetic defines canonical editorial state. Candidate observable concerns include:")
        text = one(text, "Editorial gaps are currently the most important candidate intermediate representation.", "Gap fields are derived views. Obligations, findings, evidence, decisions and continuing conditions remain distinguishable; the following gap families are classification candidates, not universal root objects.")
        text = one(text, "## 17. Training-data vertical", "## 17. Training-data vertical\n\n**Held:** this section reserves downstream questions. No dataset research, corpus construction, labeling, split generation, preference extraction or training is released by the Phase 2 merge or Phase 3 research.")
    elif path == "ROADMAP.md":
        text = one(text, "## 0. Roadmap contract", ACCEPTANCE + "## 0. Roadmap contract")
        text = one(text, "### 3.2 Doc Doctor should prove the framework, not define it", "### 3.2 Paired research proof precedes Doc Doctor integration\n\nThe first research proof co-gates the bounded Amnesia API reference and portfolio\nAbout page. Success on one cannot stand in for the other. Source parity and prose\nadjudication retain different methods. Phase 2's paired representation result is\nnot an empirical model-quality, reader-success, or production-generalization result.\nDoc Doctor remains the intended first downstream reference integration.\n\n#### Doc Doctor should prove the framework, not define it")
    elif path == "RESEARCH.md":
        text = one(text, "Status: **provisional / bootstrap-scoped / not yet an execution record**", "Status: **bootstrap-scoped / research executed in phase packets / architecture held**")
        text = one(text, "This file is a **pre-bootstrap scaffold**.", "This file is the bootstrap research-method charter. Accepted decisions and actual execution reside in versioned phase packets; earlier scaffolding language below remains a description of the revision process, not a prohibition on already authorized research.")
        text = one(text, "## 0. Bootstrap status and mandatory revision rule", ACCEPTANCE + "## 0. Bootstrap status and mandatory revision rule")
        text = section(text, "## 17. Program registry", "## 18. Beads relationship", '''## 17. Program registry

Program identifiers name research boundaries, not Beads issue IDs or a substitute
execution tracker. Phase results do not automatically close a whole program.

| Program | Boundary and evidence | Remaining gate |
|---|---|---|
| BR-FRAME / BR-DOM | Cross-cutting space and typed distinctions; Phase 2 paired fixtures | Broader falsification and accepted glossary |
| BR-EVENT-STATE | Events, fluents, causal replay; Phases 2–3 | Representation/history recommendation review |
| BR-AMN | Pinned source parity and technical fixture | Isolated product build and developer-task evidence |
| BR-PROSE | Accepted About target and real edit history | Built-output parity and empirical reader evidence |
| BR-GOAL / BR-PRIORS | Scope, obligations, norm applicability, exceptions | Goal and prior contract review |
| BR-REP | Exact material, targeting, reconciliation, alternatives | Real syntax/identity and migration evidence |
| BR-HIST | D-04B history, transaction, export and recovery workloads | Full candidate bake-off; no backend selected |
| BR-EVAL | Obligation-specific graders and adjudication protocol | Empirical reliability and adversarial meta-evaluation |
| BR-SEC | Authority, hostile content, retention and erasure | Deployed-control evidence remains absent |
| BR-INT-DD | Doc Doctor consumer/migration boundary | Downstream of reviewed paired synthesis |
| Model-training data | `research/model-training-data/CHARTER.md` | Explicitly held; separate-session release required |

[Phase 2 gates](research/phase-2/STAGE-GATE.md) record accepted evidence;
[Phase 3](research/phase-3/README.md) records subsequent experiments. None is a
production architecture authorization. No dataset research has been executed.''')
    elif path == "research/model-training-data/CHARTER.md":
        text = one(text, "Status: **placeholder / pre-bootstrap / research not yet authorized**", "Status: **bootstrap-aligned placeholder / HELD / research not authorized**")
        text = one(text, "## 0. Bootstrap revision rule", '''## Bootstrap dependency alignment — 2026-09-04

Terminology/dependencies only; no source collection, dataset design, experiment,
format choice, storage choice, budget research or training is executed here.

The upstream editorial research shape now distinguishes identity-bearing data,
causal transactions, time-scoped conditions, exact checkpoints and versioned
projections. The Amnesia/About fixtures are architecture probes, not a corpus.
Any future program must consume reviewed editorial identity, goal/prior, history,
rights, retention and evaluation contracts. Historical acceptance is not automatic
training eligibility or a preferred/rejected label. This charter remains a placeholder;
its detailed tracks below must be rescoped at the separately authorized session.

## 0. Bootstrap revision rule''')
        text = one(text, "**`PLACEHOLDER / PRE-BOOTSTRAP`**", "**`BOOTSTRAP-ALIGNED PLACEHOLDER / HELD`**")
    else:
        raise ValueError("path not allowlisted")
    return text


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    changes = {}
    for path, expected in BEFORE.items():
        raw = (ROOT / path).read_bytes()
        h = hashlib.sha256(raw).hexdigest()
        if h == AFTER[path]:
            changes[path] = {"status": "already-aligned", "sha256": h}
            continue
        if h != expected:
            raise ValueError(f"concurrent or unreviewed change to {path}; refusing overwrite")
        revised = transform(path, raw.decode("utf-8")).encode("utf-8")
        new_hash = hashlib.sha256(revised).hexdigest()
        if new_hash != AFTER[path]:
            raise ValueError(f"unexpected transformation bytes for {path}")
        changes[path] = {"before": h, "after": new_hash}
        if args.apply:
            (ROOT / path).write_bytes(revised)
    print(json.dumps(changes, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
