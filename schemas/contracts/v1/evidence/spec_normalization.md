# Spec Normalization — Evidence Schema Family

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-evidence-spec-normalization
title: Spec Normalization — Evidence Schema Family
type: standard; schema-family-note; normalization-profile; evidence-governance-boundary
authority_class: proposed-normalization-profile
version: v0.2
status: draft; PROPOSED; conflict-aware; spec-hash-mismatch-visible; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Identity steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — scaffold existed before v0.2 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; evidence; spec-normalization; canonicalization; spec-hash; evidence-bundle; evidence-ref; citation-validation; redaction-receipt; release-gated; rollback-aware
tags: [kfm, schemas, contracts, v1, evidence, spec-normalization, spec_hash, run_id, JCS, RFC-8785, EvidenceBundle, EvidenceRef, CitationValidationReport, RedactionReceipt, EvidenceDrawerPayload, deterministic-identity]
related:
  - ./README.md
  - ./evidence_ref.schema.json
  - ./evidence_bundle.schema.json
  - ./evidence-bundle.schema.json
  - ./citation_validation_report.schema.json
  - ./redaction_receipt.schema.json
  - ./evidence_drawer_payload.schema.json
  - ../common/spec_hash.schema.json
  - ../../../../docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md
  - ../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../../contracts/evidence/
  - ../../../../fixtures/contracts/v1/evidence/
  - ../../../../tools/validators/
notes:
  - "Expanded from a scaffold originally created from docs/domains/flora/IDENTITY_MODEL.md references."
  - "This document is a proposed evidence-family normalization profile, not an accepted hashing implementation."
  - "Current evidence_bundle.schema.json references common/spec_hash.schema.json."
  - "ADR-0013 proposes jcs:sha256:<64-hex-lowercase>, but common/spec_hash.schema.json currently accepts bare sha256:<64-hex-lowercase>; this mismatch is intentionally recorded as NEEDS VERIFICATION."
  - "Do not treat this note as a validator, schema registry, release decision, or canonical runtime behavior."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-PROPOSED-orange)
![family](https://img.shields.io/badge/family-evidence-purple)
![profile](https://img.shields.io/badge/profile-spec__normalization-blue)
![identity](https://img.shields.io/badge/identity-deterministic-informational)
![conflict](https://img.shields.io/badge/spec_hash-mismatch__visible-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![release](https://img.shields.io/badge/release-gated-critical)

> **Purpose.** This file records the proposed normalization profile for evidence-family schema objects before hashing, comparison, fixture generation, validator checks, release review, and rollback targeting.
>
> **One-line boundary.** This document defines proposed normalization guidance for evidence schema objects. It does not compute hashes, validate payloads, store EvidenceBundles, emit receipts, decide policy, release artifacts, or authorize public/AI claims.

---

## Quick jumps

[Status](#status) · [Evidence basis](#evidence-basis) · [Scope](#scope) · [Normalization target](#normalization-target) · [Proposed profile](#proposed-profile) · [spec_hash conflict](#spec_hash-conflict) · [Object-family rules](#object-family-rules) · [Transient fields](#transient-fields) · [Canonicalization gates](#canonicalization-gates) · [Fixtures and validators](#fixtures-and-validators) · [What this is not](#what-this-is-not) · [Promotion checklist](#promotion-checklist) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this file exist? | Yes: `schemas/contracts/v1/evidence/spec_normalization.md`. It existed as a short scaffold before this expansion. | **CONFIRMED** |
| Is this an accepted normative hashing spec? | Not yet. Treat it as a proposed evidence-family normalization profile. | **PROPOSED** |
| Does ADR-0013 define a proposed `spec_hash` grammar? | Yes. It proposes JCS canonicalization and `jcs:sha256:<64-hex-lowercase>` for `spec_hash`. | **CONFIRMED from repo doc** |
| Does current `common/spec_hash.schema.json` match that grammar? | Not fully. It currently permits bare `sha256:<64-hex-lowercase>`. | **CONFIRMED mismatch / NEEDS RESOLUTION** |
| Does this file define runtime behavior? | No. Validator code, CI, fixtures, and runtime logs were not proven here. | **NEEDS VERIFICATION** |
| Can this file promote evidence payloads to publication? | No. Publication requires release review, policy, evidence closure, correction path, and rollback target. | **CONFIRMED governance boundary** |

> [!IMPORTANT]
> This file is intentionally conflict-aware. It records the preferred normalization direction implied by ADR-0013 while preserving the current schema mismatch until the evidence/identity/schema stewards resolve it.

---

## Evidence basis

Current-session repo evidence used for this update:

| Evidence | Confirmed signal |
|---|---|
| `schemas/contracts/v1/evidence/README.md` | Evidence schema family exists, has real files, and records duplicate EvidenceBundle naming risk. |
| `schemas/contracts/v1/evidence/evidence_bundle.schema.json` | Meaningful proposed EvidenceBundle schema with `spec_hash` referencing `common/spec_hash.schema.json`. |
| `schemas/contracts/v1/evidence/evidence_ref.schema.json` | Meaningful proposed EvidenceRef schema. |
| `schemas/contracts/v1/evidence/evidence-bundle.schema.json` | Hyphenated permissive scaffold with empty `properties`; duplicate-name risk. |
| `schemas/contracts/v1/common/spec_hash.schema.json` | Current `spec_hash` field pattern is bare `sha256:<64 hex>`. |
| `docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md` | Proposed deterministic identity grammar: remove transient fields, JCS canonicalize, SHA-256 hash, record as `jcs:sha256:<64 hex>`. |

---

## Scope

This profile applies to evidence-family schema objects and evidence-adjacent payloads shaped by:

- `EvidenceRef`;
- `EvidenceBundle`;
- citation validation reports;
- redaction receipts;
- Evidence Drawer payloads;
- evidence-linked geospatial manifests;
- evidence-facing release/correction/rollback references when they carry evidence hashes.

It is intended to help authors and reviewers answer:

- What should be normalized before computing or comparing evidence identity?
- Which fields are stable identity-bearing content?
- Which fields are transient and must not influence content identity?
- Which duplicate schema names or hash formats need resolution before promotion?
- Which fixtures and validators are required before an evidence schema can be trusted?

---

## Normalization target

The target of normalization is the **content-bearing evidence object** after source-role, rights, sensitivity, transform, and citation metadata have been assembled but before any volatile runtime fields are added.

For example, an `EvidenceBundle` normalization target should include stable claim-support content such as:

- `bundle_id` when the object-family contract treats it as stable;
- `claim_scope`;
- `evidence_refs`;
- `source_records`;
- `citations`;
- `rights`;
- `sensitivity`;
- `transforms`;
- `checksums`;
- stable object-family fields declared by the accepted schema.

It should exclude volatile activity and emission fields such as generated timestamps, signatures, nonces, attestations, and run identifiers before content hash calculation.

---

## Proposed profile

> [!WARNING]
> The profile below is proposed. It should not be treated as final validator behavior until the `spec_hash` mismatch is resolved, fixtures exist, validators exist, and CI proves conformance.

Proposed normalization sequence:

1. **Start with parsed JSON data**, not raw text.
2. **Reject duplicate object keys** before normalization.
3. **Reject non-I-JSON values** such as `NaN`, `Infinity`, and values that cannot be represented safely by the accepted object-family schema.
4. **Apply declared preflight transforms** only if the object-family contract allows them.
5. **Remove transient fields** listed by this profile and the object-family contract.
6. **Preserve semantic strings** unless a declared transform says otherwise.
7. **Preserve source-role, rights, sensitivity, citation, transform, checksum, and evidence-reference fields** unless explicitly declared transient.
8. **Canonicalize JSON** using the ADR-selected canonicalizer, currently proposed as RFC 8785 / JCS for normal JSON objects.
9. **Hash canonical UTF-8 bytes** using SHA-256.
10. **Record the hash in the accepted string form** after the `spec_hash` grammar is resolved.
11. **Attach run identity separately** as activity identity, never as content identity.

---

## `spec_hash` conflict

Current evidence shows a mismatch that must be resolved before this file can be promoted.

| Surface | Current signal | Governance issue |
|---|---|---|
| ADR-0013 | Proposed canonical form: `jcs:sha256:<64-hex-lowercase>`. | This records the canonicalization route in the string. |
| `common/spec_hash.schema.json` | Current pattern: `^sha256:[a-f0-9]{64}$`. | This omits the canonicalization route and conflicts with ADR-0013's proposed grammar. |
| `evidence_bundle.schema.json` | References `common/spec_hash.schema.json`. | EvidenceBundle validation inherits the current bare-hash shape unless schema changes. |

Required handling:

- Do not silently switch evidence schemas to `jcs:sha256:` without updating `common/spec_hash.schema.json`, fixtures, validators, downstream `$ref` consumers, and migration notes.
- Do not keep writing bare `sha256:` forever if ADR-0013 is accepted as-is.
- During migration, validators may need a compatibility window, but the accepted canonical write form must be explicit.
- Hash values must not be recomputed after release without a correction/rollback trail.

---

## Object-family rules

| Object family | Normalization rule | Status |
|---|---|---|
| `EvidenceRef` | Normalize stable reference identifier, kind, and bundle linkage. Do not inject retrieval-time or runtime-status fields into content identity. | **PROPOSED** |
| `EvidenceBundle` | Normalize stable claim-support body after removing `spec_hash`, signatures, attestations, run IDs, and volatile timestamps. | **PROPOSED** |
| `CitationValidationReport` | Normalize cited target, validation ruleset identity, results, and evidence references; exclude emission timestamp and runner-specific fields from content hash unless contract says otherwise. | **PROPOSED / NEEDS VERIFICATION** |
| `RedactionReceipt` | Normalize transform reason, policy basis, source evidence reference, output evidence reference, and rollback target; protect sensitive before/after details according to policy. | **PROPOSED / NEEDS VERIFICATION** |
| `EvidenceDrawerPayload` | Treat as a display projection. Its hash may identify the payload but must not replace the underlying EvidenceBundle hash. | **PROPOSED / NEEDS VERIFICATION** |
| `KFMGeoManifest` | Normalize artifact identity, checksums, layer refs, evidence refs, and release refs. Do not let it replace ReleaseManifest or EvidenceBundle. | **PROPOSED / NEEDS VERIFICATION** |

---

## Transient fields

Minimum proposed transient fields for evidence-family content hashing:

```text
spec_hash
generated_at
updated_at
fetched_at
retrieved_at
timestamp
nonce
run_id
openlineage_run_uuid
signer
signature
signatures
attestation
attestations
validation_started_at
validation_finished_at
emitted_at
published_at
```

Object-family contracts may add fields to this list, but should not shrink the minimum list without ADR-class review.

> [!CAUTION]
> Do not remove fields merely because they are inconvenient. Source role, citations, rights, sensitivity, transforms, checksums, and evidence references are governance-bearing and should remain in the normalized body unless an accepted object-family contract explicitly excludes them.

---

## Canonicalization gates

Before evidence-family normalization can be promoted, the following gates should exist as fixtures and validator checks:

| Gate | Expected behavior |
|---|---|
| Duplicate key gate | Reject duplicate JSON object keys before canonicalization. |
| Non-finite number gate | Reject `NaN`, `Infinity`, and unsafe numeric forms. |
| Stable key order gate | Canonical output is independent of input object key order. |
| Whitespace gate | Hash is independent of insignificant JSON whitespace. |
| Unicode policy gate | Unicode normalization policy is declared and tested; strings are not silently mutated during hashing. |
| Transient exclusion gate | Adding/removing volatile timestamps or run IDs does not change content hash. |
| Governance inclusion gate | Changing citations, rights, sensitivity, transforms, checksums, or EvidenceRefs changes content hash unless the contract explicitly says otherwise. |
| Duplicate schema gate | Hyphen/underscore EvidenceBundle variants do not both act as canonical authorities. |
| Compatibility gate | Bare `sha256:` and `jcs:sha256:` handling is explicit during migration. |

---

## Fixtures and validators

Expected fixture lanes:

```text
fixtures/contracts/v1/evidence/evidence_ref/
fixtures/contracts/v1/evidence/evidence_bundle/
fixtures/contracts/v1/evidence/citation_validation_report/
fixtures/contracts/v1/evidence/redaction_receipt/
fixtures/contracts/v1/evidence/evidence_drawer_payload/
```

Expected validator lanes or entry points:

```text
tools/validators/validate_evidence_ref.py
tools/validators/validate_evidence_bundle.py
tools/validators/validate_spec_hash.py
```

These paths are schema-declared or expected by current docs, but their implementation maturity remains **NEEDS VERIFICATION** unless separately inspected.

Recommended fixture cases:

- same object with different key order produces same canonical hash;
- same object with whitespace changes produces same canonical hash;
- object with changed citation produces different hash;
- object with changed sensitivity label produces different hash;
- object with changed transform list produces different hash;
- object with changed `run_id` does not change content hash;
- object with changed `generated_at` does not change content hash;
- duplicate key input fails;
- bare `sha256:` vs `jcs:sha256:` migration behavior is explicit;
- hyphenated and underscored EvidenceBundle files do not both pass as canonical authorities.

---

## What this is not

This file is not:

- a JSON Schema;
- a validator implementation;
- a schema registry record;
- an accepted ADR;
- a release decision;
- an EvidenceBundle instance;
- a receipt or proof object;
- a policy decision;
- a public API contract;
- a MapLibre layer contract;
- an AI answer contract.

---

## Promotion checklist

Do not promote this file beyond `PROPOSED` until:

- [ ] ADR-0013 is accepted, amended, or explicitly superseded.
- [ ] `common/spec_hash.schema.json` matches the accepted `spec_hash` grammar or records a compatibility profile.
- [ ] EvidenceBundle duplicate naming is resolved, mirrored, or deprecated.
- [ ] `evidence_bundle.schema.json` and any accepted EvidenceBundle variant agree on `$id`, `$ref`, and required fields.
- [ ] Valid fixtures cover canonicalization, transient fields, governance-bearing fields, and duplicate-key rejection.
- [ ] Invalid fixtures cover malformed hashes, duplicate keys, unsafe numbers, missing citations, missing rights, missing sensitivity, and unresolved evidence refs.
- [ ] Validator implementations exist and are wired into CI.
- [ ] Downstream domain schemas and API/UI payloads use the accepted hash grammar.
- [ ] Release, correction, and rollback docs know how to treat hash-format migrations.

---

## Rollback

Rollback for this document is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/evidence/spec_normalization.md`.

Rollback for the underlying normalization profile requires more care:

1. Identify which schema, validator, fixture, API, release, or artifact began using the profile.
2. Revert or migrate `common/spec_hash.schema.json` and evidence schemas together.
3. Update `$ref` consumers and schema registry records.
4. Regenerate fixtures and validator expected outputs.
5. Update EvidenceBundle, RunReceipt, ReleaseManifest, catalog, tile metadata, and AI receipt references that recorded the prior grammar.
6. Preserve correction notices and rollback targets for any released artifacts affected by hash-format changes.
7. Keep compatibility readers only as long as the migration plan says they are necessary.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should `spec_hash` canonical write form be `jcs:sha256:<hex>` as ADR-0013 proposes, or bare `sha256:<hex>` as the current common schema permits? | **NEEDS RESOLUTION** | Identity steward + schema steward |
| Should `common/spec_hash.schema.json` accept both forms during migration? | **PROPOSED / NEEDS VERIFICATION** | Schema steward + validation steward |
| Which EvidenceBundle filename is canonical: `evidence_bundle.schema.json`, `evidence-bundle.schema.json`, or another ADR-selected form? | **NEEDS VERIFICATION** | Evidence steward |
| Which transient fields are shared across all evidence objects, and which are object-family-specific? | **NEEDS VERIFICATION** | Evidence steward + contract steward |
| Which canonicalizer is allowed for graph-shaped evidence payloads? | **ADR-0013 points to URDNA2015 option / NEEDS IMPLEMENTATION VERIFICATION** | Identity steward |
| Where is the schema registry entry for this profile? | **NEEDS VERIFICATION** | Schema steward |
| Which CI jobs prove spec normalization? | **NEEDS VERIFICATION** | Validation steward |

---

## Maintainer notes

- Keep this file conflict-aware until the hash grammar mismatch is resolved.
- Do not use this note to justify publishing evidence-backed claims without release review.
- Do not let duplicate EvidenceBundle schema names become parallel authorities.
- Preserve KFM's truth posture: generated language is downstream; EvidenceBundle and source-governed proof carry the claim.
