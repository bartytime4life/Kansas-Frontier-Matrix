# 🗂️ Catalog Schema Contracts (STAC • DCAT • PROV) ✅

![Contracts](https://img.shields.io/badge/contracts-contract--first-2ea44f)
![Gates](https://img.shields.io/badge/gates-fail--closed-critical)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-blue)
![Policy](https://img.shields.io/badge/policy-OPA%20%2F%20Rego-orange)
![Ethics](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-purple)
![Supply%20Chain](https://img.shields.io/badge/supply%20chain-cosign%20%2B%20attestations-informational)

> **One-line mission:** This folder is the **schema registry + contract docs** that power **MCP gates** for KFM’s **evidence-first** catalog (no metadata, no merge, no graph, no UI). 🔒🧾

---

## 🧭 What lives here (and why)

This directory defines the **canonical “catalog contract”** for any artifact that KFM will:
- publish 📦
- search 🔎
- map 🗺️
- query in Focus Mode 🤖
- and ingest into the knowledge graph 🕸️

The contract is **triplet-based**:

| Contract layer | Standard | What it describes | Why it matters |
|---|---|---|---|
| 🛰️ Asset contract | **STAC** | “What files exist and where are they?” (spatial/temporal footprint + assets) | powers map layers, downloads, and spatial discovery |
| 🏷️ Dataset contract | **DCAT** | “What dataset is this?” (title, publisher, license, distributions, themes) | powers dataset cards, licensing, providers, governance |
| 🧬 Lineage contract | **PROV (JSON-LD / PROV-O)** | “How was it made?” (inputs, transformations, agents, run IDs) | powers reproducibility, auditing, trust, rollbacks |

✅ **Rule of thumb:** *If it can appear in KFM, it must be representable as (STAC + DCAT + PROV).*  
(Story Nodes / Pulse Threads follow the same idea via **evidence manifests + PROV snippets**.)

---

## 📁 Expected layout

> This README is located at: `mcp/gates/contracts/data/schema/catalog/README.md`

```text
mcp/🧠
└─ gates/🚦
   └─ contracts/📜
      └─ data/🗃️
         └─ schema/🧩
            └─ catalog/🗂️
               ├─ README.md  👈 you are here
               ├─ stac/🛰️
               │  ├─ kfm-stac-item.schema.json
               │  ├─ kfm-stac-collection.schema.json
               │  └─ extensions/🧷
               ├─ dcat/🏷️
               │  ├─ kfm-dcat-dataset.schema.jsonld
               │  └─ kfm-dcat-distribution.schema.jsonld
               ├─ prov/🧬
               │  ├─ kfm-prov-bundle.schema.jsonld
               │  └─ kfm-prov-activity.schema.jsonld
               ├─ vocab/📚
               │  ├─ licenses.spdx.json
               │  ├─ sensitivity.levels.json
               │  ├─ themes.taxonomy.json
               │  └─ places.authority.json
               ├─ examples/🧪
               │  ├─ stac.item.example.json
               │  ├─ dcat.dataset.example.json
               │  └─ prov.bundle.example.jsonld
               └─ tests/🧯
                  ├─ conftest/🧾
                  └─ fixtures/🧷
```

> ⚠️ **Note:** Actual data files typically live in repo-level `data/` (raw/processed/catalog/prov/stac/etc.).  
> This folder is the **contract source-of-truth** that gates validate against.

---

## 🧠 MCP alignment (Master Coder Protocol)

MCP’s “scientific method” mindset applies directly to catalogs:

- A dataset is a **repeatable experiment**: inputs → procedure → outputs → results 📊
- The **catalog is the lab notebook**: it records what exists, what it means, and how it was produced 🧾
- The **gate is peer review**: no contract compliance = no merge ✅/❌

**Translation into contracts:**
- **Run manifests** become first-class provenance entities 🔐
- **Model cards** and **data cards** become governed metadata artifacts 📇
- **PRs and CI runs** can be treated as provenance events (auditable build chain) 🧬

---

## 🚦 How the gates use these contracts

### Gate stack (typical)
1) **Schema Gate (structure):** JSON/JSON-LD conforms to schemas  
2) **Policy Gate (meaning):** OPA/Rego checks governance rules (license, sensitivity, allowed vocab, etc.)  
3) **Catalog QA Gate (cross-file integrity):** STAC ↔ DCAT ↔ PROV consistency  
4) **Supply-chain Gate (trust):** signatures/attestations exist and match approved identities  
5) **Human review (context):** maintainers review domain correctness + ethical implications

### “Fail closed” philosophy 🔒
If a required field is missing, a license is unknown, sensitivity is unclear, or provenance is absent:
- the gate fails
- the PR does not merge
- the artifact does not ship

---

## 🧩 Contract principles (the “non-negotiables”)

### 1) Evidence-first publishing 🧾
Every artifact is publishable only if it has:
- **discoverable metadata** (DCAT)
- **concrete assets + footprints** (STAC)
- **traceable lineage** (PROV)

### 2) FAIR + CARE baked into schema 🌍🤝
Schemas **must support**:
- Findability: stable IDs, searchable themes, spatial/temporal footprints
- Accessibility: clear distributions, access constraints, contact/publisher
- Interoperability: standard vocab + JSON-LD/linked-data friendly fields
- Reusability: license clarity, provenance, versioning

…and CARE-style ethics:
- authority to control (especially for sensitive / Indigenous contexts)
- cultural protocols and permission-aware access constraints
- explicit sensitivity labeling and mitigation strategy

### 3) UI-driven metadata ✨
The UI is contract-driven:
- dataset cards, layer legends, tooltips, citations, and filters
- time slider / temporal range queries
- 3D tiles / AR overlays and “what am I looking at?” provenance panels

---

## 🏷️ Canonical identifiers & versioning

### Dataset IDs
Use stable dataset IDs that don’t change when filenames do.

**Recommended pattern:**
```text
kfm.<region>.<domain>.<slug>.v<major>
```

Examples:
- `kfm.ks.hydro.usgs_nwis_river_gauges.v1`
- `kfm.ks.climate.prism_normals_1991_2020.v1`
- `kfm.ks.history.santa_fe_trail_waypoints.v1`

### Schema versions
Schemas are versioned with **SemVer**:
- `MAJOR` = breaking changes
- `MINOR` = additive fields, new vocab terms
- `PATCH` = clarifications, bugfix constraints

**Schema rule:** *A catalog JSON MUST declare which schema version it targets* (via `$schema` / `$id` / profile field).

---

## 🧪 Minimal examples

### 🛰️ STAC Item (asset-level)
```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "kfm.ks.hydro.usgs_nwis_river_gauges.v1::station::06891000",
  "geometry": { "type": "Point", "coordinates": [-95.676, 39.049] },
  "bbox": [-95.676, 39.049, -95.676, 39.049],
  "properties": {
    "datetime": "2026-01-23T00:00:00Z",
    "kfm:dataset_id": "kfm.ks.hydro.usgs_nwis_river_gauges.v1",
    "kfm:sensitivity": "public",
    "kfm:themes": ["hydrology", "monitoring"]
  },
  "assets": {
    "latest": {
      "href": "data/processed/hydro/usgs_nwis/latest.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  },
  "links": []
}
```

### 🏷️ DCAT Dataset (dataset-level)
```json
{
  "@context": "https://www.w3.org/ns/dcat2.jsonld",
  "@type": "dcat:Dataset",
  "@id": "kfm.ks.hydro.usgs_nwis_river_gauges.v1",
  "dct:title": "USGS NWIS River Gauges (Kansas)",
  "dct:description": "Station locations and time-series readings for Kansas river gauges.",
  "dct:publisher": { "@type": "foaf:Organization", "foaf:name": "USGS" },
  "dct:license": "CC-BY-4.0",
  "dcat:keyword": ["hydrology", "river", "monitoring"],
  "kfm:sensitivity": "public",
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:format": "GeoJSON",
      "dcat:downloadURL": "data/processed/hydro/usgs_nwis/latest.geojson"
    }
  ]
}
```

### 🧬 PROV Bundle (lineage-level)
```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "kfm": "https://kfm.dev/ns#"
  },
  "@id": "kfm:prov/run/2026-01-23T00:00:00Z/usgs_nwis_ingest",
  "@type": "prov:Bundle",
  "prov:activity": {
    "@id": "kfm:activity/run_manifest_sha256:abc123...",
    "@type": "prov:Activity",
    "prov:startedAtTime": "2026-01-23T00:00:00Z",
    "prov:used": [
      { "@id": "kfm:source/usgs/nwis/api" }
    ],
    "prov:generated": [
      { "@id": "kfm:entity/kfm.ks.hydro.usgs_nwis_river_gauges.v1" }
    ],
    "prov:wasAssociatedWith": { "@id": "kfm:agent/ci" }
  }
}
```

---

## 🧾 Governance card & run manifest (contract-adjacent)

### Governance card (policy inputs)
A small JSON that enumerates:
- allowed licenses
- sensitivity tiers + required mitigations
- Indigenous sovereignty flags / cultural protocol requirements
- required metadata fields

```json
{
  "allowed_licenses": ["CC-BY-4.0", "CC0-1.0", "ODbL-1.0"],
  "required_fields": ["dct:title", "dct:description", "dct:publisher", "dct:license"],
  "sensitivity_levels": {
    "public": { "requires": [] },
    "restricted": { "requires": ["access_constraints", "redaction_strategy"] }
  }
}
```

### Run manifest (reproducibility ledger)
A structured record of each pipeline run:
- inputs, outputs, tool versions
- row counts / summaries
- canonical hash (idempotency + integrity)

```json
{
  "run_id": "2026-01-23T00:00:00Z_usgs_nwis_ingest",
  "inputs": [{ "source": "USGS NWIS API", "query": "..." }],
  "outputs": [{ "path": "data/processed/hydro/usgs_nwis/latest.geojson", "sha256": "..." }],
  "tool_versions": { "python": "3.12.x", "gdal": "3.x" },
  "canonical_digest_sha256": "abc123..."
}
```

---

## 🧵 Beyond datasets: narratives & “Pulse” content

KFM extends evidence-first contracts into narrative artifacts:
- **Story Nodes** (long-form governed narrative)
- **Pulse Threads** (timely, geotagged, data-backed updates)

**Narrative contract pattern:**
- a short human citation block (readable)
- a machine-readable evidence manifest (YAML/JSON)
- a PROV snippet that ties the narrative to sources + agents

This keeps narratives **queryable**, auditable, and linkable in the graph.

---

## 🧊 3D / AR / WebGL-ready cataloging

Catalog schemas should support assets beyond “flat maps”:
- 3D Tiles (Cesium), point clouds, meshes (glTF), CZML animations
- AR “scene packs” that reference the same STAC/DCAT/PROV foundations
- optional performance metadata (tiling scheme, LODs, bounds, cache hints)

✅ Principle: **New visualization mode ≠ new trust model.**  
AR/3D still rides on the same contract triplet.

---

## 🕵️ Privacy & sensitive-location handling

Some features/datasets may require:
- coordinate generalization / fuzzing
- access controls (authz)
- aggregation thresholds (k-anonymity style)
- auditable query logs for sensitive endpoints

📌 The catalog must explicitly encode:
- sensitivity level
- permitted uses
- redaction strategy
- who can access what, and why

---

## 🔧 Adding or changing a schema (PR checklist)

- [ ] ✅ Schema updated (`/stac`, `/dcat`, `/prov`, or `/kfm`)
- [ ] 🧪 Example updated (`/examples`)
- [ ] 🧾 Policy updated (Rego) if semantics changed (`/tests/conftest`)
- [ ] 📚 Vocab updated (`/vocab`) if new terms/licenses were added
- [ ] 🔁 Backward compatibility plan (migration notes if breaking)
- [ ] 🧬 Provenance impact assessed (graph + audit expectations)
- [ ] 🧭 UI impact assessed (filters/cards/tooltips)

---

## 📚 Reference packs (project libraries)

These files are “knowledge packs” that inform schema evolution and gate design:
- 🧠 **AI pack**: model governance, evaluation, reproducibility patterns
- 🗺️ **Maps/WebGL pack**: 3D/WebGL practices and asset formats
- 🧰 **Programming pack**: language/tooling patterns for validation + automation
- 🏗️ **Data management pack**: data engineering, lakehouse, privacy, and CI/CD patterns

> Keep schemas small, composable, and versioned. Pull ideas from packs into **explicit contracts**, not implicit tribal knowledge. ✅

---

## 🧾 Glossary

- **STAC**: SpatioTemporal Asset Catalog — geospatial asset discovery standard  
- **DCAT**: Data Catalog Vocabulary — dataset metadata for publishers and distributions  
- **PROV-O**: W3C provenance ontology — lineage for entities/activities/agents  
- **OPA / Rego**: policy-as-code engine + rule language used for gates  
- **Fail closed**: if unsure, reject (don’t silently accept incomplete metadata)  
- **FAIR/CARE**: data stewardship + ethical governance principles  
- **Run manifest**: structured record of a pipeline run (inputs/outputs/tools + digest)  
- **Evidence manifest**: structured list of sources backing a narrative (Story/Pulse)

---

## ✅ North Star

> **If it’s not in the catalog, it’s not real (to the system).**  
> The catalog is the contract boundary between raw bytes and trusted knowledge. 🧠🧾

