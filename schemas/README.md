<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/c4017624-8264-45fe-86cd-8d7cf05991ed
title: schemas
type: standard
version: v1
status: draft
owners: TBD (Schema Stewards)
created: 2026-03-03
updated: 2026-03-03
policy_label: public
related:
  - tools/validators/
  - tools/schema/
  - governance/run_receipt.schema.json
  - .github/workflows/
tags: [kfm, schemas, json-schema, contracts, governance]
notes:
  - This README documents intended contracts and guardrails. Treat any "Proposed" or "Unknown" items as design defaults until confirmed in-repo.
[/KFM_META_BLOCK_V2] -->

# schemas
Governed JSON Schema contracts for KFM artifacts (catalogs, receipts, telemetry, and other machine-validated interfaces).

![status](https://img.shields.io/badge/status-draft-lightgrey)
![contracts](https://img.shields.io/badge/contracts-governed-blue)
![json-schema](https://img.shields.io/badge/JSON%20Schema-draft%202020--12-blue)
![ci](https://img.shields.io/badge/CI-schema--lint%20%7C%20compat%20diff-blue)
<!-- TODO: Replace badges/targets once CI paths are finalized -->

## Navigation
- [Purpose](#purpose)
- [Evidence labels](#evidence-labels)
- [Where this fits in KFM](#where-this-fits-in-kfm)
- [Directory layout](#directory-layout)
- [What belongs here](#what-belongs-here)
- [Schema registry](#schema-registry)
- [Versioning and compatibility](#versioning-and-compatibility)
- [Validation](#validation)
- [Change workflow](#change-workflow)
- [Unknowns to verify](#unknowns-to-verify)

---

## Purpose

- **Confirmed:** Provide a single, reviewable place to define the **machine-validated contracts** that CI and promotion gates depend on (schemas are a hard “truth boundary,” not optional documentation).
- **Confirmed:** Support **fail-closed** validation: if an artifact (catalog, receipt, telemetry event) does not validate, it must not be promoted/published.
- **Proposed:** Make schemas easy to discover and reference via a single registry file (`schemas/registry.yaml`).
- **Proposed:** Run a PR-time **schema compatibility diff** for any schema changes, and block merges on breaking changes unless a major version bump is declared.

---

## Evidence labels

This repo treats documentation as a production surface. To avoid “hand-wavy contracts,” statements in this README use:

- **Confirmed** — supported by KFM design/governance docs or CI contract snippets.
- **Proposed** — recommended repo conventions (safe defaults) that can be implemented incrementally.
- **Unknown** — not verifiable from the currently available evidence; includes the smallest steps to confirm.

> NOTE: “Confirmed” here means “confirmed as a documented contract/intent.” It does **not** automatically mean the exact file paths already exist in this checkout.

---

## Where this fits in KFM

- **Confirmed:** KFM’s promotion model relies on automated gates (identity/versioning, licensing, sensitivity, catalog-triplet validation, QA thresholds, and run receipts). Schemas are the concrete, testable surface behind those gates.
- **Confirmed:** Catalog validation in CI is expected to run as discrete steps (DCAT/STAC/PROV validation, link checking, and spec-hash drift checks).
- **Proposed:** Treat `schemas/` as a **core contract boundary**: changes here require review by CODEOWNERS and must be accompanied by fixtures/tests.

---

## Directory layout

**Proposed default layout** (adapt to your repo once confirmed):

~~~text
schemas/
├── README.md
├── registry.yaml                  # canonical index of schemas (ids, paths, semver, compat mode)
├── common/                        # shared $defs (ids, timestamps, digests, SPDX, policy labels)
├── catalogs/
│   ├── dcat/                      # DCAT profile schemas (JSON-LD shape constraints)
│   ├── stac/                      # STAC profile schemas / extension pinning
│   └── prov/                      # PROV(-O) / run lineage bundles
├── telemetry/                     # telemetry event schemas (audit, drift, energy, carbon, etc.)
├── receipts/                      # run receipts / attestations / promotion manifests
└── api/                           # optional: request/response DTO schemas (if not kept in OpenAPI)
~~~

- **Unknown:** Whether the above subfolders already exist in your working tree.
  - **Verify:** `ls -R schemas/` and compare with this layout; update this README to reflect reality.

---

## What belongs here

### Acceptable inputs

- **Confirmed:** JSON Schema files used to validate CI-critical artifacts such as:
  - catalog records (DCAT, STAC, PROV)
  - run receipts (and receipt-like audit records)
  - telemetry events used by governance/ops checks
- **Proposed:** Shared `$defs` for cross-cutting fields:
  - `dataset_id`, `dataset_version_id`
  - `spec_hash`
  - content digests (`sha256:`)
  - time fields (`date-time`)
  - policy labels / sensitivity classifications
  - SPDX license identifiers

### Exclusions

- **Confirmed:** No raw/processed data belongs here.
- **Confirmed:** No secrets, tokens, or environment-specific configuration belongs here.
- **Proposed:** Don’t store generated artifacts here (compiled bundles, minified outputs). Prefer generating to `artifacts/` or CI artifacts.
- **Proposed:** Don’t store policy (Rego) here; keep schemas and policy separate to preserve a clean policy boundary.

---

## Schema registry

- **Proposed:** Maintain a single registry file to support:
  - schema discovery
  - compatibility checks
  - enforcement of ownership and policy labels
  - deterministic references in receipts/manifests

### Proposed `schemas/registry.yaml` shape

~~~yaml
# schemas/registry.yaml
version: 1
schemas:
  - id: kfm.schema.telemetry.drift_search.v11
    path: schemas/telemetry/drift-search-v11.json
    semver: 11.0.0
    mode: backward   # backward|forward|full (compat expectations)
    owners: [tbd-schema-stewards]
    policy_label: public

  - id: kfm.schema.receipt.run.v1
    path: schemas/receipts/run-receipt-v1.schema.json
    semver: 1.0.0
    mode: backward
    owners: [tbd-schema-stewards]
    policy_label: restricted
~~~

- **Unknown:** Whether your repo already uses `schemas/registry.yaml`.
  - **Verify:** search CI/workflows for `schemas/registry.yaml` references; if none, add registry + wire checks.

---

## Versioning and compatibility

- **Confirmed:** Use SemVer rules for schema evolution:
  - **PATCH**: descriptions/examples/annotations only
  - **MINOR**: additive, backward-compatible changes (e.g., optional fields)
  - **MAJOR**: breaking changes (e.g., new required properties, type changes)

- **Proposed:** Enforce compatibility in CI:
  1. detect changed schemas under `schemas/**/schema.json` (or your naming convention)
  2. run a JSON Schema diff tool in the declared direction/mode
  3. produce a PR artifact report and fail the job on breaking changes without major bump

---

## Validation

### Local validation

- **Proposed:** Provide a minimal local workflow:
  - validate a schema is itself well-formed
  - validate representative fixtures against the schema
  - validate cross-schema references resolve (no broken `$ref`)

Example commands (adjust to your tooling):

~~~bash
# Validate a schema file is syntactically valid JSON
jq -e . schemas/telemetry/drift-search-v11.json >/dev/null

# Validate fixtures against a schema (example)
python -m jsonschema \
  --schema schemas/telemetry/drift-search-v11.json \
  examples/telemetry/drift-search.sample.json
~~~

### CI validation

- **Confirmed (documented CI intent):** Run catalog validators + link checks + spec-hash drift checks in CI.
- **Proposed:** Add schema-lint + schema-compat-diff jobs that trigger only when `schemas/**` changes.

~~~mermaid
flowchart LR
  A[Change proposed in PR] --> B[Schema lint]
  B --> C[Schema compatibility diff]
  C --> D[Artifact validators]
  D --> E[Promotion gates]
  E --> F[Merge or fail closed]
~~~

---

## Change workflow

### Definition of Done for a schema change (PR checklist)

- [ ] **Confirmed:** schema validates (no broken refs)
- [ ] **Proposed:** registry entry exists/updated (`schemas/registry.yaml`)
- [ ] **Proposed:** SemVer bump matches the change type (patch/minor/major)
- [ ] **Proposed:** compatibility diff report is green (or major bump justified)
- [ ] **Confirmed:** fixtures/examples updated (or added) to cover new/changed fields
- [ ] **Confirmed:** CI gates pass (catalog validation, linkcheck, spec-hash drift, policy tests where applicable)
- [ ] **Proposed:** changelog note added (or PR description includes rationale + rollback plan)

### Guardrails

- **Confirmed:** Avoid schema designs that enable targeting or exposure of sensitive locations.
- **Proposed:** If a schema includes location fields, require an explicit `policy_label` and document redaction/generalization obligations in the consuming pipeline spec.

---

## Unknowns to verify

These items are intentionally **fail-closed** until confirmed:

1) **Does `schemas/registry.yaml` exist today?**  
   - Verify: list `schemas/` and search CI for registry usage.

2) **Which schema families are currently in use (catalogs, telemetry, receipts)?**  
   - Verify: grep for `schemas/` references in docs, pipelines, and CI workflows.

3) **Where is the canonical run receipt schema stored (`governance/` vs `schemas/receipts/`)?**  
   - Verify: locate `run_receipt.schema.json` and identify the consuming validators.

4) **Which JSON Schema draft is enforced (2020-12 vs older drafts)?**  
   - Verify: inspect `$schema` fields and validator tool versions/pins.

> TIP: Once verified, replace “Proposed” layouts and placeholders with the repo’s actual structure and wire the checks in CI so the README stays true automatically.

---

Back to top: [schemas](#schemas)
