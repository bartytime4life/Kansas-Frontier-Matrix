<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-domain-feature-identity
title: Domain Feature Identity Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Identity steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public-with-gates; semantic-contract; geology; identity; deterministic-identity; spec-hash; source-role-aware; evidence-bound; release-gated; correction-ready
tags: [kfm, contracts, geology, domain_feature_identity, identity, deterministic-identity, source-id, object-role, temporal-scope, spec-hash, jcs-sha256, evidence-ref, evidence-bundle, source-role, lifecycle, validation, release, correction, rollback]
related:
  - ./README.md
  - ./GeologicUnit.md
  - ./GeologyBoundaryVersion.md
  - ./BoreholeReference.md
  - ./WellLogReference.md
  - ./MineralOccurrence.md
  - ./ResourceDeposit.md
  - ./ResourceEstimate.md
  - ../../../docs/domains/geology/IDENTITY_MODEL.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../schemas/contracts/v1/domains/geology/domain_feature_identity.schema.json
  - ../../../fixtures/domains/geology/domain_feature_identity/
  - ../../../tools/validators/domains/geology/validate_domain_feature_identity.py
  - ../../../policy/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a greenfield scaffold into a Geology domain_feature_identity semantic contract."
  - "The paired schema exists at schemas/contracts/v1/domains/geology/domain_feature_identity.schema.json, but it is still a PROPOSED stub with only id, version, and spec_hash fields; field-level enforcement remains NEEDS VERIFICATION."
  - "This contract defines an identity envelope / support object for Geology feature/object claims. It is not a substitute for GeologicUnit, Lithology, StratigraphicInterval, StructureFeature, BoreholeReference, WellLogReference, MineralOccurrence, ResourceDeposit, ResourceEstimate, release manifests, or EvidenceBundles."
  - "Identity doctrine is grounded in the four-component basis source_id + object_role + temporal_scope + normalized_digest/spec_hash and the six KFM time dimensions: source, observed, valid, retrieval, release, correction."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Feature Identity — Geology

> Semantic contract for `domain_feature_identity`: the Geology identity envelope that binds source authority, object role, temporal scope, normalized digest, EvidenceRef/EvidenceBundle resolution, lifecycle state, correction, and rollback across Geology object families.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: domain_feature_identity" src="https://img.shields.io/badge/object-domain__feature__identity-blue">
  <img alt="Schema: stub" src="https://img.shields.io/badge/schema-stub%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Hash: jcs sha256" src="https://img.shields.io/badge/spec__hash-jcs%3Asha256-informational">
  <img alt="Boundary: identity not truth by itself" src="https://img.shields.io/badge/boundary-identity__not__truth__by__itself-critical">
</p>

`contracts/domains/geology/domain_feature_identity.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Identity formula](#identity-formula) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Object-family profiles](#object-family-profiles) · [Source-role rules](#source-role-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/domain_feature_identity.md`  
> **Schema path:** `schemas/contracts/v1/domains/geology/domain_feature_identity.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` stub. It currently defines only `spec_hash`, `id`, and `version`, requires only `id`, and permits additional properties.  
> **Truth posture:** Geology identity doctrine is supported by the docs-side identity model and object-family reference. Field-level schema enforcement, fixtures, validator behavior, policy runtime, release workflow, API behavior, UI behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `domain_feature_identity` is an identity envelope / support contract. It does **not** replace object-family contracts, EvidenceBundles, SourceDescriptors, policy decisions, release manifests, correction notices, rollback cards, map features, API payloads, or AI/UI truth.

---

## Meaning

`domain_feature_identity` records the minimum identity-bearing semantics needed to decide whether two Geology features or object-family records are the **same governed claim**, two versions of the same claim, or different claims that merely share a name, geometry, source, or public label.

It answers:

- Which Geology object family or feature role is being identified?
- Which source authority and source role admitted the evidence?
- Which temporal dimensions are material to this identity?
- Which normalized digest / `spec_hash` fixes the identity-bearing content?
- Which EvidenceRef and EvidenceBundle resolve the claim before use?
- Which lifecycle state, release state, correction lineage, and rollback target govern the identity?
- Which public-safe carrier may expose the identity without leaking restricted geometry, payloads, rights-limited records, or unreviewed candidates?

This contract should be used as a support layer by Geology object-family contracts, schemas, validators, catalogs, triplets, release manifests, correction notices, and governed API/UI/AI projections.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Identity semantics | `contracts/domains/geology/domain_feature_identity.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/geology/domain_feature_identity.schema.json` | CONFIRMED stub; field-level enforcement NEEDS VERIFICATION |
| Identity doctrine | `docs/domains/geology/IDENTITY_MODEL.md` | Governs four-part identity basis, source roles, time dimensions, spec hash, lifecycle, failure modes |
| Object-family roster | `docs/domains/geology/OBJECT_FAMILIES.md` | Supplies shared identity rule and per-family intrinsic key fields |
| Geology scope | `docs/domains/geology/SCOPE.md` | Defines owned/not-owned boundaries and cross-lane exclusions |
| Source identity | `data/registry/sources/geology/` and cross-cutting SourceDescriptor homes | Source authority, rights, role, cadence, and citation |
| Evidence binding | EvidenceRef / EvidenceBundle homes, paths NEED VERIFICATION | Claim support and digest closure |
| Policy and sensitivity | `policy/domains/geology/`, `policy/sensitivity/geology/` | Allow/deny/abstain and public-safe exposure decisions |
| Fixtures and tests | `fixtures/domains/geology/domain_feature_identity/`, `tests/domains/geology/` | Proof cases for identity, role, time, hash, sensitivity, release, and rollback |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion, correction, and rollback identity binding |

---

## Schema posture

The paired schema exists but is intentionally thin.

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/geology/domain_feature_identity.schema.json` |
| Schema status | `PROPOSED` |
| Schema description | Greenfield placeholder; fields to be defined per contract document and ADR |
| Defined properties | `spec_hash`, `id`, `version` |
| Required fields | `id` only |
| Additional properties | `true` |
| Schema-linked fixtures root | `fixtures/domains/geology/domain_feature_identity/` |
| Schema-linked validator | `tools/validators/domains/geology/validate_domain_feature_identity.py` |
| Validator implementation | NEEDS VERIFICATION; schema references the path, but runtime/file behavior was not verified here |

Until the schema is expanded, this contract is the semantic authority for review, but not proof of field-level validation.

---

## Identity formula

Geology identity follows the four-component basis used by the docs-side identity model and object-family reference:

```text
identity = normalize(
  source_id
  + object_role
  + temporal_scope
  + normalized_digest
)
```

Where:

| Component | Meaning | Contract posture |
|---|---|---|
| `source_id` | Stable SourceDescriptor handle for the evidence authority | Required semantic component |
| `object_role` | What kind of thing the record is and which source role supports it | Required semantic component |
| `temporal_scope` | Material time dimensions for the claim | Required semantic component |
| `normalized_digest` / `spec_hash` | Canonical content fingerprint, normally `jcs:sha256:<hex>` | Required semantic component; exact mechanics must match validator/ADR |

The six KFM time dimensions must stay distinct where material:

| Time dimension | Meaning |
|---|---|
| `source_time` | When the source authored or published the record. |
| `observed_time` | When the phenomenon was observed, sampled, logged, surveyed, or measured. |
| `valid_time` | When the claim is asserted to be valid. |
| `retrieval_time` | When KFM retrieved the source. |
| `release_time` | When KFM released the public-safe artifact. |
| `correction_time` | When KFM corrected, superseded, or rolled back a prior assertion. |

> [!WARNING]
> Collapsing source time, observed time, retrieval time, release time, or correction time can rotate meaning without changing a visible label. Validators should treat that as an identity failure, not a formatting issue.

---

## Assertions

A reviewed `domain_feature_identity` should semantically assert:

1. **Canonical identifier** — stable `id` for the identity envelope.
2. **Object family** — the Geology object family or feature role being identified.
3. **Source authority** — `source_id`, source role, source record refs, rights, and source limits.
4. **Object role** — observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, or accepted future role after ADR.
5. **Temporal scope** — material time dimensions, each preserved separately.
6. **Normalized digest** — `spec_hash` / normalized content digest with algorithm tag.
7. **Intrinsic keys** — family-specific keys such as geometry fingerprint, unit code, borehole ref, artifact digest, commodity set, classification scheme, or boundary version.
8. **Evidence closure** — EvidenceRef and EvidenceBundle refs that resolve before public or AI claims are made.
9. **Sensitivity carrier** — public-safe geometry fingerprint, redaction/aggregation receipt refs, rights posture, and restricted exact-detail posture where material.
10. **Lifecycle state** — RAW/WORK/QUARANTINE/PROCESSED/CATALOG/TRIPLET/PUBLISHED state and promotion posture.
11. **Correction lineage** — supersession, correction, merge/split, rollback target, and replacement identity refs.
12. **Anti-collapse posture** — denials for cross-role and cross-family identity equality where doctrine forbids it.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating identity as evidence | Identity points to evidence; EvidenceBundle carries support. |
| Treating identity as release approval | ReleaseManifest / PromotionDecision owns publication state. |
| Treating identity as policy decision | Policy owns allow/deny/abstain/restrict. |
| Treating identical geometry as identical object | Geometry is only one identity-bearing component; source, role, time, and digest still matter. |
| Treating name/casing drift as identity rotation | Naming drift is reconciled through drift/ADR; meaning-bearing fields rotate identity, not typography. |
| Treating public-safe geometry as exact geometry | Public-safe geometry is a derivative carrier and needs a receipt. |
| Treating source URL/path/ETag as `source_id` | SourceDescriptor identity is the source handle; URLs and ETags are validators/locators. |
| Treating candidate identity as publishable | Candidate records have no normal public edge until reviewed and promoted. |
| Treating synthetic identity as observed truth | Synthetic identities require reality-boundary disclosure and receipt support. |
| Treating UI/AI summary as identity authority | UI/AI output is interpretive and evidence-subordinate. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. Only `id`, `version`, and `spec_hash` are currently visible in the confirmed schema stub.

| Field | Meaning |
|---|---|
| `id` | Canonical domain-feature identity ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized digest, expected `jcs:sha256:<hex>` unless ADR says otherwise. |
| `domain` | Must resolve to `geology`. |
| `object_family` | Geology object family being identified. |
| `canonical_family_name` | Accepted canonical spelling after drift/ADR resolution. |
| `source_family_name` | Source-native or legacy family spelling retained for audit. |
| `object_role` | Identity role: observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, or accepted enum value. |
| `source_id` | Stable SourceDescriptor handle. |
| `source_descriptor_ref` | Link to SourceDescriptor or source registry record. |
| `source_record_refs` | Source-native IDs, rows, layers, reports, files, records, or map features. |
| `intrinsic_key_set` | Family-specific identity keys. |
| `intrinsic_key_hash` | Stable hash of normalized intrinsic key set. |
| `geometry_fingerprint` | Geometry fingerprint where geometry is identity-bearing. |
| `public_safe_geometry_fingerprint` | Public derivative geometry fingerprint where restricted geometry is generalized/redacted. |
| `temporal_scope` | Structured object carrying material time dimensions. |
| `source_time` | Source publication/assertion time. |
| `observed_time` | Observation/sample/log/survey/acquisition time where material. |
| `valid_time` | Validity interval or assertion scope. |
| `retrieval_time` | KFM retrieval/harvest time. |
| `release_time` | Public-safe release time. |
| `correction_time` | Correction/supersession time. |
| `evidence_ref_ids` | EvidenceRef IDs that must resolve. |
| `evidence_bundle_refs` | EvidenceBundle refs that support the identity. |
| `rights_state` | Rights, license, redistribution, attribution, embargo, proprietary, or unknown state. |
| `sensitivity_state` | Public, generalized, restricted, withheld, rights-limited, source-limited, or unknown state. |
| `policy_decision_ref` | Policy decision governing use or release where material. |
| `review_record_ref` | Review record for identity, source, steward, policy, release, or correction. |
| `redaction_receipt_ref` | Receipt for generalized/redacted public-safe geometry or detail. |
| `aggregation_receipt_ref` | Receipt for aggregate public derivative. |
| `representation_receipt_ref` | Receipt for synthetic/reconstructed/visualized representation where needed. |
| `validation_report_ref` | Validation result for identity closure. |
| `release_ref` | ReleaseManifest / PromotionDecision / release candidate ref. |
| `correction_refs` | Correction notices, supersession refs, merge/split refs, rollback refs. |
| `lifecycle_state` | RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, CORRECTED, WITHDRAWN, or accepted enum. |
| `quality_flags` | Identity warning states such as role conflict, temporal collapse, hash mismatch, missing evidence, restricted geometry leak, or naming drift. |

---

## Object-family profiles

The object-family reference gives each family its own intrinsic keys. This contract does not replace those object contracts; it supplies the shared envelope that carries their identity-bearing keys.

| Object family | Identity-bearing keys to carry or reference | Public/sensitivity warning |
|---|---|---|
| `GeologicUnit` | `unit_code`, `map_provenance_id`, `geometry_fingerprint`, `lithology_ref`, `age_ref` | Version pin required for rendering. |
| `Lithology` | `lithology_code`, `vocabulary_ref`, `descriptor_set_hash` | Vocabulary drift must not silently rotate meaning. |
| `StratigraphicInterval` | `interval_name`, `lower_bound_ref`, `upper_bound_ref`, `age_ref` | Bounds and age model matter. |
| `StructureFeature` / `Fault Structure` | `feature_class`, `geometry_fingerprint`, `map_provenance_id` | Structural context, not hazards risk. |
| `BoreholeReference` | `borehole_id`, `operator_role_authority`, `public_safe_geometry_fingerprint`, `source_id` | Exact point restricted/generalized by default. |
| `WellLogReference` | `borehole_ref`, `log_type`, `log_artifact_digest`, `source_id` | LAS payloads reference-only public by default. |
| `CoreSample` | `borehole_ref`, `depth_interval`, `sample_id`, `source_id` | Exact location/custody detail restricted where needed. |
| `GeophysicalObservation` | `survey_id`, `geometry_fingerprint`, `instrument_class`, `source_id` | Derived surfaces must remain modeled. |
| `GeochemistrySample` | `sample_id`, `sample_medium`, `analytical_method_ref`, `source_id` | Collection and report times must not collapse. |
| `MineralOccurrence` | `occurrence_id`, `commodity_set`, `public_safe_geometry_fingerprint`, `source_id` | Occurrence is not deposit or estimate. |
| `ResourceDeposit` | `deposit_id`, `commodity_set`, `public_safe_geometry_fingerprint`, `source_id` | Deposit is not occurrence or estimate. |
| `ResourceEstimate` | `estimate_id`, `commodity_set`, `classification_scheme_ref`, `aggregation_unit`, `source_id` | Estimate is modeled/aggregate, not observed. |
| `ExtractionSite` | `site_id`, `operator_role_authority`, `public_safe_geometry_fingerprint` | Physical site, not permit/title/operator proof. |
| `ReclamationRecord` | `site_ref`, `program_authority`, `reclamation_status_code` | Status/plan/observation, not compliance proof. |
| `CrossSection` | `section_id`, `line_geometry_fingerprint`, `interpretation_basis_ref` | Synthetic/reconstructed surfaces need representation caveats. |
| `HydrostratigraphicUnit` | `unit_name`, `geometry_fingerprint`, `hydrology_link_ref` | Geology↔Hydrology bridge; not Hydrology measurement. |

---

## Source-role rules

`object_role` is identity-bearing. A role change is not a display change; it can create a different identity.

| Role | Identity meaning | Geology examples | Failure if collapsed |
|---|---|---|---|
| `observed` | Direct reading, mapped contact, sample, survey, log curve, or first-hand source record. | mapped contacts, LAS curves, geochemistry analyses | Modeled/interpreted data falsely treated as observation. |
| `regulatory` | Governing-body determination or regulatory context. | KCC status/regulatory layers | Regulatory context falsely treated as observed geology. |
| `modeled` | Derived product from inputs, assumptions, fitted parameters, interpretation, or reconstruction. | resource estimate, interpreted tops, reconstructed surfaces | Model falsely treated as observed truth. |
| `aggregate` | Published summary over an aggregation unit. | county totals, resource summaries | Aggregate joined as per-place truth. |
| `administrative` | Program, registration, inventory, catalog, or accounting record. | borehole/well program records, source catalogs | Admin record falsely treated as field evidence. |
| `candidate` | Detected/unreviewed/unpromoted candidate. | unresolved imports, fuzzy matches | Candidate leaks into PUBLISHED. |
| `synthetic` | Generated, reconstructed, AI-created, or visualized object. | AI description, synthetic 3D scene | Synthetic content presented as observed reality. |

---

## Anti-collapse rules

This contract exists mainly to prevent identity collapse.

```text
domain_feature_identity != EvidenceBundle
domain_feature_identity != SourceDescriptor
domain_feature_identity != PolicyDecision
domain_feature_identity != ReleaseManifest
domain_feature_identity != object-family truth by itself
domain_feature_identity != map tile / UI payload / AI summary
```

Geology-specific denials:

```text
MineralOccurrence != ResourceDeposit != ResourceEstimate
BoreholeReference != WellLogReference != CoreSample
GeologicUnit != Lithology != StratigraphicInterval != GeologicAge
StructureFeature != Hazards risk
HydrostratigraphicUnit != Hydrology measurement
ExtractionSite != ownership / lease / permit / title proof
Synthetic representation != observed geology
Aggregate summary != per-place record
Candidate identity != publishable identity
```

Any equality, merge, split, or supersession between identities must be reviewable and receipt-backed.

---

## Lifecycle

| Phase | Identity handling |
|---|---|
| RAW | Source payload and SourceDescriptor are captured; identity is not yet authoritative. |
| WORK | Candidate object role, temporal scope, intrinsic keys, and draft spec are normalized. |
| QUARANTINE | Identity remains non-public until conflict, rights, sensitivity, evidence, or validation issues resolve. |
| PROCESSED | `spec_hash` becomes final for the reviewed claim; EvidenceRef and validation report can be minted. |
| CATALOG / TRIPLET | EvidenceBundle resolves and graph/catalog claims are projected from the same identity. |
| RELEASE CANDIDATE | Public-safe identity carrier is prepared with policy/review/receipt/release support. |
| PUBLISHED | Identity is exposed only through governed release artifacts, APIs, UI, and AI surfaces. |
| CORRECTED / SUPERSEDED | Correction notice records why identity was updated, replaced, merged, split, withdrawn, or rolled back. |

> [!IMPORTANT]
> Promotion is a governed state transition, not a file move. An identity can exist in PROCESSED/CATALOG while still having no public release edge.

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `domain_feature_identity.schema.json` beyond `id`, `version`, and `spec_hash`.
- [ ] Decide exact field names for `source_id`, `object_role`, `temporal_scope`, `intrinsic_key_set`, and EvidenceRef/EvidenceBundle closure.
- [ ] Add valid fixtures for at least GeologicUnit, BoreholeReference, WellLogReference, MineralOccurrence, ResourceDeposit, ResourceEstimate, StructureFeature, and HydrostratigraphicUnit identity cases.
- [ ] Add invalid fixtures for hash mismatch, missing EvidenceBundle, missing source ID, source-role collapse, temporal collapse, restricted geometry public without receipt, candidate identity published, synthetic identity without representation receipt, aggregate-to-record join, and occurrence/deposit/estimate equality.
- [ ] Implement or verify `tools/validators/domains/geology/validate_domain_feature_identity.py`.
- [ ] Add policy tests proving public clients never read RAW/WORK/QUARANTINE identities as authoritative public truth.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for correction, rollback, merge, split, naming-drift registration, and schema-version rotation.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Source, role, temporal scope, spec hash, evidence closure, policy/release state all resolve | `ANSWER` / public-safe identity carrier may be used |
| Evidence, source role, temporal scope, rights, policy, or release support is incomplete | `ABSTAIN` |
| Identity collapse, hash mismatch, restricted leak, unreviewed candidate, synthetic-as-observed, or public bypass occurs | `DENY` |
| Schema, validator, hash, source-read, evidence-resolution, or release-runtime failure occurs | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms this target file existed as a greenfield scaffold before replacement. | Does not prove contract maturity. |
| Confirmed paired schema stub | Confirms schema path, `$id`, `x-kfm` pointers, and current minimal fields. | Does not prove field-level validation or validator implementation. |
| Geology Identity Model | Confirms identity formula, seven source-role meanings, six time dimensions, JCS/SHA-256 posture, lifecycle identity handling, sensitivity guards, cross-lane relations, and failure outcomes as doctrine/proposed implementation. | Some paths/field realizations are marked PROPOSED / NEEDS VERIFICATION in that source. |
| Geology Object Families | Confirms shared identity rule and object-family intrinsic key patterns. | Field realization remains PROPOSED. |
| Geology Scope | Confirms owned/not-owned lane boundaries and cross-lane exclusions. | Does not prove runtime enforcement. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized `domain_feature_identity` weakens deterministic identity, hides evidence gaps, collapses roles or object families, leaks restricted carriers, or makes public claims without release support.

Rollback triggers include:

- schema field names or hash algorithm are superseded by ADR/schema PR;
- `spec_hash` changes because of non-meaning-bearing serialization drift;
- identity-bearing field was excluded from normalized spec;
- transport-only field was included in normalized spec and caused false rotation;
- EvidenceRef cannot resolve to EvidenceBundle;
- EvidenceRef hash and EvidenceBundle hash mismatch;
- source role, temporal scope, sensitivity state, or rights state was collapsed;
- restricted exact geometry or payload entered public identity carrier without receipt;
- occurrence/deposit/estimate, structure/hazards, hydrostratigraphy/hydrology, or extraction/title identities were equated;
- public API/UI/AI reads RAW/WORK/QUARANTINE/candidate identities as authoritative truth.

Rollback artifacts should include affected identity IDs, previous/new `spec_hash`, source IDs, intrinsic key sets, temporal scope, object role, evidence refs, bundle refs, policy decisions, receipts, validation reports, release manifests, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which fields must be required in `domain_feature_identity.schema.json` beyond `id`? | NEEDS VERIFICATION | Schema PR and validator fixture review. |
| Is `object_role` the same field as `source_role`, or should identity use a narrower object-role wrapper that includes source role? | NEEDS VERIFICATION | Source/identity ADR. |
| Which exact canonicalization library/tool is accepted for JCS/SHA-256 in repo validators? | NEEDS VERIFICATION | Tooling inspection and validator PR. |
| How should URDNA2015 graph-bundle hashes coexist with JCS descriptor hashes? | NEEDS VERIFICATION | Canonicalization standard / ADR. |
| Which naming-drift events are non-rotating aliases versus true identity rotation? | NEEDS VERIFICATION | Drift register and object-family ADR. |
| How should merge/split/supersession identities be represented in triplets and release manifests? | NEEDS VERIFICATION | Graph/catalog/release schema review. |
| Which public-safe identity carriers are allowed for restricted geometries and LAS/log payloads? | NEEDS VERIFICATION | Policy, sensitivity, receipt, and release fixture review. |

---

## Related contracts and docs

- `docs/domains/geology/IDENTITY_MODEL.md` — identity doctrine and detailed mechanics.
- `docs/domains/geology/OBJECT_FAMILIES.md` — shared identity rule and intrinsic key profiles.
- `docs/domains/geology/SCOPE.md` — owned/not-owned Geology boundary.
- `contracts/domains/geology/README.md` — Geology contract lane orientation.
- `schemas/contracts/v1/domains/geology/domain_feature_identity.schema.json` — confirmed schema stub, pending expansion.
- `fixtures/domains/geology/domain_feature_identity/` — schema-declared fixture root, pending verification.
- `tools/validators/domains/geology/validate_domain_feature_identity.py` — schema-declared validator path, pending verification.
- `policy/domains/geology/` — expected policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Expand paired schema with required identity-bearing fields.
- [ ] Verify or create validator and fixtures referenced by the schema `x-kfm` block.
- [ ] Add anti-collapse tests for source-role, temporal, resource, subsurface, structure/hazards, hydrostratigraphy/hydrology, extraction/title, candidate, synthetic, and aggregate/per-place failures.
- [ ] Confirm EvidenceRef → EvidenceBundle resolution and hash mismatch behavior.
- [ ] Confirm public map/API/UI/AI surfaces use only released public-safe identity carriers.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved naming/hash/schema/source-role drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
