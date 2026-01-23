---
title: "🧪 KFM — On‑Sensor AQ Fusion: OpenAQ·PurpleAir·AQS (Quantile‑Mapping + Kalman/EnKF) → Minimal STAC Delta"
path: "mcp/experiments/air/on-sensor-fusion/README.md"

version: "v11.2.6"
last_updated: "2025-12-16"

release_stage: "Experimental / Governed"
lifecycle: "Short‑Lived Trial → Promote if Clean"
review_cycle: "Weekly · FAIR+CARE & Data Quality Board"
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

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"

commit_sha: "<latest-commit-hash>"
provenance_chain:
  - "mcp/experiments/air/on-sensor-fusion/README.md@v11.2.6"

semantic_document_id: "kfm-experiment-air-on-sensor-fusion-v11.2.6"
doc_uuid: "urn:kfm:doc:mcp:experiments:air:on-sensor-fusion:v11.2.6"
event_source_id: "ledger:kfm:doc:mcp:experiments:air:on-sensor-fusion:v11.2.6"

ai_transform_permissions:
  - "summarization"
  - "extraction"
  - "normalization"
  - "translation"
  - "formatting"

ai_transform_prohibited:
  - "alter_normative_requirements"
  - "invent_governance_status"
  - "fabricate_provenance"
  - "claim_unverified_lineage"
  - "override_review_status"
---

<div align="center">

# 🧪 **KFM — On‑Sensor AQ Fusion: OpenAQ·PurpleAir·AQS (Quantile‑Mapping + Kalman/EnKF) → Minimal STAC Delta**
`mcp/experiments/air/on-sensor-fusion/README.md`

**Purpose**  
Here’s a compact, KFM‑ready experiment that fuses co‑located OpenAQ / PurpleAir / AQS streams on‑sensor, applies bias‑aware quantile mapping + a lightweight Kalman/EnKF smoother, flags anomalies, and emits a minimal STAC “delta” you can roll back with one command.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governed-orange" />
<img src="https://img.shields.io/badge/Status-Active-brightgreen" />

</div>

---

## 📘 Overview

Goal: **Fuse co‑located sensors** (OpenAQ brokered feeds, PurpleAir devices, EPA AQS reference sites) at the **sensor level** to produce **bias‑corrected, temporally smoothed PM2.5** with **rich QA flags**, then publish a **minimal STAC delta** that’s easy to roll back.  
**No CAMS dependency** — stay strictly on‑sensor for transparency and sovereignty.

### Why this matters (short)

- **Trust:** Sensor‑first fusion + distributional correction improves comparability without hiding errors.
- **Safety:** Delta‑only publishing with explicit QA and rollback minimizes blast radius.
- **Governance:** Clear PROV lineage, FAIR+CARE labels, and anomaly flags keep Story Nodes honest.

## 🗂️ Directory Layout

~~~text
mcp/experiments/air/on-sensor-fusion/
├── ⚙️ configs/                              # Experiment configuration (sources, H3 resolution, QA thresholds)
│   └── 🧾 experiment.yml                    # Declared config: sources, H3 resolution, co-location rules, QA thresholds
├── 🛠️ src/                                  # Fusion pipeline implementation (config-driven; reproducible entrypoints)
│   ├── 🧪📄 fuse_quantmap_kalman.py          # Fusion + quantile mapping + Kalman/EnKF smoothing for corrected series
│   ├── 🚨📄 anomaly_flags.py                 # QA flags: spikes, stuck sensors, drift vs reference, missingness checks
│   └── 🛰️📄 stac_delta.py                    # Emit minimal STAC deltas (Items + Collection updates) for this run’s outputs
├── 📦 data/                                 # Local data for the experiment (keep cache bounded; outputs are reviewable)
│   ├── 🧊 cache/                            # Cached raw pulls (OpenAQ / PurpleAir / AQS); treat as immutable per pull
│   └── ✅ outputs/                          # Produced artifacts: corrected timeseries, QA tables, and stac-delta/ bundle
└── 🧪 tests/                                # Deterministic tests (fixed seeds, golden fixtures, minimal dependencies)

## 🗺️ Diagrams

### Architecture (high‑level)

~~~mermaid
flowchart LR
  A[Raw feeds - OpenAQ PurpleAir AQS] --> B[Co location - H3 r8 + radius + time window]
  B --> C[Bias aware correction - quantile mapping - ibicus python cmethods style]
  C --> D[Temporal smoother - Kalman or EnKF low order]
  D --> E[QA and anomaly flags - spike stuck drift dropout]
  E --> F[Minimal STAC delta - items + assets + QA fields]
  F --> G[Publish + rollback - atomic delta apply revert]
~~~

## 🧱 Architecture

Method

1. Co‑location  
   - Snap each observation to H3 cell (configurable, e.g., r=8) + temporal window (e.g., 10–15 min).  
   - Prefer AQS as local reference when available; otherwise use robust median of collocated PurpleAir pairs.

2. Bias‑Aware Quantile Mapping  
   - Learn CDF mapping per (sensor_id, H3_cell) from overlapping history with reference.  
   - Use robust bins (winsorized tails) and holdout for leakage control.  
   - Persist mapping params with seeded reproducibility.

3. Temporal Smoothing  
   - Kalman (scalar state with random walk) or EnKF for small collocated groups.  
   - Tune process/obs variances via cross‑validated AIC/BIC on rolling windows.

4. QA & Anomaly Flags  
   - qa_spike, qa_stuck, qa_drift, qa_dropout, qa_mapping_gap.  
   - Encode flags as bit‑mask + human‑readable reasons; include provenance (rule_id, thresholds).

5. Minimal STAC Delta  
   - Only changed Items/assets emitted under data/outputs/stac-delta/.  
   - Add properties.qa.*, properties.lineage.*, checksums, and CARE/FAIR labels.  
   - Collection summary updated incrementally (no full republish).

## 📦 Data & Metadata

Config (excerpt) — configs/experiment.yml

~~~yaml
seed: 42
h3_resolution: 8
time_window_minutes: 15
sources:
  - openaq: {streams: ["pm25"], max_lag_min: 5}
  - purpleair: {fields: ["pm2_5_atm"], a_correction: true}
  - aqs: {parameters: ["PM25"], use_as_reference: true}
colocation:
  radius_m: 500
  min_overlap_points: 250
quantile_mapping:
  bins: 51
  tail_winsor: {lower_q: 0.01, upper_q: 0.99}
smoother:
  method: "kalman"   # or "enkf"
  process_var: 0.04
  obs_var: 0.16
qa_flags:
  spike_z: 4.0
  stuck_flatline_min: 60  # minutes
  drift_ppb_hr: 15
publish:
  stac_delta_dir: "data/outputs/stac-delta"
  collection_id: "kfm-aq-pm25"
rollback:
  enable: true
~~~

## 🌐 STAC, DCAT & PROV Alignment

STAC/DCAT & PROV Alignment

- STAC Item properties:
  - qa:flags (array) and qa:mask (int), qa:notes
  - lineage:method = "on-sensor-fusion|quantmap|kalman"
  - lineage:params_ref → JSON in assets/params.json
  - care:labels, fair:principles refs
- PROV: prov:wasDerivedFrom raw sensor Items; prov:used params; prov:wasGeneratedBy job (seed, git SHA, container digest).

## 🧪 Validation & CI/CD

Commands

1) Run fusion

~~~bash
python -m src.fuse_quantmap_kalman --config configs/experiment.yml --out data/outputs
~~~

2) Emit minimal delta

~~~bash
python -m src.stac_delta --collection kfm-aq-pm25 --delta-dir data/outputs/stac-delta
~~~

3) Apply / Roll back (one easy command each)

~~~bash
# apply
kfm stac delta apply --dir data/outputs/stac-delta --sign --attest

# rollback last apply
kfm stac delta rollback --dir data/outputs/stac-delta --to previous
~~~

Data‑Quality Gates (promotion)

- Fail promotion if:
  - 2% Items carry qa_spike|qa_stuck OR
  - KS test p<0.01 between corrected & reference distributions OR
  - RMSE vs. AQS worsens >5% vs. baseline.
- Emit OpenLineage event + PROV JSON‑LD on pass/fail.

## ⚖ FAIR+CARE & Governance

- CARE: Local calibration stays local; no external CAMS pull; community audit notes included.
- FAIR: Delta Items have checksums, JSON Schemas, and discoverable QA fields.
- Signed via Sigstore/Cosign v3; SLSA‑style attestations attached.

## 🕰️ Version History

- v11.2.6 (2025‑12‑16) — Initial experiment scaffold, quantile mapping + Kalman path, minimal STAC delta + rollback.

⸻

---

<div align="center">

🧪 **Kansas Frontier Matrix** — On‑Sensor AQ Fusion experiment (OpenAQ · PurpleAir · AQS)

Back to index ▸ docs/README.md · Data Architecture ▸ docs/architecture/README.md · Governance Charter ▸ docs/standards/governance/ROOT-GOVERNANCE.md

[📘 Docs Root](../../../../docs/README.md) · [📂 Standards Index](../../../../docs/standards/README.md) · [📄 Templates Index](../../../../docs/templates/README.md) · [⚙ CI/CD Workflows](../../../../docs/workflows/README.md) · [📈 Telemetry Standard](../../../../docs/standards/telemetry_standards.md) · [📊 Telemetry Docs](../../../../docs/telemetry/README.md) · [♿ UI Accessibility](../../../../docs/standards/ui_accessibility.md)

[🏛 Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) · [🧭 FAIR+CARE Guide](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) · [🪶 Indigenous Data Protection](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

MCP‑DL v6.3 · KFM‑MDP v11.2.6 · KFM‑OP v11 · KFM‑PDC v11

</div>
