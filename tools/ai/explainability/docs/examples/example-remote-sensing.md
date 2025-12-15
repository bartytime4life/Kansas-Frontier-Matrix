---
title: "🧪 KFM — Explainability Example: Remote Sensing (Synthetic)"
path: "tools/ai/explainability/docs/examples/example-remote-sensing.md"

version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:tools-ai-explainability-example-remote-sensing:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-explainability-example-remote-sensing"
event_source_id: "ledger:tools/ai/explainability/docs/examples/example-remote-sensing.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

# Update these refs to your governed “current release” bundle when available.
sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

json_schema_ref: "../../../../../schemas/json/tools-ai-explainability-example-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/tools-ai-explainability-example-v11.shape.ttl"

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

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next explainability platform update"

provenance_chain:
  - "tools/ai/explainability/docs/examples/README.md@v11.2.6"
---

<div align="center">

# 🧪 **KFM Explainability Example — Remote Sensing (Synthetic)**
`tools/ai/explainability/docs/examples/example-remote-sensing.md`

**Purpose**  
Demonstrate a **policy-safe remote sensing explainability bundle** (e.g., Grad-CAM / saliency-style overlays and band contributions) using **synthetic values only**, with KFM’s metadata, integrity placeholders, and governance constraints.

</div>

---

## 📘 Overview

This document is a **toy example** showing how KFM can represent explainability for:

- image classification,
- semantic segmentation,
- or raster regression (continuous outputs),

without exposing raw imagery, sensitive locations, or restricted coordinates.

### What this example demonstrates

- A **manifest** describing an explainability artifact set:
  - identity, scope, safety flags
  - inventory of artifacts and assets (with checksum placeholders)
- A **remote sensing explanation payload** that includes:
  - band/channel contribution summary (aggregate-only)
  - spatial attribution summary (reference-first)
  - governance flags and reason codes
  - STAC/DCAT/PROV-friendly references (IDs + paths, not embedded datasets)

### What this example intentionally avoids

- Any real pixel data or real satellite imagery
- Any protected locations or precise coordinates
- Any sensitive overlays that could become a leakage channel
- Any PII
- Any secrets/tokens/credentials

**Rule of thumb:** remote sensing explainability MUST be **reference-first** and **aggregation-first**.

---

## 🗂️ Directory Layout

This file lives in the explainability examples folder:

~~~text
📁 tools/
└── 🧠 ai/
    └── 🧩 explainability/
        └── 📁 docs/
            └── 📁 examples/
                ├── 📄 README.md
                ├── 📄 example-tabular.md
                └── 📄 example-remote-sensing.md        # This file
~~~

Recommended pairing for a self-contained example bundle (create if/when you want a runnable demo set):

~~~text
📁 tools/
└── 🧠 ai/
    └── 🧩 explainability/
        └── 📁 docs/
            └── 📁 examples/
                └── 📁 remote_sensing/
                    ├── 🧾 example_manifest.json        # Artifact inventory + safety flags (synthetic)
                    ├── 🧾 explanation.json             # Band + spatial attribution summary (synthetic)
                    ├── 🧾 governance_flags.json        # Reason codes + display eligibility (synthetic)
                    ├── 🧾 checksums.sha256             # Integrity placeholders (optional)
                    └── 📄 notes.md                     # What the example demonstrates (synthetic)
~~~

**Normative rule:** examples in `docs/examples/` MUST remain small and synthetic; real run artifacts belong under governed run folders (e.g., `mcp/experiments/<run-id>/...`).

---

## 🧭 Context

### When remote sensing explainability is used in KFM

Remote sensing explainability is typically required for:

- land cover classification and change detection,
- hazard mapping (flood/wildfire proxies),
- vegetation/phenology modeling,
- surface temperature / drought proxy modeling,
- segmentation masks (e.g., water/vegetation/urban extraction),
- QA of sensor transitions and preprocessing changes.

### What “spatial attribution” means here

Spatial attribution answers questions like:

- “Which regions of the input most influenced the output?”
- “Which bands/indices contributed most?”
- “Is the model relying on artifacts (cloud edges, tile seams)?”

KFM treats these explanations as:

- diagnostic evidence,
- not causal proof,
- and not authorization to reveal restricted locations or details.

### Safety notes specific to spatial outputs

Remote sensing explanations can introduce leakage risks:

- overlays can reveal exact areas of interest,
- high-resolution masks can expose protected sites,
- “top contributing area” can become a sensitive locator.

Therefore, KFM explanation artifacts SHOULD:

- avoid embedding raw overlays in public-facing docs,
- use coarse summaries (tiles/regions/classes) where policy requires,
- include explicit governance flags for display eligibility.

---

## 🗺️ Diagrams

### Remote sensing explainability lifecycle (conceptual)

~~~mermaid
flowchart TD
  A["Model inference/evaluation<br/>model_id + version/hash"] --> B["Resolve raster asset refs<br/>(STAC item + asset keys)"]
  B --> C["Compute explainability<br/>(band contributions + spatial attribution)"]
  C --> D["Safety gates<br/>(mask/suppress; no restricted coords)"]
  D --> E["Validate<br/>(schema + integrity + determinism)"]
  E --> F["Store artifacts under run_id<br/>(mcp/experiments/<run-id>/...)"]
  F --> G["Register refs<br/>(model registry + provenance pointers)"]
  G --> H["Render (if allowed)<br/>(Focus Mode / Map UI overlays)"]
~~~

Accessibility note: the flow resolves STAC asset references, computes attributions, applies safety gates, validates, stores, registers, and optionally renders.

---

## 📦 Data & Metadata

This section shows **illustrative** JSON shapes. Replace placeholder IDs/hashes with real governed values in real runs.

### Example 1: `example_manifest.json` (illustrative)

~~~json
{
  "example_id": "explainability_example_remote_sensing_v1",
  "example_version": "11.2.6",
  "example_kind": "remote_sensing",
  "created": "2025-12-15T00:00:00Z",

  "model": {
    "model_id": "demo_landcover_segmenter",
    "model_version": "demo",
    "model_hash": "<sha256>"
  },

  "dataset": {
    "dataset_id": "stac:kfm:collection:demo-remote-sensing",
    "dataset_version": "demo"
  },

  "inputs": {
    "stac_item_id": "stac:kfm:item:demo-tile-0001",
    "assets_used": [
      { "asset_key": "cog_rgb", "media_type": "image/tiff; application=geotiff" },
      { "asset_key": "cog_nir", "media_type": "image/tiff; application=geotiff" }
    ],
    "notes": "Synthetic IDs only; no real imagery."
  },

  "config": {
    "explainer_profile_ref": "tools/ai/configs/domains/remote-sensing/explainability.json",
    "config_sha256": "<sha256>"
  },

  "artifacts": [
    { "path": "explanation.json", "media_type": "application/json", "sha256": "<sha256>" },
    { "path": "governance_flags.json", "media_type": "application/json", "sha256": "<sha256>" }
  ],

  "safety": {
    "classification": "Public",
    "care_label": "Public · Low-Risk",
    "contains_pii": false,
    "contains_secrets": false,
    "contains_sensitive_locations": false,
    "spatial_precision": "synthetic_only",
    "small_group_suppression_applied": false
  },

  "refs": {
    "telemetry_ref": "mcp/experiments/<run-id>/telemetry.json",
    "provenance_bundle_ref": "mcp/experiments/<run-id>/provenance_bundle.jsonld"
  },

  "notes": "Structural example only. Demonstrates how to reference STAC assets and record explainability without embedding imagery."
}
~~~

### Example 2: `governance_flags.json` (illustrative)

This file demonstrates how an explanation can be “computed but not displayable” depending on governance.

~~~json
{
  "display_eligibility": {
    "ui_allowed": true,
    "reasons_if_denied": []
  },
  "safety_controls": {
    "mask_sensitive_geometries": true,
    "suppress_small_groups": true,
    "min_group_n": 50
  },
  "policy": {
    "classification": "Public",
    "care_label": "Public · Low-Risk",
    "redaction_applied": false,
    "suppression_applied": false,
    "reason_codes": []
  }
}
~~~

### Example 3: `explanation.json` (illustrative, remote sensing)

This payload avoids embedding imagery. It uses:

- band importance (normalized)
- spatial attribution described by **references** + small, synthetic summaries
- optional overlay asset reference (synthetic path only)

~~~json
{
  "explanation_set_id": "demo_remote_sensing_explainability_v1",
  "schema_version": "11.2.6",
  "created": "2025-12-15T00:00:00Z",

  "scope": {
    "model_id": "demo_landcover_segmenter",
    "model_version": "demo",
    "task_type": "segmentation",
    "dataset_id": "stac:kfm:collection:demo-remote-sensing",
    "dataset_version": "demo",
    "stac_item_id": "stac:kfm:item:demo-tile-0001",
    "assets_used": ["cog_rgb", "cog_nir"]
  },

  "method": {
    "explainer_id": "grad_cam_like",
    "explainer_version": "1.0.0",
    "notes": "Synthetic demonstration. No real imagery or overlays are embedded."
  },

  "band_contributions": {
    "normalization": "sum_to_1",
    "bands": [
      { "band": "R", "importance": 0.22 },
      { "band": "G", "importance": 0.18 },
      { "band": "B", "importance": 0.15 },
      { "band": "NIR", "importance": 0.45 }
    ],
    "interpretation": "Higher importance indicates greater average contribution magnitude across the tile."
  },

  "spatial_attribution": {
    "attribution_kind": "heatmap_reference",
    "resolution_class": "demo_coarse_grid",
    "summary_stats": {
      "mean": 0.10,
      "p50": 0.08,
      "p95": 0.22
    },
    "top_regions": [
      { "region_id": "grid_cell_03_04", "score": 0.31 },
      { "region_id": "grid_cell_03_05", "score": 0.27 }
    ],
    "overlay_asset_ref": {
      "path": "mcp/experiments/<run-id>/assets/demo_saliency_overlay.png",
      "media_type": "image/png",
      "sha256": "<sha256>",
      "display_note": "Synthetic-only asset path shown as a reference; do not embed real overlays in docs/examples."
    }
  },

  "outputs": {
    "predicted_classes": [
      { "class_id": "water", "coverage_fraction": 0.10 },
      { "class_id": "vegetation", "coverage_fraction": 0.65 },
      { "class_id": "built", "coverage_fraction": 0.25 }
    ],
    "coverage_semantics": "fractions_sum_to_1"
  },

  "quality": {
    "explainability_coverage_score": 0.98,
    "warnings": [],
    "limitations": [
      "Spatial attribution is not causal.",
      "Synthetic demonstration only.",
      "Real overlays require governance gating to prevent leakage."
    ]
  },

  "governance": {
    "classification": "Public",
    "care_label": "Public · Low-Risk",
    "redaction_applied": false,
    "suppression_applied": false,
    "reason_codes": []
  },

  "refs": {
    "baseline_ref": "mcp/experiments/<baseline-run-id>/baseline.json#sha256:<sha256>",
    "window_ref": "mcp/experiments/<run-id>/window_summary.json#sha256:<sha256>",
    "telemetry_ref": "mcp/experiments/<run-id>/telemetry.json",
    "provenance_bundle_ref": "mcp/experiments/<run-id>/provenance_bundle.jsonld"
  }
}
~~~

### Human-readable interpretation (safe)

- In this synthetic example, the **NIR band** is the largest global contributor.
- The spatial attribution indicates a few coarse grid regions contribute more strongly than others.
- The “overlay” is referenced (not embedded) to prevent leakage paths.

---

## 🧠 Story Node & Focus Mode Integration

### How remote sensing explanations can be shown safely

For UI contexts (MapLibre/Cesium/Story Nodes), explanations should be:

- displayed as **coarse overlays** or aggregated summaries when needed
- gated by permission and safety classification
- delivered via API/catalog references, not direct file-system access

Recommended UI fields for safe display:

- top band contributions (normalized)
- attribution summary stats (mean/p95)
- top regions by coarse region ID (not precise coordinates)
- governance banner:
  - “explanation withheld” with reason codes if not displayable

### Hard constraint: no direct graph access

Even if a model uses graph/context signals, the UI must consume explainability through governed APIs and catalogs, not direct graph queries.

---

## 🧪 Validation & CI/CD

### Example validation checklist (recommended)

For this example bundle (and for real runs), validation SHOULD include:

- JSON validity for `example_manifest.json`, `explanation.json`, `governance_flags.json`
- schema validation (when the governed schema exists)
- determinism checks:
  - stable ordering for arrays (bands, regions, classes)
  - stable rounding/precision rules (document if applied)
- safety checks:
  - no secrets
  - no PII
  - no protected-site coordinates
  - no embedded imagery/pixels
- reference completeness:
  - model identity present
  - dataset/STAC identity present
  - config ref + config hash present
  - telemetry/provenance pointers present (or intentionally omitted for docs-only examples)

### Fail-closed guidance (normative for governed runs)

If any of these are missing or ambiguous in a governed environment:

- classification/sensitivity metadata,
- dataset/model identity,
- config reference/hash,
- safety scan results,

…then the explainability output MUST be treated as **non-displayable**, and certification-dependent flows should fail closed.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC alignment (recommended)

Remote sensing explainability frequently ties to STAC Items and assets:

- `stac_item_id` identifies the input tile/scene
- `assets_used` references the specific assets (e.g., `cog_rgb`, `cog_nir`)
- explanation overlays can be treated as additional assets:
  - `media_type: image/png` (or `image/webp`) for overlays
  - checksums recorded for integrity

**Reference-first rule:** store STAC IDs and asset keys; do not embed item JSON inside explainability payloads unless required.

### DCAT alignment (recommended)

If explainability outputs are packaged as audit distributions:

- publish a policy-safe “explainability report” distribution
- link it to the dataset and model card (by ID and version)
- keep overlays gated if they can reveal sensitive patterns

### PROV alignment (recommended)

Explainability computation should be provable:

- `prov:Activity` = “explainability_computation”
- `prov:Entity` = model artifact, STAC item reference, explanation artifact set
- `prov:used` = inputs + config entity
- `prov:generated` = explanation artifacts + overlay assets
- `prov:wasAssociatedWith` = CI runner or governed operator role

---

## ⚖ FAIR+CARE & Governance

### Why remote sensing explainability needs extra care

Even “environmental” remote sensing can intersect with:

- culturally sensitive sites,
- restricted infrastructure,
- or rare events that enable location inference.

Explainability can amplify that risk via overlays and saliency maps.

Therefore, KFM requires:

- aggregation-first summaries (band contributions, coarse region scores)
- governance flags for display eligibility
- suppression/redaction controls for sensitive contexts
- strict separation between:
  - computed artifacts (stored in governed run spaces),
  - and public-safe summaries (what is actually shown)

### Training prohibition

This example and all explainability artifacts MUST NOT be used as AI training data.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Added synthetic remote sensing explainability example: STAC-referenced inputs, band contribution summaries, reference-first spatial attribution, governance display flags, and CI validation checklist (no embedded imagery). |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🧪 Remote Sensing Explainability Example · Synthetic · Governed for Integrity

[⬅️ Examples Index](./README.md) ·
[⬅️ Explainability Docs](../README.md) ·
[⬅️ Explainability](../../README.md) ·
[🛡 Governance](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

