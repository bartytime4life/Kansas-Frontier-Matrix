# 🕸️ Graph API v1 — Response Examples

![Contract-First](https://img.shields.io/badge/contract--first-%F0%9F%93%9C-blue)
![Evidence-First](https://img.shields.io/badge/evidence--first-STAC%20%2B%20DCAT%20%2B%20PROV-7b2cbf)
![API](https://img.shields.io/badge/API-v1-success)
![REST](https://img.shields.io/badge/REST-JSON-informational)
![GraphQL](https://img.shields.io/badge/GraphQL-ready-%23E10098?logo=graphql&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-graph-%23008CC1?logo=neo4j&logoColor=white)

> [!NOTE]
> This folder holds **canonical response payload examples** for the **v1 Graph API** (REST + GraphQL) used by **KFM UI**, **Focus Mode**, and any downstream tooling (tests, mocks, docs, SDK generation).

---

## 🎯 What this folder is for

These examples are designed to be:

- ✅ **Contract-first**: stable fixtures that match the v1 schemas
- 🧾 **Evidence-first**: every graph entity is traceable to catalog/provenance IDs (no “mystery nodes”)
- 🧭 **Ontology-aligned**: node/edge semantics are consistent (CIDOC-CRM / GeoSPARQL / OWL-Time / PROV-O)
- 🔐 **Policy-aware**: examples demonstrate classification + redaction patterns

---

## 📁 Folder layout

> (Some files may be added over time — this README defines the recommended naming + scenarios.)

```text
📦 api/contracts/examples/responses/v1/graph/
├─ 📄 README.md                          👈 you are here
├─ 📄 place_datasets.200.json            (REST) datasets linked to a Place
├─ 📄 place_datasets.404.json            (REST) Place not found
├─ 📄 subgraph.200.json                  (REST) generic subgraph expansion
├─ 📄 graphql.dataset.200.json           (GraphQL) dataset(id) success
├─ 📄 graphql.dataset.not_found.json     (GraphQL) dataset(id) not found
└─ 📄 subgraph.redacted.200.json         (REST) redaction/classification example
```

---

## 🧩 API surface (what these examples represent)

### REST (typical)
- `GET /v1/graph/places/{placeId}/datasets` → list datasets connected to a **Place**

### GraphQL (typical)
- `query { dataset(id: "...") { ... relatedPlaces ... relatedEvents ... } }`

> [!TIP]
> The UI should **never** query Neo4j directly. It only talks to the API (REST/GraphQL), which applies governance + authorization checks.

---

## 🧾 Evidence Triplet & Traceability (STAC + DCAT + PROV)

KFM’s graph is not “just links” — it’s a **semantic index** over **evidence-backed catalogs**:

```text
DCAT (dataset catalog) ─┐
STAC (assets/items) ────┼──▶ Neo4j Graph Node(s) + Relationships
PROV (lineage/audit) ───┘
```

**Rule of thumb for examples in this folder:**

- Every node MUST include at least one `refs.*` pointer to its backing evidence (DCAT/STAC/PROV or equivalent).
- If you can’t name the evidence, the node doesn’t belong in “published” graph responses.

---

## 🧠 Node & Edge conventions used in examples

> These are conventions for response examples and are intentionally **UI-friendly** while staying **graph-faithful**.

### Node shape (property graph style)

```json
{
  "id": "urn:kfm:place:ks:county:20175",
  "labels": ["Place", "County"],
  "types": ["geo:Feature"],
  "display": {
    "name": "Seward County, Kansas",
    "icon": "🏞️"
  },
  "props": {
    "fips": "20175",
    "iso_3166_2": "US-KS"
  },
  "geometry": {
    "type": "Point",
    "coordinates": [-100.853, 37.186]
  },
  "time": null,
  "refs": {
    "dcat": "urn:kfm:dcat:dataset:kfm.ks.admin.boundaries",
    "stac": "urn:kfm:stac:item:ks_counties.seward",
    "prov": "urn:kfm:prov:entity:ks_counties.seward@2025-01-01"
  },
  "access": {
    "classification": "public",
    "care_label": "open"
  }
}
```

### Edge shape

```json
{
  "id": "urn:kfm:edge:1f7b0e",
  "type": "COVERS",
  "from": "urn:kfm:dataset:kfm.ks.veg.health",
  "to": "urn:kfm:place:ks:county:20175",
  "props": {
    "confidence": 0.93,
    "method": "spatial_intersection"
  },
  "refs": {
    "prov": "urn:kfm:prov:activity:graph_ingest:2025-01-01"
  }
}
```

---

## ✅ REST response envelope (recommended)

Most REST examples in this folder follow an envelope so clients can rely on consistent metadata:

| Field | Type | Notes |
|---|---|---|
| `api_version` | string | e.g. `"v1"` |
| `kind` | string | semantic response type, e.g. `"kfm.graph.place_datasets"` |
| `request_id` | string | correlates logs / governance ledger |
| `generated_at` | ISO-8601 | server time |
| `data` | object | payload |
| `meta` | object | counts, paging, redactions, timing |
| `links` | object | canonical follow-up routes |

> [!IMPORTANT]
> GraphQL responses are **standard GraphQL JSON** (`data`, optional `errors`, optional `extensions`) and are shown separately below.

---

## 📌 Example: Place → Datasets (REST 200)

**Scenario:** UI opens a Place details panel (county selected), needs datasets linked to that Place.

<details>
<summary><strong>📄 place_datasets.200.json</strong> (click to expand)</summary>

```json
{
  "api_version": "v1",
  "kind": "kfm.graph.place_datasets",
  "request_id": "req_01HTEXAMPLEPLACE200",
  "generated_at": "2026-01-24T18:03:12Z",
  "data": {
    "place": {
      "id": "urn:kfm:place:ks:county:20175",
      "labels": ["Place", "County"],
      "types": ["geo:Feature"],
      "display": { "name": "Seward County, Kansas", "icon": "🏞️" },
      "props": { "fips": "20175", "state": "KS" },
      "geometry": { "type": "Point", "coordinates": [-100.853, 37.186] },
      "refs": {
        "dcat": "urn:kfm:dcat:dataset:kfm.ks.admin.boundaries",
        "stac": "urn:kfm:stac:item:ks_counties.seward",
        "prov": "urn:kfm:prov:entity:ks_counties.seward@2025-01-01"
      },
      "access": { "classification": "public", "care_label": "open" }
    },
    "datasets": [
      {
        "id": "kfm.ks.veg.health",
        "title": "Vegetation Health Index (Kansas)",
        "relation": "COVERS",
        "coverage": {
          "spatial": { "place_id": "urn:kfm:place:ks:county:20175", "resolution": "county" },
          "temporal": { "start": "2000-01-01", "end": null, "granularity": "monthly" }
        },
        "evidence": {
          "dcat_dataset": "urn:kfm:dcat:dataset:kfm.ks.veg.health",
          "stac_collection": "urn:kfm:stac:collection:kfm.ks.veg.health",
          "prov_entity": "urn:kfm:prov:entity:kfm.ks.veg.health@2025-01-01"
        },
        "access": { "classification": "public", "care_label": "open" }
      },
      {
        "id": "kfm.ks.landcover.2020",
        "title": "Kansas Landcover (2020)",
        "relation": "COVERS",
        "coverage": {
          "spatial": { "place_id": "urn:kfm:place:ks:county:20175", "resolution": "30m" },
          "temporal": { "start": "2020-01-01", "end": "2020-12-31", "granularity": "annual" }
        },
        "evidence": {
          "dcat_dataset": "urn:kfm:dcat:dataset:kfm.ks.landcover.2020",
          "stac_collection": "urn:kfm:stac:collection:kfm.ks.landcover.2020",
          "prov_entity": "urn:kfm:prov:entity:kfm.ks.landcover.2020@2025-01-01"
        },
        "access": { "classification": "public", "care_label": "open" }
      },
      {
        "id": "kfm.ks.drought.pdsi.1895-2024",
        "title": "Palmer Drought Severity Index (PDSI) — Kansas (1895–2024)",
        "relation": "RELATED_TO",
        "coverage": {
          "spatial": { "place_id": "urn:kfm:place:ks:county:20175", "resolution": "county" },
          "temporal": { "start": "1895-01-01", "end": "2024-12-31", "granularity": "monthly" }
        },
        "evidence": {
          "dcat_dataset": "urn:kfm:dcat:dataset:kfm.ks.drought.pdsi.1895-2024",
          "stac_collection": "urn:kfm:stac:collection:kfm.ks.drought.pdsi.1895-2024",
          "prov_entity": "urn:kfm:prov:entity:kfm.ks.drought.pdsi.1895-2024@2025-01-01"
        },
        "access": { "classification": "public", "care_label": "open" }
      },
      {
        "id": "kfm.sim.ks.drought.2040",
        "title": "Predicted Drought Severity in Kansas by 2040 (Simulation)",
        "relation": "RELATED_TO",
        "coverage": {
          "spatial": { "place_id": "urn:kfm:place:ks:county:20175", "resolution": "county" },
          "temporal": { "start": "2040-01-01", "end": "2040-12-31", "granularity": "annual" }
        },
        "data_kind": "simulation",
        "uncertainty": {
          "summary": "Model output; not observed truth.",
          "confidence_interval": "see model card"
        },
        "evidence": {
          "dcat_dataset": "urn:kfm:dcat:dataset:kfm.sim.ks.drought.2040",
          "stac_collection": "urn:kfm:stac:collection:kfm.sim.ks.drought.2040",
          "prov_entity": "urn:kfm:prov:entity:kfm.sim.ks.drought.2040@2025-01-01"
        },
        "access": { "classification": "public", "care_label": "open" }
      }
    ]
  },
  "meta": {
    "count": 4,
    "paging": { "cursor": null, "next": null },
    "policy": { "redactions_applied": 0 }
  },
  "links": {
    "self": "/api/v1/graph/places/urn:kfm:place:ks:county:20175/datasets",
    "place": "/api/v1/places/urn:kfm:place:ks:county:20175"
  }
}
```

</details>

---

## 🚫 Example: Place not found (REST 404)

<details>
<summary><strong>📄 place_datasets.404.json</strong> (click to expand)</summary>

```json
{
  "api_version": "v1",
  "kind": "kfm.error",
  "request_id": "req_01HTEXAMPLEPLACE404",
  "generated_at": "2026-01-24T18:03:12Z",
  "error": {
    "status": 404,
    "code": "PLACE_NOT_FOUND",
    "message": "No Place node found for placeId=urn:kfm:place:ks:county:99999",
    "details": {
      "placeId": "urn:kfm:place:ks:county:99999",
      "hint": "Check identifier scheme (FIPS-based county IDs are recommended)."
    }
  }
}
```

</details>

---

## 🌐 Example: Subgraph expansion (REST 200)

**Scenario:** UI needs a compact subgraph for a Place (for “notable events”, “related datasets”, “story links”)  
**Or:** Focus Mode needs graph context for multi-hop reasoning.

<details>
<summary><strong>📄 subgraph.200.json</strong> (click to expand)</summary>

```json
{
  "api_version": "v1",
  "kind": "kfm.graph.subgraph",
  "request_id": "req_01HTEXAMPLESUBGRAPH200",
  "generated_at": "2026-01-24T18:03:12Z",
  "data": {
    "seed": { "id": "urn:kfm:place:ks:county:20175", "label": "Seward County, Kansas" },
    "depth": 2,
    "nodes": [
      {
        "id": "urn:kfm:place:ks:county:20175",
        "labels": ["Place", "County"],
        "types": ["geo:Feature"],
        "display": { "name": "Seward County, Kansas", "icon": "🏞️" },
        "props": { "fips": "20175" },
        "geometry": { "type": "Point", "coordinates": [-100.853, 37.186] },
        "refs": {
          "dcat": "urn:kfm:dcat:dataset:kfm.ks.admin.boundaries",
          "prov": "urn:kfm:prov:entity:ks_counties.seward@2025-01-01"
        },
        "access": { "classification": "public", "care_label": "open" }
      },
      {
        "id": "urn:kfm:event:dust_bowl.great_plains",
        "labels": ["Event", "HistoricalPeriod"],
        "types": ["cidoc:E5_Event", "time:Interval"],
        "display": { "name": "Dust Bowl era (Great Plains)", "icon": "🌪️" },
        "props": { "summary": "Severe drought + land degradation across the Great Plains." },
        "time": { "start": "1930-01-01", "end": "1939-12-31" },
        "refs": {
          "dcat": "urn:kfm:dcat:dataset:kfm.docs.dust_bowl.references",
          "prov": "urn:kfm:prov:entity:kfm.docs.dust_bowl.references@2025-01-01"
        },
        "access": { "classification": "public", "care_label": "open" }
      },
      {
        "id": "urn:kfm:dataset:kfm.ks.drought.pdsi.1895-2024",
        "labels": ["Dataset"],
        "types": ["dcat:Dataset", "prov:Entity"],
        "display": { "name": "PDSI — Kansas (1895–2024)", "icon": "📊" },
        "props": {
          "dataset_id": "kfm.ks.drought.pdsi.1895-2024",
          "theme": ["climate", "drought"]
        },
        "refs": {
          "dcat": "urn:kfm:dcat:dataset:kfm.ks.drought.pdsi.1895-2024",
          "stac": "urn:kfm:stac:collection:kfm.ks.drought.pdsi.1895-2024",
          "prov": "urn:kfm:prov:entity:kfm.ks.drought.pdsi.1895-2024@2025-01-01"
        },
        "access": { "classification": "public", "care_label": "open" }
      },
      {
        "id": "urn:kfm:story:seward.dust_bowl.overview",
        "labels": ["StoryNode"],
        "types": ["kfm:StoryNode", "prov:Entity"],
        "display": { "name": "Dust Bowl Impacts — Southwest Kansas", "icon": "📖" },
        "props": {
          "format": "story_node.v1",
          "excerpt": "A guided narrative connecting climate evidence, land-use change, and local impacts."
        },
        "refs": {
          "prov": "urn:kfm:prov:entity:story:seward.dust_bowl.overview@2026-01-10",
          "citations": [
            "urn:kfm:dcat:dataset:kfm.ks.drought.pdsi.1895-2024",
            "urn:kfm:dcat:dataset:kfm.docs.dust_bowl.references"
          ]
        },
        "access": { "classification": "public", "care_label": "open" }
      },
      {
        "id": "urn:kfm:pulse:2026-01-24T17:58:00Z:seward:drought_watch",
        "labels": ["PulseThread"],
        "types": ["kfm:PulseThread", "prov:Entity"],
        "display": { "name": "Pulse: Drought Watch (Seward County)", "icon": "⚡" },
        "props": {
          "doc_uuid": "urn:uuid:5c3a9b2e-9d83-4d1a-ae8c-2b4c1d6fdc77",
          "summary": "Snapshot narrative tying current drought indicators to historical analogs.",
          "tags": ["drought", "context", "rapid-brief"]
        },
        "time": { "start": "2026-01-24T17:58:00Z", "end": null },
        "refs": {
          "prov": "urn:kfm:prov:entity:pulse:seward:drought_watch@2026-01-24",
          "citations": ["urn:kfm:dcat:dataset:kfm.ks.drought.pdsi.1895-2024"]
        },
        "access": { "classification": "public", "care_label": "open" }
      },
      {
        "id": "urn:kfm:concept:drought_severity",
        "labels": ["ConceptualAttentionNode", "Concept"],
        "types": ["skos:Concept"],
        "display": { "name": "Drought severity", "icon": "🧠" },
        "props": {
          "importance": 0.87,
          "embedding_ref": "urn:kfm:embedding:concept:drought_severity:v1"
        },
        "refs": {
          "prov": "urn:kfm:prov:entity:concept:drought_severity@2026-01-10"
        },
        "access": { "classification": "public", "care_label": "open" }
      }
    ],
    "edges": [
      {
        "id": "urn:kfm:edge:cov1",
        "type": "COVERS",
        "from": "urn:kfm:dataset:kfm.ks.drought.pdsi.1895-2024",
        "to": "urn:kfm:place:ks:county:20175",
        "props": { "confidence": 0.93, "method": "spatial_intersection" },
        "refs": { "prov": "urn:kfm:prov:activity:graph_ingest:2025-01-01" }
      },
      {
        "id": "urn:kfm:edge:rel1",
        "type": "RELATED_TO",
        "from": "urn:kfm:event:dust_bowl.great_plains",
        "to": "urn:kfm:place:ks:county:20175",
        "props": { "confidence": 0.72, "method": "historical_region_link" },
        "refs": { "prov": "urn:kfm:prov:activity:curation:2025-01-01" }
      },
      {
        "id": "urn:kfm:edge:mention1",
        "type": "CITES",
        "from": "urn:kfm:story:seward.dust_bowl.overview",
        "to": "urn:kfm:dataset:kfm.ks.drought.pdsi.1895-2024",
        "props": { "citation_style": "footnote" },
        "refs": { "prov": "urn:kfm:prov:activity:story_authoring:2026-01-10" }
      },
      {
        "id": "urn:kfm:edge:pulse1",
        "type": "ABOUT",
        "from": "urn:kfm:pulse:2026-01-24T17:58:00Z:seward:drought_watch",
        "to": "urn:kfm:concept:drought_severity",
        "props": { "confidence": 0.8 },
        "refs": { "prov": "urn:kfm:prov:activity:pulse_generation:2026-01-24" }
      },
      {
        "id": "urn:kfm:edge:pulse2",
        "type": "LOCATED_IN",
        "from": "urn:kfm:pulse:2026-01-24T17:58:00Z:seward:drought_watch",
        "to": "urn:kfm:place:ks:county:20175",
        "props": { "confidence": 0.95 },
        "refs": { "prov": "urn:kfm:prov:activity:pulse_generation:2026-01-24" }
      }
    ]
  },
  "meta": {
    "node_count": 6,
    "edge_count": 5,
    "ontology_profile": "kfm-onto:v1",
    "policy": { "redactions_applied": 0 }
  }
}
```

</details>

---

## 🔒 Example: Redaction / classification (REST 200)

**Scenario:** graph includes a “station” node that is sensitive. API must either omit it or redact its geometry.

<details>
<summary><strong>📄 subgraph.redacted.200.json</strong> (click to expand)</summary>

```json
{
  "api_version": "v1",
  "kind": "kfm.graph.subgraph",
  "request_id": "req_01HTEXAMPLESUBGRAPHREDACTED",
  "generated_at": "2026-01-24T18:03:12Z",
  "data": {
    "seed": { "id": "urn:kfm:place:ks:county:20175", "label": "Seward County, Kansas" },
    "depth": 1,
    "nodes": [
      {
        "id": "urn:kfm:station:private:seward:001",
        "labels": ["Station", "Sensor"],
        "types": ["geo:Feature"],
        "display": { "name": "Private Monitoring Station (redacted)", "icon": "🛰️" },
        "props": { "source": "private_partner", "station_code": "SEW-PRIV-001" },
        "geometry": null,
        "refs": {
          "dcat": "urn:kfm:dcat:dataset:kfm.ks.sensors.private_partner",
          "prov": "urn:kfm:prov:entity:kfm.ks.sensors.private_partner@2026-01-01"
        },
        "access": {
          "classification": "restricted",
          "care_label": "culturally_sensitive",
          "redactions": ["geometry"]
        }
      }
    ],
    "edges": []
  },
  "meta": {
    "node_count": 1,
    "edge_count": 0,
    "policy": {
      "redactions_applied": 1,
      "redaction_log": [
        {
          "target": "urn:kfm:station:private:seward:001",
          "field": "geometry",
          "reason": "classification.restricted"
        }
      ]
    }
  }
}
```

</details>

---

## 🧬 Example: Dataset query (GraphQL 200)

**Scenario:** Flexible, client-driven graph query.

<details>
<summary><strong>📄 graphql.dataset.200.json</strong> (click to expand)</summary>

```json
{
  "data": {
    "dataset": {
      "id": "kfm.ks.veg.health",
      "title": "Vegetation Health Index (Kansas)",
      "relatedEvents": [
        {
          "id": "urn:kfm:event:dust_bowl.great_plains",
          "title": "Dust Bowl era (Great Plains)",
          "timeRange": { "start": "1930-01-01", "end": "1939-12-31" }
        }
      ],
      "relatedPlaces": [
        { "id": "urn:kfm:place:ks:county:20175", "name": "Seward County, Kansas" }
      ]
    }
  },
  "extensions": {
    "request_id": "req_01HTEXAMPLEGRAPHQL200",
    "ontology_profile": "kfm-onto:v1"
  }
}
```

</details>

---

## ❓ Example: Dataset not found (GraphQL 200 + errors)

<details>
<summary><strong>📄 graphql.dataset.not_found.json</strong> (click to expand)</summary>

```json
{
  "data": { "dataset": null },
  "errors": [
    {
      "message": "Dataset not found",
      "path": ["dataset"],
      "extensions": {
        "code": "NOT_FOUND",
        "datasetId": "kfm.ks.does.not.exist",
        "request_id": "req_01HTEXAMPLEGRAPHQL404"
      }
    }
  ]
}
```

</details>

---

## 🧪 Contract testing tips

✅ Keep example files:

- **Minimal but realistic** (prefer short lists, avoid giant geometries)
- **Deterministic** (stable IDs, stable ordering of arrays)
- **Evidence-linked** (`refs.dcat|stac|prov` for every node where applicable)
- **Policy-representative** (include at least one redaction/classification example)

> [!WARNING]
> If you add a new response example that changes shape in a backwards-incompatible way, **do not** overwrite v1 examples — add v2 in the appropriate version folder.

---

## 🔗 Related concepts (for implementers)

- 🧠 Focus Mode uses graph traversal + retrieval to answer questions **with citations**
- 🗺️ UI details panels can “aggregate info from the graph” (events, datasets, stories) for a selected Place
- 🧾 Provenance-first means outputs should be auditable and explainable

---

## ✅ Quick checklist for adding new graph examples

- [ ] Node has stable `id` (URN-style recommended)
- [ ] Node has at least one evidence reference (`refs.*`)
- [ ] Edge meaning is clear (`type` matches ontology/contract naming)
- [ ] Classification is explicit (even if `public`)
- [ ] Any simulated/predicted dataset is labeled (`data_kind: simulation` + uncertainty hint)
- [ ] Example is small enough to eyeball in PR review 😄

---
