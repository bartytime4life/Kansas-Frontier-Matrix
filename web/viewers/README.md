<div align="center">

# 🗺️🛰️ KFM Web Viewers — `web/viewers/`

**Browser-first geospatial viewers for the Kansas Frontier Matrix (KFM)**  
🗺️ 2D Explorer (MapLibre) • 🛰️ 3D Globe (Cesium) • 📚 Story Nodes • 🔍 Focus Mode • 🧾 Provenance UI

<img alt="Status" src="https://img.shields.io/badge/status-active%20development-brightgreen" />
<img alt="Engines" src="https://img.shields.io/badge/engines-MapLibre%20%7C%20Cesium-blue" />
<img alt="Modes" src="https://img.shields.io/badge/modes-explore%20%7C%20story%20%7C%20focus-purple" />
<img alt="Catalog-first" src="https://img.shields.io/badge/catalog-first-STAC%20%7C%20DCAT%20%7C%20PROV-6f42c1" />
<img alt="Governance" src="https://img.shields.io/badge/governance-FAIR%20%2B%20CARE%20%2B%20Sovereignty-2ea043" />
<img alt="Security" src="https://img.shields.io/badge/security-no%20secrets%20%7C%20sanitize%20untrusted%20content-red" />

</div>

> [!IMPORTANT]
> **KFM invariant (non‑negotiable ordering):**  
> **ETL → STAC/DCAT/PROV Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**  
> Viewers are **UI**. They are **contract consumers**, not a backdoor to the graph or raw storage.

---

## 🔗 Quick links

| What | Link |
|---|---|
| 🌾 Back to `web/` | `../README.md` |
| 🎨 Static assets rules | `../assets/README.md` |
| 🗂️ Frontend data assets rules | `../data/README.md` |
| 🧩 Story Nodes runtime rules | `../story_nodes/README.md` |
| 🧾 Report an issue | `https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/new/choose` |

---

<details>
<summary><strong>🧭 Table of contents</strong></summary>

- [What lives in `web/viewers/`](#-what-lives-in-webviewers)
- [Non-negotiables](#-non-negotiables)
- [Where viewers fit in the KFM pipeline](#-where-viewers-fit-in-the-kfm-pipeline)
- [Viewer contract](#-viewer-contract-one-state-model-many-engines)
- [Viewer lineup](#-viewer-lineup)
  - [MapLibre viewer (2D)](#-maplibre-viewer-2d)
  - [Cesium viewer (3D)](#-cesium-viewer-3d)
  - [Hybrid shell](#-hybrid-shell)
  - [Capability matrix](#-capability-matrix)
- [Suggested folder layout](#-suggested-folder-layout)
- [Contracts & schemas](#-contracts--schemas)
- [Data inputs & formats](#-data-inputs--formats)
- [Story Nodes + Focus Mode integration](#-story-nodes--focus-mode-integration)
- [Provenance & governance UI](#-provenance--governance-ui)
- [Performance budgets & caching](#-performance-budgets--caching)
- [Accessibility & mobile mapping](#-accessibility--mobile-mapping)
- [Security & privacy](#-security--privacy)
- [Local development](#-local-development)
- [Testing & CI gates](#-testing--ci-gates)
- [Roadmap](#-roadmap)
- [Project library influence map](#-project-library-influence-map)

</details>

---

## 🧭 What lives in `web/viewers/`

This folder is the **front-end visualization layer** for KFM: the pieces that turn **cataloged, governed artifacts** (layers, events, Story Nodes, 3D assets, evidence bundles) into an **interactive map / globe experience**.

### ✅ Core promises

- **One dataset, many lenses**: the same cataloged artifacts can be explored in 2D, 3D, and narrative modes.
- **Catalog-driven UX**: viewers are powered by **catalog + provenance** patterns (STAC/DCAT/PROV), not hard-coded layers.
- **Story-first exploration**: Story Nodes provide curated waypoints; Focus Mode provides deep dives with evidence panels.
- **Governed UI boundary**: the viewer consumes data through **contracted endpoints or catalog pointers** (no direct coupling to graph DB).

> [!TIP]
> The viewer should render what is present, and **degrade gracefully** when data is missing, redacted, gated, or offline.

---

## 🧱 Non-negotiables

### 1) Pipeline ordering is absolute
Viewers never leapfrog upstream governance:

- 🚫 no “grab a file from a bucket and show it”
- 🚫 no “pull from Neo4j directly”
- ✅ render from **API contracts** or **catalog pointers** (STAC/DCAT/PROV)

### 2) No secrets. Ever.
Anything in `web/` is effectively world-readable.

- 🚫 no API keys that grant privileged access
- 🚫 no internal endpoints or private dataset URLs baked into styles/manifests
- ✅ if it’s sensitive, it must be gated/redacted upstream

### 3) Evidence-first UI
If the UI can show it, the UI must be able to answer:

- what is it?
- where did it come from?
- what changed it?
- what license governs it?
- what uncertainty / caveats apply?

### 4) Stable identifiers (IDs are contracts)
IDs are UI state keys and deep-link keys. Treat them like public APIs:

- **stable layer IDs** (don’t encode changing facts into IDs)
- versions live in metadata (`version`, `run_id`, `stac:version`, `prov:wasGeneratedBy`)
- keep “display names” separate from IDs

### 5) Treat all external content as hostile input
Metadata, Story Node markdown, GeoJSON properties, SVG, and style JSON are all untrusted:

- sanitize/escape before rendering
- avoid unsafe DOM sinks (`innerHTML` from untrusted input)
- enforce strict URL allowlists when fetching remote assets

---

## 🧭 Where viewers fit in the KFM pipeline

```mermaid
flowchart LR
  DATA["🗃️ Data (raw/processed)"] --> CAT["🗂️ Catalogs (STAC/DCAT/PROV)"]
  CAT --> GRAPH["🕸️ Graph / Index (derived)"]
  CAT --> API["🛡️ API boundary (contracts + policy + redaction)"]
  API --> UI["🌐 Viewers (this folder)"]
  CAT --> UI
  UI --> STORY["📚 Story Nodes + Focus Mode (evidence-linked)"]
