<!-- KFM_META_BLOCK_V2

document_id: kfm://docs/focus-mode/counties/rooks-county

title: Rooks County Focus Mode

type: county-focus-mode-readme

status: draft

truth_posture: cite-or-abstain

repository_path: docs/focus-mode/counties/rooks_county/README.md

related:
  - ./rooks_county_focus_mode_build_plan.md
  - ../../../adr/ADR-0027-county-focus-mode-control-plane.md
  - ../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md

notes:
  - Same-path modernization of an existing tracked README.
  - This document summarizes the repository-grounded county boundary; it does not claim source admission, implementation, release, deployment, or publication.
-->

<a id="top"></a>

# Rooks County Focus Mode

> **Purpose.** Define the public-safe documentation boundary for Rooks County, Kansas, and point maintainers to the county build plan without presenting proposed source, runtime, safety, legal, or release behavior as current implementation.

> [!IMPORTANT]
> This README is a **documentation boundary**, not a live county product or current-conditions service. The sibling build plan contains proposed architecture and source-derived planning material checked in June 2026. Its statements remain subordinate to current repository evidence, authoritative-current sources, admitted evidence, policy, review, and release state.

## Status at a glance

| Area | Status | Boundary |
|---|---|---|
| County scope | `CONFIRMED` | This tracked lane concerns Rooks County, Kansas. |
| Existing README role | `CONFIRMED` | This file is the county README at the current repository path. |
| Sibling build plan | `CONFIRMED` | `rooks_county_focus_mode_build_plan.md` exists beside this README. |
| County proof slice | `PROPOSED` | The plan centers Webster Reservoir and State Park, South Fork Solomon River, wildlife sensitivity, burn-ban currentness, lake-measurement semantics, and water/infrastructure non-determination. |
| Source admission | `UNKNOWN` | A source is not admitted merely because the plan cites, links, or discusses it. |
| Runtime/API/UI behavior | `UNKNOWN` | This README does not claim implemented county routes, contracts, schemas, MapLibre layers, Evidence Drawer behavior, or Focus Mode execution. |
| Current conditions | `UNKNOWN` | Burn restrictions, park availability, lake conditions, wildlife status, roads, and emergencies require current official authority. |
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

The Rooks County build plan proposes a map-first experience organized around **Webster Reservoir, Webster State Park, the South Fork Solomon River, Webster Wildlife Area, county services, dated burn-ban notices, weather-authority routing, and generalized water and recreation context**.

Its central trust problem is currentness. Public pages can contain burn resolutions, park hours, camping or facility information, lake elevation, inflow, outflow, fire restrictions, and recreation rules that appear immediately usable but may become stale, superseded, or unsafe when separated from their original authority and time basis.

The most important public-safe rule is:

> **Stable context is not live legal, access, safety, operational, or emergency guidance.**

A map, evidence object, search result, export, or AI answer must not convert dated source material into a present-tense burn-ban decision, campsite-availability claim, lake-safety interpretation, hunting or fishing permission, road recommendation, water-right conclusion, reservoir-operation statement, property-access determination, or emergency instruction. Missing currentness, authority, evidence, or release closure should produce `ABSTAIN`, `DENY`, or another governed finite outcome rather than a plausible answer.

## Proposed proof slice

The sibling plan proposes a **Webster Reservoir, Burn-Ban Currentness, and Water/Infrastructure Boundary Proof**. In bounded form, that slice would demonstrate that KFM can:

- present generalized, source-attributed reservoir, river, park, county-service, and wildlife context without becoming a live conditions system;
- explain why dated county burn-ban resolutions require current official verification before legal or field reliance;
- keep lake elevation, inflow, outflow, and other measurements separate from boating, launching, swimming, travel, drought, or operational-safety conclusions;
- preserve wildlife geoprivacy by generalizing habitat context and withholding exact or inference-enabling concentrations, nests, roosts, or targetable locations;
- distinguish reservoir context from irrigation, allocation, permit, priority, water-right, dam-operation, or infrastructure-vulnerability authority;
- route current hazard and emergency questions to the appropriate official authority rather than synthesizing a KFM warning;
- expose visible negative states when temporal fitness, rights, sensitivity, source role, review, or release closure is missing;
- prove the highest-risk boundaries through deterministic, no-network positive and negative fixtures before any live-source or public-release work.

These remain **PROPOSED** behaviors until contracts, schemas, fixtures, validators, policy, evidence, review, runtime integration, and release state are verified.

## Public-safe rules

| Rule | Required behavior |
|---|---|
| Evidence before interpretation | Consequential claims resolve through governed evidence; generated language, map styling, and model confidence never substitute for support. |
| Cite or abstain | Missing, stale, expired, conflicted, or out-of-scope evidence narrows the answer or returns a finite negative state. |
| Burn restrictions are time-bound | A resolution, notice, or archived page must not be presented as currently applicable without authoritative-current verification. |
| Park and facility status are time-bound | Hours, camping, reservations, closures, fire rules, generators, ramps, and facilities must not be copied into durable current guidance. |
| Measurements are not safety decisions | Lake level, inflow, outflow, and other observations must retain their time and measurement scope and must not become safety or operations advice. |
| Wildlife sensitivity is explicit | Exact migratory-waterfowl, nesting, roosting, refuge-use, or concentration detail is withheld or generalized. |
| Water governance remains distinct | Reservoir context does not establish water rights, allocations, permits, priorities, irrigation status, or legal entitlement. |
| Infrastructure detail is minimized | Dam, outlet, monitoring, control, security, operating, and vulnerability detail is excluded or denied unless a governed need and release basis exist. |
| Property access is not inferred | Public shoreline or park context does not establish ownership, title, easement, entry permission, or private access. |
| Weather and emergencies remain official-authority matters | KFM may identify the proper current authority but must not rewrite or replace official warnings and emergency instructions. |
| Public clients stay downstream of trust | UI, map, search, exports, and AI consume governed and released evidence rather than `RAW`, `WORK`, `QUARANTINE`, internal stores, or direct model output. |
| Correction and rollback remain visible | Future source, time, geometry, sensitivity, legal, safety, or interpretation corrections must be able to supersede or withdraw affected products without rewriting history. |

## Proposed layer and card families

The build plan names the following candidate surfaces. Their presence here records planning scope only; it does not prove implementation, source admission, or release.

| Layer or card family | Intended role | Public-safe condition |
|---|---|---|
| Rooks County / Stockton orientation | County-scale civic frame | Generalized, authoritative geometry and released civic context only |
| Webster Reservoir and South Fork Solomon context | Stable water-system orientation | No current safety, operations, allocation, or legal meaning |
| Webster State Park context | Stable public recreation description | No current availability, facility, access, fire, hunting, fishing, or safety claim |
| Burn Restriction Currentness Card | Explain legal/currentness churn | Dated source and expiry visible; no cached present-tense conclusion |
| Lake-Level Non-Safety Card | Explain measurement-versus-safety distinction | Observation time and scope visible; no launch, boating, swimming, or travel recommendation |
| Wildlife Area Generalization Card | Broad habitat and stewardship context | Safe-scale geometry and no targetable wildlife detail |
| Water-Right / Allocation Non-Determination Card | Prevent administrative and legal inference | Official authority and limitation visible; KFM does not adjudicate |
| Critical Infrastructure Withhold Notice | Explain intentional omission | No confirmation of hidden configuration, controls, vulnerabilities, or operations |
| Official Hazard Redirect Card | Route users to current hazard authority | Redirect is not represented as a KFM warning or independent answer |
| Live burn, park, lake, road, or emergency layer | Dynamic high-risk content | `DEFER` until governed feeds, expiry, review, correction, and release controls exist |

## Finite outcomes

For this county lane, the expected public-facing outcome vocabulary is:

- `ANSWER` — released evidence supports a stable, bounded, citation-valid, time-fit, rights-cleared, sensitivity-safe, policy-safe response;
- `ABSTAIN` — currentness, authority, temporal scope, rights, evidence, legal scope, measurement meaning, or release closure is insufficient;
- `DENY` — the request would expose sensitive wildlife, critical infrastructure, private-property access, protected operational detail, or another prohibited boundary;
- `ERROR` — a resolver, validator, policy engine, source adapter, or runtime dependency failed.

Representative proposed reason codes include:

- `CURRENT_BURN_RESTRICTION_REQUIRES_COUNTY_AUTHORITY`
- `CURRENT_PARK_STATUS_REQUIRES_KDWP`
- `LAKE_LEVEL_NOT_SAFETY_GUIDANCE`
- `SENSITIVE_WILDLIFE_DETAIL_WITHHELD`
- `WATER_RIGHT_OR_ALLOCATION_REQUIRES_AUTHORITY`
- `CRITICAL_WATER_INFRASTRUCTURE_DETAIL_WITHHELD`
- `PROPERTY_OR_ACCESS_DETERMINATION_DENIED`
- `OFFICIAL_CURRENT_SAFETY_CHANNEL_REQUIRED`

These outcomes and reason codes are **proposed design vocabulary**, not proof that the repository currently implements them for Rooks County.

## Source-role posture

The build plan discusses several source families, each with a different role. Candidate or public sources do not become admitted evidence or release authority automatically.

| Source family | Intended role | Must not be treated as |
|---|---|---|
| Rooks County | Dated county notices, civic services, local emergency-management routing, and county context | Evergreen burn-ban status, property/title truth, or independent proof of current road and emergency conditions |
| Kansas Department of Wildlife and Parks — park role | Webster State Park description and official-current park/recreation information | Permanent campsite availability, safety determination, or authority outside its scope |
| Kansas Department of Wildlife and Parks — wildlife role | Habitat and wildlife-area management context | Wildlife-targeting map, exact occurrence authority, or hunting-success prediction |
| Bureau of Reclamation candidate | Reservoir project and operational authority after endpoint and source admission are verified | Public vulnerability map, personal safety advice, or permission to disclose sensitive operating detail |
| Kansas water-administration sources | Water-right, allocation, permit, priority, or administrative authority where current and admissible | KFM legal adjudication or inferred entitlement |
| National Weather Service Goodland | Official-current warning, fire-weather, drought, river, lake, and hazard authority | KFM-authored warning or emergency command |
| Generated or AI narrative | Bounded interpretation of released evidence | Evidence, policy, legal, safety, operations, or release authority |

## Repository and placement posture

**CONFIRMED:** this README already exists at `docs/focus-mode/counties/rooks_county/README.md`, so this change keeps the tracked path and `docs/` responsibility root rather than inventing a new documentation home.

**CONFIRMED:** [ADR-0029](../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) is accepted and adopts the exact Directory Rules v2 bytes at `docs/doctrine/directory-rules.md` as the single writable human Directory Rules authority.

**CONFIRMED:** [ADR-0027](../../../adr/ADR-0027-county-focus-mode-control-plane.md) remains `proposed` and records the unresolved singular `docs/focus-mode/` versus plural `docs/focus-modes/` control-plane conflict. This README does not use that unaccepted decision to migrate Rooks County, create a parallel lane, or establish a new authority surface.

## Relationship to the build plan

The detailed planning artifact is:

- [Rooks County Focus Mode Build Plan](./rooks_county_focus_mode_build_plan.md)

Use the build plan for proposed layers, cards, reason codes, fixtures, source seeds, risk analysis, phases, and verification questions. Use this README for the stable county-boundary summary and current truth posture.

> [!CAUTION]
> The build plan includes point-in-time source observations from June 8, 2026. Before implementation or public use, reverify current burn restrictions, park and recreation information, lake-data semantics, source endpoints, water-administration authority, source terms, rights, sensitivity, safe geometry, reviewer assignments, and release fitness. The plan itself records that one attempted Bureau of Reclamation project URL resolved to unrelated material and therefore requires correction before use.

## Validation expectations for future implementation

A future Rooks County implementation should not be considered complete merely because Markdown or a map exists. At minimum, the changed area should eventually prove:

1. checked, effective, and expiry times for every burn, park, lake, road, warning, or other current-status object;
2. negative fixtures preventing stale or superseded burn resolutions from appearing current;
3. negative fixtures preventing park pages from becoming live campsite, facility, access, fire, hunting, or fishing permission;
4. measurement semantics that prevent lake level, inflow, or outflow from becoming safety, drought, failure, or operational conclusions;
5. safe-scale handling and negative fixtures for exact or inference-enabling wildlife detail;
6. negative fixtures for water-right, allocation, permit, priority, and irrigation-entitlement inference;
7. negative fixtures for dam, outlet, monitoring, control, security, and infrastructure-vulnerability detail;
8. positive and negative fixtures for `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` behavior;
9. no-network deterministic tests for currentness, measurement, ecology, water-governance, access, and infrastructure boundaries;
10. EvidenceRef-to-EvidenceBundle closure for every consequential public claim;
11. governed API/UI behavior with visible evidence, time, expiry, role, limitation, restricted, denied, stale, and error states;
12. no direct path from raw/internal stores, direct park or operational systems, candidate observations, or model output to public truth;
13. correction, supersession, withdrawal, cache invalidation, and rollback behavior across map, search, export, and AI surfaces;
14. release evidence appropriate to any legal, safety, ecology, water, recreation, property, infrastructure, or emergency implication.

## Known unknowns

The following remain **UNKNOWN** or **NEEDS VERIFICATION** until current implementation evidence proves otherwise:

- which Rooks County source descriptors are admitted;
- the corrected authoritative Bureau of Reclamation Webster project endpoint and its permitted use;
- current source rights and derivative-display permissions;
- current county burn-ban applicability;
- current park hours, closures, camping, facility, fire, hunting, and fishing status;
- current lake level, inflow, outflow, water quality, and the lawful meaning of those values;
- safe public geometry and generalization thresholds for wildlife and infrastructure;
- current water-right, allocation, permit, and reservoir-operation authorities;
- exact contracts, schemas, policies, validators, fixtures, and tests applicable to Rooks County;
- governed API routes, Explorer UI components, and Evidence Drawer integration;
- named county, park, ecology, water-governance, infrastructure-security, rights, and release reviewers;
- correction propagation through map, search, cache, export, and AI surfaces;
- any deployed or published Rooks County Focus Mode.

## Rollback and correction

This README is documentation-only. Before merge, rollback is abandonment of the feature branch or pull request. After merge, correction should use a transparent revert or forward-fix PR against the actual merged commit.

A documentation rollback does **not** reverse any separate future source admission, policy decision, release manifest, deployment, publication, legal/currentness correction, or public withdrawal. Those transitions require their own governed records and rollback paths.

---

**Related:** [Rooks County Focus Mode Build Plan](./rooks_county_focus_mode_build_plan.md) · [County index](../COUNTY_INDEX.md) · [Counties Focus Mode overview](../README.md)

[Back to top](#top)
