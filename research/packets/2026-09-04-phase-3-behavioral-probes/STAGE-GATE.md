# Phase 3 bounded research gate

Gate: **BOOTSTRAP-P3-BEHAVIORAL-G0**  
Verdict: **pass-with-constraints for executed behavioral probes**  
Review status: **owner review pending**  
Implementation / production ADR / dataset gates: **closed**

## Scope passed

67 executed checks cover added reference/causal integrity guards, roundtrips through
four fair representation alternatives, 140 compared original head states,
storage-order invariance, concurrent conflict and explicit adjudication, a bounded
late-knowledge example, real About edit targeting, controlled transformations on
both domains, and native Git/SQLite mechanism tests.

The eight legacy-validator blind spots remain documented negative evidence. Their
new rejection does not retroactively expand what Phase 2 originally proved.
The governing documents now state the accepted research directions and paired proof;
the model-training charter receives status/dependency alignment only.

## Decisions not made

No representation or persistence winner is selected. Information preservation is
better supported than any physical ordering of the information. The four encodings
share one experimental interpreter; they are not independent implementations or
four native databases. Git and SQLite are reference probes, not product selections.

No semantic mapping across arbitrary rewrites is accepted. Missing text produces an
unresolved target. Identical matching context remains ambiguous. Human correspondence,
parser identity, split/merge semantics, source/DOM coordinates and CRDT approaches
remain subjects for research, not default production dependencies.

## Gate limitations

| Requirement | Current evidence |
|---|---|
| Exact bounded-fragment preservation | Executed; whole private checkpoint availability remains separate |
| Causal state and referential integrity | Bounded execution; arbitrary migrations and complete semantic constraints not proved |
| Known actor versus authenticated authority | Only actor-reference integrity; authentication/authorization not implemented |
| Real target movement | About label-removal history exercised; broader syntax, AST and DOM cases remain |
| Amnesia isolated build/runtime/type checks | Not executed in this phase; private checkout/lockfile execution still required |
| Portfolio source/build/live equivalence | Not established; literal source targeting only |
| Full substrate bake-off | Not executed; native Dolt/PostgreSQL/CRDT/temporal-store comparison still required |
| Empirical reader and grader reliability | Protocol proposed only; no participants or model trials |
| Erasure | Current-file negative/cleanup probes only; replicas, backups, snapshots and media not proved |
| Hostile-content safety | Data inertness only; no deployed agent security claim |
| Doc Doctor consumer migration | Still downstream; no source modification or adapter implementation |
| Native tracker | Separate access probe; inspect raw command exit codes before claiming fan-out |
| Dataset work | Explicitly held and not executed |

## Research released

The accepted upstream contract permits further isolated builds, richer targeting and
correspondence experiments, actual candidate persistence workloads, grader-protocol
pilot scoping, authority/security fault testing and later decision-packet synthesis.
Existing audience, artifact and data-boundary choices remain binding. New provider,
participant, cost, disclosure or production-risk decisions require explicit authority
when execution reaches them; no such choice is inferred from these results.

PR approval may accept this evidence, narrow the claims or return findings. It does
not close the bootstrap adversarial gate or authorize product implementation.
