---
title: "📈 Telemetry Export Workflow — `telemetry-export.yml` (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/workflows/telemetry-export.yml.md"
version: "v10.2.4"
last_updated: "2025-11-12"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/workflows/telemetry-export-v3.json"
governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📈 **Telemetry Export Workflow — `telemetry-export.yml`**  
`docs/workflows/telemetry-export.yml.md`

**Purpose:**  
Aggregate and normalize **build, validation, and governance metrics** from all CI jobs (docs, STAC/DCAT, FAIR+CARE, AI training, web builds) into a single, FAIR+CARE-aligned telemetry ledger: **`releases/<version>/focus-telemetry.json`**.  
Provides a **machine-readable, auditable** source for sustainability dashboards, governance reviews, and certification under **MCP-DL v6.3** and **Diamond⁹ Ω / Crown∞Ω**.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blueviolet)](../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange)](../standards/faircare.md)
[![Status: Automated](https://img.shields.io/badge/Status-Automated-brightgreen)](#)

</div>

---

## 📘 Overview

`telemetry-export.yml` consolidates metrics emitted by other workflows, including:

- **Documentation** — `docs-lint.yml` (front-matter, links, mermaid guardrails)  
- **Governance** — `faircare-validate.yml` (FAIR+CARE, PII, abandonment registry)  
- **Catalog** — `stac-validate.yml` (STAC/DCAT + asset checksums)  
- **AI** — `ai-train.yml` (training/eval, drift, explainability, SBOM, SLSA)  
- **Builds** — web/pipelines build time, size, cache hits, test results

All inputs are normalized to a **stable telemetry schema v3** and appended to **`focus-telemetry.json`** for longitudinal analysis.

---

## 🗂️ Trigger & Scope

| Trigger | Paths | Notes |
|--------:|------|------|
| `workflow_run` | listens to success of: docs-lint, faircare-validate, stac-validate, ai-train | primary mode |
| `schedule` | hourly | roll-up of last N runs; trend refresh |
| `workflow_dispatch` | manual | backfill or emergency re-aggregation |

**Upstream requirement:** Each contributing workflow **must** emit a JSON summary conforming to its telemetry schema (see **Schemas & Contracts**).

---

## 🧩 Workflow (YAML)

```yaml
name: "Telemetry Export (Governed)"

on:
  workflow_run:
    workflows:
      - "Docs Lint (Governed)"
      - "FAIR+CARE Validate (Governed)"
      - "STAC/DCAT Validate (Governed)"
      - "AI Train (Governed)"
    types: [completed]
  schedule:
    - cron: "0 * * * *" # hourly aggregation
  workflow_dispatch: {}

permissions:
  contents: write
  id-token: write

concurrency:
  group: telemetry-export-${{ github.ref }}
  cancel-in-progress: true

jobs:
  export:
    runs-on: ubuntu-22.04
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }

      - name: Install tooling
        run: |
          pip install jsonschema jq
          pip install -r requirements.txt || true

      - name: Collect inputs
        run: |
          mkdir -p .telemetry/in .telemetry/out releases/v10.2.0
          python scripts/pull_artifact.py --name docs_lint_reports    --out .telemetry/in/docs    || true
          python scripts/pull_artifact.py --name faircare_reports     --out .telemetry/in/faircare || true
          python scripts/pull_artifact.py --name stac_validation_reports --out .telemetry/in/stac || true
          python scripts/pull_artifact.py --name ai_*_artifacts       --out .telemetry/in/ai     || true

      - name: Normalize to telemetry schema v3
        run: |
          python scripts/normalize_docs_lint.py \
            --in .telemetry/in/docs \
            --schema schemas/telemetry/workflows/docs-lint-v3.json \
            --out .telemetry/out/docs.json || echo "{}" > .telemetry/out/docs.json

          python scripts/normalize_faircare.py \
            --in .telemetry/in/faircare \
            --schema schemas/telemetry/workflows/faircare-validate-v3.json \
            --out .telemetry/out/faircare.json || echo "{}" > .telemetry/out/faircare.json

          python scripts/normalize_stac.py \
            --in .telemetry/in/stac \
            --schema schemas/telemetry/workflows/stac-validate-v3.json \
            --out .telemetry/out/stac.json || echo "{}" > .telemetry/out/stac.json

          python scripts/normalize_ai.py \
            --in .telemetry/in/ai \
            --schema schemas/telemetry/workflows/ai-train-v3.json \
            --out .telemetry/out/ai.json || echo "{}" > .telemetry/out/ai.json

      - name: Merge streams → focus-telemetry.json
        run: |
          python scripts/merge_telemetry.py \
            --in .telemetry/out/*.json \
            --dest releases/v10.2.0/focus-telemetry.json

      - name: Validate unified telemetry
        run: |
          python - <<'PY'
          import json
          from jsonschema import Draft202012Validator
          with open("schemas/telemetry/docs-index-v3.json") as f: schema = json.load(f)
          with open("releases/v10.2.0/focus-telemetry.json") as f: data = json.load(f)
          Draft202012Validator(schema).validate(data)
          print("Unified telemetry valid; events:", len(data.get("events", [])))
          PY

      - name: Export quick summaries
        run: |
          mkdir -p reports/telemetry
          python scripts/summarize_telemetry.py \
            --in  releases/v10.2.0/focus-telemetry.json \
            --out reports/telemetry/summary.json \
            --md  reports/telemetry/summary.md

      - name: Attach artifacts
        uses: actions/upload-artifact@v4
        with:
          name: telemetry_ledger
          path: |
            releases/v10.2.0/focus-telemetry.json
            reports/telemetry/**
```

---

## 🧪 Schemas & Contracts

Each upstream workflow must output a JSON summary conforming to its schema:

| Source | Required Schema | Example Output |
|--------|-----------------|----------------|
| docs-lint | `workflows/docs-lint-v3.json` | `reports/self-validation/docs/lint_summary.json` |
| faircare-validate | `workflows/faircare-validate-v3.json` | `reports/faircare/faircare_summary.json` |
| stac-validate | `workflows/stac-validate-v3.json` | `reports/self-validation/stac_validation.json` |
| ai-train | `workflows/ai-train-v3.json` | `reports/ai/<model>/metrics.json` |

The exporter validates each input against its schema before merging.

---

## 🧮 Metrics & Dimensions

Core fields appended to `focus-telemetry.json`:

| Field | Type | Description |
|------:|------|-------------|
| `event_id` | string | UUIDv4 per record |
| `event_type` | enum | `docs_lint` \| `faircare` \| `stac_validate` \| `ai_train` \| `build` |
| `timestamp` | ISO-8601 | Event time (UTC) |
| `branch` | string | Git ref / release tag |
| `duration_sec` | number | Total workflow runtime |
| `energy_wh` | number | Estimated energy (ISO 50001) |
| `carbon_gco2e` | number | CO₂eq emission estimate |
| `status` | enum | `success` \| `warning` \| `failure` |
| `payload` | object | Validated summary (schema-typed) |

---

## ♻️ Sustainability & Governance

- Tracks **energy** and **duration** per job; computes weekly/monthly aggregates.  
- Flags **hotspots** (long-running, energy-heavy steps) for optimization.  
- Emits a **FAIR+CARE telemetry snapshot** for council review each quarter.  
- Can be configured to **block releases** if required telemetry slices are missing.

---

## 🔐 Supply Chain & Integrity

- Telemetry ledger can be signed with **Sigstore Cosign** and accompanied by **SLSA** attestations.  
- Stored under `releases/<version>/` with the same retention and integrity guarantees as other release artifacts.  
- SBOM pointers (`sbom_ref`) enable end-to-end traceability.

---

## 🧭 Mermaid — High-Level Flow

```mermaid
flowchart LR
  A["Upstream Workflows"] --> B["Normalize & Validate (Schemas v3)"]
  B --> C["Merge → focus-telemetry.json"]
  C --> D["Summaries & Artifacts"]
  D --> E["Governance Ledger & Dashboards"]
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| **v10.2.4** | 2025-11-12 | `@kfm-devops` | Upgraded to telemetry schema v3, unified artifact paths, strengthened validation of upstream summary schemas. |
| v10.1.0 | 2025-11-10 | `@kfm-devops` | Added hourly aggregation, artifact uploader v4, telemetry-export v2. |
| v9.9.0 | 2025-11-08 | `@kfm-devops` | Initial governed telemetry exporter with schema validation and sustainability metrics. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Evidence-Driven Governance × FAIR+CARE Telemetry × Sustainable CI/CD*  
© 2025 Kansas Frontier Matrix · CC-BY 4.0 · Master Coder Protocol v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Workflows Index](README.md) · [Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>