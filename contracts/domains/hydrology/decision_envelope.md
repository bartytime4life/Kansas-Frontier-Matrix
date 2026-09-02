<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-hydrology-decision-envelope
title: Decision Envelope Contract — Hydrology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; runtime-alias; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Governed API steward
  - OWNER_TBD — Runtime contract steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-22
updated: 2026-06-22
policy_label: public-with-gates; semantic-contract; hydrology; decision-envelope; runtime-alias; finite-outcomes; cite-or-abstain; release-gated; rollback-aware; not-for-life-safety
related:
  - ./README.md
  - ./domain_layer_descriptor.md
  - ./domain_observation.md
  - ./domain_validation_report.md
  - ./nfhl_zone.md
  - ./flow_observation.md
  - ./water_level_observation.md
  - ./water_quality_observation.md
  - ./aquifer_observation.md
  - ./hydrograph.md
  - ../../../contracts/runtime/decision_envelope.md
  - ../../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../../schemas/contracts/v1/domains/hydrology/decision_envelope.schema.json
  - ../../../docs/domains/hydrology/API_CONTRACTS.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hydrology/BOUNDARY.md
  - ../../../docs/domains/hydrology/CANONICAL_PATHS.md
  - ../../../policy/domains/hydrology/
  - ../../../fixtures/domains/hydrology/decision_envelope/
  - ../../../tests/domains/hydrology/test_decision_envelope.*
  - ../../../release/candidates/hydrology/
tags: [kfm, contracts, hydrology, decision-envelope, runtime-response, ANSWER, ABSTAIN, DENY, ERROR, finite-outcomes, source-role, policy-family, evidence-refs, not-for-life-safety, nfhl, governed-api, rollback]
notes:
  - "Expanded from a short alias scaffold at contracts/domains/hydrology/decision_envelope.md."
  - "The Hydrology schema is a domain-lane alias of the shared runtime decision_envelope schema via allOf/$ref and currently adds no Hydrology-specific fields."
  - "The shared runtime schema is PROPOSED but materially defines finite outcomes and required fields: decision_id, outcome, policy_family, reasons, obligations, and evaluated_at."
  - "Hydrology-specific constraints currently live as semantic obligations/policy expectations, not additional schema fields, because the alias schema uses unevaluatedProperties=false."
  - "HydrologyDecisionEnvelope must not be used to bypass governed APIs, EvidenceBundle resolution, release manifests, source-role rules, NFHL/regulatory boundaries, or the not-for-life-safety boundary."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Decision Envelope Contract — Hydrology

> Semantic contract for the Hydrology domain alias of the shared KFM runtime `decision_envelope`: the bounded response wrapper that lets Hydrology APIs return `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` without bypassing evidence, policy, release, source-role, sensitivity, or rollback gates.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: Hydrology" src="https://img.shields.io/badge/domain-Hydrology%20%5BDOM--HYD%5D-1f9eda">
  <img alt="Schema: runtime alias" src="https://img.shields.io/badge/schema-runtime__alias-blue">
  <img alt="Outcomes: finite" src="https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-informational">
  <img alt="Policy: cite-or-abstain" src="https://img.shields.io/badge/policy-cite--or--abstain-success">
  <img alt="Boundary: not life safety" src="https://img.shields.io/badge/boundary-not__life__safety-critical">
</p>

`contracts/domains/hydrology/decision_envelope.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Alias boundary](#alias-boundary) · [Outcome grammar](#outcome-grammar) · [Hydrology DENY register](#hydrology-deny-register) · [Obligations profile](#obligations-profile) · [Illustrative examples](#illustrative-examples) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Rollback](#rollback) · [Evidence basis](#evidence-basis) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / domain alias semantic contract  
> **Contract path:** `contracts/domains/hydrology/decision_envelope.md`  
> **Domain schema path:** `schemas/contracts/v1/domains/hydrology/decision_envelope.schema.json`  
> **Runtime schema path:** `schemas/contracts/v1/runtime/decision_envelope.schema.json`  
> **Schema posture:** the Hydrology schema is an `allOf` alias of the shared runtime schema and currently adds no domain-specific fields. Domain-specific constraints must therefore be carried through `policy_family`, `reason_code`, `reasons`, `obligations`, `evidence_refs`, policy, fixtures, and docs until a follow-up schema revision adds Hydrology-specific properties.

> [!CAUTION]
> `decision_envelope` is not the Hydrology answer itself, not an EvidenceBundle, not a ReleaseManifest, not a public layer, not source truth, not emergency flood guidance, and not a way to turn NFHL regulatory context into observed flooding.

---

## Meaning

The Hydrology `decision_envelope` is a domain-lane alias of the shared runtime decision envelope. It is the finite-outcome wrapper Hydrology uses when a governed API, Evidence Drawer, Focus Mode response, layer resolver, export request, or review-facing runtime surface needs to say one of four things:

- **`ANSWER`** — KFM can answer from released, evidence-backed, policy-allowed Hydrology material.
- **`ABSTAIN`** — KFM cannot support the requested claim with sufficient evidence, citation, temporal scope, or source-role clarity.
- **`DENY`** — KFM must refuse because policy, rights, sensitivity, release state, source-role anti-collapse, or life-safety boundaries block the response.
- **`ERROR`** — KFM could not evaluate due to malformed input, schema failure, missing dependencies, resolver failure, or runtime failure.

This contract profiles the shared runtime envelope for Hydrology. It does not add new fields in the current schema step.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Human-readable Hydrology alias semantics | `contracts/domains/hydrology/decision_envelope.md` | This file. Defines how the shared runtime envelope is used by Hydrology. |
| Shared runtime meaning | `contracts/runtime/decision_envelope.md` | Common decision-envelope contract family; currently brief/generic. |
| Shared runtime schema | `schemas/contracts/v1/runtime/decision_envelope.schema.json` | Defines finite fields and required runtime properties. |
| Hydrology alias schema | `schemas/contracts/v1/domains/hydrology/decision_envelope.schema.json` | `$ref` alias to runtime schema; adds no fields. |
| Hydrology API doctrine | `docs/domains/hydrology/API_CONTRACTS.md` | Defines proposed Hydrology governed surfaces, finite outcomes, deny rules, DTO families, and trust-membrane flow. |
| Hydrology contract root | `contracts/domains/hydrology/README.md` | Directory root and object-family boundary. |
| Policy | `policy/domains/hydrology/` | Expected source-role, sensitivity, release, and deny gates. |
| Fixtures/tests | `fixtures/domains/hydrology/decision_envelope/`, `tests/domains/hydrology/` | Expected positive/negative proof for `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`. |
| Release | `release/candidates/hydrology/` and release roots | ReleaseManifest, CorrectionNotice, RollbackCard, and release closure. |

---

## Schema posture

### Confirmed domain alias schema

The Hydrology domain schema currently states:

| Schema element | Current value |
|---|---|
| `$id` | `https://schemas.kfm.local/contracts/v1/domains/hydrology/decision_envelope.schema.json` |
| Description | Hydrology domain alias of common `decision_envelope` contract. |
| `contract_doc` | `contracts/domains/hydrology/decision_envelope.md` |
| `fixtures_root` | `fixtures/domains/hydrology/decision_envelope/` |
| `validator` | `tools/validators/domains/hydrology/validate_decision_envelope.py` |
| `policy` | `policy/domains/hydrology/` |
| `status` | `PROPOSED` |
| Shape | `allOf` `$ref` to shared runtime schema |
| Extra fields | `unevaluatedProperties: false` |

### Confirmed shared runtime schema fields

The shared runtime schema currently defines these properties:

| Field | Meaning in Hydrology profile |
|---|---|
| `decision_id` | Required stable runtime decision ID. |
| `id` | Optional/general identifier retained by common schema. |
| `outcome` | Required finite outcome: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. |
| `decision` | Optional alias-like finite outcome field; exact relationship to `outcome` NEEDS VERIFICATION. |
| `policy_family` | Required policy family: promotion, access, render, capability, consent, sensitivity. |
| `reason_code` | Optional compact reason string. |
| `reasons` | Required array of reason strings. |
| `obligations` | Required array of obligations. |
| `evidence_refs` | Optional EvidenceRef ID array. |
| `evaluated_at` | Required decision evaluation timestamp. |
| `spec_hash` | Optional normalized spec/hash support. |
| `version` | Optional object/schema version. |
| `issued_at` | Optional issuance timestamp. |

Required runtime fields are: `decision_id`, `outcome`, `policy_family`, `reasons`, `obligations`, and `evaluated_at`.

---

## Alias boundary

Because the Hydrology schema uses a `$ref` alias and `unevaluatedProperties: false`, the current schema step does **not** support additional Hydrology-specific top-level fields such as `feature_id`, `object_family`, `source_role`, `release_ref`, `rollback_ref`, or `not_for_life_safety` unless the shared runtime schema is changed or the domain alias schema is revised.

Hydrology-specific meaning must therefore be encoded in the current fields:

| Hydrology concern | Current carrier |
|---|---|
| NFHL/regulatory-as-observed denial | `outcome=DENY`, `policy_family=render` or `access`, `reason_code`, `reasons`, `obligations`. |
| Missing EvidenceBundle | `outcome=ABSTAIN` or `DENY`, `reason_code`, `evidence_refs` empty/missing, `obligations`. |
| Life-safety / flood-warning refusal | `outcome=DENY`, `policy_family=sensitivity` or `capability`, `reason_code`, `reasons`, `obligations`. |
| Release missing | `outcome=DENY`, `policy_family=promotion` or `render`, `reason_code`, `reasons`. |
| Private-property sensitive join | `outcome=DENY` or `ABSTAIN`, `policy_family=sensitivity`, `reasons`, `obligations`. |
| Citation failure | `outcome=ABSTAIN`, `reason_code`, `reasons`, `obligations`, `evidence_refs`. |
| Runtime failure | `outcome=ERROR`, `policy_family` selected by attempted evaluation surface, `reason_code`, `reasons`. |

> [!WARNING]
> Do not document Hydrology-specific top-level decision-envelope fields as implemented until the schema is expanded. Current Hydrology-specific requirements are semantic/policy obligations, not schema-enforced domain fields.

---

## Outcome grammar

| Outcome | Hydrology use | Required posture |
|---|---|---|
| `ANSWER` | Released Hydrology feature/detail, drawer, layer, or focus response can be answered from evidence-backed, policy-allowed, public-safe material. | EvidenceBundle resolved where consequential; release state valid; source role preserved; no sensitive/publication blockers. |
| `ABSTAIN` | Evidence is insufficient, citation validation fails, source role conflicts, temporal scope is insufficient, reach identity is ambiguous, or no released public-safe answer exists. | No substantive claim emitted; `reasons` and `obligations` explain what blocked the answer. |
| `DENY` | Policy, rights, sensitivity, release state, source-role collapse, direct RAW/WORK access, life-safety framing, or forbidden cross-lane use blocks the answer. | `reason_code` and `reasons` identify the denial; obligations may point to review, release, or official source. |
| `ERROR` | Request/schema/resolver/runtime failure prevents evaluation. | Finite error envelope; no fallback to raw source, uncited answer, or generic AI response. |

`HOLD`, `PASS`, and `FAIL` are gate/validator outcomes. They do not replace runtime envelope outcomes on Hydrology answer surfaces.

---

## Hydrology DENY register

These Hydrology conditions must not be answered as if they were valid claims:

| Denied behavior | Runtime outcome | Suggested `reason_code` |
|---|---|---|
| NFHL flood zone presented as observed flood extent. | `DENY` | `nfhl_regulatory_not_observed` |
| Hydrology response asks KFM to issue flood warning, evacuation advice, or life-safety instruction. | `DENY` | `hydrology_not_life_safety_authority` |
| Public client asks for RAW, WORK, QUARANTINE, or unreleased candidate content. | `DENY` | `trust_membrane_bypass_denied` |
| Layer requested without ReleaseManifest / active map release. | `DENY` | `release_manifest_required` |
| Focus Mode answer lacks valid citation/evidence closure. | `ABSTAIN` | `citation_validation_failed` |
| Infrastructure/private-property detail is joined without steward review. | `DENY` | `sensitive_join_requires_review` |
| Operational-warning content is treated as Hydrology evidence. | `DENY` | `operational_warning_owned_elsewhere` |
| Flood-context layer lacks EvidenceBundle closure or RollbackCard. | `DENY` | `release_closure_missing` |
| Modeled hydrograph treated as observed time series. | `DENY` | `modeled_not_observed` |
| Aggregate HUC/county summary treated as per-place observation. | `DENY` | `aggregate_not_per_place_truth` |

---

## Obligations profile

Hydrology uses the shared `obligations[]` field to make public-safe duties machine-visible. Suggested obligation strings are **PROPOSED** until policy/tests formalize them.

| Obligation | Use |
|---|---|
| `resolve_evidence_bundle` | Consequential Hydrology claims must resolve evidence. |
| `show_source_role` | Public UI/API must preserve observed/regulatory/modeled/aggregate/admin/candidate/synthetic distinction. |
| `show_nfhl_regulatory_caveat` | Required when NFHL/regulatory context is involved. |
| `show_not_life_safety_notice` | Required where a request could be mistaken for emergency warning/guidance. |
| `require_release_manifest` | Required before public layer/detail answer. |
| `require_rollback_target` | Required before public release. |
| `require_review_for_sensitive_join` | Required for infrastructure/private-property/well/sensitive joins. |
| `abstain_on_ambiguous_reach_identity` | Required when reach identity cannot be resolved. |
| `carry_provisional_status` | Required for provisional gauge/stage/quality readings. |
| `do_not_use_raw_or_work_paths` | Required for public surfaces. |

---

## Illustrative examples

> [!NOTE]
> These examples are illustrative. They use only fields present in the shared runtime schema. They are not substitute fixtures.

### NFHL-as-observed flood request denied

```jsonc
{
  "decision_id": "hydrology:decision:nfhl-observed-deny-example",
  "outcome": "DENY",
  "policy_family": "render",
  "reason_code": "nfhl_regulatory_not_observed",
  "reasons": [
    "NFHL is regulatory context and cannot be rendered as observed flood extent."
  ],
  "obligations": [
    "show_nfhl_regulatory_caveat",
    "preserve_source_role",
    "do_not_label_regulatory_as_observed"
  ],
  "evidence_refs": [],
  "evaluated_at": "2026-06-22T00:00:00Z",
  "version": "v0.2"
}
```

### Missing evidence abstain

```jsonc
{
  "decision_id": "hydrology:decision:missing-evidence-abstain-example",
  "outcome": "ABSTAIN",
  "policy_family": "access",
  "reason_code": "evidence_bundle_not_resolved",
  "reasons": [
    "The requested Hydrology claim cannot be answered because EvidenceRef did not resolve to a release-eligible EvidenceBundle."
  ],
  "obligations": [
    "resolve_evidence_bundle",
    "do_not_generate_uncited_answer"
  ],
  "evidence_refs": ["EVIDENCE_REF_TBD"],
  "evaluated_at": "2026-06-22T00:00:00Z",
  "version": "v0.2"
}
```

---

## Lifecycle

| Phase | Decision-envelope behavior |
|---|---|
| RAW | No public decision envelope should expose RAW source payloads. |
| WORK / QUARANTINE | Runtime may evaluate candidate state internally, but public answer should `DENY`, `ABSTAIN`, or withhold. |
| PROCESSED | Validated objects may be eligible for answer evaluation, but still require catalog/evidence/release closure for public `ANSWER`. |
| CATALOG / TRIPLET | Evidence and catalog/triplet projections may support drawer/focus context; runtime answer still depends on policy and release. |
| RELEASE CANDIDATE | Decision envelope must prove release state, evidence state, source role, policy family, reasons, obligations, and rollback posture before `ANSWER`. |
| PUBLISHED | Governed API may return `ANSWER` only from released/public-safe material. All other cases return `ABSTAIN`, `DENY`, or `ERROR`. |
| CORRECTED / SUPERSEDED | Envelopes must stop answering from withdrawn/superseded evidence and must surface correction/rollback obligations through reasons/obligations. |

---

## Validation

Before this alias contract is promoted beyond draft:

- [ ] Confirm `schemas/contracts/v1/domains/hydrology/decision_envelope.schema.json` still intentionally aliases the runtime schema without extra fields.
- [ ] Confirm `tools/validators/domains/hydrology/validate_decision_envelope.py` exists and validates the alias shape, or create it.
- [ ] Add fixtures for each runtime outcome: `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`.
- [ ] Add negative fixtures for NFHL-as-observed, life-safety instruction, RAW/WORK public request, unreleased layer, citation failure, sensitive private-property join, operational-warning-as-Hydrology-evidence, modeled-as-observed, and aggregate-as-per-place.
- [ ] Confirm policy can express Hydrology-specific denial through current fields without domain-specific top-level schema fields.
- [ ] Decide whether Hydrology needs a future schema extension with domain-specific fields such as `feature_ref`, `object_family`, `source_role`, `release_ref`, and `rollback_ref`.
- [ ] Confirm Focus Mode and Evidence Drawer distinguish `ABSTAIN` from `DENY` and do not silently substitute generic answers.
- [ ] Confirm public clients never read RAW, WORK, QUARANTINE, source endpoints, or unreleased candidates when an envelope denies or abstains.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence, source role, policy, release, sensitivity, and rollback resolve | `ANSWER` |
| Evidence, citation, identity, temporal scope, or released support is insufficient | `ABSTAIN` |
| Policy, rights, sensitivity, release state, role collapse, life-safety framing, or trust-membrane bypass blocks answer | `DENY` |
| Schema, validator, resolver, source read, policy lookup, or runtime evaluation fails | `ERROR` |

---

## Rollback

Rollback is required when the Hydrology decision envelope lets unsupported, unsafe, stale, unreleased, or role-collapsed claims cross the trust membrane.

Rollback triggers include runtime envelope returning `ANSWER` for NFHL-as-observed; emergency/life-safety instruction emitted; RAW/WORK/QUARANTINE content returned; layer answered without ReleaseManifest; Focus Mode answered without citation/evidence closure; sensitive infrastructure/private-property join exposed without review; operational warning content treated as Hydrology evidence; flood-context answer lacking EvidenceBundle or RollbackCard; modeled hydrograph answered as observed; aggregate rollup answered as per-place truth; `ABSTAIN`/`DENY` collapsed into success; or schema alias extended with extra fields without ADR/schema migration.

Rollback artifacts should include affected `decision_id`s, request refs if available, evidence refs, PolicyDecision refs, release refs, correction notices, rollback cards, invalidated layer descriptors, invalidated Focus Mode outputs, invalidated exports, public-cache/style invalidation instructions, and replacement fixtures/tests proving the denied path.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `contracts/domains/hydrology/decision_envelope.md` scaffold | CONFIRMED | Target existed and stated this was a Hydrology alias of common runtime decision envelope. | Thin scaffold only; did not describe Hydrology obligations. |
| `schemas/contracts/v1/domains/hydrology/decision_envelope.schema.json` | CONFIRMED | Domain alias schema, `$ref` to runtime schema, fixtures/validator/policy pointers, `unevaluatedProperties: false`. | Adds no Hydrology-specific fields. |
| `schemas/contracts/v1/runtime/decision_envelope.schema.json` | CONFIRMED | Runtime fields, finite outcomes, policy family enum, required fields, additionalProperties false. | Schema status remains PROPOSED; policy/runtime behavior still needs tests. |
| `contracts/runtime/decision_envelope.md` | CONFIRMED | Common runtime contract exists. | Current contract text is generic and thin. |
| `docs/domains/hydrology/API_CONTRACTS.md` | CONFIRMED | Governed API posture, finite outcome semantics, Hydrology surface matrix, deny rules, source-role constraints, validation expectations. | Routes/DTOs are repeatedly marked PROPOSED / NEEDS VERIFICATION. |
| `contracts/domains/hydrology/README.md` | CONFIRMED | Contract-root boundaries, object families, source-role rules, validation and rollback expectations. | Orientation doc, not schema enforcement. |
| `docs/domains/hydrology/SOURCE_ROLE_MATRIX.md` | CONFIRMED | Seven role vocabulary and anti-collapse rules. | Navigational matrix; machine authority depends on SourceDescriptor/EvidenceBundle/policy. |
| User-provided authoring role | CONFIRMED user instruction | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Should the Hydrology alias remain fieldless, or should PR 2b add domain-specific top-level fields? | NEEDS VERIFICATION | Schema steward + governed API steward review. |
| What is the exact relationship between common schema fields `outcome` and `decision`? | NEEDS VERIFICATION | Runtime schema/contract decision. |
| Which `policy_family` values map to Hydrology feature/detail, layer, drawer, focus, export, and correction surfaces? | NEEDS VERIFICATION | Policy/fixture review. |
| Are Hydrology obligations controlled strings, schema enum, or policy-generated free strings? | NEEDS VERIFICATION | Schema + policy ADR. |
| Where should `release_ref`, `rollback_ref`, `source_role`, and `object_family` live if not in this alias schema? | NEEDS VERIFICATION | Runtime envelope extension vs domain wrapper decision. |
| Which validator proves current Hydrology decision envelopes deny NFHL-as-observed and life-safety requests? | NEEDS VERIFICATION | Implement/check validator and negative fixtures. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Hydrology contract-root README.
- [`./domain_layer_descriptor.md`](./domain_layer_descriptor.md) — Hydrology layer descriptor contract, if present/expanded.
- [`./domain_observation.md`](./domain_observation.md) — Hydrology observation envelope contract, if present/expanded.
- [`./domain_validation_report.md`](./domain_validation_report.md) — Hydrology validation-report contract, if present/expanded.
- [`../../../contracts/runtime/decision_envelope.md`](../../../contracts/runtime/decision_envelope.md) — shared runtime decision-envelope contract.
- [`../../../schemas/contracts/v1/runtime/decision_envelope.schema.json`](../../../schemas/contracts/v1/runtime/decision_envelope.schema.json) — shared runtime decision-envelope schema.
- [`../../../schemas/contracts/v1/domains/hydrology/decision_envelope.schema.json`](../../../schemas/contracts/v1/domains/hydrology/decision_envelope.schema.json) — Hydrology alias schema.
- [`../../../docs/domains/hydrology/API_CONTRACTS.md`](../../../docs/domains/hydrology/API_CONTRACTS.md) — Hydrology governed API and finite-outcome doctrine.
- [`../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`](../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md) — source-role anti-collapse matrix.
- [`../../../docs/domains/hydrology/README.md`](../../../docs/domains/hydrology/README.md) — Hydrology domain landing page.

[Back to top](#top)
