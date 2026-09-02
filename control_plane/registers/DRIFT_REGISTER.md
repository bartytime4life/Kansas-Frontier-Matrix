<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/control-plane-registers-drift-register
title: control_plane/registers/DRIFT_REGISTER.md — Machine-Readable Drift Register Contract
version: v0.1
type: register-profile; control-plane-register; drift-register-guide
status: draft; PROPOSED; scaffold-expanded; control-plane; drift-register; machine-readable-companion; implementation-bounded
owners: OWNER_TBD — Control-plane steward · Register steward · Docs steward · Policy steward · Evidence steward · Release steward
created: NEEDS VERIFICATION — scaffold existed before v0.1 expansion
updated: 2026-06-24
policy_label: public; control-plane; registers; drift-register; governance-index; no-parallel-authority
tags: [kfm, control-plane, registers, drift-register, machine-readable-register, docs-registers, verification, conflict, deprecation, authority]
related:
  - ./README.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/registers/DOCUMENT_REGISTRY.md
  - ../../../docs/registers/VERIFICATION_BACKLOG.md
  - ../../../docs/registers/AUTHORITY_LADDER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../schemas/
  - ../../../policy/
  - ../../../tests/
  - ../../../tools/validators/
notes:
  - "Expanded from a PROPOSED scaffold that referenced this path as planned from domain docs."
  - "This Markdown file profiles the intended machine-readable drift register; it is not itself a validated YAML register."
  - "The human-readable drift register currently exists at `docs/registers/DRIFT_REGISTER.md`."
  - "Machine register shape, schema, validators, and CI enforcement remain NEEDS VERIFICATION."
  - "Rollback target for this expansion is previous scaffold blob SHA `3a4892947bbadf0ae6fa92f20537d1442318ab8c`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Machine-Readable Drift Register Contract

> Control-plane profile for a machine-readable KFM drift register. The register records path drift, authority drift, schema drift, policy drift, provenance drift, implementation-readiness drift, and remediation state. It indexes drift; it does not resolve drift by itself.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: control_plane/registers" src="https://img.shields.io/badge/root-control__plane%2Fregisters-blue">
  <img alt="Boundary: index not authority" src="https://img.shields.io/badge/boundary-index__not__authority-critical">
  <img alt="Shape: needs verification" src="https://img.shields.io/badge/schema-NEEDS__VERIFICATION-orange">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite__or__abstain-green">
</p>

**Status:** draft / PROPOSED  
**Path:** `control_plane/registers/DRIFT_REGISTER.md`  
**Owning root:** `control_plane/registers/`  
**Human-facing counterpart:** `docs/registers/DRIFT_REGISTER.md`  
**Truth posture:** CONFIRMED previous target was a scaffold · CONFIRMED control-plane registers are machine-readable governance indexes and must not become schemas, policy, source data, proof stores, release decisions, or object contracts · CONFIRMED docs-side drift register has human-readable drift entries · NEEDS VERIFICATION for final YAML path, schema, validator, CI wiring, and automated consumers.

## Quick jumps

[Purpose](#purpose) · [Repo fit](#repo-fit) · [Register meaning](#register-meaning) · [Accepted entries](#accepted-entries) · [Entry fields](#entry-fields) · [Exclusions](#exclusions) · [Lifecycle states](#lifecycle-states) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

This file defines the intended control-plane role of a machine-readable drift register.

It may track:

- path or slug conflicts;
- schema-home conflicts;
- contract/schema/policy mismatch;
- source provenance gaps;
- unsupported implementation-maturity claims;
- public-surface drift from governed API/release rules;
- stale or contradictory registry entries;
- remediation, supersession, or rollback status.

It does not create authority, decide policy, validate schemas, approve release, store evidence, or implement remediation.

## Repo fit

| Responsibility | Correct home | Rule |
|---|---|---|
| Machine drift index profile | `control_plane/registers/DRIFT_REGISTER.md` | This file; Markdown profile until YAML shape is verified. |
| Human drift narrative | `docs/registers/DRIFT_REGISTER.md` | Human-readable drift log and review context. |
| Machine register instances | `control_plane/registers/drift_register.yaml` or accepted control-plane path | PROPOSED until verified. |
| Register schema | `schemas/` | Machine shape, when accepted. |
| Register validation | `tools/validators/`, `tests/` | Integrity checks and CI proof. |
| Policy rules | `policy/` | Drift entries may point to policy but do not execute it. |
| Evidence/proof | proof/data roots | EvidenceBundle and receipts remain separate. |
| Release/correction/rollback | `release/` and release contracts | Drift may reference release state but does not approve it. |

## Register meaning

A drift entry records a mismatch between intended governance and observed repository, runtime, source, policy, schema, release, or documentation state.

```text
observed state
  -> compared against intended governing artifact
  -> drift entry created
  -> steward review / remediation / rollback path
  -> status updated or closed with evidence
```

A drift entry is an index record. It must carry enough references for a steward to inspect the evidence and resolution path.

## Accepted entries

| Drift type | Examples |
|---|---|
| `path_drift` | File exists in wrong responsibility root; duplicate canonical homes. |
| `schema_drift` | Contract and schema disagree; schema stub claims maturity. |
| `policy_drift` | Policy root missing, stale, or contradicted by public surface. |
| `source_drift` | Source role, rights, provenance, or cadence unclear. |
| `evidence_drift` | EvidenceRef does not resolve to EvidenceBundle or proof record. |
| `release_drift` | Published/public claims lack release state or rollback target. |
| `implementation_drift` | Docs claim behavior that repo/tests/runtime logs do not prove. |
| `registry_drift` | Machine register and human register disagree. |
| `naming_drift` | Slug/case/alias conflict such as domain-name variants. |

## Entry fields

PROPOSED until schema/validator is verified:

| Field | Meaning |
|---|---|
| `id` | Stable drift identifier. |
| `title` | Short human-readable name. |
| `drift_type` | Controlled drift category. |
| `status` | open, needs_verification, confirmed, remediated, superseded, rejected. |
| `severity` | info, warning, blocker, release_blocker, public_surface_blocker. |
| `observed_path` | Path where the drift was found. |
| `expected_path` | Expected responsibility root or canonical path. |
| `governing_refs` | Directory Rules, ADR, contract, schema, policy, release, or source refs. |
| `evidence_refs` | EvidenceBundle, log, test, commit, or inspection refs. |
| `impact` | What the drift could break or mislead. |
| `remediation` | Required corrective action. |
| `owner` | Steward responsible for review. |
| `opened_at` | Creation date. |
| `updated_at` | Last status update date. |
| `closed_at` | Closure date, if closed. |
| `rollback_ref` | Rollback/correction pointer if relevant. |

## Exclusions

| Do not put here | Correct home |
|---|---|
| Human-only drift narrative | `docs/registers/DRIFT_REGISTER.md` |
| Object contracts | `contracts/` |
| JSON Schema | `schemas/` |
| Policy code | `policy/` |
| EvidenceBundle/proof records | proof/data roots |
| Release decisions | `release/` |
| SourceDescriptor instances | source registry / data registry roots |
| Tests or executable validators | `tests/`, `tools/validators/` |
| Raw/work/quarantine/processed/catalog/published data | `data/...` lifecycle roots |

## Lifecycle states

| State | Meaning |
|---|---|
| `open` | Drift entry created; not yet reviewed. |
| `needs_verification` | Checkable, but not sufficiently verified. |
| `confirmed` | Drift verified from repo evidence, tests, logs, or artifacts. |
| `remediated` | Corrective action completed and evidence attached. |
| `superseded` | Replaced by another drift entry or governance decision. |
| `rejected` | Determined not to be drift, with evidence. |

## Validation checklist

- [ ] Confirm final machine-readable filename and format.
- [ ] Confirm schema for drift entries.
- [ ] Confirm validator and CI wiring.
- [ ] Confirm relationship to `docs/registers/DRIFT_REGISTER.md`.
- [ ] Confirm stable ID format.
- [ ] Confirm status vocabulary.
- [ ] Confirm public-surface blocker handling.
- [ ] Confirm closure requires evidence or steward signoff.

## Rollback

Rollback is required if this file becomes the canonical human narrative register, a policy decision engine, a schema home, a proof store, a release approval record, a source registry, or a way to claim remediation without evidence.

Rollback target for this expansion: previous scaffold blob SHA `3a4892947bbadf0ae6fa92f20537d1442318ab8c`.

<p align="right"><a href="#top">Back to top</a></p>
