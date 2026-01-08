<div align="center">

# 🧪 QA Validation Gates — Kansas Frontier Matrix (KFM)
**Fail‑Closed · Evidence‑First · Governed Artifacts**

<img alt="Gates" src="https://img.shields.io/badge/QA-Validation%20Gates-blue" />
<img alt="CI" src="https://img.shields.io/badge/CI-GitHub%20Actions-black" />
<img alt="GIS" src="https://img.shields.io/badge/GIS-PostGIS%20%2B%20STAC-green" />
<img alt="Graph" src="https://img.shields.io/badge/Graph-Neo4j-orange" />
<img alt="Supply Chain" src="https://img.shields.io/badge/Supply%20Chain-SBOM%20%2B%20Sigstore-7b1fa2" />
<img alt="Governance" src="https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-gold" />

</div>

This spec defines **KFM’s validation gates**: the checks that MUST pass before a change can be **merged**, **released**, or **deployed**.

It is designed for KFM’s architecture: data ingestion & ETL → STAC/DCAT/PROV catalogs → PostGIS + Neo4j → models/simulations → APIs → WebGL map UI + Story Nodes (human-readable narratives).

---

## 🎯 Objectives

Validation gates MUST ensure that:

- 🧾 **Every promoted artifact is evidence-backed** (machine-readable reports + checksums).
- 🧭 **Metadata is complete & interoperable** (STAC/DCAT/PROV aligned).
- 🗺️ **Geospatial products are correct** (CRS, geometry validity, tiling, extents).
- 🕸️ **Graph products are consistent** (stable IDs, relationship integrity, provenance links).
- 🤖 **ML outputs are reproducible & evaluated** (no silent degradation; bias checks where applicable).
- 🎛️ **Simulation outputs are credible** (verification, validation, uncertainty discipline).
- 🖥️ **UI & visualization outputs are trustworthy** (render sanity + accessibility + asset integrity).
- 🔐 **Supply chain integrity is enforced** (SBOM + signing + provenance attestations).
- ⚖️ **Governance is enforceable** (FAIR+CARE checks + licensing + audit trails).

> ✅ Policy stance: gates are **fail‑closed** for governed artifacts. If the system can’t prove an artifact is valid, it **does not promote** it.

---

## 🧩 Gate tiers (when checks run)

| Tier | Nickname | Runs on | Goal | Typical runtime |
|---:|---|---|---|---|
| T0 | 🏎️ Local | dev machine / pre-commit | fast feedback | seconds–minutes |
| T1 | 🧱 PR Gate | pull request | block unsafe merges | minutes |
| T2 | 🧪 RC Gate | release candidate | verify release package | minutes–hours |
| T3 | 📦 Release Gate | tagged release | produce governed evidence bundle | minutes–hours |
| T4 | 🚀 Deploy Gate | deployment pipeline | enforce policy at the edge | minutes |

---

## 🗂️ Gate outputs (what “passing” means)

Every gate MUST produce a **structured result**, even if it passes.

**Required output formats (choose per suite):**
- `json` / `ndjson` for metrics & validation details
- `junit.xml` for test runners
- `sarif` for security scanners
- `markdown` summary for humans (optional, never the only artifact)

**Self-validation suite taxonomy (recommended)**
- `core/` 🧼 (lint/tests/docs)
- `security/` 🔐 (scan/secret/license)
- `data/` 🗃️ (contracts/quality)
- `catalog/` 🛰️ (STAC/DCAT/PROV)
- `geospatial/` 🗺️ (CRS/geometry/tiles)
- `db/` 🐘 (migrations/queries)
- `graph/` 🕸️ (constraints/cross-links)
- `pipeline/` 🔄 (freshness/idempotency)
- `stats/` 📈 (diagnostics)
- `ml/` 🤖 (eval/model cards)
- `simulation/` 🎛️ (V&V/UQ)
- `ui/` 🖥️ (render/a11y/assets)
- `perf/` ⚡ (load/SLO)
- `supply-chain/` 📦 (SBOM/signing/attest)
- `governance/` ⚖️ (FAIR+CARE/audit)

**Evidence root:**
- `docs/reports/self-validation/<suite>/<run_id>/...`  🧾

> 🧠 Retention posture (for governed releases): keep evidence **permanently**, record SHA‑256 in SBOM, and schedule quarterly governance review.

---

## 🧱 Gate taxonomy

Each gate is defined by:

- **Gate ID**: `G-<domain>-<number>` (stable identifier)
- **Tier(s)**: which tiers must run it
- **Trigger**: what file/path changes invoke it
- **Input contract**: schemas and invariants
- **Pass criteria**: explicit thresholds (no hidden pass/fail rules)
- **Evidence artifacts**: file paths for auditability
- **Owner**: who maintains the checks and thresholds
- **Waiver rules**: how exceptions work (time-boxed, logged, reviewed)

---

## 🧭 Gate matrix (summary)

| Gate ID | Name | Tiers | Blocks | What it validates |
|---|---|---:|---|---|
| G-CORE-00 | 🧼 Repo hygiene | T0–T1 | Merge | formatting, lint, unit tests, docs lint |
| G-SEC-10 | 🔐 Dependency + secrets | T0–T3 | Merge/Release | vuln scan, secrets, license allowlist |
| G-DATA-20 | 🗃️ Data contract & schema | T0–T2 | Merge/RC | schema, completeness, drift, provenance fields |
| G-CAT-30 | 🛰️ STAC/DCAT/PROV quick gate | T1–T3 | Merge/Release | required catalog fields, link health, profiles |
| G-GEO-40 | 🗺️ Geospatial integrity | T1–T3 | Merge/Release | CRS, geometry validity, extents, tiling |
| G-DB-50 | 🐘 PostGIS migrations & queries | T1–T3 | Merge/Release | migrations, query plans, spatial indexes |
| G-GRAPH-60 | 🕸️ Neo4j graph integrity | T1–T3 | Merge/Release | IDs, cardinality, provenance edges, cross-links |
| G-PIPE-70 | 🔄 Pipeline freshness & idempotency | T1–T3 | Merge/Release | freshness windows, replay safety, kill-switch |
| G-STATS-80 | 📈 Statistical QA | T1–T3 | Merge/Release | regression diagnostics, experiment validity |
| G-ML-90 | 🤖 Model promotion | T1–T3 | Merge/Release | eval thresholds, bias checks, canary, rollback |
| G-SIM-100 | 🎛️ Simulation credibility | T1–T3 | Merge/Release | V&V, UQ, scenario regression tests |
| G-UI-110 | 🖥️ UI/WebGL/assets | T1–T3 | Merge/Release | render sanity, a11y, legends/symbols integrity |
| G-PERF-120 | ⚡ Performance & scalability | T2–T4 | Deploy | SLO budgets, load tests, concurrency limits |
| G-SC-130 | 📦 Supply chain integrity | T2–T4 | Release/Deploy | SBOM, signing, provenance attestations, policy |
| G-GOV-140 | ⚖️ Governance & ethics | T1–T4 | Merge/Deploy | FAIR+CARE checks, licensing, audit logs |

---

## 🧾 Gate definitions (normative)

### G-CORE-00 — 🧼 Repo hygiene (T0–T1)

**Trigger:** any code/docs change.

**Checks**
- ✅ formatting (language-specific)
- ✅ lint (language-specific)
- ✅ unit tests (pytest for Python; equivalent for other languages)
- ✅ docs lint + link checks (best-effort, fail on broken internal links)

**Pass criteria**
- zero failing tests
- no lint errors above configured severity
- no broken internal links

**Evidence**
- `docs/reports/self-validation/core/<run_id>/junit.xml`
- `docs/reports/self-validation/core/<run_id>/lint.json`

**Notes**
- KFM’s engineering design emphasizes TDD, integration tests, and end-to-end UI tests (Selenium/Playwright patterns). Keep unit tests fast; keep integration tests deterministic.

---

### G-SEC-10 — 🔐 Dependency + secrets + license (T0–T3)

**Trigger:** changes to dependency manifests, container build files, workflow files, secrets/config, or vendor code.

**Checks**
- 🧯 dependency vulnerability scan (SBOM-assisted where possible)
- 🕵️ secret scanning (repo + CI environment guardrails)
- ⚖️ license allowlist enforcement for dependencies and datasets

**Pass criteria**
- no high/critical vulnerabilities without documented mitigation or waiver
- no leaked secrets (hard fail)
- license policy passes for governed artifacts

**Evidence**
- `docs/reports/self-validation/security/<run_id>/sarif/*.sarif`
- `docs/reports/self-validation/security/<run_id>/licenses.json`

> ⚠️ Defensive posture only: security references in the library include offensive techniques. QA gates must focus on prevention, scanning, and hardening.

---

### G-DATA-20 — 🗃️ Data contract & schema validation (T0–T2)

**Trigger:** changes under `data/`, `pipelines/`, `schemas/`, `tools/ingest/`, or new datasets.

**Checks (minimum)**
- 🧱 schema validation (JSON Schema / Avro / Pydantic—project choice)
- 🧮 completeness thresholds (required fields, null-rate limits)
- 📉 drift detection (distribution changes, new categories)
- 🧬 provenance fields present (`source`, `created_at`, `run_id`, `commit_sha`, `license`)

**Pass criteria**
- schema: 100% valid
- completeness: meets dataset policy thresholds (declared per dataset)
- drift: any detected drift is either (a) expected and documented, or (b) blocks promotion

**Evidence**
- `docs/reports/self-validation/data/<run_id>/schema_report.json`
- `docs/reports/self-validation/data/<run_id>/quality_metrics.json`

---

### G-CAT-30 — 🛰️ STAC/DCAT/PROV quick gate (T1–T3)

**Trigger:** changes to `data/stac/**`, `data/catalog/**`, `data/prov/**` or any artifact referenced by catalog links.

**Checks**
- ✅ required STAC keys exist for `catalog.json` and every `collection.json`:
  - `license` (non-empty string)
  - `providers` (non-empty array)
  - `stac_extensions` (array; warn if empty, **fail if missing**)
- 🔗 link health for top-level `links[].href` (fail on broken internal links; configurable for external)
- 🧾 DCAT presence for dataset-level discovery (profile-based)
- 🧬 PROV presence for lineage (profile-based)

**Pass criteria**
- required keys present for all validated entities
- link check passes per policy
- profiles pass per configured schema

**Evidence**
- `docs/reports/self-validation/catalog/<run_id>/catalog_qa.json`
- `docs/reports/self-validation/catalog/<run_id>/linkcheck.json`

**Implementation pointers**
- `tools/validation/catalog_qa/run_catalog_qa.py` (reference implementation idea)
- `.github/workflows/catalog-qa.yml` (CI hook)

---

### G-GEO-40 — 🗺️ Geospatial integrity (T1–T3)

**Trigger:** new/changed geospatial assets (vector/raster/tiles), map styles, or pipeline steps that generate them.

**Checks**
- 🧭 CRS correctness (declared + consistent)
- 🧩 geometry validity (no self-intersections, valid rings)
- 🧱 extent correctness (bbox/geometry align with file)
- 🧊 tile grid integrity (no gaps/overlaps unless intentional)
- 🛰️ raster checks (nodata rules, dtype rules, COG compliance if used)

**Pass criteria**
- 100% invalid geometries must be fixed or explicitly quarantined (with rationale)
- CRS must be explicit and pass allowlist
- tilesets must pass integrity checks (configurable tolerance only with waiver)

**Evidence**
- `docs/reports/self-validation/geospatial/<run_id>/geo_validation.json`

---

### G-DB-50 — 🐘 PostGIS migrations & query integrity (T1–T3)

**Trigger:** changes to DB migrations, schema, indexes, or query layer.

**Checks**
- 🔁 migrations apply cleanly on empty + seeded DB
- 🧭 spatial indexes exist for high-cardinality geometry columns
- 🧪 query regression tests for known critical queries (counts, boundaries, filters)
- ⚡ plan budgets (EXPLAIN ANALYZE) for a small set of representative queries

**Pass criteria**
- migrations: pass in CI, idempotency where required
- query regression: within tolerances
- plan budgets: no unexpected sequential scans on large spatial tables (unless justified)

**Evidence**
- `docs/reports/self-validation/db/<run_id>/migration_log.txt`
- `docs/reports/self-validation/db/<run_id>/query_regression.json`

---

### G-GRAPH-60 — 🕸️ Neo4j graph integrity (T1–T3)

**Trigger:** graph schema changes, ontology changes, ETL that writes nodes/edges, or Story Node bindings.

**Checks**
- 🆔 stable ID rules (no accidental regeneration of identifiers)
- 🔗 relationship integrity (required edges present; no forbidden cycles where defined)
- 🧬 provenance edges exist (source → process → artifact → node)
- 🔄 cross-links remain consistent (catalog IDs ↔ graph node IDs ↔ API IDs)

**Pass criteria**
- no orphan nodes violating constraints
- cardinality constraints pass
- provenance completeness meets policy

**Evidence**
- `docs/reports/self-validation/graph/<run_id>/graph_constraints.json`

---

### G-PIPE-70 — 🔄 Pipeline freshness & idempotency (T1–T3)

**Trigger:** pipeline DAG changes (e.g., LangGraph YAML), ingestion code, schedules, or upstream endpoint configs.

**Checks**
- 🕒 freshness windows: detects stale data vs expected update cadence
- ♻️ idempotency: re-running does not duplicate outputs (stable keys)
- 🧾 catalog output invariants: new/updated records MUST produce updated STAC Items/Collections (when applicable)
- 🕸️ graph sync invariants: when the pipeline writes to Neo4j, catalog IDs ↔ node IDs MUST stay consistent
- 🚦 fail-closed promotion gate: no artifacts → no promotion; missing license/provenance → no promotion
- 🧯 kill-switch pattern: repo/org/global toggle to stop promotions & scheduled runs

**Hazards Refresh (v11) specialization (when applicable)** 🌪️🔥🌊  
When validating the autonomous hazards pipeline, additional checks SHOULD be enabled:
- Upstream reachability: NOAA Storm Events, NWS warnings polygon feeds, FEMA declarations, USGS earthquakes, satellite wildfire detections
- Normalization correctness: event types map to controlled vocabularies
- STAC emission: each event produces/updates a STAC Item with spatial/temporal bounds
- Checksum validation: output artifacts verify against recorded digests
- Neo4j sync: hazard events appear as nodes with required ontology labels/edges (time + geometry)
- No silent skips: if a required upstream source is unavailable, the run MUST record it and fail promotion unless waived

**Pass criteria**
- freshness is within policy (or blocks)
- idempotency tests pass
- promotion policy returns ALLOW

**Evidence**
- `docs/reports/self-validation/pipeline/<run_id>/freshness.json`
- `docs/reports/self-validation/pipeline/<run_id>/idempotency.json`
- `docs/reports/self-validation/pipeline/<run_id>/policy_decision.json`
- `docs/reports/self-validation/pipeline/<run_id>/upstream_status.json` (hazards specialization)
- `docs/reports/self-validation/pipeline/<run_id>/graph_sync.json` (if Neo4j sync occurs)

---

### G-STATS-80 — 📈 Statistical QA (T1–T3)

**Trigger:** changes to statistical analyses, regression models, dashboards that surface statistical claims, or simulation calibration.

**Checks**
- 🧾 assumption checks appropriate to the method (e.g., residual structure, heteroscedasticity)
- 📉 diagnostics generated (residual plots, influence metrics, outlier handling policy)
- 🧪 experimental design validity checks where applicable (randomization, controls, leakage)

**Pass criteria**
- diagnostics exist and pass thresholds (declared)
- violations require either model adjustment or documented waiver

**Evidence**
- `docs/reports/self-validation/stats/<run_id>/diagnostics.json`
- `docs/reports/self-validation/stats/<run_id>/plots/` (optional images)

> Tip: treat “statistical regression tests” as first-class gates: if a retrained model’s metrics degrade beyond tolerance, block promotion.

---

### G-ML-90 — 🤖 Model promotion gate (T1–T3)

**Trigger:** training code changes, feature changes, new model artifacts, or evaluation config changes.

**Checks**
- 🧬 reproducibility: pinned config + dataset snapshot + commit SHA recorded
- ✅ evaluation: metrics computed on held-out sets + canary slices (spatial/temporal)
- 🧪 bias/fairness checks (where human-impactful or demographic proxies exist)
- 🔙 rollback readiness: prior model reference + alias swap strategy documented

**Pass criteria**
- metrics meet thresholds (declared per model)
- fairness checks meet thresholds (or waiver)
- rollback instructions exist and are tested in a dry-run

**Evidence**
- `docs/reports/self-validation/ml/<run_id>/model_card.md`
- `docs/reports/self-validation/ml/<run_id>/eval.json`
- `docs/reports/self-validation/ml/<run_id>/canary_eval.json`

---

### G-SIM-100 — 🎛️ Simulation credibility (V&V + UQ) (T1–T3)

**Trigger:** simulation engine changes, scenario configs, calibration inputs, solver updates, optimization changes.

**Checks**
- ✅ verification: units, boundary conditions, convergence sanity checks
- ✅ validation: compare to reference datasets / accepted benchmarks
- 🎲 uncertainty: sensitivity analysis & uncertainty reporting for key outputs
- 🔁 regression: canonical scenarios must remain stable within tolerance

**Pass criteria**
- V&V documented and re-runnable
- scenario regressions within tolerance
- uncertainty disclosures exist for any public-facing output

**Evidence**
- `docs/reports/self-validation/simulation/<run_id>/vv_report.json`
- `docs/reports/self-validation/simulation/<run_id>/uq_summary.json`

---

### G-UI-110 — 🖥️ UI / WebGL / legends & assets (T1–T3)

**Trigger:** UI code, styles, WebGL shaders, map styles, legends/symbols, Story Node visual bindings, image assets.

**Checks**
- 📱 responsive checks across breakpoints (layout invariants)
- 🧭 map render sanity (style loads, tiles load, layer ordering)
- 🧊 WebGL stability checks (context loss handling, fallback messaging)
- ♿ accessibility checks (keyboard nav, contrast, alt text where relevant)
- 🧾 legend/symbology integrity:
  - JSON schema validation
  - file existence checks (SVG/PNG)
  - STAC conformance for legend metadata
  - Story Node binding validation
  - CARE/ecological neutrality checks (if applicable)
  - optional snapshot comparisons

**Pass criteria**
- critical routes render without console errors
- a11y checks pass at configured severity
- legend validation passes

**Evidence**
- `docs/reports/self-validation/ui/<run_id>/ui_smoke.json`
- `docs/reports/self-validation/ui/<run_id>/a11y.json`
- `docs/reports/self-validation/ui/<run_id>/legend_validation.json`
- `docs/reports/self-validation/ui/<run_id>/screenshots/` (optional)

---

### G-PERF-120 — ⚡ Performance & scalability (T2–T4)

**Trigger:** release candidates, deployments, major query or rendering changes.

**Checks**
- 📏 SLO budgets (p95 latency, time-to-first-map, tile load time)
- 🧵 concurrency budgets (job queue depth, DB connection pools)
- 🧠 cache behavior sanity (hit rates, invalidation)
- 🧯 brownout behavior (reduced concurrency) before total failure

**Pass criteria**
- meets declared SLO budgets
- no regressions beyond tolerance
- concurrency limits enforced

**Evidence**
- `docs/reports/self-validation/perf/<run_id>/loadtest.json`

---

### G-SC-130 — 📦 Supply chain integrity (SBOM + signing + attestations) (T2–T4)

**Trigger:** releases, deployments, publication of any governed artifact.

**Checks**
- 📜 SBOM generated and referenced (SPDX recommended)
- 🧾 manifest inventory includes every governed artifact with SHA‑256
- ✍️ signatures created and verified by digest (keyless signing preferred)
  - keyless (OIDC) signing where feasible
  - record identity (issuer/workflow) + transparency log reference (e.g., Rekor) into attestations
- 🧬 provenance attestations reference artifact digests (SLSA-like)
- 🧱 policy check (OPA/Conftest or equivalent) enforces “no signature/no deploy”

**Pass criteria**
- SBOM present
- inventory complete
- signatures verified
- provenance attestation verified
- policy decision = ALLOW

**Evidence**
- `docs/reports/self-validation/supply-chain/<run_id>/sbom.spdx.json`
- `docs/reports/self-validation/supply-chain/<run_id>/manifest.json`
- `docs/reports/self-validation/supply-chain/<run_id>/attestation.jsonl`
- `docs/reports/self-validation/supply-chain/<run_id>/verify.json`

---

### G-GOV-140 — ⚖️ Governance & ethics (FAIR + CARE) (T1–T4)

**Trigger:** new/changed datasets, catalogs, Story Nodes, public narratives, models used in decision support.

**Checks**
- 🧾 licensing explicit (dataset + derived artifacts)
- 🧭 FAIR: findable IDs, accessible links, interoperable schemas, reusable provenance
- 🤝 CARE: community/ethical constraints encoded as metadata/policy where relevant
- 🧯 risk classification for sensitive layers (restrict or label)
- 🧾 audit logging for promotions and waivers

**Pass criteria**
- governance metadata complete
- policy decisions recorded
- sensitive outputs labeled and/or restricted per policy

**Evidence**
- `docs/reports/self-validation/governance/<run_id>/fair_care.json`
- `docs/reports/self-validation/governance/<run_id>/audit_log.jsonl`

---

## 📦 Evidence bundle spec (release-grade)

Every governed release SHOULD produce an evidence bundle:

```
releases/<tag>/
├── 📦 MANIFEST.json              # all artifacts + digests + sizes + types
├── 📜 SBOM.spdx.json             # dependency inventory
├── 🧬 ATTESTATIONS.jsonl         # provenance (build + run)
├── ✍️ SIGNATURES/                # signature artifacts / verification outputs
└── 🧾 REPORTS/                   # copied or referenced QA reports
```

### Minimal MANIFEST.json example

```json
{
  "release": "v11.2.6",
  "created_at": "2026-01-08T00:00:00Z",
  "artifacts": [
    {
      "id": "stac:kfm-hazards/collection.json",
      "type": "stac-collection",
      "path": "data/stac/hazards/collection.json",
      "sha256": "…",
      "license": "CC-BY-4.0",
      "prov_ref": "data/prov/hazards_run_2026-01-08.jsonld"
    }
  ]
}
```

---

## 🧯 Waivers (exception handling)

Waivers are allowed **only** when:

- the risk is understood and documented
- the waiver is time-boxed (expiry date)
- compensating controls exist (e.g., quarantined dataset, labeled layer, blocked deploy)

**Waiver record (MUST)**
- gate ID(s) waived
- scope (paths/artifacts affected)
- reason + risk assessment
- approver
- expiry + review date
- link to issue/ticket

Suggested location:
- `docs/reports/waivers/<waiver_id>.md` 📌

---

## 🗺️ Appendix A — Folder layout (with emojis)

```text
docs/specs/qa/
├── 📄 README.md
├── 🧪 QA__VALIDATION_GATES.md
├── 🧾 suites/
│   ├── 🛰️ stac-dcat-proc.md
│   ├── 🕸️ graph-neo4j.md
│   ├── 🗺️ geospatial-crs-tiles.md
│   ├── 🤖 ml-model-promotion.md
│   ├── 🖥️ ui-visual-regression.md
│   └── 🔐 supply-chain-signing.md
├── ✅ checklists/
│   ├── 🔀 pr-gate.md
│   ├── 🗃️ dataset-ingest.md
│   ├── 📦 model-release.md
│   └── 🌐 ui-release.md
├── 🧩 templates/
│   ├── 🧪 qa-suite.template.md
│   ├── 🧾 qa-report.template.md
│   └── 🪪 model-card.template.md
└── 📟 runbooks/
    ├── 🧯 incident-triage.md
    └── 🔙 rollback.md
```

---

## 📚 Appendix B — Project file shelf (how each file informs gates)

The following project files are treated as the **design & QA reference shelf**. Each one informs at least one gate in this document.

### 🧠 Core KFM design & governance
- **Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design.docx** → architecture, TDD/CI posture, STAC/DCAT/PROV provenance, PostGIS + Neo4j expectations (G-CORE-00, G-CAT-30, G-DB-50, G-GRAPH-60, G-GOV-140)
- **Latest Ideas.docx** → catalog quick gates, promotion fail-closed patterns, kill-switch, SBOM/manifest/signing ideas (G-CAT-30, G-PIPE-70, G-SC-130)
- **Other Ideas.docx** → hazards refresh pipeline, self-validation evidence layout, retention policy, legends/symbology validation patterns (G-PIPE-70, G-UI-110, G-GOV-140)

### 🎛️ Modeling, simulation & optimization
- **Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf** → verification/validation/UQ discipline (G-SIM-100)
- **Generalized Topology Optimization for Structural Design.pdf** → optimization convergence, regression scenarios (G-SIM-100)
- **Spectral Geometry of Graphs.pdf** → graph invariants and consistency checks inspiration (G-GRAPH-60)

### 📈 Statistics, regression & inference
- **Understanding Statistics & Experimental Design.pdf** → experimental design validity and leakage prevention (G-STATS-80)
- **regression-analysis-with-python.pdf** → model diagnostics + assumption checks (G-STATS-80, G-ML-90)
- **Regression analysis using Python - slides-linear-regression.pdf** → quick regression checklist for CI gates (G-STATS-80)
- **graphical-data-analysis-with-r.pdf** → EDA-based QA patterns and outlier policies (G-STATS-80)
- **think-bayes-bayesian-statistics-in-python.pdf** → Bayesian calibration and uncertainty reporting (G-STATS-80, G-SIM-100)
- **Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf** → practical training loops, overfit detection, and metric hygiene (G-ML-90)

### 🛰️ GIS, remote sensing & cartography
- **python-geospatial-analysis-cookbook.pdf** → geospatial processing correctness and reproducibility (G-GEO-40)
- **making-maps-a-visual-guide-to-map-design-for-gis.pdf** → cartographic clarity & symbol semantics (G-UI-110, G-GOV-140)
- **Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf** → mobile map UX and interpretation risks (G-UI-110)
- **Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf** → EO pipeline reproducibility + data contracts (G-DATA-20, G-GEO-40, G-PIPE-70)

### 🗃️ Data architecture, interoperability & performance
- **PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf** → migrations, indexing, SQL regression testing (G-DB-50)
- **Data Spaces.pdf** → cross-system data contracts and interoperability constraints (G-DATA-20, G-CAT-30, G-GOV-140)
- **Scalable Data Management for Future Hardware.pdf** → performance budgets and heterogeneity-aware scaling (G-PERF-120)

### 🖥️ Web, rendering & assets
- **responsive-web-design-with-html5-and-css3.pdf** → responsive QA patterns & accessibility basics (G-UI-110)
- **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf** → WebGL failure modes + render sanity tests (G-UI-110)
- **compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf** → asset pipeline QA (formats, compression, transparency) (G-UI-110)

### 🔐 Security, resilience & concurrency
- **ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf** → defensive security controls and audit thinking (G-SEC-10, G-SC-130)
- **Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf** → threat awareness for toolchains (defensive use) (G-SEC-10)
- **concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf** → concurrency hazards, timing budgets, distributed reliability (G-PERF-120, G-PIPE-70)

### 🤝 Ethics, human factors & legal framing
- **Introduction to Digital Humanism.pdf** → human-centered governance, harm minimization (G-GOV-140)
- **On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf** → policy-aware ML governance cues (G-GOV-140, G-ML-90)
- **Principles of Biological Autonomy - book_9780262381833.pdf** → resilience/autonomy metaphors for safe system behavior (G-PIPE-70, G-PERF-120)

### 🛠️ Programming reference compendia (language-specific QA patterns)
- **A programming Books.pdf**
- **B-C programming Books.pdf**
- **D-E programming Books.pdf**
- **F-H programming Books.pdf**
- **I-L programming Books.pdf**
- **M-N programming Books.pdf**
- **O-R programming Books.pdf**
- **S-T programming Books.pdf**
- **U-X programming Books.pdf**

These compendia help standardize lint/test choices across polyglot components (G-CORE-00, G-SEC-10).

---

## ✅ Appendix C — “Use it in CI” starter checklist

- [ ] Add / confirm evidence root: `docs/reports/self-validation/`
- [ ] Add a workflow per high-impact gate (catalog, data, geospatial, graph, supply-chain)
- [ ] Enforce required gates as branch protection checks
- [ ] Require MANIFEST + SBOM + attestations for release tags
- [ ] Record waiver decisions in repo (time-boxed)

---

<div align="center">

### 🌾 KFM QA mantra
**If it can change the story the map tells, it must be provable.** 🧾🗺️

</div>

