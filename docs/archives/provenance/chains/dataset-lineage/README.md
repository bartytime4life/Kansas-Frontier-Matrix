---
title: "🧬 Kansas Frontier Matrix — Dataset Lineage Chains (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/archives/provenance/chains/dataset-lineage/README.md"
version: "v11.0.1"
last_updated: "2025-11-19"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/archives-provenance-dataset-lineage-v1.json"
governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
status: "Active / Enforced"
doc_kind: "Provenance Subsystem Detail"
intent: "archives-provenance-dataset-lineage"
fair_category: "F1-A1-I1-R1"
care_label: "C1 · Indigenous Knowledge Protection Enabled"
---

# 🧬 Kansas Frontier Matrix — **Dataset Lineage Chains**

The **Dataset Lineage Chains** directory provides the authoritative, immutable life-cycle histories  
for every dataset ingested into the Kansas Frontier Matrix Archives.  
Each lineage record follows **PROV-O JSON-LD**, **FAIR+CARE**, and **MCP-DL v6.3** standards,  
ensuring that all datasets — historical, scientific, ecological, hydrologic, cultural, or AI-generated —  
are **fully reconstructible, ethically governed, and cryptographically verifiable**.

This subsystem captures:

- Raw → Calibrated → Processed → Harmonized → Archived transformations  
- All intermediate derivations & versions  
- Tools, models, pipelines, and human/AI agents involved  
- Hash-verified integrity at each stage  
- Governance & CARE controls  
- Complete rebuild instructions for future reproducibility  

No dataset may enter the archive without a valid lineage chain.

---

# 📁 1. Directory Layout (DL-C Compliant)

```
docs/archives/provenance/chains/dataset-lineage/
├── README.md                     ← this file
├── hydrology/
│   ├── streamflow/
│   ├── aquifer/
│   └── watershed/
├── climatology/
│   ├── normals/
│   ├── anomalies/
│   └── paleoclimate/
├── ecology/
│   ├── biodiversity/
│   ├── vegetation/
│   └── biomass/
├── historical/
│   ├── plats/
│   ├── land-records/
│   ├── census-series/
│   └── treaty-boundaries/
└── ai-generated/
    ├── synthetic-tabular/
    ├── focus-mode/
    └── story-node-v3/
```

Each subfolder contains **immutable PROV-O lineages** documenting the complete  
dataset history, stored as JSON-LD files with KFM metadata extensions.

---

# 🔗 2. What a Dataset Lineage Chain Contains

A dataset lineage chain consists of:

### 🧩 Entity Nodes  
Every state of the dataset:  
`raw`, `calibrated`, `processed`, `normalized`, `harmonized`, `archived`.

Each state includes:

- SHA-256 digest  
- Storage location  
- Timestamp  
- CARE metadata (if relevant)  
- SBOM reference  
- Reconstruction entry  

### ⚙️ Activity Nodes  
All transformations, such as:

- Digitization  
- Calibration  
- Preprocessing  
- Normalization  
- Hydrologic/Climatologic/Ecologic modeling  
- Raster/Vector transformations  
- AI inference, synthesis, or reconstruction  

Each activity captures:

- Toolchain & software (with SBOM hash)  
- Parameters & hyperparameters  
- Execution environment  
- Energy and carbon telemetry  

### 👤 Agent Nodes  
Agents involved may include:

- Field researchers  
- Archivists  
- Data engineers  
- Tribal/Community review boards  
- Scientific analysts  
- Focus Mode v2.5  
- Story Node v3  
- Automated ETL pipelines  

Every agent is identified with role, responsibility, and contribution.

---

# 🔍 3. Supported Dataset Types

Lineage records in this directory include:

### 🌊 Hydrology  
Streamflow time-series, aquifer boundaries, groundwater recharge, sediment load.

### 🌦️ Climatology  
Normals, anomalies, downscaled projections, paleoclimate reconstructions.

### 🌱 Ecology  
Species surveys, biodiversity grids, biomass estimates, vegetation indices.

### 🏛️ Historical  
Plats, treaty boundary maps, land records, census rolls, cultural landscapes.

### 🤖 AI-Generated  
Synthetic datasets, cross-domain fusion layers, Story Node v3 outputs.

---

# 🛠️ 4. Ingestion Requirements

Every lineage chain **must** include:

1. PROV-O JSON-LD graph  
2. SHA-256 digest for every dataset state  
3. SBOM reference (SPDX + CycloneDX)  
4. SLSA attestations for all transformations  
5. CARE impact and access-control metadata  
6. Energy & carbon telemetry per activity  
7. Activity parameters, hyperparameters, and execution context  
8. Reconstruction instructions (ASCII-only per KFM-MDP v11 rules)  

No dataset is accepted without a **complete, validated** lineage chain.

---

# 🧪 5. Validation & Continuity

Upon ingestion:

- Graph is checked for continuity (all entities must resolve)  
- Timestamp ordering validated  
- Provenance nodes cross-checked with STAC/DCAT metadata  
- Hashes verified end-to-end  
- Agent roles validated  
- SBOM + SLSA integrity checks performed  
- CARE review logged  

Only complete, schema-valid chains enter the archive.

---

# 🔎 6. Retrieval Examples (v11.2+)

```
kfm provenance chains expand --dataset hydrology/streamflow/ks_1903
kfm provenance chains reconstruct --id climatology/normals/kansas_1991_2020
kfm provenance chains agent --name "FocusMode v2.5"
```

These commands reconstruct lineage histories, dependencies, and agent contributions.

---

# 🔮 7. Roadmap (v11.3–v12.0)

- Multi-dataset lineage fusion for environmental synthesis  
- Temporal lineage animation in Story Node v3  
- Cross-institutional provenance federation with tribal/state archives  
- AI-assisted lineage “gap detection”  
- Distributed notarization of dataset transformations  

---

# 📚 8. Version History

- **v11.0.1** — First KFM-MDP v11-compliant dataset-lineage overview  
- **v10.4.x** — Draft lineage records added  
- **v10.x** — Initial lineage directory creation  

---

# **Kansas Frontier Matrix — Dataset Lineage Chains**  
🧬 Immutable Lineage · 🔗 PROV-O Chains · ⚖️ Governance-Compliant

[⬅️ Back to Provenance Chains](../README.md) ·  
[📁 Provenance Root](../../provenance/README.md) ·  
[⚖️ Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md)

