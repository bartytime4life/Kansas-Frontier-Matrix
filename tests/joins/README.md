<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://tests/joins/readme
title: Join Assessment Test Lane
type: test-lane-readme
version: v0.3.0
status: draft; repository-grounded; synthetic-only; no-network; nine-executable-modules-confirmed
owners: @bartytime4life — CONFIRMED CODEOWNERS review route; accountable join, validation, sensitivity, and historical-context stewardship UNKNOWN
created: 2026-08-09
updated: 2026-09-01
policy_label: repository-facing; tests; joins; non-publisher
owning_root: tests/
responsibility: Document the bounded synthetic proof surface for generic cross-lane and historical-network proximity assessment helpers.
truth_posture: cite-or-abstain
evidence_base: 9da74db4465a59336fba4cbe1658b85ebeba34c9
prior_blob: d5f5b8508b7aae0a1ebe94238d3c9bd5c45d56d1
[/KFM_META_BLOCK_V2] -->

# Join assessment test lane

`tests/joins/` contains nine executable modules: one generic
CrossLaneJoinAssessment suite, six focused generic boundary guards, one workflow
propagation guard, and one historical-network proximity suite. Every case uses
repository fixtures or synthetic mutations.

Passing this lane shows only deterministic agreement among the covered helpers,
contracts, schemas, fixtures, workflows, and receipts. It does not establish a
real-world relationship, identify a person, admit a source, clear rights or
sensitivity, approve review, release an artifact, or publish a join.

## Executable inventory

| Test module | Bounded proof |
| --- | --- |
| [`test_join_candidates.py`](test_join_candidates.py) | Generic fixture derivation, validation, tamper resistance, non-network behavior, and non-publisher effects. |
| [`test_cross_lane_scope_precedence.py`](test_cross_lane_scope_precedence.py) | Same-domain requests route to their domain validator before cross-lane dependency disposition. |
| [`test_cross_lane_source_role_schema_guard.py`](test_cross_lane_source_role_schema_guard.py) | Endpoint and copied decision source roles share one closed schema vocabulary. |
| [`test_cross_lane_synthetic_role_guard.py`](test_cross_lane_synthetic_role_guard.py) | Equal roles may remain candidates; unequal or synthetic/non-synthetic roles require review. |
| [`test_cross_lane_temporal_boundary_guard.py`](test_cross_lane_temporal_boundary_guard.py) | Genuine overlap remains eligible while zero-tolerance boundary contact abstains. |
| [`test_cross_lane_domain_alias_guard.py`](test_cross_lane_domain_alias_guard.py) | Unresolved alias/canonical pairs abstain in both orientations without normalization. |
| [`test_cross_lane_domain_alias_dependency_guard.py`](test_cross_lane_domain_alias_dependency_guard.py) | Missing or malformed alias projection fails closed instead of becoming an empty alias set. |
| [`test_cross_lane_workflow_propagation.py`](test_cross_lane_workflow_propagation.py) | Four hosted workflows retain pull-request and main replay, dependency path filters, guard collection, and this inventory. |
| [`test_historical_network_proximity.py`](test_historical_network_proximity.py) | Bounded historical-network proximity remains synthetic, deterministic, and non-authoritative. |

The inventory is a repository observation, not a required-check claim. The
workflow propagation guard compares the documented `test_cross_lane_*.py`
names with the actual directory so a newly added boundary module cannot remain
silently undocumented.

## Generic CrossLaneJoinAssessment coverage

The generic suite and its focused guards jointly cover:

- parameterized, in-memory exact-key candidate evaluation;
- bounded synthetic spatial-temporal comparison;
- same-domain routing before cross-lane disposition;
- missing EvidenceRefs and dependency failures;
- closed source-role schema projection and unequal-role abstention;
- restricted exact geometry and living-person denial;
- zero-tolerance temporal boundary ambiguity;
- unresolved domain aliases and fail-closed alias-register loss;
- schema, decision, identity, duplicate-key, and interval tampering;
- denied symlinked fixture inputs and absence of known network/file-write tokens;
- workflow triggers for the alias register, generic fixtures, helper, contract,
  schema, and all join tests; and
- false lifecycle, evidence, policy, review, release, publication, and public-use
  effects for every candidate outcome.

The finite helper outcomes are `ALLOW`, `ABSTAIN`, `DENY`, and
`ERROR`. `ALLOW` authorizes only local candidate-report emission.

## Historical-network proximity coverage

`test_historical_network_proximity.py` keeps candidate, no-overlap,
ambiguous, unsupported, and context-only outcomes distinct. It checks half-open
temporal overlap, bounded uncertainty, source-role and approximation mismatches,
deterministic profile hashing, duplicate-key rejection, non-finite values,
symlink denial, mocked socket denial, and non-authoritative effects.

These checks do not activate the proposed historical-network contract or turn
proximity into evidence of association.

## Run locally

Run the generic lane exactly as the hosted cross-lane workflow:

```bash
python tools/joins/join_candidates.py --fixtures
python -m pytest \
  tests/joins/test_join_candidates.py \
  'tests/joins/test_cross_lane_*.py' \
  -q --strict-config --strict-markers
```

Run the historical-network lane:

```bash
python -m py_compile \
  tools/joins/historical_network_proximity.py \
  tests/joins/test_historical_network_proximity.py
python tests/joins/test_historical_network_proximity.py --verbose
python tools/joins/historical_network_proximity.py --fixtures
```

## Hosted workflow coverage

| Workflow | Generic guard coverage | Trigger lifecycle |
| --- | --- | --- |
| [`cross-lane-join-assessment`](../../.github/workflows/cross-lane-join-assessment.yml) | Fixture runner, generic suite, and every `test_cross_lane_*.py` module | Pull request, main push, manual dispatch |
| [`soil-hydrology-public-safe-context`](../../.github/workflows/soil-hydrology-public-safe-context.yml) | Generic lane plus Soil–Hydrology pair proof | Pull request, main push, manual dispatch |
| [`soil-agriculture-public-safe-context`](../../.github/workflows/soil-agriculture-public-safe-context.yml) | Generic lane plus Soil–Agriculture pair proof | Pull request, main push, manual dispatch |
| [`fauna-habitat-public-safe-assignment`](../../.github/workflows/fauna-habitat-public-safe-assignment.yml) | Generic lane plus Fauna–Habitat pair proof | Pull request, main push, manual dispatch |
| [`historical-network-proximity-assessment`](../../.github/workflows/historical-network-proximity-assessment.yml) | Historical-network proof only | Its own bounded filters and dispatch |

The four generic-consuming workflows use Python 3.11, read-only repository
permissions, `KFM_NO_NETWORK=1`, generic fixture replay, and focused tests.
Their path filters include the unresolved domain-alias register, generic fixture
family, helper, contract, schema, and `tests/joins/**`. A workflow that did
not run is unavailable evidence, never a pass.

The historical workflow remains independently scoped. Its README path-filter
coverage is not implied by the generic workflows.

## Safety and authority boundary

| Evidence from this lane | What it does not establish |
| --- | --- |
| Synthetic fixtures and mutations produce expected finite outcomes | Truth of a real-world link, identity, event, or location |
| Helpers remain deterministic for covered inputs | Complete semantic or production parity |
| Workflow dependencies and test collection remain connected | Required-check status or successful execution on an untested head |
| Network and publisher effects are absent from the checked surface | Runtime confinement outside the tested process |
| Contracts, schemas, fixtures, workflows, and stored receipts agree | Adoption, approval, release, deployment, or publication |
| Covered malformed or unsafe inputs fail closed | Rights clearance, consent, sovereignty, privacy, or harmful-precision resolution |

Evidence outranks generated candidate language. Downstream evidence, provenance,
rights, sensitivity, policy, correction, review, and release controls remain
required before a candidate can affect a governed artifact.

## Interpreting failures

1. Treat a fixture-runner failure as contract, schema, fixture, or helper drift.
2. Treat a focused guard failure as a regression in its named invariant.
3. Treat an unexpected `ALLOW` or `PASS` as safety-significant and
   verify evidence, roles, sensitivity, identity, temporal, and dependency inputs.
4. Treat missing workflow execution as unavailable evidence, not success.
5. Preserve synthetic values; do not substitute real people, precise locations,
   or restricted material.

## Maintenance and rollback

When this lane changes:

- keep module, helper, contract, schema, fixture, workflow, and receipt references
  synchronized;
- add deterministic positive and negative cases for every new branch;
- keep all generic-consuming workflows aligned on dependencies and collection;
- preserve finite outcomes, non-publisher effects, and fail-closed behavior; and
- update claims only from exact repository evidence.

This document changes no runtime relationship or publication authority. Before
merge, rollback is closing the pull request or forward-reverting the bounded
documentation/test/receipt commits.
