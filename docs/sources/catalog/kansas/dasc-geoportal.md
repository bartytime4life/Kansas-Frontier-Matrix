<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-kansas-dasc-geoportal
title: Kansas Geoportal (DASC) — Live ArcGIS Source-Family Registration
type: source-family-page; live-discovery-registration; no-source-activation
version: v0.1.0
status: verified live discovery surface; candidate items; no admission or publication
owners: NEEDS VERIFICATION — Kansas source steward + affected domain steward + rights + sensitivity + release reviewer
created: 2026-09-20
updated: 2026-09-20
policy_label: public-review; discovery-live; cite-or-abstain; fail-closed; no-activation; no-publication
current_path: docs/sources/catalog/kansas/dasc-geoportal.md
truth_posture: >
  CONFIRMED public Kansas Geoportal ArcGIS Hub availability, ArcGIS organization
  identity, representative public Feature Service metadata and bounded count queries /
  PROPOSED reuse of existing bounded ArcGIS REST acquisition machinery and per-item
  SourceDescriptor intake / NEEDS VERIFICATION per-item publisher authority, scope,
  currentness, rights, attribution, sensitivity, schema, correction behavior, and
  downstream fitness / DENY portal-wide admission, parcel-title truth, owner-data
  publication, infrastructure-sensitive precision, and automatic release
related:
  - ./README.md
  - ../../ADMISSION_PROCESS.md
  - ../../SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../doctrine/directory-rules.md
  - ../../../../data/registry/sources/README.md
  - ../../../../connectors/usgs/README.md
notes:
  - "Live means the public discovery and REST surfaces responded during the dated probe; it does not mean admitted, scheduled, released, deployed, promoted, or published."
  - "DASC is an aggregator. Each ArcGIS item retains its own publisher, role, version, rights, sensitivity, and fitness decision."
  - "No parallel adapter is authorized: the existing bounded ArcGIS REST request pattern is the proposed protocol-level reuse point."
[/KFM_META_BLOCK_V2] -->

# Kansas Geoportal (DASC) — live ArcGIS source-family registration

The [Kansas Geoportal](https://hub.kansasgis.org/) is registered here as a **verified live discovery source family**. The portal is an ArcGIS Hub surface backed by ArcGIS item metadata and public REST services in organization `ZOdjAzAQ2B0f85zi`.

This registration does not flatten the portal into one authority. It does not admit every item, activate a connector or scheduler, fetch RAW payloads, create evidence, approve rights or sensitivity, release a layer, deploy code, or publish data.

## Verified access pattern

Observed on `2026-09-20`:

| Surface | Verified locator | Result |
|---|---|---|
| Discovery portal | `https://hub.kansasgis.org/` | Public ArcGIS Hub responded |
| ArcGIS item metadata | `https://www.arcgis.com/sharing/rest/content/items/{item_id}?f=json` | Public item records returned publisher, modified time, access, service URL, and item-level terms when present |
| Feature Service metadata | `https://services2.arcgis.com/ZOdjAzAQ2B0f85zi/arcgis/rest/services/{service}/FeatureServer?f=pjson` | Public service and layer metadata returned |
| Bounded query | `.../FeatureServer/{layer}/query?where=1%3D1&returnCountOnly=true&f=json` | Public count-only queries returned for the sampled services |

The request and response family matches the ArcGIS REST/Feature Service pattern already used by KFM's WBD and other bounded ArcGIS source work. **No new protocol adapter is required.** Each selected item still needs a product-specific configuration, schema mapping, pagination limit, stable identity rule, negative fixtures, and failure behavior.

## Representative live items

These examples prove catalog and service availability only. Counts are dated probe observations, not durable dataset versions.

| ArcGIS item | Publisher / owner shown by ArcGIS | Service role | Dated probe | KFM posture |
|---|---|---|---|---|
| [`0d15901ab05142bd8e8346bbf7ee59f7`](https://hub.kansasgis.org/datasets/0d15901ab05142bd8e8346bbf7ee59f7) — Kansas HUC12 boundaries | `jkastens_KU`; item terms request Kansas Biological Survey acknowledgement | Watershed boundary context derived from WBD | Polygon layer; `3,080` count response | Candidate corroborating/context source; preserve item identity and WBD lineage |
| [`00683d63239e4237bfc1878ce97ec156`](https://hub.kansasgis.org/datasets/00683d63239e4237bfc1878ce97ec156) — Kansas Stream Order 3–9 | `ks_biosurvey` | Modified NHD stream network with Strahler order | Polyline layer; `42,972` count response | Candidate derived hydrography context; not current flow, navigability, or complete NHD truth |
| [`b9fcc1196a6e4201b0d356b4836104f7`](https://hub.kansasgis.org/datasets/b9fcc1196a6e4201b0d356b4836104f7) — PLSS Township Range | `KS_Geological_Survey` | Public-land-survey township/range boundary context | Polygon layer; `2,343` count response | Candidate administrative/cadastral context; not title, surveyed parcel boundary, or ownership truth |
| [`632c404c517744a4997782e087e022d5`](https://hub.kansasgis.org/datasets/632c404c517744a4997782e087e022d5) — Parcels | `j130v976@ku.edu_KU`; no item description, tags, access information, or license text returned | Parcel-labelled polygon service with related table | Polygon layer; `422,346` count response | **HOLD / QUARANTINE** pending scope, publisher authority, county coverage, owner-field inventory, rights, privacy, and public-use review |

The parcel-labelled item must not be described as a complete statewide parcel authority from its title or feature count. Any owner/person field, private-land linkage, assessor interpretation, legal-boundary claim, or exact sensitive join remains deny-by-default.

## Registration boundary

| Decision | State |
|---|---|
| Portal discoverability | `CONFIRMED LIVE` at the dated probe |
| ArcGIS REST protocol compatibility | `CONFIRMED PATTERN`; reuse existing bounded request machinery |
| Portal-wide source admission | `DENIED` — admission is item-specific |
| Connector activation or scheduling | `NOT AUTHORIZED` |
| RAW capture | `NOT PERFORMED` |
| Public release or Explorer layer activation | `NOT AUTHORIZED` |
| Canonical SourceDescriptor write | `HOLD` pending the existing registry-topology decision and per-item review |

## Per-item intake requirements

For every selected ArcGIS item:

1. Pin the ArcGIS item ID, service URL, layer ID, publisher/owner, item modified time, and checked-at time.
2. Record source role and derivation; a DASC mirror of a federal or agency product does not replace upstream identity.
3. Capture service capabilities, maximum record count, query formats, object ID field, geometry type, CRS, field schema, pagination strategy, and deterministic ordering.
4. Resolve item-specific terms, attribution, redistribution, commercial-use posture, and disclaimer preservation.
5. Review privacy, private-land, archaeology, rare-species, infrastructure, and harmful-precision risks before retrieval or public use.
6. Add source-shaped offline fixtures and negative cases for missing metadata, pagination drift, schema change, duplicate IDs, partial responses, stale items, service errors, and unsafe fields.
7. Route successful acquisition only into governed RAW or QUARANTINE placement. Preserve `RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED` and require separate evidence, policy, review, release, correction, and rollback closure.

## Rollback

Before merge, close the pull request and abandon its branch. After merge, revert the scoped catalog and Explorer-candidate changes through a reviewed pull request. A documentation or UI rollback does not delete upstream DASC data and does not imply source deactivation, release rollback, deployment rollback, or publication rollback.
