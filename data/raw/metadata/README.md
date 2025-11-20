---
title: "📚 Kansas Frontier Matrix — Raw Data Metadata Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/metadata/README.md"

version: "v11.0.0"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-raw-metadata-registry-v11.0.0"
semantic_document_id: "kfm-doc-data-raw-metadata-readme"
event_source_id: "ledger:data/raw/metadata/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-metadata-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "Open Data Commons / FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Domain Architecture"
intent: "raw-metadata-registry"
role: "raw-metadata-domain"
category: "Data · Metadata · FAIR+CARE · Raw"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk (source-dependent exceptions)"
sensitivity_level: "Low–Moderate"
indigenous_rights_flag: "Dataset-dependent"
public_exposure_risk: "Dataset-dependent"
redaction_required: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low–Moderate"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/data-raw-metadata-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/data-raw-metadata-readme-v11-shape.ttl"

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
sunset_policy: "Superseded upon next raw-metadata-layer update"
---

<div align="center">

# 📚 Kansas Frontier Matrix — **Raw Data Metadata Registry**  
`data/raw/metadata/README.md`

**Purpose**  
Central repository for:

- 🧬 Source-level provenance manifests  
- 🧾 Checksum registries  
- ⚖️ FAIR+CARE pre-audit metadata  
- 🌐 STAC / DCAT / ISO 19115 crosswalks  

for all **raw (unaltered) datasets** in the Kansas Frontier Matrix (KFM).

This registry ensures:

- Transparent lineage for every raw dataset  
- License & ethics compliance  
- Interoperable metadata for catalogs and graph APIs  

</div>

---

## 1. 📘 Overview

The **Raw Metadata Layer** documents the **who / what / where / when / how** of all incoming datasets at the **raw layer**.

It is the **single source of truth** for:

- Provenance and attribution  
- Licensing and consent conditions  
- Checksum and integrity status  
- FAIR+CARE pre-audits (sensitivity, community impact, ethical notes)  
- STAC / DCAT / ISO 19115 metadata mapping  

All downstream layers (staging, processed, archive, graph) **depend** on this registry for trustworthy lineage.

---

## 2. 🗂️ Directory Layout (GitHub-Safe)

~~~~text
data/raw/metadata/
├── README.md                       ← this file
│
├── provenance.json                 ← source acquisition lineage & metadata records
├── checksums.json                  ← SHA-256 checksums and integrity results
├── faircare_preaudit.json          ← FAIR+CARE pre-audit summary for all raw domains
├── stac_catalog.json               ← STAC 1.x catalog for raw data assets
├── dcat_catalog.json               ← DCAT 3.0 export for external interoperability
└── metadata_index.json             ← unified registry (JSON-LD provenance contexts)
~~~~

Each file plays a distinct role in the metadata and governance ecosystem.

---

## 3. 🧬 Example Metadata Index Record

~~~~json
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "id": "raw_data_metadata_registry_v11.0.0",
  "source_domains": ["climate", "hydrology", "hazards", "terrain", "text", "tabular"],
  "checksum_records": 312,
  "fairstatus": "pre-certified",
  "records_updated": "2025-11-19T21:45:00Z",
  "validator": "@kfm-metadata-lab",
  "governance_registered": true,
  "provenance_graph": "data/raw/metadata/provenance.json",
  "linked_catalogs": {
    "stac": "data/raw/metadata/stac_catalog.json",
    "dcat": "data/raw/metadata/dcat_catalog.json"
  },
  "governance_ref": "docs/reports/audit/data_provenance_ledger.json"
}
~~~~

---

## 4. ⚙️ FAIR+CARE Governance Matrix

| Principle            | Implementation                                                        | Oversight              |
|----------------------|------------------------------------------------------------------------|------------------------|
| 🔍 **Findable**      | STAC/DCAT metadata indexed by dataset UUID, domain, and provider.     | `@kfm-data`            |
| 🔓 **Accessible**    | JSON-LD and CSV exports openly available for review.                  | `@kfm-accessibility`   |
| 🔗 **Interoperable** | Dual exports using STAC 1.x and DCAT 3.0 schemas.                     | `@kfm-architecture`    |
| 🔁 **Reusable**      | Includes provenance, checksums, licenses, and FAIR+CARE context.      | `@kfm-design`          |
| 🤝 **Collective Benefit** | Open metadata strengthens reproducibility and trust.            | `@faircare-council`    |
| 🛡️ **Authority**     | Council certifies metadata accuracy & ethical compliance.             | `@kfm-governance`      |
| 📋 **Responsibility**| Validators maintain lineage and checksum integrity.                   | `@kfm-security`        |
| 🧠 **Ethics**        | Sensitive datasets flagged; ethical considerations documented.        | `@kfm-ethics`          |

---

## 5. 🧠 Metadata Validation & Publication

| Process               | Description                                                | Output Path                                   |
|-----------------------|------------------------------------------------------------|-----------------------------------------------|
| **Checksum Audit**    | Verifies integrity of raw datasets (SHA-256).             | `data/raw/metadata/checksums.json`           |
| **Provenance Log**    | Records who/where/when/how for each dataset.              | `data/raw/metadata/provenance.json`          |
| **FAIR+CARE Pre-Audit** | Captures sensitivity, license & ethics pre-checks.     | `data/raw/metadata/faircare_preaudit.json`   |
| **Catalog Generation**| Publishes STAC/DCAT catalogs for discovery.               | `data/raw/metadata/stac_catalog.json`, `dcat_catalog.json` |
| **Index Assembly**    | Builds unified JSON-LD registry & crosswalk.              | `data/raw/metadata/metadata_index.json`      |

Automations:

- `metadata_sync.yml` — continuous synchronization to governance ledger & telemetry feeds.  

---

## 6. 🧾 Example FAIR+CARE Pre-Audit Entry

~~~~json
{
  "dataset_id": "noaa_precipitation_daily_2025",
  "domain": "climate",
  "license": "Public Domain (NOAA)",
  "sensitivity": "none",
  "indigenous_context": false,
  "community_flags": [],
  "consent_token": null,
  "reviewed_by": "@kfm-metadata-lab",
  "reviewed_on": "2025-11-19T20:00:00Z",
  "notes": "Standard NOAA CPC open data; no additional constraints."
}
~~~~

---

## 7. 🔐 Retention & Integrity Policy

| Data Type             | Retention | Policy                                         |
|-----------------------|----------:|-----------------------------------------------|
| Provenance Logs       | Permanent | Immutable lineage tracking (ISO 19115).       |
| Checksum Records      | Permanent | Long-term data integrity evidence.            |
| FAIR+CARE Pre-Audits  | 5 Years   | Periodic review under Council oversight.      |
| STAC/DCAT Catalogs    | Permanent | Continuously updated via streaming bridge.    |
| Metadata Index        | Permanent | Always reflects latest snapshot + history.    |

Retention is governed by:

~~~~text
data/raw/metadata/raw_data_retention.yml
~~~~

---

## 8. 🌱 Telemetry & Sustainability

The metadata registry is part of the **observability fabric**:

Tracked metrics:

- `metadata_records_total`  
- `checksum_coverage_ratio`  
- `fairstatus_distribution`  
- `schema_validation_failures`  
- `energy_wh` and `carbon_gCO2e` for metadata jobs  

Telemetry exported to:

~~~~text
releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/data-raw-metadata-v11.json
~~~~

Used by:

- Governance dashboards  
- Reliability & sustainability reports  
- Focus Mode “system introspection” Story Nodes  

---

## 9. 🧾 Internal Use Citation

~~~~text
Kansas Frontier Matrix (2025). Raw Data Metadata Registry (v11.0.0).
Centralized metadata registry for provenance, checksums, and FAIR+CARE pre-audits
of unaltered raw datasets in the Kansas Frontier Matrix. Implements JSON-LD,
STAC 1.x, DCAT 3.0, and ISO 19115 lineage patterns for transparent, ethical,
and reproducible open data governance.
~~~~

---

## 10. 🕰 Version History

| Version | Date       | Author       | Summary                                                                                   |
|--------:|------------|--------------|-------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-19 | `@kfm-data`  | Full v11 upgrade; telemetry v4, JSON-LD contexts v11, ROOT-GOVERNANCE alignment.         |
| v10.2.2 | 2025-11-12 | `@kfm-data`  | Added JSON-LD provenance graphs, Streaming STAC links, telemetry v2, FAIR+CARE expansion.|
| v10.0.0 | 2025-11-09 | `@kfm-data`  | Established unified registry; added checksum and DCAT support.                            |
| v9.7.0  | 2025-11-06 | `@kfm-data`  | Initial FAIR+CARE pre-audit registry; governance integration.                             |

<div align="center">

**Kansas Frontier Matrix — Raw Metadata Registry**  
📚 Metadata Transparency · ⚖️ FAIR+CARE Ethics · 🧬 Provenance Integrity  

[⬅️ Back to Raw Data Index](../README.md) ·  
[📐 Data Architecture](../ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
