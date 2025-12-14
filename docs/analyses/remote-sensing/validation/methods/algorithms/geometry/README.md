---
title: "📐 KFM — Geometry Validation Algorithms (CRS · Footprints · Tiling · Alignment)"
path: "docs/analyses/remote-sensing/validation/methods/algorithms/geometry/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Reference"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "remote-sensing-validation-algorithms-geometry"
audience:
  - "Remote Sensing Engineering"
  - "Science QA Reviewers"
  - "Data Engineering"
  - "Reliability Engineering"
  - "Governance Reviewers"

classification: "Public"
sensitivity: "General (non-sensitive) unless overridden by dataset labels"
sensitivity_level: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Remote Sensing Board · FAIR+CARE Council"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:algorithms:geometry:index:v11.2.6"
semantic_document_id: "kfm-rs-validation-algorithms-geometry"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/algorithms/geometry/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "diagram-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 📐 **KFM — Geometry Validation Algorithms**
`docs/analyses/remote-sensing/validation/methods/algorithms/geometry/README.md`

**Purpose**  
Governed metric set and deterministic computation rules for validating **geospatial integrity**
of remote-sensing outputs in KFM: CRS correctness, footprint validity, tiling consistency, and alignment sanity checks.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Validation-Geometry-blue" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Geometry validation algorithms detect and prevent:

- CRS or axis-order mistakes,
- invalid geometries (self-intersections, rings, null geometries),
- inconsistent tiling (gaps/overlaps beyond policy),
- pixel-grid/resolution drift,
- AOI coverage drift,
- unexpected spatial shifts (georegistration drift proxies),
- projection/transform metadata omissions.

These checks are designed to support:

- per-run QA bundles,
- daily rollups,
- release promotion gates (SemVer-aligned drift control).

Geometry validation MUST remain governance-safe: avoid leaking sensitive locations through overly specific reporting.

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/algorithms/     — Algorithm docs
└── 📁 geometry/                                                  — Geometry validation (this directory)
    ├── 📄 README.md                                              — This reference
    └── 📁 templates/                                             — Optional: payload templates/schemas
~~~

---

## 🧾 Inputs (conceptual)

Geometry validation can operate on any artifact set with spatial metadata, commonly:

- STAC Items and Assets (raster tiles, vectors, GeoParquet),
- projection metadata (e.g., CRS, transform, shape, GSD/resolution),
- item `geometry` and `bbox`,
- optional AOI boundary (generalized where required by policy),
- baseline artifact set (previous run or previous release) for drift checks.

Minimum required metadata per item:

- stable `id`,
- `bbox` and/or `geometry`,
- CRS (explicitly declared, not inferred),
- asset list (keys stable and enumerable).

---

## ✅ Core checks (recommended)

### 1) CRS presence and consistency

Goals:

- CRS must be present and interpretable.
- CRS must match expected product rules (policy-configured).
- CRS must be consistent across items in the same product family, unless explicitly allowed.

Outputs:

- `crs_missing_count`
- `crs_mismatch_count`
- `crs_changed_vs_baseline` (boolean)
- `axis_order_anomaly_count` (when detectable)

### 2) Footprint validity

Validate that item geometries are:

- non-null,
- valid polygons,
- non-empty,
- within allowed region bounds (generalized test),
- have sane area ranges (policy-configurable, aggregated only).

Outputs:

- `invalid_geometry_count`
- `empty_geometry_count`
- `area_outlier_count` (aggregated only)

### 3) Bounding box sanity

Check:

- bbox min ≤ max for each axis,
- bbox intersects expected region bounds (generalized),
- bbox area is within expected range.

Outputs:

- `bbox_invalid_count`
- `bbox_out_of_bounds_count` (generalized)

### 4) Tiling consistency (gaps/overlaps)

For tiled rasters/vectors:

- enumerate tile footprints deterministically,
- compute overlap rate and gap rate (aggregated),
- detect duplicate tiles (same footprint + same timestamp) when disallowed.

Outputs:

- `tile_overlap_rate_pct`
- `tile_gap_rate_pct`
- `duplicate_tile_count`

### 5) Pixel grid and resolution sanity (rasters)

Validate expected pixel characteristics:

- resolution (GSD) matches expected within tolerance,
- width/height shape consistency for a given tile scheme,
- transform metadata present (when required),
- nodata presence and policy consistency (if included in geometry checks).

Outputs:

- `gsd_expected_m` (policy)
- `gsd_observed_median_m`
- `gsd_drift_pct_p50`
- `transform_missing_count`

### 6) Alignment drift proxies (baseline comparison)

Where a baseline exists, compute aggregated alignment drift proxies such as:

- centroid shift (aggregated; generalize if needed),
- bbox delta stats,
- coarse H3 coverage delta counts (counts only under policy).

Outputs:

- `centroid_shift_m_p50` (or null if not allowed)
- `coverage_area_delta_pct` (generalized)
- `coarse_cells_delta` (counts only)

---

## 🧪 Determinism requirements (non-negotiable)

Geometry validation MUST be reproducible:

- stable enumeration and sorting:
  - item ids sorted
  - asset keys sorted
  - tile ids sorted (if used)
- fixed tolerances pinned in config:
  - bbox bounds tolerances
  - overlap/gap thresholds
  - GSD drift tolerances
- fixed numeric behavior:
  - explicit distance metric choice (geodesic vs projected) recorded
  - explicit rounding rules (if any) recorded
- baseline selection deterministic:
  - previous run resolved by stable ordering rules
  - previous release resolved by SemVer (or governed ledger order)
- sampling (if used) must be deterministic:
  - fixed seed recorded
  - deterministic sample frame hash

Fail-closed posture:

- if required metadata is missing (e.g., CRS required by policy), mark outcome `fail`.

---

## 🚦 Thresholds and gate outcomes (policy-driven)

Geometry thresholds are product- and stage-dependent. Common policies include:

- `crs_missing_count_max = 0` (critical)
- `invalid_geometry_count_max = 0` (critical)
- `tile_overlap_rate_pct_max` (warn/fail depending on product)
- `tile_gap_rate_pct_max` (warn/fail depending on product)
- `gsd_drift_pct_p50_max` (warn/fail depending on product)
- `bbox_out_of_bounds_count_max = 0` (critical in most cases)

Outcome:

- `pass`: within thresholds
- `warn`: non-critical threshold breached or low-confidence due to partial scope
- `fail`: critical threshold breached (promotion blocked)

---

## 🧾 Normalized reason codes (recommended)

| Reason code | Typical trigger | Default severity |
|---|---|---|
| `CRS_MISSING` | CRS required but absent | fail |
| `CRS_MISMATCH` | CRS differs from expected policy | fail |
| `CRS_CHANGED` | CRS changed vs baseline | fail |
| `FOOTPRINT_INVALID` | geometry invalid or null | fail |
| `BBOX_INVALID` | bbox malformed | fail |
| `BBOX_OUT_OF_RANGE` | bbox outside expected region bounds (generalized) | fail |
| `TILE_OVERLAP_EXCESS` | overlap rate > policy | warn/fail |
| `TILE_GAP_EXCESS` | gap rate > policy | warn/fail |
| `RESOLUTION_DRIFT` | GSD drift > policy | warn/fail |
| `TRANSFORM_MISSING` | required transform metadata missing | fail |
| `PROJECTION_EXTENSION_MISSING` | required projection metadata missing | fail |
| `BASELINE_NOT_FOUND` | baseline required but not resolvable | fail |
| `CARE_REDACTION_APPLIED` | details withheld under policy | warn |
| `SOVEREIGNTY_GATE_RESTRICTED` | restricted/unknown governance posture | warn/fail (policy) |

---

## 📦 Standard output shape (recommended)

Geometry validation SHOULD emit a small, stable artifact (suitable for rollups):

- per-run: `metrics.geometry.json` (or embedded in run metrics)
- release: `drift.geometry.delta.json` (optional; aggregated)

Example (truncated):

~~~json
{
  "algorithm_id": "kfm:rs:validate:geometry:integrity:v1",
  "run_id": "urn:kfm:run:<...>",
  "dataset_id": "urn:kfm:dataset:<...>",
  "scope": {
    "time_start_utc": "YYYY-MM-DDTHH:MM:SSZ",
    "time_end_utc": "YYYY-MM-DDTHH:MM:SSZ",
    "spatial_scope": "kansas|region:<...>|h3:r<...>",
    "sampling": "full|tiles|stratified|random"
  },
  "governance": {
    "care_gate_status": "allow|redact|deny",
    "sovereignty_gate": "clear|restricted|conflict|unknown",
    "redaction_summary": {
      "events_total": 0,
      "reasons": []
    }
  },
  "results": {
    "metrics": {
      "items_checked": 0,
      "crs_missing_count": 0,
      "crs_mismatch_count": 0,
      "invalid_geometry_count": 0,
      "bbox_invalid_count": 0,
      "bbox_out_of_bounds_count": 0,
      "tile_overlap_rate_pct": 0.0,
      "tile_gap_rate_pct": 0.0,
      "transform_missing_count": 0,
      "gsd_observed_median_m": null,
      "gsd_drift_pct_p50": null
    },
    "thresholds": {
      "crs_missing_count_max": 0,
      "invalid_geometry_count_max": 0,
      "tile_overlap_rate_pct_max": 2.0,
      "tile_gap_rate_pct_max": 2.0,
      "gsd_drift_pct_p50_max": 1.0
    },
    "outcome": "pass|warn|fail",
    "reason_codes": []
  },
  "refs": {
    "stac_items": [],
    "dcat_datasets": [],
    "prov_bundles": []
  },
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ"
}
~~~

Notes:

- keep metrics aggregated and safe
- do not embed coordinates or tile-specific “worst offenders” lists unless governance explicitly allows

---

## 🗺️ High-level geometry validation flow

~~~mermaid
flowchart TD
  A["Enumerate Items (deterministic ordering)"] --> B["Validate CRS + projection metadata"]
  A --> C["Validate bbox + geometry validity"]
  C --> D["Compute tile overlaps/gaps (aggregated)"]
  B --> E["Validate raster grid + resolution (if applicable)"]
  D --> F["Compare vs baseline (optional drift)"]
  E --> F
  F --> G["Evaluate thresholds (policy)"]
  G --> H["Emit small metrics artifact + refs to STAC/DCAT/PROV"]
~~~

---

## 🛡️ FAIR+CARE and sovereignty posture

Geometry metrics can become sensitive when:

- AOIs are small,
- reporting includes precise centroids or boundary coordinates,
- “bad tiles” are listed with locations.

Rules:

- use generalized `spatial_scope` (region-level or coarse H3) in in-repo artifacts
- do not include raw coordinates, site identifiers, or access instructions
- if policy requires redaction:
  - set `care_gate_status = redact|deny`
  - emit only aggregated metrics and reason codes
  - require steward review for deeper diagnosis through governed channels

---

## 🔗 Report integration

Geometry validation feeds:

- per-run bundles: `docs/analyses/remote-sensing/validation/reports/per-run/`
- daily rollups: `docs/analyses/remote-sensing/validation/reports/daily/`
- release rollups: `docs/analyses/remote-sensing/validation/reports/releases/`

Prefer linking from reports to:

- STAC Items/Collections representing validated artifacts,
- DCAT datasets/distributions,
- PROV bundles for lineage and configuration snapshots.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed geometry validation algorithms reference; defined CRS/footprint/tiling/grid checks, determinism rules, normalized reason codes, and governance-safe output shape. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Validation-Geometry-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Algorithms](../README.md) ·
[🧾 Reports](../../../reports/README.md) ·
[🏛️ Governance Charter](../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

