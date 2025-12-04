---
title: "🏺 KFM v11.2.3 — STAC Extension: Archaeology & Heritage (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "KFM STAC extension for archaeology and heritage datasets, capturing cultural periodization, investigation methods, and archaeology-specific sensitivity semantics."
path: "docs/standards/catalogs/stac/extensions/stac-ext-archaeology.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council · Archaeology Working Group"
content_stability: "stable"
backward_compatibility: "STAC 1.0.x extension-profile compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:stac-ext-archaeology-v11.2.3"
semantic_document_id: "kfm-stac-ext-archaeology-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:stac:extensions:archaeology:v11.2.3"

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
intent: "catalogs-stac-ext-archaeology"
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

json_schema_ref: "../../../../schemas/stac/stac-ext-archaeology-v1.schema.json"
shape_schema_ref: "../../../../schemas/shacl/stac-ext-archaeology-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major archaeology extension revision"
---

<div align="center">

# 🏺 STAC Extension — Archaeology & Heritage (`kfm-archaeology`)  
`docs/standards/catalogs/stac/extensions/stac-ext-archaeology.md`

**Namespace:** `https://schema.kfm.dev/stac/archaeology/1.0`  
**Prefix:** `kfmarch`

**Purpose:**  
Provide additional STAC fields for **archaeology and heritage** datasets in KFM — including cultural periodization, site/landscape classification, investigation methods, and archaeology-specific sensitivity semantics — while remaining compatible with the **STAC-first → DCAT-derived** catalog model and KFM’s FAIR+CARE + sovereignty requirements.

</div>

---

## 📘 1. Scope

The `kfm-archaeology` extension:

- Applies primarily to **STAC Items** representing:
  - Archaeology/heritage observations (e.g., survey coverage, geophysics tiles, remote-sensing interpretations).  
  - Landscape-scale cultural features (e.g., cultural regions, interaction spheres, site aggregates).  
- May also apply to **STAC Collections** that summarize archaeology datasets.

It is designed to be used:

- Alongside **`kfm-core`** (`stac-ext-kfm-core.md`) for shared KFM identifiers and domain tags.  
- Alongside **`kfm-faircare`** (`stac-ext-faircare.md`) for FAIR+CARE & sovereignty metadata.  
- Without exposing site-level or person-level sensitive information in public catalogs.

> **Important:**  
> This extension is **not** a license to expose exact site locations or restricted details. It provides a controlled vocabulary for describing archaeology datasets in a **governable, generalizable way**.

---

## 🧱 2. Fields

### 2.1 Item Fields

| Field                               | Type               | Card. | Description |
|-------------------------------------|--------------------|-------|-------------|
| `kfmarch:record_type`              | string             | 1     | High-level record type, e.g. `site-aggregate`, `landscape-region`, `survey-coverage`, `geophysics-product`, `interpretation-layer`. |
| `kfmarch:period`                   | string or [string] | 0..*  | Cultural-historical period label(s), mapped to KFM archaeology ontology (e.g. `Late Prehistoric`, `Protohistoric`). |
| `kfmarch:culture_phase`           | string or [string] | 0..*  | More specific culture/phase labels (e.g. `Great Bend Aspect`, `Central Plains Tradition`). |
| `kfmarch:investigation_method`    | string or [string] | 0..*  | Methods used: `pedestrian-survey`, `test-excavation`, `geophysics`, `remote-sensing-interpretation`, `archival-synthesis`, etc. |
| `kfmarch:dataset_role`            | string             | 0..1  | Role in archaeology workflows: `primary-observation`, `derived-interpretation`, `supporting-context`. |
| `kfmarch:location_representation` | string             | 0..1  | How location is represented: `generalized-region`, `grid`, `h3-only`, `exact-internal-only`. |
| `kfmarch:sensitivity_class`       | string             | 1     | Archaeology-specific sensitivity: `generalized`, `restricted-generalized`, `restricted-internal`. |
| `kfmarch:site_code_internal`      | string             | 0..1  | **Internal-only** site or complex code (e.g., state site ID); **must not be emitted** in public STAC/DCAT. |
| `kfmarch:notes_public`            | string             | 0..1  | Short public-friendly description; internal notes should use separate internal-only fields. |

> **Consistency rule:**  
> `kfmarch:sensitivity_class` must be consistent with `kfmfc:sensitivity` from the FAIR+CARE extension when both are present. The archaeology-specific class refines the generic CARE classification.

### 2.2 Collection Fields (Optional)

Collections may summarize broader archaeology datasets:

| Field                         | Type    | Card. | Description |
|-------------------------------|---------|-------|-------------|
| `kfmarch:primary_periods`    | [string] | 0..* | Primary periods represented in the collection. |
| `kfmarch:primary_methods`    | [string] | 0..* | Key methods represented (e.g. `geophysics`, `archival-synthesis`). |
| `kfmarch:coverage_statement` | string  | 0..1 | Narrative summary of spatial / temporal / methodological coverage. |

---

## 🧠 3. Usage Patterns & Governance

### 3.1 Site-Level vs Landscape-Level STAC

KFM public-facing archaeology STAC is generally **landscape- or aggregate-level**, not site-level:

- Items with `kfmarch:record_type = "landscape-region"` or `"site-aggregate"`:  
  - Represent generalized regions or aggregated information (e.g., densities, generalized presence/absence).  
  - `geometry` should be **generalized** in line with CARE visibility rules (`polygon-generalized` or `h3-only`).

- Items with `kfmarch:location_representation = "exact-internal-only"`:  
  - Intended for **internal-only** STAC; **must not** appear in public catalogs.  
  - Public derivatives should use separate Items with generalized geometry and redacted attributes.

### 3.2 Sensitivity Interplay  
(`kfmarch:sensitivity_class` & `kfmfc:sensitivity`)

Recommended mapping:

| `kfmarch:sensitivity_class` | `kfmfc:sensitivity`      | Intended Use                                                                 |
|-----------------------------|--------------------------|------------------------------------------------------------------------------|
| `generalized`               | `general`                | Public landscape or aggregate, geometry already generalized.                |
| `restricted-generalized`    | `restricted-generalized` | Public or community-limited, **heavily generalized** regions/aggregates.    |
| `restricted-internal`       | `restricted-internal`    | Internal-only records; only generalized derivatives appear in public STAC.  |

CI should verify that these mappings are obeyed and emit warnings or errors when they diverge.

---

## 🧾 4. Example Usage (Landscape-Scale Item)

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "arch_landscape_flint_hills_v1",
  "properties": {
    "datetime": "2025-01-01T00:00:00Z",

    "kfm:dataset_id": "urn:kfm:dataset:arch-flint-hills-landscape-v1",
    "kfm:domain": "archaeology",
    "kfm:region_slug": "flint-hills-region",
    "kfm:release_stage": "stable",

    "kfmfc:sensitivity": "restricted-generalized",
    "kfmfc:care_label": "Community-Controlled",
    "kfmfc:sovereignty_flag": true,
    "kfmfc:visibility_rules": "h3-only",

    "kfmarch:record_type": "landscape-region",
    "kfmarch:period": ["Late Prehistoric", "Protohistoric"],
    "kfmarch:culture_phase": ["Great Bend Aspect"],
    "kfmarch:investigation_method": [
      "remote-sensing-interpretation",
      "archival-synthesis"
    ],
    "kfmarch:dataset_role": "derived-interpretation",
    "kfmarch:location_representation": "h3-only",
    "kfmarch:sensitivity_class": "restricted-generalized",
    "kfmarch:notes_public": "Generalized cultural landscape region derived from multisource evidence."
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [-97.5, 37.0],
        [-96.5, 37.0],
        [-96.5, 38.0],
        [-97.5, 38.0],
        [-97.5, 37.0]
      ]
    ]
  },
  "bbox": [-97.5, 37.0, -96.5, 38.0],
  "assets": {
    "h3-grid": {
      "href": "https://data.kfm.dev/arch/flint-hills/h3_lvl6.geojson",
      "type": "application/geo+json",
      "roles": ["data"],
      "checksum:sha256": "abc123..."
    }
  }
}
~~~

> **Governance note:**  
> No site codes or exact site geometries appear here; this is a **generalized landscape representation** governed via `kfm-core`, `kfm-faircare`, and `kfm-archaeology` extension fields.

---

## 🧪 5. Validation & CI Requirements

- JSON Schema: `stac-ext-archaeology-v1.schema.json` must be applied alongside:
  - Core STAC schema.  
  - `stac-ext-kfm-core-v1.schema.json`.  
  - `stac-ext-faircare-v1.schema.json`.

- CI job (indicative): `catalog-stac-extensions-validate.yml` must ensure:

  - When `kfmarch:*` fields are present, they conform to this spec.  
  - `kfmarch:sensitivity_class` is present and consistent with `kfmfc:sensitivity`.  
  - Public STAC artifacts **do not** contain `kfmarch:site_code_internal`.  
  - Items with `kfmarch:location_representation = "exact-internal-only"` are not pushed into public catalogs or DCAT.

---

## 🔁 6. Interaction with Other Extensions & Crosswalks

- **With `kfm-core` (`stac-ext-kfm-core.md`):**  
  - Supplies core dataset identifiers (`kfm:dataset_id`), domain (`kfm:domain = "archaeology"`), and region slugs.  

- **With `kfm-faircare` (`stac-ext-faircare.md`):**  
  - Supplies generic CARE labels and sovereignty flags.  
  - `kfmarch:sensitivity_class` refines `kfmfc:sensitivity` at archaeology domain level.

- **With STAC → DCAT crosswalks (`crosswalks/stac-dcat-crosswalk.md`):**  
  - Selected fields (e.g. `kfmarch:period`, `kfmarch:culture_phase`) may be:
    - Reflected as keywords (`dcat:keyword`).  
    - Embedded in `dct:description` or thematic classification.  
  - Internal-only fields must be **excluded** from DCAT derivation.

---

## ✅ 7. Implementation Checklist (Archaeology Datasets)

When onboarding an archaeology dataset into KFM:

1. **Apply `kfm-core`**  
   - Set `kfm:dataset_id`, `kfm:domain = "archaeology"`, `kfm:region_slug`, and lifecycle fields.

2. **Apply `kfm-faircare`**  
   - Set `kfmfc:sensitivity`, `kfmfc:care_label`, `kfmfc:sovereignty_flag`, `kfmfc:visibility_rules`.

3. **Apply `kfm-archaeology`**  
   - Set `kfmarch:record_type`, `kfmarch:period`, `kfmarch:culture_phase`, `kfmarch:investigation_method`, `kfmarch:dataset_role`, `kfmarch:location_representation`, `kfmarch:sensitivity_class`, and `kfmarch:notes_public` where applicable.

4. **Generalize geometry appropriately**  
   - For public datasets, use **generalized polygons** or **H3 mosaics**, not precise site footprints.

5. **Validate in CI**  
   - Run `stac-validator` and KFM extension schema checks.  
   - Ensure CI passes both schema and governance checks.

6. **Derive DCAT safely**  
   - Use KFM STAC → DCAT crosswalks, ensuring sensitive fields do not leak.

---

## 🕰️ 8. Version History

| Version | Date       | Summary                                                                 |
|---------|------------|-------------------------------------------------------------------------|
| v1.0.0  | 2025-12-03 | Initial KFM archaeology & heritage STAC extension; aligned with KFM v11.2.3, STAC-first catalog model, FAIR+CARE + sovereignty standards, and web governance hooks. |

