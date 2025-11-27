---
title: "📜 Kansas Frontier Matrix — Data Contracts & Schemas (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/contracts/README.md"
version: "v11.2.2"
last_updated: "2025-11-27"
review_cycle: "Continuous · FAIR+CARE Council"
release_stage: "Stable / Governed"
lifecycle: "LTS"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-contracts-v2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
status: "Active / Enforced"
doc_kind: "Schema"
header_profile: "standard"
footer_profile: "standard"
category: "Data · Contracts · Validation"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
ttl_policy: "12 months"
provenance_chain:
  - "docs/data/contracts/README.md@v10.0.0"
  - "docs/data/contracts/README.md@v11.0.0"
  - "docs/data/contracts/README.md@v11.1.0"
  - "docs/data/contracts/README.md@v11.2.1"
doc_integrity_checksum: "<sha256>"
---

<div align="center">

# 📜 **Kansas Frontier Matrix — Data Contracts & Schemas**  
`docs/data/contracts/README.md`

**Purpose**  
Define, enforce, and govern **data contracts, validation schemas, provenance standards, and FAIR+CARE requirements** for all KFM ETL pipelines, datasets, and knowledge-graph entities.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../README.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../standards/faircare/FAIRCARE-GUIDE.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../releases/v11.2.2/manifest.zip)

</div>

---

## 📘 Overview

KFM **data contracts** establish the required structure, metadata fields, provenance rules, and FAIR+CARE constraints that every dataset must satisfy before ingestion.

Contracts ensure:

- Deterministic ETL pipelines  
- Schema-safe Neo4j ingestion  
- Ethical + sovereign handling of cultural data  
- STAC/DCAT interoperability  
- Complete, traceable PROV-O lineage  

All datasets MUST conform to these contracts **before inclusion in the KFM knowledge graph**.

---

## 🗂️ Directory Layout

~~~text
docs/data/contracts/
├── 📄 README.md
├── 🧩 data-contract-v3.json
├── 🧾 metadata-schema.json
├── 🧬 provenance-spec.json
└── 📚 examples/
       ├── 🗺️ topo-map-contract-example.json
       ├── 🌦️ climate-data-contract-example.json
       └── 🧠 focus-narrative-contract-example.json
~~~

---

## ⚙️ Contract Components

| Component | Description | Format |
|----------|-------------|---------|
| **Metadata Schema** | Dataset identity, title, license, STAC/DCAT mappings | JSON Schema |
| **Entity Contract** | Defines entities/attributes in KFM (Place, Person, Event, Artifact, Document) | JSON Schema / RDF |
| **Provenance Spec** | Source, authorship, consent, lineage (PROV-O) | JSON-LD |
| **Ethical Metadata** | FAIR+CARE fields for responsible data governance | JSON Schema |
| **Validation Rules** | Required fields, types, enumerations | JSON Schema Draft 2020-12 |

---

## 🧩 Core Schema Fields (data-contract-v3.json)

| Field | Type | Description | Required |
|-------|--------|-------------|----------|
| `id` | string | Unique dataset identifier | ✅ |
| `title` | string | Human-readable name | ✅ |
| `description` | string | Summary of dataset | ✅ |
| `license` | string | SPDX/CC license identifier | ✅ |
| `spatial` | object | GeoJSON bbox / footprint | ✅ |
| `temporal` | object | ISO-8601 start/end | ✅ |
| `schema_version` | string | Contract version | ✅ |
| `provenance` | object | Authoring, consent, lineage | ✅ |
| `faircare` | object | Ethical/sovereignty metadata | ✅ |
| `quality` | object | Accuracy + completeness metrics | — |

---

## ⚖️ FAIR+CARE Extensions

| Field | Description | Example |
|-------|-------------|----------|
| `collective_benefit` | Intended civic/scientific value | `"Supports Kansas historical research"` |
| `authority_to_control` | Cultural consent/ownership | `"Controlled by Kaw Nation"` |
| `responsibility` | Steward / maintainer | `"FAIR+CARE Council"` |
| `ethics` | Sensitive/cultural notes | `"Contains culturally sensitive boundary data"` |

---

## 🔍 Provenance Specification (provenance-spec.json)

Follows **PROV-O**, **PAV**, and **DCAT 3.0**.

| Field | Description |
|-------|-------------|
| `source_url` | Original source or API endpoint |
| `creator` | Dataset creator |
| `contributor` | ETL or transformation actor |
| `issued` | Publication timestamp |
| `modified` | Last modified |
| `license` | SPDX license |
| `checksum` | SHA256 integrity value |
| `consent` | Cultural/community approval |

---

## 🧾 Validation Workflows

| Workflow | Purpose | Output |
|----------|---------|---------|
| `data-contract-validate.yml` | JSON Schema validation | schema-validation.json |
| `data-provenance.yml` | Lineage + consent verification | provenance-summary.json |
| `faircare-audit.yml` | Ethical metadata enforcement | faircare-validation.json |
| `data-quality.yml` | Completeness & accuracy | completeness.json |

---

## 🧠 Example Contract — Climate Data

~~~json
{
  "id": "noaa_ks_climate_1880_2025",
  "title": "NOAA Kansas Historical Climate Observations",
  "description": "Daily temperature and precipitation across Kansas (1880–2025).",
  "license": "CC-BY-4.0",
  "spatial": { "bbox": [-102.05, 37.00, -94.60, 40.00] },
  "temporal": { "start": "1880-01-01", "end": "2025-01-01" },
  "provenance": {
    "source_url": "https://www.ncei.noaa.gov/",
    "creator": "NOAA NCEI",
    "issued": "2025-01-05T00:00:00Z",
    "consent": "Public domain — no restrictions"
  },
  "faircare": {
    "collective_benefit": "Supports climate resilience modeling",
    "authority_to_control": "Open government dataset",
    "responsibility": "KFM ETL Team",
    "ethics": "Contains no personal or sensitive cultural data"
  }
}
~~~

---

## 📊 Contract Governance

| Version | Description | Effective | Body |
|---------|-------------|-----------|--------|
| v1.0 | Initial contract standard | 2023-01-10 | Data Standards Team |
| v2.0 | FAIR integration | 2024-03-25 | FAIR Council |
| v3.0 | FAIR+CARE + consent schema | 2025-07-01 | FAIR+CARE Council |

---

## 🕰️ Version History

| Version | Date | Summary |
|---------|---------|----------|
| v11.2.2 | 2025-11-27 | Upgraded to v11.2.2 standard; emoji layout fixed; footer style updated. |
| v10.0.0 | 2025-11-10 | Initial data contracts + provenance + validation workflows. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📜 Provenance Spec](provenance-spec.json) · [🛡️ Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>
