---
title: "🛰️ KFM v11.2.4 — Lineage Telemetry Integration Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/lineage/lineage-telemetry-standard.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability · FAIR+CARE Oversight"
content_stability: "stable"
backward_compatibility: "v11.x lineage-contract compatible"
status: "Active / Enforced"
status_notes: "Validated across all lineage-aware pipelines"

doc_kind: "Standard"
intent: "lineage-telemetry-standard"
role: "lineage-telemetry-contract"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/lineage-telemetry.json"
telemetry_schema: "schemas/telemetry/lineage-v2.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public Document"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false
risk_category: "Lineage & Telemetry"
redaction_required: false

data_steward: "Reliability · Sustainability · FAIR+CARE Council"
ttl_policy: "24 months"
sunset_policy: "Superseded when lineage telemetry standard v12 is adopted"

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

provenance_chain:
  - "docs/pipelines/lineage/lineage-telemetry-standard.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-lineage-telemetry-standard-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-lineage-telemetry-standard-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:pipelines:lineage:telemetry-standard:v11.2.4"
semantic_document_id: "kfm-pipelines-lineage-telemetry-standard-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:lineage:telemetry-standard:v11.2.4"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🧭 Context"
    - "🧱 Architecture"
    - "📦 Data & Metadata"
    - "🧪 Validation & CI/CD"
    - "🗂️ Directory Layout"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

diagram_profiles:
  - "mermaid-flowchart-v1"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"
  - "lineage-telemetry-check"

ci_integration:
  workflow: ".github/workflows/lineage-audit.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Deterministic Provenance × Telemetry × Sustainable Intelligence"
  architecture: "OpenTelemetry Spans · PROV-O JSON-LD · Neo4j Lineage"
  analysis: "Evidence-Led · Audit-Ready · FAIR+CARE Grounded"
  data-spec: "STAC/DCAT/PROV-Ready · Lineage-First"
  telemetry: "Span-Aligned · JSON-LD-Backed · Carbon-Aware"
  graph: "Provenance-Rich · Queryable · Story-Node-Ready"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields: []
---

<div align="center">

# 🛰️ **Lineage Telemetry Integration Standard**  
**Deterministic Provenance · OpenTelemetry Spans · PROV-O JSON-LD Unity Layer**  
`docs/pipelines/lineage/lineage-telemetry-standard.md`

**Purpose:**  
Define a **governed, deterministic lineage telemetry contract** for all KFM pipelines, unifying  
OpenTelemetry spans and PROV-O JSON-LD artifacts into a single, Neo4j-backed lineage graph.

</div>

---

## 📘 Overview

This standard governs how every KFM pipeline emits **explainable**, **verifiable**, and **CARE-safe** lineage telemetry via:

- **Paired OpenTelemetry spans** (runtime observability).  
- **PROV-O JSON-LD artifacts** (long-lived provenance records).  

Together they ensure that:

- Every dataset version, ETL node, and AI-assisted transformation is:
  - Traceable through space and time.  
  - Reproducible from WAL and config.  
  - Anchored into the Neo4j lineage graph and external catalogs.  

Pipelines that do **not** implement this standard:

- Cannot pass lineage audit.  
- Cannot be certified as Long-Term Support (LTS).  
- May be subject to **Autonomy Matrix** slow/pause actions until compliant.

---

## 🧭 Context

This standard sits at the intersection of:

- **Pipelines** — ETL, AI inference, training, and Focus Mode transformations.  
- **Observability** — OpenTelemetry spans, metrics, logs.  
- **Provenance** — PROV-O JSON-LD, Neo4j lineage graph, STAC/DCAT metadata.  

It supports:

- **Deterministic replay** — WAL + config + inputs + PROV = reproducible.  
- **Autonomy Matrix patterns** — especially deterministic retry and WAL-safe checkpoints.  
- **FAIR+CARE governance** — by making lineage **auditable**, not implicit.

Every lineage-aware pipeline must:

- Emit **spans** that reference **PROV activities/entities**.  
- Write **JSON-LD provenance** to the required directory layout.  
- Maintain **idempotency** and consistent hashes across retries.

---

## 🧱 Architecture

### 1. Core Entities & Identifiers

#### 1.1 Identifiers

~~~text
lineage.run_id       # Unique per pipeline run
lineage.activity_id  # Unique per node activity
lineage.entity_id    # Identifies dataset entity/version
idempotency_key      # Ensures deterministic behavior across retries
~~~

| Entity               | Description                     | Recommended Format       |
|----------------------|---------------------------------|--------------------------|
| `lineage.run_id`     | Unique per pipeline run         | UUIDv7 (or UUIDv4)       |
| `lineage.activity_id`| Unique per node activity        | UUIDv4 / UUIDv7          |
| `lineage.entity_id`  | Dataset entity/version ID       | SHA-256 digest           |
| `idempotency_key`    | Retry-stable logical work key   | SHA-256(inputs + config) |

Requirements:

- `lineage.run_id` is stable for the entire pipeline run.  
- `lineage.activity_id` is stable for a node activity, including all retries.  
- `idempotency_key` **must not change** across retries for the same logical work unit.

### 2. OpenTelemetry Span Requirements

Every lineage-aware node emits at least one span containing the following attributes:

#### 2.1 Required Attributes

~~~text
etl.node
etl.retry_count
etl.idempotent

lineage.run_id
prov.activity_id
prov.entity_output

data.input_hash
data.output_hash
kfm.config_digest
idempotency.key

energy.kwh
carbon.kg_co2e
cost.usd
~~~

- `etl.node` — logical node name (e.g., `p2_monthly_report_join`).  
- `etl.retry_count` — integer, incremented on each attempt.  
- `etl.idempotent` — boolean; `true` unless explicitly and documented otherwise.  
- `data.input_hash` / `data.output_hash` — hashes of normalized inputs/outputs.  
- `kfm.config_digest` — SHA-256 of effective configuration (YAML/JSON).  
- `energy.kwh`, `carbon.kg_co2e`, `cost.usd` — telemetry bundle (min required fields).

#### 2.2 Span Status Rules

- On success:
  - `StatusCode.OK`  
  - `etl.retry_count` reflects final attempt.  
- On failure:
  - `StatusCode.ERROR`  
  - Error classification attribute (e.g., `error.class = "TransientError"`).  
  - Retries **must** increment `etl.retry_count` while preserving `idempotency.key`.

### 3. PROV-O JSON-LD Requirements

Each activity MUST generate a PROV document with the structure:

~~~json
{
  "@context": ["https://www.w3.org/ns/prov.jsonld", {"kfm":"https://kfm.org/ns#"}],
  "@id": "urn:prov:activity:<activity_id>",
  "@type": "prov:Activity",
  "prov:used": [
    { "@id": "urn:prov:entity:<input_entity_id>" }
  ],
  "prov:generated": { "@id": "urn:prov:entity:<output_entity_id>" },
  "prov:wasAssociatedWith": { "@id": "urn:prov:agent:<executor>" },
  "prov:startedAtTime": "<iso8601>",
  "prov:endedAtTime": "<iso8601>",
  "kfm:idempotencyKey": "<idempotency_key>",
  "kfm:configDigest": "<sha256>",
  "kfm:retryCount": <n>,
  "kfm:energyKwh": <float>,
  "kfm:carbonKgCO2e": <float>,
  "kfm:costUsd": <float>
}
~~~

#### 3.1 Required Linking

- `prov.activity_id` (span attribute) **must equal** the `@id` activity in JSON-LD.  
- `prov.entity_output` (span attribute) **must equal** the `prov:generated` entity ID.  
- `lineage.run_id` is carried via:
  - JSON-LD metadata (e.g., `kfm:runId`).  
  - Or graph linkage when ingesting into Neo4j.

---

## 📦 Data & Metadata

### 1. Telemetry Bundles (Per Node)

Each node **MUST** emit a telemetry bundle including, at minimum:

- `energy.kwh` — node+dependencies energy usage.  
- `carbon.kg_co2e` — derived from energy × regional grid intensity.  
- `cost.usd` — direct compute + storage cost attributed to activity.  
- `etl.retry_count` — final count of attempts.  
- `etl.idempotent` — boolean flag for idempotency compliance.  

Recommended additional fields:

- `grid_intensity_gco2_per_kwh`  
- `deadline_at` / `sla_ms`  
- `queue_depth` / `arrival_rate`  

These fields must be:

- Present in spans.  
- Reflected (where relevant) in `kfm:` extension fields in JSON-LD.

### 2. Storage Requirements for PROV

#### 2.1 Location

All PROV documents MUST be written to:

~~~text
data/lineage/prov/<year>/<month>/<day>/<activity_id>.jsonld
~~~

Examples:

- `data/lineage/prov/2025/12/06/8f5c0a3e-...-activity.jsonld`

Additional guidelines:

- Paths must be **time-based** (UTC) using start or end time.  
- Filenames should incorporate `activity_id` to ensure uniqueness.

#### 2.2 Retention & Immutability

- Minimum retention: **10 years** for production lineage.  
- Files are **immutable after commit**; amendments must be new activities/entities.  
- Underlying storage (e.g., lakeFS) must version `lineage/` and make changes auditable.

---

## 🧪 Validation & CI/CD

### 1. Determinism Checks

All nodes MUST satisfy:

- `data.output_hash` identical across retries given same inputs + config.  
- `idempotency_key` stable for identical inputs/config.  
- Divergence (drift) triggers:
  - Lineage incident SLO.  
  - Autonomy Matrix evaluation (possible `pause` or `escalate`).

### 2. Lineage Telemetry Checks

CI should enforce:

- Spans contain all **required attributes**.  
- PROV documents:
  - Validate against `lineage-v2.json` and SHACL shapes.  
  - Are consistent with spans (IDs, hashes, timings).  
- `lineage-telemetry.json` aggregates are:
  - Well-formed.  
  - Consistent with per-activity documents.

Recommended automation:

~~~text
make validate-lineage-telemetry
make validate-lineage-prov
github action: lineage-audit
~~~

### 3. Dashboard Integration Requirements

Each lineage activity MUST surface in:

- **Lineage Spacetime Graph** — event nodes with temporal and spatial context.  
- **Idempotency Compliance Heatmap** — per-node view of retries vs success.  
- **Carbon Attribution Explorer** — per-activity and per-dataset carbon usage.  
- **WAL Replay Inspector** — mapping WAL sequences ↔ PROV activities ↔ spans.

`lineage-audit` GitHub Action:

- Checks for missing PROV for any span marked `lineage-aware`.  
- Flags high `etl.retry_count` without idempotency or WAL alignment.  
- Produces a summary report for SRE and governance.

---

## 🗂️ Directory Layout

Lineage telemetry integration touches multiple parts of the repo:

~~~text
docs/
  pipelines/
    lineage/
      lineage-telemetry-standard.md     # This standard

data/
  lineage/
    prov/
      <year>/<month>/<day>/<activity_id>.jsonld   # PROV JSON-LD artifacts

schemas/
  telemetry/
    lineage-v2.json                     # Telemetry schema for lineage
  json/
    docs-pipelines-lineage-telemetry-standard-v11.2.4.schema.json
  shacl/
    docs-pipelines-lineage-telemetry-standard-v11.2.4-shape.ttl

releases/
  v11.2.4/
    sbom.spdx.json
    manifest.zip
    lineage-telemetry.json              # Aggregated lineage telemetry export
~~~

Rules:

- `lineage-telemetry-standard.md` is the **single** authoritative standard.  
- All lineage-aware pipelines must be documented under `docs/pipelines/` and reference this file.  
- Any additional lineage standards (e.g., domain-specific) must build on this doc, not override it.

---

## ⚖ FAIR+CARE & Governance

Lineage telemetry is a core part of FAIR+CARE in KFM:

- **FAIR**  
  - **Findable** — Activities/entities have stable IDs, locations, and metadata.  
  - **Accessible** — Lineage is exposed via APIs and dashboards with appropriate auth.  
  - **Interoperable** — PROV-O JSON-LD, DCAT, and STAC alignments.  
  - **Reusable** — Clear provenance and cost/energy/carbon context for derived work.

- **CARE**  
  - **Collective Benefit** — Lineage supports responsible reuse and community benefit analyses.  
  - **Authority to Control** — Sovereignty policies may restrict lineage visibility for sensitive data.  
  - **Responsibility** — SRE and stewards must monitor lineage metrics and respond to anomalies.  
  - **Ethics** — Lineage should make it clear where models/datasets used sensitive inputs so they can be governed accordingly.

Governance hooks:

- Lineage incidents (e.g., lost PROV, inconsistent hashes) must be handled via:
  - Reliability Engineering runbooks.  
  - FAIR+CARE Council where sensitive data is involved.  
- Changes to `lineage-v2` schemas or this standard require:
  - Security & reliability review.  
  - FAIR+CARE oversight sign-off.

---

## 🕰️ Version History

| Version   | Date       | Notes                                                                                      |
|----------:|------------|--------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Initial publication of unified lineage telemetry standard for KFM v11.2.4; defines span/PROV contracts, storage layout, and governance hooks. |

---

<div align="center">

🛰️ **KFM v11.2.4 — Lineage Telemetry Integration Standard**  
Deterministic Provenance · Telemetry-Driven Audits · Neo4j-Ready Lineage  

[📘 Pipelines Index](../README.md) · [🧠 Autonomy Matrix](../autonomy-matrix/README.md) · [⚖ Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>