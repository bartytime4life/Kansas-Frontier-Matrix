---
title: "📐 Kansas Frontier Matrix — Remote Sensing Lineage Schema Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/lineage/schemas/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-remote-sensing-lineage-schemas-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📐 **Kansas Frontier Matrix — Remote Sensing Lineage Schema Registry**  
`src/pipelines/remote-sensing/lineage/schemas/README.md`

**Purpose:**  
Define the **canonical JSON-LD contexts and JSON Schemas** used to validate all Remote Sensing lineage and provenance outputs — including PROV-O entities, GeoSPARQL geometries, CIDOC-CRM mappings, and KFM lineage extensions.  
These schemas guarantee that lineage records are **machine-valid**, **FAIR+CARE-governed**, **GeoSPARQL-ready**, and **MCP-DL v6.3 compliant**.

<img alt="Lineage Schemas" src="https://img.shields.io/badge/Lineage-Schema_Registry-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="Linked Data" src="https://img.shields.io/badge/Linked_Data-GeoSPARQL_success-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

Remote Sensing pipelines emit **JSON-LD lineage bundles** describing:

- STAC source Items and assets  
- Preprocessing steps (cloud mask, SAR RTC, reprojection, normalization)  
- Analytical steps (indices, hazards)  
- AI summarization activities (optional)  
- Neo4j graph publishing and spatial relationships  
- RDF/GeoSPARQL exports  
- CARE masking and sovereignty-sensitive operations  

This directory contains the **schema + context files** that:

- Define allowed entity/relationship structures  
- Bind PROV-O, GeoSPARQL, CIDOC-CRM, and KFM extensions together  
- Enable CI to validate lineage outputs before they are accepted into governance ledgers  

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/remote-sensing/lineage/schemas/
├── README.md                          # This file
│
├── lineage.schema.json                # Master JSON Schema for lineage bundles
├── prov_o_context.jsonld              # PROV-O JSON-LD context
├── geosparql_context.jsonld           # GeoSPARQL JSON-LD context
├── cidoc_crm_context.jsonld           # CIDOC-CRM JSON-LD context (selected classes)
└── kfm_lineage_rules.json             # KFM-specific lineage constraints & rules
~~~~~

---

## 🧬 Master Lineage Schema — `lineage.schema.json`

**Role:**  
Validate every lineage document produced by Remote Sensing pipelines.

### Key Requirements

Each lineage JSON-LD must:

- Be an **object** with `@context`, `@id`, and `type` fields  
- Include at least one `prov:Entity` and one `prov:Activity`  
- Reference source STAC Items & AOI entities where applicable  
- Include KFM governance fields: `kfm:careLabel`, `kfm:maskingStrategy`, `kfm:telemetryRef`, etc.  

Abridged structure:

~~~~~json
{
  "type": "object",
  "required": ["@context", "@id", "type", "prov:wasGeneratedBy"],
  "properties": {
    "@context": {
      "type": ["array", "string"]
    },
    "@id": {
      "type": "string"
    },
    "type": {
      "type": ["array", "string"]
    },
    "prov:wasGeneratedBy": {
      "$ref": "#/definitions/activity"
    },
    "kfm:careLabel": {
      "type": "string",
      "enum": ["public", "sensitive", "restricted"]
    }
  },
  "definitions": {
    "activity": {
      "type": "object",
      "required": ["@id", "type"],
      "properties": {
        "@id": { "type": "string" },
        "type": { "type": ["array", "string"] },
        "prov:used": { "type": ["array", "string"] }
      }
    }
  }
}
~~~~~

---

## 🧪 PROV-O Context — `prov_o_context.jsonld`

Defines IRIs and mappings for:

- `prov:Entity`  
- `prov:Activity`  
- `prov:Agent`  
- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:wasAttributedTo`  
- `prov:generatedAtTime`  

This context ensures all lineage documents adopt **W3C PROV-O** semantics.

---

## 🌐 GeoSPARQL Context — `geosparql_context.jsonld`

Defines:

- `geo:Feature`  
- `geo:Geometry`  
- `geo:hasGeometry`  
- `geo:asWKT`  
- Spatial functions such as `geo:sfIntersects` used in RDF exports

Remote Sensing lineage uses this context to express:

- Scene footprints  
- AOI geometries  
- Scene ↔ County / AOI intersection semantics  

---

## 🏺 CIDOC CRM Context — `cidoc_crm_context.jsonld`

Provides mappings for:

- `E7 Activity` — interpretive or analytic acts (e.g., AI summaries)  
- `E53 Place` — counties, basins, AOIs  
- `E94 Space Primitive` — geometries at specific scales  

CIDOC elements are used in advanced heritage/interpretive workflows where Remote Sensing intersects archaeological or cultural data.

---

## 🧱 KFM Lineage Rules — `kfm_lineage_rules.json`

Encodes **KFM-specific constraints** beyond basic schemas:

- Which processing steps must appear in `kfm:processingSteps[]`  
- Which fields are required when `careLabel != "public"`  
- Minimum provenance depth (e.g., at least one STAC source, one AOI entity)  
- Valid values for `kfm:maskingStrategy` (e.g., `h3_r7`, `bbox_expand_5km`)  
- Requirements for AI-related provenance:

  - `kfm:aiSummaryModel`  
  - `kfm:aiSummaryPrompt` (hashed or referenced, not raw)  
  - `kfm:aiSummaryRefusal` flags  

Example (abridged):

~~~~~json
{
  "requiredSteps": [
    "cloud_mask",
    "harmonize_gsd",
    "reproject"
  ],
  "sensitiveCareLabelsRequire": {
    "careLabel": ["sensitive", "restricted"],
    "mustInclude": ["kfm:maskingStrategy", "geo:hasGeometry"]
  }
}
~~~~~

---

## ⚖️ FAIR+CARE Governance Hooks

Lineage schemas enforce the presence of:

- `kfm:careLabel`  
- `kfm:maskingStrategy` for sensitive/restricted data  
- `kfm:sovereigntyConflict` flags when AOIs intersect sovereignty overlays  
- `kfm:governanceRef` pointing to:

  ~~~~~text
  docs/reports/audit/data_provenance_ledger.json
  ~~~~~

`faircare-validate.yml` uses these schema/context files to:

- Ensure CARE labels and masking strategies are present  
- Validate that sensitive geometries are represented in generalized form  
- Require sovereignty fields when relevant AOIs are used  

---

## 📡 Telemetry & Schema Alignment

All lineage records include a link to telemetry:

- `kfm:telemetryRef` → NDJSON summary for the run  

Schema references from this registry ensure telemetry is:

- Connected to lineage  
- Cross-checkable (energy/CO₂, pixel counts, care violations)  
- Aggregated into:

  ~~~~~text
  ../../../../../releases/v10.3.0/focus-telemetry.json
  ~~~~~

---

## 🧪 Local Validation Example

Validate a lineage JSON-LD file:

~~~~~bash
jsonschema \
  -i data/processed/lineage/landsat/scene_2025_310923.jsonld \
  src/pipelines/remote-sensing/lineage/schemas/lineage.schema.json
~~~~~

Check JSON-LD context loading (e.g., via `pyld`):

~~~~~bash
python - << 'EOF'
from pyld import jsonld
import json
doc = json.load(open("data/processed/lineage/landsat/scene_2025_310923.jsonld"))
expanded = jsonld.expand(doc)
print(len(expanded))
EOF
~~~~~

---

## 🛠️ CI Integration

Schemas in this directory are used by:

- `lineage-validate.yml` — validates lineage against `lineage.schema.json`  
- `faircare-validate.yml` — verifies CARE/sovereignty/AI rules via `kfm_lineage_rules.json`  
- `telemetry-export.yml` — cross-checks telemetry references in lineage  
- `docs-lint.yml` — ensures this README and schema paths remain consistent  

Any lineage record not conforming to these schemas MUST be:

- Rejected from governance ledgers  
- Flagged in CI  
- Investigated by the pipeline maintainers and FAIR+CARE Council  

---

## 🕰️ Version History

| Version | Date       | Author            | Summary                                                                 |
|---------|------------|-------------------|-------------------------------------------------------------------------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Introduced Remote Sensing Lineage Schema Registry; formalized PROV-O, GeoSPARQL, CIDOC, and KFM lineage rules. |

---

<div align="center">

**Kansas Frontier Matrix — Remote Sensing Lineage Schemas**  
Semantically-Rich Provenance × FAIR+CARE Governance × Linked-Data Ready  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

</div>