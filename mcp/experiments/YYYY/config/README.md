# 🧪 MCP Experiments — Config (YYYY)

![MCP](https://img.shields.io/badge/MCP-Master%20Coder%20Protocol-blueviolet)
![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-orange)
![Configs](https://img.shields.io/badge/Scope-configs%20only-2ea44f)
![Provenance](https://img.shields.io/badge/Provenance-STAC%20%2B%20DCAT%20%2B%20PROV-success)
![Governance](https://img.shields.io/badge/Governance-OPA%20%2B%20Conftest-informational)
![Data](https://img.shields.io/badge/Data-append--only-critical)
![Year](https://img.shields.io/badge/Year-YYYY-lightgrey)

> [!TIP]
> Replace `YYYY` with the 4-digit year (e.g., `2026`). Year folders keep experiments chronological, reviewable, and “append-only” by default. 📆✅

---

## 🎯 What this folder is

This directory is the **source of truth for experiment configuration** in the MCP workflow.

An **experiment config** is a declarative spec that answers:

- 🧠 **What are we trying to prove?** (hypothesis + success criteria)
- 📥 **What inputs are we using?** (datasets, docs, queries, ontology fragments)
- 🧱 **What components are we touching?** (pipeline ↔️ graph ↔️ UI ↔️ Focus Mode)
- 🧾 **What governance must pass?** (license, sensitivity, policy gates)
- 📦 **What must be produced?** (run manifest, STAC/DCAT/PROV, evidence manifests, report)

> [!IMPORTANT]
> **This folder is configs only.**  
> Put run outputs (reports, logs, artifacts, screenshots) in `../runs/` (or whatever the repo standard is). Keep `config/` deterministic and review-friendly. 🧊🧾

---

## 🧭 KFM “Golden Rules” for experiments

These are the invariants we design configs around:

1. **Provenance-first** 🧾  
   Every new dataset, layer, or derived output is traceable end-to-end (inputs → transforms → outputs).

2. **Evidence-first narratives** 🔍  
   Story Nodes and AI answers should be backed by explicit evidence inventories (citations you can verify).

3. **Append-only publishing** ➕  
   Don’t silently rewrite historical facts or artifacts. Publish versioned additions.

4. **Policy-as-code gates** 🚦  
   Governance is enforced in CI (fail-closed). If policy fails, the experiment doesn’t ship.

5. **Reproducible runs** ♻️  
   Pin tool versions, record seeds, and generate a run manifest so others can reproduce results.

---

## 🗂️ Recommended layout

> [!NOTE]
> Your repo may vary — this is a “golden path” layout that plays nicely with MCP templates and KFM’s auditability goals.

```text
mcp/
└─ 🧪 experiments/
   └─ 📅 YYYY/
      ├─ ⚙️ config/                           # 👈 you are here 📌 Declared configs + templates + schemas (PR-reviewed)
      │  ├─ 📄 README.md                      # 📘 How experiment configs work, review rules, and how runs are produced
      │  ├─ 🧪 experiments/                   # “Declared” experiment configs (committed + PR-reviewed; stable IDs)
      │  │  ├─ 🧾 YYYY-001-example.yaml        # Example declared experiment (id, hypothesis, inputs, params, expected proofs)
      │  │  └─ 🧾 YYYY-002-focus-mode-rag.yaml # Declared experiment for Focus Mode/RAG evaluation (gates + metrics)
      │  ├─ 🧩 templates/                     # Copy/paste starters for new experiment declarations
      │  │  ├─ 🧩🧾 minimal.yaml               # Minimal config (enough to run + produce receipts)
      │  │  └─ 🧩🧾 full.yaml                  # Full config (datasets, metrics, evidence, publish steps)
      │  └─ 📐 schemas/                       # Validation contracts enforced by CI/gates
      │     ├─ 📐🧾 experiment.schema.json     # Schema for declared experiment configs (YAML validated against this)
      │     └─ 📐🧾 evidence-manifest.schema.json # Schema for evidence manifests produced by runs
      └─ 🏃 runs/                             # Outputs (append-only): each run is immutable once recorded
         └─ 🏷️ YYYY-001-example__RUNID/        # One run folder per execution (id + run identifier)
            ├─ 🧾 run_manifest.json            # Run ledger: who/what/when + commands + env + inputs/outputs + hashes
            ├─ 📝 report.md                    # Human report: results, metrics, limitations, and evidence links
            ├─ 📦 artifacts/                  # Produced artifacts (figures, tables, exports, logs; keep access-safe)
            └─ 🗂️ catalogs/                   # Generated STAC/DCAT/PROV for this run (or pointers to canonical catalogs)
```

---

## 🧩 Config contract (opinionated, but practical)

### ✅ Required top-level blocks

| Block | Why it exists | Typical reviewer questions |
|------|----------------|----------------------------|
| `meta` | identity + lifecycle | “Is this named well and scoped?” |
| `hypothesis` | what we’re proving | “What does success look like?” |
| `scope` | which KFM subsystems | “Does this touch UI? AI? ingestion?” |
| `inputs` | datasets + docs + queries | “Are inputs licensed and stable?” |
| `pipeline` | transforms + steps | “Deterministic? Idempotent?” |
| `provenance` | STAC/DCAT/PROV + run ledger | “Can we trace outputs?” |
| `governance` | FAIR/CARE + sensitivity | “Can this be public?” |
| `evaluation` | metrics + acceptance | “What numbers decide go/no-go?” |
| `outputs` | where artifacts land | “Where’s the report & manifest?” |
| `policy` | CI gates / constraints | “Fail-closed? Which checks?” |

---

## 🧬 Canonical fields (suggested schema)

Below is a **human-first** schema sketch (not strict JSON Schema). Treat it as the “shape” to implement.

```yaml
meta:
  id: "YYYY-001-example"
  title: "Example experiment: Story Node + Provenance panel"
  owners: ["@your-handle"]
  status: "proposed"  # proposed|active|completed|archived|promoted
  created: "YYYY-MM-DD"
  tags: ["ui", "story-nodes", "provenance", "mcp"]

hypothesis:
  statement: >
    If Story Nodes require an evidence manifest and PROV bundle,
    then user trust + auditability will improve without slowing authoring too much.
  success_criteria:
    - "100% of Story Node claims have evidence_manifest entries"
    - "PROV bundle links story -> evidence -> generation activity"
    - "No policy gate failures in CI"

scope:
  components:
    - ui.story_nodes
    - ui.provenance_panel
    - graph.prov_edges
  risk_level: "medium"   # low|medium|high
  rollout: "demo-only"   # demo-only|dev|staging|prod-candidate

inputs:
  datasets:
    - id: "kfm.ks.example.dataset.v1"
      type: "stac+geoparquet"
      license: "CC-BY-4.0"
      where: "data/processed/example/"
  documents:
    - id: "doc.example.1908.newspaper"
      where: "docs/sources/example/1908_newspaper.pdf"
  queries:
    - id: "q.max_gauge_1908"
      text: "max flood gauge height in 1908"
      expected_source: "kfm.ks.hydro.gauges.v2"

pipeline:
  mode: "dry-run" # dry-run|run|ci
  steps:
    - name: "validate-inputs"
    - name: "generate-stac"
    - name: "generate-dcat"
    - name: "generate-prov"
    - name: "graph-upsert"
  determinism:
    seed: 42
    pinned_versions: true

provenance:
  require_triplet: true           # STAC + DCAT + PROV
  log_dynamic_queries: true       # important for Focus Mode / on-demand retrieval
  run_manifest:
    enabled: true
    canonicalize_json: true       # RFC 8785 style canonicalization (recommended)
    include_tool_versions: true
    include_source_urls: true

governance:
  classification: "public"        # public|restricted|sensitive
  fair:
    findable: true
    accessible: true
    interoperable: true
    reusable: true
  care:
    collective_benefit: true
    authority_to_control: "review-required"
    responsibility: true
    ethics: "no-sensitive-sites-exposed"

evaluation:
  metrics:
    - name: "policy_gate_pass_rate"
      target: "100%"
    - name: "provenance_completeness"
      target: ">= 0.99"
    - name: "ui_story_playback_smoothness"
      target: ">= 60fps median on dev machine"
  acceptance:
    decision: "maintainer-review" # or "auto-merge" for very low-risk changes

outputs:
  run_dir: "mcp/experiments/YYYY/runs/{{id}}__{{run_id}}/"
  report: "report.md"
  run_manifest: "run_manifest.json"
  catalogs_dir: "catalogs/"
  artifacts_dir: "artifacts/"
  screenshots_dir: "artifacts/screenshots/"

policy:
  fail_closed: true
  checks:
    - "schema.validate"
    - "rego.conftest"
    - "license.present"
    - "no_secrets"
    - "provenance.triplet_present"
```

---

## 🧪 Templates you should keep in `templates/`

### 🟢 Minimal (fast to propose)
Use for quick PoCs that still respect governance:

- `meta`
- `hypothesis`
- `scope`
- `inputs` (even if tiny)
- `outputs`
- `policy` (fail-closed)

### 🟣 Full (run-ready)
Use for anything that touches ingestion, AI behavior, public UI, or release candidates:

- everything in the schema sketch
- explicit `run_manifest`
- explicit `provenance.require_triplet`
- explicit `evaluation.metrics`

---

## 🚦 Validation & CI expectations

> [!IMPORTANT]
> A config that doesn’t validate is not a config — it’s a comment. 😄  
> Treat configs like code: typed, validated, and policy-gated.

Recommended gates:

- ✅ **Schema validation** (JSON Schema / Pydantic model)
- ✅ **Policy Pack** (OPA Rego via Conftest)
- ✅ **Secrets / license checks**
- ✅ **Provenance completeness checks**
- ✅ **Idempotency / determinism checks** (seed pinned, tool versions present)

---

## 🧾 Outputs every “real” experiment should produce

### 1) 🧾 Run Manifest (`run_manifest.json`)
A single ledger file capturing:
- `run_id`, `run_time`
- `idempotency_key`
- `canonical_digest`
- `source_urls`
- `tool_versions`
- `summary_counts` (records in/out, errors)

### 2) 📦 Catalog Triplet
- 🛰️ STAC (spatiotemporal + assets)
- 🗃️ DCAT (dataset discovery metadata)
- 🔗 PROV (lineage: entities + activities + agents)

### 3) 🧷 Evidence Manifest(s)
For Story Nodes and AI-facing outputs:
- sources + stable IDs/checksums
- queries used (if applicable)
- transformations performed
- mapping from narrative claims → evidence items

> [!TIP]
> If you can’t point to the evidence manifest, the feature isn’t ready for users. ✅

---

## 🧠 Special notes for AI / Focus Mode experiments

If your config toggles AI behavior, make it explicit:

- retrieval mode (graph / catalogs / docs / hybrid)
- citation required ✅
- dynamic query logging enabled ✅
- safeguards for uncertainty (especially simulations)

Keep the AI honest:
- It can *summarize*, but it must always be able to *trace*. 🧭

---

## 🗺️ Special notes for UI experiments (2D/3D, Story Nodes, AR)

UI-facing experiment configs should declare:

- 🌍 2D/3D mode expectations (MapLibre / Cesium usage)
- 🕰️ timeline / temporal filters (what “time” means for the data)
- 🧩 layer toggles and provenance panel behavior (“map behind the map”)
- 📖 Story Node packs (Markdown + JSON config + evidence manifest)
- 📱 mobile/offline expectations (if relevant)
- 🥽 AR “scenes” as a *filtered, decluttered* subset (AR cannot show everything)

---

## 🤖 W-P-E automation hooks (optional but powerful)

If you’re using Watcher–Planner–Executor agents for upkeep:

- Watcher emits a signed event
- Planner drafts a config change (often as a PR)
- Executor runs the experiment + attaches proof (tests, manifests)

Configs should include enough metadata so W-P-E can act safely:
- owners / reviewers
- risk level
- gates to enforce
- “auto-merge allowed” only for truly low-risk changes

---

## 🧰 Experiment categories you can standardize

Use these tags in `meta.tags` for sorting and dashboards:

- `data-intake` 📥
- `pipeline` ⚙️
- `catalogs` 🛰️
- `provenance` 🧾
- `graph` 🧠
- `focus-mode` 🤖
- `story-nodes` 📖
- `ui` 🗺️
- `real-time` ⚡
- `simulations` 🧪
- `ar` 🥽
- `governance` 🚦
- `storage-oci` 📦

---

## 📚 Project reference library (useful when writing configs)

These project docs drove the conventions above (keep them close while authoring configs):

### Core KFM design 📌
- **KFM – Comprehensive Technical Documentation** (repo map, API patterns, system components)
- **KFM – Comprehensive Architecture, Features, and Design** (stack + roadmap)
- **KFM – Comprehensive UI System Overview** (2D/3D maps, Story Nodes, Focus Mode, AR)
- **KFM – AI System Overview** (Focus Mode + knowledge graph + hybrid retrieval)
- **KFM Data Intake – Technical & Design Guide** (pipeline philosophy, standards, governance)

### Innovation / roadmap boosters 🚀
- **Innovative Concepts to Evolve KFM**
- **KFM – Latest Ideas & Future Proposals**
- **Additional Project Ideas**

### Resource packs 🧠📦
> Some of these are PDF portfolios / multi-document bundles (best opened in Acrobat/Reader).

- **AI Concepts & more** (reference bundle)
- **Various programming languages & resources** (reference bundle)
- **Data Management / Theories / Architectures / Bayesian Methods** (reference bundle)
- **Maps / Google Maps / Virtual Worlds / Archaeological CG / Geospatial WebGL** (reference bundle)

---

## 🧷 MCP appendix: “Definition of Done” for configs

An experiment config is **Done ✅** when:

- [ ] It validates against `schemas/experiment.schema.json`
- [ ] It passes policy gates (fail-closed)
- [ ] It declares clear success criteria + evaluation metrics
- [ ] It produces a run manifest + catalog triplet (if it generates outputs)
- [ ] It has an associated run report in `../runs/`
- [ ] It is reviewable (no giant opaque blobs; prefer small, composable specs)

---

## 🧾 MCP appendix: Expected outputs (per experiment)

At minimum:

- 📄 Config file (`config/experiments/*.yaml`)
- 📄 Report (`runs/.../report.md`)
- 🧾 Run manifest (`runs/.../run_manifest.json`)

When the experiment affects published data/UI:

- 📦 STAC + DCAT + PROV
- 🧷 Evidence manifest(s)
- 📸 UI captures (screenshots / short clips) as artifacts

---

## 🛟 If you’re unsure, do this first

1) Copy `templates/minimal.yaml` → `experiments/YYYY-###-your-slug.yaml`  
2) Fill in `meta`, `hypothesis`, `inputs`, `policy`  
3) Run local validation ✅  
4) Open PR early and iterate in public 👀

Because in KFM, **review is a feature** — it’s part of provenance. 🧾✨
