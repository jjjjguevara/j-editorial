# Pre-registration — <experiment name>

Program: `<slug>`  
Committed before any fixture, validator, or result exists: **<commit>**  
Author (session): `<who>`

A fixture or validator authored before this document is committed cannot count toward a gate.

## 1. Question and decision informed
## 2. Hypotheses, stated so that they can fail
## 3. Encoding or measurement protocol

Exactly how material will be encoded, measured, or executed, including tools, versions, and inputs, fixed before the material is inspected.

## 4. Predicted outcomes and their interpretation

| Outcome | Interpretation | Gate consequence |
|---|---|---|
| … | … | PASS / NARROW / RETURN-WITH-FINDINGS / DEFER / REJECT |

## 5. Falsification criteria

What observation would reject or narrow the hypothesis. At least one criterion must be achievable with the planned material.

## 6. Controls and alternatives

The minimal competitor representation, method, or null model the experiment is compared against.

## 7. Independence plan

Fixture author, validator author, red team; separate sessions confirmed.

## 8. Evidence retention plan

Which raw outputs will be committed, where, and how their digests will be bound.

## 9. Deviations

Filled in after execution: every departure from sections 3–8 and why.
