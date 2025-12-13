---
title: "🧾 Kansas Frontier Matrix — DCAT Validation Composite Action"
path: ".github/actions/dcat-validate/README.md"
version: "v11.2.3"
last_updated: "2025-12-09"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council · Architecture Board"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/github-infra-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/github-workflows-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Guide"
intent: "github-dcat-validate-action"
role: "dcat-validation-composite-action"
category: "Metadata · DCAT · CI/CD · Composite Action"

classification: "Public Document"
sensitivity: "General (non-sensitive)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
risk_category: "Metadata"
indigenous_rights_flag: false
redaction_required: false
data_steward: "KFM FAIR+CARE Council"

fair_category: "F1-A1-I1-R1"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"

provenance_chain:
  - ".github/actions/dcat-validate/README.md@v11.2.3"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/github-actions-dcat-validate-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/github-actions-dcat-validate-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-actions:dcat-validate:v11.2.3"
semantic_document_id: "kfm-action-dcat-validate"
event_source_id: "ledger:.github/actions/dcat-validate/README.md"
immutability_status: "mutable-plan"
machine_extractable: true

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "governance-override"
  - "content-alteration"

accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States / Kansas"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next dcat-validate action update"

prov_profile: "PROV-O Plan + KFM Governance Extensions"
openlineage_profile: "OpenLineage v2.5 · CI/CD and metadata pipeline events"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — DCAT Validation Composite Action**  
`.github/actions/dcat-validate/`

**Purpose**  
Provide a **single, governed entrypoint** for validating **DCAT (W3C DCAT 3.x) catalog metadata**
under the **KFM‑DCAT v11** profile, ensuring:

- Required **Catalog / Dataset / Distribution / DataService** fields are present
- License / rights fields are complete and policy-consistent
- Provenance hooks exist (PROV‑O / KFM lineage conventions)
- Machine‑readable validation output for CI/CD gates and telemetry

This action is invoked primarily by:

- `.github/workflows/dcat_validate.yml` → **governed DCAT metadata gate** for KFM

</div>

---

## 📘 Overview

The `dcat-validate` action is KFM’s **DCAT quality gate** for publishable catalog metadata.

It is designed to:

- Validate DCAT metadata artifacts (commonly **JSON‑LD** and/or **Turtle**) against:
  - **DCAT 3.x structural expectations**
  - **KFM‑DCAT v11 profile rules** (project‑specific constraints)
- Enforce **governance‑linked requirements** such as:
  - license/rights presence and consistent labeling
  - publisher/provider responsibility fields
  - provenance linkage fields required by KFM publishing contracts
- Emit **deterministic, machine‑readable summaries** for downstream CI telemetry export.

Design goals:

- **Deterministic** — identical metadata inputs produce the same outcome.
- **Config‑driven** — rules and strictness are controlled by files in `config/`.
- **Composable** — callable from any workflow that needs a DCAT validation gate.

Any **policy‑relevant error** MUST fail the action (exit non‑zero).

---

## 🗂️ Directory Layout

~~~text
.github/
└── 🧱 actions/                                      # Reusable composite actions
    └── 🧾 dcat-validate/                            # DCAT validation action (KFM-DCAT v11)
        ├── 📄 README.md                             # ← This file (governance & usage)
        ├── ⚙️ action.yml                            # GitHub Action descriptor (composite)
        ├── 🧱 entrypoint.sh                         # Bash orchestrator (deterministic runner)
        ├── ⚙️ config/                               # Validation config + profile bindings
        │   ├── 📄 README.md                         # Config documentation (normative)
        │   ├── 🧾 profiles.yml                      # Profile IDs, strictness, format rules
        │   ├── 🧩 shapes/                           # SHACL shapes for validation
        │   │   ├── 🧩 kfm-dcat-v11.shapes.ttl        # KFM-DCAT v11 constraints (primary)
        │   │   └── 🧩 dcat-3-core.shapes.ttl         # Optional baseline shapes (if used)
        │   ├── 🧾 vocab.yml                         # Controlled vocab hints (themes, mediaType, etc.)
        │   └── 🧾 crosswalks.yml                    # Optional STAC↔DCAT crosswalk checks
        └── 🧪 scripts/                              # Helper scripts (language-agnostic)
            ├── 📄 README.md                         # Scripts overview + contracts
            ├── 🧬 run_dcat_validator.py             # Parse + validate DCAT graphs
            ├── 🧭 check_profile_rules.py            # Non-SHACL checks (naming, ids, conventions)
            └── 📊 summarize_dcat_results.py         # Unified JSON summary for telemetry
~~~

> **Normative:** Any structural change to this directory MUST be reflected here and in
> the workflow(s) that invoke this action.

---

## 🧭 Context

**Where this lands in the KFM pipeline**

- **ETL → catalogs (STAC/DCAT/PROV) → graph → API → frontend → Story Nodes → Focus Mode**
- `dcat-validate` is part of the **catalog stage**:
  - It validates that DCAT metadata is consistent and publishable
  - It helps guarantee downstream interoperability (federated catalog tooling, portal harvesters, etc.)
  - It ensures governance fields needed for FAIR+CARE reporting are present and machine-extractable

**What this action validates**

- DCAT **Catalog(s)** (optional, depending on repo structure)
- DCAT **Dataset(s)** (required for publishable records)
- DCAT **Distribution(s)** (access URLs, media types, optional checksums)
- DCAT **DataService(s)** (when APIs are cataloged)
- Optional crosswalk checks against STAC identifiers (configurable)

---

## 🗺️ Diagrams

No diagrams are required for this action README.

If a diagram is added later, it MUST be CI‑safe and conform to the repo’s diagram validation rules.

---

## 🧠 Story Node & Focus Mode Integration

This action supports Story Node and Focus Mode readiness by ensuring DCAT metadata:

- Is structured and consistent enough to be ingested into catalogs and the graph layer
- Includes stable identifiers suitable for linking evidence and governance records
- Avoids “dark metadata” (missing licenses, ambiguous publishers, unlabeled distributions)

Focus Mode usage is allowed for summarization and metadata extraction, but it MUST NOT invent
missing governance or provenance fields.

---

## 🧪 Validation & CI/CD

### ⚙️ Action interface

Within the KFM repository this action MAY be used in two forms:

1) **Direct script invocation** (common for early adoption)

~~~yaml
- name: 🧾 DCAT Validation (script entrypoint)
  run: |
    set -euo pipefail
    bash .github/actions/dcat-validate/entrypoint.sh data/dcat
~~~

2) **Composite action usage** (preferred long-term)

~~~yaml
- name: 🧾 DCAT Validation (composite)
  uses: ./.github/actions/dcat-validate
  with:
    dcat_root: "data/dcat"
    profile: "kfm-dcat-v11"
    config_dir: ".github/actions/dcat-validate/config"
    summary: "_dcat-validate-summary.json"
~~~

> The repo MUST treat these two forms as behaviorally equivalent. If `action.yml` is updated,
> the invoking workflow MUST use the canonical interface.

### 🧷 Inputs (proposed, for `action.yml`)

| Name         | Type   | Default                                 | Description |
|--------------|--------|------------------------------------------|-------------|
| `dcat_root`  | string | `data/dcat`                              | Root directory containing DCAT catalogs/datasets (repository convention). |
| `profile`    | string | `kfm-dcat-v11`                           | Profile identifier to apply (KFM‑DCAT v11). |
| `config_dir` | string | `.github/actions/dcat-validate/config`   | Directory containing profile config + SHACL shapes. |
| `format`     | string | `auto`                                   | Input format: `auto`, `jsonld`, `ttl`. |
| `fail_fast`  | bool   | `true`                                   | Stop at first critical error if true; otherwise validate all files. |
| `summary`    | string | `""`                                     | Optional path to write a JSON summary file. |

> **Schema note:** These inputs MUST be reflected in
> `schemas/json/github-actions-dcat-validate-v11.schema.json`.

### 📤 Outputs (proposed)

| Name             | Type   | Description |
|------------------|--------|-------------|
| `files_checked`  | number | Total number of DCAT files validated. |
| `issues_found`   | number | Total number of validation issues discovered. |
| `severity_max`   | string | Highest severity observed (`none`, `warning`, `error`, `critical`). |
| `summary_path`   | string | Path to the summary JSON file, if produced. |

### 🧱 Behavior (normative)

At a high level, the action MUST:

1) **Discover DCAT content**
- Traverse `dcat_root` for supported files (commonly `.json`, `.jsonld`, `.ttl`).
- Ignore non-metadata artifacts unless explicitly configured.

2) **Parse into a graph model**
- Parse DCAT into a normalized in-memory representation (RDF graph semantics).
- Fail fast on syntax errors (invalid JSON‑LD/Turtle).

3) **Validate against SHACL + profile rules**
- Run SHACL validation using shapes referenced by the selected `profile`.
- Apply additional profile rules (naming, identifier conventions, required fields).

4) **Evaluate policy thresholds**
- Classify findings into `warning` / `error` / `critical`.
- Exit non‑zero when thresholds are violated.

5) **Emit machine-readable outputs**
- Write (or print) a consolidated JSON summary suitable for telemetry export.

### ✅ Failure semantics (recommended)

- Exit `0` if no policy‑relevant errors are found.
- Exit `1` if any **error/critical** rule is violated (schema, SHACL, governance contract).
- Exit `2` for configuration/runtime failures (missing config, missing shapes, tool crash).

---

## 📦 Data & Metadata

### Expected inputs

This action validates DCAT metadata intended for KFM’s publishable catalog surface.

A conformant record SHOULD include, at minimum:

- A stable identifier (e.g., `dct:identifier`)
- A title and description (`dct:title`, `dct:description`)
- License / rights information (`dct:license` and/or `dct:rights`)
- Publisher/provider responsibility (`dct:publisher` and/or `dcat:contactPoint`)
- At least one distribution when the dataset is accessible (`dcat:distribution`)
  - with access/download URL and a declared format/media type

### Output summary (recommended shape)

The action SHOULD emit a summary that supports downstream telemetry aggregation:

- counts by severity
- counts by entity type (Catalog/Dataset/Distribution/DataService)
- per-file issue lists (file path + rule id + message + severity)
- profile id and config version used

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT

- DCAT provides the catalog-facing metadata surface for datasets and services.
- KFM‑DCAT v11 constrains DCAT usage for consistent publication and governance.

### STAC

- STAC remains the primary packaging format for spatiotemporal assets.
- A repo MAY enforce crosswalk checks between STAC identifiers and DCAT identifiers via `config/crosswalks.yml`.

### PROV‑O

- DCAT records SHOULD provide linkage points to provenance entities/activities where appropriate.
- This action can enforce “presence of linkage fields” (profile-dependent), but it does not generate provenance.

---

## 🧱 Architecture

### Execution model

- `entrypoint.sh` orchestrates the run:
  - strict shell mode (`set -euo pipefail`)
  - loads configuration from `config/`
  - invokes scripts to validate and summarize
- `run_dcat_validator.py` performs parsing and SHACL validation using the selected profile.
- `summarize_dcat_results.py` consolidates results into a single schema for telemetry export.

### Determinism requirements

- No network calls during validation.
- No nondeterministic ordering in result output.
- Config files are the sole source of rules and thresholds.

---

## ⚖ FAIR+CARE & Governance

This action enforces governance-aligned metadata requirements:

- **Findable/Accessible**: requires stable identifiers and minimum descriptive fields.
- **Reusable**: requires license/rights clarity and distribution semantics.
- **CARE**: supports Authority to Control by ensuring records can be audited and policy‑checked.

Telemetry and logs MUST NOT include:

- secrets, credentials, or tokens
- sensitive sovereign disclosures beyond what is permitted in governed metadata outputs

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.3 | 2025-12-09 | Initial governed README for `dcat-validate`; aligns with KFM‑DCAT v11 and KFM‑MDP v11.2.6. |

---

<div align="center">

🧾 **Kansas Frontier Matrix — DCAT Validation Composite Action (v11.2.3)**  
Catalog-First · FAIR+CARE-Governed · Provenance-Aware  

[⬅ GitHub Infra Overview](../../README.md) · [📊 CI/CD Workflows](../../workflows/README.md) · [⚖ Governance](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
