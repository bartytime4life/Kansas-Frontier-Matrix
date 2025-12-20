---
title: "🧭 KFM — Low‑Noise Change Detection & Idempotent Handler Pattern (ETag · Events · Manifest Diff)"
path: "docs/patterns/change-detection/idempotent-handler/README.md"
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

doc_uuid: "urn:kfm:doc:patterns:change-detection:idempotent-handler:v12.0.0"
semantic_document_id: "kfm-pattern-change-detection-idempotent-handler-v12.0.0"
event_source_id: "ledger:kfm:doc:patterns:change-detection:idempotent-handler:v12.0.0"
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

# 🧭 KFM — Low‑Noise Change Detection & Idempotent Handler Pattern (ETag · Events · Manifest Diff)

## 📘 Overview

### Purpose
Provide a **low-noise, deterministic** pattern for detecting upstream change and applying **exactly-once effects** (promotion + catalog updates) under **at-least-once triggers** (polling/events/listing diffs).

### Scope

| In Scope | Out of Scope |
|---|---|
| Detector patterns: ETag/IMS, object-store events, webhooks/SSE, manifest diff | UI-side polling or browser-based change detection |
| Single idempotent handler contract behind all detectors | Frontend access to Neo4j (all UI flows through APIs) |
| Strong digests (sha256) and deterministic validation gates | Replacing KFM orchestration / queue systems |
| Minimal provenance emission (PROV; optional OpenLineage) | “Freshness” claims without timestamps + provenance refs |
| Deterministic rollback (delta/manifest-based) | Bulk destructive rollback based on time windows |

### Audience
- Primary: ETL / Data Engineering, Reliability, Catalog & Provenance maintainers
- Secondary: Governance reviewers, Security reviewers, API maintainers

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc:
  - **Detector**: answers “should we attempt processing?”
  - **Handler**: performs effects once (validate → stage → catalog → provenance → promote)
  - **Idempotency key**: stable identity for “this exact object version”
  - **WAL / ledger**: durable record of idempotency + step state
  - **Replay log**: append-only event history for deterministic replays/backfills
  - **Manifest diff**: order-independent listing comparison with stable hashing
  - **ETag / IMS**: conditional request controls (`If-None-Match`, `If-Modified-Since`)

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This doc | `docs/patterns/change-detection/idempotent-handler/README.md` | data-ops@kfm.local | Canonical pattern |
| Change detection index | `docs/patterns/change-detection/README.md` | data-ops@kfm.local | Detector selection + minimal polling |
| Schemas | `schemas/` | platform@kfm.local | Event/telemetry schemas *(recommended)* |
| Watchers | `src/pipelines/watchers/` | platform@kfm.local | Webhook/SSE/poller implementations *(not confirmed in repo)* |
| Replay/Run artifacts | `mcp/runs/` | data-ops@kfm.local | Persist run artifacts + summaries |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (Universal template key set)
- [ ] Detector/handler separation is explicit and testable
- [ ] Idempotency identity rules are unambiguous (strong digest required)
- [ ] Rollback semantics are deterministic (delta/manifest apply/revert)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

### Governance & Ops metadata (legacy v11 fields, preserved here)
| Field | Value |
|---|---|
| Prior version | v11.2.6 (last_updated 2025-12-16) |
| Release stage | Stable / Governed |
| Lifecycle | Long‑Term Support (LTS) |
| Review cycle | Quarterly · Reliability & FAIR+CARE Council |
| Content stability | stable |
| Intent | `kfm-change-detection-idempotent-handler` |
| Diagram profiles | mermaid-flowchart-v1 |
| Public exposure risk | Low |
| Indigenous rights flag | true |
| Data steward | Reliability & FAIR+CARE Council |

### Release artifacts (legacy v11 pinned references)
> These were in the v11 front-matter. Kept here to avoid inventing a new v12 release layout.

| Artifact | v11 reference |
|---|---|
| signature_ref | `releases/v11.2.6/signature.sig` |
| attestation_ref | `releases/v11.2.6/slsa-attestation.json` |
| sbom_ref | `releases/v11.2.6/sbom.spdx.json` |
| manifest_ref | `releases/v11.2.6/manifest.zip` |
| telemetry_ref | `releases/v11.2.6/change-detect-telemetry.json` |
| telemetry_schema | `schemas/telemetry/change-detect-v1.json` |
| energy_schema | `schemas/telemetry/energy-v2.json` |
| carbon_schema | `schemas/telemetry/carbon-v2.json` |

### AI policy notes (legacy v11 intent; requires human review)
> v11 included additional AI transform permissions/prohibitions beyond the v12 template defaults.
> Treat these as **non-authoritative** until codified in the repo’s governed AI policy.

- ai_training_inclusion: false
- ai_focusmode_usage: Allowed with restrictions
- extra transforms mentioned in v11: timeline-generation, semantic-highlighting, diagram-extraction, metadata-extraction, layout-normalization, a11y-adaptations, etc.
- extra prohibitions mentioned in v11: content-alteration, speculative-additions, governance-override, narrative-fabrication, unverified-architectural-claims

## 🗂️ Directory Layout

### This document
- `path`: `docs/patterns/change-detection/idempotent-handler/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Docs (patterns) | `docs/patterns/` | Canonical governed patterns |
| Watchers (detectors) | `src/pipelines/watchers/` | Webhooks/SSE/pollers *(not confirmed in repo)* |
| Tools (optional) | `tools/change_detection/` | CLI utilities (manifest diff, WAL tools) *(not confirmed in repo)* |
| Schemas | `schemas/` | Event + telemetry schemas *(recommended)* |
| Tests | `tests/change_detection/` | Determinism/idempotency/rollback tests *(not confirmed in repo)* |
| Run artifacts | `mcp/runs/change-detection/` | Run logs, manifests, provenance bundles |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 patterns/
    └── 📁 change-detection/
        ├── 📄 README.md
        └── 📁 idempotent-handler/
            └── 📄 README.md

📁 schemas/
├── 📁 telemetry/
│   └── 📄 change-detect-v1.json
└── 📁 events/
    └── 📄 object-change-event-v1.schema.json

📁 tools/
└── 📁 change_detection/
    ├── 📄 handler.py
    ├── 📄 manifest_diff.py
    ├── 📄 etag_normalize.py
    ├── 📄 wal_store.py
    └── 📄 provenance_emit.py

📁 tests/
└── 📁 change_detection/
    ├── 📄 test_idempotent_handler.py
    ├── 📄 test_manifest_diff.py
    └── 📁 fixtures/
        ├── 📄 event_samples.json
        └── 📁 manifests/
            ├── 📄 manifest_a.json
            └── 📄 manifest_b.json

📁 mcp/
└── 📁 runs/
    └── 📁 change-detection/
        └── 📁 <run-id>/
            ├── 📁 wal/
            ├── 📁 provenance/
            ├── 📁 qa/
            └── 📁 logs/
~~~

## 🧭 Context

### Background
Upstream sources (HTTP endpoints, object stores, batch drops) are unreliable in ways that matter:
- events can be duplicated or reordered,
- polling can overlap or miss intermediate changes,
- listings can be paginated or inconsistent.

Therefore detectors MUST be treated as **at-least-once triggers**, and the handler MUST implement **exactly-once effects**.

### Assumptions
- Delivery is at-least-once (duplicates are normal).
- ETags may be weak or opaque; they are not necessarily content hashes.
- Listings are not stable unless canonicalized (sort order + pagination rules).

### Constraints / invariants
- Canonical KFM ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- UI never talks to Neo4j directly; UI uses API contracts only.
- **Invariant: detector ≠ handler**
  - Detector answers “should we attempt?”
  - Handler answers “have we already produced effects for this exact identity?”

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Standard location + schema for change-event envelopes? | platform@kfm.local | TBD |
| Standard WAL backend requirement (KV vs DB) and retention? | data-ops@kfm.local | TBD |
| Standard delta manifest schema for apply/revert? | data-ops@kfm.local | TBD |

### Future extensions
- Add governed schema: `schemas/events/object-change-event-v1.schema.json`.
- Add governed telemetry schema: `schemas/telemetry/change-detect-v2.json` with freshness/efficiency metrics.
- Add a “Change Feed API” (redacted) so UI can show “Updated on…” with provenance links.

## 🗺️ Diagrams

### System / dataflow diagram
> Mermaid compatibility note: avoid `|` inside node labels and avoid `:::class` styling shorthand.

~~~mermaid
flowchart LR
  U["Upstream Objects"] --> D1["Detector: ETag/IMS Poll"]
  U --> D2["Detector: Object-store Events"]
  U --> D3["Detector: Manifest Diff"]

  D1 --> E["Event Envelope"]
  D2 --> E
  D3 --> E

  E --> WAL["WAL / Idempotency Gate"]
  WAL -->|duplicate| NOOP["No-op (safe exit)"]
  WAL -->|new| F["Fetch + Strong Digest (sha256)"]

  F --> V["Deterministic Validation"]
  V -->|fail| RB["Rollback Action (single, deterministic)"]
  V -->|pass| S["Stage + Normalize (content-addressed)"]

  S --> P["Emit PROV (and optional OpenLineage)"]
  P --> PROM["Atomic Promotion"]
  PROM --> CAT["STAC/DCAT Update"]
  PROM --> G["Graph Ingest (ETL)"]
  CAT --> API["APIs"]
  G --> API
  API --> UI["Story Nodes / Focus Mode"]
~~~

### Optional: sequence diagram (idempotency under at-least-once delivery)
~~~mermaid
sequenceDiagram
  participant Detector
  participant Queue
  participant Handler
  participant WAL as WAL/Ledger
  participant Catalog as STAC/DCAT/PROV

  Detector->>Queue: enqueue(change_candidate)
  Queue-->>Handler: deliver(change_candidate) (at-least-once)
  Handler->>WAL: check_or_create(idempotency_key)
  alt already finalized
    Handler-->>Queue: ack (no-op)
  else new
    Handler->>Handler: fetch + sha256 + validate
    alt validation fails
      Handler->>WAL: mark_failed + rollback_applied
      Handler-->>Queue: ack (failed state recorded)
    else validation passes
      Handler->>Catalog: write STAC/DCAT + emit PROV
      Handler->>WAL: finalize (exactly-once effects)
      Handler-->>Queue: ack
    end
  end
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Change candidate | JSON | detector/watchers | Schema validate |
| Source object | bytes | HTTP/object store | Hash + content checks |
| Manifest listing | JSON/CSV | listing endpoint | Canonicalize + stable hash |
| Checkpoint/WAL | KV/DB | KFM state | State machine invariants |
| Policy rules | rego/yaml | KFM governance | Gate on promote |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| WAL entries | JSON | state backend | WAL schema *(recommended)* |
| Staged artifact | bytes | content-addressed storage | digest-named paths |
| Delta manifest | JSON | `data/work/deltas/` *(example)* | apply/revert schema *(recommended)* |
| STAC items/collections | JSON | `data/stac/` | STAC + profile |
| DCAT datasets/distributions | JSON-LD | `data/catalog/dcat/` | DCAT + profile |
| PROV bundle | JSON-LD | `data/prov/` | PROV-O + profile |
| Telemetry | metrics/json | `docs/telemetry/` or run store | telemetry schema *(recommended)* |

### Sensitivity & redaction
- Do not log secrets, raw auth headers, or provider signature materials.
- If a dataset is restricted (including Indigenous data protections), ensure:
  - delta manifests are stored in restricted tiers,
  - API/UI only expose non-sensitive summaries,
  - promotions require review gates.

### Quality signals
- % of promoted artifacts with sha256 attached
- Validation pass/fail counts + reason codes
- Dedupe rate (how often duplicates were safely no-oped)
- Replay success rate (reprocessing converges to same end state)

### Minimal event envelope (detector output)
~~~json
{
  "source": "s3|gcs|azure|http",
  "uri": "s3://bucket/key|https://example/data.tif",
  "version_hint": "object-version-or-etag-or-cursor",
  "event_id": "provider-unique-id",
  "detector": "event|etag|manifest",
  "received_at": "2025-12-16T00:00:00Z",
  "metadata": {
    "content_length": 123456,
    "content_type": "image/tiff"
  }
}
~~~

### Idempotency key rules (MUST)
- Preferred (strong):
  - `(uri, sha256(content_bytes))` once bytes are fetched, OR
  - `(uri, immutable_object_version_id)` when the store guarantees immutability
- Avoid (weak):
  - `Last-Modified` alone
  - weak ETags (`W/`)
  - timestamps as identities

### WAL record (minimum)
Statuses SHOULD support: `pending`, `fetched`, `validated`, `staged`, `promoted`, `finalized`, `failed`, `rolled_back`.

~~~json
{
  "idempotency_key": "sha256:<uri+version_or_digest>",
  "status": "pending|finalized|failed|rolled_back",
  "first_seen_at": "2025-12-20T04:02:13Z",
  "finalized_at": "2025-12-20T04:05:11Z",
  "source_uri": "https://example/data.tif",
  "version_hint": "\"9b-1f4a\"",
  "checksum_sha256": "sha256:<computed>",
  "delta_manifest_ref": "data://work/deltas/<run-id>/<delta>.json",
  "prov_ref": "data://prov/<run-id>/prov.jsonld"
}
~~~

## 🌐 STAC, DCAT & PROV Alignment

### STAC
Handler SHOULD attach:
- `checksum:sha256` (strong digest computed by handler)
- detector metadata (detector type + detected/received timestamps)
- assets for provenance and QA (links, not embedded blobs)

~~~json
{
  "properties": {
    "checksum:sha256": "sha256:<...>",
    "kfm:change_detection:detector": "etag",
    "kfm:change_detection:received_at": "2025-12-20T04:02:13Z"
  },
  "assets": {
    "data": { "href": "s3://kfm-processed/.../sha256/<digest>/asset.tif", "roles": ["data"] },
    "provenance": { "href": "s3://kfm-provenance/.../<run-id>.prov.jsonld", "roles": ["provenance"] }
  }
}
~~~

### DCAT
Promoted outputs map to `dcat:Distribution` with:
- stable identifier
- media type
- checksum
- access constraints (if any)

### PROV-O (minimum)
Emit minimal lineage sufficient to answer:
- inputs used
- outputs produced
- validations/policies applied
- which run/job produced the output

At minimum:
- `prov:Entity` input (uri + version_hint)
- `prov:Entity` output (content-addressed by sha256)
- `prov:Activity` handler run (run_id, tool version, commit_sha)
- `prov:Agent` pipeline identity (service account / runner)

### Versioning
- Use STAC versioning links and graph predecessor/successor relationships where applicable.
- “Reprocessing the same bytes” should converge to a **no-op** (same digest, same effects).

## 🧱 Architecture

### Invariants (MUST)
- **At-least-once triggers; exactly-once effects.**
- Strong digest is authoritative (ETag/version_hint is advisory).
- Catalog writes (STAC/DCAT/PROV) MUST be atomic with WAL finalize.
- Rollback MUST be a single deterministic action.

### Minimal idempotent handler skeleton (pseudo-impl)
~~~python
def handle_object(event: dict) -> str:
    """
    event: {
      "source": "http|s3|gcs|azure",
      "uri": "...",
      "version_hint": "...",
      "event_id": "...",
      "detector": "event|etag|manifest",
      "received_at": "..."
    }
    """

    # 1) Gate (WAL / idempotency)
    # If already finalized for this identity, exit safely.
    if wal.already_finalized(uri=event["uri"], version_hint=event.get("version_hint")):
        return "noop:already_finalized"

    wal.stage_pending(event)

    # 2) Fetch
    obj = fetch(event["uri"], version_hint=event.get("version_hint"))

    # 3) Strong digest (authoritative identity)
    digest = sha256(obj.bytes)

    # 4) Deterministic validation (pure, order-invariant)
    if not validate_all(obj):
        wal.mark_failed(event, digest=digest, reason="validation_failed")
        rollback.single_action(event, digest=digest)  # deterministic rollback unit
        wal.mark_rolled_back(event, digest=digest)
        return "failed:rolled_back"

    # 5) Content-addressed stage
    staged_uri = stage.put(obj, digest=digest)

    # 6) Emit provenance (minimum)
    prov_ref = provenance.emit_minimal(event=event, digest=digest, staged_uri=staged_uri)

    # 7) Atomic promotion + catalog updates + finalize
    promoted_uri = promote.atomic(staged_uri)
    catalogs.write(stac_item_for(event, digest, promoted_uri, prov_ref))
    wal.finalize(event, digest=digest, promoted_uri=promoted_uri, prov_ref=prov_ref)

    return "ok"
~~~

### Rollback semantics (MUST)
Rollback MUST leave the system in one of two acceptable states:
- **No-op state**: nothing promoted; WAL shows failed + rolled_back; provenance remains as evidence (append-only).
- **Promoted state**: promotion complete; catalogs written; WAL finalized.

Rollback SHOULD NOT delete provenance evidence.

## 🧠 Story Node & Focus Mode Integration

### Goal
Story Nodes and Focus Mode must be able to answer:
- What changed?
- When did it change?
- Why should I trust this update?
- Can I roll back?

### UI contract
Frontend MUST NOT query graph internals or raw object stores directly. UI consumes **API-provided** change outcomes backed by catalog/provenance artifacts.

Recommended API-facing fields (non-sensitive):
- `change_event_id`
- `detected_at` / `received_at`
- `source_uri`
- `object_identity` (sha256 and/or immutable version id)
- `delta_manifest_ref` (apply/revert unit)
- `qa_summary`
- `prov_ref` (and optional `openlineage_ref`)

## 🧪 Validation & CI/CD

### Determinism rules (MUST)
- Validation checks must be pure (no network dependence, no time-of-day dependence).
- Canonicalize ordering before hashing/serializing.
- Any sampling must be seeded and recorded.
- Handler remains idempotent under duplicates, reordering, and concurrent delivery.

### Policy gates (recommended)
Use policy checks (OPA/Conftest or equivalent) to enforce:
- required metadata fields present
- license + access constraints consistent
- provenance artifacts attached (or waived via reviewed waiver)
- checksums match digests
- sovereignty rules applied where required

### Test cases (minimum)
- Idempotency: same event delivered twice → second is no-op
- Concurrency: two workers race → one commits; other exits safely
- Crash safety: crash between stage and commit → safe retry
- Manifest diff stability: re-ordered listing only → diff empty
- Weak ETag: weak/changed ETag without content change → digest gate prevents false promotion
- Rollback: validation fail → deterministic rollback + WAL reflects final failure state

### Run artifacts to persist (recommended)
- `mcp/runs/change-detection/<run-id>/detector.json`
- `mcp/runs/change-detection/<run-id>/wal.json`
- `mcp/runs/change-detection/<run-id>/manifest.json`
- `mcp/runs/change-detection/<run-id>/delta_manifest.json`
- `mcp/runs/change-detection/<run-id>/provenance.prov.jsonld`
- `mcp/runs/change-detection/<run-id>/summary.md`

## ⚖ FAIR+CARE & Governance

### FAIR
- Findable: stable IDs and checksums in catalogs
- Accessible: access constraints are explicit in API/cat metadata
- Interoperable: STAC/DCAT/PROV mappings are enforced
- Reusable: provenance + validation outcomes support auditability

### CARE / sovereignty
- Apply masking/aggregation rules where required by sovereignty policy.
- Keep sensitive deltas restricted; expose only redacted summaries publicly.
- Promotions for restricted datasets require documented approvals.

### Security expectations
- No secrets in logs, telemetry, or event envelopes.
- Inbound webhook/event surfaces must validate signatures and schemas.
- Supply-chain artifacts (SBOM/signatures/attestations) are referenced for governed releases.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v11.2.6 | 2025-12-16 | Baseline content (legacy formatting) | TBD |
| v12.0.0 | 2025-12-20 | Reformatted to v12 Universal Governed Doc structure; moved legacy front-matter into body tables; added Mermaid compatibility note | TBD |

---

Footer refs:
- Change detection index: `docs/patterns/change-detection/README.md`
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
