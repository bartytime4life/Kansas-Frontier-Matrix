---
title: "🛡️ KFM v11 — Dynamic H3 Generalization & Automated CARE Screening (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/standards/heritage/dynamic-h3-generalization.md"
version: "v11.0.1"
last_updated: "2025-11-23"
review_cycle: "Annual · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-dynamic-h3-generalization-v11.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
doc_kind: "Standard"
semantic_document_id: "kfm-standard-dynamic-h3-generalization-v11"
doc_uuid: "urn:kfm:docs:standards:heritage:dynamic-h3-generalization:v11.0.1"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Protected-Geo · Conditional Disclosure"
immutability_status: "version-pinned"
intent: "heritage-protection"
---

<div align="center">

# 🛡️ **Dynamic H3 Generalization & Automated CARE Screening**  
`docs/standards/heritage/dynamic-h3-generalization.md`

**Purpose:**  
Define the **v11-sensitive-location protection pipeline** for generalizing or suppressing heritage geometries using dynamic H3 resolution, CARE screening, k-anonymity, region overrides, and FAIR+CARE provenance.

</div>

---

# 🌐 Overview
This standard specifies the **v11 dynamic spatial-generalization engine** for sensitive heritage locations. All point/polygon features representing cultural-heritage, archaeological, tribal, restricted, or community-protected sites **must** pass through this pipeline before publication.

Engine guarantees:

- Adaptive H3 generalization (sensitivity → coarser hex)  
- Automatic CARE enforcement  
- k-anonymity ≥ 7  
- Region overrides (tribal AOI forcing res ≤ 3)  
- Deterministic, seeded assignment  
- PROV-O lineage emissions via STAC/DCAT  
- Focus Mode v3 safe-display constraints  

---

# 🧩 Inputs & Definitions

## Required Input Fields
- `geometry` (Point/Polygon, WGS84)  
- `sensitivity_score` (0–100)  
- `authority_tag`  
- Optional: `embargo_until`, `consent_level`, `steward_contact`

## Required Policy Files
- `policy.yml`  
- `rules/care.yaml`  
- Optional: `rules/overrides.geojson`  

---

# 🔢 Sensitivity → H3 Resolution Mapping (v11 default)

| Score Range | H3 Resolution |
|------------:|--------------:|
| 0–10  | 9 |
| 11–25 | 8 |
| 26–40 | 7 |
| 41–55 | 6 |
| 56–70 | 5 |
| 71–85 | 4 |
| 86–100 | 3 |

---

# 🛡️ CARE Screening Rules (v11)

## Collective Benefit
- Dataset MUST include `purpose_ref`.  
- Missing → **CARE_FAIL**.

## Authority to Control
- If `authority_tag`: custodial approval token required.  
- Missing/invalid → force `res ≤ 3` + embargo.

## Responsibility
- Must include steward contact + takedown SLA.  
- Missing → **block release**.

## Ethics
- Sacred AOIs: blocked unless explicit community consent.  
- If allowed → force `res ≤ 4` + drop rare attributes.

---

# 🧪 Validation Gates (CI)
- Schema + policy checksum  
- Deterministic hexing (seed=1337)  
- k-anonymity ≥ 7  
- Distance-based privacy check  
- Region override enforcement  
- CARE audit (pre-publish)

---

# 🧱 Directory Layout
```text
docs/standards/heritage/dynamic-h3-generalization.md
src/pipelines/privacy/h3_dynamic/
    policy.yml
    rules/
        care.yaml
        overrides.geojson
    scripts/
        h3_dynamic_generalize.py
        care_screen.py
    tests/
        test_policy.py
        test_k_anonymity.py
data/work/privacy/h3_dynamic/
    input/
    output/
    logs/
```

---

# ⚙️ Reference Policy (`policy.yml`)
```yaml
score_bands:
  - {min: 0,   max: 10,  h3_res: 9}
  - {min: 11,  max: 25,  h3_res: 8}
  - {min: 26,  max: 40,  h3_res: 7}
  - {min: 41,  max: 55,  h3_res: 6}
  - {min: 56,  max: 70,  h3_res: 5}
  - {min: 71,  max: 85,  h3_res: 4}
  - {min: 86,  max: 100, h3_res: 3}
k_min: 7
min_hex_res_global: 3
region_overrides:
  - {aoi_ref: "tribal_sacred_sites", min_res: 3, force: true}
  - {aoi_ref: "urban_core_analytics", min_res: 6, force: false}
attributes_bucket:
  year: decade
  value: quantile4
consent_required: ["authority_tag", "sacred_flag"]
embargo_default_days: 365
```

---

# 🧩 Deterministic Python (v11-safe)
```python
# File: src/pipelines/privacy/h3_dynamic/scripts/h3_dynamic_generalize.py
import json, os, math, hashlib, random
from datetime import datetime, timezone
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import h3

SEED = 1337
random.seed(SEED)
...
```

---

# 🧪 CARE Rule Executor
```python
# File: src/pipelines/privacy/h3_dynamic/scripts/care_screen.py
import yaml, json, sys, datetime
...
```

---

# 🧷 CI/CD Integration
```Makefile
privacy-h3:
    python src/pipelines/privacy/h3_dynamic/scripts/care_screen.py collections/heritage.yml src/pipelines/privacy/h3_dynamic/rules/care.yaml
    python src/pipelines/privacy/h3_dynamic/scripts/h3_dynamic_generalize.py \
      --in data/work/privacy/h3_dynamic/input/observations.geojson \
      --policy src/pipelines/privacy/h3_dynamic/policy.yml \
      --overrides src/pipelines/privacy/h3_dynamic/rules/overrides.geojson \
      --out data/work/privacy/h3_dynamic/output/observations_h3.geojson
```

---

# 🧱 STAC/DCAT Publication Requirements
- Publish only **H3 centroids** + aggregated attributes  
- Must include:  
  - `privacy:method = "h3_dynamic_res"`  
  - `privacy:policy_ref = <SHA256(policy.yml)>`  
  - `care:status`, `care:reason_codes`  
  - PROV-O lineage step `"H3DynamicGeneralize v11"`  

---

# 🔍 Audit & Telemetry
Emit metrics:  
- Counts by H3 band  
- % dropped via k-anonymity  
- Region override hits  
- CARE pass/fail tally  

Stored at:  
`releases/v11.0.0/standards-telemetry.json → dynamic_h3_generalization`

---

# 🧭 Migration Notes (from v10 fixed-res)
- Replace static `h3_res` with `privacy:h3_res_min` + `privacy:h3_res_actual`  
- Recompute joins  
- Maintain backward-compatibility aggregates for one release  

---

[Back to Governance](../../standards/governance/ROOT-GOVERNANCE.md) · [Releases & SBOM](../../../releases/v11.0.0/manifest.zip) · [Telemetry Schema](../../../schemas/telemetry/standards-dynamic-h3-generalization-v11.json)
