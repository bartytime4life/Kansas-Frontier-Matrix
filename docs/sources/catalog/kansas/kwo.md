<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-kansas-kwo
title: KWO — Kansas Water Office (Source Catalog Entry)
type: standard
subtype: source-catalog-entry
version: v0.3
status: source-grounded geometry/crosswalk candidate; internal; not released; NEEDS VERIFICATION before promotion
owners: NEEDS VERIFICATION — Source steward + Hydrology domain steward + Water Planning domain steward
created: 2026-07-28
updated: 2026-07-30
policy_label: public-review; bounded-source-admission; internal-registry; not-released; cite-or-abstain; fail-closed
related:
  - docs/sources/catalog/kansas/README.md
  - docs/sources/catalog/README.md
  - docs/sources/catalog/IDENTITY.md
  - docs/sources/catalog/PROFILES.md
  - docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md
  - docs/sources/catalog/OPEN-QUESTIONS.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/truth-posture.md
  - docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - schemas/contracts/v1/domains/water_planning/
  - contracts/domains/water_planning/
  - fixtures/domains/water_planning/
  - fixtures/domains/water_planning/geometry_authority/
  - tools/validators/domains/water_planning/validate_geometry_authority.py
  - tools/validators/domains/water_planning/validate_rac_registry.py
  - tests/domains/water_planning/test_geometry_authority.py
  - tests/domains/water_planning/test_rac_registry.py
  - tests/schemas/test_water_planning_contracts.py
  - docs/adr/ADR-0001-schema-home.md
tags: [kfm, source-catalog, kansas, kansas-first, kwo, water-planning, water-infrastructure, grant, rac, regional-advisory-committee, water-authority, water-plan, hydrology, governance, deferred-epic]
notes:
  - "The exact public KWO RAC Feature Service and Census 2025 county layer are admitted only for the bounded internal geometry/crosswalk candidate recorded in issue #1675."
  - "No recurring connector, scheduling, release, deployment, or publication is authorized."
  - "Slice 1 of the water-planning modeling epic (issue #1647): official public-source and document inventory."
  - "FY2027 SWIGP application deadline: 2026-09-15T23:59:00-05:00 (America/Chicago / CDT)."
  - "HB 2462 (2026) changed eligibility criteria, scoring categories, and administration — must be modeled as a new ProgramVersion."
  - "Kansas has exactly 14 Regional Advisory Committee planning areas."
  - "Slice 4 now pins one 14-feature KWO geometry payload and a 209-row positive-area county intersection crosswalk."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KWO — Kansas Water Office

> **Source family catalog entry.** The Kansas Water Office (KWO) is the state agency responsible for water resource policy, planning, and administration in Kansas. KWO administers the State Water Infrastructure Grant Program (SWIGP), coordinates the 14 Regional Advisory Committees (RACs), convenes the Kansas Water Authority (KWA), and maintains the Kansas Water Plan. This entry now records the exact public KWO RAC Feature Service used by the bounded internal geometry/crosswalk candidate. It does not authorize a recurring connector, release, or publication.

[![Status: draft](https://img.shields.io/badge/status-draft-yellow)](#status)
[![doc-version](https://img.shields.io/badge/doc--version-v0.3-blue)](#status)
[![family](https://img.shields.io/badge/family-kansas%20%C2%A77.3%20canonical-success)](#)
[![Doc type](https://img.shields.io/badge/type-source%20catalog-blue)](#)
[![Domain](https://img.shields.io/badge/domain-hydrology%20%C2%B7%20water%20planning%20%C2%B7%20governance-2ea44f)](#)
[![Implementation](https://img.shields.io/badge/implementation-bounded%20candidate-f59e0b)](#governance-status)
[![Release](https://img.shields.io/badge/release-not--released-b42318)](#authority-level)
[![Last updated](https://img.shields.io/badge/last%20updated-2026--07--30-informational)](#)

**Status:** `source-grounded candidate` (v0.3) &nbsp;·&nbsp; **Owners:** `<TODO — source steward + Hydrology domain steward>` &nbsp;·&nbsp; **Updated:** `2026-07-30`

---

## Quick jump

- [1. Scope](#1-scope) · [2. Status and source basis](#2-status-and-source-basis) · [3. Official sources](#3-official-sources)
- [4. Governance status](#4-governance-status) · [5. Required data model](#5-required-data-model) · [6. Entity types](#6-entity-types)
- [7. FY2027 application window](#7-fy2027-application-window) · [8. HB 2462 program changes](#8-hb-2462-program-changes)
- [9. RAC planning regions](#9-rac-planning-regions) · [10. Repository placement](#10-repository-placement)
- [11. Exclusions](#11-exclusions) · [12. Rights and access](#12-rights-and-access)
- [13. Open verification items](#13-open-verification-items) · [14. Related docs](#14-related-docs)

---

## 1. Scope

The Kansas Water Office is the central state agency for water resource governance in Kansas. This catalog entry scopes the following KWO surfaces as the official public-source and document inventory for the water-planning modeling epic:

| Surface | URL | Documentation status |
|---|---|---|
| State Water Infrastructure Grant Program | https://www.kwo.ks.gov/events-initiatives/grant-programs/state-water-infrastructure-grant-programs | CONFIRMED public |
| Regional Advisory Committees | https://www.kwo.ks.gov/about-us/regional-advisory-committees | CONFIRMED public |
| Kansas Water Authority | https://www.kwo.ks.gov/about-us/kansas-water-authority/-folder-105 | CONFIRMED public |
| Kansas Water Plan | https://www.kwo.ks.gov/water-plan/water-plan | CONFIRMED public |

All four URLs are official public-facing KWO pages. This document records them for inventory purposes. It does not constitute source admission, connector authorization, or publication clearance.

---

## 2. Status and source basis

| Field | Value |
|---|---|
| Document lifecycle | `draft` |
| Source family | `kansas` (§7.3 canonical) |
| Connector lane | `connectors/kansas/` — **NEEDS VERIFICATION** that KWO sub-path exists; no connector activation authorized |
| Source admission | Bounded to KWO ArcGIS item `cd87ef7a0bb34cc4a7f57e662d73ec0f`, layer `0`, and Census TIGERweb Counties 2025 for the internal RAC geometry/crosswalk candidate |
| Live network access | One observed retrieval recorded in the registry; no recurring connector or schedule |
| Rights and sensitivity | KWO item states no special restrictions; independent rights review remains pending; public administrative boundaries only |
| Release or publication effect | None |
| Human review | Pending |

---

## 3. Official sources

### 3.1 State Water Infrastructure Grant Program (SWIGP)

- **URL:** https://www.kwo.ks.gov/events-initiatives/grant-programs/state-water-infrastructure-grant-programs
- **Authority:** Kansas Water Office
- **Program purpose:** Provides state funding for water infrastructure projects submitted by eligible Kansas entities.
- **FY2027 cycle:** Application window closes at **11:59 p.m. on September 15, 2026, Central Time** (`2026-09-15T23:59:00-05:00`, `America/Chicago`).
- **Legislative basis:** 2026 HB 2462 changed eligibility criteria, scoring categories, and administration for the program. This change must be represented as a new `ProgramVersion` record, not as an overwrite of prior program history.
- **Note:** Authenticated grant-portal data is not scraped or treated as public without verified authority.

### 3.2 Regional Advisory Committees (RAC)

- **URL:** https://www.kwo.ks.gov/about-us/regional-advisory-committees
- **Geometry item:** https://www.arcgis.com/home/item.html?id=cd87ef7a0bb34cc4a7f57e662d73ec0f
- **Geometry layer:** https://services1.arcgis.com/q2CglofYX6ACNEeu/arcgis/rest/services/Regional_Planning_Area/FeatureServer/0
- **Authority:** Kansas Water Office
- **Structure:** Kansas has **14 Regional Advisory Committee planning areas** that provide regional input into state water planning.
- **Identity requirement:** All 14 RAC regions resolve through one versioned, digest-pinned identity-authority candidate. The public page supplies the names; KFM assigns `kwo-rac-01` through `kwo-rac-14` by the frozen lexicographic official-name order. The numeric suffix is not claimed to be a KWO-native identifier.
- **Observed geometry version:** Source item modified `2026-06-24T15:17:37Z`; the registry pins the exact response digest observed on `2026-07-30`.
- **County derivation source:** U.S. Census Bureau TIGERweb Counties layer, January 1, 2025 vintage. County rows are computed spatial overlaps, not KWO membership claims.

### 3.3 Kansas Water Authority (KWA)

- **URL:** https://www.kwo.ks.gov/about-us/kansas-water-authority/-folder-105
- **Authority:** Kansas Water Office
- **Role:** The Kansas Water Authority advises the Governor and Legislature on water resource policy. KWA meetings and decisions are distinct from RAC advisory meetings and from grant award decisions.

### 3.4 Kansas Water Plan

- **URL:** https://www.kwo.ks.gov/water-plan/water-plan
- **Authority:** Kansas Water Office
- **Role:** The official state water planning document. Water plan versions and amendments must be modeled as distinct `ProgramVersion` or document records, not as overwritten history.

---

## 4. Governance status

> [!IMPORTANT]
> **BOUNDED EXCEPTION RECORDED.** Issue #1675 records the exact source-research
> and candidate-authoring authority for this RAC geometry/crosswalk slice.
> Broader connector, grant-record, proof, release, deployment, publication,
> ready, and merge operations remain held.
>
> This file originated as **Slice 1 — official public-source and document inventory**. Slice 4 adds only a bounded, reference-only RAC identity and geometry-authority candidate. Neither slice authorizes connector activation, authenticated portal access, real geometry construction, proof construction, release, deployment, or publication.

| Dependency | Status |
|---|---|
| Platform controls (issue #1675) | Bounded RAC candidate exception only; connector, release, and publication remain blocked |
| Prior dependency (issue #1531) | Archived — no longer the operative dependency |
| First admissible slice | Documentation/source inventory (this file) |
| Schema scaffolds (Slice 2) | `schemas/contracts/v1/domains/water_planning/` — PROPOSED, no data produced |
| Connector work | Not authorized — requires separate review after #1675 |
| Evidence and publication | Not authorized — requires separate slice review |

### Rollback

Before merge, close the draft pull request and abandon the branch. After merge, revert scoped commits only; preserve historical program documents and event/decision lineage.

---

## 5. Required data model

The following fields must be preserved for each KWO water-planning entity. These are model requirements, not current schema implementations. All fields are subject to schema review before promotion.

| Field | Purpose | Anti-collapse rule |
|---|---|---|
| Source and source-product identity | Trace every record to its authoritative KWO page | Source identity ≠ source activation |
| Program name and version | Distinguish FY-by-FY program instances | One ProgramVersion per statutory or policy change |
| Statutory or policy basis reference | Record HB 2462 and other legislative changes | A new law creates a new version, not an overwrite |
| Document title, version, digest, and effective date | Digest-link historical guidance | Digest ≠ publication approval |
| Event type and event status | Distinguish meeting from approval | Meeting ≠ decision ≠ award |
| Application-window open/close times with timezone | FY2027: `2026-09-15T23:59:00-05:00`, `America/Chicago` | Deadline ≠ award ≠ payment |
| Meeting start/end, location, virtual-access posture | Record where and how each meeting occurred | Meeting ≠ planning decision |
| Cancellation/reschedule state | Record if a meeting was cancelled or moved | Cancellation ≠ new meeting |
| Planning-region identity and geometry reference | Tie each RAC meeting or project to a governed region | Geometry confidence: unresolved \| approximate \| confirmed |
| Applicant/recipient identity with resolution status | Track who applied and who received | Unresolved identity ≠ guessed identity |
| Project location and geometry confidence | Record where infrastructure is located | Missing geometry → unresolved, never guessed |
| Requested amount | What the applicant asked for | Requested ≠ recommended ≠ awarded ≠ paid |
| Recommended amount | What the advisory process recommended | Recommendation ≠ award |
| Awarded amount | What was formally awarded | Award ≠ payment ≠ project completion |
| Paid amount | What was actually disbursed | Payment ≠ project completion ≠ operational benefit |
| Funding source and fiscal year | Trace money to its source and year | Fiscal year ≠ calendar year |
| Source publication, retrieval, correction, supersession times | Full temporal provenance | Publication ≠ evidence closure |
| Evidence, receipt, policy, and release references | Keep each record traceable | Evidence ref ≠ publication approval |
| Rights, access, and public-record limitations | Flag authenticated portal content as non-public | Portal content ≠ public-safe data |

---

## 6. Entity types

The water-planning modeling epic requires 15 distinct entity types. A meeting is not an approval. An application is not an award. An award is not a completed project. A scoring matrix is not a project outcome. A recipient list is not proof of payment, construction, or operational benefit.

| # | Entity | Schema (PROPOSED) | Anti-collapse boundary |
|---|---|---|---|
| 1 | `PlanningRegion` | `schemas/contracts/v1/domains/water_planning/planning_region.schema.json` | Not a meeting, award, or project |
| 2 | `PublicMeeting` | `schemas/contracts/v1/domains/water_planning/public_meeting.schema.json` | Not an approval, decision, or award |
| 3 | `AdvisoryCommitteeMeeting` | `schemas/contracts/v1/domains/water_planning/advisory_committee_meeting.schema.json` | Not a public meeting, approval, or award |
| 4 | `ProgramVersion` | `schemas/contracts/v1/domains/water_planning/program_version.schema.json` | Not a scoring matrix, application, or award |
| 5 | `ScoringMatrixVersion` | `schemas/contracts/v1/domains/water_planning/scoring_matrix_version.schema.json` | Not a project outcome, application, or award |
| 6 | `ApplicationWindow` | `schemas/contracts/v1/domains/water_planning/application_window.schema.json` | Not an application, recommendation, or award |
| 7 | `Application` | `schemas/contracts/v1/domains/water_planning/application.schema.json` | Not a recommendation, award, payment, or project |
| 8 | `EligibilityDecision` | `schemas/contracts/v1/domains/water_planning/eligibility_decision.schema.json` | Not a recommendation or award |
| 9 | `Recommendation` | `schemas/contracts/v1/domains/water_planning/recommendation.schema.json` | Not an award, payment, or project |
| 10 | `Award` | `schemas/contracts/v1/domains/water_planning/award.schema.json` | Not a payment, project, or operational benefit |
| 11 | `FundingAgreement` | `schemas/contracts/v1/domains/water_planning/funding_agreement.schema.json` | Not an award or project completion |
| 12 | `Project` | `schemas/contracts/v1/domains/water_planning/project.schema.json` | Not a completion, payment, or operational benefit |
| 13 | `ConstructionMilestone` | `schemas/contracts/v1/domains/water_planning/construction_milestone.schema.json` | Not a completion or operational benefit |
| 14 | `Completion` | `schemas/contracts/v1/domains/water_planning/completion.schema.json` | Not a payment or operational benefit claim |
| 15 | `CorrectionOrWithdrawal` | `schemas/contracts/v1/domains/water_planning/correction_or_withdrawal.schema.json` | Not a new award or project record |

All schemas are **PROPOSED** scaffolds. They define the data model intent. They do not constitute source admission, release approval, or publication authorization.

---

## 7. FY2027 application window

> [!IMPORTANT]
> The Kansas Water Office states that the FY 2027 State Water Infrastructure Grant application cycle is open through **11:59 p.m. on September 15, 2026**.

| Field | Value |
|---|---|
| Fiscal year | FY2027 |
| Closes at (source-stated) | 11:59 p.m. on September 15, 2026 |
| Closes at (ISO 8601 with UTC offset) | `2026-09-15T23:59:00-05:00` |
| Timezone (IANA) | `America/Chicago` |
| UTC offset in effect | CDT (UTC−5) |
| Source URL | https://www.kwo.ks.gov/events-initiatives/grant-programs/state-water-infrastructure-grant-programs |
| Fixture | `fixtures/domains/water_planning/application_window/valid/valid_1.json` |

The FY2027 deadline is stored with explicit Central Time handling and source-native timezone evidence (`America/Chicago`). All future application-window records must include `closes_at` with a UTC offset and `source_timezone` with the IANA timezone name. The `source_timezone` field is required by the `ApplicationWindow` schema.

---

## 8. HB 2462 program changes

> [!IMPORTANT]
> 2026 HB 2462 changed eligibility criteria, scoring categories, and administration for the State Water Infrastructure Grant Program.

This legislative change must be represented as a new `ProgramVersion` record — **not** as an overwrite of prior program history. The FY2027 `ProgramVersion` fixture at `fixtures/domains/water_planning/program_version/valid/valid_1.json` demonstrates:

```json
{
  "version_id": "kwo-swigp-fy2027-hb2462",
  "program_name": "State Water Infrastructure Grant Program",
  "statutory_basis": "2026 HB 2462",
  "fiscal_year": "FY2027",
  "effective_date": "2026-07-01",
  "supersedes_ref": "kwo-swigp-fy2026",
  ...
}
```

The `supersedes_ref` field preserves the lineage to the prior program version. The prior version's records remain intact.

A scoring matrix change driven by HB 2462 must also be represented as a new `ScoringMatrixVersion`, not an overwrite.

---

## 9. RAC planning regions

The Kansas Water Office page identifies exactly **14 Regional Advisory Committee planning areas**. Slice 4 freezes the source-grounded names below and assigns stable KFM identities in lexicographic name order. The ordinal is a KFM convention, not a source-native KWO number.

| KFM ID | KFM ordinal | Source-grounded name |
|---|---:|---|
| `kwo-rac-01` | 1 | Cimarron |
| `kwo-rac-02` | 2 | Equus-Walnut |
| `kwo-rac-03` | 3 | Great Bend Prairie |
| `kwo-rac-04` | 4 | Kansas |
| `kwo-rac-05` | 5 | Marais des Cygnes |
| `kwo-rac-06` | 6 | Missouri |
| `kwo-rac-07` | 7 | Neosho |
| `kwo-rac-08` | 8 | Red Hills |
| `kwo-rac-09` | 9 | Smoky Hill-Saline |
| `kwo-rac-10` | 10 | Solomon-Republican |
| `kwo-rac-11` | 11 | Upper Arkansas |
| `kwo-rac-12` | 12 | Upper Republican |
| `kwo-rac-13` | 13 | Upper Smoky Hill |
| `kwo-rac-14` | 14 | Verdigris |

| Authority field | Slice 4 posture |
|---|---|
| Source locator | KWO Regional Advisory Committees page |
| Geometry source | KWO ArcGIS item `cd87ef7a0bb34cc4a7f57e662d73ec0f`, layer `0`, modified `2026-06-24T15:17:37Z` |
| County source | Census TIGERweb Counties layer, January 1, 2025 vintage, Kansas FIPS `20` |
| Source observation | Exact source-response digests and `2026-07-30` observation time are pinned in the registry records |
| Identity version | `kfm-rac-identity-v1` |
| Digest scope | Normalized authority metadata plus ordered ID/ordinal/name tuples; not a claimed digest of remote page bytes |
| Numeric-ID posture | `source_native_numeric_ids: false` |
| Correction posture | Explicit current/corrected/superseded state plus lineage |
| Region geometry | 14-feature source-grounded GeoJSON in `data/processed/water_planning/rac_regions/`, digest-pinned by the dataset registry |
| County crosswalk | 209 positive-area intersections across all 105 Kansas counties; 50 dominant, 122 material-partial, 37 boundary-sliver |
| Project region | Nullable state; a non-null value must resolve to the exact RAC inventory |
| Project geometry | Separate nullable reference; never inferred from region, address, recipient, venue, county, or prose |

The identity schema continues to enforce null/reference coherence for individual
entities. The concrete registry validator additionally locks payload bytes,
the exact 14-feature inventory, all 105 Kansas county GEOIDs, the ordered
mapping digest, overlap-class thresholds, source versions, and the
`not-released` posture. County intersections are geometry relationships, not
county governance membership. Synthetic authority fixtures remain test-only.

---

## 10. Repository placement

| Artifact | Path |
|---|---|
| This source catalog entry | `docs/sources/catalog/kansas/kwo.md` |
| Kansas source family index | `docs/sources/catalog/kansas/README.md` |
| Water-planning schemas (PROPOSED) | `schemas/contracts/v1/domains/water_planning/` |
| Water-planning contracts (PROPOSED) | `contracts/domains/water_planning/` |
| Water-planning fixtures (synthetic) | `fixtures/domains/water_planning/` |
| Water-planning schema tests | `tests/schemas/test_water_planning_contracts.py` |
| Slice 4 authority validator | `tools/validators/domains/water_planning/validate_geometry_authority.py` |
| Slice 4 synthetic fixtures | `fixtures/domains/water_planning/geometry_authority/` |
| Slice 4 no-network tests | `tests/domains/water_planning/test_geometry_authority.py` |
| RAC geometry dataset registry | `data/registry/datasets/water_planning/kwo_rac_regions_2026-06-24.json` |
| RAC/county crosswalk registry | `data/registry/crosswalks/water_planning/kwo_rac_counties_2026-06-24__tiger2025.json` |
| RAC geometry payload | `data/processed/water_planning/rac_regions/kwo_rac_regions_2026-06-24.geojson` |
| KWO source descriptor | `data/registry/sources/water_planning/kwo_rac_feature_service.source.json` — proposed, needs review, connector disabled |
| Census source descriptor | `data/registry/sources/water_planning/census_tigerweb_counties_2025.source.json` — proposed, needs review, connector disabled |
| Concrete registry contract | `contracts/domains/water_planning/rac_geometry_registry.md` |
| Concrete registry validator | `tools/validators/domains/water_planning/validate_rac_registry.py` |
| Concrete registry tests | `tests/domains/water_planning/test_rac_registry.py` |
| Kansas connector lane | `connectors/kansas/` — KWO sub-path **NEEDS VERIFICATION** |
| Source registry | `data/registry/sources/water_planning/` — two bounded SourceDescriptor candidates; no recurring connector |
| Policy | `policy/domains/water_planning/` — not yet created |

---

## 11. Exclusions

This catalog entry explicitly excludes:

- Authenticated grant-portal data — not scraped or treated as public without verified authority.
- Applicant personal or organization data not published on official KWO public pages.
- Grant application content, scores, review notes, or adjudication records not released as official public records.
- Any funding, approval, completion, or operational benefit claim inferred beyond the source evidence.
- Precise project geometry guessed from applicant address or project description.
- Connector, watcher, scheduler, or live-network runtime behavior.
- Release, publication, or evidence-closure decisions.

---

## 12. Rights and access

| Question | Current status |
|---|---|
| KWO public web pages | Presumed open public information; NEEDS VERIFICATION of terms of use |
| SWIGP recipient lists | Published on KWO web; rights NEEDS VERIFICATION |
| Grant application content | Non-public until official release; authenticated portal content excluded |
| RAC meeting records | Public meeting records; rights NEEDS VERIFICATION for archived content |
| KWA meeting records | Public meeting records; rights NEEDS VERIFICATION |
| Kansas Water Plan documents | Public documents; rights NEEDS VERIFICATION for specific versions |

The observed KWO item states that there are no special restrictions on the
content. Independent rights review remains required before release. The
bounded internal geometry/crosswalk candidate does not authorize an ongoing
connector or any public carrier.

---

## 13. Open verification items

| ID | Item | Priority |
|---|---|---|
| OQ-KWO-01 | Verify exact URL structure and machine-accessible endpoints for SWIGP recipient data | High |
| OQ-KWO-02 | Obtain domain/rights review for the new canonical RAC geometry and county-crosswalk records; source and derivation are now concrete, but release remains held | High |
| OQ-KWO-03 | Verify terms of use for KWO public web content | High |
| OQ-KWO-04 | Confirm FY2027 deadline is not changed by a subsequent KWO notice | High |
| OQ-KWO-05 | Verify HB 2462 effective date and scope of changes | Medium |
| OQ-KWO-06 | Identify the KWO connector sub-path under `connectors/kansas/` | Medium |
| OQ-KWO-07 | Determine whether KWA meeting minutes are machine-accessible or require manual extraction | Low |
| OQ-KWO-08 | Determine whether historical SWIGP scoring matrices are available as digest-linkable documents | Low |

---

## 14. Related docs

- [`docs/sources/catalog/kansas/README.md`](./README.md) — Kansas source family index
- [`docs/sources/catalog/README.md`](../README.md) — Source catalog parent
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — Placement and authority rules
- [`docs/doctrine/lifecycle-law.md`](../../doctrine/lifecycle-law.md) — RAW → PUBLISHED governance
- [`docs/doctrine/truth-posture.md`](../../doctrine/truth-posture.md) — Cite-or-abstain
- [`schemas/contracts/v1/domains/water_planning/`](../../../schemas/contracts/v1/domains/water_planning/) — Entity schemas (PROPOSED)
- [`contracts/domains/water_planning/`](../../../contracts/domains/water_planning/) — Contract documents (PROPOSED)
- [`fixtures/domains/water_planning/`](../../../fixtures/domains/water_planning/) — Synthetic fixtures
- [`tests/schemas/test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) — Schema tests
- [`fixtures/domains/water_planning/geometry_authority/`](../../../fixtures/domains/water_planning/geometry_authority/) — Slice 4 synthetic authority fixtures
- [`tools/validators/domains/water_planning/validate_geometry_authority.py`](../../../tools/validators/domains/water_planning/validate_geometry_authority.py) — Slice 4 deterministic checker
- [`tests/domains/water_planning/test_geometry_authority.py`](../../../tests/domains/water_planning/test_geometry_authority.py) — Slice 4 no-network tests
- [`contracts/domains/water_planning/rac_geometry_registry.md`](../../../contracts/domains/water_planning/rac_geometry_registry.md) — Concrete source and derivation contract
- [`tools/validators/domains/water_planning/validate_rac_registry.py`](../../../tools/validators/domains/water_planning/validate_rac_registry.py) — Concrete registry validator
- [`tests/domains/water_planning/test_rac_registry.py`](../../../tests/domains/water_planning/test_rac_registry.py) — Concrete registry regression tests
- [`docs/adr/ADR-0001-schema-home.md`](../../adr/ADR-0001-schema-home.md) — Schema-home convention

[Back to top](#top)
