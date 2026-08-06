# Governance validators

`tools/validators/governance/` contains deterministic governance validators and
dry-run analysis tools. They do not create evidence, make policy or review
decisions, authorize repository operations, release artifacts, or publish.

## BriefingSignal executables

### `validate_briefing_signal.py`

Validates the proposed non-authoritative `1.2.0` profile:

- bounded duplicate-key-safe JSON and closed schema shape;
- evidence references for confirmed claims;
- reproducible signal digest, daily ID, cluster ID, and issue idempotency key;
- exact materiality formula, thresholds, reason codes, and override consistency;
- exact finite routing precedence and reasons;
- duplicate issue-creation denial and declared existing-issue target shape;
- false consequential permissions;
- no inline geometry, secret-like fields, or true trust-bearing states; and
- deterministic no-network, value-minimized output.

### `deduplicate_briefing_signals.py`

Groups validated signals by event cluster, counts replay, detects collisions,
requires primary references, rejects duplicate issue creation, and emits dry-run
operations only.

### `validate_issue_inventory_projection.py`

Validates the read-only
`kfm.briefing.issue-inventory.fixture.v1` projection:

- closed, bounded, duplicate-key-safe JSON;
- sorted unique issue numbers with `OPEN` or `CLOSED` state only;
- canonical UTC-second generation and update times;
- issue-count closure;
- canonical SHA-256 digest and derived projection ID;
- fixed false live-state, authority, and mutation flags; and
- deterministic value-minimized findings.

The projection is synthetic local fixture state, not a live GitHub read or a
repository authorization record.

### `route_briefing_signals.py`

Recomputes materiality and declared routing for multiple local signals. With
`--issue-inventory`, it binds a declared `UPDATE_EXISTING_ISSUE` route to
exactly one open projected target. Missing, closed, absent-inventory, or
ambiguous targets become `HOLD_FOR_DEPENDENCY`. The report contains only IDs,
scores, priorities, finite reasons, proposed dispositions, idempotency keys, and
value-minimized issue-state metadata.

It always reports `authority_created=false` and
`repository_mutation_allowed=false`.

## Commands

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/validate_briefing_signal.py \
  examples/briefing_integration/*.json

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/validate_issue_inventory_projection.py \
  fixtures/contracts/v1/governance/issue_inventory_projection/valid/*.json

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/route_briefing_signals.py \
  --issue-inventory \
  fixtures/contracts/v1/governance/issue_inventory_projection/valid/open-target.json \
  fixtures/contracts/v1/governance/briefing_signal/valid/*.json \
  examples/briefing_integration/*.json
```

None of these tools fetches sources, reads live GitHub state, writes GitHub
issues, activates policy, or validates real-world truth.
