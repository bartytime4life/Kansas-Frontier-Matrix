<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/source/doctrine-artifact-provenance-check/readme
title: doctrine_artifact_provenance_check fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): doctrine steward; TODO(owner): source steward; TODO(owner): policy steward; TODO(owner): fixture steward; TODO(owner): maintenance steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - valid/README.md
  - valid/sync_no_change.expected.json
  - valid/sync_changed.expected.json
  - invalid/README.md
  - invalid/placeholder_urls.expected.json
  - ../../../../../scripts/maintenance/check_doctrine_artifact_provenance.py
  - ../../../../../scripts/maintenance/sync_doctrine_artifact_provenance_status.py
  - ../../../../../tests/policy/test_doctrine_artifact_provenance.py
  - ../../../../../tests/policy/test_doctrine_artifact_provenance_snapshots.py
  - ../../../../../schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json
  - ../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, source, doctrine-artifact-provenance-check, valid-fixtures, invalid-fixtures, snapshot-fixtures, policy-tests, provenance, provenance-sync, source-admission, doctrine, maintenance, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/source/doctrine_artifact_provenance_check/README.md`."
  - "This directory currently holds snapshot-style expected JSON outputs for doctrine artifact provenance maintenance tests, not conventional schema fixtures."
  - "Current invalid coverage is one placeholder-source-url failing snapshot."
  - "Current valid coverage is two provenance-status sync snapshots: no-change and changed."
  - "No tests, validators, maintenance scripts, source admission workflows, provenance review workflows, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `doctrine_artifact_provenance_check` fixtures

Snapshot fixture family for KFM doctrine artifact provenance maintenance checks.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: source" src="https://img.shields.io/badge/family-source-blue">
  <img alt="Style: snapshots" src="https://img.shields.io/badge/style-snapshot__fixtures-informational">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/source/doctrine_artifact_provenance_check/README.md`  
**Fixture posture:** expected JSON snapshot fixture family  
**Authority posture:** fixture only; checker and sync behavior live in `scripts/maintenance/` and policy tests under `tests/policy/`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Script basis](#script-basis) · [Authority boundary](#authority-boundary) · [Test behavior](#test-behavior) · [Schema and contract status](#schema-and-contract-status) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected test snapshots. They are not source registries, doctrine artifacts, provenance records, EvidenceBundles, release manifests, policy decisions, steward review proof, release approval, or publication authority.

---

## Purpose

This directory groups snapshot-style expected JSON outputs for doctrine artifact provenance maintenance behavior.

The fixture family currently covers two related maintenance surfaces:

1. **Provenance check failure** — unresolved or placeholder doctrine artifact source URLs produce a failing payload.
2. **Provenance status synchronization** — artifact presence can produce deterministic no-change or changed sync payloads.

A passing snapshot comparison proves expected output shape for a test case only. It does not prove source URLs are verified, source rights are settled, doctrine artifacts are current, review passed, release gates passed, or publication is authorized.

---

## Current inventory

| Lane | File | Current role | Status |
|---|---|---|---|
| [`invalid/`](invalid/README.md) | [`placeholder_urls.expected.json`](invalid/placeholder_urls.expected.json) | Expected failing provenance-check payload for placeholder source URLs. | CONFIRMED |
| [`valid/`](valid/README.md) | [`sync_no_change.expected.json`](valid/sync_no_change.expected.json) | Expected no-change provenance-sync payload. | CONFIRMED |
| [`valid/`](valid/README.md) | [`sync_changed.expected.json`](valid/sync_changed.expected.json) | Expected changed provenance-sync payload. | CONFIRMED |

### Invalid snapshot

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

### Valid snapshots

No-change sync snapshot:

```json
{
  "changed": [],
  "changed_count": 0,
  "check": "sync_doctrine_artifact_provenance_status",
  "result": "no_change",
  "write": false
}
```

Changed sync snapshot:

```json
{
  "changed": [
    "a.pdf"
  ],
  "changed_count": 1,
  "check": "sync_doctrine_artifact_provenance_status",
  "result": "changed",
  "write": true
}
```

---

## Script basis

### Provenance checker

The checker script is:

```text
scripts/maintenance/check_doctrine_artifact_provenance.py
```

Confirmed checker behavior:

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

### Provenance status sync

The sync script is:

```text
scripts/maintenance/sync_doctrine_artifact_provenance_status.py
```

Confirmed sync behavior:

| Item | Value |
|---|---|
| Check name | `sync_doctrine_artifact_provenance_status` |
| Default registry input | `control_plane/doctrine_artifact_provenance_sources.yaml` |
| Default artifacts directory | `docs/doctrine/artifacts` |
| Registry parser | Reuses `parse_entries` from `check_doctrine_artifact_provenance.py` |
| Change trigger | Artifact file exists and entry status is not `verified` |
| Change behavior | Set `status: verified` and add `verified_at` timestamp |
| Payload fields | `check`, `registry`, `artifacts_dir`, `changed`, `changed_count`, `result`, `write` |
| No-change result | `result: no_change`, `changed_count: 0`, `changed: []` |
| Changed result | `result: changed`, `changed_count` equals changed list length |
| Write behavior | If `--write` and changed entries exist, rewrite the registry |
| Return code | `0` |

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Snapshot fixture family | `fixtures/contracts/v1/source/doctrine_artifact_provenance_check/` | CONFIRMED |
| Failing provenance-check snapshot | `fixtures/contracts/v1/source/doctrine_artifact_provenance_check/invalid/` | CONFIRMED |
| Passing provenance-sync snapshots | `fixtures/contracts/v1/source/doctrine_artifact_provenance_check/valid/` | CONFIRMED |
| Provenance checker implementation | `scripts/maintenance/check_doctrine_artifact_provenance.py` | CONFIRMED file content / NOT RUN |
| Provenance sync implementation | `scripts/maintenance/sync_doctrine_artifact_provenance_status.py` | CONFIRMED file content / NOT RUN |
| Policy tests | `tests/policy/test_doctrine_artifact_provenance.py` and `tests/policy/test_doctrine_artifact_provenance_snapshots.py` | CONFIRMED file content / NOT RUN |
| Direct JSON Schema for this fixture family | `schemas/contracts/v1/source/doctrine_artifact_provenance_check.schema.json` | NOT FOUND BY SEARCH / NEEDS VERIFICATION |
| Semantic contract for this exact fixture family | `contracts/source/doctrine_artifact_provenance_check.md` | NOT VERIFIED / NEEDS VERIFICATION |
| Related preflight summary schema | `schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json` | CONFIRMED related shape / NOT DIRECT AUTHORITY |

Do not collapse this fixture family into the source registry, provenance registry, doctrine artifact descriptor, preflight summary, maintenance checker, sync script, policy test, EvidenceBundle, ReleaseManifest, source truth, review proof, or publication authority.

---

## Test behavior

The policy tests confirm three behaviors relevant to this fixture family:

1. The provenance checker is expected to fail with return code `1` when placeholder URLs remain.
2. The invalid snapshot test loads `invalid/placeholder_urls.expected.json` and compares selected keys from checker output.
3. The valid snapshot tests load `valid/sync_no_change.expected.json` and `valid/sync_changed.expected.json` and compare selected keys from sync output.

Observed test paths:

```text
tests/policy/test_doctrine_artifact_provenance.py
tests/policy/test_doctrine_artifact_provenance_snapshots.py
```

This README documents expected fixture behavior only. It does not claim that pytest, CI, source admission policy, doctrine artifact provenance checks, provenance sync, registry admission, release checks, or maintenance scripts were run during this update.

---

## Schema and contract status

This fixture family currently behaves more like a policy-test snapshot family than a conventional JSON Schema fixture family.

| Item | Status | Notes |
|---|---:|---|
| Direct schema | NEEDS VERIFICATION | Repository search did not find a directly named `doctrine_artifact_provenance_check` schema during this documentation sequence. |
| Related schema | CONFIRMED RELATED | `doctrine_artifact_preflight_summary.schema.json` contains a `provenance_payload` shape with `check`, `result`, `invalid_urls`, `placeholder_urls`, `invalid_status`, and `missing_fields`. |
| Common schema harness fit | NEEDS VERIFICATION | This family does not currently use the common `valid/valid_*.json` and `invalid/invalid_*.json` fixture naming pattern. |
| Semantic contract | NEEDS VERIFICATION | A directly named semantic contract was not verified during this update. |

---

## Maintenance checklist

Before changing this fixture family:

- [ ] Keep expected JSON snapshots deterministic and small.
- [ ] Keep failing provenance-check snapshots under `invalid/`.
- [ ] Keep passing provenance-sync snapshots under `valid/`.
- [ ] Update policy tests when snapshot keys or script payload structure changes.
- [ ] Add invalid snapshots for invalid URL, invalid status, missing field, and missing registry block cases when coverage expands.
- [ ] Add valid snapshots for multi-file changed sets, write-disabled changed sets, and already-verified registry entries when coverage expands.
- [ ] Keep fixture examples public-safe and limited to metadata-shaped filenames, statuses, artifact paths, URLs, and check payloads.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not treat placeholder URLs, sync snapshots, or fixture outputs as verified source provenance or release approval.
- [ ] Run the relevant policy tests before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Invalid lane | CONFIRMED | `invalid/README.md` and `placeholder_urls.expected.json` document the failing placeholder-source-url case. |
| Valid lane | CONFIRMED | `valid/README.md`, `sync_no_change.expected.json`, and `sync_changed.expected.json` document passing sync snapshots. |
| Checker script | CONFIRMED / NOT RUN | The checker defines placeholder URL handling, invalid URL handling, missing field handling, invalid status handling, payload output, and return-code behavior. |
| Sync script | CONFIRMED / NOT RUN | The sync helper defines changed/no-change payloads and optional write behavior. |
| Policy tests | CONFIRMED / NOT RUN | Tests reference both invalid and valid snapshots. |
| Direct schema | NEEDS VERIFICATION | A directly named schema for this fixture family was not found in the repository searches used in this documentation sequence. |
| Test execution | NOT RUN | No validators, pytest, source policy checks, doctrine provenance checks, sync checks, registry checks, steward review checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture-family guidance. |
| [`invalid/README.md`](invalid/README.md) | CONFIRMED | Paired invalid lane guidance. | Does not prove tests were run. |
| [`invalid/placeholder_urls.expected.json`](invalid/placeholder_urls.expected.json) | CONFIRMED | Current failing provenance-check snapshot. | It is expected output, not the registry input itself. |
| [`valid/README.md`](valid/README.md) | CONFIRMED | Paired valid lane guidance. | Does not prove tests were run. |
| [`valid/sync_no_change.expected.json`](valid/sync_no_change.expected.json) | CONFIRMED | Current no-change sync snapshot. | It is expected output, not proof the sync script was run during this update. |
| [`valid/sync_changed.expected.json`](valid/sync_changed.expected.json) | CONFIRMED | Current changed sync snapshot. | It is expected output, not proof the sync script was run during this update. |
| `../../../../../scripts/maintenance/check_doctrine_artifact_provenance.py` | CONFIRMED / NOT RUN | Checker parse rules, required fields, allowed statuses, placeholder URL handling, invalid URL handling, payload structure, and return-code behavior. | Script was not run during this update. |
| `../../../../../scripts/maintenance/sync_doctrine_artifact_provenance_status.py` | CONFIRMED / NOT RUN | Sync helper parse reuse, change trigger, payload structure, result vocabulary, write behavior, and return code. | Script was not run during this update. |
| `../../../../../tests/policy/test_doctrine_artifact_provenance.py` | CONFIRMED / NOT RUN | Policy test expects placeholder URLs to fail and produce `result: fail`. | Test was not run during this update. |
| `../../../../../tests/policy/test_doctrine_artifact_provenance_snapshots.py` | CONFIRMED / NOT RUN | Snapshot tests load invalid and valid fixtures and compare script output. | Tests were not run during this update. |
| `../../../../../schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json` | CONFIRMED RELATED / NOT DIRECT AUTHORITY | Related `provenance_payload` shape includes provenance check fields. | Search did not find a directly named schema for this fixture family. |
| `../../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
