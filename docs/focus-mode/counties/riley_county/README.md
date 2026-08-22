<!-- KFM_META_BLOCK_V2

document_id: kfm://docs/focus-mode/counties/riley-county

title: Riley County Focus Mode

type: county-focus-mode-readme

status: draft

truth_posture: cite-or-abstain

repository_path: docs/focus-mode/counties/riley_county/README.md

related:
  - ./riley_county_focus_mode_build_plan.md
  - ../../../adr/ADR-0027-county-focus-mode-control-plane.md
  - ../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md

notes:
  - Same-path modernization of an existing tracked README.
  - This document summarizes the repository-grounded county boundary; it does not claim source admission, implementation, release, deployment, or publication.
-->

<a id="top"></a>
<a id="riley-county--focus-mode-build-plan"></a>

# Riley County Focus Mode

> **Purpose.** Define the public-safe documentation boundary for Riley County, Kansas, and point maintainers to the county build plan without presenting proposed sources, layers, runtime behavior, or release work as current implementation.

> [!IMPORTANT]
> This README is a **documentation boundary**, not a live county product. The sibling build plan is a draft design artifact authored before its writer had mounted-repository evidence. Current repository reads confirm the files and governance surfaces named here, but they do not upgrade the plan's external facts, source rights, object designs, runtime behavior, or release claims into implementation evidence.

## Status at a glance

| Area | Status | Boundary |
|---|---|---|
| County scope | `CONFIRMED` | This tracked lane concerns Riley County, Kansas. |
| Existing README role | `CONFIRMED` | This file is the county README at the current repository path. |
| Sibling build plan | `CONFIRMED` | `riley_county_focus_mode_build_plan.md` exists beside this README. |
| Plan repository disclaimer | `STALE / NARROWED` | The plan's no-mounted-repository statement does not describe this implementation session; its proposed paths and behavior still require current verification. |
| County proof slice | `PROPOSED` | The plan combines Flint Hills ecology, Konza Prairie research context, Fort Riley public history, Manhattan/Kansas State University civic context, river systems, transportation corridors, and public-safe controls. |
| Source admission | `UNKNOWN` | A source mentioned in the plan is not admitted merely because it is public, cited, or linked. |
| Runtime/API/UI behavior | `UNKNOWN` | This README does not claim implemented Riley County routes, contracts, schemas, MapLibre layers, Evidence Drawer behavior, or Focus Mode execution. |
| Release/publication | `UNKNOWN` | A document, branch, commit, PR, rendered map, or passing check is not governed publication. |

## Contents

- [County boundary](#county-boundary)
- [Proposed proof slice](#proposed-proof-slice)
- [Public-safe rules](#public-safe-rules)
- [Proposed layer families](#proposed-layer-families)
- [Finite outcomes](#finite-outcomes)
- [Source-role posture](#source-role-posture)
- [Repository and placement posture](#repository-and-placement-posture)
- [About this plan](#about-this-plan)
- [Validation expectations](#validation-expectations-for-future-implementation)
- [Known unknowns](#known-unknowns)
- [Rollback and correction](#rollback-and-correction)
- [Related](#related)

## County boundary

The Riley County build plan proposes a map-first experience organized around **Flint Hills and Konza Prairie ecology, Fort Riley public historical geography, Manhattan and Kansas State University civic/research context, river corridors, Tuttle Creek context, historic transportation routes, land-cover change, and time-aware atlas claims**.

Its central trust problem is not simply combining many themes on one map. It is preserving the differences among:

- public historical context and restricted or operational military information;
- generalized ecological context and exact sensitive observations;
- research-site context and public-recreation assumptions;
- observed, derived, interpreted, and modeled layers;
- historical-route evidence and uncertain alignment;
- hydrologic context and live flood, water-management, navigation, or emergency authority;
- source evidence and generated explanation.

The most important public-safe rule is:

> **Context is not operational access. A historical, ecological, hydrologic, research, or military layer must not become live field guidance, sensitive-location disclosure, infrastructure intelligence, or unsupported certainty.**

Missing evidence, source rights, temporal fitness, safe geometry, sensitivity review, or release closure should narrow the claim or produce `ABSTAIN`, `DENY`, or another governed finite outcome rather than a plausible-looking map answer.

## Proposed proof slice

The sibling plan treats Riley County as a complementary stress test for the county Focus Mode architecture. In bounded form, the slice would demonstrate that KFM can:

- present public Fort Riley historical context without exposing restricted, operational, security-relevant, or emergency detail;
- explain Konza Prairie and Flint Hills research/ecology context using reviewed, generalized evidence rather than exact sensitive observations;
- distinguish Manhattan/Kansas State University civic and research context from current institutional operations or unverified local claims;
- show river, drainage, reservoir, and land-cover context without issuing flood, water-right, navigation, infrastructure, or emergency conclusions;
- display historic transportation corridors with visible uncertainty and limitation instead of false cartographic precision;
- connect map features and timeline items to EvidenceRefs and EvidenceBundles before consequential claims are presented as authoritative;
- demonstrate visible `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` states through deterministic, no-network fixtures before live-source or public release work.

These remain **PROPOSED** behaviors until contracts, schemas, fixtures, validators, policy, evidence, review, runtime integration, and release state are verified.

## Public-safe rules

| Rule | Required behavior |
|---|---|
| Evidence before interpretation | Consequential claims resolve through governed evidence; generated language, map styling, and model confidence never substitute for support. |
| Cite or abstain | Missing, stale, conflicted, or out-of-scope evidence must narrow the answer or return a finite negative state. |
| Military detail is minimized | Fort Riley content remains bounded to reviewed public historical/geographic context; operational, security, infrastructure, personnel, access, readiness, and emergency detail is excluded or denied. |
| Ecological sensitivity is explicit | Konza/Flint Hills context must not expose exact rare-species, nesting, roosting, research-observation, or inference-enabling sensitive locations. |
| Research rights remain visible | Publicly discoverable research material does not establish reuse, redistribution, derivative-display, or publication permission. |
| Cultural and archaeological material fails closed | Exact sacred, burial, archaeological, or culturally restricted places are withheld; public interpretation requires appropriate source and review authority. |
| Hydrology is role-bounded | River and Tuttle Creek context must not become live flood, dam-operation, navigation, water-quality, allocation, or emergency guidance. |
| Historical routes show uncertainty | Military-road or transportation alignments must expose source role, temporal scope, confidence, and limitations. |
| Living-person and property profiles are out of scope | No genealogy, personal data, private parcel/title truth, or household-level inference is created by this lane. |
| Public clients stay downstream of trust | UI, map, search, exports, and AI consume governed/released evidence rather than RAW, WORK, QUARANTINE, internal stores, or direct model output. |
| Correction and rollback remain visible | Future geometry, source, sensitivity, interpretation, or access corrections must be able to supersede or withdraw affected products without rewriting history. |

## Proposed layer families

The build plan names the following layer families. Their presence here records planning scope only; it does not prove implementation or release.

| Layer family | Intended role | Public-safe condition |
|---|---|---|
| Riley County boundary | County-scale spatial frame | Authoritative geometry, version, rights, and release state verified |
| Manhattan civic context | Settlement and civic orientation | No living-person, property, emergency, or current-service inference |
| Fort Riley historical context | Public historical/military-geography anchor | Historical public scope only; operational and restricted detail denied |
| Konza Prairie / Flint Hills context | Ecology and research-site interpretation | Generalized geometry, rights review, sensitivity review, source-role visibility |
| River and drainage corridors | Hydrologic and landscape context | No live flood, safety, water-right, water-quality, or navigation conclusion |
| Tuttle Creek context | Reservoir/watershed interpretation | No operational, infrastructure-vulnerability, access, or emergency guidance |
| Historic military-road context | Transportation and historical movement | Uncertainty, source lineage, and non-routing posture visible |
| Land-cover baseline | Derived prairie/agriculture matrix | Method, date, source role, uncertainty, and derivative status visible |
| Timeline events | Time navigation across reviewed claims | Planning buckets do not become facts without evidence closure |
| Atlas claims | Clickable claim-bearing map objects | Every consequential claim carries EvidenceRef and review/release state |

## Finite outcomes

For this county lane, the expected public-facing outcome vocabulary is:

- `ANSWER` — released evidence is in scope, citation-valid, time-fit, rights-cleared, sensitivity-safe, policy-safe, and review-complete;
- `ABSTAIN` — evidence, temporal scope, source role, geometry, rights, sensitivity, confidence, or release closure is insufficient;
- `DENY` — the request would expose restricted military information, sensitive ecology, protected cultural/archaeological locations, living-person data, private property truth, unsafe infrastructure detail, or another protected boundary;
- `ERROR` — a resolver, validator, policy engine, source adapter, or runtime dependency failed.

These outcomes are a **proposed design contract**, not proof that the current repository implements them for Riley County.

## Source-role posture

The build plan lists candidate source seeds. A candidate source is neither admitted evidence nor public-release authority.

| Source family | Intended role | Must not be treated as |
|---|---|---|
| Riley County official materials | County civic, administrative, and local-history context | Property/title truth, current emergency authority, or proof of every historical claim |
| Fort Riley official public history | Public historical context for Fort Riley | Permission to expose operational, security, access, personnel, or infrastructure detail |
| Konza Prairie / Kansas State University materials | Research-site and ecology context | Automatic reuse permission, exact sensitive-observation authority, or public-recreation guidance |
| The Nature Conservancy | Conservation and public overview context | Primary research-data authority or permission to expose sensitive ecological detail |
| Kansas Geological Survey | Geology, terrain, and historical scientific context | Live hazard, flood, water-management, legal, military, or cultural authority |
| Chapman Center / historical-route materials | Military-road and route-history interpretation | A precise, legally authoritative, or uncertainty-free modern route alignment |
| Kansas Historical Society materials | Historical markers and public-history context | Complete evidence closure for complex cultural, military, or archaeological claims |
| Future hydrology and land-cover sources | Observed or derived environmental context after admission | Emergency, dam-operation, navigation, water-right, property, or public-safety authority |

## Repository and placement posture

**CONFIRMED:** this README already exists at `docs/focus-mode/counties/riley_county/README.md`, so this change keeps the tracked path and responsibility root rather than inventing a new documentation home.

**CONFIRMED:** [ADR-0029](../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) is accepted and adopts the exact Directory Rules v2 bytes at `docs/doctrine/directory-rules.md` as the single writable human Directory Rules authority.

**CONFIRMED:** [ADR-0027](../../../adr/ADR-0027-county-focus-mode-control-plane.md) remains `proposed` and explicitly records a conflict between the current singular `docs/focus-mode/` lane and a proposed plural control plane. This README does not use that unaccepted decision to migrate Riley County, create a parallel lane, or treat the proposed repository tree in the build plan as current fact.

## About this plan

The detailed planning artifact is:

- [Riley County Focus Mode Build Plan](./riley_county_focus_mode_build_plan.md)

Use the build plan for proposed layers, object examples, source seeds, risk analysis, phases, fixtures, mock API/UI ideas, and open verification questions. Use this README for the stable county-boundary summary and current truth posture.

> [!CAUTION]
> The build plan was prepared as a draft on a different evidence boundary and contains proposed paths, endpoints, schemas, validators, source uses, time buckets, and implementation phases. Before implementation or public use, reconcile each material item against current repository evidence, accepted ADRs, authoritative sources, source terms, sensitivity policy, reviewer assignments, and release controls.

## Validation expectations for future implementation

A future Riley County implementation should not be considered complete merely because Markdown or a map exists. At minimum, the changed area should eventually prove:

1. public-safe Fort Riley historical scope with negative fixtures for restricted or operational detail;
2. generalized Konza/Flint Hills geometry with negative fixtures for exact or inference-enabling sensitive ecology;
3. explicit source terms, rights, sensitivity, temporal scope, and review state for research-derived material;
4. observed/derived/interpreted/modeled distinctions for every layer;
5. route-confidence and uncertainty handling for historical transportation claims;
6. positive and negative fixtures for `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`;
7. no-network deterministic tests for the military/ecology trust boundary;
8. EvidenceRef-to-EvidenceBundle closure for every consequential public claim;
9. governed API/UI behavior with visible evidence, policy, limitation, stale, restricted, denied, and error states;
10. no direct path from raw/internal stores, candidate observations, or model output to public truth;
11. correction, supersession, withdrawal, and rollback behavior across map, search, cache, export, and AI surfaces;
12. release evidence appropriate to the significance of military, ecology, cultural, hydrologic, and infrastructure claims.

## Known unknowns

The following remain **UNKNOWN** or **NEEDS VERIFICATION** until current implementation evidence proves otherwise:

- which Riley County source descriptors are admitted;
- current rights and derivative-display permissions for candidate research, history, geology, map, and conservation sources;
- safe geometry and generalization thresholds for Fort Riley, Konza, sensitive ecology, cultural places, and infrastructure;
- the authoritative temporal and spatial basis for historical military-road claims;
- current contracts, schemas, policies, validators, fixtures, and tests applicable to Riley County;
- governed API routes, Explorer UI components, and Evidence Drawer integration;
- named military, ecology, cultural, hydrology, rights, security, and release reviewers;
- correction propagation through map, timeline, search, cache, export, and AI surfaces;
- any deployed or published Riley County Focus Mode.

## Rollback and correction

This README is documentation-only. Before merge, rollback is abandonment of the feature branch or pull request. After merge, correction should use a transparent revert or forward-fix PR against the actual merged commit.

A documentation rollback does **not** reverse any separate future source admission, policy decision, release manifest, deployment, publication, or public correction. Those transitions require their own governed records and rollback paths.

## Related

- [Riley County Focus Mode Build Plan](./riley_county_focus_mode_build_plan.md)
- [County index](../COUNTY_INDEX.md)
- [Counties Focus Mode overview](../README.md)

[Back to top](#top)
