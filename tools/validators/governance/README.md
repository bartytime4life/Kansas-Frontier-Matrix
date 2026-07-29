# Governance validators

`tools/validators/governance/`

Status: proposed executable validation lane.

This lane contains deterministic governance validators. Validators check declared shapes and guardrails; they do not create evidence, make policy or review decisions, authorize repository operations, release artifacts, or publish.

## Accepted executable

`validate_briefing_signal.py` validates the non-authoritative `BriefingSignal` profile.

It proves only:

- schema and JSON shape;
- evidence references for confirmed claims;
- false consequential permissions;
- no inline geometry in candidate payloads;
- deterministic no-network output; and
- discovery-only authority.

It does not fetch sources or validate real-world truth.

## Command

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1   python tools/validators/governance/validate_briefing_signal.py   examples/briefing_integration/*.json
```

Related:

- `contracts/governance/briefing_signal.md`
- `schemas/contracts/v1/governance/briefing_signal.schema.json`
- `tests/governance/test_briefing_signal.py`
