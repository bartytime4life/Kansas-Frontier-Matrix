# 🧭 Focus Mode — Response Examples (API v1)

![Contract](https://img.shields.io/badge/contract-v1-blue)
![Endpoint](https://img.shields.io/badge/endpoint-POST%20%2Fv1%2Ffocus-222)
![Evidence](https://img.shields.io/badge/evidence-STAC%20%7C%20DCAT%20%7C%20PROV-0a0a0a)
![Policy](https://img.shields.io/badge/policy-OPA%20%2F%20Rego%20gated-111)
![UX](https://img.shields.io/badge/UI-Audit%20Panel%20%26%20Provenance-333)

> **Path:** `api/contracts/examples/responses/v1/focus/README.md` 📌

> [!IMPORTANT]
> **Focus Mode is advisory-only 🧠🧑‍⚖️** (no autonomous actions) and **must return evidence-backed answers with citations**. If citations can’t be produced, the system **must refuse** rather than speculate. ¹ ² ³

---

<details>
<summary><strong>📚 Table of Contents</strong></summary>

- 🎯 Purpose
- 🧱 Response shape (v1)
- 🧾 Citations & evidence model
- 🛡️ Governance, redaction, and “fail closed”
- 🧬 Provenance model
- 🧠 Explainability / Audit Panel payload
- 🧪 Example responses (canonical)
- ✅ Contract-test expectations
- 🧩 Source map (all project files)

</details>

---

## 🎯 Purpose

This folder contains **canonical, contract-testable** example responses for:

- `POST /v1/focus` (Focus Mode Q&A + guided exploration)
- UI rendering (Focus panel, **Audit Panel**, provenance popovers)
- Governance/audit logging (policy checks, redactions, ledger linkage)

These examples embody the project’s **contract-first** and **provenance-first** design: schemas are first-class artifacts, and anything returned to the UI must be traceable back to cataloged sources (STAC/DCAT/PROV + graph IDs). ² ⁴ ⁵

---

## 🧱 Response shape (v1)

### ✅ Envelope: `kfm.focus.response`

At minimum, every v1 response should provide:

- `api_version`, `kind`, `request_id`, `created_at`, `status`
- `input` echo (query + context + options)
- `output` (answer blocks + citations + suggestions)
- `governance` (policy checks + redactions + ledger reference)
- `provenance` (PROV bundle pointers / derived-from list)
- `warnings` (optional)

> [!NOTE]
> The UI must **not** bypass the API to directly query databases/graph. The API is the governed middle layer. ⁶

### Field quick reference

| Field | Purpose | Notes |
|---|---|---|
| `output.answer.blocks[]` | UI-ready answer, separated into `fact` vs `analysis` | Mirrors Story Node practice: distinguish fact vs interpretation. ⁴ |
| `output.citations[]` | Machine-readable citations | Designed to resolve to **catalog + provenance** artifacts. ⁶ ⁷ |
| `output.entities` | Graph IDs referenced by the answer | Stable IDs power UI cross-linking. ⁴ ⁶ |
| `output.audit` | Explainability payload | Feeds the Audit Panel (factors + governance flags). ⁸ ⁹ |
| `governance.checks[]` | OPA/Policy Pack results | Must reflect “fail closed” posture. ¹⁰ |
| `provenance.wasDerivedFrom[]` | PROV lineage links | Supports “how did we get here?” traceability. ⁷ |

---

## 🧾 Citations & evidence model

### Evidence triplet (STAC + DCAT + PROV)

KFM treats the catalogs as an **evidence triplet**:

- **DCAT** = dataset discovery + licensing + distributions  
- **STAC** = spatiotemporal asset/items  
- **PROV(-O)** = lineage (entities/activities/agents)

These catalogs are version-controlled and required before data is considered “published” into the platform. ⁶ ¹¹

### How citations bind to the answer

- `output.answer.blocks[].md` may contain footnote markers like `[^1]`
- `output.citations[]` contains the authoritative mapping of those footnotes to resolvable KFM references (`kfm://...`, DCAT/STAC IDs, PROV IDs, graph IDs)
- **Hard gate**: if the system can’t produce citations for claims, it **must refuse**. ³ ¹²

---

## 🛡️ Governance, redaction, and “fail closed”

Focus Mode responses must carry enough governance context to:

- communicate *why* something is redacted or refused,
- preserve community trust (FAIR+CARE, sovereignty-awareness),
- and enable oversight/auditing.

KFM bakes governance into the pipeline from intake onward (classification labels, license checks, sovereignty constraints), and defaults to **blocking** when checks cannot be performed (“fail closed”). ¹¹ ¹⁰

> [!WARNING]
> Focus Mode must not leak sensitive coordinates (e.g., sacred sites / restricted heritage locations). Redact/generalize or refuse. ¹ ³ ¹²

---

## 🧬 Provenance model

Focus Mode should be able to assert provenance in PROV terms:

- **Entity**: input dataset(s), doc excerpts, sensor readings
- **Activity**: the retrieval + answer generation run
- **Agent**: Focus Mode v1 (plus human reviewers when applicable)

PROV links like `prov:used`, `prov:wasGeneratedBy`, `prov:wasDerivedFrom`, `prov:wasAssociatedWith` allow a user (or auditor) to trace *how* an answer was produced and *which* artifacts were used. ⁷

> [!TIP]
> KFM also proposes treating **DevOps events** (e.g., PR merges) as PROV activities/entities/agents to strengthen end-to-end traceability from code to datasets and outputs. ¹³

---

## 🧠 Explainability / Audit Panel payload

The UI includes an **Audit Panel** to show:

- top influencing factors behind an answer,
- which datasets/documents were used,
- governance flags/warnings,
- and (optionally) retrieval trace stats.

This is described as a key trust-building feature for Focus Mode. ⁸ ⁹

---

## 🧪 Example responses (canonical)

> [!NOTE]
> These examples are intentionally **deterministic** (stable IDs, stable ordering) to support contract tests and hashing-based diffs (see run manifest concepts). ¹⁴

### ✅ Naming convention (recommended)

`<httpStatus>.<status>.<topic>.<variant>.json`

Examples:

- `200.ok.map-context.answer.json`
- `200.ok.realtime.usgs.answer.json`
- `200.ok.pulse-thread.draft.json`
- `200.ok.redacted.sensitive-location.json`
- `200.refused.no-evidence.json`
- `422.error.validation.json`

---

<details>
<summary><strong>✅ Example 1 — 200 OK (Map-context explanatory answer)</strong></summary>

```json
{
  "api_version": "v1",
  "kind": "kfm.focus.response",
  "request_id": "req_0001",
  "focus_id": "focus_0001",
  "created_at": "2026-01-24T18:07:12Z",
  "status": "ok",
  "input": {
    "query": "What does the drought index layer show in this view?",
    "context": {
      "map": {
        "bbox": [-97.0, 38.0, -95.0, 39.0],
        "zoom": 8,
        "active_layers": ["layer:drought_index:1934"],
        "selected_features": []
      },
      "time": { "start": "1934-01-01", "end": "1934-12-31" }
    },
    "options": {
      "include_audit": true,
      "include_suggestions": true,
      "locale": "en-US"
    }
  },
  "output": {
    "answer": {
      "format": "markdown",
      "blocks": [
        {
          "kind": "fact",
          "md": "This layer visualizes drought severity for 1934 using the dataset’s categorical index (D0–D4).[^1] In this view, darker areas represent the highest severity category in that index.[^1]",
          "citation_ids": ["cit_001"]
        },
        {
          "kind": "analysis",
          "md": "If you compare counties, consider whether the layer is clipped or interpolated at boundaries and pair it with a population/exposure layer.[^2]",
          "citation_ids": ["cit_002"],
          "confidence": 0.62
        }
      ],
      "short_answer": "It’s a categorical drought-severity index for 1934 (D0–D4), with darker areas indicating higher severity.[^1]"
    },
    "citations": [
      {
        "id": "cit_001",
        "label": "[^1]",
        "kind": "dcat_dataset",
        "title": "KFM Catalog: Drought Index (1934)",
        "ref": {
          "dcat_dataset_id": "dcat:ks:drought-index:1934:v1",
          "stac_collection_id": "stac:ks:drought-index:1934",
          "prov_activity_id": "prov:activity:ingest_drought_1934_v1"
        },
        "locator": {
          "type": "kfm://catalog",
          "uri": "kfm://catalog/datasets/dcat:ks:drought-index:1934:v1"
        }
      },
      {
        "id": "cit_002",
        "label": "[^2]",
        "kind": "doc",
        "title": "KFM Method Note: Index categories and interpolation",
        "ref": { "doc_id": "doc:method:drought-index:notes:v1" },
        "locator": {
          "type": "kfm://docs",
          "uri": "kfm://docs/doc:method:drought-index:notes:v1#methods"
        }
      }
    ],
    "entities": {
      "datasets": [
        { "graph_id": "dataset:dcat:ks:drought-index:1934:v1", "label": "Drought Index (1934)" }
      ],
      "places": [
        { "graph_id": "place:ks:region:focus_bbox", "label": "Current map view", "bbox": [-97.0, 38.0, -95.0, 39.0] }
      ],
      "concepts_in_focus": [
        { "graph_id": "concept:drought", "label": "Drought", "weight": 0.87 },
        { "graph_id": "concept:climate-variability", "label": "Climate variability", "weight": 0.41 }
      ]
    },
    "suggestions": {
      "next_questions": [
        "Show drought severity trend from 1930–1939 for the same view",
        "Overlay population density to compare exposure vs severity"
      ],
      "ui_actions": [
        {
          "type": "layer.provenance.open",
          "label": "Open provenance for drought layer",
          "payload": { "layer_id": "layer:drought_index:1934" }
        }
      ],
      "recommended_story_nodes": []
    },
    "audit": {
      "top_factors": [
        { "type": "map_layer", "id": "layer:drought_index:1934", "weight": 0.58 },
        { "type": "time_range", "start": "1934-01-01", "end": "1934-12-31", "weight": 0.22 },
        { "type": "bbox", "bbox": [-97.0, 38.0, -95.0, 39.0], "weight": 0.20 }
      ],
      "retrieval": {
        "graph_queries": 1,
        "document_hits": 2,
        "dataset_refs": ["dcat:ks:drought-index:1934:v1"]
      },
      "qa": {
        "citation_coverage": 1.0,
        "policy": { "opa_output_check": "pass" }
      }
    }
  },
  "governance": {
    "classification": "public",
    "policy_pack": { "engine": "opa", "version": "policy-pack:v1" },
    "checks": [
      { "id": "OPA_OUTPUT_CITATION_CHECK", "result": "pass" },
      { "id": "SENSITIVE_LOCATION_CHECK", "result": "pass" }
    ],
    "ledger": {
      "entry_id": "ledger:focus:2026-01-24:req_0001",
      "run_manifest_digest": "sha256:0000000000000000000000000000000000000000000000000000000000000001"
    }
  },
  "provenance": {
    "prov_bundle_id": "prov:bundle:focus:req_0001",
    "activity": {
      "prov_activity_id": "prov:activity:focus:req_0001",
      "prov_agent_id": "prov:agent:focus-mode:v1"
    },
    "wasDerivedFrom": [
      "prov:entity:dcat:ks:drought-index:1934:v1",
      "prov:entity:doc:method:drought-index:notes:v1"
    ]
  },
  "warnings": []
}
```

</details>

---

<details>
<summary><strong>✅ Example 2 — 200 OK (Real-time sensor query: Kansas River at Topeka)</strong></summary>

```json
{
  "api_version": "v1",
  "kind": "kfm.focus.response",
  "request_id": "req_0002",
  "focus_id": "focus_0002",
  "created_at": "2026-01-24T18:09:40Z",
  "status": "ok",
  "input": {
    "query": "What's the current water level of the Kansas River at Topeka?",
    "context": {
      "map": { "bbox": [-95.8, 38.9, -95.5, 39.1], "zoom": 10, "active_layers": [], "selected_features": [] }
    },
    "options": { "include_audit": true, "include_suggestions": true, "units": "imperial" }
  },
  "output": {
    "answer": {
      "format": "markdown",
      "blocks": [
        {
          "kind": "fact",
          "md": "Latest available reading for **Kansas River (Topeka gauge)**: **8.42 ft** at **2026-01-24T18:08:55Z**.[^1] This value is flagged as **provisional** (real-time feed).[^1]",
          "citation_ids": ["cit_001"]
        },
        {
          "kind": "analysis",
          "md": "If you need context, compare this reading against the station’s recent trend window (e.g., last 7 days) before drawing conclusions.[^2]",
          "citation_ids": ["cit_002"],
          "confidence": 0.70
        }
      ],
      "short_answer": "8.42 ft at 2026-01-24T18:08:55Z (provisional real-time reading).[^1]"
    },
    "data_points": [
      {
        "kind": "measurement",
        "station_id": "station:usgs:topeka",
        "observed_at": "2026-01-24T18:08:55Z",
        "value": 8.42,
        "unit": "ft",
        "quality": "provisional"
      }
    ],
    "citations": [
      {
        "id": "cit_001",
        "label": "[^1]",
        "kind": "dcat_dataset",
        "title": "KFM Catalog: USGS real-time water levels (station feed)",
        "ref": {
          "dcat_dataset_id": "dcat:usgs:nwis:realtime-water:v1",
          "prov_activity_id": "prov:activity:realtime_query:req_0002"
        },
        "locator": {
          "type": "kfm://catalog",
          "uri": "kfm://catalog/datasets/dcat:usgs:nwis:realtime-water:v1"
        }
      },
      {
        "id": "cit_002",
        "label": "[^2]",
        "kind": "doc",
        "title": "KFM Guidance: interpreting real-time sensor values",
        "ref": { "doc_id": "doc:guidance:realtime-sensors:v1" },
        "locator": { "type": "kfm://docs", "uri": "kfm://docs/doc:guidance:realtime-sensors:v1" }
      }
    ],
    "entities": {
      "places": [
        { "graph_id": "place:ks:river:kansas", "label": "Kansas River" },
        { "graph_id": "place:ks:city:topeka", "label": "Topeka" }
      ],
      "datasets": [
        { "graph_id": "dataset:dcat:usgs:nwis:realtime-water:v1", "label": "USGS NWIS real-time water" }
      ],
      "concepts_in_focus": [
        { "graph_id": "concept:hydrology", "label": "Hydrology", "weight": 0.78 }
      ]
    },
    "suggestions": {
      "next_questions": [
        "Show the last 7 days of readings for the same station",
        "Overlay floodplain or historical flood events for this area"
      ],
      "ui_actions": [
        {
          "type": "timeseries.open",
          "label": "Open station timeseries",
          "payload": { "station_id": "station:usgs:topeka", "window": "P7D" }
        }
      ]
    },
    "audit": {
      "top_factors": [
        { "type": "entity", "id": "station:usgs:topeka", "weight": 0.55 },
        { "type": "intent", "id": "realtime_measurement", "weight": 0.30 },
        { "type": "bbox", "bbox": [-95.8, 38.9, -95.5, 39.1], "weight": 0.15 }
      ],
      "retrieval": {
        "graph_queries": 1,
        "postgis_queries": 1,
        "dataset_refs": ["dcat:usgs:nwis:realtime-water:v1"]
      },
      "qa": {
        "citation_coverage": 1.0,
        "policy": { "opa_output_check": "pass" }
      }
    }
  },
  "governance": {
    "classification": "public",
    "policy_pack": { "engine": "opa", "version": "policy-pack:v1" },
    "checks": [
      { "id": "OPA_OUTPUT_CITATION_CHECK", "result": "pass" },
      { "id": "REALTIME_TIMESTAMP_PRESENT", "result": "pass" }
    ],
    "ledger": {
      "entry_id": "ledger:focus:2026-01-24:req_0002",
      "run_manifest_digest": "sha256:0000000000000000000000000000000000000000000000000000000000000002"
    }
  },
  "provenance": {
    "prov_bundle_id": "prov:bundle:focus:req_0002",
    "activity": {
      "prov_activity_id": "prov:activity:realtime_query:req_0002",
      "prov_agent_id": "prov:agent:focus-mode:v1"
    },
    "wasDerivedFrom": [
      "prov:entity:dcat:usgs:nwis:realtime-water:v1",
      "prov:entity:station:usgs:topeka"
    ]
  },
  "warnings": [
    { "code": "PROVISIONAL_DATA", "message": "Real-time values may be revised by the source." }
  ]
}
```

</details>

---

<details>
<summary><strong>✅ Example 3 — 200 OK (Pulse Thread draft output)</strong></summary>

```json
{
  "api_version": "v1",
  "kind": "kfm.focus.response",
  "request_id": "req_0003",
  "focus_id": "focus_0003",
  "created_at": "2026-01-24T18:12:05Z",
  "status": "ok",
  "input": {
    "query": "Draft a 3-step Pulse Thread about settlement patterns near this trail between 1850–1870.",
    "context": {
      "map": {
        "bbox": [-96.8, 38.5, -96.2, 39.0],
        "zoom": 9,
        "active_layers": ["layer:historic-trails"],
        "selected_features": ["feature:trail:001"]
      },
      "time": { "start": "1850-01-01", "end": "1870-12-31" }
    },
    "options": { "include_audit": true, "include_suggestions": true }
  },
  "output": {
    "answer": {
      "format": "markdown",
      "blocks": [
        {
          "kind": "fact",
          "md": "Here’s a **Pulse Thread draft** (3 steps) based on cataloged sources linked to this trail feature and time window.[^1][^2]",
          "citation_ids": ["cit_001", "cit_002"]
        }
      ],
      "short_answer": "Drafted a 3-step Pulse Thread with evidence-linked steps.[^1][^2]"
    },
    "pulse_thread": {
      "id": "pulse_0001",
      "title": "Trail-Adjacent Settlement Shifts (1850–1870)",
      "geo": {
        "type": "Polygon",
        "bbox": [-96.8, 38.5, -96.2, 39.0]
      },
      "steps": [
        {
          "id": "step_1",
          "kind": "fact",
          "md": "1850s: Early settlement clusters appear near reliable crossings and water access points along the trail corridor.[^1]",
          "citation_ids": ["cit_001"]
        },
        {
          "id": "step_2",
          "kind": "fact",
          "md": "1860s: Growth expands outward as land-use patterns formalize and adjacent routes connect to market towns.[^2]",
          "citation_ids": ["cit_002"]
        },
        {
          "id": "step_3",
          "kind": "analysis",
          "md": "Interpretation: the shift may reflect combined pull of transportation connectivity and resource constraints; validate by overlaying land claims + census distributions.[^1][^2]",
          "citation_ids": ["cit_001", "cit_002"],
          "confidence": 0.58
        }
      ]
    },
    "citations": [
      {
        "id": "cit_001",
        "label": "[^1]",
        "kind": "stac_collection",
        "title": "KFM STAC: Historic trails corridor assets",
        "ref": {
          "stac_collection_id": "stac:ks:historic-trails:v1",
          "prov_activity_id": "prov:activity:ingest_trails_v1"
        },
        "locator": { "type": "kfm://stac", "uri": "kfm://stac/collections/stac:ks:historic-trails:v1" }
      },
      {
        "id": "cit_002",
        "label": "[^2]",
        "kind": "doc",
        "title": "Story Node: Settlement & corridors (curated narrative)",
        "ref": { "story_node_id": "story:settlement-corridors:v3" },
        "locator": { "type": "kfm://story", "uri": "kfm://story/story:settlement-corridors:v3" }
      }
    ],
    "entities": {
      "places": [
        { "graph_id": "place:ks:trail:001", "label": "Selected trail feature" }
      ],
      "concepts_in_focus": [
        { "graph_id": "concept:settlement", "label": "Settlement", "weight": 0.74 },
        { "graph_id": "concept:transportation", "label": "Transportation networks", "weight": 0.52 }
      ]
    },
    "suggestions": {
      "ui_actions": [
        {
          "type": "pulse_thread.save_draft",
          "label": "Save as draft Pulse Thread",
          "payload": { "pulse_id": "pulse_0001" }
        },
        {
          "type": "overlay.add",
          "label": "Overlay land-claims layer",
          "payload": { "layer_id": "layer:land-claims:1850-1870" }
        }
      ],
      "recommended_story_nodes": ["story:settlement-corridors:v3"]
    },
    "audit": {
      "top_factors": [
        { "type": "selected_feature", "id": "feature:trail:001", "weight": 0.50 },
        { "type": "time_range", "start": "1850-01-01", "end": "1870-12-31", "weight": 0.30 },
        { "type": "layer", "id": "layer:historic-trails", "weight": 0.20 }
      ],
      "retrieval": { "graph_queries": 2, "document_hits": 1, "dataset_refs": ["stac:ks:historic-trails:v1"] },
      "qa": { "citation_coverage": 1.0, "policy": { "opa_output_check": "pass" } }
    }
  },
  "governance": {
    "classification": "public",
    "policy_pack": { "engine": "opa", "version": "policy-pack:v1" },
    "checks": [
      { "id": "OPA_OUTPUT_CITATION_CHECK", "result": "pass" },
      { "id": "SENSITIVE_LOCATION_CHECK", "result": "pass" }
    ],
    "ledger": {
      "entry_id": "ledger:focus:2026-01-24:req_0003",
      "run_manifest_digest": "sha256:0000000000000000000000000000000000000000000000000000000000000003"
    }
  },
  "provenance": {
    "prov_bundle_id": "prov:bundle:focus:req_0003",
    "activity": { "prov_activity_id": "prov:activity:focus:req_0003", "prov_agent_id": "prov:agent:focus-mode:v1" },
    "wasDerivedFrom": [
      "prov:entity:stac:ks:historic-trails:v1",
      "prov:entity:story:settlement-corridors:v3"
    ]
  },
  "warnings": [
    { "code": "DRAFT_CONTENT", "message": "Pulse Threads are drafts until reviewed/published." }
  ]
}
```

</details>

---

<details>
<summary><strong>✅ Example 4 — 200 OK (Redacted output: culturally sensitive location)</strong></summary>

```json
{
  "api_version": "v1",
  "kind": "kfm.focus.response",
  "request_id": "req_0004",
  "focus_id": "focus_0004",
  "created_at": "2026-01-24T18:14:22Z",
  "status": "ok",
  "input": {
    "query": "Give me the exact coordinates of the sacred site referenced in this story node.",
    "context": { "story_node_id": "story:indigenous-heritage:v2" },
    "options": { "include_audit": true, "include_suggestions": true }
  },
  "output": {
    "answer": {
      "format": "markdown",
      "blocks": [
        {
          "kind": "fact",
          "md": "I can’t provide exact coordinates for this location because it is classified as **culturally sensitive**. I can share a generalized area and the evidence trail for review.[^1]",
          "citation_ids": ["cit_001"]
        }
      ],
      "short_answer": "Exact coordinates are withheld due to culturally sensitive classification; providing generalized area instead.[^1]"
    },
    "redacted_geometry": {
      "type": "Polygon",
      "bbox": [-96.5, 39.0, -96.1, 39.3],
      "resolution": "generalized-area"
    },
    "citations": [
      {
        "id": "cit_001",
        "label": "[^1]",
        "kind": "story_node",
        "title": "Story Node: Indigenous heritage (restricted details)",
        "ref": { "story_node_id": "story:indigenous-heritage:v2" },
        "locator": { "type": "kfm://story", "uri": "kfm://story/story:indigenous-heritage:v2" }
      }
    ],
    "suggestions": {
      "next_questions": [
        "Show the governance metadata and access requirements for this story node",
        "Request review workflow for sensitive location access (if applicable)"
      ],
      "ui_actions": [
        { "type": "governance.panel.open", "label": "Open governance panel", "payload": { "story_node_id": "story:indigenous-heritage:v2" } }
      ]
    },
    "audit": {
      "top_factors": [
        { "type": "classification", "id": "culturally_sensitive", "weight": 0.70 },
        { "type": "policy", "id": "SENSITIVE_LOCATION_CHECK", "weight": 0.30 }
      ],
      "retrieval": { "graph_queries": 1, "document_hits": 1 },
      "qa": { "citation_coverage": 1.0, "policy": { "opa_output_check": "pass_with_redaction" } }
    }
  },
  "governance": {
    "classification": "restricted",
    "policy_pack": { "engine": "opa", "version": "policy-pack:v1" },
    "checks": [
      { "id": "SENSITIVE_LOCATION_CHECK", "result": "redact", "details": "Coordinates generalized" },
      { "id": "OPA_OUTPUT_CITATION_CHECK", "result": "pass" }
    ],
    "redactions": [
      {
        "kind": "coordinate_generalization",
        "reason": "culturally_sensitive",
        "from": { "type": "Point" },
        "to": { "type": "Polygon", "bbox": [-96.5, 39.0, -96.1, 39.3] }
      }
    ],
    "ledger": {
      "entry_id": "ledger:focus:2026-01-24:req_0004",
      "run_manifest_digest": "sha256:0000000000000000000000000000000000000000000000000000000000000004"
    }
  },
  "provenance": {
    "prov_bundle_id": "prov:bundle:focus:req_0004",
    "activity": { "prov_activity_id": "prov:activity:focus:req_0004", "prov_agent_id": "prov:agent:focus-mode:v1" },
    "wasDerivedFrom": ["prov:entity:story:indigenous-heritage:v2"]
  },
  "warnings": [
    { "code": "REDACTED", "message": "Sensitive location details were generalized." }
  ]
}
```

</details>

---

<details>
<summary><strong>🚫 Example 5 — 200 REFUSED (No evidence / no citations)</strong></summary>

```json
{
  "api_version": "v1",
  "kind": "kfm.focus.response",
  "request_id": "req_0005",
  "focus_id": "focus_0005",
  "created_at": "2026-01-24T18:16:03Z",
  "status": "refused",
  "input": {
    "query": "What happened at this exact address yesterday?",
    "context": { "map": { "bbox": [-95.7, 39.0, -95.6, 39.1], "zoom": 16 } },
    "options": { "include_audit": true, "include_suggestions": true }
  },
  "output": {
    "refusal": {
      "code": "NO_EVIDENCE",
      "message": "I can’t answer that from KFM’s cataloged sources (no supporting evidence was found for the requested claim).",
      "safe_next_steps": [
        "Broaden the time window or switch to a dataset/event layer you have loaded",
        "Ingest a relevant dataset (with STAC/DCAT/PROV) before asking for specifics",
        "Ask for related known events/entities (county, incident type, time range) instead of a single address"
      ]
    },
    "citations": []
  },
  "governance": {
    "classification": "public",
    "policy_pack": { "engine": "opa", "version": "policy-pack:v1" },
    "checks": [
      { "id": "OPA_OUTPUT_CITATION_CHECK", "result": "fail", "details": "No citations available; refusing." }
    ],
    "ledger": {
      "entry_id": "ledger:focus:2026-01-24:req_0005",
      "run_manifest_digest": "sha256:0000000000000000000000000000000000000000000000000000000000000005"
    }
  },
  "provenance": {
    "prov_bundle_id": "prov:bundle:focus:req_0005",
    "activity": { "prov_activity_id": "prov:activity:focus:req_0005", "prov_agent_id": "prov:agent:focus-mode:v1" },
    "wasDerivedFrom": []
  },
  "warnings": [
    { "code": "NO_CITATIONS", "message": "No evidence was retrieved; response refused." }
  ]
}
```

</details>

---

<details>
<summary><strong>⚠️ Example 6 — 422 ERROR (Validation)</strong></summary>

```json
{
  "api_version": "v1",
  "kind": "kfm.focus.response",
  "request_id": "req_0006",
  "created_at": "2026-01-24T18:18:41Z",
  "status": "error",
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request: `query` must be a non-empty string.",
    "fields": [{ "path": "input.query", "issue": "required" }]
  }
}
```

</details>

---

## ✅ Contract-test expectations

### Hard requirements (v1)

- ✅ **Citations required for factual answers**; otherwise `status=refused`. ³ ¹ ¹²
- ✅ **No autonomous actions**: only `suggestions.ui_actions[]` (advisory). ¹
- ✅ **Fact vs analysis separation** via `answer.blocks[].kind`. ⁴
- ✅ **Policy gating recorded** in `governance.checks[]` and `governance.redactions[]`. ¹⁰
- ✅ **Traceability** via `provenance.wasDerivedFrom[]` / PROV bundle IDs. ⁷
- ✅ **Audit panel payload** present when requested (`include_audit=true`). ⁸

### Stability requirements for examples

- Stable ordering of arrays where possible
- Deterministic IDs (no random UUIDs in examples)
- Deterministic timestamps in tests (or snapshot them)
- JSON should be canonicalizable (for hashing & diff review) ¹⁴

---

## 🧩 Source map (all project files)

> [!NOTE]
> Some supporting PDFs are packaged as **PDF Portfolios** and may require Acrobat to extract embedded documents before they can be fully indexed in search tooling. ¹⁵ ¹⁶ ¹⁷ ¹⁸ ¹⁹

| 📄 Project file | How it shaped this README / contract examples |
|---|---|
| `MARKDOWN_GUIDE_v13.md.gdoc` | Contract-first workflow; Story Node + Focus Mode integration; fact vs interpretation separation; contributors must add redaction rules when data is sensitive. ² ⁴ ⁵ |
| `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf` | Focus Mode is advisory-only; citations required; avoid speculation beyond KFM data; generalize/refuse sensitive locations; “no mystery layers.” ¹ ²⁰ ²¹ |
| `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf` | Open standards emphasis (STAC/DCAT/PROV); policy engine with OPA guardrails against unsafe outputs/prompt injection. ²² ²³ |
| `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf` | Focus Mode pipeline: retrieve evidence → generate answer → runtime policy check for citations → AnswerWithCitations; drift/monitoring concepts. ³ |
| `Kansas Frontier Matrix – Comprehensive UI System Overview.pdf` | Audit Panel concept (factors + citations + governance flags); API integration (REST/GraphQL) and decoupling. ⁸ ⁹ |
| `📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf` | Evidence triplet + catalog-driven publishing; PROV semantics; governance from day zero; fail-closed; API as governed gate. ⁶ ⁷ ¹⁰ ¹¹ |
| `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf` | Policy Pack direction; PROV integration with PRs/CI; governance invariants. ¹³ ²⁴ |
| `Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf` | AI-driven exploration + storytelling ideas (kept human-in-the-loop and evidence-first). ²⁵ |
| `Additional Project Ideas.pdf` | Pulse Threads + conceptual attention nodes; `run_manifest.json` idea for reproducible governance logging + hashing. ¹⁴ ²⁶ |
| `📘 KFM Document Refinement Request_ Final Polish (Logos, Spacing, Readability).docx` | Pulse Threads / Conceptual Attention Nodes as UI + knowledge features (reinforced). ²⁷ |
| `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf` | Standard formats (GeoTIFF/GeoJSON/CSV), STAC-like JSON, map UI architecture concepts. ²⁸ |
| `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf` | Documentation discipline for reproducible, testable system building. ²⁹ |
| `Data Mining Concepts & applictions.pdf` | Data validation, query auditing, privacy methods (informing governance/QA fields). ³⁰ |
| `KFM- python-geospatial-analysis-cookbook-...pdf` | Example geospatial processing patterns (PostGIS analysis → export GeoJSON), informing `suggestions` + derived outputs. ³¹ |
| `AI Concepts & more.pdf` (PDF Portfolio) | Packaged reference material; needs portfolio extraction for indexing. ¹⁵ |
| `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf` (PDF Portfolio) | Packaged geospatial/webgl references; needs portfolio extraction for indexing. ¹⁶ |
| `Various programming langurages & resources 1.pdf` (PDF Portfolio) | Packaged programming/API references; needs portfolio extraction for indexing. ¹⁷ |
| `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf` (PDF Portfolio) | Packaged data architecture references; needs portfolio extraction for indexing. ¹⁹ |
| `Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx` | Markdown conventions & best practices (used for structuring this README). ³² |

---

## 🔗 File attachments (quick open)

Core KFM docs:
- :contentReference[oaicite:0]{index=0} `MARKDOWN_GUIDE_v13.md.gdoc`
- :contentReference[oaicite:1]{index=1} `KFM – Comprehensive Technical Documentation`
- :contentReference[oaicite:2]{index=2} `KFM Data Intake – Technical & Design Guide`
- :contentReference[oaicite:3]{index=3} `Latest Ideas & Future Proposals`

Supporting ideas / resources:
- :contentReference[oaicite:4]{index=4} `Innovative Concepts to Evolve KFM`
- :contentReference[oaicite:5]{index=5} `Additional Project Ideas`
- :contentReference[oaicite:6]{index=6} `Document Refinement Request`
- :contentReference[oaicite:7]{index=7} `Open-Source Geospatial Mapping Hub Design`
- :contentReference[oaicite:8]{index=8} `Scientific Method / Master Coder Protocol`
- :contentReference[oaicite:9]{index=9} `Data Mining Concepts & applications`
- :contentReference[oaicite:10]{index=10} `Python Geospatial Analysis Cookbook`

Portfolio PDFs (manual extraction recommended):
- :contentReference[oaicite:11]{index=11} `AI Concepts & more (PDF Portfolio)`
- :contentReference[oaicite:12]{index=12} `Maps/GoogleMaps/WebGL (PDF Portfolio)`
- :contentReference[oaicite:13]{index=13} `Various programming languages & resources (PDF Portfolio)`
- :contentReference[oaicite:14]{index=14} `Data Management / Bayesian Methods (PDF Portfolio)`

---

## Footnotes / evidence links (project grounding)

1. Focus Mode advisory-only + citations required + avoid speculation + generalize/refuse sensitive location leaks. :contentReference[oaicite:15]{index=15}
2. “Contract-first” + provenance-first requirements for UI layers and API endpoints. :contentReference[oaicite:16]{index=16}
3. Runtime policy check / OPA citation gate; refusal if no citations. :contentReference[oaicite:17]{index=17}
4. Story Nodes require provenance for claims, graph entity references, and fact vs interpretation separation (feeds Focus Mode). :contentReference[oaicite:18]{index=18}
5. Contract-first triggers strict versioning/compatibility checks. :contentReference[oaicite:19]{index=19}
6. Evidence triplet + graph ingestion + governed API layer; UI does not bypass API. :contentReference[oaicite:20]{index=20}
7. PROV semantics (entities/activities/agents + derivation relationships). :contentReference[oaicite:21]{index=21}
8. Audit Panel concept (transparency: factors + citations + governance flags). :contentReference[oaicite:22]{index=22}
9. API integration (REST/GraphQL decoupling). :contentReference[oaicite:23]{index=23}
10. Fail-closed posture + OPA/Policy Pack enforcement. :contentReference[oaicite:24]{index=24}
11. Governance from day zero + FAIR/CARE is an engineering constraint; evidence triplet required. :contentReference[oaicite:25]{index=25}:contentReference[oaicite:26]{index=26}
12. Focus Mode “hard gate” rules (citations or refuse; no sensitive leaks; trust-preserving constraints). :contentReference[oaicite:27]{index=27}
13. PR→PROV graph integration for end-to-end provenance (devops + data lineage). :contentReference[oaicite:28]{index=28}
14. `run_manifest.json` concept + canonicalization/hashing for governance/audit trails. :contentReference[oaicite:29]{index=29}
15. `AI Concepts & more.pdf` is a PDF Portfolio requiring Acrobat to open/extract. :contentReference[oaicite:30]{index=30}
16. `Maps-...-Geospatial-webgl.pdf` is a PDF Portfolio requiring Acrobat to open/extract. :contentReference[oaicite:31]{index=31}
17. `Various programming languages & resources 1.pdf` is a PDF Portfolio requiring Acrobat to open/extract. :contentReference[oaicite:32]{index=32}
18. `Data Managment-...` is a PDF Portfolio requiring Acrobat to open/extract. :contentReference[oaicite:33]{index=33}
19. Same portfolio note (data management). :contentReference[oaicite:34]{index=34}
20. Contract-first metadata + “no mystery layers” + citations in Focus Mode from provenance metadata. :contentReference[oaicite:35]{index=35}
21. Provenance-first principle for UI/Focus Mode; open standards for interchange/lineage. :contentReference[oaicite:36]{index=36}
22. STAC/DCAT/PROV-O emphasis in architecture. :contentReference[oaicite:37]{index=37}
23. OPA policy engine guardrails (prompt injection / unsafe outputs). :contentReference[oaicite:38]{index=38}
24. Policy Pack direction (OPA/Rego + Conftest). :contentReference[oaicite:39]{index=39}
25. Innovative concepts: AI-driven exploration/storytelling with trust/traceability emphasis. :contentReference[oaicite:40]{index=40}
26. Pulse Threads / conceptual attention nodes as narrative+graph features. :contentReference[oaicite:41]{index=41}
27. Pulse Threads + conceptual attention nodes reinforcement. :contentReference[oaicite:42]{index=42}
28. Standard formats + STAC-like JSON + mapping hub architecture. :contentReference[oaicite:43]{index=43}
29. Master Coder Protocol: disciplined, reproducible system building approach. :contentReference[oaicite:44]{index=44}
30. Data validation, query auditing, privacy methods. 
31. PostGIS analysis → export GeoJSON (example geospatial processing pattern). :contentReference[oaicite:46]{index=46}
32. Markdown syntax/best-practices doc. :contentReference[oaicite:47]{index=47}

