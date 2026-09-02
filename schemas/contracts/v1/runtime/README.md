# `schemas/contracts/v1/runtime/` — Runtime Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-runtime-readme
title: schemas/contracts/v1/runtime/ — Runtime Schema Family Index
type: readme; schema-family-index; runtime-schema-boundary; governed-runtime-guardrail
authority_class: schema-family-index
version: v0.2
status: draft; runtime-family-present; mixed-maturity-schemas-present; ai-receipt-overlap; policy-evidence-exposure-overlap; consent-sensitive; layer-manifest-overlap; PROPOSED; no-parallel-authority; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Runtime steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Exposure steward
  - OWNER_TBD — Receipt steward
  - OWNER_TBD — Consent steward
  - OWNER_TBD — Layer steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — short stub existed before v0.2 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; runtime; ai-receipt; run-receipt; decision-envelope; runtime-response-envelope; evidence-drawer-payload; consent-grant; layer-manifest; governed-runtime; evidence-bound; policy-aware; exposure-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, runtime, RuntimeResponseEnvelope, DecisionEnvelope, RunReceipt, AIReceipt, EvidenceDrawerPayload, ConsentGrant, LayerManifest, policy, evidence, exposure, receipts, consent, layer-manifest, no-parallel-authority]
related:
  - ../README.md
  - ./ai_receipt.schema.json
  - ./run_receipt.schema.json
  - ./decision_envelope.schema.json
  - ./runtime_response_envelope.schema.json
  - ./evidence_drawer_payload.schema.json
  - ./consent_grant.schema.json
  - ./layer_manifest.schema.json
  - ../evidence/README.md
  - ../policy/README.md
  - ../exposure/README.md
  - ../receipts/README.md
  - ../layers/README.md
  - ../map/README.md
  - ../review/README.md
  - ../release/README.md
  - ../../../../contracts/runtime/
  - ../../../../policy/runtime/
  - ../../../../fixtures/contracts/v1/runtime/
  - ../../../../tests/
notes:
  - "Expanded from a short stub at schemas/contracts/v1/runtime/README.md."
  - "Current GitHub search surfaced ai_receipt.schema.json, run_receipt.schema.json, consent_grant.schema.json, decision_envelope.schema.json, evidence_drawer_payload.schema.json, runtime_response_envelope.schema.json, and layer_manifest.schema.json under this folder."
  - "runtime_response_envelope.schema.json, decision_envelope.schema.json, run_receipt.schema.json, and ai_receipt.schema.json are concrete PROPOSED schemas with required fields and additionalProperties false."
  - "evidence_drawer_payload.schema.json, consent_grant.schema.json, and layer_manifest.schema.json are PROPOSED empty scaffolds with additionalProperties true."
  - "This folder defines runtime object shapes only; it does not execute code, approve model output, bypass policy, replace evidence, publish layers, or store runtime records."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-runtime-purple)
![shape](https://img.shields.io/badge/authority-machine--shape-informational)
![maturity](https://img.shields.io/badge/maturity-mixed-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/runtime/` is the machine-checkable schema family for runtime-support objects such as decision envelopes, runtime response envelopes, run receipts, AI receipts, evidence drawer payloads, consent grants, and layer manifests.
>
> **One-line boundary.** Runtime schemas define object shape only. They do not execute runtime behavior, approve AI output, bypass policy, replace EvidenceBundles, publish layers, grant consent, or store emitted runtime records.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Current schema inventory](#current-schema-inventory) · [Known overlap and drift risks](#known-overlap-and-drift-risks) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Runtime-family rules](#runtime-family-rules) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/runtime/README.md`. It was a short stub before this expansion. | **CONFIRMED** |
| Are runtime schema files present in this folder? | Yes. Search surfaced seven runtime-family schema files under this folder. | **CONFIRMED path presence** |
| Are all runtime schemas mature/field-complete? | No. The inspected files are mixed: four concrete PROPOSED schemas and three empty scaffolds. | **CONFIRMED mixed maturity** |
| Is this folder runtime execution authority? | No. This folder defines schema shapes only. Runtime code, model calls, policy evaluation, layer publication, and emitted records belong in governed implementation/data roots. | **CONFIRMED boundary** |
| Can schema validation approve an AI/runtime answer? | No. A schema-valid runtime envelope or receipt needs evidence, policy, review/release context where applicable, and auditable runtime records. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A schema-valid runtime object is not runtime truth. It is only a shaped object candidate unless backed by governed inputs, evidence references, policy decisions, runtime records, validation, and release/correction posture where public output depends on it.

---

## Authority and placement

This folder is under the schema responsibility root:

```text
schemas/contracts/v1/runtime/
```

It may define runtime-support object shapes, but adjacent authority is separate:

- `contracts/runtime/` owns runtime object meaning where paired contract docs exist.
- `policy/runtime/` owns runtime policy posture where implemented.
- `schemas/contracts/v1/evidence/` owns EvidenceBundle, EvidenceRef, and evidence-support shapes.
- `schemas/contracts/v1/policy/` owns policy-decision and sensitivity machine shapes.
- `schemas/contracts/v1/exposure/` owns public/client exposure shapes where accepted.
- `schemas/contracts/v1/receipts/` owns receipt object shapes.
- `schemas/contracts/v1/layers/` and `schemas/contracts/v1/map/` own layer/map-facing shapes where accepted.
- `schemas/contracts/v1/review/` and `schemas/contracts/v1/release/` own review/release support shapes where accepted.
- `fixtures/` and `tests/` prove valid/invalid examples and validator behavior.

This README does not amend ADR-0001, Directory Rules, runtime contracts, policy docs, validators, AI governance, public API behavior, or release gates.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── runtime/
        │   ├── README.md                         # this file
        │   ├── runtime_response_envelope.schema.json
        │   ├── decision_envelope.schema.json
        │   ├── run_receipt.schema.json
        │   ├── ai_receipt.schema.json
        │   ├── evidence_drawer_payload.schema.json
        │   ├── consent_grant.schema.json
        │   └── layer_manifest.schema.json
        ├── evidence/
        ├── policy/
        ├── exposure/
        ├── receipts/
        ├── layers/
        ├── map/
        ├── review/
        └── release/

contracts/
└── runtime/                                      # semantic meaning; not schema shape

policy/
└── runtime/                                      # policy posture where implemented; not schema shape

fixtures/
tests/
data/
release/
```

---

## Current schema inventory

| File | Current posture | Shape maturity | Notes |
|---|---|---|---|
| `runtime_response_envelope.schema.json` | **PROPOSED** | Concrete schema | Requires `id`, `spec_hash`, `version`, `issued_at`, `outcome`, `reason_code`, `evidence_refs`, `policy_state`, `freshness`, and `correction_state`; `additionalProperties: false`. |
| `decision_envelope.schema.json` | **PROPOSED** | Concrete schema | Requires `decision_id`, `outcome`, `policy_family`, `reasons`, `obligations`, and `evaluated_at`; `additionalProperties: false`; overlaps policy decision semantics. |
| `run_receipt.schema.json` | **PROPOSED** | Concrete schema | Requires run identity, stage, inputs, outputs, code ref, spec hash, source descriptor refs, validation refs, and outcome; `additionalProperties: false`. |
| `ai_receipt.schema.json` | **PROPOSED** | Concrete schema | Requires AI receipt identity, run id, adapter, model ref, input/output digests, policy decision ref, citation validation ref, and outcome; `additionalProperties: false`. |
| `evidence_drawer_payload.schema.json` | **PROPOSED** | Empty scaffold | Empty `properties`, `additionalProperties: true`, `contract_doc: null`; source doc points to Habitat canonical paths. |
| `consent_grant.schema.json` | **PROPOSED** | Empty scaffold / consent-sensitive | Empty `properties`, `additionalProperties: true`, `contract_doc: null`; source doc points to People-DNA-Land planned files. |
| `layer_manifest.schema.json` | **PROPOSED** | Empty scaffold / layer overlap | Empty `properties`, `additionalProperties: true`, `contract_doc: null`; source doc points to Hazards API contracts. |

---

## Known overlap and drift risks

| Risk | Evidence signal | Required posture |
|---|---|---|
| Runtime vs policy overlap | `decision_envelope.schema.json` includes policy-family, reasons, obligations, and evaluated time. | **Keep policy decision authority separate** |
| Runtime vs evidence overlap | `runtime_response_envelope.schema.json` references evidence refs, and `evidence_drawer_payload.schema.json` is runtime-local but evidence-facing. | **EvidenceBundle/EvidenceRef still outrank runtime language** |
| Runtime vs receipt overlap | `run_receipt.schema.json` and `ai_receipt.schema.json` are receipt-like objects under runtime. | **Needs receipt/profile placement clarity** |
| Runtime vs consent overlap | `consent_grant.schema.json` is an empty scaffold tied to People-DNA-Land planning. | **Fail closed until consent semantics are verified** |
| Runtime vs layer/map overlap | `layer_manifest.schema.json` is an empty runtime scaffold but layer/map schema families also exist. | **Needs layer/profile placement clarity** |
| Namespace drift | Runtime schemas use both `https://schemas.kfm.local/contracts/...`, `https://schemas.kfm.local/schemas/...`, and `kfm://schemas/contracts/...`. | **NEEDS VERIFICATION** |
| Mixed maturity | Some runtime files are concrete; others are empty scaffolds. | **Do not imply completed runtime contract family** |

---

## What belongs here

- This README.
- Machine-checkable JSON Schema files for runtime-support object shapes.
- Schema index notes for runtime object families.
- Migration notes for runtime/policy/evidence/exposure/receipt/layer overlap.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, evidence references, receipt references, review/release references, correction references, rollback references, and tests.

---

## What does not belong here

- Runtime code, model adapters, model prompts as active runtime inputs, pipeline code, validator code, packages, UI/API implementation, map rendering code, layer files, map tiles, or dashboards.
- Emitted runtime records, AI outputs, run receipts as emitted instances, policy decisions, EvidenceBundles, evidence records, consent records, release records, correction records, rollback records, public artifacts, catalog records, triplets, screenshots, or generated summaries.
- Policy rules, governance procedures, consent policy, access-control implementation, release decisions, or public map/API behavior.
- Domain payloads or source payloads.
- Claims that a runtime answer, model output, layer, consent state, or public response is valid, evidence-backed, policy-safe, released, or public-ready merely because it validates against a runtime schema.

---

## Runtime-family rules

| Rule | Requirement |
|---|---|
| Shape is not execution | Schema validation constrains object shape; it does not run code or prove runtime behavior occurred. |
| Runtime is not truth | Runtime envelopes and AI receipts remain downstream of EvidenceBundle support and policy decisions. |
| Runtime is not policy | Runtime records may reference policy posture but do not replace policy evaluation. |
| Runtime is not evidence | Runtime records may cite evidence, but do not replace EvidenceBundles or EvidenceRefs. |
| Receipts stay auditable | Run and AI receipts need clear emitted-record homes, validators, and replay/correction posture. |
| Consent fails closed | Consent objects must not be assumed valid or sufficient without verified consent semantics and policy gates. |
| Layers remain governed | Layer manifests do not publish layers or bypass map/exposure/release gates. |
| Contracts explain meaning | Accepted runtime schemas need paired semantic contracts or approved profiles. |
| Fixtures prove behavior | Accepted schemas need valid and invalid fixtures plus validator coverage. |
| No parallel authority | Equivalent runtime, policy, evidence, receipt, consent, layer, exposure, review, and release shapes must not drift across roots without migration notes. |

---

## Promotion checklist

A runtime schema should not advance beyond `PROPOSED` unless:

- [ ] Paired semantic contract exists or an approved profile is documented.
- [ ] `$id` namespace convention is settled.
- [ ] Required fields are defined.
- [ ] Object role is separated from policy, evidence, exposure, receipt, consent, layer, review, release, and emitted runtime records.
- [ ] Evidence reference requirements are defined where runtime output depends on claims.
- [ ] Policy reference requirements are defined where runtime output depends on admissibility.
- [ ] Receipt/emitted-record storage paths are documented where the object is receipt-like.
- [ ] Consent semantics and policy references are verified where the object concerns consent.
- [ ] Public exposure/release requirements are defined where runtime outputs can be shown to clients.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validators exist and paths are correct.
- [ ] CI/schema-test coverage exists.
- [ ] Migration notes exist for duplicate or overlapping schema surfaces.
- [ ] Correction and rollback references are defined where public use depends on runtime output.

---

## Validation

Recommended local validation sequence:

```bash
# Inspect the runtime schema family.
find schemas/contracts/v1/runtime -maxdepth 3 -type f | sort

# Detect runtime/policy/evidence/exposure/receipt/layer overlap.
find schemas/contracts/v1 -maxdepth 5 -type f \
  | grep -Ei 'runtime|decision_envelope|runtime_response|ai_receipt|run_receipt|evidence_drawer|consent_grant|layer_manifest|policy|evidence|exposure|receipt|layer|map' \
  | sort

# Validate JSON syntax for runtime schemas.
find schemas/contracts/v1/runtime -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Inspect paired contracts and fixtures when present.
find contracts/runtime fixtures/contracts/v1/runtime -maxdepth 5 -type f 2>/dev/null | sort

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/policy tests/governance tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/runtime/README.md`.

Rollback for future runtime schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore policy, evidence, exposure, receipt, consent, layer, map, review, release, correction, and rollback references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers where applicable.
7. Preserve correction and rollback records if any public or semi-public runtime surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Which runtime schemas are intended to be field-complete in v1 and which are temporary scaffolds? | **NEEDS VERIFICATION** | Runtime steward + Schema steward |
| Should AI/run receipt schemas remain under `runtime/`, move under `receipts/`, or become explicit runtime receipt profiles? | **NEEDS VERIFICATION / migration-sensitive** | Runtime steward + Receipt steward |
| Should `decision_envelope` remain under runtime, policy, or a shared policy-runtime profile? | **NEEDS VERIFICATION / ADR-sensitive** | Runtime steward + Policy steward |
| Should `layer_manifest` remain under runtime, move under layers/map, or become a runtime projection profile? | **NEEDS VERIFICATION / layer-sensitive** | Runtime steward + Layer steward |
| Which consent grant shape is acceptable for People-DNA-Land or other consent-sensitive surfaces? | **NEEDS VERIFICATION / consent-sensitive** | Consent steward + Policy steward |
| Which runtime projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this folder focused on runtime-support schema shape, not runtime execution.
- Treat current schemas as PROPOSED until contracts, fixtures, validators, CI, and overlap decisions are verified.
- Prevent drift between runtime, policy, evidence, exposure, receipts, consent, layers, review, release, correction, and rollback surfaces.
- Preserve evidence, policy, consent, exposure, release, correction, and rollback boundaries for every public or semi-public runtime surface.
