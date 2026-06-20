<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nasa-readme
title: connectors/nasa/ — NASA Connector Family Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward for NASA · Earth-observation steward · Rights reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; connector-family-boundary; nasa; beyond-directory-rules-7-3; open-dsc-14; earth-observation; no-publication
proposed_path: connectors/nasa/README.md
truth_posture: CONFIRMED path exists / PROPOSED NASA connector family beyond §7.3 / IMPLEMENTATION DEPTH NEEDS VERIFICATION
related:
  - ../README.md
  - ../nasa-earthdata/README.md
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
  - ../../policy/sensitivity/
  - ../../release/
tags: [kfm, connectors, nasa, earth-observation, earthdata, firms, hls, smap, source-admission, raw, quarantine, governance, open-dsc-14]
notes:
  - "This README fills a blank `connectors/nasa/README.md` file."
  - "The NASA source-family catalog README says NASA is PROPOSED, beyond Directory Rules §7.3, and awaits OPEN-DSC-14."
  - "This umbrella connector boundary coordinates NASA product connector lanes but does not make NASA canonical §7.3 infrastructure."
  - "Downstream product connectors retain separate product identity, source roles, evidence, policy, and release gates."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NASA Connector Family Boundary

> Umbrella connector-family boundary for `connectors/nasa/`. This folder may coordinate NASA Earth-observation source-admission helpers, but it is **PROPOSED** beyond Directory Rules §7.3 until `OPEN-DSC-14` is resolved. It is not a source registry, schema root, policy root, release root, public API, or publication path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family status: beyond §7.3" src="https://img.shields.io/badge/family-beyond__%C2%A77.3-orange">
  <img alt="Open item: OPEN-DSC-14" src="https://img.shields.io/badge/open-OPEN--DSC--14-orange">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` connector-family README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/nasa/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `PROPOSED` NASA family beyond §7.3 · `NEEDS VERIFICATION` implementation files, tests, fixtures, endpoint details, and CI wiring  
> **Boundary:** source-admission coordination only; no canonical-family ratification, no product-role collapse, no direct publication.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Product lanes](#product-lanes) · [Allowed responsibilities](#allowed-responsibilities) · [Forbidden responsibilities](#forbidden-responsibilities) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation](#validation) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/nasa/` is the umbrella connector boundary for proposed NASA Earth-observation connector lanes.

It may coordinate product-specific source-admission helpers for Earthdata, FIRMS, HLS, SMAP, and future NASA products only if each downstream product keeps separate identity, source role, provenance, rights, sensitivity, cadence, uncertainty, validation, and release posture.

This folder must not collapse NASA products into one source role or treat NASA as canonical §7.3 connector infrastructure before the open directory decision is resolved.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/nasa/` | Umbrella NASA connector-family boundary. | **CONFIRMED path / PROPOSED beyond §7.3** |
| `docs/sources/catalog/nasa/README.md` | NASA source-family catalog page. | **CONFIRMED / PROPOSED beyond §7.3** |
| `connectors/nasa-earthdata/` | Earthdata access-surface boundary. | **CONFIRMED README / NEEDS IMPLEMENTATION VERIFICATION** |
| `connectors/nasa-firms/` | FIRMS candidate-detection boundary. | **CONFIRMED README / NEEDS IMPLEMENTATION VERIFICATION** |
| `connectors/nasa-hls/` | HLS context-layer boundary. | **CONFIRMED README / NEEDS IMPLEMENTATION VERIFICATION** |
| `connectors/nasa-smap/` | SMAP model-reference boundary. | **CONFIRMED README / NEEDS IMPLEMENTATION VERIFICATION** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside connector / NEEDS VERIFICATION for entries** |
| `data/raw/` and `data/quarantine/` | Allowed connector handoff targets. | **Outside connector** |
| `release/` | Release and publication controls. | **Out of scope for this connector family** |

---

## Product lanes

| Connector lane | Product or surface | Boundary |
|---|---|---|
| `connectors/nasa-earthdata/` | Earthdata Login / CMR access surface. | Access surface only; not a measurement product. |
| `connectors/nasa-firms/` | FIRMS remote-sensing detections. | Candidate detections only; no public confirmation by connector. |
| `connectors/nasa-hls/` | HLS / HLS-VI harmonized imagery. | Context layer only; claims require downstream mask evidence. |
| `connectors/nasa-smap/` | SMAP soil-moisture products. | Model-assimilated reference moisture; surface/root-zone separated. |

The umbrella folder may coordinate shared conventions, but product-specific meaning belongs to product lanes and SourceDescriptors.

---

## Allowed responsibilities

This folder may support helpers for:

- shared NASA connector conventions;
- product-lane routing;
- common descriptor precondition checks;
- shared provenance fields;
- shared source fingerprint conventions;
- shared cache validator conventions;
- shared RAW or QUARANTINE handoff envelopes;
- shared fail-closed errors when product identity, descriptor state, rights state, or provenance is unresolved.

---

## Forbidden responsibilities

This folder must not:

- make NASA canonical under Directory Rules §7.3 without ADR or migration evidence;
- collapse Earthdata, FIRMS, HLS, SMAP, MAIAC, or future NASA products into one source role;
- decide rights, sensitivity, release class, or public visibility;
- write directly to processed, catalog, triplet, published, proof, receipt, or release roots;
- expose protected source access to public clients;
- emit public maps, public APIs, public summaries, or release artifacts;
- bypass product-specific SourceDescriptors, validation, EvidenceBundles, policy review, correction paths, or rollback targets.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/nasa/README.md` | **CONFIRMED** | Target file existed and was blank before this update. | Does not prove connector code, tests, endpoint access, or CI. |
| `docs/sources/catalog/nasa/README.md` | **CONFIRMED** | NASA family is draft/PROPOSED, beyond Directory Rules §7.3, awaits OPEN-DSC-14, and lists Earthdata, FIRMS, HLS, and SMAP product pages. | Does not ratify the connector family as canonical. |
| `connectors/nasa-earthdata/README.md` | **CONFIRMED** | Earthdata connector boundary exists as access-surface README. | Does not prove implementation maturity. |
| `connectors/nasa-firms/README.md` | **CONFIRMED** | FIRMS connector boundary exists as candidate-detection README. | Does not prove implementation maturity. |
| `connectors/nasa-hls/README.md` | **CONFIRMED** | HLS connector boundary exists as context-layer README. | Does not prove implementation maturity. |
| `connectors/nasa-smap/README.md` | **CONFIRMED** | SMAP connector boundary exists as model-reference README. | Does not prove implementation maturity. |
| Actual connector implementation | **NEEDS VERIFICATION** | This README defines intended boundaries. | Actual modules, fixtures, tests, endpoint access, and CI remain unverified. |

---

## Runtime posture

Default runtime posture:

- no canonical-family claim until OPEN-DSC-14 is resolved;
- no product-role collapse;
- no source activation without product-specific SourceDescriptor and review state;
- no public output;
- no release artifact creation;
- no direct writes beyond RAW or QUARANTINE handoff envelopes;
- deterministic failure when product identity, descriptor state, rights state, provenance, or source shape is unresolved.

---

## Validation

Validation should check that:

- each NASA product keeps separate source identity and source role;
- Earthdata remains an access surface;
- FIRMS remains candidate detection material;
- HLS remains context material requiring mask evidence downstream;
- SMAP L4 remains model-assimilated reference material with surface/root-zone separation;
- SourceDescriptor and activation preconditions are product-specific;
- connector output is limited to RAW or QUARANTINE handoff;
- no release/public artifact is emitted by the umbrella connector.

---

## Rollback

Rollback is required if this README is used to justify NASA-family canonicality, product-role collapse, source activation, direct publication, public protected-source access, or implementation maturity without verified tests and review evidence.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the file was blank before this update, a safe rollback is to restore the blank placeholder or replace this document with a shorter proposed-family boundary note until OPEN-DSC-14 and implementation are verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Resolve OPEN-DSC-14 for NASA source-family placement. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm actual connector files under `connectors/nasa/`. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm product-specific SourceDescriptors and activation gates. | **NEEDS VERIFICATION** | Registry entries, code, and tests. |
| Confirm shared NASA connector conventions. | **NEEDS VERIFICATION** | Code, fixtures, and package docs. |
| Confirm RAW/QUARANTINE handoff envelope shape. | **NEEDS VERIFICATION** | Schemas/contracts and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this folder as an umbrella boundary only. Product truth belongs to product-specific descriptors, EvidenceBundles, catalog records, policy decisions, and released artifacts after governed validation and review.

[Back to top ↑](#top)
