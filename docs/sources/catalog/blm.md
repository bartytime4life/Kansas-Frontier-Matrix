<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/sources-catalog-blm
title: Bureau of Land Management Source Catalog Profile
type: source_catalog_profile
version: v0.1
status: draft
owners: <PLACEHOLDER — Source steward · Docs steward · Catalog profile owner>
created: 2026-06-12
updated: 2026-06-12
policy_label: public
related:
  - docs/sources/catalog/README.md
  - docs/sources/catalog/CROSSWALKS.md
  - docs/sources/catalog/IDENTITY.md
  - docs/sources/catalog/GLOSSARY.md
  - docs/sources/catalog/OPEN-QUESTIONS.md
  - docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/truth-posture.md
  - docs/governance/separation-of-duties.md
  - schemas/contracts/v1/source/
tags: [kfm, sources, catalog, blm, bureau-of-land-management, doi, federal, public-lands, plss, cadastral, geospatial, arcgis, land-records]
notes:
  - "v0.1 — Initial BLM source catalog profile for governed KFM ingestion, evidence use, and public-release boundaries."
  - "This profile describes source use. It does not authorize direct public-client reads from BLM systems."
] -->

# Bureau of Land Management Source Catalog Profile

Path: `docs/sources/catalog/blm.md`

## 1. Purpose

This document defines the Kansas Frontier Matrix (KFM) source-catalog profile for the **U.S. Bureau of Land Management (BLM)**.

BLM sources are useful to KFM for federal land, land-status, cadastral, Public Land Survey System (PLSS), public-land access, and selected public geospatial reference layers. Within KFM, BLM data must be treated as governed upstream source material that enters the KFM lifecycle through source descriptors, ingestion receipts, validation, EvidenceBundles, catalog records, triplets, graph records, and released artifacts.

This profile prevents BLM material from being used as an ungoverned shortcut around KFM doctrine.

## 2. Source identity

| Field | Value |
|---|---|
| Source family | Federal land-management and geospatial source |
| Steward organization | U.S. Department of the Interior — Bureau of Land Management |
| Common abbreviation | BLM |
| KFM source profile id | `source-profile:blm` |
| Recommended source id prefix | `source:blm:` |
| Primary KFM domains | `sources`, `catalog`, `map`, `land`, `cadastral`, `federal-records`, `evidence` |
| Main access modes | BLM Geospatial Business Platform Hub, BLM ArcGIS REST services, BLM land-record portals, BLM map viewers, downloadable public datasets |
| Public-client access posture | Public clients may use only KFM released artifacts, governed APIs, tile services, and policy-safe runtime envelopes. They must not read BLM raw endpoints directly. |

## 3. KFM authority posture

BLM can be authoritative for records and datasets that BLM publishes, maintains, or designates as official for its own programs. BLM is not automatically authoritative for all land, all parcels, all access rights, all environmental conditions, all cultural resources, or all county-level administrative facts.

### 3.1 Use BLM as `primary` when

Use BLM as a primary source only for BLM-published records or datasets within BLM authority, such as:

- BLM-managed public-land geospatial layers.
- BLM National PLSS / CadNSDI layers where the BLM dataset is the cited cadastral reference.
- BLM land-status or federal land-record products published by BLM.
- BLM surface-management or federal-interest datasets where the BLM service metadata identifies the dataset as the relevant BLM-managed source.
- BLM public-land access datasets published by BLM.
- BLM recreation, range, fire, vegetation, transportation, wildlife, and land layers that are explicitly public and described as BLM products.

### 3.2 Use BLM as `corroborating` when

Use BLM as corroborating support when a KFM claim also depends on another authority, including:

- County parcel ownership or tax records.
- County road status and maintenance responsibility.
- Local zoning, permitting, or land-use restrictions.
- State transportation, hydrology, wildlife, or conservation datasets.
- Historic interpretation that requires archives, local records, or scholarly sources.
- County Focus Mode claims involving access, ownership, or operational restrictions.

### 3.3 Use BLM as `context` when

Use BLM as contextual background when the record helps orient the map but does not itself prove the final KFM claim, including:

- Regional federal land context.
- National conservation or wilderness overlay context.
- PLSS township/range/section reference grids used as map context.
- Historic General Land Office reference material used to support narrative context.
- Broad federal land-management program descriptions.

### 3.4 Use BLM as `restricted` or fail closed when

Treat BLM-derived material as restricted or fail closed when it includes or implies:

- Sensitive archaeology, burial, sacred, tribal, or cultural-resource locations.
- Sensitive ecology, species, habitat, nest, den, cave, or collection-site locations.
- Law-enforcement, emergency-response, or infrastructure vulnerability information.
- Unreleased, non-public, internal, provisional, or draft BLM layers.
- Fine-grained site records whose public display could increase harm.
- Access routes, easements, or administrative roads where public right of access is uncertain.
- Any record marked as requiring review before public release.

## 4. Kansas relevance

KFM is Kansas-centered. BLM coverage in Kansas must be handled carefully.

BLM is highly relevant to Kansas for:

- PLSS township/range/section reference.
- Federal land patent and General Land Office history.
- Cadastral reference material.
- Some federal-interest, mineral, land-status, or administrative records.
- Cross-state federal land-management context.

BLM should not be treated as a replacement for Kansas county records, Kansas state agency data, local road authorities, Register of Deeds records, county GIS parcels, county emergency notices, or local field verification.

For Kansas county Focus Mode, BLM usually serves one of these roles:

1. **Cadastral reference layer** for PLSS context.
2. **Historic land-record source** for federal conveyance and survey history.
3. **Federal land-status corroborator** where federal interests appear.
4. **Context source** for national land-management categories.

## 5. Canonical access points

The following access points are recognized by this profile. Their availability, service structure, layer names, formats, and metadata must be verified during each source refresh.

| Handle | Use | KFM treatment |
|---|---|---|
| `blm:gbp-hub` | BLM Geospatial Business Platform Hub for searching, viewing, and downloading BLM public geospatial data. | Prefer for human review, dataset discovery, landing-page metadata, and governed dataset acquisition. |
| `blm:arcgis-rest` | BLM ArcGIS REST service directory and service-layer endpoints. | Use for machine-readable service metadata and governed ingestion jobs. Never expose raw REST dependency directly to public clients. |
| `blm:land-records` | BLM land-record entry points, including federal land conveyance, survey plat, and field-note access paths. | Use as evidence source for federal land-record claims. Normalize into EvidenceBundles. |
| `blm:maps` | BLM map viewers and public map products. | Use for discovery and manual verification. Do not scrape viewer-only state when downloadable or service-backed data exists. |
| `blm:glo-records` | General Land Office record access path from BLM land-records pages. | Use for historic title, patent, survey plat, and field-note references where applicable. |
| `blm:mlrs` | Mineral & Land Records System access path from BLM land-records pages. | Use only for governed records workflows and with careful authority labeling. |

## 6. Example dataset families

BLM publishes many layers and services. This profile does not whitelist every layer. Instead, it defines dataset families that can be considered by a KFM source steward.

| Dataset family | Example KFM use | Default source role | Risk posture |
|---|---|---:|---|
| PLSS / CadNSDI | Township, range, section, special survey, cadastral reference overlays | `primary` for BLM PLSS dataset; `context` for map orientation | Moderate; validate geometry, vintage, and local fit |
| Surface Management Agency | Federal surface-management context | `primary` for BLM-published SMA layer; `corroborating` for local land-status claims | Moderate; scale and generalization matter |
| Public Land Access Data | Federal-interest access references | `primary` only for BLM-published access dataset content; `corroborating` for route legality | High; access claims can mislead users |
| National Conservation Lands / NLCS | National monument, NCA, wilderness, WSA, and similar public overlays | `primary` for BLM-published BLM designation boundaries | High when tied to sensitive sites |
| Recreation | BLM recreation-site and route context | `primary` only for BLM-published BLM recreation assets | High; closures, fees, and access may change |
| Fire | BLM fire-management and incident-context layers | `context` or `corroborating` unless source clearly defines authority | High; stale operational data can be dangerous |
| Range / grazing | Grazing allotment or range program context | `primary` for BLM-published BLM allotment data; otherwise `context` | High; private/operational implications |
| Vegetation / wildlife | Resource-management context | usually `context`; sometimes `restricted` | Very high; sensitive ecology must fail closed |
| Lands / realty | Federal interests, withdrawals, reservations, easements, rights-of-way | `primary` for BLM-published federal land-status facts; `corroborating` for public access | High; legal interpretation required |
| Historic land records | Land patents, plats, field notes, survey history | `primary` for BLM record existence; `context` for interpretation | Moderate; interpretation requires caution |

## 7. KFM lifecycle requirements

BLM material must follow the KFM source lifecycle.

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET / GRAPH → PUBLISHED
```

### 7.1 RAW

RAW storage may contain downloaded files, REST metadata snapshots, service JSON, export packages, or land-record documents. RAW material is not public-facing.

Requirements:

- Preserve original filenames, request URLs, timestamps, response headers when available, and checksums.
- Preserve service metadata separately from feature payloads.
- Record access date and source handle.
- Capture license/public-domain posture as a claim to verify, not an assumption.
- Store full BLM service descriptions and layer metadata where available.

### 7.2 WORK

WORK storage may contain normalized intermediate files, projections, clipped county extracts, schema-mapping outputs, QA outputs, and draft crosswalks.

Requirements:

- Do not publish WORK outputs.
- Mark geometry operations clearly: clip, dissolve, simplify, reprojection, centroid, tile generation, attribute pruning.
- Keep BLM original identifiers alongside KFM local identifiers.
- Track any lossy transformation.
- Quarantine uncertain access, sensitive-resource, or unclear-authority records.

### 7.3 QUARANTINE

Quarantine BLM-derived material when:

- Metadata is missing or contradictory.
- A dataset appears public but contains protected, sensitive, or review-required information.
- A record’s public display could expose sensitive ecology, archaeology, tribal, burial, sacred, or security information.
- Geometry is too coarse or too generalized for the intended KFM claim.
- The layer’s service metadata says it is optimized for online performance and not official legal geometry.
- The record could imply public access where public access has not been verified.
- The dataset’s authority overlaps with county, state, tribal, or private records.

### 7.4 PROCESSED

Processed BLM-derived datasets must include:

- Normalized schema.
- KFM source descriptor.
- EvidenceBundle linkage.
- Policy classification.
- Transform receipt.
- QA report.
- Geometry validity report.
- Attribution statement.
- Update cadence.
- Staleness rules.
- Confidence and source-role labels.

### 7.5 CATALOG / TRIPLET / GRAPH

Only processed, validated, policy-labeled records may produce:

- Catalog records.
- Entity records.
- Spatial feature records.
- Triplets.
- Graph edges.
- Tile-build inputs.
- Public API payload candidates.

Triplets and graph records must never claim more authority than the BLM source supports.

### 7.6 PUBLISHED

Publication is a governed state transition. A BLM-derived artifact may be published only after:

- Source descriptor exists.
- EvidenceBundle exists.
- Policy label is assigned.
- Sensitive data review is complete.
- Attribution is present.
- Update/staleness rule is defined.
- Public API or tile envelope is generated from released KFM artifacts.
- Public-client runtime cannot bypass KFM and read RAW, WORK, QUARANTINE, canonical internal stores, or live BLM endpoints directly.

## 8. Source descriptor baseline

Use this as the starting point for a source descriptor. Adjust fields to match the current `source_descriptor` schema.

```yaml
id: source:blm
title: Bureau of Land Management
short_title: BLM
source_profile: source-profile:blm
agency:
  name: Bureau of Land Management
  parent: U.S. Department of the Interior
source_type: federal_geospatial_and_land_records
default_role: primary
role_guidance:
  primary:
    - BLM-published records and datasets within BLM authority.
    - BLM National PLSS and cadastral datasets where BLM is the stated steward.
    - BLM public land, land-status, and federal-interest datasets where BLM metadata supports the claim.
  corroborating:
    - County parcel, access, road, zoning, or ownership claims requiring local or state authority.
    - Kansas county Focus Mode claims where BLM is not the final authority.
  context:
    - PLSS reference grid overlays.
    - Regional public-land context.
    - Historic General Land Office background.
  restricted:
    - Sensitive ecology, archaeology, tribal, burial, sacred, security, or unreleased data.
jurisdiction:
  country: US
  focus_region: Kansas and relevant federal public-land states
access:
  handles:
    - blm:gbp-hub
    - blm:arcgis-rest
    - blm:land-records
    - blm:maps
    - blm:glo-records
    - blm:mlrs
policy:
  public_client_direct_read: false
  cite_or_abstain: true
  sensitive_topics_fail_closed: true
  publication_requires_evidence_bundle: true
  publication_requires_policy_review: true
refresh:
  default_cadence: quarterly
  high_volatility_cadence: monthly_or_event_driven
  stale_after_days: 120
quality:
  require_metadata_snapshot: true
  require_checksum: true
  require_geometry_validation: true
  require_schema_crosswalk: true
  require_attribution: true
```

## 9. Dataset-level descriptor extension

Each BLM dataset or service layer should receive its own dataset-level descriptor. Do not rely on this profile alone.

Recommended id pattern:

```text
source:blm:<program-or-theme>:<dataset-or-layer-slug>
```

Examples:

```text
source:blm:cadastral:plss-cadnsdi
source:blm:lands:surface-management-agency
source:blm:lands:public-land-access-data
source:blm:lands:nlcs-generalized
source:blm:land-records:glo-patents
source:blm:land-records:survey-plats
```

Minimum dataset-level fields:

```yaml
id: source:blm:<theme>:<dataset>
parent_profile: source-profile:blm
title: <official dataset or service title>
source_role: <primary|corroborating|context|restricted>
source_handle: <blm:gbp-hub|blm:arcgis-rest|blm:land-records|...>
accessed_at: <ISO-8601 timestamp>
source_landing_page: <URL or registry pointer>
service_endpoint: <URL or registry pointer>
metadata_endpoint: <URL or registry pointer>
download_endpoint: <URL or registry pointer>
spatial_coverage: <national|state|county|custom geometry>
temporal_coverage: <as stated by source>
update_frequency: <as stated by source or unknown>
license_or_use_statement: <as stated by source>
public_release_review:
  required: true
  status: pending
sensitive_data_review:
  required: true
  status: pending
geometry_policy:
  may_tile_publicly: false
  requires_simplification_review: true
  requires_scale_warning: true
evidence:
  evidence_bundle_id: <KFM EvidenceBundle id>
  receipt_id: <KFM receipt id>
```

## 10. Identity and crosswalk policy

BLM identifiers must be preserved. KFM identifiers must be deterministic and separate.

### 10.1 Preserve source identifiers

Preserve source fields such as:

- Service name.
- Layer id.
- Layer name.
- Object id or feature id.
- Global id where provided.
- Dataset title.
- Dataset item id where provided.
- Program or theme path.
- Official record number, accession number, patent number, serial number, or document id where applicable.
- PLSS identifiers such as principal meridian, township, range, section, aliquot part, special survey identifier, or related cadastral fields.

### 10.2 Create KFM identifiers

KFM identifiers should be generated deterministically from source and geometry/record fields.

Recommended pattern:

```text
kfm:feature:blm:<theme>:<normalized-source-key>
kfm:record:blm:<record-family>:<normalized-source-key>
kfm:evidence:blm:<dataset>:<receipt-hash>
```

### 10.3 Crosswalk requirements

Create or update crosswalk records when BLM data connects to:

- County parcels.
- County road centerlines.
- Kansas state agency records.
- USGS, USDA, FEMA, NPS, USFS, EPA, or other federal datasets.
- Historic map features.
- KFM Focus Mode county entities.
- KFM EvidenceBundle records.

Crosswalks must include directionality and authority posture.

Example:

```yaml
crosswalk_id: crosswalk:blm-plss:kfm-county-section:<hash>
from:
  source: source:blm:cadastral:plss-cadnsdi
  key: <BLM PLSS key>
to:
  source: kfm:county-focus:<county>
  key: <KFM county section feature id>
relationship: same_or_overlapping_reference_area
authority_posture: BLM is cadastral reference; county/local records may govern parcel ownership and local access.
confidence: <low|medium|high>
evidence_bundle_id: <EvidenceBundle id>
```

## 11. EvidenceBundle mapping

Every BLM-derived public claim must point to an EvidenceBundle.

Minimum EvidenceBundle fields for BLM material:

```yaml
evidence_bundle_id: evidence:blm:<dataset>:<hash>
claim:
  text: <precise claim supported by BLM source>
  scope: <geometry|record|attribute|relationship|context>
source:
  source_id: source:blm:<theme>:<dataset>
  source_profile: source-profile:blm
  source_role: <primary|corroborating|context|restricted>
  accessed_at: <ISO-8601 timestamp>
  source_title: <official source title>
  source_steward: Bureau of Land Management
  source_handle: <handle>
lineage:
  raw_receipt_id: <receipt id>
  transform_receipt_id: <receipt id>
  validation_receipt_id: <receipt id>
policy:
  public_release: <allowed|denied|requires_review>
  sensitive_review: <passed|failed|pending>
  redaction: <none|generalized|suppressed|withheld>
quality:
  geometry_valid: <true|false|unknown>
  metadata_complete: <true|false|unknown>
  source_date: <date or unknown>
  stale_after: <date or rule>
```

## 12. Public API and tile policy

Public KFM clients may display BLM-derived information only through KFM-governed outputs.

Allowed public surfaces:

- KFM public API records.
- KFM released vector tiles.
- KFM released raster tiles.
- KFM released static exports.
- KFM EvidenceDrawer payloads.
- KFM source-card summaries.
- KFM attribution and provenance panels.

Prohibited public surfaces:

- Direct calls from the public UI to live BLM ArcGIS REST endpoints.
- Direct calls from the public UI to BLM raw download URLs.
- Direct exposure of RAW, WORK, QUARANTINE, or internal canonical stores.
- Direct display of unreleased candidate layers.
- Runtime AI claims derived from BLM content without EvidenceBundle support.
- Public display of sensitive site locations or unreleased protected resource data.

## 13. Ingestion checklist

Before acquiring a BLM dataset:

- [ ] Identify the BLM source handle.
- [ ] Confirm source page or service endpoint.
- [ ] Confirm dataset title and steward.
- [ ] Confirm whether the dataset is public, reviewed public, or restricted.
- [ ] Capture metadata and service description.
- [ ] Capture access timestamp.
- [ ] Capture checksums for downloaded files.
- [ ] Confirm geometry type, CRS, scale, and generalization.
- [ ] Confirm update date or mark as unknown.
- [ ] Assign preliminary KFM source role.
- [ ] Assign preliminary policy label.
- [ ] Decide whether the data is suitable for county Focus Mode.
- [ ] Decide whether sensitive-data review is required.
- [ ] Create or update dataset-level source descriptor.

During processing:

- [ ] Reproject to KFM standard CRS if required.
- [ ] Validate geometries.
- [ ] Normalize attributes.
- [ ] Preserve BLM source identifiers.
- [ ] Generate deterministic KFM identifiers.
- [ ] Produce transform receipt.
- [ ] Produce QA report.
- [ ] Produce schema crosswalk.
- [ ] Produce EvidenceBundle candidates.
- [ ] Quarantine sensitive or ambiguous records.

Before publication:

- [ ] Confirm EvidenceBundle exists.
- [ ] Confirm source descriptor is current.
- [ ] Confirm policy review passed.
- [ ] Confirm sensitive-data review passed.
- [ ] Confirm attribution text exists.
- [ ] Confirm source-role label is visible.
- [ ] Confirm stale-after rule exists.
- [ ] Confirm public output does not bypass KFM.
- [ ] Confirm public UI displays scale and authority warnings where needed.

## 14. Validation rules

### 14.1 Metadata validation

Reject or quarantine if:

- No source title exists.
- No steward can be identified.
- No accessed timestamp exists.
- No source endpoint or landing page is recorded.
- No policy posture is assigned.
- No source-role label is assigned.
- No EvidenceBundle can be produced.

### 14.2 Geometry validation

Validate:

- CRS and reprojection.
- Geometry type.
- Null geometries.
- Invalid rings or self-intersections.
- Multipart handling.
- Slivers after clipping.
- Dissolve effects.
- Simplification effects.
- County-boundary clipping.
- Tile-scale visibility.
- Boundary alignment against appropriate local or state reference layers.

Do not overstate geometry precision. If a BLM layer is generalized or optimized for display, KFM must carry that warning forward.

### 14.3 Attribute validation

Validate:

- Required identifiers.
- Null or unknown values.
- Domain values.
- Date fields.
- Program/category fields.
- Legal/status labels.
- Access fields.
- Public/restricted indicators.
- Layer-name-to-schema mapping.

### 14.4 Authority validation

Ask:

- Is BLM the authority for this claim?
- Is another federal, state, tribal, county, municipal, or private source more authoritative?
- Is the claim legal, operational, historical, cartographic, or interpretive?
- Does the public display imply a right of access?
- Does the display create risk for sensitive resources or private property?
- Does the scale support the intended use?

## 15. Redaction and generalization rules

BLM-derived records must follow KFM sensitive-topic rules.

Default redaction posture:

| Topic | Default action |
|---|---|
| Archaeological sites | Withhold or aggregate; do not publish precise locations |
| Burial or sacred sites | Withhold; tribal and legal review required |
| Tribal cultural resources | Withhold unless explicit public-release authority exists |
| Sensitive species or habitat | Generalize, aggregate, or withhold |
| Law enforcement or emergency operations | Withhold operational detail |
| Infrastructure vulnerability | Withhold or generalize |
| Private-property access ambiguity | Suppress public access implication |
| Unverified easement/access route | Mark as unverified; do not route users |
| Generalized federal land boundary | Display with scale warning |
| Historic records | Display with interpretation warning where needed |

## 16. Attribution baseline

Public KFM products using BLM-derived data must include attribution.

Recommended baseline:

```text
Contains information derived from public Bureau of Land Management (BLM) datasets or records. KFM processing, normalization, filtering, generalization, and presentation are governed KFM outputs and should not be interpreted as direct BLM publication.
```

For maps:

```text
Source: Bureau of Land Management (BLM). Processed by Kansas Frontier Matrix. See EvidenceBundle for source, access date, processing receipt, and public-release policy.
```

For EvidenceDrawer:

```text
BLM source role: <primary|corroborating|context|restricted>. Authority scope: <scope>. Accessed: <date>. KFM receipt: <receipt id>.
```

## 17. Refresh and staleness policy

Default cadence:

| Dataset type | Suggested refresh |
|---|---:|
| PLSS / cadastral reference | Quarterly, or when BLM announces update |
| Surface management / land status | Quarterly |
| Public land access | Monthly or event-driven |
| Recreation / closure-sensitive layers | Monthly or event-driven |
| Fire / operational layers | Event-driven; do not publish stale operational claims |
| Wildlife / vegetation / ecology | Quarterly with sensitive-data review |
| Historic land records | Annual or on-demand |
| Service metadata snapshots | Every acquisition and before publication |

Default stale-after rule:

```yaml
stale_after_days: 120
```

Override to shorter windows for access, fire, closures, recreation operations, and safety-relevant data.

## 18. Failure modes

Known BLM-source failure modes for KFM:

| Failure mode | KFM response |
|---|---|
| Service endpoint changes | Refresh source descriptor; do not silently repoint without receipt |
| Layer id changes | Rebuild dataset descriptor and crosswalk |
| Display-optimized layer used as legal boundary | Quarantine or label with scale warning |
| Public layer includes sensitive features | Quarantine; perform sensitive review |
| Access dataset interpreted as guaranteed public route | Fail closed; require corroboration |
| PLSS geometry treated as parcel ownership | Correct source role; require county parcel source |
| Historic patent record used as current ownership | Correct claim scope; require current local authority |
| Missing metadata | Quarantine until resolved |
| Conflicting BLM and county/state records | Create conflict record; do not publish resolved claim without steward review |
| Runtime AI generates unsupported BLM claim | Suppress or mark unsupported; cite-or-abstain |

## 19. Open questions

- Which BLM dataset families should be promoted to explicit KFM whitelisted dataset descriptors?
- Should KFM maintain a national BLM mirror for selected reference layers, or acquire per Focus Mode build?
- Which Kansas county Focus Mode plans need BLM PLSS extracts by default?
- What is the canonical KFM CRS for all BLM-derived vector processing?
- What scale threshold should be required before public display of generalized BLM boundaries?
- Which BLM layers require automatic sensitive-resource quarantine?
- How should KFM represent historic BLM/GLO records alongside county Register of Deeds records?
- Should BLM access layers require manual steward approval before any routing or public access UI is enabled?

## 20. Steward review checklist

A source steward should review this file when:

- BLM changes a relevant access point.
- KFM adds a new BLM dataset family.
- KFM updates the source descriptor schema.
- KFM changes public API or tile publication policy.
- A county Focus Mode plan depends on BLM data.
- A sensitive-data incident or near miss occurs.
- BLM metadata conflicts with another authority.
- KFM adds land-record, PLSS, public-access, or federal-interest features.

## 21. Minimal publication rule

A BLM-derived KFM record may be public only when this rule passes:

```text
Public = released KFM artifact
       + EvidenceBundle
       + source descriptor
       + source role
       + policy label
       + sensitive review
       + attribution
       + staleness rule
       + no direct RAW/WORK/QUARANTINE/live-endpoint dependency
```

If any term is missing, the record is not publishable.

## 22. Implementation note

This profile is intentionally conservative. It does not reduce the value of BLM data. It protects KFM from making legal, access, ecological, cultural, or operational claims that the source does not support.

BLM data should enter KFM as evidence-bearing source material, not as sovereign runtime truth. KFM outputs must remain governed, cited, reviewable, and reversible.
