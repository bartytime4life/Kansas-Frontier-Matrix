# `release/manifests/people/` — People Release Manifests

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-manifests-blueviolet)
![domain](https://img.shields.io/badge/domain-people-purple)
![review](https://img.shields.io/badge/review-required-red)
![audit](https://img.shields.io/badge/audit-traceable-green)
![posture](https://img.shields.io/badge/default-fail--closed-red)

## Purpose

`release/manifests/people/` holds people-domain release manifest records when maintainers choose the plural manifest collection lane.

A people manifest names the release target, included records, validation support, evidence support, decision state, rights/privacy posture, and release-facing effect.

A manifest record should answer:

* What people-domain release or candidate is being described?
* Which artifacts, claims, catalog entries, triplet records, or release targets are included?
* Which evidence and validation records support the release?
* Which decision approved, held, corrected, or deferred the release?
* What rights, consent, attribution, privacy, or access review applies?
* What changelog, correction, or notice records are linked?
* What should governed release consumers treat as ready, held, superseded, or not ready?

A manifest is not the payload itself. It is the governed release record that points to approved release inputs and outputs.

## Status & authority

| Field              | Value                                                                                                                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Document type      | People release manifest README                                                                                                                                                                         |
| Owning root        | `release/`                                                                                                                                                                                             |
| Manifest lane      | `release/manifests/people/`                                                                                                                                                                            |
| Status             | Draft                                                                                                                                                                                                  |
| Authority level    | Manifest guidance. Actual manifest records, validation receipts, evidence records, decisions, changelog entries, correction records, privacy records, rights records, and schemas outrank this README. |
| Default posture    | Do not change release state from prose alone. Require governed manifest records, steward review, and policy/privacy review when people-domain exposure risk exists.                                    |
| Required reviewers | Release steward, people steward, data steward, docs steward, and policy/privacy reviewer.                                                                                                              |

## Path status

This README documents the requested path: `release/manifests/people/`.

Current-session evidence confirms this README existed as a blank file before this update. Current-session evidence also confirms `release/manifests/README.md` exists as a greenfield stub, while `release/manifest/README.md` is already documented as the singular manifest lane. Treat this people manifest sublane as draft until maintainers confirm whether the canonical manifest home is singular `release/manifest/`, plural `release/manifests/`, or both with distinct meanings.

## Repo fit

```text
release/
├── manifest/
├── manifests/
│   └── people/       # you are here
├── candidates/
│   └── people/
├── decisions/
├── changelog/
├── correction/
└── correction_notices/
```

This path belongs under the `release/` responsibility root because people-domain release manifests are release governance records. Release records are separate from data artifacts. Published payloads belong under `data/published/` only after release approval.

## People manifest responsibilities

| Responsibility         | Manifest expectation                                                                                                             |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Identity               | Provide a stable people-domain release or manifest ID.                                                                           |
| Scope                  | State the people dataset, family, population-summary, settlement-context, biographical-summary, land-context, or release target. |
| Inclusion              | List included people-domain release records or artifacts by pointer.                                                             |
| Evidence               | Link evidence records when people-domain claims depend on evidence.                                                              |
| Validation             | Link validation receipts or checks.                                                                                              |
| Rights/privacy posture | State whether rights, consent, attribution, privacy, or access review is complete, held, restricted, or not ready.               |
| Decision               | Link the steward decision that supports the release state.                                                                       |
| Changelog              | Link the release-history entry.                                                                                                  |
| Correction path        | Link correction records when the manifest is corrected, superseded, or held.                                                     |
| Client posture         | State what governed surfaces may use this release.                                                                               |

## What belongs here

* People-domain release manifest records.
* People manifest readiness checklists.
* People manifest review summaries.
* Links to people candidates, decisions, validation receipts, evidence records, rights/privacy reviews, changelog entries, corrections, and notices.
* Notes explaining people manifest state, included release targets, release scope, rights/privacy posture, and follow-up tasks.

## What does not belong here

* Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
* Bulk datasets, person-level exports, identity payloads, API payloads, or map-ready artifacts.
* Living-person records, private family records, or direct identity payloads.
* Source descriptors, schemas, contracts, policy files, or validator code.
* Generated summaries used as sovereign truth.
* Unreviewed people-domain claims presented as approved release state.

## Required manifest fields

* Manifest ID
* Manifest status
* People-domain release or candidate pointer
* People domain scope
* Artifact or release target pointers
* Included claim or record pointers, when applicable
* Evidence pointer, when applicable
* Validation pointer, when applicable
* Rights or privacy review pointer, when applicable
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

## Minimal people manifest record

```markdown
# <manifest-id>

## Status

DRAFT / READY_FOR_REVIEW / APPROVED / RELEASED / HELD / SUPERSEDED / CORRECTED / NO_ACTION

## People release or candidate

<release ID, candidate path, or N/A>

## People scope

<dataset, family, population-summary, settlement-context, biographical-summary, land-context, artifact family, or release target>

## Included records

- <artifact, claim, catalog, triplet, or release-target pointer>

## Rights and privacy posture

PUBLIC / GENERALIZED / REDACTED / RESTRICTED / HELD / NOT_READY

## Governed support pointers

- Evidence: <path or N/A>
- Validation: <path or N/A>
- Rights review: <path or N/A>
- Privacy review: <path or N/A>
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
* [ ] People-domain release or candidate pointer is present.
* [ ] Included records are listed by pointer.
* [ ] Evidence support is linked when release claims depend on evidence.
* [ ] Validation support is linked when validation is required.
* [ ] Rights, consent, attribution, privacy, or access review is linked when people-domain exposure risk exists.
* [ ] Steward decision is linked.
* [ ] Changelog entry is linked when release history changes.
* [ ] Correction or notice pointers are linked when applicable.
* [ ] Client-consumption posture is explicit.
* [ ] Living-person, private family, or direct identity payload detail is absent, generalized, redacted, restricted, or held as required.
* [ ] No data payloads are stored in this lane.

## Naming guidance

Recommended pattern:

```text
<YYYY-MM-DD>_<people-scope>_manifest.md
```

Examples:

```text
2026-07-03_people-population-summary_manifest.md
2026-07-03_people-settlement-context_manifest.md
2026-07-03_people-biographical-summary_manifest.md
```

## Open verification

* [ ] Expand `release/manifests/README.md` so this people lane inherits from a complete plural manifest parent contract.
* [ ] Confirm whether the canonical manifest home is `release/manifest/`, `release/manifests/`, or both.
* [ ] Confirm CODEOWNERS for `release/manifests/people/`.
* [ ] Confirm people manifest ID format.
* [ ] Confirm people manifest filename convention.
* [ ] Confirm manifest schema location.
* [ ] Confirm evidence pointer format.
* [ ] Confirm validation receipt pointer format.
* [ ] Confirm rights, consent, attribution, privacy, and access review pointer formats.
* [ ] Confirm decision, changelog, correction, and notice pointer formats.
* [ ] Confirm whether people manifest records require schema validation before release approval.

## Last reviewed

| Field               | Value                                                                                                                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Last reviewed       | 2026-07-03                                                                                                                                                                           |
| Review status       | Draft README content prepared; connector blocked commit                                                                                                                              |
| Next review trigger | First people manifest record, plural manifest-lane expansion, manifest schema update, candidate promotion, release decision, privacy review, rights review, or changelog integration |

