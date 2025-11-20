---
title: "🌊 Kansas Frontier Matrix — Republican River Streamflow Lineage (1910–2020) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/archives/provenance/chains/dataset-lineage/hydrology/streamflow/ks_mainstem/republican-river/1910_2020/README.md"
version: "v11.0.1"
last_updated: "2025-11-20"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Governance Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../../../../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../../../../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../../../../../../../../../schemas/telemetry/archives-provenance-republican-1910-2020-v1.json"
governance_ref: "../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
status: "Active / Enforced"
doc_kind: "Provenance Dataset Instance"
intent: "archives-provenance-streamflow-republican-river-1910-2020"
fair_category: "F1-A1-I1-R1"
care_label: "C1 · Indigenous Knowledge Protection Enabled"
---

# 🌊 Kansas Frontier Matrix — **Republican River Streamflow Lineage (1910–2020)**

This directory hosts the **authoritative PROV-O JSON-LD lineage chain**  
for the **1910–2020 Republican River streamflow dataset** — one of the longest,  
most interstate-governed, and most hydrologically significant datasets in the  
Kansas Frontier Matrix system.

The Republican River is a **tri-state watershed** (Colorado → Nebraska → Kansas)  
governed by interstate compacts, tribal water rights, agricultural demand,  
and complex climate–hydrology interactions.  
This lineage ensures every transformation from raw observation to final archive  
is fully traceable, reproducible, FAIR+CARE compliant, and governance-signed.

---

# 📁 1. Directory Layout (DL-C Compliant)

```
docs/.../republican-river/1910_2020/
├── README.md                     ← this file
└── lineage.jsonld                ← canonical PROV-O dataset lineage
```

`lineage.jsonld` is the **sole authoritative provenance graph** representing  
all Entities, Activities, and Agents in the 1910–2020 hydrologic record.

---

# 🧬 2. Dataset Overview

### Temporal Coverage  
**1910–2020** (110 years)

### Spatial Extent  
Kansas-relevant reach of the Republican River, including influence from  
Colorado headwaters and Nebraska mainstem contribution.

### Data Sources  
- USGS long-term gauge network  
- Tri-state compact hydrology datasets  
- Irrigation district logs  
- Municipal intake/outflow records  
- Field hydrometry notebooks  
- Reservoir (Harlan County Lake) release logs  
- Tribal water-observation data (CARE-governed)  
- Satellite hydrometry and climate data (post-1980)

---

# 📜 3. PROV-O Entity Structure (`prov:Entity`)

Each dataset state includes:

### **Raw (1910–1950)**  
- Handwritten gauge logs  
- Mechanical chart recorders  
- Early cross-state hydrology reports  
- Digitized microfilm scans  

### **Calibrated (1950–1990)**  
- Stage–discharge equation correction  
- Datum harmonization across tri-state jurisdiction  
- Mechanical noise removal  

### **Processed (1990–2020)**  
- Sensor drift correction  
- Multi-gauge alignment  
- Ice-affected correction  
- Event (flood/drought) harmonization  

### **Harmonized (AI-Augmented)**  
- Focus Mode v2.5 gap-filling & smoothing  
- ML-Fusion satellite–gauge blending  
- Story Node v3 climate-conditioned narratives  

### **Archived Final**  
Includes:

- PID  
- STAC/DCAT descriptors  
- CARE metadata  
- SBOM/SLSA references  
- ASCII reconstruction instructions  
- SHA-256 digest  

---

# ⚙️ 4. PROV-O Activity Structure (`prov:Activity`)

Activities capture:

### 🖨 Digitization  
- OCR + manual correction of early hydrology documents  
- Cultural review of tribal-held water knowledge  

### 🧪 Calibration  
- Instrument drift correction  
- Datum alignment across CO–NE–KS  
- Reconstruction of historical stage–discharge tables  

### 🛠 Processing  
- Consistency alignment across multi-station networks  
- Removal of outliers  
- Hydrologic plausibility checks  

### 🛰 Modeling  
- HEC-HMS rainfall–runoff calibration  
- Compact-focused hydrologic balancing  
- Flood-frequency modeling  
- Groundwater–surface water interaction corrections  

### 🤖 AI Enhancement  
- Focus Mode v2.5 reconstructive sequences  
- Story Node v3 scenario-based augmentation  
- ML-Fusion climate/satellite integration  

### 🗄 Archival Packaging  
- FAIR+CARE validation  
- Governance approval  
- SBOM/SLSA notarization  
- Carbon/energy telemetry logging  
- Reconstructibility success checks  

---

# 👤 5. PROV-O Agents (`prov:Agent`)

Agents include:

- USGS hydrologists  
- Colorado/Nebraska/Kansas compact officers  
- Tribal water stewards (CARE-restricted)  
- Digitization technicians  
- Focus Mode v2.5 (AI agent)  
- Story Node v3 (narrative generator)  
- ETL/lineage engines  
- Governance reviewers  

Each agent features documented role, authority, and responsibilities.

---

# 🧪 6. Validation Requirements

All lineage artifacts must pass:

- PROV-O JSON-LD schema validation  
- Full SHA-256 hash-chain continuity  
- SBOM/SLSA integrity checks  
- Hydrologic plausibility screening  
- CARE governance audit  
- Tri-state calibration consistency tests  
- Full ASCII-based synthetic rebuild trial  

Only **perfectly valid** lineages enter the KFM Archive.

---

# 🔎 7. Retrieval Examples (v11.2+)

```
kfm provenance chains expand --dataset hydrology/streamflow/ks_mainstem/republican-river/1910_2020
kfm provenance chains reconstruct --id hydrology/.../republican-river/1910_2020
kfm provenance chains agent --name "FocusMode v2.5"
```

---

# 🔮 8. Roadmap (v11.3–v12.0)

- Tri-state hydrologic continuity lineage  
- AI synthetic compact compliance modeling  
- Climate-conditioned reconstruction lineage  
- CARE-governed tribal hydrology extensions  
- 4D lineage visualization (flow × time × uncertainty × climate)  

---

# 📚 9. Version History

- **v11.0.1** — First Republican River 1910–2020 lineage file (KFM-MDP v11 compliant)  
- **v10.x** — Legacy hydrology archives stored pre–KFM v11  

---

# **Kansas Frontier Matrix — Republican River Streamflow Lineage (1910–2020)**  
🌊 Long-Term Hydrologic Continuity · 🧬 Immutable Provenance · ⚖️ FAIR+CARE Governance  

[⬅️ Back to Republican River Lineage](../README.md) ·  
[📁 Mainstem Hydrology Root](../../README.md) ·  
[⚖️ Governance Charter](../../../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

