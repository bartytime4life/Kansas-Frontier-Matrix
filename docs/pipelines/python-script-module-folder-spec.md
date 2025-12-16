---
title: "📁 KFM — Python Script Module Folder Specification"
path: "docs/pipelines/python-script-module-folder-spec.md"

version: "v11.2.6"
last_updated: "2025-12-16"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Data Architecture Board · FAIR+CARE Oversight"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"
intent: "python-script-folder-overview"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "pipelines"
  applies_to:
    - "src/pipelines/**"
    - "tools/**"
    - "docs/pipelines/**"
    - "src/**/README.md"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by KFM-MDP v12"

owner: "KFM Core · Data Engineering"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
---

# 📁 Python Script Module — Folder Overview

This document defines the **canonical folder contract** for a governed **Python script module** in KFM.

A “script module” is treated as a **logical execution unit** (reproducible, auditable, and CI-valid), not just a code container.

## 📘 Overview

### 🎯 Purpose

**Module name:** `<module_name>`  
**Stage:** `<etl | catalog | qa-qc | graph-load | api-support | general>`  
**Domain:** `<air-quality | hydrology | surficial-geology | soil | remote-sensing | archaeology | general>`  
**Primary responsibility:** `<single-sentence description>`

This module exists to:

- Execute deterministic operations over declared inputs
- Emit governed artifacts (data, metadata, lineage)
- Integrate cleanly into **ETL → STAC/DCAT/PROV → Graph → APIs → UI** workflows

### 🧭 Where these modules live (repo placement)

Prefer these locations:

- **ETL / orchestration modules:** `src/pipelines/<domain>/<module_name>/`
- **Validators & developer utilities:** `tools/<area>/<module_name>/` (e.g., `tools/validation/…`)
- **Documentation-only runbooks/specs:** `docs/pipelines/…`

Avoid introducing new top-level script roots unless a legacy folder already exists and governance explicitly allows it.

### 🧱 Folder contract (non-negotiable invariants)

This module MUST satisfy:

- 📌 Deterministic execution (same inputs/config → same outputs/checksums)
- 📌 Explicit inputs & outputs (declared via config/CLI; no hidden reads/writes)
- 📌 Versioned configuration (schema-validated)
- 📌 Auditable provenance (run_id + inputs + outputs + environment notes)
- 📌 CI-compatible entrypoint(s)
- 📌 Zero hidden side effects

**Hard rule:** No script may write outside declared output roots.

### 📥 Inputs & 📤 Outputs (KFM-aligned)

**Inputs MUST:**
- Be declared via CLI + config
- Be validated at runtime
- Be logged with stable identifiers (paths, dataset IDs) and hashes where practical

**Outputs MUST:**
- Write only to declared output roots
- Use atomic writes (write temp → move/rename)
- Emit checksums for final artifacts

**Canonical output roots (outside this module folder):**
- `data/work/<domain>/<module_name>/<run_id>/` — intermediates (staging)
- `data/processed/<domain>/…` — canonical processed outputs
- `data/checksums/<domain>/…` — integrity hashes
- `data/stac/<domain>/…` — STAC collections/items for discoverability
- `data/reports/<domain>/<module_name>/…` — QA/QC + summary reports (as applicable)

Outputs are eligible for:
- STAC Item generation
- DCAT Distribution registration (docs/data catalogs)
- PROV-O lineage linkage (prov:Activity / prov:Entity / prov:Agent)

### 🧬 Provenance & lineage (minimum record)

Every execution MUST record:

- `run_id` (unique)
- `started_at`, `ended_at`
- `config_ref` (path + hash)
- `inputs[]` (path/ID + hash/etag if practical)
- `outputs[]` (path + checksum)
- `software_environment` (python version + key deps, or container digest if available)
- `operator` (human or automation identity)

No silent transformations are allowed.

### 🔐 Security & governance

- Secrets are sourced **from environment variables only**
- No embedded credentials, tokens, or private endpoints in configs
- Apply CARE labels when applicable
- If data is Indigenous, sensitive, or restricted: follow sovereignty rules and masking/generalization requirements

## 🗂️ Directory Layout

### Canonical in-repo module layout

~~~text
📁 src/pipelines/<domain>/<module_name>/
├── 📄 README.md                       — Module contract (this spec applied)
├── 🐍 __init__.py                     — Optional (if packaged)
├── 🐍 main.py                         — Primary executable entrypoint (or <script_name>.py)
├── 📁 configs/                        — Versioned runtime configs
│   ├── 🧾 example.yaml                — Example (documented, non-secret)
│   ├── 🧾 dev.yaml                    — Optional (non-secret; or generate in CI)
│   ├── 🧾 prod.yaml                   — Optional (non-secret; use env vars for secrets)
│   └── 🧾 config.schema.json          — Schema for config validation
├── 📁 schemas/                        — Optional local schemas (only if module-specific)
├── 📁 tests/                          — Unit + contract tests (module-scoped)
├── 📁 fixtures/                       — Optional golden inputs/outputs (small + non-sensitive)
└── 📁 .cache/                         — Optional local cache (gitignored)
~~~

### Entry points (document every executable)

| Script | Entry point | Description |
|---|---|---|
| `main.py` | `python -m src.pipelines.<domain>.<module_name>` *or* `python main.py` | `<what it does>` |

### Configuration rules

- Runtime behavior is configuration-driven (no hardcoded environment assumptions)
- `configs/config.schema.json` is enforced (fail fast on invalid config)
- Config files are treated as provenance inputs (hash them)

### Testing expectations

Minimum requirements:

- Smoke test runnable locally
- Schema validation test (config + any output metadata schemas)
- Determinism check (repeat run → identical checksums)

Optional:

- Golden output comparisons
- Contract tests asserting STAC/DCAT/PROV shape (where applicable)

## 🕰️ Version History

| Version | Date | Notes |
|---|---:|---|
| v11.2.6 | 2025-12-16 | Canonical script module folder specification (aligned to v11 repo layout). |

### 🔗 Navigation

- 📘 Standards → `docs/standards/README.md`
- 🧱 Data Architecture → `docs/architecture/README.md`
- 🧭 Pipelines → `docs/pipelines/README.md`
- 🛡️ Governance Charter → `docs/standards/governance/ROOT-GOVERNANCE.md`