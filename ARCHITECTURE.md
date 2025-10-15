```yaml
name: "💡 Feature Request"
description: "Propose a feature or enhancement — documented, versioned, and reproducible"
title: "[Feature]: <feature name> — <component/domain>"
labels:
  - enhancement
  - needs-triage
assignees:
  - kfm-architecture
  - kfm-data

# KFM metadata
# version: v2.3.0
# last_updated: 2025-10-15
# owners: @kfm-architecture @kfm-data

body:
  - type: markdown
    attributes:
      value: |
        ## 💡 Feature Overview
        *“Every Feature Builds the Future. Every Change is Reproducible.”*

  - type: input
    id: feature_name
    attributes:
      label: Feature Name
      placeholder: "Slope Classification Enhancement for Terrain Pipeline"
    validations:
      required: true

  - type: input
    id: component_module
    attributes:
      label: Primary Component / Module
      placeholder: "terrain_pipeline.py | graph_ingest.py | stac-validate.yml | web/config/layers.json"
    validations:
      required: true

  - type: dropdown
    id: feature_type
    attributes:
      label: Feature Type
      options: ["Backend","Frontend","Cross-Layer","Infrastructure","Docs/SOP"]
    validations:
      required: true

  - type: dropdown
    id: impact
    attributes:
      label: Impact (Breaking?)
      options: ["Non-Breaking","Breaking"]
    validations:
      required: true

  - type: input
    id: scope_affected
    attributes:
      label: Scope / Affected Areas
      placeholder: "ETL (terrain), Web Map layers, STAC schema, CI workflow"
    validations:
      required: true

  - type: input
    id: target_window
    attributes:
      label: Target Release / Timeline
      placeholder: "v2.4.0 — October; or ‘next minor’"
    validations:
      required: true

  - type: input
    id: spec_or_adr_url
    attributes:
      label: Spec / ADR Link(s)
      placeholder: "/docs/adr/0007-slope-classification.md; design doc URL"

  - type: input
    id: steward
    attributes:
      label: Owner / Steward
      placeholder: "@kfm-architecture · @kfm-data (or individual)"

  - type: markdown
    attributes:
      value: "## 🌐 Design Provenance"

  - type: textarea
    id: provenance
    attributes:
      label: Design Provenance
      description: "Official internal/external references, rationale, screenshots/quotes, standards alignment"
      placeholder: |
        - ADR: /docs/adr/0007-slope-classification.md
        - SOP: /docs/sop/terrain_pipeline.md#slope
        - Standards: STAC 1.0.x fields, OWL-Time, CIDOC CRM tags
        - Rationale: why now; alternatives considered; decision summary
    validations:
      required: true

  - type: dropdown
    id: integration_scope
    attributes:
      label: Integration Scope
      options: ["Backend (ETL / AI / Graph)","Frontend (Map / Timeline / UI)","Cross-Layer (Full-stack)","Infrastructure (CI/CD / Deployment)","Documentation / SOP"]
    validations:
      required: true

  - type: textarea
    id: formats
    attributes:
      label: Artifacts / Outputs
      placeholder: ".py, .yml, .json, .md, .cog.tif, GeoJSON, OpenAPI/spec changes"
    validations:
      required: true

  - type: input
    id: interfaces
    attributes:
      label: Interfaces / Contracts
      placeholder: "Function signatures, API routes, CLI flags, config keys; note any breaking behavior"
    validations:
      required: true

  - type: dropdown
    id: update_frequency
    attributes:
      label: Release Cadence
      options: ["Static/One-off","Irregular/On-Demand","Quarterly","Monthly","Weekly","Daily"]
    validations:
      required: true

  - type: textarea
    id: quality
    attributes:
      label: QA Strategy / References
      placeholder: "Unit/integration tests, golden datasets, regression criteria, perf thresholds; link to test plan"

  - type: markdown
    attributes:
      value: "## 🧩 Intended Integration"

  - type: input
    id: pipeline
    attributes:
      label: Pipeline / Component Target
      placeholder: "terrain_pipeline.py, src/graph/ingest.py, web/config/layers.json"
    validations:
      required: true

  - type: dropdown
    id: domain
    attributes:
      label: Feature Domain
      options: ["Terrain","Hydrology","Hazards","Climate","Landcover","Knowledge Graph","Web UI","API","Text / AI / NLP","Metadata / Governance","CI/CD","Other"]
    validations:
      required: true

  - type: dropdown
    id: stac_linkage
    attributes:
      label: Schema / Standard Linkage
      options: ["Yes — new schema/extension","Yes — changes in existing schema","No/Not applicable"]
    validations:
      required: true

  - type: dropdown
    id: visualization
    attributes:
      label: Visualization Layer
      options: ["Web Map","Timeline","Story Map","3D Scene","API only"]
    validations:
      required: true

  - type: input
    id: ontology
    attributes:
      label: Semantic Ontology Tag(s)
      placeholder: "CIDOC CRM class, OWL-Time interval, PeriodO ID"

  - type: markdown
    attributes:
      value: "## 🧠 Metadata & Schema"

  - type: textarea
    id: attributes_cols
    attributes:
      label: Config Keys / Attributes
      description: "List new/changed config keys, flags, or attributes"
    validations:
      required: true

  - type: textarea
    id: units
    attributes:
      label: Codes / Units / Flags
      placeholder: "e.g., class bins, enum values, boolean flags"
    validations:
      required: true

  - type: input
    id: schema_url
    attributes:
      label: Schema / Spec Source URL
      placeholder: "Link to OpenAPI, JSON Schema, or internal spec doc"

  - type: input
    id: encoding
    attributes:
      label: Encoding / Format
      placeholder: "UTF-8 / YAML / JSON / GeoJSON"
    validations:
      required: true

  - type: textarea
    id: example_snippet
    attributes:
      label: Example Snippet
      description: "Small JSON/YAML snippet (config, API payload, or output)"
      render: json

  - type: dropdown
    id: metadata_standard
    attributes:
      label: Documentation / Spec Standard
      options: ["ADR","SOP","OpenAPI","STAC 1.0.x","Other/Unknown"]
    validations:
      required: true

  - type: markdown
    attributes:
      value: "## 🧮 Validation Requirements"

  - type: checkboxes
    id: validation
    attributes:
      label: Pre-Merge Checklist
      options:
        - label: Unit & integration tests added and passing
          required: true
        - label: STAC/schema validation passes (make stac-validate / schema-check)
          required: true
        - label: ETL reproducibility confirmed (deterministic outputs + checksums)
          required: true
        - label: License & data compliance verified (no restricted content)
          required: true
        - label: Docs updated under /docs/sop/ or /docs/adr/
          required: true
        - label: Performance checked (meets target thresholds)
          required: true
        - label: Version bump recorded in CHANGELOG.md
          required: true

  - type: markdown
    attributes:
      value: "## ⚙️ Implementation Plan (Optional)"

  - type: textarea
    id: impl_plan
    attributes:
      label: Steps & Owners
      placeholder: |
        1) Design review — Owner …
        2) Implement changes — Owner …
        3) Add tests — Owner …
        4) Update docs/ADR/SOP — Owner …
        5) Validate schema — Owner …
        6) Perf/QA gates — Owner …
        7) Release & comms — Owner …

  - type: markdown
    attributes:
      value: "## 🧭 Versioning & Governance"

  - type: textarea
    id: versioning
    attributes:
      label: Versioning Summary (SemVer + Schema)
      placeholder: |
        | Scope               | Current | Proposed | Reason / Trigger       |
        | :------------------ | :------ | :------- | :--------------------- |
        | Component/Module    | v2.3.0  | v2.4.0   | feature enhancement    |
        | CI Workflow         | v1.7.1  | v1.8.0   | new validation step    |
        | Docs / SOP          | v1.2.0  | v1.3.0   | process updated        |
      render: markdown

  - type: markdown
    attributes:
      value: "## ✅ MCP Compliance"

  - type: checkboxes
    id: mcp
    attributes:
      label: MCP Principles
      options:
        - label: Documentation-first — feature fully described with provenance
          required: true
        - label: Reproducibility — deterministic steps & checksums defined
          required: true
        - label: Open Standards — interoperable formats/specs used
          required: true
        - label: Provenance — ADR/SOP updates and traceable diffs
          required: true
        - label: Auditability — CI validation steps reproducible & archived
          required: true
        - label: Versioning — repo SemVer & schema versions updated
          required: true

  - type: markdown
    attributes:
      value: "## 🧩 Related Issues / Attachments"

  - type: textarea
    id: related
    attributes:
      label: Related Issues / PRs
      placeholder: |
        - Related: #45 (ETL refactor)
        - Dependent: #102 (web map overlay support)
        - Supersedes: #37 (legacy pipeline flag)
        - Linked Data Request: #201 (terrain COG integration)

  - type: textarea
    id: attachments
    attributes:
      label: Attachments
      description: "Diagrams, screenshots, or POC links"
      placeholder: |
        architecture_diagram.png — workflow impact
        feature_diff.json — config patch example
        prototype.mp4 — UI demo

  - type: textarea
    id: notes
    attributes:
      label: Additional Notes
      description: "Visuals, risks, rollout plan, comms, or follow-up tasks"
```
