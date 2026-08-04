# Governance validators

`tools/validators/governance/` contains deterministic governance validators and dry-run analysis tools. They check declared shapes and guardrails; they do not create evidence, make policy or review decisions, authorize repository operations, release artifacts, or publish.

## Accepted executables

### `validate_briefing_signal.py`

Validates the proposed non-authoritative `BriefingSignal` `1.1.0` profile, including:

- bounded duplicate-key-safe JSON and closed schema shape;
- evidence references for confirmed claims;
- reproducible signal digest, daily signal ID, event-cluster ID, and issue idempotency key;
- normalized identity tokens;
- unique, duplicate, conflicted, and unresolved routing semantics;
- duplicate issue-creation denial and existing-issue target binding;
- false consequential permissions;
- no inline geometry, secret-like fields, or true trust-bearing states in candidate payloads;
- deterministic no-network, value-free output; and
- discovery-only authority.

### `deduplicate_briefing_signals.py`

Performs a multi-file dry run that:

- groups validated signals by deterministic `event_cluster_id`;
- treats exact repeated inputs as replay rather than new work;
- identifies signal-ID collisions;
- requires later same-cluster signals to reference the primary signal and declare `DUPLICATE`;
- rejects duplicate signals that propose opening parallel issues; and
- emits proposed operations with `authority_created=false` and `repository_mutation_allowed=false`.

Neither tool fetches sources, reads GitHub issues, writes repository state, or validates real-world truth.

## Commands

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/validate_briefing_signal.py \
  examples/briefing_integration/*.json

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/deduplicate_briefing_signals.py \
  fixtures/contracts/v1/governance/briefing_signal/valid/*.json
```

Related:

- `contracts/governance/briefing_signal.md`
- `schemas/contracts/v1/governance/briefing_signal.schema.json`
- `tests/governance/test_briefing_signal.py`
- `tests/governance/test_briefing_signal_dedup.py`
