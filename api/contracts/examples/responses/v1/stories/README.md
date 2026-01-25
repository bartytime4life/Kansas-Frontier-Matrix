# 🧭📖 Stories API — Example Responses (v1)

![API](https://img.shields.io/badge/API-v1-blue)
![Contract First](https://img.shields.io/badge/contract--first-✅-brightgreen)
![Evidence First](https://img.shields.io/badge/evidence--first-🔎-purple)
![Formats](https://img.shields.io/badge/formats-JSON%20%7C%20Markdown%20%7C%20YAML-orange)
![Provenance](https://img.shields.io/badge/metadata-STAC%20%2B%20DCAT%20%2B%20PROV-9cf)

This folder contains **canonical response examples** for the **Stories API (v1)**—covering both:

- **🧩 Story Nodes**: interactive narrative “tours” driven by **Markdown + JSON step config** (map + timeline sync).
- **💓 Pulse Threads**: short, timely, geotagged updates that behave like a hybrid of **Story Nodes + feed items**.

> [!NOTE]
> These examples are meant to be **stable contract artifacts** (used for documentation, fixtures, and contract tests).  
> Prefer **additive changes** only. Breaking changes require a **new API version** folder (e.g., `v2/`).

---

## 🧭 Quick Links

- **Endpoints covered**: [Endpoints](#-endpoints-covered)
- **Response envelope**: [Common JSON Envelope](#-common-json-envelope)
- **Examples**: [Examples](#-examples)
- **Governance & Evidence**: [Evidence Provenance Rules](#-evidence--provenance-rules)
- **Extensibility**: [Extensions](#-extensions--future-proofing)

---

## 📁 Folder Intent

```text
📁 api/contracts/examples/responses/v1/stories/
└── ✅ README.md   (this file)
```

> [!TIP]
> If you add standalone JSON examples in this directory later, keep names obvious and greppable.
> A practical pattern is:
> - `200.list.json`
> - `200.get.story_node.json`
> - `200.get.pulse_thread.json`
> - `403.get.forbidden.json`
> - `404.get.not_found.json`
> - `422.validation_error.json`

---

## 🧱 Endpoints Covered

These examples assume a REST base path like:

- `GET /api/v1/stories`
- `GET /api/v1/stories/{storyId}`

Optionally (implementation dependent), story assets may be exposed via:
- `GET /api/v1/stories/{storyId}/content` (Markdown)
- `GET /api/v1/stories/{storyId}/config` (JSON step script)
- `GET /api/v1/stories/{storyId}/evidence` (Evidence manifest / citations)
- `GET /api/v1/stories/{storyId}/prov` (PROV JSON-LD)

---

## 📦 Common JSON Envelope

All v1 story responses should follow a consistent envelope:

```json
{
  "meta": {
    "apiVersion": "v1",
    "schema": "kfm.api.responses.v1.stories.<kind>",
    "requestId": "req_01J... (opaque)",
    "generatedAt": "2026-01-24T18:31:12Z"
  },
  "data": {},
  "links": {
    "self": "/api/v1/stories"
  }
}
```

### ✨ Conventions

- **camelCase JSON** to match UI/TS clients.
- `schema` is a stable identifier that maps to JSON Schemas in `api/contracts/...` (where applicable).
- `requestId` is always included to support tracing.

---

## 🧩 Story Types

### 🧩 Story Node (`storyType: "story_node"`)

A Story Node represents a guided narrative experience. It typically has:

- **Markdown narrative content**
- A **JSON “script”** that defines step-by-step:
  - `mapState` (center/zoom/layers)
  - `timelineYear` (or time range)
  - links from `textId` → Markdown section IDs

### 💓 Pulse Thread (`storyType: "pulse_thread"`)

Pulse Threads are:

- Short, location-specific narrative updates
- Tied into the knowledge graph with provenance + evidence
- Discoverable via map interactions and/or a feed

---

## 🧪 Examples

### 1) ✅ 200 — List Stories

<details>
<summary><strong>GET /api/v1/stories</strong> — example response</summary>

```json
{
  "meta": {
    "apiVersion": "v1",
    "schema": "kfm.api.responses.v1.stories.list",
    "requestId": "req_01J2KFMSTORIESLIST9A7C2",
    "generatedAt": "2026-01-24T18:31:12Z"
  },
  "data": [
    {
      "id": "story.ks.prairie-fires-1850s",
      "storyType": "story_node",
      "slug": "prairie-fires-1850s",
      "title": "Prairie Fires of the 1850s",
      "summary": "A guided tour of land cover context and historic fire frequency patterns.",
      "status": "published",
      "tags": ["wildfire", "landcover", "history"],
      "timeRange": { "start": "1850-01-01", "end": "1859-12-31" },
      "bbox": [-102.0517, 36.9930, -94.5884, 40.0032],
      "updatedAt": "2026-01-10T09:30:00Z",
      "links": {
        "self": "/api/v1/stories/story.ks.prairie-fires-1850s"
      }
    },
    {
      "id": "pulse.ks.streamflows-low-2026-01-20",
      "storyType": "pulse_thread",
      "slug": "streamflows-low-2026-01-20",
      "title": "Early drought signal: multiple Kansas stream gauges below the 10th percentile",
      "summary": "A rapid pulse thread tying streamflow anomalies to regional hydrologic units.",
      "status": "published",
      "tags": ["hydrology", "drought", "sensors", "pulse"],
      "pulse": {
        "timestamp": "2026-01-20T15:05:00Z",
        "category": "hydrology",
        "urgency": "watch"
      },
      "bbox": [-101.2, 37.0, -94.6, 40.0],
      "updatedAt": "2026-01-20T15:25:00Z",
      "links": {
        "self": "/api/v1/stories/pulse.ks.streamflows-low-2026-01-20"
      }
    }
  ],
  "pagination": {
    "limit": 20,
    "offset": 0,
    "total": 2
  },
  "links": {
    "self": "/api/v1/stories?limit=20&offset=0"
  }
}
```

</details>

---

### 2) ✅ 200 — Get Story Node (Detail)

<details>
<summary><strong>GET /api/v1/stories/story.ks.prairie-fires-1850s</strong> — example response</summary>

```json
{
  "meta": {
    "apiVersion": "v1",
    "schema": "kfm.api.responses.v1.stories.get",
    "requestId": "req_01J2KFMSTORIESGETS0METH1NG",
    "generatedAt": "2026-01-24T18:32:01Z"
  },
  "data": {
    "id": "story.ks.prairie-fires-1850s",
    "storyType": "story_node",
    "slug": "prairie-fires-1850s",
    "title": "Prairie Fires of the 1850s",
    "status": "published",

    "authors": [
      { "id": "agent:kfm:maintainer:0001", "name": "KFM Maintainers", "role": "editor" }
    ],

    "tags": ["wildfire", "landcover", "history"],
    "themes": ["environment", "historical-change"],
    "timeRange": { "start": "1850-01-01", "end": "1859-12-31" },
    "bbox": [-102.0517, 36.9930, -94.5884, 40.0032],

    "content": {
      "format": "markdown",
      "textEncoding": "utf-8",
      "sha256": "b7c4d7f0f5e8d3f0a8b2f6c0a9d0c6d4e7f1b2c3d4e5f6a7b8c9d0e1f2a3b4c5",
      "text": "# Prairie Fires of the 1850s\n\n## intro\nKansas in the 1850s featured broad prairie landscapes...\n\n## fire_map\nHistoric fire frequency layers reveal...\n"
    },

    "steps": [
      {
        "id": 1,
        "textId": "intro",
        "mapState": {
          "center": [-98.0, 38.5],
          "zoom": 6,
          "layers": ["1850_landcover"]
        },
        "timelineYear": 1850,
        "citations": ["E-001", "E-002"]
      },
      {
        "id": 2,
        "textId": "fire_map",
        "mapState": {
          "center": [-98.0, 38.5],
          "zoom": 6,
          "layers": ["1850_landcover", "fire_frequency"]
        },
        "timelineYear": 1855,
        "citations": ["E-002", "E-003"]
      }
    ],

    "evidence": {
      "evidenceManifest": {
        "id": "EM-84",
        "format": "yaml",
        "href": "/api/v1/stories/story.ks.prairie-fires-1850s/evidence",
        "sha256": "0f2a1b... (example)"
      },
      "citations": [
        {
          "id": "E-001",
          "kind": "dataset",
          "label": "Land cover reconstruction (1850)",
          "ref": { "datasetId": "kfm.ks.landcover.1850" },
          "howUsed": "Basemap/context layer for step 1"
        },
        {
          "id": "E-002",
          "kind": "dataset",
          "label": "Historic fire frequency surface",
          "ref": { "datasetId": "kfm.ks.fire.frequency.v1" },
          "howUsed": "Overlay layer for step 2"
        },
        {
          "id": "E-003",
          "kind": "document",
          "label": "Historic accounts of prairie burning (excerpted)",
          "ref": { "docId": "kfm.docs.prairie-fire-accounts.1850s" },
          "howUsed": "Narrative support for interpretation in step 2"
        }
      ],
      "prov": {
        "format": "jsonld",
        "href": "/api/v1/stories/story.ks.prairie-fires-1850s/prov",
        "sha256": "9ab3cc... (example)"
      }
    },

    "graphRefs": {
      "places": ["place:ks:statewide"],
      "datasets": ["kfm.ks.landcover.1850", "kfm.ks.fire.frequency.v1"],
      "concepts": ["concept:wildfire", "concept:grassland"],
      "events": []
    },

    "governance": {
      "classification": "public",
      "license": "CC-BY-4.0",
      "aiAssisted": {
        "enabled": false,
        "note": "No AI-generated narrative text in this story."
      }
    },

    "revision": {
      "version": 3,
      "etag": "W/\"story.ks.prairie-fires-1850s:v3\"",
      "updatedAt": "2026-01-10T09:30:00Z"
    },

    "links": {
      "self": "/api/v1/stories/story.ks.prairie-fires-1850s",
      "content": "/api/v1/stories/story.ks.prairie-fires-1850s/content",
      "config": "/api/v1/stories/story.ks.prairie-fires-1850s/config",
      "evidence": "/api/v1/stories/story.ks.prairie-fires-1850s/evidence",
      "prov": "/api/v1/stories/story.ks.prairie-fires-1850s/prov"
    }
  }
}
```

</details>

---

### 3) ✅ 200 — Get Pulse Thread (Detail)

<details>
<summary><strong>GET /api/v1/stories/pulse.ks.streamflows-low-2026-01-20</strong> — example response</summary>

```json
{
  "meta": {
    "apiVersion": "v1",
    "schema": "kfm.api.responses.v1.stories.get",
    "requestId": "req_01J2KFMSTORIESPULSE9X0",
    "generatedAt": "2026-01-24T18:33:10Z"
  },
  "data": {
    "id": "pulse.ks.streamflows-low-2026-01-20",
    "storyType": "pulse_thread",
    "slug": "streamflows-low-2026-01-20",
    "title": "Early drought signal: multiple Kansas stream gauges below the 10th percentile",
    "status": "published",
    "tags": ["hydrology", "drought", "pulse"],

    "pulse": {
      "timestamp": "2026-01-20T15:05:00Z",
      "category": "hydrology",
      "urgency": "watch",
      "body": "Several stream gauges show 7-day flows in the lowest 10th percentile of historic range.",
      "whyItMatters": "Low-flow clustering can precede broader drought impacts and water-use restrictions.",
      "suggestedActions": [
        "Validate sensor integrity at flagged stations",
        "Cross-check with drought monitor indicators",
        "Notify watershed stakeholders if trend persists"
      ]
    },

    "geo": {
      "bbox": [-101.2, 37.0, -94.6, 40.0],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [-101.2, 37.0],
            [-94.6, 37.0],
            [-94.6, 40.0],
            [-101.2, 40.0],
            [-101.2, 37.0]
          ]
        ]
      }
    },

    "evidence": {
      "evidenceManifest": {
        "id": "EM-201",
        "format": "yaml",
        "href": "/api/v1/stories/pulse.ks.streamflows-low-2026-01-20/evidence"
      },
      "citations": [
        {
          "id": "E-101",
          "kind": "dataset",
          "label": "Stream gauge daily flows",
          "ref": { "datasetId": "kfm.ks.usgs.gauges.dailyflows" },
          "howUsed": "Percentile computation for anomaly detection"
        },
        {
          "id": "E-102",
          "kind": "dataset",
          "label": "Drought monitor indicators",
          "ref": { "datasetId": "kfm.us.drought.monitor.weekly" },
          "howUsed": "Contextual corroboration"
        }
      ],
      "prov": {
        "format": "jsonld",
        "href": "/api/v1/stories/pulse.ks.streamflows-low-2026-01-20/prov"
      }
    },

    "graphRefs": {
      "places": ["place:ks:watershed:example-huc8"],
      "datasets": ["kfm.ks.usgs.gauges.dailyflows", "kfm.us.drought.monitor.weekly"],
      "concepts": ["concept:drought", "concept:streamflow"],
      "events": []
    },

    "governance": {
      "classification": "public",
      "license": "CC-BY-4.0",
      "aiAssisted": {
        "enabled": true,
        "humanReviewed": true,
        "confidence": 0.72
      }
    },

    "links": {
      "self": "/api/v1/stories/pulse.ks.streamflows-low-2026-01-20",
      "evidence": "/api/v1/stories/pulse.ks.streamflows-low-2026-01-20/evidence",
      "prov": "/api/v1/stories/pulse.ks.streamflows-low-2026-01-20/prov"
    }
  }
}
```

</details>

---

### 4) ⛔ 404 — Not Found

```json
{
  "meta": {
    "apiVersion": "v1",
    "schema": "kfm.api.responses.v1.error",
    "requestId": "req_01J2KFMNOTFOUND000",
    "generatedAt": "2026-01-24T18:34:00Z"
  },
  "error": {
    "code": "not_found",
    "message": "Story not found.",
    "details": {
      "storyId": "story.ks.does-not-exist"
    }
  }
}
```

---

### 5) 🔒 403 — Forbidden / Classified

```json
{
  "meta": {
    "apiVersion": "v1",
    "schema": "kfm.api.responses.v1.error",
    "requestId": "req_01J2KFMFORBIDDEN000",
    "generatedAt": "2026-01-24T18:34:22Z"
  },
  "error": {
    "code": "forbidden",
    "message": "You do not have access to this story.",
    "details": {
      "classification": "restricted",
      "reason": "policy_denied"
    }
  }
}
```

---

### 6) ⚠️ 422 — Validation Error

```json
{
  "meta": {
    "apiVersion": "v1",
    "schema": "kfm.api.responses.v1.error",
    "requestId": "req_01J2KFMVALIDATION000",
    "generatedAt": "2026-01-24T18:34:45Z"
  },
  "error": {
    "code": "validation_error",
    "message": "Invalid request parameters.",
    "details": {
      "fields": [
        {
          "field": "limit",
          "issue": "must be an integer between 1 and 100"
        }
      ]
    }
  }
}
```

---

## 🔎 Evidence & Provenance Rules

> [!IMPORTANT]
> KFM is **evidence-first**. Stories (including pulses) should support:
> - **Evidence manifests** (machine-checkable references)
> - **PROV** links (traceable lineage)
> - Citations surfaced in UI (footnotes, “View Evidence”, etc.)

Recommended minimums:
- Every story response includes `evidence.evidenceManifest` + `evidence.citations[]`
- Every `citations[]` entry has a stable `id` and a resolvable `ref` (datasetId/docId)
- `aiAssisted.enabled === true` requires explicit disclosure fields (confidence / review flags)

---

## 🧩 Extensions & Future-proofing

To keep v1 stable while enabling growth, prefer an `extensions` object (additive only):

```json
{
  "extensions": {
    "sceneState": {
      "mode": "3d",
      "tilesets": ["kfm.tiles.lidar.demo"],
      "camera": { "heading": 120, "pitch": -35 }
    }
  }
}
```

Examples of future extensions:
- 🗺️ 3D/AR story steps
- 📡 live sensor overlays
- 🧠 concept attention nodes / narrative pattern signals
- 📦 offline “story packs” for field use

---

## 🔁 Versioning & Change Rules

✅ Allowed in v1:
- adding **optional** fields
- adding new enum values **only if client-safe**
- adding new links

⛔ Not allowed in v1:
- removing/renaming fields
- changing field meanings
- changing default behaviors that break consumers

---

## 🗺️ (Optional) Flow Sketch

```mermaid
flowchart LR
  UI[🖥️ UI Story Mode] -->|GET /api/v1/stories/{id}| API[🔌 KFM API]
  API --> FS[📁 story_nodes/ (Markdown + JSON)]
  API --> KG[🕸️ Knowledge Graph]
  API --> EV[🔎 Evidence Manifest + PROV]
  API --> UI
```

---

## 📚 Related Reading

- `docs/reports/story_nodes/` 📜 (Story content lives here)
- `api/contracts/` 🧾 (schemas & contracts)
- `docs/architecture/` 🏗️ (system overview & principles)
- `web/` 🧑‍💻 (React UI that consumes these responses)

✅ If you update this README, also ensure:
- the JSON examples stay **valid JSON**
- the examples align with **schemas** and **policy rules**
- any new fields are documented here ✍️
