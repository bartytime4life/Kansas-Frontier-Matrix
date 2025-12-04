---
title: "🌦️ KFM v11.2.3 — STAC Extension: Climate & Atmosphere (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "KFM STAC extension for climate, atmosphere, and weather datasets, capturing variables, levels, run times, and aggregation semantics."
path: "docs/standards/catalogs/stac/extensions/stac-ext-climate.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council · Climate & Atmosphere Working Group"
content_stability: "stable"
backward_compatibility: "STAC 1.0.x extension-profile compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:stac-ext-climate-v11.2.3"
semantic_document_id: "kfm-stac-ext-climate-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:stac:extensions:climate:v11.2.3"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/catalog-metadata-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/catalog-metadata-v1.json"

governance_ref: "../../../governance/ROOT-GOVERNANCE.md"
faircare_ref: "../../../faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "STAC Extension Spec"
intent: "catalogs-stac-ext-climate"
status: "Active / Enforced"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E73 Information Object"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/stac/stac-ext-climate-v1.schema.json"
shape_schema_ref: "../../../../schemas/shacl/stac-ext-climate-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major climate extension revision"
---

<div align="center">

# 🌦️ STAC Extension — Climate & Atmosphere (`kfm-climate`)  
`docs/standards/catalogs/stac/extensions/stac-ext-climate.md`

**Namespace:** `https://schema.kfm.dev/stac/climate/1.0`  
**Prefix:** `kfmclim`

**Purpose:**  
Provide additional STAC fields for **climate, atmosphere, and weather** datasets in KFM (e.g., HRRR, reanalysis, forecasts, gridded climatologies) — including variables, vertical levels, run times, and aggregation semantics — while remaining compatible with the **STAC-first → DCAT-derived** catalog model.

</div>

---

## 📘 1. Scope

The `kfm-climate` extension:

- Applies primarily to **STAC Items** representing:
  - Model outputs (e.g., HRRR, GFS, downscaled products).  
  - Reanalysis or gridded observation tiles.  
  - Climate normals, climatologies, and anomaly fields.  
- May also apply to **STAC Collections** to summarize climate products.

It is designed to be used:

- Alongside **`kfm-core`** (`stac-ext-kfm-core.md`) for dataset IDs, domain tags, and region slugs.  
- Alongside domain-appropriate community extensions (e.g., **xarray/datacube** style profiles if adopted).  
- As the primary way to state variable-level semantics for climate/atmosphere in KFM STAC records.

---

## 🧱 2. Fields

### 2.1 Item Fields

| Field                           | Type      | Card. | Description |
|---------------------------------|-----------|-------|-------------|
| `kfmclim:variable`             | string    | 1     | Variable name, e.g. `precipitation`, `temperature`, `wind_speed`, `relative_humidity`. |
| `kfmclim:variable_standard`    | string    | 0..1  | Standardized variable name from a controlled vocabulary (e.g., CF standard name like `precipitation_amount`). |
| `kfmclim:units`                | string    | 0..1  | Units of the variable (e.g., `mm`, `K`, `m/s`, `%`). |
| `kfmclim:vertical_level`       | string    | 0..1  | Vertical level or layer (e.g., `surface`, `2m`, `10m`, `500hPa`, `isotherm-0C`). |
| `kfmclim:run_datetime`         | string    | 0..1  | Model run initialization time (ISO 8601) if different from valid time (e.g., HRRR run). |
| `kfmclim:lead_time_hours`      | number    | 0..1  | Forecast lead time in hours (0 for analysis or nowcast). |
| `kfmclim:spatial_resolution`   | string    | 0..1  | Human-readable nominal resolution, e.g. `3 km`, `0.25°`. |
| `kfmclim:temporal_aggregation` | string    | 0..1  | Temporal aggregation semantics: `instant`, `1h-avg`, `24h-sum`, `6h-sum`, etc. |
| `kfmclim:ensemble_member`      | string    | 0..1  | Ensemble member ID (e.g., `control`, `perturbation01`) if applicable. |
| `kfmclim:model_name`           | string    | 0..1  | Model or product name (e.g., `HRRR`, `GFS`, `ERA5`, `downscaled-HRRR-KFM`). |

### 2.2 Collection Fields (Optional)

For climate Collections, summarizing:

| Field                          | Type      | Card. | Description |
|--------------------------------|-----------|-------|-------------|
| `kfmclim:variables`           | [string]  | 0..*  | List of variables represented in this Collection. |
| `kfmclim:vertical_levels`     | [string]  | 0..*  | Common vertical levels (e.g., `surface`, `500hPa`). |
| `kfmclim:spatial_resolution`  | string    | 0..1  | Collection-level nominal resolution (e.g., `3 km`). |
| `kfmclim:temporal_coverage`   | string    | 0..1  | High-level description of temporal coverage (e.g., `2010–2025 hourly`). |
| `kfmclim:model_description`   | string    | 0..1  | Optional narrative describing the model or dataset. |

---

## 🌐 3. Usage Patterns

### 3.1 Instant vs Aggregated Products

Use `kfmclim:temporal_aggregation` to distinguish:

- **Instantaneous** fields:
  - `kfmclim:temporal_aggregation = "instant"`  
  - E.g., temperature snapshots, instantaneous wind speed.

- **Accumulated / averaged** fields:
  - `kfmclim:temporal_aggregation = "1h-avg"`, `"3h-sum"`, `"24h-sum"`, etc.  
  - E.g., 24-hour precipitation accumulation, hourly mean temperature.

This field is critical for:

- Downstream analytics (correct temporal interpretation).  
- Accurate DCAT derivation (e.g., in descriptive text, keywords).  
- UI behavior (how to display time series and tooltips).

### 3.2 Forecast vs Analysis / Reanalysis

Use `kfmclim:run_datetime` and `kfmclim:lead_time_hours` to:

- Distinguish **forecasts**:
  - `run_datetime` in the past, `lead_time_hours > 0`.  
- From **analysis / reanalysis**:
  - `run_datetime` may equal `properties.datetime`.  
  - `lead_time_hours = 0`.

This supports:

- Forecast skill evaluation.  
- Time-slice comparisons between model runs.  
- Clear semantics in Story Nodes and Focus Mode overlays.

---

## 🧾 4. Example Usage (Forecast Tile Item)

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "hrrr_precip_2025-06-01T00Z_f006",
  "properties": {
    "datetime": "2025-06-01T06:00:00Z",

    "kfm:dataset_id": "urn:kfm:dataset:hrrr-precip-ks-3km-v1",
    "kfm:domain": "climate",
    "kfm:subdomain": "precipitation",
    "kfm:region_slug": "kansas-statewide",
    "kfm:release_stage": "stable",

    "kfmclim:variable": "precipitation",
    "kfmclim:variable_standard": "precipitation_amount",
    "kfmclim:units": "mm",
    "kfmclim:vertical_level": "surface",
    "kfmclim:run_datetime": "2025-06-01T00:00:00Z",
    "kfmclim:lead_time_hours": 6,
    "kfmclim:spatial_resolution": "3 km",
    "kfmclim:temporal_aggregation": "6h-sum",
    "kfmclim:model_name": "HRRR"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [-102.0, 36.99],
        [-94.6, 36.99],
        [-94.6, 40.01],
        [-102.0, 40.01],
        [-102.0, 36.99]
      ]
    ]
  },
  "bbox": [-102.0, 36.99, -94.6, 40.01],
  "assets": {
    "data": {
      "href": "https://data.kfm.dev/hrrr/precip/2025/06/01/hrrr_precip_20250601_0000_f006.tif",
      "type": "image/tiff; application=geotiff",
      "roles": ["data"],
      "checksum:sha256": "abc123..."
    },
    "thumbnail": {
      "href": "https://data.kfm.dev/hrrr/precip/2025/06/01/hrrr_precip_20250601_0000_f006.png",
      "type": "image/png",
      "roles": ["thumbnail"]
    }
  }
}
~~~

---

## 🧪 5. Validation & CI Requirements

- **JSON Schema:** `stac-ext-climate-v1.schema.json` must be used alongside:
  - Core STAC schema.  
  - `stac-ext-kfm-core-v1.schema.json` (for `kfm:*` fields).  

- **CI Expectations:**

  - When `kfmclim:*` fields are present:
    - Validate field types and allowed values (especially for `temporal_aggregation`).  
    - Ensure `kfmclim:variable` is present and non-empty.  

  - Optional but recommended checks:
    - Validate `kfmclim:variable_standard` against a controlled vocabulary (e.g., CF standard names).  
    - Ensure `kfmclim:run_datetime` and `properties.datetime` relationships for forecasts make sense (e.g., `run_datetime` ≤ `datetime`).

- CI job (indicative): `catalog-stac-extensions-validate.yml` should include test Items using this extension.

---

## 🔁 6. Interaction with Other Extensions & Crosswalks

- **With `kfm-core` (`stac-ext-kfm-core.md`):**  
  - `kfm:domain` must typically be `climate` or `atmosphere` for datasets using this extension.  
  - `kfm:dataset_id` provides the stable identifier used in DCAT and Story Nodes.

- **With FAIR+CARE (`stac-ext-faircare.md`):**  
  - Climate datasets may have CARE metadata when they intersect with sensitive domains (e.g., vulnerability indices).  
  - `kfmfc:sensitivity`, `kfmfc:care_label`, and `kfmfc:sovereignty_flag` govern whether climate STAC records appear in public catalogs or certain views.

- **With STAC → DCAT crosswalks (`crosswalks/stac-dcat-crosswalk.md`):**  
  - `kfmclim:*` fields may map to:
    - `dcat:keyword` (e.g., variables and levels).  
    - Additional descriptive text or thematic classifications.  
  - They MUST NOT conflict with or override core STAC → DCAT mappings.

---

## ✅ 7. Implementation Checklist (Climate Datasets)

When onboarding a climate/atmosphere dataset into KFM STAC:

1. **Apply `kfm-core`**  
   - Set `kfm:dataset_id`, `kfm:domain = "climate"` (or `"atmosphere"`), `kfm:region_slug`, and lifecycle fields.

2. **Add `kfm-climate` fields**  
   - For each Item:
     - `kfmclim:variable`  
     - `kfmclim:units` (where applicable)  
     - `kfmclim:vertical_level` (for non-surface fields)  
     - `kfmclim:run_datetime` and `kfmclim:lead_time_hours` (for forecasts)  
     - `kfmclim:temporal_aggregation` and `kfmclim:spatial_resolution`  

3. **Validate**  
   - Run `stac-validator` with the climate extension schema.  
   - Ensure CI passes all extension-specific checks.

4. **Align with crosswalks**  
   - Confirm `kfmclim:*` mappings into DCAT (if used) are documented and tested.  
   - Update crosswalk unit tests where needed.

5. **Monitor telemetry**  
   - Track validation and usage of climate STAC metadata via `catalog-metadata-telemetry.json`.

---

## 🕰️ 8. Version History

| Version | Date       | Summary                                                                 |
|---------|------------|-------------------------------------------------------------------------|
| v1.0.0  | 2025-12-03 | Initial KFM climate & atmosphere STAC extension; aligned with KFM v11.2.3, STAC-first catalog model, and DCAT derivation patterns. |

