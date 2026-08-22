<!-- KFM_META_BLOCK_V2

document_id: kfm://docs/focus-mode/counties/johnson-county

title: Johnson County Focus Mode

type: county-focus-mode-readme

status: draft

truth_posture: cite-or-abstain

repository_path: docs/focus-mode/counties/johnson_county/README.md

related:
  - ./johnson_county_focus_mode_build_plan.md
  - ../../../adr/ADR-0027-county-focus-mode-control-plane.md
  - ../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md

notes:
  - Same-path modernization of an existing tracked README.
  - This document summarizes the repository-grounded county boundary; it does not claim source admission, implementation, release, deployment, or publication.
-->

<a id="top"></a>
<a id="johnson-county--focus-mode-build-plan"></a>

# Johnson County Focus Mode

> **Purpose.** Define the public-safe documentation boundary for Johnson County, Kansas, and point maintainers to the county build plan without presenting proposed suburban-growth, property, school, environmental, runtime, or release behavior as current implementation.

> [!IMPORTANT]
> This README is a **documentation boundary**, not a live county product, parcel-title service, household-profile dashboard, school-security surface, corporate-facility map, health-risk assessment, or unrestricted environmental-record index. The sibling build plan is a draft design artifact authored on a different repository-evidence boundary. Current repository reads confirm the tracked files and governance surfaces named here, but they do not upgrade the plan's external facts, source rights, object designs, runtime behavior, or release claims into implementation evidence.

## Status at a glance

| Area | Status | Boundary |
|---|---|---|
| County scope | `CONFIRMED` | This tracked lane concerns Johnson County, Kansas. |
| Existing README role | `CONFIRMED` | This file is the county README at the current repository path. |
| Sibling build plan | `CONFIRMED` | `johnson_county_focus_mode_build_plan.md` exists beside this README. |
| Plan repository disclaimer | `STALE / NARROWED` | The plan's no-mounted-repository statement does not describe this implementation session; its proposed paths and behavior still require current verification. |
| County proof slice | `PROPOSED` | The plan combines suburban growth, Shawnee Mission history, streamway parks, transportation, corporate corridors, public services, archives, property/privacy governance, and environmental-remediation context. |
| Source admission | `UNKNOWN` | A source is not admitted merely because the plan cites, links, or discusses it. |
| Runtime/API/UI behavior | `UNKNOWN` | This README does not claim implemented Johnson County routes, contracts, schemas, MapLibre layers, Evidence Drawer behavior, or Focus Mode execution. |
| Current service, access, and environmental state | `UNKNOWN` | Roads, trails, facilities, schools, remediation status, hazards, and public services require authoritative-current evidence. |
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

The Johnson County build plan proposes a map-first experience organized around **Olathe, Overland Park, Shawnee Mission public history, postwar suburban growth, streamway parks, transportation corridors, corporate and office-park geography, school and public-service systems, Johnson County Museum archives, Sunflower Army Ammunition Plant legacy and remediation context, and time-aware atlas claims**.

Its central trust problem is not simply visualizing a data-rich suburban county. It is preventing high-resolution civic, property, school, environmental, transportation, archival, and employment information from becoming household exposure, title claims, student or facility-security detail, corporate intelligence, unsupported health conclusions, or culturally incomplete history.

The system must preserve distinctions among:

- property, appraisal, and tax records and legally authoritative title or ownership conclusions;
- aggregate suburban trends and household-level wealth, health, behavior, or demographic profiles;
- public school and service-area geography and private student, personnel, or security information;
- public corporate-campus context and operational, access-control, personnel, infrastructure, or vulnerability detail;
- environmental-remediation records and present health, liability, compliance, or exposure conclusions;
- streamway and park context and exact sensitive habitat, rare-species, nesting, or inference-enabling locations;
- Shawnee Mission public-history interpretation and Indigenous cultural authority, removal history, or culturally restricted places;
- official records, museum interpretation, archival materials, derived layers, and generated explanation;
- planning or project context and current road, trail, facility, or public-service conditions.

The most important public-safe rule is:

> **Public civic visibility is not permission for household profiling, title determination, student or facility-security exposure, corporate vulnerability analysis, or unsupported cultural, environmental, health, or legal conclusions.**

Missing evidence, rights, temporal fitness, aggregation, cultural review, safe geometry, policy, or release closure should narrow the claim or produce `ABSTAIN`, `DENY`, or another governed finite outcome rather than a confident map answer.

## Proposed proof slice

The sibling plan treats Johnson County as a high-growth suburban, archival, streamway, corporate, and property/privacy stress test for the county Focus Mode architecture. In bounded form, the slice would demonstrate that KFM can:

- explain postwar suburban growth and land-use change using aggregate, method-visible evidence without creating household or parcel profiles;
- present Olathe, Overland Park, and other communities as county-scale civic context without implying current service, property, or person-level conclusions;
- represent Shawnee Mission and related Indigenous/removal history with source-role transparency, culturally appropriate review, and no exposure of restricted places;
- show Mill Creek and other streamway or park context without publishing sensitive habitat locations or treating a trail/park page as current access or safety authority;
- describe transportation and corporate corridors without becoming a live traffic, construction, routing, facility-operation, or vulnerability surface;
- distinguish appraisal and parcel context from title, ownership, valuation advice, legal boundary, access permission, or household inference;
- aggregate school and public-service geography while withholding student, personnel, security, emergency, and building-vulnerability detail;
- explain Sunflower Army Ammunition Plant legacy and remediation source roles without declaring present health risk, legal liability, regulatory compliance, property fitness, or safe access;
- connect archives and museum interpretation to EvidenceRefs and EvidenceBundles without treating collection scale or repeated narrative as proof;
- demonstrate visible `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` states through deterministic, no-network fixtures before live-source or public-release work.

These remain **PROPOSED** behaviors until contracts, schemas, fixtures, validators, policy, evidence, review, runtime integration, and release state are verified.

## Public-safe rules

| Rule | Required behavior |
|---|---|
| Evidence before interpretation | Consequential claims resolve through governed evidence; generated language, map styling, archival abundance, and familiar suburban narratives never substitute for support. |
| Cite or abstain | Missing, stale, conflicted, role-inappropriate, or out-of-scope evidence must narrow the response or return a finite negative state. |
| Property and appraisal are not title | Assessor, tax, parcel, valuation, zoning, and GIS context must not become ownership, legal boundary, access, permit, insurance, valuation advice, or title truth. |
| Household profiling is prohibited | Public data must not be joined into address-level income, health, demographic, behavioral, employment, educational, or risk profiles. |
| School and public-service detail is aggregated | Public district and service geography may be shown at safe scale; student, personnel, security, emergency, access-control, and vulnerable-facility detail is withheld. |
| Corporate and infrastructure detail is minimized | Public business-corridor context must not expose operational systems, facility layouts, personnel patterns, access controls, dependencies, or vulnerabilities. |
| Indigenous and mission history requires authority-aware review | Public-history sources do not replace Nation-authoritative evidence or culturally appropriate review; exact sacred, burial, archaeological, or restricted places fail closed. |
| Environmental records retain source role | Remediation and regulatory records must not become current health, exposure, causation, property-fitness, liability, or compliance conclusions. |
| Streamway and habitat precision is bounded | Public trail, park, and watershed context must not expose exact sensitive species, nests, roosts, habitat-use patterns, or unsafe access assumptions. |
| Transportation currentness is explicit | Planning, construction, and historic-corridor context must not become live traffic, closure, routing, emergency, or road-safety guidance. |
| Archives and interpretation remain distinct | Museum, archive, official, local-history, and generated materials retain separate authority, rights, date, and limitation fields. |
| Public clients stay downstream of trust | UI, map, search, exports, and AI consume governed and released evidence rather than RAW, WORK, QUARANTINE, internal stores, school/property systems, candidate data, or direct model output. |
| Correction and rollback remain visible | Future source, interpretation, parcel, geometry, sensitivity, environmental, or release corrections supersede or withdraw affected products without rewriting history. |

## Proposed layer and card families

The build plan names the following planning families. Their presence here records proposed scope only; it does not prove implementation, source admission, review, or release.

| Layer or card family | Intended role | Public-safe condition |
|---|---|---|
| Johnson County boundary | County-scale spatial frame | Authoritative geometry, version, rights, and release state verified |
| Olathe and Overland Park civic context | County-seat and major-city orientation | No household, property, emergency, or current-service inference |
| Shawnee Mission public-history context | Mission, removal, education, and regional-history interpretation | Authority-aware review; sensitive cultural places withheld |
| Suburban growth and land-use context | Postwar development, annexation, retail, office, and housing-pattern explanation | Aggregate scale, method, date, uncertainty, and non-household posture visible |
| Streamway parks context | Mill Creek and other green-infrastructure or trail corridors | Currentness, rights, ecology review, safe geometry, and non-access/safety posture visible |
| Transportation corridors | Metro mobility and growth context | Planning and current operations separated; no live routing or vulnerability analysis |
| Corporate and office corridors | Public economic-geography context | Generalized public context only; operational and security detail denied |
| School and public-service context | Aggregated districts, libraries, parks, health, and service geography | No student, personnel, security, emergency, or vulnerable-facility detail |
| Sunflower legacy and remediation context | Environmental and land-transition source-role explanation | No present health, liability, compliance, property-fitness, or safe-access conclusion |
| Archives and museum context | Evidence discovery and local-history source routing | Rights, collection scope, interpretation status, and evidence limits visible |
| Timeline events | Time navigation across reviewed claims | Planning buckets do not become facts without evidence closure |
| Atlas claims | Clickable claim-bearing map objects | Every consequential claim carries EvidenceRef and review/release state |

## Finite outcomes

For this county lane, the expected public-facing outcome vocabulary is:

- `ANSWER` — released evidence is in scope, citation-valid, time-fit, rights-cleared, privacy-safe, sensitivity-safe, policy-safe, and review-complete;
- `ABSTAIN` — evidence, currentness, aggregation, cultural authority, source role, geometry, rights, or release closure is insufficient;
- `DENY` — the request seeks private student or personnel data, school security, household profiling, title or access determinations, corporate or infrastructure vulnerabilities, exact sensitive habitat or cultural locations, or another protected inference;
- `ERROR` — an identity resolver, evidence resolver, validator, policy engine, source adapter, citation, integrity check, or runtime dependency failed.

These outcomes are a **proposed design contract**, not proof that the current repository implements them for Johnson County. Exact reason-code names, registry ownership, and runtime enforcement remain **NEEDS VERIFICATION**.

## Source-role posture

The build plan lists candidate source families. A candidate source is neither admitted evidence nor public-release authority.

| Source family | Intended role | Must not be treated as |
|---|---|---|
| Johnson County official materials | County identity, civic administration, services, plans, parks, and current official routing | Title truth, household profile, school-security authority, or universal proof of historical claims |
| Johnson County Park and Recreation / Museum | Park, streamway, archive, exhibit, and public-history context | Automatic cultural authority, current access/safety verdict, or proof that every interpretation is publication-ready |
| Kansas Historical Society / Shawnee Mission sources | Public historic-site and documentary context | Substitute for Nation-authoritative evidence or permission to expose sensitive cultural places |
| City of Olathe and City of Overland Park | Municipal identity, planning, services, and current official routing | Household, property, facility-security, emergency, or citywide legal conclusion |
| Appraisal, parcel, tax, zoning, and GIS sources | Administrative and planning context after explicit review | Title, ownership, survey, legal boundary, access, valuation advice, insurance, or person-level truth |
| School and public-service sources | Aggregate district and service geography | Student, personnel, security, emergency, access-control, or vulnerable-building data |
| KDHE / EPA and related environmental sources | Remediation, regulatory, and environmental-record context | Automatic current health, exposure, causation, liability, compliance, property-fitness, or safe-access determination |
| FEMA / USGS and future hydrology sources | Floodplain, stream, watershed, and observation context after admission | Current flood, emergency, property, engineering, or individual risk authority |
| USDA and derived land-cover sources | Aggregate agriculture, land-cover, and urban-edge context | Household, farm, owner, parcel, valuation, or causal conclusion |
| Corporate public materials | Public business and campus-history context | Operational, security, personnel, access-control, dependency, or vulnerability intelligence |

## Repository and placement posture

**CONFIRMED:** this README already exists at `docs/focus-mode/counties/johnson_county/README.md`, so this change keeps the tracked path and responsibility root rather than inventing a new documentation home.

**CONFIRMED:** [ADR-0029](../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) is accepted and adopts the exact Directory Rules v2 bytes at `docs/doctrine/directory-rules.md` as the single writable human Directory Rules authority.

**CONFIRMED:** [ADR-0027](../../../adr/ADR-0027-county-focus-mode-control-plane.md) remains `proposed` and records the unresolved conflict between the current singular `docs/focus-mode/` lane and a proposed plural county control plane. This README does not use that unaccepted decision to migrate Johnson County, create a parallel lane, or treat the plan's proposed tree as current fact.

## Relationship to the build plan

The detailed planning artifact is:

- [Johnson County Focus Mode Build Plan](./johnson_county_focus_mode_build_plan.md)

Use the build plan for proposed layers, object examples, source seeds, risk analysis, phases, fixtures, mock API/UI ideas, and open verification questions. Use this README for the stable county-boundary summary and current truth posture.

> [!CAUTION]
> The build plan was prepared as a draft on a different evidence boundary and contains proposed paths, endpoints, schemas, validators, source uses, time buckets, and implementation phases. Before implementation or public use, reconcile each material item against current repository evidence, accepted ADRs, authoritative sources, source terms, privacy and cultural-review requirements, environmental and security policy, reviewer assignments, and release controls.

## Validation expectations for future implementation

A future Johnson County implementation should not be considered complete merely because Markdown or a map exists. At minimum, the changed area should eventually prove:

1. parcel, appraisal, tax, zoning, and GIS evidence cannot become title, ownership, legal-boundary, access, insurance, permit, or valuation-advice conclusions;
2. household-level joins and address-based wealth, health, demographic, educational, employment, or risk profiles fail closed;
3. school and public-service layers are aggregated and negative fixtures block student, personnel, security, emergency, and vulnerable-facility detail;
4. corporate and infrastructure layers withhold operational systems, layouts, access controls, dependencies, personnel patterns, and vulnerability-relevant detail;
5. Shawnee Mission and Indigenous/removal history uses authority-aware evidence, appropriate review, and denial/generalization for culturally restricted places;
6. environmental-remediation records cannot become present health, exposure, causation, liability, compliance, property-fitness, or safe-access conclusions;
7. streamway, park, watershed, and habitat geometry uses safe scale and does not expose exact sensitive occurrences or infer current access or safety;
8. planning, construction, historic-corridor, and current transportation states remain distinct;
9. archive and museum interpretation is labeled separately from official records, primary evidence, and generated summaries;
10. positive and negative fixtures cover `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`;
11. no-network deterministic tests cover property/privacy, school/security, corporate/infrastructure, cultural, environmental, and ecology boundaries;
12. every consequential public claim resolves from EvidenceRef to EvidenceBundle;
13. governed API/UI surfaces display evidence, policy, limitation, stale, restricted, denied, corrected, and error states;
14. no direct path exists from raw/internal stores, school/property systems, candidate observations, or model output to public truth;
15. correction, supersession, withdrawal, and rollback propagate through map, timeline, search, cache, export, and AI surfaces;
16. release evidence is appropriate to the significance of property, school, cultural, environmental, health, infrastructure, and privacy claims.

## Known unknowns

The following remain **UNKNOWN** or **NEEDS VERIFICATION** until current implementation evidence proves otherwise:

- which Johnson County source descriptors are admitted;
- current rights and derivative-display permissions for county, municipal, museum, archive, park, environmental, appraisal, school, corporate, and derived sources;
- authoritative county, municipal, streamway, service-area, parcel, school, remediation, and transportation geometry;
- safe aggregation, redaction, small-cell, address, and reidentification thresholds;
- Nation-authoritative and accountable cultural-review pathways for Shawnee Mission and related history;
- current remediation, access, trail, facility, transportation, hazard, and service status;
- exact contracts, schemas, policies, validators, fixtures, and tests applicable to Johnson County;
- governed API routes, Explorer UI components, and Evidence Drawer integration;
- named privacy, property, school, security, cultural, environmental, ecology, rights, and release reviewers;
- correction propagation through map, timeline, search, cache, export, and AI surfaces;
- any deployed or published Johnson County Focus Mode.

## Rollback and correction

This README is documentation-only. Before merge, rollback is abandonment of the feature branch or pull request. After merge, correction should use a transparent revert or forward-fix PR against the actual merged commit.

A documentation rollback does **not** reverse any separate future source admission, policy decision, release manifest, deployment, publication, or public correction. Those transitions require their own governed records and rollback paths.

## Related

- [Johnson County Focus Mode Build Plan](./johnson_county_focus_mode_build_plan.md)
- [County index](../COUNTY_INDEX.md)
- [Counties Focus Mode overview](../README.md)

[Back to top](#top)
