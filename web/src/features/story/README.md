---
title: "📖 Kansas Frontier Matrix — Story Nodes · Narrative Graph & Temporal Explorer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/features/story/README.md"
version: "v10.3.2"
last_updated: "2025-11-14"
review_cycle: "Quarterly / Autonomous + FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.3.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.3.2/manifest.zip"
telemetry_ref: "../../../releases/v10.3.2/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-story-v1.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📖 **Story Nodes — Narrative Graph & Temporal Explorer**  
`web/src/features/story/README.md`

**Purpose:**  
Bring **history to life** through interconnected Story Nodes that merge **text**, **time**, and **geography**.  
This feature renders AI-assisted narratives (from the KFM knowledge graph) as **interactive cards**, synchronized with **Timeline**, **Map**, **Focus Mode v2.4**, and **FAIR+CARE governance** overlays.

<img alt="Docs · MCP" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img alt="License" src="https://img.shields.io/badge/License-MIT-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange" />
<img alt="Status" src="https://img.shields.io/badge/Status-Stable-brightgreen" />

</div>

---

## 📘 Overview

The **Story Node system** ties together **events**, **people**, **places**, and **documents** into cohesive, explorable narratives.

Each node:

- Follows the **Story Node JSON Schema**:

  ~~~~~text
  ../../../schemas/story-node.schema.json
  ~~~~~

- Is enriched by **Focus Transformer v2.x** for AI summaries and related-entity suggestions.  
- Is CARE-tagged and filtered via FAIR+CARE governance rules.  
- Synchronizes with:

  - Map focus (centroid/geometry)  
  - Timeline window (start/end intervals)  
  - Focus Mode entity selection  

**Core Goals**

- 🧩 Merge structured graph data with human-readable narrative.  
- 🗺️ Tie stories to geospatial context (counties, AOIs, routes, rivers).  
- 🧠 Integrate Focus AI insights while preserving explainability.  
- ♻️ Maintain FAIR+CARE ethics, accessibility, and telemetry traceability.  

---

## 🗂️ Directory Layout

~~~~~text
web/
└─ src/
   └─ features/
      └─ story/
         README.md               # This file — Story Nodes overview
         story-card.tsx          # React component for narrative cards
         story-context.ts        # Context for story state and selection
         useStory.ts             # Data-fetching hook for nodes + summaries
         story-service.ts        # API calls to /api/story and /api/focus
         story-metadata.json     # Story schema + version metadata
         utils/
         ├─ formatters.ts        # Markdown → HTML, link & footnote handling
         └─ governance.ts        # CARE tags, sovereignty filters, visibility rules
~~~~~

---

## 🧩 Story Node Schema (Conceptual)

Story Nodes follow the **MCP-DL Story Node schema** designed in  
`Designing Schema for Story Nodes.md` and related specs.

Each node is a **narrative atom** combining:

- Narrative text (markdown)  
- Spatial footprint (Point/Polygon/MultiPolygon)  
- Temporal interval (start / end / precision)  
- Graph relations (events, people, places, docs, datasets)  
- Governance metadata (CARE, sovereignty, licenses)  
- STAC / dataset references  

### Example Story Node (Conceptual JSON)

~~~~~json
{
  "id": "story-fort-larned-1859",
  "type": "story-node",
  "title": "Fort Larned on the Santa Fe Trail",
  "summary": "Established in 1859, Fort Larned protected the Santa Fe Trail and hosted treaty councils.",
  "narrative": {
    "body": "Fort Larned stood as a frontier post during an era of transition...",
    "format": "text/markdown"
  },
  "spacetime": {
    "geometry": { "type": "Point", "coordinates": [-99.219, 38.183] },
    "when": {
      "start": "1859-01-01",
      "end": "1878-12-31",
      "precision": "year"
    }
  },
  "relations": [
    { "rel": "mentions", "target": "event-medicine-lodge-1867" },
    { "rel": "located_in", "target": "place-pawnee-county" }
  ],
  "stac": {
    "collection": "historic-sites",
    "assets": [
      {
        "href": "pmtiles://datasets/settlements.pmtiles",
        "roles": ["data"],
        "type": "application/vnd.pmtiles"
      }
    ]
  },
  "governance": {
    "care_tag": "public",
    "sovereignty_flags": [],
    "license": "CC-BY-4.0"
  }
}
~~~~~

---

## ⚙️ Data Flow & Architecture

~~~~~mermaid
flowchart LR
  NEO["Story Nodes & Graph<br/>Neo4j · STAC · Lineage"]
    --> API["/api/story/{id}<br/>Story API"]
  API --> FOCUS["Focus Transformer v2.x<br/>AI summaries · related entities"]
  FOCUS --> CTX["Story Context<br/>useStory + story-context"]
  CTX --> CARD["StoryCard React Component"]
  CARD --> SYNC["Timeline + Map + Focus Sync"]
~~~~~

**Lifecycle**

1. User selects an entity (event/place/person) on the **Map**, **Timeline**, or **Focus Mode**.  
2. `useStory()` requests the Story Node and Focus summary via `story-service.ts`.  
3. `StoryCard` renders the node, AI summary, and links to related Story Nodes.  
4. **Timeline** and **Map** are updated to reflect the node’s temporal interval and geometry.  
5. Telemetry logs view event, latency, A11y, and CARE status.

---

## 🖥️ React Component — `StoryCard`

~~~~~text
export function StoryCard({ node }) {
  const id = node.id;
  const when = node.spacetime?.when;
  const coords = node.spacetime?.geometry?.coordinates;

  return (
    <article
      aria-labelledby={`${id}-title`}
      className="story-card rounded-2xl shadow-md p-4 bg-surface"
    >
      <header>
        <h2 id={`${id}-title`} className="text-xl font-semibold">
          {node.title}
        </h2>
        {node.summary && <p className="text-sm text-muted">{node.summary}</p>}
      </header>

      <section
        className="mt-3 prose max-w-none"
        aria-label="Story narrative"
        dangerouslySetInnerHTML={{ __html: node.narrativeHtml }}
      />

      <footer className="mt-3 flex flex-wrap gap-3 text-xs text-muted">
        {when && (
          <span>
            🕰 {when.start} – {when.end}
          </span>
        )}
        {coords && Array.isArray(coords) && (
          <span>
            📍 {coords.join(", ")}
          </span>
        )}
      </footer>
    </article>
  );
}
~~~~~

**Accessibility**

- Uses semantic `<article>`, `<header>`, `<section>`, `<footer>`.  
- `aria-labelledby` ties the card to its title for screen readers.  
- Narrative region is explicitly labeled and compatible with Focus Mode updates.

---

## 🧭 Timeline & Map Synchronization

Story Nodes integrate tightly with **Timeline** and **Map**:

- When `currentYear` falls within `node.spacetime.when`, the card is eligible to show.  
- Selecting a Story Node:
  - Centers the map on `node.spacetime.geometry`.  
  - Adjusts the timeline view to the node’s interval.  
  - Updates Focus Mode context (entity-centric analysis).  

**Sync Pattern**

- `story-context.ts` exposes:
  - `currentStoryId`  
  - `setCurrentStoryId`  
  - `timelineRange`  
  - `mapFocus`  

- Timeline and Map components subscribe to story context to coordinate highlight and viewport.

---

## 📊 Telemetry & Governance (Web Story Events)

Story interactions produce **web-story-v1** telemetry events.

Example telemetry record:

~~~~~json
{
  "event": "story-view",
  "feature": "story",
  "timestamp": "2025-11-14T21:40:00Z",
  "latencyMs": 128,
  "userRole": "public",
  "governance": "approved",
  "faircare": {
    "a11yCompliant": true,
    "ethicalTag": "public"
  },
  "context": {
    "story_id": "story-fort-larned-1859",
    "source": "timeline",
    "relations_count": 3
  }
}
~~~~~

**Governance Tags**

| Tag          | Description                       | UI Behavior                        |
|--------------|-----------------------------------|------------------------------------|
| `public`     | Open narrative                    | Normal rendering                   |
| `restricted` | Licensed/sensitive content        | Summary-only / partial masking     |
| `sensitive`  | Private cultural heritage         | Node hidden or route to consent UX |

All Story Nodes are processed by the **FAIR+CARE Council** prior to publication.

---

## 🧮 Markdown & Media Rendering

Rendering pipeline (handled in `utils/formatters.ts`):

- Parse `narrative.body` as Markdown.  
- Sanitize for XSS and enforce safe link policies.  
- Convert internal references (e.g., `story:...`) into Story Node links.  
- Support optional media arrays:

  - Images (with alt text)  
  - Maps / mini-embeds (via STAC assets)  
  - Document thumbnails  

---

## ♿ Accessibility Highlights

- Story UI respects:

  - High-contrast themes  
  - Font-size scaling  
  - Reduced motion preferences  

- Keyboard shortcuts (example pattern):

  - `← / →` – previous/next card  
  - `Esc` – close or collapse story panel  

- A11y telemetry:

  - Logs number of unlabeled images when a Story panel is opened.  
  - Logs keyboard vs mouse interactions for story navigation.

---

## 📡 Integration with Focus Mode

Focus Mode v2.4 uses Story Nodes as **narrative overlays**:

- When a user focuses on an entity (place/event/person), related Story Nodes appear as cards.  
- Story Node selection updates the Focus graph explanation panel.  
- Explainability metadata (e.g., “Why this story?”) is surfaced via Focus Mode’s **“Why This Node?”** control with links back to underlying graph edges and datasets.

---

## 🧾 Internal Citation

~~~~~text
Kansas Frontier Matrix (2025). Story Nodes — Narrative Graph & Temporal Explorer (v10.3.2).
Integrates AI-assisted narratives, geospatial context, and FAIR+CARE governance into interactive Story Cards
synchronized with Timeline, Map, and Focus Mode.
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author       | Summary                                                                 |
|--------:|------------|-------------|-------------------------------------------------------------------------|
| v10.3.2 | 2025-11-14 | `@kfm-web`  | Upgraded Story Node architecture to KFM v10.3; aligned telemetry, FAIR+CARE, A11y, and Focus Mode v2.4. |
| v9.9.0  | 2025-11-08 | `@kfm-web`  | Initial Story Node feature with AI narrative rendering and CARE tags.  |
| v9.8.0  | 2025-11-05 | `@kfm-ui`   | Timeline + map synchronization and accessibility enhancements.         |

---

<div align="center">

**Kansas Frontier Matrix — Story Nodes**  
📖 Living Narratives · 🗺 Temporal-Geospatial Context · 🔐 FAIR+CARE Ethics  

© 2025 Kansas Frontier Matrix — MIT License  

[Back to Web Features](../README.md) · [Governance Charter](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>
