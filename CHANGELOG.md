<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/9795ba1c-b246-401c-b9f9-25a8a0d799a1
title: Changelog
type: standard
version: v2
status: draft
owners: kfm-release-stewards (TBD); kfm-engineering; kfm-governance
created: 2026-02-23
updated: 2026-02-27
policy_label: public
related:
  - ./README.md
  - ./.github/README.md
  - ./SECURITY.md
  - ./CONTRIBUTING.md
  - kfm://doc/kfm-gdg-vnext-2026-02-20
tags: [kfm, changelog, releases, governance]
notes:
  - Public changelog: must not leak restricted dataset existence, sensitive locations, PII, or private operational details.
  - Every entry must be traceable to evidence (PRs/commits, run receipts, QA summaries, policy decisions, audit refs).
  - Data “releases” are recorded as DatasetVersion promotions; software releases use SemVer.
  - Replace TBD owners/links during first real release.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Changelog

![status](https://img.shields.io/badge/status-draft-lightgrey)
![format](https://img.shields.io/badge/changelog-Keep_a_Changelog-blue)
![versioning](https://img.shields.io/badge/versioning-SemVer%20%2B%20DatasetVersion-brightgreen)
![governance](https://img.shields.io/badge/governance-KFM-orange)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![policy](https://img.shields.io/badge/policy-public-lightgrey)

Governed release notes for **Kansas Frontier Matrix (KFM)**.  
Every user-facing change MUST be traceable to evidence and MUST include rollback notes. If something cannot be evidenced, it belongs in **Discover Mode** or as **UNKNOWN** with explicit verification steps.

---

## Navigation

- [Unreleased](#unreleased)
- [How to use this changelog](#how-to-use-this-changelog)
- [Disclosure policy](#disclosure-policy)
- [Release types](#release-types)
- [Evidence requirements](#evidence-requirements)
- [Release process](#release-process)
- [Entry template](#entry-template)
- [Conventions](#conventions)
- [Glossary](#glossary)

[Back to top](#top)

---

## Unreleased

### Added
- _(none yet)_

### Changed
- _(none yet)_

### Fixed
- _(none yet)_

### Security
- _(none yet)_

> [!NOTE]
> Keep Unreleased small. If it grows beyond a few screens, cut a release.

[Back to top](#top)

---

## How to use this changelog

KFM tracks **two kinds of versioning at once**:

1. **Software releases (SemVer)** — `vMAJOR.MINOR.PATCH`  
   Used for API/UI/workers/libraries/contracts toolchains.

2. **Dataset promotions (DatasetVersion)** — immutable, digest-addressed versions  
   Used for promoted outputs served by the governed API (and therefore visible in map/story/focus experiences).

This changelog records both, but **never confuses them**.

> [!IMPORTANT]
> If a change affects what users can see/query/export, it is a **governed change** and MUST include:
> - policy impact (labels/obligations)
> - evidence trail (receipts/manifests)
> - rollback option (code/config/data/policy)

[Back to top](#top)

---

## Disclosure policy

This file has `policy_label: public`. That means:

### What MUST NOT appear here
- names/identifiers that reveal existence of restricted datasets (unless governance explicitly allows)
- precise sensitive coordinates or geometries
- PII or reidentification-relevant details
- secrets, tokens, internal endpoints, or operational credentials
- exploit details prior to coordinated disclosure

### How to record restricted work safely
- Use **policy-safe references** such as:
  - `kfm://audit/entry/<id>`
  - `kfm://run/<id>`
  - “Restricted dataset promotion (details withheld; see restricted release log)”
- If you maintain a restricted changelog, link to it only through policy-safe mechanisms (do not post direct URLs if they are access-controlled).

> [!PROPOSED]
> Add a restricted counterpart (access controlled):
> - `docs/governance/CHANGELOG.restricted.md` (policy_label: restricted)

[Back to top](#top)

---

## Release types

KFM releases are multi-surface. Each entry SHOULD declare which types it includes:

- **Software release (SemVer):** API/UI/workers, tools, schema validators, contracts packaging.
- **Data release (promotion):** Raw→Processed→Catalog→Published promotion of DatasetVersions.
- **Policy release:** policy-as-code changes (default-deny rules, obligations, export controls).
- **Contracts release:** OpenAPI/schema/profile/vocab changes that affect validation and runtime boundaries.
- **Infrastructure release:** deployment posture, secrets handling, observability (without disclosing sensitive specifics).
- **Security release:** mitigations, patches, and hardening (policy-safe disclosure).

> [!TIP]
> A single SemVer software release may include multiple data promotions, but the evidence must be separated cleanly.

[Back to top](#top)

---

## Evidence requirements

Every bullet MUST include an evidence trail. Use this standardized notation:

- **PR/commit:** `PR #123` and/or `commit <sha>`
- **Receipts/manifests:** `kfm://run/...`, `promotion_manifest sha256:...`, `artifact_manifest sha256:...`
- **Policy decisions:** `kfm://policy_decision/...` (or equivalent) + obligations summary
- **Audit:** `kfm://audit/entry/...`
- **Validation:** `qa_summary sha256:...`, `catalog_validation sha256:...`, `linkcheck sha256:...`

### Minimum evidence by change area

| Change area | Minimum evidence | Include when relevant |
|---|---|---|
| Code / services | PR/commit + CI run reference | benchmarks, screenshots |
| Data promotion | dataset slug(s) **or** policy-safe placeholder + run receipt + QA summary | checksums, schema diff, license/terms snapshot |
| API contract | contract version + diff + compatibility note | migration guide, deprecation window |
| UI / Map / Story | route/component + screenshots (policy-safe) | accessibility checks, UX notes |
| Focus Mode AI | config/prompt version + evaluation summary | retrieval index/version changes |
| Governance / policy | policy diff + decision record | risk assessment, approval list |
| Security | issue/advisory ID + mitigation + verification | threat model updates |

> [!NOTE]
> If something is **UNKNOWN**, write it as **UNKNOWN** and link the verification step required.

[Back to top](#top)

---

## Release process

### Release checklist (fail-closed)

- [ ] Collect changes since last release (PRs merged, DatasetVersions promoted, policies/contracts updated)
- [ ] Confirm required checks passed (see `.github/README.md` required checks registry, if present)
- [ ] Confirm Promotion Contract gates are satisfied for any data that becomes user-visible
- [ ] Confirm API compatibility or document breaking changes + migration path
- [ ] Confirm rollback plan exists (code + data + config + policy)
- [ ] Tag release (`vX.Y.Z`) and publish release notes
- [ ] Update this file and bump MetaBlock `updated: YYYY-MM-DD`

### Rollback expectations

Every release MUST include at least one rollback option:

- **Code rollback:** revert PR(s) or deploy previous tag
- **Config rollback:** restore prior config snapshots (and record the audit reference)
- **Data rollback:** pin consumers to last-known-good DatasetVersion; rebuild projections from canonical artifacts
- **Policy rollback:** restore prior policy bundle (with audit note explaining why)

> [!IMPORTANT]
> Rollback should not require deleting canonical artifacts. Prefer pinning/promotion discipline over destructive edits.

[Back to top](#top)

---

## Entry template

Copy/paste for each release.

```markdown
## [X.Y.Z] - YYYY-MM-DD

**Release type(s):** software | data | policy | contracts | infra | security  
**Audit:** kfm://audit/entry/<id>  
**Release receipt (optional):** kfm://run/<id>  
**Owners/approvers:** <teams/roles>  
**Compatibility:** <backwards-compatible | breaking> (Details below)

### Added
- [Area] <What changed> (Evidence: <PR/commit/run_receipt/audit_ref>)

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

### Data promotions (policy-safe)
- Public datasets promoted:
  - <dataset_slug>@<dataset_version_id> (Receipt: kfm://run/...; QA: sha256:...; Catalog validation: sha256:...)
- Restricted datasets promoted:
  - <withheld> (Evidence: kfm://audit/entry/...; Details: withheld in public changelog)

### Contracts and schemas
- [Contracts] <What changed> (Evidence: <commit/pr>) (Compatibility: <...>)

### Policy changes
- [Policy] <What changed> (Evidence: <commit/pr/policy_decision>) (Obligations: <summary>)

### Breaking changes
- <List explicitly. Include migration steps and rollback notes.>

### Rollback
- Code: <how to revert software changes>
- Data: <pin to prior DatasetVersion(s) + rebuild projections>
- Config: <restore prior config snapshot>
- Policy: <restore prior policy bundle + audit note>
```

[Back to top](#top)

---

## Conventions

### Formatting

This changelog follows the spirit of **Keep a Changelog**:
- **Added**: net-new features/capabilities
- **Changed**: modifications to existing behavior
- **Deprecated**: still available, but slated for removal
- **Removed**: removed features/paths/data
- **Fixed**: bug fixes
- **Security**: security/privacy hardening or incident-related work

> [!TIP]
> Prefer short, scannable bullets that point to evidence. Put the detail in PRs, receipts, and reports.

### Versioning (SemVer)

Use **Semantic Versioning** (`MAJOR.MINOR.PATCH`):

- **MAJOR**: breaking changes (API contracts, schemas, governance behavior) or irreversible data migrations without a supported downgrade
- **MINOR**: backwards-compatible features
- **PATCH**: backwards-compatible fixes and improvements

### Dates

Use ISO dates: `YYYY-MM-DD`.

[Back to top](#top)

---

## Glossary

- **DatasetVersion:** immutable promoted dataset output version (digest-addressed; policy-labeled)
- **spec_hash:** deterministic hash derived from canonical dataset spec used to anchor identity
- **Run receipt:** immutable record of pipeline/index/story/focus runs, including inputs/outputs with digests
- **Promotion manifest:** record of a promotion event (approvals, artifacts, catalogs, validation, policy)
- **Audit ledger / audit_ref:** append-only record of governed actions; references should be policy-safe
- **EvidenceRef / EvidenceBundle:** citation reference that must resolve deterministically to policy-evaluated evidence

[Back to top](#top)
