<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-domain-feature-identity
title: Domain Feature Identity Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Identity steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Sensitivity reviewer
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-22
updated: 2026-06-22
policy_label: public-with-gates; semantic-contract; habitat; identity; deterministic-identity; source-role-aware; temporal-scope-aware; evidence-bound; release-gated; anti-collapse
tags: [kfm, contracts, habitat, domain_feature_identity, DomainFeatureIdentity, deterministic-identity, spec-hash, source-role, object-role, temporal-scope, evidence-ref, evidence-bundle, policy, sensitivity, release, correction, rollback]
related:
  - ./README.md
  - ./SuitabilityModel.md
  - ./connectivity_edge.md
  - ./corridor.md
  - ./land_cover/observation.md
  - ./land_cover/class_scheme.md
  - ./land_cover/crosswalk.md
  - ./land_cover/change_summary.md
  - ./land_cover/model_run_receipt.md
  - ./land_cover/uncertainty.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../schemas/contracts/v1/domains/habitat/domain_feature_identity.schema.json
  - ../../../policy/domains/habitat/
  - ../../../policy/sensitivity/habitat/
  - ../../../fixtures/domains/habitat/domain_feature_identity/
  - ../../../tests/domains/habitat/domain_feature_identity/
  - ../../../data/registry/sources/habitat/
  - ../../../release/manifests/habitat/
notes:
  - "Expanded from a greenfield scaffold at contracts/domains/habitat/domain_feature_identity.md."
  - "The paired schema exists at schemas/contracts/v1/domains/habitat/domain_feature_identity.schema.json, but it is still a PROPOSED scaffold that only defines spec_hash, id, and version, requires id, and allows additionalProperties=true; field-level enforcement remains NEEDS VERIFICATION."
  - "Habitat doctrine defines canonical object-family identity as source id + object role + temporal scope + normalized digest; this contract turns that shared rule into a domain-level identity support contract."
  - "DomainFeatureIdentity is an identity envelope/support object. It is not a HabitatPatch, LandCoverObservation, SuitabilityModel, ConnectivityEdge, Corridor, EvidenceBundle, PolicyDecision, ReleaseManifest, public layer, or AI answer by itself."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Feature Identity — Habitat

> Semantic contract for Habitat `DomainFeatureIdentity`: the support object that records deterministic identity, source role, object role, temporal scope, digest basis, evidence linkage, correction lineage, and anti-collapse posture for Habitat object families.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Object: DomainFeatureIdentity" src="https://img.shields.io/badge/object-DomainFeatureIdentity-blue">
  <img alt="Identity: deterministic" src="https://img.shields.io/badge/identity-deterministic-6f42c1">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: identity not truth" src="https://img.shields.io/badge/boundary-identity__not__truth-critical">
</p>

`contracts/domains/habitat/domain_feature_identity.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Identity formula](#identity-formula) · [Identity vs trust objects](#identity-vs-trust-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Object-family profiles](#object-family-profiles) · [Source-role rules](#source-role-rules) · [Temporal rules](#temporal-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/habitat/domain_feature_identity.md`  
> **Schema path:** `schemas/contracts/v1/domains/habitat/domain_feature_identity.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` scaffold that defines only `spec_hash`, `id`, and `version`, requires only `id`, and allows `additionalProperties: true`.  
> **Truth posture:** Habitat doctrine confirms the shared identity rule for canonical object families: `source id + object role + temporal scope + normalized digest`, with source / observed / valid / retrieval / release / correction times kept distinct. Field-level schema shape, fixtures, validators, source registries, policy runtime, release artifacts, map/UI behavior, Focus Mode behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `DomainFeatureIdentity` makes identity inspectable; it does not make a claim true. EvidenceBundle support, source-role review, policy decision, validation, release state, correction lineage, and rollback still govern whether a claim may be answered, rendered, exported, or published.

---

## Meaning

`DomainFeatureIdentity` records how a Habitat object is identified and distinguished from other Habitat or cross-lane objects.

It answers:

- Which source or source-derived support participates in identity?
- Which object family and object role are being identified?
- Which temporal scope is material to identity?
- Which normalized digest or `spec_hash` fixes the identity-relevant content?
- Which source role prevents the object from being mislabeled as observed, modeled, regulatory, aggregate, administrative, candidate, or synthetic?
- Which EvidenceRefs, EvidenceBundles, PolicyDecisions, ReleaseManifests, CorrectionNotices, and RollbackCards govern consequential use?

It exists to prevent identity collapse: a modeled suitability surface must not become a regulatory critical-habitat designation; a land-cover observation must not become a species occurrence; a corridor must not become observed animal movement or a transport route; and a public map tile must not become canonical truth.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Habitat identity semantics | `contracts/domains/habitat/domain_feature_identity.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/habitat/domain_feature_identity.schema.json` | CONFIRMED scaffold; field shape not enforced |
| Habitat domain doctrine | `docs/domains/habitat/README.md` | Defines object-family spine, temporal handling, lifecycle, sensitivity, cross-lane rules |
| Source-role doctrine | `docs/domains/habitat/MODEL_VS_OBSERVATION.md` | Defines observed/model/regulatory/derivative/context role separation |
| Source registry | `data/registry/sources/habitat/` | Source identity, role, rights, cadence, activation |
| Policy | `policy/domains/habitat/`, `policy/sensitivity/habitat/` | Allow/restrict/deny/abstain behavior and sensitivity posture |
| Fixtures and tests | `fixtures/domains/habitat/domain_feature_identity/`, `tests/domains/habitat/domain_feature_identity/` | PROPOSED / NEEDS VERIFICATION |
| Release | `release/` / `release/manifests/habitat/` | Publication, correction, rollback authority; not owned here |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/habitat/domain_feature_identity.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `domain_feature_identity` |
| Visible properties | `spec_hash`, `id`, `version` |
| Required fields | `id` only |
| Additional properties | `true` |
| Field-level validation | NEEDS VERIFICATION |
| Contract pointer | `contracts/domains/habitat/domain_feature_identity.md` |
| Fixtures root pointer | `fixtures/domains/habitat/domain_feature_identity/` |
| Validator pointer | `tools/validators/domains/habitat/validate_domain_feature_identity.py` |
| Policy pointer | `policy/domains/habitat/` |

Until the schema expands and validators/fixtures are confirmed, this contract is semantic guidance and review vocabulary only.

---

## Identity formula

Habitat doctrine uses a shared identity basis for canonical object families:

```text
identity = normalize(source_id + object_role + temporal_scope + normalized_digest)
```

This contract refines that formula for Habitat by requiring identity to preserve:

- `source_id` — source descriptor, admitted source, or derived source family;
- `source_role` — observed, modeled, regulatory, aggregate, administrative, candidate, synthetic, derivative, or context posture;
- `object_family` — HabitatPatch, LandCoverObservation, SuitabilityModel, ConnectivityEdge, Corridor, or another reviewed Habitat family;
- `object_role` — the object's role in the Habitat trust model;
- `temporal_scope` — source, observed, valid, retrieval, release, and correction times where material;
- `normalized_digest` / `spec_hash` — digest over identity-relevant content.

> [!WARNING]
> If two objects need different source roles, they need different identities. A file, layer, API response, or map style that blends observed, modeled, regulatory, derivative, aggregate, or candidate claims into one identity should fail closed.

---

## Identity vs trust objects

| Object / artifact | What it owns | Relationship to `DomainFeatureIdentity` |
|---|---|---|
| `DomainFeatureIdentity` | Stable identity semantics and anti-collapse posture. | This contract. |
| `SourceDescriptor` | Source identity, rights, role, cadence, and authority limits. | Identity depends on source admission. |
| `EvidenceBundle` | Evidence support for claims. | Identity may cite it; identity is not proof. |
| `ValidationReport` | Validator findings. | Identity may be validated; it does not validate itself. |
| `PolicyDecision` | Allow/restrict/deny/abstain. | Identity may route to policy; it is not policy. |
| `ReviewRecord` | Steward review. | Identity may be reviewed; it is not review approval. |
| `ReleaseManifest` / `PromotionDecision` | Publication authority. | Identity may support release; it does not publish. |
| `CorrectionNotice` / `RollbackCard` | Correction lineage and reversal target. | Identity must preserve correction lineage. |
| Public layer / tile / popup / AI answer | Delivery/interpretive surface. | Must reference released identity/evidence; not root truth. |

---

## Assertions

A reviewed `DomainFeatureIdentity` should semantically assert:

1. **Canonical identity** — a stable identifier derived from source, role, time, and digest.
2. **Object family** — one accepted Habitat object family or explicitly reviewed support object.
3. **Source role** — observed, modeled, regulatory, aggregate, administrative, candidate, synthetic, derivative, or context posture, with no silent role upgrade.
4. **Object role** — object-specific role such as patch, observation, class scheme, crosswalk, suitability model, connectivity edge, corridor, stewardship zone, or uncertainty surface.
5. **Temporal scope** — source / observed / valid / retrieval / release / correction times kept distinct where material.
6. **Digest basis** — normalized content basis and `spec_hash` or equivalent digest support.
7. **Evidence linkage** — EvidenceRef/EvidenceBundle refs required before consequential use.
8. **Policy linkage** — policy decision refs where rights, sensitivity, role collapse, or release posture is material.
9. **Release linkage** — release, correction, and rollback refs before public use.
10. **Anti-collapse posture** — explicit denial of nearby false identities.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating identity as evidence | EvidenceBundle carries evidence support; identity only labels and links. |
| Treating identity as release | ReleaseManifest / PromotionDecision owns publication. |
| Treating identity as policy | PolicyDecision owns allow/restrict/deny/abstain. |
| Treating one ID as multiple roles | Role collapse hides source authority and uncertainty. |
| Treating modeled as observed | Hides assumptions, model card, receipt, and uncertainty. |
| Treating modeled as regulatory | Invents authority KFM does not have. |
| Treating aggregate as precise | Public-safe aggregates do not imply exact geometry. |
| Treating candidate as published | Candidate objects remain WORK/QUARANTINE or review state only. |
| Treating public tile as canonical ID | Tiles are downstream carriers and may be regenerated. |
| Treating AI answer as identity source | AI is interpretive and evidence-subordinate. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM identity ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized digest over identity-relevant content. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | Habitat object family being identified. |
| `object_role` | Role inside Habitat trust model. |
| `source_id` | Stable source/source-derived handle. |
| `source_descriptor_ref` | Source identity, role, rights, cadence, attribution, authority limits. |
| `source_role` | Observed, modeled, regulatory, aggregate, administrative, candidate, synthetic, derivative, context, or accepted enum. |
| `identity_formula_version` | Version of deterministic identity formula. |
| `normalized_digest` | Digest over canonicalized identity inputs. |
| `canonicalization_profile_ref` | Rules used to normalize identity-relevant content. |
| `temporal_scope_ref` | Structured time-scope object or refs. |
| `source_time` | Source publication/assertion time. |
| `observed_time` | Observation/acquisition time where applicable. |
| `valid_time` | Valid interval of the object claim. |
| `retrieval_time` | KFM retrieval/harvest time. |
| `release_time` | Public-safe release time, if released. |
| `correction_time` | Correction/supersession time, if corrected. |
| `geometry_fingerprint` | Geometry digest/fingerprint where geometry is identity-relevant. |
| `public_geometry_fingerprint` | Public-safe geometry fingerprint where generalized/redacted. |
| `evidence_refs` | EvidenceRef links. |
| `evidence_bundle_refs` | EvidenceBundle refs behind consequential use. |
| `validation_report_ref` | ValidationReport for identity determinism, schema, source role, sensitivity, and release readiness. |
| `policy_decision_ref` | PolicyDecision where material. |
| `review_record_ref` | Steward review record. |
| `release_ref` | ReleaseManifest or PromotionDecision ref. |
| `correction_refs` | CorrectionNotice, supersession, replacement identity refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Missing source, role conflict, time collapse, digest mismatch, geometry drift, candidate public edge, sensitivity unresolved, release missing. |

---

## Object-family profiles

| Family | Identity must preserve | Forbidden collapse |
|---|---|---|
| `HabitatPatch` | Patch source, geometry fingerprint, class/source role, temporal scope. | Patch is not occurrence, corridor, or regulatory designation. |
| `LandCoverObservation` | Source vintage, class scheme, spatial scope, valid-pixel support. | Observation is not model, crosswalk, or public layer. |
| `EcologicalSystem` | Classification system, source role, evidence and time. | System class is not occurrence proof. |
| `HabitatQualityScore` | Model/scoring method, patch ref, uncertainty, valid time. | Score is descriptive, never management instruction. |
| `SuitabilityModel` | Model ID/version, model card, receipt, uncertainty, source role. | Modeled habitat is not regulatory critical habitat. |
| `ConnectivityEdge` | Node pair, method, input refs, receipt, uncertainty. | Edge is not observed movement or transport corridor. |
| `Corridor` | Connectivity refs, geometry role, method, public-safe transform. | Corridor is not Fauna migration route or exact public movement path. |
| `RestorationOpportunity` | Candidate site, method/support, review state, temporal scope. | Opportunity is not approved action or land/title claim. |
| `StewardshipZone` | Administrative/stewardship source, role, rights, time. | Zone is not title/ownership truth. |
| `ModelRunReceipt` | Model/run/input/config/output digests and run time. | Receipt is not proof or release. |
| `UncertaintySurface` | Observation/model ref, uncertainty kind, artifact digest, temporal scope. | Uncertainty is not observation truth. |

---

## Source-role rules

| Role | Identity rule | Public-use posture |
|---|---|---|
| `observed` | Direct observation/inventory with source vintage and class/source system. | Public only after evidence, rights, policy, release. |
| `modeled` | Model output under assumptions with model card, receipt, uncertainty. | Must remain visibly modeled. |
| `regulatory` | Competent-authority designation recorded as designation. | Must not be relabeled as biological fact or modeled suitability. |
| `aggregate` | Public-safe rollup or summary with aggregation receipt. | Must not imply per-place precision. |
| `administrative` | Stewardship/management context, not land/title truth. | Requires rights/policy review before public exposure. |
| `candidate` | Unreviewed/candidate object. | No PUBLISHED edge. |
| `synthetic` | AI-generated/simulated/reconstructed content. | Not observed reality; public use requires strong labeling and review. |
| `derivative` | Derived from other objects with method and support. | Must carry upstream support and uncertainty. |
| `context` | Neighbor-lane context through governed join. | Ownership stays with source lane. |

---

## Temporal rules

Habitat identity must not collapse time dimensions.

| Time kind | Meaning | Identity risk if collapsed |
|---|---|---|
| `source_time` | When the source asserted or published the source record. | Stale source may look current. |
| `observed_time` | When the landscape, observation, image, field record, or source phenomenon was observed. | Source vintage and acquisition get confused. |
| `valid_time` | Interval during which the object claim is valid. | Old model/input may appear valid now. |
| `retrieval_time` | When KFM acquired the source artifact. | Harvest time may be mistaken for observation. |
| `release_time` | When a public-safe artifact was released. | Running or ingesting an object may look like publication. |
| `correction_time` | When correction/supersession happened. | Superseded identities may remain public. |

---

## Sensitivity and release

Identity can itself become sensitive when it encodes exact geometry, source joins, rare-species context, protected-resource context, private stewardship, or living-person/land/title-adjacent detail.

Rules:

- Sensitive identity components must be generalized, redacted, restricted, delayed, or denied before public release.
- Public-safe identity may need separate public geometry fingerprint or aggregate identity from internal exact identity.
- Source-role, rights, sensitivity, validation, review, release, correction, and rollback refs must resolve before public clients use identity-bearing objects.
- Public UI/AI must show role labels and cannot use identity strings to imply stronger authority than evidence supports.
- Public clients use governed APIs and released artifacts, not RAW/WORK/QUARANTINE/candidate identity objects.

---

## Lifecycle

| Phase | Identity handling |
|---|---|
| RAW | Source IDs, source records, source times, observed times, rights, sensitivity, and hashes are captured but not public truth. |
| WORK / QUARANTINE | Candidate identities are normalized; role conflicts, time collapse, digest mismatch, rights gaps, and sensitivity failures are held with reasons. |
| PROCESSED | Reviewed identities bind source role, object role, temporal scope, digest, evidence refs, validation report, policy posture, and correction state. |
| CATALOG / TRIPLET | Identity may support catalog/triplet projection only with EvidenceBundle refs and source-role caveats. |
| RELEASE CANDIDATE | Public identity, public geometry fingerprint, API payload, layer refs, and Focus Mode references require policy/review, release manifest, correction path, and rollback target. |
| PUBLISHED | Only released public-safe identities appear through governed APIs, map surfaces, Evidence Drawer, Focus Mode, or reports. |
| CORRECTED / SUPERSEDED | Source update, role correction, geometry correction, digest correction, time correction, policy change, or sensitivity review triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/habitat/domain_feature_identity.schema.json` beyond `id`, `version`, and `spec_hash`.
- [ ] Confirm accepted source-role enum values and any aliases such as `model` vs `modeled`.
- [ ] Add valid fixtures for each Habitat object family and support object.
- [ ] Add invalid fixtures for modeled-as-observed, modeled-as-regulatory, aggregate-as-exact, candidate-as-published, derivative-without-receipt, context-with-ownership-collapse, time-collapse, digest mismatch, sensitive-exact public identity, and missing rollback target.
- [ ] Add validator checks for deterministic identity, source role, object role, temporal scope, digest basis, evidence refs, policy refs, release refs, and correction lineage.
- [ ] Add tests proving public map/UI/AI surfaces cannot treat tiles, popups, vector indexes, graph projections, or generated text as root identity/truth.
- [ ] Confirm release tests proving public clients consume released public-safe identities only.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Source, role, object family, temporal scope, digest, evidence, policy, release, and rollback all resolve | `ANSWER` / public-safe identity may support a claim |
| Evidence, role, schema, rights, sensitivity, release, or rollback support is incomplete | `ABSTAIN` / `HOLD` |
| Role collapse, sensitive leak, candidate public path, or release bypass would occur | `DENY` |
| Schema, validator, source read, digest, evidence lookup, policy lookup, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current target scaffold | Confirms target existed as greenfield scaffold before replacement. | Does not prove contract maturity. |
| Paired schema scaffold | Confirms schema path and current limited schema posture. | Does not prove field-level validation. |
| Habitat README | Confirms object-family spine, shared identity basis, lifecycle gates, sensitivity, cross-lane rules, map/AI boundaries, and proposed tests. | Some implementation claims remain PROPOSED. |
| Model-vs-observation doc | Confirms observed/model/regulatory/derivative/context role separation and anti-collapse rules. | Some enforcement/policy details remain PROPOSED / NEEDS VERIFICATION. |
| Adjacent Habitat contracts | Provide current semantic contract patterns for land cover, suitability, connectivity, and corridor objects. | Recent contract content is semantic documentation, not schema enforcement. |
| User-provided authoring role | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized Habitat identity weakens deterministic identity, source-role separation, temporal discipline, sensitivity, or release integrity.

Rollback triggers include:

- identity formula changes without migration note or ADR;
- schema or contract path changes without updating pointers and related docs;
- role aliases collapse modeled, observed, regulatory, derivative, aggregate, administrative, candidate, synthetic, or context objects;
- source, object role, temporal scope, geometry fingerprint, or digest is corrected;
- sensitive exact identity or geometry fingerprint leaks publicly;
- candidate identity appears in public API/UI/AI path;
- public map tile, popup, AI answer, graph projection, or vector index is treated as source identity;
- release, correction, or rollback refs are missing for public identity use.

Rollback artifacts should include affected identity IDs, object refs, source refs, source-role refs, temporal-scope refs, digest refs, geometry fingerprints, evidence refs, validation reports, policy decisions, release refs, correction notices, rollback cards, replacement identities, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which fields must be required in `domain_feature_identity.schema.json`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| Should source-role values use `model` or `modeled`, and where is the enum pinned? | NEEDS VERIFICATION | Source-role/schema/policy review. |
| Should Habitat have object-family-specific identity contracts or one shared identity profile? | NEEDS VERIFICATION | Contract steward + Habitat steward review. |
| How are public-safe identities linked to internal exact identities for sensitive geometry? | NEEDS VERIFICATION | Policy, redaction, and release design review. |
| Which tests prove candidate identity cannot become public truth? | NEEDS VERIFICATION | Fixture/test inspection. |
| How should identity correction invalidate public layers, graph edges, and Focus Mode cards? | NEEDS VERIFICATION | Release/runtime/cache invalidation design. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Habitat contracts root.
- [`./SuitabilityModel.md`](./SuitabilityModel.md) — modeled suitability identity and role boundary.
- [`./connectivity_edge.md`](./connectivity_edge.md) — derived connectivity edge identity.
- [`./corridor.md`](./corridor.md) — derived corridor geometry identity.
- [`./land_cover/observation.md`](./land_cover/observation.md) — land-cover observation identity.
- [`../../../docs/domains/habitat/README.md`](../../../docs/domains/habitat/README.md) — Habitat lane doctrine.
- [`../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md`](../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md) — source-role anti-collapse doctrine.
- [`../../../schemas/contracts/v1/domains/habitat/domain_feature_identity.schema.json`](../../../schemas/contracts/v1/domains/habitat/domain_feature_identity.schema.json) — confirmed scaffold schema, pending expansion.

[Back to top](#top)
