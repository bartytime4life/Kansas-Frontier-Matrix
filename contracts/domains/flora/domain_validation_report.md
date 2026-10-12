<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-domain-validation-report
title: Domain Validation Report Contract — Flora
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners: OWNER_TBD — Flora steward · Validation steward · Contract steward · Schema steward · Source steward · Sensitivity reviewer · Policy steward · Release steward · Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; semantic-contract; flora; domain-validation-report; validator-output; evidence-bound; policy-aware; sensitivity-aware; no-publication-authority
tags: [kfm, contracts, domains, flora, domain-validation-report, validation, validator-output, evidence, source-role, sensitivity, geoprivacy, rare-plant, policy, release, correction, rollback]
related:
  - ./README.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./plant_taxon.md
  - ./flora_taxon_crosswalk.md
  - ./specimen_record.md
  - ./flora_occurrence.md
  - ./rare_plant_record.md
  - ./vegetation_community.md
  - ./invasive_plant_record.md
  - ./phenology_observation.md
  - ./range_polygon.md
  - ./habitat_association.md
  - ./botanical_survey.md
  - ./restoration_planting.md
  - ./redaction_receipt.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../docs/domains/flora/SENSITIVITY_POSTURE.md
  - ../../../schemas/contracts/v1/domains/flora/domain_validation_report.schema.json
  - ../../../fixtures/domains/flora/domain_validation_report/
  - ../../../tools/validators/domains/flora/validate_domain_validation_report.py
  - ../../../tests/domains/flora/
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../data/registry/sources/flora/
  - ../../../release/manifests/
notes:
  - "Expanded from a greenfield scaffold into a Flora semantic contract for validator-result reporting."
  - "The paired schema is a PROPOSED scaffold with id/version/spec_hash only and additionalProperties=true; field-level machine enforcement remains NEEDS VERIFICATION."
  - "A DomainValidationReport records validation evidence and decision support. It is not source truth, not a policy decision, not a release manifest, and not public publication authority."
  - "Rare-plant exact geometry, steward-controlled records, private-land joins, and culturally sensitive plant knowledge remain fail-closed unless validation, policy, review, redaction, release, and rollback support all resolve."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Validation Report — Flora

> Semantic contract for a Flora `DomainValidationReport`: the auditable report emitted by validation work over Flora observations, features, evidence links, sensitivity states, source-role posture, schemas, fixtures, policy gates, release candidates, and correction/rollback paths.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: domains/flora" src="https://img.shields.io/badge/family-domains%2Fflora-2ea44f">
  <img alt="Type: semantic contract" src="https://img.shields.io/badge/type-semantic__contract-blue">
  <img alt="Schema: proposed scaffold" src="https://img.shields.io/badge/schema-PROPOSED__scaffold-lightgrey">
  <img alt="Boundary: report not release authority" src="https://img.shields.io/badge/boundary-report__not__release__authority-critical">
</p>

`contracts/domains/flora/domain_validation_report.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Finding model](#finding-model) · [Validation families](#validation-families) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/flora/domain_validation_report.md`  
> **Schema path:** `schemas/contracts/v1/domains/flora/domain_validation_report.schema.json`  
> **Truth posture:** the current contract path and paired schema pointer are confirmed from current repo evidence. The complete field model, validator behavior, fixtures, policy runtime, CI integration, release workflow, API behavior, UI behavior, and emitted validation reports remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `DomainValidationReport` records validation results and supports review. It does **not** create source truth, does **not** replace EvidenceBundle, does **not** publish Flora claims, does **not** approve rare-plant exact geometry, and does **not** substitute for PolicyDecision, ReviewRecord, ReleaseManifest, PromotionDecision, CorrectionNotice, or rollback artifacts.

---

## Meaning

`DomainValidationReport` is the Flora lane's semantic object for a bounded validation run, validation pass, dry-run check, release-candidate check, fixture check, schema check, policy preflight, or correction/rollback verification pass.

It answers:

- What Flora objects, layers, files, source rows, fixtures, release candidates, or correction artifacts were checked?
- Which validator, ruleset, schema, policy, fixture pack, source registry entry, and release candidate were used?
- Which evidence, source-role, taxon, geometry, temporal, sensitivity, redaction, rights, release, and rollback checks passed, warned, failed, abstained, or errored?
- Which findings block promotion or publication?
- Which findings are informational and can be reviewed later without weakening public safety?
- Which follow-up artifacts are required before the checked material can move forward?

A validation report is an audit object and review input. It can support a promotion decision, but it is never the promotion decision itself.

---

## Repo fit

The Flora lane follows the responsibility-root pattern: contracts define semantic meaning, schemas define machine shape, validators and tests prove behavior, policy gates exposure, and release roots carry publication state.

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Report meaning | `contracts/domains/flora/domain_validation_report.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/flora/domain_validation_report.schema.json` | Linked only; currently scaffolded |
| Validator implementation | `tools/validators/domains/flora/validate_domain_validation_report.py` | Proposed validator target from schema metadata |
| Fixtures | `fixtures/domains/flora/domain_validation_report/` | Expected valid/invalid examples |
| Tests | `tests/domains/flora/` | Expected contract/schema/policy regression checks |
| Policy inputs | `policy/domains/flora/`, `policy/sensitivity/flora/` | Validation should report policy posture but not replace decisions |
| Source registry | `data/registry/sources/flora/` | Source rights, role, cadence, access, and attribution support |
| Release artifacts | `release/`, `release/manifests/` | Validation reports may support release review but do not publish |
| Flora object contracts | `contracts/domains/flora/*.md` | Validation report may reference any Flora object family under test |
| Public surfaces | governed API/UI/map layers only | Public clients consume released, policy-safe derivatives; not raw validation internals by default |

---

## Schema posture

The paired schema currently exists as a **PROPOSED scaffold**.

| Schema fact | Current posture |
|---|---|
| Schema file path | `schemas/contracts/v1/domains/flora/domain_validation_report.schema.json` |
| Schema title | `domain_validation_report` |
| Declared properties | `spec_hash`, `id`, `version` |
| Required fields | `id` |
| Additional properties | `true` |
| Schema status | `PROPOSED` |
| Contract document | `contracts/domains/flora/domain_validation_report.md` |
| Fixtures root | `fixtures/domains/flora/domain_validation_report/` |
| Validator | `tools/validators/domains/flora/validate_domain_validation_report.py` |
| Policy root | `policy/domains/flora/` |

Because the schema is permissive, this contract defines **semantic expectations** for future schema fields, fixtures, validator outputs, CI checks, policy preflights, release gates, API payloads, and review-console behavior. It does not claim current machine enforcement.

---

## Assertions

A reviewed `DomainValidationReport` should semantically assert:

1. **Run identity** — a deterministic report identity, validation run identifier, validator name, validator version, and ruleset version.
2. **Scope** — the object, file, source batch, fixture pack, candidate release, layer, catalog entry, correction, or rollback target that was checked.
3. **Input integrity** — input artifact refs, source refs, schema refs, policy refs, manifest refs, evidence refs, and hashes used by the run.
4. **Outcome** — finite result such as `PASS`, `WARN`, `FAIL`, `ABSTAIN`, `DENY`, or `ERROR`, with severity counts and blocker status.
5. **Findings** — structured findings with code, severity, path, subject ref, message, evidence, remediation, and promotion impact.
6. **Evidence closure** — whether required EvidenceRef → EvidenceBundle resolution passed for consequential claims.
7. **Source-role posture** — whether observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic source roles were preserved and not silently upgraded.
8. **Flora-specific checks** — taxon, specimen, occurrence, rare-plant, survey, vegetation-community, invasive, phenology, range, habitat, restoration, and redaction checks where applicable.
9. **Sensitivity posture** — whether rare-plant, steward-controlled, private-land, cultural, and source-restricted material is correctly withheld, generalized, redacted, or denied.
10. **Release posture** — whether a candidate is blocked, reviewable, or eligible for a separate release/promotion decision.
11. **Correction posture** — whether correction, supersession, source withdrawal, stale-state, or rollback references resolve.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating validation as source truth | Validation can test a claim or object; it does not create the evidence. |
| Treating validation as policy approval | PolicyDecision remains a separate object family. Validation can report policy status, not replace it. |
| Treating validation as release authority | ReleaseManifest, PromotionDecision, review record, and rollback target remain separate. |
| Publishing sensitive Flora details from report findings | Findings can contain sensitive locations, source IDs, private-land joins, or steward notes and must be redacted/generalized before public exposure. |
| Passing schema shape while ignoring evidence closure | Schema validity alone is insufficient for KFM truth posture. |
| Upgrading source role because validation passed | Source role is preserved; validation does not turn modeled, aggregate, candidate, or synthetic material into observed fact. |
| Direct public access to RAW/WORK/QUARANTINE validation details | Public surfaces must use governed interfaces and released/public-safe summaries only. |
| Treating `WARN` as harmless | Warnings that touch rights, sensitivity, evidence, source role, or release may still block promotion by policy. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not fully enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical validation report identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `flora` for this contract. |
| `report_type` | `schema`, `contract`, `fixture`, `source_registry`, `evidence`, `policy_preflight`, `sensitivity`, `release_candidate`, `correction`, `rollback`, or `composite`. |
| `validation_scope` | Object family, file set, source batch, layer, release candidate, catalog entry, or correction target under test. |
| `subject_refs` | IDs or paths for records/artifacts checked. |
| `validator_ref` | Validator identity or tool path. |
| `validator_version` | Validator package/script/ruleset version or hash. |
| `ruleset_refs` | Schema, contract, policy, fixture, or lint rules used by the run. |
| `schema_refs` | Schema files or IDs evaluated. |
| `policy_refs` | Policy files, sensitivity profiles, or policy decision inputs used. |
| `input_artifact_refs` | Input files, manifests, source batches, fixtures, or release candidates. |
| `input_hashes` | Hashes of checked input artifacts. |
| `run_ref` | Pipeline run, CI run, manual review run, or dry-run identifier. |
| `started_at` / `completed_at` | Validation run timing. |
| `outcome` | Finite top-level outcome: `PASS`, `WARN`, `FAIL`, `ABSTAIN`, `DENY`, or `ERROR`. |
| `promotion_blocking` | Boolean or reason-coded gate indicating whether this report blocks promotion. |
| `severity_counts` | Count of findings by severity. |
| `finding_refs` | Structured finding references or inline finding array. |
| `evidence_resolution_summary` | EvidenceRef/EvidenceBundle closure results. |
| `source_role_summary` | Source-role preservation and anti-collapse checks. |
| `sensitivity_summary` | Rare-plant, steward, private-land, cultural, source-restricted, and public-safe checks. |
| `geometry_summary` | Geometry validity, precision, uncertainty, redaction, generalization, and public-safe support. |
| `taxon_summary` | Taxon/crosswalk/accepted-name/source-name checks. |
| `temporal_summary` | Observed, valid, source, retrieval, release, correction, and stale-state checks. |
| `rights_summary` | Source terms, redistribution, attribution, and access posture checks. |
| `release_summary` | Release candidate, manifest, promotion, and rollback readiness summary. |
| `redaction_receipt_refs` | Redaction/generalization/suppression receipts checked. |
| `correction_refs` | CorrectionNotice, supersession, withdrawal, rollback, or stale-state refs. |
| `public_summary` | Public-safe validation summary with sensitive details removed. |
| `internal_notes` | Restricted reviewer notes; never exposed publicly without policy review. |

---

## Finding model

Findings should be structured enough that maintainers can route them, reviewers can reproduce them, and release gates can consume them.

| Finding field | Meaning |
|---|---|
| `code` | Stable machine-readable finding code, e.g. `FLORA_SENS_EXACT_RARE_PLANT_PUBLIC`. |
| `severity` | `info`, `warning`, `error`, `blocker`, or policy-specific severity. |
| `outcome` | `PASS`, `WARN`, `FAIL`, `ABSTAIN`, `DENY`, or `ERROR` for the finding. |
| `subject_ref` | Object, field path, source row, artifact, layer, fixture, or release candidate affected. |
| `message` | Human-readable summary. |
| `evidence_refs` | Evidence supporting the finding. |
| `policy_refs` | Policy or sensitivity profile involved. |
| `remediation` | Required correction, review, redaction, source update, schema change, or rollback step. |
| `promotion_impact` | `none`, `review_required`, `blocks_release`, `requires_redaction`, `requires_rollback`, or `requires_adr`. |

---

## Validation families

| Family | What the report should test | Promotion impact |
|---|---|---|
| Schema shape | Required fields, types, enums, additional property posture, schema version. | Blocks if required shape fails. |
| Contract semantics | Object meaning, exclusions, invariants, references, downstream ownership. | Blocks or requires review if semantics conflict. |
| Evidence closure | EvidenceRef resolves to EvidenceBundle for consequential claims. | ABSTAIN or block if unresolved. |
| Source role | Source role is present, canonical, and not silently upgraded. | Blocks if source-role anti-collapse fails. |
| Rights and terms | Source terms, attribution, redistribution, access, and license posture. | DENY or block if unclear/forbidden. |
| Sensitivity | Rare-plant, steward-controlled, private-land, cultural, source-restricted material. | DENY/block unless redacted or reviewed. |
| Geometry | Validity, precision, uncertainty, geoprivacy, public-safe generalization. | Blocks sensitive/exact public exposure. |
| Taxonomy | Accepted name, source taxon, crosswalk, conflict, stale taxonomy. | Review/block depending on consequence. |
| Temporal | Observed/source/retrieval/release/correction/stale support. | ABSTAIN or warn/block if time support is insufficient. |
| Release readiness | Release manifest, redaction receipt, review state, rollback target. | Blocks if any release gate is missing. |
| Correction and rollback | Supersession, withdrawal, correction notice, rollback target. | Blocks if rollback target is absent for public release. |
| Privacy/consent | User-contributed, steward-provided, or Focus Mode feedback material where consent is material. | DENY/block when consent or privacy posture cannot be proven. |

---

## Sensitivity and release

A validation report may itself contain sensitive content. A finding can expose the exact location, source row, steward note, private-land join, taxon label, or source restriction that caused the finding.

Rules:

- Public validation summaries must redact exact rare-plant geometry and sensitive source details.
- Internal findings may retain exact values only under governed access.
- A `PASS` result must not be interpreted as publishable unless release, policy, review, redaction, and rollback gates are also satisfied.
- `WARN` results involving rights, sensitivity, evidence closure, source role, or release readiness should default to review-required or blocking until policy confirms otherwise.
- `candidate`, `synthetic`, sensitivity-unknown, rights-unknown, and evidence-incomplete material must not be promoted to public outputs just because structural checks pass.
- Privacy/consent checks must fail closed when validation touches user-contributed notes, Focus Mode feedback, or steward-provided restricted material.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Validation may record source-native errors or intake checks, but RAW material remains source-bound and not public. |
| WORK / QUARANTINE | Validation reports identify normalization, evidence, source-role, rights, sensitivity, and schema issues. Risky material stays quarantined. |
| PROCESSED | Passing reports may support processed objects, but report results remain tied to hashes, rulesets, validator versions, and evidence refs. |
| CATALOG / TRIPLET | Catalog/triplet projections require validation reports that preserve evidence, source role, time, and caveats. |
| RELEASE CANDIDATE | Composite validation reports can support review, redaction checks, release manifest checks, and rollback readiness. |
| PUBLISHED | Only public-safe validation summaries, if any, may be exposed. Full reports may remain internal when findings contain sensitive details. |
| CORRECTION | A failed or superseded validation report should trigger correction, revalidation, rollback, or release suppression as appropriate. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/flora/domain_validation_report.schema.json` beyond the scaffold fields.
- [ ] Add fixtures for passing schema validation, failing schema validation, evidence-closure abstention, rare-plant exact geometry denial, rights-unknown denial, source-role anti-collapse failure, redaction-receipt missing failure, rollback-target missing failure, and public-safe summary output.
- [ ] Add validator checks for run identity, input hashes, ruleset refs, schema refs, policy refs, evidence refs, source-role summaries, finding severity, promotion impact, and sensitive-detail redaction.
- [ ] Add tests proving `PASS` does not equal publication authority.
- [ ] Add tests proving sensitive findings are not emitted into public summaries.
- [ ] Add tests proving `WARN` can block promotion when rights, sensitivity, release, evidence, or source-role risks are present.
- [ ] Add no-network fixtures so CI can validate this contract without live source access.
- [ ] Add correction/rollback revalidation fixtures.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Checks pass and no promotion blocker exists | `PASS` |
| Non-blocking issue exists | `WARN` |
| Required validation check fails | `FAIL` |
| Evidence support is insufficient to validate a consequential claim | `ABSTAIN` |
| Policy/sensitivity/rights condition forbids exposure or promotion | `DENY` |
| Validator, schema, artifact, or runtime failure prevents a trustworthy result | `ERROR` |

---

## Evidence basis

This contract is grounded in these evidence classes:

| Evidence class | Use |
|---|---|
| Current repo scaffold | Confirms the existing contract path and paired schema pointer. |
| Schema metadata | Confirms the schema ID, contract doc link, fixtures root, validator path, policy root, and PROPOSED status. |
| Flora lane path doctrine | Confirms responsibility-root placement for contracts, schemas, policy, fixtures, tests, data, and release paths. |
| Flora object-family doctrine | Confirms the Flora domain surfaces this report may validate. |
| Flora sensitivity posture | Confirms rare-plant and exact sensitive location material require fail-closed, review, redaction/generalization, or denial before public release. |
| KFM lifecycle law | Confirms RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED, with publication as a governed transition. |

---

## Rollback

A validation report should trigger rollback or release suppression when it reveals that a published or release-candidate artifact no longer satisfies evidence, policy, sensitivity, source-role, schema, integrity, or rollback requirements.

Rollback triggers include:

- validator bug or superseded ruleset;
- stale schema or contract mismatch;
- bad input hash or missing manifest;
- unresolved EvidenceBundle for a public claim;
- rare-plant exact geometry leak;
- source terms or rights withdrawal;
- source-role anti-collapse failure;
- public summary contains restricted details;
- missing redaction receipt;
- missing rollback target;
- correction notice or supersession invalidates prior report.

Rollback artifacts should include affected report IDs, subject IDs, release IDs, layer IDs, evidence refs, policy refs, redaction receipts, correction notices, rollback cards, replacement validation reports, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Should `DomainValidationReport` be Flora-specific or a cross-domain base contract with Flora specialization? | NEEDS VERIFICATION | Review with validation steward and contract steward before schema expansion. |
| Which finite outcome vocabulary should be canonical for validation reports? | NEEDS VERIFICATION | Align with runtime envelope and policy outcomes before implementation. |
| Should public validation summaries be emitted at all, or only internal reports plus release receipts? | PROPOSED / NEEDS VERIFICATION | Decide with release steward and UI/API steward. |
| How should CI runs, manual review runs, and pipeline dry-runs share report identity? | NEEDS VERIFICATION | Define run identity and hash strategy in schema/validator PR. |
| Which sensitivity finding codes become blocking by default? | NEEDS VERIFICATION | Resolve in `policy/sensitivity/flora/` with fixtures. |
| How should privacy/consent checks be represented for user-contributed or Focus Mode feedback material? | NEEDS VERIFICATION | Define consent/privacy fields only after governing policy and source registry posture are reviewed. |

---

## Related contracts

- `domain_observation.md` — validation subject for Flora observation-envelope records.
- `domain_feature_identity.md` — validation subject for deterministic identity and cross-source identity posture.
- `plant_taxon.md` and `flora_taxon_crosswalk.md` — validation subjects for taxonomy and crosswalk checks.
- `flora_occurrence.md` — validation subject for occurrence claim readiness.
- `rare_plant_record.md` — validation subject for rare/protected plant sensitivity posture.
- `specimen_record.md` — validation subject for voucher/specimen support.
- `botanical_survey.md` — validation subject for survey effort, method, and completeness context.
- `phenology_observation.md` — validation subject for phenological event checks.
- `vegetation_community.md` — validation subject for community/polygon classification checks.
- `redaction_receipt.md` — validation subject for public-safe transformation proof.

---

## Maintainer checklist

- [ ] Confirm this contract against `docs/domains/flora/CANONICAL_PATHS.md` and `docs/domains/flora/OBJECT_FAMILIES.md`.
- [ ] Expand the schema in a separate schema PR.
- [ ] Add fixtures and validator coverage before any release candidate depends on this report.
- [ ] Add policy tests for exact rare-plant, source-restricted, privacy/consent, and public-summary redaction cases.
- [ ] Confirm CI or pipeline integration only after validator outputs are deterministic and hash-pinned.
- [ ] Confirm public API/UI surfaces do not expose internal sensitive findings.
- [ ] Record any contract/schema/path conflict in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
