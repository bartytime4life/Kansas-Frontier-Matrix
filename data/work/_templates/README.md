---
title: "KFM Workbench Templates"
path: "data/work/_templates/README.md"
version: "v1.0.0"
last_updated: "2026-01-11"
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

doc_uuid: "urn:kfm:doc:data:work:templates:readme:v1.0.0"
semantic_document_id: "kfm-data-work-templates-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:templates:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

<div align="center">

# 🧩 Workbench Templates — `data/work/_templates/`

![Scope](https://img.shields.io/badge/scope-data%2Fwork%2F_templates-1f6feb?style=flat-square)
![Copy/Paste](https://img.shields.io/badge/templates-copy%2Fpaste%20scaffolds-2ea44f?style=flat-square)
![Repro](https://img.shields.io/badge/repro-flight%20recorder%20manifests-purple?style=flat-square)
![Governance](https://img.shields.io/badge/FAIR%2BCARE-governance%20aware-6f42c1?style=flat-square)
![Pipeline](https://img.shields.io/badge/pipeline-ETL%E2%86%92STAC%2FDCAT%2FPROV%E2%86%92Graph%E2%86%92API%E2%86%92UI-informational?style=flat-square)

Reusable **starter files** for KFM work packages: experiments 🧪, simulations 🛰️, viz prototypes 🗺️, and dataset staging 📦.  
**Copy these templates into your run folder**, fill the blanks, and keep the result auditable.

</div>

> [!IMPORTANT]
> These templates are for **workbench artifacts** (`data/work/**`).  
> **Governing documentation templates** live in `docs/templates/` (and are subject to Markdown protocol + governance validation).:contentReference[oaicite:1]{index=1}

---

## 🚀 Quick links

- 🧰 Workbench root → `data/work/README.md`
- 🧪 Experiments lab → `data/work/experiments/README.md`
- 🛰️ Simulations → `data/work/sims/README.md`
- 🗺️ Viz prototypes → `data/work/viz/README.md`
- 📦 WIP datasets → `data/work/datasets/README.md`
- 📚 Governing docs templates (canonical) → `docs/templates/`

---

<details>
<summary><strong>🧭 Table of contents</strong></summary>

- [🎯 What this folder is for](#-what-this-folder-is-for)
- [🧱 KFM pipeline context](#-kfm-pipeline-context)
- [🗂️ Recommended template layout](#️-recommended-template-layout)
- [🧩 Template inventory](#-template-inventory)
- [✅ How to use templates](#-how-to-use-templates)
- [📄 Copy/paste templates](#-copypaste-templates)
  - [1) Work Package README](#1-work-package-readme-template__work_package__readmemd)
  - [2) Work Package manifest](#2-work-package-manifest-template__work_package__manifestyaml)
  - [3) Run manifest](#3-run-manifest-template__run__manifestjson)
  - [4) PROV hint](#4-prov-hint-template__prov_hintmd)
  - [5) Repro checklist](#5-repro-checklist-template__checklist__reproducibilitymd)
  - [6) Geo QA checklist](#6-geo-qa-checklist-template__checklist__geo_qamd)
  - [7) Stats hygiene checklist](#7-stats-hygiene-checklist-template__checklist__stats_hygienemd)
  - [8) Simulation V&V + UQ checklist](#8-simulation-vv--uq-checklist-template__checklist__sim_vv_uqmd)
  - [9) Security + privacy checklist](#9-security--privacy-checklist-template__checklist__security_privacymd)
  - [10) Datasheet template](#10-datasheet-template__dataset__datasheetmd)
  - [11) Model card template](#11-model-card-template__model__cardmd)
- [🔐 Governance & “don’t be creepy” defaults](#-governance--dont-be-creepy-defaults)
- [🧠 Automation-ready fields](#-automation-ready-fields)
- [📚 Reference shelf](#-reference-shelf)
- [🕰️ Version history](#️-version-history)

</details>

---

## 🎯 What this folder is for

This folder exists so that every work package can start with **good defaults**:

- 🧾 **Protocol-first** experiments (question → hypothesis → method → results → decision):contentReference[oaicite:3]{index=3}
- 🧷 **Run manifests** as “flight recorders” (inputs/params/env/seeds/outputs/hashes)
- 📦 **Promotion-ready metadata hooks** for STAC/DCAT/PROV
- 🔐 **Governance-aware** patterns (classification, sovereignty, safe disclosure)

If you copy nothing else, copy:
1) `manifest.yaml` ✅  
2) `RUN__manifest.json` ✅  
3) `PROV_HINT.md` ✅  

…because reproducibility is the whole point.:contentReference[oaicite:4]{index=4}

---

## 🧱 KFM pipeline context

KFM is strict about ordering. **Do not skip stages**:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

`data/work/**` is where we prove something is:
- deterministic,
- reproducible,
- reviewable,
- promotable.

Only after promotion do we treat it as a “real” dataset that downstream systems can rely on.

> [!NOTE]
> Evidence artifacts (including AI-derived ones) are treated as first-class outputs: they live in `data/processed/**`, get cataloged (STAC/DCAT), get provenance (PROV), and are referenced by the graph + served through the API boundary.

---

## 🗂️ Recommended template layout

This is a **recommended** internal organization for this folder:

```text
📁 data/work/_templates/
├─ 📄 README.md                                  👈 you are here
├─ 📁 work_package/                              🧰 baseline “work package standard”
│  ├─ 📄 TEMPLATE__WORK_PACKAGE__README.md
│  ├─ 📄 TEMPLATE__WORK_PACKAGE__manifest.yaml
│  ├─ 📄 TEMPLATE__PROV_HINT.md
│  ├─ 📄 TEMPLATE__checksums.sha256
│  └─ 📄 TEMPLATE__gitignore.snippet
├─ 📁 qa/                                        ✅ checklists
│  ├─ 📄 TEMPLATE__CHECKLIST__REPRODUCIBILITY.md
│  ├─ 📄 TEMPLATE__CHECKLIST__GEO_QA.md
│  ├─ 📄 TEMPLATE__CHECKLIST__STATS_HYGIENE.md
│  ├─ 📄 TEMPLATE__CHECKLIST__SIM_VV_UQ.md
│  └─ 📄 TEMPLATE__CHECKLIST__SECURITY_PRIVACY.md
├─ 📁 ml/                                        🤖 ML-specific docs
│  ├─ 📄 TEMPLATE__DATASET__DATASHEET.md
│  └─ 📄 TEMPLATE__MODEL__CARD.md
└─ 📁 promotion/                                 📦 promotion “starter shapes”
   ├─ 📄 TEMPLATE__DCAT__dataset.jsonld
   ├─ 📄 TEMPLATE__STAC__collection.json
   ├─ 📄 TEMPLATE__STAC__item.json
   └─ 📄 TEMPLATE__PROMOTION__CHECKLIST.md
```

> [!TIP]
> Keep templates short + practical. Anything “governing” should live under `docs/standards/` and be validated by the Markdown protocol rules.

---

## 🧩 Template inventory

| Template | Copy into… | Use when… | Why it exists |
|---|---|---|---|
| `TEMPLATE__WORK_PACKAGE__README.md` | any work package folder | always | makes work auditable |
| `TEMPLATE__WORK_PACKAGE__manifest.yaml` | any work package folder | always | captures inputs/params/outputs |
| `TEMPLATE__RUN__manifest.json` | `runs/<run-id>/` | every run | flight recorder + hashes |
| `TEMPLATE__PROV_HINT.md` | any work package folder | always | makes PROV export easy later |
| `TEMPLATE__CHECKLIST__REPRODUCIBILITY.md` | any work package folder | always | “repro or it didn’t happen” |
| `TEMPLATE__CHECKLIST__GEO_QA.md` | geo runs | GIS/RS work | CRS/units/geometry sanity |
| `TEMPLATE__CHECKLIST__STATS_HYGIENE.md` | stats/ML runs | inference | reduce self-deception |
| `TEMPLATE__CHECKLIST__SIM_VV_UQ.md` | sim runs | simulation | validation + UQ discipline |
| `TEMPLATE__CHECKLIST__SECURITY_PRIVACY.md` | any work | always | avoid leaks + unsafe patterns |
| `TEMPLATE__DATASET__DATASHEET.md` | dataset staging | dataset candidate | dataset “datasheet” expectation:contentReference[oaicite:10]{index=10} |
| `TEMPLATE__MODEL__CARD.md` | model staging | deployable model | model “card” expectation:contentReference[oaicite:11]{index=11} |

---

## ✅ How to use templates

### 1) Create your work package folder 🧰
Follow the Work Package Standard naming style (date + domain + slug + version).

### 2) Copy the baseline templates 📄
Copy into your new folder:

- `README.md`
- `manifest.yaml`
- `PROV_HINT.md`
- QA checklist(s) for your domain

### 3) Run “protocol-first” 🧾
Write your question/hypothesis/method before execution. This is a core expectation of the project’s scientific method protocol.:contentReference[oaicite:12]{index=12}

### 4) Every run gets a run-manifest 🧷
Include inputs, parameters, environment snapshot, seeds, outputs, and hashes. (This supports traceability and audit.):contentReference[oaicite:13]{index=13}

### 5) If it becomes “real,” promote it 📦
When downstream systems rely on it, promote outputs to `data/processed/**` and produce STAC/DCAT/PROV. That is the KFM boundary contract.

---

## 📄 Copy/paste templates

> [!NOTE]
> These are **starter shapes**. Keep them small; add fields only if they are actually used.

---

### 1) Work Package README (`TEMPLATE__WORK_PACKAGE__README.md`)

<details>
<summary><strong>📄 Template content</strong></summary>

```markdown
---
title: "Work Package — <short name>"
path: "data/work/<your_subpath>/README.md"
version: "v0.1.0"
last_updated: "YYYY-MM-DD"
status: "wip"         # wip | review | archived | promoted
doc_kind: "WorkPackage"
license: "CC-BY-4.0"

fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public" # public | internal | confidential | restricted
classification: "open"
jurisdiction: "US-KS"

work_package_id: "<YYYY-MM-DD__domain__slug__vNN>"
owners: ["@handle"]
git_commit: "<commit sha>"
---

# 🧰 <work_package_id> — <short name>

## 🎯 TL;DR
- **Goal / decision:**  
- **Status:**  
- **Key outputs:**  
- **Promotion intent:** (yes/no + candidate dataset_id)

## 🧠 Question / Hypothesis
- **Question:**  
- **Hypothesis:**  
- **Primary metric / success criteria:**  

## 📥 Inputs
- List inputs with *pointers + hashes* (or retrieval receipt):
  - `data/raw/...` pointer
  - external URL + version
  - checksums (sha256)

## ⚙️ How to run
```bash
# "rerun me" command(s)
make run
# or:
python -m src.run --params params/params.yaml
```

## 🧪 QA / sanity checks
- [ ] Repro checklist
- [ ] Domain checklist (geo/stats/sim/security)
- [ ] Visual spot-check (if applicable)

## 📦 Outputs
- `outputs/` (what’s in it)
- `viz/` (what’s in it)
- `exports/` (promotion candidate bundle, optional)

## 🧬 Provenance hooks
- `PROV_HINT.md` completed?
- Run manifests recorded in `runs/`?

## 🔐 Governance notes
- Sensitive data concerns:
- Redaction/generalization applied (if needed):
- Sovereignty / consent constraints:

## 🔁 Next steps
- ...
```

</details>

---

### 2) Work Package manifest (`TEMPLATE__WORK_PACKAGE__manifest.yaml`)

<details>
<summary><strong>🧾 Template content</strong></summary>

```yaml
id: "<YYYY-MM-DD__domain__slug__vNN>"
kind: "work-package"
status: "wip"  # wip | review | archived | promoted
owners:
  - "@handle"

created_at: "YYYY-MM-DD"
updated_at: "YYYY-MM-DD"

goal:
  question: "What decision does this support?"
  hypothesis: "Testable expected outcome"
  success_criteria:
    primary_metric: "TBD"
    threshold: "TBD"
    baseline: "TBD"

inputs:
  - name: "source_1"
    type: "raster|vector|table|text|api"
    pointer: "data/raw/<domain>/... OR external URL"
    version: "TBD"
    hash_sha256: "TBD"
    license: "TBD"
    notes: "Pin immutability (hash, tag, DOI, receipt)."

process:
  steps:
    - name: "validate_inputs"
      checks: ["schema", "ranges", "missingness", "crs/units"]
    - name: "transform"
      notes: "Scripted steps only (no click-ops without logging)."
    - name: "analyze"
      notes: "Stats/ML/sim method; record assumptions."
    - name: "export"
      notes: "Write artifacts with atomic writes, then hash."

parameters:
  region: "TBD"
  date_range: ["YYYY-MM-DD", "YYYY-MM-DD"]
  random_seed: 1337

outputs:
  - name: "metrics"
    path: "outputs/metrics.json"
    hash_sha256: "TBD"
  - name: "report"
    path: "outputs/report.md"
    hash_sha256: "TBD"
  - name: "artifacts"
    path: "viz/"
    hash_sha256: "TBD"

environment:
  runtime: "python|node|r|java|docker"
  lockfiles:
    - "environment/requirements.txt"
    - "environment/poetry.lock"
  container:
    image: "TBD"
    digest: "TBD"
  hardware:
    cpu: "TBD"
    gpu: "TBD"

governance:
  fair_category: "FAIR+CARE"
  care_label: "TBD"
  sensitivity: "public"    # public | internal | confidential | restricted
  classification: "open"
  jurisdiction: "US-KS"
  sovereignty_notes: "TBD"
  pii_present: false

automation:
  idempotency_key: "<stable key for reruns>"
  run_registry_path: "runs/registry.csv"

promotion_intent:
  candidate_dataset_id: "kfm.ks.<domain>.<product>.<time_range>.v1"
  promote_to: "data/processed/<domain>/..."
  requires_boundary_artifacts: true  # STAC + DCAT + PROV
  notes: "Promote only after QA + steward review."
```

</details>

> [!TIP]
> Include a stable identifier + run traceability (IDs, hashes, commit) so results remain auditable over time.:contentReference[oaicite:15]{index=15}:contentReference[oaicite:16]{index=16}

---

### 3) Run manifest (`TEMPLATE__RUN__manifest.json`)

<details>
<summary><strong>🧷 Template content</strong></summary>

```json
{
  "work_package_id": "YYYY-MM-DD__domain__slug__vNN",
  "run_id": "run-YYYYMMDD-HHMMSSZ",
  "timestamp_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "git_commit": "TBD",

  "inputs": [
    { "name": "source_1", "path_or_url": "TBD", "version": "TBD", "sha256": "TBD" }
  ],

  "params": {
    "region": "TBD",
    "date_range": ["YYYY-MM-DD", "YYYY-MM-DD"],
    "random_seed": 1337
  },

  "environment": {
    "os": "TBD",
    "runtime": "python",
    "runtime_version": "TBD",
    "lockfiles": ["environment/requirements.txt"],
    "container_image": "TBD",
    "container_digest": "TBD",
    "cpu": "TBD",
    "gpu": "TBD"
  },

  "outputs": [
    { "path": "outputs/metrics.json", "sha256": "TBD" },
    { "path": "outputs/report.md", "sha256": "TBD" },
    { "path": "viz/", "sha256": "TBD" }
  ],

  "notes": "What changed / why this run exists"
}
```

</details>

---

### 4) PROV hint (`TEMPLATE__PROV_HINT.md`)

<details>
<summary><strong>🧬 Template content</strong></summary>

```markdown
# 🧬 PROV_HINT — <work_package_id>

This file is a lightweight bridge: **workbench run → PROV bundle**.

## ✅ Entities (inputs + outputs)
- Input entities:
  - `entity:input:<name>` → pointer + hash + license
- Output entities:
  - `entity:output:<name>` → path + hash

## ✅ Activities (what happened)
- `activity:<run_id>`:
  - start/end timestamps (UTC)
  - software version (git commit)
  - parameters snapshot
  - toolchain versions

## ✅ Agents (who/what ran it)
- `agent:person:<handle>`
- `agent:software:<tool>`
- `agent:org:<publisher>`

## 🔗 Intended joins
- candidate `dataset_id`: `kfm.ks.<domain>.<product>.<time>.v1`
- planned STAC collection/item refs (if geo)
- planned DCAT dataset record path (if promoting)
- story/evidence refs (if used downstream)

## 🔐 Sensitivity & safe disclosure
- sensitivity: public|internal|confidential|restricted
- redactions/generalization applied:
- sovereignty/consent notes:

## 🧾 Notes
- ...
```

</details>

---

### 5) Repro checklist (`TEMPLATE__CHECKLIST__REPRODUCIBILITY.md`)

<details>
<summary><strong>✅ Template content</strong></summary>

```markdown
# ✅ Reproducibility Checklist — <work_package_id>

## Inputs
- [ ] Inputs are immutable or pinned (hash/tag/DOI/receipt)
- [ ] Licenses captured for all non-trivial inputs

## Parameters
- [ ] Parameters recorded (region/time window/thresholds/etc.)
- [ ] Seeds recorded + set where applicable

## Environment
- [ ] Lockfile committed (pip/conda/npm/etc.)
- [ ] Runtime versions recorded
- [ ] Hardware notes recorded if performance affects results

## Outputs
- [ ] Outputs have checksums (sha256)
- [ ] Units + CRS documented (if applicable)
- [ ] Atomic write pattern used (temp → rename)

## Audit trail
- [ ] Git commit hash recorded
- [ ] Run manifest exists under `runs/<run_id>/manifest.json`
- [ ] PROV_HINT completed (even partial)
```

</details>

> Reproducibility expectations include documenting protocols, parameters, environment configuration, and traceable outputs.:contentReference[oaicite:17]{index=17}:contentReference[oaicite:18]{index=18}

---

### 6) Geo QA checklist (`TEMPLATE__CHECKLIST__GEO_QA.md`)

<details>
<summary><strong>🗺️ Template content</strong></summary>

```markdown
# 🗺️ Geo QA Checklist — <work_package_id>

## CRS & alignment
- [ ] CRS explicitly stated (EPSG code)
- [ ] Reprojection steps scripted (no silent GIS click-ops)
- [ ] Overlay sanity check performed (spot-check control points)

## Geometry (vectors)
- [ ] Valid geometry (no self-intersections / empty geoms)
- [ ] Topology constraints noted (if relevant)

## Rasters
- [ ] Nodata value defined & preserved
- [ ] Resolution and resampling method recorded
- [ ] Overviews/pyramids built for interactive use (if needed)

## Metadata & exports
- [ ] Bounding box + temporal window recorded
- [ ] Artifacts are in standard formats (COG/GeoJSON/etc.)
- [ ] Checksums produced for publish candidates
```

</details>

---

### 7) Stats hygiene checklist (`TEMPLATE__CHECKLIST__STATS_HYGIENE.md`)

<details>
<summary><strong>📈 Template content</strong></summary>

```markdown
# 📈 Stats Hygiene Checklist — <work_package_id>

## Study intent
- [ ] Labeled as exploration vs confirmation
- [ ] Primary metric defined before running

## Data leakage & splits
- [ ] Train/val/test split documented (or CV plan)
- [ ] Leakage checks done (time leakage / feature leakage)

## Assumptions & diagnostics
- [ ] Residual diagnostics recorded (if regression)
- [ ] Confounders addressed (if observational)

## Uncertainty & reporting
- [ ] Effect sizes + uncertainty reported
- [ ] Multiple comparisons risk acknowledged (if many tests)
- [ ] Negative results captured (don’t “delete failures”)
```

</details>

---

### 8) Simulation V&V + UQ checklist (`TEMPLATE__CHECKLIST__SIM_VV_UQ.md`)

<details>
<summary><strong>🛰️ Template content</strong></summary>

```markdown
# 🛰️ Simulation V&V + UQ Checklist — <work_package_id>

## Setup & assumptions
- [ ] Simulation code/software identified + versioned
- [ ] Input parameters recorded + bounded
- [ ] Simplifying assumptions written down

## Verification & Validation
- [ ] Verification: numerical sanity checks (convergence / conservation / invariants)
- [ ] Validation: compared to baseline / empirical reference where possible

## Units & frames
- [ ] Units included everywhere
- [ ] Coordinate frames documented
- [ ] No silent unit mixing (SI preferred unless stated)

## Uncertainty
- [ ] Sensitivity sweep performed (even small)
- [ ] Uncertainty notes included (input → output)

## Artifacts
- [ ] Raw run logs kept
- [ ] Outputs have checksums + metadata
```

</details>

> Simulation documentation expectations include recording simulation setup, parameters, assumptions, how to run, and unit consistency throughout.:contentReference[oaicite:19]{index=19}

---

### 9) Security + privacy checklist (`TEMPLATE__CHECKLIST__SECURITY_PRIVACY.md`)

<details>
<summary><strong>🔐 Template content</strong></summary>

```markdown
# 🔐 Security + Privacy Checklist — <work_package_id>

## Secrets & credentials
- [ ] No secrets committed (keys, tokens, passwords)
- [ ] `.env` never committed; use `.env.example` if needed

## Sensitive locations & inference
- [ ] No precise sensitive coordinates embedded in “public” outputs
- [ ] If restricted: only coarse spatial coverage + gated access pointer

## Provenance & access
- [ ] Licenses captured
- [ ] Access constraints declared (public/internal/confidential/restricted)

## UI/API boundary safety
- [ ] UI does not hardcode storage paths that bypass governance
- [ ] Anything user-facing must flow through governed API
```

</details>

---

### 10) Datasheet (`TEMPLATE__DATASET__DATASHEET.md`)

<details>
<summary><strong>📦 Template content</strong></summary>

```markdown
---
doc_kind: "dataset-datasheet"
dataset_id: "kfm.ks.<domain>.<product>.<time_range>.v1"
status: "draft"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
sensitivity: "public"
care_label: "TBD"
license: "TBD"
---

# 📦 Dataset Datasheet — <dataset_id>

## What is this?
- Description:
- Intended uses:
- Not intended for:

## How was it created?
- Sources:
- Processing steps (high-level):
- Known limitations / biases:

## Schema / fields
- Link to `data_dictionary.md` or table

## Coverage
- Spatial:
- Temporal:

## Access & governance
- Classification:
- Access method (API / download / landing page):
- Sovereignty / consent constraints:

## Provenance hooks
- STAC refs:
- DCAT refs:
- PROV refs:
```

</details>

> The project protocol explicitly calls for dataset documentation (“datasheets”) including sources, preprocessing, and limitations/biases.:contentReference[oaicite:20]{index=20}

---

### 11) Model card (`TEMPLATE__MODEL__CARD.md`)

<details>
<summary><strong>🤖 Template content</strong></summary>

```markdown
---
doc_kind: "model-card"
model_id: "kfm.model.<name>.v1"
status: "draft"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
sensitivity: "public"
care_label: "TBD"
license: "TBD"
---

# 🤖 Model Card — <model_id>

## Summary
- Purpose:
- Model type:
- Intended users:

## Training data
- Dataset IDs + versions/hashes:
- Split strategy:
- Leakage checks:

## Evaluation
- Metrics (overall):
- Metrics (by subgroup) if relevant:
- Failure modes:

## Ethics & risk
- Potential harms:
- Bias considerations:
- Mitigations:

## Reproducibility
- Code commit:
- Environment:
- Training command:
```

</details>

> The protocol recommends model cards for important trained models, including intended use, evaluation results, and ethical considerations.:contentReference[oaicite:21]{index=21}

---

## 🔐 Governance & “don’t be creepy” defaults

- Treat `data/work/**` as **pre-public** by default.
- Anything sensitive must be labeled **and** have distributions/access patterns that don’t leak restricted details.
- Avoid “precision leaks” (exact coords, detailed site locations, etc.) in public artifacts.

The project explicitly calls out the need for strong governance, sovereignty, and safety around sensitive content and location inference. (When in doubt: generalize + gate access.):contentReference[oaicite:22]{index=22}

---

## 🧠 Automation-ready fields

KFM is moving toward automation patterns that can:
- detect changes,
- validate outputs,
- promote artifacts safely.

Templates therefore include fields like:
- `idempotency_key`
- `git_commit`
- checksums/hashes
- stable IDs for downstream joins

This aligns with “detect → validate → promote” automation concepts and idempotent run patterns described in the project proposals.:contentReference[oaicite:23]{index=23}:contentReference[oaicite:24]{index=24}

> [!TIP]
> If you adopt a “policy pack” / OPA-style validation later, keep the policy inputs (classification, access URLs, licenses, provenance refs) easy to extract from manifests. That’s the whole reason these templates are structured.:contentReference[oaicite:25]{index=25}

---

## 📚 Reference shelf

### 📘 Core KFM structure + invariants (normative)
- `MARKDOWN_GUIDE_v13.md.gdoc` (pipeline ordering, stage boundaries, invariants)
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx`:contentReference[oaicite:27]{index=27}

### 🧪 Scientific method + experiment rigor (highly influential)
- `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf` (protocol-first, experiment tracking, environment capture, model cards, datasheets):contentReference[oaicite:28]{index=28}:contentReference[oaicite:29]{index=29}

### 🗺️ System design context (influential)
- `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf` (layered architecture, reproducibility emphasis, optional DVC patterns):contentReference[oaicite:30]{index=30}:contentReference[oaicite:31]{index=31}

---

## 🕰️ Version history

| Version | Date | Summary |
|---|---|---|
| v1.0.0 | 2026-01-11 | Initial template index + copy/paste scaffolds for work packages, QA checklists, run manifests, PROV hints, datasheets, and model cards. |

---

<p align="right"><a href="#-workbench-templates--datawork_templates">⬆️ Back to top</a></p>

