---
title: "🧩 KFM v11.2.3 — STAC Extension: KFM Core (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Core KFM STAC extension for shared identifiers, domain tags, and governance metadata across all STAC Items and Collections."
path: "docs/standards/catalogs/stac/extensions/stac-ext-kfm-core.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "STAC 1.0.x extension-profile compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:stac-ext-kfm-core-v11.2.3"
semantic_document_id: "kfm-stac-ext-kfm-core-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:stac:extensions:kfm-core:v11.2.3"

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
intent: "catalogs-stac-ext-kfm-core"
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

json_schema_ref: "../../../../schemas/stac/stac-ext-kfm-core-v1.schema.json"
shape_schema_ref: "../../../../schemas/shacl/stac-ext-kfm-core-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major KFM core extension revision"
---

<div align="center">

# 🧩 STAC Extension — KFM Core (`kfm-core`)  
`docs/standards/catalogs/stac/extensions/stac-ext-kfm-core.md`

**Namespace:** `https://schema.kfm.dev/stac/kfm-core/1.0`  
**Prefix:** `kfm`

**Purpose:**  
Provide a **core KFM STAC extension** for Items and Collections, adding shared identifiers, domain tags, and lifecycle/governance metadata that are used consistently across all KFM domains (climate, hydrology, archaeology, imagery, etc.).

</div>

---

## 📘 1. Scope

The `kfm-core` extension:

- Applies to **STAC Items and Collections**.  
- Adds KFM-specific fields that:
  - Tie records into the KFM dataset registry.  
  - Classify datasets by domain and subdomain.  
  - Express lifecycle, release stage, and review cadence.  

It is designed to:

- Work **alongside** core STAC and community extensions (e.g., `eo`, `sar`).  
- Provide a **stable, minimal base** used by domain extensions such as:
  - `kfm-climate` (`stac-ext-climate.md`)  
  - `kfm-hydrology` (`stac-ext-hydrology.md`)  
  - `kfm-archaeology` (`stac-ext-archaeology.md`)  
  - `kfm-faircare` (`stac-ext-faircare.md`)  

---

## 🧱 2. Fields

### 2.1 Item / Collection Fields

| Field               | Type      | Card. | Applies To   | Description |
|---------------------|-----------|-------|-------------|-------------|
| `kfm:dataset_id`    | string    | 1     | Item, Coll. | Stable KFM dataset identifier (URI or CURIE); links STAC to KFM dataset registry and DCAT records. |
| `kfm:domain`        | string    | 1     | Item, Coll. | High-level domain classification (e.g., `climate`, `hydrology`, `archaeology`, `imagery`). |
| `kfm:subdomain`     | string    | 0..1  | Item, Coll. | Optional subdomain (e.g., `precipitation`, `streamflow`, `cultural-regions`). |
| `kfm:region_slug`   | string    | 0..1  | Item, Coll. | Slug linking to KFM region registries (e.g., `flint-hills-region`, `arkansas-river-basin`). |
| `kfm:release_stage` | string    | 1     | Item, Coll. | KFM lifecycle stage (`experimental`, `beta`, `stable`, `retired`). |
| `kfm:lifecycle`     | string    | 0..1  | Item, Coll. | Extended lifecycle tag (e.g., `LTS`, `archived`, `preview-only`). |
| `kfm:review_cycle`  | string    | 0..1  | Item, Coll. | Human-readable review schedule (e.g., `Annual · Hydrology WG`, `Biennial · Archaeology WG`). |

### 2.2 Recommended Value Sets (Illustrative)

- `kfm:domain` (non-exhaustive):  
  - `climate`, `hydrology`, `archaeology`, `imagery`, `topography`, `socioeconomic`, `governance`.

- `kfm:release_stage`:  
  - `experimental`, `beta`, `stable`, `retired`.

Controlled vocabularies should be documented in a shared ontology (e.g., `docs/standards/ontology/`) and referenced in extension schema validation.

---

## 📚 3. Example Usage (Item)

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "naip_2023_tile_001",
  "properties": {
    "datetime": "2023-07-11T18:22:00Z",

    "kfm:dataset_id": "urn:kfm:dataset:naip-ks-2023",
    "kfm:domain": "imagery",
    "kfm:subdomain": "naip",
    "kfm:region_slug": "central-kansas-region",
    "kfm:release_stage": "stable",
    "kfm:lifecycle": "LTS",
    "kfm:review_cycle": "Biennial · Imagery Working Group"
  },
  "geometry": { "...": "..." },
  "bbox": [-98.0, 38.1, -97.9, 38.2],
  "assets": {
    "image": {
      "href": "https://example.com/naip_001.tif",
      "type": "image/tiff; application=geotiff",
      "roles": ["data"],
      "checksum:sha256": "abc123..."
    },
    "thumbnail": {
      "href": "https://example.com/naip_001.png",
      "type": "image/png",
      "roles": ["thumbnail"]
    }
  }
}
~~~

**Notes:**

- `kfm:dataset_id` is stable across multiple STAC Items belonging to the same dataset.  
- `kfm:domain` and `kfm:subdomain` support:
  - Catalog filtering and discovery.  
  - Routing to domain-specific governance and visualization logic.  

---

## 🔗 4. Relationship to Other KFM Extensions

- **`kfm-faircare` (`stac-ext-faircare.md`):**  
  - Adds FAIR+CARE and sovereignty information.  
  - Uses `kfm:dataset_id` and `kfm:domain` to link governance metadata to datasets.

- **Domain extensions (`kfm-climate`, `kfm-hydrology`, `kfm-archaeology`, etc.):**  
  - Rely on `kfm:domain` / `kfm:subdomain` to scope applicability.  
  - Leverage `kfm:region_slug` for region-aware behavior (web overlays, analytics).

- **STAC → DCAT crosswalks:**  
  - Map `kfm:dataset_id` to DCAT identifiers.  
  - Use `kfm:domain` and `kfm:subdomain` as `dcat:keyword` or thematic tags.

---

## 🧪 5. Validation & CI Requirements

**Schema:**  
- `stac-ext-kfm-core-v1.schema.json` must be used alongside the core STAC schema and other applicable KFM extension schemas.

**CI checks** (indicative):

- If any `kfm:*` fields are present:
  - `kfm:dataset_id`, `kfm:domain`, and `kfm:release_stage` MUST be present.  
- `kfm:domain` values must match allowed vocabulary.  
- `kfm:release_stage` values must match allowed vocabulary.

**CI job:**  
- `catalog-stac-extensions-validate.yml` should:
  - Validate `kfm-core` fields for all Items/Collections claiming the extension.  
  - Flag missing required fields or invalid values.

---

## ✅ 6. Implementation Checklist

When onboarding a dataset into KFM STAC:

1. **Assign core identifiers and domain tags:**
   - `kfm:dataset_id`  
   - `kfm:domain` and optional `kfm:subdomain`  
   - `kfm:region_slug` (if dataset is region-specific)

2. **Set lifecycle & governance signals:**
   - `kfm:release_stage`  
   - Optional `kfm:lifecycle` and `kfm:review_cycle`

3. **Validate:**
   - Run `stac-validator` with `kfm-core` schema enabled.  
   - Ensure CI passes core extension checks.

4. **Align downstream use:**
   - Ensure STAC → DCAT crosswalk uses `kfm:dataset_id` and domain tags correctly.  
   - Ensure web UIs and analytics respect `kfm:release_stage` and lifecycle hints.

---

## 🕰️ 7. Version History

| Version | Date       | Summary                                                                 |
|---------|------------|-------------------------------------------------------------------------|
| v1.0.0  | 2025-12-03 | Initial `kfm-core` STAC extension; defined shared identifiers, domain tags, and lifecycle metadata aligned with KFM v11.2.3 and STAC-first catalog model. |

