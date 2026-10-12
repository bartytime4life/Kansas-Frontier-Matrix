<!-- KFM_META_BLOCK_V2

document_id: kfm://docs/focus-mode/counties/seward-county

title: Seward County Focus Mode

type: county-focus-mode-readme

status: draft

truth_posture: cite-or-abstain

repository_path: docs/focus-mode/counties/seward_county/README.md

related:
  - ./seward_county_focus_mode_build_plan.md
  - ../../../adr/ADR-0027-county-focus-mode-control-plane.md
  - ../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md

notes:
  - Same-path modernization of an existing tracked README.
  - This document summarizes the repository-grounded county boundary; it does not claim source admission, implementation, release, deployment, or publication.
-->

<a id="top"></a>

# Seward County Focus Mode

> **Purpose.** Define the public-safe documentation boundary for Seward County, Kansas, and point maintainers to the county build plan without presenting proposed source, runtime, operational, health, demographic, or release behavior as current implementation.

> [!IMPORTANT]
> This README is a **documentation boundary**, not a live county product, transportation service, utility monitor, public-health advisory, industrial-operations surface, or demographic profiling tool. The sibling build plan contains proposed architecture and source-derived planning material checked in June 2026. Its statements remain subordinate to current repository evidence, authoritative-current sources, admitted evidence, policy, review, and release state.

## Status at a glance

| Area | Status | Boundary |
|---|---|---|
| County scope | `CONFIRMED` | This tracked lane concerns Seward County, Kansas. |
| Existing README role | `CONFIRMED` | This file is the county README at the current repository path. |
| Sibling build plan | `CONFIRMED` | `seward_county_focus_mode_build_plan.md` exists beside this README. |
| County proof slice | `PROPOSED` | The plan combines Liberal and cross-border mobility, aviation, irrigated agriculture, municipal water, wastewater/wetland context, recreation, demographics, GIS limitations, and Hugoton-area energy history. |
| Source admission | `UNKNOWN` | A source is not admitted merely because the plan cites, links, or discusses it. |
| Runtime/API/UI behavior | `UNKNOWN` | This README does not claim implemented county routes, contracts, schemas, MapLibre layers, Evidence Drawer behavior, or Focus Mode execution. |
| Current operations | `UNKNOWN` | Flights, roads, closures, utility status, burn bans, alerts, facility operations, and emergencies require current official authority. |
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

The Seward County build plan proposes a map-first experience organized around **Liberal, the Kansas–Oklahoma border, U.S. 54/83 planning context, Liberal Mid-America Regional Airport, county-scale irrigated agriculture, municipal water and wastewater roles, Arkalon Park, public GIS, demographic aggregates, and Hugoton-area energy history**.

Its central trust problem is multi-system role separation. Public pages can expose transportation studies, airport schedules, utility reports, wastewater operations, park rules, demographic tables, GIS layers, industrial history, alerts, and service notices that look immediately actionable but may be stale, scope-limited, legally non-authoritative, privacy-sensitive, or operationally risky when detached from their original source and time basis.

The most important public-safe rule is:

> **County context is not live operations, household health advice, infrastructure intelligence, immigration or employment profiling, pollution attribution, or property and farm truth.**

A map, evidence object, search result, export, or AI answer must not convert general civic information into a present-tense flight, road, utility, closure, burn-ban, emergency, facility-operation, potability, compliance, immigration-status, employment, landowner, parcel, individual-farm, private-well, or wildlife-location conclusion. Missing authority, currentness, evidence, rights, sensitivity review, or release closure should produce `ABSTAIN`, `DENY`, or another governed finite outcome rather than a plausible answer.

## Proposed proof slice

The sibling plan proposes a **southwest-Kansas cross-border multisystem trust proof**. In bounded form, that slice would demonstrate that KFM can:

- explain Liberal's regional and cross-border transportation role without turning a planning study or public meeting into a final design, construction status, closure, traffic, or safe-routing claim;
- present the public role of Liberal Mid-America Regional Airport without caching schedules, exposing security-sensitive operational detail, or claiming live flight status;
- distinguish a municipal Consumer Confidence Report from household potability, service-line, illness, exposure, private-well, or individualized health advice;
- explain wastewater and Arkalon wetland/recreation context without assigning pollution sources, inferring regulatory compliance, or converting dated park rules into current individualized health or access guidance;
- preserve Census and agricultural statistics as dated aggregates while preventing immigration, citizenship, language, household, employment, landowner, operator, parcel, or individual-farm inference;
- preserve statistical suppression rather than reconstructing withheld agricultural values;
- keep public GIS layers bounded by their informational, non-legal, and non-engineering limitations;
- present Hugoton-area energy history without exposing or inferring current wells, pipelines, owners, production, emissions, facilities, vulnerabilities, or compliance;
- demonstrate visible `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` states through deterministic, no-network fixtures before live-source or public-release work.

These remain **PROPOSED** behaviors until contracts, schemas, fixtures, validators, policy, evidence, review, runtime integration, and release state are verified.

## Public-safe rules

| Rule | Required behavior |
|---|---|
| Evidence before interpretation | Consequential claims resolve through governed evidence; generated language, tourism copy, search snippets, map styling, and model confidence never substitute for support. |
| Cite or abstain | Missing, stale, conflicted, out-of-scope, or role-inappropriate evidence must narrow the answer or return a finite negative state. |
| Transportation currentness is explicit | A study, open house, project notice, or dated map must not become final design, construction, closure, traffic, or routing truth. |
| Airport detail is minimized | Public context may explain the airport's regional role; schedules, operations, security, facilities, personnel, and live flight status require current official authority and appropriate withholding. |
| Water reports are system- and period-bounded | A Consumer Confidence Report does not answer household, service-line, illness, exposure, private-well, or current potability questions outside its scope. |
| Wastewater and recreation roles stay distinct | Wastewater operations, wetland management, park rules, and recreation context must not become pollution attribution, compliance judgment, or individualized health advice. |
| Demographics remain aggregate | Census statistics must not be used to infer a person's immigration, citizenship, legal status, language ability, employment, household, or identity. |
| Agricultural confidentiality is preserved | Suppressed NASS values remain suppressed; no farm, operator, worker, parcel, or individual-business profile is reconstructed. |
| GIS visibility is not authority | Public GIS does not establish title, boundary, zoning, engineering, insurance, flood, utility, emergency, or redistribution truth. |
| Energy history is not current operations | Historical KGS material must not become current well, pipeline, ownership, production, emissions, facility, vulnerability, or compliance information. |
| Sensitive wildlife locations fail closed | Exact or inference-enabling occurrences, roosts, nests, or habitat-use details are withheld or generalized. |
| Public clients stay downstream of trust | UI, map, search, exports, and AI consume governed and released evidence rather than RAW, WORK, QUARANTINE, internal systems, utility/airport operational systems, or direct model output. |
| Correction and rollback remain visible | Future source, geometry, currentness, privacy, sensitivity, interpretation, or operational corrections must be able to supersede or withdraw affected products without rewriting history. |

## Proposed layer and card families

The build plan describes the following planning families. Their presence here records proposed scope only; it does not prove implementation, source admission, review, or release.

| Layer or card family | Intended role | Public-safe condition |
|---|---|---|
| Seward County and Liberal orientation | General county/civic frame | Authoritative geometry, version, rights, and release state verified |
| Kansas–Oklahoma border context | Regional orientation | No immigration, law-enforcement, personal-movement, or legal-status inference |
| U.S. 54/83 planning context | Transportation-study and corridor explanation | Study/current operations separated; no live route or closure advice |
| Airport public-role card | Regional aviation context | No cached schedule, live status, security, personnel, or facility-operation detail |
| Municipal water role card | Public-system and aquifer context | Report period and system scope visible; no household or private-well answer |
| Wastewater and Arkalon context | Wastewater, wetland, and recreation-role explanation | No pollution attribution, compliance judgment, or individualized health advice |
| Agriculture aggregate layer | County-scale irrigated-agriculture context | Suppression preserved; no farm, operator, worker, or parcel inference |
| Demographic aggregate card | Dated county population and demographic context | No person-level immigration, citizenship, employment, language, or household inference |
| GIS limitation notice | Explain informational map boundaries | No legal, engineering, title, insurance, or emergency authority |
| Hugoton-area energy-history card | Historical geology and energy context | No current facilities, wells, pipelines, ownership, production, emissions, or vulnerability |
| Official-current redirect panel | Route users to current county, city, airport, KDOT, NWS, utility, or health authority | Redirect metadata must not masquerade as a KFM answer |
| Operational-boundary notice | Explain withheld or deferred live detail | No confirmation of hidden configurations or vulnerabilities |

## Finite outcomes

For this county lane, the expected public-facing outcome vocabulary is:

- `ANSWER` — released evidence is in scope, citation-valid, time-fit, rights-cleared, privacy-safe, sensitivity-safe, policy-safe, and review-complete;
- `ABSTAIN` — evidence, currentness, source role, report period, spatial fitness, rights, claim scope, or release closure is insufficient;
- `DENY` — the request seeks operational airport, utility, industrial, infrastructure, household-health, immigration-status, employment, property, farm, private-well, sensitive-wildlife, or other protected inference;
- `ERROR` — a resolver, validator, policy engine, source adapter, identity crosswalk, or runtime dependency failed.

These outcomes are a **proposed design contract**, not proof that the current repository implements them for Seward County.

Representative proposed reason codes from the plan's boundary include:

- `CURRENT_TRANSPORT_OR_CLOSURE_REQUIRES_OFFICIAL_AUTHORITY`
- `LIVE_AIRPORT_OPERATION_NOT_PROVIDED`
- `WATER_REPORT_NOT_HOUSEHOLD_HEALTH_ADVICE`
- `WASTEWATER_CONTEXT_NOT_POLLUTION_ATTRIBUTION`
- `DEMOGRAPHIC_INDIVIDUAL_INFERENCE_DENIED`
- `SUPPRESSED_AGRICULTURAL_VALUE_NOT_RECONSTRUCTED`
- `GIS_LAYER_NOT_LEGAL_OR_ENGINEERING_AUTHORITY`
- `INDUSTRIAL_OR_INFRASTRUCTURE_DETAIL_WITHHELD`
- `SENSITIVE_WILDLIFE_DETAIL_WITHHELD`
- `OFFICIAL_CURRENT_SAFETY_CHANNEL_REQUIRED`

Reason-code naming and runtime registration remain **NEEDS VERIFICATION**.

## Source-role posture

The build plan lists candidate source families. A candidate source is neither admitted evidence nor public-release authority.

| Source family | Intended role | Must not be treated as |
|---|---|---|
| Seward County official materials | County administration, services, meetings, records, and current official routing | Living-person profile, property/title truth, current emergency answer, or universal authority over city systems |
| City of Liberal materials | Municipal services, civic context, airport, water, wastewater, parks, GIS, and project notices | Automatic current operational, health, engineering, legal, or release truth |
| KDOT or transportation-planning sources | Project-study, corridor, and public-process context | Final design, current construction, closure, traffic, or safe-routing authority outside current official status |
| Liberal Mid-America Regional Airport | Public aviation role and current official redirect | Cached flight status, security, operational, personnel, or facility-vulnerability information |
| Municipal water sources | Public-system and reporting-period context | Household potability, private-well, illness, exposure, service-line, or individualized health determination |
| Wastewater and Arkalon sources | Facility mission, wetland, park, and recreation-rule context | Pollution-source attribution, compliance ruling, or individualized health advice |
| U.S. Census Bureau | Dated aggregate demographic statistics | Person-level immigration, citizenship, language, employment, legal-status, or household evidence |
| USDA NASS | Dated county agricultural aggregates and suppression | Farm, operator, worker, parcel, livestock-location, or reconstructed confidential values |
| Kansas Geological Survey | Historical and scientific Hugoton-area context | Current wells, pipelines, operators, production, emissions, ownership, facilities, or compliance |
| National Weather Service | Official-current weather and hazard authority | KFM-authored warning, emergency command, or durable cached safety verdict |
| Future KDHE or environmental sources | Public-health and environmental context after admission | Automatic household health, pollution causation, or regulatory-compliance conclusion |

## Repository and placement posture

**CONFIRMED:** this README already exists at `docs/focus-mode/counties/seward_county/README.md`, so this change keeps the tracked path and responsibility root rather than inventing a new documentation home.

**CONFIRMED:** [ADR-0029](../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) is accepted and adopts the exact Directory Rules v2 bytes at `docs/doctrine/directory-rules.md` as the single writable human Directory Rules authority.

**CONFIRMED:** [ADR-0027](../../../adr/ADR-0027-county-focus-mode-control-plane.md) remains `proposed` and records the unresolved conflict between the current singular `docs/focus-mode/` lane and a proposed plural county control plane. This README does not use that unaccepted decision to migrate Seward County, create a parallel lane, or treat the build plan's proposed tree as current fact.

## Relationship to the build plan

The detailed planning artifact is:

- [Seward County Focus Mode Build Plan](./seward_county_focus_mode_build_plan.md)

Use the build plan for proposed layers, cards, source seeds, risk analysis, phases, fixtures, UI ideas, and open verification questions. Use this README for the stable county-boundary summary and current truth posture.

> [!CAUTION]
> The build plan contains point-in-time facts, aggregate values, current-seeming operational references, proposed paths, and source-derived statements from its June 2026 authoring run. Before implementation or public use, reverify current facts, source terms, identifiers, rights, report periods, suppression rules, privacy and sensitivity posture, operational status, reviewer assignments, and release fitness against authoritative sources and current repository controls.

## Validation expectations for future implementation

A future Seward County implementation should not be considered complete merely because Markdown or a map exists. At minimum, the changed area should eventually prove:

1. study, design, construction, closure, and live-routing states remain distinct for transportation claims;
2. airport public context cannot expose cached schedules, live operations, security-sensitive detail, personnel, or facility vulnerability;
3. water-system reports preserve system identity, reporting period, limitations, and non-household scope;
4. wastewater, wetland, and recreation evidence cannot become pollution attribution, compliance judgment, or individualized health advice;
5. demographic aggregates cannot support person-level immigration, citizenship, employment, language, household, or legal-status inference;
6. agricultural suppression is preserved and cannot be reconstructed through joined sources;
7. public GIS limitations remain visible and prevent legal, engineering, title, insurance, flood, utility, or emergency overclaim;
8. historical energy context cannot become current industrial or infrastructure intelligence;
9. positive and negative fixtures cover `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`;
10. no-network deterministic tests cover the transportation, airport, water, wastewater, privacy, agriculture, and industrial boundaries;
11. every consequential public claim resolves from EvidenceRef to EvidenceBundle;
12. governed API/UI surfaces display evidence, policy, limitations, checked time, expiry, stale, restricted, denied, and error states;
13. no direct path exists from raw/internal stores, utility or airport systems, candidate observations, or model output to public truth;
14. correction, supersession, withdrawal, and rollback propagate through map, timeline, search, cache, export, and AI surfaces;
15. release evidence is appropriate to the significance of transportation, utility, health, demographic, industrial, and infrastructure claims.

## Known unknowns

The following remain **UNKNOWN** or **NEEDS VERIFICATION** until current implementation evidence proves otherwise:

- which Seward County source descriptors are admitted;
- current rights and derivative-display permissions for county, city, airport, utility, GIS, Census, NASS, KGS, transportation, and environmental sources;
- authoritative geometry and safe-scale thresholds for airport, utility, industrial, wildlife, and infrastructure context;
- current U.S. 54/83 project state, airport schedules and operations, park rules, water reports, wastewater operations, road status, alerts, closures, burn bans, and emergency conditions;
- exact contracts, schemas, policies, validators, fixtures, and tests applicable to Seward County;
- governed API routes, Explorer UI components, and Evidence Drawer integration;
- named transportation, aviation, water, public-health, industrial, privacy, ecology, rights, security, and release reviewers;
- correction propagation through map, timeline, search, cache, export, and AI surfaces;
- any deployed or published Seward County Focus Mode.

## Rollback and correction

This README is documentation-only. Before merge, rollback is abandonment of the feature branch or pull request. After merge, correction should use a transparent revert or forward-fix PR against the actual merged commit.

A documentation rollback does **not** reverse any separate future source admission, policy decision, release manifest, deployment, publication, or public correction. Those transitions require their own governed records and rollback paths.

---

**Related:** [Seward County Focus Mode Build Plan](./seward_county_focus_mode_build_plan.md) · [County index](../COUNTY_INDEX.md) · [Counties Focus Mode overview](../README.md)

[Back to top](#top)
