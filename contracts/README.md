<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-readme
title: contracts/README.md — Contract Root README
version: v0.2
type: root-readme; governance-index; semantic-contract-root
status: draft; repo-facing; canonical-root; implementation-bounded; steward-review-needed
owners: OWNER_TBD — Contracts steward · Schema steward · Policy steward · Evidence steward · Runtime steward · Release steward · Domain stewards · UI steward · Docs steward
created: NEEDS VERIFICATION — short root stub existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; semantic-contracts; governance; evidence-first; no-parallel-authority
tags: [kfm, contracts, semantic-contracts, schemas, policy, fixtures, validators, evidence, release, runtime, ui, domains, source, object-map]
related:
  - ./OBJECT_MAP.md
  - ./domains/README.md
  - ./ui/README.md
  - ./source/README.md
  - ./runtime/README.md
  - ./policy/README.md
  - ./release/README.md
  - ./evidence/README.md
  - ./v1/README.md
  - ../schemas/contracts/v1/
  - ../policy/
  - ../fixtures/
  - ../tests/
  - ../tools/validators/
  - ../data/
  - ../release/
notes:
  - "Expanded from the short root stub that said contracts define semantic meaning and pair with schemas."
  - "Contracts are human-readable semantic meaning. Schemas define machine shape. Policy defines admissibility. Fixtures/tests/validators prove enforcement. Data/proof/release roots govern instances and publication."
  - "This README does not prove implementation, validator coverage, policy behavior, release state, or public client behavior."
  - "Versioned `contracts/v1/` paths are compatibility guards unless an ADR or migration note accepts them."
  - "Rollback target for this expansion is previous stub blob SHA `a2c5150814c1cac5a360fb03b8ddbfb4d98bb2d7`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts

> Canonical root for KFM semantic contracts. Contract Markdown defines what object families mean in the KFM trust model. It does not define JSON shape, execute validation, run policy, store source data, prove evidence, approve release, or implement UI/API behavior.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Authority: semantic meaning" src="https://img.shields.io/badge/authority-semantic__meaning-purple">
  <img alt="Truth: evidence first" src="https://img.shields.io/badge/truth-evidence__first-green">
  <img alt="Boundary: not schemas" src="https://img.shields.io/badge/boundary-not__schemas-critical">
</p>

**Status:** draft / canonical semantic-contract root  
**Path:** `contracts/README.md`  
**Object map:** `contracts/OBJECT_MAP.md`  
**Schema root:** `schemas/contracts/v1/`  
**Truth posture:** CONFIRMED previous root README stated contracts define semantic meaning and schemas define shape · CONFIRMED `OBJECT_MAP.md` exists as an evidence-limited crosswalk, not a complete inventory · CONFIRMED domain and UI lanes define semantic-contract boundaries · NEEDS VERIFICATION for full contract inventory, schema coverage, fixtures, validators, policy bundles, emitted-instance homes, CI behavior, release state, and public API/UI behavior.

## Quick jumps

[Purpose](#purpose) · [Authority boundary](#authority-boundary) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Current lanes](#current-lanes) · [Authoring rules](#authoring-rules) · [Maturity labels](#maturity-labels) · [Versioned paths](#versioned-paths) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`contracts/` is the KFM semantic-contract root.

A contract answers:

- what an object, payload, envelope, receipt, decision, source descriptor, UI projection, runtime response, release object, or domain object means;
- which claims it may and may not support;
- which evidence, policy, review, release, sensitivity, rights, correction, and rollback state must remain visible;
- which companion schema, fixture, validator, policy, proof, data, and release roots are involved;
- which consumers may safely interpret it after validation and release gates.

A contract does not make a claim true. EvidenceBundle and admissible source support outrank generated or rendered language.

---

## Authority boundary

| Responsibility | Correct root | Rule |
|---|---|---|
| Semantic meaning | `contracts/` | This root. Human-readable object meaning and boundaries. |
| Machine shape | `schemas/contracts/v1/` | JSON Schema and field-shape validation. |
| Policy/admissibility | `policy/` | Allow, deny, restrict, abstain, sensitivity, rights, and release gates. |
| Fixtures | `fixtures/` | Valid, invalid, golden, and negative examples. |
| Tests/validators | `tests/`, `tools/validators/` | Enforcement proof and validation tooling. |
| Source authority | source catalog / source registry / data registry roots | SourceDescriptor and source admission metadata. |
| Evidence/proof | `data/proofs/` or accepted proof roots | EvidenceBundle, receipts, and proof records. |
| Runtime/API responses | governed runtime/API roots | Runtime envelope instances and API behavior. |
| UI rendering | UI/web/app roots | Components, state, styles, accessibility implementation. |
| Release/correction/rollback | `release/` and release contracts | Publication state, withdrawal, correction, rollback. |
| Data lifecycle | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/published` | RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED. |

---

## What belongs here

Place Markdown under `contracts/` when it defines semantic meaning for a KFM object family or contract lane.

| Contract family | Example home | Purpose |
|---|---|---|
| Domain object meaning | `contracts/domains/<domain>/` | Domain-specific object semantics. |
| UI projection meaning | `contracts/ui/` | Trust-surface payloads, projections, badges, events, and UI envelopes. |
| Runtime envelopes | `contracts/runtime/` | Runtime response, decision, and receipt semantics. |
| Evidence contracts | `contracts/evidence/` | Evidence, citation, and proof-facing object semantics. |
| Source contracts | `contracts/source/` | SourceDescriptor, ingest receipts, and source-admission semantics. |
| Policy contracts | `contracts/policy/` | Policy input/output semantics, not executable policy. |
| Release contracts | `contracts/release/` | ReleaseManifest, rollback, promotion, withdrawal semantics. |
| Shared contracts | `contracts/shared/`, `contracts/<family>/` | Objects not owned by a single domain lane. |
| Compatibility guards | selected paths such as `contracts/v1/` | Guard against drift and prevent parallel authority. |

---

## What does not belong here

| Do not put this in `contracts/` | Correct home |
|---|---|
| JSON Schema / machine-checkable shape | `schemas/contracts/v1/...` |
| Policy bundles | `policy/...` |
| Fixtures and examples | `fixtures/...` |
| Tests and validator code | `tests/...`, `tools/validators/...` |
| SourceDescriptor instances / source registry records | source catalog / source registry / `data/registry/sources/...` |
| Raw/work/quarantine/processed/catalog/published data | `data/...` lifecycle roots |
| EvidenceBundle or proof records | `data/proofs/` or accepted proof roots |
| Runtime response instances | governed runtime/API output roots |
| Public UI/app code | UI/web/app/package roots |
| Release artifacts and decisions | `release/...` |

---

## Current lanes

This list is a maintained orientation, not a complete generated inventory.

| Lane | Path | Posture |
|---|---|---|
| Object map | `contracts/OBJECT_MAP.md` | Evidence-limited crosswalk; not complete inventory. |
| Domain contracts | `contracts/domains/` | Active domain semantic-contract lane. |
| UI contracts | `contracts/ui/` | Active UI semantic-contract lane. |
| Source contracts | `contracts/source/` | Active source semantic-contract lane. |
| Runtime contracts | `contracts/runtime/` | Runtime semantic-contract lane. |
| Evidence contracts | `contracts/evidence/` | Evidence/citation/proof-facing semantic-contract lane. |
| Policy contracts | `contracts/policy/` | Policy object semantics; executable policy remains in `policy/`. |
| Release contracts | `contracts/release/` | Release object semantics; release state remains in `release/`. |
| Shared contracts | `contracts/shared/` | Cross-family shared semantic contracts. |
| Versioned compatibility | `contracts/v1/` | Compatibility guard; not canonical authority unless ADR accepts it. |

---

## Authoring rules

Every non-trivial contract should include:

- KFM Meta Block v2;
- clear status and truth labels;
- a one-paragraph semantic definition;
- explicit exclusions;
- schema posture: schema-confirmed, schema-stub-confirmed, schema-missing, or schema-conflicted;
- evidence/source/ref requirements where claims depend on support;
- sensitivity, rights, policy, release, and public-use limitations;
- validation expectations and negative-state tests;
- rollback path or prior blob/migration target;
- related docs, schemas, policy roots, fixtures, tests, data lifecycle roots, and release roots.

Do not write “the system does X” unless current repo evidence, schema, test, release, runtime output, or logs support it. If proof is missing, use `PROPOSED`, `NEEDS VERIFICATION`, or `UNKNOWN`.

---

## Maturity labels

| Label | Meaning |
|---|---|
| `scaffold` | Placeholder only. Not safe as authority. |
| `draft` | Semantic contract exists. Not enough for public release by itself. |
| `schema-missing` | No paired schema confirmed. |
| `schema-stub-confirmed` | Paired schema exists but is permissive/incomplete. |
| `schema-aligned` | Contract fields and schema shape agree. Still requires tests/policy/release. |
| `validated` | Fixtures/tests/validators prove positive and negative states. |
| `released` | Policy/review/release/rollback artifacts exist. |
| `compatibility-guard` | Path exists to prevent drift, not to become a second authority. |
| `path-needs-review` | Placement is unresolved and needs ADR/steward decision. |

---

## Versioned paths

`contracts/v1/` is currently treated as a compatibility guard.

Do not mirror `schemas/contracts/v1/` into `contracts/v1/` without an accepted ADR or migration note. Schema versioning belongs under `schemas/`; contract versioning must not create a parallel semantic authority unless governance explicitly accepts that path.

Known guards:

| Guard | Points to | Status |
|---|---|---|
| `contracts/v1/README.md` | `contracts/` and `schemas/contracts/v1/` | Compatibility guard. |
| `contracts/v1/domains/README.md` | `contracts/domains/` | Compatibility guard. |
| `contracts/v1/domains/atmosphere/README.md` | `contracts/domains/atmosphere/` | Compatibility guard. |

---

## Validation checklist

- [ ] Generate a full `contracts/**/*.md` inventory.
- [ ] Confirm every contract has a schema posture label.
- [ ] Confirm companion schema, fixture, validator, policy, and test roots are marked correctly.
- [ ] Confirm compatibility guards do not contain canonical object contracts.
- [ ] Confirm no duplicated object authority across `air`/`atmosphere`, `transport`/`roads-rail-trade`, or other known drift lanes.
- [ ] Confirm public-facing objects preserve EvidenceBundle, policy, release, correction, and rollback boundaries.
- [ ] Confirm release gates before any contract is described as public-consumable.

## Rollback

Rollback is required if this README becomes a schema registry, policy registry, source registry, proof store, release registry, generated inventory, UI/API implementation contract, or a claim that unverified objects are implemented.

Rollback target for this expansion: previous stub blob SHA `a2c5150814c1cac5a360fb03b8ddbfb4d98bb2d7`.

<p align="right"><a href="#top">Back to top</a></p>
