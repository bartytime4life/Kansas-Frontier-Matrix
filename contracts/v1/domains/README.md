<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-v1-domains-readme
title: contracts/v1/domains/README.md — Versioned Domain Contract Compatibility README
type: readme
version: v0.1
status: draft; compatibility-guard; PROPOSED; path-needs-review; no-parallel-authority
owners: OWNER_TBD — Contracts steward · Domain stewards · Schema steward · Policy steward · Release steward · Docs steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-06-24
policy_label: public; contracts; v1; domains; compatibility; semantic-contracts; no-parallel-authority
tags: [kfm, contracts, v1, domains, compatibility, semantic-contracts, Directory Rules, EvidenceBundle, PolicyDecision, ReleaseManifest]
related:
  - ../../domains/README.md
  - ../../README.md
  - ../../../docs/architecture/contract-schema-policy-split.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../schemas/contracts/v1/
  - ../../../policy/domains/
  - ../../../fixtures/domains/
  - ../../../tests/domains/
  - ../../../release/
  - ./atmosphere/README.md
notes:
  - "This file replaces a blank placeholder at `contracts/v1/domains/README.md`."
  - "Current repo evidence identifies `contracts/domains/` as the active domain semantic-contract lane."
  - "`contracts/v1/domains/` is treated here as a compatibility/migration guard only, not a canonical contract root."
  - "Do not mirror `schemas/contracts/v1/` under `contracts/v1/` without ADR-backed path governance."
  - "Rollback target for this replacement is previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Versioned Domain Contract Compatibility README

> Compatibility guard for `contracts/v1/domains/`. The active domain semantic-contract lane is `contracts/domains/`; this versioned path must not become a parallel domain-contract authority unless an accepted ADR or migration note says so.

<p>
  <img alt="Status: compatibility guard" src="https://img.shields.io/badge/status-compatibility__guard-yellow">
  <img alt="Root: contracts/v1/domains" src="https://img.shields.io/badge/root-contracts%2Fv1%2Fdomains-blue">
  <img alt="Authority: no parallel authority" src="https://img.shields.io/badge/authority-no__parallel__authority-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite__or__abstain-green">
  <img alt="Path: needs review" src="https://img.shields.io/badge/path-NEEDS__REVIEW-orange">
</p>

**Status:** draft / compatibility guard  
**Path:** `contracts/v1/domains/README.md`  
**Active semantic-contract lane:** `contracts/domains/`  
**Schema lane:** `schemas/contracts/v1/`  
**Truth posture:** CONFIRMED this file was blank · CONFIRMED `contracts/domains/README.md` defines the active domain semantic-contract root · CONFIRMED `contracts/v1/domains/atmosphere/README.md` exists as a compatibility guard · PROPOSED this versioned root should remain a guard/pointer unless an ADR resolves otherwise

**Quick jumps:** [Purpose](#purpose) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Guardrails](#guardrails) · [Known child guards](#known-child-guards) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

This README prevents `contracts/v1/domains/` from silently becoming a second domain semantic-contract root.

Use this path only as a compatibility or migration pointer until maintainers decide whether versioned contract paths under `contracts/v1/` are accepted for this repo.

The active contract lane remains:

```text
contracts/domains/
```

The active schema lane remains separate:

```text
schemas/contracts/v1/
```

## Repo fit

| Responsibility | Current path | Status |
|---|---|---|
| Domain semantic contracts | `contracts/domains/` | CONFIRMED active lane in current repo evidence |
| Versioned compatibility pointer | `contracts/v1/domains/` | This guard; not canonical authority |
| Root contract guidance | `contracts/README.md` | Semantic meaning root; schemas/policy/data/release separate |
| Machine-checkable schemas | `schemas/contracts/v1/` | Schema lane, separate from contract Markdown |
| Domain policy | `policy/domains/` | Separate policy root |
| Fixtures/tests | `fixtures/domains/`, `tests/domains/` | Separate validation roots |
| Release/correction/rollback | `release/` | Separate publication root |

## Accepted contents

Only compatibility material belongs here:

| Accepted item | Purpose |
|---|---|
| `README.md` | Explains why this path must not become a second authority. |
| Domain child README guards | Point to active `contracts/domains/<domain>/` lanes. |
| `MIGRATION.md` | Optional steward-approved migration plan if `contracts/v1/domains/` becomes canonical. |
| `BACKLINKS.md` | Optional stale-reference audit for versioned paths. |
| `ADR_POINTER.md` | Optional pointer to accepted path-resolution ADR. |

## Exclusions

| Do not put here | Correct home |
|---|---|
| Domain object semantic contracts | `contracts/domains/<domain>/` unless ADR changes it. |
| JSON Schema / machine shape | `schemas/contracts/v1/...`. |
| Policy rules | `policy/domains/<domain>/` or accepted policy roots. |
| Fixtures and validation examples | `fixtures/domains/<domain>/`. |
| Tests and validator proof | `tests/domains/<domain>/` and validator tool roots. |
| Source descriptors and registries | Source registry/data roots. |
| EvidenceBundle/proof records | `data/proofs/` or accepted proof roots. |
| Release/correction/rollback decisions | `release/` and release contracts. |
| Data lifecycle content | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/published`. |
| Public API/UI/map/tile behavior | Governed app/API/UI/layer roots after verification. |

## Guardrails

- Do not copy full domain object contracts into this versioned path.
- Do not treat this folder as canonical merely because it contains `v1`.
- Do not make `contracts/v1/` a schema-style mirror of `schemas/contracts/v1/` without ADR review.
- Do not create parallel homes for schemas, contracts, policy, source registries, release records, proof records, or receipts without an ADR or migration note.
- Public clients must continue to rely on governed APIs, released artifacts, EvidenceBundle resolution, policy decisions, and release state — not on contract Markdown.

## Known child guards

| Child path | Status | Purpose |
|---|---|---|
| `contracts/v1/domains/atmosphere/README.md` | CONFIRMED compatibility guard | Points maintainers to `contracts/domains/atmosphere/` and records atmosphere/air path drift. |

## Validation checklist

- [ ] Confirm whether `contracts/v1/` is an accepted compatibility root or drift.
- [ ] Confirm whether a path-resolution ADR exists for versioned contract homes.
- [ ] Confirm domain semantic contracts remain indexed from `contracts/domains/`.
- [ ] Confirm schemas stay under `schemas/contracts/v1/`.
- [ ] Confirm no object contract is maintained in both this path and the active lane.
- [ ] Confirm rollback target before any migration.

## Rollback

Rollback is required if this path becomes a parallel domain contract authority, schema authority, policy authority, source registry, proof store, release root, public API surface, or UI implementation root without ADR-backed migration.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
