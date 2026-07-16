# `tests/fixtures/domains/agriculture/` — Agriculture Test-Local Fixture Routing and Safety Boundary

> Repository-grounded boundary for test-local Agriculture fixture material: small synthetic inputs and expectation records owned by a specific test area, kept separate from reusable fixture corpora, lifecycle data, source truth, evidence, policy, release, and public artifacts.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-domains-agriculture-readme
title: tests/fixtures/domains/agriculture/README.md — Agriculture Test-Local Fixture Routing and Safety Boundary
type: readme; directory-readme; test-local-fixture-lane; agriculture-domain-fixture-routing-boundary
version: v0.2
status: draft; repository-grounded; readme-only-direct-lane; parent-tests-fixtures-readme-confirmed; domains-parent-index-absent; reusable-fixture-root-confirmed; no-direct-payload-or-consumer-established; ci-unestablished; non-authoritative
owners: OWNER_TBD — Agriculture domain steward · Test steward · Fixture steward · QA steward · Contract/schema steward · Source-role steward · Evidence steward · Policy steward · Rights/sensitivity steward · Release steward · Security reviewer · CI steward · Docs steward
created: 2026-07-06
updated: 2026-07-16
supersedes: v0.1
policy_label: public-doctrine; tests; fixtures; agriculture; test-local-only; synthetic-only; no-network-default; aggregate-first; source-role-preserving; evidence-aware; policy-aware; rights-aware; sensitivity-aware; release-subordinate; correction-aware; rollback-aware; no-publication
current_path: tests/fixtures/domains/agriculture/README.md
truth_posture: CONFIRMED target README v0.1, Directory Rules, canonical tests root, tests/fixtures parent README, root fixtures README, reusable Agriculture fixture README and README-backed child lanes, Agriculture domain-test README, Agriculture E2E README, Agriculture schema-test README, common schema fixture harness limited to shared contract families rather than domain Agriculture roots, TODO-only Makefile fixtures target, Makefile default test collection limited to tests/schemas plus tests/contracts, TODO-only domain-agriculture workflow, checked absence of tests/fixtures/domains/README.md, checked absence of direct lane conftest.py, manifest_expectations.json, representative test modules, and representative valid child README, and checked absence of fixtures/domains/agriculture/valid/valid_1.json / PROPOSED declarative test-local fixture admission contract, manifest and consumer-backlink contract, orphan detection, fixture family routing, source-role and aggregate anti-collapse canaries, evidence/policy/release reference rules, no-network and filesystem controls, version/hash/generation metadata, deterministic replay, valid-invalid polarity, correction/withdrawal/rollback cases, substantive CI, nonempty inventory checks, and promotion blocking / CONFLICTED prior README claim that tests/fixtures/README.md was absent; prior proposed executable test files under a fixture directory versus the parent rule that executable tests belong in test lanes; tests/fixtures versus fixtures responsibility split without a tests/fixtures/domains parent index; README-backed reusable Agriculture fixture lanes versus unverified payload inventory; Agriculture schemas and child schema tests versus no Agriculture-domain fixture collection in the common schema harness / UNKNOWN exhaustive direct-lane inventory, generated or ignored fixture files, dynamic consumers, accepted fixture-manifest schema, canonical Agriculture fixture families, payload coverage, consumer coverage, current pass rates, no-network enforcement, artifact retention, branch-protection significance, production or release use, and promotion dependency / NEEDS VERIFICATION owners, lane-retention decision, parent domains index, exact admission threshold, manifest vocabulary, source-role vocabulary, reason-code registry, canary conventions, fixture versioning, generator location, rights review, sensitive-fixture approval, schema and contract closure, consumer backlink enforcement, CI ownership, migration plan, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: d6efbbf69a6d2f5a3eeff1512e9c57e2131a12cf
  target_prior_blob: 38438eaab819bf879157f2dbb147b63c12206372
  related_repository_blobs:
    directory_rules: 2affb080e6f0043867c64c7f06c1ca52030fbd55
    tests_root_readme: 5614de99433bca29d6a03d665fb4e00ec23eb5fb
    tests_fixtures_parent_readme: 2d0147e85eae86f687e85c5bea0d3e61f9c3a8f7
    fixtures_root_readme: b096b0ed49c8e7d95ddb0d4c813d06ef40f1528d
    agriculture_reusable_fixture_readme: 68660dfb8e64dc39a146964866f4ddcec36d6e1e
    agriculture_valid_fixture_readme: 8c7401c3169ed6d3fafe2e9a48d28fba482c8f9d
    agriculture_no_network_fixture_readme: 38026f4f535f4b297adce747874391c76e15b22c
    agriculture_no_network_nass_readme: ec233cd32d20e97cd6719cf74a9bab821fb49d4b
    agriculture_domain_tests_readme: 35ebf2a578f2a39b4f4766cc4146aafde8124e67
    agriculture_e2e_readme: a9500ca93564adddab29dfc7e1edceac4d36dc57
    agriculture_schema_test_readme: 345f667c8d1879853e80087f3609c76cf52bde06
    common_schema_fixture_test: b04342cc034d7f1cc554e155fdd02d6e972976e6
    makefile: 4dc8cf633581893d83fba53219c6ea847992e6be
    domain_agriculture_workflow: a9f5f212ef61d72fdc209d9f8b173bbf87fb1803
  direct_lane_files_confirmed:
    - tests/fixtures/domains/agriculture/README.md
  checked_absent_paths:
    - tests/fixtures/domains/README.md
    - tests/fixtures/domains/agriculture/conftest.py
    - tests/fixtures/domains/agriculture/manifest_expectations.json
    - tests/fixtures/domains/agriculture/test_fixture_manifest_shape.py
    - tests/fixtures/domains/agriculture/test_no_network_fixture_loading.py
    - tests/fixtures/domains/agriculture/valid/README.md
    - fixtures/domains/agriculture/valid/valid_1.json
  bounded_inventory_note: direct path checks and bounded repository search establish only the checked snapshot; they do not prove permanent absence from history, ignored files, generated workspaces, branch-local changes, dynamic fixtures, external storage, or uninspected paths
related:
  - ../../README.md
  - ../README.md
  - ../../../README.md
  - ../../../domains/agriculture/README.md
  - ../../../e2e/agriculture/README.md
  - ../../../domains/agriculture/schema/README.md
  - ../../../../fixtures/README.md
  - ../../../../fixtures/domains/agriculture/README.md
  - ../../../../fixtures/domains/agriculture/valid/README.md
  - ../../../../fixtures/domains/agriculture/invalid/README.md
  - ../../../../fixtures/domains/agriculture/no_network/README.md
  - ../../../../fixtures/domains/agriculture/no_network/nass/README.md
  - ../../../../contracts/domains/agriculture/
  - ../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../policy/domains/agriculture/
  - ../../../../docs/runbooks/agriculture/NO_NETWORK_TEST_RUNBOOK.md
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../.github/workflows/domain-agriculture.yml
  - ../../../../Makefile
notes:
  - "v0.2 corrects the stale claim that tests/fixtures/README.md is absent; only tests/fixtures/domains/README.md remains absent at the checked path."
  - "The direct Agriculture test-local fixture lane is README-only in bounded evidence."
  - "Executable tests do not belong in this fixture directory; they belong in their owning tests subtree and consume declarative fixture material by reference."
  - "Reusable Agriculture fixture material remains under fixtures/domains/agriculture/; README-backed child lanes do not prove payload inventory."
  - "The common schema fixture harness does not collect Agriculture-domain schemas or fixtures."
  - "The Makefile fixtures target and domain-agriculture workflow are TODO-only, and the default test target excludes this lane."
  - "This revision changes documentation only and creates no fixture payload, test, schema, contract, policy, validator, workflow behavior, data object, receipt, proof, release record, or public artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<p>
  <img alt="Document status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Direct inventory: README only" src="https://img.shields.io/badge/direct__inventory-README__only-lightgrey">
  <img alt="Scope: test local" src="https://img.shields.io/badge/scope-test__local-blue">
  <img alt="Reusable fixtures: separate root" src="https://img.shields.io/badge/reusable__fixtures-separate__root-purple">
  <img alt="Network: denied by default" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Public posture: aggregate first" src="https://img.shields.io/badge/public-aggregate__first-informational">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture__only-red">
</p>

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#purpose) · [Authority](#authority-and-directory-rules-basis) · [Current state](#confirmed-current-state) · [Home decision](#fixture-home-decision-law) · [Admission](#test-local-fixture-admission-contract) · [Manifest](#minimum-fixture-manifest-contract) · [Consumers](#consumer-backlinks-and-orphan-control) · [Agriculture](#agriculture-invariants) · [Families](#fixture-family-routing) · [Polarity](#valid-invalid-denied-and-abstention-polarity) · [Offline](#no-network-and-nass-posture) · [Cross-lane](#cross-lane-authority-preservation) · [References](#contract-schema-policy-evidence-and-release-references) · [Sensitivity](#rights-sensitivity-and-private-detail) · [Determinism](#identity-version-hash-generation-and-replay) · [Effects](#network-filesystem-and-side-effect-boundary) · [Outcomes](#fixture-test-runtime-policy-and-release-vocabularies) · [Coverage](#inventory-orphans-nonempty-coverage-and-drift) · [CI](#runner-ci-and-promotion-boundary) · [Correction](#correction-withdrawal-supersession-and-rollback) · [Migration](#migration-deprecation-and-lane-retention) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger)

---

## Status and evidence boundary

> [!IMPORTANT]
> **Evidence snapshot:** `main@d6efbbf69a6d2f5a3eeff1512e9c57e2131a12cf`
> **Prior target blob:** `38438eaab819bf879157f2dbb147b63c12206372`
> **Direct lane:** `tests/fixtures/domains/agriculture/README.md` only at the bounded snapshot
> **Parent state:** `tests/fixtures/README.md` exists; `tests/fixtures/domains/README.md` was not found
> **Reusable Agriculture fixture root:** `fixtures/domains/agriculture/`
> **Current collection:** no verified runner or CI target collects this direct lane

The direct lane is currently a routing README, not a confirmed fixture corpus, executable test suite, generator, manifest registry, or validation target.

### Safe conclusions

- **CONFIRMED:** `tests/fixtures/README.md` now exists and defines this tree as unit-test-scoped.
- **CONFIRMED:** `tests/fixtures/domains/README.md` was not found at the checked path.
- **CONFIRMED:** the direct Agriculture lane README exists.
- **CONFIRMED:** checked direct payload, harness, test, and child paths were not found.
- **CONFIRMED:** root `fixtures/` is the cross-cutting/runtime/reusable fixture responsibility root.
- **CONFIRMED:** `fixtures/domains/agriculture/` is the reusable Agriculture fixture index.
- **CONFIRMED:** README-backed Agriculture fixture child lanes exist, but their parent explicitly warns that README presence does not prove payload inventory.
- **CONFIRMED:** the checked reusable `valid/valid_1.json` example was not found.
- **CONFIRMED:** executable test code belongs in the appropriate `tests/` lane, not inside a fixture payload directory.
- **CONFIRMED:** the current common schema harness scans only shared families and `fixtures/contracts/v1/...`; it does not collect Agriculture-domain fixture roots.
- **CONFIRMED:** `make fixtures` is TODO-only.
- **CONFIRMED:** the default `make test` runs `tests/schemas` and `tests/contracts`, not this lane.
- **CONFIRMED:** the `domain-agriculture` workflow executes TODO echo commands.
- **UNKNOWN:** exhaustive payload inventory, generated fixtures, dynamic consumers, current pass rates, fixture coverage, no-network enforcement, and promotion dependency.
- **NEEDS VERIFICATION:** whether this lane should remain a README-only routing boundary or host narrowly scoped declarative fixtures.

### Maturity matrix

| Capability | Status | Evidence-bounded conclusion |
|---|---:|---|
| Direct README | `CONFIRMED` | Routing and safety boundary exists. |
| Direct fixture payloads | `NOT ESTABLISHED` | Representative declarative files were not found. |
| Direct executable tests | `NOT ESTABLISHED / WRONG HOME BY DEFAULT` | Representative tests were not found; parent routes test code elsewhere. |
| Lane-local harness | `NOT FOUND AT CHECKED PATH` | No `conftest.py` was established. |
| Parent fixture README | `CONFIRMED` | Unit-test-scoped fixture split is documented. |
| Domain parent index | `NOT FOUND AT CHECKED PATH` | Hierarchical navigation remains incomplete. |
| Reusable Agriculture fixture root | `CONFIRMED README` | Child lanes are documented; payload completeness is unknown. |
| Agriculture fixture payload inventory | `UNKNOWN` | README presence is not payload proof. |
| Consumer backlinks | `NOT ESTABLISHED` | No direct manifest or consumer map was found. |
| Agriculture schema-fixture coverage | `NOT ESTABLISHED` | Common harness excludes domain Agriculture roots. |
| Network-isolation enforcement | `NOT ESTABLISHED` | Documentation requires no-network; executable denial was not found. |
| Makefile fixture target | `TODO-ONLY` | It regenerates nothing. |
| Agriculture CI | `TODO-ONLY` | Workflow jobs do not validate fixtures. |
| Promotion blocking | `UNKNOWN` | No verified gate depends on this lane. |
| Production/release use | `NOT ESTABLISHED` | Fixtures have no publication authority. |

### Truth labels

| Label | Meaning here |
|---|---|
| `CONFIRMED` | Verified from current repository files, checked paths, or workflow commands. |
| `PROPOSED` | A fixture contract, path, or procedure not established in implementation. |
| `CONFLICTED` | Current roots or docs describe competing or unresolved placement. |
| `UNKNOWN` | Not proven by inspected repository, CI, runtime, or release evidence. |
| `NEEDS VERIFICATION` | Checkable but unresolved strongly enough to act as fact. |
| `DENY` | Disallowed because it creates parallel authority, leaks protected material, or overstates fixture meaning. |

[Back to top](#top)

---

## Purpose

`tests/fixtures/domains/agriculture/` exists to route and, when justified, hold **small declarative Agriculture fixtures that are local to one test area**.

A mature use should look like:

```text
consumer test owns behavior
  -> accepted contract/schema/policy references define expectation
  -> test-local manifest points to a small synthetic fixture
  -> fixture is loaded without network or governed-store access
  -> consumer asserts positive and negative behavior
  -> fixture and consumer remain linked
  -> correction or rollback updates both together
```

This lane may describe or eventually contain:

- fixture manifests;
- tiny JSON, JSONL, YAML, or Markdown inputs;
- expected-output records;
- canary lists;
- case metadata;
- consumer backlink indexes;
- test-local copies only when duplication is explicitly justified.

It does not own:

- executable tests;
- reusable fixture corpora;
- source captures;
- schema or contract authority;
- policy rules;
- Agriculture implementation;
- EvidenceBundles or receipts;
- lifecycle state;
- release records;
- public output.

A fixture pass proves only the bounded expectation named by its consumer.

[Back to top](#top)

---

## Authority and Directory Rules basis

KFM places files by primary responsibility.

| Responsibility | Authority home | This lane's relationship |
|---|---|---|
| Executable Agriculture tests | `tests/domains/agriculture/`, `tests/e2e/agriculture/`, or a more precise test owner | Consumers; executable assertions do not live here by default. |
| Unit-test-scoped Agriculture fixture material | `tests/fixtures/domains/agriculture/` after admission review | This lane. |
| Reusable Agriculture fixture corpora | `fixtures/domains/agriculture/` | Canonical reusable fixture lane. |
| Cross-domain/shared runtime fixtures | `fixtures/` | Shared fixture responsibility root. |
| Agriculture object meaning | `contracts/domains/agriculture/` | Referenced, never redefined. |
| Agriculture machine shape | `schemas/contracts/v1/domains/agriculture/` and accepted shared schema homes | Referenced, never authored here. |
| Agriculture policy | `policy/domains/agriculture/` and accepted policy roots | Referenced, never authored here. |
| Validator implementation | `tools/validators/` | Consumer/helper code, not fixture material. |
| Source registry and source data | governed registry and lifecycle roots | Never copied here as authority. |
| Evidence, receipts, and proofs | accepted evidence/proof/receipt roots | Synthetic references only. |
| Release, correction, withdrawal, rollback | `release/` | Synthetic references only; no decisions here. |
| Generated test artifacts | ephemeral CI or accepted `artifacts/` lane | Not fixture authority. |

### Anti-collapse rules

Do not collapse:

```text
test-local fixture       -> reusable fixture authority
reusable fixture         -> source truth
schema-valid fixture     -> semantic truth
fixture pass             -> source admission
fixture pass             -> evidence closure
fixture pass             -> policy approval
fixture pass             -> release approval
README-backed lane       -> payload inventory
illustrative manifest    -> accepted schema
expected output          -> public artifact
synthetic receipt ref    -> actual receipt
fixture timestamp        -> source freshness
aggregate example        -> field truth
test-local copy          -> canonical copy
```

[Back to top](#top)

---

## Confirmed current state

### Direct lane

Bounded checks establish:

```text
tests/fixtures/domains/agriculture/
└── README.md
```

Representative checked-absent paths:

```text
tests/fixtures/domains/agriculture/conftest.py
tests/fixtures/domains/agriculture/manifest_expectations.json
tests/fixtures/domains/agriculture/test_fixture_manifest_shape.py
tests/fixtures/domains/agriculture/test_no_network_fixture_loading.py
tests/fixtures/domains/agriculture/valid/README.md
```

The prior README's proposed test modules were not implementation facts. More importantly, executable tests are not the default content type for a fixture directory.

### Parent hierarchy

```text
tests/fixtures/README.md          CONFIRMED
tests/fixtures/domains/README.md  NOT FOUND AT CHECKED PATH
```

The prior README incorrectly said both were absent. This revision corrects that drift.

### Reusable Agriculture fixtures

The reusable root documents these child lanes:

```text
catalog/
field_level_attempt/
golden/
hls_vi/
invalid/
nass_quickstats/
no_network/
no_network/nass/
release/
soil_moisture/
ssurgo/
valid/
```

Those are README-backed lanes. Payload completeness, consumer wiring, and test execution remain unestablished unless a child provides stronger evidence.

### Harness and CI

The common contract-fixture harness discovers only:

```text
schemas/contracts/v1/{evidence,runtime,common,policy,source,governance,release}/*.schema.json
fixtures/contracts/v1/<family>/<name>/
```

It does not discover:

```text
schemas/contracts/v1/domains/agriculture/
fixtures/domains/agriculture/
tests/fixtures/domains/agriculture/
```

The Makefile fixture target and Agriculture workflow remain TODO-only, and the default test target excludes this lane.

[Back to top](#top)

---

## Fixture-home decision law

Choose a fixture home by ownership and reuse, not by convenience.

| Question | Route |
|---|---|
| Is the example used by multiple tests, validators, pipelines, runtime checks, or docs? | `fixtures/domains/agriculture/` or another accepted reusable lane. |
| Is it runtime/benchmark corpus material? | Root `fixtures/`, not `tests/fixtures/`. |
| Is it owned by one specific test module or test sublane? | Co-locate beside the test when convention permits, or use this lane with an explicit manifest. |
| Is it only a parametrization or expected-output map for one Agriculture test family? | This lane may be appropriate. |
| Is it an executable assertion, helper library, loader, or generator? | Put it with the owning test/package/tool, not here. |
| Is it a schema valid/invalid family shared by schema tests? | Use the schema-declared fixture root, normally `fixtures/contracts/v1/...` or an accepted domain schema fixture home. |
| Is it real source material or lifecycle data? | Governed source/lifecycle roots, never fixtures. |
| Is it a release, receipt, proof, or evidence record? | Its governed authority root; fixtures may only model a synthetic shape. |
| Is ownership unclear? | Do not create another lane; mark `NEEDS VERIFICATION`. |

### Duplication rule

A test-local copy of a reusable fixture is denied unless the manifest records:

- canonical fixture reference;
- reason a copy is necessary;
- exact transformation;
- content hash;
- upstream version;
- synchronization owner;
- divergence test;
- deprecation plan;
- rollback path.

Prefer a reference, fixture builder owned by the consumer, or parameter overlay over copying a full payload.

[Back to top](#top)

---

## Test-local fixture admission contract

A new declarative file belongs here only when all are true:

1. one identified Agriculture test area owns it;
2. it is not reusable enough for `fixtures/domains/agriculture/`;
3. it is synthetic, minimized, deterministic, and public-safe;
4. no live network, source, lifecycle, or public service is required;
5. the semantic contract and schema posture are named;
6. source role and aggregation posture are explicit;
7. evidence, policy, release, and sensitivity expectations are explicit where material;
8. the consumer path exists or is created in the same change;
9. expected positive or negative behavior is finite;
10. protected-value canaries are synthetic;
11. correction and rollback are possible;
12. CI will collect the consumer before the fixture is called covered.

### Denied admission

Do not admit:

- orphan fixtures with no consumer;
- real source exports;
- copied canonical records;
- large rasters or source caches;
- private parcel/operator/person joins;
- exact sensitive geometry;
- credentials or headers;
- production EvidenceBundles, receipts, proofs, or release records;
- generated CI reports;
- direct model output;
- fixture files whose only purpose is to make a README tree look complete.

[Back to top](#top)

---

## Minimum fixture manifest contract

Each stable test-local fixture should have manifest metadata in a nearby declarative record or README table.

| Field | Requirement |
|---|---|
| `fixture_id` | Stable test-local identity. |
| `fixture_version` | Explicit version or revision. |
| `domain` | `agriculture`. |
| `owner` | Named test or lane owner. |
| `consumer_refs` | Exact test modules or commands. |
| `canonical_fixture_ref` | Reusable source fixture, or `null` with reason. |
| `fixture_family` | Valid, invalid, no-network, aggregate, denial, rollback, and so on. |
| `object_family` | Contract/schema object being modeled. |
| `contract_ref` | Semantic meaning source. |
| `schema_ref` | Machine shape, if applicable. |
| `source_role` | Aggregate, modeled, administrative, observed, synthetic, or accepted vocabulary. |
| `aggregation_unit` | County/state/year/region or `null` with explanation. |
| `audience` | Public, semi-public, steward, restricted, or denied. |
| `rights_posture` | Synthetic/public-safe or explicit restricted test posture. |
| `sensitivity_posture` | Public/generalized/restricted/quarantine or accepted vocabulary. |
| `evidence_posture` | Synthetic EvidenceRef expectation or out-of-scope reason. |
| `policy_posture` | Expected decision/obligations or out-of-scope reason. |
| `release_posture` | Candidate/released/withdrawn/none as synthetic state. |
| `expected_test_result` | `PASS`, `FAIL`, `ERROR`, or accepted test vocabulary. |
| `expected_runtime_outcome` | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, or `null`. |
| `reason_codes` | Stable expected reasons. |
| `must_not_contain` | Synthetic leakage canaries. |
| `network_posture` | `DENY`, mock-only, or explicit controlled profile. |
| `generated_by` | Generator/ref or `hand_authored`. |
| `content_hash` | Digest after canonicalization. |
| `created_at` | Stable creation time. |
| `reviewed_at` | Fixture review time. |
| `supersedes` | Prior fixture version, if any. |
| `rollback_ref` | Reversion or replacement instruction. |

### Illustrative manifest

```json
{
  "fixture_id": "ag-testlocal-aggregate-deny-001",
  "fixture_version": "1",
  "domain": "agriculture",
  "owner": "tests/domains/agriculture/aggregate_only",
  "consumer_refs": [
    "tests/domains/agriculture/aggregate_only/test_public_aggregate.py"
  ],
  "canonical_fixture_ref": null,
  "fixture_family": "aggregate_to_field_denial",
  "object_family": "AgricultureAggregateObservation",
  "contract_ref": "contracts/domains/agriculture/...",
  "schema_ref": "schemas/contracts/v1/domains/agriculture/...",
  "source_role": "aggregate",
  "aggregation_unit": "county-year",
  "audience": "public",
  "rights_posture": "synthetic_public_safe",
  "sensitivity_posture": "public",
  "evidence_posture": "synthetic_ref_required",
  "policy_posture": "deny_field_level_upcast",
  "release_posture": "none",
  "expected_test_result": "PASS",
  "expected_runtime_outcome": "DENY",
  "reason_codes": [
    "AGGREGATE_TO_FIELD_UPCAST_DENIED"
  ],
  "must_not_contain": [
    "FIELD_ID_CANARY",
    "OPERATOR_ID_CANARY",
    "PARCEL_ID_CANARY"
  ],
  "network_posture": "DENY",
  "generated_by": "hand_authored",
  "content_hash": "sha256:NEEDS_VERIFICATION",
  "created_at": "2026-07-16T00:00:00Z",
  "reviewed_at": null,
  "supersedes": null,
  "rollback_ref": "git-revert-owning-change"
}
```

This is a **PROPOSED contract example**, not an accepted schema or proof that the named consumer exists.

[Back to top](#top)

---

## Consumer backlinks and orphan control

A fixture without an identified consumer is an orphan, not coverage.

Every fixture should be reachable from:

```text
fixture -> manifest -> consumer test -> command -> CI job
```

Every consumer should be able to report:

```text
consumer -> fixture ids -> expected cases -> collected count
```

### Required orphan checks

Future tooling should fail or explicitly quarantine when:

- a fixture has no consumer;
- a consumer path no longer exists;
- the manifest names a missing canonical fixture;
- a copied fixture hash diverges without review;
- a fixture is not collected by any command;
- a test discovers zero matching fixtures unexpectedly;
- a required valid or invalid counterpart is absent;
- a fixture is skipped indefinitely;
- a README names a payload that does not exist;
- a payload exists without manifest or intent.

Do not count README files as fixture cases.

[Back to top](#top)

---

## Agriculture invariants

Agriculture fixture cases must preserve these default invariants.

| Invariant | Fixture obligation |
|---|---|
| Aggregate-first public posture | Public-safe Agriculture examples remain aggregate unless an accepted policy explicitly allows a transformed exception. |
| No field/operator upcast | Aggregate statistics cannot become field, operator, parcel, farm, or person truth. |
| Source-role stability | NASS, HLS, SSURGO, soil moisture, administrative, modeled, and synthetic roles remain distinct. |
| Soil authority preserved | SSURGO and soil context do not become Agriculture-owned canonical Soil truth. |
| Hydrology/Atmosphere authority preserved | Context references do not transfer domain authority. |
| Evidence before claim | Claim-like expected output carries support expectations or abstains. |
| Rights and sensitivity fail closed | Unknown rights or sensitive precision blocks public-safe acceptance. |
| Lifecycle separation | Fixtures never participate in RAW-to-PUBLISHED state transitions. |
| Release separation | Release-shaped fixtures do not approve publication. |
| Correction visibility | Corrected, superseded, or withdrawn cases remain traceable. |
| Rollback readiness | Consequential release-shaped cases include a synthetic rollback expectation. |
| AI subordinate | Generated wording is never used as fixture authority or evidence. |

### Agriculture leakage canaries

Use unique synthetic canaries for:

```text
FIELD_ID_CANARY
OPERATOR_ID_CANARY
PARCEL_ID_CANARY
PERSON_LAND_JOIN_CANARY
PROPRIETARY_YIELD_CANARY
PESTICIDE_DETAIL_CANARY
CROP_INSURANCE_DETAIL_CANARY
EXACT_IRRIGATION_CANARY
MAP_TRUTH_CANARY
AI_TRUTH_CANARY
RELEASE_APPROVAL_CANARY
```

Tests must assert absence from every relevant output surface. Never use real protected values as canaries.

[Back to top](#top)

---

## Fixture family routing

| Family | Reusable home | Test-local use here |
|---|---|---|
| Catalog-shaped | `fixtures/domains/agriculture/catalog/` | Tiny expectation overlays for one catalog-closure test. |
| Field-level attempt | `fixtures/domains/agriculture/field_level_attempt/` | Test-specific canary set or expected reason map. |
| Golden output | `fixtures/domains/agriculture/golden/` | Local snapshot only when not reused elsewhere. |
| HLS vegetation index | `fixtures/domains/agriculture/hls_vi/` | Consumer-specific parameter map; preserve remote-sensing role. |
| Invalid | `fixtures/domains/agriculture/invalid/` | Narrow invalid case owned by one test. |
| NASS QuickStats | `fixtures/domains/agriculture/nass_quickstats/` | Local expected aggregation/policy result. |
| No-network | `fixtures/domains/agriculture/no_network/` | Consumer-local network deny manifest. |
| No-network NASS | `fixtures/domains/agriculture/no_network/nass/` | One-test parser/denial expected output if not reusable. |
| Release-shaped | `fixtures/domains/agriculture/release/` | Local correction/rollback expectation map. |
| Soil moisture | `fixtures/domains/agriculture/soil_moisture/` | One-test source-role or time-context overlay. |
| SSURGO | `fixtures/domains/agriculture/ssurgo/` | One-test lineage expectation; Soil authority remains external. |
| Valid | `fixtures/domains/agriculture/valid/` | Local positive case only when its ownership is truly singular. |

The test-local lane should normally point to reusable fixtures rather than shadowing these families.

[Back to top](#top)

---

## Valid, invalid, denied, and abstention polarity

Fixture classification must name the layer being exercised.

| Classification | Meaning | Not implied |
|---|---|---|
| Schema-valid | Matches a machine shape. | Semantic correctness, evidence, policy, release. |
| Contract-valid | Satisfies named semantic invariants. | Policy allowance or source truth. |
| Validator-pass | Passes one validator profile. | All gates closed. |
| Policy-allowed | Allowed for one operation/audience under explicit context. | Release approval. |
| Public-safe | Meets tested exposure obligations. | Universal public safety. |
| Invalid | Expected to fail a named check. | Production incident. |
| Denied | Policy blocks a named operation. | Missing evidence; denial and abstention differ. |
| Abstention | Support is insufficient. | Policy denial. |
| Error | Test/validator/runtime machinery failed. | Denial or abstention. |

A consequential family should include:

- at least one positive control;
- at least one malformed case;
- at least one semantically unsafe but shape-valid case;
- at least one rights/sensitivity failure where material;
- at least one source-role or aggregation collapse case;
- correction or rollback cases when release state is modeled.

Expected-error matching should be specific enough to prove the intended failure.

[Back to top](#top)

---

## No-network and NASS posture

No-network means executable prevention, not merely using a local file.

Future consumers should:

- intercept socket, HTTP, cloud SDK, tile, model, and external-service access;
- fail on undeclared network attempts;
- use deterministic local responses;
- avoid credentials and production endpoints;
- freeze time and source-vintage assumptions;
- prove that fallback logic does not silently call live services;
- record attempted destinations safely;
- clean caches and environment state.

For NASS-shaped cases:

- preserve aggregate source role;
- name aggregation unit and period;
- never infer exact field conditions;
- distinguish fixture vintage from current source state;
- treat missing currentness as abstention or explicit stale state;
- require evidence/citation and aggregation obligations for claim-like expected output;
- deny aggregate-to-field upcasting.

The existing no-network and NASS READMEs do not establish payloads or executable isolation by themselves.

[Back to top](#top)

---

## Cross-lane authority preservation

Agriculture fixtures may reference context from other domains without absorbing authority.

| Context | Authority that remains external | Fixture rule |
|---|---|---|
| Soil / SSURGO | Soil/geology/source lanes | Preserve lineage and source role; do not relabel as Agriculture canonical truth. |
| Hydrology | Hydrology lanes | Reference water context without owning hydrologic truth. |
| Atmosphere/weather | Atmosphere lanes | Preserve issue/valid time and uncertainty. |
| Habitat/ecoregions | Habitat lanes | Context only; no ownership transfer. |
| Flora/fauna | Ecology domain lanes | Avoid species/location leakage and role collapse. |
| Geology/resources | Geology lanes | Context only; do not reinterpret authority. |
| Hazards | Hazard lanes | Preserve event time, alert state, and release posture. |
| People/DNA/Land | Sensitive domain lanes | Deny private joins and precise exposure by default. |
| Roads/rail/trade | Network domain lanes | Preserve network identity and valid-time semantics. |
| Map/UI | Renderer and UI lanes | Display state is not truth. |

A fixture should carry references and expected obligations, not duplicate another domain's canonical record.

[Back to top](#top)

---

## Contract, schema, policy, evidence, and release references

A fixture may model multiple trust layers, but those layers remain separate.

| Reference | What it contributes | What it cannot prove |
|---|---|---|
| Contract ref | Intended object meaning. | Shape validity or policy allowance. |
| Schema ref | Machine shape. | Truth, evidence, rights, or release. |
| Source descriptor ref | Source identity/role/caveats. | Currentness or admission by fixture presence. |
| EvidenceRef | Pointer to support. | EvidenceBundle resolution by itself. |
| EvidenceBundle-shaped fixture | Synthetic support shape. | Actual evidence closure. |
| PolicyDecision-shaped fixture | Expected policy result shape. | That an evaluator ran. |
| ReviewRecord-shaped fixture | Review-state example. | Human approval. |
| ReleaseManifest-shaped fixture | Release-state example. | Publication. |
| Receipt-shaped fixture | Process metadata example. | Actual execution receipt. |
| RollbackCard-shaped fixture | Rollback expectation. | Rollback authorization or execution. |

References should resolve to accepted repository paths where those paths exist. Missing or proposed references must be labeled, not invented.

[Back to top](#top)

---

## Rights, sensitivity, and private detail

Agriculture fixtures must be public-safe by construction.

### Denied material

- real farm, operator, parcel, ownership, insurance, pesticide, irrigation, or yield records;
- living-person identifiers;
- real person-land joins;
- credentials, cookies, private headers, signed URLs;
- proprietary source payloads;
- exact protected infrastructure or ecological locations;
- source data whose license or redistribution rights are unclear;
- actual consent or revocation records;
- production logs and telemetry.

### Safe transformations

Use:

- toy IDs;
- synthetic county/state/year aggregates;
- generalized geometry;
- redacted fields;
- deliberately impossible coordinates when geometry is not under test;
- fictional source names when source identity is irrelevant;
- minimal public-domain snippets only when rights are confirmed and needed;
- explicit `synthetic: true` or equivalent manifest posture.

Rights, consent, sensitivity, and audience are inputs to testing. Fixtures do not decide them.

[Back to top](#top)

---

## Identity, version, hash, generation, and replay

Stable fixtures should support deterministic review and replay.

### Identity

Use stable IDs that are:

- test-local;
- non-secret;
- non-personal;
- unique within the owning lane;
- not confused with canonical domain IDs.

### Versioning

Version when behavior, schema, source role, expected outcome, sensitivity, or generator changes. Do not silently overwrite a fixture used by released tests.

### Hashing

Hash canonicalized content, not filesystem metadata. Record the algorithm and canonicalization profile.

### Generation

Generated fixtures require:

- generator path and version;
- input refs;
- deterministic seed where applicable;
- no-network profile;
- output inventory;
- content digests;
- review state;
- correction and rollback path.

Generator code belongs with tools or the consuming test implementation, not in this fixture payload lane by default.

### Replay

A replay should produce equivalent fixture bytes or an explained, reviewed delta. Time-dependent values must be frozen or explicitly parameterized.

[Back to top](#top)

---

## Network, filesystem, and side-effect boundary

Fixture consumption should be read-only except for declared temporary output.

Denied by default:

```text
live HTTP or socket access
source-system authentication
writes to data/raw
writes to data/work
writes to data/quarantine
writes to data/processed
writes to data/catalog
writes to data/triplet
writes to data/published
writes to release/
writes to data/receipts/
writes to data/proofs/
writes to source registries
writes to public artifact roots
```

Temporary output must use an isolated test directory and be removed after the case. Tests should fail on undeclared writes, undeclared environment changes, lingering caches, or network fallback.

Loading a fixture must not activate a policy bundle, publish an artifact, promote lifecycle state, emit an authoritative receipt, or mutate a canonical store.

[Back to top](#top)

---

## Fixture, test, runtime, policy, and release vocabularies

Keep vocabularies separate.

Fixture disposition:

```text
PRESENT
MISSING
ORPHANED
STALE
SUPERSEDED
WITHDRAWN
QUARANTINED
```

Test result:

```text
PASS
FAIL
SKIP
XFAIL
XPASS
ERROR
```

Runtime outcome:

```text
ANSWER
ABSTAIN
DENY
ERROR
```

Policy decision uses the accepted policy contract and may require normalization from engine-native states.

Release state preserves candidate, released, corrected, withdrawn, superseded, and rolled-back distinctions.

```text
fixture PRESENT     != test PASS
test PASS           != runtime ANSWER
schema-valid        != policy allowed
policy allowed      != release approved
release-shaped      != released
fixture STALE       != source stale unless explicitly modeled
fixture WITHDRAWN   != actual release withdrawal
```

[Back to top](#top)

---

## Inventory, orphans, nonempty coverage, and drift

A mature fixture lane needs machine-checkable inventory.

Future checks should measure:

- payload count by family;
- manifest count;
- consumer backlink count;
- orphan count;
- missing consumer count;
- missing canonical-ref count;
- duplicate ID count;
- hash mismatch count;
- valid/invalid polarity coverage;
- denied/abstention coverage;
- stale/superseded fixture count;
- sensitive-fixture review state;
- no-network consumer count;
- skipped case count;
- last review age.

### Fail-closed conditions

CI should fail when:

- an expected lane collects zero fixtures;
- a required manifest is missing;
- a fixture has no consumer;
- a manifest names a nonexistent consumer;
- a fixture duplicates a reusable fixture without an approved transform;
- valid and invalid cases are indistinguishable;
- synthetic markers are absent where required;
- protected canaries leak;
- source roles change silently;
- expected output is updated without consumer review;
- README inventory drifts from files;
- a deprecated fixture remains active after its removal date.

An intentionally empty routing lane may remain valid only when its README explicitly says it is README-only and no CI target counts it as payload coverage.

[Back to top](#top)

---

## Runner, CI, and promotion boundary

No accepted direct runner currently targets this lane.

Current repository behavior:

```text
make fixtures  -> echo TODO
make test      -> tests/schemas + tests/contracts only
domain-agriculture workflow -> echo TODO steps
common schema harness -> shared contract families only
```

Do not use:

```bash
pytest tests/fixtures/domains/agriculture || true
```

as trust-bearing validation. `|| true` masks failure, and fixture directories should not be assumed to contain executable tests.

### Smallest sound activation sequence

1. decide whether this lane remains README-only;
2. create `tests/fixtures/domains/README.md` if the hierarchy is retained;
3. select one real Agriculture consumer test;
4. decide reusable versus test-local fixture home;
5. create one declarative fixture and manifest;
6. add positive and negative controls;
7. enforce no-network and temporary-filesystem isolation in the consumer;
8. add consumer-backlink and orphan checks;
9. make zero expected fixture collection fatal;
10. wire the consumer test—not the fixture directory—into CI;
11. record counts, skips, and sanitized reports;
12. document correction and rollback.

### CI graduation requirements

A substantive fixture CI path should prove:

- manifest syntax and semantic minimums;
- unique fixture IDs;
- canonical refs and content hashes;
- consumer path existence;
- nonempty expected inventory;
- valid/invalid/deny/abstain polarity;
- no-network execution;
- no governed-root writes;
- synthetic and sensitive-data canaries;
- source-role and aggregate anti-collapse;
- schema/contract reference closure;
- evidence/policy/release separation;
- correction and rollback behavior;
- artifact sanitization;
- exact collected counts and bounded skips.

Fixtures and their tests may block promotion when a trust invariant is material. They cannot approve promotion or release.

[Back to top](#top)

---

## Correction, withdrawal, supersession, and rollback

When a fixture is wrong:

1. mark the issue and affected consumers;
2. stop counting it as valid coverage;
3. create a corrected version;
4. preserve the prior fixture when audit/replay requires it;
5. update manifest hashes and supersession refs;
6. rerun all consumers;
7. invalidate snapshots and reports derived from the old fixture;
8. document whether released code/tests were affected;
9. record rollback to the last accepted fixture version.

Withdraw fixtures containing real or restricted material immediately, preserve only safe audit metadata, and follow governed quarantine/correction procedures.

A fixture rollback is not a data, policy, or release rollback. Each authority remains separate.

[Back to top](#top)

---

## Migration, deprecation, and lane retention

### Retain this lane when

- test-local Agriculture fixtures are an accepted repository convention;
- consumers and manifests are enforceably linked;
- material is not reusable enough for root fixtures;
- a steward owns the split.

### Keep README-only when

- no direct fixture payload has a justified home;
- the directory is useful as a routing boundary;
- parent or historical references still point here.

### Move material when

- multiple consumers appear;
- runtime/benchmark use begins;
- a schema-declared reusable family is established;
- a domain fixture becomes stable;
- another responsibility root is more precise.

Migration steps:

1. identify the authoritative destination;
2. preserve history;
3. add a migration note;
4. update consumer refs and manifests;
5. compare hashes and behavior;
6. remove duplicate copies;
7. update parent indexes and CI;
8. retain a pointer only when useful;
9. document rollback.

Do not create `tests/fixtures/domains/README.md` merely to fill a tree. Create it when it can accurately index real child lanes and state their maturity.

[Back to top](#top)

---

## Definition of done

### This README revision

- [x] Corrects the stale parent-README claim.
- [x] Records the absent domain parent index.
- [x] Records the direct lane as README-only in bounded evidence.
- [x] Removes executable test modules from the proposed fixture layout.
- [x] Separates test-local and reusable fixture homes.
- [x] Records representative absent direct payloads and harness files.
- [x] Records README-backed reusable child lanes without claiming payload inventory.
- [x] Records that the common schema harness excludes Agriculture-domain fixtures.
- [x] Records TODO-only Makefile and Agriculture workflow posture.
- [x] Defines admission, manifest, backlinks, orphan, anti-collapse, no-network, sensitivity, replay, CI, correction, and rollback rules.
- [x] Changes documentation only.
- [ ] Record repository-native CI after PR creation.

### Future operational fixture capability

The capability is not complete until:

- owners and lane retention are accepted;
- the domain parent index decision is resolved;
- each payload has manifest and consumer backlinks;
- reusable versus test-local placement is enforced;
- Agriculture contract/schema references resolve;
- positive and negative controls exist;
- source-role and aggregation collapse tests exist;
- rights/sensitivity review exists;
- no-network and filesystem denial are executable;
- orphan and nonempty checks run;
- correction and rollback are tested;
- CI collects the owning consumer tests;
- counts, skips, runtime, and coverage are measured;
- promotion dependencies are explicit.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| `AG-TFIX-001` | Should this lane remain README-only or host declarative test-local payloads? | `NEEDS VERIFICATION` |
| `AG-TFIX-002` | Is the bounded direct inventory complete? | `NEEDS VERIFICATION` |
| `AG-TFIX-003` | Are fixtures generated or stored outside indexed repository paths? | `UNKNOWN` |
| `AG-TFIX-004` | Should `tests/fixtures/domains/README.md` be created? | `NEEDS VERIFICATION` |
| `AG-TFIX-005` | What exact criterion separates test-local from reusable Agriculture fixtures? | `NEEDS VERIFICATION` |
| `AG-TFIX-006` | What manifest schema and versioning rules are canonical? | `NEEDS VERIFICATION` |
| `AG-TFIX-007` | What fixture ID namespace is accepted? | `NEEDS VERIFICATION` |
| `AG-TFIX-008` | What source-role vocabulary is canonical? | `NEEDS VERIFICATION` |
| `AG-TFIX-009` | What aggregation-unit vocabulary is canonical? | `NEEDS VERIFICATION` |
| `AG-TFIX-010` | What reason-code and canary registries are accepted? | `NEEDS VERIFICATION` |
| `AG-TFIX-011` | Which reusable Agriculture child lanes contain payloads? | `UNKNOWN` |
| `AG-TFIX-012` | Which payloads have active consumers? | `UNKNOWN` |
| `AG-TFIX-013` | How are orphan fixtures detected? | `UNKNOWN` |
| `AG-TFIX-014` | How are copied fixtures synchronized and divergence-tested? | `UNKNOWN` |
| `AG-TFIX-015` | Which Agriculture schemas are canonical and sufficiently strict? | `NEEDS VERIFICATION` |
| `AG-TFIX-016` | What harness validates Agriculture-domain schemas and fixtures? | `UNKNOWN` |
| `AG-TFIX-017` | How is no-network behavior enforced? | `UNKNOWN` |
| `AG-TFIX-018` | How are governed-root writes denied? | `UNKNOWN` |
| `AG-TFIX-019` | What rights review is required for minimized source-derived examples? | `NEEDS VERIFICATION` |
| `AG-TFIX-020` | Who approves sensitive Agriculture fixture cases? | `NEEDS VERIFICATION` |
| `AG-TFIX-021` | How are Soil, Hydrology, Atmosphere, Habitat, and People/Land refs validated? | `UNKNOWN` |
| `AG-TFIX-022` | How are correction, withdrawal, and rollback fixtures versioned? | `NEEDS VERIFICATION` |
| `AG-TFIX-023` | Which consumer tests should run in default CI? | `UNKNOWN` |
| `AG-TFIX-024` | What workflow owns fixture manifest and orphan checks? | `UNKNOWN` |
| `AG-TFIX-025` | What generated reports may be retained, and for how long? | `NEEDS VERIFICATION` |
| `AG-TFIX-026` | Which fixture failures block promotion? | `UNKNOWN` |
| `AG-TFIX-027` | What are current fixture counts, orphan counts, consumer counts, runtime, and pass rates? | `UNKNOWN` |
| `AG-TFIX-028` | What is the deprecation trigger for this lane? | `NEEDS VERIFICATION` |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---:|---|---|
| prior target blob `38438eaa…` | `CONFIRMED` | Existing v0.1 fixture intent. | Current inventory or runner. |
| Directory Rules `2affb080…` | `CONFIRMED DOCTRINE` | Responsibility-root placement and anti-collapse. | Payload presence. |
| tests root `5614de99…` | `CONFIRMED ROOT CONTRACT` | Tests own enforceability. | Fixture completeness. |
| tests/fixtures parent `2d0147e8…` | `CONFIRMED` | Unit-test-local fixture boundary and executable-test exclusion. | Direct Agriculture payloads. |
| fixtures root `b096b0ed…` | `CONFIRMED` | Reusable/runtime fixture responsibility and domain routing. | Agriculture payload coverage. |
| reusable Agriculture root `68660dfb…` | `CONFIRMED README` | Child lane index and fixture-only rules. | Payload inventory or consumers. |
| Agriculture valid README `8c7401c3…` | `CONFIRMED README / PAYLOAD UNKNOWN` | Positive fixture posture. | Valid payload files. |
| checked `valid/valid_1.json` | `NOT FOUND AT CHECKED PATH` | Representative payload is not established. | Exhaustive payload absence. |
| no-network README `38026f4f…` | `CONFIRMED README / EXECUTION UNPROVED` | Offline fixture rules. | Network isolation. |
| no-network NASS README `ec233cd3…` | `CONFIRMED README / PAYLOAD UNKNOWN` | Aggregate NASS posture. | NASS payload or consumer. |
| Agriculture domain tests `35ebf2a5…` | `CONFIRMED DOCUMENTATION` | Expected Agriculture test responsibilities. | Executable fixture consumers. |
| Agriculture E2E `a9500ca9…` | `CONFIRMED README-ONLY LANE` | Governed composition and fixture expectations. | Executable E2E use. |
| Agriculture schema tests `345f667c…` | `CONFIRMED README-ONLY / DRIFT KNOWN` | Schema/fixture closure gaps. | Agriculture schema fixture coverage. |
| common schema harness `b04342cc…` | `CONFIRMED EXECUTABLE` | Shared-family fixture validation behavior. | Domain Agriculture collection. |
| Makefile `4dc8cf63…` | `CONFIRMED TODO/EXCLUSION` | Fixtures target is TODO; default tests exclude this lane. | External or dynamic collection. |
| Agriculture workflow `a9f5f212…` | `CONFIRMED TODO SCAFFOLD` | Workflow exists. | Fixture validation, proof, or dry run. |
| checked direct paths | `CONFIRMED BOUNDED RESULT` | Direct lane README-only conclusion. | Permanent absence across history, branches, generation, or external storage. |

For implementation claims, prefer actual fixture payloads and manifests, consumer tests, direct test results, schema/contract validators, workflow commands/logs, sanitized reports, release records, repository documentation, then plans. README intent cannot outrank payload and execution evidence.

[Back to top](#top)

---

## Maintainer note

Keep this lane small and declarative.

A README is not a fixture corpus. A fixture corpus is not source truth. A schema-valid fixture is not an admissible Agriculture claim. A local file is not proof of no-network execution. A synthetic EvidenceBundle is not evidence closure. A release-shaped example is not released. A copied reusable fixture is not canonical. A fixture with no consumer is not coverage. A green TODO workflow is not validation.

Add one real, reviewable fixture-consumer pair at a time, with explicit ownership, a manifest, synthetic data, positive and negative controls, source-role and aggregation safeguards, no-network enforcement, rights/sensitivity review, deterministic replay, correction, rollback, and substantive CI.

<p align="right"><a href="#top">Back to top</a></p>
