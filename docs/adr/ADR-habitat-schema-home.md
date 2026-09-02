<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/habitat-schema-home
title: Habitat Schema Home
adr_id: ADR-habitat-schema-home
type: architecture-decision-record
version: v1.0
status: proposed
owners:
  - <habitat-domain-steward>
  - <schema-steward>
  - <contract-steward>
reviewers:
  - <architecture-steward>
  - <validation-steward>
  - <docs-steward>
created: 2026-07-24
updated: 2026-07-24
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
current_path: docs/adr/ADR-habitat-schema-home.md
related:
  - docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - docs/adr/ADR-0002-contracts-vs-schemas-split.md
  - docs/doctrine/directory-rules.md
  - schemas/contracts/v1/README.md
  - schemas/contracts/v1/domains/README.md
  - schemas/contracts/v1/domains/habitat/README.md
  - contracts/domains/habitat/
  - docs/domains/habitat/ARCHITECTURE.md
tags: [kfm, adr, habitat, schema-home, contracts, schemas, governance, migration]
notes:
  - "This same-path update replaces a generated scaffold with an evidence-bounded domain-specific decision record."
  - "The configured Habitat schema lane is verified, but ADR-0001 remains proposed and the Habitat lane remains mixed-maturity."
  - "This ADR does not promote any schema to ACTIVE_SCHEMA, accept ADR-0001, or create migration authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR — Habitat Schema Home

> **Proposed decision.** Habitat-specific machine-checkable schemas should live under `schemas/contracts/v1/domains/habitat/`, while semantic meaning remains under `contracts/domains/habitat/`. This path is the configured Habitat schema lane, but it is not yet a fully accepted or fully mature authority surface.

![status](https://img.shields.io/badge/status-PROPOSED-yellow?style=flat-square)
![domain](https://img.shields.io/badge/domain-habitat-2ea44f?style=flat-square)
![schema-home](https://img.shields.io/badge/schema%20home-schemas%2Fcontracts%2Fv1%2Fdomains%2Fhabitat-blue?style=flat-square)
![maturity](https://img.shields.io/badge/maturity-mixed-orange?style=flat-square)
![publication](https://img.shields.io/badge/publication-none-lightgrey?style=flat-square)

> [!IMPORTANT]
> **Configured placement is not accepted authority.** Repository evidence confirms the Habitat schema lane exists and is documented as the intended domain-specific machine-shape location. ADR-0001, however, still has `proposed` status, and the Habitat lane contains scaffolds and unresolved coverage. This ADR records the domain-specific placement decision without overstating acceptance, completeness, validation, or release readiness.

## Contents

1. [Status and scope](#1-status-and-scope)
2. [Context](#2-context)
3. [Decision](#3-decision)
4. [Responsibility boundaries](#4-responsibility-boundaries)
5. [Current repository evidence](#5-current-repository-evidence)
6. [Schema-family routing](#6-schema-family-routing)
7. [No-parallel-authority rule](#7-no-parallel-authority-rule)
8. [Consequences](#8-consequences)
9. [Acceptance criteria](#9-acceptance-criteria)
10. [Validation plan](#10-validation-plan)
11. [Migration and rollback](#11-migration-and-rollback)
12. [Open questions](#12-open-questions)
13. [Evidence basis](#13-evidence-basis)

---

## 1. Status and scope

| Field | Current value |
|---|---|
| ADR status | `proposed` |
| Decision scope | Habitat-domain schema placement |
| Configured Habitat lane | `schemas/contracts/v1/domains/habitat/` |
| Semantic contract lane | `contracts/domains/habitat/` |
| Machine-shape authority posture | **PROPOSED / mixed maturity** |
| Publication effect | None |
| Supersedes | The prior scaffold at this same path |

This ADR is subordinate to repo-wide schema-home governance. It cannot independently accept ADR-0001, redefine the canonical schema root, or create a competing schema authority.

[Back to top](#top)

---

## 2. Context

KFM separates responsibilities that must remain linked but must not collapse:

```text
contracts/  -> semantic meaning and claim limits
schemas/    -> machine-checkable shape
policy/     -> admissibility and obligations
fixtures/ + tests/ + validators/ -> executable proof
release/    -> promotion, release, correction, rollback
```

Habitat needs machine shapes for domain objects such as land-cover observations, habitat patches, ecoregion context, suitability models, corridors, uncertainty, and validation reports. Without a single governed home, the repository risks:

- duplicate schemas for the same Habitat object family;
- divergence between flat and domain-segmented paths;
- contracts containing machine shape;
- schemas being mistaken for policy or publication approval;
- validators and producers targeting different files;
- migrations that cannot be audited or rolled back.

The repository currently uses `schemas/contracts/v1/domains/habitat/` as the Habitat schema index. That implementation signal is real, but the lane remains draft and mixed-maturity, and the repo-wide schema-home ADR remains proposed.

[Back to top](#top)

---

## 3. Decision

KFM will apply the following proposed decision for Habitat schemas:

1. **Habitat-specific machine-checkable schemas belong under `schemas/contracts/v1/domains/habitat/`.**
2. **Semantic meaning belongs under `contracts/domains/habitat/`.** Markdown contracts define object meaning, invariants, claim limits, and relationships; they do not become machine-schema authority.
3. **Reusable cross-domain shapes belong at the lowest verified shared responsibility root.** Habitat must reference shared evidence, source, geometry, receipt, policy-envelope, or release-support schemas rather than copying them into the Habitat lane.
4. **Policy does not belong in the schema lane.** Schemas may define policy-input or decision-envelope shape, but allow, deny, restrict, abstain, sensitivity, and release logic remain under `policy/` and governed release surfaces.
5. **Fixtures, validators, and tests do not belong in the schema lane.** They remain in their established responsibility roots and link back to the schema they exercise.
6. **Lifecycle records do not belong in the schema lane.** Source descriptors, EvidenceBundles, receipts, catalog records, release records, corrections, rollback cards, and published artifacts remain under their governed data and release roots.
7. **No alternate Habitat schema path may evolve as parallel authority.** Any existing overlap must be classified as canonical candidate, profile, mirror, transitional, deprecated, or unresolved through an ADR-backed migration process.
8. **A schema file does not become active merely by existing or validating as JSON.** Promotion requires contract pairing, stable identity, fixtures, validator coverage, CI evidence, registry linkage, steward review, and any required policy/release integration.

[Back to top](#top)

---

## 4. Responsibility boundaries

| Responsibility | Governing root | Habitat application |
|---|---|---|
| Architecture decision | `docs/adr/` | This ADR records placement, consequences, acceptance, migration, and rollback. |
| Domain explanation | `docs/domains/habitat/` | Human-facing Habitat architecture, source families, publication posture, and lane guidance. |
| Semantic meaning | `contracts/domains/habitat/` | Habitat object meaning and invariants. |
| Machine shape | `schemas/contracts/v1/domains/habitat/` | Habitat-specific JSON Schema and schema-family indexes. |
| Shared machine shape | Verified shared family under `schemas/contracts/v1/` | Common evidence, source, geometry, receipt, runtime, or policy-envelope shapes. |
| Policy | `policy/domains/habitat/` or verified shared policy root | Admissibility, sensitivity, source-role, and release decisions. |
| Fixtures | `fixtures/domains/habitat/` | Valid, invalid, boundary, public-safe, and regression examples. |
| Tests | `tests/domains/habitat/` and verified schema-test roots | Behavioral and conformance proof. |
| Validators | `tools/validators/`, packages, or another verified implementation root | Executable checks. |
| Lifecycle data | `data/` | Source registry, work/quarantine, processed, catalog, receipts, proofs, and published artifacts. |
| Release authority | `release/` | Promotion decisions, manifests, approvals, corrections, and rollback. |

Directory Rules basis: file placement follows responsibility, not topic. This ADR therefore preserves Habitat as a segment under the existing `schemas/`, `contracts/`, `policy/`, `fixtures/`, `tests/`, `data/`, and `release/` authority roots rather than creating a new root-level Habitat schema home.

[Back to top](#top)

---

## 5. Current repository evidence

The following findings are **CONFIRMED in this session** unless marked otherwise:

| Surface | Verified state | Meaning |
|---|---|---|
| `docs/adr/ADR-habitat-schema-home.md` | Existed as a generated `PROPOSED` scaffold. | A domain-reviewed decision was missing. |
| `docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md` | Exists; status remains `proposed`. | Repo-wide schema-home acceptance is not complete. |
| `schemas/contracts/v1/README.md` | Describes the v1 machine-shape index as mixed maturity. | The root is configured but not uniformly mature. |
| `schemas/contracts/v1/domains/README.md` | Routes domain schemas to `schemas/contracts/v1/domains/<domain>/`. | Domain-segmented placement is the current proposed route. |
| `schemas/contracts/v1/domains/habitat/README.md` | Exists and documents the Habitat lane. | The configured Habitat schema lane is real. |
| Habitat lane maturity | README records draft/proposed state and incomplete inventory. | Lane existence does not prove completeness. |
| Confirmed concrete schema | `land_cover/observation.schema.json` is recorded as a proposed scaffold. | At least one Habitat schema file exists, but active enforcement is not established. |
| Child lanes | `land_cover/` and `ecoregions/` indexes are documented. | The lane already has substructure, but coverage remains partial. |
| Schema registry and full validator coverage | Not verified as complete. | Promotion remains blocked. |

> [!CAUTION]
> This ADR does not convert `schemas/contracts/v1/domains/habitat/` from proposed/configured into accepted canonical authority by declaration. Acceptance requires the gates in §9 and consistency with ADR-0001.

[Back to top](#top)

---

## 6. Schema-family routing

The Habitat lane should route schemas by responsibility and reuse before specialization.

| Object or concern | Expected routing | Status |
|---|---|---|
| Habitat-specific land-cover observation | `schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json` | **CONFIRMED path; PROPOSED scaffold** |
| Habitat land-cover class scheme | Habitat `land_cover/` child lane if truly Habitat-specific; otherwise shared classification family | **NEEDS VERIFICATION** |
| Habitat crosswalk | Habitat child lane only for Habitat-specific crosswalk semantics; generic crosswalk shape should be shared | **NEEDS VERIFICATION** |
| Ecoregion object or snapshot | Habitat `ecoregions/` only if ownership is Habitat-specific and not a broader spatial-foundation concern | **NEEDS VERIFICATION** |
| Habitat patch | Habitat root or a justified child family | **NEEDS VERIFICATION** |
| Suitability model | Habitat lane may profile shared model-run, evidence, uncertainty, and receipt schemas | **NEEDS VERIFICATION** |
| Connectivity corridor | Habitat lane if it expresses Habitat-owned corridor shape; shared graph primitives should remain shared | **NEEDS VERIFICATION** |
| EvidenceRef / EvidenceBundle | Shared evidence schema family | Must not be copied into Habitat. |
| SourceDescriptor | Shared source schema family | Must not be copied into Habitat. |
| Geometry primitives | Verified shared spatial/common schema family | Habitat should reference, not fork. |
| Release or policy decision envelope | Shared release/policy schema family | Shape only; records and decisions remain outside schemas. |

A child folder is justified by a stable object-family boundary, not by presentation convenience. A new child lane must document ownership, paired contracts, validators, fixtures, and the absence of parallel authority.

[Back to top](#top)

---

## 7. No-parallel-authority rule

The following are prohibited unless governed by an accepted ADR and reversible migration plan:

- adding the same Habitat object schema under both `schemas/contracts/v1/domains/habitat/` and a flat `schemas/contracts/v1/habitat/` lane;
- maintaining independently editable machine schemas under both `contracts/domains/habitat/` and `schemas/`;
- copying shared EvidenceRef, SourceDescriptor, receipt, geometry, or decision-envelope schemas into the Habitat lane;
- treating README candidate inventories as proof that schema files exist;
- promoting a compatibility mirror without identifying its canonical source and deprecation path;
- using schema validity as evidence of policy approval, release approval, public safety, or publication.

Where overlap already exists, the repository must classify each path using finite states such as:

`ACTIVE_SCHEMA | PROFILE | MIRROR | TRANSITIONAL | DEPRECATED | STUB | NEEDS_VERIFICATION`

The classification must identify the authority source, migration owner, consumer impact, validation plan, rollback target, and retirement condition.

[Back to top](#top)

---

## 8. Consequences

### Positive

- Habitat schema discovery becomes predictable.
- Contracts and schemas remain one-to-one in responsibility without being co-located as parallel machine authority.
- Validators, fixtures, generators, and reviewers can converge on one domain lane.
- Shared schemas remain reusable rather than being forked by the Habitat domain.
- Migration and deprecation can be audited and reversed.
- Schema presence remains visibly separate from evidence, policy, review, release, and publication authority.

### Costs and constraints

- Existing flat, duplicate, or contract-hosted machine schemas cannot be silently adopted or deleted.
- Some candidate Habitat schemas may need to move to shared families after ownership review.
- Every promoted schema needs paired documentation, fixtures, validators, registry linkage, and CI support.
- ADR-0001 acceptance and schema-registry maturity remain dependencies for full closure.

### Risks

| Risk | Mitigation |
|---|---|
| Domain lane becomes a catch-all | Require lowest-common-responsibility review and shared-schema reuse. |
| README inventory outruns implementation | Label candidates and verify actual files before claims. |
| Duplicate schema authority persists | Register drift and use governed migration/deprecation records. |
| Schema validity is mistaken for publication approval | Preserve explicit policy, release, evidence, and review boundaries. |
| Breaking path changes surprise consumers | Inventory consumers and provide aliases/mirrors only through a time-bounded migration plan. |

[Back to top](#top)

---

## 9. Acceptance criteria

This ADR should not advance to `accepted` until all applicable conditions are met:

- [ ] ADR-0001 is accepted or this ADR explicitly records an approved exception.
- [ ] The Habitat schema lane is listed in the canonical ADR/schema indexes.
- [ ] A schema registry or equivalent machine register identifies Habitat schema authority and status.
- [ ] Existing Habitat schema paths outside the chosen lane are inventoried and classified.
- [ ] No unresolved duplicate authority exists for the same object family.
- [ ] Each promoted Habitat schema has a stable `$id` and declared JSON Schema dialect.
- [ ] Each promoted schema links to a paired semantic contract or approved shared profile.
- [ ] Valid and invalid fixtures exist.
- [ ] Validator coverage exists and fails closed for invalid fixtures.
- [ ] CI exercises the affected schemas and validators.
- [ ] Cross-domain references do not replace source-domain truth.
- [ ] Sensitive Habitat and species-linked fields have appropriate policy review.
- [ ] Migration, correction, and rollback paths are documented where consumers already exist.
- [ ] Habitat, schema, contract, validation, architecture, and docs stewards approve the decision.

[Back to top](#top)

---

## 10. Validation plan

A repository-backed validation pass should verify at minimum:

```bash
# Inventory the Habitat schema lane.
find schemas/contracts/v1/domains/habitat -type f | sort

# Confirm schema JSON parses.
find schemas/contracts/v1/domains/habitat -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Search for competing Habitat schema homes.
find schemas contracts -type f \
  | grep -Ei 'habitat|land[_-]?cover|ecoregion|suitability|corridor' \
  | sort

# Run repository schema and contract checks using verified paths.
python tools/validate_all.py
pytest tests/schemas tests/contracts tests/domains/habitat
```

Exact commands and test paths remain **NEEDS VERIFICATION** until run against a mounted checkout. CI results should be cited by run and commit; workflow configuration alone is not proof of a passing result.

Validation must cover:

- JSON syntax and schema meta-validation;
- unique and stable `$id` values;
- paired-contract links;
- valid/invalid fixture behavior;
- validator and CI wiring;
- duplicate path detection;
- reference resolution to shared schemas;
- backward compatibility for existing consumers;
- policy-sensitive field handling where Habitat joins to rare-species or protected-location data.

[Back to top](#top)

---

## 11. Migration and rollback

### Migration discipline

Any move into `schemas/contracts/v1/domains/habitat/` must:

1. identify the old and new paths;
2. identify the owning object family and authority source;
3. inventory producers, consumers, validators, fixtures, tests, documentation, registries, and generated artifacts;
4. classify the old path as mirror, transitional, deprecated, or removed;
5. preserve stable identity or document the breaking change;
6. update references atomically where practical;
7. provide validation evidence;
8. define a rollback target and sunset condition.

A migration is not complete when a file is copied. It is complete when authority, consumers, validation, deprecation, and rollback are all governed and auditable.

### Rollback

This documentation update is reversible by reverting its single commit. Future schema migrations must have their own rollback card or equivalent record. Rollback must restore a coherent authority chain rather than reintroducing two writable schema homes.

[Back to top](#top)

---

## 12. Open questions

| ID | Question | Status |
|---|---|---|
| HAB-SCHEMA-01 | When will ADR-0001 move from proposed to accepted, rejected, or superseded? | **UNKNOWN** |
| HAB-SCHEMA-02 | What machine registry is authoritative for schema path, `$id`, status, owner, and deprecation? | **NEEDS VERIFICATION** |
| HAB-SCHEMA-03 | Are any Habitat schemas duplicated outside `schemas/contracts/v1/domains/habitat/`? | **NEEDS VERIFICATION** |
| HAB-SCHEMA-04 | Which ecoregion schemas are Habitat-owned versus spatial-foundation or shared classification concerns? | **NEEDS VERIFICATION** |
| HAB-SCHEMA-05 | Which Habitat schemas have valid/invalid fixtures and validator coverage today? | **NEEDS VERIFICATION** |
| HAB-SCHEMA-06 | Are `SuitabilityModel.md` and `suitability_model.md` distinct semantic contracts, aliases, or naming drift? | **NEEDS VERIFICATION** |
| HAB-SCHEMA-07 | What namespace grammar governs Habitat schema `$id` values? | **NEEDS VERIFICATION** |
| HAB-SCHEMA-08 | Which existing consumers require compatibility aliases before any path migration? | **UNKNOWN** |

[Back to top](#top)

---

## 13. Evidence basis

This revision was grounded in the repository surfaces inspected during this session:

- `docs/adr/ADR-habitat-schema-home.md` — prior scaffold;
- `docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md` — repo-wide proposed schema-home decision and current implementation snapshot;
- `schemas/contracts/v1/README.md` — mixed-maturity v1 schema index;
- `schemas/contracts/v1/domains/README.md` — proposed domain-lane routing and path-conflict posture;
- `schemas/contracts/v1/domains/habitat/README.md` — configured Habitat lane, known child lanes, candidate inventory, and maturity limits;
- `docs/doctrine/directory-rules.md` — responsibility-root placement and no-parallel-authority doctrine.

No schema, contract, policy, fixture, validator, test, runtime, lifecycle record, release record, or published artifact was changed by this ADR update.

---

**Decision posture:** `PROPOSED`  
**Configured path:** `schemas/contracts/v1/domains/habitat/`  
**Implementation maturity:** mixed / incomplete  
**Publication authority:** none
