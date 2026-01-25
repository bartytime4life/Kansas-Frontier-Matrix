# 📦 KFM API Response Examples (v1)

![API](https://img.shields.io/badge/API-v1-blue)
![Contracts](https://img.shields.io/badge/contract--first-✅-success)
![Provenance](https://img.shields.io/badge/provenance--first-🧾-brightgreen)
![Geo](https://img.shields.io/badge/geospatial-🗺️-informational)
![AI](https://img.shields.io/badge/AI-evidence--first-🧭🤖-purple)

> 📍 **Location:** `api/contracts/examples/responses/v1/`  
> 🎯 **Goal:** Provide **canonical, copy/pasteable** response examples for **API v1**—used for docs, mocks, and contract tests.

---

## 🧠 What lives here

This folder is the **single source of truth** for what **good responses look like** in KFM v1:

- ✅ **REST + GraphQL** responses (UI is decoupled from backend via APIs)
- ✅ **Provenance-first** objects (STAC/DCAT/PROV-linked where relevant)
- ✅ **Evidence-first** AI responses (Focus Mode / narrative citations)
- ✅ **Geo outputs** (GeoJSON + vector tiles)
- ✅ **Governance** (classification + redaction + policy decisions)

---

## 🧭 Response styles supported

KFM v1 supports two “styles” of responses depending on interoperability needs:

### A) 📦 KFM Envelope (default)
Most KFM endpoints return an envelope with predictable metadata + links + provenance.

```json
{
  "meta": {
    "api_version": "v1",
    "status": "ok",
    "request_id": "req_01J2Y8ZQ4P9H9XK0S8C3R7M6Q1",
    "generated_at": "2026-01-24T18:42:12Z",
    "warnings": [],
    "paging": null,
    "telemetry": {
      "trace_id": "trace_6b1c7c7f4d154a1f"
    },
    "governance": {
      "policy_pack": "kfm-policy@1.4.2",
      "decision": "allow",
      "redactions": []
    }
  },
  "data": {},
  "links": {},
  "provenance": {}
}
```

### B) 🧩 Spec-native responses (STAC / GeoJSON / PROV / DCAT)
When strict compatibility matters (e.g., STAC clients), responses may be returned **unwrapped** with a spec-native `Content-Type`, e.g.:

- `application/geo+json`
- `application/json` (STAC)
- `application/ld+json` (JSON-LD PROV/DCAT)

> 📝 Tip: If you need both, return spec-native under `/stac/*` or `/dcat/*`, and return **KFM Envelope** under `/api/*`.

---

## 🧱 Common fields (KFM Envelope)

### `meta` (always)
| Field | Type | Notes |
|---|---:|---|
| `api_version` | string | `"v1"` |
| `status` | `"ok" \| "error"` | Envelope state |
| `request_id` | string | Stable ID for debugging + logs |
| `generated_at` | RFC3339 string | UTC timestamp |
| `warnings` | array | Non-fatal issues (e.g., partial redaction) |
| `paging` | object\|null | Cursor pagination where applicable |
| `telemetry.trace_id` | string | OpenTelemetry-style correlation |
| `governance` | object | Policy decision + redactions |

### `links` (recommended)
Prefer stable internal paths for navigation:

```json
{
  "self": "/api/datasets/kfm.ks.landcover.1850",
  "docs": "/api/docs#/datasets/getDataset",
  "related": [
    "/api/layers/1850_landcover"
  ]
}
```

### `provenance` (when data is derived)
KFM responses should be able to answer **“Where did this come from?”**:

```json
{
  "stac": {
    "collection": "/stac/collections/kfm.ks.landcover",
    "items": "/stac/search?collections=kfm.ks.landcover&datetime=1850-01-01/1850-12-31"
  },
  "dcat": {
    "dataset": "/dcat/datasets/kfm.ks.landcover.1850"
  },
  "prov": {
    "bundle": "/prov/bundles/prov_01J2Y8VZ3B3H0N1Q4W7S8B9F2K"
  },
  "artifacts": [
    {
      "kind": "cog",
      "digest": "sha256:5c0c1b6b4b7a5c3b1e1d9c0f0a3e2d1c...",
      "signed": true
    }
  ]
}
```

---

## 🗂️ Suggested example file layout

> These filenames are **recommended** for consistency (even if not all exist yet).

```text
api/contracts/examples/responses/v1/
├─ ♻️ common/                             # Shared response examples used across many endpoints
│  ├─ ✅🧾 ok.json                         # Standard success envelope (minimal “ok” response shape)
│  ├─ 🚨🧾 error.validation.json           # Validation failure (bad request) with field-level errors
│  ├─ 🔎🚨🧾 error.not_found.json           # Not-found error (missing resource) using standard Problem Details
│  ├─ 🚫⚖️🧾 error.policy_denied.json      # Policy denial (authz/obligations) with codes + safe reasons
│  └─ 🧯🚨🧾 error.rate_limit.json          # Rate limit response (429) with retry hints and request correlation id
├─ 🗂️ datasets/                           # Dataset endpoint examples (catalog discovery)
│  └─ 🗂️🧾 get.dataset.json                # GET dataset response (metadata + distributions + provenance pointers)
├─ 🛰️ stac/                               # STAC API examples (collections/items/search)
│  ├─ 🛰️🧾 get.collection.json             # GET STAC Collection response example
│  └─ 🛰️🧾 post.search.itemcollection.json # POST /stac/search ItemCollection response (paging/context)
├─ 🗺️ layers/                             # UI layer registry examples (what the map can render)
│  └─ 🗺️🧾 get.layer.json                  # GET layer manifest response (sources, style/legend refs, bounds, time-binding)
├─ 🧱 tiles/                               # Tile endpoint examples (binary responses and headers)
│  └─ 🧱📄 get.tile.http.txt               # Raw HTTP example (headers + content-type + caching for tiles)
├─ 🔎 focus/                               # Focus Mode examples (evidence-first Q&A)
│  └─ 🔎📚🧾 post.focus.answer.json         # POST focus answer response (citations, redactions, uncertainty, receipts)
├─ 🎬 story_nodes/                         # Story Node examples (governed narratives)
│  └─ 🎬🧾 get.story_node.json             # GET story node response (markdown/config refs + evidence pointers)
├─ 🧵 pulse/                               # Pulse thread examples (short updates with evidence)
│  └─ 🧵🧾 get.threads.json                # GET pulse threads list (summaries + paging + evidence pointers)
├─ 🕸️ graph/                               # Graph query examples (place context, GraphQL responses)
│  ├─ 🗺️🕸️🧾 get.place.datasets.json        # GET place→datasets response (graph-backed context + provenance refs)
│  └─ 🧬🕸️🧾 graphql.query.response.json     # GraphQL query response example (data + errors shape)
└─ 🧳 offline/                              # Offline pack examples (bundle manifests)
   └─ 🧳🧾 get.pack.manifest.json           # GET offline pack manifest (contents index + digests + catalog/prov refs)
```

---

# ✅ Canonical response examples

## 1) 🩺 Health check (Envelope)

**GET** `/api/healthz`

```json
{
  "meta": {
    "api_version": "v1",
    "status": "ok",
    "request_id": "req_01J2Y8ZQ4P9H9XK0S8C3R7M6Q1",
    "generated_at": "2026-01-24T18:42:12Z",
    "warnings": [],
    "paging": null,
    "telemetry": { "trace_id": "trace_6b1c7c7f4d154a1f" },
    "governance": { "policy_pack": "kfm-policy@1.4.2", "decision": "allow", "redactions": [] }
  },
  "data": {
    "service": "kfm-api",
    "uptime_s": 482193,
    "dependencies": {
      "postgis": "ok",
      "neo4j": "ok",
      "object_storage": "ok"
    }
  },
  "links": { "self": "/api/healthz" },
  "provenance": {}
}
```

---

## 2) 🧾 Dataset metadata (Envelope linking STAC/DCAT/PROV)

**GET** `/api/datasets/kfm.ks.landcover.1850`

```json
{
  "meta": {
    "api_version": "v1",
    "status": "ok",
    "request_id": "req_01J2Y90G5E5S9T2Y4D6V3H1X0K",
    "generated_at": "2026-01-24T18:45:50Z",
    "warnings": [],
    "paging": null,
    "telemetry": { "trace_id": "trace_2d7e0b40df2c4e7d" },
    "governance": { "policy_pack": "kfm-policy@1.4.2", "decision": "allow", "redactions": [] }
  },
  "data": {
    "dataset_id": "kfm.ks.landcover.1850",
    "title": "Kansas Landcover (1850 snapshot)",
    "summary": "Derived historical landcover reconstruction aligned to 1850 context for narrative + map exploration.",
    "spatial": {
      "crs": "EPSG:4326",
      "bbox": [-102.051, 36.993, -94.588, 40.003]
    },
    "temporal": {
      "start": "1850-01-01",
      "end": "1850-12-31"
    },
    "license": {
      "spdx": "CC-BY-4.0",
      "attribution": "Source attribution required; see DCAT dataset for full statement."
    },
    "classification": {
      "level": "public",
      "notes": "No sensitive locations present."
    },
    "assets": [
      {
        "asset_id": "landcover_cog",
        "kind": "cog",
        "href": "/api/assets/kfm.ks.landcover.1850/landcover_cog",
        "content_type": "image/tiff; application=geotiff",
        "roles": ["data"],
        "checksum": "sha256:5c0c1b6b4b7a5c3b1e1d9c0f0a3e2d1c..."
      },
      {
        "asset_id": "landcover_tiles",
        "kind": "vector_tiles",
        "href": "/tiles/landcover/{z}/{x}/{y}.pbf",
        "content_type": "application/vnd.mapbox-vector-tile",
        "roles": ["tiles"]
      }
    ]
  },
  "links": {
    "self": "/api/datasets/kfm.ks.landcover.1850",
    "related": ["/api/layers/1850_landcover"]
  },
  "provenance": {
    "stac": { "collection": "/stac/collections/kfm.ks.landcover" },
    "dcat": { "dataset": "/dcat/datasets/kfm.ks.landcover.1850" },
    "prov": { "bundle": "/prov/bundles/prov_01J2Y8VZ3B3H0N1Q4W7S8B9F2K" }
  }
}
```

---

## 3) 🧩 STAC Collection (spec-native)

**GET** `/stac/collections/kfm.ks.landcover`

```json
{
  "type": "Collection",
  "id": "kfm.ks.landcover",
  "title": "KFM Kansas Landcover Collection",
  "description": "Landcover layers over time, packaged for map + narrative use.",
  "extent": {
    "spatial": { "bbox": [[-102.051, 36.993, -94.588, 40.003]] },
    "temporal": { "interval": [["1850-01-01T00:00:00Z", "2025-12-31T23:59:59Z"]] }
  },
  "license": "CC-BY-4.0",
  "links": [
    { "rel": "self", "href": "/stac/collections/kfm.ks.landcover" },
    { "rel": "items", "href": "/stac/collections/kfm.ks.landcover/items" },
    { "rel": "root", "href": "/stac" }
  ]
}
```

---

## 4) 🔎 STAC Search (ItemCollection, spec-native)

**POST** `/stac/search`  
Body example: `{ "collections": ["kfm.ks.landcover"], "datetime": "1850-01-01/1850-12-31" }`

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "stac_version": "1.0.0",
      "id": "kfm.ks.landcover.1850.item",
      "bbox": [-102.051, 36.993, -94.588, 40.003],
      "geometry": {
        "type": "Polygon",
        "coordinates": [[[-102.051, 36.993], [-94.588, 36.993], [-94.588, 40.003], [-102.051, 40.003], [-102.051, 36.993]]]
      },
      "properties": {
        "datetime": "1850-07-01T00:00:00Z"
      },
      "assets": {
        "cog": {
          "href": "/api/assets/kfm.ks.landcover.1850/landcover_cog",
          "type": "image/tiff; application=geotiff",
          "roles": ["data"]
        }
      }
    }
  ],
  "links": [
    { "rel": "self", "href": "/stac/search" }
  ]
}
```

---

## 5) 🗺️ Layer registry item (Envelope for UI “Layer Info”)

**GET** `/api/layers/1850_landcover`

```json
{
  "meta": {
    "api_version": "v1",
    "status": "ok",
    "request_id": "req_01J2Y92Y7K4W8Z9C1F2J0V3B7D",
    "generated_at": "2026-01-24T18:48:10Z",
    "warnings": [],
    "paging": null,
    "telemetry": { "trace_id": "trace_7e4f8a0b8f004b77" },
    "governance": { "policy_pack": "kfm-policy@1.4.2", "decision": "allow", "redactions": [] }
  },
  "data": {
    "layer_id": "1850_landcover",
    "title": "Landcover (1850)",
    "kind": "vector_tiles",
    "dataset_id": "kfm.ks.landcover.1850",
    "tile_url_template": "/tiles/landcover/{z}/{x}/{y}.pbf",
    "style": {
      "style_id": "kfm.landcover.categorical.v1",
      "legend": [
        { "label": "Prairie", "value": "prairie" },
        { "label": "Forest", "value": "forest" },
        { "label": "Wetlands", "value": "wetlands" }
      ]
    },
    "attribution": {
      "short": "KFM • Source attribution in metadata",
      "license_spdx": "CC-BY-4.0"
    }
  },
  "links": {
    "self": "/api/layers/1850_landcover",
    "dataset": "/api/datasets/kfm.ks.landcover.1850"
  },
  "provenance": {
    "stac": { "collection": "/stac/collections/kfm.ks.landcover" },
    "dcat": { "dataset": "/dcat/datasets/kfm.ks.landcover.1850" }
  }
}
```

---

## 6) 🧱 Vector tile response (binary; headers example)

**GET** `/tiles/landcover/6/14/24.pbf`

```http
HTTP/1.1 200 OK
Content-Type: application/vnd.mapbox-vector-tile
Content-Encoding: gzip
Cache-Control: public, max-age=3600
ETag: "W/\"sha256-2a0b7c1f...\""
X-Request-Id: req_01J2Y93NQY3QFZ9N0M8W2G7P1R
X-KFM-Dataset-Id: kfm.ks.landcover.1850
X-KFM-Layer-Id: 1850_landcover

<binary gzip MVT bytes>
```

---

## 7) 🧬 GeoJSON features with redaction (Envelope + warnings)

**GET** `/api/layers/archaeology_sites/features?bbox=-99,38,-98,39`

```json
{
  "meta": {
    "api_version": "v1",
    "status": "ok",
    "request_id": "req_01J2Y94KZ1V7D3T6X9H0A2B1C4",
    "generated_at": "2026-01-24T18:52:02Z",
    "warnings": [
      {
        "code": "REDACTED_GEOMETRY",
        "message": "Some geometries were generalized due to sensitivity policy."
      }
    ],
    "paging": null,
    "telemetry": { "trace_id": "trace_0a4d0d0a6a8c4b98" },
    "governance": {
      "policy_pack": "kfm-policy@1.4.2",
      "decision": "allow",
      "redactions": [
        { "field": "geometry", "method": "hex_generalization", "reason": "sensitive_location" }
      ]
    }
  },
  "data": {
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "id": "site_01J2Y94KZ1V7",
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [-98.52, 38.62],
              [-98.48, 38.62],
              [-98.48, 38.66],
              [-98.52, 38.66],
              [-98.52, 38.62]
            ]
          ]
        },
        "properties": {
          "name": "Archaeological Site (generalized)",
          "classification": "restricted",
          "display_policy": "generalized_only"
        }
      }
    ]
  },
  "links": {
    "self": "/api/layers/archaeology_sites/features?bbox=-99,38,-98,39"
  },
  "provenance": {
    "dcat": { "dataset": "/dcat/datasets/kfm.ks.archaeology.sites" },
    "prov": { "bundle": "/prov/bundles/prov_01J2Y90A0C0C0C0C0C0C0C0C0C" }
  }
}
```

---

## 8) 🚌 Real-time feed (polling cursor)

**GET** `/api/transport/buses?since=2026-01-24T18:00:00Z`

```json
{
  "meta": {
    "api_version": "v1",
    "status": "ok",
    "request_id": "req_01J2Y95R6W0B9F6M2H3K7Z8X1Y",
    "generated_at": "2026-01-24T18:55:12Z",
    "warnings": [],
    "paging": null,
    "telemetry": { "trace_id": "trace_40ce7f05c8a74db2" },
    "governance": { "policy_pack": "kfm-policy@1.4.2", "decision": "allow", "redactions": [] }
  },
  "data": {
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "id": "bus_5021",
        "geometry": { "type": "Point", "coordinates": [-95.689, 39.049] },
        "properties": {
          "route_id": "R12",
          "heading_deg": 270,
          "speed_m_s": 7.4,
          "observed_at": "2026-01-24T18:54:58Z"
        }
      }
    ],
    "next_since": "2026-01-24T18:54:58Z"
  },
  "links": {
    "self": "/api/transport/buses?since=2026-01-24T18:00:00Z"
  },
  "provenance": {
    "prov": { "bundle": "/prov/bundles/prov_01J2Y95R9A3Z1Y8C4K2M6N7P8Q" }
  }
}
```

---

## 9) 🎬 Story Node (Markdown + script/config + evidence)

**GET** `/api/story_nodes/prairie_fires_1850s`

```json
{
  "meta": {
    "api_version": "v1",
    "status": "ok",
    "request_id": "req_01J2Y96S4Q3H7P8J1K9M0N2B4C",
    "generated_at": "2026-01-24T18:58:20Z",
    "warnings": [],
    "paging": null,
    "telemetry": { "trace_id": "trace_1b9e5e3f2b1a4c9c" },
    "governance": { "policy_pack": "kfm-policy@1.4.2", "decision": "allow", "redactions": [] }
  },
  "data": {
    "story_node_id": "prairie_fires_1850s",
    "title": "Prairie Fires of the 1850s",
    "summary": "A guided narrative exploring historic fire regimes and landcover context.",
    "content_markdown": "## Intro {#intro}\nPrairie fire was a recurring ecological process...\n\n## Fire Map {#fire_map}\nIn 1855, fire frequency patterns shift...\n",
    "script": {
      "title": "Prairie Fires of the 1850s",
      "steps": [
        {
          "id": 1,
          "text_id": "intro",
          "mapState": {
            "center": [-98.0, 38.5],
            "zoom": 6,
            "layers": ["1850_landcover"]
          },
          "timelineYear": 1850
        },
        {
          "id": 2,
          "text_id": "fire_map",
          "mapState": {
            "center": [-98.0, 38.5],
            "zoom": 6,
            "layers": ["1850_landcover", "fire_frequency"]
          },
          "timelineYear": 1855
        }
      ]
    },
    "evidence": {
      "evidence_manifest": "/api/story_nodes/prairie_fires_1850s/evidence/EM-84.yaml",
      "citations_block": [
        "USGS historical fire ecology summary (archival)",
        "KFM landcover reconstruction dataset (1850)",
        "KFM fire frequency derived layer"
      ]
    }
  },
  "links": {
    "self": "/api/story_nodes/prairie_fires_1850s",
    "ui": "/app/story/prairie_fires_1850s"
  },
  "provenance": {
    "prov": { "bundle": "/prov/bundles/prov_01J2Y96S9Q1W2E3R4T5Y6U7I8O" },
    "stac": { "collection": "/stac/collections/kfm.ks.landcover" }
  }
}
```

---

## 10) 📰 Pulse Threads (geotagged, evidence-backed snippets)

**GET** `/api/pulse/threads?place_id=leavenworth_ks&limit=2`

```json
{
  "meta": {
    "api_version": "v1",
    "status": "ok",
    "request_id": "req_01J2Y97T1D8C5B4A3E2F1G0H9J",
    "generated_at": "2026-01-24T19:02:10Z",
    "warnings": [],
    "paging": { "limit": 2, "next_cursor": null },
    "telemetry": { "trace_id": "trace_9a4c3b2d1e0f4a3b" },
    "governance": { "policy_pack": "kfm-policy@1.4.2", "decision": "allow", "redactions": [] }
  },
  "data": {
    "threads": [
      {
        "pulse_thread_id": "pulse_01J2Y97T9Q8W7E6R5T4Y3U2I1O",
        "title": "Kansas River gauge ticked up overnight",
        "snippet": "Observed level increased ~0.4 ft since 02:00Z; still below advisory threshold.",
        "place_ref": { "place_id": "leavenworth_ks", "label": "Leavenworth, KS" },
        "tags": ["water", "river", "live"],
        "confidence": 0.78,
        "created_at": "2026-01-24T19:01:55Z",
        "evidence": [
          {
            "kind": "dataset",
            "dataset_id": "kfm.usgs.nwis.gauge.kansas_river",
            "checksum": "sha256:1a2b3c4d..."
          }
        ],
        "prov_entity_id": "prov_entity_01J2Y97T..."
      }
    ]
  },
  "links": { "self": "/api/pulse/threads?place_id=leavenworth_ks&limit=2" },
  "provenance": { "prov": { "bundle": "/prov/bundles/prov_01J2Y97T..." } }
}
```

---

## 11) 🧭 Focus Mode answer (citations + audit)

**POST** `/api/focus`

```json
{
  "meta": {
    "api_version": "v1",
    "status": "ok",
    "request_id": "req_01J2Y98YV5B4N3M2C1X0Z9A8S",
    "generated_at": "2026-01-24T19:06:45Z",
    "warnings": [],
    "paging": null,
    "telemetry": { "trace_id": "trace_6c0b2a5fd0a74c78" },
    "governance": { "policy_pack": "kfm-policy@1.4.2", "decision": "allow", "redactions": [] }
  },
  "data": {
    "answer_markdown": "Based on the linked gauge dataset, the Kansas River near Leavenworth rose ~0.4 ft since 02:00Z but remains below advisory thresholds.\n\n**What to watch next:** if the trend continues for 3–6 hours, check rainfall upstream and reservoir releases.\n",
    "citations": [
      {
        "citation_id": "cite:1",
        "label": "USGS / NWIS gauge time series (Kansas River near Leavenworth)",
        "ref": {
          "kind": "dataset",
          "dataset_id": "kfm.usgs.nwis.gauge.kansas_river",
          "href": "/api/datasets/kfm.usgs.nwis.gauge.kansas_river"
        },
        "excerpt": "…level increased ~0.4 ft since 02:00Z…",
        "retrieved_at": "2026-01-24T19:06:12Z"
      }
    ],
    "map_suggestions": {
      "bbox": [-95.75, 39.00, -95.60, 39.10],
      "layers": ["river_gauges_live", "watersheds", "precip_radar"]
    },
    "audit": {
      "model": "kfm-focus-llm",
      "evidence_required": true,
      "policy_checks": [
        { "rule": "evidence_first_text", "result": "pass" },
        { "rule": "sensitive_location", "result": "pass" }
      ]
    }
  },
  "links": { "self": "/api/focus" },
  "provenance": { "prov": { "bundle": "/prov/bundles/prov_01J2Y98Y..." } }
}
```

---

## 12) 🧠 Graph query (REST)

**GET** `/api/graph/places/leavenworth_ks/datasets`

```json
{
  "meta": {
    "api_version": "v1",
    "status": "ok",
    "request_id": "req_01J2Y9A1B2C3D4E5F6G7H8I9J0",
    "generated_at": "2026-01-24T19:10:02Z",
    "warnings": [],
    "paging": null,
    "telemetry": { "trace_id": "trace_12ab34cd56ef7890" },
    "governance": { "policy_pack": "kfm-policy@1.4.2", "decision": "allow", "redactions": [] }
  },
  "data": {
    "place_id": "leavenworth_ks",
    "datasets": [
      { "dataset_id": "kfm.usgs.nwis.gauge.kansas_river", "relation": "HAS_SENSOR" },
      { "dataset_id": "kfm.ks.population.by_decade", "relation": "HAS_STATISTICS" }
    ]
  },
  "links": { "self": "/api/graph/places/leavenworth_ks/datasets" },
  "provenance": {}
}
```

---

## 13) 🧬 GraphQL response example (query + response)

**POST** `/api/graphql`

```graphql
query PersonEvents($personId: ID!) {
  person(id: $personId) {
    id
    name
    events {
      id
      label
      startDate
      places { id name }
    }
  }
}
```

```json
{
  "data": {
    "person": {
      "id": "person_john_brown",
      "name": "John Brown",
      "events": [
        {
          "id": "event_pottawatomie_1856",
          "label": "Pottawatomie Massacre",
          "startDate": "1856-05-24",
          "places": [{ "id": "place_franklin_county_ks", "name": "Franklin County, KS" }]
        }
      ]
    }
  }
}
```

---

## 14) 🧳 Offline pack manifest (Envelope)

**GET** `/api/offline/packs/kansas_river_field_kit`

```json
{
  "meta": {
    "api_version": "v1",
    "status": "ok",
    "request_id": "req_01J2Y9B0C1D2E3F4G5H6I7J8K9",
    "generated_at": "2026-01-24T19:12:44Z",
    "warnings": [],
    "paging": null,
    "telemetry": { "trace_id": "trace_abc123abc123abc1" },
    "governance": { "policy_pack": "kfm-policy@1.4.2", "decision": "allow", "redactions": [] }
  },
  "data": {
    "pack_id": "kansas_river_field_kit",
    "title": "Kansas River Field Kit",
    "region_bbox": [-96.2, 38.6, -94.9, 39.3],
    "includes": {
      "layers": ["watersheds", "river_gauges_live", "historic_flood_extents"],
      "story_nodes": ["prairie_fires_1850s", "floods_1951_overview"],
      "models": ["kfm-mini-llm@v1"]
    },
    "artifacts": [
      {
        "kind": "pmtiles",
        "href": "/api/offline/packs/kansas_river_field_kit/artifacts/watersheds.pmtiles",
        "digest": "sha256:9f8e7d6c..."
      }
    ],
    "license_summary": {
      "effective_spdx": "CC-BY-4.0",
      "note": "Effective license reflects the most restrictive included layer."
    },
    "size_estimate_mb": 842
  },
  "links": { "self": "/api/offline/packs/kansas_river_field_kit" },
  "provenance": { "prov": { "bundle": "/prov/bundles/prov_01J2Y9B0..." } }
}
```

---

# ❌ Error responses (v1)

> All errors use the same envelope pattern with `meta.status = "error"`.

<details>
<summary>🧯 Validation error (400)</summary>

```json
{
  "meta": {
    "api_version": "v1",
    "status": "error",
    "request_id": "req_01J2Y9C2D3E4F5G6H7I8J9K0L1",
    "generated_at": "2026-01-24T19:20:02Z",
    "warnings": [],
    "paging": null,
    "telemetry": { "trace_id": "trace_deadbeefdeadbeef" },
    "governance": { "policy_pack": "kfm-policy@1.4.2", "decision": "allow", "redactions": [] }
  },
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid query parameter: bbox must have 4 numbers.",
    "details": {
      "param": "bbox",
      "expected": "minX,minY,maxX,maxY"
    }
  },
  "links": { "docs": "/api/docs#/errors" },
  "provenance": {}
}
```

</details>

<details>
<summary>🛑 Policy denied (403)</summary>

```json
{
  "meta": {
    "api_version": "v1",
    "status": "error",
    "request_id": "req_01J2Y9D3E4F5G6H7I8J9K0L1M2",
    "generated_at": "2026-01-24T19:21:12Z",
    "warnings": [],
    "paging": null,
    "telemetry": { "trace_id": "trace_0ff1ce0ff1ce0ff1" },
    "governance": {
      "policy_pack": "kfm-policy@1.4.2",
      "decision": "deny",
      "redactions": [],
      "denials": [
        { "rule": "sensitive_location_exact_points", "reason": "restricted_dataset" }
      ]
    }
  },
  "error": {
    "code": "POLICY_DENIED",
    "message": "Access denied by governance policy.",
    "details": {
      "classification_required": "restricted",
      "user_role": "anonymous"
    }
  },
  "links": { "docs": "/api/docs#/governance" },
  "provenance": {}
}
```

</details>

---

# 🧰 Maintainer checklist (when adding/updating examples)

- [ ] ✅ Add/Update schema in `api/contracts/schemas/v1/`
- [ ] ✅ Add/Update example here in `api/contracts/examples/responses/v1/`
- [ ] ✅ Ensure **license + provider + classification** are present where applicable
- [ ] ✅ Ensure **STAC/DCAT/PROV links** exist for derived outputs
- [ ] ✅ Ensure **redaction warnings** appear if anything is generalized/hidden
- [ ] ✅ Keep examples deterministic (stable timestamps/IDs if used in tests)

---

## 🔗 See also

- 🗺️ UI behavior expects: layer info + provenance surfaced (for trust)
- 🧭 Focus Mode expects: citations + audit trail
- 🧾 Data intake expects: STAC/DCAT/PROV triplet + reproducibility

> If you’re unsure whether an endpoint should be enveloped or spec-native, default to:
> ✅ **Envelope for UI** | ✅ **Spec-native for external tooling interoperability**

---
