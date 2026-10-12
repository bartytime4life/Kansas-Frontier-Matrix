<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-geology
title: Geology and Natural Resources Dashboard Specification
type: standard
version: v0.2.0
status: draft; repository-grounded; bounded-validation; dashboard-runtime-unverified; policy-unbound; proof-held; non-release; non-publication
owners: "@bartytime4life (CODEOWNERS review route); Geology, Natural Resources, source/evidence, scientific/regulatory, rights/sensitivity, policy, metric/UI, release/correction, and independent stewards NEEDS VERIFICATION"
created: 2026-05-26
updated: 2026-08-22
policy_label: public
owning_root: docs/
responsibility: "Review-facing Geology and Natural Resources governance-health dashboard specification only; not geologic, scientific, resource, rights/title, engineering, regulatory, policy, runtime, release, or publication authority."
truth_posture: "CONFIRMED current repository evidence / PROPOSED metric contracts and presentation states / UNKNOWN routed dashboard, production telemetry, live-source admission, active policy evaluation, released payloads, deployment, and publication"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 6aaea704230259e4fca30fcc0b9c1a168e12c2c2
  target_prior_blob: 3daa6896f20f135b845f9b097be2b5aba8420858
  dashboard_domain_readme_blob: b44a57576d934d7df4ed3c403b526eeb660df70c
  dashboard_catalog_blob: 82c7859b2782c13e97b1b3d3d55cdf35400fe675
  geology_schema_index_blob: beb2ee7a82ff77305f8259b554e9fe458349a123
  geology_aem_schema_blob: 3ede6999513b3cd443c37de449b4e88f1fe54d24
  geology_geologic_unit_schema_blob: e955613a2602d6ddc69ac03935b543a12aa41200
  geology_evidence_drawer_projection_blob: 912bf397a4783fc88d64c4983a1e39450b598b07
  geology_policy_readme_blob: 71e4a939510712346c3b80e62c47d1770e799c03
  geology_source_registry_readme_blob: 0bb2d794e3179186abfa371a3c99532f50d2c571
  geology_proof_readme_blob: fc07012855bb4019008a3b0dce035dc8088156f6
  geology_release_candidate_readme_blob: f0313cafc641c049d367af82418212e0bad1fc35
  geology_fixture_readme_blob: 04f35c86b9a14d88ae70e4cc906bae99391f2b37
  geology_validator_readme_blob: ebfae810716f8ed8f9b52f85dfb864cb600d0951
  geology_resource_class_test_blob: 55ad09149480f72bd79a714f7df5fe626be19653
  geology_domain_workflow_blob: 74d6de5d27d7704957a89d025fdbbd2a7a01043e
  geology_evidence_drawer_component_blob: ce7594231ed59857ef9b3e37d7a0a9d1286866b4
  geology_layers_placeholder_blob: 7f261e7531795d07573adc871de93aeac25977c6
  geology_evidence_drawer_test_blob: ad7675080b49a99a9d3e61af95bd3e35764a3d26
  geology_evidence_drawer_workflow_blob: d5670253856b9e72b4f2b5240f1c7bf04750131c
  governed_api_route_registry_blob: 3418168d0b267160d6ad6dd87f289e880ef4a024
inspection_boundary: >-
  Current-session GitHub reads covered the complete prior dashboard specification;
  the dashboard catalog and domain-dashboard boundary; current Geology domain,
  semantic-contract, schema, source-registry, policy, fixture, validator, test,
  workflow, proof, release-candidate, Explorer, Evidence Drawer, and governed-API
  surfaces; accepted Directory Rules; CODEOWNERS; and open pull-request/task-branch
  overlap. No live Geology source, production metric producer, telemetry store,
  policy evaluator, proof packet, release manifest, dashboard route, deployed panel,
  correction propagation, rollback drill, or public endpoint was exercised.
related:
  - ../DASHBOARD_CATALOG.md
  - README.md
  - ../../domains/geology/README.md
  - ../../domains/geology/ARCHITECTURE.md
  - ../../domains/geology/OBJECT_FAMILIES.md
  - ../../domains/geology/SOURCE_ROLE_MATRIX.md
  - ../../domains/geology/SENSITIVITY.md
  - ../../domains/geology/MAP_UI_CONTRACTS.md
  - ../../../contracts/domains/geology/README.md
  - ../../../schemas/contracts/v1/domains/geology/README.md
  - ../../../schemas/contracts/v1/domains/geology/aem_survey_campaign.schema.json
  - ../../../schemas/contracts/v1/domains/geology/evidence_drawer_payload.schema.json
  - ../../../policy/domains/geology/README.md
  - ../../../data/registry/sources/geology/README.md
  - ../../../data/proofs/geology/README.md
  - ../../../release/candidates/geology/README.md
  - ../../../fixtures/domains/geology/README.md
  - ../../../tools/validators/domains/geology/README.md
  - ../../../tests/domains/geology/test_source_role_anti_collapse.py
  - ../../../tests/domains/geology/test_aem_campaign.py
  - ../../../tests/domains/geology/test_public_safe_geometry.py
  - ../../../tests/domains/geology/test_production_material_change.py
  - ../../../tests/validators/domains/geology/test_evidence_drawer_convergence.py
  - ../../../apps/explorer-web/src/features/domains/geology/README.md
  - ../../../apps/explorer-web/src/features/domains/geology/EvidenceDrawer.tsx
  - ../../../apps/explorer-web/src/features/domains/geology/layers.ts
  - ../../../apps/governed-api/src/governed_api/routes/registry.py
  - ../../../.github/workflows/domain-geology.yml
  - ../../../.github/workflows/geology-evidence-drawer-convergence.yml
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../../../.github/CODEOWNERS
tags: [kfm, dashboards, domain, geology, natural-resources, stratigraphy, lithology, boreholes, resources, evidence, source-role, sensitivity, public-safe-geometry, correction, rollback, specification]
notes:
  - "v0.2.0 replaces an Atlas-only proposal with a current repository-grounded dashboard specification."
  - "Numeric health thresholds from v0.1 are removed unless and until an accepted metric contract defines the eligible population, evidence source, time window, null semantics, and review authority."
  - "Four bounded no-network Geology profiles are wired in the domain workflow: resource-class anti-collapse, announcement-bound AEM candidate, public-safe geometry assessment, and production material-change assessment."
  - "The shared Evidence Drawer projection and delegation are bounded executable evidence; the Geology layer adapter remains a placeholder and no dashboard or Geology API route is registered."
  - "The Geology policy lane exists but no active Geology policy evaluator, bundle, authenticated decision emitter, or governed consumer is verified."
  - "This revision changes documentation and its generated authoring provenance only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="geology--natural-resources-dashboard-specification"></a>

# Geology and Natural Resources Dashboard Specification

**Repository-grounded review specification for Geology and Natural Resources source-role integrity, claim-class anti-collapse, stratigraphic and lithologic identity, public-safe subsurface representation, evidence closure, correction, rollback, and implementation readiness.**

![status](https://img.shields.io/badge/status-draft-blue)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![runtime](https://img.shields.io/badge/dashboard%20runtime-UNKNOWN-lightgrey)
![proof](https://img.shields.io/badge/proof-bounded%20only-f59e0b)
![policy](https://img.shields.io/badge/policy-unbound-b42318)
![public](https://img.shields.io/badge/public%20exact%20subsurface-DENY-critical)

[Scope](#1-domain-scope) · [Indicators](#2-indicator-subset) · [Contracts](#3-domain-specific-indicators-proposed) · [Measurement](#4-ownership) · [Evidence](#5-implementation-pointer) · [Presentation](#6-review-cadence) · [Public boundary](#7-open-questions) · [Validation](#8-evidence-basis--citations) · [Open work](#9-open-verification-register) · [Maintenance](#10-maintenance-correction-and-rollback)

> [!IMPORTANT]
> **Current checkpoint.** The repository contains substantial Geology documentation and semantic contracts, many machine-schema files of mixed maturity, four bounded no-network validation profiles, a shared Evidence Drawer projection and delegation, and explicit Geology workflow holds. The Geology layer adapter is still a placeholder. The governed API route registry contains only bootstrap, layers, and evidence routes, with no Geology dashboard route. Geology policy remains unbound, the proof lane has no accepted Geology proof packet, and the release-candidate lane has no verified child candidate dossier. No production metric producer, telemetry binding, released dashboard payload, deployed panel, or publication is confirmed.

> [!CAUTION]
> **Geology context is not extraction, title, reserve, engineering, or regulatory authority.** This dashboard must never present a mineral occurrence as a deposit, a deposit as a reserve, a permit or production record as physical geology, a modeled cross-section as observation, a generalized map polygon as exact subsurface truth, or a dashboard trend as mineral-rights, property-title, engineering-suitability, investment, regulatory, emergency, or extraction guidance.

> [!WARNING]
> **Sensitive subsurface and resource details fail closed.** Exact or reverse-engineerable borehole, private-well, well-log, core, sample, geochemistry, sensitive-resource, operator/parcel, or extraction-targetable detail must not appear in ordinary public dashboard data, URLs, logs, exports, tooltips, accessibility text, or client-side state. Client-side filtering is not an access-control boundary.

> [!NOTE]
> `@bartytime4life` is the verified repository review route through `CODEOWNERS`. Routing is not Geology stewardship, scientific review, mineral/property-rights authority, policy approval, independent review, release approval, or publication authority.

---

<a id="1-domain-scope"></a>

## 1. Domain scope and authority boundary

This file specifies a **review-facing governance-health projection** for the Geology and Natural Resources lane. It may summarize posture for:

- bedrock and surficial geologic units, map-unit boundaries, lithology, stratigraphy, geologic age, and structures;
- boreholes, well logs, cores, measured sections, geophysics, geochemistry, cross-sections, and hydrostratigraphic context;
- mineral occurrences, resource deposits, resource estimates, extraction and production context, and reclamation records;
- observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic source roles;
- source identity, rights, sensitivity, source vintage, map scale, authority limits, cadence, correction support, and stale state;
- EvidenceRef-to-EvidenceBundle closure for eligible claim-bearing payloads;
- public-safe geometry, generalization, aggregation, redaction, withholding, uncertainty, and representation receipts;
- validation, policy, review, proof, release, correction, supersession, withdrawal, derivative invalidation, and rollback readiness;
- implementation maturity across documentation, contracts, schemas, fixtures, validators, tests, policy, workflows, packages, API, and Explorer surfaces.

It must not decide:

- scientific truth beyond the cited evidence and accepted domain contracts;
- mineral ownership, land title, lease, permit, reserve, economic viability, engineering suitability, compliance, public safety, or investment value;
- current campaign, extraction, production, reclamation, groundwater, or resource status from a stale or announcement-only source;
- whether an exact subsurface or resource location may be disclosed;
- source admission, policy permission, release approval, deployment, or publication.

A map feature, tile, chart, dashboard card, workflow result, schema pass, generated receipt, model output, or AI summary is not sovereign evidence.

```text
released public-safe artifact or governed finite envelope
  -> validated object, claim class, source role, identity, time, scale, and uncertainty
  -> EvidenceRef -> EvidenceBundle resolution
  -> rights / sensitivity / policy / review / release checks
  -> aggregate dashboard measurement
  -> restricted, abstaining, stale, incomplete, held, or error state when closure fails
```

### Domain anti-collapse rules

| Distinction | Required dashboard behavior |
|---|---|
| `GeologicUnit` vs. `Lithology` vs. `GeologicAge` vs. `StratigraphicInterval` | Preserve distinct identities, vocabularies, source vintages, and correlation uncertainty. Do not treat a label match as equivalence. |
| Borehole vs. well log vs. core/sample vs. geochemistry | Report the object family and support type explicitly. A borehole coordinate does not prove log, sample, interval, or interpretation content. |
| Mineral occurrence vs. resource deposit vs. resource estimate | Never normalize these into one “resource” truth class. Estimates require classification and assumption support; occurrences are not deposits or reserves. |
| Permit or production record vs. physical geology | Keep regulatory/administrative/production evidence separate from observed or interpreted geology. |
| Cross-section or inversion vs. observation | Label interpretation/model identity, version, assumptions, uncertainty, and reality boundary. |
| Extraction site vs. ownership/title/lease/permit | Physical-site context does not prove legal rights, operator authority, or current permit status. |
| Hydrostratigraphic context vs. Hydrology observation | Geology may describe units and relations; Hydrology owns water measurements, flood observations, and water-status claims. |
| Generalized map polygon vs. exact subsurface support | Preserve source scale, geometry lineage, generalization state, and uncertainty. Never reverse-infer protected exact locations. |
| Historical announcement vs. current operational state | Preserve the reported historical state and explicit current-state unknowns. |
| Validation success vs. evidence/release | A green bounded check proves only its declared fixture or structural profile; it does not create source truth, policy permission, proof closure, release, or publication. |

[Back to top](#top)

---

<a id="2-indicator-subset"></a>

## 2. Indicator subset and panel model

The dashboard should organize indicators into seven review panels. These are **PROPOSED presentation groupings**, not proof that a panel, route, metric producer, or telemetry source exists.

| Panel | Review question | Typical drill-downs | Public-safe default |
|---|---|---|---|
| Evidence and source coverage | Are eligible claims tied to admitted, role-typed, versioned sources and resolvable evidence? | source family, source role, evidence disposition, stale/correction state | Counts and states only; no restricted source payload |
| Claim-class integrity | Are occurrence, deposit, estimate, permit, production, reserve, observation, interpretation, and model roles kept distinct? | object family, requested use, rejection reason, fixture profile | Do not reveal protected coordinates or targetability |
| Stratigraphy and identity | Are unit, lithology, age, interval, boundary-version, and crosswalk identities explicit and versioned? | vocabulary/version, ambiguity class, source scale, correlation state | Show ambiguity and lineage; never silently coerce |
| Subsurface and public-safe representation | Are exact or identifying records restricted, transformed, and review-bound? | transform class, representation state, review/policy outcome, scale class | Generalized/withheld summaries only |
| Time, material change, and correction | Are source vintage, announcement time, observation time, retrieval time, release time, stale state, and correction lineage distinct? | snapshot, comparison outcome, correction/withdrawal state | No unqualified “current” or “latest” |
| Policy, proof, and release readiness | Are policy evaluation, proof closure, review, candidate, release, correction, and rollback dependencies complete? | component readiness, hold reason, missing dependency | Fail closed; no implicit allow from file presence |
| API, MapLibre, and dashboard readiness | Can governed clients consume a released, finite, public-safe envelope without internal-store access? | route, schema, renderer delegation, layer adapter, telemetry producer | `ABSTAIN`, `DENY`, or `ERROR` when closure is absent |

### Permitted filters

A future implementation may expose bounded, low-cardinality filters such as:

- object family;
- source role;
- finite outcome or hold reason;
- contract/schema profile;
- source or artifact vintage;
- correction, supersession, withdrawal, or stale state;
- release state;
- public-safe geography or scale class;
- review window.

### Prohibited or restricted filters

Do not offer ordinary public filters that enable:

- exact borehole, private-well, core, sample, well-log, geochemistry, sensitive-resource, or extraction-targetable lookup;
- operator, parcel, owner, title, lease, permit, or private-person joins;
- reverse engineering of generalized locations through low-count intersections;
- sensitive source identifiers, endpoint details, restricted reason text, or hidden transform parameters;
- client-side access to RAW, WORK, QUARANTINE, internal registries, proof stores, or candidate-only payloads.

[Back to top](#top)

---

<a id="3-domain-specific-indicators-proposed"></a>

## 3. Domain-specific indicator contracts

The following are **PROPOSED metric contracts**, not implemented telemetry. Numeric targets from v0.1 are intentionally removed. Before any percentage, rank, trend, or threshold is shown, the producer must define the eligible population, numerator, denominator, measurement window, immutable snapshot, evidence inputs, null/no-data semantics, sensitivity profile, correction behavior, and review authority.

| ID | Indicator | Proposed healthy posture | Required support | Current repository state |
|---|---|---|---|---|
| `GEO-DB-01` | **Source-role and resource-claim anti-collapse** | Every eligible item preserves its declared source role and claim class; occurrence, deposit, estimate, permit, production, reserve, interpretation, model, and observation conflicts remain visible and never normalize to a stronger claim. | SourceDescriptor/source head, semantic contract, machine profile, validation findings, evidence refs, policy/review state, release identity. | **CONFIRMED bounded proof only.** The frozen resource-class profile has deterministic positive and negative fixtures; broad production records and source admission remain unverified. |
| `GEO-DB-02` | **EvidenceBundle and citation closure** | Every eligible claim-bearing payload resolves to admissible, schema-valid support or reaches `ABSTAIN`, `DENY`, `HOLD`, or `ERROR`. | EvidenceRef, EvidenceBundle, citation validation, source role, rights, sensitivity, correction history, policy/review result, release identity, digest. | **PARTIAL.** Shared EvidenceBundle support and a field-free Geology Evidence Drawer projection exist; no accepted Geology proof packet or production resolver path is confirmed. |
| `GEO-DB-03` | **Contract/schema pairing and enforcement maturity** | Every metric-bearing object uses an accepted semantic contract and a field-enforcing, closed schema profile with fixtures and validators; permissive scaffolds remain visible as incomplete. | Contract, schema `$id`, field/closed-shape checks, fixtures, validator, registry entry, review status, compatibility/migration note. | **MIXED.** Many Geology schemas exist, but maturity varies from closed fixture profiles to field-free permissive scaffolds such as `geologic_unit.schema.json`. |
| `GEO-DB-04` | **Stratigraphic, lithologic, age, and boundary identity integrity** | Unit, lithology, age, interval, boundary version, and correlation identities remain version-bound; ambiguous or many-to-many relations are represented rather than silently collapsed. | Source map/version, vocabulary/edition, stable object IDs, correlation/crosswalk report, scale and uncertainty, supersession/correction lineage. | **PROPOSED.** Contracts and documentation exist; no broad accepted identity/canonicalization metric producer is confirmed. |
| `GEO-DB-05` | **Public-safe subsurface and resource representation** | Ordinary public outputs contain no exact or reverse-engineerable restricted subsurface/resource detail and bind each generalized, aggregated, redacted, or withheld representation to reviewable support. | Sensitivity/rights profile, source geometry posture, public-safe transform declaration, representation/redaction/aggregation receipt, scale and uncertainty, PolicyDecision, ReviewRecord, ReleaseManifest. | **CONFIRMED bounded assessment / HOLD for release.** The public-safe geometry profile validates metadata and denial conditions but performs no transform and authorizes no public output. |
| `GEO-DB-06` | **Temporal, material-change, and current-state discipline** | Historical announcement, source vintage, production snapshot, retrieval, comparison, release, correction, and stale times remain distinct; no announcement or aggregate is treated as present operational truth. | Immutable snapshots, source-head metadata, material-change profile, observation/announcement/retrieval/release/correction times, rights state, comparison outcome. | **CONFIRMED bounded profiles only.** The AEM fixture keeps current campaign state unknown; the production material-change profile compares pinned metadata without live requests or publication. |
| `GEO-DB-07` | **Policy, review, proof, release, correction, and rollback readiness** | Every public candidate has an active policy decision, accountable review, claim-scoped proof support, release manifest, correction path, derivative invalidation plan, and rollback target. | Policy input/decision, ReviewRecord, EvidenceBundle/proof packet, candidate dossier, PromotionDecision, ReleaseManifest, Correction/WithdrawalNotice, rollback evidence. | **HOLD.** Geology policy is unbound, no accepted Geology proof packet is confirmed, and the release-candidate lane has no verified child candidate dossier. |
| `GEO-DB-08` | **API, MapLibre, Evidence Drawer, and dashboard implementation readiness** | Governed clients receive only released public-safe finite envelopes; domain rendering delegates to shared controlled components and has tested layer, route, metric, and access behavior. | Governed API route and contract, released layer manifest, shared Evidence Drawer schema/renderer, tested layer adapter, metric producer, telemetry binding, access tests, deployment evidence. | **PARTIAL bounded UI proof / runtime UNKNOWN.** Evidence Drawer delegation is tested; the Geology layer adapter is a placeholder; no Geology dashboard/API route, metric producer, telemetry, or deployment is confirmed. |

### Why no fixed thresholds appear here

A threshold is a policy- and population-dependent decision. The prior `>99.9%` and `100%` targets lacked:

- a defined eligible population;
- immutable source and evidence inputs;
- a measurement window;
- null, missing, stale, suppressed, and restricted semantics;
- an accepted metric owner and reviewer;
- correction and rollback behavior.

Those targets are retained only as document lineage. Future threshold profiles must be versioned, reviewed, and independently testable.

[Back to top](#top)

---

<a id="4-ownership"></a>

## 4. Measurement envelope, finite states, and ownership

Every emitted dashboard measurement should bind:

| Dimension | Required content |
|---|---|
| Identity | Stable indicator ID, metric-contract version, producer identity, computation/spec hash. |
| Snapshot | Immutable run, source, artifact, proof, or release ID plus digest; never an unqualified “latest.” |
| Time | Valid, observed/announcement where applicable, source, retrieval, comparison-window, release, correction, and stale time. |
| Population | Eligibility rule, exclusions, numerator, denominator, units, aggregation, null, missing, suppressed, restricted, and no-data semantics. |
| Domain semantics | Object family, source role, claim class, vocabulary/edition, source scale, geometry support, uncertainty, interpretation/model state. |
| Evidence and authority | SourceDescriptor/source head, EvidenceRefs and resolved bundles, contracts/schemas, validation, policy, review, proof, release, correction, rollback. |
| Sensitivity | Audience, rights, sensitivity tier/profile, public-safe transform state, anti-inference checks, minimum-cell or disclosure rules where accepted. |
| Outcome | Finite state and stable reason code; no ambiguous “green/healthy” value without its basis. |
| Lineage | Supersedes/superseded-by, correction/withdrawal references, affected derivatives, prior safe target. |

### Finite dashboard states

| Dashboard state | Meaning | Public-facing mapping |
|---|---|---|
| `SUPPORTED` | Measurement is evidence-backed, policy-safe, reviewed, released, and in scope. | `ANSWER` |
| `NO_DATA` | Eligible population exists but no supported data is available. | `ABSTAIN` |
| `STALE` | Source, evidence, rights, review, model, map, policy, or release support aged out. | `ABSTAIN` |
| `PARTIAL` | Some eligible support is present, but closure or coverage is incomplete. | Bounded `ANSWER` only when allowed; otherwise `ABSTAIN` |
| `RESTRICTED` | Measurement or drill-down is withheld or generalized for rights/sensitivity reasons. | `DENY` or public-safe summary |
| `REVIEW_PENDING` | A metric, policy, scientific, rights, sensitivity, or release review is incomplete. | `ABSTAIN` / `HOLD` |
| `CORRECTED` | Current value supersedes a prior value with visible correction lineage. | `ANSWER` with correction notice |
| `WITHDRAWN` | Supporting claim, source, proof, or release was withdrawn. | `ABSTAIN` / `DENY` |
| `ERROR` | Producer, resolver, validator, policy runtime, store, or delivery path failed. | `ERROR` |

### Ownership model

| Responsibility | Required role | Current evidence |
|---|---|---|
| Repository review routing | `@bartytime4life` via CODEOWNERS | `CONFIRMED` routing only |
| Geology and Natural Resources meaning | Geology domain steward and qualified scientific reviewers | `NEEDS VERIFICATION` |
| Source identity, rights, and cadence | Source/registry and rights stewards | `NEEDS VERIFICATION` |
| Subsurface/resource sensitivity | Sensitivity, security, and disclosure reviewers | `NEEDS VERIFICATION` |
| Metric definition and telemetry | Metric/observability steward plus domain reviewer | `NEEDS VERIFICATION` |
| Policy evaluation | Policy steward and authenticated policy runtime | `UNKNOWN` / unbound |
| Proof and evidence closure | Evidence/proof steward | `NEEDS VERIFICATION` |
| UI and accessibility | Explorer/UI and accessibility stewards | `NEEDS VERIFICATION` |
| Release, correction, withdrawal, rollback | Separate accountable release/correction roles when maturity warrants | `NEEDS VERIFICATION` |

No dashboard producer may self-approve its own metric, policy significance, release, or correction closure.

[Back to top](#top)

---

<a id="5-implementation-pointer"></a>

## 5. Current repository evidence and readiness matrix

| Surface | Current bounded evidence | What it does not prove |
|---|---|---|
| Domain documentation | The Geology lane has extensive scope, architecture, object-family, lifecycle, source-role, sensitivity, map/UI, API, and runbook documentation. | Scientific correctness, source activation, runtime behavior, policy enforcement, release, or publication. |
| Semantic contracts | `contracts/domains/geology/` contains a broad family including geologic units, ages, boreholes, cores, cross-sections, geochemistry, extraction sites, AEM campaigns, and resource objects. | Accepted vocabulary, complete field pairing, production consumers, or release readiness. |
| Schema lane | The current tree contains many `.schema.json` files, including closed fixture-specific profiles and permissive scaffolds. | Uniform maturity, accepted schema authority for every object, or broad validation coverage. |
| Resource-class profile | Deterministic no-network validator/tests preserve occurrence, deposit, and estimate distinctions and deny known collapse cases and precise-location leakage. | Canonical reserve/resource classification, live data validity, rights, policy, or release. |
| AEM announcement profile | Closed schema, source-descriptor binding, fixtures, validator, and tests preserve a 2026-05-11 historical planned announcement while keeping current campaign state unknown and binding no acquisition evidence. | Current campaign state, acquisition, processing/inversion products, source activation, or public release. |
| Public-safe geometry profile | Bounded metadata assessment denies coordinate material and requires restricted exact-source posture, generalized/withheld declarations, review, and policy summaries. | Execution of a geometry transform, safe transform proof, release approval, or public serving. |
| Production material-change profile | Version-pinned comparison profile emits bounded material-change states without live KGS requests and keeps production evidence distinct from deposit/estimate/reserve truth. | Current production, source rights, source activation, policy, or publication. |
| Domain workflow | `domain-geology.yml` executes four bounded no-network profiles and explicitly holds broader proof and release readiness. | Geology truth, active policy, EvidenceBundle closure, release, deployment, or publication. |
| Policy lane | The Geology policy directory and documentation are repository-grounded, but Rego files are default-only scaffolds and no accepted evaluator/bundle/consumer is verified. | An active fail-closed Geology policy decision path. |
| Source registry | A subtype-first Geology source-registry lane exists, but a domain-first sibling also exists and topology/record authority remains unresolved. | Broad admitted-source inventory, active connectors, current rights, or public authority. |
| Proof/release | Shared EvidenceBundle support is fielded; Geology proof and release-candidate READMEs record explicit holds and no verified child candidate dossier. | Claim-scoped Geology proof closure, release manifest, correction propagation, or rollback drill. |
| Evidence Drawer | The Geology schema is a field-free projection to the shared closed payload; the domain component delegates to the shared renderer; focused tests/workflow enforce convergence. | A Geology-specific transport, dashboard route, released payload, or public answer. |
| Layers and governed API | `layers.ts` is a placeholder; the governed API registry contains only bootstrap, layers, and evidence routes. | A Geology layer manifest, Geology/dashboard API route, metric producer, telemetry binding, or deployed panel. |

### Maturity rule

Report maturity by **evidence-backed component**, not by file count, badges, commit count, or green placeholder workflows.

A bounded profile may be `CONFIRMED` while the broader dashboard remains `UNKNOWN` or `HOLD`. Conversely, a populated directory does not imply active sources, policy, proof, release, or runtime behavior.

[Back to top](#top)

---

<a id="6-review-cadence"></a>

## 6. Presentation, accessibility, review cadence, and side-channel safety

### Card contract

Each card or table must expose:

- indicator name and stable ID;
- finite state and stable reason code;
- immutable snapshot/run/release identity;
- measurement window and “as of” timestamp;
- numerator/denominator or explicit non-ratio method;
- source-role and claim-class coverage;
- uncertainty and limitations;
- evidence, policy, review, release, correction, and rollback posture;
- a safe drill-down or a clear reason why drill-down is restricted.

### Accessibility

- Do not encode state by color alone.
- Use text labels, table summaries, keyboard navigation, and deterministic reading order.
- Announce stale, restricted, corrected, withdrawn, partial, and error states.
- Keep sensitive coordinates, identifiers, operators, parcels, owners, sources, and denial details out of accessible names, URLs, DOM attributes, client logs, and exports.
- Ensure charts have equivalent tabular data and explicit units.
- Do not use tooltips as the only location for evidence or limitation text.

### Review cadence

| Trigger | Required review |
|---|---|
| Contract, schema, vocabulary, or object-family change | Re-evaluate affected indicator contracts and anti-collapse rules. |
| New or changed source, endpoint, rights term, cadence, or source role | Recompute source eligibility and stale/correction posture. |
| Public-safe geometry or sensitivity-profile change | Repeat disclosure, side-channel, anti-inference, accessibility, and export review. |
| Policy bundle/evaluator change | Revalidate decision normalization, reason/obligation handling, and failure behavior. |
| Evidence/proof/release/correction change | Recompute closure and derivative invalidation state. |
| API, UI, layer, dashboard, or telemetry implementation | Run contract, access, finite-state, no-direct-store, accessibility, and rollback checks. |
| A metric threshold or eligible population changes | Version the metric contract; do not silently rewrite historical values. |
| Incident, source withdrawal, correction, or rights change | Mark affected metrics stale/restricted/withdrawn, propagate correction, and preserve prior lineage. |

### Side-channel controls

A future dashboard must be tested against:

- low-count and unique-record inference;
- intersections across geography, object family, source, time, and claim class;
- chart labels, tooltips, URLs, logs, caches, analytics events, exports, screenshots, and accessibility text;
- change-over-time differencing that reveals a withheld location or source;
- “no data” patterns that distinguish absence from restricted suppression;
- joins with parcel, operator, person, title, permit, or infrastructure data.

[Back to top](#top)

---

<a id="7-open-questions"></a>

## 7. Public map, API, export, search, and AI boundary

### Governed client rule

Ordinary clients may consume only:

- released public-safe artifacts;
- governed finite response envelopes;
- released layer/style/tile manifests;
- catalog records and EvidenceBundle projections approved for the audience;
- correction-aware and rollback-aware public state.

They must not consume RAW, WORK, QUARANTINE, candidate-only, registry-internal, proof-internal, exact restricted, or direct model/runtime stores.

### Current implementation boundary

- The Geology domain component delegates to the shared Evidence Drawer and contains no transport.
- The Geology layer adapter remains a placeholder.
- The governed API route registry does not contain a Geology dashboard route.
- No production metric producer, telemetry store, access-control binding, released Geology dashboard payload, deployment, or public endpoint was verified.

### MapLibre behavior

A future Geology map/dashboard integration should:

- render only released public-safe layers;
- display source role, claim class, map/source vintage, scale, uncertainty, stale state, correction state, and release identity;
- preserve generalized/withheld geometry semantics;
- prevent reverse inference through zoom, selection, export, query, or cross-layer joins;
- treat cross-sections, inversions, interpolations, and reconstructions as interpretive/model products with reality-boundary language;
- route feature inspection through the shared Evidence Drawer and governed API.

### Export and search

- Exports must preserve release ID, evidence/citation pointers, source role, claim class, scale, public-safe representation state, limitations, and correction status.
- Search indexes must not reveal exact restricted locations, sensitive source IDs, hidden reason text, or stale/withdrawn results as current.
- Static delivery is allowed only for already released public-safe artifacts and must not become a second trust authority.

### Governed AI

AI may summarize released, resolvable, policy-safe evidence with citations and bounded confidence. It must:

- return `ABSTAIN`, `DENY`, or `ERROR` when evidence, rights, sensitivity, review, release, or tool state is insufficient;
- preserve occurrence/deposit/estimate/permit/production/reserve and observation/model distinctions;
- avoid extraction targeting, investment, mineral-rights, title, legal, engineering, regulatory, or safety guidance;
- disclose uncertainty, source scale, map vintage, interpretation/model status, and correction state;
- never treat dashboard values, generated prose, vector search, map pixels, or cross-sections as root truth.

[Back to top](#top)

---

<a id="8-evidence-basis--citations"></a>

## 8. Validation, negative proof, evidence basis, and rollback tests

### Current bounded repository commands

These commands are repository-present and are intended to run no-network:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/geology/test_source_role_anti_collapse.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/geology/test_aem_campaign.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 PYTHONHASHSEED=0 \
  python -m pytest -q -p no:cacheprovider \
  tests/domains/geology/test_public_safe_geometry.py

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 PYTHONHASHSEED=0 \
  python -m pytest -q -p no:cacheprovider \
  tests/domains/geology/test_production_material_change.py

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest -q \
  tests.validators.domains.geology.test_evidence_drawer_convergence
```

The domain workflow also executes the associated validators and expected-invalid fixture rejection.

### Required dashboard validation before implementation claims

| Check | Required negative case |
|---|---|
| Metric-contract validation | Missing population, denominator, snapshot, time window, null semantics, or owner must fail. |
| Claim-class anti-collapse | Occurrence-as-deposit, estimate-as-observation/reserve, permit/production-as-deposit, and model-as-observation must fail closed. |
| Schema maturity | A field-free permissive scaffold cannot be counted as field-enforcing coverage. |
| Identity/vocabulary | Ambiguous stratigraphic/lithologic/age/boundary relations must not coerce to one identity. |
| Public-safe representation | Exact or reverse-engineerable subsurface/resource detail must be denied; missing transform/review support must hold. |
| Temporal/currentness | Announcement-only, stale, corrected, withdrawn, or unmatched snapshots must not display as current. |
| Policy/evidence/release | Missing policy, EvidenceBundle, review, proof, release, correction, or rollback support must not yield `SUPPORTED`. |
| API/UI boundary | Direct internal-store access, direct model traffic, unvalidated response envelopes, or sensitive client state must fail. |
| Accessibility/side channel | Sensitive information in accessible names, tooltips, URLs, logs, exports, or low-count intersections must fail. |
| Correction/rollback | Corrected or withdrawn support must propagate to affected metric, map, search, export, cache, and AI surfaces. |

### Evidence hierarchy for this specification

1. Current repository files, schemas, contracts, tests, workflows, manifests, and generated artifacts.
2. Accepted Directory Rules and ADR-0029 for placement and authority.
3. Current Geology domain documentation and planning lineage.
4. Atlas/dashboard doctrine as orientation only.
5. Memory and generic assumptions are not evidence.

### What a green check means

A green check proves only the declared bounded profile. It does not prove:

- live-source admission or source rights;
- scientific correctness of a geologic interpretation or resource claim;
- active policy evaluation;
- EvidenceBundle/proof closure;
- release, deployment, or publication;
- a running dashboard or public API;
- safe disclosure beyond the tested profile.

[Back to top](#top)

---

<a id="9-open-verification-register"></a>

## 9. Open verification register

- [ ] `GEO-DB-OQ-01` — Assign accountable Geology/Natural Resources, source, rights, sensitivity, policy, metric, UI, proof, release, correction, and independent review roles.
- [ ] `GEO-DB-OQ-02` — Adopt a versioned dashboard-measurement envelope or identify the existing shared contract that this spec must use.
- [ ] `GEO-DB-OQ-03` — Reconcile the subtype-first and domain-first Geology source-registry lanes without creating parallel descriptor authority.
- [ ] `GEO-DB-OQ-04` — Inventory and classify every Geology schema as closed/field-enforcing, bounded fixture profile, permissive scaffold, compatibility projection, transitional, or deprecated.
- [ ] `GEO-DB-OQ-05` — Define accepted stratigraphic, lithologic, geologic-age, boundary-version, and correlation vocabularies and ambiguity behavior.
- [ ] `GEO-DB-OQ-06` — Bind Geology policy source to an accepted evaluator, normalized decision vocabulary, authenticated decision emitter, governed consumer, and failure mode.
- [ ] `GEO-DB-OQ-07` — Establish a claim-scoped Geology proof profile and resolver behavior without exposing restricted support.
- [ ] `GEO-DB-OQ-08` — Define public-safe geometry and anti-inference acceptance criteria, transform receipts, review thresholds, and export restrictions.
- [ ] `GEO-DB-OQ-09` — Define immutable source/material-change snapshots, stale rules, correction propagation, and production/announcement currentness semantics.
- [ ] `GEO-DB-OQ-10` — Implement and test a released Geology layer adapter; the current file is a placeholder.
- [ ] `GEO-DB-OQ-11` — Decide whether a dedicated dashboard route is needed or whether a shared governed metrics endpoint should serve this spec.
- [ ] `GEO-DB-OQ-12` — Implement a production metric producer and telemetry binding with no direct access to canonical/internal stores.
- [ ] `GEO-DB-OQ-13` — Define correction, withdrawal, cache/index/tile invalidation, AI/search propagation, and rollback drill evidence.
- [ ] `GEO-DB-OQ-14` — Reconcile dashboard documentation placement/status under the broader `docs/dashboards/` ADR/verification backlog.
- [ ] `GEO-DB-OQ-15` — Confirm all repository-relative links, current schema/test/workflow inventories, and current main evidence before operational reliance.

[Back to top](#top)

---

<a id="10-maintenance-correction-and-rollback"></a>

## 10. Maintenance, correction, and documentation rollback

### Maintenance triggers

Re-review this specification when any of the following changes:

- Geology object-family, source-role, claim-class, vocabulary, schema, policy, or source-registry authority;
- public-safe geometry, sensitivity, rights, review, or anti-inference rules;
- EvidenceBundle/proof, release, correction, withdrawal, or rollback contracts;
- Geology validators, fixtures, tests, workflows, metrics, telemetry, API routes, Explorer components, or layer adapters;
- dashboard catalog status, dashboard placement decision, or owner assignments;
- a live source, released Geology artifact, public dashboard, or material correction is introduced.

### Correction behavior

When evidence, source role, claim class, rights, sensitivity, policy, review, or release support changes:

1. mark affected measurements `STALE`, `RESTRICTED`, `CORRECTED`, `WITHDRAWN`, or `ERROR` as appropriate;
2. preserve the prior immutable snapshot and reason;
3. identify affected map layers, tiles, caches, search indexes, exports, dashboards, Evidence Drawer payloads, and AI responses;
4. require a new reviewed measurement snapshot rather than editing history in place;
5. maintain forward and backward correction/supersession links.

### Documentation rollback

The deterministic documentation rollback target for this revision is prior blob:

```text
3daa6896f20f135b845f9b097be2b5aba8420858
```

Before merge, close the draft pull request and abandon the feature branch. After an authorized merge, restore the prior blob or transparently revert the documentation commit through normal Git history. A documentation revert does not reverse source admission, evidence, policy, telemetry, release, deployment, or public state because this specification creates none.

### Non-effects

This file does not:

- activate a source or connector;
- define Geology truth, rights, title, reserve, engineering, regulatory, or extraction conclusions;
- evaluate policy;
- create a metric, telemetry producer, EvidenceBundle, proof packet, review, release manifest, correction notice, withdrawal notice, or rollback card;
- implement a dashboard route, panel, layer, export, search index, or AI answer;
- release, deploy, promote, publish, merge itself, or change repository settings.

[Back to top](#top)
