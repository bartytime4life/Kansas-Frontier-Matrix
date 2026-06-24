<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-fauna-compat-readme
title: contracts/fauna — Fauna Contract Compatibility README
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Contract steward · Fauna steward · Docs steward · Directory Rules reviewer
created: 2026-06-24
updated: 2026-06-24
policy_label: public; contracts; fauna; compatibility; no-parallel-authority
related:
  - ../README.md
  - ../domains/fauna/README.md
  - ../../docs/domains/fauna/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../schemas/contracts/v1/domains/fauna/
  - ../../policy/domains/fauna/
  - ../../policy/sensitivity/fauna/
  - ../../tests/domains/fauna/
  - ../../fixtures/domains/fauna/
tags: [kfm, contracts, fauna, compatibility, directory-rules, semantic-contracts, geoprivacy, no-parallel-authority]
notes:
  - "Compatibility pointer for the legacy/requested `contracts/fauna/` path."
  - "The canonical semantic contract lane is `contracts/domains/fauna/` unless an accepted ADR changes Directory Rules."
  - "Do not place object contracts, schemas, policy, fixtures, data, release records, runtime code, or UI code here."
  - "Previous file content was a placeholder; rollback target is blob SHA `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/fauna

> Compatibility guard for the legacy Fauna contract path; use `contracts/domains/fauna/` for canonical Fauna semantic contracts.

<p>
  <img alt="Status: deprecated compatibility guard" src="https://img.shields.io/badge/status-deprecated-lightgrey">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Domain: fauna" src="https://img.shields.io/badge/domain-fauna-2ea44f">
  <img alt="Authority: pointer only" src="https://img.shields.io/badge/authority-pointer__only-orange">
  <img alt="Canonical lane: contracts/domains/fauna" src="https://img.shields.io/badge/canonical-contracts%2Fdomains%2Ffauna-blueviolet">
  <img alt="Sensitivity: fail closed" src="https://img.shields.io/badge/sensitivity-fail__closed-critical">
</p>

**Status:** `deprecated` compatibility guard  
**Owners:** `OWNER_TBD` — Contract steward · Fauna steward · Docs steward · Directory Rules reviewer  
**Path:** `contracts/fauna/README.md`  
**Canonical semantic contract lane:** [`../domains/fauna/`](../domains/fauna/)  
**Truth posture:** CONFIRMED repo placeholder replaced in draft content · CONFIRMED canonical Fauna contract lane exists · PROPOSED cleanup until maintainer review

## Quick jumps

[Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Compatibility flow](#compatibility-flow) · [Fauna safety rule](#fauna-safety-rule) · [Migration checklist](#migration-checklist) · [Rollback](#rollback)

---

## Scope

`contracts/fauna/` is **not** the canonical Fauna contract lane.

This README exists so a legacy, mistaken, or user-requested path does not silently become a second contract authority. New Fauna semantic contract work belongs in [`contracts/domains/fauna/`](../domains/fauna/), where contract files define object meaning while remaining separate from schemas, policy, fixtures, lifecycle data, release records, runtime code, and UI code.

> [!IMPORTANT]
> **Do not add Fauna object contracts here.** If a contract defines the meaning of `Taxon`, `OccurrenceEvidence`, `SensitiveSite`, `RangePolygon`, `MonitoringEvent`, redaction/publication support, or another Fauna object family, place it under `contracts/domains/fauna/` unless an accepted ADR changes the Directory Rules pattern.

---

## Repo fit

Directory placement is part of KFM governance. This file is a pointer at a drift-prone path, not a new authority root.

| Responsibility | Canonical or expected path | This file's role |
|---|---|---|
| Root contract purpose | [`../README.md`](../README.md) | Inherits the contract/schemas/policy split. |
| Fauna semantic contracts | [`../domains/fauna/`](../domains/fauna/) | Points there; does not duplicate it. |
| Fauna domain doctrine | [`../../docs/domains/fauna/README.md`](../../docs/domains/fauna/README.md) | Linked domain context only. |
| Machine schemas | [`../../schemas/contracts/v1/domains/fauna/`](../../schemas/contracts/v1/domains/fauna/) | Shape authority; not owned here. |
| Fauna policy | [`../../policy/domains/fauna/`](../../policy/domains/fauna/) | Admissibility and release authority; not owned here. |
| Sensitivity policy | [`../../policy/sensitivity/fauna/`](../../policy/sensitivity/fauna/) | Geoprivacy and deny/default tiering; not owned here. |
| Tests and fixtures | [`../../tests/domains/fauna/`](../../tests/domains/fauna/), [`../../fixtures/domains/fauna/`](../../fixtures/domains/fauna/) | Proof and examples; not owned here. |
| Source registry | `../../data/registry/sources/fauna/` | Source identity, role, cadence, rights, and terms; not owned here. |
| Release and rollback | `../../release/candidates/fauna/`, `../../release/manifests/` | Promotion and rollback authority; not owned here. |

The clean split is:

- `contracts/` defines **semantic meaning**.
- `schemas/contracts/v1/` defines **machine-checkable shape**.
- `policy/` decides **allow / deny / restrict / abstain**.
- `tests/` and `fixtures/` prove the rules are enforceable.
- `data/` stores lifecycle records and emitted evidence-bearing artifacts.
- `release/` records promotion, manifests, rollback, and publication decisions.

---

## Accepted inputs

Only these belong under `contracts/fauna/` while this compatibility path exists:

| Accepted item | Purpose | Status |
|---|---|---|
| `README.md` | Compatibility guard and redirect to `contracts/domains/fauna/`. | Accepted |
| Short migration note | Temporary note explaining how any misplaced file was moved. | Allowed only during cleanup |
| Backlink audit note | Temporary note listing inbound references to this legacy path. | Allowed only during cleanup |

No other durable content should be added here.

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| Fauna object contract Markdown | `../domains/fauna/` | Avoids parallel semantic authority. |
| `.schema.json` files | `../../schemas/contracts/v1/domains/fauna/` | Schemas own machine shape. |
| Policy or Rego bundles | `../../policy/domains/fauna/`, `../../policy/sensitivity/fauna/` | Policy owns admissibility and release gates. |
| Source descriptors or source records | `../../data/registry/sources/fauna/` | Source identity, role, cadence, rights, and terms belong in the registry. |
| RAW / WORK / QUARANTINE / PROCESSED records | `../../data/<phase>/fauna/` | Lifecycle data is never contract meaning. |
| Published artifacts or layer bundles | `../../data/published/`, `../../release/` | Publication is a governed state transition. |
| Tests, fixtures, or validators | `../../tests/domains/fauna/`, `../../fixtures/domains/fauna/`, `../../tools/validators/` | Proof and execution do not live in contracts. |
| Evidence Drawer, Focus Mode, API, or UI code | `../../apps/`, `../../packages/` | Delivery surfaces are downstream carriers, not contract authority. |

> [!WARNING]
> A second Fauna contract lane at `contracts/fauna/` would make future review harder and could let stale semantic rules diverge from `contracts/domains/fauna/`. Treat new content here as drift unless it is only a pointer, migration note, or cleanup note.

---

## Compatibility flow

```mermaid
flowchart LR
  legacy["contracts/fauna/<br>compatibility guard"] -. points to .-> canonical["contracts/domains/fauna/<br>semantic contracts"]
  canonical --> schemas["schemas/contracts/v1/domains/fauna/<br>machine shape"]
  canonical --> policy["policy/domains/fauna/ + policy/sensitivity/fauna/<br>admissibility and geoprivacy"]
  canonical --> proof["tests/domains/fauna/ + fixtures/domains/fauna/<br>proof and examples"]
  canonical --> docs["docs/domains/fauna/<br>domain doctrine"]
  canonical --> release["release/ + data/published/<br>promotion and public artifacts"]
```

---

## Fauna safety rule

Fauna contract meaning is not publication permission.

Sensitive occurrence records, steward-controlled locations, and exact-location biodiversity material fail closed unless the governed path supplies the required evidence, rights, source role, sensitivity policy, review state, redaction/generalization receipt, release manifest, correction path, and rollback target.

For Focus Mode or Evidence Drawer use, this means:

- ask what can be safely shown, not how to expose exact sensitive detail;
- surface `ABSTAIN`, `DENY`, and `ERROR` as valid governed outcomes instead of smoothing them away;
- preserve visible precision status such as generalized, withheld, aggregate, or public-safe derivative;
- never treat generated text, rendered map properties, or an app payload as root truth.

---

## Migration checklist

When a file is found under `contracts/fauna/`:

- [ ] Confirm whether it is only this compatibility README.
- [ ] If it is semantic Markdown, move it to `contracts/domains/fauna/` after checking for an existing canonical sibling.
- [ ] If it is JSON Schema, move it to `schemas/contracts/v1/domains/fauna/`.
- [ ] If it is policy, move it to `policy/domains/fauna/` or `policy/sensitivity/fauna/`.
- [ ] If it is a fixture or test, move it to the appropriate `fixtures/` or `tests/` lane.
- [ ] If it is data, identify the lifecycle phase before moving it under `data/<phase>/fauna/`.
- [ ] If it is release-related, move it to `release/` or the appropriate published-artifact location.
- [ ] Add or update a drift-register entry when the move exposes a repeated placement pattern.
- [ ] Preserve history with `git mv` where possible.
- [ ] Keep rollback notes for any moved file.

---

## Verification checklist

- [ ] `contracts/fauna/` contains no durable object contracts beyond this pointer README.
- [ ] `contracts/domains/fauna/README.md` remains the canonical Fauna contract-lane guide.
- [ ] No `.schema.json`, policy bundle, fixture, data artifact, release manifest, runtime code, or UI code is normalized here.
- [ ] Inbound links to `contracts/fauna/` are either corrected or intentionally routed through this compatibility guard.
- [ ] Sensitive-location and source-role language remains fail-closed and evidence-subordinate.
- [ ] Cleanup is reviewed by the Contract steward, Fauna steward, Docs steward, and Directory Rules reviewer.

---

## Rollback

Rollback is required if this compatibility guard is used to justify keeping new contract authority under `contracts/fauna/`, if it weakens the canonical `contracts/domains/fauna/` lane, or if it obscures where schemas, policy, evidence, fixtures, release records, or public artifacts belong.

Rollback target for this replacement: previous placeholder blob SHA `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a`.

<p align="right"><a href="#top">Back to top</a></p>