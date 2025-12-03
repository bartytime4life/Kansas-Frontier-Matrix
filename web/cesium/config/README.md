---
title: "⚙️ KFM v11.2.3 — Cesium Web Config Contracts (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed configuration layer for CesiumJS within the Kansas Frontier Matrix web stack, including environment, providers, and feature flags."
path: "web/cesium/config/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web Visualization Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Cesium 1.120 → 1.136 config-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"
doc_uuid: "urn:kfm:doc:web-cesium-config-v11-2-3"
semantic_document_id: "kfm-web-cesium-config-v11.2.3"
event_source_id: "ledger:kfm:web:cesium:config:v11.2.3"

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/web-cesium-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-cesium-release-v1.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"
status: "Active / Enforced"
doc_kind: "Subsystem Config Overview"
intent: "web-cesium-config"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# ⚙️ **Kansas Frontier Matrix — Cesium Web Config Contracts**  
`web/cesium/config/README.md`

**Purpose:**  
Define the **governed configuration layer** for CesiumJS in the KFM web stack, including environment configuration, provider registries, feature flags, and governance rules for 3D visualization.

</div>

---

## 📘 1. Overview

The files under `web/cesium/config/` control:

- **How Cesium is wired** into KFM environments (dev, staging, prod).  
- **Which providers** (imagery, terrain, 3D Tiles) are allowed.  
- **Which features** (async picking, debug layers, experimental tilesets) are enabled.  

This directory:

- **Does not** contain secrets.  
- Acts as the **source of truth** for Cesium-related configuration used by React/TS components under `web/cesium/components/`.  
- Is fully **CI-validated** and **FAIR+CARE-governed**.

For the higher-level Cesium subsystem overview, see:

- `web/cesium/README.md`

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
web/cesium/config/
│
├── 📄 README.md                     # This file — Cesium web config overview & contracts
│
├── ⚙️ cesium-env.example.json       # Example env configuration (non-secret) + required keys
├── 🗺️ cesium-providers.json         # Registry of allowed imagery/terrain/3D Tiles providers
└── 🎛️ cesium-feature-flags.json    # Feature toggles for Cesium integration (per environment/profile)
~~~

**Directory contract:**

- Only **non-secret, declarative JSON** belongs here.  
- Real secrets (tokens, API keys) live in **environment variables or secret stores**, not committed JSON.  
- Each JSON file is governed by a **JSON schema** and validated in CI.

---

## 🌎 3. `cesium-env.example.json` — Environment Contract

This file documents the **required / optional environment keys** for Cesium integration.

Typical fields (illustrative):

~~~json
{
  "CESIUM_BASE_URL": "/static/cesium",
  "CESIUM_TERRAIN_PROVIDER_ID": "terrain-kfm-primary",
  "CESIUM_DEFAULT_IMAGERY_PROVIDER_ID": "imagery-kfm-satellite",
  "CESIUM_3D_TILES_BASE_URL": "https://example.com/tilesets/",
  "CESIUM_ENABLE_DEBUG_LAYERS": false
}
~~~

**Rules:**

- `cesium-env.example.json` **must not** contain real tokens or credentials.  
- For each key, the React build or server-side layer should pull the **actual value** from:
  - `.env` files (for local dev only, git-ignored)  
  - Kubernetes/secret manager (for staging/prod)  

**Key responsibilities:**

- `CESIUM_BASE_URL`  
  - Where Cesium static assets (if any) are served from.  

- `CESIUM_TERRAIN_PROVIDER_ID` / `CESIUM_DEFAULT_IMAGERY_PROVIDER_ID`  
  - Must match provider IDs in `cesium-providers.json`.  

- `CESIUM_3D_TILES_BASE_URL`  
  - Root for KFM-served 3D Tilesets (if used in a templated fashion).  

- `CESIUM_ENABLE_DEBUG_LAYERS`  
  - Driver for dev-only debug overlays (wireframes, tile bounding boxes, etc.).

---

## 🗺️ 4. `cesium-providers.json` — Provider Registry

This file is the **only allowed source** of Cesium providers (imagery, terrain, 3D Tiles) in KFM.

Illustrative structure:

~~~json
{
  "providers": [
    {
      "id": "terrain-kfm-primary",
      "type": "terrain",
      "url": "https://example.com/terrain/",
      "attribution": "KFM Terrain",
      "license": "CC-BY 4.0",
      "care": {
        "sensitivity": "generalized",
        "notes": "Global DEM, no sensitive overlays."
      }
    },
    {
      "id": "imagery-kfm-satellite",
      "type": "imagery",
      "url": "https://example.com/imagery/",
      "attribution": "Satellite Provider X",
      "license": "Vendor Terms",
      "care": {
        "sensitivity": "generalized",
        "notes": "Used for context; no site-level overlays baked in."
      }
    },
    {
      "id": "tileset-kfm-heritage",
      "type": "3d-tiles",
      "url": "https://example.com/tilesets/heritage/",
      "attribution": "KFM Heritage",
      "license": "Custom",
      "care": {
        "sensitivity": "restricted-generalized",
        "notes": "Heritage-sensitive tileset. Visibility rules enforced elsewhere."
      }
    }
  ]
}
~~~

**Contract:**

- Every provider **must** have:
  - `id` (unique string)  
  - `type` (`"terrain"`, `"imagery"`, `"3d-tiles"`, `"vector"`, etc.)  
  - `url` (base URL or endpoint)  
  - `attribution` & `license` fields  

- For **sensitive providers** (e.g., heritage-related tilesets):
  - A `care` block is **required** with:
    - `sensitivity` (e.g., `"generalized"`, `"restricted-generalized"`)  
    - `notes` describing constraints or masking rules  

**Usage:**

- React/TS components look up providers **only** via this registry.  
- Env variables (e.g., `CESIUM_TERRAIN_PROVIDER_ID`) must reference IDs defined here.  
- Modernization (changing URLs, providers) happens **once here**, not scattered in components.

---

## 🎛️ 5. `cesium-feature-flags.json` — Feature Toggles

This file governs which Cesium features are active for a given profile (e.g., `dev`, `staging`, `prod`).

Illustrative structure:

~~~json
{
  "profiles": {
    "dev": {
      "enableAsyncPick": true,
      "enableDebugLayers": true,
      "enableExperimentalTilesets": true
    },
    "staging": {
      "enableAsyncPick": true,
      "enableDebugLayers": false,
      "enableExperimentalTilesets": false
    },
    "prod": {
      "enableAsyncPick": true,
      "enableDebugLayers": false,
      "enableExperimentalTilesets": false
    }
  }
}
~~~

**Key flags (examples):**

- `enableAsyncPick`  
  - If false, components must fall back to `scene.pick(...)` (legacy path).  
  - KFM default should be **true** for v1.136+.  

- `enableDebugLayers`  
  - Enables debug overlays (bounding volumes, tile metadata).  
  - **Must be false** in production deployments.  

- `enableExperimentalTilesets`  
  - Controls access to non-governed or experimental 3D Tilesets.  
  - Typically **dev-only** or restricted to internal environments.

**Profile selection:**

- Determined by environment (e.g., `KFM_ENV=dev|staging|prod`).  
- Components read `cesium-feature-flags.json` and `KFM_ENV` to decide which profile to apply.

---

## 🛡️ 6. Governance, Secrets & CARE

**Secrets handling:**

- **No real API keys** or sensitive URLs may appear in this directory.  
- Secret-bearing values must be injected via:
  - `.env` files (local only, git-ignored).  
  - Secret stores (Kubernetes, cloud secret manager) in higher environments.

**FAIR+CARE considerations:**

- Provider definitions must include CARE context where relevant.  
- Config must not bypass:
  - Region masking rules  
  - Provider-level CARE constraints  
  - Sovereignty restrictions on certain tilesets or imagery  

**Sovereignty & visibility:**

- Some providers may be:
  - **Internal-only** (not exposed to public users).  
  - Restricted to **aggregate views** (no detailed geometry).  
- Such restrictions must be documented:
  - In `cesium-providers.json` (via `care` block).  
  - In dataset/provenance metadata elsewhere in the repo.

---

## 🧪 7. CI Validation Expectations

Configuration files under `web/cesium/config/` are validated in CI:

- **Schema validation** (JSON schemas in a central `schemas/` directory):
  - `cesium-env.example.json` — shape & required keys.  
  - `cesium-providers.json` — provider entries, CARE blocks, types.  
  - `cesium-feature-flags.json` — profiles and flag naming.  

- **Cross-link validation**:
  - Provider IDs referenced by env variables or layer registries must exist.  
  - No provider in `cesium-providers.json` may be referenced if its license/CARE metadata is missing.  

- **Governance checks**:
  - `enableDebugLayers` must be false for production profile.  
  - Experimental flags must not be enabled for `prod` by default.

If any checks fail, CI **blocks** merges until configuration is corrected.

---

## 🧭 8. Authoring & Maintenance Workflow

When updating Cesium configuration:

1. **Plan the change**
   - Identify if it is:
     - New provider  
     - New feature flag  
     - Env variable contract change  

2. **Edit JSON in this directory**
   - Update `cesium-providers.json`, `cesium-feature-flags.json`, or `cesium-env.example.json` as appropriate.  
   - Maintain **backward-compatible** values when possible.

3. **Update related documentation**
   - If behavior changes, adjust:
     - `web/cesium/README.md`  
     - Any affected release notes under `web/cesium/releases/`.

4. **Run local validation**
   - Use repo tooling (e.g., `make validate-web-cesium-config`) to run schema and cross-link checks.

5. **Submit PR & undergo governance review**
   - FAIR+CARE + Web Visualization Systems review the change.  
   - Special care for:
     - New providers  
     - New feature flags impacting user-facing behavior  
     - Anything that could touch sovereignty or sensitive overlays.

---

## 🕰️ 9. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Web Visualization Systems WG · FAIR+CARE Council | Initial governed Cesium web config overview; defined env, providers, feature flags, and CI/governance rules for KFM v11.2.3. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT (Cesium Config & Docs)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cesium Web Integration Overview](../README.md) · [⬅ Back to Web Root](../../README.md)

</div>
