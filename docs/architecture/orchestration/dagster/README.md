---
title: "⚙️ KFM — Provenance-First Automation with Dagster (Partitioned AOIs & Incremental Syncs)"
path: "docs/architecture/orchestration/dagster/README.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Platform Architecture Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Architecture Pattern"
intent: "dagster-provenance-first-orchestration"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by KFM v12 orchestration standards"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "././releases/v11.2.6/signature.sig"
attestation_ref: "././releases/v11.2.6/slsa-attestation.json"
sbom_ref: "././releases/v11.2.6/sbom.spdx.json"
manifest_ref: "././releases/v11.2.6/manifest.zip"

telemetry_ref: "././releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "././schemas/telemetry/orchestration-doc-v11.2.6.json"
energy_schema: "././schemas/telemetry/energy-v2.json"
carbon_schema: "././schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

doc_uuid: "beeb9d86-e69a-5fda-904e-7f0b1f58a716"
semantic_document_id: "urn:kfm:doc:architecture:orchestration:dagster"
event_source_id: "urn:kfm:event_source:docs:architecture:orchestration:dagster"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain: []

ai_transform_permissions:
  - "summarize"
  - "extract_metadata"
  - "generate_navigation"
  - "produce_diagram_descriptions"
  - "draft_story_node_scaffolds"

ai_transform_prohibited:
  - "alter_normative_requirements"
  - "invent_governance_status"
  - "fabricate_provenance_or_relationships"
  - "add_unreviewed_policy_claims"
---

# ⚙️ Provenance-First Automation with Dagster

**Purpose**  
Define how **Dagster** is used in KFM as a provenance‑first orchestration layer for deterministic ETL, **partitioned Areas of Interest (AOIs)**, **incremental syncs**, and **PROV‑compatible lineage emission** with minimal recomputation.

Dagster’s software‑defined assets model is used to express *what data exists*, *how it evolves*, and *when it should update* — while preserving KFM governance constraints and reproducibility.

---

## 📘 Overview

### 1. What Dagster is responsible for in KFM

Dagster is responsible for orchestrating:

- deterministic extraction and transformation steps,
- incremental refresh policies (avoid full backfills),
- partition management (AOI × time),
- emission of run metadata required for PROV/OpenLineage alignment,
- quality gating prior to promotion.

Dagster is not a replacement for:
- STAC/DCAT/PROV catalogs (it produces/updates them),
- the Neo4j knowledge graph (it triggers ingestion),
- the API boundary (UI never reads raw files directly).

### 2. Core principles (mandatory)

1. **Partition everything that changes frequently** (AOI × time) to avoid recomputation.
2. **Idempotent materialization**: re-running the same partition yields identical outputs and IDs.
3. **Provenance is emitted on every run**, including failures.
4. **Quality gating blocks promotion** but does not block lineage.

---

## 🗂️ Directory Layout

~~~text
docs/
├── architecture/
│   └── orchestration/
│       └── dagster/
│           └── README.md                               ⚙️ This pattern
src/
├── orchestration/
│   └── dagster/
│       ├── assets/                                    🧱 Software-defined assets (ETL/catalog/ingest)
│       ├── partitions/                                🧩 AOI/time partition definitions
│       ├── sensors/                                   ⏱️ Incremental sync triggers
│       └── resources/                                 🔌 IO managers, clients (STAC/graph/lineage)
data/
├── sources/
│   └── <source-name>.yml                               📥 Source manifests (rights, checksums, access)
├── processed/
│   └── <pipeline>/<dataset>/<aoi>/<time>/<run-id>/...   🧪 Deterministic outputs by partition
├── stac/
│   └── <collection-id>/<item-id>/item.json              🗂️ STAC catalogs updated per partition
mcp/
└── runs/
    └── <run-id>/                                       🧾 Run logs + config snapshots + lineage events
tests/
└── orchestration/
    └── dagster/                                        ✅ Partitioning/idempotency/contract tests
~~~

---

## 🧭 Context

### 1. Role in the KFM pipeline

Dagster sits in the orchestration layer of the canonical pipeline:

Deterministic ETL (Dagster assets)  
→ STAC/DCAT/PROV catalogs (written/updated by assets)  
→ Graph ingestion (triggered after catalog updates)  
→ API → UI → Story Nodes → Focus Mode

### 2. Why Dagster (KFM rationale)

Dagster fits KFM because:

- Software‑defined assets encode dependencies explicitly.
- Partitions allow AOI/time slicing with deterministic recomputation.
- Asset materializations can carry structured metadata used for provenance.

---

## 🧱 Architecture

### 1. Asset taxonomy (canonical)

KFM uses these asset categories (names are examples; the pattern is normative):

1. **Source snapshot assets**  
   Fetch/ingest raw source data into `data/sources/` + `data/processed/raw/...`.

2. **Processing assets**  
   Transform source → staged/curated outputs in `data/processed/...`.

3. **Catalog assets**  
   Emit/merge STAC Items/Collections and DCAT records in `data/stac/...` (and DCAT location per repo convention).

4. **Lineage assets (or hooks)**  
   Emit PROV/OpenLineage event artifacts into `mcp/runs/<run-id>/`.

5. **Graph ingestion trigger assets**  
   Call the graph loader to upsert nodes/edges (idempotent merge).

### 2. Partition model: AOI × time (canonical)

KFM partitions are multi‑dimensional:

- **AOI partition**: a named polygon/feature (e.g., county, survey grid, project AOI).
- **Time partition**: daily/weekly/monthly depending on source cadence.

**Rule:** partition keys must be stable, human readable, and governance‑reviewable.

#### 2.1 Recommended partition key schema

- `aoi_key = "<registry-id>"` (stable)
- `time_key = "YYYY-MM-DD"` (UTC)

### 3. Incremental sync semantics

Incremental sync is the default:

- For pull sources: use `cursor`/`since` watermarks stored in deterministic state files (or asset metadata).
- For append-only sources: only new partitions are materialized.
- For corrected sources: materialize a new version and link via STAC versioning / graph predecessor relationships (per pipeline contract).

### 4. Provenance emission (required)

Each materialization MUST record:

- `process_id` (run/step stable ID)
- `code_ref` (git SHA)
- `container_digest` (if containerized)
- `params_json` (deterministic ordering)
- input entity references (STAC Item/Asset IDs, checksums)
- output entity references (STAC Item/Asset IDs, checksums)

**Output location:** `mcp/runs/<run-id>/` (run logs + lineage artifacts).

### 5. Quality gating integration

Dagster MUST implement a validation step before promotion:

- Great Expectations / Soda Core run inside an asset or dedicated op.
- Failures block promotion assets and graph ingestion assets.
- Lineage artifacts are still emitted and stored.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  subgraph D[Dagster]
    A[Process Asset (AOI×Time)] --> Q[Validate (GE/Soda)]
    Q -->|PASS| C[Emit/Update STAC+DCAT]
    Q -->|FAIL| F[Block Promotion]
    C --> L[Emit Lineage (PROV/OpenLineage)]
    F --> L
    C --> G[Trigger Graph Ingest]
  end

  G --> API[API Layer]
  API --> UI[UI + Story Nodes + Focus Mode]
~~~

---

## 📦 Data & Metadata

### 1. Output placement rules (mandatory)

- Write derived artifacts to `data/processed/` (partitioned, version-aware).
- Update STAC under `data/stac/` with stable IDs.
- Write run logs and config snapshots under `mcp/runs/`.

### 2. Deterministic configuration snapshots (mandatory)

Each run MUST persist:

- resolved config
- resolved partition keys
- input checksums and version references
- environment identifiers needed for reproducibility

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC

Dagster assets that produce governed outputs MUST:

- create/update STAC Items per partition,
- include assets with checksums and roles,
- include provenance/quality assets where applicable.

### 2. DCAT

For published datasets, Dagster SHOULD update DCAT records (per KFM-DCAT profile), ensuring license, publisher/creator, and temporal/spatial coverage are consistent with STAC.

### 3. PROV‑O

Dagster runs map to provenance:

- asset materialization = `prov:Activity` (Process)
- input/output artifacts = `prov:Entity` (Items/Assets/Datasets)

---

## 🧠 Story Node & Focus Mode Integration

- Story Nodes must reference stable graph entities generated from STAC.
- Focus Mode should be able to surface:
  - “what changed” between partitions,
  - “why this dataset is trustworthy” (quality evidence),
  - lineage traversal to sources and processes.

---

## 🧪 Validation & CI/CD

### 1. Required CI validations

- Partition naming and determinism checks
- STAC validation for Items/Collections produced by orchestration
- Quality gating enforcement (promotion blocked on FAIL)
- Provenance emission required on PASS and FAIL
- Secrets/PII scanning of logs and artifacts

### 2. Common failure conditions (hard fail)

- Non-deterministic partition key generation
- Outputs written outside `data/processed/` or catalogs outside `data/stac/`
- Missing checksums for governed outputs
- Missing provenance artifacts in `mcp/runs/<run-id>/`

---

## ⚖ FAIR+CARE & Governance

- AOI registries MUST respect Indigenous sovereignty and sensitive site masking rules.
- Output datasets inherit governance flags from inputs.
- Public views must generalize/mask where required.

---

## 🕰️ Version History

| Version | Date | Notes |
|---:|---:|---|
| **v11.2.6** | 2025-12-12 | Initial governed Dagster orchestration pattern (AOI×time partitions, incremental syncs, provenance-first). |

---

**🔗 Navigation**
- 🏛️ Governance Charter: `../../../standards/governance/ROOT-GOVERNANCE.md`
- 🤝 FAIR+CARE Guide: `../../../standards/faircare/FAIRCARE-GUIDE.md`
- 🪶 Indigenous Data Protection: `../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`