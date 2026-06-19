<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-manual-curation-readme
title: connectors/manual_curation/ — Manual Curation Connector Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Docs steward · Validation steward · Rights reviewer · Sensitivity reviewer
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; connector-boundary; manual-curation; steward-assisted; no-publication; quarantine-aware; implementation-depth-needs-verification
proposed_path: connectors/manual_curation/README.md
truth_posture: CONFIRMED path exists / PROPOSED connector boundary / IMPLEMENTATION DEPTH NEEDS VERIFICATION
related:
  - ../README.md
  - ../../docs/sources/catalog/manual_curation/README.md
  - ../../docs/sources/catalog/manual_curation/steward-curation-workflow.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../docs/sources/source-roles.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/trust-membrane.md
  - ../../docs/doctrine/lifecycle-law.md
  - ../../docs/doctrine/truth-posture.md
  - ../../docs/governance/separation-of-duties.md
  - ../../data/registry/sources/
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/sources/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, manual-curation, source-admission, steward-review, source-descriptor, source-role, quarantine, validation, evidencebundle, catalog-closure, governance]
notes:
  - "This README replaces the greenfield stub in `connectors/manual_curation/`."
  - "The manual-curation catalog README states it is methodology and steward reference, not implementation proof."
  - "Manual curation is the human-governed path for source material that cannot safely advance by automation alone."
  - "This connector boundary may support steward-assisted intake helpers only; release, policy, source-role upgrade, and catalog closure remain governed outside this folder."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Manual Curation Connector Boundary

> Connector-boundary README for `connectors/manual_curation/`. This folder may support steward-assisted source-intake helpers for manual curation, but it is **not** a release engine, source registry, policy authority, catalog-closure authority, public API, proof root, or publication path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Truth: implementation depth needs verification" src="https://img.shields.io/badge/truth-implementation__needs__verification-orange">
  <img alt="Policy: cite or abstain" src="https://img.shields.io/badge/posture-cite__or__abstain-success">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` connector-boundary README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/manual_curation/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `PROPOSED` connector boundary · `NEEDS VERIFICATION` implementation files, tests, fixtures, and CI wiring  
> **Boundary:** steward-assisted intake helpers only; no source activation, no source-role upgrade, no catalog closure, no direct publication.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed responsibilities](#allowed-responsibilities) · [Forbidden responsibilities](#forbidden-responsibilities) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation](#validation) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/manual_curation/` is a proposed helper boundary for steward-assisted source-intake and review workflows.

Manual curation applies when source material cannot safely advance by automation alone because source role, rights, sensitivity, provenance, evidence closure, validation, review state, correction state, or rollback state is unresolved.

This folder may assist with creating candidate intake records, assembling review packets, preserving evidence references, recording defect reasons, and routing records toward RAW or QUARANTINE handoff. It must not decide final authority, public visibility, catalog closure, or release.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/manual_curation/` | Proposed steward-assisted connector/helper lane. | **CONFIRMED path / PROPOSED boundary** |
| `docs/sources/catalog/manual_curation/README.md` | Manual-curation methodology and steward reference. | **CONFIRMED** |
| `docs/sources/catalog/manual_curation/steward-curation-workflow.md` | Steward workflow reference. | **CONFIRMED search result / NEEDS FILE REVIEW** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside connector / NEEDS VERIFICATION for entries** |
| `data/raw/` and `data/quarantine/` | Candidate handoff targets. | **Outside connector** |
| `policy/sources/`, `policy/sensitivity/`, `policy/rights/` | Policy authority roots. | **Outside connector** |
| `release/` | Release and publication controls. | **Out of scope for this connector** |

---

## Allowed responsibilities

This folder may support helpers for:

- candidate intake packets;
- SourceDescriptor drafting support;
- SourceActivationDecision preparation support;
- source-role review queues;
- rights and sensitivity review routing;
- evidence-reference collection;
- validation-defect summaries;
- quarantine-reason recording;
- correction and rollback handoff notes;
- RAW or QUARANTINE handoff envelopes;
- steward-facing audit notes that do not bypass review.

---

## Forbidden responsibilities

This folder must not:

- approve source activation;
- upgrade source role by convenience;
- decide rights, sensitivity, release class, or public visibility;
- close catalog records;
- write directly to processed, catalog, triplet, published, proof, receipt, or release roots;
- treat AI or watcher output as approval;
- replace EvidenceBundle, policy review, release review, correction path, or rollback target requirements.

[Back to top ↑](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/manual_curation/README.md` | **CONFIRMED** | Target file existed as a greenfield stub before this update. | Does not prove connector code, tests, or CI. |
| `docs/sources/catalog/manual_curation/README.md` | **CONFIRMED** | Manual curation is steward-led methodology; it is not implementation proof; it reinforces lifecycle, source-role anti-collapse, deny-by-default, and cite-or-abstain posture. | Exact workflow implementation, route names, schemas, and tooling remain unverified. |
| `docs/sources/catalog/manual_curation/steward-curation-workflow.md` | **CONFIRMED search result / NEEDS FILE REVIEW** | Search confirms a steward workflow doc exists. | File body was not inspected in this response. |
| Actual connector implementation | **NEEDS VERIFICATION** | This README defines intended boundaries. | Actual modules, fixtures, tests, and CI remain unverified. |

---

## Runtime posture

Default runtime posture:

- no source activation decision;
- no source-role upgrade;
- no public output;
- no catalog closure;
- no release artifact creation;
- no direct writes beyond RAW or QUARANTINE handoff envelopes;
- deterministic failure when descriptor, rights, sensitivity, source role, evidence, validation, review, correction, or rollback state is unresolved.

---

## Validation

Validation should check that:

- every candidate has a descriptor or descriptor-draft reference;
- source role remains explicit and cannot collapse into convenience labels;
- rights and sensitivity states are explicit or routed to quarantine;
- evidence references are preserved and resolvable before catalog closure;
- AI or watcher summaries are advisory only;
- unresolved material routes to quarantine or abstention;
- connector output is limited to RAW or QUARANTINE handoff;
- release and catalog-closure claims are not emitted by connector helpers.

Tests must prove these boundaries before implementation maturity is claimed.

---

## Rollback

Rollback is required if this README is used to justify source activation, source-role upgrade, catalog closure, release approval, public visibility, or policy authority without verified steward review and implementation evidence.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

A safe rollback is to restore the prior greenfield stub or replace this document with a shorter helper-boundary note until implementation files and tests are verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual connector/helper code under `connectors/manual_curation/`. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm workflow relationship to manual-curation docs. | **NEEDS VERIFICATION** | Steward workflow file body and ADR/path decision. |
| Confirm SourceDescriptor and activation-decision support. | **NEEDS VERIFICATION** | Registry entries, schemas, code, and tests. |
| Confirm rights/sensitivity/review-state handling. | **NEEDS VERIFICATION** | Policy references, code, and tests. |
| Confirm RAW/QUARANTINE handoff envelope shape. | **NEEDS VERIFICATION** | Schemas/contracts and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Manual curation is where human review protects the trust membrane. Keep this folder as a helper lane. Authority lives in descriptors, policy decisions, validation receipts, EvidenceBundles, release records, correction paths, and rollback targets outside this connector.

[Back to top ↑](#top)
