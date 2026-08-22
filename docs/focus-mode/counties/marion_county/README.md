<!-- KFM_META_BLOCK_V2

document_id: kfm://docs/focus-mode/counties/marion-county

title: Marion County Focus Mode

type: county-focus-mode-readme

status: draft

truth_posture: cite-or-abstain

repository_path: docs/focus-mode/counties/marion_county/README.md

related:
  - ./marion_county_focus_mode_build_plan.md

notes:
  - Same-path modernization of an existing tracked README.
  - This document summarizes the repository-grounded county boundary; it does not claim source admission, implementation, release, deployment, or publication.
-->

<a id="top"></a>

# Marion County Focus Mode

> **Purpose.** Define the public-safe documentation boundary for Marion County, Kansas, and point maintainers to the county build plan without presenting proposed source, runtime, release, or publication work as current implementation.

> [!IMPORTANT]
> This README is a **documentation boundary**, not a live county product. The sibling build plan contains proposed architecture and source-derived planning material; it remains subordinate to current repository evidence, accepted governance, admitted evidence, policy, review, and release state.

## Status at a glance

| Area | Status | Boundary |
|---|---|---|
| County scope | `CONFIRMED` | This lane concerns Marion County, Kansas. |
| Existing README role | `CONFIRMED` | This file is the tracked county README at the current repository path. |
| Sibling build plan | `CONFIRMED` | `marion_county_focus_mode_build_plan.md` exists beside this README. |
| County proof slice | `PROPOSED` | The build plan centers a Marion Reservoir advisory-currentness and waterbody-identity trust proof. |
| Source admission | `UNKNOWN` | No source is treated as admitted merely because the build plan cites or discusses it. |
| Runtime/API/UI behavior | `UNKNOWN` | This README does not claim implemented county routes, contracts, schemas, MapLibre layers, Evidence Drawer behavior, or Focus Mode execution. |
| Release/publication | `UNKNOWN` | A commit, PR, rendered map, or document is not governed publication. |

## County boundary

The Marion County plan proposes a county experience organized around **Marion Reservoir, Marion County Lake, the Cottonwood River landscape, water-quality/currentness discipline, geology, and county-scale agriculture**. Its key trust problem is not simply displaying water features; it is preserving identity, source role, time, and public-health boundaries while keeping advisory and operational claims fail-closed.

The most important coupled identity rule is:

> **Marion Reservoir is not Marion County Lake.**

Any future source, layer, evidence object, advisory record, or AI answer that uses an ambiguous name such as “Marion Lake” must resolve the intended waterbody before presenting a consequential claim. Ambiguity should produce `ABSTAIN`, `DENY`, or another governed finite outcome rather than a guessed join.

## Proposed first proof slice

The sibling plan proposes a **Marion Reservoir Advisory-Currentness Trust Boundary Proof**. In bounded form, that slice would demonstrate that KFM can:

- present static, source-attributed reservoir context without turning it into a live safety verdict;
- keep Marion Reservoir and Marion County Lake deterministically distinct;
- route users toward the current official advisory authority rather than copying time-sensitive status into durable prose;
- preserve the distinction between reservoir-purpose/history evidence, public-health advisories, stream observations, geology, county mapping, and agricultural statistics;
- expose visible negative states when freshness, identity, rights, review, or release closure is missing;
- avoid unnecessary operational detail about dam/outlet/release infrastructure in the first public-safe product.

These are **PROPOSED** behaviors until implementation, validation, evidence closure, policy review, and release state are verified.

## Public-safe rules

The Marion County lane should preserve the following boundaries from the build plan and KFM doctrine:

| Rule | Required behavior |
|---|---|
| Evidence before interpretation | Consequential claims resolve through governed evidence; generated language never substitutes for evidence. |
| Cite or abstain | Missing or stale support must narrow the answer or return a finite negative state. |
| Currentness is explicit | A historical or point-in-time water-quality/advisory record must not be rendered as a current health status. |
| Waterbody identity is deterministic | Records for Marion Reservoir and Marion County Lake must not be merged by name similarity alone. |
| Source roles do not collapse | USACE, KDHE, USGS, KGS, county, agricultural, or other sources retain their distinct authority and limitations. |
| Health and safety are bounded | KFM must not independently declare water safe for swimming, drinking, fishing, pets, or exposure. |
| Property and legal conclusions are out of scope | County mapping or related material must not be elevated into parcel, valuation, permit, title, insurance, or legal determinations. |
| Operational minimization | Public context should avoid unnecessary dam, outlet, discharge, or live-operation detail unless a governed need is established. |
| Public clients stay downstream of trust | UI, map, search, and AI surfaces consume governed/released evidence rather than canonical or working stores. |
| Correction and rollback remain visible | Future advisory or identity corrections must be able to supersede or withdraw affected public products without rewriting history. |

## Finite outcomes

For this county lane, the expected public-facing outcome vocabulary is:

- `ANSWER` — released evidence is in scope, current enough, identity-resolved, policy-safe, and citation-valid;
- `ABSTAIN` — evidence, freshness, identity, scope, or release closure is insufficient;
- `DENY` — the request would cross a health/safety, sensitive operational, property/legal, rights, or other protected boundary;
- `ERROR` — a resolver, validator, policy engine, source adapter, or runtime dependency failed.

These outcomes are a **design contract**, not proof that the current repository implements them for Marion County.

## Source-role posture

The build plan discusses several source families, each with a different role. Their presence in planning material does **not** establish admission or public-release authority.

| Source family | Intended role | Must not be treated as |
|---|---|---|
| U.S. Army Corps of Engineers | Reservoir purpose, history, and bounded public project context | A general health authority or license for detailed operational exposure |
| Kansas Department of Health and Environment | Harmful-algal-bloom and water-quality/public-health context, including current advisory routing | A timeless safety statement copied into durable KFM prose |
| U.S. Geological Survey | Observation/source routing for the Cottonwood River and related hydrologic context | A substitute for health, release, or reservoir-management decisions |
| Kansas Geological Survey | Geology and geologic-context evidence when fit for use | Reservoir-health, advisory, or agricultural authority |
| Marion County | County administration and mapping context | Parcel, valuation, title, permit, insurance, or legal truth for the first slice |
| Agricultural sources | County-scale agricultural context where admitted and fit | Parcel-level causation or water-health conclusions |

## Repository and placement posture

**CONFIRMED:** this README already exists at `docs/focus-mode/counties/marion_county/README.md`, so this change keeps the tracked path rather than inventing a new documentation home.

**CONFIRMED:** the current repository `docs/doctrine/directory-rules.md` is a **proposed successor**, not yet effective by its own terms. It explicitly says adoption has no effect until accepted. Structural migration therefore remains separate from this same-path documentation update.

**NEEDS VERIFICATION:** the long-term singular/plural and underscore/kebab-case Focus Mode naming model remains a repository-governance question. This README does not use the proposed Directory Rules draft to authorize a move or create a parallel county authority surface.

## Relationship to the build plan

The detailed planning artifact is:

- [Marion County Focus Mode Build Plan](./marion_county_focus_mode_build_plan.md)

Use the build plan for proposed layers, fixtures, source seeds, risk analysis, implementation phases, and verification questions. Use this README for the stable county-boundary summary and truth posture.

> [!CAUTION]
> The build plan includes point-in-time and source-derived statements from its authoring run. Before any implementation or public use, reverify current facts, source terms, identifiers, rights, sensitivity, and release fitness against authoritative sources and current repository controls.

## Validation expectations for future implementation

A future Marion County implementation should not be considered complete merely because Markdown exists. At minimum, the changed area should eventually prove:

1. deterministic Marion Reservoir versus Marion County Lake identity;
2. stale/current advisory handling with explicit retrieval and validity time;
3. positive and negative fixtures for `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` behavior;
4. no-network deterministic tests for the trust boundary;
5. EvidenceRef-to-EvidenceBundle closure for consequential claims;
6. source-role, rights, sensitivity, and public-safe policy checks;
7. governed API/UI behavior with visible negative states;
8. correction, supersession, and rollback behavior;
9. no direct path from raw source or model output to public truth;
10. release evidence appropriate to the significance of any public advisory or health-related claim.

## Known unknowns

The following remain **UNKNOWN** or **NEEDS VERIFICATION** until current implementation evidence proves otherwise:

- which Marion County source descriptors are admitted;
- canonical waterbody identifiers and crosswalks used by KFM;
- live source rights and derivative-display permissions;
- exact contracts, schemas, policies, validators, fixtures, and tests for this county;
- governed API routes and UI components;
- current advisory freshness and release behavior;
- named reviewer/steward assignments;
- correction propagation through map, search, cache, export, and AI surfaces;
- any deployed or published Marion County Focus Mode.

## Rollback and correction

This README is documentation-only. Before merge, rollback is abandonment of the feature branch or pull request. After merge, correction should use a transparent revert or forward-fix PR against the actual merged commit.

A documentation rollback does **not** reverse any separate future source admission, policy decision, release manifest, deployment, publication, or public correction. Those transitions require their own governed records and rollback paths.

---

**Related:** [Marion County Focus Mode Build Plan](./marion_county_focus_mode_build_plan.md) · [County index](../COUNTY_INDEX.md)
