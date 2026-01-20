<!--
📌 tools/ is the repo’s *governed toolchain surface* for building + validating KFM artifacts.
🗓️ Last updated: 2026-01-20
🔁 Review cycle: 90 days (or anytime pipeline order / catalogs / policy changes)
🧭 Alignment: Master Guide v13 (contract-first + evidence-first + one canonical home per subsystem)
🧪 Scientific posture: Verification + Validation + Uncertainty Quantification (V&V&UQ) for anything “model-y”
-->

> According to a document set updated through **2026-01-20**, `tools/` is the **governed command surface** for building + validating KFM artifacts — and it must preserve the v13 pipeline order, provenance-first publishing, and citation-required Focus Mode. 🧾✅[^kfm_v13]

<div align="center">

# 🛠️ `tools/` — Kansas Frontier Matrix (KFM) Toolchain

**Deterministic • Provenance-aware • CI-friendly**  
**Build it once • verify it forever • ship with a paper trail** 🧾✅

![Python](https://img.shields.io/badge/Python-3.11%2B-informational)
![Node](https://img.shields.io/badge/Node-18%2B-informational)
![Docker](https://img.shields.io/badge/Docker-optional%20%28dev%2FCI%29-informational)
![License](https://img.shields.io/badge/license-MIT-success)

![Contract-first](https://img.shields.io/badge/contract--first-schemas%20%2B%20API-blue)
![Evidence-first](https://img.shields.io/badge/evidence--first-catalogs%20%2B%20PROV-blueviolet)
![Provenance-first](https://img.shields.io/badge/provenance--first-no%20publish%20without%20PROV-red)
![Catalog-first](https://img.shields.io/badge/catalog--first-STAC%20%7C%20DCAT%20%7C%20PROV-blue)
![Policy-as-code](https://img.shields.io/badge/policy--as--code-OPA%20%2F%20Conftest-ff7a00)
![SBOM](https://img.shields.io/badge/SBOM-SPDX%20%7C%20CycloneDX-2ea043)
![SLSA-ish](https://img.shields.io/badge/SLSA-ish-attestations-8b5cf6)

![GeoParquet](https://img.shields.io/badge/GeoParquet-analytics-2ea043)
![COG](https://img.shields.io/badge/COG-rasters-1f6feb)
![PMTiles](https://img.shields.io/badge/PMTiles-vector%20tiles-8250df)
![OCI](https://img.shields.io/badge/OCI-artifact%20registry-8b5cf6)
![ORAS](https://img.shields.io/badge/ORAS-transfer-8b5cf6)
![Cosign](https://img.shields.io/badge/Cosign-signing-8b5cf6)

![STAC](https://img.shields.io/badge/STAC-catalogs-1f6feb)
![DCAT](https://img.shields.io/badge/DCAT-discovery-8250df)
![PROV](https://img.shields.io/badge/PROV-lineage-8250df)
![Neo4j](https://img.shields.io/badge/Neo4j-graph-00ba7c)
![PostGIS](https://img.shields.io/badge/PostGIS-spatial%20DB-2d6cdf)
![MapLibre](https://img.shields.io/badge/MapLibre-2D%20maps-1f6feb)
![Cesium](https://img.shields.io/badge/Cesium-optional%203D-6f42c1)

</div>

> **TL;DR:** `tools/` is the **governed toolchain** that builds, validates, and packages KFM artifacts **without bypassing governance**.  
> Tools are **CI-safe** by design: deterministic defaults, clear contracts, fast QA gates, provenance emission, and policy checks.

> [!IMPORTANT]
> **MCP** = **Methods, Controls & Processes** *(a.k.a. “Master Coder Protocol” — lab notebook + receipts)* 🧪🧾  
> `tools/` must support MCP workflows by producing **re-run-able** outputs and **linkable** provenance — without becoming “business logic.”[^mcp_receipts]

---

<details>
<summary><b>🧭 Table of contents</b></summary>

- [🧠 Quick links](#quick-links)
- [🧭 Repo invariants](#repo-invariants)
- [🧱 The non-negotiable ordering](#non-negotiable-ordering)
- [🎯 What belongs in tools](#what-belongs-in-tools)
- [🧭 Boundaries: tools vs scripts vs src vs mcp](#boundaries)
- [🤖 Agent toolchain: Watcher–Planner–Executor](#agent-toolchain)
- [🧾 Contracts & schemas](#contracts-and-schemas)
- [📦 Data staging + catalog locations](#data-staging)
- [🧩 Dual-format packaging: GeoParquet + PMTiles](#dual-format-packaging)
- [🧱 Tool contract](#tool-contract)
- [🧾 Run manifests & JSON canonicalization](#run-manifests)
- [🎲 Determinism & reproducibility levels](#determinism)
- [🧪 Artifact QA matrix](#qa-matrix)
- [📡 Telemetry & observability](#telemetry)
- [📁 Expected folder layout](#expected-layout)
- [🔁 Common workflows](#common-workflows)
- [✅ Validation & QA gates](#validation-gates)
- [🔏 Provenance, SBOM, attestations, releases](#provenance-sbom-attestations)
- [📦 OCI artifact registry distribution](#oci-distribution)
- [📦 Offline packs & field ops](#offline-packs)
- [🧵 Pulse Threads & Concept Nodes](#pulse-threads)
- [🗺️ Geo & mapping utilities](#geo-mapping)
- [🛰️ Remote sensing utilities](#remote-sensing)
- [🧊 Imaging & compression utilities](#imaging-compression)
- [🧱 3D / WebGL / scene utilities](#3d-visualization)
- [🩺 Graph health checks](#graph-health)
- [🧠 Graph & DB utilities](#graph-db)
- [📊 Statistical evidence utilities](#stats-evidence)
- [🧪 Modeling/ML/simulation utilities](#modeling-ml-simulation)
- [🔐 Security posture](#security-posture)
- [⚡ Performance & scaling notes](#performance-scaling)
- [🌍 Federation & cross-matrix interoperability](#federation)
- [🧩 Contributing a new tool](#contributing)
- [📚 Project reference library](#reference-library)
- [🧾 Metadata](#metadata)
- [🕰️ Version history](#version-history)

</details>

---

<a id="quick-links"></a>
## 🧠 Quick links

- 📘 Canonical repo guide (v13) → `docs/MASTER_GUIDE_v13.md`[^kfm_v13]
- 🧾 KFM STAC/DCAT/PROV alignment (v13) → `docs/standards/` + `schemas/`[^stac_dcat_prov]
- 📖 Glossary (shared language) → `docs/glossary.md`
- 📏 Schemas & contracts (source of truth) → `schemas/`
- 🧪 Research workflow + run receipts → `mcp/README.md`[^mcp_receipts]
- 🧪 Canonical pipelines (ETL code) → `src/pipelines/`
- 🕸️ Graph build & ontology bindings → `src/graph/`
- 🛡️ API boundary (contracts + redaction) → `src/server/` (UI does **not** query graph directly)[^kfm_v13]
- 🌐 UI (React · MapLibre · optional Cesium) → `web/`[^ui_provenance_exports]
- 🗂️ Data lifecycle + catalogs → `data/README.md` (and the staging layout below)[^data_layout]
- 🧷 Governance gates → `docs/governance/REVIEW_GATES.md`
- 🛡️ Policy pack (OPA / Conftest) → `tools/validation/policy/*.rego`[^policy_pack]
- 🔏 Releases (bundles, SBOMs, attestations) → `releases/`
- 🧾 Citation metadata (software + snapshots) → `CITATION.cff`
- ✅ Tests → `tests/README.md`

---

<a id="repo-invariants"></a>
## 🧭 Repo invariants

> [!IMPORTANT]
> These are **guardrails**, not preferences. If a tool would violate these, redesign the tool.

### ✅ One canonical home per subsystem 🧱
No mystery duplicates. If logic belongs in:
- pipelines → `src/pipelines/`
- graph → `src/graph/`
- API boundary → `src/server/`
- UI → `web/`
- schemas → `schemas/`
- governed narratives → `docs/reports/story_nodes/`

### ✅ Contract-first 📏
Schemas and API contracts are **first-class artifacts**:
- implementations must conform
- changes require versioning and compatibility checks
- tools should validate against contracts by default

### ✅ Evidence-first + provenance-first 🧾🧬
No “published-looking” output without boundary artifacts:
- **STAC + DCAT + PROV** are required before:
  - graph ingest
  - API exposure
  - UI or Story Node usage[^stac_dcat_prov]
- **Raw data is immutable**; “work” is ephemeral; “processed” is governed evidence.[^immutability]
- **Large artifacts may live outside Git** (OCI registry / DVC / artifact store) *only* if catalogs + PROV remain the canonical “truth boundary.”[^oci_registry][^dvc]

### ✅ Deterministic by default 🎲🚫
Given the same inputs + config + seed, tools must produce the same outputs (ordering included).[^immutability]

### ✅ The ordering is a governance boundary 🧱🔒
Pipeline order is **absolute** (tools must not provide shortcuts).[^kfm_v13]

### ✅ Focus Mode is citation-required (and advisory) 🧠🧾
Focus Mode must cite sources and can refuse if citations can’t be produced.[^focus_mode]

### ✅ Human-centered + sovereignty-aware 🌾🧑‍🤝‍🧑
Tools are not just “code runners” — they shape **decision artifacts**:
- respect consent, agency, and auditability
- treat policy & classification as **data**, enforced by gates[^sensitivity]
- default to *least surprise* and *least privilege*

---

<a id="non-negotiable-ordering"></a>
## 🧱 The non-negotiable ordering

> [!IMPORTANT]
> This ordering is not “architecture style.” It’s a **governance boundary**.[^kfm_v13]

**Raw → Work/ETL → Processed → Catalogs (STAC/DCAT/PROV + QA) → Graph → APIs → UI → Story Nodes → Focus Mode**

```mermaid
flowchart LR
  A["📥 Raw (immutable)<br/>data/raw/<domain>/"] --> B["🧪 Work / ETL (scratch)<br/>data/work/<domain>/"]
  B --> C["📦 Processed (publishable artifacts)<br/>data/processed/<domain>/"]
  C --> D["🗂️ Catalog boundary artifacts<br/>data/stac + data/catalog/dcat + data/prov<br/>+ QA gates"]
  D --> E["🕸️ Graph ingest<br/>(Neo4j; references catalogs)"]
  E --> F["🛡️ APIs<br/>(contracts + redaction)"]
  F --> G["🌐 UI<br/>(React · MapLibre · optional Cesium)"]
  G --> H["📚 Story Nodes<br/>(governed narratives)"]
  H --> I["🎯 Focus Mode<br/>(evidence-linked context)"]
```

**Practical implication:** `tools/` must never create **published-looking outputs** that skip **catalog + provenance**.

---

<a id="what-belongs-in-tools"></a>
## 🎯 What belongs in tools

`tools/` is for **reusable, CI-friendly tooling** that builds/validates artifacts in the governed pipeline.

✅ Good fits:
- **Catalog QA gates** (STAC/DCAT/PROV schema + link + required-field checks)
- **Deterministic ID/hashing utilities** (stable IDs, checksums, manifests)
- **Format and integrity tooling** (COG validation, GeoParquet schema checks, geometry validity)
- **Policy enforcement tooling** (OPA/Conftest policy pack; no-downgrade rules; “no publish without provenance”)[^policy_pack]
- **Graph/DB loaders** that **ingest from catalogs** (not ad-hoc inserts)
- **Release packaging** (SBOM generation, signatures, attestations)
- **CI entrypoints** (non-interactive, stable exit codes)
- **Scientific integrity harnesses** (V&V, UQ smoke checks, regression tests)[^mcp_receipts]
- **Agent wrappers** that only operate via reviewable artifacts (Watcher/Planner/Executor that opens PRs, emits receipts, and never “hot-patches” main)[^wpe]
- **Library ingestion & extraction** (e.g., extract PDF Portfolios into a normal folder + manifest for indexing)[^pdf_portfolios]
- **Content artifact helpers** that remain governed:
  - Story Node evidence manifests + PROV stubs (citation ↔ manifest consistency checks)[^story_manifest]
  - Pulse Threads + Concept Nodes generation/validation (draft-by-default, PR-based)[^pulse_threads][^concept_nodes]
- **Graph health checks** and weekly integrity reports (orphan scan, constraint check, drift summary)[^graph_health]
- **Artifact distribution helpers** for large binaries (OCI registry push/pull + signing; catalog pointers stay canonical)[^oci_registry]

🚫 Not a good fit:
- Long-lived services (APIs, daemons) → runtime/app folders
- Core domain/business logic → `src/` (importable, testable modules)
- One-off “forever scripts” that bypass provenance and approvals → keep in sandbox until promoted
- Anything that can’t run non-interactively (or can’t be made CI-safe)

---

<a id="boundaries"></a>
## 🧭 Boundaries: tools vs scripts vs src vs mcp

### `src/` = canonical behavior (the engine) 🏗️
- ETL jobs (`src/pipelines/`), graph build (`src/graph/`), API logic (`src/server/`), reusable libs.

### `tools/` = governed toolchain (the verified command surface) 🛠️
- Thin entrypoints that call canonical modules, run validators, emit provenance, and produce release-quality artifacts.

### `scripts/` = convenience orchestration (the buttons/levers) 🧰
- Local ops, developer helpers, environment glue.
- Preferred pattern: **scripts call tools**, tools call src.

### `mcp/` = receipts & scientific record (the lab notebook) 🧪🧾
- Run receipts, experiment logs, model cards, governance checklists.[^mcp_receipts]

> [!TIP]
> If you’re implementing core behavior inside `tools/`, that’s a smell.  
> Put the logic in `src/` and keep `tools/` as a predictable CLI + validator layer.

---

<a id="agent-toolchain"></a>
## 🤖 Agent toolchain: Watcher–Planner–Executor

KFM supports **agent-assisted workflows** — but only when they behave like **governed tools** (deterministic, reviewable, provenance-emitting). The recommended structure is **Watcher–Planner–Executor**.[^wpe]

### 🛰️ Watcher (detect change → propose)
- Scans a defined surface (e.g., new files in a drop folder, updated feeds, new imagery, changed catalog entries).
- Emits an **immutable event** / proposal artifact:
  - `event.json` (what changed, where, why it matters)
  - proposed `plan.json` inputs (but does **not** run destructive changes)
- Default: **no network** unless `--allow-network` is set.

### 🧭 Planner (propose plan → deterministic, diffable)
- Takes Watcher events and produces a **deterministic plan**:
  - exact tool invocations
  - expected inputs/outputs
  - policy gates to run
  - rollback / failure behavior
- Writes a plan artifact that is:
  - stable-sorted
  - hashed
  - human-readable & machine-readable
- Must incorporate governance rules (e.g., FAIR+CARE constraints, sensitivity labels, and “no publish without provenance”).[^policy_pack][^sensitivity]

### 🧾 Executor (apply plan → PR-based + attested)
- Executes the plan in a controlled environment.
- Produces:
  - updated artifacts (data + catalogs + prov)
  - structured reports
  - MCP run receipt
- **Opens a pull request** (or produces a patch) rather than mutating protected branches.
- Attaches **SBOMs + SLSA-ish attestations** for the automated output (especially if generated/packaged by the agent).[^wpe]

> [!IMPORTANT]
> “Automation” in KFM is not a bypass — it’s a **more disciplined contributor**.  
> If a human would need to pass gates, an agent does too.

---

<a id="contracts-and-schemas"></a>
## 🧾 Contracts & schemas

> [!IMPORTANT]
> **Schemas live at repo root:** `schemas/` is the canonical source of truth.  
> Tools must validate against these contracts by default.

### ✅ What counts as a “contract artifact”
- JSON Schema (STAC/DCAT/PROV, Story Nodes, UI configs, telemetry)
- API boundary contracts (OpenAPI, GraphQL SDL, typed request/response)
- Tool manifests (optional) describing inputs/outputs, gates, and network posture
- **Data contract metadata** describing dataset schema, units, provenance hooks, and sensitivity
- **Domain design packs** (recommended): small “spec packets” per domain (units, preprocessing, metrics, certainty budgets) that tools can validate and use consistently.[^concept_nodes]

### ✅ Where tools should look
- `schemas/` → JSON schemas (STAC/DCAT/PROV/storynodes/ui/telemetry)
- `docs/standards/` → KFM profiles and governance rules (STAC/DCAT/PROV profiles, repo structure standard)[^stac_dcat_prov]

### 🧾 Data contract metadata (dataset-level) 📦
For any dataset that will become evidence, require a dataset metadata file that includes:
- schema/fields + units
- coordinate reference system expectations (where applicable)
- license + attribution
- sensitivity/classification tags[^sensitivity]
- expected spatial/temporal bounds (where applicable)
- pointers to where STAC/DCAT/PROV will be emitted

---

<a id="data-staging"></a>
## 📦 Data staging + catalog locations

KFM data work is staged and traceable, with **one canonical home per dataset**.[^data_layout]

### ✅ Canonical staging pattern (v13)

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
> **Immutability & trust boundaries**:  
> `raw/` is never edited; `work/` is ephemeral; `processed/` is governed evidence.[^immutability]

### 📌 Source manifests (recommended for every ingest)
Place a source manifest alongside incoming data to make ingestion repeatable:
- URL/source identifier
- retrieval timestamp
- method (API export, manual upload, scan, etc.)
- checksums
- license/attribution notes (or links)[^sources_manifest]

### Streaming / near-real-time inputs ⏱️
For streaming datasets:
- treat each batch as **append-only**
- use windowing (daily/weekly/monthly)
- don’t rewrite history silently — publish a new version + provenance trail[^streaming]

### 📦 Where big binaries live (Git vs Registry vs DVC) 🧳
KFM supports “small in Git, big in artifact storage” patterns **only** when:
- catalogs still exist in-repo and remain the canonical boundary
- PROV links the exact digest/version of the external artifact
- policy gates run the same way (license/sensitivity/no-downgrade) before publish[^oci_registry][^dvc]

---

<a id="dual-format-packaging"></a>
## 🧩 Dual-format packaging: GeoParquet + PMTiles

KFM’s roadmap explicitly supports **dual-purpose geospatial outputs**:
- **GeoParquet** for analytics & bulk queries
- **PMTiles** for fast web map delivery and offline packs (single-file vector tile archive)[^pmtiles_dual_pack]

Why this lives in `tools/`:
- building both outputs from one processed dataset must be deterministic
- catalogs must link both distributions (STAC assets + DCAT distributions)
- provenance must record the “tile build” activity and parameters (tiling, simplification, zoom range)[^pmtiles_dual_pack]

> [!TIP]
> Treat GeoParquet + PMTiles as a *pair*: the UI serves PMTiles; analysis runs on GeoParquet; both point back to the same `data/processed/<domain>/` “evidence root.”

---

<a id="tool-contract"></a>
## 🧱 Tool contract

Every tool must behave predictably under automation.

### ✅ Required CLI features
- `--help` (purpose, inputs/outputs, side effects, env vars, examples ≥ 2)
- `--version` (git SHA or semver)
- **safe-by-default mode**
  - either `--dry-run` default, or explicit “no writes unless --apply”
- `--apply` (only when the tool mutates state)
- `--env {dev|staging|prod}` when environment matters
- `--run-id <id>` (or read `KFM_RUN_ID`) for provenance correlation
- `--seed <int>` (or read `KFM_SEED`) for deterministic randomness
- `--contracts <path>` optional override (defaults to `schemas/`)
- `--log-json` (emit JSONL logs, one record per line)
- `--report <path>` (write a machine-readable summary artifact, even on failure)

### 🧾 RunContext + RunManifest (recommended)
For anything that produces evidence artifacts, tools should emit:
- `run_context.json` (human-oriented “receipt”)
- `run_manifest.json` (machine-oriented “exactly what happened”, canonicalized & hashed)[^run_manifest]

This is the glue between **PROV**, **catalogs**, **MCP receipts**, and **idempotency**.

### ✅ Exit codes (recommended standard)
- `0` success
- `2` CLI usage error
- `3` validation/QA failure (schema invalid, missing required fields, link check fails)
- `4` policy failure (license missing, classification downgrade, prohibited field)
- `>=10` runtime failure (I/O, network, DB, unhandled exceptions)

### 🔐 Network posture
- Default to **no network** unless explicitly required
- If a tool fetches remote inputs:
  - require `--allow-network`
  - block private IP ranges by default (SSRF defense)
  - log source URLs + checksums of downloaded artifacts

### 🧾 Provenance emission (minimum viable)
If a tool produces or promotes evidence artifacts, it must emit a PROV bundle containing:
- run_id, timestamps, tool name/version
- code identity (git SHA) + config hash
- inputs used (IDs + checksums where feasible)
- outputs generated (paths + checksums)
- pointers back to STAC/DCAT records

### 🤖 AI-assisted behavior (allowed, but gated)
If a tool uses AI to suggest metadata / mappings:
- default mode must be **suggest-only** (no mutation)
- require `--apply` to write anything
- log model/version/config where permissible
- treat outputs as **draft** until validated + reviewed
- preserve user agency (human-in-the-loop by design)[^hilt]

---

<a id="run-manifests"></a>
## 🧾 Run manifests & JSON canonicalization

Run manifests solve a boring-but-critical problem: **stable identity for “a run”**.

### ✅ Why KFM cares
KFM explicitly proposes a `run_manifest.json` + canonical JSON hashing approach so:
- two runs can be compared deterministically
- artifacts can be referenced by digest (even across storage backends)
- “exactly-once ingestion” patterns become feasible (idempotency keys)[^run_manifest]

### ✅ Recommended minimum fields (shape)
- `run_id`, timestamps, tool + version + git SHA
- normalized config + config hash
- input inventory (paths/URIs + sha256)
- output inventory (paths/URIs + sha256)
- “policy outcomes” summary (pass/fail + policy bundle version)
- pointers to emitted STAC/DCAT/PROV objects (IDs/hrefs)

### ✅ Canonicalization rule
Use a JSON canonicalization scheme (e.g., RFC 8785/JCS) before hashing so:
- key ordering doesn’t change the hash
- whitespace doesn’t change the hash
- floats/ints are consistently serialized[^run_manifest]

> [!NOTE]
> This does **not** replace PROV; it makes PROV *more usable* by giving every run a stable, content-derived identity.

---

<a id="determinism"></a>
## 🎲 Determinism & reproducibility levels

Not everything needs full hermetic builds — but everything needs **auditability**.

### 🧩 Repro levels (recommended)
| Level | Name | Promise | Typical use |
|---:|---|---|---|
| R0 | Deterministic | Same inputs+config+seed ⇒ same outputs | most tools |
| R1 | Provenance-complete | Deterministic + complete PROV + catalog pointers | publishable evidence |
| R1.5 | Idempotent-run | R1 + `run_manifest.json` canonical hash + replay guarantees | ingestion/promotion tooling |
| R2 | Rebuildable | R1 + pinned deps + machine spec captured | critical releases |
| R3 | Hermetic | R2 + no network + fully captured environment | highest assurance |

> [!TIP]
> If you don’t know which level you need, default to **R1** for anything that touches `processed/`.

---

<a id="qa-matrix"></a>
## 🧪 Artifact QA matrix

Use this matrix to decide which validators must run **before promotion** ✅

| Artifact type | Minimum checks | Extra checks (recommended) |
|---|---|---|
| 📄 JSON/JSON-LD (STAC/DCAT/PROV) | schema + required fields + link resolution | URI normalization + SPDX license lint |
| 🧾 Run manifests | schema + canonicalization + stable hash recompute | cross-check inventories vs filesystem + policy bundle version |
| 🧭 Vector (GeoParquet / FlatGeobuf / GeoJSON) | schema + CRS + geometry validity | topology rules + simplification policy + attribution propagation |
| 🧱 PMTiles | header validity + TileJSON/metadata present + bounds/zoom sanity | layer budgets + “no orphan attribution” + signature verify if distributed |
| 🛰️ Raster (COG / GeoTIFF / NetCDF) | COG layout + CRS + bounds + nodata | overview completeness + histogram sanity + tiling alignment |
| 🗄️ Tabular (Parquet/CSV) | schema + types + missingness report | drift checks + range checks + sampling provenance |
| 📦 Offline packs | manifest schema + checksums + policy gates | signature verification + size budgets + “no orphan assets” scan |
| 🧾 Story Nodes (Markdown + config) | schema + links + citations present | citation ↔ manifest consistency checks[^story_manifest] |
| 🧵 Pulse Threads / Concept Nodes | schema + citations/evidence refs + provenance pointers | cadence checks + “no unsourced assertions” lint |
| 🎨 Map styles (MapLibre JSON) | JSON lint + sources valid + sprite/glyph refs | contrast/legibility budgets + scale tests |
| 🧠 ML artifacts (metrics/models) | metrics schema + dataset refs + seeds | calibration checks + fairness slices + uncertainty |
| 🧮 Simulation outputs | config+seed captured + deterministic rerun | V&V smoke tests + UQ summary + sensitivity |
| 🧊 3D assets (3D Tiles / glTF) | manifest + attribution + bounding volume | LOD validation + GPU budget checks + compression checks |
| 📦 OCI artifacts | digest pinned + signature verified + SBOM attached | referrer integrity + policy tags enforced[^oci_registry] |

---

<a id="telemetry"></a>
## 📡 Telemetry & observability

Telemetry is a **contracted surface** (schema-first) — used to measure UX safety signals, governance friction, and system health.

### ✅ Expectations
- event schemas live under `schemas/telemetry/`
- tools should validate telemetry payloads against schemas in CI
- logs should be JSONL (tool-friendly), with a minimal human-readable console summary

KFM also proposes tracking system sustainability signals (e.g., **energy consumption / carbon footprint**) as part of observability for long-running workflows.[^energy_telemetry]

> [!TIP]
> Treat telemetry as evidence about the system itself: version it, validate it, and keep it privacy-aware.

---

<a id="expected-layout"></a>
## 📁 Expected folder layout

> If your repo differs, treat this as the target structure and document deltas in `tools/README.md`.

```text
🛠️ tools/
├── 📘 README.md
├── 🧰 _lib/                      # shared helpers (logging, env validation, guardrails)
├── 🧾 manifests/                 # optional tool.yaml manifests (one per tool)
├── 🛰️ agents/                    # Watcher–Planner–Executor entrypoints (PR-based automation)
├── 🧲 ingest/                    # controlled ingest entrypoints (thin wrappers)
│   ├── docs/                     # document/PDF ingestion → text + metadata + graph links (gated)[^bulk_doc_ingest]
│   └── feeds/                    # scheduled fetchers (deny-by-default network)
├── 🏷️ catalogs/                  # STAC/DCAT emitters + catalog build helpers
├── ✅ validation/                # fast QA gates (schema/link/prov/policy)
│   ├── ⚡ catalog_qa/             # catalog QA gate (PR-friendly)
│   ├── 🛡️ policy/                # OPA/Conftest policies (license/classification/no-downgrade)[^policy_pack]
│   ├── 🧭 geo/                   # CRS/geom/raster validators
│   ├── 📊 stats/                 # drift/residuals/effect-size reports
│   ├── 🔐 security/              # hostile-input checks (zip bombs, traversal, SSRF guards)
│   └── 📡 telemetry/             # validate event schemas + payloads
├── 🆔 id/                        # deterministic IDs, hashing, manifest tooling
├── 🧬 prov/                      # provenance helpers (PROV JSON-LD emitters)
├── 🧾 audit/                     # run manifests, JSON canonicalization, policy outcome receipts[^run_manifest]
├── 📦 artifacts/                 # OCI/registry helpers (oras/cosign wrappers, digest pinning)[^oci_registry]
├── 📚 library/                   # extract PDF portfolios + build doc manifests/indexes[^pdf_portfolios]
├── 🧵 content/                   # story manifests, pulse threads, concept nodes (governed content)[^pulse_threads]
├── 🧩 dsl/                       # optional: schema/profile/policy DSL compilers (contract-first)
├── 🕸️ graph/                     # graph ingest helpers (must consume catalog roots)
│   └── 🩺 health/                # graph health checks (weekly, CI-friendly)[^graph_health]
├── 🗄️ db/                        # PostGIS helpers, migrations, query packs
├── 🗺️ geo/                       # GDAL wrappers, tiling, reprojection, COG/PMTiles utilities[^pmtiles_dual_pack]
├── 🛰️ rs/                        # remote sensing helpers (GEE export, masking, compositing)
├── 🧊 3d/                        # 3D Tiles / glTF tooling, mesh + point cloud validation
├── 🌐 web/                       # map build helpers (styles, tiles packaging, offline packs)
├── 🤖 ml/                        # train/eval orchestration (must emit datasets + metrics refs)
├── 🧮 simulation/                # scenario runners (must record configs + seeds)
├── 🔏 attest/                    # SBOM + signing helpers (cosign/sigstore patterns)
├── ⚡ perf/                      # profiling harnesses + performance budgets
└── 🧪 ci/                        # deterministic entrypoints used by CI
```

> [!NOTE]
> Canonical schemas are in `schemas/` (repo root). Tools should **reference**, not duplicate, contracts.

---

<a id="common-workflows"></a>
## 🔁 Common workflows

### 🧭 “What do I run?” (at a glance)
| I want to… | Run… | Output… |
|---|---|---|
| ✅ Quick PR gate | `tools/validation/catalog_qa/...` | report + exit code |
| 🗂️ Build catalogs | `tools/catalogs/...` | STAC/DCAT |
| 🧬 Emit provenance | `tools/prov/...` | PROV bundle |
| 🧾 Emit run manifest | `tools/audit/build_run_manifest.py` | `run_manifest.json` + hash[^run_manifest] |
| 🧩 Build GeoParquet+PMTiles | `tools/geo/package_dual.py` | `.parquet` + `.pmtiles` + catalogs[^pmtiles_dual_pack] |
| 🚚 Promote/publish | `tools/catalogs/promote...` | atomic move + updated catalogs |
| 🕸️ Load graph/DB | `tools/graph/...` / `tools/db/...` | ingest report |
| 🩺 Graph health check | `tools/graph/health/weekly_check.py` | health report + KPIs[^graph_health] |
| 🌐 Build UI assets | `tools/web/...` | tiles/styles/manifests |
| 📦 Build offline pack | `tools/web/build_offline_pack.py` | signed pack + manifest |
| 📦 Push big artifacts to OCI | `tools/artifacts/push_oci.py` | digest-pinned artifacts + signatures[^oci_registry] |
| 🔏 Release bundle | `tools/attest/...` | SBOM + attestation in `releases/` |
| 🤖 Run automation safely | `tools/agents/watcher.py → planner.py → executor.py` | PR + receipts |

---

### A) Build a dataset (stage → validate → catalog → promote) ✅

1) Ingest → `data/raw/<domain>/...`  
2) Transform → `data/work/<domain>/...`  
3) Validate (schema/CRS/geometry/license/bounds)  
4) Emit STAC/DCAT/PROV  
5) Promote to `data/processed/<domain>/...`  
6) (Optional) Ingest into graph/DB from catalogs  
7) Write MCP run receipt if it affects decisions or production  

Illustrative shape:
```bash
# ingest (examples)
python tools/ingest/ingest.py --help

# validate (fast fail)
python tools/validation/catalog_qa/run_catalog_qa.py --help

# emit catalogs + provenance
python tools/catalogs/build_catalogs.py --help
python tools/prov/emit_prov.py --help

# promote (atomic publish)
python tools/catalogs/promote.py --help
```

> [!TIP]
> If it changes `processed/`, it should also change **STAC/DCAT/PROV** and have a run receipt.[^stac_dcat_prov]

---

### B) PR gate: “Catalog QA quick check” ⚡

Designed to be fast enough to run on every PR:
- schema validity (STAC/DCAT/PROV + extensions)
- required fields (license, bbox, time, assets)
- link resolution (hrefs exist; assets reachable in repo layout)

```bash
python tools/validation/catalog_qa/run_catalog_qa.py --root data/stac
```

---

### C) Evidence artifacts (analysis / AI / simulation outputs) 🧾🤖

KFM treats analysis outputs as first-class datasets:
- store under `data/processed/<domain>/...`
- create STAC/DCAT entries
- emit PROV capturing inputs + parameters + seeds + uncertainty/metrics
- do not expose directly in UI; go through API boundary[^kfm_v13]

```bash
python tools/ml/train.py --help
python tools/simulation/run_scenario.py --help
python tools/catalogs/build_catalogs.py --help
python tools/prov/emit_prov.py --help
python tools/validation/catalog_qa/run_catalog_qa.py --root data/stac
```

Simulation outputs should follow reproducible, deterministic patterns (config + seed + V&V + UQ summaries).[^kfm_sim]

---

### D) Policy enforcement (OPA / Conftest) 🛡️

Use policy tests for hard rules:
- license must exist
- classification must not downgrade
- prohibited fields/paths
- “no publish without provenance”
- “Focus Mode must cite evidence sources”[^focus_mode][^policy_pack]

```bash
conftest test -p tools/validation/policy data/stac data/catalog/dcat data/prov --all-namespaces
```

---

### E) Graph/DB ingest from catalogs (no ad-hoc writes) 🕸️

Graph and DB loaders should:
- accept **catalog roots** as inputs (STAC/DCAT/PROV)
- refuse to load items missing provenance or license (unless explicitly allowed)
- emit an ingest report (counts, warnings, failures)

```bash
python tools/graph/ingest_from_stac.py --help
python tools/db/load_from_catalog.py --help
```

---

### F) Build web-friendly map artifacts (COG + PMTiles + styles) 🗺️

KFM’s stack supports both PostGIS tile-serving and prepackaged tile archives (PMTiles/MBTiles) depending on deployment and offline needs.[^tile_postgis][^pmtiles_dual_pack]

```bash
python tools/geo/build_cog.py --help
python tools/geo/build_pmtiles.py --help
python tools/web/lint_style.py --help
python tools/3d/package_3dtiles.py --help
```

---

<a id="validation-gates"></a>
## ✅ Validation & QA gates

Think in rings (each ring blocks promotion if it fails):

### Ring 0: Structure 🧱
- JSON parses
- schema validation (STAC/DCAT/PROV + extensions)
- required files exist

### Ring 1: Integrity 🔗
- checksums/manifest inventory
- deterministic IDs present where required
- run manifest hash recompute + match[^run_manifest]
- atomic publish (no half-state)

### Ring 2: Semantics 🧠
- CRS correctness + axis order
- geometry validity (and any allowed repair policy)
- raster sanity (nodata, resolution, alignment)
- time/bounds sanity (Kansas bounds, plausible ranges)

### Ring 3: Statistical & scientific sanity 🧪📊
- drift checks (schema + distributions)
- regression diagnostics (residuals, heteroscedasticity, multicollinearity flags)
- uncertainty summaries (where applicable)
- “smell tests” for simulation outputs (stability checks / invariants)[^kfm_sim]

### Ring 4: Governance & safety 🔐
- license required before publish
- classification propagation (no downgrade)
- sensitive fields redaction rules (including location generalization policies)[^sensitivity]
- policy tests (OPA/Conftest) where used[^policy_pack]
- secrets scans + dependency hygiene checks

### Ring 5: AI integrity 🧠🧾
- Focus Mode outputs must carry citations; otherwise refuse or return an explicit “insufficient evidence” response.[^focus_mode]
- prompt-injection defenses and redaction validation (Prompt Gate)[^prompt_gate]

---

<a id="provenance-sbom-attestations"></a>
## 🔏 Provenance, SBOM, attestations, releases

### Provenance (required for publish)
At minimum, each publish action should have:
- run_id
- code version (git SHA)
- config hash
- inputs used (IDs + checksums where feasible)
- outputs generated (paths + checksums)
- pointers to STAC/DCAT records
- (recommended) run manifest hash + location[^run_manifest]

### ✅ PR-to-PROV binding (recommended)
KFM explicitly proposes mapping GitHub PRs/commits/workflows to PROV so every code change that affects evidence can be traced to:
- PR number + commit SHAs
- workflow run ID
- SBOM + signatures + policy outcomes[^github_prov]

### SBOM + signing (recommended for releases)
For release bundles or promoted artifacts:
- generate SBOMs (tool deps and/or artifact deps)
- sign artifacts where feasible
- attach attestations (build provenance, policy checks, QA outcomes)[^wpe]

### 📦 Release bundles live in `releases/`
Recommended structure:
```text
releases/
└── 2026-01-20_v0.6.0/
    ├── sbom.spdx.json
    ├── attestations/
    ├── manifests/
    └── notes.md
```

> [!TIP]
> Keep logs lightweight in-repo; store heavy logs as CI artifacts or in an artifact store.

---

<a id="oci-distribution"></a>
## 📦 OCI artifact registry distribution

For large artifacts (PMTiles, GeoParquet, COGs), KFM proposes leveraging **OCI registries as storage**:
- use **ORAS** to push arbitrary artifacts with media types
- use **Cosign** (keyless) to sign and verify artifacts
- attach signatures/SBOMs as OCI “referrers”
- reference artifacts by **digest** inside STAC/DCAT/PROV for immutability[^oci_registry]

> [!IMPORTANT]
> OCI storage is a distribution channel — not a governance bypass.  
> Catalogs + PROV remain the canonical boundary, and policy gates still apply.[^oci_registry]

---

<a id="offline-packs"></a>
## 📦 Offline packs & field ops

KFM’s UI roadmap includes **PWA support** and **offline data packs** so field researchers, educators, and rural communities can use KFM without connectivity.[^pwa_offline]

### ✅ What an offline pack should contain
- pre-rendered tiles (vector/raster) for a defined AOI
- slimmed catalogs (STAC/DCAT/PROV) scoped to the pack
- a signed manifest (checksums + versions + policy tags)
- “credits bundle” (attribution + licensing text for export/sharing)
- optional: a small on-device model for limited offline Focus Mode (if policy allows)[^offline_packs]

PMTiles/MBTiles are explicitly considered as offline-friendly tile packaging formats for KFM’s UI and tooling.[^pmtiles_dual_pack]

### 🧾 Governance requirement
Offline packs are still “publish-like” artifacts:
- must pass validation gates
- must include provenance + catalogs
- must carry policy labels (classification, sensitivity)

### 🧭 UX alignment
The UI is designed to surface provenance (“the map behind the map”), and even exports/shared views should carry credits.[^ui_provenance_exports]

---

<a id="pulse-threads"></a>
## 🧵 Pulse Threads & Concept Nodes

KFM proposes two “content artifacts” that sit between datasets and narratives — and they belong in the governed toolchain:

### 🧵 Pulse Threads (recurring evidence-linked updates)
Pulse Threads are designed as lightweight, recurring “what’s new + why it matters” narratives, anchored in evidence and structured metadata.[^pulse_threads]

Toolchain implications:
- schema-first thread metadata (cadence, scope, evidence refs)
- citations are mandatory; “no unsourced assertions” lint
- PR-based workflow (draft → review → publish)
- PROV links thread statements back to datasets/records

### 🧠 Conceptual Attention Nodes (concept-as-entity)
Concept Nodes define shared “concept anchors” (a place/event/phenomenon) that unify:
- domains
- synonyms / aliases
- policies / sensitivity constraints
- recommended datasets + story nodes[^concept_nodes]

Toolchain implications:
- concept schema + validation (IDs, aliases, links, policy tags)
- graph ingestion downstream of catalogs (concept nodes become graph entities with provenance)
- Focus Mode can cite concept nodes as stable, governed context

---

<a id="geo-mapping"></a>
## 🗺️ Geo & mapping utilities

### CRS & units are non-negotiable 📐
Tools that touch geometry must:
- refuse unknown CRS by default
- log CRS for inputs and outputs
- document any reprojection and record it in provenance

KFM’s internal standard is **WGS84 (EPSG:4326)** for web consistency; incoming data is reprojected on ingest and tracked in provenance.[^crs_wgs84]

### Web-serving friendliness 🌐
When emitting UI-facing assets:
- prefer COG with overviews for rasters
- avoid huge GeoJSON blobs (tile/simplify)
- ensure attribution + license + legends travel with the output

### Tile serving strategies (both are valid) 🧱
- **PostGIS tile endpoints** (e.g., `ST_AsMVT`), driven by API adapters[^tile_postgis]
- **Prepackaged tiles** (PMTiles/MBTiles) for fast static hosting and offline packs[^pmtiles_dual_pack]

---

<a id="remote-sensing"></a>
## 🛰️ Remote sensing utilities

Remote sensing tooling should prefer **derived products + provenance** over raw archive dumps:
- record AOI (bbox/geometry) + time window
- record compositing + masking logic (cloud/shadow, water, snow, etc.)
- record resolution/CRS
- export as COGs (and/or cloud-optimized NetCDF where relevant)
- emit STAC Items per logical unit (scene, tile, station-day, etc.)

> [!TIP]
> Don’t let EO pipelines become “mystery rasters.” If you can’t trace how it was made, it’s not shippable.

---

<a id="imaging-compression"></a>
## 🧊 Imaging & compression utilities

Images are evidence too — and compression choices change meaning 🧾

Recommended tool behaviors:
- detect format + bit depth + alpha channels
- warn when a lossy conversion could change interpretation (e.g., subtle gradients)
- emit a small report: chosen format, compression parameters, and rationale

Practical format hints (rule-of-thumb):
- **JPEG** → photographs / continuous tone, lossy
- **PNG** → screenshots / line art / sharp edges, lossless, supports alpha
- **GIF** → limited palette, simple animations (avoid for scientific rasters)
- **BMP/XBM** → legacy / rarely suitable in modern pipelines

---

<a id="3d-visualization"></a>
## 🧱 3D / WebGL / scene utilities

When we ship 3D, we ship **performance budgets + provenance** 🧊⚡

Tools in `tools/3d/` should support:
- validating glTF / 3D Tiles manifests
- generating LOD pyramids (and verifying completeness)
- embedding attribution + license + provenance pointers in manifests
- sanity-checking GPU budgets (triangle count, texture size, draw calls) for target devices

KFM’s mapping/UI design explicitly considers MapLibre for 2D and Cesium for 3D (3D Tiles / CZML), with time-slider storytelling and optional 3D expansion.[^maplibre_cesium]

> [!NOTE]
> Archaeology and historical reconstruction workflows often require **explicit uncertainty labeling** in 3D (e.g., “measured” vs “inferred”). Treat uncertainty as metadata, not a footnote.

---

<a id="graph-health"></a>
## 🩺 Graph health checks

KFM explicitly proposes a **weekly graph health check** as a governance-friendly integrity practice:
- catch orphan nodes/edges and integrity drift early
- produce a publishable health report (counts, constraints, anomalies)
- wire into CI + maintainer review loops[^graph_health]

Recommended outputs:
- `reports/graph_health/<date>/report.json`
- `reports/graph_health/<date>/report.md`
- `run_manifest.json` pointer + hash
- suggested fixes (as a PR plan), not silent mutations

---

<a id="graph-db"></a>
## 🧠 Graph & DB utilities

### Neo4j / graph 🕸️
Graph ingest should be downstream of catalogs:
- store references back to STAC/DCAT/PROV (don’t duplicate bulky data)
- enforce invariants:
  - “every dataset node links to provenance”
  - “no orphan entities”
  - “stable pagination order for query surfaces”

### PostGIS / PostgreSQL 🗄️
- prefer database-side spatial ops when safe (joins, buffers, within, intersects)
- use staging tables + transactional swaps (load → validate → swap)
- avoid foot-guns in shared query packs:
  - prefer explicit column lists over `SELECT *`
  - validate query plans for large tables (indices, bounds, partitions)

KFM’s PostGIS adapter pattern includes tile generation via `ST_AsMVT` and emphasizes the division:
**“PostGIS stores geo truth, catalogs describe assets, graph links context.”**[^tile_postgis]

---

<a id="stats-evidence"></a>
## 📊 Statistical evidence utilities

KFM treats statistics as **evidence engineering**, not “extra math” 📈🧾

Tools should help prevent common failure modes:
- silent p-hacking / multiple comparisons
- “significant but tiny” effects presented without context
- regression assumptions ignored (heteroscedasticity, multicollinearity, non-linearity)
- underpowered or non-replicable experimental setups

Recommended outputs:
- effect sizes + uncertainty (CI/credible intervals), not just p-values
- residual diagnostics (plots + stats)
- drift reports (training vs current distribution)
- declared priors (for Bayesian tools) + sensitivity summaries

Classification tooling should prefer reporting precision/recall and macro-averaged F1 where class imbalance exists.[^ml_metrics]

> [!TIP]
> If a statistical result is used to justify a decision or an operational rule, it belongs in `mcp/` as a run receipt (with links to catalogs + provenance).[^mcp_receipts]

---

<a id="modeling-ml-simulation"></a>
## 🧪 Modeling/ML/simulation utilities

Modeling tools must behave like scientific instruments 🧪🔬:
- capture parameters + seeds
- emit evaluation artifacts (metrics + plots where relevant)
- record dataset IDs used (STAC/DCAT pointers)
- write run receipts for significant results (MCP alignment)
- support verification/validation hooks (golden tests, invariants, sanity checks)

Simulation-specific expectations (V&V & UQ mindset):
- verification: “did we solve the equations right?”
- validation: “are we solving the right equations for this phenomenon?”
- uncertainty: quantify sensitivity to inputs, parameters, and model form[^kfm_sim]

> [!CAUTION]
> If a tool uses AI-assisted generation, label it and record the model/version/config where permissible.

---

<a id="security-posture"></a>
## 🔐 Security posture

Treat `tools/` as part of the threat model:
- inputs are hostile (archives, rasters, PDFs, GeoJSON, model files)
- validate types with allowlists
- enforce size limits + decompression limits
- defend against SSRF for network fetchers
- sanitize paths and refuse traversal
- never print secrets; never require secrets in CLI args

### 🧠 Prompt security (“Prompt Gate”)
KFM explicitly calls out a **Prompt Gate** approach: guardrails against prompt injection, policy bypass, and unsafe tool execution — especially for AI-assisted workflows.[^prompt_gate]

### 🧷 Sensitivity / sovereignty posture
KFM explicitly discusses sensitivity controls such as **location generalization**, access control, and policy tags (including CARE-aligned governance expectations for indigenous/community-sensitive data).[^sensitivity]

> [!IMPORTANT]
> Security references in the library are for **defensive posture and awareness** only.  
> Tools must never provide “offense automation” — the goal is resilience, not exploitation.

---

<a id="performance-scaling"></a>
## ⚡ Performance & scaling notes

When tools grow:
- chunk work (tiles/partitions/morsels) for parallelism
- introduce “pipeline breakers” at materialization boundaries
- keep caches explicit and provenance-aware
- profile first, then optimize (measure before guessing)
- prefer near-data execution for large scans (where architecture supports it)

Database performance reminders:
- stable query shapes + stable sort orders are part of determinism
- indexing strategy must be documented (and reproducible)
- treat query plans as artifacts for critical pipelines (store summaries in reports)

> The rule: speed is good — **but correctness and provenance come first**.

---

<a id="federation"></a>
## 🌍 Federation & cross-matrix interoperability

KFM is designed to be “federation-ready” 🌾➡️🌎:
- schemas and APIs should be standardizable across regions
- export/import should operate at the catalog boundary (STAC/DCAT/PROV)
- avoid Kansas-specific assumptions in reusable tool logic (keep those in domain configs)[^streaming]

Federation is explicitly framed as “multi-region discovery” driven by shared metadata protocols, where a central UI can query multiple regional KFMs via standard outputs (DCAT/STAC/PROV).[^streaming]

Ideas that fit naturally in `tools/`:
- `tools/catalogs/export_bundle.py` → export STAC/DCAT/PROV + checksums
- `tools/catalogs/import_bundle.py` → validate + ingest external catalogs (deny-by-default)
- `tools/contracts/package_schemas.py` → publish a versioned schema pack for sister projects

> [!NOTE]
> Federation strengthens governance: shared contracts make audits and cross-region evidence easier to verify.

---

<a id="contributing"></a>
## 🧩 Contributing a new tool

### ✅ Definition of done
A tool is “real” when it has:
- entrypoint (`.py`, `.js`, `.sh`, etc.) with `--help` and 2 examples
- deterministic defaults (stable ordering; seeded randomness if applicable)
- structured logs + stable exit codes
- writes outputs to the correct data stage (raw/work/processed)
- emits/updates catalogs + provenance when producing publishable artifacts
- emits run manifest when it publishes/promotes evidence[^run_manifest]
- a CI target (smoke test at minimum)
- a clear home in the folder map above

### Suggested `tool.yaml` manifest (recommended)
```yaml
name: "catalog_qa"
entrypoint: "tools/validation/catalog_qa/run_catalog_qa.py"
owner: "@team-or-handle"
inputs:
  - "data/stac/**"
outputs:
  - "reports/catalog_qa/**"
modes:
  - dry_run: true
  - apply: false
network:
  default: "deny"
determinism:
  stable_sorting: true
  seeded: false
gates:
  - "stac_schema"
  - "link_check"
  - "license_required"
  - "prov_required_for_publish"
  - "run_manifest_required"
```

### 🪜 Promotion ladder (how scripts become tools)
1) prototype in `sandbox/` or local notebook  
2) extract core logic into `src/`  
3) add a thin `tools/` CLI wrapper  
4) add validators + provenance emission  
5) add run manifest + canonical hashing  
6) add CI target + docs + examples  
7) promote to “governed surface” ✅  

---

<a id="reference-library"></a>
## 📚 Project reference library

These files inform how tools are designed (determinism, validation, governance, scaling, and UX constraints).  
Keep this list updated when the library changes.

### 🧭 Canonical KFM system docs (architecture, AI, UI, intake)
- **KFM Master Guide / v13 contracts** → `MARKDOWN_GUIDE_v13.md.gdoc`[^kfm_v13]
- **KFM system architecture & features** → `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf`[^wpe]
- **KFM technical documentation** → `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`[^sources_manifest]
- **KFM AI system overview** → `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf`[^focus_mode]
- **KFM UI system overview** → `Kansas Frontier Matrix – Comprehensive UI System Overview.pdf`[^ui_provenance_exports]
- **KFM data intake guide** → `📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf`[^immutability]
- **KFM latest ideas & proposals** → `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf`[^pmtiles_dual_pack]
- **KFM innovation roadmap** → `Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf`[^cultural_protocols]
- **Additional ideas / add-ons** → `Additional Project Ideas.pdf` (Pulse Threads, run manifests, OCI distribution, graph health checks)[^pulse_threads]

### 🧪 Scientific method & MCP receipts
- `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf` (hypotheses, methods, receipts, reproducibility)[^mcp_receipts]

### 🗺️ Geospatial + mapping hub design
- `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf` (MapLibre/Cesium, time slider, data hosting, DVC hints)[^maplibre_cesium][^dvc]

### 🧾 Standards + writing conventions
- `Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx` (advanced GitHub markdown patterns)[^markdown_guide]

### 📦 Reference portfolios (PDF Portfolios)
Some “bookshelves” are packaged as **PDF Portfolios** (Acrobat-style bundles). Tools should support extracting them to a normal folder for indexing/search.[^pdf_portfolios]

- `AI Concepts & more.pdf` *(PDF Portfolio)*[^pdf_portfolios]
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf` *(PDF Portfolio)*[^pdf_portfolios]
- `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf` *(PDF Portfolio)*[^pdf_portfolios]
- `Various programming langurages & resources 1.pdf` *(PDF Portfolio)*[^pdf_portfolios]

> [!TIP]
> Add a governed extractor like `tools/library/extract_pdf_portfolio.py` that emits:
> - extracted PDFs
> - `manifest.json` (filename, sha256, source portfolio, extracted_at)
> - optional: a local search index for docs (dev-only)

---

<a id="metadata"></a>
## 🧾 Metadata

```yaml
title: "tools/ — Kansas Frontier Matrix Toolchain"
path: "tools/README.md"
version: "v0.6.0"
last_updated: "2026-01-20"
review_cycle: "90 days"
governance: "FAIR + CARE aligned; sovereignty-aware"
pipeline_order: "Raw → Work/ETL → Processed → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → UI → Story Nodes → Focus Mode"
```

---

<a id="version-history"></a>
## 🕰️ Version history

| Version | Date | Summary | Author |
|---:|---|---|---|
| v0.6.0 | 2026-01-20 | Integrated the newest project ideas into the governed toolchain: added **run manifests + JSON canonicalization** (idempotent runs), **OCI artifact registry distribution** (ORAS + Cosign + digest pinning), **Pulse Threads + Concept Nodes** as governed content artifacts, **weekly graph health checks**, and the **GeoParquet + PMTiles dual-format packaging** pattern. Updated folder layout, QA matrix, and reference library to include all project files (including PDF portfolios). | KFM Engineering |
| v0.5.0 | 2026-01-19 | Updated `tools/` README to v13 staging (`data/raw|work|processed`), added Watcher–Planner–Executor agent toolchain guidance, strengthened provenance-first + citation-required Focus Mode rules, added telemetry/observability contract notes, and expanded offline pack/field ops expectations; refreshed reference library. | KFM Engineering |
| v0.4.0 | 2026-01-13 | Expanded `tools/` README using project reference library: added determinism levels, artifact QA matrix, stats evidence tooling, 3D/WebGL guidance, remote sensing + compression notes, federation framing (data spaces), and a clearer promotion ladder; updated reference library and canonical data staging. | KFM Engineering |
| v0.3.0 | 2026-01-11 | Aligned `tools/` README with Master Guide v13: contract-first + evidence-first; clarified canonical paths (`schemas/`, `src/*`, `web/`, `releases/`); added contracts section + federation readiness notes. | KFM Engineering |
| v0.2.0 | 2026-01-09 | Aligned `tools/` with repo-wide boundaries (src/scripts/mcp), added tool contract + data staging rules + QA rings + security posture + richer folder map. | KFM Engineering |
| v0.1.0 | 2026-01-08 | Initial toolbox README draft. | KFM Engineering |

---

## 📎 Evidence notes (footnotes)

[^kfm_v13]: v13 invariants and pipeline staging/canonical boundary artifacts (STAC/DCAT/PROV) + “no skipping stages.” [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^data_layout]: v13 data lifecycle layout and canonical folder paths for raw/work/processed plus catalogs/prov outputs. [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^stac_dcat_prov]: STAC/DCAT/PROV alignment and evidence-artifact treatment for derived/AI outputs; catalogs are required boundary artifacts before downstream stages. [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^focus_mode]: Focus Mode / AI outputs require citations and are constrained by governance/policy guardrails; prompts and answers are treated as governance-sensitive surfaces. [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:6‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
[^immutability]: Raw input data is treated as immutable/read-only evidence; transformations occur downstream and must be deterministic/config-driven for reproducibility. [oai_citation:7‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
[^streaming]: Federation and multi-region interoperability rely on standard STAC/DCAT/PROV outputs and shared governance posture; offline packs can bundle slices across regions with careful collation/governance. [oai_citation:8‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:9‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
[^sources_manifest]: `data/sources/` manifests are used to capture external source URL/license/schema and support provenance-first ingestion (without Git-versioning huge raw inputs). [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^policy_pack]: Policy-as-code posture and OPA/Conftest gates are part of KFM’s governance enforcement surface (license/classification/no-downgrade; deny-by-default where appropriate). [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^wpe]: Watcher–Planner–Executor pattern, PR-based automation, and attested outputs align with the “tools enforce the pipeline” governance intent. [oai_citation:13‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
[^prompt_gate]: Prompt security layers/Prompt Gate are explicitly described as part of AI safety and tool misuse hardening. [oai_citation:15‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
[^ui_provenance_exports]: UI surfaces provenance (“map behind the map”), is decoupled via APIs, and exports/shared views are intended to carry credits; supports reuse by other regions. [oai_citation:16‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) [oai_citation:17‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
[^pwa_offline]: UI/mobile strategy includes offline data packs and field use; system supports offline-first usage patterns. [oai_citation:18‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
[^offline_packs]: Offline mode considerations include packaging limited Focus Mode behavior only if policy permits on-device models; offline packs remain governed artifacts. [oai_citation:19‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
[^crs_wgs84]: WGS84 (EPSG:4326) standard and vector tile tooling (e.g., Tippecanoe) are called out for scalable web delivery, with reprojection tracked in provenance. [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^maplibre_cesium]: MapLibre for 2D and optional Cesium for 3D (3D Tiles/CZML) with time-slider storytelling patterns are part of the mapping/UI architecture options. [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
[^ar_mode]: AR guidance emphasizes filtering layers, avoiding clutter, and reusing existing endpoints with an AR client profile. [oai_citation:22‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
[^bulk_doc_ingest]: Bulk document ingestion roadmap includes OCR + metadata creation + linking into the graph (gated + provenance). [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
[^telemetry]: Telemetry is treated as a schema-first contract surface; validate payloads and keep privacy-aware logs. [oai_citation:24‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
[^mcp_receipts]: MCP emphasizes QA in CI, deterministic outputs/seed recording, and structured receipts/checklists for reproducibility and governance traceability. [oai_citation:25‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32) [oai_citation:26‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)
[^hilt]: Human-in-the-loop expectations for AI-assisted metadata/story generation; AI suggests, humans approve for important outputs. [oai_citation:27‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
[^cultural_protocols]: CARE-aligned and sovereignty-aware metadata (including cultural protocol labels such as TK labels) are proposed as governance practice areas. [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^sensitivity]: Sensitivity controls include location generalization, policy tags, and permission-based access; emphasizes consent and Indigenous data sovereignty expectations. [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^story_review]: Story validation / peer review concepts to reduce narrative drift and improve trust signals are proposed in KFM’s innovation roadmap. [oai_citation:30‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
[^kfm_sim]: Simulation outputs treated as evidence artifacts: config+seed captured, V&V and UQ summaries, and provenance/policy gates for publishability. [oai_citation:31‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^pdf_portfolios]: Several reference bundles are PDF Portfolios that require extraction for normal indexing/search; governed tooling should extract + manifest them. [oai_citation:32‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr) [oai_citation:33‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2) [oai_citation:34‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6) [oai_citation:35‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)
[^run_manifest]: KFM proposes `run_manifest.json` + canonical JSON hashing (RFC 8785/JCS style) to support idempotency, exact run identity, and robust provenance linking. [oai_citation:36‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)
[^oci_registry]: ORAS + Cosign + OCI registry distribution is proposed for big artifacts (PMTiles, GeoParquet) with digest pinning and referrer-attached signatures/SBOMs; catalogs include OCI distribution metadata. [oai_citation:37‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T) [oai_citation:38‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
[^pulse_threads]: Pulse Threads are proposed as a recurring, evidence-linked narrative artifact type with structured metadata and citation discipline. [oai_citation:39‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)
[^concept_nodes]: Conceptual Attention Nodes are proposed as governed “concept anchors” connecting domains, aliases, evidence, and policy constraints. [oai_citation:40‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^graph_health]: Weekly graph health check is proposed as a recurring integrity and governance practice to catch drift/orphans and emit auditable reports. [oai_citation:41‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
[^github_prov]: GitHub Actions reusable workflow is proposed to generate PROV from PRs/commits/workflow metadata, producing traceability artifacts for code-to-data provenance. [oai_citation:42‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
[^pmtiles_dual_pack]: KFM proposes dual geospatial packaging: GeoParquet for analytics and PMTiles for web/offline delivery, with STAC/DCAT records linking both distributions. [oai_citation:43‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
[^tile_postgis]: PostGIS adapter serves tiles via SQL templates like `ST_AsMVT`; emphasizes “PostGIS stores geo truth, catalogs describe assets, graph links context,” and mentions PMTiles/GeoParquet proposals in this ecosystem. [oai_citation:44‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
[^ml_metrics]: Macro-averaged precision/recall/F1 definitions are cited as useful for imbalanced classification reporting and governance-friendly evaluation summaries.
[^energy_telemetry]: KFM proposes tracking sustainability metrics (energy consumption / carbon footprint) as part of system observability and quality monitoring. [oai_citation:45‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
[^markdown_guide]: Advanced GitHub Markdown patterns (callouts, Mermaid diagrams, tables) are referenced as writing conventions for consistent docs and run reports. [oai_citation:46‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
[^dvc]: Mapping hub design proposes using DVC (or similar) to manage large data artifacts outside Git while maintaining reproducible pointers and workflow discipline. [oai_citation:47‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)
[^story_manifest]: Story Nodes are proposed to pair narrative text with structured evidence manifests and PROV links so CI can validate citation integrity and maintain auditability. [oai_citation:48‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)