---
title: "🧪 Kansas Frontier Matrix — Geo Generalization CI Scenario Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/data-generalization/geo/examples/ci-scenarios/README.md"

version: "v11.0.0"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Examples Index"
intent: "geo-sensitive-generalization-ci-scenarios"
semantic_document_id: "kfm-doc-geo-sensitive-generalization-ci-scenarios"
doc_uuid: "urn:kfm:docs:heritage:data-generalization-geo-ci-scenarios:v11.0.0"
event_source_id: "ledger:kfm:doc:heritage:data-generalization-geo-ci-scenarios:v11.0.0"
immutability_status: "version-pinned"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/data-generalization-geo-ci-scenarios-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY-NC 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "geo-sensitive-data-generalization"
  applies_to:
    - "examples"
    - "ci"
    - "ingest"
    - "etl"
    - "stac"
    - "dcat"
    - "graph"
    - "api"
    - "frontend"
    - "maplibre"
    - "cesium"
    - "story-nodes"
    - "focus-mode"
    - "geoprivacy"
    - "archaeology"
    - "ecology"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

fair_category: "F1-A1-I2-R3"
care_label: "Restricted / High-Sensitivity"
sensitivity: "Cultural, archaeological, ecological (high)"
sensitivity_level: "High"
public_exposure_risk: "High"
classification: "Restricted"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by next geo-generalization CI examples revision"

provenance_chain:
  - "docs/standards/data-generalization/README.md@v11.0.0"
  - "docs/standards/data-generalization/geo/README.md@v11.0.0"
  - "docs/standards/data-generalization/geo/examples/README.md@v11.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

story_node_refs: []

ai_training_inclusion: false
ai_focusmode_usage: "Restricted / Governance-Only"
ai_transform_permissions:
  - "summary"
  - "index-generation"
ai_transform_prohibited:
  - "content-alteration"
  - "sensitive-detail-expansion"
  - "governance-override"
  - "narrative-fabrication"

transform_registry:
  allowed:
    - summary
    - index-generation
  prohibited:
    - content-alteration
    - sensitive-detail-expansion
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
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "📦 CI Scenario Groups"
    - "🧭 Context"
    - "🧪 Validation & CI/CD"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"
  - "sensitivity-check"

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

# 🧪 **Kansas Frontier Matrix — Geo Generalization CI Scenario Examples (v11.0.0)**  
`docs/standards/data-generalization/geo/examples/ci-scenarios/README.md`  

**Purpose**  
Provide a structured index of **geo‑level CI scenarios** that test sensitive‑site generalization in KFM: H3 masking, donut vs H3 behavior, zoom‑level enforcement, anti‑triangulation safety, and cross‑layer leakage checks.  
These examples power automated pipelines that ensure no KFM deployment can accidentally expose protected locations, even under complex layer combinations or UI changes.

</div>

---

## 📘 Overview

This file catalogs **example‑driven CI scenarios** for sensitive geo generalization, aligned with:

- 🏺 **Sensitive Site Data Generalization & CARE Governance Guide**  
- 🗺️ **Geo Generalization Standard for Sensitive Sites**  
- 🛡️ **Geoprivacy & Cultural-Safety Masking Standard**  
- 🏺 **Archaeology & Indigenous Sensitive Location Standard**  

The scenarios here are:

- **Non‑normative** as policy, but **normative** as test patterns:  
  if a real dataset behaves “worse” (less protective) than these examples, CI should fail.  
- Built as **fixtures** and **golden outputs** that encode:

  - Correct H3 resolutions by sensitivity level.  
  - Correct zoom constraints by sensitivity level.  
  - Correct STAC/DCAT/PROV metadata for generalized layers.  
  - Correct failure modes for unsafe configurations (triangulation, zoom leakage, mixed layers).

---

## 🗂️ Directory Layout

```text
📂 docs/
└── 📂 standards/
    └── 📂 data-generalization/
        └── 📂 geo/
            └── 📂 examples/
                ├── 📄 README.md                  # Geo generalization examples index
                └── 📂 ci-scenarios/
                    📄 README.md                  # ← This file
                    📄 anti_triangulation.md      # Multi-layer triangulation risk scenarios
                    📄 zoom_leakage.md            # Zoom-level and tile precision leakage tests
                    📄 mixed_layers.md            # Mixed sensitive + non-sensitive layer scenarios
```

Author rules:

- New CI scenario files must be added under `ci-scenarios/` and referenced in this layout.  
- Scenario docs must:

  - Clearly explain **what risk** they test (e.g., triangulation, zoom leakage).  
  - Reference the relevant governing standards.  
  - Use **fake or generalized** geometries only — never real sensitive coordinates.

---

## 📦 CI Scenario Groups

### 1. `anti_triangulation.md` — Multi-layer safety

Focus:

- Scenarios where **multiple independently generalized layers**, when combined, might reveal more precise locations than any single layer.  

Examples include:

- Overlapping H3 heritage cells with:

  - Infrastructure layers (roads, parcels).  
  - Hydrology layers (streams, confluences).  

- Patterns where the intersection of:

  - A few generalized hexes,  
  - A limited set of plausible site types, and  
  - Known infrastructure,  

could narrow candidate locations to a small area.

Tests should:

- Encode **expected failure conditions** (e.g., no hex with site_count=1 across multi-layer intersections).  
- Provide **golden outputs** where masking/generalization has been strengthened enough to pass.

---

### 2. `zoom_leakage.md` — Zoom & tiling constraints

Focus:

- Scenarios where tile endpoints or frontend styles allow users to:

  - Zoom far beyond intended levels, making generalized regions appear site‑precise.  
  - Misinterpret a coarse H3 cell as a single point due to marker styling.

Examples include:

- A tile endpoint intended for `maxzoom: 8` that actually serves tiles up to z=18.  
- A style that replaces H3 polygons with centered icons at high zoom.

Tests should:

- Examine **tile metadata** (STAC assets, TMS) and **styles** (where they are declarative) to verify that:

  - `minzoom`/`maxzoom` in STAC / API contracts are respected.  
  - Sensitive layers never render at zoom levels beyond governance limits.  
  - Legend text clearly states that regions are generalized.

---

### 3. `mixed_layers.md` — Sensitive + non-sensitive coexistence

Focus:

- Scenarios where a map/scene mixes:

  - Sensitive generalized layers, and  
  - Non‑sensitive high‑precision layers,  

in ways that could undermine masking.

Examples include:

- Generalized heritage hexes overlaid on parcel‑level or building‑footprint layers.  
- Coarse ecological masks combined with high‑precision access roads.  

Tests should:

- Define **allowed** combinations (e.g., heritage r5 with county‑scale boundaries).  
- Flag unsafe combinations where precision mismatch enables inference.  
- Encode expectations that frontends should:

  - Soften or hide sensitive layers when zoomed into high‑precision context, or  
  - Limit zoom globally when sensitive layers are visible.

---

## 🧭 Context

These CI scenarios are tightly coupled to:

- **Geo generalization implementation** (`geo/README.md`).  
- **Geoprivacy masking** (donut algorithm & sensitive labels).  
- **STAC geo spec** (where generalization is recorded in metadata).  
- **Story Node & Focus Mode** (where generalized spatial elements show up as narrative overlays).

They are not standalone:

- A scenario is only valid when interpreted through the standards it references.  
- If a standard changes (e.g., H3 defaults, zoom limits), these examples must be updated in the same or a follow‑up PR.

---

## 🧪 Validation & CI/CD

Typical consumption of these scenarios:

- **Unit tests**:  
  Parse scenario definitions and run masking/generalization code against known inputs, verifying results match golden outputs.

- **Integration tests**:  
  Spin up minimal tile / API endpoints using scenario configurations and assert:

  - HTTP responses are absent where layers should be unavailable.  
  - `minzoom`/`maxzoom` and H3 resolution constraints are respected.  
  - STAC and DCAT metadata match expectations.

- **Static analysis**:  
  Inspect styles, STAC items, and DCAT entries referenced by scenarios to ensure they adhere to the rules encoded here.

A PR is **blocked** if:

- Scenario fixtures detect a regression (e.g., triangulation risk reappears).  
- Zoom leakage examples show that a change would expose more detail than allowed.  
- Mixed‑layer examples reveal new unsafe layer combinations.

---

## 🕰️ Version History

| Version | Date       | Status            | Summary                                                                                                  |
|--------:|------------|-------------------|----------------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-12-06 | Active / Enforced | Initial CI scenario example index for geo‑level sensitive generalization; aligned with v11 geo standards.|

---

<div align="center">

🧪 **Kansas Frontier Matrix — Geo Generalization CI Scenario Examples (v11.0.0)**  
“If the tests don’t fail when they should, the sites are not safe.”

CC‑BY‑NC 4.0 · FAIR+CARE Council · MCP‑DL v6.3  

[⬅ Back to Geo Examples](../README.md) · [🗺 Geo Generalization Standard](../../README.md) · [⚖ Governance](../../../../governance/ROOT-GOVERNANCE.md)

</div>

