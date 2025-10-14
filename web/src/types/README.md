<div align="center">


🧩 Kansas Frontier Matrix — Web Frontend Types

web/src/types/

Shared TypeScript Definitions · Data Models · API Interfaces

</div>



⸻

🧭 Overview

web/src/types/ contains the single source of truth for all shared TypeScript interfaces, types, and enums used by the KFM web app.
These definitions formalize the frontend↔backend contract (FastAPI/GraphQL → React/MapLibre) and align with the Neo4j knowledge graph schema and STAC/GeoJSON geospatial standards.

This module implements MCP-DL v6.2: documentation-first, ontology-aware, and reproducible definitions that reinforce type safety, clarity, and interoperability across the Web UI.

⸻

📚 Directory Layout

web/src/types/
├── ai.d.ts         # AI assistant responses, citations, extracted entities
├── api.d.ts        # REST/GraphQL response payloads + error envelopes
├── data.d.ts       # STAC items, assets, GeoJSON Feature/Geometry wrappers
├── entity.d.ts     # Person, Place, Organization, Document, Event node shapes
├── map.d.ts        # MapLibre layer specs, style & legend contracts
├── timeline.d.ts   # Timeline event, range, zoom/scale, lane allocation
├── ui.d.ts         # Shared UI props (panels, toasts, dialogs), ARIA helpers
└── index.d.ts      # Re-exports for ergonomic imports

Each file exports reusable interfaces and discriminated unions to guarantee consistent shapes in React components, hooks, utils, and API clients.

⸻

🧱 Core Type Interfaces

Type	Description	Source of Truth
Event	Historical event with time, place, relations, and category	/api/events
Entity	Base for Person, Place, Organization, Document	/api/entity/{id}
Layer	Map overlay metadata derived from STAC items	data/stac/*.json
AIResponse	AI answer text, evidence, and extracted entities	/api/ask
TimelineRange	Visible time window and zoom/scale state	TimelineView
GeoFeature	GeoJSON-compliant features for map rendering	data.d.ts
STACItem	Geospatial dataset (assets, bbox, datetime, license)	data.d.ts
DocumentLink	Source doc metadata (title, URL, license, provider)	entity.d.ts


⸻

🧩 Example: Event (semantic, timeline-ready)

// entity.d.ts

export type EventCategory =
  | "battle" | "treaty" | "flood" | "drought"
  | "settlement" | "wildfire" | "storm" | "other";

export interface Event {
  id: string;
  title: string;
  description?: string;
  category: EventCategory;
  startDate: string;              // ISO 8601
  endDate?: string;               // ISO 8601 (interval support)
  placeId?: string;               // links to Place
  coordinates?: [lon: number, lat: number];
  relatedEntityIds?: string[];    // Person/Org/Doc ids
  importance?: number;            // timeline scaling (0..1 or 0..100)
  source?: string;                // dataset/doc id
  confidence?: number;            // 0..1 (uncertainty surfacing)
  tags?: string[];                // free-form keywords
}

Why: This shape supports interval events, semantic linking, timeline importance, and confidence/uncertainty, per MCP guidance.

⸻

🧠 Data Model Relationships

flowchart TD
  A["Event"] --> B["Place"]
  A --> C["Document"]
  A --> D["AIResponse"]
  B --> E["GeoFeature (Map)"]
  D --> F["Entity (People, Orgs)"]
  F --> A
%%END OF MERMAID%%

Relationships mirror the backend graph: Events ↔ Places ↔ Documents/Entities; AI output enriches and cites graph elements to maintain provenance.

⸻

🗺️ STAC & GeoJSON Alignment (data.d.ts)

export interface STACAsset {
  href: string;
  type?: string;              // e.g., "image/tiff; application=geotiff; profile=cloud-optimized"
  roles?: ("data"|"overview"|"thumbnail"|"metadata")[];
  title?: string;
}

export interface STACItem {
  id: string;
  type: "Feature";
  bbox?: [number,number,number,number];
  geometry?: GeoJSON.Geometry;
  properties: {
    datetime?: string;
    start_datetime?: string;
    end_datetime?: string;
    license?: string;
    "kfm:theme"?: string;     // custom extension for UI theming
  };
  assets: Record<string, STACAsset>;
  links?: { rel: string; href: string; type?: string }[];
}

Why: Using canonical STAC shapes ensures layer metadata flows directly from the catalog to MapLibre layers and UI legends.

⸻

⚙️ TypeScript & Tooling
	•	tsconfig.json: "strict": true, "noImplicitAny": true, "esModuleInterop": true, "skipLibCheck": true.
	•	Global exports: index.d.ts aggregates all interfaces to simplify imports.
	•	Validation: tsc --noEmit and ESLint run in CI; PRs must pass type checks.
	•	DX: VSCode IntelliSense, path aliases (e.g., @types, @api, @ui) recommended for ergonomics.

⸻

🧩 Usage Example

import { Event, Layer } from "../types";

export function renderEventMarker(event: Event, layer: Layer) {
  console.debug(`Rendering ${event.title} on layer ${layer.id}`);
}

Shared types eliminate “stringly-typed” code and keep React components, utils, and API clients in sync.

⸻

♿ Accessibility Helpers (ui.d.ts)

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

Encourages consistent WCAG 2.1 AA props in shared components.

⸻

🧾 Provenance · Integrity · Semantics

Inputs: Backend Pydantic/GraphQL schemas, STAC catalog, ontology mappings
Outputs: TypeScript definitions consumed across the Web UI
Dependencies: React, TypeScript, MapLibre GL, @types/geojson
Integrity: Versioned in Git; validated in CI; semantic fields align to:
	•	CIDOC CRM: Event ≈ crm:E5_Event, Document ≈ crm:E31_Document
	•	OWL-Time: startDate/endDate encode intervals
	•	PROV-O: source + AI citations for evidence chains

Optional JSON-LD snippet (for docs/tests):

{
  "@context": "https://kfm.org/contexts/kfm.context.jsonld",
  "@type": "crm:E73_Information_Object",
  "name": "web/src/types",
  "prov:wasDerivedFrom": ["api schemas", "stac catalog"]
}


⸻

🧪 MCP Checks (Docs · MCP v6.2)
	•	✅ Documentation-first (this README + typed contracts)
	•	✅ Reproducible (CI tsc, ESLint)
	•	✅ Provenance (source pointers + citations in AI types)
	•	✅ FAIR & Semantic (STAC, GeoJSON, CIDOC CRM, OWL-Time)
	•	✅ Accessibility hooks in UI types

⸻

🔗 Related Documentation
	•	Web Frontend Overview → web/README.md
	•	Web UI Architecture → docs/architecture/web-ui.md
	•	Knowledge Graph API Reference → docs/api/graph.md
	•	Monorepo Repository Design → docs/repo/monorepo.md

⸻

🧩 Versioning & Change Log
	•	Doc Version: v6.2
	•	Last Updated: 2025-10-14
	•	Maintainer: Web Platform Team (@KansasFrontierMatrix)

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — All code and docs follow the Master Coder Protocol for clarity, semantics, and open reproducibility.

“Strong types make strong frontiers.”