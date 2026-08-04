# Governance validators

`tools/validators/governance/` contains deterministic governance validators and dry-run analysis tools. They do not create evidence, make policy or review decisions, authorize repository operations, release artifacts, or publish.

## BriefingSignal executables

### `validate_briefing_signal.py`

Validates the proposed non-authoritative `1.2.0` profile:

- bounded duplicate-key-safe JSON and closed schema shape;
- evidence references for confirmed claims;
- reproducible signal digest, daily ID, cluster ID, and issue idempotency key;
- exact materiality formula, thresholds, reason codes, and override consistency;
- exact finite routing precedence and reasons;
- duplicate issue-creation denial and existing-issue target binding;
- false consequential permissions;
- no inline geometry, secret-like fields, or true trust-bearing states; and
- deterministic no-network, value-minimized output.

### `deduplicate_briefing_signals.py`

Groups validated signals by event cluster, counts replay, detects collisions, requires primary references, rejects duplicate issue creation, and emits dry-run operations only.

### `route_briefing_signals.py`

Recomputes materiality and routing for multiple local signals and emits only IDs, scores, priorities, finite reasons, proposed dispositions, idempotency keys, and issue targets. It always reports `authority_created=false` and `repository_mutation_allowed=false`.

## Commands

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/validate_briefing_signal.py \
  examples/briefing_integration/*.json

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/route_briefing_signals.py \
  fixtures/contracts/v1/governance/briefing_signal/valid/*.json \
  examples/briefing_integration/*.json
```

Neither tool family fetches sources, reads or writes GitHub issues, activates policy, or validates real-world truth.
