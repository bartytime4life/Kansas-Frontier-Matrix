<div align="center">

# 🧭 UI__STORY_NODE_CONTRACT

**A NASA-grade, governance-first contract for how “Story Nodes” are authored, packaged, rendered, versioned, and audited in the Kansas Frontier Matrix UI.**

<!-- Badges (safe to delete if you prefer no external assets) -->
![Status](https://img.shields.io/badge/status-DRAFT-orange)
![Contract](https://img.shields.io/badge/contract-UI%20%E2%87%84%20Story%20Nodes-blue)
![Focus%20Mode](https://img.shields.io/badge/focus%20mode-version%20lock%20%2B%20diff-purple)
![Map](https://img.shields.io/badge/map-MapLibre-informational)
![3D](https://img.shields.io/badge/3D-Cesium%20(optional)-informational)

</div>

---

## 🧠 Why this exists

Story Nodes are **machine-ingestible storytelling bundles**: narrative + map/3D state + evidence links + governance metadata. They are consumed by the UI, but must remain **reproducible**, **auditable**, and **safe** across versions.

This contract ensures:

- ✅ **Stable authoring format** (writers + engineers can collaborate)
- ✅ **Deterministic rendering** (same Story Node + same version → same experience)
- ✅ **Focus Mode reproducibility** (lock a version; freeze layers/panels; record telemetry)
- ✅ **Governance hooks** (FAIR+CARE labels, sensitivity, redaction flags, provenance)
- ✅ **Security by design** (no script injection; allow-listed assets; sandboxed execution)

---

## 🧾 Normative language

- **MUST** / **MUST NOT** = hard requirement  
- **SHOULD** / **SHOULD NOT** = strong recommendation  
- **MAY** = optional / implementation-specific

---

## 🗺️ Contract overview

### ✅ What the UI receives (runtime bundle)

The UI consumes a **StoryNodeBundle** (JSON) compiled from authoring artifacts:

- `narrative.md` (human narrative)
- `config.json` (machine controls: map scenes, camera, layers, panels)
- `assets/` (media + geometry)
- `provenance.*` (optional, but strongly recommended for traceability)

### ✍️ What authors edit (authoring bundle)

Authors work in a folder that contains:

- `narrative.md` with YAML frontmatter
- `config.json` describing scenes/beats
- `assets/` and `attachments/` for referenced files

### 🔁 How it becomes runtime

A build step transforms authoring → runtime:

- validate schemas  
- render markdown to AST/HTML  
- build asset manifest + hashes  
- emit `story_node.json` (the contract object)

---

## 🧱 Directory layout

> The repo supports both **authoring** (docs/reports) and **runtime** (web/story_nodes).  
> The UI MUST rely on the runtime bundle, not raw authoring files, in production.

### 📁 Authoring location

```text
📁 docs/
  📁 reports/
    📁 story_nodes/
      📁 draft/
        📁 <story_node_id>/
          📄 narrative.md
          📄 config.json
          📁 assets/
          📁 attachments/
      📁 published/
        📁 <story_node_id>/
          📄 narrative.md
          📄 config.json
          📁 assets/
          📁 attachments/
    📄 story_node_asset_index.yaml   (optional but recommended)
```

### 🌐 Runtime build output (UI-served)

```text
📁 web/
  📁 story_nodes/
    📁 <story_node_id>/
      📁 <version_id>/              # immutable
        📄 story_node.json           # ✅ UI contract input
        📁 assets/
        📁 attachments/
      📄 latest.json                 # pointer → latest version_id
```

---

## 🆔 Core identifiers

### Story Node ID

- **`story_node_id` MUST be stable** (slug-like): `kansas_from_above`
- Allowed: `a-z`, `0-9`, `_`, `-`
- MUST NOT encode versions inside the ID.

### Version ID

Version ID supports two compatible approaches:

- **Semver**: `1.0.0`, `1.1.0`, `2.0.0`
- **Monotonic**: `0001`, `0002`, `0003` (friendly for humans)
- **Commit hash** is allowed but SHOULD be mapped to a human label.

---

## 🧩 The StoryNodeBundle contract (runtime JSON)

### TypeScript interface (UI-facing)

```ts
export type StoryNodeId = string;
export type StoryNodeVersionId = string;

export interface StoryNodeBundle {
  meta: StoryNodeMeta;
  content: StoryNodeContent;          // rendered narrative + optional beat-linked segments
  config?: StoryNodeConfig;           // scenes/beats: camera, layers, panels
  assets: StoryNodeAssetManifest;     // files, hashes, mime, sizes
  lineage: StoryNodeLineage;          // predecessor/successor/latest/deprecated
  deps: StoryNodeDependencies;        // registry + dataset locks
  integrity: StoryNodeIntegrity;      // hashing, build stamp
  governance?: StoryNodeGovernance;   // FAIR+CARE, sensitivity, redaction flags
  evidence?: EvidenceRef[];           // STAC/DCAT/PROV/docs citations
}
```

### Required objects (minimum viable)

| Field | Required | Purpose |
|---|---:|---|
| `meta` | ✅ | identity, title, summary, time/space scope |
| `content` | ✅ | narrative payload the UI renders |
| `assets` | ✅ | allow-listed assets + integrity hashes |
| `lineage` | ✅ | version strip + diff navigation |
| `deps` | ✅ | version-lockable dependencies |
| `integrity` | ✅ | reproducibility + debugging |

---

## 🧾 `meta` contract

```json
{
  "id": "kansas_from_above",
  "title": "Kansas From Above",
  "summary": "A flyover story node connecting imagery, terrain, and historical layers.",
  "stage": "published",
  "version_id": "0003",
  "version_label": "v0.3",
  "created_at": "2025-12-21T00:00:00Z",
  "updated_at": "2026-01-06T00:00:00Z",
  "authors": [{ "name": "KFM Team", "role": "author" }],
  "tags": ["3d", "terrain", "imagery", "timeline"],
  "time_range": { "start": "1860-01-01", "end": "1900-12-31" },
  "bbox": [-102.05, 36.99, -94.59, 40.00]
}
```

### `meta` rules

- `title` MUST be human-readable.
- `stage` MUST be one of: `draft | published | archived`.
- `time_range` SHOULD exist if the Story Node includes timeline narratives.
- `bbox` SHOULD exist for map navigation + discovery.

---

## 📝 `content` contract

The UI supports either:

- **`html`** (sanitized) OR
- **`mdast`** (preferred for interactive anchors)

```json
{
  "format": "mdast",
  "body": { "...": "mdast tree" },
  "reading_time_min": 8,
  "toc": [
    { "id": "intro", "label": "Intro" },
    { "id": "terrain", "label": "Terrain & Rivers" }
  ],
  "anchors": [
    {
      "id": "beat_02",
      "kind": "beat",
      "label": "Crossing the rivers",
      "target_scene_id": "scene_02"
    }
  ]
}
```

### Content security rules

- UI MUST sanitize any HTML output (strip scripts/events, disallow iframes by default).
- Story Node markdown MUST NOT be able to execute arbitrary JS.
- If custom JS is required (e.g., `cesium_scene.js`), it MUST be treated as **trusted code**:
  - only loaded from same origin
  - only after governance approval
  - only in production builds that enable it (feature flag)

---

## 🎬 `config` contract (scenes/beats)

### Concept

A Story Node is a sequence of **scenes** (beats). Each scene defines:

- camera/view state
- layer visibility + filters
- optional annotations/callouts
- panel state (charts/tables)

### Minimal config.json example

```json
{
  "engine": "hybrid",
  "initial_scene_id": "scene_01",
  "scenes": [
    {
      "id": "scene_01",
      "label": "Intro Fly-in",
      "time": { "start": "1860-01-01", "end": "1860-12-31" },
      "camera": {
        "mode": "3d",
        "lat": 38.5,
        "lon": -98.0,
        "height_m": 900000,
        "heading_deg": 0,
        "pitch_deg": -35
      },
      "layers": [
        { "layer_id": "base_satellite", "visible": true, "opacity": 1.0 },
        { "layer_id": "hydrology_major_rivers", "visible": true, "opacity": 0.8 }
      ],
      "panels": [
        { "id": "legend", "type": "legend", "open": true }
      ]
    }
  ]
}
```

### Config rules

- `engine` MUST be one of: `maplibre | cesium | hybrid`.
- Each scene MUST have a unique `id`.
- `layer_id` MUST reference a known Layer Registry entry.
- `time` SHOULD exist if the UI has a timeline slider enabled for this Story Node.

---

## 🧱 Asset manifest contract

The bundle MUST include a **manifest** describing every file the UI may load.

```json
{
  "version": 1,
  "items": [
    {
      "path": "assets/cover.png",
      "mime": "image/png",
      "bytes": 183210,
      "sha256": "…",
      "role": "cover",
      "alt": "Kansas terrain shaded relief"
    },
    {
      "path": "assets/annotations.geojson",
      "mime": "application/geo+json",
      "bytes": 48210,
      "sha256": "…",
      "role": "annotations"
    }
  ]
}
```

### Asset rules

- UI MUST load assets only if they exist in `assets.items[]`.
- UI MUST refuse to load paths containing:
  - `..`
  - absolute paths
  - remote URLs (unless explicitly allowed by policy)
- Each asset SHOULD include `alt` when visual.
- Allowed mime-types SHOULD be allow-listed (see below).

### Recommended allow-list (baseline)

- images: `image/png`, `image/jpeg`, `image/webp`, `image/svg+xml`
- vector/data: `application/geo+json`, `application/json`, `text/csv`
- 3D: `model/gltf+json`, `model/gltf-binary` (or `application/octet-stream` with explicit role)
- documents: `application/pdf` (if needed; note it impacts UX)

---

## 🧬 Version lineage contract (for the Version Strip UI)

```json
{
  "predecessor_version_id": "0002",
  "successor_version_id": null,
  "latest_version_id": "0003",
  "deprecated": false,
  "deprecation_reason": null
}
```

### UI requirements (Version Strip)

The UI MUST support a **version strip** for Story Nodes:

- show predecessor → current → successor
- highlight **latest**
- mark **deprecated** versions
- allow:
  - click to switch version
  - hover preview (summary + timestamp)
  - open diff viewer

Keyboard SHOULD support:
- `[` / `]` or arrow keys to move versions
- `d` to open diff

---

## 🔒 Focus Mode integration (version lock contract)

### Behavior goals

When a Story Node version is locked:

- layers MUST freeze (no “latest tile” drift)
- panels MUST freeze (cached queries / dataset versions)
- UI MUST stamp the session with:
  - story_node_id
  - version_id
  - dependency versions
  - timestamp

### API surface (recommended)

> The backend shape may vary, but the UI contract assumes endpoints like:

```http
POST /focus/story-node/{story_node_id}/lock-version/{version_id}
POST /focus/story-node/{story_node_id}/unlock
GET  /story-nodes/{story_node_id}/versions
GET  /story-nodes/{story_node_id}/diff?from={v1}&to={v2}
```

### Focus telemetry events (minimum)

```json
{
  "ts": "2026-01-08T19:12:03.112Z",
  "event": "version_locked",
  "story_node_id": "kansas_from_above",
  "version_id": "0003",
  "session_id": "…",
  "deps": { "layer_registry_version": "2026.01.06", "symbol_registry_version": "2026.01.06" }
}
```

Event names the UI SHOULD emit:

- `storynode_opened`
- `beat_entered`
- `beat_completed`
- `version_navigated`
- `version_locked`
- `version_unlocked`
- `diff_opened`
- `diff_exported`

---

## 🧾 Dependency locking (`deps`)

```json
{
  "layer_registry_version": "2026.01.06",
  "symbol_registry_version": "2026.01.06",
  "dataset_versions": [
    { "id": "stac:item:landsat_scene_123", "version": "0007" }
  ],
  "api_contract_version": "1"
}
```

### Rules

- UI MUST treat `deps.*` as part of reproducibility.
- In Focus Mode, UI MUST display dependency versions in an “Info” panel.

---

## 🧷 Evidence references (`evidence[]`)

Evidence objects connect narrative claims to data and provenance:

```json
{
  "kind": "stac_item",
  "id": "landsat_scene_123",
  "label": "Landsat scene over central Kansas",
  "href": "catalogs/stac/items/landsat_scene_123.json",
  "citation": "USGS (YYYY). Landsat…",
  "confidence": "high"
}
```

Supported `kind` values:

- `stac_item`
- `stac_collection`
- `dcat_dataset`
- `prov_activity`
- `doc`
- `url`

Rules:

- Evidence SHOULD include `citation` for scholarly traceability.
- UI SHOULD render Evidence as a sidebar “Sources” list.

---

## 🧿 Symbols & legends (narrative ↔ map)

Story Nodes SHOULD reference icons from the Symbol Registry by ID, e.g.:

```md
The river reached {symbol:flood_highwater} levels in the spring thaw.
```

UI responsibilities:

- replace `{symbol:*}` with SVG/inline symbol
- auto-add used symbols to the legend
- log symbol usage to telemetry for explainability

---

## ♿ Accessibility & inclusive mapping rules

Story Nodes MUST be accessible:

- narrative MUST provide alt text for images
- legends MUST not rely on color alone (use shape/pattern)
- interactive content MUST be keyboard reachable
- UI MUST provide ARIA labels for custom controls

Recommended (baseline):

- WCAG 2.1 AA contrast targets for UI chrome
- captions for videos when used
- “reduced motion” mode respects OS preference

---

## 🛡️ Security constraints

### Content sanitization

- UI MUST sanitize markdown-rendered HTML
- UI MUST strip:
  - `<script>`, inline handlers (`onClick=...`)
  - untrusted iframes
  - `javascript:` URLs

### Query safety (graph + SQL)

- UI MUST NOT issue unbounded traversals
- UI MUST NOT build query strings via concatenation
- UI MUST use parameter binding for filters + ordering

### Asset safety

- UI MUST enforce allow-listed mime-types
- UI MUST enforce size thresholds (configurable)
- UI SHOULD verify `sha256` before use (esp. for 3D assets)

---

## 🧪 Scientific integrity (for analysis-heavy Story Nodes)

If a Story Node makes statistical/modeling claims:

- SHOULD expose uncertainty (CI/credible interval)
- SHOULD show residuals/outliers or diagnostics where relevant
- SHOULD avoid cherry-picking and undisclosed multiple testing
- MUST provide provenance for derived metrics (inputs + method + date)

UI support MAY include:

- a “Methods” collapsible panel
- an “Uncertainty” toggle on charts

---

## 🧰 Validation & CI gates

A Story Node MUST pass:

- schema validation (`narrative.md` frontmatter + `config.json`)
- asset validation (manifest exists, mime-types allowed, hashes computed)
- link validation (evidence refs resolve)
- governance validation (required labels present for published)
- security scanning (no forbidden HTML/JS patterns)

---

## 🧪 Example: `narrative.md` (authoring)

```md
---
id: kansas_from_above
title: "Kansas From Above"
stage: published
version_id: "0003"
version_label: "v0.3"
summary: "A flyover story node connecting imagery, terrain, and historical layers."
time_range:
  start: 1860-01-01
  end: 1900-12-31
bbox: [-102.05, 36.99, -94.59, 40.00]
engine: hybrid
config_path: ./config.json
cover: ./assets/cover.png
tags: [3d, terrain, hydrology, timeline]
governance:
  sensitivity_level: low
  care_label: "CARE-L0"
  license: "MIT"
---

## Intro

Welcome to Kansas, from above. {symbol:compass}

## Terrain & Rivers

We follow the hydrology lines as settlements grow.
```

---

## 🧰 Example: minimal `story_node.json` (runtime)

```json
{
  "meta": { "id": "kansas_from_above", "title": "Kansas From Above", "summary": "…", "stage": "published", "version_id": "0003" },
  "content": { "format": "html", "body": "<h2>Intro</h2>…", "reading_time_min": 8, "toc": [] },
  "config": { "engine": "hybrid", "initial_scene_id": "scene_01", "scenes": [] },
  "assets": { "version": 1, "items": [] },
  "lineage": { "predecessor_version_id": "0002", "successor_version_id": null, "latest_version_id": "0003", "deprecated": false },
  "deps": { "layer_registry_version": "2026.01.06", "symbol_registry_version": "2026.01.06", "dataset_versions": [], "api_contract_version": "1" },
  "integrity": { "build_id": "2026-01-08T00:00:00Z", "content_sha256": "…", "config_sha256": "…", "assets_sha256": "…" },
  "governance": { "sensitivity_level": "low", "care_label": "CARE-L0", "license": "MIT" },
  "evidence": []
}
```

---

## 🗂️ Cross-project references (the “use all project files” checklist) 📚

> These files informed the contract’s principles around reproducibility, visualization, security, mapping UX, data governance, and scalable analytics.

### 🧩 Core KFM docs
- `Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design.docx`
- `Latest Ideas.docx`
- `Other Ideas.docx`
- `MARKDOWN_GUIDE_v13.md.gdoc`

### 🗺️ Geospatial & mapping
- `python-geospatial-analysis-cookbook.pdf`
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`

### 🧪 Modeling, stats, analysis
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `Understanding Statistics & Experimental Design.pdf`
- `regression-analysis-with-python.pdf`
- `Regression analysis using Python - slides-linear-regression.pdf`
- `graphical-data-analysis-with-r.pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`
- `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf`
- `Understanding Machine Learning: From Theory to Algorithms.pdf` *(if present in repo/library)*

### 🧱 Data systems & governance
- `Scalable Data Management for Future Hardware.pdf`
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `Data Spaces.pdf`
- `Spectral Geometry of Graphs.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`

### 🧑‍⚖️ Ethics, society, governance
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`
- `Introduction to Digital Humanism.pdf`
- `Principles of Biological Autonomy - book_9780262381833.pdf`

### 🛡️ Security & hardening
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

### 🧰 Web/UI engineering + reference shelves
- `responsive-web-design-with-html5-and-css3.pdf`
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `A programming Books.pdf`
- `B-C programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`

---

## ✅ Acceptance criteria

A Story Node is “UI-contract compliant” when:

- [ ] Compiles into `story_node.json`
- [ ] Passes schema validation (meta/content/config/assets/lineage/deps/integrity)
- [ ] Renders deterministically (same inputs → same state)
- [ ] Supports version strip + diff navigation
- [ ] Focus Mode locks version + dependency versions + logs telemetry
- [ ] Assets are allow-listed + hashed + referenced via manifest
- [ ] Content is sanitized and safe
- [ ] Governance labels exist for published nodes

---

## 🧭 Changelog

- **1.0.0 (2026-01-08)** — Initial contract definition (UI ↔ Story Node ↔ Focus Mode)


