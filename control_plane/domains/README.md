<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/control-plane-domains-readme
title: control_plane/domains/README.md — Control-Plane Domain Lanes README
version: v0.1
type: readme; control-plane-index; domain-governance-lane-guide
status: draft; PROPOSED; control-plane; domains; governance-index; implementation-bounded
owners: OWNER_TBD — Control-plane steward · Domain stewards · Policy steward · Evidence steward · Release steward · Docs steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-06-24
policy_label: public; control-plane; domains; governance-index; no-parallel-authority
tags: [kfm, control-plane, domains, governance-index, domain-lanes, policy-gates, release-state, EvidenceBundle, sensitivity, drift-register]
related:
  - ../README.md
  - ./habitat/README.md
  - ../../docs/registers/DOMAIN_LANE.md
  - ../../docs/domains/README.md
  - ../../contracts/domains/README.md
  - ../../schemas/contracts/v1/domains/
  - ../../policy/domains/
  - ../../fixtures/domains/
  - ../../tests/domains/
  - ../../release/
notes:
  - "This file replaces a blank placeholder at `control_plane/domains/README.md`."
  - "The control-plane root is for machine-readable governance maps, registers, crosswalks, and machine indices; it is not source data, schemas, code, policy rules, or executable validators."
  - "Domain child folders under this root are governance-index lanes, not domain contract roots or data roots."
  - "The Habitat child README is currently the verified child-lane pattern for this root."
  - "Rollback target for this replacement is previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Control-Plane Domain Lanes

> Governance-index root for domain-specific control-plane artifacts. Child folders under `control_plane/domains/` may hold machine-readable maps, registers, and crosswalks describing what governs each domain lane. They must not become schema homes, policy-code homes, source-data homes, proof stores, release homes, public API surfaces, or runtime implementation roots.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: control_plane/domains" src="https://img.shields.io/badge/root-control__plane%2Fdomains-blue">
  <img alt="Boundary: governance index" src="https://img.shields.io/badge/boundary-governance__index-purple">
  <img alt="Authority: no parallel authority" src="https://img.shields.io/badge/authority-no__parallel__authority-critical">
  <img alt="Truth: evidence first" src="https://img.shields.io/badge/truth-evidence__first-green">
</p>

**Status:** draft / PROPOSED  
**Path:** `control_plane/domains/README.md`  
**Owning root:** `control_plane/`  
**Truth posture:** CONFIRMED target was blank · CONFIRMED `control_plane/README.md` defines this root as governance maps and machine indices, not schemas/code/policy/source data · CONFIRMED `control_plane/domains/habitat/README.md` exists as a child governance-index lane · NEEDS VERIFICATION for actual domain control-plane register files, validators, CI checks, and runtime governance behavior.

## Quick jumps

[Purpose](#purpose) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Domain-lane guardrails](#domain-lane-guardrails) · [Known child lanes](#known-child-lanes) · [Suggested register pattern](#suggested-register-pattern) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`control_plane/domains/` indexes domain-specific control-plane governance artifacts.

It may describe:

- which domain lanes exist or are proposed;
- which object families, source families, policy gates, release gates, reason codes, drift states, and sensitivity matrices govern each domain;
- which paths connect a domain lane to contracts, schemas, policy, fixtures, tests, source registries, data lifecycle products, and release artifacts;
- which machine-readable registers need steward review before automation or public surfaces depend on them.

It does not define object meaning, field shape, policy rules, evidence proof, source authority, release approval, data lifecycle content, public API behavior, or implementation code.

## Repo fit

| Responsibility | Correct home | Rule |
|---|---|---|
| Domain governance maps / machine indices | `control_plane/domains/<domain>/` | Child lanes under this root. |
| Control-plane root guidance | `control_plane/README.md` | Root-level control-plane boundary. |
| Human domain doctrine | `docs/domains/<domain>/` | Human-readable domain docs. |
| Semantic contracts | `contracts/domains/<domain>/` | Object meaning and contract boundaries. |
| Machine shape | `schemas/contracts/v1/domains/<domain>/` or accepted schema home | JSON Schema and field shape. |
| Policy rules | `policy/domains/<domain>/` | Allow/deny/restrict/abstain rules. |
| Fixtures/tests | `fixtures/domains/<domain>/`, `tests/domains/<domain>/` | Validation examples and proof. |
| Source registry | source catalog / source registry / data registry roots | SourceDescriptor and source authority metadata. |
| Data lifecycle | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/published` | Lifecycle products. |
| Release/correction/rollback | `release/` | Publication state and rollback. |
| Runtime/API/UI implementation | app/API/UI/package/pipeline roots | Executable behavior. |

## Accepted contents

Only governance-index material belongs here:

| File type | Purpose |
|---|---|
| `README.md` | Explains this root and child-lane boundaries. |
| `<domain>/README.md` | Explains one domain control-plane lane. |
| `<domain>/domain_lane.yaml` | Machine-readable lane metadata and steward pointers. |
| `<domain>/object_family_map.yaml` | Object-family index pointing to contracts/schemas/policy. |
| `<domain>/policy_gate_map.yaml` | Mapping from object families or source roles to policy gates. |
| `<domain>/release_gate_map.yaml` | Mapping from object families to release/correction/rollback gates. |
| `<domain>/reason_code_map.yaml` | Machine-readable reason-code registry or index. |
| `<domain>/sensitivity_matrix_ref.yaml` | Pointers to sensitivity/geoprivacy rules, not the rules themselves. |
| `<domain>/drift_register.yaml` | Machine-readable drift/conflict/deprecation entries. |

## Exclusions

| Do not put here | Correct home |
|---|---|
| Domain object contracts | `contracts/domains/<domain>/` |
| JSON Schema | `schemas/contracts/v1/domains/<domain>/` or accepted schema home |
| Policy code | `policy/domains/<domain>/` |
| Fixtures | `fixtures/domains/<domain>/` |
| Tests or validators | `tests/domains/<domain>/`, `tools/validators/` |
| Raw/work/quarantine/processed/catalog/published data | `data/...` lifecycle roots |
| SourceDescriptor instances | source registry / data registry roots |
| EvidenceBundle/proof records | proof/data roots |
| Release decisions | `release/` |
| UI/API/pipeline code | implementation roots |

## Domain-lane guardrails

- Domain names under this root are segments inside a responsibility root, not new top-level roots.
- Control-plane domain files are indexes and crosswalks, not source truth.
- Register files must point to contracts, schemas, policy, release, source, proof, and data roots without duplicating their authority.
- Sensitive domains and sensitive joins must fail closed through policy pointers, not ad hoc logic in this folder.
- Public clients must not consume control-plane registers as public truth; they use governed APIs and released projections.

## Known child lanes

| Child lane | Status | Purpose |
|---|---|---|
| `habitat/` | CONFIRMED README exists | Habitat-domain governance-index lane for object families, policy gates, release gates, reason codes, sensitivity references, and drift entries. |

## Suggested register pattern

PROPOSED for each domain child lane until files are verified:

```text
control_plane/domains/<domain>/README.md
control_plane/domains/<domain>/domain_lane.yaml
control_plane/domains/<domain>/object_family_map.yaml
control_plane/domains/<domain>/policy_gate_map.yaml
control_plane/domains/<domain>/release_gate_map.yaml
control_plane/domains/<domain>/reason_code_map.yaml
control_plane/domains/<domain>/sensitivity_matrix_ref.yaml
control_plane/domains/<domain>/drift_register.yaml
```

## Validation checklist

- [ ] Confirm which domain child lanes exist.
- [ ] Confirm each register has a schema or validation rule.
- [ ] Confirm control-plane registers point to, but do not duplicate, contracts/schemas/policy/release roots.
- [ ] Confirm sensitive-domain and sensitive-join defaults are represented as pointers to policy.
- [ ] Confirm generated/public clients do not read control-plane registers as public truth.
- [ ] Confirm rollback targets before any migration, renaming, or automated dependency.

## Rollback

Rollback is required if this folder becomes a parallel domain contract root, schema root, policy-code root, source registry, proof store, release root, lifecycle-data root, public API surface, UI implementation root, or a way to bypass policy/release gates.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
