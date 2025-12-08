---
title: "📑 Kansas Frontier Matrix — Artifact Inventory Metadata Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/metadata/README.md"
description: "Metadata specification for KFM v11 artifact inventories, aligning DCAT, STAC, CARE, and KFM archaeology extensions."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-inventory-metadata-v11.2.3"
doc_kind: "Metadata Standard"
intent: "artifact-inventory-metadata"
semantic_document_id: "kfm-doc-archaeology-artifact-inventory-metadata-v11.2.3"
category: "Analyses · Archaeology · Metadata"

sbom_ref: "releases/v11.2.3/sbom.spdx.json"
manifest_ref: "releases/v11.2.3/manifest.zip"
telemetry_ref: "releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/archaeology-artifact-inventory-metadata-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.5"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

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
immutability_status: "version-pinned"

header_profile: "standard"
footer_profile: "standard"

data_steward: "Archaeology Working Group · FAIR+CARE Council"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/metadata/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

<div align="center">

# 📑 **Kansas Frontier Matrix — Artifact Inventory Metadata Standards (v11)**  

`docs/analyses/archaeology/datasets/artifact-inventories/metadata/README.md`

**Purpose**  
Define the complete **metadata specification** for all artifact inventory datasets within the Kansas Frontier Matrix (KFM) v11, aligning DCAT, STAC, CARE, and KFM archaeology extensions for graph ingestion, visualization, and narratives.

</div>

---

## 📘 Overview

This standard ensures that artifact inventory metadata:

- Aligns with:
  - **FAIR+CARE** and sovereignty policies,  
  - **STAC 1.0** (Items + Collections),  
  - **DCAT 3.0**,  
  - **CIDOC-CRM**, **GeoSPARQL**, **OWL-Time**, **ISO 19115**,  
  - **KFM-OP v11** and **MCP-DL v6.3**.  
- Supports:
  - Neo4j **graph ingestion and reasoning**,  
  - Story Node and **Focus Mode v3** generation,  
  - Archaeological visualization (MapLibre + Cesium),  
  - Predictive and phase-based modeling,  
  - Artifact classification reproducibility and full provenance traceability.

Only **public-domain**, **open-license**, or **sovereignty-approved** inventories may be represented by metadata in this directory. No sensitive, culturally restricted, or non-consented artifact information may appear in these metadata records.

---

## 🗂️ Directory Layout

```text
KansasFrontierMatrix/
├── 📁 docs/
│   └── 📁 analyses/
│       └── 📁 archaeology/
│           └── 📁 datasets/
│               └── 📁 artifact-inventories/
│                   ├── 📁 inventories/                      # Cleaned, generalized CSVs
│                   └── 📁 metadata/
│                       📄 README.md                         # ← This file (metadata standard)
│                       📄 flint-hills-lithics-v11.json      # DCAT + STAC + CARE + KFM metadata
│                       📄 prairie-ceramics-v11.json         # Ceramic inventory metadata
│                       📄 contact-era-metals-v11.json       # Protohistoric metals metadata (governed)
│                       📄 fauna-open-v11.json               # Faunal (public-domain oriented) metadata
│                       📁 schemas/                          # JSON schemas for metadata validation
│                           📄 artifact-inventory-metadata.schema.json
│                           📄 artifact-inventory-metadata-shape.ttl
└── 📁 metadata/
    └── 📁 archaeology/
        └── 📁 artifact-inventories/
            └── 📁 stac/                                    # Mirror STAC items (optional alternative layout)
```

This layout is **normative** for artifact-inventory metadata in KFM v11.

---

## 📦 Data & Metadata

Each metadata file in this directory provides a **machine-readable description** and **governance layer** for:

- Lithic inventories,  
- Ceramic inventories,  
- Metal / protohistoric inventories,  
- Faunal (public-domain oriented) inventories,  
- Additional open-access artifact tables that meet sovereignty and FAIR+CARE criteria.

Metadata is stored as **JSON-LD**, combining:

- **DCAT 3.0 Dataset metadata**,  
- **STAC 1.0 Item metadata** (mirroring entries in `stac/items/` when present),  
- **CARE** cultural-safety metadata,  
- **KFM archaeology extensions** (`kfm:*`) linking to provenance, inventories, and graph entities.

No sensitive or restricted details are allowed in this metadata layer.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1️⃣ DCAT 3.0 Dataset Metadata

Required DCAT fields:

| Field             | Description                            | Example                                           |
|-------------------|----------------------------------------|---------------------------------------------------|
| `dct:title`       | Dataset title                          | `"Flint Hills Lithic Inventory v11"`             |
| `dct:description` | Dataset description (FAIR+CARE-aware)  | `"Generalized lithic inventory, culturally reviewed."` |
| `dct:license`     | SPDX license code                      | `"CC-BY-4.0"`                                     |
| `dct:creator`     | Source institution / custodian         | `"WSU Open Collections"`                         |
| `dct:temporal`    | Temporal coverage (OWL-Time interval)  | `"1200–1400 CE"` or explicit interval object      |
| `dct:spatial`     | Generalized spatial description        | `"Kansas, Flint Hills region (generalized)"`      |
| `dcat:distribution` | Main distribution path/URL           | `"inventories/flint-hills-lithics-v11.csv"`       |
| `dcat:keyword`    | Tags / keywords                        | `["lithic","inventory","Kansas","archaeology"]`   |

DCAT metadata MUST be consistent with STAC, CARE, and KFM extensions.

---

### 2️⃣ STAC 1.0 Item Metadata (Mirrored)

Each metadata file MUST align with the corresponding STAC Item (if present). Required STAC fields:

| STAC Field                    | Description                                   | Example                                         |
|-------------------------------|-----------------------------------------------|-------------------------------------------------|
| `stac_version`                | STAC version                                  | `"1.0.0"`                                       |
| `type`                        | STAC type                                     | `"Feature"`                                     |
| `id`                          | Unique dataset ID                             | `"flint-hills-lithics-v11"`                    |
| `bbox`                        | Generalized bounding box                      | `[-101.2, 37.5, -95.4, 40.1]`                  |
| `geometry`                    | Generalized geometry (no site-precise coords) | `MultiPoint` or generalized polygon             |
| `properties.kfm:domain`       | Domain identifier                             | `"archaeology-artifact-inventories"`           |
| `properties.kfm:phase`        | Cultural-phase name                           | `"Late Prehistoric"`                           |
| `properties.kfm:material_class` | Material class                              | `"lithic"`                                      |
| `properties.kfm:generalization` | Spatial generalization                        | `"H3-r7"`                                       |
| `properties.kfm:provenance`   | Provenance log path                           | `"provenance/flint-hills-lithics-v11.json"`    |
| `assets.data.href`            | Inventory file path                           | `"inventories/flint-hills-lithics-v11.csv"`    |
| `assets.data.type`            | MIME type                                     | `"text/csv"`                                    |

STAC and DCAT MUST share the same:

- `id`,  
- `dct:title` vs `properties.title` (if present),  
- `kfm:*` domain/phase/material fields,  
- distribution paths.

---

### 3️⃣ CARE Cultural-Safety Metadata

Required CARE fields:

| CARE Field              | Description                               | Allowed Values                                      |
|-------------------------|-------------------------------------------|----------------------------------------------------|
| `care:sensitivity`      | Sensitivity class                         | `"general"`, `"generalized"`, `"restricted-generalized"` |
| `care:review`           | Review authority                          | `"faircare"`, `"tribal"`, `"none-required"`        |
| `care:notes`            | Cultural context / review notes           | Free text; required for generalized/restricted data |
| `care:visibility_rules` | Visibility constraints                    | `"h3-only"`, `"no-exact-points"`                   |

Forbidden in this directory:

- `care:sensitivity = "restricted"` — such records belong in non-public, access-controlled locations.  
- Free-text fields that expose sacred sites, burials, or restricted information.

---

### 4️⃣ KFM Archaeology & Governance Fields (`kfm:*`)

Key KFM extension fields:

| Field                | Description                                      |
|----------------------|--------------------------------------------------|
| `kfm:domain`         | `"archaeology-artifact-inventories"`            |
| `kfm:phase`          | Cultural phase key used in graph & Story Nodes  |
| `kfm:material_class` | High-level material class                       |
| `kfm:datatype`       | Typically `"artifact-inventory"`                |
| `kfm:provenance`     | Path/ID of PROV-O JSON-LD log                   |
| `kfm:source`         | Source institution or repository                |

These fields MUST be consistent across:

- Inventory CSV,  
- STAC Item,  
- DCAT Dataset,  
- Provenance logs,  
- Graph ingestion config.

---

## 🧪 Validation & CI/CD

All artifact-inventory metadata MUST pass:

- **JSON Schema validation**  
  - Against `metadata/schemas/artifact-inventory-metadata.schema.json`.  
- **DCAT validation**  
  - Required DCAT fields present and consistent; license and creator recorded.  
- **STAC alignment checks**  
  - `id`, `assets.data.href`, `kfm:*` fields consistent with STAC Items (if mirrored).  
- **CARE validation**  
  - `care:*` values allowed and consistent with sovereignty policy and H3 generalization.  
- **Crosswalk validation**  
  - STAC/DCAT/PROV cross references remain consistent with `inventories/` and graph configs.

Recommended CI workflows:

- `.github/workflows/archaeology-artifact-metadata-validate.yml`  
- `.github/workflows/archaeology-artifact-stac-validate.yml`  
- `.github/workflows/faircare-archaeology-audit.yml`  

Any validation failure must block:

- New releases referencing these metadata,  
- Graph ingestion of corresponding inventories,  
- Story Node promotion that depends on these datasets.

---

## ⚖ FAIR+CARE & Governance

Metadata in this directory is:

- **High-sensitivity** by concept (archaeology + heritage),  
- Stored in a **public-governed** but carefully generalized form,  
- Subject to strong oversight by:
  - Archaeology Working Group,  
  - FAIR+CARE Council,  
  - Sovereignty governance structures (Tribal and community stakeholders).

Key governance requirements:

- All metadata updates must be:
  - Logged with provenance (authors, dates, justifications),  
  - Reviewed for CARE and sovereignty impacts.  

- Any change that:
  - Reduces generalization (e.g., `H3-r7` → `H3-r9`), or  
  - Introduces new fields that might increase risk

MUST be explicitly reviewed and approved by relevant governance bodies before merge.

---

## 📄 Example Metadata Snippet (v11-Aligned)

> Illustrative only; actual files MUST conform to schemas and governance decisions.

```json
{
  "dct:title": "Flint Hills Lithic Inventory v11",
  "dct:description": "Generalized lithic artifact dataset for the Flint Hills region, reviewed under FAIR+CARE.",
  "dct:license": "CC-BY-4.0",
  "dct:creator": "WSU Open Collections",
  "dct:temporal": "1200–1400 CE",
  "dct:spatial": "Kansas, Flint Hills region (generalized)",
  "dcat:distribution": "inventories/flint-hills-lithics-v11.csv",
  "dcat:keyword": ["lithic", "inventory", "Kansas", "archaeology"],

  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "flint-hills-lithics-v11",
  "bbox": [-101.2, 37.5, -95.4, 40.1],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": []
  },
  "properties": {
    "kfm:domain": "archaeology-artifact-inventories",
    "kfm:phase": "Late Prehistoric",
    "kfm:material_class": "lithic",
    "kfm:generalization": "H3-r7",
    "kfm:provenance": "provenance/flint-hills-lithics-v11.json",
    "care:sensitivity": "generalized",
    "care:review": "faircare",
    "care:notes": "Coordinates generalized via H3-r7 and reviewed for cultural safety.",
    "care:visibility_rules": "no-exact-points"
  },
  "assets": {
    "data": {
      "href": "inventories/flint-hills-lithics-v11.csv",
      "type": "text/csv",
      "roles": ["data"]
    }
  }
}
```

---

## 🕰️ Version History

| Version | Date       | Author / Steward                    | Summary                                                                 |
|--------:|------------|--------------------------------------|-------------------------------------------------------------------------|
| v11.2.3 | 2025-12-02 | Archaeology WG · FAIR+CARE Council  | Updated to KFM v11.2.3; added energy/carbon telemetry refs; aligned with STAC/CARE/KFM v11 patterns and Focus Mode v3. |
| v10.4.0 | 2025-11-17 | Archaeology WG · FAIR+CARE Council  | Created metadata standards for artifact inventories; defined STAC/DCAT/CARE rules and validation paths. |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team               | Initial structure and baseline metadata guidance.                        |

---

<div align="center">

📑 **Kansas Frontier Matrix — Artifact Inventory Metadata Standards**  

[⬅ Artifact Inventories Index](../README.md) ·  
[🏺 Inventory Files](../inventories/README.md) ·  
[⚖️ Root Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
