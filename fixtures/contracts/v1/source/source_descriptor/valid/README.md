<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/source/source-descriptor/valid/readme
title: source_descriptor valid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): source steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): rights steward; TODO(owner): sensitivity steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - valid_1.json
  - ../invalid/README.md
  - ../invalid/invalid_1.json
  - ../invalid/invalid_1.expected_error.txt
  - ../../../../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../../../../contracts/source/source_descriptor.md
  - ../../../../../../contracts/source/ingest_receipt.md
  - ../../../../../../policy/source/
  - ../../../../../../policy/rights/
  - ../../../../../../policy/sensitivity/
  - ../../../../../../data/registry/sources/
  - ../../../../../../tools/validators/sources/validate_source_descriptor.py
  - ../../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, source, source-descriptor, valid-fixtures, json-schema, source-admission, source-role, rights, sensitivity, cadence, access, citation, source-head, review-state, release-state, lifecycle, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/source/source_descriptor/valid/README.md`."
  - "Valid fixtures are positive schema examples for the `source_descriptor` schema."
  - "Current valid fixture coverage is one passing SourceDescriptor example: `valid_1.json`."
  - "The paired schema currently declares `fixtures_root` as `tests/fixtures/sources/source_descriptor/`; this README documents the observed contract fixture path requested here, so fixture-root reconciliation remains NEEDS VERIFICATION."
  - "No tests, validators, source admission workflows, source registry checks, rights/sensitivity policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `source_descriptor` valid fixtures

Positive fixture lane for the KFM `source_descriptor` source contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: source" src="https://img.shields.io/badge/family-source-blue">
  <img alt="Contract: source_descriptor" src="https://img.shields.io/badge/contract-source__descriptor-purple">
  <img alt="Lane: valid" src="https://img.shields.io/badge/lane-valid-success">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/source/source_descriptor/valid/README.md`  
**Fixture posture:** valid JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/source/source_descriptor.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Why this fixture passes](#why-this-fixture-passes) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to pass schema validation. They are not source registry records, rights decisions, sensitivity decisions, EvidenceBundles, PolicyDecisions, ReleaseManifests, source truth, release approval, or publication authority.

---

## Purpose

This directory stores positive JSON examples for the `source_descriptor` schema.

Use this lane to prove that a well-shaped `SourceDescriptor` example can pass schema validation before source records are relied on by source admission, registry, ingest, policy, evidence, catalog, release, map, API, or AI workflows. Passing this schema fixture proves shape only. It does not prove the source's claims are true, evidence is sufficient, rights are settled for every use, public release is approved, or downstream consumers may bypass governance.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`valid_1.json`](valid_1.json) | Positive SourceDescriptor fixture for a USGS NWIS hydrology source. | Schema validation should pass. | CONFIRMED |

Current valid fixture highlights:

```json
{
  "object_type": "SourceDescriptor",
  "schema_version": "v1",
  "source_id": "src:usgs-nwis-hydrology",
  "descriptor_version": "1.0.0",
  "title": "USGS National Water Information System",
  "source_type": "official_government_dataset",
  "source_role": "authoritative_for_claim",
  "authority_rank": "primary_authority",
  "sensitivity_default": "public",
  "review_state": "approved",
  "release_state": "released"
}
```

The fixture also includes the required publisher, owner/steward, rights, cadence, access, citation, source-head, admissibility, public-release, and lifecycle objects.

The paired negative fixture omits required `source_id` and should fail validation with the expected-error matcher `required`.

---

## Schema basis

The current schema evidence for this fixture lane is:

```text
schemas/contracts/v1/source/source_descriptor.schema.json
```

Confirmed schema facts:

| Item | Value |
|---|---|
| Schema title | `source_descriptor` |
| Root type | object |
| Object-family const | `object_type: SourceDescriptor` |
| Schema-version const | `schema_version: v1` |
| Required identity fields | `object_type`, `schema_version`, `source_id`, `descriptor_version`, `title` |
| Required governance fields | `source_type`, `source_role`, `authority_rank`, `publisher`, `owner_or_steward`, `rights`, `sensitivity_default`, `cadence`, `access`, `citation`, `source_head`, `admissibility_limits`, `public_release`, `review_state`, `release_state`, `lifecycle` |
| `source_id` pattern | `kfm://source/...` or `src:...` |
| `descriptor_version` pattern | semantic-version string such as `1.0.0` |
| Conditional rules | rights, sensitivity, connectors, source role, and public release conditionals are expressed in schema `allOf` rules |
| Additional properties | false |
| Declared contract doc | `contracts/source/source_descriptor.md` |
| Declared registry home | `data/registry/sources/` |
| Declared policy path | `policy/source/` |
| Declared validator | `tools/validators/sources/validate_source_descriptor.py` |
| Schema status | `PROPOSED` |

> [!NOTE]
> The schema currently declares `fixtures_root` as `tests/fixtures/sources/source_descriptor/`, while this README documents `fixtures/contracts/v1/source/source_descriptor/valid/` because that is the requested and observed fixture path. Reconciliation of fixture-root conventions remains **NEEDS VERIFICATION**.

---

## Why this fixture passes

`valid_1.json` includes every required top-level field currently required by the paired schema, including the stable source identifier:

```text
source_id: src:usgs-nwis-hydrology
```

It also uses schema-compatible values for object type, schema version, descriptor version, source type, source role, authority rank, rights posture, sensitivity, cadence, access, citation, source-head identity, admissibility limits, public release, review state, release state, and lifecycle state.

This positive fixture is intentionally reviewable. It proves the schema accepts a complete descriptor-shaped example, not that the source is currently available, not that all rights and sensitivity checks have been re-run, and not that any downstream release has been approved by this fixture.

> [!WARNING]
> `SourceDescriptor` records source admission and treatment posture. It does not make source claims true, authorize release by itself, replace evidence, or let connectors, pipelines, UI, maps, or AI bypass review and policy gates.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Positive fixture examples | `fixtures/contracts/v1/source/source_descriptor/valid/` | CONFIRMED |
| Negative fixture examples | `fixtures/contracts/v1/source/source_descriptor/invalid/` | CONFIRMED |
| Machine-checkable shape | `schemas/contracts/v1/source/source_descriptor.schema.json` | CONFIRMED |
| Semantic contract | `contracts/source/source_descriptor.md` | CONFIRMED |
| Source registry records | `data/registry/sources/` | OUT OF SCOPE FOR THIS README |
| Source / rights / sensitivity policy | `policy/source/`, `policy/rights/`, `policy/sensitivity/` | OUT OF SCOPE FOR THIS README |
| Dedicated validator implementation | `tools/validators/sources/validate_source_descriptor.py` | NEEDS VERIFICATION |
| Common schema fixture harness | `tests/schemas/test_common_contracts.py` | CONFIRMED doctrine pattern from prior fixture work / NOT RUN |

Do not collapse this fixture lane into the semantic contract, schema, source registry, rights review, sensitivity review, source admission workflow, SourceDescriptor truth, IngestReceipt, EvidenceBundle, PolicyDecision, ReleaseManifest, source truth, or publication authority.

---

## Harness behavior

The common schema fixture convention for contract fixtures is:

```text
fixtures/contracts/v1/<family>/<name>/
```

For valid fixtures, the expected pattern is:

```text
valid/valid_*.json
```

Expected behavior:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | No JSON Schema errors. |

This README documents expected fixture behavior only. It does not claim that pytest, CI, source registry resolution, rights/sensitivity policy, release checks, or the dedicated SourceDescriptor validator were run during this update.

---

## Maintenance checklist

Before changing this valid fixture lane:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep at least one complete positive SourceDescriptor fixture unless this fixture family is intentionally retired.
- [ ] Keep positive fixtures paired with negative fixtures under `../invalid/`.
- [ ] Add fixture-only, restricted-rights, restricted-sensitivity, not-released, candidate, connector-disabled, and lifecycle-quarantined valid examples when coverage expands.
- [ ] Keep fixture examples public-safe and limited to descriptor-shaped metadata.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not embed full source payloads or release-blocked material in fixtures.
- [ ] Update this README when schema fields, enum values, conditional rules, source-id conventions, fixture-root conventions, or fixture coverage changes.
- [ ] Run the schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Valid fixture | CONFIRMED | `valid_1.json` exists and includes required `source_id: "src:usgs-nwis-hydrology"`. |
| Invalid lane README | CONFIRMED | `../invalid/README.md` exists and documents the missing-required-field case. |
| Invalid fixture | CONFIRMED | `../invalid/invalid_1.json` exists and omits required `source_id`. |
| Expected-error file | CONFIRMED | `../invalid/invalid_1.expected_error.txt` exists and contains `required`. |
| Schema | CONFIRMED | `source_descriptor.schema.json` defines the rich required field surface, source-id pattern, controlled vocabularies, conditional rules, registry/policy/validator metadata, and closed additional-property posture. |
| Contract | CONFIRMED | `contracts/source/source_descriptor.md` defines semantic meaning and distinguishes SourceDescriptor from source truth, evidence sufficiency, policy approval, release approval, and bypass authority. |
| Fixture-root convention | NEEDS VERIFICATION | Schema `x-kfm.fixtures_root` points to `tests/fixtures/sources/source_descriptor/`, while the observed/requested path is under `fixtures/contracts/v1/source/source_descriptor/`. |
| Test execution | NOT RUN | No validators, pytest, source registry checks, rights/sensitivity policy checks, source admission checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define valid-fixture guidance. |
| [`valid_1.json`](valid_1.json) | CONFIRMED | Current positive fixture includes required `source_id` and the broader descriptor field surface. | Only one valid case is currently documented here. |
| [`../invalid/README.md`](../invalid/README.md) | CONFIRMED | Documents the negative fixture lane. | Does not prove tests were run. |
| [`../invalid/invalid_1.json`](../invalid/invalid_1.json) | CONFIRMED | Paired negative fixture omits required `source_id`. | Only one invalid case is currently documented there. |
| [`../invalid/invalid_1.expected_error.txt`](../invalid/invalid_1.expected_error.txt) | CONFIRMED | Expected matcher is `required`. | Broad matcher; may be tightened later. |
| [`../../../../../../schemas/contracts/v1/source/source_descriptor.schema.json`](../../../../../../schemas/contracts/v1/source/source_descriptor.schema.json) | CONFIRMED | Schema shape, required fields, source-id pattern, descriptor-version pattern, controlled vocabularies, conditionals, additional-property behavior, contract path, registry home, validator path, policy path, and status. | Schema status is `PROPOSED`; validator implementation was not verified; fixture root points elsewhere. |
| [`../../../../../../contracts/source/source_descriptor.md`](../../../../../../contracts/source/source_descriptor.md) | CONFIRMED | Semantic meaning, source-admission role, required surface, source treatment boundary, and distinction from source truth, evidence sufficiency, policy approval, release approval, and bypass authority. | Does not prove source registry maturity, validator wiring, policy behavior, release checks, or CI status. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | `fixtures/` is within the validate/operate authority surface and supports test inputs while contracts, schemas, policy, registry, and lifecycle data remain separate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
