<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-release-readme
title: fixtures/release/README.md — Release Fixture Families
class: README
version: v0.2
status: draft; repository-grounded; nested-fixture-parent; mixed-maturity; synthetic; no-network-default; non-authoritative
owner: NEEDS VERIFICATION — no path-specific CODEOWNERS rule or accepted release-fixture steward was inspected for this update
created: NEEDS VERIFICATION — file predates this versioned documentation contract
updated: 2026-07-24
supersedes: prior documentation at the same path; no fixture payload, contract, schema, policy, validator, release object, or runtime behavior is superseded
policy_label: repository-facing; fixtures; release; synthetic; public-safe; no-network-default; correction-aware; rollback-aware; non-publisher
owning_root: fixtures/
responsibility: index reusable release-governance fixture families and route each scenario to a verified schema, policy, validator, test, release dry-run, or explicitly future consumer
truth_posture: cite-or-abstain; a release fixture result proves only the declared consumer and expected condition, never release authority, evidence closure, policy approval, reviewer authority, rollback execution, publication, or production parity
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: d38b2886d1786eeaf0e8ec1f1ab83da5f0c93b3a
  prior_blob: 94b19cc0a5945947a2c1df9b2db8aba973531d86
  directory_rules_blob: 18653c00ba193a4afaa3e07a0924452807fb98ef
  fixtures_root_readme_blob: 911c20c86d9322f38b1f59db66b922a94fd027eb
  release_contract_readme_blob: 3412cb63cfde542cf9a7c8e93e035530569425d8
  promotion_fixture_readme_blob: 6f934bd5c28ebfc7f5535a980fae3d0fd05c09a5
  promotion_valid_readme_blob: a6e0fc5eb6d5f487be70ff02307e2236e7c6d01a
  promotion_invalid_readme_blob: 1a6fe6a56f8969fe0714dd273fdef5fc148d4726
  promotion_contract_blob: 42295bfc83a621cf125d33aa821912b426f70bd2
  promotion_schema_blob: a2d087a46772cf60e4b9dfb394892690e8a88b31
  promotion_validator_blob: ead33d6c5c073f319627ee42d99c5933c0e370d1
  jsonschema_runner_blob: ce05ae25d0cb6fc29a2ea41db6c65a99ca5e13e6
related:
  - ../README.md
  - ./promotion_decision/README.md
  - ./promotion_decision/valid/README.md
  - ./promotion_decision/invalid/README.md
  - ../../contracts/release/README.md
  - ../../contracts/release/promotion_decision.md
  - ../../schemas/contracts/v1/release/
  - ../../policy/release/
  - ../../policy/promotion/
  - ../../release/
  - ../../data/proofs/
  - ../../data/receipts/
  - ../../docs/architecture/directory-rules.md
notes:
  - "This is a same-path Markdown modernization. It creates no sibling README, fixture payload, schema, contract, policy, validator, release object, or publication state."
  - "PromotionDecision is the only release-fixture family whose schema, validator binding, and valid/invalid child-lane contracts were verified in this update."
  - "The current PromotionDecision consumer is a JSON Schema runner, not a complete promotion gate."
  - "Other release object families remain PROPOSED or NEEDS VERIFICATION until their contracts, schemas, consumers, fixtures, and expected outcomes are inspected together."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `fixtures/release/` — Release Fixture Families

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Scope: release fixture parent](https://img.shields.io/badge/scope-release%20fixture%20parent-1f6feb?style=flat-square)](#purpose)
[![Network: denied by default](https://img.shields.io/badge/network-denied%20by%20default-15803d?style=flat-square)](#validation)
[![Authority: non-authoritative](https://img.shields.io/badge/authority-non--authoritative-6e7781?style=flat-square)](#authority-level)

> **One-line purpose.** `fixtures/release/` indexes compact, deterministic, synthetic or public-safe examples used to exercise explicitly named release-governance contracts and consumers without turning the fixture tree into release, policy, evidence, review, proof, rollback, or publication authority.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Verified lanes](#verified-child-lanes) · [Routing](#scenario-routing-matrix) · [Belongs](#what-belongs-here) · [Does not belong](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Failures](#failure-interpretation) · [Safety](#rights-sensitivity-and-test-data) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Verification](#verification-status) · [Rollback](#rollback) · [Last reviewed](#last-reviewed)

> [!IMPORTANT]
> This directory is a **fixture-family index**, not a release simulator. A release fixture may demonstrate machine shape, a denial path, an expected diagnostic, a correction case, or a rollback condition only when a named consumer actually checks that condition. Documentation alone does not create that consumer.

> [!CAUTION]
> A fixture named `approve`, `release-ready`, `rollback-ready`, or `public-safe` does not make those statements true. The expected result must be bound to an implemented schema, policy, validator, test, dry-run, or projection check. Otherwise the scenario remains **PROPOSED** or **NEEDS VERIFICATION**.

---

## Purpose

`fixtures/release/` is the reusable-fixture lane for release-governance object families. It answers one organizing question:

> Which compact synthetic input or expected output belongs to a release-governance check, and which verified consumer owns the result?

This parent README exists to:

- index verified release-fixture families;
- distinguish current executable coverage from proposed future coverage;
- route schema, policy, evidence, review, rollback, correction, withdrawal, projection, and publication scenarios to the correct responsibility surface;
- keep fixture data synthetic, deterministic, public-safe, and no-network by default;
- prevent fixture names or passing checks from being mistaken for release authority;
- keep contracts, schemas, policy, validators, tests, proofs, receipts, release artifacts, and published outputs in their own authority homes.

The durable release truth is not a fixture. It is the governed chain of evidence, policy, review, validation, proof, manifest, promotion, correction, and rollback objects required by the release process.

[Back to top](#top)

---

## Authority level

| Field | Authority |
|---|---|
| **Directory class** | Nested reusable-fixture parent under the canonical `fixtures/` root |
| **Primary responsibility** | Index and bound synthetic release-governance fixture families |
| **May own** | Family READMEs, compact synthetic inputs, explicit valid/invalid examples, deterministic expected outputs, authoring notes, and consumer bindings |
| **Must not own** | Release object semantics, schemas, policy, actual release records, real evidence, review approvals, proofs, receipts, signed attestations, rollback execution, runtime authority, or published artifacts |
| **Network posture** | Denied by default; live release-service, signer, registry, storage, API, or model calls require a separately governed integration workflow |
| **Public-path posture** | DENY direct public use; public clients consume governed APIs and released artifacts, never fixture paths |
| **Truth posture** | A fixture result supports only its declared consumer and expected condition |

### Responsibility boundary

| Responsibility | Authority home | Role of `fixtures/release/` |
|---|---|---|
| Release object meaning | [`contracts/release/`](../../contracts/release/README.md) | Supply examples; never redefine semantics |
| Machine-checkable shape | `schemas/contracts/v1/release/` | Supply positive and negative inputs; never become schema authority |
| Release and promotion policy | `policy/release/`, `policy/promotion/`, and related policy roots | Supply reviewed test inputs when a policy consumer exists; never approve release |
| Reusable validators | `tools/validators/`, release tools, or another repo-confirmed implementation home | Supply deterministic inputs and expected diagnostics |
| Authored enforceability proof | `tests/` and workflow checks | Be consumed by tests; never substitute for assertions or required-check enforcement |
| Evidence resolution | Evidence resolvers, `EvidenceRef`, and `EvidenceBundle` authorities | Use toy references only; never claim resolution without a consumer |
| Review authority | Review records, policy, CODEOWNERS, and governed review surfaces | Use toy reviewer/ticket fields only; never authenticate or approve a reviewer |
| Release decisions and manifests | [`release/`](../../release/) | Never store or authorize real release state |
| Proofs and receipts | [`data/proofs/`](../../data/proofs/) and [`data/receipts/`](../../data/receipts/) | Never store canonical proof or process memory |
| Published artifacts | `data/published/` and governed delivery surfaces | Never serve fixtures as public products |

Directory Rules place this lane under `fixtures/` because its primary responsibility is reusable synthetic checking material. This same-path README update creates no root, lifecycle phase, schema home, contract home, policy home, release home, or parallel authority.

[Back to top](#top)

---

## Status

Snapshot: `main@d38b2886d1786eeaf0e8ec1f1ab83da5f0c93b3a`, inspected on 2026-07-24.

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| Target README | **CONFIRMED** at prior blob `94b19cc0a5945947a2c1df9b2db8aba973531d86` | Existing document is modernized in place |
| Root fixture contract | **CONFIRMED** at [`../README.md`](../README.md) | Reusable fixtures are distinct from `tests/fixtures/`, lifecycle data, artifacts, and authority roots |
| Release semantic contracts | **CONFIRMED** at [`contracts/release/README.md`](../../contracts/release/README.md) | Release contracts define meaning and explicitly do not store or execute releases |
| PromotionDecision fixture family | **CONFIRMED** at [`promotion_decision/README.md`](promotion_decision/README.md) | Current verified release-fixture family is schema-paired and bounded to machine-shape checks |
| PromotionDecision valid lane | **CONFIRMED** at [`promotion_decision/valid/README.md`](promotion_decision/valid/README.md) | Direct-child `valid/*.json` files are schema-positive inputs |
| PromotionDecision invalid lane | **CONFIRMED** at [`promotion_decision/invalid/README.md`](promotion_decision/invalid/README.md) | Direct-child `invalid/*.json` files are schema-negative inputs |
| PromotionDecision schema and validator | **CONFIRMED** | Paired schema, validator entry point, and shared runner are present and inspected |
| Other release fixture families | **UNKNOWN / not verified** | No claim is made that ReleaseManifest, RollbackCard, WithdrawalNotice, CorrectionNotice, proof, receipt, or publication fixture families exist here |
| Exact recursive lane inventory | **UNKNOWN / not performed** | Verified navigation is not an exhaustive repository tree listing |
| Fixture payload inventory | **UNKNOWN / not performed** | No payload-by-payload review is claimed |
| Policy, evidence, review, rollback, release-readiness, correction, or withdrawal enforcement | **NEEDS VERIFICATION** | The confirmed PromotionDecision consumer establishes JSON Schema behavior only |
| CI and branch-protection enforcement | **NEEDS VERIFICATION** | Workflow presence and individual runs do not prove required-check policy |
| Release or publication state | **DENIED as inference** | Fixture presence or success cannot establish KFM publication |

### Material corrections in this revision

- Replaces broad language suggesting that one fixture family currently exercises the full release-governance surface.
- Aligns this parent with the modernized PromotionDecision parent, valid, and invalid READMEs.
- Makes `PromotionDecision` the only **verified current** release-fixture family in this documentation pass.
- Separates current JSON Schema coverage from policy, evidence-resolution, reviewer-authority, rollback-readiness, release-readiness, correction, withdrawal, supersession, bounded-projection, proof, receipt, and publication checks.
- Clarifies that payload files should normally live in a named family lane with a documented consumer rather than directly in this parent directory.
- Replaces conditional “if present” wording for verified PromotionDecision surfaces with pinned repository evidence.
- Adds scenario routing, family-admission criteria, no-network posture, proof limits, and a bounded rollback path.

[Back to top](#top)

---

## Verified child lanes

The following lanes are confirmed in this update. This is a documentation index, not an exhaustive recursive tree listing.

| Lane | Verified responsibility | Current consumer boundary |
|---|---|---|
| [`promotion_decision/`](promotion_decision/README.md) | Parent for paired positive and negative `PromotionDecision` schema fixtures | JSON Schema validation only |
| [`promotion_decision/valid/`](promotion_decision/valid/README.md) | Structurally valid synthetic `PromotionDecision` objects | Each direct-child `.json` must produce zero schema errors |
| [`promotion_decision/invalid/`](promotion_decision/invalid/README.md) | Deliberately schema-invalid synthetic `PromotionDecision` objects | Each direct-child `.json` must produce at least one schema error |

### Current PromotionDecision consumer

```text
tools/validators/release/validate_promotion_decision.py
  -> schemas/contracts/v1/release/promotion_decision.schema.json
  -> fixtures/release/promotion_decision/
  -> tools/validators/_common/jsonschema_runner.py
```

Current `--fixtures` discovery:

```text
fixtures/release/promotion_decision/
├── valid/*.json
└── invalid/*.json
```

Important limits:

- discovery is non-recursive;
- only direct-child `.json` files are included;
- an empty valid/invalid inventory can return exit code `0`;
- the runner does not pass an explicit format checker, so `format: date-time` enforcement is not claimed;
- malformed JSON is not a clean stable negative-fixture pattern for `--fixtures` because the second expectation pass may raise;
- non-empty reference strings are not dereferenced;
- policy, reviewer, rollback, release, correction, supersession, proof, receipt, and public-projection behavior are not evaluated.

[Back to top](#top)

---

## Scenario routing matrix

A scenario belongs here only when its owning consumer and expected result are explicit.

| Scenario | Current or proposed home | Required consumer | Current status |
|---|---|---|---|
| Structurally valid `PromotionDecision` | `promotion_decision/valid/` | PromotionDecision JSON Schema runner | **CONFIRMED** |
| Structurally invalid `PromotionDecision` | `promotion_decision/invalid/` | PromotionDecision JSON Schema runner | **CONFIRMED** |
| Unresolvable evidence reference with schema-valid strings | Evidence-resolution test lane or a future consumer-bound child lane | Evidence resolver | **NEEDS VERIFICATION** |
| Stale, unknown, or disallowed policy bundle | Policy fixtures/tests or a future consumer-bound child lane | Promotion/release policy engine | **NEEDS VERIFICATION** |
| Reviewer fields present but actor lacks authority | Review/policy test lane | Review authority or separation-of-duties check | **NEEDS VERIFICATION** |
| Rollback URI present but target is missing or unusable | Rollback fixtures/tests | Rollback validator or drill | **NEEDS VERIFICATION** |
| Candidate is schema-valid but not release-ready | Release-readiness test or dry-run lane | Promotion/release gate | **NEEDS VERIFICATION** |
| ReleaseManifest machine shape | Future family only after contract/schema/consumer verification | ReleaseManifest validator | **UNKNOWN / PROPOSED** |
| RollbackCard machine shape or execution case | Future family only after contract/schema/consumer verification | Rollback validator or drill | **UNKNOWN / PROPOSED** |
| WithdrawalNotice or CorrectionNotice case | Future family only after authority and placement verification | Correction/withdrawal validator and policy | **UNKNOWN / PROPOSED** |
| Proof-pack or receipt closure case | Proof/receipt-specific fixture or test lane | Proof/receipt validator | **NEEDS VERIFICATION** |
| Bounded public release summary | Public-projection fixture/test lane | Governed projection validator | **NEEDS VERIFICATION** |
| Supersession history | Object-specific fixture/test lane after schema/contract support exists | Supersession/correction validator | **NEEDS VERIFICATION** |
| Malformed JSON/parser failure | Parser-specific test or explicit direct-file invocation | Parser/error-path test | **NEEDS VERIFICATION** for stable `--fixtures` use |
| Actual release, correction, rollback, or publication | Not a fixture lane | Governed release process | **DENY** |

> [!NOTE]
> A future child directory is not admitted merely because a scenario is desirable. First verify or create the semantic contract, machine schema, consumer, expected outcome, and maintenance owner. Then add the smallest fixture lane and update this index in the same reviewed change.

[Back to top](#top)

---

## What belongs here

This parent lane may contain:

- this index README;
- named child directories for release object families whose responsibility and consumer are documented;
- compact synthetic or public-safe examples inside those family lanes;
- valid, invalid, deny, abstain, hold, stale, correction, withdrawal, rollback, and expected-output cases **only when the named consumer checks that condition**;
- deterministic expected diagnostics or normalized outputs paired with stable inputs;
- family-level metadata and authoring notes that identify contract, schema, consumer, expected outcome, rights posture, sensitivity posture, and generation method;
- small documentation examples that remain clearly synthetic and non-authoritative.

### Parent-root payload rule

Payload files should normally live inside a named object-family lane, not directly beside this README. A direct payload at `fixtures/release/` requires an explicit cross-family consumer and documented reason. Do not create an unscoped catch-all collection of “release examples.”

### Admitting a new release-fixture family

Before adding a child family, verify:

1. **Object meaning** — a contract or accepted semantic authority identifies the object.
2. **Machine shape or explicit non-schema role** — a schema exists, or the fixture is clearly bound to another consumer.
3. **Consumer** — validator, policy test, release dry-run, parser, projection check, or other executable consumer is named.
4. **Expected result** — pass, reject, deny, abstain, hold, error, correction, rollback, or snapshot is explicit.
5. **Placement** — the family belongs under `fixtures/release/` rather than `tests/fixtures/`, `release/`, `data/`, `policy/`, or another root.
6. **Safety** — examples are synthetic or public-safe and contain no secrets, real reviewer data, restricted evidence, or sensitive exact locations.
7. **Maintenance** — owner/reviewer expectations and paired docs are updated.

If any requirement is unresolved, keep the proposal in documentation or the verification backlog rather than creating an ambiguous fixture authority.

[Back to top](#top)

---

## What does not belong here

Do not place any of the following under `fixtures/release/`:

- actual `ReleaseManifest`, `PromotionDecision`, `RollbackCard`, `WithdrawalNotice`, `CorrectionNotice`, `ReviewRecord`, or `PolicyDecision` records;
- real EvidenceBundles, EvidenceRefs, SourceDescriptors, proofs, receipts, signatures, attestations, release candidates, or published artifacts;
- lifecycle data from RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, or PUBLISHED;
- executable schemas, semantic contracts, Rego/OPA policy, validators, pipelines, release CLIs, application code, or workflow logs;
- generated CI artifacts, coverage reports, build output, or temporary release packages;
- direct public API, UI, map, tile, export, story, AI, or catalog payloads presented as released truth;
- real reviewer identities, private ticket content, credentials, tokens, signed URLs, internal storage paths, restricted policy context, or sensitive source/location details;
- live source/service calls disguised as fixture validation;
- child directories whose object family, consumer, and expected outcome are not documented;
- duplicated fixture copies that also evolve under `tests/fixtures/` or another lane.

> [!WARNING]
> `fixtures/release/` must not become a shadow release system, policy engine, review database, proof store, receipt store, schema registry, artifact store, or publication root.

[Back to top](#top)

---

## Inputs

Release fixtures may be authored from:

- accepted or proposed semantic contracts under `contracts/release/` and adjacent correction families;
- machine schemas under `schemas/contracts/v1/release/` and other verified schema families;
- executable policy rules and reviewed policy test requirements;
- validator and release-tool source code;
- authored tests and workflow requirements;
- incident, correction, withdrawal, rollback, or release-readiness cases converted into synthetic public-safe examples;
- documentation examples that are clearly bounded and do not claim implementation beyond the named consumer.

Every fixture should record or make discoverable:

- object family;
- scenario and expected outcome;
- contract and schema version where applicable;
- consumer path or test name;
- whether the case is schema, semantic, policy, evidence, review, rollback, release, projection, parser, or expected-output oriented;
- synthetic/public-safe status;
- generation method when generated;
- update and supersession notes when the expected result changes.

[Back to top](#top)

---

## Outputs

This lane may support downstream:

- JSON Schema regression checks;
- policy and semantic tests when separately implemented;
- validator dry-runs;
- release-readiness and rollback drills when separately implemented;
- documentation examples;
- deterministic expected diagnostics or snapshots;
- correction, withdrawal, supersession, and public-projection tests when separately implemented;
- CI jobs that explicitly invoke the relevant consumers.

It does not emit:

- release approval;
- actual release manifests or promotion decisions;
- evidence closure;
- policy authority;
- reviewer approval;
- proof packs or receipts;
- rollback execution;
- public artifacts;
- publication state.

[Back to top](#top)

---

## Validation

### Confirmed current command

From repository root, the verified PromotionDecision schema fixture command is:

```bash
python tools/validators/release/validate_promotion_decision.py --fixtures
```

Direct-file mode is also supported by the current shared runner:

```bash
python tools/validators/release/validate_promotion_decision.py \
  fixtures/release/promotion_decision/valid/<fixture>.json
```

### Expected PromotionDecision behavior

| Condition | Expected result |
|---|---|
| Every discovered valid fixture has zero schema errors and every invalid fixture has at least one | Exit `0` |
| A valid fixture has a schema error | Exit `1` |
| An invalid fixture has zero schema errors | Exit `1` |
| Direct-file mode receives no files | Exit `2` |
| A file cannot be read or parsed during the first validation pass | Printed `FAIL`; fixture-mode behavior may later raise in the second expectation pass |
| No direct-child fixture JSON files are discovered | Current implementation can exit `0`; coverage is not proven |

### Proof boundary

A passing current PromotionDecision fixture run proves only:

- discovered `valid/*.json` objects satisfy the paired schema as evaluated by the current runner; and
- discovered `invalid/*.json` objects produce at least one schema error.

It does not prove:

- fixture inventory completeness;
- date-time format enforcement;
- reference resolution;
- policy correctness or freshness;
- reviewer authorization or separation of duties;
- rollback target usability;
- release readiness;
- proof, receipt, or signature closure;
- supersession or correction correctness;
- public-summary safety;
- CI required-check enforcement;
- release or publication.

### Future consumer rule

Every future release-fixture family must document its exact command, file discovery behavior, expected exit/result contract, negative states, and proof limits. A README phrase such as “should pass release readiness” is insufficient without an implemented consumer.

[Back to top](#top)

---

## Failure interpretation

| Observation | Safe interpretation | Unsafe interpretation |
|---|---|---|
| Positive schema fixture passes | Object satisfies current machine shape | Release is approved or ready |
| Negative schema fixture is rejected | Declared shape is rejected | Policy or release process is proven fail-closed |
| Policy fixture is denied | Named policy consumer denied the synthetic input | All policy bundles and runtime paths are correct |
| Rollback drill fixture succeeds | Named rollback drill handled the synthetic case | Production rollback is universally safe |
| Expected output matches | Named deterministic transformation remained stable | Upstream evidence or release truth is correct |
| No fixtures are discovered and command exits `0` | No discovered case failed | Coverage exists |
| A domain workflow fails on the PR | That workflow needs inspection | This README caused the failure |
| README renders correctly | Documentation syntax is acceptable | Release implementation exists |

When a check fails, report the named consumer, fixture path, expected result, actual result, and whether the failure is introduced or inherited. Do not weaken the expected outcome merely to make CI green.

[Back to top](#top)

---

## Rights, sensitivity, and test data

Release fixtures must be synthetic or demonstrably public-safe.

Use:

- toy identifiers and domains;
- toy evidence, policy, review, rollback, proof, receipt, release, and artifact references;
- fixed synthetic timestamps;
- non-resolving example URIs that cannot expose internal services;
- generalized or invented geometry when spatial context is necessary;
- public-safe reason codes and summaries.

Do not use:

- real living-person or DNA/genomic data;
- exact archaeology, rare-species, cultural/sacred, private-land, or infrastructure locations;
- actual reviewer identities or private ticket text;
- credentials, tokens, secrets, signed URLs, internal hostnames, or private storage keys;
- restricted source excerpts, confidential policy decisions, or real unpublished release candidates;
- production artifact hashes if disclosure could expose restricted material.

If real or sensitive material is discovered in this tree, stop normal fixture handling, remove it from ordinary review surfaces where authorized, route it through the appropriate security/quarantine process, and record the correction path without reproducing the sensitive content.

[Back to top](#top)

---

## Review burden

No accepted release-fixture steward or path-specific CODEOWNERS rule was verified in this update. Until ownership is confirmed, request review proportionate to the change:

| Change | Minimum review concern |
|---|---|
| README clarification only | Fixture/docs maintainer familiar with the lane |
| New schema-positive or schema-negative fixture | Schema and validator owner |
| New policy or evidence-resolution scenario | Policy/evidence owner plus fixture maintainer |
| New rollback, correction, withdrawal, or release-readiness family | Release/rollback/correction owner plus contract/schema/validator owners |
| Fixture containing sensitive-domain context | Applicable policy/sensitivity/domain steward |
| Expected output or generation method change | Consumer owner and reviewer of deterministic output changes |
| Move between `fixtures/` and `tests/fixtures/` | Both ownership surfaces plus reference repair review |

Reviewers should verify:

- the scenario belongs in this lane;
- the consumer exists and is correctly named;
- expected outcomes match implementation;
- positive and negative states are not conflated;
- test material is synthetic/public-safe;
- the fixture does not claim release authority;
- related contract, schema, policy, validator, test, and README surfaces remain synchronized.

[Back to top](#top)

---

## Related folders

| Path | Relationship |
|---|---|
| [`../README.md`](../README.md) | Canonical reusable fixture-root contract |
| [`promotion_decision/README.md`](promotion_decision/README.md) | Verified current release-fixture family |
| [`promotion_decision/valid/README.md`](promotion_decision/valid/README.md) | PromotionDecision schema-positive lane |
| [`promotion_decision/invalid/README.md`](promotion_decision/invalid/README.md) | PromotionDecision schema-negative lane |
| [`../../contracts/release/README.md`](../../contracts/release/README.md) | Release object semantic-contract family |
| [`../../contracts/release/promotion_decision.md`](../../contracts/release/promotion_decision.md) | PromotionDecision semantic meaning and invariants |
| `../../schemas/contracts/v1/release/` | Machine-shape authority for verified release schema families |
| `../../policy/release/` | Release admissibility and obligations when verified |
| `../../policy/promotion/` | Promotion-gate policy when verified |
| [`../../release/`](../../release/) | Release candidates, decisions, manifests, corrections, withdrawals, and rollback authority |
| [`../../data/proofs/`](../../data/proofs/) | Canonical proof objects |
| [`../../data/receipts/`](../../data/receipts/) | Canonical process receipts |
| `../golden/README.md` | Cross-cutting deterministic expected-output lane when the ownership relationship is verified |
| `../invalid/README.md` | Broad invalid fixture lane; object-family-specific schema negatives should remain with their family |
| [`../../docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md) | Placement, compatibility, and anti-drift doctrine |

[Back to top](#top)

---

## ADRs

No ADR is required for this same-path documentation modernization. It creates no canonical root, compatibility root, lifecycle phase, schema home, policy home, release home, or parallel authority.

An ADR or migration note may be required when a future change:

- creates a new root or parallel release/schema/policy/proof/receipt home;
- changes the canonical split between `fixtures/` and `tests/fixtures/`;
- moves actual release objects or lifecycle data into fixture storage;
- changes object identity or schema version in a way that invalidates existing fixtures;
- establishes a repository-wide fixture outcome or exit-code contract;
- retires or consolidates a fixture family with downstream compatibility impact.

A new child family under this existing parent does not automatically require an ADR, but it does require the family-admission evidence and synchronized documentation described above.

[Back to top](#top)

---

## Verification status

| Check | Result |
|---|---|
| Target path and prior bytes | **CONFIRMED** at `main@d38b2886d1786eeaf0e8ec1f1ab83da5f0c93b3a`, blob `94b19cc0a5945947a2c1df9b2db8aba973531d86` |
| Same-path update | **PASS** — no sibling README or path move |
| Root fixture contract | **CONFIRMED** at blob `911c20c86d9322f38b1f59db66b922a94fd027eb` |
| Release contract-family README | **CONFIRMED** at blob `3412cb63cfde542cf9a7c8e93e035530569425d8` |
| PromotionDecision fixture parent | **CONFIRMED** at blob `6f934bd5c28ebfc7f5535a980fae3d0fd05c09a5` |
| PromotionDecision valid lane | **CONFIRMED** at blob `a6e0fc5eb6d5f487be70ff02307e2236e7c6d01a` |
| PromotionDecision invalid lane | **CONFIRMED** at blob `1a6fe6a56f8969fe0714dd273fdef5fc148d4726` |
| PromotionDecision contract | **CONFIRMED** at blob `42295bfc83a621cf125d33aa821912b426f70bd2` |
| PromotionDecision schema | **CONFIRMED** at blob `a2d087a46772cf60e4b9dfb394892690e8a88b31`; schema status remains `PROPOSED` |
| PromotionDecision validator binding | **CONFIRMED** at blob `ead33d6c5c073f319627ee42d99c5933c0e370d1` |
| Shared runner behavior | **CONFIRMED by source inspection** at blob `ce05ae25d0cb6fc29a2ea41db6c65a99ca5e13e6` |
| Other release fixture families | **UNKNOWN / not verified** |
| Exact recursive fixture inventory | **UNKNOWN / not performed** |
| Python validator execution | **NOT RUN locally** — no executable checkout mounted |
| Markdown lint, docs build, and link checker | **NOT RUN locally** |
| Policy/evidence/review/rollback/release tests | **NOT RUN / not established by the confirmed consumer** |
| CI required-check enforcement | **NEEDS VERIFICATION** |
| Release or publication | **NOT CLAIMED** |

Remote repository reads prove bytes and relationships only. They do not substitute for a validator run, policy test, release dry-run, documentation build, link check, branch-protection inspection, or end-to-end release execution.

[Back to top](#top)

---

## Rollback

This is a documentation-only, same-path update.

Rollback options:

1. revert the update commit created for this README; or
2. restore prior blob `94b19cc0a5945947a2c1df9b2db8aba973531d86` at `fixtures/release/README.md`.

Rollback changes documentation only. It does not roll back a fixture payload, contract, schema, policy, validator, release decision, manifest, correction, withdrawal, rollback execution, proof, receipt, runtime, or publication state because none of those are changed by this update.

[Back to top](#top)

---

## Last reviewed

**2026-07-24** — repository-grounded documentation review against `main@d38b2886d1786eeaf0e8ec1f1ab83da5f0c93b3a`.

Review again when:

- a new release-fixture family is added;
- PromotionDecision schema or runner behavior changes;
- a release policy, evidence resolver, review check, rollback drill, correction/withdrawal validator, or projection consumer begins using this tree;
- fixture generation or golden-output conventions change;
- ownership or CODEOWNERS rules are accepted;
- the fixture split between `fixtures/` and `tests/fixtures/` changes;
- six months pass without review.

[Back to top](#top)
