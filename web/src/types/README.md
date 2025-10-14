<div align="center">


🧩 Kansas Frontier Matrix — Web Frontend Types

web/src/types/

Shared TypeScript Definitions · Data Models · API Interfaces

</div>



⸻

🧭 Overview

The web/src/types/ directory defines all TypeScript type declarations and interfaces shared across
the Kansas Frontier Matrix (KFM) Web Application. These definitions guarantee type safety, semantic interoperability, and strict schema alignment between frontend modules and backend API contracts.

All type definitions follow MCP-DL v6.2 — the Master Coder Protocol Documentation Language — ensuring reproducibility, provenance, and alignment with FAIR data and CIDOC CRM / OWL-Time ontologies.

⸻

🗂️ Directory Layout

web/src/types/
├── ai.d.ts         # AI assistant responses, citations, extracted entities
├── api.d.ts        # REST/GraphQL payloads and standardized error envelopes
├── data.d.ts       # STAC & GeoJSON definitions for geospatial assets
├── entity.d.ts     # Person, Place, Organization, Document, Event interfaces
├── map.d.ts        # MapLibre layer, style, and legend metadata
├── timeline.d.ts   # Timeline event, zoom scale, and range interfaces
├── ui.d.ts         # Shared UI/ARIA props (panels, toasts, dialogs)
└── index.d.ts      # Root barrel export for global import convenience

Each file exports reusable interfaces, enums, and utility types shared by React components,
hooks, API clients, and MapLibre integrations — enforcing one consistent source of truth.

⸻

🧱 Core Type Interfaces

Type	Description	Defined In / Source
Event	Historical event entity with time, location, and category fields	/api/events
Entity	Abstract base type for people, places, and organizations	/api/entity/{id}
Layer	Map overlay metadata derived from STAC catalog	data/stac/*.json
AIResponse	Schema for AI Assistant responses and evidence	/api/ask
TimelineRange	Visible time window & zoom factor for timeline	timeline.d.ts
GeoFeature	GeoJSON-compliant spatial feature for maps	map.d.ts
STACItem	Geospatial dataset object (STAC 1.0)	data.d.ts
DocumentLink	Metadata describing linked sources	entity.d.ts


⸻

🧩 Example: Event Type Definition

// event.d.ts
export type EventCategory =
  | "battle" | "treaty" | "flood" | "drought"
  | "settlement" | "wildfire" | "storm" | "other";

export interface Event {
  id: string;
  title: string;
  description?: string;
  category: EventCategory;
  startDate: string;              // ISO 8601 start
  endDate?: string;               // ISO 8601 end (interval)
  placeId?: string;               // linked Place ID
  coordinates?: [lon: number, lat: number];
  relatedEntityIds?: string[];    // People / Orgs / Docs
  importance?: number;            // timeline scaling weight
  source?: string;                // dataset or doc ID
  confidence?: number;            // 0-1 uncertainty
  tags?: string[];                // custom keywords
}

This schema ensures strong typing for map, timeline, and AI modules and encodes
temporal intervals + confidence in accordance with OWL-Time and PROV-O.

⸻

🧠 Data Model Relationships

flowchart TD
  A["Event"] --> B["Place"]
  A --> C["Document"]
  A --> D["AIResponse"]
  B --> E["GeoFeature (Map)"]
  D --> F["Entity (People / Orgs)"]
  F --> A
%%END OF MERMAID%%

Interpretation: Types mirror Neo4j graph schema — Event ↔ Place ↔ Document ↔ Entity,
enabling coherent visualizations and semantic traversal in both the map and timeline UIs.

⸻

🗺️ STAC / GeoJSON Integration

export interface STACAsset {
  href: string;
  type?: string;
  roles?: ("data"|"overview"|"thumbnail"|"metadata")[];
  title?: string;
}

export interface STACItem {
  id: string;
  type: "Feature";
  bbox?: [number, number, number, number];
  geometry?: GeoJSON.Geometry;
  properties: {
    datetime?: string;
    start_datetime?: string;
    end_datetime?: string;
    license?: string;
    "kfm:theme"?: string;
  };
  assets: Record<string, STACAsset>;
  links?: { rel: string; href: string; type?: string }[];
}

This structure allows direct ingestion from STAC 1.0 catalogs and seamless linking
between backend assets → map layers → timeline overlays.

⸻

⚙️ TypeScript Configuration
	•	Compiler Settings: strict, noImplicitAny, esModuleInterop, skipLibCheck
	•	Global Exports: index.d.ts exposes all interfaces to the project scope
	•	Validation: tsc --noEmit + ESLint run in CI pipelines (.github/workflows/ci.yml)
	•	IDE Support: VS Code IntelliSense + path aliases (@types, @api, @ui)

⸻

🧩 Usage Example

import { Event, Layer } from "../types";

function renderEventMarker(event: Event, layer: Layer) {
  console.log(`Rendering ${event.title} on layer ${layer.id}`);
}

The import pattern ensures type integrity between React components,
utility functions, and backend API schemas.

⸻

♿ Accessibility (ARIA Helpers)

export interface AriaLabelled {
  "aria-label"?: string;
  "aria-describedby"?: string;
  role?: string;
}

export interface PanelProps extends AriaLabelled {
  title: string;
  isOpen: boolean;
  onClose: () => void;
}

Consistent with WCAG 2.1 AA, these types standardize accessibility props across UI components.

⸻

🧾 Provenance · Integrity · Semantics

Field	Description
Inputs	Backend schemas (FastAPI Pydantic / GraphQL SDL)
Outputs	TypeScript .d.ts definitions consumed by Web UI
Dependencies	React · TypeScript · MapLibre GL · @types/geojson
Integrity	Versioned in Git · Validated by CI TypeScript compiler
Ontology Links	crm:E5_Event, crm:E31_Document, time:Interval, prov:wasDerivedFrom

{
  "@context": "https://kfm.org/contexts/kfm.context.jsonld",
  "@type": "crm:E73_Information_Object",
  "name": "web/src/types/",
  "prov:wasDerivedFrom": ["API Schemas", "STAC Catalog"]
}


⸻

🧪 MCP Compliance Checklist

✅ Documentation-first
✅ Type-safe & strictly validated
✅ Provenance tracked (links + citations)
✅ Semantic / FAIR alignment (STAC, GeoJSON, CIDOC CRM, OWL-Time)
✅ Accessibility integrated (WCAG 2.1 AA)

⸻

🔗 Related Documentation
	•	Web Frontend Overview → web/README.md
	•	Web UI Architecture → docs/architecture/web-ui.md
	•	Knowledge Graph API Reference → docs/api/graph.md
	•	Monorepo Repository Design → docs/repo/monorepo.md

⸻

🧩 Version & Change Log

Field	Value
Doc Version	v6.2
Last Updated	2025-10-14
Maintainer	Web Platform Team (@KansasFrontierMatrix)


⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — All code and documentation follow the Master Coder Protocol (MCP-DL v6.2)
for clarity, semantic alignment, and open reproducibility.

“Strong types make strong frontiers.”

⸻
