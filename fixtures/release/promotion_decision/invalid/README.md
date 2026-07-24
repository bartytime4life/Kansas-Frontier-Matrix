<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-release-promotion-decision-invalid-readme
title: fixtures/release/promotion_decision/invalid/README.md — PromotionDecision Invalid Fixtures
type: README
version: v0.2
status: draft; repository-grounded; nested-fixture-lane; schema-negative; synthetic; no-network; fail-closed; non-authoritative
owner: NEEDS VERIFICATION — no path-specific CODEOWNERS or accepted fixture steward was inspected for this update
created: NEEDS VERIFICATION — file predates this versioned documentation contract
updated: 2026-07-24
supersedes: prior documentation at the same path; no fixture payload, contract, schema, policy, validator, release object, or runtime behavior is superseded
policy_label: repository-facing; fixtures; release; promotion-decision; invalid; synthetic; public-safe; no-network; fail-closed; non-publisher
owning_root: fixtures/
responsibility: document direct-child JSON fixtures that the current PromotionDecision JSON Schema validator must reject
truth_posture: cite-or-abstain; a negative fixture proves only that the declared schema check rejects the supplied synthetic object
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 85a939fd8a3fbac6e76fc4eaf3ce6172398d186f
  prior_blob: 1dc7245b5c0adf47601ef8ae81fb743a21fa6d97
  directory_rules_blob: 18653c00ba193a4afaa3e07a0924452807fb98ef
  fixtures_root_readme_blob: 911c20c86d9322f38b1f59db66b922a94fd027eb
  release_fixture_readme_blob: 94b19cc0a5945947a2c1df9b2db8aba973531d86
  promotion_fixture_readme_blob: 184c40ee4345b482df7a6f17c65e354e09114c7a
  valid_sibling_readme_blob: 12b95ac5b9f3dd16c6588e202e395f3a2f752072
  contract_blob: 42295bfc83a621cf125d33aa821912b426f70bd2
  schema_blob: a2d087a46772cf60e4b9dfb394892690e8a88b31
  validator_blob: ead33d6c5c073f319627ee42d99c5933c0e370d1
  jsonschema_runner_blob: ce05ae25d0cb6fc29a2ea41db6c65a99ca5e13e6
related:
  - ../../../README.md
  - ../../README.md
  - ../README.md
  - ../valid/README.md
  - ../../../../contracts/release/promotion_decision.md
  - ../../../../schemas/contracts/v1/release/promotion_decision.schema.json
  - ../../../../tools/validators/release/validate_promotion_decision.py
  - ../../../../tools/validators/_common/jsonschema_runner.py
  - ../../../../docs/architecture/directory-rules.md
notes:
  - "This is a same-path Markdown modernization. It creates no sibling README, fixture payload, schema, contract, policy, validator, release object, or publication state."
  - "The current validator treats every direct-child invalid/*.json file as a negative JSON Schema fixture that must produce at least one schema error."
  - "The current --fixtures implementation is non-recursive and does not fail merely because the valid/ and invalid/ directories contain no JSON files."
  - "Policy-invalid, evidence-unresolved, review-incomplete, rollback-unready, or release-unready cases that remain schema-valid require a separately implemented consumer and must not be claimed as covered by the current schema-only validator."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `PromotionDecision` Invalid Fixtures

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Fixture class: schema-negative](https://img.shields.io/badge/fixture%20class-schema--negative-b42318?style=flat-square)](#fixture-classification)
[![Network: not required](https://img.shields.io/badge/network-not%20required-15803d?style=flat-square)](#validation)
[![Authority: non-authoritative](https://img.shields.io/badge/authority-non--authoritative-6e7781?style=flat-square)](#authority-and-boundaries)

> **One-line purpose.** `fixtures/release/promotion_decision/invalid/` holds compact synthetic JSON objects that the current `PromotionDecision` JSON Schema validator is expected to reject.

**Quick navigation:** [Purpose](#purpose) · [Status](#status) · [Authority](#authority-and-boundaries) · [Classification](#fixture-classification) · [Scenarios](#schema-negative-scenario-catalog) · [Authoring](#authoring-contract) · [Validation](#validation) · [Failures](#failure-interpretation) · [Safety](#rights-sensitivity-and-test-data) · [Maintenance](#maintenance-and-review) · [Related paths](#related-paths) · [Verification](#verification-status) · [Rollback](#rollback)

> [!IMPORTANT]
> This lane is a **negative schema-fixture lane**, not a general release-governance failure archive. Under the current validator, every direct-child `invalid/*.json` file must produce at least one JSON Schema error. A policy-invalid or release-unready object that is still schema-valid needs a separate, implemented policy or semantic test harness.

> [!CAUTION]
> A rejected fixture does not prove that KFM policy, evidence resolution, reviewer separation, rollback execution, release readiness, publication, or runtime serving is enforced. It proves only the bounded check performed by the named consumer.

---

## Purpose

This directory specializes the reusable fixture root for one narrow question:

> Does the current `PromotionDecision` JSON Schema reject this deliberately malformed synthetic object for the declared reason?

The lane supports:

- schema-regression checks;
- validator dry-runs;
- documentation examples of fail-closed object shape;
- paired positive/negative comparisons with [`../valid/`](../valid/README.md);
- future expected diagnostic snapshots when a governed golden-output convention is verified.

It does **not** exist to store real promotion decisions or to simulate release authority.

[Back to top](#top)

---

## Status

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| Target README | **CONFIRMED** at prior blob `1dc7245b5c0adf47601ef8ae81fb743a21fa6d97` | Existing document is modernized in place |
| Parent fixture documentation | **CONFIRMED** at [`../../README.md`](../../README.md) and [`../README.md`](../README.md) | The release and PromotionDecision fixture boundaries now exist; older “parent not found” notes are stale |
| Paired schema | **CONFIRMED** at [`promotion_decision.schema.json`](../../../../schemas/contracts/v1/release/promotion_decision.schema.json) | Required fields, finite decision enum, closed properties, review shape, and hydrology ID condition are machine-declared |
| Validator entry point | **CONFIRMED** at [`validate_promotion_decision.py`](../../../../tools/validators/release/validate_promotion_decision.py) | The validator binds the schema to `fixtures/release/promotion_decision/` |
| Shared runner | **CONFIRMED** at [`jsonschema_runner.py`](../../../../tools/validators/_common/jsonschema_runner.py) | `--fixtures` reads direct-child `valid/*.json` and `invalid/*.json`, then enforces positive/negative schema expectations |
| Fixture payload inventory | **UNKNOWN** | No exhaustive directory listing or payload-by-payload review was available in this update |
| Policy and semantic enforcement | **NEEDS VERIFICATION / not established by the schema runner** | Current evidence supports JSON Schema validation only |
| CI and branch-protection enforcement | **NEEDS VERIFICATION** | File presence does not prove required-check enforcement |
| Release or publication state | **DENIED as inference** | Fixtures and validator results cannot establish KFM publication |

### Material corrections in this revision

- Replaces stale claims that `fixtures/release/README.md`, the schema, and the validator were unverified.
- Narrows the lane from broad “invalid release cases” to the negative JSON Schema cases the current runner actually enforces.
- Documents the runner’s non-recursive file discovery and empty-inventory limitation.
- Separates schema invalidity from policy, evidence, review, rollback, and release-readiness failure.
- Adds a repository-grounded command, expected exit behavior, and explicit proof limits.

[Back to top](#top)

---

## Authority and boundaries

| Responsibility | Authority home | Role of this lane |
|---|---|---|
| `PromotionDecision` meaning | [`contracts/release/promotion_decision.md`](../../../../contracts/release/promotion_decision.md) | Supplies malformed examples; never redefines semantics |
| Machine-checkable shape | [`schemas/contracts/v1/release/promotion_decision.schema.json`](../../../../schemas/contracts/v1/release/promotion_decision.schema.json) | Exercises rejection behavior; never becomes schema authority |
| Schema validation implementation | [`tools/validators/release/validate_promotion_decision.py`](../../../../tools/validators/release/validate_promotion_decision.py) | Provides negative inputs; never becomes validator authority |
| Policy admissibility | `policy/promotion/` and `policy/release/` when implemented and verified | May later supply test inputs to policy checks; never decides policy |
| Release decisions and manifests | `release/` | Must never store or approve real release state |
| Receipts and proofs | `data/receipts/` and `data/proofs/` | Must never store canonical receipts, proofs, or evidence |
| Public surfaces | Governed APIs and released artifacts | Direct fixture serving is denied |

Directory Rules place this file under `fixtures/` because its primary responsibility is reusable synthetic test input. The path changes no root, lifecycle phase, schema home, contract home, policy home, or release home.

### Explicit non-scope

Do not place any of the following here:

- actual `PromotionDecision`, `ReleaseManifest`, `RollbackCard`, `ReviewRecord`, or `PolicyDecision` records;
- real EvidenceBundles, EvidenceRefs, SourceDescriptors, receipts, proofs, attestations, or release artifacts;
- implementation code, policy rules, schemas, contracts, CI output, runtime output, or published data;
- private reviewer identities, internal ticket details, credentials, signed URLs, restricted policy context, or sensitive source/location data;
- schema-valid policy-negative cases unless a separate consumer and expected outcome are explicitly documented.

[Back to top](#top)

---

## Fixture classification

### What the current runner consumes

With `--fixtures`, the shared runner reads only:

```text
fixtures/release/promotion_decision/
├── valid/*.json
└── invalid/*.json
```

Important implementation properties:

- discovery is **non-recursive**;
- only direct-child files ending in `.json` are included;
- README, YAML, JSONL, nested directories, and differently named extensions are ignored by this command;
- every `valid/*.json` file must produce zero schema errors;
- every `invalid/*.json` file must produce at least one schema error;
- an empty `valid/` and `invalid/` inventory can currently return exit code `0`, so zero exit alone does not prove coverage exists;
- the runner constructs `Draft202012Validator` without an explicit format checker, so this README does not claim that `format: date-time` is enforced.

### Classification rule

| Case | Put it here? | Reason |
|---|---:|---|
| Missing schema-required field | Yes | Must fail JSON Schema |
| Invalid `version` or `decision` enum | Yes | Must fail JSON Schema |
| Extra root or `review` property | Yes | Schema closes additional properties |
| Invalid hydrology ID pattern | Yes | Conditional schema rule applies |
| Empty required string | Yes | `minLength: 1` applies |
| Invalid timestamp formatting only | **NEEDS VERIFICATION** | Runner does not provide an explicit format checker |
| Evidence reference exists syntactically but cannot resolve | No, not for current schema-only expectation | Requires evidence-resolution logic |
| Policy bundle is stale but non-empty | No, not for current schema-only expectation | Requires policy/semantic logic |
| Reviewer lacks real authority but fields are present | No, not for current schema-only expectation | Requires review/separation-of-duties logic |
| Rollback URI is present but unusable | No, not for current schema-only expectation | Requires rollback-readiness logic |
| Release candidate is unsafe despite schema validity | No, not for current schema-only expectation | Requires policy/release-readiness logic |

[Back to top](#top)

---

## Schema-negative scenario catalog

The paired schema supports these directly testable negative families.

| Scenario | Expected schema result | Relevant schema surface |
|---|---|---|
| Missing any required root field | Reject | Root `required` list |
| `version` is not `v1` | Reject | `const: "v1"` |
| `decision` is not `APPROVE`, `DENY`, or `ABSTAIN` | Reject | Finite enum |
| Required string is empty | Reject | `minLength: 1` |
| `review` is missing `reviewer` or `ticket` | Reject | Nested `required` |
| Unexpected property inside `review` | Reject | Nested `additionalProperties: false` |
| Unexpected root property | Reject | Root `additionalProperties: false` |
| `domain` is `hydrology` and `id` does not match `promo:hydrology:<suffix>` | Reject | Conditional `allOf` rule |
| JSON cannot be parsed | Reject operationally | Runner catches parse/read exceptions |
| `decided_at` is not a valid date-time | **NEEDS VERIFICATION** | Schema declares `format`, but current runner does not pass an explicit format checker |

Keep each fixture focused on one primary failure when practical. Multi-failure fixtures make diagnostics harder to interpret and can conceal regressions when the first reported error changes.

[Back to top](#top)

---

## Authoring contract

Each negative fixture should be:

- **synthetic** — no real release, reviewer, evidence, policy, ticket, or source data;
- **minimal** — include only enough material to isolate the intended rejection;
- **deterministic** — no live endpoint, clock, random, model, network, or secret dependency;
- **public-safe** — no sensitive exact geometry, living-person data, restricted identifiers, or private infrastructure details;
- **single-purpose where practical** — one primary invalid condition per file;
- **self-describing** — file name communicates the expected failure;
- **paired** — link to a corresponding valid fixture or expected diagnostic when such a pairing is verified;
- **consumer-bound** — identify the schema, validator, test, or documentation example that uses it.

### Recommended naming

Use descriptive kebab-case names such as:

```text
missing-evidence-ref.json
invalid-version.json
invalid-decision-enum.json
review-missing-ticket.json
unexpected-root-property.json
hydrology-id-pattern-mismatch.json
```

These names are recommendations for future or existing fixtures, not a claim that these exact files currently exist.

### Minimal illustrative example

```json
{
  "id": "promo:hydrology:example",
  "version": "v1",
  "domain": "hydrology",
  "run_id": "run:toy:001",
  "decision": "PUBLISH",
  "evidence_ref": "evidence:toy:001",
  "evidence_bundle_uri": "kfm://evidence-bundle/toy-001",
  "rollback_card_uri": "kfm://rollback-card/toy-001",
  "policy_bundle": "policy:toy:v1",
  "decided_at": "2026-01-01T00:00:00Z",
  "review": {
    "reviewer": "reviewer:toy",
    "ticket": "ticket:toy-001"
  }
}
```

Expected result: schema rejection because `PUBLISH` is outside the declared `APPROVE | DENY | ABSTAIN` enum. This is illustrative documentation, not a verified repository payload.

[Back to top](#top)

---

## Validation

### Repository-grounded command

From the repository root:

```bash
python tools/validators/release/validate_promotion_decision.py --fixtures
```

Expected aggregate behavior:

| Condition | Expected process result |
|---|---:|
| Every valid JSON passes and every invalid JSON fails schema validation | Exit `0` |
| Any valid JSON has a schema error | Exit `1` |
| Any invalid JSON has no schema error | Exit `1` |
| JSON read/parse/validation exception occurs | Exit `1` in the current shared runner |
| No fixture JSON files are discovered | May exit `0`; coverage remains unproven |

The command requires no network by design. Dependency installation and environment setup are governed elsewhere and were not reverified for this README.

### Validate one file

```bash
python tools/validators/release/validate_promotion_decision.py \
  fixtures/release/promotion_decision/invalid/<fixture>.json
```

For an intentionally invalid file, the direct single-file mode is expected to exit `1` because it reports ordinary schema validity, not “negative fixture expectation satisfied.” Use `--fixtures` for aggregate positive/negative expectation semantics.

### What a passing aggregate check proves

A passing `--fixtures` run can support only these bounded conclusions:

- discovered `valid/*.json` files had no reported schema errors;
- discovered `invalid/*.json` files had at least one reported schema error;
- discovered JSON files were readable and parseable;
- the validator and local schema resolver executed in that environment.

It does **not** prove:

- that any fixture files were discovered;
- complete scenario coverage;
- semantic contract correctness;
- EvidenceRef or EvidenceBundle resolution;
- policy-bundle freshness or policy decisions;
- reviewer identity, ticket validity, or separation of duties;
- rollback-card existence or executability;
- release-manifest closure, receipts, proofs, signatures, or attestations;
- public-summary safety, runtime behavior, CI enforcement, release, or publication.

[Back to top](#top)

---

## Failure interpretation

| Observation | Interpretation | Safe next action |
|---|---|---|
| Invalid fixture unexpectedly passes | Schema no longer rejects the declared shape, or fixture no longer expresses the intended defect | Inspect schema and fixture together; do not weaken the fixture silently |
| Valid fixture unexpectedly fails | Schema, fixture, local reference resolution, or validator environment changed | Compare against contract and schema; repair the smallest incorrect surface |
| Invalid fixture fails for a different reason | Fixture may contain multiple defects or schema ordering changed | Minimize the fixture and document the primary expected rejection |
| Command exits `0` with no discovered fixtures | Validator execution succeeded but coverage is empty | Verify inventory before claiming fixture coverage |
| Schema-valid object is unsafe by policy | Not a schema-negative fixture | Route to a verified policy/semantic test lane and retain fail-closed posture |
| Validator errors on missing dependency or resolver issue | Operational error, not object rejection | Repair environment or resolver; do not classify as expected invalid behavior |

Do not “fix” an invalid fixture merely to make it pass ordinary validation. Its success criterion is rejection for the intended, documented reason.

[Back to top](#top)

---

## Rights, sensitivity, and test data

All material in this lane must be synthetic or demonstrably public-safe.

Use:

- toy IDs and URIs;
- invented reviewer and ticket identifiers;
- non-routable or repository-local references;
- fixed timestamps;
- placeholder hashes that cannot be mistaken for signed production attestations;
- generalized or absent geometry.

Never use:

- real reviewer names or private ticket IDs;
- authentic access tokens, signatures, signed URLs, internal endpoints, or credentials;
- real living-person, DNA, archaeology, rare-species, infrastructure, land-title, or other protected records;
- production release candidates, real evidence bundles, or sensitive policy inputs.

If real or restricted material is found here, stop using the fixture, remove it through a reviewed correction, and route the source material through the appropriate security or governed lifecycle process.

[Back to top](#top)

---

## Maintenance and review

Update this README when any of the following changes:

- required fields, enum values, conditional rules, or property closure in the paired schema;
- validator entry point, fixture discovery rules, format checking, recursion, or exit behavior;
- verified payload inventory or naming convention;
- policy or semantic test lanes that consume schema-valid negative cases;
- expected diagnostic/golden-output conventions;
- parent or sibling fixture boundaries;
- Directory Rules placement or fixture-home conventions.

Review expectations:

- keep the README, schema, validator, and affected fixtures in one coherent review boundary when their contract changes together;
- preserve existing negative cases unless evidence shows they are wrong, redundant, unsafe, or superseded;
- add a valid counterpart when a negative case depends on subtle shape differences;
- avoid broad fixture churn when one focused regression case is sufficient;
- record coverage gaps rather than implying completeness.

The path-specific reviewer remains **NEEDS VERIFICATION** until current CODEOWNERS and repository rules are inspected.

[Back to top](#top)

---

## Related paths

| Path | Relationship |
|---|---|
| [`../../../README.md`](../../../README.md) | Canonical reusable fixture-root contract |
| [`../../README.md`](../../README.md) | Release fixture parent |
| [`../README.md`](../README.md) | PromotionDecision fixture-family parent |
| [`../valid/README.md`](../valid/README.md) | Positive schema-fixture sibling |
| [`../../../../contracts/release/promotion_decision.md`](../../../../contracts/release/promotion_decision.md) | Semantic contract |
| [`../../../../schemas/contracts/v1/release/promotion_decision.schema.json`](../../../../schemas/contracts/v1/release/promotion_decision.schema.json) | Machine-shape authority |
| [`../../../../tools/validators/release/validate_promotion_decision.py`](../../../../tools/validators/release/validate_promotion_decision.py) | Validator entry point |
| [`../../../../tools/validators/_common/jsonschema_runner.py`](../../../../tools/validators/_common/jsonschema_runner.py) | Shared fixture discovery and expectation logic |
| [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md) | Placement doctrine |

Potential policy, release, proof, receipt, and golden-output counterparts remain **NEEDS VERIFICATION** unless linked from verified repository evidence.

[Back to top](#top)

---

## Verification status

### CONFIRMED

- The target exists at the same path.
- The release and PromotionDecision parent READMEs exist.
- The valid sibling README exists.
- The semantic contract, paired schema, validator entry point, and shared JSON Schema runner exist.
- The schema requires `id`, `version`, `domain`, `run_id`, `decision`, `evidence_ref`, `evidence_bundle_uri`, `rollback_card_uri`, `policy_bundle`, `decided_at`, and `review`.
- The schema limits `decision` to `APPROVE | DENY | ABSTAIN`, closes root/review properties, and applies a hydrology ID pattern.
- The current `--fixtures` runner distinguishes direct-child valid and invalid JSON fixtures by expected schema result.

### NEEDS VERIFICATION

- Exact fixture filenames and payload inventory in this directory.
- Whether the repository currently has zero, one, or many negative JSON fixtures.
- Format-checker enforcement for `decided_at`.
- Policy, evidence-resolution, review, rollback, release-readiness, bounded-summary, and supersession test harnesses.
- Required CI checks, branch protection, and CODEOWNERS enforcement.
- Golden diagnostic output conventions.

### NOT RUN in this update

- Repository checkout validation.
- The Python validator command.
- Markdown lint, docs build, or link checker.
- CI workflows.

These checks were not run because this update used the authenticated GitHub contents interface rather than a mounted executable checkout. Remote read-back and base-to-head diff verification remain required after mutation.

[Back to top](#top)

---

## Rollback

This is a one-file documentation change.

Rollback method:

1. revert the documentation commit or restore prior blob `1dc7245b5c0adf47601ef8ae81fb743a21fa6d97`;
2. verify that no fixture, schema, contract, policy, validator, release, receipt, proof, or runtime file changed with it;
3. re-read the restored remote bytes.

Reverting this README changes documentation only. It does not alter fixture behavior, schema behavior, policy, release state, or publication state.

[Back to top](#top)
