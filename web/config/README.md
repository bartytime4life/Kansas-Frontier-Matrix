<div align="center">

# ⚙️ Kansas Frontier Matrix — Web Configuration  
`web/config/`

**Application Settings · Layer Metadata · Environment Variables**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../.github/workflows/ci.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

## 🧭 Overview

The `web/config/` directory defines **configuration and metadata files** used to control  
how the Kansas Frontier Matrix web frontend loads and displays geospatial and historical data.  

Configurations link the **STAC catalog**, **API endpoints**, and **UI layer settings**,  
ensuring that the **React + MapLibre** interface dynamically adapts to data changes  
without requiring manual code modifications.

The configuration system follows **Master Coder Protocol (MCP)** design standards for  
**reproducibility**, **traceability**, and **data provenance** — every dataset loaded  
into the interface references a formal JSON configuration artifact.

---

## 🧱 Directory Structure

```text
web/config/
├── app.config.json          # Global application settings
├── layers.json              # Map + timeline layer definitions (linked to STAC)
├── themes.json              # Theme tokens and color palettes
├── env.example              # Example environment variable file (.env)
├── vite.config.ts           # Vite build configuration (React + TypeScript)
├── jest.config.js           # Jest configuration for unit tests
└── README.md                # This documentation file


⸻

🧩 Core Configuration Files

🗂️ app.config.json

Defines global settings for the web client, such as API URLs, map defaults,
and accessibility toggles.

{
  "appName": "Kansas Frontier Matrix",
  "version": "1.0.0",
  "apiBaseUrl": "https://api.frontiermatrix.org",
  "defaultMapCenter": [-98.3, 38.5],
  "defaultZoom": 6,
  "enableAI": true,
  "enableAccessibilityFeatures": true,
  "supportedLanguages": ["en", "es"],
  "contactEmail": "support@frontiermatrix.org"
}


⸻

🧭 layers.json

Defines available map and timeline layers, referencing assets from the STAC catalog.
Each entry includes a title, description, source, and visibility configuration.

[
  {
    "id": "historic_topo_1894",
    "title": "USGS Topographic Map (1894)",
    "type": "raster",
    "url": "https://data.frontiermatrix.org/maps/1894_topo.tif",
    "opacity": 0.8,
    "visible": false,
    "timeRange": { "start": "1894-01-01", "end": "1894-12-31" },
    "legend": "maps/legend_topo_1894.png",
    "license": "Public Domain"
  },
  {
    "id": "kansas_treaties",
    "title": "Kansas Treaty Boundaries",
    "type": "vector",
    "url": "https://data.frontiermatrix.org/layers/treaties.geojson",
    "visible": true,
    "opacity": 1,
    "timeRange": { "start": "1800-01-01", "end": "1900-12-31" },
    "legend": "maps/legend_treaty.png",
    "license": "CC-BY 4.0"
  }
]

These settings populate the LayerControls component and the MapView at runtime.
They are automatically validated against a JSON Schema before deployment.

⸻

🎨 themes.json

Defines color palettes and typography variables for light and dark modes.
These tokens are used by SCSS and Tailwind to maintain design consistency.

{
  "light": {
    "bg": "#ffffff",
    "text": "#111111",
    "accent": "#00b3b3",
    "grid": "#e0e0e0"
  },
  "dark": {
    "bg": "#0b1020",
    "text": "#eaeaea",
    "accent": "#00e6e6",
    "grid": "#2b2b2b"
  }
}


⸻

🌎 env.example

A template for environment variables required for local and production builds.

VITE_API_BASE_URL=https://api.frontiermatrix.org
VITE_APP_NAME=Kansas Frontier Matrix
VITE_ENABLE_AI=true
VITE_ENABLE_ACCESSIBILITY=true
VITE_MAPBOX_TOKEN=your-mapbox-or-maptiler-key

Copy this file as .env and modify values for your environment.

⸻

⚙️ Build Configuration

⚡ vite.config.ts

Configures the Vite build process for the React frontend.
	•	TypeScript support with fast Hot Module Reloading.
	•	SCSS preprocessing with Tailwind integration.
	•	Environment variable injection from .env.
	•	Asset optimization for COGs, GeoJSON, and SVGs.
	•	Aliases for simplified imports (@components, @context, @utils).

Example snippet:

import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@components": "/web/src/components",
      "@context": "/web/src/context",
      "@utils": "/web/src/utils"
    }
  },
  server: {
    port: 3000,
    open: true
  }
});


⸻

🧪 jest.config.js

Ensures consistent testing environment for all web components.

export default {
  testEnvironment: "jsdom",
  transform: { "^.+\\.(t|j)sx?$": "babel-jest" },
  moduleNameMapper: {
    "\\.(css|scss)$": "identity-obj-proxy"
  },
  setupFilesAfterEnv: ["<rootDir>/setupTests.ts"],
  collectCoverageFrom: ["web/src/**/*.{ts,tsx}"],
  coverageThreshold: {
    global: { lines: 90, branches: 80 }
  }
};


⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	STAC catalog, environment variables, dataset metadata
Outputs	Compiled config files (layers.json, app.config.json) consumed by web app
Dependencies	Node.js, Vite, TypeScript, TailwindCSS
Integrity	Validated in CI via JSON Schema checks, STAC validation, and snapshot testing


⸻

🔗 Related Documentation
	•	Web UI Architecture
	•	MapView Component
	•	LayerControls Component
	•	Monorepo Repository Design

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — Managed under the Master Coder Protocol (MCP)
for reproducible, environment-driven architecture.

“Configuration is the silent framework — it lets the frontier’s data assemble itself.”

