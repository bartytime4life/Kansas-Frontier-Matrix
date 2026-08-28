<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-domain-validation-report
title: Domain Validation Report Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Sensitivity reviewer
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public-with-gates; semantic-contract; geology; domain-validation-report; validator-output; evidence-bound; source-role-aware; policy-aware; release-gated; no-publication-authority
tags: [kfm, contracts, geology, domain_validation_report, validation-report, validator-output, evidence-ref, evidence-bundle, source-role, schema, fixtures, policy, sensitivity, release-candidate, correction, rollback, anti-collapse]
related:
  - ./README.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./domain_layer_descriptor.md
  - ./GeologicUnit.md
  - ./Lithology.md
  - ./StratigraphicInterval.md
  - ./GeologicAge.md
  - ./StructureFeature.md
  - ./BoreholeReference.md
  - ./WellLogReference.md
  - ./CoreSample.md
  - ./GeophysicalObservation.md
  - ./GeochemistrySample.md
  - ./MineralOccurrence.md
  - ./ResourceDeposit.md
  - ./ResourceEstimate.md
  - ./ExtractionSite.md
  - ./ReclamationRecord.md
  - ./CrossSection.md
  - ./HydrostratigraphicUnit.md
  - ../../../docs/domains/geology/VERIFICATION_BACKLOG.md
  - ../../../docs/domains/geology/API_CONTRACTS.md
  - ../../../docs/domains/geology/RELEASE_INDEX.md
  - ../../../docs/domains/geology/IDENTITY_MODEL.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../schemas/contracts/v1/domains/geology/domain_validation_report.schema.json
  - ../../../fixtures/domains/geology/domain_validation_report/
  - ../../../tools/validators/domains/geology/validate_domain_validation_report.py
  - ../../../tests/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../policy/sensitivity/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a greenfield scaffold into a Geology semantic contract for validator-result reporting."
  - "The paired schema exists at schemas/contracts/v1/domains/geology/domain_validation_report.schema.json, but it is still a PROPOSED stub with only id, version, and spec_hash fields; field-level enforcement remains NEEDS VERIFICATION."
  - "DomainValidationReport records validation evidence, findings, and review support. It is not source truth, not an EvidenceBundle, not a PolicyDecision, not a ReviewRecord, not a ReleaseManifest, and not public publication authority."
  - "Geology validation must preserve source role, six time dimensions, sensitivity gates, EvidenceRef/EvidenceBundle closure, release/correction/rollback support, and object-family anti-collapse rules."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Validation Report — Geology

> Semantic contract for `domain_validation_report`: the auditable Geology report emitted by validation work over object-family records, observation envelopes, identity envelopes, layer descriptors, schemas, fixtures, source roles, evidence links, sensitivity states, release candidates, correction notices, and rollback paths.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: domain_validation_report" src="https://img.shields.io/badge/object-domain__validation__report-blue">
  <img alt="Schema: stub" src="https://img.shields.io/badge/schema-stub%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Truth: validation support" src="https://img.shields.io/badge/truth-validation__support-informational">
  <img alt="Boundary: report not release authority" src="https://img.shields.io/badge/boundary-report__not__release__authority-critical">
</p>

`contracts/domains/geology/domain_validation_report.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Validation report vs trust objects](#validation-report-vs-trust-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Finding model](#finding-model) · [Validation families](#validation-families) · [Geology deny checks](#geology-deny-checks) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/domain_validation_report.md`  
> **Schema path:** `schemas/contracts/v1/domains/geology/domain_validation_report.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` stub. It currently defines only `spec_hash`, `id`, and `version`, requires only `id`, and permits additional properties.  
> **Truth posture:** Geology doctrine supports validation/reporting over source role, evidence closure, lifecycle membrane, policy/sensitivity, release, rollback, and object-family boundaries. Field-level schema enforcement, fixtures, validator behavior, CI integration, policy runtime, release workflow, emitted report examples, API behavior, and UI behavior remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `domain_validation_report` records validation results and supports review. It does **not** create source truth, does **not** replace EvidenceBundle, does **not** publish Geology claims, does **not** approve exact subsurface/resource geometry, and does **not** substitute for PolicyDecision, ReviewRecord, ReleaseManifest, PromotionDecision, CorrectionNotice, or RollbackCard.

---

## Meaning

`domain_validation_report` is the Geology lane's semantic object for a bounded validation run, dry-run, schema pass, fixture pass, policy preflight, evidence-closure check, source-role check, sensitivity check, release-candidate check, correction verification, rollback verification, or anti-collapse regression check.

It answers:

- What Geology objects, observations, layer descriptors, source rows, fixtures, artifacts, release candidates, corrections, or rollback targets were checked?
- Which validator, schema, ruleset, fixture pack, source registry entry, policy posture, EvidenceBundle, catalog closure, or release candidate was used?
- Which evidence, source-role, geometry, temporal, sensitivity, rights, artifact-digest, catalog, policy, release, and rollback checks passed, warned, failed, abstained, or errored?
- Which findings block promotion or publication?
- Which findings are informational and can be reviewed later without weakening source integrity or public safety?
- Which follow-up artifacts are required before the checked material can move through the trust membrane?

A validation report is an audit object and review input. It can support a promotion or review decision, but it is never the decision itself.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Report meaning | `contracts/domains/geology/domain_validation_report.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/geology/domain_validation_report.schema.json` | CONFIRMED stub; field-level enforcement NEEDS VERIFICATION |
| Validator implementation | `tools/validators/domains/geology/validate_domain_validation_report.py` | Schema-declared target; implementation NEEDS VERIFICATION |
| Fixtures | `fixtures/domains/geology/domain_validation_report/` | Expected valid/invalid examples; presence/content NEEDS VERIFICATION |
| Tests | `tests/domains/geology/` | Expected regression checks; coverage NEEDS VERIFICATION |
| Policy inputs | `policy/domains/geology/`, `policy/sensitivity/geology/` | Report may cite posture/results; it does not replace decisions |
| Source registry | `data/registry/sources/geology/` | Source rights, role, cadence, authority, and attribution support |
| Evidence/proof inputs | EvidenceRef/EvidenceBundle/proof/catalog homes — accepted paths NEED VERIFICATION | Report verifies closure but does not become proof |
| Release artifacts | `release/`, `release/manifests/geology/` | Report may support release review; it does not publish |
| Geology contracts | `contracts/domains/geology/*.md` | Report may validate any Geology semantic contract or object family |
| Public surfaces | Governed API/UI/map layers only | Public clients consume released, policy-safe derivatives, not raw validation internals by default |

---

## Schema posture

The paired schema exists but is intentionally thin.

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/geology/domain_validation_report.schema.json` |
| Schema status | `PROPOSED` |
| Schema description | Greenfield placeholder; fields to be defined per contract document and ADR |
| Defined properties | `spec_hash`, `id`, `version` |
| Required fields | `id` only |
| Additional properties | `true` |
| Schema-linked fixtures root | `fixtures/domains/geology/domain_validation_report/` |
| Schema-linked validator | `tools/validators/domains/geology/validate_domain_validation_report.py` |
| Validator implementation | NEEDS VERIFICATION; schema references the path, but runtime/file behavior was not verified here |

Until the schema is expanded, this contract defines semantics and fixture targets, not field-level enforcement.

---

## Validation report vs trust objects

`DomainValidationReport` is part of the proof/review chain, but it is not the proof, policy, catalog, or release decision.

| Object / artifact | What it does | What the validation report may do | What the report must not do |
|---|---|---|---|
| `EvidenceBundle` | Carries admissible evidence support | Check closure, digest, and resolvability | Replace evidence or assert truth alone |
| `PolicyDecision` | Allows, restricts, denies, or holds use/release | Record policy-check inputs/results | Decide policy by itself |
| `ReviewRecord` | Captures steward review | Provide findings to reviewers | Replace human/steward review where required |
| `ReleaseManifest` | Publishes / promotes an artifact | Confirm required fields/refs exist | Publish or promote bytes |
| `CorrectionNotice` | Records correction/supersession | Verify correction target and rebuild scope | Correct without notice/lineage |
| `RollbackCard` | Defines rollback action | Verify rollback target and instructions | Roll back silently |
| `LayerManifest` / layer descriptor | Describes renderable released layer | Check artifact digest, geometry role, evidence/policy refs | Turn a layer into canonical truth |
| `AIReceipt` | Records generated-answer context | Verify AI cited evidence and outcomes | Treat AI answer as evidence |

---

## Assertions

A reviewed `domain_validation_report` should semantically assert:

1. **Run identity** — stable report ID, run ID, ruleset, validator, schema version, and `spec_hash`.
2. **Validation target** — object family, observation, identity envelope, layer descriptor, artifact, fixture, source row, release candidate, correction notice, or rollback target under test.
3. **Input refs** — source records, schemas, contracts, fixtures, policy refs, EvidenceRefs, EvidenceBundles, artifacts, release refs, and rollback refs used by the check.
4. **Check families** — schema, semantic contract, source role, EvidenceBundle closure, identity/spec hash, geometry, sensitivity, rights, policy, release, correction, rollback, and anti-collapse checks.
5. **Finding model** — finite severities and outcomes: pass, warn, fail, abstain, deny, error, hold, restrict, or needs-review.
6. **Blocking posture** — which findings block promotion, publication, API serving, map rendering, AI answer, export, or correction closure.
7. **Evidence trail** — digest of checked inputs, validator version, ruleset hash, artifact hash, time, environment summary, and evidence refs.
8. **Lifecycle posture** — whether target is RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, RELEASE_CANDIDATE, PUBLISHED, CORRECTED, WITHDRAWN, or SUPERSEDED.
9. **Sensitivity posture** — public-safe, generalized, aggregate, restricted, withheld, rights-limited, source-limited, unknown, or denied exposure state.
10. **Follow-up actions** — required fixture, schema, policy, source registry, release, correction, rollback, ADR, or drift-register work.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating validation success as source truth | Validation says a check passed; evidence and source role still carry truth. |
| Treating validation success as publication approval | ReleaseManifest / PromotionDecision owns publication. |
| Treating report as policy decision | PolicyDecision owns allow/restrict/deny/hold. |
| Treating report as EvidenceBundle | Reports may cite evidence; they are not the evidence. |
| Treating report as source registry activation | SourceDescriptor/source registry gates remain separate. |
| Treating report as review approval | ReviewRecord and steward sign-off remain separate where required. |
| Treating report as public API payload by default | Public clients should not receive raw validation internals unless released and filtered. |
| Treating warnings as harmless | Some warnings are publication blockers; severity must be explicit. |
| Treating missing evidence as pass | Missing EvidenceBundle closure is ABSTAIN/DENY, not pass. |
| Treating AI-generated report prose as validator output | Validator findings must be tool/ruleset/evidence-backed. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. Only `id`, `version`, and `spec_hash` are currently visible in the confirmed schema stub.

| Field | Meaning |
|---|---|
| `id` | Canonical validation-report ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized report digest. |
| `domain` | Must resolve to `geology`. |
| `run_id` | Validation run identifier. |
| `run_type` | Schema, semantic, fixture, source, policy, evidence, release, correction, rollback, or combined check. |
| `target_refs` | Objects, files, schemas, artifacts, fixtures, source records, release candidates, or corrections checked. |
| `target_lifecycle_state` | Lifecycle state of checked targets. |
| `validator_ref` | Validator script/tool/container/action ref. |
| `validator_version` | Validator version or digest. |
| `ruleset_ref` | Ruleset/checklist/policy/schema ref. |
| `ruleset_hash` | Digest of ruleset inputs. |
| `schema_refs` | JSON Schema refs under test. |
| `contract_refs` | Markdown semantic contracts under test. |
| `fixture_refs` | Valid/invalid/sensitive/correction fixture refs. |
| `source_descriptor_refs` | SourceDescriptor refs used by checked claims. |
| `evidence_refs` | EvidenceRef links checked for closure. |
| `evidence_bundle_refs` | EvidenceBundle refs resolved by validation. |
| `policy_refs` | Policy files/rules/decisions consulted. |
| `release_refs` | Release candidate, ReleaseManifest, PromotionDecision, or publication refs checked. |
| `correction_refs` | CorrectionNotice, supersession, withdrawal, or replacement refs checked. |
| `rollback_refs` | RollbackCard or rollback target refs checked. |
| `artifact_refs` | Layer, PMTiles, GeoParquet, COG, report, or payload artifacts checked. |
| `artifact_digests` | Digests of checked artifacts. |
| `source_role_results` | Source-role preservation and anti-collapse findings. |
| `temporal_results` | Source/observed/valid/retrieval/release/correction time findings. |
| `geometry_results` | Geometry precision, CRS, topology, fingerprint, public-safe geometry, and redaction findings. |
| `sensitivity_results` | Sensitivity, rights, public-safe exposure, redaction/aggregation/withholding findings. |
| `evidence_results` | EvidenceRef/EvidenceBundle resolution and hash findings. |
| `identity_results` | Deterministic identity and `spec_hash` findings. |
| `policy_results` | Policy-preflight findings; not final policy decision unless linked. |
| `release_results` | Release-manifest/preflight findings; not release approval. |
| `findings` | Structured findings with severity, code, message, target, source refs, and blocking state. |
| `summary_outcome` | PASS, WARN, FAIL, ABSTAIN, DENY, ERROR, HOLD, RESTRICT, NEEDS_REVIEW, or accepted enum. |
| `blocks_publication` | Boolean or enum explaining whether publication is blocked. |
| `blocks_ai_answer` | Whether Focus Mode/AI answering must abstain/deny. |
| `blocks_layer_serving` | Whether public layer serving must deny/hold. |
| `review_record_ref` | Steward review record created from or linked to the report. |
| `drift_register_refs` | Drift items opened/closed by the report. |
| `adr_refs` | ADRs required or used by the report. |
| `created_at` | Report emission time. |
| `created_by` | Tool/run/user/service that emitted the report. |
| `environment_summary` | Minimal reproducibility context without secrets. |
| `quality_flags` | Missing evidence, schema stub, unknown validator, stale source, rights unknown, sensitivity unknown, digest mismatch, source-role collapse, release gap. |

---

## Finding model

Validation findings should be finite, machine-actionable, and reviewable.

| Severity / outcome | Meaning | Publication behavior |
|---|---|---|
| `PASS` | Required check succeeded. | May proceed to next gate, not automatically publish. |
| `WARN` | Non-blocking issue or caveat. | Allowed only if release/review accepts warning. |
| `NEEDS_REVIEW` | Human/steward review required. | Hold until review. |
| `HOLD` | Missing prerequisite or unresolved drift. | Hold until resolved. |
| `ABSTAIN` | Support insufficient to answer or promote. | No authoritative public claim. |
| `RESTRICT` | Allowed only under restricted/steward access. | Public path must not expose detail. |
| `DENY` | Policy/trust/safety violation. | Publication and public serving denied. |
| `FAIL` | Validation rule failed. | Promotion blocked. |
| `ERROR` | Tool/input/runtime failure. | Do not infer validity; rerun or repair. |

> [!IMPORTANT]
> A validation report with only `WARN` findings still does not publish anything. Promotion remains a governed state transition requiring release artifacts and policy/review support.

---

## Validation families

| Family | What it checks | Examples of blocking findings |
|---|---|---|
| `schema_shape` | JSON Schema conformance and required fields. | Missing ID, invalid enum, schema stub used as final proof. |
| `semantic_contract` | Contract meaning and anti-collapse rules. | Deposit treated as estimate; structure treated as hazard risk. |
| `source_role` | Role preservation and role-specific allowed uses. | Modeled estimate relabeled observed; aggregate queried as per-place truth. |
| `temporal_scope` | Six KFM time dimensions and valid/source/observed separation. | Collection time collapsed into report time. |
| `identity_spec_hash` | Deterministic identity and normalized digest. | Meaning-bearing field excluded from hash; hash mismatch. |
| `evidence_closure` | EvidenceRef resolves to EvidenceBundle and hash matches. | Missing bundle, mismatched hash, unsupported claim. |
| `rights_and_sensitivity` | Rights, exact geometry, resource detail, LAS payload, private-well, sample/occurrence restrictions. | Restricted detail public without receipt. |
| `geometry_and_artifact` | CRS, topology, fingerprint, artifact digest, public-safe geometry. | Generalized geometry marked exact; artifact digest mismatch. |
| `policy_preflight` | Whether policy input is sufficient for later PolicyDecision. | Policy ref missing for sensitive public detail. |
| `release_preflight` | Release candidate completeness. | No ReleaseManifest, no PromotionDecision, no rollback target. |
| `correction_rollback` | Correction, supersession, withdrawal, and rollback readiness. | Public artifact corrected without CorrectionNotice. |
| `api_ui_ai_projection` | Public API/UI/AI trust membrane. | RAW/WORK/QUARANTINE read by public path; AI answer lacks EvidenceBundle. |

---

## Geology deny checks

A Geology validation report should explicitly detect and block these high-risk failures:

```text
modeled != observed
aggregate != per-place record
administrative != observed geology
regulatory != field measurement
synthetic != observed reality
EvidenceRef missing != publishable claim
ValidationReport != PolicyDecision
ValidationReport != ReleaseManifest
ValidationReport != EvidenceBundle
ValidationReport != ReviewRecord
Geology layer != canonical truth
```

Geology-specific checks:

```text
MineralOccurrence != ResourceDeposit != ResourceEstimate
ResourceEstimate != observed measurement
StructureFeature != Hazards risk / alert
HydrostratigraphicUnit != Hydrology measurement
BoreholeReference / WellLogReference / CoreSample != public exact point release
WellLogReference != public LAS payload release by default
GeochemistrySample collection time != analytical report time
ExtractionSite != ownership / lease / permit / title proof
ReclamationRecord != legal/environmental compliance proof by default
AI text != evidence
```

---

## Lifecycle

| Phase | Validation-report handling |
|---|---|
| RAW | No authoritative validation report; source payloads remain untrusted for public use. |
| WORK / QUARANTINE | Draft reports may inspect candidates, but public serving is denied. |
| PROCESSED | Schema/semantic/source/evidence/identity checks may produce reviewable reports. |
| CATALOG / TRIPLET | Evidence closure and catalog/triplet projection checks become material. |
| RELEASE CANDIDATE | Release preflight, policy preflight, sensitivity, artifact digest, rollback, and public-surface checks are required. |
| PUBLISHED | Reports support audit/correction; they do not replace release manifests. |
| CORRECTED / WITHDRAWN / SUPERSEDED | Reports verify correction scope, replacement artifacts, public cache invalidation, and rollback readiness. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `domain_validation_report.schema.json` beyond `id`, `version`, and `spec_hash`.
- [ ] Decide exact enum values for `run_type`, `summary_outcome`, finding severity, finding codes, and blocking behavior.
- [ ] Verify or create `tools/validators/domains/geology/validate_domain_validation_report.py`.
- [ ] Add valid fixtures for schema pass, semantic pass, evidence-closure pass, source-role pass, sensitivity pass, release preflight, correction verification, rollback verification, and mixed-result reports.
- [ ] Add invalid fixtures for missing target refs, missing validator ref, missing evidence refs, EvidenceBundle hash mismatch, schema-stub-as-proof, policy decision missing, release manifest missing, rollback target missing, restricted geometry public, source-role collapse, AI-as-evidence, and raw/candidate public serving.
- [ ] Add tests proving validation reports cannot act as release authority, policy authority, evidence authority, or public API truth.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for correction, rollback, source update, schema expansion, fixture failures, artifact digest mismatch, and stale/superseded reports.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Required checks pass and downstream gates still resolve | `PASS` / may proceed to next governed gate |
| Support is incomplete or unresolved | `ABSTAIN` / `HOLD` / `NEEDS_REVIEW` |
| Trust, policy, source-role, sensitivity, release, or anti-collapse rule is violated | `DENY` / `FAIL` |
| Validator, source read, evidence lookup, schema, artifact, policy, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms this target file existed as a greenfield scaffold before replacement. | Does not prove contract maturity. |
| Confirmed paired schema stub | Confirms schema path, `$id`, `x-kfm` pointers, and current minimal fields. | Does not prove field-level validation or validator implementation. |
| Geology verification backlog | Confirms the lane tracks open verification, rights/sensitivity uncertainty, validator/test/fixture gaps, and ADR-class questions. | Backlog closure protocol itself includes PROPOSED elements. |
| Geology API contracts | Confirms public boundary invariants: lifecycle membrane, promotion gates, EvidenceBundle closure, source-role preservation, sensitivity fail-closed, and finite outcomes; routes remain PROPOSED. | Does not prove runtime implementation. |
| Geology Release Index | Confirms validation reports support release artifacts, while ReleaseManifest plus supporting artifacts owns release authority. | Release artifact instances remain NEEDS VERIFICATION. |
| ADR-0011 | Confirms the doctrine distinction receipt ≠ proof ≠ catalog ≠ publication and warns it does not prove validators/tests/schemas/workflows exist. | ADR status is proposed and needs index verification. |
| Cross-domain Flora DomainValidationReport contract | Repo-local precedent for a domain validation report contract. | Flora semantics do not control Geology-specific gates. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized validation report weakens source integrity, misstates validator results, hides blockers, collapses trust-object families, or makes publication appear approved without release authority.

Rollback triggers include:

- schema field names or finding enums are superseded by ADR/schema PR;
- report marked pass despite missing evidence, missing source role, missing policy, or missing release support;
- EvidenceRef cannot resolve to EvidenceBundle or hash mismatch is ignored;
- source role, temporal scope, identity/spec hash, geometry role, sensitivity state, or rights state was collapsed;
- validation report used as PolicyDecision, ReviewRecord, EvidenceBundle, ReleaseManifest, PromotionDecision, CorrectionNotice, or RollbackCard;
- restricted geometry, LAS/log payload, private well, sample, occurrence, resource, or proprietary survey detail entered public output without receipt/release support;
- public API/UI/AI used RAW/WORK/QUARANTINE/candidate outputs as authoritative truth;
- a correction or withdrawal failed to invalidate stale reports or release candidates.

Rollback artifacts should include affected validation-report IDs, run IDs, target refs, finding refs, source refs, EvidenceBundle refs, policy refs, release refs, correction refs, rollback refs, old/new report `spec_hash`, replacement report refs, and public-cache/artifact invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which fields must be required in `domain_validation_report.schema.json` beyond `id`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| What exact finding severity and summary outcome enum should Geology use? | NEEDS VERIFICATION | Validator/schema/API alignment. |
| Should validation reports live as proof objects, receipts, review inputs, or domain records in lifecycle stores? | NEEDS VERIFICATION / CONFLICTED until ADR and Directory Rules placement are checked | ADR-0011 + Directory Rules review. |
| Which validator implementation path and command are canonical for Geology validation? | NEEDS VERIFICATION | Repo tool inspection and CI wiring. |
| Which validation reports are safe to expose publicly, and which must remain steward-only? | NEEDS VERIFICATION | Policy, sensitivity, and release fixture review. |
| How should stale or superseded validation reports invalidate release candidates and public caches? | NEEDS VERIFICATION | Release/runtime/cache invalidation design. |
| How should AI/Focus Mode cite validation findings without treating them as evidence or release approval? | NEEDS VERIFICATION | API/UI/AI projection review. |

---

## Related contracts and docs

- `contracts/domains/geology/domain_observation.md` — observation envelope under validation.
- `contracts/domains/geology/domain_feature_identity.md` — identity and `spec_hash` support.
- `contracts/domains/geology/domain_layer_descriptor.md` — layer descriptor validation target.
- `docs/domains/geology/VERIFICATION_BACKLOG.md` — domain-scoped verification register.
- `docs/domains/geology/API_CONTRACTS.md` — governed API invariants and finite outcomes.
- `docs/domains/geology/RELEASE_INDEX.md` — release surface index; not release authority.
- `docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md` — trust-object family separation.
- `schemas/contracts/v1/domains/geology/domain_validation_report.schema.json` — confirmed schema stub, pending expansion.
- `fixtures/domains/geology/domain_validation_report/` — expected fixture home, pending verification.
- `tools/validators/domains/geology/validate_domain_validation_report.py` — schema-declared validator path, pending verification.
- `policy/domains/geology/` — expected policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Expand paired schema with required validation-report fields.
- [ ] Verify or create validator and fixtures referenced by the schema `x-kfm` block.
- [ ] Add tests proving validation reports cannot substitute for EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, PromotionDecision, CorrectionNotice, or RollbackCard.
- [ ] Add anti-collapse tests for modeled/observed, aggregate/per-place, administrative/observed, regulatory/observed, synthetic/observed, occurrence/deposit/estimate, structure/hazards, hydrostratigraphy/hydrology, and AI/evidence failures.
- [ ] Confirm EvidenceRef/EvidenceBundle closure checks before release preflight can pass.
- [ ] Confirm public map/API/UI surfaces use only released public-safe outputs and do not expose raw validation internals by default.
- [ ] Confirm correction, supersession, withdrawal, rollback, and cache invalidation behavior before promotion.
- [ ] Record unresolved schema/validator/finding-enum/release-placement drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
