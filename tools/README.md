<!--
📌 tools/ is the repo’s *governed toolchain surface* for building + validating KFM artifacts.
🗓️ Last updated: 2026-01-26
🔁 Review cycle: 90 days (or anytime pipeline order / catalogs / policy changes)
🧭 Alignment: Master Guide v13 (contract-first + evidence-first + one canonical home per subsystem)
🧪 Scientific posture: Verification + Validation + Uncertainty Quantification (V&V&UQ) for anything “model-y”
🧾 Provenance posture: STAC + DCAT + PROV are the canonical publish boundary
🔐 Security posture: deny-by-default network, hostile-input assumptions, and Prompt Gate for AI/tooling
🔎 Retrieval posture: keyword + vector (embeddings) where justified; retrieval results must remain citeable
-->

<div align="center">

# 🛠️ `tools/` — Kansas Frontier Matrix (KFM) Toolchain

**Deterministic • Provenance-aware • CI-friendly**  
**Build it once • verify it forever • ship with a paper trail** 🧾✅

<!-- Core runtime badges -->
![Python](https://img.shields.io/badge/Python-3.11%2B-informational)
![Node](https://img.shields.io/badge/Node-18%2B-informational)
![Docker](https://img.shields.io/badge/Docker-optional%20%28dev%2FCI%29-informational)
![License](https://img.shields.io/badge/license-MIT-success)

<!-- Governance / assurance badges -->
![Contract-first](https://img.shields.io/badge/contract--first-schemas%20%2B%20API-blue)
![Evidence-first](https://img.shields.io/badge/evidence--first-catalogs%20%2B%20PROV-blueviolet)
![Provenance-first](https://img.shields.io/badge/provenance--first-no%20publish%20without%20PROV-red)
![Catalog-first](https://img.shields.io/badge/catalog--first-STAC%20%7C%20DCAT%20%7C%20PROV-blue)
![Policy-as-code](https://img.shields.io/badge/policy--as--code-OPA%20%2F%20Conftest-ff7a00)
![SBOM](https://img.shields.io/badge/SBOM-SPDX%20%7C%20CycloneDX-2ea043)
![SLSA-ish](https://img.shields.io/badge/SLSA-ish-attestations-8b5cf6)

<!-- Geo / UI delivery badges -->
![GeoParquet](https://img.shields.io/badge/GeoParquet-analytics-2ea043)
![COG](https://img.shields.io/badge/COG-rasters-1f6feb)
![PMTiles](https://img.shields.io/badge/PMTiles-vector%20tiles-8250df)
![STAC](https://img.shields.io/badge/STAC-catalogs-1f6feb)
![DCAT](https://img.shields.io/badge/DCAT-discovery-8250df)
![PROV](https://img.shields.io/badge/PROV-lineage-8250df)

<!-- Storage / distribution badges -->
![OCI](https://img.shields.io/badge/OCI-artifact%20registry-8b5cf6)
![ORAS](https://img.shields.io/badge/ORAS-transfer-8b5cf6)
![Cosign](https://img.shields.io/badge/Cosign-signing-8b5cf6)

<!-- Infra badges -->
![FastAPI](https://img.shields.io/badge/FastAPI-API%20layer-009688)
![GraphQL](https://img.shields.io/badge/GraphQL-contracts%20%2B%20queries-e10098)
![Search](https://img.shields.io/badge/Search-Elasticsearch%20%7C%20OpenSearch%20%7C%20Whoosh-informational)
![Neo4j](https://img.shields.io/badge/Neo4j-graph-00ba7c)
![PostGIS](https://img.shields.io/badge/PostGIS-spatial%20DB-2d6cdf)
![MapLibre](https://img.shields.io/badge/MapLibre-2D%20maps-1f6feb)
![Cesium](https://img.shields.io/badge/Cesium-optional%203D-6f42c1)
![Ollama](https://img.shields.io/badge/Ollama-local%20LLM%20runtime%20%28optional%29-2ea043)

</div>

> **TL;DR:** `tools/` is the **governed command surface** that builds, validates, packages, and publishes KFM artifacts **without bypassing governance**.  
> It is intentionally **not** “business logic” and it is intentionally **not** “a scripts junk drawer.”  
> If it touches `data/processed/` (or produces any publish-looking output), it must also produce catalogs + provenance 🧾🧬.

> [!IMPORTANT]
> **MCP** = **Master Coder Protocol** *(implemented as “Methods & Computational Experiments” in `mcp/`)* 🧪🧾  
> Tools must support MCP by producing **re-run-able outputs**, **linkable provenance**, and **reviewable diffs** — without becoming domain/business logic.

---

<details>
<summary><b>🧭 Table of contents</b></summary>

- [🧠 Quick links](#quick-links)
- [🧭 Repo invariants](#repo-invariants)
- [🧱 Non-negotiable pipeline order](#non-negotiable-pipeline-order)
- [🎯 What belongs in tools](#what-belongs-in-tools)
- [🧭 Boundaries: tools vs scripts vs src vs mcp](#boundaries-tools-vs-scripts-vs-src-vs-mcp)
- [🗂️ Tool registry & manifests](#tool-registry--manifests)
- [🧾 Contracts & schemas](#contracts--schemas)
- [🧾 Run manifests & JSON canonicalization](#run-manifests--json-canonicalization)
- [🎲 Determinism & reproducibility levels](#determinism--reproducibility-levels)
- [🧪 Artifact QA matrix](#artifact-qa-matrix)
- [✅ Validation rings (QA gates)](#validation-rings-qa-gates)
- [🤖 Agent toolchain: Watcher–Planner–Executor](#agent-toolchain-watcherplannerexecutor)
- [🧠 LLM runtime & Prompt Gate utilities](#llm-runtime--prompt-gate-utilities)
- [📦 Data staging + catalog locations](#data-staging--catalog-locations)
- [🧩 Dual-format geo packaging: GeoParquet + PMTiles](#dual-format-geo-packaging-geoparquet--pmtiles)
- [📦 OCI artifact registry distribution](#oci-artifact-registry-distribution)
- [📦 Offline packs & field ops](#offline-packs--field-ops)
- [🧵 Story Nodes, Pulse Threads, Concept Nodes](#story-nodes-pulse-threads-concept-nodes)
- [🗺️ Geo & mapping utilities](#geo--mapping-utilities)
- [🛰️ Remote sensing utilities](#remote-sensing-utilities)
- [🧊 Imaging & compression utilities](#imaging--compression-utilities)
- [🧱 3D / WebGL / scene utilities](#3d--webgl--scene-utilities)
- [🩺 Graph health checks](#graph-health-checks)
- [🧠 Graph & DB utilities](#graph--db-utilities)
- [🔎 Search & retrieval utilities](#search--retrieval-utilities)
- [📊 Statistical evidence utilities](#statistical-evidence-utilities)
- [🧪 Modeling/ML/simulation utilities](#modelingmlsimulation-utilities)
- [🔐 Security posture](#security-posture)
- [📡 Telemetry & observability](#telemetry--observability)
- [⚡ Performance & scaling notes](#performance--scaling-notes)
- [🌍 Federation & cross-matrix interoperability](#federation--cross-matrix-interoperability)
- [🧩 Contributing a new tool](#contributing-a-new-tool)
- [📚 Project reference library](#project-reference-library)
- [🧾 Metadata](#metadata)
- [🕰️ Version history](#version-history)

</details>

---

<a id="quick-links"></a>
## 🧠 Quick links

- 📘 **Master Guide v13 (repo contract)** → `docs/MASTER_GUIDE_v13.md` *(or mirror)*[^kfm_v13]
- 🧾 **Markdown + folder protocol (v13)** → `MARKDOWN_GUIDE_v13.md.gdoc` *(canonical layout + patterns)*[^markdown_v13]
- 🧱 **Docs templates (PR-ready)** → `docs/templates/` *(one-page subsystem docs, runbooks, checklists)*[^markdown_v13]
- 📏 **Schemas & contracts (source of truth)** → `schemas/`
- 🧪 **MCP receipts / lab notebook** → `mcp/README.md`[^mcp_receipts]
- 🧪 **Canonical pipelines** → `src/pipelines/`
- 🕸️ **Graph build & ontology bindings** → `src/graph/`
- 🔎 **Indexing & doc library** → `docs/library/` + `tools/library/` + `tools/search/`[^tech_doc]
- 🛡️ **API boundary** → `src/server/` *(UI does not query DB/graph directly)*[^kfm_v13]
- 🌐 **UI** (React · MapLibre · optional Cesium) → `web/`[^ui_arch]
- 🗂️ **Data lifecycle** → `data/README.md` *(staging rules + catalogs)*[^data_layout]
- 🛡️ **Policy pack** (OPA/Conftest) → `tools/validation/policy/*.rego`[^policy_pack]
- 🔏 **Releases** (bundles, SBOMs, attestations) → `releases/`
- 🧾 **Citation metadata** → `CITATION.cff`
- ✅ **Tests** → `tests/README.md`

---

<a id="repo-invariants"></a>
## 🧭 Repo invariants

> [!IMPORTANT]
> These are **guardrails**, not preferences. If a tool would violate these, redesign the tool.

### ✅ One canonical home per subsystem 🧱
No mystery duplicates.

- pipelines → `src/pipelines/`
- graph → `src/graph/`
- API boundary → `src/server/`
- UI → `web/`
- schemas → `schemas/`
- reference docs + “why” → `docs/` + `docs/library/`[^tech_doc]
- governed narratives → `docs/reports/story_nodes/`[^story_nodes]

### ✅ Contract-first 📏
Schemas and API contracts are first-class artifacts:
- implementations must conform
- changes require versioning + compatibility checks
- tools validate against contracts **by default** (not “optional if you remember”)  
- templates exist for consistency (`docs/templates/`) 🧩[^markdown_v13]

### ✅ Evidence-first + provenance-first 🧾🧬
No “published-looking output” without boundary artifacts:
- **STAC + DCAT + PROV** required **before**:
  - graph ingest
  - API exposure
  - UI consumption / Story Node linking[^stac_dcat_prov]
- **Raw data is immutable**; “work” is ephemeral; “processed” is governed evidence.[^immutability]

### ✅ Deterministic by default 🎲🚫
Given the same inputs + config + seed, tools must produce the same outputs (**ordering included**).

### ✅ Focus Mode is advisory-only, citation-required 🧠🧾
- Focus Mode must cite evidence; **no uncited assertions**.[^focus_mode]
- If citations can’t be produced, Focus Mode refuses or clearly returns “insufficient evidence.”
- Focus Mode never takes autonomous actions (it proposes; humans approve).[^focus_mode]

### ✅ Human-centered + sovereignty-aware 🌾🧑‍🤝‍🧑
Tools shape decision artifacts:
- respect consent, agency, and auditability
- treat sensitivity/classification as **data**, enforced by gates[^sensitivity]
- prefer least privilege, least surprise

---

<a id="non-negotiable-pipeline-order"></a>
## 🧱 Non-negotiable pipeline order

> [!IMPORTANT]
> This ordering is not “architecture style.” It’s a **governance boundary**.[^kfm_v13]

**Raw → Work/ETL → Processed → Catalogs (STAC/DCAT/PROV + QA) → Stores/Indexes/Graph → APIs → UI → Story Nodes → Focus Mode**

```mermaid
flowchart LR
  A["📥 Raw (immutable)<br/>data/raw/&lt;domain&gt;/"] --> B["🧪 Work / ETL (scratch)<br/>data/work/&lt;domain&gt;/"]
  B --> C["📦 Processed (publishable artifacts)<br/>data/processed/&lt;domain&gt;/"]
  C --> D["🗂️ Catalog boundary artifacts<br/>data/stac + data/catalog/dcat + data/prov<br/>+ QA gates"]
  D --> E["🗄️ Stores + indexes<br/>PostGIS + Search + Vector (optional)<br/>(built from catalogs)"]
  E --> F["🕸️ Graph ingest<br/>(Neo4j; references catalogs + store IDs)"]
  F --> G["🛡️ APIs<br/>(contracts + redaction + policy)"]
  G --> H["🌐 UI<br/>(React · MapLibre · optional Cesium)"]
  H --> I["📚 Story Nodes<br/>(governed narratives)"]
  I --> J["🎯 Focus Mode<br/>(evidence-linked context)"]
```

**Practical implication:** `tools/` must never provide “shortcuts” that skip catalogs + provenance.

---

<a id="what-belongs-in-tools"></a>
## 🎯 What belongs in tools

`tools/` is for **reusable, CI-friendly tooling** that builds/validates artifacts in the governed pipeline.

✅ Good fits:
- Catalog builders + validators (STAC/DCAT/PROV; required fields; link checks)
- Deterministic ID/hashing utilities (stable IDs, checksums, manifests)
- Format integrity tooling (COG validation, GeoParquet schema checks, geometry validity)
- Policy enforcement tooling (OPA/Conftest; “no publish without provenance,” “no downgrade,” “AI must cite”) [^policy_pack]
- Graph/DB loaders that **ingest from catalogs** (no ad-hoc inserts)
- Search index builders (keyword index + optional embedding/vector retrieval) that keep outputs citeable[^tech_doc]
- Release packaging (SBOM, signatures, attestations)[^slsa_attest]
- CI entrypoints (non-interactive, stable exit codes)
- Scientific integrity harnesses (V&V + UQ smoke checks, regression tests)[^mcp_receipts]
- Agent wrappers that operate via reviewable artifacts (Watcher/Planner/Executor that opens PRs and emits receipts)[^wpe]
- Document/PDF ingestion + manifests for indexing/search (governed library tooling)[^pdf_portfolios]
- Story Node / storyboard validators (citation ↔ manifest consistency checks)[^story_nodes]
- Offline pack builders (signed manifest; scoped catalogs; policy labels)[^offline_packs]

🚫 Not a fit:
- Long-lived services (APIs, daemons) → runtime/app folders
- Core domain/business logic → `src/` (importable, testable)
- One-off scripts that bypass provenance and approvals → keep in sandbox until promoted
- Anything that can’t run non-interactively (or can’t be made CI-safe)

---

<a id="boundaries-tools-vs-scripts-vs-src-vs-mcp"></a>
## 🧭 Boundaries: tools vs scripts vs src vs mcp

### `src/` = canonical behavior (the engine) 🏗️
ETL jobs, graph build, API logic, reusable libraries.

### `tools/` = governed toolchain (the verified command surface) 🛠️
Thin entrypoints that call `src/`, run validators, emit provenance, and produce release-quality artifacts.

### `scripts/` = convenience orchestration (the buttons/levers) 🧰
Local ops + developer helpers + environment glue. Preferred pattern: **scripts call tools**, tools call src.

### `mcp/` = receipts & scientific record (the lab notebook) 🧪🧾
Run receipts, experiment logs, model cards, governance checklists.[^mcp_receipts]

> [!TIP]
> If you’re implementing core behavior inside `tools/`, that’s a smell.  
> Put the logic in `src/` and keep `tools/` as predictable CLI + validator layer.

---

<a id="tool-registry--manifests"></a>
## 🗂️ Tool registry & manifests

To keep `tools/` governable at scale, treat tools like **declared assets**, not “whatever is in a folder.”

### ✅ Recommended: one manifest per tool
Store under `tools/manifests/<tool>.yaml` (or `.json`) so CI can:
- list the governed tool surface (what exists)
- validate defaults (dry-run, network posture, output locations)
- generate docs (help text, examples) automatically
- enforce “deny-by-default network” and “policy pack pinned” defaults[^policy_pack]

Example (minimum viable):

```yaml
name: "catalog_qa"
entrypoint: "tools/validation/catalog_qa/run_catalog_qa.py"
owner: "@kfm-engineering"
inputs:
  - "data/stac/**"
  - "data/catalog/dcat/**"
  - "data/prov/**"
outputs:
  - "reports/catalog_qa/**"
modes:
  dry_run: true
  apply: false
network:
  default: "deny"
determinism:
  stable_sorting: true
  seeded: false
policy:
  opa_bundle: "tools/validation/policy/"
  record_policy_hash: true
gates:
  - "schema_valid"
  - "required_fields"
  - "href_integrity"
  - "license_required"
  - "prov_required_for_publish"
```

> [!NOTE]
> A manifest is not a replacement for docs — it’s the **machine-checkable** view of governance.

---

<a id="contracts--schemas"></a>
## 🧾 Contracts & schemas

> [!IMPORTANT]
> **Schemas live at repo root:** `schemas/` is the canonical source of truth.  
> Tools must validate against contracts by default.

### ✅ Contract artifact types
- JSON Schema (STAC/DCAT/PROV, Story Nodes, telemetry, offline pack manifests)
- API boundary contracts (OpenAPI, GraphQL SDL)
- Tool manifests (the governed command surface)
- Dataset metadata contracts (schema, units, CRS, license, sensitivity tags)

### ✅ Story Nodes are governed “machine-ingestible” narratives
A valid Story Node must:
- include provenance/citations for claims
- reference graph entities via stable IDs
- distinguish fact vs interpretation/inference[^story_nodes]

---

<a id="run-manifests--json-canonicalization"></a>
## 🧾 Run manifests & JSON canonicalization

Run manifests solve a boring-but-critical problem: **stable identity for “a run.”**

### ✅ Required for publish-like outputs
If a tool produces evidence (or promotes to `processed/`), it should emit:
- `run_context.json` *(human-readable receipt)*
- `run_manifest.json` *(machine-precise inventory + hashes)*[^run_manifest]

**Recommended fields** (because they matter later 🧠🧾):
- tool version + git commit
- schema pack version
- policy pack hash (OPA bundle hash)
- container image digest (if used)
- model + embedding model identifier (if used)
- seeds + determinism flags

### ✅ Canonicalization rule
Canonicalize JSON before hashing (e.g., RFC 8785/JCS style):
- stable key ordering
- stable number serialization
- whitespace ignored
- stable arrays where order should not matter[^run_manifest]

> [!TIP]
> This does not replace PROV — it makes PROV more usable by giving each run a stable, content-derived identity.

---

<a id="determinism--reproducibility-levels"></a>
## 🎲 Determinism & reproducibility levels

Not everything needs hermetic builds — but everything needs auditability.

| Level | Name | Promise | Typical use |
|---:|---|---|---|
| R0 | Deterministic | Same inputs+config+seed ⇒ same outputs | most tools |
| R1 | Provenance-complete | R0 + complete PROV + catalog pointers | publishable evidence |
| R1.5 | Idempotent-run | R1 + canonical `run_manifest.json` hash | ingestion/promotion tooling |
| R2 | Rebuildable | R1 + pinned deps + env captured | critical releases |
| R3 | Hermetic | R2 + no network + fully captured env | highest assurance |

> [!TIP]
> If you don’t know which level you need, default to **R1** for anything that touches `processed/`.

---

<a id="artifact-qa-matrix"></a>
## 🧪 Artifact QA matrix

Use this matrix to decide which validators must run **before promotion** ✅

| Artifact type | Minimum checks | Extra checks (recommended) |
|---|---|---|
| 📄 JSON/JSON-LD (STAC/DCAT/PROV) | schema + required fields + link resolution | URI normalization + SPDX license lint |
| 🧾 Run manifests | schema + canonicalization + hash recompute | inventory ↔ filesystem cross-check |
| 🧭 Vector (GeoParquet/GeoJSON/FlatGeobuf) | schema + CRS + geometry validity | topology rules + simplification policy |
| 🧱 PMTiles | header validity + metadata present + bounds/zoom sanity | layer budgets + attribution propagation |
| 🛰️ Raster (COG/GeoTIFF/NetCDF) | COG layout + CRS + bounds + nodata | overview completeness + tiling alignment |
| 🗄️ Tabular (Parquet/CSV) | schema + types + missingness report | drift checks + range checks |
| 🔎 Search index snapshots | manifest + docID↔source links | analyzer/version pinning + redaction lint |
| 🧠 Embedding stores | model ID captured + dataset refs | vector drift checks + retrieval QA |
| 📦 Offline packs | manifest schema + checksums + policy tags | signature verify + “no orphan assets” scan |
| 📚 Story Nodes | schema + citations present + evidence refs resolvable | citation ↔ manifest consistency checks |
| 🧠 ML artifacts | metrics schema + dataset refs + seeds | calibration + fairness slices + uncertainty |
| 🧮 Simulation outputs | config+seed captured + deterministic rerun | V&V smoke tests + UQ summary |
| 📦 OCI artifacts | digest pinned + signature verified | referrer integrity + SBOM present |

---

<a id="validation-rings-qa-gates"></a>
## ✅ Validation rings (QA gates)

Think in rings (each ring blocks promotion if it fails):

### Ring 0: Structure 🧱
- JSON parses
- schema validation (STAC/DCAT/PROV + extensions)
- required files exist

### Ring 1: Integrity 🔗
- checksums/manifest inventory
- deterministic IDs present
- run manifest hash recompute + match
- atomic publish (no half-state)

### Ring 2: Semantics 🧠
- CRS correctness + axis order
- geometry validity (and any allowed repair policy)
- raster sanity (nodata, resolution, alignment)
- time/bounds sanity (Kansas bounds + plausible ranges)

### Ring 3: Statistical & scientific sanity 🧪📊
- drift checks
- residual diagnostics where applicable
- uncertainty summaries (where applicable)
- “smell tests” for simulation invariants

### Ring 4: Governance & safety 🔐
- license required before publish
- classification propagation (no downgrade)
- sensitive field redaction rules (including location generalization)[^sensitivity]
- policy tests (OPA/Conftest)
- secrets scans + dependency hygiene
- audit log includes **policy version hash** for decisions[^focus_mode]

### Ring 5: AI integrity 🧠🧾
- Focus Mode: no uncited assertions; refuse if no evidence
- Prompt Gate: prompt-injection defense + tool execution constraints[^prompt_gate]
- “No hallucinated names” rule: people referenced must exist in graph (policy-checked)[^focus_mode]
- Speculation must be labeled with hedging language (policy-checked)[^focus_mode]

---

<a id="agent-toolchain-watcherplannerexecutor"></a>
## 🤖 Agent toolchain: Watcher–Planner–Executor

KFM supports agent-assisted workflows — only when they behave like governed tools:
**deterministic, reviewable, provenance-emitting, PR-based**.[^wpe]

```mermaid
flowchart LR
  W["🛰️ Watcher<br/>detect change"] --> P["🧭 Planner<br/>produce plan.json"]
  P --> E["🧾 Executor<br/>run plan + emit receipts"]
  E --> PR["🔀 PR / Patch<br/>human review + gates"]
  PR --> M["✅ Merge/Publish<br/>catalogs+prov+attest"]
```

### 🛰️ Watcher (detect change → propose)
- scans a defined surface (drop folder, feeds, updated catalogs)
- uses **content-aware fetch** where applicable (ETag / If-Modified-Since) to avoid redundant downloads[^roadmap]
- emits immutable event artifacts:
  - `event.json` (what changed)
  - `inputs.json` (candidate inputs)
  - `fetch_receipt.json` (headers/status/checksums when network is allowed)[^roadmap]
- default: **no network** unless `--allow-network`

### 🧭 Planner (propose plan → deterministic + diffable)
- turns events into a deterministic plan:
  - exact tool invocations
  - expected inputs/outputs
  - policy gates to run
  - rollback behavior
- can propose schema evolution safely (e.g., generate migration SQL in PR)[^schema_drift]

### 🧾 Executor (apply plan → PR-based + attested)
- executes in controlled environment
- guarantees **idempotency** (re-running a plan yields the same results) and supports a **kill switch**[^wpe]
- produces:
  - artifacts + updated STAC/DCAT/PROV
  - structured reports
  - MCP run receipt
  - SBOM + signature/attestation for publish-like artifacts (SLSA-ish)[^slsa_attest]
- opens PR (or produces a patch) rather than mutating protected branches

> [!IMPORTANT]
> Automation is not a bypass — it is a more disciplined contributor.

---

<a id="llm-runtime--prompt-gate-utilities"></a>
## 🧠 LLM runtime & Prompt Gate utilities

KFM’s AI system is designed to be:
- **local-first (optional)** (e.g., Ollama) for sovereignty/offline resilience[^ollama_infra]
- **advisory-only** (never autonomous)
- **evidence-backed** (citations required, enforceable by policy)[^focus_mode]

### 🔌 Runtime posture (Ollama is a common default)
Tooling in `tools/ai/` should support:
- model inventory + pinning (name/tag/digest)
- embedding model pinning for vector retrieval
- offline/test mode (CI-friendly: smaller models, deterministic prompts)[^ollama_infra]
- “model card” / runtime manifest outputs into MCP (`mcp/model_cards/`)

### 🧱 Prompt Gate posture (defense-in-depth)
Prompt Gate is a *policy-controlled boundary* that:
- sanitizes hostile instructions (prompt injection patterns)
- enforces allow/deny lists for tool calls
- blocks unsafe or policy-violating requests before they touch models
- post-checks outputs for required structure (e.g., citations present)[^prompt_gate]

**Policy engineering expectation:**
- rules are versioned in Git
- audit logs record policy hash + decision outcomes for later review[^focus_mode]

### 🧪 Focus Mode pipeline (implementation hint)
A typical Focus Mode request is a **retrieval + governance + synthesis** workflow:
1) retrieve evidence (search index + graph + PostGIS)
2) apply governance policy checks (OPA)
3) synthesize answer with citations
4) output + evidence bundle (for UI “inspectability”)[^focus_mode]

> [!TIP]
> Treat AI outputs like any other “model-y” artifact: capture config/seed, link datasets, and emit receipts.

---

<a id="data-staging--catalog-locations"></a>
## 📦 Data staging + catalog locations

KFM data work is staged and traceable, with **one canonical home per dataset**.[^data_layout]

```text
data/
├── sources/                     # retrieval manifests + checksums + licenses (recommended)
├── raw/
│   └── <domain>/                # immutable as-received data
├── work/
│   └── <domain>/                # intermediates / scratch (rebuildable)
├── processed/
│   └── <domain>/                # publishable evidence artifacts
├── stac/
│   ├── collections/
│   └── items/
├── catalog/
│   └── dcat/                    # DCAT JSON-LD datasets/distributions
└── prov/                        # PROV bundles (JSON-LD recommended)
```

> [!IMPORTANT]
> `raw/` is never edited; `work/` is ephemeral; `processed/` is governed evidence.[^immutability]

> [!TIP]
> Each new domain should also ship a **runbook** (one-page) under `docs/data/<domain>.md` using `docs/templates/`.[^markdown_v13]

---

<a id="dual-format-geo-packaging-geoparquet--pmtiles"></a>
## 🧩 Dual-format geo packaging: GeoParquet + PMTiles

KFM supports dual-purpose geospatial outputs:
- **GeoParquet** → analytics & bulk query
- **PMTiles** → fast web delivery & offline packs (single-file archive)[^pmtiles_dual_pack]

Toolchain implications:
- deterministic build of both outputs from the same processed dataset
- catalogs link both distributions (STAC assets + DCAT distributions)
- provenance records tile-build parameters (zoom range, simplification, tiler version)[^pmtiles_dual_pack]

> [!TIP]
> Treat GeoParquet + PMTiles as a *pair*: analysis runs on GeoParquet; UI serves PMTiles; both point back to one evidence root.

---

<a id="oci-artifact-registry-distribution"></a>
## 📦 OCI artifact registry distribution

For large artifacts (PMTiles, GeoParquet, COGs, model bundles), KFM can leverage **OCI registries** as storage/distribution:
- push arbitrary artifacts with **ORAS**
- sign/verify with **Cosign** (Sigstore patterns)
- attach SBOMs/attestations as OCI referrers
- reference artifacts by immutable **digest** inside STAC/DCAT/PROV[^oci_registry]

> [!IMPORTANT]
> OCI is a distribution channel — not a governance bypass.  
> Catalogs + PROV remain the canonical boundary, and policy gates still apply.

---

<a id="offline-packs--field-ops"></a>
## 📦 Offline packs & field ops

KFM supports offline-first usage (field researchers, educators, rural connectivity). Offline packs are still publish-like artifacts.[^offline_packs]

### ✅ Offline pack should include
- pre-rendered tiles (PMTiles/MBTiles) for a defined AOI
- slimmed catalogs (STAC/DCAT/PROV) scoped to the pack
- signed manifest (checksums + versions + policy tags)
- credits bundle (attribution + licensing)
- optional: **mini web app shell** for offline browsing (so it’s usable in classrooms/kiosks) 📦🌾[^offline_packs]
- optional: AR/field overlays only when policy allows (future-facing roadmap) 🛰️🧭[^roadmap]

### ✅ Governance requirement
Offline packs must pass QA rings and carry policy labels (classification, sensitivity).

---

<a id="story-nodes-pulse-threads-concept-nodes"></a>
## 🧵 Story Nodes, Pulse Threads, Concept Nodes

These are governed content artifacts that connect datasets to narratives and AI context.

### 📚 Story Nodes (governed narratives)
Story Nodes are markdown + structured metadata:
- citations required
- link to datasets via catalog IDs
- link entities via stable graph IDs
- distinguish fact vs interpretation/inference[^story_nodes]

**UI authoring model:** Story Nodes are content + behavior:
- **Markdown** = narrative content (text, media, citations)
- **JSON storyboard** = map/timeline “slides” (declarative UI state)[^ui_arch]

Example storyboard pattern (conceptual):

```json
{
  "title": "Dust Bowl Story",
  "slides": [
    { "section": "Black Sunday (1935-04-14)",
      "mapState": { "center": [-100.0, 38.5], "zoom": 6, "layers": ["dust_storms_1935"], "time": "1935-04-14" }
    }
  ]
}
```

**Tooling** in `tools/content/` should:
- validate Story Node schema + citation integrity
- validate storyboard JSON schema (and reference integrity)
- emit provenance of story construction (what sources were used)

### 🧵 Pulse Threads (recurring evidence-linked updates)
- lightweight “what’s new + why it matters”
- cadence + scope + evidence refs in metadata
- “no unsourced assertions” lint

### 🧠 Concept Nodes (concept-as-entity anchors)
- shared concept IDs + aliases + policy tags
- bind datasets + story nodes to stable anchors
- safe for Focus Mode to cite as governed context (with provenance pointers)

---

<a id="geo--mapping-utilities"></a>
## 🗺️ Geo & mapping utilities

### CRS & units are non-negotiable 📐
- refuse unknown CRS by default
- log CRS for inputs and outputs
- record reprojections in provenance

KFM standard is **WGS84 (EPSG:4326)** for web consistency.[^crs_wgs84]

> [!TIP]
> Prefer wrappers around mature tools (GDAL/PROJ), with stable args + captured versions.  
> Pipelines commonly rely on GDAL/GeoPandas/Shapely/Rasterio for deterministic transforms and QC.[^roadmap]

### Tile serving strategies (both valid) 🧱
- PostGIS tile endpoints (e.g., `ST_AsMVT`) for dynamic serving
- Prepackaged tiles (PMTiles/MBTiles) for static hosting + offline packs

---

<a id="remote-sensing-utilities"></a>
## 🛰️ Remote sensing utilities

Remote sensing tooling should prefer **derived products + provenance** over raw archive dumps:
- record AOI + time window
- record compositing + masking logic
- export as COGs (and/or cloud-optimized NetCDF where relevant)
- emit STAC Items per logical unit

---

<a id="imaging--compression-utilities"></a>
## 🧊 Imaging & compression utilities

Images are evidence too — compression choices can change meaning 🧾
- detect bit depth / alpha / nodata semantics
- warn on lossy conversions for scientific rasters
- emit a small report with chosen params + rationale

---

<a id="3d--webgl--scene-utilities"></a>
## 🧱 3D / WebGL / scene utilities

When we ship 3D, we ship **performance budgets + provenance** 🧊⚡
- validate glTF / 3D Tiles manifests
- generate/verify LOD pyramids
- embed attribution + license + provenance pointers
- check GPU budgets (triangles, textures) for target devices

---

<a id="graph-health-checks"></a>
## 🩺 Graph health checks

Recommended recurring integrity practice:
- orphan scan (nodes/edges)
- constraint checks
- drift summary
- publish health report + suggested fixes (PR plan), not silent mutations

---

<a id="graph--db-utilities"></a>
## 🧠 Graph & DB utilities

### Neo4j ingest 🕸️
Graph ingest must be downstream of catalogs:
- reference STAC/DCAT/PROV (don’t duplicate bulky data)
- enforce invariants: “every dataset links to provenance,” “no orphan entities”
- align with standard ontologies where applicable (CIDOC-CRM, OWL-Time) to support interoperability[^arch_design]

### PostGIS helpers 🗄️
- staging tables + transactional swaps (load → validate → swap)
- stable query shapes + stable sort orders (determinism)
- treat query plans as artifacts for critical pipelines

---

<a id="search--retrieval-utilities"></a>
## 🔎 Search & retrieval utilities

KFM uses search as **evidence retrieval**, not “mystery magic.” Search outputs must stay citeable.

### 🔍 Keyword index (Elasticsearch/OpenSearch/Whoosh)
Tooling should:
- index Story Nodes + doc library extractions + OCR text with stable doc IDs
- propagate sensitivity labels into index fields
- return results with **source pointers** (document ID + location) so UI/AI can cite[^tech_doc]

### 🧠 Vector retrieval (embeddings)
If semantic retrieval is enabled:
- embeddings must record: model ID, chunking strategy, normalization, and versioned parameters[^ollama_infra]
- retrieval must return citeable evidence spans (docID + offsets/page refs)
- index snapshots should be exportable for offline packs (scoped to AOI/topic)

> [!IMPORTANT]
> If retrieval can’t produce citeable evidence, Focus Mode should refuse rather than hallucinate.[^focus_mode]

---

<a id="statistical-evidence-utilities"></a>
## 📊 Statistical evidence utilities

Statistics is evidence engineering, not “extra math” 📈🧾
- effect sizes + uncertainty (CIs/credible intervals), not just p-values
- drift checks and residual diagnostics
- declared priors (Bayesian tools) + sensitivity summaries
- log multiple comparisons and guard against p-hacking

> [!TIP]
> For privacy-preserving release and inference control, reference k-anonymity/l-diversity/t-closeness, query auditing, and differential privacy techniques.[^privacy_inference]

---

<a id="modelingmlsimulation-utilities"></a>
## 🧪 Modeling/ML/simulation utilities

Modeling tools must behave like scientific instruments 🧪🔬:
- capture params + seeds
- record dataset IDs (catalog pointers)
- emit evaluation artifacts (metrics + plots where relevant)
- write MCP receipts when results influence decisions
- include V&V + UQ summaries for simulation outputs

---

<a id="security-posture"></a>
## 🔐 Security posture

Treat `tools/` as part of the threat model:
- inputs are hostile (archives, rasters, PDFs, GeoJSON, model files)
- allowlist file types; enforce size + decompression limits (zip bombs)
- sanitize paths; refuse traversal
- SSRF defenses for network fetchers
- never print secrets; never require secrets in CLI args

### 🧠 Prompt Gate (AI + tool safety)
For AI-assisted workflows:
- policy rules are centrally defined and versioned
- outputs are scanned for required citations (“no uncited assertions”)
- tool execution is sandboxed / least privilege
- unsafe requests are blocked by allow/deny lists[^prompt_gate]

### 🔒 Privacy & inference control (defense-in-depth)
When datasets include sensitive fields or exact locations:
- enforce redaction + generalization policies
- apply privacy-aware release techniques where applicable:
  - k-anonymity / l-diversity / t-closeness
  - perturbation methods
  - query auditing / inference control[^privacy_inference]

> [!IMPORTANT]
> Security references in the library are for defensive posture only.  
> Tools must never provide offense automation.

---

<a id="telemetry--observability"></a>
## 📡 Telemetry & observability

Telemetry is a **contracted surface** (schema-first):
- event schemas live under `schemas/telemetry/`
- tools validate telemetry payloads in CI
- logs should be JSONL + a minimal human-readable summary

**Strongly recommended fields**:
- tool version + git commit
- dataset IDs (catalog pointers)
- policy hash (OPA bundle hash) for decisions
- model IDs (if AI invoked)

---

<a id="performance--scaling-notes"></a>
## ⚡ Performance & scaling notes

When tools grow:
- chunk work for parallelism (tiles/partitions)
- introduce explicit materialization boundaries
- keep caches provenance-aware
- profile first, then optimize

> Speed is good — but correctness and provenance come first.

---

<a id="federation--cross-matrix-interoperability"></a>
## 🌍 Federation & cross-matrix interoperability

KFM is federation-ready:
- export/import at the **catalog boundary** (STAC/DCAT/PROV)
- shared contracts enable cross-region audits and discovery
- OCI registries enable artifact reuse across regions (digest pinned; signed)[^oci_registry]

Ideas that fit naturally in `tools/`:
- `tools/catalogs/export_bundle.py` → export catalogs + checksums
- `tools/catalogs/import_bundle.py` → validate + ingest external catalogs (deny-by-default)
- `tools/contracts/package_schemas.py` → publish versioned schema pack

> [!NOTE]
> Federation strengthens governance: shared contracts make audits and cross-region evidence verifiable.

---

<a id="contributing-a-new-tool"></a>
## 🧩 Contributing a new tool

### ✅ Definition of done
A tool is “real” when it has:
- CLI: `--help`, `--version`, and **≥ 2 examples**
- deterministic defaults (stable ordering; seeded randomness when applicable)
- structured logs + stable exit codes
- writes outputs to correct stage (raw/work/processed)
- emits/updates catalogs + provenance for publish-like outputs
- emits run manifest for publish/promote steps
- CI target (smoke test minimum)
- clear home in folder map
- optional: matching runbook doc under `docs/tools/<tool>.md` (template-based) 🧾[^markdown_v13]

### 🪜 Promotion ladder (scripts → governed tools)
1) prototype in `sandbox/` or notebook  
2) move core logic into `src/`  
3) add thin `tools/` CLI wrapper  
4) add validators + provenance emission  
5) add run manifest + canonical hashing  
6) add CI target + docs + examples  
7) promote to governed surface ✅

---

## 📁 Expected folder layout (target)

```text
🛠️ tools/
├── 📘 README.md
├── 🧰 _lib/                      # shared helpers (logging, env validation, guardrails)
├── 🧾 manifests/                 # tool manifests (one per tool)
├── 🛰️ agents/                    # Watcher–Planner–Executor entrypoints (PR-based automation)
├── 🧲 ingest/                    # controlled ingest entrypoints (thin wrappers)
│   ├── docs/                     # doc/PDF ingestion → text + metadata + graph links (gated)
│   └── feeds/                    # scheduled fetchers (deny-by-default network)
├── 🏷️ catalogs/                  # STAC/DCAT emitters + catalog build helpers
├── ✅ validation/                # fast QA gates (schema/link/prov/policy)
│   ├── ⚡ catalog_qa/             # PR-friendly catalog QA gate
│   ├── 🛡️ policy/                # OPA/Conftest policy pack
│   ├── 🧭 geo/                   # CRS/geom/raster validators
│   ├── 📊 stats/                 # drift/effect-size reports
│   ├── 🔐 security/              # hostile-input checks (zip bombs, traversal, SSRF)
│   └── 📡 telemetry/             # validate event schemas + payloads
├── 🆔 id/                        # deterministic IDs, hashing, manifest tooling
├── 🧬 prov/                      # provenance helpers (PROV JSON-LD emitters)
├── 🧾 audit/                     # run manifests, canonical JSON hashing, AI ledger tooling
├── 📦 artifacts/                 # OCI/registry helpers (oras/cosign wrappers)
├── 📚 library/                   # extract PDF portfolios + build doc manifests/indexes
├── 🔎 search/                    # build/validate keyword index + snapshots (optional)
├── 🧠 ai/                        # prompt gate, model pinning, embedding index builders
├── 🧵 content/                   # Story Nodes, storyboard.json, Pulse Threads, Concept Nodes
├── 🕸️ graph/                     # graph ingest helpers (must consume catalog roots)
│   └── 🩺 health/                # graph health checks
├── 🗄️ db/                        # PostGIS helpers, migrations, query packs
├── 🗺️ geo/                       # GDAL wrappers, tiling, reprojection, COG/PMTiles utilities
├── 🛰️ rs/                        # remote sensing helpers
├── 🧊 3d/                        # 3D Tiles / glTF tooling
├── 🌐 web/                       # map build helpers (styles, offline packs, export tools)
├── 🤖 ml/                        # train/eval orchestration (must emit datasets + metrics refs)
├── 🧮 simulation/                # scenario runners (must record configs + seeds)
├── 🔏 attest/                    # SBOM + signing helpers
├── ⚡ perf/                      # profiling harnesses + performance budgets
└── 🧪 ci/                        # deterministic entrypoints used by CI
```

---

<a id="project-reference-library"></a>
## 📚 Project reference library

These project files inform the toolchain design (determinism, provenance, governance, security, scaling, and UX constraints).  
Keep this list updated when the library changes.

> [!NOTE]
> Recommended canonical home: `docs/library/` (PDFs, docx, and extracted portfolio contents) + `docs/` for authored docs.[^tech_doc]

### 🧭 Core KFM contracts & architecture
- **Master Guide v13 (repo contract)** → `docs/MASTER_GUIDE_v13.md`[^kfm_v13]
- **Markdown + folder protocol (v13)** → `MARKDOWN_GUIDE_v13.md.gdoc`[^markdown_v13]
- **Platform overview & roadmap** → `Kansas Frontier Matrix (KFM) – Comprehensive Platform Overview and Roadmap.pdf`[^roadmap]
- **Architecture, features, and design** → `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf`[^arch_design]
- **Technical documentation** → `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`[^tech_doc]
- **UI system architecture guide** → `Kansas Frontier Matrix (KFM) – Comprehensive UI System Overview (Technical Architecture Guide).pdf`[^ui_arch]
- **Design audit (gaps + enhancements)** → `Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf`[^design_audit]

### 🤖 AI, governance, and safety
- **AI system overview** → `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf`[^focus_mode]
- **AI infrastructure (local runtime + dev/CI patterns)** → `KFM AI Infrastructure – Ollama Integration Overview.pdf`[^ollama_infra]
- **MCP / Scientific method receipts** → `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf`[^mcp_receipts]
- **Privacy + inference control references** → `Data Mining Concepts & applictions.pdf`[^privacy_inference]

### 🗺️ Geospatial & mapping references
- **Mapping hub design patterns** → `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf`[^mapping_hub]
- **Geospatial analysis cookbook (Python)** → `KFM- python-geospatial-analysis-cookbook-...-with-python.pdf`[^gdal_ogr2ogr]

### 🧾 Writing conventions
- **Advanced GitHub Markdown patterns** → `Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx`[^markdown_guide]

### 📦 Reference portfolios (PDF Portfolios) 🗃️
Some “bookshelves” are packaged as **PDF Portfolios** and should be extracted into normal folders for indexing/search.[^pdf_portfolios]

- `AI Concepts & more.pdf` *(PDF Portfolio)*
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf` *(PDF Portfolio)*
- `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf` *(PDF Portfolio)*
- `Various programming langurages & resources 1.pdf` *(PDF Portfolio)*
- `Mapping-Modeling-Python-Git-HTTP-CSS-Docker-GraphQL-Data Compression-Linux-Security.pdf` *(PDF Portfolio)*
- `Geographic Information-Security-Git-R coding-SciPy-MATLAB-ArcGIS-Apache Spark-Type Script-Web Applications.pdf` *(PDF Portfolio)*

> [!TIP]
> Add a governed extractor like `tools/library/extract_pdf_portfolio.py` that emits:
> - extracted PDFs
> - `manifest.json` (filename, sha256, source portfolio, extracted_at)
> - optional local search index for docs (dev-only)

---

<a id="metadata"></a>
## 🧾 Metadata

```yaml
title: "tools/ — Kansas Frontier Matrix Toolchain"
path: "tools/README.md"
version: "v0.8.0"
last_updated: "2026-01-26"
review_cycle: "90 days"
governance: "FAIR + CARE aligned; sovereignty-aware"
pipeline_order: "Raw → Work/ETL → Processed → STAC/DCAT/PROV catalogs → Stores/Indexes/Graph → APIs → UI → Story Nodes → Focus Mode"
```

---

<a id="version-history"></a>
## 🕰️ Version history

| Version | Date | Summary | Author |
|---:|---|---|---|
| v0.8.0 | 2026-01-26 | **Contract + library alignment upgrade:** integrated v13 folder/markdown protocol references, clarified hybrid stores/indexes stage (PostGIS + Neo4j + Search + optional vector retrieval), expanded Prompt Gate + OPA policy version hash logging expectations, added dedicated Search/Retrieval + AI runtime tooling guidance (Ollama optional), and refreshed the project reference library (adds v13 protocol, design audit, mapping hub, geospatial cookbook, privacy/inference refs, and markdown guide docx). | KFM Engineering |
| v0.7.0 | 2026-01-26 | **Upgrade pass (alignment + safety + tool governance):** clarified tool registry/manifest expectations, strengthened Prompt Gate + “no uncited assertions” posture, expanded offline pack + OCI artifact distribution guidance, folded Story Node storyboard validation into governed tooling, added privacy/inference-control guidance (k-anonymity/l-diversity/t-closeness + query auditing), and updated reference library to include all PDF portfolios. | KFM Engineering |
| v0.6.0 | 2026-01-20 | Integrated run manifests + JSON canonicalization (idempotent runs), OCI artifact registry distribution (ORAS + Cosign + digest pinning), Pulse Threads + Concept Nodes as governed content artifacts, weekly graph health checks, and GeoParquet + PMTiles dual-format packaging. | KFM Engineering |
| v0.5.0 | 2026-01-19 | Aligned with v13 staging (`data/raw|work|processed`), added Watcher–Planner–Executor guidance, strengthened provenance-first + citation-required Focus Mode rules, expanded offline pack expectations; refreshed reference library. | KFM Engineering |
| v0.4.0 | 2026-01-13 | Added determinism levels, artifact QA matrix, stats evidence tooling, 3D/WebGL guidance, remote sensing + compression notes, federation framing; clearer promotion ladder. | KFM Engineering |
| v0.3.0 | 2026-01-11 | Aligned to Master Guide v13 invariants: contract-first + evidence-first; clarified canonical paths (`schemas/`, `src/*`, `web/`, `releases/`). | KFM Engineering |
| v0.2.0 | 2026-01-09 | Clarified boundaries (tools vs src/scripts/mcp), added tool contract + QA rings + security posture + folder map. | KFM Engineering |
| v0.1.0 | 2026-01-08 | Initial toolbox README draft. | KFM Engineering |

---

## 📎 Evidence notes (footnotes)

[^kfm_v13]: Master Guide v13: contract-first + evidence-first; API boundary; deterministic ETL; catalog/provenance before downstream stages; Story Nodes + Focus Mode are citation-enforced and advisory-only.  
[^markdown_v13]: v13 markdown + folder protocol (templates, runbooks, canonical paths; “pipeline ordering is absolute”).  
[^data_layout]: Data lifecycle layout: raw/work/processed + catalogs/prov as publish boundary (see v13 protocol + core architecture docs).  
[^immutability]: Raw input data is immutable/read-only; transformations are deterministic/config-driven for reproducibility.  
[^stac_dcat_prov]: “Catalog triplet” requirement: STAC + DCAT + PROV emitted per dataset and stored at the publish boundary.  
[^policy_pack]: Policy-as-code posture (OPA/Conftest) and governance enforcement surface (license/classification/no-downgrade; deny-by-default).  
[^wpe]: Watcher–Planner–Executor pattern: PR-based automation, receipts, idempotency expectations, and attested outputs.  
[^focus_mode]: Focus Mode: evidence-backed, citation-enforced, advisory-only; policy versioning + audit logs; no hallucinated entities; hedging rules for speculation.  
[^prompt_gate]: Prompt Gate: prompt-injection defense, tool execution constraints, allow/deny lists, sandboxing, and output post-checks for citations.  
[^sensitivity]: Sensitivity controls: location generalization, policy tags, permission-based access; sovereignty-aware governance.  
[^run_manifest]: Run manifests + canonical JSON hashing to support idempotency and robust provenance linking.  
[^pmtiles_dual_pack]: Dual packaging: GeoParquet for analytics + PMTiles for web/offline; catalogs link both distributions; provenance captures tiling params.  
[^oci_registry]: OCI registry distribution: ORAS push/pull + Cosign signing + digest pinning; DCAT distributions reference immutable digests.  
[^offline_packs]: Offline packs: governed artifacts with signed manifests, scoped catalogs, policy labels, and (optionally) an offline web shell.  
[^story_nodes]: Story Nodes: machine-ingestible storytelling (Markdown + citations + stable graph IDs) and declarative storyboard JSON for UI playback.  
[^ui_arch]: UI architecture: provenance-first UX; citations as inspectable evidence; Story Node playback; timeline + map state as declarative script.  
[^schema_drift]: Planner-driven schema drift handling: propose migrations/scripts in PR; controlled evolution.  
[^slsa_attest]: SLSA-ish attestations for build/release artifacts; signed provenance; SBOM generation.  
[^privacy_inference]: Privacy & inference control methods (k-anonymity, l-diversity, t-closeness, differential privacy, query auditing).  
[^crs_wgs84]: WGS84 (EPSG:4326) as web-friendly standard; reprojection tracked in provenance.  
[^gdal_ogr2ogr]: GDAL/GeoPandas/Shapely/Rasterio patterns and geospatial implementation references in the cookbook/docs.  
[^mapping_hub]: Mapping hub design patterns (catalogs, exports, interoperability, and doc knowledge base).  
[^tech_doc]: Technical documentation (hybrid stores incl. PostGIS + Neo4j + search index; provenance-first; catalogs; supply-chain posture).  
[^arch_design]: Architecture/design reference (system layering; hybrid DB; ontology alignment; search + semantic retrieval; optional 3D).  
[^roadmap]: Platform roadmap (Watcher-based ingestion, content-aware fetch receipts, offline packs, immersive/AR direction, federation).  
[^ollama_infra]: Ollama integration overview (local runtime, embeddings, test/CI patterns, policy checks, developer ergonomics).  
[^design_audit]: Design audit notes (gaps, enhancement opportunities, and backlog candidates for tooling/UX).  
[^markdown_guide]: Markdown best practices and advanced GitHub formatting patterns.
[^pdf_portfolios]: PDF Portfolios are “containers” of PDFs; extract to folders for indexing/search; governed extractor should emit a manifest + hashes.