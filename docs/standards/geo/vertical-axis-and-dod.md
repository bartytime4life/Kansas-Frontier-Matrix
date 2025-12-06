---
title: "📐 KFM v11 — Vertical Datums, CF Z-Axis, and DoD Sign Convention Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/geo/vertical-axis-and-dod.md"

version: "v11.0.1"
last_updated: "2025-11-22"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Semiannual · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Standard"
semantic_document_id: "kfm-vaxis-dod-v11"
doc_uuid: "urn:kfm:docs:standards:vertical-axis-dod:v11"
event_source_id: "ledger:kfm:doc:standards:geo:vertical-axis-dod:v11"
immutability_status: "version-pinned"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-vertical-axis-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "vertical-axis-and-dod"
  applies_to:
    - "dem"
    - "bathymetry"
    - "hydrology"
    - "sediment"
    - "lidar"
    - "DoD"
    - "etl"
    - "stac"
    - "dcat"
    - "graph"
    - "api"
    - "frontend"
    - "story-nodes"
    - "focus-mode"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity: "General (non-sensitive; vertical semantics only)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public (Governed)"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by next vertical-axis/DoD standard revision"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

json_schema_ref: "../../../schemas/json/vertical-axis-and-dod-v11.0.1.schema.json"
shape_schema_ref: "../../../schemas/shacl/vertical-axis-and-dod-v11.0.1-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "governance-override"
  - "narrative-fabrication"

transform_registry:
  allowed:
    - summary
    - semantic-highlighting
    - diagram-extraction
    - metadata-extraction
  prohibited:
    - content-alteration
    - speculative-additions
    - governance-override
    - narrative-fabrication

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

heading_registry:
  approved_h2:
    - "🗂️ Directory Layout"
    - "📘 Overview"
    - "🧭 Context"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"
---

<div align="center">

# 📐 **KFM v11 — Vertical Datums, CF Z-Axis, and DoD Sign Convention Standard**  
`docs/standards/geo/vertical-axis-and-dod.md`  
### **Diamond⁹ Ω / Crown∞Ω Ultimate Certified**

**Purpose**  
Define strict, machine‑verifiable vertical metadata rules for all KFM v11 datasets, ensuring correct elevation/depth semantics, reproducible DEM/DoD workflows, and UI/API alignment across MapLibre/Cesium, ETL, and STAC/DCAT.  
This standard is the **authoritative vertical reference** for DEMs, bathymetry, hydrology, sediment, and change detection in KFM.

</div>

---

## 🗂️ Directory Layout

```text
📂 docs/
└── 📂 standards/
    ├── 📂 geo/
    │   📄 README.md                  # 🌎 Geo Standards Index
    │   📄 crs-standard.md            # 🗺 CRS standard
    │   📄 vertical-axis-and-dod.md   # 📐 Vertical datums, CF Z-axis, DoD sign (this file)
    │   📄 stac-geo-spec.md           # 🛰 STAC geospatial metadata spec
    │   📄 tiling-and-pyramids.md     # 🧱 Raster tiling & pyramid standard
    │   📄 hydrology-standards.md     # 💧 Hydrology & water-surface (legacy v11 baseline)
    │   📄 soil-source-comparison.md  # 🌱 Soil source & provenance
    │   📄 archaeology-sensitive-locations.md  # 🛡 Archaeology & Indigenous sensitive locations (legacy path)
    └── 📂 governance/
        📄 ROOT-GOVERNANCE.md         # ⚖ Root governance charter
```

Author rules:

- This document defines vertical semantics for **all** KFM spatial standards.  
- CRS, STAC, tiling, hydrology, and archaeology standards must not contradict these vertical rules.  
- Any change to datum, CF Z‑axis, or DoD sign conventions must be reflected here and in dependent docs.

---

## 📘 Overview

This standard governs every KFM dataset with vertical meaning:

- DEMs and terrain surfaces.  
- Bathymetry and depth grids.  
- Lidar‑derived rasters.  
- Hydrology and water‑surface elevation models.  
- Sediment and bed‑change models.  
- DEM‑of‑Difference (DoD) products.  

Incorrect or missing vertical metadata causes inverted surfaces, wrong DoD magnitudes, broken 3D visualization, and misinterpretation in analyses and Story Nodes. KFM v11 enforces:

- **Deterministic vertical metadata** across ETL, STAC, API, and UI.  
- **Consistent sign conventions** so erosion vs deposition is unambiguous.  
- **Explicit datum and geoid declarations** so heights can be compared and transformed safely.

If vertical metadata is incomplete or inconsistent, the dataset is **not eligible** for publication in KFM catalogs or for use in Focus Mode.

---

## 🧭 Context

This standard is tightly coupled to:

- **CRS Standard (`crs-standard.md`)**  
  - XY and Z must be handled in compatible CRSs; XY reprojection must not silently alter vertical reference.  

- **Hydrology & Water Surface Standards (`hydrology-standards.md`)**  
  - Water surfaces, bathymetry, and hydraulic models rely on these vertical rules.  

- **STAC Geospatial Metadata Spec (`stac-geo-spec.md`)**  
  - `vertical:*`, `kfm:cf_positive`, and `kfm:dod_sign` fields encode these semantics into catalogs.  

- **Tiling & Pyramids Standard (`tiling-and-pyramids.md`)**  
  - 3D exaggeration and height rendering in WebMercator tiles depend on correct vertical metadata.  

- **Archaeology & Sensitive Locations Standard**  
  - Change detection near sensitive sites must use correct DoD sign conventions to avoid misinterpretation.

In the KFM pipeline:

> Vertical‑aware ETL → Vertical‑aware STAC/DCAT/PROV → Graph nodes with Z semantics → APIs → MapLibre/Cesium → Story Nodes & Focus Mode

this document defines **what “up” and “down” mean** and how change is encoded.

---

## 📦 Data & Metadata

### 1️⃣ Vertical datum specification (required)

Every vertical‑aware dataset **must** declare:

- `vertical_datum` (e.g., `"NAVD88"`).  
- `vertical_epoch` (e.g., `"2018.0"` or `"2007.0"`).  
- `geoid_model` (e.g., `"GEOID18"`).  
- `units` (KFM v11: **meters only** for vertical).  

**KFM internal keys (generic metadata):**

```text
kfm.vertical_datum:  "NAVD88"
kfm.vertical_epoch:  "2018.0"
kfm.geoid_model:     "GEOID18"
kfm.vertical_units:  "m"
```

#### Tidal datums

If tidal datums are involved (e.g., `MLLW`, `MHW`):

1. The tidal datum must be declared explicitly in metadata.  
2. A transformation description (and tool version) must be provided.  
3. PROV‑O lineage must link source tidal heights to NAVD88 or other orthometric references.

Tidal‑to‑orthometric transformations **must not** be implicit.

---

### 2️⃣ CF‑Conventions Z‑axis rules

Any grid or field with vertical meaning must have a CF‑compliant vertical coordinate or attribute.

**NetCDF example (bathymetry):**

```text
float depth(y, x);
  depth:standard_name = "depth";
  depth:long_name = "Bathymetric depth below NAVD88";
  depth:units = "m";
  depth:positive = "down";
  depth:vertical_datum = "NAVD88";
  depth:geoid_model = "GEOID18";
```

**Rule‑of‑thumb table:**

| Dataset Type       | `positive` | Meaning                              |
|--------------------|-----------:|--------------------------------------|
| DEM / Elevation    | `"up"`     | Higher elevation = positive          |
| Water surface (WSEL) | `"up"`   | Higher water surface = positive      |
| Bathymetry / Depth | `"down"`   | Deeper (below reference) = positive |

The CF `positive` attribute is **mandatory** and must match reality.

---

### 3️⃣ DEM‑of‑Difference (DoD) sign convention (mandatory)

KFM v11 **canonical DoD convention**:

- **Erosion = NEGATIVE**  
- **Deposition = POSITIVE**

Meaning:

```text
DoD = DEM_later - DEM_earlier

DoD < 0  → erosion (surface lowered)
DoD > 0  → deposition (surface raised)
```

**Required metadata keys:**

```text
dod.sign_convention: "erosion_negative_deposition_positive"
dod.reference: "NAVD88, m"
```

**UI legend (standardized text):**

```text
Negative (blue) = erosion
Positive (red)  = deposition
NAVD88, meters
```

MapLibre, Cesium, and any dashboards must use this wording (or a very close, clearly equivalent variant).

---

### 4️⃣ Units & precision

- Vertical units MUST be `"m"` (meters).  
- Storage precision:
  - Preserve native resolution from DEM / lidar where feasible.  
- Visualization precision:
  - Recommended to display to 0.01–0.1 m depending on map scale and uncertainty.  
- DoD products:
  - Should include uncertainty or noise floor metadata where available.

---

### 5️⃣ File‑level requirements

#### 5.1 GeoTIFF / COG

Where possible, populate vertical geokeys; in addition, a **sidecar JSON** (or embedded STAC metadata) is required:

```json
{
  "vertical_datum": "NAVD88",
  "vertical_epoch": "2018.0",
  "geoid_model": "GEOID18",
  "units": "m",
  "cf_positive": "up"
}
```

#### 5.2 NetCDF

Global attributes **required**:

```text
:vertical_datum = "NAVD88";
:vertical_epoch = "2018.0";
:geoid_model    = "GEOID18";
:vertical_units = "m";
```

Each vertical variable must also carry `units` and `positive`.

---

### 6️⃣ Examples (validated patterns)

**Bathymetry grid:**

- Datum → `NAVD88`  
- `positive = "down"`  
- STAC → `"kfm:cf_positive": "down"`

**Terrain DEM:**

- Datum → `NAVD88`  
- `positive = "up"`  

**DoD product:**

- Both epochs must be on **the same vertical datum** (typically NAVD88).  
- Erosion < 0, deposition > 0.  
- STAC → `"kfm:dod_sign": "erosion_negative_deposition_positive"`.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC vertical fields

STAC Items for vertical‑aware datasets must include:

```json
{
  "proj:epsg": 26914,
  "vertical:reference_frame": "NAVD88",
  "vertical:geoid_model": "GEOID18",
  "vertical:unit": "meter",
  "kfm:cf_positive": "up or down",
  "kfm:dod_sign": "erosion_negative_deposition_positive"  // DoD only
}
```

Rules:

- If a dataset has vertical meaning (DEM, bathymetry, DoD, WSEL, etc.), `vertical:*` and `kfm:cf_positive` are mandatory.  
- `kfm:dod_sign` is mandatory for any DoD or bed‑change product.

### 2. DCAT mapping

In DCAT 3.0:

- `vertical:reference_frame` → `dct:conformsTo` or profile‑specific vertical property.  
- `vertical:unit` → may map to `qudt:unit` in extended profiles.  
- `kfm:dod_sign` → part of domain‑specific metadata used in DCAT notes or provenance extensions.

### 3. PROV‑O vertical lineage

Vertical transformations (e.g., tidal → NAVD88) must be represented as:

```text
prov:used            → source DEM / bathymetry / tide model
prov:activity        → "vertical-transformation-v11"
prov:wasGeneratedBy  → vertical transformation tool + version
prov:generatedAtTime → timestamp
prov:wasAssociatedWith → KFM ETL agent or service
```

If heights are transformed between datums or geoid models, those operations must **never** be implicit.

---

## 🧱 Architecture

### 1. Vertical semantics in ETL

ETL pipelines must:

- Treat vertical information as a **first‑class dimension**.  
- Keep vertical transformations distinct from XY reprojections.  
- Fail early if vertical metadata is missing or inconsistent between inputs.

Typical steps:

1. Validate vertical metadata for inputs (DEM, bathymetry, WSEL, etc.).  
2. Normalize to KFM references (NAVD88 + GEOID18) where appropriate.  
3. Record all transformations (vertical and XY) in PROV.  
4. Emit STAC Items with correct `vertical:*`, `kfm:cf_positive`, and `kfm:dod_sign`.

### 2. API & UI schemas

APIs returning vertical‑aware data must include:

```text
vertical_datum
vertical_epoch
geoid_model
units
cf_positive
dod_sign    # DoD only
```

MapLibre/Cesium:

- Must display datum + units + sign convention in legends or layer metadata.  
- Must use orthometric heights (NAVD88) for 3D vertical exaggeration.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode depend on this standard to:

- Interpret DEM and water‑surface layers correctly when giving explanations.  
- Describe erosion/deposition accurately for DoD‑based narratives.  
- Avoid misleading statements about “rise” or “fall” when sign conventions differ.

Requirements:

- Story Nodes must **not** invert DoD semantics; they should use the standard:
  - Negative = erosion, positive = deposition.  
- Focus Mode must:
  - Surface datum and units when summarizing vertical products.  
  - Avoid speculative interpretations if vertical metadata is incomplete (and should flag that as a limitation).  

Vertical metadata may be included in Story Node `spacetime` or `attributes` sections via references to STAC Items and this standard.

---

## 🧪 Validation & CI/CD

The following are **PR blockers** for vertical‑aware datasets:

- Missing `vertical:reference_frame` or `vertical:unit`.  
- Missing `kfm:cf_positive` for any vertical‑aware dataset.  
- Missing `kfm:dod_sign` for DoD products.  
- Inconsistent or missing vertical metadata between files and STAC.  
- Unclear or absent vertical metadata in API schemas or UI configurations for vertical layers.  
- Failure of vertical‑axis schema validation (JSON/SHACL).

Typical automated checks:

- **schema‑lint** — validates STAC and NetCDF/GeoTIFF metadata against vertical schemas.  
- **metadata‑check** — ensures required vertical keys/fields are present.  
- **provenance‑check** — ensures vertical transformations are recorded in PROV where expected.  
- **footer‑check** — ensures this standard is referenced consistently by dependent docs.

---

## ⚖ FAIR+CARE & Governance

Vertical semantics impact FAIR+CARE indirectly:

- **FAIR**

  - Clear vertical metadata improves **interoperability** of DEM, DoD, and hydrology datasets.  
  - Deterministic DoD conventions make change products more **reusable** and comparable across studies.

- **CARE**

  - Erosion/deposition and elevation can be used to argue about land change, flooding, and impacts to communities.  
  - Mislabeling or misinterpreting vertical change could cause harm (e.g., under‑representing flood risk).  
  - This standard supports responsible communication of vertical change by removing ambiguity.

Governance rules:

- Any change to datum, CF sign conventions, or DoD semantics requires FAIR+CARE Council review.  
- Datasets impacting Indigenous lands or sensitive heritage sites must have vertical interpretations cross‑checked against sovereignty policies and, where appropriate, community reviewers.

---

## 🕰️ Version History

| Version | Date       | Status            | Notes                                                                                           |
|--------:|------------|-------------------|-------------------------------------------------------------------------------------------------|
| v11.0.1 | 2025-11-22 | Active / Enforced | Upgraded to KFM‑MDP v11.2.4 layout; added STAC/DCAT/PROV alignment, CI profiles, and governance hooks. |
| v11.0.0 | 2025-11-20 | Superseded        | Initial v11 vertical‑axis/DoD standard; established datum, CF Z‑axis, and DoD sign rules.      |

---

<div align="center">

📐 **KFM v11 — Vertical Datums, CF Z-Axis, and DoD Sign Convention Standard**  
Accurate Elevations · Correct Depths · Trustworthy Change Maps  

[⬅ Back to Geo Standards](./README.md) · [🏛 Governance](../governance/ROOT-GOVERNANCE.md) · [📘 KFM v11 Reference](../../reference/kfm_v11_master_documentation.md)

</div>
