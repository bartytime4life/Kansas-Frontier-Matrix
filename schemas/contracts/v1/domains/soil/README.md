# `schemas/contracts/v1/domains/soil/` — Soil Domain Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-soil-readme
title: schemas/contracts/v1/domains/soil/ — Soil Domain Schema Index
type: readme; schema-lane-readme; domain-schema-index
version: v1
status: draft; scaffolded-schema-lane; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Soil domain steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — greenfield scaffold existed before v1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; soil; source-role-aware; support-type-separation; lifecycle-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, domains, soil, ssurgo, gssurgo, sda, map-unit, component, horizon, soil-moisture, evidence-bundle, decision-envelope, layer-manifest, release-manifest, rollback]
related:
  - ../../../../README.md
  - ../../../../../contracts/domains/soil/README.md
  - ../../../../../docs/domains/soil/README.md
  - ../../../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../../../docs/domains/soil/ARCHITECTURE.md
  - ../../../../../docs/domains/soil/API_CONTRACTS.md
  - ../../../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../../../docs/sources/catalog/nrcs/ssurgo.md
  - ../../../../../docs/sources/catalog/nrcs/gssurgo.md
  - ../../../../../policy/domains/soil/README.md
  - ../../../../../fixtures/domains/soil/
  - ../../../../../tests/domains/soil/
  - ../../../../../tools/validators/
  - ../../../../../release/candidates/soil/
notes:
  - "Expanded from a short greenfield scaffold at schemas/contracts/v1/domains/soil/README.md."
  - "This file is a schema-lane README only: it documents the machine-shape home for Soil schemas."
  - "Semantic contracts, policy, tests, fixtures, packages, pipelines, source registry records, lifecycle data, release manifests, receipts, proofs, and public artifacts remain in their own responsibility roots."
  - "Current GitHub search surfaced concrete Soil schema scaffold files, but opened examples are still field-empty PROPOSED scaffolds; schema maturity remains NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-soil-8B4513)
![shape](https://img.shields.io/badge/authority-machine--shape-purple)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![support](https://img.shields.io/badge/support--type-separation-critical)
![release](https://img.shields.io/badge/publication-release--gated-orange)

> **Purpose.** `schemas/contracts/v1/domains/soil/` is the draft Soil domain schema lane: the machine-checkable JSON Schema home for Soil object shapes and schema-family indexes.
>
> **One-line boundary.** Schemas say what Soil JSON objects look like; contracts say what Soil objects mean; policy decides whether and how they may be used; release records decide what becomes public.

---

## Quick jumps

[Scope](#scope) · [Status and authority](#status-and-authority) · [Placement basis](#placement-basis) · [Repo fit](#repo-fit) · [Current schema inventory](#current-schema-inventory) · [Candidate gaps](#candidate-gaps) · [Schema-lane rules](#schema-lane-rules) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Support-type separation](#support-type-separation) · [Review checklist](#review-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Scope

This folder is the **schema responsibility-root lane** for the Soil domain.

It may host JSON Schema files and schema-index documentation for Soil object families such as `SoilMapUnit`, `SoilComponent`, `Horizon`, `SoilProperty`, `HydrologicSoilGroup`, `SoilMoistureObservation`, `Pedon`, `SoilProfileView`, `ErosionRisk`, `SuitabilityRating`, `ComponentHorizonJoin`, `SoilTimeCaveat`, and Soil-specific governed envelopes or projections.

It must not host semantic contract prose, policy rules, fixtures, tests, validator implementation code, packages, pipelines, source registry records, source data, lifecycle data, emitted receipts, proof objects, catalog records, release decisions, or public artifacts.

> [!IMPORTANT]
> A schema is a machine-shape contract. It can constrain fields, types, identifiers, enum values, required properties, and references. It does not admit a source, prove evidence closure, approve public release, publish a map layer, or authorize an AI answer.

---

## Status and authority

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/domains/soil/README.md`. | **CONFIRMED** |
| What is the owning root? | `schemas/`, because this lane owns machine-checkable shape. | **CONFIRMED** |
| What is the domain segment? | `soil`. | **CONFIRMED** |
| Is this path the only possible historical schema path mentioned in KFM materials? | No. Soil canonical-path doctrine records variance between `schemas/contracts/v1/domains/soil/` and flatter atlas-era forms. | **NEEDS VERIFICATION / ADR-sensitive** |
| Are concrete schema files present under this folder? | Current GitHub search surfaced several `.schema.json` files under this path. | **CONFIRMED path presence** |
| Are the schemas field-complete and production-ready? | Not proven. Opened examples are `PROPOSED` scaffolds with empty `properties` and permissive `additionalProperties`. | **NEEDS VERIFICATION** |
| Does this README itself validate data? | No. It is documentation and schema-lane navigation only. | **CONFIRMED** |

Schema files, paired semantic contracts, fixtures, validators, registry records, policy decisions, release records, ADRs, and steward decisions outrank this README.

---

## Placement basis

Current KFM placement doctrine separates responsibility roots:

- `contracts/` defines object meaning.
- `schemas/` defines machine-checkable shape.
- `policy/` decides allow, deny, restrict, or abstain behavior.
- `tests/` and `fixtures/` prove behavior and provide examples.
- `data/` holds lifecycle data and registry/proof/receipt surfaces.
- `release/` holds release decisions, manifests, rollback cards, and correction notices.

For domain-specific material, the domain name appears as a **segment** under the proper responsibility root, not as a root-level folder. This file therefore belongs under:

```text
schemas/contracts/v1/domains/soil/README.md
```

This placement matches the schema-home convention and the Soil canonical-path guidance for the machine-shape lane. Any competing flat path or mirrored schema path should stay visible as drift, migration, or ADR material until resolved.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        └── domains/
            └── soil/
                ├── README.md                         # this file
                ├── *.schema.json                     # Soil machine shapes
                └── <child-lane>/README.md            # only when steward-approved

contracts/
└── domains/
    └── soil/                                         # semantic meaning; not JSON Schema

docs/
└── domains/
    └── soil/                                         # domain doctrine and architecture

policy/
└── domains/
    └── soil/                                         # allow / deny / restrict / abstain

fixtures/
└── domains/
    └── soil/                                         # examples and validator inputs

tests/
└── domains/
    └── soil/                                         # behavior and validation proof

data/                                                   # lifecycle, registry, receipts, proofs, catalog, publication

release/                                                # promotion, release, correction, rollback
```

This README should link across those lanes, but it must not collapse them into this folder.

---

## Current schema inventory

Current GitHub search surfaced the following files under `schemas/contracts/v1/domains/soil/`. Path presence does not prove field completeness, fixture coverage, validator wiring, CI coverage, or release readiness.

| Schema file | Primary role | Maturity note |
|---|---|---|
| `catalog_matrix.schema.json` | Soil catalog-closure / digest matrix shape. | **NEEDS VERIFICATION** |
| `correction_notice.schema.json` | Soil correction notice shape or domain profile. | **NEEDS VERIFICATION** |
| `decision_envelope.schema.json` | Generic or domain-profiled finite outcome envelope. | **NEEDS VERIFICATION** |
| `domain_feature_identity.schema.json` | Soil feature identity shape. | **NEEDS VERIFICATION** |
| `domain_layer_descriptor.schema.json` | Soil layer descriptor shape; not release authority. | **NEEDS VERIFICATION** |
| `domain_observation.schema.json` | Soil domain observation envelope. | **NEEDS VERIFICATION** |
| `domain_validation_report.schema.json` | Soil validation report shape. | **NEEDS VERIFICATION** |
| `evidence_bundle.schema.json` | Evidence bundle shape or soil profile of shared evidence shape. | **NEEDS VERIFICATION** |
| `evidence_drawer_payload.schema.json` | Evidence Drawer payload projection for Soil UI. | **NEEDS VERIFICATION** |
| `layer_manifest.schema.json` | Soil layer manifest shape; not publication decision. | **NEEDS VERIFICATION** |
| `promotion_decision.schema.json` | Soil promotion decision shape or domain profile. | **NEEDS VERIFICATION** |
| `release_manifest.schema.json` | Soil release manifest shape or domain profile. | **NEEDS VERIFICATION** |
| `rollback_card.schema.json` | Soil rollback card shape or domain profile. | **NEEDS VERIFICATION** |
| `run_receipt.schema.json` | Soil run receipt shape or domain profile. | **NEEDS VERIFICATION** |
| `soil_decision_envelope.schema.json` | Soil-specific finite outcome envelope. | **NEEDS VERIFICATION** |
| `soil_evidencebundle.schema.json` | Soil-specific EvidenceBundle profile. | **NEEDS VERIFICATION** |
| `soil_map_unit.schema.json` | Soil map unit shape; opened example is a `PROPOSED` scaffold. | **NEEDS VERIFICATION** |
| `soil_moisture_dedupe_key.schema.json` | Soil moisture deduplication key shape. | **NEEDS VERIFICATION** |
| `soil_moisture_reading.schema.json` | Soil moisture reading shape; opened example is a `PROPOSED` scaffold. | **NEEDS VERIFICATION** |
| `soil_moisture_units_time.schema.json` | Soil moisture unit/time normalization shape. | **NEEDS VERIFICATION** |
| `source_state_hash.schema.json` | Source-state hash / change-detection shape. | **NEEDS VERIFICATION** |
| `ssurgo_source_descriptor.schema.json` | SSURGO source descriptor profile. | **NEEDS VERIFICATION** |

> [!NOTE]
> Inventory should be regenerated before promotion using a repository tree command or schema registry, not by relying on this README alone.

---

## Candidate gaps

The contract lane already names additional Soil object families that may need paired schema files or explicit decisions not to create duplicate domain schemas.

| Candidate schema | Paired semantic contract | Status |
|---|---|---|
| `soil_component.schema.json` | `contracts/domains/soil/soil_component.md` | **NEEDS VERIFICATION** |
| `horizon.schema.json` | `contracts/domains/soil/horizon.md` | **NEEDS VERIFICATION** |
| `component_horizon_join.schema.json` | `contracts/domains/soil/component_horizon_join.md` | **NEEDS VERIFICATION** |
| `soil_property.schema.json` | `contracts/domains/soil/soil_property.md` | **NEEDS VERIFICATION** |
| `hydrologic_soil_group.schema.json` | `contracts/domains/soil/hydrologic_soil_group.md` | **NEEDS VERIFICATION** |
| `soil_moisture_observation.schema.json` | `contracts/domains/soil/soil_moisture_observation.md` | **NEEDS VERIFICATION** |
| `pedon_soil_profile_view.schema.json` | `contracts/domains/soil/pedon_soil_profile_view.md` | **NEEDS VERIFICATION** |
| `erosion_risk.schema.json` | `contracts/domains/soil/erosion_risk.md` | **NEEDS VERIFICATION** |
| `suitability_rating.schema.json` | `contracts/domains/soil/suitability_rating.md` | **NEEDS VERIFICATION** |
| `soil_time_caveat.schema.json` | `contracts/domains/soil/soil_time_caveat.md` | **NEEDS VERIFICATION** |

A candidate should become a schema file only when the object meaning, source role, support type, temporal model, fixtures, validation behavior, and policy/release implications are understood well enough to avoid parallel authority.

---

## Schema-lane rules

| Rule | Requirement |
|---|---|
| Stable identity | Every schema should have a stable `$id` in the `kfm://schemas/contracts/v1/domains/soil/...` namespace or another ADR-approved namespace. |
| JSON Schema version | Use JSON Schema draft 2020-12 unless an ADR says otherwise. |
| Contract pairing | Link each schema to its semantic contract under `contracts/domains/soil/` or mark the pairing **NEEDS VERIFICATION**. |
| Support-type separation | Do not let static survey, gridded derivative, station reading, satellite grid, pedon/profile, or interpretation records masquerade as each other. |
| Temporal explicitness | Preserve valid time, source time, observed time, retrieval time, release time, and correction time where material. |
| Source identity | Preserve source system, source role, source version/vintage, retrieval basis, query hash, and digest fields where material. |
| Evidence closure | Evidence-related schemas should reference or profile EvidenceBundle / EvidenceRef without turning this schema lane into a proof store. |
| Policy separation | Sensitivity, rights, redaction, public-safe geometry, and release decisions belong in policy and release lanes. Schemas may include fields for decisions; they do not make decisions. |
| Release separation | ReleaseManifest, PromotionDecision, CorrectionNotice, and RollbackCard schemas may define shape, but the authoritative records live under `release/`. |
| Drift discipline | Keep any flat-vs-domain schema-home variants visible until ADR/steward resolution. |

---

## What belongs here

- This README.
- Soil JSON Schema files under the accepted `schemas/contracts/v1/domains/soil/` lane.
- Schema-family and child-lane README files.
- Schema index notes.
- Migration notes for Soil schema placement.
- Drift notes about duplicate, stale, or mirrored Soil schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, source registry records, policy references, release references, correction references, rollback references, and tests.

---

## What does not belong here

- Contract prose or semantic definitions.
- Policy rules, sensitivity rules, or allow/deny logic.
- Validator implementation code.
- Runtime code.
- Packages or pipeline implementation.
- Lifecycle data payloads.
- Source registry records or SourceDescriptor instances.
- Emitted receipt instances.
- Proof outputs or EvidenceBundles as data.
- Catalog records.
- Release records, release manifests, or release decisions as records.
- Public tiles, map/UI behavior, dashboards, screenshots, or generated summaries.
- Agriculture, Hydrology, Hazards, Geology, Habitat, Flora, Fauna, Archaeology, People/DNA/Land, or Spatial Foundation truth.
- Cross-domain schemas that belong under a lowest-common responsibility root.
- Claims that a schema is complete without fixtures, validators, registry records, policy checks, and steward review support.

---

## Support-type separation

Soil schemas must preserve the difference between evidence and derivative carriers.

| Support type | Examples | Schema warning |
|---|---|---|
| `authoritative_static_soil` | SSURGO/SDA map units, components, horizons, properties. | Preserve MUKEY/COKEY/CHKEY lineage, source version, query hash, and geometry/support caveats. |
| `gridded_derivative_soil` | gSSURGO/gNATSGO, raster/COG layers, PMTiles/GeoParquet derivations. | Must cite derivation and resolution; cannot replace static survey provenance. |
| `station_soil_moisture` | Kansas Mesonet or other station readings. | Preserve station metadata, UTC timestamp, source timezone, depths, units, and QC flags. |
| `reference_station_soil_climate` | SCAN/USCRN station subsets. | Keep cadence and QC distinct from Mesonet and satellite products. |
| `satellite_soil_moisture_grid` | SMAP-like grid estimates. | Pixel/grid support and retrieval latency must remain visible; cannot masquerade as station reading. |
| `profile_soil_evidence` | Pedon/profile/horizon evidence. | Do not invent unsupported chemistry, physics, depth, or horizon detail. |
| `soil_interpretation` | Hydrologic group, hydric, drainage, prime farmland, LCC, suitability, erosion-risk interpretations. | Separate source interpretation from KFM-derived summary; method and aggregation must be visible. |
| `governed_change_evidence` | SoilDiffReport, PromotionCandidate, CorrectionReceipt. | Promote only on meaningful content/source/schema/validator/policy change, not retrieval timestamp alone. |

---

## Schema status values

| Status | Meaning |
|---|---|
| `STUB` | Schema exists but is not field-complete. |
| `PROPOSED` | Schema is a proposed or scaffolded shape. |
| `DRAFT_SCHEMA` | Schema has meaningful fields but still needs review and test support. |
| `ACTIVE_SCHEMA` | Schema has accepted contract pairing, fixtures, validator support, registry record, review status, and CI support. |
| `PROFILE` | Schema profiles a shared source, evidence, release, runtime, or common schema without creating duplicate authority. |
| `MIRROR` | Schema mirrors another accepted schema location while a migration is active. |
| `PATH_CONFLICT` | Placement is blocked by unresolved schema-home or flat-vs-domain drift. |
| `TRANSITIONAL` | Schema is awaiting migration to the accepted home. |
| `DEPRECATED` | Schema should no longer receive new producers or consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, review, or CI support has not been verified. |

---

## Review checklist

- [ ] Schema has a stable `$id`.
- [ ] Schema uses JSON Schema draft 2020-12 unless an ADR says otherwise.
- [ ] Paired semantic contract is linked or marked **NEEDS VERIFICATION**.
- [ ] Source-role semantics are explicit.
- [ ] Support type is explicit where material.
- [ ] Temporal fields preserve valid/source/observed/retrieval/release/correction distinctions where material.
- [ ] Units, depth, method, CRS, geometry support, and scale are explicit where material.
- [ ] Evidence references point to evidence surfaces without embedding proof instances in this schema lane.
- [ ] Policy and release fields reference decisions without making this schema lane the decision store.
- [ ] Valid fixtures are linked or marked **NEEDS VERIFICATION**.
- [ ] Invalid fixtures are linked or marked **NEEDS VERIFICATION**.
- [ ] Validator path is linked or marked **NEEDS VERIFICATION**.
- [ ] CI/schema-test support is linked or marked **NEEDS VERIFICATION**.
- [ ] Adjacent-domain boundaries are preserved.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

---

## Validation

Recommended validation sequence for this lane:

```bash
# Inspect schema files and path drift.
find schemas/contracts/v1/domains/soil -maxdepth 2 -type f | sort
find schemas/contracts/v1 -maxdepth 4 -type f | grep -Ei 'soil|ssurgo|gssurgo|sda|mukey|cokey|chkey|moisture|pedon|horizon' | sort

# Validate JSON syntax.
python -m json.tool schemas/contracts/v1/domains/soil/soil_map_unit.schema.json >/dev/null
python -m json.tool schemas/contracts/v1/domains/soil/soil_moisture_reading.schema.json >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/domains/soil tests/contract tests/schemas || true
```

Replace `|| true` with fail-closed CI behavior once the repository validator set and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/domains/soil/README.md`.

Rollback for schema files must be more careful:

1. Revert the schema file change.
2. Revert or update paired fixtures.
3. Revert or update validators and tests.
4. Revert or update schema registry entries.
5. Revert or update any producer/consumer code.
6. If a schema entered a release candidate, update the release candidate, promotion decision, correction notice, or rollback card as required.

No schema rollback should silently leave stale producers, validators, public API responses, MapLibre layer descriptors, Evidence Drawer payloads, or Focus Mode fixtures pointing at a withdrawn shape.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should all Soil domain schemas remain under `schemas/contracts/v1/domains/soil/`, or should any flat atlas-era path be retained as a mirror? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + docs steward |
| Which surfaced schemas are intended as profiles of shared core schemas rather than separate domain authorities? | **NEEDS VERIFICATION** | Schema steward + contract steward |
| Which schema scaffolds are field-complete enough to advance from `PROPOSED` / `STUB` to `DRAFT_SCHEMA`? | **NEEDS VERIFICATION** | Soil domain steward + validation steward |
| Where is the authoritative schema registry entry for each Soil schema? | **NEEDS VERIFICATION** | Schema steward |
| Which fixtures prove valid and invalid cases for MUKEY/COKEY/CHKEY lineage, horizon depth sanity, soil-moisture units/time/QC, support-type separation, and public-safe layer behavior? | **NEEDS VERIFICATION** | Validation steward |
| Which release and rollback fixtures bind Soil schemas to release behavior? | **NEEDS VERIFICATION** | Release steward |
| Which public API and Evidence Drawer payloads currently consume these schemas? | **NEEDS VERIFICATION** | API/UI steward |

---

## Maintainer notes

- Keep this README as an index and boundary document, not as a substitute for schema review.
- Prefer small schema changes with paired fixtures and validators over broad field additions.
- Preserve the KFM lifecycle: `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`.
- Preserve the public trust path: public clients use governed APIs, released artifacts, catalog records, tile services, and EvidenceBundle resolution; they do not read RAW, WORK, QUARANTINE, unpublished candidates, internal stores, or model output directly.
- Preserve cite-or-abstain: a schema can enable a claim shape, but only evidence, policy, review, release, and correction state can support public truth.
