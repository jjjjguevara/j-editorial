# Coverage matrix — <program or synthesis>

Rows are the contract cases the program is accountable for. Columns name the fixture transactions, checks, or executed tests that exercise each case. "trivial" marks coverage that cannot fail; "none" marks an uncovered case. An uncovered or trivial row blocks PASS for the gate that depends on it.

| Case | Source of the case | Technical slice coverage | Prose slice coverage | Strength | Notes |
|---|---|---|---|---|---|
