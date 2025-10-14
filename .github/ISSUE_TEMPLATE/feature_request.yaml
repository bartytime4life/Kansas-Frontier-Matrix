name: "💡 Feature Request"
description: "Propose a feature/enhancement — documented, versioned, and reproducible"
title: "[Feature]: <short title>"
labels:
  - enhancement
  - needs-triage
assignees:
  - kfm-architecture
  - kfm-data
# KFM metadata
# version: v2.2.0
# last_updated: 2025-10-13
# owners: @kfm-architecture @kfm-data

body:
  - type: markdown
    attributes:
      value: |
        # 💡 Kansas Frontier Matrix — Feature Request
        *“Every Feature Builds the Future · Every Change is Reproducible.”*
        Please provide clear context, the problem to solve, and measurable outcomes.

  - type: textarea
    id: summary
    attributes:
      label: 💡 Summary
      description: Describe the feature, enhancement, or optimization and expected benefits.
      placeholder: "Add slope classification to terrain pipeline outputs and enable gradient visualization in MapLibre."
    validations:
      required: true

  - type: markdown
    attributes:
      value: "## 🎯 Motivation / Use Case"

  - type: dropdown
    id: domain
    attributes:
      label: Domain / Module
      options:
        - Terrain
        - Hydrology
        - Climate
        - Hazards
        - Landcover
        - Knowledge Graph
        - Web UI
        - API
        - Text / AI / NLP
        - Metadata / Governance
        - CI/CD
        - Other
    validations:
      required: true

  - type: input
    id: component
    attributes:
      label: Pipeline / Component
      placeholder: "terrain_pipeline.py | graph_ingest.py | stac-validate.yml | web/config/layers.json"
    validations:
      required: true

  - type: textarea
    id: use_case
    attributes:
      label: Use Case
      placeholder: "Enable classification maps for slope ranges to support hazard & trail planning."
    validations:
      required: true

  - type: textarea
    id: limitation
    attributes:
      label: Current Limitation
      placeholder: "No slope visualization or classification available."
    validations:
      required: true

  - type: textarea
    id: dependencies
    attributes:
      label: Dependencies
      description: Tools, APIs, libraries, schema updates, permissions
      placeholder: "WhiteboxTools v2.2+, STAC schema update, web layer style"
    validations:
      required: false

  - type: markdown
    attributes:
      value: "## 🧩 Proposed Solution"

  - type: textarea
    id: solution
    attributes:
      label: Proposed Implementation
      description: Include technical specifics, workflow changes, and architecture impacts.
      placeholder: |
        - Extend terrain_pipeline.py with --add-slope-classification
        - Generate slope class COG + STAC property `slope_class_version`
        - Add `layers.json` entry with gradient style
      render: markdown
    validations:
      required: true

  - type: checkboxes
    id: change_types
    attributes:
      label: Change Type(s)
      options:
        - label: Add new data transformation module
        - label: Modify ETL pipeline step
        - label: Extend STAC metadata/schema
        - label: Create new visualization layer
        - label: Update documentation / SOP
        - label: Other (describe in solution)

  - type: markdown
    attributes:
      value: "## 🧮 Expected Outcome"

  - type: textarea
    id: outcome
    attributes:
      label: Expected Outcome / Metrics
      placeholder: |
        | Metric              | Target                                   |
        | :------------------ | :----------------------------------------|
        | Data Quality        | Add slope class attr; STAC fields updated|
        | Reproducibility     | Deterministic outputs; SOP updated       |
        | Usability           | Map layer toggle + legend                |
        | Performance         | < +5% runtime impact                     |
      render: markdown
    validations:
      required: true

  - type: markdown
    attributes:
      value: "## ⚙️ Implementation Plan (Optional)"

  - type: textarea
    id: plan
    attributes:
      label: Steps & Owners
      placeholder: |
        1) Draft design (ADR-XXXX) — Owner …
        2) Implement code — Owner …
        3) Add unit/integration tests — Owner …
        4) Docs + STAC updates — Owner …
        5) Peer review + merge — Owner …
    validations:
      required: false

  - type: markdown
    attributes:
      value: "## 🧭 Versioning Impact (SemVer / STAC)"

  - type: dropdown
    id: semver
    attributes:
      label: Repo SemVer Impact
      options: ["semver:none","semver:patch","semver:minor","semver:major"]
      description: Patch=fix | Minor=new feature | Major=breaking change
    validations:
      required: true

  - type: textarea
    id: version_matrix
    attributes:
      label: Version Matrix
      description: Bump any affected schema/data versions
      placeholder: |
        | Scope                 | Current | Proposed | Notes                      |
        | :-------------------- | :------ | :------- | :------------------------- |
        | Dataset / STAC Schema | v1.2.0  | v1.3.0   | Add metadata fields        |
        | Pipeline / Script     | v2.0.0  | v2.1.0   | Terrain ETL refactor       |
        | Repo (SemVer)         | v1.4.0  | v1.5.0   | Minor feature addition     |
      render: markdown
    validations:
      required: false

  - type: markdown
    attributes:
      value: "## 🔗 Related Artifacts"

  - type: textarea
    id: related
    attributes:
      label: Related Items
      placeholder: |
        - STAC Items/Collections
        - Checksums (if validation affected)
        - Workflow run/log URLs
        - Related Issues/PRs
        - SOP / ADR links (docs/adr/ADR-XXXX-<title>.md)
    validations:
      required: false

  - type: markdown
    attributes:
      value: "## 🧠 MCP Compliance"

  - type: checkboxes
    id: mcp
    attributes:
      label: MCP Principles
      options:
        - label: Documentation-first — motivation + technical context
          required: true
        - label: Reproducibility — deterministic test/validation paths
          required: true
        - label: Open Standards — STAC/JSON Schema/COG conventions
          required: true
        - label: Provenance — linked datasets, commits, workflows
          required: true
        - label: Auditability — traceable via CI validation/review gates
          required: true
        - label: Versioning — SemVer bump & STAC versions updated
          required: true

  - type: markdown
    attributes:
      value: "## 📈 Potential Impact"

  - type: textarea
    id: impact
    attributes:
      label: Impact Analysis
      placeholder: |
        | Category                   | Description                             |
        | :------------------------- | :-------------------------------------- |
        | Performance                | Estimate runtime/memory changes         |
        | Data Scope                 | Datasets/layers/models affected         |
        | Backward Compatibility     | Any breaking changes?                   |
        | UI / Visualization         | Map layers/timelines/legends changed    |
        | Security / Compliance      | Access control / data exposure impacts  |
      render: markdown
    validations:
      required: true

  - type: markdown
    attributes:
      value: "## 🧮 Validation Requirements"

  - type: checkboxes
    id: validation
    attributes:
      label: Pre-Merge Checks
      options:
        - label: Unit tests added and passing
          required: true
        - label: STAC schema validated (`make stac-validate`)
          required: true
        - label: ETL reproducibility confirmed (deterministic outputs)
          required: true
        - label: License & data compliance verified
          required: true
        - label: Docs updated under `/docs/sop/` or `/docs/adr/`
          required: true
        - label: Version bump recorded in `CHANGELOG.md`
          required: true

  - type: markdown
    attributes:
      value: "## 📊 Governance Review Checklist (Maintainers)"

  - type: checkboxes
    id: governance
    attributes:
      label: Maintainer Review
      options:
        - label: Design Doc submitted (`docs/adr/`)
        - label: STAC schema impact assessed (versioning)
        - label: CI/CD tests passing (green checks)
        - label: Security review complete (no new vulnerabilities)
        - label: Version/tag bump approved (SemVer policy)
