# `schemas/contracts/v1/exposure/` — Exposure Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-exposure-readme
title: schemas/contracts/v1/exposure/ — Exposure Schema Family Index
type: readme; schema-family-index; exposure-governance-boundary
authority_class: schema-family-index
version: v0.1
status: draft; empty-family-index; proposed-schema-family; no-current-schema-files-found; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Exposure steward
  - OWNER_TBD — Security steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; exposure; trust-membrane; public-surface; access-control; sensitivity; release-gated; deny-by-default; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, exposure, public-surface, trust-membrane, governed-api, sensitivity, redaction, access, release, policy-decision, exposure-decision, exposure-surface, exposure-audit]
related:
  - ../README.md
  - ../policy/sensitivity_label.schema.json
  - ../evidence/evidence_bundle.schema.json
  - ../evidence/redaction_receipt.schema.json
  - ../../../../docs/security/EXPOSURE_PLAN.md
  - ../../../../policy/access/README.md
  - ../../../../contracts/policy/policy_decision.md
  - ../../../../contracts/policy/sensitivity_label.md
  - ../../../../docs/doctrine/policy-aware.md
  - ../../../../docs/architecture/sensitivity.md
  - ../../../../docs/architecture/critical-asset-exposure.md
  - ../../../../release/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/exposure/README.md."
  - "GitHub search did not surface existing files under schemas/contracts/v1/exposure/ beyond this README in the current check."
  - "Exposure shape is adjacent to, but not a replacement for, policy, access, sensitivity, evidence, release, security, or runtime enforcement."
  - "docs/security/EXPOSURE_PLAN.md describes exposure posture and trust membrane; this README only defines the proposed schema-family boundary."
  - "Do not create exposure schemas here that duplicate policy_decision, sensitivity_label, release_manifest, or redaction_receipt authority without contract/schema review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-exposure-purple)
![shape](https://img.shields.io/badge/authority-machine--shape-informational)
![default](https://img.shields.io/badge/default-deny--by--default-critical)
![maturity](https://img.shields.io/badge/maturity-empty__family__index-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/exposure/` is the proposed schema-family home for machine-checkable shapes that describe public/semi-public exposure surfaces, exposure decisions, exposure envelopes, exposure audits, and trust-membrane crossing metadata.
>
> **One-line boundary.** This folder may define exposure object **shape**. It does not make exposure decisions, grant access, downgrade sensitivity, publish data, approve releases, store public artifacts, or bypass governed APIs.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Candidate schemas](#candidate-schemas) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Schema-family rules](#schema-family-rules) · [Trust membrane guardrails](#trust-membrane-guardrails) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/exposure/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are exposure schema files currently present in this folder? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Is `exposure/` already listed as a real-shape family in `schemas/contracts/v1/README.md`? | Not confirmed in the current evidence. | **NEEDS VERIFICATION** |
| Is this a policy or security document? | No. It is a schema-family index that links to policy/security authorities. | **CONFIRMED boundary** |
| Can schemas here decide public exposure? | No. They may shape exposure inputs/outputs, but decisions require policy, evidence, release, and governed API enforcement. | **CONFIRMED governance posture** |
| Should new schema files be added here without review? | No. Add only after paired contracts, fixtures, validators, and steward review are planned. | **PROPOSED discipline** |

> [!IMPORTANT]
> Exposure is policy-significant. A valid exposure-shaped JSON payload is not permission to expose anything. Public and semi-public surfaces remain deny-by-default unless evidence, policy, sensitivity, rights, review, release, and rollback support are resolved.

---

## Authority and placement

The exposure family belongs under `schemas/contracts/v1/` only as machine-checkable shape. Adjacent authority is split across roots:

- `docs/security/EXPOSURE_PLAN.md` describes human-facing exposure posture and the trust membrane.
- `policy/access/` defines who may use bounded capabilities.
- `policy/` and `contracts/policy/` define policy decision meaning and posture.
- `schemas/contracts/v1/policy/` defines policy-related machine shapes such as sensitivity labels.
- `schemas/contracts/v1/evidence/` defines EvidenceRef/EvidenceBundle and redaction receipt shapes.
- `release/` owns release, correction, withdrawal, and rollback decisions.
- Governed API/runtime surfaces enforce the trust membrane; this schema folder does not.

This README does not amend policy, security, release, Directory Rules, or ADR-0001.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── policy/
        │   └── sensitivity_label.schema.json          # adjacent policy shape; PROPOSED
        ├── evidence/
        │   ├── evidence_bundle.schema.json            # evidence closure shape; PROPOSED
        │   └── redaction_receipt.schema.json          # redaction receipt shape; maturity NEEDS VERIFICATION
        └── exposure/
            └── README.md                              # this file; proposed empty-family index

policy/
├── access/                                             # who may use bounded capabilities
└── ...                                                 # allow / deny / restrict / abstain / redaction posture

docs/
└── security/
    └── EXPOSURE_PLAN.md                                # exposure posture and trust membrane guidance

release/                                                # publication, correction, withdrawal, rollback authority
```

---

## Current inventory

Current check:

| Path | Status | Note |
|---|---|---|
| `schemas/contracts/v1/exposure/README.md` | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/exposure/*.schema.json` | **Not found in current search** | Treat family as proposed/empty until a mounted checkout or schema registry proves otherwise. |

Related surfaced files outside this folder:

| Related path | Why it matters |
|---|---|
| `docs/security/EXPOSURE_PLAN.md` | Human-facing exposure posture; trust membrane and deny-by-default framing. |
| `policy/access/README.md` | Access-control policy lane; who may use bounded capabilities. |
| `schemas/contracts/v1/policy/sensitivity_label.schema.json` | Adjacent sensitivity shape used by evidence and exposure decisions. |
| `schemas/contracts/v1/evidence/evidence_bundle.schema.json` | Evidence support required before public truth or exposure. |
| `schemas/contracts/v1/evidence/redaction_receipt.schema.json` | Adjacent shape for redaction/generalization receipts. |

---

## Candidate schemas

The following are candidate shapes only. Do not add them without paired semantic contracts, fixture plan, validator plan, and steward review.

| Candidate schema | Purpose | Status |
|---|---|---|
| `exposure_surface.schema.json` | Describes a public/semi-public surface: route, file, tile, export, UI panel, API endpoint, log, or hosted artifact. | **PROPOSED** |
| `exposure_decision.schema.json` | Records finite allow/deny/restrict/abstain/error outcome for a requested exposure. | **PROPOSED** |
| `exposure_envelope.schema.json` | Runtime-safe envelope for what may cross the trust membrane. | **PROPOSED** |
| `exposure_audit_event.schema.json` | Auditable event for an exposure check, denial, transform, release, withdrawal, or attempted bypass. | **PROPOSED** |
| `public_surface_manifest.schema.json` | Manifest for a public-facing release surface, tied to evidence, policy, release, and rollback refs. | **PROPOSED** |
| `exposure_transform.schema.json` | Describes redaction, generalization, aggregation, clipping, delay, or other transform before exposure. | **PROPOSED** |
| `exposure_failure.schema.json` | Shape for deny/abstain/error responses when exposure checks fail. | **PROPOSED** |

> [!CAUTION]
> Some candidate shapes may belong in existing families instead: `policy/`, `runtime/`, `release/`, `evidence/`, or domain-specific schema lanes. Choose `exposure/` only when the primary responsibility is the shape of crossing the external/public boundary.

---

## What belongs here

- This README.
- Exposure-family JSON Schema files after contract/schema review.
- Machine-readable shapes for exposure surfaces, exposure decisions, trust-membrane crossing envelopes, public surface manifests, exposure transforms, and exposure audit events when they do not belong more specifically under `policy/`, `runtime/`, `release/`, or `evidence/`.
- Migration notes, mirror notices, or deprecation notes for exposure schema placement.
- Links to paired contracts, fixtures, validators, policy, security docs, release records, correction/withdrawal records, rollback cards, and tests.

---

## What does not belong here

- Policy rules or access-control logic.
- Security posture documents.
- Secrets, tokens, credentials, keys, or deployment configuration.
- Runtime/governed API implementation.
- Public app route implementation.
- Release approvals, release manifests, correction notices, withdrawal notices, or rollback cards as emitted records.
- EvidenceBundle instances, proofs, receipts, source payloads, or catalog records as data.
- Map tiles, PMTiles, COGs, GeoParquet, screenshots, dashboards, public exports, or generated summaries.
- Domain policy profiles, sensitivity rubrics, or redaction decisions.
- Claims that an object is safe to expose merely because it validates against a schema.

---

## Schema-family rules

| Rule | Requirement |
|---|---|
| Deny-by-default | Missing evidence, policy, release, sensitivity, rights, or rollback context should shape a deny/abstain/error outcome, not an allow. |
| Evidence dependency | Exposure shapes should reference EvidenceRef/EvidenceBundle where claims or artifacts depend on evidence. |
| Policy dependency | Exposure decisions should reference policy decisions, sensitivity labels, rights posture, and access posture without becoming policy authority. |
| Release dependency | Public exposure should reference release/correction/withdrawal/rollback surfaces where applicable. |
| Lifecycle separation | RAW, WORK, QUARANTINE, internal canonical stores, unpublished candidates, direct source-system side effects, and direct model outputs must not be exposed to normal public clients. |
| Transform visibility | Redaction, generalization, aggregation, clipping, delay, or geoprivacy transforms must be visible through transform refs or receipts. |
| Public client boundary | Public clients should consume governed APIs and released artifacts, not this schema folder or internal lifecycle stores. |
| Auditability | Exposure checks should be auditable without leaking protected details. |
| No parallel authority | Do not duplicate policy, release, evidence, or runtime schemas under `exposure/` without ADR/migration notes. |

---

## Trust membrane guardrails

Exposure schemas should preserve the trust membrane described in the exposure posture:

```text
non-public lifecycle stores
  RAW / WORK / QUARANTINE / PROCESSED / CATALOG / TRIPLET / candidates / internal stores
        ↓
trust membrane
  evidence resolution + citation validation + rights + sensitivity + policy + release + finite outcome
        ↓
public-safe surfaces
  governed API responses + released artifacts + public UI + public-safe exports
```

Required default outcomes:

| Condition | Shape expectation |
|---|---|
| Evidence unresolved | `ABSTAIN`, `DENY`, or `ERROR`; never silent allow. |
| Policy missing | `DENY` or `ERROR`; fail closed. |
| Sensitivity unclear | `DENY`, `RESTRICT`, `GENERALIZE`, or `QUARANTINE` depending on policy; never publish precise sensitive content by default. |
| Release missing | `DENY` for public exposure. |
| Rights unclear | `DENY` or `RESTRICT`; no silent public reuse. |
| Rollback target missing | Do not promote; mark **NEEDS VERIFICATION**. |
| Direct internal-store access requested | `DENY`; normal public path must use governed interfaces. |

---

## Promotion checklist

An exposure schema should not advance beyond `PROPOSED` unless:

- [ ] Primary responsibility is exposure shape, not policy, runtime, release, evidence, or domain semantics.
- [ ] Paired semantic contract exists or is explicitly marked **NEEDS VERIFICATION**.
- [ ] `$id` and filename are stable.
- [ ] JSON Schema dialect is pinned.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validator implementation exists.
- [ ] CI/schema-test support exists.
- [ ] Policy references are explicit.
- [ ] Evidence references are explicit where claims/artifacts depend on evidence.
- [ ] Release, correction, withdrawal, and rollback references are explicit where public exposure is possible.
- [ ] Sensitive-domain deny/restrict/generalize cases are tested.
- [ ] Direct lifecycle-store and direct model-output bypass cases are tested as deny/error outcomes.

---

## Validation

Recommended local validation sequence:

```bash
# Inspect current exposure schema family.
find schemas/contracts/v1/exposure -maxdepth 2 -type f | sort

# Look for possible duplicate exposure authority elsewhere.
find schemas/contracts/v1 policy contracts docs/security -maxdepth 5 -type f \
  | grep -Ei 'exposure|public_surface|trust_membrane|access|sensitivity|redaction|release|withdrawal' \
  | sort

# Validate JSON syntax once schemas exist.
find schemas/contracts/v1/exposure -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/policy tests/security || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/exposure/README.md`.

Rollback for future exposure schemas requires checking every downstream reference:

1. Revert or migrate the schema file.
2. Revert or update paired semantic contracts.
3. Revert or update fixtures and validators.
4. Revert or update schema registry entries.
5. Revert or update policy/runtime/release/evidence references.
6. Revert or update governed API payloads, public UI payloads, MapLibre layer descriptors, Evidence Drawer payloads, and public export manifests.
7. Preserve correction/withdrawal/rollback records for any public surface affected by schema changes.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should `exposure/` be a first-class schema family or should exposure shapes live under `policy/`, `runtime/`, `release/`, or `evidence/`? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + security steward |
| Which exposure object families are actually needed? | **PROPOSED** | Exposure steward |
| Is there an accepted semantic contract home for exposure objects? | **NEEDS VERIFICATION** | Contract steward |
| Which fixtures should prove deny-by-default behavior? | **NEEDS VERIFICATION** | Validation steward |
| Which governed API payloads need exposure envelopes? | **NEEDS VERIFICATION** | API/UI steward |
| Which release/correction/withdrawal/rollback contracts should exposure schemas reference? | **NEEDS VERIFICATION** | Release steward |
| Which sensitive domains require exposure-specific generalization or denial fixtures? | **NEEDS VERIFICATION** | Policy steward + domain stewards |

---

## Maintainer notes

- Keep this folder empty except for this README until the exposure family is accepted or a specific schema is reviewed.
- Do not use exposure schemas to bypass policy or release.
- Prefer fail-closed outcomes where evidence, rights, sensitivity, release, or rollback support is missing.
- Public truth still requires evidence, policy, review, release, correction, and rollback support; schema shape alone is never enough.
