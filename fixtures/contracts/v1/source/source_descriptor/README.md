<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/source/source-descriptor/readme
title: source_descriptor fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): source steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): rights steward; TODO(owner): sensitivity steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - valid/README.md
  - valid/valid_1.json
  - invalid/README.md
  - invalid/invalid_1.json
  - invalid/invalid_1.expected_error.txt
  - ../../../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../../../contracts/source/source_descriptor.md
  - ../../../../../contracts/source/ingest_receipt.md
  - ../../../../../policy/source/
  - ../../../../../policy/rights/
  - ../../../../../policy/sensitivity/
  - ../../../../../data/registry/sources/
  - ../../../../../tools/validators/sources/validate_source_descriptor.py
  - ../../../../../tests/schemas/test_common_contracts.py
  - ../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, source, source-descriptor, valid-fixtures, invalid-fixtures, expected-error, json-schema, source-admission, source-role, rights, sensitivity, cadence, access, citation, source-head, review-state, release-state, lifecycle, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/source/source_descriptor/README.md`."
  - "This directory is the observed contract fixture family for `source_descriptor`."
  - "Current fixture coverage includes one valid SourceDescriptor example and one invalid missing-required-field example."
  - "The paired schema currently declares `fixtures_root` as `tests/fixtures/sources/source_descriptor/`; this README documents the requested and observed `fixtures/contracts/v1/source/source_descriptor/` path, so fixture-root reconciliation remains NEEDS VERIFICATION."
  - "No tests, validators, source admission workflows, source registry checks, rights/sensitivity policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `source_descriptor` fixtures

Fixture family for the KFM `source_descriptor` source contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: source" src="https://img.shields.io/badge/family-source-blue">
  <img alt="Contract: source_descriptor" src="https://img.shields.io/badge/contract-source__descriptor-purple">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
  <img alt="Root mismatch: needs verification" src="https://img.shields.io/badge/fixture__root-NEEDS%20VERIFICATION-orange">
</p>

**Path:** `fixtures/contracts/v1/source/source_descriptor/README.md`  
**Fixture posture:** JSON Schema valid/invalid fixture family  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/source/source_descriptor.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are schema fixtures. They are not source registry records, rights decisions, sensitivity decisions, EvidenceBundles, PolicyDecisions, ReleaseManifests, source truth, review approval, release approval, or publication authority.

---

## Purpose

This directory groups positive and negative JSON fixtures for the `source_descriptor` schema.

Use this fixture family to verify that KFM accepts a complete descriptor-shaped source-admission example and rejects descriptor-shaped metadata that lacks a stable source identifier. The fixture family keeps source-descriptor shape testable without turning fixture examples into source truth, evidence sufficiency, policy approval, review approval, release approval, or public-client authority.

A passing fixture proves schema shape only. It does not prove the source's claims are true, that the source is currently reachable, that all rights and sensitivity checks have been re-run, that release is approved, or that downstream consumers may bypass governance.

---

## Current inventory

| Lane | File | Current role | Status |
|---|---|---|---|
| [`valid/`](valid/README.md) | [`valid_1.json`](valid/valid_1.json) | Positive SourceDescriptor fixture for a USGS NWIS hydrology source. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.json`](invalid/invalid_1.json) | Negative fixture missing required `source_id`. | CONFIRMED |
| [`invalid/`](invalid/README.md) | [`invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | Expected-error matcher currently set to `required`. | CONFIRMED |

Current positive fixture highlights:

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

Current negative fixture highlights:

```json
{
  "object_type": "SourceDescriptor",
  "schema_version": "v1",
  "descriptor_version": "1.0.0",
  "title": "USGS National Water Information System",
  "description": "Invalid fixture: the required source_id property is omitted."
}
```

The snippets above are shortened for readability. The actual fixtures include the broader descriptor field surface needed for schema validation context.

---

## Schema basis

The current schema evidence for this fixture family is:

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
| Controlled vocabularies | source type, source role, authority rank, claim role, sensitivity class, rights status, permission state, cadence, access method, access posture, review state, release state, and lifecycle registry state |
| Conditional rules | rights, sensitivity, connectors, source role, and public release conditionals are expressed in schema `allOf` rules |
| Additional properties | false |
| Declared contract doc | `contracts/source/source_descriptor.md` |
| Declared registry home | `data/registry/sources/` |
| Declared policy path | `policy/source/` |
| Declared validator | `tools/validators/sources/validate_source_descriptor.py` |
| Schema status | `PROPOSED` |

> [!NOTE]
> The schema currently declares `fixtures_root` as `tests/fixtures/sources/source_descriptor/`, while this README documents `fixtures/contracts/v1/source/source_descriptor/` because that is the requested and observed fixture path. Reconciliation of fixture-root conventions remains **NEEDS VERIFICATION**.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Fixture examples | `fixtures/contracts/v1/source/source_descriptor/` | CONFIRMED |
| Positive fixture examples | `fixtures/contracts/v1/source/source_descriptor/valid/` | CONFIRMED |
| Negative fixture examples | `fixtures/contracts/v1/source/source_descriptor/invalid/` | CONFIRMED |
| Machine-checkable shape | `schemas/contracts/v1/source/source_descriptor.schema.json` | CONFIRMED |
| Semantic contract | `contracts/source/source_descriptor.md` | CONFIRMED |
| Source registry records | `data/registry/sources/` | OUT OF SCOPE FOR THIS README |
| Source / rights / sensitivity policy | `policy/source/`, `policy/rights/`, `policy/sensitivity/` | OUT OF SCOPE FOR THIS README |
| Dedicated validator implementation | `tools/validators/sources/validate_source_descriptor.py` | NEEDS VERIFICATION |
| Common schema fixture harness | `tests/schemas/test_common_contracts.py` | CONFIRMED doctrine pattern from prior fixture work / NOT RUN |

`SourceDescriptor` must remain distinguishable from:

| Do not collapse `SourceDescriptor` into | Why |
|---|---|
| Source truth | A descriptor records how a source may be treated; it does not make source claims true. |
| EvidenceBundle | Evidence supports claims; source descriptors govern source posture. |
| IngestReceipt | IngestReceipt records capture events; SourceDescriptor governs source identity and admissibility posture. |
| PolicyDecision | Policy decides admissibility; descriptor metadata does not approve use by itself. |
| ReleaseManifest | Release manifests bind released artifacts; source descriptors do not publish. |
| Public-client permission | Public clients still require governed APIs, release state, policy checks, citations, and rollback posture. |

---

## Harness behavior

The common schema fixture convention for contract fixtures is:

```text
fixtures/contracts/v1/<family>/<name>/
```

For this source family, that means:

```text
fixtures/contracts/v1/source/source_descriptor/
```

Observed fixture layout:

```text
fixtures/contracts/v1/source/source_descriptor/
  README.md
  valid/
    README.md
    valid_1.json
  invalid/
    README.md
    invalid_1.json
    invalid_1.expected_error.txt
```

Expected behavior:

| Fixture pattern | Expected result |
|---|---|
| `valid/valid_*.json` | no JSON Schema errors |
| `invalid/invalid_*.json` | at least one JSON Schema error |
| `invalid/invalid_*.expected_error.txt` | expected text appears in combined schema error messages |

This README documents expected fixture behavior only. It does not claim that pytest, CI, source registry resolution, rights/sensitivity policy, release checks, or the dedicated SourceDescriptor validator was run during this update.

---

## Maintenance checklist

Before changing this fixture family:

- [ ] Keep passing examples under `valid/valid_<n>.json`.
- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep at least one complete positive fixture and one missing-required-identity invalid fixture.
- [ ] Add source-id-pattern, descriptor-version-pattern, const, enum, nested required, source-head anyOf, conditional rights, conditional sensitivity, connector, public-release, additional-property, and deprecated-alias migration failures when coverage expands.
- [ ] Add fixture-only, restricted-rights, restricted-sensitivity, not-released, candidate, connector-disabled, and lifecycle-quarantined valid examples when coverage expands.
- [ ] Keep fixture examples public-safe and limited to descriptor-shaped metadata.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not embed full source payloads or release-blocked material in fixtures.
- [ ] Update parent and lane READMEs when schema fields, enum values, conditional rules, source-id conventions, fixture-root conventions, or fixture coverage changes.
- [ ] Run the common schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Valid lane | CONFIRMED | `valid/README.md` and `valid/valid_1.json` exist. |
| Invalid lane | CONFIRMED | `invalid/README.md`, `invalid/invalid_1.json`, and `invalid_1.expected_error.txt` exist. |
| Schema | CONFIRMED | `source_descriptor.schema.json` defines the rich required field surface, source-id pattern, controlled vocabularies, conditional rules, registry/policy/validator metadata, and closed additional-property posture. |
| Contract | CONFIRMED | `contracts/source/source_descriptor.md` defines semantic meaning and separates SourceDescriptor from source truth, evidence sufficiency, policy approval, release approval, and bypass authority. |
| Fixture-root convention | NEEDS VERIFICATION | Schema `x-kfm.fixtures_root` points to `tests/fixtures/sources/source_descriptor/`, while the observed/requested path is under `fixtures/contracts/v1/source/source_descriptor/`. |
| Test execution | NOT RUN | No validators, pytest, source registry checks, rights/sensitivity policy checks, source admission checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture-family guidance. |
| [`valid/README.md`](valid/README.md) | CONFIRMED | Positive fixture lane guidance. | Does not prove tests were run. |
| [`valid/valid_1.json`](valid/valid_1.json) | CONFIRMED | Current positive fixture includes required `source_id` and the broader descriptor field surface. | Only one valid fixture is currently documented. |
| [`invalid/README.md`](invalid/README.md) | CONFIRMED | Negative fixture lane guidance. | Does not prove tests were run. |
| [`invalid/invalid_1.json`](invalid/invalid_1.json) | CONFIRMED | Current negative fixture omits required `source_id`. | Only one invalid fixture is currently documented. |
| [`invalid/invalid_1.expected_error.txt`](invalid/invalid_1.expected_error.txt) | CONFIRMED | Current expected matcher is `required`. | Broad matcher; may be tightened later. |
| [`../../../../../schemas/contracts/v1/source/source_descriptor.schema.json`](../../../../../schemas/contracts/v1/source/source_descriptor.schema.json) | CONFIRMED | Schema shape, required fields, source-id pattern, descriptor-version pattern, controlled vocabularies, conditionals, additional-property behavior, contract path, registry home, validator path, policy path, and status. | Schema status is `PROPOSED`; validator implementation was not verified; fixture root points elsewhere. |
| [`../../../../../contracts/source/source_descriptor.md`](../../../../../contracts/source/source_descriptor.md) | CONFIRMED | Semantic meaning, source-admission role, required surface, source treatment boundary, and distinction from source truth, evidence sufficiency, policy approval, release approval, and bypass authority. | Does not prove source registry maturity, validator wiring, policy behavior, release checks, or CI status. |
| `../../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | `fixtures/` is within the validate/operate authority surface and supports test inputs while contracts, schemas, policy, registry, and lifecycle data remain separate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
