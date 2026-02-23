<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/9795ba1c-b246-401c-b9f9-25a8a0d799a1
title: Changelog
type: standard
version: v1
status: draft
owners: <team or names>
created: 2026-02-23
updated: 2026-02-23
policy_label: public
related:
  - <path or kfm:// ids>
tags: [kfm, changelog, releases]
notes:
  - This file records governed releases for the Kansas-Matrix-System.
  - Replace placeholders (owners/related links) during first release.
[/KFM_META_BLOCK_V2] -->

# Changelog

![status](https://img.shields.io/badge/status-draft-lightgrey)
![format](https://img.shields.io/badge/changelog-Keep_a_Changelog-blue)
![versioning](https://img.shields.io/badge/versioning-SemVer-brightgreen)
![governance](https://img.shields.io/badge/governance-KFM-orange)

Governed release notes for the Kansas-Matrix-System. Every entry must be traceable to evidence (PRs, commit SHAs, run receipts, QA reports, policy decisions) and must include rollback notes.

## Navigation

- [Unreleased](#unreleased)
- [Release process](#release-process)
- [Entry template](#entry-template)
- [Conventions](#conventions)
- [Glossary](#glossary)

## Conventions

### Formatting

This changelog follows the spirit of **Keep a Changelog**:
- **Added**: net-new features/capabilities
- **Changed**: modifications to existing behavior
- **Deprecated**: still available, but slated for removal
- **Removed**: removed features/paths/data
- **Fixed**: bug fixes
- **Security**: security/privacy hardening or incident-related work

### Versioning

Use **Semantic Versioning** (`MAJOR.MINOR.PATCH`):

- **MAJOR**: breaking changes (API contracts, data schemas, governance behavior) or irreversible data migrations without a supported downgrade
- **MINOR**: backwards-compatible features
- **PATCH**: backwards-compatible fixes and small improvements

### Evidence requirements

Every bullet must include an evidence trail.

| Change area | Minimum evidence | Include when relevant |
|---|---|---|
| Code / services | PR/commit SHA + CI run link | benchmarks, screenshots |
| Data promotion (Raw→Work→Processed→Published) | dataset ID(s) + run receipt + QA results | checksums, schema diff, license check |
| API contract | contract version + diff + compatibility note | migration guide, deprecation window |
| UI / Map / Story | route/component + screenshots | UX notes, accessibility checks |
| Focus Mode AI | prompt/config diff + evaluation notes | retrieval index/version changes |
| Governance / policy | policy doc diff + decision record | risk assessment, approval list |
| Security | issue ID + mitigation + verification | CVE refs, threat model updates |

> NOTE: If something is **Unknown**, write it down as **Unknown** and link the verification step you still need.

## Release process

### Release checklist

- [ ] Collect changes since last release (PRs merged, datasets promoted, policies updated)
- [ ] Confirm promotion gates pass (CI, QA, license/sensitivity checks)
- [ ] Confirm API compatibility or document breaking change + migration path
- [ ] Confirm rollback plan exists (code + data + config)
- [ ] Tag release (`vX.Y.Z`) and publish release notes
- [ ] Update this file and set `updated: YYYY-MM-DD` in the meta block

### Rollback expectations

Every release must include at least one rollback option:

- **Code rollback**: revert PR(s) or deploy previous tag
- **Config rollback**: restore prior config snapshots
- **Data rollback**: either revert promoted dataset version or pin consumers to last-known-good artifact
- **Policy rollback**: restore prior policy doc with an audit note explaining why

## Entry template

Copy/paste for each release:

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- [Area] <What changed> (Evidence: <PR/commit/run receipt>)

### Changed
- [Area] <What changed> (Evidence: <...>) (Upgrade notes: <...>)

### Deprecated
- [Area] <What is deprecated> (Evidence: <...>) (Removal target: vX.Y+1)

### Removed
- [Area] <What was removed> (Evidence: <...>) (Replacement: <...>)

### Fixed
- [Area] <What was fixed> (Evidence: <...>)

### Security
- [Area] <What was secured> (Evidence: <...>) (Verification: <...>)

### Breaking changes
- <If any, list explicitly. Include migration steps and rollback notes.>

### Rollback
- Code:
- Data:
- Config:
- Policy:
