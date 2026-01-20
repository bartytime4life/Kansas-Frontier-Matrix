# 🧪 MCP Run — `RUN_ID`

![KFM](https://img.shields.io/badge/KFM-provenance--first-2ea44f)
![MCP](https://img.shields.io/badge/MCP-run-blue)
![metadata](https://img.shields.io/badge/metadata-STAC%2FDCAT%2FPROV-important)
![AI](https://img.shields.io/badge/AI-Focus%20Mode%20(citations)-8a2be2)

> [!TIP]
> Treat this folder as a **run capsule**: *humans* get a narrative summary, and *machines* get verifiable artifacts (manifests, catalogs, provenance, policy results).

---

## 📌 What is this?

This directory (`mcp/runs/RUN_ID/`) is the canonical **MCP run output** bundle (human + machine readable). The repo design explicitly calls out `mcp/` as tooling/automation and `mcp/runs/` as generated run outputs + experiment reports. 

KFM’s architecture emphasizes:
- **Provenance-first data publishing** (STAC + DCAT + PROV) with hard enforcement (“Publish Rule 3”).
- **Watcher → Planner → Executor (W‑P‑E)** automation for intake and processing (auditable, deterministic).
- **Policy gates** (schema checks, licensing, sensitivity, provenance completeness, etc.) enforced via CI and a Policy Pack (OPA/Conftest). [oai_citation:0‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- **AI Focus Mode** that must be evidence-based and cite sources; outputs should “fail closed” if citations can’t be produced.

---

## 🔗 Quick Links

> Update these paths to match what your runner actually emits 👇

- 🧾 **Run manifest**: `./run_manifest.json` *(or canonical at `data/audits/<run_id>/run_manifest.json`)*
- 🧾 **Evidence manifest**: `./evidence_manifest.json` (citations + “why you should trust this”)
- 🧬 **Provenance bundle**: `./provenance/` (W3C PROV JSON‑LD)
- 🗺️ **STAC catalog**: `./stac/` (catalog + items/assets)
- 🗃️ **DCAT dataset**: `./dcat/`
- 🧠 **AI index diff**: `./indexes/` (vector/graph deltas)
- ✅ **Policy results**: `./policy/` (OPA/Conftest outputs) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- 📈 **Metrics**: `./metrics/`
- 🧾 **Logs**: `./logs/` (NDJSON recommended; include Focus telemetry)
- 🖼️ **UI snapshots**: `./ui/` (screenshots / story playback)

---

## 🏷️ Run Metadata

| Field | Value |
|---|---|
| `run_id` | `RUN_ID` |
| Run type | `ingest \| transform \| graph_sync \| tile_build \| ai_index \| publish \| backfill \| qa` |
| Trigger | `manual \| schedule \| PR \| watcher` |
| Started (UTC) | `YYYY-MM-DDTHH:MM:SSZ` |
| Ended (UTC) | `YYYY-MM-DDTHH:MM:SSZ` |
| Repo commit | `GIT_SHA` |
| Build/runner | `CI_JOB_URL` / `runner@version` |
| Container image(s) | `image@sha256:...` |
| Operator(s) | `@handle` (role: `curator|maintainer|admin`) |
| Policy pack version | `policy_pack@sha256:...` |
| Data sensitivity | `public \| internal \| restricted` |
| License posture | `OK \| review \| blocked` |
| Publish target | `dev \| staging \| prod \| none` |

> [!NOTE]
> “Roles / auth / least-privilege” are explicitly called out as part of the future proposal set (curator vs maintainer vs admin). Record the actor + role for every run. [oai_citation:2‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## ✅ Run Status Checklist

- [ ] Policy gates **PASSED** (schema, license, sensitivity classification, provenance completeness)
- [ ] **Publish Rule 3** satisfied (STAC + DCAT + PROV present)
- [ ] Focus Mode outputs include **citations** (or feature disabled for this run)
- [ ] Artifacts packaged (optional) and signed (OCI + ORAS/Cosign)
- [ ] Published to target catalog(s) + indexes updated
- [ ] Rollback plan documented (and tested if high-risk) [oai_citation:3‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## 🎯 Objective / Hypothesis (Scientific Method Alignment)

> [!IMPORTANT]
> MCP runs should be written like experiments: objective → method → results → interpretation → next steps (repeatable + auditable).

**Objective (1–2 sentences):**  
`TODO: What are we trying to achieve?`

**Hypothesis / Expected outcome:**  
`TODO: What should change if this run succeeds?`

**Success criteria:**  
- `TODO: Metric or invariant #1`
- `TODO: Metric or invariant #2`

---

## 🧭 KFM Context for This Run

KFM is built to unify **maps (2D + 3D), time navigation, story narratives, and AI assistance** into one experience where every visualization is traceable to its sources (“the map behind the map”). [oai_citation:4‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

From the UI and architecture perspectives:
- UI is **React-based** and **decoupled** from backend via REST/GraphQL (so UI can evolve independently). [oai_citation:5‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- Story Nodes are intentionally designed so domain experts can contribute narrative content by editing simple files **“without writing code”** (subject to review). [oai_citation:6‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

---

## 📁 Folder Layout (Run Capsule Contract)

```text
mcp/runs/RUN_ID/
├─ README.md                        🧾 (this file)
│
├─ run_manifest.json                🧪 structured run record (inputs/outputs/metrics)
├─ evidence_manifest.json           🔎 citations + trust chain
├─ plan.json                        🧭 planner output (W‑P‑E)
│
├─ provenance/                      🧬 W3C PROV JSON‑LD (+ any bundles)
│  ├─ prov.jsonld
│  └─ prov.summary.md
│
├─ stac/                            🗺️ STAC catalog/items/assets
├─ dcat/                            🗃️ DCAT dataset metadata
│
├─ outputs/                         📦 produced data assets (COG/GeoParquet/tiles/etc)
├─ indexes/                         🧠 graph + vector index changes (if any)
│
├─ policy/                          ✅ OPA/Conftest results + gate reports
├─ metrics/                         📈 metrics snapshots + QA reports
├─ logs/                            🧾 NDJSON logs (executor + focus telemetry)
└─ ui/                              🖼️ screenshots / story playback recordings
```

> [!IMPORTANT]
> KFM run tracking calls out **structured run identifiers** and recommends a `run_manifest.json` plus telemetry (including Focus telemetry in NDJSON) for auditability.

---

## 🧾 Inputs

> Include **source URIs**, checksums, licensing, sensitivity notes, and provenance references.

| Input | Version / Time Range | Source URI | License | Sensitivity | Integrity |
|---|---:|---|---|---|---|
| `TODO` | `TODO` | `TODO` | `TODO` | `TODO` | `sha256:...` |

**Notes**
- If any input is missing required metadata, the run should **fail the policy gate** (and publishing is blocked).

---

## 🔧 W‑P‑E Execution Summary

### 👀 Watcher Signals
`TODO: What sources or triggers fired?`

### 🧭 Planner Output
- `plan.json`: `TODO: link/summary`
- Plan intent: `TODO`

### ⚙️ Executor Steps
1. `TODO`
2. `TODO`

> [!NOTE]
> W‑P‑E is explicitly described as: Watchers monitor sources, Planner produces a structured plan, Executor runs deterministic pipelines while capturing logs and audit records.

---

## 📦 Outputs

### ✅ Primary Artifacts
| Artifact | Path | Description |
|---|---|---|
| Run Manifest | `run_manifest.json` | structured record: inputs, params, outputs, timestamps, metrics |
| Evidence Manifest | `evidence_manifest.json` | citations + evidence chain for claims/derived products |
| PROV | `provenance/prov.jsonld` | lineage + derivations across pipeline stages |
| STAC | `stac/` | catalog + item assets for datasets |
| DCAT | `dcat/` | dataset-level metadata |
| Focus telemetry | `logs/focus_telemetry.ndjson` | Q/A + citation traces (if AI used) |

### 📤 Publish Targets
`TODO: Where did this run publish (dev/staging/prod)?`

---

## 🧬 Provenance, Catalogs, and the “No-Surprises” Rule

> [!IMPORTANT]
> **Publish Rule 3**: no publishing unless the **evidence triplet** exists: **STAC + DCAT + PROV**. If incomplete → block the publish step.

### Required references
- Every output dataset should carry a `provenance_ref` (or equivalent) that points to the PROV record(s).

---

## 🧠 AI / Focus Mode Impact (If Applicable)

KFM’s AI layer is designed to be **hybrid retrieval** (knowledge graph + vector embeddings) so answers can be grounded in both structured relations and semantic context.

> [!IMPORTANT]
> Focus Mode should **always cite sources**; if an answer can’t be derived from indexed evidence, it should refuse / return “insufficient data” rather than inventing output.

### AI changes captured in this run
- [ ] vector index rebuilt
- [ ] entity linking suggestions produced
- [ ] metadata drafts generated (“AI data steward”)
- [ ] story-node drafting suggestions (future)

> [!NOTE]
> The AI “data steward” concept: AI can draft metadata and suggest entity links, but the human uploader/curator reviews and signs off (human-in-the-loop). [oai_citation:7‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 🗺️ UI / Story / Timeline Touchpoints

### Story Nodes changed?
- `TODO: list story_node IDs / paths`
- Evidence links present in narrative text/media?

> [!NOTE]
> Story content is designed so historians/educators can contribute by editing files “without writing code” (reviewed/moderated). [oai_citation:8‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

### UI validation artifacts
- Screenshots: `ui/screenshots/...`
- Story playback capture: `ui/story_playback.mp4` (optional)
- Any map-layer attribution checks?

---

## 🧵 Pulse Threads & Conceptual Attention Nodes (Optional Extensions)

If this run produces narrative or anomaly signals, capture them:

- **Pulse Thread**: a stream of observations for one theme/event/entity across time.  
- **Conceptual Attention Node**: a metadata-rich “why this matters” marker that highlights patterns/anomalies.  
- **Evidence Manifest**: web-renderable citations to support every claim.  
- **Run Manifest**: structured run record (inputs/outputs/metrics).

**Suggested files**
- `pulse_threads/<thread_id>.json`
- `conceptual_attention/<node_id>.json`

---

## 🛡️ Policy Gates, Privacy, and Governance

### ✅ Policy Pack gates (record pass/fail + links)
- [ ] Schema validation (STAC/DCAT/PROV completeness)
- [ ] License present + compatible
- [ ] Sensitivity classification present
- [ ] Provenance completeness / lineage capture
- [ ] OPA/Conftest checks passed (CI policy pack) [oai_citation:9‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

### 🔐 Privacy-preserving options (use if restricted/sensitive)
Privacy-preserving data mining methods include techniques like encryption/anonymization and differential privacy to protect data while enabling analysis.

> [!TIP]
> If a dataset is sensitive, record which transformation(s) were applied (masking, aggregation, jitter, generalization, access controls) and the justification.

---

## 📦 Packaging, Signing, and Supply Chain (Optional but Recommended)

KFM proposals include storing data and policy artifacts in an **OCI registry** (e.g., `oci://...`) and attaching provenance + metadata, signed with **Cosign**, pushed via **ORAS**.

**If used, record:**
- OCI ref(s): `oci://registry/org/kfm-data:RUN_ID`
- Signature ref(s): `cosign://...`
- Digest(s): `sha256:...`

---

## ♻️ Reproducibility & Re-Run Notes

**Minimum reproducibility kit**
- runner version / container digests
- exact inputs (URIs + checksums)
- plan.json
- run_manifest.json + provenance

> [!NOTE]
> KFM intake tooling aims to provide “golden paths” and consistent templates so new contributors can mimic existing pipelines and remain compliant. [oai_citation:10‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## ⏪ Rollback & Provenance Repair (If Needed)

If a publish step is reverted, record:
- rollback trigger
- what was reverted (catalog entries / graph nodes / tiles / indices)
- what provenance “repair” actions were taken

> [!IMPORTANT]
> Future proposals explicitly call for rollback runbooks and “provenance repair” steps that can revert changes while keeping the audit trail coherent. [oai_citation:11‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## 🔁 PR → PROV Linkage (If Run Triggered by a PR)

If applicable, capture:
- PR URL / ID
- commit range
- which datasets and catalogs changed
- provenance linkage (PR as a PROV activity)

> [!NOTE]
> Proposal: treat PR events as provenance activities linked into the PROV graph so code+data evolution is queryable like the datasets themselves. [oai_citation:12‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## 🧭 Future Hooks (Optional, but align with roadmap)

KFM’s roadmap explores:
- **4D digital twin / time-travel simulation** concepts (time as a core dimension). [oai_citation:13‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- **AR + hybrid 2D/3D storytelling** (Voyager-style guided tours). [oai_citation:14‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- **Dashboards + live data + simulations** in the UI (e.g., “replay last 24 hours” sensor data). [oai_citation:15‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

If this run creates assets relevant to those, label them explicitly in `outputs/` and cross-link them from `evidence_manifest.json`.

---

## 📚 Project Docs Used for This Template

### Core KFM docs (high signal)
- Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf  [oai_citation:16‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- Kansas Frontier Matrix – Comprehensive UI System Overview.pdf  [oai_citation:17‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf  [oai_citation:18‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- 📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf  [oai_citation:19‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf (Policy Pack / OPA / CI gates)

### “Run + documentation system” sources
- Open-Source Geospatial Historical Mapping Hub Design (MCP structure + templates).
- Scientific Method / Master Coder Protocol (repeatable run reporting).

### Resource Packs (PDF Portfolios)
These uploaded files are **PDF portfolios containing many embedded references** (books/cookbooks).

<details>
<summary>📦 AI Concepts &amp; more — embedded library list (extracted from the portfolio)</summary>

- A Developer’s Guide to Building AI Applications - English.pdf  
- A Gentle Introduction to Symbolic Computation.pdf  
- AI Foundations of Computational Agents 3rd Ed.pdf  
- Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf  
- Artificial Neural Networks Models & Applications.pdf  
- Artificial-neural-networks-an-introduction.pdf  
- Basics of Linear Algebra for machine Learning (Discover The Mathematical LLanguage of Data in Python) - Jason Brownlee.pdf  
- Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf  
- Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf.pdf  
- Deep Learning with Python.pdf  
- Foundations of Machine Learning - Foundations_of_Machine_Learning.pdf  
- Gradient Expectations - Stucture, Origins, & Synthesis Of Predictive Neural Networks.pdf  
- Introduction to Digital Humanism.pdf  
- Introduction to Machine Learning with Python - Introduction to Machine Learning with Python.pdf  
- Neural Network Architectures and Activation Functions_ A Gaussian Process Approach - 106621.pdf  
- Neural Network Toolbox User_s Guide - nnet.pdf  
- Neural Networks Using C# Succinctly - Neural_Networks_Using_C_Sharp_Succinctly.pdf  
- On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf  
- Pattern Recognition and Machine Learning.pdf  
- Principles of Biological Autonomy - book_9780262381833.pdf  
- Recurrent Neural Networks for Temporal Data Processing.pdf  
- Regression analysis using Python - slides-linear-regression.pdf  
- Volume 1–3 Machine Learning under Resource Constraints.pdf  
- artificial-intelligence-a-modern-approach.pdf  
- haykin.neural-networks.3ed.2009.pdf  
- neural-network-design.pdf  
- understanding-machine-learning-theory-algorithms.pdf  
</details>

<details>
<summary>📦 Data Management / Data Science / Bayesian — embedded library list</summary>

- An Introduction to Statistical Learning.pdf  
- Bayesian Methods for Hackers Probabilistic Programming and Bayesian Inference.pdf  
- Comprehensive CI_CD Guide for Software and Data Projects.pdf  
- Data Mining Concepts & applictions.pdf  
- The Data Engineering Cookbook.pdf  
- The Data Lakehouse Platform For Dummies.pdf  
- The Elements of Statistical Learning.pdf  
- Theory & Practice of Cryptography & Network Security Protocols & Technologies.pdf  
- clean-architectures-in-python.pdf  
- think-bayes-bayesian-statistics-in-python.pdf  
</details>

<details>
<summary>📦 Various programming languages &amp; resources — embedded highlights</summary>

- Python Notes for Professionals.pdf  
- JavaScript Notes for Professionals.pdf  
- TypeScript Notes for Professionals.pdf  
- React JS Notes for Professionals.pdf  
- PostgreSQL Notes for Professionals.pdf  
- Introduction-to-Docker.pdf  
- The-Data-Engineers-Guide-to-Apache-Spark.pdf  
- An Introduction to Spatial Data Analysis and Visualisation in R.pdf  
- Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf  
- software-architecture-patterns.pdf  
</details>

<details>
<summary>📦 Maps / Virtual Worlds / WebGL — embedded highlights</summary>

- webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf  
- google-maps-javascript-api-cookbook.pdf  
- DesigningVirtualWorlds.pdf  
- Archaeological 3D GIS.pdf  
- making-maps-a-visual-guide-to-map-design-for-gis.pdf  
- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf  
</details>

---

## 📎 Appendix: JSON Skeletons (Drop-in Templates)

### `run_manifest.json` (skeleton)
```json
{
  "run_id": "RUN_ID",
  "type": "ingest|transform|publish|qa",
  "trigger": "manual|schedule|PR|watcher",
  "started_at": "YYYY-MM-DDTHH:MM:SSZ",
  "ended_at": "YYYY-MM-DDTHH:MM:SSZ",
  "inputs": [
    { "name": "source_name", "uri": "…", "sha256": "…", "license": "…", "sensitivity": "…" }
  ],
  "outputs": [
    { "name": "dataset_id", "path": "outputs/…", "sha256": "…", "provenance_ref": "provenance/prov.jsonld" }
  ],
  "policy": { "pack_version": "…", "passed": true, "report_path": "policy/report.json" },
  "metrics": { "path": "metrics/metrics.json" }
}
```

### `evidence_manifest.json` (skeleton)
```json
{
  "run_id": "RUN_ID",
  "claims": [
    {
      "claim": "Example: County boundary layer updated for 1890–1900",
      "evidence": [
        { "type": "source", "ref": "stac/item.json#asset:...", "citation": "…" },
        { "type": "provenance", "ref": "provenance/prov.jsonld#activity:..." }
      ]
    }
  ]
}
```

---

<details>
<summary>🧾 Source excerpts used to craft this run template (for traceability)</summary>

- Publish Rule 3 + evidence triplet STAC/DCAT/PROV
- Run IDs + `run_manifest.json` and Focus telemetry NDJSON
- W‑P‑E automation model
- Policy gates + OPA/Conftest policy pack [oai_citation:20‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- Focus Mode citation requirements
- UI decoupling + provenance surfacing (“map behind map”) [oai_citation:21‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) [oai_citation:22‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- Story contribution “without writing code” [oai_citation:23‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- OCI + ORAS + Cosign concept for data artifacts
- PR events as provenance + rollback/provenance repair runbooks [oai_citation:24‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe) [oai_citation:25‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- PDF portfolios (AI / maps / languages / data mgmt) contain many embedded references

</details>
