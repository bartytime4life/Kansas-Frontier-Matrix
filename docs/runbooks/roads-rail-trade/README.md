<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks-roads-rail-trade-readme
title: docs/runbooks/roads-rail-trade/ — Roads, Rail, and Trade Operational Procedure Boundary
type: readme
subtype: boundary-compact
version: v1.0
prior_state: no local README path
status: draft; repository-grounded; bounded synthetic CorridorRoute validation executable; broader source operation, policy, proof, promotion, rollback, release, deployment, and publication held
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Roads/Rail/Trade, transport, evidence, policy, safety, source, and release assignments"
created: 2026-08-28
updated: 2026-08-28
policy_label: repository-facing; infrastructure-sensitive; historic and cultural corridor precision-sensitive; fail-closed
current_path: docs/runbooks/roads-rail-trade/README.md
owning_root: docs/
responsibility: human procedure index and operational boundary for the Roads/Rail/Trade lane
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, source records, policy, evidence, lifecycle, review, release, correction, rollback, and official authorities
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 2de55d48ab35a41875eb9f094dc55dda18618ecc
  parent_runbooks_readme_blob: 26f9e77d329d58fb140fd4cfe814b4590e62952c
  domain_readme_blob: f2d1250dad3eefd2f148483ddcc388e66d2a2186
  workflow_blob: 391fead3fdd0d7ecead6464be7946cbaf68247e0
  no_network_runbook_blob: 96445de559fd98fedde6924f047625f611a0b596
  promotion_runbook_blob: 315eb67a2c6cadac812f66e4e81f0a42f7f0c40d
  rollback_runbook_blob: a097a2aa95bda465227a4103aa5da7416a72622d
  source_refresh_runbook_blob: 2b403f3a6ca9bad993a30a0c8c609e712f3e4029
  corridor_route_contract_blob: 2bef2e964b8afa855ca7e72c86ca72dad2b63f52
  corridor_route_schema_blob: 663afd8aa09c52a2626d84cfbc6c76965df79942
  corridor_route_validator_blob: 9b75fd5d15d348ec788057fa1e1371f82e685415
  corridor_route_tests_blob: 4df9495c441810e5ad196d88ad67f64e00426136
  domain_smoke_test_blob: 967f997329a7308cd5267df96d258de8092224c7
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  direct_markdown_files_before_this_readme: 4
  bounded_executable_profiles: 1
  proposal_or_stale_child_procedures: 4
related:
  - ../README.md
  - ../../domains/roads-rail-trade/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/domain-roads-rail-trade.yml
  - ../../../contracts/domains/roads-rail-trade/corridor_route.md
  - ../../../schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json
  - ../../../tools/validators/domains/roads-rail-trade/validate_corridor_route.py
  - ../../../tests/schemas/test_corridor_route_contract.py
  - ../../../fixtures/domains/roads-rail-trade/corridor_route/
  - ../../../policy/domains/roads-rail-trade/README.md
  - ../../../data/registry/sources/roads-rail-trade/README.md
  - ../../../data/proofs/roads-rail-trade/README.md
  - ../../../release/candidates/roads-rail-trade/README.md
notes:
  - "v1.0 closes the missing local boundary without changing any child procedure or authority surface."
  - "The CorridorRoute contract, schema, validator, synthetic fixtures, and focused tests form one executable no-network profile with PASS, ABSTAIN, DENY, and ERROR outcomes."
  - "The four child runbooks retain proposal-era paths, commands, roles, or no-mounted-repository claims and are not current operational authority."
  - "The domain smoke test remains an assert-true placeholder; the fixture README remains a greenfield stub; broader validation and proof production remain held."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Roads, Rail, and Trade Operational Procedure Boundary

This directory routes maintainers to Roads/Rail/Trade procedures while keeping
one implemented synthetic validation profile separate from proposal-era source,
promotion, and rollback instructions. It is an index and boundary contract, not
a route, network, source, policy, evidence, proof, release, or publication
authority.

> [!WARNING]
> KFM is not a navigation, dispatch, traffic-control, railroad-operating,
> bridge-safety, emergency-routing, legal-access, right-of-way, regulatory, or
> current-closure authority. A repository check cannot establish that any road,
> rail line, bridge, crossing, ferry, facility, route, or corridor is open,
> lawful, current, complete, or safe.

> [!IMPORTANT]
> Current executable evidence is limited to a no-network, synthetic
> `CorridorRoute` profile. It checks deterministic shape and selected
> anti-collapse boundaries; it does not establish real route identity,
> alignment, membership, operator, restriction, access, condition, source
> admission, policy approval, proof, release readiness, or public behavior.

**Start here:** [bounded CorridorRoute validation](#bounded-validation) ·
[child-procedure maturity](#child-procedure-maturity) ·
[parent runbook index](../README.md) ·
[domain boundary](../../domains/roads-rail-trade/README.md)

## Purpose and inherited authority

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md), which place
human operational procedures below `docs/runbooks/` and require boundaries to
inherit authority rather than manufacture it.

This README therefore:

- identifies the implemented and held portions of this lane;
- routes readers to the exact repository-backed validation commands;
- preserves source-role, route/segment/membership, time, sensitivity, and
  cross-domain boundaries;
- records stop conditions for operational or public claims; and
- keeps procedure documentation distinct from review, release, deployment,
  promotion, and publication.

It does not resolve the repository's `roads-rail-trade` versus `transport` path
split. That remains an ADR- and migration-dependent question.

## Current maturity

| Surface | Repository evidence | Bounded conclusion |
|---|---|---|
| `CorridorRoute` semantic contract | Draft contract paired with a bounded schema profile | Meaning and selected invariants are documented; source, policy, review, release, and runtime admission remain open |
| Schema and validator | Draft 2020-12 schema plus executable no-network validator | Can return `PASS`, `ABSTAIN`, `DENY`, or `ERROR` for the bounded profile |
| Synthetic fixtures | Two valid fixtures and eight invalid fixtures | Cover one passing candidate, one unresolved-support abstention, and eight denial cases; they are not route evidence |
| Focused test module | Fourteen tests in `tests/schemas/test_corridor_route_contract.py` | Exercises pairing, required fields, anti-collapse rules, deterministic hashing, synthetic/no-network posture, and CLI outcomes |
| Domain workflow | Executes the focused test module and validator fixture runner | Demonstrates orchestration and bounded checks at the tested SHA only |
| Domain smoke test | `assert True` placeholder | Does not establish a substantive domain test suite |
| Fixture README | Two-line greenfield stub | Does not document the implemented `corridor_route/` fixture family |
| Broader validators | Several related validator roots remain documentation-only | Crossing, facility, bridge, public-safety, source-role, catalog, and proof closure are not established as a complete lane |
| Policy | Domain README remains proposal-oriented | No active policy runtime or release decision is established by this lane |
| Proof and release | Proof lane reports no accepted end-to-end producer; candidate lane remains pre-publication guidance | No proof closure, approved manifest, release, or publication is established |

## Bounded validation

Run from the repository root at the exact revision being reviewed:

```bash
python -m pytest -q tests/schemas/test_corridor_route_contract.py
python tools/validators/domains/roads-rail-trade/validate_corridor_route.py --fixtures
```

The active domain workflow runs both commands after dependency installation.
The validator treats file arguments differently from the fixture suite: file
mode exits successfully for `PASS` or `ABSTAIN`, while `DENY` or `ERROR` exits
non-zero. The `--fixtures` mode succeeds only when every tracked fixture returns
its declared expected outcome.

### What the profile checks

- JSON Schema pairing and Draft 2020-12 declaration;
- required source-packet and temporal fields;
- route identity kept separate from segments, segment membership, and embedded
  geometry;
- explicit denial of live-routing, legal-designation, and publication-authority
  fields;
- deterministic `spec_hash` calculation over canonical content;
- valid-time ordering;
- selected public-geometry, rights, and sensitivity boundaries;
- unresolved source, evidence, geometry, or rights support producing
  `ABSTAIN` unless a released posture makes the conflict a denial; and
- synthetic, no-network fixture metadata.

### What the profile does not check

It does not prove:

- a real road, rail line, historic route, trade corridor, crossing, bridge,
  ferry, depot, yard, restriction, or operator assertion;
- source identity, currentness, admission, terms, rights, cadence, or authority;
- route membership, full geometry lineage, live status, legal access, safe
  passage, bridge condition, or railroad operating status;
- active policy evaluation, accountable review, EvidenceBundle closure,
  catalog closure, proof production, or rollback execution; or
- governed API, map, graph, export, Focus Mode, deployment, release, promotion,
  or publication behavior.

## Child-procedure maturity

| Procedure | Current classification | Safe use |
|---|---|---|
| [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | Proposal-era procedure; not the canonical description of the implemented CorridorRoute profile | Use the commands above and current workflow as executable evidence; treat unmatched commands and paths as illustrative until verified |
| [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Proposal-heavy promotion design | Review concepts only; do not execute a lifecycle transition or infer promotion authority |
| [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Proposal-heavy operational rollback design with unverified release infrastructure | Review defect classes and boundaries only; no operational rollback capability is established |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | Stale May 2026 source-refresh draft that states the repository was not mounted | Lineage only; do not use its proposed paths, roles, source endpoints, commands, or lifecycle actions as current implementation |

No child runbook may be upgraded from proposal to executable merely because a
related workflow or validator exists. Reconcile its complete command, input,
output, failure, authority, and rollback contract against current repository
evidence first.

## Inputs, outputs, and failure cases

### Permitted bounded inputs

- tracked synthetic JSON fixtures below
  `fixtures/domains/roads-rail-trade/corridor_route/`;
- the paired contract and schema at their exact reviewed revisions;
- the exact validator and test module at the reviewed SHA; and
- local repository files required by the read-only pull-request workflow.

### Bounded outputs

- console outcomes from the validator;
- pytest results for the focused module; and
- GitHub workflow status and step summary tied to an exact commit.

These outputs are validation observations, not EvidenceBundles,
PolicyDecisions, ReviewRecords, proofs, PromotionDecisions, ReleaseManifests,
RollbackCards, or published artifacts.

### Failure interpretation

| Observation | Interpretation | Required response |
|---|---|---|
| `PASS` | The bounded synthetic profile satisfied the implemented checks | Record the exact SHA and limitations; do not generalize to real routes or release readiness |
| `ABSTAIN` | Support remains unresolved but no released posture was claimed | Preserve unresolved fields and stop any stronger claim |
| `DENY` | Shape, hash, time, rights, sensitivity, public geometry, or released-support rule failed | Do not advance the candidate; correct the input or boundary |
| `ERROR` | The validator could not load or evaluate valid inputs | Treat as invalid execution; repair tooling or environment before relying on results |
| Domain smoke test passes | The placeholder asserted `True` | Do not report substantive domain coverage |
| Workflow is green | Named checks completed at one SHA | Do not infer review, source admission, policy approval, proof, release, deployment, or publication |

## Safety, rights, and cross-domain boundaries

Roads/Rail/Trade material can expose sensitive infrastructure, private-property
context, culturally significant movement corridors, Indigenous or Tribal
knowledge, historic-route uncertainty, and harmful precision. Apply the most
restrictive supported exposure and stop when rights, sovereignty, consent,
sensitivity, source role, time, freshness, geometry lineage, uncertainty, or
correction status is unresolved.

Keep these concerns separate:

- routes are not segments, route membership assertions, or graph edges;
- an alignment is not proof of operator, designation, access, or current status;
- crossing records do not absorb Hydrology, Infrastructure, Hazards, legal, or
  safety authority;
- reconstructed and narrative corridors are not surveyed alignments;
- generalized public geometry does not replace restricted canonical geometry;
  and
- maps, indexes, tests, workflows, and generated text are not sovereign truth.

Do not place credentials, temporary source URLs, restricted payloads, precise
sensitive coordinates, private facility detail, or unreviewed source excerpts
in runbooks, pull requests, logs, or fixture output.

## Stop conditions

Stop and return `HOLD`, `ABSTAIN`, `DENY`, `ERROR`, or `ESCALATE` as supported
when any required item is unresolved:

- exact revision, command, schema/contract pairing, fixture set, or expected
  negative outcome;
- source identity, source role, rights, license, cadence, currentness, or
  retrieval context;
- route, segment, membership, crossing, facility, operator, restriction,
  temporal, or geometry identity;
- evidence, policy, sensitivity, cultural/sovereignty review, or accountable
  reviewer authority;
- proof, manifest, release decision, correction path, invalidation plan, or
  rollback target; or
- public-safe interface, release, deployment, promotion, or publication state.

Never weaken a schema, validator, negative fixture, no-network guard, policy
hold, or topology ratchet to obtain a passing result.

## Maintenance

When this lane changes:

1. Verify commands and paths against the current workflow and repository bytes.
2. Update this maturity table when a child procedure, fixture index, smoke test,
   validator family, policy runtime, proof producer, or release control changes.
3. Keep proposal-era runbooks labeled until their complete procedure contracts
   are reconciled.
4. Preserve route/segment/membership, source-role, temporal, sensitivity,
   cross-domain, correction, and rollback separation.
5. Keep semantic, schema, policy, source, evidence, proof, lifecycle, release,
   and executable changes in their owning roots.

GitHub review routes through [CODEOWNERS](../../../.github/CODEOWNERS) to
`@bartytime4life`. That route does not establish domain expertise, independent
review, policy approval, source admission, release, deployment, promotion, or
publication.

## Related responsibility roots

- [Roads/Rail/Trade domain boundary](../../domains/roads-rail-trade/README.md)
- [`CorridorRoute` semantic contract](../../../contracts/domains/roads-rail-trade/corridor_route.md)
- [`CorridorRoute` schema](../../../schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json)
- [CorridorRoute validator](../../../tools/validators/domains/roads-rail-trade/validate_corridor_route.py)
- [Focused CorridorRoute tests](../../../tests/schemas/test_corridor_route_contract.py)
- [Domain workflow](../../../.github/workflows/domain-roads-rail-trade.yml)
- [Domain policy boundary](../../../policy/domains/roads-rail-trade/README.md)
- [Source-registry boundary](../../../data/registry/sources/roads-rail-trade/README.md)
- [Proof boundary](../../../data/proofs/roads-rail-trade/README.md)
- [Release-candidate boundary](../../../release/candidates/roads-rail-trade/README.md)

## Documentation rollback

Before merge, close the draft pull request and discard only its feature branch.
After merge, revert the documentation commit or submit a reviewed forward
correction. Either action changes documentation only; it does not undo source
admission, evidence, policy, lifecycle, release, deployment, promotion, or
publication state.

[Back to top](#top)
