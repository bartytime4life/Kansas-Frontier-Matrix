# 🧭 Story Nodes — UI Narratives for the Experiment Report Template

📍 **Path:** `mcp/dev_prov/examples/10_experiment_report_template/(example_report_tree)/ui/story_nodes/`

> Story Nodes turn an experiment report into a **guided, evidence-backed “tour”** where narrative text stays synchronized with **map + timeline state (2D/3D)**, and every claim can be traced to provenance (“the map behind the map”).[^kfm-ui][^kfm-tech][^kfm-ai]

---

## 🧭 Quick Nav
- [What is a Story Node?](#-what-is-a-story-node)
- [Folder layout](#-folder-layout)
- [Story package contract](#-story-package-contract)
- [Markdown authoring rules](#-markdown-authoring-rules)
- [JSON config choreography](#-json-config-choreography)
- [Provenance & dev_prov requirements](#-provenance--dev_prov-requirements)
- [Experiment report integration](#-experiment-report-integration)
- [QA checklist](#-qa-checklist)
- [Future extensions](#-future-extensions)
- [Reference library](#-reference-library)

---

## 🧩 What is a Story Node?

In the KFM design, **Story Nodes are the building blocks of interactive stories/tours**: narrative content + a specified map state. Practically, stories are authored as **Markdown + JSON** so non-developers can contribute guided tours without writing app code.[^kfm-arch][^kfm-ui]

### ✨ Key idea
A **Story Package** = a folder that contains:
- 📝 **Narrative** (`story.md`)  
- 🎛️ **Choreography** (`story.json`) → which layers/camera/timeline to show at each step  
- 🧾 **Evidence manifest** (`evidence.manifest.yaml`) → machine-readable provenance for auditing & trust  
- 🖼️ **Assets** (`assets/`) → images/media used by the narrative  

When the UI enters “story mode”, it typically presents a **split view** (story panel + interactive map) with **Next/Prev controls**, optional progress indicators, and smooth transitions where each step updates the map/timeline automatically.[^kfm-tech][^kfm-ui]

---

## 🗂 Folder layout

> [!NOTE]
> The KFM repo often stores story content under paths like `web/story_nodes/` or `content/stories/`.[^kfm-ui]  
> In **this experiment report template**, story content lives here under `ui/story_nodes/` to keep the “report UI” self-contained.

Example structure (recommended):

```text
📁 ui/story_nodes/
├─ 📄 README.md
├─ 📁 stories/
│  ├─ 📁 exp-010_railroads/
│  │  ├─ 📝 story.md
│  │  ├─ 🎛️ story.json
│  │  ├─ 🧾 evidence.manifest.yaml
│  │  └─ 🖼️ assets/
│  │     ├─ 🖼️ thumbnail.jpg
│  │     └─ 🖼️ figure_01_map_overlay.png
│  └─ 📁 exp-011_drought_signals/
│     ├─ 📝 story.md
│     ├─ 🎛️ story.json
│     ├─ 🧾 evidence.manifest.yaml
│     └─ 🖼️ assets/
└─ 📁 _shared/
   └─ 🖼️ assets/
      └─ 🧷 kfm_logo_mark.png
```

---

## 📦 Story package contract

| 🧩 Component | 📄 File | ✅ Required | Why it exists |
|---|---|---:|---|
| Narrative | `story.md` | ✅ | Human-readable story text (with citations & entity refs) |
| Choreography | `story.json` | ✅ | Machine-readable “steps” that drive map + timeline changes |
| Evidence Manifest | `evidence.manifest.yaml` | ⭐ Recommended | Provenance-first auditing, CI validation, reuse, traceability |
| Assets | `assets/*` | Optional | Local images/media (best for offline packs & reproducibility) |
| Run Manifest | `run.manifest.json` | Optional | Links story to pipeline runs / experiment executions (dev_prov) |

---

## 🧠 How the UI consumes a story package

```mermaid
flowchart LR
  MD[📝 story.md] --> RENDER[🧼 Markdown renderer<br/>sanitized]
  JSON[🎛️ story.json] --> CTRL[🎚️ Story Controller<br/>steps/state]
  CTRL --> MAP[🗺️ MapLibre (2D)<br/>or Cesium (3D)]
  CTRL --> TIME[⏳ Timeline / Temporal nav]
  EVID[🧾 evidence.manifest.yaml] --> AUDIT[🔎 Provenance/Audit panel]
  RENDER --> UI[🪟 Story Panel]
  MAP --> UI
  TIME --> UI
  AUDIT --> UI
```

This mirrors the KFM approach where the front-end reads Markdown + JSON, renders Markdown safely, and applies step state via MapLibre/Cesium APIs.[^kfm-tech][^kfm-arch]

---

## ✍️ Markdown authoring rules

KFM treats Story Nodes as **machine-ingestible storytelling**:
- **Every claim should be traceable to evidence**
- **Entities should link to stable knowledge-graph IDs**
- **Fact vs interpretation should be clearly separated**[^md-guide]

### 1) Frontmatter (recommended)
Use YAML frontmatter so the UI (and indexing tools) can list and search stories consistently:

```yaml
---
id: exp-010_railroads
title: "Railroads reshape settlement patterns"
summary: "A guided tour showing how rail expansion correlates with settlement changes over time."
authors:
  - name: "Your Name"
    role: "Author"
created: "2026-01-22"
updated: "2026-01-22"

tags: ["experiment", "time-series", "transport"]
thumbnail: "./assets/thumbnail.jpg"

# Governance
sensitivity: "public"   # public | restricted | sensitive
license: "CC-BY-4.0"

# Integration hooks
related:
  experiments: ["exp-010"]
  datasets: ["dcat:example:railroads_ks_1860_1900"]
  graph_entities:
    - "kfm:place:flint_hills"
    - "kfm:concept:infrastructure"
---
```

> [!TIP]
> Keep `id` stable and slug-like (`exp-###_topic`). This makes stories easy to reference in provenance graphs and dev_prov logs.[^kfm-additional]

### 2) Step anchors (recommended)
If `story.json` references step anchors, add headings like:

```md
## Step 1 — Baseline (1860) {#step-1}
## Step 2 — Expansion (1870) {#step-2}
```

*(If your Markdown renderer doesn’t support `{#id}`, just use consistent headings and map to them via `markdownAnchor` strings.)*

### 3) Citations are non-negotiable 🔍
KFM’s UX emphasizes that everything is auditable; Focus Mode similarly **must refuse or show uncertainty** if it cannot cite sources.[^kfm-ai][^kfm-intake]

Recommended patterns:
- Footnotes: `... statement ...[^src-1]`
- Or bracketed references: `... statement ... [1]` (then define [1] at the end)

Example:

```md
Kansas saw significant rail growth between 1860 and 1880, reshaping trade corridors and settlement clustering.[^rail-dataset]

[^rail-dataset]: DCAT dataset `dcat:example:railroads_ks_1860_1900` (see `evidence.manifest.yaml`).
```

### 4) Fact vs Interpretation (make it explicit)
KFM guidance stresses separating direct facts from inference/hypothesis, especially with AI assistance.[^md-guide]

Use callouts:

> [!NOTE]
> **Fact (from dataset):** Rail segments increase in the NE corridor between 1870–1880.[^rail-dataset]

> [!IMPORTANT]
> **Interpretation:** This correlates with population growth clusters, but causality requires additional controls (migration policy, land grants, etc.).[^pop-dataset]

### 5) Accessibility & safety
- ✅ Always add **alt text** for images
- ✅ Caption charts/maps (what + when + source)
- ✅ Avoid raw HTML/JS embeds (story Markdown is typically sanitized in-app)[^kfm-ui]

---

## 🎛️ JSON config choreography

KFM’s design uses JSON to define **steps** such as: “zoom here”, “turn these layers on”, “set timeline to 1935”, and the UI applies them via MapLibre/Cesium calls.[^kfm-tech][^kfm-ui]

### Minimal example (`story.json`)
```json
{
  "storyId": "exp-010_railroads",
  "title": "Railroads reshape settlement patterns",
  "mapEngine": "maplibre",
  "steps": [
    {
      "id": "step-1",
      "title": "Baseline (1860)",
      "markdownAnchor": "Step 1",
      "timeline": { "year": 1860 },
      "camera": {
        "center": [-98.0, 38.5],
        "zoom": 5.2,
        "bearing": 0,
        "pitch": 0
      },
      "layers": [
        { "id": "kfm:layer:counties_1860", "visible": true },
        { "id": "kfm:layer:railroads_1860", "visible": false }
      ],
      "transition": { "durationMs": 900, "easing": "easeInOut" }
    },
    {
      "id": "step-2",
      "title": "Expansion (1870)",
      "markdownAnchor": "Step 2",
      "timeline": { "year": 1870 },
      "layers": [
        { "id": "kfm:layer:railroads_1870", "visible": true }
      ],
      "highlight": {
        "type": "bbox",
        "bbox": [-96.0, 37.8, -94.5, 39.2],
        "label": "NE corridor growth zone"
      }
    }
  ]
}
```

### Field reference (pragmatic)
| Field | Meaning | Notes |
|---|---|---|
| `storyId` | Stable ID for story package | Match Markdown frontmatter `id` |
| `mapEngine` | `maplibre` (2D) or `cesium` (3D) | KFM uses MapLibre + Cesium in the UI stack.[^kfm-arch] |
| `steps[]` | Ordered list of story steps | Drives Next/Prev, progress dots, scroll-driven, etc.[^kfm-ui] |
| `timeline` | Year/range/state | Syncs with temporal navigation |
| `camera` / `camera3d` | View state | 2D: center/zoom; 3D: Cesium destination/orientation |
| `layers[]` | Which layers are active | IDs should map to your data catalog entries |
| `highlight` | Optional emphasis | bbox/feature highlight to draw attention |
| `transition` | Optional animation style | Smooth transitions improve immersion[^kfm-ui] |

> [!WARNING]
> **Layer IDs must be real.** Maintainers review JSON references to ensure layer IDs map to catalog IDs and that story claims have citations.[^kfm-ui]

---

## 🧾 Provenance & dev_prov requirements

KFM’s “provenance-first” approach applies to:
- Datasets and map layers (STAC/DCAT metadata)
- AI answers and derived artifacts
- Stories and narratives (Story Nodes, Pulse Threads)[^kfm-intake][^kfm-additional]

### 1) Evidence manifest (`evidence.manifest.yaml`) ⭐
This makes stories auditable and queryable (e.g., “which stories used this dataset?”). It also enables CI checks: every citation in the narrative should resolve to a manifest entry.[^kfm-additional]

Example:

```yaml
storyId: exp-010_railroads
version: 1

agents:
  - id: agent:human:your_name
    role: author
  - id: agent:ai:focus_mode_v1
    role: ai_assist
    notes: "Only used for drafting; human reviewed."

sources:
  - id: src:railroads_dcat
    type: dcatDataset
    ref: "dcat:example:railroads_ks_1860_1900"
    license: "CC-BY-4.0"
    sensitivity: public

  - id: src:pop_dcat
    type: dcatDataset
    ref: "dcat:example:population_by_county_1860_1900"
    license: "Public Domain"
    sensitivity: public

artifacts:
  - id: art:thumbnail
    type: image
    path: "assets/thumbnail.jpg"
    sha256: "<fill-me>"

claims:
  - id: claim:rail_growth_ne
    text: "Rail segments increase in the NE corridor between 1870–1880."
    supportedBy: ["src:railroads_dcat"]
```

### 2) PROV hooks (conceptual)
KFM explicitly calls out provenance links like:
- `prov:wasDerivedFrom` → datasets/documents used
- `prov:wasAssociatedWith` → authors/agents (including AI if AI-drafted)[^kfm-additional]

Even if your template doesn’t serialize full PROV-O triples yet, your manifest should be written so it can be upgraded later.

### 3) Sensitive data & CARE principles 🔐
KFM documentation emphasizes:
- **Location generalization** (coarsen coords for sensitive sites)
- **Access control** for restricted data
- **Sensitivity tags** in metadata
- **CARE-aligned governance** for Indigenous/community data (Authority to Control, Responsibility, Ethics)[^kfm-tech]

> [!IMPORTANT]
> If a story step zooms to a sensitive location, prefer:
> - region polygons / hex bins
> - blurred bounding boxes
> - “click-to-acknowledge” warnings (if your UI supports it)
> - or omit entirely from public story packs

---

## 🧪 Experiment report integration

This folder lives inside an **experiment report template**, so Story Nodes should help answer:

- ✅ *What changed?* (state transitions)
- ✅ *Where/when did it change?* (map + timeline sync)
- ✅ *Why do we believe it?* (evidence manifest + citations)
- ✅ *How was it produced?* (run manifests, environment, metrics)

### 1) Tie a story to an experiment/run (recommended)
Add a lightweight `run.manifest.json` (or link to one elsewhere) so dev_prov can connect UI narrative ↔ pipeline execution:

- run id
- dataset versions
- environment hash / container digest
- metric spec id (if model evaluation is involved)[^kfm-additional][^science-protocol]

### 2) Reporting ML/analytics results inside stories
If your story summarizes a model, include *transparent metrics* (macro precision/recall/F1 is a common baseline) and cite evaluation artifacts.[^data-mining]

> [!TIP]
> If a domain uses custom evaluation, KFM proposes versioned “spec files” like **MetricSpec** so everyone knows exactly how a score was computed.[^kfm-additional]

### 3) Reproducibility habits
Align with the “living documentation” + peer review guidance:
- keep docs versioned with code
- update docs in the same commit as changes
- run periodic audits
- encourage replication/peer review of experiments[^science-protocol]

---

## ✅ QA checklist

Before merging a new story package:

### Content ✅
- [ ] `id` / `storyId` is unique and stable
- [ ] Every factual claim has a citation
- [ ] Fact vs interpretation sections are clearly marked
- [ ] No sensitive locations are revealed (or they are generalized + justified)

### UI correctness 🗺️
- [ ] Each `layers[].id` exists in the catalog / layer registry
- [ ] Each step has a sane camera + timeline state
- [ ] Step transitions feel smooth (no jarring jumps)
- [ ] Works on narrow/mobile layouts (story panel bottom)[^kfm-ui]

### Provenance 🔎
- [ ] `evidence.manifest.yaml` includes every cited dataset/doc/image
- [ ] Checksums are provided for local artifacts (images, exported charts)
- [ ] AI-assisted text is disclosed in metadata (if used), with human review noted[^kfm-intake][^kfm-ai]

### Governance & CI 🔐
- [ ] Licenses are declared for datasets + images
- [ ] No secrets/PII are embedded
- [ ] Policy gates pass (OPA/Conftest-style governance checks where configured)[^kfm-additional]

---

## 🚀 Future extensions

KFM’s roadmap (and related proposals) point to upgrades that fit naturally here:

- 🧰 **Visual Story Builder (GUI)** so authors don’t hand-edit JSON[^kfm-tech][^kfm-latest]  
- 📦 **Offline story packs** for field/classroom use (bundled layers + stories)[^kfm-ai]  
- 🛰️ **“Kansas From Above” 3D stories** blending 2D → 3D camera transitions (Cesium)[^kfm-latest][^kfm-arch]  
- 📍 **Pulse Threads** (timely, geotagged micro-stories) as a “live feed” sibling to Story Nodes[^kfm-additional][^doc-refine]  
- 🧠 **Conceptual Attention Nodes** to help Focus Mode + story generation stay thematically complete and transparent[^kfm-additional]  
- 📈 **Narrative Pattern Detection** (detectors → templated narratives → curated publication)[^kfm-additional]  
- 🌍 Long-horizon ideas like “4D digital twin” concepts and advanced governance/credit systems[^kfm-innov]

---

## 📚 Reference library

> [!NOTE]
> Some items in the project library are **PDF Portfolios** and may require Acrobat/Reader to access their embedded documents.[^ai-portfolio][^maps-portfolio][^prog-portfolio][^data-mgmt-portfolio]

### Core KFM docs (directly informing Story Nodes)
- UI + Story Nodes + playback UX: [^kfm-ui]  
- Implementation details (Markdown renderer + MapLibre/Cesium API calls): [^kfm-tech]  
- Full stack & roadmap (MapLibre/Cesium, AR, offline): [^kfm-arch]  
- Focus Mode + RAG + governance checks: [^kfm-ai]  
- Provenance-first intake + OPA-style “must cite” enforcement: [^kfm-intake]  
- Markdown/JSON story convention + “Kansas From Above” idea: [^kfm-latest]  
- Evidence manifests, Pulse Threads, policy gates, OCI artifact ideas: [^kfm-additional]  

### Supporting references used by this template
- Story Node & Focus Mode integration rules (machine-ingestible narrative): [^md-guide]  
- Validation + reproducible documentation practices: [^science-protocol]  
- Evaluation metrics + privacy techniques (macro P/R/F1, k-anonymity, etc.): [^data-mining]  
- Geospatial processing + 3D visualization patterns (GDAL → 3D assets): [^geo-cookbook]  
- Historical mapping hub design patterns (validation, time slider, moderation): [^kfm-hubdesign]  

---

## Footnotes / Sources 🔗

[^kfm-ui]: **Kansas Frontier Matrix – Comprehensive UI System Overview** (Story Nodes, story content management, narrative playback UI).  [oai_citation:0‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  [oai_citation:1‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
[^kfm-tech]: **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** (Markdown+JSON story implementation; MapLibre/Cesium step application; story_nodes assets).  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
[^kfm-arch]: **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design** (Story Nodes concept; stack: React/TypeScript + MapLibre + Cesium; roadmap: offline/AR).  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
[^kfm-ai]: **Kansas Frontier Matrix (KFM) – AI System Overview** (Focus Mode: citations, RAG, governance checks, explainability).  [oai_citation:6‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
[^kfm-intake]: **📚 KFM Data Intake – Technical & Design Guide** (provenance-first; AI output as artifact; “no source → no answer”; policy checks).  [oai_citation:7‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:8‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
[^kfm-latest]: **🌟 Latest Ideas & Future Proposals** (Interactive storytelling enhancements; Markdown/JSON story convention; “Kansas From Above” 3D story).  [oai_citation:9‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  
[^kfm-additional]: **Additional Project Ideas** (Evidence Manifest; Run Manifest; Policy Gate/OPA; Pulse Threads; Conceptual Attention Nodes; OCI artifacts).  [oai_citation:10‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:11‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:12‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
[^doc-refine]: **Document Refinement Request (within Additional Project Ideas)** (Pulse Threads architecture & evidence-first narrative).  [oai_citation:13‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:14‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
[^kfm-innov]: **Innovative Concepts to Evolve KFM** (governance/credit; forward-looking digital twin references).  [oai_citation:15‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  [oai_citation:16‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
[^kfm-hubdesign]: **Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design** (system architecture; validation; time-series patterns; moderation).  [oai_citation:17‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)  
[^md-guide]: **MARKDOWN_GUIDE_v13** (Story Nodes as governed, machine-ingestible storytelling; entity refs; fact vs interpretation; Focus Mode hard rules).  [oai_citation:18‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
[^science-protocol]: **Scientific Method / Research / Master Coder Protocol Documentation** (living docs, validation, peer review, reproducibility).  [oai_citation:19‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  [oai_citation:20‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)  
[^data-mining]: **Data Mining Concepts & Applications** (attention-based models; macro precision/recall/F1; privacy concepts like k-anonymity & inference control).  [oai_citation:21‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)  
[^geo-cookbook]: **Python Geospatial Analysis Cookbook** (GDAL workflows; 3D terrain visualization patterns).  [oai_citation:22‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  [oai_citation:23‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  

[^ai-portfolio]: **AI Concepts & more** (PDF portfolio; open with Acrobat/Reader to access embedded docs).  [oai_citation:24‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)  
[^prog-portfolio]: **Various programming languages & resources** (PDF portfolio; open with Acrobat/Reader).  [oai_citation:25‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
[^data-mgmt-portfolio]: **Data Management / Architectures / Bayesian Methods** (PDF portfolio; open with Acrobat/Reader).  [oai_citation:26‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)  
[^maps-portfolio]: **Maps / GoogleMaps / VirtualWorlds / Archaeological / Geospatial WebGL** (PDF portfolio; open with Acrobat/Reader).  [oai_citation:27‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)  
