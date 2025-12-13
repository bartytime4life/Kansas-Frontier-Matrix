---
title: "🛰 Kansas Frontier Matrix — STAC Validation Composite Action"
path: ".github/actions/stac-validate/README.md"
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
stac_profile: "KFM-STAC v11"

status: "Active / Enforced"
doc_kind: "Guide"
intent: "github-stac-validate-action"
role: "stac-validation-composite-action"
category: "Metadata · STAC · CI/CD · Composite Action"

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
  - ".github/actions/stac-validate/README.md@v11.2.2"
  - ".github/actions/stac-validate/README.md@v11.2.3"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/github-actions-stac-validate-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/github-actions-stac-validate-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:github-actions:stac-validate:v11.2.3"
semantic_document_id: "kfm-action-stac-validate"
event_source_id: "ledger:.github/actions/stac-validate/README.md"
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
sunset_policy: "Superseded upon next stac-validate action update"

prov_profile: "PROV-O Plan + KFM Governance Extensions"
openlineage_profile: "OpenLineage v2.5 · CI/CD and metadata pipeline events"
---

<div align="center">

# 🛰 **Kansas Frontier Matrix — STAC Validation Composite Action**
`.github/actions/stac-validate/`

**Purpose**
Provide a **single, governed entrypoint** for validating **STAC 1.x Items and Collections** under the KFM‑STAC v11 profile, ensuring:

- Correct **STAC structure & required fields**
- Proper **spatiotemporal metadata** (GeoJSON, bbox, datetime)
- **Licensing, provenance, and FAIR+CARE hooks** for downstream governance
- Clean, machine‑readable validation output for CI/CD and telemetry

This action is invoked primarily by:

- `.github/workflows/stac_validate.yml` → **governed STAC gate** for KFM.

</div>

---

## 📘 Overview

The `stac-validate` action implements KFM’s **STAC validation layer**:

- Validates **STAC Items & Collections** in `data/stac/**` against:
  - **OGC STAC 1.x** core specification
  - **KFM-STAC v11 profile** (project‑specific extensions & conventions)
- Checks **GeoJSON geometry & bbox** consistency, `datetime` / `start_datetime` / `end_datetime`, and asset metadata fields.
- Ensures key **provenance & licensing** fields are present and consistent with KFM governance.
- Produces **structured logs** suitable for `telemetry_export.yml` and catalog dashboards.

Design goals:

- **Deterministic** — same STAC inputs → same outcome.
- **Config-driven** — profile & extension behavior controlled via config files.
- **Composable** — callable from any workflow gate that needs STAC validation.

Any invalid STAC entity MUST cause this action (and upstream workflows) to fail, blocking merges or releases.

---

## 🗂️ Directory Layout

~~~text
.github/
└── 🧱 actions/                                   # Reusable composite actions
    └── 🛰 stac-validate/                         # STAC validation action
        ├── 📄 README.md                          # ← This file (governance & usage)
        ├── ⚙️ action.yml                         # GitHub Action descriptor (composite / shell)
        ├── 🧱 entrypoint.sh                      # Main orchestrator script (bash)
        ├── ⚙️ config/                            # STAC profile & validation config
        │   ├── 🧾 profiles.yml                   # KFM-STAC profile IDs, options, strictness
        │   ├── 🧾 collections.yml                # Collection-level conventions (ids, hierarchies)
        │   └── 🧾 assets.yml                     # Asset-type rules (required fields, roles, media types)
        └── 🧪 scripts/                           # Helper scripts (optional, language-agnostic)
            ├── 🧬 run_stac_validator.py          # Core STAC validation wrapper
            ├── 🧭 check_spatiotemporal.py        # Extra bbox/time consistency checks
            └── 📊 summarize_stac_results.py      # Aggregates results → machine-readable summary
~~~

> **Normative:** Any structural change to this directory MUST be reflected here and in  
> `.github/workflows/stac_validate.yml`, plus relevant metadata docs in `docs/data/` & `docs/standards/`.

---

## 🧭 Context

This action is part of KFM’s **catalog governance layer** (STAC/DCAT/PROV) and is designed to block:

- Invalid STAC JSON (schema failures)
- KFM-STAC profile violations (missing fields, inconsistent spatiotemporal data)
- Governance-relevant metadata omissions (license, required provenance hooks)

It is intended to be used as a **CI/CD gate** before publishing STAC outputs, generating tiles, ingesting to Neo4j, or attaching Story Nodes.

---

## 🧱 Architecture

### Action ID

Within the KFM repository this action MAY be used in two forms:

1. **Direct script invocation** (current pattern in `stac_validate.yml`):

~~~yaml
- name: 🛰 Run STAC Validator (Composite Action)
  run: |
    set -euo pipefail
    bash .github/actions/stac-validate/entrypoint.sh data/stac
~~~

2. **Composite action usage** (if `action.yml` is defined as a composite action):

~~~yaml
- name: 🛰 Run STAC Validator (Composite Action)
  uses: ./.github/actions/stac-validate
  with:
    stac_root: "data/stac"
    profile: "kfm-stac-v11"
    config_dir: ".github/actions/stac-validate/config"
~~~

> The repo MUST treat these forms as behaviorally equivalent. If `action.yml` is updated,  
> `.github/workflows/stac_validate.yml` MUST be updated to use the canonical interface.

### Inputs (proposed, for `action.yml`)

| Name         | Type   | Default                                | Description                                                                 |
|--------------|--------|----------------------------------------|-----------------------------------------------------------------------------|
| `stac_root`  | string | `data/stac`                            | Root directory containing STAC Collections/Items.                          |
| `profile`    | string | `kfm-stac-v11`                         | STAC profile identifier (e.g., `kfm-stac-v11`).                            |
| `config_dir` | string | `.github/actions/stac-validate/config` | Directory with profile/asset/collection config.                            |
| `fail_fast`  | bool   | `true`                                 | If `true`, stop at first critical failure; otherwise validate everything.  |
| `summary`    | string | `""`                                   | Optional path to write JSON summary (e.g., `_stac-validate-summary.json`). |

> **Schema note:** These inputs MUST be reflected in  
> `schemas/json/github-actions-stac-validate-v11.schema.json`.

### Outputs (proposed)

| Name                  | Type   | Description                                                            |
|-----------------------|--------|------------------------------------------------------------------------|
| `items_checked`       | number | Number of STAC Items validated.                                       |
| `collections_checked` | number | Number of STAC Collections validated.                                 |
| `issues_found`        | number | Total number of validation issues discovered.                         |
| `severity_max`        | string | Highest severity observed (`none`, `warning`, `error`, `critical`).   |
| `summary_path`        | string | Path to JSON summary, if produced.                                    |

These outputs are intended for internal workflows (e.g., telemetry aggregation, dashboards).

### Behavior

At a high level, the action MUST:

1. **Discover STAC content**
   - Recursively traverse `stac_root` for `collection.json` and Item JSON files.
   - Ignore non‑JSON or non‑STAC files unless explicitly configured.

2. **Validate against STAC spec + KFM profile**
   - Use a STAC validator (CLI or library) via `run_stac_validator.py`.
   - Apply the selected `profile` and any extensions from `config/`.
   - Distinguish between **schema errors** and **profile violations**.

3. **Check spatiotemporal consistency** (via `check_spatiotemporal.py`)
   - Validate GeoJSON geometry + `bbox` consistency.
   - Check `datetime` vs `start_datetime`/`end_datetime`.
   - Verify CRS assumptions are consistent with KFM-STAC v11 conventions.

4. **Enforce governance‑linked metadata**
   - Ensure presence of `license`, `providers`, and key lineage/provenance fields.
   - Verify references to FAIR+CARE and sovereignty policies when required.
   - Surface violations as **errors** when they breach KFM governance contracts.

5. **Summarize results**
   - Aggregate per‑file results into a single JSON summary (`summarize_stac_results.py`).
   - Include counts, severities, and per‑file references suitable for dashboards.

6. **Fail on policy‑relevant issues**
   - Exit non‑zero when errors/critical issues are present.
   - Allow warnings to pass but reflect them in summaries and logs.

### Implementation Notes

- `entrypoint.sh` SHOULD:
  - Use strict bash flags (`set -euo pipefail`).
  - Accept `stac_root` as its first argument and optional flags thereafter.
  - Orchestrate `run_stac_validator.py`, `check_spatiotemporal.py`, and summarization.

- `run_stac_validator.py` SHOULD:
  - Integrate with a STAC validator library/CLI.
  - Respect `profile` and `config_dir`.
  - Emit structured JSON (file → list of issues & severities).

- `check_spatiotemporal.py` SHOULD:
  - Parse geometry, `bbox`, and times.
  - Add additional issues to the same structured output format.

- `summarize_stac_results.py` SHOULD:
  - Merge tool outputs into a unified schema.
  - Respect severity thresholds.
  - Optionally write a summary JSON file at the `summary` path.

Any change to:

- STAC profile behavior,
- severity thresholds, or
- mapping from validator output → policy decisions

MUST be:

1. Reflected in `config/profiles.yml` (and related config files).
2. Documented in this README under **Architecture → Behavior**.
3. Tested via `.github/workflows/stac_validate.yml` and updated examples in `docs/data/`.

---

## 🧪 Validation & CI/CD

### Example usage from `.github/workflows/stac_validate.yml`

~~~yaml
- name: 🛰 Run STAC Validator (Composite Action)
  run: |
    set -euo pipefail
    roots=("data/stac")
    for root in "${roots[@]}"; do
      if [[ -d "$root" ]]; then
        echo "Validating STAC root: $root"
        bash .github/actions/stac-validate/entrypoint.sh "$root"
      else
        echo "No STAC directory at $root; skipping."
      fi
    done
~~~

### As a composite action

~~~yaml
jobs:
  stac-validate:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - name: 🛰 Validate STAC 1.x (KFM-STAC v11)
        uses: ./.github/actions/stac-validate
        with:
          stac_root: "data/stac"
          profile: "kfm-stac-v11"
          config_dir: ".github/actions/stac-validate/config"
          fail_fast: true
          summary: "_stac-validate-summary.json"
~~~

### Determinism & failure mode

- The action MUST exit non‑zero if any STAC Collection/Item fails schema validation or violates KFM‑STAC v11 requirements.
- Validation tooling SHOULD be pinned (version-locked) in CI for reproducible outcomes.
- If `fail_fast: false`, the action SHOULD validate all discovered STAC files and return a combined failure.

---

## 📦 Data & Metadata

This action is designed to treat STAC JSON as governed metadata artifacts:

- Inputs:
  - `data/stac/**` (Collections and Items)
  - `.github/actions/stac-validate/config/**` (profile and rule configuration)

- Outputs (optional):
  - `_stac-validate-summary.json` (or the configured `summary` path)

Where present, summaries SHOULD be compatible with KFM telemetry export tooling and must avoid embedding:

- raw secrets (never)
- PII (never)
- disallowed precise coordinates for protected locations (see sovereignty policy)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Validates STAC Items and Collections as catalog-first assets.
- Encourages stable IDs and consistent spatiotemporal fields (`geometry`, `bbox`, `datetime`, `start_datetime`, `end_datetime`).

### DCAT

- Validation outcomes can be summarized into catalog health signals suitable for DCAT-aligned publishing pipelines.

### PROV-O

- Validation runs are treated as pipeline activities; summary outputs can be attached to provenance traces as run artifacts.

---

## ⚖ FAIR+CARE & Governance

- This action is governed under KFM’s FAIR+CARE posture and must:
  - enforce required licensing/provenance fields as policy-relevant metadata
  - avoid leaking sensitive site locations in logs or telemetry
  - remain deterministic and audit-friendly (clear failures, clear summaries)

Telemetry MUST NOT include:

- raw coordinates of sensitive sites beyond what is allowed in governed STAC outputs
- any non-governed or internal STAC drafts not intended for publication

Where necessary, telemetry SHOULD be aggregated (e.g., counts per collection) rather than per-feature details.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                  |
|--------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-12-09 | Aligned with KFM-MDP v11.2.6; documented inputs/outputs; clarified KFM-STAC v11 profile integration.    |
| v11.2.2 | 2025-11-28 | Initial governed README for stac-validate; aligned with `stac_validate.yml` and KFM STAC catalog flows. |

<div align="center">

🛰 **Kansas Frontier Matrix — STAC Validation Composite Action (v11.2.3)**
Catalog-First · FAIR+CARE-Governed · Provenance-Aware

[⬅ GitHub Infra Overview](../../README.md) · [📊 CI/CD Workflows](../../workflows/README.md) · [📚 Data & STAC Standards](../../../docs/data/README.md)  
[⚖ Governance](../../../docs/standards/governance/ROOT-GOVERNANCE.md) · [🧭 FAIR+CARE](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) · [🪶 Sovereignty Policy](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>
