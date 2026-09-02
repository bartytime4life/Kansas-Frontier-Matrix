<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-source-doctrine-artifact-descriptor
title: contracts/source/doctrine_artifact_descriptor.md — DoctrineArtifactDescriptor Contract
type: contract
version: v0.2
status: draft; PROPOSED; schema-paired; doctrine-source-admission; integrity-bound
owners: OWNER_TBD — Doctrine steward · Source steward · Contracts steward · Schema steward · Review steward · Evidence steward · Docs steward
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; source; doctrine-artifact; descriptor; provenance; integrity; review-signoff; authority-status; no-source-truth
tags: [kfm, contracts, source, doctrine-artifact-descriptor, doctrine, source-admission, sha256, provenance, authority-status, steward-signoff, review, integrity]
related:
  - ./README.md
  - ./source_descriptor.md
  - ../../schemas/contracts/v1/source/doctrine_artifact_descriptor.schema.json
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../docs/doctrine/
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../policy/source/
  - ../../policy/rights/
  - ../../policy/sensitivity/
  - ../../data/registry/sources/
  - ../../release/
notes:
  - "Expanded from a thin schema-paired stub at `contracts/source/doctrine_artifact_descriptor.md`."
  - "Paired schema verified at `schemas/contracts/v1/source/doctrine_artifact_descriptor.schema.json`; schema status is PROPOSED."
  - "The schema requires doc_id, filename, sha256, provenance, authority_status, admitted_at, and steward_signoff_ref; additional properties are false."
  - "DoctrineArtifactDescriptor records admission metadata for doctrine artifacts. It is not the doctrine artifact itself, not EvidenceBundle, not ReleaseManifest, not source truth, not a schema, not a policy decision, and not review proof by itself."
  - "Rollback target for this expansion is previous stub blob SHA `2f2b3088288ea3b18588d2a1b71bba567c5e2307`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# DoctrineArtifactDescriptor Contract

> `DoctrineArtifactDescriptor` records the governed admission metadata for a KFM doctrine artifact: which document/file is being admitted, what integrity hash pins it, where it came from, what authority status is assigned, when it was admitted, and which steward signoff or review reference supports admission. It describes the admitted doctrine artifact; it does not replace the artifact, prove the artifact is correct, or authorize downstream publication by itself.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts/source" src="https://img.shields.io/badge/root-contracts%2Fsource-blue">
  <img alt="Object: DoctrineArtifactDescriptor" src="https://img.shields.io/badge/object-DoctrineArtifactDescriptor-blueviolet">
  <img alt="Schema: paired" src="https://img.shields.io/badge/schema-paired-green">
  <img alt="Integrity: SHA-256" src="https://img.shields.io/badge/integrity-SHA--256-0a7ea4">
  <img alt="Boundary: descriptor not doctrine truth" src="https://img.shields.io/badge/boundary-descriptor__not__truth-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/source/doctrine_artifact_descriptor.md`  
**Paired schema:** `schemas/contracts/v1/source/doctrine_artifact_descriptor.schema.json`  
**Schema status:** PROPOSED  
**Owning root:** `contracts/source/` — source/doctrine-artifact semantic meaning only  
**Policy homes:** `policy/source/`, `policy/rights/`, `policy/sensitivity/`, and doctrine-review policy if accepted  
**Registry/lifecycle homes:** source/doctrine artifact registries and lifecycle roots, not this contract  
**Truth posture:** CONFIRMED target was a thin schema-paired stub · CONFIRMED paired schema exists and points to this contract · CONFIRMED required fields and closed additional-properties posture · NEEDS VERIFICATION for registry home, validator wiring, fixtures, steward review workflow, source/doctrine authority register, release workflow, and runtime consumers

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Schema-paired field surface](#schema-paired-field-surface) · [Field semantics](#field-semantics) · [Authority-status semantics](#authority-status-semantics) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Validation expectations](#validation-expectations) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`DoctrineArtifactDescriptor` is the admission descriptor for doctrine artifacts that KFM depends on for governed behavior.

It answers:

- which doctrine artifact is being admitted;
- which filename or carrier identifies the artifact;
- which SHA-256 digest pins its content;
- where the artifact came from or how its provenance is described;
- whether its authority posture is `CONFIRMED`, `NEEDS_VERIFICATION`, or `PROPOSED`;
- when it was admitted;
- which steward signoff or review reference supports that admission.

It does not answer:

- whether every statement inside the doctrine artifact is true;
- whether the artifact is the newest version;
- whether downstream implementation conforms to the doctrine;
- whether source data, public claims, maps, API responses, or AI answers are correct;
- whether a release is approved;
- whether policy/review obligations have been satisfied beyond the referenced signoff.

---

## Meaning

A `DoctrineArtifactDescriptor` is a source-family descriptor for doctrine artifacts. It is used when the project needs to admit, pin, review, and reference a doctrine file or carrier as part of the governed build system.

A mature governed flow should look like:

```text
doctrine artifact candidate
  -> integrity hashing
  -> provenance capture
  -> steward review / signoff
  -> DoctrineArtifactDescriptor
  -> doctrine/source registry reference
  -> downstream contracts, schemas, policies, tests, docs, or build plans cite the descriptor when doctrine matters
```

The descriptor is metadata and control surface. It is not the artifact content, not source truth, and not implementation proof.

---

## Schema-paired field surface

The paired schema currently confirms these fields:

| Field | Required | Schema-confirmed shape | Semantic role |
|---|---:|---|---|
| `doc_id` | yes | string | Stable identifier for the doctrine artifact or doctrine record. |
| `filename` | yes | string | Filename or carrier name being described. |
| `sha256` | yes | string matching `^[a-fA-F0-9]{64}$` | Content integrity digest without prefix. |
| `provenance` | yes | string | Human-readable provenance statement or provenance ref. |
| `authority_status` | yes | enum: `CONFIRMED`, `NEEDS_VERIFICATION`, `PROPOSED` | Authority posture assigned at admission. |
| `admitted_at` | yes | date-time string | Timestamp when this descriptor was admitted. |
| `steward_signoff_ref` | yes | string | Review/signoff reference supporting admission. |

The schema also confirms:

```text
additionalProperties: false
```

---

## Field semantics

### `doc_id`

Stable identifier for the doctrine artifact descriptor.

Recommended posture:

- should be stable across file moves when the described doctrine artifact remains the same;
- should be unique inside the doctrine/source registry;
- should not be generated from mutable titles alone.

PROPOSED examples:

```text
kfm://doctrine/directory-rules
kfm://doctrine/trust-membrane
kfm://doctrine/source-descriptor-standard
```

### `filename`

Filename or carrier path being described.

This is not sufficient identity by itself. The digest and provenance must carry integrity and origin posture.

### `sha256`

Content digest for the admitted doctrine artifact.

The schema requires exactly 64 hexadecimal characters and does not include a `sha256:` prefix. A future schema may choose to normalize prefixed digests, but this contract follows the currently verified schema.

### `provenance`

Human-readable provenance statement or reference.

It should explain where the artifact came from, whether it was uploaded, generated, converted, migrated, reviewed, or copied, and what upstream source or review process supports it.

### `authority_status`

Authority posture assigned to the admitted doctrine artifact.

This field should be treated as a truth label for governance use, not as a style preference.

### `admitted_at`

Timestamp when this descriptor was admitted.

This is not necessarily the artifact creation time, source publication date, or last-review time.

### `steward_signoff_ref`

Reference to steward review, signoff, approval, review record, issue, PR, receipt, or other governed signoff object.

The schema currently accepts a string. The exact reference format is NEEDS VERIFICATION.

---

## Authority-status semantics

| Status | Meaning | Use posture |
|---|---|---|
| `CONFIRMED` | The artifact's authority for its stated scope has been verified through accepted review/signoff in this repo context. | May be cited as governing doctrine within its scope, while still respecting conflicts and newer ADRs. |
| `NEEDS_VERIFICATION` | The artifact is relevant but not verified strongly enough for authoritative use. | Use cautiously; do not rely on it as sole authority for implementation or release. |
| `PROPOSED` | The artifact or its role is draft/proposed. | Treat as design input; require steward/ADR/review before promotion. |

Authority status does not mean every implementation already conforms. Implementation claims require repo files, tests, logs, runtime evidence, release artifacts, or other current-session evidence.

---

## Invariants

CONFIRMED by paired schema:

- `doc_id`, `filename`, `sha256`, `provenance`, `authority_status`, `admitted_at`, and `steward_signoff_ref` are required.
- `sha256` must match 64 hex characters.
- `authority_status` must be `CONFIRMED`, `NEEDS_VERIFICATION`, or `PROPOSED`.
- `admitted_at` must be date-time formatted.
- Additional properties are not allowed.

PROPOSED semantic invariants:

- A doctrine artifact must not be treated as admitted without a descriptor or equivalent registry record.
- `CONFIRMED` must be supported by steward signoff or an equivalent review record.
- `NEEDS_VERIFICATION` and `PROPOSED` artifacts must not be used as sole evidence for implementation claims, release claims, or public-trust claims.
- Digest mismatch invalidates the descriptor until re-admitted or corrected.
- Superseded doctrine should receive a new descriptor or correction/supersession record rather than silent mutation.
- Generated or converted doctrine carriers must preserve provenance and conversion limits.

---

## Lifecycle role

Doctrine artifacts are not source data in the same sense as external datasets, but they can govern how source data, evidence, policy, contracts, schemas, releases, and AI answers are handled.

Typical uses:

| Lifecycle / governance point | Role of DoctrineArtifactDescriptor |
|---|---|
| Doctrine admission | Pins artifact identity, provenance, digest, and signoff. |
| Contract/schema authoring | Allows doctrine-backed statements to cite admitted doctrine. |
| Policy authoring | Identifies which doctrine document supports a policy rule. |
| Review | Shows whether an artifact is confirmed, proposed, or still under verification. |
| Correction/supersession | Helps track which downstream docs or contracts depended on outdated doctrine. |
| AI build/use | Prevents generated text from silently standing in for admitted doctrine. |

---

## Boundaries

| Boundary | Rule |
|---|---|
| Descriptor vs doctrine artifact | Descriptor describes the artifact; it does not contain or replace the artifact. |
| Descriptor vs SourceDescriptor | SourceDescriptor governs source admission generally; this object specializes doctrine artifact admission metadata. |
| Descriptor vs EvidenceBundle | EvidenceBundle supports claims; descriptor pins doctrine artifact metadata. |
| Descriptor vs ReviewRecord | ReviewRecord/signoff supports admission; descriptor references it. |
| Descriptor vs ReleaseManifest | ReleaseManifest binds released artifacts; descriptor does not publish. |
| Descriptor vs schema | Schema defines shape; this contract defines meaning. |
| Descriptor vs policy | Policy decides admissibility; descriptor records status/signoff context. |
| Descriptor vs AI output | AI may reference admitted doctrine; AI must not mint doctrine authority. |

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- validator existence and wiring for doctrine artifact descriptors;
- fixture coverage for confirmed, needs-verification, proposed, bad hash, missing signoff, and stale/superseded cases;
- registry home for descriptor instances;
- steward signoff reference format;
- digest canonicalization rules for Markdown, PDF, converted carriers, and generated carriers;
- supersession/correction workflow for doctrine changes;
- CI checks that block unreviewed doctrine from being treated as confirmed;
- downstream docs/contracts/policies that cite doctrine descriptors.

---

## Fixtures

Minimum fixture set PROPOSED:

| Fixture | Purpose |
|---|---|
| `valid_confirmed_doctrine.json` | CONFIRMED doctrine artifact with digest and signoff. |
| `valid_needs_verification_doctrine.json` | Relevant artifact not fully reviewed. |
| `valid_proposed_doctrine.json` | Draft/proposed doctrine artifact. |
| `invalid_missing_sha256.json` | Confirms digest requirement. |
| `invalid_bad_sha256_pattern.json` | Confirms 64-hex digest rule. |
| `invalid_unknown_authority_status.json` | Confirms enum. |
| `invalid_missing_steward_signoff_ref.json` | Confirms signoff ref requirement. |
| `invalid_extra_property.json` | Confirms additional properties are closed. |

Fixtures must use synthetic or review-safe references only.

---

## Open questions

- Where should doctrine artifact descriptor instances live: source registry, doctrine registry, control plane, or another governed registry root?
- Should `sha256` use bare 64-hex, `sha256:<hex>`, or `jcs:sha256:<hex>` in a future revision?
- Which review object type should `steward_signoff_ref` point to?
- How should converted PDFs, Markdown carriers, and generated doctrine summaries be hashed and related?
- Should this object become a subtype of SourceDescriptor or remain separate?

---

## Rollback

Rollback is required if this contract is used as doctrine content, source truth, schema authority, policy authority, proof of implementation, release approval, public API/UI/map/AI permission, or a way to treat generated doctrine summaries as admitted authority without review.

Rollback target for this expansion: previous stub blob SHA `2f2b3088288ea3b18588d2a1b71bba567c5e2307`.

<p align="right"><a href="#top">Back to top</a></p>
