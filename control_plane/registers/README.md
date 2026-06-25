<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/control-plane-registers-readme
title: control_plane/registers/README.md — Control-Plane Registers README
version: v0.1
type: readme; control-plane-register-index; governance-lane-guide
status: draft; PROPOSED; control-plane; registers; governance-index; implementation-bounded
owners: OWNER_TBD — Control-plane steward · Register steward · Docs steward · Policy steward · Evidence steward · Release steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-06-24
policy_label: public; control-plane; registers; governance-index; no-parallel-authority
tags: [kfm, control-plane, registers, governance-index, machine-registers, docs-registers, drift, verification, authority]
related:
  - ../README.md
  - ../../docs/registers/DOCUMENT_REGISTRY.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../docs/registers/VERIFICATION_BACKLOG.md
  - ../../docs/registers/OBJECT_FAMILY_MAP.md
  - ../../docs/registers/AUTHORITY_LADDER.md
  - ../../docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md
  - ../../schemas/
  - ../../policy/
  - ../../tests/
  - ../../tools/validators/
notes:
  - "This file replaces a blank placeholder at `control_plane/registers/README.md`."
  - "The control-plane root is for machine-readable governance maps, registers, crosswalks, and machine indices; it is not source data, schemas, code, policy rules, or executable validators."
  - "`docs/registers/` carries human-readable counterparts; control-plane register files are the machine-readable side."
  - "Register entries index and crosswalk authority; they do not create object truth, policy decisions, release approval, or proof closure."
  - "Rollback target for this replacement is previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Control-Plane Registers

> Machine-readable governance-register lane for KFM. Files under `control_plane/registers/` may index authority, drift, verification, object families, documents, sources, policies, releases, and crosswalks. They must not become source data, schemas, policy code, executable validators, proof stores, release decisions, or object contracts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: control_plane/registers" src="https://img.shields.io/badge/root-control__plane%2Fregisters-blue">
  <img alt="Boundary: governance index" src="https://img.shields.io/badge/boundary-governance__index-purple">
  <img alt="Authority: no parallel authority" src="https://img.shields.io/badge/authority-no__parallel__authority-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite__or__abstain-green">
</p>

**Status:** draft / PROPOSED  
**Path:** `control_plane/registers/README.md`  
**Owning root:** `control_plane/`  
**Human-readable counterpart root:** `docs/registers/`  
**Truth posture:** CONFIRMED target was blank · CONFIRMED `control_plane/README.md` defines this root as governance maps and machine indices, not schemas/code/policy/source data · CONFIRMED `docs/registers/DOCUMENT_REGISTRY.md` describes a human-facing register pattern paired with machine-readable control-plane YAML · NEEDS VERIFICATION for actual register files, schemas, validator coverage, CI checks, and runtime consumers.

## Quick jumps

[Purpose](#purpose) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Register guardrails](#register-guardrails) · [Suggested register pattern](#suggested-register-pattern) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`control_plane/registers/` is for machine-readable KFM governance registers.

It may describe:

- which documents, contracts, schemas, policies, sources, releases, object families, and domain lanes exist;
- how authority, lifecycle state, drift state, verification state, and deprecation state are indexed;
- which human-readable `docs/registers/` files mirror or explain each machine register;
- which automated checks may consume register data after validation.

It does not define object meaning, field shape, policy rules, release decisions, evidence proof, source truth, lifecycle data, or implementation behavior.

## Repo fit

| Responsibility | Correct home | Rule |
|---|---|---|
| Machine-readable registers | `control_plane/registers/` | This lane. |
| Root control-plane guidance | `control_plane/README.md` | Defines control-plane root boundary. |
| Human-readable register docs | `docs/registers/` | Human counterpart and reviewer-facing explanation. |
| Semantic contracts | `contracts/` | Object meaning and boundaries. |
| Machine shape | `schemas/` | JSON Schema and field shape. |
| Policy rules | `policy/` | Admissibility and sensitivity decisions. |
| Tests and validators | `tests/`, `tools/validators/` | Enforcement and integrity checks. |
| Source/evidence/data/release | source, proof, data, and release roots | Canonical records and lifecycle outputs. |

## Accepted contents

Only machine-readable register/index material belongs here:

| File type | Purpose |
|---|---|
| `README.md` | Explains register lane boundaries. |
| `document_registry.yaml` | Machine-readable document inventory/classification, if placed under this subroot. |
| `object_family_map.yaml` | Machine-readable object-family to contract/schema/policy map. |
| `domain_lane_register.yaml` | Domain lane index, if not placed at control-plane root. |
| `source_authority_register.yaml` | Source-authority crosswalk pointers, not source records themselves. |
| `drift_register.yaml` | Machine-readable drift/conflict/deprecation entries. |
| `verification_backlog.yaml` | Machine-readable verification backlog. |
| `release_gate_register.yaml` | Release gate crosswalk pointers, not release decisions. |

## Exclusions

| Do not put here | Correct home |
|---|---|
| Human narrative register docs | `docs/registers/` |
| Object contracts | `contracts/` |
| JSON Schema | `schemas/` |
| Policy code | `policy/` |
| SourceDescriptor instances | source catalog / source registry / data registry roots |
| EvidenceBundle/proof records | proof/data roots |
| Release decisions | `release/` |
| Raw/work/quarantine/processed/catalog/published data | `data/...` lifecycle roots |
| Runtime/API/UI/pipeline code | implementation roots |
| Executable validators | `tools/validators/` |

## Register guardrails

- Register files index authority; they do not create authority by themselves.
- Machine registers must link to canonical homes instead of copying contracts, schemas, policy, source descriptors, proofs, or release decisions.
- Register claims about implementation maturity must be backed by schema/test/validator/release/runtime evidence.
- When a machine register and a human register disagree, record drift and resolve through steward review.
- Public clients must not treat control-plane registers as public truth; they use governed APIs and released projections.

## Suggested register pattern

PROPOSED until files are verified:

```text
control_plane/registers/README.md
control_plane/registers/document_registry.yaml
control_plane/registers/object_family_map.yaml
control_plane/registers/domain_lane_register.yaml
control_plane/registers/source_authority_register.yaml
control_plane/registers/drift_register.yaml
control_plane/registers/verification_backlog.yaml
control_plane/registers/release_gate_register.yaml
```

Where existing root-level files already exist, this README should become a pointer/index rather than forcing a move.

## Validation checklist

- [ ] Confirm which machine-readable register files exist.
- [ ] Confirm whether registers live at `control_plane/` root or under `control_plane/registers/`.
- [ ] Confirm each register has a schema or validation rule.
- [ ] Confirm each machine register has a human-readable counterpart or explanatory doc where appropriate.
- [ ] Confirm registers link to canonical artifacts and do not duplicate their authority.
- [ ] Confirm CI checks reject stale, contradictory, or unsupported register entries.

## Rollback

Rollback is required if this folder becomes a parallel contract root, schema root, policy-code root, source registry, proof store, release root, lifecycle-data root, executable-validator root, public API surface, or a way to claim implementation maturity without evidence.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
