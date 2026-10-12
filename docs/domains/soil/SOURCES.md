<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/sources
title: Soil source families and review checklist
type: domain-guide
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Soil source families and review checklist; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/domains/soil/SOURCE_REGISTRY.md
  - data/registry/sources/soil/README.md
  - docs/domains/soil/MAP_UI_CONTRACTS.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# SOURCES

Start here to choose the appropriate Soil source family and review boundary.
This is a navigation guide to repository-held records; it does not verify live
provider terms, endpoints, coverage or source activation. Detailed lineage and
historical registry issues remain in [SOURCE_REGISTRY.md](SOURCE_REGISTRY.md).

## Source-family map

| Family | Repository record | Intended contribution | Important limit |
|---|---|---|---|
| NRCS SSURGO | [Descriptor](../../../data/registry/sources/soil/nrcs-ssurgo.yaml) | Survey map units, components and horizons | Survey support is not field-uniform truth |
| USDA NRCS SDA | [Descriptor](../../../data/registry/sources/soil/nrcs-sda.yaml) | Source query/access surface | An access mechanism is not a new soil product |
| gSSURGO | [Descriptor](../../../data/registry/sources/soil/nrcs-gssurgo.yaml) | Gridded survey-derived context | Retain derivation and grid support |
| gNATSGO | [Descriptor](../../../data/registry/sources/soil/nrcs-gnatsgo.yaml) | Integrated gridded soil context | Preserve product composition and edition |
| Kansas Mesonet | [Descriptor](../../../data/registry/sources/soil/ks-mesonet.yaml) | Station soil moisture | Preserve station, depth, unit, time and QC |
| NRCS SCAN | [Descriptor](../../../data/registry/sources/soil/nrcs-scan.yaml) | Reference station soil climate | Reference-site support is spatially bounded |
| NOAA USCRN | [Descriptor](../../../data/registry/sources/soil/noaa-uscrn.yaml) | Reference soil/climate context | Keep observed quantities and station meaning distinct |
| NASA SMAP | [Descriptor](../../../data/registry/sources/soil/nasa-smap.yaml) | Satellite/model-assimilation moisture grids | Not an in-situ field measurement |
| ISRIC SoilGrids | [Descriptor](../../../data/registry/sources/soil/isric-soilgrids.yaml) | Modeled gridded soil properties | Model prediction, depth and uncertainty stay explicit |

Some records remain short proposed declarations. An existing YAML file is not a
completed SourceDescriptor or activation decision. Source families can also have
several products with different rights, editions, methods and support.

## Product review worksheet

Before using a source for a candidate, record:

1. **Identity:** provider, exact product, edition/version, source-native keys,
   geography and time/depth coverage.
2. **Meaning:** observed, modeled or interpretive role; spatial support, units,
   methods, uncertainty, missing-value and QC semantics.
3. **Rights:** current authoritative terms, attribution, redistribution, caching
   and derivative restrictions, with the review date and reviewer role.
4. **Sensitivity:** precise station/field/parcel implications and cross-domain
   joins, not just the provider's public/private label.
5. **Acquisition:** bounded extent/history, expected size, pagination, quotas,
   cache policy and explicit user control over material volume.
6. **Reproducibility:** capture/payload digest, retrieval time, source edition,
   transform/profile version, validation and evidence references.
7. **Lifecycle:** admission/activation state, correction and withdrawal handling,
   release audience and rollback target.

Unknown rights, source identity or sensitivity remains an unresolved gate. Use
synthetic local fixtures to advance independent validation while review proceeds.

## Existing entry points

Human source pages include [SDA](../../sources/catalog/nrcs/soil-data-access.md),
[Web Soil Survey](../../sources/catalog/nrcs/web-soil-survey.md),
[SCAN](../../sources/catalog/nrcs/scan-soil-climate.md) and
[SoilGrids](../../sources/catalog/isric/isric-soilgrids.md).
The [fixture-only SSURGO watcher](../../../tools/ingest/ssurgo_watch/ssurgo_watch.py)
provides package-change evidence, not a scheduled live downloader. The
[Site map guide](MAP_UI_CONTRACTS.md) records separate imagery/query behavior.

## Refresh and troubleshooting

Compare edition, content, schema, rights and support semantics independently.
A changed retrieval timestamp alone is not proof of a new product. A successful
HTTP response is not proof of complete coverage or reuse permission. If a source
returns an unexpected shape, partial result or missing depth unit, preserve the
bounded candidate and fail its intended claim rather than guessing values.

Review is complete for a named product only when its evidence and accountable
outcome are recorded. Source activation and release remain separate transitions.
