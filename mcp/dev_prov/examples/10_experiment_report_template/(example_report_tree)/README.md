# 🧪 Experiment Report Template — `example_report_tree`

![MCP](https://img.shields.io/badge/MCP-dev__prov-blue)
![Template](https://img.shields.io/badge/status-template-brightgreen)
![Provenance](https://img.shields.io/badge/provenance-first-success)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-informational)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-purple)
![Pipelines](https://img.shields.io/badge/pipelines-deterministic%20%2B%20idempotent-0aa)

> [!NOTE]
> This folder is a **copy‑ready, provenance‑first experiment report skeleton** for Kansas Frontier Matrix (KFM).  
> It’s designed so *every experiment result can be audited, reproduced, and safely promoted into*:
> - 🗺️ map layers (MapLibre/Cesium)
> - 📚 Story Nodes (step-based narrative playback)
> - 🤖 Focus Mode outputs (citation-bound answers)
>
> The philosophy is: **no “mystery layers”, no untraceable claims, no silent rewrites**. Every artifact is tied to evidence and lineage.

---

## 🎯 What this template is for

Use this template whenever you run an experiment that might change or produce any of the following:

- ✅ a **new dataset** (e.g., GeoParquet/COG/PMTiles)
- ✅ a **new processing pipeline or pipeline parameter set**
- ✅ a **new AI/ML output** (model, metrics, embeddings, label set, etc.)
- ✅ a **new narrative** (Story Node / Pulse Thread) backed by data
- ✅ a **graph/ontology change** (new node types, relationships, migrations)
- ✅ a **UI integration** (new layer, legend, timeline behavior)

This template aligns with KFM’s contract-first, provenance-first approach: metadata + provenance are mandatory, and policy gates fail closed.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:1‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  [oai_citation:2‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧠 Core rules (aka “don’t make Future-You sad”)

### 1) **Evidence Triplet required** 🧾🛰️🧬
Every promoted output should have:
- **STAC** (asset-level discoverability, spatial/temporal footprints)
- **DCAT** (dataset-level catalog, licensing, attribution, distribution)
- **PROV** (lineage: *Entity–Activity–Agent*)

KFM enforces this as a foundational contract and expects derived outputs (including AI answers) to stay citation-bound.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 2) **Deterministic + idempotent runs** 🔁
Runs should be replayable: same inputs → same outputs (or deltas must be explained).  
For automated runs, prefer:
- a **Run Manifest** with an **idempotency key**
- canonicalized JSON + **sha256 digest**
- stored for audit + policy checks

This is explicitly recommended for KFM automation and governance.  [oai_citation:5‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:6‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 3) **Policy gates apply to humans AND agents** 🛡️
OPA/Conftest policy packs gate merges (licenses, schema validity, sensitivity tags, “no secrets”, AI citation rules, etc.).  [oai_citation:7‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  [oai_citation:8‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 4) **Focus Mode + narratives must be sourceable** 🤖📚
Focus Mode should not introduce unsourced material: answers and narratives must trace to graph/datasets/docs.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:10‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 📁 Directory layout

Below is the **intended structure** of this `example_report_tree` folder. Copy it, rename it, and fill it.

```text
📁 example_report_tree/
├─ 📄 README.md                     ← you are here
├─ 🧾 report.md                     ← human-readable experiment report (Markdown)
├─ ⚙️ report.yaml                   ← machine-readable metadata index (IDs, params, checksums)
│
├─ 📦 artifacts/                    ← what you publish/cite
│  ├─ 🛰️ stac/                      ← STAC Collection + Item(s)
│  ├─ 🗂️ dcat/                      ← DCAT Dataset record(s)
│  ├─ 🧬 prov/                      ← PROV-O JSON-LD (run + outputs)
│  ├─ 🧾 manifests/                 ← run_manifest + evidence_manifest (canonicalized)
│  ├─ 🔏 attestations/              ← SBOM + in-toto + cosign refs (optional)
│  └─ 📎 exports/                   ← deliverables (PMTiles/GeoParquet/COG/etc.)
│
├─ 🧪 work/                         ← experiment workspace (reproducible but not necessarily “published”)
│  ├─ 📓 notebooks/
│  ├─ 🐍 scripts/
│  ├─ 🧱 configs/                   ← deterministic params; no “magic defaults”
│  └─ 🧫 samples/                   ← tiny sample inputs for reviewers (optional)
│
├─ 📊 results/                      ← results + diagnostics
│  ├─ 📈 metrics/                   ← metrics.json/csv (and metric spec IDs if relevant)
│  ├─ 🖼️ figures/                   ← plots, maps, screenshots
│  └─ 🧵 logs/                      ← run logs (sanitized)
│
├─ 🗺️ ui/                           ← optional: wire outputs to UI/Stories
│  ├─ 🧩 layers/                    ← layer registry entry + style/legend
│  └─ 📚 story_nodes/               ← story markdown + map-state JSON steps
│
└─ 🔗 registry/                     ← optional: OCI/ORAS pointers (digest, tags, verify steps)
   ├─ 📄 oci_refs.yaml
   └─ 📄 cosign_verify.md
```

> [!TIP]
> Keep **big binaries** out of git when possible. Prefer **OCI artifact distribution** (ORAS + Cosign) and reference by **immutable digest** in STAC/DCAT metadata.  [oai_citation:11‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:12‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧾 What to put in `report.md`

Treat `report.md` as the human-facing narrative of the experiment (reviewers should understand it in <10 minutes).

### Suggested sections (copy/paste)
- **Overview**: what you tested + why
- **Research question / hypothesis**
- **Inputs**: dataset IDs, versions, licenses, sensitivity classification
- **Method**: pipeline steps, params, environment, “what changed”
- **Results**: metrics + visuals + key findings
- **Risk & governance**: FAIR/CARE, redaction/sensitivity notes, failure modes
- **Decision**: promote / revise / reject + why
- **Next steps**: exact TODOs

If you want KFM-style consistency, use YAML front matter patterns (title, version, status, doc_kind, governance refs, integrity checksum).  [oai_citation:13‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

---

## ⚙️ What to put in `report.yaml` (machine index)

This file is meant to be grep-friendly and CI-friendly.

**Example (template-ish):**
```yaml
experiment_id: "exp-YYYYMMDD-####-short_slug"
title: "TBD"
status: "draft"          # draft | in_review | approved | deprecated
owners: ["@you"]
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"

question: "TBD"
hypothesis: "TBD"

inputs:
  - dataset_id: "kfm.<domain>.<name>.vX"
    stac_ref: "../artifacts/stac/<collection_or_item>.json"
    dcat_ref: "../artifacts/dcat/<dataset>.jsonld"
    license: "TBD"
    sensitivity: "public"  # public | restricted | confidential

outputs:
  - artifact_name: "TBD"
    type: "GeoParquet|COG|PMTiles|Model|Embedding|..."
    stac_ref: "../artifacts/stac/<item>.json"
    dcat_ref: "../artifacts/dcat/<dataset>.jsonld"
    prov_ref: "../artifacts/prov/<run>.prov.jsonld"
    oci_digest: "sha256:TBD"     # if published to registry
    cosign_ref: "../artifacts/attestations/<sig or attestation>.txt"

run:
  run_manifest: "../artifacts/manifests/run_manifest.json"
  idempotency_key: "sha256:TBD"
  environment:
    git_commit: "TBD"
    python: "TBD"
    container_image: "TBD"

evaluation:
  metrics_file: "../results/metrics/metrics.json"
  acceptance_criteria:
    - "TBD"

ui_integration:
  layer_entry: "../ui/layers/<layer>.yaml"
  story_node: "../ui/story_nodes/<story>.md"
```

> [!NOTE]
> If you don’t know a field yet, prefer `"TBD"` over deleting it — schema/policy gates often expect stable shapes.  [oai_citation:14‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

---

## 📦 Evidence & provenance artifacts (what “done” means)

### Required minimum ✅
- `artifacts/stac/*`  
- `artifacts/dcat/*`  
- `artifacts/prov/*`  
- `artifacts/manifests/run_manifest.*` *(recommended)*

KFM treats these as contract artifacts across pipeline subsystems (ETL, catalogs, graph, APIs, UI, story/focus).  [oai_citation:15‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### Strongly recommended 🔥
- **Evidence Manifest** listing sources used (especially for narratives / AI text)  [oai_citation:16‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **Run Manifest** with canonical digest + idempotency key  [oai_citation:17‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **Policy gate report** (what passed/failed, with versions)  [oai_citation:18‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  

### Optional but powerful 🧩
- OCI artifact distribution (`registry/`) using **ORAS + Cosign**, with signatures stored as registry referrers  [oai_citation:19‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:20‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- SBOM / in-toto provenance attestations (`artifacts/attestations/`)  [oai_citation:21‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

---

## 🔄 Where this fits in KFM (contracts + promotion path)

KFM operates with subsystem contracts and “do not break” invariants (schema stability, migrations, backward-compatible APIs, no provenance loss, etc.).  [oai_citation:22‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

```mermaid
flowchart LR
  A[🧾 Raw sources] --> B[🧪 ETL / Pipelines]
  B --> C[📦 Artifacts: STAC/DCAT/PROV]
  C --> D[🧠 Graph (Neo4j)]
  C --> E[🗄️ PostGIS / Spatial store]
  D --> F[🔌 APIs]
  E --> F
  F --> G[🗺️ UI (MapLibre/Cesium)]
  F --> H[🤖 Focus Mode]
  C --> I[📚 Stories / Pulse Threads]
```

> [!IMPORTANT]
> “Provenance-first publishing: all data must have provenance before graph/UI use” applies even to streaming/real-time layers.  [oai_citation:23‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:24‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧭 If your experiment creates UI narratives (Story Nodes)

KFM Story Nodes are modular Markdown files + step configuration so the UI can “play back” a narrative and drive map state changes (pan/zoom, layer on/off, timeline changes, highlights).  [oai_citation:25‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

**Put Story Node content in:**
- `ui/story_nodes/<story>.md` (story text + citations)
- `ui/story_nodes/<story>.json` (step map states / timeline steps)

> [!TIP]
> This is designed so domain experts can contribute story content “without writing code”, while still remaining provenance-linked.  [oai_citation:26‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

---

## 🤖 If your experiment impacts Focus Mode / AI outputs

Focus Mode is designed to rely on the knowledge graph + approved sources so answers stay grounded and citeable.  [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Practical implications for this template:
- include evaluation metrics in `results/metrics/`
- store prompts / retrieval configs deterministically in `work/configs/`
- ensure AI outputs have citations and can be traced back to datasets/docs via PROV and/or Evidence Manifests  [oai_citation:28‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🧰 Dev provenance add‑ons (dev_prov power-ups)

### ✅ Watcher–Planner–Executor (W‑P‑E) agent flow
KFM proposes a safe automation architecture:
- **Watcher** emits immutable facts/alerts
- **Planner** deterministically forms a plan (diff/patch)
- **Executor** opens a PR (never auto‑merges) + kill switch + idempotency keys  [oai_citation:29‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  [oai_citation:30‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

This template is structured so agents can:
- drop run manifests + results in predictable places
- attach provenance artifacts for review

### ✅ PR → PROV graph integration
KFM also maps GitHub PR events into PROV-O (PR as Activity, commits as Entities, authors/reviewers as Agents) so development history becomes queryable lineage.  [oai_citation:31‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  [oai_citation:32‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 📰 Pulse Threads, Conceptual Attention Nodes, Narrative Pattern Detection

If your experiment is about “what’s changing right now” (anomaly detection, event narratives, etc.), align with these KFM glossary terms:

<details>
  <summary><strong>📌 Glossary (click to expand)</strong></summary>

- **Pulse Thread**: short, timely narrative tied to places/data events, citation-backed, map-integrated.  [oai_citation:33‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **Conceptual Attention Node**: graph node for high-level themes (“Drought”, “Infrastructure”) to focus retrieval/context.  [oai_citation:34‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **Narrative Pattern Detection**: system that detects noteworthy patterns (stats/anomalies) and generates narrative explanations.  [oai_citation:35‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **Evidence Manifest**: machine-readable list of evidence sources supporting a narrative.  [oai_citation:36‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- **Run Manifest**: structured record of a pipeline run (inputs, outputs, tools, versions, digests).  [oai_citation:37‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

</details>

---

## ✅ Definition of Done (DoD) checklist

### Baseline (must-have)
- [ ] `report.md` written and understandable
- [ ] `report.yaml` filled (no missing critical fields)
- [ ] STAC + DCAT + PROV exist for every promoted output  [oai_citation:38‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Licenses declared (SPDX-style where possible)
- [ ] Sensitivity/classification declared (and enforced in UI/API if needed)
- [ ] Policy gates pass locally/CI (OPA/Conftest)  [oai_citation:39‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### Reproducibility (strongly recommended)
- [ ] Run manifest captured with canonical digest + idempotency key  [oai_citation:40‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- [ ] Metrics file(s) saved + acceptance criteria stated
- [ ] Any randomness is seeded and recorded
- [ ] Environment recorded (commit sha, container digest, tool versions)

### Supply chain (optional but excellent)
- [ ] Artifacts packaged in OCI registry with immutable digests  [oai_citation:41‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- [ ] Cosign signatures + SBOM / in-toto attestation attached  [oai_citation:42‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 📚 Source docs that shaped this template (project bundle)

> [!NOTE]
> These are the foundational project docs and resource packs this template is aligned with.

### KFM core docs
- **🌟 Latest Ideas & Future Proposals**  [oai_citation:43‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  [oai_citation:44‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- **Comprehensive Architecture, Features, and Design**  [oai_citation:45‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- **AI System Overview 🧭🤖**  [oai_citation:46‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  [oai_citation:47‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- **Comprehensive Technical Documentation**  [oai_citation:48‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  [oai_citation:49‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Comprehensive UI System Overview**  [oai_citation:50‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  [oai_citation:51‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- **📚 Data Intake – Technical & Design Guide**  [oai_citation:52‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  [oai_citation:53‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **Innovative Concepts to Evolve KFM**  [oai_citation:54‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  [oai_citation:55‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- **Document Refinement Request (Pulse/Concept Nodes/Narrative/Graph Health/OCI)**  [oai_citation:56‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  [oai_citation:57‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Additional Project Ideas (OCI artifacts, policy gates, glossary terms)**  [oai_citation:58‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Repo-wide standards / contracts
- **MARKDOWN_GUIDE (contracts, invariants, versioning)**  [oai_citation:59‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Comprehensive Markdown Guide (front matter + doc templates)**  [oai_citation:60‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)

### Research / reference bundles (deep dives)
- **AI Concepts & more (PDF portfolio)**  [oai_citation:61‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
- **Maps / GoogleMaps / Virtual Worlds / Geo WebGL (PDF portfolio)**  [oai_citation:62‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)
- **Data Management / Architectures / Bayesian / Programming ideas (PDF portfolio)**  [oai_citation:63‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)
- **Various programming languages & resources (PDF portfolio)**  [oai_citation:64‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)

---

## 🧩 Next: turn this into your experiment

1) Copy this folder → rename to your experiment slug  
2) Fill `report.yaml` + write `report.md`  
3) Generate artifacts (STAC/DCAT/PROV + manifests)  
4) Add results + figures  
5) (Optional) integrate into UI (layer/story node)  
6) Open PR → let policy gates + reviewers do the rest ✅

Happy experimenting — but keep it evidence-first 🧾✨
