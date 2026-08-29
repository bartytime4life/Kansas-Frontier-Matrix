<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/settlements-infrastructure/no-network-test
title: Settlements / Infrastructure No-Network Test Runbook
type: runbook
version: v1.0
prior_version: v0.1
prior_state: proposal-era procedure with unverified commands, fixture trees, workflow, and receipt outputs
status: DRAFT_REPOSITORY_GROUNDED; SHARED_PYTHON_GUARD_AVAILABLE; SETTLEMENTS_SPECIFIC_SUBSTANTIVE_NO_NETWORK_PROOF_ABSENT; RUNNER_WIDE_AND_NON_PYTHON_EGRESS_DENIAL_HELD
owners:
  - "@bartytime4life — verified repository review route"
  - "NEEDS VERIFICATION — accountable Settlements/Infrastructure, QA, security, policy, evidence, release, and operations assignments"
created: 2026-05-12
updated: 2026-08-29
policy_label: repository-facing; validation-sensitive; fail-closed
current_path: docs/runbooks/settlements-infrastructure/NO_NETWORK_TEST_RUNBOOK.md
owning_root: docs/
responsibility: Human procedure for reproducing and interpreting the lane's current bounded Python-process no-network posture without claiming substantive domain validation, runner-wide isolation, source admission, evidence closure, policy approval, release, deployment, or publication.
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
current_disposition: SHARED_PYTHON_GUARD_AVAILABLE / DOMAIN_PROOF_AND_WORKFLOW_HELD
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: ab312c693eb7315bb111bc6484d78d2a28d6f3d5
  target_prior_blob: 6608cef57d32ffcfef5b2f394892e11dbdd495ae
  shared_guard_readme_blob: d0e89356c9a9175f2c9798daa1923d73a9034eca
  shared_guard_blob: 0f2c661459b73179f531f0ce1d3b0892d05ee7c8
  settlements_tests_readme_blob: 08cd09f1700ca02fae7a35c55a1c22684c996448
  settlements_fixtures_readme_blob: 7c72dba10228decae24e9b46561e1370fa6a6cec
  settlements_schema_readme_blob: 5b8d78c55ca6872e54e5ad99ed418427313a62e9
  settlements_policy_readme_blob: 792a67caab14d119cf4a21dee1365216bfaefb11
  settlements_workflow_blob: a47d89c40efd58ac31bc44dbc56bdfb1ccc3a325
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
related:
  - README.md
  - ../README.md
  - ../../domains/settlements-infrastructure/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../tools/ci/kfm_no_network/README.md
  - ../../../tools/ci/kfm_no_network/sitecustomize.py
  - ../../../tests/domains/settlements-infrastructure/README.md
  - ../../../fixtures/domains/settlements-infrastructure/README.md
  - ../../../schemas/contracts/v1/domains/settlements-infrastructure/README.md
  - ../../../policy/domains/settlements-infrastructure/README.md
  - ../../../.github/workflows/domain-settlements-infrastructure.yml
non_effects:
  - does_not_contact_or_validate_live_sources
  - does_not_establish_runner_wide_or_non_python_egress_denial
  - does_not_create_substantive_settlements_infrastructure_test_coverage
  - does_not_activate_or_admit_sources
  - does_not_write_lifecycle_evidence_proof_release_or_published_state
  - does_not_validate_or_change_the_deployed_explorer
  - does_not_promote_release_deploy_or_publish
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements / Infrastructure No-Network Test Runbook

Use this procedure to reproduce the lane's current bounded Python-process
no-network posture at an exact repository revision. The repository provides an
opt-in startup guard, but it does not yet provide a substantive
Settlements/Infrastructure no-network proof, fixture corpus, or domain workflow.

> [!IMPORTANT]
> A green command today proves only that the shared Python guard loaded and that
> the lane's current placeholder test package did not fail. It does not prove
> settlement identity, municipal status, census-place separation, infrastructure
> topology, restricted-geometry denial, evidence closure, policy enforcement,
> release readiness, or publication safety.

## 1. Authority and scope

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
and the adopted [Directory Rules](../../doctrine/directory-rules.md) place human
procedures under `docs/runbooks/`. Executable tests belong under `tests/`,
fixtures under `fixtures/`, machine shapes under `schemas/`, binding rules under
`policy/`, and release decisions under `release/`.

This file explains current executable evidence. It does not create or amend a
contract, schema, fixture, validator, policy, workflow, EvidenceBundle, proof,
PromotionDecision, ReleaseManifest, rollback object, deployment, or publication
state.

In scope:

- loading the repository-owned Python startup guard before application imports;
- proving that one named Python egress attempt fails with the guard's expected
  denial message;
- running the current Settlements/Infrastructure test package under that guard;
- classifying the result without upgrading placeholder coverage into domain
  assurance.

Out of scope:

- operating-system, container, network-namespace, runner-wide, dependency-install,
  subprocess, native-extension, browser, Node.js, or other non-Python isolation;
- live Census, GNIS, KDOT, FEMA, municipal, utility, archive, geocoder, map, model,
  or telemetry requests;
- real settlement, person, property, cultural, facility, condition, dependency,
  or exact infrastructure geometry;
- source admission, lifecycle writes, evidence or proof production, policy or
  review approval, release, deployment, promotion, publication, or public use;
- the connected Explorer/Sites publication, which is a networked deployed
  consumer and cannot serve as no-network test evidence.

[Back to top](#top)

## 2. Current repository evidence

| Surface | Current state at the evidence snapshot | Bounded conclusion |
|---|---|---|
| [`tools/ci/kfm_no_network/sitecustomize.py`](../../../tools/ci/kfm_no_network/sitecustomize.py) | Substantive opt-in Python startup guard | When loaded with `KFM_NO_NETWORK=1`, it denies the documented IPv4/IPv6 socket, resolver, and `urllib` paths while preserving Unix-domain sockets. |
| [`tools/ci/kfm_no_network/README.md`](../../../tools/ci/kfm_no_network/README.md) | Current activation contract and limitation statement | The guard is process-level, not a host firewall or runner-wide proof. |
| [`tests/domains/settlements-infrastructure/`](../../../tests/domains/settlements-infrastructure/README.md) | Seven named test modules contain proposal docstrings only; the smoke module contains one `assert True`; `identity/` contains documentation but no executable identity test | The lane has package presence and one trivial collection canary, not substantive domain coverage. |
| [`fixtures/domains/settlements-infrastructure/`](../../../fixtures/domains/settlements-infrastructure/README.md) | Stub README, `.gitkeep` files, and three placeholder Markdown files; no domain JSON fixture corpus | Valid, invalid, denied, abstention, correction, or rollback polarity is not established. |
| [`schemas/contracts/v1/domains/settlements-infrastructure/`](../../../schemas/contracts/v1/domains/settlements-infrastructure/README.md) | Domain schemas are present | The current lane test package does not bind or validate them. |
| [`policy/domains/settlements-infrastructure/`](../../../policy/domains/settlements-infrastructure/README.md) | Domain Rego files are present | No current Settlements/Infrastructure no-network suite proves their evaluation or expected decisions. |
| `pipelines/domains/settlements-infrastructure/` | Mostly tiny greenfield modules | No offline pipeline behavior or lifecycle transition is established. |
| [`.github/workflows/domain-settlements-infrastructure.yml`](../../../.github/workflows/domain-settlements-infrastructure.yml) | Read-only static readiness workflow; parses schema and fixture structure, recognizes placeholders, and records explicit semantic-validation, proof, and release holds; it does not run the lane tests or shared no-network guard | Static responsibility/readiness checks are present. Settlements-specific no-network execution, semantic validation, proof production, and release dry-run execution are not established. |

Planning material in connected Google Drive correctly emphasizes source-role
separation, public-safe synthetic fixtures, restricted-infrastructure caution,
and reversible publication. It also states that it was prepared without a
mounted repository. It remains design lineage; the repository inventory above
controls current-behavior claims. Notion remains coordination only.

[Back to top](#top)

## 3. Preconditions

Stop before running if any requirement cannot be met.

1. Use a clean checkout of the exact commit under review.
2. Install the repository's test dependencies before enabling the guard. Do not
   install packages during a claimed no-network execution.
3. Confirm the shared guard files and the Settlements/Infrastructure test package
   exist at that revision.
4. Confirm no real or restricted data has replaced the placeholder fixtures.
5. Record the revision and worktree state:

```bash
git rev-parse HEAD
git status --short
```

A dirty tree is not automatically invalid, but the changed paths must be included
in the handoff. Do not describe a dirty-tree result as an exact-commit result.

[Back to top](#top)

## 4. Activate and prove the shared Python guard

Run from the repository root in a dedicated subshell whose dependencies are
already present. Exiting the subshell restores the caller's environment:

```bash
bash --noprofile --norc

export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
export PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD${PYTHONPATH:+:$PYTHONPATH}"

python -c 'import sitecustomize; assert sitecustomize.GUARD_ACTIVE'
```

Then run a negative probe against an IANA documentation address. Success means
the connection attempt fails and the expected guard message is present:

```bash
probe_log="$(mktemp)"
if python -c "import socket; socket.create_connection(('192.0.2.1', 443), timeout=1)" \
  2>"$probe_log"; then
  echo "ERROR: guarded Python connection unexpectedly succeeded" >&2
  rm -f "$probe_log"
  exit 1
fi

grep -F "KFM no-network guard denied Python network egress" "$probe_log"
rm -f "$probe_log"
```

If guard activation or the negative probe fails, classify the run as `ERROR` and
do not continue under a no-network label.

For a broader negative test of the same shared control, run its current
fresh-interpreter proof:

```bash
python -m pytest -q tests/domains/hydrology/test_no_network_proof.py
```

That test is currently stored in the Hydrology package. Its result may support
the shared guard's named Python API behavior, but it is not
Settlements/Infrastructure domain proof.

[Back to top](#top)

## 5. Run the current lane package

With the guard still active:

```bash
python -m pytest -q tests/domains/settlements-infrastructure
```

At the evidence snapshot, only
`test_settlements_infrastructure_smoke.py::test_placeholder` contains an
executable assertion. The other named modules are proposal docstrings. Therefore:

- a pass means the package collected and its placeholder canary passed under the
  bounded Python-process guard;
- a failure is actionable test or environment evidence;
- either result leaves substantive domain validation, fixture polarity, policy
  execution, and workflow enforcement held.

Do not add flags that silently exclude failures, accept zero collected tests, or
turn warnings into unreviewed success. If new substantive tests or fixtures land,
reconcile this inventory and their exact commands before claiming broader
coverage.

[Back to top](#top)

## 6. Interpret and record the result

| Observation | Classification | Allowed statement |
|---|---|---|
| Guard loads, negative probe denies, and current lane package passes | `PASS / PLACEHOLDER COVERAGE ONLY` | The bounded Python guard was active and the current placeholder package did not fail at the recorded revision. |
| Guard activation or negative probe fails | `ERROR` | No no-network claim is available. |
| Shared guard proof fails | `ERROR / SHARED CONTROL REGRESSION` | Investigate the shared guard; do not weaken or bypass it. |
| Lane package fails | `FAIL` | Report the exact failing node and revision; do not infer source, policy, or release consequences beyond the failure. |
| New substantive files are present but not inventoried here | `NEEDS VERIFICATION` | Update the runbook from current repository evidence before broadening the claim. |
| Stronger host, container, or runner isolation is required | `HOLD` | A separate reviewed enforcement mechanism and negative proof are required. |

Record at minimum:

- exact commit or synthetic merge SHA;
- dirty-tree paths, if any;
- Python version;
- guard activation result;
- negative-probe command and denial message;
- exact pytest commands, collected count, pass/fail/skip count, and duration;
- known limitations and the terminal classification from the table above.

Console output or a CI check is execution evidence only. It is not an
EvidenceBundle, proof pack, release receipt, approval, or publication record.

[Back to top](#top)

## 7. Failure triage

### Guard does not load

Verify that `tools/ci/kfm_no_network` is first on `PYTHONPATH`, the command runs
from the repository root, and `KFM_NO_NETWORK` is exactly `1`. Do not replace the
guard with an ad hoc test-local monkeypatch and preserve the same claim.

### A guarded Python network operation succeeds

Stop the run. Preserve the minimal reproducer and revision, classify the result
as a shared-control regression, and repair the control in a separate tested
change. Do not continue to domain assertions under a no-network label.

### The lane reports a pass with only one test

That is the current expected collection shape, not mature coverage. Preserve the
`PLACEHOLDER COVERAGE ONLY` qualifier. The next implementation slice must add
public-safe synthetic fixtures and substantive positive and negative assertions
before this runbook can claim domain behavior.

### A test attempts a live or sensitive read

Stop. Remove the live dependency from the default suite and replace it with a
reviewed local fixture. Do not copy exact critical-infrastructure geometry,
operator details, inspection data, living-person data, cultural locations,
credentials, or production payloads into the repository to make a test offline.

[Back to top](#top)

## 8. Held acceptance boundary

The lane remains held until a reviewed change establishes all applicable items:

- substantive public-safe fixtures with explicit positive and expected-negative
  polarity;
- executable tests for the intended schema, identity, source-role, temporal,
  sensitivity, topology, evidence, policy, correction, and rollback boundaries;
- an accepted command that binds those fixtures to current contracts and schemas;
- a Settlements/Infrastructure-specific negative no-network proof or an accepted
  domain-neutral shared proof location;
- deliberate no-network execution in the current read-only readiness workflow,
  including the shared guard and a negative proof without removing its semantic,
  proof, or release holds;
- hosted exact-head evidence and any required-check coupling separately verified;
- accountable review assignments and rollback guidance.

None of these gates requires or authorizes live-source access, source activation,
lifecycle mutation, release, deployment, promotion, publication, or a change to
the connected Explorer.

[Back to top](#top)

## 9. Rollback

This procedure writes no repository or lifecycle artifacts. Exit the dedicated
subshell after the run:

```bash
exit
```

If a dedicated subshell was not used, restore the caller's prior environment;
do not blindly unset a pre-existing `PYTHONPATH`.

If this documentation change proves inaccurate, close or revert its unmerged
branch and restore the prior blob. Do not restore the prior hypothetical commands
as current implementation claims without new repository evidence.

## Related documentation

- [Settlements / Infrastructure runbook index](README.md)
- [Runbooks root contract](../README.md)
- [Settlements / Infrastructure domain documentation](../../domains/settlements-infrastructure/README.md)
- [Shared Python no-network guard](../../../tools/ci/kfm_no_network/README.md)
- [Settlements / Infrastructure tests](../../../tests/domains/settlements-infrastructure/README.md)
- [Settlements / Infrastructure fixtures](../../../fixtures/domains/settlements-infrastructure/README.md)
- [Settlements / Infrastructure readiness workflow](../../../.github/workflows/domain-settlements-infrastructure.yml)
- [Accepted Directory Rules adoption](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Adopted Directory Rules](../../doctrine/directory-rules.md)

[Back to top](#top)
