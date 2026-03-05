<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/457ea010-48d8-4f54-a83c-d86f2204f4d4
title: Indigenous Data Protection Standard
type: standard
version: v1
status: draft
owners: ["KFM Governance Council", "KFM Sovereignty Working Group"]
created: 2026-03-05
updated: 2026-03-05
policy_label: restricted
related:
  - ../../governance/ROOT_GOVERNANCE_CHARTER.md
  - ../../quality/SECURITY_BASELINE.md
  - ../../guides/security/00-threat-model.md
tags: [kfm, sovereignty, indigenous-data, policy]
notes:
  - Defines handling rules for culturally sensitive location-linked and narrative data.
[/KFM_META_BLOCK_V2] -->

# Indigenous Data Protection Standard

This standard defines minimum controls for data that may impact Indigenous communities, culturally significant places, and protected knowledge systems.

## Core policy

1. Sensitive Indigenous-context data MUST default to `restricted` policy label.
2. Publish workflows MUST support generalized public derivatives when disclosure is permitted.
3. Precise sacred/cultural location coordinates MUST NOT be exposed in public outputs.
4. Access decisions MUST record rationale and applicable obligations.

## Required obligations

| Obligation ID | Description | Enforced at |
|---|---|---|
| `geom-generalize-h3-r8` | Replace precise geometries with H3 aggregates at resolution 8 | pipeline + API serializer |
| `redact-cultural-markers` | remove place-name fields containing protected terms | transform + response filter |
| `review-tribal-steward` | require explicit steward approval before promotion | CI gate + approval workflow |

## Policy fixture example

```json
{
  "subject": {"role": "public"},
  "resource": {
    "dataset_id": "kfm.cultural_sites.sample",
    "policy_label": "restricted",
    "contains_sensitive_locations": true
  },
  "expected": {
    "decision": "deny",
    "obligations": ["redact-cultural-markers", "geom-generalize-h3-r8"]
  }
}
```

## Example redaction transform (Python)

```python
import pandas as pd

PROTECTED_COLUMNS = {"site_name", "traditional_name", "cultural_notes"}

def redact_sensitive_columns(df: pd.DataFrame) -> pd.DataFrame:
    cols = [c for c in df.columns if c in PROTECTED_COLUMNS]
    out = df.copy()
    for col in cols:
        out[col] = "[REDACTED]"
    return out
```

## Governance requirements

- Maintain a steward-reviewed allowlist for disclosures.
- Log every promotion waiver with review metadata and expiration.
- Include sovereign-data checks in incident drills and rollback tests.

