---
title: "📁 Sentinel-1 InSAR — Deformation Fixtures (IFG · Unwrapped Phase · LOS Generalized)"
path: "docs/data/satellites/sentinel-1/transforms/deformation/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "High-Sensitivity Test Fixtures (CARE-B)"
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
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

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
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "Interval"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../schemas/json/sentinel1-deformation-fixtures-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-deformation-fixtures-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-deformation-fixtures:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-deformation-fixtures"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/deformation/fixtures/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded after next ESA deformation reprocessing epoch"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 InSAR — Deformation Fixture Library**  
`docs/data/satellites/sentinel-1/transforms/deformation/fixtures/`

Reference input/output products used for **InSAR deformation ETL tests**,  
including wrapped interferograms, unwrapped phase, and sovereignty-generalized  
LOS displacement rasters.

</div>

---

## 🗂️ 1. Directory Layout (Strict Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/deformation/fixtures/
├── 📄 README.md
│
├── 🛰️ SAFE_annotation_subset.xml         # Reduced SAFE annotation for deformation tests
├── 🌍 ifg_reference.tif                  # Reference wrapped interferogram
├── 🌍 unwrapped_reference.tif            # Reference unwrapped phase surface
└── 🌍 los_reference_generalized.tif      # Reference sovereignty-generalized LOS displacement
~~~

✔ Emoji prefix BEFORE filenames  
✔ Same structure as rtc/fixtures, coherence/fixtures, radiometric/fixtures  
✔ Box-safe, single fenced block  
✔ Strict, non-drifting, consistent

---

## 📘 2. Purpose

These fixtures support deterministic testing of the deformation ETL pipeline:

- **Interferogram generation**
- **Phase unwrapping**
- **LOS displacement projection**
- **Sovereignty generalization enforcement**
- **Governance metadata propagation**

The deformation pipeline is the **most sensitive component** of the Sentinel-1 ingestion chain,  
and these fixtures ensure stable, reproducible, governed outputs.

---

## 🧩 3. Fixture Descriptions

### 🛰️ `SAFE_annotation_subset.xml`
A reduced ESA SAFE annotation containing:

- orbit & geometry metadata  
- Doppler coefficients  
- IW burst timing  
- incidence angle  
- pixel/line mapping  
- slant-range parameters  

Used for:

- IFG creation tests  
- unwrapping geometry consistency  
- incidence-angle alignment with DEM tiles  

---

### 🌍 `ifg_reference.tif`
Reference **wrapped interferogram** used to validate:

- complex multiply operations  
- wrapped phase range (–π to +π)  
- burst-aligned geometry  
- bit-exact reproducibility  

---

### 🌍 `unwrapped_reference.tif`
Reference **continuous unwrapped phase** surface.

Used to validate:

- branch-cut unwrapping  
- residue detection  
- stable continuous phase values  
- no discontinuities or rewrap artifacts  

---

### 🌍 `los_reference_generalized.tif`
Reference **sovereignty-generalized LOS displacement** raster.

Used to validate:

- correct LOS projection math  
- H3 generalization  
- uncertainty flooring  
- spatial smoothing in sovereign cells  
- `"kfm:*"` governance metadata expectations  

This file is **MANDATORY** for verifying that LOS generalization logic does not leak  
sensitive ground motion patterns.

---

## 🔗 4. PROV-O Lineage

Fixture lineage is recorded to maintain reproducible test states:

~~~json
{
  "prov:Entity": "s1_deformation_fixture",
  "prov:label": "Deformation Test Fixture",
  "kfm:care_label": "CARE-B",
  "kfm:provenance_type": "test-fixture"
}
~~~

---

## 🔐 5. FAIR+CARE & Sovereignty Handling

Because deformation outputs inherently reveal:

- subsidence  
- uplift  
- ground motion tied to tribal lands  
- cultural-landscape sensitivity  

Fixtures must enforce:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true`  
- `"kfm:mask_required" = true`  

Although fixtures do not contain raw sovereign coordinates,  
LOS displacement rasters encode potentially sensitive patterns → **always governed**.

---

## 🧪 6. CI Integration

CI validates:

- IFG, unwrapping, LOS reference matching  
- deterministic deformation pipeline behavior  
- `"kfm:*"` metadata propagation  
- H3 sovereignty generalization correctness  
- schema + SHACL compliance  
- reproducibility across platforms  

If any mismatch occurs → **ETL pipeline is blocked** until corrected.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, non-drifting deformation fixture README; emojis validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Tests](../tests/README.md) · [🌍 LOS Outputs](../los/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

