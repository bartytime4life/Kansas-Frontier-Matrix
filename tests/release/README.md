<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-release-readme
title: tests/release/ — Release Governance Enforceability and Promotion-Safety Boundary
type: readme; directory-readme; release-test-boundary; promotion-safety; correction-and-rollback
version: v0.2
status: draft; repository-grounded; direct-lane-readme-only; pytest-configured; release-schema-harness-present-but-fixture-gated; dedicated-release-suite-not-established; release-policy-stubs; release-tooling-documentation-only; no-network-by-default; fail-closed; non-authoritative
owners: OWNER_TBD — QA steward · Release steward · Promotion steward · Contract steward · Schema steward · Fixture steward · Validator steward · Evidence steward · Policy steward · Correction steward · Rollback steward · CI steward · Security reviewer · Docs steward
created: 2026-07-06
updated: 2026-07-16
supersedes: v0.1 planning-oriented release-test README
policy_label: public-doc; tests; release; promotion; correction; rollback; withdrawal; supersession; synthetic-only; no-network; evidence-aware; policy-aware; review-aware; fail-closed; no-release-authority
current_path: tests/release/README.md
truth_posture: CONFIRMED target README and prior blob, tests responsibility root, release governance root, release contract family, mixed-maturity release schema family, root pytest configuration, Makefile test targets, common schema fixture harness, release fixture parent and PromotionDecision child README lanes, release and promotion policy stubs, release tooling and release-validator README-only maturity, selected workflow definitions, proposed promotion-gate ADR status, and bounded repository search that did not establish a direct executable under tests/release / PROPOSED dedicated release-governance tests, fixture-consumer contracts, A-G gate mapping, no-network release test target, coverage manifest, CI artifact, promotion dependency, and maturity ladder / CONFLICTED release fixture parent-child documentation freshness and fixture homes used by schema versus release-behavior tests / UNKNOWN exhaustive recursive direct-lane inventory, fixture payload inventory, dynamic test generation, ignored files, current collected cases, current pass rates, branch-protection requirements, release runtime behavior, emitted receipts, and production promotion behavior / NEEDS VERIFICATION accepted owners, CODEOWNERS, direct test runner, actual release fixture payloads, schema-to-fixture coverage, validator implementations, policy bundle implementations, CI path filters, required checks, correction consumers, and rollback drill execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 04e9cbac69305a5d708509ceef62c6f43ca1f41c
  target_prior_blob: 011984d8e32031d07d1e4590d8ced348b1ab206f
  direct_lane_files_confirmed:
    - tests/release/README.md
  bounded_inventory_note: connector code search did not establish a direct executable test under tests/release; this does not prove permanent absence from history, other refs, ignored files, generated workspaces, dynamic test generation, or uninspected paths
related:
  - ../README.md
  - ../schemas/README.md
  - ../contracts/README.md
  - ../schemas/test_common_contracts.py
  - ../../release/README.md
  - ../../contracts/release/README.md
  - ../../schemas/contracts/v1/release/README.md
  - ../../fixtures/release/README.md
  - ../../fixtures/contracts/v1/README.md
  - ../../tools/release/README.md
  - ../../tools/validators/release/README.md
  - ../../policy/release/README.md
  - ../../policy/promotion/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0018-promotion-gate-sequence.md
  - ../../Makefile
  - ../../pyproject.toml
  - ../../.github/workflows/contracts-validate.yml
  - ../../.github/workflows/schema-validation.yml
  - ../../.github/workflows/validator-suite.yml
  - ../../.github/workflows/policy-boundary-guards.yml
tags: [kfm, tests, release, promotion, ReleaseManifest, PromotionDecision, RollbackCard, CorrectionNotice, WithdrawalNotice, fixtures, pytest, no-network, fail-closed, correction, rollback, CI, trust-spine]
notes:
  - "v0.2 replaces a planning-oriented README with a repository-grounded release-test boundary and current maturity assessment."
  - "The direct tests/release lane is README-only in the bounded snapshot; no dedicated executable release test module was established."
  - "The generic schema fixture harness names the release family but only creates a case when fixtures/contracts/v1/release/<schema_name>/ exists; the fixture parent records release schema-fixture coverage as unresolved."
  - "fixtures/release/ documents synthetic release-governance examples and PromotionDecision sublanes, but its own payload inventory was not verified and child READMEs contain stale parent-not-found statements."
  - "make test executes tests/schemas and tests/contracts only; it does not directly execute tests/release."
  - "policy/release and policy/promotion are greenfield stubs; tools/release and tools/validators/release are documentation boundaries without confirmed executables."
  - "This revision changes documentation only and creates no test, fixture, schema, contract, validator, policy, workflow, release record, receipt, proof, lifecycle artifact, or public output."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/release/` — Release Governance Enforceability and Promotion-Safety Boundary

> **Purpose.** Define the executable proof boundary for KFM release governance: candidates must not become releases by naming, placement, merge, deployment, schema validity, fixture success, tool output, or generated prose. A mature suite must prove that evidence, validation, policy, review, promotion, manifest, correction, withdrawal, supersession, and rollback requirements fail closed and remain auditable.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Direct inventory: README only" src="https://img.shields.io/badge/direct__inventory-README__only-lightgrey">
  <img alt="Runner: pytest configured" src="https://img.shields.io/badge/runner-pytest__configured-blue">
  <img alt="Dedicated suite: not established" src="https://img.shields.io/badge/dedicated__suite-not__established-orange">
  <img alt="Fixture coverage: unresolved" src="https://img.shields.io/badge/fixture__coverage-UNRESOLVED-red">
  <img alt="Failure posture: fail closed" src="https://img.shields.io/badge/failure-fail__closed-critical">
  <img alt="Authority: tests only" src="https://img.shields.io/badge/authority-tests__only-purple">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose-and-audience) · [Authority](#authority-and-repository-fit) · [Current state](#confirmed-current-state) · [Scope](#test-scope-and-non-scope) · [Outcomes](#finite-outcome-vocabulary) · [Fixtures](#fixture-and-test-data-contract) · [Test model](#release-governance-test-model) · [Gates](#promotion-gate-coverage) · [Execution](#deterministic-execution-and-no-network-posture) · [CI](#ci-and-promotion-boundary) · [Failures](#failure-interpretation) · [Passing](#what-a-passing-suite-does-not-prove) · [Maintenance](#maintenance-and-fixture-update-rules) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [Rollback](#documentation-correction-and-rollback)

---

## Status and evidence boundary

> [!IMPORTANT]
> **CONFIRMED direct lane:** the bounded repository snapshot establishes `tests/release/README.md` but did not establish a direct `test_*.py` or equivalent executable under `tests/release/`.
>
> **CONFIRMED adjacent execution:** the repository configures pytest, and `tests/schemas/test_common_contracts.py` can include the `release` schema family when a matching fixture directory exists.
>
> **NOT established:** a dedicated release-governance suite, confirmed release fixture payload inventory, release policy implementation, release validator implementation, release dry-run implementation, release-specific CI artifact, or promotion-blocking required check.

### Safe conclusion

`tests/release/` is the correct cross-cutting test boundary for release governance, but the direct lane remains documentation-only in the checked snapshot. Existing adjacent machinery provides a partial foundation, not a release suite:

- `pyproject.toml` configures Python 3.11+, pytest as a test extra, and the repository root on `pythonpath`.
- `make test` runs `tests/schemas` and `tests/contracts`; it does **not** directly run `tests/release`.
- `tests/schemas/test_common_contracts.py` names `release` in its hard-coded family list, but it creates a test case only when `fixtures/contracts/v1/release/<schema_name>/` exists.
- `fixtures/contracts/v1/README.md` records release schema-fixture coverage as `NEEDS VERIFICATION`.
- `fixtures/release/README.md` documents a synthetic release-governance fixture parent and PromotionDecision child lanes, but it did not verify payload files.
- `policy/release/README.md` and `policy/promotion/README.md` are greenfield stubs.
- `tools/release/README.md` and `tools/validators/release/README.md` document intended boundaries, while executable behavior remains verification-bound.
- `schemas/contracts/v1/release/README.md` records a mixed-maturity schema family: one concrete PromotionDecision schema, several permissive stubs, and several empty scaffolds.

### Truth labels used here

| Label | Meaning in this README |
|---|---|
| `CONFIRMED` | Verified from repository files or bounded connector search at the pinned snapshot. |
| `PROPOSED` | A recommended test, fixture, command, gate, artifact, or path relationship not established as current implementation. |
| `UNKNOWN` | Not resolved by inspected evidence. |
| `NEEDS VERIFICATION` | Checkable, but not sufficiently verified to act as fact. |
| `CONFLICTED` | Repository documents disagree or carry stale relationship claims; no silent winner is selected. |
| `DENY` | A prohibited release or authority interpretation. |

[Back to top](#top)

---

## Purpose and audience

`tests/release/` should prove that KFM release governance is enforceable across the transition from release candidate to governed public state and through later correction, withdrawal, supersession, or rollback.

This README is for:

- QA and test stewards;
- release and promotion stewards;
- schema, contract, policy, evidence, receipt, proof, correction, and rollback owners;
- domain-lane maintainers who need cross-cutting release behavior;
- CI maintainers deciding which checks may support promotion;
- reviewers evaluating whether a passing result has enough scope to matter.

The durable test question is:

> Can the repository demonstrate, with deterministic and public-safe evidence, that a release transition is explicit, supported, reviewable, fail-closed, correctable, and reversible without treating tests as release authority?

A mature suite should expose both positive and negative behavior. It should make unsupported release claims fail visibly rather than disappear through skipped discovery, empty fixture sets, permissive schemas, TODO tooling, or undocumented CI behavior.

[Back to top](#top)

---

## Authority and repository fit

Directory Rules place enforceability proof under `tests/` and release governance under `release/`. The current path is therefore correctly placed and requires no move or new ADR.

| Responsibility | Authority home | Role of `tests/release/` |
|---|---|---|
| Release governance records and decisions | `release/` | Assert required behavior; never create or store authoritative release records. |
| Release object meaning | `contracts/release/` and adjacent correction contracts | Test semantic invariants; never redefine them here. |
| Release object machine shape | `schemas/contracts/v1/release/` and accepted adjacent schema families | Validate selected shapes; never become schema authority. |
| Release and promotion policy | `policy/release/`, `policy/promotion/`, and accepted policy roots | Exercise policy behavior; never author or infer policy. |
| Synthetic release examples | `fixtures/release/` | Consume behavior-oriented fixtures when confirmed and linked. |
| Schema fixture examples | `fixtures/contracts/v1/release/<schema_name>/` | Consume shape fixtures through the schema harness when present. |
| Release-support tooling | `tools/release/` | Test deterministic helpers when implemented. |
| Release validation routing | `tools/validators/release/` and specialized validator lanes | Exercise validator behavior when implemented. |
| Evidence, proofs, and receipts | `data/proofs/`, `data/receipts/`, and accepted evidence homes | Use synthetic references and assert closure; never store trust artifacts here. |
| Published public-safe carriers | `data/published/` and governed delivery roots | Assert public-boundary controls; never store published payloads here. |
| Release enforceability proof | `tests/release/` | This lane. |

> [!WARNING]
> A passing test, green workflow, valid schema, generated report, merged pull request, copied file, deployed artifact, public URL, map layer, or AI answer is **not** a release decision. Only governed release records and the required supporting evidence, policy, review, manifest, correction, and rollback state can support that conclusion.

### Placement prohibitions

Do not use this lane as:

- a second release record store;
- a release manifest registry;
- a schema, contract, policy, fixture, source, receipt, proof, catalog, or lifecycle data authority;
- a public artifact or export store;
- a place to hide validator or release implementation logic;
- a shortcut around review, separation of duties, correction, or rollback;
- a normal public-client path into RAW, WORK, QUARANTINE, candidate, canonical, or internal stores.

[Back to top](#top)

---

## Confirmed current state

### Direct lane inventory

| Surface | Status | Evidence-bounded conclusion |
|---|---:|---|
| `tests/release/README.md` | `CONFIRMED` | Existing v0.1 planning README; this revision replaces it. |
| Direct executable test module | `NOT ESTABLISHED` | Bounded code search did not establish a direct executable under `tests/release/`. |
| Direct test-local fixtures | `NOT ESTABLISHED` | No test-local fixture inventory was established for this lane. |
| Dedicated runner or marker | `NOT ESTABLISHED` | No lane-specific pytest marker, Make target, or runner was verified. |
| Dedicated CI workflow or artifact | `NOT ESTABLISHED` | No release-test workflow or release-test report artifact was verified. |

The bounded search limit matters: absence from search results is not proof of permanent nonexistence across history, other refs, ignored files, generated workspaces, or dynamic test generation.

### Repository-native test execution

| Surface | Confirmed behavior | Release-lane consequence |
|---|---|---|
| `pyproject.toml` | Python `>=3.11`; pytest test extra; root `pythonpath`. | Pytest is the grounded repository runner family. |
| `make test` | Runs `python -m pytest tests/schemas tests/contracts -q`. | Direct `tests/release/` coverage is excluded. |
| `make schemas` | Runs `python tools/validators/_common/run_all.py`. | Runs an aggregate validator path, not a dedicated release suite. |
| `make release-dry-run` | Emits a TODO message. | No release dry-run implementation is established. |
| `make publish-check` | Emits a TODO message. | No promotion-gate implementation is established by this target. |
| `make deny-test` | Emits a TODO message. | No release/public-boundary deny suite is established by this target. |

### Adjacent schema coverage

`tests/schemas/test_common_contracts.py`:

1. scans immediate `*.schema.json` files in seven hard-coded families, including `release`;
2. derives `fixtures/contracts/v1/<family>/<schema_name>/`;
3. silently omits a schema when that fixture directory does not exist;
4. accepts `valid/valid_*.json` only when no schema errors occur;
5. accepts `invalid/invalid_*.json` only when at least one schema error occurs;
6. optionally checks expected error text.

That harness is relevant but insufficient for release governance. It does not by itself prove:

- release semantic completeness;
- evidence resolution;
- policy or rights evaluation;
- review or separation of duties;
- receipt/proof closure;
- correction, withdrawal, supersession, or rollback behavior;
- public-boundary denial;
- release runtime integration;
- actual promotion or publication.

### Release fixture surfaces

Two fixture responsibilities are present and must not be collapsed:

| Fixture home | Intended role | Current evidence |
|---|---|---|
| `fixtures/contracts/v1/release/<schema_name>/` | Shape fixtures consumed by the generic schema harness. | Parent fixture README records release coverage as unresolved. |
| `fixtures/release/` | Synthetic release-governance behavior examples and PromotionDecision child lanes. | Parent and child READMEs exist; payload inventory was not verified. |

There is a documentation freshness conflict: `fixtures/release/README.md` now exists, but older PromotionDecision child READMEs still state that the parent was not found. Treat this as `CONFLICTED / NEEDS VERIFICATION`; do not infer payload or consumer maturity from README hierarchy alone.

### Release contract and schema maturity

| Family | Current documented maturity | Test implication |
|---|---|---|
| `PromotionDecision` | Semantic contract present; schema described as concrete and closed. | First credible shape/semantic thin slice, but policy/review/runtime behavior remains unproven. |
| `ReleaseManifest` | Semantic contract present; schema described as permissive. | Do not treat schema validity as manifest completeness. |
| `RollbackCard` | Semantic scaffold; permissive schema. | Rollback-readiness tests must remain proposed until fields/validator are accepted. |
| `WithdrawalNotice` | Semantic scaffold; permissive schema. | Withdrawal tests need accepted meaning and negative fixtures. |
| `ReleaseState` | Empty permissive schema scaffold. | Documented release-state vocabulary is not proven schema-enforced. |
| `CorrectionNotice` | Adjacent semantic contract; empty release-family schema scaffold and placement seam. | Correction tests must expose the seam instead of hiding it. |
| `RedactionReceipt` and `PublicationTransformReceipt` | Receipt-like release schema scaffolds. | Receipt-family placement and semantics need explicit migration/profile decisions. |

### Policy, validator, and tooling maturity

- `policy/release/README.md` is a greenfield stub.
- `policy/promotion/README.md` is a greenfield stub.
- `tools/release/README.md` defines support-only tooling expectations but confirms no executable helper.
- `tools/validators/release/README.md` defines routing expectations but confirms no executable release validator.
- `ADR-0018` proposes a canonical Promotion Gates A–G sequence; its status is `proposed`, so the sequence must not be presented as accepted implementation.

### Workflow posture

| Workflow | Trigger/command | What it establishes | What it does not establish |
|---|---|---|---|
| `contracts-validate.yml` | `push`, `pull_request`; installs `.[test]`; runs `make test`. | Schema and contract directories are part of a repo workflow path. | Direct `tests/release/` execution, release semantic coverage, or release gate status. |
| `schema-validation.yml` | Pull request and push to `main`; runs `make schemas`. | Aggregate validators run in CI. | Direct release tests or complete release schema coverage. |
| `validator-suite.yml` | Pull request and push to `main`; runs `make schemas` and one evidence fail-closed check. | Some fail-closed validation is exercised. | Release policy, promotion gates, rollback, correction, or release runtime. |
| `policy-boundary-guards.yml` | Path-filtered pull request plus manual dispatch; runs boundary tests. | Selected policy and trust-membrane guards exist. | A change only to `tests/release/README.md` is not in its inspected path filter. |

[Back to top](#top)

---

## Test scope and non-scope

### In scope

A mature cross-cutting release suite should test:

- candidate-versus-release separation;
- `ReleaseManifest` required structure and dependency closure;
- `PromotionDecision` finite release-transition vocabulary and support refs;
- evidence, proof, receipt, validation, policy, review, signature, correction, and rollback references;
- lifecycle transition rules from CATALOG/TRIPLET toward PUBLISHED;
- hold, deny, abstain, error, correction, withdrawal, supersession, and rollback paths;
- separation of ReleaseManifest, PromotionDecision, PolicyDecision, ReviewRecord, EvidenceBundle, RunReceipt, ProofPack, CorrectionNotice, WithdrawalNotice, and RollbackCard responsibilities;
- public-boundary denial for unreleased, stale, withdrawn, or superseded material;
- no-network and deterministic fixture behavior;
- report and receipt accuracy when a validator or test runner emits governed test evidence;
- no-op behavior when the requested release state already exists and is valid;
- correction and rollback propagation to downstream APIs, maps, exports, and bounded AI surfaces when those consumers are implemented.

### Out of scope

This lane must not:

- author or approve real release records;
- publish or copy artifacts into public paths;
- implement release policy inside test code;
- redefine schemas or semantic contracts;
- store production EvidenceBundles, proofs, receipts, signatures, release manifests, correction notices, rollback cards, or reviewer identities;
- use real sensitive source material or exact protected locations;
- require live network access in the default tier;
- treat fixture success, schema validity, validator output, or CI success as public truth;
- merge, deploy, sign, release, correct, withdraw, supersede, or roll back production state;
- silently skip unsupported categories and count the omission as success.

[Back to top](#top)

---

## Finite outcome vocabulary

Release tests must keep three vocabularies separate.

### Test execution outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The asserted test condition is supported by the tested inputs and harness. |
| `FAIL` | A required invariant was violated. |
| `ABSTAIN` | Required evidence, policy, schema, contract, or fixture context is unavailable or ambiguous. |
| `SKIP_EXPLICIT` | The category is intentionally inapplicable, with a recorded reason and owner. |
| `ERROR` | Test infrastructure failed; no release conclusion is valid. |

### Release-transition decision vocabulary

The current PromotionDecision fixture documentation uses:

| Outcome | Meaning |
|---|---|
| `APPROVE` | The tested decision object records approval for the scoped transition; it is not publication by itself. |
| `DENY` | The transition is refused and prior state remains. |
| `ABSTAIN` | The decision cannot safely authorize or deny because context is insufficient, stale, unresolved, conflicted, or unsafe. |

### Documented release states

`release/README.md` documents states including `DRAFT`, `READY_FOR_REVIEW`, `HELD`, `READY_FOR_MANIFEST`, `APPROVED`, `RELEASED`, `CORRECTED`, `SUPERSEDED`, `WITHDRAWN`, and `NO_ACTION`.

These are documented release-root vocabulary, not confirmed schema enforcement. Tests must not conflate them with runtime response outcomes such as `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`.

> [!CAUTION]
> The same word may appear in more than one vocabulary. Always bind an outcome to its object family, schema/contract version, tested operation, and evidence scope.

[Back to top](#top)

---

## Fixture and test data contract

### Fixture families required for credible coverage

| Family | Purpose | Minimum expected posture |
|---|---|---|
| Valid | Complete public-safe positive path. | `PASS`; never implies real release. |
| Invalid | Malformed or semantically unsupported object. | `FAIL`. |
| Denied | Rights, sensitivity, access, policy, or public-boundary refusal. | `DENY` or test `PASS` proving denial. |
| Abstained | Missing, stale, unresolved, conflicted, or insufficient evidence/context. | `ABSTAIN`. |
| Held/quarantined | Candidate remains before release because gates or review are incomplete. | `HELD`, quarantine/hold reason, or test `PASS` proving block. |
| Error | Validator, resolver, signature, digest, or test infrastructure failure. | `ERROR`; no unsafe fallback. |
| Correction | Existing released state requires a visible correction. | `CORRECTED` or test `PASS` proving correction path. |
| Withdrawal | Release must become unavailable with audit history preserved. | `WITHDRAWN`. |
| Supersession | A newer governed record replaces an older state without silent mutation. | `SUPERSEDED`. |
| Rollback | Prior release target and reversal instructions are resolvable. | Rollback-readiness `PASS`; not proof rollback executed. |
| No action | Evaluation produces no authorized change. | `NO_ACTION`; no empty release mutation. |

### Fixture home rules

Use the primary responsibility to choose the fixture home:

```text
fixtures/contracts/v1/release/<schema_name>/
  valid/valid_*.json
  invalid/invalid_*.json
  invalid/invalid_*.expected_error.txt

fixtures/release/
  promotion_decision/
    valid/
    invalid/
  <future release-behavior families only after placement and consumer review>
```

- Shape fixtures for the common schema harness belong under `fixtures/contracts/v1/release/`.
- Cross-cutting behavior fixtures may belong under `fixtures/release/` when they are synthetic, deterministic, public-safe, and linked to a consumer.
- Domain-specific release fixtures belong under the applicable `fixtures/domains/<domain>/` lane when the primary concern is domain release behavior.
- Avoid `tests/release/fixtures/` unless an accepted test-local fixture convention explicitly owns those examples.
- Do not duplicate the same authoritative fixture across homes. Use pointers, profiles, or a migration note.

### Required fixture metadata or companion documentation

Each stable fixture should identify, directly or through an accepted manifest:

- fixture ID and scenario family;
- input object family and version;
- semantic contract reference;
- schema reference when applicable;
- expected test and release-transition outcomes;
- evidence/policy/review/rollback assumptions;
- rights and sensitivity posture;
- whether the example is valid, invalid, denied, abstained, held, corrected, withdrawn, superseded, rollback-ready, or error-inducing;
- consumer test or validator path;
- correction/supersession lineage when a fixture changes.

### Rights and sensitivity posture

All default fixtures must be synthetic and public-safe.

Do not include:

- real living-person identifiers;
- DNA/genomic data;
- exact archaeology or rare-species locations;
- exact sensitive infrastructure locations or configurations;
- private landowner-sensitive joins;
- secrets, access tokens, credentials, signatures, or private keys;
- unreleased source-system exports;
- real reviewer identities or private review notes;
- proprietary payloads without explicit test rights.

When a sensitive-domain behavior must be tested, use a transformed toy fixture that proves denial, redaction, generalization, withheld fields, staged access, or restricted review without preserving real sensitive detail.

[Back to top](#top)

---

## Release-governance test model

A cross-cutting release test should evaluate an explicit packet rather than infer state from directories.

```text
release candidate
  -> contract and schema posture
  -> evidence and provenance support
  -> validation results
  -> policy and rights/sensitivity decision
  -> review and separation-of-duties state
  -> promotion decision
  -> release manifest readiness
  -> receipt/proof/signature support
  -> correction and rollback readiness
  -> public-boundary decision
  -> finite test result
```

### Proposed test packet

The following is a design aid, not a repository schema:

```text
ReleaseTestCase {
  case_id
  scenario_family
  candidate_ref
  contract_refs[]
  schema_refs[]
  fixture_refs[]
  evidence_refs[]
  validation_refs[]
  policy_refs[]
  review_refs[]
  promotion_decision_ref
  release_manifest_ref
  receipt_refs[]
  proof_refs[]
  rollback_ref
  correction_ref
  withdrawal_ref
  supersedes_ref
  expected_test_outcome
  expected_release_state
  public_surface_expectation
}
```

### Required validation layers

| Layer | Question | Failure posture |
|---|---|---|
| Shape | Does the object conform to an accepted schema version? | `FAIL` or `ABSTAIN`; never auto-release. |
| Semantics | Does the object mean what its contract says and preserve non-ownership? | `FAIL`. |
| Identity | Are IDs, versions, refs, hashes, and supersession links stable and resolvable? | `FAIL` or `ABSTAIN`. |
| Evidence | Do release-visible claims resolve through EvidenceRef to admissible support? | `ABSTAIN` or `DENY`. |
| Validation | Are required validator results present, current, scoped, and successful? | `HELD`, `FAIL`, or `ERROR`. |
| Policy | Are rights, sensitivity, access, public-surface, and obligations evaluated? | `DENY`, `ABSTAIN`, or `ERROR`. |
| Review | Is required human review bound to the candidate and decision? | `HELD`. |
| Separation of duties | Are policy-significant release roles separated where required? | `HELD` or `DENY`. |
| Provenance/receipt | Do receipts describe what actually ran and bind relevant inputs/outputs? | `FAIL`, `ABSTAIN`, or `ERROR`. |
| Manifest | Does the manifest bind the intended artifact set and required support refs? | `HELD` or `FAIL`. |
| Integrity/signature | Do required digests/signatures verify against pinned content? | `DENY` or `ERROR`. |
| Correction/rollback | Can the release be corrected, withdrawn, superseded, or rolled back visibly? | `HELD` or `FAIL`. |
| Public boundary | Are unreleased, stale, withdrawn, superseded, or sensitive carriers denied? | `DENY`; boundary failure is critical. |

### Required negative assertions

At minimum, future tests should prove:

- a candidate is not a release;
- a review is not approval;
- schema validity is not release readiness;
- a PromotionDecision is not a ReleaseManifest;
- a ReleaseManifest is not EvidenceBundle or policy approval;
- a merged pull request is not KFM publication;
- a copied file is not promotion;
- a generated tile, export, screenshot, graph, or AI answer is not release authority;
- missing evidence does not become an invented claim;
- unknown rights or sensitivity does not default allow;
- missing review does not auto-approve;
- missing rollback support does not silently pass;
- stale or withdrawn material does not remain public-active;
- a test infrastructure error does not fall back to `PASS`;
- zero discovered fixtures or zero collected tests does not count as coverage.

[Back to top](#top)

---

## Promotion gate coverage

`ADR-0018-promotion-gate-sequence.md` is currently `proposed`. Its A–G sequence is useful as a future test organization, but it is not accepted implementation evidence.

### Proposed A–G mapping

| Proposed gate | Proposed outcome name | Release-test responsibility |
|:---:|---|---|
| A | `schema_valid` | Positive/negative schema cases; no unknown enum values; deterministic spec/hash checks where accepted. |
| B | `inputs_pinned` | Source, artifact, version, digest, rights, and license inputs are explicit and resolvable. |
| C | `checks_pass` | Required validators and domain-quality checks run and report bounded results. |
| D | `signatures_valid` | Required receipt/signature/attestation checks fail closed on missing or mismatched support. |
| E | `provenance_complete` | Evidence and provenance closure, supersession, and rollback refs resolve. |
| F | `no_policy_violations` | Policy returns a finite outcome; obligations and human-review holds are visible. |
| G | `release_ready` | Manifest candidate, catalog/proof closure level, rollback target, public DTO, and unresolved holds are checked. |

Tests must preserve these caveats:

- The ADR is proposed, so names and exact mapping remain `PROPOSED` until accepted.
- Gate success supports a PromotionReceipt or release review; it is not publication by itself.
- A missing gate result is a failure or hold, not implicit success.
- Gate H Merkle integrity and Gate I ReleaseManifest closure are explicitly outside that ADR and must not be silently claimed.
- Per-domain tests may strengthen checks inside a gate but must not invent competing gate authority.

[Back to top](#top)

---

## Suggested test families and future layout

The direct lane should remain small and cross-cutting. Domain-specific release behavior belongs under domain test lanes.

```text
tests/release/
|-- README.md
|-- test_candidate_is_not_release.py                 # PROPOSED
|-- test_release_manifest_closure.py                 # PROPOSED
|-- test_promotion_decision_boundary.py              # PROPOSED
|-- test_policy_review_and_hold_states.py            # PROPOSED
|-- test_receipt_proof_and_signature_links.py        # PROPOSED
|-- test_correction_withdrawal_supersession.py       # PROPOSED
|-- test_rollback_readiness.py                       # PROPOSED
|-- test_public_surface_denial.py                    # PROPOSED
`-- test_release_coverage_manifest.py                # PROPOSED; fail on zero/unknown coverage
```

This layout is intentionally proposed. Do not create empty placeholder tests merely to make the tree look complete.

### Cross-cutting versus domain test ownership

| Primary assertion | Preferred test home |
|---|---|
| Universal release object separation and finite outcomes | `tests/release/` |
| Generic release schema shape | `tests/schemas/` with `fixtures/contracts/v1/release/` |
| Semantic contract text and link discipline | `tests/contracts/` |
| Release/promotion policy behavior | `tests/policy/` and/or `tests/release/` depending on primary assertion |
| Domain-specific release manifest behavior | `tests/domains/<domain>/...` |
| Domain-specific sensitive geometry/publication denial | `tests/domains/<domain>/...` with policy/security review |
| Release tooling helper behavior | `tests/release/` when cross-cutting; package/tool tests when implementation-local |
| Governed API/UI release-state rendering | API/UI/e2e lanes with release fixtures and explicit trust-boundary assertions |

[Back to top](#top)

---

## Deterministic execution and no-network posture

### Confirmed commands

These commands are grounded in current repository tooling:

```bash
# Current aggregate test target; does not directly execute tests/release.
make test

# Equivalent confirmed command from the Makefile.
python -m pytest tests/schemas tests/contracts -q

# Directly inspect the generic schema fixture harness.
python -m pytest tests/schemas/test_common_contracts.py -q

# Current aggregate schema-validator target; not a dedicated release suite.
make schemas
```

### Proposed direct command after executable tests exist

```bash
# PROPOSED — do not treat as a working release suite until test modules are added.
python -m pytest tests/release -q
```

Until at least one direct executable test is present, a command targeting only `tests/release/` may collect zero tests. Zero collection must not be reported as release coverage.

### No-network default

The default release suite must:

- use only repository-local synthetic fixtures;
- freeze or control time where time affects outcomes;
- avoid live APIs, artifact registries, transparency logs, signing services, model endpoints, tile servers, source systems, or public sites;
- avoid ambient credentials and user-specific environment state;
- use deterministic IDs, hashes, timestamps, and expected outputs where practical;
- write temporary outputs only to isolated test directories;
- clean up after itself;
- produce the same semantic outcome from the same pinned inputs.

### Separate live tier

Live integration checks may exist only as an explicitly separate tier with:

- an opt-in marker or workflow;
- least-privilege credentials;
- explicit host allowlist;
- timeout, retry, rate-limit, and circuit-breaker behavior;
- no production mutation by default;
- no release or publication side effect;
- redacted logs and artifacts;
- clear ownership and retention;
- a statement that live availability does not prove release correctness.

[Back to top](#top)

---

## CI and promotion boundary

### Current CI conclusion

The inspected workflows do not establish a release-test gate:

- `contracts-validate` runs `make test`, which excludes the direct release lane.
- `schema-validation` and `validator-suite` run `make schemas`, not `pytest tests/release`.
- `policy-boundary-guards` does not include `tests/release/**` in its inspected pull-request path filter.
- Current pass rates, branch-protection requirements, required-check configuration, and promotion dependency are `UNKNOWN`.

### Proposed mature CI contract

A future release-test job should:

1. install pinned test dependencies;
2. run a dedicated deterministic release suite;
3. fail if zero direct release tests are collected;
4. fail if required fixture families are absent or unconsumed;
5. report schema, semantic, evidence, policy, review, receipt/proof, correction, rollback, and public-boundary coverage separately;
6. distinguish test failures from infrastructure errors and explicit skips;
7. emit a machine-readable report with repository SHA, test command, collected count, passed/failed/skipped/error counts, fixture manifest digest, and coverage gaps;
8. upload only public-safe artifacts;
9. avoid release mutation and publication side effects;
10. remain support for promotion review, not release approval.

### Proposed coverage report fields

```json
{
  "suite": "tests/release",
  "repository_sha": "<commit>",
  "command": "python -m pytest tests/release -q",
  "collected": 0,
  "passed": 0,
  "failed": 0,
  "skipped_explicit": 0,
  "errors": 0,
  "fixture_manifest_sha256": "<digest-or-null>",
  "layers": {
    "shape": "NOT_RUN",
    "semantics": "NOT_RUN",
    "evidence": "NOT_RUN",
    "policy": "NOT_RUN",
    "review": "NOT_RUN",
    "receipts_and_proofs": "NOT_RUN",
    "correction_and_rollback": "NOT_RUN",
    "public_boundary": "NOT_RUN"
  },
  "release_decision_created": false,
  "publication_created": false
}
```

The example is proposed. `collected: 0` must be a failing coverage state, not a green result.

### Workflow-trigger safety for this README change

A documentation-only edit to this path may trigger broad pull-request workflows, but the inspected target-specific path does not trigger a privileged release or deployment action. Do not manually dispatch release, signing, publication, rollback, or environment workflows merely to validate this README.

[Back to top](#top)

---

## Failure interpretation

| Signal | Safe interpretation | Unsafe interpretation |
|---|---|---|
| Schema test fails | The tested object does not meet the selected machine-shape expectation. | The source claim is false or the release must be withdrawn automatically. |
| Contract test fails | The documented semantic boundary is incomplete or inconsistent. | The schema or policy must be rewritten without review. |
| Evidence test abstains | Required support could not be resolved for the tested case. | Treat missing evidence as approval. |
| Policy test denies | The tested action is blocked under the selected policy inputs. | The data must be deleted or the denial applies beyond its scope. |
| Review test holds | Required review binding is missing or incomplete. | A developer or test runner may self-approve. |
| Signature/digest test fails | Required integrity support is missing or mismatched. | Ignore the failure because the artifact renders. |
| Rollback test fails | The tested release lacks a verified reversal path. | Publish now and document rollback later. |
| Public-boundary test fails | Unreleased or unsafe material may be exposed. | Downgrade to a warning. |
| Test infrastructure errors | No release conclusion is valid. | Fall back to pass or continue promotion. |
| Zero tests collected | Coverage is absent. | Treat process exit or empty output as success. |
| Explicit skip | The category was knowingly not run with a reason. | Count the category as covered. |

Failure routing should be finite and reviewable: fix the test or implementation, add missing evidence, hold the candidate, deny the transition, quarantine affected material, narrow scope, or record an explicit abstention. Do not patch around trust-spine failures with direct publication or admin shortcuts.

[Back to top](#top)

---

## What a passing suite does not prove

Even a comprehensive green release suite does **not** prove:

- that a source claim is true;
- that evidence is authoritative outside its declared role;
- that current rights or terms permit publication;
- that sensitivity review is complete for every audience;
- that human review actually occurred unless the reviewed record is verified;
- that a signature identity is authorized merely because cryptography verifies;
- that a ReleaseManifest contains every relevant artifact unless closure is checked;
- that rollback has been executed successfully merely because a RollbackCard validates;
- that downstream API/UI/map/AI surfaces enforce release state unless those consumers are tested;
- that a workflow is required by branch protection;
- that production deployment, publication, correction, withdrawal, supersession, or rollback occurred;
- that untested domains or fixture categories are safe;
- that future changes preserve behavior;
- that KFM publication authority has been granted.

A passing suite is enforceability evidence within a defined scope. It is never sovereign truth or release authority.

[Back to top](#top)

---

## Maintenance and fixture-update rules

### When tests change

Update this README, the relevant fixture indexes, and CI documentation when:

- a direct release test module is added, renamed, split, or retired;
- the runner, marker, Make target, or workflow changes;
- a release object family becomes accepted, deprecated, superseded, or migrated;
- fixture discovery or naming changes;
- release policy or promotion policy becomes executable;
- a validator or release-support tool becomes executable;
- an A–G gate ADR is accepted, superseded, or rejected;
- correction, withdrawal, supersession, rollback, signature, or receipt requirements change;
- a public consumer starts relying on release test evidence;
- a fixture contains sensitive or rights-restricted material;
- a coverage gap is closed or newly discovered.

### Fixture update discipline

For each fixture change:

1. identify the consuming test and object family;
2. state why behavior changed;
3. preserve the prior fixture or record supersession when it remains historically relevant;
4. update paired expected outputs;
5. verify valid and invalid polarity;
6. review rights and sensitivity;
7. recompute deterministic hashes where used;
8. update fixture parent and child README indexes;
9. run the narrow consumer and relevant aggregate suites;
10. avoid mass snapshot acceptance without semantic review.

### Skips and gaps

Every skip must include:

- category;
- reason;
- owner or resolution role;
- expected follow-up;
- whether the gap blocks promotion;
- review date or trigger.

Unknown coverage must not be converted into `PASS` by omission.

### Documentation consistency

The current fixture tree contains stale parent-not-found statements in child READMEs after `fixtures/release/README.md` was added. Correct those documents in a separate scoped change or a coordinated fixture-documentation PR. This README records the conflict; it does not silently rewrite unrelated files.

[Back to top](#top)

---

## Review burden

| Change type | Minimum review roles | Required focus |
|---|---|---|
| Direct release test | QA + release owner + affected implementation owner | Test scope, false positives/negatives, authority boundary. |
| Release fixture | QA + fixture owner + release owner | Synthetic/public-safe posture, expected outcome, consumer link. |
| Sensitive-domain fixture | QA + domain steward + policy/sensitivity/security reviewer | No real sensitive data; denial/generalization behavior. |
| Release schema assertion | QA + schema + contract + release owner | Shape versus meaning; no schema-valid-is-release collapse. |
| Promotion-policy assertion | QA + policy + release/promotion owner | Policy version, obligations, finite outcomes, human review. |
| Correction/rollback test | QA + correction/rollback + release owner | Audit history, reversibility, stale-state propagation. |
| CI promotion dependency | QA + CI + release + governance owner | Required-check semantics, artifacts, failure routing, separation of duties. |
| Removal or broad skip | QA + release + affected subsystem owner | Lost trust-spine coverage and migration/rollback plan. |

Owner names and CODEOWNERS mappings remain `NEEDS VERIFICATION`; do not invent reviewers or treat an automated actor as human approval.

[Back to top](#top)

---

## Definition of done

The direct release lane is not mature until all applicable criteria pass.

| Criterion | Required result |
|---|---|
| Direct executable inventory | At least one real test module is collected from `tests/release/`. |
| Zero-case protection | CI fails when no direct tests or required cases are collected. |
| Fixture inventory | Stable release fixture manifest exists; each fixture has a consumer and expected outcome. |
| Shape coverage | Accepted release schemas have positive and negative fixture coverage. |
| Semantic coverage | Release object boundaries are tested against accepted contracts. |
| Evidence coverage | Missing/unresolved evidence produces abstention, denial, or hold as specified. |
| Policy coverage | Rights, sensitivity, access, public-surface, and obligation cases are exercised. |
| Review coverage | Required human review and separation-of-duties holds are testable. |
| Receipt/proof coverage | Required receipt, proof, digest, signature, and provenance refs are checked. |
| Correction/rollback coverage | Correction, withdrawal, supersession, and rollback states have positive and negative cases. |
| Public-boundary coverage | Unreleased, stale, withdrawn, superseded, and sensitive material is denied. |
| No-network default | Default target is deterministic and offline. |
| CI artifact | Machine-readable report records command, commit, counts, fixture digest, and gaps. |
| Local/CI parity | Documented local command matches CI semantics. |
| Promotion use | Any promotion dependency is explicit, reviewed, and never equated with release approval. |
| Documentation | README, fixture indexes, contracts/schemas/policy links, and open gaps are current. |

Current status: **PARTIAL / NOT ESTABLISHED**. The README boundary is present; the direct executable suite and its proof artifacts are not established in the checked snapshot.

[Back to top](#top)

---

## Incremental implementation sequence

Prefer the smallest proof-bearing sequence:

1. **Inventory and drift check** — enumerate the direct lane, release fixtures, release schemas, contracts, policy stubs, validators, tools, workflows, and domain release test lanes.
2. **Coverage manifest** — add a deterministic inventory test that fails on zero direct tests and reports unresolved fixture families.
3. **PromotionDecision thin slice** — pair its concrete schema and semantic contract with confirmed synthetic valid/invalid fixtures and a direct boundary test.
4. **Candidate-not-release rule** — prove candidate, review, merge, file move, and schema validity do not equal release.
5. **Evidence/policy/review holds** — add missing evidence, stale policy, missing review, and unresolved obligation cases.
6. **ReleaseManifest hardening** — only after contract/schema fields are accepted; add dependency-closure tests.
7. **Correction and rollback** — add explicit correction, withdrawal, supersession, and rollback-readiness cases.
8. **Public-boundary integration** — test governed API/UI/map consumers against released, held, stale, withdrawn, and superseded states.
9. **CI integration** — add a no-network release-test job, machine-readable report, and fail-on-zero behavior.
10. **Promotion dependency** — only after accepted governance review; consume test evidence without letting the suite approve release.

Each step should be independently reviewable and reversible. Do not create empty scaffolds across all steps in one broad PR.

[Back to top](#top)

---

## Open verification register

| ID | Question | Evidence needed | Current status |
|---|---|---|---|
| RELTEST-001 | What files actually exist under `tests/release/` beyond the README? | Recursive tree at pinned ref or mounted checkout. | `NEEDS VERIFICATION` |
| RELTEST-002 | Are any release tests dynamically generated or located under another cross-cutting lane? | Pytest collection report and full test inventory. | `UNKNOWN` |
| RELTEST-003 | What release fixture payload files exist under `fixtures/release/`? | Recursive fixture tree, hashes, and consumer map. | `NEEDS VERIFICATION` |
| RELTEST-004 | Does `fixtures/contracts/v1/release/` contain schema fixtures despite the parent README gap? | Direct tree and test collection. | `NEEDS VERIFICATION` |
| RELTEST-005 | Which release schemas are accepted versus scaffolds? | Accepted ADR/schema registry and current schema review state. | `NEEDS VERIFICATION` |
| RELTEST-006 | Is the PromotionDecision schema paired with real valid/invalid fixtures and a validator? | Fixture files, validator implementation, tests, and CI logs. | `NEEDS VERIFICATION` |
| RELTEST-007 | Are `policy/release/` and `policy/promotion/` executable policy bundles? | Rego/equivalent files, tests, bundle IDs/digests, and logs. | `NOT ESTABLISHED` |
| RELTEST-008 | Are release validators or release helpers executable? | Source files, entry points, tests, and run evidence. | `NOT ESTABLISHED` |
| RELTEST-009 | Is ADR-0018 accepted, superseded, or still proposed at implementation time? | Current ADR status and decision log. | `PROPOSED` at snapshot |
| RELTEST-010 | Which workflows run release tests, and are they required? | Workflow definitions, branch protection/rulesets, and recent runs. | `UNKNOWN` |
| RELTEST-011 | What are current collected counts and pass rates? | Local/CI pytest collection and run artifacts at pinned commit. | `UNKNOWN` |
| RELTEST-012 | How are test reports linked to PromotionReceipt or release review without becoming approval? | Accepted contract, schema, policy, and consumer implementation. | `NEEDS VERIFICATION` |
| RELTEST-013 | Which domain release lanes are executable rather than README scaffolds? | Domain test inventory and collection report. | `NEEDS VERIFICATION` |
| RELTEST-014 | How do correction and rollback results propagate to public consumers? | API/UI/map/runtime tests, release records, and logs. | `UNKNOWN` |
| RELTEST-015 | Who owns this lane and its required reviews? | CODEOWNERS and steward registry. | `NEEDS VERIFICATION` |
| RELTEST-016 | Should stale fixture parent references be corrected in one coordinated PR? | Fixture documentation authority/supersession review. | `CONFLICTED / NEEDS VERIFICATION` |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| `tests/release/README.md` prior blob | `CONFIRMED` | Existing scope, exclusions, finite release-state emphasis, and placeholder maturity. | Planning-oriented; did not reflect current adjacent repo evidence. |
| `tests/README.md` | `CONFIRMED` | `tests/` is the canonical enforceability root; release tests are an accepted lane. | Runner/CI/pass rates remain partly verification-bound. |
| `release/README.md` | `CONFIRMED` | Release governance root, state vocabulary, record boundaries, correction/rollback posture. | README is not release authority or enforcement proof. |
| `contracts/release/README.md` | `CONFIRMED` | Semantic contract family and mixed maturity. | Does not prove schemas, fixtures, validators, or runtime. |
| `schemas/contracts/v1/release/README.md` | `CONFIRMED` | Eight surfaced schema files and mixed maturity. | Family README is not schema acceptance or current validation evidence. |
| `tests/schemas/test_common_contracts.py` | `CONFIRMED` | Release family is in the generic schema harness; fixture-gated discovery and valid/invalid behavior. | No direct release semantics, policy, review, correction, or runtime coverage. |
| `fixtures/contracts/v1/README.md` | `CONFIRMED` | Release schema-fixture parent coverage remains unresolved. | Does not prove payload absence. |
| `fixtures/release/README.md` | `CONFIRMED` | Synthetic release fixture parent and PromotionDecision child-lane index. | Payload inventory not verified. |
| `fixtures/release/promotion_decision/README.md` and child READMEs | `CONFIRMED / CONFLICTED` | Proposed fixture scenario vocabulary and maintenance rules. | Contain stale parent-not-found statements and do not prove payloads/consumers. |
| `policy/release/README.md` | `CONFIRMED` | Release policy README path exists. | Greenfield stub; no executable policy established. |
| `policy/promotion/README.md` | `CONFIRMED` | Promotion policy README path exists. | Greenfield stub; no executable policy established. |
| `tools/release/README.md` | `CONFIRMED` | Support-only tooling boundary and proposed test surface. | No executable helper established. |
| `tools/validators/release/README.md` | `CONFIRMED` | Release validator routing boundary and expected invariants. | No executable validator established. |
| `pyproject.toml` | `CONFIRMED` | Python and pytest configuration. | Does not prove collection or pass state. |
| `Makefile` | `CONFIRMED` | Current test/schema targets and release TODO targets. | Convenience targets do not prove CI requirements or release behavior. |
| `contracts-validate.yml` | `CONFIRMED` | Runs `make test` on push/PR. | Direct release lane excluded by current Make target. |
| `schema-validation.yml` and `validator-suite.yml` | `CONFIRMED` | Aggregate validator execution in CI. | Not a direct release-test suite. |
| `policy-boundary-guards.yml` | `CONFIRMED` | Selected boundary tests and path filters. | Target README path is not in the inspected PR filter. |
| `ADR-0018-promotion-gate-sequence.md` | `CONFIRMED document / PROPOSED decision` | Proposed A–G gate vocabulary and fail-closed mapping. | Not accepted implementation evidence. |
| `docs/doctrine/directory-rules.md` | `CONFIRMED doctrine` | `tests/` and `release/` responsibility-root separation; current path is appropriate. | Does not prove executable maturity. |
| Bounded GitHub code search | `CONFIRMED search result` | Did not establish a direct executable under `tests/release/`. | Search is not an exhaustive recursive tree or history proof. |

### No-loss assessment

The v0.1 README’s strongest material is retained and expanded:

- release tests remain enforceability proof, not release authority;
- promotion remains a governed state transition, not a file move;
- candidates, reviews, manifests, readiness checks, and changelogs do not equal approval;
- evidence, validation, policy, review, correction, withdrawal, supersession, and rollback remain explicit;
- default tests remain synthetic and no-network;
- release records stay under `release/`;
- schemas, contracts, policy, fixtures, receipts, proofs, lifecycle data, and implementation remain in their owning roots.

The schematic `.test.PROPOSED` filenames and placeholder `pytest tests/release` claim were replaced with repository-grounded current commands, a clearly proposed future layout, and explicit zero-collection risk.

[Back to top](#top)

---

## Documentation correction and rollback

This README is documentation, not a release record. Correct it when repository evidence changes.

### Correction triggers

- a direct release test appears;
- release fixture payloads are verified;
- release/promotion policy becomes executable;
- release validators or tools become executable;
- ADR-0018 changes status;
- release schemas mature or move;
- CI starts running or requiring release tests;
- fixture parent-child documentation is reconciled;
- a statement here becomes stale, contradicted, or overbroad.

### Rollback path

Before merge:

- leave the draft pull request unmerged; or
- restore the prior blob in a transparent follow-up commit on the same branch.

After merge:

- revert the documentation commit or pull request;
- do not reset or rewrite shared history;
- preserve the superseded v0.2 record in Git history;
- file a correction or drift note when the rollback reflects a substantive governance conflict rather than a simple editorial error.

Rolling back this README does not roll back a KFM release, workflow, policy bundle, schema, fixture, validator, receipt, proof, or public artifact because this change modifies documentation only.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-16 |
| Review state | Draft, repository-grounded documentation update |
| Direct lane maturity | README-only at bounded snapshot |
| Executable release suite | Not established |
| Next smallest safe change | Inventory actual release fixture payloads and add one PromotionDecision boundary test only after schema, contract, expected outcomes, and consumer path are verified. |

---

*Last updated: 2026-07-16 · Version: v0.2 · Authority: enforceability documentation only · [Back to top](#top)*
