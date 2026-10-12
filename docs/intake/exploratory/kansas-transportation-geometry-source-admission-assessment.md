<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/kansas-transportation-geometry-source-admission-assessment
title: Kansas transportation geometry source-admission assessment
type: exploratory-source-admission-assessment
version: v1.0
status: proposed; no-ingest; no-source-activation
owners:
  - "@bartytime4life — verified repository review route"
  - "OWNER_TBD — transportation source steward"
  - "OWNER_TBD — rights and sensitivity reviewer"
created: 2026-08-15
updated: 2026-08-15
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
owning_root: docs/
responsibility: >-
  Reconcile official Kansas transportation geometry, linear-referencing, mobile
  LiDAR, and supporting catalog surfaces into finite non-promotional source
  admission dispositions without ingesting, copying, normalizing, or publishing
  source data.
current_path: docs/intake/exploratory/kansas-transportation-geometry-source-admission-assessment.md
related:
  - docs/adr/ADR-0017-source-descriptor-admission-process.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - policy/source/
  - policy/rights/
  - policy/sensitivity/
  - docs/domains/roads-rail-trade/
  - docs/domains/settlements-infrastructure/
  - docs/registers/VERIFICATION_BACKLOG.md
tags: [kansas, kdot, k-hub, lrs, ng911, lidar, source-admission, transportation]
notes:
  - "The assessment authorizes no ingest, connector, schedule, lifecycle transition, road-authority decision, release, or publication."
  - "Official service metadata was inspected on 2026-08-15; no bulk feature payload was downloaded or retained."
  - "Geometry authority, attribute authority, observation authority, and catalog stewardship remain separate."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas transportation geometry source-admission assessment

> **Assessment result.** Admit the NG911 road centerline and KDOT K-Hub/LRS
> services as **reference candidates only**. Hold evaluation snapshots until
> rights, update semantics, identifier lifecycle, and public-safe precision are
> closed. Hold mobile LiDAR derivatives because authentication, product rights,
> precision, and stable snapshot behavior remain incomplete. Admit DASC catalog
> and administrative products only as supporting reference candidates, never as
> substitutes for transportation geometry authority.

> [!IMPORTANT]
> No result in this document creates an accepted `SourceDescriptor`, network
> connector, ingest receipt, lifecycle transition, road identity authority,
> release, deployment, publication, or public-use permission.

## Evidence checkpoint

| Field | Value |
| --- | --- |
| Repository baseline | `main@0dcc2e4cc6d2257a7a389acd00d67d420af1ae13` |
| Assessment date | 2026-08-15 |
| Official services inspected | DASC NG911 Road Centerline; KDOT State System KUPS/K-Hub LRS; KDOT GIS and mobile LiDAR guidance; DASC sharing guidance |
| Payload handling | Metadata inspection only; no bulk source payload retained |
| Current implementation authority | None |
| Overall posture | `REFERENCE_CANDIDATES / SNAPSHOT_HOLD / NO_INGEST` |

Official evidence indicates that KDOT is retiring the former CANSYS linear
referencing system, placing crash locations on K-Hub/LRS, developing a permanent
ground-based imagery and LiDAR program, and aligning non-state road geometry to
NG911 road centerlines for later change detection.

The DASC NG911 service identifies the Kansas PSAPs, NG911 Coordinating Council,
and DASC as the service copyright/stewardship context. Its Road Centerline layer
is a queryable polyline feature layer with JSON and GeoJSON output, pagination,
a 1,000-record maximum response, source spatial reference EPSG:3395, stewardship
and effective-date fields, `NGSEGID`, `LRSKEY`, and related road attributes.

The KDOT State System KUPS service describes the county route network as the
route reference for public highways and non-state roads in Kansas. Its layer is
a queryable polyline feature layer with JSON, GeoJSON, and PBF output, a
2,000-record maximum response, source spatial reference WKID 6923, route and
event identifiers, measures, LRS date fields, edit timestamps, `GlobalID`, and
location-source/error attributes.

KDOT's mobile LiDAR download guidance requires an ArcGIS Online or KanPlan
account for GIS extracts. That access surface does not, by itself, establish
redistribution rights, public-safe precision, stable revision identity, or
unattended KFM retrieval authority.

## Finite disposition vocabulary

| Outcome | Meaning |
| --- | --- |
| `ADMIT_REFERENCE_CANDIDATE` | Official metadata is sufficient to design a later `SourceDescriptor`; no ingest or snapshot is authorized. |
| `ADMIT_SNAPSHOT_CANDIDATE` | A bounded immutable evaluation snapshot may be proposed in a separate reviewed change. |
| `HOLD` | Rights, identity, cadence, precision, reproducibility, authority, or operational evidence is incomplete. |
| `DENY` | The source conflicts with KFM authority, rights, sensitivity, reproducibility, or correction requirements. |

## Lane assessment

| Lane | Geometry role | Attribute or observation role | Disposition | Blocking evidence |
| --- | --- | --- | --- | --- |
| DASC NG911 Road Centerline | Candidate primary geometry for roads not maintained by KDOT; statewide emergency-addressing context | Stewardship, effective/expiration dates, addressing, road classification, and candidate LRS crosswalk attributes | `ADMIT_REFERENCE_CANDIDATE` | Layer-level license/redistribution terms, revision/snapshot identity, identifier lifecycle, precision review, and complete update semantics remain unverified |
| KDOT K-Hub / State System KUPS LRS | Candidate state/public-highway route and measure reference | Route system, event identity, measures, LRS validity dates, source and edit metadata | `ADMIT_REFERENCE_CANDIDATE` | Public download rights, stable consumer contract, edit capability boundary, identifier supersession, authoritative designation, and snapshot semantics remain incomplete |
| KDOT mobile LiDAR derivatives | Candidate transportation observation or derived-asset source, not road-network authority | Extracted approaches, assets, surfaces, and other collection-specific observations | `HOLD` | Account-based access, product-level rights, exact precision, collection/version identity, derivative methodology, download automation, and redistribution remain unresolved |
| DASC catalog and administrative products | Supporting catalog, stewardship, and boundary reference | Discovery, metadata, official-boundary context, archival and steward routing | `ADMIT_REFERENCE_CANDIDATE` | Each selected product still requires its own authoritative designation, rights, version, CRS, and correction evidence |

No lane inherits authority from another. In particular:

- NG911 geometry does not become KDOT-maintained-road authority;
- K-Hub route identity does not automatically authorize NG911 addressing
  attributes;
- LiDAR observations do not replace road-network or route authority;
- a DASC catalog listing does not prove semantic, legal, or operational
  admission; and
- matching identifiers do not prove stable one-to-one crosswalks.

## Candidate endpoint inventory

### NG911 road centerlines

- Service:
  `https://services.kansasgis.org/arcgis4/rest/services/NG911/NG911/MapServer`
- Layer:
  `https://services.kansasgis.org/arcgis4/rest/services/NG911/NG911/MapServer/1`
- Layer ID: `1`
- Geometry: `esriGeometryPolyline`
- Source CRS: EPSG:3395
- Maximum response: 1,000 records
- Query formats: JSON and GeoJSON
- Advanced query capabilities include pagination, ordering, distinct values,
  statistics, datum transformation, distance, and extent queries.
- High-value candidate fields include `STEWARD`, `L_UPDATE`, `EFF_DATE`,
  `EXP_DATE`, `NGSEGID`, `LRSKEY`, `UPDATEBY`, road-name components,
  jurisdiction fields, status, surface, travel, and authority flags.

A later evaluation query must pin `where`, `outFields`, geometry behavior,
`outSR`, ordering, `resultOffset`, `resultRecordCount`, response format,
retrieval time, source metadata digest, payload digest, and observed count.

### KDOT K-Hub / LRS

- Service:
  `https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/APPS/State_System_KUPS/MapServer`
- Layer:
  `https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/APPS/State_System_KUPS/MapServer/0`
- Layer ID: `0`
- Service item ID: `724140867d6e40a793cca30d01bcb8e1`
- Geometry: `esriGeometryPolyline`
- Source CRS: WKID 6923, NAD 1983 Kansas LCC feet
- Maximum response and selection: 2,000 records
- Query formats: JSON, GeoJSON, and PBF
- Candidate identifiers and temporal fields include `RouteID`, `EventID`,
  `GlobalID`, `FromMeasure`, `ToMeasure`, `InventoryStartDate`, `LRSFromDate`,
  `LRSToDate`, `CreatedDate`, and `LastEditedDate`.

The service metadata reports that the fourth `RouteID` character distinguishes
route systems. KFM must test that rule against captured records and correction
history before using it in deterministic identity.

### KDOT mobile LiDAR

The KDOT GIS resources page links a Mobile LiDAR Project Data Portal. Current
download guidance lists collection-specific GIS extracts, including 2021 and
2023 products, and requires an ArcGIS Online or KanPlan account for extract
downloads.

Before this lane can become a snapshot candidate, KFM needs:

- product and collection identifiers;
- rights, license, attribution, and redistribution terms;
- source and derivative CRS, precision, and generalization;
- collection date versus publication/update date;
- extraction methodology and quality statements;
- stable archive/download URLs or approved captured responses;
- authentication and unattended-access authorization;
- public-safe precision and infrastructure-exposure review; and
- correction, withdrawal, and supersession behavior.

### DASC supporting products

DASC sharing guidance requires designated stewards, maintained authoritative
content, metadata, discoverability, and recurring quality review. Supporting
administrative or catalog products may be admitted only when they are necessary
to interpret transportation sources and their own admission evidence closes.

## Identifier and crosswalk assessment

### `NGSEGID` and `NGKSSEGID`

These are candidate NG911 segment identities. Their field presence and lengths
are confirmed from service metadata. Permanence, reuse, merge/split behavior,
county reassignment, and correction semantics are not established.

### `LRSKEY`

The NG911 road layer exposes `LRSKEY`, but field presence alone does not prove
that every feature is populated, current, unique, stable, or semantically
equivalent to K-Hub route identity.

### `RouteID`, `EventID`, and `GlobalID`

K-Hub exposes route, event, and global identifiers plus measure and validity
dates. KFM must distinguish route identity from event identity and object-store
identity. `GlobalID` must not become a cross-system semantic key without
evidence.

### Required crosswalk proof

A later synthetic profile must model:

- one-to-one matches;
- one K-Hub route to multiple NG911 segments;
- one NG911 segment intersecting multiple route events;
- split, merge, retire, replace, and corrected identifiers;
- missing or conflicting keys;
- temporal non-overlap;
- geometry disagreement above a declared tolerance; and
- independent geometry, attribute, and observation authority.

Unknown or contradictory matches return `HOLD` or `DENY`; they do not select a
winner by proximity alone.

## Rights, sensitivity, and public-safe handling

Current official service availability is not sufficient redistribution
authority. Before snapshots:

1. obtain or record explicit license/rights evidence for each lane;
2. record attribution and downstream redistribution obligations;
3. classify infrastructure and emergency-addressing exposure;
4. define whether exact road, measure, asset, or LiDAR precision may be public;
5. prevent private-account credentials or session material from entering KFM
   receipts or logs;
6. retain only public-safe synthetic fixtures until rights close; and
7. route uncertainty to `HOLD`.

## Reproducible evaluation packet

A future snapshot proposal must contain:

- exact service URL, layer ID, query parameters, output format, and source CRS;
- source metadata JSON and SHA-256 digest;
- response retrieval time and source-reported update/validity values;
- stable ordering and pagination proof;
- response payload digest and record count;
- finite handling for duplicate pages, changing counts, timeouts, rate limits,
  authentication, unsupported transformations, and partial responses;
- a source descriptor candidate that remains unadmitted;
- tuple-level lineage from source fields to proposed KFM fields;
- sensitivity and rights decisions;
- correction/supersession links; and
- a rollback that removes only the evaluation snapshot and derived candidates.

## Smallest dependency-closed next slice

Create a no-network synthetic `KansasTransportationGeometrySourceAssessment`
profile with four lanes and exact outcomes. It should validate endpoint identity,
source role, CRS declaration, pagination limits, identifier-role separation,
rights/sensitivity prerequisites, crosswalk uncertainty, and all governance
effects fixed false.

The first live follow-up may capture metadata and a count-only result. It must
not retrieve statewide geometry until explicit snapshot-candidate review closes.

## Validation

A later implementation should include:

- positive and negative synthetic fixtures for all four dispositions;
- malformed endpoint, unpinned layer, unknown CRS, missing rights,
  authentication-required, identifier-conflict, precision-risk, and
  source-role-collapse cases;
- deterministic no-network tests;
- workflow-security and topology checks;
- generated-receipt integrity; and
- explicit proof that no connector, schedule, lifecycle write, release, or
  publication path is introduced.

## Non-effects

This assessment does not:

- admit a source or descriptor;
- execute or schedule a live query;
- download geometry or LiDAR;
- copy source records into KFM lifecycle storage;
- authenticate a steward, identifier, or rights claim;
- decide a canonical road geometry or K-Hub/NG911 crosswalk;
- expose crash, emergency-response, protected infrastructure, or account data;
- release, deploy, publish, or change repository settings.

## Change history

| Version | Date | Change |
| --- | --- | --- |
| `v1.0` | 2026-08-15 | Initial four-lane evidence-backed source-admission assessment. |

[Back to top](#top)
