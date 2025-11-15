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
Turn the Kansas Frontier Matrix (KFM) knowledge graph into a **living storybook** — a lattice of **Story Nodes** that braid together **time**, **place**, and **people**.  
This feature renders AI-assisted narratives as **interactive cards**, synchronized with **Timeline**, **Map**, **Focus Mode v2.4**, and **Web Telemetry** — all guarded by **FAIR+CARE** governance.

<img alt="Docs · MCP" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img alt="License" src="https://img.shields.io/badge/License-MIT-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange" />
<img alt="Status" src="https://img.shields.io/badge/Status-Stable-brightgreen" />

</div>

---

## 📘 Overview

The **Story Node system** is the **narrative face** of KFM’s semantic stack:

- Ingests **graph entities** (events, people, places, documents, datasets) from Neo4j.  
- Wraps them into **Story Nodes** that follow KFM’s Story Node schema and MCP-DL guidelines.  
- Uses **Focus Transformer v2.x** to synthesize short, explainable summaries and relationship hints.  
- Aligns each Story Node with:
  - A **time span** (OWL-Time-aware)  
  - A **spatial footprint** (GeoSPARQL-aware)  
  - A **governance profile** (FAIR+CARE tags, sovereignty flags)  

**What you get**

- 🧩 **Narrative Graph:** Nodes linked by relations like `mentions`, `located_in`, `precedes`, `co-occurs`.  
- 🗺️ **Temporal Explorer:** Cards that light up as the Timeline scrubs across years.  
- 🧠 **Focus-Aware:** Seamless handoff between Focus Mode and narrative cards.  
- ♻️ **Ethically Governed:** CARE labels, sovereignty overlays, and telemetry baked in.

---

## 🗂️ Directory Layout

~~~~~text
web/
└─ src/
   └─ features/
      └─ story/
         README.md               # This file — Story Nodes overview
         story-card.tsx          # React component for narrative cards
         story-context.ts        # Story selection + syncing context
         useStory.ts             # Data-fetching hook for nodes + AI summaries
         story-service.ts        # API calls to /api/story and /api/focus
         story-metadata.json     # Story schema + version metadata
         utils/
         ├─ formatters.ts        # Markdown → HTML, media + link handling
         └─ governance.ts        # CARE tags, sovereignty filters, visibility rules
~~~~~

---

## 🧩 Story Node Schema (Conceptual)

Story Nodes implement the KFM Story Node design described in:

- `docs/architecture/story-nodes.md`  
- `docs/architecture/focus_mode/AI-Powered Focus Mode for the Kansas Frontier Matrix.pdf`  

Each Story Node is a **narrative atom** with:

- Narrative content (`narrative.body` in Markdown).  
- A time interval (`spacetime.when` with `start`, `end`, `precision`).  
- A geometry (`spacetime.geometry` as Point/Polygon/MultiPolygon).  
- Relations to other entities (events, places, people, docs, datasets).  
- Optional STAC hooks (layer overlays, evidence rasters).  
- Governance payload (CARE, sovereignty, licensing).

### Example Story Node (JSON)

~~~~~json
{
  "id": "story-fort-larned-1859",
  "type": "story-node",
  "title": "Fort Larned on the Santa Fe Trail",
  "summary": "Established in 1859, Fort Larned protected traffic along the Santa Fe Trail and became a site for treaty councils.",
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
    { "rel": "located_in", "target": "place-pawnee-county" },
    { "rel": "precedes", "target": "story-medicine-lodge-treaty-1867" }
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

## ⚙️ Data Flow & Focus Mode Integration

~~~~~mermaid
flowchart LR
  NEO["Story + Entity Graph<br/>Neo4j · Lineage · STAC refs"]
    --> API["/api/story/{id}<br/>Story API Layer"]
  API --> FOCUS["Focus Transformer v2.x<br/>AI summaries · Why-This explanations"]
  FOCUS --> CTX["Story Context<br/>useStory + story-context"]
  CTX --> CARD["StoryCard<br/>React Component"]
  CARD --> SYNC["Timeline + Map + Focus Sync<br/>via shared contexts"]
  CARD --> TELE["Web Telemetry<br/>web-story-v1 events"]
~~~~~

**Story selection channels**

- **From Map:** user clicks a feature → nearest Story Node is loaded.  
- **From Timeline:** user scrubs to a year or interval → Story Nodes overlapping the range are shown.  
- **From Focus Mode:** focusing on an entity pulls relevant Story Nodes into the narrative sidebar.  

**Focus Mode handshake**

- Story Node includes relations and evidential datasets; Focus Mode uses those to answer “Why this story?” with neo4j queries and STAC lineage.

---

## 🖥️ React Component — `StoryCard`

~~~~~text
export function StoryCard({ node }) {
  const id = node.id;
  const when = node.spacetime?.when;
  const geom = node.spacetime?.geometry;
  const coordinates = geom?.type === "Point" ? geom.coordinates : null;

  return (
    <article
      aria-labelledby={`${id}-title`}
      className="story-card rounded-2xl shadow-md p-4 bg-surface"
    >
      <header className="flex flex-col gap-1">
        <h2 id={`${id}-title`} className="text-xl font-semibold">
          {node.title}
        </h2>
        {node.summary && (
          <p className="text-sm text-muted-foreground">{node.summary}</p>
        )}
      </header>

      <section
        className="mt-3 prose max-w-none"
        aria-label="Story narrative"
        // HTML is sanitized in formatters.ts before this point
        dangerouslySetInnerHTML={{ __html: node.narrativeHtml }}
      />

      <footer className="mt-3 flex flex-wrap gap-3 text-xs text-muted-foreground">
        {when && (
          <span>
            🕰 {when.start} – {when.end}
            {when.precision ? ` (${when.precision})` : ""}
          </span>
        )}
        {coordinates && Array.isArray(coordinates) && (
          <span>
            📍 {coordinates.map((c) => c.toFixed?.(3) ?? c).join(", ")}
          </span>
        )}
      </footer>
    </article>
  );
}
~~~~~

**Accessibility**

- Semantic containers + ARIA labels.  
- Compatible with screen readers and Focus Mode updates.  
- Easily themed via Tailwind / design tokens.

---

## 🧭 Timeline & Map Synchronization

Story Nodes are **time-aware** and **geo-aware**:

- **Timeline:**  
  - A Story Node is “active” when `currentRange` intersects `node.spacetime.when`.  
  - Cards fade in/out as the user scrubs the Timeline.

- **Map:**  
  - When a Story Node is selected, a highlight layer is added at its geometry.  
  - Map viewport animates toward the node’s centroid, respecting user motion preferences.

- **Shared Context:**  
  - `story-context.ts` exposes `currentStoryId`, `timelineRange`, `mapFocus`, and event handlers for cross-component orchestration.

---

## 📊 Telemetry & Governance (web-story-v1)

Story Node interactions push events into the **Web Telemetry** system (`web-telemetry-v2` overall; `web-story-v1` feature schema slice).

**Example Telemetry Event**

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

**Integration points**

- **Telemetry sink:**  

  ~~~~~text
  ../../../releases/v10.3.2/focus-telemetry.json
  ~~~~~

- **Governance ledger:**  

  ~~~~~text
  ../../../docs/reports/audit/web-telemetry-governance.json
  ~~~~~

---

## ⚖️ FAIR+CARE Governance

Story Nodes are **governance-aware UI primitives**:

- `governance.ts` applies:

  - CARE tags (`public`, `restricted`, `sensitive`).  
  - Sovereignty overlays (tribal lands, cultural sites, protected ecologies).  
  - License restrictions (e.g., “display only summary”, “no maps”, “no image thumbnails”).

- UI behavior by CARE tag:

  | CARE Tag      | Behavior                                                         |
  |---------------|------------------------------------------------------------------|
  | `public`      | Full narrative and map integration allowed.                      |
  | `restricted`  | Summary-only; certain endpoints require authenticated roles.     |
  | `sensitive`   | Node hidden or replaced with generic explanation / consent flow. |

- All filters are **telemetry-visible**, so governance can see where nodes were hidden or redacted.

---

## ♿ Accessibility Highlights

- Story panel respects **high-contrast**, **prefers-reduced-motion**, and **font scaling**.  
- Cards are keyboard navigable and grouped as a logical reading order.  
- A11y scanner (from Web Telemetry reporters) also assesses Story UI:

  - Missing alts for historical imagery  
  - Insufficient color contrast in Story tags or metadata  
  - Focus traps or inaccessible links  

Findings are aggregated under:

~~~~~text
reports/audit/ui_a11y_summary.json
~~~~~

---

## 🧪 Developer Workflow

**Hook Setup**

- Import `useStory` and `useTelemetry` to wire Story Nodes into your view.

~~~~~text
const { story, isLoading } = useStory(currentStoryId);
const { log } = useTelemetry("story");

useEffect(() => {
  if (story) {
    log("story-view", { story_id: story.id, source: "focus-mode" });
  }
}, [story, log]);
~~~~~

**Governance Filtering**

- Use `governance.ts` helpers to filter Story Nodes for the current user / CARE profile:

~~~~~text
import { canDisplayStory } from "./utils/governance";

if (!canDisplayStory(node, currentUserRoles)) {
  return null;
}
~~~~~

---

## 🧾 Internal Citation

~~~~~text
Kansas Frontier Matrix (2025). Story Nodes — Narrative Graph & Temporal Explorer (v10.3.2).
A FAIR+CARE-governed narrative interface connecting Neo4j entities, STAC layers, and Focus Mode
through accessible, telemetry-aware Story Cards aligned with MCP-DL v6.3.
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author       | Summary                                                                 |
|--------:|------------|-------------|-------------------------------------------------------------------------|
| v10.3.2 | 2025-11-14 | `@kfm-web`  | Upgraded Story Nodes to KFM v10.3; integrated Web Telemetry v2, FAIR+CARE overlays, Focus Mode v2.4 sync, and governance helpers. |
| v9.9.0  | 2025-11-08 | `@kfm-web`  | Initial Story Node feature with AI narrative rendering and CARE tags.  |
| v9.8.0  | 2025-11-05 | `@kfm-ui`   | Timeline + Map synchronization and accessibility enhancements.         |

---

<div align="center">

**Kansas Frontier Matrix — Story Nodes**  
📖 Living Narratives · 🗺 Temporal & Spatial Context · 🔐 FAIR+CARE Ethics · 📡 Telemetry-Aware UX  

© 2025 Kansas Frontier Matrix — MIT License  

[Back to Web Features](../README.md) · [Governance Charter](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>
