<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nasa-firms-readme
title: connectors/nasa-firms/ — NASA FIRMS Connector Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward for NASA · Hazards steward · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; connector-boundary; nasa-firms; candidate-detections; beyond-directory-rules-7-3; open-dsc-14; no-publication
proposed_path: connectors/nasa-firms/README.md
truth_posture: CONFIRMED path exists / PROPOSED NASA connector family beyond §7.3 / IMPLEMENTATION DEPTH NEEDS VERIFICATION
related:
  - ../README.md
  - ../nasa-earthdata/README.md
  - ../../docs/sources/catalog/nasa/README.md
  - ../../docs/sources/catalog/nasa/nasa-firms.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../docs/doctrine/directory-rules.md
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
tags: [kfm, connectors, nasa, nasa-firms, firms, candidate-detection, remote-sensing, hazards, raw, quarantine, governance]
notes:
  - "This README fills a blank `connectors/nasa-firms/README.md` file."
  - "The NASA source-family README says the NASA family is PROPOSED, beyond Directory Rules §7.3, and awaits OPEN-DSC-14."
  - "The NASA FIRMS product page frames records as candidate remote-sensing detections, not confirmed public events."
  - "This connector may support source-admission only; public-safe meaning is downstream of governed validation and release."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NASA FIRMS Connector Boundary

> Connector-boundary README for `connectors/nasa-firms/`. NASA FIRMS material enters KFM as **candidate remote-sensing detections** only. This connector does not confirm events, publish public layers, or bypass downstream validation and release gates.

> [!IMPORTANT]
> **Status:** `draft` connector-boundary README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/nasa-firms/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `PROPOSED` NASA family beyond §7.3 · `NEEDS VERIFICATION` implementation files, tests, fixtures, endpoint details, and CI wiring  
> **Boundary:** source-admission helper only; records remain candidate detections until downstream gates and release review.

---

## Scope

`connectors/nasa-firms/` is a proposed connector boundary for NASA FIRMS remote-sensing detection source admission.

The source catalog frames FIRMS records as candidate detections. KFM must preserve that candidate status through source admission and avoid upgrading the material into public truth from connector behavior alone.

This folder may support source-shape parsing, candidate record preservation, dataset-version tagging, retrieval timestamp preservation, supersession metadata, source fingerprinting, and RAW/QUARANTINE handoff envelopes. It must not become a release root, public API, or truth store.

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/nasa-firms/` | NASA FIRMS candidate-detection connector boundary. | **CONFIRMED path / PROPOSED beyond §7.3** |
| `docs/sources/catalog/nasa/nasa-firms.md` | NASA FIRMS product/source catalog page. | **CONFIRMED** |
| `docs/sources/catalog/nasa/README.md` | NASA source-family catalog page. | **CONFIRMED / PROPOSED beyond §7.3** |
| `connectors/nasa-earthdata/` | Related Earthdata access-surface connector boundary. | **CONFIRMED README / NEEDS IMPLEMENTATION VERIFICATION** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside connector / NEEDS VERIFICATION for entries** |
| `data/raw/` and `data/quarantine/` | Allowed connector handoff targets. | **Outside connector** |
| `release/` | Release and publication controls. | **Out of scope for this connector** |

---

## Allowed responsibilities

This folder may support helpers for:

- FIRMS source metadata preservation;
- candidate detection parsing and normalization without truth upgrade;
- source URI, retrieval timestamp, cache validator, and source fingerprint preservation;
- dataset-version and cadence tagging;
- supersession metadata preparation when records are replaced or revised;
- SourceDescriptor and activation precondition checks;
- RAW or QUARANTINE handoff envelopes;
- deterministic fail-closed errors when descriptor, source shape, product identity, rights state, or provenance is unresolved.

---

## Forbidden responsibilities

This folder must not:

- call a raw detection a confirmed public event;
- collapse near-real-time and revised records without supersession metadata;
- decide rights, sensitivity, release class, or public visibility;
- write directly to processed, catalog, triplet, published, proof, receipt, or release roots;
- emit public maps, public APIs, public summaries, or release artifacts;
- treat the NASA family as canonical §7.3 infrastructure before OPEN-DSC-14 is resolved.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/nasa-firms/README.md` | **CONFIRMED** | Target file existed and was blank before this update. | Does not prove connector code, tests, endpoint access, or CI. |
| `docs/sources/catalog/nasa/nasa-firms.md` | **CONFIRMED** | FIRMS records are candidate detections; cadence and supersession are governance concerns. | Endpoint details, current terms, and implementation remain unverified. |
| `docs/sources/catalog/nasa/README.md` | **CONFIRMED** | NASA family is draft/PROPOSED, beyond Directory Rules §7.3, and awaits OPEN-DSC-14. | Does not ratify the connector as canonical. |
| Actual connector implementation | **NEEDS VERIFICATION** | This README defines intended boundaries. | Actual modules, fixtures, tests, endpoint access, and CI remain unverified. |

---

## Validation

Validation should check that:

- FIRMS records are labeled as candidate detections;
- raw records are not labeled as confirmed public events;
- source URI, retrieval timestamp, dataset version, and source fingerprint are preserved where applicable;
- revised records retain supersession metadata where applicable;
- SourceDescriptor and activation preconditions are required;
- connector output is limited to RAW or QUARANTINE handoff;
- no release/public artifact is emitted by this connector.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Resolve OPEN-DSC-14 for NASA source-family placement. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm actual connector files under `connectors/nasa-firms/`. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm SourceDescriptor and activation gate wiring. | **NEEDS VERIFICATION** | Registry entries, code, and tests. |
| Confirm current FIRMS endpoint/cadence behavior. | **NEEDS VERIFICATION** | Source documentation and steward review. |
| Confirm RAW/QUARANTINE handoff envelope shape. | **NEEDS VERIFICATION** | Schemas/contracts and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this connector conservative. FIRMS records can support hazards context after governed gates, but raw records must remain candidate detections until downstream validation and release review.

[Back to top ↑](#top)
