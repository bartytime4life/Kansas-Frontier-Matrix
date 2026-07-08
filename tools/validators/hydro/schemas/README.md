<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-hydro-schemas-readme
title: tools/validators/hydro/schemas README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hydrology-steward-plus-schema-steward-plus-tooling-qa-owner-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; validator-schema-routing; hydrology; hydro-alias; not-schema-authority; not-flood-warning; non-authoritative
owning_root: tools/
responsibility: validator-local schema routing README for the scaffolded hydro validator lane; documents how Hydrology validators should discover, reference, and report schema bindings while deferring Hydrology machine shape, contracts, policy, evidence, receipts, proofs, lifecycle data, fixtures, tests, and release decisions to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../fixtures/README.md
  - ../policy/README.md
  - ../../README.md
  - ../../_common/README.md
  - ../../domains/hydrology/README.md
  - ../../atmosphere_hydrology/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../hazards/README.md
  - ../../domains/hazards/README.md
  - ../../../../schemas/contracts/v1/domains/hydrology/
  - ../../../../schemas/contracts/v1/joins/hydrology_soil/README.md
  - ../../../../schemas/contracts/v1/joins/hydrology_hazards/README.md
  - ../../../../schemas/contracts/v1/joins/hydrology_agriculture/README.md
  - ../../../../schemas/contracts/v1/joins/hydrology_settlements/README.md
  - ../../../../schemas/contracts/v1/cross/atmosphere_hydrology/README.md
  - ../../../../schemas/contracts/v1/domains/agriculture/hydrology-ext/README.md
  - ../../../../docs/domains/hydrology/README.md
  - ../../../../docs/domains/hydrology/ARCHITECTURE.md
  - ../../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../../docs/domains/hydrology/source-role-matrix.md
  - ../../../../contracts/domains/hydrology/
  - ../../../../policy/domains/hydrology/
  - ../../../../policy/release/hydrology/
  - ../../../../data/registry/sources/hydrology/
  - ../../../../data/proofs/hydrology/README.md
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This README replaces an empty file at tools/validators/hydro/schemas/README.md. It does not confirm schema files, executable validator code, tests, or CI wiring."
  - "Directory Rules identify schemas/ as the root that defines machine shape. This tools-local schemas folder is therefore a routing/index surface, not a schema authority."
  - "tools/validators/hydro/README.md is a scaffold and explicitly says machine-checkable shape belongs in schemas/ unless an accepted ADR says otherwise."
  - "tools/validators/domains/hydrology/README.md remains the richer per-domain Hydrology validator index and routes Hydrology schemas to schemas/contracts/v1/domains/hydrology/ or accepted ADR-selected homes."
  - "No JSON Schema, contract meaning, policy rule, source data, lifecycle data, evidence record, receipt, release approval, flood-warning authority, emergency instruction, or regulatory determination belongs here."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/hydro/schemas

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-hydro--validator--schema--routing-informational)
![schema](https://img.shields.io/badge/schema-authority--elsewhere-lightgrey)
![boundary](https://img.shields.io/badge/not--flood--warning-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/hydro/schemas/` documents schema lookup and reporting expectations for the scaffolded `hydro` validator lane; actual Hydrology machine shape belongs in `schemas/`, not inside a validator folder.

---

## Purpose

`tools/validators/hydro/schemas/` exists to keep Hydrology validator schema dependencies inspectable without turning `tools/validators/` into a schema root.

The durable KFM question for this README is:

> How should Hydrology validators discover, reference, pin, and report schema inputs for watershed, HUC, reach, gauge, well, observation, hydrograph, NFHL/regulatory context, upstream trace, water-use, drought, irrigation, cross-domain joins, evidence references, policy references, release references, correction paths, rollback targets, and public-surface checks without defining machine shape locally?

The answer should be routing guidance for validator maintainers. This folder should not define Hydrology schemas, object meaning, policy, emergency-warning behavior, regulatory determinations, EvidenceBundles, receipts, release decisions, public map outputs, or AI-facing truth.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/hydro/schemas/README.md` | **CONFIRMED README** | This README replaces the previous empty file. |
| `tools/validators/hydro/README.md` | **CONFIRMED scaffold** | Parent `hydro` path is a proposed scaffold and says machine-checkable shape belongs in `schemas/` unless an accepted ADR says otherwise. |
| `tools/validators/domains/hydrology/README.md` | **CONFIRMED README / executable NEEDS VERIFICATION** | Richer per-domain Hydrology validator index; current implementation behavior remains unverified. |
| Canonical Hydrology schema roots | **PROPOSED / NEEDS VERIFICATION** | Candidate homes include `schemas/contracts/v1/domains/hydrology/` and related join/cross schema roots; existence, contents, and accepted schema set need verification before use. |
| Local schema files in this folder | **NOT CLAIMED / DISCOURAGED** | No JSON Schema, YAML schema, OpenAPI fragment, enum, DTO, contract, or validation schema is claimed here. |
| Executables, schema bindings, test harnesses, policy bundles, receipt emission, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Placement decision

Directory Rules split responsibilities by authority:

| Responsibility | Preferred root |
|---|---|
| Repo-wide validator, generator, builder, checker | `tools/` |
| Machine shape | `schemas/` |
| Object meaning | `contracts/` |
| Allow, deny, restrict, or abstain rules | `policy/` |
| Tests that prove a rule is enforceable | `tests/` |
| Golden, valid, or invalid sample data for tests | `fixtures/` |
| Lifecycle data | `data/` |
| Release decision, manifest, rollback, correction | `release/` |

Therefore this path should normally be a **schema routing guide**, not a schema bundle store. Validators may read, pin, or report schema identifiers and digests, but they must not become the source of machine-shape truth.

[Back to top](#top)

---

## Schema routing relationship

| Concern | Preferred home | Validator responsibility |
|---|---|---|
| Hydrology domain object schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema home | Validate against accepted schema ids and report the schema id/version/digest used. |
| Hydrology domain meaning | `contracts/domains/hydrology/` and `docs/domains/hydrology/` | Do not define meaning locally; validator checks conformance only. |
| Hydrology × Soil joins | `schemas/contracts/v1/joins/hydrology_soil/` | Ensure join payloads preserve ownership, source role, evidence, policy, and release posture. |
| Hydrology × Hazards joins | `schemas/contracts/v1/joins/hydrology_hazards/` | Ensure flood/hazard context does not collapse into warning authority or emergency instruction. |
| Hydrology × Agriculture joins | `schemas/contracts/v1/joins/hydrology_agriculture/` and related accepted homes | Ensure irrigation/water-use context preserves neighboring-domain authority. |
| Hydrology × Settlements joins | `schemas/contracts/v1/joins/hydrology_settlements/` | Ensure infrastructure/private/public-surface policy is preserved. |
| Atmosphere × Hydrology cross schemas | `schemas/contracts/v1/cross/atmosphere_hydrology/` | Ensure precipitation, drought, runoff, weather, and atmosphere context stays source-role aware. |
| Agriculture Hydrology extension schemas | `schemas/contracts/v1/domains/agriculture/hydrology-ext/` | Ensure Agriculture extension does not absorb Hydrology truth. |
| Policy references | `policy/domains/hydrology/`, `policy/release/hydrology/` | Validate schema fields carry policy references when required; do not decide policy. |
| Evidence and receipt references | `data/proofs/`, `data/receipts/` | Verify reference shape only where schemas require it; do not create proof authority here. |

[Back to top](#top)

---

## Schema input classes

Future validators may need to resolve schema inputs such as:

| Schema input class | Validator question | Failure if absent |
|---|---|---|
| `domain_schema_id` | Which Hydrology domain schema was used? | `SCHEMA_ID_MISSING` |
| `domain_schema_digest` | Can the exact schema version be pinned? | `SCHEMA_DIGEST_MISSING` |
| `object_family_schema` | Does the object family match the declared Hydrology type? | `OBJECT_FAMILY_SCHEMA_MISSING` |
| `identity_schema` | Are HUC, reach, COMID, gauge, well, and upstream/downstream identities shaped correctly? | `IDENTITY_SCHEMA_MISSING` |
| `observation_schema` | Are units, timestamp fields, observed/model/regulatory posture, and source role shaped correctly? | `OBSERVATION_SCHEMA_MISSING` |
| `join_schema` | Does a cross-domain join use an accepted join/cross schema? | `JOIN_SCHEMA_MISSING` |
| `policy_ref_schema` | Does the candidate carry policy/review/release reference fields where required? | `POLICY_REF_SCHEMA_MISSING` |
| `evidence_ref_schema` | Does the candidate carry EvidenceRef/EvidenceBundle reference fields where required? | `EVIDENCE_REF_SCHEMA_MISSING` |
| `public_surface_schema` | Does the public artifact shape prevent overclaim, stale context, emergency instruction, and ungoverned UI leakage? | `PUBLIC_SURFACE_SCHEMA_MISSING` |

[Back to top](#top)

---

## Minimal schema binding manifest

Future validator runs may record schema binding metadata in a report or receipt. This sketch is **PROPOSED**, not a confirmed schema.

```yaml
validator_lane: tools/validators/hydro
schema_binding_id: hydro-schema-binding-example-001
domain_schema_home: schemas/contracts/v1/domains/hydrology
join_schema_home: schemas/contracts/v1/joins/hydrology_hazards
schema_id: NEEDS_VERIFICATION
schema_version: NEEDS_VERIFICATION
schema_digest: NEEDS_VERIFICATION
contract_home: contracts/domains/hydrology
policy_home: policy/domains/hydrology
release_policy_home: policy/release/hydrology
source_registry_home: data/registry/sources/hydrology
expected_schema_outcome: SCHEMA_BINDING_PRESENT
validator_may_define_schema: false
validator_may_define_contract_meaning: false
notes: Metadata sketch only; not a schema, contract, EvidenceBundle, receipt, ReleaseManifest, or official hydrology decision.
```

Do not treat this manifest sketch as a schema until a schema file, validator registry entry, report destination, and test harness are verified.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| This schema README and validator schema-routing guidance | `tools/validators/hydro/schemas/` |
| Hydro validator scaffold | `tools/validators/hydro/` |
| Per-domain Hydrology validator index | `tools/validators/domains/hydrology/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Hydrology schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema homes |
| Hydrology join/cross schemas | `schemas/contracts/v1/joins/`, `schemas/contracts/v1/cross/`, or accepted schema homes |
| Hydrology domain meaning | `docs/domains/hydrology/`, `contracts/domains/hydrology/` |
| Hydrology policy rules | `policy/domains/hydrology/`, `policy/release/hydrology/`, or accepted policy homes |
| Tests | `tests/validators/hydro/`, `tests/validators/domains/hydrology/`, `tests/domains/hydrology/`, or accepted test home |
| Fixtures | `fixtures/domains/hydrology/`, `fixtures/validators/hydrology/`, or accepted fixture home |
| Source descriptors | `data/registry/sources/hydrology/` or accepted source registry home |
| Evidence/proof support | `data/proofs/hydrology/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Lifecycle data | `data/raw/hydrology/`, `data/work/hydrology/`, `data/quarantine/hydrology/`, `data/processed/hydrology/`, `data/catalog/...`, `data/published/...` |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator schema binding metadata may be documented here if it points to accepted `schemas/` roots and does not become schema authority.
- **NEEDS VERIFICATION:** whether schema homes, schema ids, schema versions, digests, registry entries, fixtures, report destinations, receipt emission, runtime behavior, and CI wiring exist.
- **DENY:** using this folder as Hydrology doctrine, schema authority, contract authority, policy authority, emergency-warning authority, flood-warning authority, regulatory-determination authority, source registry, lifecycle data store, proof store, receipt store, release record store, or public map product surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/hydro/schemas/` include:

- this README;
- notes on how a Hydrology validator should locate accepted schema ids, schema versions, schema homes, and schema digests;
- schema binding metadata examples that are clearly marked **PROPOSED**;
- expected schema-related validator outcomes;
- links to canonical `schemas/`, `contracts/`, `policy/`, `release/`, `data/proofs/`, `data/receipts/`, `tests/`, and `fixtures/` homes;
- reminders that validators check schema conformance but do not define object meaning or approve release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/hydro/schemas/` | Correct home |
|---|---|
| Hydrology JSON Schema, YAML schema, enum, DTO, OpenAPI fragment, or schema bundle | `schemas/contracts/v1/domains/hydrology/` or accepted schema home |
| Hydrology join/cross schemas | `schemas/contracts/v1/joins/`, `schemas/contracts/v1/cross/`, or accepted schema home |
| Hydrology contracts or doctrine | `contracts/domains/hydrology/`, `docs/domains/hydrology/` |
| Hydrology policy rules | `policy/domains/hydrology/`, `policy/release/hydrology/` |
| Source descriptors | `data/registry/sources/hydrology/` |
| EvidenceBundles, proof packs, receipts, validation reports, ModelRunReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, rollback cards, correction notices | `release/` |
| Tests and fixtures | `tests/`, `fixtures/` |
| Real source extracts or lifecycle data | governed `data/` lifecycle roots |
| Public API, UI, map, tile, search, graph, Focus Mode, export, screenshot, or AI runtime output | governed application/runtime roots |
| Flood warnings, evacuation advice, dam-safety instructions, navigation safety advice, engineering decisions, or regulatory determinations | official agencies and governed source systems, not KFM validator docs |

[Back to top](#top)

---

## Schema safety rules

Hydrology schema-routing notes must:

- identify the schema home rather than copy schema definitions locally;
- preserve object-family separation for watersheds, HUC units, reaches, gauges, wells, observations, hydrographs, NFHL zones, upstream traces, water-use links, drought links, and irrigation links;
- preserve observed/model/regulatory/aggregate/public-map source-role separation;
- preserve not-flood-warning and not-emergency-instruction boundaries;
- preserve most-restrictive policy propagation across cross-domain joins;
- require schema id, version, and digest when validators claim a schema was applied;
- require explicit failure when schema binding is missing, ambiguous, stale, superseded, or unreviewed;
- require release, correction, and rollback references before public surfaces are treated as safe;
- avoid embedding hidden thresholds, exact sensitive locations, real operational instructions, current warning text, or machine-shape rules in validator docs;
- never convert validator pass into publication approval.

[Back to top](#top)

---

## Standard schema outcomes

| Outcome | Meaning |
|---|---|
| `SCHEMA_BINDING_PRESENT` | Validator found an accepted schema binding reference. |
| `SCHEMA_ID_MISSING` | Required schema id is absent. |
| `SCHEMA_VERSION_MISSING` | Required schema version is absent. |
| `SCHEMA_DIGEST_MISSING` | Required schema digest, checksum, or immutable reference is absent. |
| `SCHEMA_HOME_MISSING` | Referenced schema home is absent or unresolved. |
| `SCHEMA_BINDING_STALE` | Referenced schema is superseded, expired, or not accepted for the candidate surface. |
| `SCHEMA_CONFORMANCE_FAIL` | Candidate fails the accepted schema. |
| `OBJECT_FAMILY_SCHEMA_MISSING` | Candidate cannot prove declared Hydrology object-family shape. |
| `IDENTITY_SCHEMA_MISSING` | Candidate lacks accepted HUC/reach/COMID/gauge/well identity shape. |
| `OBSERVATION_SCHEMA_MISSING` | Candidate lacks accepted observation, unit, timestamp, or source-role shape. |
| `JOIN_SCHEMA_MISSING` | Candidate lacks accepted join/cross-domain schema binding. |
| `POLICY_REF_SCHEMA_MISSING` | Candidate lacks accepted policy/review/release reference fields. |
| `EVIDENCE_REF_SCHEMA_MISSING` | Candidate lacks accepted EvidenceRef/EvidenceBundle reference shape. |
| `PUBLIC_SURFACE_SCHEMA_MISSING` | Candidate lacks accepted public-surface guard fields. |
| `VALIDATOR_SCHEMA_SYSTEM_ERROR` | Validator could not resolve schema because of malformed input, missing dependency, missing registry entry, or unexpected runtime error. |

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty file at `tools/validators/hydro/schemas/README.md`.
- [x] It marks this path as validator-local schema-routing guidance, not schema authority.
- [x] It points Hydrology machine shape to `schemas/contracts/v1/domains/hydrology/` or accepted schema homes.
- [x] It links Hydrology join/cross schemas where relevant.
- [x] It links the scaffolded `hydro` lane to the richer per-domain `hydrology` validator index.
- [x] It preserves not-flood-warning, source-role, identity, freshness, evidence, policy, release, correction, rollback, and public-surface denial boundaries.
- [x] It marks executable behavior, schema files, schema digests, tests, policy bundles, fixtures, receipt emission, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Accepted schema homes, ids, versions, and digests are verified.
- [ ] Schema binding metadata shape is accepted or replaced by a real schema.
- [ ] Tests exercise present, missing, stale, superseded, malformed, and conflicting schema bindings.
- [ ] CI invokes the relevant Hydrology schema validation checks in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty README with Hydrology validator schema-routing documentation. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
