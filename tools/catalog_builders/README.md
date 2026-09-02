<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-catalog-builders-readme
title: Catalog Builders README
type: tool-readme
version: v0.1
status: draft; greenfield-stub-replaced; catalog-builder-tooling-lane; PROPOSED / NEEDS VERIFICATION
owners:
  - OWNER_TBD - Tooling steward
  - OWNER_TBD - Catalog steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-07
updated: 2026-07-07
policy_label: public-doc; tools; catalog-builders; catalog; stac; dcat; prov; no-network-default; release-gated
tags: [kfm, tools, catalog-builders, data-catalog, STAC, DCAT, PROV, EvidenceBundle, CatalogBuildReceipt, release-gated, NEEDS_VERIFICATION]
related:
  - ../README.md
  - ../../data/catalog/README.md
  - ../../data/triplets/
  - ../../data/processed/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../pipelines/catalog/README.md
  - ../../pipeline_specs/
  - ../../schemas/
  - ../../contracts/
  - ../../policy/
  - ../../release/
  - ../../tests/pipelines/README.md
notes:
  - "This README replaces the greenfield stub at tools/catalog_builders/README.md."
  - "tools/README.md defines tools/catalog_builders/ as programs that compose data/catalog records from validated data/processed outputs."
  - "Catalog builder tools may prepare catalog candidates and proposed catalog records; they do not approve publication, create source truth, replace EvidenceBundle support, or make release decisions."
  - "Executable inventory, CLI shape, catalog schemas, fixture coverage, CI wiring, receipt output, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Catalog builders

> Tooling lane for catalog-builder helpers under `tools/catalog_builders/`. Use this directory for executable tools that compose catalog-stage records from validated processed inputs while preserving evidence, policy, receipt, triplet, and release boundaries.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tools" src="https://img.shields.io/badge/root-tools%2F-blue">
  <img alt="Lane: catalog builders" src="https://img.shields.io/badge/lane-catalog__builders-purple">
  <img alt="Lifecycle: processed to catalog" src="https://img.shields.io/badge/lifecycle-PROCESSED%E2%86%92CATALOG-informational">
  <img alt="Release: gated" src="https://img.shields.io/badge/release-gated-critical">
</p>

**Path:** `tools/catalog_builders/README.md`  
**Status:** draft / greenfield stub replaced / catalog-builder tooling lane / PROPOSED until executable inventory is verified  
**Owning root:** `tools/`  
**Lane family:** `catalog_builders`  
**Default posture:** deterministic, no-network by default, explicit inputs, receipt-aware outputs  
**Truth posture:** CONFIRMED target file existed as a greenfield stub before replacement; CONFIRMED `tools/README.md` lists `tools/catalog_builders/` as catalog-builder tooling; CONFIRMED `data/catalog/` is catalog-stage data and not release authority; CONFIRMED `pipelines/catalog/` prepares catalog candidates and is not publication authority; NEEDS VERIFICATION for actual helper files, CLI names, schemas, tests, CI, receipts, and pass rates.

---

## Scope

Use `tools/catalog_builders/` for repo-wide executable helpers that compose catalog records and indexes.

In scope:

- STAC, DCAT, PROV, and KFM catalog record builders;
- domain catalog candidate builders;
- catalog index builders;
- catalog quality summary builders;
- release-reference catalog manifest helpers;
- helper code that emits catalog-build receipts or receipt-ready metadata.

Out of scope:

- catalog data records themselves;
- pipeline orchestration;
- source connectors;
- schemas, contracts, or policy rules;
- EvidenceBundle/proof authority;
- release decisions or public publication.

---

## Repo fit

| Responsibility | Correct home | Relationship |
|---|---|---|
| Catalog-builder helper code | `tools/catalog_builders/` | This lane. |
| Catalog pipeline orchestration | `pipelines/catalog/` | Composes the flow; may call these tools. |
| Catalog job specs | `pipeline_specs/` | Declarative configuration, not code. |
| Catalog-stage records | `data/catalog/` | Output data lane, not tool code. |
| Graph/triplet projection | `data/triplets/` | Paired CATALOG/TRIPLET projection. |
| Processed inputs | `data/processed/` | Upstream validated data. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Audit/proof records, not tool code. |
| Schemas/contracts/policy | `schemas/`, `contracts/`, `policy/` | Authority roots read by tools. |
| Release decisions | `release/` | Publication authority. |
| Tests and fixtures | `tests/`, `fixtures/`, `tests/fixtures/` | Test and sample input homes. |

> [!IMPORTANT]
> `tools/catalog_builders/` must not become `data/catalog/`, `data/triplets/`, `data/processed/`, `data/receipts/`, `data/proofs/`, `release/`, a schema root, a policy root, a contract root, a fixture home, or a public artifact root.

---

## Catalog-builder rule

Catalog builders prepare catalog candidates. They do not publish.

| Expectation | Required posture |
|---|---|
| Explicit input | Builders receive processed records, refs, manifests, or fixture paths explicitly. |
| Evidence-aware | Catalog records keep evidence/proof pointers where material. |
| Policy-aware | Rights, sensitivity, access, and review posture are preserved. |
| Release-gated | Output may support release review but does not approve publication. |
| Receipt-ready | Runs should be able to emit or reference a CatalogBuildReceipt where material. |
| Deterministic | Same inputs and config should produce stable catalog output. |
| Fail closed | Missing validation, unresolved evidence, policy gaps, or malformed inputs stop the build. |

---

## Expected helper families

| Family | Purpose | Status |
|---|---|---|
| `build_stac_catalog` | Build STAC-style catalog records from validated processed inputs. | PROPOSED. |
| `build_dcat_catalog` | Build DCAT-style catalog records. | PROPOSED. |
| `build_prov_catalog` | Build PROV-style catalog/provenance records. | PROPOSED. |
| `build_domain_catalog` | Build domain-scoped catalog candidates. | PROPOSED. |
| `build_catalog_index` | Compose catalog lookup indexes. | PROPOSED. |
| `build_quality_summary` | Emit catalog quality summaries pointing to validation and receipt support. | PROPOSED. |
| `link_release_refs` | Build release-reference pointers without approving release. | PROPOSED. |

---

## Inputs and outputs

Accepted inputs:

- validated `data/processed/` refs or fixture equivalents;
- source descriptor refs, EvidenceRef/EvidenceBundle refs, validation refs, policy decisions, and release/correction/rollback refs;
- schemas, contracts, and policy definitions as read-only authority references.

Expected outputs:

- candidate catalog records;
- catalog indexes;
- quality summaries;
- receipt-ready metadata;
- proposed release-reference catalog manifests.

Final catalog records belong under `data/catalog/`. Public materialized outputs belong under `data/published/` only after governed release.

---

## Suggested layout

```text
tools/catalog_builders/
|-- README.md
|-- build_stac_catalog.PROPOSED
|-- build_dcat_catalog.PROPOSED
|-- build_prov_catalog.PROPOSED
|-- build_domain_catalog.PROPOSED
|-- build_catalog_index.PROPOSED
|-- build_quality_summary.PROPOSED
`-- link_release_refs.PROPOSED
```

The layout is schematic. Actual filenames, language, CLI shape, package manager, and CI wiring remain NEEDS VERIFICATION.

---

## Run posture

No executable command was verified while authoring this README.

```bash
: "PROPOSED / NEEDS VERIFICATION"
python -m tools.catalog_builders --help
```

Default operation should be local and no-network. Live source access belongs in connectors or explicitly gated pipeline tiers, not default catalog-builder tools.

---

## Maintenance checklist

- [ ] Keep catalog-builder code in this lane and catalog records in `data/catalog/`.
- [ ] Keep orchestration in `pipelines/catalog/` and job specs in `pipeline_specs/`.
- [ ] Preserve EvidenceBundle, policy, validation, release, correction, and rollback refs where material.
- [ ] Do not turn catalog metadata into source truth or release approval.
- [ ] Add tests and fixtures before using a builder in promotion or release gates.
- [ ] Document CLI inputs, outputs, exit codes, and receipt behavior once implemented.

---

## Verification status

| Item | Status |
|---|---|
| Target README path | CONFIRMED; greenfield stub replaced. |
| Parent `tools/` boundary | CONFIRMED in `tools/README.md`. |
| `tools/catalog_builders/` placement | CONFIRMED in `tools/README.md`. |
| `data/catalog/` lifecycle boundary | CONFIRMED in `data/catalog/README.md`. |
| Catalog pipeline boundary | CONFIRMED in `pipelines/catalog/README.md`. |
| Executable helper inventory | NEEDS VERIFICATION. |
| CLI shape and language/runtime | NEEDS VERIFICATION. |
| Catalog schemas and fixtures | NEEDS VERIFICATION. |
| Tests and CI wiring | NEEDS VERIFICATION. |
| Tests and validators | NOT RUN. |
