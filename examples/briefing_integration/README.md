# Briefing integration examples

`examples/briefing_integration/` contains proposed, non-authoritative worked examples. They demonstrate how briefing stories become deterministically identified `BriefingSignal` records without becoming evidence, source admission, repository authority, lifecycle records, release approval, or public truth.

## Current examples

| File | Demonstrates | Required boundary |
|---|---|---|
| `hays_water_local_consult_2026_07_29.json` | Source-announced `PublicMeeting` candidate linked to existing issue #1647 | Schedule confirmed; occurrence, attendance, submissions, recommendations, decisions, and geometries unresolved. |
| `gmd_action_plan_inventory_2026_07_29.json` | Versioned authority-index observation linked to issue #1647 | Link presence does not prove submission acceptance, review, approval, implementation, or outcome. |

Both records declare `DUPLICATE` routing because existing issue #1647 already owns the bounded follow-up. Their idempotency keys reproduce, so a future projector can update rather than open parallel work. No issue mutation occurs in this repository slice.

## Validation

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/governance/validate_briefing_signal.py \
  examples/briefing_integration/*.json

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest discover \
  --start-directory tests/governance \
  --pattern 'test_briefing_signal*.py' \
  --verbose
```

## Exclusions

No credentials, authenticated portal content, personal submissions, attendee data, inline coordinates, source payloads, EvidenceBundles, PolicyDecisions, proof objects, release objects, public routes, or published artifacts belong here.

The examples remain non-authoritative even when validation passes.
