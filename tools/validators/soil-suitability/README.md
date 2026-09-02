<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-soil-suitability-readme
title: tools/validators/soil-suitability README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-soil-steward-plus-agriculture-steward-plus-join-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; soil-suitability-validator-index; agriculture-soil; SoilCropSuitability; MUKEY; COKEY; CHKEY; source-role-aware; support-type-aware; modeled-derivative-aware; aggregation-aware; release-gated; non-authoritative
owning_root: tools/
responsibility: parent soil-suitability validator routing README under tools/validators; documents validation expectations for SoilCropSuitability and related soil suitability derivatives, MUKEY/COKEY/CHKEY continuity, Soil-owned EvidenceRef consumption, Agriculture-owned derivative boundaries, Soil support-type separation, source-role anti-collapse, suitability method/version posture, units/class vocabulary, field-level and operator-adjacent sensitivity controls, aggregation/redaction receipt linkage, evidence/proof linkage, policy/review/release posture, correction cascade, rollback support, public-surface denial, schema/fixture/test routing, and finite outcomes while deferring Agriculture meaning, Soil meaning, canonical schemas, policy decisions, evidence records, receipts, lifecycle data, release records, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../agriculture/README.md
  - ../soil/README.md
  - ../domains/agriculture/soil-join/README.md
  - ../domains/soil/README.md
  - ../joins/agriculture-soil/README.md
  - ../cross-domain-joins/README.md
  - ../policy/README.md
  - ../rights/README.md
  - ../sensitivity/README.md
  - ../release/README.md
  - ../promotion_gate/README.md
  - ../../../docs/domains/agriculture/OBJECTS.md
  - ../../../docs/domains/agriculture/CROSS_LANE.md
  - ../../../docs/domains/agriculture/POLICY.md
  - ../../../docs/domains/agriculture/SENSITIVITY.md
  - ../../../docs/domains/soil/README.md
  - ../../../docs/domains/soil/ARCHITECTURE.md
  - ../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../contracts/domains/agriculture/
  - ../../../contracts/domains/soil/
  - ../../../schemas/contracts/v1/domains/agriculture/
  - ../../../schemas/contracts/v1/domains/soil/
  - ../../../schemas/contracts/v1/joins/agriculture-soil/
  - ../../../policy/domains/agriculture/
  - ../../../policy/domains/soil/
  - ../../../data/registry/sources/agriculture/
  - ../../../data/registry/sources/soil/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
  - ../../../fixtures/
  - ../../../tests/
notes:
  - "This README replaces an empty placeholder at tools/validators/soil-suitability/README.md. It does not confirm executable soil-suitability validators, registry wiring, schemas, fixtures, policy bundles, receipt emission, runtime behavior, or CI behavior."
  - "This lane is for suitability-derivative validation. It must not compete with shared Agriculture-Soil join routing at tools/validators/joins/agriculture-soil/ or Agriculture-facing join routing at tools/validators/domains/agriculture/soil-join/."
  - "Agriculture may own SoilCropSuitability as an Agriculture derivative, but Soil owns canonical Soil map-unit/component/horizon semantics. Agriculture consumes Soil-owned objects by EvidenceRef and must not republish Soil objects as Agriculture truth."
  - "MUKEY is the load-bearing Agriculture x Soil join key; COKEY/CHKEY continuity must remain visible when component/horizon details are material. Unresolved identifiers should ABSTAIN or route to review, not fabricate suitability or snap identity from geometry alone."
  - "Suitability ratings are derived/modelled/interpretive outputs. They are not raw Soil truth, field-level management orders, agronomic advice, regulatory determinations, or public release approval by themselves."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/soil-suitability

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-soil--suitability--validator-informational)
![join](https://img.shields.io/badge/join-MUKEY-blueviolet)
![authority](https://img.shields.io/badge/authority-derived--not--truth-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/soil-suitability/` is the validator routing lane for Soil suitability derivatives such as `SoilCropSuitability`, checking Soil-owned identity and evidence consumption, Agriculture-owned derivative boundaries, support-type/source-role preservation, method/version posture, aggregation/redaction needs, release readiness, correction cascade, rollback support, and public-surface denial.

---

## Purpose

`tools/validators/soil-suitability/` exists to make suitability-specific validation visible without turning a validator folder into Soil truth, Agriculture truth, join authority, policy authority, evidence authority, release authority, or agronomic advice.

The durable KFM question for this lane is:

> Does a soil suitability candidate preserve Soil-owned MUKEY/COKEY/CHKEY identity, cite Soil evidence through governed EvidenceRefs, keep Agriculture-owned suitability derivatives separate from canonical Soil truth, preserve source roles and support types, expose method/version/units/class vocabulary, close evidence/policy/review/release/correction/rollback support, and deny unsafe field-level or public-surface exposure?

The answer should be a deterministic validation result or routing decision. This folder should not create Agriculture truth, Soil truth, SoilMapUnit truth, field-level truth, suitability truth, agronomic recommendations, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/soil-suitability/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `tools/validators/domains/agriculture/soil-join/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Agriculture-facing Agriculture × Soil join lane; names MUKEY/COKEY/CHKEY preservation, Soil-owned EvidenceRefs, and Agriculture-owned `SoilCropSuitability` derivatives. |
| `tools/validators/joins/agriculture-soil/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Shared Agriculture × Soil join route; this suitability lane is derivative-specific and must not compete with shared join routing. |
| `tools/validators/agriculture/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Agriculture parent validator lane lists `SoilCropSuitability` references to Soil-owned MUKEY semantics as a validator concern. |
| `tools/validators/domains/soil/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Soil per-domain validator index preserves Soil support-type separation, source-role discipline, MUKEY/COKEY/CHKEY continuity, evidence, policy, release, correction, rollback, and public-surface boundaries. |
| `docs/domains/agriculture/OBJECTS.md` | **CONFIRMED draft reference / realization NEEDS VERIFICATION** | Agriculture owns `SoilCropSuitability`, while Soil owns map-unit and horizon semantics including MUKEY, COKEY, CHKEY, and horizon properties. |
| Executable soil-suitability scripts, registry wiring, schemas, fixtures, policy bundles, method vocabularies, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home | Boundary |
|---|---|---|
| Soil suitability derivative validation | `tools/validators/soil-suitability/` | Derivative-specific routing for suitability outputs. |
| Shared Agriculture × Soil join validation | `tools/validators/joins/agriculture-soil/` | Shared join identity/evidence/source-role/support-type posture. |
| Agriculture-facing Agriculture × Soil edge | `tools/validators/domains/agriculture/soil-join/` | Agriculture derivative and domain-edge posture. |
| Agriculture parent validation | `tools/validators/agriculture/` | Broad Agriculture validator lane. |
| Soil parent validation | `tools/validators/domains/soil/`, `tools/validators/soil/` if confirmed | Soil identity, support type, source role, lineage, catalog, and public-surface posture. |
| Domain meaning | `docs/domains/agriculture/`, `contracts/domains/agriculture/`, `docs/domains/soil/`, `contracts/domains/soil/` | Validators check conformance; they do not define meaning. |
| Machine shape | `schemas/contracts/v1/domains/agriculture/`, `schemas/contracts/v1/domains/soil/`, accepted join schema homes | Schemas define shape; this folder does not. |
| Policy and release posture | `policy/domains/agriculture/`, `policy/domains/soil/`, `release/` | Validator reports gaps; it does not decide policy or release. |
| Evidence/proofs and receipts | `data/proofs/`, `data/receipts/` | Validators check references; they do not create authority records. |
| Fixtures and tests | `fixtures/`, `tests/` or accepted convention | Synthetic examples and tests prove behavior; they are not suitability authority. |

[Back to top](#top)

---

## Suitability validation packet

A suitability candidate should expose enough explicit context for deterministic validation.

| Required family | Validator expectation | Must not be treated as |
|---|---|---|
| Candidate identity | Candidate id, Agriculture object refs, Soil object refs, lifecycle state, source refs, artifact refs, requested audience, requested operation, and requested surface. | Permission by naming convention. |
| Soil identity | MUKEY is preserved and resolvable; COKEY/CHKEY remain visible when component/horizon details are material. | Fabricated identity or geometry-snapped truth. |
| Soil evidence consumption | Soil-owned EvidenceRefs resolve to EvidenceBundles/proof support for Soil map units, components, horizons, properties, or interpretations. | Copying Soil objects into Agriculture authority. |
| Agriculture derivative boundary | `SoilCropSuitability` or related suitability output remains Agriculture-owned derivative with declared modeled/derived posture. | Raw Soil truth, field-level truth, or direct agronomic advice. |
| Support type and source role | Static survey, gridded derivative, station observation, satellite grid, pedon/profile, interpretation, public-safe derivative, observed, regulatory, modeled, aggregate, and candidate roles remain distinct. | Generic suitability truth with support collapse. |
| Suitability method | Method id/version, crop or use context, suitability class/rating vocabulary, units, limitations, temporal applicability, uncertainty, scale, and assumptions are explicit. | Universal or timeless suitability. |
| Sensitivity/rights posture | Field-level, operator-adjacent, private parcel, sensitive location, source-rights, and public-surface limits are preserved. | Public release by derived status alone. |
| Evidence/policy/review support | EvidenceRef, validation report, policy decision, reason codes, obligations, review bindings, and source-rights posture are present where required. | Validator success as policy approval. |
| Release/correction/rollback support | Release reference, correction path, rollback target, supersession, stale-state, and Soil-side correction cascade are visible where public-bound. | Publication by validator success. |
| Public-surface envelope | Map/API/tile/export/screenshot/graph/search/Focus Mode/embedding/AI surfaces are limited to approved aggregate/public-safe derivatives. | Unbounded reuse across surfaces. |

[Back to top](#top)

---

## Suitability invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| Soil ownership is preserved | Soil objects remain Soil-owned and are cited by EvidenceRef. | SoilMapUnit, SoilComponent, Horizon, SoilProperty, Hydrologic Soil Group, Pedon, or interpretation is republished as Agriculture truth. |
| Agriculture derivative is explicit | Suitability remains a derived Agriculture-owned object or clearly routed derivative. | Suitability output is presented as raw Soil truth or field-level fact. |
| MUKEY resolves | MUKEY is preserved verbatim and resolves through governed Soil evidence. | MUKEY is missing, malformed, stale, fabricated, geometry-derived only, or unresolved. |
| COKEY/CHKEY continuity is visible | Component/horizon identifiers remain traceable where used. | COKEY/CHKEY are dropped, synthesized, or used outside verified scope. |
| Support types do not collapse | Static survey, gridded derivative, station observation, satellite grid, pedon/profile, interpretation, and public-safe derivatives remain distinct. | Soil support families are merged into generic suitability. |
| Source roles do not collapse | Observed, regulatory, modeled, aggregate, candidate, and public-safe roles remain visible. | Regulatory or observed Soil evidence is relabeled as generic modeled Agriculture truth. |
| Method and context are bounded | Suitability method, crop/use context, class vocabulary, scale, limits, uncertainty, and time applicability are explicit. | Suitability is interpreted as universal advice or mandate. |
| Field-level exposure is denied by default | Field/operator/private parcel-adjacent suitability requires aggregation/redaction/review/release support before public use. | Private or field-level output reaches public surface. |
| Corrections cascade | Soil-side correction, stale source, rights change, revocation, withdrawal, or rollback invalidates dependent suitability outputs. | Suitability remains active after upstream support changes. |
| Carriers are not authority | Maps, tiles, exports, graphs, screenshots, Focus Mode, embeddings, and AI answers are downstream carriers. | Carrier becomes evidence, policy, release, or suitability authority. |

[Back to top](#top)

---

## Fail-closed conditions

A soil-suitability candidate should fail closed, deny, restrict, abstain, or route to steward review when:

- MUKEY is missing, malformed, stale, unresolved, fabricated, or derived only from geometry;
- COKEY/CHKEY are required but absent, synthesized, or no longer traceable;
- Soil-owned EvidenceRefs or EvidenceBundles are missing, unresolved, stale, contradicted, withdrawn, or insufficient;
- suitability output republishes Soil objects, Soil interpretations, or Soil properties as Agriculture canonical truth;
- suitability method id/version, crop/use context, rating vocabulary, units, limitations, uncertainty, scale, or temporal applicability is missing;
- support types or source roles collapse across static survey, gridded derivative, station observation, satellite grid, pedon/profile, interpretation, observed, regulatory, modeled, aggregate, candidate, or public-safe derivative records;
- field-level, operator-adjacent, private parcel, sensitive location, or rights-limited suitability is public-bound without aggregation/redaction/review/release support;
- policy decision, review binding, rights posture, EvidenceRef, receipt, release reference, correction path, rollback target, or supersession posture is missing where required;
- map, tile, export, screenshot, search, graph, embedding, Focus Mode, popup, or AI answer output overclaims suitability, hides caveats, drops evidence, or exposes unsupported details.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Soil suitability validator routing | `tools/validators/soil-suitability/` |
| Agriculture-facing Soil join validation | `tools/validators/domains/agriculture/soil-join/` |
| Shared Agriculture × Soil join validation | `tools/validators/joins/agriculture-soil/` |
| Agriculture validators | `tools/validators/agriculture/`, `tools/validators/domains/agriculture/` |
| Soil validators | `tools/validators/domains/soil/`, accepted Soil validator lanes |
| Agriculture and Soil meaning | `docs/domains/agriculture/`, `contracts/domains/agriculture/`, `docs/domains/soil/`, `contracts/domains/soil/` |
| Agriculture, Soil, and join schemas | `schemas/contracts/v1/domains/agriculture/`, `schemas/contracts/v1/domains/soil/`, accepted join schema homes |
| Agriculture and Soil policy | `policy/domains/agriculture/`, `policy/domains/soil/`, accepted policy homes |
| Source descriptors | `data/registry/sources/agriculture/`, `data/registry/sources/soil/` |
| Evidence/proofs | `data/proofs/` |
| Receipts | `data/receipts/` |
| Lifecycle/quarantine/data products | governed `data/` lifecycle roots |
| Release records and rollback | `release/` |
| Fixtures | `fixtures/` and accepted fixture homes |
| Tests | `tests/` and accepted test homes |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared soil-suitability invariants and delegates Agriculture meaning, Soil meaning, schema authority, policy decisions, evidence, receipts, lifecycle data, release records, and public runtime authority to owning roots.
- **NEEDS VERIFICATION:** exact executable files, registry entries, `SoilCropSuitability` schema/contract homes, Soil suitability method vocabulary, MUKEY/COKEY/CHKEY schema bindings, fixture files, test paths, policy bundle homes, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as Soil truth, Agriculture truth, suitability truth, agronomic advice, source registry, policy home, schema home, evidence store, proof store, receipt store, lifecycle data store, release record store, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/soil-suitability/` include:

- this README;
- small validation adapters that check soil-suitability derivative packets;
- checks for MUKEY/COKEY/CHKEY continuity and Soil-owned EvidenceRef consumption;
- checks that `SoilCropSuitability` remains a derived Agriculture-owned object and not raw Soil truth;
- checks for method id/version, crop/use context, rating vocabulary, units, limitations, uncertainty, and scale caveats;
- checks for support-type and source-role anti-collapse;
- checks that field-level/private/operator-adjacent suitability requires aggregation/redaction/review/release support;
- checks that Soil-side corrections, revocations, stale sources, or rollbacks cascade into suitability outputs;
- finite outcome vocabulary and reason-code mapping;
- report destination notes that keep generated outputs out of policy, receipt, proof, lifecycle, and release authority unless explicitly routed to accepted homes.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Agriculture or Soil semantic contracts | `contracts/domains/agriculture/`, `contracts/domains/soil/` |
| Agriculture, Soil, or join schemas | `schemas/contracts/v1/domains/agriculture/`, `schemas/contracts/v1/domains/soil/`, accepted join schema homes |
| Policy rules, suitability allowlists, agronomic thresholds, steward decisions, source-rights decisions | `policy/`, steward review homes, release governance homes |
| Soil source data, SSURGO extracts, gridded rasters, pedon data, field/operator records, suitability products | governed `data/` lifecycle roots |
| EvidenceBundles, proof packs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |
| Secrets, source credentials, private source content, sensitive exact locations, hidden thresholds, production signing keys, or reconstruction hints | denied here; keep out of repository-facing validator docs |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `SOIL_SUITABILITY_VALIDATOR_PASS` | Candidate passed configured soil-suitability checks. |
| `SOIL_SUITABILITY_VALIDATOR_FAIL` | Candidate failed one or more configured soil-suitability checks. |
| `SOIL_SUITABILITY_VALIDATOR_DENY` | Candidate must not proceed because evidence, policy, review, rights, sensitivity, release, correction, rollback, or public-surface support cannot be resolved. |
| `SOIL_SUITABILITY_VALIDATOR_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `SOIL_SUITABILITY_VALIDATOR_ABSTAIN` | Candidate lacks enough support for a suitability assertion. |
| `MUKEY_MISSING_OR_UNRESOLVED` | Required MUKEY is absent, malformed, stale, fabricated, geometry-derived only, or unresolved. |
| `COKEY_CHKEY_TRACE_MISSING` | Required component/horizon identity is absent or not traceable. |
| `SOIL_EVIDENCE_REF_MISSING` | Required Soil-owned EvidenceRef or EvidenceBundle pointer is absent or unresolved. |
| `SOIL_AUTHORITY_COLLAPSE_DENIED` | Candidate republishes Soil-owned object meaning as Agriculture truth. |
| `AGRICULTURE_DERIVATIVE_BOUNDARY_MISSING` | Suitability output does not identify itself as Agriculture-owned derivative. |
| `SUITABILITY_METHOD_MISSING` | Method id/version, crop/use context, rating vocabulary, units, scale, limitations, or uncertainty is absent. |
| `SUPPORT_TYPE_COLLAPSE_DENIED` | Soil support types collapse into generic suitability. |
| `SOURCE_ROLE_COLLAPSE_DENIED` | Observed/regulatory/modeled/aggregate/candidate roles collapse. |
| `FIELD_LEVEL_PUBLIC_DENIED` | Field/operator/private parcel-adjacent suitability is public-bound without aggregation/redaction/review/release support. |
| `POLICY_OR_REVIEW_GAP` | Required policy decision, review state, rights posture, sensitivity posture, or obligation support is absent. |
| `RELEASE_REFERENCE_MISSING` | Required release, correction, withdrawal, reevaluation, or rollback reference is absent. |
| `CORRECTION_CASCADE_MISSING` | Soil-side correction, revocation, stale source, withdrawal, or rollback did not propagate to suitability output. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose unsupported or sensitive suitability content to public API, map, tile, export, screenshot, graph, Focus Mode, embedding, or AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, evaluator error, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/soil-suitability/
├── README.md
├── validate_soil_suitability.py         # PROPOSED; not confirmed
├── validate_soil_crop_suitability.py    # PROPOSED; not confirmed
├── validate_suitability_cascade.py      # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

Do not add executable validators, policy bundles, local schema files, source data, suitability payloads, release records, or fixtures unless the placement decision is documented, the canonical authority relationship is explicit, and tests prove fail-closed behavior without granting suitability, public-surface, or release authority.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/soil-suitability/README.md`.
- [x] It marks this path as soil-suitability validator routing, not Soil truth, Agriculture truth, suitability truth, agronomic advice, schema authority, policy authority, proof/receipt storage, release record storage, public runtime, or AI authority.
- [x] It distinguishes this derivative-specific lane from shared `joins/agriculture-soil/` and Agriculture-facing `domains/agriculture/soil-join/` lanes.
- [x] It preserves MUKEY/COKEY/CHKEY continuity, Soil-owned EvidenceRef consumption, Agriculture-owned derivative boundary, support-type separation, source-role preservation, method/version posture, correction cascade, rollback, and public-surface denial.
- [x] It routes domain meaning to `contracts/` and `docs/`, machine shape to `schemas/`, policy to `policy/`, receipts/proofs to `data/`, release records to `release/`, fixtures to `fixtures/`, and tests to `tests/`.
- [x] It marks executable scripts, registry wiring, schema homes, method vocabularies, policy bundles, fixtures, tests, receipt emission, release integration, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to soil-suitability validators are searched and classified.
- [ ] `SoilCropSuitability` contract/schema homes and Soil suitability method vocabulary are verified.
- [ ] MUKEY/COKEY/CHKEY, Soil EvidenceRef, support type, source role, rating vocabulary, and release-reference schema bindings are verified.
- [ ] Fixture files are added only as synthetic/minimized public-safe payloads with documented expected outcomes.
- [ ] Tests prove positive, negative, deny, restrict, abstain, MUKEY-missing, evidence-missing, support-collapse, source-role-collapse, method-missing, field-public-denied, correction-cascade-missing, and public-surface-blocked cases.
- [ ] CI invokes soil-suitability validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with soil-suitability validator parent README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
