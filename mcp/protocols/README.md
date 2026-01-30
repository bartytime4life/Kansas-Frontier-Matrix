# 🧪 MCP Protocols (Playbooks & SOPs)

![MCP](https://img.shields.io/badge/MCP-Master%20Coder%20Protocol-blue)
![Reproducibility](https://img.shields.io/badge/Reproducibility-First-brightgreen)
![Docs](https://img.shields.io/badge/Docs-Living%20Runbooks-informational)
![KFM](https://img.shields.io/badge/KFM-Pipeline%20Aligned-6f42c1)

> [!TIP]
> **Protocols = the “how.”**  
> **Experiment reports = the “what happened.”**  
> If it’s repeatable, it belongs here. If it’s a result, it belongs in `mcp/experiments/`.

---

## 🎯 Purpose

This directory is the **canonical home for step-by-step protocols** (a.k.a. SOPs / runbooks) used across the Kansas Frontier Matrix system.

Protocols exist to:
- ✅ Make recurring work **repeatable** (anyone can follow the steps)
- ✅ Make outcomes **auditable** (what ran, with what inputs, producing what outputs)
- ✅ Keep KFM **pipeline-aligned** (no “shortcut” publishing)
- ✅ Reduce tribal knowledge and speed up onboarding 🧭

---

## 🧭 Golden Rules (Non-Negotiables)

> [!WARNING]
> If a workflow touches data, it must respect the **canonical pipeline sequence**:
> **Raw → Processed → Catalog/Prov → Database → API → UI**  
> No skipping steps. No “just load it into the UI.” No bypassing metadata/provenance.

- 📌 **Write the protocol before** you run the work (or update it immediately if you discover gaps).
- 🧾 **Every run must reference a protocol ID** and record the exact code/config used (commit hash, parameters).
- 🧪 **If the method changes, bump the protocol version** and note the delta.
- 🔁 **Deviations must be documented** in the run report (not silently “fixed”).
- 🧰 Protocols should be **tool-agnostic**, but provide **exact commands** and known-good defaults.

---

## 🗂️ What Lives Here?

| Type | What it is | Examples |
|---|---|---|
| 🧾 SOP (Standard Operating Procedure) | Step-by-step guide for recurring tasks | “Georeference map layer”, “Create COG tiles”, “Publish STAC/DCAT/PROV” |
| 🧪 Experiment Protocol | Pre-defined experimental method (not results) | “NER model training eval plan”, “OCR parameter sweep method” |
| ✅ QA / Verification Checklist | How we validate correctness and reproducibility | “Dataset acceptance checks”, “Catalog/provenance required fields” |
| 🧯 Troubleshooting Runbook | Known failures + fixes | “PostGIS import errors”, “Tile build issues”, “CI failures” |

---

## 📁 Recommended Layout

> [!NOTE]
> Your repo may evolve—this is the **recommended** organization for scale and discoverability.

```text
📁 mcp/
  ├─ 📁 protocols/
  │  ├─ 📄 README.md                    👈 you are here
  │  ├─ 📁 templates/                   # copy/paste starter docs
  │  │  ├─ 📄 SOP_TEMPLATE.md
  │  │  ├─ 📄 EXP_PROTOCOL_TEMPLATE.md
  │  │  └─ 📄 QA_CHECKLIST_TEMPLATE.md
  │  ├─ 📁 etl/                         # ingestion + transformation protocols
  │  ├─ 📁 geospatial/                  # georeferencing, tiling, projections
  │  ├─ 📁 ai/                          # training, evaluation, labeling protocols
  │  ├─ 📁 ops/                         # dev environment, deployments, backups
  │  └─ 📁 deprecated/                  # retired protocols (kept for traceability)
  ├─ 📁 experiments/                    # run logs / results (what happened)
  ├─ 📁 model_cards/                    # model documentation
  └─ 📁 notebooks/                      # exploratory work (when applicable)
```

---

## ⚡ Quick Start: Add a New Protocol

1) 🧩 Pick the protocol type:
- Recurring task → **SOP**
- Planned test / method → **Experiment Protocol**
- Validation gate → **QA Checklist**

2) 🏷️ Assign an ID + filename (see next section)

3) 🧾 Copy a template (recommended):
- `mcp/protocols/templates/SOP_TEMPLATE.md`
- `mcp/protocols/templates/EXP_PROTOCOL_TEMPLATE.md`
- `mcp/protocols/templates/QA_CHECKLIST_TEMPLATE.md`

4) 🔗 Link it:
- Reference related scripts in `src/` / `tools/`
- Reference datasets and expected catalog/prov outputs
- Add cross-links to `mcp/experiments/` once runs exist

---

## 🏷️ Naming, IDs, and Versioning

### ✅ ID Formats (choose one and be consistent)
- `SOP-001`, `SOP-002`, …
- `EXP-001`, `EXP-002`, …
- `QA-001`, `QA-002`, …

### ✅ Filename Convention
```text
<type>-<nnn>_<short-kebab-slug>.md
```

Examples:
- `SOP-003_georeference-historical-map.md`
- `SOP-008_generate-stac-dcat-prov.md`
- `EXP-004_ner-training-eval-plan.md`
- `QA-002_dataset-acceptance-checklist.md`

### 🔁 Versioning
- Use **SemVer** for protocol documents when the workflow is stable:
  - `v1.0.0` initial stable
  - `v1.1.0` backward-compatible improvements
  - `v2.0.0` breaking procedural change (different outputs, new required tools, etc.)

---

## 🧾 Protocol Metadata Header (Recommended)

Add this at the top of every protocol file:

```yaml
---
id: SOP-000
title: Short human-readable title
status: draft | active | deprecated
version: 0.1.0
owners:
  - "@your-handle"
last_reviewed: 2026-01-29
pipeline_stage: raw | processed | catalog | prov | database | api | ui
inputs:
  - data/raw/<domain>/<source>
outputs:
  - data/processed/<domain>/<artifact>
  - data/catalog/<...>
  - data/provenance/<...>
links:
  - ../experiments/EXPLOG-000_some-run.md
  - ../model_cards/<model>.md
---
```

> [!TIP]
> The `pipeline_stage` field is a forcing function: it makes “where this belongs” explicit.

---

## 🧱 SOP Template (Copy/Paste)

<details>
<summary><strong>📄 SOP Minimal Template</strong> (click to expand)</summary>

```markdown
---
id: SOP-000
title: SOP Title
status: draft
version: 0.1.0
owners: ["@owner"]
last_reviewed: YYYY-MM-DD
pipeline_stage: processed
inputs: []
outputs: []
---

# 🎯 Purpose
Why does this SOP exist? What problem does it solve?

# 🧰 Tools Needed
- OS / runtime requirements
- CLI tools
- Python/R env + versions
- External services (if any)

# 📦 Inputs
- List datasets, paths, IDs, expected format
- Reference catalogs (STAC/DCAT) when relevant

# 🧪 Procedure (Step-by-Step)
1. …
2. …
3. …

# ✅ Verification
How do we confirm it worked?
- checksums?
- schema validation?
- visual inspection?
- unit/integration tests?

# 🧯 Troubleshooting
| Symptom | Likely Cause | Fix |
|---|---|---|
| … | … | … |

# 🧾 Outputs
- Produced files + locations
- Required catalog/prov artifacts

# 📝 Change Log
- v0.1.0: initial draft
```

</details>

---

## 🧪 Experiment Protocol Template (Copy/Paste)

<details>
<summary><strong>🧪 Experiment Protocol Template</strong> (click to expand)</summary>

```markdown
---
id: EXP-000
title: Experiment Protocol Title
status: draft
version: 0.1.0
owners: ["@owner"]
last_reviewed: YYYY-MM-DD
---

# ❓ Objective
What question are we answering?

# 🧠 Hypothesis
What do we expect to happen, and why?

# 🔧 Variables
- Independent variables:
- Dependent variables:
- Controls:

# 🧰 Materials / Data
- Dataset(s) and versions
- Tools + environment (pin versions)
- Hardware assumptions (if relevant)

# 🧪 Procedure
1. Setup steps
2. Execution steps
3. Data collection steps

# 📈 Analysis Plan
- Metrics
- Statistical tests (if any)
- Visualizations to generate

# ✅ Expected Outcome
What would “success” look like?

# 🔁 Replication Notes
How should another person reproduce this exactly?
```

</details>

---

## ✅ “Definition of Done” Checklist

Use this before considering a protocol “active”:

- [ ] Steps are complete and unambiguous (a new contributor can follow them)
- [ ] Inputs/outputs are explicitly defined
- [ ] Pipeline stage is declared and respected (no step skipping)
- [ ] Required catalogs/provenance artifacts are listed (when data changes)
- [ ] Verification steps exist and are realistic
- [ ] Troubleshooting includes at least the top 2–3 common failures
- [ ] A real run has referenced this protocol (and surfaced any missing steps)

---

## 🔗 Related MCP Areas (Where To Put What)

- 🧪 **Results / runs / outputs:** `mcp/experiments/`
- 🧠 **Model documentation:** `mcp/model_cards/`
- 📓 **Exploration notebooks:** `mcp/notebooks/`
- 🧾 **Governed pipeline contracts / ordering:** `docs/` (Master Guide / Architecture docs)

---

## 🧼 Deprecation Policy

When retiring a protocol:
1) Mark `status: deprecated`
2) Add a banner at the top with the replacement link
3) Move to `mcp/protocols/deprecated/` (optional but recommended)
4) Do **not** delete (old experiments may still reference it)

---

## 🙋 FAQ

**Q: A protocol changed—do I update the old one?**  
A: If old runs depend on it, **keep it** and bump version / add changelog. If it’s a breaking change, create a new major version.

**Q: Where do I document “we tried X and it didn’t work”?**  
A: In the corresponding run report under `mcp/experiments/`, referencing the protocol ID.

**Q: Do protocols need citations?**  
A: If adapted from an external method, paper, or another workflow, yes—cite it in the protocol so others can trace lineage.

---

## 🧩 Next Protocols to Add (Starter Ideas)

- 🗺️ `SOP-___ georeference historical maps`
- 🧱 `SOP-___ convert raster to Cloud-Optimized GeoTIFF (COG)`
- 🧾 `SOP-___ generate STAC/DCAT/PROV for dataset`
- 🤖 `SOP-___ update / retrain NLP model (with evaluation gates)`
- ✅ `QA-___ dataset acceptance checklist (schemas + provenance required)`

