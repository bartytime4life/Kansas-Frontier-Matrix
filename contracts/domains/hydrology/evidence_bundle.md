<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-hydrology-evidence-bundle
title: Evidence Bundle Contract — Hydrology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; runtime-alias; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-22
updated: 2026-06-22
policy_label: public-with-gates; semantic-contract; hydrology; evidence-bundle; evidence-closure; source-role-aware; rights-aware; sensitivity-aware; release-gated; rollback-aware
tags: [kfm, contracts, hydrology, evidence-bundle, EvidenceBundle, EvidenceRef, SourceDescriptor, citations, rights, sensitivity, transforms, checksums, spec-hash, source-role, NFHL, CitationValidationReport, ReleaseManifest, RollbackCard]
related:
  - ./README.md
  - ./decision_envelope.md
  - ./domain_feature_identity.md
  - ./domain_layer_descriptor.md
  - ./domain_observation.md
  - ./domain_validation_report.md
  - ./drought_link.md
  - ./nfhl_zone.md
  - ./flow_observation.md
  - ./hydrograph.md
  - ../../../contracts/evidence/evidence_bundle.md
  - ../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../../schemas/contracts/v1/domains/hydrology/evidence_bundle.schema.json
  - ../../../docs/domains/hydrology/API_CONTRACTS.md
  - ../../../docs/domains/hydrology/OBJECT_FAMILIES.md
  - ../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hydrology/BOUNDARY.md
  - ../../../policy/domains/hydrology/
  - ../../../fixtures/domains/hydrology/evidence_bundle/
  - ../../../tests/domains/hydrology/test_evidence_bundle.*
  - ../../../data/registry/sources/hydrology/
  - ../../../release/candidates/hydrology/
notes:
  - "Expanded from a short alias scaffold at contracts/domains/hydrology/evidence_bundle.md."
  - "The Hydrology schema is a domain-lane alias of the shared evidence_bundle schema via allOf/$ref and currently adds no Hydrology-specific fields."
  - "The shared evidence_bundle schema is PROPOSED but materially requires bundle_id, claim_scope, evidence_refs, source_records, citations, rights, sensitivity, transforms, checksums, and spec_hash."
  - "Hydrology-specific constraints currently live in claim_scope, evidence_refs, source_records, citations, transforms, sensitivity, policy, fixtures, validation reports, and docs; they are not extra top-level schema fields in this alias."
  - "EvidenceBundle proves support for a claim scope; it is not source truth, PolicyDecision, ReleaseManifest, ValidationReport, RunReceipt, public layer, or AI answer."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Evidence Bundle Contract — Hydrology

> Semantic contract for the Hydrology alias of KFM's shared `evidence_bundle`: the closure artifact that packages source records, evidence refs, citations, rights, sensitivity, transforms, checksums, and spec linkage for a Hydrology claim scope without becoming source truth, release authority, policy, validation, or generated answer text.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: Hydrology" src="https://img.shields.io/badge/domain-Hydrology%20%5BDOM--HYD%5D-1f9eda">
  <img alt="Object: EvidenceBundle" src="https://img.shields.io/badge/object-EvidenceBundle-blue">
  <img alt="Schema: shared alias" src="https://img.shields.io/badge/schema-shared__alias-blue">
  <img alt="Boundary: proof not release" src="https://img.shields.io/badge/boundary-proof__not__release-critical">
  <img alt="Policy: cite-or-abstain" src="https://img.shields.io/badge/policy-cite--or--abstain-success">
</p>

`contracts/domains/hydrology/evidence_bundle.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Alias boundary](#alias-boundary) · [EvidenceBundle vs trust objects](#evidencebundle-vs-trust-objects) · [Hydrology claim scopes](#hydrology-claim-scopes) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Field profile](#field-profile) · [Source-role rules](#source-role-rules) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Rollback](#rollback) · [Evidence basis](#evidence-basis) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / domain alias semantic contract  
> **Contract path:** `contracts/domains/hydrology/evidence_bundle.md`  
> **Domain schema path:** `schemas/contracts/v1/domains/hydrology/evidence_bundle.schema.json`  
> **Shared schema path:** `schemas/contracts/v1/evidence/evidence_bundle.schema.json`  
> **Schema posture:** the Hydrology schema is an `allOf` alias of the shared EvidenceBundle schema and currently adds no domain-specific fields. The shared schema requires `bundle_id`, `claim_scope`, `evidence_refs`, `source_records`, `citations`, `rights`, `sensitivity`, `transforms`, `checksums`, and `spec_hash`.

> [!CAUTION]
> A Hydrology EvidenceBundle is claim-scope proof support. It is not a SourceDescriptor, raw source record, PolicyDecision, ValidationReport, CitationValidationReport, ReleaseManifest, RunReceipt, layer descriptor, runtime `ANSWER`, or AI-generated explanation.

---

## Meaning

The Hydrology `evidence_bundle` is the domain-lane alias of KFM's shared EvidenceBundle contract. It closes the support needed for a bounded Hydrology claim scope by packaging:

- one or more `EvidenceRef` members;
- source-record handles sufficient for provenance review;
- publication-ready citations;
- effective rights and license posture;
- sensitivity label;
- transforms applied between source evidence and the claim scope;
- checksums for critical inputs/outputs;
- deterministic `spec_hash` linkage.

Hydrology uses EvidenceBundles to support claims such as:

- a HUC/WBD boundary or drainage-accounting claim;
- a reach identity or hydrographic network claim;
- an observed flow, stage, water-quality, groundwater, or aquifer observation claim;
- an NFHL regulatory-context claim, not observed flooding;
- an observed flood event claim, not NFHL-derived alone;
- a modeled hydrograph or upstream trace derivative with model/lineage caveats;
- a cross-lane link such as `DroughtLink`, `WaterUseLink`, or `IrrigationLink`, where both sides preserve ownership, source role, sensitivity, and evidence.

EvidenceBundles answer: “What evidence supports this exact claim scope?” They do not answer: “Is this public-safe?” or “Should this be rendered?” Those require policy and release gates.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Human-readable Hydrology alias meaning | `contracts/domains/hydrology/evidence_bundle.md` | This file. Defines Hydrology-specific use of the shared EvidenceBundle. |
| Shared EvidenceBundle meaning | `contracts/evidence/evidence_bundle.md` | Common contract defining purpose, lifecycle, fields, and invariants. |
| Shared machine schema | `schemas/contracts/v1/evidence/evidence_bundle.schema.json` | Required field shape for all evidence bundles. |
| Hydrology alias schema | `schemas/contracts/v1/domains/hydrology/evidence_bundle.schema.json` | `$ref` alias to shared schema; adds no fields. |
| Hydrology API doctrine | `docs/domains/hydrology/API_CONTRACTS.md` | EvidenceBundle resolver surface, trust-membrane flow, citation validation, finite outcomes. |
| Source-role doctrine | `docs/domains/hydrology/SOURCE_ROLE_MATRIX.md` | Defines what evidence can and cannot prove by role. |
| Object catalog | `docs/domains/hydrology/OBJECT_FAMILIES.md` | Object families and cross-lane link posture. |
| Policy | `policy/domains/hydrology/` | Expected rights/sensitivity/release/source-role gates. |
| Fixtures/tests | `fixtures/domains/hydrology/evidence_bundle/`, `tests/domains/hydrology/` | Expected valid/invalid proof fixtures. |
| Release | `release/candidates/hydrology/` and release roots | ReleaseManifest, CorrectionNotice, RollbackCard; bundle is prerequisite support, not release. |

---

## Schema posture

### Confirmed Hydrology alias schema

| Schema element | Current value |
|---|---|
| `$id` | `https://schemas.kfm.local/contracts/v1/domains/hydrology/evidence_bundle.schema.json` |
| Description | Hydrology domain alias of common `evidence_bundle` contract. |
| `contract_doc` | `contracts/domains/hydrology/evidence_bundle.md` |
| `fixtures_root` | `fixtures/domains/hydrology/evidence_bundle/` |
| `validator` | `tools/validators/domains/hydrology/validate_evidence_bundle.py` |
| `policy` | `policy/domains/hydrology/` |
| `status` | `PROPOSED` |
| Shape | `allOf` `$ref` to shared EvidenceBundle schema |
| Extra fields | `unevaluatedProperties: false` |

### Confirmed shared schema fields

| Field | Required | Hydrology interpretation |
|---|:--:|---|
| `bundle_id` | yes | Stable bundle ID for a Hydrology claim scope. |
| `claim_scope` | yes | Exact Hydrology claim or cross-lane relation this bundle supports. |
| `evidence_refs` | yes | Non-empty set of EvidenceRefs. |
| `source_records` | yes | Non-empty source-record handles for provenance reconstruction. |
| `citations` | yes | Non-empty publication-ready citations. |
| `rights` | yes | Effective rights object, requiring `license`. |
| `sensitivity` | yes | Sensitivity label object. |
| `transforms` | yes | Ordered transformations applied from source evidence to claim support. |
| `checksums` | yes | At least one SHA-256 checksum entry. |
| `spec_hash` | yes | Deterministic spec linkage. |

---

## Alias boundary

Because the Hydrology schema is a `$ref` alias and uses `unevaluatedProperties: false`, it cannot currently add Hydrology-specific top-level fields such as `object_family`, `source_role`, `release_ref`, `rollback_ref`, `nfhl_caveat`, or `not_for_life_safety` unless the shared schema is extended or the domain alias schema is revised.

Hydrology-specific meaning must therefore be carried through existing common fields:

| Hydrology concern | Current schema carrier |
|---|---|
| Object family / claim type | `claim_scope`, `evidence_refs`, `source_records`, `transforms`, citations. |
| Source-role anti-collapse | `claim_scope`, EvidenceRef/SourceDescriptor content, `transforms`, validation report, policy. |
| NFHL regulatory caveat | `claim_scope`, `citations`, `transforms`, `sensitivity`, policy/release docs. |
| Modeled hydrograph caveat | `claim_scope`, `source_records`, `transforms`, checksums, validation/report refs outside this schema. |
| Cross-lane link evidence | `claim_scope`, `evidence_refs`, `source_records`, citations and transforms for both sides. |
| Rights/sensitivity | `rights`, `sensitivity`, policy review. |
| Integrity | `checksums`, `spec_hash`. |
| Public release readiness | Outside this schema: PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard. |

> [!WARNING]
> Do not document Hydrology-specific EvidenceBundle fields as implemented until the schema is extended. Current Hydrology-specific obligations are semantic, policy, fixture, and validation expectations layered on top of the shared schema.

---

## EvidenceBundle vs trust objects

| Object / artifact | What it owns | Boundary |
|---|---|---|
| `EvidenceBundle` | Evidence closure for a claim scope. | This contract profiles Hydrology use. |
| `EvidenceRef` | Pointer/member evidence item. | Bundle contains refs; refs are not the closure by themselves. |
| `SourceDescriptor` | Source identity, source role, rights, cadence, permitted claims. | Bundle cites source records; it does not admit source role. |
| Source records | Raw/source provenance handles. | Bundle cites handles; source bytes remain in lifecycle/source roots. |
| `PolicyDecision` | Allow/restrict/deny/abstain posture. | Bundle supplies facts for policy; it does not decide. |
| `ValidationReport` | Gate-check results. | Bundle may be checked by reports; it is not a report. |
| `CitationValidationReport` | Citation/evidence closure for an answer surface. | Bundle supports it; it does not replace it. |
| `ReleaseManifest` | Public publication authority and rollback target. | Bundle is release prerequisite, not release. |
| `LayerManifest` / map tiles | Delivery artifacts. | Bundle may support layer claims; tiles are not evidence. |
| `AIReceipt` / generated answer | AI audit/generated surface. | Bundle outranks generated text. |

---

## Hydrology claim scopes

`claim_scope` must be narrow enough that reviewers can tell what the bundle supports and what it does not support.

| Scope type | Example claim scope pattern | Required warning |
|---|---|---|
| HUC / watershed | `hydrology:huc12:<code>:wbd:<snapshot>` | Vintage/snapshot must be visible. |
| Reach identity | `hydrology:reach:<id>:nhdplus:<version>` | Ambiguous reach identity causes ABSTAIN, not guessing. |
| Gauge observation | `hydrology:flow_observation:<site>:<parameter>:<window>` | Unit, qualifier/provisional state, observed/source time required. |
| Water level | `hydrology:water_level:<site>:<parameter>:<window>` | Not emergency flood stage guidance unless separately authoritative and released by official sources. |
| Water quality | `hydrology:water_quality:<station>:<characteristic>:<sample>` | Program rights/sensitivity and method limits matter. |
| Groundwater/aquifer | `hydrology:aquifer_observation:<well_or_site>:<window>` | Private-property/well-owner implications require review/generalization. |
| NFHL regulatory context | `hydrology:nfhl_zone:<panel_or_zone>:<effective_date>` | Regulatory only; never observed inundation. |
| Observed flood event | `hydrology:observed_flood_event:<source>:<event_window>` | Must be observed evidence; not NFHL-derived alone. |
| Hydrograph derivative | `hydrology:hydrograph:<series_or_run>:<window>` | Modeled/derived; model/run/uncertainty and inputs must travel. |
| Drought link | `hydrology:drought_link:<hydrology_ref>:<drought_ref>:<window>` | Link is not drought truth; both sides preserve ownership and evidence. |

---

## Assertions

A reviewed Hydrology EvidenceBundle should assert:

1. **Bundle identity** — `bundle_id` and `spec_hash` are stable and deterministic for the claim scope.
2. **Claim scope** — scope is explicit enough to prevent overuse.
3. **Evidence membership** — `evidence_refs` is non-empty and relevant to the scope.
4. **Source reconstruction** — `source_records` is non-empty and sufficient to reconstruct provenance review.
5. **Citation readiness** — `citations` is non-empty and public-safe for the intended audience.
6. **Rights posture** — `rights.license` is present and compatible with intended exposure.
7. **Sensitivity posture** — `sensitivity` reflects the highest applicable restriction.
8. **Transform lineage** — `transforms` records aggregation, clipping, reprojection, generalization, redaction, modeling, or derivation steps.
9. **Integrity** — `checksums` covers critical source and derived materials.
10. **Role safety** — source-role anti-collapse is inspectable through refs, source records, transforms, and validation/policy records.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating bundle presence as public release | ReleaseManifest / PromotionDecision still required. |
| Treating bundle as policy approval | PolicyDecision still required. |
| Treating bundle as source admission | SourceDescriptor and source registry own source role/rights/cadence. |
| Treating bundle as validation report | ValidationReport / CitationValidationReport remain separate. |
| Treating map tile or style as evidence | Tiles/styles are delivery surfaces. |
| Using a broad bundle for a narrower unsupported claim | Claim scope must match the answer/export/layer. |
| Using NFHL bundle as observed-flood evidence | Regulatory context is not observed inundation. |
| Using modeled bundle as observed reading | Modeled role and transforms must remain visible. |
| Using aggregate bundle as per-place truth | Aggregate evidence cannot prove individual/place claims. |
| Using AI summary as evidence | AI is interpretive; bundle must resolve source evidence. |

---

## Field profile

The Hydrology alias uses the shared required field set.

| Field | Hydrology requirements |
|---|---|
| `bundle_id` | Stable ID; should encode domain/claim family only if ID registry allows it. |
| `claim_scope` | Must say what Hydrology claim or cross-lane relation is supported. Avoid vague scopes like `flood layer` or `water data`. |
| `evidence_refs` | Must resolve to relevant EvidenceRefs; source role should be traceable through refs/SourceDescriptor. |
| `source_records` | Must include record handles sufficient to audit source, time, rights, and transformation. |
| `citations` | Must be publication-ready or explicitly marked restricted/internal where policy allows. |
| `rights` | Must include license and be compatible with public/restricted exposure. |
| `sensitivity` | Must represent highest applicable sensitivity, especially for groundwater/private-property/infrastructure/cross-lane joins. |
| `transforms` | Must record every material transform: normalize, reproject, aggregate, generalize, redact, model, crosswalk, join, or clip. |
| `checksums` | Must contain at least one `sha256:<64 hex>` entry; should cover source and material derivatives. |
| `spec_hash` | Must bind the bundle to schema/contract baseline and normalized support set. |

---

## Source-role rules

EvidenceBundles do not assign source role, but Hydrology bundles must preserve source-role visibility.

| Role condition | Bundle behavior |
|---|---|
| Observed readings | Cite source records and time/unit/qualifier support; provisional/final status must be recoverable. |
| Regulatory NFHL | Claim scope and citations must say regulatory context; observed-flood claims are denied. |
| Modeled hydrograph | Transform lineage must record model/run/inputs/uncertainty support. |
| Aggregate HUC/drought/summary | Scope must preserve aggregation unit/window; no per-place claim without separate evidence. |
| Administrative records | Claim scope must stay administrative unless observed evidence also exists. |
| Candidate material | Bundle cannot support public answer until admission/review/promotion resolves. |
| Synthetic/AI material | Cannot serve as underlying evidence for observed reality; may be cited only as interpretive output with AIReceipt. |

---

## Lifecycle

| Phase | EvidenceBundle handling |
|---|---|
| RAW | Source bytes/records are captured in lifecycle roots; no bundle is source truth. |
| WORK / QUARANTINE | Evidence refs, source records, rights, transforms, sensitivity, and checksums are assembled or held. |
| PROCESSED | Bundle may be formed as closure of normalized evidence collection. |
| CATALOG / TRIPLET | Bundle IDs can support catalog/triplet claims, but projections do not become truth. |
| RELEASE CANDIDATE | Bundle is checked with PolicyDecision, ReviewRecord where needed, ReleaseManifest, correction path, and RollbackCard. |
| PUBLISHED | Governed APIs, Evidence Drawer, Focus Mode, exports, and layers may cite bundle support only through released public-safe paths. |
| CORRECTED / SUPERSEDED | New bundle or correction lineage records changed evidence, transforms, rights, sensitivity, or checksums; prior bundles remain auditable. |

---

## Validation

Before this alias contract is promoted beyond draft:

- [ ] Confirm the Hydrology alias schema intentionally adds no fields beyond the shared EvidenceBundle schema.
- [ ] Confirm `tools/validators/domains/hydrology/validate_evidence_bundle.py` exists and validates alias + Hydrology-specific semantic fixtures, or create it.
- [ ] Add valid fixtures for HUC/WBD evidence, reach identity evidence, gauge observation evidence, NFHL regulatory context, observed flood evidence, hydrograph derivative evidence, groundwater/aquifer evidence, and DroughtLink cross-lane evidence.
- [ ] Add invalid fixtures for empty `evidence_refs`, empty `source_records`, empty `citations`, missing `rights.license`, missing `sensitivity`, missing transforms, invalid checksum, missing `spec_hash`, NFHL-as-observed, modeled-as-observed, aggregate-as-per-place, candidate public support, and AI-summary-as-evidence.
- [ ] Confirm CitationValidationReport cannot pass public answer surfaces without a matching EvidenceBundle.
- [ ] Confirm PolicyDecision gates rights/sensitivity/source-role exposure before release.
- [ ] Confirm ReleaseManifest and RollbackCard are required before public layers/exports/answers use the bundle.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Bundle validates, source role is preserved, evidence/citations/rights/sensitivity/transforms/checksums resolve, and release/policy allow use | `ANSWER` support / release-eligible proof support |
| Evidence refs, citations, rights, sensitivity, transforms, or checksums are insufficient | `ABSTAIN` / `HOLD` |
| Policy, rights, sensitivity, source-role collapse, candidate exposure, AI-as-evidence, or public-path bypass blocks use | `DENY` |
| Schema, resolver, checksum, source lookup, policy lookup, or release lookup fails | `ERROR` |

---

## Rollback

Rollback is required when a Hydrology EvidenceBundle is over-trusted, malformed, mismatched to claim scope, or used outside its authority.

Rollback triggers include missing or invalid required fields; EvidenceRefs cannot resolve; source records are insufficient; citations are missing or wrong; rights/license changes; sensitivity label is too permissive; transform lineage is incomplete; checksum mismatch; `spec_hash` drift; NFHL regulatory bundle used as observed-flood support; modeled hydrograph bundle used as observed reading; aggregate bundle used as per-place truth; candidate evidence used publicly; AI summary treated as evidence; public answer emitted without CitationValidationReport; release uses bundle without ReleaseManifest or RollbackCard; or source correction invalidates bundle members.

Rollback artifacts should include affected `bundle_id`s, claim scopes, EvidenceRefs, source records, citations, rights/sensitivity labels, transform list, checksums, spec hashes, validation reports, citation validation reports, PolicyDecisions, ReleaseManifests, CorrectionNotices, RollbackCards, invalidated layer descriptors, invalidated decision envelopes, invalidated exports, and public-cache/style invalidation instructions.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `contracts/domains/hydrology/evidence_bundle.md` scaffold | CONFIRMED | Target existed and stated it is a Hydrology alias of the common evidence bundle contract. | Thin alias only; did not include Hydrology-specific semantics. |
| `schemas/contracts/v1/domains/hydrology/evidence_bundle.schema.json` | CONFIRMED | Domain alias schema, `$ref` to shared schema, fixtures/validator/policy pointers, `unevaluatedProperties: false`. | Adds no Hydrology-specific fields. |
| `schemas/contracts/v1/evidence/evidence_bundle.schema.json` | CONFIRMED | Required shared field set and schema constraints. | Schema status remains PROPOSED. |
| `contracts/evidence/evidence_bundle.md` | CONFIRMED | Common purpose, lifecycle, fields, invariants, cross-references, validator/status notes. | Common contract; Hydrology-specific constraints are profile semantics. |
| `docs/domains/hydrology/API_CONTRACTS.md` | CONFIRMED | Trust membrane, EvidenceBundle resolver surface, Evidence Drawer/CitationValidationReport relationship, finite outcomes, forbidden public paths. | Routes/DTOs/runtime implementation remain PROPOSED / NEEDS VERIFICATION. |
| `docs/domains/hydrology/SOURCE_ROLE_MATRIX.md` | CONFIRMED | Source roles are fixed at admission; source-role collapse fails closed. | Machine enforcement requires SourceDescriptor/policy/fixtures/validators. |
| `docs/domains/hydrology/OBJECT_FAMILIES.md` | CONFIRMED | Hydrology object families and cross-lane links that need evidence closure. | Some field realizations remain PROPOSED. |
| User-provided authoring role | CONFIRMED user instruction | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Should Hydrology EvidenceBundle remain a pure alias forever, or gain domain-specific fields in PR 2b? | NEEDS VERIFICATION | Evidence/schema/domain steward review. |
| Where should Hydrology-specific `object_family`, `source_role`, `release_ref`, and `rollback_ref` live if the alias remains fieldless? | NEEDS VERIFICATION | Runtime/schema/policy design. |
| Which Hydrology claim-scope vocabulary is canonical? | NEEDS VERIFICATION | Schema/fixtures/contract registry. |
| Which validator proves NFHL-as-observed and modeled-as-observed cannot pass bundle closure? | NEEDS VERIFICATION | Negative fixtures and validator implementation. |
| How should CitationValidationReport reference EvidenceBundle in public Focus Mode answers? | NEEDS VERIFICATION | Governed API + AIReceipt contract review. |
| Which receipts/proofs root stores Hydrology EvidenceBundle outputs? | NEEDS VERIFICATION | Directory Rules + evidence/release steward review. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Hydrology contract-root README.
- [`./decision_envelope.md`](./decision_envelope.md) — Hydrology runtime decision-envelope alias.
- [`./domain_feature_identity.md`](./domain_feature_identity.md) — Hydrology feature identity contract.
- [`./domain_layer_descriptor.md`](./domain_layer_descriptor.md) — Hydrology layer descriptor contract.
- [`./domain_observation.md`](./domain_observation.md) — Hydrology observation contract.
- [`./domain_validation_report.md`](./domain_validation_report.md) — Hydrology validation-report contract.
- [`../../../contracts/evidence/evidence_bundle.md`](../../../contracts/evidence/evidence_bundle.md) — shared EvidenceBundle contract.
- [`../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json`](../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json) — shared EvidenceBundle schema.
- [`../../../schemas/contracts/v1/domains/hydrology/evidence_bundle.schema.json`](../../../schemas/contracts/v1/domains/hydrology/evidence_bundle.schema.json) — Hydrology alias schema.
- [`../../../docs/domains/hydrology/API_CONTRACTS.md`](../../../docs/domains/hydrology/API_CONTRACTS.md) — governed API and EvidenceBundle resolver doctrine.
- [`../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`](../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md) — source-role anti-collapse matrix.
- [`../../../docs/domains/hydrology/OBJECT_FAMILIES.md`](../../../docs/domains/hydrology/OBJECT_FAMILIES.md) — object-family catalog.

[Back to top](#top)
