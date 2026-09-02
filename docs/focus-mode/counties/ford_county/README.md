<!-- KFM_META_BLOCK_V2

document_id: kfm://docs/focus-mode/counties/ford-county

title: Ford County Focus Mode

type: county-focus-mode-readme

status: draft

truth_posture: cite-or-abstain

repository_path: docs/focus-mode/counties/ford_county/README.md

related:
  - ./ford_county_focus_mode_build_plan.md
  - ../../../adr/ADR-0027-county-focus-mode-control-plane.md
  - ../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md

notes:
  - Same-path modernization of an existing tracked README.
  - This document summarizes the repository-grounded county boundary; it does not claim source admission, implementation, release, deployment, or publication.
-->

<a id="top"></a>
<a id="ford-county--focus-mode-build-plan"></a>

# Ford County Focus Mode

> **Purpose.** Define the public-safe documentation boundary for Ford County, Kansas, and point maintainers to the county build plan without presenting proposed historical, hydrologic, agricultural, runtime, or release behavior as current implementation.

> [!IMPORTANT]
> This README is a **documentation boundary**, not a live county product, romanticized Old West map, water-quality advisory, property service, or unrestricted cultural-site index. The sibling build plan is a draft design artifact authored on a different repository-evidence boundary. Current repository reads confirm the tracked files and governance surfaces named here, but they do not upgrade the plan's external facts, source rights, object designs, runtime behavior, or release claims into implementation evidence.

## Status at a glance

| Area | Status | Boundary |
|---|---|---|
| County scope | `CONFIRMED` | This tracked lane concerns Ford County, Kansas. |
| Existing README role | `CONFIRMED` | This file is the county README at the current repository path. |
| Sibling build plan | `CONFIRMED` | `ford_county_focus_mode_build_plan.md` exists beside this README. |
| Plan repository disclaimer | `STALE / NARROWED` | The plan's no-mounted-repository statement does not describe this implementation session; its proposed paths and behavior still require current verification. |
| County proof slice | `PROPOSED` | The plan combines Dodge City, Fort Dodge, Santa Fe Trail movement, railroad and cattle-shipping history, Arkansas River context, agriculture, water-quality interpretation, and public-history correction. |
| Source admission | `UNKNOWN` | A source is not admitted merely because the plan cites, links, or discusses it. |
| Runtime/API/UI behavior | `UNKNOWN` | This README does not claim implemented Ford County routes, contracts, schemas, MapLibre layers, Evidence Drawer behavior, or Focus Mode execution. |
| Current water, access, and operational state | `UNKNOWN` | Water conditions, regulatory status, access, roads, emergencies, and current operations require authoritative-current evidence. |
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
- [Related](#related)

## County boundary

The Ford County build plan proposes a map-first experience organized around **Dodge City, Fort Dodge, Santa Fe Trail and wagon-movement context, railroad arrival and cattle shipping, the Arkansas River corridor, water-quality and groundwater interpretation, county-scale agriculture and land cover, public-history sites, and time-aware atlas claims**.

Its central trust problem is not simply displaying famous western-Kansas history. It is preserving the differences among:

- source-backed historical claims, folklore, legend, reenactment, tourism narrative, and generated explanation;
- official public records, local-history interpretation, and promotional public-history material;
- public Fort Dodge and military-trail context and operational or sensitive site detail;
- public historic places and exact archaeological, burial, cemetery, sacred, or culturally restricted locations;
- historical route corridors and false cartographic precision;
- river observations, regulatory water-quality records, groundwater interpretation, and current safety or legal conclusions;
- agricultural aggregates or derived land-cover indicators and private farms, households, wells, parcels, owners, or water rights;
- a map feature, an AtlasCard, an EvidenceBundle, and a released public claim.

The most important public-safe rule is:

> **Famous history is not self-authenticating truth, and a compelling map must not turn mythology, uncertain routes, sensitive places, or environmental context into unsupported certainty.**

Missing evidence, source role, rights, temporal fitness, safe geometry, cultural or sensitivity review, or release closure should narrow the claim or produce `ABSTAIN`, `DENY`, or another governed finite outcome rather than a confident story.

## Proposed proof slice

The sibling plan treats Ford County as a western-Kansas frontier-and-water stress test for the county Focus Mode architecture. In bounded form, the slice would demonstrate that KFM can:

- present Dodge City and Fort Dodge public historical context without converting tourism narrative or familiar legend into verified fact;
- distinguish official, local-history, marker, archival, and tourism source roles in the Evidence Drawer;
- show Santa Fe Trail, wagon, railroad, and cattle-shipping corridors with explicit uncertainty, temporal scope, and limitations rather than false precision;
- explain the Arkansas River corridor while keeping river observation, groundwater science, regulatory water-quality material, and generated interpretation distinct;
- present agriculture and land-cover context with method, reporting period, scale, and derived-status labels while withholding private-operation and property inference;
- protect Indigenous, archaeological, burial, cemetery, sacred, and culturally restricted places through review, withholding, or generalization;
- make correction and supersession visible when a public-history interpretation, route alignment, source status, geometry, or environmental claim changes;
- demonstrate visible `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` states through deterministic, no-network fixtures before live-source or public-release work.

These remain **PROPOSED** behaviors until contracts, schemas, fixtures, validators, policy, evidence, review, runtime integration, and release state are verified.

## Public-safe rules

| Rule | Required behavior |
|---|---|
| Evidence before interpretation | Consequential claims resolve through governed evidence; generated language, map styling, familiarity, and tourism repetition never substitute for support. |
| Cite or abstain | Missing, stale, conflicted, role-inappropriate, or out-of-scope evidence must narrow the response or return a finite negative state. |
| Interpretation status is explicit | Public surfaces distinguish factual claim, interpretation, folklore, tourism narrative, reenactment, and derived indicator. |
| Source roles do not collapse | County, local-history, tourism, archival, marker, scientific, regulatory, hydrologic, agricultural, and generated sources retain distinct authority and limitations. |
| Historical routes show uncertainty | Santa Fe Trail, military-road, wagon, railroad, and cattle-shipping alignments expose source lineage, date, confidence, scale, and limitations. |
| Cultural and archaeological material fails closed | Exact sacred, burial, cemetery, archaeological, or culturally restricted places are withheld; public interpretation requires appropriate source and review authority. |
| Military and infrastructure detail is minimized | Fort Dodge and related context remains historical and public-safe; operational, security, infrastructure, personnel, and vulnerability detail is excluded or denied. |
| Water roles remain distinct | River geometry, observation, groundwater science, regulatory water-quality records, and current health, safety, allocation, or legal authority must not collapse into one layer. |
| Agriculture remains aggregate and method-visible | County or derived context must not identify farms, households, owners, parcels, private wells, operations, or water-right status. |
| Property and legal conclusions are out of scope | A public map does not establish title, access, boundary, permit, allocation, water right, liability, or compliance. |
| Current conditions require current authority | Water conditions, road status, access, emergencies, and active operations require checked time, expiry, supersession, and authoritative-current routing. |
| Public clients stay downstream of trust | UI, map, search, exports, and AI consume governed and released evidence rather than RAW, WORK, QUARANTINE, internal stores, candidate data, or direct model output. |
| Correction and rollback remain visible | Future source, interpretation, route, geometry, sensitivity, environmental, or release corrections supersede or withdraw affected products without rewriting history. |

## Proposed layer and card families

The build plan names the following planning families. Their presence here records proposed scope only; it does not prove implementation, source admission, review, or release.

| Layer or card family | Intended role | Public-safe condition |
|---|---|---|
| Ford County boundary | County-scale spatial frame | Authoritative geometry, version, rights, and release state verified |
| Dodge City public-history context | Civic, cattle-town, and tourism orientation | Interpretation status and source role visible; no folklore presented as fact |
| Fort Dodge context | Public military and trail history | Historical public scope only; sensitive or operational detail denied |
| Santa Fe Trail and wagon corridor | Movement and route-history interpretation | Uncertainty, time, source lineage, and non-routing posture visible |
| Railroad and cattle-shipping context | Transportation and economic-history interpretation | Evidence required; mythology and reenactment separated from claims |
| Arkansas River corridor | Hydrologic and landscape context | No current safety, water-right, allocation, or property conclusion |
| Water-quality context | Scientific and regulatory water interpretation | KGS, KDHE, USGS, or other roles explicit; status and time basis visible |
| Agriculture and land-cover baseline | County-scale crop, range, irrigation, or land-use context | Method, date, scale, uncertainty, and derived status visible; no private-operation inference |
| Public-history sites | Boot Hill, museums, markers, and downtown interpretation | Public access and interpretation do not authorize sensitive-site exposure or factual overclaim |
| Timeline events | Time navigation across reviewed claims | Planning buckets do not become facts without evidence closure |
| Atlas claims | Clickable claim-bearing map objects | Every consequential claim carries EvidenceRef, limitation, review, and release state |

## Finite outcomes

For this county lane, the expected public-facing outcome vocabulary is:

- `ANSWER` — released evidence is in scope, citation-valid, time-fit, rights-cleared, sensitivity-safe, policy-safe, and review-complete;
- `ABSTAIN` — evidence, interpretation status, source role, route confidence, temporal scope, rights, geometry, or release closure is insufficient;
- `DENY` — the request would expose protected cultural or archaeological locations, private people or property, restricted infrastructure, unsafe precision, or another protected boundary;
- `ERROR` — a resolver, validator, policy engine, source adapter, identity crosswalk, citation check, or runtime dependency failed.

These outcomes are a **proposed design contract**, not proof that the current repository implements them for Ford County. Exact reason-code names and registry ownership remain **NEEDS VERIFICATION**.

## Source-role posture

The build plan lists candidate source families. A candidate source is neither admitted evidence nor public-release authority.

| Source family | Intended role | Must not be treated as |
|---|---|---|
| Ford County official materials | County identity, civic context, and local public-history routing | Complete proof of complex history, property truth, or current emergency authority |
| Ford County Historical Society and local-history materials | Local archives, interpretation, and source discovery | Automatic publication authority, living-person evidence, or uncertainty-free historical truth |
| Dodge City official tourism/history materials | Public-history and visitor context | Primary proof for every factual claim or permission to collapse legend into history |
| Kansas State University Research and Extension | County and agriculture context | Private-farm, household, parcel, water-right, or current operational evidence |
| Kansas Geological Survey | Groundwater, geology, salinity, and historical scientific interpretation | Current health, regulatory, water-right, property, or legal authority |
| Kansas Department of Health and Environment | Regulatory water-quality context where current and admitted | Household health, current recreation safety, pollution causation, or automatic liability judgment |
| U.S. Geological Survey | Hydrography and observation-source context | Current legal, regulatory, health, property, or allocation authority |
| USDA/NASS and land-cover sources | Dated county aggregates or derived crop/land-cover context | Farm, operator, household, parcel, or reconstructed confidential values |
| Kansas Historical Society and Library of Congress | Markers, archival maps, and historic source routing | Complete cultural authority, current access truth, or precise sensitive-site permission |
| Genealogy and digitized local-history collections | Historical source discovery under strict scope | Living-person profiles, unreviewed genealogy, or current family/property conclusions |

## Repository and placement posture

**CONFIRMED:** this README already exists at `docs/focus-mode/counties/ford_county/README.md`, so this change keeps the tracked path and responsibility root rather than inventing a new documentation home.

**CONFIRMED:** [ADR-0029](../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) is accepted and adopts the exact Directory Rules v2 bytes at `docs/doctrine/directory-rules.md` as the single writable human Directory Rules authority.

**CONFIRMED:** [ADR-0027](../../../adr/ADR-0027-county-focus-mode-control-plane.md) remains `proposed` and records the unresolved conflict between the current singular `docs/focus-mode/` lane and a proposed plural county control plane. This README does not use that unaccepted decision to migrate Ford County, create a parallel lane, or treat the build plan's proposed repository tree as current fact.

## Relationship to the build plan

The detailed planning artifact is:

- [Ford County Focus Mode Build Plan](./ford_county_focus_mode_build_plan.md)

Use the build plan for proposed layers, object examples, source seeds, risk analysis, phases, fixtures, mock API/UI ideas, and open verification questions. Use this README for the stable county-boundary summary and current truth posture.

> [!CAUTION]
> The build plan was prepared as a draft on a different evidence boundary and contains proposed paths, source-derived facts, time buckets, endpoints, schemas, validators, source uses, and implementation phases. Before implementation or public use, reconcile each material item against current repository evidence, accepted ADRs, authoritative sources, source terms, cultural and sensitivity policy, reviewer assignments, and release controls.

## Validation expectations for future implementation

A future Ford County implementation should not be considered complete merely because Markdown or a map exists. At minimum, the changed area should eventually prove:

1. interpretation status distinguishes factual claim, interpretation, folklore, tourism narrative, reenactment, and derived indicator;
2. unsupported Dodge City, gunfight, outlaw, cattle-town, or frontier mythology cannot pass as a factual public claim;
3. official, local-history, tourism, marker, archival, scientific, regulatory, and generated source roles remain distinct;
4. Santa Fe Trail, wagon, railroad, and cattle-shipping alignments expose source lineage, temporal scope, confidence, uncertainty, and non-routing posture;
5. exact archaeological, burial, cemetery, sacred, and culturally restricted locations fail closed or are safely generalized;
6. Fort Dodge content cannot expose operational, security, infrastructure, personnel, or vulnerability detail;
7. river, groundwater, water-quality, regulatory, health, safety, allocation, and legal roles remain separate;
8. agriculture and land-cover layers expose date, method, scale, uncertainty, and derived status without private-operation inference;
9. positive and negative fixtures cover `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`;
10. no-network deterministic tests cover the public-history, route-uncertainty, cultural-sensitivity, water-role, and property/privacy boundaries;
11. every consequential public claim resolves from EvidenceRef to EvidenceBundle;
12. governed API/UI surfaces display evidence, interpretation status, policy, limitations, uncertainty, stale, restricted, denied, corrected, and error states;
13. no direct path exists from raw/internal stores, candidate history, private records, observations, or model output to public truth;
14. correction, supersession, withdrawal, and rollback propagate through map, timeline, search, cache, export, and AI surfaces;
15. release evidence is appropriate to the significance of historical, cultural, hydrologic, agricultural, property, and infrastructure claims.

## Known unknowns

The following remain **UNKNOWN** or **NEEDS VERIFICATION** until current implementation evidence proves otherwise:

- which Ford County source descriptors are admitted;
- current rights and derivative-display permissions for county, historical, tourism, archival, marker, scientific, regulatory, hydrologic, and agricultural sources;
- authoritative county, city, trail, railroad, river, public-history, and land-cover geometry;
- safe generalization thresholds for cultural, archaeological, cemetery, military, infrastructure, and private-property information;
- accountable Indigenous, cultural, archaeological, military-history, hydrology, water-quality, agriculture, rights, and release review routes;
- the authoritative temporal and spatial basis for Santa Fe Trail, wagon, railroad, and cattle-shipping claims;
- current KDHE regulatory status and release fitness of water-quality material;
- fit-for-use methods, vintages, scales, and uncertainty for groundwater, hydrology, agriculture, and land-cover products;
- current contracts, schemas, policies, validators, fixtures, and tests applicable to Ford County;
- governed API routes, Explorer UI components, timeline behavior, and Evidence Drawer integration;
- correction propagation through map, timeline, search, cache, export, and AI surfaces;
- any deployed or published Ford County Focus Mode.

## Rollback and correction

This README is documentation-only. Before merge, rollback is abandonment of the feature branch or pull request. After merge, correction should use a transparent revert or forward-fix PR against the actual merged commit.

A documentation rollback does **not** reverse any separate future source admission, policy decision, release manifest, deployment, publication, correction, or public-reliance transition. Those transitions require their own governed records and rollback paths.

## Related

- [Ford County Focus Mode Build Plan](./ford_county_focus_mode_build_plan.md)
- [County index](../COUNTY_INDEX.md)
- [Counties Focus Mode overview](../README.md)

[Back to top](#top)
