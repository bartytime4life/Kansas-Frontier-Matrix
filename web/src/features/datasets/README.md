---
title: "🗂️ Kansas Frontier Matrix — Datasets Feature (STAC/DCAT Exploration & Governance · Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/datasets/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council + Data Stewardship Board"
content_stability: "stable"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-readme>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/web-datasets-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-datasets-v2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Feature Overview"
intent: "web-features-datasets"
role: "overview"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Dataset-Dependent"
sensitivity_level: "Dataset-dependent"
public_exposure_risk: "Medium"
indigenous_rights_flag: "Conditional"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"
redaction_required: true

provenance_chain:
  - "web/src/features/datasets/README.md@v10.3.2 (archived)"
  - "web/src/features/datasets/README.md@v11.0.0 (refactor)"

ontology_alignment:
  cidoc: "E31 Document / E53 Place / E52 Time-Span"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
  prov_o: "prov:Entity"

json_schema_ref: "../../../../schemas/json/web-features-datasets-readme-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/web-features-datasets-readme-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:web-features-datasets-readme-v11.2.2"
semantic_document_id: "kfm-doc-web-features-datasets-readme-v11"
event_source_id: "ledger:web/src/features/datasets/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions (no speculative dataset metadata)"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "summaries"
  - "unverified-historical-claims"
  - "speculative-additions"
  - "governance-override"
  - "content-alteration"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public with CARE exceptions"

ttl_policy: "Review each major release"
sunset_policy: "Superseded on next datasets-feature architecture revision"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Datasets Feature (STAC/DCAT Exploration & Governance)**  
`web/src/features/datasets/README.md`

**Purpose:**  
Provide the **canonical feature architecture** for STAC/DCAT dataset exploration in the KFM Web Platform — including  
FAIR+CARE-governed discovery, metadata browsing, spatial/temporal previews, filtering, sorting,  
and secure integration with MapView, Story Nodes, Timeline, and Focus Mode v3.

</div>

---

## 📘 1. Overview

The **Datasets Feature** powers:

- 🔍 Dataset search (keyword, spatial, temporal, facet)  
- 🗂️ Catalog browsing (STAC & DCAT v3)  
- 🛰️ Footprint previews with H3 masking  
- 🧭 Dataset → Focus Mode handoff  
- 🧬 Provenance & rights display (SBOM + PROV-O)  
- 📅 Temporal extent filtering (OWL-Time aligned)  
- 🔐 CARE/Sovereignty enforcement  
- ♿ Accessibility-first dataset interactions  
- 📈 Telemetry capture (performance, energy, FAIR+CARE events)  

The feature **does not** include UI components; it powers them via pipelines, hooks, helpers, and governance logic.

---

## 🗂️ 2. Directory Structure (Emoji-Enhanced · v11.2.2)

~~~text
web/src/features/datasets/
│
├── 📘 README.md                   # This file
│
├── 🔎 search/                     # Dataset search orchestration
│   ├── 🪝 useDatasetSearch.ts     # Keyword + temporal + spatial search logic
│   ├── ⚙️ buildQuery.ts           # STAC/DCAT-compliant query builder
│   └── 🧪 search-validators.ts    # Schema + CARE validation for search filters
│
├── 🔗 pipelines/                  # Dataset ingestion + harmonization pipelines
│   ├── 🛰️ stacPipeline.ts        # STAC Collection/Item fetch + normalization
│   ├── 📚 dcatPipeline.ts        # DCAT Dataset → DatasetVM alignment
│   └── 🧬 datasetNormalizer.ts    # Provenance, CARE, spatial/temporal extraction
│
├── 🧠 state/                      # Feature-local state & contexts
│   ├── 🧭 datasetState.ts        # Selected dataset, filters, sort order
│   └── 🕰️ temporalState.ts       # Time filters synced with TimelineView
│
├── 🪝 hooks/                      # High-level orchestrators
│   ├── useDatasetResults.ts      # Manages fetching/searching/filtering
│   ├── useDatasetProvenance.ts   # Provenance chain extraction
│   └── useDatasetGovernance.ts   # CARE + sovereignty rule enforcement
│
├── 🧬 view-models/                # Dataset semantic models
│   └── datasetViewModel.ts       # Typed VM for dataset display in UI layers
│
└── 🛠️ utils/                      # Shared helpers
    ├── 🗺️ spatial-utils.ts        # H3 masking, centroid extraction
    ├── 📅 temporal-utils.ts       # Normalize OWL-Time intervals
    ├── 📜 provenance-utils.ts     # Ledger + STAC provenance helpers
    └── 🔐 governance-utils.ts     # CARE enforcement helpers
~~~

---

## 🧩 3. Dataset Feature Responsibilities

### ✔ Data Discovery (STAC/DCAT)

- Harmonize STAC v1.x Collections/Items.  
- Surface DCAT distributions & rights metadata.  
- Respect dataset licenses (SPDX).  
- Provide unified **DatasetVM** to all UI components.

### ✔ Spatial/Temporal Governance

- Apply **H3 r7** standard masking to sensitive datasets.  
- Generalize bounding boxes when sovereignty applies.  
- Temporal generalization for culturally sensitive periods.

### ✔ Provenance (PROV-O / SBOM)

Datasets MUST include:

- Source lineage  
- Rights holder  
- License  
- Transformation chain  
- Checksums (SPDX, SHA256)

### ✔ Non-Speculative Metadata

No guessing, no inferred fields, no speculative temporal/spatial claims.

---

## 🧬 4. Dataset View-Model (DatasetVM) Summary

*(Authoritative shape defined in `datasetViewModel.ts`)*

A DatasetVM MUST include fields describing:

- identity  
- provenance  
- spatial/temporal extent  
- licensing + rights  
- CARE label  
- sovereignty flag  
- generalization/masking metadata  

It MUST be validated with JSON schema + TS strict mode.

---

## 🧠 5. Governance Integration (FAIR+CARE v11)

This feature MUST enforce:

- Sovereignty rules for tribal datasets  
- CARE label propagation  
- License restrictions (non-commercial, restricted access)  
- Cultural sensitivity masking  
- Prohibition of exposing raw coordinates for protected datasets  

Governance violations → **CI BLOCK**.

Audit log path:

~~~text
releases/<version>/governance/datasets-governance-ledger.json
~~~

---

## ♿ 6. Accessibility Integration

Datasets feature must ensure:

- Screenreader-safe dataset names  
- High-contrast result lists  
- Fully keyboard-operable filters  
- Accessible temporal picker (if UI triggers)  
- Structured metadata labeling for AT devices  

Accessibility compliance is verified via consuming components + CI (`accessibility_scan.yml`).

---

## 📈 7. Telemetry Responsibilities

Telemetry MUST record:

- dataset search queries (non-PII)  
- filter and sort usage  
- provenance expansions  
- governance warnings displayed  
- energy + latency characteristics  
- masking/CARE enforcement events  

Telemetry bundle (v11.2.2):

~~~text
releases/v11.2.2/web-datasets-telemetry.json
~~~

---

## 🧪 8. Testing Requirements

- Unit tests for pipelines + hooks  
- Integration tests for dataset → UI flows  
- Governance validation tests  
- Temporal/spatial masking tests  
- Telemetry schema emission tests  

Tests are located under:

~~~text
tests/unit/web/features/datasets/**
tests/integration/web/features/datasets/**
tests/e2e/web/features/datasets/**
~~~

---

## 🕰 9. Version History

| Version  | Date       | Summary                                                                                     |
|---------:|------------|---------------------------------------------------------------------------------------------|
| v11.2.2  | 2025-11-30 | Full v11 alignment: FAIR+CARE v11, telemetry v2, H3 masking upgrades, KFM-OP alignment.     |
| v10.3.2  | 2025-11-14 | Added DCAT + STAC harmonization & DatasetVM strengthening.                                  |
| v11.0.0  | 2025-03-10 | Dataset feature refactor for v11 release structure.                                         |

---

## ⚖️ Footer

<div align="center">

**Kansas Frontier Matrix — Datasets Feature**  
🗂️ Ethical Dataset Discovery · 🛰️ STAC/DCAT Integration · 🛡️ FAIR+CARE Governance  

[← Back to Web Features](../README.md) •  
[🧬 Entities Layer](../../entities/README.md) •  
[🛡 Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

© 2025 Kansas Frontier Matrix — MIT License  

**End of Document**

</div>
