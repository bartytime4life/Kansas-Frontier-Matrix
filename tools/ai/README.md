---
title: "KFM tools/ai — README"
path: "tools/ai/README.md"
version: "v0.1.0"
last_updated: "2025-12-18"
status: "draft"
doc_kind: "Guide"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:subsystem:tools-ai-readme:v0.1.0"
semantic_document_id: "kfm-tools-ai-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:subsystem:tools-ai-readme:v0.1.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "speculative_additions"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# KFM tools/ai — README

## 📘 Overview

### Purpose
- Define conventions for AI/ML utilities housed under `tools/ai/`.
- Ensure AI tooling aligns with the canonical pipeline stage “AI Analysis and QA” and its governance gates.
- Standardize where AI artifacts live (experiments, model cards, provenance, metrics).

### Non-goals
- `tools/ai/` is not the production inference service layer.
- This document does not define new API fields/endpoints (use API Contract Extension template).
- This does not enumerate the full AI tool inventory (not confirmed in repo until `tools/ai/` is enumerated).

### Audience
- Contributors building:
  - feature extractors and labelers,
  - training/evaluation runners,
  - inference batch scorers that emit evidence artifacts,
  - QA/bias/sanity checks for model outputs.

### Status
- Draft. Fill in concrete tool inventory and entrypoints after repo scan (**not confirmed in repo**).

## 🗂️ Directory Layout

### Expected file tree for this sub-area
~~~text
tools/
├── 🤖 ai/
│   └── 🧰 README.md
└── 📁 … (other tool areas; not confirmed in repo)
~~~

### Key files and what they mean
| Path | Purpose | Owner |
|---|---|---|
| `tools/ai/README.md` | AI tooling conventions and governance gates. | KFM Maintainers (TBD) |

## 🧭 Context

### System placement (pipeline stage)
- KFM’s high-level pipeline includes an “AI Analysis and QA” stage where ML models enrich data and governance checks run in parallel.
- AI tooling must remain provenance-anchored and must not bypass the catalogs/graph/API boundaries.

### Dependencies
- AI tools typically require a reproducible environment:
  - pinned libraries,
  - fixed random seeds where feasible,
  - captured model checkpoint identifiers.
- Prefer containerized execution when available.

### Upstream inputs
- Trusted datasets and features from:
  - `data/processed/` (preferred for training/evaluation inputs)
  - STAC-indexed assets from `data/stac/` (preferred for imagery/rasters)
- Graph exports or API-derived training labels (if applicable; specific sources not confirmed in repo).

### Downstream outputs
- **Experiment artifacts**: `mcp/experiments/` (reports, metrics, plots, comparisons)
- **Run artifacts**: `mcp/runs/<run-id>/` (logs, manifests, checksums, provenance)
- **Model documentation**: `mcp/model_cards/` (recommended location; confirm in repo)
- **Derived datasets** (if promoted): `data/processed/` + corresponding STAC/DCAT/PROV updates
- **Evidence artifacts** for graph/UI consumption:
  - predictions + uncertainty
  - explanation sidecars (feature attributions, supporting assets)
  - provenance pointers to the run and model version

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Trusted inputs<br/>data/processed/ + STAC"] --> B["AI tool run<br/>tools/ai/..."]
  B --> C["Predictions + uncertainty<br/>(evidence artifacts)"]
  B --> D["Evaluation metrics<br/>mcp/experiments/"]
  B --> E["Model card update<br/>mcp/model_cards/"]
  B --> F["Run manifest + PROV<br/>mcp/runs/<run-id>/"]

  C --> G["Catalog + provenance alignment<br/>STAC/DCAT/PROV"]
  G --> H["Graph ingestion (via pipelines)"]
  H --> I["API"]
  I --> J["UI / Story Nodes / Focus Mode"]
~~~

## 🧱 Architecture

### Key concepts
- **Evidence-first AI**: AI outputs must be treated as evidence products with provenance, not as authoritative truth.
- **Model versioning**: Every prediction must be attributable to a model/version and a run_id.
- **Uncertainty required for scores** (recommended): If a tool emits a confidence/probability score, it should also emit an uncertainty measure or calibration artifact when feasible.
- **Human-in-the-loop**: For high-impact outputs (e.g., candidate site detection), treat AI as triage; require review gates.

### Components
| Component | Responsibility | Entry points |
|---|---|---|
| Feature/label utilities | Prepare training/eval datasets, labeling aids. | tool-specific (not confirmed) |
| Training runners | Train models with reproducibility controls. | tool-specific (not confirmed) |
| Evaluation harness | Metrics, calibration, error analysis. | tool-specific (not confirmed) |
| Batch inference | Generate evidence artifacts for downstream ingestion. | tool-specific (not confirmed) |
| Governance checks | Bias/sensitivity scans; sanity bounds. | CI + local |
| Reporting | MCP experiment reports and model cards. | `mcp/experiments/`, `mcp/model_cards/` |

### Interfaces

Recommended CLI contract:
- `--config <path>`
- `--run-id <run-id>`
- `--seed <int>` (or seed in config)
- `--output-dir <path>`
- `--dry-run` (where feasible)
- `--promote` (only for `data/processed/` writes)

Recommended outputs contract:
- `predictions.*` (format depends on task)
- `metrics.json`
- `manifest.json` (inputs/outputs/checksums)
- `provenance.*` (PROV activity/relations)
- model card update artifact (if training or updating a model)

### Failure modes
- Training/evaluation data leakage (label leakage, temporal leakage).
- Non-reproducible training (unfixed seeds, drifting dependencies).
- “Score without provenance” (predictions missing model version and run_id).
- Sensitive location leakage (high-precision coordinates exported without governance).
- Narrative contamination (LLM-generated claims without evidence grounding).

### Security notes
- Avoid sending data to external services unless explicitly allowed and documented under governance/security.
- Treat any model weights or embeddings derived from restricted data as restricted artifacts.
- Do not log raw sensitive content; keep logs redacted.

## 📦 Data & Metadata

### Entities (what data you touch)
| Entity | Format | Where |
|---|---|---|
| Training/eval datasets | parquet/csv/jsonl/etc. | `data/processed/` (preferred) |
| Model checkpoints | binary files | artifact store / release packaging (not confirmed) |
| Predictions | json/csv/parquet/geojson/etc. | `mcp/runs/` + optional `data/work/` |
| Metrics & calibration | json + plots | `mcp/experiments/` |
| Model cards | markdown | `mcp/model_cards/` (recommended) |

### Metadata requirements
- For every run:
  - run_id
  - model identifier + version/checkpoint hash
  - dataset identifiers + splits definition
  - seeds and environment identifiers
  - checksums for outputs

### Provenance (PROV)
- Emit a PROV Activity capturing:
  - which datasets were used (and their versions)
  - which code version produced outputs (commit_sha)
  - which model version produced predictions
  - which outputs were generated (and checksums)

## 🌐 STAC, DCAT & PROV Alignment

### If this doc introduces/updates any dataset
Examples (task-dependent; not confirmed in repo):
- Tile-level prediction rasters (STAC Items with GeoTIFF assets)
- Vector predictions (STAC Items with GeoJSON assets)
- Evaluation datasets (DCAT datasets)

Required alignment:
- **STAC**: Items/Collections with proper extents, roles, and version pointers.
- **DCAT**: dataset record with license and access notes.
- **PROV**: explicit linkage from run activity to generated prediction artifacts.

### If this doc introduces/updates any API
- Use API Contract Extension template.

## 🛠️ Implementation

### Setup
- Prefer containerized execution when available.
- Fix and record seeds for any stochastic process.
- Ensure tool configs reference trusted inputs (`data/processed/`, STAC IDs) whenever possible.

### How to run
~~~bash
# Example pattern — adjust to actual entrypoint (not confirmed in repo)
python -m tools.ai.<tool> \
  --config tools/ai/<tool>/config.yaml \
  --run-id <run-id> \
  --seed 12345
~~~

### Configuration
Recommended fields:
- `data.inputs`: dataset IDs/paths, split definitions, filters
- `model`: architecture + checkpoint IDs
- `repro`: seed(s), deterministic flags, environment identifiers
- `governance`: sensitivity handling, PII scans, redaction rules
- `outputs`: where to write predictions/metrics/manifests

### Output artifacts
- Always include a manifest + checksums.
- If predictions are intended for graph/UI:
  - include uncertainty (recommended)
  - include explanation/evidence pointers where feasible
  - include model version and run_id on every record

## 🧪 Validation & CI/CD

### CI checks (expected)
- Tool outputs must pass schema/sanity checks (bounds, required fields).
- Provenance completeness checks:
  - no predictions without model version/run_id
  - no promoted artifacts without checksums
- Bias/sensitivity checks where applicable (especially for discovery or narrative-adjacent outputs).
- Docs front-matter + protocol validation for reports/model cards.

### Local validation commands
~~~bash
# Examples — adjust to actual repo scripts (not confirmed in repo)
# make test
# make docs-validate
# python -m tools.ai.validate_outputs --run-id <run-id>
~~~

## ⚖ FAIR+CARE & Governance

### Governance review triggers
- A new model is introduced or an existing model is updated for pipeline use.
- AI outputs are used for Story Nodes / Focus Mode narratives.
- AI outputs include or infer sensitive locations.
- External services or proprietary datasets are introduced.
- Any change that affects public-facing confidence claims or risk of harm.

### Sensitivity handling
- Apply coordinate generalization/redaction before exporting public outputs when required.
- Attach sensitivity/classification flags and route through review gates.

### Ethical AI notes
- Treat AI as assistive triage for discovery tasks; require human validation for high-stakes claims.
- Maintain a model card describing intended use, limitations, and evaluation context.

## 🕰️ Version History
| Date | Version | Change | Author |
|---|---|---|---|
| 2025-12-18 | v0.1.0 | Initial governed README for `tools/ai`. | <author> |

## Footer refs:
- `docs/MASTER_GUIDE_v12.md`
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `KFM’s AI Project Reference Data`