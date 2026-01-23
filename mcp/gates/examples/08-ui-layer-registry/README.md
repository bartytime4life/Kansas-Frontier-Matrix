<div align="center">

# 🧩🗺️ Example 08 — UI Layer Registry

**Single source of truth for every visible layer** (2D 🗺️, 3D 🌍, Story Nodes 📖, Pulse Threads ⚡) — validated by **MCP Gates** so KFM never ships “mystery layers”.

![MCP Gate](https://img.shields.io/badge/MCP%20Gate-ui--layer--registry-6f42c1)
![Policy](https://img.shields.io/badge/policy--as--code-OPA%2FRego-111827)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-0ea5e9)
![Rendering](https://img.shields.io/badge/render-React%20%2B%20MapLibre%20%2B%20Cesium-22c55e)
![Ethics](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-f59e0b)

</div>

> [!IMPORTANT]
> In KFM, a **map layer is a claim**. If a layer can’t surface its **source, license, lineage, and handling**, it **doesn’t ship**.

---

## 🎯 What this example demonstrates

This gate + example layout shows how to:

- ✅ Define every UI layer in **manifest files** (schema-driven, config-first)
- ✅ Compile manifests into a **runtime registry artifact** (`ui-layer-registry.json`)
- ✅ Enforce **“No Mystery Layers”**:
  - every layer ties back to **STAC / DCAT / PROV**
  - every layer exposes a **Layer Info** / **Provenance** view in the UI
- ✅ Enforce **governance + safety**:
  - sensitivity classification, CARE redactions, “safe-by-default” visibility rules
- ✅ Support KFM’s “map behind the map” UX:
  - Layer Provenance panel 🧾
  - Focus Mode citations 🔎
  - Story Nodes + timeline-driven layer state ⏳
- ✅ Support **performance** patterns:
  - deterministic packaging (GeoParquet + PMTiles) + hashed artifacts for reproducible rendering
  - static tile delivery for big layers, optional offline packs 📦

---

## 🧠 Mental model

### Layer Manifest vs Layer Registry

- **Layer manifest** = source-of-truth definition for one layer (YAML/JSON).
- **Layer registry** = compiled index the UI consumes (searchable, grouped, sortable, safe defaults).

> Think: *STAC/DCAT/PROV describe the data* ✅  
> *UI Layer Registry describes how the UI is allowed to render the data* ✅

---

## 🧬 End-to-end flow (the “gate” perspective)

```mermaid
flowchart LR
  A[📄 Layer manifests<br/>layers/*.layer.yaml] --> B[🛡️ Gate: ui-layer-registry]
  B -->|schema + policy checks| C[📦 Compiled registry artifact<br/>dist/ui-layer-registry.json]
  C --> D[🧾 Lockfile<br/>dist/ui-layer-registry.lock.json]
  C --> E[🗺️ UI Layer Panel<br/>React + MapLibre + (optional) Cesium]
  E --> F[🔎 Layer Provenance panel<br/>source + license + processing summary]
  E --> G[🧠 Focus Mode context bundle<br/>active layers + citations]
```

---

## 📁 Suggested example layout

```text
📁 mcp/
  📁 gates/
    📁 examples/
      📁 08-ui-layer-registry/
        📄 README.md

        📁 layer-registry/
          📄 registry.yaml                       # (optional) grouping + defaults
          📁 layers/                              # source-of-truth manifests (1 file = 1 layer)
            📄 hydrology.river_gauges.layer.yaml
            📄 geology.surficial_units.layer.yaml
            📄 history.treaty_boundaries.layer.yaml
            📄 story.prairie_fire.layer.yaml
            📄 pulse.frontier_updates.layer.yaml

          📁 schemas/
            📄 ui-layer.schema.json               # schema for a single layer manifest
            📄 ui-layer-registry.schema.json      # schema for compiled registry artifact

          📁 policies/
            📄 ui_layer.rego                      # policy-as-code checks (OPA/Rego)
            📄 governance.rego                    # FAIR+CARE, sensitivity, licensing

          📁 scripts/
            📄 validate_registry.(py|ts)          # schema + policy runner
            📄 compile_registry.(py|ts)           # compile manifests → runtime JSON

        📁 dist/
          📄 ui-layer-registry.json               # build artifact UI loads
          📄 ui-layer-registry.lock.json          # digests + build metadata for rollbacks
          📁 reports/
            📄 ui-layer-registry.report.md        # human readable gate report
```

> [!NOTE]
> Your repo may use different tooling (Node/Python/Make). The shape above is the *contract* this example is aiming for.

---

## 🧾 Layer manifest (v1) — recommended fields

Below is a **pragmatic** manifest shape that matches the spirit of the KFM docs: **configuration-driven UI**, **catalog-first**, and **provenance always available**.

### ✅ Minimal manifest example

```yaml
# layers/hydrology.river_gauges.layer.yaml
id: hydrology.river_gauges.realtime
title: "River Gauges (Real-time)"
description: "Live water level readings per station, refreshed automatically."
category: "Hydrology"
tags: ["realtime", "water", "monitoring"]

type: vector.point
render:
  engine: maplibre
  source:
    kind: geojson
    api:
      method: GET
      path: /api/hydrology/river-gauges
      params:
        latest: true
  style:
    # style can be inline, a reference, or a generated style token
    marker: "water-drop"
    labelField: "station_name"

temporal:
  mode: realtime
  refreshSeconds: 60

spatial:
  crs: "EPSG:4326"
  boundsWgs84: [-102.1, 36.99, -94.6, 40.0]

provenance:
  # required: must link to cataloged metadata
  dcat_dataset_id: "dcat:usgs-nwis-water-data"
  stac_collection_id: "stac:hydrology-river-gauges"
  prov_bundle: "data/prov/hydrology/river_gauges.prov.json"
  attribution: "USGS NWIS"

governance:
  license: "Public Domain"
  sensitivity: "public" # public | restricted | sensitive
  care:
    # CARE notes / enforcement hints for policy pack
    requiresRedaction: false

ui:
  defaultVisible: false
  opacityDefault: 0.85
  legend:
    kind: "categorical"
    title: "Gauge Stations"

a11y:
  label: "Real-time river gauge stations"
  keyboardHint: "Toggle layer from the Layers panel"
```

---

## ⚙️ Packaging patterns supported by the registry

KFM’s “fast UI + reproducible ETL” approach benefits from deterministic artifact packaging.

### 🧱 Example: dual-format packaging (GeoParquet + PMTiles)

```yaml
# layers/geology.surficial_units.layer.yaml
id: geology.surficial_units
title: "Surficial Geology Units"
type: vector.polygon
render:
  engine: maplibre
  source:
    kind: pmtiles
    # recommended: treat large tile artifacts as immutable, addressable assets
    uri: "oci://ghcr.io/kfm/tiles/surficial_geology:2026-01-11#sha256:<digest>"
  styleRef: "styles/geology/surficial_units.style.json"

provenance:
  stac_collection_id: "stac:surficial-geology"
  dcat_dataset_id: "dcat:surficial-geology-package"
  prov_bundle: "data/prov/geology/surficial_units.prov.json"

governance:
  license: "CC-BY-4.0"
  sensitivity: "public"
```

Why this matters:
- **PMTiles** supports fast static tile serving (and offline-friendly workflows) 📦
- **GeoParquet** stays analytics-friendly 🧪
- **STAC/DCAT records** register both artifacts
- **hashes/digests** enable reproducible rebuilds + rollbacks 🔁

---

## 🛡️ Gate checks (what must pass)

This example’s gate should fail **closed**. If a layer can’t prove compliance, it can’t be registered.

### 1) ✅ Schema validation
- every manifest conforms to `schemas/ui-layer.schema.json`
- compiled registry conforms to `schemas/ui-layer-registry.schema.json`

### 2) ⛓ Provenance required (No Mystery Layers)
- every visible layer must link to:
  - **DCAT dataset** (who/what/where/license)
  - **STAC collection/item** (spatial/temporal/bounds/assets)
  - **PROV bundle** (lineage: inputs → activities → outputs)
- the registry must include enough information for the UI to render:
  - a **Layer Info** view
  - a **Layer Provenance** panel entry

### 3) ⚖ Governance + ethics (FAIR + CARE)
- license present + compatible with public display
- sensitivity classification present
- if `sensitivity != public`:
  - enforce access policy flags
  - enforce coordinate generalization / redaction hints
- require explicit “fact vs interpretation” flags for narrative layers (Story Nodes)

### 4) 🔎 Focus Mode & Story Node integration rules
- layers must be **machine-ingestible**: stable IDs, tags, provenance links
- story-related layers must:
  - reference graph IDs (people/places/events) where applicable
  - include citations for factual claims
- registry must expose a “context bundle” shape the AI can ingest:
  - active layer IDs
  - provenance pointers (STAC/DCAT/PROV)
  - warnings / governance flags

### 5) 🧑‍🦽 Accessibility & UX contract
- each layer includes `a11y.label` (screen reader friendly)
- legends and popups must be renderable without custom one-off code
- UI must remain modular/config-driven (no hard-coded Kansas-only logic)

### 6) 🚀 Performance budgets
- required bounds / zoom constraints for heavy layers
- tile or feature limits (policy-defined)
- prefer packaged artifacts (PMTiles / precomputed tiles) for large datasets

---

## 🧾 Gate output artifacts (recommended)

### `dist/ui-layer-registry.json`
- flattened list of layers
- grouped + ordered by category
- UI defaults (visible, opacity, min/max zoom)
- provenance pointers (STAC/DCAT/PROV)
- governance flags (license, sensitivity, CARE notes)
- optional: AI context metadata (tags, disclaimers)

### `dist/ui-layer-registry.lock.json`
- deterministic digests for each layer manifest (canonicalized)
- compiled registry digest
- build metadata:
  - gate version
  - schema version
  - policy pack version
- supports:
  - rollbacks
  - audit diffs (“what changed in UI-visible reality?”)

---

## 🧩 UI integration (how the registry is consumed)

### Layer Panel (2D + 3D)
- **MapLibre** for 2D map rendering
- **Cesium** for 3D globe / terrain layers
- one unified “Layers” UI that can host:
  - map layers
  - story overlays
  - 3D tilesets
  - pulse thread overlays

### Provenance UX (non-negotiable)
When a user toggles layers:
- show each active layer in a **Layer Provenance** panel:
  - source + license
  - processing summary
  - “view metadata” jump (STAC/DCAT/PROV)
- exports / shares carry attribution automatically

> [!TIP]
> The registry should make it *hard* to forget provenance by making it *impossible* to register a layer without it.

---

## 🧠 How this example “uses all the KFM docs” (crosswalk)

| 📄 Project file | What it contributes | How it shows up here |
|---|---|---|
| **KFM – Comprehensive UI System Overview** | React UI, MapLibre+Cesium split, timeline, story mode, Focus Mode citations, a11y | Registry contains render engine + a11y + timeline/stories integration |
| **KFM – Comprehensive Technical Documentation** | “no black box”, “map behind the map”, standards-first, map tech stack | Gate enforces provenance pointers + UI contract |
| **KFM – Comprehensive Architecture, Features, and Design** | governance, policy pack, layer provenance panel, sensitivity handling | Gate policy rules + sensitivity fields + provenance UI expectations |
| **KFM – AI System Overview** | provenance-enforced AI, audit logs, drift checks, “always cites sources” | Registry outputs AI context bundle + provenance pointers |
| **KFM Data Intake – Technical & Design Guide** | pipeline order, “no bypassing catalogs”, examples like real-time river gauges | Manifests reference API endpoints but still require DCAT/STAC/PROV |
| **KFM – Latest Ideas & Future Proposals** | PMTiles + GeoParquet packaging, hashed artifacts, 3D/AR expansion | Registry supports packaged layers + immutable artifact references |
| **Innovative Concepts to Evolve KFM** | 4D/AR narratives, future interaction modes, immersive mapping | Registry supports layer “types” beyond classic GIS layers |
| **Additional Project Ideas** | Pulse Threads, Conceptual Attention Nodes, artifact registry patterns | Registry supports pulse overlays + concept tags + lockfiles |
| **AI Concepts & more (portfolio)** | deep AI references (agents, RAG, humanism, reliability) | informs Focus Mode + governance posture |
| **Data Management (portfolio)** | metadata architecture, CI/CD patterns, privacy ideas | informs schema/policy checks and reproducible compilation |
| **Maps / WebGL / Virtual Worlds (portfolio)** | WebGL + mapping references, projections, rendering practices | informs render engine fields + CRS + 2D/3D constraints |
| **Various programming languages & resources (portfolio)** | engineering reference library, secure/reliable patterns | informs gate runner quality + maintainability |

---

## ✅ Definition of Done: adding a new UI layer

When you add a new layer, the PR should include:

- [ ] `layers/<id>.layer.yaml` (manifest)
- [ ] any style artifacts referenced by the manifest
- [ ] valid STAC/DCAT/PROV pointers (or stubs for provisional/streaming, if policy allows)
- [ ] license + attribution
- [ ] sensitivity classification + CARE notes
- [ ] a11y label + legend/popup behavior
- [ ] passes gate: schema + policy + performance budgets
- [ ] (if story-related) story node references + citations
- [ ] (if large) packaged artifacts (PMTiles/tileset) and hashes

---

## 🔭 Extension ideas (optional)

- ⏳ **Timeline-driven layers**: registry includes time windows + default visibility per era
- 🧊 **3D Tiles registry entries**: tilesets for built environment / terrain overlays
- 📲 **Offline packs**: compile a pack manifest from the registry for field/classroom use
- 🧠 **Conceptual lenses**: “Conceptual Attention Nodes” that activate bundles of layers + stories
- ⚡ **Pulse Threads**: live narrative overlays that are still provenance-bound

---

## 📚 Reference packs (not required to run this example)

These are included in the project’s document set to inform implementation depth:

- 🤖 **AI Concepts & more**: curated AI texts (agents, ML, digital humanism)
- 🗃️ **Data Management pack**: data engineering + CI/CD + lakehouse patterns
- 🧭 **Maps/WebGL pack**: mapping + projections + webgl/virtual world references
- 🛠️ **Programming resources pack**: broad engineering references (security, languages, best practices)

---

## 🧷 TL;DR

**UI Layer Registry** is the contract between:
- the **catalog + provenance system** (STAC/DCAT/PROV)
- the **UI rendering engines** (MapLibre/Cesium)
- the **trust + ethics model** (FAIR+CARE)
- the **AI assistant** (Focus Mode with citations)

…and the **gate** makes that contract enforceable ✅

