---
title: "🛰️ Kansas Frontier Matrix — Explainability Examples: Remote Sensing"
path: "tools/ai/explainability/docs/examples/remote_sensing/README.md"

version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Architecture"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:tools-ai-explainability-examples-remote-sensing:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-xai-examples-remote-sensing"
event_source_id: "ledger:tools/ai/explainability/docs/examples/remote_sensing/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

# NOTE: These refs point to the most recently known release packet in the repo docs.
# If a newer release exists (e.g., v11.2.6), update these refs to match that release folder.
sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "United States · Kansas"
sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_data_flag: false
risk_category: "Low"
redaction_required: false

ai_training_allowed: false
ai_training_guidance: "Explainability examples and governance artifacts MUST NOT be used as training data."

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - summary
    - timeline-generation
    - semantic-highlighting
    - 3d-context-render
    - a11y-adaptations
    - diagram-extraction
    - metadata-extraction
    - layout-normalization
  prohibited:
    - content-alteration
    - speculative-additions
    - unverified-architectural-claims
    - narrative-fabrication
    - governance-override

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next explainability platform update"

provenance_chain:
  - "tools/ai/README.md@v11.2.6"
  - "tools/ai/explainability/docs/README.md@v11.2.6"
  - "tools/ai/explainability/docs/examples/README.md@v11.2.6"
---

<div align="center">

# 🛰️ **KFM — Explainability Examples: Remote Sensing**
`tools/ai/explainability/docs/examples/remote_sensing/README.md`

**Purpose**  
Provide **policy-safe, KFM-compliant example patterns** for producing and packaging **explainability artifacts** for remote-sensing models (classification, segmentation, change detection), including:
how to bind results to **STAC/DCAT metadata**, attach **PROV-O lineage**, and ensure examples are **Focus Mode / Story Node ready** without leaking sensitive locations or restricted imagery.

</div>

---

## 📘 Overview

### What this folder is

This folder contains **documentation examples** for **remote-sensing explainability** in KFM:

- how to represent *inputs* (imagery/rasters) and *outputs* (masks/tiles/derived layers),
- how to produce *explainability overlays* (heatmaps, saliency maps, attention-like visualizations),
- how to package everything into a **governed evidence bundle** suitable for:
  - audits,
  - reproducible model evaluation,
  - Focus Mode evidence visualization,
  - downstream cataloging (STAC/DCAT) and provenance (PROV-O).

### What this folder is not

- Not a storage location for large rasters, training corpora, or full-resolution explainability outputs.
- Not a place to store run logs. Put run artifacts under:
  - `mcp/experiments/<run-id>/...` (preferred), or
  - `mcp/runs/<run-id>/...` (if your project uses that structure).

### Scope: remote-sensing model families covered

These examples are written to cover common KFM remote-sensing workloads:

- **Segmentation** (e.g., trails, land cover, water extent): pixel-wise masks + confidence rasters
- **Classification** (e.g., tile-level labels): class logits + uncertainty summaries
- **Change detection** (e.g., before/after comparisons): delta rasters + highlight regions

> The examples are model-agnostic: they focus on **artifact contracts** and **governed packaging**.

### Core invariants (normative)

1. Examples MUST remain **policy-safe** (no restricted coordinates, no PII, no sensitive imagery disclosures).
2. Explainability artifacts MUST be **traceable**:
   - input asset ID(s),
   - model identity (ID + version/hash),
   - output asset ID(s),
   - explainability artifact identity + checksums,
   - provenance activity references.
3. Examples MUST be **reproducible by design**:
   - fixed parameters,
   - pinned versions,
   - deterministic configs,
   - schema-checked payloads where applicable.
4. Examples MUST be usable by the UI without bypassing governance:
   - frontend loads assets through approved catalogs/APIs,
   - no direct graph access from the UI layer.

---

## 🗂️ Directory Layout

This README is one part of the Explainability docs example suite.

### Upstream context (expected explainability docs structure)

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 explainability/
        ├── 📄 README.md                          # Explainability subsystem entry (overview + contracts)
        └── 📁 docs/
            ├── 📄 README.md                      # Explainability docs home
            └── 📁 examples/
                ├── 📄 README.md                  # Examples index (tabular, narrative, remote sensing)
                ├── 📄 example-tabular.md         # Walkthrough example (tabular)
                ├── 📄 example-narrative.md       # Walkthrough example (narrative)
                ├── 📄 example-remote-sensing.md  # Walkthrough example (remote sensing)
                ├── 📁 integrity/
                │   └── 📄 README.md              # Example integrity patterns (checksums, provenance)
                ├── 📁 narrative/
                │   └── 📄 README.md              # Narrative explainability examples (Focus Mode / Story Nodes)
                └── 📁 remote_sensing/
                    └── 📄 README.md              # This file
~~~

### Local structure (this folder)

This folder is intentionally lightweight and documentation-first.

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 explainability/
        └── 📁 docs/
            └── 📁 examples/
                └── 📁 remote_sensing/
                    ├── 📄 README.md                     # This file
                    │
                    ├── 📁 templates/                    # Small, policy-safe templates (JSON/MD)
                    │   ├── 🧾 stac-item.template.json   # Minimal STAC Item template w/ XAI assets
                    │   ├── 🧾 prov-activity.template.jsonld # Minimal PROV-O activity template
                    │   └── 🧾 xai-bundle.template.json  # Explainability evidence bundle template
                    │
                    ├── 📁 examples/                     # Optional micro-examples (tiny, synthetic)
                    │   ├── 📄 example-segmentation.md   # Segmentation packaging pattern
                    │   ├── 📄 example-classification.md # Classification packaging pattern
                    │   └── 📄 example-change.md         # Change detection packaging pattern
                    │
                    └── 📁 assets/                       # OPTIONAL: tiny preview images only
                        ├── 🖼️ xai-overlay.example.png   # Downsampled overlay preview
                        └── 🖼️ mask-preview.example.png  # Downsampled mask preview
~~~

**Directory rules (normative)**

- If `assets/` exists, it MUST contain **only small previews** (no full-resolution imagery).
- Any example that references an image MUST include a **provenance pointer** (even for synthetic data).
- Any example that references coordinates MUST:
  - use **generalized geometry**, or
  - demonstrate masking / obfuscation in accordance with the sovereignty policy.

---

## 🧭 Context

### Why remote-sensing explainability needs “artifact contracts”

Remote-sensing models produce outputs that are visually compelling but can be misleading without context:

- preprocessing and band selection can dominate outcomes,
- sensor changes and seasonal differences can shift feature importance,
- explainability overlays can be mistaken for “ground truth.”

KFM treats explainability as an **evidence contract**, not a screenshot.

### Where explainability fits in the KFM pipeline

Remote sensing explainability should integrate cleanly with KFM’s governed flow:

- ETL and inference produce **assets**
- assets are cataloged in **STAC/DCAT**
- lineage is bound with **PROV-O**
- the graph stores relationships and identities
- APIs expose safe views to the UI
- Focus Mode shows narrative + evidence + citations

### Common remote-sensing explainability artifacts

This example suite focuses on policy-safe versions of:

- **Heatmaps** (importance per pixel or per patch)
- **Overlay previews** (importance blended with RGB)
- **Mask comparisons** (prediction vs baseline/reference)
- **Uncertainty summaries** (tile-level or region-level aggregates)
- **Evidence bundles** (JSON that binds it all with provenance and governance)

> This suite avoids embedding raw sensitive imagery. Use downsampled previews and/or synthetic tiles.

### Example “model folder pattern” used in KFM planning

KFM reference planning notes propose a model structure that explicitly includes `explainability/` alongside `config/` and `telemetry/` for remote sensing models (e.g., a segmentation CNN).  
This suite shows how to document and package explainability outputs in that style.

---

## 🗺️ Diagrams

### Remote-sensing explainability packaging flow (example)

~~~mermaid
flowchart LR
  A[Input imagery asset] --> B[Model inference]
  B --> C[Model outputs]
  B --> D[Explainability method]
  D --> E[XAI artifacts]
  C --> F[STAC Item update]
  E --> F
  F --> G[PROV-O activity record]
  G --> H[Registry / audit linkage]
  H --> I[API surfaces safe evidence]
  I --> J[Focus Mode evidence panel]
~~~

Accessibility note: data flows from imagery → inference → outputs and XAI → packaged into STAC + PROV → exposed via API → displayed in Focus Mode.

---

## 🧠 Story Node & Focus Mode Integration

### Evidence-first UX expectations

KFM planning and system workflow docs describe a Focus Mode UI with:

- a narrative panel with **citations** to source documents/datasets,
- an **AI explanation toggle** that reveals the “why” behind a summary,
- an **audit panel** that surfaces governance flags and redaction notices.

Remote sensing explainability examples should support that UX by providing:

- stable IDs and metadata links,
- preview-ready assets (downsampled),
- clear provenance pointers for every visual.

### Evidence panel mapping (recommended)

When a Focus Mode “evidence panel” renders remote sensing explainability, it should be able to fetch:

- preview image assets (e.g., overlay, mask preview),
- a compact JSON evidence bundle describing:
  - what the image is,
  - how it was derived,
  - what input/output it corresponds to,
  - what governance constraints apply.

To support this, the STAC Item (or a linked evidence record) SHOULD provide asset keys like:

- `xai_overlay_preview`
- `xai_heatmap`
- `prediction_mask`
- `uncertainty_summary`
- `xai_report`

> The exact asset keys are governed by your STAC profile; the examples here demonstrate the pattern, not a mandatory vocabulary.

### Redaction behavior (normative)

If explainability outputs could reveal protected locations or restricted cultural data:

- examples MUST demonstrate how to:
  - generalize geometry (e.g., coarse polygons or centroids),
  - omit precise coordinates from documentation artifacts,
  - include an audit notice describing the masking behavior,
  - ensure UI layers respect CARE settings (off-by-default, zoom-limited, or hidden).

---

## 🧪 Validation & CI/CD

### Compliance expectations for example content

Even “examples” are CI-visible and must remain clean:

- markdown lint must pass
- front-matter must validate (schema-lint)
- diagrams must be valid (diagram-check)
- **secret scanning** and **PII scanning** must not be triggered by example payloads

### Determinism rules for example templates

Example templates SHOULD be deterministic and stable:

- no timestamps embedded in example content unless explicitly documented
- no random IDs unless fixed and described
- checksums may be shown as `<sha256>` placeholders (do not include real secrets)

### Recommended checks for explainability examples

- `markdown-lint` (structure and fences)
- `schema-lint` (front-matter + JSON templates when applicable)
- `diagram-check` (Mermaid validity)
- `provenance-check` (every example asset has a provenance pointer)
- `secret-scan` / `pii-scan` (examples must not leak)

---

## 📦 Data & Metadata

### Minimal “XAI evidence bundle” contract (recommended)

A compact JSON record (policy-safe) that binds:

- model identity
- input asset reference(s)
- output asset reference(s)
- explainability artifact reference(s)
- governance labels
- provenance references

Example (illustrative):

~~~json
{
  "bundle_id": "kfm-xai-rs-demo-001",
  "bundle_version": "v11.2.6",
  "task": "segmentation",
  "model": {
    "model_id": "trail-segmentation-cnn",
    "model_version": "v0.1.0",
    "model_hash": "<sha256>"
  },
  "input": {
    "stac_item_id": "kfm-demo-imagery-tile-001",
    "assets": ["image_cog"]
  },
  "output": {
    "stac_item_id": "kfm-demo-segmentation-output-001",
    "assets": ["prediction_mask", "prediction_confidence"]
  },
  "explainability": {
    "method": "gradcam_like",
    "assets": ["xai_heatmap", "xai_overlay_preview"],
    "notes": "Example uses synthetic imagery and downsampled previews."
  },
  "governance": {
    "classification": "Public",
    "care_label": "Public · Low-Risk",
    "sensitivity": "General",
    "redaction_applied": false
  },
  "provenance": {
    "prov_activity_ref": "prov:kfm:activity:demo-xai-rs-001",
    "run_artifacts_ref": "mcp/experiments/<run-id>/"
  }
}
~~~

### STAC Item template (recommended pattern)

For remote sensing explainability, a STAC Item representing *model outputs* SHOULD attach explainability artifacts as assets.

Example (illustrative; keep real coordinates out of docs when sensitive):

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "kfm-demo-segmentation-output-001",
  "properties": {
    "datetime": "2025-01-01T00:00:00Z",
    "kfm:model_id": "trail-segmentation-cnn",
    "kfm:model_version": "v0.1.0",
    "kfm:care_label": "Public · Low-Risk"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[0.0, 0.0],[1.0, 0.0],[1.0, 1.0],[0.0, 1.0],[0.0, 0.0]]]
  },
  "bbox": [0.0, 0.0, 1.0, 1.0],
  "links": [],
  "assets": {
    "prediction_mask": {
      "href": "s3://<bucket>/demo/prediction_mask.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    },
    "xai_overlay_preview": {
      "href": "s3://<bucket>/demo/xai_overlay_preview.png",
      "type": "image/png",
      "roles": ["thumbnail"]
    },
    "xai_bundle": {
      "href": "s3://<bucket>/demo/xai_bundle.json",
      "type": "application/json",
      "roles": ["metadata"]
    }
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC alignment (remote sensing + explainability)

Recommended approach:

- Input imagery is indexed as STAC Items (imagery collection)
- Model outputs are indexed as STAC Items (model-output collection)
- Explainability artifacts are attached as **assets** on the output Item and/or as a linked “evidence item”

When versioning matters:

- maintain stable Item IDs for conceptual identity
- use explicit versioning metadata and/or the STAC Versioning Extension where your profile supports it

### DCAT alignment (dataset-level)

Use DCAT for dataset-level metadata when you publish:

- model output collections (e.g., statewide segmentation outputs)
- curated explainability bundles meant for external consumption

### PROV-O alignment (lineage)

Represent a remote-sensing explainability run as:

- `prov:Activity` = inference + explainability generation
- `prov:Entity` = input imagery item(s), output item(s), explainability bundle(s)
- `prov:Agent` = pipeline runner, model owner role, governance reviewer role

Key rule: **no “orphan” evidence assets** — every evidence artifact should have a provenance pointer.

---

## 🧱 Architecture

### Architecture goals for remote-sensing explainability in KFM

1. **Explainability is optional but governed**  
   Some deployments may disable heavy explainability; examples show safe minimal alternatives (previews + summaries).

2. **Artifacts must be discoverable and linkable**  
   Explainability outputs need stable IDs and catalog exposure so UI and audits can retrieve them.

3. **Artifacts must be safe-by-default**  
   Avoid storing sensitive imagery in doc paths. Prefer:
   - masked geometry
   - downsampled previews
   - aggregate summaries

### Reference implementation split (recommended)

- Model inference:
  - produces prediction rasters and summary JSON
- Explainability step:
  - produces heatmaps/overlays + bundle JSON
- Packaging step:
  - updates STAC Items and writes PROV records
- Surfacing:
  - API exposes safe evidence references
  - UI renders previews in an evidence panel and binds citations/provenance

---

## ⚖ FAIR+CARE & Governance

### Non-negotiables (normative)

- If data is sensitive, examples MUST show the **masking strategy** rather than leaking precision.
- Documentation MUST NOT invent governance status, provenance, or dataset relationships.
- Explainability artifacts that could be misinterpreted MUST include:
  - uncertainty notes,
  - method notes,
  - and provenance pointers.

### CARE-aware remote sensing concerns

Remote sensing can unintentionally reveal:

- protected cultural locations,
- sensitive infrastructure patterns,
- private activity patterns (depending on resolution and content).

Examples here must remain:
- synthetic, downsampled, generalized, or otherwise policy-safe,
- and must demonstrate how the system warns/redacts when needed.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Created remote-sensing explainability examples README: example suite scope, artifact contracts, STAC/DCAT/PROV packaging patterns, Focus Mode evidence integration, and CI-safe governance rules. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🛰️ Remote Sensing Explainability Examples · Governed for Integrity

[⬅️ Examples Index](../README.md) · [📘 Explainability Docs](../../README.md) · [🧠 AI Tools](../../../../README.md) · [🛡 Governance](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

