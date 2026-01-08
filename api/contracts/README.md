<div align="center">

# 🧩 **API Contracts**
### Kansas Frontier Matrix (KFM) — Contract-first interfaces for data, graphs, analysis & Focus Mode

![Contract-first](https://img.shields.io/badge/Contract--first-Required-2ea44f)
![OpenAPI](https://img.shields.io/badge/OpenAPI-3.1-blue)
![GraphQL](https://img.shields.io/badge/GraphQL-SDL-purple)
![JSON%20Schema](https://img.shields.io/badge/JSON%20Schema-Validated-0aa)
![STAC/DCAT/PROV](https://img.shields.io/badge/STAC%20%2F%20DCAT%20%2F%20PROV-Aligned-orange)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%2BCARE-Governed-ff8c00)

</div>

> ✅ **Rule:** If it’s used across a boundary (UI ↔ API, API ↔ ETL, external partners ↔ KFM), it must have a **versioned, machine-validated contract** here — and implementations must honor it.

---

## 🧭 What this folder is for

This directory is the **single source of truth** for KFM API interface contracts, including:

- 🌐 **REST contracts** (OpenAPI) for public and internal endpoints  
- 🧠 **Graph contracts** (GraphQL SDL + graph-query constraints)  
- 🧾 **Schema contracts** (JSON Schema) for:
  - 📦 catalogs & discovery (STAC / DCAT)
  - 🧬 lineage (PROV-style references)
  - 🧪 analytics outputs (stats/regression/Bayesian)
  - 🤖 Focus Mode bundles (Story Nodes, citations, evidence)
  - 📈 telemetry & audit payloads
- 🧰 **Examples + golden test fixtures** to support contract tests & CI

If a feature can’t point to a contract in this folder, it’s **not ready** to be depended on by the UI, governance workflows, or external integrators.

---

## 🧱 What counts as a “contract” in KFM (quick definition)

A **contract artifact** is a machine-validated schema/spec that defines an interface (examples: JSON Schema, OpenAPI, GraphQL SDL, UI config).  
Contracts are **versioned**, and breaking changes require explicit version bumps + migration plans.

Also relevant “pipeline contracts” KFM treats as sacred:
- 🧾 **Evidence artifacts** must be catalog-registered (STAC/DCAT) and lineage-linked (PROV-style) before UI/narratives use them.
- 🧠 **Focus Mode** must not display unsourced or non-provenanced content.

---

## 🗂️ Suggested directory layout

> Adapt this layout to your repo conventions — but keep the “one canonical home” rule.

```text
📁 api/
└── 📁 contracts/
    ├── 📄 README.md                          # You are here ✨
    ├── 📁 openapi/                           # REST contracts
    │   ├── 📄 public.v1.yaml
    │   ├── 📄 internal.v1.yaml
    │   └── 📁 components/                    # shared schemas/params/responses
    ├── 📁 graphql/                           # GraphQL contracts
    │   ├── 📄 schema.graphql
    │   └── 📄 directives.graphql             # auth/policy gating (optional)
    ├── 📁 jsonschema/                        # JSON Schemas (machine validated)
    │   ├── 📁 catalogs/                      # STAC/DCAT/PROV related shapes
    │   ├── 📁 focus_mode/                    # Story Node bundle + citations
    │   ├── 📁 analysis/                      # stats/regression/bayes outputs
    │   ├── 📁 jobs/                          # async job lifecycle
    │   └── 📁 telemetry/                     # audit + usage events
    ├── 📁 examples/                          # fixtures (redaction-safe)
    │   ├── 📁 requests/
    │   └── 📁 responses/
    ├── 📁 changelog/                         # contract change notes
    │   └── 📄 CONTRACTS_CHANGELOG.md
    └── 📁 tests/                             # contract tests (language/tool agnostic)
        ├── 📄 README.md
        └── 📁 fixtures/
```

---

## 🔑 Non‑negotiables (API contract invariants)

These are “do not break” rules. If a contract violates any of these, it should not ship.

### 1) 🧾 Versioning & compatibility
- ✅ **SemVer per contract surface** (OpenAPI bundle, GraphQL schema, JSON Schemas).
- ✅ **Backward-compatible by default**: additive changes OK; removals/renames require a new major version.
- ✅ Deprecations must be explicit and time-bounded (sunset plan).

### 2) 🧬 Determinism & provenance
- ✅ Contracted outputs must be **reproducible** for the same inputs (or differences must be explainable & logged).
- ✅ Every “evidence-like” response should support provenance hooks:
  - `stac_item_ids[]` / `collection_id`
  - `dcat_dataset_ids[]` / `distribution_ids[]`
  - `prov_activity_ids[]` / `run_id`

### 3) 🛡️ Safety, sovereignty & redaction
- ✅ **No sensitive leakage**: contracts must support redaction/generalization states (not just “raw data everywhere”).
- ✅ Policy must be **first-class** (auditable and visible in responses where applicable).
- ✅ For graph queries: **no unbounded traversal**, deterministic ordering, and parameter binding only.

### 4) 🌍 Interoperability first
- ✅ Prefer standards + portable payloads:
  - GeoJSON (vector), GeoTIFF/COG (raster), GeoParquet (tabular geo), CSV/JSON (tables)
  - STAC/DCAT/PROV alignment for discovery + lineage
- ✅ CORS support for browser clients when publishing public endpoints.

---

## 🧰 Contract surfaces (what we standardize)

### 🌐 REST (OpenAPI)
Use OpenAPI (3.1 recommended) for:
- dataset discovery + dataset detail
- catalog surfacing (DCAT/STAC)
- Focus Mode “bundle retrieval” (story + map/timeline context)
- long-running compute requests (simulation/analysis → job IDs)
- media delivery (thumbnails, legends, exports)

**Target patterns from KFM design docs:**
- `GET /api/datasets/{id}` → metadata + access links (catalog surface)
- `GET /api/graph/entities?...` → bounded entity queries
- `GET /api/analysis/focus?entity=...` → Focus Mode AI summary with citations
- `POST /api/simulations/ABM` → submit agent-based simulation job, return job ID

> 🧠 Tip: Keep REST endpoints **resource-shaped** and stable. Hide storage engines and internal schema churn behind the contract.

---

### 🧠 Graph (GraphQL)
GraphQL is best for:
- complex relationship queries (Place ↔ Event ↔ Person ↔ Dataset)
- selective fetching (clients ask only what they need)
- ontology-shaped types

**Contract rules for GraphQL:**
- ✅ schema mirrors the ontology (types like `Place`, `Event`, `Person`, `Dataset`)
- ✅ bounded complexity:
  - max depth
  - max nodes/edges
  - deterministic ordering fields
- ✅ policy gating:
  - redaction-aware fields
  - restricted attributes are either omitted or generalized by contract
- ✅ “no raw Cypher” exposure: clients never send Cypher strings

---

### 📦 Catalogs (STAC / DCAT / PROV references)
Catalog alignment is not optional in KFM. Contracts should:
- expose catalog identifiers in API responses
- allow “follow the links” access patterns
- ensure catalog records are validated (schemas + profiles)

**Recommended contract expectations:**
- STAC Items/Collections for assets & geospatial evidence
- DCAT dataset/distribution representation for discovery & harvesting
- PROV-style run/activity identifiers for lineage

---

## 🧾 Standard response envelope (recommended)

To keep clients sane across domains (datasets, graph, analysis, simulations), prefer a consistent envelope:

```json
{
  "data": {},
  "links": {
    "self": "...",
    "related": []
  },
  "meta": {
    "request_id": "uuid",
    "contract_version": "public.v1",
    "generated_at": "ISO8601",
    "warnings": []
  },
  "provenance": {
    "stac_item_ids": [],
    "dcat_dataset_ids": [],
    "prov_activity_ids": []
  },
  "policy": {
    "sovereignty_mode": "clear|restricted|conflict|unknown",
    "redaction": {
      "level": "none|generalized|withheld",
      "notes": []
    }
  }
}
```

### ❌ Standard error shape
```json
{
  "error": {
    "code": "KFM_INVALID_INPUT",
    "message": "Human readable summary",
    "details": {},
    "request_id": "uuid"
  }
}
```

---

## 🧪 Long-running compute pattern (jobs)

Many KFM operations are compute-heavy:
- 🔥 remote sensing derivations (time series, composites, change detection)
- 🧠 Focus Mode generation (evidence-constrained summarization)
- 🧬 graph analytics (community detection, spectral measures, pathfinding)
- 🧫 simulations (agent-based, optimization, scenario runs)

**Use async jobs** with a stable lifecycle:

```text
POST /api/jobs          -> 202 Accepted + job_id
GET  /api/jobs/{id}     -> status + progress + links
GET  /api/jobs/{id}/result -> final outputs (or links)
```

**Job contract must include:**
- `job_id`, `status`, `submitted_at`, `started_at`, `completed_at`
- `inputs` (with hashes), `parameters`
- `seed` and `randomness_control` (when stochastic)
- `environment` (runtime versions) when reproducibility matters
- provenance references (`prov_activity_ids`, etc.)

> 🧪 For simulation/analytics, treat outputs like **evidence artifacts**: register + validate + lineage-link before UI uses them.

---

## 📊 Analytics contracts (stats, regression, Bayesian)

KFM analysis endpoints should be explicit about:
- assumptions
- diagnostics
- uncertainty

### Minimum fields for analysis outputs
- `method`: `"linear_regression" | "logistic_regression" | "bayesian_update" | ...`
- `inputs`: dataset IDs, filters, time bounds
- `results`: coefficients/posteriors/estimates
- `uncertainty`: confidence/credible intervals, standard errors
- `diagnostics`: residual tests, convergence info, outliers handled
- `multiple_testing`: correction strategy (when relevant)
- provenance + policy fields

> ⚠️ Analytics contracts must avoid “single-number truth.” Always provide uncertainty and method transparency.

---

## 🌍 Geospatial contracts (maps, layers, routing)

Geospatial APIs should favor:
- spatial filters (`bbox`, `intersects`, `h3_cells`, `region_id`)
- time filters (`time_start`, `time_end`)
- pagination + tiling for big data
- links to optimized formats (COGs, GeoParquet) instead of massive JSON payloads

### Routing / network outputs (example expectation)
When returning paths/segments:
- GeoJSON FeatureCollection or vector tiles
- stable ordering of segments
- explicit CRS assumptions (default WGS84 unless stated)

---

## 🎨 Visualization & media contracts (legends, thumbnails, 3D)

KFM supports rich map/timeline/3D experiences (including WebGL-based rendering).

**Contracts should define:**
- image/thumbnail endpoints:
  - supported formats (PNG/JPEG/WebP as appropriate)
  - max dimensions
  - caching headers (ETag, Cache-Control)
- legends & symbol metadata:
  - accessibility labels (alt text, language)
  - governance + license
- 3D assets:
  - explicit formats (e.g., glTF/GLB or 3D Tiles if adopted)
  - coordinate frames & units
  - LOD conventions

> 📱 Mobile clients must be first-class: payload sizes, caching, and progressive loading are contract concerns.

---

## 🔐 Security & governance requirements

### API security baseline
- ✅ no string-concatenated queries (SQL/Cypher); parameter binding only
- ✅ input validation at the edge (schema validation + bounds)
- ✅ request IDs + audit-friendly logging
- ✅ authentication/authorization for write/admin surfaces
- ✅ CORS explicitly configured (don’t “*” by accident for privileged surfaces)

### Supply-chain & artifact integrity
If contract bundles ship as governed releases, they must support:
- checksum/digest references
- SBOM linkage (where applicable)
- signed release artifacts (Sigstore/Cosign model when the repo’s governance requires it)

---

## ✅ Contract validation & CI gates (minimum)

When you change any contract, CI should be able to:
- lint OpenAPI (structure + examples)
- validate JSON Schemas + example fixtures
- validate GraphQL schema (SDL parse + breaking change detection)
- run contract tests against known fixtures (goldens)

### PR checklist (copy/paste)
- [ ] updated OpenAPI/GraphQL/JSON Schema contracts
- [ ] added/updated **examples** under `api/contracts/examples/`
- [ ] added/updated contract tests (or fixtures)
- [ ] documented change in `api/contracts/changelog/CONTRACTS_CHANGELOG.md`
- [ ] bumped contract version (if breaking)
- [ ] documented migration path (if breaking)
- [ ] checked sovereignty/redaction implications

---

## 🔄 How to propose a new endpoint / contract change

1) 🧾 Write the contract change first  
2) 🧪 Add examples + fixtures  
3) ✅ Add validation/tests  
4) 🔁 Version bump if needed  
5) 📣 Document the change + migration notes  
6) ⚖️ Trigger governance review if it affects: redaction, sovereignty, public narratives, or catalog requirements

> If your repo includes it, use: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` as the proposal format.

---

## 📚 Project file coverage (why these contracts look like this)

This README is informed by the project’s attached references across:
- 🧪 scientific modeling + verification/validation/UQ
- 📊 statistics + regression + Bayesian workflows
- 🌍 geospatial + remote sensing + cartography
- 🧠 graphs + graph analytics
- 🧱 scalable data management + streaming semantics
- 🔐 security + secure coding
- 🎨 WebGL + responsive UI + media formats
- ⚖️ digital humanism + AI governance considerations
- 🧰 multi-language programming references (client generation + interoperability)

### 📎 Source list (expected repo placement: `docs/research/source_summaries/_attachments/` or `docs/references/`)
> Add these PDFs/docs to the repo (or link to an internal archive) so the references remain durable.

- `Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design.docx`
- `Latest Ideas.docx`
- `Other Ideas.docx`
- `MARKDOWN_GUIDE_v13.md.gdoc`

**Modeling / Statistics / ML**
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `Understanding Statistics & Experimental Design.pdf`
- `regression-analysis-with-python.pdf`
- `Regression analysis using Python - slides-linear-regression.pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`
- `graphical-data-analysis-with-r.pdf`
- `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf`

**Geospatial / Remote sensing / Cartography**
- `python-geospatial-analysis-cookbook.pdf`
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`

**Graphs / Optimization / Autonomy**
- `Spectral Geometry of Graphs.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`
- `Principles of Biological Autonomy - book_9780262381833.pdf`

**Data systems / Concurrency**
- `Scalable Data Management for Future Hardware.pdf`
- `Data Spaces.pdf`
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`

**Security / Governance**
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`
- `Introduction to Digital Humanism.pdf`
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`

**Frontend / Media**
- `responsive-web-design-with-html5-and-css3.pdf`
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

**Programming references (multi-language)**
- `A programming Books.pdf`
- `B-C programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`

---

## 🧭 Next recommended actions
- 📌 Create `api/contracts/openapi/public.v1.yaml` and define the baseline endpoints
- 📌 Add `api/contracts/graphql/schema.graphql` aligned with the ontology
- 📌 Add JSON Schemas for:
  - Focus Mode bundles
  - job lifecycle
  - analysis outputs
  - telemetry/audit events
- 📌 Stand up CI validation gates for contracts + examples
- 📌 Publish a “contract changelog” policy (deprecations + version bumps)

---

<div align="center">

© 2026 Kansas Frontier Matrix — Contract-first, provenance-linked, governed interfaces 🧭

</div>

