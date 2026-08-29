<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/settlements-infrastructure/no-network-test
title: No-Network Test Runbook — Settlements / Infrastructure
type: runbook
version: v1.0.0
prior_version: v0.1
prior_state: proposal-era domain-wide procedure with unverified commands, fixture trees, policy outcomes, proof production, release closure, and rollback execution
status: DRAFT_REPOSITORY_GROUNDED; BOUNDED_EVIDENCEBUNDLE_SCHEMA_CONVERGENCE_EXECUTABLE; GUARDED_LOCAL_COMMAND_AVAILABLE; WORKFLOW_GUARD_INJECTION_HELD; DOMAIN_SEMANTIC_PROOF_RELEASE_AND_PUBLICATION_HELD; NOT_FOR_OPERATIONAL_USE
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Settlements/Infrastructure, source, evidence, policy, infrastructure-sensitivity, sovereignty, cultural, legal, QA, and release assignments"
created: 2026-05-12
updated: 2026-08-29
policy_label: repository-facing; critical-infrastructure-sensitive; cultural-and-sovereignty-sensitive; fail-closed; shared-fixture-only
current_path: docs/runbooks/settlements-infrastructure/NO_NETWORK_TEST_RUNBOOK.md
owning_root: docs/
responsibility: bounded human procedure for guarded local execution and interpretation of the implemented Settlements/Infrastructure EvidenceBundle schema-convergence profile
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, source records, policy, evidence, review, lifecycle, proof, release, correction, and rollback authorities
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  target_prior_blob: 6608cef57d32ffcfef5b2f394892e11dbdd495ae
  lane_readme_blob: 5de90772b7ae420f42ed2794e7f545e55035aaa9
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  domain_workflow_blob: a47d89c40efd58ac31bc44dbc56bdfb1ccc3a325
  convergence_workflow_blob: 584ac26dcaf5791b1a560cb71bd059e889f55791
  domain_projection_schema_blob: 44c022ffc7f24cc582b061c5f3145b716e3f150f
  shared_evidence_bundle_schema_blob: cf5256831b63dca46a5f68b168441adcf68b8751
  projection_validator_blob: 407c99ad07442e0b4802d057b695e391bdf4f8eb
  convergence_tests_blob: d1cfa0e9064e250dc3d157372d0091ae835d05c1
  shared_fixture_readme_blob: 89ace659414a757c14a4d3e516fd31d44c6a9969
  shared_python_guard_readme_blob: d0e89356c9a9175f2c9798daa1923d73a9034eca
  bounded_test_count: 3
  valid_fixture_count: 1
  invalid_fixture_count: 1
related:
  - ./README.md
  - ../../domains/settlements-infrastructure/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/domain-settlements-infrastructure.yml
  - ../../../.github/workflows/settlements-infrastructure-evidence-bundle-convergence.yml
  - ../../../schemas/contracts/v1/domains/settlements-infrastructure/evidence_bundle.schema.json
  - ../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../../fixtures/contracts/v1/evidence/evidence_bundle/
  - ../../../tools/validators/validate_settlements_infrastructure_evidence_bundle_projection.py
  - ../../../tests/validators/domains/settlements-infrastructure/test_evidence_bundle_schema_convergence.py
  - ../../../tools/ci/kfm_no_network/README.md
notes:
  - "v1.0.0 replaces proposal-era domain-wide commands with the exact bounded EvidenceBundle convergence commands on current main."
  - "The domain schema is a PROPOSED projection of the shared EvidenceBundle shape and creates no independent fields, evidence semantics, critical-infrastructure exposure authority, release authority, or publication authority."
  - "The convergence workflow sets KFM_NO_NETWORK=1 but does not inject tools/ci/kfm_no_network into PYTHONPATH; guarded local execution is available, while workflow-wide startup enforcement remains held."
  - "Connected Drive and Notion material remains proposal and coordination lineage; the current repository determines executable claims."
  - "The hosted Sites Explorer is not exercised or changed by this runbook."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# No-Network Test Runbook — Settlements / Infrastructure

Use this runbook to execute and interpret the repository's bounded
Settlements/Infrastructure `EvidenceBundle` schema-convergence profile without
live source retrieval or intentional network access. The procedure is
deterministic, read-only, and limited to the exact revision under review.

> [!WARNING]
> KFM is not a municipal, census, land-status, infrastructure-ownership,
> facility-condition, service-availability, engineering, emergency, safety,
> security, legal, planning, or regulatory authority. A passing repository
> check does not establish that any place, boundary, facility, network,
> operator, condition, dependency, service, or access route is real, current,
> complete, lawful, available, or safe.

> [!IMPORTANT]
> Current executable scope is schema convergence only: one proposed domain
> projection, one shared schema, one shared valid fixture, one shared invalid
> fixture, three focused tests, and one validator wrapper. It does not establish
> materialized evidence, real source admission, policy execution, accountable
> review, proof, release, deployment, promotion, rollback execution, or
> publication.

**Use:** [scope](#scope) · [preconditions](#preconditions) ·
[procedure](#procedure) · [outcomes](#outcomes-and-acceptance) ·
[failure diagnosis](#failure-diagnosis) · [handoff](#review-handoff) ·
[rollback](#documentation-rollback)

## Purpose and authority

This runbook operationalizes the currently implemented no-network-compatible
schema slice for Settlements/Infrastructure. It tells a maintainer how to:

- activate the shared Python-process startup guard for the validation window;
- prove that a representative connection path is denied in a fresh process;
- compile and run the focused schema-convergence test module;
- validate the shared positive and negative fixtures through the domain
  projection;
- interpret `OK`, `EXPECTED_FAIL`, and `FAIL` without widening them into domain,
  evidence, policy, release, or publication claims; and
- preserve a reviewable failure and rollback boundary.

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md). Those rules
place human operational procedures under `docs/runbooks/`; the schema,
fixtures, validator, tests, workflows, and CI helper remain in their owning
responsibility roots.

This document explains those authorities. It does not replace or amend them.

## Current implementation boundary

| Surface | Current repository evidence | Bounded conclusion | Not established |
|---|---|---|---|
| Domain projection | `schemas/contracts/v1/domains/settlements-infrastructure/evidence_bundle.schema.json` | Proposed projection delegates its complete shape to the shared schema and denies independent fields or exposure authority | Accepted domain evidence semantics or a materialized domain EvidenceBundle |
| Shared schema | `schemas/contracts/v1/evidence/evidence_bundle.schema.json` | Closed draft object shape requires ten top-level fields | Claim truth, source authority, rights correctness, sensitivity correctness, or evidence closure |
| Shared fixtures | `valid/valid_1.json` and `invalid/invalid_1.json` under the shared EvidenceBundle fixture root | One example is accepted and one example without `bundle_id` is rejected | Settlements/Infrastructure source, geometry, facility, operator, network, or dependency coverage |
| Validator wrapper | `validate_settlements_infrastructure_evidence_bundle_projection.py` | Runs the shared JSON Schema harness against the domain projection | Domain policy, evidence resolution, proof production, or release decision |
| Focused tests | Three tests in `test_evidence_bundle_schema_convergence.py` | Projection delegation, shared required fields, and positive/negative fixture behavior are checked | A substantive Settlements/Infrastructure domain suite |
| Shared guard | `tools/ci/kfm_no_network/sitecustomize.py` and its README | Opt-in startup denial for named Python IPv4/IPv6 connection, send, resolver, and URL-open paths | Operating-system, runner-wide, container, namespace, dependency-install, non-Python, or arbitrary private-API isolation |
| Convergence workflow | `.github/workflows/settlements-infrastructure-evidence-bundle-convergence.yml` | Compiles the focused files, runs three tests, and replays two shared fixtures with deterministic environment values | Shared startup-guard injection or runner-wide no-egress enforcement |
| Domain readiness workflow | `.github/workflows/domain-settlements-infrastructure.yml` | Checks current paths, parses tracked JSON, classifies placeholders, and records proof and release holds | Semantic domain validation, proof, release dry run, or publication readiness |

### Guard wiring gap

The convergence workflow currently sets `KFM_NO_NETWORK=1`, but the shared
guard loads only when `tools/ci/kfm_no_network` is also present on `PYTHONPATH`
before Python starts. Therefore:

- the workflow's current environment value is not, by itself, proof that the
  shared startup guard was active;
- the focused code path remains bounded to tracked local schemas and fixtures;
- this runbook injects the guard explicitly for local execution; and
- workflow-wide startup enforcement remains `NEEDS VERIFICATION` until the
  workflow is deliberately updated and proven with a negative probe.

Do not describe either workflow as host-wide, runner-wide, or process-wide
no-egress enforcement.

## Scope

### Included

- the exact schemas, shared fixtures, validator, tests, and workflows named in
  this runbook;
- local tracked inputs only;
- explicit shared-guard activation for each Python process in the validation
  window;
- a representative fresh-process denial probe;
- deterministic positive and negative schema expectations; and
- worktree-write checks after the procedure.

### Excluded

- dependency installation from the guarded window;
- live Census, KDOT, Kansas Geoportal, FEMA, USGS, municipal, utility,
  operator, Tribal, archival, or other source requests;
- real place, legal status, ownership, boundary, facility, condition, service,
  dependency, vulnerability, capacity, access, or safety determinations;
- source admission, EvidenceRef resolution, EvidenceBundle construction,
  active policy evaluation, specialist review, or infrastructure-exposure
  approval;
- domain fixtures below `fixtures/domains/settlements-infrastructure/`, which
  remain placeholder topology rather than this profile's inputs;
- hosted Sites Explorer, MapLibre, browser, API, graph, tile, export, search,
  Focus Mode, model-provider, deployment, or access-control behavior;
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
   schemas/contracts/v1/domains/settlements-infrastructure/evidence_bundle.schema.json
   schemas/contracts/v1/evidence/evidence_bundle.schema.json
   fixtures/contracts/v1/evidence/evidence_bundle/valid/valid_1.json
   fixtures/contracts/v1/evidence/evidence_bundle/invalid/invalid_1.json
   tools/validators/validate_settlements_infrastructure_evidence_bundle_projection.py
   tests/validators/domains/settlements-infrastructure/test_evidence_bundle_schema_convergence.py
   tools/ci/kfm_no_network/sitecustomize.py
   ```

3. Use Python 3.11, matching both current domain workflows.
4. Confirm no real, restricted, credentialed, or operational settlement or
   infrastructure material is present in the test input.
5. Confirm no lifecycle, source, proof, candidate, release, or published write
   is intended.
6. Record any pre-existing worktree change. Prefer a clean worktree; do not
   attribute inherited changes to this procedure.

### Dependency bootstrap boundary

The convergence workflow installs the declared `project-test` profile with:

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
export TZ=UTC
export PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD${PYTHONPATH:+:$PYTHONPATH}"

python -c 'import sitecustomize; assert sitecustomize.GUARD_ACTIVE'
```

Expected result: exit code `0`. Any import error or false `GUARD_ACTIVE` is
`ERROR`; stop before running the profile.

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

### 3. Compile the focused validator and tests

```bash
python -m py_compile \
  tools/validators/validate_settlements_infrastructure_evidence_bundle_projection.py \
  tests/validators/domains/settlements-infrastructure/test_evidence_bundle_schema_convergence.py
```

Expected result: exit code `0` and no repository output because
`PYTHONDONTWRITEBYTECODE=1` is active.

### 4. Run the focused convergence tests

```bash
python -m unittest discover \
  --start-directory tests/validators/domains/settlements-infrastructure \
  --pattern 'test_evidence_bundle_schema_convergence.py' \
  --verbose
```

Expected result at the evidence snapshot: three tests pass. They check:

- the domain projection references the shared schema and denies independent
  fields and exposure authority;
- the shared schema remains closed and requires its ten declared top-level
  fields; and
- the projection accepts the tracked valid fixture and rejects the tracked
  fixture that omits `bundle_id`.

A different test count is a review trigger, not automatically a defect. Inspect
the exact diff and update this runbook only after the changed coverage is
understood.

### 5. Replay the shared fixtures through the domain projection

```bash
python \
  tools/validators/validate_settlements_infrastructure_evidence_bundle_projection.py \
  --fixtures
```

Expected result at the evidence snapshot:

- `valid/valid_1.json` prints `OK`;
- `invalid/invalid_1.json` prints `EXPECTED_FAIL` because `bundle_id` is
  required; and
- the command exits `0` only when both expectations hold.

The successful exit does not mean both fixtures are valid. It means the positive
fixture was accepted and the negative fixture was rejected as declared.

### 6. Confirm the procedure wrote no repository content

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

### Schema-runner outcomes

| Output | Implemented meaning | Permitted conclusion |
|---|---|---|
| `OK <valid fixture>` | The tracked positive fixture satisfied the proposed projection and shared schema | This example satisfied the bounded schema profile |
| `EXPECTED_FAIL <invalid fixture>` | The tracked negative fixture was rejected as declared | The required-field negative control remains effective |
| `FAIL <path>: <reason>` | A positive fixture failed, a negative fixture was accepted, input could not be read, or evaluation failed | Stop and diagnose; no trust conclusion is available |
| Exit `0` from `--fixtures` | Every tracked positive and negative expectation matched | The two-fixture schema profile is internally consistent at this revision |
| Exit `1` or `2` | Validation failed or required input was absent | Use `HOLD` or `ERROR`; do not report convergence |

These are harness outputs, not `ANSWER`, `ABSTAIN`, `DENY`, or governed runtime
decisions. Do not translate `OK` into evidence closure, policy approval, or
release readiness.

### Acceptance checklist

Use `READY_FOR_HUMAN_REVIEW` only when all applicable items hold:

- [ ] Exact repository revision and worktree baseline were recorded.
- [ ] Shared guard activation succeeded in the validation process.
- [ ] The representative denial probe succeeded.
- [ ] Focused compilation and all three tests passed without weakened checks.
- [ ] The valid fixture returned `OK` and the invalid fixture returned
      `EXPECTED_FAIL`.
- [ ] No new repository content was written.
- [ ] No live source, real infrastructure detail, restricted material,
      credential, or sensitive coordinate was used or emitted.
- [ ] Workflow guard-injection, broader domain, policy, proof, release, Sites,
      and publication holds remain explicit.
- [ ] Human review remains pending unless independently recorded.

Otherwise use `HOLD`, `CHANGES_REQUESTED`, or `ERROR` with an exact failure
packet.

## Failure diagnosis

| Symptom | Classification | Required response |
|---|---|---|
| Guard import or activation fails | Environment or `PYTHONPATH` error | Stop; correct the command or checkout before testing |
| Representative connection is not denied | No-network enforcement regression | Stop; do not retain the guarded claim; inspect the shared helper and exact revision |
| Compilation fails | Syntax, import, or environment error | Record the exact file and revision; repair without bypassing compilation |
| Projection gains independent fields or authority | Schema-authority drift | Stop; reconcile shared/domain authority rather than duplicating fields |
| Shared required fields change | Contract/schema drift | Review the shared contract, schema, fixtures, consumers, and compatibility impact |
| Valid fixture is rejected | Positive-profile regression | Compare schema, resolver, fixture, and validator bytes |
| Invalid fixture is accepted | Fail-closed regression | Block handoff; restore rejection or approve a deliberate schema change through the owning process |
| Validator prints `FAIL` or exits nonzero | Input or evaluation failure | Repair tooling/input; do not count it as expected rejection |
| Worktree gains files or edits | Undeclared side effect or cache output | Preserve evidence, identify the writer, and remove only task-created disposable output |
| Real or restricted material appears | Rights, sensitivity, sovereignty, privacy, or security incident | Stop propagation; quarantine through the owning process; do not paste payloads into PRs or logs |
| Workflow is green but guard injection is absent | Evidence-scope mismatch | Report only the workflow's bounded local-schema checks, not process-wide no-egress enforcement |
| Proof, candidate, release, or published artifact appears | Authority or lifecycle expansion | Stop; route through owning contracts, policy, evidence, review, release, correction, and rollback controls |

Never weaken a schema, negative fixture, validator expectation, network guard, or
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

Do not include secrets, private URLs, restricted payloads, facility interiors,
dependency graphs, exploitable condition details, or precise sensitive geometry
in the packet.

## Safety, rights, and cross-domain boundaries

Settlements/Infrastructure material can expose critical assets, facility
interiors, dependencies, condition observations, service gaps,
private-property context, living-person proximity, reservation communities,
culturally significant places, archaeological locations, and harmful
precision. Shared schema examples must not be mistaken for clearance to create
or publish domain material.

Keep these meanings separate:

- a legal municipality is not interchangeable with a census place, named
  place, post office, historic townsite, community, or map label;
- a facility record is not proof of ownership, operation, condition, capacity,
  availability, safety, access, or current status;
- a dependency edge or service area is not authority to expose a vulnerable
  network or infer continuity risk;
- generalized public geometry does not replace restricted canonical geometry;
- neighboring Roads/Rail/Trade, Hazards, Hydrology, People/DNA/Land,
  Archaeology, legal, emergency, safety, and regulatory claims retain their own
  authority; and
- maps, indexes, schemas, fixtures, tests, workflows, dashboards, Sites, and
  generated language are not sovereign truth.

Stop or abstain when source identity, source role, rights, sovereignty,
consent, sensitivity, time, geometry lineage, evidence, policy, review, release,
correction, or rollback support is unresolved.

## Evidence and artifact boundary

This procedure may produce terminal output, unittest results, validator output,
and GitHub workflow results tied to an exact commit. Those observations are
validation evidence for the bounded repository profile.

They are not a:

- source admission or current-source attestation;
- real-claim `EvidenceRef` or materialized `EvidenceBundle`;
- policy, sensitivity, sovereignty, cultural, legal, or infrastructure-security
  decision;
- accountable review record;
- validation receipt, proof pack, or catalog-closure object;
- promotion decision, release manifest, correction notice, or rollback card;
- governed API response, hosted Sites validation, map layer, Focus Mode answer,
  or published artifact.

The domain workflow explicitly holds semantic validation, proof production, and
release-dry-run production. This runbook does not fill those gaps with prose.

## Review handoff

```markdown
## Settlements/Infrastructure no-network validation handoff

- Repository:
- Base SHA:
- Tested head or synthetic merge SHA:
- Branch / pull request:
- Python version:
- Dependency bootstrap command and boundary:
- Guard activation result:
- Representative denial probe:
- Focused unittest result:
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
- Sites runtime validation: NOT_RUN / out of scope
- Human reviewer route: @bartytime4life
- Human review state: pending
- Rollback:
- Open verification:
```

The verified GitHub route does not create domain, source, evidence, policy,
legal, safety, security, sovereignty, cultural, release, or independent-review
expertise. Keep capability assignments `NEEDS VERIFICATION` until evidenced.

## Current holds and graduation triggers

### Holds

- The convergence workflow does not inject the shared startup guard path.
- The domain readiness workflow remains a static readiness and hold detector.
- `fixtures/domains/settlements-infrastructure/` contains placeholder topology,
  not this profile's substantive domain fixtures.
- The full Settlements/Infrastructure object-family suite is not implemented.
- Active domain policy evaluation is not established by this profile.
- Real source admission, EvidenceRef resolution, materialized EvidenceBundles,
  accountable specialist review, proof production, candidate assembly, release
  dry run, correction, and operational rollback are not established.
- No public API, Sites runtime, map, graph, deployment, promotion, publication,
  or source activation is authorized.

### Re-review this runbook when

- either EvidenceBundle schema, either shared fixture, the validator, or the
  focused test set changes;
- the shared guard API or limitations change;
- the convergence workflow begins injecting or independently enforcing
  no-network controls;
- substantive domain fixtures or tests replace placeholders;
- a source, evidence, policy, proof, candidate, release, correction, or rollback
  producer is admitted; or
- the responsibility or path boundary changes through an accepted ADR or
  migration.

## Documentation rollback

Before merge, close the draft pull request and discard only its feature branch.
After an authorized merge, use a reviewed revert or a bounded
forward-correction pull request against current `main`.

Documentation rollback changes this runbook and its directly related runbook
index classification only. It does not alter source admission, real domain data,
contracts, schemas, fixtures, validators, tests, policy, evidence, proofs,
release state, Sites deployments, caches, published artifacts, or public
claims.

Do not restore v0.1's proposal-era implementation claims as current truth.

## Related current surfaces

- [Settlements/Infrastructure runbook boundary](./README.md)
- [Settlements/Infrastructure domain boundary](../../domains/settlements-infrastructure/README.md)
- [Domain EvidenceBundle projection](../../../schemas/contracts/v1/domains/settlements-infrastructure/evidence_bundle.schema.json)
- [Shared EvidenceBundle schema](../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json)
- [Shared EvidenceBundle fixtures](../../../fixtures/contracts/v1/evidence/evidence_bundle/)
- [Projection validator](../../../tools/validators/validate_settlements_infrastructure_evidence_bundle_projection.py)
- [Focused convergence tests](../../../tests/validators/domains/settlements-infrastructure/test_evidence_bundle_schema_convergence.py)
- [Shared Python startup guard](../../../tools/ci/kfm_no_network/README.md)
- [EvidenceBundle convergence workflow](../../../.github/workflows/settlements-infrastructure-evidence-bundle-convergence.yml)
- [Domain readiness workflow](../../../.github/workflows/domain-settlements-infrastructure.yml)
- [Directory Rules](../../doctrine/directory-rules.md)
- [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)

---

<sub>**Current path:** `docs/runbooks/settlements-infrastructure/NO_NETWORK_TEST_RUNBOOK.md` · **Version:** v1.0.0 · **Updated:** 2026-08-29 · **Status:** repository-grounded draft · **Truth posture:** cite-or-abstain · [Back to top](#top)</sub>
