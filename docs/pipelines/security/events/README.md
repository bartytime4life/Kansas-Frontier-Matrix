---
title: "🛡️ Kansas Frontier Matrix — Security Event Pipelines Directory"
path: "docs/pipelines/security/events/README.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security & Supply Chain Council"
content_stability: "stable"

doc_kind: "Pipeline Directory"
status: "Active / Canonical"
intent: "security-event-pipeline-index"
semantic_document_id: "kfm-doc-pipelines-security-events-index-v11.2.6"

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

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
telemetry_ref: "../../../releases/v11.2.6/security-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines/security-events-v1.json"
---

# 🛡️ Security Event Pipelines for KFM v11.2.6

This directory README is the **canonical index** for **security event pipelines** in Kansas Frontier Matrix.  
It defines how security-relevant events (e.g., supply-chain threats, credential abuse, cloud pivots) flow through:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode.

All security-event pipeline additions or changes **must** be reflected here.

---

## 📘 Purpose & Scope

This document:

- describes the **documentation layout** under `docs/pipelines/security/events/`
- links each **documented pipeline** to its:
  - ETL config(s)
  - catalog artifacts (STAC/DCAT)
  - Neo4j graph mappings
  - telemetry and provenance bundles
- defines minimum **governance, reproducibility, and FAIR+CARE** requirements for security event pipelines
- anchors pipelines to **security event briefs** under `docs/security/events/`

It does **not** contain implementation code; runtime logic lives under `src/` and `configs/`.

---

## 🗂️ Documentation Layout

~~~text
docs/pipelines/security/events/
├── 📄 README.md                        # This file (canonical directory index)
├── 📄 github-pat-cloud-pivot.md        # Pipeline spec for GitHub PAT → cloud pivot events (summary + pointers)
├── 📁 templates/
│   └── 📄 event-pipeline-template.md   # Reusable template for new security event pipelines
└── 📁 guides/
    ├── 📄 onboarding.md                # How to add a new security event pipeline
    └── 📄 troubleshooting.md           # Common failure modes and playbooks
~~~

Each **concrete pipeline** documented here **must**:

- reference at least one **security event brief** under `docs/security/events/...`
- declare its **ETL config** under `configs/pipelines/security/events/`
- describe its **catalog outputs** under `data/stac/security/events/` and `data/catalog/security/`
- specify its **graph mapping** into Neo4j (labels, relationships, key properties)
- point to **PROV and telemetry** locations under `mcp/` and `releases/`

---

## 🧬 Role in the KFM Pipeline

Security event pipelines are a specialized slice of the core KFM pipeline:

1. **Deterministic ETL**
   - Ingests security-relevant telemetry and artifacts (e.g., GitHub audit logs, CI events, cloud control-plane logs).
   - Normalizes records into **event schemas** under `schemas/security/events/`.
   - All ETL is configuration-driven and reproducible (config files under `configs/pipelines/security/events/`).

2. **STAC/DCAT/PROV Catalogs**
   - Every pipeline run writes:
     - **STAC Items/Collections** under `data/stac/security/events/`
     - **DCAT datasets** under `data/catalog/security/`
     - **PROV-O bundles** under `mcp/experiments/security/events/<pipeline_id>/prov.jsonld`
   - Catalogs reference their **source URIs, licenses, temporal/spatial coverage**, and KFM governance links.

3. **Neo4j Graph Ingestion**
   - Normalized events become `SecurityEvent` (and related) nodes.
   - Relationships link events to:
     - `System` (e.g., GitHub repo, CI runner, cloud project)
     - `ThreatPattern` / `AttackPattern`
     - `PipelineRun`, `Dataset`, and `StoryNode`.
   - Ingestion follows KFM-OP and is validated via schema checks.

4. **API & Frontend**
   - APIs expose queries such as:
     - “Show all high-severity supply-chain threats in the last 30 days”
     - “Graph the event chain for this security incident”
   - Frontend surfaces security event Story Nodes in **Focus Mode**, enabling investigation and historical context.

5. **Story Nodes & Focus Mode**
   - Each significant security event or pattern is rendered as **Story Nodes** with:
     - title, temporal extent, affected systems
     - links to security briefs, pipelines, and raw catalogs
   - Focus Mode supports structured incident investigation without exposing sensitive raw data unnecessarily.

---

## 📊 Security Event Pipeline Catalog

The table below tracks all **documented** security event pipelines for KFM v11.2.6.

| Pipeline ID                 | Description                                              | Primary Source(s)                                 | ETL Config                                                | Event Brief Link                                                                                     | Status          |
|----------------------------|----------------------------------------------------------|--------------------------------------------------|----------------------------------------------------------|------------------------------------------------------------------------------------------------------|-----------------|
| `github-pat-cloud-pivot`   | Detect and catalog GitHub PAT → cloud control-plane pivots and related supply-chain threats. | GitHub audit logs, Actions telemetry, cloud IAM/control-plane logs | `configs/pipelines/security/events/github-pat-cloud-pivot.yaml` | `docs/security/events/github-pat-cloud-pivot/README.md` (GitHub PAT → Cloud Control Plane Pivot) | Active / Stable |
| `TBD-new-security-event`   | Reserved placeholder for next governed security event pipeline. | TBD                                              | `configs/pipelines/security/events/TBD.yaml`             | `docs/security/events/TBD/README.md`                                                                | Planned         |

> When creating a new pipeline, add a row here and ensure the **Event Brief Link** points to an approved security event brief under `docs/security/events/`.

---

## 🌐 Catalog & Graph Integration

Each security event pipeline **must** define:

### STAC Integration

- STAC **Collection** per stable security event family, e.g.:
  - `data/stac/security/events/github-pat-cloud-pivot/collection.json`
- STAC **Items** per pipeline run or per batch of events, with:
  - `id` including pipeline ID and timestamp
  - `datetime` representing event or batch time
  - `properties.severity`, `properties.threat_pattern`, `properties.confidence`
  - `assets` for:
    - normalized event JSON
    - redacted views for Story Nodes / Focus Mode
    - PROV bundles and supporting evidence

### DCAT Integration

- DCAT datasets under `data/catalog/security/`, e.g.:
  - `data/catalog/security/security-events-github-pat-cloud-pivot.jsonld`
- DCAT fields:
  - `title`, `description`, `license`, `publisher`
  - `temporal` coverage for events
  - `spatial` extent (redacted if needed per CARE and sovereignty requirements)
  - links to STAC Collections, PROV bundles, and security briefs

### Neo4j Graph Model (Draft Schema)

Minimum node labels and relationships (to be reviewed under KFM-OP):

- **Nodes**
  - `SecurityEvent`
  - `ThreatPattern`
  - `System` (e.g., `GitHubRepository`, `CloudProject`)
  - `PipelineRun`
  - `Dataset`
- **Relationships**
  - `(:SecurityEvent)-[:INSTANCE_OF]->(:ThreatPattern)`
  - `(:SecurityEvent)-[:OBSERVED_IN]->(:System)`
  - `(:SecurityEvent)-[:RECORDED_IN]->(:Dataset)`
  - `(:PipelineRun)-[:GENERATED]->(:SecurityEvent)`
  - `(:PipelineRun)-[:USED]->(:Dataset)`

Graph mappings must be documented in each pipeline’s own spec under `docs/pipelines/security/events/<pipeline_id>.md`.

---

## 🧪 Reproducibility & Execution

Security event pipelines must be **deterministic** and **config-driven**.

### Configuration

- All configs live under:

  - `configs/pipelines/security/events/<pipeline_id>.yaml`

- Configs must specify:
  - source systems and URIs
  - time windows and filters
  - normalization and mapping strategies
  - output locations under `data/`, `mcp/`, and `logs/`
  - fixed random seeds (if used) and where they are recorded

### Execution

Typical execution pattern (example):

~~~text
# Run a single pipeline (example CLI, actual command may vary)
make pipelines/security/events/github-pat-cloud-pivot

# Or via a Python entrypoint
python -m src.pipelines.security.events.github_pat_cloud_pivot \
  --config configs/pipelines/security/events/github-pat-cloud-pivot.yaml
~~~

Execution **must**:

- write structured logs under `mcp/experiments/security/events/<pipeline_id>/logs/`
- record run metadata:
  - start/end time
  - git commit SHA
  - config hash
  - dataset and graph write locations
- emit a minimal **PROV bundle** per run (see next section)

---

## 🧾 Provenance & Telemetry

### PROV-O Requirements

For each pipeline:

- Entities:
  - raw input datasets (e.g., GitHub logs, cloud API logs)
  - normalized security events
  - STAC/DCAT artifacts
  - graph nodes (aggregated representation)
- Activities:
  - extraction, normalization, classification, graph ingestion
- Agents:
  - KFM pipeline runner (service)
  - source systems (modeled as `prov:SoftwareAgent` or `prov:Organization`)
  - human maintainers (where appropriate)

Minimum location:

- `mcp/experiments/security/events/<pipeline_id>/prov.jsonld`

### Telemetry Requirements

Security event pipelines publish into the shared **security telemetry stream**:

- Append-only telemetry under:

  - `releases/v11.2.6/security-telemetry.json`

- Schema documented at:

  - `schemas/telemetry/pipelines/security-events-v1.json`

Telemetry **must not** leak sensitive endpoints or identities; generalize or redact where required by **FAIR+CARE** and KFM security policy.

---

## ⚖ Governance & Change Control

- Security event pipelines are governed by the **Security & Supply Chain Council**, with coordination from:
  - Governance Council
  - Data & Storytelling Council (for Story Node impacts)
- Any change that:
  - introduces a new security event pipeline
  - materially alters STAC/DCAT/PROV structures
  - changes graph labels/relationships
  - affects telemetry schemas

  must:

  - be proposed via a governed change (PR with RFC or design note)
  - update this directory README and relevant pipeline spec(s)
  - pass:
    - `markdown-lint`
    - schema validation for STAC/DCAT/PROV
    - `footer-check`
    - security/secret scanning workflows

CARE and Indigenous data sovereignty requirements override convenience; sensitive locations and identities **must** be generalized, anonymized, or omitted where necessary.

---

## 🕰️ Version History

| Version  | Date       | Description                                                               |
|----------|------------|---------------------------------------------------------------------------|
| v11.2.6  | 2025-12-10 | Initial creation of Security Event Pipelines directory for KFM v11.2.6.   |

---

### ⚖ FAIR+CARE & Governance Footer

This document:

- complies with **KFM-MDP v11.2.6**, **FAIR+CARE**, and KFM security governance policies  
- is governed by the **Security & Supply Chain Council**, with co-review by the Governance Council  
- must be updated whenever KFM adds, removes, or materially changes **security event pipelines**

Edits require approval from the **Security & Supply Chain Council** and must pass `markdown-lint`, `schema-lint`, `footer-check`, and security/secret scans per KFM-MDP test profiles.

<br/>

<sub>© Kansas Frontier Matrix · CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM-MDP v11.2.6</sub>

<br/>

<div align="center">

🛡️ **Kansas Frontier Matrix — Security Event Pipelines Directory v11.2.6**  
Security Telemetry · Provenance-First Pipelines · FAIR+CARE Aligned  

[📘 Docs Root](../../../README.md) · [🧬 Pipelines Index](../../README.md) · [⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>