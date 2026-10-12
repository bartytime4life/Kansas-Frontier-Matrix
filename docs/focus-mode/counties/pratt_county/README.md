<!-- KFM_META_BLOCK_V2

document_id: kfm://docs/focus-mode/counties/pratt-county

title: Pratt County Focus Mode

type: county-focus-mode-readme

status: draft

truth_posture: cite-or-abstain

repository_path: docs/focus-mode/counties/pratt_county/README.md

related:
  - ./pratt_county_focus_mode_build_plan.md

notes:
  - Same-path modernization of an existing tracked README.
  - This document summarizes the repository-grounded county boundary; it does not claim source admission, implementation, release, deployment, or publication.
-->

<a id="top"></a>

# Pratt County Focus Mode

> **Purpose.** Define the public-safe documentation boundary for Pratt County, Kansas, and connect maintainers to the county build plan without presenting proposed source, runtime, policy, release, or publication work as current implementation.

> [!IMPORTANT]
> This README is a **documentation boundary**, not a live county product. The sibling build plan contains proposed architecture and source-derived planning material. Its claims remain subordinate to current repository evidence, admitted evidence, policy, review, and release state.

## Status at a glance

| Area | Status | Boundary |
|---|---|---|
| County scope | `CONFIRMED` | This lane concerns Pratt County, Kansas. |
| Existing README role | `CONFIRMED` | This file is the tracked county README at the current repository path. |
| Sibling build plan | `CONFIRMED` | `pratt_county_focus_mode_build_plan.md` exists beside this README. |
| County proof slice | `PROPOSED` | The build plan centers Pratt Sandhills, South Fork Ninnescah headwaters, county recreation context, and working-landscape aggregates. |
| Source admission | `UNKNOWN` | A source is not admitted merely because it appears in the build plan. |
| Runtime/API/UI behavior | `UNKNOWN` | This README does not claim implemented county routes, contracts, schemas, MapLibre layers, Evidence Drawer behavior, or Focus Mode execution. |
| Release/publication | `UNKNOWN` | A commit, PR, rendered map, or documentation artifact is not governed publication. |

## County boundary

The Pratt County plan proposes a county experience organized around **Pratt Sandhills Wildlife Area, South Fork Ninnescah headwaters, county civic/recreation context, and county-scale working-landscape evidence**. Its central trust problem is that useful public context can easily become overprecise or time-sensitive field guidance if wildlife, access, road, safety, well, parcel, or legal signals are treated as durable truth.

The defining rule is:

> **Public landscape context must not become live wildlife, access, safety, routing, parcel, well, or legal guidance.**

Any future map, card, source object, or AI answer must preserve source role, time basis, safe spatial scale, and the distinction between educational context and current operational authority.

## Proposed first proof slice

The sibling plan proposes a **Pratt Sandhills Wildlife-Access / Non-Live-Safety Boundary Proof**. In bounded form, that slice would demonstrate that KFM can:

- present generalized Pratt Sandhills and watershed context without exposing sensitive wildlife precision;
- explain county civic and recreation context without asserting current road, closure, facility, hunting, or safety conditions;
- preserve the difference between state wildlife-area context, county civic sources, hydrology, transportation, agriculture, and other source roles;
- keep private land, parcel, title, well, water-right, and individual-risk conclusions outside the public product;
- expose visible negative states when freshness, sensitivity, rights, scale, or release closure is insufficient;
- direct users to current official authorities for time-sensitive access, weather, recreation, road, and emergency information rather than copying volatile status into durable KFM prose.

These are **PROPOSED** behaviors until implementation, validation, evidence closure, policy review, and release state are verified.

## Public-safe rules

| Rule | Required behavior |
|---|---|
| Evidence before interpretation | Consequential claims resolve through governed evidence; generated language never substitutes for evidence. |
| Cite or abstain | Missing or stale support must narrow the answer or return a finite negative state. |
| Wildlife precision is minimized | Sensitive species, nesting, roosting, stocking, habitat-management, or hunt-optimization detail is withheld or generalized. |
| Access and recreation are currentness-sensitive | KFM must not present copied road, closure, hunting, facility, or safety status as current without explicit freshness and release controls. |
| Private-property inference is out of scope | Public UI must not derive parcel ownership, title, permission, private-well status, pumping, or water-right conclusions. |
| Source roles do not collapse | KDWP, county, KDOT, USGS/hydrology, agricultural, and other source families retain distinct authority and limitations. |
| Agriculture remains aggregate | County-level agricultural context must not become farm-, operator-, parcel-, or household-level profiling. |
| Dated maps are not live routing | Historical or dated transportation maps are context only, not current navigation or emergency authority. |
| Public clients stay downstream of trust | UI, map, search, and AI surfaces consume governed/released evidence rather than canonical or working stores. |
| Correction and rollback remain visible | Future source, access, geometry, or interpretation corrections must be able to supersede or withdraw affected public products without rewriting history. |

## Finite outcomes

For this county lane, the expected public-facing outcome vocabulary is:

- `ANSWER` — released evidence is in scope, sufficiently current, policy-safe, citation-valid, and at an allowed spatial precision;
- `ABSTAIN` — evidence, freshness, safe scale, rights, identity, or release closure is insufficient;
- `DENY` — the request would expose sensitive wildlife, unsafe operational guidance, private-property/well information, legal conclusions, or another protected boundary;
- `ERROR` — a resolver, validator, source adapter, policy engine, or runtime dependency failed.

These outcomes are a **design contract**, not proof that the current repository implements them for Pratt County.

## Source-role posture

The build plan discusses several source families. Their appearance in planning material does **not** establish source admission or public-release authority.

| Source family | Intended role | Must not be treated as |
|---|---|---|
| Kansas Department of Wildlife and Parks | Public wildlife-area and land-management context | Live wildlife-location, hunting-optimization, closure, or current safety authority inside KFM |
| Pratt County | Civic/administrative and public-service context | Emergency, property, parcel, title, private-well, or legal truth |
| KDOT | Transportation and administrative-map context where admitted | Live routing, closure, road-condition, or emergency-response authority |
| USGS / hydrography sources | Watershed and hydrologic geometry/context where admitted | Flood, water-quality, irrigation, water-right, or emergency conclusions without separate authority |
| USDA/NASS/NRCS-style sources | County-scale agricultural and soil context where admitted | Farm-, operator-, household-, or parcel-level profiling |

## Repository and placement posture

**CONFIRMED:** this README already exists at `docs/focus-mode/counties/pratt_county/README.md`, so this change keeps the tracked path rather than inventing a new documentation home.

**CONFIRMED:** ADR-0029 is accepted and adopts Directory Rules v2 at `docs/doctrine/directory-rules.md` as the single writable human placement authority.

**NEEDS VERIFICATION:** long-term county-lane naming and any future migration remain separate governance work. This README does not create a parallel Focus Mode home, move the county lane, or change any authority root.

## Relationship to the build plan

The detailed planning artifact is:

- [Pratt County Focus Mode Build Plan](./pratt_county_focus_mode_build_plan.md)

Use the build plan for proposed layers, source seeds, fixtures, risk analysis, implementation phases, and verification questions. Use this README for the stable county-boundary summary and truth posture.

> [!CAUTION]
> The build plan includes source-derived and point-in-time statements from its authoring run. Before implementation or public use, reverify current facts, source terms, rights, identifiers, access/currentness, safe geometry, and release fitness against authoritative sources and current repository controls.

## Validation expectations for future implementation

A future Pratt County implementation should not be considered complete merely because Markdown exists. At minimum, the changed area should eventually prove:

1. safe-scale geometry and generalized wildlife-area presentation;
2. stale/current handling for access, roads, closures, facilities, and safety-related source material;
3. positive and negative fixtures for `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` behavior;
4. deterministic no-network tests for the county trust boundary;
5. EvidenceRef-to-EvidenceBundle closure for consequential claims;
6. source-role, rights, sensitivity, and public-safe policy checks;
7. governed API/UI behavior with visible negative states;
8. no public path from raw wildlife, private-property, well, or operational data to public truth;
9. correction, supersession, and rollback behavior;
10. release evidence appropriate to any time-sensitive access or safety-related claim.

## Known unknowns

The following remain **UNKNOWN** or **NEEDS VERIFICATION** until current implementation evidence proves otherwise:

- which Pratt County source descriptors are admitted;
- authoritative geometry and safe display scale for the Pratt Sandhills and hydrologic layers;
- live source rights and derivative-display permissions;
- exact contracts, schemas, policies, validators, fixtures, and tests for this county;
- governed API routes and UI components;
- current access, recreation, road, wildlife, or county-lake status handling;
- named reviewer/steward assignments;
- correction propagation through map, search, cache, export, and AI surfaces;
- any deployed or published Pratt County Focus Mode.

## Rollback and correction

This README is documentation-only. Before merge, rollback is abandonment of the feature branch or pull request. After merge, correction should use a transparent revert or forward-fix PR against the actual merged commit.

A documentation rollback does **not** reverse any separate future source admission, policy decision, release manifest, deployment, publication, or public correction. Those transitions require their own governed records and rollback paths.

---

**Related:** [Pratt County Focus Mode Build Plan](./pratt_county_focus_mode_build_plan.md) · [County index](../COUNTY_INDEX.md)
