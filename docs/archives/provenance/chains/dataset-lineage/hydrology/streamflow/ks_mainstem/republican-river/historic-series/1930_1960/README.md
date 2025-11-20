---
title: "📜🌊 Kansas Frontier Matrix — Republican River Historic Streamflow Lineage (1930–1960 Series) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/archives/provenance/chains/dataset-lineage/hydrology/streamflow/ks_mainstem/republican-river/historic-series/1930_1960/README.md"
version: "v11.0.1"
last_updated: "2025-11-20"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Governance Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../../schemas/telemetry/archives-provenance-republican-historic-1930-1960-v1.json"
governance_ref: "../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
status: "Active / Enforced"
doc_kind: "Historical Provenance Instance"
intent: "archives-provenance-streamflow-republican-river-historic-1930-1960"
fair_category: "F1-A1-I1-R1"
care_label: "C1 · Indigenous Knowledge Protection Enabled"
---

# 📜🌊 Kansas Frontier Matrix — **Republican River Historic Streamflow Lineage (1930–1960)**

This directory contains the **complete PROV-O JSON-LD provenance chain**  
for **Republican River hydrologic datasets from 1930–1960**, documenting a  
major era of modernization in U.S. river monitoring and water-management  
infrastructure.

The 1930–1960 period includes:

- Widespread adoption of **mechanical chart recorders**  
- Early cross-state hydrology coordination for the Republican River Compact  
- Expansion of municipal and agricultural water infrastructure  
- Mid-century flood-control projects  
- Increasing documentation for groundwater/surface-water interactions  
- Tribal water observations (CARE-restricted)  

Every transformation—from raw strip-chart scans to final archived dataset—  
is recorded, validated, and protected under **FAIR+CARE**, **SBOM/SLSA**,  
and **MCP-DL v6.3** governance.

---

# 📁 1. Directory Layout (DL-C Compliant)

```
docs/.../historic-series/1930_1960/
├── README.md                     ← this file
└── lineage.jsonld                ← canonical PROV-O historical provenance graph
```

`lineage.jsonld` is the authoritative, hash-verified lineage graph  
representing the dataset’s full Entity–Activity–Agent structure.

---

# 🕰️ 2. Overview of 1930–1960 Hydrologic Sources

### 📈 Mechanical & Analog Instrumentation  
- Strip-chart hydrographs  
- Mechanically recorded stage/discharge curves  
- Drum recorders and analog velocity meters  
- Paper and mylar hydrology strips  

### 📚 Municipal & Engineering Records  
- Bridge and levee inspection hydrology  
- Waterworks intake & operations logs  
- Irrigation/diversion reports  
- Floodplain engineering notebooks  

### 🏛 Federal & State Hydrology  
- Early USGS standardized datasets  
- Army Corps flood-control engineering surveys  
- State hydrology bureau expansion  
- Compact-era tri-state hydrology coordination  

### 🪶 Tribal Water Knowledge (CARE-Restricted)  
- Seasonal flow knowledge  
- Cultural hydrologic histories  
- Restricted narrative and observational data  
- CARE-sensitive metadata  

---

# 🧬 3. PROV-O Entity Requirements (`prov:Entity`)

Each dataset state includes:

- SHA-256 digest  
- Source classification (strip-chart, ledger, notebook, narrative)  
- Digitization metadata (scanner type, distortion correction, OCR edits)  
- CARE metadata (permission-level, sensitivity classification)  
- Data schema (flow, stage, event notes, units)  
- STAC/DCAT cross-references  
- ASCII-only reconstruction instructions  
- SBOM reference  

---

# ⚙️ 4. PROV-O Activity Requirements (`prov:Activity`)

Activities document each transformation:

### 🖨 Digitization  
- Scan capture & resolution normalization  
- OCR + manual transcription  
- Geometric correction of strip-chart distortions  
- CARE cultural review  

### 🧪 Calibration  
- Rebuilding discharge curves  
- Drift/noise removal for mechanical recorders  
- Datum reconciliation across multiple sites  
- Snowmelt/ice correction for winter records  

### 🛠 Cleaning & Processing  
- Time normalization  
- Event annotation alignment  
- Outlier detection & correction  
- Hydrologic plausibility tests  

### 🗄 Archival Integration  
- PID assignment  
- FAIR metadata validation  
- CARE governance review  
- SBOM/SLSA attestation  
- Reconstruction reproducibility checks  
- Carbon/energy telemetry  

---

# 👤 5. PROV-O Agents (`prov:Agent`)

Agents include:

- USGS hydrology teams  
- State water bureaus  
- Municipal waterworks engineers  
- Digitization technicians & archivists  
- Tribal cultural stewards (CARE-restricted)  
- KFM lineage engine  
- ETL pipelines  
- Governance auditors  

All agents include role, authority domain, and contribution metadata.

---

# 🧪 6. Validation Requirements

A 1930–1960 lineage chain must pass:

- PROV-O schema validation  
- SHA-256 hash-chain continuity  
- SBOM/SLSA toolchain verification  
- Digitization accuracy audit  
- Hydrologic plausibility cross-checks  
- Tri-state hydrology continuity validation  
- CARE governance review  
- ASCII-based reproduction test  

Only lineage chains passing **all tests** enter the KFM Archive.

---

# 🔎 7. Retrieval Examples (v11.2+)

```
kfm provenance chains expand --dataset hydrology/streamflow/ks_mainstem/republican-river/historic-series/1930_1960
kfm provenance chains reconstruct --id hydrology/.../historic-series/1930_1960
kfm provenance chains agent --name "USGS Field Team"
```

---

# 🔮 8. Roadmap (v11.3–v12.0)

- Machine-learning enhancement of degraded strip-chart scans  
- Multi-era continuity lineage (pre-1900 → 1930–1960 → 2024)  
- CARE-governed tribal hydrology integration  
- Hydro-climate lineage fusion with Story Node v3  
- 4D lineage visualization (flow × time × climate × uncertainty)  

---

# 📚 9. Version History

- **v11.0.1** — First Republican River 1930–1960 file (KFM-MDP v11 compliant)  
- **v10.x** — Early hydrology lineage preserved under legacy schema  

---

# **Kansas Frontier Matrix — Republican River Historic Series (1930–1960)**  
📜 Mid-Century Hydrology · 🧬 Immutable Provenance · ⚖️ FAIR+CARE Governance  

[⬅️ Back to Historic Series](../README.md) ·  
[📁 Mainstem Hydrology Root](../../README.md) ·  
[⚖️ Governance Charter](../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

