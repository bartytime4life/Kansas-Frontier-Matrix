# 📖 Stories Route (`web/src/routes/stories/`) — Scrollytelling + Map + Timeline

![Status](https://img.shields.io/badge/status-active-brightgreen)
![UI](https://img.shields.io/badge/ui-map%2Bstory%2Btimeline-blue)
![Provenance](https://img.shields.io/badge/provenance-first-purple)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-black)

> **Purpose:** This route powers KFM’s interactive narratives (“story nodes”)—a guided, map-synced reading experience where **scroll / steps drive time, layers, and camera moves**, and where **every claim is evidence-backed (“the map behind the map”)**. [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧭 What lives here

This folder owns the **/stories** experience:

- 📚 **Story index** (browse/search stories)
- 🧩 **Story detail** (play a single story, step-by-step / scroll-linked)
- 🗺️ **Map sync** (2D MapLibre + optional 3D Cesium modes)
- 🕰️ **Timeline sync** (year/range drives filters + story highlights)
- 🧾 **Citations & provenance UI** (datasets, sources, licenses)

KFM’s broader UI philosophy is **evidence-first**: maps + narratives are not “pretty outputs”; they’re **traceable** and **auditable**. [oai_citation:2‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🔗 Route contract (URLs & deep-linking)

KFM’s blueprint explicitly anticipates story routes such as:

- `/stories`  
- `/stories/:slug` (example mentioned: `/stories/dust-bowl`) [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Deep-linking goals (required):**
- ✅ Story can be opened directly via URL
- ✅ Optional query params can restore view state (e.g., `year=1935`, `step=4`, `mode=2d|3d`)
- ✅ Back/forward navigation should not lose the reader’s position

> If your router differs (React Router vs framework router), keep the contract the same: **storyId/slug** must be addressable via URL.

---

## 🧠 What is a “Story” in KFM?

A **Story Node** is a narrative container with a **time range**, **map view**, **layer list**, and **citations/media**, with steps that can trigger map/timeline actions. [oai_citation:5‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

KFM is explicitly designed so that:
- **every story is provenance-backed** (citations attached, no black boxes) [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- data access is **governed** (UI talks to API; policy decides what’s visible) [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🗺️ Map & timeline behavior (the “sync” contract)

### Global state: one source of truth

KFM’s blueprint describes a central store (often Redux) where components stay in sync—**timeline changes update the map and story panel** and vice versa. [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

**Minimum shared state (suggested):**
- `activeStoryId`
- `activeStepId` / `activeStepIndex`
- `currentYear` or `currentDateRange`
- `mapView`: `{ center, zoom, bearing, pitch, mode2D3D }`
- `visibleLayers`: layer IDs + params (opacity, filters)
- `highlightedFeatures` (optional: story-driven annotations)

### Scrollytelling mechanics

The blueprint calls out scroll-linked storytelling (via `IntersectionObserver`) where:
- story paragraphs entering view trigger **timeline jumps**, **map pans/zooms**, and **layer toggles** [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

> Keep animations smooth and reversible. If the reader scrolls backward, the map/time should rewind coherently.

---

## 🧩 Map engines (2D + 3D)

KFM explicitly references:

- **MapLibre GL JS (2D)** for interactive vector maps and layered data visualization [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- **CesiumJS (3D)** as an optional 3D globe/terrain mode with a UI toggle [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### Rule of thumb 🎯
- Default: 2D (MapLibre) for reading + fast interaction
- Optional: 3D (Cesium) for “fly-through” or terrain-based storytelling
- Switching modes should preserve context (keep user roughly in same place) [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🌐 Data sources used by this route

### 1) Story Nodes API (REST)

The system documentation describes **Story Nodes endpoints** under `/api/v1/story`:
- create a story node (auth + contributor role)
- fetch story by ID
- search stories (filter by bbox/time/tags) [oai_citation:14‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 2) Knowledge Graph / GraphQL

KFM includes a GraphQL interface for rich relationship queries across **places ↔ datasets ↔ events ↔ stories**, and it’s explicitly called out as a way to query story nodes efficiently. [oai_citation:15‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

Example query (from the blueprint’s dev workflow section):

```graphql
query {
  storyNodes {
    id
    title
    yearRange
  }
}
```

 [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 3) Map tiles & datasets

KFM serves tiles for map visualization:
- vector tiles (MVT): `GET /tiles/{layer}/{z}/{x}/{y}.pbf`
- raster tiles: `GET /tiles/{layer}/{z}/{x}/{y}.png` (or `.webp`) [oai_citation:18‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

…and datasets are discoverable and retrievable via REST endpoints for metadata and data payloads (e.g., GeoJSON). [oai_citation:19‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🧱 Suggested folder structure (keep it tidy)

> Adjust filenames to match your stack, but keep responsibilities separated.

```text
📁 web/src/routes/stories/
├── 📄 README.md ✅ (this file)
├── 📄 index.tsx                # route entry (list + nested routes)
├── 📄 StoriesIndexPage.tsx      # browse/search
├── 📄 StoryPage.tsx            # story player shell (map + panel)
├── 📁 components/
│   ├── 📄 StoryPlayer.tsx       # orchestrates steps + scroll sync
│   ├── 📄 StoryStep.tsx         # renders a single step (md + media)
│   ├── 📄 StoryTOC.tsx          # navigation / progress
│   ├── 📄 CitationsDrawer.tsx   # provenance UI per step/story
│   └── 📄 StoryMetaBar.tsx      # title, tags, time range, share links
├── 📁 data/
│   ├── 📄 storyApi.ts           # REST/GraphQL wrappers
│   ├── 📄 storySchemas.ts       # runtime validation (zod/io-ts)
│   └── 📄 storyCache.ts         # caching + prefetch hints
├── 📁 hooks/
│   ├── 📄 useStory.ts           # fetch & normalize story
│   ├── 📄 useStoryScrollSync.ts # IntersectionObserver bindings
│   └── 📄 useStoryDeepLink.ts   # URL ↔ state sync
├── 📁 types/
│   ├── 📄 storyTypes.ts         # TS interfaces
│   └── 📄 provenanceTypes.ts    # citation/source types
└── 📁 __tests__/
    ├── 📄 storyParsing.test.ts
    └── 📄 storyScrollSync.test.ts
```

---

## 🧾 Story format (frontend contract)

Even if story nodes come from the API, the route should normalize them into a stable UI contract.

### TypeScript-friendly shape (recommended)

```ts
export type StoryNode = {
  id: string;
  slug: string;
  title: string;
  summary?: string;

  // time
  yearRange?: { start: number; end: number };

  // map defaults
  map?: {
    mode: "2d" | "3d";
    center: [number, number]; // lon, lat
    zoom: number;
    bearing?: number;
    pitch?: number;
  };

  // layers implied by the story (can be overridden by steps)
  layers?: Array<{
    id: string;           // stable layer ID
    type: "vector" | "raster" | "geojson";
    source?: string;      // tile endpoint / dataset endpoint reference
    opacity?: number;
  }>;

  // the narrative
  steps: StoryStep[];

  // provenance: story-level sources
  citations?: Citation[];
  tags?: string[];
};

export type StoryStep = {
  id: string;
  title?: string;

  // narrative content (Markdown encouraged)
  body: string;

  // triggers when the step becomes active
  onEnter?: {
    setYear?: number;
    setYearRange?: { start: number; end: number };

    flyTo?: {
      center: [number, number];
      zoom: number;
      bearing?: number;
      pitch?: number;
      durationMs?: number;
    };

    enableLayers?: string[];
    disableLayers?: string[];

    highlight?: {
      datasetId?: string;
      featureIds?: string[];
    };
  };

  // provenance: step-level sources override/extend story sources
  citations?: Citation[];
};

export type Citation = {
  id: string;
  label: string;
  sourceType: "dataset" | "document" | "map" | "media" | "other";
  datasetId?: string;     // ideal when tied to a dataset record
  url?: string;           // linkable reference (if allowed)
  license?: string;
  notes?: string;
};
```

**Why this matters:** KFM treats story narratives like first-class, governed outputs—**citations are non-optional for factual claims** (“Provenance First”). [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## ✅ Adding a new story (authoring checklist)

### Authoring steps ✍️
1. **Define the narrative arc** (what question does the story answer?)
2. **Pick the time range** (start/end) and your “hero map views”
3. **Choose layers** you will enable/disable during the story (prefer tile layers for performance)
4. **Attach citations** at story-level and step-level:
   - dataset IDs where possible
   - license + provenance notes
5. **Implement step triggers** (time, camera, layers)
6. **Test scroll-sync** both directions (down + up)

### “Provenance First” acceptance criteria 🧾
- No step that asserts facts ships without citations.
- If a story node lacks required provenance metadata, it should be blocked/flagged (“fail closed” governance philosophy). [oai_citation:21‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🛡️ Governance, RBAC, and “fail closed”

KFM’s governance model includes:
- Role-based access control (Public Viewer, Contributor, Maintainer, Admin)
- Policy enforcement (OPA) that can deny access or block operations by default (“fail closed”) [oai_citation:23‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

**Stories route implications:**
- UI must gracefully handle `403/401`:
  - Hide “Create/Edit Story” unless role permits
  - Show clear “access denied” messaging
- When story content references restricted datasets:
  - Prefer **partial rendering** (redacted sections) over broken UI
  - Citations panel should indicate restricted sources if appropriate

---

## 🤝 FAIR + CARE (especially for Indigenous data)

KFM explicitly adopts **FAIR + CARE** as core operating principles (Findable/Accessible/Interoperable/Reusable + Collective Benefit/Authority to Control/Responsibility/Ethics). [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

Indigenous Data Sovereignty literature highlighted in the project files makes a key point:
- FAIR alone does not sufficiently protect Indigenous data
- CARE was developed as an essential addition when dealing with Indigenous data [oai_citation:25‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)

**Stories route requirements when Indigenous data is involved:**
- ✅ Make provenance explicit (who produced it, who governs it, why it’s included)
- ✅ Respect restrictions, consent, and governance mechanisms
- ✅ Avoid “deficit narrative” framing; prioritize context and community benefit

> If a dataset is tagged as sensitive or governed by community policy, the story player must defer to policy (OPA/RBAC) rather than “trying to be helpful.” [oai_citation:26‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:27‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)

---

## 🧾 Metadata & licenses (don’t ship stories without them)

Map-design guidance in the project files emphasizes that **dependable GIS data requires metadata**, including:
- identification, quality, spatial reference, temporal info, distribution/use policy, and how to cite it [oai_citation:28‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

**Practical UI implication:**
- Citations drawer should show (when available):
  - dataset title + publisher
  - date/temporal coverage
  - license / usage
  - recommended citation
  - link back to dataset catalog entry

Also: maps and representations can be copyright-protected even if facts are not—be careful about reusing cartographic styling from copyrighted works. [oai_citation:29‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)

---

## ♿ Accessibility requirements (non-negotiable)

Stories are reading-first. Make them accessible:

- ✅ Keyboard navigation for TOC + step jump
- ✅ Visible focus states
- ✅ Reduced motion support (respect OS setting; shorten/disable flyTo animations)
- ✅ Provide non-scroll navigation (Next/Prev step buttons)
- ✅ Don’t trap screen readers in the map canvas

---

## ⚡ Performance guidelines

- Prefer **vector/raster tiles** for large layers; avoid huge GeoJSON in story playback
- Keep step triggers lightweight (debounce scroll events; avoid repeated `flyTo` spam)
- Cache story payloads (in-memory + optionally localStorage)
- Consider prefetching:
  - next story step media
  - next tile layers

KFM’s API supports vector/raster tile endpoints intended for exactly this purpose. [oai_citation:30‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🧪 Testing strategy (minimum viable coverage)

### Unit tests
- Story schema validation (required fields, citations presence)
- Trigger normalization (onEnter actions merged correctly)

### Integration tests
- Scroll → activeStep changes → store updates
- activeStep → timeline changes → map filter updates
- URL deep-link loads correct story + step + year

### “Definition of Done” ✅
- [ ] Deep link works (`/stories/:slug`)
- [ ] Timeline and story remain synchronized (both directions) [oai_citation:31‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] Story steps update map/time smoothly (scrollytelling) [oai_citation:32‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] Citations render per story + per step (“Provenance First”) [oai_citation:33‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] RBAC respected; restricted stories/data fail closed [oai_citation:34‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- [ ] A11y checks pass (keyboard, reduced motion)

---

## 🛠️ Troubleshooting (developer quick hits)

If your environment is Docker-based, the blueprint notes common pitfalls:
- port conflicts (e.g., 5432, 8000, 3000)
- volume mount issues for web hot reload
- use Swagger UI at `http://localhost:8000/docs` to explore endpoints [oai_citation:35‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:36‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 📚 Source excerpts that inform this README

These are the most load-bearing project references used for this route documentation:

- KFM evidence-first mission & “map behind the map” provenance framing [oai_citation:37‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Provenance-first + FAIR/CARE emphasis (blueprint) [oai_citation:38‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:39‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Frontend sync: shared store ties timeline ↔ map ↔ story panel [oai_citation:40‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Scrollytelling mechanics and MapLibre/Cesium usage [oai_citation:41‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:42‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Story Nodes endpoints + GraphQL story nodes query capability [oai_citation:43‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:44‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Governance: RBAC + OPA fail-closed enforcement [oai_citation:45‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- CARE as essential addition to FAIR for Indigenous data stewardship [oai_citation:46‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)
- GIS metadata essentials + copyright caution for map representations [oai_citation:47‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9) [oai_citation:48‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](sediment://file_00000000602471f786dfbbaac9329fb9)