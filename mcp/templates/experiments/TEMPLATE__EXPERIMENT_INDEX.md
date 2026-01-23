<!--
📄 Template: mcp/templates/experiments/TEMPLATE__EXPERIMENT_INDEX.md
🎯 Intended destination: mcp/experiments/EXPERIMENT_INDEX.md
🧠 MCP = Master Coder Protocol
-->

# 🧪 MCP Experiment Index (Template) — Kansas Frontier Matrix 🌾🧭

![MCP](https://img.shields.io/badge/MCP-Master%20Coder%20Protocol-2b6cb0)
![Evidence](https://img.shields.io/badge/Evidence%E2%80%91First-Required-0f766e)
![Provenance](https://img.shields.io/badge/PROV-STAC%20%2B%20DCAT%20%2B%20PROV-7c3aed)
![Reproducible](https://img.shields.io/badge/Reproducible-Yes-16a34a)
![Status](https://img.shields.io/badge/Index-Template-f59e0b)

> [!NOTE]
> This file is the **single master registry** for experiments across KFM (data intake 🧾, mapping 🗺️, UI 🧩, AI 🤖, graph 🧠, ops ⚙️, AR 🥽).  
> Keep it **boringly consistent** so W→P→E automation, CI gates, and humans can all trust it.  
> Inspired by MCP’s requirement for unique experiment IDs + a master index.

---

<details>
<summary>📚 Table of Contents</summary>

- [✅ How to use this template](#-how-to-use-this-template)
- [🧾 ID conventions](#-id-conventions)
- [🗂️ Recommended folder layout](#️-recommended-folder-layout)
- [📋 Experiment registry](#-experiment-registry)
- [✅ Minimum entry contract](#-minimum-entry-contract)
- [🧬 Manifests & artifacts](#-manifests--artifacts)
- [🧯 Governance, licensing, and ethics](#-governance-licensing-and-ethics)
- [📈 Metrics menu](#-metrics-menu)
- [🧩 Domain playbooks](#-domain-playbooks)
- [🔍 Review, replication, closeout](#-review-replication-closeout)
- [📚 Research library pointers](#-research-library-pointers)
- [🔗 Related MCP templates](#-related-mcp-templates)
- [🧾 Sources used to design this template](#-sources-used-to-design-this-template)

</details>

---

## ✅ How to use this template

1. **Copy** this file to: `mcp/experiments/EXPERIMENT_INDEX.md`
2. For every experiment:
   - Create an experiment folder (recommended layout below).
   - Add a single **row** in the registry table.
   - Add a **details block** (optional but encouraged for anything non-trivial).
3. Treat updates like code:
   - PR required ✅
   - CI must pass ✅
   - Policy gates must pass ✅ (license/provenance/sensitivity)

---

## 🧾 ID conventions

> [!IMPORTANT]
> Every experiment must have a **unique ID** and appear in this index.

### Format

`EXP-<DOMAIN>-<YYYY>-<NNN>`

Examples:
- `EXP-AI-2026-001`
- `EXP-UI-2026-004`
- `EXP-INGEST-2026-002`
- `EXP-4D-2026-001` (Voxel/4D/temporal digital twin experiments)

### Suggested domains (extend as needed)

| Domain Tag | Meaning |
|---|---|
| `AI` | Focus Mode, retrieval, evaluation, model changes |
| `UI` | React UI, map/timeline/story nodes UX, accessibility |
| `MAP` | MapLibre/Cesium layers, tiles, performance |
| `GRAPH` | Neo4j schema, linkers, graph QA, concept nodes |
| `INGEST` | ETL, catalog, provenance, idempotent ingestion |
| `POLICY` | OPA/Rego gates, licensing, sensitivity policies |
| `SIM` | Scenario engine + outputs visualization |
| `AR` | AR overlays, location-based narratives |
| `4D` | VoxelMaps / 4D spatiotemporal structures |
| `OPS` | W→P→E agents, CI/CD, observability, packaging |

---

## 🗂️ Recommended folder layout

```text
mcp/
└─ 🧪 experiments/
   ├─ 🧾📄 EXPERIMENT_INDEX.md                 # 👈 (generated) Registry of experiments (ids, status, links, key outcomes)
   ├─ 🧪 EXP-AI-2026-001__focus-mode-citations/ # One experiment folder (area + year + sequence + short slug)
   │  ├─ 📄 README.md                          # Overview: purpose, scope, owners, timeline, and quick links
   │  ├─ 🧪📄 protocol.md                      # Protocol: hypothesis, method, datasets, metrics, acceptance criteria
   │  ├─ 📊📄 results.md                       # Results: metrics, findings, artifacts links, limitations, follow-ups
   │  ├─ ✅📄 decision.md                      # ✅ Ship / don’t ship decision + rationale + required follow-ups
   │  ├─ 🧬 manifests/                         # Provenance/evidence receipts (machine-verifiable)
   │  │  ├─ 🧾🔐 run_manifest.json              # Run manifest: env, commands, inputs/outputs, tool versions, hashes
   │  │  ├─ 🧬🧾 prov.jsonld                    # PROV bundle: lineage graph linking inputs → run → outputs
   │  │  └─ 📎🧾 evidence_manifest.yaml         # Evidence manifest (only when narrative-facing outputs exist)
   │  ├─ 📦 artifacts/                         # Produced artifacts (signed OCI artifacts / exports / figures; keep access-safe)
   │  │  └─ 🔏📦 …                             # e.g., digests, signatures, exported datasets, charts
   │  └─ 📓 notebooks/                         # Optional notebooks used during the experiment (keep runnable)
   │     └─ 📓 exploration.ipynb               # Exploration notebook (should reference manifests + pinned env)
   └─ 🧪 EXP-INGEST-2026-002__gtfs-rt-watcher/  # Another experiment (example placeholder)
      └─ ➕ …                                    # Same structure: protocol/results/decision/manifests/artifacts/notebooks

```

> [!TIP]
> KFM already uses notebooks for exploration and pipelines designed to be deterministic/reproducible; keep experiments aligned with that culture.

---

## 📋 Experiment registry

### Status legend 🧭
- 🧠 **Proposed** (idea exists, protocol not written)
- 📝 **Planned** (protocol approved, not started)
- 🧪 **Running** (actively executing)
- 🧰 **Analyzing** (runs done, results being interpreted)
- ✅ **Completed** (decision made, documented)
- 🚢 **Shipped** (merged & deployed)
- 🧊 **Archived** (kept for reference)

---

### Registry table (copy/paste rows)

> [!NOTE]
> Keep titles short. Put full context in the details block below.

| ID | Title | Domain | Status | Owner | Start | End | Surfaces 🎛️ | Data / Model touchpoints | Links |
|---|---|---:|---:|---|---|---|---|---|---|
| `EXP-___-____-___` | `<short name>` | `<AI/UI/INGEST/...>` | 🧠 Proposed | `@handle` | `YYYY-MM-DD` | `—` | `Map` `Timeline` `Focus` `Story` `API` | `<datasets/models>` | `[protocol](./EXP-.../protocol.md) · [results](./EXP-.../results.md)` |
| `EXP-___-____-___` | `<short name>` | `<...>` | 📝 Planned | `@handle` | `YYYY-MM-DD` | `—` |  |  |  |
| `EXP-___-____-___` | `<short name>` | `<...>` | ✅ Completed | `@handle` | `YYYY-MM-DD` | `YYYY-MM-DD` |  |  |  |

---

## ✅ Minimum entry contract

Every experiment row **must** have:

- [ ] Unique ID + folder name matches the ID pattern
- [ ] `protocol.md` (hypothesis, method, metrics, stop conditions)
- [ ] `results.md` (what happened + artifacts + analysis)
- [ ] `decision.md` (ship/no-ship + why + follow-ups)
- [ ] `run_manifest.json` for each run (or for the “main run”)
- [ ] Provenance recorded (PROV) before anything is surfaced to graph/UI
- [ ] If experiment produces **narrative-facing outputs** (Story Node / Pulse Thread): include an Evidence Manifest

---

## 🧬 Manifests & artifacts

### 1) Run Manifest (`manifests/run_manifest.json`)
A structured record of a pipeline run / experiment run: run id, timestamps, inputs, outputs, env details, plus an integrity hash.

Minimal example:

```json
{
  "run_id": "RUN-2026-01-21T00:00:00Z__EXP-AI-2026-001",
  "experiment_id": "EXP-AI-2026-001",
  "started_at": "2026-01-21T00:00:00Z",
  "ended_at": "2026-01-21T00:10:00Z",
  "git": { "repo": "kansas-frontier-matrix", "commit": "<sha>" },
  "inputs": [
    { "type": "dataset", "id": "DS-...", "ref": "data/catalog/DS-....json", "sha256": "<...>" }
  ],
  "outputs": [
    { "type": "artifact", "ref": "oci://registry/kfm/...", "digest": "sha256:<...>" }
  ],
  "environment": {
    "container": "ghcr.io/<org>/<image>:<tag>",
    "python": "3.12.x"
  },
  "integrity": { "canonicalization": "RFC8785", "sha256": "<hash-of-manifest>" }
}
```

### 2) Provenance (PROV)
KFM uses provenance-first publishing: data must have provenance before graph/UI use.

> [!TIP]
> Treat PROV as the “audit spine” that lets us answer:  
> “Which stories used this dataset?” and “What process produced this artifact?”

### 3) Evidence Manifest (YAML/JSON)
Required when you create or modify:
- Story Nodes (interactive narratives)
- Pulse Threads (geotagged narrative updates)

Evidence manifests make narrative claims machine-checkable and traceable (checksums, dataset IDs, parameters).

### 4) Artifact packaging (OCI + signing) 📦🔏
For heavy outputs (processed datasets, models, simulation results), prefer OCI artifacts and sign them (cosign/oras) for provenance and integrity.

---

## 🧯 Governance, licensing, and ethics

> [!IMPORTANT]
> KFM treats policies as tests: failing policy checks blocks merges, just like failing unit tests.

Minimum checklist per experiment:

- [ ] License OK for all inputs + derived outputs (document licenses in catalogs)
- [ ] Sensitivity classification enforced (no leaking restricted locations/data)
- [ ] No bypass of catalogs/APIs: all published data goes through official catalog + provenance
- [ ] If community/heritage content: align with CARE + Collective Benefit principles (where applicable)
- [ ] If AI-generated content: mark clearly + keep human-in-the-loop

---

## 📈 Metrics menu

Pick metrics that match the experiment domain; document them in `protocol.md`.

### AI / Focus Mode 🤖
- Citation coverage (% of claims with citations)
- Retrieval precision/recall (manual eval set)
- Hallucination rate (red-team prompts)
- “Explainability surface” completeness (citations + concept nodes shown)

### Data intake / pipelines 🧾
- Determinism: same inputs → identical outputs (hash match)
- QA gate pass-rate (catalog + data validation)
- Time-to-ingest (SLO)
- Idempotency (exactly-once ingest)

### UI / UX 🧩
- Task success rate (discover dataset → visualize → cite)
- Map performance (FPS, tile latency)
- Accessibility checks (keyboard nav, contrast)
- Mobile smoothness (touch map + Focus Mode)

### Knowledge graph 🧠
- Orphan node rate / schema drift rate / hub explosion detection
- Linker quality (precision/recall on ground truth)
- Backup verification pass rate

### 4D / Voxel / Digital Twin ⏳🧊
- Query performance at time slices
- Visual streaming performance (LOD transitions)
- Temporal correctness (time interval semantics)
- Storage growth vs resolution

---

## 🧩 Domain playbooks

<details>
<summary>🧾 Ingestion & Catalog Experiments (INGEST)</summary>

**Ground rules**
- Evidence triplet: `STAC + DCAT + PROV` for each dataset.
- Ingestion order matters: raw → normalize → derive → index/graph → publish.

**Common experiment ideas**
- “Exactly-once ingest” guards (Redis lock / run ledger)
- Bulk document ingestion with OCR + NLP entity linking to graph
- Real-time watcher prototypes (e.g., GTFS-RT) with idempotent polling + STAC Items

</details>

<details>
<summary>🧩 UI Experiments (UI)</summary>

KFM UI includes:
- 2D map viewer + 3D globe/terrain
- timeline navigation
- story nodes (markdown + JSON config)
- Focus Mode w/ citations + explainability
- offline packs + AR integration

**Story Nodes**
- Steps include `mapState`, `timelineYear`, narrative text, and optional media; the player updates view per step.

**Planned authoring**
- “Story Builder” GUI to generate Markdown/JSON from interactive edits.

</details>

<details>
<summary>🤖 AI Experiments (AI)</summary>

Focus Mode relies on the knowledge graph for context + relationship-based explanations.

**Recommended experiment patterns**
- Retrieval eval harness (golden questions → expected sources)
- “Conceptual Attention Nodes” guiding retrieval + transparency
- Citations-first UI rendering (differentiate AI text vs sourced facts)

</details>

<details>
<summary>🧠 Graph Experiments (GRAPH)</summary>

**Health checks**
- Orphans, hub detection, schema drift, backup verification; store artifacts + summary for audit.

**Schema ideas**
- Concept nodes (:Concept) for thematic pivots and AI attention routing.

</details>

<details>
<summary>🧊 4D / Voxel / Digital Twin Experiments (4D)</summary>

Innovative concept: treat Kansas as a **4D spatiotemporal digital twin** using VoxelMaps (octree + time).

**Testable hypotheses**
- “Voxel LOD + time slicing improves interactive exploration vs layer stacks”
- “AR overlays increase narrative comprehension for location-based learning”

</details>

<details>
<summary>🧭 Policy Experiments (POLICY)</summary>

Codify rules in a Policy Pack (OPA/Rego) and fail closed:
- licensing
- metadata completeness
- provenance presence
- sensitivity enforcement

</details>

---

## 🔍 Review, replication, closeout

> [!IMPORTANT]
> Every experiment should end with: **summary + conclusion + next steps** (even if it “failed”).

Closeout checklist:
- [ ] Results written in `results.md`
- [ ] Decision recorded in `decision.md` (ship / no-ship / iterate)
- [ ] Registry table updated (status + links)
- [ ] Artifacts stored + (if applicable) signed
- [ ] If affects UI/AI, add screenshots or short GIFs
- [ ] If affects data/graph, add before/after metrics and QA evidence

---

## 📚 Research library pointers

Some KFM project PDFs are **PDF portfolios** (bundles of many books/papers). Use them as your experiment method shelf:

### 📦 Portfolio files (bundles)
- `AI Concepts & more.pdf` (≈36 embedded AI/ML texts)
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf` (≈31 embedded data/DS texts)
- `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf` (≈14 embedded geospatial/3D/WebGL texts)
- `Various programming langurages & resources 1.pdf` (≈69 embedded language/tooling texts)

### 🧠 Examples of “methods you can pull from the shelf”
- Data validation & cleansing patterns (data mining texts)
- Web-based 3D GIS / Three.js pathways (geospatial cookbook)

---

## 🔗 Related MCP templates

> [!TIP]
> If you don’t have these yet, create them next. The index becomes powerful when all experiments follow the same skeleton.

Suggested template siblings:
- `mcp/templates/experiments/TEMPLATE__EXPERIMENT_PROTOCOL.md`
- `mcp/templates/experiments/TEMPLATE__EXPERIMENT_RESULTS.md`
- `mcp/templates/experiments/TEMPLATE__EXPERIMENT_DECISION.md`
- `mcp/templates/manifests/TEMPLATE__RUN_MANIFEST.json`
- `mcp/templates/manifests/TEMPLATE__EVIDENCE_MANIFEST.yaml`

---

## 🧾 Sources used to design this template

<details>
<summary>📎 Primary KFM project docs (uploaded)</summary>

- Kansas Frontier Matrix – Comprehensive UI System Overview.pdf  [oai_citation:0‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
- 📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf  [oai_citation:1‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf  [oai_citation:2‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
- Additional Project Ideas / “Document Refinement Request” concepts  [oai_citation:3‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf  [oai_citation:6‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
- 🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf  [oai_citation:7‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  
- AI Concepts & more.pdf (PDF portfolio)  
- Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf (PDF portfolio)  
- Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf (PDF portfolio)  
- Various programming langurages & resources 1.pdf (PDF portfolio)  

</details>

<details>
<summary>🧾 MCP + supporting technical references (embedded / extracted)</summary>

- Scientific Method _ Research _ Master Coder Protocol Documentation.pdf
- Kansas-Frontier-Matrix Open-Source Geospatial Historical Mapping Hub Design.pdf
- Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf

</details>
