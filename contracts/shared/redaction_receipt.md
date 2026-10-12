<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-shared-redaction-receipt
title: contracts/shared/redaction_receipt.md — Shared RedactionReceipt Contract
type: contract
version: v0.2
status: draft; PROPOSED; shared-semantics; receipt-schema-home-open; sensitivity-aware; release-gated
owners: OWNER_TBD — Redaction steward · Sensitivity steward · Receipt steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Release steward · Docs steward
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-06-24
policy_label: restricted; contracts; shared; redaction-receipt; receipt; sensitivity; geoprivacy; rights; public-safe-transform; audit-required; no-release-authority
tags: [kfm, contracts, shared, redaction-receipt, receipt, redaction, generalization, suppression, withholding, masking, geoprivacy, sensitivity, rights, policy, review, release, correction, rollback]
related:
  - ./README.md
  - ../domains/flora/redaction_receipt.md
  - ../domains/fauna/redaction_receipt.md
  - ../../schemas/contracts/v1/receipts/redaction_receipt.schema.json
  - ../../policy/redaction/
  - ../../policy/runtime/
  - ../../policy/release/
  - ../../docs/atlases/receipt-catalog.md
  - ../../docs/standards/REDACTION_DETERMINISM.md
  - ../../docs/architecture/contract-schema-policy-split.md
notes:
  - "Expanded from a planned-path scaffold created from `docs/domains/flora/CONTINUITY_INVENTORY.md`."
  - "Existing domain-specific redaction receipt contracts were verified for Flora and Fauna; this shared file defines cross-domain common semantics and must not erase domain-specific constraints."
  - "A proposed receipts schema scaffold exists at `schemas/contracts/v1/receipts/redaction_receipt.schema.json`, but it has no properties and `contract_doc: null`; schema home and field enforcement remain NEEDS VERIFICATION."
  - "Receipt catalog doctrine identifies RedactionReceipt as the receipt that records public-safe transformation for sensitivity, rights, or policy."
  - "RedactionReceipt records a protective transform. It is not redaction policy, not a redaction recipe that reveals sensitive parameters, not EvidenceBundle, not PolicyDecision, not ReviewRecord, not ReleaseManifest, and not publication approval."
  - "Rollback target for this expansion is previous scaffold blob SHA `1aa1cde98e36e257ed3d6adccb90eba7d86fdbe6`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Shared RedactionReceipt Contract

> `RedactionReceipt` is the cross-domain semantic receipt for a public-safe protective transform: content was removed, masked, fuzzed, generalized, aggregated, delayed, withheld, suppressed, clipped, simplified, or otherwise transformed because sensitivity, rights, source-role, consent, policy, or re-identification risk required it. It proves the transform was recorded; it does not prove the transform was sufficient or authorize publication.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts/shared" src="https://img.shields.io/badge/root-contracts%2Fshared-blue">
  <img alt="Object: RedactionReceipt" src="https://img.shields.io/badge/object-RedactionReceipt-blueviolet">
  <img alt="Receipt: audit" src="https://img.shields.io/badge/receipt-audit-0a7ea4">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold-orange">
  <img alt="Boundary: not release approval" src="https://img.shields.io/badge/boundary-not__release__approval-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/shared/redaction_receipt.md`  
**Shared-lane status:** proposed cross-domain semantic anchor  
**Proposed schema scaffold:** `schemas/contracts/v1/receipts/redaction_receipt.schema.json`  
**Schema posture:** PROPOSED scaffold; no declared fields; `contract_doc: null`; schema home open  
**Domain-specific contracts:** `contracts/domains/flora/redaction_receipt.md`, `contracts/domains/fauna/redaction_receipt.md`  
**Policy authority:** `policy/redaction/`, sensitivity policy, domain policy, and release policy roots — not this contract  
**Truth posture:** CONFIRMED target scaffold replaced · CONFIRMED Flora and Fauna redaction receipt contracts exist · CONFIRMED receipt catalog lists RedactionReceipt as a receipt class · CONFIRMED receipts are process memory and not sovereign truth · CONFIRMED proposed receipts schema scaffold exists but has no fields and no contract_doc · NEEDS VERIFICATION for schema home, field shape, validators, fixtures, policy runtime behavior, review workflow, release workflow, persistence, signatures, and public API/UI behavior

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Shared vs domain-specific contracts](#shared-vs-domain-specific-contracts) · [Schema posture](#schema-posture) · [Recommended field families](#recommended-field-families) · [Transform classes](#transform-classes) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Validation expectations](#validation-expectations) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`RedactionReceipt` records a governed protective transform across KFM domains.

It answers:

- what target object, field, geometry, attribute, layer, export, claim, or response was transformed;
- which transform class was applied;
- why the transform was required;
- which policy decision, sensitivity rule, review record, source descriptor, evidence bundle, or release candidate supported the transform;
- which restricted input remained protected;
- which public-safe derivative was produced, if any;
- which validation, correction, withdrawal, and rollback surfaces remain linked.

It does not answer:

- whether publication is approved;
- whether the transform was policy-admissible by itself;
- whether the transform is sufficient without review/validation;
- whether the redacted derivative is canonical exact truth;
- how to reverse the transform;
- the unredacted sensitive value;
- the full hidden transform parameters when those parameters would enable re-identification.

---

## Meaning

A redaction receipt is a receipt for a protective transform. It makes redaction inspectable without leaking what redaction was designed to protect.

A mature governed redaction flow should look like:

```text
restricted or policy-significant source object
  -> sensitivity / rights / source-role / consent / policy evaluation
  -> selected redaction profile or withholding action
  -> transform execution
  -> validation / review
  -> RedactionReceipt
  -> public-safe derivative candidate
  -> release decision / correction / rollback as applicable
```

The receipt is a trust artifact. It records that a transform happened under a declared policy/review context. It does not itself perform policy evaluation, validate the transform, or release the result.

---

## Shared vs domain-specific contracts

This shared contract defines common semantics across domains. Domain-specific redaction receipts may add constraints for their sensitivity model.

| Contract | Role | Boundary |
|---|---|---|
| `contracts/shared/redaction_receipt.md` | Cross-domain common meaning. | Does not erase Flora/Fauna/domain-specific rules. |
| `contracts/domains/flora/redaction_receipt.md` | Flora-specific geoprivacy and rare-plant transform semantics. | Does not become global receipt authority. |
| `contracts/domains/fauna/redaction_receipt.md` | Fauna-specific sensitive occurrence/site/range transform semantics. | Placement is conflicted/open in repo evidence. |
| `schemas/contracts/v1/receipts/redaction_receipt.schema.json` | Proposed receipt schema scaffold. | No fields yet; not enforcement proof. |
| `policy/redaction/` and sensitivity/domain policy roots | Decides admissibility and profile selection. | Receipt records result/application only. |

If domain-specific rules conflict with this shared contract, treat the conflict as NEEDS VERIFICATION and route through steward/ADR review. Do not silently collapse the domain-specific contract into this shared file.

---

## Schema posture

The proposed schema scaffold currently exists at:

```text
schemas/contracts/v1/receipts/redaction_receipt.schema.json
```

Current verified posture:

| Schema fact | Current evidence |
|---|---|
| Schema title | `Redaction Receipt` |
| Declared properties | none yet |
| Required fields | none declared |
| Additional properties | `true` |
| Status | `PROPOSED` |
| Contract document | `null` |
| Source docs | fauna API/data lifecycle docs |

Because the schema is empty and permissive, this shared contract defines semantic expectations only. Machine enforcement, fixture coverage, validator wiring, signing, persistence, and API behavior remain NEEDS VERIFICATION.

---

## Recommended field families

Future schema or fixtures should consider these field families. They are PROPOSED until schema/ADR review accepts them.

| Field family | Purpose |
|---|---|
| Receipt identity | Stable `receipt_id`, version, issued time, emitter/steward/tool identity. |
| Target identity | Ref to source object, field, geometry, layer, claim, or response being transformed. |
| Input digest/ref | Hash/ref of restricted input without leaking sensitive payload. |
| Output digest/ref | Hash/ref of public-safe derivative, if one exists. |
| Transform class | Redaction/generalization/suppression/withholding/aggregation/masking/etc. |
| Transform profile | Named versioned profile or policy-selected method. |
| Policy basis | PolicyDecision/ref, sensitivity tier, rights/consent/source-role posture. |
| Review basis | ReviewRecord/ref or steward approval where required. |
| Evidence basis | EvidenceBundle/EvidenceRef refs supporting the public-safe derivative. |
| Validation basis | ValidationReport/ref proving schema/policy/transform checks ran. |
| Release basis | ReleaseManifest/candidate refs, when publication occurs. |
| Correction/rollback | CorrectionNotice, WithdrawalNotice, RollbackCard, invalidation refs. |
| Non-disclosure guard | Flag or note that hidden parameters are withheld when reversal/re-identification risk exists. |

---

## Transform classes

A `RedactionReceipt` may record one or more protective transform classes:

| Class | Meaning |
|---|---|
| `remove` | Field/content removed from public derivative. |
| `mask` | Value replaced with safe placeholder or category. |
| `fuzz` | Value/geometry displaced under deterministic or policy-approved method. |
| `generalize` | Precision reduced, such as coordinate rounding or taxonomic/geographic roll-up. |
| `aggregate` | Multiple records grouped into a public-safe unit. |
| `suppress` | Record/attribute withheld from public derivative. |
| `delay` | Publication held until time-based risk is reduced. |
| `clip` | Geometry clipped to safe public boundary. |
| `simplify` | Geometry or attribute detail reduced. |
| `withhold` | No public derivative released. |

Transform classes should not expose reversal parameters. For deterministic transforms, receipts should include enough verifier-safe material to confirm the public output without revealing protected input.

---

## Invariants

PROPOSED semantic invariants:

- RedactionReceipt must be emitted for consequential redaction/generalization/suppression/withholding before public or semi-public use.
- RedactionReceipt must never include the unredacted sensitive value in public-safe form.
- RedactionReceipt must not store transform secrets or parameters that allow reversal or re-identification.
- RedactionReceipt must reference policy/review/validation/release context rather than replacing it.
- A public derivative is not canonical exact truth; it is a public-safe representation with caveats.
- Unknown rights, sensitivity, source-role, consent, or review state must fail closed.
- If a released derivative is corrected, withdrawn, or rolled back, the affected redaction receipt must remain auditable and superseded rather than silently edited.
- Public clients consume released derivatives and receipt-safe notices, never restricted source values.

---

## Lifecycle role

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Typical role by lifecycle phase:

| Lifecycle point | Role of RedactionReceipt |
|---|---|
| WORK / QUARANTINE | Records transform decision and prevents unsafe promotion. |
| PROCESSED | Binds public-safe derivative to restricted input and validation refs. |
| CATALOG / TRIPLET | Supports public-safe graph/catalog projection without leaking exact values. |
| Release candidate | Supports review, policy, and release manifest checks. |
| PUBLISHED | Provides audit trail for public-safe derivative and caveats. |
| Correction/withdrawal/rollback | Supports invalidation, correction, and safe rollback of derivatives. |

---

## Boundaries

| Boundary | Rule |
|---|---|
| RedactionReceipt vs policy | Policy selects/allows/denies transforms; receipt records applied transform. |
| RedactionReceipt vs ReviewRecord | ReviewRecord records human/steward review; receipt references review. |
| RedactionReceipt vs EvidenceBundle | EvidenceBundle supports claims; receipt supports transform audit. |
| RedactionReceipt vs ReleaseManifest | ReleaseManifest publishes artifacts; receipt does not publish. |
| RedactionReceipt vs restricted source | Receipt must not reveal restricted source values. |
| RedactionReceipt vs transform recipe | Receipt may reference a profile; it must not expose reversal-enabling secrets. |
| RedactionReceipt vs domain contracts | Shared semantics do not override Flora/Fauna or other domain-specific rules. |

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- accepted schema home and field shape for RedactionReceipt;
- validator existence and wiring;
- fixture coverage for remove/mask/fuzz/generalize/aggregate/suppress/delay/withhold cases;
- policy profile selection and fail-closed behavior;
- deterministic redaction verifier behavior where applicable;
- receipt signing/hash/integrity posture;
- review workflow for sensitive domains;
- release workflow requiring receipt refs for public-safe derivatives;
- public API/UI behavior showing caveats without leaking protected values;
- correction/withdrawal/rollback invalidation behavior.

---

## Fixtures

Minimum fixture set PROPOSED:

| Fixture | Purpose |
|---|---|
| `valid_generalized_geometry.json` | Geometry precision reduction with policy/review refs. |
| `valid_suppressed_record.json` | Withheld object with no public derivative. |
| `valid_masked_attribute.json` | Attribute masking with safe output digest. |
| `valid_delayed_publication.json` | Time-delay transform with release gating. |
| `valid_aggregated_output.json` | Aggregation-based public-safe derivative. |
| `invalid_missing_policy_ref.json` | Fails when policy basis is absent. |
| `invalid_leaks_sensitive_value.json` | Fails when protected value appears in receipt. |
| `invalid_no_validation_ref.json` | Fails where validation is required. |
| `invalid_reversible_parameters_public.json` | Fails when reversal-enabling parameters leak. |

Fixtures must use synthetic/safe refs only.

---

## Open questions

- Should `contracts/shared/redaction_receipt.md` become the canonical shared contract, or should redaction receipts live under a future `contracts/receipts/` or `contracts/correction/` lane?
- Should `schemas/contracts/v1/receipts/redaction_receipt.schema.json` set `contract_doc` to this file after review?
- Which redaction profile vocabulary is canonical across domains?
- Which fields are safe for public receipt display versus restricted steward audit?
- Which domains require domain-specific extensions beyond this shared contract?

---

## Rollback

Rollback is required if this contract is used to leak protected values, reveal reversal-enabling parameters, replace policy/review/release decisions, claim schema enforcement without implementation, override domain-specific sensitivity rules, or publish a public derivative by itself.

Rollback target for this expansion: previous scaffold blob SHA `1aa1cde98e36e257ed3d6adccb90eba7d86fdbe6`.

<p align="right"><a href="#top">Back to top</a></p>
