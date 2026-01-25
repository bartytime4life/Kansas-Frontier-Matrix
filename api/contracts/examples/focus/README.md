# 🎯 Focus Mode API Contract Examples (KFM)

![Contract-First](https://img.shields.io/badge/contract--first-✅-success)
![Evidence-First](https://img.shields.io/badge/evidence--first-📌-blue)
![Provenance](https://img.shields.io/badge/provenance-STAC%2FDCAT%2FPROV-purple)
![Policy](https://img.shields.io/badge/policy-OPA%2BConftest-black)
![UI-Integrated](https://img.shields.io/badge/ui-map%20aware-🗺️-informational)

> **Focus Mode** is KFM’s evidence-backed Q&A assistant integrated into the map UI.  
> It answers questions using **only** cataloged datasets/documents/graph entities and returns **footnoted citations** for every claim. It is **advisory-only** and enforced by **policy gates**.

---

## 🧭 What this folder is

This directory is the **contract example pack** for Focus Mode.

✅ **Why it exists**
- Aligns **frontend + backend** on the wire format (request/response + streaming).
- Enables **contract tests** (JSON Schema + policy checks).
- Provides **realistic example payloads** for mocks, QA, and docs.

> [!TIP]
> If you’re looking for repo-wide contract conventions, see:  
> `../../../../docs/data/contracts/examples/README.md` (global examples & patterns)

---

## 🗂️ Suggested folder layout

```text
api/contracts/examples/focus/
├─ ✅📄 README.md                          # ✅ (this file) 📌 How Focus Mode contracts/examples are used + citation rules
├─ 📘🧾 openapi.focus.yaml                 # (optional) OpenAPI slice for Focus Mode (handy for docs/tests or subservices)
├─ 📐 schemas/                             # JSON Schemas defining Focus Mode request/response + supporting objects
│  ├─ 🔎📐🧾 FocusQueryRequest.schema.json  # Request contract (question, context refs, filters, desired output mode)
│  ├─ 📤📐🧾 FocusQueryResponse.schema.json # Response contract (answer, citations, redactions, uncertainty, actions, receipts)
│  ├─ 📦📐🧾 FocusContextBundle.schema.json # Context bundle contract (UI state, selected layers, retrieved sources, safe metadata)
│  ├─ 📚📐🧾 Citation.schema.json           # Citation contract (source id, locator, quote/snippet rules, license/attribution)
│  ├─ 🧭📐🧾 UiAction.schema.json           # UI action contract (map/layer/time/panel actions suggested by Focus)
│  └─ 🚨📐🧾 FocusError.schema.json         # Error contract (refusals, policy denials, validation errors; safe messages)
└─ 🧪 examples/                            # Example instances (golden fixtures) used by docs + contract tests
   ├─ 🧪🧾 01_explain_layer.request.json                # Ask to explain a layer (requires citations + provenance pointers)
   ├─ ✅🧾 01_explain_layer.response.json               # Answer with citations + suggested UI actions (open legend/metadata)
   ├─ 🧪🧾 02_realtime_station.request.json             # Realtime query (station id + window + freshness constraints)
   ├─ ✅🧾 02_realtime_station.response.json            # Answer includes data summary + citations + uncertainty
   ├─ 🧪🧾 03_sensitive_location.request.json           # Sensitive location request (tests redaction/denial rules)
   ├─ 🚫🧾 03_sensitive_location.refused.response.json  # Refusal response (policy denial + safe redirect + no sensitive leakage)
   ├─ 🧪🧾 04_suggest_entity.request.json               # Entity suggestion request (graph-backed linking)
   └─ ✅🧾 04_suggest_entity.response.json              # Entity suggestions with confidence + provenance refs

> [!NOTE]
> The `schemas/` and `examples/` files are **recommended siblings** to this README.  
> This document provides the contract shape so those artifacts can be added consistently.
```
---

## ✅ Contract invariants (non‑negotiable)

These are the **hard rules** that drive the contract design:

- **Evidence-first narrative**: *no citations → no answer* (fail-closed).
- **Provenance-first publishing**: Focus Mode uses **only ingested + cataloged sources** (STAC/DCAT/PROV + graph).
- **Advisory-only**: it may suggest actions, but never performs autonomous changes.
- **Policy-gated outputs**: response is validated (runtime + CI) by **OPA/Conftest** rules.
- **No hidden actions**: any suggested change must be explicit, reviewable, and traceable (PROV + ledger).

> [!IMPORTANT]
> Treat the **response** as a first-class artifact: it must include provenance identifiers and be logged for audit.

---

## 🔌 API surface (REST)

### Endpoint summary

| Method | Path | Purpose | Returns |
|---:|---|---|---|
| POST | `/api/focus` | Single-shot answer (non-streaming) | `FocusQueryResponse` |
| POST | `/api/focus/stream` | Streaming answer (SSE) | `FocusStreamEvent` frames |
| GET | `/api/focus/runs/{run_id}` | Retrieve an audited run (optional) | `FocusQueryResponse` |
| GET | `/api/focus/citations/{citation_id}` | Resolve a citation to a source object (optional) | dataset/doc/graph ref |

> [!TIP]
> KFM supports both REST and GraphQL at the platform level. This folder documents **REST-first** contracts, with a GraphQL sketch later.

---

## 🧠 Core request/response design

### 🔎 FocusQueryRequest (shape)

```json
{
  "question": "string",
  "context": {
    "map": {
      "bbox": [-97.5, 38.8, -95.8, 39.9],
      "center": [-96.8, 39.35],
      "zoom": 8,
      "crs": "EPSG:4326",
      "active_layer_ids": ["layer:drought_index_1930s"],
      "selected_features": [
        {
          "layer_id": "layer:counties",
          "feature_id": "county:Douglas",
          "geometry": { "type": "Polygon", "coordinates": [] }
        }
      ]
    },
    "time": {
      "start": "1930-01-01",
      "end": "1939-12-31"
    },
    "story": {
      "story_node_id": "story:dust-bowl-ks",
      "step_id": "panel:overview"
    },
    "attention": {
      "concept_ids": ["concept:drought", "concept:agriculture"]
    }
  },
  "options": {
    "output_format": "markdown",
    "include_audit": true,
    "include_ui_actions": true,
    "max_citations": 12
  },
  "actor": {
    "user_id": "user:123",
    "roles": ["public"],
    "session_id": "sess_abc123"
  },
  "idempotency_key": "optional-string-or-null"
}
```

#### Field notes 📝
- `context.map` makes Focus Mode **UI-aware** (viewport/layers/selection).
- `context.attention.concept_ids` supports **Conceptual Attention Nodes** (theme hubs that guide retrieval).
- `idempotency_key` allows deterministic caching/logging for the same request shape (recommended to compute via canonical JSON hashing in the backend).

---

### 🧾 FocusQueryResponse (shape)

```json
{
  "status": "ok | refused | redacted | partial",
  "run": {
    "run_id": "focusrun_2026-01-24T01:02:03Z_9f1c",
    "started_at": "2026-01-24T01:02:03Z",
    "finished_at": "2026-01-24T01:02:05Z",
    "canonical_digest": "sha256:...",
    "idempotency_key": "sha256:..."
  },
  "answer": {
    "answer_markdown": "Markdown with footnotes like this.[^1]\n\n[^1]: Citation label…",
    "citations": [
      {
        "citation_id": "cite:1",
        "kind": "dcat_dataset | stac_item | prov_activity | graph_entity | document_chunk | api_query",
        "ref": "dcat:dataset:usgs-nwis-waterdata",
        "title": "USGS Real-time Water Data (example)",
        "license": "CC-BY-4.0 | custom | unknown",
        "access": { "classification": "public | internal | restricted" },
        "links": [
          { "rel": "dcat", "href": "kfm://catalog/dcat/..." },
          { "rel": "stac", "href": "kfm://catalog/stac/..." },
          { "rel": "prov", "href": "kfm://provenance/..." }
        ]
      }
    ],
    "ui_actions": [
      {
        "type": "SET_VIEWPORT | SET_TIME_RANGE | TOGGLE_LAYER | HIGHLIGHT_FEATURE | OPEN_DATASET | OPEN_STORY_NODE | OPEN_PROVENANCE",
        "payload": {}
      }
    ],
    "suggestions": [
      {
        "type": "CREATE_ENTITY_DRAFT | LINK_ENTITY | CREATE_STORY_DRAFT",
        "requires_human_review": true,
        "summary": "string",
        "proposed_payload": {},
        "supporting_citations": ["cite:2", "cite:5"]
      }
    ]
  },
  "audit": {
    "citation_coverage": 1.0,
    "retrieval": {
      "sources_considered": 42,
      "top_hits": [{ "ref": "graph:node:...", "score": 0.82 }]
    },
    "xai": {
      "top_factors": [
        { "type": "graph_edge", "label": "LOCATED_IN", "weight": 0.21 },
        { "type": "dataset_signal", "label": "drought_index", "weight": 0.18 }
      ],
      "governance_flags": ["SENSITIVE_DATA_PRESENT:false"]
    },
    "policies_applied": [
      "EVIDENCE_FIRST_NARRATIVE",
      "NO_AUTONOMOUS_ACTIONS",
      "NO_OUTPUT_LESS_RESTRICTIVE_THAN_INPUTS"
    ]
  },
  "provenance": {
    "prov_activity_id": "prov:activity:focusrun_...",
    "ledger_entry_id": "ledger:appendonly:...",
    "agent": { "id": "agent:focus_mode_v1", "type": "software" }
  },
  "errors": []
}
```

---

## 🧷 Citations format (markdown footnotes)

### ✅ Required
- **Footnote markers** in `answer_markdown`: `[^1]`, `[^2]`, …
- **Footnote definitions** at the end:
  - `[^1]: ...`
  - Each footnote corresponds to an entry in `answer.citations[]`.

### ✅ Why footnotes?
- UI can render them as clickable links to KFM source objects.
- Policy checks can validate citation presence deterministically.

> [!IMPORTANT]
> If a claim cannot be supported by evidence, the correct response is `status: "refused"` (or `"partial"` with explicit omissions).

---

## 🛡️ Governance + policy (OPA/Conftest)

### Typical policy outcomes
- **PASS** → `status: ok` (or `partial`)
- **FAIL (insufficient evidence)** → `status: refused`
- **FAIL (sensitive output)** → `status: redacted` or `refused` depending on policy

### Common policy checks (examples)
- No output without citations (rule #5 style)
- No secrets, no private coordinates, no leaking restricted sources
- Output classification must not be less restrictive than inputs
- Required license/provider fields in citations

> [!NOTE]
> Keep policy “fail closed”: if a rule can’t be evaluated, treat it as a failure.

---

## 🌊 Streaming (SSE) contract (optional but recommended)

### POST `/api/focus/stream`

**Server-Sent Events** allow the UI to stream tokens while still enforcing governance:

- The server streams `token` events,
- then runs the final OPA scan before sending `final`.

Example event frames:

```text
event: meta
data: {"run_id":"focusrun_...","status":"streaming"}

event: token
data: {"delta":"As of 8:00 PM, the water level is ","citations":[]}

event: token
data: {"delta":"12.4 ft","citations":[1]}

event: final
data: {"status":"ok","answer_markdown":"...","citations":[...],"provenance":{...}}
```

> [!IMPORTANT]
> Even in streaming mode, the **final** frame must be policy-checked and contain a complete citation set.

---

## 🧬 GraphQL sketch (optional)

If the platform exposes Focus Mode via GraphQL, keep the types congruent:

```graphql
input FocusQueryInput {
  question: String!
  context: FocusContextInput!
  options: FocusOptionsInput
  idempotencyKey: String
}

type FocusQueryResult {
  status: FocusStatus!
  run: FocusRun!
  answer: FocusAnswer
  audit: FocusAudit
  provenance: FocusProvenance!
  errors: [FocusError!]!
}

type Query {
  focus(query: FocusQueryInput!): FocusQueryResult!
}
```

---

## 🧩 UI Actions (how Focus Mode “drives” the interface)

UI actions are **suggestions** the client can apply (or ignore). Common actions:

- `SET_VIEWPORT` → pan/zoom to relevant area
- `SET_TIME_RANGE` → synchronize timeline slider
- `TOGGLE_LAYER` → enable/disable a layer
- `HIGHLIGHT_FEATURE` → outline a feature
- `OPEN_DATASET` → open dataset panel
- `OPEN_PROVENANCE` → open PROV/ledger view
- `OPEN_STORY_NODE` → jump to a narrative

> [!TIP]
> Keep `ui_actions[].payload` minimal and stable. Use canonical IDs over raw blobs.

---

## 🧪 Example payloads

### Example 01 — Explain a visible layer 🗺️

**Request**
```json
{
  "question": "What does this drought index layer show, and what time period is it summarizing?",
  "context": {
    "map": {
      "bbox": [-100.2, 37.0, -94.6, 40.2],
      "center": [-97.4, 38.6],
      "zoom": 6,
      "crs": "EPSG:4326",
      "active_layer_ids": ["layer:drought_index_1930s"],
      "selected_features": []
    },
    "time": { "start": "1930-01-01", "end": "1939-12-31" }
  },
  "options": { "output_format": "markdown", "include_ui_actions": true }
}
```

**Response (abridged)**
```json
{
  "status": "ok",
  "answer": {
    "answer_markdown": "This layer visualizes a drought severity index aggregated over the 1930s.[^1]\n\n[^1]: Drought Index (1930–1939) — KFM catalog entry.",
    "citations": [{ "citation_id": "cite:1", "kind": "stac_item", "ref": "stac:item:drought_1930s", "title": "Drought Index 1930–1939", "license": "CC-BY-4.0", "access": { "classification": "public" }, "links": [{ "rel": "stac", "href": "kfm://catalog/stac/items/drought_1930s" }] }],
    "ui_actions": [
      { "type": "OPEN_DATASET", "payload": { "dataset_id": "dcat:dataset:drought_1930s" } },
      { "type": "SET_TIME_RANGE", "payload": { "start": "1930-01-01", "end": "1939-12-31" } }
    ]
  },
  "errors": []
}
```

---

### Example 02 — Real-time station value 🌊

**Request**
```json
{
  "question": "What's the current water level of the Kansas River at Topeka?",
  "context": {
    "map": {
      "bbox": [-96.9, 39.0, -95.4, 39.2],
      "center": [-96.0, 39.1],
      "zoom": 10,
      "crs": "EPSG:4326",
      "active_layer_ids": ["layer:realtime_river_gauges"]
    },
    "time": { "start": "now-2h", "end": "now" }
  },
  "options": { "output_format": "markdown", "include_audit": true }
}
```

**Response (abridged)**
```json
{
  "status": "ok",
  "answer": {
    "answer_markdown": "As of 2026-01-24T01:00:00Z, the water level at the Topeka gauge is 12.4 ft.[^1]\n\n[^1]: USGS NWIS real-time feed (KFM catalog + station entity).",
    "citations": [
      { "citation_id": "cite:1", "kind": "dcat_dataset", "ref": "dcat:dataset:usgs-nwis-waterdata", "title": "USGS NWIS Real-time Water Data", "license": "Public Domain", "access": { "classification": "public" }, "links": [{ "rel": "dcat", "href": "kfm://catalog/dcat/usgs-nwis" }] }
    ],
    "ui_actions": [
      { "type": "HIGHLIGHT_FEATURE", "payload": { "layer_id": "layer:realtime_river_gauges", "feature_id": "station:topeka" } }
    ]
  },
  "audit": {
    "policies_applied": ["EVIDENCE_FIRST_NARRATIVE", "PROVENANCE_FIRST_PUBLISHING"]
  }
}
```

> [!NOTE]
> Real-time answers should still produce PROV describing the **timestamped reading** used.

---

### Example 03 — Sensitive location (refusal / redaction) 🔒

**Request**
```json
{
  "question": "Give me the exact coordinates of the restricted archaeological site near X.",
  "context": { "map": { "bbox": [-99, 37, -95, 40], "center": [-97, 38.5], "zoom": 7, "crs": "EPSG:4326" } },
  "actor": { "roles": ["public"] }
}
```

**Response**
```json
{
  "status": "refused",
  "errors": [
    {
      "code": "POLICY_VIOLATION",
      "message": "This request asks for restricted or sensitive location detail. Focus Mode cannot provide exact coordinates with your access level.",
      "details": { "policy": "NO_SENSITIVE_COORDINATES" }
    }
  ],
  "provenance": {
    "prov_activity_id": "prov:activity:focusrun_...",
    "ledger_entry_id": "ledger:appendonly:..."
  }
}
```

---

### Example 04 — Suggest creating a missing entity 🧩

**Request**
```json
{
  "question": "Is there a record for Historian Jane Doe in the knowledge graph?",
  "context": { "map": { "bbox": [-102, 36.9, -94.6, 40.1], "center": [-98.5, 38.5], "zoom": 5, "crs": "EPSG:4326" } },
  "options": { "include_ui_actions": true }
}
```

**Response (abridged)**
```json
{
  "status": "partial",
  "answer": {
    "answer_markdown": "I don’t see an existing entity for *Jane Doe* in the current KFM graph snapshot.[^1]\n\nIf you want, I can propose a draft entity for review (with sources).[^2]\n\n[^1]: Graph search snapshot (KFM). \n[^2]: Document reference supporting the proposed entity.",
    "citations": [
      { "citation_id": "cite:1", "kind": "api_query", "ref": "kfm://queries/graph/search?term=Jane%20Doe", "title": "Graph search result for “Jane Doe”", "license": "N/A", "access": { "classification": "public" }, "links": [] },
      { "citation_id": "cite:2", "kind": "document_chunk", "ref": "doc:archive:ks_history_001#chunk=18", "title": "Kansas Historical Archive (excerpt)", "license": "unknown", "access": { "classification": "public" }, "links": [] }
    ],
    "suggestions": [
      {
        "type": "CREATE_ENTITY_DRAFT",
        "requires_human_review": true,
        "summary": "Create a draft Person entity for Jane Doe with links to the cited archive entry.",
        "proposed_payload": { "entity_type": "Person", "label": "Jane Doe", "properties": { "roles": ["Historian"] } },
        "supporting_citations": ["cite:2"]
      }
    ]
  }
}
```

---

## 🧱 Contract tests checklist

When you add/change Focus Mode contracts, ensure:

- ✅ **JSON Schema** validation passes for request/response examples
- ✅ **OPA/Conftest** policy checks pass (citations, sensitivity, licenses, etc.)
- ✅ **Golden examples** are updated (examples/ as fixtures)
- ✅ **Version bump** if breaking changes (and a migration note)

> [!TIP]
> Breakage signal: if UI needs code changes to parse fields, treat it as a contract-breaking change.

---

## 🔐 Security & prompt safety (high-level)

- Sanitize user inputs (prompt injection defenses)
- Parameterize DB access (no string concatenation)
- Enforce RBAC based on dataset/entity classification
- Never leak secrets or restricted coordinates
- Log runs (PII-aware) for audit, with governance controls

---

## 📚 Related KFM docs (recommended reading)

From this directory, the common “jump links” are:

- `../../../../docs/architecture/` — AI system, governance, policy pack
- `../../../../docs/ui/` — Focus Mode panel + audit UX
- `../../../../docs/data/` — STAC/DCAT/PROV profiles + contracts
- `../../../../api/scripts/policy/` — OPA/Conftest rules + examples
- `../../../../docs/guides/pipelines/` — how AI suggestions become PRs (human reviewed)

---

## 🧾 Glossary

- **STAC**: SpatioTemporal Asset Catalog (geospatial asset metadata)
- **DCAT**: Data Catalog Vocabulary (dataset-level metadata)
- **PROV**: W3C Provenance model (lineage)
- **OPA/Conftest**: Policy-as-code enforcement (CI + runtime)
- **Conceptual Attention Node**: a theme hub in the graph (e.g., “drought”) used to guide retrieval
- **Governance ledger**: append-only log for auditable AI/system actions

---

## 🧰 “Good citizen” rules for implementers

- Prefer stable IDs (`dcat:dataset:…`, `stac:item:…`, `prov:activity:…`) over raw URLs
- Keep `answer_markdown` human-first, audit second (citations must still be complete)
- Always include `provenance.*` identifiers so answers are traceable
- If in doubt: **refuse** or **redact**, never guess

💡 This contract is designed to make Focus Mode “powerful, but never mysterious.”
