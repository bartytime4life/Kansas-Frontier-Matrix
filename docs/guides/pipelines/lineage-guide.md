---
title: "🧬 Kansas Frontier Matrix — Lineage & Provenance Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/pipelines/lineage-guide.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-lineage-guide-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
kfm_markdown_protocol: "docs/standards/kfm_markdown_output_protocol.md"
---

<div align="center">

# 🧬 **Kansas Frontier Matrix — Lineage & Provenance Guide**  
`docs/guides/pipelines/lineage-guide.md`

**Purpose:**  
Define how every KFM pipeline produces **verifiable, machine-readable, FAIR+CARE-governed lineage** using **PROV-O**, **CIDOC-CRM**, and **OGC GeoSPARQL**, ensuring that every dataset, raster, vector, STAC Item, neo4j node, and RDF export is **traceable**, **auditable**, and **reproducible**.

This guide governs ALL ingestion, preprocessing, analytics, validation, promotion, and publishing pipelines.

</div>

---

## 📘 Overview

Lineage is the **binding layer** between:

- FAIR+CARE governance  
- Telemetry  
- STAC/DCAT metadata  
- Neo4j graph semantics  
- RDF/GeoSPARQL linked data  
- Pipeline reproducibility  

Every KFM dataset is required to include:

- Lineage JSON-LD  
- Provenance links to source datasets  
- Processing & transformation chains  
- Checksums  
- Telemetry references  
- CARE masking evidence  
- Governance ledger entry  

---

## 🗂️ Directory Layout (Lineage Layer)

~~~~~text
data/processed/lineage/
├── <dataset_id>/
│   └── <version>.jsonld             # PROV-O + GeoSPARQL + CIDOC lineage export
src/pipelines/remote-sensing/lineage/
├── schemas/
│   └── lineage.schema.json          # Required schema for all lineage bundles
~~~~~

---

## 🧬 Required Lineage Model

Every lineage bundle MUST conform to:

- **W3C PROV-O**
- **CIDOC CRM** (for historical, cultural, contextual meaning)
- **OGC GeoSPARQL** (for geospatial semantics)
- **KFM CARE Extensions**
- **KFM Telemetry Extensions**

### Core Entities

| Entity | Description |
|--------|-------------|
| `prov:Entity` | A dataset, raster, vector, STAC Item, document, or derived output |
| `prov:Activity` | A processing step (ingest, preprocess, analytics, validate, publish) |
| `prov:Agent` | Pipeline executor (system), data provider, AI module |
| `geo:Feature` | Spatial asset with geometry |
| `crm:E5_Event` | Historical/cultural events (if linked) |
| `kfm:CARE` | Governance & masking metadata |
| `kfm:Telemetry` | Summaries connected to lineage |

---

## 🧩 Lineage Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Source Datasets<br/>STAC · Raster · Vector"] --> B["Pipeline Activities<br/>Ingest · Preprocess · Analytics"]
  B --> C["Validation Gate<br/>GX · FAIR+CARE"]
  C --> D["Promotion<br/>Staging → Processed"]
  D --> E["Publishing<br/>STAC · DCAT · Neo4j · RDF"]
  E --> F["Lineage Export<br/>JSON-LD"]
  F --> G["Governance Ledger<br/>Append Entry"]
~~~~~

---

## 🧱 Lineage JSON-LD Structure

Every lineage bundle MUST include:

### 1. **Context Block (@context)**

~~~~~text
[
  "https://www.w3.org/ns/prov.jsonld",
  "https://schema.org/",
  "https://openspatial.org/contexts/geosparql.jsonld",
  "docs/contexts/kfm-care.context.jsonld",
  "docs/contexts/kfm-telemetry.context.jsonld"
]
~~~~~

### 2. **Entities**

Each input or output dataset must be defined:

~~~~~json
{
  "@id": "kfm:landsat_scene_2025_11_14_001",
  "@type": ["prov:Entity", "geo:Feature"],
  "kfm:checksum_sha256": "sha256-abc123...",
  "geo:asWKT": "POLYGON((...))",
  "kfm:careLabel": "public",
  "kfm:telemetryRef": "data/processed/telemetry/landsat_ingest.ndjson"
}
~~~~~

### 3. **Activities**

Each pipeline step becomes a PROV-O Activity:

~~~~~json
{
  "@id": "kfm:landsat_ingest_activity_2025_11_14",
  "@type": "prov:Activity",
  "prov:startedAtTime": "2025-11-14T03:11:21Z",
  "prov:endedAtTime": "2025-11-14T03:11:40Z",
  "kfm:processingSteps": ["stac_fetch","gsd_harmonize","rtc","bandstack"],
  "kfm:energy_wh": 11.4,
  "kfm:co2_g": 7.9
}
~~~~~

### 4. **Relations**

Required relations:

- `prov:used` (Activity → Entity)  
- `prov:generated` (Activity → Entity)  
- `prov:wasAssociatedWith` (Activity → Agent)  
- `prov:wasDerivedFrom` (Entity → Entity)  
- `geo:sfIntersects` for spatial relationships  
- `crm:P17_was_motivated_by` for historical/cultural context (where appropriate)  

---

## 🛡 CARE Integration

Lineage bundles MUST include:

- CARE labels  
- Masking strategies  
- Sovereignty flags  
- Sensitive geometry generalization evidence  

Example:

~~~~~json
{
  "kfm:careLabel": "sensitive",
  "kfm:maskingStrategy": "h3_generalize_r7",
  "kfm:sovereigntyFlags": ["tribal_land_overlap"]
}
~~~~~

---

## 📡 Telemetry Integration

Lineage MUST include:

- Telemetry reference  
- Telemetry summary fields inside Activity blocks  
- Performance, energy, carbon, masking, errors  

Telemetry validator (`telemetry-export.yml`) ensures consistency with:

~~~~~text
../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🔐 Governance Ledger Integration

Each lineage bundle MUST be appended to:

~~~~~text
docs/reports/audit/data_provenance_ledger.json
~~~~~

The ledger entry MUST include:

- Dataset ID  
- Version  
- CARE label  
- Lineage path  
- Telemetry path  
- STAC/DCAT/Graph references  
- SBOM & SLSA attestations  
- All pipeline workflow run IDs  

---

## 🧪 Validation Requirements

Lineage bundles MUST pass:

- `lineage.schema.json`  
- JSON-LD shape validation  
- PROV-O structure validation  
- GeoSPARQL geometry validation  
- CIDOC CRM structure (if historical linkages exist)  
- FAIR+CARE rules (governance validator)  

CI workflows:

- `lineage-validate.yml`  
- `faircare-validate.yml`  
- `linked-data-validate.yml` (future)  
- `telemetry-export.yml`  
- `docs-lint.yml`  

---

## 🧭 Local Build Pattern

~~~~~bash
python build_lineage.py \
  --input data/processed/<dataset>/<version> \
  --out data/processed/lineage/<dataset>/<version>.jsonld \
  --care-label sensitive
~~~~~

---

## 🪜 Example Lineage Bundle (Abbreviated)

~~~~~json
{
  "@context": ["prov", "geosparql", "kfm-care", "kfm-telemetry"],
  "@id": "kfm:landsat_scene_2025_11_14_001",
  "@type": ["prov:Entity", "geo:Feature"],
  "geo:asWKT": "POLYGON((...))",
  "kfm:careLabel": "public",
  "prov:wasDerivedFrom": "kfm:landsat_ingest_batch_2025_11_14",
  "prov:wasGeneratedBy": "kfm:landsat_ingest_activity_2025_11_14",
  "kfm:telemetryRef": "data/processed/telemetry/landsat_ingest.ndjson"
}
~~~~~

---

## 🕰 Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.3.1 | 2025-11-14 | Lineage Governance Team | Initial lineage guide with PROV-O, GeoSPARQL, CIDOC, CARE, telemetry, governance integration. |

---

<div align="center">

**Kansas Frontier Matrix — Lineage & Provenance Guide**  
Immutable Provenance × FAIR+CARE × PROV-O × GeoSPARQL × CIDOC CRM  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

</div>

