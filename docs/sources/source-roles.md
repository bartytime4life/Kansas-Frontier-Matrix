# Source Roles

| Field | Value |
|---|---|
| Document path | `docs/sources/source-roles.md` |
| Document type | Human-readable source-governance reference |
| Status | PROPOSED until merged and reviewed in the live repository |
| Owner | Source steward / docs steward |
| Reviewers | Source steward, policy steward, evidence steward, affected domain steward |
| Related doctrine | `docs/doctrine/authority-ladder.md`, `docs/doctrine/truth-posture.md`, `docs/doctrine/trust-membrane.md`, `docs/doctrine/lifecycle-law.md`, `docs/architecture/contract-schema-policy-split.md` |
| Related machine homes | `data/registry/sources/`, `schemas/contracts/v1/source/`, `policy/`, `tests/`, `fixtures/`, `tools/validators/` |
| Lifecycle invariant | RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED |

## 1. Purpose

This document defines the source-role vocabulary used by Kansas Frontier Matrix (KFM) when admitting, describing, validating, citing, reviewing, and publishing source material.

A source role describes a source's relationship to a claim. It is not a popularity score, quality score, or blanket authority label. The same organization or dataset may play different roles for different claims.

Source roles exist to prevent authority collapse. KFM must not treat an occurrence aggregator as a legal authority, a regulatory map as an observed event, a model as a measurement, an assessor record as title truth, or a generated summary as evidence.

## 2. Operating rule

Every admitted source MUST have a declared source role before it can support a claim, EvidenceBundle, catalog record, layer manifest, triplet, Focus Mode response, Story Node, or public UI explanation.

If the source role is unknown, ambiguous, missing, or incompatible with the claim type, KFM MUST fail closed:

- `DENY` for publication or public exposure when misuse could create legal, safety, rights, sensitivity, or trust risk.
- `ABSTAIN` when the system lacks enough evidence to answer truthfully.
- `ERROR` when a required source descriptor, EvidenceRef, registry record, or policy rule cannot be resolved.
- `QUARANTINE` when the material may be useful later but cannot safely advance.

## 3. Source role families

### 3.1 Primary evidence

Primary evidence is source material that directly supports the claim being made, within the source's own authority and limits.

Use this role when the source is the direct basis for the claim, not merely background or corroboration.

Examples:

- A source-native observation record used to support an observation claim.
- A legal instrument used to support a legal-history claim.
- A steward-reviewed field record used to support a reviewed occurrence claim.
- A source-native timestamped measurement used to support a measurement claim.

Primary evidence still needs rights, sensitivity, provenance, temporal validity, spatial validity, and review checks. Primary does not mean publishable by default.

### 3.2 Corroborating evidence

Corroborating evidence supports or checks a claim but is not sufficient by itself to carry the claim.

Examples:

- A second observation source that agrees with a primary observation.
- A historical map that supports, but does not prove, a settlement-location interpretation.
- A monitoring network summary that supports a trend already grounded in source-native observations.

Corroborating evidence MUST NOT be promoted into primary evidence merely because it agrees with an expected answer.

### 3.3 Context

Context sources help users understand background, geography, methods, conditions, or interpretation limits.

Examples:

- County histories used as background for a frontier-era narrative.
- General GIS, hydrology, planning, or ecology references used to explain methods.
- Gazetteers used to clarify place-name context.

Context sources MUST NOT carry claims outside their authority. A context source can explain why something matters, but it usually cannot prove that a specific KFM claim is true.

### 3.4 Regulatory context

Regulatory context sources describe official regulatory zones, decisions, classifications, filings, or administrative designations.

Examples:

- Flood hazard zones used as regulatory context.
- Conservation designations used as legal or administrative context.
- Transportation restrictions or official road classifications.
- Public administrative boundaries.

Regulatory context MUST NOT be mislabeled as a physical observation. A flood-hazard zone is not the same as an observed flood event. A designated habitat boundary is not the same as an observed species occurrence.

### 3.5 Legal authority

Legal authority sources support claims about legal status, rights, ownership, restrictions, designations, or formal decisions.

Examples:

- Statutes, ordinances, court records, deeds, plats, easements, title records, or official agency determinations.
- Legal notices or official administrative decisions.

Legal authority sources MUST be handled with strict citation, date, jurisdiction, and scope. Assessor and tax records are administrative sources, not title truth, unless the claim is explicitly about assessment or taxation.

### 3.6 Administrative record

Administrative records are operational or governmental records that document how an agency or institution manages, classifies, taxes, inspects, inventories, or reports something.

Examples:

- Parcel assessment records.
- Inspection inventories.
- Agency-maintained facility records.
- Permit indexes or public management records.

Administrative records can support administrative claims. They MUST NOT be treated as legal proof, physical measurement, or historical interpretation unless the source's authority and evidence support that use.

### 3.7 Observation

Observation sources record something measured, witnessed, detected, sampled, surveyed, or reported at a time and place.

Examples:

- Streamflow readings.
- Weather observations.
- Field survey observations.
- Species occurrence observations.
- Remote-sensing detections when treated as detections, not confirmations.

Observation sources require temporal fields, spatial fields, method or sensor metadata, uncertainty or qualifier handling, and source-role-compatible claim types.

### 3.8 Monitoring reference

Monitoring references summarize or expose ongoing conditions, cadence, network status, station behavior, source health, or operational data availability.

Examples:

- Mesonet station status.
- USGS gauge availability metadata.
- Source status pages.
- Watcher HEAD / ETag / Last-Modified records.

Monitoring references are useful for freshness and health. They do not prove the underlying domain claim unless paired with admissible evidence.

### 3.9 Operational notice

Operational notices announce warnings, outages, advisories, status changes, closures, incidents, or service conditions.

Examples:

- Weather warnings.
- Source outage alerts.
- Road closure notices.
- Agency operational bulletins.

KFM may preserve operational notices as context or evidence of what was announced. KFM MUST NOT present itself as an emergency alert system, dispatch authority, or official life-safety notice channel.

### 3.10 Scientific interpretation

Scientific interpretation sources contain expert analysis, peer-reviewed findings, technical reports, interpreted maps, modeled classifications, or research conclusions.

Examples:

- Geological interpretations.
- Habitat suitability interpretations.
- Climate or hydrology assessments.
- Archaeological interpretations.

Scientific interpretation is not raw observation. It must retain method, uncertainty, scale, date, authorship, assumptions, and fitness-for-use limits.

### 3.11 Model product

Model products are outputs of computational models, interpolations, simulations, classifications, predictions, reanalyses, or derived surfaces.

Examples:

- Flood-risk model outputs.
- Air-quality model fields.
- Habitat suitability models.
- Land-cover classifications.
- Synthetic or digital-twin surfaces.

Model products MUST be labeled as model products. They can support analytical or interpretive claims, but they MUST NOT be treated as direct measurement without supporting evidence and method disclosure.

### 3.12 Remote-sensing product

Remote-sensing products are imagery, derived raster products, detections, indices, classifications, or sensor-based surfaces.

Examples:

- Satellite imagery.
- LiDAR-derived products.
- NDVI or land-cover rasters.
- Active-fire detections.
- Aerosol optical depth products.

Remote-sensing products require sensor, processing level, acquisition time, resolution, algorithm/version, cloud/quality flags, spatial accuracy, and public-safety/sensitivity review.

### 3.13 Aggregator

Aggregators compile, index, normalize, or redistribute records from other sources.

Examples:

- Biodiversity aggregators.
- Community-science portals.
- Open-data catalogs.
- Cross-source search systems.

Aggregators are often valuable for discovery and context. They MUST NOT automatically inherit the authority of original sources. When possible, KFM should resolve aggregator records back to original records, source terms, and steward review state.

### 3.14 Community observation

Community observations are observations submitted by volunteers, residents, visitors, community scientists, or non-official contributors.

Examples:

- Citizen-science species observations.
- Volunteered geographic information.
- Community-reported local conditions.

Community observations may be useful, but they often require review, geoprivacy, rights checks, uncertainty handling, and steward validation before public claim support.

### 3.15 Historical source

Historical sources document past conditions, events, boundaries, names, routes, land use, ownership, narratives, or interpretations.

Examples:

- Historic maps.
- Newspapers.
- county histories.
- archival documents.
- land-office records.
- oral histories where rights and consent permit use.

Historical sources require date, provenance, transcription/translation status, georeferencing method if mapped, uncertainty, rights, and interpretive caution.

### 3.16 Generated derivative

Generated derivatives are outputs created by KFM tools, scripts, AI systems, transformations, map builders, graph builders, summarizers, model pipelines, or analysts.

Examples:

- AI summaries.
- Derived layers.
- PMTiles generated from processed data.
- graph projections.
- normalized tables.
- synthetic indicators.

Generated derivatives are downstream carriers, not sovereign truth. They must reference EvidenceRefs, source descriptors, receipts, validation reports, policy decisions, and release manifests when used in public surfaces.

### 3.17 Restricted source

Restricted sources contain material that is sensitive, private, rights-limited, embargoed, sovereign, culturally sensitive, security-relevant, or otherwise unsuitable for normal public release.

Examples:

- Precise rare-species locations.
- Archaeological site coordinates.
- burial or sacred site records.
- living-person records.
- DNA/genomic data.
- critical infrastructure details.
- private property records with exposure risk.

Restricted source material defaults to quarantine, redaction, generalization, aggregation, delayed release, staged access, or denial. Public derivatives require transform receipts and review.

### 3.18 Unknown / unclassified

Unknown or unclassified means KFM has not established the source role strongly enough.

Unknown is not a temporary allow state. It is a fail-closed state until a source steward resolves the role.

## 4. Role-to-claim compatibility

The table below is a default compatibility guide. Domain policies may be stricter.

| Claim type | Strong supporting roles | Usually insufficient alone | Must not be used as |
|---|---|---|---|
| Physical observation | Observation, primary evidence | Aggregator, community observation, remote-sensing detection | Legal authority |
| Regulatory status | Regulatory context, legal authority | Context, aggregator | Physical observation |
| Legal ownership or right | Legal authority | Administrative record, assessor record, context | Title proof unless explicitly legal source |
| Administrative status | Administrative record, regulatory context | Context, generated derivative | Physical or legal truth outside admin scope |
| Historical interpretation | Historical source, primary evidence, corroborating evidence | Context, generated derivative | Present-day fact without temporal scope |
| Scientific interpretation | Scientific interpretation, model product, observation | Context, generated derivative | Direct measurement unless supported |
| Public map layer | Released generated derivative with EvidenceBundle | Raw, work, quarantine, unpublished candidate | Canonical truth store |
| AI answer | EvidenceBundle-backed released or cataloged source references | Raw model output, generated derivative alone | Source of record |
| Source health | Monitoring reference, operational notice, source-head record | Context | Domain truth |
| Emergency or life-safety instruction | Official operational notice shown with disclaimer and source link | KFM generated text | KFM-authored alert |

## 5. Required SourceDescriptor fields

A source descriptor SHOULD include at least:

```yaml
id: string
name: string
role_family: string
claim_types_allowed: []
claim_types_denied: []
source_url: string
publisher: string
steward: string
contact: string
jurisdiction: string
coverage_spatial: string
coverage_temporal: string
cadence: string
version_or_accessed_at: string
rights:
  license: string
  redistribution: string
  attribution: string
  terms_url: string
sensitivity:
  default_tier: string
  exact_location_allowed: boolean
  living_person_risk: boolean
  cultural_or_sovereignty_review: boolean
quality:
  uncertainty: string
  known_limitations: []
  required_qualifiers: []
source_head:
  etag: string
  last_modified: string
  content_length: integer
  checked_at: string
admissibility:
  public_use: allow | deny | restrict | abstain
  required_reviews: []
  required_transforms: []
  fail_closed_reasons: []
citation:
  preferred_label: string
  citation_text: string
  accessed_at: string
```

The machine schema for source descriptors belongs in the schema/contract authority home chosen by repository doctrine. This Markdown file explains the vocabulary; it is not the schema.

## 6. Validation rules

A source-role validator SHOULD enforce these rules:

1. `role_family` is present and belongs to the approved vocabulary.
2. `claim_types_allowed` and `claim_types_denied` are explicit.
3. Unknown role means quarantine or denial, never silent promotion.
4. Source role is compatible with the proposed claim type.
5. Rights, sensitivity, and citation fields are present before publication.
6. Aggregator records identify original-source references when available.
7. Model products include method/version/uncertainty metadata.
8. Remote-sensing products include sensor, processing level, acquisition time, resolution, and quality flags.
9. Operational notices include issue time, expiry or validity window, publisher, and disclaimer obligations.
10. Restricted sources declare public-safe transform requirements.
11. Generated derivatives include upstream EvidenceRefs, transform receipts, and release references.
12. Public payloads expose source-role badges where source role affects trust.

## 7. Public UI requirements

Public KFM surfaces SHOULD show enough source-role context for a user to understand why a claim can or cannot be trusted.

Minimum public-facing source-role indicators:

- role badge, such as `observation`, `regulatory_context`, `model_product`, `aggregator`, `generated_derivative`, or `restricted_public_derivative`;
- source title and publisher;
- date or temporal validity;
- evidence and citation link;
- policy/review/release state;
- limitations and uncertainty;
- correction or supersession state when applicable.

The UI MUST NOT expose raw, work, quarantine, restricted, private, or unpublished source material through normal public routes.

## 8. Examples

### 8.1 NFHL flood layer

- Role: `regulatory_context`.
- Can support: regulatory flood-hazard context.
- Cannot support by itself: an observed flood event claim.
- Required UI language: regulatory context, not observed flooding.

### 8.2 USGS stream gauge observation

- Role: `observation`.
- Can support: timestamped stream stage or discharge observation.
- Cannot support by itself: legal floodplain status or emergency instruction.
- Required UI language: include qualifiers, provisional state, units, and timestamp.

### 8.3 GBIF or eBird occurrence record

- Role: `aggregator` or `community_observation`, depending on record and claim.
- Can support: occurrence context or candidate occurrence.
- Cannot support by itself: legal species status, exact public rare-species location, or steward-confirmed presence.
- Required UI language: source role, review state, geoprivacy state.

### 8.4 Parcel assessment record

- Role: `administrative_record`.
- Can support: assessor/tax administrative claim.
- Cannot support by itself: title truth or legal boundary proof.
- Required UI language: administrative record, not title determination.

### 8.5 AI-generated county summary

- Role: `generated_derivative`.
- Can support: no factual claim by itself.
- Must reference: EvidenceBundle, source descriptors, citation validation, policy decision, release state.
- Required UI language: AI summary is interpretive and evidence-subordinate.

## 9. Governance and change control

Changes to this document SHOULD be reviewed when they:

- add, rename, merge, or retire a source role;
- change role-to-claim compatibility;
- alter fail-closed behavior;
- change public UI obligations;
- affect sensitive domains such as ecology, archaeology, people, DNA, land ownership, infrastructure, hazards, or public safety;
- introduce a new machine registry, policy home, or schema home.

Changes that create a parallel source registry, schema home, policy home, proof home, receipt home, or release home require Directory Rules review and, when applicable, an ADR.

## 10. Non-goals

This document does not:

- define the JSON Schema for `SourceDescriptor`;
- approve any specific external source;
- grant publication rights;
- replace source descriptors, EvidenceBundles, receipts, validation reports, policies, or release manifests;
- authorize direct public access to RAW, WORK, QUARANTINE, restricted, private, or unpublished source material;
- allow AI-generated text to act as evidence.

## 11. Maintainer checklist

Before a new source role or source descriptor is accepted, confirm:

- [ ] source role is declared;
- [ ] source role matches claim type;
- [ ] rights are known;
- [ ] sensitivity tier is known;
- [ ] citation text is present;
- [ ] temporal and spatial scope are present;
- [ ] steward or publisher is identified;
- [ ] original source is linked when the record comes through an aggregator;
- [ ] required transforms are recorded;
- [ ] EvidenceRefs resolve before publication;
- [ ] policy decision is recorded;
- [ ] review state is recorded;
- [ ] release state is recorded;
- [ ] rollback/correction path is available;
- [ ] public UI can show source-role limitations.
