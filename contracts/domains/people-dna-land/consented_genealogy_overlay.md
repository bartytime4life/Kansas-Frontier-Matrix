<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/people-dna-land/consented-genealogy-overlay
title: Consented Genealogy Overlay Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; fixture-profile; restricted-review; not-released
owners:
  - OWNER_TBD - People/DNA/Land domain steward
  - OWNER_TBD - consent steward
  - OWNER_TBD - privacy steward
  - OWNER_TBD - evidence steward
  - OWNER_TBD - schema steward
  - OWNER_TBD - validation steward
  - OWNER_TBD - policy steward
  - OWNER_TBD - release steward
created: 2026-08-03
updated: 2026-08-03
policy_label: restricted-review; synthetic-fixture-only; consent-bound; revocation-aware; no-raw-dna; no-identifying-kit-id; no-exact-location; no-public-release
owning_root: contracts/
responsibility: Define the bounded meaning of a synthetic, non-identifying genealogy-overlay candidate and its fixture-only revocation-manifest dependency without creating person identity, kinship, DNA, consent, policy, evidence, release, or publication authority.
related:
  - ./README.md
  - ../../../docs/domains/people-dna-land/CONSENT_MODEL.md
  - ../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../../docs/runbooks/people-dna-land/CONSENT_RUNBOOK.md
  - ../../../policy/consent/people-dna-land/README.md
  - ../../../schemas/contracts/v1/domains/people-dna-land/consented_genealogy_overlay.schema.json
  - ../../../schemas/contracts/v1/domains/people-dna-land/genealogy_overlay_revocation_manifest.schema.json
  - ../../../fixtures/domains/people-dna-land/consent_overlay/README.md
  - ../../../tools/validators/domains/people-dna-land/validate_consent_overlay.py
  - ../../../tests/domains/people-dna-land/consent/revocation/test_consent_overlay_safety.py
tags: [kfm, contract, people-dna-land, genealogy, overlay, consent, revocation, privacy, synthetic-fixture, no-network, fail-closed]
notes:
  - "This contract implements a frozen synthetic fixture profile, not a production overlay or consent credential."
  - "The profile deliberately narrows disclosure to restricted/internal, release_state=not_released, public_exposure=false, and promotion_eligible=false."
  - "A passing fixture proves only that the bounded profile behaved as tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Consented Genealogy Overlay Candidate Contract

> **Purpose:** define one bounded, synthetic, non-identifying genealogy-overlay
> candidate shape that can be accepted or rejected deterministically in
> no-network tests. The contract exists to prove consent, revocation,
> deterministic-hash, evidence, spatial/temporal generalization, and non-release
> guardrails before any overlay producer or public surface is considered.

| Field | Value |
|---|---|
| Status | `PROPOSED` fixture profile |
| Owning responsibility root | `contracts/` - semantic meaning |
| Machine shapes | `schemas/contracts/v1/domains/people-dna-land/` |
| Validator | `tools/validators/domains/people-dna-land/validate_consent_overlay.py` |
| Fixtures | `fixtures/domains/people-dna-land/consent_overlay/` |
| Tests | `tests/domains/people-dna-land/consent/revocation/` |
| Exposure posture | restricted/internal fixture only |
| Release posture | `not_released`; never promotion-eligible |
| Network posture | no network |
| Real-person posture | denied |
| Raw-genomic posture | denied |

> [!IMPORTANT]
> **Consent is necessary where this profile requires it, but it is never
> sufficient for release.** A passing candidate still does not establish
> identity, kinship, source rights, sensitivity clearance, EvidenceBundle
> closure, policy approval, review approval, release approval, or publication.

> [!CAUTION]
> This contract must never be used with real names, real people, real kit or
> vendor identifiers, raw genotype/sequence/segment material, exact coordinates,
> addresses, parcels, deeds, or production consent credentials.

## 1. Meaning

`ConsentedGenealogyOverlayCandidate` is a fixture-only envelope for a
**non-identifying derived summary**. It can represent either:

1. a synthetic DNA-derived match summary that has active, scoped, time-bounded
   fixture consent; or
2. a synthetic documentary/historical genealogy context record for a
   deceased-or-historical subject posture, with no kit hash.

It is not:

- a canonical person record;
- a person-identity or kinship proof;
- a consent credential;
- a revocation execution record;
- raw or derived genomic evidence suitable for external use;
- a public map layer;
- a catalog item;
- a release candidate;
- a release manifest;
- an EvidenceBundle;
- a policy decision;
- a publication approval.

## 2. Bounded-context rules

The profile preserves these distinctions:

| Concept | Meaning in this profile | Must not collapse into |
|---|---|---|
| `subject_posture` | fixture declaration of `living_person`, `deceased_or_historical`, or unresolved | identity truth |
| `material_kind` | `dna_derived_summary` or `documentary_genealogy_context` | raw DNA or confirmed relationship |
| `kit_hash` | deterministic synthetic fixture token only | a vendor kit ID or public identifier |
| `consent` | fixture state used to exercise fail-closed rules | legal sufficiency or release approval |
| `revocation_root` | hash bound to a separate fixture manifest | proof that production revocation executed |
| `events` | coarse, non-identifying summary buckets | exact person, place, date, or relationship truth |
| `evidence_refs` | fixture-only references | resolved production EvidenceBundles |
| `spec_hash` | deterministic fixture integrity | source authority or release integrity |
| `governance` | explicit non-release fixture posture | promotion or publication state |

## 3. Required candidate fields

| Field | Requirement |
|---|---|
| `fixture_id` | `fixture://...` identity; no production identifier |
| `profile_id` | exact frozen profile ID |
| `object_family` | `ConsentedGenealogyOverlayCandidate` |
| `overlay_id` | `sha256:<64 lowercase hex>` |
| `spec_hash` | SHA-256 over canonical JSON excluding `spec_hash` |
| `evaluation_time` | timezone-aware ISO 8601 fixture time |
| `material_kind` | DNA-derived summary or documentary context |
| `subject_posture` | explicit living/historical/unresolved posture |
| `source_role` | exact `fixture_only` |
| `kit_hash` / `kit_salt_version` | required only for DNA-derived summary; fixture values only |
| `consent` | explicit state, hash, interval, scope, audience, and revocation ref |
| `revocation_root` | must match the separately validated fixture manifest |
| `events` | bounded coarse time/place summaries with evidence refs |
| `evidence_refs` | non-empty unique fixture refs |
| `disclosure_level` | restricted or internal only |
| `governance` | exact fixture-only, not-released state |
| `limitations` | exact non-authority and non-release limitations |

## 4. Consent rules

1. `living_person` requires `consent.status=active`.
2. `dna_derived_summary` requires active consent regardless of subject posture.
3. Active consent requires a synthetic token hash, issue time, expiry time,
   restricted-steward audience, and approved scope.
4. Evaluation time must be inside the active interval.
5. Revoked or expired consent fails closed.
6. `not_required` is allowed only for
   `deceased_or_historical + documentary_genealogy_context`.
7. A consent pass does not waive evidence, rights, sensitivity, review, release,
   correction, withdrawal, or rollback requirements.

## 5. Revocation-manifest rules

A candidate is invalid when:

- no revocation manifest is supplied;
- the manifest is malformed or its deterministic `spec_hash` fails;
- the candidate and manifest `revocation_root` values differ; or
- the candidate `overlay_id` appears in `revoked_overlay_ids`.

The fixture manifest does not execute deletion, withdrawal, cache invalidation,
graph cleanup, search cleanup, or publication rollback. It proves only that the
validator can fail closed on a manifest-bound revocation state.

## 6. Privacy and precision rules

The profile denies:

- cleartext or vendor kit identifiers;
- names, person IDs, email, phone, address, birth/death dates, or other
  identifying fields;
- raw DNA, genotype, sequence, segments, or triangulation material;
- latitude, longitude, coordinates, street addresses, or exact geometry;
- real county identifiers in fixtures;
- post-1900 time buckets narrower than ten years;
- high-confidence summary scores without at least two fixture evidence refs;
- public disclosure or released/promotion-eligible governance states.

All spatial fixtures use reserved non-real county sentinel `99999`.

## 7. Finite validation findings

The executable profile emits stable `{code, path}` findings and never includes
candidate values. Important findings include:

- `CONSENT_REQUIRED_FOR_LIVING_PERSON`
- `CONSENT_REQUIRED_FOR_DNA_DERIVATIVE`
- `CONSENT_EXPIRED`
- `REVOCATION_ACTIVE`
- `REVOCATION_MANIFEST_REQUIRED`
- `REVOCATION_ROOT_MISMATCH`
- `IDENTIFYING_KIT_FIELD_DENIED`
- `RAW_GENOMIC_MATERIAL_DENIED`
- `SENSITIVE_LOCATION_DENIED`
- `RECENT_TIME_BUCKET_TOO_PRECISE`
- `HIGH_CONFIDENCE_EVIDENCE_INSUFFICIENT`
- `EVIDENCE_REFS_INVALID`
- `GOVERNANCE_STATE_INVALID`
- `SPEC_HASH_MISMATCH`

A clean result means only that the fixture satisfied the frozen profile.

## 8. Lifecycle and authority boundary

This slice does not move any artifact through KFM lifecycle state:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

The fixture profile is test material. It performs no source access, admission,
normalization, catalog emission, proof closure, policy evaluation, review,
promotion, release, withdrawal, rollback, API delivery, MapLibre rendering, or
AI interpretation.

## 9. Validation and acceptance

The bounded profile is accepted for review when:

- both schemas are closed Draft 2020-12 shapes;
- valid synthetic fixtures pass;
- every frozen invalid fixture matches an exact sorted sidecar;
- revoked-manifest membership denies the candidate;
- deterministic hashes are stable under object-key reordering;
- malformed, duplicate-key, non-finite, oversized, and non-object JSON fail
  closed;
- diagnostics do not echo sensitive sentinel values;
- tests prove no network call occurs; and
- the existing People/DNA/Land workflow executes only this bounded profile while
  preserving broader proof and release holds.

## 10. Rollback and correction

Rollback is a normal revert of the feature commit. It removes the contract,
schemas, fixtures, validator, tests, workflow wiring, source map, and generated
receipt. It does not modify any source, real person record, consent record,
revocation system, lifecycle store, catalog, proof, release, cache, API, map,
search index, graph, AI context, or published artifact.

[Back to top](#top)
