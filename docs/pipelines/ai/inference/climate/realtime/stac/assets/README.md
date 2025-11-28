---
title: "🌡️⚡📦📁 KFM v11.2.2 — Climate Realtime AI STAC Asset Templates (GeoTIFF · NetCDF · Parquet · XAI Links)"
path: "docs/pipelines/ai/inference/climate/realtime/stac/assets/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "STAC Asset Template Suite (Realtime Climate Inference)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/climate-inference-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-climate-inference-v11.2.2.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Climate-Inference-Asset-Metadata"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-realtime-stac-assets"
  - "geotiff-schema"
  - "parquet-schema"
  - "netcdf-schema"
  - "xai-linkage"
  - "ephemeral-and-persistent-asset-metadata"
  - "scientific-metadata"
  - "projection-metadata"
  - "checksum-metadata"
  - "prov-xai"
  - "stac-xai"
  - "care-governance"
  - "h3-maskable"

scope:
  domain: "pipelines/ai/inference/climate/realtime/stac/assets"
  applies_to:
    - "geotiff.json"
    - "netcdf.json"
    - "parquet.json"
    - "xai-link.json"
    - "ephemeral-assets"
    - "persistent-assets"
    - "stac-xai"
    - "prov-xai"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🌡️⚡📦📁 **Realtime Climate Inference — STAC Asset Templates**  
`docs/pipelines/ai/inference/climate/realtime/stac/assets/README.md`

**Purpose:**  
Define the **canonical STAC asset schemas** for realtime climate inference outputs (GeoTIFF, NetCDF, Parquet, and XAI linkage) in both **ephemeral** (returned-only) and **persistent** (stored + cataloged) modes.  
These templates guarantee that every realtime asset is **deterministic**, **FAIR+CARE-compliant**, **sovereignty-safe**, **STAC-XAI aligned**, and **PROV-O traceable**, ready for use in Story Nodes, Focus Mode, and downstream climate/hazard analysis.

</div>

---

## 📘 Overview

Realtime climate inference in KFM can emit results as:

- **Ephemeral assets** returned directly to API clients (REST / WebSocket / gRPC) and not persisted.
- **Persistent assets** written to storage (e.g., lakeFS, object store) and indexed in the Climate STAC catalog.

Regardless of mode, asset **shape and metadata** must follow a small set of reusable JSON templates:

- `geotiff.json` — raster products (e.g., downscaled fields, micro-rasters, anomaly tiles).
- `netcdf.json` — multi-variable gridded outputs (e.g., tensor forecasts, ensembles).
- `parquet.json` — tabular climate driver outputs (e.g., CAPE / CIN / SRH driver tables).
- `xai-link.json` — linkage metadata connecting assets to JSON-LD explainability bundles and PROV.

This README specifies the **field-level requirements** so that:

- STAC Items can safely reference these assets under `assets.*`.
- Focus Mode and Story Nodes can rely on consistent metadata for spatiotemporal context.
- FAIR+CARE and sovereignty policies are consistently honored.

---

## 🗂️ Directory Layout

```text
docs/pipelines/ai/inference/climate/realtime/stac/assets/
├── README.md              # This file
├── geotiff.json           # Template for GeoTIFF climate rasters
├── netcdf.json            # Template for NetCDF multi-var outputs
├── parquet.json           # Template for Parquet climate driver tables
└── xai-link.json          # Template for XAI linkage blocks within STAC Items
```

Each JSON template is:

- **Schema-validated** in CI against KFM-STAC v11 profiles.
- **Reusable** both for ephemeral-response descriptions and persistent STAC entries.
- **Decorated with FAIR+CARE fields**, including license, provenance, and sovereignty flags.

---

## 🟥 GeoTIFF Asset Template (`geotiff.json`)

**Purpose:** Represent realtime raster outputs (e.g., downscaled fields, anomaly layers) as STAC assets.

### Required Core Fields

- `type`: `"image/tiff; application=geotiff"`
- `roles`: `["data"]`
- `proj:epsg`: EPSG code (typically `4326` or the operational CRS).
- `proj:shape`: `[height, width]` in pixels.
- `proj:transform`: 6-parameter or 9-parameter affine transform array.
- `proj:bbox`: `[minx, miny, maxx, maxy]` in asset CRS.
- `raster:bands`: array describing each band (index, `data_type`, `nodata`, `unit`, etc.).
- `scientific:units`: e.g. `"K"`, `"mm/day"`, `"m/s"`, `"Pa"`.
- `kfm:domain`: `"climate"`.
- `kfm:variable`: short variable name, e.g. `"tas"`, `"pr"`, `"cape"`, `"soil_moisture"`.

### Ephemeral vs Persistent

- **Ephemeral**:
  - `href` may be a presigned URL or omitted if the data stream is embedded in the response body.
  - `checksum:multihash` MAY be omitted but is **recommended** if the asset is materialized even temporarily.
- **Persistent**:
  - `href`: stable URL in object store / lakeFS.
  - `checksum:multihash`: REQUIRED (e.g. `"1220abcd..."`).
  - `kfm:persistence`: `"persistent"`.

### FAIR+CARE & Sovereignty

Required governance fields:

- `care:scope`: e.g. `"Public"` / `"Restricted"` if it encodes sensitive micro-climate for protected sites.
- `care:notes`: human-readable notes for use constraints.
- `sovereignty:flags`: e.g. `"within_tribal_land"`, `"none"`.
- `kfm:masking`: `"h3-generalized"` if spatial generalization has been applied.

---

## 🟦 NetCDF Asset Template (`netcdf.json`)

**Purpose:** Describe realtime multi-variable NetCDF outputs (ensembles, tensor forecasts, etc.).

### Required Core Fields

- `type`: `"application/netcdf"`
- `roles`: `["data"]`
- `kfm:domain`: `"climate"`.
- `kfm:variable_set`: array of variables present, e.g. `["tas", "pr", "hurs"]`.
- `kfm:model_version`: model identifier (aligning with model cards in `mcp/model_cards/`).
- `proj:epsg`: if coordinates are geographic/projected.
- `scientific:units`: may be a map of `variable -> unit`.
- `checksum:multihash`: REQUIRED for persistent assets.

### Optional Fields

- `kfm:ensemble_member`: e.g. `"r1i1p1f1"` or custom member id.
- `kfm:run_config`: pointer to an experiment log or configuration in `mcp/experiments/`.

### Governance

Same CARE and sovereignty fields as GeoTIFF:

- `care:scope`
- `care:notes`
- `sovereignty:flags`

---

## 🟩 Parquet Asset Template (`parquet.json`)

**Purpose:** Represent tabular realtime driver outputs (CAPE, CIN, SRH, LLJ metrics, etc.) as STAC assets.

### Required Core Fields

- `type`: `"application/x-parquet"`
- `roles`: `["data"]`
- `kfm:domain`: `"climate"`.
- `kfm:driver_set`: description or list of driver indicators included, e.g.:

  ```json
  "kfm:driver_set": ["CAPE", "CIN", "SRH_0_1km", "LLJ_speed_850hPa"]
  ```

- `schema`: a compact description of columns (names, types, units).
- `checksum:multihash`: REQUIRED for persistent assets.

### Spatial Information (If Applicable)

If rows are spatially keyed:

- `proj:epsg`: coordinate system of any geometry or coordinate columns.
- `kfm:spatial_index`: e.g. `"h3"`, with an accompanying resolution if using H3, or `"latlon"` for raw coordinates.

### Governance

- CARE and sovereignty fields as above.
- If table includes sensitive sites, note masking rules in `kfm:masking`.

---

## 🧬 XAI Linkage Template (`xai-link.json`)

**Purpose:** Provide a reusable object that can be embedded under STAC Item `properties` or `assets.*` to bind assets to explainability bundles and provenance.

### Required Fields

- `xai:local`: URL or ID of JSON-LD local explainability bundle (e.g. SHAP/IG per inference).
- `xai:global`: URL or ID of global driver explainability (if applicable).
- `xai:spatial`: URL or ID of spatial XAI artifact (CAM or spatial attribution tiles/rasters).
- `xai:drivers`: URL or ID of driver taxonomy JSON-LD (e.g. `climate-driver-taxonomy.jsonld`).

### Provenance

- `prov:wasGeneratedBy`: reference to the realtime inference run id.
- `prov:used`: array of input STAC Item IDs or source dataset URIs.
- `kfm:run_id`: internal run identifier matching logs in `mcp/experiments/`.

### CARE & Sovereignty

- `care:scope`
- `care:notes`
- `sovereignty:flags`

These fields ensure that explainability outputs respect the same ethical / sovereignty guardrails as the data.

---

## 📡 STAC-XAI Integration Rules

When embedding these asset schemas into STAC Items:

- Include `kfm:explainability:method` on the Item or asset, e.g. `"shap"`, `"integrated-gradients"`, `"cams"`, `"spatial-attribution"`.
- Ensure `kfm:explainability:{local|global|spatial}` flags are consistent with which XAI bundles exist.
- For **ephemeral** responses (no persistent Items), the same schema applies, but `href` may be transient or omitted, and checksums may be optional.
- For **persistent** outputs, all STAC-required fields (including `href`, `checksum:multihash`, `proj:*` where applicable) MUST be present.

---

## 🧪 CI / Validation

CI enforces:

- JSON schema validation of `geotiff.json`, `netcdf.json`, `parquet.json`, `xai-link.json`.
- Presence of CARE/sovereignty fields in all asset templates.
- Conformance to `KFM-STAC v11` and `KFM-DCAT v11` profiles.
- Deterministic ordering of keys (to keep diffs clean and reproducible).

Any deviation → ❌ merge blocked, until asset templates are corrected.

---

## 🕰️ Version History

| Version  | Date       | Notes                                                                 |
|----------|------------|-----------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate Realtime STAC asset template suite (this document).   |

---

<div align="center">

### 🔗 Footer  

[⬅ Back to Realtime STAC](../README.md) · [🌡️ Climate Inference Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
