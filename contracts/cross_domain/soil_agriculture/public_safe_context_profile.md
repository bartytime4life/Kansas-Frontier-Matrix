<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/cross-domain/soil-agriculture/public-safe-context-profile
title: Soil–Agriculture Public-Safe Context Candidate Profile
type: contract; cross-domain assessment profile
version: v0.2.0
status: proposed; fixture-first; no-network; non-authoritative
created: 2026-08-14
updated: 2026-09-08
policy_label: repository-facing; public-safe; sensitivity-aware; non-publisher
owning_root: contracts/
responsibility: Define the bounded meaning, ownership, finite outcomes, and non-effects of a synthetic Soil-to-Agriculture context candidate without creating suitability, yield, relationship-truth, policy, review, release, or publication authority.
truth_posture: cite-or-abstain
related:
  - ../../joins/cross_lane_join_assessment.md
  - ../../../tools/validators/cross_domain/soil_agriculture/validate_public_safe_context.py
  - ../../../fixtures/contracts/v1/joins/soil_agriculture_public_safe_context/cases.json
  - ../../../tests/cross_domain/soil_agriculture/test_public_safe_context.py
  - ../../../control_plane/cross_domain_seam_register.yaml
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "ALLOW means only that the generic helper emitted a reviewable candidate and the pair validator accepted its declared synthetic fixture posture."
  - "The proposed seam projection remains HOLD_UNRESOLVED with public_join_allowed false; this profile does not resolve that hold or register a canonical seam identity."
  - "No coordinate or geometry payload, live source, lifecycle write, EvidenceBundle creation, policy or review decision, release decision, public route, or publication is in scope."
[/KFM_META_BLOCK_V2] -->

# Soil–Agriculture Public-Safe Context Candidate Profile

## Status and purpose

**PROPOSED.** This profile defines the pair-specific meaning of the existing, deterministic, fixture-first `CrossLaneJoinAssessment` for one synthetic Soil-to-Agriculture context candidate. It checks whether already-generalized references are internally coherent enough to continue to later review. It does not establish soil suitability for a crop, observed crop or yield behavior, farm or operator identity, causation, a canonical relation, an EvidenceBundle, policy permission, review approval, release, or a public claim.

Version `v0.2.0` reconciles the prose with the current generic join contract, the executable pair validator and seven-case fixture matrix, accepted Directory Rules, and the proposed cross-domain seam projection. It changes no schema, fixture, validator, test, workflow, source, policy, lifecycle object, release object, or public behavior.

## Evidence and authority boundary

Current repository authority wins when planning or coordination sources differ:

- [`CrossLaneJoinAssessment`](../../joins/cross_lane_join_assessment.md) defines deterministic identity, finite generic outcomes, source-role preservation, sensitivity inheritance, temporal-boundary handling, alias-dependency failure, and non-publisher effects.
- The pair [validator](../../../tools/validators/cross_domain/soil_agriculture/validate_public_safe_context.py), [fixtures](../../../fixtures/contracts/v1/joins/soil_agriculture_public_safe_context/cases.json), and [tests](../../../tests/cross_domain/soil_agriculture/test_public_safe_context.py) define the executable fixture profile. Documentation does not override those bytes.
- The proposed [`cross_domain_seam_register`](../../../control_plane/cross_domain_seam_register.yaml) records `agriculture--soil--suitability-context` as `HOLD_UNRESOLVED`, sets `public_join_allowed` to `false`, and leaves `seam_contract_path` unset. It is a navigational and review projection only; neither the register nor this profile authorizes a public join.
- The Soil architecture report preserves MUKEY/source lineage, distinguishes authoritative static survey support from gridded derivatives, and requires visible aggregation methods, rights, and limitations. It is planning and lineage evidence, not repository or publication authority.
- Notion coordination material preserves the domain boundary: Soil owns soil map units, components, horizons, properties, and soil-source authority; Agriculture owns agricultural observations and crop/yield context. It also keeps rights and public reuse at `NEEDS VERIFICATION`.
- Google Drive metadata confirms the Soil architecture report and revised Agriculture implementation dossier are private, owner-held planning artifacts. Access or ownership metadata does not grant public reuse, derivative-publication, or source-activation permission.

No external planning source can relax the repository's fail-closed behavior or elevate a fixture result into truth.

## Directory Rules and path posture

Accepted ADR-0029 adopts Directory Governance Standard v2. The adopted rules place cross-domain semantic meaning under `contracts/cross_domain/<seam_id>/`, shared validators under `tools/validators/cross_domain/<seam_id>/`, tests under `tests/cross_domain/<seam_id>/`, and reusable synthetic inputs under `fixtures/`.

This update is a same-path semantic refinement of the existing `contracts/cross_domain/soil_agriculture/` lane. It does **not** assert that `soil_agriculture` is the accepted canonical seam ID. The current projection instead names `agriculture--soil--suitability-context`, but that projection is proposed, incomplete, and held. Renaming or moving the contract would require accepted identity, consumer mapping, compatibility analysis, and a bounded migration; none occurs here. No new root or parallel contract, schema, policy, proof, receipt, release, or publication home is introduced.

## Atomic ownership and output role

| Concern | Authority retained by | Candidate use |
|---|---|---|
| Soil map units, components, horizons, properties, MUKEY lineage, and soil support type | Soil | Referenced as synthetic context only; no soil fact is rewritten. |
| Agricultural observations, crop context, yield context, aggregation, farm/operator privacy, and agriculture source role | Agriculture | Referenced as synthetic aggregate context only; no field, farm, operator, or yield fact is created. |
| Pair assessment | This pair profile plus the generic join contract | Validates a `CANDIDATE_RELATION`; it owns neither endpoint and creates no canonical relation. |
| Policy, review, proof, release, and publication | Their separate governing roots and accountable actors | Mandatory later gates; never inferred from `ALLOW`, validation success, a pull request, or a merge. |

Soil is the left endpoint and Agriculture the right endpoint only for deterministic fixture behavior and finding paths. Ordering transfers no authority.

## Required candidate posture

| Element | Required or bounded value | Meaning |
|---|---|---|
| `relation_profile_ref` | `kfm:relation-profile:soil-agriculture-public-safe-context:v1` | Fixture-profile identity; not the canonical seam-register identity. |
| Predicate | `SPATIAL_TEMPORAL` | Synthetic spatial-cell and valid-time comparison; not a geometry engine. |
| Temporal tolerance | `0` seconds | Genuine overlap is eligible; boundary-touch alone abstains under the generic contract. |
| Endpoint domains | left `soil`; right `agriculture` | Deterministic pair routing; contradictory domain declarations fail pair validation. |
| References | `kfm:fixture:` object, source-descriptor, spatial-cell, and optional EvidenceRef values | No live URL, coordinate, geometry payload, or production identifier is admitted. |
| Positive-fixture roles | `OBSERVED` / `OBSERVED` | Frozen baseline only. It does not establish a repository-wide role crosswalk. |
| Positive-fixture sensitivity and precision | both `PUBLIC_SAFE` and `GENERALIZED` | Declared fixture posture only; public-use authorization remains false. |
| Output role | `CANDIDATE_RELATION` | Review candidate, never relationship truth. |
| Effects | every generic effect is `false` | No lifecycle, evidence, policy, review, release, publication, or public-use effect. |

## Pair rules

1. The generic join assessment must be structurally coherent before pair-specific checks run.
2. Both endpoints retain their object, source-descriptor, source-role, EvidenceRef, sensitivity, precision, spatial-cell, and valid-time declarations.
3. Missing EvidenceRefs are permitted only so the generic result can `ABSTAIN`; an `ALLOW` declaration with missing evidence fails pair validation.
4. Any living-person state is denied by the generic assessment and is also invalid for this pair profile.
5. `ALLOW / JOIN_CANDIDATE` requires both endpoints to be `PUBLIC_SAFE`, `GENERALIZED`, evidence-bearing, spatial-temporally matched, and non-publishing.
6. Restricted exact geometry remains `DENY`. Restricted generalized context remains `ABSTAIN` for sensitivity review. An `ALLOW` declaration using public-safe but exact precision fails pair validation.
7. The generic helper sends every unequal source-role vector to `ABSTAIN / SOURCE_ROLE_REVIEW_REQUIRED`. Equal raw values may proceed through the generic check, but this pair profile creates no role-equivalence authority. The frozen positive case remains `OBSERVED` / `OBSERVED`.
8. A zero-tolerance interval that only touches at a boundary remains `ABSTAIN / NO_JOIN_CANDIDATE`; this profile does not invent inclusive interval semantics.
9. Loss, corruption, unsafe indirection, or identity mismatch of the generic domain-alias projection remains `ERROR / VALIDATOR_SYSTEM_ERROR`; absence of the review signal is never interpreted as permission.
10. Private farm, operator, parcel, or yield linkage is prohibited semantically. The current pair validator specifically rejects `private-farm`, `operator`, or `parcel` tokens in an Agriculture `object_ref` that otherwise declares `ALLOW`; broader reconstruction and yield semantics still require policy, privacy review, and negative-case expansion before any widened use.
11. Soil properties may contextualize an agricultural question, but they cannot be relabeled as observed crop suitability, management advice, yield, ownership, or causation.
12. Aggregated or generalized output must preserve source roles, temporal basis, geography/precision disclosure, aggregation method where applicable, rights posture, limitations, and endpoint evidence references through every later gate.

## Finite outcomes

| Outcome | Meaning in this profile | Required next route |
|---|---|---|
| `ALLOW / JOIN_CANDIDATE` | The declared synthetic candidate passed the generic assessment and pair-specific fixture checks. | Pair/domain review, EvidenceBundle resolution, policy, rights, sensitivity, release, and publication gates remain outstanding. |
| `ABSTAIN / NO_JOIN_CANDIDATE` | Predicate mismatch, same-domain routing, unresolved alias review, or ambiguous zero-tolerance boundary prevents a generic candidate. | Route to the named domain, alias, or temporal authority; do not coerce to `ALLOW`. |
| `ABSTAIN / EVIDENCE_REF_MISSING` | One or both endpoint EvidenceRefs are absent. | Resolve evidence or remain abstained. |
| `ABSTAIN / SOURCE_ROLE_REVIEW_REQUIRED` | The raw endpoint role values differ. | Participating-domain authority must define compatibility; the generic helper cannot. |
| `ABSTAIN / SENSITIVITY_REVIEW_REQUIRED` | Restricted generalized context requires review. | Preserve the more restrictive posture and route to sensitivity policy/review. |
| `DENY / LIVING_PERSON_JOIN_DENIED` | A living-person declaration blocks the candidate. | Do not emit a relation. |
| `DENY / GEOMETRY_PRECISION_BLOCKED` | Restricted exact geometry blocks the candidate. | Do not generalize implicitly or emit a relation. |
| `ERROR / VALIDATOR_SYSTEM_ERROR` | A declared dependency or the bounded alias-review projection cannot be safely used. | Repair the dependency and rerun; absence is not permission. |
| Pair validation `FAIL` | The document contradicts the required profile, fixture-only boundary, or `ALLOW` invariants. | Correct the declaration or preserve the generic non-allow outcome; no relation is created. |

The pair validator reports validation coherence separately from the generic decision. A `PASS` pair-validation result confirms only that the assessment and its finite outcome agree with this fixture profile; it does not mean the underlying relation is true or publicly admissible.

## Current executable fixture coverage

The frozen matrix contains seven deterministic cases:

1. public-safe generalized candidate;
2. restricted exact Soil geometry denial;
3. missing Soil EvidenceRef abstention;
4. modeled Agriculture role mismatch abstention;
5. private-farm/parcel Agriculture context denial;
6. public-safe exact Soil precision pair-profile failure;
7. wrong relation-profile pair-profile failure.

The focused tests also assert deterministic sealing, non-publishing effects, absence of coordinate/geometry payload keys and live URLs in the base fixture, and absence of network clients or write paths in the pair validator. This is fixture-level conformance, not live-source, policy, renderer, release, or publication proof.

## Known holds and required expansion before wider use

- Canonical seam identity and path mapping remain unresolved; the proposed seam register is not acceptance authority.
- `public_join_allowed` remains `false`; no caller may use this profile as a public-join permission.
- Source rights, attribution, reuse terms, and derivative-publication permission remain `NEEDS VERIFICATION` for any real source.
- The current validator's token guard is not a complete reconstruction-risk, farm/operator/privacy, or yield-policy engine.
- The current fixture set does not prove county/HUC aggregation thresholds, k-anonymity, small-cell suppression, multi-layer reconstruction resistance, suitability methodology, agronomic validity, or advice safety.
- No live EvidenceRef resolution, EvidenceBundle closure, policy bundle, reviewer identity, release manifest, correction propagation, rollback drill, governed API, MapLibre layer, Evidence Drawer projection, or Focus Mode response is exercised.

Any implementation widening must add the owning contract/schema/policy changes, deterministic positive and negative fixtures, validator behavior, consumer impact, migration/compatibility analysis, and rollback appropriate to that scope. It must not silently convert a proposed fixture profile into public relationship authority.

## Non-effects

This profile does not:

- activate, retrieve, admit, or redistribute a source;
- ingest, transform, generalize, aggregate, or emit geometry or data;
- resolve an EvidenceRef or create an EvidenceBundle;
- evaluate policy, assign a reviewer, or record approval;
- write `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`, `TRIPLETS`, or `PUBLISHED` state;
- create a proof, receipt, PromotionDecision, ReleaseManifest, correction notice, withdrawal, or rollback record;
- authorize agricultural advice, crop suitability, yield inference, farm/operator identification, or causal claims;
- authorize a governed API, MapLibre layer, Evidence Drawer payload, Focus Mode answer, export, release, deployment, promotion, publication, or public use.

## Acceptance and rollback

Review of this documentation update requires focused Markdown structure and relative-link checks, semantic comparison with the current generic contract, validator, fixtures, tests, seam projection, and accepted Directory Rules, plus exact-head diff readback. Because executable behavior is unchanged, broader implementation tests are proportionately not proof of this prose; the existing pair and generic regression suites remain required before any later implementation or release transition relies on the profile.

Rollback is a focused revert of this documentation change. It restores the prior profile bytes and does not mutate the generic join contract, schema, helper, pair validator, fixtures, tests, policy, data, release state, or public surface.
