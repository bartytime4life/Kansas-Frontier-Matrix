<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-ecology-invalid
title: Ecology Invalid Fixtures
type: standard
version: v1
status: active
owners: kfm-data-governance
created: 2026-04-28
updated: 2026-04-28
policy_label: restricted
related: [../README.md, ../valid/README.md, ../policy/README.md, ../../README.md, ../../../README.md]
tags: [kfm, tests, fixtures, ecology, invalid, policy, geoprivacy]
notes: [Negative fixtures for ecology validators; each file is intentionally invalid and should fail a specific gate.]
[/KFM_META_BLOCK_V2] -->

# Ecology Invalid Fixtures

This directory contains **synthetic negative fixtures** used to verify fail-closed behavior for ecology schema and policy checks.

## Fixture inventory

| File | Primary expected failure |
| --- | --- |
| `derived_vegetation_layer.missing_catalog_refs.invalid.json` | Missing `catalog_refs` closure for derived layer payloads. |
| `habitat_assignment.missing_class.invalid.json` | Missing `habitat_class` on derived habitat assignment. |
| `missing_policy_id.invalid.json` | Missing required `policy_id` for publication decisioning. |
| `observation_plot.unknown_rights.invalid.json` | `rights_status` is `unknown` for a publishable observation payload. |
| `sensitive_occurrence_record.public_exact_geometry.invalid.json` | Restricted occurrence includes public exact geometry posture. |
| `taxon_record.missing_spec_hash.invalid.json` | Missing deterministic `spec_hash`. |

## Rules for fixtures in this folder

- Keep fixtures synthetic; never commit real sensitive coordinates or protected site detail.
- Prefer one dominant failure reason per file.
- Name files as `<object>.<failure_reason>.invalid.json`.
- If a fixture is changed, update tests/policy fixtures in the same PR when behavior changes.

## Quick checks

```bash
# List fixtures
find tests/fixtures/ecology/invalid -maxdepth 1 -type f -name '*.json' | sort

# JSON parse sanity
python - <<'PY'
from pathlib import Path
import json
for p in sorted(Path('tests/fixtures/ecology/invalid').glob('*.json')):
    json.loads(p.read_text(encoding='utf-8'))
    print('ok', p)
PY
```

## Expected outcome

These fixtures should produce a failing result (`DENY`, `HOLD`, `ABSTAIN`, or validator `ERROR`) and must never be accepted as public-ready payloads.
