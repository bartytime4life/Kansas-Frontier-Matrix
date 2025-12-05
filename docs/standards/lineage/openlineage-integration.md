---
title: "🧬 KFM v11.2.4 — OpenLineage Integration Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/lineage/openlineage-integration.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Data Provenance Board"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x lineage-contract compatible"
status: "Active / Enforced"

doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "lineage/openlineage"
  applies_to:
    - "etl"
    - "streaming"
    - "ai-ml"
    - "stac"
    - "dcat"
    - "graph"
    - "story-nodes"
    - "focus-mode"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
classification: "Public"
indigenous_rights_flag: true

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/lineage-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/lineage/lineage-v1.json"
governance_ref: "../governance/ROOT-GOVERNANCE.md"

doc_uuid: "urn:kfm:docs:standards:lineage:openlineage-integration:v11.2.4"
semantic_document_id: "kfm-std-openlineage-integration-v11.2.4"
event_source_id: "ledger:kfm:docs:standards:lineage:openlineage-integration:v11.2.4"

license: "Apache-2.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
---

<div align="center">

# 🧬 KFM OpenLineage Integration Standard  
**Deterministic Provenance for ETL → STAC → Knowledge Graph Pipelines**  

`docs/standards/lineage/openlineage-integration.md`

**Purpose:**  
Define the authoritative **OpenLineage integration standard** for KFM v11 so that all pipelines (ETL, streaming, AI/ML, catalog construction, graph ingestion, Story Node/Focus Mode precomputation) emit deterministic, versioned lineage events that make historical runs reproducible, audit-safe, FAIR+CARE-aligned, and compatible with STAC, DCAT, and PROV-O.

</div>

---

## 📘 Overview

OpenLineage is the **authoritative lineage protocol** inside KFM v11. All pipeline components **MUST** emit:

- Deterministic, versioned lineage events.  
- Consistent job and dataset identifiers.  
- Run state transitions (`START`, `COMPLETE`, `FAIL`) for every execution.  

This standard specifies:

- Job naming rules and run semantics.  
- Dataset and dataset-version facets (including AI/ML-specific requirements).  
- Emission architecture (OpenLineage → Marquez → governance).  
- Compliance rules enforced by CI/CD and governance workflows.

### 1. Scope & Coverage

This standard governs lineage for:

- Deterministic ETL (batch and streaming).  
- Atmospheric, soil, hydrology, geology, and related pipelines.  
- AI/ML training and inference clusters.  
- STAC and DCAT catalog construction pipelines.  
- Neo4j ingestion and backfills.  
- Story Node & Focus Mode precomputation and summarization jobs.

All pipelines MUST emit lineage events for **start**, **complete**, and **error/failure** transitions — even if a particular run produces no output datasets.

---

## 🧱 Architecture

### 1. Job naming (deterministic)

Jobs MUST follow this pattern:

```text
kfm.<domain>.<subsystem>.<pipeline>.<step>
```

Examples:

- `kfm.soil.gnatsgo.ingest.partition`  
- `kfm.atmo.noaa.hrrr.decode-grib`  
- `kfm.archaeo.inference.geomorph.ai-profile`  

Job names MUST be:

- **Stable across releases** (except when a deliberate, documented breaking change occurs).  
- **Unique** enough to distinguish domain, subsystem, pipeline, and step for governance and analysis.

### 2. Run events

Each execution MUST emit OpenLineage run events with at least:

| Field           | Requirement                                       |
|-----------------|---------------------------------------------------|
| `runId`         | UUID v4, stable for the entire run                |
| `state`         | One of `START`, `COMPLETE`, or `FAIL`             |
| `startTime`     | RFC 3339 timestamp                                |
| `endTime`       | RFC 3339 timestamp (for `COMPLETE` / `FAIL`)      |
| `errorMessage`  | Present and non-empty for failures (`FAIL`) only  |

Additional requirements:

- All runs MUST be recorded, even if they produce no outputs.  
- Partial failures (e.g., per-partition errors) must be modeled using multiple runs or facets, rather than silently dropping lineage.

### 3. Emission architecture (KFM v11)

Lineage emission flows through the following architecture:

```text
Pipeline Node
   → Lineage Emitter (OpenLineage client)
       → Marquez Event Bus
           → Marquez DB (Postgres)
               → Read API
                   → Governance Dashboards & Audits
```

Key rules:

- Each node is responsible for **its own lineage** via a node-local OpenLineage client; no shared global emitter that obscures which node produced which events.  
- Emission must be **best-effort and resilient**, with:
  - Local buffering or retry mechanisms.  
  - Clear failure logging if lineage emission itself fails.  
- Marquez (or equivalent OpenLineage-compatible service) is the **system of record** for runtime lineage, augmented by PROV-O exports for long-term archival.

---

## 📦 Data & Metadata

### 1. Dataset semantics

Each OpenLineage dataset MUST define:

| Property     | Requirement                                                           |
|--------------|-----------------------------------------------------------------------|
| `namespace`  | Storage or logical namespace (e.g., `s3`, `gcs`, `neo4j`, `postgres`) |
| `name`       | Fully qualified path or logical identifier                            |
| `type`       | One of `file`, `table`, `graph`, `vector`, or `model`                 |

Guidelines:

- `namespace` SHOULD correspond to an actual service or storage system.  
- `name` SHOULD be stable across runs for a given dataset version family.  
- `type` MUST be chosen from the controlled vocabulary to avoid ambiguity in downstream tools.

### 2. Dataset version facets (mandatory)

Each dataset MUST include a **version facet** that makes the concrete version of the dataset identifiable and reproducible:

- **Files**
  - `etag` and/or `sha256` digest.  
  - Byte size (optional but recommended).  

- **Tables**
  - Snapshot ID or timestamp.  
  - Partition specification (if applicable).  
  - Row count at snapshot time (optional but recommended).  

- **Graph nodes (Neo4j)**
  - Commit SHA or equivalent for ingestion contract or schema version.  
  - Node count delta or other change summary.  

- **Models**
  - Artifact digest (e.g., `sha256:<digest>` for model binary).  
  - Model card identifier (e.g., `urn:kfm:model:soil-moisture:v2`).  

Missing dataset version facets are a **CI-blocking compliance violation** for any pipeline governed by this standard.

### 3. AI/ML pipelines

For AI/ML pipelines (training and inference), lineage MUST include additional facets:

- **Inference runs MUST record:**
  - Model version facet (artifact digest + model card ID).  
  - Training dataset version facet(s).  
  - Parameter snapshot digest (e.g., config hash, hyperparameters).  
  - Explainability-related metadata (e.g., SHAP summary outputs) when generated.  
  - Energy and carbon telemetry facets (referencing KFM energy standards and telemetry v3).

Example version structure:

```yaml
modelVersion:
  artifact_digest: "sha256:..."
  model_card: "urn:kfm:model:soil-moisture:v2"
datasetVersion:
  hash: "sha256:..."
  provenance: "prov:entity:..."
```

These facets MUST be attached as OpenLineage dataset facets or run facets, depending on implementation.

---

## 🌐 STAC, DCAT & PROV Alignment

OpenLineage lineage MUST be compatible with KFM’s wider metadata and provenance ecosystem:

- **STAC**
  - Dataset `name` and `namespace` SHOULD map cleanly to STAC Collections/Items and asset URLs.  
  - Dataset version facets SHOULD be usable to link STAC assets to specific pipeline runs.

- **DCAT**
  - Lineage information can enrich DCAT `dcat:Dataset` and `dcat:Distribution` records via:
    - References to OpenLineage job/run IDs.  
    - Dataset version identifiers in DCAT metadata.  

- **PROV-O**
  - OpenLineage jobs and runs correspond to `prov:Activity`.  
  - Datasets correspond to `prov:Entity`.  
  - Pipeline services correspond to `prov:Agent`.  
  - OpenLineage records SHOULD be convertible into PROV-O bundles, which are referenced via `provenance_ref` fields across KFM.

This standard assumes that OpenLineage is the **operational lineage layer**, with PROV-O used for long-term archival and semantic integration.

---

## 🧪 Validation & CI/CD

### 1. Compliance rules

The following rules are **normative** and enforced via CI and governance:

**Rule 1 — Every job must emit lineage**  
- If a job performs work without emitting at least `START` and `COMPLETE` (or `FAIL`) lineage events, CI treats this as a **hard error**.

**Rule 2 — Every output MUST produce a dataset version**  
- Outputs with missing or incomplete dataset version facets **fail review** and automated lineage audits.

**Rule 3 — No retroactive mutation of old lineage**  
- Historical lineage records MUST NOT be altered, except under explicit governance-approved processes:
  - Retractions or corrections must be recorded as new lineage events, not by editing history in-place.

**Rule 4 — Backfills MUST generate unique run IDs**  
- Backfill runs MUST use distinct `runId` values and be clearly separable from operational runs via:
  - Run facets or naming conventions.  
  - PROV relations indicating `wasDerivedFrom` a backfill configuration.

### 2. CI/CD integration

Lineage compliance is enforced through:

- Lineage CI gates (e.g., `.github/workflows/lineage-audit.yml`) that:
  - Check for lineage event emission for known jobs.  
  - Verify presence of dataset version facets.  
  - Compare lineage structure against `lineage-v1.json`.  

- Reproducibility verification runs:
  - Use lineage data to reconstruct run configurations.  
  - Validate that dataset versions and outputs match expectations.

- Energy/carbon audit workflows:
  - Use lineage information to link energy telemetry to pipeline runs and datasets.

### 3. Integration snippet (pseudocode)

Example OpenLineage integration (Python-like pseudocode):

```python
from openlineage.client import OpenLineageClient
from openlineage.client.facet import DatasetVersionFacet

client = OpenLineageClient(url="http://marquez:5000")

client.emit_start(
    run_id="uuid4-here",
    job_name="kfm.soil.gnatsgo.ingest.partition",
    inputs=[{
        "namespace": "s3",
        "name": "kfm-raw/gnatsgo/2025-12-01/soil.tif",
        "facets": {
            "datasetVersion": DatasetVersionFacet("etag:98ab...")
        }
    }],
    outputs=[]
)

# ... pipeline work ...

client.emit_complete(
    run_id="uuid4-here",
    job_name="kfm.soil.gnatsgo.ingest.partition",
    outputs=[{
        "namespace": "s3",
        "name": "kfm-processed/gnatsgo/v1/soil.parquet",
        "facets": {
            "datasetVersion": DatasetVersionFacet("sha256:abc123...")
        }
    }]
)
```

Implementations must:

- Use library or language bindings appropriate for the service.  
- Ensure `runId`, `job_name`, inputs, outputs, and facets match this standard’s requirements.

---

## ⚖ FAIR+CARE & Governance

This lineage standard underpins FAIR+CARE and governance objectives:

- **FAIR**
  - *Findable*: lineage events and dataset versions are indexed in Marquez and exported to catalogs.  
  - *Accessible*: authorized users can query lineage via APIs and dashboards.  
  - *Interoperable*: OpenLineage is mapped to PROV-O, STAC, and DCAT structures.  
  - *Reusable*: dataset versions and run metadata enable reproducible analyses and reprocessing.

- **CARE & sovereignty**
  - Lineage reveals **how** data was transformed, which is essential when handling:
    - Indigenous knowledge and culturally sensitive datasets.  
    - Archaeological or environmental data with sovereignty constraints.  
  - Pipelines working with such data must:
    - Include lineage facets referencing geoethical and geoprivacy policies where applicable.  
    - Ensure that lineage does not itself leak sensitive information (e.g., by exposing raw paths or internal identifiers that reveal restricted locations).

### Governance hooks

This standard integrates with:

- Lineage CI gates and automated audits.  
- FAIR+CARE review checks when pipelines affect sensitive datasets.  
- Data Provenance Board oversight for standards evolution.  
- Reproducibility and energy/carbon audit workflows.

Any deviation from this standard automatically triggers a **lineage variance report** that must be reviewed and resolved.

---

## 🗂️ Directory Layout

```text
📂 docs/standards/lineage/
├── 📄 README.md                       # 🧬 Lineage Standards Index (to be created/maintained)
└── 📄 openlineage-integration.md      # 🧬 OpenLineage Integration Standard (this file)
```

Additional lineage-related standards (e.g., PROV-O export profiles, Marquez configuration guidelines) must be added under this directory and referenced from `README.md`.

---

## 🕰️ Version History

| Version | Date       | Status            | Notes                                                                |
|--------:|------------|-------------------|----------------------------------------------------------------------|
| v11.2.4 | 2025-12-05 | Active / Enforced | Full alignment with KFM-MDP v11.2.4; telemetry v3; governance certs. |
| v11.2.3 | 2025-12-03 | Superseded        | Added mandatory dataset version facets and stronger CI rules.        |
| v11.2.0 | 2025-11-20 | Superseded        | Initial standardization of lineage flows in KFM v11.                 |

Future revisions must:

- Document changes to dataset facet requirements or job naming patterns.  
- Update CI/CD guidance and telemetry schema references when lineage schemas evolve.  
- Maintain backward compatibility expectations in `backward_compatibility`.

---

<div align="center">

🧬 **KFM v11.2.4 — OpenLineage Integration Standard**  
Deterministic Provenance · Catalog-Integrated Lineage · FAIR+CARE Governance  

[📘 Docs Root](../../..) · [📂 Standards Index](../README.md) · [⚖ Governance](../governance/ROOT-GOVERNANCE.md)

</div>