<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-nasa-smap-nested-readme
title: connectors/nasa/smap/ — NASA SMAP Nested Product-Lane Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward for NASA · Soil steward · Agriculture steward · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; nested-product-lane-boundary; nasa; smap; model-assimilated-reference; surface-root-zone-separated; beyond-directory-rules-7-3; open-dsc-14; no-publication
proposed_path: connectors/nasa/smap/README.md
truth_posture: CONFIRMED path exists / PROPOSED nested NASA product lane / IMPLEMENTATION DEPTH NEEDS VERIFICATION
related:
  - ../README.md
  - ../../nasa-smap/README.md
  - ../../nasa-earthdata/README.md
  - ../../../docs/sources/catalog/nasa/README.md
  - ../../../docs/sources/catalog/nasa/nasa-smap.md
  - ../../../docs/sources/catalog/nasa/nasa-earthdata.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/sources/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../release/
tags: [kfm, connectors, nasa, nested-lane, nasa-smap, smap, soil-moisture, model-assimilated, surface-root-zone, nrt, reprocessed, raw, quarantine, governance]
notes:
  - "This README fills a blank nested SMAP product-lane README under `connectors/nasa/`."
  - "The NASA source-family catalog README says NASA is PROPOSED, beyond Directory Rules §7.3, and awaits OPEN-DSC-14."
  - "The NASA SMAP product page frames SMAP L4 as a model-assimilated LDAS/EnKF reference product, not raw observation truth."
  - "The top-level `connectors/nasa-smap/README.md` is the sibling product connector boundary; this nested path must not create conflicting authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# NASA SMAP Nested Product-Lane Boundary

> Nested product-lane README for `connectors/nasa/smap/`. This path is a proposed nested lane under the NASA umbrella connector boundary. It must stay aligned with `connectors/nasa-smap/` and must not create a second authority for SMAP source truth, release, schema, policy, or public presentation.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family status: beyond §7.3" src="https://img.shields.io/badge/family-beyond__%C2%A77.3-orange">
  <img alt="Open item: OPEN-DSC-14" src="https://img.shields.io/badge/open-OPEN--DSC--14-orange">
  <img alt="Role: model-assimilated reference" src="https://img.shields.io/badge/role-model__assimilated__reference-yellow">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` nested product-lane README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/nasa/smap/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `PROPOSED` nested NASA product lane · `NEEDS VERIFICATION` implementation files, tests, fixtures, and CI wiring  
> **Boundary:** nested source-admission helper lane only; no canonical-family ratification, no source activation, no surface/root-zone merge, no direct publication.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Alignment with top-level lane](#alignment-with-top-level-lane) · [Allowed responsibilities](#allowed-responsibilities) · [Forbidden responsibilities](#forbidden-responsibilities) · [Semantic posture](#semantic-posture) · [Evidence ledger](#evidence-ledger) · [Validation](#validation) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/nasa/smap/` is a proposed nested product-lane location for SMAP source-admission helper code under the proposed NASA umbrella connector family.

SMAP material must retain product identity, model-assimilated reference status, surface/root-zone separation, cadence class, dataset version, native grid/projection context, provenance, rights state, and supersession state.

This folder may support source-admission helper organization only. Product truth belongs to SourceDescriptors, EvidenceBundles, catalog records, policies, release records, correction paths, and rollback targets outside this lane.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/nasa/smap/` | Nested SMAP product-lane boundary under NASA umbrella. | **CONFIRMED path / PROPOSED nested lane** |
| `connectors/nasa/README.md` | Umbrella NASA connector-family boundary. | **CONFIRMED / PROPOSED beyond §7.3** |
| `connectors/nasa-smap/README.md` | Sibling top-level SMAP connector boundary. | **CONFIRMED** |
| `docs/sources/catalog/nasa/nasa-smap.md` | NASA SMAP product/source catalog page. | **CONFIRMED** |
| `docs/sources/catalog/nasa/README.md` | NASA source-family catalog page. | **CONFIRMED / PROPOSED beyond §7.3** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside connector / NEEDS VERIFICATION for entries** |
| `data/raw/` and `data/quarantine/` | Allowed handoff targets. | **Outside connector** |
| `release/` | Release and publication controls. | **Out of scope for this lane** |

---

## Alignment with top-level lane

This nested path and `connectors/nasa-smap/` must not diverge.

Until an ADR or migration note chooses one placement, treat:

- `connectors/nasa-smap/` as the confirmed sibling product connector boundary README already present;
- `connectors/nasa/smap/` as a proposed nested lane under the NASA umbrella;
- both as documentation boundaries only unless implementation files, tests, workflows, and SourceDescriptors prove runtime behavior.

If both paths remain, a future ADR or migration note should define whether one becomes compatibility-only, whether one is canonical, and how imports/tests/fixtures are routed.

---

## Allowed responsibilities

This nested lane may support helpers for:

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

This nested lane must not:

- present SMAP L4 as raw measurement or ground truth;
- merge surface and root-zone outputs into one generic soil-moisture value by convenience;
- silently merge SMAP with Kansas Mesonet or other in-situ observations;
- collapse NRT and reprocessed products without supersession metadata;
- decide rights, sensitivity, release class, or public visibility;
- write directly to processed, catalog, triplet, published, proof, receipt, or release roots;
- emit public maps, public APIs, public summaries, alerts, or release artifacts;
- treat the NASA family as canonical §7.3 infrastructure before OPEN-DSC-14 is resolved.

---

## Semantic posture

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
| `connectors/nasa/smap/README.md` | **CONFIRMED** | Target file existed and was blank before this update. | Does not prove nested implementation, tests, or CI. |
| `connectors/nasa/README.md` | **CONFIRMED** | NASA umbrella boundary exists and is proposed beyond §7.3. | Does not ratify NASA as canonical. |
| `connectors/nasa-smap/README.md` | **CONFIRMED** | Top-level SMAP connector boundary exists. | Does not prove implementation maturity. |
| `docs/sources/catalog/nasa/nasa-smap.md` | **CONFIRMED** | SMAP L4 is model-assimilated reference moisture, not raw observation truth; surface/root-zone and NRT/reprocessed distinctions are required. | Endpoint details, current terms, and implementation remain unverified. |
| Actual connector implementation | **NEEDS VERIFICATION** | This README defines intended boundaries. | Actual modules, fixtures, tests, endpoint access, and CI remain unverified. |

---

## Validation

Validation should check that:

- nested and top-level SMAP connector lanes do not make conflicting claims;
- SMAP L4 is labeled as model-assimilated reference moisture;
- surface and root-zone outputs remain separate;
- SMAP and in-situ observations remain distinct unless an explicit reviewed crosswalk says otherwise;
- dataset version, cadence class, source URI, retrieval timestamp, and source fingerprint are preserved where applicable;
- NRT and reprocessed records retain supersession metadata where applicable;
- connector output is limited to RAW or QUARANTINE handoff;
- no release/public artifact is emitted by this lane.

---

## Rollback

Rollback is required if this README is used to justify nested-path canonicality, raw-measurement claims for SMAP L4, surface/root-zone merge, SMAP/Mesonet silent merge, source activation, direct publication, or implementation maturity without verified tests and review evidence.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the file was blank before this update, a safe rollback is to restore the blank placeholder or replace this document with a shorter nested-lane boundary note until OPEN-DSC-14 and implementation placement are verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Resolve OPEN-DSC-14 for NASA source-family placement. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Decide relation between `connectors/nasa/smap/` and `connectors/nasa-smap/`. | **NEEDS VERIFICATION** | ADR, migration note, or package README decision. |
| Confirm actual nested connector files under `connectors/nasa/smap/`. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm SourceDescriptor and activation gate wiring. | **NEEDS VERIFICATION** | Registry entries, code, and tests. |
| Confirm surface/root-zone separation and supersession handling. | **NEEDS VERIFICATION** | Product descriptors, code, and tests. |
| Confirm RAW/QUARANTINE handoff envelope shape. | **NEEDS VERIFICATION** | Schemas/contracts and tests. |

---

## Maintainer note

Keep this nested lane subordinate to governed placement decisions. It may organize SMAP helper code only if it does not conflict with the umbrella NASA boundary or the sibling `connectors/nasa-smap/` boundary.

[Back to top ↑](#top)
