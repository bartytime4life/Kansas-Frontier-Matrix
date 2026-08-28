<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/earth-observation-harvest-authority-matrix
title: Earth Observation Harvest Authority Matrix Contract
type: semantic-contract; control-plane-matrix; source-access-boundary; fixture-first
version: v0.1.0
status: proposed; inactive; documented-only; no-live-network
owners: OWNER_TBD — EO source steward · Connector steward · Rights steward · Security reviewer · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: public; source; earth-observation; authority-matrix; no-secrets; no-activation
related:
  - ../../docs/sources/catalog/nasa/nasa-earthdata.md
  - ../../docs/sources/catalog/nasa/nasa-hls.md
  - ../../connectors/nasa-earthdata/README.md
  - ../../connectors/nasa-hls/README.md
  - ../../control_plane/earth_observation_harvest_authority_matrix.json
  - ../../schemas/contracts/v1/source/earth_observation_harvest_authority_matrix.schema.json
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, earth-observation, source, authority, access, auth, pagination, rate-limit, control-plane]
[/KFM_META_BLOCK_V2] -->

# Earth Observation Harvest Authority Matrix Contract

> The `EarthObservationHarvestAuthorityMatrix` is a machine-readable control-plane crosswalk for EO access surfaces and product lanes. It makes source role, repository evidence, access/auth posture, pagination/rate-limit unknowns, rights/sensitivity state, and network activation state explicit without activating a connector or embedding an endpoint or secret.

## Source-derived requirement

Pass 31 proposes an EO harvest authority matrix covering STAC endpoints, CMR/Earthdata access, provider authentication, pagination, and rate-limit behavior. The repository already documents NASA Earthdata and HLS but records their connector lanes as README-only and source authority as unestablished. This slice converts that documented state into a deterministic, inactive matrix—not into live source admission.

## Responsibility split

| Responsibility | Home |
|---|---|
| Matrix meaning | `contracts/source/earth_observation_harvest_authority_matrix.md` |
| Machine shape | `schemas/contracts/v1/source/earth_observation_harvest_authority_matrix.schema.json` |
| Cross-system projection | `control_plane/earth_observation_harvest_authority_matrix.json` |
| Source identity/activation | Existing accepted `data/registry/sources/` and source-authority mechanisms; not this matrix |
| Connector implementation | `connectors/` after separate acceptance and activation |
| Validation | `tools/validators/validate_earth_observation_harvest_authority_matrix.py` |

Adopted Directory Rules place semantic meaning in `contracts/`, machine shape in `schemas/`, and governance crosswalks in `control_plane/`.

## Authority roles

- `ACCESS_SURFACE`: credentialed or public discovery/retrieval gateway shared by products.
- `PRODUCT_CONTEXT`: a product lane that uses an access surface but preserves its own source role and validation burden.
- `CATALOG_ENDPOINT`: a catalog/discovery surface such as a reviewed STAC endpoint.
- `PROVIDER_DISTRIBUTION`: a provider/DAAC distribution surface.

These roles are non-interchangeable. Successful authentication or catalog discovery is not product truth, rights clearance, source admission, or publication permission.

## Matrix states

| State | Meaning |
|---|---|
| `DOCUMENTED_ONLY` | Repository documentation exists; source authority, descriptor, activation, endpoint, and runtime remain unresolved. Network authorization is false. |
| `REVIEWED_INACTIVE` | Authority and rights review references may exist, but no effective activation is referenced. Network authorization is false. |
| `ACTIVE` | An external accepted activation record and required source/policy bindings are referenced. This matrix still grants no RAW, promotion, release, or publication authority. |
| `SUSPENDED` | Access is held because of security, rights, source, policy, currentness, or operational concerns. |
| `RETIRED` | Identity and lineage remain, but the access surface must not be used. |

## Secret and endpoint boundary

The matrix stores references, never tokens, credentials, authorization headers, cookies, signed URLs, private endpoint values, or secret-manager payloads. `endpoint_ref` may point to reviewed configuration or documentation; it must not contain a raw URL. Browser/client credential exposure is always denied.

## Determinism and integrity

- Entries are sorted and unique by `authority_id`.
- `access_surface_ref` must resolve to another matrix entry with role `ACCESS_SURFACE` or `CATALOG_ENDPOINT`.
- Repository document/connector references are canonical relative paths and must exist.
- Reason and operation arrays use canonical ordering.
- `spec_hash` is RFC 8785 JCS plus SHA-256 over the matrix with `spec_hash` omitted.

## Non-effects

A passing matrix proves only closed shape, deterministic identity/order, repository-reference closure, and explicit inactive/unknown posture. It does not prove current external endpoints, terms, authentication, pagination, quotas, data quality, source rights, source activation, connector implementation, evidence closure, release, or publication.

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive packet. No credential, external request, lifecycle data, catalog record, release, public API, map, or AI surface is created or changed.
