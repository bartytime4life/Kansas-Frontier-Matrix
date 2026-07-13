<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-kdwp-tests-readme
title: connectors/kdwp/tests/ — KDWP Greenfield Connector Test Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Test steward · Kansas/KDWP source steward · Fauna steward · Flora steward · Habitat steward · Rights reviewer · Privacy/sensitivity reviewer · Security reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-07-13
policy_label: public-doctrine; connector-local-tests; greenfield-scaffold; compatibility-path; canonical-family-migration; product-and-role-conflict; no-network; synthetic-fixtures; rights-fail-closed; sensitivity-fail-closed; no-activation; no-publication
current_path: connectors/kdwp/tests/README.md
truth_posture: CONFIRMED README-only inspected test lane, named conventional test files absent, 0.0.0 parent package scaffold, empty initializer, comment-only fetch/admit files, four-field local descriptor, absent named package scaffold below the Kansas-family KDWP lane, empty source-authority register, schema conflict, and TODO-only connector workflows / CONFLICTED final connector-local test home, package migration, product dispatch, SourceDescriptor machine authority, narrative-to-machine role mapping, fixture routing, and cross-system test ownership / PROPOSED fail-closed connector-local test contract / UNKNOWN differently named tests, package runtime, source access, activation, current rights, sensitive-location transforms, substantive CI coverage, deployment, and release readiness
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: d2c7141f7b26f02e378de2c1c9666914d12d08e0
  prior_blob: 09c3ba43fd8e8eee81031747482545449f28fb20
  readme_introduction_commit: c5be0d8977e4cf62c84028498cae3a5ef53667af
related:
  - ../../README.md
  - ../README.md
  - ../pyproject.toml
  - ../src/README.md
  - ../src/kdwp/README.md
  - ../src/kdwp/descriptor.yaml
  - ../../kansas/README.md
  - ../../kansas/kdwp/README.md
  - ../../kansas/kdwp_flora/README.md
  - ../../kansas/kdwp_ert/README.md
  - ../../../CONTRIBUTING.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/connector-gate.yml
  - ../../../.github/workflows/source-descriptor-validate.yml
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../../docs/sources/catalog/kansas/kdwp.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../data/registry/sources/habitat/kdwp.yaml
  - ../../../data/registry/fauna/sources/kdwp_species.yaml
  - ../../../control_plane/source_authority_register.yaml
  - ../../../tests/README.md
  - ../../../fixtures/README.md
  - ../../../policy/rights/README.md
  - ../../../policy/sensitivity/README.md
  - ../../../release/
tags: [kfm, connectors, kdwp, tests, kansas, wildlife, sinc, listed-species, fauna, flora, habitat, greenfield, compatibility, source-admission, source-role, rights, sensitivity, no-network, fixtures, raw, quarantine, no-publication]
notes:
  - "Direct reads at base commit d2c7141f7b26f02e378de2c1c9666914d12d08e0 confirm this README, project version 0.0.0, an empty __init__.py, comment-only fetch.py and admit.py files, and a four-field descriptor.yaml placeholder."
  - "Exact probes at the pinned base returned Not Found for connectors/kdwp/tests/__init__.py, conftest.py, test_fetch.py, test_admit.py, test_descriptor.py, and tests/fixtures/README.md."
  - "Exact probes below connectors/kansas/kdwp/ returned Not Found for pyproject.toml, src/README.md, and tests/README.md; the Kansas-family lane is a coordination README, not verified package or test implementation."
  - "The local descriptor uses deprecated minimal aliases, leaves role and rights unresolved, and asserts sensitivity_floor: public; tests must treat it as an invalid negative input, not source authority or public-safety evidence."
  - "The machine source-authority register contains entries: []; the populated singular SourceDescriptor schema labels the plural path canonical while the plural schema is an empty PROPOSED scaffold; narrative and machine role vocabularies remain unratified."
  - "The connector-gate and source-descriptor-validate workflows execute TODO echo steps; a green run cannot establish KDWP test coverage or governance enforcement."
  - "Only this Markdown file is in scope. No test, fixture, code, package metadata, schema, contract, policy, descriptor, registry entry, workflow, receipt, source activation, path move, release object, or public artifact is created or changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KDWP Greenfield Connector Test Boundary

> [!IMPORTANT]
> **Document lifecycle:** `draft v0.2`  
> **Current test maturity:** README-only inspected lane; executable tests were not found at the named conventional paths  
> **Package maturity:** `0.0.0` greenfield scaffold; no supported fetch, parser, admission, candidate-envelope, or lifecycle behavior  
> **Path posture:** the top-level package is a compatibility scaffold, while the Kansas-family KDWP lane is the current coordination path; package and test migration remain `CONFLICTED / NEEDS VERIFICATION`  
> **Boundary:** this folder may eventually hold narrow package-owned tests. It does not activate KDWP, prove source access, establish descriptor authority, validate a real sensitive record, approve public precision, or authorize release.

> [!WARNING]
> A README, local placeholder descriptor, source-catalog statement, green workflow, or directory name is not test coverage. Until executable tests, safe fixtures, an accepted runner, and observed results exist, package behavior remains `UNKNOWN` and source activation remains denied.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#current-status) · [What belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#test-inputs) · [Outputs](#test-outputs) · [Product boundaries](#kdwp-product-and-role-test-boundaries) · [Fixtures](#fixture-and-sensitive-data-contract) · [Failure contract](#failure-contract) · [Validation](#validation) · [Review](#review-burden) · [Evidence](#evidence-basis) · [Definition of done](#definition-of-done) · [Rollback](#rollback) · [Backlog](#verification-backlog)

---

## Purpose

`connectors/kdwp/tests/` is the repository-present test-documentation lane beside the non-operational `connectors/kdwp/src/kdwp/` package scaffold.

Its narrow purpose is to define what **connector-local** tests must prove if the compatibility package is retained, redirected, or migrated:

- importing or inspecting the package causes no network, credential, filesystem, lifecycle, evidence, release, or publication side effect;
- the connector-local descriptor placeholder is rejected as authority and as public-safety evidence;
- KDWP product identity, source role, rights, sensitivity, geometry, time, source head, attribution, and disclaimer fields are preserved rather than upgraded;
- listed-status, SINC-rank, range, observation, habitat/stewardship, ecological-review, and operational products remain distinct;
- package helpers return bounded, caller-owned candidate outcomes rather than writing lifecycle state;
- sensitive ecological and private-location information fails closed;
- compatibility behavior does not silently create a second KDWP implementation or settle unresolved package/test migration by convenience.

This folder is not the canonical home for all KDWP, Fauna, Flora, Habitat, policy, release, source-admission, or end-to-end tests. Cross-system enforceability belongs under the canonical [`tests/`](../../../tests/README.md) responsibility root and its accepted source, policy, domain, pipeline, release, API, UI, and runtime-proof lanes.

[Back to top](#top)

---

## Authority level

**Connector-local test lane inside a noncanonical greenfield package scaffold. It has no source, schema, policy, lifecycle, evidence, release, or publication authority.**

| Concern | Status | Evidence-bounded determination |
|---|---:|---|
| Owning responsibility | **CONFIRMED** | Small package-owned behavior tests may live beside a retained package; canonical cross-system enforceability belongs under root `tests/`. |
| Current path | **CONFIRMED** | `connectors/kdwp/tests/README.md` exists at the pinned base. |
| Current executable tests | **NOT FOUND AT NAMED PROBES / OTHERWISE UNKNOWN** | Direct reads found this README but not the conventional modules listed in the current snapshot. |
| Current package behavior | **GREENFIELD PLACEHOLDER** | Project version `0.0.0`, empty initializer, comment-only fetch/admit modules, and minimal metadata establish no runnable behavior. |
| Kansas-family KDWP lane | **CONFIRMED COORDINATION / PACKAGE DEPTH UNKNOWN** | `connectors/kansas/kdwp/README.md` exists; named `pyproject.toml`, `src/README.md`, and `tests/README.md` paths below it were absent at this base. |
| Product/test layout | **CONFLICTED** | KDWP, KDWP Flora, KDWP ERT, top-level compatibility, and Kansas-family coordination surfaces exist without an accepted final package and test topology. |
| Descriptor/schema authority | **CONFLICTED / NOT ESTABLISHED FOR KDWP** | Local metadata is nonconforming; registry files are placeholders; the populated singular schema calls itself legacy; the plural schema is empty; the machine authority register has no entries. |
| Source-role vocabulary | **CONFLICTED** | Narrative doctrine uses `authority`, `regulatory`, `observed`, `context`, and `model`; the populated schema uses different machine values. No accepted mapping was found in scope. |
| Source activation | **DENIED / NOT VERIFIED** | No approved product descriptor, source head, rights/sensitivity review, activation decision, or executable gate was verified. |
| Public release | **NONE** | Connector-local tests cannot approve a listed-status claim, occurrence, range layer, ecological-review result, map, API response, receipt, proof, or release. |

Editing this existing README does not ratify the top-level package, the Kansas-family implementation layout, any product lane, descriptor, role mapping, fixture home, or test runner.

[Back to top](#top)

---

## Current status

### Bounded repository snapshot

The following snapshot is bounded to repository `bartytime4life/Kansas-Frontier-Matrix` at base commit `d2c7141f7b26f02e378de2c1c9666914d12d08e0` and the exact paths inspected for this revision:

```text
connectors/kdwp/
├── README.md                           # top-level compatibility documentation
├── pyproject.toml                      # kfm-connector-kdwp, version 0.0.0
├── src/
│   ├── README.md                       # compatibility source-layout boundary
│   └── kdwp/
│       ├── README.md                   # greenfield package boundary
│       ├── __init__.py                 # empty
│       ├── fetch.py                    # comment-only placeholder
│       ├── admit.py                    # comment-only placeholder
│       └── descriptor.yaml             # four-field nonconforming placeholder
└── tests/
    └── README.md                       # this documentation contract
```

Exact probes returned `Not Found` for:

```text
connectors/kdwp/tests/__init__.py
connectors/kdwp/tests/conftest.py
connectors/kdwp/tests/test_fetch.py
connectors/kdwp/tests/test_admit.py
connectors/kdwp/tests/test_descriptor.py
connectors/kdwp/tests/fixtures/README.md
connectors/kansas/kdwp/pyproject.toml
connectors/kansas/kdwp/src/README.md
connectors/kansas/kdwp/tests/README.md
```

These absence statements are bounded to the pinned commit and named paths. Differently named, generated, unindexed, or later-added files remain `UNKNOWN`.

### Current maturity table

| Item | Current state | Safe conclusion |
|---|---|---|
| This README | **DRAFT v0.2** | Reviewable boundary documentation only. |
| Test runner | **NOT DECLARED** | `pyproject.toml` declares no build backend, dependencies, supported Python version, package discovery, command, or test framework. |
| Import tests | **NOT FOUND** | No import-safety behavior is proven. |
| Fetch tests | **NOT FOUND** | No no-network, host, timeout, retry, rate-limit, response-size, content-type, source-head, or payload-logging behavior is proven. |
| Admission tests | **NOT FOUND** | No descriptor gate, activation gate, finite outcome, quarantine, receipt, or candidate-handoff behavior is proven. |
| Descriptor tests | **NOT FOUND** | The local placeholder remains unsafe and unvalidated as an activation input. |
| Fixtures | **NO CONNECTOR-LOCAL FIXTURE README FOUND** | No fixture rights, sensitivity, provenance, generation, minimization, or expected-outcome record was verified. |
| Connector workflows | **TODO-ONLY STUBS** | `connector-gate` and `source-descriptor-validate` currently run `echo TODO ...`; success proves workflow execution only. |
| Package runtime | **ABSENT / UNKNOWN** | No supported command, callable API, source client, parser, output DTO, sink, or runtime log was verified. |
| Source activation and public use | **DENIED BY DEFAULT** | Repository presence does not authorize access, admission, evidence use, ecological review, or release. |

[Back to top](#top)

---

## What belongs here

Only after package placement and test routing are accepted, this connector-local lane may contain small tests for behavior owned by the retained package, such as:

- import and module smoke tests with no network or side effects;
- deterministic tests for package-local pure parsing, source-head, checksum, identity-preservation, and candidate-envelope helpers;
- tests that reject the local four-field descriptor as source authority, activation state, sensitivity clearance, or release permission;
- tests that require caller-supplied, conforming, reviewed, product-specific descriptor and activation references;
- no-network transport tests using explicit fakes or approved synthetic responses;
- tests that preserve source-native product, record, taxon/community, status/rank, observation, geometry, uncertainty, time, rights, attribution, and disclaimer fields;
- product-dispatch and role anti-collapse tests after the machine role vocabulary is accepted;
- tests that return explicit admit-candidate, hold/quarantine-candidate, deny, abstain, no-op, rate-limit, or error outcomes without selecting or writing lifecycle sinks;
- package compatibility tests only when an accepted migration retains the top-level `kdwp` namespace;
- small expected outputs that are clearly synthetic and do not become registry, receipt, proof, policy, evidence, catalog, or release authority.

Executable tests must be paired with an accepted runner, documented fixture home, observable CI command, and negative coverage before implementation maturity is claimed.

[Back to top](#top)

---

## What does not belong here

This folder must not contain or become:

- live KDWP source payloads, bulk downloads, private exports, or unreviewed upstream samples;
- real exact sensitive taxa, nests, dens, roosts, hibernacula, spawning sites, rare plants, natural communities, private-land records, landholder data, or sensitive facilities;
- credentials, cookies, access tokens, account details, private endpoints, signed URLs, or secrets in source, fixtures, logs, snapshots, or exceptions;
- production connector code, package metadata, runtime configuration, caches, or downloaded source files;
- authoritative `SourceDescriptor` instances, source-authority entries, activation decisions, rights decisions, sensitivity decisions, redaction profiles, or policy bundles;
- a second schema, contract, policy, source registry, fixture authority, receipt, proof, catalog, release, or publication home;
- direct writes to `data/raw/`, `data/quarantine/`, `data/work/`, `data/receipts/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/proofs/`, `data/published/`, or `release/`;
- tests that contact live sources by default or require internet access to pass;
- tests that convert a successful fetch, parse, validation, Git commit, workflow, map, tile, graph edge, AI summary, or README statement into source truth or release approval;
- cross-system tests that silently make this local lane the owner of Fauna, Flora, Habitat, taxonomy, legal status, sensitivity policy, ecological review, rights, release, or public precision;
- operational hunting/fishing, closure, emergency, legal, land-use, ecological-clearance, or life-safety advice.

Use the canonical responsibility root that owns each concern.

[Back to top](#top)

---

## Test inputs

### Current inputs

None. No executable test module, fixture contract, command, runner, package API, endpoint, descriptor resolver, activation resolver, or output DTO is established by the inspected lane.

### Future admissible inputs

After placement, package, descriptor, fixture, and runner decisions are accepted, connector-local tests may consume:

- package modules owned by the retained KDWP connector;
- a conforming, reviewed, product-specific descriptor reference or a deliberately invalid descriptor fixture;
- an explicit activation-state fixture for fixture-only, restricted, denied, or reviewed-live operation;
- synthetic or explicitly rights-cleared source-response fixtures;
- exact KDWP program/product identity and source-native identifiers;
- source-head evidence such as release date, checksum, `ETag`, `Last-Modified`, or reviewed manual version;
- source, observed, validity/effective, retrieval, and correction time where material;
- rights, attribution, sensitivity, geometry, precision, uncertainty, withholding, and reviewer references;
- caller-owned in-memory candidate sinks or test doubles;
- expected finite outcome and reason-code fixtures.

Inputs must be minimized, deterministic, offline by default, and incapable of disclosing a real sensitive locality.

[Back to top](#top)

---

## Test outputs

A connector-local test may produce only ephemeral assertions, test-run output, or disposable expected values.

It may verify that a future package returns:

- a deterministic source-head or probe result;
- a parse result that preserves source-native meaning;
- a `RAW` handoff **candidate** when identity, role, rights, sensitivity, source head, and activation are sufficiently resolved;
- a `QUARANTINE` handoff **candidate** with a structured reason when they are not;
- an explicit deny, abstain, no-op, rate-limit, or error outcome;
- a receipt candidate only when an accepted contract exists and the test does not persist it as authority.

Connector-local tests must not create or approve lifecycle data, EvidenceBundles, policy decisions, catalog/triplet records, releases, public geometry, maps, API responses, ecological-review results, or AI answers.

[Back to top](#top)

---

## KDWP product and role test boundaries

KDWP is a source family, not one homogeneous test fixture. The labels below describe narrative source-document posture only; they are not approved machine enum values.

| Product or record class | Required test distinction | Denied collapse |
|---|---|---|
| Listed, endangered, threatened, SINC, and other status artifacts | Preserve issuing program, instrument/list identity, effective date, taxon/community identity, source head, citation, rights, and review state. | Regulatory or stewardship context treated as an observation or unrestricted location grant. |
| SINC ranks and sensitivity inputs | Preserve rank vocabulary/version, identity, effective date, disagreement state, citation, and steward provenance. | Rank treated as public-release permission or proof of current local presence. |
| Range and spatial-status products | Preserve product/version, scale, vintage, support type, geometry, uncertainty, taxon identity, and disclaimer. | Range polygon treated as a dated occurrence or exact sensitive locality. |
| Survey, monitoring, mortality, or disease observations | Preserve program/event identity, observation time, taxon identity, geometry, uncertainty, withholding state, and source-native identifiers. | Observation treated as legal status, complete population truth, or unrestricted public point. |
| Habitat, natural-community, or stewardship layers | Preserve product identity, source role, model/compilation status, scale, vintage, geometry/support, and rights. | Context polygon treated as per-place occurrence or final habitat truth. |
| Ecological Review Tool or related review output | Preserve tool/product version, input scope, rule/model version, review date, disclaimer, source refs, output class, and steward state. | Output treated as permit, legal clearance, complete absence finding, or release approval. |
| Operational notices, seasons, closures, or transient advisories | Preserve product identity, source time, expiry, intended use, and not-for-life-safety posture. | KFM treated as current official or emergency channel. |

Minimum anti-collapse assertions:

1. one publisher name does not produce one publisher-wide descriptor, role, rights state, sensitivity state, or cadence;
2. mixed products or records split by governed identity and role or fail closed;
3. regulatory/listed-status context remains distinct from observed events;
4. range and habitat context remain distinct from occurrences;
5. ERT/review output remains distinct from legal clearance and release approval;
6. federal status, NatureServe rank, taxonomy backbone, and aggregator provenance retain their own authority;
7. maps, tiles, summaries, joins, dashboards, and AI explanations remain downstream carriers.

[Back to top](#top)

---

## Fixture and sensitive-data contract

A fixture is allowed only when it is:

- fully synthetic and plainly marked as non-real;
- minimized to the fields required by the test;
- rights-cleared or generated without upstream proprietary content;
- generalized, withheld, or fictionalized so it cannot reveal or reconstruct a sensitive locality;
- paired with expected outcome, sensitivity posture, source-role intent, and generation/provenance notes;
- stable under deterministic hashing or canonicalization when identity is tested;
- free of credentials, tokens, private URLs, living-person data, landholder identity, real private coordinates, and restricted media.

Fixture suites should include negative-first cases for:

- unknown rights or redistribution;
- unresolved sensitivity or withholding;
- exact sensitive geometry;
- invalid or missing taxon/community identity;
- mixed product or role content;
- missing listed-status instrument or effective date;
- range-as-occurrence collapse;
- ERT-as-legal-clearance collapse;
- missing source head, source URI, citation, or disclaimer;
- stale or superseded product version;
- missing activation state;
- forbidden lifecycle or public-output target;
- accidental payload or geometry echo in logs and exceptions.

The local `descriptor.yaml` value `sensitivity_floor: public` is a required negative case: tests must reject any attempt to use it as record-level sensitivity, public precision, redaction, or release authority.

[Back to top](#top)

---

## Failure contract

A future connector test suite must prove deterministic failure without echoing sensitive payload content. Minimum reason families include:

- unresolved package/test migration or product identity;
- missing, nonconforming, unreviewed, superseded, or inactive descriptor;
- missing activation decision or disallowed activation mode;
- unknown product, unsupported source shape, source-head mismatch, or stale source;
- unresolved narrative-to-machine role mapping;
- unresolved rights, attribution, redistribution, cadence, disclaimer, or sensitivity;
- missing taxon/community, listed-status, rank, observation/event, source URI, citation, temporal, geometry, uncertainty, or withholding context;
- mixed regulatory, observed, context, modeled, administrative, operational, or review-tool material without a governed split;
- denied network posture, unapproved host, unsafe credential handling, oversized response, unexpected content type, or payload logging;
- attempted lifecycle persistence, evidence/release creation, public output, or sensitive-location exposure;
- reliance on `sensitivity_floor: public` from the local placeholder.

Unknowns route to `DENY`, `ABSTAIN`, `HOLD`, `ERROR`, or a `QUARANTINE` candidate. They never receive permissive defaults.

[Back to top](#top)

---

## Validation

No package build, install, import, or test command is documented because none is supported by the inspected project metadata.

Before test maturity can be claimed, evidence must cover:

1. accepted KDWP package location, import name, product topology, compatibility class, and losing-path migration;
2. complete recursive package, test, fixture, workflow, and backlink inventory;
3. build backend, package discovery, supported Python versions, dependency policy, entry points, test framework, and clean install/import;
4. accepted `SourceDescriptor` schema/contract authority and narrative-to-machine role mapping;
5. product-specific descriptors, source-authority/registry state, source heads, reviews, and activation decisions;
6. current source access methods, formats, schemas, terms, attribution, redistribution, cadence, rate limits, correction, and withdrawal behavior;
7. no-network default plus host, credential, timeout, retry, response-size, content-type, redirect, cache, and payload-logging controls;
8. synthetic or rights-cleared fixtures with listed-status, role, rights, sensitivity, exact-location, withholding, taxonomy, time, geometry, and malformed-input negative cases;
9. product and role anti-collapse coverage for lists/ranks, ranges, observations, habitat/stewardship surfaces, ERT/review outputs, and operational notices;
10. deterministic `RAW`/`QUARANTINE` candidate, idempotency, no-op, denial, and lifecycle-boundary behavior;
11. proof that connector code and local tests cannot create policy, evidence, catalog, release, public map/API/UI, or AI authority;
12. substantive package-specific test discovery and CI execution, including negative coverage and failure evidence;
13. correction, supersession, invalidation, deactivation, migration, and rollback tests.

The current `connector-gate` and `source-descriptor-validate` workflows are TODO-only scaffolds. Their successful status cannot be used as evidence that this package, descriptor, rights, sensitivity, fixture safety, or lifecycle boundary was tested.

Documentation checks for this revision should include one H1, balanced fenced blocks, working repository-relative links, no remote badge/image dependencies, no credential-like strings, a final newline, and an exact one-file diff.

[Back to top](#top)

---

## Review burden

Review this lane as source-access, product-identity, source-role, rights, sensitivity, privacy, exact-location, test-data, security, lifecycle-boundary, and migration work—even when the diff is documentation-only.

Minimum reviewers remain `OWNER_TBD`, but the intended review roles are:

- connector/package maintainer;
- KDWP/Kansas source steward;
- Fauna, Flora, and Habitat stewards for affected product classes;
- rights and attribution reviewer;
- privacy/sensitivity and public-precision reviewer;
- security reviewer for network, secret, logging, and fixture posture;
- test/validation steward;
- docs steward;
- release steward only when release-boundary tests are in scope.

A connector-local green test run cannot replace cross-system policy, evidence, release, or public-surface review.

[Back to top](#top)

---

## Evidence basis

Evidence for this revision is bounded to repository `bartytime4life/Kansas-Frontier-Matrix` at base commit `d2c7141f7b26f02e378de2c1c9666914d12d08e0`.

| Evidence | Status | Supports | Does not support |
|---|---:|---|---|
| Target README and history | **CONFIRMED** | Prior blob `09c3ba43fd8e8eee81031747482545449f28fb20`; substantive README introduced by commit `c5be0d8977e4cf62c84028498cae3a5ef53667af`. | Runtime, test execution, source access, descriptor validity, or release. |
| [`pyproject.toml`](../pyproject.toml) | **CONFIRMED** | Project name `kfm-connector-kdwp` and version `0.0.0`. | Buildability, dependencies, supported Python, package discovery, API, runner, or command. |
| Exact package-file reads | **CONFIRMED** | Empty initializer, comment-only fetch/admit placeholders, four-field descriptor placeholder. | Executable fetch, parse, admission, candidate output, or lifecycle behavior. |
| Exact connector-local test probes | **CONFIRMED absent at base** | Named conventional tests and local fixture README were not found. | Permanent nonexistence or absence of differently named/unindexed files. |
| [`connectors/kansas/kdwp/README.md`](../../kansas/kdwp/README.md) plus exact probes | **CONFIRMED coordination / named package paths absent** | Kansas-family KDWP lane exists; named package and tests scaffold was not found below it. | Accepted package/test migration, product layout, or runtime. |
| [`docs/sources/catalog/kansas/kdwp.md`](../../../docs/sources/catalog/kansas/kdwp.md) | **CONFIRMED draft** | KDWP source-family, product, role, sensitivity, and Kansas-family placement doctrine. | Current endpoints, terms, valid machine roles, descriptor admission, fixture safety, or activation. |
| `SourceDescriptor` contract and populated singular schema | **CONFIRMED draft/PROPOSED** | Rich descriptor surface, deprecated aliases, closed-object and fail-closed constraints. | Accepted plural-path migration, persisted KDWP descriptors, or runtime enforcement. |
| Plural schema | **CONFIRMED empty PROPOSED scaffold** | Current schema-path conflict. | Meaningful validation or canonical migration completion. |
| KDWP registry placeholder files | **CONFIRMED** | Placeholder/template state. | Registry admission, product identity, rights, sensitivity, source head, activation, or release. |
| Source-authority register | **CONFIRMED** | Register is `PROPOSED` and contains `entries: []`. | Any KDWP authority or activation decision. |
| Root [`tests/`](../../../tests/README.md) doctrine | **CONFIRMED documentation** | Canonical cross-system enforceability belongs under the test responsibility root. | Executable inventory, runner, coverage, or passing CI. |
| Connector and descriptor workflows | **CONFIRMED TODO-only** | Workflow names and pull-request triggers exist. | Substantive package, descriptor, rights, sensitivity, or lifecycle validation. |

Not inspected: live KDWP services or portals, current terms pages, credentials, source payloads, private or sensitive records, real exact coordinates, differently named executable tests, runtime logs, deployed configuration, emitted receipts, EvidenceBundles, release manifests, or public clients. Treat associated claims as `UNKNOWN` or `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Definition of done

### Documentation boundary

- [x] Current README-only test state and exact named absence probes are explicit.
- [x] Parent `0.0.0` package and placeholder modules are not overstated.
- [x] Kansas-family coordination and unresolved package/test migration are separated.
- [x] Connector-local tests and canonical cross-system `tests/` ownership are separated.
- [x] Descriptor/schema/registry/role/workflow conflicts and default-deny result are explicit.
- [x] Product, source-role, rights, sensitivity, exact-location, ERT, operational, and public-use anti-collapse rules are explicit.
- [x] Current inputs, outputs, commands, runner, fixtures, tests, activation, lifecycle behavior, and publication are stated as absent or unknown.
- [x] Evidence limits, review burden, migration discipline, and rollback target are recorded.

### Implementation readiness

- [ ] Package/test location, import/product identity, and losing-path migration are accepted.
- [ ] Owners and required reviewers are assigned.
- [ ] Build, install, supported-runtime, dependency, entry-point, package API, and test-runner contracts exist.
- [ ] `SourceDescriptor` machine authority and narrative-to-machine role mapping are accepted.
- [ ] Product-specific descriptors, authority/registry records, source heads, review states, rights, sensitivity, and activation decisions exist.
- [ ] Current source access, formats, schemas, terms, attribution, redistribution, cadence, rate limits, correction, and withdrawal are reviewed.
- [ ] Sensitive-location, private-land/living-person, geometry, uncertainty, withholding, redaction, and public-precision policy is executable.
- [ ] Product dispatch, parsing, candidate-envelope, no-op, denial, and lifecycle-boundary behavior is implemented.
- [ ] Default tests are offline, deterministic, synthetic or rights-cleared, minimized, negative-first, and CI-discovered.
- [ ] Connector and descriptor workflows execute substantive checks rather than TODO steps.
- [ ] Cross-system policy, evidence, release, API/UI, correction, deactivation, migration, and rollback tests exist in accepted canonical lanes.

Until every applicable implementation-readiness item closes, keep this lane documentation-only and fail closed.

[Back to top](#top)

---

## Rollback

Rollback this README revision if it is used to:

- claim executable tests, fixtures, runner, CI enforcement, source access, or activation that does not exist;
- ratify a package or test path without an accepted migration;
- activate the local descriptor or infer public safety from `sensitivity_floor: public`;
- permit live-network default tests, secrets, sensitive payloads, exact locations, or harmful joins;
- collapse listed-status/rank, range, observation, habitat/stewardship, ERT, or operational products;
- create lifecycle, evidence, policy, catalog, release, public map/API/UI, or AI authority from connector-local tests.

Before merge, close the draft change and abandon its scoped branch if rejected. After merge, create a transparent revert of the documentation commit; do not reset, force-push, or rewrite shared history. The baseline target blob is `09c3ba43fd8e8eee81031747482545449f28fb20` at base commit `d2c7141f7b26f02e378de2c1c9666914d12d08e0`.

[Back to top](#top)

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Complete recursive test and fixture inventory. | **NEEDS VERIFICATION** | Git tree or mounted checkout at the review commit. |
| Final KDWP package and connector-local test home. | **CONFLICTED / NEEDS VERIFICATION** | Accepted ADR or migration plan. |
| Product topology across KDWP, Flora, ERT, and compatibility lanes. | **CONFLICTED** | Accepted product/source-ID and ownership decision. |
| Build backend, package discovery, dependencies, supported Python, and test runner. | **UNKNOWN** | Implemented project metadata and clean install/test evidence. |
| `SourceDescriptor` schema authority and role mapping. | **CONFLICTED** | Accepted ADR, populated canonical schema, validator, fixtures, and tests. |
| Product-specific descriptors, registry/authority state, and activation. | **NOT VERIFIED** | Reviewed records and activation decisions. |
| Current access methods, formats, terms, rights, attribution, cadence, and source heads. | **NEEDS VERIFICATION** | Source-steward and rights review. |
| Sensitive geometry, withholding, redaction, public precision, and ERT legal-use policy. | **NEEDS VERIFICATION** | Executable policy, approved fixtures, receipts, and negative tests. |
| Connector-local fixture home and fixture receipt/provenance contract. | **NEEDS VERIFICATION** | Accepted fixture-routing decision and reviewed files. |
| Substantive CI discovery and negative coverage. | **UNKNOWN** | Workflow steps, jobs, logs, and failure evidence. |
| Finite outcome, candidate-envelope, idempotency, no-op, logging, and reason-code contracts. | **PROPOSED / NEEDS VERIFICATION** | Contracts, code, fixtures, and tests. |
| Correction, deactivation, supersession, migration, and rollback behavior. | **NEEDS VERIFICATION** | Implemented workflows and drills. |

[Back to top](#top)

---

## Maintainer note

Keep this lane small, offline, negative-first, and reversible. Connector-local tests should prove retained package behavior without becoming source, policy, fixture, evidence, lifecycle, or release authority. Cross-system trust-spine enforcement belongs under the canonical `tests/` responsibility root.

<p align="right"><a href="#top">Back to top</a></p>
