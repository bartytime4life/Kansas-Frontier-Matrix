</div>

---

## 🧭 Overview

The **DetailPanel** component presents contextual information about a **selected entity or event**  
within the Kansas Frontier Matrix application. It is the bridge between the interactive **map**,  
**timeline**, and **AI summaries**, providing deep-dive views of the people, places, and events  
that populate the Frontier Matrix knowledge graph.

The panel aggregates and formats data from multiple sources:
- Structured graph data from `/api/entity/{id}`
- AI-generated summaries (from `/api/ask`)
- Related spatial and temporal context (linked map markers or timeline intervals)
- Provenance citations from underlying documents, treaties, and datasets

Designed to be responsive, accessible, and semantically rich, the DetailPanel helps transform  
data into narrative — turning layers of Kansas’s history into readable, traceable insights.

---

## 🧱 Directory Structure

```text
web/src/components/DetailPanel/
├── DetailPanel.tsx          # Main panel component
├── DetailSection.tsx        # Subcomponent for grouped info (summary, sources, timeline)
├── CitationList.tsx         # Renders document/source citations
├── RelatedEntities.tsx      # Lists linked people, places, and events
├── styles.scss              # Theming + responsive design
└── __tests__/               # Jest + RTL tests for rendering and API integration


⸻

⚙️ Component Architecture

flowchart TD
  SEL["SelectionContext\n(selectedEntity)"] --> API["API\nGET /entity/{id}"]
  API --> DP["DetailPanel\n(summary, metadata, sources)"]
  DP --> AI["AIAssistant\ncontextual Q&A"]
  DP --> MAP["MapView\nhighlight location"]
  DP --> TL["TimelineView\nfocus on date range"]
  DP --> CITE["CitationList\nprovenance sources"]
%% END OF MERMAID


⸻

🧩 Key Features

Feature	Description	Data Source
Entity Overview	Displays name, type, and summary of selected entity/event.	Neo4j Graph (/api/entity/{id})
AI Summary Integration	Fetches and displays AI-generated synopsis (short, medium, long forms).	/api/ask?id={entityId}
Citations & Provenance	Shows original sources (documents, treaties, datasets) with links and metadata.	Knowledge Graph MENTIONS relationships
Linked Entities	Lists people, places, and events related to the entity.	Graph relationships (PARTICIPATED_IN, OCCURRED_AT)
Temporal Context	Highlights associated timeline range or specific date.	TimelineContext
Spatial Context	Triggers map zoom to entity’s coordinates or region.	MapContext
Accessibility	ARIA-compliant panel with keyboard focus management and live region updates.	WCAG 2.1 AA


⸻

💬 Example Usage

import React from "react";
import { useSelection } from "../../context/SelectionContext";
import { DetailPanel } from "./DetailPanel";

export function RightSidebar() {
  const { selected } = useSelection();
  return (
    <aside className="detail-sidebar">
      {selected ? <DetailPanel entityId={selected.id} /> : <p>Select an item to view details.</p>}
    </aside>
  );
}


⸻

🧠 TypeScript Interface

export interface DetailPanelProps {
  entityId: string;
}

export interface EntityDetail {
  id: string;
  label: string;
  type: "Person" | "Place" | "Event" | "Document";
  description?: string;
  summary?: string;
  coordinates?: [number, number];
  startDate?: string;
  endDate?: string;
  relatedEntities?: { id: string; label: string; type: string }[];
  citations?: Citation[];
}

export interface Citation {
  id: string;
  title: string;
  sourceUrl?: string;
  license?: string;
  excerpt?: string;
}


⸻

🧩 Rendering Flow

sequenceDiagram
  participant U as User
  participant S as SelectionContext
  participant API as FastAPI / GraphQL
  participant D as DetailPanel
  participant AI as AI Summarizer

  U->>S: Select entity on map/timeline
  S->>D: Provide entityId
  D->>API: GET /entity/{id}
  API-->>D: Returns metadata, relationships, sources
  D->>AI: Optionally fetch AI summary (/api/ask)
  AI-->>D: Returns summary text with citations
  D-->>U: Renders full detail view + source links
%% END OF MERMAID


⸻

🎨 Layout & Styling
	•	Width: 30–40% of viewport on desktop; collapses to drawer on mobile.
	•	Sections: Summary, Details, Linked Entities, Sources, Timeline.
	•	Animation: Slide-in/out transitions powered by Framer Motion.
	•	Colors: Adaptive to ThemeContext (light/dark modes).
	•	Typography: Uses semantic headings (<h2>, <h3>) and accessible link colors.

⸻

🧪 Testing

Test Case	Description
API Integration	Mocks /api/entity/{id} and /api/ask to ensure correct rendering.
Rendering Sections	Verifies Summary, Linked Entities, and Citations appear.
Keyboard Navigation	Tests focus order and tab key accessibility.
Error Handling	Ensures fallback UI displays on failed API fetch.
Snapshot Testing	Validates consistent rendering across themes.

Frameworks: Jest, React Testing Library, Mock Service Worker (MSW), axe-core.

Target coverage: ≥ 90% lines / branches.

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	/api/entity/{id} (graph data), /api/ask (AI summary), SelectionContext
Outputs	HTML panel rendered with text, markdown, and linked entities
Dependencies	React, Axios, Markdown-it, Framer Motion
Integrity	Checked via CI — unit tests, accessibility scan, markdown sanitization


⸻

🔗 Related Documentation
	•	Web Frontend Components
	•	AIAssistant Component
	•	Context — Selection & Timeline
	•	Web UI Architecture

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — Developed under the Master Coder Protocol (MCP)
for clarity, provenance, and semantic interoperability.

“Every document has a voice — the Detail Panel lets Kansas’s archives speak.”

