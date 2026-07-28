<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-kansas-kcds
title: Kansas Crash Data System (KCDS) — Governed Discovery
type: source-product-page; discovery-only; privacy-rights-discovery; no-connector-activation
version: v0.1.0
status: discovery-only draft; no source activation; blocked pending KFM-#1675
owners: NEEDS VERIFICATION — Kansas source steward + Roads/Rail/Trade steward + Privacy reviewer + Rights reviewer + Public-safety steward
created: 2026-07-28
updated: 2026-07-28
policy_label: >
  public-review; discovery-only; cite-or-abstain; fail-closed;
  privacy-gated; rights-gated; sensitivity-gated; no-activation;
  no-publication; no-incident-level-ingestion; no-authenticated-access
current_path: docs/sources/catalog/kansas/kcds.md
truth_posture: >
  CONFIRMED official KDOT/KDPS program page identity, April 27 2026 go-live
  date, KHP KLER transition schedule, and public road-reference FeatureServer
  existence / PROPOSED KFM source-role split, candidate SourceDescriptor
  identities, field-level privacy classification, temporal model, and
  public-safe generalization proposal / NEEDS VERIFICATION ArcGIS
  FeatureServer terms, aggregate-statistics surfaces, XML schema availability,
  MMUCC mapping, field-level enumeration, and all authenticated portal
  content / UNKNOWN incident-level API, bulk-export, open-data-portal
  release, stable crash-ID semantics, and complete correction model
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: DISCOVERY-SNAPSHOT-2026-07-28
  kcds_program_page: https://www.ksdot.gov/about/our-organization/divisions/transportation-safety/safety-data/kansas-crash-data-system-kscds
  le_crash_reporting_page: https://www.ksdot.gov/about/our-organization/divisions/transportation-safety/safety-data/law-enforcement-crash-reporting-information
  khp_kler_page: https://kansashighwaypatrol.gov/about-us/kler-information/
  feature_server: https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Transportation/Kansas_Crash_Data_System_Roads/FeatureServer
  go_live_date: 2026-04-27
  blocking_issue: bartytime4life/Kansas-Frontier-Matrix#1675
  closing_issue: bartytime4life/Kansas-Frontier-Matrix#1648
related:
  - ./README.md
  - ./kdot.md
  - ../README.md
  - ../RIGHTS-AND-SENSITIVITY-MAP.md
  - ../OPEN-QUESTIONS.md
  - ../../SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../doctrine/directory-rules.md
  - ../../../../data/registry/sources/
  - ../../../../policy/sensitivity/
  - ../../../../policy/rights/
  - ../../../../release/
  - ../../../../fixtures/synthetic/kcds/
tags: >
  [kfm, kansas, kdot, khp, kcds, kler, crash-data,
  roads-rail-trade, privacy, rights, discovery-only,
  pii, sensitive, no-activation, no-publication,
  road-reference, feature-server, mmucc, law-enforcement]
notes:
  - >-
    KCDS is a KDOT/KHP collaborative program; it is NOT a separate source
    authority root. Discovery belongs under the existing kansas/ source
    family and the KDOT product page family.
  - >-
    The public ArcGIS road-reference FeatureServer is a road-placement
    geometry aid, NOT a crash-incident record dataset. This distinction
    must be preserved in every future KFM artifact referencing KCDS.
  - >-
    This document does NOT authorize: authenticated KCDS/KLER portal
    access, account creation, incident-level ingestion, personal-data
    processing, connector activation, or publication.
  - >-
    Blocked for any branch/commit/PR until bartytime4life/Kansas-Frontier-Matrix#1675
    records verified platform controls and explicit bounded recovery authorization.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas Crash Data System (KCDS) — Governed Discovery

> **Documentation-only discovery report** for the Kansas Crash Data System (KCDS) operated by KDOT's Transportation Safety Division in collaboration with the Kansas Highway Patrol (KHP). This page records the results of a governed source-surface, rights, privacy, and API discovery. It does not activate a connector, create a source authority, admit incident-level records, or authorize publication of any crash data.

[![Status: discovery-only](https://img.shields.io/badge/status-discovery--only-d4a72c?style=flat-square)](#status)
[![Blocking issue: #1675](https://img.shields.io/badge/blocked%20by-%231675-b42318?style=flat-square)](#governance-status)
[![Source activation: none](https://img.shields.io/badge/source%20activation-none-b42318?style=flat-square)](#authority-boundary)
[![Incident-level ingestion: denied](https://img.shields.io/badge/incident--level%20ingestion-denied-b42318?style=flat-square)](#authority-boundary)
[![Privacy: fail-closed](https://img.shields.io/badge/privacy-fail--closed-b42318?style=flat-square)](#privacy-and-sensitivity-matrix)
[![Road reference ≠ crash incidents](https://img.shields.io/badge/road%20reference-%E2%89%A0%20crash%20incidents-b42318?style=flat-square)](#source-role-matrix)

> [!CAUTION]
> **The public road-reference FeatureServer is NOT a crash-incident dataset.** The ArcGIS FeatureServer at `kanplan.ksdot.gov/…/Kansas_Crash_Data_System_Roads` provides road geometry intended to assist law-enforcement agencies in placing crash locations within KCDS. It does not expose crash records, fatality data, person records, vehicle records, or investigation findings. Mislabeling it as public crash-incident data is a source-role anti-collapse violation.

> [!WARNING]
> **All incident-level and personal-data questions are fail-closed.** Unresolved rights, privacy, juvenile, medical, witness, vehicle, address, or precise-location questions remain fail-closed pending policy review. No connector, release, publication, or public-map layer may reference KCDS incident data until every gate listed in this document closes.

> [!IMPORTANT]
> **Blocked.** This discovery document may be read, linked, and updated with official-source evidence. No branch, commit (other than this discovery document itself), authenticated session, scraper, connector, incident-level dataset, or public map layer may be created until bartytime4life/Kansas-Frontier-Matrix#1675 records verified platform controls and explicit bounded recovery authorization.

**Quick navigation:** [Status](#status) · [Governance](#governance-status) · [Authority](#authority-boundary) · [Program identity](#program-identity) · [Surface inventory](#1-source-surface-inventory) · [Rights matrix](#2-rights-and-terms-matrix) · [Privacy matrix](#3-field-level-privacy-and-sensitivity-matrix) · [Source-role matrix](#4-source-role-matrix) · [Temporal model](#5-temporal-and-correction-model) · [SourceDescriptors](#6-inactive-candidate-sourcedescriptors) · [Generalization](#7-public-safe-generalization-proposal) · [Fixtures](#8-synthetic-fixtures) · [Threat model](#9-threat-model) · [Go/no-go](#10-gono-go-recommendations) · [Open questions](#11-open-questions) · [Rollback](#rollback)

---

## Status

| Field | Value |
|---|---|
| Document lifecycle | `discovery-only draft` |
| KFM source activation | None created by this page |
| Live network or authenticated access | None performed |
| Incident-level ingestion | Denied |
| Publication authority | None |
| Blocking issue | bartytime4life/Kansas-Frontier-Matrix#1675 |
| Closed issue | bartytime4life/Kansas-Frontier-Matrix#1648 |
| Human review | Pending |
| Rights closure | NEEDS VERIFICATION per surface |
| Privacy closure | Fail-closed; pending policy |

---

## Governance status

**BLOCKED for all implementation work by bartytime4life/Kansas-Frontier-Matrix#1675.**

Issue bartytime4life/Kansas-Frontier-Matrix#1531 is archived and is no longer the operative dependency. Do not create a branch (other than the one carrying this discovery document), commit, pull request, account, authenticated session, scraper, connector, incident-level dataset, or public map layer until bartytime4life/Kansas-Frontier-Matrix#1675 records verified platform controls and explicit bounded recovery authorization.

This discovery document is the first bounded deliverable and is documentation-only.

---

## Authority boundary

| Action | Permitted by this document? |
|---|---|
| Reading official public program pages | Yes — cited below |
| Documenting observed public surface inventory | Yes — this document |
| Updating open questions and evidence records | Yes |
| Accessing authenticated KCDS/KLER portals | **No** |
| Creating law-enforcement accounts or credentials | **No** |
| Ingesting incident-level crash records | **No** |
| Processing personal data from crash reports | **No** |
| Activating any connector | **No** |
| Releasing or publishing any KCDS data | **No** |
| Creating a separate KCDS source-authority root | **No** — KCDS belongs under the kansas/ source family |
| Treating the road-reference FeatureServer as crash-incident data | **No** |

---

## Program identity

The **Kansas Crash Data System (KCDS)** is the statewide crash data management system operated by the Kansas Department of Transportation (KDOT) Transportation Safety Division, in collaboration with the Kansas Highway Patrol (KHP).

| Attribute | Value | Official source |
|---|---|---|
| Program name | Kansas Crash Data System (KCDS) | KDOT program page |
| Alternate abbreviation | KSCDS (seen on KDOT program page URL) | KDOT program page URL slug |
| Operating agency | KDOT Transportation Safety Division | KDOT program page |
| Law-enforcement partner | Kansas Highway Patrol (KHP) | KHP KLER page |
| Go-live date | April 27, 2026 | KDOT program page (per issue body) |
| Submission methods at go-live | Web entry, KLER electronic submission | KDOT program page (per issue body) |
| Planned future method | RMS XML integration (anticipated late 2026–2027) | KDOT program page (per issue body) |
| Agency selection deadline | September 2026 — agencies select submission method | KDOT program page (per issue body) |
| KLER end date | December 31, 2027 — KLER crash-report submission ends | KDOT program page / KHP KLER page (per issue body) |
| Source family | `kansas` — under existing KDOT/Kansas source family | Directory Rules v1.2 §7.3; `kdot.md` |
| KFM domain anchor | Roads/Rail/Trade Routes (primary); Hazards (crash events); Public Safety (pending) | Discovery inference — NEEDS VERIFICATION |

KCDS is not a separate agency. It is a KDOT program with KHP participation. **Do not create a separate KCDS authority root.**

---

## 1. Source-surface inventory

Classification key:
- `PUBLIC` — No authentication required; terms may still restrict reuse
- `AUTHENTICATED` — Requires account/credential; law-enforcement, agency, or system access
- `PUBLIC_RECORD_REQUEST` — Available by formal KORA or public-records request
- `RESTRICTED` — Legally restricted beyond public-records request
- `UNKNOWN` — Existence or access level not established from official public sources
- `DEPRECATED` — Officially superseded; maintained for lineage

| Surface | URL / locator | Classification | Notes |
|---|---|---|---|
| KCDS program page | `https://www.ksdot.gov/about/our-organization/divisions/transportation-safety/safety-data/kansas-crash-data-system-kscds` | `PUBLIC` | Program overview; no incident data |
| Law-enforcement crash reporting info | `https://www.ksdot.gov/about/our-organization/divisions/transportation-safety/safety-data/law-enforcement-crash-reporting-information` | `PUBLIC` | Guidance for LE agencies; not incident data |
| KHP KLER transition page | `https://kansashighwaypatrol.gov/about-us/kler-information/` | `PUBLIC` | KHP electronic reporting transition info |
| KCDS road-reference FeatureServer | `https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Transportation/Kansas_Crash_Data_System_Roads/FeatureServer` | `PUBLIC` *(road geometry only — see caution)* | Road-reference geometry for crash placement. **NOT crash-incident records.** ArcGIS FeatureServer; terms NEEDS VERIFICATION |
| KCDS web-entry portal (law enforcement) | Not published on public-facing pages | `AUTHENTICATED` | Law-enforcement-only submission portal; no public access |
| KLER submission portal | Not directly available | `AUTHENTICATED` | Kansas Law Enforcement Records electronic submission; end-dated Dec 31 2027 |
| RMS XML integration endpoint | Not yet operational | `UNKNOWN` | Planned for late 2026–2027; not yet available |
| KCDS aggregate statistics / dashboard | Not confirmed on official pages | `UNKNOWN` | May exist; NEEDS VERIFICATION from official KDOT public-data surfaces |
| KCDS downloadable tables / bulk export | Not confirmed | `UNKNOWN` | No confirmed public bulk export at discovery time |
| KCDS open-data portal entry | Not confirmed | `UNKNOWN` | No confirmed Kansas Open Data portal entry for KCDS at discovery time |
| XML schema / code-list specifications | Existence not confirmed on public pages | `UNKNOWN` | May be available to law-enforcement/RMS vendors; public availability NEEDS VERIFICATION |
| MMUCC alignment documentation | Existence not confirmed | `UNKNOWN` | KCDS likely aligns with MMUCC (federal crash data standard); documentation publicly available NEEDS VERIFICATION |
| KDOT crash statistics reports (historical) | `https://www.ksdot.gov/…/safety-data/` (general area) | `UNKNOWN` | KDOT publishes annual crash statistics reports; whether these derive from KCDS at go-live is NEEDS VERIFICATION |
| Prior KACRASH system (predecessor) | Superseded by KCDS April 27 2026 | `DEPRECATED` | NEEDS VERIFICATION: exact name and relationship of predecessor system |

### Surface classification rationale

**Road-reference FeatureServer:** The service exists at a public ArcGIS REST endpoint on `kanplan.ksdot.gov`. It is confirmed as a road-reference geometry service intended to assist crash-report placement. The ArcGIS FeatureServer REST endpoint is publicly reachable. However:
- Terms of reuse for this ArcGIS service are NEEDS VERIFICATION;
- The geometry it contains represents road network reference lines, not crash records;
- Use of this layer outside KCDS placement workflows requires explicit rights verification.

**Authenticated portals:** The KCDS web-entry portal and KLER submission system are law-enforcement/agency tools. No law-enforcement or agency credentials may be created or used without separate explicit authorization. These surfaces are classified `AUTHENTICATED` and are outside the bounds of this discovery.

---

## 2. Rights and terms matrix

| Surface | License / terms | Attribution requirement | Redistribution | Derivative works | Rate limit | Evidence |
|---|---|---|---|---|---|---|
| KCDS program page | Kansas state website terms (NEEDS VERIFICATION) | Cite KDOT as source | Linking permitted; content redistribution NEEDS VERIFICATION | Not addressed | N/A (static page) | KDOT program page (per issue body) |
| Law-enforcement crash reporting info page | Same as above | Same | Same | Same | N/A | KDOT LE reporting page |
| KHP KLER transition page | KHP / State of Kansas website terms (NEEDS VERIFICATION) | Cite KHP as source | Linking permitted; content NEEDS VERIFICATION | Not addressed | N/A | KHP KLER page |
| KCDS road-reference FeatureServer | ArcGIS Online / KDOT GIS terms — **NEEDS VERIFICATION** | NEEDS VERIFICATION | NEEDS VERIFICATION | NEEDS VERIFICATION | ArcGIS FeatureServer default limits apply; exact rate NEEDS VERIFICATION | No explicit terms URL confirmed; Esri/ArcGIS standard terms may apply |
| KCDS authenticated portal | N/A — law-enforcement restricted | N/A | N/A | N/A | N/A | Not accessed |
| KCDS aggregate statistics (if public) | Kansas state public records (KORA); agency-specific terms NEEDS VERIFICATION | NEEDS VERIFICATION | NEEDS VERIFICATION | NEEDS VERIFICATION | NEEDS VERIFICATION | UNKNOWN surface; unverified |
| KCDS XML schemas (if public) | NEEDS VERIFICATION — may be KDOT technical documentation with or without redistribution restriction | NEEDS VERIFICATION | NEEDS VERIFICATION | NEEDS VERIFICATION | N/A | UNKNOWN surface; unverified |

### Key rights notes

1. **KORA applicability.** Kansas crash records are public records under the Kansas Open Records Act (KORA), subject to specific exemptions for personal information, ongoing investigations, juvenile records, and similar categories. The existence of KORA rights does not mean data is available via API; a formal records request is likely required for individual crash reports.

2. **ArcGIS FeatureServer terms.** Esri/ArcGIS services hosted by state agencies may carry the state agency's terms layered on Esri terms. Neither KDOT's nor Esri's specific terms for this service have been verified. KFM must not consume this service at scale before terms verification.

3. **No redistribution assumption.** The default KFM posture is no redistribution permitted until terms verification proves otherwise.

4. **Crash report vs. aggregate statistics.** KORA exemptions and redistribution rules differ between individual crash reports (which contain personal information) and aggregate statistics (which may not). These must be treated as separate rights surfaces.

5. **NEEDS VERIFICATION items requiring official source confirmation before any ingestion:**
   - Exact terms URL for the KCDS road-reference FeatureServer
   - KDOT policy on bulk export or API reuse of road-reference geometry
   - Whether KDOT publishes an explicit open-government data license for GIS layers
   - KORA exemption categories applicable to KCDS crash records
   - Aggregate statistics release schedule and redistribution terms

---

## 3. Field-level privacy and sensitivity matrix

> [!WARNING]
> All fields below that are classified `RESTRICTED` or `PII` are **fail-closed**. No field from the `RESTRICTED` or `PII` rows may appear in any KFM public release without explicit policy review, legal authority verification, and release-gate approval.

Classification key:
- `PUBLIC` — May appear in public releases under verified terms
- `AGGREGATE_ONLY` — May appear only as aggregate statistics (no record-level)
- `PII` — Personal information; restricted; requires policy and legal review
- `RESTRICTED` — Legally restricted; not for public release
- `SENSITIVE` — Operationally or legally sensitive; requires policy review
- `GEOMETRY_RISK` — Precise location that could enable re-identification or harm
- `NEEDS VERIFICATION` — Classification not established; fail-closed until verified

### Road-reference geometry fields (FeatureServer — road network only)

| Field category | Examples | Classification | Notes |
|---|---|---|---|
| Road network geometry | Centerline geometry, route ID, route name | `PUBLIC` *(terms NEEDS VERIFICATION)* | Road-reference geometry only; no crash data |
| Road segment identifiers | LRS route ID, milepost ranges | `PUBLIC` *(terms NEEDS VERIFICATION)* | Reference IDs for crash placement, not crash IDs |
| Administrative attribution | County, city, road class | `PUBLIC` *(terms NEEDS VERIFICATION)* | Standard road-network attributes |

### Crash record fields (incident-level — ALL RESTRICTED pending policy)

> These fields are inferred from MMUCC (Model Minimum Uniform Crash Criteria) standards and comparable state crash-data systems. **No KCDS field-level documentation has been obtained.** All classifications below are `PROPOSED` and `NEEDS VERIFICATION` against official KCDS data dictionaries.

| Field category | Examples | Classification | Notes |
|---|---|---|---|
| **Crash location — precise** | GPS coordinates, address, intersection, milepost | `GEOMETRY_RISK` / `RESTRICTED` | Precise crash locations can enable re-identification when combined with other fields; spatial generalization required for public-safe use |
| **Crash location — generalized** | County, city/township, road class | `AGGREGATE_ONLY` | May appear in aggregate; not record-level without further review |
| **Crash date and time** | Date, time of day, day of week | `SENSITIVE` | Alone not PII; combined with location and persons becomes identifying |
| **Driver information** | Name, DOB, address, license number, state | `PII` / `RESTRICTED` | Personal information; restricted under KORA and federal Driver's Privacy Protection Act (DPPA) |
| **Passenger information** | Name, DOB, address, seating position | `PII` / `RESTRICTED` | Same as driver; DPPA applies |
| **Pedestrian / bicyclist information** | Name, DOB, address | `PII` / `RESTRICTED` | Personal information |
| **Witness information** | Name, address, contact | `PII` / `RESTRICTED` | Witness protection may apply |
| **Officer / agency information** | Officer name, badge, agency, report number | `SENSITIVE` | Some fields may be public; officer name sensitivity varies by agency policy |
| **Injury severity** | KABCO scale, injury type, fatal/non-fatal | `SENSITIVE` | Aggregate forms may be public; record-level may identify victim |
| **Medical outcome** | Transport, treatment location, outcome | `PII` / `RESTRICTED` | HIPAA may apply; medical outcome is highly sensitive |
| **Juvenile records** | Any field involving a person under 18 | `RESTRICTED` | Juvenile information has heightened legal protection |
| **Vehicle information** | VIN, plate, make/model/year, owner | `PII` / `RESTRICTED` | VIN and plate are subject to DPPA; vehicle owner is personal information |
| **Insurance information** | Carrier, policy number | `PII` / `RESTRICTED` | Insurance records are personal financial information |
| **Alcohol / drug involvement** | Test result, refusal, substance type | `RESTRICTED` | Criminal-investigation context; medical sensitivity |
| **Citations issued** | Citation type, violation code | `SENSITIVE` | May be public record; varies by KORA and court-record rules |
| **Criminal investigation fields** | Felony flag, hit-and-run status, investigation open | `RESTRICTED` | Active-investigation exception under KORA |
| **Crash narrative** | Officer free-text description | `SENSITIVE` | May contain PII, medical detail, or investigation content |
| **Diagram / scene sketch** | Scene layout, vehicle positions | `SENSITIVE` | May reveal precise location or identify parties |
| **Crash ID / report number** | KCDS-assigned crash identifier | `SENSITIVE` | Alone not PII; combined with other fields may enable re-identification; stability across corrections NEEDS VERIFICATION |
| **Submission metadata** | Submitting agency, submission date, KLER or web-entry flag | `SENSITIVE` | Operational metadata; not directly PII but may be sensitive |

### Applicable federal and state legal frameworks

| Framework | Applicability to KCDS |
|---|---|
| Kansas Open Records Act (KORA) | Applies to crash reports as public records; specific exemptions cover personal information, ongoing investigations, and juveniles; NEEDS VERIFICATION of exact KDOT/KHP KORA implementation |
| Driver's Privacy Protection Act (DPPA, 18 USC §2721) | Applies to driver and vehicle owner information obtained from motor-vehicle records; driver/owner PII in crash reports may be DPPA-covered |
| HIPAA | May apply to medical outcome fields if sourced from covered entities; NEEDS VERIFICATION |
| Kansas Juvenile Justice Code | Heightened protection for records involving persons under 18 |
| FERPA | Not directly applicable unless crash involves educational-setting records |
| Criminal investigation exemption | KORA exemption for records of ongoing criminal investigations |

---

## 4. Source-role matrix

| Role | Surface | KFM `source_role` | Activation status | Notes |
|---|---|---|---|---|
| Road-reference geometry | KCDS road-reference FeatureServer | `authority` *(for road geometry)* | Inactive — terms NEEDS VERIFICATION | Road network centerlines for crash location placement; not crash incidents |
| Crash incident reports | KCDS web-entry and KLER submission system | `observed` (crash events) + `regulatory` (official record) | **Denied** — law-enforcement only; PII; multiple fail-closed gates | Individual crash reports; contains PII, medical data, investigation data |
| Crash occurrence data | KCDS incident database (authenticated) | `observed` | **Denied** — authenticated; pending all privacy gates | Occurrence time, location, parties — all PII-bearing |
| Aggregate crash statistics | KDOT published aggregate reports (if any) | `aggregate` | `UNKNOWN` — surface existence unverified | May be published as annual reports; rights and derivation from KCDS NEEDS VERIFICATION |
| Manuals and schemas | KCDS data dictionary, XML spec, MMUCC mapping | `documentation` | `UNKNOWN` — public availability unverified | Technical documentation; may be available to vendors; not a data surface |
| Dashboards | KDOT crash data dashboard (if any) | `presentation` | `UNKNOWN` — existence unverified | Interactive visualization; may be public but contains aggregated data only |
| Correction events | KCDS correction/amendment records | `correction` | **Denied** — authenticated; inside crash record lineage | Amendment and rejection records for individual crash reports |
| KLER transition records | Legacy KLER submissions (until Dec 31 2027) | `observed` (transition-era) | **Denied** — authenticated; same PII gates | KLER is the electronic submission mechanism; data is still crash records |
| RMS XML integration | Planned future feed (late 2026–2027) | TBD — not yet defined | **Not yet applicable** | Planned capability; no current surface to classify |

### Anti-collapse rules

The following source-role collapses are prohibited:

| Collapse | Why prohibited |
|---|---|
| Road-reference geometry → crash-incident dataset | The FeatureServer contains road network geometry, not crash records |
| Aggregate statistics → incident-level records | Aggregates do not expose individual crash data; treating them as incident-level is a privacy violation |
| Public crash statistics dashboard → public crash API | A visualization surface does not constitute a data API or bulk-export right |
| KLER transition mechanism → crash data | KLER is a submission mechanism; the resulting data lives in KCDS and carries all KCDS restrictions |
| Documentation / schema → data surface | XML specifications and data dictionaries are not data surfaces |

---

## 5. Temporal and correction model

### Timeline and program evolution

| Date | Event | Certainty |
|---|---|---|
| April 27, 2026 | KCDS goes live; web-entry and KLER submission begin | CONFIRMED (per KDOT program page cited in issue body) |
| September 2026 | Agencies select submission method (web-entry vs. KLER vs. RMS) | CONFIRMED (per KDOT program page) |
| Late 2026 – 2027 | RMS XML integration anticipated | CONFIRMED (per KDOT program page) |
| December 31, 2027 | KLER crash-report submission ends | CONFIRMED (per KDOT/KHP pages) |

### Timestamp semantics

KCDS records involve multiple distinct timestamps that KFM must never collapse:

| Timestamp name | Definition | Notes |
|---|---|---|
| `crash_occurred_at` | Date and time of the crash event | May be estimated; represents the incident, not the report |
| `report_submitted_at` | Date and time the agency submitted the crash report to KCDS | Via web-entry or KLER; submission lag is meaningful |
| `report_accepted_at` | Date and time KCDS accepted the submission | May differ from submission if validation is batched |
| `report_corrected_at` | Date and time a correction or amendment was submitted | May occur multiple times per crash report |
| `report_rejected_at` | Date and time KCDS rejected a submission (if applicable) | Rejection may require resubmission |
| `kfm_retrieved_at` | Date and time KFM retrieved the surface (future, if permitted) | KFM-side timestamp; entirely separate from crash and submission times |
| `kfm_released_at` | Date and time KFM released a derivative (future, if permitted) | KFM release is downstream of retrieval, normalization, and review |

### Record lifecycle states

Proposed normalization vocabulary for future crash-record lifecycle states:

- `PRELIMINARY` — Submitted; not yet reviewed or accepted
- `ACCEPTED` — Accepted by KCDS; may still be subject to correction
- `CORRECTED` — Amended after initial acceptance; prior version must be preserved in lineage
- `REJECTED` — Rejected by KCDS; reason must be preserved
- `DELETED` — Removed from dataset; reason and prior version must be preserved
- `SUPERSEDED` — Replaced by a correction; prior version remains in lineage
- `AGGREGATE_ONLY` — Record contributed to aggregate statistics but individual record is restricted

### Crash ID stability

**NEEDS VERIFICATION.** Whether KCDS assigns stable crash IDs that persist across corrections, amendments, deletions, and roadway-geometry updates is not established from the public program page. Stable crash-ID semantics are required before any KFM join, deduplication, or lineage claim is made.

### Source lineage after geometry updates

When roadway geometry or geocoding is updated in the road-reference FeatureServer, existing crash location attributions based on prior geometry may change. KFM must preserve:
- The geometry version used at placement time;
- The LRS reference version used to derive coordinates;
- Explicit uncertainty flags on LRS-derived positions;
- A `geometry_source` field distinguishing direct observation from LRS derivation.

### Correction and lineage requirements

- Preliminary records must be clearly marked and must not be promoted as accepted without evidence.
- Corrected records must preserve lineage to prior versions; prior versions must not be silently overwritten.
- Deleted records must be tombstoned, not erased; deletion reason must be preserved.
- Source lineage must be retained when roadway geometry or geocoding is updated.

---

## 6. Inactive candidate SourceDescriptors

The following are **inactive candidate SourceDescriptors** proposed for future governed activation. None is currently registered in `data/registry/sources/`. None confers any access right, admission decision, or publication authority.

> [!IMPORTANT]
> These descriptors are documentation artifacts only. Activation requires separate governed process: rights verification, sensitivity review, policy approval, connector implementation, evidence bundle, and release gate.

### SD-KCDS-ROAD-REF-001 (Candidate — Inactive)

```yaml
# CANDIDATE SourceDescriptor — INACTIVE — do not activate without rights verification
# Path (proposed): data/registry/sources/kansas/kcds-road-ref/descriptor.yaml
source_id: kdot-kcds-road-reference
source_family: kansas
institution: Kansas Department of Transportation (KDOT)
program: Kansas Crash Data System (KCDS)
surface_type: road_reference_geometry
surface_role: authority
native_endpoint: https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Transportation/Kansas_Crash_Data_System_Roads/FeatureServer
endpoint_type: arcgis_feature_server
classification: PUBLIC  # terms NEEDS VERIFICATION before activation
activation_status: INACTIVE
activation_blockers:
  - ArcGIS FeatureServer terms of reuse not verified
  - KDOT GIS redistribution policy not verified
  - Rate limits not verified
  - Geometry update cadence not verified
sensitivity_rank: 0  # road geometry only; no PII
pii: false
crash_incident_data: false  # MUST remain false; this is road reference only
notes: >
  Road network geometry used for KCDS crash-report location placement.
  NOT crash incident data. Mislabeling prohibited.
```

### SD-KCDS-AGGREGATE-001 (Candidate — Inactive — Surface Unverified)

```yaml
# CANDIDATE SourceDescriptor — INACTIVE — surface existence unverified
# Path (proposed): data/registry/sources/kansas/kcds-aggregate/descriptor.yaml
source_id: kdot-kcds-aggregate-statistics
source_family: kansas
institution: Kansas Department of Transportation (KDOT)
program: Kansas Crash Data System (KCDS)
surface_type: aggregate_statistics
surface_role: aggregate
native_endpoint: UNKNOWN — NEEDS VERIFICATION
endpoint_type: UNKNOWN
classification: UNKNOWN
activation_status: INACTIVE
activation_blockers:
  - Surface existence not confirmed from official sources
  - Rights and terms not verified
  - Derivation from KCDS not confirmed
  - Refresh cadence not established
  - Field definitions not verified
sensitivity_rank: 1  # aggregate only; no individual PII if properly aggregated
pii: false  # only if truly aggregated; must be verified
crash_incident_data: false  # aggregate only
notes: >
  If KDOT publishes aggregate crash statistics derived from KCDS, this
  descriptor would cover that surface. Existence and terms are not
  yet verified. Annual crash-statistics reports may pre-date KCDS.
```

### SD-KCDS-INCIDENT-001 (Candidate — DENIED — PII / Law-Enforcement Restricted)

```yaml
# CANDIDATE SourceDescriptor — DENIED — DO NOT ACTIVATE
# This descriptor is recorded for lineage only. Activation is prohibited
# without separate explicit legal authority, rights verification,
# privacy impact assessment, and policy approval.
source_id: kdot-kcds-incident
source_family: kansas
institution: Kansas Department of Transportation (KDOT)
program: Kansas Crash Data System (KCDS)
surface_type: incident_reports
surface_role: observed
native_endpoint: AUTHENTICATED — law-enforcement portal; not publicly accessible
endpoint_type: authenticated_portal
classification: AUTHENTICATED
activation_status: DENIED
activation_blockers:
  - Requires law-enforcement credentials (cannot be created without separate authorization)
  - Contains PII (driver, passenger, pedestrian, witness, officer names/addresses)
  - Contains DPPA-covered motor vehicle information
  - Contains juvenile records (heightened protection)
  - Contains medical outcome data (potential HIPAA applicability)
  - Contains criminal investigation records (KORA active-investigation exemption)
  - Contains precise crash locations (re-identification risk)
  - No public API or bulk export confirmed
  - KORA exemption categories not fully enumerated
  - Privacy impact assessment not performed
  - Policy approval not obtained
sensitivity_rank: 5  # highest — PII + legal restrictions + medical + juvenile + investigation
pii: true
crash_incident_data: true
notes: >
  Individual crash reports in KCDS. Contains PII, DPPA-covered vehicle
  information, juvenile records, medical outcomes, and criminal-investigation
  content. Activation requires: separate legal authority, verified rights,
  privacy impact assessment, data use agreement, policy approval, and
  release gate. This descriptor is documentation of the surface, not
  authorization to access it.
```

---

## 7. Public-safe generalization proposal

> [!IMPORTANT]
> This section is a **proposal requiring explicit policy review** before any implementation. No generalization rule described here is approved or active.

### Spatial generalization

| Data type | Minimum public-safe generalization | Rationale | Policy review required |
|---|---|---|---|
| Individual crash location (precise GPS) | Suppress entirely or generalize to road segment without house-number precision | Precise crash locations can re-identify parties and reveal residence proximity | **Yes — explicit policy approval required** |
| Crash location (county-level aggregate) | County or city/township level may be publishable for aggregate counts | County-level does not re-identify individuals | Yes — confirm with aggregate count thresholds |
| Road segment crash density | Heat-map or density surface at segment level, without date/party overlap | Requires k-anonymity threshold (e.g., minimum 5 crashes per cell) | **Yes — explicit policy approval required** |
| Road-reference geometry (FeatureServer) | May be used at full resolution for road reference if terms permit | Road geometry itself does not contain PII | Yes — terms verification required |

### Temporal generalization

| Data type | Minimum public-safe generalization | Rationale |
|---|---|---|
| Individual crash date/time | Suppress exact time; publish month/year or year only | Date-time plus location plus vehicle type can re-identify parties |
| Aggregate crash counts | Annual or quarterly aggregates, not daily | Daily counts in small areas can isolate individual events |
| Preliminary records | Suppress from public output until accepted | Preliminary records may be corrected or rejected |

### K-anonymity and small-cell suppression

- Any aggregate cell with fewer than **k=5** records (proposed; requires policy decision) must be suppressed.
- Road segments with fewer than the minimum threshold crashes must be suppressed from public-safe density surfaces.
- Combinations of crash characteristics (e.g., time of day + road type + crash type) that narrow to fewer than the threshold must be suppressed.

The exact k threshold requires explicit policy approval from the privacy reviewer and source steward.

### Required public-safe markers

Any future public release derived from KCDS must carry:

1. A clear statement that the data is derived from crash reports and may not reflect all crashes (reporting completeness varies).
2. A not-for-operational-routing or not-for-life-safety disclaimer where applicable.
3. Attribution to KDOT and the KCDS program.
4. The aggregate period and completeness caveats.
5. A link to the current official KDOT crash statistics page rather than KFM-held data being treated as authoritative.

---

## 8. Synthetic fixtures

No live network access was performed for this discovery. The following fixture files are provided for no-network schema and validation testing only.

Fixture location: [`fixtures/synthetic/kcds/`](../../../../fixtures/synthetic/kcds/)

| Fixture file | Content | Purpose |
|---|---|---|
| `road_reference_feature_stub.json` | Synthetic ArcGIS FeatureServer response stub for a road-reference geometry record | Schema-shape validation; does not contain real crash data or real road geometry |
| `source_surface_inventory.yaml` | Machine-readable version of the surface inventory table (§1) | Documentation fixture; tooling validation |

> [!CAUTION]
> Synthetic fixtures represent invented data for schema testing only. They are not real KCDS data, not real road geometry, and not evidence of any KCDS surface being publicly accessible. No fixture implies that the corresponding data surface is activated or that access is authorized.

---

## 9. Threat model

### Threat categories

| Threat | Description | Mitigation |
|---|---|---|
| **Credential exposure** | Law-enforcement KCDS/KLER credentials obtained or simulated | No credentials created; no authenticated access; connectors blocked until separate authorization |
| **Personal data ingestion** | Incident-level crash records (containing PII) ingested without authority | Incident-level surfaces denied; all `AUTHENTICATED` surfaces blocked |
| **Unauthorized inference** | Combining road-reference geometry with other public data to infer crash locations or parties | Road-reference geometry is road network only; crash occurrence data not ingested; spatial generalization required |
| **Precise location exposure** | GPS-level crash coordinates published, enabling party re-identification or residence inference | Precise locations fail-closed; spatial generalization required before any public release |
| **Stale/corrected record presentation** | Preliminary or corrected crash records presented as accepted/final | Lifecycle states tracked; preliminary records suppressed; correction lineage required |
| **Driver's Privacy Protection Act (DPPA) violation** | Motor vehicle owner or driver information published without statutory authority | All vehicle/driver PII fail-closed; DPPA applicability noted explicitly |
| **Juvenile record exposure** | Records involving persons under 18 published | Juvenile fields fail-closed; heightened legal protection noted |
| **Medical data exposure** | Injury severity, transport, or outcome data published at record level | Medical fields fail-closed; HIPAA applicability noted |
| **Criminal investigation disclosure** | Active-investigation records published in violation of KORA exemption | Investigation-context fields fail-closed; KORA active-investigation exemption applies |
| **Source mislabeling** | Road-reference FeatureServer mislabeled as a crash-incident dataset | Explicit caution in this document and in every future artifact referencing the FeatureServer |
| **Aggregate re-identification** | Aggregate statistics published with cells small enough to identify individuals | k-anonymity threshold required; small-cell suppression required |
| **Terms violation** | ArcGIS FeatureServer or KDOT GIS data consumed at scale without verified terms | Terms verification required before any FeatureServer ingestion |
| **Timing attack** | Daily or near-real-time publication of crash counts enabling inference of individual events | Temporal generalization to monthly/quarterly aggregates required |
| **Cross-source join** | KCDS crash locations joined with parcel, utility, or other identity-rich data | Cross-membrane join inherits most-restrictive posture; crash data joins are effectively denied pending policy |

### Fail-closed defaults

All KCDS surfaces default to the most restrictive classification until rights and privacy review explicitly permits a less restrictive classification:

- Incident-level data: `DENIED`
- Any PII field: `DENIED`
- Precise locations: `DENIED`
- Any juvenile field: `DENIED`
- Medical outcome: `DENIED`
- Active investigation fields: `DENIED`
- Vehicle owner / driver information: `DENIED` (DPPA applies)
- Road-reference geometry (FeatureServer): `INACTIVE` — pending terms verification (not denied, but not active)
- Aggregate statistics: `INACTIVE` — pending surface existence and terms verification

---

## 10. Go/no-go recommendations

| Surface | Recommendation | Rationale | Pre-conditions for Go |
|---|---|---|---|
| KCDS road-reference FeatureServer | **CONDITIONAL GO** (pending terms) | Public ArcGIS endpoint; road geometry only; no PII | Verify ArcGIS/KDOT terms of reuse; confirm redistribution rights; verify rate limits; confirm no crash-incident data is returned |
| KCDS aggregate statistics | **HOLD** | Surface existence not verified | Confirm surface exists; obtain official URL; verify rights; confirm derivation from KCDS vs. predecessor systems; verify k-anonymity |
| KCDS web-entry portal | **NO GO** | Law-enforcement authenticated; outside discovery scope | Separate legal authority; data use agreement; privacy impact assessment; explicit policy approval; KFM governance authorization |
| KLER submission portal | **NO GO** | Law-enforcement authenticated; same gates as above | Same as web-entry portal |
| KCDS incident-level database | **NO GO** | PII + DPPA + juvenile + medical + investigation; multiple fail-closed gates | All of the above plus explicit KFM governance decision and public-safety policy review |
| KCDS XML schema / spec documentation | **HOLD** | Existence and public availability not verified | Confirm official URL; verify terms; assess whether schema publication constitutes data admission |
| MMUCC mapping documentation | **HOLD** | MMUCC is a federal standard; KCDS-specific alignment documentation not verified | Verify KDOT/KCDS-specific MMUCC alignment document; MMUCC itself (federal) may be separately reusable |
| KDOT historical crash statistics reports | **HOLD** | Pre-KCDS reports may be available; derivation from KCDS unclear | Confirm official URL; verify that KCDS-era vs. pre-KCDS reports are distinguishable; verify rights |

### Summary disposition

```
Road-reference geometry:  CONDITIONAL GO — terms must be verified first
Aggregate statistics:     HOLD — surface must be confirmed
Incident-level records:   NO GO — multiple hard blockers (PII, DPPA, juvenile, medical, investigation)
Authenticated portals:    NO GO — out of scope; separate authorization required
XML schemas / docs:       HOLD — existence and terms must be confirmed
```

---

## 11. Open questions

| ID | Question | Priority | Who resolves |
|---|---|---|---|
| OPEN-KCDS-01 | What are the exact terms of use for the KCDS road-reference FeatureServer? Is KDOT's ArcGIS published under an explicit open-government license? | High | Rights reviewer + KDOT official contact |
| OPEN-KCDS-02 | Does KDOT publish aggregate crash statistics derived from KCDS? What URL, cadence, and format? | High | Kansas source steward + KDOT program page review |
| OPEN-KCDS-03 | What are the complete KORA exemption categories applicable to KCDS crash records? | High | Rights reviewer + legal review |
| OPEN-KCDS-04 | Are KCDS XML schemas or data dictionaries publicly available for download? What are their terms? | Medium | Kansas source steward + KDOT/KHP contact |
| OPEN-KCDS-05 | Does KCDS align with MMUCC? Is a KCDS-specific MMUCC crosswalk document publicly available? | Medium | Roads/Rail/Trade steward |
| OPEN-KCDS-06 | Are KCDS crash IDs stable across corrections, amendments, and deletions? | Medium | Roads/Rail/Trade steward + KDOT documentation |
| OPEN-KCDS-07 | What coordinate reference system does the road-reference FeatureServer use? What geometry types are returned? | Medium | Roads/Rail/Trade steward (can be confirmed from FeatureServer metadata without ingestion) |
| OPEN-KCDS-08 | Does KDOT provide an aggregate crash dashboard? If so, what URL? | Low | Kansas source steward |
| OPEN-KCDS-09 | What was the predecessor system to KCDS? Are predecessor aggregate statistics still available and distinguishable from KCDS-era data? | Low | Kansas source steward + KDOT program history |
| OPEN-KCDS-10 | Does the DRIVER's Privacy Protection Act (DPPA) apply to crash report data obtained from KCDS, or only to motor-vehicle-record sources? | High | Legal review |
| OPEN-KCDS-11 | What is the exact KCDS FeatureServer field schema (field names, types, domain values)? Can this be obtained from the public endpoint metadata without constituting data ingestion? | Medium | Roads/Rail/Trade steward (ArcGIS `/layers` endpoint) |
| OPEN-KCDS-12 | Is the rate limit on the public FeatureServer sufficient for background monitoring, or does it require a separate agreement? | Medium | Rights reviewer + technical review |
| OPEN-KCDS-13 | What k-anonymity threshold does KDOT apply (or would approve) for public aggregate crash-count releases? | High | Privacy reviewer + KDOT policy contact |

---

## Rollback

### Before merge

Close the draft pull request and abandon the branch. This document is the first bounded deliverable and may be merged after human review. It does not create a connector, activation, or publication path.

### After merge

Revert only the scoped discovery documentation through a reviewed pull request. Do not delete evidence of corrected source classifications. Do not rewrite history.

If any fact in this document is found to be incorrect after merge:
1. Open a correction issue citing the specific factual error and its official-source evidence.
2. Submit a documentation correction PR updating only the affected section.
3. Preserve prior incorrect statements in a correction note; do not silently overwrite.

[Back to top](#top)
