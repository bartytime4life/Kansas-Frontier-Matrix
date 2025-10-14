<div align="center">

# 🧮 Kansas Frontier Matrix — Web Frontend Utilities  
`web/src/utils/`

**Helper Functions · API Clients · Data Parsers · Map & Timeline Utilities**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../../.github/workflows/ci.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../.github/workflows/codeql.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-green)](../../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Web Frontend Utilities"
version: "v1.2.0"
last_updated: "2025-10-13"
owners: ["@kfm-web", "@kfm-data"]
tags: ["web","utils","api","maplibre","timeline","mcp","typescript"]
license: "MIT"
---

🧭 Overview

The web/src/utils/ directory provides shared, pure utility modules that support the Kansas Frontier Matrix Web UI —
simplifying logic used across the Map, Timeline, AI Assistant, and Data Layers.

These modules enforce MCP reproducibility, type-safety, and deterministic outputs, enabling:
	•	consistent formatting and parsing for STAC, GeoJSON, and API responses,
	•	reusable transformations and temporal scaling,
	•	clear data provenance and zero side effects.

Each function includes JSDoc / TSDoc annotations, version tracking through Git, and test coverage ≥ 85%.

⸻

🧱 Directory Structure

web/src/utils/
├── apiClient.ts         # REST/GraphQL wrappers for API calls
├── mapUtils.ts          # MapLibre helpers (layers, markers, transforms)
├── timelineUtils.ts     # Time parsing, scaling, interpolation
├── aiUtils.ts           # AI/LLM bridge (summaries, Q&A)
├── formatters.ts        # Locale-aware date, number, and label formatting
├── dataParser.ts        # Convert API payloads → internal app structures
├── hooks.ts             # Custom hooks (useFetch, useDebounce, useResizeObserver)
├── constants.ts         # Shared config (API URLs, STAC paths, layer constants)
└── __tests__/           # Jest unit tests for all utils


⸻

⚙️ Core Modules

File	Purpose	Example Function
apiClient.ts	Standardized HTTP/GraphQL client with retry + logging.	getEvents(start,end)
mapUtils.ts	MapLibre helpers for layer toggles, transitions, geometry math.	addLayer(map,id,url,opacity)
timelineUtils.ts	Normalize and map temporal data to pixels/time ranges.	timeToPixel(date,scale)
aiUtils.ts	Interface to /api/ask and /api/entity/{id} endpoints.	fetchAISummary(entityId)
formatters.ts	Text/date/number formatting with localization.	formatDateHuman(date)
dataParser.ts	Transform raw API JSON → Timeline/Map structures.	parseEventData(json)
hooks.ts	Reusable logic for async ops and UI responsiveness.	useDebounce(fn,delay)
constants.ts	Centralized URLs and configuration constants.	API_BASE_URL, LAYER_CONFIG_PATH


⸻

🧩 Example Usage

// Load and parse timeline events (1850–1900)
import { getEvents } from "./apiClient";
import { parseEventData } from "./dataParser";
import { formatDateHuman } from "./formatters";

export async function loadTimeline(start:string, end:string){
  const data = await getEvents(start,end);
  const events = parseEventData(data);
  console.info(`Loaded ${events.length} events from ${formatDateHuman(start)}–${formatDateHuman(end)}.`);
  return events;
}


⸻

🗺️ Map & Timeline Utility Relationships

flowchart TD
  A["MapView<br/>(MapLibre GL JS)"] --> B["mapUtils.ts<br/>layer & marker ops"]
  A --> C["formatters.ts<br/>popup/legend labels"]
  D["TimelineView<br/>(Canvas/D3)"] --> E["timelineUtils.ts<br/>time→pixel transforms"]
  D --> C
%% END OF MERMAID


⸻

🤖 AI Utilities Integration

aiUtils.ts bridges the frontend and backend AI/NLP endpoints:
	•	/api/ask — free-form natural language Q&A
	•	/api/entity/{id} — contextual summaries for specific nodes

Handles:
	•	Prompt submission, streaming responses, and error fallbacks
	•	Caching and memoization of previous responses
	•	Inline citation extraction linking back to Neo4j entities
	•	Output shaping for AIAssistant panel rendering

Responses follow:
{ answer: string; citations: { id: string; label: string; source: string; }[] }

⸻

🧮 Coding Standards
	•	Style — ESLint + Prettier; enforced via CI
	•	Docs — JSDoc/TSDoc for all public exports
	•	Testing — Jest + RTL; __tests__/ per file; coverage ≥ 85%
	•	Determinism — pure functions only; no globals or side effects
	•	Typing — Strict TypeScript types; utility generics (T extends Record<string,any>)

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	STAC (config/layers.json), API payloads (/events, /entity, /ask)
Outputs	Parsed objects (Event, Entity, Layer) consumed by Map/Timeline components
Dependencies	React, Axios, MapLibre GL JS, D3
Integrity	Versioned via Git; validated by CI checksums & CodeQL scans


⸻

🧠 MCP & Governance Alignment

MCP Principle	Implementation
Documentation-first	Inline TSDoc + per-file README comments
Reproducibility	Deterministic utilities; CI regression tests
Open Standards	GeoJSON, STAC, DCAT, ISO temporal format
Provenance	API source + STAC item linked in metadata
Auditability	Unit test coverage; logs of inputs/outputs retained in CI
Versioning	Semantic commits; utilities follow SemVer via package version field


⸻

🧰 Example: Deterministic Formatter

/**
 * Format ISO date into human-friendly year/month.
 * @param isoDate - ISO 8601 date string
 * @returns formatted label, deterministic across locales
 */
export function formatDateHuman(isoDate:string):string {
  const d = new Date(isoDate);
  return d.toLocaleDateString("en-US", { year: "numeric", month: "short" });
}


⸻

🧩 Test Example

import { timeToPixel } from "../timelineUtils";

describe("timelineUtils", () => {
  it("maps ISO date to correct pixel", () => {
    const scale = { start: 1800, end: 1900, width: 1000 };
    const result = timeToPixel("1850-01-01", scale);
    expect(result).toBe(500);
  });
});


⸻

🧭 Reproducibility Hooks
	•	🧱 Deterministic build — Vite caching + dependency pins (package-lock.json)
	•	🔒 CodeQL / Trivy — catch vulnerable deps
	•	🧪 Pre-commit — lint, typecheck, and test before merge
	•	🧾 Checksum log — optional SHA256 per compiled file in dist/
	•	📦 Immutable imports — import type declarations to avoid runtime pollution

⸻

🧮 Performance Considerations
	•	Memoize parsed data; avoid re-parsing identical payloads
	•	Preprocess STAC collections at build-time (static caching)
	•	Use lazy imports for heavy libraries (e.g., D3 modules)
	•	Avoid blocking I/O in utils; always async fetch wrappers

⸻

🔗 Related Documentation
	•	Web Frontend Overview — web/README.md
	•	Web UI Architecture — web/ARCHITECTURE.md
	•	API Layer Reference — ../docs/architecture.md
	•	Monorepo Design — ../docs/monorepo.md

⸻

📜 License & Credits

Released under the MIT License.
© 2025 Kansas Frontier Matrix — Utilities follow the Master Coder Protocol (MCP) for transparency, reproducibility, and scientific integrity.

“Utilities are the silent scaffolds — unseen, but holding the frontier together.”

