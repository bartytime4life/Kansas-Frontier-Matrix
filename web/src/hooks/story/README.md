# 🪝 Story Hooks (`web/src/hooks/story`)

![Scope](https://img.shields.io/badge/Scope-Story%20Hooks-blue)
![React](https://img.shields.io/badge/React-Hooks-61DAFB?logo=react&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-Ready-3178C6?logo=typescript&logoColor=white)
![Provenance](https://img.shields.io/badge/Provenance-First-brightgreen)
![Focus%20Mode](https://img.shields.io/badge/Focus%20Mode-Hard%20Gate-orange)

> **Mission:** Provide React hooks that power the **Story Node + Focus Mode** experience: loading governed narrative artifacts, synchronizing them with **map + timeline** context, and enforcing provenance & sovereignty guardrails.

---

## ⚡ Quick Links

- ⬅️ **Repo Overview:** `../../../../README.md`
- 📘 **Master Guide / Rules of the Road:** `../../../../docs/MASTER_GUIDE_v13.md` (or equivalent)
- 🧾 **Story Node authoring contract:** `../../../../docs/templates/TEMPLATE__STORY_NODE_V3.md` [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- 🔌 **API docs (Story + GraphQL + Tiles):** `../../../../src/server/api/README.md`
- 🧠 **Why “Focus Mode” is strict:** see **Focus Mode rules** below [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧠 What are Story Nodes and Focus Mode?

### 🧾 Story Nodes (governed narrative artifacts)
In KFM, a **Story Node** is not “just markdown.” It’s a **machine‑ingestible** narrative artifact that must:

- include **provenance for every claim** (citations trace back to cataloged evidence),
- **reference graph entities** via stable identifiers,
- **distinguish fact vs interpretation** (especially when AI-assisted text exists). [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🔍 Focus Mode (the “hard gate” reading experience)
**Focus Mode** is the interactive reader where a Story Node is presented alongside **map + timeline** context, and it is governed by strict trust rules:

- **Only provenance‑linked content** can display (hard gate).
- **AI contributions must be opt‑in and transparent** (labeled + confidence/uncertainty).
- **No sensitive location leaks** (generalize/omit sensitive sites per sovereignty rules). [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

**Implication for this folder:** story hooks are not “just UX helpers” — they are part of the trust boundary.

---

## 🧱 Non‑Negotiable Invariants

### 🧬 Canonical pipeline order (don’t bypass stages)
KFM’s pipeline order is explicitly defined and must not regress:  
**ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode** [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🚫 API boundary rule
The frontend **must not query Neo4j (graph) directly**; all data access goes through the governed API layer. [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 🧭 Provenance + CARE in UI work
When implementing UI features that touch Story Nodes (e.g., highlighting locations), new UI layers must tie back to provenance and respect CARE principles, including hiding precise coordinates if sensitive. [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📦 What lives in `web/src/hooks/story`

This directory houses hooks that typically fall into four buckets:

### 1) 📡 Data hooks (fetch + cache governed story content)
- Load Story Nodes by ID
- Search Story Nodes (bbox, time, tags)
- Resolve story ↔ dataset ↔ event ↔ place relationships (GraphQL)

### 2) 🎛️ Player hooks (step/scene orchestration)
- Current step, progress, next/prev navigation
- “chapter” state + derived UI state (active citations, active media, etc.)

### 3) 🗺️ Sync hooks (map + timeline coupling)
- Apply Story Node “scene state” to map center/layers
- Apply Story Node time range to timeline filters

### 4) 🛡️ Focus Mode safety hooks (hard‑gate enforcement)
- Ensure only provenance-linked assets render
- Ensure AI content is opt‑in + labeled + includes confidence/uncertainty
- Ensure sensitive geometry is generalized/omitted

> 📝 **Naming note:** hook names may vary. Prefer a single “public surface” via `index.ts` re-exports. Keep this README updated as hooks evolve.

---

## 🔌 API touchpoints story hooks are allowed to use

### 🧾 Story Nodes REST API
The system exposes **Story Node endpoints under `/api/v1/story`**, including:
- `POST /api/v1/story` to create a Story Node (authenticated contributor role), with JSON including **title, time range, map center, layer list, citations/media**
- `GET` endpoints to fetch by **ID** or **search** (filter by bbox/time/tags). [oai_citation:7‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 🧠 GraphQL for cross-domain joins
GraphQL (`POST /graphql`) is explicitly positioned for complex relationship queries like **places ↔ datasets ↔ events ↔ stories**, including “all story nodes connected to a given dataset.” [oai_citation:8‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

The technical blueprint even shows a simple query shape for Story Nodes:
```graphql
query {
  storyNodes {
    id
    title
    yearRange
  }
}
``` [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 🧩 Map tile endpoints (map rendering)
Standard tile endpoints exist for layers, including vector tiles like:
- `GET /tiles/{layer}/{z}/{x}/{y}.pbf` (MVT)
- raster variants like `.png/.webp` (implementation dependent). [oai_citation:10‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 🤖 Focus Mode AI endpoints (use carefully)
The API includes AI endpoints such as `POST /api/v1/ai/query` (answers with citations, optional context), plus an experimental streaming endpoint and suggestions endpoint. [oai_citation:11‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

> ✅ Hooks may integrate AI *only* in ways that satisfy Focus Mode rules: opt-in, labeled, uncertainty shown, sovereignty respected. [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📜 Scrollytelling: how Story Hooks drive “narrative → map/timeline”

KFM’s UI vision includes a **Story/Narrative player** that supports “scrollytelling”: as the user scrolls, the **map updates** and the **timeline slider updates**. The blueprint explicitly suggests using the **Intersection Observer API**, with trigger elements carrying attributes like `data-year` and `data-mapState`, and a hook reading those attributes to update global state. [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### Suggested pattern (DOM triggers → hook → global story state)

**Example DOM markup (authoring-friendly):**
```html
<section data-story-step data-year="1870" data-map-state='{"center":[-96.5,38.5],"zoom":6,"layers":["trails"]}'>
  <h2>Rail expansion begins</h2>
  <p>…</p>
</section>
```

**Example hook skeleton (framework-agnostic):**
```ts
type MapState = { center: [number, number]; zoom: number; layers: string[] };

type StoryStepActivation = {
  year?: number;
  mapState?: MapState;
  stepId?: string;
};

export function useStoryScrollSync(params: {
  root?: Element | null;
  onActivateStep: (activation: StoryStepActivation) => void;
}) {
  // Implementation idea:
  // - observe [data-story-step] elements
  // - on intersection, parse dataset attributes
  // - call onActivateStep({ year, mapState, stepId })
}
```

---

## 🧩 Recommended “public interface” conventions

To keep the Story system predictable across the app, prefer these conventions:

### ✅ Return shapes
- Prefer `{ data, status, error }` (or equivalent) for data hooks.
- Keep stable callback identities (use `useCallback`) for player actions.
- Make “derived state” explicit: e.g. `activeYearRange`, `activeLayers`, `activeCitations`.

### 🧯 Abort + race safety
Story navigation can be fast (scrolling). Data hooks should:
- use abortable requests (AbortController),
- ignore stale responses,
- avoid flicker by caching last-good story state.

### 🧼 Determinism + “no surprises”
- Hooks should not fabricate narrative.
- Hooks should not silently “fill in” missing story data; missing provenance should be treated as a hard stop in Focus Mode contexts. [oai_citation:14‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🛡️ Focus Mode compliance checklist (PR gate ✅)

Before merging changes to hooks in this folder:

- [ ] **No unsourced narrative** is introduced via UI logic (hard gate). [oai_citation:15‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] Any AI feature is **off by default**, **user-triggered**, **labeled**, and exposes confidence/uncertainty. [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] Sensitive locations are **generalized/omitted** (no coordinates side-channel). [oai_citation:17‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] Map/time updates are driven by **cataloged/provenance-backed** sources (layers must cite data). [oai_citation:18‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] All data access stays inside the **API boundary** (no direct graph calls). [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧪 Testing notes (what matters most)

Recommended test coverage targets:

- ✅ **State machine correctness** (step activation, next/prev, scroll activation ordering)
- ✅ **Sync correctness** (map+timeline apply the correct derived “scene state”)
- ✅ **Hard gate behavior** (blocks rendering when required provenance identifiers/citations are missing)
- ✅ **Sensitive geometry handling** (does not leak precision when flagged)

---

## 🧰 Troubleshooting

### Map and story steps drift out of sync
- Check that the scroll hook activates steps deterministically (avoid multiple triggers for the same step).
- Ensure map updates are debounced/throttled only where safe (don’t drop events).

### Story search returns data but Focus Mode shows nothing
- Focus Mode can intentionally hide content that lacks provenance IDs or citations (hard gate). [oai_citation:20‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### “Why can’t we just query Neo4j from the UI?”
- This is explicitly prohibited by the API boundary rule; data access must go through `src/server/` governed endpoints. [oai_citation:21‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📚 Project file references (grounding)

- **KFM Master Guide / Markdown Guide v13**  [oai_citation:22‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
  (Story Node requirements + Focus Mode hard gate + pipeline invariants) [oai_citation:23‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:24‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

- **KFM Comprehensive System Documentation**  [oai_citation:25‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
  (REST + GraphQL + Story Node endpoints + tiles + system integration points) [oai_citation:26‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:27‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

- **KFM Comprehensive Technical Blueprint**  [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  
  (UI scrollytelling + Intersection Observer + example GraphQL query shape) [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:30‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🗂️ (Optional) Suggested local layout

```text
📁 web/src/hooks/story/
├─ 📄 README.md        # you are here ✨
├─ 🪝 useStoryNode.ts
├─ 🪝 useStorySearch.ts
├─ 🪝 useStoryPlayer.ts
├─ 🪝 useStoryScrollSync.ts
├─ 🪝 useStoryMapSync.ts
├─ 🪝 useStoryTimelineSync.ts
└─ 📦 index.ts         # re-exports (public surface)
```

> If the actual hook inventory differs, update this README to match what is exported by `index.ts`.

---