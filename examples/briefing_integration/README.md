# Briefing integration examples

`examples/briefing_integration/`

Status: proposed, non-authoritative worked examples.

This lane demonstrates how a daily KFM briefing story becomes a `BriefingSignal` without becoming evidence, source admission, repository authority, a lifecycle record, release approval, or public truth.

## Current examples

| File | Demonstrates | Required boundary |
|---|---|---|
| `hays_water_local_consult_2026_07_29.json` | Source-announced `PublicMeeting` candidate | Schedule confirmed; occurrence, attendance, submissions, recommendations, decisions, and geometries unresolved. |
| `gmd_action_plan_inventory_2026_07_29.json` | Versioned authority-index observation | Link presence does not prove submission acceptance, review, approval, implementation, or outcome. |

## Validation

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1   python tools/validators/governance/validate_briefing_signal.py   examples/briefing_integration/*.json

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1   python -m unittest discover   --start-directory tests/governance   --pattern 'test_briefing_signal.py'   --verbose
```

## Exclusions

No credentials, authenticated portal content, personal submissions, attendee data, inline coordinates, source payloads, EvidenceBundles, PolicyDecisions, proof objects, release objects, public routes, or published artifacts belong here.

## Authority

The owning semantic and machine surfaces are:

- `contracts/governance/briefing_signal.md`
- `schemas/contracts/v1/governance/briefing_signal.schema.json`
- `tools/validators/governance/validate_briefing_signal.py`

The examples remain non-authoritative even when validation passes.
