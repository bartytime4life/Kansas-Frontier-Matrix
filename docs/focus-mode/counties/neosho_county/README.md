<!-- KFM_META_BLOCK_V2

document_id: kfm://docs/focus-mode/counties/neosho-county

title: Neosho County Focus Mode

type: county-focus-mode-readme

status: draft

truth_posture: cite-or-abstain

repository_path: docs/focus-mode/counties/neosho_county/README.md

related:
  - ./neosho_county_focus_mode_build_plan.md

notes:
  - Same-path modernization of an existing tracked README.
  - This document summarizes the repository-grounded county boundary; it does not claim source admission, implementation, release, deployment, or publication.
-->

<a id="top"></a>

# Neosho County Focus Mode

> **Purpose.** Define the public-safe documentation boundary for Neosho County, Kansas, and point maintainers to the county build plan without presenting proposed source, runtime, release, or publication work as current implementation.

> [!IMPORTANT]
> This README is a **documentation boundary**, not a live county product. The sibling build plan contains proposed architecture and source-derived planning material; it remains subordinate to current repository evidence, accepted governance, admitted evidence, policy, review, and release state.

## Status at a glance

| Area | Status | Boundary |
|---|---|---|
| County scope | `CONFIRMED` | This lane concerns Neosho County, Kansas. |
| Existing README role | `CONFIRMED` | This file is the tracked county README at the current repository path. |
| Sibling build plan | `CONFIRMED` | `neosho_county_focus_mode_build_plan.md` exists beside this README. |
| County proof slice | `PROPOSED` | The build plan centers a managed-wetland, refuge-access, wildlife-sensitivity, and floodplain/public-data trust proof. |
| Source admission | `UNKNOWN` | No source is treated as admitted merely because the build plan cites or discusses it. |
| Runtime/API/UI behavior | `UNKNOWN` | This README does not claim implemented county routes, contracts, schemas, MapLibre layers, Evidence Drawer behavior, or Focus Mode execution. |
| Release/publication | `UNKNOWN` | A commit, PR, rendered map, or document is not governed publication. |

## County boundary

The Neosho County plan proposes a county experience organized around **Neosho Wildlife Area, the Neosho River, Flat Rock Creek, managed wetlands, floodplain context, geology, and county-scale agriculture**. Its central trust problem is not simply displaying a public wildlife area; it is preventing public habitat information from becoming a live wildlife-targeting, hunting-optimization, stale access-guidance, or fine-grained management-operations surface.

The most important public-safe rule is:

> **Habitat context is not live targeting guidance.**

Any future map, evidence object, closure card, search result, export, or AI answer must preserve the distinction between broad public habitat context and current wildlife location, access status, management operations, or field advice. Missing currentness, sensitivity review, or safe-scale evidence should produce `ABSTAIN`, `DENY`, or another governed finite outcome rather than a guessed recommendation.

## Proposed first proof slice

The sibling plan proposes a **Neosho Managed Wetland and Refuge Boundary Proof**. In bounded form, that slice would demonstrate that KFM can:

- present static, source-attributed context for a managed wetland complex without exposing live or predicted wildlife concentrations;
- preserve the distinction between habitat purpose, refuge/closure rules, public recreation, hydrology, floodplain information, water-quality material, geology, and agriculture;
- route users toward current official access and rule authorities rather than copying time-sensitive field guidance into durable prose;
- suppress unnecessary water-control or wetland-management operational detail in the first public-safe product;
- keep parcel, floodplain, regulatory, and water-quality material from becoming legal, insurance, permit, safety, or liability determinations;
- expose visible negative states when freshness, rights, sensitivity, identity, review, or release closure is missing.

These are **PROPOSED** behaviors until implementation, validation, evidence closure, policy review, and release state are verified.

## Public-safe rules

The Neosho County lane should preserve the following boundaries from the build plan and KFM doctrine:

| Rule | Required behavior |
|---|---|
| Evidence before interpretation | Consequential claims resolve through governed evidence; generated language never substitutes for evidence. |
| Cite or abstain | Missing or stale support must narrow the answer or return a finite negative state. |
| Wildlife sensitivity is explicit | Public habitat context must not be transformed into current wildlife concentrations, refuge-use hotspots, sensitive-species occurrences, or live targeting guidance. |
| Access currentness is explicit | Seasonal or dated access/closure material must not be represented as current field permission without fresh, governed support. |
| Source roles do not collapse | KDWP, county, KDA/DWR, USGS, KDHE, KGS, agricultural, or other sources retain their distinct authority and limitations. |
| Property and flood conclusions are bounded | Parcel, BFE, NFIP, insurance, permit, boundary, or legal outcomes are outside this first documentation slice. |
| Water-quality conclusions are bounded | Regulatory or historical water-quality material must not be elevated into current ecological-health, human-safety, or liability conclusions. |
| Operational minimization | Public context should avoid unnecessary wetland-control, refuge-operation, or fine management detail unless a governed need is established. |
| Public clients stay downstream of trust | UI, map, search, and AI surfaces consume governed/released evidence rather than canonical or working stores. |
| Correction and rollback remain visible | Future access, sensitivity, geometry, regulatory, or source corrections must be able to supersede or withdraw affected public products without rewriting history. |

## Finite outcomes

For this county lane, the expected public-facing outcome vocabulary is:

- `ANSWER` — released evidence is in scope, current enough, sensitivity-safe, policy-safe, and citation-valid;
- `ABSTAIN` — evidence, currentness, safe scale, sensitivity, scope, or release closure is insufficient;
- `DENY` — the request would cross a wildlife-targeting, restricted-access, sensitive-habitat, property/legal, flood/safety, rights, or other protected boundary;
- `ERROR` — a resolver, validator, policy engine, source adapter, or runtime dependency failed.

These outcomes are a **design contract**, not proof that the current repository implements them for Neosho County.

## Source-role posture

The build plan discusses several source families, each with a different role. Their presence in planning material does **not** establish admission or public-release authority.

| Source family | Intended role | Must not be treated as |
|---|---|---|
| Kansas Department of Wildlife and Parks | Broad wildlife-area, habitat-purpose, and official access/closure context | Live wildlife-location authority, hunting optimizer, or permission for sensitive occurrence exposure |
| Neosho County | County administration, GIS, parcel, and floodplain context | Survey, legal boundary, valuation, insurance, permit, or property truth for the first slice |
| Kansas DWR / floodplain sources | Floodplain and mapping context where current and fit | Parcel-level BFE, insurance, permit, or emergency guidance |
| U.S. Geological Survey | Observation/source routing for the Neosho River and related hydrologic context | A substitute for flood, access, health, release, or regulatory decisions |
| Kansas Department of Health and Environment | Regulatory and water-quality context where current and admissible | Automatic current ecological-health, human-safety, or liability determination |
| Kansas Geological Survey | Geology and geologic-context evidence when fit for use | Wildlife, flood, access, water-quality, or agricultural authority |
| Agricultural sources | County-scale agricultural context where admitted and fit | Parcel-level causation, pollution assignment, or property conclusion |

## Repository and placement posture

**CONFIRMED:** this README already exists at `docs/focus-mode/counties/neosho_county/README.md`, so this change keeps the tracked path rather than inventing a new documentation home.

**CONFIRMED:** ADR-0029 is accepted and adopts the exact Directory Rules v2 bytes at `docs/doctrine/directory-rules.md` as the single writable human Directory Rules authority. This same-path documentation edit does not require or imply a county-lane migration.

**NEEDS VERIFICATION:** the long-term singular/plural and underscore/kebab-case Focus Mode naming model remains a separate repository-governance and compatibility question. This README does not create a parallel county authority surface or perform structural migration.

## Relationship to the build plan

The detailed planning artifact is:

- [Neosho County Focus Mode Build Plan](./neosho_county_focus_mode_build_plan.md)

Use the build plan for proposed layers, fixtures, source seeds, risk analysis, implementation phases, and verification questions. Use this README for the stable county-boundary summary and truth posture.

> [!CAUTION]
> The build plan includes point-in-time and source-derived statements from its authoring run. Before any implementation or public use, reverify current facts, source terms, identifiers, rights, sensitivity, access status, regulatory currentness, and release fitness against authoritative sources and current repository controls.

## Validation expectations for future implementation

A future Neosho County implementation should not be considered complete merely because Markdown exists. At minimum, the changed area should eventually prove:

1. safe-scale handling for Neosho Wildlife Area and refuge/wetland geometry;
2. current/stale access and closure handling with explicit retrieval and validity time;
3. positive and negative fixtures for `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` behavior;
4. no-network deterministic tests for the habitat/access trust boundary;
5. EvidenceRef-to-EvidenceBundle closure for consequential claims;
6. source-role, rights, sensitivity, and public-safe policy checks;
7. governed API/UI behavior with visible negative states;
8. correction, supersession, and rollback behavior;
9. no direct path from raw source, candidate wildlife data, or model output to public truth;
10. release evidence appropriate to the significance of any access, habitat, floodplain, or water-quality claim.

## Known unknowns

The following remain **UNKNOWN** or **NEEDS VERIFICATION** until current implementation evidence proves otherwise:

- which Neosho County source descriptors are admitted;
- live source rights and derivative-display permissions;
- safe public geometry/generalization thresholds;
- current KDWP access, closure, and management-status handling;
- current floodplain/effective-map state and admissible public use;
- current KDHE regulatory status and release fitness;
- exact contracts, schemas, policies, validators, fixtures, and tests for this county;
- governed API routes and UI components;
- named reviewer/steward assignments;
- correction propagation through map, search, cache, export, and AI surfaces;
- any deployed or published Neosho County Focus Mode.

## Rollback and correction

This README is documentation-only. Before merge, rollback is abandonment of the feature branch or pull request. After merge, correction should use a transparent revert or forward-fix PR against the actual merged commit.

A documentation rollback does **not** reverse any separate future source admission, policy decision, release manifest, deployment, publication, or public correction. Those transitions require their own governed records and rollback paths.

---

**Related:** [Neosho County Focus Mode Build Plan](./neosho_county_focus_mode_build_plan.md) · [County index](../COUNTY_INDEX.md)
