# 🧪 UI Fixtures

![Scope](https://img.shields.io/badge/scope-UI%20fixtures-6f42c1?style=flat-square)
![Contract-First](https://img.shields.io/badge/contract--first-required-0b74de?style=flat-square)
![Evidence-First](https://img.shields.io/badge/evidence--first-required-f39c12?style=flat-square)
![Provenance](https://img.shields.io/badge/provenance-keep%20it%20traceable-ff6f00?style=flat-square)
![KFM](https://img.shields.io/badge/KFM-living%20atlas%20(UI%20stage)-2ea44f?style=flat-square)

> Deterministic **sample payloads + static assets** used to build, demo, and test the KFM web UI 🗺️✨  
> Think: **“What does the UI consume?”** and **“What states must the UI handle?”** — without needing a live backend.

---

## 📍 Location

`web/assets/samples/ui/fixtures/`

This folder is for **front-end consumed fixtures**, not raw ingestion artifacts.

---

## 🧭 Guiding rules (KFM-style)

> [!IMPORTANT]
> Fixtures are **UI-boundary artifacts**. They should resemble **contracted API outputs** and **governed narrative payloads**, not raw database/graph dumps.

- ✅ **Contract-first**: fixtures should conform to the relevant **schemas/contracts** (UI config, API response shapes, telemetry events, etc.).
- ✅ **Evidence-first**: if a fixture supports narrative/UI explanations, it should include **source pointers** (or a sidecar meta file that does).
- ✅ **Provenance-first UI**: the UI is expected to surface “where did this come from?”—fixtures should help us test that.
- ✅ **Deterministic**: stable IDs, stable ordering, no timestamps unless the fixture is explicitly “time-sensitive”.

---

## 📦 What belongs here

| Fixture Type | What it’s for | Typical formats |
|---|---|---|
| 🌐 **API payload snapshots** | Mock UI consumption of endpoints (catalog search, dataset details, tiles metadata, story fetch, etc.) | `.json`, `.geojson`, `.jsonld` |
| 🗺️ **Map/UI state presets** | Camera state, selected feature, layer stack, timeline position, legend state | `.json` |
| 🎬 **Story-mode samples** | Minimal “story node” payloads used by UI rendering (steps, citations, media) | `.md`, `.json` |
| 🧠 **Focus Mode demos** | Grounded “question → evidence-backed answer” UI states / transcripts | `.json`, `.md` |
| 🖼️ **Media + thumbnails** | UI preview images, icons, screenshots for demo pages | `.png`, `.jpg`, `.svg`, `.webp` |

> [!TIP]
> Keep fixtures **small** and **purpose-built**. If you need a heavier payload for performance testing, put it in a clearly labeled `large/` or `stress/` folder and call it out in the manifest.

---

## 🗂️ Suggested layout (recommended)

```text
web/assets/samples/ui/fixtures/
├─ 📄 README.md
├─ 🧾 manifest.json              # (recommended) registry for gallery/demo selection
│
├─ 🌐 api/
│  ├─ datasets.search.basic.json
│  ├─ datasets.search.empty.json
│  ├─ datasets.get.one.json
│  └─ story.get.sample.json
│
├─ 🗺️ ui/
│  ├─ map_state.default.json
│  ├─ map_state.feature_selected.json
│  ├─ layer_panel.grouped.json
│  └─ timeline.scrub.1900.json
│
├─ 🎬 story/
│  ├─ prairie_fire_story.md
│  ├─ prairie_fire_story.steps.json
│  └─ prairie_fire_story.meta.json   # provenance + catalog pointers
│
├─ 🧠 focus_mode/
│  ├─ drought_question.sample.json
│  └─ drought_question.meta.json
│
└─ 🖼️ media/
   ├─ thumbnails/
   └─ screenshots/
```

> [!NOTE]
> This layout is a **convention**, not a prison. If you add new top-level folders, make sure they’re obvious, documented, and referenced by the manifest.

---

## 🏷️ Fixture metadata (manifest + sidecars)

Because JSON can’t contain comments, use **either**:

- ✅ a top-level `manifest.json` registry (recommended), and/or  
- ✅ a `*.meta.json` sidecar next to the payload

### Minimal `manifest.json` shape (suggested)

```json
{
  "version": 1,
  "fixtures": [
    {
      "id": "api.datasets.search.basic",
      "title": "Dataset search — basic results",
      "kind": "api",
      "files": ["api/datasets.search.basic.json"],
      "contracts": [
        "schemas/ui/...", 
        "src/server/... (OpenAPI/GraphQL reference)"
      ],
      "notes": "Use to test layer catalog list + quick add."
    },
    {
      "id": "ui.timeline.scrub.1900",
      "title": "Timeline scrub — year 1900",
      "kind": "ui-state",
      "files": ["ui/timeline.scrub.1900.json"],
      "notes": "Use to test time-aware layers + legend updates."
    }
  ]
}
```

### Suggested `*.meta.json` (provenance-friendly)

```json
{
  "id": "story.prairie_fire_story",
  "title": "Prairie fires story sample",
  "owner": "web-ui",
  "source_pointers": [
    "dcat:dataset:…",
    "stac:item:…",
    "prov:bundle:…"
  ],
  "contracts": [
    "schemas/story_nodes/…",
    "schemas/ui/…"
  ],
  "sensitivity": {
    "contains_pii": false,
    "contains_sensitive_locations": false
  }
}
```

> [!IMPORTANT]
> If the fixture drives a UI that shows citations/tooltips (“map behind the map”), the **fixture must enable that** — either directly in the payload or via `*.meta.json`.

---

## ✅ Adding a new fixture (checklist)

- [ ] Pick the **UI scenario** (what component/page/state is this for?)
- [ ] Choose the **boundary contract**:
  - API response snapshot (preferred for UI integration), or
  - UI state/config snapshot (for component-level stories)
- [ ] Create the payload file (and `*.meta.json` if needed)
- [ ] Ensure **determinism**
  - stable IDs
  - sorted arrays (where ordering isn’t semantically meaningful)
  - no random values
- [ ] Ensure **safety**
  - no secrets, tokens, keys
  - no PII
  - no copyrighted media without permission
- [ ] Register it in `manifest.json` (if the project uses one)
- [ ] Add 1–2 sentence **usage notes**: what it covers, what it doesn’t

---

## 🧰 Using fixtures in code

### Option A: Fetch from static assets (bundler-friendly)

```ts
const url = new URL(
  "../../assets/samples/ui/fixtures/api/datasets.search.basic.json",
  import.meta.url
);

const data = await fetch(url).then(r => r.json());
```

### Option B: Import JSON directly (if enabled)

```ts
// Depends on build tooling configuration
import searchBasic from "../../assets/samples/ui/fixtures/api/datasets.search.basic.json";

console.log(searchBasic);
```

### Option C: Drive UI “demo pages” / “component playgrounds”

If you have a UI route like `/samples` or a component sandbox, treat `manifest.json` as the **fixture index** and build a picker UI from it 🎛️

---

## 🔐 Privacy, safety, and governance

> [!WARNING]
> These fixtures ship in the repo. Treat them like public artifacts.

- 🚫 No API keys / secrets / tokens
- 🚫 No personal data (names, addresses, emails, exact coordinates tied to private individuals)
- ✅ Prefer synthetic or **clearly public** data
- ✅ If sensitive locations are possible in real data, include a fixture that tests **redaction/generalization UI behavior**
- ✅ Keep a clear trail to governed evidence where appropriate (DCAT/STAC/PROV pointers in meta)

---

## 🔎 Coverage targets (what we want fixtures to represent)

Aim to include fixtures for:

- 🔍 Search:
  - empty results
  - many results
  - “no permission”
  - server error
- 🗂️ Layer catalog panel:
  - grouped categories
  - time-aware layers vs static layers
  - legend rendering
  - transparency + ordering
- 🕰️ Timeline:
  - year scrub
  - event markers
  - time window selection
- 🧷 Feature details:
  - pop-up minimal
  - details sidebar rich (charts/media)
  - missing metadata edge cases
- 🎬 Story mode:
  - step-driven camera/layer changes
  - citations + media
- 🧠 Focus Mode:
  - answer with references
  - “insufficient evidence” response
  - follow-up questions that refine map/time scope

---

## 🔗 Related docs (inside the repo)

- 📘 `docs/MASTER_GUIDE_v13.md` — canonical pipeline + boundaries  
- 🧩 `web/` — UI implementation (components, views, viewers)  
- 🧾 `schemas/` — JSON Schemas (UI, telemetry, story nodes, etc.)  
- 🎬 `docs/reports/story_nodes/` — governed story content (draft vs published)

---

## 🧯 Non-goals

- ❌ Not a home for ingestion inputs (raw CSVs/rasters)  
- ❌ Not a substitute for governed catalogs (STAC/DCAT/PROV belong in their canonical homes)  
- ❌ Not “test snapshots” that are opaque/unstable (avoid noisy diffs)

---

## 🧭 “If you’re unsure…”

1) Start from the **UI scenario** you’re trying to build/test  
2) Identify the **contract** the UI consumes  
3) Create the smallest payload that proves the UI works  
4) Add provenance pointers if it becomes narrative/explanatory

Happy fixture crafting 🧪🗺️
