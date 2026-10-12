<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-vegetation-community-readme
title: tools/validators/vegetation_community README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-flora-steward-plus-vegetation-community-steward-plus-habitat-steward-plus-taxonomy-steward-plus-sensitivity-reviewer-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; vegetation-community-validator-index; flora; habitat-boundary-aware; community-classification; polygonal-classification; floristic-composition; source-role-aware; taxonomy-aware; sensitivity-aware; geoprivacy-aware; release-gated; no-canonical-habitat-truth; non-authoritative
owning_root: tools/
responsibility: vegetation community validator routing README under tools/validators; documents validation expectations for Flora VegetationCommunity records, community-classification labels, classification systems and versions, polygon/plot/survey/model/aggregate support, floristic composition, dominant and indicator taxa, Flora/Habitat anti-collapse, taxonomy and crosswalk refs, source-role preservation, temporal scope, uncertainty and scale, sensitive rare-plant and rare-habitat inference, private-land stewardship, cultural/ecological sensitivity, redaction/generalization receipt linkage, evidence/proof linkage, policy/review/release posture, correction cascade, rollback support, public-surface denial, schema/fixture/test routing, and finite outcomes while deferring Flora meaning, Habitat meaning, taxonomy authority, canonical schemas, policy decisions, evidence records, receipts, lifecycle data, release records, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../taxonomy_resolver/README.md
  - ../source_role/README.md
  - ../sensitivity/README.md
  - ../sensitive_geometry/README.md
  - ../geoprivacy/README.md
  - ../rights/README.md
  - ../policy/README.md
  - ../release/README.md
  - ../promotion_gate/README.md
  - ../../../contracts/domains/flora/vegetation_community.md
  - ../../../contracts/domains/flora/plant_taxon.md
  - ../../../contracts/domains/flora/flora_taxon_crosswalk.md
  - ../../../contracts/domains/flora/habitat_association.md
  - ../../../contracts/domains/flora/range_polygon.md
  - ../../../contracts/domains/flora/botanical_survey.md
  - ../../../contracts/domains/flora/flora_occurrence.md
  - ../../../contracts/domains/flora/occurrence_public.md
  - ../../../contracts/domains/flora/occurrence_restricted.md
  - ../../../contracts/domains/flora/rare_plant_record.md
  - ../../../contracts/domains/flora/redaction_receipt.md
  - ../../../contracts/domains/habitat/ecological_system.md
  - ../../../contracts/domains/habitat/habitat_patch.md
  - ../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../docs/domains/flora/CROSSWALKS.md
  - ../../../docs/domains/flora/SENSITIVITY_POSTURE.md
  - ../../../docs/domains/flora/CROSS_LANE_NOTES.md
  - ../../../docs/domains/habitat/sublanes/ecological_systems.md
  - ../../../docs/domains/habitat/cross-domain.md
  - ../../../schemas/contracts/v1/domains/flora/vegetation_community.schema.json
  - ../../../schemas/contracts/v1/flora/README.md
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../policy/domains/habitat/
  - ../../../data/registry/sources/flora/
  - ../../../data/registry/sources/habitat/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
  - ../../../fixtures/domains/flora/vegetation_community/
  - ../../../tests/domains/flora/
notes:
  - "This README replaces an empty placeholder at tools/validators/vegetation_community/README.md. It does not confirm executable vegetation-community validators, registry wiring, schemas, fixtures, policy bundles, receipt emission, runtime behavior, or CI behavior."
  - "VegetationCommunity captures polygonal, plot-based, survey-derived, modeled, aggregate, or reviewed vegetation-community classification and floristic composition support. It does not replace HabitatAssociation, RangePolygon, BotanicalSurvey, FloraOccurrence, PlantTaxon, or Habitat EcologicalSystem."
  - "Vegetation community polygons can expose rare habitats, rare-plant search areas, private-land stewardship, source-restricted field notes, or culturally sensitive ecological context. Public use requires evidence, rights, sensitivity, policy, review, release, correction, and rollback support."
  - "Habitat EcologicalSystem is Habitat-owned classification context and is not Flora VegetationCommunity, occurrence truth, regulatory critical habitat, suitability, connectivity/corridor, management instruction, or release authority."
  - "No exact rare-plant locations, rare-habitat reconstruction hints, private stewardship details, cultural plant knowledge, redaction parameters, grid sizes, geohash precision, hidden policy thresholds, or restricted source values belong in this validator README."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/vegetation_community

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-vegetation__community--validator-informational)
![boundary](https://img.shields.io/badge/boundary-Flora%20%E2%89%A0%20Habitat-critical)
![posture](https://img.shields.io/badge/posture-release--gated-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/vegetation_community/` is the validator routing lane for Flora `VegetationCommunity` classification packets, checking community labels, taxonomy/crosswalk refs, floristic support, source-role preservation, Habitat anti-collapse, sensitivity, evidence, policy, release, correction, rollback, and public-surface denial without becoming ecology truth, Habitat truth, taxonomy authority, or publication authority.

---

## Purpose

`tools/validators/vegetation_community/` exists to make vegetation-community validation visible under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a vegetation community candidate preserve the difference between a Flora community-classification claim, plant taxon support, occurrence support, survey support, Habitat ecological-system context, public-safe geometry, rare-habitat and rare-plant sensitivity, source-role limits, taxonomy/crosswalk refs, evidence support, policy/review posture, release reference, correction path, rollback target, and public-surface limits?

The answer should be a deterministic validation result or routing decision. This folder should not define Flora meaning, define Habitat meaning, author taxonomy records, create occurrence proof, certify habitat truth, decide policy, create EvidenceBundles, write receipts, store lifecycle data, approve release, publish map layers, expose public API payloads, or generate public answers from unresolved community classifications.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/vegetation_community/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `contracts/domains/flora/vegetation_community.md` | **CONFIRMED draft contract / schema and runtime NEEDS VERIFICATION** | Defines `VegetationCommunity` as Flora evidence-bound polygonal/plot/survey/model/aggregate vegetation-community classification and floristic composition support. |
| `contracts/domains/habitat/ecological_system.md` | **CONFIRMED draft contract / schema and runtime NEEDS VERIFICATION** | Defines Habitat `EcologicalSystem` as a separate Habitat-owned classification object, not Flora `VegetationCommunity`, occurrence truth, regulatory critical habitat, suitability, or release authority. |
| `docs/domains/flora/OBJECT_FAMILIES.md` | **CONFIRMED planning/register evidence / implementation NEEDS VERIFICATION** | Lists Flora object families including `VegetationCommunity`, rare-plant deny-by-default surfaces, validators/tests/fixtures backlog, and responsibility-root planning. |
| Executable vegetation-community scripts, validator registry wiring, schema enforcement, taxonomy/crosswalk registry, source registries, fixtures, policy bundles, report destinations, receipt emission, release integration, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home | Boundary |
|---|---|---|
| Vegetation-community validator routing | `tools/validators/vegetation_community/` | Checks Flora `VegetationCommunity` packets and fail-closed posture. |
| Vegetation-community meaning | `contracts/domains/flora/vegetation_community.md` | Semantic meaning; this validator checks conformance. |
| Habitat ecological-system meaning | `contracts/domains/habitat/ecological_system.md` | Separate Habitat classification; not Flora community truth. |
| Taxonomy and crosswalk validation | `tools/validators/taxonomy_resolver/`, Flora taxon/crosswalk contracts | Checks refs and ambiguity; does not own taxonomy authority. |
| Source-role validation | `tools/validators/source_role/` | Prevents survey/model/aggregate/candidate/community labels from becoming occurrence truth. |
| Sensitive geometry / geoprivacy | `tools/validators/sensitive_geometry/`, `tools/validators/geoprivacy/` | Exact/potentially reconstructable rare-plant and rare-habitat geometry must fail closed. |
| Flora and Habitat source registries | `data/registry/sources/flora/`, `data/registry/sources/habitat/` | Own source identity, rights, cadence, attribution, and limits. |
| Policy and release posture | `policy/domains/flora/`, `policy/sensitivity/flora/`, `release/` | Validator reports gaps; it does not decide policy or release. |
| Evidence/proofs and receipts | `data/proofs/`, `data/receipts/` | Validators check refs; they do not create authority records here. |
| Fixtures and tests | `fixtures/domains/flora/vegetation_community/`, `tests/domains/flora/` | Synthetic examples and tests prove behavior; they are not community authority. |

[Back to top](#top)

---

## Validation packet

A vegetation-community candidate should expose enough explicit context for deterministic validation.

| Required family | Validator expectation | Must not be treated as |
|---|---|---|
| Candidate identity | Candidate id, object family, lifecycle state, source refs, artifact refs, requested audience, operation, and surface. | Permission by naming convention. |
| Community classification | Source-native label, normalized label, classification scheme, scheme version, method, review state, confidence, and uncertainty are explicit. | Habitat truth or occurrence truth. |
| Floristic support | Dominant taxa, indicator taxa, composition summaries, cover estimates, structure notes, or source-native species lists are traceable where used. | Exact species occurrence proof by itself. |
| Spatial support | Polygon, multipolygon, plot, transect, grid, raster unit, generalized public geometry, withheld geometry, scale, precision, and topology state are explicit. | Public exact-location permission. |
| Source-role posture | Survey-derived, modeled, aggregate, reviewed, candidate, remote-sensing, and source-native labels remain distinct. | Source-role collapse or upgrade. |
| Taxonomy/crosswalk posture | Plant taxon refs, community vocabulary refs, aliases, crosswalks, versions, review state, and deprecated/stale term handling are visible. | Taxonomy authority by label match. |
| Flora/Habitat boundary | Flora `VegetationCommunity`, `HabitatAssociation`, `RangePolygon`, `FloraOccurrence`, and Habitat `EcologicalSystem` remain separate. | Cross-domain truth collapse. |
| Sensitivity/rights posture | Rare habitat, rare/protected plant inference, private land stewardship, cultural plant knowledge, source-restricted field notes, and public-safe state are resolved. | Public release by contract presence. |
| Evidence/policy/release support | EvidenceRef, EvidenceBundle/proof refs, validation report, policy decision, reason codes, obligations, review bindings, release reference, correction path, rollback target, and receipts exist where required. | Publication by validator success. |
| Public-surface envelope | Map/API/tile/export/screenshot/graph/search/Focus Mode/embedding/AI surfaces are limited to released, public-safe derivatives and caveats. | Unbounded reuse across public surfaces. |

[Back to top](#top)

---

## Invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| Community classification is not occurrence proof | A vegetation-community record may support context, but it does not prove exact species occurrence by itself. | Candidate treats community polygon as occurrence, voucher, or rare-plant proof. |
| Flora and Habitat do not collapse | Flora `VegetationCommunity` and Habitat `EcologicalSystem` remain separate bounded-context objects. | Candidate substitutes Habitat classification for Flora community truth or vice versa. |
| Taxonomy labels are not authority | Labels, aliases, map legends, UI strings, and AI prose are not canonical taxonomy/community truth. | Candidate resolves ambiguous labels silently. |
| Source roles remain visible | Survey, modeled, aggregate, remote-sensing, reviewed, candidate, and source-native labels remain distinct. | Candidate upgrades model/candidate/aggregate to observed or authoritative truth. |
| Spatial support is scoped | Geometry type, scale, precision, topology, public-safe transform, and withheld state are explicit. | Exact/reconstructable rare community or rare-plant context reaches public surface. |
| Sensitivity fails closed | Rare habitat, rare/protected plant inference, private land stewardship, source-restricted notes, and cultural/ecological sensitivity require review. | Public artifact omits sensitivity or rights support. |
| Corrections cascade | Taxonomy change, source correction, classification revision, geometry redaction, rights change, release withdrawal, or rollback invalidates downstream carriers. | Public layer/AI answer remains active after blocking change. |
| Carriers are not authority | Maps, tiles, graph views, exports, screenshots, Focus Mode, embeddings, and AI answers are downstream carriers. | Carrier becomes evidence, taxonomy, community, habitat, policy, or release authority. |

[Back to top](#top)

---

## Fail-closed conditions

A vegetation-community candidate should fail closed, deny, restrict, abstain, or route to steward review when:

- community label, classification scheme/version, method, source refs, source role, lifecycle state, review state, confidence, uncertainty, or temporal scope is missing;
- taxonomy ref, community vocabulary ref, plant taxon ref, alias, synonym, crosswalk, deprecated term, stale term, or ambiguous label is unresolved;
- vegetation community is treated as exact occurrence proof, rare-plant record, Habitat EcologicalSystem truth, regulatory critical habitat, management instruction, or release authority;
- spatial support, scale, geometry role, topology state, public-safe derivative, redaction/generalization receipt, or withheld geometry posture is missing where required;
- rare habitat, rare/protected plant inference, private stewardship site, source-restricted field notes, cultural plant knowledge, or sensitive ecological context is public-bound without policy/review/release support;
- source roles collapse across survey, modeled, aggregate, remote-sensing, candidate, reviewed, or source-native records;
- EvidenceRef, EvidenceBundle, validation report, receipt, policy decision, review binding, release reference, correction path, rollback target, or supersession posture is missing where required;
- public map, tile, export, screenshot, graph, search, Focus Mode, popup, or AI output would expose unreleased community detail, reconstruct sensitive sites, or overclaim classification truth.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Vegetation-community validator routing | `tools/validators/vegetation_community/` |
| Vegetation-community semantic contract | `contracts/domains/flora/vegetation_community.md` |
| Flora object contracts | `contracts/domains/flora/` |
| Habitat ecological-system contract | `contracts/domains/habitat/ecological_system.md` |
| Flora and Habitat schemas | `schemas/contracts/v1/domains/flora/`, `schemas/contracts/v1/domains/habitat/`, accepted schema homes |
| Taxonomy helper / resolver code | `packages/taxonomy/`, `tools/validators/taxonomy_resolver/` |
| Source registries | `data/registry/sources/flora/`, `data/registry/sources/habitat/` |
| Sensitive geometry and geoprivacy validation | `tools/validators/sensitive_geometry/`, `tools/validators/geoprivacy/` |
| Policy | `policy/domains/flora/`, `policy/sensitivity/flora/`, accepted policy homes |
| Evidence/proofs | `data/proofs/` |
| Receipts | `data/receipts/` |
| Lifecycle data | governed `data/` lifecycle roots |
| Release records and rollback | `release/` |
| Fixtures | `fixtures/domains/flora/vegetation_community/` and accepted fixture homes |
| Tests | `tests/domains/flora/` and accepted test homes |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared vegetation-community invariants and delegates semantic meaning, taxonomy authority, canonical schemas, policy decisions, evidence, receipts, lifecycle data, release records, and public runtime authority to owning roots.
- **NEEDS VERIFICATION:** exact executable files, registry entries, classification vocabulary homes, schema bindings, fixture files, test paths, policy bundle homes, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as Flora truth, Habitat truth, taxonomy authority, occurrence proof, rare-plant location store, source registry, policy home, schema home, evidence store, proof store, receipt store, lifecycle data store, release record store, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/vegetation_community/` include:

- this README;
- small validation adapters that check vegetation-community packets;
- checks for community classification scheme, method, version, label, confidence, uncertainty, and review state;
- checks for floristic support, dominant/indicator taxa, taxonomy refs, aliases, crosswalks, and deprecated/stale term handling;
- checks that Flora community classification does not become Habitat truth, occurrence proof, regulatory habitat, or release authority;
- checks for public-safe geometry, redaction/generalization receipts, rare-habitat and rare-plant inference risk, private stewardship, and cultural/ecological sensitivity;
- checks for evidence, policy, review, release, correction, rollback, and public-surface support;
- finite outcome vocabulary and reason-code mapping;
- report destination notes that keep generated outputs out of policy, receipt, proof, lifecycle, taxonomy, and release authority unless explicitly routed to accepted homes.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Flora or Habitat semantic contracts | `contracts/domains/flora/`, `contracts/domains/habitat/` |
| JSON Schemas, DTOs, enums, or machine shape | `schemas/contracts/v1/domains/flora/`, `schemas/contracts/v1/domains/habitat/`, accepted schema homes |
| Taxonomy vocabularies, accepted crosswalk ledgers, community classification registries | accepted taxonomy/registry homes, not validator docs |
| Source data, survey payloads, occurrence records, rare-plant records, community polygons, map artifacts | governed `data/` lifecycle roots and release homes after gates close |
| Policy rules, allowlists, denylists, steward decisions, release decisions | `policy/`, `release/`, accepted governance homes |
| EvidenceBundles, proof packs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |
| Sensitive exact locations, rare-habitat reconstruction hints, private stewardship details, cultural plant knowledge, hidden thresholds, source credentials, or production signing keys | denied here; keep out of repository-facing validator docs |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `VEGETATION_COMMUNITY_PASS` | Candidate passed configured vegetation-community checks. |
| `VEGETATION_COMMUNITY_FAIL` | Candidate failed one or more configured checks. |
| `VEGETATION_COMMUNITY_DENY` | Candidate must not proceed because classification, evidence, sensitivity, policy, review, release, rollback, or public-surface support cannot be resolved. |
| `VEGETATION_COMMUNITY_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `VEGETATION_COMMUNITY_ABSTAIN` | Candidate lacks enough support for a community-classification assertion. |
| `COMMUNITY_CLASSIFICATION_MISSING` | Required classification label, scheme, version, method, or review state is absent. |
| `COMMUNITY_TAXONOMY_REF_MISSING` | Required taxonomy/community vocabulary/plant taxon/crosswalk reference is absent. |
| `COMMUNITY_LABEL_AMBIGUOUS` | Community label, alias, or synonym resolves ambiguously. |
| `COMMUNITY_SOURCE_ROLE_COLLAPSE_DENIED` | Survey/model/aggregate/candidate/source-native roles are collapsed or upgraded. |
| `COMMUNITY_OCCURRENCE_OVERCLAIM` | Community record is treated as exact species occurrence or rare-plant proof. |
| `COMMUNITY_HABITAT_COLLAPSE_DENIED` | Flora community classification is collapsed with Habitat EcologicalSystem, HabitatAssociation, or regulatory habitat truth. |
| `COMMUNITY_GEOMETRY_PUBLIC_DENIED` | Exact or reconstructable sensitive community/rare-plant context is public-bound. |
| `COMMUNITY_SENSITIVITY_REVIEW_REQUIRED` | Rare habitat, rare/protected plant inference, private stewardship, source-restricted notes, or cultural/ecological context requires review. |
| `COMMUNITY_REDACTION_RECEIPT_MISSING` | Required redaction/generalization/aggregation receipt is absent. |
| `COMMUNITY_EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, proof, or validation support is absent. |
| `COMMUNITY_POLICY_OR_REVIEW_GAP` | Required policy decision, review state, rights posture, sensitivity posture, or obligations are absent. |
| `COMMUNITY_RELEASE_REFERENCE_MISSING` | Required release, correction, withdrawal, reevaluation, or rollback reference is absent. |
| `COMMUNITY_CORRECTION_CASCADE_MISSING` | Taxonomy/source/classification/geometry/release correction did not propagate downstream. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose unsupported or sensitive community state to public API, map, tile, export, screenshot, graph, Focus Mode, embedding, or AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, evaluator error, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/vegetation_community/
├── README.md
├── validate_vegetation_community.py        # PROPOSED; not confirmed
├── validate_community_classification.py    # PROPOSED; not confirmed
├── validate_community_public_surface.py    # PROPOSED; not confirmed
└── registry_notes.md                       # PROPOSED; documentation only
```

Do not add executable validators, policy bundles, taxonomy ledgers, local schema files, source data, community polygons, rare-plant payloads, release records, or fixtures unless the placement decision is documented, the canonical authority relationship is explicit, and tests prove fail-closed behavior without granting Flora, Habitat, taxonomy, public-surface, or release authority.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/vegetation_community/README.md`.
- [x] It marks this path as validator routing, not Flora truth, Habitat truth, taxonomy authority, occurrence proof, rare-plant location storage, schema authority, policy authority, proof/receipt storage, release record storage, public runtime, or AI authority.
- [x] It preserves the boundary between Flora `VegetationCommunity`, Flora occurrences/taxa/range/habitat associations, and Habitat `EcologicalSystem`.
- [x] It preserves source-role, classification, taxonomy/crosswalk, spatial support, sensitivity, evidence, review, release, correction, rollback, and public-surface boundaries.
- [x] It routes semantic meaning to `contracts/` and `docs/`, machine shape to `schemas/`, taxonomy authority to accepted taxonomy/registry homes, policy to `policy/`, receipts/proofs to `data/`, release records to `release/`, fixtures to `fixtures/`, and tests to `tests/`.
- [x] It marks executable scripts, registry wiring, classification vocabulary homes, schemas, fixtures, tests, policy bundles, receipt emission, release integration, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to vegetation-community validators are searched and classified.
- [ ] VegetationCommunity schema bindings, taxonomy/community vocabulary homes, crosswalk refs, and source registry bindings are verified.
- [ ] Fixture files are added only as synthetic/minimized public-safe payloads with documented expected outcomes.
- [ ] Tests prove positive, negative, deny, restrict, abstain, missing-classification, ambiguous-label, missing-taxonomy-ref, source-role-collapse, occurrence-overclaim, habitat-collapse, geometry-public-denied, sensitivity-review-required, missing-redaction-receipt, release-missing, correction-cascade-missing, and public-surface-blocked cases.
- [ ] CI invokes vegetation-community validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with vegetation-community validator README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
