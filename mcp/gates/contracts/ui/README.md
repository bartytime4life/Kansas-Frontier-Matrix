# 🎛️ UI Contracts — MCP Gates

![Contracts](https://img.shields.io/badge/contracts-UI-blue)
![Gatekeeping](https://img.shields.io/badge/gates-fail--closed-critical)
![Policy](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-7b2cbf)
![Provenance](https://img.shields.io/badge/provenance-STAC%20%7C%20DCAT%20%7C%20PROV-success)
![API](https://img.shields.io/badge/API-REST%20%7C%20GraphQL-lightgrey)
![UI](https://img.shields.io/badge/UI-React%20%2B%20TypeScript-9cf)

> 🚦 **Contract registry for everything that crosses the UI boundary** (UI ↔ API ↔ AI).  
> If it can’t be **validated**, **provenance-linked**, and **policy-cleared**, it does **not** render. “Fail-closed” is the default posture.  
> This aligns with KFM’s **contract-first** + **evidence-first** architecture. [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:1‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

📍 **You are here:** `mcp/gates/contracts/ui/README.md`

---

## 🧭 What this folder is

This folder defines the **UI-facing contracts** used by “gates” (schema + policy) to validate:
- 📦 **API → UI** payloads (layers, features, timelines, story content, exports)
- 🖱️ **UI → API** requests (search, filtering, map context, story playback, AI queries)
- 🤖 **AI → UI** payloads (Focus Mode answers with citations + audit metadata)

KFM’s documentation repeatedly stresses **clear contracts between stages** and **deterministic pipelines**—this folder is where that becomes enforceable at the UI boundary. [oai_citation:2‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🔍 Why contracts (and why “gates”)?

The repo audit flagged a need for clearer modular boundaries and explicit interface specs (plugin/service-style integration needs “well-defined interfaces and clear module boundaries”). This directory is that missing “interface spec” for the UI boundary.  [oai_citation:3‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-TkRzAfTnxCYDUHauCf1NcH)

---

## 🗺️ KFM UI context (what these contracts must support)

KFM’s UI is designed around:
- 🗺️ **2D Map Viewer** (MapLibre GL JS / Leaflet) + 🧊 **3D Globe** (CesiumJS)
- 🕰️ **timeline/temporal navigation**
- 🧾 **layer inspection** (metadata, provenance, licensing)
- 🧠 **Focus Mode**: evidence-citing AI assistant that is contextual to map/time/layers
- 📖 **Story Nodes**: “machine-ingestible storytelling” stored as Markdown + optional JSON config
- ⚡ **Pulse Threads**: short, geotagged narrative updates tied to evidence
- 🤝 collaboration features (comments/annotations) planned/expanded over time

These are described as **React/TypeScript UI** decoupled via **REST + GraphQL** APIs, with provenance surfaced and AI answers shipped with citations. [oai_citation:4‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) [oai_citation:5‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 🧱 Non‑negotiables (Design Anchors) ✅

These are “hard rules” the UI contracts must encode and gates must enforce:

1) **Canonical pipeline order — no skipping**  
The pipeline ordering is treated as “absolute” (raw → processed → catalogs → graph → API → UI → story/focus). UI must not accept payloads that bypass catalogs/provenance or come from “mystery sources.” [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

2) **No direct graph access from UI**  
UI must not query Neo4j directly; it must go through API contracts so policy + provenance gates stay centralized. [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

3) **No “mystery layers”**  
Every dataset/layer requires a metadata contract (source, license, dates, processing steps). Missing metadata blocks loading/publishing; UI surfaces this via Layer Info dialogs and similar UX patterns. [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

4) **Evidence-first narratives**  
Any human-facing narrative content needs citations and must mark AI-generated text if present; missing evidence fails gates. [oai_citation:9‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

5) **Sovereignty / sensitivity propagates forward**  
Classifications must never be downgraded by transformation. If sensitive locations require generalization/blurring, the classification tags must propagate into UI contracts so the UI can apply safeguards at the right zoom/contexts. [oai_citation:10‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

6) **AI answers are traceable and policy-checked**  
Focus Mode must cite sources; if it can’t derive an answer from available data, it must refuse/express uncertainty. It runs governance checks before output is shown. [oai_citation:11‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) [oai_citation:12‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

7) **Fail-closed enforcement via Policy Pack**  
OPA + Conftest policies encode governance rules (license required, citations required, no secrets, etc.). CI blocks merges when policies fail; runtime policy checks can deny actions/outputs. [oai_citation:13‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) [oai_citation:14‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 🗂️ Recommended layout (inside `mcp/gates/contracts/ui/`) 📁

> This repo is contract-first; treat schemas as “boundary artifacts” and generate types/tests from them. [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

```text
📦 mcp/
  🚦 gates/
    📜 contracts/
      🖥️ ui/
        📄 README.md            👈 you are here
        🧾 schemas/             # JSON Schema (source of truth)
        🧬 types/               # generated TS types (optional)
        🧪 tests/               # contract tests (examples validate against schemas)
        🧷 examples/            # canonical payload examples (goldens)
        🧭 policies/            # UI-surface policies (if split from global policy pack)
```

---

## 🧩 Contract surfaces (what we define here)

| Surface 🧩 | Direction 🔁 | Why it needs a contract | Gate checks 🚦 |
|---|---:|---|---|
| Map Layers & Styles 🗺️ | API → UI | Prevent “mystery layers”; guarantee provenance & license UI can display | schema + license + provenance required [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) |
| Feature Inspection 🔍 | API → UI | Consistent “feature popup” payloads (attrs, links, provenance) | schema + sensitivity labels |
| Search & Filters 🔎 | UI → API | Stable query contract (bbox, time, layers, keywords) | schema + rate/role policy |
| Timeline / Temporal Nav 🕰️ | UI ↔ API | Slider/filter contract; time-bounded queries | schema + range validation |
| Focus Mode 🤖 | UI ↔ AI/API | Evidence-linked answers with governance check & audit metadata | schema + citations + OPA deny rules [oai_citation:17‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) |
| Story Nodes 📖 | API → UI / Repo → UI | Markdown + JSON config must remain machine-ingestible | schema + citations rules |
| Pulse Threads ⚡ | API → UI | Short, timely narratives tied to evidence | schema + evidence manifest |
| Exports / Share Links 🔗 | UI → API | Ensure exports carry attribution/provenance | schema + policy |
| Collaboration (comments/annotations) 🤝 | UI ↔ API | Moderation + audit + permissions | schema + role policy |

---

## 🧾 Shared contract conventions (must be consistent)

### ✅ Common top-level fields
Every UI contract should include these where applicable:

- `schema_version` — semantic version for the payload (e.g., `"ui.layer@1.0.0"`)
- `id` — stable identifier (UUID / slug / catalog ID)
- `created_at`, `updated_at` — ISO timestamps
- `provenance` — links into STAC/DCAT/PROV + run/evidence manifests
- `license` / `rights` — machine-readable license + human summary
- `classification` — sensitivity label(s) (public/restricted/etc.) + reason
- `citations[]` — structured citations (required for narratives & AI)
- `attribution[]` — credits to contributors/sources

KFM’s “no mystery layer” stance makes these fields **mandatory** for anything user-facing. [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 🧬 Provenance object (recommended shape)
Contracts should allow multiple provenance paths (catalog + graph + run ledger):

```json
{
  "provenance": {
    "stac": { "collection": "stac://collections/...", "item": "stac://items/..." },
    "dcat": { "dataset": "dcat://datasets/...", "distribution": "dcat://distributions/..." },
    "prov": { "bundle": "prov://bundles/...", "activity": "prov://activities/..." },
    "run_manifest": "audit://runs/<run_id>/run_manifest.json",
    "evidence_manifest": "evidence://<evidence_id>/manifest.yaml"
  }
}
```

This aligns with the system’s expectation that metadata/provenance standards are first-class and policy-enforced. [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🚦 Gates & enforcement model

### 1) Schema validation (fail fast)
- Validate request/response payloads at runtime (API edge) and in CI (golden examples).  
- Use JSON Schema as the “truth” and generate TypeScript and/or Pydantic types from it (as needed).

### 2) Policy-as-code (OPA + Conftest)
Policies enforce cross-cutting rules like:
- “Every dataset must have a license”
- “AI outputs must include at least one citation”
- “No secrets in committed files”
- “Sensitive outputs must retain restrictive classification”
- “Missing PROV or broken links fail the build”

This is explicitly described as a core governance mechanism used in CI and potentially at runtime. [oai_citation:21‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg) [oai_citation:22‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### 3) Run manifests + hashing (audit ledger)
Pipeline and content generation runs should emit structured **run manifests** and include canonical hashing to create stable identifiers for audit/provenance linking. [oai_citation:23‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧪 Minimal examples (copy/paste starters)

> These are **illustrative**: keep final field names aligned with the actual schemas you commit in `schemas/`.

### 🗺️ Example: LayerDescriptor (API → UI)

```json
{
  "schema_version": "ui.layer@1.0.0",
  "id": "layer:hydrology:streamflow_gauges",
  "title": "USGS Streamflow Gauges",
  "description": "Point layer of stream gauges with observed discharge.",
  "geometry_type": "Point",
  "time_range": { "start": "1930-01-01", "end": "2025-12-31" },
  "render": {
    "engine": "maplibre",
    "source": { "type": "geojson", "href": "https://api.kfm.local/layers/streamflow_gauges.geojson" }
  },
  "license": { "spdx": "CC-BY-4.0", "url": "https://creativecommons.org/licenses/by/4.0/" },
  "classification": { "level": "public", "reason": "Open government data" },
  "provenance": {
    "stac": { "collection": "stac://collections/hydrology", "item": "stac://items/usgs_gauges" },
    "prov": { "bundle": "prov://bundles/run_2026_01_22" },
    "run_manifest": "audit://runs/run_2026_01_22/run_manifest.json"
  },
  "attribution": [
    { "name": "USGS", "role": "source" },
    { "name": "Kansas Frontier Matrix", "role": "publisher" }
  ]
}
```

Real-time / sensor layers should also carry classification + provenance so the UI can label/blur appropriately. [oai_citation:24‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

### 🤖 Example: FocusModeRequest (UI → AI/API)

```json
{
  "schema_version": "ui.focus.request@1.0.0",
  "question": "What does this drought index layer show in Douglas County in the 1930s?",
  "context": {
    "bbox": [-95.5, 38.8, -94.6, 39.3],
    "time": { "start": "1930-01-01", "end": "1939-12-31" },
    "active_layer_ids": ["layer:climate:drought_index_1930s"],
    "selected_feature_ids": []
  }
}
```

Focus Mode is explicitly “context-aware” (location, timeframe, active layers). [oai_citation:25‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

### 🧠 Example: FocusModeResponse (AI/API → UI)

```json
{
  "schema_version": "ui.focus.response@1.0.0",
  "answer_markdown": "The drought index layer summarizes ... [1] ...",
  "citations": [
    {
      "id": "cite:1",
      "label": "[1]",
      "targets": [
        { "type": "stac_item", "ref": "stac://items/drought_index_1930s" }
      ]
    }
  ],
  "audit": {
    "policy_version": "policy-pack@2026.01",
    "governance": { "status": "allow", "flags": [] },
    "explainability": { "enabled": true, "top_factors": ["graph:Event->Place", "dataset:drought_index"] }
  },
  "disclaimer": "Advisory only. Verify against cited sources."
}
```

Focus Mode requires citations and runs a governance check before answers are returned. [oai_citation:26‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

### 📖 Example: Story Node (Markdown + JSON config)

Story Nodes are stored as Markdown with optional JSON config (map view, active layers, etc.). [oai_citation:27‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

```markdown
---
schema_version: "ui.story_node@1.0.0"
id: "story:1934_dust_bowl_douglas"
title: "Dust Bowl Impacts in Douglas County"
time:
  start: "1934-01-01"
  end: "1934-12-31"
layers:
  - "layer:climate:drought_index_1930s"
citations:
  - id: "cite:1"
    targets:
      - type: "stac_item"
        ref: "stac://items/drought_index_1930s"
---

Narrative text here with citations.
```

---

### ⚡ Example: Pulse Thread (short narrative post)

Pulse Threads are intended as short, timely narratives tied to evidence and governance workflows (human-in-loop for high stakes). [oai_citation:28‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

```json
{
  "schema_version": "ui.pulse_thread@1.0.0",
  "id": "pulse:2026-01-22:river_low_flow",
  "headline": "River X at record low flow this week",
  "geo": { "type": "Point", "coordinates": [-95.1, 39.0] },
  "confidence": 0.78,
  "severity": "medium",
  "citations": [
    { "id": "cite:1", "targets": [{ "type": "dataset", "ref": "layer:hydrology:streamflow_gauges" }] }
  ],
  "moderation": { "requires_human_approval": false }
}
```

---

## 🔁 Versioning & compatibility

- Use **SemVer** for schemas (breaking changes ⇒ major bump).
- Prefer **additive** changes (new optional fields) to keep UI/clients forward-compatible.
- Keep deprecations explicit (e.g., `deprecated: true`, `replaced_by` pointers).

Policy pack rules and contracts are versioned along with code, which supports auditability (“which rules were in effect?”). [oai_citation:29‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 🤝 Contribution workflow (contracts-first)

1) 🧾 Update/introduce a schema in `schemas/`
2) 🧷 Add/refresh canonical examples in `examples/`
3) 🧪 Add/refresh contract tests in `tests/`
4) 🚦 Ensure **OPA/Conftest** gates pass (license, provenance, classification, citations, secrets)
5) 📚 Update documentation (this README or the relevant subsystem docs)

Story content currently leans on Markdown/JSON templates with Git-based review (maintainers validate references and correctness). [oai_citation:30‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

---

## 🧭 Roadmap hooks (contracts you’ll likely add)

These are recurring future directions across the docs—design contracts with extension points:

- 📦 **Offline data packs** for mobile/field use (downloadable bundles, sync metadata) [oai_citation:31‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- 🕶️ **AR / immersive exploration** (3D + narrative overlays) [oai_citation:32‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe) [oai_citation:33‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- 🧪 **Simulation dashboards** + scenario playback (contract for scenario inputs/outputs) [oai_citation:34‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- 🧬 **DevOps → PROV mapping** (PR/commit activity becomes queryable provenance) [oai_citation:35‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 📚 Source docs used (project file index) 🧾

> These are the design anchors for this README/spec. (Each bullet links to the source file.)

- **KFM Technical Documentation** — contracts, standards, QA culture  
   [oai_citation:36‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

- **KFM Architecture, Features, and Design** — policy gates, governance, FAIR+CARE, security  
   [oai_citation:37‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)

- **KFM AI System Overview** — Focus Mode, RAG pipeline, governance checks, policy pack  
   [oai_citation:38‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

- **KFM UI System Overview** — UI capabilities, Story Nodes/Focus Mode surface, API boundaries  
   [oai_citation:39‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)

- **KFM Data Intake Guide** — ingestion gates, evidence rules, classification propagation  
   [oai_citation:40‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)

- **Latest Ideas & Future Proposals** — offline packs, AR, dashboards, provenance roadmap  
   [oai_citation:41‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

- **Innovative Concepts to Evolve KFM** — 4D digital twins, AR/VR, cultural protocols + CARE hooks  
   [oai_citation:42‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)

- **Additional Project Ideas** — run manifests, evidence manifests, pulse concepts, fail-closed governance  
   [oai_citation:43‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

- **Pulse Threads / Story Nodes / Evidence Manifest refinement doc** — narrative workflow emphasis  
   [oai_citation:44‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

- **Open-Source Geospatial Mapping Hub Design** — MapLibre/Cesium UI patterns (time slider, etc.)  
  

- **Design Audit** — gaps motivating contracts/interfaces  
  

- **Master Markdown Guide v13** — canonical pipeline ordering + governance expectations  
  

- **Scientific Method / Master Coder Protocol** — reproducibility mindset, SOPs, auditability culture  
   [oai_citation:45‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

<details>
<summary>📚 Project research libraries (PDF portfolios)</summary>

These are supporting reference libraries used by the project (multi-document PDF portfolios):

- AI Concepts & more —  [oai_citation:46‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- Data Management / Architectures / Bayesian / etc —  [oai_citation:47‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- Maps / Google Maps / Virtual Worlds / WebGL —  [oai_citation:48‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- Programming languages & resources —  [oai_citation:49‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)  

</details>

---

## ✅ “Definition of done” for UI contracts (quick checklist)

- [ ] Schema exists in `schemas/` (with version + description)
- [ ] Example payloads exist in `examples/` and validate
- [ ] Policy checks pass (license, provenance, classification, citations, secrets)
- [ ] UI rendering is deterministic for the same input payload
- [ ] Sensitive content pathways are tagged so UI can blur/generalize as required
- [ ] Docs updated (this README + feature docs)

🚀 When in doubt: **make the boundary explicit**, and let gates enforce it.
