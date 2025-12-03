---
title: "🧬 Kansas Frontier Matrix — Artifact Inventory Provenance Logs (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/datasets/artifact-inventories/provenance/README.md"
description: "Provenance and lineage JSON-LD logs for KFM v11 artifact inventories, capturing FAIR+CARE, PROV-O, and sovereignty-aligned review."
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
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

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/archaeology-artifact-inventory-provenance-v1.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

data_steward: "Archaeology Working Group · FAIR+CARE Council"
provenance_chain:
  - "docs/analyses/archaeology/datasets/artifact-inventories/provenance/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true
---

# 🧬 Kansas Frontier Matrix — Artifact Inventory Provenance Logs (v11)

`docs/analyses/archaeology/datasets/artifact-inventories/provenance/README.md`

**Purpose**  
Serve as the authoritative **provenance repository** for all artifact inventory datasets used in the Kansas Frontier Matrix (KFM).

These logs capture:

- Data lineage and processing history  
- Cultural and sovereignty review trails (FAIR+CARE, tribal review)  
- Spatial generalization and redaction steps  
- Version-to-version evolution of each inventory  

Provenance is encoded using **PROV-O**, with CARE and KFM extensions, and is referenced by STAC Items, DCAT records, the knowledge graph, Story Nodes, and Focus Mode v3.

Every artifact inventory MUST include a corresponding provenance record in this directory.

---

## 📘 Overview

Provenance logs in this directory document, at minimum:

- **Source origins**  
  - Museum, archive, academic repository, PD/open dataset, or field project.  
- **Acquisition methods**  
  - Download, API fetch, ingest scripts, OCR pipelines, etc.  
- **Processing steps**  
  - Cleaning, normalization, deduplication, category harmonization, encoding conversion.  
- **Cultural and sovereignty review**  
  - FAIR+CARE and tribal review events, including outcomes and conditions.  
- **Spatial generalization**  
  - H3 mapping, coordinate removal, precision reduction, visibility rules.  
- **Transformations**  
  - Schema harmonization, column renames, type casting, value recoding.  
- **Attribution**  
  - Analysts, reviewers, institutions, and working groups involved.  
- **Version history**  
  - Links between raw → v1 → vN, and rationale for major changes.

Each provenance file acts as the **ground-truth lineage record** linking source data to KFM-ready artifact inventories.

---

## 🗂️ Directory Layout

~~~text
docs/analyses/archaeology/datasets/artifact-inventories/provenance/
├── 📄 README.md                           # This file
├── 📄 flint-hills-lithics-v11.json        # Provenance for lithic inventory
├── 📄 prairie-ceramics-v11.json           # Provenance for ceramic inventory
├── 📄 contact-era-metals-v11.json         # Provenance for protohistoric metals (governed)
├── 📄 fauna-open-v11.json                 # Provenance for faunal (public-domain oriented) dataset
└── 📂 templates/                          # Provenance JSON-LD template definitions
~~~

This layout is **normative** for artifact-inventory provenance logs in KFM v11.

---

## 📦 Required PROV-O & CARE Components

Every provenance file must include a minimal, consistent PROV-O structure with CARE and KFM extensions.

### Entities

| Concept        | Description                      | Example label                          |
|----------------|----------------------------------|----------------------------------------|
| Raw dataset    | Initial source file or dataset   | `"Flint Hills Lithics Inventory – Raw"` |
| Processed data | Cleaned / harmonized inventory   | `"Flint Hills Lithics Inventory – v11"` |

Typical fields:

- `prov:Entity`  
- `prov:label`  
- `prov:type` (for example, `"Dataset"` or `"File"`)  
- `kfm:source` (institution / collection)  
- `kfm:provenance_version` (for example, `"v11"`)

### Activities

| Concept     | Description                        | Examples                     |
|-------------|------------------------------------|------------------------------|
| Activities  | Processing steps or reviews        | `"Cleaning"`, `"Generalization"`, `"CARE Review"` |

Typical fields:

- `prov:Activity`  
- `prov:type` (for example, `"Cleaning"`, `"Generalization"`)  
- `prov:startTime`, `prov:endTime` (ISO 8601 timestamps)

### Agents

| Concept | Description                 | Example                               |
|--------|-----------------------------|---------------------------------------|
| Agents | People or organizations     | `"KFM Archaeology WG"`, `"FAIR+CARE Council"` |

Typical fields:

- `prov:Agent`  
- `prov:type` (`"Person"` or `"Organization"`)  
- `prov:label`  
- `prov:actedOnBehalfOf` (for example, working group or council)

### Relations

Key PROV-O relations:

- `prov:wasDerivedFrom` — links processed data back to raw sources.  
- `prov:wasGeneratedBy` — links entities to activities that produced them.  
- `prov:used` — links activities to inputs they consumed.  
- `prov:wasAttributedTo` — connects entities to responsible agents.

### CARE & Sovereignty Layer

Every provenance record must include an explicit CARE layer:

| Field                | Description                                                                |
|----------------------|----------------------------------------------------------------------------|
| `care:sensitivity`   | `"general"`, `"generalized"`, or `"restricted-generalized"`                |
| `care:review`        | `"faircare"`, `"tribal"`, or `"none-required"`                             |
| `care:notes`         | Narrative summary of cultural and sovereignty review                       |
| `care:visibility_rules` | For example, `"h3-only"` or `"no-exact-points"`                        |

Values must align with the artifact’s STAC Item and the sovereignty policy referenced in the front matter.

---

## 🧪 Provenance JSON-LD Template (v11-Aligned)

Example skeleton for a provenance log (illustrative only):

~~~json
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
~~~

Actual records may include additional entities, activities, and agents (for example, OCR, classification, or external review steps).

---

## 🗺️ Integration Within KFM

Provenance logs are referenced and used across the stack:

### STAC & DCAT

- STAC Items reference provenance via `properties.kfm:provenance`.  
- DCAT metadata can surface provenance URIs and summary fields.  

### Knowledge Graph (Neo4j)

- Provenance entities and activities are translated into nodes and relationships:
  - `ArtifactInventory` → `HAS_PROVENANCE` → `ProvenanceRecord`  
  - `ProvenanceRecord` → `WAS_GENERATED_BY` → `Activity`  
  - `ProvenanceRecord` → `HAS_CARE_SENSITIVITY` → `CareState`

### Story Nodes & Focus Mode v3

- Focus Mode uses provenance to:
  - Construct provenance chips beneath explanations.  
  - Apply sensitivity-aware reasoning based on CARE and sovereignty flags.  
- Story Nodes can embed provenance snippets to provide readers with context and auditability.

---

## 📊 Provenance File Index (Illustrative)

| Provenance File              | Dataset                      | Status       | Last Review | Notes                            |
|-----------------------------|------------------------------|-------------|-------------|----------------------------------|
| `flint-hills-lithics-v11.json`   | Lithic inventory           | 🟢 Active    | 2025-11     | Fully validated; generalized H3. |
| `prairie-ceramics-v11.json`      | Ceramic inventory          | 🟢 Active    | 2025-11     | CARE motif review complete.      |
| `contact-era-metals-v11.json`    | Protohistoric metals       | 🟡 Review    | 2025-09     | Tribal consultation in progress. |
| `fauna-open-v11.json`            | Faunal (PD-oriented)       | 🟢 Active    | 2025-11     | PD-only; sacred species removed. |

The canonical index is derived from release manifests and this directory contents; this table is descriptive.

---

## 🕰 Version History

| Version   | Date       | Author                               | Summary                                                                 |
|-----------|------------|--------------------------------------|-------------------------------------------------------------------------|
| v11.2.3   | 2025-12-02 | Archaeology Working Group · FAIR+CARE Council | Aligned with KFM v11.2.3; added energy/carbon telemetry refs, sovereignty metadata, and Focus Mode v3 integration notes. |
| v10.4.0   | 2025-11-17 | Archaeology Working Group · FAIR+CARE Council | Defined provenance structure, PROV-O/CARE requirements, validation rules, and file index. |
| v10.0.0   | 2025-11-10 | Artifact Metadata Team               | Initial provenance framework.                                            |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · Sovereignty-Governed  
KFM-MDP v11.2.2 · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Artifact Inventories](../README.md)
