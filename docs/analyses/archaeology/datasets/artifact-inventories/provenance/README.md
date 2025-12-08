---
title: "🧬 Kansas Frontier Matrix — Artifact Inventory Provenance Logs (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/provenance/README.md"
description: "Provenance and lineage JSON-LD logs for KFM v11 artifact inventories, capturing FAIR+CARE, PROV-O, and sovereignty-aligned review."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_uuid: "urn:kfm:doc:archaeology-artifact-inventory-provenance-v11.2.3"
doc_kind: "Provenance Logs"
intent: "artifact-inventory-provenance"
semantic_document_id: "kfm-doc-archaeology-artifact-inventory-provenance-v11.2.3"
category: "Analyses · Archaeology · Provenance"

sbom_ref: "releases/v11.2.3/sbom.spdx.json"
manifest_ref: "releases/v11.2.3/manifest.zip"
telemetry_ref: "releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/archaeology-artifact-inventory-provenance-v1.json"
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
  - "docs/analyses/archaeology/datasets/artifact-inventories/provenance/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

<div align="center">

# 🧬 **Kansas Frontier Matrix — Artifact Inventory Provenance Logs (v11)**  

`docs/analyses/archaeology/datasets/artifact-inventories/provenance/README.md`

**Purpose**  
Serve as the authoritative **provenance repository** for all artifact inventory datasets used in the Kansas Frontier Matrix (KFM), capturing FAIR+CARE, PROV-O, and sovereignty-aligned review.

</div>

---

## 🗂️ Directory Layout

```text
KansasFrontierMatrix/
└── 📁 docs/
    └── 📁 analyses/
        └── 📁 archaeology/
            └── 📁 datasets/
                └── 📁 artifact-inventories/
                    ├── 📁 inventories/                     # Cleaned, generalized inventory tables
                    ├── 📁 metadata/                        # DCAT/STAC/CARE/KFM metadata
                    └── 📁 provenance/
                        📄 README.md                        # ← This file (provenance index)
                        📄 flint-hills-lithics-v11.json     # Provenance for lithic inventory
                        📄 prairie-ceramics-v11.json        # Provenance for ceramic inventory
                        📄 contact-era-metals-v11.json      # Provenance for protohistoric metals (governed)
                        📄 fauna-open-v11.json              # Provenance for faunal (PD-oriented) dataset
                        📁 templates/                       # JSON-LD provenance templates & examples
```

Provenance filenames MUST:

- Match their corresponding inventory/metadata stems (`flint-hills-lithics-v11.*` etc.), and  
- Be referenced from metadata (`kfm:provenance`) and STAC Items (`properties.kfm:provenance`).

---

## 📘 Overview

Provenance logs in this directory are **ground-truth lineage records** for artifact inventories. Each log documents:

- **Source origins**  
  - Museum, archive, academic repository, PD/open dataset, or field project.  

- **Acquisition methods**  
  - Download, API fetch, ingest scripts, OCR pipelines, or manual curation.  

- **Processing steps**  
  - Cleaning, normalization, deduplication, category harmonization, encoding conversion.  

- **Cultural & sovereignty review**  
  - FAIR+CARE and Tribal review events, including outcomes and conditions.  

- **Spatial generalization & redaction**  
  - H3 mapping, coordinate removal, precision reduction, visibility rules.  

- **Transformations**  
  - Schema harmonization, column renames, type casting, value recoding.  

- **Attribution**  
  - Analysts, reviewers, institutions, and working groups involved.  

- **Version history**  
  - Links between raw → v1 → vN, and rationale for major changes.

Every artifact inventory in `inventories/` MUST have a corresponding provenance record in this directory.

---

## 📦 Required PROV-O & CARE Components

Each provenance file MUST include a minimal, consistent PROV-O structure with CARE and KFM extensions.

### Entities

At minimum:

- `raw` — raw or source dataset  
- `processed` — KFM cleaned/generalized v11 inventory

Typical fields:

- `prov:Entity`  
- `prov:label`  
- `prov:type` (e.g., `"Dataset"`, `"File"`)  
- `kfm:source` (institution / collection)  
- `kfm:provenance_version` (e.g., `"v11"`)

### Activities

Key activities:

- `"Cleaning"` — structural and content cleaning  
- `"Generalization"` — spatial H3 generalization and redaction  
- `"CAREReview"` / `"TribalReview"` — cultural and sovereignty review activities  

Typical fields:

- `prov:Activity`  
- `prov:type` (e.g., `"Cleaning"`, `"SpatialGeneralization"`, `"CAREReview"`)  
- `prov:startTime`, `prov:endTime`  

### Agents

Agents involved:

- Individual analysts (`prov:type = "Person"`)  
- Organizations / working groups (`prov:type = "Organization"`)  

Typical fields:

- `prov:Agent`  
- `prov:type`  
- `prov:label`  
- `prov:actedOnBehalfOf` (e.g., Archaeology WG acting on behalf of KFM).

### Relations

Key PROV-O relations:

- `prov:wasDerivedFrom` — processed inventory → raw sources  
- `prov:wasGeneratedBy` — entity → generating activity  
- `prov:used` — activity → input entities  
- `prov:wasAttributedTo` — entity → responsible agents  

### CARE & Sovereignty Layer

Each provenance record MUST include CARE fields:

| Field                  | Description                                                                |
|------------------------|----------------------------------------------------------------------------|
| `care:sensitivity`     | `"general"`, `"generalized"`, `"restricted-generalized"`                  |
| `care:review`          | `"faircare"`, `"tribal"`, or `"none-required"`                           |
| `care:notes`           | Narrative summary of cultural & sovereignty review; required when generalized |
| `care:visibility_rules`| e.g., `"h3-only"`, `"no-exact-points"`                                   |

Values MUST align with metadata and STAC entries, and respect the sovereignty policy.

---

## 🧪 Provenance JSON-LD Template (v11-Aligned)

> Example skeleton for a provenance log (illustrative only). Real logs MUST follow governed templates and schemas.

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "care": "https://schema.kfm.dev/care#",
    "kfm": "https://schema.kfm.dev/core#"
  },
  "prov:Entity": {
    "raw": {
      "prov:label": "Raw Artifact Inventory",
      "prov:type": "Dataset",
      "kfm:source": "WSU Open Collections"
    },
    "processed": {
      "prov:label": "Processed Artifact Inventory (v11)",
      "prov:type": "Dataset",
      "kfm:provenance_version": "v11"
    }
  },
  "prov:Activity": {
    "cleaning": {
      "prov:type": "Cleaning",
      "prov:startTime": "2025-10-01T14:32:00Z",
      "prov:endTime": "2025-10-01T15:10:00Z"
    },
    "generalization": {
      "prov:type": "SpatialGeneralization",
      "prov:startTime": "2025-10-01T15:15:00Z",
      "prov:endTime": "2025-10-01T15:20:00Z",
      "kfm:generalization": "H3-r7"
    }
  },
  "prov:Agent": {
    "analyst": {
      "prov:type": "Person",
      "prov:label": "J. Barta"
    },
    "reviewer": {
      "prov:type": "Organization",
      "prov:label": "FAIR+CARE Council"
    }
  },
  "prov:wasDerivedFrom": [
    {
      "prov:generatedEntity": "processed",
      "prov:usedEntity": "raw"
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:entity": "processed",
      "prov:activity": "generalization"
    }
  ],
  "care:sensitivity": "generalized",
  "care:review": "faircare",
  "care:notes": "Coordinates generalized via H3-r7 and motif categories reviewed for cultural safety.",
  "care:visibility_rules": "no-exact-points"
}
```

---

## 🧭 How Provenance Ties Into KFM

### STAC & DCAT

- STAC Items reference provenance via `properties.kfm:provenance`.  
- DCAT records may expose provenance URIs and summarized provenance statements.  

### Neo4j Knowledge Graph

Provenance logs are ingested as:

- `:ProvenanceRecord` nodes linked to:
  - `:ArtifactInventory` nodes via `HAS_PROVENANCE`.  
- Activities and agents may be materialized (where useful) as:
  - `:ProvenanceActivity`, `:ProvenanceAgent` nodes for analytics and audit graph.

### Story Nodes & Focus Mode

Story Nodes and Focus Mode v3 use provenance to:

- Show provenance chips and “How do we know this?” panels.  
- Apply sensitivity-aware logic (e.g., hide certain details depending on CARE rules).  
- Provide anchors for narratives across time (e.g., how inventory v10 → v11 changed).

---

## 🧪 Validation & CI/CD

Provenance logs must:

- Validate against:
  - PROV-O structure (via JSON Schema or SHACL where applicable),  
  - CARE-related schemas,  
  - Cross-linking schema (metadata ↔ provenance).

- Be continuously validated via CI workflows, including:
  - `.github/workflows/provenance-validate.yml`  
  - `.github/workflows/faircare-provenance-audit.yml`  

Validation checks:

- Entity, Activity, Agent structures present.  
- Required PROV-O relations present: `wasDerivedFrom`, `wasGeneratedBy`, `used`, `wasAttributedTo`.  
- CARE fields present and consistent with inventory metadata.  
- Filenames and IDs match inventory and metadata naming conventions.

Any failures MUST block inclusion in releases and graph ingestion.

---

## 🧭 Governance & FAIR+CARE

Provenance logs are **high-sensitivity** artifacts and are:

- Governed by:
  - Archaeology Working Group,  
  - FAIR+CARE Council,  
  - Sovereignty governance structures (as applicable).  

- Used as evidence in:
  - External transparency reports,  
  - Community and Tribal consultations,  
  - Internal audits.

Provenance MUST:

- Never expose restricted raw coordinate sets or restricted provenance notes.  
- Document any masking or generalization step as a first-class activity.  
- Record conditions (if any) attached to dataset use (e.g., “not for commercial use”, “consult tribe X before reuse”).

---

## 🕰 Version History

| Version | Date       | Author / Steward                    | Summary                                                                 |
|--------:|------------|--------------------------------------|-------------------------------------------------------------------------|
| v11.2.3 | 2025-12-02 | Archaeology Working Group · FAIR+CARE Council | Aligned with KFM v11.2.3; added telemetry references and Focus Mode v3 integration details. |
| v10.4.0 | 2025-11-17 | Archaeology Working Group · FAIR+CARE Council | Defined provenance structure, PROV-O/CARE requirements, validation rules, and file index. |
| v10.0.0 | 2025-11-10 | Artifact Metadata Team               | Initial provenance framework.                                            |

---

<div align="center">

🧬 **Kansas Frontier Matrix — Artifact Inventory Provenance Logs**  

[⬅ Artifact Inventories Index](../README.md) ·  
[📑 Metadata Standard](../metadata/README.md) ·  
[⚖️ Root Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
