---
title: "🔔 KFM — Change Detection with Minimal Polling (Webhooks, SSE, ETags, Idempotency)"
path: "docs/patterns/change-detection/README.md"
version: "v12.0.0"
last_updated: "2025-12-20"
status: "active"
doc_kind: "Pattern"
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
care_label: "Public · Low-Risk"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:pattern:change-detection:v12.0.0"
semantic_document_id: "kfm-pattern-change-detection-v12.0.0"
event_source_id: "ledger:kfm:doc:pattern:change-detection:v12.0.0"
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

# 🔔 KFM — Change Detection with Minimal Polling (Webhooks, SSE, ETags, Idempotency)

## 📘 Overview

### Purpose
Standardize **low-noise, governance-friendly change detection** across KFM sources while **minimizing polling**:
- Prefer **push** (Webhooks / SSE / object-store events) when available.
- If only pull is possible, use **checkpointed conditional requests** (ETag / If-Modified-Since) and/or **manifest diff** before heavy fetch.
- Route all detections through a single **idempotent handler contract** so duplicates/retries are harmless.
- Ensure **deterministic rollback** using delta/manifest units, and **traceable provenance** (STAC/DCAT/PROV).

### Scope

| In Scope | Out of Scope |
|---|---|
| Detector patterns: Webhooks, SSE, object-store events, ETag/IMS polling, manifest diff | UI/browser-side polling loops |
| Idempotency keys + dedupe ledger/WAL + replay log | Frontend accessing Neo4j directly |
| Bounded retries + backoff + jitter + DLQ | “Freshness” claims without `detected_at` + provenance refs |
| Minimal provenance + catalog updates + reversible deltas | Provider-specific integration tutorials (kept in source-specific docs) |

### Audience
- Primary: Data Engineering, Data Ops, Reliability, Pipeline Maintainers
- Secondary: Domain Stewards, Governance reviewers, Security reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc:
  - **Detector**: decides “should we attempt processing?”
  - **Handler**: performs effects once (stage, validate, catalog, lineage, promote)
  - **Idempotency key**: stable identity for “this exact object version”
  - **Replay log / WAL**: append-only record enabling deterministic replays/backfills
  - **Manifest diff**: order-independent listing comparison with stable hashing
  - **ETag / IMS**: conditional request signals (`If-None-Match`, `If-Modified-Since`)

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This pattern | `docs/patterns/change-detection/README.md` | data-ops@kfm.local | Canonical index + minimal polling guidance |
| Idempotent handler pattern | `docs/patterns/change-detection/idempotent-handler/README.md` | platform@kfm.local | Recommended; avoids detector/handler coupling *(not confirmed in repo)* |
| Governance standards | `docs/standards/` | data-ops@kfm.local | See governance + security + lineage *(not confirmed in repo)* |
| Change-detection telemetry | `docs/telemetry/README.md#change-detection` | platform@kfm.local | Metrics + SLOs *(not confirmed in repo)* |
| SBOM reference | `docs/standards/sbom/kfm_components_sbom.json` | platform@kfm.local | SBOM for governed components *(not confirmed in repo)* |
| Change detection manifest ref | `data/archive/manifests/change-detection-pattern.manifest.json` | data-ops@kfm.local | Pattern manifest / integrity *(not confirmed in repo)* |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Detector/handler separation and idempotency rules are unambiguous
- [ ] Message + manifest schemas are stable and testable
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `docs/patterns/change-detection/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Detector implementations | `src/pipelines/watchers/` | Webhook/SSE handlers, pollers, manifest checkers *(not confirmed in repo)* |
| Idempotency ledger | `data/work/idempotency/` or KV | Idempotency keys + statuses *(storage backend is implementation-specific)* |
| Replay logs | `data/prov/replay/` or object store | Append-only change replay logs *(not confirmed in repo)* |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` | STAC + DCAT artifacts |
| Provenance bundles | `data/prov/` | PROV JSON-LD bundles |
| Schemas | `schemas/telemetry/` | Telemetry schemas for change-detection *(not confirmed in repo)* |
| Tests | `tests/` | Determinism + idempotency + rollback tests *(not confirmed in repo)* |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 patterns/
    └── 📁 change-detection/
        ├── 📄 README.md
        └── 📁 idempotent-handler/
            └── 📄 README.md
~~~

## 🧭 Context

### Background
Change detection is a **reliability feature** and a **governance feature**. High-noise detectors create:
- unnecessary promotions,
- confusing provenance,
- reviewer fatigue,
- “false freshness” in Story Nodes.

KFM prefers detection that is:
- **cheap to evaluate**,
- **stable under retries**,
- **explainable in lineage**.

### Assumptions
- Upstream delivery is typically **at-least-once** (duplicates will happen).
- ETags are sometimes **weak** (not a true content hash).
- Listings can drift without canonicalization (pagination/order changes).
- Deterministic ETL + stable IDs are non-negotiable.

### Constraints / invariants
- **Canonical pipeline order is preserved**: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- **API boundary**: UI never reads Neo4j directly.
- **Invariant: detector ≠ handler**
  - Detectors only answer: **“Should I attempt processing?”**
  - The handler answers: **“Have I already produced effects for this exact object identity?”**
- **Rollback must be deterministic**
  - Rollback references a **delta manifest** or a **prior manifest** as the single source of truth.
  - Never define rollback as “delete everything from the last hour.”

### Detector selection (what to use when)

| Detector | Best for | Noise profile | What you trust | What you must not assume |
|---|---|---|---|---|
| Object-store events (S3/GCS/Azure) | Buckets you control | Very low (push) | event_id + object versioning | Exactly-once delivery |
| Webhooks / SSE | Providers offering push | Low (push) | signature + event_id/cursor | Ordering or no duplicates |
| HTTP ETag / If-None-Match | Public HTTP(S) | Low–Medium | server token + cache semantics | ETag is a strong content hash |
| Manifest/listing diff | Batch drops / folder releases | Medium | canonical listing + your hashing | Listing order is stable without canonicalization |

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we standardize a single “change-event” JSON schema under `schemas/`? | platform@kfm.local | TBD |
| Where is the canonical replay log stored for each domain? | data-ops@kfm.local | TBD |
| Do we expose a public “change feed” API for UI badges? | platform@kfm.local | TBD |

### Future extensions
- Add a governed **Change Feed API** (with redaction rules) for UI “Updated on…” badges.
- Add source-specific adapters that map provider events into a single stable event schema.

## 🗺️ Diagrams

### System / dataflow diagram (canonical KFM flow + change detection)
~~~mermaid
flowchart LR
  subgraph Detect
    U[Upstream Source] --> D[Detector: Event | Webhook | SSE | ETag/IMS | Manifest Diff]
  end

  D --> G[Idempotency Gate: Ledger/WAL]
  G -->|new| H[Handler: Fetch + Digest + Validate]
  G -->|already processed| N[No-op: Safe Exit]

  H --> S[Stage + Normalize (content-addressed)]
  S --> C[STAC/DCAT/PROV Updates]
  C --> X[Neo4j Graph Load]
  X --> A[API Layer]
  A --> UI[React/Map UI]
  UI --> SN[Story Nodes]
  SN --> FM[Focus Mode]
~~~

### Optional: sequence diagram (provider → watcher → catalogs)
~~~mermaid
sequenceDiagram
  participant Provider
  participant Watcher as Watcher/Detector
  participant Queue as Durable Queue
  participant Handler as Idempotent Handler
  participant Catalog as STAC/DCAT/PROV

  Provider-->>Watcher: Event / Webhook / SSE tick
  Watcher->>Watcher: Verify + normalize + checkpoint
  Watcher->>Queue: Enqueue change candidate (idempotency_key)
  Queue-->>Handler: Deliver (at-least-once)
  Handler->>Handler: Dedupe + fetch + strong digest
  Handler->>Catalog: Upsert STAC/DCAT + emit PROV (+ delta manifest)
  Catalog-->>Handler: Commit result (refs)
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Webhook payload | JSON | Provider | Signature verify + schema validate |
| SSE message | JSON/text | Provider | Schema validate |
| Object-store notification | JSON | Cloud provider | Signature verify (if supported) |
| HTTP resource / manifest | JSON/CSV/HTML | Provider | Conditional GET + schema validate |
| Checkpoint state | JSON/KV | KFM store | Schema validate; monotonic cursor |
| Secrets | K/V | Secret manager | Rotation + least privilege |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Change candidate messages | JSON | Queue topic `kfm-changes` *(example)* | Stable event schema *(recommended)* |
| Replay log (append-only) | JSONL / Parquet | `data/prov/replay/...` *(example)* | Run-bound schema |
| Delta manifest (apply/revert) | JSON | `data/work/deltas/...` *(example)* | Manifest schema + checksum |
| STAC updates | JSON | `data/stac/...` | STAC + KFM profiles |
| DCAT updates | JSON-LD/Turtle | `data/catalog/dcat/...` | DCAT profile |
| PROV bundles | JSON-LD | `data/prov/...` | PROV-O profile |
| Telemetry | JSON | `docs/telemetry/...` or run store | Telemetry schema *(recommended)* |

### Sensitivity & redaction
- Do not leak sensitive locations or restricted identifiers via verbose logs, public delta manifests, or UI tooltips.
- If a dataset is restricted (including Indigenous data protections):
  - keep deltas in restricted storage tiers,
  - expose only aggregated/non-sensitive summaries publicly,
  - require documented approvals for promotions.

### Quality signals
- Digest coverage: percent of promoted artifacts with `sha256`.
- Geometry validity and schema validity pass rates.
- Request efficiency: 304:200 ratio and bytes saved.
- Dedupe hit rate and replay success rate.

### Change event payload (recommended; detector output)
~~~json
{
  "change_event_id": "evt_2025-12-20T04:02:11Z_abc123",
  "detector": "webhook|sse|event|etag|manifest",
  "source_uri": "https://example.org/data/file.tif",
  "detected_at": "2025-12-20T04:02:11Z",
  "received_at": "2025-12-20T04:02:13Z",
  "version_hint": "etag-or-object-version-or-cursor",
  "notes": "Optional, non-sensitive"
}
~~~

### Work queue message (recommended; handler input)
> The handler should compute a **strong digest** (sha256) as early as possible and convert `version_hint` into a durable `version` used by idempotency.

~~~json
{
  "source": "usgs.streamflow",
  "type": "upsert",
  "entity_id": "site:06892390:ts:00060",
  "detector": "webhook",
  "cursor": "2025-12-20T04:00:00Z",
  "version_hint": "\"9b-1f4a\"",
  "version": "sha256:<computed-after-fetch>",
  "idempotency_key": "usgs.streamflow|site:06892390:ts:00060|sha256:<...>",
  "links": {
    "item_href": "data://stac/items/usgs/06892390/00060/<...>"
  },
  "observed_at": "2025-12-20T04:02:11Z"
}
~~~

### Checkpoint schema (KV or small JSON)
~~~json
{
  "source": "epa.aqs",
  "since": "2025-12-18T00:00:00Z",
  "last_etag": "\"9b-1f4a\"",
  "last_modified": "Sat, 20 Dec 2025 03:58:00 GMT",
  "page_token": null,
  "poll_interval_s": 300
}
~~~

### Manifest record (order-independent; hash-stable)
~~~json
{
  "manifest_id": "man_2025-12-20_kfm-aq-pm25",
  "generated_at": "2025-12-20T04:10:00Z",
  "listing_basis": "bucket-listing|api-list|git-tree",
  "canonical_sort": "uri_asc",
  "entries": [
    {
      "uri": "s3://bucket/key1",
      "version": "v123",
      "checksum_sha256": "<optional-if-known>",
      "size_bytes": 111
    }
  ],
  "manifest_checksum_sha256": "sha256:<sha256-of-canonical-json>"
}
~~~

### Idempotency ledger record (recommended statuses)
~~~json
{
  "idempotency_key": "source|logical_id|sha256:...",
  "status": "pending|finalized|failed|rolled_back",
  "first_seen_at": "2025-12-20T04:02:13Z",
  "finalized_at": "2025-12-20T04:05:11Z",
  "delta_manifest_ref": "data://work/deltas/<run-id>/<delta>.json",
  "prov_ref": "data://prov/<run-id>/prov.jsonld"
}
~~~

## 🌐 STAC, DCAT & PROV Alignment

### STAC
Attach change detection + idempotency context in `properties`, and include provenance assets:
- `properties.kfm:change_detection.detector`
- `properties.kfm:change_detection.detected_at`
- `properties.kfm:change_detection.idempotency_key`
- `properties.checksum:sha256`
- `assets.provenance` (PROV JSON-LD)
- `assets.openlineage` *(if used; not required)*
- `links` to delta manifest (apply/revert unit)

### DCAT
For catalog-level datasets:
- Each promoted artifact is a `dcat:Distribution`.
- Each distribution includes checksum and media type.
- Distributions are versioned and linked to provenance artifacts.

### PROV-O
At minimum, each successful run should express:
- **Entity**: upstream object (as observed)
- **Entity**: staged artifact (content-addressed by checksum)
- **Activity**: handler run (deterministic, versioned)
- **Agent**: pipeline identity (service account / runner)

~~~json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",
  "entity": {
    "urn:kfm:entity:source:obj": {
      "prov:label": "source_uri",
      "kfm:uri": "https://example.org/data/file.tif"
    },
    "urn:kfm:entity:artifact:sha256:<...>": {
      "prov:label": "staged_artifact",
      "kfm:checksum_sha256": "<...>"
    }
  },
  "activity": {
    "urn:kfm:activity:change-detect:run:<...>": {
      "prov:label": "change-detection-handler",
      "kfm:detector": "etag"
    }
  },
  "wasGeneratedBy": {
    "_:wgb1": {
      "prov:entity": "urn:kfm:entity:artifact:sha256:<...>",
      "prov:activity": "urn:kfm:activity:change-detect:run:<...>"
    }
  }
}
~~~

### Versioning
- Prefer linking to predecessor/successor STAC Items (and mirror in graph relationships) when publishing new versions.
- Treat “reprocessing the same bytes” as a **no-op** at the handler level.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Detector | Find candidate changes cheaply | Webhook/SSE/event/poll |
| Idempotency gate (ledger/WAL) | Decide “already processed?” | `idempotency_key` lookup |
| Fetch + strong digest | Compute sha256 early | HTTP/object fetch |
| Deterministic validation | Schema/geo/QA/security checks | Validators |
| Stage + normalize | Content-addressed outputs | `data/work/` → `data/processed/` |
| Catalog writer | Update STAC/DCAT | Catalog contracts + validators |
| Provenance emitter | Emit PROV bundles | `data/prov/` |
| Promotion | Move into governed tier | Release/publish step |
| Rollback | Apply one reversible action | Delta manifest apply/revert |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Change event schema | `schemas/...` *(recommended)* | Semver + contract tests |
| Telemetry schemas | `schemas/telemetry/...` *(recommended)* | Semver + changelog |
| Catalog profiles | STAC/DCAT/PROV profiles | Validator-enforced |

### Reference design A — Webhook/SSE-first watcher (minimal polling)

**Use when** the source offers Webhooks or SSE, with optional polling fallback.

**Key points**
- Verify signatures (fail-closed).
- Normalize to a stable message schema.
- Dedupe at enqueue time using idempotency keys.
- Always log to replay (append-only).

~~~mermaid
flowchart LR
  W[Webhook/SSE Event] --> F[Watcher Handler]
  F --> V[Signature Verify + Parse]
  V --> D[Dedupe Store / Ledger]
  D -->|new| Q[Durable Queue]
  D -->|seen| X[Drop / No-op]
  Q --> H[Idempotent Handler]
  F -.-> P[Fallback Poll (ETag/IMS)]:::dim

classDef dim opacity:0.6;
~~~

**Idempotency key guidance**
- Recommended (strong):
  - `(source_uri, checksum_sha256)` once bytes are fetched, OR
  - `(source_uri, object_version_id)` when the store guarantees version immutability.
- Avoid (weak):
  - `Last-Modified` alone
  - weak ETags (`W/`)
  - timestamps as identities

**Retries & backoff**
- Transient errors: exponential backoff + full jitter; cap attempts; then DLQ.
- Respect `Retry-After` on 429/503; degrade to checkpointed polling until healthy.

### Reference design B — Conditional GET watcher (ETag/IMS + manifest diff)

**Use when** only polling is available or for backfills.

~~~mermaid
flowchart LR
  S[Scheduled Task] --> L[Load Checkpoint]
  L --> R[HEAD/GET with If-None-Match / If-Modified-Since]
  R -->|304| H[No Change -> Save heartbeat + adapt interval]
  R -->|200| M[Fetch Manifest/Index]
  M --> C[Canonicalize + Diff + Checksums]
  C --> Q[Enqueue Changes]
  Q --> U[Idempotent Handler -> Upsert STAC/DCAT + PROV]
  U --> P[Persist Checkpoint + Replay Log]
~~~

**Conditional strategy**
- Prefer `If-None-Match: <last_etag>`, fallback to `If-Modified-Since: <last_modified>`.
- If neither works, compare **manifest checksums**; if absent, keep a local checksum map (`uri → sha256`).

**Adaptive polling**
- Increase interval on repeated 304s (e.g., +25% up to max).
- Decrease interval after changes within SLO bounds.
- Always add jitter to avoid thundering herds.

### Dedupe, replay, ordering
- Dedupe at enqueue time and at consume time; duplicates must be safe no-ops.
- Replay uses an append-only log ordered by `observed_at`; keep bounded windows (e.g., last 90 days) unless a governed backfill is approved.
- Do not assume provider ordering; rely on `version` (strong digest) or monotonic cursors.

### Deterministic rollback semantics
Rollback should reference:
- the delta manifest that was applied (revert unit), or
- a prior manifest (desired state).

Never rollback based on time windows alone.

### Drop-in KFM artifacts (pseudo-impl; keep detector/handler separate)

#### 1) Serverless watcher skeleton (TypeScript, pseudo-impl)
~~~ts
// src/pipelines/watchers/serverless_watcher.ts
import { verifySignature, enqueue, ledgerSeen, replayAppend } from "./lib";

export async function handler(req: Request): Promise<Response> {
  const raw = await req.text();
  if (!verifySignature(req.headers, raw)) return new Response("unauthorized", { status: 401 });

  const candidate = normalize(JSON.parse(raw)); // { source_uri, detector, version_hint, ... }
  const idemHint = `${candidate.source}|${candidate.source_uri}|${candidate.version_hint ?? "none"}`;

  // Ledger check here is only a *hint*; handler must still enforce strong idempotency after digest.
  const seen = await ledgerSeen(idemHint);
  if (seen) return new Response("ok", { status: 200 });

  await enqueue("kfm-changes", { ...candidate, idempotency_key: idemHint });
  await replayAppend(candidate); // append-only
  return new Response("accepted", { status: 202 });
}
~~~

#### 2) Orchestrator task watcher (Python, pseudo-impl)
~~~python
# src/pipelines/watchers/orchestrator_task.py
import time
from httpx import Client

def conditional_fetch(client: Client, url: str, cp: dict):
    headers = {}
    if cp.get("last_etag"):
        headers["If-None-Match"] = cp["last_etag"]
    if cp.get("last_modified"):
        headers["If-Modified-Since"] = cp["last_modified"]
    return client.get(url, headers=headers, timeout=30)

def run_task(cp_store, queue, replay_log, manifest_url):
    cp = cp_store.load()

    with Client() as http:
        r = conditional_fetch(http, manifest_url, cp)

        if r.status_code == 304:
            cp_store.save({**cp, "poll_interval_s": min(int(cp["poll_interval_s"] * 1.25), 3600)})
            return

        r.raise_for_status()

        etag = r.headers.get("ETag")
        lm = r.headers.get("Last-Modified")
        manifest = r.json()

        detected_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        for entry in manifest.get("entries", []):
            msg = {
                "detector": "etag",
                "source_uri": entry["uri"],
                "version_hint": entry.get("version") or etag or lm,
                "detected_at": detected_at
            }
            queue.send(msg)       # downstream handler computes sha256 + final idempotency_key
            replay_log.append(msg)

        cp_store.save({**cp, "last_etag": etag, "last_modified": lm})
~~~

## 🧠 Story Node & Focus Mode Integration

### Goal
Story Nodes and Focus Mode must be able to answer:
- What changed?
- When did it change?
- Why should I trust this update?
- Can I roll back?

### Required UI-facing contract
Do **not** push graph internals to the frontend. Instead:
- publish change outcomes through **API endpoints** backed by catalog/provenance artifacts, and
- make every “freshness” claim traceable to:
  - a run timestamp,
  - an input identifier,
  - a delta/manifest reference.

### Recommended fields to expose via API responses
- `change_event_id` (detector-provided or KFM-generated)
- `detected_at`
- `source_uri`
- `object_identity` (object version and/or sha256)
- `delta_manifest_ref` (apply/revert unit)
- `qa_summary` (high-level, non-sensitive)
- `prov_ref` (PROV link)
- `openlineage_ref` *(optional)*

### Story Node guidance
- If a Story Node references a dataset layer affected by a delta:
  - Show **“Updated on <date>”** with a link to provenance.
  - Show a QA disclaimer when anomalies or incomplete coverage are flagged.
  - For sensitive topics/places: apply masking/aggregation rules; avoid precise coordinates unless permitted.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV + message schemas where applicable)
- [ ] Determinism tests (stable ordering + stable hashes)
- [ ] Idempotency tests (duplicate event delivery → no duplicate effects)
- [ ] Crash-safety tests (fail between stage and commit → safe retry)
- [ ] Rollback tests (apply + revert via delta manifest)
- [ ] Security checks (signature verification, payload schema, secret handling)
- [ ] Sovereignty/sensitivity checks (masking + access constraints)

### Minimum CI expectations (implementation-level)
1. Deterministic tests
   - fixed seeds if randomness exists,
   - canonicalized ordering for manifests,
   - reproducible hashes.

2. Idempotency tests
   - same event delivered twice → same final state,
   - retry after partial failure → converges to one outcome,
   - pagination drift → reconciliation prevents missing/duplicate items.

3. Policy gates (if used)
   - required catalog fields present,
   - checksums attached,
   - provenance emitted or explicitly waived (waivers require review).

4. Drift guards
   - golden-record tests for high-risk datasets,
   - schema invariants enforced.

### CI artifacts to persist (recommended)
Prefer storing run artifacts under MCP runs (repo placement rule):
- `mcp/runs/change-detect/<run-id>/detector.json`
- `mcp/runs/change-detect/<run-id>/manifest.json`
- `mcp/runs/change-detect/<run-id>/delta_manifest.json`
- `mcp/runs/change-detect/<run-id>/provenance.prov.jsonld`
- `mcp/runs/change-detect/<run-id>/summary.md`

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Freshness lag (p50/p95) | handler | `docs/telemetry/` + run store |
| 304:200 ratio | watcher | `docs/telemetry/` + run store |
| Dedupe hit rate | ledger | `docs/telemetry/` + run store |
| DLQ depth | queue | `docs/telemetry/` + run store |
| Replay success rate | replay tool | `docs/telemetry/` + run store |

## ⚖ FAIR+CARE & Governance

### Review gates
- Data Ops & FAIR+CARE council review: required for new sources, new public endpoints, new sensitive layers.
- Security council review: required for webhook secret handling patterns and any new inbound surface.

### CARE / sovereignty considerations
- Do not publish sensitive deltas/manifests or raw identifiers when restrictions apply.
- For datasets with Indigenous data protections:
  - enforce access constraints,
  - limit public exposure to aggregated summaries,
  - require documented approvals for promotions.

### AI usage constraints
- AI may summarize/structure this doc, but must not generate policy or infer sensitive locations (see front-matter).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v11.2.6 | 2025-12-17 | Prior index-style guidance (detector/handler separation, rollback semantics) | TBD |
| v12.0.0 | 2025-12-20 | Merged “minimal polling” reference designs with low-noise detector/handler/rollback + Story Node contract guidance | TBD |

---

Back to 📚 **Docs Index** → [docs/README.md](../../README.md)  
📂 **Patterns** → [docs/patterns/README.md](../README.md) *(not confirmed in repo)*  
🏗️ **Architecture** → [docs/architecture/README.md](../../architecture/README.md)  
⚖️ **Governance** → [docs/standards/README.md](../../standards/README.md)
