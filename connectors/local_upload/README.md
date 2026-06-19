<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-local-upload-readme
title: connectors/local_upload/ — Local Upload Connector Family
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source-intake steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; connector-family; directory-rules-7-3; local-upload; trust-edge; deny-by-default; quarantine-first; no-publication
proposed_path: connectors/local_upload/README.md
truth_posture: CONFIRMED path exists / CONFIRMED doctrine-level §7.3 connector family / IMPLEMENTATION DEPTH NEEDS VERIFICATION
related:
  - ../README.md
  - ../../docs/sources/catalog/local_upload/README.md
  - ../../docs/sources/catalog/local_upload.md
  - ../../docs/sources/catalog/local_upload/user-file-upload.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/trust-membrane.md
  - ../../docs/doctrine/lifecycle-law.md
  - ../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../data/registry/sources/
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/sources/local_upload/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, local-upload, local_upload, intake, source-admission, trust-edge, source-descriptor, raw, quarantine, rights, sensitivity, provenance, receipts, governance]
notes:
  - "This README replaces the greenfield stub in `connectors/local_upload/`."
  - "The local-upload source catalog states that `connectors/local_upload/` is named in Directory Rules §7.3 and in the proposed target tree."
  - "Local upload is the highest-uncertainty source-intake lane: identity, rights, sensitivity, source role, geometry precision, and redistribution posture are unknown until reviewed."
  - "Connector output may enter RAW or QUARANTINE handoff only; validation, EvidenceBundle closure, rights/sensitivity review, catalog/triplet projection, release review, publication, correction, and rollback remain outside this folder."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Local Upload Connector Family

> Connector README for `connectors/local_upload/`, the KFM trust-edge lane for files supplied by a person or operator rather than fetched from a versioned external source endpoint. This connector admits candidate material only; it does not publish, promote, normalize to truth, or bypass rights and sensitivity review.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Directory Rules: §7.3 connector" src="https://img.shields.io/badge/directory__rules-%C2%A77.3__connector-success">
  <img alt="Policy: deny by default" src="https://img.shields.io/badge/policy-deny__by__default-red">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` connector README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/local_upload/README.md`  
> **Truth posture:** `CONFIRMED` path exists · `CONFIRMED` doctrine-level §7.3 connector family · `NEEDS VERIFICATION` implementation files, tests, fixtures, and CI wiring  
> **Boundary:** trust-edge source admission only; no direct publication, no source-role upgrade, no rights/sensitivity bypass, no public client access to RAW/QUARANTINE.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Evidence ledger](#evidence-ledger) · [Admission posture](#admission-posture) · [Lifecycle boundary](#lifecycle-boundary) · [Validation](#validation) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/local_upload/` covers files admitted into KFM from a user, steward, operator, browser upload, CLI import, or staging-folder handoff where the producer is not a versioned external publisher.

At admission time, identity, rights, sensitivity, source role, provenance, geometry precision, source date, and redistribution status are unresolved unless a governed descriptor and review state prove otherwise.

A local-upload file is candidate material. It becomes admissible only after descriptor creation, validation, policy checks, and review decisions appropriate to the file class and risk.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/local_upload/` | Canonical local-upload connector-family lane named in Directory Rules §7.3. | **CONFIRMED path / CONFIRMED doctrine-level family** |
| `docs/sources/catalog/local_upload/README.md` | Human-facing source catalog entry for local uploads. | **CONFIRMED** |
| `docs/sources/catalog/local_upload/user-file-upload.md` | Product/surface-level catalog page for user-file upload. | **CONFIRMED search result / NEEDS FILE REVIEW** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside connector / NEEDS VERIFICATION for entries** |
| `data/raw/` | Candidate immutable RAW handoff target. | **Outside connector** |
| `data/quarantine/` | Candidate fail-closed handoff target. | **Outside connector** |
| `policy/sources/local_upload/` | Candidate local-upload source policy root. | **Referenced by catalog / NEEDS VERIFICATION** |
| `policy/rights/`, `policy/sensitivity/` | Rights and sensitivity authority. | **Outside connector** |
| `release/` | Release and publication controls. | **Out of scope for this connector** |

---

## Accepted inputs

This connector may accept candidate files only for governed admission. Acceptance is not approval.

Typical candidate classes include tabular, geospatial, document, image, bundled, or opaque files. Actual classification must be based on content inspection, metadata, schema checks, and steward review where needed. Filename extension alone is not authoritative.

Accepted material should preserve upload event, supplied filename, content fingerprint, candidate source role, available rights statement, sensitivity flags, review state, parsing defects, and quarantine reasons where applicable.

---

## Exclusions

This connector must not silently promote:

- files from a versioned external publisher that should use a dedicated connector;
- files addressed directly to processed, catalog, triplet, published, proof, receipt, or release roots;
- release artifacts presented as uploads;
- generated files presented as observed reality without proper candidate or synthetic labeling;
- high-risk or unresolved files where the safe outcome is quarantine, redaction, generalization, staged access, or denial.

Rejected or quarantined files should produce an auditable outcome, not silent discard.

[Back to top ↑](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/local_upload/README.md` | **CONFIRMED** | Target file existed as a greenfield stub before this update. | Does not prove implementation files, tests, or CI. |
| `docs/sources/catalog/local_upload/README.md` | **CONFIRMED** | Catalog says local upload is a trust-edge intake lane; `connectors/local_upload/` is named in Directory Rules §7.3; output must stay RAW/QUARANTINE until governed review. | Does not prove current implementation depth. |
| `docs/sources/catalog/local_upload/user-file-upload.md` | **CONFIRMED search result / NEEDS FILE REVIEW** | Product/surface page exists in search results. | File body was not inspected in this response. |
| `docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md` | **CONFIRMED search result / NEEDS FILE REVIEW** | Search result indicates an ADR for connector RAW/QUARANTINE-only outputs. | File body was not inspected in this response. |

---

## Admission posture

Default admission posture:

- source role starts as `candidate`;
- rights status starts unresolved unless reviewed;
- sensitivity starts conservative;
- publication is denied until release review succeeds;
- public clients must not read RAW, WORK, QUARANTINE, or unpublished candidates;
- unknown or opaque content routes to quarantine;
- parsing failure routes to quarantine with reason;
- claimed source role is not trusted until review;
- promotion does not upgrade source role by itself.

The connector may prepare descriptors, event envelopes, file fingerprints, and quarantine receipts. It may not decide final source authority or public visibility.

---

## Lifecycle boundary

Allowed connector outputs are limited to governed handoff records and candidate files for:

```text
RAW or QUARANTINE only
```

The connector must not write directly to processed, catalog, triplet, published, proof, receipt, release, or public UI surfaces.

Downstream movement from RAW or QUARANTINE is a governed state transition with validation, provenance, policy checks, review, and rollback targets.

---

## Validation

Validation should check that:

- an upload event is recorded;
- a content fingerprint exists;
- file type classification is content-based;
- SourceDescriptor creation is required before activation;
- source role remains candidate until reviewed;
- rights status is explicit and unresolved rights fail closed;
- sensitivity status is explicit and conservative by default;
- malformed, opaque, unsafe, or high-risk material routes to quarantine;
- no output is treated as released or public;
- connector writes are limited to RAW or QUARANTINE handoff.

Tests must prove these boundaries before implementation maturity is claimed.

---

## Rollback

Rollback is required if this README is used to justify direct publication, source-role upgrade, rights or sensitivity bypass, public access to unpublished upload material, or direct writes beyond RAW/QUARANTINE handoff.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

A safe rollback is to restore the prior greenfield stub or replace this document with a shorter connector-boundary note until implementation files and tests are verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual connector code under `connectors/local_upload/`. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm SourceDescriptor schema fields for local upload. | **NEEDS VERIFICATION** | Schema file and fixtures. |
| Confirm local-upload source policy files. | **NEEDS VERIFICATION** | `policy/sources/local_upload/` contents. |
| Confirm RAW/QUARANTINE handoff implementation. | **NEEDS VERIFICATION** | Code, tests, and ADR review. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |
| Confirm quarantine receipts. | **NEEDS VERIFICATION** | Code, validators, and test evidence. |

---

## Maintainer note

Keep this connector conservative. Local upload is useful because it lets KFM admit user-supplied evidence, but it is also where rights, sensitivity, identity, source role, and provenance are most uncertain. Fail closed, preserve evidence, and let governed review carry the truth boundary.

[Back to top ↑](#top)
