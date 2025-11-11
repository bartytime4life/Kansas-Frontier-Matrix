---
title: "🧠 AI Training Workflow — `ai-train.yml` (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/workflows/ai-train.yml.md"
version: "v10.1.0"
last_updated: "2025-11-10"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.1.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.1.0/manifest.zip"
telemetry_ref: "../../releases/v10.1.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/workflows/ai-train-v2.json"
governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧠 **AI Training Workflow — `ai-train.yml`**  
`docs/workflows/ai-train.yml.md`

**Purpose:**  
Define the **GitHub Actions workflow** that trains and evaluates KFM AI models (e.g., **Focus Transformer v2**), enforces **FAIR+CARE** & **MCP-DL v6.3** governance, generates **Model Cards**, computes **bias/drift/explainability** metrics, signs artifacts (SLSA/OIDC), and exports **telemetry** & **SBOM** for Diamond⁹/Crown∞Ω certification.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blueviolet)](../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange)](../standards/faircare.md)
[![Status](https://img.shields.io/badge/Status-Automated-brightgreen)](#)

</div>

---

## 📘 Overview

This workflow orchestrates **data-to-model** steps with auditable governance:

- ✅ *Reproducibility*: pinned environments, lockfiles, deterministic seeds, artifact versioning.  
- ⚖️ *Ethics by design*: **FAIR+CARE** checks, PII scans, data-contract enforcement, consent gates.  
- 🔍 *Quality*: unit tests, eval suites, out-of-distribution & **drift** checks, **SHAP/LIME/IG** explainability.  
- 🔐 *Supply chain*: **SLSA** provenance, SBOM, container/image signing (OIDC + Cosign).  
- 📊 *Telemetry*: training & evaluation metrics, energy usage, bias/fairness — emitted to `focus-telemetry.json`.

---

## 🗂️ Trigger & Inputs

| Trigger | When | Inputs (defaults) |
|--------:|------|--------------------|
| `workflow_dispatch` | Manual training runs | `model_id`, `dataset_ref`, `config_path`, `epochs`, `device` |
| `push` | Changes under `src/ai/**`, `data/training/**`, `configs/ai/**` | — |
| `schedule` | Nightly model health check | — |

**Input schema (example):**
```yaml
on:
  workflow_dispatch:
    inputs:
      model_id: { description: "e.g. focus_transformer_v2", required: true, type: string }
      dataset_ref: { description: "STAC Collection ID or data bundle", required: true, type: string }
      config_path: { description: "Training config", default: "configs/ai/focus_v2.yaml", type: string }
      epochs: { description: "Epoch count", default: "3", type: number }
      device: { description: "cpu|cuda", default: "cuda", type: choice, options: [cpu, cuda] }
```

---

## 🧩 Workflow (YAML)

```yaml
name: "AI Train (Governed)"

on:
  push:
    paths:
      - "src/ai/**"
      - "data/training/**"
      - "configs/ai/**"
  workflow_dispatch:
    inputs:
      model_id: { required: true, type: string }
      dataset_ref: { required: true, type: string }
      config_path: { required: true, default: "configs/ai/focus_v2.yaml", type: string }
      epochs: { required: false, default: "3", type: number }
      device: { required: false, default: "cuda", type: choice, options: [cpu, cuda] }

permissions:
  contents: read
  id-token: write
  actions: read

concurrency:
  group: ai-train-${{ github.ref }}-${{ inputs.model_id }}
  cancel-in-progress: true

env:
  PYTHON_VERSION: "3.11"
  PIP_CACHE_DIR: ~/.cache/pip
  HF_HOME: ~/.cache/huggingface
  PIP_DISABLE_PIP_VERSION_CHECK: "1"

jobs:
  train:
    name: Train & Validate (${{ inputs.model_id || 'focus_transformer_v2' }})
    runs-on: ${{ inputs.device == 'cuda' && 'ubuntu-22.04-gpu' || 'ubuntu-22.04' }}
    timeout-minutes: 480
    env:
      MODEL_ID: ${{ inputs.model_id }}
      DATASET_REF: ${{ inputs.dataset_ref }}
      CONFIG_PATH: ${{ inputs.config_path }}
      EPOCHS: ${{ inputs.epochs }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python ${{ env.PYTHON_VERSION }}
        uses: actions/setup-python@v5
        with: { python-version: ${{ env.PYTHON_VERSION }} }

      - name: Cache deps
        uses: actions/cache@v4
        with:
          path: |
            ${{ env.PIP_CACHE_DIR }}
            ${{ env.HF_HOME }}
          key: ${{ runner.os }}-pip-${{ hashFiles('pyproject.toml','poetry.lock','requirements.lock') }}
          restore-keys: ${{ runner.os }}-pip-

      - name: Install deps
        run: |
          pip install -U pip wheel
          pip install -r requirements.txt -r requirements.train.txt

      - name: Validate data contract
        run: |
          python scripts/validate_contract.py \
            --dataset $DATASET_REF \
            --contract docs/contracts/data-contract-v3.json \
            --out data/work/staging/tabular/tmp/validation/contract_${MODEL_ID}.json

      - name: FAIR+CARE audit
        run: |
          python scripts/faircare_audit.py \
            --dataset $DATASET_REF \
            --out data/work/staging/tabular/tmp/validation/faircare_${MODEL_ID}.json

      - name: Train model
        env:
          HF_TOKEN: ${{ secrets.HF_TOKEN }}
        run: |
          python src/ai/train.py \
            --model $MODEL_ID \
            --data $DATASET_REF \
            --config $CONFIG_PATH \
            --epochs $EPOCHS \
            --device ${{ inputs.device }}

      - name: Evaluate (metrics + OOD + drift)
        run: |
          python src/ai/eval.py --model $MODEL_ID --data $DATASET_REF --out reports/ai/${MODEL_ID}/metrics.json
          python src/ai/drift_check.py --model $MODEL_ID --baseline releases/models/${MODEL_ID}/baseline_metrics.json --out reports/ai/${MODEL_ID}/drift.json

      - name: Explainability (SHAP/LIME/IG)
        run: |
          python src/ai/explainability/run_shap.py --model $MODEL_ID --data $DATASET_REF --out reports/ai/${MODEL_ID}/explainability.json

      - name: Generate Model Card
        run: |
          python scripts/make_model_card.py \
            --model $MODEL_ID \
            --metrics reports/ai/${MODEL_ID}/metrics.json \
            --drift reports/ai/${MODEL_ID}/drift.json \
            --explain reports/ai/${MODEL_ID}/explainability.json \
            --template docs/templates/model_card.md \
            --out releases/models/${MODEL_ID}/MODEL_CARD.md

      - name: Build SBOM (SPDX)
        uses: anchore/syft-action@v1
        with:
          args: "dir:. -o spdx-json=./releases/v10.1.0/sbom.spdx.json"

      - name: Attest Build Provenance (SLSA)
        uses: slsa-framework/slsa-github-generator/actions/attest-build-provenance@v1
        with:
          subject-path: "releases/models/${{ env.MODEL_ID }}/"

      - name: Install Cosign
        uses: sigstore/cosign-installer@v3
      - name: Cosign sign
        run: |
          cosign sign-blob --yes --output-signature releases/models/${MODEL_ID}/signature.sig \
            --output-certificate releases/models/${MODEL_ID}/certificate.pem \
            releases/models/${MODEL_ID}/MODEL_CARD.md

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: ai_${{ env.MODEL_ID }}_artifacts
          path: |
            releases/models/${{ env.MODEL_ID }}/
            reports/ai/${{ env.MODEL_ID }}/
            data/work/staging/tabular/tmp/validation/*${{ env.MODEL_ID }}*.json

      - name: Emit telemetry
        run: |
          python scripts/emit_telemetry.py \
            --kind ai_train \
            --summary reports/ai/${MODEL_ID}/metrics.json \
            --drift reports/ai/${MODEL_ID}/drift.json \
            --explain reports/ai/${MODEL_ID}/explainability.json \
            --out telemetry_ai_${MODEL_ID}.json

      - name: Append telemetry to unified log
        run: |
          python scripts/merge_telemetry.py \
            --in telemetry_ai_${MODEL_ID}.json \
            --dest releases/v10.1.0/focus-telemetry.json
```

---

## 🧮 Inputs, Artifacts & Outputs

| Type | Key | Description |
|------|-----|-------------|
| **Input** | `model_id` | Model to train (e.g., `focus_transformer_v2`) |
| **Input** | `dataset_ref` | STAC/contracted dataset identifier |
| **Artifact** | `releases/models/<model_id>/MODEL_CARD.md` | Generated Model Card (governed) |
| **Artifact** | `reports/ai/<model_id>/*.json` | Metrics, drift, explainability |
| **Artifact** | `releases/v10.1.0/sbom.spdx.json` | Build SBOM for supply-chain integrity |
| **Telemetry** | `releases/v10.1.0/focus-telemetry.json` | Training time, energy, bias/fairness, drift |

---

## ⚖️ FAIR+CARE & Governance

| Principle | Enforcement | Evidence |
|-----------|-------------|----------|
| **Findable** | STAC/DCAT registration; model & dataset IDs in outputs | `manifest_ref` |
| **Accessible** | Role-scoped artifact access; public model cards | Repo artifacts |
| **Interoperable** | JSON Schema, DCAT 3.0; optional ONNX/MLflow exports | Metadata & SBOM |
| **Reusable** | CC-BY for docs; MIT for code; configs version-locked | LICENSE + configs |
| **CARE** | PII scan, consent checks, ethics gating, council approval | Validation reports |

**Abandonment candidates:** model training **must not** ingest quarantined data from `data/work/staging/tabular/abandonment_candidates/` unless **governance-approved** remediation has occurred (job will fail otherwise).

---

## 🔐 Security & Supply Chain

- **OIDC + Cosign** for signing; provenance via **SLSA** attestations.  
- **Trivy**/SAST recommended before training to scan images/deps.  
- Ephemeral runners; no long-lived secrets.  
- Least-privilege `permissions`.

---

## 🔍 Telemetry & Sustainability

Emitted to `focus-telemetry.json` (schema `ai-train-v2`):

| Metric | Example | Notes |
|--------|---------|------|
| `train_time_min` | 142.3 | End-to-end duration |
| `energy_wh` | 1835 | Runner power telemetry or estimator |
| `f1_macro` | 0.842 | Primary quality metric |
| `bias_score` | 0.05 | Lower is better |
| `drift_flag` | false | From drift check |
| `explainability.stability` | 0.93 | LIME/SHAP stability |
| `license_spdx` | `Apache-2.0` | From SBOM/license scan |

---

## 🧭 Mermaid: High-Level Flow

```mermaid
flowchart LR
  A["Data (STAC/DCAT)"] --> B["Contract & FAIR+CARE Validation"]
  B --> C["Train (Deterministic Seeds)"]
  C --> D["Evaluate + Drift + Explainability"]
  D --> E["Model Card + SBOM + SLSA Attest"]
  E --> F["Upload Artifacts + Telemetry Merge"]
  F --> G["Governance Review & Publish"]
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| **v10.1.0** | 2025-11-10 | `@kfm-devops` | Upgraded to v10.1.0 artifacts; added IG explainability; telemetry schema v2. |
| v9.9.0 | 2025-11-08 | `@kfm-devops` | Initial governed AI training workflow doc with SLSA/Cosign, drift/explainability, and telemetry export. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Governed AI × FAIR+CARE Ethics × SLSA Provenance*  
© 2025 Kansas Frontier Matrix · CC-BY 4.0 · Master Coder Protocol v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Workflows Index](README.md) · [Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>
