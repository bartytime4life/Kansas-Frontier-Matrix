<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-people-dna-land-validation
title: People/DNA/Land Validation Runbook
type: runbook
version: v1.0.1
prior_version: v1.0.0
prior_state: explicit scaffold with no operational procedure
status: DRAFT_REPOSITORY_GROUNDED; TWO_BOUNDED_DOMAIN_WORKFLOW_PROFILES_EXECUTABLE; FOCUSED_HISTORICAL_RESOLUTION_AND_EVIDENCE_BUNDLE_CONVERGENCE_SUITES_EXECUTABLE; BROADER_SEMANTICS_POLICY_PROOF_RELEASE_AND_PUBLICATION_HELD
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable People/DNA/Land, privacy, consent, Indigenous/Tribal, legal, policy, source, evidence, proof, release, operations, and independent-review assignments"
created: 2026-08-29
updated: 2026-08-29
policy_label: repository-facing; sensitive-domain; synthetic-fixture-only; validation; fail-closed; non-release; non-publication
current_path: docs/runbooks/people-dna-land/VALIDATION_RUNBOOK.md
owning_root: docs/
responsibility: Human procedure for selecting, running, interpreting, and recording the People/DNA/Land lane's current repository-backed synthetic validation surfaces without admitting real sensitive material or claiming policy, evidence, proof, release, deployment, or publication authority.
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, source and evidence authority, executable validators and tests, workflow definitions, policy, accountable review, lifecycle, proof, release, correction, revocation, withdrawal, rollback, and sovereignty-aware stewardship
current_disposition: BOUNDED_SYNTHETIC_VALIDATION_AVAILABLE / REAL_DATA_POLICY_RUNTIME_PROOF_RELEASE_AND_PUBLICATION_HELD
reason_codes:
  - PDL_VALIDATION_EXACT_SHA_REQUIRED
  - PDL_VALIDATION_SYNTHETIC_FIXTURES_ONLY
  - PDL_VALIDATION_SCOPE_LIMITED_TO_NAMED_PROFILE
  - PDL_VALIDATION_EXPECTED_REJECTION_REQUIRED
  - PDL_VALIDATION_REAL_SENSITIVE_DATA_DENIED
  - PDL_VALIDATION_POLICY_RUNTIME_NEEDS_VERIFICATION
  - PDL_VALIDATION_EVIDENCE_PROOF_RELEASE_AND_PUBLICATION_HELD
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: c00096f904c66053938355e52f4a5cb9402be6a4
  target_prior_blob: 9ac1079ed880d3c94d52aabe083541987a9afc39
  lane_readme_prior_blob: 1ba3f28deaaea1fc9811ee1eb58e59558c2ecd84
  domain_workflow_blob: bcf64c3e3b6653b9543489fc5a6031805ae3ef48
  evidence_convergence_workflow_blob: d8414de26b72507689c92f61f5d0953cd4b63391
  consent_overlay_test_blob: 2ee112baeb352846dd0ef4d065baf0177e7aa38b
  consent_overlay_validator_blob: 6ea7a2904b2062df2ef080785035c43588a4e633
  revocation_assessment_test_blob: bceeef36e5c4e456e6f8a3fc192cd1c349d34fb5
  revocation_assessment_validator_blob: 76c7805428f253a7a711c7bc68a27e9cbcce40e7
  historical_resolution_test_blob: 9c98ad5b6b4e11ed6625305121e0e39026eac1c1
  historical_resolution_validator_blob: 3ce791ef6b04a87807146675a7d1536ee6c713bc
  evidence_convergence_test_blob: 0823f8254cf80ba9a6fc0ab92ae3b7976784ff90
  evidence_projection_validator_blob: 1393ed22ec8a6f46f2745bffdb0f7406bc90d7a1
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
related:
  - ./README.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./LIVING_PERSON_REVIEW.md
  - ./CONSENT_RUNBOOK.md
  - ./revocation.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/people-dna-land/README.md
  - ../../domains/people-dna-land/API_CONTRACTS.md
  - ../../../.github/workflows/domain-people-dna-land.yml
  - ../../../.github/workflows/people-dna-land-evidence-bundle-convergence.yml
  - ../../../contracts/domains/people-dna-land/README.md
  - ../../../schemas/contracts/v1/domains/people-dna-land/README.md
  - ../../../policy/domains/people-dna-land/README.md
  - ../../../policy/consent/people-dna-land/README.md
  - ../../../fixtures/domains/people-dna-land/README.md
  - ../../../fixtures/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution/README.md
  - ../../../tests/domains/people-dna-land/README.md
  - ../../../tests/validators/domains/people-dna-land/test_evidence_bundle_schema_convergence.py
  - ../../../tests/validators/test_validate_historical_person_place_event_resolution.py
  - ../../../tools/validators/domains/people-dna-land/README.md
  - ../../../tools/validators/validate_historical_person_place_event_resolution.py
  - ../../../tools/validators/validate_people_dna_land_evidence_bundle_projection.py
non_effects:
  - does_not_process_real_people_genealogy_dna_consent_land_title_or_culturally_restricted_material
  - does_not_contact_live_sources_or_vendor_accounts
  - does_not_establish_runner_wide_or_non_python_egress_denial
  - does_not_activate_or_replace_policy
  - does_not_issue_validate_or_revoke_real_consent
  - does_not_resolve_real_evidence_refs_or_create_evidence_or_proof
  - does_not_execute_cleanup_correction_withdrawal_erasure_or_rollback
  - does_not_write_lifecycle_release_deployment_or_publication_state
  - does_not_approve_review_release_deployment_promotion_or_publication
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People/DNA/Land Validation Runbook

Use this runbook to select, execute, interpret, and record the current
repository-backed People/DNA/Land validation surfaces. The available procedures
operate on committed synthetic fixtures and repository metadata. They are not a
production validation service, policy engine, consent system, identity resolver,
title examiner, proof producer, release gate, or publication approval.

> [!CAUTION]
> Never place real living-person identifiers, family relationships, DNA or
> genomic material, raw kit or vendor identifiers, consent credentials,
> revocation records, addresses, person-parcel joins, exact private locations,
> disputed title material, protected cultural information, or proprietary
> source excerpts in Git, test inputs, CI logs, screenshots, or validation
> records. Stop and escalate if any such material appears.

> [!IMPORTANT]
> A passing check proves only the named synthetic profile at the tested commit.
> It does not establish identity, kinship, consent validity, rights, source
> admissibility, title, legal boundary, EvidenceBundle closure, active policy,
> operational cleanup, proof, release readiness, rollback readiness, or public
> safety.

**Quick navigation:** [Authority](#authority-and-scope) · [Status](#current-repository-status) · [Choose](#validation-profile-selection) · [Prepare](#preflight) · [Run](#execution-procedures) · [Interpret](#finite-outcomes) · [Record](#validation-record) · [Failures](#failure-and-escalation) · [CI](#hosted-ci-interpretation) · [Maintenance](#maintenance-open-verification-and-rollback)

## Authority and scope

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md). Those rules place
human procedures under `docs/runbooks/`; they keep contracts, schemas, policy,
fixtures, validators, tests, evidence, receipts, proofs, lifecycle state, and
release decisions in their owning roots. This runbook explains how to use those
surfaces. It does not become their authority.

| Concern | Owning surface | This runbook may do |
|---|---|---|
| Domain meaning and source-role limits | [`docs/domains/people-dna-land/`](../../domains/people-dna-land/README.md) and [`contracts/`](../../../contracts/domains/people-dna-land/README.md) | Route the operator to exact claims and keep object families distinct |
| Machine shape | [`schemas/contracts/v1/domains/people-dna-land/`](../../../schemas/contracts/v1/domains/people-dna-land/README.md) | Name the schema exercised by an implemented check |
| Allow, deny, restrict, or abstain policy | [`policy/domains/people-dna-land/`](../../../policy/domains/people-dna-land/README.md), [`policy/consent/people-dna-land/`](../../../policy/consent/people-dna-land/README.md), and accountable review | Preserve outcomes and holds; never activate or replace policy |
| Test inputs | [`fixtures/domains/people-dna-land/`](../../../fixtures/domains/people-dna-land/README.md) and contract fixtures | Admit only committed synthetic fixtures named by an implemented test or validator |
| Executable checks | [`tests/`](../../../tests/domains/people-dna-land/README.md), [`tools/validators/`](../../../tools/validators/domains/people-dna-land/README.md), and workflow definitions | Run exact commands, preserve expected rejection, and record limitations |
| Evidence, proof, lifecycle, release, and publication | Their owning data, proof, lifecycle, and `release/` surfaces | Stop and hand off; validation output is not authority for these transitions |

## Current repository status

This runbook is grounded in `main@c00096f904c66053938355e52f4a5cb9402be6a4`.
Re-check paths and commands if the tested revision differs.

| Surface | Current state | Bounded conclusion |
|---|---:|---|
| [Domain workflow](../../../.github/workflows/domain-people-dna-land.yml) | **Executable bounded hold gate** | Runs two synthetic consent profiles and static boundary checks; broader semantics, policy runtime, proof, and release remain held |
| Consent-overlay safety | **Executable synthetic profile** | Valid fixtures must pass; the committed invalid lane must be rejected |
| Consent-revocation propagation assessment | **Executable synthetic profile** | Replays declared outcomes across a closed seven-surface dependency set; it does not execute cleanup |
| Historical person/place/event resolution | **Executable focused synthetic suite** | Checks deterministic scoring, evidence posture, private/DNA denial, and fixture polarity; it does not establish a canonical person or public claim |
| People/DNA/Land EvidenceBundle projection | **Executable focused convergence suite** | Verifies that the domain projection delegates to the shared EvidenceBundle schema and accepts/rejects shared fixtures |
| Smoke test | **Executable but minimal** | Proves only that the domain test lane is discoverable; it is not semantic coverage |
| Other People/DNA/Land validator and test directories | **Mixed scaffold, documentation-only, or held** | File presence and README intent do not prove implementation |
| Proof-build job | **Explicit held success path** | Confirms that no accepted proof producer or deterministic proof command has surfaced; it emits no proof |
| Publication dry-run job | **Explicit held success path** | Confirms that no accepted candidate manifest contract or domain release-dry-run command has surfaced; it publishes nothing |
| Real person, genealogy, DNA, consent, vendor, parcel, title, or culturally controlled payload | **Not admitted** | Do not use this runbook; stop and escalate to an approved handling environment and accountable reviewers |

The Drive blueprint is design lineage, not current implementation evidence. Its
assertion-first model, DNA restriction, evidence-bound temporal land assertions,
living-person denial posture, and assessor/parcel anti-collapse rules are used
only where current repository contracts, schemas, fixtures, validators, tests,
or governance support the same boundary.

## Validation profile selection

Run only the profile that matches the changed surface. Running more profiles is
reasonable when a change crosses their dependencies, but a larger test set does
not expand the meaning of a pass.

| Change or question | Required focused profile | Additional check when applicable |
|---|---|---|
| Consent-overlay contract, schema, fixtures, validator, or test | [Consent-overlay safety](#profile-a-consent-overlay-safety) | Revocation propagation when consent state or downstream obligations change |
| Revocation assessment contract, schema, cases, validator, or test | [Revocation propagation](#profile-b-consent-revocation-propagation) | Consent overlay when the same change affects overlay admission |
| Historical person/place/event resolution contract, schema, fixture, validator, or test | [Historical resolution](#profile-c-historical-personplaceevent-resolution) | Domain workflow only when shared sensitive-domain boundaries also change |
| Domain EvidenceBundle projection or shared EvidenceBundle schema/fixtures | [EvidenceBundle convergence](#profile-d-evidencebundle-projection-convergence) | Shared evidence validation required by the changed shared surface |
| Domain workflow or lane-wide sensitive boundary | Profiles A and B plus the workflow's static boundary inventory | Add C or D only when their files or dependencies are affected |
| Documentation-only change | Markdown, metadata, link, and document-graph checks used by the repository | Run a domain profile only when the document changes an executable command or maturity claim |
| Real-data, policy-activation, cleanup, proof, release, deployment, or publication claim | **Do not run as authorization** | `HOLD` or `ESCALATE` to the owning authority |

## Preflight

### 1. Freeze the revision

Record the exact commit before running a command.

```bash
git rev-parse HEAD
git status --short
```

Use a clean worktree or explain every local change in the validation record. Do
not cite a branch name alone: branch heads move.

### 2. Confirm the input boundary

The selected input must be a committed synthetic fixture under a named profile.
Do not substitute local copies, downloaded vendor exports, personal records,
unreviewed examples, screenshots, production payloads, or source-derived data.

Before execution, confirm:

- the exact schema, fixture, validator, test, and workflow paths exist at the tested commit;
- the profile's positive and negative lanes are both present where the profile defines them;
- no fixture contains real identifiers or restricted values;
- no command includes a URL, credential, token, vendor account, or live source path;
- the proposed output is repository-visible and contains only paths, counts, hashes, reason codes, and minimized synthetic summaries.

### 3. Provision declared test dependencies

The domain workflows use Python 3.11 and the repository's declared test
dependency installer:

```bash
python --version
python tools/ci/install_python_ci.py project-test
```

Dependency installation may require package-network access. The validation
profiles themselves must remain fixture-only. If dependencies cannot be
provisioned from the approved environment, record `NOT_RUN` or `ERROR`; do not
silently replace the repository environment or weaken a validator.

### 4. Set deterministic, bounded execution variables

```bash
export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
```

`KFM_NO_NETWORK=1` is a declared profile signal, not proof of runner-wide
isolation. The current Python tests exercise explicit network-denial seams; they
do not establish operating-system, container, non-Python, DNS, or subprocess
egress denial. Use the [no-network runbook](./NO_NETWORK_TEST_RUNBOOK.md) for the
full limitation statement.

## Execution procedures

Run commands from the repository root. Preserve exact exit codes and do not pipe
validator output through filters that could hide a failure.

### Profile A: consent-overlay safety

This profile checks the consent-safe genealogy-overlay fixture family, including
closed schema posture, deterministic hashes, manifest membership, consent expiry
and revocation precedence, identifying-field and raw-genomic denial, public
release denial, bounded parsing, deterministic value-free diagnostics, and
explicit Python network denial.

Run the test module:

```bash
python tests/domains/people-dna-land/consent/revocation/test_consent_overlay_safety.py --verbose
```

Validate the committed positive fixtures:

```bash
python tools/validators/domains/people-dna-land/validate_consent_overlay.py \
  --revocation-manifest fixtures/domains/people-dna-land/consent_overlay/revocation_manifest.json \
  fixtures/domains/people-dna-land/consent_overlay/valid/*.json
```

The committed invalid lane must fail. Treat unexpected acceptance as a profile
failure:

```bash
if python tools/validators/domains/people-dna-land/validate_consent_overlay.py \
  --revocation-manifest fixtures/domains/people-dna-land/consent_overlay/revocation_manifest.json \
  fixtures/domains/people-dna-land/consent_overlay/invalid/*.json; then
  echo "FAIL: known-invalid consent-overlay fixtures were accepted" >&2
  exit 1
fi

echo "EXPECTED_REJECTION: invalid consent-overlay fixtures"
```

Do not interpret rejection of an invalid fixture as cleanup, revocation
execution, erasure, EvidenceBundle closure, policy activation, or public safety.

### Profile B: consent-revocation propagation

This profile replays the committed synthetic assessment cases and checks exact
outcomes, consent states, scope mismatch, deterministic hashes, safe JSON input,
and the declared `READ`, `ANSWER`, `EXPORT`, `TILE`, `GRAPH`, `INDEX`, and
`CACHE` dependency set.

```bash
python tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py --verbose

python tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py --fixtures
```

A pass confirms declared fixture agreement only. It does not discover production
dependencies, authenticate a consent or revocation record, call an executor,
invalidate a deployed carrier, verify post-action state, or establish closure.

### Profile C: historical person/place/event resolution

This focused profile validates the current schema and synthetic fixture polarity,
deterministic confidence and disposition, source-authority ordering, conflict
holds, and fail-closed private/DNA fields.

```bash
python -m pytest -q tests/validators/test_validate_historical_person_place_event_resolution.py

python tools/validators/validate_historical_person_place_event_resolution.py --fixtures
```

The fixture runner must report a valid positive and negative lane and exit zero.
Its result is a candidate-review disposition, hold, or abstention inside the
synthetic contract. It is not canonical identity, kinship proof, title evidence,
source admission, or publication authority.

### Profile D: EvidenceBundle projection convergence

This profile checks that the domain EvidenceBundle projection delegates shape to
the shared schema and preserves closed claim scope while accepting and rejecting
the shared fixtures as expected.

```bash
python -m py_compile \
  tools/validators/validate_people_dna_land_evidence_bundle_projection.py \
  tests/validators/domains/people-dna-land/test_evidence_bundle_schema_convergence.py

python -m unittest discover \
  --start-directory tests/validators/domains/people-dna-land \
  --pattern 'test_*.py' \
  --verbose

python tools/validators/validate_people_dna_land_evidence_bundle_projection.py --fixtures
```

Schema convergence is not evidence resolution. A pass does not prove that a
real EvidenceRef resolves, that sources or rights are valid, that an
EvidenceBundle is release-significant, or that review and policy gates passed.

### Optional minimal smoke test

```bash
python -m pytest -q tests/domains/people-dna-land/test_people_dna_land_smoke.py
```

Use this only as a discovery/import check. It cannot replace any focused profile.

## Finite outcomes

Assign the runbook outcome after reviewing every selected command, its exit code,
its expected-rejection behavior, and its scope.

| Outcome | Use when | Required next step |
|---|---|---|
| `PASS` | Every selected positive check passed, every required negative case was rejected, and no boundary violation occurred | Record exact SHA, commands, profiles, and limitations |
| `FAIL` | An implemented positive case failed, an invalid case was accepted, diagnostics drifted unexpectedly, or the change introduced a regression | Stop; preserve minimized diagnostics; repair or revert the bounded change |
| `NOT_RUN` | A selected command was not executed | State why and do not imply validation |
| `HOLD` | Required authority, dependency, schema, policy, evidence, source, rights, sensitivity, consent, reviewer, proof, release, or rollback support is unresolved | Route the unresolved question to its owning surface |
| `ABSTAIN` | The validator or reviewer lacks enough supported evidence to decide safely | Narrow the claim or obtain the missing evidence |
| `DENY` | A fixture or proposed use violates an explicit safety or admissibility boundary | Keep the denied object out of downstream use; do not convert denial into cleanup authority |
| `ERROR` | Tooling, parsing, environment, or execution failed without a trustworthy domain decision | Repair the environment or tool, then rerun from the same or newly recorded SHA |
| `ESCALATE` | Real sensitive material, legal/sovereignty conflict, credential exposure, harmful precision, unexpected live access, or possible public exposure appears | Stop, minimize further exposure, preserve safe audit facts, and use the accountable incident/review route |

An expected `DENY`, `ABSTAIN`, or parser `ERROR` inside a negative fixture can
contribute to an overall profile `PASS` only when the committed test declares
that exact result. Never relabel an unexpected error as an expected rejection.

## Validation record

Store the result in the pull request or approved validation surface without
copying fixture payloads. Use this template:

```markdown
### People/DNA/Land validation

- Repository: `bartytime4life/Kansas-Frontier-Matrix`
- Commit: `<full 40-character SHA>`
- Environment: `<local or workflow run; Python version>`
- Profiles: `<A, B, C, D, or smoke>`
- Commands: `<exact commands or workflow job links>`
- Positive cases: `<PASS, FAIL, NOT_RUN, or ERROR>`
- Expected negative cases: `<rejected as declared, unexpectedly accepted, or NOT_RUN>`
- Overall bounded outcome: `<PASS | FAIL | NOT_RUN | HOLD | ABSTAIN | DENY | ERROR | ESCALATE>`
- Reason codes: `<stable codes only; no protected values>`
- Changed paths: `<paths relevant to the result>`
- Limitations: `<what this result does not prove>`
- Hosted checks: `<pending, success, failure, skipped, or unavailable at exact head>`
- Accountable review: `<requested, pending, approved with evidence, or NEEDS VERIFICATION>`
```

Record branch-head evidence separately from merge-commit evidence. A green result
for a superseded head is historical; it must not be presented as the current
pull-request result.

## Failure and escalation

### Unexpected positive-case failure

1. Stop the selected profile.
2. Record the exact commit, command, exit code, failing path, and value-free reason code.
3. Confirm the failure reproduces from a clean worktree at the same commit.
4. Separate introduced failure from inherited or environment-only failure.
5. Repair the smallest owning surface or revert the bounded change.
6. Rerun the complete affected profile, including negative fixtures.

### Unexpected acceptance of an invalid fixture

Treat this as a fail-closed regression. Do not continue to proof, promotion,
release, deployment, or publication work. Preserve the fixture name and reason
code without copying sensitive-looking values, repair the validator/schema/test
boundary, and rerun all positive and negative cases in that profile.

### Sensitive or live material appears

Stop immediately. Do not echo, copy, download, inspect further, attach, or commit
the material. Preserve only the minimum safe audit facts: where it appeared, the
time, the repository revision or run identifier, exposure classification, and
the accountable escalation route. Do not use ordinary Git history rewriting as
an improvised privacy, legal, consent, or incident response.

## Hosted CI interpretation

The domain workflow contains three jobs with different meanings:

| Job | Green means | Green does not mean |
|---|---|---|
| `validate-people-dna-land` | Required boundaries were present and two bounded synthetic consent profiles completed as declared | Broader semantic coverage, real consent enforcement, EvidenceBundle closure, policy approval, proof, cleanup, release, or publication |
| `build-proof-people-dna-land` | The explicit proof hold remained intact and no accepted proof producer surfaced | Proof was built or validated |
| `publish-dry-run-people-dna-land` | The explicit release-dry-run hold remained intact and no accepted domain candidate contract surfaced | A release candidate was validated, promoted, deployed, or published |

The separate EvidenceBundle-convergence workflow runs only for its declared
schema, shared fixture, validator, test, and workflow paths. Check the exact
workflow trigger and tested head before using its result.

Classify hosted results precisely:

- `SUCCESS`: the named job completed at the exact SHA;
- `FAILURE`: inspect the failing step before attributing cause;
- `SKIPPED`: no evidence for the skipped surface;
- `PENDING` or `IN_PROGRESS`: terminal validation is not available;
- external deployment status: separate from repository validation unless the changed surface requires it.

Do not conceal inherited failures, but do not expand a focused documentation or
validator repair merely to absorb unrelated failures.

## Review checklist

- [ ] Exact commit and dirty-worktree state are recorded.
- [ ] Only committed synthetic fixtures were used.
- [ ] The selected profile matches the changed dependency surface.
- [ ] Positive and required negative lanes were both executed.
- [ ] Expected rejection was checked rather than ignored.
- [ ] No real identifier, DNA/genomic value, consent credential, private location, title material, vendor credential, or protected cultural content entered inputs or logs.
- [ ] Outcome and reason codes are finite and value-free.
- [ ] Validation output is not described as identity, kinship, consent, title, policy, evidence, proof, release, deployment, or publication authority.
- [ ] Hosted results are tied to the exact pull-request head or merge commit.
- [ ] Accountable review and all unresolved holds remain visible.

## Related procedures

- [Runbook lane boundary](./README.md)
- [No-network test limitations](./NO_NETWORK_TEST_RUNBOOK.md)
- [Living-person review](./LIVING_PERSON_REVIEW.md)
- [Consent review and revocation handoff](./CONSENT_RUNBOOK.md)
- [Revocation propagation review](./revocation.md)
- [Domain API and outcome contracts](../../domains/people-dna-land/API_CONTRACTS.md)
- [Domain definition of done](../../domains/people-dna-land/DEFINITION_OF_DONE.md)

## Maintenance, open verification, and rollback

Re-review this runbook whenever a named schema, fixture, validator, test,
workflow, dependency installer, policy binding, report shape, output location,
or sensitive-data boundary changes.

Open verification remains for:

1. accountable People/DNA/Land, privacy, consent, Indigenous/Tribal, legal, policy, source, evidence, proof, release, operations, and independent-review assignments;
2. runner-wide and non-Python network denial;
3. the authority and maturity of documentation-only or placeholder validators and test directories;
4. active policy-runtime binding and approved sensitive-data handling;
5. real EvidenceRef resolution, proof production, complete revocation/withdrawal cleanup, and post-action verification;
6. operational promotion, rollback, release, deployment, and publication controls.

To roll back this scaffold replacement before integration, close its draft pull
request and delete only the task-owned branch. After separately authorized
integration, revert the focused documentation commit or restore prior blob
`9ac1079ed880d3c94d52aabe083541987a9afc39` through reviewed history. Restoring
the scaffold would remove this procedure; it would not undo a validation run,
alter policy, revoke consent, delete data, invalidate a cache, withdraw a
release, roll back a deployment, or change published state.

[Back to top](#top)
