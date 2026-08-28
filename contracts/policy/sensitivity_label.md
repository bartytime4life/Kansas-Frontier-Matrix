<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-policy-sensitivity-label
title: SensitivityLabel Semantic Contract
type: contract
version: v0.2
status: draft; PROPOSED; schema-paired; sensitivity-policy-aware; fail-closed
owners: OWNER_TBD — Policy steward · Sensitivity steward · Contracts steward · Schema steward · Evidence steward · Release steward · Docs steward
created: NEEDS VERIFICATION — contract existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; policy; sensitivity-label; finite-levels; fail-closed; redaction-aware; generalization-aware; release-gated; no-sensitive-values
related:
  - ./README.md
  - ./policy_input_bundle.md
  - ./policy_decision.md
  - ../evidence/evidence_bundle.md
  - ../../schemas/contracts/v1/policy/sensitivity_label.schema.json
  - ../../policy/sensitivity/
  - ../../policy/domains/
  - ../../policy/release/
  - ../../packages/policy-runtime/README.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../docs/standards/MAP_TRUST_STATES.md
  - ../../fixtures/contracts/v1/policy/sensitivity_label/
  - ../../tests/contracts/policy/
tags: [kfm, contracts, policy, sensitivity-label, public, generalized, restricted, quarantine, redaction, generalization, fail-closed, evidence-bundle, policy-decision, release-gated, no-sensitive-values]
notes:
  - "Expanded from existing stub at `contracts/policy/sensitivity_label.md`."
  - "Paired schema verified at `schemas/contracts/v1/policy/sensitivity_label.schema.json`; schema status is PROPOSED."
  - "This contract defines semantic meaning only. It does not author executable sensitivity rules, define JSON Schema shape, store sensitive values, issue receipts, publish artifacts, or override release gates."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SensitivityLabel

> `SensitivityLabel` records the governed exposure posture attached to an object, claim, feature, layer, artifact, request, or release candidate. It states whether the material is `public`, `generalized`, `restricted`, or `quarantine`, why the label was applied, and when it was applied. It does **not** store the sensitive fact itself, decide policy by itself, or authorize publication.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Object: SensitivityLabel" src="https://img.shields.io/badge/object-SensitivityLabel-0a7ea4">
  <img alt="Levels: finite" src="https://img.shields.io/badge/levels-finite-critical">
  <img alt="Policy: fail closed" src="https://img.shields.io/badge/policy-fail__closed-critical">
  <img alt="Sensitive values: not stored" src="https://img.shields.io/badge/sensitive__values-not__stored-critical">
</p>

**Status:** draft / PROPOSED  
**Contract path:** `contracts/policy/sensitivity_label.md`  
**Schema path:** `schemas/contracts/v1/policy/sensitivity_label.schema.json`  
**Schema status:** PROPOSED  
**Validator path named by schema:** `tools/validators/validate_sensitivity_label.py` — NEEDS VERIFICATION for implementation/wiring  
**Policy rule authority:** `policy/sensitivity/`, `policy/domains/`, and release/access policy roots, not this contract  
**Downstream policy contract:** `contracts/policy/policy_decision.md`  
**Truth posture:** CONFIRMED schema pairing and finite field surface · PROPOSED semantic invariants beyond current schema · NEEDS VERIFICATION for validators, fixtures, policy bundles, runtime adapters, receipts, and CI enforcement

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Schema-paired field surface](#schema-paired-field-surface) · [Field semantics](#field-semantics) · [Level semantics](#level-semantics) · [Sensitivity families](#sensitivity-families) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Validation expectations](#validation-expectations) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`SensitivityLabel` is the semantic label that makes exposure posture explicit before a governed operation proceeds.

It answers:

- what exposure level is attached;
- why that label was applied;
- when the label was applied;
- whether downstream policy must restrict, generalize, quarantine, deny, hold, or allow a surface.

It does not answer:

- whether a user or client may view the material — that is policy/access evaluation;
- whether exact sensitive content may be published — that requires policy, review, release, correction, and rollback support;
- what the sensitive value is — sensitive values must remain in governed data/evidence homes, not in the label string;
- whether evidence is true — that is EvidenceBundle / evidence resolution;
- whether a release is approved — that is release governance.

---

## Meaning

A `SensitivityLabel` is a finite, audit-friendly exposure marker. It is designed to travel with governed objects, manifests, layer payloads, PolicyInputBundle context, PolicyDecision outcomes, release candidates, evidence refs, public API envelopes, map render envelopes, and AI answer envelopes.

It should be used to preserve the distinction between:

- material safe for public display;
- material safe only after generalization/redaction;
- material requiring restricted review or constrained access;
- material that must remain quarantined until rights, sensitivity, evidence, review, or release gates resolve.

A sensitivity label is not a policy decision by itself. It supplies policy-relevant context; policy rules decide what to do with it.

---

## Schema-paired field surface

The paired schema currently defines these fields as required and disallows additional properties.

| Field | Required | Schema-confirmed shape | Semantic role |
|---|---:|---|---|
| `level` | yes | enum: `public`, `generalized`, `restricted`, `quarantine` | Finite exposure posture. |
| `reason` | yes | string | Safe reason code or explanation for the label. |
| `applied_at` | yes | string, `date-time` | Time the label was applied. |

> [!NOTE]
> This contract may recommend domain-specific semantics that are not yet schema-enforced. Those recommendations are PROPOSED until paired validators, policy rules, fixtures, and tests prove them.

---

## Field semantics

### `level`

Finite exposure posture.

Valid schema-confirmed values:

- `public`
- `generalized`
- `restricted`
- `quarantine`

The label should describe the material's exposure posture, not a user's access grant. Access is decided by policy using this label plus audience, operation, rights, evidence, lifecycle, release, and review context.

### `reason`

Safe reason code or explanation for the label.

Requirements:

- should be stable enough for policy decisions, receipts, review dashboards, release manifests, and correction workflows;
- must not embed sensitive coordinates, living-person identifiers, DNA kit/vendor IDs, private residence details, sacred-site identifiers, rare-species exact locations, infrastructure vulnerabilities, or private source content;
- may be a public-safe code like `rare_species_exact_location`, `living_person_residence`, `dna_genomic_material`, `archaeology_site_precision`, `rights_unclear`, `source_terms_limit_publication`, or `release_not_reviewed`.

### `applied_at`

Time the label was applied.

Semantics:

- used for freshness, audit, supersession, and rollback;
- should use UTC RFC 3339 / JSON Schema `date-time` compatible form;
- should not be rewritten to make stale labels appear current;
- supersession should issue a new label event or attach an explicit replacement path rather than mutating historical meaning without receipt.

---

## Level semantics

| Level | Meaning | Typical downstream posture |
|---|---|---|
| `public` | No known policy-sensitive restriction for the evaluated operation and audience. | May proceed only if evidence, rights, lifecycle, release, and runtime gates also pass. |
| `generalized` | Exact values are unsafe, but generalized/redacted representation may be allowed. | Generalize geometry, redact fields, reduce precision, delay, or aggregate. |
| `restricted` | Access requires restricted-review, steward, partner, consent, or special-purpose context. | Block public display; route through controlled access and audit. |
| `quarantine` | Material is not safe for normal processing or release until unresolved issues are cleared. | Keep out of public clients and release paths; require review/remediation. |

> [!WARNING]
> `public` is not publication approval. It is only the sensitivity label. Public release still requires evidence, rights, source authority, validation, policy, review, release, correction, and rollback support.

---

## Sensitivity families

Sensitivity policies are domain- and operation-specific. The following families commonly require deny-by-default, generalization, restricted review, or quarantine:

| Sensitivity family | Typical label posture | Contract note |
|---|---|---|
| Living-person data | `restricted` or `quarantine`; sometimes `generalized` | Do not expose private residence, identity-link, personal contact, or sensitive relationship detail without governance. |
| DNA / genomic material | `restricted` or `quarantine` | Never place raw kit/vendor IDs, segments, genotypes, or private match details in public labels. |
| Rare/protected species exact locations | `generalized`, `restricted`, or `quarantine` | Exact geometry usually requires generalization or withholding. |
| Archaeology, burial, sacred, or culturally sensitive sites | `restricted` or `quarantine` | Exact location and site identity require special review and sovereignty/cultural sensitivity handling. |
| Critical infrastructure or security-relevant detail | `generalized`, `restricted`, or `quarantine` | Remove exploit-enabling precision before public release. |
| Private person-to-place or person-to-parcel joins | `restricted` or `quarantine` | Public map joins can expose people even when individual datasets are public. |
| Rights/license/terms uncertainty | `restricted` or `quarantine` | Unknown rights should not be converted into public release. |
| Release or review incompleteness | `restricted` or `quarantine` | Missing review/release/rollback support blocks publication. |

---

## Invariants

CONFIRMED by paired schema:

- `level` is required and must be one of `public | generalized | restricted | quarantine`.
- `reason` is required and string-shaped.
- `applied_at` is required and must be a `date-time` string.
- No additional properties are allowed by the current schema.

PROPOSED semantic invariants:

- Sensitive exact values must not be embedded in `reason`.
- `public` must not be treated as release approval.
- `generalized` must carry or imply an enforceable downstream generalization/redaction obligation in a PolicyDecision or release/render envelope.
- `restricted` must not be rendered to public clients without a policy decision and controlled-access context.
- `quarantine` must keep material out of normal public and release paths until review/remediation produces a superseding posture.
- Missing, stale, contradictory, or unreviewed sensitivity context should fail closed.
- Supersession should preserve the previous label for audit and rollback.

---

## Lifecycle role

Sensitivity labels may be created, reviewed, superseded, and enforced across the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Expected uses:

- **RAW / WORK:** attach initial suspected sensitivity and quarantine uncertain content.
- **QUARANTINE:** hold sensitive, rights-uncertain, or review-incomplete content.
- **PROCESSED:** confirm whether redaction/generalization is sufficient.
- **CATALOG / TRIPLET:** prevent sensitive exact values from entering public discovery or graph projections.
- **PUBLISHED:** ensure only released, policy-safe, reviewed, and rollback-ready representations are exposed.
- **Correction / rollback:** supersede labels when sensitivity, rights, or review state changes.

---

## Boundaries

| Boundary | Rule |
|---|---|
| Contract vs schema | This contract defines meaning; schema defines machine shape. |
| Contract vs policy | This label supplies policy context; policy decides admissibility. |
| Label vs decision | `SensitivityLabel` is input/context; `PolicyDecision` is the evaluated result. |
| Label vs evidence | EvidenceBundle remains evidence authority. |
| Label vs source registry | Source rights/caveats remain source-registry authority. |
| Label vs release | Release gates decide publication; labels do not publish. |
| Label vs data | Sensitive values live in governed data/evidence homes, not in label text. |
| Label vs AI | AI may explain labels with citations; it cannot create sensitivity truth without governed support. |

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- schema validation command for `schemas/contracts/v1/policy/sensitivity_label.schema.json`;
- validator existence and wiring for `tools/validators/validate_sensitivity_label.py`;
- fixtures under `fixtures/contracts/v1/policy/sensitivity_label/`;
- tests for each finite level;
- tests that `reason` does not contain exact sensitive payloads where policy can detect them;
- policy-runtime mapping from label level to obligations and PolicyDecision outcomes;
- release/render checks that prevent `public` label from bypassing release gates;
- correction/rollback handling for superseded labels.

---

## Fixtures

Minimum fixture set PROPOSED:

| Fixture | Purpose |
|---|---|
| `valid_public.json` | Public-safe label that still requires release gates. |
| `valid_generalized_rare_species.json` | Generalized posture for exact protected-species location. |
| `valid_restricted_living_person.json` | Restricted posture for living-person data. |
| `valid_quarantine_rights_unclear.json` | Quarantine posture for unresolved rights. |
| `invalid_unknown_level.json` | Confirms finite enum. |
| `invalid_missing_reason.json` | Confirms required reason. |
| `invalid_missing_applied_at.json` | Confirms required timestamp. |
| `invalid_extra_property.json` | Confirms `additionalProperties: false`. |
| `blocked_sensitive_reason_payload.json` | Demonstrates policy/validator rejection of raw sensitive content in reason. |
| `valid_superseded_label_pair.json` | Demonstrates audit-safe label supersession. |

Fixtures involving sensitive topics must use synthetic, generalized, or redacted values only.

---

## Open questions

- Should `reason` become a typed reason-code enum or structured object in the next schema version?
- Should the schema add `label_id`, `object_ref`, `applied_by`, `supersedes`, `review_ref`, `policy_decision_ref`, and `redaction_profile_ref`?
- Should `public` be renamed or split to avoid being mistaken for release approval?
- Should generalized posture require a companion geometry/redaction transform receipt?
- Which validator or policy rule will detect sensitive payload leakage inside `reason`?

---

## Rollback

Rollback is required if this contract is used to store sensitive values, bypass policy/release gates, treat `public` as publication approval, expose restricted/quarantine material to public clients, or treat AI-generated sensitivity judgments as authority.

Rollback target for this expansion: previous blob SHA `11e30f6f4de8310a41288cc1eb3fc8016a8aab38`.

<p align="right"><a href="#top">Back to top</a></p>
