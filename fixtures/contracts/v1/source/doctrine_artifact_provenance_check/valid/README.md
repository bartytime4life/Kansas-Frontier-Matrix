<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/contracts/v1/source/doctrine-artifact-provenance-check/valid/readme
title: doctrine_artifact_provenance_check valid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): doctrine steward; TODO(owner): source steward; TODO(owner): policy steward; TODO(owner): fixture steward; TODO(owner): maintenance steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-06-30 expansion
updated: 2026-06-30
policy_label: public-review
related:
  - sync_no_change.expected.json
  - sync_changed.expected.json
  - ../invalid/README.md
  - ../invalid/placeholder_urls.expected.json
  - ../../../../../../scripts/maintenance/check_doctrine_artifact_provenance.py
  - ../../../../../../scripts/maintenance/sync_doctrine_artifact_provenance_status.py
  - ../../../../../../tests/policy/test_doctrine_artifact_provenance.py
  - ../../../../../../tests/policy/test_doctrine_artifact_provenance_snapshots.py
  - ../../../../../../schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json
  - ../../../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, contracts, v1, source, doctrine-artifact-provenance-check, valid-fixtures, snapshot-fixtures, policy-tests, provenance, provenance-sync, source-admission, doctrine, maintenance, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/contracts/v1/source/doctrine_artifact_provenance_check/valid/README.md`."
  - "This fixture lane currently holds expected passing snapshot outputs for doctrine artifact provenance-status synchronization, not conventional `valid_*.json` JSON Schema fixtures."
  - "Current valid fixture coverage includes a no-change sync snapshot and a changed sync snapshot."
  - "The paired invalid lane documents the expected failing placeholder-source-url provenance check snapshot."
  - "No tests, validators, maintenance scripts, source admission workflows, provenance review workflows, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `doctrine_artifact_provenance_check` valid fixtures

Positive snapshot fixture lane for KFM doctrine artifact provenance-status synchronization.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Family: source" src="https://img.shields.io/badge/family-source-blue">
  <img alt="Check: doctrine_artifact_provenance" src="https://img.shields.io/badge/check-doctrine__artifact__provenance-purple">
  <img alt="Lane: valid" src="https://img.shields.io/badge/lane-valid-success">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/contracts/v1/source/doctrine_artifact_provenance_check/valid/README.md`  
**Fixture posture:** valid / passing snapshot fixture lane  
**Authority posture:** fixture only; synchronization behavior lives in `scripts/maintenance/sync_doctrine_artifact_provenance_status.py` and tests under `tests/policy/`  
**Quick links:** [Purpose](#purpose) · [Current inventory](#current-inventory) · [Sync-script basis](#sync-script-basis) · [Why these fixtures are valid](#why-these-fixtures-are-valid) · [Authority boundary](#authority-boundary) · [Test behavior](#test-behavior) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files in this directory are expected snapshot outputs for tests. They are not source registries, doctrine artifacts, provenance records, EvidenceBundles, release decisions, policy decisions, steward review proof, or publication authority.

---

## Purpose

This directory stores expected passing output snapshots for the doctrine artifact provenance-status synchronization helper.

Use this lane to prove that the sync helper emits bounded, deterministic result payloads for both no-change and changed cases. These fixtures protect KFM's source-admission boundary by making provenance-status synchronization reviewable without treating a fixture snapshot as source truth, steward signoff, provenance verification by itself, release approval, or publication authority.

This fixture lane is **not** currently shaped like the common `valid/valid_*.json` schema-fixture pattern. The confirmed files in this directory are snapshot-style expected JSON outputs used by policy tests.

---

## Current inventory

| File | Role | Expected result | Status |
|---|---|---|---|
| [`sync_no_change.expected.json`](sync_no_change.expected.json) | Expected payload when provenance sync finds no registry entries to change. | Snapshot comparison should pass. | CONFIRMED |
| [`sync_changed.expected.json`](sync_changed.expected.json) | Expected payload when provenance sync changes one registry entry and writes the update. | Snapshot comparison should pass. | CONFIRMED |

Current no-change snapshot:

```json
{
  "changed": [],
  "changed_count": 0,
  "check": "sync_doctrine_artifact_provenance_status",
  "result": "no_change",
  "write": false
}
```

Current changed snapshot:

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

Paired invalid snapshot fixture:

| File | Current role | Status |
|---|---|---|
| [`../invalid/placeholder_urls.expected.json`](../invalid/placeholder_urls.expected.json) | Expected failing provenance-check payload for placeholder source URLs. | CONFIRMED |

---

## Sync-script basis

The current synchronization-script evidence for this fixture lane is:

```text
scripts/maintenance/sync_doctrine_artifact_provenance_status.py
```

Confirmed sync-script facts:

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

The paired checker script handles unresolved or invalid provenance sources and produces a failure payload for invalid conditions. The valid snapshots here are sync-result snapshots, not proof that provenance URLs are verified, source rights are settled, or doctrine artifacts are release-approved.

---

## Why these fixtures are valid

The current valid snapshots match the bounded output shapes used by the policy snapshot tests:

| Snapshot | Why it is valid |
|---|---|
| `sync_no_change.expected.json` | It records no changed entries, `changed_count: 0`, `result: no_change`, and `write: false`. |
| `sync_changed.expected.json` | It records one changed filename, `changed_count: 1`, `result: changed`, and `write: true`. |

These fixtures are intentionally small. They prove expected output snapshots only. They do not prove that source URLs are verified, that registry entries are complete, that doctrine artifacts are current, that rights or sensitivity checks passed, or that any release gate was satisfied.

> [!WARNING]
> A passing provenance-sync snapshot is not source truth, not full provenance verification, not a steward review record, and not release or publication approval. It is an expected payload for a bounded maintenance helper.

---

## Authority boundary

| Responsibility | Home | Status in this check |
|---|---|---|
| Passing sync snapshot fixtures | `fixtures/contracts/v1/source/doctrine_artifact_provenance_check/valid/` | CONFIRMED |
| Failing provenance-check snapshot fixture | `fixtures/contracts/v1/source/doctrine_artifact_provenance_check/invalid/` | CONFIRMED |
| Provenance sync implementation | `scripts/maintenance/sync_doctrine_artifact_provenance_status.py` | CONFIRMED file content / NOT RUN |
| Provenance checker implementation | `scripts/maintenance/check_doctrine_artifact_provenance.py` | CONFIRMED file content from paired invalid-lane update / NOT RUN |
| Policy tests | `tests/policy/test_doctrine_artifact_provenance.py` and `tests/policy/test_doctrine_artifact_provenance_snapshots.py` | CONFIRMED file content / NOT RUN |
| Direct JSON Schema for this fixture family | `schemas/contracts/v1/source/doctrine_artifact_provenance_check.schema.json` | NOT FOUND BY SEARCH / NEEDS VERIFICATION |
| Related preflight summary schema | `schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json` | CONFIRMED related shape / NOT DIRECT AUTHORITY |

Do not collapse this fixture lane into the source registry, provenance registry, doctrine artifact descriptor, preflight summary, maintenance checker, sync script, policy test, EvidenceBundle, ReleaseManifest, source truth, review proof, or publication authority.

---

## Test behavior

The policy snapshot tests confirm two behaviors relevant to this valid fixture lane:

1. `sync_no_change.expected.json` is loaded and compared against the sync helper output when no changes are expected.
2. `sync_changed.expected.json` is loaded and compared against the sync helper output when a temporary registry and artifact trigger a write-mode status change.

Observed test path:

```text
tests/policy/test_doctrine_artifact_provenance_snapshots.py
```

This README documents expected fixture behavior only. It does not claim that pytest, CI, source admission policy, doctrine artifact provenance checks, provenance sync, registry admission, release checks, or the maintenance scripts were run during this update.

---

## Maintenance checklist

Before changing this valid fixture lane:

- [ ] Keep passing sync snapshots under `valid/` when they represent accepted sync-helper output shapes.
- [ ] Keep expected JSON snapshots stable enough for policy tests to compare deterministically.
- [ ] Update tests if snapshot keys or sync payload structure changes.
- [ ] Add additional valid snapshots for multi-file changed sets, write-disabled changed sets, and already-verified registry entries when coverage expands.
- [ ] Keep fixture examples public-safe and limited to metadata-shaped filenames, statuses, artifact paths, and check payloads.
- [ ] Avoid private, unpublished, source-system, prompt-like, or policy-restricted content.
- [ ] Do not embed full doctrine artifacts, raw evidence payloads, protected location detail, credentials, or release-blocked material in fixtures.
- [ ] Do not treat sync snapshots as verified source provenance or release approval.
- [ ] Run the relevant policy tests before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| No-change snapshot fixture | CONFIRMED | `sync_no_change.expected.json` exists and records `result: no_change`. |
| Changed snapshot fixture | CONFIRMED | `sync_changed.expected.json` exists and records `result: changed`. |
| Invalid lane | CONFIRMED | `../invalid/README.md` and `placeholder_urls.expected.json` document the failing placeholder-source-url case. |
| Sync script | CONFIRMED / NOT RUN | The script defines changed/no-change payloads and optional write behavior. |
| Policy tests | CONFIRMED / NOT RUN | Tests reference these valid snapshots and compare helper output. |
| Direct schema | NEEDS VERIFICATION | Prior search did not find a directly named schema for `doctrine_artifact_provenance_check`; the related preflight-summary schema includes provenance payload shape. |
| Test execution | NOT RUN | No validators, pytest, source policy checks, doctrine provenance checks, sync checks, registry checks, steward review checks, release checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define valid-fixture guidance. |
| [`sync_no_change.expected.json`](sync_no_change.expected.json) | CONFIRMED | Current no-change sync snapshot. | It is expected output, not proof the sync script was run during this update. |
| [`sync_changed.expected.json`](sync_changed.expected.json) | CONFIRMED | Current changed sync snapshot. | It is expected output, not proof the sync script was run during this update. |
| [`../invalid/README.md`](../invalid/README.md) | CONFIRMED | Paired invalid lane guidance for placeholder URL failure. | Does not prove tests were run. |
| [`../invalid/placeholder_urls.expected.json`](../invalid/placeholder_urls.expected.json) | CONFIRMED | Paired failing provenance-check snapshot. | It is an expected output snapshot, not the registry input itself. |
| `../../../../../../scripts/maintenance/sync_doctrine_artifact_provenance_status.py` | CONFIRMED / NOT RUN | Sync helper parse reuse, change trigger, payload structure, result vocabulary, write behavior, and return code. | Script was not run during this update. |
| `../../../../../../scripts/maintenance/check_doctrine_artifact_provenance.py` | CONFIRMED / NOT RUN | Paired provenance checker rules for invalid/placeholder source provenance. | Script was not run during this update. |
| `../../../../../../tests/policy/test_doctrine_artifact_provenance_snapshots.py` | CONFIRMED / NOT RUN | Snapshot tests load these valid fixtures and compare helper output. | Tests were not run during this update. |
| `../../../../../../schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json` | CONFIRMED RELATED / NOT DIRECT AUTHORITY | Related provenance payload shape includes provenance check fields. | Prior search did not find a directly named schema for this fixture family. |
| `../../../../../../docs/doctrine/directory-rules.md` | CONFIRMED doctrine | `fixtures/` is the root for golden, valid, and invalid test inputs; contracts/schemas/policy split remains separate. | Specific fixture completeness requires inventory and tests. |

[Back to top](#top)
