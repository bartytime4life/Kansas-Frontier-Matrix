# 03 — Story Nodes Gate 📖🗺️ (MCP / Gates / Examples)

![MCP](https://img.shields.io/badge/MCP-gates-blue?style=flat)
![Example](https://img.shields.io/badge/example-03--story--nodes-7f8c8d?style=flat)
![Format](https://img.shields.io/badge/format-Markdown%20%2B%20JSON-brightgreen?style=flat)
![Principle](https://img.shields.io/badge/principle-Provenance--First-9cf?style=flat)
![Policy](https://img.shields.io/badge/policy-OPA%20%2B%20Conftest-orange?style=flat)

> [!IMPORTANT]
> This example documents the **Story Nodes Gate**: a fail-closed quality + provenance gate that ensures Story Nodes are (1) **UI-playable** and (2) **evidence-backed** before they can ship into the Kansas Frontier Matrix (KFM) experience.

---

## 🎯 What this gate is for

In KFM, **Story Nodes** are the system’s “guided tours” / interactive narratives: a *step-by-step* story that drives **map state** (layers + camera) and **time** (timeline year/range) while the user reads the narrative. Story Nodes are designed to be **authorable** (domain experts can write them) and **machine-readable** (UI + AI can run them).:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

This gate exists because KFM is explicitly **evidence-first**:
- Story Nodes are authored as **Markdown + JSON config** (narrative + steps):contentReference[oaicite:2]{index=2}
- KFM’s “Focus Mode” and publishing rules require **citations** and provenance (fail closed when missing):contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}
- Governance explicitly calls for automated policy gates (OPA/Conftest) to enforce standards:contentReference[oaicite:5]{index=5}

---

## 🧠 What are “Story Nodes” in KFM?

Story Nodes are:
- 📄 **Narrative content** written in Markdown
- 🧩 A **JSON configuration** describing story steps (each step can set layers, camera view, and timeline year/range)
- 🔗 **Connected to the Knowledge Graph** (places, people, datasets)
- 🧾 **Provable**: every meaningful claim should be traceable to evidence, with provenance metadata

This is the “Story Mode” UX:
- Split view (map + story panel)
- Step navigation (Next/Prev, progress indicator)
- Each step updates the map to the relevant view / layers:contentReference[oaicite:6]{index=6}

---

## 🧭 Quick navigation

- [📦 Recommended example layout](#-recommended-example-layout)
- [🚪 Gate contract](#-gate-contract)
- [✅ Gate checks](#-gate-checks)
- [🧩 Templates](#-templates)
- [🧪 Suggested “Definition of Done”](#-suggested-definition-of-done)
- [📚 Project reference library](#-project-reference-library-used)
- [📎 Evidence trail](#-evidence-trail)

---

## 📦 Recommended example layout

This example assumes each Story Node is a small **bundle** (narrative + config + evidence + provenance).

```text
mcp/gates/examples/03-story-nodes/
├─ 📘 README.md  (you are here)
└─ 📦 story-node-pack/                # (recommended) one runnable Story Node
   ├─ 🧾 node.md                       # Markdown narrative (with front matter)
   ├─ 🧩 node.config.json              # Step config (map/timeline states)
   ├─ 🧾 evidence/
   │  └─ 🧾 EM-0001.yaml               # Evidence manifest (sources + artifacts)
   ├─ 🧬 prov/
   │  └─ 🧬 node.prov.jsonld           # PROV bundle linking transforms + sources
   ├─ 🖼️ assets/
   │  ├─ 🖼️ hero.jpg
   │  └─ 🖼️ inline-diagram.png
   └─ 📤 exports/                      # (optional) generated artifacts
      ├─ 🗺️ tiles.pmtiles
      └─ 🧾 citations.json
```

> [!NOTE]
> KFM’s architecture describes Story Nodes as folders containing Markdown + JSON config (machine-readable “guided tours”).:contentReference[oaicite:7]{index=7}

---

## 🚪 Gate contract

### ✅ Input
A **Story Node Pack** directory containing:
- `node.md` (Markdown narrative)
- `node.config.json` (steps: camera/layers/timeline)
- `evidence/EM-xxxx.yaml` (evidence manifest)
- `prov/*.jsonld` (provenance bundle)

### ✅ Output
A **GateResult** (conceptually):
- pass/fail
- structured errors + warnings
- optional generated artifacts (normalized config, extracted citations index, etc.)

> [!IMPORTANT]
> KFM governance explicitly supports automated policy gates (e.g., OPA/Conftest) and fail-closed rules for provenance/citation standards.:contentReference[oaicite:8]{index=8}

---

## ✅ Gate checks

Below are the checks this gate is designed to enforce (policy-as-code style):

### 1) 🧾 Narrative is evidence-first
- [ ] **Every meaningful claim** is tied to a citation (or explicitly marked as interpretation)
- [ ] Citations are **inspectable** (user can trace back to sources)
- [ ] If evidence is missing, we **refuse** to claim certainty (aligns with Focus Mode constraints):contentReference[oaicite:9]{index=9}:contentReference[oaicite:10]{index=10}

### 2) 🔗 Graph-aware references
- [ ] Story Node references Knowledge Graph entities (people/places/events/datasets)
- [ ] IDs are stable (no “mystery strings”)

> KFM’s Markdown/Story Node guidance calls for Story Nodes to reference graph entities and distinguish fact vs interpretation.:contentReference[oaicite:11]{index=11}

### 3) 🧬 Provenance bundle exists and is consistent
- [ ] `prov/*.jsonld` exists
- [ ] Evidence manifest entries map to the citations used in the Markdown
- [ ] Evidence/transform chain is captured (inputs → processing → outputs)

> Additional project ideas propose Story Nodes that include **evidence manifests** and a **PROV JSON-LD** bundle, with “View Evidence” UX support and CI validation of citations ↔ manifest resolution.:contentReference[oaicite:12]{index=12}

### 4) 🗺️ UI-playable steps (config-driven storytelling)
- [ ] Config has a `steps[]` array
- [ ] Each step defines:
  - map camera state (2D/3D)
  - layers on/off (or layer preset)
  - timeline year/range
- [ ] Steps are deterministic (same input pack → same UX)

> The UI spec describes Story Mode with a story panel and step navigation where each step updates map view/layers.:contentReference[oaicite:13]{index=13}

### 5) 🧠 AI transparency + “Focus Mode” alignment
- [ ] If AI assisted, it is declared (opt-in, transparent)
- [ ] Outputs must remain evidence-backed (citations required)

> Focus Mode rules are treated as a hard gate: citations required; no inventing data; opt-in AI; no sensitive leaks.:contentReference[oaicite:14]{index=14}

### 6) 🏷️ Governance metadata (FAIR/CARE + sensitivity)
- [ ] Has license + usage constraints (when applicable)
- [ ] Has a CARE/visibility/sensitivity label (especially for cultural or sensitive content)

> Governance docs emphasize ethics, compliance, and FAIR/CARE-inspired practices and controls in the pipeline.:contentReference[oaicite:15]{index=15}

---

## 🧩 Templates

### 📄 `node.md` (Markdown narrative + front matter)

> [!TIP]
> Keep the narrative pleasant to read, but **treat it like a dataset**: stable IDs, citations, provenance hooks.

```markdown
---
kind: story_node
id: kfm:story:example:railroads-1860-1880
title: "Railroads reshape Kansas (1860–1880)"
slug: railroads-1860-1880
version: 0.1.0
authors:
  - name: "Your Name"
date_published: "2026-01-23"
license: "CC-BY-4.0"
tags: ["kansas", "railroads", "infrastructure"]
time_span:
  start: 1860
  end: 1880
bbox: [-102.05, 36.99, -94.59, 40.00]
entities:
  places: ["kfm:place:kansas"]
  datasets: ["dcat:dataset:ks-rail-lines"]
evidence_manifest: "evidence/EM-0001.yaml"
prov_bundle: "prov/node.prov.jsonld"
care_label: "Public"
ai_assisted:
  used: false
---

## Step 1 — Setting the stage (1860)

Kansas is still early in its statehood era, and transportation corridors are limited.[^S1]

## Step 2 — Rails expand (1870s)

By the 1870s, rail connectivity changes settlement and trade patterns.[^S2]

---

### Citations (tiny block)
- [S1] Example archival map / dataset entry (see evidence manifest)
- [S2] Example report / dataset entry (see evidence manifest)
```

> The “machine-ingestible” Story Node concept and authoring guidance is explicitly documented in the project Markdown guide.:contentReference[oaicite:16]{index=16}

---

### 🧩 `node.config.json` (step config)

```json
{
  "story_id": "kfm:story:example:railroads-1860-1880",
  "ui": {
    "autoplay": false,
    "progress": "dots"
  },
  "steps": [
    {
      "id": "step-01",
      "title": "Kansas in 1860",
      "timeline": { "year": 1860 },
      "camera": { "mode": "2d", "center": [-98.0, 38.5], "zoom": 6.2 },
      "layers": { "on": ["base", "boundaries_1860"], "off": ["rail_lines"] },
      "narrative_anchor": "step-1"
    },
    {
      "id": "step-02",
      "title": "Rail expansion in the 1870s",
      "timeline": { "range": [1870, 1880] },
      "camera": { "mode": "2d", "center": [-96.5, 38.7], "zoom": 6.5 },
      "layers": { "on": ["base", "rail_lines"], "off": ["boundaries_1860"] },
      "narrative_anchor": "step-2"
    }
  ]
}
```

> Story nodes are explicitly described as config-driven guided tours (Markdown + JSON; step = map state).:contentReference[oaicite:17]{index=17}

---

### 🧾 `evidence/EM-0001.yaml` (evidence manifest)

This is the “bridge” between human citations and machine validation (CI can check citations resolve).

```yaml
id: EM-0001
story_id: kfm:story:example:railroads-1860-1880
created: 2026-01-23
sources:
  - id: S1
    type: dataset
    title: "Kansas railroad lines (sample)"
    ref: "dcat:dataset:ks-rail-lines"
    used_in_steps: ["step-02"]
  - id: S2
    type: document
    title: "Historical report (sample)"
    ref: "kfm:doc:report-1878"
    used_in_steps: ["step-02"]
artifacts:
  - id: A1
    type: tiles
    media_type: application/vnd.pmtiles
    path: exports/tiles.pmtiles
```

> The “Evidence manifest + PROV bundle” idea is spelled out as a Story Node pattern (with CI validation + a “View Evidence” UX hook).:contentReference[oaicite:18]{index=18}

---

### 🧬 `prov/node.prov.jsonld` (minimal PROV skeleton)

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "kfm": "https://kfm.example/ns#"
  },
  "@id": "kfm:story:example:railroads-1860-1880",
  "@type": "kfm:StoryNode",
  "prov:used": [
    { "@id": "kfm:evidence:S1" },
    { "@id": "kfm:evidence:S2" }
  ],
  "prov:wasGeneratedBy": {
    "@id": "kfm:activity:build-story-pack-2026-01-23",
    "@type": "prov:Activity"
  }
}
```

---

## 🧪 Suggested Definition of Done

Before a Story Node Pack should pass the gate:

- [ ] ✅ `node.md` has front matter + stable `id`
- [ ] ✅ Every meaningful claim is cited or labeled interpretation:contentReference[oaicite:19]{index=19}
- [ ] ✅ `node.config.json` steps all define timeline + camera + layers
- [ ] ✅ Evidence manifest exists and matches citations:contentReference[oaicite:20]{index=20}
- [ ] ✅ PROV bundle exists and links sources/artifacts
- [ ] ✅ Sensitivity / care label set (if applicable):contentReference[oaicite:21]{index=21}
- [ ] ✅ Focus Mode constraints satisfied (citations, no invention, opt-in AI):contentReference[oaicite:22]{index=22}

---

## 🧠 Why this lives under `mcp/gates/…`

KFM adopts a **documentation-first, reproducible** philosophy aligned with MCP:
- `mcp/` is a home for SOPs, experiments, glossary, model cards, and other repeatable workflows:contentReference[oaicite:23]{index=23}
- The broader MCP documentation emphasizes scientific-method discipline, protocols, provenance, and repeatable methods:contentReference[oaicite:24]{index=24}:contentReference[oaicite:25]{index=25}

This example is intentionally “policy-minded”: **story content is a deliverable**, so it must meet the same reproducibility standards as code.

---

## 🔮 Extension ideas (aligned with project proposals)

- 🎬 **Hybrid 2D/3D story playback** (camera transitions, 3D moments in story steps)
- 🛠️ **Visual Story Builder UI** (drag steps, set layers/camera/timeline, export pack):contentReference[oaicite:27]{index=27}
- 🧾 **Stronger CI validation** (citations ↔ evidence manifest ↔ PROV ↔ graph entities)
- 📦 **Portable story packs** (shareable bundles with signed artifacts)

---

## 📚 Project reference library (used)

> [!NOTE]
> Some “books/resources” files are **PDF portfolios** (collections of embedded docs). They may require Adobe Reader/Acrobat to browse fully.:contentReference[oaicite:28]{index=28}

### Core KFM design + architecture 📌
- 📘 **Comprehensive Architecture, Features, and Design** — Story Nodes + governance/policy gates:contentReference[oaicite:29]{index=29}:contentReference[oaicite:30]{index=30}
- 🎛️ **Comprehensive UI System Overview** — Story Mode UI and future Story Builder tooling:contentReference[oaicite:31]{index=31}:contentReference[oaicite:32]{index=32}
- 🧭 **AI System Overview** — Focus Mode expectations (citations, evidence-based answers):contentReference[oaicite:33]{index=33}
- 📚 **Data Intake – Technical & Design Guide** — Provenance-first publishing, validation, FAIR/CARE framing:contentReference[oaicite:34]{index=34}:contentReference[oaicite:35]{index=35}
- 🌟 **Latest Ideas & Future Proposals** — Story improvements, transitions, authoring ideas:contentReference[oaicite:36]{index=36}
- 💡 **Innovative Concepts to Evolve KFM** — 2D/3D storytelling and related concepts
- 🧩 **Additional Project Ideas** — Evidence manifests, PROV bundles, CI validation concepts:contentReference[oaicite:38]{index=38}

### MCP / reproducibility backbone 🧪
- 🧰 **Open-Source Geospatial Historical Mapping Hub Design** — `mcp/` directory + SOP/experiment/model-card structure:contentReference[oaicite:39]{index=39}
- 🧪 **Scientific Method / Research / MCP Documentation** — documentation-first, reproducible, modular methodology:contentReference[oaicite:40]{index=40}

### Resource portfolios (embedded books/docs) 📦
- 🤖 **AI Concepts & more** (PDF portfolio):contentReference[oaicite:41]{index=41}
- 🌍 **Maps / Google Maps / Virtual Worlds / Geospatial WebGL** (PDF portfolio):contentReference[oaicite:42]{index=42}
- 🧰 **Various programming languages & resources 1** (PDF portfolio):contentReference[oaicite:43]{index=43}
- 🗄️ **Data Management / Architectures / Bayesian Methods** (PDF portfolio):contentReference[oaicite:44]{index=44}

---

## 📎 Evidence trail

<details>
<summary>Show evidence snippets used to author this README 🧾</summary>

- Story Nodes as guided tours (folder with Markdown + JSON config; step = map state):contentReference[oaicite:45]{index=45}
- Story Mode split panel + step navigation + map updates per step:contentReference[oaicite:46]{index=46}
- Governance: automated policy gates; AI outputs require citations / refuse without sources:contentReference[oaicite:47]{index=47}
- Provenance-first publishing rule via policy pack (OPA/Conftest checks; fail-closed):contentReference[oaicite:48]{index=48}
- Focus Mode rules (hard gate): citations required; no inventing; opt-in AI; no sensitive leaks:contentReference[oaicite:49]{index=49}
- Story Nodes should reference graph entities and distinguish fact vs interpretation:contentReference[oaicite:50]{index=50}
- Evidence manifest + PROV bundle + “View Evidence” concept for Story Nodes:contentReference[oaicite:51]{index=51}
- `mcp/` directory for experiments/SOPs/glossary/model cards & reproducibility framing:contentReference[oaicite:52]{index=52}
- MCP documentation-first / reproducible / modular methodology framing:contentReference[oaicite:53]{index=53}
- PDF portfolios require Acrobat/Reader for best experience (resource packs):contentReference[oaicite:54]{index=54}

</details>

<!-- Required file cites for tool linkage: :contentReference[oaicite:55]{index=55} :contentReference[oaicite:56]{index=56} :contentReference[oaicite:57]{index=57} -->

