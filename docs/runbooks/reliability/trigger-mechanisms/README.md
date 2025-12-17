---
title: "⏱️ KFM — Trigger Mechanisms Decision Guide (Webhook · Polling · Object-Event · Deployment)"
path: "docs/runbooks/reliability/trigger-mechanisms/README.md"
version: "v11.2.7"
last_updated: "2025-12-17"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Council · FAIR+CARE Oversight"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "Runbook"
intent: "kfm-trigger-selection-decision-guide"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY-4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PDC v11"
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

doc_uuid: "urn:kfm:doc:runbooks:reliability:trigger-mechanisms:v11.2.7"
semantic_document_id: "kfm-runbook-trigger-mechanisms-v11.2.7"
event_source_id: "ledger:kfm:doc:runbooks:reliability:trigger-mechanisms:v11.2.7"
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

# ⏱️ KFM — Trigger Mechanisms Decision Guide (Webhook · Polling · Object-Event · Deployment)

## 📘 Overview

### Purpose
This runbook provides a **practical, production-oriented decision guide** for selecting trigger mechanisms across KFM pipelines, CI/CD, and operational automation.

It standardizes **when to use**:
- Webhook (push) triggers
- Polling (sensor) triggers
- Object-event (cloud-native event bus) triggers
- Deployment / release lifecycle triggers

…while preserving **idempotency, observability, provenance, deterministic replay, and FAIR+CARE governance**.

### Scope

| In Scope | Out of Scope |
|---|---|
| Selection rules for trigger classes | Vendor-specific setup guides (AWS/GCP/Azure specifics) |
| Reliability + security requirements for triggers and handlers | Full event-bus architecture & procurement |
| Integration expectations (PROV emission, telemetry, catalog updates) | Application-level business logic of downstream pipelines |
| Failure modes, replay patterns, and kill-switch expectations | API contract changes (use API contract template if needed) |

### Audience
- Primary: Reliability / Platform Engineering; ETL & pipeline owners
- Secondary: Governance reviewers; security reviewers; SRE/operations

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Idempotency key**: deterministic key used to deduplicate trigger processing.
  - **Watermark**: persisted cursor used by polling to avoid missed/duplicate work.
  - **DLQ**: dead-letter queue/path for poison events and exhausted retries.
  - **Replay**: reprocessing from a persisted event log or re-run plan.
  - **At-least-once delivery**: duplicates are possible; handlers must dedupe.
  - **Object-event**: broker/emitter indicates an object lifecycle transition (e.g., “finalized”).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This runbook | `docs/runbooks/reliability/trigger-mechanisms/README.md` | Reliability Council | Canonical selection guide |
| Schemas | `schemas/` | Platform / Data Engineering | Telemetry + contract schemas live here (paths vary) |
| Pipelines | `src/pipelines/` | Pipeline owners | Triggered workloads execute here |
| Catalog outputs | `data/stac/` + `docs/data/` | Data Engineering | STAC/DCAT/PROV alignment & docs |
| Telemetry docs | `docs/telemetry/` | Reliability / Observability | Where signals are defined & governed |

> Note: Example handler/config paths in this runbook are illustrative; confirm actual module locations in-repo.

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Trigger taxonomy + selection rules are unambiguous
- [ ] Mandatory reliability controls are explicitly listed
- [ ] Validation steps listed and repeatable (even if commands are placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `docs/runbooks/reliability/trigger-mechanisms/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area
~~~text
docs/runbooks/reliability/trigger-mechanisms/
  README.md
  examples/
    trigger.webhook.example.yaml
    trigger.polling.example.yaml
    trigger.object_event.example.yaml
    trigger.deployment.example.yaml
~~~

## 🧭 Context

### Background
KFM integrates diverse upstream sources (data portals, storage buckets, CI systems, partner APIs). The *choice of trigger mechanism* directly determines reliability, security posture, observability quality, and governance traceability.

This guide exists to avoid common failure patterns:
- Duplicate processing and inconsistent catalogs (missing idempotency)
- Missed updates (polling windows, bad watermarks)
- Untraceable automation (no PROV/telemetry emission)
- Overshared sensitive payloads (logging and routing risks)

### Assumptions
- Treat most trigger delivery as **at-least-once** (duplicates are expected).
- Event ordering is not guaranteed across partitions/providers.
- Sources may be untrusted; payloads must be validated and minimized.
- Trigger handling must be safe under retries, restarts, and replays.

### Constraints / invariants
- Canonical pipeline ordering remains preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Every automated activation must be auditable (PROV + telemetry + ledger).

### Trigger taxonomy (KFM canon)

| Trigger Class | Signal Direction | Latency Profile | Typical Source |
|---|---|---|---|
| **Webhook (Push)** | Source → KFM | Near-real-time | Git, APIs, SaaS |
| **Polling (Sensor)** | KFM → Source | Interval-bound | Legacy APIs |
| **Object-Event** | Event Bus → KFM | Near-real-time | Cloud storage, queues/topics |
| **Deployment Event** | Platform → KFM | Near-real-time | CI/CD systems |

### Operational trade-off matrix

| Dimension | Webhook | Polling | Object-Event | Deployment |
|---|---|---|---|---|
| Latency | ✅ Immediate | ❌ Interval-bound | ✅ Immediate | ✅ Immediate |
| Infra cost | Low | Medium–High | Low | Low |
| Failure mode | Retries required | Missed window / bad cursor | Broker-managed (still dedupe) | Retries required |
| Security surface | Inbound endpoint | Outbound only | IAM-scoped | Tokenized |
| Cloud-native fit | Partial | No | Yes | Yes |
| Governance fit | High | Medium | Very High | High |

### Quick selection rules (decision flow)
1. If the platform emits **authoritative object lifecycle events** (e.g., “object finalized”) and you can scope access with IAM → prefer **Object-Event**.
2. Else if the source can **push signed events** to a controlled endpoint → prefer **Webhook**.
3. Else if the source cannot push (or inbound is prohibited) → use **Polling** with strict watermarks + budgets.
4. If the trigger is about a **release/deploy lifecycle** (smoke tests, rollback gating, freezing pipelines) → use **Deployment Events**.

### Selection rules (KFM-standard)

#### ✅ Use Webhook (Push) when
- You can securely expose an endpoint (HMAC/JWT, IP allowlist as appropriate).
- Near-real-time reactions matter.
- Event volume is moderate and meaningful.
- You can tolerate retries and duplicates.

**Required controls**
- Authenticate + verify signatures; reject unsigned payloads.
- Extract/compute an **idempotency key** from stable fields (event ID, commit SHA, object URI).
- Apply structured retries with exponential backoff (and cap).
- Route poison events to DLQ.

**Examples**
- Git push → ETL kickoff
- Upstream API publishes dataset update → catalog refresh pipeline

#### ⚠️ Use Polling (Sensor) only when
- The source cannot emit events / no webhooks.
- Security policy prohibits inbound connectivity.
- Event frequency is low and the polling budget is acceptable.

**Hard requirements**
- Idempotent handlers (dedupe by watermark + stable IDs).
- Change detection (ETag, checksum, “updated_at” cursor, or monotonically increasing revision).
- Explicit polling budget + rate limits + jitter (avoid thundering herd).
- “Catch-up mode” behavior documented (what happens after downtime).

**Examples**
- Legacy REST API without webhooks → nightly ingest with cursor
- Partner system with limited connectivity → scheduled check + diff

#### ✅ Use Object-Event triggers when
- You operate inside cloud-native ecosystems (storage, queues, topics, event buses).
- Object lifecycle events are authoritative (finalize/commit semantics).
- You need broker-managed delivery and scalable fan-out.

**Required controls**
- IAM-scoped subscriptions; least privilege.
- Dedupe (at-least-once is common even on event buses).
- Backpressure handling (queue depth limits, concurrency controls).
- DLQ + replay tooling (re-drive events safely).

**Examples**
- Object finalized in bucket → STAC ingest + validation
- Queue/topic event → downstream fusion pipeline

#### ✅ Use Deployment / Release triggers when
- Automation must react to deploy state (success/failure/rollback).
- Observability & provenance must link to CI artifacts.
- Downstream pipelines depend on release readiness.

**Required controls**
- Link to artifact identifiers (build ID, image digest, commit SHA).
- Gate “dangerous automation” behind policy (freeze, rollback).
- Record provenance of the release-triggered activity (what changed, who approved).

**Examples**
- Deployment success → smoke tests
- Rollback event → data pipeline freeze + alert

### Reliability & safety requirements (apply to ALL triggers)
All triggers MUST implement:
- Idempotency keys + dedupe window
- Dead-letter routing (DLQ/path) for poison events
- Structured retries with backoff + caps (no infinite retry loops)
- Kill-switch support (global + per-source)
- Replay-safe execution (deterministic reruns; no hidden side effects)

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  S[Trigger Signal] --> H[Idempotent Handler]
  H --> X[ETL / Task Execution]
  X --> C[STAC / DCAT Update]
  X --> P[PROV Lineage Emission]
  X --> T[Telemetry & Governance Ledger]

  C --> G[Graph Update (derived)]
  G --> A[APIs]
  A --> U[UI / Story Nodes / Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Source as Source System
  participant Gateway as Trigger Gateway
  participant Handler as Idempotent Handler
  participant Runner as Pipeline Runner
  participant Catalog as STAC/DCAT Writer
  participant Prov as PROV Emitter
  participant Tel as Telemetry/Ledger

  Source->>Gateway: Event (signed / authenticated)
  Gateway->>Handler: Normalized trigger envelope
  Handler->>Runner: Dispatch run (idempotent)
  Runner->>Catalog: Write/Update catalogs
  Runner->>Prov: Emit prov:Activity + links
  Runner->>Tel: Emit telemetry + audit entries
  Handler-->>Gateway: ACK (or NACK + retry policy)
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Webhook payload | JSON (source-defined) | Git/SaaS/API | Signature + schema + allowlist |
| Polling diff | JSON/CSV/etc | Legacy API | Schema + watermark correctness |
| Object-event envelope | JSON (provider-defined) | Bucket/topic/event bus | Schema + IAM principal |
| Deployment event | JSON (CI/CD-defined) | CI/CD platform | Artifact ID + source auth |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Trigger handling log | Structured log | (platform-specific) | Telemetry schema (as applicable) |
| DLQ item | JSON | (queue/bucket) | DLQ schema (recommended) |
| Run record | JSON | `mcp/runs/` (or equivalent) | Run manifest schema (recommended) |
| Catalog updates | STAC/DCAT | `data/stac/` + `docs/data/` | STAC/DCAT profiles |
| Provenance record | PROV (JSON/RDF) | (provenance store) | PROV profile |

### Sensitivity & redaction
- Minimize payload retention: store **references** (object URI, dataset ID) over full payloads where possible.
- Do not log sensitive coordinates or restricted identifiers in plaintext.
- Apply sovereignty rules to any trigger that touches restricted/Indigenous data domains.

### Quality signals
Track at minimum:
- Trigger ingestion latency (p50/p95)
- Duplicate rate (dedupe hits)
- Retry rate + exhaustion rate
- DLQ depth and age
- Polling watermark drift (time since last successful checkpoint)
- Replay success rate (and time-to-recover)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: (TBD — depends on triggered pipeline)
- Items involved: (TBD)
- Extension(s): (TBD; use only governed extensions)

### DCAT
- Dataset identifiers: (TBD)
- License mapping: follow governed source contracts
- Contact / publisher mapping: (TBD)

### PROV-O
Trigger-driven runs should produce, at minimum:
- A `prov:Activity` representing the triggered run
- `prov:used` links to upstream inputs (datasets, objects, configs)
- `prov:wasGeneratedBy` links for derived outputs (catalog items, artifacts)
- Activity / Agent identities: trace back to CI identity / service identity

### Versioning
- Prefer explicit version identifiers in:
  - run manifests (run_id, commit_sha, config version)
  - derived artifacts (checksums, inputs list)
  - catalog entries (consistent item IDs + version links where applicable)

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Trigger Gateway | Receives/normalizes events | HTTP endpoint / subscription |
| Idempotent Handler | Dedupe + dispatch + policy checks | Trigger envelope → run dispatch |
| Work Queue / Dispatcher | Backpressure + concurrency control | queue/topic |
| Pipeline Runner | Executes ETL/tasks | run config + inputs |
| Catalog Writer | Updates STAC/DCAT | JSON outputs + validation |
| PROV Emitter | Emits lineage | PROV artifacts |
| Telemetry/Ledger | Observability + audit | metrics/logs/events |
| DLQ | Poison event routing | durable store |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Trigger envelope (recommended) | `schemas/` (TBD) | Semver + changelog |
| Telemetry schema | `schemas/telemetry/` | Semver + contract tests |
| Provenance profile | PROV profile | Governed versioning |
| Catalog profiles | STAC/DCAT profiles | Governed versioning |

### Reference implementations (configuration stubs)
> These are examples. Adjust keys and file paths to match your runtime (Airflow, Argo, Prefect, custom).

**Webhook (Push)**
~~~yaml
trigger:
  type: webhook
  auth:
    mode: hmac-sha256
    secret_ref: "secret://kfm/webhook/hmac"
  retries:
    policy: exponential
    max_attempts: 12
  idempotency:
    key_from: ["event_id", "commit_sha"]
    dedupe_window: "72h"
  handler:
    module: "src/.../handlers/webhook_ingest.py"
~~~

**Polling (Sensor)**
~~~yaml
trigger:
  type: polling
  interval: "15m"
  jitter: "30s"
  budget:
    max_requests_per_hour: 240
  change_detection:
    mode: etag
  watermark:
    mode: updated_at_cursor
    store: "state://kfm/polling/<source>"
  handler:
    module: "src/.../handlers/poll_ingest.py"
~~~

**Object-Event**
~~~yaml
trigger:
  type: object_event
  provider: "cloud-storage"
  event: "object.finalized"
  subscription:
    iam_role_ref: "iam://kfm/object-events/reader"
  idempotency:
    key_from: ["bucket", "object_key", "generation"]
    dedupe_window: "168h"
  dlq:
    enabled: true
  handler:
    module: "src/.../handlers/object_ingest.py"
~~~

**Deployment Event**
~~~yaml
trigger:
  type: deployment
  provider: "cicd"
  event: "release.success"
  artifact_linkage:
    fields: ["build_id", "image_digest", "commit_sha"]
  policy:
    allow_automation: true
    require_approval_for_freeze: true
  handler:
    module: "src/.../handlers/deploy_hook.py"
~~~

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Trigger-driven pipelines must ensure **catalogs and provenance** are updated so that:
  - the UI can discover new/updated assets (via STAC/DCAT)
  - Focus Mode can reference evidence with traceable lineage (via PROV)
- Trigger systems should expose *focusable entities* only through APIs (no direct graph access).

### Provenance-linked narrative rule
- Any downstream narrative that depends on triggered outputs must trace claims to dataset/record/asset IDs.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [-98.0000, 38.0000]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Trigger envelope validation (if implemented)
- [ ] Idempotency tests (duplicate delivery simulation)
- [ ] DLQ + replay tests (poison event handling)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) Run doc lint / markdown protocol checks
# <cmd>

# 2) Validate STAC/DCAT/PROV outputs (if your change affects them)
# <cmd>

# 3) Run trigger handler unit/integration tests
# <cmd>
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| trigger_lag_ms | handler | `docs/telemetry/` + `schemas/telemetry/` |
| dedupe_hits_total | handler | telemetry backend |
| retries_total | handler/runner | telemetry backend |
| dlq_depth | queue/bucket | telemetry backend |
| polling_watermark_age | polling | telemetry backend |

## ⚖ FAIR+CARE & Governance

### Review gates
- Reliability Council approval for:
  - changes to default retry policies, dedupe windows, DLQ routing
  - changes that affect replay behavior or kill-switch semantics
- FAIR+CARE oversight for:
  - automation that touches restricted/sensitive domains
  - changes that affect auditability or redaction rules

### CARE / sovereignty considerations
- Triggers are governed entry points into the data lifecycle.
- Indigenous, restricted, or sensitive datasets require pre-authorization and auditable controls.
- Ensure logs and DLQs do not leak restricted identifiers.

### AI usage constraints
- Ensure this doc’s AI permissions/prohibitions remain aligned with governance expectations.
- Do not use automated systems to infer sensitive locations from trigger metadata.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v11.2.7 | 2025-12-17 | Template alignment + clarified decision flow + cleaned diagrams/config examples | TBD |
| v11.2.6 | 2025-12-17 | Canonical trigger decision guide | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`