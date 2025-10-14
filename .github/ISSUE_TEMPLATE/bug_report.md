name: "🐞 Bug Report"
description: "Report a defect in code, data, metadata, or workflows — MCP-compliant & reproducible"
title: "[Bug]: <short summary>"
labels:
  - bug
  - needs-triage
assignees:
  - kfm-architecture
# KFM header metadata (for humans)
# version: v2.2.0
# last_updated: 2025-10-13
# owners: @kfm-architecture @kfm-data @kfm-security

body:
  - type: markdown
    attributes:
      value: |
        ## 🧩 Summary
        *“Every Bug Leaves a Trace — Every Trace Leads to Reproducibility.”*
        Please provide a concise description of the unexpected behavior or data discrepancy.
        > Example: Terrain ETL workflow fails checksum verification for 2020 LiDAR tiles when reprojecting to EPSG:4326.

  - type: textarea
    id: summary
    attributes:
      label: Summary
      description: What happened? What were you trying to do?
      placeholder: |
        - ETL step failed during raster reprojection
        - Graph build produced missing edges for treaty X
    validations:
      required: true

  - type: markdown
    attributes:
      value: "## 🧠 Context"

  - type: input
    id: module
    attributes:
      label: Module / Workflow
      description: File or workflow name
      placeholder: terrain_pipeline.py | stac-validate.yml | src/graph/build_graph.py
    validations:
      required: true

  - type: dropdown
    id: domain
    attributes:
      label: Data Domain
      options:
        - Terrain
        - Hydrology
        - Hazards
        - Landcover
        - Climate
        - Text / AI / NLP
        - Web / UI
        - API
        - ETL
        - CI/CD
        - Knowledge Graph
      multiple: true
    validations:
      required: true

  - type: input
    id: branch_commit
    attributes:
      label: Branch / Commit
      placeholder: main | feature/lidar-v2 | 4a8e91c
    validations:
      required: true

  - type: input
    id: environment
    attributes:
      label: Environment
      description: OS, Python/Node versions, container image hash, runner type
      placeholder: Ubuntu 22.04 · Python 3.11 · node 20.x · gh-runner=ubuntu-latest · image sha256:…
    validations:
      required: true

  - type: input
    id: date_observed
    attributes:
      label: Date Observed
      placeholder: "2025-10-13"
    validations:
      required: true

  - type: input
    id: stac_id
    attributes:
      label: Dataset Version / STAC ID
      placeholder: terrain_ks_1m_v2.3 | data/stac/items/terrain_ks_2020.json
    validations:
      required: false

  - type: input
    id: ci_url
    attributes:
      label: Workflow Run URL (if applicable)
      placeholder: https://github.com/.../runs/123456789
    validations:
      required: false

  - type: markdown
    attributes:
      value: "## 🔁 Steps to Reproduce"

  - type: textarea
    id: steps
    attributes:
      label: Deterministic Steps
      description: Minimal input, exact commands, reproducible steps
      placeholder: |
        1) make terrain
        2) python src/pipelines/terrain/terrain_pipeline.py --config config/test_terrain.yaml
        3) Observe FileNotFoundError for intermediate COG
    validations:
      required: true

  - type: markdown
    attributes:
      value: "## 🧠 Expected Behavior"

  - type: textarea
    id: expected
    attributes:
      label: Expected Result
      placeholder: Expected artifact(s), message(s), or output structure
    validations:
      required: true

  - type: markdown
    attributes:
      value: "## 💥 Actual Behavior"

  - type: textarea
    id: actual
    attributes:
      label: Actual Result
      description: Include error messages, stack traces, or screenshots
      placeholder: |
        FileNotFoundError: 'data/processed/terrain/ks_1m_dem_2020.tif' missing.
    validations:
      required: true

  - type: markdown
    attributes:
      value: "## 📄 Logs & Evidence"

  - type: textarea
    id: logs
    attributes:
      label: Logs / Evidence
      description: Paste key snippets or attach artifacts (avoid secrets)
      placeholder: data/work/logs/<domain>_etl_debug.log
      render: shell
    validations:
      required: false

  - type: markdown
    attributes:
      value: "## 🔍 Checksum / Integrity Verification (if applicable)"

  - type: textarea
    id: checksum_table
    attributes:
      label: Checksum Comparisons
      description: Compare Expected vs Observed SHA-256 when integrity is relevant
      placeholder: |
        | File                                        | Expected SHA-256 | Observed SHA-256 |
        | :------------------------------------------ | :--------------- | :--------------- |
        | data/processed/terrain/ks_1m_dem_2020.tif   | abc123…          | def789…          |
        | data/stac/items/terrain_ks_2020.json        | ffd234…          | ffd234… ✅        |
      render: markdown

  - type: markdown
    attributes:
      value: "## 🧾 Impact Assessment"

  - type: dropdown
    id: severity
    attributes:
      label: Severity
      options:
        - "🟥 Critical"
        - "🟧 Major"
        - "🟨 Moderate"
        - "🟩 Minor"
    validations:
      required: true

  - type: textarea
    id: downstream
    attributes:
      label: Affected Pipelines / Downstream Effects
      description: Impact on ETL/web/graph/STAC, end users, or CI/CD
      placeholder: |
        - Affected pipelines: make terrain
        - Downstream: web UI map missing tiles; STAC validate fails
    validations:
      required: true

  - type: markdown
    attributes:
      value: "## 🧰 Suggested Fix / Next Steps (Optional)"

  - type: checkboxes
    id: suggested
    attributes:
      label: Candidate Actions
      options:
        - label: Patch ETL pipeline logic
        - label: Re-run `make checksums`
        - label: Update STAC metadata (datetime, bbox, CRS)
        - label: Regenerate missing artifacts
        - label: Verify locally (`make validate-<domain>`)
        - label: Submit PR referencing this issue

  - type: markdown
    attributes:
      value: "## 🧪 Validation Commands"

  - type: textarea
    id: validation_cmds
    attributes:
      label: Commands for Validation
      description: Exact commands others can run to reproduce/verify
      placeholder: |
        make checksums
        make terrain
        make stac-validate
        pre-commit run --all-files
      render: shell
    validations:
      required: true

  - type: markdown
    attributes:
      value: "## 🧭 Versioning Impact (SemVer / STAC)"

  - type: textarea
    id: versioning
    attributes:
      label: Versioning Summary
      description: Indicate scope and proposed bump(s)
      placeholder: |
        | Scope                  | Current | Affected | Action        |
        | :--------------------- | :------ | :------- | :------------ |
        | Dataset / STAC         | v1.3.0  | ✅       | bump → v1.3.1 |
        | Pipeline / Script      | v2.0.0  | ✅       | fix → v2.0.1  |
        | Workflow (CI/CD)       | v1.2.0  | ❌       | none          |
        | Repo Release (SemVer)  | v1.4.0  | ✅       | patch         |
      render: markdown
    validations:
      required: false

  - type: markdown
    attributes:
      value: "## ✅ MCP Compliance Checklist"

  - type: checkboxes
    id: mcp_checklist
    attributes:
      label: MCP Principles
      options:
        - label: Documentation-first — Clear summary + structured context
          required: true
        - label: Reproducibility — Deterministic steps + validation commands
          required: true
        - label: Open Standards — Make/CI workflows used to reproduce
          required: true
        - label: Provenance — Logs, checksums, STAC items attached
          required: true
        - label: Auditability — CI run/links provided; evidence attached
          required: true
        - label: Versioning — SemVer / STAC version fields updated or impact noted
          required: true

  - type: markdown
    attributes:
      value: "## 🧩 Related Issues / References"

  - type: textarea
    id: related
    attributes:
      label: Related Links
      description: Link PRs, similar issues, affected STAC items, ADRs, SOPs
      placeholder: |
        - PR: #123
        - Similar: #456
        - STAC: data/stac/items/terrain_ks_2020.json
        - Docs: docs/sop/terrain_pipeline.md
    validations:
      required: false

  - type: textarea
    id: notes
    attributes:
      label: Additional Notes
      description: Screenshots, specs, or diagnostic insight to accelerate triage
    validations:
      required: false
```
