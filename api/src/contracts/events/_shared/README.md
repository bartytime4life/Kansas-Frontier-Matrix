# 🧩 `_shared` Event Contracts (KFM)

![Contract-first](https://img.shields.io/badge/contracts-contract--first-0aa2ff)
![Provenance-first](https://img.shields.io/badge/provenance-enforced-6f42c1)
![Policy gates](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-2ea44f)
![Event-driven](https://img.shields.io/badge/architecture-event--driven-f97316)
![Status](https://img.shields.io/badge/status-active-success)

> **Purpose:** This folder defines the **shared, reusable building blocks** used by all event contracts in `api/src/contracts/events/*`.
> Think of it as the “standard event envelope + common metadata” layer that keeps KFM **auditable, idempotent, provenance-rich, and policy-gated**.

---

## 📘 Overview

### ✅ What this folder is for
- A **single, consistent event envelope** (CloudEvents-inspired) used across KFM.
- Shared primitives: `EventType`, `EventId`, `RunId`, `DatasetId`, `Actor`, `Classification`, `ProvenanceRef`, etc.
- Shared “extension blocks” (KFM-specific) that attach governance + provenance + run manifests to any event.
- Cross-cutting rules: **versioning**, **compatibility**, **redaction**, and **validation**.

### ❌ What this folder is *not* for
- Defining *domain-specific payloads* (those live in sibling event folders like `events/catalog/*`, `events/pipeline/*`, etc.).
- Implementing transports (Kafka/NATS/SQS/WebSockets). This is **contract-level only**.

---

## 🗂️ Directory Layout

> ⚠️ The exact filenames may differ in your repo; this README describes the **intended contract anatomy** for `_shared`.

```text
api/src/contracts/events/
└─ 🧩 _shared/
   ├─ 📍📄 README.md                 # 📍 You are here 📌 Shared event primitives used by all event domains/versions
   ├─ 📦🧾 envelope.*                # Core event wrapper: headers + payload + timestamps + schema/version routing
   ├─ 🆔🧾 identifiers.*             # Strongly-typed IDs (EventId, RunId, DatasetId, StoryId, etc.) + validation helpers
   ├─ 🔒🧾 classification.*          # Classification labels (public/internal/restricted) + handling hints/propagation fields
   ├─ 🧬🧾 provenance.*              # Provenance pointers: PROV/DCAT/STAC refs + evidence manifest refs
   ├─ 🛡️🧾 governance.*              # Governance fields: policy decisions, approvals, waivers, ledger pointers
   ├─ 🔗🧾 links.*                   # Typed link objects (uri + rel + mediaType + integrity/digest when available)
   └─ 🚫🧾 errors.*                  # Standard error/violation shapes (codes, severities, pointers, remediation hints)
```

---

## ✨ Design Principles (KFM-style)

- **Contract-first:** every event is validated against a schema before it’s accepted/published.  
- **Evidence-first:** events must carry enough references to show *why* the system believes something is true.
- **Append-only mindset:** don’t rewrite history—emit new facts/events and link them.
- **Policy-gated:** validation + governance checks can “fail closed.”
- **Idempotent & replayable:** events should be safe to reprocess without duplicating side effects.

---

## 📦 Standard Event Envelope (CloudEvents-inspired)

All events should serialize into a consistent envelope with:
- **routing + traceability** fields (who/what/when/where)
- **governance + provenance** fields (why it’s allowed + what evidence backs it)
- a **typed payload** (`data`) whose schema is defined in the domain event contract

### 🧾 Canonical shape

```jsonc
{
  // ---- CloudEvents-ish core -------------------------------------------------
  "specversion": "1.0",
  "id": "evt_01HTY8WQ9YJ7Q0V7Q1J9J9Z3A8",
  "type": "kfm.pipeline.run.completed.v1",
  "source": "kfm://api/pipelines/ingest",
  "subject": "kfm.dataset.kansas.usgs.nwis.river_gauges",
  "time": "2026-01-23T18:42:17.120Z",
  "datacontenttype": "application/json",
  "dataschema": "https://schemas.kfm.dev/events/pipeline/run_completed.v1.schema.json",

  // ---- KFM extensions -------------------------------------------------------
  "kfm": {
    "classification": {
      "level": "public",
      "redactions": [],
      "handling": ["cacheable"]
    },
    "actor": {
      "kind": "service",
      "id": "kfm-api",
      "display": "KFM API",
      "roles": ["emitter"]
    },
    "run": {
      "run_id": "run_20260123_184217Z_9d2f",
      "idempotency_key": "sha256:....",
      "canonical_digest": "sha256:....",
      "manifest_ref": {
        "kind": "uri",
        "href": "kfm://audits/run_20260123_184217Z_9d2f/run_manifest.json"
      }
    },
    "provenance": {
      "prov_activity": "kfm.prov.activity.ingest.usgs_nwis.20260123",
      "prov_ref": { "kind": "uri", "href": "kfm://prov/kfm.prov.activity.ingest.usgs_nwis.20260123.json" },
      "dcat_dataset_id": "kfm.dataset.kansas.usgs.nwis.river_gauges",
      "stac_collection": "kfm.stac.collection.usgs_nwis_river_gauges",
      "evidence": [
        { "rel": "source", "href": "https://waterdata.usgs.gov/", "mediaType": "text/html" }
      ]
    },
    "governance": {
      "policy_pack": "kfm-policy-pack@v13",
      "decisions": [
        { "policy_id": "KFM-PROV-001", "result": "pass" },
        { "policy_id": "KFM-LICENSE-001", "result": "pass" }
      ],
      "ledger_ref": { "kind": "uri", "href": "kfm://ledger/evt_01HTY8WQ9YJ7Q0V7Q1J9J9Z3A8" }
    },
    "trace": {
      "trace_id": "trc_3f2d...",
      "span_id": "spn_9aa1...",
      "parent_span_id": "spn_17be..."
    }
  },

  // ---- Domain payload -------------------------------------------------------
  "data": {
    "status": "completed",
    "outputs": [
      { "kind": "dataset", "id": "kfm.dataset.kansas.usgs.nwis.river_gauges", "version": "2026-01-23" }
    ],
    "summary": { "records_in": 1482, "records_out": 1482, "warnings": 0 }
  }
}
```

---

## 🧱 Shared Fields (Required vs Recommended)

### ✅ Always required
| Field | Why it exists |
|------|----------------|
| `id` | unique event identity (supports dedupe + audit) |
| `type` | routing + compatibility contract (versioned) |
| `source` | where it came from (service/component) |
| `time` | when it happened (not when it was processed) |
| `data` | domain payload |

### ⭐ Strongly recommended
| Field | Why it exists |
|------|----------------|
| `subject` | “what this is about” (dataset/story/entity) |
| `dataschema` | points to a JSON Schema (or equivalent) |
| `kfm.classification` | prevents “oops we leaked sensitive detail” |
| `kfm.provenance` | enables evidence-backed UI + replayable truth |
| `kfm.governance` | shows policy decisions + ledger hooks |
| `kfm.run` | supports determinism + idempotency |

---

## 🧬 Provenance & Evidence References (STAC / DCAT / PROV)

KFM leans on standard metadata and lineage patterns, so shared events should be able to reference:

- **DCAT dataset identifiers** (discovery + licensing + ownership)
- **STAC collections/items** (geospatial assets + extents + access)
- **PROV activities/entities/agents** (lineage + reproducibility)

**Rule of thumb:** if an event asserts something about data, it must carry enough refs to reconstruct the chain of custody.

---

## 🧾 Run Manifests, Canonical Digests, and Idempotency

Some KFM workflows generate a **Run Manifest** (a JSON audit record) per pipeline run.  
Shared events should support these fields:

- `run_id` – human navigable run handle
- `idempotency_key` – stable dedupe key (same inputs + same config ⇒ same key)
- `canonical_digest` – hash of canonicalized manifest content (self-fingerprinting)
- `manifest_ref` – pointer to the stored manifest artifact

> 💡 This is what makes “replay the pipeline” and “prove what happened” actually workable.

---

## 🛡️ Classification, Redaction, and Privacy

KFM operates across public and sensitive domains. Events must be safe to:
- store long-term
- replay into new systems
- display in UI contexts

Recommended shared pattern:

```jsonc
"classification": {
  "level": "public | internal | restricted",
  "redactions": ["precise_location", "pii", "sacred_site"],
  "handling": ["no_cache", "no_export", "review_required"]
}
```

**Guideline:** If a domain payload could contain sensitive info, either:
- **omit it** and replace with references, or
- **include it but mark + redact + gate** it (policy + access control).

---

## 🧭 Event Type Naming Convention

Use **dot-separated**, versioned types:

```text
kfm.<domain>.<entity>.<action>.v<major>
```

Examples:
- `kfm.catalog.dataset.published.v1`
- `kfm.pipeline.run.started.v1`
- `kfm.pipeline.run.completed.v1`
- `kfm.focus.answer.generated.v1`
- `kfm.story.node.published.v1`
- `kfm.pulse.thread.created.v1` 🫀

**Versioning rule:** bump `v<major>` only for breaking changes (field removals, meaning changes).

---

## 🧠 Special Case: AI & Narrative Outputs (Focus Mode / Story / Pulse)

AI outputs in KFM are treated as *first-class artifacts*:
- they must be **cited**
- they must be **logged**
- they must be **reviewable**

Shared events should support:
- linking to **source evidence**
- marking content as **AI-generated**
- tying outputs to a **governance ledger entry**
- connecting to Story Nodes / Pulse Threads (short-form narrative updates)

---

## ✅ Validation & “Fail Closed” Gates

Event validation is expected to happen:
- in API handlers (before accepting an event)
- in pipelines (before publishing outputs)
- in CI (for contract changes)
- optionally at runtime via policy checks (OPA-style)

**Definition of done** for any new event contract ✅
- [ ] Has a schema / model (and lives under `events/<domain>/...`)
- [ ] Uses `_shared` envelope and extensions (no custom snowflakes)
- [ ] Includes classification guidance
- [ ] Includes provenance hooks
- [ ] Has examples + tests + compatibility notes

---

## 🧪 Quick Start (for new event authors)

1) Pick a type name: `kfm.<domain>.<entity>.<action>.v1`  
2) Define your domain payload schema (only `data`)  
3) Wrap it with the shared envelope  
4) Add provenance + governance refs where relevant  
5) Add at least one sample JSON fixture (happy path + failure path)  

---

## 🔗 Related KFM Concepts (Where events show up)

- 🗺️ UI can surface event-driven updates (live layers, notifications, “pulse” markers)
- 🧵 Pulse Threads can be emitted from watchers and then curated/published
- 🤖 W-P-E agents generate immutable event records and propose changes via PRs
- 🧾 Policy packs enforce required metadata and citation rules
- 🧬 Provenance references keep “the map behind the map” intact

---

## 📚 References (internal to the repo)

Look for these docs in your repo (names may vary):
- `docs/architecture/*` (W-P-E, policy gates, AI design)
- `docs/data/contracts/*` (STAC/DCAT/PROV profiles & examples)
- `docs/ui/*` (Focus Mode, Story Nodes, live data UX)
- `data/audits/*` (run manifests and pipeline evidence)

---

## 🧯 FAQ

**Q: Do I put domain fields (like `dataset_id`) at the top level?**  
A: No—put domain specifics inside `data`. Use top-level + `kfm.*` for cross-cutting metadata only.

**Q: What if I don’t have PROV for an event yet?**  
A: Don’t publish the event as “official” output. Emit a *draft/internal* event, or fail closed until lineage exists.

**Q: Can events carry big blobs (GeoJSON, tiles, model outputs)?**  
A: Prefer references (`links`, `manifest_ref`, OCI artifacts) over large payloads. Events should stay lightweight and replay-friendly.

---

## 🧠 Motto

> **Events are the receipts.**  
> If it happened in KFM, we should be able to replay it, verify it, cite it, and explain it.

