<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-release-promotion-decision-readme
title: fixtures/release/promotion_decision/README.md — PromotionDecision Fixture Family
type: README
version: v0.2
status: draft; repository-grounded; nested-fixture-family; schema-paired; synthetic; no-network; non-authoritative
owner: NEEDS VERIFICATION — no path-specific CODEOWNERS or accepted fixture steward was inspected for this update
created: NEEDS VERIFICATION — file predates this versioned documentation contract
updated: 2026-07-24
supersedes: prior documentation at the same path; no fixture payload, contract, schema, policy, validator, release object, or runtime behavior is superseded
policy_label: repository-facing; fixtures; release; promotion-decision; synthetic; public-safe; no-network; schema-validation; non-publisher
owning_root: fixtures/
responsibility: document the paired positive and negative JSON Schema fixture lanes consumed by the current PromotionDecision validator
truth_posture: cite-or-abstain; fixture acceptance or rejection proves only the declared machine-shape check against the supplied synthetic object
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 5128df3c0b2385045bcdbecb06283a260e21d7a7
  prior_blob: 184c40ee4345b482df7a6f17c65e354e09114c7a
  directory_rules_blob: 18653c00ba193a4afaa3e07a0924452807fb98ef
  fixtures_root_readme_blob: 911c20c86d9322f38b1f59db66b922a94fd027eb
  release_fixture_readme_blob: 94b19cc0a5945947a2c1df9b2db8aba973531d86
  valid_readme_blob: a6e0fc5eb6d5f487be70ff02307e2236e7c6d01a
  invalid_readme_blob: 1a6fe6a56f8969fe0714dd273fdef5fc148d4726
  contract_blob: 42295bfc83a621cf125d33aa821912b426f70bd2
  schema_blob: a2d087a46772cf60e4b9dfb394892690e8a88b31
  validator_blob: ead33d6c5c073f319627ee42d99c5933c0e370d1
  jsonschema_runner_blob: ce05ae25d0cb6fc29a2ea41db6c65a99ca5e13e6
related:
  - ../../README.md
  - ../README.md
  - ./valid/README.md
  - ./invalid/README.md
  - ../../../contracts/release/promotion_decision.md
  - ../../../schemas/contracts/v1/release/promotion_decision.schema.json
  - ../../../tools/validators/release/validate_promotion_decision.py
  - ../../../tools/validators/_common/jsonschema_runner.py
  - ../../../docs/architecture/directory-rules.md
notes:
  - "This is a same-path Markdown modernization. It creates no sibling README, fixture payload, schema, contract, policy, validator, release object, or publication state."
  - "The current validator consumes direct-child valid/*.json and invalid/*.json files only; discovery is non-recursive."
  - "The current shared runner treats valid files as schema-positive and invalid files as schema-negative, but an empty fixture inventory can still return success."
  - "Reference resolution, policy freshness, reviewer authority, rollback usability, release readiness, supersession, bounded public projection, and publication require separate consumers and are not established by this schema-only fixture family."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `PromotionDecision` Fixture Family

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Fixture family: schema-paired](https://img.shields.io/badge/fixture%20family-schema--paired-1f6feb?style=flat-square)](#current-consumer-model)
[![Network: not required](https://img.shields.io/badge/network-not%20required-15803d?style=flat-square)](#validation)
[![Authority: non-authoritative](https://img.shields.io/badge/authority-non--authoritative-6e7781?style=flat-square)](#authority-and-boundaries)

> **One-line purpose.** `fixtures/release/promotion_decision/` organizes compact synthetic JSON objects that the current `PromotionDecision` JSON Schema validator must accept in `valid/` or reject in `invalid/`.

**Quick navigation:** [Purpose](#purpose) · [Status](#status) · [Authority](#authority-and-boundaries) · [Consumer](#current-consumer-model) · [Schema](#schema-confirmed-shape) · [Lanes](#child-lane-contract) · [Routing](#scenario-routing-matrix) · [Authoring](#authoring-contract) · [Validation](#validation) · [Failures](#failure-interpretation) · [Safety](#rights-sensitivity-and-test-data) · [Maintenance](#maintenance-and-review) · [Related](#related-paths) · [Verification](#verification-status) · [Rollback](#rollback)

> [!IMPORTANT]
> This is a **schema-fixture family**, not a complete promotion-gate simulator. The implemented consumer checks JSON Schema shape. It does not resolve evidence, execute policy, authenticate reviewers, test rollback targets, emit release manifests, prove release readiness, project a public summary, or publish anything.

> [!CAUTION]
> `APPROVE`, `DENY`, and `ABSTAIN` are all structurally valid enum values. A fixture containing `"decision": "APPROVE"` can pass the schema while the real transition remains unsupported, denied, unsafe, or nonexistent.

---

## Purpose

This directory answers two bounded questions:

1. Does the current `PromotionDecision` schema **accept** this structurally valid synthetic object?
2. Does the current `PromotionDecision` schema **reject** this deliberately schema-invalid synthetic object?

The family supports:

- positive and negative JSON Schema regression checks;
- validator dry-runs;
- documentation examples of the current machine shape;
- finite decision-enum examples for `APPROVE`, `DENY`, and `ABSTAIN`;
- focused negative cases for required fields, enums, closed properties, nested review shape, and the hydrology ID condition;
- future expected diagnostics or normalized-output snapshots when a governed golden-output convention and consumer are verified.

It does **not** exist to store actual promotion decisions, authorize lifecycle transitions, or simulate release authority.

[Back to top](#top)

---

## Status

Snapshot: `main@5128df3c0b2385045bcdbecb06283a260e21d7a7`, inspected on 2026-07-24.

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| Target README | **CONFIRMED** at prior blob `184c40ee4345b482df7a6f17c65e354e09114c7a` | Existing document is modernized in place |
| Release fixture parent | **CONFIRMED** at [`../README.md`](../README.md) | A synthetic, non-authoritative release-fixture boundary exists, although some broader scenario language remains inherited documentation debt |
| Valid child README | **CONFIRMED** at [`valid/README.md`](valid/README.md) | Direct-child positive JSON fixtures are explicitly bounded to schema acceptance |
| Invalid child README | **CONFIRMED** at [`invalid/README.md`](invalid/README.md) | Direct-child negative JSON fixtures are explicitly bounded to schema rejection |
| Semantic contract | **CONFIRMED** at [`contracts/release/promotion_decision.md`](../../../contracts/release/promotion_decision.md) | Contract defines meaning and distinguishes PromotionDecision from PolicyDecision, ReleaseManifest, RollbackCard, ReviewRecord, and public surfaces |
| Paired schema | **CONFIRMED** at [`promotion_decision.schema.json`](../../../schemas/contracts/v1/release/promotion_decision.schema.json); schema status is `PROPOSED` | Required fields, finite enum, closed properties, nested review shape, and hydrology ID condition are machine-declared |
| Validator entry point | **CONFIRMED** at [`validate_promotion_decision.py`](../../../tools/validators/release/validate_promotion_decision.py) | Validator binds the paired schema to this fixture root |
| Shared runner | **CONFIRMED** at [`jsonschema_runner.py`](../../../tools/validators/_common/jsonschema_runner.py) | `--fixtures` reads direct-child `valid/*.json` and `invalid/*.json` and enforces positive/negative schema expectations |
| Fixture payload inventory | **UNKNOWN** | No exhaustive child-file listing or payload-by-payload review was available in this update |
| Evidence, policy, review, rollback, and release-readiness enforcement | **NEEDS VERIFICATION / not established by the schema runner** | Current evidence supports machine-shape validation only |
| CI and branch-protection enforcement | **NEEDS VERIFICATION** | Workflow or file presence does not prove required-check enforcement |
| Release or publication state | **DENIED as inference** | Fixtures and validation results cannot establish KFM publication |

### Material corrections in this revision

- Replaces the stale statement that `fixtures/release/README.md` was absent.
- Replaces conditional “if present” wording for the contract, schema, validator, and child lanes with pinned repository evidence.
- Narrows the family from broad promotion-gate behavior to the positive/negative JSON Schema behavior the current runner actually enforces.
- Documents non-recursive discovery, `.json`-only inclusion, empty-inventory success, and the missing explicit format checker.
- Separates non-empty reference fields from actual evidence, policy, review, rollback, or release closure.
- Removes supersession and bounded-public-summary cases from the current schema-fixture claim because the current schema has no fields for either concern.
- Records the malformed-JSON hazard in the shared runner’s second expectation pass.

[Back to top](#top)

---

## Authority and boundaries

| Responsibility | Authority home | Role of this fixture family |
|---|---|---|
| `PromotionDecision` meaning | [`contracts/release/promotion_decision.md`](../../../contracts/release/promotion_decision.md) | Supplies examples; never redefines semantics |
| Machine-checkable shape | [`schemas/contracts/v1/release/promotion_decision.schema.json`](../../../schemas/contracts/v1/release/promotion_decision.schema.json) | Exercises acceptance and rejection; never becomes schema authority |
| Schema validation implementation | [`tools/validators/release/validate_promotion_decision.py`](../../../tools/validators/release/validate_promotion_decision.py) and the shared runner | Supplies deterministic inputs; never becomes validator authority |
| Policy admissibility | `policy/promotion/` and `policy/release/` when implemented and verified | May later supply policy-test inputs; never decides policy |
| Evidence resolution | Evidence resolvers and `EvidenceBundle` authorities | Reference strings here are synthetic and are not dereferenced by the schema runner |
| Review authority | Review records, policy, CODEOWNERS, or another governed review surface | `review.reviewer` and `review.ticket` are shape fields only |
| Rollback readiness | `RollbackCard`, release policy, and rollback tooling | `rollback_card_uri` is checked only as a non-empty string |
| Release decisions and manifests | `release/` | Must never store or authorize real release state |
| Receipts and proofs | `data/receipts/` and `data/proofs/` | Must never store canonical process or evidence objects |
| Public surfaces | Governed APIs and released artifacts | Direct fixture serving is denied |

Directory Rules place this family under `fixtures/` because its primary responsibility is reusable synthetic checking input. This same-path README update creates no new root, lifecycle phase, schema home, contract home, policy home, release home, or authority surface.

### Explicit non-scope

Do not place any of the following here:

- actual `PromotionDecision`, `ReleaseManifest`, `RollbackCard`, `ReviewRecord`, or `PolicyDecision` records;
- real EvidenceBundles, EvidenceRefs, SourceDescriptors, receipts, proofs, attestations, or release artifacts;
- implementation code, policy rules, schemas, contracts, workflow output, runtime output, or published data;
- credentials, signed URLs, private ticket data, real reviewer identities, restricted policy context, or sensitive source/location data;
- schema-valid semantic or policy cases unless a separate consumer and expected outcome are explicitly identified.

[Back to top](#top)

---

## Current consumer model

The validator entry point is a thin binding:

```text
tools/validators/release/validate_promotion_decision.py
  -> schemas/contracts/v1/release/promotion_decision.schema.json
  -> fixtures/release/promotion_decision/
  -> tools/validators/_common/jsonschema_runner.py
```

With `--fixtures`, the shared runner discovers:

```text
fixtures/release/promotion_decision/
├── valid/*.json
└── invalid/*.json
```

Current implementation properties:

- discovery is **non-recursive**;
- only direct-child files ending in `.json` are included;
- README, YAML, JSONL, nested directories, and other extensions are ignored by `--fixtures`;
- every discovered `valid/*.json` file must produce zero schema errors;
- every discovered `invalid/*.json` file must produce at least one schema error;
- an empty valid/invalid inventory can return exit code `0`, so zero exit alone does not prove coverage exists;
- the validator uses `Draft202012Validator` without an explicit format checker, so this README does not claim that `format: date-time` is enforced;
- the runner reads discovered files once for general validation and again for lane expectation checks;
- malformed JSON may be caught during the first pass but then raise during the second expectation pass, so stable fixtures should remain syntactically valid JSON.

> [!WARNING]
> Keep `invalid/*.json` **parseable JSON**. Deliberate syntax errors are not reliable schema-negative fixtures under the current two-pass runner and can produce an operational traceback instead of a bounded expected rejection.

### Direct-file mode

Without `--fixtures`, the runner accepts explicit file paths:

```bash
python tools/validators/release/validate_promotion_decision.py path/to/object.json
```

Direct-file mode reports schema validity only. It does not know whether the file was intended to be positive or negative. Calling the command without a file and without `--fixtures` returns the runner’s “No files provided” error path.

[Back to top](#top)

---

## Schema-confirmed shape

The paired schema currently requires exactly these root fields and rejects additional root properties.

| Field | Schema rule | What the current runner proves | What it does not prove |
|---|---|---|---|
| `id` | non-empty string; hydrology condition applies | String and conditional pattern shape | Deterministic identity, uniqueness, registration, or resolvability |
| `version` | exactly `v1` | Constant value | Migration support or compatibility policy |
| `domain` | non-empty string | String presence | Accepted domain registry membership |
| `run_id` | non-empty string | String presence | Run existence or integrity |
| `decision` | `APPROVE`, `DENY`, or `ABSTAIN` | Enum membership | Correctness or authority of the decision |
| `evidence_ref` | non-empty string | String presence | Evidence resolution or admissibility |
| `evidence_bundle_uri` | non-empty string | String presence | EvidenceBundle existence, closure, or release state |
| `rollback_card_uri` | non-empty string | String presence | RollbackCard existence or operational readiness |
| `policy_bundle` | non-empty string | String presence | Policy bundle existence, version, freshness, hash, or decision result |
| `decided_at` | string with declared `date-time` format | String type; format enforcement is **NEEDS VERIFICATION** | Freshness, UTC policy, ordering, or audit integrity |
| `review` | object requiring `reviewer` and `ticket`; no extra properties | Nested shape and non-empty strings | Reviewer identity, authority, independence, ticket existence, or approval |

### Hydrology condition

When `domain` is exactly `hydrology`, `id` must match:

```text
^promo:hydrology:[A-Za-z0-9._:-]+$
```

No equivalent domain-specific ID pattern is currently declared for other domain values in this schema.

### Closed shape

The schema sets `additionalProperties: false` at the root and inside `review`. Therefore fields such as these are not part of the current object shape:

- `supersedes`;
- `public_summary`;
- `release_manifest_uri`;
- `proof_pack_uri`;
- `reason_codes`;
- `policy_decision_uri`;
- `correction_notice_uri`.

Adding one of those fields to a fixture should currently make it schema-invalid. A future contract/schema revision may introduce separate objects or versioned fields, but this README does not predict that design.

[Back to top](#top)

---

## Child lane contract

| Lane | Required expectation | Appropriate cases | Inappropriate cases |
|---|---|---|---|
| [`valid/`](valid/README.md) | Every direct-child `*.json` object produces zero schema errors | Complete required shape, any admitted decision enum, hydrology ID positive case, closed review object | “Evidence resolved,” “policy approved,” “review authorized,” “rollback ready,” or “release ready” unless a separate consumer proves it |
| [`invalid/`](invalid/README.md) | Every direct-child `*.json` object produces at least one schema error | Missing required field, wrong enum/const/type, empty required string, extra property, invalid hydrology ID, invalid review shape | Schema-valid policy denial, stale policy, unresolved reference, unauthorized reviewer, unusable rollback target, unsafe release candidate |

### Pairing rule

Pair positive and negative cases when the relationship is stable and focused. Example:

```text
valid/hydrology-approve-shape.json
invalid/hydrology-invalid-id.json
```

The pair demonstrates a machine-shape boundary only. It does not create a real decision pair or promotion record.

[Back to top](#top)

---

## Scenario routing matrix

| Scenario | Current lane or authority | Current expected check |
|---|---|---|
| All required fields, admitted enum, no extra properties | `valid/` | Schema accepts |
| Missing `evidence_ref` | `invalid/` | Schema rejects missing required field |
| Non-empty but unresolvable `evidence_ref` | Separate evidence-resolution fixture/test | Not checked by current schema runner |
| Missing `rollback_card_uri` | `invalid/` | Schema rejects missing required field |
| Non-empty but unusable rollback URI | Separate rollback-readiness fixture/test | Not checked by current schema runner |
| Missing `review.ticket` | `invalid/` | Schema rejects nested required field |
| Reviewer field present but actor is unauthorized or not independent | Separate review/separation-of-duties test | Not checked by current schema runner |
| `policy_bundle` missing or empty | `invalid/` | Schema rejects |
| Policy bundle non-empty but stale, unknown, or denies transition | Separate policy fixture/test | Not checked by current schema runner |
| `decision` is `APPROVE`, `DENY`, or `ABSTAIN` | `valid/` when the rest of shape is valid | Schema accepts enum member |
| `decision` uses another value | `invalid/` | Schema rejects enum violation |
| Hydrology ID matches required pattern | `valid/` | Schema accepts conditional pattern |
| Hydrology ID violates required pattern | `invalid/` | Schema rejects conditional pattern |
| Non-hydrology domain uses a project-specific invalid ID | Separate identity/domain-registry test unless another schema rule exists | Not checked by this schema |
| Extra `supersedes` field | `invalid/` under current schema | Schema rejects additional property |
| Supersession relationship between two decisions | Separate release-history/correction object and test | Current schema has no supersession field |
| Bounded public summary | Separate projection contract/schema/fixture | Current schema has no public-summary field |
| Malformed JSON syntax | Avoid as a stable fixture | May trigger operational exception rather than bounded expectation result |
| No JSON files in either child lane | Coverage failure concept, but not currently enforced | `--fixtures` can return success |

[Back to top](#top)

---

## Authoring contract

Every fixture in this family should be:

- **synthetic** — no real decision, evidence, policy, review, ticket, source, or release data;
- **parseable JSON** — even in `invalid/`;
- **minimal** — include only what is needed to demonstrate the intended shape boundary;
- **deterministic** — no live endpoint, clock, randomness, model, network, or secret dependency;
- **public-safe** — no sensitive exact geometry, living-person data, private infrastructure, or restricted identifiers;
- **direct-child** — place consumed JSON files directly under `valid/` or `invalid/` for the current runner;
- **single-purpose where practical** — isolate one primary invalid condition per negative fixture;
- **self-describing** — name communicates object, posture, and expected result;
- **consumer-bound** — document the schema, validator, test, or example that uses it;
- **proof-bounded** — state what a pass proves and explicitly what it does not prove.

### Recommended naming

Use descriptive kebab-case names such as:

```text
valid/approve-minimal-shape.json
valid/deny-minimal-shape.json
valid/abstain-minimal-shape.json
valid/hydrology-valid-id.json
invalid/missing-evidence-ref.json
invalid/invalid-decision-enum.json
invalid/extra-root-property.json
invalid/review-missing-ticket.json
invalid/hydrology-invalid-id.json
```

Names are documentation aids. The current runner discovers by directory and `.json` suffix, not by semantic filename pattern.

### Synthetic reference posture

Use obvious toy reference values, for example:

```text
evidence_ref       = ev:toy:001
evidence_bundle_uri = kfm://evidence-bundle/toy-001
rollback_card_uri   = kfm://rollback-card/toy-001
policy_bundle       = policy:toy:v1
review.reviewer     = reviewer:toy
review.ticket       = ticket:toy-001
```

These strings satisfy shape when non-empty. They must never be presented as resolvable or authoritative unless a separate fixture and consumer explicitly establishes that behavior.

[Back to top](#top)

---

## Validation

### Fixture-family command

From the repository root:

```bash
python tools/validators/release/validate_promotion_decision.py --fixtures
```

Expected bounded behavior:

- exit `0` when every discovered valid fixture is schema-valid and every discovered invalid fixture is schema-invalid;
- nonzero when a discovered valid fixture has schema errors, an invalid fixture has no schema errors, or an operational read/parse failure occurs;
- **zero fixtures may still yield exit `0`**, so reviewers must confirm inventory separately;
- no evidence, policy, review-authority, rollback, release-readiness, or publication check is implied.

### Direct-file command

```bash
python tools/validators/release/validate_promotion_decision.py \
  fixtures/release/promotion_decision/valid/<fixture>.json
```

This checks schema validity only. Direct-file mode does not apply valid/invalid lane expectation semantics.

### Suggested repository checks

Where available in a mounted checkout, also run the repository’s Markdown lint, link checker, docs build, and relevant aggregate validator commands. Record the exact commands and results in the pull request rather than claiming generic validation.

### What a passing run proves

A passing fixture-family run proves only that:

- each discovered `valid/*.json` file satisfies the current schema as executed by the current runner; and
- each discovered `invalid/*.json` file produces at least one current schema error.

It does not prove:

- fixture inventory completeness;
- `date-time` format enforcement;
- evidence reference resolution;
- EvidenceBundle closure;
- policy bundle existence or result;
- reviewer identity, authority, or separation of duties;
- rollback-card existence or executable rollback;
- release-manifest or proof-pack closure;
- release readiness, promotion, deployment, serving, or publication;
- CI required-check or branch-protection enforcement.

[Back to top](#top)

---

## Failure interpretation

| Observation | Safe interpretation | Unsafe interpretation |
|---|---|---|
| Valid fixture is rejected | Schema, fixture, resolver, or runner compatibility needs investigation | “The release was denied” |
| Invalid fixture is accepted | The negative case no longer violates the current schema or the fixture is misclassified | “Policy allowed the unsafe transition” |
| Command exits `0` with no discovered fixtures | Runner completed without discovering a contradiction | “Fixture coverage is complete” |
| `APPROVE` fixture passes | The object shape admits the `APPROVE` enum value | “The candidate is approved or publishable” |
| `DENY` fixture passes | The object shape admits the `DENY` enum value | “A real policy denial occurred” |
| Reference strings are accepted | Required strings are non-empty | “Evidence, policy, review, or rollback resolved” |
| Malformed JSON crashes or traces | Operational handling gap or unsuitable fixture design | “Expected schema rejection passed cleanly” |
| Workflow is green | That workflow completed its configured checks for that revision | “KFM publication or production parity is proven” |

When results conflict with the README, contract, or schema, preserve the evidence and classify the conflict. Do not silently change a fixture merely to restore green status.

[Back to top](#top)

---

## Rights, sensitivity, and test data

Fixtures should be safe to keep in a public repository.

Use:

- invented identifiers and names;
- synthetic URIs and hashes;
- fixed toy timestamps;
- generalized or nonexistent geometry if geometry is ever introduced by a future object version;
- no-network and no-secret assumptions.

Do not use:

- real reviewer identities or internal ticket contents;
- real evidence excerpts, signed attestations, release credentials, or restricted policy bundles;
- living-person, DNA/genomic, rare-species, archaeology, cultural, private-land, or precise infrastructure data;
- production URLs, signed URLs, access tokens, API keys, or internal hostnames;
- actual release or rollback records disguised as examples.

If real or sensitive material is discovered here, stop treating it as a fixture, remove it from the public checking path, use the appropriate security or governed quarantine process, and record the correction path.

[Back to top](#top)

---

## Maintenance and review

Update this README and the affected child README when any of these change:

- the `PromotionDecision` semantic contract;
- the paired schema version, fields, conditional rules, or `x-kfm` bindings;
- validator entry point or shared-runner behavior;
- fixture discovery depth, extension rules, or empty-inventory behavior;
- explicit format-checker configuration;
- child-lane names or fixture naming conventions;
- implemented policy, evidence-resolution, review, rollback, release-readiness, projection, or supersession consumers;
- golden-output conventions;
- repository validation commands or CI wiring.

### Review checklist

- [ ] Fixture is synthetic, parseable, deterministic, and public-safe.
- [ ] File is a direct-child `.json` under the correct current lane.
- [ ] Valid fixture has zero expected schema errors.
- [ ] Invalid fixture has at least one intended schema error.
- [ ] Negative case isolates one primary condition where practical.
- [ ] Claimed behavior matches the current schema and runner.
- [ ] Semantic or policy claims name a separate implemented consumer.
- [ ] No real release, evidence, reviewer, ticket, policy, proof, receipt, or sensitive data is present.
- [ ] Passing results are described with bounded proof language.
- [ ] Parent and child documentation remain aligned.

### Documentation debt outside this one-file scope

The current [`fixtures/release/README.md`](../README.md) still uses broader policy-pass, release-readiness, evidence-resolution, review-ready, supersession, and bounded-summary vocabulary for this family. Until that parent is modernized, this README and the child-lane READMEs provide the narrower repository-grounded consumer boundary.

The semantic contract also retains verification notes that predate the confirmed validator file. This README confirms file presence and binding, but it does not claim workflow enforcement or amend contract authority.

[Back to top](#top)

---

## Related paths

| Path | Relationship |
|---|---|
| [`../../README.md`](../../README.md) | Canonical reusable fixture-root rules |
| [`../README.md`](../README.md) | Release fixture parent index |
| [`valid/README.md`](valid/README.md) | Schema-positive child-lane contract |
| [`invalid/README.md`](invalid/README.md) | Schema-negative child-lane contract |
| [`../../../contracts/release/promotion_decision.md`](../../../contracts/release/promotion_decision.md) | Semantic meaning and invariants |
| [`../../../contracts/release/README.md`](../../../contracts/release/README.md) | Release contract-family boundary |
| [`../../../schemas/contracts/v1/release/promotion_decision.schema.json`](../../../schemas/contracts/v1/release/promotion_decision.schema.json) | Current paired machine shape |
| [`../../../tools/validators/release/validate_promotion_decision.py`](../../../tools/validators/release/validate_promotion_decision.py) | Validator entry point |
| [`../../../tools/validators/_common/jsonschema_runner.py`](../../../tools/validators/_common/jsonschema_runner.py) | Shared discovery and expectation runner |
| `../../../policy/promotion/` | Promotion policy authority when implementation and tests are verified |
| `../../../policy/release/` | Release policy authority when implementation and tests are verified |
| `../../../release/` | Release decisions, manifests, corrections, and rollback authority |
| `../../../data/proofs/` | Canonical proof objects, not fixture material |
| `../../../data/receipts/` | Canonical process receipts, not fixture material |
| [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md) | Placement and anti-drift doctrine |

[Back to top](#top)

---

## Verification status

| Check | Result |
|---|---|
| Target path and prior bytes | **CONFIRMED** at `main@5128df3c0b2385045bcdbecb06283a260e21d7a7`, blob `184c40ee4345b482df7a6f17c65e354e09114c7a` |
| Same-path update | **PASS** — no sibling README or path move |
| Release fixture parent presence | **CONFIRMED** |
| Valid child README | **CONFIRMED** at blob `a6e0fc5eb6d5f487be70ff02307e2236e7c6d01a` |
| Invalid child README | **CONFIRMED** at blob `1a6fe6a56f8969fe0714dd273fdef5fc148d4726` |
| Contract presence | **CONFIRMED** at blob `42295bfc83a621cf125d33aa821912b426f70bd2` |
| Schema pairing and field surface | **CONFIRMED** at blob `a2d087a46772cf60e4b9dfb394892690e8a88b31`; schema status remains `PROPOSED` |
| Validator binding | **CONFIRMED** at blob `ead33d6c5c073f319627ee42d99c5933c0e370d1` |
| Shared-runner behavior | **CONFIRMED by source inspection** at blob `ce05ae25d0cb6fc29a2ea41db6c65a99ca5e13e6` |
| Exhaustive fixture payload inventory | **UNKNOWN / not performed** |
| Python validator execution | **NOT RUN locally** — no executable checkout mounted |
| Markdown lint, docs build, and link checker | **NOT RUN locally** |
| Policy/evidence/review/rollback/release tests | **NOT RUN / not established by current consumer** |
| CI required-check enforcement | **NEEDS VERIFICATION** |
| Release or publication | **NOT CLAIMED** |

### Not run locally

No executable repository checkout was mounted for this update. Remote file reads prove repository bytes and relationships only; they do not substitute for a validator, documentation build, link check, policy test, release dry-run, or end-to-end run.

[Back to top](#top)

---

## Rollback

This is a documentation-only, same-path update.

Rollback options:

1. revert the update commit created for this README; or
2. restore prior blob `184c40ee4345b482df7a6f17c65e354e09114c7a` at `fixtures/release/promotion_decision/README.md`.

Rollback changes documentation only. It does not roll back a fixture payload, schema, contract, policy, validator, release decision, manifest, proof, receipt, runtime, or publication state because none of those are changed by this update.

[Back to top](#top)
