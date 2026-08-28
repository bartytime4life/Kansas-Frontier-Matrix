<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-fauna-domain-feature-identity
title: Fauna Domain Feature Identity Contract
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Fauna steward · Identity steward · Contract steward · Source steward · Sensitivity reviewer · Policy steward · Schema steward · Validation steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; semantic-contract; fauna; identity; deterministic-id; source-role-aware; sensitivity-aware; no-publication-authority
related:
  - ./README.md
  - ./conservation_status.md
  - ./disease_observation.md
  - ../../../docs/domains/fauna/README.md
  - ../../../docs/domains/fauna/SOURCES.md
  - ../../../docs/domains/fauna/SOURCE_ROLES.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../docs/domains/fauna/SCHEMAS.md
  - ../../../schemas/contracts/v1/domains/fauna/domain_feature_identity.schema.json
  - ../../../data/registry/sources/fauna/
  - ../../../policy/domains/fauna/
  - ../../../policy/sensitivity/fauna/
  - ../../../fixtures/domains/fauna/domain_feature_identity/
  - ../../../tests/domains/fauna/
tags: [kfm, contracts, fauna, domain-feature-identity, identity, deterministic-id, source-role, temporal-scope, spec-hash, evidence, sensitivity, governance]
notes:
  - "Expanded from a greenfield scaffold into a Fauna identity-support semantic contract."
  - "The paired schema is a PROPOSED stub requiring only id and allowing additional properties; full field enforcement remains NEEDS VERIFICATION."
  - "This contract defines identity meaning only; it is not a species occurrence, disease record, conservation status, policy decision, release manifest, evidence bundle, or public-safe location approval."
  - "Fauna identity must preserve source role, object family, temporal scope, spatial/support scope, evidence references, sensitivity posture, correction lineage, and rollback context where material."
  - "The user-provided Markdown Authoring Agent v2 prompt was treated as authoring guidance, not pasted into this contract."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Domain Feature Identity

> Semantic contract for the Fauna identity-support object that names, scopes, versions, and links a Fauna feature across source role, object family, taxonomic scope, time, support geometry, evidence, sensitivity, correction, and rollback context.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/fauna" src="https://img.shields.io/badge/family-domains%2Ffauna-2ea44f">
  <img alt="Contract type: semantic" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed stub" src="https://img.shields.io/badge/schema-PROPOSED__stub-lightgrey">
  <img alt="Identity: deterministic" src="https://img.shields.io/badge/identity-deterministic-blueviolet">
  <img alt="Sensitivity: fail closed" src="https://img.shields.io/badge/sensitivity-fail__closed-critical">
</p>

`contracts/domains/fauna/domain_feature_identity.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Identity recipe](#identity-recipe) · [Invariants](#invariants) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Open questions](#open-questions) · [Evidence basis](#evidence-basis) · [Rollback](#rollback)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/fauna/domain_feature_identity.md`  
> **Schema path:** `schemas/contracts/v1/domains/fauna/domain_feature_identity.schema.json`  
> **Truth posture:** target path, prior scaffold, paired schema metadata, Fauna contract-lane split, and Fauna schema-home split are CONFIRMED from current repo evidence. Field-level enforcement, fixtures, validators, policy behavior, source registry behavior, release workflow, public API behavior, and UI behavior remain NEEDS VERIFICATION.

> [!CAUTION]
> This contract defines identity meaning only. It does **not** authorize public release, expose exact sensitive locations, prove occurrence, decide policy, define schema shape, or replace object-family contracts such as `conservation_status.md` or `disease_observation.md`.

---

## Meaning

`DomainFeatureIdentity` is the Fauna-domain identity carrier for a governed Fauna feature or feature-like semantic object.

It exists to answer:

- Which Fauna object family is being identified?
- Which source and source role contributed the identity?
- Which taxon, host, population, site, range, event, occurrence, monitoring, mortality, disease, or invasive-species scope is involved?
- Which temporal axes are part of identity and must not be collapsed?
- Which support geometry or spatial scope is part of identity, and is it safe to expose?
- Which normalized digest or `spec_hash` pins the represented content?
- Which EvidenceRef, source descriptor, policy decision, review record, correction notice, and rollback context applies?

It is an identity-support object. It is **not** the object payload itself. Object meaning stays in object-specific contracts such as `conservation_status.md`, `disease_observation.md`, `occurrence_evidence.md`, `sensitive_site.md`, `range_polygon.md`, or future reviewed Fauna contracts.

---

## Repo fit

The Fauna contract README places semantic meaning in `contracts/domains/fauna/` while keeping machine shape in `schemas/`, policy in `policy/`, proof in `tests/` and `fixtures/`, source registry content in `data/registry/sources/fauna/`, lifecycle data in `data/`, and release decisions in `release/`.

| Responsibility | Fauna lane path | This contract's role |
|---|---|---|
| Semantic identity meaning | `contracts/domains/fauna/domain_feature_identity.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/fauna/domain_feature_identity.schema.json` | Linked only |
| Object-family meaning | `contracts/domains/fauna/*.md` | Referenced, not replaced |
| Source identity and source role | `data/registry/sources/fauna/` | Required upstream support |
| Sensitivity and geoprivacy policy | `policy/sensitivity/fauna/`, `policy/domains/fauna/` | Required admissibility gate |
| Evidence/proof support | `data/proofs/`, `tests/domains/fauna/`, `fixtures/domains/fauna/` | Required before consequential use |
| Release/correction/rollback | `release/`, correction contracts, receipts | Required downstream governance |

This split prevents an identity contract from quietly becoming a schema, source registry, policy file, sensitive-location disclosure, release manifest, or public truth store.

---

## Schema posture

The paired schema currently exists as a **PROPOSED stub**.

| Schema fact | Current evidence |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/fauna/domain_feature_identity.schema.json` |
| Schema title | `domain_feature_identity` |
| Declared properties | `spec_hash`, `id`, `version` |
| Required fields | `id` only |
| Additional properties | `true` |
| Fixture root | `fixtures/domains/fauna/domain_feature_identity/` in schema metadata |
| Validator path | `tools/validators/domains/fauna/validate_domain_feature_identity.py` in schema metadata |
| Policy path | `policy/domains/fauna/` in schema metadata |

Because the schema is not field-complete, this contract defines **semantic expectations** for future schema, fixtures, validators, and policy tests. It does not claim the current schema enforces those expectations.

---

## Accepted uses

| Use | Allowed? | Rule |
|---|---:|---|
| Carrying stable Fauna feature identity | Yes | Must preserve source, source role, object family, temporal scope, spatial/support scope, digest, and lineage context. |
| Linking object-family records to evidence and source records | Yes | Evidence and source references must resolve before consequential claims. |
| Supporting dedupe, merge, supersession, or non-regression checks | Yes | Must not collapse source role, taxonomic scope, sensitivity posture, or time. |
| Supporting correction and rollback lineage | Yes | Identity changes must remain auditable. |
| Distinguishing observed, regulatory, aggregate, administrative, candidate, modeled, and synthetic objects | Yes | Source-role discipline is part of identity context. |
| Publishing a public Fauna claim | No | Release requires separate evidence, policy, review, redaction, and release support. |
| Acting as object payload | No | Object-family contracts own object meaning. |
| Acting as schema enforcement | No | `.schema.json` files own shape. |
| Acting as policy decision | No | Policy homes decide allow/deny/restrict/abstain. |
| Acting as sensitive-location approval | No | Geoprivacy and release are governed separately. |

---

## Exclusions

| Does not belong in `DomainFeatureIdentity` | Correct home |
|---|---|
| Full species occurrence, conservation status, disease, mortality, range, or monitoring payload | Object-family contracts and schemas |
| Raw coordinates, sensitive site details, transform parameters, or re-identifying join details | Policy/restricted data roots; not in public contract prose |
| Source descriptor, license, cadence, or rights record | `data/registry/sources/fauna/` |
| EvidenceBundle content | Evidence/proof roots |
| JSON Schema shape | `schemas/contracts/v1/domains/fauna/domain_feature_identity.schema.json` |
| Validator implementation | `tools/validators/domains/fauna/validate_domain_feature_identity.py` after verification |
| PolicyDecision, ReviewRecord, RedactionReceipt, ReleaseManifest, CorrectionNotice, RollbackCard | Their own governance/release/correction homes |
| Public UI/API payload or Focus Mode content | Governed app/API/UI/focus-mode roots |

> [!WARNING]
> Do not use example identity values that reveal exact sensitive locations, nests, dens, roosts, hibernacula, spawning sites, restricted steward records, private-land joins, rare-taxon locations, or redaction transform parameters.

---

## Recommended semantics

The current schema requires only `id`. The following fields are PROPOSED semantic expectations for a reviewed schema and fixture suite.

| Field | Meaning |
|---|---|
| `id` | Canonical Fauna feature identity. |
| `version` | Contract/object identity version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `object_family` | Fauna object family, such as `Taxon`, `ConservationStatus`, `OccurrenceEvidence`, `DiseaseObservation`, `SensitiveSite`, `RangePolygon`, or `InvasiveSpeciesRecord`. |
| `feature_role` | Identity role within the object family: occurrence, status, disease observation, mortality event, monitoring event, range, site, or aggregate. |
| `source_id` | SourceDescriptor/source identity that contributed the feature. |
| `source_role` | Canonical source role for the assertion. |
| `source_native_id` | Source-native key, record id, catalog id, event id, or observation id where available. |
| `taxon_ref` | Taxon or authority-taxonomy reference when material. |
| `support_geometry_ref` | Geometry, site, range, grid, administrative unit, or generalized spatial support reference. |
| `sensitivity_tier` | Release/sensitivity posture when relevant. |
| `public_geometry_policy` | Whether and how public geometry may be derived. |
| `temporal_scope` | Observed, valid, source, retrieval, release, and correction time roles where material. |
| `normalized_digest` | Canonicalized digest of identity-defining content. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links required before cite-or-answer behavior. |
| `policy_refs` | PolicyDecision or policy rule references. |
| `review_refs` | Steward, domain, source, sensitivity, or release review references. |
| `correction_refs` | CorrectionNotice or supersession references. |
| `rollback_ref` | Rollback target when a published or promoted identity is corrected or withdrawn. |

---

## Identity recipe

A stable Fauna identity should use a deterministic recipe that avoids merging unlike records.

```text
fauna_feature_identity = hash(
  source_id +
  object_family +
  feature_role +
  source_role +
  taxon_or_subject_scope +
  temporal_scope +
  support_geometry_scope +
  normalized_digest
)
```

This recipe is PROPOSED until the paired schema and validator define exact canonicalization. At minimum, the identity must preserve:

- source role and source identity;
- object family and feature role;
- taxon/subject scope where material;
- observed/valid/source/retrieval/release/correction time separation where material;
- spatial/support scope without exposing restricted geometry;
- normalized digest or `spec_hash`;
- correction and rollback lineage.

---

## Invariants

1. **Identity is not evidence.** Identity points to evidence; it does not prove a claim by itself.
2. **Identity is not release.** A stable id can exist for T4 or quarantined records that must never be public.
3. **Source role is identity-significant.** A regulatory status, observed occurrence, aggregate rank, modeled range, and synthetic reconstruction must not share identity merely because they reference the same taxon or geography.
4. **Time roles remain separate.** Observed time, valid time, source time, retrieval time, release time, and correction time must not be collapsed.
5. **Sensitive geometry is not normalized into public identity prose.** Identity can preserve a restricted geometry reference without revealing the geometry.
6. **Correction changes must be auditable.** Reclassification, duplicate merge, withdrawn source record, taxonomic split/lump, changed sensitivity tier, and false-positive correction require lineage.
7. **Derived layers do not replace canonical truth.** Tiles, maps, summaries, vector indexes, and AI text are downstream carriers, not identity authority.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native ids and payload digests may be captured but are not public identity. |
| WORK / QUARANTINE | Candidate identity is normalized, source-role checked, rights checked, sensitivity checked, and compared against existing identities. |
| PROCESSED | Reviewed identity receives deterministic id/spec hash, evidence references, temporal scope, and support-scope references. |
| CATALOG / TRIPLET | Identity can support graph edges only when evidence, source role, and safe scope resolve. |
| PUBLISHED | Public-safe identity surfaces only through released artifacts/governed interfaces and only at the approved granularity. |
| CORRECTION / ROLLBACK | Identity changes must record correction notice, supersession target, and rollback target where applicable. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Define exact identity canonicalization algorithm for Fauna features.
- [ ] Confirm whether `spec_hash` uses RFC 8785 JCS + SHA-256 or another accepted project digest rule.
- [ ] Update the paired schema beyond the current stub fields.
- [ ] Add valid fixtures for at least conservation status, occurrence evidence, sensitive site, range, monitoring event, mortality observation, disease observation, and invasive species record identity cases.
- [ ] Add invalid fixtures proving source-role collapse, time-role collapse, sensitive-geometry leakage, and object-family merge errors fail validation.
- [ ] Confirm validator path existence and behavior.
- [ ] Confirm policy tests block public identity disclosure when sensitivity, rights, review, or release state is unresolved.
- [ ] Confirm correction and rollback records can resolve from an identity change.

---

## Open questions

| ID | Question | Status |
|---|---|---|
| OQ-FAUNA-DFI-001 | What exact canonicalization rule should Fauna identity use for `spec_hash`? | NEEDS VERIFICATION |
| OQ-FAUNA-DFI-002 | Which object-family names are final for v1 schema enforcement? | NEEDS VERIFICATION |
| OQ-FAUNA-DFI-003 | Should `sensitivity_tier` be required in identity or only linked by policy/release records? | NEEDS VERIFICATION |
| OQ-FAUNA-DFI-004 | How should taxonomic split/lump corrections affect identity supersession? | NEEDS VERIFICATION |
| OQ-FAUNA-DFI-005 | Which geometry scopes can appear in public identity displays without re-identification risk? | NEEDS VERIFICATION |
| OQ-FAUNA-DFI-006 | Should source-native ids be stored directly, hashed, or wrapped in EvidenceRef for restricted sources? | NEEDS VERIFICATION |

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `contracts/domains/fauna/domain_feature_identity.md` prior version | CONFIRMED repo evidence | Target existed as a greenfield scaffold. | Did not define authoritative semantics. |
| `schemas/contracts/v1/domains/fauna/domain_feature_identity.schema.json` | CONFIRMED repo evidence | Paired schema exists, points to this contract, declares `spec_hash`, `id`, and `version`, and requires `id`. | Schema is a PROPOSED stub and allows additional properties. |
| `contracts/domains/fauna/README.md` | CONFIRMED repo evidence | Fauna contract lane owns semantic meaning and excludes schema, policy, data, fixtures, tests, and release decisions. | Does not define this specific identity object. |
| `docs/domains/fauna/SCHEMAS.md` | CONFIRMED repo evidence | Explains the shape/meaning/policy/proof split and schema-home rule. | Does not implement validator behavior. |
| `docs/domains/fauna/SOURCE_ROLES.md` | CONFIRMED repo evidence | Provides source-role anti-collapse vocabulary and examples. | Crosswalk only; per-source assignments belong to SourceDescriptor records. |
| `docs/domains/fauna/SENSITIVITY.md` | CONFIRMED repo evidence | Establishes fail-closed sensitive Fauna posture and geoprivacy concerns. | Binding policy remains outside this contract. |

---

## Rollback

Rollback if this file is used to claim implemented identity validation, publish sensitive Fauna identities, merge unlike source roles, collapse time roles, bypass policy/review/release gates, or treat identity as evidence or publication permission.

Rollback target: prior scaffold blob SHA `ffbd48fc44e32a5f066b11bc5c694f660ef8a853`.

<p align="right"><a href="#top">Back to top</a></p>
