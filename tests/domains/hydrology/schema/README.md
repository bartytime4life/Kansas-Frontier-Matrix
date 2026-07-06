<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-hydrology-schema-readme
title: Hydrology Schema Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; schema-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; hydrology; schema; no-network; contract-schema-parity; evidence-bound; source-role-aware; release-gated; rollback-aware
tags: [kfm, tests, hydrology, schema, JSON-Schema, contract-schema-parity, schema-scaffold, ReachIdentity, HUCUnit, HydroFeature, GaugeSite, FlowObservation, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../../README.md
  - ../README.md
  - ../identity/README.md
  - ../policy/README.md
  - ../no_network/README.md
  - ../../../../schemas/contracts/v1/domains/hydrology/README.md
  - ../../../../schemas/contracts/v1/domains/hydrology/reach_identity.schema.json
  - ../../../../contracts/domains/hydrology/README.md
  - ../../../../contracts/domains/hydrology/reach_identity.md
  - ../../../../contracts/domains/hydrology/huc_unit.md
  - ../../../../contracts/domains/hydrology/hydro_feature.md
  - ../../../../contracts/domains/hydrology/gauge_site.md
  - ../../../../contracts/domains/hydrology/flow_observation.md
  - ../../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../../docs/domains/hydrology/OBJECT_FAMILIES.md
  - ../../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../../docs/domains/hydrology/CANONICAL_PATHS.md
  - ../../../../docs/domains/hydrology/DATA_LIFECYCLE.md
  - ../../../../fixtures/domains/hydrology/schema/
  - ../../../../policy/domains/hydrology/
  - ../../../../release/manifests/hydrology/
notes:
  - "This file replaces a blank placeholder at tests/domains/hydrology/schema/README.md."
  - "This is a test-lane README only. It does not define Hydrology doctrine, contracts, schemas, fixtures, source descriptors, lifecycle records, EvidenceBundles, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that Hydrology schema checks preserve the contract/schema split: contracts define human-readable meaning, schemas define machine-checkable shape, policy gates decide admissibility, fixtures prove examples, and release records decide publication."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, public tiles, and restricted records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology schema tests

> Deterministic, no-network test documentation for proving that Hydrology JSON Schemas stay paired with semantic contracts, remain honest about scaffold maturity, and do not become policy, release, evidence, or public-truth authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-2aa1c6">
  <img alt="Lane: schema" src="https://img.shields.io/badge/lane-schema-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: schema not policy" src="https://img.shields.io/badge/boundary-schema__not__policy-success">
</p>

**Path:** `tests/domains/hydrology/schema/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `hydrology`  
**Test lane:** `schema`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED `schemas/contracts/v1/domains/hydrology/` is the Hydrology schema lane and is not a home for contract prose, policy, validator code, lifecycle data, registry data, proof output, receipts, source descriptor instances, or release authority · CONFIRMED `reach_identity.schema.json` exists as a PROPOSED scaffold with empty properties and `additionalProperties: true` · CONFIRMED Hydrology contracts own human-readable meaning while schemas own machine shape · NEEDS VERIFICATION for executable schema tests, full schema inventory, strictness, fixture coverage, validator behavior, CI coverage, and pass rates.

---

## Purpose

`tests/domains/hydrology/schema/` is the intended home for Hydrology schema tests.

This lane should prove that Hydrology schema files are discoverable, valid JSON Schema documents, correctly paired with semantic contracts, honest about scaffold maturity, and compatible with local fixture examples where fixtures exist.

A passing test here should **not** mean that Hydrology claims are true, sources are admitted, policy gates passed, public layers are safe, or releases are approved. It should mean only that schema guardrails behaved as expected against bounded fixtures and local files.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Hydrology is a domain segment inside that root. `schema/` is a test lane, not the schema authority root, contract root, policy root, lifecycle store, source registry, proof store, release home, public API surface, or public map surface.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Hydrology schema tests | `tests/domains/hydrology/schema/` | This directory. |
| Machine-checkable Hydrology shape | `schemas/contracts/v1/domains/hydrology/` | Schema files under test; not redefined here. |
| Human-readable meaning | `contracts/domains/hydrology/` | Paired semantic contracts; tests check parity only. |
| Hydrology doctrine | `docs/domains/hydrology/` | Context for object families, identity, source roles, and lifecycle. |
| Synthetic fixtures | `fixtures/domains/hydrology/schema/` | Preferred toy valid/invalid examples if populated. |
| Policy homes | `policy/domains/hydrology/` | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/hydrology/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Schemas define shape, not truth.** Hydrology schemas may validate machine structure, but they do not prove evidence, decide policy, approve release, infer source role, fix rights, or publish data. Contract meaning, schema shape, fixtures, policy, evidence, lifecycle, and release must remain separate roots.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Schema validity | JSON Schema documents parse and declare an expected draft where material. | validation failure / `ERROR`. |
| Pairing | Schema `x-kfm.contract_doc`, `$id`, title, and path align with the paired Hydrology contract where known. | validation failure / NEEDS VERIFICATION. |
| Scaffold honesty | PROPOSED scaffolds with permissive `additionalProperties: true` remain labeled as incomplete. | validation failure. |
| Contract/schema split | Tests do not treat contract prose as schema shape or schema pass as semantic truth. | validation failure. |
| Fixture parity | Valid/invalid fixtures exercise declared required fields when mature enough to enforce. | validation failure / NEEDS VERIFICATION. |
| Source-role posture | Schema fields do not silently collapse observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic roles. | validation failure / `ABSTAIN`. |
| Evidence/release posture | Schema validation does not replace EvidenceBundle, PolicyDecision, ReleaseManifest, correction, or rollback gates. | promotion-blocking failure. |
| No network | Schema tests use local files only. | validation failure / `ERROR`. |

---

## Expected scope

Tests in this lane may validate:

- Hydrology schema files parse as JSON and follow expected `$schema` / `$id` conventions;
- paired contracts exist for schemas that claim a `contract_doc`;
- schema descriptions and `x-kfm.status` preserve PROPOSED / scaffold labels where fields are incomplete;
- permissive scaffolds are not used as proof of strict validation;
- fixture examples do not require live sources or lifecycle stores;
- schema paths stay under `schemas/contracts/v1/domains/hydrology/` unless an ADR or migration note says otherwise;
- schema checks do not bypass policy, evidence, release, correction, or rollback roots.

Live source checks, real source exports, production credentials, public tile generation, and real hydrology payloads are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected pass/fail outcome;
- explicit schema path, paired contract path, scaffold/maturity posture, evidence posture, policy state, release relationship, correction, and rollback posture where material;
- no real source exports, lifecycle data, public tiles, credentials, restricted records, or published artifacts.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Local schema parses and declares correct scaffold posture | accepted schema support only. |
| Schema has invalid JSON or invalid `$schema` value | validation failure / `ERROR`. |
| Schema points to missing paired contract | validation failure / NEEDS VERIFICATION. |
| Schema is permissive but represented as strict enforcement | validation failure. |
| Contract prose and schema shape disagree materially | `ABSTAIN` / drift entry / validation failure. |
| Fixture fails schema unexpectedly | validation failure. |
| Schema pass is treated as evidence closure or release approval | promotion-blocking failure. |
| Network access is attempted | validation failure / `ERROR`. |

---

## Suggested layout

```text
tests/domains/hydrology/schema/
├── README.md
├── test_schema_files_parse.py
├── test_schema_contract_pairing.py
├── test_scaffold_status_is_honest.py
├── test_additional_properties_posture.py
├── test_fixture_schema_parity.py
├── test_source_role_fields_not_collapsed.py
└── test_schema_not_evidence_policy_or_release.py
```

---

## Run posture

```bash
pytest tests/domains/hydrology/schema
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/hydrology/schema/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `tests/domains/hydrology/README.md` | CONFIRMED | Hydrology test parent currently exists as a greenfield stub. | Parent lane still needs expansion. |
| `schemas/contracts/v1/domains/hydrology/README.md` | CONFIRMED schema-lane doc | Defines the Hydrology schema lane as machine-checkable shape and excludes contract prose, policy, validator code, lifecycle data, registry data, proof output, receipts, source descriptor instances, and release authority. | Its inventory notes may be stale relative to later observed schema files. |
| `schemas/contracts/v1/domains/hydrology/reach_identity.schema.json` | CONFIRMED schema file | Exists as a JSON Schema 2020-12 object with PROPOSED `x-kfm.status`, paired contract pointer, empty properties, and `additionalProperties: true`. | It is a permissive scaffold, not strict validation proof. |
| `contracts/domains/hydrology/README.md` and `reach_identity.md` | CONFIRMED semantic contract evidence | Contracts own human-readable meaning and record schema scaffolding / NEEDS VERIFICATION posture. | Contract prose is not schema enforcement or runtime proof. |

---

## Validation checklist

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Schema discovery is deterministic and no-network.
- [ ] Hydrology schemas parse under the expected JSON Schema draft.
- [ ] Claimed paired contract paths resolve locally or produce finite NEEDS VERIFICATION output.
- [ ] Permissive scaffolds are detected and not counted as strict validation.
- [ ] Synthetic valid/invalid fixtures exist for mature schemas before required-field assertions are enforced.
- [ ] EvidenceRef / EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, and RollbackCard expectations remain referenced but not bypassed.
- [ ] CI runs the no-network Hydrology schema suite or marks it as an expected gap.
- [ ] Failures block contract/schema promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a schema authority, contract root, policy authority, fixture authority, source registry, lifecycle data store, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, live source fetcher, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
