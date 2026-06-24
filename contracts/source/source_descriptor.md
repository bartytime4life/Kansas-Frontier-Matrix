<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-source-source-descriptor
title: contracts/source/source_descriptor.md — SourceDescriptor Contract
type: contract
version: v0.3
status: draft; PROPOSED; schema-paired; canonical-lowercase; source-admission; source-role-anti-collapse
owners: OWNER_TBD — Source steward · Contracts steward · Schema steward · Policy steward · Catalog steward · Evidence steward · Release steward · Docs steward
created: NEEDS VERIFICATION — file existed before v0.3 expansion
updated: 2026-06-24
policy_label: public; contracts; source; source-descriptor; source-admission; rights; sensitivity; cadence; access; citation; review; release; lifecycle; fail-closed
tags: [kfm, contracts, source, source-descriptor, source-role, source-type, rights, sensitivity, cadence, access, citation, source-head, admissibility, review-state, release-state, lifecycle, registry]
related:
  - ./README.md
  - ./SOURCE_DESCRIPTOR.md
  - ./ingest_receipt.md
  - ./doctrine_artifact_descriptor.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../packages/source-registry/README.md
  - ../../data/registry/sources/
  - ../../policy/source/
  - ../../policy/rights/
  - ../../policy/sensitivity/
  - ../../fixtures/contracts/v1/source/
  - ../../tools/validators/
  - ../../docs/architecture/contract-schema-policy-split.md
notes:
  - "Expanded from an older minimal SourceDescriptor contract that used legacy fields `id`, `domain`, `role`, `authority`, `sensitivity_floor`, `update_cadence`, `access_posture`, and `citation_template`."
  - "Paired schema verified at `schemas/contracts/v1/source/source_descriptor.schema.json`; schema status is PROPOSED."
  - "The schema identifies this lowercase file as `x-kfm.contract_doc` and records `schemas/contracts/v1/sources/source_descriptor.schema.json` as canonical schema path plus this source path as legacy schema path."
  - "Canonical validation now requires richer SourceDescriptor v1 fields: object_type, schema_version, source_id, descriptor_version, title, source_type, source_role, authority_rank, publisher, owner_or_steward, rights, sensitivity_default, cadence, access, citation, source_head, admissibility_limits, public_release, review_state, release_state, and lifecycle."
  - "Deprecated legacy aliases remain schema properties for migration only."
  - "SourceDescriptor records how source material may be treated; it does not make source claims true, authorize release by itself, or replace evidence, policy, review, validation, source registry records, or release artifacts."
  - "Rollback target for this expansion is previous blob SHA `737dc98d36a75d597b3533c87a6027e23f123e2d`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SourceDescriptor Contract

> `SourceDescriptor` is the governed admission and authority-control descriptor for a source. It records source identity, type, role, authority posture, rights, sensitivity, cadence, access, citation, source-head metadata, admissibility limits, review state, release state, and lifecycle posture before source material can shape downstream evidence, catalog, map, graph, API, release, or AI outputs. It records how a source may be treated; it does not make the source's claims true.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts/source" src="https://img.shields.io/badge/root-contracts%2Fsource-blue">
  <img alt="Object: SourceDescriptor" src="https://img.shields.io/badge/object-SourceDescriptor-blueviolet">
  <img alt="Schema: paired" src="https://img.shields.io/badge/schema-paired-green">
  <img alt="Default: fail closed" src="https://img.shields.io/badge/default-fail__closed-critical">
  <img alt="Boundary: source metadata not truth" src="https://img.shields.io/badge/boundary-source__metadata__not__truth-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/source/source_descriptor.md`  
**Legacy-case pointer:** `contracts/source/SOURCE_DESCRIPTOR.md`  
**Paired schema currently inspected:** `schemas/contracts/v1/source/source_descriptor.schema.json`  
**Schema-declared canonical path:** `schemas/contracts/v1/sources/source_descriptor.schema.json`  
**Schema-declared legacy path:** `schemas/contracts/v1/source/source_descriptor.schema.json`  
**Schema status:** PROPOSED  
**Registry home named by schema:** `data/registry/sources/`  
**Policy home named by schema:** `policy/source/`  
**Truth posture:** CONFIRMED this lowercase file is the schema-declared contract doc · CONFIRMED current schema requires the richer SourceDescriptor v1 field surface · CONFIRMED older minimal fields are now deprecated migration aliases · NEEDS VERIFICATION for canonical schema-path migration, validator path/wiring, fixtures, policy packages, persisted source registry records, CI gates, runtime/catalog/API/AI consumers, release workflows, and source-authority register maturity

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Schema-paired required surface](#schema-paired-required-surface) · [Field semantics](#field-semantics) · [Enums and controlled states](#enums-and-controlled-states) · [Legacy field aliases](#legacy-field-aliases) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Validation expectations](#validation-expectations) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`SourceDescriptor` captures the governed admission profile for a source before its records can influence downstream claims.

It answers:

- which source is being admitted or governed;
- which domains may consider the source;
- what kind of source it is;
- which source role it can play;
- who publishes, owns, or stewards it;
- what rights, terms, attribution, redistribution, and access limits apply;
- what sensitivity default and review posture apply;
- how current or stale the source is expected to be;
- how it may be accessed;
- how it must be cited;
- what low-cost source-head or content identity evidence is known;
- which claim roles are allowed or prohibited;
- whether public release is allowed, review-gated, redaction-gated, or denied;
- what review, release, and lifecycle state applies.

It does not answer:

- whether any claim in the source is true;
- whether derived evidence is sufficient;
- whether release is approved;
- whether downstream policy gates pass;
- whether source data can be copied into public artifacts;
- whether AI may infer source authority;
- whether a connector, watcher, or pipeline may bypass policy or review.

---

## Meaning

`SourceDescriptor` is the governance handle attached to source material. It is not a bibliography entry, citation string, manifest, license file, data payload, or release record.

A mature source-admission flow should look like:

```text
source candidate
  -> SourceDescriptor draft
  -> rights / sensitivity / access / citation / authority review
  -> policy and steward review
  -> registry admission or quarantine / denial / retirement
  -> ingest receipt and downstream lifecycle use only if allowed
  -> evidence/catalog/release/public surfaces cite source posture without upgrading it
```

The descriptor fixes how KFM may treat a source. It does not upgrade a weak source into a strong source, a candidate signal into verified truth, or a fixture into public evidence.

---

## Schema-paired required surface

The current inspected schema requires these fields:

| Field | Required | Schema-confirmed shape | Semantic role |
|---|---:|---|---|
| `object_type` | yes | const `SourceDescriptor` | Object-family discriminator. |
| `schema_version` | yes | const `v1` | Schema version for this object. |
| `source_id` | yes | `kfm://source/...` or `src:...` pattern | Stable source identifier. |
| `descriptor_version` | yes | semantic-version pattern | Version of the descriptor record. |
| `title` | yes | string, min length 3 | Human-readable source title. |
| `source_type` | yes | controlled enum | What kind of source it is. |
| `source_role` | yes | controlled enum | What evidentiary or contextual role it may play. |
| `authority_rank` | yes | controlled enum | How the source's authority is ranked for its role. |
| `publisher` | yes | organization contact object | Publishing organization/contact posture. |
| `owner_or_steward` | yes | organization contact object | Owner/steward organization/contact posture. |
| `rights` | yes | closed object | Rights, license/terms, attribution, redistribution, commercial use, and verification. |
| `sensitivity_default` | yes | controlled enum | Default sensitivity class. |
| `cadence` | yes | closed object | Update cadence, freshness expectation, and staleness policy. |
| `access` | yes | closed object | Access method, posture, endpoints, auth and format targets. |
| `citation` | yes | closed object | Citation requirement, template, guidance, and optional links/text. |
| `source_head` | yes | closed object | Source-head/content identity observation. |
| `admissibility_limits` | yes | closed object | Allowed/prohibited claim roles and confidence posture. |
| `public_release` | yes | closed object | Public-release allowance, review, redaction, and conditions. |
| `review_state` | yes | controlled enum | Review status. |
| `release_state` | yes | controlled enum | Release status. |
| `lifecycle` | yes | closed object | Registry state, created/updated time, supersession fields. |

The schema also permits optional `domain_scope`, `secondary_source_roles`, `connectors`, `governance_refs`, `spec_hash`, and deprecated legacy aliases. `additionalProperties` is false.

---

## Field semantics

### Identity and version

- `object_type` must identify this object as `SourceDescriptor`.
- `schema_version` pins the shape version.
- `source_id` is the stable source identifier; it should be used for source registry lookup and source-role enforcement.
- `descriptor_version` versions the descriptor record independently of upstream source version.
- `title` names the source clearly enough for review, citation, and registry navigation.

### Scope and role

- `domain_scope` lists KFM domain lanes where the source may be considered; it is not an authority grant by itself.
- `source_type` identifies the type of source material.
- `source_role` identifies the allowed role the source can play.
- `secondary_source_roles` can record additional roles without silently upgrading the primary role.
- `authority_rank` and `authority_notes` express why the source is authoritative, contextual, candidate-only, fixture-only, or otherwise limited.

### Publisher and stewardship

`publisher` and `owner_or_steward` are organization contact objects. They preserve who publishes and who owns or stewards the source. Unknown or unavailable contact posture should remain explicit rather than guessed.

### Rights

`rights` records rights status, license or terms, attribution requirement, redistribution allowance, commercial-use allowance, verification time, and verifier.

Rights are policy-significant. Unknown, noassertion, denied, or restricted rights must fail closed for public release unless a later governed policy/review path explicitly resolves them.

### Sensitivity

`sensitivity_default` records the default sensitivity class for source material. Sensitivity does not disappear when a source is ingested, transformed, summarized, tiled, mapped, graphed, or answered by AI.

### Cadence and freshness

`cadence` records update cadence, freshness expectation, and staleness policy. Freshness posture affects citation, runtime response, review, and release decisions.

### Access

`access` records how the source is reached and under what access posture. Credentialed, restricted, closed, or unknown access must not be converted into public availability by a connector, pipeline, or AI helper.

### Citation

`citation` records whether citation is required, the citation template, and guidance. Missing citation duties can block public release or force abstention.

### Source-head identity

`source_head` records low-cost source-head or content identity evidence such as ETag, last modified, content length, checksum, upstream version, revision id, or a not-applicable reason. It supports drift detection but does not replace validation, rights review, or publication gates.

### Admissibility and public release

`admissibility_limits` records which claim roles this source may support, which roles are prohibited, limitations, confidence posture, and review requirements.

`public_release` records whether public release is allowed, review-gated, redaction-gated, and under which conditions. It is not release approval; `ReleaseManifest`, review, policy, and correction/rollback paths remain separate.

### Review, release, lifecycle, and governance refs

- `review_state` records review posture.
- `release_state` records whether the descriptor/source posture is not released, candidate, released, deprecated, or withdrawn.
- `lifecycle` records registry state, creation/update times, and supersession metadata.
- `governance_refs` can link source registry, rights review, sensitivity policy, ADR, or validation report references.

---

## Enums and controlled states

The schema defines controlled vocabularies for source type, source role, authority rank, claim role, sensitivity class, rights status, permission state, update cadence, access method, access posture, review state, release state, endpoint purpose, source-head method, connector activation state, staleness policy, auth type, confidence posture, and lifecycle registry state.

Notable examples:

- Source roles include `authoritative_for_claim`, `regulatory_context`, `legal_context`, `observation`, `occurrence_evidence`, `aggregator`, `candidate_signal`, `derived_public_product`, `steward_review_source`, `citation_source`, and `fixture_only`.
- Sensitivity classes include `public`, `low`, `restricted`, `sensitive_location`, `living_person`, `dna_genomic`, `cultural_sensitive`, `infrastructure_sensitive`, `steward_controlled`, `controlled`, and `unknown_review_required`.
- Rights statuses include `verified_open`, `verified_restricted`, `permission_required`, `unknown`, `noassertion`, and `denied`.
- Release states include `not_released`, `candidate`, `released`, `deprecated`, and `withdrawn`.

---

## Legacy field aliases

The schema retains these deprecated aliases for migration only:

| Deprecated field | Canonical replacement |
|---|---|
| `id` | `source_id` |
| `domain` | `domain_scope[]` |
| `role` | `source_role` |
| `authority` | `authority_rank` plus `authority_notes` |
| `sensitivity_floor` | `sensitivity_default` plus `public_release` controls |
| `update_cadence` | `cadence.update_cadence` |
| `access_posture` | `access.access_posture` |
| `citation_template` | `citation.citation_template` |

Do not write new descriptors using only legacy fields. They are present so older records can be migrated safely, not so the older minimal contract remains canonical.

---

## Invariants

CONFIRMED by paired schema:

- The current contract doc is this lowercase path.
- The schema status is PROPOSED.
- The richer v1 required fields listed above are required.
- `object_type` must be `SourceDescriptor`.
- `schema_version` must be `v1`.
- `source_id` must match the declared KFM/source or `src:` pattern.
- `descriptor_version` must match a three-part semantic version pattern.
- `rights`, `cadence`, `access`, `citation`, `source_head`, `admissibility_limits`, `public_release`, and `lifecycle` are closed objects.
- `additionalProperties` is false.
- If rights are `unknown`, `noassertion`, or `denied`, public release must be `allowed: false`.
- If sensitivity is restricted/sensitive/living-person/DNA/cultural/infrastructure/steward-controlled/controlled/unknown-review, public release requires review.
- If connectors are `live_candidate` or `live_active`, review state must be `reviewed` or `approved`.
- If source role is `fixture_only`, public release must be false and release state must not be normal public release.
- If public release is allowed, review state must be `reviewed` or `approved`.

PROPOSED semantic invariants:

- Source role is fixed at admission and must not be silently upgraded by promotion.
- Unknown rights fail closed.
- Unknown sensitivity fails closed.
- Candidate, fixture-only, restricted, or denied sources must not shape public claims without governed review/policy/release state.
- AI cannot infer or upgrade source authority.
- A SourceDescriptor controls treatment of source material; it does not make source claims true.
- Supersession must be explicit and auditable.

---

## Lifecycle role

`SourceDescriptor` begins before or during RAW intake planning and stays visible throughout downstream lifecycle transitions:

```text
source candidate
  -> SourceDescriptor draft/proposed
  -> source admission / rights / sensitivity / access / citation review
  -> RAW ingest or WORK / QUARANTINE hold
  -> PROCESSED evidence assembly if allowed
  -> CATALOG / TRIPLET source-role projection if allowed
  -> PUBLISHED release only through release/review/policy gates
```

The descriptor may be active, quarantined, retired, or superseded. Supersession does not rewrite history; downstream receipts and release artifacts must remain auditable.

---

## Boundaries

| Boundary | Rule |
|---|---|
| SourceDescriptor vs source data | Descriptor records governance metadata; it does not contain source payloads. |
| SourceDescriptor vs IngestReceipt | Descriptor governs source posture; ingest receipt records a capture event. |
| SourceDescriptor vs EvidenceBundle | EvidenceBundle supports claims; SourceDescriptor constrains source use. |
| SourceDescriptor vs PolicyDecision | Policy decides allow/deny/restrict/abstain; descriptor supplies policy input. |
| SourceDescriptor vs ReleaseManifest | ReleaseManifest binds published artifacts; descriptor cannot publish by itself. |
| SourceDescriptor vs source-registry package | Package may resolve descriptors; it must not override them. |
| SourceDescriptor vs citation | Citation text is downstream rendering; descriptor controls citation guidance. |
| SourceDescriptor vs AI | AI may reference descriptor-approved evidence; AI must not mint source authority. |

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- canonical schema path migration from `source` to `sources`, if accepted;
- validator path and CI wiring;
- fixture updates for the richer v1 field surface;
- policy/source enforcement of rights, sensitivity, review, and release gating;
- source registry record persistence under `data/registry/sources/` or accepted successor;
- source-authority register maturity;
- connector/watcher activation checks against descriptor review state;
- source-head drift checks;
- catalog, graph, API, map, and AI consumers resolving descriptor posture before use;
- correction/supersession workflows for descriptor updates.

---

## Fixtures

Minimum fixture set PROPOSED:

| Fixture | Purpose |
|---|---|
| `valid_verified_open_authoritative.json` | Open authoritative source with public release allowed after review. |
| `valid_restricted_review_required.json` | Restricted or sensitive source requiring review/redaction. |
| `valid_fixture_only.json` | Fixture source that must not be public release source truth. |
| `valid_unknown_rights_denied_public.json` | Rights unknown/noassertion/denied forces public release false. |
| `valid_live_connector_reviewed.json` | Live connector state with reviewed/approved review state. |
| `invalid_missing_required_field.json` | Confirms richer v1 required surface. |
| `invalid_bad_source_id_pattern.json` | Confirms source id pattern. |
| `invalid_unknown_rights_public_allowed.json` | Confirms fail-closed rights rule. |
| `invalid_sensitive_no_review.json` | Confirms sensitive source requires review. |
| `invalid_extra_property.json` | Confirms closed object/additional property behavior. |

Fixtures must avoid credentials, secrets, private URLs, living-person data, protected locations, and unlicensed payloads.

---

## Open questions

- Should `schemas/contracts/v1/sources/source_descriptor.schema.json` become the active schema path and this `source` path become legacy only?
- Which validator path is the accepted current path: older `tools/validators/validate_source_descriptor.py` or schema-declared `tools/validators/sources/validate_source_descriptor.py`?
- Where exactly do persisted SourceDescriptor records live in the final registry layout?
- Which policy package enforces source admission and public-release constraints?
- Should source admission emit a dedicated receipt in addition to SourceDescriptor and IngestReceipt?

---

## Rollback

Rollback is required if this contract is used as source data storage, source-claim truth, schema authority, policy authority, source-registry instance storage, connector permission, release approval, runtime/API/UI/map permission, or AI authority.

Rollback target for this expansion: previous blob SHA `737dc98d36a75d597b3533c87a6027e23f123e2d`.

<p align="right"><a href="#top">Back to top</a></p>
