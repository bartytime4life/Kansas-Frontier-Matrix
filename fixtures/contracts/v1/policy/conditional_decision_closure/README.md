# Conditional Decision Closure Fixtures

These synthetic, no-network fixtures exercise the inactive `ConditionalDecisionClosure` profile over references to already-declared conditional decisions and `PolicyObligationSet` candidates.

| Lane | Expected outcome | Purpose |
|---|---|---|
| `valid/` | `PASS` | Reproduce evidence-backed satisfaction and waiver, plus open, expired, and violated hold states. |
| `schema_invalid/` | `ERROR` | Prove the machine-shape gate fails closed when the non-authority boundary is absent. |
| `semantic_invalid/` | `DENY` | Reject missing closure evidence, missing waiver authority, outcome upgrades, noncanonical ordering, and incomplete blocking summaries. |

A `PASS` does not evaluate policy, issue or enforce an obligation, approve review, authorize promotion or release, publish a candidate, or authorize public use.
