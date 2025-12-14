---
title: "📦 Kansas Frontier Matrix — Staging Data Workspace (Diamond9 Omega / CrownInfinityOmega Ultimate Certified)"
path: "data/work/staging/README.md"
version: "v11.1.0"
last_updated: "2025-11-19"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.1.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.1.0/manifest.zip"
telemetry_ref: "../../../releases/v11.1.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-work-staging-v11.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "Internal · FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
status: "Active / Enforced"
doc_kind: "Data Layer"
intent: "staging-workspace"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Verified"
---

<div align="center">

# 📦 **Kansas Frontier Matrix — Staging Data Workspace**  
`data/work/staging/README.md`

**Purpose**  
Define the controlled, FAIR+CARE-supervised **staging environment** for KFM datasets.  
This workspace is the **pre-publication validation zone** where datasets undergo schema alignment, FAIR+CARE audits, checksum verification, provenance registration, and telemetry recording before promotion into governed publication layers.

</div>

## 📘 Overview

The Staging Workspace bridges:

**raw ingestion → temporary processing → validation → ethics review → governance registration → promotion**

All datasets entering staging are subject to:

- deterministic ETL normalization (when applicable)
- schema + JSON-schema compliance (where schemas exist)
- FAIR+CARE ethics validation
- provenance chain generation (PROV-O)
- checksum and manifest integrity checks
- telemetry v11 sustainability metrics capture
- governance approval workflow
- pre-STAC/DCAT metadata preparation

This directory is **internal-only** and is **not** published directly.

## 🗂 Directory Layout

~~~text
data/
└── work/
    └── staging/
        ├── README.md
        ├── tabular/
        │   ├── tmp/
        │   ├── normalized/
        │   ├── validation/
        │   └── logs/
        ├── spatial/
        │   ├── tmp/
        │   ├── validation/
        │   └── logs/
        └── metadata/
            ├── tmp/
            ├── validation/
            └── logs/
~~~

Directory semantics:

- `tmp/` — ephemeral transformation outputs (may be overwritten; not authoritative)
- `normalized/` — schema-aligned intermediate artifacts (tabular-first; may be used elsewhere if required)
- `validation/` — QC, FAIR+CARE, checksum, and compliance results
- `logs/` — execution history, telemetry, audit traces (no secrets / no PII)

All staging data MUST remain isolated from production/published layers.

## 🧭 Context

Staging is a governed workspace for datasets that are not yet eligible for publication.

Key boundaries:

- **Raw intake** belongs in `data/**/raw/**` (immutable source-of-record evidence).
- **Staging** belongs here (`data/work/staging/**`) for pre-publication checks and controlled iteration.
- **Published distributions** belong in governed output layers (e.g., processed/published surfaces defined by the repo’s data architecture).
- **Catalogs** (STAC/DCAT) and **lineage** (PROV/OpenLineage) must be authored/registered from governed locations, not from ad-hoc scratch artifacts.

Staging’s job is to make promotion decisions **repeatable**, **auditable**, and **governance-safe**.

## 🗺 Diagrams

~~~mermaid
flowchart LR
  A[Raw Intake] --> B[Staging: tmp/]
  B --> C[Staging: normalized/ (when applicable)]
  C --> D[Staging: validation/]
  D --> E{FAIR+CARE + Governance Review}
  E -->|passed| F[Promotion to Governed Publication Layers]
  E -->|failed| G[Remediate + Re-run Deterministic Checks]
  D --> H[Telemetry + Logs]
  H --> E
~~~

## 🧠 Story Node & Focus Mode Integration

Staging is **not** a narrative evidence surface.

- Story Nodes and Focus Mode should reference **promoted, governed** datasets and their catalogs/lineage records.
- Staging telemetry and validation outputs can inform sustainability and quality dashboards, but should be treated as **pre-publication** and **mutable** until promotion.
- Promotion is the point where identifiers and provenance become stable enough to support narrative assertions.

## 🧪 Validation & CI/CD

Before promotion, staging datasets SHOULD pass the applicable gates:

- JSON schema validation (where a schema exists)
- FAIR+CARE certification checks
- checksum integrity checks (sha256 + manifest comparison)
- provenance chain validation (PROV-O completeness / consistency)
- licensing checks (including open-data compatibility when relevant)
- telemetry completeness (energy / carbon / coverage fields per telemetry schema)
- governance approval workflow outcome
- spatial datasets (when applicable):
  - CRS enforcement (e.g., EPSG:4326 where required by contract)
  - topology QA / geometry validity
- tabular datasets (when applicable):
  - field-type enforcement
  - missingness checks
  - key integrity checks (PK/FK where defined)

Validation artifacts SHOULD be written to:

- `data/work/staging/**/validation/` (stage-local evidence)
- and, if the repo uses centralized reporting roots, to:
  - `data/reports/validation/`
  - `data/reports/fair/`
  - `data/reports/audit/`

No validation output may contain secrets, credentials, signed URLs, or PII.

## 📦 Data & Metadata

Staging prepares and isolates three major intermediate domains:

- **Tabular** intermediate datasets (normalized tables)
- **Spatial** intermediate datasets (vectors, rasters)
- **Metadata** bundles (validation outputs, schema specs, pre-catalog records)

Each staged dataset SHOULD carry (or be linkable to) a minimal staging metadata record that includes:

- a stable staging identifier (string)
- dataset type (`tabular` / `spatial` / `metadata`)
- schema version reference (if applicable)
- validation state (`in_review`, `passed`, `failed`)
- checksum (sha256; temporary integrity record)
- FAIR+CARE status
- timestamps (ASCII ISO 8601)
- governance pointer for ethics review
- telemetry block (e.g., `energy_wh`, `carbon_gco2e`, coverage)

Example (illustrative):

~~~json
{
  "id": "staging_tabular_environmental_indicators_v11.1.0",
  "dataset_type": "tabular",
  "source": "data/raw/climate/noaa_temperature.csv",
  "schema_version": "v3.3.0",
  "records_processed": 55204,
  "validation_status": "in_review",
  "checksum_sha256": "sha256:3e9bcfa27d14fbb0ad0c2c4afd0f584c94f00468bc930a7a7fa191c3b63a2911",
  "fairstatus": "in_review",
  "telemetry": {
    "energy_wh": 7.4,
    "co2_g": 9.8,
    "validation_coverage_pct": 100
  },
  "governance_ref": "data/reports/audit/data_provenance_ledger.json",
  "created": "2025-11-19T20:01:00Z"
}
~~~

Retrieval examples:

~~~python
import json

with open("data/work/staging/tabular/validation/validation_report.json", "r", encoding="utf-8") as f:
    report = json.load(f)

print(report.get("status"))
~~~

~~~bash
ls data/work/staging/spatial/
~~~

~~~cypher
MATCH (s:StagingEntity)
RETURN s.id, s.validation_status, s.telemetry_energy_wh;
~~~

## 🌐 STAC, DCAT & PROV Alignment

Staging is **pre-catalog** and **pre-publication**, but it must be catalog-ready.

### PROV-O entity requirements

All staging datasets SHOULD record:

- a `prov:Entity` identifier (UUID or stable staging id)
- sha256 checksum (temporary integrity record)
- dataset type (tabular/spatial/metadata)
- schema version reference (if applicable)
- validation state (`in_review`, `passed`, `failed`)
- FAIR+CARE status
- temporal metadata (ASCII ISO 8601)
- governance pointer for ethics review
- telemetry block (e.g., `energy_wh`, `carbon_gco2e`)

Entities may change while in staging; upon promotion they become governed/stable per the publication layer’s immutability rules.

### Activity requirements

Activities executed inside staging include:

- normalization pipelines
- schema validation
- FAIR+CARE ethics auditing
- explainability/bias evaluation (AI workflows, when applicable)
- checksum generation + manifest comparison
- metadata harmonization (STAC/DCAT alignment preparation)
- governance review procedures

Each activity SHOULD log:

- pipeline version
- parameter digest (ASCII hash)
- execution timestamp
- validation coverage
- associated agents
- promotion eligibility outcome

Represent activities as PROV-O `prov:Activity`.

### Agent requirements

Agents involved in staging workflows SHOULD be modeled as PROV-O `prov:Agent`, including:

- `@kfm-staging` — staging pipeline stewards
- `@kfm-architecture` — schema alignment oversight
- `@faircare-council` — ethics and CARE supervision
- `@kfm-security` — checksum/integrity oversight
- `@kfm-data` — governance lifecycle management

### STAC/DCAT preparation

Staging must prepare (but not publish directly):

- STAC-compatible extents, assets, and identifiers
- DCAT-compatible dataset/distribution fields (title/description/license/publisher/coverage)
- linkable provenance references for promoted assets

## 🧱 Architecture

Promotion contract (high-level):

- staging artifacts are mutable and internal
- promotion produces governed artifacts:
  - publishable data distributions
  - catalogs (STAC/DCAT)
  - provenance registrations (PROV/OpenLineage)
  - release manifests / checksums / SBOM references

Telemetry integration:

- `telemetry_ref` points to the release telemetry bundle for v11.1.0
- `telemetry_schema` defines required fields and validation expectations for staging telemetry reporting

Roadmap (planning targets):

- v11.2 — AI-assisted staging anomaly detection
- v11.3 — schema auto-alignment pipeline for tabular/spatial
- v11.4 — integration of staging metadata into Focus Mode v3 timelines
- v11.5 — automated promotion scoring engine

## ⚖ FAIR+CARE & Governance

Staging is governed and enforced:

- internal-only; never published directly
- FAIR+CARE Council oversight for ethics and CARE supervision
- integrity controls: checksums + manifest comparisons
- governance approval required for promotion eligibility
- no secrets, credentials, signed URLs, or PII allowed anywhere in this workspace
- rights/licensing must be checked before any external publication

Authoritative governance reference:

- `../../../docs/standards/governance/ROOT-GOVERNANCE.md`

## 🕰 Version History

| Version | Date | Author | Summary |
|---:|---:|---|---|
| v11.1.0 | 2025-11-19 | `@kfm-staging` | Full KFM-MDP v11 rebuild; validation logic expansion; telemetry v11 alignment; directory normalization. |
| v11.0.0 | 2025-11-15 | `@kfm-staging` | Initial v11 staging layer migration. |
| v10.0.0 | 2025-11-09 | `@kfm-staging` | Original staging workspace definition. |

<div align="center">

[⬅️ Back to Work Layer](../README.md) ·
[📐 Data Architecture](../../../docs/ARCHITECTURE.md) ·
[⚖️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
