---
title: "🌾 KFM — Pasture Biomass Estimation Design Pack (Image-Based)"
path: "docs/design/pasture-biomass/README.md"
version: "v0.1.1"
last_updated: "2025-12-10"

release_stage: "Draft / Experimental"
lifecycle: "Incubation"
review_cycle: "Quarterly · Data & Agronomy Working Group"
content_stability: "evolving"
status: "Active"

doc_kind: "Design Note"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "pasture-biomass"
  applies_to:
    - "kfm-pasture-biomass-module"
    - "kansas-agro-ecology"
    - "image-based-biomass-models"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM Data & Agronomy Working Group"

json_schema_ref: "schemas/json/design-pasture-biomass-v0.1.1.schema.json"
shape_schema_ref: "schemas/shacl/design-pasture-biomass-v0.1.1-shape.ttl"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:design:pasture-biomass:v0.1.1"
semantic_document_id: "kfm-design-pasture-biomass-v0.1.1"
event_source_id: "ledger:kfm:doc:design:pasture-biomass:v0.1.1"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🌾 **Pasture Biomass Estimation Design Pack (Image-Based)**  
`docs/design/pasture-biomass/README.md`

**Purpose**  
Define a KFM-native, **config-driven design pack** for estimating pasture biomass from top-down imagery, wired cleanly into the pipeline:

**ETL → STAC/DCAT/PROV catalogs → Neo4j → API → React/MapLibre/Cesium → Story Nodes → Focus Mode**

This document standardizes:

- Sample units (quadrats)  
- Label semantics and constraints  
- Preprocessing lineage  
- Training vs inference interfaces  
- Metrics and evaluation  
- Ontology fragments for biomass  
- Model recipes and QC patterns  
- Licensing and governance hooks  

</div>

---

## 📘 Overview

### Scope

This design pack covers **image-based estimation of pasture biomass per fixed quadrat**. It is:

- **KFM-native** — no external competition assumptions.  
- **Deterministic** — everything must be representable as config and metadata.  
- **Graph-aware** — every spec here should map to Neo4j nodes/relationships.  
- **Story-ready** — outputs must be safe and understandable in Story Nodes / Focus Mode.

It should be used as the **reference template** when:

- Ingesting new pasture biomass quadrat datasets  
- Designing new biomass models or evaluation pipelines  
- Adding related Story Nodes and Focus Mode overlays for Kansas pastures

### Out of Scope (for this document)

- Non-image modalities as primary inputs (e.g., LiDAR-only, radar-only)  
- Plot-level or paddock-level aggregation strategies (covered by higher-level range modules)  
- Detailed implementation code (lives under `src/` with configs referencing this design)

---

## 🗂️ Directory Layout

This design pack assumes the following minimal layout in the monorepo:

~~~text
📂 docs/design/pasture-biomass/
├── 📄 README.md              # Pasture biomass estimation design pack (this document)
├── 📂 specs/                 # Machine-readable specs (YAML/JSON)
│   ├── 📄 sample_unit.yaml   # SampleUnitSpec definitions
│   ├── 📄 constraints.yaml   # ConstraintSpec
│   ├── 📄 preprocess.yaml    # PreprocessSpec
│   ├── 📄 metrics.yaml       # MetricSpec
│   ├── 📄 profiles.yaml      # Training/Inference profiles
│   └── 📄 models.yaml        # ModelRecipe definitions
├── 📂 examples/              # Example configs, notebooks, and synthetic demo data
└── 📂 stac/                  # Draft STAC Collections/Items for quadrat datasets
~~~

Author rules:

- **Do not** introduce new top-level directories for pasture biomass under `docs/`. Extend this tree.  
- Every spec introduced below must have a matching file under `docs/design/pasture-biomass/specs/`.  
- STAC/DCAT examples live in `docs/design/pasture-biomass/stac/` and are mirrored into `data/stac/` by ETL.

---

## 🧭 Context

### KFM Pipeline Fit

This design pack must fit the standard KFM pipeline:

1. **Deterministic ETL**  
   - ETL pulls raw quadrat images and tabular biomass measurements.  
   - Applies `PreprocessSpec` to align geometry and resolution.  
   - Enforces `ConstraintSpec` and `QCReport` rules at ingest.

2. **STAC/DCAT/PROV catalogs**  
   - Each quadrat sample is a STAC Item with: `SampleUnitSpec`, `PreprocessSpec`, QC flags, and biomass labels.  
   - DCAT Dataset(s) describe the overall pasture biomass collections.  
   - PROV captures ETL runs and model evaluations as Activities with generated Entities.

3. **Neo4j Knowledge Graph**  
   - Nodes for `SampleUnit`, `BiomassComponent`, `PreprocessSpec`, `ModelRecipe`, etc.  
   - Relationships express constraints, derivations, and evaluation results.

4. **API Layer**  
   - Read-only APIs surface biomass predictions, QC status, and metadata per quadrat or aggregated area.  
   - Contracts reference the `InferenceProfile` identifiers defined here.

5. **React / MapLibre / Cesium**  
   - Frontends render maps, time-series, and uncertainty bands over Kansas pasture lands.  
   - Only high-QC quadrats and tiles are exposed in public layers by default.

6. **Story Nodes → Focus Mode**  
   - Story Nodes help explain biomass trends in space/time (e.g., drought years vs. wet years).  
   - Focus Mode constrains itself to the semantics and guardrails defined in this design pack.

---

## 📦 Data & Metadata

### 1. Sample Unit Specification (Pasture Quadrat)

#### 1.1 Concept

The **atomic sample unit** is a **fixed physical quadrat** imaged from above.

KFM treats each quadrat as a first-class object so that:

- Multiple datasets can share the same `SampleUnitSpec`  
- Models and evaluations can refer to a stable `sample_unit` identifier  
- STAC, DCAT, Neo4j, and APIs all agree on “what one sample is”

#### 1.2 SampleUnitSpec (logical schema)

Authoritative schema lives under `docs/design/pasture-biomass/specs/sample_unit.yaml`.  
Illustrative example:

~~~yaml
SampleUnitSpec:
  id: quadrat_70x30_topdown_v1
  description: "Top-down pasture quadrat sample"
  footprint_cm:
    width: 70
    height: 30
  capture_view: "top_down"
  required_contents:
    - "quadrat_frame_fully_visible"
    - "pasture_within_frame"
  notes:
    - "Assumes camera is roughly nadir; minor perspective distortion handled in preprocessing."
~~~

#### 1.3 KFM Usage

Attach `SampleUnitSpec.id` to:

- STAC Items representing quadrat images (e.g., `properties.sample_unit = "quadrat_70x30_topdown_v1"`).  
- Dataset cards and DCAT Datasets describing quadrat-based collections.  
- Model cards and evaluation entities in Neo4j.  
- Validation logic in ETL to flag samples that violate quadrat framing (e.g., incomplete frame, heavy occlusion).

---

### 2. Label Semantics and Compositional Constraints

#### 2.1 Biomass Components

All biomass labels are defined per quadrat, in **grams (g)**:

- `Dry_Green_g` — green, non-clover dry biomass  
- `Dry_Dead_g` — dead/senescent dry biomass  
- `Dry_Clover_g` — clover/legume dry biomass  
- `GDM_g` — green dry matter (derived)  
- `Dry_Total_g` — total dry biomass (derived)

#### 2.2 Compositional Rules

Rather than treating each label as independent columns, we encode **constraints**:

- `GDM_g = Dry_Green_g + Dry_Clover_g`  
- `Dry_Total_g = Dry_Green_g + Dry_Dead_g + Dry_Clover_g`

These constraints are normatively enforced at:

- Ingest (labels)  
- Evaluation (predictions)  
- Monitoring (drift or constraint violations over time)

#### 2.3 ConstraintSpec

Logical schema (stored in `docs/design/pasture-biomass/specs/constraints.yaml`):

~~~yaml
ConstraintSpec:
  id: pasture_biomass_constraints_v1
  constraints:
    - id: gdm_is_green_plus_clover
      expression: "GDM_g == Dry_Green_g + Dry_Clover_g"
      description: "Green dry matter equals green plus clover fractions."
    - id: total_is_sum_of_components
      expression: "Dry_Total_g == Dry_Green_g + Dry_Dead_g + Dry_Clover_g"
      description: "Total dry biomass equals sum of green, dead, and clover components."
~~~

#### 2.4 KFM Usage

- **ETL** — reject or flag rows where constraints fail beyond tolerance.  
- **Evaluation** — check both ground truth and predictions for consistency; report violation rates.  
- **Model design** — encourage recipes that predict base components and derive totals.

---

### 3. Data Quality and Provenance

#### 3.1 QCReport

QC spec lives in `docs/design/pasture-biomass/specs/qc.yaml`. Schema sketch:

~~~yaml
QCReport:
  id: pasture_biomass_qc_v1
  description: "Quality checks for curated quadrat samples."
  checks:
    - id: biomass_range_check
      description: "Validate biomass values are within plausible agronomic ranges."
    - id: sum_consistency_check
      description: "Check derived totals match sum of components within tolerance."
    - id: image_visibility_check
      description: "Ensure quadrat is fully visible and not occluded."
    - id: metadata_completeness
      description: "Flag missing critical metadata fields."
  outputs:
    dataset_summary:
      total_samples: "<fill-in>"
      passed_all_checks: "<fill-in>"
      failed_any_checks: "<fill-in>"
    per_sample_flags: true
~~~

#### 3.2 KFM Usage

- QC outputs are stored alongside datasets in STAC Items and Neo4j.  
- Training pipelines should support filtering to **high-QC** samples.  
- Public-facing Story Nodes must **avoid** showing low-QC or ambiguous areas by default.

---

## 🧱 Architecture

### 4. Preprocessing Lineage for Pasture Images

#### 4.1 Goals

- Standardize quadrat geometry and resolution across datasets.  
- Make models portable across capture hardware and protocols.  
- Represent preprocessing as a **versioned spec**, not ad-hoc code.

#### 4.2 PreprocessSpec

Stored at `docs/design/pasture-biomass/specs/preprocess.yaml`:

~~~yaml
PreprocessSpec:
  id: pasture_quadrat_rectify_v1
  description: "Rectify quadrat region and standardize resolution/orientation."
  input:
    modality: "RGB"
    sample_unit: "quadrat_70x30_topdown_v1"
  steps:
    - id: detect_quadrat_roi
      type: "geometry_detection"
      description: "Detect quadrat boundaries (frame or markers) in the image."
    - id: rectify_to_rectangle
      type: "projective_transform"
      description: "Apply affine/perspective transform so quadrat becomes a flat rectangle."
    - id: resample
      type: "rescale"
      params:
        width_px: 2000
        height_px: 1000
    - id: orientation_align
      type: "orientation_normalization"
      description: "Rotate so quadrat has a consistent orientation (e.g., long side horizontal)."
  invariants:
    - "Each pixel corresponds to a consistent physical area."
    - "Quadrat region fills the frame after preprocessing."
~~~

#### 4.3 KFM Usage

- ETL tags STAC Items and DCAT Distributions with `preprocess_spec`.  
- Training configs and experiment logs reference `PreprocessSpec.id` directly.  
- Provenance graphs capture preprocessing Activities and Entities using PROV-O.

---

### 5. Training vs Inference Profiles

#### 5.1 Concept

We keep **training** and **inference** interfaces explicit and separable:

- Training can see extra signals (e.g., height, NDVI)  
- Inference must only rely on what is guaranteed in production

#### 5.2 InferenceProfile (image-only)

~~~yaml
InferenceProfile:
  id: pasture_biomass_image_only_v1
  description: "Production interface using only an RGB image."
  inputs:
    - name: image
      type: "RGBImage"
      constraints:
        sample_unit: "quadrat_70x30_topdown_v1"
        preprocess_spec: "pasture_quadrat_rectify_v1"
  outputs:
    - "Dry_Green_g"
    - "Dry_Dead_g"
    - "Dry_Clover_g"
    - "GDM_g"
    - "Dry_Total_g"
~~~

#### 5.3 TrainingProfile (image + auxiliary signals)

~~~yaml
TrainingProfile:
  id: pasture_biomass_image_plus_aux_v1
  description: "Training interface that may include auxiliary field measurements."
  inputs:
    - name: image
      type: "RGBImage"
      constraints:
        sample_unit: "quadrat_70x30_topdown_v1"
        preprocess_spec: "pasture_quadrat_rectify_v1"
    - name: ndvi
      type: "float"
      optional: true
    - name: height_cm
      type: "float"
      optional: true
    - name: sampling_date
      type: "date"
      optional: true
    - name: species
      type: "categorical"
      optional: true
    - name: state
      type: "categorical"
      optional: true
  outputs:
    - "Dry_Green_g"
    - "Dry_Dead_g"
    - "Dry_Clover_g"
    - "GDM_g"
    - "Dry_Total_g"
~~~

#### 5.4 KFM Usage

- Models tagged with `pasture_biomass_image_only_v1` **must not** depend on auxiliary fields at runtime.  
- Training pipelines may use auxiliary inputs for representation learning and side tasks, but those paths must be disabled under the inference profile.

---

### 6. Metric Specification for Biomass Regression

#### 6.1 Concept

We use a **metric spec** so every experiment evaluates in the same target space with the same weighting.

#### 6.2 MetricSpec: weighted log-R²

~~~yaml
MetricSpec:
  id: weighted_log_r2_v1
  description: "Log-stabilized per-target R², weighted by importance."
  transform:
    id: log_stabilize_v1
    type: "log1p"
    expression: "log(1 + x)"
  per_target_metric: "r2"
  targets:
    - name: "Dry_Green_g"
      weight: 0.1
    - name: "Dry_Dead_g"
      weight: 0.1
    - name: "Dry_Clover_g"
      weight: 0.1
    - name: "GDM_g"
      weight: 0.2
    - name: "Dry_Total_g"
      weight: 0.5
~~~

#### 6.3 KFM Usage

- All model evaluations (offline and production) reference `MetricSpec.id`.  
- Scores are comparable across time, data splits, and teams.  
- Metric results are stored as Entities in PROV graphs and as properties on Model nodes in Neo4j.

---

### 7. Pasture Biomass Ontology Fragment

#### 7.1 Concepts

Logical ontology fragment (mirrored in `src/graph/` and ontology configs):

~~~yaml
OntologyFragment:
  id: pasture_biomass_v1
  concepts:
    - id: biomass_dry
      label: "Dry Biomass"
      type: "quantity"
    - id: biomass_dry_green
      label: "Green Dry Biomass"
      parent: "biomass_dry"
    - id: biomass_dry_dead
      label: "Dead Dry Biomass"
      parent: "biomass_dry"
    - id: biomass_dry_clover
      label: "Clover Dry Biomass"
      parent: "biomass_dry"
    - id: biomass_gdm
      label: "Green Dry Matter"
      parent: "biomass_dry"
      derived_from:
        - "biomass_dry_green"
        - "biomass_dry_clover"
    - id: biomass_dry_total
      label: "Total Dry Biomass"
      parent: "biomass_dry"
      derived_from:
        - "biomass_dry_green"
        - "biomass_dry_dead"
        - "biomass_dry_clover"
    - id: vigor_ndvi
      label: "NDVI"
      type: "index"
    - id: vigor_height
      label: "Canopy Height"
      type: "length"
~~~

#### 7.2 KFM Usage

- STAC and DCAT fields reference these concept IDs in their semantics.  
- Neo4j nodes and relationships use these IDs for strong typing.  
- UI uses them to drive labels and aggregations (e.g., “dead fraction”, “clover contribution”).

---

### 8. Model Recipes with Constraint Guarantees

#### 8.1 Recipe: Predict base components, derive totals

~~~yaml
ModelRecipe:
  id: vision_regression_3head_plus_derived_totals_v1
  description: "Three-head vision model predicting base biomass components; totals derived."
  backbone:
    type: "vision_backbone"
    examples: ["resnet50", "efficientnet_b3", "vit_small"]
  heads:
    - "Dry_Green_g"
    - "Dry_Dead_g"
    - "Dry_Clover_g"
  training:
    loss:
      type: "huber"
      target_space: "log_stabilize_v1"
    aux_tasks:
      - name: "ndvi_prediction"
        enabled: true
        optional_input: "ndvi"
      - name: "height_prediction"
        enabled: true
        optional_input: "height_cm"
  inference:
    profile: "pasture_biomass_image_only_v1"
  postprocess:
    - derive:
        name: "GDM_g"
        expression: "Dry_Green_g + Dry_Clover_g"
    - derive:
        name: "Dry_Total_g"
        expression: "Dry_Green_g + Dry_Dead_g + Dry_Clover_g"
  constraints_enforced:
    - "gdm_is_green_plus_clover"
    - "total_is_sum_of_components"
  metric_spec: "weighted_log_r2_v1"
~~~

#### 8.2 Recipe: Direct 5-head + constraint penalty

~~~yaml
ModelRecipe:
  id: vision_regression_5head_with_constraint_penalty_v1
  description: "Five-head model predicting all biomass targets with soft constraint penalties."
  backbone:
    type: "vision_backbone"
  heads:
    - "Dry_Green_g"
    - "Dry_Dead_g"
    - "Dry_Clover_g"
    - "GDM_g"
    - "Dry_Total_g"
  training:
    loss:
      primary:
        type: "huber"
        target_space: "log_stabilize_v1"
      penalties:
        - id: "gdm_consistency_penalty"
          expression: "GDM_g - (Dry_Green_g + Dry_Clover_g)"
          type: "l2"
          weight: 0.1
        - id: "total_consistency_penalty"
          expression: "Dry_Total_g - (Dry_Green_g + Dry_Dead_g + Dry_Clover_g)"
          type: "l2"
          weight: 0.1
  inference:
    profile: "pasture_biomass_image_only_v1"
  metric_spec: "weighted_log_r2_v1"
~~~

---

### 9. KFM Module Template (Minimal Wiring)

A minimal module schema tying the pieces together:

~~~yaml
KFMModule: "pasture_biomass_estimation"
version: "v0.1.1"
dataset_card:
  id: "pasture_biomass_image_quadrats_v1"
  sample_unit: "quadrat_70x30_topdown_v1"
  targets:
    - "Dry_Green_g"
    - "Dry_Dead_g"
    - "Dry_Clover_g"
    - "GDM_g"
    - "Dry_Total_g"
  license: "CC-BY-SA-4.0"
  ontology_fragment: "pasture_biomass_v1"
specs:
  sample_unit_spec: "quadrat_70x30_topdown_v1"
  preprocess_spec: "pasture_quadrat_rectify_v1"
  constraint_spec: "pasture_biomass_constraints_v1"
  metric_spec: "weighted_log_r2_v1"
  inference_profiles:
    - "pasture_biomass_image_only_v1"
  training_profiles:
    - "pasture_biomass_image_plus_aux_v1"
model_recipes:
  - "vision_regression_3head_plus_derived_totals_v1"
  - "vision_regression_5head_with_constraint_penalty_v1"
qc_report_spec: "pasture_biomass_qc_v1"
license_spec: "CC-BY-SA-4.0"
~~~

This module definition is intended to be imported by:

- ETL configs under `src/pipelines/`  
- Graph/ontology mappings under `src/graph/`  
- API schemas under `src/api/`  
- Story Node templates under `docs/design/` and `docs/analyses/`

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC Items (Quadrat Samples)

Each quadrat image sample should be a STAC Item with, at minimum:

- `properties.sample_unit` → `SampleUnitSpec.id`  
- `properties.preprocess_spec` → `PreprocessSpec.id`  
- `properties.constraint_spec` → `ConstraintSpec.id`  
- `properties.metric_spec` (for evaluation Items) → `MetricSpec.id`  
- `properties.ontology_fragment` → `pasture_biomass_v1`  
- `properties.qc_report_id` and QC flags

Illustrative (partial) Item properties:

~~~json
{
  "id": "ks_pasture_quadrat_000123",
  "properties": {
    "datetime": "2025-05-12T16:30:00Z",
    "sample_unit": "quadrat_70x30_topdown_v1",
    "preprocess_spec": "pasture_quadrat_rectify_v1",
    "constraint_spec": "pasture_biomass_constraints_v1",
    "ontology_fragment": "pasture_biomass_v1",
    "biomass_labels": {
      "Dry_Green_g": 210.0,
      "Dry_Dead_g": 95.0,
      "Dry_Clover_g": 40.0,
      "GDM_g": 250.0,
      "Dry_Total_g": 345.0
    },
    "qc": {
      "report_spec": "pasture_biomass_qc_v1",
      "flags": ["passed_all_checks"]
    }
  }
}
~~~

### DCAT Datasets

DCAT Datasets should capture:

- Dataset title/description and spatial/temporal coverage  
- Linkage to this design pack via `dct:conformsTo`  
- Versioning using DCAT 3 patterns if multiple biomass dataset releases exist

Example sketch:

- `dcat:Dataset` — `ks-pasture-biomass-quadrats-v1`  
  - `dct:conformsTo` → this design document (`semantic_document_id`)  
  - `dcat:distribution` → quadrat label tables, STAC catalogs, and derived gridded surfaces

### PROV Lineage

Use PROV-O to represent:

- Raw quadrat image `prov:Entity`  
- Preprocessing `prov:Activity` using raw image and generating preprocessed image Entity  
- Labeling campaign `prov:Activity` generating biomass label tables  
- Training runs `prov:Activity` using the above Entities and generating a Model Entity

Key relationships:

- `prov:wasGeneratedBy` — for preprocessed imagery, model weights, evaluation reports  
- `prov:used` — for images, labels, specs, and QC reports consumed by Activities  
- `prov:wasDerivedFrom` — for predictions derived from images and models

---

## 🧠 Story Node & Focus Mode Integration

### Story Node Patterns

Story Nodes built on this design pack should:

- Reference this document via `semantic_document_id` for context.  
- Use spatial extents derived from quadrat locations or aggregated tiles.  
- Include temporal windows matching observation or prediction dates.  
- Explicitly label **facts** (observed biomass), **interpretation** (e.g., “likely drought effect”), and **speculation**.

Example narrative fields:

- **Title** — “Pasture Biomass and Drought in Southwestern Kansas (2025)”  
- **Facts** — Graph-backed metrics (e.g., median `Dry_Total_g` vs historical baseline).  
- **Interpretation** — Short explanation sourced from agronomic knowledge and data, not from model speculation alone.

### Focus Mode Behavior

When Focus Mode is active on a pasture biomass layer:

- **May**  
  - Summarize biomass levels and trends in the selected area.  
  - Highlight QC status and model version in use.  
  - Explain which labels are derived vs directly predicted.

- **Must Not**  
  - Invent biomass values or ecological processes not supported by data.  
  - Override FAIR+CARE or sovereignty constraints (e.g., private ranch data, sensitive locations).  
  - Present speculative management recommendations as facts.

---

## 🧪 Validation & CI/CD

### Tests and Checks

CI/CD should include (at minimum):

- **Schema validation** for all specs in `docs/design/pasture-biomass/specs/` against `json_schema_ref` and `shape_schema_ref`.  
- **Markdown linting** for this document (KFM-MDP v11.2.6 compliance).  
- **Constraint tests** — synthetic data rows that intentionally violate constraints must be caught by ETL.  
- **Metric spec tests** — ensure log-transform and weights are applied consistently in evaluation code.

### Pipelines

Recommended CI integration:

- `.github/workflows/kfm-ci.yml` includes a pasture-biomass job that:  
  - Validates specs.  
  - Runs unit tests for training/inference profile enforcement.  
  - Runs quick smoke tests on sample STAC/DCAT/PROV outputs.

### Reproducibility

- All experiments must be config-driven (no hard-coded hyperparameters).  
- Random seeds are recorded in experiment configs and PROV Activities.  
- Model Registry entries include `ModelRecipe.id`, `MetricSpec.id`, seeds, and dataset versions.

---

## ⚖ FAIR+CARE & Governance

### Licensing and Governance Controls

#### LicenseSpec

~~~yaml
LicenseSpec:
  id: "CC-BY-SA-4.0"
  name: "Creative Commons Attribution-ShareAlike 4.0"
  requires_attribution: true
  requires_sharealike: true
  url: "https://creativecommons.org/licenses/by-sa/4.0/"
~~~

#### KFM Usage

- Dataset cards and derived artifacts must declare license and attribution text blocks.  
- Export and publishing flows should:  
  - Warn or block incompatible downstream licenses.  
  - Auto-insert attribution snippets into generated docs and Story Nodes.

### FAIR+CARE Considerations

- **FAIR**  
  - Findable: STAC & DCAT entries indexed and searchable by sample unit, region, and time.  
  - Accessible: Open access for non-sensitive quadrat data; gated access where private land or agreements apply.  
  - Interoperable: STAC/DCAT/PROV-compliant metadata.  
  - Reusable: Clear licenses, provenance, and constraints.

- **CARE**  
  - Collective Benefit: Designed to support pasture management, research, and education.  
  - Authority to Control: Respect private landowner and Indigenous/tribal agreements for data sharing.  
  - Responsibility: Clearly mark uncertainty and QC in public-facing outputs.  
  - Ethics: Avoid misinterpretation of model outputs as direct management prescriptions.

All pasture biomass work must also comply with:

- `ROOT-GOVERNANCE.md` for overall decision-making and auditability.  
- `FAIRCARE-GUIDE.md` and `INDIGENOUS-DATA-PROTECTION.md` where relevant.

---

## 🕰️ Version History

| Version  | Date       | Author     | Summary                                                                                   |
|----------|------------|-----------|-------------------------------------------------------------------------------------------|
| v0.1.1   | 2025-12-10 | KFM Team  | Realigned with KFM-MDP v11.2.6; added directory layout, STAC/DCAT/PROV alignment, Story Node & Focus Mode guidance, CI/CD hooks, and governance footer. |
| v0.1.0   | 2025-12-10 | KFM Team  | Initial pasture biomass design pack: sample unit, labels, constraints, preprocessing, profiles, metrics, ontology fragment, model recipes, QC, and licensing. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  

Part of the KFM pasture and agro-ecology module · Governed by  
[ROOT-GOVERNANCE](../../standards/governance/ROOT-GOVERNANCE.md) ·  
[FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) ·  
[Indigenous Data Protection](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)  

[⬅ Back to Design Index](../README.md) ·  
[🌾 Pasture Data Index](../../data/pasture/README.md) ·  
[🔐 Governance & Standards](../../standards/README.md)

</div>
