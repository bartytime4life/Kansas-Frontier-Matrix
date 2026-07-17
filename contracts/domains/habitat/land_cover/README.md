<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-land-cover-readme
title: Habitat Land Cover Contracts README
type: readme
version: v0.1
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Land-cover steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Schema and validation steward
  - OWNER_TBD — Policy and release steward
  - OWNER_TBD — Docs steward
created: 2026-07-16
updated: 2026-07-16
policy_label: public-with-gates; readme; semantic-contracts; habitat; land-cover; source-role-aware; evidence-bound; release-gated
tags: [kfm, contracts, habitat, land_cover, README, LandCoverObservation, ClassSchemeProfile, CoverClassCrosswalk, LandCoverChangeSummary, ModelRunReceipt, UncertaintySurface, correction, rollback]
related:
  - ../README.md
  - ../ecoregions/README.md
  - ../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../schemas/contracts/v1/domains/habitat/land_cover/README.md
  - ../../../../fixtures/domains/habitat/land_cover/
  - ../../../../tests/domains/habitat/land_cover/README.md
  - ../../../../tools/validators/domains/habitat/README.md
  - ../../../../policy/domains/habitat/land_cover/
  - ../../../../pipelines/domains/habitat/land_cover/README.md
  - ../../../../pipeline_specs/habitat/land_cover/README.md
notes:
  - "Directory README required by docs/doctrine/directory-rules.md section 15."
  - "This directory is authoritative for Habitat land-cover semantic-contract meaning only; it does not own machine shape, executable validation, policy, data, or release authority."
  - "All six direct contract documents are draft and PROPOSED. Five paired schemas exist as permissive scaffolds; the ModelRunReceipt schema was not found. Field-level enforcement remains NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

# Habitat Land Cover Contracts

`contracts/domains/habitat/land_cover/`

## Purpose

This folder owns the semantic meaning, invariants, and anti-collapse boundaries for Habitat land-cover contract objects. It keeps observations, classification schemes, crosswalks, change summaries, model-run receipts, and uncertainty distinct before schemas, validators, pipelines, policy, release, API, map, or AI surfaces use them.

## Authority level

**Canonical responsibility lane for Habitat land-cover semantic-contract Markdown.** Files here define object meaning and field intent under the `contracts/` root; they do not provide machine-checkable shape or executable enforcement.

Authority is deliberately split:

| Concern | Authority |
|---|---|
| Land-cover object meaning and invariants | This directory |
| Machine-checkable field shape | `schemas/contracts/v1/domains/habitat/land_cover/` |
| Admissibility and sensitivity decisions | `policy/domains/habitat/land_cover/` and `policy/sensitivity/habitat/` |
| Executable validation and behavioral proof | `tools/validators/`, `fixtures/`, and `tests/` |
| Source identity, role, rights, and cadence | `data/registry/sources/habitat/` |
| Processing and configuration | `pipelines/domains/habitat/land_cover/` and `pipeline_specs/habitat/land_cover/` |
| Publication, correction, and rollback decisions | `release/` |

## Status

**PROPOSED / NEEDS VERIFICATION before promotion.** The directory and six semantic-contract documents are confirmed present. Their prose is draft contract guidance, not proof that consumers or enforcement exist.

Current enforcement posture:

- `observation`, `class_scheme`, `crosswalk`, `change_summary`, and `uncertainty` have paired JSON Schema files, but each schema has empty `properties`, no required fields, and `additionalProperties: true`.
- `model_run_receipt.md` has no paired schema at `schemas/contracts/v1/domains/habitat/land_cover/model_run_receipt.schema.json` in the inspected tree.
- `tools/validators/domains/habitat/validate_schema.py` raises `NotImplementedError` and `validate_model_run_receipt.py` is a `PROPOSED` placeholder.
- No executable test modules were found below `tests/domains/habitat/land_cover/`; the current child lanes are README-level plans.
- The object-family names, field constraints, fixture corpus, validator behavior, policy rules, CI wiring, and release integration therefore remain **NEEDS VERIFICATION**.

## What belongs here

- Directory orientation for the Habitat land-cover semantic-contract lane.
- Markdown contracts defining one Habitat land-cover object family or support object.
- Object identity, field intent, invariants, source-role boundaries, temporal and spatial scope, evidence expectations, and model-versus-observation rules.
- Semantic requirements for correction, supersession, and rollback references.
- Compatibility notes for an accepted contract rename or version change, when governed by the required ADR and migration work.

New files belong here only when their primary responsibility is **semantic meaning** and the object cannot be represented by an existing Habitat or shared contract.

## What does NOT belong here

- JSON Schema, JSON-LD contexts, or other machine-shape artifacts.
- Validator code, test modules, fixtures, golden outputs, or CI configuration.
- Policy rules, sensitivity decisions, review records, or release approvals.
- Source descriptors, source exports, RAW/WORK/QUARANTINE/PROCESSED data, catalogs, triplets, proofs, emitted receipts, tiles, or public artifacts.
- Pipeline code, pipeline specifications, renderer logic, API payloads, UI components, Focus Mode content, or generated AI claims.
- Species or plant occurrence truth, critical-habitat designation truth, crop truth, hydrology truth, soil truth, hazard truth, land/title truth, or publication authority.
- Silent class recodes, modeled-as-observed claims, or the treatment of a receipt, schema pass, map layer, or generated summary as evidence by itself.

## Inputs

Contract authors use:

- Habitat doctrine and the land-cover sublane charter under `docs/domains/habitat/`;
- admitted source-family and SourceDescriptor evidence from `data/registry/sources/habitat/`;
- reviewed object-family decisions, schema-home rules, and relevant ADRs;
- paired schema, fixture, test, validator, policy, and release evidence from their owning roots; and
- steward-reviewed correction or supersession decisions.

Source rasters, lifecycle records, model outputs, and generated summaries are not authored into this folder.

## Outputs

This folder supplies semantic definitions and review vocabulary to schema authors, validator and fixture authors, pipeline implementers, policy reviewers, release stewards, and governed downstream interfaces.

It emits no source data, processed data, proof, policy decision, release manifest, public layer, API response, or AI answer. A contract file does not promote an object or authorize publication.

## Validation

Review each change against the following checks:

1. Confirm the file describes semantic meaning rather than machine shape, policy, execution, data, or release state.
2. Preserve distinct identities for `LandCoverObservation`, `ClassSchemeProfile`, `CoverClassCrosswalk`, `LandCoverChangeSummary`, `ModelRunReceipt`, and `UncertaintySurface`.
3. Confirm every claimed schema, fixture, validator, test, policy, source, and release path exists; label absent or incomplete enforcement `PROPOSED` or `NEEDS VERIFICATION`.
4. Check paired schemas under `schemas/contracts/v1/domains/habitat/land_cover/` for non-empty constraints before claiming field-level enforcement.
5. Require explicit source role, source vintage, class-scheme/crosswalk posture, spatial and temporal scope, evidence, uncertainty, policy, review, correction, and rollback semantics where material.
6. Reject silent recoding, modeled-as-observed output, occurrence/regulatory truth collapse, and any contract-to-publication shortcut.
7. Run repository Markdown/link checks and `git diff --check` available to the change; do not describe the placeholder Habitat validators as passing enforcement.

Active land-cover-specific validator and CI coverage is **not confirmed**. Promotion requires implemented validators, valid and invalid fixtures, executable tests, and verified CI wiring rather than README claims alone.

## Review burden

Changes require review by the Habitat domain steward, land-cover steward, and contract steward. Add schema/validation review when fields or pairing expectations change; source/evidence review for provenance semantics; and policy, sensitivity, release, and correction review when public or sensitive behavior could change.

**CODEOWNERS posture:** CONFIRMED. [`.github/CODEOWNERS`](../../../../.github/CODEOWNERS) assigns the repository wildcard to `@kfm/maintainers` and specifically routes `/contracts/` changes to `@kfm/contract-stewards`. The `OWNER_TBD` domain-role entries above remain assignment gaps; they do not replace that automated contract-steward route.

## Related folders

| Folder | Relationship |
|---|---|
| [`../`](../README.md) | Parent Habitat semantic-contract lane. |
| [`../ecoregions/`](../ecoregions/README.md) | Adjacent Habitat regionalization-context contracts; not land-cover identity. |
| [`../../../../docs/domains/habitat/`](../../../../docs/domains/habitat/README.md) | Human-facing Habitat doctrine and source-family guidance. |
| [`../../../../schemas/contracts/v1/domains/habitat/land_cover/`](../../../../schemas/contracts/v1/domains/habitat/land_cover/README.md) | Paired machine-shape lane. |
| `../../../../fixtures/domains/habitat/land_cover/` | Synthetic child fixture families; no parent `README.md` was confirmed. |
| [`../../../../tests/domains/habitat/land_cover/`](../../../../tests/domains/habitat/land_cover/README.md) | Planned behavioral proof lanes. |
| [`../../../../tools/validators/domains/habitat/`](../../../../tools/validators/domains/habitat/README.md) | Habitat validator lane; current scripts are placeholders. |
| `../../../../policy/domains/habitat/land_cover/` | Policy-family placeholders; no active rule files were confirmed. |
| [`../../../../pipelines/domains/habitat/land_cover/`](../../../../pipelines/domains/habitat/land_cover/README.md) | Executable processing responsibility. |
| [`../../../../pipeline_specs/habitat/land_cover/`](../../../../pipeline_specs/habitat/land_cover/README.md) | Declarative processing responsibility. |
| [`../../../../data/registry/sources/habitat/`](../../../../data/registry/sources/habitat/README.md) | Habitat source descriptors, including NLCD, NWI, and GAP/LANDFIRE profiles. |
| `../../../../release/` | Publication, correction, and rollback authority; no `release/manifests/habitat/` path was confirmed. |

## ADRs

- [`ADR-0001 — Schema Home`](../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) is `proposed` but reflects the Directory Rules boundary: `contracts/` owns meaning and `schemas/contracts/v1/` owns machine shape.
- [`ADR-0011 — Receipts vs Proofs vs Manifests vs Catalog Separation`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) is `proposed` and applies to `ModelRunReceipt` separation: a receipt is not proof, catalog truth, or publication.
- No accepted land-cover-specific ADR was confirmed during this review. A rename that changes object meaning, a new canonical root, or a schema-home change requires ADR-backed migration rather than a README-only decision.

## Current contract inventory

| Contract | Semantic responsibility | Enforcement posture |
|---|---|---|
| [`observation.md`](observation.md) | `LandCoverObservation`: governed categorical or continuous classification over declared space and time. | Paired schema is a permissive `PROPOSED` scaffold. |
| [`class_scheme.md`](class_scheme.md) | `ClassSchemeProfile`: versioned classification vocabulary and class identity. | Paired schema is a permissive `PROPOSED` scaffold. |
| [`crosswalk.md`](crosswalk.md) | `CoverClassCrosswalk`: explicit, reviewed mapping between schemes; no silent recode. | Paired schema is a permissive `PROPOSED` scaffold. |
| [`change_summary.md`](change_summary.md) | `LandCoverChangeSummary`: derived comparison between governed observations. | Paired schema is a permissive `PROPOSED` scaffold; threshold enforcement is unverified. |
| [`model_run_receipt.md`](model_run_receipt.md) | `ModelRunReceipt`: process memory for modeled or transformed output, not proof or release. | Paired schema absent; validator file is a placeholder. |
| [`uncertainty.md`](uncertainty.md) | `UncertaintySurface`: accuracy, footprint, source-vintage, crosswalk, model, and display caveats. | Paired schema is a permissive `PROPOSED` scaffold. |

## Correction and rollback

Correct or roll back a contract change when it creates parallel authority, overstates enforcement, collapses object families or source roles, permits silent recoding, relabels modeled output as observed, or implies that semantic prose authorizes publication.

A correction must identify affected contract paths and update paired schema links, fixture/test plans, validator references, policy references, downstream consumers, and correction/supersession notes where they exist. If a released artifact depended on the changed meaning, the release steward must handle its correction notice, rollback target, replacement reference, and public-cache invalidation under `release/`; deleting or rewriting contract history is not a substitute.

## Last reviewed

2026-07-16 — draft directory contract; owner assignment, fielded schemas, land-cover validators, executable tests, policy enforcement, CI coverage, and release integration remain **NEEDS VERIFICATION**.
