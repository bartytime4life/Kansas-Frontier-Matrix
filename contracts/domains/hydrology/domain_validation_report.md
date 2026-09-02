<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-hydrology-domain-validation-report
title: Domain Validation Report Contract — Hydrology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-22
updated: 2026-06-22
policy_label: public-with-gates; semantic-contract; hydrology; validation-report; source-role-aware; evidence-bound; policy-bound; release-gated; rollback-aware
tags: [kfm, contracts, hydrology, domain-validation-report, ValidationReport, CitationValidationReport, SourceDescriptor, EvidenceRef, EvidenceBundle, PolicyDecision, ReleaseManifest, RollbackCard, PASS, FAIL, HOLD, ABSTAIN, DENY, ERROR]
related:
  - ./README.md
  - ./decision_envelope.md
  - ./domain_feature_identity.md
  - ./domain_layer_descriptor.md
  - ./domain_observation.md
  - ./nfhl_zone.md
  - ./hydrograph.md
  - ./aquifer_observation.md
  - ../../../docs/domains/hydrology/API_CONTRACTS.md
  - ../../../docs/domains/hydrology/OBJECT_FAMILIES.md
  - ../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/hydrology/CANONICAL_PATHS.md
  - ../../../schemas/contracts/v1/domains/hydrology/domain_validation_report.schema.json
  - ../../../policy/domains/hydrology/
  - ../../../fixtures/domains/hydrology/domain_validation_report/
  - ../../../tests/domains/hydrology/test_domain_validation_report.*
  - ../../../data/registry/sources/hydrology/
  - ../../../release/candidates/hydrology/
notes:
  - "Expanded from a greenfield scaffold at contracts/domains/hydrology/domain_validation_report.md."
  - "The paired schema exists at schemas/contracts/v1/domains/hydrology/domain_validation_report.schema.json, but it remains a PROPOSED stub with only spec_hash, id, and version properties; only id is required and additionalProperties=true."
  - "Hydrology API doctrine names ValidationReport as part of normalization/validation gates and CitationValidationReport as a public-answer citation closure artifact. This contract keeps those families distinct."
  - "A validation report records deterministic gate results. It is not the validator implementation, not EvidenceBundle proof, not a PolicyDecision, not a ReleaseManifest, and not public-release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Validation Report Contract — Hydrology

> Semantic contract for `domain_validation_report`: the Hydrology validation-report object that records deterministic validation results, failed gates, role-collapse findings, evidence-resolution status, policy/release prerequisites, and rollback implications without becoming proof, policy, release authority, validator code, or a public claim by itself.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: Hydrology" src="https://img.shields.io/badge/domain-Hydrology%20%5BDOM--HYD%5D-1f9eda">
  <img alt="Object: domain_validation_report" src="https://img.shields.io/badge/object-domain__validation__report-blue">
  <img alt="Boundary: report not proof" src="https://img.shields.io/badge/boundary-report__not__proof-critical">
  <img alt="Schema: stub" src="https://img.shields.io/badge/schema-stub%20%2F%20NEEDS__VERIFICATION-orange">
</p>

`contracts/domains/hydrology/domain_validation_report.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Validation report vs trust objects](#validation-report-vs-trust-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended fields](#recommended-fields) · [Gate families](#gate-families) · [Hydrology failure cases](#hydrology-failure-cases) · [Outcome vocabulary](#outcome-vocabulary) · [Lifecycle](#lifecycle) · [Validation of this contract](#validation-of-this-contract) · [Rollback](#rollback) · [Evidence basis](#evidence-basis) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/hydrology/domain_validation_report.md`  
> **Schema path:** `schemas/contracts/v1/domains/hydrology/domain_validation_report.schema.json`  
> **Schema posture:** paired schema exists, but remains a `PROPOSED` stub with only `spec_hash`, `id`, and `version` visible. Only `id` is required and `additionalProperties: true` is still allowed.  
> **Truth posture:** Hydrology docs confirm validation and promotion-gate expectations, but field-level schema shape, validator implementation, fixtures, policy enforcement, CI behavior, emitted reports, and release artifacts remain **NEEDS VERIFICATION**.

> [!CAUTION]
> A validation report is a gate record, not authority to publish. Public release still requires EvidenceBundle closure, PolicyDecision, review where required, ReleaseManifest, correction path, and rollback target.

---

## Meaning

`domain_validation_report` records what Hydrology validation checked, what passed, what failed, what was held, and which downstream state transitions are allowed or blocked.

It can support:

- schema validation results;
- source-role anti-collapse checks;
- identity and `spec_hash` checks;
- temporal-field separation checks;
- geometry/scope checks;
- EvidenceRef/EvidenceBundle resolution checks;
- rights/sensitivity/policy prerequisites;
- release-readiness checks;
- rollback and correction readiness checks.

It does **not** replace the validator, policy engine, evidence bundle, release manifest, or review record. It is the inspectable report emitted by those checks.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Human-readable validation-report meaning | `contracts/domains/hydrology/domain_validation_report.md` | This file; semantic contract for Hydrology validation reports. |
| Machine schema | `schemas/contracts/v1/domains/hydrology/domain_validation_report.schema.json` | Confirmed stub; full report shape is not enforced yet. |
| Contract root | `contracts/domains/hydrology/README.md` | Directory root and object-family boundaries. |
| Runtime envelope | `contracts/domains/hydrology/decision_envelope.md` | Runtime outcomes; not validator report. |
| Feature identity | `contracts/domains/hydrology/domain_feature_identity.md` | Identity and `spec_hash` inputs that validation should check. |
| Observation envelope | `contracts/domains/hydrology/domain_observation.md` | Observation semantics whose validation may emit this report. |
| Layer descriptor | `contracts/domains/hydrology/domain_layer_descriptor.md` | Public-layer descriptor that must cite validation/release state. |
| Source-role matrix | `docs/domains/hydrology/SOURCE_ROLE_MATRIX.md` | Human-readable role-collapse rules that validation should enforce. |
| Policy | `policy/domains/hydrology/` | Expected role/sensitivity/release policy gates. |
| Fixtures/tests | `fixtures/domains/hydrology/domain_validation_report/`, `tests/domains/hydrology/` | Expected valid/invalid examples and gate proofs. |
| Release | `release/candidates/hydrology/` and release roots | ReleaseManifest, CorrectionNotice, RollbackCard; validation report is prerequisite evidence, not release. |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/hydrology/domain_validation_report.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `domain_validation_report` |
| Visible properties | `spec_hash`, `id`, `version` |
| Required fields | `id` only |
| Additional properties | `true` |
| Contract pointer | `contracts/domains/hydrology/domain_validation_report.md` |
| Fixtures pointer | `fixtures/domains/hydrology/domain_validation_report/` |
| Validator pointer | `tools/validators/domains/hydrology/validate_domain_validation_report.py` |
| Policy pointer | `policy/domains/hydrology/` |
| Full report enforcement | NEEDS VERIFICATION |

The schema currently does not prove enforcement of checked object refs, gate outcomes, report status, issue list, validator version, EvidenceBundle resolution, PolicyDecision refs, ReleaseManifest refs, correction refs, or rollback refs.

---

## Validation report vs trust objects

| Object / artifact | What it owns | Boundary |
|---|---|---|
| `domain_validation_report` | Records deterministic validation checks, gate results, issues, and blocked/allowed next steps. | This contract. |
| Validator implementation | Executes checks. | Lives in tool/runtime/test roots, not this contract. |
| `EvidenceBundle` | Proves claims from evidence. | Validation report may confirm resolution, but is not evidence itself. |
| `PolicyDecision` | Allows/restricts/denies access, rendering, sensitivity, or promotion. | Validation report cites it; does not decide policy. |
| `ReleaseManifest` | Publication authority and rollback target. | Validation report is prerequisite support, not release authority. |
| `CorrectionNotice` | Correction/supersession record. | Validation report may require or cite it. |
| `RollbackCard` | Rollback target and invalidation instructions. | Validation report may require it before public release. |
| `decision_envelope` | Runtime `ANSWER / ABSTAIN / DENY / ERROR`. | Validation report feeds it; not the same object. |
| `CitationValidationReport` | Citation/evidence closure for public answer surfaces. | Related but narrower to citation closure; domain report is broader. |

---

## Assertions

A reviewed `domain_validation_report` should assert:

1. **Report identity** — stable report ID, version, `spec_hash`, validator profile, and evaluated target refs.
2. **Target scope** — which object, artifact, layer, source descriptor, evidence bundle, release candidate, or batch was validated.
3. **Gate results** — schema, source role, identity, temporal scope, geometry, evidence, policy, sensitivity, release, correction, and rollback gates are recorded.
4. **Failure visibility** — errors, warnings, holds, denies, abstain triggers, and incomplete dependencies are inspectable.
5. **Source-role integrity** — NFHL-as-observed, modeled-as-observed, aggregate-as-per-place, administrative-as-observation, candidate-as-public, and synthetic-as-observed are detected as failures.
6. **Lifecycle safety** — public exposure is blocked unless required release and rollback artifacts resolve.
7. **Evidence support** — report cites EvidenceRefs/EvidenceBundles it checked, but does not become the evidence.
8. **Policy support** — report cites PolicyDecision/ReviewRecord state where applicable, but does not decide policy.
9. **Correction support** — corrected/superseded objects identify invalidated derivatives and rollback implications.
10. **Runtime compatibility** — report findings can feed `decision_envelope` outcomes without bypassing the governed API.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Validation report as proof of a claim | EvidenceBundle is proof; report only states checks passed/failed. |
| Validation report as release approval | ReleaseManifest / PromotionDecision owns publication. |
| Validation report as policy decision | PolicyDecision owns allow/restrict/deny. |
| Validation report as validator code | Tool/runtime roots own executable checks. |
| Passing schema as public readiness | Schema pass alone cannot prove source role, evidence, rights, policy, release, or rollback. |
| Missing findings treated as pass | Unknown/missing validator state is not approval. |
| `PASS` converted directly to runtime `ANSWER` | Runtime answer still needs evidence, policy, release, and citation closure. |
| NFHL regulatory context validated as observed flood | Role collapse; must fail. |
| Modeled hydrograph validated as observation | Role collapse unless explicitly role-flagged and bounded. |
| Candidate object validated as public | Candidate requires governed admission/review/promotion first. |

---

## Recommended fields

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the current schema stub.

| Field | Meaning |
|---|---|
| `id` | Canonical validation-report ID. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic digest over normalized validation report content. |
| `domain` | Must resolve to `hydrology`. |
| `report_type` | object, batch, source, layer, release_candidate, citation, correction, rollback, or accepted enum. |
| `target_refs` | Object IDs, source descriptors, layer descriptors, artifacts, EvidenceRefs, or release candidates validated. |
| `validator_profile` | Validator name/profile/version/checksum. |
| `evaluated_at` | Evaluation timestamp. |
| `input_digests` | Payload/artifact/spec hashes evaluated. |
| `overall_status` | pass, fail, hold, warning, error, or accepted enum. |
| `gate_results` | Structured results by gate family. |
| `issues` | Errors/warnings/findings with severity, code, message, target path, and remediation. |
| `source_role_findings` | Role-collapse and source-role preservation results. |
| `identity_findings` | ID/spec_hash/source/time/geography checks. |
| `temporal_findings` | source/observed/valid/retrieval/release/correction separation checks. |
| `geometry_findings` | CRS, topology, public geometry, aggregation, redaction/generalization checks. |
| `evidence_findings` | EvidenceRef/EvidenceBundle resolution checks. |
| `policy_findings` | PolicyDecision/review/sensitivity checks. |
| `release_findings` | ReleaseManifest/correction/rollback readiness checks. |
| `recommended_outcome` | Suggested gate/runtime outcome, not authority by itself. |
| `evidence_ref_ids` | EvidenceRefs checked or required. |
| `evidence_bundle_ids` | EvidenceBundles checked or required. |
| `policy_decision_refs` | Policy decisions checked or required. |
| `release_refs` | ReleaseManifest/PromotionDecision refs checked or required. |
| `correction_refs` | CorrectionNotice/supersession refs. |
| `rollback_refs` | RollbackCard refs. |
| `quality_flags` | schema_stub, missing_evidence, role_conflict, release_missing, rollback_missing, sensitive_join, nfhl_observed_collapse, modeled_as_observed, aggregate_as_per_place. |

---

## Gate families

| Gate family | Purpose | Failure consequence |
|---|---|---|
| `schema` | Does the object match expected shape? | `FAIL` / `ERROR`; public answer blocked. |
| `source_descriptor` | Does source identity, role, rights, cadence, and citation resolve? | `HOLD` / `FAIL`; no promotion. |
| `identity` | Does `id` / `spec_hash` / temporal scope / object family resolve deterministically? | `FAIL`; correction or quarantine. |
| `source_role` | Does role match object-family permitted basis? | `DENY` / `FAIL` on collapse. |
| `temporal` | Are source/observed/valid/retrieval/release/correction times distinct? | `FAIL` or `ABSTAIN` depending surface. |
| `geometry` | CRS/topology/geometry-role/public-safe geometry check. | `HOLD` / `DENY` for unsafe exposure. |
| `evidence` | EvidenceRef resolves to EvidenceBundle where claims depend on evidence. | `ABSTAIN` / `HOLD`; no public claim. |
| `policy` | Rights/sensitivity/access/render/promotion policy check. | `DENY` / `RESTRICT` / `HOLD`. |
| `release` | ReleaseManifest, correction path, rollback target, version lock. | No public `ANSWER` / no published layer. |
| `correction` | Supersession/invalidation path for changed claims. | `HOLD` until correction lineage exists. |
| `rollback` | Rollback target and invalidation plan exist. | `HOLD` / `DENY` public release. |

---

## Hydrology failure cases

Validation must fail, hold, deny, or abstain on these Hydrology-specific risks:

| Failure case | Required posture |
|---|---|
| NFHL regulatory polygon framed as observed flood extent | `DENY` / `FAIL` |
| Observed flood event derived from NFHL alone | `DENY` / `FAIL` |
| Modeled hydrograph or terrain-derived surface framed as observed reading | `DENY` / `FAIL` |
| HUC/watershed aggregate used as per-place observation | `DENY` / `FAIL` |
| Water-right or well registry row treated as measurement | `DENY` / `FAIL` unless separately evidenced |
| Candidate flood mark or watcher output exposed publicly | `DENY` / `HOLD` |
| Synthetic/AI summary treated as evidence | `DENY` / `FAIL` |
| Missing EvidenceBundle for consequential claim | `ABSTAIN` / `HOLD` |
| Missing ReleaseManifest / rollback target for public layer | `DENY` / `HOLD` |
| Private well/owner/parcel or infrastructure-sensitive join without review | `DENY` / `RESTRICT` / `HOLD` |
| Retrieval/release time substituted for observed/source time | `FAIL` |
| Public path reads RAW/WORK/QUARANTINE directly | `DENY` / `FAIL` |

---

## Outcome vocabulary

Validation reports and runtime answer envelopes have related but different outcome vocabularies.

| Vocabulary | Used by | Meaning |
|---|---|---|
| `PASS` | Validators/gate checks | A check passed. Does not equal public `ANSWER`. |
| `FAIL` | Validators/gate checks | A check failed. Usually blocks promotion or answer. |
| `HOLD` | Review/promotion gates | Work must pause until missing support resolves. |
| `WARNING` | Validators/gate checks | Non-blocking or review-needed finding; must not hide risk. |
| `ERROR` | Validators/runtime | Evaluation failed. |
| `ANSWER` | Runtime decision envelope | Public/governed answer can be returned. |
| `ABSTAIN` | Runtime decision envelope | KFM cannot support the claim. |
| `DENY` | Runtime/policy | KFM refuses unsafe/unsupported access or framing. |

A validation `PASS` can support `ANSWER`, but cannot produce `ANSWER` alone.

---

## Lifecycle

| Phase | Validation-report handling |
|---|---|
| RAW | No public validation report required; source capture should have payload/reference hash and SourceDescriptor context. |
| WORK / QUARANTINE | Validation reports explain why normalization passed, failed, or quarantined. |
| PROCESSED | Reports bind validated objects, EvidenceRefs, source-role checks, identity checks, and quality flags. |
| CATALOG / TRIPLET | Reports help prove catalog/triplet projections do not outrun evidence. |
| RELEASE CANDIDATE | Reports must confirm evidence, policy, source-role, sensitivity, correction, rollback, and release prerequisites. |
| PUBLISHED | Public clients may see safe report summaries or report refs; reports do not replace EvidenceBundle/citations. |
| CORRECTED / SUPERSEDED | New validation reports identify invalidated derivatives and support correction/rollback records. |

---

## Validation of this contract

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/hydrology/domain_validation_report.schema.json` beyond `spec_hash`, `id`, and `version`.
- [ ] Define canonical `overall_status`, `gate_results`, `issue.severity`, `issue.code`, `recommended_outcome`, and `quality_flags` values.
- [ ] Decide whether this object profiles a shared `ValidationReport` schema or remains a Hydrology-specific schema.
- [ ] Add positive fixtures for schema pass, source-role pass, evidence pass, release-candidate pass, corrected-object validation, and rollback-ready validation.
- [ ] Add negative fixtures for NFHL-as-observed, modeled-as-observed, aggregate-as-per-place, candidate-as-public, AI-as-evidence, missing EvidenceBundle, missing ReleaseManifest, missing rollback target, and sensitive join without review.
- [ ] Add validator coverage for report structure and for the underlying gate families.
- [ ] Confirm validation reports are stored or emitted in the appropriate lifecycle/proof/receipt/release roots and not as ad-hoc artifacts.
- [ ] Confirm public API/UI uses `decision_envelope` for answer outcomes and does not treat a validation `PASS` as public release.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| All required checks pass and evidence/policy/release/rollback resolve | `PASS` / release-eligible support |
| Some checks need steward review or missing artifacts can be supplied | `HOLD` |
| Role collapse, policy denial, sensitive exposure, candidate public path, or unsupported source claim occurs | `FAIL` / `DENY` |
| Validator/schema/evidence/policy/release lookup fails | `ERROR` |
| Claim support remains insufficient but not forbidden | `ABSTAIN` for runtime answer surface |

---

## Rollback

Rollback is required when a validation report is wrong, incomplete, over-trusted, or used outside its authority.

Rollback triggers include report schema drift; validator profile drift; missed NFHL-as-observed failure; missed modeled-as-observed failure; aggregate-as-per-place not caught; candidate exposed publicly; synthetic/AI text treated as evidence; missing EvidenceBundle reported as pass; ReleaseManifest/rollback target missing but report marks public-ready; sensitive private-property/infrastructure join not flagged; public runtime treats `PASS` as `ANSWER`; corrected source data invalidates report inputs; or report stored as anonymous artifact without traceable target, validator profile, evidence refs, and correction/rollback linkage.

Rollback artifacts should include affected validation-report IDs, target refs, validator profile, input digests, gate results, issue codes, EvidenceRefs/EvidenceBundles, PolicyDecisions, ReleaseManifests, CorrectionNotices, RollbackCards, invalidated decision envelopes, invalidated layer descriptors, invalidated exports, and replacement validation reports.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `contracts/domains/hydrology/domain_validation_report.md` scaffold | CONFIRMED | Target existed as a greenfield scaffold. | Did not contain Hydrology-specific validation semantics. |
| `schemas/contracts/v1/domains/hydrology/domain_validation_report.schema.json` | CONFIRMED | Schema pointer, current stub fields, fixtures/validator/policy pointers. | Does not enforce full validation report fields. |
| `docs/domains/hydrology/API_CONTRACTS.md` | CONFIRMED | Lifecycle gates, promotion gates, `ValidationReport`, `CitationValidationReport`, anti-patterns, open verification backlog, outcome separation. | Routes, validators, fixture homes, and implementation remain PROPOSED / NEEDS VERIFICATION. |
| `docs/domains/hydrology/OBJECT_FAMILIES.md` | CONFIRMED | Observation families, flood-family separation, hydrograph role, groundwater sensitivity, and object-home crosswalk. | Some field details are inferred/proposed. |
| `docs/domains/hydrology/SOURCE_ROLE_MATRIX.md` | CONFIRMED | Seven-role vocabulary, object-family source-role matrix, cannot-prove grid, anti-collapse DENY conditions. | Matrix is navigational; machine authority requires SourceDescriptor/EvidenceBundle/policy/test support. |
| `contracts/domains/hydrology/README.md` | CONFIRMED | Contract-root trust flow, validation expectations, source-role rules, rollback posture. | Orientation doc, not validator implementation. |
| `contracts/domains/hydrology/decision_envelope.md` | CONFIRMED | Runtime outcome separation and Hydrology deny/obligation profile. | Runtime envelope, not validation report schema. |
| User-provided authoring role | CONFIRMED user instruction | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is this object a Hydrology-specific schema or a profile of a shared cross-domain `ValidationReport`? | NEEDS VERIFICATION | Schema steward + validation steward review. |
| Which exact gate families are required for all Hydrology validation reports? | NEEDS VERIFICATION | Schema/validator/fixture design. |
| Where should validation reports be stored: data/proofs, data/receipts, processed metadata, release candidates, or all with refs? | NEEDS VERIFICATION | Directory Rules + release steward review. |
| Which policy file enforces validation failure-to-deny mappings? | NEEDS VERIFICATION | Inspect `policy/domains/hydrology/` and tests. |
| What is the canonical validator exit-code contract? | OPEN / NEEDS VERIFICATION | ADR or validator contract review. |
| How does `CitationValidationReport` relate to broader `domain_validation_report`? | NEEDS VERIFICATION | API/schema contract review. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Hydrology contract-root README.
- [`./decision_envelope.md`](./decision_envelope.md) — Hydrology runtime decision-envelope alias.
- [`./domain_feature_identity.md`](./domain_feature_identity.md) — Hydrology feature identity contract.
- [`./domain_layer_descriptor.md`](./domain_layer_descriptor.md) — Hydrology layer descriptor contract.
- [`./domain_observation.md`](./domain_observation.md) — Hydrology observation envelope contract.
- [`../../../docs/domains/hydrology/API_CONTRACTS.md`](../../../docs/domains/hydrology/API_CONTRACTS.md) — governed API, gate, and finite-outcome doctrine.
- [`../../../docs/domains/hydrology/OBJECT_FAMILIES.md`](../../../docs/domains/hydrology/OBJECT_FAMILIES.md) — Hydrology object-family catalog.
- [`../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`](../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md) — source-role anti-collapse matrix.
- [`../../../schemas/contracts/v1/domains/hydrology/domain_validation_report.schema.json`](../../../schemas/contracts/v1/domains/hydrology/domain_validation_report.schema.json) — current schema stub.

[Back to top](#top)
