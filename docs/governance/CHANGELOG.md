<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/84480176-1efa-486d-a174-bafeddd5b9bf
title: Governance Changelog
type: standard
version: v1
status: draft
owners: TBD
created: 2026-03-02
updated: 2026-03-02
policy_label: public
related:
  - kfm://doc/TBD  # KFM Definitive Design & Governance Guide (vNext)
  - kfm://doc/TBD  # Tooling the KFM pipeline
  - docs/governance/README.md  # TODO: add/confirm
  - docs/governance/policy/  # TODO: add/confirm
  - policy/  # TODO: add/confirm
  - contracts/  # TODO: add/confirm
  - docs/adr/  # TODO: add/confirm
  - docs/governance/DECISIONS.md  # TODO: add/confirm
  - docs/governance/REVIEW_WORKFLOWS.md  # TODO: add/confirm
  - docs/governance/PROMOTION_CONTRACT.md  # TODO: add/confirm
  - docs/governance/POLICY_LABELS.md  # TODO: add/confirm
tags: [kfm, governance, changelog]
notes:
  - This changelog tracks governance changes that affect policy, promotion gates, review workflows, and evidence/citation rules.
  - Keep entries evidence-linked (ADR/policy tests/receipts) and reversible.
[/KFM_META_BLOCK_V2] -->

# Governance Changelog

**One-line purpose:** Track *governance-surface* changes (policy, promotion gates, review workflows, evidence rules) as auditable, reversible increments.

![status](https://img.shields.io/badge/status-draft-yellow)
![scope](https://img.shields.io/badge/scope-governance-blue)
![policy_label](https://img.shields.io/badge/policy_label-public-brightgreen)
![changelog](https://img.shields.io/badge/format-Keep%20a%20Changelog-lightgrey)
![versioning](https://img.shields.io/badge/versioning-CalVer-8A2BE2)

**Change policy:** default-deny when unclear • cite-or-abstain • fail closed in CI • ship in small, reversible slices.

---

## Navigation

- [What belongs here](#what-belongs-here)
- [How to add an entry](#how-to-add-an-entry)
- [Governance surfaces we track](#governance-surfaces-we-track)
- [Baseline invariants](#baseline-invariants)
- [Changelog](#changelog)
- [References](#references)

---

## What belongs here

This changelog is for **governance changes that affect how KFM makes or enforces trust decisions**, including:

- **Promotion Contract** rules, gates, thresholds, and required artifacts.
- **Policy labels / obligations** (e.g., new `policy_label` values, new redaction obligations, new default-deny rules).
- **Policy-as-code semantics** (OPA/Rego changes that change allow/deny outcomes or obligations).
- **Evidence / citation rules** (EvidenceRef formats, evidence resolver constraints, cite-or-abstain gates).
- **Review workflows** (Promotion Queue, Story Review Queue) and role permissions.
- **Audit / receipts** retention, redaction, and access rules.

**Does *not* belong here** (log elsewhere):

- Pure refactors with no governance behavior impact.
- Dataset-specific content changes (track in dataset release manifests and dataset-specific changelogs).
- UI polish with no trust-membrane or evidence behavior change.

---

## How to add an entry

1. Add an entry under **[Unreleased](#unreleased)**.
2. Include **evidence links** (ADR, policy tests, schema diffs, run receipts, release manifest).
3. Call out **impact scope** (who/what breaks) and **rollback path**.
4. If the change is user-visible, add a short **communication note**.

### Changelog entry template (copy/paste)

```md
### YYYY-MM-DD — <short title>

**Type:** Added | Changed | Deprecated | Removed | Fixed | Security

**What changed**
- 

**Why**
- 

**Impact**
- Users:
- Contributors:
- Operators:

**Migration / Rollback**
- Migration steps:
- Rollback steps:

**Evidence**
- ADR: docs/adr/ADR-XXXX.md
- Policy tests: policy/... (fixtures + expected outcomes)
- Contract/schema: contracts/... (diff)
- Receipt / manifest: data/... or artifacts/... (if applicable)
```

---

## Governance surfaces we track

| Surface | Examples of changes | Where the evidence usually lives |
|---|---|---|
| Policy bundle | allow/deny outcomes, obligations, default-deny tightening | `policy/` + `policy/tests` + CI logs |
| Promotion Contract | required gates/artifacts, thresholds, quarantine rules | `docs/governance/` + schemas + validator outputs |
| Controlled vocabularies | new `policy_label`, `citation.kind`, `artifact.zone` values | `contracts/` + vocab files + tests |
| Evidence resolution contract | EvidenceRef format, resolver behavior, redaction | evidence resolver specs + integration tests |
| Review workflows | Promotion Queue, Story Review Queue rules | workflow docs + UI/backend enforcement |
| Audit and receipts | receipt schema, retention/redaction policy | receipt schema + policy + storage rules |

---

## Baseline invariants

These are **baseline governance invariants**. Changes here are **BREAKING** and must include explicit steward sign-off and a rollback plan.

- **Truth path lifecycle:** upstream → RAW → WORK/QUARANTINE → PROCESSED → CATALOG (DCAT+STAC+PROV + receipts) → PUBLISHED.
- **Trust membrane:** clients never access storage/DB directly; all access is policy-evaluated at the governed API (PEP).
- **Policy-as-code:** the same policy semantics must hold in CI and runtime (fixtures and outcomes must match).
- **Cite-or-abstain:** Story publishing and Focus Mode must not emit unsupported claims; citations must resolve and be policy-allowed.
- **Default deny:** sensitive or unclear licensing/sensitivity must fail closed (quarantine or deny) until resolved.

---

## Changelog

### Unreleased

#### Added
- _(none)_

#### Changed
- _(none)_

#### Deprecated
- _(none)_

#### Removed
- _(none)_

#### Fixed
- _(none)_

#### Security
- _(none)_

---

### 2026-03-02 — Governance changelog scaffold

**Type:** Added

**What changed**
- Added `docs/governance/CHANGELOG.md` to track governance-surface changes with evidence and rollback discipline.
- Captured the *baseline governance invariants* and *entry template* so future changes are consistently recorded.

**Impact**
- No runtime behavior impact (documentation only).

**Evidence**
- KFM governance posture: truth path + promotion gates + trust membrane + cite-or-abstain are documented as core constraints.

---

## References

> NOTE: Replace `TBD` IDs/paths above with the canonical in-repo paths or `kfm://doc/...` identifiers once registered.

- KFM architecture, governance, truth path, promotion contract, and evidence model: `kfm://doc/TBD`
- KFM pipeline tooling, CI gates, and work packages: `kfm://doc/TBD`
