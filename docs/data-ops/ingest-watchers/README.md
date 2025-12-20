---
title: "Ingest Watchers — DataOps README"
path: "docs/data-ops/ingest-watchers/README.md"
version: "v0.1.0"
last_updated: "2025-12-20"
status: "draft"
doc_kind: "Guide"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:data-ops:ingest-watchers:readme:v0.1.0"
semantic_document_id: "kfm-data-ops-ingest-watchers-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data-ops:ingest-watchers:readme:v0.1.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# Ingest Watchers — DataOps README

> Status note (draft): The *concept* of ingest automation is described in system docs, but the concrete
> implementation (daemon vs cron vs queue worker, exact config paths, entrypoints) is **not confirmed in repo**
> from the materials available to this document. Treat all “runbook” and “contract” items below as a **draft
> operating target** until the repo implementation is verified and linked.

## 📘 Overview

### Purpose
- Define the DataOps-facing responsibilities and operating expectations for **ingest watchers**: mechanisms that
  detect new/updated source assets (scheduled harvests or manual uploads) and hand them off to the governed
  KFM pipeline.
- Ensure watchers preserve KFM invariants:
  - Canonical ordering: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
  - Required staging: **`data/raw/ → data/work/ → data/processed/ → data/stac/`** (+ other outputs as needed).
- Provide a minimal runbook, failure-mode map, and validation checklist for DataOps.

### Scope
| In Scope | Out of Scope |
|---|---|
| Detect/receive new sources (scheduled harvests, manual uploads) | Parser implementation details (PDF/CSV/OCR/GDAL/etc.) |
| Capture ingest metadata (source, contributor, date, license, checksums) | Deep normalization/enrichment logic |
| Trigger the governed ETL run + record run IDs/logs | Graph modeling/ontology decisions |
| Quarantine + retry rules (high-level) | UI behavior and UX decisions |
| Observability expectations (signals + auditability) | Infrastructure-as-code / deployment specifics (unless linked) |

### Audience
- Primary: DataOps / ETL maintainers
- Secondary: Catalog (STAC/DCAT/PROV) maintainers, Graph maintainers, API maintainers

### Definitions
- Link: `docs/glossary.md` *(not confirmed in repo; add if missing)*
- Terms used in this doc:
  - **Ingest watcher**: a process/pattern that detects new source material and produces an *ingest event* that the
    ETL pipeline can process.
  - **Ingest event**: a record describing “what arrived,” “where,” “when,” and “under what license,” plus integrity
    signals (hash/size/type).
  - **Harvest**: scheduled import of online datasets/APIs (automated).
  - **Source Upload**: manual upload by authorized contributors (interface-driven).
  - **Quarantine**: segregated holding area for suspicious/invalid/unparseable inputs.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline invariants | `docs/MASTER_GUIDE_v12.md` | Docs/Governance | Canonical ordering + staging expectations |
| System ingestion description | `docs/architecture/` *(recommended)* | Docs/Governance | “System Structure and Scope” describes ingestion modes + determinism expectations |
| Ingest watcher configs | *(not confirmed in repo)* | DataOps | Link actual config once located |
| ETL runner entrypoint | *(not confirmed in repo)* | DataOps/ETL | Link actual command/module once located |
| Run logs | `mcp/runs/` *(expected)* | DataOps | Store deterministic run outputs + provenance pointers |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] All claims link to governed docs / schemas / tickets / commits (as applicable)
- [ ] Watcher responsibilities vs non-responsibilities are explicit
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] “Not confirmed in repo” items enumerated as follow-ups

## 🗂️ Directory Layout

### This document
- `path`: `docs/data-ops/ingest-watchers/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Raw inputs | `data/raw/` | Unmodified source captures (as received) |
| Working/intermediate | `data/work/` | Temporary transforms, extraction intermediates |
| Processed outputs | `data/processed/` | Cleaned/normalized datasets ready for cataloging |
| STAC | `data/stac/` | STAC Collections/Items JSON (catalog artifacts) |
| DCAT | `data/catalog/dcat/` | DCAT dataset records |
| PROV | `data/prov/` | Provenance bundles / activity records |
| Pipelines | `src/pipelines/` | ETL + catalog build logic |
| Run artifacts | `mcp/runs/` | Deterministic run logs + evidence products |
| Docs | `docs/` | Standards, templates, governance, subsystem docs |

### 📁 File tree (expected canonical placement)
~~~text
📁 docs/
├── 📁 data-ops/
│   └── 📁 ingest-watchers/
│       └── 📄 README.md
├── 📄 MASTER_GUIDE_v12.md
└── 📁 templates/
    └── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
📁 data/
├── 📁 raw/
├── 📁 work/
├── 📁 processed/
├── 📁 stac/
├── 📁 catalog/
│   └── 📁 dcat/
└── 📁 prov/
📁 mcp/
└── 📁 runs/
📁 src/
└── 📁 pipelines/
~~~

## 🧭 Context

### What ingest watchers are in KFM
KFM supports flexible ingestion modes (scheduled/automated harvests of online datasets/APIs and manual uploads
via an interface). Ingestion captures source metadata (source name, contributor, date, license) and the pipeline
detects source type to apply appropriate extraction. ETL is expected to be deterministic, logged, and idempotent
(no duplicates on re-run). *(Implementation specifics of the watcher mechanism are not confirmed in repo; this
README documents the intended operating envelope.)*

### Non‑negotiable invariants (must not break)
- **Ordering:** Watchers must feed **ETL first**, and ETL must emit **STAC/DCAT/PROV catalogs** before the graph is
  updated. Watchers must not “write directly to the graph” as a bypass.
- **Staging:** All ingest outputs should respect the required staging path:
  - `data/raw/ → data/work/ → data/processed/ → data/stac/` (+ any `data/reports/` outputs as needed)
- **Provenance:** Every downstream story/narrative experience depends on “no unsourced narrative” and “provenance
  is first-class.” Ingest is the start of that chain, so it must capture source identity and licensing.
- **API boundary:** The UI never reads Neo4j directly; all consumption is via API contracts. Watchers must not
  create UI-only side channels.

### Responsibilities (watcher) vs (ETL) vs (catalog)
| Step | Watcher responsibility | ETL responsibility | Catalog responsibility |
|---|---|---|---|
| Detect new source | ✅ yes | ❌ no | ❌ no |
| Capture raw bytes | ✅ yes (store/point to raw) | ✅ sometimes (if ETL fetches) | ❌ no |
| Integrity signals | ✅ yes (hash/size/type) | ✅ verify | ❌ no |
| Parsing/extraction | ❌ no | ✅ yes | ❌ no |
| Normalization/enrichment | ❌ no | ✅ yes | ❌ no |
| STAC/DCAT/PROV creation | ❌ no (must not) | ✅ produce required metadata inputs | ✅ validate + persist catalogs |
| Graph update | ❌ no | ✅ via governed graph ingest | ❌ no |
| Run logs + audit | ✅ minimal signals | ✅ full run logs | ✅ validation logs |

### Failure modes to plan for
- **Duplicate detection:** same file re-seen; must not create duplicate ETL loads.
- **Partial uploads:** file detected before upload complete (common in shared volumes).
- **Untrusted formats:** macro-enabled office docs, malformed PDFs, hostile ZIPs.
- **Remote flakiness:** intermittent 5xx, rate limits, timeouts.
- **License unknown:** missing or ambiguous license metadata.
- **Sensitive content:** culturally sensitive locations or PII accidentally present.

### Open questions (not confirmed in repo)
- Where are watcher configs stored? (`src/pipelines/...`, `tools/...`, `mcp/...`?)
- Are watchers long-running daemons, cron jobs, queue workers, or CI-triggered?
- Where is “quarantine” implemented (if at all)?
- What is the canonical “run id” format for linking ingest → PROV → STAC → graph?

## 🗺️ Diagrams

### End-to-end flow (conceptual)
~~~mermaid
flowchart LR
  subgraph Ingest
    W["Ingest Watcher(s)\n(scheduled harvest / manual upload detect)"] --> E["Ingest Event\n(metadata + integrity signals)"]
  end

  subgraph Data
    E --> R["data/raw/\n(raw capture or pointers)"]
    E --> P["ETL + Normalization\n(deterministic, logged, idempotent)"]
    R --> P
    P --> S["STAC Items + Collections\n(data/stac/)"]
    P --> D["DCAT dataset records\n(data/catalog/dcat/)"]
    P --> V["PROV lineage bundles\n(data/prov/)"]
  end

  S --> G["Neo4j Graph"]
  G --> A["API Layer"]
  A --> U["React/Map UI"]
  U --> N["Story Nodes"]
  N --> F["Focus Mode"]
~~~

### Watcher → ETL handoff (sequence)
~~~mermaid
sequenceDiagram
  participant W as Watcher
  participant R as Raw Store (data/raw)
  participant Q as Ingest Queue / Trigger (impl TBD)
  participant E as ETL Runner
  participant C as Catalog Build (STAC/DCAT/PROV)
  participant G as Graph Ingest

  W->>R: Write raw bytes or stable pointer
  W->>Q: Emit ingest event (id, uri, hash, license, contributor, timestamp)
  Q->>E: Trigger deterministic ETL run (run_id)
  E->>C: Produce catalog artifacts + validation outputs
  C->>G: Provide governed artifacts for graph ingest (no direct raw→graph)
~~~

## 📦 Data & Metadata

### Minimal ingest event record (draft; not confirmed in repo)
A watcher SHOULD be able to emit the following **minimum** metadata (as JSON/YAML or a durable message):

~~~json
{
  "ingest_event_id": "evt-<stable-id>",
  "observed_at": "2025-12-20T00:00:00Z",
  "capture_method": "scheduled_harvest|manual_upload|other",
  "source_name": "TBD",
  "source_uri": "https://... or file:///...",
  "raw_artifact_path": "data/raw/<domain>/... (or pointer)",
  "mime_type": "application/pdf",
  "size_bytes": 123456,
  "checksum_sha256": "hex...",
  "license": "TBD",
  "contributor": "TBD",
  "upstream_last_modified": "TBD",
  "notes": "optional"
}
~~~

### Sensitivity + redaction flags
- Watchers SHOULD record whether an ingest event may contain:
  - PII (names/addresses), sensitive sites, culturally sensitive content
  - licensing restrictions
- Watchers MUST NOT attempt to “infer sensitive locations” as an automated policy action (handled under governed
  review + downstream gates).

### Determinism + idempotency expectations
- Detect duplicates using stable identifiers (hash + source_uri + size + last_modified where applicable).
- Retries must not create new logical records unless content truly changed.
- If a harvest produces a new version, the ingest event should link predecessor/successor identifiers.

## 🌐 STAC, DCAT & PROV Alignment

### Alignment goal
Watchers are the first step in ensuring every asset and narrative can be traced back to source material via:
- **STAC IDs** (asset-level catalog)
- **DCAT identifiers** (dataset-level catalog)
- **PROV activity/run IDs** (lineage + reproducibility)

### Mapping (conceptual)
| Concept | Watcher emits | ETL/Catalog emits |
|---|---|---|
| Source capture | raw bytes/pointer + license metadata | STAC Asset link + license propagation |
| Provenance | ingest_event_id | PROV Activity (run_id) that used the raw entity |
| Dataset grouping | capture_method + source_name + domain | STAC Collection + DCAT dataset record |
| Versioning | checksum/last_modified + predecessor pointer | STAC/PROV version linkage + graph lineage |

## 🧱 Architecture

### Subsystem contract (draft)
For an “ingest watcher” subsystem to be considered production-ready in KFM, it SHOULD have:
- **Config-as-data** (YAML/JSON) describing watched sources, schedules, and destination domains *(not confirmed in repo)*.
- **Deterministic run logging** (each trigger results in a run record under `mcp/runs/` or equivalent).
- **Security posture**:
  - least privilege for filesystem + network
  - no execution of untrusted content
  - secrets via secret manager (not in repo)
- **Backpressure**:
  - bounded queue
  - rate-limited harvesters
  - quarantine for failures

### Interfaces (conceptual)
- Inputs:
  - Scheduled pull from URL/API endpoints (harvest)
  - Manual upload drop zone / UI-driven upload (source upload)
- Outputs:
  - Ingest event record
  - Raw artifacts in `data/raw/` (or stable pointers)
  - Trigger to ETL runner (mechanism TBD)

## 🧠 Story Node & Focus Mode Integration

- Focus Mode requires provenance-linked facts; ingest events must preserve:
  - source identity + license
  - stable artifact references
  - run IDs for transformations
- If any AI-generated enrichment is produced later, it must be clearly labeled and tied to sources and uncertainty;
  ingest watchers should ensure the provenance chain begins cleanly (no “mystery sources”).

## 🧪 Validation & CI/CD

### DataOps validation checklist (draft)
- [ ] Watcher emits ingest_event_id + observed_at + license + checksum (or justified exception)
- [ ] Duplicate detection verified (re-run does not duplicate)
- [ ] Partial upload handling verified (no ingest until file stable)
- [ ] Untrusted formats handled safely (no macro execution; zip bombs mitigated)
- [ ] ETL run is deterministic and logged (run_id linkable)
- [ ] Catalog outputs validate (STAC/DCAT/PROV schema validation)
- [ ] Provenance chain can be followed: ingest_event → run_id → STAC/DCAT → graph → API

### CI hooks (where applicable)
- Lint watcher configs (YAML schema / JSON schema)
- Validate STAC/DCAT/PROV artifacts generated by ingest-triggered runs
- Ensure run artifacts include checksums and input references

## ⚖ FAIR+CARE & Governance

- New ingestion sources require:
  - explicit license capture (or documented “unknown license” handling + human review)
  - sovereignty/CAR(E) review if culturally sensitive or community-owned data is involved
  - sensitivity classification review if locations/individuals are involved
- Any changes affecting security posture, redaction, or policy gates: **requires human review**.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-20 | Initial README scaffold for ingest watchers | TBD |
