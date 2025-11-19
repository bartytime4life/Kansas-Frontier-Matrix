---
title: "🧾 Kansas Frontier Matrix — Processed Metadata Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/processed/metadata/README.md"

version: "v11.0.0"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-processed-metadata-v11.0.0"
semantic_document_id: "kfm-doc-data-processed-metadata-readme"
event_source_id: "ledger:data/processed/metadata/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-processed-metadata-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0 / FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Domain Architecture"
intent: "processed-metadata-layer"
role: "metadata-domain"
category: "Data · Metadata · FAIR+CARE · Processed"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity_level: "Low"
indigenous_rights_flag: "Dataset-dependent"
public_exposure_risk: "Low"
redaction_required: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/data-processed-metadata-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/data-processed-metadata-readme-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative"
  - "unverified historical claims"

machine_extractable: true
classification: "Public Document"
jurisdiction: "Kansas / United States"
accessibility_compliance: "WCAG 2.1 AA"
ttl_policy: "Permanent"
sunset_policy: "Superseded upon next metadata-layer update"
---

<div align="center">

# 🧾 Kansas Frontier Matrix — Processed Metadata Layer  
`data/processed/metadata/README.md`

Central repository for **FAIR+CARE-certified metadata collections** documenting all processed datasets in the **Kansas Frontier Matrix (KFM)**.

This layer guarantees:

- 🔍 Discoverability via **STAC 1.x** and **DCAT 3.0**  
- 🧬 Provenance integrity via **PROV-O** and **ISO 19115**  
- ⚖️ Governance traceability via FAIR+CARE JSON-LD metadata  
- 📊 Telemetry-backed certification for validation and sustainability  

</div>

---

## 1. 📘 Overview

The **Processed Metadata Layer** is the **single source of truth** for metadata describing:

- Processed datasets under `data/processed/**`  
- Their schemas, checksums, FAIR+CARE status, and provenance  
- Their entries in **STAC collections** and **DCAT catalogs**  

Each record:

- Aligns with STAC 1.x, DCAT 3.0, ISO 19115, and PROV-O  
- Is recorded in governance-ledger-aligned structures  
- Is referenced by CI/CD, Focus Mode, and registry tooling  

---

## 2. 🗂️ Directory Layout (GitHub-Safe)

~~~~text
data/processed/metadata/
├── README.md                       ← this file
│
├── stac_collection.json            ← STAC 1.x collection for processed datasets
├── dcat_catalog.json               ← DCAT 3.0 catalog of processed datasets/distributions
├── provenance_manifest.json        ← PROV-O / ISO 19115 lineage manifest (graph-friendly JSON-LD)
├── governance_certification.json   ← FAIR+CARE governance certification summary (JSON-LD)
├── metadata_summary.csv            ← Human-readable inventory (dataset → metadata refs)
└── metadata.json                   ← Internal context: checksums, schema versions, governance links
~~~~

---

## 3. 🧭 Metadata Summary Table

| Metadata Record         | Domains Covered                                  | Schema/Model              | Status        | Certified By          | License   |
|-------------------------|--------------------------------------------------|---------------------------|---------------|-----------------------|-----------|
| `stac_collection.json`  | Spatial, Climate, Hazards, Hydrology, Landcover | STAC 1.x                  | ✅ Certified   | `@kfm-data`           | CC-BY 4.0 |
| `dcat_catalog.json`     | Tabular, Spatial, Landcover, Metadata           | DCAT 3.0 JSON-LD          | ✅ Certified   | `@kfm-governance`     | CC-BY 4.0 |
| `provenance_manifest.json` | All processed domains                       | PROV-O · ISO 19115        | ✅ Certified   | `@kfm-security`       | CC-BY 4.0 |
| `governance_certification.json` | FAIR+CARE governance summary          | FAIR+CARE JSON-LD         | ✅ Certified   | `@faircare-council`   | CC-BY 4.0 |
| `metadata_summary.csv`  | Aggregated registry                             | KFM Metadata v11          | ✅ Maintained | `@kfm-metadata-lab`   | CC-BY 4.0 |

---

## 4. 🧩 Example Processed Metadata Registry Entry

~~~~json
{
  "id": "processed_metadata_registry_v11.0.0",
  "schemas": ["STAC 1.x", "DCAT 3.0", "PROV-O", "ISO 19115"],
  "datasets_covered": ["climate", "hazards", "hydrology", "landcover", "tabular", "spatial"],
  "records_total": 196,
  "checksum_sha256": "sha256:d7b1c6a9e4f2b8c5a7e3d1f9c4b2a6e8d5c9a4e1f7b3d6a2e4c5f9b7a8e3d2f1",
  "fairstatus": "certified",
  "validator": "@kfm-metadata-lab",
  "license": "CC-BY 4.0",
  "created": "2025-11-19T23:05:00Z",
  "governance_ref": "docs/reports/audit/data_provenance_ledger.json"
}
~~~~

---

## 5. ⚙️ FAIR+CARE & Catalog Governance Workflow

~~~~mermaid
flowchart TD
    ASMB["Assembled Dataset Metadata"] --> VAL["Schema Validation\n(STAC · DCAT · PROV-O · ISO 19115)"]
    VAL --> CHK["Checksum Verification\n(SHA-256)"]
    CHK --> CERT["FAIR+CARE Governance Review\n(JSON-LD)"]
    CERT --> LEDGER["Ledger Synchronization\n(Provenance & Governance)"]
    LEDGER --> PUB["Catalog Publication\n(STAC/DCAT + Streaming STAC)"]
~~~~

### Workflow Stages

1. **Assemble metadata** from processed domain outputs.  
2. **Validate schemas** (STAC Items/Collections, DCAT Datasets, PROV-O JSON-LD).  
3. **Verify checksums** against file and manifest records.  
4. **Apply FAIR+CARE review** and embed CARE tags where necessary.  
5. **Write governance and provenance entries** to ledgers.  
6. **Publish to catalogs** (STAC, DCAT, Streaming STAC).

---

## 6. 📜 Metadata Files — Roles & Expectations

### 6.1 `stac_collection.json` (🌐 STAC Collection)

- Defines the high-level STAC Collection for processed datasets.  
- Includes links to Items for domains: climate, hazards, hydrology, landcover, etc.  
- Must pass STAC 1.x validation.  

### 6.2 `dcat_catalog.json` (📚 DCAT Catalog)

- DCAT 3.0 JSON-LD description of processed datasets.  
- Integrates into external portals and linked data ecosystems.  

### 6.3 `provenance_manifest.json` (🧬 Lineage Manifest)

- PROV-O + ISO 19115 lineage information for all processed datasets.  
- Used by graph ingestion and governance audit workflows.  

### 6.4 `governance_certification.json` (⚖️ Governance)

- FAIR+CARE Council certification summary.  
- Contains dataset-level governance decisions and CARE labels.  

### 6.5 `metadata_summary.csv` (🧾 Human Inventory)

- Simple table listing dataset → STAC/DCAT → provenance → checksum references.  

---

## 7. 🔐 Integrity & Checksum Records

Checksums for metadata artifacts are:

- Calculated with SHA-256  
- Recorded in:

~~~~text
data/checksums/manifest.json
data/archive/2025Q4/checksums/metadata_checksums.json
~~~~

Each file must have:

- Exact `path`  
- `checksum` using prefix `sha256-`  
- A `validated` flag and timestamp  

---

## 8. 🧠 FAIR+CARE Governance (Metadata Domain)

Metadata governance:

- Ensures catalog entries do not misrepresent or overpromise dataset content.  
- Tracks usage restrictions and sensitivities via FAIR+CARE tags.  
- References data-level governance for sensitive domains (e.g., hazards, cultural sites).  

FAIR+CARE summaries stored in:

~~~~text
data/processed/metadata/governance_certification.json
docs/reports/fair/data_care_assessment.json
~~~~

---

## 9. ♻️ Telemetry & Sustainability

Metadata processing contributes to sustainability metrics:

- `energy_wh` spent generating and validating metadata  
- `carbon_gCO2e` estimated for metadata jobs  
- `records_total` and `catalog_size` metrics  

Telemetry bundles:

~~~~text
releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/data-processed-metadata-v11.json
~~~~

---

## 10. 🔗 Integration with Other Layers

The Processed Metadata Layer connects:

- **Data** → `data/processed/**`  
- **Checksums** → `data/checksums/**`  
- **Archive** → `data/archive/2025Q4/**`  
- **Graph** → Neo4j ingestion of provenance entities  
- **Focus Mode** → uses metadata for narrative citations and overlays  

All domain READMEs must reference this layer when describing STAC/DCAT and provenance behavior.

---

## 11. 🧾 Internal Citation

~~~~text
Kansas Frontier Matrix (2025). Processed Metadata Layer (v11.0.0).
Unified FAIR+CARE-certified metadata registry for all processed datasets, integrating
STAC 1.x, DCAT 3.0, ISO 19115, and PROV-O lineage for ethical, transparent, and
reproducible open data governance in the Kansas Frontier Matrix.
~~~~

---

## 12. 🕰 Version History

| Version | Date       | Summary                                                                                           |
|--------:|------------|---------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-19 | Full v11 upgrade: STAC/DCAT/PROV-O/ISO 19115 alignment, telemetry v4 wiring, governance v11.     |
| v10.2.2 | 2025-11-12 | Streaming STAC sync, telemetry v2 upgrades, Focus Mode v2.1 citations and ethics flags added.     |
| v10.0.0 | 2025-11-09 | Initial processed metadata layer spec; STAC/DCAT/PROV-O baseline with ISO 19115 lineage.         |

<div align="center">

**Kansas Frontier Matrix — Processed Metadata Layer**  
🧾 Metadata Transparency · ⚖️ FAIR+CARE Ethics · 🧬 Provenance Integrity · 🌐 Catalog Interoperability  

[⬅️ Back to Processed Layer](../README.md) ·  
[📐 Data Architecture](../../ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>