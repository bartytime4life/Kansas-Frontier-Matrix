---
title: "🔁 Kansas Frontier Matrix — Ingestion Pipelines Overview (LangGraph × lakeFS × Great Expectations · Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ingestion/README.md"
version: "v11.2.0"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.0/manifest.zip"
telemetry_ref: "../../releases/v11.2.0/pipelines-telemetry.json"
telemetry_schema: "../../schemas/telemetry/ingestion-index-v11.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active · Enforced"
doc_kind: "Pipeline Index"
intent: "ingestion-root-index"
category: "Ingestion · Pipelines · FAIR+CARE"

classification: "Public Document"
sensitivity: "General; may govern heritage-capable ingestion pipelines via CARE flags in dataset configs."
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Medium"
redaction_required: true

fair_category: "F1-A1-I2-R1"
care_label: "CARE-aware · Heritage-capable"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/pipelines/ingestion/README.md@v11.1.0"
  - "docs/pipelines/ingestion/langgraph-lakefs-ge-workflow.md@v11.1.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true

json_schema_ref: "../../schemas/json/ingestion-index-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/ingestion-index-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "governance-override"
  - "narrative-fabrication"
  - "speculative-additions"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

doc_uuid: "urn:kfm:doc:pipelines:ingestion:index:v11.2.0"
semantic_document_id: "kfm-ingestion-root-index"
event_source_id: "ledger:docs/pipelines/ingestion/README.md"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

jurisdiction: "Kansas · United States"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded by ingestion-index-v12"
---

<div align="center">

# 🔁 **Kansas Frontier Matrix — Ingestion Pipelines Overview (v11.2)**  
`docs/pipelines/ingestion/README.md`

[![LangGraph](https://img.shields.io/badge/Orchestrator-LangGraph_v11-1976d2)]()
[![lakeFS](https://img.shields.io/badge/Data_Versioning-lakeFS-6a1b9a)]()
[![Great Expectations](https://img.shields.io/badge/Validation-Great_Expectations-ff9800)]()
[![FAIR](https://img.shields.io/badge/FAIR-Reproducible-brightgreen)]()
[![CARE](https://img.shields.io/badge/CARE-Heritage--Capable-important)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-blue)]()

**Purpose**  
Serve as the **root index** for all ingestion pipelines within the Kansas Frontier Matrix (KFM), describing how **LangGraph**, **lakeFS**, and **Great Expectations** are used to build deterministic, recoverable, FAIR+CARE-aligned ingestion workflows across hydrology, archaeology, atmospheric, wildfire, and other domains.

</div>

---

## 📘 1. Overview

KFM ingestion pipelines:

- Fetch raw data from external systems (APIs, file drops, cloud archives)  
- Transform and harmonize into KFM’s spatial/temporal and semantic standards  
- Validate data quality and contracts (KFM-PDC v11) via **Great Expectations**  
- Use **lakeFS branches** as ingestion sandboxes for safe promotion to curated layers  
- Emit **PROV-O lineage**, **OpenLineage events**, and **STAC/DCAT metadata**  
- Respect **FAIR+CARE** and sovereignty rules, especially for heritage-adjacent datasets  
- Produce data that is ready for use in Focus Mode narratives and Story Nodes  

This README ties together the **architectural pattern** and the **dataset-specific ingestion specs**.

---

## 🗂️ 2. Directory Layout (v11.2 · Immediate + One Branch)

```text
📁 docs/pipelines/ingestion/                  — Ingestion documentation root
│   📄 README.md                              — This ingestion root index
│   📄 langgraph-lakefs-ge-workflow.md        — Reference LangGraph + lakeFS + GE pattern
│   📂 datasets/                              — Dataset-specific ingestion docs (hydrology, archaeology, wildfire, etc.)
```

Implementation code typically lives under:

```text
📁 src/pipelines/ingestion/                   — Ingestion pipeline implementations
│   📂 langgraph_lakefs_ge/                   — Shared pattern implementation
│   📂 <dataset>_*                            — Dataset-specific ingestion modules
│   📄 README.md                              — (Optional) implementation details
```

---

## 🔁 3. Core Pattern: LangGraph + lakeFS + GE

The ingestion stack for v11.2 is standardized as:

1. **LangGraph** — Orchestration / DAG & agent runtime  
2. **lakeFS** — Data versioning, ingest branches, atomic commits & merges  
3. **Great Expectations** — Validation gates (schema, ranges, nulls, distribution checks)  

Workflow theme:

> _Trigger → Branch → Fetch → Transform → Validate → (Commit + Merge) or (Fail + Retain Branch) → Register (STAC/DCAT) → Story Node / Focus Mode_

The detailed specification for this pattern lives in:  
`docs/pipelines/ingestion/langgraph-lakefs-ge-workflow.md`.

---

## 🌊 4. Domains Covered

Ingestion pipelines cover multiple domains:

- **Hydrology** (USGS, reservoir, streamflow, WID, etc.)  
- **Atmospheric** (HRRR, air-quality pipelines / AQS-AQ, AirNow, KDHE)  
- **Archaeology & Heritage** (subject to H3 + CARE rules)  
- **Wildfire & Hazards** (fuel, dryness, risk layers)  
- **Terrain & Geology** (DEM, surficial geology, soils)  
- **Metadata / Reference** (lookup tables, DMU-lite dictionaries)  

Each domain’s ingestion is documented in dedicated files under `docs/pipelines/ingestion/datasets/`.

---

## 🧬 5. Ingestion Lifecycle (Conceptual)

1. **Configuration & Trigger**  
   - Dataset config loaded (dataset ID, sources, expectations, CARE flags)  
   - Run can be triggered by scheduler, webhooks, or CI/CD.

2. **Branch Creation (lakeFS)**  
   - `ingest/<dataset_id>/<run_id>` branch created from `main` or `staging`.  

3. **Raw Ingest (Fetch Node)**  
   - Data fetched from source systems into `raw/` namespace on ingest branch.  
   - Source URIs + checksums recorded in provenance.  

4. **Transform and Harmonize**  
   - Raw → curated transformations applied.  
   - CRS, units, and naming aligned with KFM standards.  
   - STAC Items & DCAT entries drafted for outputs.  

5. **Validation (GE)**  
   - Expectation suites executed.  
   - Hard fails block promotion.  
   - Telemetry & validation summaries recorded.  

6. **Gate & Promotion**  
   - If validation passes → commit + merge branch into curated mainline.  
   - Else → mark run as failed, no promotion, branch optionally retained for debugging.  

7. **Registration & Narrative Hooks**  
   - STAC/DCAT metadata finalized & stored.  
   - Story Nodes/Focus Mode context generated (where appropriate).  

---

## ⚖️ 6. Governance & CARE Integration

Ingestion pipelines must:

- Honor FAIR+CARE, sovereignty, and data contracts.  
- Respect H3 generalization policies for sensitive spatial layers.  
- Encode CARE flags in dataset configs and metadata.  
- Ensure heritage datasets are screened before public publication.  

Governance is enforced via:

- Config-level flags (`requires_care_screening`, `heritage_sensitive`)  
- GE expectations that check labeling and masking  
- CI workflows (`faircare_validate.yml`, `data_pipeline.yml`) that block problematic changes  

---

## 📊 7. Telemetry & Sustainability Expectations

Each ingestion pipeline should:

- Emit OTEL spans per node  
- Log durations, error counts, bytes processed  
- Estimate energy Wh and carbon gCO₂e (via `energy_schema` / `carbon_schema`)  
- Contribute to the global `focus-telemetry.json` per release  

This supports:

- Reliability dashboards  
- FAIR+CARE audit logs  
- Sustainability reporting (ISO 50001/14064 alignment)  

---

## 🧩 8. How to Add a New Ingestion Pipeline

1. **Create Dataset Config**  
   - Under `config/pipelines/ingestion/<dataset>.yml`  
   - Define sources, lakeFS branches, GE suites, CARE flags, narrative templates.  

2. **Implement Nodes**  
   - Add functions to `src/pipelines/ingestion/langgraph_lakefs_ge/` or into a dataset-specific module.  

3. **Add Expectations**  
   - Define GE suites in `config/expectations/<dataset>/`.  

4. **Wire LangGraph DAG**  
   - Use the reference graph pattern to integrate all nodes and gates.  

5. **Instrumentation**  
   - Add OTEL traces, metrics, energy/carbon emission logic.  

6. **Metadata & Story Nodes**  
   - Implement STAC/DCAT outputs and optional Story Node v3 templates.  

7. **Documentation & CI**  
   - Add/Update docs in `docs/pipelines/ingestion/datasets/<dataset>.md`.  
   - Ensure relevant CI workflows validate the new dataset’s pipeline (contracts, FAIR+CARE, telemetry).  

---

## 🕰️ 9. Version History

| Version | Date       | Summary                                                                                       |
|--------:|------------|-----------------------------------------------------------------------------------------------|
| v11.2.0 | 2025-11-27 | Upgraded to KFM-MDP v11.2.2; added badges, directory layout, FAIR+CARE/telemetry expectations, and LangGraph pattern reference. |
| v11.1.0 | 2025-11-26 | Initial v11 ingestion root; documented LangGraph + lakeFS + GE as standard pattern.          |

---

<div align="center">

**Kansas Frontier Matrix — Ingestion Pipelines**  
*Deterministic · Reproducible · FAIR+CARE-Governed*

[⬅ Back to Pipelines Overview](../README.md) ·  
[🏗 Repository Architecture](../../ARCHITECTURE.md) ·  
[⚖ Governance Standards](../../standards/README.md)

</div>

