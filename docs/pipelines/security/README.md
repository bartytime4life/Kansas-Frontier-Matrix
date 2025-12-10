---
title: "🛡️ Kansas Frontier Matrix — Security Pipelines Index"
path: "docs/pipelines/security/README.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security & Supply Chain Council"
content_stability: "stable"

doc_kind: "Pipeline Overview"
status: "Active / Canonical"
intent: "security-pipelines-index"
semantic_document_id: "kfm-doc-pipelines-security-index-v11.2.6"

license: "CC-BY 4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
prov_profile: "KFM-PROV v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

header_profile: "standard"
footer_profile: "standard"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
signature_ref: "../../../releases/v11.2.6/signature.sig"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
telemetry_ref: "../../../releases/v11.2.6/security-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines/security-v1.json"
---

# 🛡️ Security Pipelines for KFM v11.2.6

This README is the **canonical index** for all **security-focused pipelines** in Kansas Frontier Matrix (KFM):

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode.

It ties together:

- **Security event pipelines** (e.g., GitHub PAT → cloud control-plane pivot)  
- **Security control pipelines** (e.g., branch protections, OIDC & identity posture)  
- **Detection and correlation pipelines** (e.g., anomaly detection, supply-chain alerts)  

All new or modified security pipelines must be reflected here and must comply with **KFM-MDP, KFM-OP, FAIR+CARE, and security governance**.

---

## 📘 Purpose & Scope

This document:

- defines the **documentation layout** under `docs/pipelines/security/`
- describes how security pipelines fit the **core KFM pipeline**
- catalogs existing and planned **security pipeline families**
- standardizes expectations for:
  - ETL configs (`configs/pipelines/security/`)
  - data layout under `data/`
  - STAC/DCAT/PROV catalogs
  - Neo4j graph modeling
  - APIs and Story Node surfaces
- establishes minimum **governance and CI/CD** rules for security pipelines

Implementation details live under `src/` and `configs/`, not in this README.

---

## 🗂️ Documentation Layout

Documentation under `docs/pipelines/security/` follows a standard structure:

~~~text
docs/pipelines/security/
├── 📄 README.md                       # This file (security pipelines index)
├── 📁 events/
│   └── 📄 README.md                   # Security event pipelines directory
├── 📁 controls/
│   ├── 📄 README.md                   # Pipelines around security controls posture
│   ├── 📄 github-branch-protections.md
│   ├── 📄 oidc-enforcement-posture.md
│   └── 📄 cloud-iam-posture.md
└── 📁 detections/
    ├── 📄 README.md                   # Detection / correlation / anomaly pipelines
    ├── 📄 supply-chain-detections.md
    ├── 📄 anomaly-detection-ci-cd.md
    └── 📄 provenance-integrity-checks.md
~~~

Related non-docs locations (specified in each sub-README):

- `src/pipelines/security/events/` — ETL & logic for security event ingestion  
- `src/pipelines/security/controls/` — posture / control-state pipelines  
- `src/pipelines/security/detections/` — alerting, correlation, anomaly detection  
- `configs/pipelines/security/` — YAML configs for all security pipelines  
- `data/raw/security/` — immutable raw security data (logs, exports)  
- `data/work/security/` — normalized and enriched security tables  
- `data/processed/security/` — graph-ready or API-ready security artifacts  
- `data/stac/security/` — STAC Collections/Items for security datasets  
- `data/catalog/security/` — DCAT catalogs for security-related datasets  
- `data/provenance/security/` — PROV bundles (batch- and run-level)  

Each directory under `docs/pipelines/security/` has its own README that details:

- local directory layout  
- specific pipelines and IDs  
- graph mapping and catalogs  
- tests and CI hooks  

---

## 🧬 Security Pipelines in the KFM Pipeline

Security pipelines follow the same canonical flow as the rest of KFM, with stricter governance:

1. **Deterministic ETL (src/pipelines/security/...)**
   - Ingests security data from:
     - GitHub and CI/CD  
     - cloud control-plane & IAM logs  
     - dependency, SBOM, and vulnerability scanners  
     - provenance auditing systems
   - All ETL is **config-driven** (no hard-coded constants that affect semantics).

2. **STAC / DCAT / PROV Catalogs**
   - Each ETL run produces:
     - STAC Items/Collections under `data/stac/security/`  
     - DCAT datasets under `data/catalog/security/`  
     - PROV-O bundles under `data/provenance/security/` and `mcp/experiments/security/...`

3. **Neo4j Security Graph**
   - Normalized outputs become graph entities in Neo4j:
     - `SecurityEvent`, `SecurityControl`, `SecurityDetection`, `ThreatPattern`, `System`, `Credential` (abstract), `Policy`, etc.
   - Relationships connect events, controls, policies, datasets, and Story Nodes.

4. **API Layer**
   - APIs under `src/api/security/` expose security graph views and curated aggregates:
     - event timelines  
     - control posture views  
     - detection and correlation results  

5. **Frontend & Story Nodes**
   - Frontend modules under `src/web/security/` and Story Nodes render:
     - security event narratives  
     - investigations and incident timelines  
     - control-state evolution over time  
   - Focus Mode provides **governed investigation surfaces** without exposing raw sensitive logs.

---

## 🧱 Security Pipeline Families

### 🔹 Events

Documented under: `docs/pipelines/security/events/README.md`

Focus: **raw and normalized security events**, such as:

- GitHub audit & workflow events  
- cloud IAM and control-plane logs  
- provenance anomalies and integrity checks  

Example pipeline:

- `github-pat-cloud-pivot` — Security event pipeline supporting the
  **GitHub PAT → Cloud Control Plane Pivot** event brief under
  `docs/security/events/github-pat-cloud-pivot/README.md`.

### 🔹 Controls

Documented under: `docs/pipelines/security/controls/README.md`

Focus: **security control posture** across KFM:

- branch protections and required reviews  
- GitHub OIDC enforcement, PAT usage, and token scope posture  
- cloud IAM policies and policy drift  
- configuration of CI/CD safeguards (e.g., disallowing risky workflow triggers)

Pipelines typically:

- periodically ingest control-state snapshots  
- compare against desired baselines and policies  
- emit control posture datasets and alerts

### 🔹 Detections & Correlation

Documented under: `docs/pipelines/security/detections/README.md`

Focus: connecting **events + controls + data flows** into detections:

- anomaly detection on CI/CD or cloud behavior  
- supply-chain detection (e.g., suspicious package behavior, provenance breaks)  
- correlations between events, code changes, and Story Nodes  
- integrity checks for SBOM, attestations, and PROV bundles

Outputs feed:

- `SecurityDetection` nodes in Neo4j  
- detection catalogs and dashboards  
- security event Story Nodes and Focus Mode views

---

## 📊 Security Pipeline Catalog (v11.2.6 Snapshot)

This table provides a high-level catalog across all security pipeline families.

| Pipeline ID                      | Family      | Brief Description                                                  | Primary Source(s)                            | Spec Doc (docs/pipelines/security/...)                        | Status          |
|---------------------------------|-------------|--------------------------------------------------------------------|---------------------------------------------|----------------------------------------------------------------|-----------------|
| `github-pat-cloud-pivot`        | events      | Ingest, normalize, and catalog events relevant to GitHub PAT → cloud control-plane pivot threats. | GitHub audit logs, Actions, cloud IAM logs  | `events/github-pat-cloud-pivot.md`                            | Active / Stable |
| `github-branch-protections`     | controls    | Track and evaluate repository branch protections for KFM repos.    | GitHub repository config / APIs             | `controls/github-branch-protections.md`                       | Planned         |
| `oidc-enforcement-posture`      | controls    | Measure and report on OIDC vs static credentials usage in CI/CD.   | GitHub Actions configs, cloud IAM policies  | `controls/oidc-enforcement-posture.md`                        | Planned         |
| `cloud-iam-posture`             | controls    | Evaluate least-privilege posture of cloud IAM roles used by KFM.   | Cloud IAM policy exports                    | `controls/cloud-iam-posture.md`                               | Planned         |
| `supply-chain-detections`       | detections  | Correlate events, SBOM, and attestation data into supply-chain detections. | SBOM, attestations, security events         | `detections/supply-chain-detections.md`                       | Planned         |
| `provenance-integrity-checks`   | detections  | Validate PROV and attestation chains for integrity and consistency.| PROV bundles, attestations, OpenLineage     | `detections/provenance-integrity-checks.md`                   | Planned         |

Each pipeline’s full specification lives in the path shown and must:

- describe ETL, catalogs, graph mappings, Story Nodes, and CI tests  
- reference relevant **security event briefs** under `docs/security/events/` where applicable  

---

## 🗺️ Data Layout & Catalog Expectations

All security pipelines share common layout rules:

### Data Layers

- **Raw** (`data/raw/security/`):
  - strictly immutable  
  - content-addressed where feasible  
  - access-controlled due to potential sensitivity

- **Work** (`data/work/security/`):
  - normalized, joined, and partially enriched tables/files  
  - useful for debugging and intermediate analysis

- **Processed** (`data/processed/security/`):
  - graph-ready exports  
  - redacted views for Story Nodes and Focus Mode  
  - API-ready aggregates and summary tables

### STAC & DCAT

- Each pipeline contributes to at least one **STAC Collection** in `data/stac/security/collections/` and a set of **STAC Items** in `data/stac/security/items/`.
- DCAT datasets live under `data/catalog/security/` and must record:
  - license, publisher, temporal coverage  
  - spatial extent (generalized or omitted for sensitive sites)  
  - links to STAC artifacts, PROV, and governance docs

### PROV-O

- Run-level PROV bundles go to `data/provenance/security/<family>/<pipeline_id>/...` and/or `mcp/experiments/security/...`.
- Minimal PROV content:
  - Entities: datasets, exports, and key artifacts  
  - Activities: ETL, normalization, graph ingestion, detection runs  
  - Agents: pipeline runners, maintainers, external systems

---

## 🧪 Reproducibility & Execution

All security pipelines must be **deterministic**, **config-driven**, and **re-runnable**.

### Configuration

- Configs live under: `configs/pipelines/security/<family>/<pipeline_id>.yaml`
- Required config elements:
  - `pipeline_id`, `family`, `version`  
  - source system descriptors and URIs  
  - windowing and watermark strategies  
  - normalization, mapping, and filtering rules  
  - output destinations (raw/work/processed, catalogs, graph ingestion job)  
  - logging and telemetry settings

### Execution Patterns

Example invocation pattern (illustrative):

~~~text
# Run a specific security event pipeline
make pipelines/security/events/github-pat-cloud-pivot

# Run all security pipelines for a daily batch
make pipelines/security/daily-security-batch

# Direct Python entrypoint (example)
python -m src.pipelines.security.events.github_pat_cloud_pivot \
  --config configs/pipelines/security/events/github-pat-cloud-pivot.yaml
~~~

Execution must:

- log to `mcp/experiments/security/<family>/<pipeline_id>/logs/`  
- record:
  - timestamps  
  - git commit SHA  
  - config fingerprint (hash)  
  - output dataset and graph locations  
- emit a PROV bundle per run tying together all used and generated entities

---

## 🛰️ APIs, Story Nodes, and Focus Mode

### API Contracts

The API layer under `src/api/security/`:

- provides stable, documented endpoints for:
  - retrieving security events and detections  
  - exploring security control posture  
  - querying security-related graph structures
- must **not** expose raw secrets or sensitive personal data  
- should return:
  - identifiers linking back to STAC/DCAT/PROV  
  - Story Node IDs where applicable  

### Story Nodes

Security pipelines feed **Story Nodes** that:

- summarize incidents, threats, and posture changes  
- clearly distinguish:
  - **Facts** — supported by data and catalogs  
  - **Interpretation** — council’s reading of the facts  
  - **Speculation** — hypotheses and open questions  
- reference:
  - relevant pipelines (by ID)  
  - event briefs under `docs/security/events/`  
  - governance and policy documents  

Story Node schema references for security-focused stories are defined under:

- `schemas/storynodes/security/*.json` (to be detailed in Story Node docs)

---

## ✅ Governance, FAIR+CARE, and CI/CD

Security pipelines carry heightened governance requirements:

- **Governance Bodies**
  - Primary: **Security & Supply Chain Council**  
  - Co-review: Governance Council, Data & Storytelling Council (for Story Nodes)

- **FAIR+CARE**
  - Findable: catalogs, Story Nodes, and pipeline specs must be discoverable  
  - Accessible: controlled, governed access to sensitive material  
  - Interoperable: strict adherence to KFM-STAC, KFM-DCAT, KFM-PROV profiles  
  - Reusable: clear licensing, provenance, and schema documentation  
  - CARE & sovereignty: generalize or remove sensitive spatial/identity details where required

- **CI/CD Expectations**
  - Markdown:
    - `markdown-lint`, `schema-lint`, `footer-check`  
  - Pipelines:
    - dry-run and determinism tests  
    - schema validation for STAC/DCAT/PROV  
    - SBOM and SLSA checks for pipeline dependencies  
    - secret scanning and security policy checks

CI workflows for security pipelines should live under:

- `.github/workflows/pipelines-security.yml` (or equivalent),  
  referencing pipeline configs and tests defined above.

---

## 🕰️ Version History

| Version  | Date       | Description                                                         |
|----------|------------|---------------------------------------------------------------------|
| v11.2.6  | 2025-12-10 | Initial creation of Security Pipelines index for KFM v11.2.6.       |

---

### ⚖ FAIR+CARE & Governance Footer

This document:

- complies with **KFM-MDP v11.2.6**, **FAIR+CARE**, and KFM security governance policies  
- is governed by the **Security & Supply Chain Council**, with co-review by the Governance Council  
- must be updated whenever KFM adds, removes, or materially changes **security pipelines or families**

Edits require approval from the **Security & Supply Chain Council** and must pass `markdown-lint`, `schema-lint`, `footer-check`, and security/secret scans per KFM-MDP test profiles.

<br/>

<sub>© Kansas Frontier Matrix · CC‑BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

🛡️ **Kansas Frontier Matrix — Security Pipelines Index v11.2.6**  
Security Telemetry · Provenance-First Pipelines · FAIR+CARE Aligned  

[📘 Docs Root](../../README.md) · [🧬 Pipelines Index](../README.md) · [🛡️ Security Docs Index](../../security/README.md) · [⚖ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>