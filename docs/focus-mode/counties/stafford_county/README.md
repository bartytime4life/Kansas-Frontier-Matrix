<!-- KFM_META_BLOCK_V2

document_id: kfm://docs/focus-mode/counties/stafford-county

title: Stafford County Focus Mode

type: county-focus-mode-readme

status: draft

truth_posture: cite-or-abstain

repository_path: docs/focus-mode/counties/stafford_county/README.md

related:
  - ./stafford_county_focus_mode_build_plan.md
  - ../../../adr/ADR-0027-county-focus-mode-control-plane.md
  - ../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md

notes:
  - Same-path modernization of an existing tracked README.
  - This document summarizes the repository-grounded county boundary; it does not claim source admission, implementation, release, deployment, or publication.
-->

<a id="top"></a>
<a id="stafford-county--focus-mode-build-plan"></a>

# Stafford County Focus Mode

> **Purpose.** Define the public-safe documentation boundary for Stafford County, Kansas, and point maintainers to the county build plan without presenting proposed sources, layers, water-governance behavior, runtime behavior, or release work as current implementation.

> [!IMPORTANT]
> This README is a **documentation boundary**, not a live county product, wildlife-discovery tool, water-right administration system, refuge-operations dashboard, wellfield map, road advisory, or emergency service. The sibling build plan is a draft planning artifact authored on a different repository-evidence boundary. Current repository reads confirm the tracked files and governance surfaces named here, but they do not upgrade the plan's external facts, source rights, object designs, runtime behavior, or release claims into implementation evidence.

## Status at a glance

| Area | Status | Boundary |
|---|---|---|
| County scope | `CONFIRMED` | This tracked lane concerns Stafford County, Kansas. |
| Existing README role | `CONFIRMED` | This file is the county README at the current repository path. |
| Sibling build plan | `CONFIRMED` | `stafford_county_focus_mode_build_plan.md` exists beside this README. |
| Plan repository disclaimer | `STALE / NARROWED` | The plan's no-mounted-repository statement does not describe this implementation session; its proposed paths and behavior still require current verification. |
| County proof slice | `PROPOSED` | The plan centers Quivira National Wildlife Refuge, Rattlesnake Creek, wetland and sand-prairie habitat, water-governance source roles, hydrogeologic context, monitoring references, agriculture, and dated mobility. |
| Source admission | `UNKNOWN` | A source is not admitted merely because the plan cites, links, or discusses it. |
| Runtime/API/UI behavior | `UNKNOWN` | This README does not claim implemented Stafford County routes, contracts, schemas, MapLibre layers, Evidence Drawer behavior, or Focus Mode execution. |
| Current operations and conditions | `UNKNOWN` | Refuge operations, water availability, hunting conditions, drought, flood, roads, and emergencies require current official authority. |
| Release/publication | `UNKNOWN` | A document, commit, pull request, rendered map, or passing check is not governed publication. |

## Contents

- [County boundary](#county-boundary)
- [Proposed proof slice](#proposed-proof-slice)
- [Public-safe rules](#public-safe-rules)
- [Proposed layer and card families](#proposed-layer-and-card-families)
- [Finite outcomes](#finite-outcomes)
- [Source-role posture](#source-role-posture)
- [Repository and placement posture](#repository-and-placement-posture)
- [Relationship to the build plan](#relationship-to-the-build-plan)
- [Validation expectations](#validation-expectations-for-future-implementation)
- [Known unknowns](#known-unknowns)
- [Rollback and correction](#rollback-and-correction)

## County boundary

The Stafford County build plan proposes a map-first experience organized around **Quivira National Wildlife Refuge, the Rattlesnake Creek watershed, wetland and sand-prairie habitat, public water-governance records, hydrogeologic interpretation, monitoring-reference evidence, county-scale agriculture, and dated transportation context**.

Its central trust problem is not simply showing where these themes overlap. It is preserving the differences among:

- refuge-scale public habitat context and exact or inference-enabling sensitive wildlife locations;
- watershed planning and environmental-decision records and legal water-right adjudication;
- administrative source status and private water-user, parcel, well, or operator information;
- historical scientific interpretation and current monitoring or operational conditions;
- a monitoring-location reference and a claim about current water availability, quality, safety, drought, or flood;
- county agricultural aggregates and individual farms, wells, parcels, owners, or irrigation practices;
- a dated transportation notice and live road, closure, passability, routing, or emergency guidance;
- source evidence and generated explanation.

The most important public-safe rule is:

> **Public landscape context is not sensitive-location disclosure, legal water adjudication, private-user inference, infrastructure intelligence, or live operational guidance.**

Missing evidence, source rights, temporal fitness, safe geometry, sensitivity review, legal scope, or release closure should narrow the claim or produce `ABSTAIN`, `DENY`, or another governed finite outcome rather than a plausible-looking map answer.

## Proposed proof slice

The sibling plan proposes a **Quivira–Rattlesnake Creek public-context proof**. In bounded form, that slice would demonstrate that KFM can:

- explain Quivira at refuge scale without exposing exact species occurrences, nests, roosts, migration concentrations, or management-sensitive habitat detail;
- present Rattlesnake Creek watershed, planning, environmental-decision, and administrative context without making legal water-right, impairment, priority, allocation, owner, or private-user conclusions;
- keep precise irrigation, augmentation, monitoring, wellfield, dam, control, and vulnerability-sensitive infrastructure out of normal public output;
- distinguish historical KGS scientific interpretation from current USGS monitoring references and from present operational conclusions;
- show county-scale agricultural totals without creating farm, operator, parcel, well, water-use, ownership, or compliance profiles;
- present dated mobility context without claiming current road, closure, construction, passability, routing, or safety status;
- connect every consequential map feature or card to EvidenceRefs and EvidenceBundles before treating it as authoritative;
- demonstrate visible `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` states through deterministic, no-network fixtures before live-source or public-release work.

These remain **PROPOSED** behaviors until contracts, schemas, fixtures, validators, policy, evidence, review, runtime integration, and release state are verified.

## Public-safe rules

| Rule | Required behavior |
|---|---|
| Evidence before interpretation | Consequential claims resolve through governed evidence; generated language, map styling, source visibility, and model confidence never substitute for support. |
| Cite or abstain | Missing, stale, conflicted, out-of-scope, or role-inappropriate evidence must narrow the answer or return a finite negative state. |
| Ecological precision fails closed | Public Quivira context remains refuge-scale or otherwise reviewed and generalized; exact sensitive wildlife or management-sensitive locations are withheld. |
| Water-governance roles remain distinct | NRCS planning/decision records, KDA/DWR administration, scientific studies, monitoring references, and generated explanations must not collapse into one legal or operational water claim. |
| Private water and property inference is denied | Public records must not identify or infer private water-right holders, irrigation or augmentation wells, parcel owners, operators, priorities, allocations, title, compliance, or legal entitlement. |
| Infrastructure detail is minimized | Precise wells, controls, monitoring configurations, wellfields, refuge operations, dam or water-system vulnerabilities, and other security-sensitive details are excluded or denied. |
| Monitoring is not current condition | A station or historical study does not establish current water availability, safety, quality, drought, flood, impairment, or operational status. |
| Agriculture remains aggregate | County totals may be used only after admission and review; no farm, operator, parcel, well, water-use, ownership, or individual-business profile is created. |
| Mobility evidence is time-bounded | A dated project or road notice must not become live closure, passability, construction, routing, emergency, or safety guidance. |
| Public clients stay downstream of trust | UI, map, search, exports, and AI consume governed and released evidence rather than RAW, WORK, QUARANTINE, internal stores, direct source-system side effects, or direct model output. |
| Correction and rollback remain visible | Future geometry, source, sensitivity, legal-scope, currentness, interpretation, or operational corrections must be able to supersede or withdraw affected products without rewriting history. |

## Proposed layer and card families

The build plan describes the following planning families. Their presence here records proposed scope only; it does not prove implementation, source admission, review, or release.

| Layer or card family | Intended role | Public-safe condition |
|---|---|---|
| Stafford County orientation | County-scale civic and landscape frame | Authoritative geometry, version, rights, and release state verified |
| Quivira refuge context | Public habitat, wetland, sand-prairie, and Central Flyway interpretation | Refuge-scale/generalized geometry; sensitive locations and operations withheld |
| Rattlesnake Creek watershed context | Watershed and landscape relationship | No private-user, legal entitlement, operational, or safety conclusion |
| Water-governance source-role panel | Explain planning, decision, administrative, scientific, and monitoring source roles | Roles, dates, limitations, and non-adjudication posture visible |
| Hydrogeology and historic-science card | Historical stream–aquifer and mineral-intrusion context | Publication date and historic/interpretive status visible; no current-condition claim |
| Monitoring-reference card | Identify a reviewed monitoring source and its bounded scope | Parameter, time, revision, fitness, and release state verified before display |
| Agriculture aggregate layer | County-scale agricultural context | Aggregate only; no parcel, farm, well, operator, or water-use inference |
| Dated mobility context | Secondary transportation and project-history context | No live road, closure, construction, routing, or safety authority |
| Sensitive-detail withhold notice | Explain absent wildlife, water-user, well, and infrastructure precision | Must not confirm hidden configurations or enable harmful inference |
| Evidence and correction panel | Expose source role, time, limitations, review, release, correction, and rollback | Every consequential claim resolves to governed evidence and release state |

## Finite outcomes

For this county lane, the expected public-facing outcome vocabulary is:

- `ANSWER` — released evidence is in scope, citation-valid, time-fit, rights-cleared, sensitivity-safe, policy-safe, and review-complete;
- `ABSTAIN` — evidence, temporal scope, source role, monitoring fitness, legal scope, geometry, rights, or release closure is insufficient;
- `DENY` — the request would expose sensitive wildlife, private water users, precise wells or infrastructure, property details, legal entitlement, operational status, or another protected boundary;
- `ERROR` — a resolver, validator, policy engine, source adapter, identity crosswalk, or runtime dependency failed.

These outcomes are a **proposed design contract**, not proof that the current repository implements them for Stafford County.

Representative proposed reason codes include:

- `SENSITIVE_WILDLIFE_DETAIL_WITHHELD`
- `WATER_RIGHT_OR_PRIVATE_USER_INFERENCE_DENIED`
- `CRITICAL_WATER_INFRASTRUCTURE_DETAIL_WITHHELD`
- `MONITORING_REFERENCE_NOT_CURRENT_CONDITION`
- `CURRENT_OPERATIONAL_STATUS_REQUIRES_AUTHORITY`
- `AGGREGATE_DATA_NOT_PARCEL_OR_OPERATOR_TRUTH`
- `DATED_TRANSPORT_NOTICE_NOT_LIVE_ROUTING`

Reason-code naming and runtime registration remain **NEEDS VERIFICATION**.

## Source-role posture

The build plan lists candidate source families. A candidate source is neither admitted evidence nor public-release authority.

| Source family | Intended role | Must not be treated as |
|---|---|---|
| Stafford County official materials | County identity, services, and bounded civic context | Current emergency authority, private-person profile, property truth, or proof of all historical claims |
| U.S. Fish and Wildlife Service | Refuge mission, public habitat, and broad Quivira context | Permission to expose exact sensitive wildlife, refuge operations, or current field conditions |
| USDA NRCS | Watershed-plan, environmental-review, and decision-record context | Water-right adjudication, private-user identification, or current operational authority |
| Kansas Department of Agriculture / Division of Water Resources | Administrative and public water-governance context | KFM legal conclusion, private holder profile, allocation decision, or entitlement determination |
| Kansas Geological Survey | Historical and scientific hydrogeologic interpretation | Current monitoring, impairment, safety, legal, operational, or emergency authority |
| U.S. Geological Survey | Monitoring-location and observation-reference evidence after admission | Automatic current water availability, quality, safety, drought, flood, or legal conclusion |
| Agricultural statistical sources | Dated county aggregates | Farm, operator, parcel, well, owner, individual-business, or reconstructed private fact |
| Kansas Department of Transportation | Dated project and transportation context | Live routing, closure, construction, passability, travel-safety, or emergency authority |
| Future weather, drought, flood, or refuge-operation authorities | Official-current operational routing after admission | Durable cached KFM safety verdict or AI-authored alert |

## Repository and placement posture

**CONFIRMED:** this README already exists at `docs/focus-mode/counties/stafford_county/README.md`, so this change keeps the tracked path and responsibility root rather than inventing a new documentation home.

**CONFIRMED:** [ADR-0029](../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) is accepted and adopts the exact Directory Rules v2 bytes at `docs/doctrine/directory-rules.md` as the single writable human Directory Rules authority.

**CONFIRMED:** [ADR-0027](../../../adr/ADR-0027-county-focus-mode-control-plane.md) remains `proposed` and records the unresolved conflict between the current singular `docs/focus-mode/` lane and a proposed plural county control plane. This README does not use that unaccepted decision to migrate Stafford County, create a parallel lane, or treat the build plan's proposed tree as current fact.

## Relationship to the build plan

The detailed planning artifact is:

- [Stafford County Focus Mode Build Plan](./stafford_county_focus_mode_build_plan.md)

Use the build plan for proposed layers, objects, source seeds, risk analysis, phases, fixtures, UI ideas, and open verification questions. Use this README for the stable county-boundary summary and current truth posture.

> [!CAUTION]
> The build plan contains point-in-time facts, proposed paths, candidate source uses, numerical source statements, and external checks from its May 2026 authoring run. Before implementation or public use, reverify current facts, source terms, identifiers, rights, dates, geometry, sensitivity, legal scope, reviewer assignments, operational status, and release fitness against authoritative sources and current repository controls.

## Validation expectations for future implementation

A future Stafford County implementation should not be considered complete merely because Markdown or a map exists. At minimum, the changed area should eventually prove:

1. refuge-scale or otherwise approved Quivira geometry with negative fixtures for exact or inference-enabling sensitive wildlife detail;
2. explicit separation among watershed planning, environmental decisions, water administration, historical science, monitoring references, and generated interpretation;
3. denial of private water-right holder, parcel, well, operator, priority, allocation, title, compliance, and legal-entitlement inference;
4. infrastructure minimization with negative fixtures for precise wells, controls, monitoring configurations, wellfields, operations, and vulnerability detail;
5. historical studies and monitoring references cannot become current water-availability, safety, quality, drought, flood, or operational claims;
6. agriculture remains aggregate and cannot create farm, operator, parcel, well, ownership, or water-use profiles;
7. dated transportation evidence cannot become live routing, closure, construction, passability, emergency, or safety guidance;
8. positive and negative fixtures cover `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`;
9. no-network deterministic tests cover ecology, water governance, monitoring semantics, private-user inference, infrastructure, agriculture, and mobility boundaries;
10. every consequential public claim resolves from EvidenceRef to EvidenceBundle;
11. governed API/UI surfaces display evidence, source role, time, policy, limitations, stale, restricted, denied, corrected, and error states;
12. no direct path exists from raw/internal stores, candidate observations, source-system side effects, or model output to public truth;
13. correction, supersession, withdrawal, and rollback propagate through map, timeline, search, cache, export, and AI surfaces;
14. release evidence is appropriate to the significance of ecological, legal, water, infrastructure, agriculture, and mobility claims.

## Known unknowns

The following remain **UNKNOWN** or **NEEDS VERIFICATION** until current implementation evidence proves otherwise:

- which Stafford County source descriptors are admitted;
- current source rights, terms, and derivative-display permissions;
- approved public geometry and generalization thresholds for Quivira, sensitive wildlife, wells, water systems, and infrastructure;
- current water-governance, watershed-plan, administrative, monitoring, refuge-operation, drought, flood, and road status;
- canonical identifiers and temporal semantics for proposed monitoring and administrative records;
- current contracts, schemas, policies, validators, fixtures, and tests applicable to Stafford County;
- governed API routes, Explorer UI components, Evidence Drawer integration, and reason-code registration;
- named ecology, water-governance, legal-scope, infrastructure-security, agriculture, rights, and release reviewers;
- correction propagation through map, timeline, search, cache, export, and AI surfaces;
- any deployed or published Stafford County Focus Mode.

## Rollback and correction

This README is documentation-only. Before merge, rollback is abandonment of the feature branch or pull request. After merge, correction should use a transparent revert or forward-fix PR against the actual merged commit.

A documentation rollback does **not** reverse any separate future source admission, policy decision, water-administration record, release manifest, deployment, publication, or public correction. Those transitions require their own governed records and rollback paths.

## Related

- [Stafford County Focus Mode Build Plan](./stafford_county_focus_mode_build_plan.md)
- [County index](../COUNTY_INDEX.md)
- [Counties Focus Mode overview](../README.md)

[Back to top](#top)
