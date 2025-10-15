```yaml
name: "💡 Feature Request"
description: "Propose a new feature or enhancement — documented, versioned, and reproducible"
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
      label: Impact Level
      options: ["Low","Moderate","High","Breaking"]
    validations:
      required: true

  - type: input
    id: related_scope
    attributes:
      label: Related Scope / Module
      placeholder: "ETL (terrain), Web Map layers, STAC schema, CI workflow"
    validations:
      required: true

  - type: input
    id: release_target
    attributes:
      label: Target Release / Timeline
      placeholder: "v2.4.0 — October; or ‘next minor’"
    validations:
      required: true

  - type: input
    id: spec_ref
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
    id: artifacts
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
    id: release_cadence
    attributes:
      label: Release Cadence
      options: ["Static/One-off","Irregular/On-Demand","Quarterly","Monthly","Weekly","Daily"]
    validations:
      required: true

  - type: textarea
    id: qa_strategy
    attributes:
      label: QA Strategy / References
      placeholder: "Unit/integration tests, golden datasets, regression criteria, perf thresholds; link to test plan"

  - type: markdown
    attributes:
      value: "## 🎯 Motivation & Current Limitation"

  - type: textarea
    id: motivation
    attributes:
      label: Motivation / Use Case
      placeholder: "Explain the problem this feature solves and who benefits (users, pipelines, governance)."
    validations:
      required: true

  - type: textarea
    id: limitation
    attributes:
      label: Current Limitation
      placeholder: "Describe the gap, constraints, or pain points in current behavior or architecture."
    validations:
      required: true

  - type: markdown
    attributes:
      value: "## ⚙️ Proposed Implementation"

  - type: textarea
    id: proposal
    attributes:
      label: Proposed Implementation
      description: "Include technical specifics, workflow changes, architecture impacts, and rollout."
      placeholder: |
        - Extend terrain_pipeline.py with --add-slope-classification
        - Generate slope class COG and add STAC property slope_class_version
        - Add layers.json entry with gradient style
        - Update ADR/SOP; add unit/integration tests; validate STAC; perf gate
    validations:
      required: true

  - type: checkboxes
    id: change_type
    attributes:
      label: Change Type(s)
      options:
        - label: Add new module/component
        - label: Modify ETL pipeline step
        - label: Extend STAC metadata/schema
        - label: Create new visualization layer
        - label: Update documentation / SOP
        - label: Other (describe in proposal)

  - type: markdown
    attributes:
      value: "## 🧮 Expected Outcome / Metrics"

  - type: textarea
    id: expected_outcome
    attributes:
      label: Expected Outcome / Metrics
      placeholder: |
        | Metric          | Target                                        |
        | :-------------- | :---------------------------------------------|
        | Data Quality    | slope_class attribute present; STAC fields updated |
        | Reproducibility | Deterministic outputs; SOP updated            |
        | Usability       | Map layer toggle + legend                     |
        | Performance     | < +5% runtime impact                          |
    validations:
      required: true

  - type: markdown
    attributes:
      value: "## 🧩 Implementation Plan"

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
      label: Related Issues / PRs / Data Requests
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
