<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/domains/archaeology/review
title: Archaeology Review Policy README
type: readme; directory-readme; domain-policy-sublane; cultural-review-policy-boundary; sensitive-domain
version: v0.2
status: draft; repository-grounded; README-only-direct-lane; generic-review-shape-partial; archaeology-review-enforcement-unestablished; fail-closed; non-authoritative-for-cultural-substance-or-release
owners: OWNER_TBD — Archaeology steward · Review steward · Policy steward · Cultural-review liaison · Named cultural/community authority · Sensitivity reviewer · Rights-holder representative · Consent/revocation steward · Evidence steward · Contract/schema steward · Validator/test steward · Release authority · Correction/rollback steward · Security reviewer · Docs steward
created: 2026-06-15
updated: 2026-07-19
supersedes: v0.1 Archaeology review policy guide
policy_label: restricted-review; policy; archaeology; review; cultural-authority-deferred; consent-live; separation-of-duties; no-public-authority
current_path: policy/domains/archaeology/review/README.md
owning_root: policy/
responsibility: >
  Archaeology-specific review-policy boundary for deciding whether required cultural, steward,
  sensitivity, rights-holder, consent, sovereignty, and release-adjacent review conditions are
  sufficiently explicit, current, independent, evidence-bound, and obligation-preserving for a
  requested action. This lane records policy requirements and repository maturity without
  performing consultation, defining cultural knowledge, storing review or consent records,
  approving release, or treating a schema, fixture, comment, workflow, or receipt as authority.
truth_posture: >
  CONFIRMED target v0.1 README and direct-lane path; bounded repository search surfaced only this
  README under policy/domains/archaeology/review; parent Archaeology policy, Cultural Review
  protocol, sensitivity/publication doctrine, CulturalReview and StewardReview semantic contracts,
  generic ReviewRecord semantic contract, two ReviewRecord schema paths, generic valid/invalid
  fixture family, common schema harness, test-local review-fixture README, review-receipt README,
  release-review parent, promotion-gate review hold, domain-Archaeology readiness hold, and
  dedicated review validator placeholder exist; CulturalReview and StewardReview schemas are
  empty-property permissive PROPOSED scaffolds; schemas/contracts/v1/governance/
  review_record.schema.json is a concrete closed PROPOSED shape while
  schemas/contracts/v1/review/review_record.schema.json is an empty permissive scaffold; the
  governance schema points to a lowercase contract path that is absent while the repository
  semantic contract is contracts/governance/ReviewRecord.md; release/reviews contains guidance
  and an Atmosphere sublane but no governed Archaeology ReviewRecord in the workflow-bounded
  inventory; named consent_receipt, revocation_manifest, cultural_review, and steward_review
  schemas under schemas/contracts/v1/governance were not found at checked paths /
  PROPOSED bounded Archaeology review policy model, reviewer-role and authority matrix, immutable
  policy-input packet, currentness/supersession rules, consent/revocation checks, reason-code and
  obligation families, decision normalization, public-surface controls, validation matrix, review
  separation, correction handling, and reversible implementation sequence /
  CONFLICTED ReviewRecord contract filename casing and schema metadata; competing review schema
  homes; generic ReviewRecord decision vocabulary approve/reject/request_changes versus the richer
  semantic-contract vocabulary and Archaeology review states; generic reviewer_role enum
  steward/reviewer/auditor versus Archaeology's cultural, sensitivity, rights-holder, release, and
  sovereignty roles; generic ReviewRecord schema versus domain CulturalReview/StewardReview
  contracts; documentation references to consent/revocation governance schemas that are absent at
  checked paths; release-review outcome vocabulary versus policy/runtime outcome vocabularies /
  UNKNOWN accepted Archaeology review bundle, evaluator, query interface, policy input schema,
  active reviewer/authority registry, real ReviewRecord/CulturalReview/StewardReview/ConsentReceipt/
  RevocationManifest instances, consultation workflow, consent service, release-review records,
  production consumers, branch-protection significance, monitoring, and runtime enforcement /
  NEEDS VERIFICATION owners and CODEOWNERS, named authority resolution, reviewer identity and
  confidentiality model, canonical review object adapter, schema and contract migration, consent
  scope/expiry/revocation semantics, CARE obligation registry, separation-of-duties matrix,
  deterministic fixtures, no-network tests, policy/runtime parity, public API/UI/map/AI obligation
  handling, correction cascade, cache invalidation, withdrawal, rollback drill, and independent
  cultural and release review.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 89575c9bc5f90efb7b578a57a40a95608deb51b6
  prior_blob: 7bbe921a139999249840885173e4946fcc4deaf7
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  parent_archaeology_policy_blob: 8d03cdb11361739e7ad33214f76a0cfe4836ff9b
  cultural_review_protocol_blob: 2097297fc05b371964e61c3c06481652d33b85b9
  review_record_contract_blob: 9641345d1e5d939dc59687a900e60a563d92c4f0
  governance_review_record_schema_blob: fe2f2223af46481e7fb19b0baa94f62ce9c6c855
  review_family_scaffold_schema_blob: a053448d68e8379b92b12a16e6528275b975433c
  review_record_fixture_readme_blob: fccac522a0c178bb87fdaf3c7d932861a40786da
  common_contract_harness_blob: b04342cc034d7f1cc554e155fdd02d6e972976e6
  review_record_validator_blob: e1aa5fcc4b2da4055eb61276a031512512bcb4ca
  cultural_review_contract_blob: 98511de808d07668ddf9e6364dad3a2804ea8828
  cultural_review_schema_blob: 7f2e1a3f7ef4d6b43ad77614e30803671379636d
  steward_review_contract_blob: 986ce11a30a02cf4025c763182f463c57d1894b0
  steward_review_schema_blob: 4888b5934e6bcfb6d15eae39b8c6b2eefa303f1c
  archaeology_test_local_review_fixture_blob: ae305821f112832d0613e1c5eb190113c89d20f0
  archaeology_review_receipts_readme_blob: 083abe1b8dfa1b8f10f87b72858c2f6ebc0d95be
  release_reviews_readme_blob: d927536c39a2102b1f012007fc8de4facb7abd90
  promotion_gate_workflow_blob: feb8bef88c197bc27a4ed1aa692f72b86f7a9a1f
  domain_archaeology_workflow_blob: 41e377f50ca310eccdc4b716ba8374c4fa8181db
related:
  - ../README.md
  - ../../README.md
  - ../../../../docs/domains/archaeology/CULTURAL_REVIEW.md
  - ../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../docs/domains/archaeology/PIPELINE.md
  - ../../../../docs/domains/archaeology/PRESERVATION_MATRIX.md
  - ../../../../docs/governance/REVIEW_DUTIES.md
  - ../../../../docs/governance/SEPARATION_OF_DUTIES.md
  - ../promotion/README.md
  - ../sensitivity/README.md
  - ../../../../contracts/governance/ReviewRecord.md
  - ../../../../contracts/domains/archaeology/cultural_review.md
  - ../../../../contracts/domains/archaeology/steward_review.md
  - ../../../../schemas/contracts/v1/governance/review_record.schema.json
  - ../../../../schemas/contracts/v1/review/review_record.schema.json
  - ../../../../schemas/contracts/v1/domains/archaeology/cultural_review.schema.json
  - ../../../../schemas/contracts/v1/domains/archaeology/steward_review.schema.json
  - ../../../../fixtures/contracts/v1/governance/review_record/README.md
  - ../../../../tests/schemas/test_common_contracts.py
  - ../../../../tools/validators/validate_review_record.py
  - ../../../../tests/fixtures/domains/archaeology/review/README.md
  - ../../../../fixtures/domains/archaeology/synthetic_steward_review/README.md
  - ../../../../data/receipts/archaeology/review/README.md
  - ../../../../release/reviews/README.md
  - ../../../../release/candidates/archaeology/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/doctrine/ai-build-operating-contract.md
  - ../../../../.github/workflows/promotion-gate.yml
  - ../../../../.github/workflows/domain-archaeology.yml
tags:
  - kfm
  - policy
  - archaeology
  - review
  - cultural-review
  - steward-review
  - review-record
  - cultural-authority
  - sovereignty
  - CARE
  - consent
  - revocation
  - embargo
  - separation-of-duties
  - evidence
  - sensitivity
  - no-network
  - release-gated
  - correction
  - rollback
notes:
  - "This revision changes only policy/domains/archaeology/review/README.md plus the required AI-generated provenance receipt."
  - "No policy rule, schema, contract, fixture payload, test, validator, workflow, review record, consultation note, consent/revocation record, protected payload, evidence object, release artifact, deployment, public route, map layer, or AI behavior is created or modified."
  - "Review records governance and decision support; it does not create cultural authority, evidence closure, policy permission, promotion, release, or publication."
  - "Cultural substance remains deferred to the named authority recorded through governed references; restricted substance does not belong in this README or ordinary logs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `policy/domains/archaeology/review/` — Archaeology Review Policy Boundary

> **One-line purpose.** Define the fail-closed Archaeology policy boundary for deciding whether required cultural, steward, sensitivity, rights-holder, consent, sovereignty, and release-adjacent review conditions are explicit, current, independent, evidence-bound, and obligation-preserving—without making KFM the authority over cultural knowledge or treating review as release permission.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: policy" src="https://img.shields.io/badge/root-policy%2F-blue">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-6E4C1E">
  <img alt="Direct lane: README only" src="https://img.shields.io/badge/direct__lane-README__only-lightgrey">
  <img alt="Generic review shape: partial" src="https://img.shields.io/badge/generic__shape-partial-orange">
  <img alt="Domain enforcement: unestablished" src="https://img.shields.io/badge/domain__enforcement-unestablished-critical">
  <img alt="Default: hold or deny" src="https://img.shields.io/badge/default-HOLD__or__DENY-critical">
</p>

> [!IMPORTANT]
> **A review record is not cultural authority, evidence proof, policy approval, promotion, or release.** It records who or what authority reviewed a bounded subject, under which role and support, with which disposition and obligations. The named authority controls cultural substance where applicable; KFM records and defers.

> [!CAUTION]
> **Current review shapes are not one coherent executable model.** The repository has domain `CulturalReview` and `StewardReview` semantic contracts with permissive empty schemas, a generic `ReviewRecord` semantic contract, a stricter generic governance schema and fixtures, a second permissive review schema, an absent lowercase contract path named by schema metadata, and a dedicated validator that raises `NotImplementedError`.

> [!WARNING]
> **Review details can themselves be sensitive.** Reviewer identities, consultation substance, protected locations, burial or sacred context, community-controlled categories, consent tokens, revocation tokens, objections, restrictions, and authority deliberations must not leak through policy traces, logs, receipts, pull requests, maps, exports, screenshots, embeddings, search indexes, or AI answers.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status-and-repository-evidence) · [Belongs](#what-belongs-here) · [Does not](#what-does-not-belong-here) · [Model](#review-object-model-and-anti-collapse-rules) · [Roles](#reviewer-roles-and-authority) · [Required](#review-required-matrix) · [Inputs](#minimum-review-policy-input) · [Currentness](#review-currentness-supersession-and-revocation) · [Consent](#consent-embargo-waiver-and-revocation) · [CARE](#care-sovereignty-and-named-authority) · [Separation](#separation-of-duties) · [Decisions](#decision-vocabularies-and-normalization) · [Reasons](#reason-codes-and-obligations) · [Public surfaces](#public-surface-and-log-minimization) · [Validation](#validation-tests-and-ci) · [Threats](#threat-and-failure-model) · [Sequence](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Conflicts](#conflict-and-adr-register) · [Open](#open-verification-register) · [Rollback](#maintenance-correction-and-rollback) · [Evidence](#evidence-ledger) · [Changelog](#changelog)

---

## Purpose

`policy/domains/archaeology/review/` is the Archaeology-specific review-policy documentation sublane under KFM's canonical singular `policy/` responsibility root.

Its durable question is:

> Given an explicitly identified Archaeology subject and requested action, are the required human, community, cultural, steward, sensitivity, rights-holder, consent, policy, and release-adjacent review conditions sufficiently resolved to permit the bounded next step—and which obligations remain binding?

A complete implementation behind this README should answer:

1. What subject, claim, candidate, transform, map, release item, correction, or public output is being reviewed?
2. What action and audience are requested?
3. Which review types are required by object family, sensitivity, authority, lifecycle, and materiality?
4. Who or what named authority has authority to control cultural substance?
5. Are reviewer identities, roles, credentials, scopes, and independence established without overexposing personal information?
6. Are source, EvidenceRef/EvidenceBundle, policy, sensitivity, rights, and consent inputs complete?
7. Is each review current, unexpired, unrevoked, unsuperseded, and applicable to this exact version and action?
8. Are conditions, objections, restrictions, embargoes, CARE obligations, and benefit commitments preserved?
9. Are author, reviewer, cultural authority, sensitivity reviewer, rights-holder representative, and release authority separated where required?
10. Can the system emit a bounded machine decision without exposing protected review substance?
11. Can correction, withdrawal, revocation, and rollback invalidate downstream use?
12. Can deterministic no-network tests replay every allow, hold, deny, abstain, escalation, expiry, and revocation path?

### In scope

- determining whether review is required;
- evaluating review-record presence, identity, role, scope, status, currentness, and subject/version binding;
- cultural, steward, sensitivity, rights-holder, consent, sovereignty, and release-adjacent review requirements;
- named-authority and authority-to-control references;
- consent grant, scope, expiry, revocation, embargo, waiver, and retention inputs;
- CARE labels, obligations, benefit commitments, and downstream inheritance;
- separation-of-duties and reviewer-independence checks;
- finite decisions, safe reason codes, and downstream obligations;
- correction, supersession, withdrawal, revocation, and rollback review posture;
- safe public projections of review status without sensitive substance;
- deterministic fixtures, negative tests, policy/runtime parity, and audit expectations.

### Out of scope

- defining the substance of Indigenous, cultural, sacred, burial, oral-history, or community-controlled knowledge;
- deciding who has cultural authority by KFM assertion;
- performing consultation or community engagement;
- creating reviewer credentials, consent, or authority;
- defining object meaning or machine shape;
- storing ReviewRecord, CulturalReview, StewardReview, ConsentReceipt, or RevocationManifest instances;
- storing protected consultation notes, identities, exact locations, consent tokens, or revocation tokens;
- approving promotion, release, publication, or public rendering;
- source admission, evidence creation, or proof closure;
- public API, UI, map, export, search, graph, or AI implementation;
- legal, ethical, tribal, cultural, medical, or regulatory advice.

[Back to top](#top)

---

## Authority level

**Canonical policy responsibility / non-authoritative for cultural substance, evidence, review records, and release.**

| Concern | Authority home | This lane's role |
|---|---|---|
| Review admissibility and required obligations | Accepted lanes under `policy/` | May own reviewed review-gate logic after acceptance. |
| Cultural-review protocol | `docs/domains/archaeology/CULTURAL_REVIEW.md` | Applies governance protocol; does not replace named authority. |
| Cultural substance and authority | Named community, tribe, nation, repository, rights holder, or other controlling authority | KFM records references and defers. |
| Archaeology object meaning | `contracts/domains/archaeology/` | Consumes `CulturalReview` and `StewardReview` meaning. |
| Generic review meaning | `contracts/governance/ReviewRecord.md` or accepted successor | Consumes cross-cutting review semantics. |
| Machine shape | `schemas/contracts/v1/` after conflict resolution | Consumes accepted schemas; README prose is not machine shape. |
| Review and consent instances | Governed `data/receipts/`, restricted stores, and accepted governance/release lanes | Requires references; stores no instances here. |
| Evidence and proof | EvidenceRef/EvidenceBundle and `data/proofs/` | Requires support; cannot create proof closure. |
| Reviewer and authority registry | Accepted control-plane or governance register | Consumes authoritative identities, roles, scopes, and revocation state. |
| Consent and revocation policy | Accepted `policy/consent/`, governance, or domain policy lane | Evaluates live state; does not invent consent. |
| Validation | `tools/validators/` and `tests/` | Policy is validated; validators and tests do not create authority. |
| Promotion and release | `policy/promotion/` and `release/` | Review may be prerequisite; cannot approve transition or publication. |
| Correction, withdrawal, rollback | `release/`, correction contracts, governed runbooks | Review policy can require action; execution remains outside this lane. |
| Public API/UI/map/export/AI | Governed applications and released artifacts | Must preserve decisions and obligations; cannot read internal review stores directly. |
| CI | `.github/workflows/` | Orchestrates checks; a green hold is not review approval. |

### Directory Rules basis

Directory Rules separates:

```text
docs/       human protocol and doctrine
contracts/  semantic meaning
schemas/    machine shape
policy/     admissibility and obligations
tests/      enforceability proof
fixtures/   deterministic examples
tools/      validators and checkers
data/       lifecycle state, receipts, proofs, registries
release/    release, correction, withdrawal, rollback decisions
apps/       governed consuming surfaces
```

This existing path remains under `policy/` because its primary responsibility is deciding whether review prerequisites are satisfied. It must not absorb the cultural-review protocol, semantic contracts, schemas, receipts, reviewer registry, release records, or application code.

### Governing order

When review sources disagree, apply this order:

1. KFM operating law and sensitive-domain invariants.
2. The named authority for cultural/community-controlled substance.
3. Accepted ADRs and governance registers.
4. Accepted consent, sovereignty, rights, and sensitivity decisions.
5. Archaeology cultural-review, sensitivity, and publication doctrine.
6. Accepted semantic contracts and machine schemas.
7. Accepted review policy bundle and input contract.
8. This README.
9. Current scaffolds, examples, filenames, and planning documents.

A lower-ranked artifact must not broaden audience, weaken a restriction, convert silence into consent, or replace the named authority.

[Back to top](#top)

---

## Status and repository evidence

### Confirmed current state

At `main@89575c9bc5f90efb7b578a57a40a95608deb51b6`:

| Surface | Inspected status | Safe conclusion |
|---|---|---|
| `policy/domains/archaeology/review/` | **README-only in bounded search** | Review-policy documentation exists; no direct executable rule surfaced. |
| Parent Archaeology policy | **Draft README** | Deny-by-default obligations are documented; runtime enforcement remains unproved. |
| Cultural Review protocol | **Draft v1.1 doctrine** | Defines governance of who reviews, when, how recorded, and how revoked; not cultural substance or release authority. |
| `CulturalReview` contract | **Rich draft semantic contract** | Domain meaning exists; no automatic consent or release. |
| `CulturalReview` schema | **Empty permissive PROPOSED scaffold** | Does not enforce contract fields. |
| `StewardReview` contract | **Rich draft semantic contract** | Domain steward-review meaning exists; distinct from cultural review. |
| `StewardReview` schema | **Empty permissive PROPOSED scaffold** | Does not enforce contract fields. |
| Generic `ReviewRecord` contract | **Draft semantic contract at `ReviewRecord.md`** | Rich meaning/dispositions documented; casing/path drift exists. |
| Governance `ReviewRecord` schema | **Concrete closed PROPOSED shape** | Requires seven fields; has narrow role and decision enums. |
| Review-family schema | **Empty permissive scaffold at `schemas/contracts/v1/review/`** | Competing schema home; not meaningful enforcement. |
| Generic ReviewRecord fixtures | **One valid + one invalid JSON case** | Provides minimal shape examples. |
| Common schema harness | **Executable pytest module** | Discovers governance schema fixture families. Current run result not established here. |
| Dedicated ReviewRecord validator | **`NotImplementedError` placeholder** | No accepted validator CLI or behavior. |
| Test-local Archaeology review lane | **README-only direct lane** | Rich fixture routing guidance; no direct payload/test implementation established. |
| Reusable steward-review examples | **Placeholder payloads documented** | Filenames `approve.json`/`deny.json` do not prove outcomes. |
| Archaeology review receipt lane | **README documentation** | Proposed process-memory home; no receipt instances or accepted layout established here. |
| Release review lane | **Guidance + Atmosphere sublane in workflow-bounded inventory** | No governed Archaeology release ReviewRecord established. |
| Promotion-gate workflow | **Command-bearing readiness hold** | Confirms no governed release ReviewRecord and validator remains placeholder. |
| Domain-Archaeology workflow | **Command-bearing structural hold** | Does not resolve cultural authority, apply policy, or prove public safety. |
| Consent/revocation governance schemas named by v0.1 | **Not found at checked paths** | Consent/revocation machine closure is not established. |

### Truth labels

| Label | Meaning here |
|---|---|
| `CONFIRMED` | Verified from inspected repository content, exact file reads, or workflow definitions. |
| `PROPOSED` | A review policy design, field, reason code, obligation, test, or migration not accepted as implementation. |
| `CONFLICTED` | Two or more repository surfaces disagree without an accepted resolution. |
| `UNKNOWN` | Not resolved by inspected evidence. |
| `NEEDS VERIFICATION` | Checkable, but insufficiently verified to use as authority. |

### Safe current conclusion

The repository has substantial review doctrine and semantic documentation, a partial generic schema/fixture surface, and explicit CI holds. It does **not** establish:

- an accepted Archaeology review policy bundle;
- a review evaluator or selector;
- complete CulturalReview or StewardReview machine shapes;
- a working dedicated ReviewRecord validator;
- a reviewer or authority registry;
- real cultural consultation, consent, revocation, or review records;
- Archaeology release review records;
- policy/runtime parity;
- release or public-surface adoption.

[Back to top](#top)

---

## What belongs here

This lane may contain:

- Archaeology review-policy source after accepted topology and package conventions exist;
- policy-owned data that maps object families, actions, audiences, sensitivity, and materiality to required review classes;
- review-currentness, supersession, expiry, consent, revocation, embargo, and separation-of-duties rules;
- reason-code and obligation definitions when owned by policy;
- policy bundle manifests or source indexes when the canonical bundle topology is accepted;
- README documentation for the review-policy boundary;
- references to accepted contracts, schemas, fixtures, tests, validators, review records, receipts, and release records;
- correction, withdrawal, and rollback policy requirements.

Every executable rule must state:

- package/query identity;
- accepted input schema and version;
- finite machine outcome mapping;
- safe reason codes;
- obligations;
- default and error behavior;
- policy/bundle version and digest;
- fixture and test coverage;
- review burden;
- correction and rollback behavior;
- public-log minimization requirements.

[Back to top](#top)

---

## What does not belong here

| Material | Correct authority |
|---|---|
| Cultural-review protocol or consultation procedure | `docs/domains/archaeology/` and governed operational runbooks |
| Cultural knowledge, oral history, sacred/burial substance, consultation notes | Named authority and governed restricted stores |
| Semantic contracts | `contracts/governance/`, `contracts/domains/archaeology/` |
| JSON Schemas | `schemas/contracts/v1/` |
| Reviewer/authority/role registry | Accepted control-plane or governance register |
| Consent grants, revocation manifests, tokens, embargo records | Accepted governed data/consent/review record homes |
| Review receipts | `data/receipts/` after layout acceptance |
| EvidenceBundle or proof records | Evidence/proof authority lanes |
| Reusable fixtures | `fixtures/` |
| Executable tests | `tests/` |
| Validator implementation | `tools/validators/` |
| PromotionDecision, ReleaseManifest, correction, withdrawal, rollback records | `release/` |
| Protected Archaeology payloads or exact locations | Restricted lifecycle stores |
| Public API, UI, MapLibre, search, graph, export, or AI code | Governed application/package roots |
| Secrets, credentials, private endpoints, raw identity data | Secret manager or restricted operational systems |

This README must never contain real protected consultation substance, exact locations, consent/revocation tokens, private reviewer details, or restricted rationale.

[Back to top](#top)

---

## Review object model and anti-collapse rules

The review model has distinct object families. They must not silently collapse.

| Object/process | Durable role | Must not become |
|---|---|---|
| `ReviewRecord` | Cross-cutting structured review event | Cultural authority, EvidenceBundle, PolicyDecision, PromotionDecision, or release |
| `CulturalReview` | Domain record for culturally significant review posture | Automatic consent, consultation itself, cultural-knowledge substance, or release |
| `StewardReview` | Domain steward/domain-quality/release-readiness review posture | Cultural review by default, evidence proof, or release |
| Consent grant/receipt | Records scoped permission where applicable | Permanent blanket permission or cultural authority |
| Revocation manifest/event | Withdraws or narrows prior consent/authority/use | Optional advisory that downstream consumers may ignore |
| Rights-holder review | Assesses rights/use/redistribution authority | Cultural review, sensitivity review, or release approval |
| Sensitivity review | Assesses exposure tier and transform obligations | Archaeological truth, cultural authority, or publication |
| Release review | Assesses candidate readiness for release decision | ReleaseManifest or publication |
| `PolicyDecision` | Machine policy result | Human consultation, ReviewRecord, or release |
| `PromotionDecision` | Records governed transition decision | ReviewRecord, ReleaseManifest, or public permission |
| GitHub review/comment | Platform discussion or approval evidence | Complete semantic ReviewRecord |
| CODEOWNERS/branch protection | Platform routing/enforcement | Cultural authority or ReviewRecord semantics |
| Receipt | Process memory | Evidence proof, policy authority, or release |

### Adapter requirement

A future implementation must explicitly define whether:

1. `CulturalReview` and `StewardReview` are domain-specific records that adapt into a generic `ReviewRecord`;
2. they extend a shared review envelope;
3. they remain separate records linked by refs; or
4. another accepted model replaces the current families.

Until accepted, do not serialize one family using another family's schema by convenience.

### Subject binding

Every review used for a trust-bearing action must bind to:

- exact subject identity;
- immutable version/digest where practical;
- requested action;
- audience;
- lifecycle/release state;
- review scope;
- policy/bundle context;
- evidence and source refs;
- expiry/supersession/revocation state.

A review of one version, audience, transform, map, or purpose must not be replayed as approval for another without an explicit governed rule.

[Back to top](#top)

---

## Reviewer roles and authority

### Proposed role classes

| Role | Review responsibility | Boundary |
|---|---|---|
| Archaeology domain steward | Object identity, candidate/site distinction, source role, domain quality | Not cultural authority or release authority by default |
| Cultural-review liaison | Routes review and records process state | Does not substitute for named cultural/community authority |
| Named cultural/community authority | Controls cultural substance within documented scope | Authority must not be invented by KFM |
| Sensitivity reviewer | Exposure tier, redaction/generalization, reverse-inference risk | Does not establish truth or rights by itself |
| Rights-holder representative | Rights, use, redistribution, attribution, restricted-source posture | Does not replace cultural or sensitivity review |
| Consent/revocation steward | Validates consent scope, expiry, revocation, embargo, waiver | Does not grant consent personally unless authorized |
| Evidence reviewer | EvidenceRef/EvidenceBundle support and citation posture | Does not approve policy or release |
| Policy steward | Review-rule, bundle, reason-code, obligation, parity posture | Does not perform substantive cultural review |
| Release authority | Release decision and rollback readiness | Must not be collapsed with author for material sensitive release |
| Correction/rollback reviewer | Corrective scope, affected derivatives, withdrawal, rollback | Does not silently rewrite history |
| Security/privacy reviewer | Identity, log, export, reverse-inference, access controls | Does not replace named cultural authority |

### Authority requirements

A reviewer identity is meaningful only when accompanied by:

- authoritative role assignment;
- scope;
- jurisdiction or subject applicability;
- effective and expiry times where relevant;
- delegation basis;
- independence requirements;
- confidentiality/public-display posture;
- revocation/supersession path.

A display name, GitHub username, email, organization string, or self-asserted role is not sufficient authority by itself.

### Confidentiality

Policy inputs should prefer pseudonymous or controlled reviewer references. Public outputs should expose only the minimum safe role/status information required for transparency. Restricted identities and rationale remain in governed review/receipt stores.

[Back to top](#top)

---

## Review-required matrix

This matrix is **PROPOSED policy design**, not executable authority.

| Subject/action | Minimum review posture | Default when unresolved |
|---|---|---|
| Exact or reverse-engineerable site geometry | Sensitivity + domain + named cultural/rights review where applicable | `DENY` |
| Burial, human remains, sacred or ceremonial context | Named authority + cultural + sensitivity + rights/consent review | `DENY` |
| Restricted oral history or community-controlled narrative | Named authority + scoped consent + cultural review | `DENY` or `ABSTAIN` |
| CandidateFeature promoted toward confirmed-site assertion | Domain steward + evidence review; cultural review when context requires | `HOLD` |
| Remote-sensing, LiDAR, geophysics, or 3D derivative | Domain + sensitivity + reverse-inference review | `HOLD` or `RESTRICT` |
| Collection-security or repository-access detail | Steward + rights + sensitivity review | `DENY` or `RESTRICT` |
| Public-safe geometry transform | Sensitivity review + named profile/receipt + reverse-inference check | `HOLD` |
| Public narrative, label, story, or Focus Mode answer | Evidence + cultural + sensitivity review as applicable | `ABSTAIN`, `DENY`, or `RESTRICT` |
| Release candidate | Required domain/cultural/rights/sensitivity reviews + release authority | `HOLD` |
| Correction, takedown, suppression, withdrawal | Correction reviewer + affected authority roles | Immediate restriction may precede full review |
| Consent expiry or revocation | Consent/revocation authority; downstream invalidation | `DENY` and invalidate |
| Review supersession or withdrawal | Current authorized reviewer/authority | `HOLD` or `DENY` |
| Internal research use | Role/audience/rights/sensitivity review appropriate to access class | `HOLD` |
| Public API/map/export/search/embedding | Trust-membrane review and obligation tests | `DENY` until released |

The most restrictive applicable row wins.

[Back to top](#top)

---

## Minimum review policy input

A future evaluator should receive a complete immutable packet. It must not fetch hidden facts.

```yaml
review_policy_input:
  input_version: "<accepted version>"
  request_id: "<stable id>"
  operation: "<review | promote | render | export | release | correct | withdraw | rollback>"
  audience: "<internal | reviewer | restricted | public>"
  subject:
    ref: "<stable artifact/object/ref>"
    type: "<object family or artifact family>"
    version: "<version>"
    digest: "<sha256 or accepted digest>"
    domain: "archaeology"
    lifecycle_state: "<RAW | WORK | QUARANTINE | PROCESSED | CATALOG | TRIPLET | PUBLISHED>"
  source:
    source_descriptor_ref: "<ref>"
    role: "<role>"
    rights_state: "<resolved state>"
  sensitivity:
    audience_tier: "<T0-T4 or accepted vocabulary>"
    record_rank: "<accepted rank>"
    exact_or_reconstructable_location: true
    protected_categories: []
    transform_profile_ref: "<ref or null>"
    transform_receipt_ref: "<ref or null>"
  authority:
    named_authority_ref: "<ref or null>"
    authority_to_control_ref: "<ref or null>"
    authority_scope: "<scope or null>"
    authority_status: "<current state>"
  consent:
    consent_ref: "<ref or null>"
    scope: "<scope or null>"
    effective_at: "<time or null>"
    expires_at: "<time or null>"
    revocation_ref: "<ref or null>"
    embargo_until: "<time or null>"
    waiver_ref: "<ref or null>"
  evidence:
    evidence_refs: []
    evidence_bundle_refs: []
    resolution_status: "<closed | incomplete | conflicted | unavailable>"
  required_reviews:
    - review_type: "<cultural | steward | sensitivity | rights | evidence | release>"
      required_role: "<role>"
      authority_scope: "<scope>"
      independent_from: []
  supplied_reviews:
    - review_ref: "<ref>"
      review_type: "<type>"
      subject_ref: "<ref>"
      subject_digest: "<digest>"
      reviewer_ref: "<controlled ref>"
      reviewer_role: "<role>"
      authority_ref: "<ref>"
      disposition: "<review disposition>"
      conditions: []
      obligations: []
      reviewed_at: "<time>"
      expires_at: "<time or null>"
      superseded_by: "<ref or null>"
      revoked_by: "<ref or null>"
  policy:
    bundle_id: "<id>"
    bundle_version: "<version>"
    bundle_digest: "<digest>"
    query: "<entrypoint>"
  release:
    candidate_ref: "<ref or null>"
    release_manifest_ref: "<ref or null>"
    rollback_ref: "<ref or null>"
    correction_ref: "<ref or null>"
  requester:
    actor_ref: "<controlled ref>"
    roles: []
  now: "<deterministic evaluation time>"
```

### Required properties

The accepted input contract should enforce:

- no hidden network access;
- exact subject/version/digest binding;
- explicit action and audience;
- explicit named-authority status;
- explicit consent/revocation state;
- explicit required and supplied review classes;
- deterministic evaluation time;
- policy bundle/query/digest identity;
- evidence closure status;
- release/correction/rollback context;
- bounded reviewer identity;
- no protected consultation substance in normal policy input.

Missing required context fails closed.

[Back to top](#top)

---

## Review currentness, supersession, and revocation

A review is usable only when all applicable currentness checks pass.

### Currentness checks

- subject identity and digest still match;
- action and audience remain within scope;
- reviewer role and authority remain valid;
- named authority has not changed or withdrawn delegation;
- review is not expired;
- consent is live and within scope;
- embargo/retention rules permit the requested use;
- no revocation applies;
- no newer review supersedes the supplied record;
- evidence and policy context have not materially changed;
- transform profile and public projection are unchanged;
- reviewer independence remains valid;
- release/correction state has not invalidated the review.

### State transitions

```text
DRAFT
  -> CURRENT
  -> CONDITIONALLY_CURRENT
  -> SUPERSEDED
  -> EXPIRED
  -> REVOKED
  -> WITHDRAWN
  -> INVALID
```

These labels are proposed. An accepted closed vocabulary is required before implementation.

### Supersession rules

- Never mutate prior review history silently.
- New review state must link the prior record.
- The effective current record must be deterministic.
- Contradictory current records fail closed.
- A less restrictive new review cannot override an authority revocation or higher-order restriction.
- Public caches and derivatives must be invalidated when review state becomes more restrictive.

[Back to top](#top)

---

## Consent, embargo, waiver, and revocation

Consent and revocation are **live policy inputs**, not static metadata.

### Consent validity

A consent record is usable only when:

- issuer/authority is verified;
- subject and material scope are explicit;
- purpose and audience are explicit;
- effective and expiry times are valid;
- redistribution, derivative, attribution, retention, and deletion obligations are explicit;
- downstream use remains within scope;
- revocation channel and identifier are known;
- no revocation or superseding restriction applies.

### Revocation behavior

A valid revocation should trigger:

1. fail-closed policy outcome for new use;
2. identification of affected reviews, evidence products, candidates, releases, caches, indexes, exports, embeddings, and AI summaries;
3. public-surface restriction or withdrawal;
4. correction/withdrawal/rollback records;
5. cache and search invalidation;
6. preservation of audit history without protected substance;
7. re-evaluation of dependent reviews and releases;
8. notification to authorized stewards where required.

### Embargo and waiver

- Embargo expiry does not imply automatic public release.
- Waivers must identify authority, scope, rationale, effective/expiry time, and review.
- A waiver must not override non-waivable cultural, legal, rights, safety, or operating-law constraints.
- Missing waiver authority is `DENY` or `HOLD`.
- A local administrative override must not become the normal public path.

### Current repository boundary

The v0.1 README names governance consent/revocation schemas that were not found at the checked paths. This README therefore defines no accepted consent or revocation machine shape.

[Back to top](#top)

---

## CARE, sovereignty, and named authority

### CARE posture

Review policy should preserve:

- Collective Benefit;
- Authority to Control;
- Responsibility;
- Ethics.

Proposed machine obligations may include:

- `care_labels_required`;
- `authority_to_control_required`;
- `benefit_commitments_required`;
- `community_attribution_required`;
- `named_authority_review_required`;
- `downstream_obligation_propagation_required`;
- `revocation_channel_required`.

These identifiers are not accepted registry values until governance approves them.

### Named-authority rule

KFM must not:

- infer cultural authority from geography alone;
- infer consent from silence, public availability, prior publication, or a data license;
- infer a community's position from a single unrelated reviewer;
- translate restricted cultural categories into KFM-owned meaning;
- publish the substance of deliberation as transparency;
- treat a sovereignty label as proof of consent;
- let AI summarize protected review substance.

### Geography and sovereignty overlays

Spatial intersection may signal that review is required. It does not establish:

- authority;
- cultural affiliation;
- ownership;
- consent;
- jurisdiction;
- permission to expose location or cultural substance.

The relevant authority must be resolved through governed records.

[Back to top](#top)

---

## Separation of duties

### Proposed independence matrix

| Action | Author may be sole reviewer? | Additional independent review |
|---|---:|---|
| Non-trust-bearing documentation typo | Possibly, per repository rules | Maintainer review as required |
| Domain interpretation or candidate/site status | No for consequential change | Archaeology steward and evidence reviewer |
| Sensitivity tier or transform change | No | Sensitivity reviewer; named authority where applicable |
| Cultural/community-controlled material | No | Named authority/cultural review |
| Rights or redistribution change | No | Rights-holder representative |
| Consent, waiver, or revocation | No | Authorized consent/revocation role |
| Policy rule or bundle change | No | Policy steward + affected domain/review role |
| Release candidate or public projection | No | Release authority + required domain/cultural/sensitivity roles |
| Correction/withdrawal/rollback | No for material action | Correction/rollback reviewer + affected authority roles |
| Emergency restriction/takedown | May be initiated by authorized operator | Post-action independent review and audit |

### Required checks

- author and reviewer refs are known;
- prohibited role overlap is detected;
- reviewer role and authority scope are valid;
- required distinct reviewers are present;
- self-review exceptions are explicit, narrow, and governed;
- automation is never treated as cultural or rights-holder authority;
- CODEOWNERS routing is not treated as substantive review;
- conditions are resolved before unconditional use;
- review record subject/digest matches the exact artifact.

### Materiality

Materiality should consider:

- exposure of protected location or cultural substance;
- audience expansion;
- sensitivity decrease;
- consent/rights change;
- candidate-to-confirmed change;
- release/publish state;
- policy weakening;
- correction reversal;
- removal of caveats or obligations;
- cross-lane joins that increase inference risk.

[Back to top](#top)

---

## Decision vocabularies and normalization

The repository currently exposes multiple vocabularies.

### Generic governance schema

```text
approve | reject | request_changes
```

### Rich generic semantic contract

```text
approve
approve_with_conditions
request_changes
abstain
deny
escalate
informational
```

### Proposed Archaeology internal review dispositions

```text
REVIEW_NOT_REQUIRED
REVIEW_CURRENT
REVIEW_CURRENT_WITH_CONDITIONS
HOLD_FOR_CULTURAL_REVIEW
HOLD_FOR_STEWARD_REVIEW
HOLD_FOR_SENSITIVITY_REVIEW
HOLD_FOR_RIGHTS_REVIEW
HOLD_FOR_CONSENT
ESCALATE_TO_NAMED_AUTHORITY
DENY_REVOKED
DENY_PROTECTED_EXPOSURE
ERROR_REVIEW_SYSTEM
```

### Canonical outward policy envelope

The accepted shared `PolicyDecision`/runtime boundary must determine the public machine outcome. This README proposes:

| Internal review state | Canonical outward outcome | Obligations |
|---|---|---|
| Review not required and all other gates close | `ANSWER` | Scope and policy refs |
| Required reviews current; no unresolved conditions | `ANSWER` | Review refs and obligations |
| Current with unresolved mandatory conditions | `ABSTAIN` or `DENY` | Hold/condition reason |
| Review missing, expired, superseded, or authority unresolved | `ABSTAIN` or `DENY` | Required review type |
| Consent revoked or protected exposure prohibited | `DENY` | Withdraw/invalidate obligations |
| Reviewer lacks authority or scope | `ABSTAIN` | Escalation obligation |
| Review machinery unavailable or malformed | `ERROR` | Fail closed; no protected output |

### Normalization requirements

- Do not add `HOLD`, `RESTRICT`, or `ESCALATE` to a shared enum without contract/schema governance.
- Preserve internal disposition and outward outcome separately.
- `approve` does not mean release or public answer.
- `approve_with_conditions` must not normalize to unconditional `ANSWER`.
- `request_changes`, `abstain`, `deny`, `reject`, and unresolved escalation block trust-bearing action.
- Unknown values fail closed.
- Normalization must be versioned and tested.

[Back to top](#top)

---

## Reason codes and obligations

These identifiers are **PROPOSED** pending accepted registries.

### Reason-code families

#### Review requirement

- `archaeology.review.required`
- `archaeology.review.type_unknown`
- `archaeology.review.record_missing`
- `archaeology.review.subject_mismatch`
- `archaeology.review.version_mismatch`

#### Authority and identity

- `archaeology.review.named_authority_unresolved`
- `archaeology.review.authority_scope_insufficient`
- `archaeology.review.reviewer_role_invalid`
- `archaeology.review.reviewer_identity_unverified`
- `archaeology.review.independence_failed`

#### Currentness

- `archaeology.review.expired`
- `archaeology.review.superseded`
- `archaeology.review.withdrawn`
- `archaeology.review.revoked`
- `archaeology.review.conflicting_current_records`
- `archaeology.review.context_changed`

#### Consent and obligations

- `archaeology.review.consent_missing`
- `archaeology.review.consent_out_of_scope`
- `archaeology.review.consent_expired`
- `archaeology.review.consent_revoked`
- `archaeology.review.embargo_active`
- `archaeology.review.waiver_invalid`
- `archaeology.review.care_obligation_missing`

#### Evidence, sensitivity, and public safety

- `archaeology.review.evidence_unresolved`
- `archaeology.review.sensitivity_unresolved`
- `archaeology.review.protected_location_risk`
- `archaeology.review.reverse_inference_risk`
- `archaeology.review.transform_receipt_missing`
- `archaeology.review.public_projection_unsafe`

#### System and contract

- `archaeology.review.schema_conflicted`
- `archaeology.review.contract_conflicted`
- `archaeology.review.validator_unavailable`
- `archaeology.review.policy_bundle_unavailable`
- `archaeology.review.policy_error`

### Obligation families

- `cultural_review_required`
- `steward_review_required`
- `sensitivity_review_required`
- `rights_holder_review_required`
- `named_authority_resolution_required`
- `consent_check_required`
- `revocation_check_required`
- `care_obligations_required`
- `separation_of_duties_required`
- `evidence_bundle_required`
- `redaction_or_generalization_required`
- `transform_receipt_required`
- `audience_restriction_required`
- `embargo_required`
- `public_summary_redaction_required`
- `cache_invalidation_required`
- `correction_notice_required`
- `withdrawal_required`
- `rollback_required`
- `official_contact_required`
- `no_public_output`
- `no_indexing`
- `no_embedding`
- `no_ai_summary`

### Safety rules

Reason codes and obligations must:

- avoid protected details;
- be stable and bounded;
- separate machine identifier from restricted rationale;
- identify remediation without leaking substance;
- propagate through policy, promotion, release, and public adapters;
- be preserved in correction and rollback;
- be tested at every consumer.

[Back to top](#top)

---

## Public surface and log minimization

### Public contract

Public clients must receive only released, policy-bounded projections through governed interfaces.

A public review-status projection may expose:

- bounded status such as `review_required`, `review_complete`, `restricted`, `withheld`, or `unavailable`;
- safe reason category;
- public-safe obligations/caveats;
- release and evidence refs safe for the audience;
- correction/stale/withdrawn status;
- official contact or authority redirect where approved.

It must not expose:

- reviewer identity unless explicitly cleared;
- consultation notes or deliberation;
- named objections or restricted rationale;
- exact or reverse-engineerable locations;
- sacred/burial/human-remains detail;
- consent/revocation tokens;
- community-controlled categories;
- private contact data;
- policy internals that facilitate bypass;
- restricted review receipt paths.

### Consumer requirements

| Surface | Required behavior |
|---|---|
| Governed API | Return finite outcome and bounded obligations; never internal review record by default |
| Explorer/MapLibre | Hide/restrict geometry and labels; render safe status/caveat only |
| Evidence Drawer | Show safe support and review-status summary without restricted substance |
| Focus Mode/AI | Answer only from released, evidence-supported, policy-permitted scope; otherwise abstain/deny |
| Search/graph | Exclude restricted review substance and protected relationships |
| Export/download | Re-evaluate audience, review currentness, consent, obligations, and release state |
| Screenshots/print | Preserve restrictions and notices; avoid protected layers |
| Embeddings/vector indexes | Do not ingest restricted review text or protected rationale |
| Caches/CDN | Invalidate on revocation, withdrawal, sensitivity increase, or review invalidation |
| Audit logs | Record refs/status, not protected content or tokens |

### Log minimization

Normal logs should include:

- request ID;
- subject type and controlled ref;
- policy bundle/query/digest;
- outward outcome;
- safe reason codes;
- obligation identifiers;
- review refs as opaque IDs;
- evaluation time;
- error class.

Normal logs should exclude:

- exact coordinates;
- cultural substance;
- consultation text;
- consent/revocation tokens;
- private reviewer data;
- protected authority deliberation;
- raw source or evidence payloads.

[Back to top](#top)

---

## Validation, tests, and CI

### Current validated surfaces

- the generic governance ReviewRecord schema has a closed required-field shape;
- one valid and one invalid generic fixture exist;
- the common schema harness discovers governance fixture families;
- the dedicated ReviewRecord validator file exists but is a placeholder;
- CulturalReview and StewardReview schemas are permissive scaffolds;
- test-local Archaeology review-fixture documentation exists but no direct executable review test was established;
- promotion-gate CI explicitly confirms no governed release ReviewRecord and placeholder review validators;
- domain-Archaeology CI inspects structure but does not resolve cultural authority or apply policy.

### Required test matrix

| Test family | Required cases |
|---|---|
| Schema/contract | Contract/schema path parity, casing, required fields, enums, additional properties |
| Object adapters | CulturalReview↔ReviewRecord and StewardReview↔ReviewRecord mapping or explicit separation |
| Review required | Required/not-required/unknown by object, action, audience, sensitivity |
| Authority | Valid, missing, expired, revoked, out-of-scope named authority |
| Reviewer identity | Valid role, invalid role, unverifiable identity, confidentiality-safe output |
| Subject binding | Matching/mismatching subject ref, version, digest, action, audience |
| Currentness | Current, conditional, expired, superseded, withdrawn, conflicting |
| Consent | Valid, absent, expired, out-of-scope, revoked, embargoed, invalid waiver |
| CARE | Complete/missing obligations; downstream propagation |
| Separation of duties | Valid independent set, author-reviewer collapse, automation-as-authority denial |
| Evidence | Closed EvidenceBundle, missing ref, unresolved bundle, stale/conflicted support |
| Sensitivity | Exact geometry, reverse inference, cultural substance, safe generalized projection |
| Conditions | All resolved, partially resolved, unresolved, changed after review |
| Release | Candidate review, manifest handoff, release authority, correction, withdrawal, rollback |
| Public surfaces | API/UI/map/search/export/cache/AI no-leak and obligation preservation |
| Failure | Missing bundle, invalid schema, unavailable registry, timeout, corrupted record |
| No-network | Deterministic local fixtures; deny unexpected live fetch |
| Replay | Same inputs/time/bundle produce deterministic decision |
| Correction | Revocation/supersession invalidates dependent outputs |

### Required fixtures

Fixtures must be:

- synthetic;
- public-safe;
- deterministic;
- no-network;
- clearly valid, invalid, held, denied, abstained, expired, revoked, superseded, and errored;
- free of real cultural substance and exact locations;
- linked to consuming tests;
- nonempty in positive and negative lanes;
- paired with expected outcomes.

### CI graduation criteria

The review-policy lane may graduate from a readiness hold only when:

1. accepted review semantic model and schema topology exist;
2. dedicated validator or policy input validation is executable;
3. non-vacuous fixtures cover positive and negative cases;
4. policy bundle/query/digest is accepted;
5. evaluator is pinned and no-network testable;
6. policy/runtime parity is tested;
7. reviewer/authority and consent/revocation inputs are governed;
8. separation-of-duties tests are substantive;
9. public consumer obligations are tested;
10. correction, withdrawal, cache invalidation, and rollback are exercised;
11. independent reviewers approve;
12. required check names and rollback are documented.

### What a passing check does not prove

A passing schema, fixture, policy, or workflow check does not prove:

- cultural authority;
- consultation occurred;
- consent;
- archaeological truth;
- evidence closure;
- review independence;
- release approval;
- public safety;
- current production enforcement.

[Back to top](#top)

---

## Threat and failure model

| Threat/failure | Required response |
|---|---|
| Self-asserted cultural authority | Hold/deny; require governed authority ref |
| Automation treated as cultural reviewer | Deny |
| Reviewer identity leaked publicly | Redact/restrict; incident/correction review |
| Review subject changed after approval | Invalidate and re-review |
| Consent revoked after release | Deny new use; withdraw/correct/invalidate caches |
| Review expired but cached public output remains | Mark stale/restrict; invalidate cache |
| Conditions ignored downstream | Deny/restrict; correction and rollback |
| Generic schema accepted as full cultural review | Deny implementation claim |
| Permissive domain schema permits arbitrary fields | Treat as scaffold; no enforcement claim |
| Contract/schema casing drift | Block canonical closure until migration |
| Two review schemas diverge | Fail closed; select via ADR/migration |
| GitHub approval treated as ReviewRecord | Hold unless governed adapter and fields exist |
| CODEOWNERS treated as cultural authority | Deny |
| Review receipt treated as proof | Abstain/deny |
| Review treated as release permission | Hold at release gate |
| Protected rationale written to logs/PR | Remove/restrict; preserve safe audit record |
| Search/embedding indexes restricted review text | Disable, purge, correct, audit |
| Cross-lane join reveals protected association | Deny or generalize; re-review |
| Policy/evaluator unavailable | `ERROR`; no protected output |
| Conflicting current reviews | Hold and escalate |
| Revocation signal unavailable | Fail closed for affected use |

[Back to top](#top)

---

## Smallest sound implementation sequence

### Phase 0 — Governance freeze

- Freeze new executable review rules in this child lane until topology is accepted.
- Do not add real review/consent records to the repository.
- Assign owners and reviewers.
- Inventory all review contracts, schemas, fixtures, tests, validators, policy, receipts, and release records.
- Record contract/schema path and vocabulary drift.

### Phase 1 — Decide object and schema topology

- Decide relationship among `ReviewRecord`, `CulturalReview`, and `StewardReview`.
- Select canonical ReviewRecord contract filename and schema home.
- Migrate or deprecate competing schema safely.
- Define closed review-role, disposition, state, reason-code, and obligation vocabularies.
- Define consent/revocation object authority.
- Record ADR or migration decision.

### Phase 2 — Contracts and schemas

- Update semantic contracts without cultural-substance overreach.
- Implement non-permissive schemas.
- Bind schemas to exact contract/fixture/validator paths.
- Add subject/version/digest, authority, currentness, supersession, conditions, and release refs.
- Add safe public projection contract separately.

### Phase 3 — Fixtures and validators

- Add deterministic valid/invalid/expired/revoked/superseded fixtures.
- Implement dedicated schema/input validators.
- Add adapter tests across review families.
- Add no-network and sensitive-log checks.
- Prevent vacuous fixture success.

### Phase 4 — Policy bundle

- Define accepted input schema.
- Implement default-deny rules.
- Version bundle, query, data, reason codes, and obligations.
- Test normalization to canonical outward outcomes.
- Add CI/runtime parity checks.

### Phase 5 — Governance records and review workflow

- Define reviewer/authority registry and access controls.
- Define consent/revocation service or record flow.
- Implement restricted ReviewRecord receipt/storage path.
- Add review-console or workflow integration without public direct access.
- Test separation of duties and authority revocation.

### Phase 6 — Release and public consumers

- Consume review decisions in promotion/release gates.
- Test public API/UI/map/search/export/cache/AI obligations.
- Implement correction, withdrawal, revocation cascade, and rollback.
- Run independent cultural, sensitivity, rights, security, and release review.
- Promote only through governed release records.

Each phase is independently reversible. Do not collapse generation, review, and release into one unreviewed action.

[Back to top](#top)

---

## Definition of done

This lane is not executable-review complete until:

### Governance

- [ ] Owners and CODEOWNERS are assigned.
- [ ] Named cultural/community authority resolution is governed.
- [ ] Review-role and authority registry is accepted.
- [ ] Separation-of-duties matrix is accepted.
- [ ] Consent, embargo, waiver, expiry, and revocation authority is accepted.

### Contracts and schemas

- [ ] `ReviewRecord` contract filename/path drift is resolved.
- [ ] Competing ReviewRecord schema homes are resolved.
- [ ] CulturalReview/StewardReview adapter relationship is accepted.
- [ ] Non-permissive domain schemas exist.
- [ ] Consent/revocation contracts and schemas exist where required.
- [ ] Review state, disposition, reason, and obligation vocabularies are closed.

### Policy and runtime

- [ ] Accepted policy input schema exists.
- [ ] Review policy bundle/query/digest exists.
- [ ] Default-deny and error behavior are tested.
- [ ] Evaluator is pinned and no-network reproducible.
- [ ] CI/runtime parity is proven.
- [ ] Policy failures expose no protected substance.

### Fixtures and tests

- [ ] Positive and negative fixture sets are nonempty.
- [ ] Review-required, authority, currentness, consent, CARE, and separation tests exist.
- [ ] Expiry, supersession, withdrawal, and revocation tests exist.
- [ ] Public no-leak and log-minimization tests exist.
- [ ] API/UI/map/search/export/cache/AI obligations are tested.
- [ ] Correction and rollback drills pass.

### Release and operations

- [ ] Governed ReviewRecord/CulturalReview/StewardReview flow exists.
- [ ] Restricted storage and access controls are reviewed.
- [ ] Archaeology release-review integration exists.
- [ ] Public consumers use governed interfaces only.
- [ ] Monitoring and correction paths exist.
- [ ] Independent cultural, sensitivity, rights, policy, security, and release review is complete.
- [ ] Generated provenance is human-approved or governed override exists.

[Back to top](#top)

---

## Conflict and ADR register

| Conflict | Current evidence | Required resolution |
|---|---|---|
| ReviewRecord contract casing | Schema points to lowercase absent path; semantic contract is `ReviewRecord.md` | Canonicalize with migration/backlinks |
| Two generic review schema homes | Governance schema is concrete; review-family schema is empty | ADR/migration; no divergent authority |
| Generic vs domain review objects | ReviewRecord, CulturalReview, StewardReview overlap but are not adapted | Define inheritance/link/adapter model |
| Decision vocabularies | Narrow schema vs rich contract vs release-review vs policy/runtime outcomes | Define versioned normalization |
| Reviewer-role vocabulary | Generic enum lacks Archaeology roles | Accepted role registry/schema |
| Domain schemas permissive | CulturalReview/StewardReview allow arbitrary fields | Implement closed shapes |
| Validator maturity | Dedicated ReviewRecord validator is placeholder | Implement or retire declared path |
| Consent/revocation paths | v0.1 named governance schemas absent at checked paths | Decide object families and homes |
| Receipt topology | Archaeology review receipt lane documented; exact layout unaccepted | Receipt ADR/migration |
| Release review topology | Parent guidance, Atmosphere sublane, no Archaeology records | Define domain review handoff |
| Cultural authority | Protocol defers to named authority; runtime registry unknown | Govern authority resolution |
| GitHub/platform review | Platform approval not semantic ReviewRecord | Define adapter or keep separate |
| CARE vocabulary | Obligations documented but registry not accepted | Create accepted vocabulary |
| Review condition handling | No executable conditional-approval path | Contract/schema/policy/test closure |

This documentation revision does not resolve these conflicts by assertion.

[Back to top](#top)

---

## Open verification register

### Repository and placement

- exhaustive direct-lane inventory;
- accepted policy package/query path;
- schema and contract migration state;
- reviewer/authority registry path;
- consent/revocation record homes;
- review receipt layout;
- release-review domain lane;
- CODEOWNERS and branch protection.

### Semantics and authority

- named-authority resolution process;
- reviewer credential, scope, delegation, and revocation model;
- relationship among ReviewRecord, CulturalReview, and StewardReview;
- cultural-review conditions and public summaries;
- CARE obligation registry;
- consent/waiver/embargo/revocation vocabulary;
- confidentiality classification for review records;
- lawful and culturally appropriate retention/deletion.

### Implementation

- dedicated validator behavior;
- policy input schema;
- bundle/evaluator/selector;
- deterministic fixtures and tests;
- policy/runtime parity;
- review-console/workflow integration;
- receipt emission;
- release-gate consumption;
- public obligation handlers;
- monitoring and metrics.

### Correction and rollback

- dependency graph for review invalidation;
- cache/search/embedding invalidation;
- withdrawal/correction record topology;
- rollback drill;
- protected-notice minimization;
- revocation propagation timing;
- restoration and re-review criteria.

Until resolved, narrow the action and fail closed.

[Back to top](#top)

---

## Maintenance, correction, and rollback

### Change discipline

Any material change to this lane should identify:

- policy family and package/query;
- input contract/schema;
- review object model;
- role/authority vocabulary;
- consent/revocation implications;
- reason codes and obligations;
- affected contracts/schemas/fixtures/tests/validators;
- public consumers;
- correction and rollback;
- reviewers and separation;
- migration impact.

### Correction triggers

Correction or withdrawal is required when:

- authority was misidentified;
- reviewer role/scope was invalid;
- self-review violated separation requirements;
- review was applied to the wrong subject/version/action/audience;
- consent was absent, expired, out of scope, or revoked;
- conditions were not met;
- cultural substance or reviewer identity leaked;
- review state was stale, superseded, withdrawn, or contradictory;
- schema/contract/policy behavior was wrong;
- public consumers ignored obligations;
- review receipt or release linkage was corrupted.

### Corrective sequence

1. Restrict affected public and internal use.
2. Identify affected subjects, reviews, decisions, candidates, releases, derivatives, caches, indexes, exports, embeddings, and AI summaries.
3. Preserve safe audit history.
4. Notify authorized stewards/authorities.
5. Emit correction/withdrawal/revocation records.
6. Invalidate unsafe caches and indexes.
7. Restore prior safe state or deny access.
8. Re-run evidence, policy, review, validation, release, and public-surface checks.
9. Record final disposition without protected detail.

### Rollback for this documentation change

Restore prior README blob:

```text
7bbe921a139999249840885173e4946fcc4deaf7
```

Remove the paired generated receipt if this revision is reverted. No policy source, schema, contract, fixture payload, test, validator, workflow, review/consent record, protected payload, evidence object, release object, deployment, public route, map layer, or AI state requires restoration.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Supports | Limitation |
|---|---|---|
| Directory Rules | `policy/` responsibility and root separation | Doctrine, not runtime proof |
| Prior target README | Existing scope and review concepts | Predates current repository maturity |
| Parent Archaeology policy | Deny-by-default domain boundary | Draft; runtime unproved |
| Cultural Review protocol | Named-authority deferral, reviewer roles, consent/revocation governance | Draft doctrine; not consultation or machine enforcement |
| `ReviewRecord` contract | Rich cross-cutting review semantics and anti-collapse rules | Draft; path/casing drift |
| Governance ReviewRecord schema | Concrete closed shape and narrow enums | `PROPOSED`; limited semantics |
| Review-family ReviewRecord schema | Competing path exists | Empty permissive scaffold |
| Generic review fixtures | Minimal positive and negative cases | Only one each; generic |
| Common schema harness | Executable fixture discovery | Current run result not established here |
| Dedicated review validator | Declared validator path exists | Raises `NotImplementedError` |
| CulturalReview contract/schema | Domain cultural-review meaning and paired path | Schema empty/permissive |
| StewardReview contract/schema | Domain steward-review meaning and paired path | Schema empty/permissive |
| Test-local Archaeology review README | Rich routing/conflict analysis | Direct lane README-only |
| Archaeology review receipt README | Process-memory boundary and proposed layout | No instances/layout authority established |
| Release review README | Release-review guidance and outcomes | Not Archaeology review record |
| Promotion-gate workflow | Explicit review-record/validator readiness hold | Does not perform review or release |
| Domain-Archaeology workflow | Explicit domain validation/proof/release holds | Does not resolve authority or apply policy |
| This revision | Repository-grounded policy boundary | Documentation, not implementation or approval |

[Back to top](#top)

---

## Changelog

### v0.2 — 2026-07-19

- Replaced the generic v0.1 guide with a repository-grounded review-policy boundary.
- Added a pinned evidence snapshot and explicit truth-label split.
- Distinguished cultural authority, consultation, review records, policy decisions, promotion, and release.
- Recorded direct-lane README-only maturity.
- Added the generic/domain review object model and adapter requirement.
- Added schema-home, contract-casing, vocabulary, validator, consent/revocation, and release-review conflicts.
- Added reviewer authority, currentness, subject binding, consent/revocation, CARE, and separation-of-duties models.
- Added minimum review-policy input, decision normalization, reason codes, obligations, public-surface controls, no-leak/log minimization, test matrix, threat model, implementation sequence, definition of done, open verification, correction, and rollback.
- Added a generated provenance receipt separately.
- Changed no executable policy, review, consent, release, or public behavior.

### v0.1 — 2026-06-15

- Introduced a bounded Archaeology review-policy sublane.
- Documented review gates, obligations, record expectations, and open verification items.

---

KFM rule: Archaeology review policy may record and evaluate bounded review state, but it never creates cultural authority, consultation, consent, evidence, promotion, release, or public permission. When named authority, review scope, currentness, consent, independence, evidence, sensitivity, or downstream obligation handling is unresolved, the system narrows, holds, abstains, or denies.

<p align="right"><a href="#top">Back to top</a></p>
