<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/control-plane-registers-drift-register
title: control_plane/registers/DRIFT_REGISTER.md — Machine-Readable Drift Register Contract
version: v0.2
type: register-profile; control-plane-register; drift-register-guide; currentness-reconciliation
status: draft; PROPOSED; repository-grounded; current-main-reconciled; scaffold-expanded; control-plane; drift-register; machine-readable-companion; implementation-bounded
owners: OWNER_TBD — Control-plane steward · Register steward · Docs steward · Policy steward · Evidence steward · Release steward
created: NEEDS VERIFICATION — scaffold existed before v0.1 expansion
updated: 2026-09-06
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
  - "This v0.2 update refreshes current-main evidence only; it does not create a machine register, change repository settings, resolve an incident, or authorize merge, release, deployment, promotion, or publication."
  - "The active ruleset readback still lacks a required_status_checks rule even though main contains the repository-control authorization workflow; this is an observed enforcement gap, not a settings-change authorization."
  - "The surrounding control-plane README and register-lane README retain older evidence snapshots; this profile records that currentness mismatch without silently rewriting those owner surfaces."
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 1e69410cfd871e1ec004eedcd23f845eff435137
  target_blob_before_update: 2c472bd2552b758d365a8e9311aaa19ff4d5d7b9
  control_plane_root_blob: 51026faa37b2ebe940472e1d513a25cd0832c692
  registers_lane_readme_blob: aee5412b9c4ebd8b6343a07f628dd7210bc30695
  human_drift_register_blob: 5c5078b93c467e66f4cc8b86a7a696dbce5ae7e0
  docs_control_plane_workflow_blob: ed0d3b50a12931b67cad005cd99433924c829fa3
  register_meta_contract_test_blob: 83e74c1c657d06f9c7b4bd256419a8aa8868d173
  repository_control_workflow_blob: 7d4e1dd250a1114898599ccedc14b99ff0577523
  active_ruleset: Protect / 15484585
  open_pull_requests: 1
  open_pull_request_set: "#4325 control_plane/README.md; path-disjoint from this target"
  required_status_checks_rule: ABSENT_AT_READBACK
  checked_at: 2026-09-06

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

**Status:** draft / PROPOSED · current-main reconciliation recorded 2026-09-06  
**Path:** `control_plane/registers/DRIFT_REGISTER.md`  
**Owning root:** `control_plane/registers/`  
**Human-facing counterpart:** `docs/registers/DRIFT_REGISTER.md`  
**Truth posture:** CONFIRMED previous target was a scaffold · CONFIRMED the current implementation authority is main@1e69410cfd871e1ec004eedcd23f845eff435137 at the bounded readback · CONFIRMED control-plane registers are machine-readable governance indexes and must not become schemas, policy, source data, proof stores, release decisions, or object contracts · CONFIRMED docs-side drift register has human-readable drift entries · CONFIRMED the active ruleset readback has no required-status-check rule while repository-control.yml exists · NEEDS VERIFICATION for server-side enforcement, final YAML path, schema, validator, CI wiring, independent review, and automated consumers.

## Quick jumps

[Purpose](#purpose) · [Repo fit](#repo-fit) · [Register meaning](#register-meaning) · [Current reconciliation](#current-reconciliation) · [Accepted entries](#accepted-entries) · [Entry fields](#entry-fields) · [Exclusions](#exclusions) · [Lifecycle states](#lifecycle-states) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

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

## Current reconciliation

**Readback date:** 2026-09-06 UTC  
**Implementation authority:** [main@1e69410cfd871e1ec004eedcd23f845eff435137](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/1e69410cfd871e1ec004eedcd23f845137)  
**Scope:** profile currentness and drift indexing only. This snapshot does not admit a YAML instance, change a ruleset, resolve an incident, or promote a register.

| Observed surface | Current evidence | Bounded interpretation |
|---|---|---|
| Repository tip | main@1e69410cfd871e1ec004eedcd23f845eff435137; open pull requests: 1 (#4325 targets control_plane/README.md) | CONFIRMED by direct GitHub readback at this snapshot; no direct target-path overlap was found; point-in-time evidence only. |
| Profile/human pair | This profile was blob 2c472bd2552b758d365a8e9311aaa19ff4d5d7b9 before this update; docs/registers/DRIFT_REGISTER.md is blob 5c5078b93c467e66f4cc8b86a7a696dbce5ae7e0. | CONFIRMED paired paths; the Markdown profile remains non-authoritative and no child YAML instance is established. |
| Register lane | control_plane/registers/README.md is blob aee5412b9c4ebd8b6343a07f628dd7210bc30695; it records nine required root YAML registers, one populated and eight empty at its older snapshot. | CONFIRMED lane relationship; current population and cross-register semantic closure remain NEEDS VERIFICATION. |
| Bounded validation | docs-control-plane.yml is blob ed0d3b50a12931b67cad005cd99433924c829fa3; the register meta-contract test is blob 83e74c1c657d06f9c7b4bd256419a8aa8868d173. | CONFIRMED bounded repository checks; they do not make this Markdown file a YAML instance or establish semantic closure. |
| Merge authorization control | Active Protect ruleset 15484585 has zero required approvals and no required_status_checks rule. Main contains repository-control.yml, blob 7d4e1dd250a1114898599ccedc14b99ff0577523, with an authorize-ready-and-merge job. | CONFIRMED enforcement gap at the ruleset readback; workflow presence is not proof that GitHub rejects an unauthorized merge. |
| Adjacent profile currentness | control_plane/README.md embeds an older base_commit: 6aa1ce50dfc4e818e5f33d47fff24b6d06a1c91e and updated: 2026-08-22; control_plane/registers/README.md embeds base_commit: 4e5e4870ac47b4fe5075c5c163ce363061783cee and updated: 2026-07-24. | CONFIRMED snapshot divergence; whether those older pins are intentionally historical or require repinning is OPEN. |

### Indexed drift signals (non-authoritative)

1. **Authorization-enforcement drift — policy_drift / implementation_drift**  
   **State:** confirmed for the missing server-side required-check rule; remediation is not complete.  
   **Impact:** the repository-control workflow can report a hold without the active ruleset necessarily blocking a merge.  
   **Next bounded action:** separately authorize a settings operation, then run capability-separated negative and positive canaries that prove GitHub rejects an unauthorized merge before integration. Do not infer enforcement from workflow presence or from a merged commit.

2. **Register-snapshot drift — registry_drift**  
   **State:** needs_verification; the mismatch is observed, but the intended repin cadence and owner are not established.  
   **Impact:** readers can mistake an embedded historical base for current repository state, or treat a profile refresh as synchronized closure for neighboring documents.  
   **Next bounded action:** decide and document a reviewed repin cadence for control_plane/README.md and control_plane/registers/README.md; keep this profile’s snapshot explicitly dated until then.

3. **Lifecycle/coordination drift — implementation_drift / evidence_drift**  
   **State:** confirmed historical evidence; current cause and prevention remain unresolved. The current Workbench readback records the #4313/#4315/#4317/#4318 draft-to-ready-to-merge conflicts and the missing ruleset requirement; GitHub remains implementation authority.  
   **Impact:** draft-only records, GitHub terminal state, and server-side authorization evidence can disagree, so a merged commit must not be treated as proof of review or approval.  
   **Next bounded action:** preserve the incident records, independently reconcile each lifecycle event, and close the prevention gap only through an authorized settings change and canary evidence.

### Coordination cross-check

- [Notion KFM Repository Workbench](https://app.notion.com/p/3c9a92021bf68195b8b1f3a8d694b447?pvs=204) was read at 2026-09-06T06:07Z as a coordination mirror. It agrees with the current GitHub main pin and records the ruleset gap and lifecycle history; it does not override GitHub implementation authority.
- [Google Drive KFM System Chronicle](https://docs.google.com/document/d/1fBOUDqrcsHaPJiEfM5HmtJL7fBMKFr-rgoN2ge_uVrI/edit) was read read-only. Its current document contains older main pins (87099f5… and 7c5d412…) and explicitly treats GitHub as implementation authority; those entries remain historical coordination evidence and do not override the current GitHub readback.

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

Rollback target for this v0.2 currentness update: restore the pre-update profile blob 2c472bd2552b758d365a8e9311aaa19ff4d5d7b9 through a reviewed forward revert.\n\nRollback target for the original scaffold expansion remains: previous scaffold blob SHA 3a4892947bbadf0ae6fa92f20537d1442318ab8c.

<p align="right"><a href="#top">Back to top</a></p>
