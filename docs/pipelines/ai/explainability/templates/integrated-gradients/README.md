---
title: "⚡ KFM v11 — Integrated Gradients Explainability Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/explainability/templates/integrated-gradients/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Explainability WG · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../../../../releases/v11.2.3/integrated-gradients-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-explainability-integrated-gradients-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

doc_kind: "Explainability Template"
intent: "integrated-gradients-explainability-template"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant · Sensitivity-Aware"

classification: "Public (Governed)"
sensitivity: "Low/Moderate"
machine_extractable: true
jurisdiction: "United States · Kansas"
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# ⚡ **Integrated Gradients Explainability Template (KFM v11)**  
`docs/pipelines/ai/explainability/templates/integrated-gradients/`

**Purpose**  
Provide the official **v11 integrated gradients (IG) explainability template**  
for all KFM AI pipelines that rely on deep learning or differentiable models.  
Supports climate, hydrology, soils, ecology, wildfire, atmosphere, and remote-sensing AI stacks.

Integrated Gradients (IG) is required for neural-network–based explainability  
due to its **axiomatic guarantees**, **model faithfulness**, and **sensitivity** properties.

</div>

---

## 📘 1. Overview — What Integrated Gradients Provide

Integrated Gradients quantify:

> **“How much each input contributed to the AI model’s output by integrating the gradient along a path from a baseline to the true input.”**

This template defines:

- How IG maps are generated  
- Required metadata (STAC/DCAT + JSON-LD)  
- Provenance (PROV-O + OpenLineage)  
- Sustainability telemetry (energy, carbon)  
- CARE-aligned handling of sensitive geographies  
- H3-compatible attribution output formats  
- Story Node v3 integration  

Designed for:  
CNNs · RNNs · transformers · GNNs · climate downscalers · spatial models · sequence models.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/ai/explainability/templates/integrated-gradients/
├── 📄 README.md                        # This file
│
├── ⚡ templates/                       # Baseline IG templates
│   ├── 📊 ig_global_template.parquet   # Global attribution aggregation
│   ├── 📍 ig_local_template.parquet    # Per-instance attribution map
│   ├── 🧬 ig_temporal_template.parquet # Time-series IG attributions
│   └── 🧭 ig_h3_template.parquet       # Hex-grid generalization output
│
├── 🌐 stac/                            # STAC templates
│   ├── 📄 item-template.json
│   └── 📄 collection-template.json
│
├── 🔗 lineage/                         # PROV-O + OpenLineage metadata
│   ├── 🧾 prov-template.json
│   └── 📡 ol-template.json
│
├── 🧪 validation/                      # Validation requirements & scripts
│   ├── 📄 validate-integrity.md
│   ├── 📄 validate-metadata.md
│   ├── 📄 validate-care.md
│   └── 📄 validate-sustainability.md
│
└── 📊 examples/                        # Example IG runs
    ├── 📁 global/
    ├── 📁 local/
    ├── 📁 temporal/
    └── 📁 h3/
~~~

---

## ⚙️ 3. Integrated Gradients Standards (v11)

### Required IG Output Fields

| Field | Description | Required |
|-------|-------------|---------|
| `model:version` | Version of AI model | ✔ |
| `kfm:explainability_method` | `"integrated-gradients"` | ✔ |
| `kfm:domain` | climate, soil, hydro, etc. | ✔ |
| `kfm:input_variables` | Input features fed into model | ✔ |
| `baseline_description` | Baseline used in IG (zeros, climatology, soil reference) | ✔ |
| `integration_steps` | Number of integration steps used | ✔ |
| `kfm:sensitivity_flag` | CARE-sensitive handling | ✔ |
| `kfm:energy_wh` | Energy cost | ✔ |
| `kfm:carbon_gco2e` | Carbon emissions | ✔ |
| `datetime` | When inference occurred | ✔ |
| CRS / H3 fields | Required if spatial | conditional |

### Supported Output Types

- **Global IG:** aggregated across many predictions  
- **Local IG:** per-sample or per-grid-cell  
- **Temporal IG:** attribution over time  
- **H3 IG:** IG mapped to H3 grid for privacy + scale  

---

## 🧪 4. Validation Rules (v11)

All IG artifacts MUST pass:

### ✔ Spatial Integrity  
- All IG values finite  
- CRSs consistent (EPSG:4326 or H3).  
- Bounds match input dataset extents.  
- No unmasked sensitive coordinates.

### ✔ Metadata Completeness  
- All STAC fields populated  
- Model + explainability method pinned  
- Input variables listed  
- Energy & carbon metrics present

### ✔ CARE / Sovereignty  
- Sensitive areas masked or generalized  
- H3 R7–R9 used for high-risk zones  
- CARE flag correctly set

### ✔ Sustainability  
- IG computation must stay within pipeline budgets  
- Metrics appended to STAC + OpenLineage

Validation failure → rollback (Reliability Layer v11).

---

## 🌐 5. STAC Templates (Required Fields)

Each IG output MUST publish a STAC Item:

- `datetime`  
- `model:version`  
- `kfm:explainability_method="integrated-gradients"`  
- `kfm:input_variables`  
- `kfm:energy_wh`  
- `kfm:carbon_gco2e`  
- `baseline_description`  
- `integration_steps`  
- `kfm:sensitivity_flag`  
- `assets.*` (IG parquet, IG raster, optional PNG previews)  
- Provenance links (OpenLineage + PROV-O)

Templates stored under:

~~~text
stac/item-template.json
stac/collection-template.json
~~~

---

## 🔗 6. Provenance (PROV-O + OpenLineage)

Every IG run MUST include:

### PROV-O
- `prov:Activity` — IG generation event  
- `prov:used` — input datasets + model artefacts  
- `prov:generated` — IG attribution outputs  
- `prov:wasAssociatedWith` — agent performing IG

### OpenLineage
- runId / job facets  
- attribution asset pointers  
- temporal info  
- hardware resource usage (optional)

Stored under:

~~~text
lineage/prov-template.json
lineage/ol-template.json
~~~

---

## 📡 7. Telemetry (OTel v11)

Integrated Gradients runs MUST emit:

- `kfm.expl_method="integrated-gradients"`  
- `kfm.expl_energy_wh`  
- `kfm.expl_carbon_gco2e`  
- `kfm.expl_latency_ms`  
- `kfm.expl_cells` (if spatial/H3)  
- `cpu_pct`, `gpu_pct`, `ram_mb`  

Telemetry MUST be attached to:

- STAC Item  
- OpenLineage event  
- Release-level telemetry bundle  

---

## 🎨 8. Rendering Guidelines

IG maps SHOULD support:

- **Signed attribution** (positive/negative influence)  
- Diverging colormap (cool → warm)  
- Per-cell normalization  
- Global vs local views  
- H3 multi-resolution mapping (R3–R9)  

Example uses:

- Climate model drivers  
- Smoke/PM2.5 sensitivity  
- Flood/soil moisture gradients  
- Terrain → risk explainability  

---

## 🔮 9. Story Node Integration (Focus Mode v3)

Each IG output SHOULD create a Story Node summarizing:

- What drove the prediction  
- Where the model concentrated sensitivity  
- How attribution changes across model versions  
- CARE compliance for sensitive areas  
- Energy/costs for explainability run  
- Provenance chain and dataset lineage  

Story Nodes power explainability-first narratives across KFM.

---

## 🧭 10. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.2.3 | 2025-11-29 | Initial v11 Integrated Gradients template; full metadata, lineage, and CARE compliance. |

---

<div align="center">

⚡ **Kansas Frontier Matrix — Integrated Gradients Template (v11.2.3)**  
Deep Learning Explainability · FAIR+CARE · Provenance-Rich · Sustainable AI  

[📘 Docs Root](../../../../../..) • [🧠 Explainability Templates](../README.md) • [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>