<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/domains/archaeology/sensitivity
title: Archaeology Sensitivity Policy README
type: readme; directory-readme; domain-policy-sublane; sensitivity-policy-boundary; sensitive-domain
version: v0.2
status: draft; repository-grounded; README-only-direct-lane; parent-rego-scaffolds-confirmed; transform-and-receipt-shapes-permissive; archaeology-sensitivity-enforcement-unestablished; fail-closed; non-authoritative-for-release
owners: OWNER_TBD — Archaeology steward · Sensitivity steward · Policy steward · Cultural-review liaison · Named cultural/community authority · Rights-holder representative · Consent/revocation steward · Geoprivacy/redaction steward · Evidence steward · Contract/schema steward · Validator/test steward · Release authority · Correction/rollback steward · Security reviewer · Docs steward
created: 2026-06-15
updated: 2026-07-19
supersedes: v0.1 Archaeology sensitivity policy guide
policy_label: restricted-review; policy; archaeology; sensitivity; exact-location-deny; cultural-authority-deferred; named-profile-required; receipt-required; no-public-authority
current_path: policy/domains/archaeology/sensitivity/README.md
owning_root: policy/
responsibility: >
  Archaeology-specific sensitivity-policy boundary for deciding whether a requested lifecycle,
  review, render, export, search, map, graph, tile, screenshot, embedding, Focus Mode, or AI action
  may use a given Archaeology object or derivative. This lane documents classification, exact-detail
  denial, most-restrictive propagation, named-transform requirements, receipt and review obligations,
  consent/revocation/embargo handling, public-surface restrictions, current repository maturity,
  validation expectations, correction, and rollback without storing protected detail, defining
  cultural substance, performing transforms, emitting receipts, approving release, or publishing.
truth_posture: >
  CONFIRMED target v0.1 README and direct-lane path; bounded repository code search at the latest
  indexed snapshot surfaced only this README under policy/domains/archaeology/sensitivity; parent
  Archaeology policy and the merged v0.2 promotion/review sibling READMEs exist; ten domain-level
  Archaeology Rego files were directly read and are six-line PROPOSED generated scaffolds with
  default allow false and no rule bodies; policy/sensitivity/archaeology/README.md was not found at
  the checked path; Archaeology sensitivity, publication, cultural-review, promotion,
  redaction-profile, registry, receipt, fixture, validator, and workflow documentation exists;
  SensitivityTransform and PublicationTransformReceipt have rich semantic contracts but
  empty-property permissive PROPOSED schemas; RedactionReceipt is an empty-property permissive
  PROPOSED schema with no contract_doc and Fauna source docs; the profile catalog at
  policy/redaction/profiles.yaml is a seven-line PROPOSED placeholder sourced from Habitat planning
  material; the sensitive-geometry test-local lane is README-only; named Archaeology tests are
  docstring-only placeholders; the sensitive-geometry validator lane is README-only; the
  domain-Archaeology workflow is an explicit validation/proof/release readiness hold; the shared
  PolicyDecision schema permits ANSWER, ABSTAIN, DENY, and ERROR and includes sensitivity as a family /
  PROPOSED bounded Archaeology sensitivity policy model, immutable policy-input packet,
  classification and transform admission rules, reason-code and obligation families, decision
  normalization, no-leak and reverse-inference controls, review and separation-of-duties model,
  deterministic fixtures, validator and CI graduation criteria, correction handling, and reversible
  implementation sequence /
  CONFLICTED detailed draft Archaeology profile/tier doctrine versus an unpopulated active profile
  catalog; policy/sensitivity/archaeology/ doctrine references versus the missing checked lane; rich
  transform and receipt semantics versus permissive empty schemas; RedactionReceipt doctrine versus
  a Fauna-sourced schema without a semantic contract reference; domain-level six-line Rego stubs
  versus the README child-lane structure; internal ALLOW/RESTRICT/HOLD/QUARANTINE vocabulary versus
  the shared PolicyDecision ANSWER/ABSTAIN/DENY/ERROR envelope and PromotionDecision
  APPROVE/DENY/ABSTAIN vocabulary; draft numeric/profile guidance versus no accepted runtime profile,
  verifier, fixture, receipt emitter, or parity proof /
  UNKNOWN accepted sensitivity bundle, bundle manifest, evaluator, query interface, immutable input
  schema, profile registry consumer, transform implementation, receipt emitter, active reviewer and
  authority registry, consent/revocation service, substantive domain policy tests, runtime/public
  consumers, emitted sensitivity decisions or receipts, branch-protection significance, monitoring,
  and production enforcement /
  NEEDS VERIFICATION owners and CODEOWNERS, canonical relationship between domain and cross-cutting
  sensitivity policy lanes, policy package names, rule composition and precedence, accepted audience
  tier and per-record rank assignments, named Archaeology profile catalog and parameters, registry
  authority, deterministic transform and replay behavior, receipt contract/schema migration,
  cultural/sovereignty/rights review implementation, consent scope/expiry/revocation semantics,
  no-network fixtures, side-channel and reconstruction-risk validators, API/UI/map/search/graph/
  export/cache/embedding/AI obligation handling, correction cascade, cache invalidation, withdrawal,
  rollback drill, and independent release review.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 1e192dcb99682cc6637e90b80a659f1a0a1797e3
  prior_blob: ef2e4add020d2d6ec94bfd0c735f314d13a8151d
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  parent_archaeology_policy_blob: 8d03cdb11361739e7ad33214f76a0cfe4836ff9b
  promotion_policy_readme_blob: 7268ee0f8531887a4c16c0b443f37108e08364c3
  review_policy_readme_blob: daa0139faaddd39931c8810a6fb367eeae153b86
  archaeology_sensitivity_doctrine_blob: ca7888f2d43f022faeef5e1a6e16ab00526cf7aa
  redaction_profiles_standard_blob: 402abcf3e231db1c2ede5ed09d0d373d574e5053
  redaction_profile_catalog_blob: e928e91ccf278fe42ac0cd83f571ba323787573d
  sensitivity_transform_contract_blob: 5de68a7e2223d14128157792fcb415cc66d1cc5f
  sensitivity_transform_schema_blob: f72aa3c4504afa6c2c7ce669ad06fb5de514862e
  publication_transform_receipt_contract_blob: fee559d492c3d0145edc30a7ab39369ae7716dd8
  publication_transform_receipt_schema_blob: 379621207697fb9ad2bd16254cc96f6f7d230aae
  redaction_receipt_schema_blob: 6251119ecc2293cd219e4ddfa5bbde8b9d6f8f24
  sensitivity_receipts_readme_blob: 3c1ac1ac2d2e387f046a234f130f8df0bc54c3b0
  sensitivity_registry_readme_blob: 0a5e708bb2939214fd4843fb13246c508fa0a615
  sensitive_geometry_fixture_readme_blob: 9119f4db4cb42e8ff0d00baad449235a6d392536
  sensitive_geometry_validator_readme_blob: 166d08f780e96396dbcf8690e3b7218d6d74331b
  policy_decision_schema_blob: 1472d26a42c73f17545b4464a275412ffa1d098e
  domain_archaeology_workflow_blob: 41e377f50ca310eccdc4b716ba8374c4fa8181db
  candidate_not_site_policy_blob: f570a241cf5b7512e9512d146f82c18c1ad91b45
  site_policy_blob: 5796f8c1c586bd517c7dbd46f7c577f750a173a3
  exact_location_deny_policy_blob: 37e9d0a624be86ba22a9f1dfa94d99df77b953a8
  sacred_site_deny_policy_blob: 4c6d0500776bf357393f550f49dfc4a09bf4cc80
  burial_human_remains_policy_blob: ef525cb267f009950eb06a27a77a3bc1ffd62071
  looting_risk_deny_policy_blob: 0a76edfec70cb01f1bbae6c40a36739ec00a47a0
  collection_security_deny_policy_blob: dde42b4b4948bae10fe44e10cbd54552a4824541
  oral_history_consent_policy_blob: a5fcf89aaccc771945bab0ea9c99f4a5d1a10c0c
  rights_cultural_review_policy_blob: 01778b7e12851148811cb79544337c44f5eb9207
  ai_exact_location_deny_policy_blob: a5137a8bacddbd7e8015c364175eb4f33d246536
  public_no_leak_test_blob: a980e7db572586cdf2f8e31fae643a841c0f58e1
  candidate_not_site_test_blob: ba8587b1804b97144f31ac13af1cf2d526a11f69
  direct_lane_files_confirmed:
    - policy/domains/archaeology/sensitivity/README.md
  checked_absent_paths:
    - policy/sensitivity/archaeology/README.md
  bounded_inventory_note: >
    Exact path reads and repository code search establish only the inspected snapshot. They do not
    prove permanent absence from history, forks, ignored files, generated workspaces, Git LFS,
    external restricted systems, dynamic policy loading, branch-local changes, or differently
    named artifacts.
related:
  - ../README.md
  - ../promotion/README.md
  - ../review/README.md
  - ../../README.md
  - ../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../docs/domains/archaeology/PRESERVATION_MATRIX.md
  - ../../../../docs/domains/archaeology/CULTURAL_REVIEW.md
  - ../../../../docs/domains/archaeology/MAP_UI_CONTRACTS.md
  - ../../../../docs/runbooks/archaeology/PROMOTION_RUNBOOK.md
  - ../../../../docs/runbooks/archaeology/ROLLBACK_RUNBOOK.md
  - ../../../../docs/standards/SENSITIVITY_RUBRIC.md
  - ../../../../docs/standards/REDACTION_PROFILES.md
  - ../../../../docs/standards/REDACTION_DETERMINISM.md
  - ../../../redaction/profiles.yaml
  - ../../../sensitivity/archaeology/
  - ../candidate_not_site.rego
  - ../site.rego
  - ../exact_location_deny.rego
  - ../sacred_site_deny.rego
  - ../burial_and_human_remains_deny.rego
  - ../looting_risk_deny.rego
  - ../collection_security_deny.rego
  - ../oral_history_consent.rego
  - ../rights_and_cultural_review.rego
  - ../ai_exact_location_deny.rego
  - ../../../../contracts/domains/archaeology/sensitivity_transform.md
  - ../../../../contracts/domains/archaeology/publication_transform_receipt.md
  - ../../../../schemas/contracts/v1/domains/archaeology/sensitivity_transform.schema.json
  - ../../../../schemas/contracts/v1/domains/archaeology/publication_transform_receipt.schema.json
  - ../../../../schemas/contracts/v1/receipts/redaction_receipt.schema.json
  - ../../../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../../../tests/fixtures/domains/archaeology/sensitive_geometry/README.md
  - ../../../../tests/domains/archaeology/test_public_no_leak.py
  - ../../../../tests/domains/archaeology/test_candidate_not_site.py
  - ../../../../tools/validators/sensitive_geometry/README.md
  - ../../../../data/registry/sensitivity/archaeology/README.md
  - ../../../../data/receipts/archaeology/sensitivity/README.md
  - ../../../../data/quarantine/archaeology/exact_geometry/README.md
  - ../../../../release/candidates/archaeology/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/doctrine/ai-build-operating-contract.md
  - ../../../../.github/workflows/domain-archaeology.yml
tags:
  - kfm
  - policy
  - archaeology
  - sensitivity
  - exact-location-deny
  - reverse-inference
  - sensitive-geometry
  - redaction
  - generalization
  - suppression
  - aggregation
  - cultural-review
  - sovereignty
  - CARE
  - consent
  - revocation
  - embargo
  - candidate-not-site
  - named-profile
  - deterministic-transform
  - receipt
  - finite-outcomes
  - no-network
  - release-gated
  - correction
  - rollback
notes:
  - "This revision changes only policy/domains/archaeology/sensitivity/README.md plus the required AI-generated provenance receipt."
  - "No Rego/YAML rule, profile value, numeric threshold, schema, contract, fixture payload, test, validator, workflow, protected record, evidence object, sensitivity registry record, receipt instance, candidate dossier, release artifact, deployment, public route, map layer, search index, cache, embedding, or AI behavior is created or modified."
  - "The draft Archaeology sensitivity doctrine is preserved as doctrine evidence; its tier/rank/profile parameters are not represented as accepted runtime configuration."
  - "Cultural substance and authority remain deferred to the named authority; policy records governance conditions and obligations only."
  - "Exact or reverse-engineerable protected detail must not appear in this README, policy traces, ordinary logs, public fixtures, error messages, generated summaries, or public carriers."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `policy/domains/archaeology/sensitivity/` — Archaeology Sensitivity Policy Boundary

> **One-line purpose.** Define the fail-closed Archaeology policy boundary for classifying sensitivity, denying exact or reverse-engineerable protected detail, requiring accepted deterministic transforms and receipts, preserving cultural and sovereignty obligations, and blocking public use until evidence, review, consent, policy, release, correction, and rollback support close.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: policy" src="https://img.shields.io/badge/root-policy%2F-blue">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-6E4C1E">
  <img alt="Direct lane: README only" src="https://img.shields.io/badge/direct__lane-README__only-lightgrey">
  <img alt="Domain Rego: scaffolded" src="https://img.shields.io/badge/domain__rego-scaffolded-orange">
  <img alt="Profiles: inactive placeholder" src="https://img.shields.io/badge/profile__catalog-placeholder-critical">
  <img alt="Default: hold or deny" src="https://img.shields.io/badge/default-HOLD__or__DENY-critical">
</p>

> [!IMPORTANT]
> **A conservative default is not complete enforcement.** The ten directly inspected Archaeology Rego files all use `default allow := false`, but they contain no rule bodies, immutable input contract, reason codes, obligations, profile lookup, receipt resolution, review checks, evaluator binding, or parity tests. They must not be treated as an active sensitivity system.

> [!CAUTION]
> **The draft sensitivity doctrine is richer than the implementation.** It describes audience tiers, per-record ranks, named profiles, review, consent, revocation, receipts, and public-safe transforms. The current profile catalog is only a generic placeholder; transform and receipt schemas are permissive; the cross-cutting Archaeology sensitivity lane is absent at the checked path; and the domain tests and validator lane are scaffolds.

> [!WARNING]
> **Protected detail includes inference channels.** Exact coordinates are only one leakage path. Bounds, extents, tile coverage, feature counts, stable identifiers, graph edges, labels, screenshots, search results, cache keys, errors, model prompts, embeddings, temporal clues, derivative intersections, and generated descriptions can also reveal or narrow restricted places or cultural context.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level-and-directory-rules-basis) · [Status](#status-and-repository-evidence) · [Belongs](#what-belongs-here) · [Does not](#what-does-not-belong-here) · [Model](#sensitivity-model-and-anti-collapse-rules) · [Topology](#policy-topology-and-composition) · [Inputs](#minimum-sensitivity-policy-input) · [Classification](#classification-and-most-restrictive-wins) · [Profiles](#transform-profile-admission) · [Geometry](#exact-detail-public-safe-derivatives-and-inference-risk) · [Culture](#cultural-sovereignty-care-rights-and-consent) · [Decisions](#decision-vocabularies-and-normalization) · [Reasons](#reason-codes-and-obligations) · [Receipts](#transform-receipt-registry-evidence-and-release-boundaries) · [Public surfaces](#public-surface-and-log-minimization) · [Validation](#validation-tests-and-ci) · [Threats](#threat-and-failure-model) · [Sequence](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Conflicts](#conflict-and-adr-register) · [Open](#open-verification-register) · [Rollback](#maintenance-correction-and-rollback) · [Evidence](#evidence-ledger) · [Changelog](#changelog)

---

## Purpose

`policy/domains/archaeology/sensitivity/` is the Archaeology-specific sensitivity-policy documentation sublane under KFM's canonical singular `policy/` responsibility root.

Its durable question is:

> Given an explicitly identified Archaeology subject, derivative, audience, requested action, source role, evidence state, sensitivity classification, cultural and rights context, transform state, receipt state, review state, consent state, release state, and rollback context, may the action proceed—and which obligations must remain binding downstream?

A complete implementation behind this README should answer at least:

1. What exact subject, version, digest, and lifecycle state is being evaluated?
2. Is the subject a candidate, confirmed assertion, source record, collection record, observation, transform, receipt, map layer, release candidate, or public derivative?
3. Which audience and action are requested?
4. Which sensitivity rubric applies, and are audience tier and per-record rank kept distinct?
5. Does the subject or any derivative expose exact, narrowable, or reverse-engineerable protected detail?
6. Which source, rights, cultural, sovereignty, CARE, consent, revocation, and embargo constraints apply?
7. Is an accepted named and versioned transform profile required?
8. Has the transform actually run against the correct immutable input?
9. Does a resolvable receipt bind input, output, profile, policy, review, evidence, and lineage?
10. Are required sensitivity, cultural, rights-holder, and release reviews current and independent?
11. Does the EvidenceRef resolve to the support required for the claim-bearing output?
12. Is the requested carrier downstream of an accepted release with correction and rollback support?
13. Can every downstream consumer enforce the obligations without receiving protected internals?
14. Has any correction, withdrawal, revocation, embargo, or policy change invalidated the result?

If those questions cannot be answered safely, the policy narrows, holds, abstains, quarantines, or denies. It does not infer safety from file location, schema validity, a profile name, a map style, a generalized-looking display, a green workflow, or prior publication.

### In scope

- Archaeology-specific sensitivity classification policy.
- Exact-detail, reverse-inference, collection-security, sacred-site, burial/human-remains, looting-risk, and restricted-cultural-material denial.
- Candidate-versus-confirmed and source-role preservation where sensitivity depends on meaning.
- Most-restrictive inheritance across joins and derivatives.
- Named profile admission and transform prerequisites.
- Receipt, evidence, review, consent, release, correction, and rollback obligations.
- Public API, map, tile, search, graph, screenshot, export, cache, embedding, Focus Mode, Evidence Drawer, and AI restrictions.
- Safe reason codes and downstream obligations.
- Deterministic fixture, validator, test, and CI requirements.
- Correction, revocation, withdrawal, supersession, and rollback triggers.

### Out of scope

- Defining the substance of cultural or community-controlled knowledge.
- Storing exact locations, restricted identifiers, consultation substance, consent tokens, or profile secrets.
- Choosing or activating numeric transform parameters in documentation.
- Executing redaction, generalization, suppression, aggregation, or differential privacy.
- Defining semantic contract meaning or JSON Schema shape.
- Emitting receipts, EvidenceBundles, ReviewRecords, release objects, or public artifacts.
- Performing consultation or granting cultural, legal, rights-holder, or release authority.
- Implementing public APIs, UIs, maps, tiles, search indexes, graphs, exports, caches, embeddings, or AI adapters.
- Treating a public-safe derivative as proof of the underlying claim.

[Back to top](#top)

---

## Authority level and Directory Rules basis

### Responsibility-root decision

Directory Rules assigns admissibility and obligation logic to the singular `policy/` root. The requested file therefore remains correctly placed at:

```text
policy/domains/archaeology/sensitivity/README.md
```

The domain is a segment beneath the responsibility root. No new root is created.

### Authority split

| Responsibility | Owning root or lane | This README's relationship |
|---|---|---|
| Sensitivity doctrine and human guidance | `docs/domains/archaeology/`, `docs/standards/` | Interprets and cross-references; does not replace doctrine |
| Archaeology admissibility | `policy/domains/archaeology/` | Parent domain policy family |
| This sublane | `policy/domains/archaeology/sensitivity/` | Archaeology-specific sensitivity-policy boundary |
| Cross-cutting sensitivity policy | `policy/sensitivity/` | Shared composition candidate; Archaeology child path needs resolution |
| Profile catalog | `policy/redaction/` | Named-profile authority only after accepted population and review |
| Object meaning | `contracts/` | Semantic contracts; not executable policy |
| Machine shape | `schemas/contracts/v1/` | JSON Schema; not policy or release |
| Reusable fixtures | `fixtures/` | Synthetic inputs; never protected source material |
| Tests | `tests/` | Enforceability proof; not authority |
| Validators | `tools/validators/` | Deterministic checks; not policy discretion |
| Registry/control state | `data/registry/` | Pointers and review state; not policy or payload truth |
| Receipts/process memory | `data/receipts/` | What ran; not proof, policy, or release |
| Evidence/proof | `data/proofs/` and EvidenceBundle lanes | Claim support; not sensitivity permission alone |
| Lifecycle records | `data/raw|work|quarantine|processed|catalog|triplet|published/` | Governed artifacts by state |
| Candidate/release/correction/rollback | `release/` | Release authority and reversible public state |
| Public clients | governed API and released artifacts | Consume obligations; never direct policy/internal-store access |

### No parallel authority

This README must not become:

- the active profile catalog;
- the redaction-transform implementation;
- a receipt schema or receipt store;
- the sensitivity registry;
- an EvidenceBundle or proof store;
- a review or consent record store;
- release approval;
- a public route;
- a repository for exact geometry or restricted cultural substance.

### Directory Rules conflicts to preserve

The current repository carries both a domain-specific sensitivity sublane and documentation references to a cross-cutting `policy/sensitivity/archaeology/` lane. The cross-cutting README was not found at the checked path. This revision does not decide whether the final implementation uses:

1. only the domain lane;
2. only a cross-cutting lane with domain data;
3. domain rules composed with shared sensitivity helpers; or
4. another ADR-approved arrangement.

That composition decision must be explicit, testable, versioned, and free of duplicate authority.

[Back to top](#top)

---

## Status and repository evidence

### Safe conclusion

At `main@1e192dcb99682cc6637e90b80a659f1a0a1797e3`:

- the direct `policy/domains/archaeology/sensitivity/` lane is README-only in bounded search;
- ten Archaeology Rego files exist one directory above this sublane;
- every one of those ten files was directly read and is a six-line generated `PROPOSED` scaffold with `default allow := false`;
- none of those files contains a rule body, profile lookup, reason-code output, obligation output, receipt check, review check, evidence check, consent check, release check, or evaluator binding;
- `policy/sensitivity/archaeology/README.md` was not found at the checked path;
- `policy/redaction/profiles.yaml` exists only as a generic seven-line `PROPOSED` placeholder sourced from Habitat planning material;
- Archaeology `SensitivityTransform` and `PublicationTransformReceipt` semantic contracts exist, but their paired schemas have no properties and allow arbitrary properties;
- the checked `RedactionReceipt` schema likewise has no properties, no semantic contract reference, and cites Fauna source documents;
- the sensitivity registry and receipt lanes are documentation/control boundaries, not populated authority established by this inspection;
- the sensitive-geometry test-local lane is README-only;
- the directly checked Archaeology `test_public_no_leak.py` and `test_candidate_not_site.py` files contain only placeholder docstrings;
- the sensitive-geometry validator lane is documentation-only;
- the domain-Archaeology workflow explicitly holds validation, proof, and release readiness;
- the shared `PolicyDecision` schema includes `sensitivity` as a policy family and permits only `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`.

### Maturity matrix

| Surface | Confirmed repository state | Safe interpretation |
|---|---|---|
| This sublane | README-only in bounded search | Policy boundary exists as documentation only |
| Parent Archaeology policy | v0.1 domain boundary plus generated Rego scaffolds | Intended policy families are visible; execution is not established |
| Promotion sibling | Repository-grounded v0.2 | Shared shape validation is distinguished from domain enforcement |
| Review sibling | Repository-grounded v0.2 | Cultural authority and review-model conflicts are explicit |
| Archaeology sensitivity doctrine | Rich draft catalogue | Doctrine evidence, not accepted runtime configuration |
| Redaction profile standard | Rich draft standard | Defines invariants; catalog and verifier adoption remain unverified |
| Profile catalog | Seven-line generic placeholder | No active Archaeology profile is established |
| Domain Rego inventory | Ten six-line `PROPOSED` scaffolds | Conservative default only; no substantive decision logic |
| Cross-cutting Archaeology sensitivity lane | README absent at checked path | Composition and ownership unresolved |
| `SensitivityTransform` contract | Rich draft meaning | Not a transform implementation or policy decision |
| `SensitivityTransform` schema | Empty permissive scaffold | No field-level enforcement |
| `PublicationTransformReceipt` contract | Rich draft meaning | Not an emitted receipt or release approval |
| `PublicationTransformReceipt` schema | Empty permissive scaffold | No field-level enforcement |
| `RedactionReceipt` schema | Empty permissive scaffold, no contract ref | Does not close receipt semantics |
| Sensitivity registry README | Draft control-state boundary | No concrete record inventory established |
| Sensitivity receipt README | Draft process-memory boundary | No emitted receipt inventory established |
| Sensitive-geometry fixture lane | README-only direct lane | No substantive fixture corpus established there |
| Named domain tests | Placeholder docstrings | No executable public-no-leak or candidate/site proof |
| Sensitive-geometry validator lane | README-only | No executable validator established |
| Domain workflow | Explicit readiness holds | Green structure is not sensitivity approval or release |
| Runtime/public consumers | UNKNOWN | No production enforcement claim is made |

### Ten directly verified Rego scaffolds

| File | Intended concern | Current executable content |
|---|---|---|
| `site.rego` | Site-family policy | Package declaration + `PROPOSED` comment + `default allow := false` |
| `candidate_not_site.rego` | Candidate/site anti-collapse | Same scaffold pattern |
| `exact_location_deny.rego` | Exact-location denial | Same scaffold pattern |
| `sacred_site_deny.rego` | Sacred-site denial | Same scaffold pattern |
| `burial_and_human_remains_deny.rego` | Burial/human-remains denial | Same scaffold pattern |
| `looting_risk_deny.rego` | Looting-risk denial | Same scaffold pattern |
| `collection_security_deny.rego` | Collection-security denial | Same scaffold pattern |
| `oral_history_consent.rego` | Oral-history consent | Same scaffold pattern |
| `rights_and_cultural_review.rego` | Rights/cultural-review gate | Same scaffold pattern |
| `ai_exact_location_deny.rego` | AI exact-location denial | Same scaffold pattern |

A default-false result can prevent accidental allow if the caller queries that exact value correctly. It does not prove that callers use the correct package/query, distinguish denial from evaluator failure, attach safe reasons and obligations, resolve dependencies, or enforce the result across runtime and public surfaces.

### Truth labels used here

| Label | Meaning |
|---|---|
| `CONFIRMED` | Directly verified from the pinned repository, file contents, or attached governing evidence |
| `PROPOSED` | A design or requirement not accepted as implemented authority |
| `UNKNOWN` | Not resolved by the bounded inspection |
| `NEEDS VERIFICATION` | Checkable but not verified enough to act as fact |
| `CONFLICTED` | Sources or repository surfaces disagree without an accepted resolution |

[Back to top](#top)

---

## What belongs here

This sublane may contain, after governance acceptance:

- Archaeology-specific sensitivity policy modules.
- A sublane README and policy-package documentation.
- Domain composition rules that call accepted shared sensitivity helpers.
- Classification and obligation rules for Archaeology object families.
- Exact-detail and reverse-inference denial rules.
- Most-restrictive inheritance rules for joins and derivatives.
- Accepted named-profile selection rules.
- Consent, revocation, embargo, cultural-review, and rights-holder prerequisites expressed as policy inputs.
- Public-surface admissibility rules.
- Safe reason-code and obligation mapping.
- Versioned bundle manifests or pointers when the accepted policy topology assigns them here.
- Policy-local fixtures only when they are explicitly distinct from reusable and test-local fixture roots.

Every executable child must identify:

- policy package and query;
- input contract;
- finite output contract;
- reason-code vocabulary;
- obligation vocabulary;
- shared helper dependencies;
- profile registry dependency;
- evidence, review, consent, receipt, and release dependencies;
- tests and fixtures;
- bundle identity/version/digest;
- rollback and supersession path.

[Back to top](#top)

---

## What does not belong here

| Material | Correct authority home |
|---|---|
| Sensitivity doctrine and profile explanations | `docs/domains/archaeology/`, `docs/standards/` |
| Cultural knowledge substance or consultation notes | Named authority and governed restricted records |
| Exact or reverse-engineerable protected geometry | Restricted lifecycle stores; never ordinary repo documentation |
| Semantic object meaning | `contracts/` |
| JSON Schema | `schemas/contracts/v1/` |
| Active profile data unless topology selects this lane | Accepted `policy/redaction/` or ADR-selected catalog |
| Transform implementation | Approved package/tool/pipeline root |
| Reusable fixtures | `fixtures/` |
| Test-local fixtures | `tests/fixtures/` where documented |
| Executable tests | `tests/` |
| Validators | `tools/validators/` |
| Sensitivity registry records | `data/registry/sensitivity/` |
| Transform and policy receipts | `data/receipts/` |
| EvidenceBundle and proof material | `data/proofs/` and evidence roots |
| Source, work, quarantine, processed, catalog, triplet, or published payloads | Corresponding `data/` lifecycle roots |
| Review, consent, or revocation record instances | Governed review/consent/receipt stores |
| Release candidates, manifests, decisions, corrections, withdrawals, rollback cards | `release/` |
| Public API, map, UI, tile, search, graph, export, cache, embedding, or AI code | Governed app/package roots |
| Secrets, private endpoints, profile salts, sensitive seeds, restricted identifiers | Secret manager or restricted operational system |

[Back to top](#top)

---

## Sensitivity model and anti-collapse rules

### Separate object families

The following must remain distinct:

```text
Sensitivity classification
!= sensitivity policy decision
!= transform profile
!= transform implementation
!= transformed output
!= transform receipt
!= sensitivity registry record
!= ReviewRecord
!= EvidenceBundle
!= PromotionDecision
!= ReleaseManifest
!= public carrier
```

### Two rubrics, two questions

The current draft doctrine uses:

- **audience tier** to answer who may see a released artifact and under what controls;
- **per-record sensitivity rank** to answer how sensitive the source or individual record is before transformation.

They must not be collapsed into one field or inferred from one another without an accepted mapping.

A public-safe output can have a less restrictive audience posture than its source only after a governed transform, receipt, review, evidence, policy, and release path closes. The source record's sensitivity and restrictions remain intact.

### Draft doctrine versus runtime authority

The current Archaeology sensitivity document labels certain protected classes at the most restrictive end of its draft tier/rank models and states that no transform makes some classes openly releasable. This README preserves that deny-by-default doctrine.

It does **not** activate:

- a numeric threshold;
- a geometry cell size;
- a jitter radius;
- an aggregation count;
- a differential-privacy budget;
- a k-anonymity parameter;
- a profile name;
- a consent-token mechanism;
- a sovereignty overlay rule;
- a runtime tier mapping.

Those require accepted machine policy, profile records, fixtures, validators, reviews, and parity checks.

### Anti-collapse invariants

| Invalid collapse | Required posture |
|---|---|
| Candidate or anomaly → confirmed site | Deny the upgrade without evidence and review |
| Exact/internal geometry → public geometry | Deny; public geometry must be a separate governed derivative |
| Map style hiding → redaction | Deny; style is not a transform |
| Coarse-looking display → safe release | Hold until the immutable output and receipt are verified |
| Transform profile name → transform execution | Hold; verify actual run and output hashes |
| Receipt → policy approval | Hold; receipt records process memory only |
| Schema pass → safe publication | Hold; shape is not sensitivity, evidence, review, or release |
| Review → consent | Deny unless a governed consent object explicitly grants scope |
| Prior publication → continuing permission | Re-evaluate current rights, consent, sensitivity, and revocation |
| Cultural review → KFM cultural authority | Deny the authority claim; defer substance to named authority |
| Aggregate → non-sensitive by definition | Re-evaluate reconstruction, small-group, join, and side-channel risk |
| Remote-sensing/3D derivative → harmless context | Treat as sensitivity-bearing and candidate-only until governed |
| Public layer → evidence | Preserve EvidenceBundle separation |
| AI summary → proof or safe disclosure | Require governed evidence and sensitivity decision; otherwise abstain/deny |
| Watcher/workflow success → publication | Watchers remain non-publishers |

[Back to top](#top)

---

## Policy topology and composition

### Current topology

```text
policy/domains/archaeology/
├── README.md
├── sensitivity/
│   └── README.md
├── promotion/
│   └── README.md
├── review/
│   └── README.md
├── site.rego
├── candidate_not_site.rego
├── exact_location_deny.rego
├── sacred_site_deny.rego
├── burial_and_human_remains_deny.rego
├── looting_risk_deny.rego
├── collection_security_deny.rego
├── oral_history_consent.rego
├── rights_and_cultural_review.rego
└── ai_exact_location_deny.rego
```

The bounded search established only this README inside the direct `sensitivity/` child lane.

### Shared lanes referenced by doctrine

```text
policy/sensitivity/archaeology/   # checked README absent
policy/redaction/profiles.yaml    # generic placeholder
policy/consent/archaeology/       # NEEDS VERIFICATION
policy/release/archaeology/       # NEEDS VERIFICATION
```

### Required composition decision

Before executable work, maintainers must choose and document:

1. the canonical policy package(s);
2. the query called for classification, access, render, promotion, and release;
3. whether domain rules import shared helpers or a shared bundle imports domain data;
4. which lane owns profile selection;
5. how bundle precedence and most-restrictive wins are computed;
6. how missing packages, queries, profiles, or inputs map to finite outcomes;
7. how CI and runtime prove identical bundle digests and input normalization;
8. how policy corrections invalidate decisions and public derivatives.

### No silent fallback

Forbidden fallback behavior includes:

- missing domain rule → use generic allow;
- missing profile → use a weaker profile;
- evaluator error → treat default value as approval;
- unknown rank/tier → assume open;
- absent consent state → infer consent;
- missing review → infer no review required;
- unresolved cultural authority → use project ownership as authority;
- missing receipt → trust output appearance;
- unavailable release record → serve from processed/catalog data;
- unsupported consumer obligation → drop the obligation.

Every one of these fails closed.

[Back to top](#top)

---

## Minimum sensitivity policy input

The executable input contract is **PROPOSED** and must become schema-backed before activation.

### Request identity

| Field | Requirement |
|---|---|
| `request_id` | Stable evaluation identifier |
| `operation` | Closed enum: ingest, normalize, validate, catalog, promote, render, detail, map, tile, search, graph, export, screenshot, embed, focus_mode, ai_answer, correct, withdraw, rollback |
| `audience` | Public, authenticated, reviewer, steward, named agreement, internal, or another accepted class |
| `requested_fields` | Explicit field/claim projection |
| `requested_precision` | Symbolic precision class, not hidden inline sensitive values |
| `purpose` | Bounded intended use |
| `evaluated_at` | Trusted time source |

### Subject identity

| Field | Requirement |
|---|---|
| `subject_ref` | Immutable object/artifact/candidate/layer/release reference |
| `subject_version` | Exact version |
| `subject_digest` | Integrity hash |
| `object_family` | Accepted contract family |
| `knowledge_character` | Candidate, confirmed assertion, observation, model, aggregate, context, synthetic, restricted, or another accepted class |
| `source_role` | Explicit source role |
| `lifecycle_state` | Current governed state |
| `domain` | Must resolve to Archaeology or an explicit cross-lane composition |

### Sensitivity and exposure context

| Field | Requirement |
|---|---|
| `audience_tier` | Explicit or unresolved |
| `record_sensitivity_rank` | Explicit or unresolved; distinct from audience tier |
| `sensitivity_flags` | Closed registry refs, not free-text protected substance |
| `geometry_role` | Exact/internal, generalized, aggregated, public-safe derivative, absent, or another accepted class |
| `exposure_channels` | Fields, geometry, relations, bounds, counts, labels, tiles, logs, search, graph, cache, screenshots, embeddings, AI |
| `join_inputs` | Upstream sensitivity/rights/consent refs |
| `reconstruction_risk_ref` | Validator/report reference when applicable |

### Profile and transform context

| Field | Requirement |
|---|---|
| `required_profile_ref` | Accepted named/versioned profile or explicit deny/no-safe-transform |
| `applied_profile_ref` | Exact profile used |
| `profile_status` | Active, deprecated, retired, revoked, unknown, or accepted vocabulary |
| `transform_run_ref` | Exact execution reference |
| `input_hashes` | Immutable source hashes where allowed |
| `output_ref` | Transformed output identity |
| `output_hashes` | Immutable output hashes |
| `receipt_refs` | Resolvable receipt references |
| `residual_risk_ref` | Bounded review/validation statement |

### Authority, rights, CARE, consent, and review

| Field | Requirement |
|---|---|
| `steward_org_ref` | Governed organization ref where applicable |
| `authority_to_control_ref` | Named authority ref; KFM does not invent it |
| `care_obligation_refs` | Registry-backed obligations |
| `rights_refs` | Rights and redistribution posture |
| `consent_refs` | Scoped grants where applicable |
| `revocation_refs` | Live revocation state |
| `embargo_refs` | Active/expired/unknown embargo state |
| `review_refs` | Current required sensitivity, cultural, rights-holder, steward, and release reviews |
| `review_independence` | Separation-of-duties result |

### Evidence, policy, release, and reversibility

| Field | Requirement |
|---|---|
| `evidence_refs` | EvidenceRefs used by claim-bearing output |
| `evidence_bundle_refs` | Required resolved support |
| `policy_bundle_ref` | Bundle id/version/digest |
| `policy_input_version` | Normalized input contract version |
| `candidate_ref` | Release candidate when applicable |
| `promotion_decision_ref` | Governed transition decision when applicable |
| `release_manifest_ref` | Required for released public use |
| `correction_refs` | Active corrections |
| `withdrawal_refs` | Active withdrawal state |
| `rollback_ref` | Resolvable rollback target |
| `stale_state` | Current/expired/unknown according to accepted rules |

### Input invariants

- References must resolve under authorization; a string is not closure.
- Unknown required fields fail closed.
- Exact protected detail must not be copied into policy logs or reason text.
- Inputs should carry symbolic classifications and opaque refs rather than protected payloads.
- The normalized input must be identical in CI and runtime for parity tests.
- Input digest and bundle digest should be recorded in decisions/receipts.
- A prior decision must not be replayed against a changed subject, profile, consent state, review state, policy bundle, or release state.

[Back to top](#top)

---

## Classification and most restrictive wins

### Classification order

A safe evaluator should resolve classification in this order:

1. validate input identity and version;
2. establish object family and knowledge character;
3. resolve source role and source restrictions;
4. resolve current audience tier and per-record rank without collapsing them;
5. collect protected-category flags through registry references;
6. collect rights, CARE, sovereignty, consent, revocation, embargo, and review context;
7. inspect geometry role and all exposure channels;
8. inherit restrictions from every join, source, derivative, and dependency;
9. choose the most restrictive applicable disposition;
10. determine whether any accepted transform can satisfy the requested use;
11. require receipt, evidence, review, release, correction, and rollback closure;
12. emit finite outcome, safe reasons, and obligations.

### Most-restrictive propagation

For a derived object `D` based on inputs `I1..In`, the effective sensitivity posture must not be less restrictive than any applicable upstream posture unless an accepted policy explicitly authorizes a governed transform and all required artifacts close.

This applies to:

- spatial joins;
- temporal joins;
- graph edges;
- catalog projections;
- tiles and PMTiles;
- aggregate counts;
- cluster centroids;
- heatmaps;
- convex hulls and extents;
- search and autocomplete;
- vector/semantic indexes;
- screenshots and report figures;
- map labels and popups;
- AI prompts, retrieval context, answers, and summaries;
- cache entries and export bundles.

### No sensitivity laundering

Processing, aggregation, summarization, map rendering, model inference, AI explanation, source mixing, or conversion to a different object family must not silently lower sensitivity.

### Safer downgrade rule

A move toward a more restrictive state may occur immediately when risk, rights, consent, review, or evidence changes. A move toward broader access requires the complete accepted transform/review/release path.

[Back to top](#top)

---

## Transform profile admission

A profile name in a record is not enough. A profile is eligible only when all accepted requirements are satisfied.

### Minimum profile record

| Field | Required behavior |
|---|---|
| Stable profile id | Names a single governed profile |
| Version | Immutable semantic version |
| Status | Only accepted active status may be used |
| Domain applicability | Explicit Archaeology or accepted cross-domain scope |
| Applicable object families | Closed set or registry refs |
| Input sensitivity classes | Explicit |
| Allowed output classes | Explicit |
| Strategy | Accepted transform family |
| Parameters | Governed and reviewable; sensitive parameters excluded from ordinary logs/docs |
| Determinism rule | Reproducible |
| Seed rule | Governed when stochastic methods are used |
| Denial conditions | States when no safe transform is possible |
| Required reviews | Explicit roles |
| Required receipts | Explicit receipt family |
| Verifier reference | Executable deterministic validator |
| Fixture references | Nonempty valid/invalid/revoked/edge-case coverage |
| Residual-risk statement | Required |
| Correction/rollback behavior | Required |
| Supersedes/deprecates | Explicit lineage |

### Profile lifecycle

```text
draft -> review -> accepted/active -> deprecated -> retired/revoked
```

- `draft` profiles cannot support public release.
- `deprecated` profiles cannot be selected for new outputs unless a governed exception exists.
- `retired` or `revoked` profiles invalidate dependent public artifacts according to correction policy.
- A parameter change creates a new version; it does not silently mutate the old profile.
- Deletion must not erase lineage required to reproduce or correct prior outputs.

### Current catalog boundary

`policy/redaction/profiles.yaml` is currently a seven-line placeholder with no profiles. It is not an active catalog and cannot satisfy the admission contract above.

### Inline profiles forbidden

Runtime requests must not supply ad hoc redaction parameters and call them a profile. Inline parameters bypass review, versioning, determinism, fixtures, verifier parity, correction, and rollback.

### No safe transform

When protected substance cannot be made safe for the requested use, the correct policy result is deny, abstain, hold, or suppress. A system must not manufacture a public summary merely because a caller expects content.

[Back to top](#top)

---

## Exact detail, public-safe derivatives, and inference risk

### Separate identities

Exact/internal source and public-safe derivative must have separate:

- object references;
- versions;
- hashes;
- geometry roles;
- access controls;
- lifecycle states;
- cache keys;
- catalog/release identities;
- policy decisions;
- receipts and lineage.

A style layer, filter, zoom limit, hidden field, or UI toggle does not create a separate public-safe artifact.

### Denied public channels

Protected detail must not leak through:

- API fields or error payloads;
- map source data, tile payloads, tile bounds, feature IDs, query endpoints, hover state, labels, clustering behavior, or style expressions;
- downloadable files or export bundles;
- screenshots, thumbnails, reports, legends, or alt text;
- search results, snippets, facets, counts, sorting, autocomplete, or “nearby” features;
- graph edges, adjacency, traversal, or linked public entities;
- timestamps, cadence, change events, or availability windows;
- cache keys, filenames, object-store paths, URLs, ETags, or debug metadata;
- validation findings, policy reasons, stack traces, metrics labels, or logs;
- embeddings, vector indexes, retrieval chunks, prompt context, tool calls, model traces, or generated answers;
- intersections with parcels, roads, waterways, terrain, imagery, administrative boundaries, or other layers that narrow location;
- 3D geometry, point clouds, camera paths, terrain clipping, photogrammetry, LiDAR, SAR, or derived anomalies.

### Reconstruction-risk review

Public-safe validation must consider combinations of outputs, not only each object independently.

Examples of cumulative risk:

- multiple generalized releases whose intersection narrows the source;
- a coarse point plus a descriptive narrative;
- a count plus a known survey boundary;
- a tile presence/absence pattern;
- a public label aligned with a restricted feature;
- repeated outputs with different seeds or profile versions;
- release history that reveals a location by change pattern;
- an AI answer that combines public clues.

### Geometry-free output

Removing geometry does not automatically make an object safe. Identifiers, collection names, descriptions, ownership, chronology, route proximity, imagery, or relational context may still reveal the place.

### Public-safe carrier rule

A public carrier may reference only a released public-safe derivative. It must never receive exact/internal geometry and rely on client-side hiding.

[Back to top](#top)

---

## Cultural, sovereignty, CARE, rights, and consent

### Authority boundary

KFM governs the review and policy interface. It does not define the substance of cultural, Indigenous, sacred, burial, oral-history, or community-controlled knowledge.

Where authority applies:

- the named authority controls the substantive determination;
- KFM records opaque authority references, review status, obligations, and permitted scope;
- protected deliberation and substance remain in authorized restricted systems;
- absence of an authority record does not transfer authority to the project.

### CARE and sovereignty obligations

Policy should preserve accepted obligations such as:

- authority to control;
- responsibility and stewardship;
- benefit commitments;
- attribution or notice requirements;
- access limitations;
- downstream sharing restrictions;
- retention/deletion rules;
- review requirements;
- revocation/correction contacts.

The obligation registry and exact machine fields remain `NEEDS VERIFICATION`.

### Consent is live state

Consent must be evaluated against:

- subject and authority;
- scope and purpose;
- audience;
- object/claim/derivative;
- permitted fields and precision;
- issue and expiry time;
- embargo;
- revocation;
- retention;
- redistribution;
- correction and deletion obligations.

Silence, prior access, repository ownership, license compatibility, prior publication, geographic intersection, or a generic review must not be treated as consent.

### Revocation and embargo

A revocation, embargo activation, rights change, or authority change must:

1. block new evaluations;
2. identify affected decisions and receipts;
3. restrict or withdraw dependent candidates/releases;
4. invalidate caches, indexes, exports, screenshots, and embeddings where governed;
5. update public stale/withdrawn state without exposing protected reason detail;
6. issue correction/withdrawal records;
7. preserve safe audit lineage;
8. require fresh review before any broader reuse.

### Separation of duties

Material public release should separate, as applicable:

- author/producer;
- Archaeology domain steward;
- sensitivity reviewer;
- cultural/community authority or liaison;
- rights-holder representative;
- consent/revocation steward;
- policy reviewer;
- release authority;
- correction/rollback reviewer.

A role label alone does not prove independence or authority.

[Back to top](#top)

---

## Decision vocabularies and normalization

### Shared machine envelope

The current shared `PolicyDecision` schema allows:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

and includes `sensitivity` as a policy family.

This README does not add another machine enum.

### Internal dispositions

Policy implementations may use internal dispositions for orchestration:

```text
ALLOW
RESTRICT
HOLD
QUARANTINE
SUPPRESS
REVIEW_REQUIRED
DENY
ABSTAIN
ERROR
```

These must be normalized before crossing a governed interface.

### Normalization matrix

| Internal disposition | Shared outcome | Required interpretation |
|---|---|---|
| `ALLOW` | `ANSWER` | Only for the exact scoped operation after all release/public obligations close |
| `RESTRICT` | `ANSWER` or `DENY` | `ANSWER` only if the consumer can enforce every obligation; otherwise `DENY` |
| `SUPPRESS` | `ANSWER`, `ABSTAIN`, or `DENY` | Bounded non-sensitive answer only when policy explicitly permits; never invent content |
| `HOLD` | `ABSTAIN` or `DENY` | Preserve prior state; no public trust-bearing action |
| `QUARANTINE` | `DENY` or `ABSTAIN` | Route internal artifact; public action blocked |
| `REVIEW_REQUIRED` | `ABSTAIN` or `DENY` | No implied approval |
| `DENY` | `DENY` | Safe reason only; no protected detail |
| `ABSTAIN` | `ABSTAIN` | Insufficient or unresolved support |
| `ERROR` | `ERROR` | Fail closed; no fallback allow |

### Promotion vocabulary remains separate

`PromotionDecision` uses:

```text
APPROVE | DENY | ABSTAIN
```

A sensitivity policy result may support a promotion decision but does not equal it. `APPROVE` still does not publish by itself.

### No obligation loss

A consumer that cannot enforce:

- restricted audience;
- field suppression;
- public-safe derivative selection;
- notice/citation requirements;
- stale/withdrawn markers;
- no-download;
- no-index;
- no-cache;
- no-AI;
- review or revalidation requirements;

must not downgrade the result to unrestricted `ANSWER`.

[Back to top](#top)

---

## Reason codes and obligations

These families are **PROPOSED**. They must be accepted in a registry/schema before machine use.

### Safe reason-code families

| Family | Example codes |
|---|---|
| Input/identity | `SUBJECT_UNRESOLVED`, `SUBJECT_DIGEST_MISMATCH`, `OBJECT_FAMILY_UNKNOWN`, `LIFECYCLE_STATE_INVALID` |
| Classification | `AUDIENCE_TIER_UNKNOWN`, `SENSITIVITY_RANK_UNKNOWN`, `SENSITIVITY_FLAGS_UNRESOLVED`, `MOST_RESTRICTIVE_INPUT_UNRESOLVED` |
| Exact/inference | `EXACT_DETAIL_PRESENT`, `REVERSE_INFERENCE_RISK`, `SIDE_CHANNEL_RISK`, `STYLE_ONLY_HIDING`, `PUBLIC_DERIVATIVE_UNVERIFIED` |
| Candidate/source role | `CANDIDATE_NOT_CONFIRMED`, `SOURCE_ROLE_MISSING`, `SOURCE_ROLE_COLLAPSE` |
| Profile | `PROFILE_REQUIRED`, `PROFILE_UNKNOWN`, `PROFILE_INACTIVE`, `PROFILE_REVOKED`, `PROFILE_VERSION_MISMATCH`, `PROFILE_NOT_APPLICABLE` |
| Transform/receipt | `TRANSFORM_NOT_VERIFIED`, `INPUT_HASH_MISMATCH`, `OUTPUT_HASH_MISMATCH`, `RECEIPT_REQUIRED`, `RECEIPT_UNRESOLVED`, `RESIDUAL_RISK_UNRESOLVED` |
| Authority/CARE | `AUTHORITY_TO_CONTROL_UNRESOLVED`, `CARE_OBLIGATION_UNRESOLVED`, `SOVEREIGNTY_REVIEW_REQUIRED` |
| Rights/consent | `RIGHTS_UNRESOLVED`, `CONSENT_REQUIRED`, `CONSENT_OUT_OF_SCOPE`, `CONSENT_EXPIRED`, `CONSENT_REVOKED`, `EMBARGO_ACTIVE` |
| Review | `SENSITIVITY_REVIEW_REQUIRED`, `CULTURAL_REVIEW_REQUIRED`, `RIGHTS_HOLDER_REVIEW_REQUIRED`, `REVIEW_STALE`, `REVIEW_NOT_INDEPENDENT` |
| Evidence | `EVIDENCE_REF_UNRESOLVED`, `EVIDENCE_BUNDLE_REQUIRED`, `CLAIM_SUPPORT_INSUFFICIENT` |
| Release | `RELEASE_REQUIRED`, `RELEASE_WITHDRAWN`, `CORRECTION_ACTIVE`, `ROLLBACK_UNRESOLVED`, `PUBLIC_SURFACE_UNAUTHORIZED` |
| Runtime | `POLICY_BUNDLE_UNRESOLVED`, `POLICY_QUERY_MISSING`, `POLICY_VERSION_DRIFT`, `EVALUATOR_ERROR`, `CONSUMER_OBLIGATION_UNSUPPORTED` |

Reason text must be safe for its audience. It must not include exact coordinates, protected names, sensitive categories not cleared for disclosure, private identities, secret profile parameters, consent tokens, or reconstruction clues.

### Obligation families

| Obligation | Required effect |
|---|---|
| `deny_exact_detail` | Remove/block exact or reverse-engineerable protected detail |
| `quarantine_required` | Route artifact to governed quarantine |
| `named_profile_required` | Use only an accepted profile id/version |
| `redaction_required` | Apply governed field/relationship suppression |
| `generalization_required` | Produce a separate public-safe derivative |
| `aggregation_required` | Use accepted aggregate logic and reconstruction checks |
| `suppression_required` | Produce no public carrier for protected subject |
| `transform_receipt_required` | Emit and resolve required receipt |
| `sensitivity_review_required` | Obtain current sensitivity review |
| `cultural_review_required` | Route to named cultural/community authority process |
| `rights_holder_review_required` | Obtain applicable rights-holder review |
| `consent_check_required` | Re-evaluate live consent/revocation/embargo state |
| `restricted_audience_required` | Limit to accepted role/audience |
| `evidence_bundle_required` | Resolve required claim support |
| `public_safe_derivative_required` | Serve only released derivative |
| `no_download` | Disable download/export |
| `no_search_index` | Exclude from public search/vector indexes |
| `no_graph_projection` | Exclude sensitive edges/relations |
| `no_cache` | Prevent or invalidate caches where required |
| `no_embedding` | Prevent vectorization/retrieval use |
| `no_ai_context` | Prevent model retrieval/prompt inclusion |
| `notice_required` | Carry approved limitation/authority notice |
| `release_manifest_required` | Require governed release |
| `correction_path_required` | Link correction/withdrawal handling |
| `rollback_required` | Require resolvable rollback target |
| `revalidate_on_change` | Re-run when policy/profile/rights/consent/review/evidence changes |

Obligations must be structured, versioned, machine-enforceable, and preserved end to end.

[Back to top](#top)

---

## Transform receipt, registry, evidence, and release boundaries

### Transform versus receipt

`SensitivityTransform` describes the governed transform class or intent.

`PublicationTransformReceipt` or an accepted `RedactionReceipt` records a specific application.

Neither one is:

- a PolicyDecision;
- a ReviewRecord;
- an EvidenceBundle;
- a PromotionDecision;
- a ReleaseManifest;
- a public artifact.

### Minimum receipt semantics

The accepted receipt model should eventually bind:

- receipt id/version;
- subject and source refs;
- input versions and hashes;
- output refs and hashes;
- profile id/version/status;
- transform implementation/run ref;
- policy bundle/query/input digest;
- reason and obligation refs;
- evidence refs;
- review/authority/rights/consent refs;
- kept/removed/generalized field classes without leaking protected values;
- residual-risk statement;
- creation time and actor/runner;
- correction, supersession, withdrawal, revocation, and rollback lineage;
- deterministic replay/verifier references.

The current Archaeology transform-receipt and RedactionReceipt schemas do not enforce this roster.

### Receipt storage

`data/receipts/archaeology/sensitivity/` documents a process-memory lane. It does not prove:

- concrete receipt instances;
- accepted subtype layout;
- signatures;
- replay validation;
- policy integration;
- proof integration;
- release integration.

### Sensitivity registry

`data/registry/sensitivity/archaeology/` documents control-state pointers and blockers. It must not duplicate policy or store protected payloads.

A registry record may point to:

- subject identity;
- tier/rank refs;
- profile refs;
- authority/review/consent refs;
- receipt refs;
- evidence/proof refs;
- release/correction/rollback refs.

It does not decide admissibility.

### Evidence boundary

A sensitivity-safe output can still be unsupported. EvidenceBundle closure and sensitivity permission are independent requirements.

### Release boundary

A validated transform and receipt do not publish. Public use additionally requires accepted release records, public-safe artifact identity, correction path, rollback target, and consumer obligation handling.

[Back to top](#top)

---

## Public surface and log minimization

### Governed API

The governed API must:

- accept only released public-safe refs for public operations;
- never query or serialize exact/internal protected geometry for public clients;
- enforce policy decision and obligations;
- return finite outcomes;
- omit protected reason detail;
- preserve citations and limitation notices;
- refuse unsupported obligation sets;
- honor withdrawal, correction, revocation, and stale state.

### MapLibre and tiles

Map and tile systems must:

- receive public-safe derivatives upstream;
- reject internal/exact geometry;
- avoid style-only hiding;
- prevent source inspection and query endpoints from exposing restricted properties;
- check bounds, feature IDs, tile presence, zoom behavior, clustering, labels, and screenshots for inference;
- invalidate affected tiles and caches after policy/revocation/correction changes.

### Evidence Drawer and Focus Mode

These surfaces may show:

- public-safe claim/evidence summaries;
- approved authority/limitation notices;
- finite denial/abstention states;
- released receipt or policy summaries that do not expose internals.

They must not show exact protected detail, private review substance, profile secrets, consent tokens, or internal receipt payloads.

### Search, graph, export, and embedding

Policy must cover more than the map:

- public search and autocomplete;
- graph projections and neighbor traversal;
- downloadable tables and GIS files;
- report exports;
- vector indexes and embeddings;
- retrieval-augmented generation;
- screenshots and previews.

Exclusion from the map does not imply exclusion from these channels.

### Governed AI

AI must receive already governed context.

Required behavior:

- no exact or reverse-engineerable protected location in prompts or retrieval;
- no inference from nearby public layers to narrow a protected site;
- no conversion of candidate/anomaly/context into confirmed archaeology;
- no claim that KFM owns cultural authority;
- no explanation of hidden profile parameters or reconstruction methods;
- cite resolved evidence where a claim is allowed;
- `ABSTAIN` or `DENY` when safe bounded support is unavailable;
- correction and revocation propagate to retrieval indexes and cached answers.

### Log minimization

Logs, metrics, traces, errors, receipts, and policy decisions should use:

- opaque subject refs;
- safe reason codes;
- policy/profile versions;
- counts only where safe;
- hashes only when they do not create a public correlation channel;
- restricted destinations and retention.

They must not contain protected coordinates, sensitive identifiers, cultural substance, consent tokens, hidden parameters, raw policy input payloads, or public reconstruction clues.

[Back to top](#top)

---

## Validation, tests, and CI

### Validation matrix

| Case | Expected policy posture | Required proof |
|---|---|---|
| Unknown classification | Hold/abstain/deny | Negative policy test |
| Exact protected detail in public request | Deny | Rego test + public no-leak test |
| Candidate presented as confirmed site | Deny | Candidate/site anti-collapse test |
| Missing/unknown/inactive/revoked profile | Deny/hold | Profile registry fixture and test |
| Inline profile parameters | Deny | Policy test |
| Transform ref without output hash binding | Hold | Receipt/lineage test |
| Missing receipt | Hold/deny | Negative fixture |
| Receipt points to wrong subject/output | Deny/error | Integrity test |
| Permissive schema accepts meaningless object | Test must expose semantic gap | Schema/semantic validator test |
| Required cultural review absent | Hold/deny | Review policy test |
| Consent missing/out of scope/expired/revoked | Deny/hold | Live-state fixtures |
| Embargo active | Deny/hold | Time-controlled fixture |
| Rights unresolved | Deny/hold | Rights policy fixture |
| Join lowers upstream restriction | Deny | Most-restrictive propagation test |
| Map style hides exact source | Deny | UI/map integration test |
| Tile/bounds/label leaks location | Deny | Side-channel fixture |
| Search/graph/embedding reveals subject | Deny | Cross-surface tests |
| Consumer cannot enforce obligations | Deny | Contract test |
| Release missing/withdrawn | Deny/abstain | Release integration test |
| Correction/revocation after release | Withdraw/invalidate | End-to-end correction test |
| Evaluator/package/query missing | Error/deny | Failure injection |
| CI/runtime bundles differ | Fail gate | Digest parity test |

### Fixture requirements

Fixtures must be:

- synthetic and public-safe;
- deterministic;
- no-network by default;
- free of real protected geometry or cultural substance;
- non-vacuous;
- linked to exact consumer tests;
- versioned with profile and policy dependencies;
- paired with expected finite outcomes and reason/obligation sets.

Required fixture families include:

- classification valid/invalid/unknown;
- candidate versus confirmed site;
- exact/internal versus public-safe derivative;
- reverse-inference and side channels;
- profile active/deprecated/retired/revoked/unknown;
- receipt valid/missing/mismatched/replayed;
- review present/missing/stale/not independent;
- consent valid/out of scope/expired/revoked;
- embargo active/expired;
- most-restrictive joins;
- public API/map/tile/search/graph/export/embedding/AI behavior;
- correction, withdrawal, cache invalidation, and rollback.

### Current test boundary

The checked domain tests are placeholder docstrings. The sensitive-geometry fixture lane is a README-only routing boundary. The profile catalog and receipt schemas do not support substantive end-to-end tests yet.

### Validator requirements

An accepted validator should:

1. validate normalized input shape;
2. resolve profile metadata;
3. reproduce deterministic transform when authorized;
4. compare input/output hashes and receipt binding;
5. inspect geometry role and exposure channels;
6. detect side-channel and reconstruction risks;
7. verify most-restrictive propagation;
8. resolve required review, consent, evidence, policy, and release refs;
9. emit structured findings without protected detail;
10. support correction/rollback revalidation.

The current `tools/validators/sensitive_geometry/` lane documents these responsibilities but does not establish an executable.

### CI graduation criteria

The domain workflow may graduate from readiness hold only when:

- accepted policy source and bundle topology exist;
- package/query and immutable input contract are fixed;
- active profile catalog is nonempty and reviewed;
- transform and receipt contracts/schemas are substantive;
- validators are executable;
- valid/invalid fixtures are nonempty;
- negative tests cover every protected family and public channel;
- policy bundle parity is proven between CI and runtime;
- review, consent, receipt, evidence, release, correction, and rollback refs are checked;
- no protected data enters CI logs or artifacts;
- branch rules identify required checks;
- rollback has been rehearsed.

### Passing limits

A passing check does not prove:

- archaeological truth;
- cultural authority;
- consent;
- rights clearance;
- evidence sufficiency;
- public safety for untested channels;
- release approval;
- ongoing permission after revocation;
- production deployment;
- absence of side channels outside the tested scope.

[Back to top](#top)

---

## Threat and failure model

| Threat or failure | Consequence | Required response |
|---|---|---|
| Exact location exposed | Looting, harm, rights/cultural violation | Deny, contain, correct, withdraw, investigate |
| Reverse inference from derivatives | Restricted place narrowed without direct coordinates | Treat derivative as sensitive; invalidate and redesign |
| Candidate/site collapse | Unverified feature becomes asserted site | Deny assertion; preserve candidate role |
| Profile spoofing | Weak/ad hoc transform treated as accepted | Require registry identity/version/digest |
| Missing-profile fallback | Strong requirement silently weakened | Deny |
| Non-deterministic transform | Output cannot be reproduced/audited | Reject profile/output |
| Receipt spoof or mismatch | Process memory detached from actual transform | Deny/error; quarantine |
| Permissive schema laundering | Empty/meaningless object passes shape check | Require semantic validator and negative tests |
| Cultural authority substitution | KFM interprets or approves controlled substance | Defer to named authority; withdraw claim |
| Consent inference | Use proceeds without scoped live permission | Deny/hold |
| Revocation race | Cached/public derivative remains available | Immediate block and invalidation |
| Most-restrictive loss | Join or summary weakens upstream controls | Deny and repair propagation |
| Style-only hiding | Exact data reaches client | Replace with upstream public-safe derivative |
| Log/trace leakage | Protected detail appears in operational systems | Minimize, restrict, rotate, correct |
| Search/index leakage | Hidden data discoverable outside map | Remove/invalidate index and test all surfaces |
| AI triangulation | Generated answer narrows protected location | Deny/abstain; remove context and cached output |
| Review-role collapse | Author self-approves sensitive release | Hold; require independent roles |
| Bundle drift | CI and runtime make different decisions | Fail gate; pin digest and parity test |
| Stale policy/profile | Old decision remains treated as current | Re-evaluate and invalidate dependents |
| Rollback failure | Unsafe output cannot be removed | Block release until rollback is resolvable/tested |

### Untrusted content

Source text, oral history, uploaded documents, metadata, filenames, and model output are untrusted. They must not override policy, disclose protected information through prompt injection, or create authority/consent records.

[Back to top](#top)

---

## Smallest sound implementation sequence

Each phase is **PROPOSED** and separately reviewable.

### Phase 0 — Resolve governance and placement

1. Assign owners and CODEOWNERS.
2. Decide domain versus cross-cutting sensitivity policy composition.
3. Select canonical package/query names.
4. Decide profile catalog authority.
5. Decide receipt contract/schema authority.
6. Resolve doctrine/profile parameter acceptance and protected configuration handling.
7. Record ADRs/drift/migration notes.

**Rollback:** documentation/register changes only.

### Phase 1 — Define immutable contracts

1. Define sensitivity policy input contract.
2. Define safe reason-code and obligation registries.
3. Make `SensitivityTransform` schema substantive.
4. Make transform/RedactionReceipt schema substantive and contract-paired.
5. Define profile schema and lifecycle.
6. Define registry pointer shape.
7. Define review/consent/revocation adapter refs.
8. Add deterministic identity/version/hash rules.

**Rollback:** revert schemas/contracts/registries before runtime adoption.

### Phase 2 — Populate profiles and fixtures

1. Add reviewed profile records without exposing protected operational secrets.
2. Add nonempty public-safe synthetic fixtures.
3. Add profile lifecycle/revocation cases.
4. Add transform/receipt integrity fixtures.
5. Add side-channel/reconstruction cases.
6. Add cross-surface cases.
7. Link every fixture to consumers.

**Rollback:** remove unaccepted profiles/fixtures; no production use.

### Phase 3 — Implement policy

1. Replace six-line scaffolds with accepted rules or compose them through a new reviewed bundle.
2. Keep defaults fail closed.
3. Resolve every required input.
4. Emit finite outcomes, safe reasons, and obligations.
5. Implement most-restrictive propagation.
6. Implement profile and receipt checks.
7. Implement review, consent, evidence, release, and rollback prerequisites.
8. Add bundle manifest/version/digest.

**Rollback:** restore prior bundle and invalidate decisions from rejected version.

### Phase 4 — Implement validators and tests

1. Implement profile validator.
2. Implement transform/receipt replay validator.
3. Implement sensitive-geometry and reconstruction validator.
4. Implement policy tests for every rule.
5. Implement API/map/tile/search/graph/export/embedding/AI tests.
6. Add no-network defaults and sensitive-log tests.
7. Prove CI/runtime parity.

**Rollback:** disable validator/CI adoption while preserving findings.

### Phase 5 — Integrate review, registry, receipt, and release

1. Resolve authorized reviewer/authority registries.
2. Wire consent/revocation/embargo state.
3. Emit governed receipts.
4. Link evidence and review records.
5. Integrate candidate/release/correction/withdrawal/rollback.
6. Test revocation and cache/index invalidation.
7. Keep public clients on governed APIs and released derivatives.

**Rollback:** deny public use and restore prior safe release.

### Phase 6 — Operational adoption

1. Establish monitoring and drift detection.
2. Establish profile/policy review cadence.
3. Rehearse correction and rollback.
4. Document incident/takedown contacts without exposing restricted data.
5. Require human review for material profile, policy, or release changes.
6. Measure false allow, false deny, unresolved, and obligation-enforcement failures.

[Back to top](#top)

---

## Definition of done

### Governance

- [ ] Owners and CODEOWNERS are assigned.
- [ ] Domain/cross-cutting policy topology is accepted.
- [ ] Profile catalog authority is accepted.
- [ ] Receipt/registry/review/release authority boundaries are accepted.
- [ ] Required ADRs and drift entries are closed or linked.
- [ ] Cultural/community authority deferral is operationally supported.

### Contracts and schemas

- [ ] Immutable policy input contract exists.
- [ ] PolicyDecision/reason/obligation vocabularies are accepted.
- [ ] SensitivityTransform schema is substantive.
- [ ] PublicationTransformReceipt/RedactionReceipt meaning and shape are paired.
- [ ] Profile schema and lifecycle are accepted.
- [ ] Registry, review, consent, revocation, correction, and rollback refs have accepted shapes.
- [ ] No permissive empty schema is treated as enforcement.

### Policy

- [ ] Package/query and bundle manifest are accepted.
- [ ] All ten intended concerns have substantive rules or explicit composition.
- [ ] Default and missing-dependency behavior fail closed.
- [ ] Most-restrictive propagation is implemented.
- [ ] Named-profile, receipt, review, consent, evidence, release, and rollback gates are implemented.
- [ ] Safe reason codes and obligations are emitted.
- [ ] CI/runtime bundle parity is proven.

### Profiles and transforms

- [ ] Active profile catalog is nonempty and reviewed.
- [ ] Profiles are named, versioned, deterministic, fixture-backed, and verifier-linked.
- [ ] No inline profile parameters are accepted.
- [ ] Transform execution binds immutable input/output hashes.
- [ ] Residual risk and no-safe-transform cases are explicit.
- [ ] Profile correction/revocation invalidates dependents.

### Tests and validators

- [ ] Nonempty valid/invalid fixtures exist.
- [ ] Domain policy tests are executable.
- [ ] Public-no-leak and candidate-not-site tests are substantive.
- [ ] Sensitive-geometry/reconstruction validator is executable.
- [ ] Receipt replay/integrity validator is executable.
- [ ] Cross-surface API/map/tile/search/graph/export/cache/embedding/AI tests pass.
- [ ] No-network and no-sensitive-log tests pass.
- [ ] Failure injection covers missing evaluator/package/query/profile/receipt/review/release.

### Review, release, and reversibility

- [ ] Named authorities and reviewers are resolved under access control.
- [ ] Separation of duties is enforced.
- [ ] Consent/revocation/embargo are live inputs.
- [ ] Receipt and registry records are emitted and auditable.
- [ ] EvidenceBundle support is resolvable.
- [ ] Candidate/release/correction/withdrawal/rollback links are valid.
- [ ] Cache, index, export, embedding, tile, screenshot, and AI invalidation are tested.
- [ ] Rollback drill is recorded.
- [ ] Human review approves operational adoption.

[Back to top](#top)

---

## Conflict and ADR register

| Conflict | Current evidence | Required resolution |
|---|---|---|
| Domain versus cross-cutting sensitivity policy home | Domain README/rules exist; checked cross-cutting Archaeology README absent | ADR/lane-register composition decision |
| Direct child lane versus parent-level Rego | Child lane README-only; executable-intent files are parent siblings | Decide move, compose, or document parent layout |
| Doctrine versus active profile catalog | Rich draft profile doctrine; catalog is generic placeholder | Accepted profile authority and populated records |
| Draft tier/rank/profile values versus runtime config | Detailed doctrine; no accepted machine profile/input/evaluator | Steward review, schemas, fixtures, policy, parity |
| Transform semantics versus schema | Rich contract; empty permissive schema | Schema/validator implementation |
| Receipt semantics versus schema | Rich domain receipt contract; empty permissive schema | Contract/schema reconciliation |
| `RedactionReceipt` doctrine versus schema | Required by doctrine; schema empty, Fauna-sourced, no contract ref | Canonical semantic contract and schema migration |
| Profile catalog source | Habitat-sourced placeholder used cross-domain | Replace with governed cross-domain catalog |
| Review/consent schema references | Doctrine names governance objects; several checked paths absent or scaffolded | Accepted adapter/contracts/schemas |
| Policy default versus substantive behavior | `default allow := false` is conservative, but no rules/output contract | Implement rules and tests; verify query semantics |
| Internal decisions versus machine envelope | ALLOW/RESTRICT/HOLD etc. versus ANSWER/ABSTAIN/DENY/ERROR | Accepted normalization contract |
| Sensitivity versus promotion vocabulary | Policy outcome versus APPROVE/DENY/ABSTAIN | Preserve separate object families and mapping |
| Registry versus policy | Registry docs contain control posture | Keep pointers only; no duplicated decision authority |
| Receipt versus proof/release | Receipt lane describes process memory | Preserve separation; require proof and release independently |
| Public-safe fixture path drift | Multiple archaeology public-safe fixture forms exist | Governed migration/deprecation plan |
| Numeric/reconstruction detail in public docs | Doctrine includes draft values; security docs warn against leakage | Decide public versus restricted parameter handling |

No conflict is silently resolved by this README.

[Back to top](#top)

---

## Open verification register

### Policy and runtime

- Which package and query does each operation use?
- Are the ten parent-level Rego files retained, moved, composed, or replaced?
- What is the accepted shared/domain precedence algorithm?
- What is the immutable input schema?
- How are missing packages/queries/evaluator failures represented?
- Where is the bundle manifest and digest?
- Which deployed consumers evaluate the bundle?
- Does CI use the exact runtime bundle/input normalization?

### Classification and profiles

- Which audience tiers and record ranks are accepted for each Archaeology object family?
- Which draft doctrine values remain public documentation versus restricted operational configuration?
- Which profiles are accepted and active?
- Where is the profile registry and schema?
- How are profile review, deprecation, retirement, revocation, and supersession governed?
- How are deterministic seeds and protected parameters stored?
- How is residual reconstruction risk reviewed?

### Contracts, schemas, and receipts

- What is the canonical RedactionReceipt semantic contract?
- Is `PublicationTransformReceipt` the domain specialization, an adapter, or a separate receipt family?
- Which schema home is canonical?
- Where do emitted receipts live?
- How are signatures, replay, and lineage verified?
- Which receipt fields may be public, reviewer-only, or restricted?

### Cultural, rights, consent, and review

- How are named authorities registered and authorized?
- Which review roles are required per object/action/audience?
- What is the machine representation of CARE obligations?
- What are consent scope, expiry, revocation, retention, and redistribution semantics?
- How are objections, takedowns, and revocations received and authenticated?
- How is reviewer confidentiality protected?
- How is separation of duties enforced?

### Tests and public surfaces

- Which fixture root is canonical for each scenario?
- Which tests consume the sensitive-geometry fixtures?
- Are public-no-leak and candidate-not-site tests implemented?
- Which validators inspect reverse inference and side channels?
- How are maps, tiles, API, search, graph, exports, screenshots, caches, embeddings, Focus Mode, Evidence Drawer, and AI tested?
- How are public artifacts invalidated after correction or revocation?

### Release and operations

- Which candidate/release records consume sensitivity decisions?
- What are branch-protection required checks?
- Where are monitoring, incidents, corrections, withdrawals, and rollback results recorded?
- What is the maximum safe response time for blocking an unsafe public derivative?
- Has an end-to-end revocation and rollback drill been completed?

[Back to top](#top)

---

## Maintenance, correction, and rollback

### Review triggers

Review this README and the implementation whenever:

- sensitivity doctrine changes;
- a policy rule/package/query changes;
- a profile is added, changed, deprecated, retired, or revoked;
- a transform or receipt schema changes;
- consent, rights, CARE, or sovereignty handling changes;
- a new Archaeology object family or source role is added;
- a new public carrier is added;
- a side channel or inference path is discovered;
- a validator or test becomes executable;
- a workflow hold graduates;
- a candidate or release record appears;
- an incident, correction, withdrawal, revocation, or rollback occurs.

### Correction triggers

Correct or withdraw dependent decisions/artifacts when:

- exact or reverse-engineerable protected detail is found;
- source role or candidate/site status was wrong;
- sensitivity classification was wrong;
- a profile was unaccepted, mismatched, non-deterministic, weak, or revoked;
- input/output hashes or receipt bindings are wrong;
- rights, authority, consent, review, or embargo state changes;
- evidence support changes;
- policy bundle or evaluator behavior was wrong;
- release or rollback support is invalid;
- a public consumer dropped obligations;
- caches, indexes, exports, screenshots, embeddings, or AI outputs remain after withdrawal.

### Corrective sequence

1. Restrict affected public and internal use.
2. Identify subjects, inputs, outputs, decisions, receipts, reviews, candidates, releases, and derivatives.
3. Preserve safe audit history.
4. Notify authorized stewards and named authorities.
5. Issue correction, withdrawal, revocation, or embargo records.
6. Invalidate unsafe tiles, caches, indexes, exports, screenshots, embeddings, and AI summaries.
7. Restore prior safe state or deny access.
8. Re-run classification, transform, receipt, evidence, review, policy, release, and public-surface checks.
9. Record final disposition without protected detail.
10. Update fixtures/tests to prevent recurrence.

### Policy rollback

A policy/profile rollback must:

- identify the rejected bundle/profile version;
- stop new evaluations using it;
- find dependent decisions/receipts/releases;
- re-evaluate or withdraw affected outputs;
- restore a prior accepted bundle/profile;
- verify bundle digest parity;
- preserve supersession lineage;
- document why rollback was required;
- avoid exposing sensitive details in public notices.

### Rollback for this documentation change

Restore prior README blob:

```text
ef2e4add020d2d6ec94bfd0c735f314d13a8151d
```

Remove the paired generated receipt if this revision is reverted. No policy source, profile, schema, contract, fixture payload, test, validator, workflow, protected record, evidence object, registry record, receipt instance, release artifact, deployment, public route, map layer, search index, cache, embedding, or AI state requires restoration.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Supports | Limitation |
|---|---|---|
| Directory Rules | `policy/` responsibility and authority-root separation | Doctrine, not runtime proof |
| Prior target README | Existing v0.1 scope and sensitivity concepts | Predates current evidence inventory |
| Parent Archaeology policy | Domain deny-by-default boundary | Draft; parent README does not prove runtime |
| Promotion v0.2 README | Promotion/shape/enforcement separation | Documentation boundary |
| Review v0.2 README | Cultural authority, consent, review-model boundaries | Documentation boundary |
| Archaeology sensitivity doctrine | Draft tier/rank/profile, review, receipt, consent, and revocation posture | Values and paths are not accepted runtime config by this evidence alone |
| Redaction Profiles standard | Named/versioned/deterministic/receipt-bearing invariants | Draft; active catalog adoption unverified |
| `policy/redaction/profiles.yaml` | Catalog path exists | Seven-line Habitat-sourced placeholder; no profiles |
| Ten Archaeology Rego files | Intended policy concerns and conservative default | Six-line scaffolds; no rule bodies or output contract |
| `SensitivityTransform` contract | Rich domain transform semantics | Draft; not implementation |
| SensitivityTransform schema | Paired path exists | Empty permissive scaffold |
| `PublicationTransformReceipt` contract | Rich receipt semantics | Draft; no emitted records |
| PublicationTransformReceipt schema | Paired path exists | Empty permissive scaffold |
| RedactionReceipt schema | Named schema path exists | Empty permissive, no contract ref, Fauna-sourced |
| Sensitivity registry README | Control-state and pointer boundary | No concrete records/authority established |
| Sensitivity receipts README | Process-memory boundary | No instances/layout/signing established |
| Sensitive-geometry fixture README | Detailed conflict/current-state inventory | Direct lane README-only |
| Public-no-leak and candidate/site tests | Named test paths exist | Docstring-only placeholders |
| Sensitive-geometry validator README | Intended validator responsibilities | README-only; no executable surfaced |
| Shared PolicyDecision schema | Finite machine outcomes and sensitivity family | Status `PROPOSED`; evaluator/consumer use unverified |
| Domain-Archaeology workflow | Explicit structure/readiness holds | Does not apply policy or publish |
| This revision | Repository-grounded policy boundary | Documentation, not enforcement or approval |

[Back to top](#top)

---

## Changelog

### v0.2 — 2026-07-19

- Replaced the generic v0.1 guide with a repository-grounded sensitivity-policy boundary.
- Added a pinned evidence snapshot and explicit truth-label split.
- Recorded direct child-lane README-only maturity.
- Directly inventoried all ten domain-level Archaeology Rego scaffolds and their default-false/no-rule-body posture.
- Recorded the absent checked cross-cutting Archaeology sensitivity README and unresolved policy composition.
- Distinguished sensitivity classification, policy decision, profile, transform, receipt, registry, review, evidence, promotion, release, and public carrier.
- Added immutable input requirements, most-restrictive propagation, profile admission, exact-detail and reverse-inference controls, cultural/CARE/rights/consent handling, decision normalization, safe reasons and obligations.
- Added receipt/registry/evidence/release boundaries, public API/UI/MapLibre/tile/search/graph/export/cache/embedding/AI controls, log minimization, deterministic test matrix, threat model, implementation sequence, definition of done, conflict register, open verification, correction, revocation, withdrawal, and rollback.
- Preserved draft doctrine without accepting or inventing runtime profile values or numeric thresholds.
- Added a generated provenance receipt separately.
- Changed no executable policy, profile, transform, receipt, release, or public behavior.

### v0.1 — 2026-06-15

- Introduced a bounded Archaeology sensitivity-policy sublane.
- Documented sensitivity gates, obligations, record expectations, and open verification items.

---

KFM rule: Archaeology sensitivity policy must deny or narrow exact and reverse-engineerable protected detail, preserve the most restrictive applicable authority/rights/consent/review posture, and require accepted deterministic transforms, receipts, evidence, release, correction, and rollback before broader use. Documentation, a default-false stub, schema validity, a profile name, a generalized-looking map, or a prior publication is never sufficient authority.

<p align="right"><a href="#top">Back to top</a></p>
