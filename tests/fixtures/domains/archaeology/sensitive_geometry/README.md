# `tests/fixtures/domains/archaeology/sensitive_geometry/` — Archaeology Sensitive-Geometry Test-Local Fixture and Exposure-Safety Boundary

> Repository-grounded routing, fixture, and safety contract for test-local Archaeology sensitive-geometry examples. This lane may describe small synthetic manifests and expectations owned by specific tests, but it does not store protected geometry, define redaction policy, perform a transform, emit a receipt, approve review or release, publish a map/API artifact, establish archaeology truth, or authorize reconstruction of restricted places.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-domains-archaeology-sensitive-geometry-readme
title: tests/fixtures/domains/archaeology/sensitive_geometry/README.md — Archaeology Sensitive-Geometry Test-Local Fixture and Exposure-Safety Boundary
type: readme; directory-readme; test-local-fixture-lane; archaeology-sensitive-geometry-routing-boundary; exposure-safety-test-boundary
version: v0.2
status: draft; repository-grounded; README-only-direct-lane; archaeology-parent-confirmed; domains-parent-index-absent; reusable-generalization-placeholder-confirmed; SpatialGeometry-schema-concrete-validator-stub; SensitivityTransform-contract-confirmed-schema-permissive; PublicationTransformReceipt-contract-confirmed-schema-permissive; RedactionReceipt-schema-permissive; redaction-profile-catalog-placeholder; sensitivity-subpolicy-path-absent; sensitive-geometry-validator-readme-only; substantive-domain-sensitive-geometry-tests-unestablished; substantive-ci-unestablished; non-authoritative
owners: OWNER_TBD — Archaeology domain steward · Test steward · Fixture steward · GIS steward · Sensitivity reviewer · Geoprivacy steward · Redaction steward · Cultural-review liaison · Rights-holder representative · Contract/schema steward · Evidence steward · Policy steward · Release steward · Correction/rollback steward · Security reviewer · CI steward · Docs steward
created: 2026-07-06
updated: 2026-07-16
supersedes: v0.1
policy_label: public-doc; tests; fixtures; archaeology; sensitive-geometry-fixtures; test-local-only; synthetic-only; no-network-default; deny-by-default; exact-location-denied; reverse-engineering-denied; candidate-not-confirmed; named-profile-required; receipt-required; evidence-required; review-gated; policy-gated; release-subordinate; correction-aware; revocation-aware; rollback-aware; no-publication
current_path: tests/fixtures/domains/archaeology/sensitive_geometry/README.md
truth_posture:
  CONFIRMED:
    - target README v0.1 and prior blob
    - Directory Rules and tests/fixtures responsibility split
    - tests/fixtures parent README
    - tests/fixtures/domains/archaeology parent README and sensitive_geometry child index
    - tests/domains/archaeology and tests/domains/archaeology/fixtures READMEs
    - root fixtures and reusable Archaeology fixture READMEs
    - reusable synthetic_publication_transform_receipt README and generalize_to_township.json placeholder
    - SpatialGeometry semantic contract and concrete PROPOSED schema
    - SpatialGeometry validator is a NotImplementedError stub
    - SensitivityTransform and PublicationTransformReceipt semantic contracts
    - SensitivityTransform and PublicationTransformReceipt paired permissive PROPOSED schemas
    - Redaction Profiles standard
    - policy/redaction/profiles.yaml is a four-line PROPOSED placeholder sourced from Habitat planning material
    - RedactionReceipt schema is a permissive PROPOSED scaffold with no contract_doc
    - Archaeology sensitivity and publication/policy doctrine
    - Archaeology domain-policy README and missing policy/sensitivity/archaeology README at the checked path
    - sensitive-geometry validator routing README and bounded search surfacing no executable in that lane
    - TODO-only Makefile fixture behavior and domain-archaeology workflow behavior
    - checked absence of tests/fixtures/domains/README.md
    - checked absence of direct-lane conftest.py, manifest_expectations.json, and representative test module
    - checked absence of tests/domains/archaeology/fixtures/sensitive_geometry/README.md
  CONFLICTED:
    - v0.1 claim that tests/fixtures/domains/archaeology/README.md was absent
    - v0.1 proposed executable test modules inside a fixture directory versus current parent guidance that executable tests belong in owning test lanes
    - doctrine names detailed Archaeology redaction profiles while policy/redaction/profiles.yaml is only a generic placeholder sourced from Habitat planning material
    - doctrine requires RedactionReceipt closure while the checked RedactionReceipt schema has no fields and no semantic contract reference
    - rich transform semantics versus permissive empty-property SensitivityTransform and PublicationTransformReceipt schemas
    - generalize_to_township.json filename implies a transform receipt while its payload is only a planned-file placeholder
    - Archaeology sensitivity doctrine names policy/sensitivity/archaeology/ while no README was found at that checked path
    - concrete SpatialGeometry shape validation versus unimplemented dedicated validator and unverified sensitive-location semantics
    - rich sensitivity, review, policy, release, revocation, and cache-invalidation doctrine versus incomplete fixtures, validators, tests, and CI
  UNKNOWN:
    - exhaustive direct-lane inventory outside checked paths
    - generated, ignored, branch-local, dynamic, or externally stored sensitive-geometry fixtures
    - exact runtime policy bundle, profile registry, transform implementation, receipt emitter, and cache invalidation behavior
    - real cultural, sovereignty, rights, consent, and review workflows
    - branch-protection significance and complete repository-wide workflow trigger set
    - current sensitive-geometry fixture pass rates and production/release use
  NEEDS_VERIFICATION:
    - lane-retention decision
    - tests/fixtures/domains parent index
    - exact test-local fixture admission threshold
    - accepted sensitive-geometry manifest contract and identifier vocabulary
    - canonical geometry_role, exposure_class, precision, profile, reason-code, and obligation vocabularies
    - non-placeholder reusable redaction/generalization/receipt fixtures
    - active consumer tests and consumer backlinks
    - substantive SpatialGeometry validator implementation
    - substantive SensitivityTransform, PublicationTransformReceipt, and RedactionReceipt schemas and validators
    - canonical redaction profile catalog ownership and profile activation process
    - Archaeology sensitivity policy bundle syntax and runtime enforcement
    - cultural, sovereignty, rights, consent, consultation, and sensitivity review workflow
    - side-channel and reconstruction-risk detection
    - substantive CI ownership and promotion-blocking behavior
    - correction, withdrawal, revocation, cache invalidation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 80eb1bc7c9ae751125787db4f0054f2bfcf2c4e5
  target_prior_blob: f148929f53d0071a8ca3ee635081a0a51d753611
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
    synthetic_publication_transform_receipt_readme: 78f623961ff8a2da596741863a7243aa0073e444
    generalize_to_township_placeholder: 19281375c9eb628e2894635150c3942d0e8f17b0
    spatial_geometry_contract: 1713cf12437df0ad384588565f3b3519d061627a
    spatial_geometry_schema: 97921f5f98cb34a84caaf4df7a594f5af6d57fba
    spatial_geometry_validator: 387e613baaea0767fae83832ef91c7f9a27ea68a
    sensitivity_transform_contract: 5de68a7e2223d14128157792fcb415cc66d1cc5f
    sensitivity_transform_schema: f72aa3c4504afa6c2c7ce669ad06fb5de514862e
    publication_transform_receipt_contract: fee559d492c3d0145edc30a7ab39369ae7716dd8
    publication_transform_receipt_schema: 379621207697fb9ad2bd16254cc96f6f7d230aae
    redaction_profiles_standard: 402abcf3e231db1c2ede5ed09d0d373d574e5053
    redaction_profile_catalog_placeholder: e928e91ccf278fe42ac0cd83f571ba323787573d
    redaction_receipt_schema: 6251119ecc2293cd219e4ddfa5bbde8b9d6f8f24
    archaeology_sensitivity_doc: ca7888f2d43f022faeef5e1a6e16ab00526cf7aa
    archaeology_publication_policy_doc: 835bd3afb1b6a41de8f598d16b794873df0b6f75
    archaeology_domain_policy_readme: 8d03cdb11361739e7ad33214f76a0cfe4836ff9b
    sensitive_geometry_validator_readme: 166d08f780e96396dbcf8690e3b7218d6d74331b
    sibling_api_readme: 054905beab4e847588569d3306f56a71e9a1c48e
    sibling_promotion_readme: e16733aa226e5eb24f09225e64bc920cbb0b32a3
    sibling_review_readme: ae305821f112832d0613e1c5eb190113c89d20f0
    makefile: 4dc8cf633581893d83fba53219c6ea847992e6be
    domain_archaeology_workflow: b6a2869314efe2e34890baa5bbbe41d656629dd3
  direct_lane_files_confirmed:
    - tests/fixtures/domains/archaeology/sensitive_geometry/README.md
  checked_absent_paths:
    - tests/fixtures/domains/README.md
    - tests/fixtures/domains/archaeology/sensitive_geometry/conftest.py
    - tests/fixtures/domains/archaeology/sensitive_geometry/manifest_expectations.json
    - tests/fixtures/domains/archaeology/sensitive_geometry/test_sensitive_geometry_fixture_manifest_shape.py
    - tests/domains/archaeology/fixtures/sensitive_geometry/README.md
    - policy/sensitivity/archaeology/README.md
  bounded_inventory_note: Direct path checks and bounded repository search establish only the checked snapshot; they do not prove permanent absence from history, ignored files, generated workspaces, branch-local changes, dynamic fixtures, external storage, or uninspected paths.
related:
  - ../README.md
  - ../api/README.md
  - ../promotion/README.md
  - ../review/README.md
  - ../../../README.md
  - ../../../../README.md
  - ../../../../domains/archaeology/README.md
  - ../../../../domains/archaeology/fixtures/README.md
  - ../../../../../fixtures/README.md
  - ../../../../../fixtures/domains/archaeology/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_archaeological_site/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_candidate_feature/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_publication_transform_receipt/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_publication_transform_receipt/generalize_to_township.json
  - ../../../../../contracts/common/spatial_geometry.md
  - ../../../../../schemas/contracts/v1/common/spatial_geometry.schema.json
  - ../../../../../tools/validators/validate_spatial_geometry.py
  - ../../../../../contracts/domains/archaeology/sensitivity_transform.md
  - ../../../../../contracts/domains/archaeology/publication_transform_receipt.md
  - ../../../../../schemas/contracts/v1/domains/archaeology/sensitivity_transform.schema.json
  - ../../../../../schemas/contracts/v1/domains/archaeology/publication_transform_receipt.schema.json
  - ../../../../../schemas/contracts/v1/receipts/redaction_receipt.schema.json
  - ../../../../../docs/standards/REDACTION_PROFILES.md
  - ../../../../../policy/redaction/profiles.yaml
  - ../../../../../policy/domains/archaeology/README.md
  - ../../../../../tools/validators/sensitive_geometry/README.md
  - ../../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../../docs/domains/archaeology/MAP_UI_CONTRACTS.md
  - ../../../../../docs/doctrine/directory-rules.md
  - ../../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../../../docs/registers/DRIFT_REGISTER.md
  - ../../../../../.github/workflows/domain-archaeology.yml
  - ../../../../../Makefile
notes:
  - "v0.2 corrects the stale claim that tests/fixtures/domains/archaeology/README.md is absent; that parent exists and indexes this sensitive_geometry lane."
  - "The direct sensitive-geometry fixture lane is README-only in bounded repository evidence."
  - "Executable tests do not belong in this fixture directory by default; they belong in an owning tests/ lane and consume declarative fixtures by reference."
  - "SpatialGeometry has a concrete PROPOSED schema, but its dedicated validator raises NotImplementedError and shape validity does not prove safe exposure."
  - "SensitivityTransform and PublicationTransformReceipt have rich semantic contracts but only permissive empty-property PROPOSED schemas."
  - "The checked RedactionReceipt schema is also permissive, has no contract_doc, and cites Fauna source docs rather than Archaeology."
  - "policy/redaction/profiles.yaml is a planned-file placeholder sourced from Habitat planning material; it is not an active Archaeology profile catalog."
  - "generalize_to_township.json is a planned-file placeholder; its filename does not prove a transform, receipt, safe geometry, or release."
  - "The Archaeology sensitivity-specific policy README was not found at policy/sensitivity/archaeology/README.md."
  - "The sensitive-geometry validator lane surfaced only a README in bounded search; executable enforcement is unestablished."
  - "The domain-archaeology workflow and relevant Makefile targets are TODO-only; this revision creates no executable enforcement."
  - "This revision changes documentation only and creates no fixture payload, test, schema, contract, policy, profile, validator, workflow, data object, receipt, proof, release record, map artifact, tile, API output, AI output, consent record, consultation record, or public artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<p>
  <img alt="Document status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Direct inventory: README only" src="https://img.shields.io/badge/direct__inventory-README__only-lightgrey">
  <img alt="Scope: test local" src="https://img.shields.io/badge/scope-test__local-blue">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-8a6d3b">
  <img alt="Sensitivity: deny by default" src="https://img.shields.io/badge/sensitivity-deny__by__default-critical">
  <img alt="Exposure: reverse engineering denied" src="https://img.shields.io/badge/exposure-reconstruction__denied-red">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture__only-purple">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose) · [Authority](#authority-and-directory-rules-basis) · [Current state](#confirmed-current-state) · [Threat model](#sensitive-geometry-threat-model) · [Object model](#geometry-transform-receipt-and-release-anti-collapse) · [Fixture home](#fixture-home-decision-law) · [Admission](#test-local-sensitive-geometry-fixture-admission-contract) · [Manifest](#minimum-sensitive-geometry-fixture-manifest-contract) · [Consumers](#consumer-backlinks-and-orphan-control) · [Families](#sensitive-geometry-fixture-family-routing) · [SpatialGeometry](#spatialgeometry-contract-schema-and-validator-posture) · [SensitivityTransform](#sensitivitytransform-semantic-contract-and-schema-posture) · [Transform receipt](#publicationtransformreceipt-semantic-contract-and-schema-posture) · [Redaction](#redaction-profile-and-redactionreceipt-maturity) · [Outcomes](#finite-outcomes-and-vocabulary-separation) · [Exact geometry](#exact-geometry-denial-and-default-posture) · [Generalization](#generalization-precision-and-profile-posture) · [Reconstruction](#side-channel-and-reconstruction-risk) · [Candidate posture](#candidate-confirmed-and-source-role-anti-collapse) · [Closure](#evidence-review-policy-receipt-and-release-closure) · [Rights](#cultural-sovereignty-rights-consent-and-consultation) · [Public surfaces](#map-tile-api-export-screenshot-and-ai-boundaries) · [Network](#no-network-security-and-side-effects) · [Determinism](#identity-version-hash-generation-and-replay) · [Polarity](#valid-invalid-denied-restricted-held-abstained-quarantined-and-error-cases) · [Correction](#correction-withdrawal-revocation-cache-invalidation-and-rollback) · [Coverage](#inventory-orphans-nonempty-coverage-and-vacuous-pass-risk) · [Commands](#deterministic-validation-commands) · [CI](#runner-ci-and-promotion-boundary) · [Failure meaning](#failure-interpretation) · [Passing limits](#what-a-passing-suite-does-not-prove) · [Layout](#proposed-layout-and-routing) · [Maintenance](#maintenance-and-fixture-update-rules) · [Migration](#migration-deprecation-and-lane-retention) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [Rollback](#rollback)

---

## Status and evidence boundary

> [!IMPORTANT]
> **Evidence snapshot:** `main@80eb1bc7c9ae751125787db4f0054f2bfcf2c4e5`
> **Prior target blob:** `f148929f53d0071a8ca3ee635081a0a51d753611`
> **Direct lane:** `tests/fixtures/domains/archaeology/sensitive_geometry/README.md` only at the bounded snapshot
> **Parent state:** `tests/fixtures/README.md` and `tests/fixtures/domains/archaeology/README.md` exist; `tests/fixtures/domains/README.md` was not found
> **Reusable fixture root:** `fixtures/domains/archaeology/`
> **Executable consumer lane:** `tests/domains/archaeology/fixtures/` exists; a `sensitive_geometry/` child is not established in checked evidence
> **Current collection:** no verified default runner or substantive CI job collects this direct fixture lane

This directory is currently a routing README. It is not a fixture corpus, geometry validator, geoprivacy engine, redaction catalog, transform implementation, receipt emitter, policy bundle, evidence store, review registry, release queue, map source, tile source, API surface, AI source, or public artifact home.

### Safe conclusions

- **CONFIRMED:** the target README exists.
- **CONFIRMED:** the Archaeology test-fixture parent exists and indexes this child.
- **CONFIRMED:** the higher `tests/fixtures/domains/README.md` index remains absent at the checked path.
- **CONFIRMED:** the direct lane has no checked `conftest.py`, manifest, or representative test module.
- **CONFIRMED:** executable tests belong in an owning `tests/` lane rather than in a fixture payload directory by default.
- **CONFIRMED:** root `fixtures/` is the reusable fixture responsibility root.
- **CONFIRMED:** the checked reusable generalization example is a placeholder rather than a receipt-shaped payload.
- **CONFIRMED:** common `SpatialGeometry` has a concrete PROPOSED schema, while its dedicated validator is unimplemented.
- **CONFIRMED:** Archaeology transform and transform-receipt semantic contracts exist, while their schemas are permissive scaffolds.
- **CONFIRMED:** the checked RedactionReceipt schema is also permissive and lacks a semantic-contract reference.
- **CONFIRMED:** the checked redaction profile catalog file is a placeholder, not an active reviewed catalog.
- **CONFIRMED:** the checked Archaeology sensitivity-specific policy README is absent.
- **CONFIRMED:** bounded search surfaced only the sensitive-geometry validator README in its direct lane.
- **NEEDS VERIFICATION:** any claim of substantive fixture coverage, reconstruction-risk detection, policy enforcement, receipt closure, release gating, or CI enforcement.

### Truth labels used here

| Label | Meaning in this README |
|---|---|
| `CONFIRMED` | Verified from repository content or a bounded path/search check at the pinned snapshot. |
| `PROPOSED` | A design, contract, fixture shape, command, path relationship, or test expectation not established as current implementation. |
| `UNKNOWN` | Not resolved by inspected evidence. |
| `NEEDS VERIFICATION` | Checkable, but not sufficiently verified to act as fact. |
| `CONFLICTED` | Repository artifacts disagree, overstate maturity, or carry stale/cross-domain lineage; no silent winner is selected. |
| `DENY` | A prohibited exposure or authority interpretation. |

[Back to top](#top)

---

## Purpose

`tests/fixtures/domains/archaeology/sensitive_geometry/` is a test-local fixture routing and safety boundary for synthetic examples that exercise sensitive-location denial, public-safe geometry posture, transform/receipt linkage, and downstream exposure controls.

The durable question is:

> Can an owning test prove that an Archaeology geometry carrier is synthetic, non-reconstructive, correctly classified, evidence-aware, policy-aware, review-aware, receipt-backed where required, release-subordinate, correctable, revocable, and reversible—without placing protected coordinates or authority records in the fixture lane?

This README is for:

- fixture and test stewards deciding whether a test-local wrapper belongs here;
- Archaeology, GIS, geoprivacy, redaction, sensitivity, rights, and release stewards;
- schema, contract, policy, receipt, validator, map, API, tile, export, screenshot, and AI-surface reviewers;
- maintainers investigating whether a geometry-related test is substantive or vacuously green;
- reviewers checking that a generalized label, profile name, receipt reference, or passing shape check is not being misread as release permission.

This README does not prove the lane is implemented. It defines safe routing, anti-collapse rules, minimum future fixture expectations, failure meaning, and verification work.

[Back to top](#top)

---

## Authority and Directory Rules basis

Directory Rules separate responsibility roots:

- `tests/` proves enforceability;
- `fixtures/` stores reusable synthetic inputs;
- `contracts/` defines semantic meaning;
- `schemas/` defines machine shape;
- `policy/` defines admissibility and obligations;
- `tools/validators/` evaluates bounded conditions;
- `data/receipts/` and `data/proofs/` retain process memory and evidence support;
- `release/` governs promotion, correction, withdrawal, supersession, and rollback;
- governed APIs and released public artifacts serve normal clients.

This path remains under `tests/fixtures/` because it is a test-local fixture expectation lane. That does not make it the correct home for executable tests or reusable geometry payloads.

| Responsibility | Owning home | Relationship to this README |
|---|---|---|
| Test-local sensitive-geometry manifests and expectation maps | `tests/fixtures/domains/archaeology/sensitive_geometry/` | May live here when a verified consumer requires them. |
| Executable Archaeology sensitive-geometry tests | `tests/domains/archaeology/fixtures/sensitive_geometry/` or another accepted owning test lane | PROPOSED future consumer lane; absent at the checked path. |
| Reusable Archaeology fixtures | `fixtures/domains/archaeology/` | Referenced, not duplicated here. |
| Common geometry meaning and shape | `contracts/common/spatial_geometry.md`, `schemas/contracts/v1/common/spatial_geometry.schema.json` | Referenced; not redefined here. |
| Archaeology transform meaning | `contracts/domains/archaeology/sensitivity_transform.md` | Referenced; not redefined here. |
| Transform-receipt meaning | `contracts/domains/archaeology/publication_transform_receipt.md` | Referenced; not redefined here. |
| Redaction profile doctrine and catalog | `docs/standards/REDACTION_PROFILES.md`, `policy/redaction/` | Doctrine/catalog responsibility; catalog maturity is not established here. |
| Archaeology admissibility policy | `policy/domains/archaeology/` and accepted subpolicy lanes | Referenced; not authored here. |
| Sensitive-geometry validation | `tools/validators/sensitive_geometry/` and owning validator lanes | Referenced; direct executable maturity is unestablished. |
| Evidence, receipts, proof, and review records | Governed trust roots | Referenced through synthetic IDs only. |
| Promotion, release, correction, withdrawal, and rollback | `release/` | Never decided here. |
| Public maps, tiles, APIs, exports, screenshots, and AI answers | Governed released public surfaces | Never produced or served here. |

No root, schema-home, policy-home, receipt-home, release-home, or lifecycle decision changes in this documentation-only revision. No ADR or drift-register mutation is required to correct this README; the README records observed drift rather than adjudicating it.

[Back to top](#top)

---

## Confirmed current state

| Surface | Evidence status | Safe interpretation |
|---|---|---|
| Direct sensitive-geometry lane | README only in bounded checks | Routing documentation, not executable coverage. |
| Archaeology test-fixture parent | Exists and indexes this child | v0.1 parent-missing claim is stale. |
| `tests/fixtures/domains/README.md` | Not found at checked path | Parent-index gap remains. |
| Owning domain fixture-test parent | Exists | Potential executable owner, not fixture authority. |
| Owning `sensitive_geometry/` test child | Not found at checked path | Dedicated consumer suite is unestablished. |
| Reusable Archaeology fixture root | Exists | Reusable inputs belong there. |
| `generalize_to_township.json` | Four-field PROPOSED placeholder | Filename is not transform/receipt/safety evidence. |
| `SpatialGeometry` schema | Concrete required fields and precision enum; status PROPOSED | Shape support exists; exposure safety does not follow. |
| `validate_spatial_geometry.py` | Raises `NotImplementedError` | Dedicated validator cannot serve as a green gate. |
| `SensitivityTransform` contract | Rich semantic contract | Machine enforcement remains unestablished. |
| `SensitivityTransform` schema | Empty properties; `additionalProperties: true` | Schema acceptance is nearly non-substantive. |
| `PublicationTransformReceipt` contract | Rich semantic contract | Receipt meaning exists; emitted receipt behavior remains unverified. |
| `PublicationTransformReceipt` schema | Empty properties; `additionalProperties: true` | Schema acceptance does not prove transform lineage. |
| Redaction Profiles standard | Draft doctrine | Profile semantics are documented. |
| `policy/redaction/profiles.yaml` | PROPOSED placeholder sourced from Habitat planning doc | Not an active Archaeology profile catalog. |
| RedactionReceipt schema | Empty properties; `additionalProperties: true`; no contract doc | Does not close receipt semantics. |
| Archaeology domain policy README | Draft documentation | Concrete bundles, tests, CI, and runtime behavior remain unverified. |
| `policy/sensitivity/archaeology/README.md` | Not found at checked path | Named subpolicy path is unestablished. |
| Sensitive-geometry validator lane | README only in bounded search | No executable validator established. |
| `domain-archaeology` workflow | TODO-only behavior in checked evidence | Trigger success is not substantive geometry safety proof. |
| `make fixtures` | TODO-oriented behavior in checked evidence | Command success is not fixture validation. |

### Maturity conclusion

The repository contains strong human-readable doctrine and several semantic contracts. It also contains a concrete common geometry schema. It does **not** yet establish a complete, machine-enforced Archaeology sensitive-geometry path from safe fixture input through profile resolution, transform execution, receipt validation, policy decision, review, release, public carrier, revocation, and rollback.

The direct lane must therefore remain explicitly `PROPOSED / NEEDS VERIFICATION` as an implementation surface.

[Back to top](#top)

---

## Sensitive-geometry threat model

Sensitive geometry is broader than a coordinate pair.

A fixture or consumer may expose a restricted place through:

- exact coordinates or raw geometry;
- high-resolution centroids, bounding boxes, extents, or tile bounds;
- feature IDs, filenames, cache keys, hashes, stable ordering, or join keys;
- labels, hover text, popup fields, error messages, debug logs, screenshots, thumbnails, or map-fit behavior;
- counts, density surfaces, sparse aggregates, or repeated generalized outputs;
- graph edges, nearest-neighbor results, routing, distance responses, reverse joins, search results, exports, vector indexes, embeddings, or AI prose;
- source metadata, collection-security records, private-landowner information, consent metadata, or cultural-context clues;
- candidate/anomaly labels that imply a confirmed site;
- correction, withdrawal, or stale cache behavior that leaves an unsafe derivative active.

### Threat classes

| Threat class | Example test question | Required posture |
|---|---|---|
| Direct exposure | Does any public-bound fixture carry exact/internal geometry? | `DENY`. |
| Precision mismatch | Is `survey` or `parcel` precision carried into a public-safe context? | `DENY` or governed restriction. |
| Reconstruction | Can several generalized outputs be combined to narrow the location? | `DENY` / `HOLD`. |
| Side-channel leakage | Do labels, bounds, cache keys, errors, or screenshots expose location? | `DENY`. |
| Role collapse | Does a candidate/anomaly appear as a confirmed archaeological site? | `DENY` / `ABSTAIN`. |
| Receipt collapse | Is a receipt filename/reference treated as proof that a transform ran? | Validation failure. |
| Policy collapse | Is a profile name or coarse geometry treated as policy approval? | `DENY`. |
| Release collapse | Is a passing fixture, schema, validator, or map render treated as publication approval? | Promotion block. |
| Revocation failure | Does an unsafe or revoked derivative remain active? | `ERROR` / rollback required. |

The test posture is not “hide exact geometry in the UI.” The posture is “public clients never receive exact/internal geometry through the normal path.”

[Back to top](#top)

---

## Geometry, transform, receipt, and release anti-collapse

Sensitive geometry crosses several object families. They must not be collapsed.

| Object or artifact | What it means | What it does **not** mean |
|---|---|---|
| `SpatialGeometry` | Geometry carrier with explicit CRS and precision bucket. | Safe exposure, source accuracy, evidence closure, or release. |
| Archaeology domain object | The site/candidate/observation/context meaning owned by Archaeology. | Public geometry permission. |
| `SensitivityTransform` | Semantic description of a redaction/generalization/suppression class. | Transform execution, policy approval, or release. |
| Redaction profile | Named, versioned transform policy artifact. | Proof the profile exists, is active, or was applied. |
| Transform executable | Code that applies a transform. | Evidence, policy, review, receipt, or release. |
| `PublicationTransformReceipt` / `RedactionReceipt` | Process-memory record describing a specific transform result. | Underlying archaeological truth, review approval, or release. |
| `PolicyDecision` | Admissibility outcome and obligations. | Evidence proof or release manifest. |
| `ReviewRecord` / steward/cultural review | Governed review posture. | Consent by inference, cultural authority, or publication. |
| `EvidenceBundle` | Evidence support for claims. | Policy approval or release. |
| `PromotionDecision` | Governed decision to advance state. | Public release by itself. |
| `ReleaseManifest` / map release artifact | Released scope and lineage. | Source truth beyond evidence support. |
| Map/tile/API/AI carrier | Downstream public representation. | Canonical truth, evidence root, or internal geometry authority. |

### Required separation

A mature fixture family should make each boundary independently testable:

1. shape can pass while policy denies;
2. transform semantics can be known while executable implementation is absent;
3. executable transform can run while receipt validation fails;
4. receipt shape can pass while evidence/review/policy/release closure fails;
5. coarse geometry can still be sensitive;
6. released geometry can later be withdrawn, corrected, superseded, or revoked;
7. candidate status remains candidate status through every transform.

[Back to top](#top)

---

## Fixture-home decision law

Before adding a file, answer these questions in order.

### 1. Is it real or protected material?

Do not place it in any fixture lane. Use governed restricted lifecycle storage and approved test substitution mechanisms.

### 2. Is it a reusable synthetic domain payload?

Use an accepted child under `fixtures/domains/archaeology/`.

### 3. Is it a cross-domain schema fixture for `SpatialGeometry` or a receipt family?

Use the schema-declared or accepted contract fixture root, not this domain test-local lane.

### 4. Is it an executable test?

Use an owning `tests/` lane. Do not place `test_*.py` modules beside fixture payloads by default.

### 5. Is it a tiny test-local manifest or expected-result map required by one owning test?

This lane may be appropriate when all of the following are true:

- the consumer test is identified;
- the file is synthetic and public-safe;
- the file contains no protected coordinate or reverse-engineering hint;
- the file is not reusable across multiple consumers;
- the manifest schema/version is explicit;
- expected outcomes and reason codes are finite;
- consumer and fixture backlink to each other;
- removal behavior is defined.

### 6. Would the file create a parallel contract, schema, policy, profile, receipt, evidence, review, or release home?

Do not add it here. Route it to the owning root and use an ADR or migration note if placement is disputed.

[Back to top](#top)

---

## Test-local sensitive-geometry fixture admission contract

A future payload in this lane should be admitted only when all required conditions are met.

| Admission condition | Required evidence |
|---|---|
| Consumer ownership | Exact test module or test case ID. |
| Test-local necessity | Explanation why a reusable root is unsuitable. |
| Synthetic provenance | `mock_marker: true` and synthetic generator/author reference. |
| No protected geometry | Automated and human review confirming no exact/reconstructive detail. |
| Explicit object family | `SpatialGeometry`, candidate envelope, transform manifest, receipt ref envelope, map carrier, or another reviewed class. |
| Explicit geometry role | Internal, restricted, candidate, generalized, aggregate, public-safe, denied, or no-geometry posture from an accepted vocabulary. |
| Explicit precision/exposure posture | Closed, versioned value; unknown values fail closed. |
| Named profile posture | Profile ref present when required; placeholder refs marked synthetic. |
| Receipt posture | Expected receipt family and resolution behavior declared. |
| Evidence/review/policy/release posture | Required refs and expected missing-ref behavior declared. |
| Finite outcome | Expected test/policy/runtime outcome and reason code declared. |
| Determinism | Stable IDs, ordering, seed/clock assumptions, and replay hash. |
| Lifecycle | Add/update/deprecate/remove behavior documented. |
| Backlinks | Fixture points to consumer; consumer points to fixture. |

A fixture that lacks a consumer, polarity, or removal path is an orphan risk. A fixture whose safety depends on humans recognizing a filename is not governed enough.

[Back to top](#top)

---

## Minimum sensitive-geometry fixture manifest contract

The following is **illustrative**, not an accepted schema.

```json
{
  "fixture_manifest_id": "fixture:archaeology:sensitive-geometry:example:001",
  "manifest_version": "PROPOSED-v1",
  "domain": "archaeology",
  "fixture_scope": "test_local",
  "consumer_test_ref": "tests/domains/archaeology/fixtures/sensitive_geometry/test_public_safe_geometry.py::test_missing_receipt_abstains",
  "canonical_fixture_refs": [
    "fixtures/domains/archaeology/synthetic_candidate_feature/example.json"
  ],
  "object_family": "SpatialGeometry",
  "source_role": "candidate",
  "geometry_role": "generalized_placeholder",
  "precision_bucket": "region",
  "raw_geometry_present": false,
  "public_geometry_present": true,
  "reverse_engineering_canary_present": false,
  "mock_marker": true,
  "redaction_profile_ref": "profile:synthetic:archaeology:region-generalization@v1",
  "sensitivity_transform_ref": "transform:synthetic:archaeology:region-generalization@v1",
  "publication_transform_receipt_ref": null,
  "redaction_receipt_ref": null,
  "evidence_ref": "evidence-ref:synthetic:archaeology:001",
  "review_record_ref": "review-record:synthetic:archaeology:001",
  "policy_decision_ref": "policy-decision:synthetic:archaeology:001",
  "release_manifest_ref": null,
  "rollback_card_ref": "rollback-card:synthetic:archaeology:001",
  "expected_test_outcome": "PASS",
  "expected_policy_outcome": "ABSTAIN",
  "expected_runtime_outcome": "ABSTAIN",
  "expected_reason_codes": [
    "SENSITIVE_GEOMETRY_RECEIPT_UNRESOLVED",
    "SENSITIVE_GEOMETRY_NOT_RELEASED"
  ],
  "must_not_claim": [
    "EXACT_COORDINATE_CANARY",
    "PROTECTED_LOCATION_CANARY",
    "REVERSE_GEOCODE_HINT_CANARY",
    "CONFIRMED_SITE_CANARY",
    "TRANSFORM_EXECUTED_CANARY",
    "RECEIPT_VALID_CANARY",
    "POLICY_APPROVAL_CANARY",
    "REVIEW_APPROVAL_CANARY",
    "MAP_TRUTH_CANARY",
    "AI_TRUTH_CANARY",
    "RELEASE_APPROVAL_CANARY"
  ]
}
```

### Manifest rules

- `consumer_test_ref` must resolve before the fixture is admitted.
- `canonical_fixture_refs` must resolve or be explicitly marked as intentionally absent negative cases.
- `raw_geometry_present: true` is prohibited for public-readable fixture files unless the value is a non-geographic canary that cannot encode a real place.
- `public_geometry_present: true` does not imply release.
- `precision_bucket` does not imply accuracy or safety.
- profile, transform, receipt, evidence, review, policy, release, and rollback refs are separate.
- expected test, policy, and runtime outcomes are separate fields.
- unknown vocabulary values fail closed.
- the manifest must not include real profile parameters, protected thresholds, or reconstruction recipes.

[Back to top](#top)

---

## Consumer backlinks and orphan control

Every test-local fixture should have a verified consumer.

### Required bidirectional linkage

Fixture to consumer:

```text
consumer_test_ref: tests/.../test_file.py::test_case
```

Consumer to fixture:

```python
FIXTURE = ROOT / "tests/fixtures/domains/archaeology/sensitive_geometry/<file>.json"
```

The code snippet is illustrative. It does not claim the test exists.

### Orphan checks

A future inventory validator should fail when:

- a fixture has no consumer;
- a consumer points to a missing fixture;
- a consumer path has moved without updating the manifest;
- a fixture references a nonexistent schema, contract, profile, receipt, policy, or release object;
- a negative fixture lacks an expected failure class;
- a profile/transform fixture has no version pin;
- a safe-output fixture has no policy/review/release expectation;
- a fixture is not listed in its local inventory;
- a fixture survives after its final consumer is removed.

### Removal rule

When the last consumer is removed, remove or deliberately migrate the fixture in the same change. Do not retain “maybe useful” sensitive-geometry examples without ownership.

[Back to top](#top)

---

## Sensitive-geometry fixture family routing

| Fixture family | Preferred home | Expected consumer | Boundary |
|---|---|---|---|
| Reusable synthetic site/candidate payload | `fixtures/domains/archaeology/` | Domain tests and docs | Not site truth. |
| Generic `SpatialGeometry` valid/invalid shape | Schema-declared common fixture root | Common schema harness | Shape only; not safe exposure. |
| Archaeology `SensitivityTransform` example | Accepted reusable Archaeology fixture child | Domain transform tests | Not executable transform or policy. |
| Archaeology transform-receipt example | `fixtures/domains/archaeology/synthetic_publication_transform_receipt/` after substantive payload review | Receipt/lineage tests | Not release approval. |
| RedactionReceipt schema fixture | Accepted receipt fixture root | Receipt schema tests | Not transform proof. |
| Profile catalog fixture | Accepted policy/redaction fixture root | Profile verifier/policy tests | Must not expose protected parameters. |
| One-consumer expectation manifest | This lane, conditionally | Owning Archaeology test | Test-local only. |
| Executable sensitive-geometry assertion | Owning `tests/` lane | Pytest or accepted runner | Not a fixture payload. |
| Real restricted geometry | Governed restricted lifecycle store | Controlled integration environment | Never committed here. |
| Public-safe released geometry | Governed release/public artifact roots | Governed API/UI | Never authored here. |

### Existing placeholder warning

`fixtures/domains/archaeology/synthetic_publication_transform_receipt/generalize_to_township.json` currently records only:

- `status: PROPOSED`;
- a source planning document;
- its own path;
- a placeholder note.

It does not contain source refs, transform type, profile version, input/output hashes, evidence refs, review refs, policy refs, receipt identity, release refs, or rollback lineage. It must not be consumed as a successful transform receipt.

[Back to top](#top)

---

## SpatialGeometry contract, schema, and validator posture

The common `SpatialGeometry` family is the most concrete machine-shape evidence inspected for this lane.

### Confirmed schema shape

Required top-level fields:

- `geometry`;
- `crs`;
- `precision_bucket`.

The current precision enum is:

```text
survey | parcel | community | region | coarse
```

### What shape validation can prove

- the required fields are present;
- nested geometry has `type` and `coordinates`;
- `crs` is a string;
- `precision_bucket` uses the current enum;
- additional top-level fields are rejected.

### What shape validation cannot prove

- coordinates are valid, accurate, synthetic, or non-sensitive;
- the geometry type and coordinate nesting are semantically valid;
- CRS values are recognized or correctly applied;
- a precision bucket matches actual coordinate precision;
- the geometry is not reverse-engineerable;
- source rights, evidence, consent, cultural authority, policy, review, receipt, release, correction, or rollback obligations are satisfied;
- a `region` or `coarse` carrier is safe;
- a public client may receive the geometry.

### Validator posture

`tools/validators/validate_spatial_geometry.py` raises `NotImplementedError("Greenfield placeholder")`. A fixture suite must not treat the validator path as implemented merely because schema metadata names it.

### Required future semantic checks

- recognized geometry types and coordinate structure;
- explicit/approved CRS handling;
- precision-bucket truthfulness;
- geometry-role separation;
- sensitive-location policy inheritance;
- transform/receipt linkage;
- source-role preservation;
- reconstruction-risk checks;
- public-surface release closure.

[Back to top](#top)

---

## SensitivityTransform semantic contract and schema posture

The `SensitivityTransform` contract defines the meaning of governed redaction, suppression, generalization, aggregation, masking, delayed visibility, summary-only representation, public-safe derivation, denial, and abstention.

### Confirmed semantic boundaries

A `SensitivityTransform` is not:

- transform executable code;
- a transform receipt;
- a PolicyDecision;
- a ReviewRecord;
- an EvidenceBundle;
- a ReleaseManifest;
- public geometry;
- proof that release is approved.

### Current machine-shape posture

The paired schema:

- is status `PROPOSED`;
- has an empty `properties` object;
- permits additional properties;
- does not require transform identity, type, source/output class, profile, policy, review, evidence, receipt, release, or rollback fields.

A fixture that “validates” against this schema may still have no meaningful transform semantics.

### Required future polarity

Positive cases should prove reviewed semantic completeness. Negative cases should include:

- missing transform identity/version;
- unknown transform type;
- missing source/output visibility classes;
- missing named profile where required;
- missing receipt requirement;
- unsafe output precision;
- absent residual-risk statement;
- missing policy/review/evidence/release refs;
- denial condition incorrectly converted into a public output;
- candidate/source-role mutation.

[Back to top](#top)

---

## PublicationTransformReceipt semantic contract and schema posture

The `PublicationTransformReceipt` contract describes process memory for a specific transformation from internal/controlled material to a public-safe, semi-public, or release-candidate representation.

### Confirmed receipt boundaries

The receipt is not:

- transform code;
- a PolicyDecision;
- a ReviewRecord;
- an EvidenceBundle;
- a ReleaseManifest;
- public output;
- proof that the source claim is true;
- proof that release occurred.

### Current receipt schema posture

The paired schema:

- is status `PROPOSED`;
- has no defined properties;
- permits arbitrary properties;
- does not enforce source refs, transform type, profile, input/output hashes, evidence, review, validation, policy, release, correction, withdrawal, supersession, or rollback lineage.

### Source-ledger drift

The semantic contract records a source-ledger mismatch between prior Markdown scaffold lineage and schema lineage. This fixture lane must not adjudicate that conflict. It should expose it until the owning contract/schema work resolves it.

### Required future receipt tests

- stable receipt identity and schema version;
- source object and lifecycle state;
- transform/profile version;
- input and output hashes;
- output visibility/precision class;
- evidence, validation, review, and policy refs;
- release-candidate/release refs when relevant;
- residual-risk statement;
- correction/supersession/withdrawal/rollback lineage;
- deterministic replay or explicit non-replayable justification;
- denial when the output cannot be made safe.

[Back to top](#top)

---

## Redaction profile and RedactionReceipt maturity

### Redaction Profiles standard

The standard requires profiles to be:

- named rather than inline;
- versioned;
- deterministic;
- seeded when stochastic behavior exists;
- receipt-bearing;
- fail-closed when missing, unresolved, or revoked;
- fixture-backed and verifier-checked before publication use.

### Current catalog posture

`policy/redaction/profiles.yaml` is only a placeholder with:

- `status: PROPOSED`;
- a `source_doc` pointing to Habitat planning material;
- its path;
- a placeholder note.

It is not a machine-verified catalog of active Archaeology profiles. It does not establish the profile IDs described in Archaeology sensitivity doctrine.

### Current RedactionReceipt schema posture

The checked schema:

- is status `PROPOSED`;
- has no properties;
- permits arbitrary properties;
- has `contract_doc: null`;
- cites Fauna source documents rather than Archaeology.

This is cross-domain provenance and maturity drift, not proof that Archaeology RedactionReceipts are implemented.

### Fixture requirements

A mature sensitive-geometry suite should prove:

- unknown profile → deny;
- unversioned profile → deny;
- deprecated/revoked profile → deny or governed migration;
- inline parameters without accepted profile → deny;
- profile/receipt mismatch → deny;
- input/output hash mismatch → error;
- non-deterministic replay → error;
- missing evidence/review/policy/release support → abstain/hold/deny;
- receipt shape success without semantic closure → blocked;
- profile version change does not silently rewrite prior outputs.

[Back to top](#top)

---

## Finite outcomes and vocabulary separation

Different layers use different vocabularies. Do not collapse them.

| Layer | Example vocabulary | Fixture rule |
|---|---|---|
| Test assertion | `PASS`, `FAIL`, `SKIP`, `ERROR` | Describes test execution only. |
| Policy | `ALLOW`, `RESTRICT`, `HOLD`, `DENY`, `ABSTAIN`, `ERROR` | Describes admissibility/obligations. |
| Runtime response | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Describes client-facing behavior. |
| Geometry role | internal, restricted, candidate, generalized, aggregate, public-safe, denied | Must use accepted/versioned vocabulary. |
| Precision bucket | `survey`, `parcel`, `community`, `region`, `coarse` | Shape declaration; not exposure permission. |
| Transform state | requested, planned, applied, verified, failed, superseded, revoked | PROPOSED until contract/schema accepted. |
| Receipt state | emitted, verified, invalid, superseded, withdrawn | PROPOSED until contract/schema accepted. |
| Promotion | `APPROVE`, `DENY`, `ABSTAIN` in checked PromotionDecision schema | Does not equal release. |
| Lifecycle | RAW, WORK/QUARANTINE, PROCESSED, CATALOG/TRIPLET, PUBLISHED | State transition, not test outcome. |

### Example

A negative fixture may produce:

```text
Test assertion: PASS
Policy outcome: DENY
Runtime outcome: DENY
Reason: exact/internal geometry reached a public-bound carrier
```

That is a successful test of denied behavior, not a failed fixture and not a release.

[Back to top](#top)

---

## Exact geometry denial and default posture

Archaeology exact site geometry, burials, sacred sites, human remains, collection-security locations, looting-risk exposure, and unresolved cultural sensitivity fail closed.

### Required fixture assertions

- exact/internal geometry never appears in a public-bound fixture;
- real coordinates are never used as test data;
- coordinate-looking canaries cannot correspond to a real place;
- a public carrier cannot read an internal geometry field and hide it with styling;
- source geometry cannot be returned in API errors or debug payloads;
- raw geometry cannot be embedded in map tiles, screenshots, exports, vector indexes, or AI prompts;
- missing sensitivity rank defaults to the most restrictive posture;
- exact geometry plus active-threat detail is treated as a compounded risk;
- burial/sacred/human-remains examples remain denial cases, not “coarse release” cases;
- no fixture demonstrates how to reverse an approved transform.

### No style-only hiding

These patterns are forbidden as a safety mechanism:

- opacity zero;
- hidden layer toggles;
- zoom thresholds;
- client-side clipping;
- CSS masking;
- removing popup fields while retaining coordinates;
- shipping exact geometry to the browser but not drawing it;
- storing exact geometry in tile attributes;
- depending on UI access controls without upstream public-safe derivation.

The public artifact must be safe before it reaches the client.

[Back to top](#top)

---

## Generalization, precision, and profile posture

Generalization is not a universal permission to publish.

### Doctrine versus implementation

Archaeology sensitivity doctrine describes audience tiers, sensitivity ranks, named profiles, and an H3 resolution floor. Those are human-facing doctrine claims. The checked profile catalog and receipt schemas do not yet establish machine enforcement.

### Required fixture rules

- use symbolic profile IDs and synthetic geometry rather than real operational parameters where disclosure could aid reconstruction;
- require a named and versioned profile reference;
- keep profile activation state separate from profile existence;
- keep precision bucket separate from sensitivity rank and audience tier;
- do not assume `region` or `coarse` is safe;
- require minimum-count or aggregation protections when sparse counts can reveal a location;
- preserve source role and candidate status;
- require residual-risk and reconstruction-risk checks;
- require a receipt for material transforms;
- require policy, review, evidence, and release closure before public use;
- fail closed when profile, receipt, or policy registry cannot resolve.

### Parameter exposure rule

This README and public-readable fixtures should not publish hidden operational thresholds, seeds, exact jitter values, reconstruction cutoffs, private grid parameters, or other data that would materially improve an attacker’s ability to reverse a transform. Test expected values may use symbolic or synthetic non-operational parameters in controlled locations after policy review.

[Back to top](#top)

---

## Side-channel and reconstruction risk

A geometry can be reconstructed without an explicit coordinate field.

### Required future test families

| Risk | Negative fixture concept | Expected behavior |
|---|---|---|
| Bounds leakage | Public payload includes tight source bounds. | `DENY`. |
| Sparse aggregate | One-feature county/region aggregate reveals the site. | `HOLD` / `DENY`. |
| Stable jitter averaging | Repeated outputs enable location narrowing. | `DENY` / profile failure. |
| Tile extent leakage | Empty/nonempty tile pattern reveals location. | `DENY`. |
| Label placement | Label anchor follows hidden exact point. | `DENY`. |
| Map-fit side effect | Viewport auto-centers on restricted feature. | `DENY`. |
| Error leakage | Validation error includes exact geometry. | `ERROR` with sanitized report. |
| Cache key leakage | Key embeds source coordinates or restricted ID. | `DENY`. |
| Search ordering | Distance-ranked results reveal location. | `RESTRICT` / `DENY`. |
| Graph edge | Public relation links a generalized feature to a precise private asset. | `DENY`. |
| Export metadata | File metadata or auxiliary index contains exact extent. | `DENY`. |
| Screenshot/thumbnail | Rasterized output visibly narrows location. | `DENY`. |
| AI prose | Generated text gives directions, distances, or landmarks sufficient to reconstruct. | `ABSTAIN` / `DENY`. |
| Cross-release differencing | Old and new generalized releases narrow the source. | `HOLD` pending differential analysis. |

### Reconstruction posture

The most restrictive upstream rights, consent, sensitivity, review, and release posture must propagate through joins and derivatives. A “safe” object combined with another public object may become unsafe; fixtures should include such cross-object cases.

[Back to top](#top)

---

## Candidate-confirmed and source-role anti-collapse

Sensitive geometry often attaches to candidates, anomalies, or remote-sensing observations.

### Invariants

- `CandidateFeature` remains a candidate after redaction/generalization.
- `RemoteSensingAnomaly` remains an anomaly.
- `LiDARCandidate` remains a candidate.
- a generalized marker must not be labeled “archaeological site” unless a separate governed role transition and release support it;
- geometry transformation cannot strengthen evidentiary status;
- map symbols, colors, labels, API types, search categories, and AI wording must preserve candidate posture;
- absence of exact geometry does not make a candidate less uncertain;
- a receipt records transformation, not confirmation.

### Canary cases

- candidate payload rendered with confirmed-site icon;
- `source_role: candidate` omitted in public carrier;
- generalized anomaly described as a known site;
- transform receipt used as evidence of site existence;
- multiple candidate points aggregated into a “site cluster” without evidence/review;
- AI answer states certainty not supported by the released evidence.

Expected outcomes are `DENY`, `ABSTAIN`, or a failing assertion depending on the layer under test.

[Back to top](#top)

---

## Evidence, review, policy, receipt, and release closure

Public-safe geometry requires multiple independent closures.

| Closure | Required question | Missing/unresolved posture |
|---|---|---|
| Source-role closure | What role and authority does the source have? | `ABSTAIN` / `HOLD`. |
| Evidence closure | Does the claim resolve through EvidenceRef to an EvidenceBundle? | `ABSTAIN`. |
| Sensitivity closure | What is the most restrictive applicable rank/tier/context? | `DENY` / `HOLD`. |
| Profile closure | Is the named/versioned profile accepted and active? | `DENY`. |
| Transform closure | Is the transform semantically and operationally verified? | `ERROR` / `HOLD`. |
| Receipt closure | Does the receipt resolve and match input/output lineage? | `DENY` / `ERROR`. |
| Review closure | Are required steward/cultural/sensitivity/rights reviews present and scoped? | `HOLD` / `DENY`. |
| Policy closure | Does an accepted policy decision allow the exact audience/use and preserve obligations? | `DENY` / `ABSTAIN`. |
| Release closure | Does a release artifact cover this exact output/version/scope? | `ABSTAIN` / `DENY`. |
| Correction closure | Is there a correction/withdrawal/supersession path? | `HOLD`. |
| Rollback closure | Can the release be reversed and caches invalidated? | `HOLD`. |

No single fixture field may stand in for the entire closure chain.

### Resolve-or-fail behavior

Synthetic refs should test both:

- successful resolution through a controlled fixture registry; and
- unresolved, mismatched, stale, revoked, or wrong-version references.

A string that looks like `redaction-receipt:123` is not sufficient. Tests must establish what resolver is authoritative and what semantic checks it applies.

[Back to top](#top)

---

## Cultural, sovereignty, rights, consent, and consultation

Archaeology geometry can carry cultural, sovereignty, sacred-site, burial, oral-history, community-controlled, custodial, private-landowner, and collection-security obligations.

### Non-inference rules

- KFM does not infer cultural authority from a fixture.
- A steward review is not a cultural review by default.
- A cultural review record is not automatic consent.
- Consent is not inferred from source availability, prior publication, public indexing, coarse geometry, or lack of objection.
- Consultation is not inferred from a review reference.
- Rights clearance for one use/audience does not imply another.
- A sovereignty label is not permission to reveal the named authority when the authority identity is itself restricted.
- Revocation and embargo state are live inputs, not static documentation notes.

### Fixture safety

Fixtures must not contain:

- real community, tribe/nation, reviewer, participant, owner, custodian, or rights-holder identities unless expressly cleared for public test use;
- sacred/burial context detail;
- consent or revocation tokens;
- exact collection repository locations;
- private parcel/landowner detail;
- culturally restricted terminology or narratives;
- location hints derived from public landmarks.

Use role-only synthetic identifiers and policy-safe abstractions.

[Back to top](#top)

---

## Map, tile, API, export, screenshot, and AI boundaries

Public carriers are downstream consumers, not geometry authority.

### Map and tile

- consume only governed, released, public-safe geometry;
- do not receive internal geometry hidden by style;
- do not leak through bounds, zoom, labels, source metadata, feature IDs, tile sparsity, or cache behavior;
- preserve candidate/source role and sensitivity notices;
- reference release and receipt lineage where appropriate;
- invalidate or tombstone stale derivatives after correction/revocation.

### API and export

- use governed endpoints rather than canonical/internal stores;
- return finite decisions with safe reason codes;
- omit exact/internal geometry and unsafe metadata;
- do not expose internal refs that can be joined back to protected geometry;
- enforce audience/use/policy/release scope on every read;
- handle stale/revoked release state fail-closed.

### Screenshot and derived media

- screenshots, thumbnails, printable reports, scene exports, animations, and cached previews are releases/derivatives too;
- the absence of machine-readable coordinates does not make an image safe;
- derived media must be covered by the relevant release and correction/rollback path.

### AI and Focus Mode

- AI is interpretive and downstream of evidence, policy, review, and release;
- answers must not infer or reconstruct protected location detail;
- missing or conflicting release support causes narrowed scope, abstention, or denial;
- generated descriptions, distances, route cues, landmarks, and “near” statements must be tested as potential geometry leakage;
- an AI answer cannot use the fixture lane as evidence.

[Back to top](#top)

---

## No-network, security, and side effects

Default sensitive-geometry fixture tests should be hermetic.

### Prohibited default behavior

- live source, GIS, geocoder, map, tile, policy, review, receipt, release, cache, search, vector-index, graph, or AI service calls;
- DNS resolution or HTTP fallback;
- reads from production/internal lifecycle stores;
- writes to `data/`, `release/`, public artifacts, caches, object stores, registries, or audit ledgers;
- production credentials, private endpoints, real tokens, or production logs;
- invocation of external geocoders or reverse-geocoders;
- loading exact geometry from developer machines or environment variables;
- network-dependent golden files.

### Allowed default behavior

- local synthetic fixture loading;
- schema/contract/policy adapters loaded from pinned repository files;
- deterministic local transforms using synthetic non-operational inputs;
- fake resolvers with explicit maps;
- temporary-directory outputs deleted after test completion;
- sanitized validation reports containing no geometry/reconstruction clues.

### Network canary

A future harness should fail if any socket/network client is used unless the test is explicitly marked as governed integration and isolated from real sensitive data.

[Back to top](#top)

---

## Identity, version, hash, generation, and replay

Sensitive-geometry tests need deterministic identity without turning hashes into disclosure channels.

### Minimum posture

- stable fixture manifest ID;
- explicit manifest/schema/contract/profile versions;
- stable synthetic source-object identity;
- deterministic seed/clock for any stochastic test transform;
- canonical JSON serialization before hashing;
- stable ordering;
- input and expected-output hashes where safe;
- explicit generator version;
- receipt/profile version pins;
- replay result comparison;
- supersession linkage when expected output changes.

### Hash safety

Do not publish hashes of real protected geometry or restricted payloads in public fixtures. Hashes can become correlation or confirmation oracles. Use synthetic payloads only.

### Replay expectations

A deterministic profile test should distinguish:

- same input + same profile version + same seed context → same output;
- changed profile version → explicitly different expected output and migration path;
- revoked profile → deny, not replay;
- mismatched input/output hash → error;
- nondeterministic result under deterministic contract → error;
- intentionally nondeterministic method → requires explicit accepted contract and risk review rather than silent tolerance.

[Back to top](#top)

---

## Valid, invalid, denied, restricted, held, abstained, quarantined, and error cases

A mature fixture family needs positive and negative polarity beyond “JSON parses.”

| Case | Example | Expected layer result |
|---|---|---|
| Valid shape, internal only | Synthetic `SpatialGeometry` with explicit CRS/precision, no public use. | Schema/test `PASS`; no release implication. |
| Valid public-safe candidate | Synthetic generalized carrier with complete synthetic closure refs. | Test `PASS`; policy/runtime depends on resolved fixtures. |
| Invalid shape | Missing `crs` or unknown precision bucket. | Test `FAIL` / schema error. |
| Exact geometry public-bound | Exact/internal geometry present. | Policy `DENY`; test `PASS` when denial is expected. |
| Unresolved profile | Profile ID absent from accepted registry. | `DENY`. |
| Unversioned profile | Inline or unpinned profile. | `DENY`. |
| Placeholder receipt | `generalize_to_township.json` used as receipt. | Validation failure / `DENY`. |
| Receipt mismatch | Input/output hashes or profile mismatch. | `ERROR` / `DENY`. |
| Missing evidence | Claim-like geometry summary without resolvable EvidenceBundle. | `ABSTAIN`. |
| Missing review | Sensitive carrier lacks required review. | `HOLD` / `DENY`. |
| Missing consent/rights | Cultural/consent-bound context unresolved. | `HOLD` / `DENY`. |
| Restricted audience | Output may be used only under named restricted audience. | `RESTRICT` with obligations. |
| Sparse aggregate | Generalized count still discloses location. | `DENY` / `HOLD`. |
| Candidate role lost | Candidate rendered as confirmed site. | `DENY` / assertion failure. |
| Revoked profile/consent | Previously acceptable output becomes disallowed. | `DENY`, invalidate carriers. |
| Stale release | Release/receipt version mismatch. | `ABSTAIN` / `DENY`. |
| Quarantine | Fixture provenance or safety cannot be reviewed. | Remove from normal collection / `QUARANTINE`. |
| Network attempt | Test calls live geocoder/map/API. | `ERROR` / assertion failure. |
| Side-effect attempt | Test writes to governed roots. | `ERROR` / assertion failure. |
| Validator stub | Dedicated validator raises `NotImplementedError`. | `ERROR`; never green. |
| Empty fixture family | No positive/negative payloads collected. | Coverage failure, not success. |

### Invalid fixtures must remain safe

A negative fixture does not need real sensitive detail. Use symbolic geometry tokens, clearly impossible/non-geographic coordinate canaries, or structural violations that cannot identify a real place.

[Back to top](#top)

---

## Correction, withdrawal, revocation, cache invalidation, and rollback

Sensitive geometry is time-aware. A carrier that was once allowed may later become unsafe or stale.

### Required future cases

- source correction changes the underlying geometry;
- sensitivity rank/tier becomes more restrictive;
- redaction profile is deprecated or revoked;
- receipt is invalidated;
- rights or consent are revoked;
- cultural/sovereignty review changes;
- candidate is rejected, confirmed, or superseded through a separate governed event;
- release manifest is corrected, withdrawn, or superseded;
- map tile, API cache, search index, vector index, screenshot, export, and AI cache must invalidate;
- rollback restores a prior safe release or removes the carrier entirely.

### No silent regeneration

Do not silently rerender prior public outputs under a new profile version. Emit explicit supersession/correction lineage and preserve the rollback target.

### Tombstone posture

When an output is withdrawn, public clients should receive a safe withdrawn/not-available posture. Tombstones must not reveal why in a way that leaks restricted context.

### Fixture assertions

- revoked refs no longer resolve as active;
- stale release hashes are denied;
- caches and indexes are included in invalidation expectations;
- rollback does not restore an unsafe earlier artifact;
- correction notices do not embed exact geometry;
- old and new generalized outputs are checked for differential reconstruction risk.

[Back to top](#top)

---

## Inventory, orphans, nonempty coverage, and vacuous-pass risk

Documentation presence is not fixture coverage.

### Required future inventory fields

| Field | Purpose |
|---|---|
| fixture path | Exact tracked file. |
| fixture family | Shape, transform, receipt, policy, carrier, side channel, correction, or rollback. |
| polarity | valid, invalid, deny, restrict, hold, abstain, quarantine, error. |
| object/contract/schema version | What semantics are expected. |
| consumer test ref | Who uses it. |
| expected outcome/reason | Finite assertion. |
| sensitivity review state | Public-safe fixture confirmation. |
| generator/version/hash | Deterministic provenance. |
| deprecation/removal state | Lifecycle. |

### Vacuous-pass conditions

The suite must fail when:

- zero fixtures are discovered;
- only positive fixtures exist;
- only negative fixtures exist;
- a schema has no paired fixture family;
- the direct lane contains no declared payloads but a command returns zero;
- every test is skipped;
- validator stubs are swallowed or marked expected without an explicit maturity gate;
- placeholder payloads are counted as semantic coverage;
- policy/profile registries cannot resolve but tests bypass them;
- consumer backlink checks are absent;
- expected reason codes are not asserted.

### Coverage minimum

Before claiming a fixture family is substantive, establish at least:

- one positive internal-shape case;
- one public-safe positive case with complete synthetic closure;
- one exact-geometry deny case;
- one unresolved-profile deny case;
- one receipt mismatch case;
- one missing-evidence abstain case;
- one missing-review/rights hold or deny case;
- one reconstruction/side-channel deny case;
- one candidate-role preservation case;
- one revocation/correction/rollback case;
- one no-network/side-effect case.

[Back to top](#top)

---

## Deterministic validation commands

No dedicated executable command for this direct lane is confirmed.

### Documentation checks performed for this revision

```bash
# Illustrative local checks used for the README artifact itself
python -m compileall <not-applicable-for-markdown>
# Markdown structure, anchors, tables, whitespace, and secret patterns were checked separately.
```

### Proposed future targeted command

```bash
pytest -q tests/domains/archaeology/fixtures/sensitive_geometry
```

This command is **PROPOSED** because the child lane is absent at the checked path.

### Proposed future fixture-inventory command

```bash
python -m tools.validators.fixture_inventory \
  --fixture-root tests/fixtures/domains/archaeology/sensitive_geometry \
  --require-consumers \
  --require-nonempty-polarity
```

The module and options are **PROPOSED** and must not be presented as current repository behavior.

### Command requirements before documentation promotion

- exact command exists;
- zero-collected cases fail;
- no-network posture is enforced;
- placeholders are rejected as substantive fixtures;
- validator stubs fail visibly;
- expected reason codes are asserted;
- outputs are deterministic and sanitized;
- command is linked from the owning test README and CI job.

[Back to top](#top)

---

## Runner, CI, and promotion boundary

### Current evidence

- the direct lane is README-only;
- the owning domain fixture-test parent exists, but no checked sensitive-geometry child exists;
- the dedicated sensitive-geometry validator lane surfaced only a README;
- `validate_spatial_geometry.py` is a stub;
- the Archaeology workflow is TODO-only in checked evidence;
- relevant Makefile fixture behavior is not substantive;
- no required-check or branch-protection significance was verified.

### CI requirements before calling the lane enforced

- collect the owning executable suite;
- fail on zero cases and excessive skips;
- enforce no-network and no-governed-root writes;
- verify fixture inventory and backlinks;
- run shape, semantic, policy, receipt, side-channel, release, revocation, and rollback cases;
- pin schema/contract/profile versions;
- publish a sanitized machine-readable test artifact;
- distinguish expected deny/abstain from test failure;
- block promotion when a required sensitive-geometry gate fails;
- never publish geometry as a CI side effect.

### Promotion rule

A green documentation, schema, fixture, validator, map, API, or CI check is not a PromotionDecision or ReleaseManifest. Promotion remains a governed state transition with evidence, validation, policy, review, receipt, correction, and rollback support.

[Back to top](#top)

---

## Failure interpretation

| Failure | Likely meaning | Safe response |
|---|---|---|
| Missing parent/consumer link | Documentation or ownership drift. | Block fixture admission; repair link/ownership. |
| Placeholder counted as payload | Maturity overclaim. | Reject coverage claim. |
| Shape validation failure | Schema mismatch. | Correct fixture/schema through owning lane. |
| Shape pass but semantic failure | Contract/policy gap. | Deny/hold; do not weaken semantics. |
| Exact geometry detected | Sensitive exposure risk. | Deny, sanitize reports, quarantine source. |
| Reverse-engineering canary triggered | Public derivative is unsafe. | Deny and revise profile/transform. |
| Profile unresolved/revoked | Policy artifact unavailable. | Deny. |
| Receipt unresolved/mismatched | Transform lineage unproven. | Deny/error. |
| Evidence unresolved | Claim unsupported. | Abstain. |
| Review/rights/consent unresolved | Authority incomplete. | Hold/deny. |
| Release ref missing/stale | Public use unauthorized. | Deny/abstain. |
| Validator stub executed | Implementation gap. | Error; do not mark green. |
| Network attempted | Hermeticity/security failure. | Fail test and investigate. |
| Governed-root write attempted | Side-effect/authority breach. | Fail test and rollback artifact. |
| Cache invalidation failure | Revoked/stale carrier remains accessible. | Incident/correction/rollback path. |
| Outcome vocabulary mismatch | Contract drift. | Block until adapter/ADR resolves. |

Failures should preserve enough sanitized context for correction without embedding the sensitive value that caused the failure.

[Back to top](#top)

---

## What a passing suite does not prove

Even a mature passing suite would not prove:

- an archaeological site exists;
- coordinates are accurate or survey-authoritative;
- a candidate is confirmed;
- a source role is primary or authoritative;
- a profile is legally or culturally sufficient for every use;
- a transform actually ran in production;
- a receipt was emitted in production;
- evidence is complete beyond the tested fixture;
- cultural authority, consultation, or consent occurred;
- rights are resolved for untested uses or audiences;
- policy is correctly deployed in every runtime;
- release occurred;
- maps, tiles, APIs, exports, screenshots, indexes, or AI surfaces are safe outside tested versions;
- branch protection requires the check;
- correction, revocation, cache invalidation, and rollback work in production;
- no unknown reconstruction attack exists.

Passing means only that the defined bounded assertions passed against the pinned synthetic inputs and versions.

[Back to top](#top)

---

## Proposed layout and routing

The direct lane should remain declarative and small.

```text
tests/fixtures/domains/archaeology/sensitive_geometry/
├── README.md
├── manifest.json                         # PROPOSED; only when consumers exist
├── public_safe_missing_receipt.json      # PROPOSED test-local manifest
├── exact_geometry_denied.json            # PROPOSED structural/symbolic negative case
├── reverse_engineering_denied.json       # PROPOSED side-channel manifest
└── revoked_profile_denied.json           # PROPOSED revocation manifest
```

Executable tests should live in an owning test lane:

```text
tests/domains/archaeology/fixtures/sensitive_geometry/
├── README.md                              # PROPOSED; absent at checked path
├── test_fixture_inventory.py
├── test_spatial_geometry_shape.py
├── test_exact_geometry_denial.py
├── test_profile_and_receipt_resolution.py
├── test_candidate_role_preservation.py
├── test_side_channel_reconstruction.py
├── test_no_network_and_no_side_effects.py
└── test_revocation_correction_rollback.py
```

Reusable payloads should remain under accepted `fixtures/` children. Do not create duplicate profile, schema, receipt, policy, or release homes beneath this directory.

The proposed tree is not repository fact and should not be created wholesale without consumer-backed need.

[Back to top](#top)

---

## Maintenance and fixture update rules

When adding or changing a fixture:

1. identify the owning consumer and requirement;
2. verify Directory Rules and parent guidance;
3. confirm the fixture is synthetic and non-reconstructive;
4. choose the correct reusable or test-local home;
5. pin contract/schema/profile versions;
6. declare geometry role, precision, sensitivity, and expected outcomes;
7. add positive and negative polarity;
8. add consumer backlinks and inventory entry;
9. run no-network and no-side-effect checks;
10. run secret/protected-detail scans;
11. verify sanitized failures;
12. update docs, coverage, and deprecation state;
13. preserve correction/revocation/rollback expectations;
14. do not treat the fixture change as policy/review/release approval.

### Review triggers

Require elevated sensitivity/geoprivacy review when a change:

- adds coordinate-like values;
- changes precision or generalization posture;
- changes profile parameters or version;
- changes receipt or resolver behavior;
- changes candidate/source-role rendering;
- changes map/tile/API/export/AI behavior;
- affects rights, consent, sovereignty, cultural context, or participant identity;
- weakens deny/hold/abstain behavior;
- changes correction, revocation, or cache invalidation expectations.

[Back to top](#top)

---

## Migration, deprecation, and lane retention

### Lane-retention decision

This lane should be retained only if test-local manifests exist that cannot safely or cleanly live in reusable fixture roots and have verified consumers.

Possible governed outcomes:

| Outcome | Condition | Required action |
|---|---|---|
| Retain | Active consumer-backed test-local manifests exist. | Add inventory, ownership, commands, and CI. |
| Merge into reusable fixture child | Payload is reused across consumers. | Move with migration note and update backlinks. |
| Move to contract fixture root | Payload is primarily schema-shape coverage. | Preserve polarity and expected errors. |
| Remove | README remains empty of consumers/payloads and adds no value. | Delete via reviewed PR; update parent index. |
| Quarantine | A fixture contains questionable coordinate/provenance material. | Remove from normal tests and investigate under restricted process. |

### Deprecation rules

- mark fixture/profile/manifest version deprecated;
- identify replacement;
- retain only when historical compatibility tests require it;
- prevent deprecated profile from authorizing new public output;
- preserve supersession links;
- remove after the documented support window and final consumer removal;
- verify no cache/index/public artifact still depends on it.

[Back to top](#top)

---

## Definition of done

This lane is not substantively implemented until all applicable items are verified.

| Area | Done condition |
|---|---|
| Ownership | Named maintainers and CODEOWNERS/rules verified. |
| Lane decision | Retain/migrate/remove decision recorded. |
| Parent indexes | `tests/fixtures/domains/` and child routing are current. |
| Inventory | Nonempty, reviewed fixture inventory exists. |
| Consumers | Every fixture has a resolvable active consumer. |
| Orphan control | Bidirectional and removal checks exist. |
| Synthetic safety | No protected or reconstructive material; scans and review pass. |
| SpatialGeometry | Shape and semantic checks exist; validator implemented or officially retired. |
| Transform semantics | SensitivityTransform schema/validator enforce substantive fields. |
| Receipt semantics | PublicationTransformReceipt and RedactionReceipt have accepted schemas/contracts/validators. |
| Profile catalog | Canonical, versioned, reviewed catalog and activation state exist. |
| Policy | Archaeology sensitivity rules are executable and tested. |
| Review/rights | Cultural, sovereignty, rights, consent, and separation-of-duties behavior is testable. |
| Evidence | EvidenceRef resolution and missing-evidence abstention are tested. |
| Exposure | Exact, side-channel, and reconstruction attacks are tested. |
| Candidate posture | Candidate/source role is preserved across carriers. |
| Public surfaces | Map/tile/API/export/screenshot/AI tests consume released public-safe derivatives only. |
| Hermeticity | No-network and no-governed-root-write enforcement exists. |
| Determinism | Stable versions, clocks, seeds, hashes, ordering, and replay. |
| CI | Substantive jobs run, fail on zero cases, and report finite outcomes. |
| Promotion | Required-check significance verified; no automatic publication. |
| Correction | Revocation, correction, withdrawal, cache invalidation, and rollback exercised. |
| Documentation | Commands, evidence, limitations, migration, and rollback remain current. |

Until then, this README remains a routing and safety contract, not proof of implemented sensitive-geometry coverage.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status | Evidence needed |
|---|---|---|---|
| ARCH-SG-FIX-001 | Should this direct lane be retained? | NEEDS VERIFICATION | fixture-owner and test-owner decision |
| ARCH-SG-FIX-002 | Who owns the lane? | NEEDS VERIFICATION | CODEOWNERS or steward assignment |
| ARCH-SG-FIX-003 | Should `tests/fixtures/domains/README.md` be created? | NEEDS VERIFICATION | parent-tree documentation decision |
| ARCH-SG-FIX-004 | What exact threshold admits test-local fixtures here? | NEEDS VERIFICATION | accepted fixture-home rule |
| ARCH-SG-FIX-005 | What is the canonical manifest schema? | UNKNOWN | contract/schema/ADR |
| ARCH-SG-FIX-006 | What are the stable fixture identity/version/hash rules? | NEEDS VERIFICATION | identity contract |
| ARCH-SG-FIX-007 | What is the canonical geometry-role vocabulary? | UNKNOWN | contract/schema/policy decision |
| ARCH-SG-FIX-008 | How do precision bucket, sensitivity rank, audience tier, and geometry role relate? | NEEDS VERIFICATION | adapter contract and tests |
| ARCH-SG-FIX-009 | When will `validate_spatial_geometry.py` be implemented or retired? | UNKNOWN | tooling decision |
| ARCH-SG-FIX-010 | When will SensitivityTransform schema gain substantive fields? | UNKNOWN | schema PR and review |
| ARCH-SG-FIX-011 | When will PublicationTransformReceipt schema gain substantive fields? | UNKNOWN | schema PR and review |
| ARCH-SG-FIX-012 | What semantic contract governs RedactionReceipt? | UNKNOWN | contract path and accepted schema linkage |
| ARCH-SG-FIX-013 | Which source docs should govern RedactionReceipt across domains? | CONFLICTED | contract/schema provenance decision |
| ARCH-SG-FIX-014 | Where is the canonical active redaction profile catalog? | CONFLICTED / NEEDS VERIFICATION | policy ownership and activation evidence |
| ARCH-SG-FIX-015 | Are the Archaeology profile IDs in doctrine implemented? | UNKNOWN | catalog, policy, verifier, and fixtures |
| ARCH-SG-FIX-016 | Is `generalize_to_township.json` retained, replaced, or removed? | NEEDS VERIFICATION | fixture review |
| ARCH-SG-FIX-017 | Which executable tests consume Archaeology sensitive-geometry fixtures? | UNKNOWN | repository test inventory |
| ARCH-SG-FIX-018 | Where should the executable child lane live? | NEEDS VERIFICATION | parent test-lane decision |
| ARCH-SG-FIX-019 | How are consumer backlinks and orphan checks enforced? | NEEDS VERIFICATION | inventory validator/test |
| ARCH-SG-FIX-020 | Which exact policy bundle/version governs Archaeology geometry exposure? | NEEDS VERIFICATION | concrete policy files and registry |
| ARCH-SG-FIX-021 | Should `policy/sensitivity/archaeology/` exist, and what owns it? | NEEDS VERIFICATION | policy placement decision |
| ARCH-SG-FIX-022 | How are cultural authority, sovereignty, rights, consent, and consultation represented safely? | NEEDS VERIFICATION | reviewed contracts/policy/fixtures |
| ARCH-SG-FIX-023 | How is separation of duties enforced? | NEEDS VERIFICATION | accepted ADR, platform, policy, and tests |
| ARCH-SG-FIX-024 | What side-channel and reconstruction-risk suite is required? | UNKNOWN | threat model and test specification |
| ARCH-SG-FIX-025 | How are sparse aggregates and cross-release differencing tested? | UNKNOWN | privacy/geoprivacy test design |
| ARCH-SG-FIX-026 | How are profile and receipt revocations propagated? | NEEDS VERIFICATION | runtime/cache/index integration tests |
| ARCH-SG-FIX-027 | How are correction, withdrawal, and rollback propagated to map/API/tile/export/AI surfaces? | NEEDS VERIFICATION | integration tests |
| ARCH-SG-FIX-028 | Are secret, coordinate-like, and reconstruction-canary scans enforced? | UNKNOWN | CI/test evidence |
| ARCH-SG-FIX-029 | Are no-network and no-governed-root-write rules enforced? | UNKNOWN | sandbox/test evidence |
| ARCH-SG-FIX-030 | Which workflows trigger and which checks are required by branch protection? | UNKNOWN | workflow/ruleset evidence |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| Uploaded implementation prompt v3.1 | CONFIRMED user-supplied instruction | implementation workflow, tests README profile, acceptance, validation, and handoff requirements | repository state |
| `docs/doctrine/directory-rules.md` | CONFIRMED repository doctrine | responsibility-root placement and no parallel authority | target implementation maturity |
| Schema-home ADR | CONFIRMED file; status proposed | schema/contract/fixture separation | accepted ADR status or CI enforcement |
| Drift register | CONFIRMED file | recorded repository drift | exhaustive drift |
| Target v0.1 README | CONFIRMED prior content | preserved synthetic/no-network/exposure safety intent and stale claims to correct | executable fixture coverage |
| `tests/fixtures/README.md` | CONFIRMED | test-local versus reusable fixture split | lane retention |
| Archaeology test-fixture parent | CONFIRMED | parent exists and indexes sensitive_geometry child | payload and consumer maturity |
| Archaeology domain test READMEs | CONFIRMED | executable test ownership and boundaries | sensitive-geometry child implementation |
| Reusable Archaeology fixtures README | CONFIRMED | domain fixture routing | substantive geometry payload coverage |
| Synthetic publication-transform receipt README | CONFIRMED | intended receipt-shaped fixture lane | semantic payload validity |
| `generalize_to_township.json` | CONFIRMED placeholder | planned path lineage | transform execution, receipt validity, or safe output |
| SpatialGeometry contract | CONFIRMED draft v0.2 | geometry/CRS/precision semantics and anti-collapse rules | exposure safety or runtime behavior |
| SpatialGeometry schema | CONFIRMED PROPOSED | required shape and precision enum | geometry validity, sensitivity, or release |
| SpatialGeometry validator | CONFIRMED stub | path exists | validator behavior |
| SensitivityTransform contract | CONFIRMED draft v0.2 | transform semantics and boundaries | machine enforcement |
| SensitivityTransform schema | CONFIRMED permissive PROPOSED scaffold | file/path pairing | semantic validity |
| PublicationTransformReceipt contract | CONFIRMED draft v0.2 | receipt semantics and boundaries | emitted receipts or release |
| PublicationTransformReceipt schema | CONFIRMED permissive PROPOSED scaffold | file/path pairing | semantic validity |
| Redaction Profiles standard | CONFIRMED draft | named/versioned/deterministic/receipt-bearing doctrine | active catalog or runtime enforcement |
| `policy/redaction/profiles.yaml` | CONFIRMED placeholder | planned catalog path | active profiles, Archaeology ownership, or verification |
| RedactionReceipt schema | CONFIRMED permissive PROPOSED scaffold | checked schema path | receipt semantics, Archaeology provenance, or validation |
| Archaeology sensitivity doc | CONFIRMED draft | deny-by-default, tier/rank/profile/revocation doctrine | executable policy or safe parameters |
| Archaeology publication/policy doc | CONFIRMED draft | trust membrane, governed public surfaces, release/correction posture | implemented routes or gates |
| Archaeology domain policy README | CONFIRMED draft | policy-lane intent and finite outcomes | concrete bundles or runtime enforcement |
| Missing sensitivity subpolicy README | CONFIRMED bounded 404 | named path absent at snapshot | permanent absence or policy decision |
| Sensitive-geometry validator README | CONFIRMED | validator routing and exposure threat classes | executable validator |
| Bounded validator search | CONFIRMED | only README surfaced in direct lane | permanent/exhaustive absence |
| API, promotion, and review sibling READMEs | CONFIRMED | consistent test-local routing and no-authority boundaries | sensitive-geometry implementation |
| Makefile | CONFIRMED | current target behavior and TODOs | future commands |
| `domain-archaeology` workflow | CONFIRMED TODO scaffold | dedicated trigger exists | substantive CI or required-check status |
| Checked 404 paths | CONFIRMED bounded checks | named direct/consumer paths absent at pinned ref | permanent or exhaustive absence |

[Back to top](#top)

---

## Rollback

This is a documentation-only revision.

Before merge, rollback means leaving the draft pull request unmerged or adding a transparent revert commit to the feature branch. Do not reset or force-push shared history.

After merge, rollback means a transparent revert commit or revert pull request based on the merged commit, followed by documentation validation.

Rollback is required if this README:

- is mistaken for geometry, policy, profile, transform, receipt, evidence, review, release, or publication authority;
- directs executable tests into a fixture payload directory;
- encourages storage of real coordinates or reconstruction hints;
- claims substantive schema, validator, profile, policy, receipt, or CI coverage without evidence;
- treats `generalize_to_township.json` or any filename as transform/receipt proof;
- treats shape validity or a coarse precision bucket as exposure safety;
- treats a profile reference as proof the profile exists, is active, or was applied;
- silently collapses SpatialGeometry, transform, receipt, policy, review, evidence, promotion, release, or public-carrier families;
- weakens exact-location, burial, sacred-site, human-remains, collection-security, cultural, sovereignty, rights, consent, consultation, private-landowner, candidate-role, or looting-risk safeguards;
- hides validator stubs, placeholder catalogs, permissive schemas, missing policy paths, or TODO-only CI behavior;
- creates or implies a parallel fixture, schema, policy, profile, receipt, review, release, map, API, or AI authority.

**No-loss assessment:** v0.2 preserves the v0.1 synthetic-only, no-network, exact-geometry denial, generalized-only, evidence, policy, review, receipt, release, correction, withdrawal, rollback, map, API, and AI-boundary intent. It corrects stale parent-path claims, removes misleading executable-test placement, grounds geometry/transform/receipt/profile maturity in current repository evidence, surfaces placeholder and permissive-schema risks, adds reconstruction and side-channel controls, strengthens cultural/rights/consent non-inference, and makes implementation gaps inspectable.

[Back to top](#top)
