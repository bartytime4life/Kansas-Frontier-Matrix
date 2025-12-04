---
title: "🔗 KFM v11.2.3 — OpenLineage CI Validation Pipeline (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed lineage-validation system enforcing dataset provenance integrity across PRs, merges, and nightly full-graph audits."
path: "docs/pipelines/lineage/ci-validation/README.md"

version: "v11.2.3"
last_updated: "2025-12-04"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Provenance & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x lineage-contract compatible"
status: "Active · Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/lineage-ci-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/lineage-ci-validation-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY-4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Pipeline Specification"
intent: "openlineage-ci-validation-pipeline"
category: "Pipelines · Lineage · CI · OpenLineage"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "Kansas / United States"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
immutability_status: "version-pinned"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major lineage CI validation standard"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# 🔗 KFM v11.2.3 — OpenLineage CI Validation Pipeline  

`docs/pipelines/lineage/ci-validation/README.md`

**A fully governed lineage-integrity enforcement module ensuring that every KFM dataset, STAC Item, pipeline run, and graph mutation maintains complete, non-cyclic, schema-aligned provenance.**

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.3-purple" />
<img src="https://img.shields.io/badge/Lineage-OpenLineage-green" />
<img src="https://img.shields.io/badge/Data-FAIR%2BCARE-gold" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🧭 1. Purpose

This pipeline defines the **OpenLineage CI validation contract** for KFM.

It ensures that KFM’s lineage graph is:

- **Complete** — no orphan datasets without an allowed root tag.
- **Correct** — no missing upstreams for derived datasets.
- **Non-cyclic** — no cycles in lineage graphs.
- **Schema-aligned** — no schema drift without explicit version bumps.
- **Version-consistent** — downstream contracts are honored when upstreams change.

Every pull request (PR) must pass lineage checks before merge. Nightly jobs validate the full production lineage graph.

---

## 🧱 2. Directory Layout (Emoji-Prefix Standard)

Canonical layout for the CI validation pipeline:

    docs/pipelines/lineage/ci-validation/
    │
    ├── 📄 README.md                         # This file (lineage CI spec)
    │
    ├── 🧪 tests/                            # Lineage validation unit & contract tests
    │   ├── 📄 test_orphans.py
    │   ├── 📄 test_cycles.py
    │   ├── 📄 test_schema_drift.py
    │   └── 📄 test_version_bumps.py
    │
    ├── 🧰 scripts/                          # CLI utilities invoked by CI
    │   ├── 📄 emit_lineage.py               # Controlled emission of OpenLineage events
    │   ├── 📄 checks.py                     # Graph rules engine (cycles, orphans, drifts)
    │   └── 📄 snapshot_graph.py             # Nightly full-graph export
    │
    ├── ⚙️ config/                           # Declarative rule and policy configuration
    │   ├── 📄 rules.yaml                    # Required parents, cycles, schema-drift gates
    │   └── 📄 catalog_allowlist.yaml        # Controlled exceptions for deprecations
    │
    └── 🧩 github-actions/                   # CI entrypoints
        └── 📄 lineage-validation.yml        # PR + nightly validation workflow

Each directory must be governed by its own README (where appropriate) and align with KFM-MDP v11.2.3.

---

## 🔄 3. CI Behavior Overview

### 3.1 PR Validation (Fast, Deterministic)

For each pull request:

- Detect changed datasets / pipelines / DAGs / lineage configs.
- Emit OpenLineage events in **dry-run** mode for the changed scope.
- Enforce:

  - No orphan datasets.
  - No missing upstreams (unless tagged as `seed` or `external-source`).
  - No cycles in lineage graphs.
  - No schema drift without corresponding dataset version increment.

- Any violation **fails the PR** and must be addressed before merge.

### 3.2 Nightly Full-Graph Audit

Nightly scheduled job:

- Pulls full lineage from the OpenLineage API.
- Exports a `snapshot.json` (or equivalent) representing the lineage graph.
- Runs deep rules:

  - Orphans across all namespaces.
  - Dangling datasets (no consumers, no deprecation marker).
  - Contract regressions vs. previous runs.
  - Schema mismatch vs. historical manifests.

- Emits telemetry and artifacts for governance review and long-term audits.

---

## ⚙️ 4. Example GitHub Actions Workflow

**Note:** The actual implementation may live under `.github/workflows/`, but the logical structure is:

    name: lineage-validation

    on:
      pull_request:
        paths:
          - "pipelines/**"
          - "dags/**"
          - "dbt/**"
          - ".lineage/**"
      push:
        branches: [ main ]
      schedule:
        - cron: "13 3 * * *"

    jobs:
      pr_lineage_check:
        if: github.event_name != 'schedule'
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4

          - uses: actions/setup-python@v5
            with:
              python-version: "3.11"

          - name: Install lineage tools
            run: |
              pip install openlineage-python dbt-core networkx pydantic

          - name: Dry-run lineage emission
            env:
              OPENLINEAGE_URL: http://localhost:5001
              OPENLINEAGE_NAMESPACE: ci-preview
            run: |
              python .lineage/emit_lineage.py --changed-only --dry-run --fail-on-missing-parents

          - name: Apply lineage rules
            run: |
              python .lineage/checks.py \
                --rules .lineage/rules.yaml \
                --fail-on orphans,cycles,missing-upstreams,schema-drift,version-regressions

      nightly_graph_consistency:
        if: github.event_name == 'schedule'
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - uses: actions/setup-python@v5
            with:
              python-version: "3.11"

          - run: pip install openlineage-python networkx pydantic

          - name: Snapshot graph
            env:
              OPENLINEAGE_URL: ${{ secrets.OPENLINEAGE_URL }}
            run: |
              python .lineage/snapshot_graph.py --out snapshot.json

          - name: Full graph validation
            run: |
              python .lineage/checks.py \
                --graph snapshot.json \
                --rules .lineage/rules.yaml \
                --fail-on orphans,cycles,dangling-datasets,schema-drift

This workflow is illustrative; actual paths should match the `scripts/` and `config/` layout above.

---

## 📏 5. Rules Contract (`rules.yaml`)

Common rule patterns enforced via `config/rules.yaml`:

- `required_parents: true`  
  Every non-root dataset must have at least one upstream.

- `block_cycles: true`  
  Any strongly connected component of size > 1 in the lineage graph causes failure.

- `block_orphans: true`  
  Datasets without upstreams and without allowed root tags cause failure.

- `allow_root_tags:`  

  - `seed`
  - `external-source`

- `require_version_bump_on_schema_change: true`  
  If schema changes vs. previous manifest, a dataset version bump is required.

- `version_conflict_policy: "fail"`  
  Any version regression or incompatible change fails validation.

Rules are declarative and version-controlled; changes to `rules.yaml` must themselves pass CI and governance review.

---

## 🧪 6. Validation Logic Summary

### 6.1 Orphan Detection

- Any dataset without upstream lineage and **not** explicitly root-tagged (`seed`, `external-source`, or other configured tags) → **fail**.
- Orphans are reported with:
  - Dataset ID.
  - Namespace.
  - Owning pipeline / project.

### 6.2 Cycle Detection

- The lineage graph is topologically sorted; if topological sort fails or any strongly connected component has size > 1 → **fail**.
- Reports include:
  - Cycle members.
  - Edge list forming the cycle.

### 6.3 Schema Drift

- Dataset schema (e.g., columns, types, constraints) is compared to the previous **manifest**.
- If changed and no version increment is detected:
  - **fail** with a schema-drift error.
- If version bump exists:
  - Check downstream compatibility policies (e.g., optional fields vs. breaking deletions).

### 6.4 Downstream Consistency

- For datasets with declared downstream consumers:
  - Breaking changes must be accompanied by explicit downstream compatibility contracts or migration notes.
- Violations (unannounced breaking changes) → **fail**.

---

## 📦 7. Allowlist Usage (`catalog_allowlist.yaml`)

In some cases, datasets enter controlled **deprecation windows**:

- The allowlist enumerates:
  - Datasets temporarily exempt from certain rules (e.g., orphans during decommission).
  - Time-bounded exceptions, with review dates.

Rules for the allowlist:

- Allowlist entries must include:
  - Dataset ID.
  - Reason for exception.
  - Expiry or review date.
- The allowlist itself is:
  - Version-controlled.
  - Audited nightly during the full-graph validation.
  - Subject to FAIR+CARE and governance review.

---

## 📈 8. Telemetry

All lineage CI checks emit structured telemetry (as defined by `telemetry_schema`):

Minimum fields:

- `lineage_ci.run_id` — CI run or workflow execution ID.
- `lineage_ci.rule_violation_count` — Count of violations per rule type.
- `lineage_ci.violations` — Aggregated summary (rule → count).
- `lineage_ci.namespaces` — Namespaces affected in the run.
- `lineage_ci.runtime_seconds` — Wall-clock runtime for lineage validation.
- `lineage_ci.result` — `pass` / `fail`.

Optional:

- `lineage_ci.dataset_ids_sample` — Small sample (non-PII) of affected dataset IDs.
- `lineage_ci.energy_kwh` and `lineage_ci.carbon_gco2e` — Estimated energy/carbon for the job (when energy/carbon telemetry is enabled).

Telemetry records:

- Are exported via OpenTelemetry.
- Feed reliability and governance dashboards.
- Are retained according to KFM’s telemetry retention policy.

---

## 🧬 9. Integration with KFM Knowledge Graph

Validated lineage events hydrate Neo4j and other graph stores:

- Datasets map to **CIDOC-CRM** and PROV-O entities, e.g.:

  - `crm:E73_Information_Object` → dataset or data product.
  - `prov:Entity` → dataset versions.

- Edges map to:

  - `crm:P148_has_component` / `crm:P106_is_composed_of` for component relationships.
  - `prov:wasDerivedFrom` for transformation lineage.

- Activities (pipeline runs):

  - `prov:Activity` nodes with:
    - `prov:used` (upstream datasets).
    - `prov:generated` (downstream datasets).
    - `prov:wasAssociatedWith` (pipeline Agents, services).

By enforcing lineage via CI, the knowledge graph remains:

- **Coherent** — no random or untracked transformations.
- **Queryable** — reliable lineage queries for audits and analyses.
- **Auditable** — provenance trails for datasets, dashboards, Story Nodes, and AI outputs.

---

## 🕰 10. Version History

| Version  | Date       | Notes                                                                                     |
|---------:|------------|-------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial KFM-MDP v11.2.3-aligned lineage CI contract; emoji layout; telemetry integration. |

---

<div align="center">

### 🔗 KFM v11.2.3 — OpenLineage CI Validation Pipeline

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Provenance Enforcement  

[📚 Lineage Pipelines Index](../README.md) ·  
[🧬 Provenance Standards](../../../../docs/standards/provenance/README.md) ·  
[⚖ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>