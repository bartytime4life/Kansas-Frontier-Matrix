---
title: "🧠 Kansas Frontier Matrix — KFM AI Pipeline Cookiecutter (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/pipelines/kfm-ai-pipeline-cookiecutter.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/kfm-ai-pipeline-cookiecutter-v2.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Guide"
intent: "reliable-ai-pipelines"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A2-R2-E1"
kfm_readme_template: "Platinum v7.1"
ci_enforced: true
---

<div align="center">

# 🧠 **Kansas Frontier Matrix — KFM AI Pipeline Cookiecutter**  
`docs/guides/pipelines/kfm-ai-pipeline-cookiecutter.md`

**Purpose**  
Define a reusable, KFM-native **AI data pipeline cookiecutter** that implements an  
**event-driven, agent-assisted, deterministic** workflow —  
**Ingest → Validate → Transform (Agent) → Publish** — wired into **KFM paths, STAC/DCAT, FAIR+CARE v2, and CI**.

</div>

<p align="center">
  <img alt="Status: Diamond9 Omega" src="https://img.shields.io/badge/KFM-Diamond%E2%81%B9%20%CE%A9%20Certified-purple.svg">
  <img alt="Docs: MCP-DL v6.3" src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue.svg">
  <img alt="FAIR+CARE v2" src="https://img.shields.io/badge/Data-FAIR%2BCARE_v2-green.svg">
  <img alt="KFM v10 Series" src="https://img.shields.io/badge/KFM-v10.4.x-orange.svg">
</p>

---

# 📁 Directory Layout (Guide + Template)

~~~text
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
                │       ├── cli.py                      # Typer CLI entrypoint
                │       ├── config.py                   # KFM-aware paths & env
                │       ├── context.py                  # RunContext + @step wrapper
                │       ├── ledger.py                   # Append-only JSONL ledger
                │       ├── agent.py                    # Agent interface (JSON-only)
                │       ├── stac.py                     # STAC helpers
                │       ├── faircare.py                 # FAIR+CARE v2 checks
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
~~~

---

# 1️⃣ Overview

This cookiecutter defines the **standard KFM AI data-pipeline skeleton**.  
Every new AI/ETL pipeline should be instantiated from this template so that:

- Every run carries a **RunContext JSON** state file and an **append-only ledger**.
- The agent is **read-only** — it only returns **validated JSON plans**; all side-effects are implemented by deterministic Python.
- Data paths align with the KFM monorepo layout:

  - `data/work/staging/` — raw, ephemeral ingest  
  - `data/work/validated/` — validated, analysis-ready artifacts  
  - `data/assets/` — versioned published assets with `latest` pointer  
  - `data/catalogs/stac/` — STAC Items & Collections  
  - `data/catalogs/dcat/` — DCAT Dataset JSON-LD  

- Every publish step creates **immutable assets + metadata** and supports **fast rollback**.
- CI validates **schemas + tests + linting**, so each pipeline is safe to plug into production.

---

# 2️⃣ Pipeline Lifecycle (KFM Pattern)

## 2.1 Conceptual Flow

```text
Ingest → Validate → Transform (Agent) → Publish
                         │
                         └── Agent produces JSON “action plan”; Python applies it.
````

* **Ingest** — deterministic pull into `data/work/staging/<run_id>/`.
* **Validate** — structural checks + FAIR+CARE v2 overlay → `validation_report`.
* **Transform (Agent)** — agent proposes an **AgentAction** JSON plan; Python validates and applies it.
* **Publish** — writes **versioned assets + STAC Item + DCAT Dataset**, and may flip `latest` pointer.

## 2.2 RunContext & Idempotent Steps

Every step function is wrapped by `@step("name")` in `context.py`.

* Each step records:

  * `started_at`, `completed_at`, `status`
  * `inputs_hash`, `outputs_hash`
  * optional `metadata`

* RunContext JSON (`run-<run_id>.json`) lives at:

```text
data/work/tmp/ledger/run-<run_id>.json
```

* Ledger JSONL (`run-<run_id>.jsonl`) logs events:

```text
data/work/tmp/ledger/run-<run_id>.jsonl
```

If a step already completed successfully, calling it again is a **no-op**.
This gives **idempotent resume** and safe reruns.

---

# 3️⃣ Cookiecutter Configuration (`cookiecutter.json`)

```json
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
```

These values control the generated project name, slug, and agent model.

---

# 4️⃣ KFM-Aware Configuration (`config.py`)

`Settings` encapsulates all KFM paths and env options:

* `repo_root` — base of repo (default: `Path.cwd()`).
* `staging_dir` — `data/work/staging`
* `validated_dir` — `data/work/validated`
* `assets_dir` — `data/assets`
* `ledger_dir` — `data/work/tmp/ledger`
* `stac_catalog_dir` — `data/catalogs/stac`
* `dcat_dir` — `data/catalogs/dcat`
* `telemetry_dir` — `data/work/tmp/telemetry`
* `governance_dir` — `docs/standards/governance`

Environment overrides use `KFM_PIPELINE_` prefix:

```bash
export KFM_PIPELINE_REPO_ROOT=/workspaces/Kansas-Frontier-Matrix
export KFM_PIPELINE_ASSETS_DIR=data/assets
export KFM_PIPELINE_OPENAI_MODEL=gpt-4.1-mini
```

`get_settings()` is cached so any module can call it.

---

# 5️⃣ RunContext, Ledger, and `@step` Decorator

## 5.1 RunContext

`RunContext` tracks:

* `run_id`
* `created_at`
* `state_path`
* `steps` (mapping of step name → `StepRecord`)

Each `StepRecord` stores:

* `name`
* `status` (`pending|running|completed|failed`)
* `started_at`, `completed_at`
* `inputs_hash`, `outputs_hash`
* `metadata`

Schema defined in `schemas/run_context.schema.json`, validated in tests.

## 5.2 Ledger

`ledger.py` appends events to a JSONL file per run:

* `run_id`
* `step`
* `event` (`step_started` | `step_completed` | `step_failed`)
* `timestamp`
* `payload` (hashes, extra fields)

This provides an **append-only activity log** for audits and Focus Mode dashboards.

## 5.3 `@step` Decorator

`@step("name")` ensures:

1. If step already `completed`, skip (idempotent).
2. Otherwise, log `step_started`.
3. Run the function.
4. Compute `outputs_hash`, log `step_completed`.

This pattern is used across:

* `ingest.py`
* `validate.py`
* `transform.py`
* `publish.py`

---

# 6️⃣ Agent Contract & JSON Schemas

## 6.1 Agent Interface (`agent.py`)

The agent is **purely advisory**, not imperative.

* `call_agent(prompt, context)` sends a chat completion request with:

  * strict system instructions: *“Return JSON that conforms to `AgentAction` schema; never run code or access the network.”*
  * `response_format: { "type": "json_object" }`

* The function:

  * parses `message.content` as JSON
  * validates against `agent_action.schema.json`
  * returns the JSON object (Python dict)

No side-effects occur in the agent itself.

## 6.2 AgentAction Schema

`schemas/agent_action.schema.json` defines:

* `version` — string, e.g. `"v1"`.
* `operations[]` — list of operations.

Each operation:

* `op` (enum) — `filter`, `project`, `group_by`, `aggregate`, `tag`, `route`.
* `target` — e.g. `"records"`.
* `params` — JSON object with operation parameters.
* `notes` — optional explanation string.

In `transform.py`:

1. Build prompt: pipeline context + validation summary + sample rows.
2. Call `call_agent`.
3. Validate JSON with `jsonschema`.
4. Apply deterministic transform using Python (e.g. `pandas` / `polars`).
5. Save results to:

```text
data/work/validated/<run_id>/transformed.json
```

* Include the `agent_action` used in `metadata` → ensures reproducibility.

---

# 7️⃣ Validation & FAIR+CARE v2

## 7.1 Structural Validation (`validate.py`)

Default behavior:

* Load raw ingest output (e.g., `raw.json` or `input.parquet`).
* Confirm required keys/columns exist.
* Generate `validation_report`:

  * `record_count`
  * `field_summaries`
  * `warnings`, `errors`

## 7.2 FAIR+CARE Overlay (`faircare.py`)

The FAIR+CARE overlay is called post-validation:

* Input:

  * `ingest_manifest`
  * `validation_report`
  * `RunContext` metadata

* Output:

  * `faircare_summary` (passes/warnings/errors)
  * augmented `validation_report` with governance notes

The default implementation is a **minimal stub** you can extend:

* Ensure `source_uri` exists.
* Detect any fields flagged as PII or sensitive.
* Flag datasets needing manual review.

---

# 8️⃣ STAC & DCAT Integration

## 8.1 STAC (`stac.py`)

`build_stac_item()` creates minimal valid STAC:

* `id: demo-<run_id>`
* `collection: demo` (override in domain projects)
* `properties.datetime`
* `assets.data.href` → `data/assets/<collection>/vX.Y.Z/data.json`
* `properties["kfm:run_id"]`
* `properties["kfm:version"]`

Written to:

```text
data/catalogs/stac/<collection>/items/demo-<run_id>.json
```

## 8.2 DCAT

`build_dcat_dataset()` builds a DCAT Dataset JSON-LD:

* `@type: "dcat:Dataset"`
* `dct:title`, `dct:description`
* `dct:identifier`
* `dct:issued`, `dct:modified`
* `dcat:distribution[]` with `accessURL` pointing at data asset

Written to:

```text
data/catalogs/dcat/kfm-demo-<run_id>.json
```

---

# 9️⃣ CLI (`cli.py`)

The CLI uses **Typer**.

## 9.1 Commands

### `run`

```bash
{{ cookiecutter.project_slug }} run dummy://example --dry-run
```

* Orchestrates:

  * `ingest`
  * `validate`
  * `transform`
  * `publish`

* `--dry-run` ensures no `latest` pointer is updated and no STAC/DCAT is written to final locations.

### `resume`

* Intended to resume partial runs based on `run_id`.
* Template implementation prints current RunContext; you extend it to resume.

### `show-run`

* Prints RunContext JSON and ledger path for a given `run_id`.

---

# 🔟 Tests & CI (`tests/**`, `.github/workflows/ci.yml`)

## 10.1 Tests

* `test_schemas.py`

  * Validates each schema with `jsonschema`.
  * Validates example payloads in `examples/`.

* `test_pipeline_smoke.py`

  * Runs simplified ingest + validate.
  * Asserts that:

    * `record_count` exists.
    * No fatal errors occur.

You are expected to add additional tests for transform & publish as you specialize.

## 10.2 CI Workflow (`ci.yml`)

* Setup Python 3.11
* Install `.[dev]`
* Run `ruff`
* Run `pytest`
* Run JSON Schema validation

All new pipelines must pass CI before being added to upstream KFM.

---

# 1️⃣1️⃣ Using the Cookiecutter

## Generate a New Pipeline

From repo root:

```bash
cd docs/guides/pipelines
pip install cookiecutter
cookiecutter cookiecutter-kfm-ai-pipeline/
```

Follow prompts:

* `project_name`: `"KFM Hazards AI Pipeline"`
* `project_slug`: `"kfm_hazards_ai_pipeline"`

Then:

```bash
cd {{ project_slug }}
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Run a dry-run:

```bash
export KFM_PIPELINE_REPO_ROOT=/workspaces/Kansas-Frontier-Matrix
export KFM_PIPELINE_OPENAI_API_KEY=<your-key>

{{ project_slug }} run dummy://example --dry-run
```

Expected:

* RunContext and ledger written
* Raw → validated → transformed artifacts created in `data/work`
* STAC/DCAT drafts created under `data/catalogs`
* No `latest` pointer updated (because `--dry-run`).

---

# 1️⃣2️⃣ Governance, Telemetry & Version History

* Frontmatter references SBOM/SBOM schema + governance doc.
* RunContext + ledger provide step-level provenance.
* STAC/DCAT carry `kfm:*` fields required by publishing.
* Telemetry v2 events emitted by `telemetry` module may feed dashboards.

## Version History

| Version | Date       | Summary                                                                                          |
| ------: | ---------- | ------------------------------------------------------------------------------------------------ |
| v10.4.2 | 2025-11-16 | Upgraded to KFM-MDP v10.4.2; added Telemetry v2, CARE v2 references, updated paths & CI guidance |
| v10.2.3 | 2025-11-13 | Initial KFM AI Pipeline Cookiecutter guide and specification                                     |

---

<div align="center">

**Kansas Frontier Matrix — KFM AI Pipeline Cookiecutter (v10.4.2)**
Reliable AI Pipelines × FAIR+CARE v2 × STAC/DCAT × Deterministic Orchestration
© 2025 Kansas Frontier Matrix — CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
