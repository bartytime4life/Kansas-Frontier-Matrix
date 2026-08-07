<!--
KFM_WIKI_SOURCE
page_id: Domains
title: Domains
status: PROPOSED wiki source; review required
updated: 2026-08-07
authority: orientation-only; canonical repository evidence and adopted KFM authority outrank this page
source_path: docs/wiki/Domains.md
publication_effect: none until separately synchronized to the native GitHub Wiki
-->
# Domains

KFM domains are bounded knowledge lanes that share one trust spine. A domain does not become a new repository root. Its documentation, contracts, schemas, policy, fixtures, tests, pipelines, lifecycle data, and release records live under the responsibility roots that own those artifacts.

## Domain lane index

| Lane | Scope | Key trust boundary |
|---|---|---|
| [Hydrology](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/docs/domains/hydrology) | Surface water, groundwater, watersheds, hydrography, observations, and water context. | Operational conditions require time/source clarity; KFM is not an emergency-alert authority. |
| [Soil](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/docs/domains/soil) | Soil survey, horizons, properties, interpretations, moisture, and soil-climate support. | Static survey, station, gridded derivative, and satellite supports must remain distinct. |
| [Fauna](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/docs/domains/fauna) | Animal taxonomy, occurrence evidence, range, movement, status, and stewardship context. | Rare or vulnerable occurrence precision defaults to generalization or denial. |
| [Flora](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/docs/domains/flora) | Plant taxonomy, specimens, occurrences, phenology, invasive species, and restoration context. | Rare-plant locations and culturally sensitive plant knowledge require review. |
| [Habitat](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/docs/domains/habitat) | Land cover, habitat patches, suitability, connectivity, condition, and restoration. | Suitability and connectivity models remain derived, uncertainty-bearing products. |
| [Geology](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/docs/domains/geology) | Bedrock and surficial geology, stratigraphy, structures, subsurface references, and resources. | Observation, interpretation, model, occurrence, estimate, extraction, and regulation must not collapse. |
| [Atmosphere](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/docs/domains/atmosphere) | Weather, climate, air quality, smoke, observations, forecasts, and modeled conditions. | Observation, forecast, advisory, and model roles plus freshness must be visible. |
| [Roads, Rail, and Trade](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/docs/domains/roads-rail-trade) | Modern and historical transport networks, crossings, depots, routes, and trade connections. | Historic uncertainty, private access, and infrastructure sensitivity require bounded exposure. |
| [Settlements and Infrastructure](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/docs/domains/settlements-infrastructure) | Settlements, services, facilities, networks, dependencies, and change over time. | Critical-infrastructure details fail closed or are generalized. |
| [Archaeology](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/docs/domains/archaeology) | Sites, surveys, collections, interpretations, cultural heritage, and documentation. | Exact locations, sovereignty, sacred knowledge, and site vulnerability default to restriction. |
| [Hazards](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/docs/domains/hazards) | Hazard events, exposure, vulnerability, resilience, warnings as context, and recovery. | KFM is not an official warning or emergency-action authority. |
| [Agriculture](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/docs/domains/agriculture) | Crops, fields, irrigation, livestock, yields, land use, stress, and farm-system context. | Private farm detail, derived remote sensing, and aggregate statistics need role and scale clarity. |
| [People, DNA, and Land](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/docs/domains/people-dna-land) | People assertions, genealogy, relationships, genomic references, land and title context. | Living-person, DNA/genomic, private-land, and disputed-title information defaults to deny or staged access. |

## Shared domain packet

A mature domain lane typically needs some combination of:

- bounded scope and ubiquitous language;
- source descriptors and source-role rules;
- stable domain identity and time semantics;
- semantic contracts and machine schemas;
- valid, invalid, denied, stale, and correction fixtures;
- validators and policy profiles;
- pipeline and lifecycle placement;
- evidence resolution and catalog closure;
- public-safe layer/API/UI projection;
- review, release, correction, withdrawal, and rollback;
- documentation and verification backlog.

The packet is shared; the risk is domain-specific. Archaeology and genomic material cannot inherit the public defaults of a general hydrology fixture.

## Cross-domain seams

Cross-domain relations should be explicit and owned:

- soil parent material relates to surficial geology;
- hydrostratigraphy informs hydrology without replacing measurements;
- habitat relates flora and fauna without becoming occurrence authority;
- hazards consume conditions and exposure without replacing official alerts;
- roads and settlements connect access, trade, services, and historic change;
- people and land assertions may relate places and records without collapsing identity, ownership, or evidence roles.

A seam is not permission to duplicate canonical records. Use stable IDs, evidence-bearing relation objects, source-role labels, and time/scale semantics.

## Sensitive domains

The following normally require stricter review and fail-closed behavior:

- rare species and rare plants;
- archaeological and sacred/cultural locations;
- living people and family/private records;
- DNA and genomic material;
- critical infrastructure and private facilities;
- disputed or private land/title information;
- private wells and harmful-precision environmental locations.

See [Security and Sensitivity](Security-and-Sensitivity.md).

## Domain maturity

Documentation presence is not domain completion. Verify, at a known revision:

- source rights and activation state;
- contract/schema/policy agreement;
- deterministic fixtures and negative tests;
- pipeline outputs and receipts;
- evidence and catalog closure;
- public-safe transformations;
- release and rollback records;
- governed API/UI behavior.

## Canonical index

Read the current [domain documentation index](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/domains/README.md) for lane names, current documentation status, conflicts, and links to owning roots.
