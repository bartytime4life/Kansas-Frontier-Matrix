<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-kansas-kdhe-harmful-algal-blooms
title: KDHE harmful-algal-bloom advisories
type: source-product-page; volatile-advisory-profile; documentation-only
version: v0.1.0
status: proposed documentation profile; identity conflict active; no source activation
owners: NEEDS VERIFICATION — Kansas source steward + Hydrology/Hazards + public-safety + correction/release stewards
created: 2026-07-25
updated: 2026-07-25
policy_label: public-review; volatile; safety-relevant; cite-or-abstain; fail-closed
current_path: docs/sources/catalog/kansas/kdhe-harmful-algal-blooms.md
truth_posture: >
  CONFIRMED official KDHE advisory levels, July 24 2026 table and press-release
  conflict, zoned-lake support, monitoring-season context, and closure-authority
  limitation / PROPOSED KFM identity, temporal, outcome, and fixture requirements /
  NEEDS VERIFICATION stable water-body identifiers, geometry authority, rights,
  source activation, connector behavior, evidence closure, review, release, and
  public delivery
evidence_snapshot:
  repository_base: 57c1a05b07b29793a5747a25b83594b6598df812
  source_table_updated: 2026-07-24
  source_press_release_published: 2026-07-24
  conflict_record: Kirwin Lake — Lyon County in table; Phillips County in press release
  bounded_exception: KFM-EXCEPTION-20260725-SOURCE-CATALOG-CORRECTION-001
related:
  - ./README.md
  - ./cross-source-condition-semantics.md
  - ../RIGHTS-AND-SENSITIVITY-MAP.md
  - ../../SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../data/registry/sources/
  - ../../../../policy/
  - ../../../../release/
tags: [kfm, kansas, kdhe, harmful-algal-bloom, hab, advisory, hydrology, hazards, identity-conflict, volatile-source]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KDHE harmful-algal-bloom advisories

> Documentation profile for Kansas Department of Health and Environment harmful-algal-bloom advisory surfaces. This page preserves volatile advisory state and official-source conflicts; it does not activate a connector, issue an alert, close a water body, or authorize publication.

[![Status: proposed](https://img.shields.io/badge/status-proposed-d4a72c?style=flat-square)](#status)
[![Conflict: active](https://img.shields.io/badge/identity%20conflict-active-b42318?style=flat-square)](#confirmed-july-24-2026-conflict)
[![Source activation: none](https://img.shields.io/badge/source%20activation-none-6e7781?style=flat-square)](#authority-boundary)
[![Public delivery: denied](https://img.shields.io/badge/public%20delivery-denied-b42318?style=flat-square)](#authority-boundary)

> [!WARNING]
> Two official KDHE surfaces published or updated on July 24, 2026 disagree about Kirwin Lake’s county. KFM must preserve both statements and emit `IDENTITY_CONFLICT`; it must not choose a county from name matching, convenience, or generated language.

> [!IMPORTANT]
> KDHE provides health-advisory recommendations and states that it does not have authority to close a lake. Closure, access, and local management decisions must remain separate authority records.

**Quick navigation:** [Status](#status) · [Sources](#official-source-surfaces) · [Conflict](#confirmed-july-24-2026-conflict) · [Authority](#authority-boundary) · [Model](#required-record-model) · [States](#finite-normalized-states) · [Freshness](#freshness-and-complete-snapshot-rules) · [Geometry](#water-body-identity-and-geometry) · [Fixtures](#required-no-network-fixtures) · [Release](#evidence-review-and-release-gates) · [Rollback](#correction-and-rollback)

## Status

| Field | Value |
|---|---|
| Documentation status | `proposed` |
| KFM source activation | None |
| Live connector or schedule | None |
| Current official-source conflict | `ACTIVE` |
| Conflict key | `Kirwin Lake / county` |
| Public-safe publication | Denied until identity, freshness, evidence, policy, review, release, correction, and rollback gates close |
| Current review | Pending |

## Official source surfaces

| Surface | Official locator | Snapshot role |
|---|---|---|
| Current advisories table and recommendations | `https://www.kdhe.ks.gov/777/Harmful-Algal-Blooms` | Volatile current-state table, advisory-level definitions, zoned-lake context, and authority limitation |
| July 24, 2026 press release | `https://www.kdhe.ks.gov/m/newsflash/home/detail/2059` | Dated announcement of additions, elevations, lowerings, and current advisory list |
| Response program | `https://www.kdhe.ks.gov/779/Response-Program` | Program and threshold context; verify exact version before use |

Each retrieval must preserve the exact locator, retrieval time, source-reported update/publication time, content digest, parse result, and source-surface type. A table and press release are separate artifacts even when they describe the same advisory cycle.

## Confirmed July 24, 2026 conflict

| Official surface | Native statement |
|---|---|
| Current advisories table | `Kirwin Lake` · `Lyon` · `Warning` |
| July 24 press release | `Kirwin Lake` · `Phillips County` · `Warning` · elevated July 24 |

Required KFM disposition:

```yaml
outcome: IDENTITY_CONFLICT
conflict_fields:
  - county
source_values:
  current_table: Lyon
  press_release: Phillips
advisory_level: Warning
public_geometry: null
publication_allowed: false
resolution_status: NEEDS_VERIFICATION
```

The record may later resolve through a stable water-body identifier and governed geometry authority. The conflict itself must remain in lineage after resolution.

## Authority boundary

KDHE defines three native advisory levels:

- `Watch`;
- `Warning`; and
- `Hazard`.

KFM must preserve the native level exactly. Normalized state is an additional field, not a replacement.

KDHE’s current page also states:

- monitoring generally coincides with the April 1–October 31 water-recreation season;
- advisories can remain active outside that season;
- some lakes have multiple management zones; and
- KDHE provides recommendations but does not itself have lake-closure authority.

Therefore:

- `Hazard` does not by itself prove that a local closure order was issued;
- a recommendation to close cannot be represented as a closure decision;
- a zone advisory cannot be generalized to an entire lake;
- a lake-manager action cannot be attributed to KDHE without its own evidence; and
- public guidance must link to current official instructions rather than paraphrasing them as KFM authority.

## Required record model

A future normalized advisory snapshot should preserve at minimum:

| Field | Requirement |
|---|---|
| `source_id` and `source_product_id` | Stable governed identities; inactive until reviewed |
| `source_surface_type` | `current_table`, `press_release`, `response_plan`, or another reviewed value |
| `source_locator` | Exact official locator |
| `source_updated_at` / `source_published_at` | Preserve source-native time and timezone evidence |
| `retrieved_at` | KFM retrieval time, separate from source time |
| `content_digest` | Digest of immutable captured bytes |
| `water_body_name_native` | Exact source spelling |
| `water_body_id` | Stable identifier or explicit unresolved state |
| `county_native` | Exact source value; do not overwrite conflicts |
| `advisory_level_native` | `Watch`, `Warning`, or `Hazard` |
| `scope_type` | `whole_water_body`, `zone`, `partial`, or `unresolved` |
| `zone_id` and `geometry_ref` | Required when scope is zoned or spatially bounded |
| `geometry_confidence` | Explicit, never inferred as certainty |
| `first_observed_at` / `last_observed_at` | KFM observation lineage |
| `supersedes_snapshot_id` | Link to prior snapshot when state changes |
| `recommendation_version_ref` | Digest or version reference for applicable official guidance |
| `closure_authority_ref` | Separate optional authority record; never implied |
| `evidence_refs` / `receipt_refs` | Resolvable governed references |
| `identity_resolution_status` | `RESOLVED`, `UNRESOLVED`, or `CONFLICT` |
| `freshness_status` | Current, stale, unavailable, or quarantined under reviewed budgets |

## Finite normalized states

Proposed normalization vocabulary:

- `WATCH`
- `WARNING`
- `HAZARD`
- `LIFTED`
- `NO_CURRENT_ADVISORY_CONFIRMED`
- `SOURCE_UNAVAILABLE`
- `STALE_SOURCE`
- `IDENTITY_UNRESOLVED`
- `IDENTITY_CONFLICT`
- `GEOMETRY_UNRESOLVED`
- `QUARANTINED`

These values require contract, schema, policy, fixture, and validator review before implementation.

`NO_CURRENT_ADVISORY_CONFIRMED` is allowed only when:

1. the expected official source surface was retrieved successfully;
2. the snapshot is complete and current under the accepted freshness budget;
3. parsing and integrity checks passed;
4. the prior advisory identity was resolved;
5. absence is evaluated against the complete snapshot rather than one failed row; and
6. supersession or lifting lineage is preserved.

## Freshness and complete-snapshot rules

A volatile safety-relevant source must fail closed.

- A failed retrieval cannot clear an active advisory.
- A missing row cannot become “no advisory” without a complete, current snapshot.
- A parse error, partial response, stale cache, or changed page shape becomes `SOURCE_UNAVAILABLE`, `STALE_SOURCE`, or `QUARANTINED`.
- Current-table and press-release snapshots retain separate digests and times.
- A later table update may supersede current-state preference but must not erase the earlier conflict or press-release lineage.
- Public clients must receive source vintage and stale-state behavior when publication is eventually authorized.

The exact freshness budget remains `NEEDS VERIFICATION`.

## Water-body identity and geometry

Identity resolution must prefer governed identifiers and geometry evidence over names.

Required negative cases include:

- duplicate water-body names in different counties;
- one water body spanning multiple counties;
- county spelling or publication errors;
- aliases and renamed water bodies;
- whole-lake versus cove, beach, pond, outlet, or management-zone scope;
- a press release using a broad place name while the table uses a managed subunit; and
- geometry unavailable or inconsistent with the source-native name.

No guessed centroid, county polygon, whole-lake polygon, or route may be published from an unresolved identity.

## Required no-network fixtures

Before any live connector is enabled, add synthetic or source-permitted fixtures for:

1. Watch;
2. Warning;
3. Hazard;
4. lifted advisory;
5. zoned advisory;
6. whole-water-body advisory;
7. duplicate name in different counties;
8. conflicting official surfaces;
9. malformed row;
10. partial snapshot;
11. source unavailable;
12. stale snapshot;
13. correction after publication; and
14. recommendation/closure-authority separation.

Fixtures are test material, not source authority.

## Evidence, review, and release gates

A public-safe HAB layer or alert requires, at minimum:

- active and reviewed SourceDescriptor;
- verified rights, terms, access, and attribution;
- deterministic capture and immutable source snapshots;
- water-body identity and geometry closure;
- freshness and complete-snapshot validation;
- evidence bundle and receipts;
- policy evaluation;
- public-safety and source-steward review;
- release manifest and explicit approval;
- correction, withdrawal, cache invalidation, and rollback targets; and
- a public client that exposes source vintage and unresolved/stale states.

This page closes none of those gates.

## Correction and rollback

### Documentation correction

The July 24 conflict is recorded instead of resolved by guess. If KDHE later corrects either surface, capture the corrected bytes, publication/update time, and digest; link the correction to both prior snapshots.

### Before merge

Close the draft pull request and abandon the branch.

### After merge

Revert this documentation file through a reviewed pull request if its profile is wrong. Do not delete captured source history, silently clear an advisory, or rewrite shared repository history.

[Back to top](#top)
