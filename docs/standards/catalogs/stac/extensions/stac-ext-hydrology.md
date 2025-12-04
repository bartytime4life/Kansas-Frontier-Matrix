---
title: "🌊 KFM v11.2.3 — STAC Extension: Hydrology & Rivers (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "KFM STAC extension for hydrology and riverine datasets, capturing watershed context, gauge metadata, vertical datums, and hydrology-specific sensitivity semantics."
path: "docs/standards/catalogs/stac/extensions/stac-ext-hydrology.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council · Hydrology Working Group"
content_stability: "stable"
backward_compatibility: "STAC 1.0.x extension-profile compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:stac-ext-hydrology-v11.2.3"
semantic_document_id: "kfm-stac-ext-hydrology-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:stac:extensions:hydrology:v11.2.3"

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
intent: "catalogs-stac-ext-hydrology"
status: "Active / Enforced"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: true
public_benefit_level: "High"
risk_category: "Moderate"
redaction_required: true

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E26 Physical Feature"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/stac/stac-ext-hydrology-v1.schema.json"
shape_schema_ref: "../../../../schemas/shacl/stac-ext-hydrology-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major hydrology extension revision"
---

<div align="center">

# 🌊 STAC Extension — Hydrology & Rivers (`kfm-hydrology`)  
`docs/standards/catalogs/stac/extensions/stac-ext-hydrology.md`

**Namespace:** `https://schema.kfm.dev/stac/hydrology/1.0`  
**Prefix:** `kfmhydro`

**Purpose:**  
Provide additional STAC fields for **hydrology and riverine** datasets in KFM — including watershed context, river IDs, gauge metadata, vertical datums, stage/discharge semantics, and hydrology-specific sensitivity classes — while remaining compatible with the **STAC-first → DCAT-derived** catalog model and KFM’s FAIR+CARE + sovereignty requirements.

</div>

---

## 📘 1. Scope

The `kfm-hydrology` extension:

- Applies primarily to **STAC Items** representing:
  - Streamflow / stage time series slices or tiles.  
  - Gridded hydrology products (e.g., runoff, soil moisture, flood depth rasters).  
  - Vector features such as river reaches, watershed boundaries, or inundation extents.  
- May also apply to **Collections** summarizing hydrology datasets.

It is designed to be used:

- Alongside **`kfm-core`** (`stac-ext-kfm-core.md`) for dataset IDs, domain tags, and region slugs.  
- Alongside **`kfm-faircare`** (`stac-ext-faircare.md`) where hydrology intersects with sensitive/sovereignty-governed contexts (e.g., tribal water rights, culturally significant waters).  

> **Note:**  
> This extension focuses on **hydrologic semantics**, not on storing raw time series in STAC. Time series live in assets (e.g., NetCDF, Parquet, CSV) referenced by STAC Items.

---

## 🧱 2. Fields

### 2.1 Item Fields

| Field                           | Type               | Card. | Description |
|---------------------------------|--------------------|-------|-------------|
| `kfmhydro:watershed_id`        | string             | 0..1  | Watershed or basin ID (e.g., HUC code or KFM watershed registry ID). |
| `kfmhydro:river_id`            | string             | 0..1  | River or reach ID (e.g., `arkansas-river-mainstem`, `smoky-hill-mainstem`). |
| `kfmhydro:gauge_id_internal`   | string             | 0..1  | **Internal-only** gauge/station ID; **must not be used** in public STAC/DCAT if sensitive. |
| `kfmhydro:gauge_kind`          | string             | 0..1  | Station type: `usgs-gage`, `kwo-station`, `reservoir-outlet`, `model-virtual`. |
| `kfmhydro:variable`            | string             | 0..1  | Primary hydrologic variable: `discharge`, `stage`, `water_level`, `storage`, `soil_moisture`. |
| `kfmhydro:units`               | string             | 0..1  | Units of `variable` (e.g., `m3/s`, `ft3/s`, `m`, `ft`, `percent`). |
| `kfmhydro:vertical_datum`      | string             | 0..1  | Vertical datum for stage/water-level (e.g., `NAVD88`, `NGVD29`, `local-datum`). |
| `kfmhydro:time_aggregation`    | string             | 0..1  | Temporal aggregation: `instant`, `15min-avg`, `1h-avg`, `daily-mean`, `daily-max`, `daily-min`. |
| `kfmhydro:product_kind`        | string             | 0..1  | Product type: `observation`, `forecast`, `reanalysis`, `derived-index`, `inundation-extent`. |
| `kfmhydro:hydro_sensitivity`   | string             | 0..1  | Hydrology-specific sensitivity (e.g., `general`, `operational-sensitive`, `rights-sensitive`). |
| `kfmhydro:notes_public`        | string             | 0..1  | Public-facing description of hydrology context (no confidential details). |

> **Governance rule:**  
> Use `kfmhydro:gauge_id_internal` only in internal STAC or internal views. Public STAC/DCAT may link to external public IDs (e.g., USGS site numbers) only where governance approves.

### 2.2 Collection Fields (Optional)

| Field                               | Type       | Card. | Description |
|-------------------------------------|------------|-------|-------------|
| `kfmhydro:primary_rivers`          | [string]   | 0..* | Primary rivers or reaches represented (e.g., `["arkansas-river", "smoky-hill-river"]`). |
| `kfmhydro:primary_watersheds`      | [string]   | 0..* | Key watersheds/basins represented (e.g., HUCs). |
| `kfmhydro:primary_variables`       | [string]   | 0..* | Key hydrology variables (e.g., `["discharge", "stage"]`). |
| `kfmhydro:hydro_coverage_statement`| string     | 0..1 | Narrative summary of hydrologic coverage (spatial, temporal, gauge/river types). |

---

## 🌐 3. Usage Patterns

### 3.1 Gauge/Station-Oriented Items

For Items representing time series at a gauge:

- Geometry should represent:
  - A point at a generalized location, or  
  - A short reach segment, if appropriate.

- Fields to set:

  - `kfmhydro:watershed_id`  
  - `kfmhydro:river_id`  
  - `kfmhydro:gauge_kind`  
  - `kfmhydro:variable`, `kfmhydro:units`  
  - `kfmhydro:vertical_datum` (for stage levels)  
  - `kfmhydro:time_aggregation` (e.g., `15min-avg`, `daily-mean`)  
  - `kfmhydro:product_kind = "observation"`

Public STAC may:

- Use external gauge IDs (e.g., USGS IDs) if governance-approved.  
- Omit or map internal gauge IDs to more generic labels where necessary.

### 3.2 Raster/Gridded Hydrology Products

For inundation rasters, runoff grids, soil moisture tiles:

- Use `kfmhydro:variable` and `kfmhydro:units` to describe field semantics.  
- Geometry/bbox should cover the gridded domain.  
- `kfmhydro:product_kind` often `derived-index` or `inundation-extent`.  
- `kfmhydro:time_aggregation` clarifies snapshot vs multi-hour or daily accumulation.

---

## 🧾 4. Example Usage (Gauge-Oriented Item)

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "usgs_06887500_daily_2025-06-01",
  "properties": {
    "datetime": "2025-06-01T12:00:00Z",

    "kfm:dataset_id": "urn:kfm:dataset:ks-river-gauges-daily-v1",
    "kfm:domain": "hydrology",
    "kfm:subdomain": "streamflow",
    "kfm:region_slug": "arkansas-river-basin",
    "kfm:release_stage": "stable",

    "kfmclim:temporal_aggregation": "daily-mean",  // optional if shared with climate

    "kfmhydro:watershed_id": "huc8-11030001",
    "kfmhydro:river_id": "arkansas-river-mainstem",
    "kfmhydro:gauge_id_internal": "USGS:06887500",
    "kfmhydro:gauge_kind": "usgs-gage",
    "kfmhydro:variable": "discharge",
    "kfmhydro:units": "ft3/s",
    "kfmhydro:vertical_datum": "local-datum",
    "kfmhydro:time_aggregation": "daily-mean",
    "kfmhydro:product_kind": "observation",
    "kfmhydro:hydro_sensitivity": "general",
    "kfmhydro:notes_public": "Daily mean discharge for a mainstem Arkansas River gauge in Kansas."
  },
  "geometry": {
    "type": "Point",
    "coordinates": [-97.345, 37.896]
  },
  "bbox": [-97.345, 37.896, -97.345, 37.896],
  "assets": {
    "timeseries": {
      "href": "https://data.kfm.dev/hydro/usgs/daily/06887500_2025-06-01.parquet",
      "type": "application/x-parquet",
      "roles": ["data"],
      "checksum:sha256": "abc123..."
    }
  }
}
~~~

> **Governance note:**  
> If exposure of a specific gauge location or ID is sensitive under certain contexts, a derived public STAC record should be created with generalized location and redacted IDs.

---

## 🧪 5. Validation & CI Requirements

- **Schema:** `stac-ext-hydrology-v1.schema.json` must be applied with:
  - Core STAC schema.  
  - `stac-ext-kfm-core-v1.schema.json` (for `kfm:*`).  

- **CI expectations:**

  - If any `kfmhydro:*` fields are present:
    - Validate field types and allowed values (e.g., `time_aggregation`, `product_kind`).  
    - Ensure `kfmhydro:variable` and `kfmhydro:units` are present for value fields.  
    - Check that `kfmhydro:gauge_id_internal` is omitted or redacted in public STAC builds, unless explicitly approved.

- **CI job (indicative):** `catalog-stac-extensions-validate.yml`  
  - Should include hydrology test records and assert that:
    - Internal-only IDs are absent from public bundles.  
    - Required fields are present and consistent.

---

## 🔁 6. Interaction with Other Extensions & Crosswalks

- **With `kfm-core` (`stac-ext-kfm-core.md`):**  
  - `kfm:domain` must typically be `"hydrology"` for Items using `kfm-hydrology`.  
  - `kfm:dataset_id` and `kfm:region_slug` link the dataset into larger KFM hydrology and region registries.

- **With `kfm-faircare` (`stac-ext-faircare.md`):**  
  - In certain contexts (e.g., water rights, sensitive reservoirs), hydrology datasets may be:
    - Tagged `kfmfc:sensitivity = "restricted-generalized"` or `restricted-internal`.  
  - `kfmhydro:hydro_sensitivity` can refine how restrictions apply (e.g., operations vs public education).

- **STAC → DCAT Crosswalks (`crosswalks/stac-dcat-crosswalk.md`):**  
  - Hydrology fields may inform:
    - `dcat:keyword` (e.g., `streamflow`, `river`, `watershed`).  
    - Additional descriptive text or thematic categories.  
  - Internal-only linkages (e.g., `gauge_id_internal`) must **not** appear in derived DCAT.

---

## ✅ 7. Implementation Checklist (Hydrology Datasets)

When onboarding a hydrology dataset into KFM STAC:

1. **Apply `kfm-core`:**  
   - Set `kfm:dataset_id`, `kfm:domain = "hydrology"`, `kfm:region_slug`, lifecycle fields.

2. **Add `kfm-hydrology` fields:**  
   - For Items: populate `watershed_id`, `river_id`, `gauge_kind`, `variable`, `units`, `vertical_datum`, `time_aggregation`, `product_kind`, `hydro_sensitivity`, and `notes_public` as appropriate.

3. **Consider FAIR+CARE:**  
   - If water rights, tribal governance, or sensitive infrastructures are involved, add `kfm-faircare` fields.

4. **Validate via CI:**  
   - Run STAC + extensions schemas.  
   - Ensure internal-only IDs do not leak to public artifacts.

5. **Derive DCAT safely:**  
   - Map relevant hydrology concepts to DCAT metadata and keywords without exposing sensitive IDs or locations.

6. **Monitor telemetry:**  
   - Track validation and crosswalk usage in `catalog-metadata-telemetry.json`.

---

## 🕰️ 8. Version History

| Version | Date       | Summary                                                                 |
|---------|------------|-------------------------------------------------------------------------|
| v1.0.0  | 2025-12-03 | Initial KFM hydrology & rivers STAC extension; aligned with KFM v11.2.3, STAC-first catalog model, FAIR+CARE + sovereignty standards, and hydrology governance requirements. |

