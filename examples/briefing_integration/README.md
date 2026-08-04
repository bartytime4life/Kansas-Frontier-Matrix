# Briefing integration examples

`examples/briefing_integration/` contains proposed, non-authoritative worked examples. They show deterministic identity, explainable materiality, and existing-issue-first routing without becoming evidence, source admission, repository authority, lifecycle records, release approval, or public truth.

| File | Computed profile | Demonstrates | Boundary |
|---|---|---|---|
| `hays_water_local_consult_2026_07_29.json` | score `26`; `P2`; `UPDATE_EXISTING_ISSUE` | Source-announced meeting candidate linked to issue #1647 | Schedule is supported; occurrence, attendance, submissions, decisions, and geometries remain unresolved. |
| `gmd_action_plan_inventory_2026_07_29.json` | score `37`; `P1`; `UPDATE_EXISTING_ISSUE` | Authority-index observation linked to issue #1647 | Link presence does not prove submission acceptance, review, approval, implementation, or outcome. |

Both records declare `DUPLICATE` because existing issue #1647 already owns the bounded follow-up. Existing-issue precedence produces `UPDATE_EXISTING_ISSUE` regardless of later new-work routing context. No issue mutation occurs.

```bash
python tools/validators/governance/validate_briefing_signal.py \
  examples/briefing_integration/*.json

python tools/validators/governance/route_briefing_signals.py \
  examples/briefing_integration/*.json
```

The examples remain non-authoritative even when validation passes.
