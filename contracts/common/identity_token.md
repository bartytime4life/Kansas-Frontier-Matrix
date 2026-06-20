<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/identity-token
title: contracts/common/identity_token.md — IdentityToken Contract
type: contract
version: v0.2
status: draft
owners: OWNER_TBD — Contract steward · Schema steward · Runtime steward · Source steward · Evidence steward · Governance steward · Docs steward
created: 2026-06-20
updated: 2026-06-20
policy_label: public; contracts; common; identity-token; semantic-contract; shared-kernel
related:
  - ./README.md
  - ../../schemas/contracts/v1/common/identity_token.schema.json
  - ../../fixtures/contracts/v1/common/identity_token/
  - ../../tools/validators/validate_identity_token.py
  - ../../policy/common/
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../release/
tags: [kfm, contracts, common, identity-token, identity, shared-kernel, run, source, decision, review, bundle, actor, provenance, governance]
notes:
  - "Expanded from scaffold into a semantic contract for the common identity_token object."
  - "Machine-checkable shape is in schemas/contracts/v1/common/identity_token.schema.json."
  - "Schema metadata points to fixtures/contracts/v1/common/identity_token/, tools/validators/validate_identity_token.py, and policy/common/, but validator/policy/fixture existence and behavior remain NEEDS VERIFICATION unless separately inspected."
  - "identity_token is a reference/identity carrier, not an authorization credential, security token, secret, login token, or proof of identity by itself."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# IdentityToken Contract

> Semantic contract for `identity_token`, a small common identity carrier used to reference governed KFM things such as runs, sources, decisions, reviews, evidence bundles, and actors without copying their full records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Family: common" src="https://img.shields.io/badge/family-common-blue">
  <img alt="Schema: proposed" src="https://img.shields.io/badge/schema-PROPOSED-orange">
  <img alt="Authority: semantic" src="https://img.shields.io/badge/authority-semantic__contract-green">
</p>

`contracts/common/identity_token.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Schema pairing](#schema-pairing) · [Fields](#fields) · [Invariants](#invariants) · [Allowed kinds](#allowed-kinds) · [Non-goals](#non-goals) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Owner:** `OWNER_TBD`  
> **Contract path:** `contracts/common/identity_token.md`  
> **Schema path:** `schemas/contracts/v1/common/identity_token.schema.json`  
> **Truth posture:** `CONFIRMED` contract path, schema path, schema shape, and current update; validator, fixtures, policy behavior, runtime integration, and downstream references remain `NEEDS VERIFICATION`.

---

## Meaning

`identity_token` is a compact, typed identity reference for a governed KFM entity.

It answers four questions:

1. **What is being referenced?** — `id`.
2. **What kind of thing is it?** — `kind`.
3. **When was this token issued?** — `issued_at`.
4. **Who or what issued the token?** — `issuer`, when known.

An `identity_token` is useful when a contract, receipt, decision, review, evidence bundle, or runtime envelope needs to point at a governed thing without embedding that thing's complete record.

It is a shared-kernel value object. It must stay small, stable, and semantically narrow.

---

## Schema pairing

The paired schema is:

```text
schemas/contracts/v1/common/identity_token.schema.json
```

The schema defines machine shape. This Markdown contract defines meaning.

The current schema metadata identifies:

| Schema metadata | Value | Verification posture |
|---|---|---|
| `$id` | `https://schemas.kfm.local/contracts/v1/common/identity_token.schema.json` | `CONFIRMED` from schema. |
| `contract_doc` | `contracts/common/identity_token.md` | `CONFIRMED` from schema. |
| `fixtures_root` | `fixtures/contracts/v1/common/identity_token/` | `NEEDS VERIFICATION` existence/coverage. |
| `validator` | `tools/validators/validate_identity_token.py` | `NEEDS VERIFICATION`; not proven present in this edit. |
| `policy` | `policy/common/` | `NEEDS VERIFICATION` existence/behavior. |
| `status` | `PROPOSED` | `CONFIRMED` from schema metadata. |

---

## Fields

| Field | Required by schema | Semantic meaning | Notes |
|---|---:|---|---|
| `id` | Yes | Identifier of the referenced governed thing. | The referenced record must be resolved by the caller's owning context. This field alone does not prove existence. |
| `kind` | Yes | Closed classification of the referenced thing. | Current enum: `run`, `source`, `decision`, `review`, `bundle`, `actor`. |
| `issued_at` | Yes | Date-time when this token was issued. | This is token issuance time, not necessarily source observation time, evidence creation time, review time, or release time. |
| `issuer` | No | Component, actor, steward, service, or process that issued the token. | Optional in current schema; downstream policy may require it for some uses. |

---

## Invariants

An `identity_token` must preserve these invariants:

- `id` must identify exactly one referenced thing in the resolver context that consumes it.
- `kind` must remain a closed enum value until a schema version explicitly changes it.
- `issued_at` must be a valid date-time and must represent token issuance time.
- `issuer`, when present, must identify the token issuer, not necessarily the referenced entity's owner.
- The token must not carry secret material, credentials, personal identifiers beyond the referenced `actor` semantics, or embedded source/evidence payloads.
- The token must not replace SourceDescriptor, EvidenceBundle, ReviewRecord, PolicyDecision, ReleaseManifest, AIReceipt, or any other full governed object.
- Consumers must not treat a syntactically valid token as proof that the referenced object exists, is current, is released, or is policy-allowed.

---

## Allowed kinds

| `kind` | Meaning | Correct resolution surface |
|---|---|---|
| `run` | References a run, job, pipeline execution, model invocation, or comparable runtime event. | Runtime/run receipt surfaces. |
| `source` | References a source identity or admitted source object. | SourceDescriptor/source registry surfaces. |
| `decision` | References a policy, promotion, release, correction, or other decision object. | Policy/release/governance decision surfaces. |
| `review` | References a review record or review workflow artifact. | Governance/review surfaces. |
| `bundle` | References an evidence bundle or proof-supporting bundle. | Evidence/proof surfaces. |
| `actor` | References an actor identity in a governed context. | Actor/identity/governance surfaces; must not become an authentication credential. |

---

## Non-goals

`identity_token` is not:

- an authentication token;
- an authorization grant;
- a session token;
- a password, API key, JWT, bearer token, or secret;
- proof that a referenced object exists;
- proof that evidence is valid;
- proof that policy allowed an action;
- a release manifest;
- a substitute for a full governed object;
- a public identifier suitable for all audiences by default.

If a workflow needs security credentials, access-control tokens, signed authorization, consent tokens, or identity-provider integration, it must use a separate security/consent contract and policy surface.

---

## Lifecycle

```mermaid
flowchart LR
  CREATE[Issuer creates identity_token] --> VALIDATE[Schema validation]
  VALIDATE --> RESOLVE[Consumer resolves id + kind]
  RESOLVE --> POLICY[Policy / review / release gate as needed]
  POLICY --> USE[Use as reference]
  USE --> RECEIPT[Receipt / audit trail]
```

Lifecycle notes:

- A token may be created during RAW/WORK processing, runtime execution, review, evidence bundling, or release workflows.
- Schema validation proves only shape.
- Resolution proves only that a referenced object can be found in the relevant context.
- Policy/review/release gates decide whether the reference may be used for a specific purpose.
- Supersession of the referenced object does not automatically update prior tokens; receipts and downstream objects must record their own correction/rollback posture.

---

## Validation

Before relying on this contract, verify:

- schema validation passes against `schemas/contracts/v1/common/identity_token.schema.json`;
- `kind` remains a closed enum or versioned change is documented;
- validators exist and cover valid, invalid, missing-field, invalid-date-time, unknown-kind, extra-field, and optional-issuer cases;
- fixtures exist under the schema-declared fixture root;
- policy behavior, if any, is in `policy/common/` or a more specific policy root;
- every consumer resolves `id + kind` through the correct owning surface;
- no consumer treats `identity_token` as an authentication or authorization credential;
- release/public-display contexts check sensitivity, rights, audience, and release state before exposing tokens.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| Prior `contracts/common/identity_token.md` scaffold | `CONFIRMED` | Contract existed and referenced the schema URL, lifecycle, and open verification note. | Scaffold delegated field meaning to schema and lacked semantic boundaries. |
| `schemas/contracts/v1/common/identity_token.schema.json` | `CONFIRMED` | Current field set, required fields, allowed `kind` enum values, no additional properties, x-kfm metadata. | Schema metadata points to validator/fixtures/policy, but their behavior is not proven by schema alone. |
| `contracts/common/README.md` | `CONFIRMED` | Common contracts may define small cross-cutting value objects only when no single domain owns them; common must stay narrow. | Does not prove individual common contract inventory. |
| `docs/architecture/contract-schema-policy-split.md` | `CONFIRMED` | Contracts define meaning; schemas define shape; policy decides admissibility; tests/fixtures prove enforceability. | Path presence and runtime behavior remain verification-bound. |

---

## Rollback

Rollback is required if this contract is used as an authentication/authorization credential, if it substitutes for the referenced governed object, or if it is used to bypass evidence, policy, review, release, or resolver checks.

Rollback target: prior scaffold content SHA `d1cbf05d6d0422aa1fd0048a1b977a39fa1ec8d1`.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Validator existence and behavior are verified.
- [ ] Fixtures exist and cover valid/invalid/denied/abstain cases where applicable.
- [ ] Policy behavior is either linked or explicitly marked not applicable.
- [ ] Consumer contracts document how `id + kind` resolves for each use case.
- [ ] Security review confirms this is not used as a credential or authorization grant.
- [ ] Public-release review confirms exposure rules for tokens in public envelopes.
- [ ] Any enum expansion is versioned and migration-tested.

---

## Status summary

`identity_token` is a common semantic value object for typed references to governed KFM things. It is not the governed thing itself, not proof of existence, not proof of evidence, not proof of policy allowance, not a release artifact, and not a security credential.

<p align="right"><a href="#top">Back to top</a></p>
