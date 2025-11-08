---
title: "⚖️ FAIR+CARE Validation Workflow — `faircare-validate.yml` (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/workflows/faircare-validate.yml.md"
version: "v9.9.0"
last_updated: "2025-11-08"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v9.9.0/sbom.spdx.json"
manifest_ref: "../../releases/v9.9.0/manifest.zip"
telemetry_ref: "../../releases/v9.9.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/workflows/faircare-validate-v1.json"
governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# ⚖️ **FAIR+CARE Validation Workflow — `faircare-validate.yml`**  
`docs/workflows/faircare-validate.yml.md`

**Purpose:**  
Define the **GitHub Actions** workflow that validates datasets and docs for **FAIR+CARE** compliance,  
performs **ethics/PII scans**, enforces **data contracts**, manages **abandonment candidates**, and  
emits **governance-ready reports** with full telemetry for Diamond⁹ / Crown∞Ω certification.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange)](../standards/faircare.md)
[![Status: Automated](https://img.shields.io/badge/Status-Automated-brightgreen)](#)

</div>

---

## 📘 Overview

`faircare-validate.yml` is the **ethics and governance gate** for the Kansas Frontier Matrix.  
It operates on tabular, spatial, and documentation changes to ensure:

- ✅ **FAIR**: Findable / Accessible / Interoperable / Reusable checks  
- ✅ **CARE**: Collective benefit, Authority to control, Responsibility, Ethics  
- ✅ **Contracts**: JSON Schema & data-contract conformance (e.g., `data-contract-v3.json`)  
- ✅ **PII/Sensitive**: Automated redaction and cultural sensitivity screening  
- ✅ **Quarantine**: Noncompliant assets moved to `abandonment_candidates/` with registry entry  
- ✅ **Reports**: Machine-readable audit, provenance, and council-ready ethics review packs

All results are exported under `reports/` and appended to `focus-telemetry.json`.

---

## 🗂️ Trigger & Scope

| Trigger | Paths | Notes |
|--------:|------|------|
| `pull_request` | `data/**`, `docs/**`, `schemas/**` | Blocks merge on failure |
| `push` (protected) | `data/**`, `docs/**`, `schemas/**` | Required for releases |
| `schedule` | nightly | Continuous surveillance of staged data |

**Ignore:** binaries (`*.tif`, `*.pmtiles`) for lint; metadata is still validated.

---

## 🧩 Workflow (YAML)

```yaml
name: "FAIR+CARE Validate (Governed)"

on:
  pull_request:
    paths: ["data/**", "docs/**", "schemas/**"]
  push:
    branches: ["main", "release/**"]
    paths: ["data/**", "docs/**", "schemas/**"]
  schedule:
    - cron: "0 3 * * *"

permissions:
  contents: read
  id-token: write

concurrency:
  group: faircare-validate-${{ github.ref }}
  cancel-in-progress: true

jobs:
  validate:
    runs-on: ubuntu-22.04
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with: { python-version: "3.11" }

      - name: Install validators
        run: |
          pip install -r requirements.txt
          pip install jsonschema jq yq

      - name: Validate data contracts (schema)
        run: |
          python scripts/validate_contract.py \
            --root data/ --contract docs/contracts/data-contract-v3.json \
            --out reports/faircare/contract_summary.json

      - name: FAIR+CARE audit (ethics & governance)
        run: |
          python scripts/faircare_audit.py \
            --input data/ --standards docs/standards/faircare.yaml \
            --out reports/faircare/faircare_summary.json

      - name: PII & sensitive content scan
        run: |
          python scripts/pii_scan.py \
            --input data/ --rules docs/standards/pii_rules.yaml \
            --out reports/faircare/pii_scan.json

      - name: Flag noncompliant → abandonment candidates
        run: |
          python scripts/abandonment_triage.py \
            --violations reports/faircare/faircare_summary.json \
            --pii reports/faircare/pii_scan.json \
            --staging data/work/staging/tabular \
            --quarantine data/work/staging/tabular/abandonment_candidates \
            --registry data/work/staging/tabular/abandonment_candidates/abandonment_registry.json

      - name: Generate provenance trace
        run: |
          python scripts/make_provenance.py \
            --root data/ --out reports/faircare/provenance_trace.json

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: faircare_reports
          path: |
            reports/faircare/**
            data/work/staging/tabular/abandonment_candidates/abandonment_registry.json

      - name: Emit telemetry
        run: |
          python scripts/emit_telemetry.py \
            --kind faircare \
            --summary reports/faircare/faircare_summary.json \
            --pii reports/faircare/pii_scan.json \
            --contract reports/faircare/contract_summary.json \
            --out faircare_telemetry.json

      - name: Append telemetry to unified log
        run: |
          python scripts/merge_telemetry.py \
            --in faircare_telemetry.json \
            --dest releases/v9.9.0/focus-telemetry.json
```

---

## 🔎 Inputs, Artifacts & Outputs

| Type | Key/Path | Description |
|------|----------|-------------|
| **Input** | `data/**` | Incoming tabular/spatial/metadata under review |
| **Artifact** | `reports/faircare/faircare_summary.json` | FAIR+CARE audit results |
| **Artifact** | `reports/faircare/provenance_trace.json` | Lineage map (DCAT/PROV-O) |
| **Artifact** | `reports/faircare/pii_scan.json` | Detected PII / sensitive markers |
| **Artifact** | `abandonment_registry.json` | Quarantined dataset registry |
| **Telemetry** | `releases/v9.9.0/focus-telemetry.json` | Aggregated governance metrics |

---

## ✅ FAIR+CARE Rule Set

**FAIR**  
- *F1 (Findable):* Required front-matter keys; STAC/DCAT presence; stable IDs.  
- *A1 (Accessible):* License clarity; role-based access; reproducible links.  
- *I1 (Interoperable):* JSON Schema OK; DCAT 3.0 vocab; CRS & units declared.  
- *R1 (Reusable):* Provenance, versioning, checksum; contract-aligned fields.

**CARE**  
- *Collective Benefit:* No extractive use; community benefit tags.  
- *Authority to Control:* `care_tag` enforced; consent and opt-out honored.  
- *Responsibility:* PII scan; redaction or masking pipelines.  
- *Ethics:* Cultural sensitivity checks (Indigenous data, minors, health).

**Failure policy:** Noncompliant assets are moved to `abandonment_candidates/` with reason + checksum.

---

## 🧭 Abandonment Candidates Integration

When violations occur, the workflow:

1. Moves files to `data/work/staging/tabular/abandonment_candidates/`  
2. Appends a record to `abandonment_registry.json` (id, reason, reviewer, checksum)  
3. Produces reports in `reports/` (validation, provenance, ethics review)  
4. Emits telemetry events: `dataset-flagged`, `dataset-remediated`, `dataset-archived`  
5. Blocks publication until **FAIR+CARE Council** marks the dataset as remediated or archived

---

## 📊 Telemetry & Sustainability

Appends governance metrics to `focus-telemetry.json`:

| Metric | Example | Notes |
|--------|---------|------|
| `datasets_scanned` | 152 | Count by type (csv/parquet/geojson) |
| `violations_found` | 7 | Sum of FAIR+CARE failures |
| `quarantined` | 3 | Added to abandonment registry |
| `energy_wh` | 96 | Runner energy estimate (ISO 50001) |
| `duration_min` | 12.4 | Total runtime |
| `policy_version` | `faircare@2025.4` | Standards pack hash |

---

## 🔒 Supply Chain & Provenance

- Optional **Syft** SBOM and **SLSA** attestations for governance evidence.  
- **OIDC** used for artifact signing if redaction packages are produced.  
- Provenance maps (`provenance_trace.json`) link datasets → sources → contracts.

---

## 🧭 Mermaid — High-Level Flow

```mermaid
flowchart LR
  A["PR/Push/Schedule"] --> B["Data-Contract + FAIR+CARE + PII"]
  B --> C{"Compliant?"}
  C -->|Yes| D["Provenance Trace + Reports"]
  C -->|No| E["Quarantine → abandonment_candidates + Registry"]
  D --> F["Upload Artifacts + Telemetry"]
  E --> F
  F --> G["Governance Ledger + Council Review"]
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v9.9.0 | 2025-11-08 | `@kfm-governance` | Adds quarantine & registry, PII scan, provenance export, telemetry merge. |
| v9.8.0 | 2025-11-05 | `@kfm-data` | Expanded FAIR+CARE checks and contract validation. |
| v9.7.0 | 2025-11-02 | `@kfm-core` | Initial governance validation workflow doc. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Ethical Automation × FAIR+CARE Governance × Sustainable CI/CD*  
© 2025 Kansas Frontier Matrix · CC-BY 4.0 · Master Coder Protocol v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Workflows Index](README.md) · [Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>

