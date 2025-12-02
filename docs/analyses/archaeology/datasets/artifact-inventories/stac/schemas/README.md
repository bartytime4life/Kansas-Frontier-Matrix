---
title: "📐 Kansas Frontier Matrix — Artifact Inventory STAC Schemas (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/README.md"
description: "Schema set for validating STAC 1.0 Items and Collections for KFM v11 artifact inventories, including KFM and CARE extensions."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council · Metadata Standards Subcommittee"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-stac-schemas-v11.2.3"
doc_kind: "Schema Documentation"
intent: "artifact-inventory-stac-schemas"
semantic_document_id: "kfm-doc-archaeology-artifact-stac-schemas-v11.2.3"
category: "Analyses · Archaeology · STAC Schemas"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/archaeology-artifact-stac-schemas-v1.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A1-I1-R1"
care_label: "High-Sensitivity · Sovereignty-Governed"
sensitivity: "Cultural / Archaeological / Heritage"
sensitivity_level: "High"
indigenous_rights_flag: true
risk_category: "Moderate"
public_exposure_risk: "Governed"
redaction_required: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Public (Governed)"
jurisdiction: "Kansas / United States"
immutability_status: "mutable-plan"

header_profile: "standard"
footer_profile: "standard"

data_steward: "Archaeology Working Group · Metadata Standards Subcommittee"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 📐 Kansas Frontier Matrix — Artifact Inventory STAC Schemas (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/README.md`

**Purpose**  
Define and document the **STAC JSON Schema set** used to validate artifact-inventory STAC Items and Collections in KFM v11.

These schemas enforce compliance with:

- STAC 1.0 core  
- Projection extension (`proj`)  
- Scientific extension (`sci`)  
- Versioning extension (`version`)  
- Checksum extension (`checksum`)  
- KFM archaeology extension (`kfm:*`)  
- CARE cultural safety extension (`care:*`)  
- DCAT 3.0 crosswalk rules  
- FAIR+CARE and sovereignty governance

Every artifact-inventory STAC document must validate against this schema set **before** it can enter the KFM catalog, knowledge graph, pipelines, or Focus Mode v3.

---

## 📘 Overview

Schemas in this directory define:

- Valid **STAC Item** structure for artifact inventories  
- Valid **STAC Collection** structure for artifact groupings  
- **Domain-specific archaeology fields** (`kfm:*`)  
- **Cultural safety fields** (`care:*`)  
- Structural constraints for:
  - Spatial generalization  
  - Temporal coverage  
  - Provenance linkage  
- Required cross-linking to:
  - Inventories in `../items/` → `../inventories/`  
  - Metadata/DCAT in `../metadata/`  
  - PROV-O lineage in `../provenance/`  

These schemas are used by:

- CI pipelines (for example, `artifact-stac-validate.yml`)  
- Dataset ingestion utilities  
- Story Node and Focus Mode metadata builders  
- KFM STAC and catalog viewers  

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/stac/schemas/
├── 📄 README.md                          # This file (schema documentation)
├── 📄 stac-item-schema.json              # Validator for artifact-inventory STAC Items
├── 📄 stac-collection-schema.json        # Validator for artifact-inventory STAC Collections
├── 📄 kfm-archaeology-extension.json     # KFM archaeology extension schema (kfm:*)
├── 📄 care-sensitivity-extension.json    # CARE cultural safety extension schema (care:*)
├── 📄 dcat-crosswalk.json                # DCAT ↔ STAC mapping constraints
└── 📂 templates/                         # Example skeletons for new/extended schemas
~~~

This layout is **normative** for artifact-inventory STAC schemas.

---

## 1️⃣ STAC Item Schema — Artifact Inventories

**Location:** `stac-item-schema.json`

This schema validates STAC Items representing individual artifact inventories.

### Core STAC fields

The Item schema enforces:

- `stac_version = "1.0.0"`  
- `type = "Feature"`  
- `id` — non-empty string; typically lowercase, versioned  
- `bbox` — array of numeric coordinates (generalized only)  
- `geometry` — valid GeoJSON object (MultiPoint / Polygon / MultiPolygon)  
- `properties` — required object  
- `assets` — required object containing at least one `data` asset  
- `links` — array of link objects

### Required Item properties

Minimum expectations for artifact inventories:

- `properties.datetime` — `null` or representative timestamp  
- Or, depending on pattern, phase-based temporal metadata in Items or their parent Collections  
- `assets.data`:
  - `href` — path to inventory table (CSV/Parquet)  
  - `type` — correct MIME type  
  - `roles` — must include `"data"`  
- `links`:
  - At least one entry with `rel = "collection"` referencing the parent Collection JSON

The Item schema does **not** permit raw, non-generalized geometries for KFM archaeology.

---

## 2️⃣ STAC Collection Schema — Artifact Groupings

**Location:** `stac-collection-schema.json`

Validates STAC Collections that group artifact inventories by material, phase, or scope.

Key checks:

- `stac_version = "1.0.0"`  
- `type = "Collection"`  
- `id` — non-empty string; consistent with file name and grouping semantics  
- `description` — human-readable explanation of the Collection  
- `license` — SPDX identifier (for example, `"CC-BY-4.0"`)  
- `extent.spatial.bbox` — generalized bounding box  
- `extent.temporal.interval` — array of time intervals  
- `links` — optional for file-only catalogs; required when exposed via API  
- `kfm:*` and `care:*` fields when present, enforced by extension schemas

Collections support:

- Root artifact-inventories collection  
- Material-specific groupings (lithics, ceramics, metals, faunal)  
- Additional sub-Collections as needed

---

## 3️⃣ KFM Archaeology Extension Schema (`kfm:*`)

**Location:** `kfm-archaeology-extension.json`

Defines KFM-specific archaeology metadata used in Items and Collections.

Typical fields enforced:

| Field                | Purpose                                           |
|----------------------|---------------------------------------------------|
| `kfm:domain`         | Domain identifier (must be `archaeology-artifact-inventories`) |
| `kfm:phase`          | Cultural-phase classification                    |
| `kfm:material_class` | Material class: `lithic`, `ceramic`, `metal`, `faunal` |
| `kfm:datatype`       | Dataset type (for example, `"artifact-inventory"`) |
| `kfm:source`         | Institution / repository providing the dataset   |
| `kfm:provenance`     | Path to PROV-O lineage JSON                      |
| `kfm:review_cycle`   | Governance review cadence (for example, `Biannual`) |

The extension schema ensures:

- Controlled vocabularies for material classes and datatypes.  
- Presence of fields required for ETL, graph ingestion, and Focus Mode.  
- Consistent domain tagging across all artifact inventories.

---

## 4️⃣ CARE Sensitivity Schema (`care:*`)

**Location:** `care-sensitivity-extension.json`

Defines the CARE cultural safety extension used by artifact-inventory STAC documents.

Key fields:

| Field              | Rules / Purpose                                                  |
|--------------------|------------------------------------------------------------------|
| `care:sensitivity` | `general`, `generalized`, or `restricted-generalized`; no `restricted` in public artifacts |
| `care:review`      | `faircare`, `tribal`, or `none-required`                         |
| `care:notes`       | Required when sensitivity is `generalized` or `restricted-generalized` |
| `care:sovereignty` | Indicates sovereignty-governed status (for example, `protected`) |
| `care:visibility_rules` | Optional; rules for geometry/visibility (for example, `h3-only`) |

The schema prohibits:

- Raw site coordinates in Items labeled as artifact inventories.  
- Use of `care:sensitivity = "restricted"` in the public STAC layer.  

It enforces alignment between sensitivity labels and generalization practices.

---

## 5️⃣ DCAT Crosswalk Schema

**Location:** `dcat-crosswalk.json`

The crosswalk schema ensures STAC metadata can be translated to DCAT for external catalogs.

Checks include:

- Presence and value-type correctness for key DCAT-mapped fields.  
- Alignment between:
  - STAC `license` and DCAT `dct:license`  
  - STAC temporal fields and DCAT temporal coverage  
  - STAC assets and DCAT distributions  

This ensures KFM artifact inventories can be surfaced in DCAT-compatible catalogs without losing essential semantics or governance information.

---

## 🧪 Validation Pipeline Integrations

Schemas in this directory are used by CI and tooling, including:

- `.github/workflows/artifact-stac-validate.yml`  
- Any archaeology-specific metadata validation workflows  

Typical validation sequence:

1. STAC core schema validation (Item or Collection).  
2. KFM archaeology extension validation (`kfm-archaeology-extension.json`).  
3. CARE extension validation (`care-sensitivity-extension.json`).  
4. DCAT crosswalk validation (`dcat-crosswalk.json`), when DCAT records exist.  
5. Checksum and integrity checks (where `checksum` extension is used).  
6. Provenance linkage checks (paths under `../provenance/`).  
7. Cross-file consistency checks with:
   - `../items/`  
   - `../collections/`  
   - `../metadata/`  
   - PROV-O archives  

Only artifacts that pass all checks may be used in releases, Focus Mode, or Story Node generation.

---

## 🧠 Example Minimal Schema Snippet

Illustrative fragment from an Item schema (not normative):

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Archaeology STAC Item Schema",
  "type": "object",
  "required": ["id", "stac_version", "type", "bbox", "geometry", "properties", "assets"],
  "properties": {
    "stac_version": { "const": "1.0.0" },
    "type": { "const": "Feature" }
  }
}
~~~

Full schemas are defined in the JSON files in this directory and must be treated as the authoritative source.

---

## 🕰 Version History

| Version   | Date       | Author                                       | Summary                                                                 |
|-----------|------------|----------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Archaeology WG · Metadata Standards Subcommittee | Updated schema documentation for KFM v11.2.3; added energy/carbon telemetry references and clarified CARE/sovereignty constraints. |
| v10.4.0   | 2025-11-17 | Archaeology WG · FAIR+CARE Council          | Added schema suite for artifact inventories; integrated KFM and CARE extensions; documented validation pipeline. |
| v10.0.0   | 2025-11-10 | Artifact Metadata Team                       | Initial schema directory structure and stub documentation.             |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Artifact STAC Catalog](../README.md)