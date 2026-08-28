<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-v1-domains-atmosphere-readme
title: contracts/v1/domains/atmosphere/README.md — Atmosphere v1 Contract Compatibility README
type: readme
version: v0.1
status: draft; compatibility-guard; PROPOSED; path-needs-review; no-parallel-authority
owners: OWNER_TBD — Atmosphere steward · Contract steward · Schema steward · Policy steward · Release steward · Docs steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-06-24
policy_label: public; contracts; v1; domains; atmosphere; compatibility; semantic-contracts; no-parallel-authority
tags: [kfm, contracts, v1, domains, atmosphere, air, compatibility, semantic-contracts, Directory Rules, EvidenceBundle, PolicyDecision, ReleaseManifest]
related:
  - ../../../domains/atmosphere/README.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../../contracts/atmosphere/README.md
  - ../../../../contracts/air/README.md
  - ../../../../schemas/contracts/v1/domains/atmosphere/
  - ../../../../policy/domains/atmosphere/
  - ../../../../fixtures/domains/atmosphere/
  - ../../../../tests/domains/atmosphere/
  - ../../../../release/
notes:
  - "This file replaces a blank placeholder at `contracts/v1/domains/atmosphere/README.md`."
  - "Current repo evidence identifies `contracts/domains/atmosphere/` as the active Atmosphere semantic-contract lane."
  - "Atmosphere docs record ADR-class naming and path drift around `air`, `atmosphere`, and `domains/atmosphere`."
  - "This README is a compatibility guard only; it does not create a new canonical contract root."
  - "Rollback target for this replacement is previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere v1 Contract Compatibility README

> Compatibility guard for `contracts/v1/domains/atmosphere/`. The active Atmosphere semantic-contract lane is `contracts/domains/atmosphere/`; this versioned path must not become a parallel contract authority unless an accepted ADR or migration note says so.

<p>
  <img alt="Status: compatibility guard" src="https://img.shields.io/badge/status-compatibility__guard-yellow">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-1f8fff">
  <img alt="Authority: no parallel authority" src="https://img.shields.io/badge/authority-no__parallel__authority-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite__or__abstain-green">
  <img alt="Path: needs review" src="https://img.shields.io/badge/path-NEEDS__REVIEW-orange">
</p>

**Status:** draft / compatibility guard  
**Path:** `contracts/v1/domains/atmosphere/README.md`  
**Active semantic-contract lane:** `contracts/domains/atmosphere/`  
**Schema lane:** `schemas/contracts/v1/domains/atmosphere/`  
**Truth posture:** CONFIRMED this file was blank · CONFIRMED `contracts/domains/atmosphere/README.md` exists and declares the active Atmosphere contract meaning lane · CONFIRMED path/slug drift exists across `air`, `atmosphere`, and `domains/atmosphere` variants · PROPOSED this versioned path should remain a guard/pointer unless an ADR resolves otherwise

**Quick jumps:** [Purpose](#purpose) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Guardrails](#guardrails) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

This README prevents `contracts/v1/domains/atmosphere/` from silently becoming a second Atmosphere semantic-contract root.

Use this path only as a compatibility or migration pointer until maintainers decide whether versioned contract paths under `contracts/v1/` are accepted for this repo.

The active contract lane remains:

```text
contracts/domains/atmosphere/
```

The machine-shape lane remains separate:

```text
schemas/contracts/v1/domains/atmosphere/
```

## Repo fit

| Responsibility | Current path | Status |
|---|---|---|
| Atmosphere semantic contracts | `contracts/domains/atmosphere/` | CONFIRMED active lane in current repo evidence |
| Versioned compatibility pointer | `contracts/v1/domains/atmosphere/` | This guard; not canonical authority |
| Plain atmosphere compatibility | `contracts/atmosphere/` | CONFIRMED compatibility/path-conflict README |
| Air slug compatibility | `contracts/air/` | CONFIRMED via repo search as sibling compatibility surface |
| Machine-checkable schemas | `schemas/contracts/v1/domains/atmosphere/` | Schema lane, separate from contract Markdown |
| Atmosphere placement doctrine | `docs/domains/atmosphere/CANONICAL_PATHS.md` | CONFIRMED path registry / naming-drift evidence |
| Policy, fixtures, tests, release | `policy/`, `fixtures/`, `tests/`, `release/` roots | Separate responsibility roots |

## Accepted contents

Only compatibility material belongs here:

| Accepted item | Purpose |
|---|---|
| `README.md` | Explains why this path must not become a second authority. |
| `MIGRATION.md` | Optional steward-approved migration plan if `contracts/v1/` becomes canonical. |
| `BACKLINKS.md` | Optional stale-reference audit for versioned paths. |
| `ADR_POINTER.md` | Optional pointer to accepted path-resolution ADR. |

## Exclusions

| Do not put here | Correct home |
|---|---|
| Atmosphere object semantic contracts | `contracts/domains/atmosphere/` unless ADR changes it. |
| JSON Schema / machine shape | `schemas/contracts/v1/domains/atmosphere/`. |
| Policy rules | `policy/domains/atmosphere/` or accepted policy roots. |
| Fixtures and validation examples | `fixtures/domains/atmosphere/`. |
| Tests and validator proof | `tests/domains/atmosphere/` and validator tool roots. |
| EvidenceBundle/proof records | `data/proofs/` or accepted proof roots. |
| Release/correction/rollback decisions | `release/` and release contracts. |
| Raw/work/quarantine/processed/published data | Data lifecycle roots. |
| Public API/UI/map/tile behavior | Governed app/API/UI/layer roots after verification. |

## Guardrails

- Do not copy full Atmosphere object contracts into this versioned path.
- Do not treat this folder as canonical merely because it contains `v1`.
- Do not make `contracts/v1/` a schema-style mirror of `schemas/contracts/v1/` without ADR review.
- Do not resolve the `air` / `atmosphere` / `domains/atmosphere` naming conflict here.
- Public clients must continue to rely on governed APIs, released artifacts, EvidenceBundle resolution, policy decisions, and release state — not on contract Markdown.

## Validation checklist

- [ ] Confirm whether `contracts/v1/` is an accepted compatibility root or drift.
- [ ] Confirm whether a path-resolution ADR exists for `air` vs `atmosphere` vs `domains/atmosphere`.
- [ ] Confirm all Atmosphere semantic contracts are indexed from `contracts/domains/atmosphere/`.
- [ ] Confirm schemas stay under `schemas/contracts/v1/domains/atmosphere/`.
- [ ] Confirm no object contract is maintained in both this path and the active lane.
- [ ] Confirm rollback target before any migration.

## Rollback

Rollback is required if this path becomes a parallel Atmosphere contract authority, schema authority, policy authority, source registry, proof store, release root, public API surface, or UI implementation root without ADR-backed migration.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
