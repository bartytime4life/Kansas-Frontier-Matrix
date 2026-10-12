<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-policy-policy-input-bundle
title: PolicyInputBundle Semantic Contract
type: contract
version: v0.2
status: draft; PROPOSED; greenfield-schema; policy-runtime-aware
owners: OWNER_TBD — Policy steward · Contracts steward · Schema steward · Policy-runtime steward · Evidence steward · Source steward · Release steward · Docs steward
created: NEEDS VERIFICATION — contract existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; policy; policy-input-bundle; explicit-inputs; fail-closed; evidence-aware; source-role-aware; rights-aware; sensitivity-aware; no-hidden-fetches
related:
  - ./README.md
  - ./policy_decision.md
  - ./sensitivity_label.md
  - ../evidence/evidence_bundle.md
  - ../source/source_descriptor.md
  - ../runtime/decision_envelope.md
  - ../../schemas/contracts/v1/policy/policy_input_bundle.schema.json
  - ../../policy/
  - ../../packages/policy-runtime/README.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../docs/architecture/governed-ai/FOCUS_FLOW.md
  - ../../docs/standards/MAP_TRUST_STATES.md
  - ../../docs/architecture/publication/RELEASE_GATES.md
  - ../../fixtures/policy/policy_input_bundle/
  - ../../tests/contracts/policy/
tags: [kfm, contracts, policy, policy-input-bundle, policy-decision, explicit-inputs, evidence-ref, evidence-bundle, source-role, rights, sensitivity, lifecycle, audience, operation, fail-closed, no-hidden-fetches]
notes:
  - "Expanded from greenfield scaffold at `contracts/policy/policy_input_bundle.md`."
  - "Paired schema verified at `schemas/contracts/v1/policy/policy_input_bundle.schema.json`; schema is currently a greenfield placeholder with only `id` required and `additionalProperties: true`."
  - "This contract defines semantic meaning only. It does not author executable policy, define JSON Schema shape, execute policy runtime helpers, fetch missing facts, issue receipts, publish artifacts, or override release gates."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# PolicyInputBundle

> `PolicyInputBundle` is the explicit, inspectable input object submitted to a policy gate. It gathers the operation, audience, object references, evidence state, source-role state, rights posture, sensitivity posture, lifecycle/release context, and evaluator context needed for policy evaluation. It must not fetch missing facts, embed raw sensitive data, or stand in for evidence, policy, review, release, or AI truth.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Schema: greenfield" src="https://img.shields.io/badge/schema-greenfield__placeholder-orange">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Authority: semantic meaning" src="https://img.shields.io/badge/authority-semantic__meaning-blueviolet">
  <img alt="Input: explicit" src="https://img.shields.io/badge/input-explicit-critical">
  <img alt="Hidden fetches: forbidden" src="https://img.shields.io/badge/hidden__fetches-forbidden-critical">
</p>

**Status:** draft / PROPOSED  
**Contract path:** `contracts/policy/policy_input_bundle.md`  
**Schema path:** `schemas/contracts/v1/policy/policy_input_bundle.schema.json`  
**Schema status:** PROPOSED / greenfield placeholder  
**Validator path named by schema:** `tools/validators/policy/validate_policy_input_bundle.py` — NEEDS VERIFICATION for implementation/wiring  
**Policy rule authority:** `policy/`, not this contract  
**Runtime helper authority:** `packages/policy-runtime/`, not this contract  
**Downstream decision contract:** `contracts/policy/policy_decision.md`  
**Truth posture:** CONFIRMED schema pairing · CONFIRMED placeholder schema surface · PROPOSED semantic field families and invariants until schema, validators, fixtures, policy bundles, tests, and runtime adapters are verified

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Schema-paired field surface](#schema-paired-field-surface) · [Proposed semantic input families](#proposed-semantic-input-families) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Validation expectations](#validation-expectations) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`PolicyInputBundle` is the governed input carrier for policy evaluation.

It answers:

- what operation is being evaluated;
- who or what audience/context is requesting the operation;
- which object, layer, dataset, claim, release candidate, API response, map render, AI answer, or export is being evaluated;
- what evidence, source-role, rights, sensitivity, lifecycle, release, and review state is available;
- which policy bundle/evaluator context should be used;
- what must be treated as missing or unresolved.

It does not answer:

- whether the policy gate allows the operation — that is `PolicyDecision`;
- whether raw evidence is true — that is EvidenceBundle / evidence resolution;
- whether a source is authoritative — that is SourceDescriptor/source registry posture;
- whether a release is approved — that is release governance;
- whether a public UI/API/AI response may render — that requires downstream governed envelopes and release/publication checks.

---

## Meaning

A `PolicyInputBundle` is a snapshot of policy-relevant context at a gate. It must be explicit, inspectable, hashable where practical, and safe to log or receipt according to sensitivity policy.

It is intentionally different from:

- `PolicyDecision` — output of policy evaluation;
- `DecisionEnvelope` — runtime transport wrapper;
- `EvidenceBundle` — evidence closure;
- `SourceDescriptor` — source identity and source-role authority;
- `ReleaseManifest` — release binding for published artifacts;
- UI/API request body — transport surface, not necessarily policy-ready;
- AI prompt/context — generated or assembled context cannot create policy authority.

A policy gate must not silently reach outside the bundle for missing facts unless that fetch is itself governed, logged, and represented in a new input bundle or receipt. Unknown context should fail closed.

---

## Schema-paired field surface

The paired schema is currently a greenfield placeholder.

| Field | Required | Schema-confirmed shape | Semantic role |
|---|---:|---|---|
| `id` | yes | string | Canonical identifier for this policy input bundle. |
| `spec_hash` | no | string | Deterministic content hash, if present. |
| `version` | no | string | Contract or object version, if present. |

Current schema also permits additional properties. That means the rich semantic fields below are **PROPOSED** and not yet machine-enforced by the schema.

> [!WARNING]
> Do not treat this contract as proof that the implementation accepts or validates the proposed fields. Schema, fixtures, validators, and policy-runtime adapters must be updated before callers rely on them.

---

## Proposed semantic input families

These field families are the recommended semantic target for the next schema/fixture pass.

| Field family | Purpose | Required posture |
|---|---|---|
| Identity | `id`, `spec_hash`, `version`, bundle type, canonicalization profile. | Deterministic identity where practical; no mutable latest pointers. |
| Operation context | requested operation such as `render`, `answer`, `export`, `promote`, `release`, `correct`, `rollback`, `join`, `query`, `download`. | Operation-specific decisions; no generic approval. |
| Audience context | public, restricted-review, steward, internal, partner, export, AI adapter, map runtime, release gate. | Audience must be explicit; unknown audience fails closed. |
| Object context | object refs, dataset/layer/claim/release refs, domain, lifecycle phase, release state. | Refs only; do not embed raw lifecycle data. |
| Evidence context | EvidenceRef list, EvidenceBundle refs, resolver status, citation validation status, evidence freshness. | Missing/unresolved evidence yields abstain/deny/hold/error according to gate. |
| Source context | SourceDescriptor refs, source role, source rights, cadence, caveats, active/deprecated status. | Source-role anti-collapse; source data is not embedded. |
| Rights context | license, terms, attribution, redistribution/export limits, embargo, rights uncertainty. | Unknown rights fail closed. |
| Sensitivity context | living-person, DNA/genomic, rare species, archaeology, infrastructure, precise location, tribal/cultural, private join flags. | Exact sensitive details must be referenced/redacted/generalized, not exposed. |
| Geometry/location context | precision, generalization state, redaction state, tile/layer/render target. | Map/render decisions must be precision-aware. |
| Review context | review state, steward assignment, review record refs, required separation of duties. | Review refs do not equal approval unless policy says so. |
| Release context | candidate id, release state, ReleaseManifest ref, rollback target, correction lineage, supersession state. | Publication remains release-gated. |
| Evaluator context | policy bundle id/hash/version, evaluator profile/version, timeout/fail-closed mode. | Missing or stale evaluator context yields error/hold/deny. |
| Prior decisions | prior PolicyDecision refs, supersession links, stale/degraded flags. | Prior decisions may inform but do not replace current evaluation. |

---

## Invariants

CONFIRMED by paired schema:

- `id` is required.
- `spec_hash` is optional and string-shaped if present.
- `version` is optional and string-shaped if present.
- Additional properties are currently allowed.

PROPOSED semantic invariants:

- All policy inputs must be explicit; no hidden fetches from source systems, RAW stores, UI state, operator memory, vector indexes, model prompts, or generated language.
- The bundle must identify the requested operation and audience before any policy decision is trusted.
- Source role, rights, sensitivity, evidence, lifecycle, and release context must be present or explicitly marked unresolved.
- Missing evidence, rights, source authority, sensitivity posture, release state, review state, policy bundle version, or evaluator integrity must fail closed.
- Raw sensitive values should not be embedded directly; use refs, redaction state, generalized geometry, or synthetic fixtures.
- A policy input bundle is immutable once evaluated; re-evaluation creates a new input bundle or new version/spec hash.
- `spec_hash`, when present, should be computed over canonical content and referenced by `PolicyDecision`, receipts, or logs.
- A bundle must not be treated as evidence, release approval, policy approval, or consent approval by itself.

---

## Lifecycle role

`PolicyInputBundle` may be assembled at any governed gate across the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Expected gate contexts:

- **Ingest / quarantine:** decide whether material can enter WORK or must remain QUARANTINE.
- **Processing:** decide whether source roles, rights, and sensitivity allow transformation.
- **Catalog/triplet projection:** decide whether evidence and policy support graph/catalog exposure.
- **Map/render/API:** decide whether public or restricted presentation is allowed.
- **Governed AI:** decide whether to answer, abstain, deny, or error.
- **Promotion/release:** decide whether release gates have enough evidence, rights, review, and rollback support.
- **Correction/rollback:** decide whether supersession, withdrawal, or rollback action is required.

A `PolicyInputBundle` supports policy evaluation, but does not itself move artifacts through lifecycle phases.

---

## Boundaries

| Boundary | Rule |
|---|---|
| Contract vs schema | This contract defines semantic meaning; schema defines machine shape. |
| Contract vs policy | This contract says what inputs mean; `policy/` decides admissibility. |
| Input vs decision | `PolicyInputBundle` is input; `PolicyDecision` is output. |
| Input vs evidence | Evidence refs and status may appear here; EvidenceBundle remains evidence authority. |
| Input vs source registry | Source refs and roles may appear here; source registry remains source authority. |
| Input vs release | Release refs may appear here; release gates decide publication. |
| Input vs runtime | Runtime wrappers may carry this object; they do not redefine it. |
| Input vs AI | AI context cannot substitute for explicit policy input fields. |

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- strengthen schema beyond placeholder `id` / `spec_hash` / `version` surface;
- decide whether proposed field families become first-class fields or nested typed records;
- validator existence and wiring for `tools/validators/policy/validate_policy_input_bundle.py`;
- fixtures under `fixtures/policy/policy_input_bundle/` or aligned `fixtures/contracts/v1/policy/policy_input_bundle/` home;
- tests for missing operation, missing audience, missing evidence, unknown rights, sensitive exact location, stale policy bundle, invalid release state, hidden-fetch attempt, and evaluator error;
- policy-runtime adapter behavior for fail-closed evaluation;
- mapping from `PolicyInputBundle` hash to `PolicyDecision` and receipt/proof references.

---

## Fixtures

Minimum fixture set PROPOSED:

| Fixture | Purpose |
|---|---|
| `valid_render_public_generalized.json` | Public map/render gate with generalized-safe location. |
| `valid_answer_with_evidence_refs.json` | Governed AI answer gate with resolvable evidence refs. |
| `valid_promote_candidate.json` | Promotion gate with release/review/rollback context. |
| `valid_restrict_sensitive_geometry.json` | Sensitive exact-location context that requires restrictions. |
| `invalid_missing_id.json` | Schema-required missing id. |
| `invalid_missing_operation_semantic.json` | Semantically invalid despite placeholder schema allowing extra fields. |
| `deny_unknown_rights.json` | Rights posture unknown; fail closed. |
| `abstain_missing_evidence.json` | Evidence unresolved; cite-or-abstain behavior. |
| `error_stale_policy_bundle.json` | Evaluator/bundle context stale or invalid. |
| `blocked_hidden_fetch_attempt.json` | Demonstrates no-hidden-fetch boundary. |

Fixtures for sensitive lanes must be synthetic, generalized, or redacted.

---

## Open questions

- What is the accepted canonical fixture home: `fixtures/policy/policy_input_bundle/` from the current schema, or `fixtures/contracts/v1/policy/policy_input_bundle/` for consistency with other contracts?
- Should the next schema make operation, audience, object context, evidence context, source context, rights context, sensitivity context, lifecycle context, release context, and evaluator context required?
- Should `PolicyInputBundle` include direct `EvidenceRef` arrays, only EvidenceBundle refs, or both?
- Should source role and rights posture be copied into the bundle or referenced by immutable source registry snapshots?
- Should `spec_hash` be required before any release-gate use?
- How should public-safe and steward-only sensitivity context be separated?

---

## Rollback

Rollback is required if this contract is used to justify hidden source fetches, raw sensitive data in policy inputs, AI-generated context as policy truth, policy approval without a `PolicyDecision`, or release/publication without governed gates.

Rollback target for this expansion: previous blob SHA `a0596152c0e6820a7403ffe72135ffe9258131c9`.

<p align="right"><a href="#top">Back to top</a></p>
