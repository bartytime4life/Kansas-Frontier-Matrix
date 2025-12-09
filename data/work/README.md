---
title: "⚙️ Kansas Frontier Matrix — Work Data Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/work/README.md"

version: "v11.2.3"
last_updated: "2025-12-09"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-work-readme:v11.2.3"
semantic_document_id: "kfm-doc-data-work-layer"
event_source_id: "ledger:data/work/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/data-work-layer-v11.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.5"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Guide"
intent: "work-data-layer"
role: "etl-staging-layer"
category: "Data · ETL · Governance · FAIR+CARE"

fair_category: "F1-A1-I1-R1"
care_label: "Variable — Dataset Dependent"
sensitivity: "Mixed"
sensitivity_level: "Variable"
risk_category: "Dataset-level"
indigenous_rights_flag: "Dataset-level"
redaction_required: false
data_steward: "KFM FAIR+CARE Council"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

prov_profile: "PROV-O Plan + KFM Data Lineage Profile"
openlineage_profile: "OpenLineage v2.5 · ETL pipeline events"

provenance_chain:
  - "data/work/README.md@v11.0.0"
  - "data/work/README.md@v11.1.0"
  - "data/work/README.md@v11.2.3"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "hallucinated-datasets"

machine_extractable: true
classification: "Public Document (describes internal layer; data may be sensitive)"
jurisdiction: "Kansas / United States"
accessibility_compliance: "WCAG 2.1 AA"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next Work Data Layer update"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# ⚙️ **Kansas Frontier Matrix — Work Data Layer**  
`data/work/README.md`

**Purpose**  
Formal definition of the **Work Data Layer** within the Kansas Frontier Matrix (KFM).  

This layer is the **governed transformation zone** between **raw data ingestion** and **processed dataset publication**. It hosts:

- Deterministic ETL intermediates  
- Schema‑aligned staging outputs  
- AI‑assisted validation artifacts  
- FAIR+CARE and sovereignty checks  
- Pre‑STAC/DCAT metadata drafts  
- Governance‑linked promotion state for movement into `data/processed/` and `data/stac/`

It is tightly integrated with **PROV‑O**, **OpenLineage**, and **CI/CD workflows** to provide full **traceability**, **lineage**, and **reproducible pipelines**.

</div>

---

## 📘 Overview

The Work Data Layer is the **operational center** of KFM’s data transformation pipeline:

- It is where **raw, immutable sources** from `data/raw/` are:
  - Cleaned and normalized,  
  - Enriched and joined,  
  - Checked against data contracts,  
  - Prepared for cataloging and graph ingest.

- It is **transient but governed**:
  - Contents can be recomputed from `data/raw/` + configs + code,  
  - Yet still must respect FAIR+CARE, sovereignty, and security rules.

- It bridges:
  - **Storage** (`data/raw/`, `data/processed/`),  
  - **Catalogs** (`data/stac/`, `data/dcat/`),  
  - **Graph** (Neo4j),  
  - **Narrative layers** (Story Nodes, Focus Mode).

Work layer assets are:

- **Not directly exposed** to public UIs or external APIs,  
- But they are **first‑class citizens** in provenance, risk assessment, and sustainability accounting.

---

## 🗂️ Directory Layout

Aligned with the canonical `data/` architecture (`data/README.md` and `data/ARCHITECTURE.md`), the Work Data Layer uses a **domain‑aware but type‑first structure**:

~~~text
📁 data/work/
├── 📄 README.md                     # This document (Work Data Layer guide)
│
├── 📁 tables/                       # Normalized tabular intermediates
│   ├── 📁 climate/                  # Climate tables (indices, normals, joins)
│   ├── 📁 hazards/                  # Hazard classification/event tables
│   ├── 📁 hydrology/                # Watershed, streamflow, hydrograph tables
│   ├── 📁 landcover/                # Land cover/use tabular summaries
│   ├── 📁 terrain/                  # Elevation/terrain derivatives
│   ├── 📁 cultural/                 # Cultural/heritage tabular intermediates
│   └── 📁 text/                     # Tokenized/OCR/NLP outputs (governed)
│
├── 📁 spatial/                      # Intermediate spatial layers
│   ├── 📁 climate/                  # Reprojected rasters, zonal stats, tiles
│   ├── 📁 hazards/                  # Event extents, footprints, exposure masks
│   ├── 📁 hydrology/                # Derived streams, catchments, HUC joins
│   ├── 📁 landcover/                # Regridded land cover, change layers
│   ├── 📁 terrain/                  # Slope/aspect/curvature derivatives
│   └── 📁 cultural/                 # H3‑generalized cultural/heritage intermediates
│
├── 📁 metadata/                     # Pre‑publication metadata & logs
│   ├── 📁 stac-drafts/              # STAC‑adjacent JSON for future Items/Collections
│   ├── 📁 dcat-drafts/              # Draft DCAT Dataset/Distribution JSON‑LD
│   ├── 📁 schemas/                  # Snapshot copies of active schemas/contracts
│   └── 📁 lineage/                  # Work‑layer PROV/OpenLineage run fragments
│
└── 📁 logs/                         # Optional: ETL/validation logs (short‑lived)
    ├── 📁 checks/                   # Data contract & validation logs
    └── 📁 ai/                       # AI validation / explainability logs (redacted if needed)
~~~

**Normative notes:**

- `data/work/processed/` and `data/work/tmp/` are **deprecated** patterns.  
  - Final ETL outputs belong in `data/processed/`.  
  - Scratch work belongs in `data/tmp/`.  
- New subdirectories under `tables/` or `spatial/` MUST be:
  - Added to this layout section,  
  - Governed by appropriate FAIR+CARE and sovereignty rules,  
  - Connected to STAC/DCAT/graph modeling where relevant.

---

## 🔄 Role in the Data Lifecycle

Within the canonical **raw → work → processed → catalogs → graph** flow, the Work layer:

1. **Ingests from `data/raw/`**  
   - Pipelines read immutable sources and write normalized outputs into `tables/` and `spatial/`.

2. **Applies data contracts & quality controls**  
   - Schema enforcement, value ranges, CRS harmonization, and geometry checks.

3. **Performs domain‑specific enrichment**  
   - Join external keys, compute indices, derive masks, aggregate by H3 or polygons.

4. **Prepares catalog‑ready views**  
   - Drafts STAC/DCAT metadata in `metadata/stac-drafts/` and `metadata/dcat-drafts/`.

5. **Feeds `data/processed/`**  
   - Only ETL outputs that pass Work‑layer governance and validation are promoted.

6. **Emits lineage & telemetry**  
   - PROV‑O / OpenLineage documents, checksum updates, and sustainability metrics.

No data should skip the Work layer on its way from `raw/` into `processed/` (except in tightly‑scoped emergency flows which MUST be documented and short‑lived).

---

## 🧬 Entities (PROV‑O: `prov:Entity`)

Every **materialized artifact** in `data/work/` that is a meaningful pipeline output SHOULD be modeled as a `prov:Entity`. At a minimum, Work‑layer entities SHOULD carry:

- **Path & identity**
  - `kfm:path` — repository‑relative path (e.g., `data/work/tables/hazards/events_1900_1950.parquet`)  
  - `kfm:entity_uuid` — stable Work‑layer UUID (ASCII‑safe URI/URN)

- **Integrity & versioning**
  - `checksum_sha256` — content hash  
  - `source_commit` — Git commit SHA of the pipeline code  
  - `source_dvc_rev` (if applicable) — DVC version for upstream raw data

- **Governance metadata**
  - `fair_category` — e.g., `F1-A1-I1-R1`  
  - `care_label` — e.g., `Collective Benefit · Authority to Control · Responsibility · Ethics`  
  - `sovereignty_flag` / `sensitivity_level` — to reflect cultural, ecological, or privacy risk

- **Telemetry block (if significant job)**
  - `energy_wh`  
  - `carbon_gco2e`  
  - `records_processed` / `bytes_processed`  

Entity metadata is written into:

- JSON sidecars in `metadata/` (e.g., `metadata/lineage/<entity_uuid>.json`), and/or  
- Central lineage docs under `data/reports/self-validation/lineage/`.

Once an entity is **promoted** to `data/processed/`, its Work‑layer metadata becomes part of its permanent provenance record and MUST NOT be silently changed.

---

## ⚙️ Activities (PROV‑O: `prov:Activity`)

Each ETL or AI operation that creates or modifies Work‑layer entities is a `prov:Activity`. Activities SHOULD record:

- **Identity & config**
  - `pipeline_id` — human‑readable name (e.g., `etl.hazards.events.v3`)  
  - `pipeline_version` — semver or Git tag  
  - `config_fingerprint_sha256` — hash of pipeline configuration used  
  - `environment` — container image tag or environment spec ID

- **Execution details**
  - `started_at` / `ended_at` — ISO 8601 timestamps (`YYYY-MM-DDTHH:MM:SSZ`)  
  - `inputs` / `outputs` — lists of Work‑layer and raw entities (by path or UUID)  
  - Validation coverage metrics (e.g., `% rows tested`, `% rules passed`)

- **Governance hooks**
  - FAIR+CARE validation result (pass/warn/fail),  
  - Sovereignty review status,  
  - Any manual overrides or waivers with justification.

Activities are typically captured via:

- OpenLineage events emitted by CI/CD (`data_pipeline.yml`, `kfm-auto-update.yml`), and/or  
- Python scripts such as `scripts/emit_lineage.py`.

---

## 🧑‍💼 Agents (PROV‑O: `prov:Agent`)

Agents represent people, services, or collectives that are responsible for Work‑layer operations:

Examples:

- `@kfm-etl-ops` — pipeline operators and maintainers  
- `@kfm-architecture` — data/ontology architects  
- `@faircare-council` — FAIR+CARE governance stewards  
- `@kfm-security` — integrity & access control  
- `@kfm-data` — catalog and metadata maintainers  

Each Agent is modeled as a `prov:Agent` and is linked to Activities via relationships such as:

- `prov:wasAssociatedWith`  
- `prov:actedOnBehalfOf`

These associations drive:

- Audit trails,  
- Governance dashboards,  
- Reviewer assignment for high‑risk changes.

---

## 🧪 Validation in the Work Layer

Although Work is transient, validation here is **the primary shield** that prevents flawed data from reaching `processed/`, catalogs, or the graph.

### Validation Scope

Work‑layer validation SHOULD include:

- **Schema & contracts**
  - JSON Schema / SHACL for metadata,  
  - Tabular schema checks (types, allowed values, required fields),  
  - Spatial schema checks (geometry type, CRS, required attributes).

- **Geospatial integrity**
  - Geometry validity (buffer(0) style checks),  
  - CRS correctness and expected transform history,  
  - Meaningful `bbox` coverage (no zero‑area extents unless well‑justified).

- **FAIR+CARE & sovereignty**
  - CARE labels present and appropriate,  
  - Sovereignty and sensitivity flags set correctly,  
  - H3 generalization or masking applied where required before promotion.

- **Security & integrity**
  - Checksum verification vs. `data/checksums/raw/` (for upstream),  
  - No secrets or credentials embedded in Work‑layer data.

- **AI‑specific checks** (when applicable)
  - Bias and drift signals,  
  - Explainability/feature importance logs (where required),  
  - Clear labeling of synthetic / AI‑generated values.

### Where Validation Outputs Live

Work‑layer validation feeds into:

- `data/reports/self-validation/` — schema, FAIR+CARE, and integrity reports,  
- `data/reports/audit/` — higher‑level governance and incident follow‑ups,  
- `data/reports/telemetry/` — aggregated metrics on ETL performance and sustainability.

Promotion from `data/work/` to `data/processed/` MUST be blocked when critical validation fails.

---

## 💾 Example Usage Patterns

### Python — Read Work‑Layer Metadata Sidecar

~~~python
import json
from pathlib import Path

entity_uuid = "urn:kfm:work:hazards:events_1900_1950"
meta_path = Path("data/work/metadata/lineage") / f"{entity_uuid.replace(':', '_')}.json"

with meta_path.open() as f:
    meta = json.load(f)

print("Checksum:", meta["checksum_sha256"])
print("Upstream sources:", meta["upstream_entities"])
~~~

### Bash — Sanity Check of a Spatial Intermediate

~~~bash
# Verify checksum against recorded value
sha256sum data/work/spatial/hazards/events_1900_1950.gpkg

# Inspect CRS and geometry types with ogrinfo (or equivalent)
ogrinfo -al -so data/work/spatial/hazards/events_1900_1950.gpkg
~~~

### Cypher — Trace Work‑Layer Lineage to Raw Sources

~~~cypher
MATCH (w:Entity {layer: "work", domain: "hazards"})
OPTIONAL MATCH (w)-[:wasGeneratedBy]->(act:Activity)-[:used]->(r:Entity {layer: "raw"})
RETURN w.kfm_id AS work_id,
       collect(DISTINCT r.kfm_id) AS raw_sources,
       max(act.ended_at) AS last_run_at;
~~~

---

## 🛣️ Roadmap (Work Layer)

Planned enhancements for the Work Data Layer:

- **v11.2.x** —  
  - Standardize per‑entity lineage sidecars in `metadata/lineage/`.  
  - Tighten integration with `data_pipeline.yml` and `kfm-auto-update.yml` for promotion gating.

- **v11.3** —  
  - Validation‑driven automatic promotion pipelines (Work → Processed → STAC/DCAT).  
  - Domain‑specific Work‑layer dashboards (hydrology, hazards, climate).

- **v11.4** —  
  - AI‑assisted anomaly detection for Work‑layer tables and spatial layers.  
  - Risk scoring for cultural/heritage layers before catalog publication.

- **v11.5** —  
  - Integrated dataset‑risk scoring and FAIR+CARE impact metrics across all Work‑layer domains.

---

## 🕰️ Version History

| Version | Date       | Author       | Summary                                                                                     |
|--------:|------------|--------------|---------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-12-09 | `@kfm-ops`   | Aligned with data/README & data/ARCHITECTURE; simplified layout; integrated PROV/OpenLineage and FAIR+CARE semantics; updated telemetry refs. |
| v11.1.0 | 2025-11-19 | `@kfm-ops`   | KFM-MDP v11 refactor; PROV-O hardening; introduced Work-layer telemetry schema reference.   |
| v11.0.0 | 2025-11-15 | `@kfm-ops`   | Initial v11 migration for Work Data Layer documentation.                                   |
| v10.3.1 | 2025-11-13 | `@kfm-ops`   | Retention policy and v10 telemetry wiring for Work-layer intermediates.                    |

---

<div align="center">

⚙️ **Kansas Frontier Matrix — Work Data Layer (v11.2.3)**  
Staging‑First · FAIR+CARE‑Governed · Provenance‑Aware  

[⬅️ Back to Data Overview](../README.md) ·  
[🗄️ Data System Architecture](../ARCHITECTURE.md) ·  
[🏗️ Repository Architecture](../../ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>