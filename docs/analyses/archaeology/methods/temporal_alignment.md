---
title: "⏳ Kansas Frontier Matrix — Archaeology Temporal Alignment (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/archaeology/methods/temporal_alignment.md"
version: "v11.0.0"
last_updated: "2025-11-25"
review_cycle: "Biannual · Archaeology Working Group · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/archaeology-methods-temporal-v11.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Method Specification"
intent: "archaeology-temporal-alignment"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
immutability_status: "version-pinned"
semantic_document_id: "kfm-arch-method-temporal-alignment-v11"
doc_uuid: "urn:kfm:docs:archaeology:methods:temporal_alignment:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# ⏳ **Kansas Frontier Matrix — Archaeology Temporal Alignment**  
`docs/analyses/archaeology/methods/temporal_alignment.md`

**Purpose:**  
Define FAIR+CARE-compliant **temporal alignment methods** for archaeological datasets within KFM, enabling cross-dataset chronological comparison, OWL-Time standardization, uncertainty modeling, time-series alignment, and integration with Focus Mode v3 and Story Node v3.

</div>

---

## 📘 Overview

Temporal alignment refers to harmonizing dates, time ranges, chronology systems, and uncertainty representations across archaeological sources, including:

- Radiocarbon (¹⁴C) dates  
- OSL dates  
- Dendrochronology (if present)  
- Stratigraphic relative sequences  
- Historical/ethnohistorical dates  
- Paleoenvironmental temporal ranges  
- Artifact-phase chronologies  
- Cultural period frameworks  

KFM temporal alignment ensures that:

- All dates map to **OWL-Time** compliant intervals  
- Uncertainty is preserved and never collapsed  
- No speculative precision is introduced  
- Indigenous and descendant community interpretations are respected  
- Chronologies support Story Node and Focus Mode semantic linking  

---

## 🗂 Directory Layout

```text
docs/
- analyses/
  - archaeology/
    - methods/
      - spatial_analysis.md
      - proximity_statistics.md
      - temporal_alignment.md
```

---

## 🧭 Temporal Alignment Principles

### 1️⃣ OWL-Time Standardization

KFM forces all temporal data into the OWL-Time model:

- `time:Instant`  
- `time:ProperInterval`  
- `time:hasBeginning` / `time:hasEnd`  
- `time:inXSDDateTime` or `time:inXSDgYear`  

All KFM datasets must provide **normalized** chronology fields, even if original data uses:

- BCE/CE  
- BP  
- Uncal ± error  
- Relative terms (e.g., “Late Woodland”)  

### 2️⃣ Chronology Translation

Translations preserve original phrasing:

| Original Input | KFM Representation |
|----------------|--------------------|
| “ca. 800–1200 CE” | Interval + `kfm:time_label` |
| “1050 ± 50 BP (uncal)” | Interval with symmetry + calibration metadata |
| “Late Archaic” | Lookup to cultural period thesaurus → interval + label |
| “Stratum III older than Stratum II” | Relative ordering → probabilistic interval ordering |

### 3️⃣ Uncertainty Preservation

Uncertainty is **never collapsed**. All temporal data must include:

- **Measurement uncertainty** (e.g., ± years for ¹⁴C)  
- **Calibration uncertainty**  
- **Cultural interpretive uncertainty**  
- **Narrative uncertainty** for Story Nodes  

Fields:

- `kfm:uncertainty_years`  
- `kfm:calibration_curve`  
- `kfm:confidence`  
- `kfm:time_precision`  
- `kfm:time_label`  

### 4️⃣ CARE Compliant Chronology

Temporal data must not:

- Override descendant community interpretations  
- Imply absolute precision on culturally sensitive histories  
- Frame Indigenous timelines in colonial-centric schemas without annotation  

---

## 🧩 Method Families

### 1️⃣ Radiocarbon Alignment (¹⁴C)

Procedure:

- Parse input (uncalibrated)  
- Apply calibration curve (IntCal, SHCal, etc.)  
- Convert to probability density function (PDF)  
- Collapse PDF to OWL-Time interval enveloping 68% or 95% confidence  
- Retain original `BP` and lab codes  

Metadata:

- `kfm:calibration_curve`  
- `kfm:lab_id`  
- `kfm:uncertainty_years`  
- `kfm:pdf_uri`  

### 2️⃣ OSL Alignment

OSL dates are expressed as:

- Central age  
- De (equivalent dose)  
- Error term  

KFM alignment:

- Convert to interval with symmetrical or asymmetrical uncertainty  
- Apply sediment-accumulation context notes  
- Link to stratigraphic unit via PROV-O  

### 3️⃣ Period & Phase Alignment

Cultural periods are mapped using the **KFM Cultural Chronology Thesaurus**:

- Great Bend Aspect  
- Plains Village  
- Central Plains Tradition  
- Late Woodland  
- etc.

These alignments generate:

- A canonical interval  
- `kfm:time_label` preserving original term  
- PROV-O links to the period source authority  

### 4️⃣ Stratigraphic Temporal Alignment

Relative chronology:

- “Layer 3 older than Layer 2” → constraints  
- Sequencing constraints resolve into **partial orders**  
- Compatible with Harris matrices  
- Temporal ordering feeds into depositional event Story Nodes  

### 5️⃣ Temporal Fusion (Cross-Dataset Alignment)

Used when combining:

- ¹⁴C sets  
- Periods  
- Stratigraphy  
- Documentary dates  
- Paleoenvironment datasets  

Algorithm:

- Normalize → translate → derive constraints → solve for global compatible interval set  
- Output: aligned intervals per entity with confidence metadata  

---

## 🧮 Example Temporal Alignment Block

```json
{
  "kfm:temporal_alignment": {
    "interval": {
      "start": "0800-01-01T00:00:00Z",
      "end": "1200-01-01T00:00:00Z"
    },
    "kfm:time_precision": "century",
    "kfm:time_label": "ca. 800–1200 CE",
    "kfm:uncertainty_years": 200,
    "kfm:confidence": 0.82,
    "prov:used": [
      "lab/rc-smokyhill-3451.json",
      "periods/central-plains-tradition.json"
    ],
    "care:sensitivity": "generalized"
  }
}
```

---

## 🔍 Focus Mode & Story Node Integration

### **Focus Mode v3**
Temporal alignment allows Focus Mode to:

- Infer correct time-window context  
- Merge multi-source chronologies  
- Highlight overlapping cultural periods  
- Provide timeline-adaptive narratives  
- Apply uncertainty bars in the UI  

### **Story Node v3**
Story Nodes use aligned temporal data for:

- `spacetime.when` interval  
- Relative event alignment  
- Cultural period classification  
- Multi-source chronology reconciliation  

No Story Node may:

- Misrepresent uncertainty  
- Collapse Indigenous chronological interpretations  

---

## 🔗 STAC, DCAT & PROV-O Integration

Every temporal alignment produces:

- A derived temporal dataset  
- A PROV-O activity bundle  
- A STAC `scientific` extension record  

Required fields:

- `kfm:method_name: "temporal_alignment_v11"`  
- `kfm:parameters` (calibration curve, period authority, etc.)  
- `prov:used`  
- `prov:wasGeneratedBy`  
- Checksums (SHA-256) for all outputs  

---

## 🧪 CI Validation Requirements

The following must pass:

- `archaeology-temporal-align-validate.yml`  
- CARE timeline audit  
- OWL-Time validator  
- FAIR metadata check  
- PROV-O lineage checker  
- KFM-MDP v11 Markdown linter  

---

## 🕰 Version History

| Version | Date | Author | Notes |
|---------|--------|-------------------------------|-------------------------------|
| v11.0.0 | 2025-11-25 | Archaeology Working Group · FAIR+CARE Council | Initial release of temporal alignment methods |

---

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE · MCP-DL v6.3 · STAC 1.0.0 · DCAT 3.0  

[⬅ Back to Archaeology Methods](../README.md) ·  
[📑 Metadata Standards](../../../standards/README.md) ·  
[📘 Master Guide v11](../../../reference/kfm_v11_master_documentation.md)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~markdown
