# 🧩 Story Components (`web/components/story`)

![KFM](https://img.shields.io/badge/KFM-v13-blue)
![UI](https://img.shields.io/badge/UI-React%20%2B%20Map-green)
![Narratives](https://img.shields.io/badge/Narratives-Story%20Nodes-orange)
![Trust](https://img.shields.io/badge/Trust-Provenance--First-purple)
![Boundary](https://img.shields.io/badge/Rule-API%20Boundary-red)

> **What this folder is:** React UI components that render **Story Nodes** (governed narrative) and coordinate them with the **map + timeline** experience (and optionally **Focus Mode**) — without ever breaking KFM’s provenance and sovereignty rules. 🧭📚🗺️  
> KFM’s pipeline ordering + API boundary rule are *non-negotiable* here. :contentReference[oaicite:0]{index=0}

---

## 📌 Why Story Components exist

KFM isn’t “just a map.” It’s a combined **map-and-narrative UI** where story content can drive map/timeline state (camera, layers, time windows) and where users can explore evidence interactively. :contentReference[oaicite:1]{index=1}

Story UI is a core part of that: Story nodes turn narrative text into an interactive, data-linked “storybook” experience for educators, historians, and public outreach use cases. :contentReference[oaicite:2]{index=2}

---

## ✅ Non‑negotiable contracts (read first)

### 1) Canonical pipeline ordering (no leapfrogging)
Everything must follow the ordering:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode** :contentReference[oaicite:3]{index=3}

No stage can consume data that hasn’t passed the previous stage’s contracts + outputs. :contentReference[oaicite:4]{index=4}

### 2) API boundary rule (hard rule)
**The frontend UI must never query Neo4j directly** — all data access goes through the governed API layer. This is how we enforce redaction, access controls, and schema consistency. :contentReference[oaicite:5]{index=5}

### 3) Evidence-first narrative (Story Nodes + Focus Mode)
Story Nodes must be provenance-linked, and Focus Mode must not introduce unsourced content (no “hallucinated” claims). :contentReference[oaicite:6]{index=6}

### 4) Focus Mode “hard gate” rules (when Story is shown in Focus Mode)
- **Only provenance-linked content** may appear. :contentReference[oaicite:7]{index=7}
- **AI contributions are opt‑in and clearly labeled** (with uncertainty/confidence). :contentReference[oaicite:8]{index=8}
- **No sensitive location leaks** (generalize/omit sensitive places to prevent side‑channels). :contentReference[oaicite:9]{index=9}

### 5) UI layer provenance + CARE compliance
Any new UI layer (including map overlays used by Story steps) must tie back to provenance (e.g., popup/legend cites DCAT/STAC) and must comply with CARE (including hiding precise coordinates if sensitive). :contentReference[oaicite:10]{index=10}

---

## 🧠 Core concepts

### 📖 Story Nodes
Story Nodes are “machine‑ingestible storytelling”: Markdown docs with semantic annotations + citations that turn narrative into governed content. :contentReference[oaicite:11]{index=11}

A valid Story Node must:  
- include provenance for every claim,  
- reference graph entities via stable identifiers,  
- distinguish fact vs interpretation (especially if AI-assisted). :contentReference[oaicite:12]{index=12}

### 🗺️ Story Mode (step-by-step map syncing)
Each story is typically authored as:
- **Markdown** (narrative + citations)  
- **JSON config** (step instructions: activate layers, set camera, set timeline/time) :contentReference[oaicite:13]{index=13}

Steps should synchronize the narrative with map updates (zoom/layers/time). :contentReference[oaicite:14]{index=14}

### 🕸️ Story ↔ Graph linking
Stories use the graph to link narrative text to data: entity mentions can become interactive UI elements showing entity info, and story steps can fetch related places/events to highlight on the map. :contentReference[oaicite:15]{index=15}

### 🤖 Focus Mode (optional assistant)
When Focus Mode answers questions, it relies on the graph to traverse entities, datasets, and relationships — but must remain evidence-first and provenance-linked. :contentReference[oaicite:16]{index=16}

---

## 🗂️ What lives in `web/components/story`

This folder is the **UI/UX implementation** for story rendering and interaction (not the narrative source-of-truth).

- **Narrative content canonical home:** `docs/reports/story_nodes/` (draft vs published). :contentReference[oaicite:17]{index=17}
- In v13, story content is explicitly reorganized into that governed structure. :contentReference[oaicite:18]{index=18}

> ⚠️ Note: Older design references mention a `web/story_nodes/` asset location for images/story assets in the running app; treat `docs/reports/story_nodes/` as the governed source and consider `web/story_nodes/` as a *build artifact* if/when used. :contentReference[oaicite:19]{index=19}:contentReference[oaicite:20]{index=20}

### Suggested internal layout (recommended)

```text
flowchart LR
  A["📦 API returns StoryNode<br/>+ provenance/citations"] --> B["🧾 StoryMarkdown<br/>render safely"]
  A --> C["🧭 StoryStepper<br/>progress & navigation"]
  C --> D["🗺️ StoryStepEffects<br/>map/timeline sync"]
  D --> E["🧩 Map UI<br/>layers/camera/time"]
  B --> F["🔖 CitationPanel<br/>evidence drilldown"]
  B --> G["🧷 EntityLink<br/>graph-backed context"]
  E --> H["🧠 Focus Mode (optional)<br/>evidence-first assistant"]
```

---

## 🧬 Data contracts (TypeScript shape)

KFM is contract-first: treat these shapes as **interfaces to the governed API + schemas** (and keep them aligned with JSON schema / OpenAPI definitions). :contentReference[oaicite:21]{index=21}

```ts
/** Minimal story node shape (align with schema + API contract) */
export type StoryNode = {
  id: string;               // stable id / slug
  title: string;
  status: "draft" | "published";
  markdown: string;         // narrative markdown with citations + semantic annotations
  citations: StoryCitation[];
  entities?: EntityRef[];   // stable graph identifiers mentioned/used
  steps?: StoryStep[];      // optional map/timeline choreography
};

export type StoryCitation = {
  id: string;               // footnote id
  label?: string;           // short label
  href?: string;            // link to cataloged asset/page
  catalogRef?: {
    dcat?: string;          // dataset id
    stac?: string;          // item/collection id
    prov?: string;          // provenance id
  };
};

export type EntityRef = {
  id: string;               // stable graph id
  kind: "Person" | "Place" | "Event" | "Document" | string;
  label?: string;
};

export type StoryStep = {
  id: string;
  title?: string;
  narrativeAnchor?: string; // optional: id in markdown to scroll to
  map?: {
    /** camera settings may be expressed in various projections; keep contract explicit */
    camera?: { lon: number; lat: number; zoom: number };
    layersOn?: string[];
    layersOff?: string[];
    highlight?: { entityIds?: string[]; featureIds?: string[] };
  };
  timeline?: {
    /** for historical narrative: year ranges are common */
    from?: string; // ISO date or year
    to?: string;   // ISO date or year
  };
};
```

---

## 🔁 How the story pipeline should behave in the UI

```mermaid
flowchart LR
  A[📦 API returns StoryNode<br/>+ provenance/citations] --> B[🧾 StoryMarkdown<br/>render safely]
  A --> C[🧭 StoryStepper<br/>progress & navigation]
  C --> D[🗺️ StoryStepEffects<br/>map/timeline sync]
  D --> E[🧩 Map UI<br/>layers/camera/time]
  B --> F[🔖 CitationPanel<br/>evidence drilldown]
  B --> G[🧷 EntityLink<br/>graph-backed context]
  E --> H[🧠 Focus Mode (optional)<br/>evidence-first assistant]
```

Key idea: story UI is not “freeform content.” It is **governed narrative + governed state changes**, derived from provenance-first pipeline artifacts. :contentReference[oaicite:22]{index=22}:contentReference[oaicite:23]{index=23}

---

## 🗺️ Map + Timeline synchronization

From the implementation design:
- Story content is authored in **Markdown + JSON config**.
- JSON step config can say things like:  
  “at step 2, activate layer X and Y, set map camera to [lon, lat, zoom], set timeline to year 1935”  
- Front-end applies these using MapLibre/Cesium-style map APIs. :contentReference[oaicite:24]{index=24}

### Example step config (illustrative)
```json
{
  "id": "dust-bowl-step-2",
  "title": "1935: Peak conditions",
  "map": {
    "camera": { "lon": -98.0, "lat": 38.5, "zoom": 5.8 },
    "layersOn": ["rainfall_anomaly_1935", "migration_by_county_1930s"]
  },
  "timeline": { "from": "1935-01-01", "to": "1935-12-31" }
}
```

> 🧷 If you add a new map layer used by stories, ensure it includes provenance-backed popups/legends and respects coordinate redaction for sensitive sites. :contentReference[oaicite:25]{index=25}

---

## 🔖 Citations, provenance, and “evidence drilldown”

Story Nodes must include provenance for each claim and must remain traceable back to cataloged sources. :contentReference[oaicite:26]{index=26}

**UI expectation:** every citation should open an evidence trail (DCAT/STAC/PROV) — no orphan footnotes.

Recommended UI affordances:
- footnote list + inline popovers
- “View Dataset” / “View Lineage” links when `catalogRef` exists
- per-step “evidence used in this slide” panel

---

## 🧷 Entity linking (graph-backed chips)

Story narrative linking is a core feature: narrative text can become interactive links that show entity info from the graph, and steps can highlight related entities/places on the map. :contentReference[oaicite:27]{index=27}

**Implementation note:** Keep entity resolution behind the API boundary (no direct Neo4j querying in the client). :contentReference[oaicite:28]{index=28}

---

## 🔒 Security & redaction (don’t skip)

### 1) Markdown rendering must be safe
If Markdown is rendered to HTML, sanitize it and avoid dangerous DOM injection patterns. XSS risk is commonly associated with unsafe usage of `document.write()`, `eval()`, and `innerHTML`/`outerHTML`. :contentReference[oaicite:29]{index=29}

**Rule of thumb:** render Markdown via a sanitizer whitelist (and do not pass raw HTML through by default).

### 2) No sensitive location leaks
Focus Mode + Story should never become a side channel to reveal restricted coordinates. The system must generalize/omit sensitive locations. :contentReference[oaicite:30]{index=30}

---

## ♿ Accessibility & UX quality

KFM’s web app is designed to be responsive and accessible; story components must uphold the same bar. :contentReference[oaicite:31]{index=31}

Suggested checks:
- keyboard navigation for next/prev
- focus management when changing steps
- caption/alt text for story media
- avoid scroll-jank (especially in “scroll-driven progress” mode) :contentReference[oaicite:32]{index=32}

---

## 🧪 Testing expectations

Minimum useful tests for story UI:
- ✅ Markdown renderer sanitization (XSS regression tests) :contentReference[oaicite:33]{index=33}
- ✅ Step-effects produce correct map/timeline “commands” given a step config :contentReference[oaicite:34]{index=34}
- ✅ Redaction behavior for sensitive coordinates (generalize/omit) :contentReference[oaicite:35]{index=35}
- ✅ Contract tests at boundaries (API response shape → UI props) :contentReference[oaicite:36]{index=36}

---

## ✅ Definition of Done (DoD) for changes in this folder

Use this checklist in PRs:

- [ ] No UI feature bypasses pipeline ordering or contracts. :contentReference[oaicite:37]{index=37}
- [ ] No direct Neo4j access from web client; all data via API. :contentReference[oaicite:38]{index=38}
- [ ] Any new map layer or overlay shows provenance (DCAT/STAC) and respects CARE/redaction. :contentReference[oaicite:39]{index=39}
- [ ] Story rendering enforces “evidence-first narrative” (citations required, traceable). :contentReference[oaicite:40]{index=40}
- [ ] If Focus Mode is involved: AI text is opt-in, labeled, and does not leak sensitive data. :contentReference[oaicite:41]{index=41}:contentReference[oaicite:42]{index=42}
- [ ] A11y basics pass (keyboard, focus, ARIA labels, readable contrast). :contentReference[oaicite:43]{index=43}
- [ ] Tests updated/added for renderer + step effects + redaction. :contentReference[oaicite:44]{index=44}

---

## 🛣️ Roadmap hint: Story Builder GUI (future)
A future goal is a Story Builder GUI so non-developers can build stories without writing JSON manually. Components here should keep step contracts clean to support that future authoring workflow. :contentReference[oaicite:45]{index=45}

---

## 🔗 Related docs (repo pointers)

- 📘 `MARKDOWN_GUIDE_v13.md` (pipeline ordering, contracts, canonical homes) :contentReference[oaicite:46]{index=46}
- 🧾 Story node content canonical home: `docs/reports/story_nodes/` :contentReference[oaicite:47]{index=47}
- 🧱 Technical architecture reference: “Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation” :contentReference[oaicite:48]{index=48}

---

<details>
<summary>📎 Quick mental model (one-liner)</summary>

**Stories are governed Markdown + governed step-config → rendered safely in React → synced to map/timeline via API-backed data → optionally enhanced by evidence-first Focus Mode.** :contentReference[oaicite:49]{index=49}:contentReference[oaicite:50]{index=50}

</details>
