<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nasa-hls-readme
title: connectors/nasa-hls/ — NASA HLS Connector Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward for NASA · Agriculture steward · Remote-sensing steward · Rights reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; connector-boundary; nasa-hls; hls; context-layer; mask-gated; beyond-directory-rules-7-3; open-dsc-14; no-publication
proposed_path: connectors/nasa-hls/README.md
truth_posture: CONFIRMED path exists / PROPOSED NASA connector family beyond §7.3 / IMPLEMENTATION DEPTH NEEDS VERIFICATION
related:
  - ../README.md
  - ../nasa-earthdata/README.md
  - ../nasa-firms/README.md
  - ../../docs/sources/catalog/nasa/README.md
  - ../../docs/sources/catalog/nasa/nasa-hls.md
  - ../../docs/sources/catalog/nasa/nasa-earthdata.md
  - ../../docs/sources/catalog/nasa/nasa-firms.md
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
  - ../../policy/sensitivity/
  - ../../release/
tags: [kfm, connectors, nasa, nasa-hls, hls, hls-vi, landsat, sentinel-2, vegetation, agriculture, remote-sensing, context-layer, mask-gate, raw, quarantine, governance]
notes:
  - "This README fills a blank `connectors/nasa-hls/README.md` file."
  - "The NASA source-family README says the NASA family is PROPOSED, beyond Directory Rules §7.3, and awaits OPEN-DSC-14."
  - "The NASA HLS product page frames HLS as a context layer, not field truth."
  - "HLS-derived analytical claims require explicit mask evidence and downstream validation; this connector may support source admission only."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NASA HLS Connector Boundary

> Connector-boundary README for `connectors/nasa-hls/`. NASA HLS and HLS-VI material enters KFM as harmonized remote-sensing source material and context evidence. This connector does not create field truth, vegetation-change truth, public alerts, or release artifacts by itself.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family status: beyond §7.3" src="https://img.shields.io/badge/family-beyond__%C2%A77.3-orange">
  <img alt="Open item: OPEN-DSC-14" src="https://img.shields.io/badge/open-OPEN--DSC--14-orange">
  <img alt="Role: context layer" src="https://img.shields.io/badge/role-context__layer-yellow">
  <img alt="Mask gate: required" src="https://img.shields.io/badge/mask__gate-required-red">
</p>

> [!IMPORTANT]
> **Status:** `draft` connector-boundary README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/nasa-hls/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `PROPOSED` NASA family beyond §7.3 · `NEEDS VERIFICATION` implementation files, tests, fixtures, endpoint details, and CI wiring  
> **Boundary:** source-admission helper only; HLS without masks is not eligible for downstream analytical claims.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed responsibilities](#allowed-responsibilities) · [Forbidden responsibilities](#forbidden-responsibilities) · [Mask posture](#mask-posture) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation](#validation) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/nasa-hls/` is a proposed connector boundary for NASA Harmonized Landsat–Sentinel-2 and HLS-VI source admission.

The source catalog frames HLS as a context layer, not field truth. HLS scenes, bands, sidecars, vegetation indices, and derived candidate rasters must preserve mask state, reference period, uncertainty, source identity, and provenance before any downstream claim can be promoted.

This folder may support source discovery/fetch preparation, scene metadata preservation, product identity preservation, QA/mask metadata preservation, valid-pixel footprint preparation, source fingerprinting, and RAW/QUARANTINE handoff envelopes. It must not become a release root, public API, field-truth authority, or publication path.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/nasa-hls/` | NASA HLS context-layer connector boundary. | **CONFIRMED path / PROPOSED beyond §7.3** |
| `docs/sources/catalog/nasa/nasa-hls.md` | NASA HLS product/source catalog page. | **CONFIRMED** |
| `docs/sources/catalog/nasa/README.md` | NASA source-family catalog page. | **CONFIRMED / PROPOSED beyond §7.3** |
| `connectors/nasa-earthdata/` | Related Earthdata access-surface connector boundary. | **CONFIRMED README / NEEDS IMPLEMENTATION VERIFICATION** |
| `connectors/nasa-firms/` | Related FIRMS masking/context connector boundary. | **CONFIRMED README / NEEDS IMPLEMENTATION VERIFICATION** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside connector / NEEDS VERIFICATION for entries** |
| `data/raw/` and `data/quarantine/` | Allowed connector handoff targets. | **Outside connector** |
| `release/` | Release and publication controls. | **Out of scope for this connector** |

---

## Allowed responsibilities

This folder may support helpers for:

- HLS source metadata preservation;
- HLS L30, HLS S30, and HLS-VI product identity preservation;
- source URI, retrieval timestamp, cache validator, and source fingerprint preservation;
- scene, band, sidecar, and COG reference preservation;
- QA and mask metadata preservation;
- valid-pixel footprint preparation;
- cadence and dataset-version tagging;
- SourceDescriptor and activation precondition checks;
- RAW or QUARANTINE handoff envelopes;
- deterministic fail-closed errors when descriptor, source shape, mask state, product identity, rights state, or provenance is unresolved.

---

## Forbidden responsibilities

This folder must not:

- present HLS pixels or vegetation indices as field truth;
- emit vegetation-change claims without downstream mask evidence and release review;
- collapse HLS L30, HLS S30, HLS-VI, Landsat archive, MAIAC, or FIRMS roles into one source role;
- decide rights, sensitivity, release class, or public visibility;
- write directly to processed, catalog, triplet, published, proof, receipt, or release roots;
- emit public maps, public APIs, public summaries, alerts, or release artifacts;
- treat the NASA family as canonical §7.3 infrastructure before OPEN-DSC-14 is resolved.

[Back to top ↑](#top)

---

## Mask posture

HLS evidence is not complete without mask and uncertainty context.

| Required context | Purpose | Connector posture |
|---|---|---|
| HLS QA / scene mask | Screens unusable pixels and scene defects. | Preserve metadata; do not derive public claims. |
| Atmospheric context | Records aerosol or atmospheric uncertainty where applicable. | Preserve reference or route unresolved state downstream. |
| FIRMS context | Helps screen candidate fire-affected windows when used downstream. | Preserve relationship only; do not collapse product roles. |
| Valid-pixel footprint | Defines what pixels were eligible for downstream analysis. | May prepare candidate evidence artifact; not public by itself. |
| Reference period | Binds before/after or baseline/current comparisons. | Preserve; absence blocks promotion. |
| Uncertainty band | Bounds derived analytical claims. | Preserve or require downstream derivation. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/nasa-hls/README.md` | **CONFIRMED** | Target file existed and was blank before this update. | Does not prove connector code, tests, endpoint access, or CI. |
| `docs/sources/catalog/nasa/nasa-hls.md` | **CONFIRMED** | HLS is a context layer, not field truth; mask trail is required before analytical claims. | Endpoint details, current terms, and implementation remain unverified. |
| `docs/sources/catalog/nasa/README.md` | **CONFIRMED** | NASA family is draft/PROPOSED, beyond Directory Rules §7.3, and awaits OPEN-DSC-14. | Does not ratify the connector as canonical. |
| Actual connector implementation | **NEEDS VERIFICATION** | This README defines intended boundaries. | Actual modules, fixtures, tests, endpoint access, and CI remain unverified. |

---

## Runtime posture

Default runtime posture:

- no field-truth claims from connector output;
- no vegetation-change claims without downstream mask gates;
- no source activation without SourceDescriptor and review state;
- no public output;
- no release artifact creation;
- no direct writes beyond RAW or QUARANTINE handoff envelopes;
- deterministic failure when descriptor, source shape, mask state, product identity, rights state, provenance, reference period, or uncertainty is unresolved.

---

## Validation

Validation should check that:

- HLS is labeled as context/source material, not field truth;
- HLS L30, HLS S30, HLS-VI, and sibling products remain distinct;
- source URI, retrieval timestamp, dataset version, and source fingerprint are preserved where applicable;
- QA/mask metadata and valid-pixel footprint references are preserved where applicable;
- reference period and uncertainty metadata are preserved or required downstream;
- SourceDescriptor and activation preconditions are required;
- connector output is limited to RAW or QUARANTINE handoff;
- no release/public artifact is emitted by this connector.

Tests must prove these boundaries before implementation maturity is claimed.

---

## Rollback

Rollback is required if this README is used to justify field-truth claims, unmasked analytical claims, NASA-family canonicality, source activation, direct publication, or implementation maturity without verified tests and review evidence.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the file was blank before this update, a safe rollback is to restore the blank placeholder or replace this document with a shorter context-layer boundary note until OPEN-DSC-14 and implementation are verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Resolve OPEN-DSC-14 for NASA source-family placement. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm actual connector files under `connectors/nasa-hls/`. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm SourceDescriptor and activation gate wiring. | **NEEDS VERIFICATION** | Registry entries, code, and tests. |
| Confirm current HLS access, product identity, cadence, and cache behavior. | **NEEDS VERIFICATION** | Current source documentation and steward review. |
| Confirm mask and valid-pixel handling. | **NEEDS VERIFICATION** | Product descriptors, code, and tests. |
| Confirm RAW/QUARANTINE handoff envelope shape. | **NEEDS VERIFICATION** | Schemas/contracts and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this connector conservative. HLS can support agriculture and vegetation-change context after governed mask gates, but connector output alone is not field truth and is not a release artifact.

[Back to top ↑](#top)
