---
title: "🍪 Kansas Frontier Matrix — Cookiecutter Template for AI/ETL Pipelines (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/pipelines/cookiecutter-kfm-ai-pipeline/README.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/pipelines-cookiecutter-ai-v2.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Template Guide"
intent: "cookiecutter-ai-etl"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A2-R2-E1"
kfm_readme_template: "Platinum v7.1"
ci_enforced: true
---

<div align="center">

# 🍪 **Kansas Frontier Matrix — Cookiecutter Template for AI/ETL Pipelines**  
`docs/guides/pipelines/cookiecutter-kfm-ai-pipeline/README.md`

**Purpose**  
Provide the **official Cookiecutter scaffolding** for building new **AI**, **ETL**, **STAC**,  
**geospatial**, or **remote-sensing** pipelines inside the Kansas Frontier Matrix (KFM).  

All generated pipelines automatically conform to **FAIR+CARE v2**, **MCP-DL v6.3**,  
**STAC/DCAT**, **Neo4j**, **RDF/GeoSPARQL**, **Lineage v2**, **Telemetry v2**, and  
**Governance** requirements.

This template is the **only approved starting point** for creating new KFM pipelines.

</div>

---

# 📘 Overview

The **Cookiecutter KFM AI Pipeline template** generates a pipeline that includes:

- ✅ Canonical directory structure:  
  `ingest → preprocess → analytics → validate → promote → publish`
- 🧬 Lineage v2 stubs (PROV-O · GeoSPARQL · CIDOC · CARE v2)
- 🧪 Great Expectations (GX) validation checkpoint stubs
- ⚖️ FAIR+CARE v2 masking, sovereignty checks, governance hooks
- 🛰 STAC/DCAT metadata creation helpers
- 🌐 Neo4j upsert + spatial indexing boilerplate
- 🧠 Optional AI module (agent-assisted transform / summarization)
- 📡 Telemetry v2 emitters (energy, CO₂, metrics, violations)
- 🔐 SBOM + SLSA attestation placeholders
- 🧱 Idempotent Makefile tasks
- 🛠 CI workflow templates (lint, tests, schemas, governance)

The resulting project is **deployment-ready**, **testable**, **documented**, **governed**, and **reproducible**.

---

# 📁 Directory Layout (Generated Pipeline Skeleton)

~~~text
{{ cookiecutter.project_slug }}/
├── README.md                               # Pipeline-specific README
├── pyproject.toml                          # Project metadata & dependencies
├── config/
│   ├── pipeline.config.yaml                # Domain/pipeline configuration
│   └── ai_prompt.txt                       # Optional AI prompt template
├── ingest/
│   ├── fetch.py                            # HTTP/S3/FS ingest logic
│   ├── schema/
│   │   └── ingest.schema.json              # Ingest manifest/data schema (JSON Schema)
│   └── utils.py                            # Shared ingest helpers
├── preprocessing/
│   ├── cloud_mask.py                       # Cloud/shadow/snow masking (optional)
│   ├── reprojection.py                     # CRS transforms (GDAL/PROJ)
│   ├── harmonize_gsd.py                    # Resolution harmonization
│   └── utils.py                            # Preprocessing helpers
├── analytics/
│   ├── ndvi.py                             # Example analytic (placeholder)
│   ├── flood_extent.py                     # Example analytic (placeholder)
│   ├── trend.py                            # Example analytic (placeholder)
│   └── utils.py                            # Analytics helpers
├── validate/
│   ├── great_expectations.yml              # GX config
│   ├── checkpoints/
│   │   └── pipeline_schema.yml             # Example checkpoint
│   └── expectations/
│       └── schema_{{ cookiecutter.project_slug }}.json  # Example expectations
├── promote/
│   ├── promote.py                          # Move staging → processed (Validate→Promote)
│   └── metadata.json                       # Promotion config/metadata stub
├── publish/
│   ├── stac_publish.py                     # STAC Items/Collections creation
│   ├── neo4j_publish.py                    # Graph upsert logic (Neo4j)
│   └── rdf_export.py                       # RDF + GeoSPARQL export
├── lineage/
│   ├── build_lineage.py                    # Lineage v2 JSON-LD builder
│   ├── lineage.context.jsonld              # JSON-LD context for KFM lineage
│   └── lineage.schema.json                 # Lineage schema for validation
├── telemetry/
│   └── writer.py                           # Telemetry v2 writer (NDJSON)
├── governance/
│   ├── care_rules.json                     # CARE v2 rules config
│   ├── sovereignty_masks.geojson           # Sovereignty AOI overlays (synthetic stub)
│   └── audit_hooks.py                      # Governance hooks for pipeline
├── tests/
│   ├── test_ingest.py                      # Ingest smoke tests
│   ├── test_preproc.py                     # Preprocessing tests
│   ├── test_analytics.py                   # Analytics tests
│   ├── test_validate.py                    # GX validation tests
│   ├── test_publish.py                     # STAC/graph/RDF tests (stubs)
│   └── data/                               # Test fixtures
└── Makefile                                # Idempotent entrypoints
~~~

---

# 🧩 Architecture Model (Conceptual Flow)

```text
Ingest → Preprocess → Analytics → Validate (GX) → Promote → Publish → Lineage → Governance
````

* **Ingest** — Controlled data acquisition with ETag, checksums, manifests.
* **Preprocess** — Harmonize, clean, transform, enforce CARE early mask hints.
* **Analytics** — Domain-specific computation, hazard/climate/historical models.
* **Validate (GX)** — Schema + integrity + FAIR+CARE checks.
* **Promote** — Move from staging → processed (Validate→Promote pattern).
* **Publish** — STAC/DCAT/Neo4j/RDF exports (optional per pipeline).
* **Lineage** — Lineage v2 bundle (JSON-LD) linking everything.
* **Governance** — Append to governance ledger; integrate SBOM and SLSA.

---

# ⚙️ Required Cookiecutter Variables

The template prompts for:

| Variable              | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| `project_name`        | Human-readable project name                                  |
| `project_slug`        | Python package + directory name                              |
| `project_description` | Short description of the pipeline                            |
| `domain`              | `remote_sensing`, `hazards`, `hydrology`, `historical`, etc. |
| `care_label_default`  | Default CARE label: `public`, `sensitive`, or `restricted`   |
| `stac_collections`    | Comma-separated list of STAC collections to integrate with   |
| `ai_enabled`          | `y/n` — whether to include AI/agent modules                  |
| `use_github_actions`  | `y/n` — include CI workflow                                  |
| `license`             | Project license (default: MIT)                               |

---

# 🧪 Validation & GX Integration

The template provides a baseline **Great Expectations** structure:

* `great_expectations.yml` — project config stub.
* `checkpoints/pipeline_schema.yml` — example checkpoint.
* `expectations/schema_{{ project_slug }}.json` — starter expectations.

### Standard expectation suites to extend:

* Schema expectations (required columns, types).
* Value range checks.
* Nullability rules.
* CARE-related expectations (flags, AOI intersection status).
* Temporal expectations (monotonic time for timeseries).

Pipelines instantiated from this template should then tighten these expectations based on domain requirements.

---

# ⚖️ Governance & CARE v2 Integration

The generated pipeline contains governance stubs in `governance/`:

* `care_rules.json` — defines CARE v2 policy profile for the pipeline.
* `sovereignty_masks.geojson` — synthetic AOI overlay example.
* `audit_hooks.py` — Python hooks to:

  * enrich metadata with CARE v2 fields
  * run sovereignty intersection checks
  * apply masking strategies (e.g., H3, centroid-only)
  * append governance entries to the ledger

Developers must:

* Configure `care_rules.json` per domain.
* Replace synthetic AOIs with real overlays in controlled repos.
* Integrate `audit_hooks.py` into preprocess / publish steps.

---

# 🧬 Lineage v2 Stubs

The `lineage/` folder contains:

* `build_lineage.py` — to generate lineage JSON-LD bundles.
* `lineage.context.jsonld` — KFM lineage context (PROV-O + GeoSPARQL + CARE v2).
* `lineage.schema.json` — schema for validating lineage bundles.

Every pipeline is expected to:

* Call `build_lineage.py` during Promote or Publish.
* Update the lineage bundle with:

  * input datasets
  * steps performed
  * transformations
  * CARE decisions
  * telemetry summary
  * published STAC/DCAT/Graph/RDF references

---

# 📡 Telemetry v2

The `telemetry/writer.py` module:

* Writes Telemetry v2 entries into NDJSON:

```text
data/telemetry/<project_slug>.ndjson
```

* Fields include:

  * `pipeline`, `stage`, `run_id`
  * `status`
  * `duration_ms`
  * `rows_processed` / `pixels_processed`
  * `energy_wh`, `co2_g`
  * `care_violations`, `sovereigntyConflicts`
  * `errors[]`

These are aggregated into:

```text
releases/v10.4.2/pipeline-telemetry.json
```

The exact aggregator & schema must be wired in the main KFM repo once the pipeline is installed.

---

# 🛰 STAC / DCAT / Neo4j / RDF Exports

The template provides:

* `publish/stac_publish.py` — helper to write STAC Items/Collections.
* `publish/neo4j_publish.py` — helper to upsert Nodes and relationships.
* `publish/rdf_export.py` — helper to write RDF + GeoSPARQL TTL or JSON-LD.

These are **stubs**, deliberately minimal but:

* Use official KFM paths.
* Carry forward the `kfm:*` metadata.
* Accept published artifact and manifest as inputs.
* Should be extended with domain-specific mapping (e.g., Scenes, Places, Events).

---

# 🧪 Tests & CI Templates

The template includes:

* Pytest tests in `tests/`:

  * `test_ingest.py`, `test_preproc.py`, `test_analytics.py`, `test_validate.py`, `test_publish.py`.
  * Schema and lineage tests.

* A CI workflow stub in `.github/workflows/ci.yml` that runs:

  * Python setup
  * `pip install -e .[dev]`
  * Lint (e.g., `ruff`)
  * Tests (`pytest`)
  * JSON Schema validation for `schemas/` and `lineage/`

Each new pipeline can adjust CI but **must keep governance checks** in place.

---

# 🚀 Usage

## 1. Generate a New Pipeline

From the repo root (or dedicated tools directory):

```bash
pip install cookiecutter
cookiecutter docs/guides/pipelines/cookiecutter-kfm-ai-pipeline
```

Answer prompts to define:

* `project_name`
* `project_slug`
* domain, CARE defaults, and publishing modes.

The scaffold will appear as:

```text
{{ project_slug }}/
```

You may then move or rename it under KFM’s canonical pipeline space, e.g.:

```text
src/pipelines/{{ project_slug }}/
```

## 2. Initialize

```bash
cd {{ project_slug }}
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## 3. First Validation Run

```bash
make validate
make test
```

Fix any schema, CARE, or test failures before integrating into the main KFM repo.

---

# 🧭 Relationship to `kfm-ai-pipeline-cookiecutter` Guide

This README documents the **template itself**.

For design rationale and higher-level architecture, see:

```text
docs/guides/pipelines/kfm-ai-pipeline-cookiecutter.md
```

That document explains:

* Why RunContext + ledger exist
* The conceptual Ingest → Validate → Transform (Agent) → Publish lifecycle
* How to use the template within KFM pipelines and CI

---

# 🕰 Version History

| Version | Date       | Summary                                                                                           |
| ------: | ---------- | ------------------------------------------------------------------------------------------------- |
| v10.4.2 | 2025-11-16 | Upgraded to KFM-MDP v10.4.2; added Telemetry v2, CARE v2, lineage v2, updated paths & CI guidance |
| v10.3.1 | 2025-11-14 | Initial cookiecutter template documentation; aligned with FAIR+CARE, governance, telemetry, STAC  |

---

<div align="center">

**Kansas Frontier Matrix — Cookiecutter AI/ETL Pipeline Template (v10.4.2)**
Reproducible Pipelines × FAIR+CARE v2 × Provenance × AI Safety × STAC/DCAT/Graph/RDF
© 2025 Kansas Frontier Matrix — MIT License

</div>
