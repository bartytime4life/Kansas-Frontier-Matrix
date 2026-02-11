# Kansas Frontier Matrix (KFM) — `web/` 🌐🗺️🧭

![React](https://img.shields.io/badge/ui-react-61DAFB?logo=react&logoColor=000)
![TypeScript](https://img.shields.io/badge/lang-typescript-3178C6?logo=typescript&logoColor=fff)
![MapLibre](https://img.shields.io/badge/maps-maplibre-1E1E1E?logo=mapbox&logoColor=fff)
![Provenance-first](https://img.shields.io/badge/provenance-first-success)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%2BCARE-aligned-purple)
![Trust Membrane](https://img.shields.io/badge/trust%20membrane-enforced-blue)
![Policy-as-Code](https://img.shields.io/badge/policy-as--code-OPA-blue)

> [!IMPORTANT]
> This is a **governed UI surface**. KFM’s “trust membrane” applies here:
>
> - **The web app must never access databases directly** (no “temporary” direct PostGIS/Neo4j connections, no embedded credentials, no client-side SQL/Cypher).
> - **All data access must go through the governed API** (which applies validation + policy checks).
> - **Every layer, Story Node, and AI answer must be inspectable** (provenance/citations), or the UI must **refuse / abstain**.

> [!NOTE]
> Some paths and scripts below are **recommended defaults** based on KFM’s canonical architecture docs and may differ in your repo. If a path is missing, treat it as **(not confirmed in repo)** and align it to the canonical layout in `docs/`.

---

## Table of contents

- [What lives in `web/`](#what-lives-in-web)
- [Core UX features](#core-ux-features)
- [Architecture at a glance](#architecture-at-a-glance)
- [Directory layout](#directory-layout)
- [Local development](#local-development)
- [Configuration](#configuration)
- [How the UI talks to KFM](#how-the-ui-talks-to-kfm)
- [Layers and domains](#layers-and-domains)
- [Story Nodes](#story-nodes)
- [Focus Mode AI](#focus-mode-ai)
- [Adding a new layer safely](#adding-a-new-layer-safely)
- [Testing](#testing)
- [Governance and sensitive information](#governance-and-sensitive-information)
- [Performance and accessibility](#performance-and-accessibility)
- [Troubleshooting](#troubleshooting)
- [Key internal references](#key-internal-references)

---

## What lives in `web/`

This directory contains the **KFM front-end application**: the interactive map + timeline UI, Story Node viewer, and the governed “Focus Mode” AI interface.

The KFM architecture treats the UI as a **read-and-explain** surface:

- it renders **maps and timelines**
- it exposes **dataset metadata + provenance**
- it provides **narrative Story Nodes**
- it provides **AI-assisted Q&A** with citations and auditability

If you are looking for ingestion, cataloging, or storage code, those live elsewhere in the repo (e.g., `pipelines/`, `data/`, `api/`, `policy/`) **(not confirmed in repo)**.

---

## Core UX features

### 🗺️ Map + timeline explorer
- 2D map with interactive layers (vector + raster)
- timeline slider / time scrubber for time-enabled layers
- click-to-inspect: feature popups link to dataset provenance and related entities

### 🧾 Provenance-first inspection
- “Dataset info” dialogs surface **source attribution + transformations**
- provenance/audit panel shows **PROV lineage** for layers, stories, and AI answers

### 📖 Story Nodes
- browse and read narrative Story Nodes (Markdown)
- Story Nodes can control map state (camera/time/layers) as users step/scroll

### 🤖 Focus Mode AI (governed)
- Q&A assistant that:
  - retrieves only from governed sources
  - returns answers with citations/footnotes
  - provides an “Audit” view of what evidence was used

---

## Architecture at a glance

```mermaid
flowchart LR
  subgraph UI["web/ (React UI)"]
    Map["Map View (MapLibre)"]
    Time["Timeline / Time Scrubber"]
    Layers["Layer Panel + Legend"]
    Prov["Provenance Panel"]
    Story["Story Node Viewer"]
    Focus["Focus Mode Chat + Audit"]
  end

  subgraph API["Backend API (governed)"]
    Catalog["Catalog (STAC/DCAT)"]
    ProvAPI["Provenance (PROV)"]
    Tiles["Tiles/Features/Timeseries endpoints"]
    Search["Search + Retrieval endpoints"]
    Policy["Policy Engine (OPA)"]
  end

  UI -->|HTTP(S)| API
  API --> Policy
  Catalog --> UI
  ProvAPI --> Prov
  Tiles --> Map
  Search --> Focus
  Story --> Map
  Story --> Time
```

> [!WARNING]
> **No “shortcut integrations.”** If a feature would require the UI to ingest raw files directly, or embed untracked data blobs, that violates KFM’s canonical data path and governance stance. Route it through pipeline → catalog/prov → API first.

---

## Directory layout

Recommended canonical layout (may differ) **(not confirmed in repo)**:

```text
web/
  README.md

  package.json
  tsconfig.json
  vite.config.* / webpack.config.*     # one of these (not confirmed in repo)
  public/
    index.html
    favicon.ico

  src/
    main.tsx
    App.tsx

    api/                               # typed API client(s) + fetch wrappers
      http.ts
      catalog.ts
      layers.ts
      provenance.ts
      focusMode.ts
      search.ts

    components/
      MapView.tsx
      Timeline.tsx
      LayerPanel.tsx
      Legend.tsx
      ProvenancePanel.tsx
      StoryNodeViewer.tsx
      FocusModeChat.tsx
      DatasetInfoDialog.tsx
      EntityDrawer.tsx                 # people/places/events explorer (recommended)

    routes/
      MapRoute.tsx
      StoryRoute.tsx
      FocusRoute.tsx
      ExperimentsRoute.tsx             # AI driving experiments (recommended)

    state/
      store.ts                         # Redux/Zustand/Context (not confirmed in repo)
      slices/                          # if Redux is used (not confirmed in repo)

    styles/
      global.css
      map.css

    utils/
      time.ts
      geo.ts
      accessibility.ts
```

---

## Local development

### Prerequisites
- Node.js LTS (version pinned in `.nvmrc` / `engines` if present) **(not confirmed in repo)**
- The KFM backend API running locally (often via Docker Compose) **(not confirmed in repo)**

### Install
```bash
cd web
npm install
```

### Run dev server
One of the following will exist (check `package.json`):

```bash
npm run dev
# or
npm start
```

### Build
```bash
npm run build
```

### Lint / format
```bash
npm run lint
npm run format
```

> [!TIP]
> If the repo uses `pre-commit`, run it before pushing to mirror CI gates:
>
> ```bash
> pre-commit run --all-files
> ```

---

## Configuration

### Environment variables

The UI should be configurable without code changes. Prefer `.env.local` for dev **(not confirmed in repo)**.

| Variable | Purpose | Example | Notes |
|---|---|---|---|
| `VITE_API_BASE_URL` or `REACT_APP_API_BASE_URL` | Base URL for governed API | `http://localhost:8000` | Choose the one your build tool supports |
| `VITE_TILES_BASE_URL` | Tile endpoint base | `http://localhost:8000/api/tiles` | Keep tiles behind the API |
| `VITE_PUBLIC_MODE` | Public vs internal UI toggles | `true` | Hide internal tools in public mode |
| `VITE_FOCUS_MODE_ENABLED` | Enable Focus Mode UI | `true` | Must remain governed + cite-or-abstain |
| `VITE_CESIUM_ENABLED` | Enable 3D mode | `false` | Optional (performance + complexity) |

> [!IMPORTANT]
> Never commit secrets into the frontend. If the UI needs auth, use token-based auth that can be rotated and is issued by the backend **(not confirmed in repo)**.

---

## How the UI talks to KFM

### 1) Catalog-driven UI (STAC/DCAT-first)
The UI should **discover** datasets/layers via the catalog rather than hardcoding.

Recommended flow:
1. `GET /api/v1/catalog` (or similar) returns dataset/layer descriptors
2. The Layer Panel builds categories + search from those descriptors
3. Layer toggles use IDs that resolve back to catalog/provenance records

### 2) Tiles + features
For map rendering, prefer server-produced tiles:
- vector tiles (e.g., `*.pbf`) for interactive layers
- raster tiles for heavy imagery and time-slices

Example tile pattern (your repo may differ):
- `/api/tiles/<layerId>/{z}/{x}/{y}.pbf` **(not confirmed in repo)**

### 3) Provenance everywhere
UI components that must have provenance hooks:
- Layer Panel (metadata + provenance link)
- Dataset Info dialog (source, publisher, transformations)
- Story Node viewer (citations + referenced datasets)
- Focus Mode (answer footnotes + audit panel)

### 4) Knowledge-graph-backed entity navigation (people/places/events)
KFM’s knowledge graph links:
- people ↔ places ↔ events ↔ datasets ↔ story nodes

Recommended UI surface:
- an **Entity Drawer** / **Entity Page** that shows:
  - summary + timeline
  - related Story Nodes
  - related datasets/layers
  - map zoom-to geometry (if permitted by policy)

---

## Layers and domains

KFM’s unified blueprint explicitly supports integrating **environment, infrastructure, and communities** into one governed interface. The web app must make those domains navigable, comparable through time, and provenance-backed.

### Domain coverage checklist (UI-ready)

> [!NOTE]
> This list captures **required UI integration targets** mentioned in KFM planning docs and prior gap reviews. Some datasets may exist only as planned inventory until pipelines land.

- [ ] **Land ownership / cadastral**
  - parcel boundaries / cadastral overlays (restricted where necessary)
  - PLSS township/range/section browsing
  - “ownership” display must avoid PII unless explicitly authorized
- [ ] **Historical figures**
  - Person entities, affiliations, events, and locations (knowledge graph)
  - link people ↔ story nodes ↔ evidence bundles
- [ ] **Hydrology**
  - rivers/streams/watersheds
  - groundwater / aquifers
  - water quality sampling sites (map + time series)
- [ ] **Geology**
  - formations, aquifers, hazards (where available)
  - geology ↔ land use ↔ hydrology comparisons
- [ ] **Disasters**
  - disaster declarations (events + geography)
  - flood mapping / inundation (where available)
  - drought intensity (time-scrubbable)
- [ ] **Air quality / smoke**
  - pollutant layers (NO₂, PM2.5 proxies, etc.)
  - smoke indicators where available (often remote sensing derived)
- [ ] **Soil**
  - SSURGO-derived soil properties
  - soil moisture + drought overlays
- [ ] **Fires**
  - wildfire perimeters (time-filtered)
  - burn history and associated environmental impacts
- [ ] **Roads**
  - transportation basemaps (modern + historical when available)
  - roads as context for settlement and hazard response
- [ ] **Trains / rail**
  - rail corridors (modern/historical)
  - Story Node tie-ins (railroads ↔ settlement expansion)
- [ ] **AI driving experiments**
  - internal-only “Experiments” route for evaluation harnesses:
    - retrieval tuning / ablation comparisons
    - citation coverage metrics
    - sandboxed model comparisons (no policy bypass)

### Recommended layer taxonomy in the UI

| Category | Examples | Expected UI affordances |
|---|---|---|
| Land & Ownership | PLSS, parcels, land cover | high-sensitivity flags, access gating, export watermarking |
| People & History | historical figures, events, story steps | entity drawer, timeline, citations |
| Water | hydrology, reservoirs, water quality | time series charts + map |
| Earth | geology, soils | compare panels, legends, scale notes |
| Hazards | disasters, drought, floods, fires | time scrubber, event lists, filters |
| Air | air quality proxies, smoke indicators | time series, disclaimers, uncertainty notes |
| Infrastructure | roads, rail | basemap overlays, historical map comparison |
| Experiments | AI evaluation harness | internal-only gating, audit logs |

---

## Story Nodes

Story Nodes are Markdown narratives that the UI renders as a guided experience:
- each step can control map/time/layers
- each step must cite sources
- Story Node metadata (author/date/sources) should be displayed for attribution

Recommended content locations **(not confirmed in repo)**:
- `docs/stories/<story>.md`
- `docs/stories/<story>_meta.json`
- `docs/stories/media/*`

> [!IMPORTANT]
> Treat Story Nodes as **governed content**. The UI must:
> - refuse to render “official/published” badges unless validated
> - surface citations prominently
> - route sensitive topics for governance review triggers

---

## Focus Mode AI

Focus Mode is not a generic chatbot. It is:
- retrieval-backed
- policy constrained
- provenance-forward (“cite-or-abstain”)

### UI requirements
- Always show:
  - citations/footnotes to sources
  - an Audit view (what was retrieved, what policy gates applied)
- Never allow:
  - hidden prompts that bypass policy
  - direct DB access
  - responses without evidence for factual claims

### Recommended internal tooling
- “Evaluation harness” UI that runs canned questions and reports:
  - citation coverage
  - abstention rates
  - sensitivity policy triggers
  - latency (p50/p95)

---

## Adding a new layer safely

> [!WARNING]
> A new UI layer is not “just a front-end change.” In KFM it is a **governed artifact** that must be:
> pipeline-built → cataloged → provenance-logged → policy-labeled → API-served → UI-rendered.

### Definition of Done (new layer)

- [ ] Dataset ingested via pipeline (raw → processed)
- [ ] STAC/DCAT metadata created/updated
- [ ] PROV lineage created/updated
- [ ] Policy labels assigned (public/restricted + sensitivity tags)
- [ ] API exposes tiles/features/timeseries endpoints
- [ ] UI renders the layer and shows:
  - legend
  - dataset info dialog
  - provenance panel linkage
- [ ] E2E test:
  - toggle layer → provenance visible
  - story node references render citations
  - Focus Mode citations resolve (if used)

### Recommended UI implementation steps

1. Add/verify catalog entry exists (don’t hardcode)
2. Add layer renderer plugin (vector/raster/time)
3. Add legend + units + uncertainty notes
4. Ensure dataset info dialog resolves provenance
5. Add time-dimension support (if temporal)
6. Add test coverage (unit + e2e)

---

## Testing

Recommended test layers **(not confirmed in repo)**:

### Unit tests
- Component rendering, reducers/store, utility functions
- Citation rendering edge cases
- “restricted layer” gating behavior (UI hides what policy denies)

### Integration tests
- API contract mocks (catalog/layers/provenance)
- layer toggle → fetch tiles → show legend → show provenance

### End-to-end tests
Critical flows:
- layer toggle → provenance panel shows attribution
- story node load → citations resolve
- Focus Mode question → citations resolve + Audit panel shows retrieval set

---

## Governance and sensitive information

KFM adheres to **FAIR** + **CARE**, which has concrete UI implications:

- Avoid publishing **precise locations** of sacred/vulnerable sites.
- If content is culturally restricted or sensitive:
  - generalize (rounding, bounding boxes, aggregation)
  - redact fields
  - require governance review

> [!IMPORTANT]
> When in doubt: **generalize, redact, and flag for governance review** rather than exposing details in the UI.

---

## Performance and accessibility

### Performance expectations
- Prefer vector tiles for heavy interactive layers
- Avoid rendering huge GeoJSON blobs client-side
- Use caching and request deduplication (e.g., query cache) **(not confirmed in repo)**

### Accessibility requirements
- Keyboard-navigable UI controls
- Proper heading hierarchy and landmarks
- Legends and charts must be readable with assistive tech
- Respect `prefers-reduced-motion` for scrollytelling / animations

---

## Troubleshooting

### Common issues
- **Blank map**: confirm API base URL and tile endpoints; check CORS.
- **Layers don’t appear**: confirm catalog returns entries and policy allows visibility.
- **Provenance panel empty**: confirm PROV endpoints and dataset IDs match catalog IDs.
- **Focus Mode has no citations**: treat as failure; verify retrieval endpoints + evidence store.

### Debug tips
- Add a “debug overlay” in dev mode to show:
  - active layer IDs
  - current time extent
  - last API calls and status codes
  - policy decision summaries (allow/deny reasons)

---

## Key internal references

If these paths differ, treat as **(not confirmed in repo)** and align to canonical standards in `docs/`.

- Repo governance + CI gates:
  - `../.github/README.md`
- Docs standards:
  - `../docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md`
  - `../docs/standards/KFM_CHATGPT_WORK_PROTOCOL.md`
- Story Node template:
  - `../docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contracts:
  - `../docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance:
  - `../docs/governance/ROOT_GOVERNANCE.md`
  - `../docs/governance/ETHICS.md`
  - `../docs/governance/SOVEREIGNTY.md`

---

<details>
  <summary>Maintainers: UI gatekeeping rules (recommended)</summary>

- Do not merge UI changes that:
  - add a new layer without dataset metadata + provenance links
  - render restricted datasets in public mode
  - degrade citation/audit UX for Focus Mode
- Require e2e coverage for:
  - provenance panel behavior
  - story node citation rendering
  - Focus Mode “cite-or-abstain” behavior

</details>