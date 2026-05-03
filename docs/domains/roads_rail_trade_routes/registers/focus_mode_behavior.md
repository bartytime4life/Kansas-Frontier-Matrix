# Focus Mode Behavior

Behavior contract for bounded synthesis in this lane.

## Allowed outcomes
- `ANSWER`: evidence-closed and policy-allowed.
- `ABSTAIN`: insufficient/conflicting evidence.
- `DENY`: policy/rules prohibit disclosure or claim.
- `ERROR`: runtime failure path.

## Requirements
- No direct raw-store access.
- Include evidence refs and reason codes in responses.
