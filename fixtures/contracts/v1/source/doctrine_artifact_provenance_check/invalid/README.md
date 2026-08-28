<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/source/doctrine-artifact-provenance-check/invalid/readme
title: doctrine_artifact_provenance_check invalid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): doctrine steward; TODO(owner): source steward; TODO(owner): policy steward; TODO(owner): fixture steward; TODO(owner): maintenance steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - placeholder_urls.expected.json
  - ../valid/sync_no_change.expected.json
  - ../valid/sync_changed.expected.json
  - ../../../../../../scripts/maintenance/check_doctrine_artifact_provenance.py
  - ../../../../../../scripts/maintenance/sync_doctrine_artifact_provenance_status.py
  - ../../../../../../tests/policy/test_doctrine_artifact_provenance.py
  - ../../../../../../tests/policy/test_doctrine_artifact_provenance_snapshots.py
  - ../../../../../../schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, source, doctrine-artifact-provenance-check, invalid-fixtures, snapshot-fixtures, policy-tests, provenance, placeholder-url, source-admission, doctrine, maintenance, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/source/doctrine_artifact_provenance_check/invalid/README.md`."
  - "This fixture lane currently holds an expected failing snapshot for the doctrine artifact provenance checker, not a conventional `invalid_1.json` JSON Schema fixture."
  - "Current invalid fixture coverage is one placeholder-source-url failure snapshot: `placeholder_urls.expected.json`."
  - "Repository search found policy tests and the maintenance checker for this fixture family; it did not find a directly named `doctrine_artifact_provenance_check` schema during this update."
  - "No tests, validators, maintenance scripts, source admission workflows, provenance review workflows, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `doctrine_artifact_provenance_check` invalid fixtures

Negative snapshot fixture lane for the KFM doctrine artifact provenance checker.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: source" src="https://img.shields.io/badge/family-source-blue">
  <img alt="Check: doctrine_artifact_provenance" src="https://img.shields.io/badge/check-doctrine__artifact__provenance-purple">
  <img alt="Lane: invalid" src="https://img.shields.io/badge/lane-invalid-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/source/doctrine_artifact_provenance_check/invalid/README.md`  
**Fixture posture:** invalid / failing snapshot fixture lane  
**Authority posture:** fixture only; checker behavior lives in `scripts/maintenance/check_doctrine_artifact_provenance.py` and tests under `tests/policy/`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Checker basis](#checker-basis) · [Why this fixture is invalid](#why-this-fixture-is-invalid) · [Authority boundary](#authority-boundary) · [Test behavior](#test-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected failing snapshot fixtures. They are not source registries, doctrine artifacts, provenance records, EvidenceBundles, release decisions, policy decisions, steward review proof, or publication authority.

---

## Purpose

This directory stores expected failing output for the doctrine artifact provenance checker.

Use this lane to prove that placeholder doctrine artifact source URLs are detected and represented as a failed provenance-check payload. This fixture protects KFM's source-admission boundary: doctrine artifacts may be referenced by filename and descriptor metadata, but placeholder or unresolved source URLs must not be silently treated as verified provenance.

This fixture lane is **not** currently shaped like the common `invalid/invalid_*.json` schema-fixture pattern. The confirmed file in this directory is a snapshot-style expected JSON output used by policy tests.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`placeholder_urls.expected.json`](placeholder_urls.expected.json) | Expected failing payload for placeholder source URLs in the doctrine artifact provenance check. | Policy snapshot test should compare checker output against this payload. | CONFIRMED |

Current invalid snapshot fixture:

```json
{
  "check": "required_doctrine_artifact_provenance",
  "entry_count": 3,
  "invalid_status": [],
  "invalid_urls": [],
  "missing_fields": [],
  "placeholder_urls": [
    "KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf",
    "Master_MapLibre_Components-Functions-Features.pdf",
    "Kansas_Frontier_Matrix_Definitive_Greenfield_Building_Plan_v1_1.pdf"
  ],
  "result": "fail"
}
```

Paired valid snapshot fixtures currently live under `../valid/` for provenance-status synchronization cases:

| File | Current role | Status |
|---|---|---|
| [`../valid/sync_no_change.expected.json`](../valid/sync_no_change.expected.json) | Expected no-change sync payload. | CONFIRMED |
| [`../valid/sync_changed.expected.json`](../valid/sync_changed.expected.json) | Expected changed sync payload. | CONFIRMED |

---

## Checker basis

The current checker evidence for this fixture lane is:

```text
scripts/maintenance/check_doctrine_artifact_provenance.py
```

Confirmed checker facts:

| Item | Value |
|---|---|
| Check name | `required_doctrine_artifact_provenance` |
| Default registry input | `control_plane/doctrine_artifact_provenance_sources.yaml` |
| Required registry block | `required_doctrine_artifact_provenance:` |
| Required fields per entry | `filename`, `doc_id`, `source_url`, `status` |
| Allowed status values | `pending`, `verified`, `needs_verification` |
| Placeholder URL trigger | `source_url: NEEDS_VERIFICATION` |
| Disallowed placeholder hosts | `example.org`, `example.com`, `localhost` |
| Invalid URL trigger | `source_url` not starting with `http://` or `https://` |
| Failing result | `result: fail` when invalid URLs, invalid status, missing fields, or placeholder URLs are present |
| Failing return code | `1` when result is `fail` |

The related preflight-summary schema also contains a `provenance_payload` shape with `check: required_doctrine_artifact_provenance`, `result`, `invalid_urls`, `placeholder_urls`, `invalid_status`, and `missing_fields`. This README treats that as related schema evidence, not as a direct schema for this fixture family.

---

## Why this fixture is invalid

`placeholder_urls.expected.json` represents a failed provenance-check output because its `placeholder_urls` array is non-empty and `result` is `fail`.

That failure matters because source provenance must not remain a filename-only or placeholder-only assertion. A doctrine artifact provenance entry with unresolved source URL posture may be useful as a backlog item, but it must not be treated as verified source provenance, review proof, release approval, or publication authority.

The current snapshot names three affected doctrine artifact filenames:

- `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`
- `Master_MapLibre_Components-Functions-Features.pdf`
- `Kansas_Frontier_Matrix_Definitive_Greenfield_Building_Plan_v1_1.pdf`

> [!WARNING]
> This fixture records expected failing checker output. It does not prove that the checker was run in this documentation update, that the registry is current, that source URLs are verified, or that doctrine artifacts are admitted for release.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Failing snapshot fixture | `fixtures/contracts/v1/source/doctrine_artifact_provenance_check/invalid/` | CONFIRMED |
| Passing sync snapshot fixtures | `fixtures/contracts/v1/source/doctrine_artifact_provenance_check/valid/` | CONFIRMED file presence |
| Provenance checker implementation | `scripts/maintenance/check_doctrine_artifact_provenance.py` | CONFIRMED file content / NOT RUN |
| Provenance sync implementation | `scripts/maintenance/sync_doctrine_artifact_provenance_status.py` | REFERENCED BY TEST / NOT INSPECTED HERE |
| Policy tests | `tests/policy/test_doctrine_artifact_provenance.py` and `tests/policy/test_doctrine_artifact_provenance_snapshots.py` | CONFIRMED file content / NOT RUN |
| Direct JSON Schema for this fixture family | `schemas/contracts/v1/source/doctrine_artifact_provenance_check.schema.json` | NOT FOUND BY SEARCH / NEEDS VERIFICATION |
| Related preflight summary schema | `schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json` | CONFIRMED related shape / NOT DIRECT AUTHORITY |

Do not collapse this fixture lane into the source registry, provenance registry, doctrine artifact descriptor, preflight summary, maintenance checker, sync script, policy test, EvidenceBundle, ReleaseManifest, source truth, review proof, or publication authority.

---

## Test behavior

The policy tests confirm two behaviors relevant to this invalid fixture lane:

1. The provenance checker is expected to fail with return code `1` when placeholder URLs remain.
2. The snapshot test loads `placeholder_urls.expected.json` and compares selected keys from the checker output against it.

Observed test paths:

```text
tests/policy/test_doctrine_artifact_provenance.py
tests/policy/test_doctrine_artifact_provenance_snapshots.py
```

This README documents expected fixture behavior only. It does not claim that pytest, CI, source admission policy, doctrine artifact provenance checks, registry admission, release checks, or the maintenance checker were run during this update.

---

## Maintenance checklist

Before changing this invalid fixture lane:

- [ ] Keep failing snapshot examples under `invalid/` when they represent denied or failed provenance-check output.
- [ ] Keep expected JSON snapshots stable enough for policy tests to compare deterministically.
- [ ] Update tests if snapshot keys or checker payload structure changes.
- [ ] Add additional invalid snapshots for invalid URL, invalid status, missing field, and missing registry block cases when coverage expands.
- [ ] Keep fixture examples public-safe and limited to metadata-shaped filenames, statuses, URLs, and check payloads.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not embed full doctrine artifacts, raw evidence payloads, protected location detail, credentials, or release-blocked material in fixtures.
- [ ] Do not treat placeholder URLs as verified provenance.
- [ ] Run the relevant policy tests before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Invalid snapshot fixture | CONFIRMED | `placeholder_urls.expected.json` exists and records `result: fail` with three placeholder URLs. |
| Valid snapshot fixtures | CONFIRMED | `sync_no_change.expected.json` and `sync_changed.expected.json` exist under `../valid/`. |
| Checker script | CONFIRMED / NOT RUN | The checker defines allowed statuses, placeholder URL handling, invalid URL handling, missing field handling, payload output, and return-code behavior. |
| Policy tests | CONFIRMED / NOT RUN | Tests reference this invalid snapshot and expect checker failure for placeholder URLs. |
| Direct schema | NEEDS VERIFICATION | Search did not find a directly named schema for `doctrine_artifact_provenance_check`; the related preflight-summary schema includes the provenance payload shape. |
| Test execution | NOT RUN | No validators, pytest, source policy checks, doctrine provenance checks, registry checks, steward review checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define invalid-fixture guidance. |
| [`placeholder_urls.expected.json`](placeholder_urls.expected.json) | CONFIRMED | Current failing snapshot fixture with non-empty `placeholder_urls` and `result: fail`. | It is an expected output snapshot, not the registry input itself. |
| [`../valid/sync_no_change.expected.json`](../valid/sync_no_change.expected.json) | CONFIRMED | Related passing sync no-change snapshot. | It belongs to provenance sync behavior, not the failing provenance-check case. |
| [`../valid/sync_changed.expected.json`](../valid/sync_changed.expected.json) | CONFIRMED | Related passing sync changed snapshot. | It belongs to provenance sync behavior, not the failing provenance-check case. |
| `../../../../../../scripts/maintenance/check_doctrine_artifact_provenance.py` | CONFIRMED / NOT RUN | Checker parse rules, required fields, allowed statuses, placeholder URL handling, invalid URL handling, payload structure, and return-code behavior. | Script was not run during this update. |
| `../../../../../../tests/policy/test_doctrine_artifact_provenance.py` | CONFIRMED / NOT RUN | Policy test expects placeholder URLs to fail and produce `result: fail`. | Test was not run during this update. |
| `../../../../../../tests/policy/test_doctrine_artifact_provenance_snapshots.py` | CONFIRMED / NOT RUN | Snapshot test loads this invalid fixture and compares checker output keys. | Test was not run during this update. |
| `../../../../../../schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json` | CONFIRMED RELATED / NOT DIRECT AUTHORITY | Related `provenance_payload` shape includes `required_doctrine_artifact_provenance` fields. | Search did not find a directly named schema for this fixture family. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
