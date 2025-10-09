<div align="center">

# 🧩 Kansas Frontier Matrix — Web Frontend Types  
`web/src/types/`

**Shared TypeScript Definitions · Data Models · API Interfaces**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../../.github/workflows/ci.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../.github/workflows/codeql.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../LICENSE)

</div>

---

## 🧭 Overview

The `web/src/types/` directory defines all **TypeScript type declarations** and **interfaces** shared across  
the Kansas Frontier Matrix Web Application. These types ensure **type safety**, **clarity**, and **strong coupling**  
between React components, utility functions, and backend API responses.

Types here model the **data contracts** between frontend and backend — including `Event`, `Entity`,  
`Layer`, and `AIResponse` structures — ensuring the React app communicates consistently with the  
FastAPI/GraphQL API and the underlying Neo4j Knowledge Graph.

This directory forms the foundation of **code correctness** and **interoperability** for the web layer under  
the **Master Coder Protocol (MCP)** documentation-first methodology.

---

## 📚 Directory Structure

```text
web/src/types/
├── api.d.ts           # Interfaces for API responses (Events, Entities, GraphQL types)
├── data.d.ts          # STAC/GeoJSON feature definitions and spatial metadata
├── entity.d.ts        # Knowledge graph entities (Person, Place, Event, Document)
├── map.d.ts           # Map layer and overlay definitions (MapLibre GL config)
├── timeline.d.ts      # Timeline event, range, and scale structures
├── ai.d.ts            # AI Assistant response schema and metadata
├── ui.d.ts            # Shared UI props (DetailPanel, LayerControls, etc.)
└── index.d.ts         # Master type exports for global use

Each file exports reusable interfaces, types, and enums that define data shapes for
frontend–backend interoperability.

⸻

🧱 Core Type Interfaces

Type	Description	Source
Event	Represents a single historical event with date, location, and category.	/api/events
Entity	Abstract interface for people, places, and organizations.	/api/entity/{id}
Layer	Defines map overlay metadata derived from the STAC catalog.	data/stac/catalog.json
AIResponse	Schema for AI Assistant responses, including text, citations, and entities.	/api/ask
TimelineRange	Holds current visible time window and zoom factor.	TimelineView
GeoFeature	GeoJSON-compliant spatial feature used for map rendering.	map.d.ts
STACItem	Represents a geospatial dataset from the STAC catalog.	data.d.ts
DocumentLink	Metadata about source documents (title, URL, license).	entity.d.ts


⸻

🧩 Example: Event Type Definition

// event.d.ts
export interface Event {
  id: string;
  title: string;
  description?: string;
  category: "battle" | "treaty" | "flood" | "drought" | "settlement" | "other";
  startDate: string;   // ISO 8601 date
  endDate?: string;
  placeId?: string;
  coordinates?: [number, number];
  relatedEntities?: string[];
  importance?: number; // for timeline scaling
  source?: string;     // dataset or document ID
}

This type definition ensures that timeline and map components display events consistently
and that any new event data from the backend is validated at compile time.

⸻

🧠 Data Model Relationships

flowchart TD
  A["Event"] --> B["Place"]
  A --> C["Document"]
  A --> D["AIResponse"]
  B --> E["GeoFeature (Map)"]
  D --> F["Entity (People, Orgs)"]
  F --> A
%% END OF MERMAID

The types mirror relationships defined in the backend Neo4j graph schema:
Events link to Places, Documents, and Entities, forming a cohesive data graph
that feeds both the map and timeline visualizations.

⸻

⚙️ TypeScript Configuration
	•	Compiler Options: strict, noImplicitAny, and esModuleInterop are enabled in tsconfig.json.
	•	Global Declaration: index.d.ts exports all shared interfaces to global.d.ts scope.
	•	Type Validation: Enforced via ESLint and checked in CI pipelines using tsc --noEmit.
	•	IDE Support: Fully compatible with VSCode IntelliSense for autocompletion and refactoring.

⸻

🧩 Usage Example

import { Event, Layer } from "../types";

function renderEventMarker(event: Event, layer: Layer) {
  console.log(`Rendering ${event.title} on layer ${layer.id}`);
}

The import pattern above allows seamless type safety across all modules
— React components, utils, and API clients share the same source of truth.

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	Backend API schemas (FastAPI Pydantic, GraphQL SDL)
Outputs	TypeScript definitions (.d.ts) used across frontend
Dependencies	React, TypeScript, MapLibre GL, GeoJSON typings
Integrity	Versioned in Git; validated by TypeScript compiler in CI


⸻

🔗 Related Documentation
	•	Web Frontend Overview
	•	Web UI Architecture
	•	Knowledge Graph API Reference
	•	Monorepo Repository Design

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — All code and documentation follow the Master Coder Protocol
for clarity, semantic alignment, and open reproducibility.

“Strong types make strong frontiers.”

