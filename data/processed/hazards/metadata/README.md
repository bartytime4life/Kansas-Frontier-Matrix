---
title: "⚠️ Kansas Frontier Matrix — Processed Hazards Metadata (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/processed/hazards/metadata/README.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-processed-hazards-metadata-v11.0.0"
semantic_document_id: "kfm-doc-data-processed-hazards-metadata-readme"
event_source_id: "ledger:data/processed/hazards/metadata/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/data-hazards-processed-metadata-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0 / FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Domain Metadata Registry"
intent: "processed-hazards-metadata"
role: "hazards-domain"
category: "Data · Hazards · Metadata · Processed"

fair_category: "F1-A1-I1-R1"
care_label: "Mixed — community-impacted hazards"
sensitivity_level: "Dataset-dependent"
indigenous_rights_flag: "Dataset-dependent"
redaction_required: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Medium–High (hazards affect people)"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/data-hazards-processed-metadata-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/data-hazards-processed-metadata-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified hazard claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Public / Mixed Sensitivity"
jurisdiction: "Kansas / United States"
lifecycle_stage: "stable"
ttl_policy: "Permanent"
sunset_policy: "Superseded upon next hazards-domain metadata update"
---

<div align="center">

# ⚠️ **Kansas Frontier Matrix — Processed Hazards Metadata**  
`data/processed/hazards/metadata/README.md`

Metadata governing:

- 🌪️ Tornado tracks & severe storms  
- 🌊 Flood risk zones (FEMA & derived)  
- 🔥 Wildfire perimeters & severity  
- 🌵 Drought severity indices  
- 🧩 Multi-hazard composites & intensity indices  
- 🧱 Exposure, vulnerability, and asset datasets  
- 🧠 Focus Mode v3 hazard narratives  
- 🌐 STAC/DCAT metadata & FAIR+CARE certification  

All metadata files are **schema-validated, checksum-verified, and governance-approved**.

</div>

---

## 1. 📘 Purpose

This directory stores **metadata artifacts** governing processed hazards datasets, including:

- Schema validation outputs  
- FAIR+CARE certification JSON  
- PROV-O lineage exports  
- Domain-level checksum manifests  
- Metadata completeness & QC reports  

These metadata ensure:

- Full traceability  
- Ethical usage of community-impacting hazard data  
- STAC/DCAT discoverability  
- Consistency with ISO 19115 lineage models  
- Compatibility with Neo4j hazard graph ingestion  

---

## 2. 🗂️ Directory Layout (GitHub-Safe)

```text
data/processed/hazards/metadata/
├── README.md                               ← this file
├── checksums.json                           ← SHA-256 checksums for all processed hazards datasets
├── provenance.json                          ← PROV-O lineage exports
├── schema_validation.json                   ← Schema contract validation results
├── faircare_certification.json              ← FAIR+CARE certification record
└── metadata_manifest.json                   ← Linked metadata catalog (DCAT/STAC)
```

---

## 3. 📑 Metadata Coverage

Hazards metadata covers:

- **Dataset identity**
  - Titles, descriptions, keywords  
  - STAC/DCAT fields  
  - KFM identifiers & semantic IDs  

- **Schema structure**
  - File-level schema compliance  
  - Field-level validation  
  - Geometry checks (GeoJSON/COORD/CRS)  

- **Ethical flags**
  - CARE-sensitive fields (fatalities, injuries, damages)  
  - Indigenous privacy constraints  
  - Aggregation requirements (H3 cells / census tracts)  

- **Quality & lineage**
  - Source data provenance  
  - ETL pipeline steps  
  - Data quality indicators (ISO 19157)  

- **Filesystem tracking**
  - Checksums (sha256)  
  - SBOM reference  
  - Manifest references  

---

## 4. 🔗 PROV-O Lineage Overview

Every processed hazards dataset is expressed as a `prov:Entity` with:

- `prov:wasDerivedFrom` → raw hazard datasets  
- `prov:used` → staging/intermediate artifacts  
- `prov:wasGeneratedBy` → hazards ETL pipeline processes  
- `prov:wasAttributedTo` → “KFM Data Council”  
- `prov:qualifiedGeneration` → pipeline configuration & environment  

The file `provenance.json` contains:

- Multi-step lineage  
- Responsible agents  
- Timestamped ETL events  
- Input/output resources  

---

## 5. ⚖️ FAIR+CARE Governance

Processed hazards datasets are **high-impact** and require:

### FAIR

- **Findable** — cataloged in STAC/DCAT  
- **Accessible** — public CC-BY 4.0  
- **Interoperable** — schema-aligned, typed fields  
- **Reusable** — full provenance & validation reports  

### CARE (critical for hazards)

- **Collective Benefit** — public safety & community planning  
- **Authority to Control** — Indigenous sovereignty policy applied  
- **Responsibility** — hazard impact context is mandatory  
- **Ethics** — no misuse (fear-based narratives, overprecision, etc.)  

`faircare_certification.json` records:

- Reviewer decisions  
- Redaction notes  
- Sensitive field restrictions  

---

## 6. 🧪 Schema Validation Summary

`schema_validation.json` contains:

- Field-level validation (types, ranges, enums)  
- Geometry validation via SHACL  
- CRS checks (EPSG:4326 required)  
- Temporal coverage validation (OWL-Time)  
- Data-contract compliance (KFM-PDC v11)  

Common checks:

- No null geometries  
- No invalid polygon rings  
- No out-of-range EF-scales, risk classes, drought values  
- CARE-sensitive columns must be flagged  

---

## 7. 🧮 Checksums & Metadata Manifest

`checksums.json` includes:

- SHA-256 for every processed hazards asset  
- Provenance references  
- Timestamp of checksum generation  
- Link to `metadata_manifest.json`  

`metadata_manifest.json`:

- STAC-aligned metadata index  
- DCAT Dataset + Distribution records  
- Pointers to schemas, provenance, FAIRCARE certification  

---

## 8. 🖥️ Focus Mode Integration

Focus Mode v3 uses metadata for:

- Hazard location summaries  
- Timeline context (e.g., storm outbreaks by period)  
- Risk explanation layers  
- Multi-hazard narrative overlays  

Metadata here ensures Focus Mode:

- Does not surface CARE-sensitive fields without redaction  
- Avoids harmful or misleading interpretations  
- Applies correct uncertainty and provenance indicators  

---

## 9. 🕰️ Version History

| Version | Date       | Summary                                                 |
|--------:|------------|---------------------------------------------------------|
| v11.0.0 | 2025-11-20 | Initial metadata registry using preferred formatting     |
| v10.0.0 | 2025-11-10 | Preliminary metadata added to hazards processing domain |

<div align="center">

**Kansas Frontier Matrix — Hazards Domain Metadata**  
⚠️ FAIR+CARE Certified · Integrity-Verified · Diamond⁹ Ω / Crown∞Ω  

© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Hazards](../README.md) · [Data Architecture](../../ARCHITECTURE.md) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>