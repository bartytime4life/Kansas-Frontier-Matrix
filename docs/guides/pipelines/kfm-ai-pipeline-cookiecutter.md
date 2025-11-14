---
title: "🧠 Kansas Frontier Matrix — KFM AI Pipeline Cookiecutter (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/pipelines/kfm-ai-pipeline-cookiecutter.md"
version: "v10.2.3"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/kfm-ai-pipeline-cookiecutter-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧠 **Kansas Frontier Matrix — KFM AI Pipeline Cookiecutter**  
`docs/guides/pipelines/kfm-ai-pipeline-cookiecutter.md`

**Purpose:**  
Define a reusable, KFM-native **AI data pipeline cookiecutter** that implements the **event-driven, agent-assisted, deterministic** workflow — **ingest → validate → transform (agent) → publish** — wired into **KFM paths, STAC/DCAT, FAIR+CARE, and CI**.

</div>

---

<p align="center">
  <img alt="Status: Diamond9 Omega" src="https://img.shields.io/badge/KFM-Diamond%E2%81%B9%20%CE%A9%20Certified-purple.svg">
  <img alt="Docs: MCP-DL v6.3" src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue.svg">
  <img alt="FAIR+CARE Aligned" src="https://img.shields.io/badge/Data-FAIR%2BCARE-green.svg">
  <img alt="KFM v10 Series" src="https://img.shields.io/badge/KFM-v10.2.x-orange.svg">
</p>

---

## 📁 Directory Layout

This layout is for this guide and the cookiecutter template it documents.

    docs/
    └── guides/
        └── pipelines/
            ├── README.md                                   # Pipelines guides index
            ├── kfm-ai-pipeline-cookiecutter.md             # THIS DOCUMENT
            └── cookiecutter-kfm-ai-pipeline/               # Cookiecutter template root
                ├── cookiecutter.json                       # Cookiecutter configuration
                └── {{ cookiecutter.project_slug }}/        # Rendered project skeleton
                    ├── .gitignore
                    ├── README.md                           # Template README
                    ├── pyproject.toml
                    ├── src/
                    │   └── {{ cookiecutter.project_slug }}/
                    │       ├── __init__.py
                    │       ├── cli.py                      # Typer CLI
                    │       ├── config.py                   # KFM-aware paths & env
                    │       ├── context.py                  # RunContext + step()
                    │       ├── ledger.py                   # Append-only JSONL ledger
                    │       ├── agent.py                    # Agent interface (JSON only)
                    │       ├── stac.py                     # STAC helpers
                    │       ├── faircare.py                 # FAIR+CARE checks
                    │       └── pipeline/
                    │           ├── __init__.py
                    │           ├── ingest.py               # Deterministic ingest
                    │           ├── validate.py             # Validation + FAIR+CARE overlay
                    │           ├── transform.py            # Agent-assisted transform
                    │           └── publish.py              # Assets + STAC + DCAT publish
                    ├── schemas/
                    │   ├── run_context.schema.json         # RunContext JSON Schema
                    │   ├── agent_action.schema.json        # AgentAction contract
                    │   ├── stac_item.schema.json           # Minimal STAC Item schema
                    │   └── dcat_dataset.schema.json        # Minimal DCAT Dataset schema
                    ├── examples/
                    │   ├── sample_run_context.json
                    │   ├── sample_agent_action.json
                    │   ├── sample_stac_item.json
                    │   └── sample_dcat_dataset.json
                    ├── tests/
                    │   ├── __init__.py
                    │   ├── test_schemas.py                 # JSON Schema validation tests
                    │   └── test_pipeline_smoke.py          # Ingest/validate smoke test
                    └── .github/
                        └── workflows/
                            └── ci.yml                      # Lint + tests + schema validation

---

## 1. Overview

This cookiecutter defines the **standard KFM AI data-pipeline skeleton**. Every new AI/ETL flow should be created from this template so that:

- Every run carries a **RunContext JSON state file** and an **append-only ledger**.
- The agent is **read-only** — it only returns **validated JSON plans**; all side-effects are implemented by deterministic Python.
- Data paths align with the KFM monorepo layout:

  - `data/work/staging/` — raw, ephemeral ingest  
  - `data/work/validated/` — validated, analysis-ready artifacts  
  - `data/assets/` — versioned published assets with blue/green `latest` pointer  
  - `data/catalogs/stac/` — STAC Items for assets  
  - `data/catalogs/dcat/` — DCAT Dataset JSON-LD for catalogs  

- Every publish step creates **immutable assets + metadata** and supports **fast rollback** (flip `latest` back).
- CI validates **schemas + tests + style** so each pipeline is safe to plug into KFM’s production graph.

---

## 2. Pipeline Lifecycle (KFM Pattern)

### 2.1 Conceptual Flow

    Ingest  → Validate → Transform (Agent) → Publish
                         │
                         └─ Agent produces JSON “action plan”; Python applies it.

- **Ingest** — deterministic pull into `data/work/staging/<run_id>/`.
- **Validate** — structural checks + FAIR+CARE overlay → validation report.
- **Transform (Agent)** — agent proposes an **AgentAction** JSON plan; Python validates the JSON and applies it.
- **Publish** — writes versioned assets + STAC Item + DCAT Dataset; can flip `latest` pointer (blue/green).

### 2.2 RunContext & Idempotent Steps

Every step function is wrapped by `@step("name")` from `context.py`:

- Each step records:

  - `started_at`, `completed_at`, `status`
  - `inputs_hash`, `outputs_hash`
  - `metadata` (free-form)

- The **RunContext JSON** is written to:

    data/work/tmp/ledger/run-<run_id>.json

- The **ledger JSONL** is written to:

    data/work/tmp/ledger/run-<run_id>.jsonl

If a step has already completed successfully, calling it again is a **no-op** (idempotent resume).

---

## 3. Cookiecutter Template Configuration

### 3.1 `cookiecutter.json`

    {
      "project_name": "KFM AI Data Pipeline",
      "project_slug": "kfm_ai_pipeline",
      "project_description": "Kansas Frontier Matrix event-driven, agent-assisted, deterministic AI data pipeline with STAC/DCAT + FAIR+CARE.",
      "author_name": "Kansas Frontier Matrix",
      "author_email": "you@example.com",
      "python_version": "3.11",
      "openai_model": "gpt-4.1-mini",
      "license": "MIT",
      "use_github_actions": "y"
    }

These values control the generated project name, import slug, and model choice.

---

## 4. KFM-Aware Configuration (`config.py`)

`Settings` encapsulates all KFM paths and environment options:

- `repo_root` — root of the KFM repo (default: `Path.cwd()`).
- `staging_dir` — `data/work/staging`
- `validated_dir` — `data/work/validated`
- `assets_dir` — `data/assets`
- `ledger_dir` — `data/work/tmp/ledger`
- `stac_catalog_dir` — `data/catalogs/stac`
- `dcat_dir` — `data/catalogs/dcat`
- `telemetry_dir` — `data/work/tmp/telemetry`
- `governance_dir` — `docs/standards/governance`
- `openai_api_key`, `openai_model` — agent configuration.

Environment overrides use the prefix `KFM_PIPELINE_`, for example:

    export KFM_PIPELINE_REPO_ROOT=/workspaces/Kansas-Frontier-Matrix
    export KFM_PIPELINE_ASSETS_DIR=data/assets

`get_settings()` is cached so every module can import it cheaply.

---

## 5. RunContext, Ledger, Step Decorator

### 5.1 RunContext

`RunContext` (in `context.py`) holds:

- `run_id` (string)
- `created_at` (ISO timestamp)
- `state_path` (path to `run-<run_id>.json`)
- `steps` (mapping of step name → `StepRecord`)

Each `StepRecord` stores:

- `name`
- `started_at`
- `completed_at`
- `status` (`running`, `completed`, `failed`)
- `inputs_hash`, `outputs_hash`
- `metadata` (dict)

The **RunContext schema** is documented in `schemas/run_context.schema.json` and used for smoke testing.

### 5.2 Ledger

`ledger.py` appends small JSON objects to `run-<run_id>.jsonl`:

- `run_id`
- `step`
- `event_type` (`step_started` / `step_completed`)
- `payload` (hashes, metadata)
- `timestamp`

This gives a replayable history for audits and Focus Mode dashboards.

### 5.3 Step Decorator

`step(name)` wraps functions with signature `fn(ctx: RunContext, **kwargs)`:

- Computes `inputs_hash` from `kwargs`.
- If the step is already recorded as `status == "completed"`, it **returns immediately**.
- Otherwise:

  1. Writes `step_started` ledger entry.
  2. Executes the function.
  3. Computes `outputs_hash` from the return value.
  4. Updates RunContext + ledger with `step_completed`.

This is the core **idempotency primitive** for all pipeline steps.

---

## 6. Agent Contract & JSON Schemas

### 6.1 Agent Interface (`agent.py`)

`call_agent_system(prompt, context)`:

- Calls an OpenAI-compatible `/chat/completions` endpoint.
- Uses `response_format: { "type": "json_object" }`.
- System prompt forbids side-effects; agent must **only** return an `AgentAction` JSON object.
- The function parses `message.content` as JSON and returns it.

If parsing fails, the pipeline raises a `RuntimeError` — no partial or ambiguous actions are accepted.

### 6.2 AgentAction Schema

`schemas/agent_action.schema.json` defines the contract:

- `version` — e.g. `"v1"`.
- `operations` — array of operations.
- Each operation:

  - `op` — one of: `filter`, `project`, `group_by`, `aggregate`, `tag`, `route`.
  - `target` — logical target (e.g. `"records"`).
  - `params` — dict with operation parameters.
  - `notes` — optional explanation.

In `transform.py`:

1. Agent is given a **summary context** (run id, record count, validation info, source uri).
2. Response is validated against `agent_action.schema.json` using `jsonschema`.
3. If valid, Python applies a deterministic transform (template: simple projection + `run_id` tagging).
4. The output file is:

    data/work/validated/<run_id>/transformed.json

   and includes the `agent_action` used for reproducibility.

---

## 7. Validation & FAIR+CARE (`validate.py`, `faircare.py`)

### 7.1 Structural Validation

The default `validate()` step:

- Loads `raw.json` from the ingest manifest.
- Confirms:

  - `records` key exists.
  - `records` is a list.

- Optionally loads `schemas/run_context.schema.json` and checks that the schema itself is valid (smoke test).

It returns a `validation_report` dict with:

- `record_count`
- `warnings`
- `errors`
- `faircare` (added by overlay below)

### 7.2 FAIR+CARE Overlay

`run_fair_care_checks()` receives:

- `ingest_manifest`
- `validation_report`
- `context` (e.g. `run_id`, `raw_path`)

It returns:

- `summary` (counts of passes, warnings, errors)
- `passes`, `warnings`, `errors`
- `context`

The default implementation is a **stub**:

- Checks that a `source_uri` exists in `ingest_manifest`.
- Checks that `record_count > 0`.

You can extend this for:

- License compatibility.
- PII and sensitive attribute checks.
- Indigenous data governance.
- Spatial restrictions for specific locations.

---

## 8. STAC & DCAT Integration (`stac.py`, `publish.py`)

### 8.1 STAC Items

`build_minimal_stac_item()` constructs a small STAC Item:

- `type: "Feature"`
- `stac_version: "1.0.0"`
- `id` — e.g. `"demo-<run_id>"`
- `properties.datetime`
- `assets.data.href` → path to published `data.json`
- Custom fields such as:

  - `properties["kfm:collection"]`
  - `properties["kfm:run_id"]`

`write_stac_item(item, collection_id)` writes the item to:

    data/catalogs/stac/<collection_id>/items/<item_id>.json

### 8.2 DCAT Datasets

`publish.py` also writes a minimal **DCAT Dataset JSON-LD**:

- `@type: "dcat:Dataset"`
- `@id`: `"kfm-demo-<run_id>"`
- `dct:title`, `dct:description`, `dct:identifier`
- `dct:issued`, `dct:modified`
- `dcat:distribution` with an entry pointing at the `data.json` asset.
- `kfm:assetDir` pointing at the asset directory.

Output path:

    data/catalogs/dcat/kfm-demo-<run_id>.json

### 8.3 Asset-Oriented Publish (Blue/Green)

`publish()`:

- Copies `transformed.json` into:

    data/assets/<collection>/v<run_id_prefix>/data.json

- Manages the `latest` pointer:

    data/assets/<collection>/latest  →  data/assets/<collection>/v<run_id_prefix>/

- If `dry_run=True`, `latest` is **not** updated (candidate only).
- Writes corresponding STAC Item and DCAT Dataset.

This pattern enables:

- Fast rollback (re-point `latest`).
- Versioned history of assets.
- Clean integration with catalog layers.

---

## 9. CLI Usage (`cli.py`)

The CLI entrypoint is registered in `pyproject.toml`:

    [project.scripts]
    {{ cookiecutter.project_slug }} = "{{ cookiecutter.project_slug }}.cli:app"

### 9.1 `run`

Example:

    {{ cookiecutter.project_slug }} run \
      --run-id demo-001 \
      --dry-run \
      dummy://example

Arguments:

- `run_id` (optional) — autogenerated if omitted.
- `source_uri` (positional) — logical source identifier.
- `--dry-run` — publish artifacts but do not flip `latest`.

Flow:

1. `ingest()` → `ingest_manifest`
2. `validate()` → `validation_report`
3. `transform()` → `transform_manifest`
4. `publish()` → `publish_manifest`

All manifests are printed as formatted JSON.

### 9.2 `resume`

Intended to resume partially-completed runs. The template implementation shows how to load the RunContext and dump its JSON; you will typically extend it to rehydrate `source_uri` and resume the DAG.

### 9.3 `show_run`

Prints the RunContext JSON for a given `run_id` — useful for debugging, governance, and Focus Mode dashboards.

---

## 10. Tests & CI

### 10.1 Schema & Pipeline Tests

`tests/test_schemas.py`:

- Validates each JSON Schema with `Draft202012Validator.check_schema`.
- Validates the example payloads:

  - `sample_run_context.json`
  - `sample_agent_action.json`
  - `sample_stac_item.json`
  - `sample_dcat_dataset.json`

`tests/test_pipeline_smoke.py`:

- Runs a minimal ingest + validate flow and asserts:

  - `manifest["raw_path"]` exists.
  - `validation_report["record_count"]` exists.

### 10.2 GitHub Actions CI (`.github/workflows/ci.yml`)

Stages:

1. Checkout and Python setup.
2. Install project with `.[dev]`.
3. Run `ruff` against `src` and `tests`.
4. Run `pytest` with coverage.
5. Validate all `schemas/*.schema.json` using `jsonschema`.

This keeps new pipelines aligned with KFM standards.

---

## 11. Using the Cookiecutter in KFM

### 11.1 Generate a New Pipeline

From the KFM repo root:

    cd docs/guides/pipelines
    pip install cookiecutter
    cookiecutter cookiecutter-kfm-ai-pipeline/

Example answers:

- `project_name`: `KFM Hazards AI Pipeline`
- `project_slug`: `kfm_hazards_ai_pipeline`

Result:

    kfm_hazards_ai_pipeline/
      ├── README.md
      ├── pyproject.toml
      ├── src/kfm_hazards_ai_pipeline/...
      └── ...

You can move this project under `tools/` or `src/pipelines/` as needed.

### 11.2 First Local Run

    cd kfm_hazards_ai_pipeline
    python -m venv .venv
    source .venv/bin/activate
    pip install -e ".[dev]"

    export KFM_PIPELINE_REPO_ROOT=/workspaces/Kansas-Frontier-Matrix
    export KFM_PIPELINE_OPENAI_API_KEY="<your-key>"

    kfm_hazards_ai_pipeline run dummy://example --dry-run

Artifacts you should see:

- `data/work/staging/<run_id>/raw.json`
- `data/work/validated/<run_id>/transformed.json`
- `data/assets/demo/v<run_id_prefix>/data.json`
- `data/catalogs/stac/demo/items/demo-<run_id>.json`
- `data/catalogs/dcat/kfm-demo-<run_id>.json`
- `data/work/tmp/ledger/run-<run_id>.jsonl`

---

## 12. Domain Specialization Hooks

- In `publish.py`, change:

    collection_id = "demo"

  to a domain-specific collection, for example:

    collection_id = "hazards"
    collection_id = "hydrology"
    collection_id = "treaties"

- Extend `validate.py` with domain schemas, spatial sanity checks, and temporal rules.
- Extend `faircare.py` with domain FAIR+CARE logic and a `policy_profile`:

    {
      "profile": "hazards-public",
      "requires_manual_review": false
    }

---

## 13. Governance & Version History

This cookiecutter is wired into KFM governance:

- YAML front-matter references:

  - `governance_ref` → ROOT governance.
  - `sbom_ref`, `manifest_ref` → release metadata.
  - `telemetry_ref`, `telemetry_schema` → pipeline telemetry contract.

- RunContext + ledger provide:

  - Input/output hashes.
  - Timestamps and status per step.
  - Provenance trail for audits.

- STAC/DCAT capture:

  - Asset URLs.
  - Dataset-level metadata.
  - Custom `kfm:*` fields for graph integration.

### 13.1 Version History

| Version | Date       | Author           | Summary                                                                 |
|--------:|-----------:|------------------|-------------------------------------------------------------------------|
| v10.2.3 | 2025-11-13 | KFM System Docs  | Initial **KFM AI Pipeline Cookiecutter** guide and specification.      |
