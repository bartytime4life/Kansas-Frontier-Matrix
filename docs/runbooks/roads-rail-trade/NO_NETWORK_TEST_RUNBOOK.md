<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/roads-rail-trade/no-network-test
title: Roads, Rail, and Trade Routes — No-Network Test Runbook
type: runbook
version: v1.0.0
prior_version: v0.1
prior_state: proposal-era trust-spine design with unverified paths, commands, outcomes, receipt production, release dry run, and rollback drill
status: DRAFT_REPOSITORY_GROUNDED; BOUNDED_SYNTHETIC_CORRIDOR_ROUTE_PROFILE_EXECUTABLE; GUARDED_LOCAL_COMMAND_AVAILABLE; WORKFLOW_GUARD_INJECTION_HELD; BROADER_DOMAIN_PROOF_RELEASE_AND_PUBLICATION_HELD; NOT_FOR_OPERATIONAL_USE
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Roads/Rail/Trade, transport, source, evidence, policy, safety, and release assignments"
created: 2026-05-12
updated: 2026-08-29
policy_label: repository-facing; infrastructure-sensitive; historic and cultural corridor precision-sensitive; fail-closed; synthetic-only
current_path: docs/runbooks/roads-rail-trade/NO_NETWORK_TEST_RUNBOOK.md
owning_root: docs/
responsibility: bounded human procedure for deterministic no-network validation of the implemented synthetic CorridorRoute profile
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, source records, policy, evidence, review, lifecycle, proof, release, correction, and rollback authorities
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  target_prior_blob: 96445de559fd98fedde6924f047625f611a0b596
  lane_readme_blob: 5de90772b7ae420f42ed2794e7f545e55035aaa9
  workflow_blob: 391fead3fdd0d7ecead6464be7946cbaf68247e0
  corridor_route_contract_blob: 2bef2e964b8afa855ca7e72c86ca72dad2b63f52
  corridor_route_schema_blob: 663afd8aa09c52a2626d84cfbc6c76965df79942
  corridor_route_validator_blob: 9b75fd5d15d348ec788057fa1e1371f82e685415
  corridor_route_tests_blob: 4df9495c441810e5ad196d88ad67f64e00426136
  shared_python_guard_readme_blob: d0e89356c9a9175f2c9798daa1923d73a9034eca
  bounded_test_count: 14
  valid_fixture_count: 2
  invalid_fixture_count: 8
related:
  - ./README.md
  - ../../domains/roads-rail-trade/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/domain-roads-rail-trade.yml
  - ../../../contracts/domains/roads-rail-trade/corridor_route.md
  - ../../../schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json
  - ../../../fixtures/domains/roads-rail-trade/corridor_route/
  - ../../../tools/validators/domains/roads-rail-trade/validate_corridor_route.py
  - ../../../tests/schemas/test_corridor_route_contract.py
  - ../../../tools/ci/kfm_no_network/README.md
notes:
  - "v1.0.0 replaces proposal-era commands with the exact bounded CorridorRoute commands on current main."
  - "The implemented validator uses PASS, ABSTAIN, DENY, and ERROR; it does not implement an ANSWER outcome or an end-to-end runtime decision envelope."
  - "The shared Python startup guard is available for local guarded execution, but the current Roads/Rail/Trade workflow does not inject its directory into PYTHONPATH."
  - "No receipt, proof, promotion, release, rollback-execution, deployment, or publication producer is established by this procedure."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Roads, Rail, and Trade Routes — No-Network Test Runbook

Use this runbook to execute and interpret the repository's bounded, synthetic
`CorridorRoute` schema and validator profile without live source retrieval or
intentional network access. The procedure is deterministic, read-only, and
limited to the exact revision under review.

> [!WARNING]
> KFM is not a navigation, dispatch, traffic-control, railroad-operating,
> bridge-safety, emergency-routing, legal-access, right-of-way, regulatory, or
> current-closure authority. A passing repository test does not establish that
> any road, rail line, bridge, crossing, ferry, facility, route, or corridor is
> open, lawful, current, complete, or safe.

> [!IMPORTANT]
> Current executable scope is one synthetic `CorridorRoute` profile. It does
> not establish real route identity, source admission, EvidenceBundle closure,
> active policy evaluation, human review, proof, release, deployment,
> promotion, rollback execution, or publication.

**Use:** [scope](#scope) · [preconditions](#preconditions) ·
[procedure](#procedure) · [outcomes](#outcomes-and-acceptance) ·
[failure diagnosis](#failure-diagnosis) · [handoff](#review-handoff) ·
[rollback](#documentation-rollback)

## Purpose and authority

This runbook operationalizes the currently implemented no-network validation
slice for Roads/Rail/Trade. It tells a maintainer how to:

- activate the shared Python-process startup guard for the validation window;
- prove that a representative connection path is denied in a fresh process;
- run the focused `CorridorRoute` test module and fixture validator;
- interpret `PASS`, `ABSTAIN`, `DENY`, and `ERROR` without widening them into
  real-world, policy, release, or publication claims; and
- preserve a reviewable failure and rollback boundary.

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md). Those rules
place human operational procedures under `docs/runbooks/`; the executable
contract, schema, fixtures, validator, tests, workflow, and CI helper remain in
their owning responsibility roots.

This document explains those authorities. It does not replace or amend them.

## Current implementation boundary

| Surface | Current repository evidence | Bounded conclusion | Not established |
|---|---|---|---|
| Semantic contract | `contracts/domains/roads-rail-trade/corridor_route.md` | Draft `CorridorRoute` meaning and anti-collapse boundaries are documented | Accepted domain-wide transport semantics or real-route truth |
| Schema | `schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json` | Draft 2020-12 profile is paired to the contract | Complete Roads/Rail/Trade object-family coverage |
| Fixtures | Two valid and eight invalid JSON fixtures below `fixtures/domains/roads-rail-trade/corridor_route/` | Synthetic `PASS`, `ABSTAIN`, and `DENY` polarity is executable | Real source, geometry, rights, evidence, or policy validity |
| Validator | `validate_corridor_route.py` | Deterministic schema, hash, time, support, rights, sensitivity, and public-geometry checks | Evidence resolution, policy-engine execution, review, proof, or release decision |
| Focused tests | Fourteen tests in `tests/schemas/test_corridor_route_contract.py` | Pairing, required fields, anti-collapse, hash, fixture posture, and CLI behavior are checked | A substantive full-domain suite; the domain smoke test remains a placeholder |
| Shared guard | `tools/ci/kfm_no_network/sitecustomize.py` and its README | Opt-in startup denial for named Python IPv4/IPv6 connection, send, resolver, and URL-open paths | Operating-system, runner-wide, container, namespace, dependency-install, non-Python, or arbitrary private-API isolation |
| Domain workflow | `.github/workflows/domain-roads-rail-trade.yml` | Runs the focused tests and fixture validator with synthetic local inputs | Shared startup-guard injection; broader semantic, proof, release, or publication readiness |

### Guard wiring gap

The domain workflow currently sets `KFM_NO_NETWORK=1`, but the shared guard
loads only when `tools/ci/kfm_no_network` is also present on `PYTHONPATH` before
Python starts. Therefore:

- the workflow's current `KFM_NO_NETWORK` environment value is not, by itself,
  proof that the shared startup guard was active;
- the fixture-only code path is still bounded to local repository inputs; and
- this runbook's local procedure injects the guard explicitly, while
  workflow-wide startup enforcement remains `NEEDS VERIFICATION` until the
  workflow is deliberately updated and proven.

Do not describe the current workflow as runner-wide or process-wide no-egress
enforcement.

## Scope

### Included

- the exact contract, schema, validator, fixtures, and focused test module named
  in this runbook;
- local, synthetic, non-sensitive fixture inputs only;
- explicit shared-guard activation for each Python process in the command
  window;
- a representative fresh-process denial probe;
- deterministic expected-outcome comparison for all tracked fixtures; and
- worktree-write checks after the procedure.

### Excluded

- dependency installation from the guarded window;
- live KDOT, FHWA, FRA, WZDx, OSM, GNIS, KanDrive, KanPlan, railroad,
  municipal, Tribal, archival, or other source requests;
- real route, rail, crossing, bridge, facility, restriction, closure, operator,
  access, or safe-passage determinations;
- source admission, rights verification, EvidenceRef resolution,
  EvidenceBundle construction, active policy evaluation, or accountable review;
- graph, map, API, tile, export, Focus Mode, model-provider, or browser behavior;
- writes to RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, PUBLISHED,
  receipt, proof, candidate, release, correction, or rollback stores; and
- release, deployment, promotion, publication, source activation, or rollback
  execution.

## Preconditions

Run from a clean, dedicated checkout or worktree at the exact revision being
reviewed.

1. Record repository identity and revision:

   ```bash
   git remote get-url origin
   git rev-parse HEAD
   git status --short
   ```

2. Confirm these paths exist:

   ```text
   contracts/domains/roads-rail-trade/corridor_route.md
   schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json
   fixtures/domains/roads-rail-trade/corridor_route/
   tools/validators/domains/roads-rail-trade/validate_corridor_route.py
   tests/schemas/test_corridor_route_contract.py
   tools/ci/kfm_no_network/sitecustomize.py
   ```

3. Use Python 3.11, matching the current domain workflow.
4. Confirm the checkout contains no real, restricted, credentialed, or
   operational transport material.
5. Confirm no lifecycle, source, proof, candidate, release, or published write
   is intended.
6. Record any pre-existing worktree change. Prefer a clean worktree; do not
   attribute an inherited change to this procedure.

### Dependency bootstrap boundary

The current workflow installs the declared `project-test` profile with:

```bash
python tools/ci/install_python_ci.py project-test
```

Run bootstrap before the guarded validation window. Dependency installation is
not covered by the shared startup guard and must not be reported as an offline
or runner-isolated operation. In CI, treat the install step as a separate
network and supply-chain boundary.

## Procedure

### 1. Enter the guarded Python window

From the repository root:

```bash
export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
export PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD${PYTHONPATH:+:$PYTHONPATH}"

python -c 'import sitecustomize; assert sitecustomize.GUARD_ACTIVE'
```

Expected result: exit code `0`. Any import error, false `GUARD_ACTIVE`, or
unexpected output is `ERROR`; stop before running the profile.

### 2. Run a representative fresh-process denial probe

```bash
python - <<'PY'
import socket
import sitecustomize

assert sitecustomize.GUARD_ACTIVE
try:
    socket.create_connection(("192.0.2.1", 9), timeout=0.1)
except sitecustomize.NetworkAccessDenied as exc:
    print(f"PASS shared Python guard denied representative connection: {exc}")
else:
    raise SystemExit("ERROR shared Python guard allowed representative connection")
PY
```

Expected result: one `PASS` line and exit code `0`. The TEST-NET-1 address is a
sentinel only; an active guard must deny the call before any connection attempt.

This probe demonstrates the named `socket.create_connection` path at the exact
revision. It does not prove every Python extension, private socket factory,
subprocess, shell command, dependency installer, host process, or runner path.

### 3. Run the focused contract tests

```bash
python -m pytest -q -p no:cacheprovider \
  tests/schemas/test_corridor_route_contract.py
```

Expected result at the evidence snapshot: fourteen tests pass. The module checks
contract/schema pairing, required fields, route-versus-segment separation,
forbidden authority fields, deterministic hashing, valid-time rules, fixture
polarity, synthetic/no-network metadata, and CLI behavior.

A different test count is not automatically a failure, but it is a review
trigger: inspect the exact diff and update this runbook only after the changed
coverage is understood.

### 4. Replay the tracked fixture suite

```bash
python \
  tools/validators/domains/roads-rail-trade/validate_corridor_route.py \
  --fixtures
```

Expected result at the evidence snapshot:

- one synthetic historic candidate returns `PASS`;
- one schema-valid candidate with unresolved evidence returns `ABSTAIN`;
- eight negative fixtures return `DENY`; and
- the command exits `0` only when every fixture matches its declared expected
  outcome.

The batch's successful exit does not mean every fixture passed validation. It
means positive and negative fixtures produced their declared finite outcomes.

### 5. Confirm the procedure wrote no repository content

```bash
git diff --exit-code
git diff --cached --exit-code
test -z "$(git ls-files --others --exclude-standard)"
```

Expected result: all commands exit `0` in the dedicated clean worktree. If the
checkout was already dirty, compare against the recorded baseline and classify
only new changes. Do not delete or overwrite unrelated work to make this check
pass.

## Outcomes and acceptance

### Validator outcomes

| Outcome | Implemented meaning | Command behavior | Permitted conclusion |
|---|---|---|---|
| `PASS` | The candidate satisfied the bounded schema, hash, time, support, rights, sensitivity, and public-geometry checks | File mode exits `0` | This synthetic candidate satisfied the reviewed profile |
| `ABSTAIN` | Required source, evidence, geometry, or rights support is unresolved, or rights/sensitivity keep the candidate non-public | File mode exits `0`; fixture mode requires the declared expectation | Preserve uncertainty and make no stronger claim |
| `DENY` | Shape, hash, time, release-support, rights, sensitivity, or public-geometry rule failed | File mode exits `1`; fixture mode expects denial for negative fixtures | Do not advance the candidate |
| `ERROR` | Input or validator loading/evaluation failed before a valid decision | File mode exits `1` | Repair the execution or input; no trust conclusion is available |

`ANSWER` is not an implemented outcome in this validator. Do not translate
`PASS` into a governed runtime answer.

### Acceptance checklist

Use `READY_FOR_HUMAN_REVIEW` only when all applicable items hold:

- [ ] Exact repository revision and worktree baseline were recorded.
- [ ] Shared guard activation succeeded in the validation process.
- [ ] The representative denial probe succeeded.
- [ ] All focused tests passed without weakening or skipping checks.
- [ ] Every tracked fixture matched its declared outcome.
- [ ] No new repository content was written.
- [ ] No real source, restricted material, credential, or sensitive coordinate
      was used or emitted.
- [ ] Workflow guard-injection, broader domain, policy, proof, release, and
      publication holds remain explicit.
- [ ] Human review remains pending unless independently recorded.

Otherwise use `HOLD`, `CHANGES_REQUESTED`, or `ERROR` with an exact failure
packet.

## Failure diagnosis

| Symptom | Classification | Required response |
|---|---|---|
| Guard import or activation fails | Environment or `PYTHONPATH` error | Stop; correct the command or checkout before testing |
| Representative connection is not denied | No-network enforcement regression | Stop; do not retain the guarded claim; inspect the shared helper and exact revision |
| Focused test fails | Contract, schema, fixture, validator, dependency, or test drift | Record the failing test and exact SHA; do not weaken the test to obtain green |
| Valid historic fixture no longer returns `PASS` | Intended or accidental semantic drift | Compare contract, schema, validator, and fixture bytes; require review |
| Unresolved fixture no longer returns `ABSTAIN` | Fail-closed or expectation regression | Block handoff; unresolved support must not become stronger truth silently |
| Negative fixture no longer returns `DENY` | Fail-closed regression | Block handoff; restore rejection or approve a deliberate semantic change |
| Validator returns `ERROR` | Invalid input or execution failure | Repair tooling/input; do not count as expected denial |
| Worktree gains files or edits | Undeclared side effect or cache output | Preserve evidence, identify the writer, and remove only task-created disposable output |
| Real or restricted transport material appears | Rights, sensitivity, or security incident | Stop propagation; quarantine through the owning process; do not paste payloads into PRs or logs |
| Workflow is green but guard injection is absent | Evidence-scope mismatch | Report only the workflow's bounded local-fixture checks, not process-wide no-egress enforcement |
| Proof, candidate, release, or published artifact appears | Authority or lifecycle expansion | Stop; route through owning contracts, policy, evidence, review, release, correction, and rollback controls |

Never weaken a schema, negative fixture, validator outcome, network guard, or
held boundary merely to obtain a passing result.

### Failure packet

```text
repository:
tested_revision:
worktree_baseline:
python_version:
command:
exit_code:
expected_result:
actual_result:
fixture_or_test:
introduced_or_inherited:
guard_activation:
representative_probe:
sensitive_data_observed: no / HOLD
source_activation: none
lifecycle_effect: none
recommended_disposition: HOLD / CHANGES_REQUESTED / ERROR
rollback_or_correction:
```

Do not include secrets, private URLs, restricted payloads, or precise sensitive
geometry in the packet.

## Safety, rights, and cross-domain boundaries

Roads/Rail/Trade material can expose infrastructure, private-property context,
culturally significant movement corridors, Indigenous or Tribal knowledge,
historic-route uncertainty, and harmful precision. Synthetic fixtures must not
be traced from protected real geometry merely to appear realistic.

Keep these meanings separate:

- a route is not a segment, route-membership assertion, or graph edge;
- an alignment is not proof of designation, operator, legal access, current
  status, condition, or safe passage;
- a crossing does not absorb Hydrology, Infrastructure, Hazards, legal, or
  safety authority;
- a narrative or reconstructed corridor is not a surveyed alignment;
- generalized public geometry does not replace restricted canonical geometry;
  and
- maps, graphs, indexes, tests, workflows, fixtures, and generated language are
  not sovereign truth.

Stop or abstain when source identity, source role, rights, sovereignty,
consent, sensitivity, time, geometry lineage, evidence, policy, review, release,
correction, or rollback support is unresolved.

## Evidence and artifact boundary

This procedure may produce terminal output, pytest results, validator outcomes,
and a GitHub workflow result tied to an exact commit. Those observations are
validation evidence for the bounded repository profile.

They are not a:

- `SourceDescriptor` admission or current-source attestation;
- real-claim `EvidenceRef` or `EvidenceBundle`;
- policy or sensitivity decision;
- accountable review record;
- validation receipt, proof pack, or catalog-closure object;
- promotion decision, release manifest, correction notice, or rollback card;
- governed API response, map layer, routing product, Focus Mode answer, or
  published artifact.

The current Roads/Rail/Trade workflow explicitly holds broader proof and release
dry-run production. This runbook does not fill those gaps with prose.

## Review handoff

```markdown
## Roads/Rail/Trade no-network validation handoff

- Repository:
- Base SHA:
- Tested head or synthetic merge SHA:
- Branch / pull request:
- Python version:
- Dependency bootstrap command and boundary:
- Guard activation result:
- Representative denial probe:
- Focused pytest result:
- Fixture outcome summary:
- Worktree-write check:
- Introduced failures:
- Inherited failures:
- Pending or skipped checks:
- Sensitive data observed: no / HOLD
- Source activation: none
- Lifecycle writes: none
- Evidence/policy/proof/release effect: none
- Workflow guard-injection status: HOLD
- Human reviewer route: @bartytime4life
- Human review state: pending
- Rollback:
- Open verification:
```

The verified GitHub route does not create transport, source, evidence, policy,
safety, security, release, or independent-review expertise. Keep capability
assignments `NEEDS VERIFICATION` until they are evidenced.

## Current holds and graduation triggers

### Holds

- The current domain workflow does not inject the shared startup guard path.
- The full Roads/Rail/Trade object-family suite is not implemented.
- Several crossing, bridge/river-crossing, facility, and topology validators
  remain documentation-only scaffolds.
- The domain smoke test is not substantive coverage.
- Active domain policy evaluation is not established by this profile.
- Real source admission, EvidenceBundle resolution, accountable review, proof
  production, candidate assembly, release dry run, correction, and operational
  rollback are not established.
- No public API, routing, map, graph, deployment, promotion, publication, or
  source activation is authorized.

### Re-review this runbook when

- the contract, schema, fixtures, validator, or focused test set changes;
- the shared guard API or limitations change;
- the domain workflow begins injecting or independently enforcing no-network
  controls;
- a substantive domain test replaces the placeholder smoke test;
- a source, evidence, policy, proof, candidate, release, correction, or rollback
  producer is admitted; or
- the responsibility or path boundary changes through an accepted ADR or
  migration.

## Documentation rollback

Before merge, close the draft pull request and discard only its feature branch.
After an authorized merge, use a reviewed revert or a bounded forward-correction
pull request against current `main`.

Documentation rollback changes this runbook only. It does not alter source
admission, real transport data, contracts, schemas, fixtures, validators, tests,
policy, evidence, proofs, release state, deployments, caches, published
artifacts, or public claims.

Do not restore v0.1's proposal-era implementation claims as current truth.

## Related current surfaces

- [Roads/Rail/Trade runbook boundary](./README.md)
- [Roads/Rail/Trade domain boundary](../../domains/roads-rail-trade/README.md)
- [`CorridorRoute` semantic contract](../../../contracts/domains/roads-rail-trade/corridor_route.md)
- [`CorridorRoute` schema](../../../schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json)
- [Synthetic fixture family](../../../fixtures/domains/roads-rail-trade/corridor_route/)
- [`CorridorRoute` validator](../../../tools/validators/domains/roads-rail-trade/validate_corridor_route.py)
- [Focused contract tests](../../../tests/schemas/test_corridor_route_contract.py)
- [Shared Python startup guard](../../../tools/ci/kfm_no_network/README.md)
- [Domain workflow](../../../.github/workflows/domain-roads-rail-trade.yml)
- [Directory Rules](../../doctrine/directory-rules.md)
- [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)

---

<sub>**Current path:** `docs/runbooks/roads-rail-trade/NO_NETWORK_TEST_RUNBOOK.md` · **Version:** v1.0.0 · **Updated:** 2026-08-29 · **Status:** repository-grounded draft · **Truth posture:** cite-or-abstain · [Back to top](#top)</sub>
