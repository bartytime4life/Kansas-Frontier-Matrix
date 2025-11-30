---
title: "🌍 Sentinel-1 InSAR — Unwrapped Phase (Continuous Phase Surfaces for LOS Deformation)"
path: "docs/data/satellites/sentinel-1/transforms/deformation/unwrapped/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (High-Sensitivity InSAR Intermediate)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · FAIR+CARE Council + Remote Sensing WG"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-deformation-unwrapped-v11.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F4-A2-I3-R5"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "High"
risk_category: "Very High"
public_exposure_risk: "High"
redaction_required: true

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "Interval"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-unwrapped-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-unwrapped-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-deformation-unwrapped:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-deformation-unwrapped"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/deformation/unwrapped/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded by next ESA unwrapping algorithm revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌍 **Sentinel-1 InSAR — Unwrapped Phase Directory**  
`docs/data/satellites/sentinel-1/transforms/deformation/unwrapped/`

Continuous unwrapped phase surfaces derived from wrapped interferograms,  
used for **LOS displacement** modeling under KFM’s deformation ETL pipeline.

</div>

---

## 🗂️ 1. Directory Layout (STRICT OPTION-A EMOJI STYLE)

~~~text
docs/data/satellites/sentinel-1/transforms/deformation/unwrapped/
├── 📄 README.md
│
├── 🌍 unwrapped_20250101_20250113.tif     # Unwrapped phase from IFG pair 01–13 Jan 2025
├── 🌍 unwrapped_20250314_20250326.tif     # Unwrapped phase from IFG pair 14–26 Mar 2025
└── 🌍 unwrapped_20250620_20250702.tif     # Additional unwrapped phase tiles
~~~

✔ Emoji BEFORE filenames  
✔ No drift  
✔ Matches interferograms/, los/, tests/, fixtures/ patterns  
✔ Box-safe  

---

## 📘 2. Purpose

Unwrapped phase rasters represent **continuous phase** values extracted from  
wrapped interferograms and form the main intermediate product for:

- converting phase → **LOS displacement**  
- deformation Story Nodes and hazard analysis  
- hydrology deformation cross-checking  
- infrastructure stability layer preparation  
- sovereignty-governed masking operations during LOS stage  

Unwrapped rasters themselves are **not released** publicly due to sensitivity.

---

## 🧩 3. How Unwrapped Phase Is Produced

### 1️⃣ Input Interferograms  
Provided by:

```
transforms/deformation/interferograms/
```

### 2️⃣ Residue Detection  
- identifies phase discontinuities  
- maps residues for branch-cut algorithm

### 3️⃣ Branch-Cut Phase Unwrapping  
- resolves modulo-2π ambiguities  
- creates continuous phase surface  
- ensures phase consistency across overlaps

### 4️⃣ Masking & Quality Control  
- removes incoherent regions  
- applies coherence-based weights  
- discards unusable low-SNR regions  

### 5️⃣ Output: Unwrapped Tiles  
Saved into this directory.

---

## 🔗 4. PROV-O Lineage

Each unwrapped phase raster is a **prov:Entity**, e.g.:

~~~json
{
  "prov:Entity": "s1_unwrapped_20250101_20250113",
  "prov:used": [
    "ifg_20250101_20250113",
    "orbit_metadata",
    "dem"
  ],
  "prov:wasGeneratedBy": "s1_phase_unwrapping",
  "kfm:care_label": "CARE-B",
  "kfm:h3_sensitive": true
}
~~~

All lineage is forwarded to the **LOS stage**, where sovereignty rules are applied.

---

## 🔐 5. FAIR+CARE & Sovereignty Handling

Unwrapped phase signals can reveal:

- subsidence  
- uplift  
- infrastructure strain  
- culturally sensitive motion patterns  

Thus:

- **CARE-B mandatory**  
- `"kfm:h3_sensitive" = true`  
- `"kfm:mask_required" = true` propagated to LOS stage  
- NO unmasked unwrapped rasters are released  
- sovereignty generalization occurs **after LOS conversion**,  
  but flags **must** propagate at unwrapped stage

---

## 🧪 6. CI Validation Requirements

CI checks:

- unwrapped phase continuity  
- absence of uncorrected wraps  
- correct residue/branch-cut behavior  
- matching reference fixtures  
- deterministic results across platforms  
- correct `"kfm:*"` metadata propagation  
- schema + SHACL compliance  

Failures → ETL blocked.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, non-drifting unwrapped-phase README; emoji prefixes validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🌍 Interferograms](../interferograms/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

