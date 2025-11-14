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
Define a reusable, KFM-native **AI data pipeline cookiecutter** that implements the **event-driven, agent-assisted, deterministic** workflow: **ingest → validate → transform (agent) → publish**, wired into **KFM paths, STAC/DCAT, FAIR+CARE, and CI**.

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

This layout is for **this guide directory** and the **cookiecutter template** it describes.

```text
docs/
└── guides/
    └── pipelines/
        ├── README.md                                   # Pipelines guides index (existing / planned)
        ├── kfm-ai-pipeline-cookiecutter.md             # THIS DOCUMENT
        └── cookiecutter-kfm-ai-pipeline/               # Cookiecutter template root
            ├── cookiecutter.json                       # Cookiecutter configuration
            └── {{ cookiecutter.project_slug }}/        # Rendered project skeleton
                ├── .gitignore
                ├── README.md                           # Pipeline template README (local to project)
                ├── pyproject.toml
                ├── src/
                │   └── {{ cookiecutter.project_slug }}/
                │       ├── __init__.py
                │       ├── cli.py                      # Typer CLI entrypoint
                │       ├── config.py                   # KFM-aware settings (paths, env)
                │       ├── context.py                  # RunContext + step decorator + hashing
                │       ├── ledger.py                   # Append-only run ledger (.jsonl)
                │       ├── agent.py                    # Agent interface (OpenAI-style, JSON-only)
                │       ├── stac.py                     # Minimal STAC item builder + writer
                │       ├── faircare.py                 # FAIR+CARE checks scaffold
                │       └── pipeline/
                │           ├── __init__.py
                │           ├── ingest.py               # Deterministic ingest
                │           ├── validate.py             # Validation + FAIR+CARE overlay
                │           ├── transform.py            # Agent-assisted transform
                │           └── publish.py              # Assets + STAC + DCAT publish
                ├── schemas/
                │   ├── run_context.schema.json         # RunContext JSON Schema
                │   ├── agent_action.schema.json        # Agent action contract
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
                │   └── test_pipeline_smoke.py          # Ingest/validate smoke tests
                └── .github/
                    └── workflows/
                        └── ci.yml                      # Lint + tests + schema validation
