---
title: "🔐 Kansas Frontier Matrix — Data Checksums & Integrity Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/checksums/README.md"

version: "v11.0.0"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-checksums-readme-v11.0.0"
semantic_document_id: "kfm-doc-data-checksums-readme"
event_source_id: "ledger:data/checksums/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/data-checksums-v11.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "data-checksums-registry"
role: "integrity-registry"
category: "Data · Integrity · Provenance"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity_level: "Mixed"
public_exposure_risk: "Dataset-level"
indigenous_rights_flag: "Dataset-level"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: false

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/data-checksums-readme-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/data-checksums-readme-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next integrity-registry update"
---

<div align="center">

# 🔐 Kansas Frontier Matrix — Data Checksums & Integrity Registry  
`data/checksums/README.md`

**Purpose**  
Describe the **checksum verification system**, integrity tracking, and provenance linkage for all datasets and releases in the **Kansas Frontier Matrix (KFM)**.  

Every artifact—from raw dataset to release bundle—is:

- Cryptographically signed (SHA-256)  
- Registered into governance ledgers  
- Cross-checked with SBOM and release manifests  
- Integrated with FAIR+CARE governance and sustainability telemetry  

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue.svg)](#)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen.svg)](#)  
[![FAIR+CARE Certified](https://img.shields.io/badge/FAIR%2BCARE-Integrity%20Certified-gold.svg)](#)  
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)](#)

</div>

---

## 1. 📘 Overview

The **Checksum Integrity Registry** keeps **SHA-256 manifests** for:

- Datasets under `data/**`  
- STAC/DCAT metadata files  
- Release artifacts (`manifest.zip`, STAC catalogs, DCAT catalogs)  
- Other critical files (e.g., data contracts, ontology schemas)  

Checksums serve as **verifiable fingerprints** that bind:

- Data files  
- Release manifests  
- SBOM entries  
- Governance and FAIR+CARE certifications  

Core objectives:

- Detect unauthorized modifications or corruption  
- Provide public verifiability of all releases  
- Support reproducibility of historical analysis  
- Feed integrity signals into governance, telemetry, and dashboards  

---

## 2. 🧭 System Architecture

~~~~mermaid
flowchart TD
    ETL["ETL & Validation Pipelines"]
      --> GEN["Checksum Generator\n(SHA-256)"]
    GEN --> REG["Integrity Registry\n(data/checksums/*.json)"]
    REG --> LED["Governance Ledger\n(docs/reports/audit/data_provenance_ledger.json)"]
    REG --> SBOM["SBOM & manifest\n(releases/v11.0.0)"]
    SBOM --> PUB["Public Release Verification"]
~~~~

### Flow Description

1. **Generation**  
   - Pipelines compute checksums after ETL or file generation.  

2. **Registration**  
   - Checksums written to **manifest files** in `data/checksums/`.  
   - SBOM verification ensures coverage and consistency.  

3. **Governance Linking**  
   - Governance ledger entries reference checksum IDs and manifests.  

4. **Publication & Verification**  
   - Releases include a verifiable checksum set that enables public integrity checks.  

---

## 3. 🗂️ Directory Layout (Checksums)

~~~~text
data/checksums/
├── README.md                    ← this file
├── manifest.json                ← master SHA-256 manifest for core datasets
├── processed_datasets.json      ← checksums for FAIR+CARE-certified outputs
├── staging_datasets.json        ← checksums for normalized/staging artifacts
├── work_datasets.json           ← checksums for ETL workspaces (optional)
└── release_hashes.json          ← checksums mapped to SBOM + manifest.zip entries
~~~~

Rules:

- `manifest.json` is a **canonical index** of checksums for key datasets.  
- Other files split responsibility by lifecycle stage (processed, staging, work, releases).  
- All JSON files must conform to the `data-checksums-readme-v11` schema or sub-schemas.  

---

## 4. ⚙️ Manifest Structure

All manifests share a common core structure with versioning and algorithm metadata.

~~~~json
{
  "version": "v11.0.0",
  "generated_on": "2025-11-19T19:25:00Z",
  "hash_algorithm": "SHA-256",
  "datasets": [
    {
      "id": "hazards_processed_v11.0.0",
      "path": "data/processed/hazards/hazards_composite_v11.0.0.geojson",
      "checksum": "sha256-2f1e3b8c97df84b5d2c3e39bbd95b9e8d12b64ad38a62400f745d68ec6d1b75e",
      "fairstatus": "certified",
      "governance_ref": "docs/reports/audit/data_provenance_ledger.json",
      "stac_ref": "data/stac/items/hazards_v11_2025Q4.json",
      "dcat_ref": "data/dcat/hazards_v11_2025Q4.jsonld"
    },
    {
      "id": "climate_staging_v11.0.0",
      "path": "data/staging/climate/climate_aggregate_v11.0.0.parquet",
      "checksum": "sha256-a8373fa4d12d49be5f5f2178a91d79981b1d28b947f05eaa52e9e7e8d2cfadcd",
      "fairstatus": "pending"
    }
  ]
}
~~~~

**Checksum format**: always `sha256-<hex>`.

Required fields per dataset:

- `id`  
- `path`  
- `checksum`  
- `fairstatus`  

Optional but recommended:

- `governance_ref`  
- `stac_ref`, `dcat_ref`  

---

## 5. 🧠 FAIR+CARE Integrity Governance

Checksums are tightly integrated with FAIR+CARE:

| Principle              | Implementation                                                   | Verified By          |
|------------------------|------------------------------------------------------------------|----------------------|
| **Findable**           | Checksums referenced in STAC/DCAT and release manifests         | @kfm-data            |
| **Accessible**         | JSON checksum manifests published under CC-BY 4.0               | @kfm-accessibility   |
| **Interoperable**      | Structures compatible with SPDX, STAC, and DCAT                 | @kfm-architecture    |
| **Reusable**           | Immutable, versioned logs with provenance links                  | @kfm-governance      |
| **Collective Benefit** | Public can independently verify dataset integrity                | @faircare-council    |
| **Authority to Control** | Governance Council defines checksum coverage & policies       | @kfm-governance      |
| **Responsibility**     | Telemetry-backed coverage and periodic re-verification           | @kfm-security        |
| **Ethics**             | Integrity guarantees prevent tampering with ethically sensitive data | @kfm-ethics     |

Governance ledger entries link checksum records to FAIR+CARE decisions and data contracts.

---

## 6. 🧮 Validation Workflows

Workflows (in `.github/workflows/`) ensure checksums are correct and in sync:

| Workflow               | Description                                      | Primary Outputs                                                      |
|------------------------|--------------------------------------------------|----------------------------------------------------------------------|
| `checksum-verify.yml`  | Generates & verifies SHA-256 hashes              | `data/checksums/manifest.json`, per-stage checksum files            |
| `faircare_validate.yml`| Ensures checksum processes respect FAIR+CARE     | `docs/reports/fair/faircare_summary.json`                           |
| `governance-ledger.yml`| Aligns checksum records with governance ledger   | `docs/reports/audit/data_provenance_ledger.json`                    |
| `sbom_verify.yml`      | Confirms checksums match SPDX SBOM and manifest  | `releases/v11.0.0/sbom.spdx.json`, `releases/v11.0.0/manifest.zip`  |

These workflows are required for merges affecting:

- `data/checksums/**`  
- `releases/**`  
- `sbom_ref` or `manifest_ref`  

---

## 7. 📊 Example CLI Verification

Users can perform local verification using standard tools.

~~~~bash
# 1) Compute checksum locally
sha256sum data/processed/hazards/hazards_composite_v11.0.0.geojson

# 2) Look up expected checksum in manifest
jq '.datasets[] | select(.id=="hazards_processed_v11.0.0")' data/checksums/manifest.json

# 3) Compare output manually or via script
~~~~

Scripts in `tools/validation/` can automate these comparisons as part of a continuous verification routine.

---

## 8. 🌱 Sustainability & Integrity Metrics

Sustainability and integrity metrics captured by telemetry:

| Metric              | Target                       | Verified By               |
|---------------------|-----------------------------|---------------------------|
| Checksum Coverage   | 100% of released datasets    | @kfm-validation           |
| Governance Sync     | 100% of archived datasets    | @kfm-governance           |
| SBOM Parity         | ≥ 99.9% SBOM–manifest match  | @kfm-architecture         |
| Energy per Batch    | ≤ 10 Wh per checksum batch   | @kfm-sustainability       |
| FAIR+CARE Compliance| Certified processes only     | @faircare-council         |

Telemetry is exported to:

~~~~text
../../releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/data-checksums-*.json
~~~~

---

## 9. 🗂️ Naming & Conventions

- **Datasets**: `<domain>_<layer>_v<semver>.<ext>`  
  - e.g., `hazards_composite_v11.0.0.geojson`  
- **Checksum IDs**: `<dataset_id>`, matching STAC/DCAT IDs where applicable  
- **Checksum field**: Required `checksum` field in all manifest files, `sha256-...` format  

Immutability:

- Once a release is finalized and tagged, its checksum entries are **never overwritten**.  
- Any corrections result in **additional records** with clear references to superseded entries.

---

## 10. 🧾 Internal Citation

~~~~text
Kansas Frontier Matrix (2025). Data Checksums & Integrity Registry (v11.0.0).
Checksum governance, cryptographic verification, and FAIR+CARE-integrated integrity
processes for KFM datasets and releases. Ensures dataset immutability, reproducibility,
and public verifiability across versions.
~~~~

---

## 11. 🕰️ Version History

| Version | Date       | Author       | Summary                                                                                      |
|--------:|------------|--------------|----------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-19 | @kfm-data    | Upgraded to v11; added sustainability telemetry v4, ROOT-GOVERNANCE link, and ontology hooks.|
| v10.2.2 | 2025-11-12 | @kfm-data    | Aligned with v10.2 release; SBOM/manifest linkage, JSON-LD guidance, CLI examples, telemetry.|
| v10.0.0 | 2025-11-10 | @kfm-data    | Baseline registry; governance mapping, manifest examples, and metrics.                       |

<div align="center">

**Kansas Frontier Matrix — Data Checksums & Integrity Registry**  
*Data Integrity × FAIR+CARE Trust × Sustainable Provenance*  

© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Data Architecture](../ARCHITECTURE.md) · [Back to Data Index](../README.md) · [Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
