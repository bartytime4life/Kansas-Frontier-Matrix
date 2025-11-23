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
Define the **v11-sensitive-location protection pipeline** used across KFM to generalize or suppress heritage geometries using **dynamic H3 resolution**, **CARE-driven policy checks**, **k-anonymity**, and **FAIR+CARE-aligned provenance**.

</div>

---

# 🌐 Overview  
This standard specifies the **v11 dynamic spatial-generalization engine** for sensitive heritage locations.  
All point or polygon features representing cultural sites, archaeological zones, tribal heritage areas, restricted archives, or community-protected places **must** pass through this pipeline before publication or rendering in the KFM map, timeline, or Story Nodes.

The engine enforces:

- **Adaptive H3 generalization** (sensitivity → coarser hex)  
- **CARE governance** at ingest, staging, and publish-time  
- **k-anonymity** at hex level  
- **Region overrides** (e.g., tribal AOI forcing `res ≤ 3`)  
- **Reproducible hex assignment** (seeded, deterministic)  
- **Full PROV-O lineage** emitted as STAC + DCAT metadata  
- **Focus Mode v3–safe outputs** (no accidental revealing geometries)  

This ensures strong **privacy by design**, **community authority**, and **analytics fidelity**.

---

# 🧩 Inputs & Definitions  

## Required Input Fields  
- `geometry` (Point or Polygon, WGS84)  
- `sensitivity_score` 0–100  
- `authority_tag` (custodial authority or tribal governance marker)  
- Optional: `embargo_until`, `consent_level`, `steward_contact`

## Required Policy Files  
- `policy.yml`  
- `rules/care.yaml`  
- Optional: `rules/overrides.geojson`  

---

# 🔢 Sensitivity → H3 Resolution Mapping  
(Default v11 policy; can be overridden)

| Score Range | H3 Resolution | Notes |
|------------:|--------------:|------|
| 0–10 | 9 | Fine-grain (low-risk) |
| 11–25 | 8 |  |
| 26–40 | 7 |  |
| 41–55 | 6 |  |
| 56–70 | 5 |  |
| 71–85 | 4 | High-risk |
| 86–100 | 3 | Ultra-high-risk (tribal or sacred) |

Rationale: Each step coarsens by ~2–7×, balancing privacy vs. analytical utility.

---

# 🛡️ CARE Screening Rules (v11)  

**1. Collective Benefit**  
- Dataset metadata MUST include `purpose_ref`.  
- Missing purpose → **hard fail**.

**2. Authority to Control**  
- If `authority_tag` present → requires custodial approval token.  
- Failure or absence → fallback to **H3 res ≤ 3** + **embargo**.

**3. Responsibility**  
- Must include steward contact + 24h takedown SLA.  
- Missing → **deny release**.

**4. Ethics**  
- Sacred AOIs: block unless explicit consent token.  
- If allowed → force `res ≤ 4` and drop rare attributes.

---

# 🧪 Validation Gates (CI)  
- Schema conformance  
- Policy checksum integrity  
- Deterministic hexing (seed=1337)  
- **k-anonymity ≥ 7**  
- Distance-to-nearest sensitive site threshold  
- Region override compliance  
- Full CARE audit (pre-publish)

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
(All randomness seeded; no external calls; no Unicode math.)

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

(Truncated here for brevity in spec; code remains identical to approved v11 canonical version.)

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

# 🧱 STAC/DCAT Publication Rules  
Every published layer MUST include:

- STAC Item with:  
  - `privacy:method = "h3_dynamic_res"`  
  - `privacy:policy_ref = <policy.yml SHA256>`  
  - `care:status`, `care:reason_codes`  
  - PROV-O lineage step `"H3DynamicGeneralize v11"`  

---

# 🔍 Audit & Telemetry (v11)  
Emit:  
- Counts by resolution band  
- % dropped by k-anonymity  
- Override hits  
- CARE pass/fail tallies  

Stored under:  
`releases/v11.0.0/standards-telemetry.json → dynamic_h3_generalization`

---

# 🧭 Migration Notes (from v10 fixed-res)  
- Replace `h3_res` → `privacy:h3_res_min` & `privacy:h3_res_actual`  
- Recompute joins  
- Maintain v10 aggregates for 1 release (backward-compat)

---

<div align="center">

[Back to Governance](../../standards/governance/ROOT-GOVERNANCE.md) ·  
[Releases & SBOM](../../../releases/v11.0.0/manifest.zip) ·  
[Telemetry Schema](../../../schemas/telemetry/standards-dynamic-h3-generalization-v11.json)

</div>


