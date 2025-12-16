---
title: "🧪 KFM — On‑Sensor AQ Fusion: OpenAQ·PurpleAir·AQS (Quantile‑Mapping + Kalman/EnKF) → Minimal STAC Delta"
path: "mcp/experiments/air/on-sensor-fusion/README.md"

version: "v11.2.6"
last_updated: "2025-12-16"

release_stage: "Experimental / Governed"
lifecycle: "Short‑Lived Trial → Promote if Clean"
review_cycle: "Weekly · FAIR+CARE Council (escalate to Architecture Board on promotion / contract impact)"
content_stability: "changing"

status: "Active"
doc_kind: "Experiment"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "air-quality"
  applies_to:
    - "mcp/experiments/air/on-sensor-fusion/**"
    - "data/air-quality/**"
    - "data/updates/air-quality/**"
    - "data/reports/air-quality/**"
    - "data/stac/**"
    - "data/dcat/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low‑Risk (sensor data; location masking required for private sensors)"
sensitivity: "Potentially sensitive (private sensor locations, household‑adjacent placements)"
sensitivity_level: "Low"
public_exposure_risk: "Medium"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "6 months"
sunset_policy: "Auto‑expire unless promoted to a governed dataset/pipeline component"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "././releases/experiments/air/on-sensor-fusion/v11.2.6/signature.sig"
attestation_ref: "././releases/experiments/air/on-sensor-fusion/v11.2.6/slsa-attestation.json"
sbom_ref: "././releases/experiments/air/on-sensor-fusion/v11.2.6/sbom.spdx.json"
manifest_ref: "././releases/experiments/air/on-sensor-fusion/v11.2.6/manifest.zip"

telemetry_ref: "././releases/experiments/air/on-sensor-fusion/v11.2.6/focus-telemetry.json"
telemetry_schema: "././schemas/telemetry/markdown-protocol-v11.2.6.json"
energy_schema: "././schemas/telemetry/energy-v2.json"
carbon_schema: "././schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

doc_uuid: "urn:kfm:doc:mcp:experiments:air:on-sensor-fusion:v11.2.6"
semantic_document_id: "kfm-exp-air-on-sensor-fusion-v11.2.6"
event_source_id: "urn:kfm:event-source:mcp:air:on-sensor-fusion"

ontology_alignment:
  prov_o: "prov:Plan"
  schema_org: "TechArticle"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/standards/kfm_markdown_protocol_v11.2.6.md@v11.2.6"
  - "mcp/experiments/air/on-sensor-fusion/README.md@v11.2.6"

ai_transform_permissions:
  - "Summarization for readability"
  - "Timeline generation from cited facts"
  - "Semantic highlighting / terminology normalization"
  - "Accessibility adaptations (alt-text, a11y headings)"
  - "Diagram extraction into approved mermaid profiles"
  - "Metadata extraction into KFM-approved schema fields"
  - "Layout normalization to match KFM-MDP v11.2.6"
ai_transform_prohibited:
  - "Content alteration that changes meaning"
  - "Speculative additions not grounded in sources"
  - "Unverified architectural claims"
  - "Narrative fabrication (invented results/metrics)"
  - "Override of governance or sensitivity constraints"
immutability_status: "mutable-plan"
---

# 🧪 KFM — On‑Sensor AQ Fusion: OpenAQ·PurpleAir·AQS → Minimal STAC Delta

**Purpose**  
Prototype a **sensor‑first, bias‑aware PM2.5 fusion** workflow that (1) fuses co‑located OpenAQ / PurpleAir / AQS streams, (2) applies **quantile‑mapping bias correction** plus a **lightweight Kalman / EnKF smoother**, (3) emits **explicit QA/anomaly flags**, and (4) publishes a **minimal STAC delta** designed for **atomic apply + one‑command rollback**.

**Non‑goals (explicit)**  
- No external atmospheric model dependency (e.g., no CAMS) for this experiment.
- Not a replacement for regulatory reference monitoring; outputs remain **derived products** with QA.
- Not a new front‑end integration path (UI consumption stays **behind KFM APIs**, not direct graph access).

---

## 📘 Overview

### Hypothesis
A distribution‑aligned correction (quantile mapping to a local reference when available) plus a low‑order temporal filter can improve **comparability** and **interpretability** of low‑cost sensor PM2.5 while preserving anomalies via explicit QA flags.

### What “success” means (promotion gates for this trial)
This experiment is *promote‑eligible* only if, on held‑out periods and co‑located reference windows:

- Error does **not** worsen vs. a baseline (e.g., raw or simple linear correction) beyond a small tolerance.
- Distribution shift is controlled (e.g., corrected vs reference is “closer” under agreed tests).
- QA rules remain stable and auditable (flags explain “why”, with rule IDs + thresholds).

> These gates are intentionally conservative. Thresholds should be tuned under FAIR+CARE review before promotion.

### Outputs (what gets produced)
- Bias‑corrected and smoothed PM2.5 time series (machine‑readable).
- QA tables (flags + reasons) and a run summary report (machine + human).
- A **minimal STAC delta bundle** (only changed Items + minimal Collection update) designed for rollback.

---

## 🗂️ Directory Layout

~~~text
📁 Kansas-Frontier-Matrix/
├── 📁 mcp/
│   └── 📁 experiments/
│       └── 📁 air/
│           └── 📁 on-sensor-fusion/
│               ├── 📁 configs/                         🧾 Experiment configuration (seeded)
│               │   └── 🧾 experiment.yml
│               ├── 📁 src/                             🧠 Prototype code (no derived data here)
│               │   ├── 📄 fuse_quantmap_kalman.py
│               │   ├── 📄 anomaly_flags.py
│               │   └── 📄 stac_delta.py
│               ├── 📁 tests/                           ✅ Determinism + unit tests
│               │   └── 📁 fixtures/
│               └── 📄 README.md
├── 📁 data/
│   ├── 📁 air-quality/                                 🌫 Domain area (raw + processed)
│   │   ├── 📁 raw/                                     📥 Raw pulls (DVC/LFS as needed)
│   │   │   ├── 📁 openaq/
│   │   │   ├── 📁 purpleair/
│   │   │   └── 📁 aqs/
│   │   └── 📁 processed/                               🧮 Derived outputs (reproducible)
│   │       └── 📁 pm25_fused/
│   │           └── 📁 <run_id>/
│   ├── 📁 updates/                                     🔁 Incremental update payloads
│   │   └── 📁 air-quality/
│   │       └── 📁 <collection_id>/
│   │           └── 📁 <run_id>/
│   │               └── 📁 stac-delta/
│   ├── 📁 reports/                                     📊 QA summaries + review artifacts
│   │   └── 📁 air-quality/
│   │       └── 📁 on-sensor-fusion/
│   │           └── 📁 <run_id>/
│   ├── 📁 stac/                                        🗂 Published STAC catalog (static JSON)
│   └── 📁 dcat/                                        🌐 DCAT views/exports (if applicable)
└── 📁 releases/                                        🧾 Release artifacts (signatures/SBOMs)
~~~

---

## 🧭 Context

KFM’s pipeline is **ETL → STAC/DCAT/PROV catalogs → graph → APIs → UI**. This experiment lives at the **ETL + catalog emission** boundary:

- It generates a derived sensor product and publishes it as **catalog updates** (STAC delta).
- It emits **PROV lineage** suitable for ingestion into the provenance/graph layer.
- It does **not** change client behavior; UI remains behind the KFM API surface.

### Data handling note (important)
Some sensors (especially community devices) may be household‑adjacent. Public outputs must avoid exposing precise private locations. This experiment assumes **location masking/generalization** is applied before publishing (see Governance section).

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Raw sensor observations<br/>OpenAQ · PurpleAir · AQS"] --> B["Co-location<br/>H3 + radius + time window"]
  B --> C["Bias correction<br/>Quantile mapping to local reference"]
  C --> D["Temporal smoothing<br/>Kalman (scalar) or EnKF (small groups)"]
  D --> E["QA + anomaly flags<br/>spike · stuck · drift · dropout · mapping_gap"]
  E --> F["Minimal STAC delta<br/>changed Items + minimal Collection update"]
  F --> G["Apply/Rollback<br/>atomic, reviewable change-set"]
~~~

**Diagram explanation**  
Each stage is deterministic given `(config, seed, input snapshots)`. The “STAC delta” is designed to minimize blast radius: changes are isolated, reviewable, and revertible.

---

## 📦 Data & Metadata

### Inputs (expected)
- **OpenAQ**: brokered air‑quality observations where available.
- **PurpleAir**: PM2.5 observations from community devices.
- **EPA AQS**: reference measurements (preferred local reference where co‑located).

> Source licensing / use constraints must be reviewed per governance policy before promotion.

### Normalization conventions (recommended)
- Time: UTC
- Units: standardize to µg/m³ for PM2.5 (record original units where present)
- CRS: record and normalize if any geospatial transforms occur
- IDs: stable sensor IDs + stable STAC Item IDs across reruns

### Outputs (expected)
Under `data/air-quality/processed/pm25_fused/<run_id>/`:
- `pm25_fused_timeseries.parquet` (or equivalent): corrected + smoothed series
- `qa_flags.parquet`: per‑observation flags + reasons + thresholds
- `params/quantile_map.json`: mapping parameters per `(sensor_id, H3_cell)` (seeded)

Under `data/reports/air-quality/on-sensor-fusion/<run_id>/`:
- `run_manifest.json`: config hash, seed, git SHA, input snapshot references
- `qa_summary.json`: aggregated metrics and pass/fail gates for reviewers

Under `data/updates/air-quality/<collection_id>/<run_id>/stac-delta/`:
- `collection.json` (or minimal patch representation)
- `items/*.json` (only new/changed Items)
- `delta_manifest.json` (checksums + file list)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC Items (minimal but governed)
Each derived Item SHOULD include:
- `properties.qa:*` fields:
  - `qa:mask` (int bitmask)
  - `qa:flags` (array of strings)
  - `qa:notes` (array of short reason strings, include rule IDs)
- `properties.lineage:*` fields:
  - `lineage:method` = `"on-sensor-fusion|quantile-map|kalman"` (or `"|enkf"`)
  - `lineage:params_ref` → asset reference (e.g., quantile map params)
- Checksums for assets/distributions (align with KFM provenance + integrity practice).

### STAC versioning (required for safe deltas)
When Items are updated, apply the **STAC Versioning Extension** patterns:
- Use `version` and `deprecated` fields on Items when appropriate.
- Add predecessor/successor link relations to preserve update lineage.

### DCAT view (if emitted)
If the repo’s DCAT export is maintained for this collection, ensure:
- The derived dataset is discoverable as a dataset/distribution.
- Distributions point to STAC and/or downloadable assets.
- Checksums and provenance references remain consistent.

### PROV lineage (minimal, auditable)
Emit a PROV JSON‑LD bundle per run that records:
- `prov:Activity` = this fusion run (include seed + config hash + code ref).
- `prov:used` = raw sensor observation Entities and parameter Entities.
- `prov:wasGeneratedBy` = corrected output Entities and STAC delta Entities.

---

## 🧠 Story Node & Focus Mode Integration

If promoted to a surfaced product:
- Story Nodes must be **evidence-led**: narrative claims should be backed by the QA summary and/or provenance references.
- Avoid exposing precise private sensor coordinates in narrative/UI; prefer:
  - aggregation to H3 cells / counties, or
  - generalized location statements appropriate to sensitivity policy.
- Any anomaly callouts (“spike”, “drift”) should link to:
  - the rule ID,
  - the threshold used,
  - the affected time window, and
  - the run’s provenance bundle.

---

## 🧪 Validation & CI/CD

### Determinism & reproducibility
- All stochastic components (e.g., EnKF perturbations) MUST be seed‑controlled.
- Store a `run_manifest.json` with config hash + input snapshot identifiers to support one‑click reruns.

### Minimum CI expectations (align to KFM-MDP)
This README and its artifacts should pass:
- Markdown lint + schema lint
- Footer/governance link checks
- Diagram checks (approved mermaid profile, no HTML)
- Secret/PII scan (especially important given location sensitivity)

### Proposed data‑quality gates (trial defaults)
Fail the run (block promotion) if any of the following are true on the evaluation slice:
- Too many severe QA flags (spike/stuck above an agreed tolerance)
- Corrected distribution diverges meaningfully from local reference under agreed tests
- Reference error worsens materially vs baseline

> Exact thresholds should be set in `configs/experiment.yml` and treated as governed parameters.

### Commands (scaffold; adapt to actual entrypoints)
1) Run fusion (produce processed outputs + QA)
~~~bash
python mcp/experiments/air/on-sensor-fusion/src/fuse_quantmap_kalman.py \
  --config mcp/experiments/air/on-sensor-fusion/configs/experiment.yml \
  --run-id <run_id>
~~~

2) Emit minimal STAC delta
~~~bash
python mcp/experiments/air/on-sensor-fusion/src/stac_delta.py \
  --collection-id <collection_id> \
  --run-id <run_id>
~~~

3) Apply / rollback (one-command rollback)
**Preferred “one-command each” approach for a trial:** emit a git patch alongside the delta.
- Apply:
~~~bash
git apply data/updates/air-quality/<collection_id>/<run_id>/stac-delta/stac-delta.patch
~~~
- Roll back:
~~~bash
git apply -R data/updates/air-quality/<collection_id>/<run_id>/stac-delta/stac-delta.patch
~~~

> If the repo provides a CLI in `tools/cli/` for delta application, prefer that. (Not confirmed here—verify in repo.)

---

## ⚖ FAIR+CARE & Governance

### CARE + sovereignty
- Treat household‑adjacent sensor placement as potentially sensitive.
- Apply location masking/generalization before publishing public STAC (e.g., store H3 cell geometry/centroid instead of exact coordinates when required by sensitivity policy).
- Ensure any community‑sourced data handling is aligned with Indigenous Data Protection policy where applicable.

### Supply-chain + release integrity (for promotion)
If this experiment is promoted into a governed dataset/pipeline component, releases should include:
- SBOM + provenance + signatures/attestations as required by KFM security posture.
- Clear dependency review (new libraries/models must pass governance/security review).

### What requires human approval
- Introducing new external services/dependencies
- Publishing unmasked locations for non-reference sensors
- Changing STAC/DCAT/PROV contracts or collection semantics
- Any Story Node narrative claims derived from “soft” sensor inferences

---

## 🕰️ Version History

- **v11.2.6 (2025-12-16)** — Initial experiment README, aligned to KFM‑MDP v11.2.6 headings/fencing, updated repo‑consistent paths (`data/air-quality/`, `data/updates/`, `data/stac/`, `data/dcat/`), and added deterministic + rollback-first STAC delta workflow.

---

Back to index ▸ docs/README.md · Data Architecture ▸ docs/architecture/README.md · Governance Charter ▸ docs/standards/governance/ROOT-GOVERNANCE.md · FAIR+CARE ▸ docs/standards/faircare/FAIRCARE-GUIDE.md · Sovereignty ▸ docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md