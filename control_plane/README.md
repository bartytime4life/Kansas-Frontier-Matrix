<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/control-plane-readme
title: control_plane/README.md — Control-Plane Root README
version: v0.2
type: root-readme; governance-index-root; machine-register-root
status: draft; PROPOSED; canonical-root; control-plane; implementation-bounded; steward-review-needed
owners: OWNER_TBD — Control-plane steward · Register steward · Domain stewards · Policy steward · Evidence steward · Release steward · Docs steward
created: NEEDS VERIFICATION — short root stub existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; control-plane; governance-index; machine-registers; no-parallel-authority
tags: [kfm, control-plane, governance-index, machine-registers, crosswalks, domains, registers, drift, policy-gates, release-state]
related:
  - ./domains/README.md
  - ./domains/habitat/README.md
  - ./registers/README.md
  - ./registers/DRIFT_REGISTER.md
  - ../docs/registers/DOCUMENT_REGISTRY.md
  - ../docs/registers/DRIFT_REGISTER.md
  - ../contracts/README.md
  - ../schemas/
  - ../policy/
  - ../tests/
  - ../tools/validators/
  - ../data/
  - ../release/
notes:
  - "Expanded from the short control-plane root stub."
  - "The control-plane root is for machine-readable governance maps, registers, crosswalks, and machine indices."
  - "It is not source data, processed data, schemas, code, policy rules, executable validators, proof storage, or release approval."
  - "Subroots such as `control_plane/domains/` and `control_plane/registers/` are governance-index lanes only."
  - "Rollback target for this expansion is previous stub blob SHA `4e4cfa42b63d5c40bc233f9635d685a7d88df4f3`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# control_plane

> Canonical root for machine-readable governance maps, registers, crosswalks, and indices. The control plane answers “what governs what?” for KFM automation and steward review. It is not a source-data root, schema root, policy-code root, proof store, release root, validator root, public API surface, or implementation package.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: control_plane" src="https://img.shields.io/badge/root-control__plane-blue">
  <img alt="Boundary: governance index" src="https://img.shields.io/badge/boundary-governance__index-purple">
  <img alt="Authority: no parallel authority" src="https://img.shields.io/badge/authority-no__parallel__authority-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite__or__abstain-green">
</p>

**Status:** draft / PROPOSED  
**Path:** `control_plane/README.md`  
**Truth posture:** CONFIRMED previous root README defined control plane as machine-readable governance maps and indices · CONFIRMED `control_plane/domains/README.md` and `control_plane/registers/README.md` now define child governance-index lanes · NEEDS VERIFICATION for full register inventory, schemas, validators, CI wiring, and automated consumers.

## Quick jumps

[Purpose](#purpose) · [Authority boundary](#authority-boundary) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Current lanes](#current-lanes) · [Register rules](#register-rules) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`control_plane/` contains machine-readable governance artifacts that are too operational for prose-only documentation.

It may describe:

- which documents, contracts, schemas, policies, sources, object families, domain lanes, releases, and registers exist;
- which artifacts govern other artifacts;
- which policy gates, release gates, contradiction states, deprecations, drift entries, or verification states are active;
- which machine-readable indexes automation may inspect after validation.

It does not create truth, approve release, execute policy, validate schemas, store evidence, or replace steward review.

## Authority boundary

| Responsibility | Correct home | Rule |
|---|---|---|
| Machine governance maps and indices | `control_plane/` | This root. |
| Human-readable register docs | `docs/registers/` | Reviewer-facing explanations and narrative register views. |
| Semantic contracts | `contracts/` | Object meaning and contract boundaries. |
| Machine shape | `schemas/` | JSON Schema and field shape. |
| Policy rules | `policy/` | Admissibility and sensitivity decisions. |
| Tests and validators | `tests/`, `tools/validators/` | Enforcement and integrity checks. |
| Source/evidence/proof records | source, proof, and data roots | Canonical records and lifecycle outputs. |
| Release/correction/rollback | `release/` | Publication state and rollback. |
| Runtime/API/UI/package code | implementation roots | Executable behavior. |

## What belongs here

| Artifact type | Purpose |
|---|---|
| YAML governance registers | Machine-readable inventory or authority indexes. |
| Crosswalk tables | Maps between docs, contracts, schemas, policy, sources, release, and tests. |
| Domain-lane governance maps | Domain-specific control-plane maps under `control_plane/domains/`. |
| Register-lane profiles | Machine-register guides and register companions under `control_plane/registers/`. |
| Drift, deprecation, contradiction, and verification indexes | Machine-readable governance state for review and automation. |
| Release-gate or policy-gate maps | Pointers to policy/release gates, not the gates themselves. |

## What does not belong here

| Do not put here | Correct home |
|---|---|
| Human-only docs | `docs/` |
| Semantic contracts | `contracts/` |
| JSON Schema | `schemas/` |
| Policy code | `policy/` |
| Tests or executable validators | `tests/`, `tools/validators/` |
| SourceDescriptor instances | source catalog / source registry / data registry roots |
| EvidenceBundle/proof records | proof/data roots |
| Release decisions | `release/` |
| Raw/work/quarantine/processed/catalog/published data | `data/...` lifecycle roots |
| Runtime/API/UI/pipeline code | implementation roots |

## Current lanes

| Lane | Path | Posture |
|---|---|---|
| Domain governance lanes | `control_plane/domains/` | Governance-index root for domain child lanes. |
| Habitat governance lane | `control_plane/domains/habitat/` | Confirmed child README; register files still PROPOSED. |
| Register governance lane | `control_plane/registers/` | Machine-readable register lane guide. |
| Drift register profile | `control_plane/registers/DRIFT_REGISTER.md` | Markdown profile for a machine-readable drift register; final YAML/schema still NEEDS VERIFICATION. |
| Human register counterparts | `docs/registers/` | Human-facing register docs; not machine-register root. |

## Register rules

- Registers index authority; they do not create authority by themselves.
- Registers must point to canonical homes instead of copying contracts, schemas, policy, source records, proofs, or release decisions.
- Register entries that claim implementation maturity must be backed by schema, test, validator, release, runtime, or artifact evidence.
- When a machine register and a human register disagree, record drift and resolve through steward review.
- Public clients must use governed APIs and released projections, not raw control-plane registers.

## Validation checklist

- [ ] Inventory all files under `control_plane/`.
- [ ] Confirm which files are canonical machine registers versus compatibility pointers.
- [ ] Confirm schema or validation rule for each machine register.
- [ ] Confirm each register has an owner and review burden.
- [ ] Confirm human-readable counterparts exist where needed.
- [ ] Confirm CI rejects stale, contradictory, or unsupported entries.
- [ ] Confirm no control-plane file duplicates schema, policy, source, proof, release, data, or implementation authority.

## Rollback

Rollback is required if this root becomes a parallel contract root, schema root, policy-code root, source registry, proof store, release root, lifecycle-data root, executable-validator root, public API surface, UI implementation root, or a way to claim implementation maturity without evidence.

Rollback target for this expansion: previous stub blob SHA `4e4cfa42b63d5c40bc233f9635d685a7d88df4f3`.

<p align="right"><a href="#top">Back to top</a></p>
