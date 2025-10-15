<div align="center">

# ⚙️ Kansas Frontier Matrix — **Web Configuration**  
`web/config/`

**Application Settings · Layer Metadata · Environment Variables**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../.github/workflows/ci.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Web Configuration (web/config/)"
version: "v1.5.0"
last_updated: "2025-10-14"
owners: ["@kfm-web", "@kfm-devops"]
tags: ["config","stac","vite","env","themes","metadata","mcp"]
license: "MIT"
semantic_alignment:
  - STAC 1.0
  - JSON Schema Validation
  - WCAG 2.1 AA (Theme Accessibility)
---
````

---

## 🧭 Overview

The `web/config/` directory defines the **metadata, settings, and environment configuration** that govern how the **Kansas Frontier Matrix (KFM)** frontend operates.
It provides centralized control over API endpoints, map and timeline layers, theme variables, and environment definitions.

Configurations connect the **STAC catalog**, **backend API**, and **React/MapLibre UI**, ensuring that every deployment of the web app is **reproducible**, **environment-driven**, and **data-traceable** under **MCP-DL v6.2** standards.

> **Philosophy:** In KFM, configuration is documentation — every parameter is transparent, validated, and version-controlled.

---

## 🧱 Directory Structure

```text
web/config/
├── app.config.json        # Global application configuration
├── layers.json            # Map + timeline layer definitions linked to STAC
├── themes.json            # Theme tokens and color palettes
├── env.example            # Environment variable template
├── vite.config.ts         # Vite build configuration for React + TypeScript
├── jest.config.js         # Jest unit testing configuration
└── README.md              # This documentation file
```

---

## 🧩 Core Configuration Files

### 🗂️ app.config.json

Defines top-level **application behavior**, including API endpoints, map defaults, and feature toggles.

```json
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
```

> Used during app bootstrap; ensures that feature flags and endpoints remain declarative and reproducible.

---

### 🧭 layers.json

Lists all **map and timeline layers**, referencing datasets from the **STAC catalog**.
Each entry includes metadata, visibility options, temporal extent, and licensing details.

```json
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
```

These definitions dynamically populate **LayerControls**, **MapView**, and **TimelineView**.
All JSON files are schema-validated during CI to prevent malformed data deployment.

---

### 🎨 themes.json

Defines **color palettes, typography, and accessibility tokens** for both light and dark modes.
These tokens sync with the design system to ensure visual consistency.

```json
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
```

> `ThemeContext` consumes this configuration to apply color modes across all React components.

---

### 🌎 env.example

Template for environment variables that define **API URLs**, **tokens**, and **feature toggles**.

```bash
VITE_API_BASE_URL=https://api.frontiermatrix.org
VITE_APP_NAME=Kansas Frontier Matrix
VITE_ENABLE_AI=true
VITE_ENABLE_ACCESSIBILITY=true
VITE_MAPBOX_TOKEN=your-maptiler-or-mapbox-token
```

Developers can copy this file to `.env` and customize for local, staging, or production environments.

---

### ⚡ vite.config.ts

Vite configuration for React and TypeScript.
Enables aliasing, asset optimization, and environment injection.

```ts
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
  server: { port: 3000, open: true }
});
```

> The Vite build pipeline ensures reproducible builds and optimized static output for KFM’s web interface.

---

### 🧪 jest.config.js

Configures Jest for **unit and integration testing** across web components.

```js
export default {
  testEnvironment: "jsdom",
  transform: { "^.+\\.(t|j)sx?$": "babel-jest" },
  moduleNameMapper: { "\\.(css|scss)$": "identity-obj-proxy" },
  setupFilesAfterEnv: ["<rootDir>/setupTests.ts"],
  collectCoverageFrom: ["web/src/**/*.{ts,tsx}"],
  coverageThreshold: {
    global: { lines: 90, branches: 80 }
  }
};
```

---

## 🧮 Validation Workflow (CI/CD)

KFM’s continuous integration system enforces reproducibility and schema compliance.

| Validation Step          | Description                                                                            | Tool                        |
| :----------------------- | :------------------------------------------------------------------------------------- | :-------------------------- |
| **Schema Validation**    | Ensures `app.config.json`, `layers.json`, and `themes.json` conform to defined schemas | Ajv / JSON Schema Validator |
| **STAC Integrity Check** | Confirms that all `layers.json` entries reference valid STAC IDs                       | STAC Validator              |
| **Env Consistency**      | Verifies required environment variables exist                                          | Node.js dotenv parser       |
| **Snapshot Testing**     | Confirms UI parity with configuration-driven output                                    | Jest Snapshot               |
| **Build Verification**   | Validates that `vite.config.ts` builds successfully under production mode              | Vite CLI                    |

---

## ♿ Accessibility Compliance

* Theme tokens validated for **color contrast ≥ 4.5:1**
* Text/background combinations tested for readability under both themes
* Font size and spacing tokens conform to design system accessibility standards
* Config-driven color and layout variables dynamically loaded for user preferences (`prefers-color-scheme`)

---

## 🧾 Provenance & Integrity

| Artifact         | Description                                                   |
| :--------------- | :------------------------------------------------------------ |
| **Inputs**       | STAC metadata, environment variables, design tokens           |
| **Outputs**      | Compiled config JSONs loaded by frontend                      |
| **Dependencies** | Node.js, Vite, TailwindCSS, TypeScript                        |
| **Integrity**    | Verified via CI (schema validation + reproducible hashes)     |
| **Traceability** | All configurations versioned and referenced by Git commit SHA |

---

## 🧠 MCP Compliance Checklist

| MCP Principle       | Implementation                                            |
| :------------------ | :-------------------------------------------------------- |
| Documentation-first | All config files include inline comments and README links |
| Provenance          | Each file is schema-validated and checksum-tracked        |
| Reproducibility     | Deterministic builds and version-controlled configs       |
| Accessibility       | Theme colors validated for WCAG 2.1 AA compliance         |
| Open Standards      | JSON, STAC 1.0, Env format                                |
| Auditability        | CI logs document each configuration validation stage      |

---

## 🔗 Related Documentation

* **Web UI Architecture** — `web/ARCHITECTURE.md`
* **MapView Component** — `web/src/components/MapView/README.md`
* **LayerControls Component** — `web/src/components/LayerControls/README.md`
* **Monorepo Repository Design** — `docs/monorepo/README.md`

---

## 📜 License

Released under the **MIT License**.
© 2025 Kansas Frontier Matrix — developed under **MCP-DL v6.2** for reproducible, environment-driven web architecture.

> *“Configuration is the silent framework — it lets the frontier’s data assemble itself.”*

```
```
