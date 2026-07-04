# `schemas/contracts/v1/domains/hazards/` — Hazards Domain Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-hazards-readme
title: schemas/contracts/v1/domains/hazards/ — Hazards Domain Schema Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <hazards-domain-steward>
  - <contract-steward>
  - <validation-steward>
  - <freshness-steward>
  - <policy-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, hazards, receipts, warning-context, freshness, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-hazards-red)
![posture](https://img.shields.io/badge/posture-domain--schema--index-orange)
![canonical](https://img.shields.io/badge/canonical-PROPOSED%20%2F%20CONFLICTED-yellow)
![boundary](https://img.shields.io/badge/boundary-not%20life--safety%20authority-critical)

## Purpose

`schemas/contracts/v1/domains/hazards/` is the draft Hazards domain schema lane.

This path is for machine-checkable Hazards schema shapes: JSON Schema files, schema-family README files, schema index notes, migration notes, and links to paired contracts, fixtures, validators, registry records, tests, policy references, source-registry references, freshness references, correction references, rollback references, and release references.

This path is not a home for Hazards contract prose, policy rules, validator code, packages, pipelines, lifecycle data, source registry records, emitted receipts, proof outputs, EvidenceBundles, catalog records, release records, review records, public map/API artifacts, operational alerts, or life-safety instructions.

This README is documentation only. It is not itself a schema file, contract prose, policy, validator code, pipeline code, lifecycle data, registry data, proof output, receipt instance, source descriptor instance, emergency alert authority, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Hazards domain schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/hazards/` |
| Status | Draft |
| Authority level | Domain schema index guidance. Schema files, paired contracts, registry records, validators, fixtures, tests, ADRs, policy records, release records, and steward decisions outrank this README. |
| Path posture | PROPOSED / CONFLICTED. This path exists in the repo as a scaffold, while Hazards architecture records a non-domain schema-home note for Hazards pending ADR/schema-home resolution. |
| Canonical posture | ADR-0001 says domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`, but Hazards architecture records an unresolved Hazards-specific schema-home segment conflict. |
| Concrete schema inventory | NEEDS VERIFICATION. Current-session search did not confirm concrete `.schema.json` files under this path. |
| Known child lanes | `receipts/` README exists as a draft Hazards receipts schema index. |
| Hazards boundary | KFM Hazards is not an emergency alert system or life-safety authority. Official sources remain the authority for live safety action. |
| Required reviewers | Schema steward, Hazards domain steward, receipt steward where applicable, contract steward, validation steward, freshness steward, policy/release stewards where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session Directory Rules evidence confirms field-level shape belongs under `schemas/`, while lifecycle data, registries, proofs, receipts, policy decisions, and release materials are separate responsibility roots and parallel homes require ADR review.

Current-session evidence confirms this README previously claimed broadly that docs, contracts, schemas, policies, fixtures, tests, packages, pipelines, registries, and data lifecycle artifacts could belong here. This update corrects that boundary: this path is schema-shape only.

Current-session evidence confirms `schemas/contracts/v1/domains/hazards/receipts/README.md` exists as a draft Hazards receipts schema index and marks concrete receipt schemas NEEDS VERIFICATION.

Current-session search did not confirm concrete Hazards `.schema.json` files under `schemas/contracts/v1/domains/hazards/`.

Current-session Hazards architecture evidence records a Hazards-specific schema-home conflict: it says an older/default Hazards schema home was `schemas/contracts/v1/hazards/`, while the `/domains/<x>/` form is flagged CONFLICTED pending ADR-S-01 / ADR-0001. This README therefore treats the requested path as present and useful, but not fully settled as canonical until the conflict is resolved.

Current-session Hazards architecture evidence also confirms the Hazards lane covers historical, regulatory, modeled, and operational-context hazard information for analysis and resilience, while refusing to act as life-safety alerting.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        └── domains/
            └── hazards/
                ├── README.md              # you are here
                └── receipts/
                    └── README.md          # draft receipt schema index

contracts/
└── domains/
    └── hazards/                           # semantic meaning; not schema shape

docs/
└── domains/
    └── hazards/                           # human-facing doctrine; not schema shape

data/
├── receipts/hazards/                      # emitted process-memory receipts; not schema shape
├── proofs/hazards/                        # proof objects; not schema shape
└── catalog/domain/hazards/                # catalog/discovery; not schema shape

policy/
└── domains/hazards/                       # allow/deny/restrict/abstain; not schema shape

fixtures/
└── domains/hazards/                       # test examples; coverage NEEDS VERIFICATION

release/                                  # release decisions and records; not schema home
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/hazards/README.md` | Greenfield scaffold before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| Directory Rules | Confirms machine shape belongs under `schemas/`; parallel homes require ADR review. |
| `schemas/contracts/v1/domains/hazards/receipts/README.md` | Existing draft Hazards receipts schema index; concrete receipt schema inventory remains NEEDS VERIFICATION. |
| Search for Hazards schema files | Did not confirm concrete `.schema.json` files under this path in current-session search. |
| `data/receipts/hazards/README.md` | Hazards receipt process-memory lane; not proof, catalog, release, public, alert, or life-safety authority. |
| ADR-0011 | Proposed separation rule: receipt, proof, catalog, and publication are distinct families; schema homes remain governed by ADR-0001. |
| `docs/domains/hazards/ARCHITECTURE.md` | Hazards architecture; records schema-home conflict and establishes the life-safety boundary. |

This README does not verify complete Hazards schema coverage, schema registry entries, fixture coverage, validator wiring, CI behavior, source-admission behavior, freshness enforcement, policy behavior, release integration, emitted receipt instance layout, runtime behavior, public API behavior, or map rendering behavior.

## Current schema inventory

| Schema file | Paired contract | Status | Notes |
|---|---|---|---|
| No concrete `.schema.json` file confirmed in this edit | N/A | NEEDS VERIFICATION | Current-session search found Hazards docs/contracts/receipt lanes but did not confirm concrete Hazards schemas under this path. |

## Current child lanes

| Child path | Status | Responsibility |
|---|---|---|
| `receipts/` | Draft schema index / NEEDS VERIFICATION | Candidate receipt-shaped Hazards schema sublane. It does not store emitted receipts and does not become proof, catalog, policy, release, alert, or life-safety authority. |

## Candidate schema inventory

Hazards schema candidates below require steward review, schema files, paired contracts, fixtures, validators, registry records, freshness semantics, and CI support before promotion.

| Candidate schema | Status | Notes |
|---|---|---|
| `hazard_event.schema.json` | NEEDS VERIFICATION | Candidate historical or observed hazard event shape. |
| `hazard_context.schema.json` | NEEDS VERIFICATION | Candidate context envelope for regulatory, modeled, or operational context. |
| `warning_context.schema.json` | NEEDS VERIFICATION | Candidate operational warning/advisory/watch context shape; not life-safety authority. |
| `regulatory_hazard_area.schema.json` | NEEDS VERIFICATION | Candidate regulatory context shape such as NFHL-style areas; not observed inundation. |
| `remote_sensing_detection.schema.json` | NEEDS VERIFICATION | Candidate detection/candidate shape; not event confirmation by itself. |
| `exposure_summary.schema.json` | NEEDS VERIFICATION | Candidate exposure/resilience summary shape. |
| `hazard_timeline.schema.json` | NEEDS VERIFICATION | Candidate role-aware hazard timeline shape. |
| `freshness_envelope.schema.json` | NEEDS VERIFICATION | Candidate time/freshness/expiry support shape. |
| `domain_feature_identity.schema.json` | NEEDS VERIFICATION | Candidate deterministic identity support shape. |
| `domain_validation_report.schema.json` | NEEDS VERIFICATION | Candidate validation-report shape; not proof or release authority. |
| `receipts/source_intake_receipt.schema.json` | NEEDS VERIFICATION | Candidate source-intake process-memory receipt shape. |
| `receipts/freshness_receipt.schema.json` | NEEDS VERIFICATION | Candidate freshness-check receipt shape. |
| `receipts/model_run_receipt.schema.json` | NEEDS VERIFICATION | Candidate model/materialization receipt shape. |
| `receipts/release_support_receipt.schema.json` | NEEDS VERIFICATION | Candidate release-support receipt shape, not release authority. |

## Schema-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Domain schema index | List Hazards schema files and child schema lanes as they are verified. |
| Contract pairing | Link each schema to paired semantic contracts under `contracts/domains/hazards/` or another verified contract lane. |
| Path-conflict discipline | Keep the `/domains/hazards/` vs `v1/hazards/` conflict visible until ADR/steward resolution. |
| Life-safety boundary | Do not encode operational instructions, emergency directions, or public life-safety authority. |
| Freshness discipline | Preserve source time, issue time, expiry time, retrieval time, release time, and correction time where schemas eventually require them. |
| Boundary preservation | Keep policy, fixtures, validators, pipelines, lifecycle data, source registry records, receipt instances, proofs, catalog records, and release records in their own responsibility roots. |
| Adjacent-domain discipline | Hazards may reference Hydrology, Atmosphere, Geology, Soil, Agriculture, Settlements/Infrastructure, Roads/Rail/Trade, Archaeology, and People context, but must not replace their owned truth. |
| Drift prevention | Prevent duplicate canonical schema definitions across requested domain path, possible non-domain Hazards path, child lanes, cross-domain lanes, and common schema families. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Machine-checkable Hazards JSON Schema files once placement is confirmed.
- Hazards schema-family and child-lane README files.
- Schema index notes.
- Migration notes for Hazards schema placement.
- Drift notes about duplicate or stale Hazards schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, source-registry records, policy references, release references, correction references, rollback references, and tests.

## What does not belong here

- Contract prose.
- Policy rules or sensitivity decisions.
- Validator implementation code.
- Runtime code.
- Packages or pipeline implementation.
- Lifecycle data payloads.
- Source registry records or SourceDescriptor instances.
- Emitted receipt instances.
- Proof outputs or EvidenceBundles.
- Catalog records.
- Release records, release manifests, or release decisions.
- Public tiles, map/UI behavior, dashboards, screenshots, or generated summaries.
- Operational alert instructions, emergency directions, or life-safety guidance.
- Hydrology measurements, Atmosphere/Air observations, Geology truth, Soil truth, Agriculture truth, Settlements/Infrastructure truth, Roads/Rail/Trade truth, Archaeology truth, or People/living-person truth.
- Cross-domain schemas that belong under `schemas/contracts/v1/cross/` or another lowest-common responsibility root.
- Generic reusable schemas that belong under `schemas/contracts/v1/common/`.
- Claims that a schema is complete without fixtures, validators, registry records, and steward review support.

## Schema status values

Use finite status values where possible:

| Status | Meaning |
|---|---|
| `STUB` | Schema exists but is not field-complete. |
| `DRAFT_SCHEMA` | Schema has meaningful fields but still needs review and test support. |
| `ACTIVE_SCHEMA` | Schema has accepted contract pairing, fixtures, validator support, registry record, and review status. |
| `PATH_CONFLICT` | Schema placement is blocked by unresolved Hazards schema-home conflict. |
| `PROFILE` | Schema profiles a shared source, spatial, time, or common schema without creating duplicate authority. |
| `MIRROR` | Schema mirrors another accepted schema location. |
| `TRANSITIONAL` | Schema is awaiting migration to the accepted home. |
| `DEPRECATED` | Schema should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, review, or CI support has not been verified. |

## Minimal schema note

```markdown
# <hazards-schema-note-id>

## Status
STUB / DRAFT_SCHEMA / ACTIVE_SCHEMA / PATH_CONFLICT / PROFILE / MIRROR / TRANSITIONAL / DEPRECATED / NEEDS_VERIFICATION

## Schema path
<schemas/contracts/v1/domains/hazards/... or alternate path under review>

## Paired contract
<contracts/domains/hazards/... or N/A>

## Child lane
<root / receipts / other / N/A>

## Freshness posture
<source-time / issue-time / expiry-time / retrieval-time / release-time / correction-time / N/A / NEEDS VERIFICATION>

## Fixtures
<fixtures path or N/A>

## Validator
<tools/validators path or N/A>

## Policy and release references
<policy/release path or N/A>

## Notes
<short note grounded in repo evidence>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Schema has a stable `$id`.
- [ ] Schema has `$schema` set to JSON Schema draft 2020-12 unless an ADR says otherwise.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Hazards schema-home conflict is resolved or explicitly marked PROPOSED / CONFLICTED.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Freshness/expiry behavior is linked or marked NEEDS VERIFICATION where relevant.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Pipeline, policy, data, registry, proof, receipt, catalog, and release records remain outside `schemas/`.
- [ ] Hazards life-safety boundary is preserved.
- [ ] Adjacent-domain boundaries are preserved.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended schema filename pattern:

```text
<object_name>.schema.json
```

Examples:

```text
hazard_event.schema.json
hazard_context.schema.json
warning_context.schema.json
regulatory_hazard_area.schema.json
remote_sensing_detection.schema.json
exposure_summary.schema.json
hazard_timeline.schema.json
freshness_envelope.schema.json
domain_feature_identity.schema.json
domain_validation_report.schema.json
receipts/source_intake_receipt.schema.json
receipts/freshness_receipt.schema.json
receipts/model_run_receipt.schema.json
receipts/release_support_receipt.schema.json
```

Use lowercase snake_case for schema filenames unless the schema registry or ADR specifies otherwise. Do not silently create duplicate schemas across `schemas/contracts/v1/domains/hazards/`, `schemas/contracts/v1/hazards/`, cross-domain, or common schema paths.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/hazards/`.
- [ ] Resolve the Hazards schema-home conflict between the requested `/domains/hazards/` path and the non-domain `schemas/contracts/v1/hazards/` note in Hazards architecture.
- [ ] Confirm complete Hazards schema inventory.
- [ ] Confirm whether concrete schema files exist under alternate casing or alternate paths.
- [ ] Confirm paired contract paths for all accepted schemas.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm freshness/expiry fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm policy, source-registry, release, correction, and rollback references for Hazards schemas.
- [ ] Confirm whether `schemas/README.md` should index this Hazards domain schema lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield scaffold |
| Next review trigger | Hazards schema-home resolution, new Hazards schema, child-lane decision, schema-home migration, validator update, fixture update, schema registry update, ADR update, Hazards contract update, freshness-policy update, policy/release reference update, or compatibility-lane decision |
