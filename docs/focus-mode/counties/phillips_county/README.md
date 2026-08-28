<!-- KFM_META_BLOCK_V2

document_id: kfm://docs/focus-mode/counties/phillips-county

title: Phillips County Focus Mode

type: county-focus-mode-readme

status: draft

truth_posture: cite-or-abstain

repository_path: docs/focus-mode/counties/phillips_county/README.md

related:
  - ./phillips_county_focus_mode_build_plan.md

notes:
  - Same-path modernization of an existing tracked README.
  - This document summarizes the repository-grounded county boundary; it does not claim source admission, implementation, review, release, deployment, or publication.
-->

<a id="top"></a>

# Phillips County Focus Mode

> **Purpose.** Define the public-safe documentation boundary for Phillips County, Kansas, and point maintainers to the county build plan without turning proposed refuge, reservoir, cultural-landscape, source, runtime, or release work into current implementation claims.

> [!IMPORTANT]
> This README is a **documentation boundary**, not a live county product. The sibling build plan contains proposed architecture and dated source-derived planning material. Current repository evidence, accepted governance, admitted evidence, policy, review, and release state outrank planning prose.

## Status at a glance

| Area | Status | Boundary |
|---|---|---|
| County scope | `CONFIRMED` | This lane concerns Phillips County, Kansas. |
| Existing README role | `CONFIRMED` | This file is the tracked county README at the current repository path. |
| Sibling build plan | `CONFIRMED` | `phillips_county_focus_mode_build_plan.md` exists beside this README. |
| County proof slice | `PROPOSED` | The build plan centers a Kirwin refuge / reservoir / North Fork Solomon River trust proof. |
| Source admission | `UNKNOWN` | No source is treated as admitted merely because the build plan cites or discusses it. |
| Runtime/API/UI behavior | `UNKNOWN` | This README does not claim implemented county routes, contracts, schemas, MapLibre layers, Evidence Drawer behavior, or Focus Mode execution. |
| Release/publication | `UNKNOWN` | A commit, PR, rendered map, or document is not governed publication. |

## County boundary

The Phillips County plan proposes a county experience organized around **Kirwin National Wildlife Refuge, Kirwin Reservoir, the North Fork Solomon River, prairie-transition ecology, Pawnee cultural-landscape responsibility, water-management context, and county-scale agriculture**.

Its central trust problem is that useful public education about a refuge and reservoir can easily become unsafe or misleading when exact wildlife detail, culturally sensitive places, operational water/access status, or stale rules are treated as durable public truth.

The county lane therefore needs to keep several authority classes distinct:

- refuge-management and public-use authority;
- cultural/Nation-authoritative evidence and review;
- reservoir and irrigation/flood-control context;
- river observations and hydrologic context;
- historic/scientific geology or water interpretation;
- agricultural aggregates;
- public-safe runtime interpretation.

## Proposed first proof slice

The sibling plan proposes a **Kirwin Refuge, Reservoir Operations, North Fork Solomon River, and Migratory-Bird Protection Proof Slice**. In bounded form, that slice would demonstrate that KFM can:

- explain Kirwin refuge and reservoir purpose without exposing sensitive wildlife-use locations;
- preserve refuge-management, reservoir-operations, water-administration, cultural, scientific, and agricultural source roles;
- treat current refuge closures, hunting/fishing rules, boating access, ramp usability, and water levels as time-sensitive official-authority information;
- generalize or withhold exact sensitive species or cultural-resource detail;
- require Nation-authoritative evidence and appropriate review for Pawnee cultural-landscape representation;
- surface visible negative states when evidence, freshness, rights, geometry, sensitivity, review, or release closure is missing;
- avoid converting reservoir or irrigation context into legal, safety, water-allocation, or access determinations.

These are **PROPOSED** behaviors until implementation, validation, evidence closure, policy review, and release state are verified.

## Public-safe rules

| Rule | Required behavior |
|---|---|
| Evidence before interpretation | Consequential claims resolve through governed evidence; generated language never substitutes for evidence. |
| Cite or abstain | Missing, stale, over-precise, or unresolved support must narrow the answer or return a finite negative state. |
| Wildlife sensitivity fails closed | Exact or inference-enabling bird, nesting, roosting, refuge-use, or sensitive occurrence locations must be withheld or generalized. |
| Cultural sovereignty is explicit | Pawnee cultural-landscape representation requires Nation-authoritative evidence and appropriate review; precise sensitive cultural places remain protected. |
| Current access is not durable prose | Closures, hunting/fishing rules, boating restrictions, ramps, and water-level-dependent access require current official authority. |
| Reservoir operations stay bounded | Public context must not become operational guidance, flood-safety advice, or water-allocation/legal conclusions. |
| Source roles do not collapse | USFWS, Pawnee Nation, USBR, USGS, KGS, agricultural, county, and other sources retain their distinct authority and limitations. |
| Public clients stay downstream of trust | UI, map, search, and AI surfaces consume governed/released evidence rather than canonical or working stores. |
| Historic science is labeled by time | Older KGS or similar scientific material may support historical context only when its age and limitations are visible. |
| Correction and rollback remain visible | Future access, wildlife, cultural, water, or interpretation corrections must supersede or withdraw affected public products without rewriting history. |

## Finite outcomes

For this county lane, the expected public-facing outcome vocabulary is:

- `ANSWER` — released evidence is in scope, current enough, sensitivity-safe, policy-safe, and citation-valid;
- `ABSTAIN` — evidence, freshness, authority, geometry, review, or release closure is insufficient;
- `DENY` — the request would cross a wildlife-sensitivity, cultural-sovereignty, operational, legal/safety, rights, or other protected boundary;
- `ERROR` — a resolver, validator, policy engine, source adapter, or runtime dependency failed.

These outcomes are a **design contract**, not proof that the current repository implements them for Phillips County.

## Source-role posture

The build plan discusses several source families, each with a different role. Their presence in planning material does **not** establish admission, rights clearance, or public-release authority.

| Source family | Intended role | Must not be treated as |
|---|---|---|
| U.S. Fish and Wildlife Service | Refuge purpose, habitat/public-use management, broad closure/rule context | License to expose precise sensitive wildlife locations or stale access status |
| Pawnee Nation / Nation-authoritative sources | Cultural-landscape authority and review basis | Generic historical color that can be replaced by outside interpretation |
| U.S. Bureau of Reclamation | Reservoir, irrigation, and flood-control project context | KFM-issued legal water allocation, flood-safety, or operational guidance |
| U.S. Geological Survey | River observations and hydrologic/scientific context | Refuge, cultural, legal, release, or public-safety authority |
| Kansas Geological Survey | Historic/scientific interpretation where fit and time-bounded | Current operational or regulatory authority |
| Agricultural sources | County-scale agricultural context where admitted and fit | Farm-, operator-, parcel-, or irrigation-compliance profiling |
| County/local sources | Public administration and routing context | Automatic proof of current access, safety, property, or legal status |

## Repository and placement posture

**CONFIRMED:** this README already exists at `docs/focus-mode/counties/phillips_county/README.md`, so this change keeps the tracked path rather than creating a new documentation authority surface.

**CONFIRMED:** ADR-0029 is accepted and adopts the exact Directory Rules v2 bytes at `docs/doctrine/directory-rules.md` as the single writable human-readable Directory Rules authority.

**NEEDS VERIFICATION:** long-term county-lane naming and migration remain separate governance work. This README does not create a parallel plural/kebab-case lane or migrate the sibling build plan.

## Relationship to the build plan

The detailed planning artifact is:

- [Phillips County Focus Mode Build Plan](./phillips_county_focus_mode_build_plan.md)

Use the build plan for proposed layers, source seeds, fixtures, object families, risk analysis, implementation phases, and verification questions. Use this README for the stable county-boundary summary and truth posture.

> [!CAUTION]
> The build plan includes point-in-time and source-derived statements from its authoring run. Before implementation or public use, reverify current rules, source terms, rights, geometry, wildlife sensitivity, cultural-review requirements, reservoir/access currentness, and release fitness against authoritative sources and current repository controls.

## Validation expectations for future implementation

A future Phillips County implementation should not be considered complete merely because Markdown exists. At minimum, the changed area should eventually prove:

1. sensitive-wildlife geometry generalization or denial behavior;
2. Pawnee cultural-authority/review gating for consequential cultural claims;
3. stale/current closure and access handling with explicit retrieval/validity time;
4. source-role separation across refuge, reservoir, river, cultural, geology, and agriculture lanes;
5. positive and negative fixtures for `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` behavior;
6. no-network deterministic tests for the first trust-boundary slice;
7. EvidenceRef-to-EvidenceBundle closure for consequential claims;
8. rights, sensitivity, public-safe geometry, policy, review, and release checks;
9. governed API/UI behavior with visible negative states;
10. correction, supersession, withdrawal, and rollback behavior.

## Known unknowns

The following remain **UNKNOWN** or **NEEDS VERIFICATION** until current implementation evidence proves otherwise:

- which Phillips County source descriptors are admitted;
- authoritative geometry and public-safe scale for refuge/wildlife/cultural features;
- current source rights and derivative-display permissions;
- current refuge closures, access rules, water levels, boating restrictions, and hunting/fishing conditions;
- accountable Pawnee/Nation-authoritative review path and reviewer assignments;
- exact contracts, schemas, policies, validators, fixtures, and tests for this county;
- governed API routes and UI components;
- correction propagation through map, search, cache, export, and AI surfaces;
- any deployed or published Phillips County Focus Mode.

## Rollback and correction

This README is documentation-only. Before merge, rollback is abandonment of the feature branch or pull request. After merge, correction should use a transparent revert or forward-fix PR against the actual merged commit.

A documentation rollback does **not** reverse any separate future source admission, cultural-review decision, policy decision, release manifest, deployment, publication, or public correction. Those transitions require their own governed records and rollback paths.

---

**Related:** [Phillips County Focus Mode Build Plan](./phillips_county_focus_mode_build_plan.md) · [County index](../COUNTY_INDEX.md)
