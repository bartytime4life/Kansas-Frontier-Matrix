<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-agriculture-readme
title: release/agriculture/ — Agriculture Release Governance, Promotion Records, and Correction/Rollback Control
type: per-domain-release-readme
version: v1
status: draft
owners:
  - <agriculture-domain-steward>
  - <release-steward>
  - <policy-sensitivity-reviewer>
  - <data-steward>
created: 2026-07-03
updated: 2026-07-03
policy_label: public
related:
  - release/README.md
  - release/manifests/
  - release/candidates/
  - release/corrections/
  - release/rollbacks/
  - data/published/agriculture/
  - data/processed/agriculture/
  - data/catalog/
  - data/registry/sources/agriculture/
  - docs/domains/agriculture/
  - packages/domains/agriculture/
  - schemas/contracts/v1/
  - contracts/
  - policy/
  - docs/architecture/release-discipline.md
  - docs/doctrine/directory-rules.md
  - docs/runbooks/
tags:
  - kfm
  - release
  - agriculture
  - promotion
  - release-manifest
  - correction
  - rollback
  - provenance
  - sensitivity
  - auditability
notes:
  - "This directory is for agriculture release governance records. It is not a storage location for published artifacts, raw source data, processed datasets, schemas, policy rules, or source registry records."
  - "Agriculture releases must resolve evidence, rights, sensitivity, policy, validation, review state, release state, correction path, and rollback path before public or semi-public exposure."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `release/agriculture/` — Agriculture Release Governance, Promotion Records, and Correction/Rollback Control

> **One-line purpose.** Hold agriculture-domain release governance records so KFM agriculture outputs become public only through reviewed, evidence-backed, policy-safe, rollback-addressable release transitions.

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![domain](https://img.shields.io/badge/domain-agriculture-green)
![promotion](https://img.shields.io/badge/promotion-governed_transition-success)
![rollback](https://img.shields.io/badge/rollback-required-red)
![artifacts](https://img.shields.io/badge/artifacts-live_in_data%2Fpublished-orange)

---

## Quick jump

[Purpose](#purpose) · [Status & authority](#status--authority) · [Repo fit](#repo-fit) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Agriculture release contract](#agriculture-release-contract) · [Release gates](#release-gates) · [Required release record](#required-release-record) · [Validation](#validation) · [Review burden](#review-burden) · [Open verification](#open-verification)

---

## Purpose

`release/agriculture/` is the domain-specific release-governance lane for KFM agriculture outputs. It records release readiness, promotion decisions, release manifests, correction links, withdrawal notes, rollback posture, and public/sensitive exposure decisions for agriculture layers, API payloads, exports, cards, summaries, or map-ready artifacts.

This directory does **not** hold the released artifacts themselves. Released agriculture artifacts belong under the appropriate `data/published/...` path. `release/agriculture/` records the decision trail that proves an agriculture artifact is allowed to be public or semi-public.

Agriculture release work must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move. An agriculture artifact reaches public use only after evidence, source, validation, policy, sensitivity, rights, review, release, correction, and rollback requirements are satisfied.

[Back to top](#top)

---

## Status & authority

| Field | Value |
|---|---|
| **Document type** | Per-domain release README |
| **Owning responsibility root** | `release/` |
| **Subpath role** | `agriculture/` — agriculture release records, promotion notes, release readiness, correction links, rollback posture, public-exposure review |
| **Authority level** | Draft domain-release guidance. Directory Rules, accepted ADRs, release discipline, policy, contracts, schemas, and signed manifests outrank this README. |
| **Lifecycle phase** | Release governance for transition into or correction of PUBLISHED state |
| **Default posture** | Do not release until evidence, rights, sensitivity, validation, policy, review, correction, and rollback posture are resolved |
| **Owners** | `<agriculture-domain-steward>`, `<release-steward>`, `<policy-sensitivity-reviewer>`, `<data-steward>` — fill from CODEOWNERS when assigned |
| **Reviewers required** | Agriculture domain steward + release steward for all agriculture release records; policy/sensitivity reviewer when rights, precision, producer/parcel, infrastructure, ecology, or public-exposure risk exists |

[Back to top](#top)

---

## Repo fit

```text
Kansas-Frontier-Matrix/
└── release/
    ├── README.md
    ├── candidates/
    ├── manifests/
    ├── corrections/
    ├── rollbacks/
    └── agriculture/       ◀── you are here
        └── README.md
```

### Responsibility split

| Location | Owns | Does not own |
|---|---|---|
| `release/agriculture/` | Agriculture release readiness, promotion records, domain release notes, correction/rollback linkage, exposure review | Published artifacts, raw data, processed data, source registry, schemas, policy rules |
| `release/manifests/` | Cross-domain or canonical release manifests when organized centrally | Agriculture domain explanation unless linked here |
| `release/candidates/` | Release candidate dossiers and staged release bundles | Final published data storage |
| `release/corrections/` | Correction records and public correction trail | Primary domain release README content |
| `release/rollbacks/` | Release-level rollback records | Migration rollback records under `migrations/rollback/` |
| `data/published/agriculture/` | Released agriculture artifacts and payloads | Release decisions or approvals |
| `data/processed/agriculture/` | Validated non-public or pre-release derived agriculture outputs | Release approval |
| `data/registry/sources/agriculture/` | Agriculture source registry/source descriptors | Release promotion authority |
| `schemas/contracts/v1/` | Machine-checkable schema authority | Release records |
| `contracts/` | Human-readable contract meaning | Release decisions |
| `policy/` | Allow / deny / restrict / abstain rules | Release manifests or artifacts |

[Back to top](#top)

---

## What belongs here

Use `release/agriculture/` for agriculture-domain release governance material such as:

- Agriculture release readiness notes.
- Domain-specific release manifests or manifest pointers.
- Agriculture promotion records and approval summaries.
- Release candidate review summaries for agriculture layers, cards, exports, API payloads, or map products.
- Correction, withdrawal, supersession, tombstone, and rollback links for agriculture releases.
- Sensitivity and rights review notes for agriculture outputs.
- Public-exposure notes for agricultural land, crop, soil/agronomic, irrigation, conservation, production, facility, or infrastructure-adjacent data.
- Validation summaries proving the artifact is schema-valid, policy-reviewed, evidence-linked, and release-ready.
- Links to EvidenceBundle, SourceDescriptor, PolicyDecision, ValidationReceipt, ReleaseManifest, CorrectionRecord, and RollbackRecord identifiers when available.
- Changelog entries for agriculture release posture.

Accepted file types are Markdown release records, manifest pointers, release checklists, sanitized validation summaries, changelog notes, and non-sensitive release review summaries. Do not store raw data or published artifact payloads here.

[Back to top](#top)

---

## What does not belong here

Do **not** use `release/agriculture/` as a data store, source registry, schema home, policy home, or shortcut to publication.

The following must not live here:

- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED lifecycle payloads.
- Bulk agriculture datasets, rasters, vector tiles, PMTiles, COGs, GeoParquet files, shapefiles, CSV extracts, or API payload files.
- Source descriptors, source intake records, source credentials, source API tokens, or harvested source data.
- Policy bundles, schema files, contract authority, or validator source code.
- Private farm/operator records, precise producer-linked details, sensitive facility/infrastructure information, proprietary production information, private irrigation/water-use details, or rights-uncertain datasets.
- Release approvals without evidence, validation, policy, rights, sensitivity, correction, and rollback posture.
- Unreviewed AI summaries or generated narratives presented as release authority.
- Secrets, credentials, private endpoints, `.env` files, tokens, API keys, private certificates, or production connection details.

If an artifact, secret, or sensitive agriculture dataset lands here, move it to the correct governed location and record the correction. If restricted material was exposed, treat it as a security or governance incident.

[Back to top](#top)

---

## Agriculture release contract

Every agriculture release record should prove that public exposure is appropriate and reversible.

### Required properties

- **Named release unit.** Identify the agriculture layer, export, API payload, Atlas/Card bundle, map product, or documentation release.
- **Artifact pointer.** Link to the artifact in `data/published/...` or the release candidate path. Do not duplicate the payload here.
- **Evidence closure.** Every release claim should resolve to evidence, preferably through EvidenceRef -> EvidenceBundle.
- **Source closure.** Every source should resolve to source descriptor and intake/provenance records.
- **Rights and license posture.** Confirm redistribution/publication rights or fail closed.
- **Sensitivity review.** Address producer, parcel, facility, infrastructure, ecology, water, and precision-location risk where relevant.
- **Policy decision.** Record allow/deny/restrict/abstain outcome and reason code.
- **Validation.** Record schema, contract, data-quality, geometry, attribution, citation, and public-safety checks.
- **Review state.** Identify required stewards and approvals.
- **Release state.** Link ReleaseManifest or release decision record.
- **Correction path.** Identify how errors are corrected after publication.
- **Rollback path.** Identify how public exposure is rolled back, withdrawn, superseded, or tombstoned.

### Agriculture-specific sensitivity prompts

Before release, reviewers should ask:

1. Does the artifact expose precise farm, ranch, operator, parcel, facility, irrigation, production, or infrastructure details?
2. Does it include living-person or private business information?
3. Does it reveal sensitive ecological, conservation, rare-species, archaeology, burial/sacred-site, or critical infrastructure context through agricultural overlays?
4. Are source rights, licensing, redistribution, and attribution clear?
5. Is geometry generalized or redacted where necessary?
6. Are uncertainty, date, source, and update cadence visible to users?
7. Can the release be corrected or rolled back without rewriting history?

[Back to top](#top)

---

## Release gates

| Gate | Question | Failure outcome |
|---|---|---|
| Identity | Is the release unit named and versioned? | BLOCK |
| Source | Do all source references resolve? | BLOCK or QUARANTINE |
| Evidence | Do all release claims resolve to evidence? | ABSTAIN or BLOCK |
| Rights | Are publication and redistribution rights clear? | BLOCK |
| Sensitivity | Are agriculture-specific exposure risks reviewed? | RESTRICT, GENERALIZE, REDACT, or BLOCK |
| Policy | Is there a PolicyDecision with reason code? | DENY / ABSTAIN / BLOCK |
| Validation | Do schema, geometry, data-quality, citation, and artifact checks pass? | BLOCK |
| Review | Have required stewards approved? | BLOCK |
| Manifest | Is the ReleaseManifest or release record complete? | BLOCK |
| Correction | Is correction path defined? | BLOCK |
| Rollback | Is rollback/withdrawal/supersession path defined? | BLOCK |

[Back to top](#top)

---

## Required release record

Every agriculture release should have a reviewable release record.

```markdown
# <agriculture-release-name> release record

## Status
PROPOSED / CANDIDATE / APPROVED / RELEASED / CORRECTED / SUPERSEDED / WITHDRAWN / ROLLED_BACK / BLOCKED

## Release unit
<layer, export, API payload, atlas/card bundle, map product, or docs release>

## Version
<semantic version, date version, content hash, or manifest id>

## Artifact pointer
<data/published/... or release candidate path; do not duplicate payload here>

## Evidence closure
<EvidenceRef / EvidenceBundle references and resolution status>

## Source closure
<SourceDescriptor / SourceIntakeRecord references and resolution status>

## Rights and license
<license, attribution, redistribution, uncertainty, blockers>

## Sensitivity review
<producer/parcel/facility/infrastructure/ecology/location/public-safety notes>

## Policy decision
<ALLOW / DENY / RESTRICT / ABSTAIN with reason code>

## Validation summary
<schema, geometry, citation, data quality, public exposure checks>

## Steward review
<domain, data, policy/sensitivity, release, security if needed>

## Release manifest
<ReleaseManifest id/path/hash>

## Correction path
<how errors are corrected and announced>

## Rollback path
<rollback, withdrawal, supersession, tombstone path>

## Changelog
<public-facing summary and internal notes>
```

[Back to top](#top)

---

## Validation

Agriculture releases require evidence before public exposure.

| Check | Expected result | Evidence |
|---|---|---|
| Path placement | Release record belongs under `release/agriculture/` | PR review |
| Artifact pointer | Artifact lives in `data/published/...` or release candidate path | Path/reference |
| Source resolution | Sources resolve to descriptors/intake records | Source closure note |
| Evidence resolution | EvidenceRefs resolve to EvidenceBundles | Evidence closure note |
| Rights review | License/redistribution posture is clear | Rights note |
| Sensitivity review | Agriculture exposure risks reviewed and mitigated | Sensitivity note |
| Policy decision | Policy outcome and reason code recorded | PolicyDecision reference |
| Schema/contract validation | Payloads match contracts/schemas | Validation receipt |
| Geometry/public-safety check | Sensitive precision is generalized/redacted where needed | Validation note |
| Release manifest | Manifest exists and identifies release unit/version | ReleaseManifest reference |
| Correction path | Correction process is documented | Correction pointer |
| Rollback path | Rollback/withdrawal/supersession path is documented | Rollback pointer |

A release is not ready until reviewers can answer:

1. What is being released?
2. Where is the artifact?
3. What evidence supports it?
4. What rights allow publication?
5. What sensitivity risks remain?
6. What policy decision applies?
7. What validates the artifact?
8. Who approved it?
9. How is it corrected or rolled back?

[Back to top](#top)

---

## Review burden

| Change type | Required review |
|---|---|
| README-only wording with no release behavior | Docs steward or release steward |
| Agriculture release candidate record | Agriculture domain steward + data steward + release steward |
| Public agriculture layer/API/export release | Agriculture domain steward + release steward + policy/sensitivity reviewer |
| Release involving producer, parcel, farm, facility, irrigation, production, or business-sensitive detail | Policy/sensitivity reviewer + domain steward + release steward |
| Release involving ecology, rare species, archaeology, burial/sacred-site, or infrastructure adjacency | Relevant domain steward + policy/sensitivity reviewer + release steward |
| Release correction | Release steward + agriculture domain steward + correction owner |
| Withdrawal, supersession, tombstone, or rollback | Release steward + agriculture domain steward + rollback/correction owner |
| Rights-uncertain or source-license-uncertain release | Source steward + release steward + policy/sensitivity reviewer |
| Exception to normal release gate | ADR or documented risk acceptance with rollback path |

[Back to top](#top)

---

## Open verification

- [ ] Confirm CODEOWNERS for `release/agriculture/`.
- [ ] Confirm whether agriculture release records are stored directly here or under `release/manifests/` with this directory as an index.
- [ ] Confirm canonical ReleaseManifest schema path.
- [ ] Confirm agriculture artifact paths under `data/published/agriculture/`.
- [ ] Confirm agriculture source registry path and source descriptor conventions.
- [ ] Confirm policy/sensitivity rubric for agriculture producer, parcel, facility, irrigation, production, and infrastructure-adjacent data.
- [ ] Confirm validation receipt format and location.
- [ ] Confirm correction record path for agriculture releases.
- [ ] Confirm rollback, withdrawal, supersession, and tombstone path for agriculture releases.
- [ ] Confirm release changelog convention.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing blank file |
| Next review trigger | First agriculture release candidate, ReleaseManifest, correction, withdrawal, supersession, rollback, public API payload, tile/layer/export release, or sensitivity-significant agriculture release PR |
