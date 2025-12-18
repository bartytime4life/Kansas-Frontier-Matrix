---
title: "KFM Web — Cesium Config"
path: "web/cesium/config/README.md"
version: "v1.0.0"
last_updated: "2025-12-18"
status: "draft"
doc_kind: "README"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:cesium:config:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-config-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:config:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# KFM Web — Cesium Config

## 📘 Overview

### Purpose
This folder defines **configuration conventions** for KFM’s Cesium-powered web UI surface: how Cesium defaults are set, how environment/runtime values are loaded, and how configuration relates to the **layer registry** and **Focus Mode** expectations.

This doc is **UI-stage** guidance within the canonical pipeline:
ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.

### Scope
In-scope configuration topics:
- Cesium viewer defaults (camera, terrain/imagery provider selection, time controls)
- Layer registry integration (declarative, contract-governed layer enablement and gating)
- Build-time vs runtime configuration boundaries
- Safe handling of tokens/keys (no secrets committed)
- Validation expectations for config changes (schema checks + UI checks)

Out-of-scope:
- API contract changes (use `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`)
- Story Node content authoring (use `docs/templates/TEMPLATE__STORY_NODE_V3.md`)
- ETL/catalog/graph generation (see `docs/MASTER_GUIDE_v12.md`)

### Audience
- Web UI engineers working in `web/cesium/`
- Data/catalog engineers adding new layers that must surface safely in UI
- Governance reviewers auditing layer access / sensitivity behavior

### Key invariants (non-negotiable)
- **No direct graph/DB access from the frontend**: all data access flows through contract-governed APIs.
- **No unauthorized data leakage**: layer access is governed via a declarative registry and policy flags.
- **No secrets in repo**: tokens/keys must be injected via secure mechanisms (CI/CD, secrets manager).
- **Focus Mode requires provenance-linked content**: configuration must not enable unsourced narrative paths.

### Definitions (working)
- **Config**: the normalized, validated object used by Cesium UI initialization and layer loading.
- **Layer registry**: the declarative list of UI layers + their provenance references + gating rules.
- **Runtime config**: config values that may differ by environment without rebuilding the bundle (pattern varies; not confirmed in repo).
- **Build-time config**: config embedded at build/bundle time (pattern varies; not confirmed in repo).

### Key governed artifacts (related)
- Master pipeline + invariants: `docs/MASTER_GUIDE_v12.md`
- Web architecture: `web/ARCHITECTURE.md`
- Cesium module overview: `web/cesium/README.md`
- Cesium components overview: `web/cesium/components/README.md`
- Layer registry (expected contract artifact): `web/cesium/layers/regions.json`

### Definition of done (for config changes)
- [ ] Config change is **documented here** (or in the owning module README, if more specific)
- [ ] Config is **typed** (TS types or schema) and **validated** (schema or runtime checks)
- [ ] Any new layer exposure goes through the **layer registry** (no ad-hoc hardcoded layers)
- [ ] CI passes: lint/tests + UI schema checks + security/sovereignty checks (as applicable)
- [ ] No secrets/tokens are committed; local dev uses safe, documented injection

---

## 🗂️ Directory Layout

### This folder (expected)
> Note: exact filenames may differ — **not confirmed in repo**. Treat this as the *intended* layout pattern for `web/cesium/config/`.

~~~text
📁 web/
└── 📁 cesium/
    ├── 📁 config/
    │   ├── 📄 README.md
    │   ├── 📄 (types + defaults + loaders)  ← not confirmed in repo
    │   └── 📄 (schema/validation helpers)   ← not confirmed in repo
    └── 📁 layers/
        └── 📄 regions.json  ← declarative layer registry (contract-governed)
~~~

### Related paths (common touchpoints)
- `web/cesium/layers/regions.json` — declarative layers + provenance refs + gating rules
- `web/cesium/components/` — components should consume *normalized config* only (no env parsing)
- `docs/` — governance, design docs, and validation standards

---

## 🧭 Context

### Why configuration is governed here
KFM’s frontend is a **governed presentation layer**: it must be able to safely render many datasets and derived evidence products without allowing:
- accidental exposure of restricted layers,
- hardcoded special cases that bypass review,
- unsourced narrative in Focus Mode contexts.

Configuration is therefore treated as a **contract surface** between:
- catalog/metadata products (STAC/DCAT/PROV),
- API responses (contract-governed),
- UI rendering behavior (layer registry + config defaults).

### What is “not confirmed in repo”
Because this README is being generated from governed documentation patterns (not the live filesystem), the following are **not confirmed in repo** until verified in `web/`:
- exact build tool (Vite/Next/CRA/etc.) and therefore the env var prefix rules,
- whether runtime config is loaded from a `config.json`, injected global, or build-time only,
- the exact module filenames under `web/cesium/config/`.

---

## 🗺️ Diagrams

### Config flow: source → validation → normalized config → Cesium initialization
~~~mermaid
flowchart LR
  A["(1) Sources<br/>- defaults<br/>- env vars (build-time)<br/>- runtime config (optional)"] --> B["(2) Load + parse"]
  B --> C["(3) Validate<br/>- type guards / schema<br/>- required fields<br/>- safe defaults"]
  C --> D["(4) Normalized Config Object"]
  D --> E["(5) Cesium Viewer Init"]
  D --> F["(6) Layer Registry Resolver<br/>web/cesium/layers/regions.json"]
  F --> G["(7) Layer Loader(s)"]
  E --> G
  G --> H["Map UI + Focus Mode UX"]
~~~

---

## 🧾 Data & Metadata

### Inputs
- **Layer registry entries** (expected): `web/cesium/layers/regions.json`
  - should include provenance references (e.g., STAC collection IDs) and gating flags
- **Environment/runtime values** (pattern not confirmed in repo), commonly including:
  - API base URL / gateway base URL
  - Cesium Ion access token (if used)
  - Basemap/imagery provider tokens (if used)
  - Feature flags (enable/disable experimental layers)

### Outputs
- A **single normalized config object** that:
  - is safe to log at info-level (redacted where needed),
  - is safe to expose in client bundle (no private secrets),
  - is the only config interface consumed by Cesium components.

### Provenance expectation (UI-facing)
Even though UI config is not itself a catalog artifact, it must *support* provenance:
- Layer config should be able to link rendered features back to **dataset IDs** / **STAC IDs**.
- Focus Mode UI must be able to display citations and governance flags when configured to do so.

---

## 🔌 Interfaces & Contracts

### Layer Registry is a UI contract
The Cesium UI must not introduce new visible layers by hardcoding.
Instead, layers are declared in the layer registry (expected: `web/cesium/layers/regions.json`), which should support:
- `visibility.default_enabled` (default on/off)
- `zoom ranges` or other constraints
- `sensitivity_class` / CARE-related gating
- provenance pointers (e.g., `provenance.stac_id`)

> If you need to add a new layer: update the layer registry + ensure the renderer supports the layer type.

### API boundaries
Frontend config may store:
- API base URL(s)
- endpoint paths (if stable)

Frontend config must not:
- encode DB connection details,
- encode internal network endpoints,
- bypass API contracts.

---

## 🧱 Architecture

### Recommended separation of concerns
Even if filenames differ, the config responsibilities should be separated:

1) **Defaults (versioned)**
- stable, reviewable defaults committed to the repo
- includes safe Cesium defaults, safe feature flags, and conservative layer enablement

2) **Loading**
- reads env/runtime sources (pattern not confirmed in repo)
- normalizes types (string → number/boolean where applicable)
- redacts sensitive values in logs

3) **Validation**
- schema or type-guard validation
- fail-fast on missing required fields *only when needed*
  - example: require token only if a provider is enabled

4) **Consumption**
- Cesium components consume the normalized config only
- components do not read env vars or `window` globals directly

### Example config shape (illustrative — not confirmed in repo)
~~~json
{
  "api": { "baseUrl": "TBD" },
  "cesium": {
    "ionToken": "TBD (do not commit)",
    "defaultView": { "center": [-98.0, 38.0], "zoom": 6 }
  },
  "layers": {
    "registryPath": "web/cesium/layers/regions.json",
    "defaultRegion": "TBD"
  },
  "featureFlags": {
    "enable3D": true,
    "enableFocusMode": true
  }
}
~~~

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Config must support Focus Mode’s non-negotiable behaviors:
- enforce provenance-linked content display,
- surface governance flags (including sensitivity-related blurring/generalization),
- control default layers/time bounds when entering Focus Mode (if the UI implements these features).

### Provenance-linked narrative rule
- Every claim shown in Focus Mode must trace to a dataset / record / asset ID.
- Config must not introduce “free text narrative defaults” without a provenance model.

### Optional structured controls
> These are *controls the UI may support* — actual support is **not confirmed in repo**.

~~~yaml
focus_layers:
  - "TBD-layer-id-from-registry"
focus_time: "TBD-iso8601-or-range"
focus_center: [ -98.0000, 38.0000 ]
~~~

---

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] UI schema checks (layer registry)
- [ ] Config schema/type validation (if implemented)
- [ ] Security and sovereignty checks (as applicable)
- [ ] No-secrets scan (ensure tokens/keys are not committed)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) UI lint + typecheck
# <pkg-manager> run lint
# <pkg-manager> run typecheck

# 2) validate layer registry schema (if a checker exists)
# <pkg-manager> run validate:layers

# 3) validate docs markdown protocol (if a checker exists)
# <pkg-manager> run lint:docs
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Config validation failures | Web UI | `docs/telemetry/` + `schemas/telemetry/` |
| Layer gating events (blocked/blurred) | Web UI | `docs/telemetry/` + `schemas/telemetry/` |

---

## ⚖ FAIR+CARE & Governance

### Review gates
Config changes that affect:
- **layer visibility defaults**,
- **sensitivity gating**,
- **provenance display rules**,
- **Focus Mode behavior**,

…should be reviewed by:
- Web UI maintainers, and
- governance reviewers when data sensitivity/sovereignty is impacted.

### CARE / sovereignty considerations
- If a layer or feature can expose precise site locations for protected or culturally sensitive resources, config must:
  - default to **off** (where appropriate),
  - enforce **generalization/blur** behaviors,
  - surface a **governance notice** in UI (audit panel pattern).

### Secrets & security constraints
- Do not commit tokens/keys in defaults or in the layer registry.
- Prefer CI/CD secrets injection and local `.env` patterns (implementation depends on build tooling; not confirmed in repo).

### AI usage constraints
- Ensure the doc’s AI permissions/prohibitions match intended use.
- Do not infer or embed sensitive locations or restricted site coordinates in configuration.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial README for Cesium config conventions | TBD |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Web: `web/ARCHITECTURE.md`
- Cesium: `web/cesium/README.md`
- Cesium Components: `web/cesium/components/README.md`
- Layer Registry (expected): `web/cesium/layers/regions.json`