---
title: "📦 Kansas Frontier Matrix — Datasets Entities Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/entities/datasets/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/web-entities-datasets-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-entities-datasets-v2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Architecture Overview"
intent: "web-entities-datasets"
role: "overview"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Dataset-dependent"
sensitivity_level: "Dataset-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/entities/datasets/README.md@v10.3.2"

ontology_alignment:
  cidoc: "E31 Document / E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"
  prov_o: "prov:Entity"

json_schema_ref: "../../../../../schemas/json/web-components-entities-datasets-readme-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/web-components-entities-datasets-readme-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:web-entities-datasets-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-entities-datasets-readme-v11"
event_source_id: "ledger:web/src/entities/datasets/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with constraints"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "summaries"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
classification: "Public / Dataset-sensitive"

ttl_policy: "Review each major release"
sunset_policy: "Superseded upon Datasets Entities v12 upgrade"
---

<div align="center">

# 📦 **Kansas Frontier Matrix — Datasets Entities Architecture (v11.2.2)**  
`web/src/entities/datasets/README.md`

**Purpose:**  
Define the **FAIR+CARE-certified, Diamond⁹ Ω–grade Entity View-Model (EVM) architecture** for **Datasets** in the Kansas Frontier Matrix (KFM) v11.2.2.  
Dataset entities unify **STAC**, **DCAT**, **Neo4j**, **PROV-O**, and **Story Node** lineage into a reproducible, governed, provenance-rich model  
used across the entire KFM web platform.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Datasets-orange)]()  
[![Status](https://img.shields.io/badge/Status-Stable-success)]()  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

</div>

---

## 📘 Overview

The **Datasets Entities Layer** defines how KFM represents all datasets, including:

- STAC Collections and Items  
- DCAT Datasets and Distributions (v3 aligned)  
- Neo4j dataset nodes and relationships  
- Provenance lineage chains (PROV-O)  
- Dataset-level CARE governance (rights, consent, sovereignty flags)  
- Dataset quality, checksum, version, and diff history  
- Dataset context for Focus Mode v3 explainability  
- Dataset integration for MapView, TimelineView, Story Nodes, and DataCards  

In KFM, a **Dataset** is not just a file — it is a full semantic record with governed meaning.

---

## 🗂️ Directory Layout

~~~text
web/src/entities/datasets/
│
├── 📘 README.md                # This file
├── 🧬 datasetViewModel.ts      # Dataset EVM type + factory
├── 🧭 datasetMapper.ts         # STAC/DCAT/graph → canonical DatasetVM
└── 📝 metadata.json            # Domain metadata, schema hints, and governance notes
~~~

- `datasetViewModel.ts` → strict typed contract for DatasetVM  
- `datasetMapper.ts` → STAC/DCAT/graph → canonical DatasetVM construction logic  
- `metadata.json` → human-readable semantic notes, versioning, governance, and telemetry lineage  

---

## 🧬 Dataset View-Model Specification

### Conceptual `DatasetVM`

The **DatasetVM** is the canonical, UI-ready representation of a dataset entity.

~~~ts
export type DatasetVM = {
  id: string;
  type: "dataset";
  label: string;                     // dataset name/title
  description?: string;              // accessible summary

  stac?: {
    collectionId?: string;
    itemId?: string;
    assetIds?: string[];
    version?: string;
    datetime?: string;               // primary timestamp, if any
    bbox?: number[];                 // generalized bbox (WGS84)
    hasGeometry?: boolean;
  };

  dcat?: {
    themes?: string[];
    keywords?: string[];
    distributions?: string[];        // IDs/URLs (governance-checked)
    license?: string;                // SPDX or license string
  };

  temporal?: {
    start?: string;                  // ISO 8601
    end?: string;                    // ISO 8601
    precision?: "year" | "month" | "day" | "approximate";
    predictive?: boolean;            // true if modeled/future scenario
    originalLabel?: string;          // e.g. "mid-20th century"
  };

  spatial?: {
    bbox?: number[];                 // generalized extent, not raw tiles
    centroid?: [number, number];     // generalized centroid
    masked?: boolean;                // true if geometries are masked
    generalizationLevel?: "h3-r7" | "h3-r6" | "county" | "region" | "none";
  };

  provenance: {
    sourceIds: string[];             // IDs of primary sources
    lineage?: string[];              // transformation steps
    stacRefs?: string[];             // STAC IDs or URLs
    checksumVerified?: boolean;
    ledgerRefs?: string[];           // governance ledger entries
  };

  care: {
    label: "public" | "sensitive" | "restricted" | "sovereignty-controlled";
    sovereignty?: string;            // tribe/jurisdiction
    consentRequired?: boolean;
  };

  explainability?: {
    relevanceScore?: number;         // ranking signal for Focus Mode
    evidenceSources?: string[];      // StoryNode IDs, document IDs, etc.
  };

  accessibility?: {
    longDescription?: string;        // full summary for screen readers
    shortLabel?: string;             // shorter label for list views
  };
};
~~~

All concrete DatasetVM instances MUST be validated against the DatasetVM schema and TypeScript guards.

---

## 🧭 Dataset Mapper — `datasetMapper.ts`

### Responsibilities

The mapper is responsible for **canonicalizing and governing** dataset metadata:

- Validate and normalize STAC/DCAT metadata and ensure schemas are correct  
- Extract provenance & lineage from STAC/DCAT, Neo4j, and ETL metadata  
- Apply CARE governance rules to sensitive datasets:
  - enforce spatial/temporal masking flags  
  - embed sovereignty & consent indicators  
- Identify predictive datasets and scenario time windows (e.g., 2030–2050)  
- Validate checksum & integrity metadata  
- Convert raw geometry into safe spatial summaries (bbox, centroid, generalization level)  
- Produce accessible dataset descriptions (no speculation, no invented claims)  

### Mapping Flow

~~~mermaid
flowchart TD
    RAWDS["Raw Dataset Metadata<br/>STAC/DCAT · Neo4j · Story Nodes"] --> SAN["Sanitizer & Schema Validation"]
    SAN --> CAREPROC["CARE & Sovereignty Processor"]
    CAREPROC --> PROV["Provenance Builder"]
    PROV --> TEMP["Temporal Extractor"]
    TEMP --> SPAT["Spatial Extractor & Generalizer"]
    SPAT --> VM["DatasetVM<br/>canonical, governed, a11y-ready"]
~~~

The mapper MUST be deterministic and idempotent: given the same input, it yields the same DatasetVM.

---

## ⚖️ FAIR+CARE Governance Integration

Datasets are often **governance-sensitive**:

- Sacred or tribal spatial data  
- Restricted ecological layers  
- Archival sources with personally sensitive content  
- Sovereignty-governed records  
- Strict license constraints

Governance must be encoded **directly** in `DatasetVM.care` and related fields:

~~~mermaid
flowchart TD
    META["Raw Dataset Metadata"] --> CAREENGINE["CARE/Sovereignty Engine"]
    CAREENGINE --> GOVVM["Governed DatasetVM"]
    GOVVM --> LEDGER["Governance Ledger Update"]
~~~

A governance ledger is maintained at:

~~~text
../../../docs/reports/audit/web-entities-datasets-governance.json
~~~

**Rules:**

- When CARE indicates **restricted** or **sovereignty-controlled**, `spatial.masked = true` must be enforced if spatial data exists.  
- License and rights-holder fields must never be defaulted to “open” if unknown; unknown must be explicit and flagged.  
- `DatasetVM` must include `ledgerRefs` linking to governance decisions, when applicable.

---

## 🧠 Explainability Integration (Focus Mode v3)

DatasetVMs contribute to Focus Mode explainability by:

- Supplying evidence nodes (`explainability.evidenceSources`) used in ranking  
- Providing context on coverage, quality, and recency that may influence `relevanceScore`  
- Linking to Story Nodes and events that “use” or “interpret” the dataset  

Explainability metadata in DatasetVM MUST:

- Reflect underlying model outputs (no front-end fabrication)  
- Identify which datasets contributed to a given Focus explanation  
- Be version-aware (if explainability method/model changes, this must be reflected in provenance)

---

## 🗺️ Spatial Semantics

DatasetVM’s `spatial` block supports safe spatial integration:

- `bbox`: generalized bounding box for MapView zoom  
- `centroid`: generalized, masked centroid for map marker placement  
- `generalizationLevel`: indicator of how much geometry has been coarsened  
- `masked`: boolean flag indicating if actual geometry has been withheld

Rules:

- NO raw, full-fidelity geometry in DatasetVM — that stays in geospatial pipelines.  
- For sovereignty-controlled or sensitive datasets, `masked = true` and `generalizationLevel` must specify the masking strategy (e.g., `h3-r7`).  

---

## ⏳ Temporal Semantics

DatasetVM’s `temporal` block supports:

- Exact and fuzzy time ranges (using ISO strings + `precision` + `originalLabel`)  
- Predictive windows (e.g., climate projections 2030–2050, 2050–2100 → `predictive = true`)  
- Alignment with TimelineView for:
  - dataset filtering  
  - highlighting relevant time windows  

Rules:

- Temporal uncertainties must never be hidden; if fuzzy, mark as `precision = "approximate"` and include `originalLabel`.  
- Predictive datasets MUST be clearly marked (no confusion with historical data).

---

## ♿ Accessibility Requirements

DatasetVMs must provide A11y-ready content for UI:

- `accessibility.longDescription`:
  - Summarizes dataset content in plain language  
  - Avoids overly technical or speculative claims  
- `label` / `shortLabel`:
  - Clear, unambiguous names for screen reader users  
- Structured fields allow UIs to:
  - Announce coverage (“Dataset covers Kansas, 1900–1930”)  
  - Indicate CARE/sovereignty status  

Flow:

~~~mermaid
flowchart TD
    DVM[DatasetVM] --> A11Y[a11y Text Builder]
    A11Y --> UI[Accessible Components<br/>DataCards · Drawers · StoryNodes]
~~~

The Entities Layer MUST avoid mixing “UI copy” concerns with core semantics but MUST provide enough structure to make accessible UI easy and consistent.

---

## 📡 Telemetry & Sustainability Integration

DatasetVMs are tied into telemetry pipelines via usage patterns:

Telemetry events (wired by UI/services) include:

- `dataset:select`  
- `dataset:masking-applied`  
- `dataset:predictive-view`  
- `dataset:focus-used`  
- `dataset:lineage-view`  

Telemetry is stored (for v11.2.2) at, for example:

~~~text
../../../releases/v11.2.2/web-entities-datasets-telemetry.json
~~~

Telemetry MUST be:

- Non-PII  
- CARE-aware (e.g., dataset:select for restricted datasets tracked only in aggregate)  
- Schema-validated per `web-entities-datasets-v2.json`  

Entities logic itself should not emit telemetry directly; instead it exposes stable, typed signals/hooks that telemetry collectors can subscribe to.

---

## 🧪 CI / Validation Requirements

**Validation coverage includes:**

| Layer         | Validator / Check                                |
|--------------:|--------------------------------------------------|
| Type safety   | TypeScript strict mode (`tsconfig` strict)       |
| Schema        | DatasetVM JSON Schema + `schemaGuards.ts`       |
| Governance    | `faircare-validate.yml` for CARE + sovereignty   |
| Telemetry     | `telemetry-export.yml` for event schema checks   |
| Accessibility | A11y tests on DatasetVM-driven components        |
| Provenance    | Lineage + checksum verification in ETL tests     |
| Security      | CodeQL + Trivy scans (for pipelines using STAC/DCAT) |
| Docs          | `docs-lint.yml` (this README + related docs)     |

All dataset entities MUST pass:

- Schema & type guards  
- Governance audits for any dataset flagged as sensitive or sovereignty-controlled  
- Telemetry schema validation for new event types  

---

## 🧾 Example Dataset Metadata Record

~~~json
{
  "id": "datasets_entities_v11.2.2",
  "datasets_indexed": 2450,
  "care_public": 2050,
  "care_sensitive": 320,
  "care_restricted": 80,
  "provenance_complete": true,
  "spatial_masked": 145,
  "telemetry_linked": true,
  "timestamp": "2025-11-30T23:59:00Z"
}
~~~

This is a **governance/telemetry summary** record, not a DatasetVM itself.

---

## 🕰 Version History

| Version | Date       | Summary                                                                                                                                               |
|--------:|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Upgraded to v11.2.2; aligned DatasetVM with KFM-OP v11, FAIR+CARE v11, telemetry v2, energy/carbon tracking, and stricter masking/sovereignty rules. |
| v10.3.2 | 2025-11-14 | Deep-architecture creation: STAC/DCAT harmonization, spatial masking, predictive-period metadata, explainability integration, provenance expansion.  |

---

## ⚖️ Footer

<div align="center">

**Kansas Frontier Matrix — Datasets Entities Architecture**  
📦 Semantic Dataset Modeling · 🔐 FAIR+CARE Governance · 🔗 Provenance Fidelity · 🧠 Explainable Data Integration  

[Back to Entities Index](../README.md) •  
[Docs Root](../../../README.md) •  
[Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — MIT License  

**End of Document**

</div>