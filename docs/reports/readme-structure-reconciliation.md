<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<NEEDS-UUID>
title: README Structure Reconciliation Report
type: standard
version: v1
status: draft
owners: <NEEDS-OWNER-VERIFICATION>
created: <NEEDS-CREATED-DATE>
updated: <NEEDS-UPDATED-DATE>
policy_label: <NEEDS-POLICY-LABEL>
related: [README.md, .github/workflows/README.md, contracts/README.md, schemas/README.md, policy/README.md, tests/README.md]
tags: [kfm, docs, repo-structure, scaffolding, readme]
notes: [doc_id/owners/dates/policy label need verification, current public-tree check confirms this file exists on main, workflow YAML names preserved below should be read as historical scaffold entries unless regenerated from the live tree]
[/KFM_META_BLOCK_V2] -->

# README Structure Reconciliation Report

Structural reconciliation snapshot for README-declared tree entries, with a current public-tree recheck to separate **historical scaffold inventory** from **still-confirmed public `main` structure**.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Evidence: public--tree%20checked](https://img.shields.io/badge/evidence-public--tree%20checked-blue)
![Snapshot: historical](https://img.shields.io/badge/snapshot-historical-7c3aed)
![Parity: regenerate](https://img.shields.io/badge/parity-regenerate-red)
![Scope: structure only](https://img.shields.io/badge/scope-structure%20only-6b7280)

**Quick jump:** [Repo fit](#repo-fit) · [Evidence basis](#evidence-basis) · [Method](#method) · [Current reconciliation status](#current-public-tree-reconciliation-status) · [Snapshot summary](#reported-scaffold-snapshot) · [High-signal paths](#high-signal-path-families) · [Scaffold inventory](#reported-scaffolded-paths-by-area-historical-snapshot) · [Verification caveats](#verification-caveats) · [Follow-up](#recommended-follow-up)

> [!IMPORTANT]
> This document should now be read as a **historical scaffold snapshot with a current public-tree correction layer**.  
> It preserves the structure report already checked into the repo, but it does **not** treat every listed path as current public-tree fact.

> [!CAUTION]
> Current path parity remains **NEEDS VERIFICATION** unless this document explicitly marks a point as **CONFIRMED current public-tree evidence**.  
> In particular, historically reported workflow YAML names under `.github/workflows/` should **not** be read as current checked-in files on public `main` without regeneration.

## Repo fit

| Item | Value |
|---|---|
| Likely target path | `docs/reports/readme-structure-reconciliation.md` **(CONFIRMED)** |
| Upstream inputs | Current public `README.md`-adjacent repo surfaces, the checked-in reconciliation report, and nearby README/doc boundaries that define how structural claims should be read |
| Downstream use | Reviewer orientation, scaffold drift detection, README-tree cleanup, historical audit context, and future regeneration of a live inventory |
| Accepted inputs | Code-fenced tree blocks, directory READMEs, current public repo listings, and structure-first documentation artifacts |
| Exclusions | Behavioral completeness claims, merge-enforcement claims, policy-execution claims, route/runtime claims, and any assertion that scaffolded paths are operational without direct re-verification |
| Interpretation rule | Presence in the scaffold inventory means **reported as scaffolded or declared**, not **confirmed as implemented** |

## Evidence basis

This revision uses a **two-layer evidence model** rather than pretending one snapshot can do both jobs cleanly.

| Evidence layer | Role in this report | Reading rule |
|---|---|---|
| Current public-tree evidence | Re-check what public `main` exposes **now** for the target file and nearby structure-defining READMEs | **CONFIRMED** for visible public-tree state only |
| Checked-in reconciliation report | Preserve the already-recorded scaffold inventory and counts | Treat as a **historical scaffold snapshot** |
| Repo-grounded sprint summary | Corroborate where staleness and documentary-vs-executable risks were already identified | Useful historical warning, not live-tree proof |
| KFM doctrinal overlays | Keep truth labels, overclaim protection, and source-discipline language aligned with project doctrine | Use for framing, not for inventing repo state |

## Method

The reconciliation logic in this revision is intentionally conservative.

1. Preserve the strongest existing substance from the checked-in report.
2. Re-check the current public `main` tree where adjacent repo surfaces are directly visible.
3. Reclassify older path inventories as **historical scaffold entries** unless current parity is directly visible.
4. Surface contradictions instead of smoothing them away.
5. Keep executable-looking names structurally useful, but not behaviorally over-read.

```mermaid
flowchart LR
    A[Checked-in scaffold report] --> B[Current public-tree recheck]
    B --> C[Confirm what still exists on public main]
    C --> D[Flag historical-only or drift-prone entries]
    D --> E[Preserve useful scaffold inventory]
    E --> F[Recommend regeneration from live working tree]
```

> [!NOTE]
> This revision is a **reconciliation pass**, not a fresh filesystem crawl.  
> Its job is to stop the document from reading like a live inventory when the visible repo evidence does not justify that reading.

## Current public-tree reconciliation status

The table below is the most important corrective addition in this revision.

| Surface | Current public reading | Consequence for this report | Status |
|---|---|---|---|
| `docs/reports/readme-structure-reconciliation.md` | The file exists on public `main` and still presents itself as a structure-only draft with verification caveats | Keep the report, but harden its **historical snapshot** reading | **CONFIRMED** |
| `.github/workflows/` | Public `main` currently presents `workflows/` as a README-only checked-in surface | Historically named workflow YAMLs preserved below must be read as **historical scaffold/history-derived names**, not current checked-in files | **CONFIRMED** |
| `contracts/` | Current docs treat machine-contract pathing as still authority-sensitive, with `contracts/` the stronger working signal | Keep contract-looking entries structural; do not claim final authority resolution | **CONFIRMED / PROPOSED** |
| `schemas/` | Current docs explicitly warn against growing a parallel authoritative schema universe beside `contracts/` | Treat `schemas/*` as boundary/documentary structure unless authority is re-resolved | **CONFIRMED** |
| `policy/` | Current docs allow executable bundles, fixtures, tests, and vocabularies to belong here | Preserve policy-looking entries as valid structural expectations, but not as executed reality | **CONFIRMED / NEEDS VERIFICATION** |
| `tests/` | Current docs now name multiple test families and e2e proof lanes | Preserve test-lane shape as meaningful repo intent, but not proof of runnable coverage | **CONFIRMED / NEEDS VERIFICATION** |

## Reported scaffold snapshot

The counts below are preserved from the existing checked-in report and should be read as **historical reported totals from the scaffold pass**, not as a recomputed current-tree count.

**Historical reported total:** **130** concrete scaffolded paths  
**Historical reported breakdown:** **80** directories + **50** files  
**Implicit companions not counted:** `.gitkeep` files added to otherwise-empty new directories

| Area | Historical reported paths | Files | Directories | Read this as |
|---|---:|---:|---:|---|
| `.github` | 24 | 8 | 16 | Governance/scaffold snapshot, now partially contradicted by current public workflow inventory |
| `policy` | 24 | 14 | 10 | Policy surface intent, not proof of mounted executable bundles |
| `scripts` | 20 | 18 | 2 | Validator/entrypoint intent, not verified runnable commands |
| `infra` | 12 | 0 | 12 | Deployment-shape scaffolding only |
| `schemas` | 12 | 0 | 12 | Schema-family surface only; not authoritative schema-home proof |
| `examples` | 10 | 6 | 4 | Example-object scaffolding |
| `tools` | 10 | 2 | 8 | Tooling layout intent |
| `brand` | 8 | 0 | 8 | Asset/token/template structure |
| `data` | 4 | 0 | 4 | Catalog/provenance/quarantine shape |
| `tests` | 3 | 0 | 3 | Older narrow test-lane snapshot only |
| `migrations` | 2 | 2 | 0 | Stub existence reported by scaffold pass |
| `configs` | 1 | 0 | 1 | Configuration surface only |

## High-signal path families

These families are easy to over-read. The table below keeps them disciplined.

| Path family | Why reviewers may over-read it | How this revision treats it |
|---|---|---|
| `.github/workflows/*.yml` | Looks like active merge gates or current checked-in automation | **Historical scaffold/history-derived names only** unless rechecked; current public `main` shows a README-only workflow directory |
| `policy/*.rego` and `policy/*.json` | Looks like executable policy bundles and vocabularies | **Structural policy surface** until real files, tests, and decisions are re-verified |
| `scripts/*` and `tools/*` | Looks like runnable validators and maintenance entrypoints | **Placeholder or planned executable surface** until command behavior is verified |
| `migrations/*.sql` | Looks like applied database state | **Stub existence only** until order, execution history, and target DB use are verified |
| `schemas/*` and `contracts/*` | Looks like settled authoritative machine-contract home | **Authority unresolved in repo docs**; keep both structural but do not infer a live canonical registry from names alone |
| `examples/*.json`, `tests/*`, `policy/{valid,invalid}` | Looks like active fixtures and test coverage | **Intent-bearing structure** until validators and harnesses are rechecked |

## Reported scaffolded paths by area (historical snapshot)

The inventories below are preserved because they are still useful as **audit context** and **cleanup targets**. They are intentionally not presented as a fresh live-tree crawl.

### `.github` and repo-governance surfaces

<details>
<summary><strong>.github</strong> — historically reported scaffold entries</summary>

> [!NOTE]
> Current public `main` confirms `.github/workflows/README.md` as the checked-in workflow surface.  
> The YAML names below are preserved as **historically reported scaffold entries** and should not be read as current checked-in workflow files without regeneration.

```text
.github/ISSUE_TEMPLATE/config.yml
.github/actions/action.yml
.github/actions/metadata-validate
.github/actions/metadata-validate-v2
.github/actions/opa-gate
.github/actions/provenance-guard
.github/actions/sbom-produce-and-sign
.github/actions/src
.github/apps
.github/contracts
.github/data
.github/docs
.github/infra
.github/packages
.github/policy
.github/scripts
.github/tests
.github/tools
.github/workflows/promote-and-reconcile.yml
.github/workflows/release-evidence.yml
.github/workflows/verify-contracts-and-policy.yml
.github/workflows/verify-docs.yml
.github/workflows/verify-runtime.yml
.github/workflows/verify-tests-and-reproducibility.yml
```

</details>

### Brand, config, and data structure

<details>
<summary><strong>brand</strong> — historically reported scaffold entries</summary>

```text
brand/LICENSES
brand/assets
brand/icons
brand/logos
brand/source
brand/templates
brand/tokens
brand/usage
```

</details>

<details>
<summary><strong>configs</strong> — historically reported scaffold entries</summary>

```text
configs/systemd
```

</details>

<details>
<summary><strong>data</strong> — historically reported scaffold entries</summary>

```text
data/dcat
data/prov
data/quarantine
data/stac
```

</details>

### Examples and infrastructure

<details>
<summary><strong>examples</strong> — historically reported scaffold entries</summary>

```text
examples/catalog_closure.json
examples/dataset_version.json
examples/evidence_bundle.json
examples/hydrology
examples/ingest_receipt.json
examples/invalid
examples/release_manifest.json
examples/source_descriptor.json
examples/thin_slice
examples/valid
```

</details>

<details>
<summary><strong>infra</strong> — historically reported scaffold entries</summary>

```text
infra/apps
infra/compose
infra/contracts
infra/docs
infra/gitops
infra/kubernetes
infra/monitoring
infra/policy
infra/runbooks
infra/systemd
infra/terraform
infra/tests
```

</details>

### Migrations and policy

<details>
<summary><strong>migrations</strong> — historically reported scaffold entries</summary>

```text
migrations/0001_enable_extensions.sql
migrations/0002_spatial_indexes.sql
```

</details>

<details>
<summary><strong>policy</strong> — historically reported scaffold entries</summary>

```text
policy/access.rego
policy/bundles
policy/citations.rego
policy/completeness.rego
policy/evidence.rego
policy/exceptions
policy/fixtures
policy/generalization.rego
policy/invalid
policy/local-check.md
policy/obligation_codes.json
policy/pack.rego
policy/provenance
policy/publication
policy/reason_codes.json
policy/release.rego
policy/review-checklist.md
policy/review.rego
policy/reviewer_roles.json
policy/runbooks
policy/runtime
policy/sensitivity
policy/valid
policy/withholding.rego
```

</details>

### Schemas, scripts, tests, and tools

<details>
<summary><strong>schemas</strong> — historically reported scaffold entries</summary>

```text
schemas/apis
schemas/contracts
schemas/deployment
schemas/docs
schemas/events
schemas/examples
schemas/invalid
schemas/observability
schemas/policy
schemas/profiles
schemas/tests
schemas/valid
```

</details>

<details>
<summary><strong>scripts</strong> — historically reported scaffold entries</summary>

```text
scripts/attach_evidence.sh
scripts/crosslink_consistency.py
scripts/domain_freshness.sh
scripts/emit_error_json.sh
scripts/example_record_valid.sh
scripts/focus_mode_gate.sh
scripts/has_metadata.sh
scripts/md_required_sections.sh
scripts/release
scripts/run_receipt_valid.sh
scripts/spdx_ok.sh
scripts/spec_hash_valid.sh
scripts/stac_valid.sh
scripts/validate_jsonld.sh
scripts/validate_prov.py
scripts/validate_stac.py
scripts/validators
scripts/verify_checksums.sh
scripts/verify_fingerprint.py
scripts/write_index_entry.sh
```

</details>

<details>
<summary><strong>tests</strong> — historically reported scaffold entries</summary>

```text
tests/correction
tests/release_assembly
tests/runtime_proof
```

</details>

<details>
<summary><strong>tools</strong> — historically reported scaffold entries</summary>

```text
tools/attest
tools/bash
tools/catalog
tools/catalog_qa
tools/ci
tools/config.yml
tools/partition
tools/run_catalog_qa.py
tools/sql
tools/validate
```

</details>

## Interpretation legend

| Label | Meaning in this report |
|---|---|
| **CONFIRMED** | Directly visible in the current public-tree check or explicitly stated by the checked-in report |
| **INFERRED** | Conservative editorial completion used to reconcile historical scaffold language with current repo doctrine |
| **PROPOSED** | Follow-up or regeneration step that would make this report safer, clearer, or more machine-usable |
| **UNKNOWN** | Anything about mounted implementation, command behavior, merge settings, branch protection, or runtime execution not directly proven here |
| **NEEDS VERIFICATION** | Any path-by-path parity claim that was not freshly regenerated from the current working tree |

## Verification caveats

This report should be read with five constraints in mind.

1. **Historical scaffold is not live inventory.**  
   The inventories below preserve a useful structural memory, but they are not a substitute for a fresh tree-derived report.

2. **A real divergence is already visible.**  
   The current public workflow directory snapshot and the older scaffolded workflow names do not line up cleanly. That means other path families may also contain drift.

3. **Executable-looking names carry extra risk.**  
   Workflow YAML, Rego files, SQL migrations, validators, and tool entrypoints visually imply maturity. This report intentionally refuses that implication.

4. **Authority and implementation are different questions.**  
   `contracts/`, `schemas/`, `policy/`, and `tests/` now communicate stronger repo intent than a generic placeholder reading, but they still do not by themselves prove mounted implementation depth.

5. **Authoritative inventory should be generated.**  
   Long-term, this report should either become a generated snapshot or be frozen as historical context and linked to a generated source of truth.

## Recommended follow-up

- [ ] Regenerate this report from the **current working tree** and replace historical counts with live counts.
- [ ] Split “historical scaffold inventory” from “current verified public-tree inventory” if both are still worth keeping.
- [ ] Replace the historically reported `.github/workflows/*.yml` list with either:
  - current checked-in workflow files, or
  - a clearly labeled historical appendix.
- [ ] Reconcile `contracts/` vs `schemas/` authority in one explicit repo-level decision.
- [ ] Re-check `policy/`, `tests/`, `scripts/`, and `tools/` path inventories against the actual tree before treating those families as parity-complete.
- [ ] Add a machine-generated inventory source if the repo wants this report to stay current.

## Non-goals

This report does **not** attempt to:

- prove that the listed files contain complete or correct contents
- certify CI/CD behavior, branch protection, or review enforcement
- prove that any listed script, workflow, tool, policy bundle, or test harness actually runs
- resolve final machine-contract authority between `contracts/` and `schemas/`
- prove mounted runtime, database, or release state
- substitute for a generated repo inventory or verification command

## Maintenance note

When this document is updated, prefer one of the following patterns:

1. **Verified snapshot pattern**  
   Regenerate the inventory from the current tree, stamp the evidence basis, and keep only live entries in the main body.

2. **Historical record pattern**  
   Freeze this document as a dated scaffold artifact and move all live inventory duties elsewhere.

3. **Hybrid pattern**  
   Keep the historical scaffold inventory in an appendix, but surface a generated live inventory at the top.

> [!TIP]
> The safest next move is the **verified snapshot pattern**.  
> It removes ambiguity, shortens reviewer time, and stops historical scaffold names from reading like current implementation claims.

---

[Back to top](#readme-structure-reconciliation-report)
