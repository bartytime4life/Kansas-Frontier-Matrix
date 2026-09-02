# `release/manifests/roads-rail-trade/` — Roads Rail Trade Release Manifests

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-manifests-blueviolet)
![domain](https://img.shields.io/badge/domain-roads--rail--trade-slategray)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)

## Purpose

`release/manifests/roads-rail-trade/` holds release manifest records for the roads-rail-trade domain when maintainers choose the plural manifest collection lane.

A manifest record names the release target, included records, validation support, evidence support, decision state, time context, and release-facing effect.

A manifest is not the payload itself. It is the governed release record that points to approved release inputs and outputs.

## Status & authority

| Field              | Value                                                                                                                                                                 |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Document type      | Roads rail trade release manifest README                                                                                                                              |
| Owning root        | `release/`                                                                                                                                                            |
| Manifest lane      | `release/manifests/roads-rail-trade/`                                                                                                                                 |
| Status             | Draft                                                                                                                                                                 |
| Authority level    | Manifest guidance. Actual manifest records, validation receipts, evidence records, decisions, changelog entries, correction records, and schemas outrank this README. |
| Default posture    | Do not change release state from prose alone. Require governed manifest records and steward review.                                                                   |
| Required reviewers | Release steward, roads-rail-trade steward, data steward, and docs steward.                                                                                            |

## Path status

This README documents the requested path: `release/manifests/roads-rail-trade/`.

Current-session evidence confirms this README existed as a blank file before this update. Current-session evidence also confirms `release/manifests/README.md` exists as a greenfield stub, while `release/manifest/README.md` is already documented as the singular manifest lane. Treat this sublane as draft until maintainers confirm whether the canonical manifest home is singular `release/manifest/`, plural `release/manifests/`, or both with distinct meanings.

## Repo fit

```text
release/
├── manifest/
├── manifests/
│   └── roads-rail-trade/       # you are here
├── candidates/
│   └── roads-rail-trade/
├── decisions/
├── changelog/
├── correction/
└── correction_notices/
```

Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

## Manifest responsibilities

| Responsibility  | Manifest expectation                                                                    |
| --------------- | --------------------------------------------------------------------------------------- |
| Identity        | Provide a stable release or manifest ID.                                                |
| Scope           | State the domain family, summary family, network family, time slice, or release target. |
| Inclusion       | List included release records or artifacts by pointer.                                  |
| Evidence        | Link evidence records when claims depend on evidence.                                   |
| Validation      | Link validation receipts or checks.                                                     |
| Time context    | State time range, temporal confidence, or version context when relevant.                |
| Decision        | Link the steward decision that supports the release state.                              |
| Changelog       | Link the release-history entry.                                                         |
| Correction path | Link correction records when the manifest is corrected, superseded, or held.            |
| Client posture  | State what governed surfaces may use this release.                                      |

## What belongs here

* Roads-rail-trade release manifest records.
* Manifest readiness checklists.
* Manifest review summaries.
* Links to candidates, decisions, validation receipts, evidence records, changelog entries, corrections, and notices.
* Notes explaining manifest state, included release targets, release scope, time context, and follow-up tasks.

## What does not belong here

* Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
* Bulk datasets, exports, service payloads, or map-ready artifacts.
* Source descriptors, schemas, contracts, policy files, or validator code.
* Generated summaries used as sovereign truth.
* Unreviewed claims presented as approved release state.

## Required manifest fields

* Manifest ID
* Manifest status
* Release or candidate pointer
* Domain scope
* Artifact or release target pointers
* Included claim or record pointers, when applicable
* Evidence pointer, when applicable
* Validation pointer, when applicable
* Time context, when applicable
* Decision pointer
* Changelog pointer
* Correction pointer, when applicable
* Notice pointer, when applicable
* Release-facing effect
* Client-consumption posture
* Date recorded
* Recorded by
* Steward review state
* Follow-up items

## Minimal manifest record

```markdown
# <manifest-id>

## Status

DRAFT / READY_FOR_REVIEW / APPROVED / RELEASED / HELD / SUPERSEDED / CORRECTED / NO_ACTION

## Release or candidate

<release ID, candidate path, or N/A>

## Domain scope

<domain family, summary family, network family, time slice, artifact family, or release target>

## Included records

- <artifact, claim, catalog, triplet, or release-target pointer>

## Time context

<time range, version context, temporal confidence, or N/A>

## Governed support pointers

- Evidence: <path or N/A>
- Validation: <path or N/A>
- Decision: <path or N/A>
- Changelog: <path or N/A>
- Correction: <path or N/A>
- Notice: <path or N/A>

## Release-facing effect

<none / ready / released / held / superseded / corrected / review pending>

## Client posture

<which governed release surfaces may use this release, or N/A>

## Date recorded

<YYYY-MM-DD>

## Recorded by

<steward or maintainer>

## Review state

<reviewers, decision, and date>

## Follow-up

<open items or none>
```

## Review checklist

* [ ] Manifest ID is stable.
* [ ] Release or candidate pointer is present.
* [ ] Included records are listed by pointer.
* [ ] Evidence support is linked when release claims depend on evidence.
* [ ] Validation support is linked when validation is required.
* [ ] Time context is stated when relevant.
* [ ] Steward decision is linked.
* [ ] Changelog entry is linked when release history changes.
* [ ] Correction or notice pointers are linked when applicable.
* [ ] Client-consumption posture is explicit.
* [ ] No data payloads are stored in this lane.

## Naming guidance

Recommended pattern:

```text
<YYYY-MM-DD>_<domain-scope>_manifest.md
```

Examples:

```text
2026-07-03_roads-rail-trade-summary_manifest.md
2026-07-03_roads-rail-trade-network_manifest.md
2026-07-03_roads-rail-trade-context_manifest.md
```

## Open verification

* [ ] Expand `release/manifests/README.md` so this lane inherits from a complete plural manifest parent contract.
* [ ] Confirm whether the canonical manifest home is `release/manifest/`, `release/manifests/`, or both.
* [ ] Confirm CODEOWNERS for `release/manifests/roads-rail-trade/`.
* [ ] Confirm manifest ID format.
* [ ] Confirm manifest filename convention.
* [ ] Confirm manifest schema location.
* [ ] Confirm evidence pointer format.
* [ ] Confirm validation receipt pointer format.
* [ ] Confirm decision, changelog, correction, and notice pointer formats.
* [ ] Confirm whether manifest records require schema validation before release approval.

## Last reviewed

| Field               | Value                                                                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Last reviewed       | 2026-07-03                                                                                                                                     |
| Review status       | Draft README content prepared; connector blocked commit                                                                                        |
| Next review trigger | First manifest record, plural manifest-lane expansion, manifest schema update, candidate promotion, release decision, or changelog integration |

