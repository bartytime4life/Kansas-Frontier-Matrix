---
title: "🧪 Kansas Frontier Matrix — Data Quality Gating with OpenLineage (Great Expectations & Soda Core)"
path: "docs/data-ops/data-quality/openlineage-quality-gating.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Data Reliability Board · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Architecture & Implementation Guide"
intent: "data-quality-lineage-gating"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "data-ops"
  applies_to:
    - "docs/data-ops/**"
    - "src/**"
    - "data/**"
    - "mcp/**"

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
sunset_policy: "Superseded by KFM-DataOps v12"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "././releases/v11.2.6/signature.sig"
attestation_ref: "././releases/v11.2.6/slsa-attestation.json"
sbom_ref: "././releases/v11.2.6/sbom.spdx.json"
manifest_ref: "././releases/v11.2.6/manifest.zip"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

provenance_chain: []
provenance_requirements:
  versions_required: false
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: false

story_node_refs: []
immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:data-ops:data-quality:openlineage-quality-gating:v11.2.6"
semantic_document_id: "kfm-openlineage-quality-gating-v11.2.6"
event_source_id: "ledger:kfm:doc:data-ops:data-quality:openlineage-quality-gating:v11.2.6"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — Data Quality Gating with OpenLineage**
`docs/data-ops/data-quality/openlineage-quality-gating.md`

**Purpose**  
Define the canonical KFM pattern for integrating **data‑quality validation** (Great Expectations, Soda Core) with **OpenLineage**, enabling deterministic **quality facets**, hard **promotion gating**, and complete **STAC/DCAT/PROV‑aligned provenance** even on failure.

<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/OpenLineage-Quality%20Facets-blue" />
<img src="https://img.shields.io/badge/Great%20Expectations-Validation-purple" />
<img src="https://img.shields.io/badge/Soda%20Core-Validation-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />

</div>

---

## 📘 Overview

### 1. What this standard enforces (normative)

This pattern is **mandatory** for all governed KFM pipelines that promote data between lifecycle tiers.

It enables:

- Deterministic emission of **quality assertions and metrics** as OpenLineage facets
- **Hard promotion gating** when validation fails
- Full **STAC / DCAT / PROV‑O–aligned provenance**, even on failure
- Compatibility with **Airflow**, **Prefect**, and future orchestrators

### 2. Key principle (normative)

> Quality is lineage, not a side channel.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 data-ops/
    └── 📁 data-quality/
        └── 📄 openlineage-quality-gating.md — this standard

📁 data/
├── 📁 processed/
│   └── 📁 <dataset_id>/
└── 📁 prov/
    └── 📁 <run_id>/
        ├── 📄 openlineage.events.jsonl
        └── 📄 prov.bundle.json

📁 mcp/
└── 📁 runs/
    └── 📁 <run_id>/
        ├── 📄 run-config.snapshot.yml
        ├── 📄 quality.summary.json
        └── 📄 run.log

📁 src/
└── 📁 pipelines/
    └── 📁 quality/
        ├── 📄 ge_runner.py
        ├── 📄 soda_runner.py
        └── 📄 openlineage_emit.py

📁 tests/
└── 📁 data-quality/
    ├── 📄 test_ge_expectations.py
    └── 📄 test_soda_checks.py
~~~

---

## 🧭 Context

### 1. Architectural position in the KFM pipeline (reference)

~~~text
Deterministic ETL
↓
STAC / DCAT / PROV catalogs
↓
🧪 Data Quality Validation (GE / Soda)
↓   ↳ OpenLineage quality facets emitted (PASS or FAIL)
Promotion Gate (PASS / FAIL)
↓
Neo4j Knowledge Graph
↓
API → UI → Story Nodes → Focus Mode
~~~

### 2. Failure semantics (normative)

- Validation failure MUST fail the promotion step.
- Lineage emission MUST still occur on failure (auditable completeness).
- Failures MUST be represented as first‑class provenance events (not “just logs”).

---

## 🗺️ Diagrams

### 1. Quality gating flow (reference)

~~~mermaid
flowchart LR
  A[ETL task produces candidate output] --> B[Quality validation]
  B --> C[Emit OpenLineage facets]
  C --> D{Promotion gate}
  D -->|PASS| E[Promote to next tier]
  D -->|FAIL| F[Block promotion]
  E --> G[Graph ingest]
  F --> H[Retain lineage + artifacts for audit]
~~~

---

## 🧱 Architecture

### 1. OpenLineage quality facet strategy (normative)

KFM uses **OpenLineage dataset and run facets** to encode quality signals.

| Facet type | Purpose | Notes |
|---|---|---|
| `assertions` | Expectation / check pass–fail results | Deterministic IDs required |
| `metrics` | Row counts, null rates, distributions | Stable metric naming |
| `custom:*` | Domain‑specific signals | MUST be governed + schema‑registered |

All emitted facets MUST include:

- `_producer`
- `_schemaURL`
- deterministic identifiers (stable across retries for the same inputs)

### 2. Great Expectations integration (canonical)

#### 2.1 Checkpoint configuration (reference)

Great Expectations checkpoints MUST include the OpenLineage validation action.

~~~yaml
action_list:
  - name: store_validation_result
    action:
      class_name: StoreValidationResultAction

  - name: openlineage
    action:
      class_name: OpenLineageValidationAction
      module_name: openlineage.common.provider.great_expectations
      openlineage_host: ${OPENLINEAGE_URL}
      openlineage_namespace: kfm
      job_name: ge_validate_${dataset_id}
~~~

#### 2.2 Emitted lineage (normative)

On checkpoint execution:

- Each expectation becomes an **assertion facet**
- Success/failure is embedded in lineage
- Lineage is emitted regardless of pass/fail

#### 2.3 Promotion gate (normative)

- Orchestrator task MUST fail on validation failure
- Downstream promotion tasks MUST be blocked
- Lineage MUST remain complete and auditable

### 3. Soda Core integration (canonical)

#### 3.1 Execution pattern (reference)

Soda scans are executed via the Python API and mapped to OpenLineage events.

~~~python
from soda.scan import Scan
from openlineage.client import OpenLineageClient
from openlineage.client.run import RunEvent, Job, InputDataset, OutputDataset

scan = Scan()
scan.execute()

facets = {
  "sodaChecks": {
    "_producer": "kfm-soda-runner",
    "_schemaURL": "urn:kfm:openlineage:facet:soda-checks:v1",
    "results": scan.results_as_dict(),
  }
}

event = RunEvent(
  run=...,  # deterministic run id for this attempt
  job=Job(namespace="kfm", name="soda_scan"),
  inputs=[InputDataset(namespace="kfm", name="dataset")],
  outputs=[OutputDataset(namespace="kfm", name="dataset")],
  run_facets=facets,
)

OpenLineageClient().emit(event)
~~~

#### 3.2 Failure semantics (normative)

- Soda exit code MUST govern orchestration success
- Lineage emission MUST be non‑conditional
- Custom facets MUST be schema‑registered under KFM governance

### 4. Orchestration gating rules (normative)

#### 4.1 Airflow

- Validation task failure halts DAG
- OpenLineage Airflow provider captures:
  - task‑level lineage
  - dataset‑level quality facets

#### 4.2 Prefect

- Validation task MUST raise on failure
- Promotion tasks MUST be conditionally skipped
- OpenLineage events MUST be emitted inside task bodies

---

## 🧠 Story Node & Focus Mode Integration

### 1. What the UI is allowed to do (normative)

- Story Nodes MAY display quality summaries as evidence links (never as facts without source).
- Focus Mode MAY:
  - summarize reported quality outcomes,
  - highlight failing assertions,
  - link to the provenance activity that produced them.

### 2. What the UI must not do (normative)

- Focus Mode MUST NOT invent “PASS” where lineage indicates “FAIL”.
- Focus Mode MUST NOT fabricate metrics, assertions, or thresholds.

---

## 🧪 Validation & CI/CD

### 1. Gating contract (normative)

A pipeline MUST NOT promote outputs if **any governed quality suite fails**.

### 2. Minimum checks (normative)

- Deterministic assertion identifiers
- Lineage emission on pass and fail
- Artifact retention for audit:
  - GE validation results
  - Soda scan results
  - OpenLineage run events (JSONL recommended)
- Promotion step blocked on failure

### 3. Anti‑patterns (disallowed)

- Silent validation failures
- Promotion without lineage emission
- Quality stored outside OpenLineage as the “source of truth”
- Non‑deterministic assertion identifiers

---

## 📦 Data & Metadata

### 1. Retention (normative)

- Validation artifacts MUST be retained according to governance TTL.
- Run logs and config snapshots MUST be stored under `mcp/runs/<run_id>/`.

### 2. Deterministic identifiers (normative)

Quality assertions MUST be stable under:

- task retries
- replays with identical inputs
- environment redeploys (when `code_ref` and `container_digest` are unchanged)

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC

- STAC Items MAY reference quality summaries via a governed link field (e.g., `quality:href`) provided it does not expose restricted content.
- Quality artifacts SHOULD be modeled as Assets (when appropriate) with checksum + size metadata.

### 2. DCAT

- Quality measurements MAY be published as `dcat:qualityMeasurement` links when permitted by governance.
- Distributions MUST preserve license and access constraints.

### 3. PROV‑O

- Validation runs MUST be representable as `prov:Activity`.
- Failure is a first‑class provenance event (not an error that “disappears”).

---

## ⚖ FAIR+CARE & Governance

### 1. CARE‑aligned quality for sensitive datasets (normative)

Indigenous and sensitive datasets MUST:

- use CARE‑compliant metrics where required
- avoid disallowed assertions
- apply NHPA §304‑safe disclosure rules to any surfaced quality artifacts

### 2. Schema governance (normative)

- All custom OpenLineage facets MUST be registered under a governed KFM Schema Registry process.
- Unregistered facet shapes MUST be rejected in governed promotion.

---

## 🕰️ Version History

| Version | Date | Notes |
|---|---:|---|
| v11.2.6 | 2025-12-12 | Initial governed release (MDP‑compliant formatting). |

---

<div align="center">

📑 **OpenLineage Quality Gating (KFM)**  
Deterministic Pipelines · Explainable Validation · Governed Provenance

[📘 Docs Root](../../README.md) ·
[🧪 Data Quality Index](./README.md) ·
[🧱 Data‑Ops Index](../README.md) ·
[🏛️ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6

</div>