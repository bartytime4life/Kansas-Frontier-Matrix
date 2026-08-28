<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/agriculture/catalog/readme
title: fixtures/domains/agriculture/catalog/ — Agriculture Catalog Fixture Boundary
type: readme; directory-readme; fixture-lane; agriculture-domain; catalog-fixture-boundary
version: v0.2.0
status: draft; repository-grounded; README-only; structurally-empty; fixture-only; implementation-blocked; non-authoritative
owners: GitHub review route CONFIRMED — @bartytime4life; governance role assignments OWNER_TBD — Agriculture domain steward · Catalog steward · Fixture steward · Contract and schema steward · Evidence steward · Policy steward · Validation steward · Release steward · Docs steward
created: NEEDS VERIFICATION — the lane and a blank-file expansion predate this revision
updated: 2026-07-20
policy_label: public-review; synthetic-fixtures-only; no-canonical-data; no-publication-authority
current_path: fixtures/domains/agriculture/catalog/README.md
responsibility_root: fixtures/
truth_posture: >
  CONFIRMED the target path, direct-child inventory, parent Agriculture fixture
  README, live and duplicate Directory Rules copies, drift register, current draft
  CatalogMatrix contract, two permissive CatalogMatrix schema placeholders, the
  domain validator placeholder, the catalog-closure test placeholder, the proposed
  catalog-closure ADRs, and the Agriculture CI readiness hold at the pinned base /
  PROPOSED fixture admission contract, case taxonomy, expected layout, naming
  rules, validation sequence, and definition of done /
  UNKNOWN accepted CatalogMatrix authority and final path topology, substantive
  validator behavior, collected catalog-closure tests, reason-code vocabulary,
  policy evaluation, fixture regeneration, CI enforcement, public consumers,
  owners, and production use /
  NEEDS VERIFICATION before payload admission: accepted semantic contract and
  schema pair, consuming test or validator, deterministic identity and digest
  grammar, expected outcomes, rights and sensitivity posture, and correction and
  rollback requirements
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 9a29f659be82af7acbed4a2563ab8f96c1f84046
  prior_blob: 37fff71f890b67e38303a852d1d97432ad22a4c0
  directory_rules_live_blob: 18653c00ba193a4afaa3e07a0924452807fb98ef
  directory_rules_duplicate_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  catalog_matrix_contract_blob: c67923beb505aa39e7c0c768c16e75a00826ff31
  data_catalog_matrix_schema_blob: 75a927376066226d8a0f89a630d7bb3693143c41
  agriculture_catalog_matrix_schema_blob: fa72fae93bb1b4af94ee1e292b8aaf305841a269
  agriculture_catalog_matrix_validator_blob: 177914fce5674ad707448c76225422b1b9d72e12
  agriculture_catalog_closure_test_blob: 0ba84246303e04c112a9c403e057fffb36078d12
  agriculture_workflow_blob: 1dd9938b92de61c7d905f30170cf6394e6c06ea1
related:
  - ../README.md
  - ../../../README.md
  - ../../../../contracts/data/catalog_matrix.md
  - ../../../../schemas/contracts/v1/data/catalog_matrix.schema.json
  - ../../../../schemas/contracts/v1/domains/agriculture/catalog_matrix.schema.json
  - ../../../../tools/validators/domains/agriculture/validate_catalog_matrix.py
  - ../../../../tests/domains/agriculture/test_catalog_closure.py
  - ../../../../tests/domains/agriculture/catalog_closure/README.md
  - ../../../../data/catalog/domain/agriculture/README.md
  - ../../../../policy/domains/agriculture/README.md
  - ../../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../docs/architecture/directory-rules.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/registers/DRIFT_REGISTER.md
  - ../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
  - ../../../../.github/workflows/domain-agriculture.yml
tags: [kfm, fixtures, agriculture, catalog, catalog-matrix, evidence-closure, source-role, lifecycle, policy, release, correction, rollback, no-network, synthetic, fail-closed]
notes:
  - "This revision changes the target README only; a generated-work receipt is maintained separately under the repository's existing receipt authority."
  - "At the pinned base, this directory contains only .gitkeep and README.md; it contains no fixture payload, expected-output file, or child directory."
  - "The proposed layout and case matrix below are admission guidance, not claims that fixtures or enforcement exist."
  - "A fixture, passing schema check, green workflow, receipt, catalog record, or pull request is not evidence truth, policy approval, release approval, or KFM publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture catalog fixture boundary

`fixtures/domains/agriculture/catalog/` is the review boundary for future, synthetic Agriculture catalog-shaped fixtures. At the recorded repository snapshot, the lane is **structurally empty**: it contains only `.gitkeep` and this README.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2.0" src="https://img.shields.io/badge/version-v0.2.0-informational">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-success">
  <img alt="Inventory: no payloads" src="https://img.shields.io/badge/inventory-no%20payloads-lightgrey">
  <img alt="Validator: placeholder" src="https://img.shields.io/badge/validator-placeholder-orange">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

> [!IMPORTANT]
> **This lane is not a catalog.** Material here may model a catalog candidate for a bounded test. It is never a canonical catalog record, SourceDescriptor, EvidenceBundle, proof, PolicyDecision, PromotionDecision, ReleaseManifest, published layer, public API response, or publication authorization.

> [!CAUTION]
> **Do not add payloads yet without a named consumer.** Current repository evidence contains competing CatalogMatrix path declarations, permissive placeholder schemas, a domain validator that raises `NotImplementedError`, and a docstring-only catalog-closure test module. An unconsumed JSON example would create apparent maturity without enforceability.

> [!WARNING]
> **Fail closed on consequential gaps.** Missing or conflicting identity, digest, source role, evidence, rights, sensitivity, lifecycle, policy, review, release, correction, or rollback support must remain invalid, denied, held, abstained, quarantined, or explicitly unresolved. Do not infer success from plausible content.

**Quick links:** [Purpose](#purpose) · [Status](#verified-status) · [Placement](#placement-and-authority) · [Admission](#fixture-admission-contract) · [Cases](#proposed-case-matrix) · [Layout](#proposed-layout) · [Validation](#validation) · [Maintenance](#maintenance-workflow) · [Evidence](#evidence-ledger) · [Rollback](#correction-removal-and-rollback) · [Done](#definition-of-done)

---

## Purpose

This directory is reserved for small, deterministic, public-safe Agriculture examples that exercise an accepted catalog contract, schema, validator, resolver, policy helper, or test without reading canonical lifecycle stores.

When the lane becomes executable, its fixtures should help prove bounded questions such as:

- whether a catalog candidate has stable identity and digest posture;
- whether Agriculture source roles remain explicit and non-collapsed;
- whether consequential `EvidenceRef` values resolve to adequate `EvidenceBundle` support;
- whether aggregation, rights, sensitivity, lifecycle, policy, review, and release state remain distinct;
- whether STAC, DCAT, and PROV projections agree where an accepted catalog-closure contract requires agreement;
- whether exact field, operator, farm, parcel, private-yield, or restricted-source exposure fails closed;
- whether receipts, proofs, catalogs, manifests, and release decisions remain separate object families; and
- whether correction, supersession, withdrawal, and rollback references remain inspectable.

A fixture is evidence about a test case, not evidence that an Agriculture claim is true. A passing case proves only the named assertion under the pinned schema, validator, policy, and test versions.

---

## Verified status

### Direct inventory at the pinned base

| Direct child | Kind | Status | Safe conclusion |
|---|---|---:|---|
| `.gitkeep` | zero-byte placeholder | CONFIRMED | Preserves the directory in Git; carries no fixture semantics. |
| `README.md` | directory guide | CONFIRMED | Documents the intended boundary; does not implement it. |
| JSON/YAML fixture payloads | none present | CONFIRMED ABSENT | No positive, invalid, denial, snapshot, or expected-output case exists in this lane. |
| Child directories | none present | CONFIRMED ABSENT | `valid/`, `invalid/`, `denied/`, and other layouts below are proposed only. |

The inventory was obtained from the complete, non-truncated Git tree for `main@9a29f659be82af7acbed4a2563ab8f96c1f84046`, not from filename search alone.

### Adjacent implementation evidence

| Surface | Observed state | Consequence for this lane |
|---|---|---|
| `contracts/data/catalog_matrix.md` | Draft semantic contract exists. | Useful meaning source, but not an accepted final topology or executable contract. |
| `schemas/contracts/v1/data/catalog_matrix.schema.json` | Placeholder; requires only `id` and permits additional properties. | Shape success is too weak to prove catalog closure. |
| `schemas/contracts/v1/domains/agriculture/catalog_matrix.schema.json` | Second placeholder with the same minimal shape. | Creates an unresolved generic-versus-domain schema profile question. |
| Domain schema `x-kfm.fixtures_root` | Declares `fixtures/domains/agriculture/catalog_matrix/`. | That declared path is absent and differs from this existing `catalog/` lane. |
| Data schema `x-kfm.fixtures_root` | Declares `fixtures/data/catalog_matrix/`. | That declared path is also absent at the pinned base. |
| `contracts/domains/agriculture/catalog_matrix.md` | Not present. | The domain schema's declared semantic contract does not resolve. |
| `tools/validators/domains/agriculture/validate_catalog_matrix.py` | Exists but `main()` raises `NotImplementedError`. | No substantive domain CatalogMatrix validation is established. |
| `tests/domains/agriculture/test_catalog_closure.py` | Docstring-only `PROPOSED placeholder`. | No collected closure assertion is established by this module. |
| `tests/domains/agriculture/catalog_closure/` | README plus `.gitkeep`; no executable child test. | Test design exists, implementation does not. |
| `.github/workflows/domain-agriculture.yml` | Pull-request workflow with explicit validation/proof/release holds. | A green held job is readiness evidence only, not validation or release proof. |
| `make fixtures` | Prints a TODO readiness marker. | It does not generate, verify, or refresh fixtures. |

### Maturity statement

| Capability | Status |
|---|---:|
| Fixture lane documentation | CONFIRMED |
| Fixture payload inventory | CONFIRMED EMPTY |
| Accepted CatalogMatrix contract/schema/path pairing | UNKNOWN / CONFLICTED |
| Executable Agriculture CatalogMatrix validator | NOT IMPLEMENTED at inspected path |
| Collected catalog-closure tests consuming this lane | NOT ESTABLISHED |
| Deterministic fixture regeneration | NOT ESTABLISHED |
| Policy and EvidenceBundle resolution | UNKNOWN |
| CI enforcement of this lane | NOT ESTABLISHED |
| Release or publication authority | NOT APPLICABLE / NOT GRANTED |

---

## Placement and authority

Directory Rules assigns `fixtures/` to the validate/operate responsibility surface. The Agriculture segment is appropriate for Agriculture-specific synthetic inputs and expected outputs. Editing this existing README does not create a new root, move authority, or approve either competing CatalogMatrix path declaration.

The repository contains two Directory Rules copies. The architecture-side document identifies itself as the live v1.3.1 artifact while recording the doctrine-side path as unresolved drift. This README cites both and does not attempt to settle that repository-wide placement decision.

### Authority matrix

| Responsibility | Authority home | This lane's role |
|---|---|---|
| Synthetic Agriculture catalog fixtures | `fixtures/domains/agriculture/catalog/` | Owns bounded test inputs and expected outputs only after admission. |
| CatalogMatrix semantic meaning | Current draft: `contracts/data/catalog_matrix.md` | References meaning; does not redefine it. |
| Machine-checkable CatalogMatrix shape | `schemas/contracts/v1/...` after accepted profile/path decision | Conforms to a pinned schema; does not author schema here. |
| Agriculture domain semantics | `contracts/domains/agriculture/` | Exercises domain meaning; does not replace contracts. |
| Source identity and source role | source-registry and SourceDescriptor authorities | Uses synthetic refs; cannot admit or activate a source. |
| Evidence support | EvidenceRef/EvidenceBundle contracts and proof roots | Models closure; cannot become proof. |
| Policy, rights, sensitivity, and access | `policy/` plus governed review | Supplies test inputs; cannot decide admissibility. |
| Canonical catalog records | `data/catalog/` after governed promotion | Must never be copied here as fixture truth. |
| Tests and assertions | `tests/` | Named consumers establish what each fixture proves. |
| Validator and resolver code | `tools/validators/`, `tools/resolvers/`, or accepted implementation roots | Named consumers read fixtures; code does not belong here. |
| Release, correction, and rollback | `release/` and governed artifact roots | May be modeled; never authorized here. |
| Public API, UI, map, export, graph, search, or AI output | governed released interfaces | Must not read this lane as a normal data source. |

### Anti-collapse rules

Never collapse:

- a fixture into source truth or canonical catalog state;
- schema validity into semantic validity;
- semantic validity into evidence closure;
- evidence closure into policy permission;
- a receipt into proof;
- proof into review or release approval;
- catalog presence into publication;
- aggregate Agriculture data into field, operator, farm, parcel, or living-person truth;
- a proposed ADR into accepted repository behavior;
- a green readiness-hold workflow into implemented enforcement; or
- generated language into an EvidenceBundle or authoritative claim.

---

## Lifecycle boundary

The governed data lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Fixtures sit **outside** this lifecycle. They may model lifecycle states, transitions, or rejection conditions, but they do not enter, advance through, or authorize the lifecycle.

| Fixture operation | Lifecycle effect |
|---|---|
| Add or edit a JSON example | None. |
| Pass JSON Schema validation | None beyond shape evidence for the pinned schema. |
| Pass catalog-closure tests | None beyond bounded enforceability evidence. |
| Link an EvidenceBundle-shaped object | Does not create or approve an EvidenceBundle. |
| Produce an `ALLOW`-shaped expected result | Does not create a PolicyDecision. |
| Produce a release-shaped snapshot | Does not promote, release, publish, sign, or deploy anything. |

Promotion remains a governed state transition. Moving a file out of this lane is never a valid promotion mechanism.

---

## Fixture admission contract

Do not add a payload until every required admission field below is known and reviewable.

| Admission field | Requirement |
|---|---|
| Case ID | Stable, lowercase, descriptive identifier; no personal data or mutable timestamps. |
| Case purpose | One assertion or bounded scenario. |
| Consumer | Exact test module, validator, resolver, or policy-helper path. |
| Invocation | Repository-native command that actually consumes the case. |
| Contract | Exact semantic contract path and pinned version/ref. |
| Schema | Exact `$id`, repository path, draft, and version. |
| Input role | Synthetic input, expected output, snapshot, or expected error. |
| Expected outcome | Finite result such as `PASS`, `FAIL`, `DENY`, `HOLD`, `ABSTAIN`, `QUARANTINE`, `RESTRICT`, or `ERROR`, but only when the consumer defines it. |
| Expected reason | Stable reason code or assertion; do not rely only on fragile prose. |
| Evidence posture | Resolvable synthetic refs, explicit missing-evidence case, or evidence-not-applicable rationale. |
| Source role | Observed, modeled, aggregate, administrative, candidate, context, restricted, or synthetic as defined by the accepted contract. |
| Rights and sensitivity | Public-safe synthetic content; explicit restrictions for negative cases. |
| Lifecycle posture | Candidate state modeled without treating the fixture as lifecycle data. |
| Determinism | Stable ordering, fixed units/CRS/time values, no network, no current-time dependence, and reproducible bytes where required. |
| Correction and rollback | Required expected references for public-facing or release-shaped cases; explicit not-applicable reason otherwise. |

### Minimum review questions

1. Why is this Agriculture-specific rather than a generic `fixtures/data/` case?
2. Which exact executable consumer fails if the fixture is wrong?
3. Which contract and schema define meaning and shape?
4. Does the case preserve source role, evidence, lifecycle, and policy boundaries?
5. Does it contain only synthetic, minimized, public-safe material?
6. Can the expected outcome be checked deterministically without network access?
7. Does the fixture introduce a parallel authority or normalize an unresolved path conflict?
8. What must be updated or reverted when the contract or schema changes?

If any answer is unknown, keep the proposed case in planning documentation rather than adding an unbound payload.

---

## Proposed case matrix

The following matrix is a backlog, not a current inventory. Case names, reason codes, and outcomes must be aligned with the accepted consumer before files are created.

| Proposed case | Expected posture | Assertion |
|---|---|---|
| `minimal_shape_only` | PASS for placeholder shape; HOLD for closure | Demonstrates that `id` alone can satisfy the current permissive schema but cannot establish semantic or evidence closure. |
| `missing_id` | FAIL | Required `id` is absent. |
| `unknown_properties` | PASS for current placeholder shape | Records that `additionalProperties: true` accepts undeclared fields; must not be mislabeled as semantic validation. |
| `unresolved_evidence_ref` | ABSTAIN or HOLD | Consequential evidence cannot be resolved; cite-or-abstain prevents unsupported promotion. |
| `source_role_collapsed` | FAIL or DENY | Modeled, aggregate, administrative, or context material is presented as direct observation or primary support. |
| `receipt_substituted_for_proof` | FAIL | Process memory is incorrectly used as evidence or proof closure. |
| `stac_dcat_prov_disagreement` | DENY or HOLD | Identifier, digest, rights, release reference, or lineage differs across projections after ADR-0022-style agreement is accepted. |
| `raw_or_quarantine_public_candidate` | DENY | A candidate attempts to bypass the trust membrane. |
| `field_operator_parcel_join` | DENY or RESTRICT | Exact or private-adjacent Agriculture linkage is requested without explicit reviewed authority. |
| `aggregate_public_safe` | PASS or ALLOW candidate | Synthetic aggregate metadata meets the accepted evidence, rights, sensitivity, policy, review, and release prerequisites. |
| `missing_release_ref` | HOLD | Public-facing catalog candidate lacks governed release linkage. |
| `missing_correction_or_rollback` | HOLD | Release-shaped candidate lacks correction, supersession, withdrawal, or rollback posture. |
| `spec_hash_mismatch` | FAIL | Deterministic digest does not match canonicalized fixture content after the hash grammar is accepted. |
| `stale_schema_version` | FAIL or migration-required | Fixture declares an unsupported schema version. |
| `network_dependency` | ERROR | The supposed deterministic test attempts external access. |

### Finite outcomes

Use only outcomes defined by the consuming contract or policy. Do not invent a local vocabulary merely to populate fixtures. At minimum, keep these distinctions visible:

| Outcome family | Meaning in a test | Not equivalent to |
|---|---|---|
| `PASS` / `FAIL` | Assertion result. | Policy permission or release approval. |
| `ALLOW` / `DENY` / `RESTRICT` | Expected policy posture when backed by a real policy contract. | Schema validity or publication. |
| `HOLD` / `QUARANTINE` | More evidence, review, correction, or policy work is required. | Permanent denial or successful promotion. |
| `ABSTAIN` | Adequate support is unavailable for the requested claim or scope. | Error or silent success. |
| `ERROR` | Consumer could not produce a governed decision. | Denial, abstention, or test success. |

---

## Proposed layout

No child layout currently exists. After the path and consumer conflicts are resolved, prefer the smallest accepted structure:

```text
fixtures/domains/agriculture/catalog/
  README.md
  valid/
    README.md
    <case-id>.json
  invalid/
    README.md
    <case-id>.json
    <case-id>.expected.json
  denied/
    README.md
    <case-id>.input.json
    <case-id>.expected.json
```

Use `valid/` and `invalid/` only for schema or validator truth. Use `denied/`, `held/`, `abstained/`, or explicit expected-output pairs when policy or resolver outcomes differ from shape validity. A schema-valid denial case belongs with policy-oriented cases, not under `invalid/` merely because publication is denied.

If the accepted topology selects `fixtures/data/catalog_matrix/` or `fixtures/domains/agriculture/catalog_matrix/` instead, migrate or supersede this lane through an explicit reviewed change. Do not populate two live fixture homes.

### Naming rules

- Use lowercase ASCII kebab-case for case IDs unless a repository-wide fixture convention is accepted.
- Keep the same case ID across input, expected result, test parameter, and documentation.
- Do not encode mutable dates, branch names, human names, secrets, or source credentials.
- Prefer semantic names such as `unresolved-evidence-ref` over ordinal names such as `invalid_7`.
- Pair every negative or finite-decision input with a stable expected assertion or result.
- Document whether snapshots compare exact bytes, normalized JSON, selected fields, or reason codes.

---

## Fixture content rules

### Required qualities

Fixtures must be:

- synthetic and public-safe;
- small enough for human review;
- deterministic and no-network;
- pinned to an exact contract and schema version;
- explicit about source role, evidence state, lifecycle state, and expected outcome;
- free of credentials, proprietary source payloads, exact private-field data, and living-person joins;
- stable under timezone, locale, object-ordering, and current-time differences; and
- paired with a real executable consumer.

### Content that does not belong here

- source-system exports, API captures, database dumps, rasters, tiles, or large derived datasets;
- real farm, operator, parcel, private-yield, pesticide, contract, or account records;
- exact restricted or harm-amplifying locations;
- canonical SourceDescriptors, EvidenceBundles, PolicyDecisions, receipts, proofs, catalog records, release manifests, or rollback cards;
- signing material, tokens, credentials, private endpoints, or licensed content whose redistribution is unclear;
- generated claims presented as facts;
- mutable golden files with no regeneration and review contract; or
- payloads that no test, validator, resolver, or policy helper consumes.

### Aggregate-safe default

Agriculture public-facing cases should default to synthetic aggregate metadata. Exact field-level or person-linked cases should normally be negative, denied, restricted, or generalized fixtures unless a separately reviewed policy and test contract explicitly requires a public-safe positive case.

---

## Validation

### What can be checked now

| Check | Command or evidence | Expected result |
|---|---|---|
| JSON syntax for a future case | `python -m json.tool <path-to-fixture>.json >/dev/null` | Syntax only; no semantic conclusion. |
| README structure | Markdown parser/link checks used by the documentation workflow | Documentation quality only. |
| Direct lane inventory | Git tree or repository contents read at a pinned commit | Presence/absence only. |
| Diff hygiene | `git diff --check` in an isolated checkout | Whitespace and conflict-marker hygiene only. |

### Commands that are not substantive proof today

| Surface | Current behavior | Do not claim |
|---|---|---|
| `python tools/validators/domains/agriculture/validate_catalog_matrix.py` | Raises `NotImplementedError`. | CatalogMatrix validity. |
| `python -m pytest tests/domains/agriculture/test_catalog_closure.py -q` | The inspected module contains only a docstring placeholder. | Collected closure coverage. |
| `make fixtures` | Prints `TODO: regenerate deterministic fixtures`. | Fixture generation or freshness. |
| Agriculture CI readiness job | Confirms known placeholder boundaries and records holds. | Validation, proof, release readiness, or publication safety. |

Do not paste these commands into automation as gates until the underlying implementation is reviewed and the expected exit behavior is established.

### Required validation after implementation

When payloads and consumers are introduced, validation should include:

1. JSON/YAML syntax and exact schema validation;
2. semantic contract assertions beyond the permissive placeholder;
3. positive, negative, denial, hold, abstain, restriction, error, correction, and rollback cases as applicable;
4. source-role and EvidenceRef-to-EvidenceBundle closure checks;
5. rights, sensitivity, aggregation, and public-surface policy checks;
6. deterministic identity and digest verification;
7. no-network enforcement;
8. test collection proof showing the intended cases actually ran;
9. workflow wiring with least-privilege permissions and no publication side effects; and
10. remote read-back of the committed fixtures, expected outputs, tests, and validation results.

### Failure interpretation

- A schema failure means the instance does not match the pinned machine shape; it does not decide truth or policy.
- A semantic failure means a contract invariant was violated; it does not automatically identify a policy outcome.
- A policy denial may be the correct passing result for a negative case.
- An abstention is a governed success only when the test expected insufficient evidence and the reason is inspectable.
- An error must not be silently reclassified as denial, abstention, or pass.
- A green workflow that runs only readiness holds is not substantive validation evidence.

---

## Workflow-trigger posture

The scoped README change can trigger repository pull-request workflows. The inspected Agriculture workflow uses `pull_request`, `push` to `main`, and manual dispatch; grants `contents: read`; checks out with persisted credentials disabled; and performs readiness checks with explicit holds. It does not make this lane executable or authorize publication.

Repository-wide workflows may also run on pull requests. Their results are CI evidence only. They do not create an EvidenceBundle, PolicyDecision, PromotionDecision, release approval, or KFM publication event.

No workflow, policy, secret, runner, deployment, release, or environment setting is changed by this README revision.

---

## Maintenance workflow

### Add a case

1. Resolve the accepted CatalogMatrix contract, schema, fixture home, and consumer.
2. Record the case in the admission matrix and select one bounded assertion.
3. Create synthetic input and expected output or error under the accepted layout.
4. Add or update the executable test/validator that consumes the exact path.
5. Run syntax, schema, semantic, policy, sensitivity, evidence, no-network, and collection checks that apply.
6. Record the exact command, outcome, schema version, and relevant artifact hashes.
7. Update the direct inventory and case table in this README.
8. Keep generated-work provenance and human review separate from test success.

### Change a case

Treat a fixture change as a contract-sensitive change when expected semantics change. Explain whether the change corrects bad data, follows a schema version, changes an expected policy outcome, or updates deterministic normalization. Update the consumer and expected result in the same reviewable change.

Do not silently refresh a golden snapshot simply because a test failed.

### Remove or supersede a case

Before removal, search for direct and indirect consumers. Remove or migrate the fixture, expected outputs, parameters, inventory entry, and documentation together. Preserve a migration note when the case encoded a contract version or historically important regression.

---

## Review burden

Reviewers should verify:

- the lane remains fixture-only and public-safe;
- the direct inventory is accurate at the reviewed commit;
- every proposed payload has a real consumer and bounded assertion;
- contract, schema, validator, test, and policy references resolve;
- no parallel CatalogMatrix authority is normalized accidentally;
- source roles and EvidenceBundle requirements remain visible;
- field/operator/parcel/private-data exposure remains fail-closed;
- schema success is not described as catalog closure;
- receipts, proofs, catalogs, manifests, review, release, and publication remain separate;
- fixture and expected-output bytes are deterministic; and
- correction, supersession, withdrawal, and rollback posture is adequate for release-shaped cases.

Human review is required before merge. Fixture or receipt generation cannot self-approve.

---

## Related paths

| Path | Relationship | Current posture |
|---|---|---:|
| [`../README.md`](../README.md) | Parent Agriculture fixture index. | CONFIRMED documentation |
| [`../../../../contracts/data/catalog_matrix.md`](../../../../contracts/data/catalog_matrix.md) | Current generic semantic contract. | CONFIRMED draft |
| [`../../../../schemas/contracts/v1/data/catalog_matrix.schema.json`](../../../../schemas/contracts/v1/data/catalog_matrix.schema.json) | Current generic machine shape. | CONFIRMED placeholder |
| [`../../../../schemas/contracts/v1/domains/agriculture/catalog_matrix.schema.json`](../../../../schemas/contracts/v1/domains/agriculture/catalog_matrix.schema.json) | Current domain-specific machine shape. | CONFIRMED placeholder / topology conflict |
| [`../../../../tools/validators/domains/agriculture/validate_catalog_matrix.py`](../../../../tools/validators/domains/agriculture/validate_catalog_matrix.py) | Declared domain validator implementation. | CONFIRMED placeholder |
| [`../../../../tests/domains/agriculture/test_catalog_closure.py`](../../../../tests/domains/agriculture/test_catalog_closure.py) | Top-level test placeholder. | CONFIRMED docstring-only |
| [`../../../../tests/domains/agriculture/catalog_closure/README.md`](../../../../tests/domains/agriculture/catalog_closure/README.md) | Detailed closure-test design boundary. | CONFIRMED README-only |
| [`../../../../data/catalog/domain/agriculture/README.md`](../../../../data/catalog/domain/agriculture/README.md) | Candidate Agriculture catalog data boundary. | CONFIRMED draft documentation |
| [`../../../../policy/domains/agriculture/README.md`](../../../../policy/domains/agriculture/README.md) | Agriculture policy boundary. | CONFIRMED documentation / runtime NEEDS VERIFICATION |
| [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md) | Architecture-side live Directory Rules artifact. | CONFIRMED live claim in file |
| [`../../../../docs/doctrine/directory-rules.md`](../../../../docs/doctrine/directory-rules.md) | Parallel Directory Rules copy. | CONFIRMED duplicate / placement unresolved |
| [`../../../../docs/registers/DRIFT_REGISTER.md`](../../../../docs/registers/DRIFT_REGISTER.md) | Repository drift register. | CONFIRMED; no new entry required by this doc-only change |
| [`../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md`](../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | Schema-home decision record. | CONFIRMED repository file; status must be read before migration |
| [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | Object-family separation. | CONFIRMED repository file; no authority collapsed here |
| [`../../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md`](../../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md) | Proposed catalog agreement and fixture topology. | CONFIRMED text / PROPOSED decision |

---

## Evidence ledger

| Evidence location | Observation supported | Status and limit |
|---|---|---|
| `main@9a29f659be82af7acbed4a2563ab8f96c1f84046` complete Git tree | Direct lane inventory; related contract, schema, validator, test, workflow, ADR, and Directory Rules paths. | CONFIRMED; snapshot-specific |
| Prior target blob `37fff71f890b67e38303a852d1d97432ad22a4c0` | Previous purpose, authority warnings, proposed `valid/invalid` layout, and maintenance guidance. | CONFIRMED; preserved and expanded |
| `docs/architecture/directory-rules.md` blob `18653c00ba193a4afaa3e07a0924452807fb98ef` | `fixtures/` validate/operate responsibility; file placement as authority; parallel Directory Rules drift. | CONFIRMED doctrine; repository-wide duplicate remains unresolved |
| Supplied `Directory Rules.pdf` | Same responsibility-root, lifecycle, governance, and drift posture used for placement preflight. | CONFIRMED supplied doctrine; not repository implementation proof |
| `docs/registers/DRIFT_REGISTER.md` at the pinned base | Existing recorded drift; no catalog-fixture entry currently needed for a README-only correction. | CONFIRMED; register is not exhaustive proof of no other drift |
| `contracts/data/catalog_matrix.md` blob `c67923beb505aa39e7c0c768c16e75a00826ff31` | Draft CatalogMatrix semantics and separation from evidence, policy, release, and public truth. | CONFIRMED draft; not executable acceptance |
| Generic and domain CatalogMatrix schema blobs | Both require only `id`, allow additional properties, and declare different absent fixture homes. | CONFIRMED placeholders; semantic completeness not established |
| Domain validator blob `177914fce5674ad707448c76225422b1b9d72e12` | `main()` raises `NotImplementedError`. | CONFIRMED placeholder; no validation result |
| Catalog-closure test blob `0ba84246303e04c112a9c403e057fffb36078d12` | Module contains only a `PROPOSED placeholder` docstring. | CONFIRMED placeholder; collection and coverage not established |
| `tests/domains/agriculture/catalog_closure/README.md` | Proposed closure cases, path conflicts, evidence/policy/release boundaries. | CONFIRMED documentation; no executable child test |
| Agriculture workflow blob `1dd9938b92de61c7d905f30170cf6394e6c06ea1` | Pull-request trigger, read-only contents permission, placeholder discovery, explicit validation/proof/release holds. | CONFIRMED readiness scaffold; not substantive proof |
| `Makefile` at the pinned base | `make fixtures` and catalog/release targets remain TODO readiness markers. | CONFIRMED; not executable enforcement |

---

## Open verification register

| Question | Status | Required next evidence |
|---|---:|---|
| Which CatalogMatrix contract/schema pair is canonical? | UNKNOWN / CONFLICTED | Accepted ADR or migration decision plus resolved metadata links. |
| Is this `catalog/` lane retained, migrated, or superseded? | NEEDS VERIFICATION | Directory Rules and ADR-backed fixture topology decision. |
| What stable reason-code vocabulary governs cases? | UNKNOWN | Accepted contract/policy and validator implementation. |
| What exact deterministic identity and `spec_hash` grammar applies? | NEEDS VERIFICATION | Common identity/hash contract plus executable tests. |
| Which consumer owns each case? | UNKNOWN until payload admission | Exact repository path and command. |
| Are EvidenceRef, source-role, rights, sensitivity, and policy resolvers wired? | UNKNOWN | Executable integration tests and receipts/logs. |
| Does CI collect and block on this lane? | NOT ESTABLISHED | Workflow command, test collection evidence, and required-check configuration. |
| Who owns review and governance approval? | CODEOWNERS CONFIRMED / roles NEEDS VERIFICATION | `.github/CODEOWNERS` routes `/fixtures/` to `@bartytime4life`; stewardship assignments and separation of duties remain unresolved. |
| Are any public/API/UI/map/AI consumers permitted to use these fixtures? | NO NORMAL PUBLIC USE; test-only use NEEDS VERIFICATION | Explicit test harness and governed boundary review. |

---

## Correction, removal, and rollback

This README revision is documentation-only. Before merge, rollback is to leave or close the draft pull request; closing or deleting repository objects remains a separate action. After merge, restore the prior README through a transparent revert commit or revert pull request. Do not reset or rewrite shared history.

For future payload changes:

- correct the fixture and its expected result in the same bounded change;
- record whether the correction changes shape, semantics, policy expectation, or only malformed test data;
- update every consumer and inventory entry;
- retain compatibility fixtures when a supported schema version remains active;
- remove orphaned payloads only after consumer search and review; and
- never "promote" a fixture by moving it into a catalog or release root.

Rollback of fixture enforcement does not roll back canonical data or a KFM release because fixtures have no lifecycle or publication authority. If a fixture exposed sensitive or restricted material, remove it through the repository's approved incident/correction path and treat Git history exposure separately; a normal revert does not erase prior Git objects.

---

## Definition of done

This lane is not implementation-complete until all applicable items are satisfied:

- [ ] Governance role assignments are confirmed; the existing GitHub CODEOWNERS route is reviewed for adequate separation of duties.
- [ ] One CatalogMatrix semantic contract and schema/profile topology is accepted.
- [ ] The accepted fixture home is resolved without parallel live authorities.
- [ ] Placeholder schema limitations are addressed or explicitly bounded by semantic validation.
- [ ] The Agriculture catalog validator implements deterministic behavior.
- [ ] Catalog-closure tests are collected and consume the exact fixture paths.
- [ ] Positive and negative shape cases exist.
- [ ] Evidence, source-role, policy, denial, hold, abstain, restriction, error, correction, and rollback cases exist where applicable.
- [ ] Every case has an expected result and stable reason assertion.
- [ ] No-network behavior is enforced.
- [ ] Rights, sensitivity, aggregation, and exact-location/private-join posture are tested fail-closed.
- [ ] CI runs substantive commands and distinguishes readiness holds from enforcement.
- [ ] Remote read-back confirms committed bytes, paths, hashes, tests, and results.
- [ ] Human review is recorded separately from generation and validation.
- [ ] No fixture is represented as source truth, proof, policy approval, release approval, or publication.

Until then, the correct maturity label is **documented boundary / no fixture payloads / implementation not established**.

---

## Last reviewed

- Date: `2026-07-20`
- Repository: `bartytime4life/Kansas-Frontier-Matrix`
- Evidence snapshot: `main@9a29f659be82af7acbed4a2563ab8f96c1f84046`
- Prior target blob: `37fff71f890b67e38303a852d1d97432ad22a4c0`
- Direct payload count: `0`
- Child-directory count: `0`
- Executable validator: `NOT IMPLEMENTED` at the inspected domain path
- Consuming collected tests: `NOT ESTABLISHED`
- Repository-native fixture validation: `NOT RUN / no payloads`
- Release or publication action: `NONE`

[Back to top](#top)
