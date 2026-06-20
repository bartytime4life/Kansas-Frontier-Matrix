<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nasa-smap-readme
title: connectors/nasa-smap/ — NASA SMAP Connector Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward for NASA · Soil steward · Agriculture steward · Rights reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; connector-boundary; nasa-smap; smap; model-assimilated-reference; surface-root-zone-separated; beyond-directory-rules-7-3; open-dsc-14; no-publication
proposed_path: connectors/nasa-smap/README.md
truth_posture: CONFIRMED path exists / PROPOSED NASA connector family beyond §7.3 / IMPLEMENTATION DEPTH NEEDS VERIFICATION
related:
  - ../README.md
  - ../nasa-earthdata/README.md
  - ../nasa-hls/README.md
  - ../nasa-firms/README.md
  - ../../docs/sources/catalog/nasa/README.md
  - ../../docs/sources/catalog/nasa/nasa-smap.md
  - ../../docs/sources/catalog/nasa/nasa-earthdata.md
  - ../../docs/sources/catalog/nasa/nasa-hls.md
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
tags: [kfm, connectors, nasa, nasa-smap, smap, soil-moisture, ldas, enkf, ease-grid, soil, agriculture, model-assimilated, nrt, reprocessed, supersession, raw, quarantine, governance]
notes:
  - "This README fills a blank `connectors/nasa-smap/README.md` file."
  - "The NASA source-family README says the NASA family is PROPOSED, beyond Directory Rules §7.3, and awaits OPEN-DSC-14."
  - "The NASA SMAP product page frames SMAP L4 as a model-assimilated LDAS/EnKF reference product, not raw observation truth."
  - "Surface and root-zone semantics must remain separate; NRT and reprocessed products must preserve cadence and supersession metadata."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NASA SMAP Connector Boundary

> Connector-boundary README for `connectors/nasa-smap/`. NASA SMAP material enters KFM as satellite-derived and model-assimilated soil-moisture source material. This connector does not create raw observation truth, field truth, public drought truth, or release artifacts by itself.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family status: beyond §7.3" src="https://img.shields.io/badge/family-beyond__%C2%A77.3-orange">
  <img alt="Open item: OPEN-DSC-14" src="https://img.shields.io/badge/open-OPEN--DSC--14-orange">
  <img alt="Role: model-assimilated reference" src="https://img.shields.io/badge/role-model__assimilated__reference-yellow">
  <img alt="Semantics: surface/root-zone split" src="https://img.shields.io/badge/semantics-surface__rootzone__split-blue">
</p>

> [!IMPORTANT]
> **Status:** `draft` connector-boundary README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/nasa-smap/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `PROPOSED` NASA family beyond §7.3 · `NEEDS VERIFICATION` implementation files, tests, fixtures, endpoint details, and CI wiring  
> **Boundary:** source-admission helper only; SMAP L4 must remain labeled as model-assimilated reference moisture and surface/root-zone outputs must not be merged by convenience.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed responsibilities](#allowed-responsibilities) · [Forbidden responsibilities](#forbidden-responsibilities) · [Semantic posture](#semantic-posture) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation](#validation) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/nasa-smap/` is a proposed connector boundary for NASA SMAP soil-moisture source admission.

The source catalog frames SMAP L4 as a model-assimilated LDAS/EnKF reference product, not raw observation truth. It also requires surface and root-zone semantics to remain separate, with NRT and reprocessed cadence classes preserved.

This folder may support source discovery/fetch preparation, granule metadata preservation, dataset-version and cadence tagging, EASE-Grid identity preservation, surface/root-zone separation, source fingerprinting, supersession metadata, and RAW/QUARANTINE handoff envelopes. It must not become a release root, public API, field-truth authority, or publication path.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/nasa-smap/` | NASA SMAP soil-moisture connector boundary. | **CONFIRMED path / PROPOSED beyond §7.3** |
| `docs/sources/catalog/nasa/nasa-smap.md` | NASA SMAP product/source catalog page. | **CONFIRMED** |
| `docs/sources/catalog/nasa/README.md` | NASA source-family catalog page. | **CONFIRMED / PROPOSED beyond §7.3** |
| `connectors/nasa-earthdata/` | Related Earthdata access-surface connector boundary. | **CONFIRMED README / NEEDS IMPLEMENTATION VERIFICATION** |
| `connectors/nasa-hls/` | Related HLS context connector boundary. | **CONFIRMED README / NEEDS IMPLEMENTATION VERIFICATION** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside connector / NEEDS VERIFICATION for entries** |
| `data/raw/` and `data/quarantine/` | Allowed connector handoff targets. | **Outside connector** |
| `release/` | Release and publication controls. | **Out of scope for this connector** |

---

## Allowed responsibilities

This folder may support helpers for:

- SMAP source metadata preservation;
- L3, L4 surface, L4 root-zone, NRT, and reprocessed product identity preservation;
- source URI, retrieval timestamp, cache validator, and source fingerprint preservation;
- dataset-version, cadence class, and supersession metadata;
- EASE-Grid and native projection metadata preservation;
- separate surface and root-zone output references;
- SourceDescriptor and activation precondition checks;
- RAW or QUARANTINE handoff envelopes;
- deterministic fail-closed errors when descriptor, product identity, cadence, projection, rights state, or provenance is unresolved.

---

## Forbidden responsibilities

This folder must not:

- present SMAP L4 as raw measurement or ground truth;
- merge surface and root-zone outputs into one generic soil-moisture value by convenience;
- silently merge SMAP with Kansas Mesonet or other in-situ observations;
- collapse NRT and reprocessed products without supersession metadata;
- decide rights, sensitivity, release class, or public visibility;
- write directly to processed, catalog, triplet, published, proof, receipt, or release roots;
- emit public maps, public APIs, public summaries, alerts, or release artifacts;
- treat the NASA family as canonical §7.3 infrastructure before OPEN-DSC-14 is resolved.

[Back to top ↑](#top)

---

## Semantic posture

KFM language for this connector must stay precise:

| SMAP material | Required posture | Forbidden before downstream proof |
|---|---|---|
| SMAP L4 surface | Model-assimilated reference moisture for surface layer. | Raw measurement or ground truth. |
| SMAP L4 root-zone | Model-assimilated reference moisture for root-zone layer. | Interchangeable with surface moisture. |
| SMAP NRT | Preliminary cadence class with explicit dataset version and timestamp. | Final analytical truth. |
| Standard/reprocessed products | Higher-confidence analytical candidate after supersession handling. | Public truth without release review. |
| Mesonet comparison | Independent comparator or sibling evidence. | Silent merge. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/nasa-smap/README.md` | **CONFIRMED** | Target file existed and was blank before this update. | Does not prove connector code, tests, endpoint access, or CI. |
| `docs/sources/catalog/nasa/nasa-smap.md` | **CONFIRMED** | SMAP L4 is model-assimilated reference moisture, not raw observation truth; surface/root-zone and NRT/reprocessed distinctions are required. | Endpoint details, current terms, and implementation remain unverified. |
| `docs/sources/catalog/nasa/README.md` | **CONFIRMED** | NASA family is draft/PROPOSED, beyond Directory Rules §7.3, and awaits OPEN-DSC-14. | Does not ratify the connector as canonical. |
| Actual connector implementation | **NEEDS VERIFICATION** | This README defines intended boundaries. | Actual modules, fixtures, tests, endpoint access, and CI remain unverified. |

---

## Runtime posture

Default runtime posture:

- no field-truth claims from connector output;
- no raw-observation claim for model-assimilated L4 products;
- no surface/root-zone merge by convenience;
- no SMAP/Mesonet silent merge;
- no source activation without SourceDescriptor and review state;
- no public output;
- no release artifact creation;
- no direct writes beyond RAW or QUARANTINE handoff envelopes;
- deterministic failure when descriptor, product identity, cadence, projection, rights state, provenance, layer semantics, or supersession state is unresolved.

---

## Validation

Validation should check that:

- SMAP L4 is labeled as model-assimilated reference moisture;
- surface and root-zone outputs remain separate;
- SMAP and in-situ observations remain distinct unless an explicit reviewed crosswalk says otherwise;
- source URI, retrieval timestamp, dataset version, cadence class, and source fingerprint are preserved where applicable;
- NRT and reprocessed records retain supersession metadata where applicable;
- EASE-Grid/native projection metadata is preserved where applicable;
- SourceDescriptor and activation preconditions are required;
- connector output is limited to RAW or QUARANTINE handoff;
- no release/public artifact is emitted by this connector.

Tests must prove these boundaries before implementation maturity is claimed.

---

## Rollback

Rollback is required if this README is used to justify raw-measurement claims for SMAP L4, surface/root-zone merge, SMAP/Mesonet silent merge, NASA-family canonicality, source activation, direct publication, or implementation maturity without verified tests and review evidence.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the file was blank before this update, a safe rollback is to restore the blank placeholder or replace this document with a shorter model-reference boundary note until OPEN-DSC-14 and implementation are verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Resolve OPEN-DSC-14 for NASA source-family placement. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm actual connector files under `connectors/nasa-smap/`. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm SourceDescriptor and activation gate wiring. | **NEEDS VERIFICATION** | Registry entries, code, and tests. |
| Confirm current SMAP dataset IDs, access, cadence, and cache behavior. | **NEEDS VERIFICATION** | Current source documentation and steward review. |
| Confirm surface/root-zone separation and supersession handling. | **NEEDS VERIFICATION** | Product descriptors, code, and tests. |
| Confirm RAW/QUARANTINE handoff envelope shape. | **NEEDS VERIFICATION** | Schemas/contracts and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this connector conservative. SMAP can support soil and agriculture context after governed gates, but SMAP L4 remains model-assimilated reference moisture and must not be presented as raw observation truth.

[Back to top ↑](#top)
