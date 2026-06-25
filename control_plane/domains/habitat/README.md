<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/control-plane-domains-habitat-readme
title: control_plane/domains/habitat/README.md — Habitat Control-Plane Domain Lane README
version: v0.1
type: readme; control-plane-domain-index; governance-lane-guide
status: draft; PROPOSED; control-plane; habitat; governance-index; implementation-bounded
owners: OWNER_TBD — Control-plane steward · Habitat steward · Policy steward · Evidence steward · Release steward · Docs steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-06-24
policy_label: public; control-plane; domains; habitat; governance-index; no-parallel-authority
tags: [kfm, control-plane, habitat, domain-lane, governance-index, policy-gates, release-state, EvidenceBundle, sensitivity, geoprivacy]
related:
  - ../../README.md
  - ../../../docs/domains/habitat/CANONICAL_PATHS.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/CONTRACTS.md
  - ../../../docs/domains/habitat/REASON_CODES.md
  - ../../../contracts/domains/habitat/
  - ../../../schemas/contracts/v1/domains/habitat/
  - ../../../policy/domains/habitat/
  - ../../../fixtures/domains/habitat/
  - ../../../tests/domains/habitat/
  - ../../../release/
notes:
  - "This file replaces a blank placeholder at `control_plane/domains/habitat/README.md`."
  - "The control-plane root is for machine-readable governance maps, registers, crosswalks, and machine indices; it is not source data, schemas, code, policy rules, or executable validators."
  - "Habitat canonical paths identify habitat as a domain segment inside responsibility roots, not a root folder."
  - "Habitat sensitive joins fail closed by default when occurrence, exact geometry, rare-species, or culturally sensitive context is involved."
  - "Rollback target for this replacement is previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Control-Plane Domain Lane

> Governance-index lane for Habitat-domain control-plane artifacts. This folder may hold machine-readable maps, registers, and crosswalks that describe what governs Habitat lanes. It must not become a schema home, policy-code home, source-data home, release home, proof store, or runtime implementation root.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: control_plane" src="https://img.shields.io/badge/root-control__plane-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-green">
  <img alt="Boundary: governance index" src="https://img.shields.io/badge/boundary-governance__index-purple">
  <img alt="Sensitivity: fail closed" src="https://img.shields.io/badge/sensitive__joins-fail__closed-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `control_plane/domains/habitat/README.md`  
**Owning root:** `control_plane/`  
**Domain segment:** `habitat`  
**Truth posture:** CONFIRMED target was blank · CONFIRMED `control_plane/README.md` defines this root as governance maps and machine indices, not schemas/code/policy/source data · CONFIRMED Habitat canonical paths treat habitat as a domain lane inside responsibility roots and mark sensitive joins as fail-closed · NEEDS VERIFICATION for actual control-plane YAML/register files, validators, CI checks, and runtime governance behavior.

## Quick jumps

[Purpose](#purpose) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Habitat guardrails](#habitat-guardrails) · [Suggested registers](#suggested-registers) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`control_plane/domains/habitat/` is the governance-index lane for Habitat-domain control-plane artifacts.

It may describe:

- which Habitat object families, source families, policy gates, release gates, and reason codes are active or proposed;
- which domain lanes govern Habitat contracts, schemas, policy, fixtures, tests, data, and release artifacts;
- which sensitivity, geoprivacy, and cross-domain join rules must fail closed;
- which drift, deprecation, conflict, or rollout states need machine-readable indexing.

It does not define Habitat object meaning, machine shape, policy rules, data lifecycle content, public API behavior, or release approval.

## Repo fit

| Responsibility | Correct home | Rule |
|---|---|---|
| Governance maps / machine indices | `control_plane/domains/habitat/` | This lane. |
| Human doctrine and canonical placement docs | `docs/domains/habitat/` | Human-readable domain doctrine. |
| Semantic contracts | `contracts/domains/habitat/` | Object meaning and contract boundaries. |
| Machine shape | `schemas/contracts/v1/domains/habitat/` or accepted schema home | JSON Schema and field shape. |
| Policy rules | `policy/domains/habitat/` | Allow/deny/restrict/abstain rules. |
| Fixtures/tests | `fixtures/domains/habitat/`, `tests/domains/habitat/` | Validation examples and proof. |
| Source registry | source catalog / `data/registry/sources/habitat/` | SourceDescriptor and source authority metadata. |
| Data lifecycle | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/published` | Lifecycle products. |
| Release/correction/rollback | `release/` | Publication state and rollback. |
| Runtime/API/UI implementation | app/API/UI/package/pipeline roots | Executable behavior. |

## Accepted contents

Only governance-index material belongs here:

| File type | Purpose |
|---|---|
| `README.md` | Explains control-plane Habitat lane boundaries. |
| `domain_lane.yaml` | Machine-readable lane metadata and owner/steward pointers. |
| `object_family_map.yaml` | Object-family index pointing to contracts/schemas/policy. |
| `policy_gate_map.yaml` | Mapping from object families or source roles to policy gates. |
| `release_gate_map.yaml` | Mapping from object families to release/correction/rollback gates. |
| `reason_code_map.yaml` | Machine-readable reason-code registry or index. |
| `sensitivity_matrix_ref.yaml` | Pointers to sensitivity/geoprivacy rules, not the rules themselves. |
| `drift_register.yaml` | Machine-readable drift/conflict/deprecation entries for Habitat governance. |

## Exclusions

| Do not put here | Correct home |
|---|---|
| Habitat object contracts | `contracts/domains/habitat/` |
| JSON Schema | `schemas/contracts/v1/domains/habitat/` or accepted schema home |
| Policy code | `policy/domains/habitat/` |
| Fixtures | `fixtures/domains/habitat/` |
| Tests or validators | `tests/domains/habitat/`, `tools/validators/` |
| Raw/work/quarantine/processed/catalog/published data | `data/...` lifecycle roots |
| SourceDescriptor instances | source registry / data registry roots |
| EvidenceBundle/proof records | proof/data roots |
| Release decisions | `release/` |
| UI/API/pipeline code | implementation roots |

## Habitat guardrails

- Habitat is a domain segment, not a root folder.
- Habitat control-plane files are indexes, not source truth.
- Sensitive Habitat × Fauna and Habitat × Flora joins must fail closed by default when exact occurrence geometry, rare-species sites, nests, dens, roosts, hibernacula, spawning sites, or culturally sensitive context are involved.
- Source role and knowledge-character distinctions must remain visible. Habitat suitability, habitat patch, ecoregion, species occurrence, conservation status, and advisory context must not collapse into one truth class.
- Public clients must consume governed API/release projections, not control-plane registers directly.

## Suggested registers

PROPOSED until files are verified:

| Register | Status | Purpose |
|---|---|---|
| `domain_lane.yaml` | PROPOSED | Names Habitat lane owners, status, and related roots. |
| `object_family_map.yaml` | PROPOSED | Maps Habitat object families to contract/schema/policy homes. |
| `policy_gate_map.yaml` | PROPOSED | Maps Habitat object families to policy gates. |
| `release_gate_map.yaml` | PROPOSED | Maps Habitat products to release/correction/rollback gates. |
| `reason_code_map.yaml` | PROPOSED | Indexes Habitat reason codes for denial, abstention, caveat, and error states. |
| `sensitivity_matrix_ref.yaml` | PROPOSED | Points to Habitat sensitivity/geoprivacy rules without duplicating policy. |
| `drift_register.yaml` | PROPOSED | Records unresolved path, slug, schema, or policy drift. |

## Validation checklist

- [ ] Confirm which control-plane Habitat registers exist.
- [ ] Confirm each register has a schema or validation rule.
- [ ] Confirm control-plane registers point to, but do not duplicate, contracts/schemas/policy/release roots.
- [ ] Confirm sensitive-join defaults are represented as pointers to policy, not reimplemented here.
- [ ] Confirm generated/public clients do not read control-plane registers as public truth.
- [ ] Confirm rollback targets before any migration or renaming.

## Rollback

Rollback is required if this folder becomes a parallel Habitat contract root, schema root, policy-code root, source registry, proof store, release root, lifecycle-data root, public API surface, UI implementation root, or a way to bypass sensitive Habitat join gates.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
