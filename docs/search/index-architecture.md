<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<NEEDS_VERIFICATION_UUID>
title: Search Index Architecture
type: standard
version: v1
status: draft
owners: <NEEDS_VERIFICATION>
created: <NEEDS_VERIFICATION_DATE>
updated: <NEEDS_VERIFICATION_DATE>
policy_label: <NEEDS_VERIFICATION>
related: [<NEEDS_VERIFICATION>]
tags: [kfm, search, architecture]
notes: [Target path docs/search/index-architecture.md; repo tree not directly mounted in current session; placeholders retained pending repo verification.]
[/KFM_META_BLOCK_V2] -->

# Search Index Architecture

Release-backed, evidence-constrained search for KFM’s governed spatial evidence system.

> [!IMPORTANT]
> This document treats the search index as a **derived, rebuildable delivery surface**, never as canonical truth. Exact repo topology, worker names, endpoint names, schemas, and deployment shape remain **UNKNOWN** until the mounted repository is directly inspected.

**Quick jump:** [Purpose](#purpose) · [Authority boundary](#authority-boundary) · [Five-plane placement](#search-in-the-five-plane-model) · [Logical search surfaces](#logical-search-surfaces) · [Build lifecycle](#build-lifecycle) · [Contracts](#contracts-and-proof-objects) · [Runtime flow](#runtime-flow) · [Review gates](#minimum-review-gates) · [Open verification](#open-verification-items)

| Field | Value |
|---|---|
| Target path | `docs/search/index-architecture.md` |
| Document role | Search-layer architecture note |
| Current posture | **CONFIRMED** doctrine · **INFERRED** structural completion · **PROPOSED** starter shape · **UNKNOWN** mounted implementation |
| Primary concern | Make search useful without letting it become sovereign truth |
| Main consumers | Builders, stewards, reviewers, API designers, search/ranking implementers |

## Purpose

This document defines how search should behave inside KFM’s architecture.

It does **not** define search as a standalone product, a parallel truth store, or a convenience-first indexing layer. In KFM, search exists to support discovery, navigation, retrieval acceleration, and evidence-aware runtime behavior while remaining downstream of governed publication, policy, review, release state, and correction lineage.

A KFM search hit is therefore a **navigation and retrieval aid**. It is not proof by itself.

### In scope

| Included here | Why it belongs here |
|---|---|
| Release-backed discovery | Search must operate over promoted scope, not arbitrary internal state |
| Full-text / metadata search | Core public and steward-facing discovery behavior |
| Retrieval acceleration | Search may assist dossier, story, and Focus flows |
| Freshness, rebuild, and correction | Search must stay tied to release and correction state |
| Proof objects and runtime accountability | Search results must remain explainable under dispute or failure |

### Out of scope

| Excluded here | Why it is excluded |
|---|---|
| Source onboarding mechanics | Covered upstream by source and intake architecture |
| Canonical storage design in full | Covered by canonical data architecture |
| Free-form assistant UX | Covered by bounded AI / Focus architecture |
| Exact engine choice | **UNKNOWN** in the mounted repo; doctrine constrains role more than product choice |
| Search ranking experimentation in isolation | Must remain subordinate to evidence, policy, and release rules |

## Authority boundary

This page is doctrine-led and intentionally conservative about implementation claims.

| Boundary | Status | Notes |
|---|---|---|
| KFM doctrine about truth path, trust membrane, authoritative-vs-derived separation, and governed runtime | **CONFIRMED** | Strongly established across March 2026 KFM manuals |
| Search index as a derived / rebuildable layer | **CONFIRMED** | Repeated across central KFM architecture documents |
| Exact contents of `docs/search/` | **UNKNOWN** | Repo tree not directly mounted in this session |
| Existing search workers, route tree, schema files, CI jobs, and manifests | **UNKNOWN** | Not directly verified from mounted repo artifacts |
| Top-level documentary repo surfaces like `contracts/`, `schemas/`, `policy/README.md`, `tests/README.md`, and workflow/readme scaffolding | **CONFIRMED** via secondary repo-grounded evidence | Useful context, but not a substitute for direct repo inspection |

> [!NOTE]
> Where this document proposes structure, it does so as the **smallest plausible completion** of KFM’s doctrine, not as a claim that the repo already implements it.

## Search in the five-plane model

KFM’s search architecture only makes sense when placed inside the broader dependency order.

```mermaid
flowchart LR
    A[Source & intake<br/>descriptors, raw captures,<br/>validation, quarantine] --> B[Canonical truth<br/>DatasetVersion-backed<br/>facts and features]
    B --> C[Catalog / policy / review<br/>CatalogClosure, DecisionEnvelope,<br/>ReviewRecord, ReleaseManifest]
    C --> D[Projection & packaging workers]
    D --> E[Search index<br/>derived / rebuildable]
    D --> F[Vector / embedding index<br/>derived / rebuildable]
    E --> G[Governed API / evidence resolver]
    F --> G
    G --> H[Map shell]
    G --> I[Dossier / story]
    G --> J[Focus]
    G --> K[Export / review surfaces]
```

### Placement rule

The search index belongs in the **derived delivery** part of the system.

That has four consequences:

1. It is built **from promoted scope**, not from raw or unpublished materials on the public path.
2. It is written by **projection / packaging workers**, not by UI clients or runtime shells.
3. It remains **rebuildable by default**.
4. It must never become the only place where meaning survives.

## What search is allowed to do

| Allowed role | Posture |
|---|---|
| Discover release-backed objects | Required |
| Accelerate retrieval for dossier, story, export, and Focus | Allowed |
| Rank or filter candidates for bounded assistance | Allowed |
| Provide snippets or previews | Allowed, but previews are not final authority |
| Carry freshness and release linkage | Required |
| Surface generalized or policy-shaped representations where necessary | Required |
| Resolve to evidence-bearing or release-backed objects | Required |

## What search must never do

| Forbidden role | Why it is disallowed |
|---|---|
| Act as canonical truth | Violates authoritative-vs-derived separation |
| Bypass governed APIs | Breaks the trust membrane |
| Read from RAW / WORK / QUARANTINE directly on the public path | Violates publication discipline |
| Return uncited prose as if the hit itself were evidence | Breaks evidence-linked public claims |
| Become the only surviving representation of meaning | Violates rebuildability and auditability |
| Silently outrank release, policy, or correction state | Undermines governed publication |

## Logical search surfaces

The corpus strongly supports search as a family of derived discovery and retrieval surfaces, but not every slice is equally confirmed. The table below separates what is doctrinally firm from what remains a starter pattern.

| Surface | Status | Primary role | Truth status | Must resolve to |
|---|---|---|---|---|
| Catalog search | **CONFIRMED** | Discover release-backed outward objects | Derived | `CatalogClosure` + release-linked outward metadata |
| Evidence text search | **INFERRED** | Find released evidence packages, excerpts, and inspectable support | Derived | `EvidenceBundle` or release-backed evidence object |
| Vector / embedding retrieval | **CONFIRMED** doctrine for derived vector/embedding stores; **PROPOSED** as a distinct search slice here | Accelerate semantic retrieval for bounded assistance | Derived | `EvidenceBundle`, citation checks, release refs |
| Steward review search | **PROPOSED** | Help reviewers compare generalized vs precise, active vs withdrawn, prior vs superseding releases | Derived / review-bearing | `DecisionEnvelope`, `ReviewRecord`, `CorrectionNotice` context |
| UI-local query state | **INFERRED** | Remember search text, filters, sort, pane state | Ephemeral | UI state only; never truth-bearing |

### Reading rule

A **search result row** is not the trust object.

The trust object is the governed thing the row resolves to: a release-backed object, an `EvidenceBundle`, a `CatalogClosure`, or a runtime envelope with audit linkage.

## Search-serving KFM surfaces

Search should serve KFM’s map-first shell rather than pull the product into a search-first posture.

| Surface | Search should help by… | Search must not do… |
|---|---|---|
| Map | Finding places, features, districts, service areas, and released thematic layers | Certifying truth by map jump alone |
| Dossier | Surfacing release-backed facts, evidence excerpts, and related records | Flattening evidence into detached snippets |
| Story | Finding reusable release-backed narrative materials | Stripping context from archival or oral-history material |
| Focus | Accelerating bounded retrieval before synthesis | Becoming a free-form answer path |
| Review | Comparing surface states, release lineage, and correction effects | Acting as a hidden admin bypass |

```mermaid
sequenceDiagram
    participant U as User / steward
    participant API as Governed API
    participant P as Policy checks
    participant SI as Search index
    participant ER as Evidence resolver
    participant RT as Runtime envelope
    participant UI as KFM surface

    U->>API: search or Focus request
    API->>P: precheck scope, role, surface
    P-->>API: allowed / narrowed / denied
    API->>SI: query promoted search surface
    SI-->>API: ranked candidates + release refs
    API->>ER: resolve candidates to evidence-bearing objects
    ER-->>API: EvidenceBundle / release-backed refs
    API->>P: postcheck obligations, sensitivity, correction state
    P-->>API: final constraints
    API->>RT: emit accountable result envelope
    RT-->>UI: result + state + audit linkage
```

## Engine selection boundary

This document deliberately avoids pretending that doctrine already proves a particular engine.

| Decision area | Current status | Guidance |
|---|---|---|
| Exact search engine | **UNKNOWN** | Verify before documenting product-specific behavior |
| Single index vs multiple indexes | **INFERRED / PROPOSED** | Decompose by role only if proofs, freshness, and rebuild paths stay clear |
| Metadata + full-text + semantic retrieval split | **PROPOSED** | Useful only when each slice remains derived and release-backed |
| Direct database-only search | **UNKNOWN** | May be viable, but must still honor derived status and governed runtime |
| External search service | **UNKNOWN** | Acceptable only if it preserves trust membrane, release linkage, and rebuildability |

> [!CAUTION]
> Search technology is a secondary decision. KFM doctrine constrains **authority**, **freshness**, **correction**, **proof**, and **access path** before it constrains product selection.

## Build lifecycle

A search index should be built and maintained as a release-scoped projection.

1. **Canonical and control-plane prerequisites close.**  
   Eligible inputs are promoted `DatasetVersion` objects and the required catalog / policy / review artifacts for the release scope.

2. **Projection workers build the index.**  
   Search build logic runs downstream of release, not as a side effect of browsing or authoring.

3. **A proof object is emitted.**  
   The build should produce a `ProjectionBuildReceipt` or equivalent proof object describing source release, projection class, build time, freshness basis, and stale-after policy.

4. **Governed API exposure begins.**  
   Public and steward clients read search only through governed interfaces.

5. **Runtime resolution reconstructs trust.**  
   Search candidates are resolved to release-backed objects or `EvidenceBundle` references before consequential outward use.

6. **Correction propagates forward.**  
   Supersession, withdrawal, narrowing, or replacement must trigger stale marking, rebuild, or withdrawal of derived search artifacts.

## Contracts and proof objects

Search architecture is thin without explicit object families.

| Object family | Why search cares |
|---|---|
| `DatasetVersion` | Defines the authoritative subject set that search may project from |
| `CatalogClosure` | Anchors outward discovery metadata and release linkage |
| `DecisionEnvelope` | Carries machine-readable policy results that may narrow or block search exposure |
| `ReviewRecord` | Matters where steward or policy-significant review is required |
| `ReleaseManifest` / `ReleaseProofPack` | Defines the releasable scope and rollback/correction posture |
| `ProjectionBuildReceipt` | Proves the search projection was built from known release scope |
| `EvidenceBundle` | Packages support for a hit preview, dossier claim, export, or Focus retrieval |
| `RuntimeResponseEnvelope` | Makes runtime search / Focus outcomes accountable |
| `CorrectionNotice` | Preserves lineage when releases or search-facing meanings change |

### Minimum search-facing contract expectations

| Concern | Minimum expectation |
|---|---|
| Release linkage | Every indexable object must point back to release-backed authority |
| Surface class | Public, steward, review, export, or Focus use must be explicit |
| Freshness basis | Search must declare when the projection was built and when it becomes stale |
| Correction linkage | Superseded or withdrawn material must remain traceable |
| Rights / sensitivity | Searchable representation must reflect allowed precision and exposure rules |
| Auditability | Runtime search and Focus paths should emit accountable runtime objects |

## Freshness, rebuild, and correction

Search is only trustworthy when its staleness model is explicit.

| Requirement | Why it matters |
|---|---|
| Build time recorded | Explains what the index actually reflects |
| Freshness basis declared | Prevents silent drift |
| `stale-after` or equivalent policy present | Enables visible stale handling |
| Rebuild trigger linked to release/correction events | Keeps search aligned with published scope |
| Superseded content remains explainable | Preserves lineage instead of erasing history |
| Public-safe narrowing supported | Lets search degrade safely rather than lie |

### Surface behavior under change

| State | Meaning |
|---|---|
| Ready / promoted | Search projection matches a released scope |
| Partial | Coverage is intentionally incomplete and must be labeled |
| Stale-visible | Search is still readable but outside its declared freshness basis |
| Withdrawn | Searchable representation must no longer be served on that surface |
| Denied | Policy blocks the requested action or scope |
| Rebuilding | **INFERRED / PROPOSED** operator-visible state during correction or refresh |

## Security, policy, and trust-visible behavior

Search is part of KFM’s trust system, not just a convenience layer.

| Rule | Architectural consequence |
|---|---|
| Governed API only | No direct browser-to-index trust path |
| Public-safe scope only | Public search must not expose unpublished or unsafe candidates |
| Rights and sensitivity first | Searchable snippets, previews, and highlights may need generalization or withholding |
| No exact-location bluffing | Search must not imply parcel-grade certainty when source support is coarser |
| No silent model escalation | Semantic retrieval may assist, but it does not authorize synthesis by itself |
| No hidden correction state | Search must reflect supersession, withdrawal, or narrowing visibly |

## Minimum review gates

A search layer should not be considered done merely because queries return fast.

- [ ] Derived / rebuildable status is explicit in docs and architecture notes
- [ ] Search build inputs are restricted to promoted release scope
- [ ] `ProjectionBuildReceipt` or equivalent proof object exists
- [ ] Freshness basis and stale policy are declared
- [ ] Correction-triggered rebuild or withdrawal path is documented
- [ ] Search results drill through to release-backed objects or `EvidenceBundle` support
- [ ] Focus retrieval path is citation-checked and runtime-accountable
- [ ] Policy shaping of snippets, previews, and exact-location behavior is tested
- [ ] No direct frontend, shell, or model-runtime bypass around the governed API
- [ ] Negative-path behavior is visible and reviewable

## Open verification items

The following items remain intentionally visible because the mounted repo was not directly inspected in this session.

| Item | Why it matters | Current status |
|---|---|---|
| Exact neighboring docs under `docs/search/` | Needed for native repo fit and local cross-linking | **UNKNOWN** |
| Existing search implementation, if any | Prevents rewriting around phantom or duplicate structures | **UNKNOWN** |
| Actual engine choice(s) | Needed before documenting operational specifics | **UNKNOWN** |
| Existing schema files for projection / runtime search objects | Needed for contract-accurate documentation | **UNKNOWN** |
| Existing tests and fixtures | Needed before claiming verification depth | **UNKNOWN** |
| Active CI jobs for search rebuild / validation | Needed before documenting automation | **UNKNOWN** |
| Freshness thresholds per search surface | Needed for truthful stale-state language | **UNKNOWN** |
| Review-only vs public-safe search behavior in mounted code | Needed for accurate policy surface documentation | **UNKNOWN** |

## Non-goals

- Not a search-first authority engine.
- Not a free-form answer source.
- Not a detached admin bypass around governed APIs.
- Not a substitute for `CatalogClosure`, `EvidenceBundle`, or runtime accountability.
- Not a place where tiles, vectors, embeddings, graph projections, or snippets quietly become truth.

## Illustrative starter decomposition

<details>
<summary>Open a small starter topology (INFERRED / PROPOSED)</summary>

```text
promoted release scope
        │
        ├── catalog search projection
        │     └── outward discovery, release cards, filters
        │
        ├── evidence text projection
        │     └── released excerpts, dossier/story support
        │
        ├── vector / embedding projection
        │     └── semantic retrieval acceleration only
        │
        └── governed API
              ├── public search
              ├── steward review search
              └── Focus retrieval handoff
```

Use this only as a logical decomposition. The mounted repo may implement these concerns differently.

</details>

## Working summary

Search in KFM should be boring in exactly the right way:

- downstream of release,
- explicit about freshness,
- unable to outrank authority,
- forced through governed APIs,
- correction-aware,
- and always capable of resolving a useful hit into an inspectable, release-backed object.

[Back to top](#search-index-architecture)
