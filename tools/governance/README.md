---
title: "⚖️ Kansas Frontier Matrix — Governance & Provenance Tools (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tools/governance/README.md"
version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:tools:governance:readme:v11.2.6"
semantic_document_id: "kfm-tools-governance-readme-v11.2.6"
event_source_id: "ledger:tools/governance/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/tools-governance-registry-v3.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

doc_kind: "Architecture"
intent: "tools-platform-governance"
role: "governance-registry"
category: "Governance · Provenance · FAIR+CARE"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: true
risk_category: "Low"
redaction_required: false
data_steward: "KFM FAIR+CARE Council"

provenance_chain:
  - "tools/governance/README.md@v11.2.2"
  - "tools/governance/README.md@v11.0.0"
  - "tools/governance/README.md@v10.2.2"
  - "tools/governance/README.md@v10.0.0"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareSourceCode"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "N/A"

json_schema_ref: "../../../schemas/json/tools-governance-readme-v11.json"
shape_schema_ref: "../../../schemas/shacl/tools-governance-readme-v11.shape.ttl"

ai_training_allowed: false
ai_training_guidance: "Do not use governance ledger contents as model training data."
ai_outputs_require_explainability: true
ai_outputs_require_bias_audit: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas · United States"
lifecycle_stage: "operational"
ttl_policy: "Review required every 6 months"
sunset_policy: "Superseded upon next major tools-platform governance update"
---

<div align="center">

# ⚖️ Kansas Frontier Matrix — Governance & Provenance Tools (v11.2.6)
`tools/governance/README.md`

**Purpose**  
Define the governance + provenance tooling that records **what ran**, **what changed**, **what passed**, and **what is publishable** under FAIR+CARE oversight.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/License-MIT-green" />

</div>

---

## 📘 Overview

The `tools/governance/` module is the KFM **provenance + governance consolidation layer**. It:

- aggregates validation, ETL, telemetry, and AI audit outputs
- appends governed records into ledgers (append-only, reviewable)
- produces release-facing governance manifests linked to SBOM + attestations
- enforces publication constraints (license, sensitivity, sovereignty, CARE labels)

This layer is designed to run in CI/CD, release workflows, and controlled backfill jobs.

## 🗂️ Directory Layout

~~~text
📁 tools/
└── 📁 governance/                              — Governance + provenance tooling
    ├── 📄 README.md                            — This document
    ├── 📄 governance_sync.py                   — Aggregate + normalize governance signals
    ├── 📄 certification_audit.py               — FAIR+CARE / ethics / sovereignty evaluation
    ├── 📄 ledger_update.py                     — Append ledger entries (deterministic format)
    ├── 📄 governance_manifest_generator.py      — Build release governance manifest bundle
    └── 🧾 metadata.json                         — JSON-LD context + mapping configuration
~~~

Notes:
- Checksum validation belongs to the validation layer (e.g., `tools/validation/**`) and is referenced from governance manifests (do not duplicate hashing logic here).

## 🧭 Context

KFM pipeline placement (tooling view):

~~~text
ETL outputs
  ↓
tools/validation/        — schema + integrity checks
  ↓
tools/governance/        — consolidate → decide → record
  ↓
releases/**              — signed bundles (SBOM, manifest, telemetry)
  ↓
catalogs + graph + APIs  — STAC/DCAT/PROV → Neo4j → API → UI
~~~

Governance tools must not “fix” data. They record results, decisions, and provenance so downstream systems can trust what they ingest.

## 🧱 Architecture

Core scripts (responsibilities are stable; exact CLI flags may vary by release):

- `governance_sync.py`
  - inputs: normalized outputs from validation/audit/telemetry layers
  - output: a staging bundle used by the audit + ledger steps

- `certification_audit.py`
  - evaluates: FAIR+CARE, ethics constraints, sovereignty policy, accessibility requirements (where applicable)
  - output: a deterministic certification decision (`certified` / `provisional` / `blocked`) plus reasons

- `ledger_update.py`
  - writes: append-only governance/provenance events (machine-readable; schema-validated)
  - must record: inputs used, outputs generated, and the responsible agent (human or bot)

- `governance_manifest_generator.py`
  - builds: release governance manifest bundle referencing SBOM/attestations/telemetry
  - output is pinned into `manifest_ref` for the release

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["ETL / Validation / AI / Telemetry Outputs"] --> B["governance_sync.py\nNormalize + stage"]
  B --> C["certification_audit.py\nFAIR+CARE / ethics / sovereignty"]
  C --> D["ledger_update.py\nAppend governance ledger"]
  D --> E["governance_manifest_generator.py\nRelease manifest bundle"]
  E --> F["Publication boundary\n(releases/**, catalogs, graph, APIs)"]
~~~

## 📦 Data & Metadata

Typical artifacts this module references or produces:

- Governance ledgers (append-only):
  - `data/reports/audit/**` (exact filenames are governed by schema + release)

- Release bundles:
  - `releases/**/manifest.zip`
  - `releases/**/sbom.spdx.json`
  - `releases/**/focus-telemetry.json`

Retention guidance (governed; see `ttl_policy`):

| Artifact | Retention | Notes |
|---|---:|---|
| Ledger records | Permanent | Canonical provenance |
| Release manifests | Permanent | Release boundary evidence |
| Staging bundles | ≥ 1 year | Safe to rotate after manifesting |

## 🌐 STAC, DCAT & PROV Alignment

Governance outputs must remain interoperable with KFM catalogs + graph.

- DCAT: governance artifacts may be represented as catalog records; `semantic_document_id` maps to a stable identifier.
- STAC: releases can expose governed artifacts as non-spatial Items/Assets.
- PROV-O: ledger entries must be expressible as `prov:Activity` / `prov:Entity` / `prov:Agent` links.

Schematic example (illustrative only):

~~~json
{
  "governance_id": "kfm_gov_record_YYYYMMDD_###",
  "entity_type": "dataset",
  "dataset_id": "processed_example_v11",
  "certification_status": "certified",
  "prov": {
    "wasGeneratedBy": "prov:Activity/kfm-governance-run-<id>",
    "used": ["prov:Entity/input-report-<id>"],
    "wasAssociatedWith": "prov:Agent/kfm-governance-bot"
  },
  "integrity": {
    "sha256": "sha256-<placeholder>",
    "sbom": "releases/<ver>/sbom.spdx.json",
    "manifest": "releases/<ver>/manifest.zip"
  }
}
~~~

## 🧪 Validation & CI/CD

This documentation and its referenced schemas are expected to pass the repo’s CI profiles, including:

- markdown formatting and structure checks (KFM-MDP)
- schema validation for front-matter + ledger/manifests
- provenance and link checks (refs must resolve inside the repo)
- secret/PII scanning (no credentials, no personal data)

CI entrypoint is typically the monorepo workflow (see `.github/workflows/kfm-ci.yml`).

## ⚖ FAIR+CARE & Governance

Governance is binding. This module must support:

- Authority to Control: sovereignty policy + classification gates
- Responsibility: who/what/when recorded for every decision
- Ethics: narratives and publish decisions cannot exceed evidence
- Collective Benefit: transparency where public exposure is allowed

Operational constraints:

- Never record secrets (tokens, keys) in ledgers or manifests.
- Avoid precise sensitive locations; use approved generalization/masking rules.
- Prefer stable IDs over raw names in audit records.

## 🧠 Story Node & Focus Mode Integration

Focus Mode may summarize governance state, but it must not override it.

- Story Nodes should link to governed evidence (ledger ID + manifest ref) when presenting certification status.
- AI summaries must treat `certification_status` and `care_label` as authoritative fields.

## 🕰️ Version History

| Version | Date | Summary |
|---:|---:|---|
| **v11.2.6** | 2025-12-15 | Updated to KFM-MDP v11.2.6; normalized approved H2 headings; converted internal fences to `~~~`; refreshed release refs to v11.2.6. |
| v11.2.2 | 2025-11-27 | Introduced v11 governance tool README format and expanded metadata/provenance fields. |
| v11.0.0 | 2025-11-24 | v11 governance platform alignment; clarified checksum validation separation. |
| v10.2.2 | 2025-11-12 | JSON-LD exports; STAC/DCAT parity; signed ledger integration; telemetry wiring. |
| v10.0.0 | 2025-11-10 | Initial governance tools documentation. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

[⬅️ Tools Index](../README.md) ·
[🧱 Tools Architecture](../ARCHITECTURE.md) ·
[🏛️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>