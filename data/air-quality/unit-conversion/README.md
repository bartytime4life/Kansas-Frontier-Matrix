---
title: "🔁 KFM — Air Quality Unit Conversion (Profiles · Schemas · Reference)"
path: "data/air-quality/unit-conversion/README.md"

version: "v11.2.6"
last_updated: "2025-12-17"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Data Architecture Board · FAIR+CARE Oversight"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "Directory README"
header_profile: "standard"
footer_profile: "standard"
intent: "air-quality-unit-conversion"

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
    - "data/air-quality/unit-conversion/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; formulas & lookup tables)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by KFM v12 (or later) air-quality unit-conversion specification"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

json_schema_ref: "../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"

immutability_status: "mutable-living-doc"
doc_uuid: "urn:kfm:doc:data:air-quality:unit-conversion:readme:v11.2.6"
semantic_document_id: "kfm-air-quality-unit-conversion-readme"
event_source_id: "ledger:kfm:doc:data:air-quality:unit-conversion:readme:v11.2.6"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "data/air-quality/unit-conversion/README.md@v11.2.6"
---

<div align="center">

# 🔁 **KFM — Air Quality Unit Conversion**
`data/air-quality/unit-conversion/README.md`

**Purpose**  
Provide **canonical, versioned unit-conversion profiles** used by KFM air-quality ETL and metadata production (e.g., ppm/ppb ↔ µg/m³, AQI breakpoint rules), with **deterministic behavior** and **auditable provenance**.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Domain-Air%20Quality-brightgreen" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Canonical-brightgreen" />

</div>

---

## 📘 Overview

This folder contains **unit-conversion “profiles”** and related documentation used to **standardize air‑quality measurement units** across KFM.

This is a **data dependency** (reference material), not an ETL output:
- It **does not** store raw sensor readings or processed datasets.
- It **does** store conversion rules and parameters that ETL jobs can apply consistently.

### What belongs here

- **Conversion profiles** (JSON/YAML): versioned, deterministic conversion definitions
- **Schemas**: local validation schemas for those profiles (JSON Schema)
- **Examples/fixtures**: small, stable samples for correctness testing and round‑trip checks
- **Documentation**: assumptions, sources, and governance notes

### What does not belong here

- Runtime logs, secrets, credential files
- Large datasets (raw or processed)
- Code modules that belong under `src/` (this directory can be consumed by code, but not house code as the primary artifact)

---

## 🗂️ Directory Layout

~~~text
📁 data/air-quality/unit-conversion/
├── 📄 README.md                                   — This file (what this folder is + how to use it)
├── 📁 profiles/                                   — Versioned conversion profiles (JSON/YAML)
│   ├── 🧾 aqi_breakpoints_us_epa_v1.json           — Example: AQI breakpoint rules (profile)
│   ├── 🧾 gas_molecular_weights_v1.json            — Example: MW lookup for ppm/ppb conversions
│   └── 🧾 concentration_conversions_v1.json        — Example: unit conversion recipes (generic)
├── 📁 schemas/                                    — Validation schemas for profiles in /profiles
│   ├── 🧾 unit-conversion-profile.schema.json      — Schema for a single profile
│   └── 🧾 unit-conversion-bundle.schema.json       — Schema for bundles/collections of profiles
└── 📁 examples/                                   — Small examples + roundtrip fixtures (optional)
    ├── 🧾 example_inputs.json                      — Example concentrations + conditions
    └── 🧾 example_expected_outputs.json            — Expected normalized outputs
~~~

**Rule:** if a change affects conversion behavior, it must be expressed as a **profile change** (and validated), not as an undocumented implicit assumption inside ETL code.

---

## 🧭 Context

Unit conversion sits in the pipeline as a **normalization step**:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI/Story Nodes/Focus Mode

Typical air‑quality workflows require consistent units because sources vary (e.g., mixing ratio vs. mass concentration, different averaging periods). This folder provides:
- a governed place to declare **assumptions** (temperature, pressure, molecular weight),
- a deterministic reference for ETL,
- and traceable metadata hooks (STAC/DCAT/PROV) to record “what conversion rules were used”.

---

## 📦 Data & Metadata

### Conversion profile concept

A **conversion profile** is a machine‑readable object that defines:
- **what** is being converted (pollutant / quantity),
- **from_unit** and **to_unit** (explicit strings; prefer a consistent unit system),
- **required parameters** (e.g., temperature_K, pressure_kPa, molecular_weight_g_mol),
- **defaults** (only when governance allows a default),
- **validity constraints** (ranges, supported pollutants),
- **source references** (where the rule/breakpoints came from),
- **profile versioning** and identifiers.

### Minimal recommended profile shape

~~~json
{
  "profile_id": "kfm:air-quality:unit-conversion:concentration:ideal-gas:v1",
  "version": "v1",
  "title": "Ideal gas conversion: ppb ↔ µg/m³",
  "quantity_kind": "concentration",
  "from_unit": "ppb",
  "to_unit": "ug/m3",
  "parameters": {
    "molecular_weight_g_mol": { "required": true },
    "temperature_K": { "required": true },
    "pressure_kPa": { "required": true }
  },
  "defaults": {
    "temperature_K": null,
    "pressure_kPa": null
  },
  "constraints": {
    "temperature_K": { "min": 150, "max": 350 },
    "pressure_kPa": { "min": 70, "max": 110 }
  },
  "source": {
    "authority": "TBD (insert authoritative spec or publication)",
    "retrieved_at": "YYYY-MM-DD",
    "citation": "TBD"
  },
  "notes": [
    "Do not apply a default T/P unless explicitly governed and documented."
  ]
}
~~~

**Important:** conversions that depend on environmental conditions (T/P) must not silently assume “standard conditions” unless the profile explicitly declares a governed default and its provenance.

### AQI breakpoint profiles

If KFM computes AQI from pollutant concentration, store breakpoint logic as a profile (breakpoints + formula). Keep:
- pollutant name + averaging period,
- breakpoints (concentration ranges ↔ index ranges),
- rounding rules,
- provenance/source authority and version.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

Conversion profiles can be referenced from STAC Items that represent air-quality products. A common pattern is:
- keep the profile file in this directory,
- include it as a STAC **asset** on the Item that used it,
- record the profile identifier and version in Item properties.

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "kfm-air-quality-<dataset-id>",
  "geometry": null,
  "bbox": null,
  "properties": {
    "datetime": "2025-12-17T00:00:00Z",
    "kfm:unit_conversion": {
      "profile_id": "kfm:air-quality:unit-conversion:concentration:ideal-gas:v1",
      "profile_version": "v1"
    }
  },
  "assets": {
    "unit-conversion-profile": {
      "href": "data/air-quality/unit-conversion/profiles/concentration_conversions_v1.json",
      "type": "application/json",
      "roles": ["metadata"]
    }
  }
}
~~~

If `kfm:unit_conversion` is not yet an approved property in the repo’s STAC profile, treat it as **proposed** and route through schema/ontology review before enforcing.

### DCAT

In DCAT, conversion profiles can be modeled as:
- a small `dcat:Dataset` (the conversion profile set),
- with one or more `dcat:Distribution` objects (each profile file).

The “used profile” relationship for a produced dataset should be represented through PROV (below) and/or through documented dataset metadata fields.

### PROV‑O

For reproducibility, ETL runs should record they **used** a conversion profile entity (and optionally generated a normalized dataset).

~~~json
{
  "@context": "https://openprovenance.org/prov-jsonld/context.jsonld",
  "@graph": [
    {
      "@id": "urn:kfm:prov:activity:air-quality:etl:<run-id>",
      "@type": "prov:Activity",
      "prov:used": [
        "urn:kfm:prov:entity:air-quality:unit-conversion:concentration:ideal-gas:v1"
      ]
    }
  ]
}
~~~

---

## 🧪 Validation & CI/CD

Minimum expectations for anything added/changed here:

- **Schema validation** for every profile file in `profiles/`
- **Determinism check**: repeated application of the same profile to the same inputs yields identical outputs
- **No silent defaults**: where parameters are required (T/P/MW), the absence must be a hard failure unless governance explicitly permits defaults

Suggested checks (examples; wire to your repo’s validators as applicable):

~~~bash
# Validate profile JSON against schema
python -m jsonschema -i data/air-quality/unit-conversion/profiles/concentration_conversions_v1.json \
  data/air-quality/unit-conversion/schemas/unit-conversion-profile.schema.json
~~~

Security posture:
- No secrets in this folder
- No PII
- No precise sensitive locations (generally not applicable to conversion profiles, but still subject to scanning rules)

---

## ⚖ FAIR+CARE & Governance

This folder is low‑risk by default (formulas and lookup tables), but governance still applies because conversion choices can materially change interpretation.

Governance requirements:
- Every profile must include a **source authority reference** and **retrieval date**
- Any change that affects conversion outputs is a **governed change** (reviewed; versioned)
- Where conversion assumptions could bias interpretation (e.g., default conditions), the defaults must be explicitly justified and approved

Binding references:
- Governance Charter: `../../../docs/standards/governance/ROOT-GOVERNANCE.md`
- FAIR+CARE Guide: `../../../docs/standards/faircare/FAIRCARE-GUIDE.md`
- Indigenous Data Protection: `../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-17 | Created/normalized directory README for air-quality unit-conversion profiles; aligned with KFM‑MDP v11.2.6 (front matter, heading registry, directory layout, governance footer). |

---

<div align="center">

**✅ Status:** Active / Canonical (Air Quality Data Reference)

**Navigation**  
[📂 Data Domain Root](../README.md) ·
[📁 Air Quality STAC](../stac/README.md) ·
[⚖ Governance (Air Quality)](../governance/README.md)

**Standards**  
[📘 Standards Index](../../../docs/standards/README.md) ·
[🏛️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6

</div>