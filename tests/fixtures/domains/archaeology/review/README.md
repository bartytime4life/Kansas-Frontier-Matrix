# `tests/fixtures/domains/archaeology/review/` — Archaeology Review Test-Local Fixture and Cultural-Authority Boundary

> Repository-grounded routing, fixture, and safety contract for test-local Archaeology review-shaped examples. This lane may describe small synthetic manifests and expectations owned by specific tests, but it does not perform review, prove consultation or consent, establish cultural authority, approve policy or release, create archaeology truth, or expose protected archaeological detail.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-domains-archaeology-review-readme
title: tests/fixtures/domains/archaeology/review/README.md — Archaeology Review Test-Local Fixture and Cultural-Authority Boundary
type: readme; directory-readme; test-local-fixture-lane; archaeology-review-fixture-routing-boundary; cultural-authority-test-boundary
version: v0.2
status: draft; repository-grounded; README-only-direct-lane; archaeology-parent-confirmed; domains-parent-index-absent; reusable-review-placeholders-confirmed; StewardReview-contract-confirmed-schema-permissive; CulturalReview-contract-confirmed-schema-permissive; ReviewRecord-contract-schema-vocabulary-conflicted; ReviewRecord-validator-stub; substantive-domain-review-tests-unestablished; substantive-ci-unestablished; non-authoritative
owners: OWNER_TBD — Archaeology domain steward · Test steward · Fixture steward · Review steward · Cultural-review liaison · Rights-holder representative · Sensitivity reviewer · Governance steward · Contract/schema steward · Evidence steward · Policy steward · Release steward · Correction/rollback steward · Security reviewer · CI steward · Docs steward
created: 2026-07-06
updated: 2026-07-16
supersedes: v0.1
policy_label: public-doc; tests; fixtures; archaeology; review-fixtures; test-local-only; synthetic-only; no-network-default; deny-by-default; exact-location-denied; candidate-not-confirmed; cultural-authority-deferred; consent-not-inferred; consultation-not-inferred; evidence-required; policy-gated; release-subordinate; correction-aware; rollback-aware; no-publication
current_path: tests/fixtures/domains/archaeology/review/README.md
truth_posture:
  CONFIRMED:
    - target README v0.1 and prior blob
    - Directory Rules and tests/fixtures responsibility split
    - tests/fixtures parent README
    - tests/fixtures/domains/archaeology parent README and review child index
    - tests/domains/archaeology and tests/domains/archaeology/fixtures READMEs
    - root fixtures and reusable Archaeology fixture READMEs
    - reusable synthetic_steward_review README
    - approve.json and deny.json are four-field PROPOSED placeholders
    - StewardReview and CulturalReview semantic contracts
    - StewardReview and CulturalReview paired permissive PROPOSED schemas
    - generic ReviewRecord semantic contract
    - generic ReviewRecord paired PROPOSED schema and valid/invalid fixture family
    - generic ReviewRecord validator file is a NotImplementedError stub
    - common schema harness collects governance schema fixtures
    - Archaeology cultural-review protocol, review duties, and review-receipt README
    - TODO-only Makefile fixture behavior and domain-archaeology workflow behavior
    - checked absence of tests/fixtures/domains/README.md
    - checked absence of direct-lane conftest.py, manifest_expectations.json, and representative test module
    - checked absence of tests/domains/archaeology/fixtures/review/README.md
  CONFLICTED:
    - v0.1 claim that tests/fixtures/domains/archaeology/README.md was absent
    - v0.1 proposed executable test modules inside a fixture directory versus current parent guidance that executable tests belong in owning test lanes
    - generic ReviewRecord schema decisions approve/reject/request_changes versus broader semantic-contract dispositions and domain review states
    - generic ReviewRecord schema metadata points to lowercase contracts/governance/review_record.md while the confirmed semantic contract is contracts/governance/ReviewRecord.md
    - reusable approve.json and deny.json filenames imply outcomes while their payloads are only planned-file placeholders
    - rich review doctrine versus incomplete domain schemas, validators, fixtures, policy enforcement, tests, and CI
  UNKNOWN:
    - exhaustive direct-lane inventory outside checked paths
    - generated, ignored, branch-local, dynamic, or externally stored review fixtures
    - real reviewer rosters, consultation records, consent records, rights-holder authority, and cultural-authority workflows
    - branch-protection significance and complete repository-wide workflow trigger set
    - current review-fixture pass rates and production/release use
  NEEDS_VERIFICATION:
    - lane-retention decision
    - tests/fixtures/domains parent index
    - exact test-local fixture admission threshold
    - accepted Archaeology review manifest contract and identifier vocabulary
    - adapter relationship among StewardReview, CulturalReview, and ReviewRecord
    - canonical review-state, disposition, decision, reason-code, and obligation vocabularies
    - non-placeholder reusable StewardReview and CulturalReview payloads
    - active consumer tests and consumer backlinks
    - policy bundle syntax and runtime enforcement
    - cultural, sovereignty, rights, consent, consultation, and sensitivity review workflow
    - separation-of-duties enforcement
    - substantive CI ownership and promotion-blocking behavior
    - correction, withdrawal, cache invalidation, revocation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: ba141d8ee7092427936161ad7b954fc449036601
  target_prior_blob: 5713f67701fa923804f77d3adb6660359390f2f7
  uploaded_prompt:
    filename: Pasted text(34).txt
    version: "3.1.0"
    sha256: b061d3d8b153af8083cd1f62f447b389c396b5a882e590328ede7c3e3ff25e85
  related_repository_blobs:
    directory_rules: 2affb080e6f0043867c64c7f06c1ca52030fbd55
    schema_home_adr: ab0010a278d766356845c23055f882f328abb418
    drift_register: 97a775522dcd058299f752ac7862d0fc56c13280
    tests_fixtures_parent_readme: 2d0147e85eae86f687e85c5bea0d3e61f9c3a8f7
    fixtures_root_readme: b096b0ed49c8e7d95ddb0d4c813d06ef40f1528d
    archaeology_test_fixtures_parent: 34b8aa536aa19c234f30f939ed1c06fa428b57dc
    archaeology_domain_tests_readme: 2b739d5bdf322de4523faa09a2b788be910bf8b0
    archaeology_fixture_tests_readme: 9ef754a4b4111862ce4bfa1a435b69841df52c6a
    archaeology_reusable_fixture_readme: ab348d4a5345d52cb0999072138e7c0feb63e8f1
    synthetic_steward_review_readme: 78f623961ff8a2da596741863a7243aa0073e444
    synthetic_steward_review_approve: bdf1226fe48a4005767df4b0b232cbb4bfae804a
    synthetic_steward_review_deny: 2408e3018b0e8335559648d35b334755f1d8e2d1
    steward_review_contract: 986ce11a30a02cf4025c763182f463c57d1894b0
    steward_review_schema: 4888b5934e6bcfb6d15eae39b8c6b2eefa303f1c
    cultural_review_contract: 98511de808d07668ddf9e6364dad3a2804ea8828
    cultural_review_schema: 7f2e1a3f7ef4d6b43ad77614e30803671379636d
    review_record_contract: 9641345d1e5d939dc59687a900e60a563d92c4f0
    review_record_schema: fe2f2223af46481e7fb19b0baa94f62ce9c6c855
    review_record_validator: e1aa5fcc4b2da4055eb61276a031512512bcb4ca
    review_record_fixture_readme: fccac522a0c178bb87fdaf3c7d932861a40786da
    common_schema_fixture_test: b04342cc034d7f1cc554e155fdd02d6e972976e6
    review_duties_doc: f815ffe1417d883dfbd671f1112dd25b73f94037
    cultural_review_protocol: 2097297fc05b371964e61c3c06481652d33b85b9
    archaeology_review_receipts_readme: 083abe1b8dfa1b8f10f87b72858c2f6ebc0d95be
    sibling_api_readme: 054905beab4e847588569d3306f56a71e9a1c48e
    sibling_promotion_readme: e16733aa226e5eb24f09225e64bc920cbb0b32a3
    makefile: 4dc8cf633581893d83fba53219c6ea847992e6be
    domain_archaeology_workflow: b6a2869314efe2e34890baa5bbbe41d656629dd3
  direct_lane_files_confirmed:
    - tests/fixtures/domains/archaeology/review/README.md
  checked_absent_paths:
    - tests/fixtures/domains/README.md
    - tests/fixtures/domains/archaeology/review/conftest.py
    - tests/fixtures/domains/archaeology/review/manifest_expectations.json
    - tests/fixtures/domains/archaeology/review/test_review_fixture_manifest_shape.py
    - tests/domains/archaeology/fixtures/review/README.md
  bounded_inventory_note: Direct path checks and bounded repository search establish only the checked snapshot; they do not prove permanent absence from history, ignored files, generated workspaces, branch-local changes, dynamic fixtures, external storage, or uninspected paths.
related:
  - ../README.md
  - ../api/README.md
  - ../promotion/README.md
  - ../../../README.md
  - ../../../../README.md
  - ../../../../domains/archaeology/README.md
  - ../../../../domains/archaeology/fixtures/README.md
  - ../../../../../fixtures/README.md
  - ../../../../../fixtures/domains/archaeology/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_steward_review/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_steward_review/approve.json
  - ../../../../../fixtures/domains/archaeology/synthetic_steward_review/deny.json
  - ../../../../../fixtures/contracts/v1/governance/review_record/README.md
  - ../../../../../contracts/domains/archaeology/steward_review.md
  - ../../../../../contracts/domains/archaeology/cultural_review.md
  - ../../../../../contracts/governance/ReviewRecord.md
  - ../../../../../schemas/contracts/v1/domains/archaeology/steward_review.schema.json
  - ../../../../../schemas/contracts/v1/domains/archaeology/cultural_review.schema.json
  - ../../../../../schemas/contracts/v1/governance/review_record.schema.json
  - ../../../../../tools/validators/validate_review_record.py
  - ../../../../../docs/domains/archaeology/CULTURAL_REVIEW.md
  - ../../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../../docs/governance/REVIEW_DUTIES.md
  - ../../../../../data/receipts/archaeology/review/README.md
  - ../../../../../docs/doctrine/directory-rules.md
  - ../../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../../../docs/registers/DRIFT_REGISTER.md
  - ../../../../../.github/workflows/domain-archaeology.yml
  - ../../../../../Makefile
notes:
  - "v0.2 corrects the stale claim that tests/fixtures/domains/archaeology/README.md is absent; that parent exists and indexes this review lane."
  - "The direct review fixture lane is README-only in bounded repository evidence."
  - "Executable tests do not belong in this fixture directory by default; they belong in an owning tests/ lane and consume declarative fixtures by reference."
  - "StewardReview and CulturalReview have rich semantic contracts but only permissive empty-property PROPOSED schemas."
  - "The generic ReviewRecord family has a stricter PROPOSED schema and valid/invalid fixtures, but its dedicated validator raises NotImplementedError."
  - "The ReviewRecord schema points to a lowercase contract path while the confirmed contract filename is ReviewRecord.md."
  - "Generic ReviewRecord decisions and domain review states are not silently treated as one vocabulary."
  - "The reusable approve.json and deny.json files are planned-file placeholders; their filenames do not prove review outcomes."
  - "The domain-archaeology workflow and relevant Makefile targets are TODO-only; this revision creates no executable enforcement."
  - "This revision changes documentation only and creates no fixture payload, test, schema, contract, policy, validator, workflow, data object, receipt, proof, release record, map artifact, AI output, consent record, consultation record, or public artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<p>
  <img alt="Document status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Direct inventory: README only" src="https://img.shields.io/badge/direct__inventory-README__only-lightgrey">
  <img alt="Scope: test local" src="https://img.shields.io/badge/scope-test__local-blue">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-8a6d3b">
  <img alt="Sensitivity: deny by default" src="https://img.shields.io/badge/sensitivity-deny__by__default-critical">
  <img alt="Cultural authority: deferred" src="https://img.shields.io/badge/cultural__authority-deferred-purple">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture__only-red">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose) · [Authority](#authority-and-directory-rules-basis) · [Current state](#confirmed-current-state) · [Review model](#review-object-model-and-anti-collapse-rules) · [Fixture home](#fixture-home-decision-law) · [Admission](#test-local-review-fixture-admission-contract) · [Manifest](#minimum-review-fixture-manifest-contract) · [Consumers](#consumer-backlinks-and-orphan-control) · [Families](#review-fixture-family-routing) · [StewardReview](#stewardreview-semantic-contract-and-schema-posture) · [CulturalReview](#culturalreview-semantic-contract-and-schema-posture) · [ReviewRecord](#reviewrecord-cross-cutting-contract-schema-and-drift) · [Outcomes](#finite-outcomes-and-vocabulary-separation) · [Authority](#cultural-sovereignty-rights-consent-and-consultation-boundary) · [Closure](#evidence-policy-review-and-release-closure) · [Candidate posture](#candidate-confirmed-and-source-role-anti-collapse) · [Sensitivity](#archaeology-sensitivity-and-public-safety) · [Network](#no-network-security-and-side-effects) · [Determinism](#identity-version-hash-generation-and-replay) · [Polarity](#valid-invalid-denied-abstained-held-escalated-and-error-cases) · [Correction](#correction-withdrawal-revocation-supersession-and-rollback) · [Coverage](#inventory-orphans-placeholder-coverage-and-vacuous-meaning-risk) · [Commands](#deterministic-validation-commands) · [CI](#runner-ci-and-promotion-boundary) · [Failure meaning](#failure-interpretation) · [Passing limits](#what-a-passing-suite-does-not-prove) · [Layout](#proposed-layout-and-routing) · [Maintenance](#maintenance-and-fixture-update-rules) · [Migration](#migration-deprecation-and-lane-retention) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [Rollback](#rollback)

---

## Status and evidence boundary

> [!IMPORTANT]
> **Evidence snapshot:** `main@ba141d8ee7092427936161ad7b954fc449036601`
> **Prior target blob:** `5713f67701fa923804f77d3adb6660359390f2f7`
> **Direct lane:** `tests/fixtures/domains/archaeology/review/README.md` only at the bounded snapshot
> **Parent state:** `tests/fixtures/README.md` and `tests/fixtures/domains/archaeology/README.md` exist; `tests/fixtures/domains/README.md` was not found
> **Reusable fixture roots:** `fixtures/domains/archaeology/synthetic_steward_review/` and `fixtures/contracts/v1/governance/review_record/`
> **Executable consumer lane:** `tests/domains/archaeology/fixtures/` exists; a `review/` child is not established in checked evidence
> **Current collection:** the generic schema harness can collect `governance/review_record`; no verified default runner or substantive CI job collects this direct Archaeology review fixture lane

This directory is currently a routing README. It is not a fixture corpus, test suite, review service, consultation archive, consent registry, policy bundle, schema family, evidence store, receipt store, review-record store, release queue, publication surface, or rollback executor.

### Safe conclusions

- **CONFIRMED:** the target README exists.
- **CONFIRMED:** the Archaeology test-fixture parent exists and indexes this review child.
- **CONFIRMED:** the higher `tests/fixtures/domains/README.md` index remains absent at the checked path.
- **CONFIRMED:** the direct lane has no checked `conftest.py`, manifest, or representative test module.
- **CONFIRMED:** executable tests belong in an owning `tests/` lane rather than in a fixture payload directory by default.
- **CONFIRMED:** root `fixtures/` is a reusable/runtime fixture responsibility root distinct from `tests/fixtures/`.
- **CONFIRMED:** `fixtures/domains/archaeology/synthetic_steward_review/` contains a README plus `approve.json` and `deny.json`.
- **CONFIRMED:** `approve.json` and `deny.json` are planned-file placeholders, not StewardReview instances.
- **CONFIRMED:** `StewardReview` and `CulturalReview` semantic contracts exist.
- **CONFIRMED:** their paired schemas accept arbitrary objects because they define no properties and allow additional properties.
- **CONFIRMED:** generic `ReviewRecord` has a stricter PROPOSED schema with one valid and one invalid fixture family.
- **CONFIRMED:** the dedicated ReviewRecord validator is not implemented; it raises `NotImplementedError`.
- **CONFIRMED:** the common schema harness includes the `governance` family and can exercise generic ReviewRecord fixtures.
- **CONFIRMED:** the generic schema path and semantic-contract filename disagree in case/path form.
- **CONFIRMED:** the dedicated Archaeology workflow and relevant Makefile fixture targets are scaffolds/TODO-only.
- **UNKNOWN:** real review, consultation, consent, cultural-authority, release, and branch-protection behavior.
- **NEEDS VERIFICATION:** lane ownership, adapter design, vocabulary convergence, domain-review fixtures, consumer tests, policy/runtime enforcement, and substantive CI.

### Truth labels used here

| Label | Meaning in this README |
|---|---|
| `CONFIRMED` | Verified from repository files or bounded connector checks at the pinned snapshot. |
| `PROPOSED` | A recommended contract, fixture, test, command, path relationship, vocabulary, or implementation not established as current behavior. |
| `UNKNOWN` | Not resolved by inspected evidence. |
| `NEEDS VERIFICATION` | Checkable, but not sufficiently verified to act as fact. |
| `CONFLICTED` | Evidence disagrees or vocabularies/path claims do not align; no silent winner is selected. |
| `DENY` | A prohibited authority, sensitivity, or release interpretation. |
| `ABSTAIN` | Insufficient evidence, authority, context, or scope to make a consequential review claim. |
| `ERROR` | Test, validator, schema, policy, runtime, or repository failure; fail closed. |

[Back to top](#top)

---

## Purpose

`tests/fixtures/domains/archaeology/review/` documents the admission, routing, safety, and expected-use contract for test-local Archaeology review-shaped fixture material.

The lane exists so maintainers can answer:

1. What review-shaped fixture material may be local to a test?
2. Which reusable fixture root owns domain and cross-cutting review examples?
3. How are `StewardReview`, `CulturalReview`, and `ReviewRecord` kept separate?
4. Which outcomes and states are machine-enforced, semantic proposals, or unresolved?
5. Which tests must prove that review does not collapse into evidence, policy, consent, cultural authority, promotion, release, or publication?
6. What prevents exact location, sacred/burial context, reviewer identity, consultation detail, or community-controlled knowledge from leaking through fixtures, logs, snapshots, or generated text?
7. How are correction, withdrawal, revocation, supersession, and rollback represented without mutating history?

A mature review-fixture lane should support deterministic negative and positive cases while preserving KFM's core posture:

```text
review fixture
  -> fixture admission and sensitivity checks
  -> shape validation where a schema is authoritative enough
  -> semantic/anti-collapse assertions
  -> evidence and policy reference checks
  -> review authority and separation-of-duties checks
  -> release/correction/rollback boundary checks
  -> finite test outcome
```

The fixture lane does not perform the review. It only supplies bounded test material and records expected behavior.

[Back to top](#top)

---

## Authority and Directory Rules basis

Directory Rules choose placement by responsibility.

| Responsibility | Authority home | Relationship to this lane |
|---|---|---|
| Test-local fixture material | `tests/fixtures/` | This lane may hold small declarative wrappers only when owned by specific tests. |
| Executable enforceability | owning `tests/` subtree | Test modules belong here, not beside fixture payloads by default. |
| Reusable Archaeology review examples | `fixtures/domains/archaeology/synthetic_steward_review/` or accepted domain child | Referenced; not duplicated. |
| Generic ReviewRecord schema examples | `fixtures/contracts/v1/governance/review_record/` | Reusable cross-cutting shape fixtures. |
| StewardReview meaning | `contracts/domains/archaeology/steward_review.md` | Semantic authority; fixtures do not redefine it. |
| CulturalReview meaning | `contracts/domains/archaeology/cultural_review.md` | Semantic authority; fixtures do not redefine it. |
| ReviewRecord meaning | `contracts/governance/ReviewRecord.md` | Cross-cutting semantic authority; path drift remains visible. |
| Machine shape | `schemas/contracts/v1/...` | Schema authority; maturity differs by object family. |
| Policy/admissibility | `policy/` | Decides allow/deny/restrict/hold/abstain obligations. |
| Review process memory | `data/receipts/archaeology/review/` or accepted receipt home | Real receipt instances; not test fixtures. |
| Evidence/proof | `data/proofs/` and EvidenceBundle homes | Review references evidence; it is not evidence. |
| Release decisions | `release/` | Review may support but never replaces promotion/release authority. |
| Cultural-review protocol | `docs/domains/archaeology/CULTURAL_REVIEW.md` | Human-facing governance; not executable policy. |
| Reviewer duties | `docs/governance/REVIEW_DUTIES.md` | Separation-of-duties reference; enforcement remains verification-bound. |
| Public API, map, export, UI, and AI surfaces | governed app/release roots | Consume released, public-safe outputs only. |

> [!IMPORTANT]
> Do not use this directory as a review queue, reviewer-note store, consultation archive, consent registry, cultural-knowledge archive, review receipt store, policy decision store, release approval store, evidence store, source registry, map source, or public artifact home.

No new root, schema home, policy home, review home, receipt home, or release home is created by this revision. The existing requested path remains under `tests/`.

[Back to top](#top)

---

## Confirmed current state

### Direct lane inventory

The bounded checks establish:

```text
tests/fixtures/domains/archaeology/review/
└── README.md
```

The following representative direct-lane paths were checked and not found:

```text
tests/fixtures/domains/archaeology/review/conftest.py
tests/fixtures/domains/archaeology/review/manifest_expectations.json
tests/fixtures/domains/archaeology/review/test_review_fixture_manifest_shape.py
```

This is a bounded result, not proof of permanent absence from history, other branches, generated workspaces, ignored files, external storage, or uninspected paths.

### Reusable Archaeology review fixture state

Confirmed reusable lane:

```text
fixtures/domains/archaeology/synthetic_steward_review/
├── README.md
├── approve.json
└── deny.json
```

The README says fixtures must be synthetic, compact, deterministic, reviewable, and tied to a known consumer. The two JSON files are not review records. Their complete content is planned-file metadata:

```json
{
  "status": "PROPOSED",
  "source_doc": "docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md",
  "path": "fixtures/domains/archaeology/synthetic_steward_review/<approve-or-deny>.json",
  "notes": [
    "Placeholder created from docs/domains markdown inventory."
  ]
}
```

Consequences:

- the filenames do not establish `approve` or `deny` semantics;
- the payloads do not conform to the StewardReview recommended fields;
- permissive StewardReview schema validation would not establish semantic validity;
- consumers must not treat these placeholders as review completion, consultation, consent, policy approval, or release readiness;
- the files require explicit replacement, migration, or continued-placeholder documentation before substantive use.

### Generic ReviewRecord fixture state

Confirmed cross-cutting fixture family:

```text
fixtures/contracts/v1/governance/review_record/
├── README.md
├── valid/valid_1.json
└── invalid/invalid_1.json
```

The generic family is discoverable by `tests/schemas/test_common_contracts.py` because `governance` is in its hard-coded family list. That proves shape-test reachability for the generic schema, not Archaeology domain-review coverage.

### Execution and CI state

- `tools/validators/validate_review_record.py` raises `NotImplementedError`.
- `tests/schemas/test_common_contracts.py` can validate generic ReviewRecord fixtures.
- The harness does not scan `schemas/contracts/v1/domains/archaeology/`.
- `make fixtures` remains TODO-only.
- `make test` runs schema and contract test lanes, not this direct review fixture lane.
- `.github/workflows/domain-archaeology.yml` triggers, but its jobs are TODO echo scaffolds.
- No checked `tests/domains/archaeology/fixtures/review/` child exists.
- No substantive review-fixture promotion-blocking CI dependency is established.

[Back to top](#top)

---

## Review object model and anti-collapse rules

KFM currently carries three related review families. They must not be flattened.

| Family | Primary meaning | Current machine posture | Must not collapse into |
|---|---|---|---|
| `StewardReview` | Archaeology-domain steward/domain/data/evidence/release-readiness review posture | Paired schema is permissive empty-property PROPOSED scaffold | evidence proof, CulturalReview, PolicyDecision, ReviewRecord by assumption, release approval |
| `CulturalReview` | Culturally significant, sovereignty-related, sacred/burial, community-held, collection, access, publication, or interpretive review posture | Paired schema is permissive empty-property PROPOSED scaffold | consent, consultation proof, legal compliance, EvidenceBundle, policy approval, release approval |
| `ReviewRecord` | Cross-cutting inspectable governance review event | Paired schema has required fields and closed enums; status PROPOSED; dedicated validator is a stub | PolicyDecision, PromotionDecision, ReleaseManifest, EvidenceBundle, ADR, GitHub comment |

### Required anti-collapse assertions

A mature suite must prove:

- StewardReview does not imply CulturalReview.
- CulturalReview does not imply consent.
- ReviewRecord does not imply policy approval.
- Any review does not imply evidence truth.
- Any review does not confirm a CandidateFeature as an ArchaeologicalSite.
- `approve` does not mean `PUBLISHED`.
- `approve_with_conditions` cannot become unconditional approval.
- `abstain`, `deny`, `reject`, `request_changes`, `escalate`, `blocked`, or `needs evidence` cannot be silently converted to allow.
- reviewer identity or role does not prove independence unless author/reviewer separation is checked.
- a schema-valid object is not semantically valid when required evidence, authority, sensitivity, policy, correction, or release context is absent.
- a public summary is not the internal review record.
- a review receipt is process memory, not proof or release authority.

### Adapter requirement

Because the three families use different field and outcome vocabularies, any adapter between them must be explicit, versioned, tested, and reversible. No filename, helper, serializer, UI label, or generated summary may silently translate one family's outcome into another.

[Back to top](#top)

---

## Fixture home decision law

Use this decision order before adding review fixture material.

1. **Is it a real review, receipt, consultation, consent, policy, evidence, or release record?**
   Do not store it in fixtures.
2. **Is it a reusable generic ReviewRecord shape example?**
   Use `fixtures/contracts/v1/governance/review_record/`.
3. **Is it a reusable Archaeology review example whose domain semantics matter?**
   Use `fixtures/domains/archaeology/synthetic_steward_review/` or an accepted domain child.
4. **Is it a tiny declarative wrapper owned by one review-fixture consumer test?**
   This test-local lane may be appropriate after the admission contract passes.
5. **Is it executable test logic?**
   Put it in `tests/domains/archaeology/fixtures/review/` if that child is accepted, or another verified owning test lane.
6. **Is ownership still unclear?**
   Do not create duplicate copies. Record `NEEDS VERIFICATION` and route the decision to fixture/test stewards.

### Duplication rule

The same logical payload must not be maintained independently in:

- `tests/fixtures/domains/archaeology/review/`;
- `fixtures/domains/archaeology/synthetic_steward_review/`;
- `fixtures/contracts/v1/governance/review_record/`.

A test-local wrapper may reference a reusable payload. It should not clone it.

[Back to top](#top)

---

## Test-local review fixture admission contract

A proposed file in this lane is admissible only when every applicable condition is met.

| Admission question | Required answer |
|---|---|
| Is the file synthetic and public-safe? | Yes |
| Is a specific consumer test identified? | Yes |
| Is the file local to that consumer rather than broadly reusable? | Yes |
| Is the reusable fixture alternative documented? | Yes |
| Is the object family explicit? | `StewardReview`, `CulturalReview`, `ReviewRecord`, or explicit wrapper |
| Is the authority posture explicit? | Fixture only |
| Is the expected test outcome explicit? | Yes |
| Is source role and candidate posture explicit where relevant? | Yes |
| Are sensitivity and audience postures explicit? | Yes |
| Are cultural authority, consent, and consultation non-inference rules explicit? | Yes |
| Are evidence, policy, review, and release references synthetic? | Yes |
| Are exact location and restricted cultural content absent? | Yes |
| Is network access unnecessary? | Yes |
| Are filesystem side effects unnecessary? | Yes |
| Are identity, version, timestamps, and ordering deterministic? | Yes |
| Are correction, revocation, supersession, and rollback expectations explicit where material? | Yes |
| Is the file linked from a manifest/index and consumer? | Yes |
| Would moving it to a reusable root be lossless if reuse expands? | Yes |

A file that cannot answer these questions should remain uncreated, move to the correct responsibility root, or be held pending governance.

[Back to top](#top)

---

## Minimum review fixture manifest contract

No accepted manifest schema is confirmed for this lane. The structure below is **PROPOSED** for review and must not be treated as canonical machine shape.

```json
{
  "fixture_manifest_id": "fixturemanifest:archaeology:review:example-001",
  "fixture_manifest_version": "v0.2-proposed",
  "domain": "archaeology",
  "fixture_scope": "test_local_review_wrapper",
  "fixture_family": "steward_review",
  "review_model": "StewardReview",
  "canonical_fixture_ref": "fixtures/domains/archaeology/synthetic_steward_review/deny.json",
  "consumer_test_refs": [
    "tests/domains/archaeology/fixtures/review/test_review_boundary.py"
  ],
  "mock_marker": true,
  "review_case": "needs_cultural_review_and_more_evidence",
  "reviewed_object_ref": "candidate:archaeology:fixture:001",
  "source_role": "candidate",
  "candidate_state": "unconfirmed",
  "reviewer_role": "domain_steward",
  "reviewer_visibility": "role_only",
  "cultural_authority_ref": null,
  "consultation_ref": null,
  "consent_ref": null,
  "evidence_refs": [
    "evidence-ref:fixture:arch-review-001"
  ],
  "policy_refs": [
    "policy-ref:fixture:arch-review-001"
  ],
  "redaction_receipt_refs": [],
  "release_refs": [],
  "correction_refs": [],
  "rollback_refs": [
    "rollback-ref:fixture:arch-review-001"
  ],
  "expected_test_outcome": "ABSTAIN",
  "expected_domain_review_state": "needs_cultural_review",
  "reason_codes": [
    "CULTURAL_AUTHORITY_UNRESOLVED",
    "EVIDENCE_INSUFFICIENT"
  ],
  "must_not_claim": [
    "REVIEW_APPROVAL_CANARY",
    "CULTURAL_REVIEW_COMPLETED_CANARY",
    "CONSULTATION_COMPLETED_CANARY",
    "CONSENT_GRANTED_CANARY",
    "CANDIDATE_CONFIRMED_CANARY",
    "PROTECTED_LOCATION_PUBLIC_CANARY",
    "POLICY_APPROVAL_CANARY",
    "RELEASE_APPROVAL_CANARY",
    "MAP_TRUTH_CANARY",
    "AI_TRUTH_CANARY"
  ]
}
```

### Manifest rules

- `canonical_fixture_ref` must resolve to a synthetic fixture.
- `consumer_test_refs` must not be empty once the file is admitted.
- `mock_marker` must be true.
- Real reviewer, participant, community, tribe/nation, owner, consultation, consent, revocation, or location data must not appear.
- A null authority, consultation, consent, evidence, policy, or release ref must produce a fail-closed expected outcome when material.
- `expected_test_outcome` is test vocabulary, not ReviewRecord or PolicyDecision vocabulary.
- Unknown fields, versions, models, and reason codes require explicit failure or review.
- Hashing/canonicalization rules remain `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Consumer backlinks and orphan control

Every admitted fixture must be bidirectionally traceable.

### Fixture to consumer

The fixture or manifest should identify:

- consumer test path;
- object family and schema/contract refs;
- expected outcome;
- reason-code expectations;
- sensitivity posture;
- review-authority posture;
- correction/rollback expectations;
- fixture version or digest.

### Consumer to fixture

The consuming test should identify:

- exact fixture path;
- why the fixture is test-local;
- which contract/schema/policy rule is being asserted;
- which negative canaries are expected;
- which network and side-effect constraints apply.

### Orphan checks

A mature inventory check should fail when:

- a fixture has no consumer;
- a consumer references a missing fixture;
- a manifest references a reusable placeholder without declaring placeholder status;
- a canonical fixture is copied into the test-local lane;
- the same fixture ID appears in multiple authority homes;
- a reusable fixture is renamed without updating consumers;
- a review record references no reviewed object;
- an approval-like case has no evidence/policy/authority basis;
- an invalid fixture has no expected failure;
- a fixture family has only a README and no explicit documentation-only status.

[Back to top](#top)

---

## Review fixture family routing

| Fixture family | Preferred reusable home | Expected test responsibility | Boundary |
|---|---|---|---|
| Generic ReviewRecord valid/invalid shape | `fixtures/contracts/v1/governance/review_record/` | schema shape and closed-enum behavior | not domain review completion |
| StewardReview semantic examples | `fixtures/domains/archaeology/synthetic_steward_review/` after placeholder replacement | domain review states, evidence/policy/release anti-collapse | not cultural review or approval |
| CulturalReview semantic examples | accepted Archaeology cultural-review fixture child, if created | cultural-authority, consent, participant-visibility, restriction, escalation, revocation | not cultural knowledge or consent by itself |
| Test-local manifest/wrapper | this lane | routing, consumer binding, no-network, expected outcomes | not reusable authority |
| ReviewRecord receipt examples | receipt fixture root if accepted | process-memory shape and reference separation | not real receipt storage |
| Review-release integration examples | release fixture root | review reference required for promotion/release | review does not publish |
| Review-correction examples | correction/rollback fixture roots | supersession, revocation, withdrawal, rollback references | no silent edit |
| Public-summary examples | public-safe fixture root | role-only identity, redaction, no restricted detail | not internal review record |
| API/Focus review summaries | API/Focus fixture lanes | cite-or-abstain, release-gated output | not public endpoint authority |

[Back to top](#top)

---

## StewardReview semantic contract and schema posture

### StewardReview confirmed semantic meaning

`StewardReview` records an Archaeology-domain review posture for objects, claims, sources, evidence, validation, transforms, corrections, rollbacks, or release candidates.

It may record:

- requested or pending review;
- blocked or conditionally acceptable state;
- accepted-for-internal-use state;
- needs-evidence, needs-policy, or needs-cultural-review state;
- denied, superseded, withdrawn, or abstain state;
- required actions and related evidence, policy, validation, sensitivity, release, correction, and rollback references.

It does not become:

- EvidenceBundle or proof;
- PolicyDecision;
- CulturalReview;
- consent or consultation;
- legal compliance;
- release approval;
- public permission;
- confirmation of a candidate feature.

### StewardReview confirmed schema posture

The paired schema:

```text
schemas/contracts/v1/domains/archaeology/steward_review.schema.json
```

currently has:

- object root type;
- `PROPOSED` status;
- no properties;
- no required fields;
- `additionalProperties: true`.

Therefore the schema can accept `{}`, the planned-file placeholders, and arbitrary objects. A schema pass cannot support any claim about StewardReview semantic completeness.

### Required test layers

A mature StewardReview suite needs:

1. schema-shape assertions after the schema becomes substantive;
2. semantic required-field assertions;
3. closed review-state vocabulary;
4. reviewed-object reference resolution;
5. evidence and policy reference behavior;
6. candidate-vs-confirmed protection;
7. CulturalReview non-inference;
8. release-approval non-inference;
9. sensitivity and participant-visibility checks;
10. correction/supersession/rollback lineage checks.

[Back to top](#top)

---

## CulturalReview semantic contract and schema posture

### CulturalReview confirmed semantic meaning

`CulturalReview` records a governed culturally significant review posture where sovereignty, community-held knowledge, sacred places, burial contexts, repatriation, collection access, public narrative, publication exposure, correction, suppression, or rollback may matter.

It may record:

- requested, pending, in-review, concern-raised, restricted, conditionally acceptable, denied, abstain, release-candidate, superseded, or withdrawn state;
- controlled reviewer/authority references;
- participant visibility;
- restrictions and required actions;
- evidence, source, policy, review, release, correction, and rollback references.

It does not become:

- cultural knowledge itself;
- automatic consent;
- proof of consultation;
- legal compliance;
- EvidenceBundle;
- PolicyDecision;
- ReleaseManifest;
- permission to disclose sacred/burial context, exact location, participant identity, community-controlled knowledge, or sensitive collection detail.

### CulturalReview confirmed schema posture

The paired schema:

```text
schemas/contracts/v1/domains/archaeology/cultural_review.schema.json
```

currently has:

- object root type;
- `PROPOSED` status;
- no properties;
- no required fields;
- `additionalProperties: true`.

A schema pass cannot establish authority, consent, consultation, restrictions, evidence closure, participant visibility, or release readiness.

### Named-authority rule

Where cultural or community authority applies, KFM records and defers to the named authority. Test fixtures must not manufacture authority by using plausible organization names, generic reviewer roles, or synthetic "approved" labels.

Use role-only and clearly synthetic values. Do not embed cultural knowledge, restricted narratives, real consultation substance, or real participant identity.

[Back to top](#top)

---

## ReviewRecord cross-cutting contract, schema, and drift

### Semantic contract

The confirmed contract is:

```text
contracts/governance/ReviewRecord.md
```

It defines an inspectable review event: who reviewed what, in which role, against what evidence/policy context, with what finding and disposition.

The semantic contract proposes dispositions including:

- `approve`;
- `approve_with_conditions`;
- `request_changes`;
- `abstain`;
- `deny`;
- `escalate`;
- `informational`.

### Machine schema

The paired schema is:

```text
schemas/contracts/v1/governance/review_record.schema.json
```

It requires:

- `review_id`;
- `subject_ref`;
- `reviewer_role`;
- `decision`;
- `reasons`;
- `obligations`;
- `reviewed_at`.

Its closed enums are:

```text
reviewer_role: steward | reviewer | auditor
decision: approve | reject | request_changes
```

### Confirmed drift

1. Schema metadata points to `contracts/governance/review_record.md`.
2. The confirmed semantic contract is `contracts/governance/ReviewRecord.md`.
3. The semantic contract disposition vocabulary is broader than the schema decision vocabulary.
4. The semantic contract proposes fields such as author, basis refs, policy context, sensitivity context, conditions, expiry, supersession, release refs, receipts, and rollback that the current schema does not model.
5. The dedicated validator raises `NotImplementedError`.
6. The generic schema harness can validate the existing generic fixture pair, but that does not resolve semantic or domain-review drift.

This README does not choose a winner. Resolution requires schema/contract review, an adapter decision, or an ADR/migration note if authority/path behavior changes.

[Back to top](#top)

---

## Finite outcomes and vocabulary separation

Different layers use different vocabularies. Tests must not conflate them.

| Layer | Confirmed/proposed vocabulary | Meaning |
|---|---|---|
| Test execution | `PASS`, validation failure, `ERROR`, skipped/not run | Whether assertions executed and passed |
| Generic ReviewRecord schema | `approve`, `reject`, `request_changes` | Current machine decision enum |
| ReviewRecord semantic contract | `approve`, `approve_with_conditions`, `request_changes`, `abstain`, `deny`, `escalate`, `informational` | Proposed governance dispositions |
| StewardReview domain states | requested, pending, blocked, conditional, internal-use, needs evidence/policy/cultural review, denied, superseded, withdrawn, abstain | Proposed domain review posture |
| CulturalReview domain states | requested, pending, in review, abstain, concern raised, conditional, restricted, denied, internal-use, release-candidate, superseded, withdrawn | Proposed cultural review posture |
| Policy | `ALLOW`, `DENY`, `RESTRICT`, `HOLD`, `ABSTAIN`, `ERROR` or bundle-specific equivalent | Admissibility/obligations |
| PromotionDecision | `APPROVE`, `DENY`, `ABSTAIN` | Lifecycle transition decision |
| Runtime response | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Public/governed response behavior |
| Lifecycle | RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED | Artifact state |

### Required behavior

- Store the original vocabulary and model version.
- Translate only through a named adapter.
- Test every mapping and unmapped value.
- Fail closed on unknown values.
- Never map `approve` directly to `PUBLISHED`.
- Never map `accepted for internal use` to public release.
- Never map `review completed` to consent.
- Never map `consultation_ref` presence to consultation sufficiency without governed validation.
- Never map `ABSTAIN` to `approve`.
- Never map test `PASS` to policy or release approval.

[Back to top](#top)

---

## Cultural, sovereignty, rights, consent, and consultation boundary

### Cultural authority

KFM records who or what authority was identified, what review state was recorded, and what restrictions or obligations apply. It does not define the substance of cultural knowledge or replace the named authority.

### Consent

A review record is not a consent record. Consent must be represented through a governed consent/authorization family when applicable, with scope, validity, revocation, and authority.

### Consultation

A fixture may model a synthetic consultation reference. It must not claim real consultation happened, was sufficient, or created authority.

### Sovereignty and rights

Sovereignty, authority-to-control, source rights, redistribution rights, collection access, and publication rights remain separate checks. One favorable review does not satisfy the others.

### Participant identity

Fixtures should use synthetic role/category references. They must not contain real reviewer, community, tribe/nation, landowner, donor, descendant, interviewee, repository-contact, or rights-holder identity.

### Separation of duties

Where review independence matters, fixtures must model both author/producer and reviewer role/identity refs and assert they are distinct under the applicable rule.

A single self-review must not satisfy sensitive-lane release readiness merely because a fixture says `approve`.

[Back to top](#top)

---

## Evidence, policy, review, and release closure

A review-shaped fixture is not closed merely because fields exist.

### Evidence closure

For consequential claims:

- EvidenceRef should resolve to EvidenceBundle;
- missing, stale, conflicted, or unsupported evidence produces `ABSTAIN`, `DENY`, `HOLD`, or expected failure;
- review comments do not become evidence;
- reviewed-object refs must resolve within the synthetic fixture graph.

### Policy closure

- identify policy bundle/version/hash when modeled;
- preserve obligations and restrictions;
- fail closed when policy context is missing or unknown;
- review recommendations do not replace PolicyDecision.

### Review closure

- identify review model and state/disposition;
- identify reviewer role and visibility;
- identify authority basis when cultural/rights review applies;
- identify conditions, blockers, expiry, supersession, and related review refs;
- distinguish completed review from sufficient review.

### Release closure

- review may support release readiness but does not issue PromotionDecision or ReleaseManifest;
- public-bound cases need release refs, correction path, and rollback support where required;
- absence of release state blocks public API/map/export/Focus/AI expectations;
- fixtures must not write release records.

[Back to top](#top)

---

## Candidate-confirmed and source-role anti-collapse

Review fixtures must preserve epistemic state.

| Input state | Forbidden shortcut | Expected posture |
|---|---|---|
| CandidateFeature | steward review approves data quality | Remains candidate unless confirmation evidence/process exists |
| RemoteSensingAnomaly | review finds it plausible | Remains anomaly/candidate |
| LiDARCandidate | review recommends field follow-up | Remains candidate |
| Context-only source | reviewer finds it useful | Remains context-only |
| Aggregated source | review accepts for comparison | Does not become primary authority |
| Cultural concern | review records concern | Concern may gate action; it is not site proof |
| Review denied/abstained | UI wants a simple label | Preserve denial/abstention; do not coerce to unknown/allow |
| Public-safe transform | review accepts transform | Does not authorize publication by itself |

Canaries should detect phrases or fields that upcast:

- candidate to confirmed site;
- review to evidence;
- generic steward review to cultural review;
- cultural review to consent;
- context source to authority;
- review acceptability to policy allow;
- release readiness to published;
- map display to truth;
- generated summary to authority.

[Back to top](#top)

---

## Archaeology sensitivity and public safety

The lane is deny-by-default for:

- exact archaeological coordinates or footprints;
- reverse-geocodable location hints;
- burial or human-remains context;
- sacred-place details;
- community-controlled or culturally restricted knowledge;
- collection-security information;
- looting-risk information;
- private-landowner or participant identity;
- consultation/consent tokens;
- restricted repository or accession details;
- unpublished source packets;
- raw internal review rationale;
- real reviewer communications.

### Public-safe review summaries

A public-safe synthetic summary should expose only what a governed released surface would need, such as:

- review status category;
- public-safe restriction summary;
- role category instead of participant identity;
- evidence/release availability badge;
- correction/supersession state;
- abstention/denial reason that does not leak restricted substance.

The fixture must not include the sensitive reason merely to prove it was withheld. Use a canary token or controlled synthetic ref.

[Back to top](#top)

---

## No-network, security, and side effects

Default review-fixture tests must not:

- call source APIs;
- call consultation/review systems;
- call identity providers;
- call policy or release services;
- call geocoders, maps, tiles, or external assets;
- call AI/model runtimes;
- access secrets or production credentials;
- read RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, receipt, proof, or release stores directly;
- write to governed roots;
- emit real review records, receipts, policy decisions, releases, corrections, or rollback cards;
- upload artifacts containing protected or restricted details.

### Required controls

- synthetic local inputs only;
- network disabled or intercepted;
- deterministic clocks/IDs;
- temporary writable directory only;
- governed roots read-only or unavailable;
- secret-pattern scan;
- protected-canary scan;
- test cleanup;
- no hidden fallback to live services;
- fail closed on missing dependency.

[Back to top](#top)

---

## Identity, version, hash, generation, and replay

Each substantive fixture should identify:

- stable fixture ID;
- fixture version;
- review model and model version;
- contract/schema refs;
- generation method or authoring note;
- source/reusable-fixture refs;
- consumer refs;
- canonical digest once a rule is accepted;
- deterministic timestamp/clock policy;
- expected outcome and reason codes;
- superseded fixture ref when revised.

### Replay rules

A replay should produce:

- the same parsed fixture;
- the same deterministic IDs;
- the same ordering;
- the same expected outcome;
- the same public-safe projection;
- no network traffic;
- no governed-root writes;
- no secret or protected-detail leakage.

Unknown schema versions, review models, adapter versions, or fixture digests must not be silently accepted.

[Back to top](#top)

---

## Valid, invalid, denied, abstained, held, escalated, and error cases

A complete suite needs more than `approve.json` and `deny.json`.

| Case | Minimum example | Expected behavior |
|---|---|---|
| Valid generic ReviewRecord shape | all generic schema-required fields | schema pass only |
| Invalid generic ReviewRecord shape | missing required field | schema failure |
| Valid StewardReview semantics | subject, role, state, refs, sensitivity, actions | semantic pass once accepted |
| Invalid StewardReview semantics | arbitrary object accepted by permissive schema | semantic failure despite schema pass |
| Cultural review required | StewardReview requests CulturalReview | no inference; route/hold |
| Cultural authority unresolved | no authority ref | `HOLD`, `ABSTAIN`, or `DENY` |
| Consent absent | release-like request without consent where required | fail closed |
| Consultation not demonstrated | fixture only names a consultation ref | fail review sufficiency |
| Approve with conditions | unresolved condition remains | block unconditional use |
| Request changes | blocker exists | block next trust-bearing step |
| Abstain | insufficient evidence/authority | preserve abstention |
| Deny/reject | prohibited exposure or unsupported action | preserve denial |
| Escalate | reviewer lacks authority | route; do not approve |
| Informational | context-only review | no trust effect |
| Self-review conflict | same author/reviewer where separation required | fail or hold |
| Candidate upcast | candidate reviewed as plausible | remain candidate |
| Exact-location canary | protected coordinate/hint appears | `DENY` / validation failure |
| Public-summary leak | internal rationale appears in public projection | fail |
| Stale/expired review | expiry passed | hold/refresh required |
| Superseded review | later review replaces earlier | preserve lineage |
| Revoked consent/authority | revocation ref applies | invalidate dependent use |
| Correction/withdrawal | published carrier depends on changed review | invalidate/rebuild/withdraw |
| Rollback | review or release found unsafe | exercise dry-run rollback refs |
| Network attempt | loader calls external service | `ERROR` |
| Governed-root write | test writes receipt/release/data | `ERROR` |
| Validator stub | dedicated validator executed | expected failure; not a pass gate |
| Unknown vocabulary | unrecognized state/decision | fail closed |

[Back to top](#top)

---

## Correction, withdrawal, revocation, supersession, and rollback

Review history must be append-only or explicitly superseding, not silently overwritten.

### Required test concepts

- a new review supersedes a prior review through an explicit ref;
- prior records remain auditable;
- review expiry or revocation invalidates dependent readiness;
- consent revocation is a live fail-closed input where applicable;
- correction does not erase prior state;
- withdrawal invalidates dependent public carriers;
- cache/map/API/AI summaries do not retain stale favorable review state;
- rollback references a known prior safe state;
- rollback tests use dry-run/synthetic targets and do not write release state;
- failed correction or rollback remains visible as `ERROR`/`HOLD`.

A changed fixture should update consumers, expected outputs, indexes, and supersession notes together.

[Back to top](#top)

---

## Inventory, orphans, placeholder coverage, and vacuous-meaning risk

### Direct lane inventory gate

The direct lane is README-only. Do not claim review-fixture payload coverage until a bounded inventory proves otherwise.

### Placeholder gate

The current reusable Archaeology `approve.json` and `deny.json` files are placeholders. A test that only checks their presence proves planned-path presence, not review behavior.

A non-placeholder gate should require at least one field that belongs to the accepted review model and reject the planned-file placeholder shape for substantive review tests.

### Schema permissiveness gate

Both domain review schemas currently accept arbitrary objects. Therefore:

```text
schema pass != domain review validity
```

Tests must include semantic assertions until the schemas become substantive.

### Generic ReviewRecord coverage gate

The generic fixture family has one valid and one invalid case. That is real shape coverage for the current generic schema, but it is not:

- StewardReview coverage;
- CulturalReview coverage;
- Archaeology sensitivity coverage;
- consultation/consent coverage;
- release integration coverage;
- separation-of-duties coverage;
- runtime policy coverage.

### Orphan/nonempty gate

Before promotion claims, prove:

- nonempty domain-review fixture inventory;
- every fixture has a consumer;
- every consumer has a fixture;
- placeholders are excluded or explicitly tested as placeholders;
- valid and invalid polarity exists;
- denied/abstained/held/escalated/error cases exist;
- expected failures are specific;
- no duplicate IDs or logical payloads exist across roots.

[Back to top](#top)

---

## Deterministic validation commands

These commands are an inspection and targeted shape-validation starting point. They do not establish complete review behavior.

```bash
# Inventory the direct lane and adjacent owning/reusable lanes.
find tests/fixtures/domains/archaeology/review \
  tests/domains/archaeology/fixtures \
  fixtures/domains/archaeology/synthetic_steward_review \
  fixtures/contracts/v1/governance/review_record \
  -maxdepth 6 -type f 2>/dev/null | sort

# Inspect the review contract/schema/validator surfaces.
find contracts/domains/archaeology contracts/governance \
  schemas/contracts/v1/domains/archaeology schemas/contracts/v1/governance \
  tools/validators \
  -maxdepth 5 -type f 2>/dev/null | sort | grep -Ei 'review|archaeology'

# Run the existing generic ReviewRecord schema fixture case.
python -m pytest -q tests/schemas/test_common_contracts.py -k review_record
```

### Dedicated validator warning

Do not use this as a green gate:

```bash
python tools/validators/validate_review_record.py
```

The checked file raises `NotImplementedError`. Its failure proves the dedicated validator is a stub; it does not mean the schema fixture harness is unavailable.

### Proposed future command

```bash
# PROPOSED / NEEDS VERIFICATION after an owning test child exists.
python -m pytest -q tests/domains/archaeology/fixtures/review
```

Required execution posture:

- no network;
- deterministic synthetic inputs;
- no protected detail;
- no governed-root writes;
- no real reviewer/authority/consultation/consent data;
- finite outcomes;
- explicit non-placeholder and nonempty coverage;
- no silent skip treated as pass.

[Back to top](#top)

---

## Runner, CI, and promotion boundary

### Current state

| Surface | Current behavior | Status |
|---|---|---|
| Direct review fixture lane | README only | CONFIRMED bounded snapshot |
| Generic ReviewRecord schema fixtures | one valid and one invalid case | CONFIRMED |
| Generic schema harness | includes governance family | CONFIRMED |
| Dedicated ReviewRecord validator | raises `NotImplementedError` | CONFIRMED stub |
| StewardReview/CulturalReview schemas | permissive empty-property scaffolds | CONFIRMED |
| Archaeology review fixture tests | no checked owning test child | NEEDS VERIFICATION |
| `make test` | schema and contract tests only | CONFIRMED exclusion of direct lane |
| `make fixtures` | TODO echo | CONFIRMED scaffold |
| `domain-archaeology` workflow | TODO echo jobs | CONFIRMED scaffold |
| Review-blocking required check | not verified | UNKNOWN |
| CODEOWNERS review mapping for this lane | not verified | UNKNOWN |

### Workflow-trigger note

The dedicated Archaeology workflow triggers on pull requests and pushes to `main`, but its checked jobs only check out the repository and echo TODO commands. It does not provide substantive Archaeology review-fixture enforcement.

The full workflow set, path filters, branch rules, required checks, environment secrets, and review platform settings were not exhaustively inspected for this README. Do not infer that no other workflow can run.

### Promotion boundary

CI may provide evidence that review rules were tested. CI must not:

- create or approve real review records from fixture results;
- claim consultation or consent;
- substitute KFM for a named cultural authority;
- publish automatically from a README or fixture change;
- treat generic schema success as domain review readiness;
- bypass human/cultural/rights review;
- expose protected detail in logs or artifacts;
- write PolicyDecision, PromotionDecision, ReviewRecord, ReleaseManifest, receipt, or proof objects without governed authority;
- execute untrusted changed code with privileged secrets without an explicit safe design.

[Back to top](#top)

---

## Failure interpretation

| Failure | Interpretation | Required response |
|---|---|---|
| README structure or link failure | Documentation defect | Fix before merge |
| Missing referenced fixture | Fixture graph incomplete | Fail inventory; no silent substitute |
| Placeholder used as substantive review | Meaning coverage absent | Fail placeholder gate |
| Permissive schema accepts arbitrary object | Shape insufficient | Run semantic assertions; do not claim validity |
| Generic schema failure | Generic ReviewRecord shape rejected | Preserve failure |
| Dedicated validator raises `NotImplementedError` | Validator unimplemented | Report NOT IMPLEMENTED; do not suppress |
| Vocabulary mapping missing | Adapter undefined | Fail closed |
| Missing reviewed object | Review scope unresolved | `ABSTAIN`, `HOLD`, or failure |
| Missing evidence | Evidence closure absent | `ABSTAIN` / `DENY` / `HOLD` |
| Missing policy | Policy closure absent | `HOLD`, `DENY`, `ABSTAIN`, or `ERROR` |
| Missing cultural authority | Authority unresolved | `HOLD`, `ABSTAIN`, or `DENY` |
| Consent/consultation inferred | Governance violation | `DENY`; correct fixture |
| Separation-of-duties failure | Independence absent | block consequential action |
| Candidate upcast | Epistemic/source-role violation | `DENY` / `ABSTAIN` |
| Protected detail detected | Public-safety violation | `DENY`, quarantine, inspect exposure |
| Public-summary leak | Trust-membrane violation | block carrier and correct |
| Network access attempted | Determinism/security violation | `ERROR`; fail test |
| Governed-root write attempted | Side-effect violation | `ERROR`; fail closed |
| Stale/revoked review ignored | Correction/revocation failure | invalidate dependent use |
| Rollback ref missing | Reversibility absent | block public-bound transition |
| CI skipped or TODO-only | Enforcement absent | report NOT RUN/UNKNOWN |

[Back to top](#top)

---

## What a passing suite does not prove

Even a complete green suite would not prove:

- an archaeological site exists;
- a candidate is confirmed;
- a source is authoritative;
- evidence is true outside the synthetic test graph;
- cultural review occurred;
- consultation happened;
- consent was granted;
- consent remains valid;
- a named cultural/community/tribal authority approved anything;
- rights are resolved;
- exact coordinates or restricted details are safe to release;
- reviewer independence exists in production;
- policy is correct or complete;
- a real ReviewRecord was issued;
- a review receipt exists;
- a reviewer approved a real promotion or release;
- a PromotionDecision or ReleaseManifest was emitted;
- a public API, map, tile, export, Focus Mode, or AI response is authorized;
- production correction, revocation, withdrawal, or rollback can execute;
- branch protection requires the suite;
- the repository has no uninspected drift.

Tests provide bounded evidence about their assertions. They do not replace evidence, named authority, policy, review, consent, release, correction, or rollback.

[Back to top](#top)

---

## Proposed layout and routing

The direct lane should remain declarative.

```text
tests/fixtures/domains/archaeology/review/
├── README.md
└── manifest_expectations.json          # PROPOSED only if a specific consumer owns it
```

Executable tests should live in an owning test lane:

```text
tests/domains/archaeology/fixtures/review/
├── README.md                            # PROPOSED child; not currently established
├── test_review_fixture_inventory.py
├── test_review_fixture_manifest.py
├── test_review_model_anti_collapse.py
├── test_review_authority_and_consent_non_inference.py
├── test_review_evidence_policy_release_closure.py
├── test_review_no_network_and_no_writes.py
├── test_review_sensitive_canaries.py
└── test_review_correction_revocation_rollback.py
```

Reusable fixtures remain under their responsibility roots:

```text
fixtures/domains/archaeology/synthetic_steward_review/
fixtures/contracts/v1/governance/review_record/
```

This layout is PROPOSED. Do not create it without confirming child ownership, fixture-home rules, manifest schema, and consumer strategy.

[Back to top](#top)

---

## Maintenance and fixture update rules

When review fixture behavior changes:

1. identify the owning contract/schema/policy;
2. update semantic contract before or with shape changes;
3. update schema version and migration notes where machine shape changes;
4. update reusable fixtures, not test-local copies;
5. update valid, invalid, denied, abstained, held, escalated, error, expiry, revocation, correction, and rollback cases;
6. update expected errors precisely;
7. update consumers and backlinks atomically;
8. update parent/child README indexes;
9. record supersession rather than silent mutation;
10. run generic schema tests and owning domain tests;
11. verify no network or governed-root writes;
12. scan secrets and protected canaries;
13. record CI outcome honestly;
14. preserve rollback to the prior fixture/schema/contract set.

### Placeholder maintenance

Until `approve.json` and `deny.json` become real review fixtures or are removed:

- retain explicit placeholder status;
- do not link them as valid StewardReview cases;
- do not let filename semantics drive expected outcomes;
- add tests that reject them as substantive review records if consumers encounter them;
- update `MISSING_OR_PLANNED_FILES.md` lineage when the placeholders graduate or are superseded.

[Back to top](#top)

---

## Migration, deprecation, and lane retention

Whether this test-local lane should persist remains `NEEDS VERIFICATION`.

### Retain when

- a bounded test owns a small declarative wrapper;
- the wrapper would not be reusable elsewhere;
- the direct lane has a manifest and consumer backlinks;
- duplication checks pass.

### Deprecate or collapse when

- all review fixtures are reusable domain or governance fixtures;
- no consumer needs test-local material;
- the lane is README-only with no distinct responsibility;
- another accepted lane owns the same contract more clearly.

### Migration procedure

1. inventory files and consumers;
2. classify each item as reusable, test-local, executable, receipt-like, or trust-bearing;
3. move only with explicit authorization and history-preserving mechanics;
4. update references and parent indexes atomically;
5. add deprecation/supersession notes;
6. run consumer/orphan checks;
7. preserve rollback to the prior path;
8. do not create a second canonical review or fixture home.

No move, rename, delete, or deprecation is performed by this README revision.

[Back to top](#top)

---

## Definition of done

This lane is ready to support review-fixture coverage claims only when all applicable criteria pass.

| Criterion | Required evidence |
|---|---|
| Parent indexes | `tests/fixtures/domains/README.md` decision and relevant indexes current |
| Lane authority | explicit retain/deprecate decision and owner |
| Model relationship | accepted StewardReview/CulturalReview/ReviewRecord adapter or separation rule |
| Vocabulary | versioned review states, dispositions, decisions, reason codes, and obligations |
| Manifest contract | accepted fields, version, ID, consumer refs, and validator |
| Payload inventory | non-placeholder, public-safe, synthetic cases |
| Polarity | valid, invalid, denied, abstained, held, escalated, error, expired, revoked, correction, and rollback cases |
| Consumers | executable tests load every admitted fixture |
| Orphan control | fixture-to-consumer and consumer-to-fixture checks |
| Generic ReviewRecord schema | path/case drift resolved and fixture tests pass |
| Domain review schemas | substantive closed shapes or explicit semantic validator coverage |
| Dedicated validator | implemented or officially retired |
| Semantics | anti-collapse invariants tested beyond shape |
| Evidence | resolution and missing-evidence behavior tested |
| Policy | exact bundle/version and obligations tested |
| Authority | cultural/sovereignty/rights/consent/consultation non-inference tested |
| Separation of duties | author/reviewer independence behavior tested |
| Sensitivity | exact-location and protected-context canaries denied |
| Side effects | no-network and governed-root write denial enforced |
| Determinism | stable clock, seed, ordering, IDs, versions, and replay |
| CI | substantive jobs execute and report finite outcomes |
| Promotion gate | required-check significance verified; no auto-publication |
| Correction | expiry, revocation, supersession, withdrawal, invalidation, and rollback exercised |
| Documentation | parent/child indexes, commands, evidence, and limitations current |

Until then, this README remains a routing and safety contract, not proof of implemented Archaeology review-fixture coverage.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status | Evidence needed |
|---|---|---|---|
| ARCH-REVIEW-FIX-001 | Should this direct lane be retained? | NEEDS VERIFICATION | fixture-owner and test-owner decision |
| ARCH-REVIEW-FIX-002 | Who owns the lane? | NEEDS VERIFICATION | CODEOWNERS or steward assignment |
| ARCH-REVIEW-FIX-003 | Should `tests/fixtures/domains/README.md` be created? | NEEDS VERIFICATION | parent-tree documentation decision |
| ARCH-REVIEW-FIX-004 | What exact threshold admits test-local review fixtures here? | NEEDS VERIFICATION | accepted fixture-home rule |
| ARCH-REVIEW-FIX-005 | What is the canonical review manifest schema? | UNKNOWN | contract/schema/ADR |
| ARCH-REVIEW-FIX-006 | What is the stable fixture ID/version/hash rule? | NEEDS VERIFICATION | identity contract |
| ARCH-REVIEW-FIX-007 | How do StewardReview, CulturalReview, and ReviewRecord relate? | CONFLICTED / NEEDS VERIFICATION | adapter or separation ADR/contract |
| ARCH-REVIEW-FIX-008 | Which review-state/disposition/decision vocabulary is canonical per model? | CONFLICTED | schema-contract-policy decision |
| ARCH-REVIEW-FIX-009 | Will the ReviewRecord contract path use uppercase or lowercase filename? | CONFLICTED | path migration/metadata correction |
| ARCH-REVIEW-FIX-010 | When will StewardReview schema gain substantive fields? | UNKNOWN | schema PR and review |
| ARCH-REVIEW-FIX-011 | When will CulturalReview schema gain substantive fields? | UNKNOWN | schema PR and review |
| ARCH-REVIEW-FIX-012 | Will the dedicated ReviewRecord validator be implemented or retired? | UNKNOWN | tooling decision |
| ARCH-REVIEW-FIX-013 | Are approve.json and deny.json retained, replaced, or removed? | NEEDS VERIFICATION | fixture review |
| ARCH-REVIEW-FIX-014 | Which executable tests consume Archaeology review fixtures? | UNKNOWN | repository test inventory |
| ARCH-REVIEW-FIX-015 | Where should the executable review test child live? | NEEDS VERIFICATION | parent test-lane decision |
| ARCH-REVIEW-FIX-016 | How are consumer backlinks and orphan checks enforced? | NEEDS VERIFICATION | inventory validator/test |
| ARCH-REVIEW-FIX-017 | Which policy bundle/version governs Archaeology review obligations? | NEEDS VERIFICATION | concrete policy files and registry |
| ARCH-REVIEW-FIX-018 | How is cultural authority represented without exposing restricted identity? | NEEDS VERIFICATION | reviewed contract and fixtures |
| ARCH-REVIEW-FIX-019 | How are consent and consultation represented and revoked? | NEEDS VERIFICATION | governance/policy contracts and tests |
| ARCH-REVIEW-FIX-020 | How are rights-holder obligations enforced? | NEEDS VERIFICATION | policy and review tests |
| ARCH-REVIEW-FIX-021 | What exact public-safe geometry/reason-summary rule applies? | NEEDS VERIFICATION | accepted policy and transform contract |
| ARCH-REVIEW-FIX-022 | How is separation of duties enforced? | NEEDS VERIFICATION | accepted ADR, platform, policy, and tests |
| ARCH-REVIEW-FIX-023 | Which review receipt family is canonical? | NEEDS VERIFICATION | receipt-layout governance |
| ARCH-REVIEW-FIX-024 | How are review expiry and stale states enforced? | NEEDS VERIFICATION | schema/policy/runtime tests |
| ARCH-REVIEW-FIX-025 | How are revocation, correction, and withdrawal propagated to map/API/cache/AI surfaces? | NEEDS VERIFICATION | integration tests |
| ARCH-REVIEW-FIX-026 | How is rollback tested without writing release state? | NEEDS VERIFICATION | dry-run harness |
| ARCH-REVIEW-FIX-027 | Are secret and protected-canary scans enforced? | UNKNOWN | CI/test evidence |
| ARCH-REVIEW-FIX-028 | Are no-network and no-governed-root-write rules enforced? | UNKNOWN | sandbox/test evidence |
| ARCH-REVIEW-FIX-029 | Which workflows trigger on this path? | UNKNOWN | complete workflow inventory |
| ARCH-REVIEW-FIX-030 | Is any review suite required by branch protection? | UNKNOWN | ruleset/check evidence |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| Uploaded implementation prompt v3.1 | CONFIRMED user-supplied instruction | implementation workflow, tests README profile, acceptance, validation, and handoff requirements | repository state |
| `docs/doctrine/directory-rules.md` | CONFIRMED repository doctrine | responsibility-root placement and no parallel authority | target implementation maturity |
| schema-home ADR | CONFIRMED file; status proposed | schema/contract/fixture separation | accepted ADR status or CI enforcement |
| drift register | CONFIRMED file | recorded repository drift | exhaustive drift |
| target v0.1 README | CONFIRMED prior content | preserved safety substance and stale claims to correct | executable fixture coverage |
| `tests/fixtures/README.md` | CONFIRMED | test-local versus reusable fixture split | review lane retention |
| Archaeology test-fixture parent | CONFIRMED | parent exists and indexes review child | payload and consumer maturity |
| Archaeology domain test READMEs | CONFIRMED | executable test ownership and boundaries | review child implementation |
| reusable Archaeology fixtures README | CONFIRMED | domain fixture routing | substantive review payload coverage |
| synthetic steward review README | CONFIRMED | review-shaped fixture lane and non-authority boundary | semantic payload validity |
| `approve.json`, `deny.json` | CONFIRMED placeholders | planned path lineage | approval, denial, schema, or semantic coverage |
| StewardReview contract | CONFIRMED draft v0.2 | semantic meaning and anti-collapse rules | machine enforcement |
| StewardReview schema | CONFIRMED permissive PROPOSED scaffold | file/path pairing | semantic validity |
| CulturalReview contract | CONFIRMED draft v0.2 | cultural-authority and non-consent boundaries | real cultural review or machine enforcement |
| CulturalReview schema | CONFIRMED permissive PROPOSED scaffold | file/path pairing | semantic validity |
| ReviewRecord contract | CONFIRMED draft | cross-cutting review semantics | schema alignment or runtime enforcement |
| ReviewRecord schema | CONFIRMED PROPOSED | required generic fields and enums | broader semantics or Archaeology coverage |
| ReviewRecord validator | CONFIRMED stub | path exists | validator behavior |
| generic ReviewRecord fixture README | CONFIRMED | one valid/invalid schema fixture pair and harness relation | Archaeology domain review behavior |
| common schema harness | CONFIRMED | generic governance fixture discovery | domain Archaeology schema collection |
| Review Duties | CONFIRMED draft | role/separation reference and unresolved enforcement | live reviewer independence |
| Cultural Review protocol | CONFIRMED draft | named-authority, consent/revocation, and review-gate doctrine | real consultation or consent |
| Archaeology review receipts README | CONFIRMED draft | receipt/process-memory separation | emitted receipts or canonical receipt layout |
| API and promotion sibling READMEs | CONFIRMED | consistent test-local routing and no-authority boundaries | review test implementation |
| Makefile | CONFIRMED | current default target behavior and TODOs | future commands |
| `domain-archaeology` workflow | CONFIRMED TODO scaffold | dedicated trigger exists | substantive CI or required-check status |
| checked 404 paths | CONFIRMED bounded checks | named direct/consumer paths absent at pinned ref | permanent or exhaustive absence |

[Back to top](#top)

---

## Rollback

This is a documentation-only revision.

Before merge, rollback means leaving the draft pull request unmerged or adding a transparent revert commit to the feature branch. Do not reset or force-push shared history.

After merge, rollback means a transparent revert commit or revert pull request based on the merged commit, followed by documentation validation.

Rollback is required if this README:

- is mistaken for review, cultural, consent, consultation, evidence, policy, release, or publication authority;
- directs executable tests into a fixture payload directory;
- claims substantive StewardReview or CulturalReview schema coverage without evidence;
- treats planned-file placeholders as approve/deny review records;
- silently collapses ReviewRecord, StewardReview, and CulturalReview vocabularies;
- treats schema success as review sufficiency;
- weakens exact-location, cultural, sovereignty, rights, consent, consultation, participant-identity, or collection-security safeguards;
- hides the ReviewRecord validator stub or TODO-only CI behavior;
- creates or implies a parallel fixture, review, receipt, policy, or release authority.

**No-loss assessment:** v0.2 preserves the v0.1 synthetic-only, no-network, evidence, policy, review, redaction, release, correction, withdrawal, rollback, and AI-boundary intent. It corrects stale parent-path claims, removes misleading executable-test placement, grounds review-family maturity in current repository evidence, surfaces vocabulary/path drift, exposes placeholder and permissive-schema risks, strengthens cultural-authority and consent non-inference rules, and makes implementation gaps inspectable.

[Back to top](#top)
