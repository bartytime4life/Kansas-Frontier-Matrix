<div align="center">

# 🧮 Kansas Frontier Matrix — Web Frontend Utilities  
`web/src/utils/`

**Helper Functions · API Clients · Data Parsers · Map & Timeline Utilities**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../../.github/workflows/ci.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../.github/workflows/codeql.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../LICENSE)

</div>

---

## 🧭 Overview

The `web/src/utils/` directory houses **shared utility functions** and **helper modules** that support  
the Kansas Frontier Matrix Web UI — simplifying logic used across components like the Map, Timeline,  
and AI Assistant. Utilities here maintain **clean separation of concerns**, keeping React components  
focused on rendering and UI interaction.

All utilities adhere to **Master Coder Protocol (MCP)** reproducibility and documentation standards,  
including inline JSDoc-style comments, version control through Git commits, and deterministic outputs  
for consistent client-side rendering.

---

## 🧱 Directory Structure

```text
web/src/utils/
├── apiClient.js          # Axios / Fetch wrappers for REST & GraphQL requests
├── mapUtils.js           # MapLibre helpers (layer toggles, coordinate transforms)
├── timelineUtils.js      # Time parsing, scaling, and range utilities
├── aiUtils.js            # AI/LLM interface (summarization, Q&A response handling)
├── formatters.js         # Common date, number, and text formatting functions
├── dataParser.js         # Converts API JSON → internal structures for timeline & map
├── hooks.js              # Custom React hooks (useFetch, useDebounce, useResizeObserver)
└── constants.js          # Shared constants (API endpoints, STAC catalog paths)


⸻

⚙️ Key Modules

File	Purpose	Example Function
apiClient.js	Standardized HTTP client with error handling & logging.	getEvents(start, end)
mapUtils.js	Controls MapLibre layers, markers, and camera transitions.	addLayer(map, id, url, opacity)
timelineUtils.js	Normalizes temporal data and scales timeline positions.	timeToPixel(date, scale)
aiUtils.js	Connects to /ask endpoint and formats AI assistant output.	fetchAISummary(entityId)
formatters.js	Handles locale-based formatting for UI text.	formatDateISOtoHuman(date)
dataParser.js	Transforms backend payloads into React-friendly structures.	parseEventData(json)
hooks.js	Encapsulates reusable logic for async operations and UI responsiveness.	useDebounce(fn, delay)
constants.js	Provides shared URLs, API routes, and configuration.	API_BASE_URL, LAYER_CONFIG_PATH


⸻

🧩 Example Usage

// Example: Fetch and render events between 1850–1900 on timeline
import { getEvents } from "./apiClient";
import { parseEventData } from "./dataParser";
import { formatDateISOtoHuman } from "./formatters";

async function loadTimeline(start, end) {
  const response = await getEvents(start, end);
  const events = parseEventData(response.data);
  console.log(`Loaded ${events.length} events from ${formatDateISOtoHuman(start)}–${formatDateISOtoHuman(end)}`);
  return events;
}


⸻

🗺️ Map & Timeline Utilities

flowchart TD
  A["MapView\n(MapLibre GL JS)"] --> B["mapUtils.js\nadd/remove layers"]
  A --> C["formatters.js\nstyle popups, dates"]
  D["TimelineView\n(Canvas/D3)"] --> E["timelineUtils.js\nscale/time transforms"]
  D --> C
%% END OF MERMAID


⸻

🧠 AI Utilities Integration
	•	aiUtils.js bridges the React client with the backend AI endpoints (/api/ask and /api/entity/{id}).
	•	Handles:
	•	Query submission and streaming responses.
	•	Response caching and error handling.
	•	Inline citation extraction (links to entities/events in the Neo4j graph).
	•	Outputs structured objects ready for rendering in the AI Assistant panel.

⸻

🧮 Coding Standards & Testing
	•	All utility functions include JSDoc headers (type signatures, parameter descriptions).
	•	Unit tests for each file under web/src/utils/__tests__/.
	•	Linting via ESLint + Prettier, enforced through CI.
	•	Coverage threshold: ≥ 85% for all utils.
	•	Each exported function must be deterministic and pure (no global side effects).

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	STAC layers.json, API endpoint data (/events, /entity, /ask)
Outputs	Formatted, parsed objects rendered in Map & Timeline components
Dependencies	React, Axios, MapLibre GL, D3.js
Integrity	Versioned in Git with semantic commits and CI checksums


⸻

🔗 Related Documentation
	•	Web Frontend Overview
	•	Web UI Architecture
	•	API Layer Reference
	•	Monorepo Repository Design

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — Documentation and code follow the Master Coder Protocol
for reproducibility, clarity, and open access.

“Utilities are the silent scaffolds — unseen, but holding the frontier together.”

