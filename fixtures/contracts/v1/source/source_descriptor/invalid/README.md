<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/source/source-descriptor/invalid/readme
title: source_descriptor invalid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): source steward; TODO(owner): schema steward; TODO(owner): fixture steward; TODO(owner): validator steward; TODO(owner): rights steward; TODO(owner): sensitivity steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: public-review
related:
  - ../valid/valid_1.json
  - invalid_1.json
  - invalid_1.expected_error.txt
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
tags: [kfm, fixtures, contracts, v1, source, source-descriptor, invalid-fixtures, expected-error, json-schema, source-admission, source-role, rights, sensitivity, cadence, access, citation, source-head, review-state, release-state, lifecycle, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/source/source_descriptor/invalid/README.md`."
  - "Invalid fixtures are intentionally failing examples for the `source_descriptor` schema."
  - "Current invalid fixture coverage is one missing-required-field case: `invalid_1.json` omits `source_id`; matcher `required`."
  - "The paired schema currently declares `fixtures_root` as `tests/fixtures/sources/source_descriptor/`; this README documents the observed contract fixture path requested here, so fixture-root reconciliation remains NEEDS VERIFICATION."
  - "No tests, validators, source admission workflows, source registry checks, rights/sensitivity policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `source_descriptor` invalid fixtures

Negative fixture lane for the KFM `source_descriptor` source contract schema.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: source" src="https://img.shields.io/badge/family-source-blue">
  <img alt="Contract: source_descriptor" src="https://img.shields.io/badge/contract-source__descriptor-purple">
  <img alt="Lane: invalid" src="https://img.shields.io/badge/lane-invalid-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/source/source_descriptor/invalid/README.md`  
**Fixture posture:** invalid JSON Schema fixture lane  
**Authority posture:** fixture only; schema authority lives in `schemas/contracts/v1/source/source_descriptor.schema.json`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Schema basis](#schema-basis) · [Why this fixture fails](#why-this-fixture-fails) · [Authority boundary](#authority-boundary) · [Harness behavior](#harness-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected to fail schema validation. They are not SourceDescriptors, source registry records, rights decisions, sensitivity decisions, EvidenceBundles, PolicyDecisions, ReleaseManifests, source truth, release approval, or publication authority.

---

## Purpose

This directory stores negative JSON examples for the `source_descriptor` schema.

Use this lane to prove that incomplete source descriptors are rejected before they can be treated as governed source-admission records. Invalid fixtures help preserve KFM's source boundary: a `SourceDescriptor` records how source material may be treated, but fixture shape alone must not become source truth, evidence sufficiency, policy approval, review approval, or release approval.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`invalid_1.json`](invalid_1.json) | Negative fixture missing required `source_id`. | Schema validation should fail. | CONFIRMED |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | Expected-error matcher for `invalid_1.json`. | Combined schema errors should include `required`. | CONFIRMED |

The current invalid fixture is otherwise descriptor-shaped but omits the required stable source identifier:

```json
{
  "object_type": "SourceDescriptor",
  "schema_version": "v1",
  "descriptor_version": "1.0.0",
  "title": "USGS National Water Information System",
  "description": "Invalid fixture: the required source_id property is omitted."
}
```

The paired positive fixture includes the required field:

```json
{
  "object_type": "SourceDescriptor",
  "schema_version": "v1",
  "source_id": "src:usgs-nwis-hydrology",
  "descriptor_version": "1.0.0",
  "title": "USGS National Water Information System"
}
```

The snippets above are shortened for readability; the actual fixtures include the broader required descriptor surface.

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
> The schema currently declares `fixtures_root` as `tests/fixtures/sources/source_descriptor/`, while this README documents `fixtures/contracts/v1/source/source_descriptor/invalid/` because that is the requested and observed fixture path. Reconciliation of fixture-root conventions remains **NEEDS VERIFICATION**.

---

## Why this fixture fails

`invalid_1.json` fails the current schema because it omits:

```text
source_id
```

The paired schema requires `source_id` as the stable source identifier and constrains it to either a `kfm://source/...` or `src:...` pattern. The expected-error file currently uses the broad matcher:

```text
required
```

That failure matters because a `SourceDescriptor` without a stable `source_id` cannot be reliably linked to source registry records, ingest receipts, citation surfaces, policy decisions, evidence assembly, release review, correction paths, or downstream public surfaces.

> [!WARNING]
> `SourceDescriptor` records source admission and treatment posture. It does not make source claims true, authorize release by itself, replace evidence, or let connectors, pipelines, UI, maps, or AI bypass review and policy gates.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Negative fixture examples | `fixtures/contracts/v1/source/source_descriptor/invalid/` | CONFIRMED |
| Positive fixture examples | `fixtures/contracts/v1/source/source_descriptor/valid/` | CONFIRMED file present / README not checked in this update |
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

For invalid fixtures, the expected pattern is:

```text
invalid/invalid_*.json
invalid/invalid_*.expected_error.txt
```

Expected behavior:

| Fixture pattern | Expected result |
|---|---|
| `invalid/invalid_*.json` | At least one JSON Schema error. |
| `invalid/invalid_*.expected_error.txt` | Expected text appears in the combined schema error messages. |

This README documents expected fixture behavior only. It does not claim that pytest, CI, source registry resolution, rights/sensitivity policy, release checks, or the dedicated SourceDescriptor validator were run during this update.

---

## Maintenance checklist

Before changing this invalid fixture lane:

- [ ] Keep failing examples under `invalid/invalid_<n>.json`.
- [ ] Keep expected-error text beside the invalid fixture it describes.
- [ ] Keep at least one missing-required-identity failure unless another fixture family covers that failure class.
- [ ] Add source-id-pattern, descriptor-version-pattern, const, enum, nested required, source-head anyOf, conditional rights, conditional sensitivity, connector, public-release, additional-property, and deprecated-alias migration failures when coverage expands.
- [ ] Keep fixture examples public-safe and limited to descriptor-shaped metadata.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not embed full source payloads or release-blocked material in fixtures.
- [ ] Update this README when schema fields, enum values, conditional rules, source-id conventions, fixture-root conventions, or expected-error behavior changes.
- [ ] Run the schema fixture test before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Invalid fixture | CONFIRMED | `invalid_1.json` exists and omits required `source_id`. |
| Expected-error file | CONFIRMED | `invalid_1.expected_error.txt` exists and contains `required`. |
| Positive fixture | CONFIRMED | `valid/valid_1.json` exists and includes required `source_id: "src:usgs-nwis-hydrology"`. |
| Schema | CONFIRMED | `source_descriptor.schema.json` defines the rich required field surface, source-id pattern, controlled vocabularies, conditional rules, registry/policy/validator metadata, and closed additional-property posture. |
| Contract | CONFIRMED | `contracts/source/source_descriptor.md` defines semantic meaning and distinguishes SourceDescriptor from source truth, evidence sufficiency, policy approval, release approval, and bypass authority. |
| Fixture-root convention | NEEDS VERIFICATION | Schema `x-kfm.fixtures_root` points to `tests/fixtures/sources/source_descriptor/`, while the observed/requested path is under `fixtures/contracts/v1/source/source_descriptor/`. |
| Test execution | NOT RUN | No validators, pytest, source registry checks, rights/sensitivity policy checks, source admission checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define invalid-fixture guidance. |
| [`invalid_1.json`](invalid_1.json) | CONFIRMED | Current negative fixture omits required `source_id`. | Only one invalid case is currently documented here. |
| [`invalid_1.expected_error.txt`](invalid_1.expected_error.txt) | CONFIRMED | Expected matcher is `required`. | Broad matcher; may be tightened later. |
| [`../valid/valid_1.json`](../valid/valid_1.json) | CONFIRMED | Paired positive fixture includes required `source_id` and the broader descriptor field surface. | Positive lane README was not checked during this update. |
| [`../../../../../../schemas/contracts/v1/source/source_descriptor.schema.json`](../../../../../../schemas/contracts/v1/source/source_descriptor.schema.json) | CONFIRMED | Schema shape, required fields, source-id pattern, descriptor-version pattern, controlled vocabularies, conditionals, additional-property behavior, contract path, registry home, validator path, policy path, and status. | Schema status is `PROPOSED`; validator implementation was not verified; fixture root points elsewhere. |
| [`../../../../../../contracts/source/source_descriptor.md`](../../../../../../contracts/source/source_descriptor.md) | CONFIRMED | Semantic meaning, source-admission role, required surface, source treatment boundary, and distinction from source truth, evidence sufficiency, policy approval, release approval, and bypass authority. | Does not prove source registry maturity, validator wiring, policy behavior, release checks, or CI status. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | `fixtures/` is within the validate/operate authority surface and supports test inputs while contracts, schemas, policy, registry, and lifecycle data remain separate roots. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
