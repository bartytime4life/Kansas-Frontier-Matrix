# 📨 Event Contracts (`api/src/contracts/events/`)

🏷️ **Status:** `Active` • 🧱 **Principle:** `Contract-first` • 🧪 **Validation:** `Required` • 🔒 **Scope:** `Internal + Telemetry`

> This folder defines **machine-validated event contracts** used for asynchronous workflows and audit/telemetry across the KFM backend.  
> In KFM’s architecture, internal components can communicate via **message queues / event streams** (e.g., RabbitMQ, Kafka, cloud equivalents) to decouple processing—like publishing a `"new_image_available"` event when ingestion completes so downstream pipelines can react asynchronously. :contentReference[oaicite:0]{index=0}

---

## 📌 Why event contracts exist

KFM uses event-driven patterns to improve resilience and decoupling—so the web/API layer can trigger work and return quickly, while background workers process and publish results when ready. :contentReference[oaicite:1]{index=1}

Event contracts here are treated as **contract artifacts**: machine-validated specs that define interfaces and must be versioned and honored. :contentReference[oaicite:2]{index=2}

Also: KFM’s broader repo guidance is **contract-first**: schemas and contracts are first-class artifacts, and changes trigger versioning + compatibility checks. :contentReference[oaicite:3]{index=3}

---

## 🧩 What belongs in this folder

✅ **Belongs here**
- Event payload **schemas** (contract artifacts)
- Shared **event envelope** types (metadata requirements)
- Examples / fixtures (sample payloads)
- Contract tests (producer + consumer compatibility)
- Version history notes for breaking changes

🚫 **Does not belong here**
- Transport wiring (Kafka/RabbitMQ/NATS client setup)
- Business logic handlers
- Database migrations
- HTTP request/response DTOs (those belong in API route contracts)

---

## 🧠 “Event” definition (KFM-flavored)

An **event** is a *fact* that something happened.  
It is not a command (requesting something happen) and not a query (asking for data).

KFM uses events for:
- **Pipeline orchestration** (ingestion → processing → publish)
- **Cross-service decoupling** (workers subscribe without tight coupling)
- **UI streaming updates** (optionally via WebSockets or Server-Sent Events) :contentReference[oaicite:4]{index=4}
- **Governance + audit trails** (especially around sensitive data handling) :contentReference[oaicite:5]{index=5}

---

## 🧱 Contract-first rules (non-negotiable)

### 1) Events are contract artifacts
Event schemas MUST be:
- machine-validated
- versioned
- treated as the single source of truth for event shape + semantics  
:contentReference[oaicite:6]{index=6}

### 2) Backwards compatibility is the default
Breaking changes require a version bump and coordination—mirroring KFM’s API contract versioning policy. :contentReference[oaicite:7]{index=7}

### 3) Contract changes must be tested
Contract changes are not “just refactors.” They require tests to ensure known inputs/outputs remain consistent (adapt this principle from API contracts to events). :contentReference[oaicite:8]{index=8}

---

## 📦 Standard Event Envelope

To keep producers/consumers consistent across services and transports, every event should follow a shared envelope pattern:

### ✅ Required envelope fields

- `meta.event_id` — unique id (UUID recommended)
- `meta.type` — stable event type string
- `meta.version` — schema major version for this `type`
- `meta.occurred_at` — ISO timestamp (when it happened)
- `meta.producer` — service name (or subsystem)
- `meta.correlation_id` — ties a workflow together (optional but strongly recommended)
- `meta.trace_id` — distributed tracing (optional but recommended)
- `meta.classification` — data sensitivity / governance flags
- `meta.provenance` — pointers to evidence lineage where relevant (PROV / catalog IDs)
- `data` — the event payload

> 🔎 Why include provenance? KFM emphasizes traceability and evidence-linked artifacts; event payloads should generally **reference** stored artifacts (data lake, STAC assets, etc.) rather than embed large blobs. :contentReference[oaicite:9]{index=9}

### Example envelope (JSON)

```json
{
  "meta": {
    "event_id": "b6c57f3c-3cfe-4c05-9d4e-7e61b24f6f0e",
    "type": "kfm.ingestion.new_image_available",
    "version": 1,
    "occurred_at": "2026-01-04T18:22:19.000Z",
    "producer": "ingestion-service",
    "correlation_id": "corr_9a0f3f2f1f6d",
    "trace_id": "trace_01J0XYZABC...",
    "classification": {
      "tier": "public",
      "redaction_required": false
    },
    "provenance": {
      "prov_activity_id": "prov:activity:ingest:2026-01-04T18:22Z",
      "stac_item_ids": ["stac:item:ks:landsat:2026-01-04"],
      "dcat_distribution_id": "dcat:dist:landsat-mosaic-2026-01-04"
    }
  },
  "data": {
    "asset_kind": "satellite_image",
    "asset_ref": "stac:item:ks:landsat:2026-01-04",
    "hint": "NDVI pipeline can subscribe and process"
  }
}
```

---

## 🏷️ Event type naming conventions

### Recommended pattern
Use a **namespace + domain + action** naming approach:

```
kfm.<domain>.<event_name>
```

Examples (real + suggested):
- `kfm.ingestion.new_image_available` ✅ (based on KFM’s documented example queue/event name) :contentReference[oaicite:10]{index=10}
- `kfm.ui.focus_mode_redaction_notice_shown` ✅ (based on KFM audit/telemetry example) :contentReference[oaicite:11]{index=11}
- `kfm.pipeline.run_started` (suggested)
- `kfm.catalog.stac_item_published` (suggested)
- `kfm.graph.sync_completed` (suggested)

### Naming rules
- Prefer **lowercase** + **snake_case** tokens (mirrors `"new_image_available"`)
- Keep names stable; avoid embedding environment (`dev/prod`) into `type`
- If routing requires environment separation, handle it in **transport config** (topic/queue naming), not contract `type`

---

## 🧬 Versioning & compatibility

### How versioning works
- `meta.type` stays stable for the “concept”
- `meta.version` increments when the **schema meaningfully changes**

### What counts as a breaking change (requires `version++`)
- Removing/renaming fields
- Changing a field type
- Tightening constraints (optional → required)
- Changing meaning/semantics of a field
- Changing enum values in a non-additive way

> KFM’s general rule: breaking a contract requires a deliberate version bump + coordination (mirrors API versioning guidance). :contentReference[oaicite:12]{index=12}

### What is considered safe / non-breaking
- Adding optional fields
- Adding new enum values (if consumers handle unknowns safely)
- Relaxing constraints

### Deprecation policy
When releasing `v2` for a `type`:
- keep emitting `v1` in parallel (bridge / dual publish) until consumers migrate
- document deprecation window in the contract’s changelog section
- add contract tests ensuring both versions remain valid during overlap

---

## 🔒 Security, governance, and sovereignty hooks

KFM’s network design notes that internal systems (including a message broker/data bus) are not publicly accessible—only internal components can publish/subscribe. :contentReference[oaicite:13]{index=13}

### Required practices
- **Do not** publish raw sensitive datasets in an event payload
- Prefer references to controlled storage locations (IDs, URIs, catalog refs)
- Include `classification` metadata in `meta`
- Emit audit/telemetry events when redaction or access controls are applied

KFM specifically calls out audit trails and emitting telemetry signals like `focus_mode_redaction_notice_shown` to document when data was withheld/generalized. :contentReference[oaicite:14]{index=14}

---

## 🧪 Validation & testing

### Validation expectations
Every event payload must be machine-validated against its contract (schema) before:
- publishing (producer-side validation)
- processing (consumer-side validation)

### Contract tests
At minimum:
- ✅ “golden payload” tests (examples validate)
- ✅ backwards compatibility tests (v1 payloads remain accepted if still supported)
- ✅ breaking change detection (CI should fail if a “breaking” change occurs without a version bump)

This mirrors KFM’s emphasis that contract changes are tested against known behavior to ensure consistency. :contentReference[oaicite:15]{index=15}

---

## 🛠️ Adding a new event contract (checklist)

### ✅ Step-by-step
1. **Choose domain + name**  
   - Confirm it fits the `kfm.<domain>.<event_name>` convention
2. **Define the schema**  
   - Include envelope + payload requirements
3. **Write at least one example payload**  
   - Add a “happy path” fixture
4. **Add contract tests**  
   - Validate schema + example payload
5. **Document governance**  
   - classification expectations
   - provenance hooks (if applicable)
6. **Version it**  
   - start at `version: 1`
7. **Update the registry/index** (if your repo maintains one)  
   - Keep discovery simple and explicit

### ✅ Definition of Done (DoD)
- [ ] Schema exists and is machine-validated
- [ ] Example payload exists and passes validation
- [ ] Contract tests added/updated
- [ ] Versioning rules followed (no breaking change without version bump)
- [ ] Classification + provenance guidance documented (if relevant)

---

## 🧾 KFM-aligned example events

### 1) Ingestion → pipeline trigger (`new_image_available`)
KFM documents an example where ingestion publishes an event to a queue like `"new_image_available"` so pipelines can subscribe and process asynchronously. :contentReference[oaicite:16]{index=16}

**Use it for:** “new raw satellite image arrived” → trigger NDVI pipeline, tiling jobs, metadata indexing, etc.

### 2) Governance telemetry (`focus_mode_redaction_notice_shown`)
KFM’s governance guidance calls out emitting an event like `focus_mode_redaction_notice_shown` as an audit signal when data was withheld/generalized. :contentReference[oaicite:17]{index=17}

**Use it for:** audit trails, compliance reporting, “who saw what and why” tracking.

---

## 🗂️ Suggested local structure (optional)

> You don’t have to use this exact layout, but keeping shared envelope parts centralized reduces drift.


```text
api/src/contracts/events/
├─ 🧭 README.md
├─ 🧰 _shared/                         🧱 shared envelope + meta building blocks
│  ├─ 📦 event-envelope.schema.json     📨 canonical event envelope schema
│  └─ 🏷️ event-meta.schema.json         🧾 shared meta schema (ids, timestamps, trace, etc.)
├─ 🚚 ingestion/                        🌾 ingestion-domain event contracts
│  └─ 🛰️ new_image_available.v1.schema.json
├─ 🖥️ ui/                               🎛️ UI/telemetry-domain event contracts
│  └─ 🛡️ focus_mode_redaction_notice_shown.v1.schema.json
└─ 🗺️ registry.ts                       🧩 (optional) maps (type, version) → schema
```

---

## 📚 References (project docs)

- KFM contract-first + contract artifact definition (schemas/contracts as first-class, machine-validated) :contentReference[oaicite:18]{index=18}:contentReference[oaicite:19]{index=19}
- KFM API versioning + compatibility guidance (apply same mindset to event contracts) :contentReference[oaicite:20]{index=20}
- KFM contract testing expectation (apply to events as well) :contentReference[oaicite:21]{index=21}
- KFM messaging/event-stream decoupling + `"new_image_available"` example :contentReference[oaicite:22]{index=22}
- KFM internal message broker not publicly accessible (security boundary) :contentReference[oaicite:23]{index=23}
- KFM governance audit telemetry example (`focus_mode_redaction_notice_shown`) :contentReference[oaicite:24]{index=24}

