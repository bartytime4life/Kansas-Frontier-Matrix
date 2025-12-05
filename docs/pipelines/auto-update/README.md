---
title: "⚡ KFM v11.2.3 — Event-Driven Auto-Update Ingestion Pipeline (SNS → SQS · Incremental Refresh · STAC-First)"
description: "Event-driven update detection, incremental deltas, deterministic catalog writing, and reliability primitives for auto-updating KFM datasets using SNS → SQS and STAC-first contracts."
path: "docs/pipelines/auto-update/README.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x ingestion-contract compatible"
status: "Active · Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/auto-update-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/auto-update-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Pipeline Specification"
intent: "event-driven-auto-update-ingestion"
category: "Pipelines · Auto-Update · SNS/SQS · STAC"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "Kansas / United States"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
immutability_status: "version-pinned"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major auto-update ingestion standard"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# ⚡ KFM v11 — Event-Driven Auto-Update Ingestion Pipeline  
`docs/pipelines/auto-update/README.md`

**Purpose**  
Define the governed, event-driven auto-update ingestion pattern for KFM datasets using **SNS → SQS → Workers → STAC**, including incremental refresh, idempotency, reliability primitives, and FAIR+CARE-aligned governance gates.

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.3-purple" />
<img src="https://img.shields.io/badge/Updates-SNS_%E2%86%92_SQS-orange" />
<img src="https://img.shields.io/badge/Metadata-STAC_first-green" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

### 1. Why this pipeline pattern exists

The **Auto-Update Ingestion Pipeline** defines a reusable pattern for **event-driven, incremental updates** across KFM datasets:

- Eliminate polling via **push-style notifications** for new/updated assets.  
- Support **idempotent, delta-only refreshes** using content hashes/ETags.  
- Make **STAC the source-of-truth** for updated geospatial assets.  
- Embed **validation, governance, and reliability gates** into every update unit.  
- Standardize behavior across domains (hydrology, soils, atmo, archives, etc.).

This specification is **normative** for any KFM pipeline that consumes upstream update events via SNS/SQS and writes to STAC.

### 2. Scope

Applies to:

- All SNS→SQS-driven ingestion flows.  
- Auto-update pipelines that perform incremental refreshes on KFM datasets.  
- Pipelines that promote data between `work` → `processed` → `stable` layers.  
- Any system where **STAC catalogs** are treated as the canonical asset registry.

Out of scope:

- Fully manual ingest workflows.  
- Non-event-driven bulk backfills (unless they explicitly adopt this contract).  

---

## 🗂️ Directory Layout

~~~text
docs/pipelines/auto-update/
├── 📄 README.md                     # This file (auto-update pipeline spec)
│
├── 📨 sns-schema/                   # SNS event definitions
│   └── 📄 message-v1.json
│
├── 📬 sqs-contract/                 # Consumer contract, idempotency keys, retry rules
│   └── 📄 README.md
│
├── 🔍 validation-gates/             # Schema, QA, CARE/FAIR, provenance checks
│   ├── 📄 schema-check.md
│   ├── 📄 qa-rules.md
│   └── 📄 governance-gate.md
│
├── 📦 processors/                   # Workers: ingestion → transform → STAC write
│   ├── 📄 parquet-updater.md
│   ├── 📄 raster-updater.md
│   └── 📄 vector-updater.md
│
├── 🗺️ stac-writers/                 # Atomic STAC Item/Collection creation
│   ├── 📄 item-writer.md
│   └── 📄 collection-writer.md
│
├── ⏱️ watermarks/                   # Event-time watermarks, lag monitors
│   └── 📄 watermark-spec.md
│
└── 📊 telemetry/                    # OTel spans, metrics, error budgets
    └── 📄 metrics.md
~~~

Author rules:

- Each listed subdirectory **must** contain a `README.md` or equivalent spec.  
- Directory trees in docs use fenced `text` blocks and emoji-prefixed entries per KFM-MDP.  

---

## 🧭 Context

The auto-update pattern sits between **upstream publishers** and **KFM’s STAC-first catalogs**:

- Upstream systems publish thin **SNS messages** describing what changed.  
- SNS fanned-out messages land in **SQS queues** per dataset or domain.  
- KFM workers consume messages, enforce validation & governance gates, and perform **atomic STAC updates**.  
- Watermarks and WAL ensure replay-safety and ordered promotion to `stable`.

This pattern must align with:

- KFM-MDP v11.2.x (documentation & governance).  [oai_citation:0‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.4.pdf](file-service://file-57iDMaU6FoN7pZ8e5HbsPp)  
- STAC 1.x + KFM-STAC extensions.  
- DCAT 3.0 dataset-level cataloging.  
- PROV-O + OpenLineage for run-level lineage.  [oai_citation:1‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
- GeoSPARQL for spatial semantics where applicable.  [oai_citation:2‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  

---

## 🧱 Architecture

### 1. Event flow: SNS → SQS → Worker → STAC

~~~mermaid
flowchart LR
    P[Upstream Publisher] --> S[SNS Topic]
    S --> Q[SQS Queue (per dataset/domain)]
    Q --> W[Auto-Update Worker]
    W --> G[Validation & Governance Gates]
    G -->|pass| C[Candidate STAC]
    C --> V[STAC Validation]
    V -->|promote| K[Canonical STAC Catalog]
    G -->|fail| D[DLQ / Quarantine + Replay Ticket]
~~~

**Hot path (realtime):**

1. Publisher emits compact update event to SNS.  
2. SNS routes to SQS queues by dataset/product/priority.  
3. Worker consumes SQS message and executes:
   - Idempotency and dedupe check.  
   - Conditional fetch (skip if ETag unchanged).  
   - Transform into KFM-ready structure.  
   - Validation & governance gates (Schema, QA, CARE/FAIR, PROV).  
   - **Atomic STAC write** (Item/Collection).  

**Batch path (scheduled/backfill):**

- Cron/EventBridge emits synthetic messages using the same schema.  
- Same gates, same STAC rules; no bypass of protections.  

---

### 2. SNS Event Schema (v1)

Example SNS message payload:

~~~json
{
  "event_time": "2025-12-04T03:14:15Z",
  "dataset": "usgs/streamflow",
  "asset_uri": "s3://bucket/path/file.parquet",
  "content_etag": "W/\"a1b2c3\"",
  "granule_start": "2025-12-04T03:00:00Z",
  "granule_end": "2025-12-04T03:59:59Z",
  "priority": "high",
  "schema_version": "1.0"
}
~~~

Design principles:

- **Stable** — schema is additive; old events remain valid.  
- **Minimal** — only pointers + minimal metadata (no heavy payloads).  
- **Deterministic** — `dataset + asset_uri + content_etag` is sufficient to reproduce the update.  

Schema details and JSON Schema live in `sns-schema/message-v1.json`.

---

### 3. Incremental Refresh Model

Each dataset supports versioned, idempotent upserts using the keys:

| Key                                                                 | Purpose                                      |
|---------------------------------------------------------------------|----------------------------------------------|
| `asset_uri`                                                         | Unique pointer to raw or derived data.       |
| `content_etag`                                                      | Detects content change; skip if unchanged.   |
| `idempotency_key = sha256(dataset + asset_uri + content_etag)`      | Deduplication and safe retries.              |
| Checkpoint store                                                    | Tracks last granule processed.               |

Workers:

- Refresh only **deltas**, never blindly recompute an entire dataset.  
- Log idempotency hits/misses to telemetry and provenance.  
- Maintain per-dataset checkpoint state in a durable store.  

---

### 4. Validation & Governance Gates

All ingest units must pass three gate families before promotion:

#### 4.1 Schema Gate

- Structural validity (JSON/Parquet schema).  
- CRS and geospatial consistency (where applicable).  
- Time monotonicity (no inverted or impossible ranges).  

#### 4.2 QA Gate

- Range checks and statistical sanity checks.  
- Geometry validity (e.g., polygons not self-intersecting).  
- Null/NaN thresholds and severity tiers.  

#### 4.3 Governance Gate

- CARE restrictions and sovereignty flags.  
- Provenance completeness (entities, activities, agents).  [oai_citation:3‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
- STAC licensing and usage terms.  
- Sensitivity masking/generalization where required (e.g., heritage sites).  

**Gate failures are quarantined** (DLQ / quarantine bucket); workers **never** publish STAC updates on red.

---

### 5. STAC as Source-of-Truth

#### 5.1 Writing rules

- STAC Items are created/updated **atomically** via a temp → validate → promote pattern:  
  1. Write candidate Item to a staging catalog.  
  2. Validate (STAC schema + KFM business rules).  
  3. Promote to canonical catalog only on success.  

- Validation targets:
  - STAC 1.x core.  
  - KFM-STAC extensions (e.g., `raster:*`, `proj:*`, `processing:*`).  

#### 5.2 Collections

- Collections maintain **stable extents** with versioned summaries.  
- Each update attaches lineage:
  - OpenLineage/PROV-O references for the ingest run.  [oai_citation:4‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
  - QA/SLO status when available.  

The STAC catalog is the **authoritative index** of which assets exist and which versions are active.

---

### 6. Watermarks & Ordered Backfills

Per-dataset and per-partition **event-time watermarks**:

- Workers backfill only data **≤ watermark**.  
- Watermark advances only when **all partitions converge**.  
- Prevent mixed ordering and race conditions in concurrent environments.  
- Allow shared infrastructure across domains (hydrology, soils, atmo, imagery) while preserving ordering guarantees.

Details and invariants live in `watermarks/watermark-spec.md`.

---

### 7. Reliability Model

Reliability primitives:

- **Deterministic idempotency keys**: `sha256(dataset + asset_uri + content_etag)`.  
- **WAL-backed replay**: reprocess without duplication, using WAL as source-of-truth.  
- **Safe retries**: SQS visibility timeouts tuned to data size and processing time.  
- **Canary mode**: route a fraction of events through new logic; compare outputs and telemetry.  
- **Kill-switch flags per dataset**: immediate disable of auto-updates on governance or reliability incidents.

Conceptual checkpoint/state tables:

| Table         | Shape                                                      |
|---------------|------------------------------------------------------------|
| `ingest_state`| `(dataset, asset_uri) → {etag, version, processed_at}`     |
| `checkpoints` | `(dataset, partition) → {watermark, updated_at}`           |
| `qa_findings` | `(run_id, dataset, severity, rule)`                        |

---

### 8. Rollout Sequence (Recommended)

1. Define SNS message schema and SQS DLQs.  
2. Implement **idempotent consumer** with persistent state store.  
3. Add **validation + governance gates** (Schema, QA, CARE/FAIR).  
4. Integrate **STAC atomic writer** (Items/Collections).  
5. Add **OpenTelemetry** instrumentation and connect dashboards.  
6. Enable SNS routing from upstream publishers.  
7. Scale workers and tune concurrency/visibility timeouts.  
8. Enable **cron-based backfills** and QA scans using the same contract.  

---

## 🧪 Validation & CI/CD

CI/CD requirements for auto-update pipelines:

- **Schema tests** for SNS/SQS envelopes and STAC outputs.  
- **Unit/integration tests** for workers, gates, and STAC writers.  
- **Lineage checks** ensuring OpenLineage events are emitted for each run.  
- **Governance tests** verifying CARE/sovereignty policies and kill-switches.  
- **Telemetry conformance tests** using `telemetry_schema`, `energy_schema`, and `carbon_schema`.  

A typical CI workflow (`kfm-ci.yml`) should include:

- Markdown + YAML lint for docs under `docs/pipelines/auto-update/`.  
- Validation of `sns-schema/message-v1.json`.  
- Replay tests for WAL-backed reprocessing.  

---

## 📦 Data & Metadata

Each processed update must result in:

- A STAC Item (or update) for each promoted asset.  
- Updated Collection summaries (extent, temporal coverage, statistics where applicable).  
- A telemetry record (energy, carbon, runtime, counts) appended to `auto-update-telemetry.json`.  
- A lineage record stored via OpenLineage/PROV-O, referencing:
  - Input assets (by URI/hash).  
  - Config version.  
  - Software agent and run parameters.  

All metadata must be:

- Machine-extractable (JSON/JSON-LD).  
- Compatible with KFM-STAC and DCAT mappings.  
- Safe for public exposure given `care_label` and `classification`.  

---

## 🌐 STAC, DCAT & PROV Alignment

- **STAC** — asset-level, spatiotemporal metadata and processing history.  
- **DCAT** — dataset-level cataloging for discovery and governance.  
- **PROV-O/OpenLineage** — detailed run-level provenance (activities, entities, agents).  [oai_citation:5‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  

Examples:

- STAC Item → `dcat:Distribution` for a DCAT Dataset.  
- Lineage run → `prov:Activity` with `prov:used` and `prov:generated` links.  
- Dataset versioning via `prov:wasDerivedFrom` and DCAT version fields.  

The auto-update pipeline is responsible for keeping these layers **consistent and mutually referential**.

---

## ⚖ FAIR+CARE & Governance

FAIR:

- **Findable:** Every promoted asset has a STAC Item reachable via catalogs and search.  
- **Accessible:** Access URLs and licenses are explicit and enforced.  
- **Interoperable:** Uses STAC, DCAT, PROV-O, and GeoSPARQL-aligned geometry where appropriate.  [oai_citation:6‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  
- **Reusable:** Clear licensing, provenance, and versioning for each update.  

CARE:

- **Collective Benefit:** Auto-updates improve timeliness and reliability for affected communities.  
- **Authority to Control:** Respect `sovereignty_policy` for any dataset intersecting Indigenous or sensitive contexts.  
- **Responsibility:** Failed governance or masking gates **must** block promotion to `stable`.  
- **Ethics:** No auto-update may bypass review where specified by policy (e.g., for heritage-sensitive datasets).  

Governance hooks:

- `governance_ref`, `ethics_ref`, `sovereignty_policy` in front-matter are binding references.  
- Auto-update behavior must be consistent with these standards and subject to periodic review.  

---

## 🕰️ Version History

| Version | Date       | Notes                                             |
|--------:|------------|---------------------------------------------------|
| v11.2.3 | 2025-12-04 | Initial governed release of the auto-update spec. |

---

<div align="center">

⚡ **Kansas Frontier Matrix — Event-Driven Auto-Update Ingestion Pipeline (v11.2.3)**  
Scientific Insight · Deterministic Pipelines · FAIR+CARE Ethics · Sustainable Intelligence  

[📘 Pipelines Index](../README.md) · [⚖ Governance](../../standards/governance/ROOT-GOVERNANCE.md) · [📦 Data & STAC Catalogs](../../data/README.md)

</div>