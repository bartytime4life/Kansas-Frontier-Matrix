---
title: "🌐 Kansas Frontier Matrix — Pipeline Publishing Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/pipelines/publishing-guide.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-publishing-guide-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
kfm_markdown_protocol: "docs/standards/kfm_markdown_output_protocol.md"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Pipeline Publishing Guide**  
`docs/guides/pipelines/publishing-guide.md`

**Purpose:**  
Provide the authoritative publishing workflow for all KFM pipelines — including **STAC**, **DCAT**, **Neo4j**, **RDF/GeoSPARQL**, and **public data release promotion** — ensuring **FAIR+CARE**, **lineage**, **provenance**, and **MCP-DL v6.3** compliance.

This guide defines how validated data becomes official KFM **published assets**.

<img alt="Publish" src="https://img.shields.io/badge/Publish-STAC·DCAT·Neo4j·RDF-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="Linked Data" src="https://img.shields.io/badge/Linked_Data-GeoSPARQL-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

Publishing represents the **final and irreversible step** of a KFM pipeline.

Published assets MUST be:

- FAIR+CARE–certified  
- Fully validated (GX + schema + governance)  
- Lineage-complete  
- Telemetry-linked  
- Immutable (version-locked)  
- Discoverable via **STAC**, **DCAT**, **Neo4j**, and **Linked Data endpoints**  

Only data in `data/processed/` may be published.

---

## 🗂️ Directory Layout (Publishing Layer)

~~~~~text
data/
├── processed/                           # Finished FAIR+CARE-approved datasets
├── stac/
│   ├── published/
│   │   ├── items/<collection>/<id>.json
│   │   └── collections/<collection>.json
├── dcat/
│   └── datasets/<dataset>.jsonld
├── rdf/
│   └── <dataset>/<version>/*.ttl
└── lineage/
    └── <dataset>/<version>.jsonld
~~~~~

---

## 🧩 Publishing Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Staging → Processed<br/>Validated · CARE-labeled · Checksum-locked"] --> B["Publish Gate<br/>FAIR+CARE + Provenance Checks"]
  B -->|PASS| C["Write STAC Items/Collections"]
  B -->|PASS| D["Write DCAT Datasets<br/>JSON-LD"]
  B -->|PASS| E["Upsert Neo4j Graph Nodes<br/>Scene · Event · Place"]
  B -->|PASS| F["Export RDF<br/>GeoSPARQL Linked Data"]
  F --> G["Governance Ledger<br/>Append Entry"]
  G --> H["Telemetry Export<br/>Publish Metrics"]
~~~~~

---

# 🛠 1. Publishing Gate Requirements

No dataset may be published unless ALL of the following are true:

### Validation Requirements
- GX validation: **ALL PASS**, **no warnings**  
- Schema validation: STAC/DCAT/JSONSchema complete  
- CARE checks: no unresolved sovereignty or masking violations  
- Provenance: lineage JSON-LD valid  
- Telemetry: required fields present  

### Required Metadata
Each published asset MUST include:

| Field | Description |
|-------|-------------|
| `kfm:version` | Semantic dataset version |
| `kfm:processingSteps[]` | full pipeline trace |
| `kfm:checksum_sha256` | integrity lock |
| `kfm:careLabel` | public / sensitive / restricted |
| `kfm:maskingStrategy` | required for sensitive+restricted |
| `kfm:lineageRef` | path to JSON-LD lineage |
| `kfm:telemetryRef` | NDJSON summary |
| `kfm:provenanceRef` | governance ledger link |

### Mandatory Inputs

Only datasets under:

~~~~~text
data/processed/<dataset>/<version>/
~~~~~

are eligible for publication.

---

# 📦 2. STAC Publishing

Publishing requires writing:

### 2.1 Collections

~~~~~text
data/stac/published/collections/<collection_id>.json
~~~~~

Requirements:

- Complete STAC 1.0 structure  
- Valid spatial & temporal extents  
- Asset summaries  
- Provider metadata  
- License, citation, DOIs  
- CARE extensions embedded  
- Links:  
  - `root`  
  - `self`  
  - `items`  

### 2.2 Items

~~~~~text
data/stac/published/items/<collection_id>/<item_id>.json
~~~~~

Each Item MUST:

- Include normalized geometry  
- Include datetime, bbox, EO/SAR fields  
- Reference lineage and telemetry  
- Include `kfm:ingest_version` & `kfm:publish_version`  
- Be checksum-locked  

---

# 📚 3. DCAT Publishing

Each dataset generates a **DCAT Dataset JSON-LD**:

~~~~~text
data/dcat/datasets/<dataset_id>.jsonld
~~~~~

Must include:

- `dct:title`, `dct:description`  
- `dct:creator`, `dct:publisher`  
- `dct:temporal`, `dct:spatial`  
- `dct:provenance` (lineageRef)  
- `dct:license`  
- `dcat:distribution` referencing STAC assets  
- CARE statements  

DCAT exports must pass CI validator:  
`dcat-validate.yml`

---

# 🌐 4. Neo4j Publishing

Publishing requires updating graph entities:

### Scene Nodes
`(:Scene {id})`

Set:

- `datetime`  
- `collection`  
- `cloud_cover`  
- `centroid` (POINT)  
- `geom` (WKT or GeoJSON)  
- `aoi_overlaps[]`  
- CARE flags  

### Dataset Nodes
`(:Dataset {id})`

- Version  
- Title  
- License  
- STAC/ DCAT references  

### Relationships

- `(:Scene)-[:INTERSECTS]->(:County)`  
- `(:Scene)-[:WITHIN]->(:AOI)`  
- `(:Scene)-[:HAS_DERIVATIVE]->(:IndexLayer)`  

All writes must be **idempotent**:

~~~~~text
MERGE … ON MATCH SET …
~~~~~

Graph writes must occur **after** lineage has been generated.

---

# 🌐 5. RDF / GeoSPARQL Publishing

Generated per dataset:

~~~~~text
data/rdf/<dataset>/<version>/*.ttl
~~~~~

Includes:

- scene features  
- geometry (`geo:asWKT`)  
- AOI relationships (`geo:sfIntersects`)  
- provenance (`prov:wasGeneratedBy`)  
- dataset → STAC/DCAT MADS mappings  

Graphs must validate with:

- `geosparql_context.jsonld`
- `prov_o_context.jsonld`
- `cidoc_crm_context.jsonld`

CI enforcement: `linked-data-validate.yml` (future)

---

# 🧬 6. Lineage & Provenance Integration

Every published dataset MUST link:

- STAC files → lineageRef  
- DCAT → lineageRef  
- Neo4j nodes → lineage attributes  
- RDF → lineage metadata  

Lineage stored at:

~~~~~text
data/processed/lineage/<dataset>/<version>.jsonld
~~~~~

Validated against:

~~~~~text
src/pipelines/remote-sensing/lineage/schemas/lineage.schema.json
~~~~~

---

# 📡 7. Telemetry Integration

Every publishing pipeline MUST emit NDJSON containing:

- `stage: "publish"`  
- `items_published`  
- `collections_updated`  
- `graph_nodes_written`  
- `rdf_files_written`  
- `energy_wh`, `co2_g`  
- `care_violations`  
- `duration_ms`  

Stored at:

~~~~~text
data/processed/telemetry/<pipeline>.ndjson
~~~~~

Aggregated to:

~~~~~text
../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

# 🛡 8. Governance Ledger Integration

Every publish event MUST append to:

~~~~~text
docs/reports/audit/data_provenance_ledger.json
~~~~~

Fields recorded:

- dataset ID  
- version  
- CARE label / masking strategy  
- lineageRef  
- telemetryRef  
- stacRef / dcatRef / graphRef / rdfRef  
- sbomRef  
- slsaRef  
- CI workflow IDs  

Governance ledger entries are **append-only**.

---

# 🔒 9. CI Enforcement

The following workflows **must pass** before publication:

| Workflow | Responsibility |
|----------|----------------|
| `stac-validate.yml` | STAC schema validation |
| `dcat-validate.yml` | DCAT JSON-LD validation |
| `neo4j-schema-guard.yml` | Graph constraints & node shape |
| `faircare-validate.yml` | CARE & governance compliance |
| `telemetry-export.yml` | Metadata & telemetry completeness |
| `docs-lint.yml` | KFM Markdown rules |
| `sbom-validate.yml` | Match SBOM to published artifacts |
| `slsa-verify.yml` | Provenance attestation validation |

Merge is blocked unless **all** are green.

---

# 🧭 10. Developer Publishing Checklist

Before running publish:

- [ ] Staging → Processed promotion succeeded  
- [ ] All GX validation passed  
- [ ] CARE masking applied & verified  
- [ ] Sovereignty overlays checked  
- [ ] Lineage JSON-LD generated & validated  
- [ ] Telemetry NDJSON complete  
- [ ] Checksums verified  
- [ ] STAC/DCAT metadata complete  
- [ ] RDF exports valid  
- [ ] Neo4j writes tested  
- [ ] Governance ledger updated  

---

## 🕰️ Version History

| Version | Date       | Author               | Summary |
|---------|------------|----------------------|---------|
| v10.3.1 | 2025-11-14 | Publishing Governance Team | Initial Publishing Guide; full STAC/DCAT/Neo4j/RDF/CARE integration. |

---

<div align="center">

**Kansas Frontier Matrix — Publishing Guide**  
FAIR+CARE Publishing × Immutable Provenance × STAC/DCAT/Graph/RDF Harmony  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

</div>

