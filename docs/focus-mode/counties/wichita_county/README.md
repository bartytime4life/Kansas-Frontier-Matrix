<!-- KFM_META_BLOCK_V2

document_id: kfm://docs/focus-mode/counties/wichita-county-kansas

title: Wichita County, Kansas Focus Mode

type: county-focus-mode-readme

status: draft

truth_posture: cite-or-abstain

repository_path: docs/focus-mode/counties/wichita_county/README.md

related:
  - ./wichita_county_build_plan.md
  - ../../../adr/ADR-0027-county-focus-mode-control-plane.md
  - ../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md

notes:
  - Same-path modernization of an existing tracked README.
  - This document summarizes the repository-grounded county boundary; it does not claim source admission, implementation, release, deployment, or publication.
-->

<a id="top"></a>

# Wichita County, Kansas Focus Mode

> **Purpose.** Define the public-safe documentation boundary for Wichita County, Kansas, and point maintainers to the county build plan without presenting proposed identity, groundwater, legal-status, runtime, operational, or release behavior as current implementation.

> [!IMPORTANT]
> This README is a **documentation boundary**, not a live county product, private-well adviser, water-right service, allocation calculator, compliance system, landowner database, burn-ban monitor, weather service, or infrastructure-security surface. The sibling build plan contains proposed architecture and source-derived planning material checked in June 2026. Its statements remain subordinate to current repository evidence, authoritative-current sources, admitted evidence, policy, review, and release state.

## Status at a glance

| Area | Status | Boundary |
|---|---|---|
| County scope | `CONFIRMED` | This tracked lane concerns Wichita County, Kansas. |
| Existing README role | `CONFIRMED` | This file is the county README at the current repository path. |
| Sibling build plan | `CONFIRMED` | `wichita_county_build_plan.md` exists beside this README. |
| Plan filename declaration | `CONFLICTED / NEEDS VERIFICATION` | The tracked file is `wichita_county_build_plan.md`, while the plan internally names `wichita_county_focus_mode_build_plan.md` as its deliverable. This README preserves the tracked filename and does not rename either artifact. |
| County proof slice | `PROPOSED` | The plan centers geographic-entity resolution, Leoti, High Plains aquifer context, GMD1 and LEMA governance, county-scale agriculture, municipal-water context, and official-current redirects. |
| Source admission | `UNKNOWN` | A source is not admitted merely because the plan cites, links, or discusses it. |
| Runtime/API/UI behavior | `UNKNOWN` | This README does not claim implemented county routes, contracts, schemas, entity resolution, MapLibre layers, Evidence Drawer behavior, or Focus Mode execution. |
| Current legal and operational state | `UNKNOWN` | LEMA approval, burn restrictions, weather, roads, emergency notices, and municipal conditions require current official authority. |
| Release/publication | `UNKNOWN` | A document, commit, pull request, rendered map, or passing check is not governed publication. |

## Contents

- [County and identity boundary](#county-and-identity-boundary)
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

## County and identity boundary

The Wichita County build plan proposes a map-first experience organized around **Wichita County, Kansas; Leoti; county-scale agriculture; High Plains aquifer science; Western Kansas Groundwater Management District No. 1; Wichita County LEMA records; municipal-water authority; and official-current county and weather routing**.

Its first trust problem is identity. An unqualified request for “Wichita” can refer to several different places. The plan requires a future resolver to distinguish:

- Wichita County, Kansas;
- the City of Wichita;
- Sedgwick County, Kansas; and
- Wichita County, Texas.

The plan uses a Kansas county identity composed from state, county name, county FIPS, Leoti, and authoritative geometry. Those source-derived identity fields must still be bound to admitted, current evidence before runtime or release reliance.

The most important public-safe rule is:

> **Resolve the county before retrieving evidence, and never convert county-scale groundwater or governance context into private, legal, operational, or property-level truth.**

Wrong-geography evidence should fail as an identity error. Ambiguous geography should produce `ABSTAIN` with bounded choices. Missing legal status, currentness, rights, scale, privacy review, or release closure should never be filled by generated language.

## Proposed proof slice

The sibling plan proposes a **Wichita County Entity Resolution and Groundwater-Governance Boundary Proof**. In bounded form, that slice would demonstrate that KFM can:

- resolve Wichita County, Kansas before source retrieval and reject evidence belonging to Wichita city, Sedgwick County, or Wichita County, Texas;
- present Leoti and county-scale civic orientation without creating living-person, title, access, tax, appraisal, or property profiles;
- explain High Plains aquifer context at the scale and time supported by admitted scientific evidence without characterizing a private well, household supply, legal right, property value, or remaining allocation;
- keep Kansas Geological Survey science, GMD1 management-district context, and Kansas Division of Water Resources legal or administrative authority distinct;
- represent LEMA proposal, submission, hearing, order, revision, approval, effective period, expiration, and supersession as separate evidence-backed states;
- preserve USDA NASS suppression and county aggregation without reconstructing operations, owners, workers, or individual farms;
- explain municipal-water ordinances or report availability without giving household potability, service-line, compliance, or network-vulnerability conclusions;
- abstain when current burn-ban, weather, road, emergency, or legal-status sources conflict, are stale, or lack a governed currentness envelope;
- demonstrate `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` through deterministic, no-network fixtures before live-source or public-release work.

These remain **PROPOSED** behaviors until contracts, schemas, identity records, fixtures, validators, policy, evidence, review, runtime integration, and release state are verified.

## Public-safe rules

| Rule | Required behavior |
|---|---|
| Entity resolution comes first | Every consequential request binds the intended state, county identity, authoritative geometry, and stable identifier before evidence retrieval. |
| Wrong Wichita evidence fails closed | City of Wichita, Sedgwick County, and Wichita County, Texas material must not enter a Wichita County, Kansas answer through name similarity. |
| Evidence before interpretation | Consequential claims resolve through governed evidence; generated language, cached snippets, map labels, and model confidence never substitute for support. |
| Cite or abstain | Missing, stale, conflicted, role-inappropriate, or out-of-scope support must narrow the response or return a finite negative state. |
| Legal and administrative states stay distinct | Proposed, submitted, heard, returned, revised, approved, effective, expired, and superseded LEMA states cannot collapse into a fluent summary. |
| Source roles do not collapse | KGS scientific interpretation, GMD1 management context, KDA/DWR legal administration, county/city administration, NASS statistics, Census identity/statistics, and NWS operations retain distinct authority. |
| Aquifer scale is explicit | County or regional aquifer evidence must not become a private-well, household, property, allocation, compliance, or legal-right conclusion. |
| Private wells and water rights fail closed | No public yield, life, depth, contamination, potability, priority, ownership, validity, impairment, transferability, or compliance determination is produced. |
| Individual allocations are out of scope | Allocation and Combined Well Unit materials must not become public person-, owner-, farm-, or right-specific calculations or advice. |
| Agricultural confidentiality is preserved | Suppressed values remain suppressed; no farm, operator, worker, feedlot, parcel, or operation profile is reconstructed through joins. |
| Small-population privacy is heightened | Property, water, agriculture, public-record, and living-person datasets require reidentification review before any joined public derivative. |
| Municipal-water context is bounded | Ordinances and system reports may support dated authority context, not household potability, current compliance, exposure, private-well, or network-security conclusions. |
| Current operations expire | Burn bans, weather, roads, alerts, meetings, and emergency notices require checked time, expiry, supersession, and official-current routing. Conflicts produce `ABSTAIN`. |
| Infrastructure detail is minimized | Exact wells, utilities, controls, monitoring configurations, road or energy systems, emergency systems, and vulnerability-relevant detail are withheld or generalized. |
| Public clients stay downstream of trust | UI, map, search, exports, and AI consume governed and released evidence rather than RAW, WORK, QUARANTINE, direct rights/allocation systems, parcel systems, emergency banners, or model output. |
| Correction and rollback remain visible | Future identity, legal-status, source, currentness, privacy, geometry, interpretation, or release corrections must supersede or withdraw affected products without rewriting history. |

## Proposed layer and card families

The build plan describes the following planning families. Their presence here records proposed scope only; it does not prove implementation, source admission, review, or release.

| Layer or card family | Intended role | Public-safe condition |
|---|---|---|
| Wichita County entity-resolution card | State, county, seat, FIPS, geometry, aliases, and prohibited confusions | Admitted identity sources and geometry digest; mismatch and ambiguity tests pass |
| County frame and Leoti context | County-scale civic orientation | No living-person, property, emergency, or operational inference |
| Census aggregate card | Dated population and geography context | Reference periods and disclosure flags visible; no household inference |
| 2022 agriculture snapshot | County-scale NASS context | Reporting year and suppression visible; no operation-level inference |
| High Plains aquifer context | Scientific groundwater interpretation | Product version, scale, time, rights, and private-well non-claims visible |
| GMD1 role card | Management-district mission and public-process context | No legal-right, approval, or compliance determination |
| Wichita County LEMA timeline | Evidence-backed proposal, hearing, order, revision, approval, effective, expiration, and supersession states | Current official status reverified; no individual allocation or compliance advice |
| Leoti municipal-water authority card | Ordinance and report-routing context | Redirect-first; no household potability, exposure, compliance, or network conclusion |
| County and NWS operational redirect | Official-current burn, weather, road, alert, and emergency routing | Checked time and expiry required; no cached KFM safety verdict |
| Identity and water boundary notice | Explain what KFM will not infer or expose | Visible on map, evidence, answer, abstention, denial, export, and correction surfaces |

## Finite outcomes

For this county lane, the expected public-facing outcome vocabulary is:

- `ANSWER` — the Kansas county entity is resolved and released evidence is in scope, citation-valid, time-fit, rights-cleared, privacy-safe, policy-safe, and review-complete;
- `ABSTAIN` — geography, legal status, currentness, rights, scale, source role, evidence, or release closure is insufficient or conflicting;
- `DENY` — the request seeks private-well, individualized allocation, compliance, owner, farm, property, living-person, exact infrastructure, or other protected inference;
- `ERROR` — evidence belongs to the wrong Wichita geography, or an identity, integrity, contract, citation, policy, manifest, or service dependency failed.

These outcomes are a **proposed design contract**, not proof that the current repository implements them for Wichita County.

Representative proposed reason codes from the plan include:

- `WC-ENTITY-AMBIGUOUS`
- `WC-ENTITY-MISMATCH`
- `WC-EVIDENCE-MISSING`
- `WC-EVIDENCE-STALE`
- `WC-LEMA-STATUS-UNCLEAR`
- `WC-OPERATIONAL-CONFLICT`
- `WC-RIGHTS-UNCLEAR`
- `WC-WATER-RIGHT-LEGAL`
- `WC-PRIVATE-WELL`
- `WC-ALLOCATION-INDIVIDUAL`
- `WC-COMPLIANCE-JUDGMENT`
- `WC-OWNER-PROFILE`
- `WC-INDIVIDUAL-FARM`
- `WC-INFRASTRUCTURE-EXACT`
- `WC-LIVE-HAZARD-REDIRECT`
- `WC-INTEGRITY-FAIL`

Reason-code naming, registry ownership, and runtime enforcement remain **NEEDS VERIFICATION**.

## Source-role posture

The build plan lists candidate source families. A candidate source is neither admitted evidence nor public-release authority.

| Source family | Intended role | Must not be treated as |
|---|---|---|
| Wichita County official materials | County identity, administration, meetings, offices, and current official routing | Living-person profile, property/title truth, current safety answer, or unrestricted reuse authority |
| City of Leoti materials | Municipal identity, ordinances, reports, GIS, services, and current official routing | Household potability, current compliance, network status, property truth, or infrastructure-vulnerability evidence |
| U.S. Census Bureau | County identity and dated aggregate demographic/geographic statistics | Living-person, household, employment, legal-status, or property evidence |
| USDA NASS | Dated county agricultural aggregates and disclosure suppression | Farm, operator, worker, feedlot, parcel, allocation, or reconstructed confidential values |
| Kansas Geological Survey | Scientific aquifer and geological context | Water-right, LEMA approval, individual allocation, compliance, private-well, or property authority |
| Western Kansas GMD1 | Management-district role, stakeholder process, and district-published LEMA context | Chief Engineer approval, individualized legal advice, or public allocation calculation |
| Kansas Division of Water Resources | State water administration and admitted official decisions | Scientific aquifer interpretation, household advice, or permission to expose private right/well data |
| National Weather Service Goodland | Official-current weather and hazard authority | KFM-authored warning, emergency command, or durable cached safety verdict |
| Future property, water-right, well, or GIS sources | Restricted administrative or scientific context after explicit review | Direct public owner, well, right, allocation, compliance, access, or vulnerability product |

## Repository and placement posture

**CONFIRMED:** this README already exists at `docs/focus-mode/counties/wichita_county/README.md`, so this change keeps the tracked path and responsibility root rather than inventing a new documentation home.

**CONFIRMED:** the detailed tracked plan is `wichita_county_build_plan.md`. The plan's internal metadata names a different deliverable filename. That naming drift is documented here and remains unresolved; this README does not silently rename the plan or create a second copy.

**CONFIRMED:** [ADR-0029](../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) is accepted and adopts the exact Directory Rules v2 bytes at `docs/doctrine/directory-rules.md` as the single writable human Directory Rules authority.

**CONFIRMED:** [ADR-0027](../../../adr/ADR-0027-county-focus-mode-control-plane.md) remains `proposed` and records the unresolved conflict between the current singular `docs/focus-mode/` lane and a proposed plural county control plane. This README does not use that unaccepted decision to migrate Wichita County, create a parallel lane, or treat the plan's proposed tree as current fact.

## Relationship to the build plan

The detailed planning artifact is:

- [Wichita County Focus Mode Build Plan](./wichita_county_build_plan.md)

Use the build plan for proposed entity-resolution objects, LEMA state vocabulary, source seeds, layer/card designs, risk analysis, phases, fixtures, UI ideas, and open verification questions. Use this README for the stable county-boundary summary and current truth posture.

> [!CAUTION]
> The build plan contains point-in-time external facts, legal and administrative status statements, population and agricultural values, conflicting current-status observations, proposed paths, and source-derived claims from its June 2026 authoring run. Before implementation or public use, reverify current facts, entity identifiers, authoritative geometry, LEMA status, source terms, report periods, suppression rules, privacy and infrastructure posture, operational currentness, reviewer assignments, and release fitness against authoritative sources and current repository controls.

## Validation expectations for future implementation

A future Wichita County implementation should not be considered complete merely because Markdown or a map exists. At minimum, the changed area should eventually prove:

1. Wichita County, Kansas resolves through admitted state, county, FIPS, seat, and geometry evidence before claim retrieval;
2. City of Wichita, Sedgwick County, and Wichita County, Texas fixtures fail as mismatches, while ambiguous “Wichita” requests abstain with bounded choices;
3. LEMA proposal, submission, hearing, order, revision, approval, effective, expiration, and supersession states validate as distinct transitions;
4. GMD1, KDA/DWR, KGS, county, city, Census, NASS, and NWS source roles remain separate;
5. aquifer cards expose product date, scale, scientific role, uncertainty, and private-well/property/legal non-claims;
6. private-well, water-right, individual-allocation, compliance, owner, farm, and infrastructure requests fail closed without echoing protected values;
7. NASS and Census suppression/disclosure flags are preserved and cannot be reconstructed through joins;
8. small-population and multi-source joins undergo reidentification review;
9. operational conflicts and expired county, city, road, burn-ban, weather, and emergency material produce `ABSTAIN` and official redirects;
10. positive and negative fixtures cover `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` in deterministic, no-network tests;
11. every consequential public claim resolves from EvidenceRef to EvidenceBundle;
12. governed API/UI surfaces display resolved entity, source role, legal status, evidence, policy, dates, expiry, scale, rights, privacy, stale, restricted, denied, corrected, and error states;
13. no direct path exists from raw/internal stores, water-right or allocation systems, private-well or parcel systems, emergency banners, or model output to public truth;
14. identity, legal-status, source, privacy, and currentness corrections propagate through map, timeline, search, cache, export, and AI surfaces;
15. release evidence includes review, citation validation, correction, withdrawal, and rollback appropriate to groundwater, legal-status, privacy, and infrastructure significance.

## Known unknowns

The following remain **UNKNOWN** or **NEEDS VERIFICATION** until current implementation evidence proves otherwise:

- which Wichita County source descriptors are admitted;
- the canonical KFM entity and alias registry for Wichita County, Kansas;
- authoritative county geometry, vintage, CRS, aliases, and digest;
- current LEMA approval, effective period, plan version, and supersession status;
- current rights and derivative-display permissions for county, city, GMD1, KDA, KGS, Census, NASS, map, document, and attachment sources;
- safe public scale and fields for aquifer, LEMA, water-right, well, agricultural, property, municipal, road, and energy information;
- current burn-ban, weather, road, emergency, and municipal-notice authority and expiry behavior;
- the canonical filename for the Wichita County build plan;
- current contracts, schemas, identity objects, policies, validators, reason-code registries, fixtures, and tests applicable to this county;
- governed API routes, Explorer UI components, Evidence Drawer integration, and entity-selection behavior;
- named entity, groundwater, water-law, agriculture, municipal-water, privacy, security, rights, and release reviewers;
- correction propagation through map, timeline, search, cache, export, and AI surfaces;
- any deployed or published Wichita County Focus Mode.

## Rollback and correction

This README is documentation-only. Before merge, rollback is abandonment of the feature branch or pull request. After merge, correction should use a transparent revert or forward-fix PR against the actual merged commit.

A documentation rollback does **not** reverse any separate future source admission, entity-record change, policy decision, LEMA status correction, release manifest, deployment, publication, or public correction. Those transitions require their own governed records and rollback paths.

---

**Related:** [Wichita County Focus Mode Build Plan](./wichita_county_build_plan.md) · [County index](../COUNTY_INDEX.md) · [Counties Focus Mode overview](../README.md)

[Back to top](#top)
