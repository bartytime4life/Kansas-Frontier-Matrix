---
title: "🛡️ KFM v11 — Dynamic H3 Generalization & Automated CARE Screening (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/standards/heritage/dynamic-h3-generalization.md"
version: "v11.0.3"
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
doc_uuid: "urn:kfm:docs:standards:heritage:dynamic-h3-generalization:v11.0.3"
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
Define and enforce the v11 dynamic spatial-generalization and CARE-screening pipeline that protects sensitive heritage geographies while preserving analytical utility.

</div>

---

# 🌐 Overview

This standard governs how **sensitive heritage locations** (tribal sites, sacred places, archaeological features, community-protected areas, restricted archives) are handled before they are:

- displayed in **MapLibre/Cesium**  
- surfaced in **Focus Mode v3**  
- attached to **Story Nodes v3**  
- exported via **STAC/DCAT** datasets  

It mandates:

- **Dynamic H3 generalization** driven by a `sensitivity_score`  
- **Automated CARE screening** (Collective Benefit, Authority to Control, Responsibility, Ethics)  
- **k-anonymity** at H3 cell level (`k_min` ≥ 7 by default)  
- **Region overrides** for tribal AOIs, urban cores, and other special policies  
- **Deterministic, seeded** H3 assignment for reproducibility  
- **PROV-O lineage** and STAC/DCAT metadata for all published outputs  

Any geometry that fails CARE or privacy checks **MUST NOT** be published to public maps, Focus Mode, or Story Nodes.

---

# 🧩 Inputs & Definitions

## 1. Feature Inputs

Each input feature MUST provide:

- `geometry`: Point or Polygon in WGS84 (EPSG:4326)  
- `sensitivity_score`: integer in `[0, 100]`  
- `authority_tag`: string indicating custodial authority (e.g. tribal council, archive steward)  

Optional fields:

- `embargo_until`: date or datetime (ISO 8601) after which less-coarse publication is allowed  
- `consent_level`: enum (e.g. `none`, `implicit`, `explicit`)  
- `steward_contact`: email or URI for takedown / inquiry  
- `sacred_flag`: boolean (true if sacred or highly sensitive)  

## 2. Policy & Configuration Inputs

Required files:

- `policy.yml` — H3 mapping, k-anonymity, bucketing, region overrides  
- `rules/care.yaml` — CARE policy, consent rules, takedown SLA config  
- Optional: `rules/overrides.geojson` — AOIs that enforce minimum H3 resolution or forced overrides  

---

# 🔢 Sensitivity → H3 Resolution Mapping (Default v11 Policy)

The default mapping in `policy.yml` is:

| Score Range | H3 Resolution | Notes |
|------------:|--------------:|------|
| 0–10  | 9 | Low sensitivity, fine-grain allowed |
| 11–25 | 8 |  |
| 26–40 | 7 |  |
| 41–55 | 6 |  |
| 56–70 | 5 |  |
| 71–85 | 4 | High sensitivity |
| 86–100 | 3 | Ultra-sensitive; tribal or sacred |

Each step coarsens spatial precision by ~2–7× area, reducing re-identification risk while maintaining useful aggregation.

---

# 🛡️ CARE Screening Rules (v11)

CARE screening runs as a **pre-publish gate**. If it fails, the pipeline MUST NOT emit public assets.

## 1. Collective Benefit

- Dataset-level metadata MUST declare a `purpose_ref`.  
- Missing, vague, or exploitative purpose → `CARE_FAIL_COLLECTIVE_BENEFIT`.  
- Examples: “tribal-tourism marketing without consent” → block; “heritage conservation planning” → allowed.

## 2. Authority to Control

- If `authority_tag` is present, a valid `consent.community_token` or equivalent approval MUST exist.  
- If not present or invalid, the engine either:
  - forces `h3_res` to **3** (coarsest), or  
  - applies full embargo (`embargo_until`), depending on `care.yaml`.  

## 3. Responsibility

- Collection metadata MUST include `contacts.steward.email` and takedown SLA.  
- If missing, the dataset is rejected: `CARE_FAIL_RESPONSIBILITY`.  
- Takedown flows MUST be documented and accessible to communities.

## 4. Ethics

- Features intersecting **sacred AOIs** are blocked by default unless `care.yaml` authorizes limited publication.  
- If allowed, they MUST:
  - use `h3_res ≤ 4`  
  - drop rare or re-identifying attributes  
  - be flagged with explicit CARE reason codes  

---

# 🧪 Validation Gates (CI & Pipelines)

Before any dataset is published or promoted:

1. **Schema validation**  
   - Required columns present: `geometry`, `sensitivity_score`, `authority_tag`  
   - Types and ranges checked.

2. **Policy integrity**  
   - `policy.yml` checksum recorded; change requires governance review.

3. **Deterministic H3 assignment**  
   - H3 calculation uses a fixed `SEED = 1337`.  
   - Re-running with same inputs produces identical outputs.

4. **k-anonymity**  
   - For each H3 cell, after attribute bucketing: `count ≥ k_min` (default 7).  
   - Cells below threshold are dropped or merged further up.

5. **Distance-based privacy**  
   - Minimum distance to any unpublished, highly sensitive feature enforced (configurable).

6. **Region overrides**  
   - All AOIs in `overrides.geojson` are applied with their `min_res` and `force` flags.

7. **CARE audit**  
   - CARE rule engine (`care_screen.py`) must return `CARE_OK`.  
   - Any `CARE_FAIL_*` status blocks publication and logs the reason.

---

# 🗂 Directory Layout (v11 Tree with Comments)

```text
Kansas-Frontier-Matrix/
│
├── docs/                               # Documentation root
│   └── standards/                      # Standards and governance docs
│       └── heritage/                   # Heritage-focused standards
│           └── dynamic-h3-generalization.md   # This H3 generalization standard
│
├── src/                                # Source code (ETL, pipelines, services)
│   └── pipelines/                      # Data and privacy pipelines
│       └── privacy/                    # Privacy-preserving processing
│           └── h3_dynamic/             # Dynamic H3 generalization pipeline
│               ├── policy.yml          # Score→H3 mapping and k-anonymity policy
│               ├── rules/              # CARE and AOI override rules
│               │   ├── care.yaml       # CARE screening configuration
│               │   └── overrides.geojson   # Spatial overrides (tribal AOIs, urban cores)
│               ├── scripts/            # Executable pipeline scripts
│               │   ├── h3_dynamic_generalize.py   # Main H3 generalization engine
│               │   └── care_screen.py  # CARE pre-publish gate script
│               └── tests/              # Unit and integration tests for this pipeline
│                   ├── test_policy.py  # Policy parsing and score→res mapping tests
│                   └── test_k_anonymity.py   # k-anonymity enforcement tests
│
└── data/                               # Data workspaces
    └── work/                           # Staging/work directories
        └── privacy/                    # Privacy pipeline workspaces
            └── h3_dynamic/             # Dynamic H3 workspace
                ├── input/              # Raw heritage observations (pre-H3)
                ├── output/             # H3-aggregated outputs (for staging)
                └── logs/               # Run logs and CARE audit traces
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
  - aoi_ref: "tribal_sacred_sites"
    min_res: 3
    force: true
  - aoi_ref: "urban_core_analytics"
    min_res: 6
    force: false
attributes_bucket:
  year: decade        # bucket years to decades (e.g. 1990s)
  value: quantile4    # 4-bin quantiles for continuous attributes
consent_required:
  - authority_tag
  - sacred_flag
embargo_default_days: 365
```

---

# 🧩 Deterministic H3 Generalization (Python Excerpt)

```python
# File: src/pipelines/privacy/h3_dynamic/scripts/h3_dynamic_generalize.py
import os, random
import geopandas as gpd
from shapely.geometry import Point
import h3

SEED = 1337
random.seed(SEED)

def load_policy(fp):
    import yaml
    with open(fp, "r") as f:
        return yaml.safe_load(f)

def score_to_res(score, bands, fallback_res=3):
    for band in bands:
        if band["min"] <= score <= band["max"]:
            return int(band["h3_res"])
    return int(fallback_res)

def assign_h3_row(row, bands, min_global):
    s = max(0, min(100, float(row.get("sensitivity_score", 100))))
    res = max(min_global, score_to_res(s, bands))
    lon, lat = row.geometry.x, row.geometry.y
    return h3.geo_to_h3(lat, lon, res)

# Additional logic: region overrides, bucketing, grouping, k-anonymity, output saving
```

Implementation note: the **full script** in the repo MUST match the v11 canonical implementation and be covered by tests.

---

# 🧪 CARE Rule Executor (Python Excerpt)

```python
# File: src/pipelines/privacy/h3_dynamic/scripts/care_screen.py
import yaml, sys

def load(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def ensure(meta, path, msg):
    node = meta
    for key in path.split("."):
        node = node.get(key, {}) if isinstance(node, dict) else None
    if not node:
        raise SystemExit("CARE_FAIL: %s" % msg)

def main(meta_fp, rules_fp):
    meta = load(meta_fp)
    rules = load(rules_fp)

    ensure(meta, "dataset.purpose_ref", "Missing purpose_ref (Collective Benefit).")
    ensure(meta, "contacts.steward.email", "Missing steward contact (Responsibility).")

    if meta.get("dataset", {}).get("sacred_flag", False):
        ensure(meta, "consent.community_token", "Missing community consent (Authority to Control).")

    if rules.get("ethics", {}).get("block_sacred_aoi", True) and meta.get("dataset", {}).get("in_sacred_aoi", False):
        raise SystemExit("CARE_FAIL: Sacred AOI blocked by policy.")

    print("CARE_OK")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit("Usage: care_screen.py <collection_meta.yml> <rules.yml>")
    main(sys.argv[1], sys.argv[2])
```

---

# 🧷 CI/CD Integration

```Makefile
privacy-h3:
	python src/pipelines/privacy/h3_dynamic/scripts/care_screen.py \
	    collections/heritage.yml \
	    src/pipelines/privacy/h3_dynamic/rules/care.yaml
	python src/pipelines/privacy/h3_dynamic/scripts/h3_dynamic_generalize.py \
	    --in data/work/privacy/h3_dynamic/input/observations.geojson \
	    --policy src/pipelines/privacy/h3_dynamic/policy.yml \
	    --overrides src/pipelines/privacy/h3_dynamic/rules/overrides.geojson \
	    --out data/work/privacy/h3_dynamic/output/observations_h3.geojson
```

- This target MUST run on every dataset promotion.  
- CI MUST fail if either script exits non-zero.

---

# 🧱 STAC/DCAT Publication Rules

Every published generalized dataset MUST:

- Register as a **STAC Collection + Items** in `data/stac/`  
- Include for each STAC Item:
  - `properties["privacy:method"] = "h3_dynamic_res"`
  - `properties["privacy:policy_ref"] = "<SHA256(policy.yml)>"`
  - `properties["care:status"]` and `properties["care:reason_codes"]`
  - GeoJSON centroid geometry and `bbox`  
- Record PROV-O lineage:
  - `prov:wasGeneratedBy = "H3DynamicGeneralize v11"`

These records allow Focus Mode v3, Story Nodes, and external consumers to reason about privacy guarantees and provenance.

---

# 🔍 Telemetry & Audit

For each run, the pipeline MUST emit telemetry fields including:

- `total_features_in`  
- `total_features_out`  
- counts by H3 resolution band  
- `dropped_for_k_anonymity`  
- `override_hits` (by AOI)  
- CARE statuses (OK vs each CARE_FAIL code)

All telemetry is appended or merged into:

- `releases/v11.0.0/standards-telemetry.json` under key `dynamic_h3_generalization`

---

# 🧭 Migration Notes (from Fixed-Resolution H3)

Older v10 datasets using a fixed `h3_res` MUST be migrated as follows:

1. Introduce `privacy:h3_res_min` and `privacy:h3_res_actual`.  
2. Recompute aggregates using the dynamic mapping, maintaining old aggregates for at least one release.  
3. Update joins and analytics queries to use `privacy:h3_res_actual`.  
4. Annotate migrated datasets with `migration:from = "h3_res_v10_fixed"`.

---

# 🕰 Version History

| Version  | Date       | Changes                                                                                 |
|---------:|-----------:|-----------------------------------------------------------------------------------------|
| v11.0.3  | 2025-11-23 | Directory layout updated with connectors and comments; clarified v11 tree requirements. |
| v11.0.2  | 2025-11-23 | Added Version History section; kept v11 metadata and corrected footer.                  |
| v11.0.1  | 2025-11-23 | Footer formatting aligned with MDP v11; removed trailing fence annotations.            |
| v11.0.0  | 2025-11-23 | Initial v11 release of Dynamic H3 + CARE standard with deterministic pipeline.         |

---

[Back to Governance](../../standards/governance/ROOT-GOVERNANCE.md) · [Releases & SBOM](../../../releases/v11.0.0/manifest.zip) · [Telemetry Schema](../../../schemas/telemetry/standards-dynamic-h3-generalization-v11.json)
