# 🧰 `api/scripts/_lib` — Shared Utilities for Script Land

![Scope](https://img.shields.io/badge/scope-api%2Fscripts-blue)
![Contract-first](https://img.shields.io/badge/contract--first-yes-2ea44f)
![Deterministic](https://img.shields.io/badge/deterministic-runs-orange)
![Evidence-first](https://img.shields.io/badge/evidence--first-STAC%2FDCAT%2FPROV-7b68ee)
![Security](https://img.shields.io/badge/security-defense--minded-red)

> [!NOTE]
> **What this folder is:** a small “standard library” for everything under `api/scripts/` so scripts stay **small, focused, repeatable** (CLI/Makefile-invoked steps) instead of becoming copy‑pasted snowflakes. The upstream architecture explicitly frames the ingestion/processing layer as “scripts and tools” that fetch, convert, OCR/parse, and standardize data with traceable metadata. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## 🧭 Quick Nav

- [🎯 Goals](#-goals)
- [🚦 Non‑negotiables](#-nonnegotiables)
- [✅ What belongs in `_lib`](#-what-belongs-in-_lib)
- [🗂️ Suggested layout](#️-suggested-layout)
- [🧩 Core building blocks](#-core-building-blocks)
- [🧪 Testing & QA](#-testing--qa)
- [🔐 Security & governance](#-security--governance)
- [🧱 Adding a new utility](#-adding-a-new-utility)
- [📚 Reference shelf](#-reference-shelf)
- [📖 Glossary](#-glossary)

---

## 🎯 Goals

This `_lib` exists to make scripts:

1. **Contract‑first + deterministic**  
   Scripts should behave the same way given the same config + inputs, and should treat schemas/contracts as the source of truth. :contentReference[oaicite:2]{index=2}

2. **Evidence‑first (catalogs before graph/UI)**  
   The system expects a strict ordering where ETL produces **catalog artifacts (STAC/DCAT/PROV)** *before* graph enrichment and long before UI consumption. :contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}

3. **Provenance by default**  
   Every run should emit traceable metadata (where data came from, what happened to it, and what got produced). The design docs explicitly call for STAC-like catalogs enumerating source URLs/refs, spatial reference, temporal coverage, and processing steps. :contentReference[oaicite:5]{index=5}

4. **Safe to operate**  
   The API boundary is where redaction/classification must be applied; scripts should not “publish to UI” directly. :contentReference[oaicite:6]{index=6}  
   Future proposals also emphasize provenance logs and governance-oriented automation. :contentReference[oaicite:7]{index=7}

---

## 🚦 Non‑negotiables

> [!IMPORTANT]
> If you only remember one thing: **scripts emit evidence artifacts first** and **everything UI-facing goes through the API boundary**.

### 🔒 Invariants this folder must reinforce

- **Pipeline order stays intact**:  
  `ETL/Scripts → Catalogs (STAC/DCAT/PROV) → Graph → API → UI` :contentReference[oaicite:8]{index=8}

- **Graph references catalogs/evidence (not raw blobs)**  
  Graph nodes should point to STAC/DCAT/provenance artifacts rather than “mystery files.” :contentReference[oaicite:9]{index=9}

- **API boundary**  
  Anything served to the UI must go through the API layer so redaction and classification propagation can happen. :contentReference[oaicite:10]{index=10}

- **Documentation is part of the system**  
  Project docs explicitly favor emoji-friendly, scan‑able markdown with code snippets and citations; this README follows that style. :contentReference[oaicite:11]{index=11}

---

## ✅ What belongs in `_lib`

### ✅ Put it here if it is…

- Reused by **2+ scripts** (or will be reused soon)
- Generic plumbing: config, logging, retries, hashing, paths, CLI helpers
- Provenance + evidence artifacts: STAC/DCAT/PROV utilities, run manifests, checksums
- DB/Graph clients with safe defaults (timeouts, retries, parameterization)
- Geospatial primitives: bbox, GeoJSON validation, CRS handling, tile math
- Policy helpers: policy evaluation, redaction, access rules, “publish gate”

### 🚫 Don’t put it here if it is…

- A one-off dataset transform only used once
- API route handlers / server business logic (keep server code separate)
- Notebook-only experimentation
- UI code

---

## 🗂️ Suggested layout

> [!TIP]
> The broader project layout separates pipelines, tools/validation, models, etc. Treat `_lib` as shared glue — not as “where all code goes.” :contentReference[oaicite:12]{index=12}

```text
api/scripts/_lib/
  README.md

  cli/                # argparse/commander wrappers, standard flags, help text
  config/             # config loading, schema validation, env overlays
  log/                # structured logging, run context, redaction
  io/                 # paths, filesystem, caching, atomic writes
  hash/               # content hashing, checksums, deterministic IDs
  geo/                # bbox, CRS helpers, GeoJSON, raster/vector IO helpers
  catalog/            # STAC/DCAT/PROV builders + validators
  provenance/         # run manifests, lineage events (OpenLineage-style)
  db/                 # Postgres/PostGIS helpers
  graph/              # graph writes that reference catalogs (no raw data)
  security/           # policy pack hooks, secret handling, access rules

  testing/            # fixtures + helpers to keep scripts testable
```

> [!NOTE]
> Names are a suggestion; pick idioms that match the language/runtime used in `api/scripts/`.

---

## 🧩 Core building blocks

### 1) 🧾 Run Context (the “envelope”)

Every script should begin by constructing a `RunContext` capturing:

- `run_id` (UUID)
- script name + version (git SHA or release tag)
- config hash
- inputs: URIs + checksums
- outputs: paths + checksums
- timestamps + duration
- policy decisions (if any)

Why: proposals call for stable run identifiers and auditable event trails (e.g., OpenLineage-style events). :contentReference[oaicite:13]{index=13}

---

### 2) 📦 Evidence artifacts (STAC/DCAT/PROV)

Scripts should write boundary artifacts that other layers can safely reference:

- **STAC-like** metadata for geospatial layers (bbox/time/source) :contentReference[oaicite:14]{index=14}
- **Catalog entries** describing source URLs/refs, coordinate system, processing steps :contentReference[oaicite:15]{index=15}
- **PROV lineage**: activities, entities, agents (or a pragmatic equivalent)

> [!IMPORTANT]
> The graph should link to these artifacts, not to ad-hoc files. :contentReference[oaicite:16]{index=16}

---

### 3) ♻️ Idempotency + determinism

Recommended patterns:

- Deterministic output paths based on `(config_hash + input_hash)`
- `--dry-run` and `--force` flags in every script
- Idempotency keys for “write once” operations
- Safe retries for network I/O

Future proposals explicitly describe idempotent, traceable pipelines with idempotency keys and “kill switch” controls. :contentReference[oaicite:17]{index=17}

---

### 4) 🧵 “Small scripts, big pipeline”

The design document suggests scripts remain **small and focused** and are invoked via CLI/Makefile as core pipeline steps. :contentReference[oaicite:18]{index=18}

This implies `_lib` should:

- make the happy path easy (templates + helpers)
- make “doing the wrong thing” annoying (guardrails)

---

## 🚀 Script template (copy/paste starter)

> [!NOTE]
> This is intentionally language‑agnostic pseudocode. Swap in your actual runtime (Python/Node/etc).

### CLI contract (recommended)
- `--config <file>`
- `--run-id <uuid|auto>`
- `--dry-run`
- `--force`
- `--log-json` (machine-readable logs)
- `--out <dir>`

### Golden path pseudocode

```text
1) ctx = create_run_context()
2) cfg = load_config_and_validate(cfg_schema)
3) policy = evaluate_policy(cfg, inputs)
4) emit_run_manifest(status="started")
5) run_work()
6) write_catalog_artifacts(STAC/DCAT/PROV)
7) emit_run_manifest(status="completed")
```

### Provenance manifest example

```json
{
  "run_id": "6c9b9c8a-2c6d-4d7b-a6c7-51b222f4d3c1",
  "script": "build_cog_tiles",
  "version": "git:abc1234",
  "config_hash": "sha256:...",
  "inputs": [{"uri": "s3://.../source.tif", "checksum": "sha256:..."}],
  "outputs": [{"path": "data/processed/.../layer.cog.tif", "checksum": "sha256:..."}],
  "started_at": "2026-01-12T00:00:00Z",
  "ended_at": "2026-01-12T00:02:10Z",
  "policy": {"decision": "allow", "rules": ["license_ok", "no_pii"]}
}
```

---

## 🧪 Testing & QA

> [!TIP]
> Treat scripts like production code: tests, validation, and quality gates.

Recommended test layers:

- **Unit tests**: fast, no network, deterministic fixtures
- **Integration tests**: containerized Postgres/Neo4j where needed
- **Catalog QA**: validate STAC/DCAT/PROV output schemas + invariants

The technical documentation calls out `tools/validation/*` and catalog/data QA tooling (e.g., schema validators, integrity checks, map QA). :contentReference[oaicite:19]{index=19}

---

## 🔐 Security & governance

### 🔑 Secrets & credentials
- Secrets come from env variables or a secret manager
- Never print tokens/keys; `_lib/log` should redact by default
- Prefer least privilege for DB/API credentials

### 🛂 Policy enforcement hooks
Proposals discuss policy packs (OPA/Rego etc.), signing/attestation, and structured lineage events for auditability. Use `_lib/security` as the standard integration point so scripts don’t “roll their own.” :contentReference[oaicite:20]{index=20}

### 🧯 Defensive security only
The project includes security references (ethical hacking / reverse engineering). They are here for **defensive hardening**, validation, and safe operations — not offensive misuse.

---

## 🧱 Adding a new utility

✅ **Definition of done** checklist:

- [ ] Name communicates intent (verb‑noun, or domain‑noun)
- [ ] Single responsibility
- [ ] Deterministic (outputs depend on args/config only)
- [ ] Side effects are explicit and testable
- [ ] Structured logging + redaction
- [ ] Unit tests added
- [ ] Minimal usage snippet added to this README (or local module README)
- [ ] If it writes artifacts: adds/updates schema + validation rules

---

## 📚 Reference shelf

> [!NOTE]
> This section is intentionally exhaustive: it’s the shared “project bookshelf” that informs how `_lib` should evolve.

<details>
<summary>📖 Expand the full project file list</summary>

### 🧠 Core architecture & internal docs
- `MARKDOWN_GUIDE_v13.md.gdoc` (contract-first, deterministic, evidence artifacts) :contentReference[oaicite:21]{index=21}
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx` (repo layout, QA tools, doc style) :contentReference[oaicite:22]{index=22}
- `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx` (policy automation, provenance logs, idempotency) :contentReference[oaicite:23]{index=23}
- `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf` (ingestion scripts, STAC-like catalog, modular layers) :contentReference[oaicite:24]{index=24}

### 🛰️ Geospatial, cartography, remote sensing
- `python-geospatial-analysis-cookbook.pdf`
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`

### 📈 Statistics, modeling, analysis
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `Understanding Statistics & Experimental Design.pdf`
- `regression-analysis-with-python.pdf`
- `Regression analysis using Python - slides-linear-regression.pdf`
- `graphical-data-analysis-with-r.pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`

### 🗄️ Data management & systems engineering
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `Scalable Data Management for Future Hardware.pdf` (performance/streaming patterns) :contentReference[oaicite:25]{index=25}
- `Data Spaces.pdf`
- `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`

### 🧩 Algorithms & theory (graphs/optimization)
- `Spectral Geometry of Graphs.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`

### 🕸️ UI & media pipeline (used by scripts that precompute assets)
- `responsive-web-design-with-html5-and-css3.pdf`
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

### ⚖️ Governance, ethics, law, security mindset
- `Introduction to Digital Humanism.pdf`
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`
- `Principles of Biological Autonomy - book_9780262381833.pdf`

### 🧱 Programming compendiums (broad reference library)
- `A programming Books.pdf`
- `B-C programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`

</details>

---

## 📖 Glossary

- **STAC**: SpatioTemporal Asset Catalog (metadata for geospatial assets)
- **DCAT**: Data Catalog Vocabulary (dataset catalog metadata)
- **PROV**: Provenance (lineage: what produced what, using which inputs)
- **COG**: Cloud Optimized GeoTIFF (web-friendly georaster format)
- **Idempotency**: repeated runs don’t create duplicates or corrupt state
- **Evidence artifact**: an output that other layers can reference safely (schema’d, validated, traceable)

---

> [!FOOTNOTE]
> This README is intentionally strict: it’s a guardrail for a provenance-first, reproducible pipeline culture aligned with the project’s modular architecture goals. :contentReference[oaicite:26]{index=26}:contentReference[oaicite:27]{index=27}

