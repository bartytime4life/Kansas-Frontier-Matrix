# Evidence resolver validator

Repository-facing CLI wrapper for the package-local v1alpha1 evidence candidate
check. It inherits validator authority limits from
[`tools/validators/`](../README.md).

## Boundary contract

- Purpose: run one explicit input or the synthetic fixture suite.
- Owner: evidence/proof and validation stewards — `OWNER_TBD`.
- Input: bounded JSON matching the internal candidate profile.
- Output: deterministic JSON for one input, or pass/fail fixture summaries.
- Exit codes: `0 RESOLVED`, `2 UNRESOLVED`, `3 DENIED`, `4 ERROR`;
  fixture mode returns `0` only when all selected expectations match.
- Prohibited: registry/network/store access, evidence creation, policy
  evaluation, review/release action, public response generation, or publishing.
- Exposure/retention: local/CI diagnostic only; nothing is persisted.
- Rollback: revert the validator with its package, fixture, test, Make, and
  workflow surfaces.

```text
tools/validators/evidence_resolver/
├── README.md
└── validate_candidate.py
```

Run through `make evidence-resolver` or `make evidence-resolver-deny`. A pass
means only that the declared internal fixture expectations matched.
