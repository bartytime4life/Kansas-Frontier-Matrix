<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-hydrology
title: Hydrology Dashboard Specification
type: standard
version: v0.2.0
status: draft; repository-grounded; bounded-validation; dashboard-runtime-unverified; proof-held; non-release; non-publication
owners: "@bartytime4life (CODEOWNERS review route); Hydrology, evidence/source, scientific/regulatory, policy, metric/UI, release/correction, and independent stewards NEEDS VERIFICATION"
created: 2026-05-26
updated: 2026-08-21
policy_label: public
owning_root: docs/
responsibility: "Review-facing Hydrology dashboard specification and repository-state reporting only; not source, evidence, scientific, regulatory, policy, runtime, emergency, release, or publication authority."
truth_posture: "CONFIRMED current repository evidence / PROPOSED metric contracts and presentation states / UNKNOWN routed dashboard, production telemetry, live-source admission, release, deployment, and publication"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 12466fcf0196af9917a26b0dc5251f56e742f506
  target_prior_blob: b38da1ba2d00d95a854f195bbbf7ec97a0050bf0
  dashboard_catalog_blob: f86b42f7bc6fd28de78e98f06cf1f89cc5af7d4c
  hydrology_domain_readme_blob: 72d7d2608dfa7b40e4515aacb213bed0b46cbfee
  hydrology_contract_index_blob: ae71803b28c3d3d8853c74f1264a852ab5a13e3a
  hydrology_schema_index_blob: dfe13f5437a426e470a7e2adfc497080415129bb
  hydrology_policy_index_blob: 1e39301650009a8e2a01c0b9dc3bb344e934a92b
  evidence_drawer_projection_blob: 59b748e2e6e194f65584e7686a87bb75013f329e
  evidence_drawer_component_blob: ce7594231ed59857ef9b3e37d7a0a9d1286866b4
  hydrology_layers_placeholder_blob: b95a28ef96b428731d30d05f9f8cf823c7cfbf92
  evidence_drawer_test_blob: f8225336f42f0f25898ce11142b9b4756beeb86b
  evidence_drawer_workflow_blob: 954eb6818faadc086dec5a4858b90a586926c9e1
  evidence_resolver_readme_blob: 74b12d1732b297458967a8c76bacca240b74eba3
  governed_api_route_registry_blob: 3418168d0b267160d6ad6dd87f289e880ef4a024
inspection_boundary: >-
  Current-session GitHub reads covered the complete prior dashboard
  specification; current dashboard catalog; Hydrology domain, semantic-contract,
  schema, map/UI, thin-slice, release, and policy documentation; the Explorer
  Hydrology README, shared Evidence Drawer delegation, layer placeholder, schema
  projection, focused test, and no-network workflow; the internal
  manifest-backed synthetic Hydrology fixture adapter and its negative proof;
  the Hydrology readiness workflow; the governed API route registry; accepted
  directory authority; and open pull-request/task-branch overlap. No live source,
  production metric producer, telemetry store, policy evaluator, dashboard route,
  deployed panel, release record, correction propagation, rollback drill, or
  public endpoint was exercised.
related:
  - ../DASHBOARD_CATALOG.md
  - README.md
  - ../../domains/hydrology/README.md
  - ../../domains/hydrology/BOUNDARY.md
  - ../../domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../domains/hydrology/MAP_UI_CONTRACTS.md
  - ../../domains/hydrology/PUBLICATION_POSTURE.md
  - ../../domains/hydrology/THIN_SLICE.md
  - ../../domains/hydrology/RELEASE_INDEX.md
  - ../../../apps/explorer-web/src/features/domains/hydrology/README.md
  - ../../../apps/explorer-web/src/features/domains/hydrology/EvidenceDrawer.tsx
  - ../../../apps/explorer-web/src/features/domains/hydrology/layers.ts
  - ../../../contracts/domains/hydrology/README.md
  - ../../../schemas/contracts/v1/domains/hydrology/README.md
  - ../../../schemas/contracts/v1/domains/hydrology/evidence_drawer_payload.schema.json
  - ../../../policy/domains/hydrology/README.md
  - ../../../packages/evidence-resolver/README.md
  - ../../../tests/validators/domains/hydrology/test_evidence_drawer_convergence.py
  - ../../../tests/packages/evidence_resolver/test_hydrology_fixture_adapter.py
  - ../../../.github/workflows/hydrology-evidence-drawer-convergence.yml
  - ../../../.github/workflows/domain-hydrology.yml
  - ../../../apps/governed-api/src/governed_api/routes/registry.py
  - ../../adr/ADR-0009-hydrology-is-the-first-proof-bearing-lane.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../../../.github/CODEOWNERS
tags: [kfm, dashboards, domain, hydrology, watershed, gauge, groundwater, nfhl, evidence, source-role, time, datum, policy, correction, rollback, specification]
notes:
  - "v0.2.0 replaces an Atlas-only proposal with a current repository-grounded dashboard specification."
  - "Numeric health thresholds from v0.1 are removed unless and until an accepted metric contract defines the eligible population, evidence source, time window, null semantics, and review authority."
  - "Bounded executable proof exists for shared Evidence Drawer convergence, selected Hydrology schema/fixture families, and one manifest-backed synthetic fixture adapter; none establishes a production dashboard or public answer."
  - "NFHL remains regulatory context only; Hydrology is not an emergency, navigation, engineering, insurance, legal-entitlement, or regulatory-determination authority."
  - "This revision changes documentation and its generated authoring provenance only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Dashboard Specification

**Repository-grounded review specification for Hydrology source-role integrity, evidence closure, identity and time support, public-safe representation, correction, rollback, and implementation readiness.**

![status](https://img.shields.io/badge/status-draft-blue)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![runtime](https://img.shields.io/badge/dashboard%20runtime-UNKNOWN-lightgrey)
![proof](https://img.shields.io/badge/proof-bounded%20only-f59e0b)
![safety](https://img.shields.io/badge/life--safety%20authority-DENY-critical)

[Scope](#1-domain-scope) · [Indicators](#2-indicator-contracts) · [Measurement](#3-measurement-envelope-and-finite-states) · [Evidence](#4-current-repository-evidence) · [Ownership](#5-ownership-and-review) · [Implementation](#6-implementation-and-acceptance-boundary) · [Public boundary](#7-public-map-api-and-ai-boundary) · [Open work](#8-open-verification-register) · [Validation](#9-validation) · [Rollback](#10-maintenance-correction-and-rollback)

> [!IMPORTANT]
> **Current checkpoint.** Current repository evidence confirms a substantial Hydrology documentation and semantic surface, selected closed schemas and synthetic fixtures, bounded no-network validators/tests, a shared Evidence Drawer projection and renderer delegation, and one internal manifest-backed synthetic fixture adapter. The Hydrology layer adapter remains a placeholder. The governed API route registry contains only bootstrap, layers, and evidence routes, with no Hydrology dashboard route. Hydrology policy remains unbound mixed scaffolding. No production metric producer, telemetry binding, live-source admission, released Hydrology dashboard payload, deployed panel, or publication is confirmed.

> [!CAUTION]
> **Hydrology context is not operational authority.** This dashboard must never present FEMA NFHL material as observed flooding; a model as an observation; a static source as current road, flood, drought, water-quality, supply, irrigation, or emergency status; or a dashboard trend as an engineering, insurance, legal-entitlement, compliance, navigation, or regulatory determination. Unsupported or unsafe operations fail closed.

> [!NOTE]
> `@bartytime4life` is the verified repository review route through `CODEOWNERS`. Routing is not Hydrology stewardship, scientific review, regulatory authority, policy approval, independent review, release approval, or publication authority.

---

## 1. Domain scope

This file specifies a **review-facing governance-health projection** for the Hydrology lane. It may summarize posture for:

- watershed, HUC, hydro-feature, reach, gauge, well, aquifer-observation, hydrograph, and water-quality object families without collapsing their meanings;
- observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic source roles;
- source identity, source version, acquisition state, rights, freshness, qualifiers, and correction support;
- EvidenceRef-to-EvidenceBundle closure for eligible claim-bearing payloads;
- HUC, reach, waterbody, gauge, well, aquifer-context, and crosswalk identity ambiguity;
- parameter code, unit, vertical datum, coordinate reference system, timezone, provisional state, no-data semantics, and uncertainty;
- public-safe geometry, private-well and owner-identifiability controls, aggregation, redaction, and restricted-state handling;
- release, correction, supersession, withdrawal, derivative invalidation, and rollback readiness;
- implementation maturity across documentation, contracts, schemas, fixtures, validators, tests, policy, workflows, packages, API, and Explorer surfaces.

It must not decide hydrologic truth, source admission, water rights, compact compliance, present supply, present road or access conditions, flood or drought status, engineering fitness, insurance eligibility, permit status, regulatory meaning, or emergency action.

It must not treat a map feature, layer, tile, chart, dashboard card, workflow result, receipt, generated narrative, model output, or successful fixture as sovereign evidence.

```text
released public-safe artifact or governed finite envelope
  -> validated object, source-role, identity, time, unit, and datum semantics
  -> EvidenceRef -> EvidenceBundle resolution
  -> rights / sensitivity / policy / review / release checks
  -> aggregate dashboard measurement
  -> restricted, abstaining, stale, incomplete, or error state when closure fails
```

### Domain anti-collapse rules

| Distinction | Required dashboard behavior |
|---|---|
| Observed gauge reading vs. modeled hydrograph | Report separate source roles, time bases, quality/receipt state, and limitations. Never merge into one “water condition” truth class. |
| NFHL zone vs. observed inundation | Label NFHL as regulatory context only. Never infer current flooding, forecast extent, damage, or safety. |
| HUC or watershed boundary vs. stream/reach identity | Preserve object family, source vintage, and crosswalk ambiguity. A spatial overlap is not identity proof. |
| Gauge value vs. station status | A value does not prove the station is operational, complete, or current. |
| Public hydrography vs. private well/person/property detail | Apply minimum-necessary public precision and deny re-identifying joins. |
| Historical record vs. present condition | Keep valid, observed, source, retrieval, release, correction, and stale time distinct. |
| Validation success vs. evidence/release | A green check proves the declared bounded profile only; it does not create source truth, policy permission, review, release, or publication. |

[↑ back to top](#top)

---

## 2. Indicator contracts

The following are **PROPOSED metric contracts**, not implemented telemetry. Numeric thresholds are intentionally not invented. Every future producer must define its eligible population, numerator, denominator, time window, immutable snapshot, source and evidence inputs, null and no-data semantics, sensitivity profile, correction behavior, and safe failure outcome before displaying a percentage, count, rank, or trend.

| ID | Indicator | Proposed healthy posture | Required support | Current state |
|---|---|---|---|---|
| `HYD-DB-01` | **Source-role anti-collapse** | Every eligible item preserves its declared observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic role; conflicts remain visible and do not normalize to an answer. | SourceDescriptor/source head, contract/schema role fields, validation report, policy/review result, release identity. | **PARTIAL bounded evidence.** Role distinctions are documented and exercised in selected synthetic profiles; no production metric producer is confirmed. |
| `HYD-DB-02` | **EvidenceBundle closure** | Every eligible claim-bearing payload either resolves to an admissible, schema-valid EvidenceBundle or reaches `ABSTAIN`, `DENY`, or `ERROR`. | EvidenceRef, EvidenceBundle, verification/correction history, citations, policy context, resolver result, spec/content digest. | **CONFIRMED bounded candidate proof.** Shared alias/projection and one manifest-backed synthetic adapter exist; public runtime resolution remains unverified. |
| `HYD-DB-03` | **Identity and crosswalk integrity** | HUC, waterbody, reach, gauge, well, and relation identities remain version-bound; one-to-many or ambiguous matches are represented, not silently collapsed. | Identity contracts, source vintage, geometry basis, crosswalk report, ambiguity outcome, migration/correction lineage. | **PARTIAL bounded evidence.** A closed synthetic NHDPlus waterbody-crosswalk family and tests exist; broad identity closure remains proposed. |
| `HYD-DB-04` | **Temporal, freshness, provisional, and no-data visibility** | Every eligible observation or derivative exposes its material time basis, provisional/quality state, stale rule, and no-data semantics; stale and absent are not rendered as current or zero. | Observation/source/retrieval/release/correction times, cadence profile, qualifiers, stale decision, immutable snapshot. | **PROPOSED.** Documentation and selected fixtures carry time semantics; no production freshness telemetry is confirmed. |
| `HYD-DB-05` | **Parameter, unit, datum, CRS, and qualifier integrity** | Values are comparable only under an accepted parameter/unit/datum/CRS profile; unresolved conversions or mixed datums remain `INCOMPLETE`, `ABSTAIN`, or `ERROR`. | Parameter code, unit, vertical datum, CRS, conversion receipt, qualifier, uncertainty, validation report. | **MIXED.** Selected validators exist; generic schema/descriptor validators and policy values remain incomplete or held. |
| `HYD-DB-06` | **Public-safe geometry and sensitive-join protection** | Public outputs expose no private-well owner detail, exact restricted infrastructure or cultural/ecological location, unsafe access detail, or reverse-engineerable protected join; unknown coverage is `INCOMPLETE`. | Sensitivity/rights profile, public-safe geometry transform, aggregation/redaction receipt, audience and join-purpose decision, negative tests, release manifest. | **HOLD.** Policy is unbound and no production exposure-audit producer is confirmed. |
| `HYD-DB-07` | **Correction, withdrawal, derivative invalidation, and rollback** | Every corrected, withdrawn, or superseded release identifies affected derivatives and reaches a bounded corrected, withdrawn, invalidated, or rolled-back state. | Deterministic lineage, Correction/WithdrawalNotice, release identity, cache/index/tile invalidation record, rollback target and drill result. | **PROPOSED / HOLD.** Release and rollback documentation exists; no accepted Hydrology release or propagation drill is confirmed. |
| `HYD-DB-08` | **Implementation and proof/release readiness** | Maturity is reported by evidence-backed components and explicit holds, never by file count, badge, or green placeholder workflow alone. | Contracts, schemas, fixtures, validators, tests, policy, workflows, resolver/API/UI consumers, proofs, review, release, correction, rollback. | **CONFIRMED mixed maturity.** Several bounded families run; broader proof, policy, dashboard, and release remain held or unknown. |

### Candidate drill-downs

These remain `PROPOSED` until a metric contract and safe producer are accepted:

- EvidenceBundle disposition by immutable fixture or released snapshot;
- source-role conflict and model/observation/regulatory anti-collapse failures;
- HUC/reach/waterbody/gauge/well identity ambiguity by versioned family;
- stale, provisional, corrected, withdrawn, and no-data states by eligible public-safe family;
- unit/datum/CRS/parameter incompatibility by declared comparison operation;
- public-safe transform coverage by accepted audience and disclosure profile;
- correction-to-derivative-invalidation state by release identity;
- scaffolding-to-substantive-validation maturity by responsibility root.

[↑ back to top](#top)

---

## 3. Measurement envelope and finite states

Every emitted dashboard measurement should bind:

| Dimension | Required content |
|---|---|
| Identity | Stable indicator ID, metric-contract version, producer identity, computation/spec hash. |
| Snapshot | Immutable run, artifact, or release ID plus content digest; never an unqualified “latest” value. |
| Time | Valid, observed where applicable, source, retrieval, measurement-window, release, correction, and stale time. |
| Population | Eligibility rule, exclusions, numerator, denominator, units, aggregation, null, missing, suppressed, and no-data semantics. |
| Evidence and authority | SourceDescriptor/source head, EvidenceRefs and resolved bundles, contracts/schemas, PolicyDecision, ReviewRecord, ReleaseManifest, validation reports. |
| Hydrology semantics | Object family, source role, parameter code, unit, datum, CRS, qualifier, provisional state, feature identity, source vintage, and crosswalk relation. |
| Spatial scope | Geometry identity, scale/resolution, generalization, uncertainty, sensitive-detail exclusions, and relation to requested map context. |
| Sensitivity and audience | Access label, public-safe profile, authorized audience, minimum-necessary aggregate disclosure, and denial/withholding obligations. |
| Correction | Superseded measurement, correction/withdrawal reference, derivative-invalidation state, rollback target, current disposition. |

Presentation state is separate from policy and runtime outcome:

| Presentation state | Meaning |
|---|---|
| `AVAILABLE` | A public-safe released aggregate is supported for the audience and exact measurement snapshot. |
| `NO_DATA` | The eligible snapshot contains no reportable measurement; this does not prove a real-world absence or zero. |
| `STALE` | A prior measurement identity and age remain visible; it is not presented as current. |
| `INCOMPLETE` | Population, identity, time, evidence, policy, producer, or consumer coverage is insufficient for a complete result. |
| `RESTRICTED` | The value is withheld without leaking a protected record, reason, location, threshold, or transform. |
| `ERROR` | Resolver, validator, policy, producer, telemetry, or delivery failed; never fall back to `AVAILABLE`. |

Governed outward outcomes converge on `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.

`HOLD`, `PASS`, `FAIL`, `RESOLVED`, `UNRESOLVED`, `DENIED`, and `CONTINUE_GOVERNED_CHECKS` are review, validator, package, or orchestration states. They do not automatically become a public `ANSWER` or dashboard `AVAILABLE` state.

[↑ back to top](#top)

---

## 4. Current repository evidence

| Surface | Status at the pinned checkpoint | What it proves | What it does not prove |
|---|---|---|---|
| [`docs/domains/hydrology/README.md`](../../domains/hydrology/README.md) and boundary companions | **CONFIRMED docs** | Hydrology scope, object families, source-role anti-collapse, lifecycle, no-life-safety boundary, and public-client posture are documented. | Current real-world claims, source admission, policy enforcement, dashboard runtime, release, or publication. |
| [`contracts/domains/hydrology/`](../../../contracts/domains/hydrology/README.md) | **CONFIRMED semantic family / mixed maturity** | Twenty-five direct semantic contract documents and explicit source-role, evidence, correction, and release boundaries exist. | Adoption, source truth, complete schema pairing, public use, or production consumer conformance. |
| [`schemas/contracts/v1/domains/hydrology/`](../../../schemas/contracts/v1/domains/hydrology/README.md) | **CONFIRMED mixed schema lane** | Three closed bounded schemas, three shared aliases, four minimal open envelopes, eleven permissive scaffolds, and four missing contract-declared schemas are indexed. | Schema-complete Hydrology, real-world correctness, evidence authenticity, policy, proof, or release. |
| Hydrology Evidence Drawer projection | **CONFIRMED bounded executable** | The [domain schema](../../../schemas/contracts/v1/domains/hydrology/evidence_drawer_payload.schema.json) is a field-free `$ref` projection to the shared closed UI profile; the [component](../../../apps/explorer-web/src/features/domains/hydrology/EvidenceDrawer.tsx) delegates to the shared renderer; focused [tests](../../../tests/validators/domains/hydrology/test_evidence_drawer_convergence.py) and a no-network [workflow](../../../.github/workflows/hydrology-evidence-drawer-convergence.yml) enforce convergence. | Live API transport, evidence authenticity, policy/review/release binding, map-click wiring, telemetry, deployment, or publication. |
| Explorer Hydrology layer seam | **CONFIRMED placeholder** | [`layers.ts`](../../../apps/explorer-web/src/features/domains/hydrology/layers.ts) exists. | It exports only `placeholder = true`; no Hydrology layer adapter, dashboard panel, metric producer, or map binding is established. |
| Internal Hydrology fixture resolution | **CONFIRMED issue-scoped bounded executable** | [`packages/evidence-resolver/`](../../../packages/evidence-resolver/README.md) resolves stable ID `hb1` through one closed manifest to one synthetic fixture with complete-object digest verification; focused tests cover deterministic success and fail-closed tamper, path, manifest, correction, policy, and no-network cases. | Authoritative registry access, source admission, public `ANSWER`, renderability, policy evaluation, review, release, deployment, or production behavior. |
| Hydrology domain workflow | **CONFIRMED readiness and bounded validation** | [`.github/workflows/domain-hydrology.yml`](../../../.github/workflows/domain-hydrology.yml) runs selected schema, fixture-polarity, identity, observation, and crosswalk checks while preserving explicit wider holds. | Hydrologic truth, source activation, active policy, emitted proof, candidate release, rollback rehearsal, deployment, or publication. |
| Hydrology policy lane | **CONFIRMED lane / unbound mixed scaffolding** | [`policy/domains/hydrology/README.md`](../../../policy/domains/hydrology/README.md) inventories eight Rego sources and their conflicting allow/deny scaffold polarity. | An accepted bundle, evaluator, native policy tests, decision emitter, obligation enforcement, production consumer, or release authorization. |
| Governed API route registry | **CONFIRMED finite route inventory** | [`registry.py`](../../../apps/governed-api/src/governed_api/routes/registry.py) registers bootstrap, layers, and evidence routes. | A Hydrology-specific route, dashboard route, production metric endpoint, or end-to-end Hydrology query path. |
| Thin-slice and release documents | **CONFIRMED planning/navigation surfaces** | [`THIN_SLICE.md`](../../domains/hydrology/THIN_SLICE.md) and [`RELEASE_INDEX.md`](../../domains/hydrology/RELEASE_INDEX.md) describe intended no-network proof, release, correction, and rollback closure. | A completed thin slice, emitted ProofPack, accepted release candidate, ReleaseManifest, correction propagation, or rollback drill. |

### Current maturity conclusion

The repository contains more than a proposal-only Hydrology lane: selected schema/fixture families, Evidence Drawer convergence, domain readiness checks, and a manifest-backed synthetic resolver adapter are executable and deterministic.

The repository does **not** yet provide evidence for a running Hydrology dashboard. No production metric contract, metric producer, telemetry store, dashboard route, Hydrology layer adapter, bound policy evaluator, accepted public resolver, released payload, deployed panel, or public publication was verified.

[↑ back to top](#top)

---

## 5. Ownership and review

| Responsibility | Current status | Boundary |
|---|---|---|
| Repository review route | **CONFIRMED:** `@bartytime4life` through [`CODEOWNERS`](../../../.github/CODEOWNERS). | Routing only; not approval, stewardship, or independent review. |
| Hydrology semantic/scientific steward | **NEEDS VERIFICATION** | Owns domain meaning, measurement semantics, and limitations; cannot self-approve policy or release. |
| Source and evidence steward | **NEEDS VERIFICATION** | Owns source admission, source role, rights/currentness, EvidenceBundle closure, and correction support. |
| Regulatory / water-governance reviewer | **NEEDS VERIFICATION** | Reviews NFHL, compact, water-administration, and legal-scope nondetermination boundaries. |
| Sensitivity / privacy reviewer | **NEEDS VERIFICATION** | Reviews wells, owners, infrastructure, exact locations, joins, aggregation, and public-safe geometry. |
| Policy steward / independent approver | **NEEDS VERIFICATION** | Owns accepted decision semantics, bundle/evaluator binding, obligations, and separation of duties. |
| Metric / observability steward | **NEEDS VERIFICATION** | Owns metric contracts, immutable snapshots, telemetry lineage, null/stale semantics, and producer correctness. |
| Explorer / governed-API owner | **NEEDS VERIFICATION** | Owns implementation and governed delivery; cannot redefine evidence, science, or policy. |
| Release / correction / rollback authority | **NEEDS VERIFICATION** | Owns public-use state, correction propagation, withdrawal, rollback drills, and release decisions. |

No owner placeholder may be converted into an executable GitHub identity without verifying the account/team and accepted responsibility assignment.

[↑ back to top](#top)

---

## 6. Implementation and acceptance boundary

### Current implementation pointer

| Surface | Current disposition |
|---|---|
| Review-facing dashboard application | **UNKNOWN.** No Hydrology dashboard route or deployed review panel was verified. Do not present `apps/review-console/` as current implementation without route and consumer evidence. |
| Public map surface | **BOUNDED SEAM.** Explorer shares the Evidence Drawer renderer; Hydrology layer implementation remains a placeholder. |
| Governed API | **PARTIAL GENERAL SCAFFOLD.** Bootstrap, layers, and evidence routes exist; no Hydrology dashboard route is registered. |
| Metric producer and telemetry | **UNKNOWN.** No accepted producer contract, runtime emitter, or telemetry store was verified. |
| Evidence resolution | **BOUNDED INTERNAL ALPHA.** One manifest-backed synthetic fixture path exists; it is non-authoritative and non-renderable. |
| Policy enforcement | **HOLD.** Hydrology policy sources are not bound to an accepted evaluator/consumer profile. |
| Proof and release | **HOLD.** No accepted Hydrology proof pack, release candidate, rollback drill, or published dashboard payload was verified. |

### Minimum acceptance evidence

A running or semi-public Hydrology dashboard remains **HOLD** until evidence appropriate to consequence establishes:

1. accepted metric contracts for every displayed measurement;
2. closed request/response and dashboard-measurement machine profiles;
3. deterministic valid, no-data, stale, incomplete, restricted, corrected, and error fixtures;
4. source admission and immutable snapshot identity for every production input;
5. EvidenceRef-to-EvidenceBundle resolution appropriate to each claim-bearing aggregate;
6. source-role, parameter, unit, datum, CRS, qualifier, provisional, time, and no-data validation;
7. accepted policy bundle/evaluator binding and enforceable obligations;
8. public-safe geometry, privacy, sensitive-join, anti-reidentification, and side-channel negative proof;
9. a governed route and consumer that never reads canonical/internal lifecycle stores directly;
10. snapshot, telemetry, metric-producer, and access-control lineage;
11. correction, withdrawal, derivative invalidation, cache/search/tile refresh, and rollback drills;
12. qualified human review and a separate release decision;
13. deployed evidence showing safe finite states without emergency or regulatory overclaim.

A documentation update, passing schema fixture, receipt, workflow, pull request, or merge cannot satisfy these gates by itself.

[↑ back to top](#top)

---

## 7. Public map, API, and AI boundary

### Public client rules

A future Hydrology dashboard, map, or AI surface may consume only governed finite envelopes and released public-safe artifacts. It must not read:

- RAW, WORK, QUARANTINE, internal candidates, or canonical lifecycle stores;
- unrestricted source payloads or direct source-system responses;
- private-well owner/person/property detail;
- exact restricted infrastructure, cultural, archaeological, ecological, or access-enabling locations;
- direct model output;
- policy internals or sensitive denial reasons;
- unreleased receipts, proofs, review notes, or release candidates.

### Surface-specific behavior

| Surface | Required behavior |
|---|---|
| Map layer | Preserve source role, release identity, time basis, stale/correction state, and public-safe geometry; never use style as truth. |
| Evidence Drawer | Render the shared closed profile through the governed resolver; do not add a parallel Hydrology payload shape. |
| Dashboard card/chart | Bind to an immutable metric snapshot and display population, time window, null/stale semantics, evidence posture, and correction state. |
| Search/export | Preserve release ID, evidence/citation references, source role, time scope, limitations, and correction link. |
| Focus Mode / governed AI | Resolve evidence, apply policy and sensitivity, validate citations, and return `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`; never issue emergency, engineering, insurance, legal-entitlement, or regulatory verdicts. |
| Accessibility and telemetry | Expose equivalent safe state without embedding restricted records, exact locations, prompts, source payloads, or protected reason details. |

A refusal is part of the trust surface. Public explanations should state that information is unavailable, insufficient, stale, or withheld without revealing whether a protected record exists, where it is, or how a protection threshold or transform works.

[↑ back to top](#top)

---

## 8. Open verification register

| ID | Question | Required closure |
|---|---|---|
| `HYD-DASH-OQ-01` | Which application and route own the review-facing Hydrology dashboard? | Current route/component inventory, accepted interface contract, access control, consumer tests, deployment evidence, and rollback path. |
| `HYD-DASH-OQ-02` | What is the accepted dashboard measurement contract and schema home? | Semantic contract, closed schema, compatibility/version decision, fixtures, validator, and producer/consumer tests. |
| `HYD-DASH-OQ-03` | Which indicators remain local Hydrology profiles and which require an Atlas/master-catalog amendment? | Dashboard/Atlas authority review and ADR only where indicator meaning changes. |
| `HYD-DASH-OQ-04` | What source-role vocabulary and policy input profile are accepted end to end? | Contract/schema/policy convergence, source registry, evaluator binding, and negative tests. |
| `HYD-DASH-OQ-05` | Which parameter, unit, datum, CRS, qualifier, provisional, and freshness profiles are authoritative? | Qualified scientific/source review, machine profiles, conversions, fixtures, and correction behavior. |
| `HYD-DASH-OQ-06` | Which public geometry, aggregation, and join rules protect wells, owners, infrastructure, and sensitive locations? | Accepted policy, audience/purpose profiles, negative tests, qualified privacy/sensitivity review, and transform receipts. |
| `HYD-DASH-OQ-07` | How does the internal fixture adapter graduate—or remain permanently test-only? | Accepted resolver contract, authoritative registry/snapshot inputs, consumer decision, policy/review/release binding, and rollback. |
| `HYD-DASH-OQ-08` | What evidence is sufficient to move runtime status from `NEEDS VERIFICATION` to `CONFIRMED`? | Route, producer, telemetry snapshot, access tests, finite-state fixtures, observed deployment, correction and rollback proof. |
| `HYD-DASH-OQ-09` | How are corrections propagated through metrics, API caches, search, maps, tiles, exports, and AI context? | Deterministic dependency graph, invalidation receipts, replay tests, corrected snapshot, and rollback drill. |
| `HYD-DASH-OQ-10` | Who holds accountable domain, scientific/regulatory, policy, metric, security/privacy, and release roles? | Accepted responsibility assignments and independent-review rules; CODEOWNERS alone is insufficient. |

[↑ back to top](#top)

---

## 9. Validation

### Focused documentation validation

This specification change should pass:

- KFM metadata parsing and current path identity;
- one H1 and unique explicit anchors;
- quick-navigation and same-document fragment closure;
- repository-relative link resolution;
- balanced fenced blocks and tables;
- no tabs, trailing whitespace, or missing final newline;
- no credentials, private payloads, exact protected locations, unsafe infrastructure/well detail, or protection-transform parameters;
- exact changed-path and generated-receipt hash closure;
- `git diff --check` and repository-native documentation checks where available.

### Current repository proof surfaces

| Surface | Focused command or workflow | Bounded meaning |
|---|---|---|
| Shared Evidence Drawer convergence | `.github/workflows/hydrology-evidence-drawer-convergence.yml` / focused `unittest` | Shared closed UI schema and renderer delegation only. |
| Hydrology readiness | `.github/workflows/domain-hydrology.yml` | Selected bounded schema, fixture, identity, observation, and crosswalk checks plus explicit holds. |
| Manifest-backed fixture resolver | `make evidence-resolver` and `make evidence-resolver-deny` | One internal deterministic synthetic lookup/integrity profile; no public answer or production lookup. |
| Repository topology and docs | Repository-native validator suite | Path, metadata, links, and declared repository rules only; not Hydrology truth or release. |

### Required negative proof before runtime graduation

Future implementation tests should cover at minimum:

- NFHL represented as observed/current flooding;
- modeled hydrograph represented as an observation;
- missing or unresolved EvidenceBundle;
- ambiguous HUC/reach/waterbody/gauge/well identity;
- stale/provisional value represented as current/final;
- incompatible unit, datum, CRS, parameter, or qualifier comparison;
- no-data represented as zero or real-world absence;
- private-well/person/property or restricted-location join leakage;
- direct public access to lifecycle/internal stores;
- policy/evidence/metric producer unavailable;
- corrected or withdrawn source left visible in metrics, caches, maps, exports, or AI context;
- release or dashboard snapshot without a correction path and rollback target.

[↑ back to top](#top)

---

## 10. Maintenance, correction, and rollback

### Maintenance triggers

Review this specification when any of the following changes:

- a Hydrology contract, schema, fixture, validator, test, policy bundle, source registry, resolver, or workflow materially changes;
- the Explorer Hydrology layer adapter, dashboard route, metric producer, telemetry, or governed API consumer is implemented;
- a source, role vocabulary, unit/datum/time profile, public-safe transform, or sensitivity policy is accepted;
- a ProofPack, release candidate, ReleaseManifest, correction notice, withdrawal, or rollback drill appears;
- Atlas/master indicator meaning or dashboard-placement authority changes;
- a dashboard incident, side-channel finding, stale state, or correction exposes a documentation gap.

### Correction posture

A correction must preserve:

1. prior metric snapshot identity and digest;
2. the corrected source/evidence/policy/release state;
3. affected dashboard measurements and downstream consumers;
4. stale, superseded, withdrawn, invalidated, and corrected dispositions;
5. cache, search, map, tile, export, and AI-context invalidation evidence;
6. the correction explanation at a public-safe level;
7. rollback target and reviewer trail.

Do not rewrite a historical measurement in place or silently reinterpret a prior source role.

### Rollback

For this documentation slice:

- before merge, close the draft pull request and abandon the feature branch;
- after an authorized merge, revert the dashboard specification, catalog row, and generated authoring receipt together or apply a bounded forward correction;
- no source, evidence, policy, runtime, telemetry, release, deployment, or publication state requires restoration.

For future runtime work, rollback must disable the exact route, producer, profile, release, and public alias without falling back to direct stores, stale unmarked values, raw model output, or a less restrictive policy path.

[↑ back to top](#top)

---

**Last updated:** 2026-08-21 · **Edition:** v0.2.0 · **Status:** repository-grounded draft · **Runtime/publication effect:** none
