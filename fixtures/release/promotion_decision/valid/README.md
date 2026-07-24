<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-release-promotion-decision-valid-readme
title: fixtures/release/promotion_decision/valid/README.md — PromotionDecision Valid Fixtures
type: README
version: v0.2
status: draft; repository-grounded; nested-fixture-lane; schema-positive; synthetic; no-network; non-authoritative
owner: NEEDS VERIFICATION — no path-specific CODEOWNERS or accepted fixture steward was inspected for this update
created: NEEDS VERIFICATION — file predates this versioned documentation contract
updated: 2026-07-24
supersedes: prior documentation at the same path; no fixture payload, contract, schema, policy, validator, release object, or runtime behavior is superseded
policy_label: repository-facing; fixtures; release; promotion-decision; valid; synthetic; public-safe; no-network; non-publisher
owning_root: fixtures/
responsibility: document direct-child JSON fixtures that the current PromotionDecision JSON Schema validator must accept
truth_posture: cite-or-abstain; a positive fixture proves only that the declared schema check accepts the supplied synthetic object
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 00caf13517214f487f8e05465782bcf5d01d613d
  prior_blob: 12b95ac5b9f3dd16c6588e202e395f3a2f752072
  directory_rules_blob: 18653c00ba193a4afaa3e07a0924452807fb98ef
  fixtures_root_readme_blob: 911c20c86d9322f38b1f59db66b922a94fd027eb
  release_fixture_readme_blob: 94b19cc0a5945947a2c1df9b2db8aba973531d86
  promotion_fixture_readme_blob: 184c40ee4345b482df7a6f17c65e354e09114c7a
  invalid_sibling_readme_blob: 1a6fe6a56f8969fe0714dd273fdef5fc148d4726
  contract_blob: 42295bfc83a621cf125d33aa821912b426f70bd2
  schema_blob: a2d087a46772cf60e4b9dfb394892690e8a88b31
  validator_blob: ead33d6c5c073f319627ee42d99c5933c0e370d1
  jsonschema_runner_blob: ce05ae25d0cb6fc29a2ea41db6c65a99ca5e13e6
related:
  - ../../../README.md
  - ../../README.md
  - ../README.md
  - ../invalid/README.md
  - ../../../../contracts/release/promotion_decision.md
  - ../../../../schemas/contracts/v1/release/promotion_decision.schema.json
  - ../../../../tools/validators/release/validate_promotion_decision.py
  - ../../../../tools/validators/_common/jsonschema_runner.py
  - ../../../../docs/architecture/directory-rules.md
notes:
  - "This is a same-path Markdown modernization. It creates no sibling README, fixture payload, schema, contract, policy, validator, release object, or publication state."
  - "The current validator treats every direct-child valid/*.json file as a positive JSON Schema fixture that must produce zero schema errors."
  - "The current --fixtures implementation is non-recursive and does not fail merely because the valid/ and invalid/ directories contain no JSON files."
  - "Schema acceptance does not prove that evidence resolves, a policy bundle is current, a reviewer is authorized, a rollback target works, a release is ready, or publication occurred."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `PromotionDecision` Valid Fixtures

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Fixture class: schema-positive](https://img.shields.io/badge/fixture%20class-schema--positive-15803d?style=flat-square)](#fixture-classification)
[![Network: not required](https://img.shields.io/badge/network-not%20required-15803d?style=flat-square)](#validation)
[![Authority: non-authoritative](https://img.shields.io/badge/authority-non--authoritative-6e7781?style=flat-square)](#authority-and-boundaries)

> **One-line purpose.** `fixtures/release/promotion_decision/valid/` holds compact synthetic JSON objects that the current `PromotionDecision` JSON Schema validator is expected to accept.

**Quick navigation:** [Purpose](#purpose) · [Status](#status) · [Authority](#authority-and-boundaries) · [Classification](#fixture-classification) · [Scenarios](#schema-positive-scenario-catalog) · [Example](#illustrative-schema-positive-object) · [Authoring](#authoring-contract) · [Validation](#validation) · [Failures](#failure-interpretation) · [Safety](#rights-sensitivity-and-test-data) · [Maintenance](#maintenance-and-review) · [Related paths](#related-paths) · [Verification](#verification-status) · [Rollback](#rollback)

> [!IMPORTANT]
> This lane is a **positive schema-fixture lane**, not a release-approval, evidence-resolution, policy-pass, review-authorization, rollback-readiness, or publication archive. Under the current validator, every direct-child `valid/*.json` file must produce zero JSON Schema errors.

> [!CAUTION]
> An accepted fixture proves only that the supplied synthetic object satisfies the machine shape enforced by the current schema runner. It does **not** prove that referenced evidence exists, a policy bundle is current, a reviewer is authorized, a rollback target is usable, a candidate is release-ready, or KFM has published anything.

---

## Purpose

This directory specializes the reusable fixture root for one narrow question:

> Does the current `PromotionDecision` JSON Schema accept this compact synthetic object as structurally valid?

The lane supports:

- positive JSON Schema regression checks;
- validator dry-runs;
- documentation examples of the current object shape;
- paired positive/negative comparisons with [`../invalid/`](../invalid/README.md);
- finite decision-enum examples for `APPROVE`, `DENY`, and `ABSTAIN`;
- future expected diagnostic or normalized-output snapshots when a governed golden-output convention is verified.

It does **not** exist to store actual promotion decisions, authorize lifecycle transitions, or simulate release authority.

[Back to top](#top)

---

## Status

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| Target README | **CONFIRMED** at prior blob `12b95ac5b9f3dd16c6588e202e395f3a2f752072` | Existing document is modernized in place |
| Parent fixture documentation | **CONFIRMED** at [`../../README.md`](../../README.md) and [`../README.md`](../README.md) | Release and PromotionDecision fixture boundaries exist; the older “parent not found” note is stale |
| Sibling invalid lane | **CONFIRMED** at [`../invalid/README.md`](../invalid/README.md) | The negative side is explicitly limited to schema-rejected direct-child JSON fixtures |
| Paired schema | **CONFIRMED** at [`promotion_decision.schema.json`](../../../../schemas/contracts/v1/release/promotion_decision.schema.json) | Required fields, finite decision enum, closed properties, review shape, and hydrology ID condition are machine-declared |
| Validator entry point | **CONFIRMED** at [`validate_promotion_decision.py`](../../../../tools/validators/release/validate_promotion_decision.py) | The validator binds the schema to `fixtures/release/promotion_decision/` |
| Shared runner | **CONFIRMED** at [`jsonschema_runner.py`](../../../../tools/validators/_common/jsonschema_runner.py) | `--fixtures` reads direct-child `valid/*.json` and `invalid/*.json`, then enforces positive/negative schema expectations |
| Fixture payload inventory | **UNKNOWN** | No exhaustive directory listing or payload-by-payload review was available in this update |
| Evidence, policy, review, rollback, and release-readiness enforcement | **NEEDS VERIFICATION / not established by the schema runner** | Current evidence supports JSON Schema validation only |
| CI and branch-protection enforcement | **NEEDS VERIFICATION** | File and workflow presence do not prove required-check enforcement |
| Release or publication state | **DENIED as inference** | Fixtures and validator results cannot establish KFM publication |

### Material corrections in this revision

- Replaces the stale claim that `fixtures/release/README.md` was absent.
- Replaces conditional “if present” wording for the paired schema and validator with pinned repository evidence.
- Narrows the lane from broad “positive release cases” to the positive JSON Schema cases the current runner actually enforces.
- Documents the runner’s non-recursive file discovery and empty-inventory limitation.
- Separates machine-shape validity from evidence resolution, policy validity, review authority, rollback usability, and release readiness.
- Adds a repository-grounded command, expected exit behavior, illustrative object, and explicit proof limits.

[Back to top](#top)

---

## Authority and boundaries

| Responsibility | Authority home | Role of this lane |
|---|---|---|
| `PromotionDecision` meaning | [`contracts/release/promotion_decision.md`](../../../../contracts/release/promotion_decision.md) | Supplies accepted examples; never redefines semantics |
| Machine-checkable shape | [`schemas/contracts/v1/release/promotion_decision.schema.json`](../../../../schemas/contracts/v1/release/promotion_decision.schema.json) | Exercises acceptance behavior; never becomes schema authority |
| Schema validation implementation | [`tools/validators/release/validate_promotion_decision.py`](../../../../tools/validators/release/validate_promotion_decision.py) | Provides positive inputs; never becomes validator authority |
| Policy admissibility | `policy/promotion/` and `policy/release/` when implemented and verified | May later supply inputs to policy checks; never decides policy |
| Evidence resolution | Evidence resolver and `EvidenceBundle` surfaces when implemented and verified | Uses toy references only; never proves evidence closure |
| Review authority | Review records, policy, and separation-of-duties controls | Carries toy `review` fields; never establishes reviewer authority |
| Release decisions and manifests | `release/` | Must never store or approve real release state |
| Receipts and proofs | `data/receipts/` and `data/proofs/` | Must never store canonical receipts, proofs, or evidence |
| Public surfaces | Governed APIs and released artifacts | Direct fixture serving is denied |

Directory Rules place this file under `fixtures/` because its primary responsibility is reusable synthetic checking input. This same-path update changes no root, lifecycle phase, schema home, contract home, policy home, release home, or publication state.

### Explicit non-scope

Do not place any of the following here:

- actual `PromotionDecision`, `ReleaseManifest`, `RollbackCard`, `ReviewRecord`, or `PolicyDecision` records;
- real EvidenceBundles, EvidenceRefs, SourceDescriptors, receipts, proofs, attestations, or release artifacts;
- implementation code, policy rules, schemas, contracts, CI output, runtime output, or published data;
- private reviewer identities, internal ticket details, credentials, signed URLs, restricted policy context, or sensitive source/location data;
- claims that a schema-valid toy reference resolves or that a schema-valid `APPROVE` is authorized.

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
| All required fields are present with allowed machine types and values | Yes | Expected to pass JSON Schema |
| `decision` is `APPROVE`, `DENY`, or `ABSTAIN` | Yes | All three are schema-valid finite release-transition values |
| `domain` is `hydrology` and `id` matches `promo:hydrology:<suffix>` | Yes | Satisfies the conditional schema rule |
| Non-hydrology object uses a non-empty synthetic ID | Yes | No domain-specific ID pattern is declared for other domains |
| `review` contains exactly non-empty `reviewer` and `ticket` strings | Yes | Satisfies the closed nested object shape |
| Toy evidence, rollback, and policy references are non-empty but not resolved | Yes **only as schema-positive examples** | Schema checks non-empty strings, not resolution or usability |
| Policy bundle is stale but remains a non-empty string | Not as a claimed policy-positive example | It may pass schema but requires a separate semantic/policy negative test |
| Reviewer fields are present but the actor lacks authority | Not as a claimed review-positive example | Requires review/separation-of-duties logic |
| Rollback URI is present but unusable | Not as a claimed rollback-ready example | Requires rollback-readiness logic |
| Release candidate is unsafe despite schema validity | Not as a claimed release-ready example | Requires policy/release-readiness logic |
| `decided_at` appears malformed but all other fields are valid | **NEEDS VERIFICATION** | Schema declares `format`, but the current runner does not pass an explicit format checker |

> [!NOTE]
> A schema-positive fixture may use clearly synthetic, non-resolving URI-like strings because the current schema checks only non-empty strings. The fixture name and documentation must not relabel that result as evidence closure, rollback readiness, policy approval, or review authorization.

[Back to top](#top)

---

## Schema-positive scenario catalog

The paired schema supports these directly testable positive families.

| Scenario | Expected schema result | Relevant schema surface |
|---|---|---|
| Complete synthetic `APPROVE` object | Accept | Required fields, `decision` enum, closed object |
| Complete synthetic `DENY` object | Accept | `decision` enum includes `DENY` |
| Complete synthetic `ABSTAIN` object | Accept | `decision` enum includes `ABSTAIN` |
| `version` is exactly `v1` | Accept | `const: "v1"` |
| All required strings are non-empty | Accept | `minLength: 1` |
| `review` contains exactly `reviewer` and `ticket` | Accept | Nested `required` and `additionalProperties: false` |
| Root contains no undeclared property | Accept | Root `additionalProperties: false` |
| Hydrology ID matches `promo:hydrology:<suffix>` | Accept | Conditional `allOf` rule |
| Non-hydrology domain has any non-empty ID | Accept | Hydrology condition does not apply |
| Clear RFC 3339 timestamp string | Expected to accept | Schema declares `format: date-time`; enforcement details remain bounded by runner configuration |

A positive fixture should focus on one useful shape or decision posture while preserving the complete required object. Avoid stuffing unrelated semantic claims into filenames such as `policy-approved`, `evidence-resolved`, or `release-ready` unless a verified consumer beyond JSON Schema actually checks those properties.

[Back to top](#top)

---

## Illustrative schema-positive object

The following object is an **illustrative documentation example**, not a confirmed repository payload and not a real release decision:

```json
{
  "id": "promo:hydrology:fixture-approve-001",
  "version": "v1",
  "domain": "hydrology",
  "run_id": "run:fixture:hydrology:001",
  "decision": "APPROVE",
  "evidence_ref": "evidence:fixture:001",
  "evidence_bundle_uri": "kfm://evidence-bundle/fixture-001",
  "rollback_card_uri": "kfm://rollback-card/fixture-001",
  "policy_bundle": "policy:fixture:v1",
  "decided_at": "2026-01-01T00:00:00Z",
  "review": {
    "reviewer": "reviewer:fixture",
    "ticket": "ticket:fixture-001"
  }
}
```

What this example demonstrates:

- all schema-required fields are present;
- the object uses the required `v1` version;
- `APPROVE` is an allowed enum value;
- the hydrology ID follows the conditional pattern;
- the nested review object has exactly the declared fields;
- no undeclared root property is present.

What it does **not** demonstrate:

- that any reference resolves;
- that evidence supports the decision;
- that the named policy bundle exists or is current;
- that the reviewer is authorized or independent;
- that the rollback card is executable;
- that the run is release-ready;
- that a release manifest, proof pack, receipt, signature, or publication exists.

[Back to top](#top)

---

## Authoring contract

Each positive fixture should be:

- **synthetic** — no real release, reviewer, evidence, policy, ticket, or source data;
- **complete** — include every schema-required field;
- **minimal** — avoid optional narrative or unrelated semantics that the schema does not check;
- **deterministic** — no live endpoint, clock, random, model, network, or secret dependency;
- **public-safe** — no sensitive exact geometry, living-person data, restricted identifiers, or private infrastructure details;
- **explicitly schema-scoped** — state that acceptance is machine-shape acceptance only;
- **self-describing** — file name communicates the shape or enum posture being exercised;
- **paired where useful** — link to a corresponding invalid fixture or expected diagnostic when such a pairing is verified;
- **consumer-bound** — identify the schema, validator, test, or documentation example that uses it.

### Recommended naming

Use descriptive kebab-case names such as:

```text
approve-minimal.json
deny-minimal.json
abstain-minimal.json
hydrology-approve-valid-id.json
non-hydrology-valid-id.json
review-shape-complete.json
```

Avoid names that claim unverified semantics, including:

```text
policy-approved.json
evidence-resolved.json
reviewer-authorized.json
rollback-ready.json
release-ready.json
published.json
```

Those names are admissible only after a specific verified consumer checks the named property and the fixture documentation identifies that consumer and expected result.

[Back to top](#top)

---

## Validation

### Current schema-fixture command

From a repository checkout with the required Python dependencies installed:

```bash
python tools/validators/release/validate_promotion_decision.py --fixtures
```

Current runner behavior:

1. load `schemas/contracts/v1/release/promotion_decision.schema.json`;
2. build a local JSON Schema registry;
3. discover direct-child `valid/*.json` and `invalid/*.json` files;
4. parse and validate each discovered file;
5. require each valid fixture to produce zero schema errors;
6. require each invalid fixture to produce at least one schema error;
7. return non-zero when an expectation is violated.

### Validate one candidate file

```bash
python tools/validators/release/validate_promotion_decision.py \
  fixtures/release/promotion_decision/valid/<fixture>.json
```

Expected command-level posture:

| Result | Interpretation |
|---|---|
| Exit `0` for a named file | The file parsed and produced zero errors under the current JSON Schema validator |
| Exit `1` for a named file | Parsing, file access, or schema validation failed for at least one named file |
| Exit `2` with no named file and without `--fixtures` | The runner was invoked without an input target |
| Exit `0` for `--fixtures` with no discovered JSON files | Current empty-inventory limitation; **not** proof of coverage |

> [!WARNING]
> Do not label a successful schema run as `policy pass`, `evidence resolved`, `review approved`, `rollback ready`, `release ready`, `published`, or `production parity`. Those claims require separate evidence and consumers.

### What a passing fixture check proves

| Claim | Supported by current schema check? |
|---|---:|
| JSON parsed | Yes |
| Required fields and declared types are satisfied | Yes |
| `version` and `decision` enum are accepted | Yes |
| Closed root/review object shape is satisfied | Yes |
| Hydrology conditional ID rule is satisfied | Yes, when applicable |
| Date-time format is actively enforced | **NEEDS VERIFICATION** |
| Evidence reference resolves | No |
| EvidenceBundle supports the decision | No |
| Policy bundle exists or is current | No |
| Reviewer is authorized or independent | No |
| Rollback target works | No |
| Release candidate is safe or ready | No |
| Release manifest, proof, receipt, signature, or publication exists | No |

[Back to top](#top)

---

## Failure interpretation

When a file in `valid/` is rejected, investigate in this order:

1. **JSON parse or file-read failure** — malformed JSON, encoding issue, or missing file.
2. **Required-field drift** — a required property is missing or misspelled.
3. **Enum/version drift** — `version` is not `v1`, or `decision` is outside the finite enum.
4. **Closed-property drift** — an undeclared root or review field was added.
5. **Nested review drift** — `reviewer` or `ticket` is missing or empty.
6. **Hydrology ID drift** — a hydrology object does not use the conditional ID pattern.
7. **Schema evolution** — the schema changed and the fixture needs a reviewed update.
8. **Consumer mismatch** — the file was intended for a semantic or policy test rather than the schema-positive lane.

A rejected positive fixture is not automatically a schema defect. The fixture may be stale or misplaced. Compare the contract, schema, validator, sibling invalid cases, and intended consumer before changing any authority surface.

Conversely, a schema-valid object with unresolved evidence, stale policy, unauthorized review, or unusable rollback support is not a successful governed release case. It is only a structurally accepted object and needs a separate semantic or policy consumer.

[Back to top](#top)

---

## Rights, sensitivity, and test data

Use toy, public-safe values only.

| Data class | Fixture posture |
|---|---|
| Credentials, tokens, signed URLs, private endpoints | **DENY** |
| Real reviewer identity or internal ticket details | **DENY** |
| Real release candidate, decision, receipt, proof, or rollback reference | **DENY** |
| Living-person, DNA/genomic, archaeology, rare-species, infrastructure, or private-land detail | **DENY** unless separately transformed and explicitly approved for a public-safe fixture |
| Exact sensitive geometry | **DENY** |
| Synthetic IDs, URI-like refs, hashes, timestamps, and actor labels | Allowed when clearly marked as toy values |

A fixture accidentally containing real or restricted material must be removed from this lane, handled through the applicable quarantine or security process, and accompanied by a correction path. Do not “sanitize” it silently while preserving exposed history.

[Back to top](#top)

---

## Maintenance and review

Update this README and the affected fixture documentation when any of these change:

- required schema fields, types, enum values, closed-property rules, or conditional ID rules;
- validator entry point, runner behavior, recursion, extension discovery, or format checking;
- file naming or pairing conventions;
- fixture payloads or expected outputs;
- a new semantic, policy, evidence, review, rollback, or release-readiness consumer becomes implemented;
- CI wiring or required-check enforcement becomes verified;
- the fixture root versus `tests/fixtures/` responsibility split changes through a reviewed migration.

### Review burden

At minimum, changes should be reviewed by the maintainers responsible for the affected surfaces:

- fixture lane and parent README;
- `PromotionDecision` semantic contract;
- paired JSON Schema;
- validator/shared runner when behavior changes;
- policy, evidence, review, rollback, or release owners when new claims or consumers are introduced.

Path-specific CODEOWNERS and enforced reviewer requirements remain **NEEDS VERIFICATION**. Do not invent steward approval from repository access or fixture success.

### Maintenance rule for broader positive scenarios

When a schema-valid fixture is intended to prove more than machine shape:

1. identify the exact additional consumer;
2. add or verify the corresponding policy, semantic, evidence-resolution, review, rollback, or release-readiness test;
3. record the expected finite result;
4. place the fixture according to Directory Rules and existing fixture-home responsibilities;
5. update the parent, sibling, consumer, and verification-status documentation together;
6. avoid relabeling schema acceptance as system-level approval.

[Back to top](#top)

---

## Related paths

| Path | Relationship |
|---|---|
| [`../../../README.md`](../../../README.md) | Canonical reusable fixture-root boundaries |
| [`../../README.md`](../../README.md) | Release fixture parent and child-lane index |
| [`../README.md`](../README.md) | PromotionDecision fixture-family parent |
| [`../invalid/README.md`](../invalid/README.md) | Paired schema-negative lane |
| [`../../../../contracts/release/promotion_decision.md`](../../../../contracts/release/promotion_decision.md) | Semantic meaning and invariants |
| [`../../../../schemas/contracts/v1/release/promotion_decision.schema.json`](../../../../schemas/contracts/v1/release/promotion_decision.schema.json) | Machine-checkable shape |
| [`../../../../tools/validators/release/validate_promotion_decision.py`](../../../../tools/validators/release/validate_promotion_decision.py) | Schema validator entry point |
| [`../../../../tools/validators/_common/jsonschema_runner.py`](../../../../tools/validators/_common/jsonschema_runner.py) | Shared direct-child fixture-discovery and expectation logic |
| [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md) | Responsibility-root and fixture-sprawl placement rules |
| `../../../../policy/promotion/` | Promotion policy home when present and verified |
| `../../../../policy/release/` | Release policy home when present and verified |
| `../../../../release/` | Real release decision, manifest, correction, withdrawal, and rollback authority |
| `../../../../data/proofs/` | Canonical proof material, not fixtures |
| `../../../../data/receipts/` | Canonical process receipts, not fixtures |

### ADRs and placement

No ADR is required for this same-path documentation modernization. It adds no root, lifecycle phase, schema home, contract home, policy home, proof home, receipt home, or release home.

A future change that creates a new fixture authority, parallel schema/policy/release home, or changes the root fixture split may require an ADR or migration note under Directory Rules.

[Back to top](#top)

---

## Verification status

### CONFIRMED in this update

- Repository and base: `bartytime4life/Kansas-Frontier-Matrix` at `main@00caf13517214f487f8e05465782bcf5d01d613d`.
- Existing target blob: `12b95ac5b9f3dd16c6588e202e395f3a2f752072`.
- Release fixture parent README exists.
- PromotionDecision fixture parent README exists.
- Sibling invalid README exists and is modernized around schema-negative behavior.
- Semantic contract exists at `contracts/release/promotion_decision.md`.
- Paired schema exists at `schemas/contracts/v1/release/promotion_decision.schema.json`.
- Validator entry point exists at `tools/validators/release/validate_promotion_decision.py`.
- Shared runner reads direct-child `.json` files from `valid/` and `invalid/`.
- Current schema requires the declared fields, finite enum, closed object shapes, and hydrology ID condition.
- Current runner can return success when no fixture JSON files are discovered.
- Current runner does not pass an explicit JSON Schema format checker.

### UNKNOWN or NEEDS VERIFICATION

- Exact payload inventory and whether the valid lane currently contains any JSON files.
- Whether every payload has one verified consumer and an expected result.
- Whether schema format assertions such as `date-time` are enforced elsewhere.
- Evidence resolution, policy validity, reviewer authority, rollback readiness, release readiness, bounded-summary safety, and supersession behavior.
- CI workflow conclusions, required-check enforcement, and branch protection.
- Path-specific CODEOWNERS and separation-of-duties enforcement.
- Any public release, production parity, or KFM publication claim.

### Not run locally

- Python schema validator;
- repository Markdown lint;
- docs build or host-render validation;
- link checker;
- policy, evidence-resolution, review, rollback, release-readiness, or end-to-end tests.

No executable repository checkout was mounted for this update. Remote file reads prove repository bytes and relationships only; they do not substitute for a test run.

[Back to top](#top)

---

## Rollback

This is a documentation-only, same-path update.

Rollback options:

1. revert the update commit created for this README; or
2. restore prior blob `12b95ac5b9f3dd16c6588e202e395f3a2f752072` at `fixtures/release/promotion_decision/valid/README.md`.

Rollback changes documentation only. It does not roll back a fixture payload, schema, contract, policy, validator, release decision, manifest, proof, receipt, runtime, or publication state because none of those are changed by this update.

[Back to top](#top)
