<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nasa-earthdata-readme
title: connectors/nasa-earthdata/ — NASA Earthdata Connector Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward for NASA · Earth-observation steward · Security reviewer · Rights reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; connector-boundary; nasa-earthdata; access-surface; beyond-directory-rules-7-3; open-dsc-14; credentialed-access; no-browser-token-exposure; no-publication
proposed_path: connectors/nasa-earthdata/README.md
truth_posture: CONFIRMED path exists / PROPOSED NASA connector family beyond §7.3 / IMPLEMENTATION DEPTH NEEDS VERIFICATION
related:
  - ../README.md
  - ../nasa/README.md
  - ../nasa-firms/README.md
  - ../nasa-hls/README.md
  - ../nasa-smap/README.md
  - ../../docs/sources/catalog/nasa/README.md
  - ../../docs/sources/catalog/nasa/nasa-earthdata.md
  - ../../docs/sources/catalog/nasa/nasa-firms.md
  - ../../docs/sources/catalog/nasa/nasa-hls.md
  - ../../docs/sources/catalog/nasa/nasa-smap.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/trust-membrane.md
  - ../../docs/doctrine/lifecycle-law.md
  - ../../data/registry/sources/
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/sources/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, nasa, nasa-earthdata, earthdata, cmr, edl, daac, access-surface, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a blank `connectors/nasa-earthdata/README.md` file."
  - "The NASA source-family README says the NASA family is PROPOSED, beyond Directory Rules §7.3, and awaits OPEN-DSC-14."
  - "The NASA Earthdata product page frames Earthdata as a credentialed access surface, not a measurement product or STAC collection."
  - "Public clients must not depend on NASA/CMR auth tokens; governed server-side access and released assets are the safe public path."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NASA Earthdata Connector Boundary

> Connector-boundary README for `connectors/nasa-earthdata/`. NASA Earthdata is treated here as a **credentialed access surface** for discovering and retrieving downstream NASA Earth-observation products. It is not itself a measurement product, catalog truth store, release engine, public API, or browser-facing dependency.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family status: beyond §7.3" src="https://img.shields.io/badge/family-beyond__%C2%A77.3-orange">
  <img alt="Open item: OPEN-DSC-14" src="https://img.shields.io/badge/open-OPEN--DSC--14-orange">
  <img alt="Public clients: no direct tokens" src="https://img.shields.io/badge/public__clients-no__direct__tokens-critical">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` connector-boundary README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/nasa-earthdata/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `PROPOSED` NASA family beyond §7.3 · `NEEDS VERIFICATION` implementation files, tests, fixtures, endpoint details, credentials handling, and CI wiring  
> **Boundary:** server-side source-admission access helper only; no browser token exposure, no downstream-product collapse, no direct publication.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed responsibilities](#allowed-responsibilities) · [Forbidden responsibilities](#forbidden-responsibilities) · [Downstream products](#downstream-products) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation](#validation) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/nasa-earthdata/` is a proposed connector boundary for NASA Earthdata access-surface helpers.

The source catalog frames NASA Earthdata as the shared credentialed access surface for downstream NASA products such as SMAP, HLS/HLS-VI, FIRMS, and MAIAC AOD candidates. Product-specific catalog records, SourceDescriptors, STAC/DCAT/PROV records, domain projections, rights review, sensitivity review, and release decisions belong with the downstream products and governed KFM lifecycle records.

This folder may support source discovery, access-surface metadata, server-side retrieval preparation, source fingerprint preservation, fetch receipt preparation, and RAW/QUARANTINE handoff envelopes. It must not become a public map dependency, measurement product root, source registry, policy root, release root, or publication path.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/nasa-earthdata/` | NASA Earthdata access-surface connector boundary. | **CONFIRMED path / PROPOSED beyond §7.3** |
| `docs/sources/catalog/nasa/nasa-earthdata.md` | NASA Earthdata product/access-surface catalog page. | **CONFIRMED** |
| `docs/sources/catalog/nasa/README.md` | NASA source-family catalog page. | **CONFIRMED / PROPOSED beyond §7.3** |
| `connectors/nasa-firms/`, `connectors/nasa-hls/`, `connectors/nasa-smap/` | Downstream product connector lanes. | **NEEDS VERIFICATION** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside connector / NEEDS VERIFICATION for entries** |
| `data/raw/` and `data/quarantine/` | Allowed connector handoff targets. | **Outside connector** |
| `release/` | Release and publication controls. | **Out of scope for this connector** |

---

## Allowed responsibilities

This folder may support helpers for:

- Earthdata/CMR access-surface metadata;
- server-side discovery request preparation;
- downstream-product collection and granule reference preservation;
- source URI, retrieval timestamp, cache validator, and source fingerprint preservation;
- descriptor and activation precondition checks;
- product-family routing to SMAP, HLS, FIRMS, MAIAC, or other governed NASA product lanes;
- RAW or QUARANTINE handoff envelopes;
- deterministic fail-closed errors when access, descriptor, rights, product identity, or provenance is unresolved.

---

## Forbidden responsibilities

This folder must not:

- expose credentials, tokens, or protected source access to public clients;
- treat Earthdata as a STAC collection or measurement product;
- collapse SMAP, HLS, FIRMS, MAIAC, or other NASA products into one source role;
- decide rights, sensitivity, release class, or public visibility;
- write directly to processed, catalog, triplet, published, proof, receipt, or release roots;
- emit public maps, public APIs, public summaries, or release artifacts;
- treat `connectors/nasa-earthdata/` or the NASA family as canonical §7.3 infrastructure before OPEN-DSC-14 is resolved.

[Back to top ↑](#top)

---

## Downstream products

NASA Earthdata is an access surface. Downstream product records remain separate:

| Product lane | Role of Earthdata | Status |
|---|---|---:|
| NASA SMAP | Access/discovery and authenticated retrieval surface. | **NEEDS VERIFICATION per product descriptor** |
| NASA HLS / HLS-VI | Access/discovery and authenticated retrieval surface. | **NEEDS VERIFICATION per product descriptor** |
| NASA FIRMS | Access or discovery relationship depends on endpoint/product details. | **NEEDS VERIFICATION** |
| NASA MAIAC AOD | Candidate access/discovery relationship noted in catalog. | **NEEDS VERIFICATION; product page not confirmed here** |

Product-specific truth, rights, sensitivity, cadence, spatial/temporal identity, and release posture belong to product descriptors and downstream catalog records, not this access-surface connector.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/nasa-earthdata/README.md` | **CONFIRMED** | Target file existed and was blank before this update. | Does not prove connector code, tests, credentials handling, or CI. |
| `docs/sources/catalog/nasa/nasa-earthdata.md` | **CONFIRMED** | Earthdata is an access surface, not a measurement product; no browser token exposure is a governance requirement; downstream products remain separate. | Endpoint details, current auth behavior, and implementation remain unverified. |
| `docs/sources/catalog/nasa/README.md` | **CONFIRMED** | NASA family is draft/PROPOSED, beyond Directory Rules §7.3, and awaits OPEN-DSC-14; companion connector folders are listed but need verification. | Does not ratify the connector as canonical. |
| Actual connector implementation | **NEEDS VERIFICATION** | This README defines intended boundaries. | Actual modules, fixtures, tests, endpoint access, and CI remain unverified. |

---

## Runtime posture

Default runtime posture:

- no public client access to protected source credentials or protected source catalogs;
- no source activation without SourceDescriptor and review state;
- no product-role collapse across NASA downstream products;
- no public output;
- no release artifact creation;
- no direct writes beyond RAW or QUARANTINE handoff envelopes;
- deterministic failure when descriptor, access state, product identity, rights state, provenance, or source shape is unresolved.

---

## Validation

Validation should check that:

- Earthdata is treated as an access surface, not a measurement product;
- downstream product identity is explicit;
- source URI, retrieval timestamp, cache validator, and source fingerprint are preserved where applicable;
- credentials and protected source access remain server-side only;
- SourceDescriptor and activation preconditions are required;
- rights and product identity are explicit or route to quarantine/abstention;
- connector output is limited to RAW or QUARANTINE handoff;
- no release/public artifact is emitted by this connector.

Tests must prove these boundaries before implementation maturity is claimed.

---

## Rollback

Rollback is required if this README is used to justify public credential exposure, source activation, NASA-family canonicality, product-role collapse, direct publication, or implementation maturity without verified tests and review evidence.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the file was blank before this update, a safe rollback is to restore the blank placeholder or replace this document with a shorter access-surface boundary note until OPEN-DSC-14 and implementation are verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Resolve OPEN-DSC-14 for NASA source-family placement. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm actual connector files under `connectors/nasa-earthdata/`. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm SourceDescriptor and activation gate wiring. | **NEEDS VERIFICATION** | Registry entries, code, and tests. |
| Confirm current access, discovery, auth, and cache behavior. | **NEEDS VERIFICATION** | Current source documentation and steward review. |
| Confirm downstream product routing. | **NEEDS VERIFICATION** | Product descriptors, code, and tests. |
| Confirm RAW/QUARANTINE handoff envelope shape. | **NEEDS VERIFICATION** | Schemas/contracts and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this connector as an access-surface helper. NASA product truth belongs to downstream product descriptors, EvidenceBundles, catalog records, and release artifacts after governed validation and review.

[Back to top ↑](#top)
