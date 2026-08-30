<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ahgp-tests-readme
title: connectors/ahgp/tests/ — AHGP Connector Test Boundary
type: readme; directory-readme; test-routing-boundary
version: v1.0.0
status: repository-grounded; documentation-only; no-executable-tests; unindexed-local-suite; non-release; non-publication
owner: NEEDS VERIFICATION — connector, source, genealogy, rights, sensitivity, test, and independent review stewardship are not established
created: 2026-08-29
updated: 2026-08-29
current_path: connectors/ahgp/tests/README.md
owning_root: connectors/ahgp/
policy_label: public; test-routing; no-network; synthetic-only; placeholder-hold; non-release; non-publication
responsibility: Record the empty AHGP connector-test lane, route future assertions and fixtures, and prevent documentation or generic CI from being mistaken for source-specific test evidence.
base_commit: 64e875bd2f98502adca9d73e5bb70ff2983b18cd
prior_blob: c64905e3740fa6bf6e0afb5a52ffca0fa2a4b5db
truth_posture: CONFIRMED README-only directory with no executable AHGP tests, fixtures, configuration, discovery index, or source-specific workflow binding / CONFIRMED connector package version 0.0.0 with empty or comment-only Python modules and unresolved role and rights metadata / CONFIRMED generic connector checks do not exercise AHGP / HOLD local-versus-root test placement, implementation contract, fixtures, consumers, ownership, and activation
[/KFM_META_BLOCK_V2] -->

# AHGP connector test boundary

> [!IMPORTANT]
> `connectors/ahgp/tests/` contains documentation only. It does not establish
> an executable test suite, test result, AHGP endpoint, approved fixture,
> source admission, activation decision, release gate, or publication approval.

## Purpose

This directory records the expected boundary for tests of the American History
and Genealogy Project (AHGP) connector. It replaces a two-line Greenfield stub
without adding test code or deciding whether future AHGP tests should remain
adjacent to the connector or move under root `tests/`.

Use this page to:

- understand what is and is not currently tested;
- route proposed assertions by their primary responsibility;
- keep future tests no-network and fixtures synthetic or irreversibly
  generalized;
- distinguish generic connector checks from AHGP-specific evidence; and
- identify the evidence required before the lane can be called executable.

## Current repository evidence

At `main@64e875bd2f98502adca9d73e5bb70ff2983b18cd`:

| Surface | Observed state | Safe conclusion |
|---|---|---|
| This directory | `README.md` only | No executable AHGP test module, fixture, marker, configuration, manifest, or result is present. |
| [Connector project](../pyproject.toml) | `kfm-connector-ahgp` version `0.0.0`; no build backend, dependencies, or package discovery | The project remains a packaging placeholder. |
| [Package initializer](../src/ahgp/__init__.py) | Empty | No package export or import-time behavior is implemented there. |
| [Admission module](../src/ahgp/admit.py) | Comment only | No admission function or finite outcome is implemented. |
| [Fetch module](../src/ahgp/fetch.py) | Comment only | No endpoint, transport, retry, cadence, or retrieval behavior is implemented. |
| [Local descriptor](../src/ahgp/descriptor.yaml) | `role: TBD`, `rights: TBD` | It is not an admitted SourceDescriptor or activation decision. |
| [Connector gate](../../../.github/workflows/connector-gate.yml) | Runs shared connector-core tests, generic non-publisher checks, and IngestReceipt validator prerequisites | It does not import, instantiate, fetch from, or admit through the AHGP package. |

The absence of implementation means there is no AHGP runtime behavior for this
directory to validate. A README, directory, workflow name, or passing generic
check must not be counted as AHGP-specific coverage.

## Placement and routing

Accepted Directory Rules place reusable executable conformance under root
[`tests/`](../../../tests/README.md) and reusable inputs under root
[`fixtures/`](../../../fixtures/README.md). Root test guidance permits
owner-local tests only when adjacency is intentional and root orchestration
indexes them.

That condition is not established here. Until placement is reviewed, route work
as follows:

| Proposed assertion or input | Preferred starting point |
|---|---|
| AHGP fetch/admission behavior tied to an implemented adapter | A reviewed `tests/connectors/ahgp/` lane, or this local lane only after explicit indexing and placement approval |
| Generic connector output confinement | [`tests/policy/test_pipeline_connector_non_publisher.py`](../../../tests/policy/test_pipeline_connector_non_publisher.py) |
| Source identity, role, rights, cadence, citation, or activation | Root `tests/source/` or another accepted source-governance suite |
| Contract or schema shape and polarity | The owning contract/schema validator and its root test lane |
| Reusable valid, invalid, deny, abstain, or golden inputs | Root [`fixtures/`](../../../fixtures/README.md) under an accepted family |
| Real captured source bytes | Governed RAW or QUARANTINE storage, never a repository fixture by default |

Do not create both a local and root AHGP suite as parallel writable authorities.
A reviewed placement decision must identify one collection path, one fixture
route, consumers, workflow discovery, compatibility behavior, and rollback.

## Required test contract

Before an AHGP connector can be called implemented or test-covered, its suite
must exercise the actual code and include deterministic positive, negative,
boundary, and regression cases for:

1. side-effect-free imports: no network, credential access, filesystem writes,
   registry mutation, or lifecycle mutation;
2. explicit configuration and bounded locators, redirects, timeouts, retries,
   response sizes, and cancellation;
3. fail-closed behavior for missing or unresolved source identity, role, rights,
   sensitivity, access, cadence, and activation state;
4. exact captured-byte identity, content digest, retrieval metadata, and
   source-head behavior;
5. finite outcomes for success, not modified, timeout, rate limit, malformed
   content, unsupported content type, partial response, and upstream drift;
6. RAW or QUARANTINE handoff only, plus receipt-ready metadata through a
   caller-owned governed sink;
7. denial of direct WORK, PROCESSED, CATALOG, TRIPLET, PROOF, PUBLISHED,
   release, public API/UI, map, export, or AI writes;
8. replay, correction, supersession, and interruption behavior; and
9. stable test discovery in the declared local command and CI workflow.

Tests must not contact AHGP or any other live source in pull-request CI. Network
behavior should use an injected transport or an equivalent deterministic fake.

## Fixture safety

Genealogy material may expose living people, family relationships, residences,
burials, cemeteries, obituaries, exact locations, private land context, and
culturally sensitive information. Repository fixtures must therefore be
synthetic, minimized, public-safe, or irreversibly generalized.

Do not copy live AHGP pages, volunteer family trees, credentials, cookies,
contact details, restricted records, or real sensitive source bytes into this
directory. Fixture prose and expected outcomes are test carriers, not people,
genealogy, place, rights, policy, evidence, or publication authority.

## Current validation

From the repository root, reviewers can inspect the present boundary with:

```bash
git ls-tree -r --name-only HEAD -- connectors/ahgp/tests

find connectors/ahgp/tests -type f \
  ! -name 'README.md' \
  -print

python -m compileall -q connectors/ahgp/src/ahgp
PYTHONPATH=connectors/ahgp/src \
  python -c "import ahgp; import ahgp.admit; import ahgp.fetch"

python -m pytest \
  tests/policy/test_pipeline_connector_non_publisher.py \
  -q --strict-config --strict-markers
```

For the current documentation-only posture, the `find` command must print
nothing. The compile and import commands establish only syntax and import
safety for the current empty or comment-only modules. The policy test is a
bounded static non-publisher check; it does not prove AHGP behavior,
source-specific output routing, rights clearance, or runtime confinement.

### Failure interpretation

| Observation | Required response |
|---|---|
| A file appears besides this README | Stop and verify placement, discovery, fixture safety, implementation binding, and workflow coverage. |
| Import performs I/O or requires credentials | Treat as a boundary violation; do not add exceptions that normalize import-time effects. |
| A fixture contains real or sensitive material | Remove it from the proposed change and route the material through governed data handling. |
| A test passes without importing or invoking AHGP code | Classify it as generic or vacuous, not AHGP connector evidence. |
| A test expects publication or release as a connector effect | Reject the expectation; connectors are non-publishers. |
| A live-network test is proposed for pull-request CI | Replace it with deterministic injected transport or hold the test pending an accepted isolated profile. |

## Admission gate for executable tests

Before adding any executable file here or at a replacement path, establish:

- accepted local-versus-root placement and a single collection route;
- an implemented AHGP behavior and explicit contract to exercise;
- source-safe fixture identities, expected polarity, provenance, retention, and
  correction posture;
- deterministic no-network execution and pinned test dependencies;
- non-vacuous negative cases and failure assertions;
- a discoverable local command and exact workflow binding;
- verified consumers and no duplicate suite;
- accountable connector, source, genealogy, rights, sensitivity, test, and
  independent reviewers; and
- migration and rollback steps if this placeholder path is retired.

A merge, green workflow, generated report, or test count does not satisfy source
admission, review, release, deployment, promotion, or publication requirements.

## Correction and rollback

This document changes no connector behavior. Before merge, close the draft pull
request and abandon its branch to roll back. After merge, use a focused
corrective pull request or revert the documentation commit.

Do not restore the Greenfield stub as a shortcut and do not add dummy tests to
make the lane appear implemented. Any later executable rollback must disable
the relevant caller or adapter while preserving captured bytes, receipts,
review history, and correction lineage in their governed homes.

## Open verification register

| ID | Question | Status |
|---|---|---|
| AHGP-TEST-001 | Should AHGP tests live here or under root `tests/connectors/ahgp/`? | **HOLD / NEEDS DIRECTORY REVIEW** |
| AHGP-TEST-002 | Which implemented AHGP behaviors and interfaces should the first suite bind? | **NOT IMPLEMENTED** |
| AHGP-TEST-003 | Which synthetic fixture profile and expected outcomes are acceptable? | **NEEDS VERIFICATION** |
| AHGP-TEST-004 | Which workflow and local command should collect the suite? | **UNKNOWN** |
| AHGP-TEST-005 | Who owns source, genealogy, rights, sensitivity, test, and independent review? | **NEEDS VERIFICATION** |

## Related surfaces

- [AHGP connector boundary](../README.md)
- [AHGP source-tree inventory](../src/README.md)
- [AHGP package boundary](../src/ahgp/README.md)
- [AHGP source-family catalog](../../../docs/sources/catalog/ahgp.md)
- [Root test contract](../../../tests/README.md)
- [Root fixture contract](../../../fixtures/README.md)
- [Connector gate workflow](../../../.github/workflows/connector-gate.yml)
- [Accepted Directory Rules](../../../docs/doctrine/directory-rules.md)

## Changelog

| Version | Date | Change |
|---|---|---|
| v1.0.0 | 2026-08-29 | Replaces the two-line Greenfield stub with a repository-grounded test-routing and safety boundary; no test or connector behavior is added. |

