<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-golden-readme
title: fixtures/golden/README.md — Cross-Cutting Golden Expected-Output Fixture Boundary
type: readme; directory-readme; golden-fixture-parent; expected-output-index; non-authoritative
version: v0.3
status: draft; repository-grounded; top-level-golden-parent; direct-inventory-bounded; consumer-wiring-unverified; dedicated-ci-unestablished; non-authoritative
owners:
  - "@bartytime4life — verified GitHub CODEOWNER for /fixtures/ review routing"
  - "OWNER_TBD — semantic fixture stewardship and cross-cutting admission ownership"
created: NEEDS VERIFICATION — file predates this revision
updated: 2026-07-21
supersedes: v0.2 top-level golden fixture README
policy_label: public-doc; fixtures; golden; expected-output; synthetic-only; deterministic; no-network-default; public-safe; source-role-preserving; evidence-aware; policy-aware; sensitivity-aware; release-subordinate; correction-aware; rollback-aware; no-publication
current_path: fixtures/golden/README.md
truth_posture:
  CONFIRMED:
    - fixtures/golden/README.md exists at the checked base
    - the fixtures responsibility root is the repository home for reusable synthetic, valid, invalid, and golden checking inputs
    - fixtures/ and tests/fixtures/ have documented distinct scopes
    - multiple domain-specific golden README lanes exist under fixtures/domains/
    - .github/CODEOWNERS routes /fixtures/ review to @bartytime4life
    - the Makefile fixtures target is TODO-only and the default test target does not execute this lane
  PROPOSED:
    - this lane owns only genuinely cross-cutting golden admission, pairing, manifest, consumer-backlink, determinism, sensitivity, update-review, and migration guidance
    - stable domain-owned golden outputs move to fixtures/domains/<domain>/golden/
    - a future machine-readable golden manifest may enumerate input, expected output, consumer, hashes, comparison profile, and review state
  UNKNOWN:
    - exhaustive tracked and generated payload inventory, external golden stores, active consumers, current pass rates, required-check significance, branch-protection enforcement, and release dependency
  NEEDS_VERIFICATION:
    - accepted semantic owners and review separation
    - exact admission threshold between top-level and domain, object-family, runtime, renderer, or test-local golden lanes
    - substantive golden payloads, active consumers, two-way backlinks, nonempty coverage, no-network enforcement, and dedicated CI ownership
evidence_state_qualifiers:
  CONFLICTED:
    - the repository contains three Directory Rules documents with overlapping authority claims; CONTRIBUTING.md directs live contribution preflight to docs/architecture/directory-rules.md while the doctrine copy remains at docs/doctrine/directory-rules.md
  NARROWED:
    - direct inventory and consumer conclusions are bounded to connector reads and indexed repository search, not a byte-complete recursive tree walk
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 77ee6d6fdfad928d19e45ff667935d80df9fd125
  target_prior_blob: 445ea46215cdd5fd00d1343c2c5055d30cb5480d
  related_repository_blobs:
    contributing: 935f8bbefd8f966275887c9f58277746b9c67c28
    directory_rules_live_preflight: 18653c00ba193a4afaa3e07a0924452807fb98ef
    directory_rules_doctrine_copy: 2affb080e6f0043867c64c7f06c1ca52030fbd55
    directory_rules_uppercase_copy: 19a480a329eab17f68fc6da888665c98ffa8e4a6
    fixtures_root_readme: b096b0ed49c8e7d95ddb0d4c813d06ef40f1528d
    tests_fixtures_readme: 2d0147e85eae86f687e85c5bea0d3e61f9c3a8f7
    codeowners: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
    makefile: 51537af34ee065c2de571134688415042b83b22a
    workflows_readme: c3dfbe1168d405e7244c6a7dacf0e0616faf120e
notes:
  - "This revision changes documentation only."
  - "Golden fixtures are expected-output carriers, not sovereign truth or publication authority."
  - "README presence, filenames, hashes, or a passing comparison do not prove semantic correctness, evidence closure, policy admissibility, release readiness, or production behavior."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `fixtures/golden/` — cross-cutting golden expected outputs

> **One-line purpose.** `fixtures/golden/` is KFM's last-resort lane for stable, synthetic, cross-cutting expected outputs when no domain, object family, runtime, renderer, or test-local fixture lane is the accepted narrower owner.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-blue">
  <img alt="Lane: golden expected output" src="https://img.shields.io/badge/lane-golden__expected__output-purple">
  <img alt="Inventory: bounded" src="https://img.shields.io/badge/inventory-bounded-orange">
  <img alt="Network: denied by default" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture__only-red">
</p>

> [!IMPORTANT]
> Use the narrowest stable owner. Domain-owned expected outputs belong under `fixtures/domains/<domain>/golden/`; one-test-only outputs belong with that test's accepted fixture convention.

> [!CAUTION]
> A golden comparison proves only that a named implementation produced the expected bytes or normalized structure for a declared synthetic case. It does **not** prove source truth, semantic truth, evidence closure, policy approval, release readiness, current-world accuracy, or safe publication.

> [!WARNING]
> Golden files must never freeze sensitive exact geometry, private identities, living-person information, DNA or genomic material, archaeology locations, rare-species localities, critical-infrastructure detail, credentials, live alerts, or reverse-engineerable protected information into repository history.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs here](#what-belongs-here) · [Does not belong](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related folders](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Placement](#placement-and-routing) · [Admission](#golden-case-admission-contract) · [Pairing](#input-expected-output-and-consumer-pairing) · [Manifest](#minimum-golden-manifest-contract) · [Determinism](#determinism-normalization-and-hashing) · [Outcomes](#outcome-vocabulary-separation) · [Boundaries](#runtime-evidence-policy-release-and-ai-boundaries) · [Sensitivity](#rights-sensitivity-and-public-safety) · [Updates](#golden-update-review-contract) · [Coverage](#consumer-backlinks-orphans-and-nonempty-coverage) · [Maintenance](#maintenance-correction-and-rollback) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Ledger](#evidence-ledger)

---

## Purpose

This README helps fixture, test, runtime, renderer, API, AI, domain, governance, and release maintainers:

- decide whether an expected output belongs in this lane or a narrower owner;
- create stable regression anchors without turning snapshots into authority;
- keep synthetic input, expected output, consumer, comparison profile, and review reason connected;
- preserve finite KFM outcomes without collapsing them into test pass or fail language;
- prevent sensitive, stale, nondeterministic, or environment-specific values from entering golden history;
- update, correct, migrate, deprecate, or retire expectations transparently; and
- detect orphaned, duplicated, vacuous, or unconsumed golden files.

This lane does not exist to make all expected outputs discoverable in one place. It exists only for expectations whose accepted responsibility is genuinely cross-cutting or temporarily unresolved.

[Back to top](#top)

## Authority level

**Implementation-supporting fixture lane; non-authoritative for truth, evidence, policy, review, release, and publication.**

The repository's current contribution guide identifies a conflict among three Directory Rules documents and directs live contribution preflight to [`docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md). The supplied Directory Rules artifact and all three repository copies agree on the placement rule material to this lane: `fixtures/` owns golden, valid, invalid, and synthetic checking inputs; `tests/` owns executable assertions; contracts, schemas, policy, lifecycle data, receipts, proofs, and release decisions retain separate authority homes.

> [!NOTE]
> The Directory Rules document-authority conflict remains **CONFLICTED / NEEDS VERIFICATION**. This README does not resolve it or create a fourth authority surface. The target path already exists under the canonical `fixtures/` responsibility root, so this documentation-only revision does not require a new root, migration, or placement ADR.

| Responsibility | Owning surface | This lane's boundary |
|---|---|---|
| Cross-cutting reusable expected output | `fixtures/golden/` | Own only when no narrower accepted owner applies. |
| Domain expected output | `fixtures/domains/<domain>/golden/` | Preferred when domain ownership or sensitivity context is clear. |
| Test-local expected output | `tests/fixtures/` or the owning test subtree | Use when a fixture exists only for one test package. |
| Executable assertions | `tests/` | Golden files are inputs, not tests. |
| Object meaning | `contracts/` | Fixtures imitate accepted meaning; they do not define it. |
| Machine shape | `schemas/` | Fixtures exercise schemas; they do not create schemas. |
| Policy and admissibility | `policy/` | Fixtures may represent expected decisions; they do not decide them. |
| Lifecycle data | `data/` | Golden material is outside the governed lifecycle. |
| Receipts and proofs | accepted receipt and proof homes | Receipt-shaped and proof-shaped fixtures remain synthetic examples. |
| Release and rollback decisions | `release/` | Golden comparisons never approve, withdraw, or reverse a release. |
| Generated CI output | `artifacts/` | Generated reports are not committed golden authority by default. |

The governing lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Golden fixtures do not enter, shortcut, or substitute for this lifecycle.

[Back to top](#top)

## Status

| Evidence field | Current bounded result |
|---|---|
| Repository snapshot | `bartytime4life/Kansas-Frontier-Matrix` at `main@77ee6d6fdfad928d19e45ff667935d80df9fd125` |
| Prior README blob | `445ea46215cdd5fd00d1343c2c5055d30cb5480d` |
| Direct tracked inventory | **NARROWED / NEEDS VERIFICATION** — indexed search surfaced this README; the connector did not provide a byte-complete recursive directory listing. |
| Direct consumer inventory | **NEEDS VERIFICATION** — indexed search surfaced documentation references but no executable consumer of this top-level lane. |
| Review route | **CONFIRMED** — `.github/CODEOWNERS` maps `/fixtures/` to `@bartytime4life`; required-review enforcement remains **UNKNOWN**. |
| Makefile fixture refresh | **CONFIRMED TODO-only** — `make fixtures` prints a readiness marker. |
| Default `make test` | **CONFIRMED** — runs `tests/schemas` and `tests/contracts`, not this lane. |
| Dedicated top-level golden CI | **NOT ESTABLISHED** — broad PR workflows exist, but no named top-level golden consumer or gate was confirmed. |

### Safe conclusions

- **CONFIRMED:** the target README and its parent fixture contract exist at the pinned commit.
- **CONFIRMED:** the repository documents distinct scopes for `fixtures/` and `tests/fixtures/`.
- **CONFIRMED:** domain-specific golden README lanes exist and are the preferred owners for domain-specific expectations.
- **CONFIRMED:** review routing for `/fixtures/` exists in CODEOWNERS.
- **PROPOSED:** this top-level lane is a last-resort cross-cutting parent, not the default home for new golden cases.
- **UNKNOWN:** exhaustive payload inventory, generated or ignored files, external stores, active consumers, current pass rates, required checks, and promotion dependency.
- **NEEDS VERIFICATION:** whether this lane should remain README-only or admit narrowly scoped cross-cutting cases.

### Maturity matrix

| Capability | Status | Evidence-bounded conclusion |
|---|---:|---|
| Directory README | `CONFIRMED` | Routing and governance surface exists. |
| Direct golden payloads | `NOT ESTABLISHED` | No payload was confirmed by the bounded inspection. |
| Input/output pairing | `NOT ESTABLISHED` | No direct pair inventory was verified. |
| Consumer backlinks | `NOT ESTABLISHED` | No direct executable consumer was surfaced. |
| Machine-readable manifest | `NOT ESTABLISHED` | A proposed shape appears below; no accepted schema was found. |
| Deterministic normalization | `NOT ESTABLISHED` | Required before substantive golden use. |
| Hash or identity registry | `NOT ESTABLISHED` | Proposed only. |
| No-network enforcement | `NOT ESTABLISHED` | Required posture; executable proof was not found. |
| Orphan and duplicate detection | `NOT ESTABLISHED` | Required future gate. |
| Dedicated CI collection | `NOT ESTABLISHED` | Broad workflows do not prove this lane is consumed. |
| Release authority | `DENIED` | Golden fixtures never approve publication. |

[Back to top](#top)

## What belongs here

- Small, synthetic, public-safe expected outputs whose accepted responsibility is genuinely cross-cutting.
- Stable expected bytes or normalized structures paired with declared synthetic inputs.
- Cases consumed by a named test, validator, renderer check, governed API check, or documentation harness.
- Explicit comparison profiles for semantic JSON, text, geometry, images, rendered output, or another accepted format.
- Expected finite outcomes such as `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` when the governing runtime contract uses them.
- Review notes, manifests, and deterministic generation instructions needed to understand and reproduce the expectation.
- Temporary cross-cutting cases with an unresolved-owner note and a defined migration trigger.

[Back to top](#top)

## What does NOT belong here

- Domain-owned expectations that belong under `fixtures/domains/<domain>/golden/`.
- One-test-only fixtures that belong with the owning test convention.
- Contracts, schemas, policy rules, executable tests, validators, source registries, or runtime implementation.
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data.
- Actual EvidenceBundles, receipts, proofs, review records, promotion decisions, release manifests, correction notices, or rollback cards.
- Production snapshots, current-world caches, live alerts, source dumps, logs, credentials, private endpoints, or environment-specific output.
- Generated CI or build output copied into the repository without an accepted deterministic generation and review contract.
- Sensitive or reverse-engineerable material prohibited by the warning at the top of this README.
- Duplicate copies created only for directory symmetry or discoverability.

[Back to top](#top)

## Inputs

Every substantive case requires:

- an exact synthetic input path or a deterministic generator reference;
- an accepted contract and schema reference where applicable;
- a named executable consumer;
- a declared comparison or normalization profile;
- expected finite outcome vocabulary and failure class;
- sensitivity, rights, and public-safety posture;
- deterministic identity or content hashes where the accepted contract requires them;
- a change reason and rollback target; and
- an explanation of why no narrower fixture lane owns the case.

Inputs must not depend on live source systems, current time, local user state, ambient credentials, or canonical/internal stores as a shortcut.

[Back to top](#top)

## Outputs

This lane may support:

- expected byte-for-byte artifacts;
- normalized expected JSON, GeoJSON, text, SVG, image, tile, renderer, API, or AI-envelope output;
- expected validation or finite-outcome summaries;
- reviewable semantic diffs; and
- machine-readable manifests if an accepted schema and owner are established.

It does not emit or authorize source admission, evidence closure, policy approval, lifecycle promotion, release state, deployment, or publication. Generated comparison reports belong in declared temporary or artifact locations and remain non-authoritative.

[Back to top](#top)

## Validation

### Current executable boundary

- `make fixtures` is a TODO-only readiness marker; it does not regenerate or compare golden outputs.
- `make test` executes the repository's schema and contract test lanes, not `fixtures/golden/`.
- Broad pull-request workflows run schema, contract, validator, documentation-readiness, link-readiness, control-plane, and CodeQL jobs. Their existence does not prove this lane has a consumer.
- The inspected documentation build and link-check workflows are explicit holds; a green held job does not mean the README rendered or its links were checked.
- No dedicated top-level golden runner, manifest validator, orphan detector, or non-vacuous collection gate was confirmed.

### Required case validation

A future accepted golden gate should verify:

1. every case has input, expected output, comparison profile, consumer, owner, and review reason;
2. scenario IDs and contract or schema versions match;
3. generation and comparison are deterministic and no-network by default;
4. ignored paths and tolerances do not remove meaningful assertions;
5. sensitive and private content is absent or the case is denied from this public repository lane;
6. orphans, duplicate IDs, missing backlinks, zero collected cases, all-skipped runs, and self-comparisons fail explicitly;
7. expected-output changes are reviewed as behavior changes; and
8. CI output remains a review signal, not truth, policy, or release authority.

[Back to top](#top)

## Review burden

`.github/CODEOWNERS` routes `/fixtures/` changes to `@bartytime4life`. That is a verified GitHub review route, not proof of semantic ownership, completed review, independent approval, or branch-protection enforcement.

Reviewers should include the owners of every materially affected responsibility:

- fixture and test stewardship for admission, pairing, and executable coverage;
- domain stewardship for domain-specific meaning or sensitivity;
- contract and schema stewardship for versioned meaning and shape;
- policy, rights, privacy, sovereignty, cultural, ecological, archaeology, infrastructure, or living-person reviewers when those concerns apply;
- runtime, renderer, API, or AI stewardship for expected behavior;
- security review for secrets, path, network, filesystem, or generated-output risk; and
- release or correction stewardship when an expectation is relied on by a governed release process.

Changing an expected output is a behavior change unless the diff is provably editorial metadata only. Do not approve a bulk re-record merely because a test failed.

[Back to top](#top)

## Related folders

| Path | Relationship |
|---|---|
| [`fixtures/README.md`](../README.md) | Parent fixture-root scope and separation from tests, artifacts, and lifecycle data. |
| [`fixtures/valid/README.md`](../valid/README.md) | Broad positive-path fixture index when no narrower owner is accepted. |
| [`fixtures/invalid/README.md`](../invalid/README.md) | Broad fail-closed fixture index when no narrower owner is accepted. |
| [`fixtures/domains/README.md`](../domains/README.md) | Domain fixture routing root; domain-specific golden lanes live below it. |
| [`tests/fixtures/README.md`](../../tests/fixtures/README.md) | Test-only fixture scope; must not evolve as a competing cross-cutting fixture authority. |
| [`CONTRIBUTING.md`](../../CONTRIBUTING.md) | Current repository contribution and preflight requirements. |
| [live Directory Rules preflight](../../docs/architecture/directory-rules.md) | Current contribution guide's selected live placement document; authority conflict remains open. |
| [doctrine Directory Rules copy](../../docs/doctrine/directory-rules.md) | Overlapping doctrine copy with the same fixture responsibility-root rule. |
| [domain placement law](../../docs/architecture/domain-placement-law.md) | Additional repository guidance for routing domain-owned files into responsibility-root lanes. |
| [CODEOWNERS](../../.github/CODEOWNERS) | GitHub review routing for `/fixtures/`; not semantic or release authority. |
| [Makefile](../../Makefile) | Current repository-native command surface and its TODO-only fixture target. |

[Back to top](#top)

## ADRs

No accepted fixture-specific ADR governing `fixtures/golden/` was established by the bounded ADR-index and repository inspection.

- The target path already exists under the documented `fixtures/` responsibility root; this revision creates no root, compatibility surface, schema home, contract home, policy home, lifecycle phase, receipt home, proof home, or release authority.
- The repository contains draft or unindexed ADR files that discuss contracts, schemas, fixtures, receipts, proofs, manifests, catalogs, or identity. Their proposed language is informative only and does not become accepted authority here.
- The Directory Rules copy conflict is visible in `CONTRIBUTING.md` and remains unresolved; this one-file revision does not modify the drift register or attempt an ADR-class resolution.
- A future machine-readable golden manifest, new canonical normalization registry, or competing fixture home requires its own placement, authority, and ADR review before adoption.

[Back to top](#top)

## Last reviewed

**2026-07-21**, against `main@77ee6d6fdfad928d19e45ff667935d80df9fd125`.

This review covered the target README; parent and adjacent fixture READMEs; current contribution guidance; all three Directory Rules copies plus the supplied PDF; the ADR index and relevant draft ADR surfaces; the drift register; CODEOWNERS; Makefile targets; open pull-request and branch overlap; and pull-request workflow triggers relevant to a documentation-only change.

It did not establish a byte-complete tree inventory, generated or ignored files, external fixture stores, branch-protection configuration, required-check configuration, active consumer execution, current pass rates, or KFM publication state.

[Back to top](#top)

---

## Placement and routing

Use the narrowest stable owner.

1. **One domain owns the expectation:** use `fixtures/domains/<domain>/golden/`.
2. **One object family owns it:** use the accepted object-family fixture lane.
3. **One executable test owns it:** use that test's local fixture convention.
4. **One runtime or renderer subsystem owns it:** use the accepted subsystem fixture lane.
5. **One relation or join owns a cross-domain result:** use the accepted relation or cross-domain lane.
6. **No narrower owner is accepted:** use `fixtures/golden/` temporarily, record the unresolved owner, and migrate once ownership is settled.

Do not create parallel copies merely to satisfy directory symmetry.

### Relocation triggers

Move a case out of this lane when:

- domain, object-family, runtime, renderer, or test ownership becomes clear;
- the file starts resembling evidence, a receipt, a proof, a release record, or lifecycle data;
- sensitivity or rights require a more controlled lane;
- a dedicated accepted fixture lane replaces the temporary top-level home; or
- the expectation becomes obsolete, superseded, duplicated, or unconsumed.

[Back to top](#top)

## Golden case admission contract

A new case belongs here only when every required question has an explicit answer.

| Question | Required answer |
|---|---|
| What is the scenario? | Stable scenario ID and concise purpose. |
| Why top-level? | No accepted narrower owner, or the case is genuinely cross-cutting. |
| What is the input? | Exact synthetic input path or deterministic generator reference. |
| What is expected? | Exact expected output path and comparison profile. |
| Who consumes it? | Named test, validator, renderer check, API check, or documentation harness. |
| What governs meaning and shape? | Exact contract and schema references, versions, and compatibility profile. |
| What outcome applies? | Runtime, policy, validation, render, or comparison outcome stated explicitly. |
| What is ignored? | Documented nondeterministic fields and why exclusion is safe. |
| What sensitivity applies? | Synthetic public-safe, generalized, withheld, quarantined, or denied posture. |
| Why is the update safe? | Change rationale, reviewer burden, and regression effect. |
| How is it retired? | Deprecation, supersession, consumer update, and deletion plan. |

Reject or relocate a case when any answer is missing.

[Back to top](#top)

## Input, expected-output, and consumer pairing

Every substantive golden fixture should form a traceable set:

```text
synthetic input
    + declared normalization or comparison profile
    + named executable consumer
    + accepted contract and schema references
    -> expected golden output
```

Illustrative naming only:

```text
<scenario>.input.json
<scenario>.expected.json
<scenario>.golden.yaml
<scenario>.expected.geojson
<scenario>.expected.svg
```

Pairing rules:

- scenario IDs match exactly across files;
- input and expected output declare compatible contract and schema versions;
- the consumer path is recorded in a manifest or README;
- expected output contains no undeclared nondeterministic fields;
- negative and fail-closed cases name the expected reason or failure class;
- corrections update input, expectation, manifest, consumer, and review note together; and
- one expected output is not silently reused for incompatible profiles.

Golden files without consumers are orphans. Consumers without declared golden identity are untraceable.

[Back to top](#top)

## Minimum golden manifest contract

The following shape is **PROPOSED and illustrative**. It is not an accepted schema, registry, or file-placement decision.

```yaml
golden_id: golden:<stable-scenario-id>
version: 1
status: active
owner: OWNER_TBD
scope: cross-cutting
input_ref: ../path/to/scenario.input.json
expected_ref: ./scenario.expected.json
consumer_refs:
  - tests/path/to/test_case.py
contract_refs:
  - contracts/path/to/contract.md
schema_refs:
  - schemas/contracts/v1/path/to/schema.json
comparison:
  mode: semantic-json
  ignored_paths: []
  ordering: canonical
  numeric_tolerance: null
outcome:
  vocabulary: runtime
  expected: ABSTAIN
sensitivity:
  posture: synthetic-public-safe
network: denied
filesystem_writes: denied
input_sha256: "<computed>"
expected_sha256: "<computed>"
supersedes: null
review:
  reason: "<why this expectation is correct>"
  approved_by: []
```

Do not invent accepted field names, enum values, registry IDs, tolerances, or approval states from this example. An adopted manifest requires an accepted owner, canonical home, schema, validator, fixtures, tests, compatibility rule, and migration path.

[Back to top](#top)

## Determinism, normalization, and hashing

Golden output must be reproducible under the declared profile.

Required controls where applicable:

- canonical JSON key ordering;
- stable list ordering or explicit order-insensitive comparison;
- normalized timestamps or fixture-pinned time;
- stable UUIDs, IDs, seeds, and hashes;
- normalized line endings and Unicode;
- explicit coordinate precision;
- declared numeric tolerance rather than hidden rounding;
- stable locale and timezone;
- no hostnames, usernames, absolute paths, process IDs, ports, or temporary directories;
- no network-derived values;
- no environment-specific package metadata unless intentionally pinned; and
- no generated-at timestamps unless fixture-controlled.

Hashing proves byte identity only. It does not prove semantic correctness, policy safety, evidence closure, or release readiness.

[Back to top](#top)

## Outcome vocabulary separation

Keep these vocabularies distinct.

| Vocabulary | Example values | Meaning |
|---|---|---|
| KFM runtime | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Governed response posture. |
| Policy | allow, restrict, hold, deny, review-required | Admissibility or obligation posture. |
| Validation | valid, invalid, warning, unresolved | Contract, schema, or check result. |
| Renderer or UI | rendered, blocked, degraded, fallback, hidden | Surface behavior. |
| Test runner | pass, fail, skip, xfail, error | Execution result. |
| Release | candidate, approved, denied, withdrawn, superseded | Governed publication state. |

A test passing because an expected `DENY` was returned does not mean the policy result was allow. A golden `ANSWER` does not mean release approval.

[Back to top](#top)

## Runtime, evidence, policy, release, and AI boundaries

Golden fixtures may support bounded comparisons for governed API envelopes, renderer or tile inputs and normalized outputs, Evidence Drawer payloads, Focus Mode responses, search and graph projections, export summaries, runtime replay, and AI adapter envelopes.

They must not become:

- public API payload authority, UI truth state, style or tile release authority, or a production snapshot;
- a route contract, schema, policy, or validator substitute;
- direct model memory or proof that generated language is correct;
- an EvidenceRef or EvidenceBundle resolution substitute;
- a ReviewRecord, receipt, proof, catalog, manifest, release, correction, or rollback authority; or
- a current-world cache.

AI-generated expected text requires especially careful review. Generated fluency cannot substitute for EvidenceBundle support, policy state, review state, source role, temporal scope, or accepted wording contracts.

Public clients and normal UI surfaces still require governed interfaces and released public-safe derivatives.

[Back to top](#top)

## Rights, sensitivity, and public safety

All golden material must be synthetic or demonstrably public-safe.

Deny repository inclusion of:

- real precise rare-species, rare-plant, nest, den, roost, spawning, telemetry, or stewardship locations;
- archaeological sites, burials, sacred places, collection-security details, or culturally restricted knowledge;
- living-person records, DNA or genomic data, consent records, private relationships, or private parcels;
- critical-infrastructure details, access controls, vulnerabilities, or operational dependencies;
- exact private wells, protected facilities, or reverse-engineerable protected joins;
- credentials, tokens, private endpoints, production logs, or source dumps; and
- live emergency warnings or life-safety instructions.

The strictest applicable domain, rights, consent, sovereignty, cultural, privacy, infrastructure, or release posture wins. Generalize, redact, quarantine, stage access, or deny the case when public-safe inclusion is not supported.

[Back to top](#top)

## Golden update review contract

Changing a golden expectation is a behavior change, not routine formatting.

Every substantive update must state:

1. what implementation or accepted contract changed;
2. why the prior expectation is no longer correct;
3. whether the change is intended, corrective, compatibility-driven, or a narrowed safety response;
4. which consumers are affected;
5. whether policy, sensitivity, evidence, temporal, or release semantics changed;
6. whether downstream snapshots, caches, exports, or docs must change;
7. whether the old golden remains useful as a negative, compatibility, or lineage case; and
8. the rollback target.

Prohibited pattern:

```text
test failed
-> regenerate every golden
-> commit without semantic inspection
```

Required pattern:

```text
behavior or contract change
-> inspect the semantic delta
-> verify authority and sensitivity
-> update only affected cases
-> run named consumers
-> review the complete diff
-> record the reason and rollback target
```

[Back to top](#top)

## Consumer backlinks, orphans, and nonempty coverage

A future substantive gate should fail when:

- a golden file has no declared consumer;
- a consumer references a missing golden file;
- input and expected-output scenario IDs differ;
- duplicate golden IDs exist;
- the lane contains zero substantive cases when coverage is required;
- every case is skipped;
- generated output is compared to itself;
- ignored paths remove every meaningful assertion;
- a domain-owned case remains here without a current reason;
- a sensitive case lacks a public-safe review posture; or
- an expectation changes without a review reason and rollback target.

Golden generation and comparison must be hermetic by default: no live APIs, websites, tile or glyph servers, model services, databases, source systems, publication side effects, fixture mutation, or undeclared filesystem writes.

Coverage is case-specific. Counting README files, empty directories, or a green readiness-hold workflow is not coverage.

[Back to top](#top)

## Maintenance, correction, and rollback

When a golden case is wrong:

1. mark it disputed or failing;
2. stop treating it as the accepted expectation;
3. identify affected consumers and derived documentation;
4. determine whether the implementation, contract, or fixture is wrong;
5. create a reviewed correction;
6. preserve the prior case when needed for regression or correction lineage;
7. update hashes, manifests, links, consumers, and review notes together;
8. run the named consumers; and
9. record a transparent rollback target.

When ownership changes, move the case through a reviewed commit that updates all backlinks. Do not leave duplicate active copies.

For this README revision, rollback means restoring prior blob `445ea46215cdd5fd00d1343c2c5055d30cb5480d` through a transparent revert commit. Before merge, leave the draft pull request unmerged or add a corrective commit; after merge, create a revert commit or pull request. Do not reset or force-push shared history.

[Back to top](#top)

## Definition of done

This parent is operationally complete only when:

- [ ] semantic owners and review duties are accepted;
- [ ] top-level admission criteria are accepted;
- [ ] substantive tracked, generated, and external payload inventory is known;
- [ ] every case has input, expected output, manifest, consumer, and comparison profile;
- [ ] every case has deterministic normalization and identity;
- [ ] domain and single-consumer cases are routed to narrower lanes;
- [ ] no sensitive, private, restricted, or rights-unclear material is present;
- [ ] no-network and side-effect controls are executable;
- [ ] orphan, duplicate, zero-case, all-skipped, and vacuous-comparison checks exist;
- [ ] expected-output updates require semantic review and rollback targets;
- [ ] CI executes named consumers and preserves primary failures;
- [ ] correction, deprecation, migration, and rollback are tested; and
- [ ] documentation matches verified current behavior.

Until then, this README is a governed design and routing boundary, not proof of implemented golden-fixture enforcement.

[Back to top](#top)

## Open verification register

- [ ] Resolve the Directory Rules document-authority conflict without creating another copy.
- [ ] Assign semantic fixture owners and decide review separation.
- [ ] Obtain a byte-complete inventory of direct, generated, ignored, and external golden content.
- [ ] Identify active consumers and verify two-way backlinks.
- [ ] Decide whether this lane remains README-only.
- [ ] Decide the accepted top-level admission threshold.
- [ ] Decide whether a machine-readable manifest is needed and, if so, its canonical owner, home, schema, and migration path.
- [ ] Establish stable golden IDs and versions.
- [ ] Establish canonical comparison and normalization profiles.
- [ ] Establish numeric, geometry, rendered-image, and ignored-field rules.
- [ ] Add orphan, duplicate, missing-backlink, nonempty, all-skipped, and non-vacuous checks.
- [ ] Add no-network and filesystem isolation.
- [ ] Add sensitive-content scanning and reviewer requirements.
- [ ] Add domain ownership migration checks.
- [ ] Add update-reason and rollback requirements.
- [ ] Add substantive CI collection for named consumers.
- [ ] Confirm required checks, branch-protection enforcement, artifact retention, and public-safety rules.
- [ ] Confirm no promotion gate treats a golden pass as release or publication approval.

[Back to top](#top)

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| `fixtures/golden/README.md` blob `445ea462...` at the pinned base | `CONFIRMED` | Existing v0.2 guidance and no-loss baseline. | Current payloads, consumers, CI, or branch rules. |
| `fixtures/README.md` blob `b096b0ed...` | `CONFIRMED` | Parent scope and separation from tests, artifacts, and lifecycle data. | Direct inventory or execution of this lane. |
| `tests/fixtures/README.md` blob `2d0147e8...` | `CONFIRMED` | Test-only fixture boundary. | That every consumer follows it. |
| `CONTRIBUTING.md` blob `935f8bbe...` | `CONFIRMED` | Review-branch default and live Directory Rules conflict handling. | Branch-protection or completed human review. |
| Directory Rules blobs `18653c00...`, `2affb080...`, and `19a480a3...` plus supplied PDF | `CONFIRMED / CONFLICTED` | Shared fixture responsibility-root and README-contract rules. | Which repository copy is finally authoritative. |
| `.github/CODEOWNERS` blob `dd2a84aa...` | `CONFIRMED` | `/fixtures/` review routes to `@bartytime4life`. | Semantic ownership, required review, or enforcement. |
| ADR index blob `d6550e41...` and bounded ADR search | `NARROWED` | No accepted fixture-specific ADR was established. | Absolute absence outside inspected index and search scope. |
| Drift register blob `97a77552...` | `CONFIRMED` | Existing drift entries were inspected. | Resolution of the Directory Rules copy conflict; no matching entry was present. |
| Makefile blob `51537af3...` | `CONFIRMED` | `make fixtures` is TODO-only; default `make test` excludes this lane. | All CI, package, or external consumer behavior. |
| Workflow README blob `c3dfbe11...` and inspected PR workflow YAML | `CONFIRMED / NARROWED` | Broad PR checks exist; no dedicated top-level golden check was established. | Required-check configuration, current pass rates, or exhaustive workflow inventory. |
| Indexed search at `main@77ee6d6...` | `NARROWED` | Domain golden READMEs and documentation references exist; no direct executable top-level consumer surfaced. | Byte-complete tree absence, generated files, ignored files, or external stores. |

---

This README revision changes documentation only. It adds no fixture payload, executable test, validator, schema, contract, policy, workflow, lifecycle object, receipt, proof, release record, runtime behavior, deployment, or public artifact.

[Back to top](#top)
