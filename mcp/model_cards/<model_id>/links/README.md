<!--
📍 Path: mcp/model_cards/<model_id>/links/README.md
Purpose: Curated source index + provenance map for writing/maintaining the <model_id> model card.
-->

# 🔗 `<model_id>` — Model Card Links (Kansas Frontier Matrix)

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-111827?logo=github)
![MCP](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-2563EB)
![Evidence](https://img.shields.io/badge/Evidence-First%20%26%20Traceable-16A34A)
![Metadata](https://img.shields.io/badge/Metadata-STAC%20%2B%20DCAT%20%2B%20PROV-059669)
![Governance](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-F59E0B)

> [!NOTE]
> This folder is the **source-of-truth link index** for everything the `<model_id>` model card claims.
> If it’s not backed by a link here (or a pinned repo permalink), it’s not “publishable evidence.” ✅

---

## 📁 Folder layout (recommended)

```text
mcp/
  model_cards/
    <model_id>/
      links/
        README.md
        assets/                       # 👇 keep filenames ASCII + stable for clean linking
          kfm_comprehensive_technical_documentation.pdf
          kfm_architecture_features_design.pdf
          kfm_ai_system_overview.pdf
          kfm_ui_system_overview.pdf
          kfm_data_intake_guide.pdf
          kfm_latest_ideas_future_proposals.pdf
          kfm_innovative_concepts.pdf
          kfm_additional_project_ideas.pdf
          kfm_open_source_mapping_hub_design.pdf
          kfm_markdown_guide_v13.md
          packs_ai_concepts.pdf
          packs_geospatial_webgl.pdf
          packs_programming_resources.pdf
          packs_data_management_bayesian.pdf
          scientific_method_master_coder_protocol.pdf
```

> [!TIP]
> The original PDFs include emojis, long names, and Unicode punctuation. For repo durability, keep **sanitized aliases** in `assets/` and link to those.

---

## 🧭 Quick navigation

- [✅ How to use this link index](#-how-to-use-this-link-index)
- [🧱 Canonical project references (assets)](#-canonical-project-references-assets)
- [🧩 Repo-native “pinned sources”](#-repo-native-pinned-sources)
- [🧾 Model-card section → evidence map](#-model-card-section--evidence-map)
- [➕ Adding new links](#-adding-new-links)
- [🧰 Maintenance checklist](#-maintenance-checklist)

---

## ✅ How to use this link index

1. **When drafting the model card**, cite claims to one (or more) of the sources below.
2. Prefer **repo permalinks** (pinned commit URLs) for anything in-repo, so citations remain stable.
3. Treat **policy gates** and **provenance requirements** as “hard constraints”:
   - If a claim can’t be sourced, it should be removed or explicitly marked as an assumption. 🧠

> [!IMPORTANT]
> If the model can output user-facing text (e.g., Focus Mode responses), ensure the model card references the **citation/provenance rules** and the **policy gates** that enforce them.

---

## 🧱 Canonical project references (assets)

> [!NOTE]
> Links below assume the recommended `assets/` folder exists. If you store sources elsewhere, update paths (but keep alias names stable).

| 🔖 Alias (recommended) | 📄 Source document (original) | 🎯 What to pull for the model card |
|---|---|---|
| [`assets/kfm_comprehensive_technical_documentation.pdf`](./assets/kfm_comprehensive_technical_documentation.pdf) | Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation | End-to-end system overview, repo layout, contracts/metadata mindset, licensing posture, “no mystery layers” principle |
| [`assets/kfm_architecture_features_design.pdf`](./assets/kfm_architecture_features_design.pdf) | Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design | v13 architecture, automated policy gates, W-P-E agents, release/CI governance hooks |
| [`assets/kfm_ai_system_overview.pdf`](./assets/kfm_ai_system_overview.pdf) | Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖 | Focus Mode behavior, retrieval/citation expectations, evaluation/monitoring concepts, AI governance framing |
| [`assets/kfm_ui_system_overview.pdf`](./assets/kfm_ui_system_overview.pdf) | Kansas Frontier Matrix – Comprehensive UI System Overview | Human factors + UI affordances that shape outputs (map/timeline/story nodes/focus mode UX) |
| [`assets/kfm_data_intake_guide.pdf`](./assets/kfm_data_intake_guide.pdf) | 📚 KFM Data Intake – Technical & Design Guide | Provenance/metadata pipeline, validation gates, checksums/telemetry, FAIR+CARE oversight workflow |
| [`assets/kfm_latest_ideas_future_proposals.pdf`](./assets/kfm_latest_ideas_future_proposals.pdf) | 🌟 KFM – Latest Ideas & Future Proposals | Roadmap items, near-term integrations, feature proposals (for “future work” + risk notes) |
| [`assets/kfm_innovative_concepts.pdf`](./assets/kfm_innovative_concepts.pdf) | Innovative Concepts to Evolve KFM | Longer-horizon concepts, ethical design ideas, AR/simulation/storytelling upgrades |
| [`assets/kfm_additional_project_ideas.pdf`](./assets/kfm_additional_project_ideas.pdf) | Additional Project Ideas | Ops/security/integrity concepts (artifact signing, policy packs, “drift” ideas, governance automation) |
| [`assets/kfm_open_source_mapping_hub_design.pdf`](./assets/kfm_open_source_mapping_hub_design.pdf) | Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design | Alternate/earlier system framing: ingestion → catalogs → AI reasoning → visualization; good for “system overview” cross-checks |
| [`assets/kfm_markdown_guide_v13.md`](./assets/kfm_markdown_guide_v13.md) | MARKDOWN_GUIDE_v13 (Master Guide) | Canonical doc map, pipeline ordering, STAC/DCAT/PROV alignment policy, governance expectations |
| [`assets/scientific_method_master_coder_protocol.pdf`](./assets/scientific_method_master_coder_protocol.pdf) | Scientific Method / Master Coder Protocol Documentation | Reproducibility + engineering discipline: environment capture, peer review, validation norms |

### 📚 Background “packs” (PDF portfolios / compiled reading)

| 🔖 Alias (recommended) | 📦 Pack | 💡 Notes |
|---|---|---|
| [`assets/packs_ai_concepts.pdf`](./assets/packs_ai_concepts.pdf) | AI Concepts & more | Often a **PDF portfolio**; open in Acrobat if the embedded docs don’t render in GitHub |
| [`assets/packs_geospatial_webgl.pdf`](./assets/packs_geospatial_webgl.pdf) | Maps / Google Maps / Virtual Worlds / Archaeological CG / Geospatial WebGL | Background for web mapping stacks + 3D/virtual world concepts |
| [`assets/packs_programming_resources.pdf`](./assets/packs_programming_resources.pdf) | Various programming languages & resources | General engineering reference pack |
| [`assets/packs_data_management_bayesian.pdf`](./assets/packs_data_management_bayesian.pdf) | Data management / architectures / data science / Bayesian methods | Background for data systems + statistical thinking |

---

## 🧩 Repo-native “pinned sources”

These are in-repo docs that frequently become **primary citations** for model card claims (use permalinks in the model card when possible).

> [!TIP]
> From this folder, repo root is typically `../../../../`

### 🧱 Architecture & blueprints
- `../../../../docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- `../../../../docs/architecture/system_overview.md`
- `../../../../docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md`
- `../../../../docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md`

### 🧪 Pipelines & ingestion
- `../../../../docs/guides/pipelines/ingestion-guide.md`
- `../../../../docs/guides/pipelines/kfm-ai-pipeline-cookiecutter.md`
- `../../../../docs/guides/pipelines/kfm_end_to_end_pipeline_v0.1.0.md`

### ⚖️ Governance & policy
- `../../../../api/scripts/policy/README.md` (OPA/Conftest gates, policy pack rules)
- `../../../../docs/guides/governance/faircare-oversight.md`
- `../../../../docs/governance/ROOT_GOVERNANCE.md`
- `../../../../docs/governance/ETHICS.md`
- `../../../../docs/governance/SOVEREIGNTY.md`

### 🧾 Templates (standardization = maintainability)
- `../../../../docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `../../../../docs/templates/TEMPLATE__STORY_NODE_V3.md`
- `../../../../docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

---

## 🧾 Model-card section → evidence map

Use this table as your “citation routing map” when filling out the `<model_id>` model card.

| 🧩 Model card section | ✅ What needs evidence | 🔗 Primary sources to cite |
|---|---|---|
| **Intended use & users** | Who it’s for, supported tasks, non-goals | `kfm_comprehensive_technical_documentation`, `kfm_open_source_mapping_hub_design` |
| **System context** | How the model sits inside KFM (services, UI, data layers) | `kfm_comprehensive_technical_documentation`, `kfm_architecture_features_design`, repo blueprints |
| **Data & provenance** | Data intake ordering, contracts, STAC/DCAT/PROV linkage, checksums/telemetry | `kfm_data_intake_guide`, `kfm_markdown_guide_v13`, policy docs |
| **Model behavior** | Focus Mode expectations, citation rules, refusal conditions | `kfm_ai_system_overview`, `kfm_architecture_features_design`, policy pack docs |
| **UX / human factors** | UI elements shaping outputs (map/timeline/story nodes) and user interpretation | `kfm_ui_system_overview` |
| **Safety & governance** | Policy gates, sensitivity handling, FAIR+CARE review triggers | `kfm_architecture_features_design`, `kfm_data_intake_guide`, governance docs |
| **Monitoring & integrity** | Drift ideas, graph health checks, artifact signing/verification | `kfm_additional_project_ideas`, `kfm_architecture_features_design` |
| **Evaluation** | What “good” means; metrics; tests; review norms | `kfm_ai_system_overview`, `scientific_method_master_coder_protocol`, policy docs |
| **Limitations** | Known gaps, scope boundaries, failure modes | `kfm_comprehensive_technical_documentation`, `kfm_ai_system_overview`, UI overview |
| **Roadmap / future work** | Planned features + guardrails | `kfm_latest_ideas_future_proposals`, `kfm_innovative_concepts`, `kfm_additional_project_ideas` |

---

## ➕ Adding new links

When you add a new source to this folder:

1. Drop the file into `assets/` using a **clean alias**: `lower_snake_case`, ASCII, stable.
2. Add a row in:
   - **Canonical project references (assets)**
   - and (optionally) the **Model-card section → evidence map**
3. For repo docs, prefer linking to a **pinned commit permalink** in the model card (not a moving `main` link).

> [!TIP]
> Recommended metadata to record alongside each new source (in a short bullet under the table row, if needed):
> - Version / date
> - Owner / maintainer
> - What sections it supports
> - Any deprecation notes (“superseded by v13 blueprint”)

---

## 🧰 Maintenance checklist

- [ ] Links resolve locally in GitHub (no broken relative paths) 🔗
- [ ] Each model-card claim has **≥1 source** from this README ✅
- [ ] Any “policy gate” behavior cited has a corresponding policy doc link ⚖️
- [ ] Roadmap items are clearly marked as **future** (not current behavior) 🧭
- [ ] Packs/portfolios are labeled if they require Acrobat to browse embedded docs 📚
- [ ] Deprecated docs are flagged (and replaced by newer sources) ♻️

---

## 🧷 Small but important conventions

- **Evidence-first**: Prefer sources that define the rule (policy doc) over sources that merely mention it.
- **Fail-closed mindset**: If the system can’t cite provenance, treat the behavior as “should refuse.”
- **Traceability > cleverness**: Model cards are an audit artifact. Keep the link trail clean. 🧾✨
