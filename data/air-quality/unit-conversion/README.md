---
title: "🌡️ KFM — Air-Quality Unit Conversion (ppb ↔ µg/m³) · Temperature-Pressure Dependent"
path: "docs/data/air-quality/unit-conversion/README.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & Atmospheric Science WG"
content_stability: "stable"

doc_kind: "Technical Guide"
status: "Active"
intent: "air-quality-unit-conversion"
semantic_document_id: "kfm-doc-air-quality-unit-conversion-v11.2.6"

license: "CC-BY 4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

header_profile: "standard"
footer_profile: "standard"
---

# 🌡️ Air-Quality Unit Conversion — ppb ↔ µg/m³  
Temperature- & Pressure-Sensitive Gas-Phase Conversions

Most atmospheric gases **cannot** be converted between ppb and µg/m³ with a single static factor.  
The conversion depends on **temperature (T)** and **pressure (P)** via the ideal-gas law.  
This guide establishes the official KFM method for deterministic, reproducible conversions.

---

## 🗂️ Directory Layout

~~~text
docs/
└── 📁 data/
    └── 📁 air-quality/
        ├── 📄 README.md
        └── 📁 unit-conversion/
            ├── 📄 README.md                  # 🌡️ This file
            ├── 📁 samples/
            │   └── 📄 example-calculations.md
            └── 📁 schemas/
                └── 📄 unit-conversion-spec-v11.json

src/
└── 📁 data/
    └── 📁 air_quality/
        └── 📄 unit_conversion.py             # Reference implementation (ppb ↔ µg/m³)

configs/
└── 📁 data/
    └── 📁 air_quality/
        └── 📄 unit-conversion-v11.yaml       # Config for which gases, MW values, T/P sources

data/
└── 📁 processed/
    └── 📁 air_quality/
        └── 📄 harmonized-concentrations.parquet  # Converted & harmonized outputs

mcp/
└── 📁 experiments/
    └── 📁 air_quality/
        └── 📄 unit-conversion-log.jsonl      # Deterministic conversion logs + PROV references
~~~

---

## 📘 Overview

Air-quality sources within KFM (OpenAQ, AirNow, CAMS NRT, PurpleAir, internal AQ sensors, etc.) frequently mix:

- **mass concentrations** (µg/m³) and  
- **mixing ratios** (ppb)

Because KFM performs **cross-source harmonization**, all conversions must be:

- **explicit** (T, P, molecular weight documented)
- **deterministic & reproducible** (config-driven, not ad hoc)
- **reversible** (inverse conversion available)
- **provenance-tracked** (fully described via PROV-O)

This document defines the **canonical formula**, **metadata requirements**, and **integration points** in the KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → Story Nodes / Focus Mode.

---

## 🧮 Canonical Formula (Ideal-Gas Based)

### ppb → µg/m³

$begin:math:display$
\mu\text{g m}^{-3}
=
\text{ppb}
\times
\frac{
\text{MW}\;(\text{g mol}^{-1}) \times P
}{
R \times T
}
\times 10^{3}
$end:math:display$

Where:

- **MW** — molecular weight (g·mol⁻¹)  
- **P** — pressure (Pa)  
- **T** — temperature (K)  
- **R** — 8.314 462 618 J·mol⁻¹·K⁻¹  

### µg/m³ → ppb (inverse)

$begin:math:display$
\text{ppb}
=
\mu\text{g m}^{-3}
\times
\frac{
R \times T
}{
\text{MW} \times P
}
\times 10^{-3}
$end:math:display$

These formulas are the **only** ones KFM uses internally for gas-phase ppb ↔ µg/m³ conversions.

---

## 🌡️ Why Conversion Factors Differ

Regulatory and scientific agencies publish approximate conversion factors at **fixed reference conditions**.

Example factors:

| Gas | MW (g/mol) | 20 °C / 1013 mb             | 25 °C / 1 atm              |
|-----|------------|-----------------------------|----------------------------|
| NO₂ | 46.0055    | 1 ppb ≈ 1.9125 µg/m³        | 1 ppb ≈ 1.88 µg/m³         |
| O₃  | 48.00      | 1 ppb ≈ 1.9957 µg/m³        | 1 ppb ≈ 1.96 µg/m³         |

These differences arise **entirely** from the chosen T/P constants.  
Therefore **KFM never uses static tables internally**—only explicit, T/P-aware formulas recorded in metadata.

---

## 🧩 KFM Best Practices

### 1️⃣ Store native units from source systems

- Do **not** convert raw values during ingestion.
- Keep the original:
  - unit (e.g., `"ppb"` or `"µg/m³"`)
  - temperature & pressure context when provided

### 2️⃣ Always record the conversion context

For any conversion run, KFM must record at minimum:

- **temperature** (°C or K; stored as K in schemas)  
- **pressure** (mb or Pa; stored as Pa in schemas)  
- **molecular weight (MW)** for the gas  
- **reference conditions** if using a specific agency standard (e.g., `"DEFRA 20 °C, 1013 mb"`)

These are stored in:

- ETL config (`unit-conversion-v11.yaml`)  
- per-run logs (`mcp/experiments/.../unit-conversion-log.jsonl`)  
- PROV bundles (see below)

### 3️⃣ Perform conversions after ingestion

Conversions should occur:

- **after ingestion**, in deterministic ETL or analysis steps  
- **before visualization / cross-source blending**

This allows:

- reproducible re-runs with updated T/P or MW values  
- alternative scenarios (e.g., re-running at different reference conditions)

### 4️⃣ Provide explicit reversibility

Every conversion pipeline must:

- implement both **forward** (ppb → µg/m³) and **inverse** (µg/m³ → ppb) formulas  
- record the direction and parameters in PROV-O so that the transformation is auditable and reversible

---

## 🔗 Integration With STAC / DCAT / PROV

### STAC

For STAC Collections / Items that contain converted gas-phase concentrations, KFM SHOULD use:

- `properties.kfm:unit_conversion_method` — e.g., `"ideal-gas-ppb-ugm3-v11"`  
- `properties.kfm:temperature_reference` — e.g., `298.15` (K)  
- `properties.kfm:pressure_reference` — e.g., `101325` (Pa)  
- `properties.kfm:conversion_formula_ref` — URI or identifier of this guide or schema entry  

Example (Item properties):

~~~json
{
  "datetime": "2025-12-10T00:00:00Z",
  "kfm:unit_conversion_method": "ideal-gas-ppb-ugm3-v11",
  "kfm:temperature_reference": 298.15,
  "kfm:pressure_reference": 101325,
  "kfm:conversion_formula_ref": "kfm-doc-air-quality-unit-conversion-v11.2.6#ideal-gas"
}
~~~

### DCAT

DCAT Datasets representing converted air-quality products SHOULD include:

- `kfm:unit_conversion_method` — as above  
- `kfm:conversion_formula_ref` — link to this document  
- `prov:wasDerivedFrom` — identifiers for original datasets in native units  

These fields live in `data/catalogs/**` DCAT JSON-LD.

### PROV-O

For each converted field, PROV bundles must express:

- `prov:Entity` — original concentration and converted concentration  
- `prov:Activity` — conversion step / pipeline run  
- `prov:Agent` — ETL service or analyst (as appropriate)  

Key relations:

- `converted_entity prov:wasDerivedFrom original_entity`  
- `conversion_activity prov:used original_entity`  
- `conversion_activity prov:generated converted_entity`  
- `conversion_activity prov:used` parameters:
  - temperature, pressure, molecular weight  
  - formula reference, config hash  

This ensures deterministic lineage and full reproducibility.

---

## 🧪 Example Calculation (NO₂ at 25 °C, 1 atm)

For **1 ppb NO₂**:

- MW = 46.0055 g/mol  
- T = 298.15 K  
- P = 101325 Pa  

$begin:math:display$
\mu\text{g m}^{-3}
=
1 \times
\frac{
46.0055 \times 101325
}{
8.314462618 \times 298.15
}
\times 10^{3}
\approx
1.88 \;\mu\text{g m}^{-3}
$end:math:display$

This example SHOULD appear in:

- `docs/data/air-quality/unit-conversion/samples/example-calculations.md`  
- automated test cases in `src/data/air_quality/unit_conversion.py`  

so that CI can assert correctness of future changes.

---

## 🧪 CI & Validation

Conversion logic is validated via:

- **Unit tests**
  - reuse known reference factors (e.g., NO₂, O₃ at standard conditions)  
  - compare pipeline output to computed values within a small tolerance

- **Schema validation**
  - `unit-conversion-spec-v11.json` applied to:
    - ETL configs  
    - harmonized concentration tables

- **Determinism checks**
  - fixed inputs (raw concentration, T, P, MW) must always yield the same converted value  
  - logs in `mcp/experiments/.../unit-conversion-log.jsonl` must be reproducible

Changes to conversion formulas or MW tables **must** go through Atmospheric Science WG review.

---

## 📎 Provenance Requirements

Every conversion must emit PROV-O statements:

- `prov:wasDerivedFrom` → original concentration entity  
- `prov:valueConversion` (or equivalent custom property) → formula reference and implementation ID  
- `prov:used` → temperature & pressure metadata, molecular weight, and config version  
- `prov:generatedAtTime` → conversion timestamp  
- `prov:wasAssociatedWith` → ETL pipeline / operator identity  

PROV bundles for air-quality conversions SHOULD live under:

- `mcp/experiments/air_quality/unit-conversion-prov.jsonld`

and be referenced from STAC/DCAT metadata where appropriate.

---

## 🧭 Version History

| Version  | Date       | Notes                                                                 |
|----------|------------|-----------------------------------------------------------------------|
| v11.2.6  | 2025-12-10 | Initial KFM-aligned unit conversion guide for gas-phase ppb ↔ µg/m³. |

---

### ⚖ FAIR+CARE & Governance Footer

This document:

- complies with **KFM-MDP v11.2.6**, **KFM-STAC v11**, **KFM-DCAT v11**, and **KFM-PROV v11**  
- is governed by the **FAIR+CARE Council** and **Atmospheric Science Working Group**, with co-review by the Governance Council  
- must be updated when conversion formulas, MW tables, or metadata conventions are materially changed

Edits require approval from the FAIR+CARE Council and Atmospheric Science WG and must pass
`markdown-lint`, `schema-lint`, `footer-check`, and unit-conversion validation tests in CI.

<br/>

<sub>© Kansas Frontier Matrix · CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

🌡️ **Kansas Frontier Matrix — Air-Quality Unit Conversion (ppb ↔ µg/m³) v11.2.6**  
Deterministic Conversions · Atmospheric Science Aligned · FAIR+CARE Governance  

[📘 Docs Root](../../../README.md) · [📊 Data Docs Index](../../README.md) · [🌫 Air-Quality Index](../README.md) · [⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>