<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-domain-validation-report
title: Domain Validation Report Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Sensitivity reviewer
  - OWNER_TBD — Release steward
  - OWNER_TBD — Map/UI steward
  - OWNER_TBD — Docs steward
created: 2026-06-22
updated: 2026-06-22
policy_label: public-with-gates; semantic-contract; habitat; domain-validation-report; validator-output; evidence-bound; source-role-aware; policy-aware; sensitivity-aware; release-gated; no-publication-authority
tags: [kfm, contracts, habitat, domain_validation_report, DomainValidationReport, validation-report, validator-output, evidence-ref, evidence-bundle, source-role, schema, fixtures, policy, sensitivity, geoprivacy, release-candidate, correction, rollback, anti-collapse, map-ui, focus-mode]
related:
  - ./README.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./domain_layer_descriptor.md
  - ./SuitabilityModel.md
  - ./connectivity_edge.md
  - ./corridor.md
  - ./land_cover/observation.md
  - ./land_cover/class_scheme.md
  - ./land_cover/crosswalk.md
  - ./land_cover/change_summary.md
  - ./land_cover/model_run_receipt.md
  - ./land_cover/uncertainty.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/MAP_UI_CONTRACTS.md
  - ../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../docs/domains/habitat/sublanes/suitability.md
  - ../../../docs/domains/habitat/sublanes/connectivity.md
  - ../../../schemas/contracts/v1/domains/habitat/domain_validation_report.schema.json
  - ../../../fixtures/domains/habitat/domain_validation_report/
  - ../../../tools/validators/domains/habitat/validate_domain_validation_report.py
  - ../../../tests/domains/habitat/
  - ../../../policy/domains/habitat/
  - ../../../policy/sensitivity/habitat/
  - ../../../data/registry/sources/habitat/
  - ../../../release/manifests/habitat/
notes:
  - "Expanded from a greenfield scaffold at contracts/domains/habitat/domain_validation_report.md."
  - "The paired schema exists at schemas/contracts/v1/domains/habitat/domain_validation_report.schema.json, but it is still a PROPOSED scaffold that only defines spec_hash, id, and version, requires id, and allows additionalProperties=true; field-level enforcement remains NEEDS VERIFICATION."
  - "A DomainValidationReport records bounded validation findings and decision support. It is not source truth, not an EvidenceBundle, not a PolicyDecision, not a ReviewRecord, not a ReleaseManifest, not a PromotionDecision, not a CorrectionNotice, not a RollbackCard, and not public publication authority."
  - "Habitat validation must preserve source-role anti-collapse, temporal discipline, sensitivity/geoprivacy, evidence closure, release/correction/rollback support, map/UI boundaries, and governed AI finite outcomes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Validation Report — Habitat

> Semantic contract for Habitat `DomainValidationReport`: the auditable report emitted by validation work over Habitat observations, identities, layer descriptors, source roles, schemas, fixtures, model receipts, uncertainty, sensitivity states, policy gates, release candidates, correction notices, and rollback paths.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Object: DomainValidationReport" src="https://img.shields.io/badge/object-DomainValidationReport-blue">
  <img alt="Truth: validation support" src="https://img.shields.io/badge/truth-validation__support-informational">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: report not release authority" src="https://img.shields.io/badge/boundary-report__not__release__authority-critical">
</p>

`contracts/domains/habitat/domain_validation_report.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Validation report vs trust objects](#validation-report-vs-trust-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Finding model](#finding-model) · [Validation families](#validation-families) · [Habitat deny checks](#habitat-deny-checks) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/habitat/domain_validation_report.md`  
> **Schema path:** `schemas/contracts/v1/domains/habitat/domain_validation_report.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` scaffold that defines only `spec_hash`, `id`, and `version`, requires only `id`, and allows `additionalProperties: true`.  
> **Truth posture:** Habitat doctrine supports validation over source descriptors, source roles, object families, geometry, temporal scope, evidence closure, sensitivity/geoprivacy, policy gates, release manifests, rollback drills, map/UI boundaries, and governed AI behavior. Field-level schema enforcement, fixtures, validator implementation, CI integration, policy runtime, release workflow, emitted validation-report examples, API behavior, MapLibre/UI behavior, and Focus Mode behavior remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `DomainValidationReport` records validation results and supports review. It does **not** create source truth, does **not** replace EvidenceBundle, does **not** publish Habitat claims, does **not** approve sensitive exact geometry, and does **not** substitute for PolicyDecision, ReviewRecord, ReleaseManifest, PromotionDecision, CorrectionNotice, or RollbackCard.

---

## Meaning

`DomainValidationReport` is the Habitat lane's semantic object for a bounded validation run, dry-run, schema pass, fixture pass, policy preflight, evidence-closure check, source-role check, sensitivity/geoprivacy check, model-card/receipt/uncertainty check, release-candidate check, correction verification, rollback verification, map/UI preflight, or anti-collapse regression check.

It answers:

- What Habitat objects, observations, identities, layer descriptors, source rows, fixtures, artifacts, release candidates, corrections, or rollback targets were checked?
- Which validator, schema, ruleset, fixture pack, source registry entry, policy posture, EvidenceBundle, catalog closure, or release candidate was used?
- Which source-role, geometry, temporal, sensitivity, rights, evidence, artifact-digest, model-card, model-run receipt, uncertainty, policy, release, map/UI, Focus Mode, correction, and rollback checks passed, warned, failed, abstained, denied, or errored?
- Which findings block promotion or publication?
- Which findings are informational and can be reviewed later without weakening source integrity or public safety?
- Which follow-up artifacts are required before checked material can move through the trust membrane?

A validation report is an audit object and review input. It can support a promotion or review decision, but it is never the decision itself.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Report meaning | `contracts/domains/habitat/domain_validation_report.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/habitat/domain_validation_report.schema.json` | CONFIRMED scaffold; field-level enforcement NEEDS VERIFICATION |
| Validator implementation | `tools/validators/domains/habitat/validate_domain_validation_report.py` | Schema-declared target; implementation NEEDS VERIFICATION |
| Fixtures | `fixtures/domains/habitat/domain_validation_report/` | Expected valid/invalid examples; presence/content NEEDS VERIFICATION |
| Tests | `tests/domains/habitat/` | Expected contract/schema/policy regression checks; coverage NEEDS VERIFICATION |
| Policy inputs | `policy/domains/habitat/`, `policy/sensitivity/habitat/` | Report may cite posture/results; it does not replace decisions |
| Source registry | `data/registry/sources/habitat/` | Source rights, role, cadence, authority, attribution, and activation support |
| Evidence/proof inputs | EvidenceRef/EvidenceBundle/proof/catalog homes — accepted paths NEED VERIFICATION | Report verifies closure but does not become proof |
| Release artifacts | `release/`, `release/manifests/habitat/` | Report may support release review; it does not publish |
| Habitat contracts | `contracts/domains/habitat/*.md`, `contracts/domains/habitat/land_cover/*.md` | Report may validate any Habitat semantic contract or object family |
| Public surfaces | governed API/UI/map layers only | Public clients consume released, policy-safe derivatives, not raw validation internals by default |

---

## Schema posture

The paired schema exists but is intentionally thin.

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/habitat/domain_validation_report.schema.json` |
| Schema status | `PROPOSED` |
| Schema description | Greenfield placeholder; fields to be defined per contract document and ADR |
| Defined properties | `spec_hash`, `id`, `version` |
| Required fields | `id` only |
| Additional properties | `true` |
| Schema-linked fixtures root | `fixtures/domains/habitat/domain_validation_report/` |
| Schema-linked validator | `tools/validators/domains/habitat/validate_domain_validation_report.py` |
| Validator implementation | NEEDS VERIFICATION; schema references the path, but runtime/file behavior was not verified here |

Until the schema is expanded, this contract defines semantics and fixture targets, not field-level enforcement.

---

## Validation report vs trust objects

| Object / artifact | What it owns | Relationship to `DomainValidationReport` |
|---|---|---|
| `DomainValidationReport` | Bounded validation findings, outcomes, checked refs, and remediation requirements. | This contract. |
| `EvidenceBundle` | Evidence support for claims. | Report may validate closure; report is not proof. |
| `PolicyDecision` | Allow/restrict/deny/abstain. | Report may cite outcome; report is not policy. |
| `ReviewRecord` | Steward review and signoff. | Report may support review; report is not review approval. |
| `PromotionDecision` / `ReleaseManifest` | Publication authority. | Report may be prerequisite; report cannot publish. |
| `CorrectionNotice` | Correction/supersession statement. | Report may validate correction; report is not correction. |
| `RollbackCard` | Rollback target and procedure. | Report may test rollback; report is not rollback authority. |
| Source registry row | Source role, rights, cadence, attribution. | Report may validate completeness; report is not the registry. |
| Public tile/popup/AI answer | Delivery or interpretation surface. | Report may check them; they remain downstream carriers. |

---

## Assertions

A reviewed `DomainValidationReport` should semantically assert:

1. **Run identity** — stable report ID, validator identity, ruleset version, schema refs, input refs, output refs, run time, and digest.
2. **Validation scope** — object families, source descriptors, fixtures, release candidates, artifacts, corrections, rollback targets, map/UI cards, or Focus Mode responses checked.
3. **Input closure** — checked input refs and artifact digests are recorded.
4. **Source-role posture** — observed, modeled/model, regulatory/authority, derivative, aggregate, administrative, candidate, synthetic, and context roles were checked for collapse.
5. **Temporal posture** — source, observed, valid, retrieval, release, and correction times were checked where material.
6. **Evidence closure** — EvidenceRefs resolve to EvidenceBundles where consequential claims are present.
7. **Sensitivity posture** — sensitive habitat, occurrence-linked context, rare-species links, stewardship/private context, exact corridor/path geometry, and public-safe transforms were checked.
8. **Policy posture** — policy preflight and deny/abstain/fail-closed outcomes are recorded.
9. **Release posture** — release, correction, rollback, stale-state, cache/style invalidation, and public artifact refs were checked where material.
10. **Finite outcome** — the report records pass/warn/fail/abstain/deny/error at finding level and a summary publication-blocking status.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating report as proof | EvidenceBundle carries proof support. |
| Treating report as policy | PolicyDecision owns allow/restrict/deny/abstain. |
| Treating report as release | ReleaseManifest/PromotionDecision owns publication. |
| Treating report as review approval | ReviewRecord owns steward signoff. |
| Treating clean schema pass as publishable | Evidence, rights, sensitivity, policy, release, correction, and rollback still need closure. |
| Treating missing validator path as implemented | Schema metadata does not prove runtime behavior. |
| Treating warning-only report as safe by default | Warnings need explicit review if material. |
| Treating report as public layer metadata | DomainLayerDescriptor/LayerManifest own public-layer semantics. |
| Treating report as source truth | Source registry/EvidenceBundle/source records carry source truth. |
| Treating AI summary of report as report | AI is interpretive and must cite/abstain/deny. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical validation report ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized digest over report-relevant content. |
| `domain` | Must resolve to `habitat`. |
| `report_kind` | schema, fixture, source-role, evidence, policy, sensitivity, release, correction, rollback, map-ui, focus-mode, aggregate, or accepted enum. |
| `validator_id` | Validator or tool identity. |
| `validator_version` | Validator version or digest. |
| `ruleset_refs` | Ruleset/policy/schema refs used by the run. |
| `schema_refs` | Schemas validated. |
| `contract_refs` | Semantic contracts validated. |
| `fixture_pack_refs` | Fixture packs used. |
| `checked_object_refs` | Habitat object refs checked. |
| `checked_artifact_refs` | Artifacts checked. |
| `checked_artifact_digests` | Digests checked. |
| `source_descriptor_refs` | Source registry rows checked. |
| `evidence_refs` | EvidenceRef links checked. |
| `evidence_bundle_refs` | EvidenceBundle refs checked. |
| `policy_decision_refs` | Policy decisions checked or produced upstream. |
| `review_record_refs` | Review records checked. |
| `release_refs` | ReleaseManifest / PromotionDecision refs checked. |
| `correction_refs` | CorrectionNotice refs checked. |
| `rollback_refs` | RollbackCard refs checked. |
| `model_run_receipt_refs` | Model-run receipts checked. |
| `uncertainty_surface_refs` | Uncertainty support checked. |
| `redaction_receipt_refs` | Redaction/generalization/aggregation receipts checked. |
| `source_role_findings` | Role and anti-collapse findings. |
| `temporal_findings` | Time-dimension findings. |
| `geometry_findings` | Geometry validity/public-safe-geometry findings. |
| `sensitivity_findings` | Sensitivity/geoprivacy findings. |
| `evidence_findings` | Evidence closure findings. |
| `policy_findings` | Policy preflight findings. |
| `release_findings` | Release/correction/rollback findings. |
| `ui_ai_findings` | Map/UI/Evidence Drawer/Focus Mode/AI finite-outcome findings. |
| `summary_outcome` | pass, warn, fail, abstain, deny, error, or blocked. |
| `blocks_promotion` | Boolean or outcome explaining whether promotion is blocked. |
| `required_followups` | Follow-up actions or artifacts required. |
| `run_time` | Validation run time. |
| `reported_by` | Tool, steward, or automation identity; owner verification required. |
| `quality_flags` | Missing evidence, role collapse, rights unknown, sensitivity unresolved, missing release, stale source, validator error, schema gap, fixture gap. |

---

## Finding model

| Finding outcome | Meaning | Promotion posture |
|---|---|---|
| `pass` | Check passed. | May proceed if all material gates pass. |
| `warn` | Non-blocking concern or review note. | Needs steward review if material. |
| `fail` | Check failed. | Blocks promotion until corrected or quarantined. |
| `abstain` | Support insufficient to decide safely. | Blocks public answer/publication. |
| `deny` | Policy or trust invariant forbids the output/path. | Blocks publication; record reason. |
| `error` | Tool/input/environment/schema/source lookup failed. | Blocks until rerun or triaged. |
| `blocked` | Aggregate state: one or more material findings prevent promotion. | No public release. |

> [!IMPORTANT]
> A validation report can be clean for one gate and still block publication overall. For example, a schema pass does not override missing EvidenceBundle, unresolved rights, sensitive exact geometry, missing model receipt, missing uncertainty, or absent rollback target.

---

## Validation families

| Family | Required checks |
|---|---|
| Source descriptor | role, rights, sensitivity, citation, cadence, source time, hash, activation gate. |
| Source-role anti-collapse | observed/modeled/regulatory/aggregate/administrative/candidate/synthetic/derivative/context separation. |
| Object-family schema | object family, contract path, schema refs, required fields, allowed enum values, version. |
| Identity/digest | deterministic ID, `spec_hash`, artifact digests, geometry fingerprints, correction lineage. |
| Temporal | source, observed, valid, retrieval, release, correction times kept distinct. |
| Geometry/spatial | CRS, valid geometry, public-safe geometry role, spatial scope, resolution/scale. |
| Evidence closure | EvidenceRef resolves to EvidenceBundle; claim support exists for consequential statements. |
| Model support | model card, model-run receipt, input/config/output digests, uncertainty surface. |
| Sensitivity/geoprivacy | exact sensitive locations, rare species, occurrence-linked habitat, private/stewardship context, redaction receipts. |
| Policy | allow/restrict/deny/abstain outcome, fail-closed default, policy reason. |
| Release/correction/rollback | release manifest, correction path, rollback target, stale-state, cache/style invalidation. |
| Map/UI/AI | layer badges, Evidence Drawer refs, Focus Mode finite outcome, no tile/popup/AI-as-truth. |

---

## Habitat deny checks

The following conditions should normally produce `deny` or publication-blocking `fail` unless a stronger, reviewed policy path explicitly allows a safer derivative.

| Check | Expected blocking posture |
|---|---|
| Modeled suitability presented as regulatory critical habitat | `deny` |
| Modeled output presented as observed land cover or occurrence truth | `deny` |
| Regulatory designation presented as broader biological fact | `deny` / `abstain` depending request |
| Habitat object claims animal/plant occurrence ownership | `deny` |
| Corridor or connectivity edge presented as observed Fauna movement route | `deny` |
| Habitat corridor presented as Roads/Rail/Trade transport corridor | `deny` |
| Sensitive exact habitat-occurrence join exposed publicly | `deny` |
| Sensitive geometry hidden only by style filter | `deny` |
| Candidate object served through public API/UI | `deny` |
| AI answer reads RAW/WORK/QUARANTINE/candidate material | `deny` |
| Missing EvidenceBundle for consequential claim | `abstain` / `fail` |
| Missing release manifest for public artifact | `fail` |
| Missing rollback target for release candidate | `fail` |

---

## Sensitivity and release

Validation reports may include sensitive findings, restricted source IDs, private stewardship context, or exact geometry references. Public display of validation reports therefore needs the same policy posture as any other Habitat artifact.

Rules:

- Public validation summaries must not expose exact sensitive geometry, private/stewardship-sensitive context, or source-restricted detail.
- Detailed reports may require restricted access, redaction, aggregation, delayed release, or steward-only view.
- Report findings must not leak denied coordinates through error text, screenshots, tile previews, artifact paths, or AI summaries.
- Public release requires EvidenceBundle support, policy decision, review record, release manifest, correction path, and rollback target where material.
- Validation report links in public UI should point to public-safe summaries unless the user has approved access.

---

## Lifecycle

| Phase | Validation-report handling |
|---|---|
| RAW | No validation report creates source truth. Source payloads remain immutable inputs. |
| WORK / QUARANTINE | Validator outputs candidate findings; failed gates record quarantine reasons. |
| PROCESSED | Reports bind checked refs, schemas, rulesets, findings, digests, evidence refs, policy posture, and followups. |
| CATALOG / TRIPLET | Report summaries may be cataloged with EvidenceBundle/proof refs where needed. |
| RELEASE CANDIDATE | Public-safe report summary may support promotion review; full report may remain restricted. |
| PUBLISHED | Only released public-safe report summaries or descriptors appear through governed APIs/UI. |
| CORRECTED / SUPERSEDED | Validator change, schema change, fixture change, source correction, evidence correction, policy update, or release withdrawal triggers supersession or rollback verification. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/habitat/domain_validation_report.schema.json` beyond `id`, `version`, and `spec_hash`.
- [ ] Confirm validator path `tools/validators/domains/habitat/validate_domain_validation_report.py` exists and implements the expected checks.
- [ ] Add valid fixtures for schema pass, fixture pass, source-role pass, evidence-closure pass, policy preflight, sensitivity-redaction pass, release-candidate pass, rollback-drill pass, map/UI preflight, and Focus Mode finite-outcome pass.
- [ ] Add invalid fixtures for modeled-as-regulatory, modeled-as-observed, regulatory-as-biological-truth, sensitive exact public geometry, missing EvidenceBundle, missing policy decision, missing model-run receipt, missing uncertainty, missing release manifest, missing rollback target, candidate public path, tile-as-truth, and AI answer from RAW/WORK.
- [ ] Add tests proving deny/abstain/error outcomes are finite, visible, and cannot be silently converted to pass.
- [ ] Add report redaction tests proving sensitive coordinates and restricted source details cannot leak through public summaries.
- [ ] Add release tests proving public clients consume released report summaries/artifacts only.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| All material checks pass and release/correction/rollback refs resolve | `pass` / may support review |
| Non-blocking findings require steward review | `warn` |
| A material validator check fails | `fail` |
| Support is insufficient to decide safely | `abstain` |
| Policy or trust invariant forbids the path | `deny` |
| Tool/input/schema/source lookup fails | `error` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current target scaffold | Confirms target existed as greenfield scaffold before replacement. | Does not prove contract maturity. |
| Paired schema scaffold | Confirms schema path and current limited schema posture. | Does not prove field-level validation. |
| Habitat README | Confirms lane scope, source-role enum, object families, lifecycle gates, sensitivity, cross-lane rules, map/AI boundaries, and proposed test families. | Some implementation claims remain PROPOSED. |
| Habitat MAP_UI_CONTRACTS | Confirms public viewing products, governed API posture, Evidence Drawer, Focus Mode boundaries, sensitivity-redacted view, trust badges, stale/correction state, and release behavior. | Runtime implementation remains NEEDS VERIFICATION unless inspected separately. |
| Model-vs-observation doc | Confirms observed/modeled/regulatory separation and source-role collapse as publication-class defect. | Role spelling and exact policy/schema enforcement remain NEEDS VERIFICATION. |
| Geology and Flora validation-report contracts | Provide current repo-native semantic-contract pattern for domain validation reports. | They are adjacent-domain patterns, not Habitat implementation proof. |
| User-provided authoring role | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized validation report weakens evidence integrity, hides policy/sensitivity failure, or allows unsupported public promotion.

Rollback triggers include:

- schema, validator, fixture, source registry, ruleset, policy, or release manifest changes invalidate prior findings;
- a report falsely marks pass when EvidenceBundle, policy, release, correction, or rollback support is missing;
- role collapse is missed or downgraded to a warning;
- sensitive exact geometry or restricted source detail leaks in report text, logs, screenshots, paths, or AI summaries;
- public UI exposes full restricted report where only public-safe summary is allowed;
- AI or Focus Mode treats report text as source truth or release authority;
- stale/corrected report remains linked from public layers without correction state.

Rollback artifacts should include affected report IDs, checked object refs, schema refs, validator refs, fixture refs, source refs, artifact refs/digests, EvidenceBundle refs, policy refs, release refs, correction notices, rollback cards, replacement reports, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which fields must be required in `domain_validation_report.schema.json`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| Which Habitat validators actually exist and which checks do they enforce today? | NEEDS VERIFICATION | Tool path and tests inspection. |
| Should public validation reports expose only summaries while full reports remain restricted? | NEEDS VERIFICATION | Policy/release review. |
| Which source-role enum spelling is canonical: `model` or `modeled`; `authority` or `regulatory`? | NEEDS VERIFICATION | Source-role/schema/policy review. |
| Which map/UI/Focus Mode validation findings are required before public map release? | NEEDS VERIFICATION | Map/UI and release fixture review. |
| How should validation-report corrections invalidate public layers, graph projections, vector indexes, and Focus Mode cards? | NEEDS VERIFICATION | Release/runtime/cache invalidation design. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Habitat contracts root.
- [`./domain_observation.md`](./domain_observation.md) — domain observation envelope.
- [`./domain_feature_identity.md`](./domain_feature_identity.md) — deterministic identity and anti-collapse support.
- [`./domain_layer_descriptor.md`](./domain_layer_descriptor.md) — layer/view descriptor support.
- [`./SuitabilityModel.md`](./SuitabilityModel.md) — modeled suitability contract.
- [`./connectivity_edge.md`](./connectivity_edge.md) — derived connectivity contract.
- [`./corridor.md`](./corridor.md) — derived corridor geometry contract.
- [`./land_cover/observation.md`](./land_cover/observation.md) — land-cover observation contract.
- [`./land_cover/model_run_receipt.md`](./land_cover/model_run_receipt.md) — model/run receipt semantics.
- [`./land_cover/uncertainty.md`](./land_cover/uncertainty.md) — uncertainty support semantics.
- [`../../../docs/domains/habitat/README.md`](../../../docs/domains/habitat/README.md) — Habitat lane doctrine.
- [`../../../docs/domains/habitat/MAP_UI_CONTRACTS.md`](../../../docs/domains/habitat/MAP_UI_CONTRACTS.md) — Habitat map/UI trust contract.
- [`../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md`](../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md) — source-role anti-collapse doctrine.
- [`../../../schemas/contracts/v1/domains/habitat/domain_validation_report.schema.json`](../../../schemas/contracts/v1/domains/habitat/domain_validation_report.schema.json) — confirmed scaffold schema, pending expansion.

[Back to top](#top)
