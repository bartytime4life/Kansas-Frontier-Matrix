# 🎛️ UI Contract Schemas (`api/contracts/schemas/ui`)

![JSON Schema](https://img.shields.io/badge/JSON%20Schema-Draft%202020--12-informational)
![Contract First](https://img.shields.io/badge/Contracts-First-blue)
![Provenance First](https://img.shields.io/badge/Provenance-First-brightgreen)
![Accessibility](https://img.shields.io/badge/A11y-Required-orange)

**Purpose:** This folder defines the **machine-validated JSON Schemas** that govern Kansas Frontier Matrix (KFM) **frontend/UI-facing contract artifacts**—the things the UI loads, renders, logs, and audits (configs + event envelopes), without hard-coding “mystery behavior” into the client.

> 🧭 In KFM, the UI is intentionally *not* a private data logic layer.  
> The UI **renders what the API returns**, exposes **provenance**, and must never enable data leakage.

---

## 📌 What belongs here

Schemas in this directory are for **UI-consumed artifacts** that must remain stable across:
- 🖥️ the web client (React SPA)
- 🔌 the API surface that serves UI configuration
- ✅ CI validation & audit tooling (a11y, telemetry, governance checks)
- 🌐 future federation (multi-region “Frontier Matrix” hubs)

Typical schema families:
- 🗺️ **Layer Registry / Layer Catalog View** (what layers exist, how the UI should request them, display rules)
- ⏳ **Timeline / Temporal UI config** (supported time windows, playback constraints, defaults)
- 🎛️ **UI Settings / Feature Flags** (capabilities & toggles, including experimental features)
- 🧾 **Telemetry Event Envelope** (audit-friendly, privacy-aware interaction logging)
- ♿ **Accessibility Audit Reports** (structured outputs from UI audit tooling)
- 🧠 **Focus Mode UI State** (the UI state wrapper around evidence-backed Q&A, citations, and redaction notices)

---

## 🚫 What does *not* belong here

Keep these out of this directory:
- React components / TS source code (that lives in `web/`)
- CSS / map stylesheets (unless they are referenced by an explicit config contract)
- API endpoint definitions (those live in `api/contracts/openapi/`)
- Knowledge graph ontology schemas (those live in graph/ontology areas)

---

## 🧱 Folder layout & conventions

```text
📁 api/
  📁 contracts/
    📁 schemas/
      📁 ui/
        📄 README.md                👈 you are here
        📄 *.schema.json            ✅ JSON Schema definitions
        📁 examples/                🧪 example payloads validated by schemas
          📄 *.example.json
```

### ✅ File naming
- **Schemas:** `kebab-case.schema.json`
- **Examples:** `kebab-case.example.json` (place in `examples/`)

Examples:
- `layer-registry.schema.json`
- `ui-telemetry-event.schema.json`
- `timeline-config.schema.json`
- `a11y-audit-report.schema.json`

---

## 🧬 Schema design rules (KFM defaults)

These rules keep schemas **portable**, **type-safe**, and **audit-friendly**:

### 1) Pin the dialect
Use Draft 2020-12 unless there’s a reason not to:
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema"
}
```

### 2) Be strict by default
Prefer:
- `additionalProperties: false`
- explicit `required` lists
- enums for known modes / layer types

### 3) Stable identifiers > display names
UI contracts should carry **stable IDs** (for diffing, provenance links, federation) and keep display labels separate.

Recommended fields:
- `layerId` (stable, unique)
- `datasetId` (stable, versioned dataset identifier)
- `title` (human-friendly)
- `slug` (URL-safe, optional)

### 4) Prefer references to *sources of truth*
UI config should **reference** canonical entities rather than duplicate them:
- `datasetId` → catalog entry (STAC/DCAT/PROV)
- `provenanceRef` → provenance bundle / link
- `licenseRef` → license identifier / URL
- `attribution` → UI-renderable credit line

### 5) Federation-ready shapes
Avoid Kansas-only assumptions in core schema objects. Kansas specificity belongs in data/config instances, not schema structure.

---

## 🗺️ Layer Registry schema (recommended shape)

The **Layer Registry** is the UI’s “table of contents” for the map.

### Suggested top-level fields
- `schemaVersion` — the registry schema version
- `generatedAt` — ISO timestamp (helps QA + auditing)
- `layers[]` — list of layers with stable IDs + rendering rules

### Example: `layer-registry.example.json`
```json
{
  "schemaVersion": "1.0.0",
  "generatedAt": "2026-01-12T00:00:00Z",
  "layers": [
    {
      "layerId": "kfm.ks.boundaries.counties.v1",
      "datasetId": "kfm.ks.boundaries.counties.1850-2020.v1",
      "title": "Kansas Counties",
      "description": "County boundaries with temporal variants where available.",
      "layerType": "vector",
      "time": {
        "mode": "range",
        "start": "1850-01-01",
        "end": "2020-12-31"
      },
      "source": {
        "protocol": "tilejson",
        "url": "/api/v1/tiles/kfm.ks.boundaries.counties.1850-2020.v1"
      },
      "style": {
        "defaultVisibility": true,
        "opacity": 0.9
      },
      "governance": {
        "classification": "public",
        "redactionPolicy": "none"
      },
      "attribution": {
        "text": "KFM / Source: documented in dataset metadata",
        "license": "CC-BY-4.0"
      }
    }
  ]
}
```

> 🧩 Tip: Treat the Layer Registry as a **derived artifact** from catalogs + policy, not a hand-maintained list when possible.  
> Deterministic generation makes QA and provenance easier.

---

## ⏳ Timeline config schema (recommended scope)

Temporal navigation is a core UI capability. Timeline config schemas should describe:
- supported temporal resolution (`year`, `month`, `day`)
- default window / initial cursor
- playback constraints (min/max, step, looping)
- dataset-layer compatibility rules (optional)

Example `timeline-config.example.json`:
```json
{
  "schemaVersion": "1.0.0",
  "defaults": {
    "cursor": "1900-01-01",
    "window": {
      "mode": "range",
      "start": "1850-01-01",
      "end": "2020-12-31"
    }
  },
  "playback": {
    "enabled": true,
    "step": { "unit": "year", "value": 1 },
    "maxFps": 30
  }
}
```

---

## 🧾 Telemetry event schema (audit-friendly)

Telemetry in KFM is not “just analytics”—it supports:
- ✅ reproducibility (what was viewed/toggled)
- 🧑‍⚖️ governance auditing (redaction notice shown, restricted access flows)
- ♿ accessibility monitoring (UI regressions)
- 🔍 UX research (with privacy safeguards)

### Recommended event envelope fields
- `eventName` (enum or string pattern)
- `occurredAt` (ISO timestamp)
- `actor` (anonymous-safe shape; **no PII by default**)
- `uiContext` (route, view mode, session id)
- `subject` (datasetId / layerId / storyNodeId)
- `policy` (what policy decision applied, if any)

Example `ui-telemetry-event.example.json`:
```json
{
  "eventName": "focus_mode_redaction_notice_shown",
  "occurredAt": "2026-01-12T02:14:22Z",
  "actor": { "type": "anonymous", "sessionId": "s_9f4c1b" },
  "uiContext": { "route": "/focus", "view": "focus-mode" },
  "subject": { "datasetId": "kfm.ks.some_sensitive_dataset.1900-1950.v1" },
  "policy": {
    "decision": "redacted",
    "reason": "classification:restricted"
  }
}
```

---

## ♿ Accessibility (A11y) report schema

KFM treats accessibility as a first-class contract. An a11y schema should:
- store tool name + version (axe, lighthouse, etc.)
- store score + structured violations
- allow CI thresholds (“block merge if regression”)

Example `a11y-audit-report.example.json`:
```json
{
  "tool": { "name": "axe-core", "version": "4.x" },
  "runAt": "2026-01-12T00:00:00Z",
  "target": { "route": "/map", "viewport": "desktop" },
  "summary": { "violations": 0, "incomplete": 0, "passes": 42 },
  "violations": []
}
```

---

## 🔐 Security & “no data leakage” guardrails

UI schemas should help enforce:
- **classification awareness** (public/restricted/internal)
- **redaction policies** (geometry generalization, delayed release, withheld fields)
- **safe defaults** (don’t let UI toggle a control that implies “bypass”)
- **audit coverage** (telemetry events for policy outcomes)

> 🧯 Important: UI contracts may *describe* redaction behavior, but the **backend remains the enforcement authority**.

---

## 🔁 Versioning & compatibility

### What counts as a breaking change?
Breaking changes include:
- removing required fields
- changing a field type (e.g., string → object)
- changing semantics of an enum value
- renaming stable identifiers

### Recommended strategy
- Use **SemVer** in schema metadata (`schemaVersion`)
- If breaking: create a new major version and support both during migration
- Keep a short `CHANGELOG` section in this README (or adjacent `CHANGELOG.md`)

---

## ✅ Validation (local + CI)

### Local validation options
- **Node/AJV**
  ```bash
  npx ajv-cli validate \
    -s api/contracts/schemas/ui/layer-registry.schema.json \
    -d api/contracts/schemas/ui/examples/layer-registry.example.json
  ```

- **Python/jsonschema**
  ```bash
  python -m jsonschema \
    -i api/contracts/schemas/ui/examples/layer-registry.example.json \
    api/contracts/schemas/ui/layer-registry.schema.json
  ```

### CI expectations (recommended)
- every `*.example.json` must validate against its matching schema
- schema linting runs on PR
- UI telemetry schema changes require a short governance note

---

## 🧑‍💻 Adding a new UI schema (checklist)

When you add a schema here:

- [ ] Add `your-schema.schema.json`
- [ ] Add at least one example in `examples/`
- [ ] Add validation wiring (CI or scripts)
- [ ] Ensure strictness (`additionalProperties: false`) unless you *intend* an extension point
- [ ] Add a short entry to the **Schema Catalog** section below
- [ ] If this schema is served via REST: update `api/contracts/openapi/`

---

## 🗂️ Schema Catalog (fill in / keep updated)

> 🧩 Keep this list aligned with what actually exists in this folder.

| Schema file | Used by | What it governs |
|---|---|---|
| `layer-registry.schema.json` | UI + API | Map layer discovery, endpoints, visibility rules |
| `timeline-config.schema.json` | UI | Timeline defaults & playback constraints |
| `ui-telemetry-event.schema.json` | UI + API | Telemetry event envelope for audits/analytics |
| `a11y-audit-report.schema.json` | CI | Accessibility regression reporting |

---

## 🔗 Related contract folders

- 📜 **OpenAPI:** `api/contracts/openapi/`
- 🧾 **Catalog schemas:** (STAC / DCAT / PROV) typically live alongside catalog tooling/schemas
- 🧠 **Story/Focus schemas:** templates + context bundle definitions live in narrative/story contract areas

---

## 📚 Project reference shelf (why the schema style looks like this)

<details>
<summary><strong>📖 Internal KFM docs</strong></summary>

- 🌾 Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation (`.docx`)
- 🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals (`.docx`)
- 🧾 Audit of the Kansas Frontier Matrix (KFM) Repository (`.pdf`)
- 🧱 Master guide / contract invariants (v13)

</details>

<details>
<summary><strong>🗺️ Geospatial, cartography, remote sensing</strong></summary>

- 🧭 Making Maps: A Visual Guide to Map Design for GIS (`.pdf`)
- 🛰️ Cloud-Based Remote Sensing with Google Earth Engine (`.pdf`)
- 🧳 Mobile Mapping: Space, Cartography and the Digital (`.pdf`)
- 🗺️ Python Geospatial Analysis Cookbook (`.pdf`)

</details>

<details>
<summary><strong>🌐 Web UI, performance, visualization</strong></summary>

- 📱 Responsive Web Design with HTML5 and CSS3 (`.pdf`)
- 🧊 WebGL Programming Guide (`.pdf`)
- 🖼️ Compressed Image File Formats (JPEG/PNG/GIF/…) (`.pdf`)

</details>

<details>
<summary><strong>📈 Data science, modeling, uncertainty</strong></summary>

- 🚀 Scientific Modeling and Simulation (NASA-grade guide) (`.pdf`)
- 📊 Understanding Statistics & Experimental Design (`.pdf`)
- 📉 Regression Analysis with Python (`.pdf`) + slides
- 🎲 Think Bayes: Bayesian Statistics in Python (`.pdf`)
- 📊 Graphical Data Analysis with R (`.pdf`)

</details>

<details>
<summary><strong>🛡️ Security, governance, and ethics</strong></summary>

- 🔐 Ethical Hacking & Countermeasures: Secure Network Infrastructures (`.pdf`)
- 🧰 Gray Hat Python (`.pdf`)
- 🧑‍⚖️ AI law foundations (machine learning age) (`.pdf`)
- 🧠 Introduction to Digital Humanism (`.pdf`)

</details>

<details>
<summary><strong>🗄️ Data platforms & architecture</strong></summary>

- 🧱 PostgreSQL Notes for Professionals (`.pdf`)
- ⚙️ Scalable Data Management for Future Hardware (`.pdf`)
- 🌐 Data Spaces (`.pdf`)
- 🕸️ Spectral Geometry of Graphs (`.pdf`)
- 🧬 Principles of Biological Autonomy (`.pdf`) *(systems thinking inspiration)*

</details>

---

## 🏁 Bottom line

If it affects how the UI:
- discovers layers 🗺️
- navigates time ⏳
- logs and audits actions 🧾
- enforces redaction 🔐
- proves accessibility ♿

…it should have a **schema here** ✅
