<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-people-dna-land-no-network-test
title: People/DNA/Land No-Network Test Runbook
type: runbook
version: v1.0.3
prior_version: v1.0.2
prior_state: repository-grounded procedure whose exact-revision snapshot mixed current and old-base evidence blobs
status: DRAFT_REPOSITORY_GROUNDED; TWO_BOUNDED_SYNTHETIC_PYTHON_PROFILES_EXECUTABLE; RUNNER_WIDE_AND_NON_PYTHON_EGRESS_DENIAL_HELD; BROADER_PEOPLE_DNA_LAND_AUTHORITY_HELD
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable People/DNA/Land, privacy, consent, Indigenous/Tribal, legal, policy, source, evidence, proof, release, operations, and independent-review assignments"
created: 2026-05-12
updated: 2026-08-30
policy_label: repository-facing; sensitive-domain; validation-sensitive; fail-closed; non-release; non-publication
current_path: docs/runbooks/people-dna-land/NO_NETWORK_TEST_RUNBOOK.md
owning_root: docs/
responsibility: Human procedure for reproducing and interpreting the People/DNA/Land lane's two current deterministic synthetic fixture profiles without claiming runner-wide isolation, real-person or DNA authority, operational consent or revocation, evidence closure, policy approval, proof, release, deployment, or publication.
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, source and evidence authority, executable validators and tests, workflow definitions, policy, accountable review, lifecycle, proof, release, correction, revocation, withdrawal, rollback, and sovereignty-aware stewardship
current_disposition: TWO_BOUNDED_SYNTHETIC_PYTHON_PROFILES_AVAILABLE / RUNNER_WIDE_NON_PYTHON_EGRESS_AND_BROADER_TRUST_SPINE_HELD
reason_codes:
  - PDL_NO_NETWORK_EXACT_SHA_REQUIRED
  - PDL_NO_NETWORK_PROCESS_PATCHES_ONLY
  - PDL_NO_NETWORK_RUNNER_EGRESS_NEEDS_VERIFICATION
  - PDL_NO_NETWORK_SYNTHETIC_FIXTURES_ONLY
  - PDL_NO_NETWORK_REAL_CONSENT_REVOCATION_AND_CLEANUP_HELD
  - PDL_NO_NETWORK_EVIDENCE_POLICY_PROOF_RELEASE_AND_PUBLICATION_HELD
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 31f5ade589b9f20d87a59ce83be228e577f51cca
  target_prior_blob: 7e364eed087db970057fc8ca86d6afc253650ba2
  lane_readme_prior_blob: 6e1c464aa1d51d55b4683702471ec2b18e515d54
  domain_workflow_blob: bcf64c3e3b6653b9543489fc5a6031805ae3ef48
  consent_overlay_test_blob: c071e54d53e06871b537b8adc20e522d05f4ef31
  revocation_assessment_test_blob: bceeef36e5c4e456e6f8a3fc192cd1c349d34fb5
  consent_overlay_validator_blob: 22ae36a38ff782229f024d9a7a370f21b4a15aef
  revocation_assessment_validator_blob: 76c7805428f253a7a711c7bc68a27e9cbcce40e7
  consent_overlay_fixture_tree: 67720650ddab72b675818278cdf998418eb287bf
  revocation_assessment_fixture_tree: ee9e1cfc9873779bb9d56a8c8d17eaf5ce4a0fb2
  revocation_assessment_schema_blob: e976211d1bf536b2aae7901842474dbcb1c3a484
  test_lane_readme_blob: 8054ad137c0d74fb27f3f44920acec153344c00d
  policy_readme_blob: 7260394c77d79629895da16d8d680e8d80c56b32
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
related:
  - docs/runbooks/people-dna-land/README.md
  - docs/runbooks/people-dna-land/LIVING_PERSON_REVIEW.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/domains/people-dna-land/README.md
  - .github/workflows/domain-people-dna-land.yml
  - .github/workflows/consent-revocation-propagation.yml
  - tests/domains/people-dna-land/consent/revocation/README.md
  - tests/domains/people-dna-land/consent/revocation/test_consent_overlay_safety.py
  - tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py
  - tools/validators/domains/people-dna-land/validate_consent_overlay.py
  - tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py
  - fixtures/domains/people-dna-land/consent_overlay/README.md
  - fixtures/domains/people-dna-land/consent_revocation_propagation/README.md
  - policy/domains/people-dna-land/README.md
  - data/registry/sources/people-dna-land/README.md
  - data/proofs/people-dna-land/README.md
  - release/candidates/people-dna-land/README.md
non_effects:
  - does_not_contact_live_sources
  - does_not_establish_runner_wide_or_non_python_egress_denial
  - does_not_admit_real_people_dna_consent_land_title_or_cultural_material
  - does_not_issue_or_validate_real_consent
  - does_not_execute_revocation_withdrawal_deletion_or_derivative_invalidation
  - does_not_activate_sources_or_policy
  - does_not_write_lifecycle_or_publication_state
  - does_not_resolve_real_evidence_refs_or_create_evidence_or_proof
  - does_not_approve_review_release_deployment_or_publication
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People/DNA/Land No-Network Test Runbook

Repository-grounded procedure for reproducing and interpreting the
People/DNA/Land lane's two current deterministic synthetic fixture profiles at
an exact repository revision. The executable evidence is narrower than a
runner-wide network sandbox: one test module patches five Python networking
entry points for every test, while the other patches socket construction and
connection creation during its deterministic replay test. The standalone
validators read local files and do not themselves establish an egress control.

> [!CAUTION]
> Never substitute real living-person identifiers, family relationships, DNA or
> genomic material, kit or vendor identifiers, consent or revocation records,
> private addresses, parcel-owner joins, exact private locations, disputed
> title material, or culturally restricted information for these fixtures.

> [!IMPORTANT]
> A green result proves only the named code and frozen synthetic fixtures at the
> tested SHA. It does not establish identity, kinship, consent validity, rights,
> title, legal boundary, sovereignty or stewardship approval, operational
> revocation, deletion, derivative or cache invalidation, EvidenceBundle
> closure, policy approval, proof, release, deployment, or publication.

**Navigation:** [Boundary](#1-boundary-and-authority) · [Evidence](#2-current-executable-evidence) · [Preflight](#3-preflight) · [Commands](#4-exact-bounded-procedure) · [Interpretation](#5-interpretation-and-failure-classification) · [Record](#6-minimum-result-record) · [Maintenance](#7-maintenance-lineage-and-rollback)

## 1. Boundary and authority

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md), which place
human operational procedures under `docs/runbooks/`. Enforceability proof stays
under `tests/`; object shape stays under `schemas/`; decisions stay under
`policy/`; source, evidence, proof, lifecycle, and release authorities retain
their own responsibility roots.

This file explains current executable evidence. It creates no contract, schema,
policy, source admission, evidence object, proof, consent record, revocation
receipt, release decision, rollback object, deployment, or publication state.

### In scope

- The exact commands in the current `domain-people-dna-land` workflow for the
  consent-overlay and consent-revocation propagation fixture profiles.
- Frozen, synthetic, public-safe, repository-local fixtures only.
- Positive, expected-negative, deterministic replay, and bounded Python-process
  network-denial behavior implemented by the named tests.
- Exact-SHA result identity and truthful failure attribution.

### Out of scope

- Live genealogy, DNA, people-search, identity, consent, assessor, deed, title,
  parcel, mapping, storage, model, or other remote systems.
- Credentials, package retrieval, source activation, source admission, or live
  data refresh.
- Runner, container, namespace, firewall, operating-system, dependency-install,
  or non-Python egress proof.
- Real consent issuance or validation, revocation or withdrawal execution,
  cleanup, deletion, derivative invalidation, cache invalidation, or rollback.
- Writes to `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`, `TRIPLET`, or
  `PUBLISHED`.
- Identity, kinship, DNA relationship, title, boundary, ownership, cultural
  authority, current-truth, evidence, policy, proof, release, or public-use
  determinations.

[Back to top](#top)

## 2. Current executable evidence

The current [domain workflow](../../../.github/workflows/domain-people-dna-land.yml)
sets `KFM_NO_NETWORK=1`, `PYTHONDONTWRITEBYTECODE=1`, and `PYTHONHASHSEED=0` for
the two bounded steps. `KFM_NO_NETWORK=1` is a declaration consumed as test
context; it is not, by itself, a firewall or shared startup guard.

| Profile | Current evidence | Bounded conclusion | Not established |
|---|---|---|---|
| Consent-safe genealogy overlay | `test_consent_overlay_safety.py` runs 17 tests; its per-test setup patches `socket.connect`, `connect_ex`, `create_connection`, `getaddrinfo`, and `urllib.request.urlopen`. The validator accepts two valid fixtures and the workflow requires all 13 known-invalid fixtures to be rejected against the frozen revocation manifest. | Local shape, consent/expiry/revocation precedence, fixture refs, coarse synthetic place/time, deterministic hashes, identifying-field and raw-genomic denial, and non-release posture for this profile. | Runner-wide isolation, real identity or kinship, real consent, evidence resolution, policy enforcement, public-safe transformation, release, or publication. |
| Consent-revocation propagation assessment | `test_consent_revocation_propagation_assessment.py` runs nine tests; its replay test patches socket construction and connection creation. The validator evaluates 17 frozen cases spanning `PASS`, `DENY`, and `ERROR` expectations over seven declared downstream surfaces. | Deterministic assessment of declared scope and declared propagation receipt posture for synthetic cases. | Receipt authenticity, real revocation, cleanup, withdrawal, derivative or cache invalidation, rollback execution, evidence or policy authority, release, or publication. |
| Workflow inventory and hold jobs | The workflow allows only the two named test modules, two named validators, and two fixture roots as substantive validation surfaces; proof and release jobs remain explicit holds. | New substantive files cannot silently become accepted validation, proof, or release authority. | Complete domain coverage, policy runtime, proof production, release dry-run, deployment, or human approval. |

The dedicated
[`consent-revocation-propagation`](../../../.github/workflows/consent-revocation-propagation.yml)
workflow also runs the second profile and checks its authoring receipt. That
additional workflow remains fixture proof, not operational revocation or release
authority.

### What no-network means here

- The accepted inputs are repository-local JSON and schema files.
- The test modules exercise the named Python denial seams above.
- The commands require no intended remote service and must not be modified to
  fetch dependencies or payloads during this procedure.
- An unexpected network attempt is a failure and produces `HOLD`, even if some
  assertions passed.

It does **not** mean that every Python API, subprocess, non-Python process, CI
runner, or operating-system path is isolated. Do not describe this result as an
air gap, sandbox, firewall proof, or complete egress denial.

[Back to top](#top)

## 3. Preflight

1. Pin the exact revision and confirm the working tree state:

   ```bash
   git rev-parse HEAD
   git status --short
   ```

2. Confirm the named tests, validators, fixtures, schema, and workflow still
   exist at that revision. If a path moved or a command changed, stop and
   reconcile this runbook from repository evidence before running it.
3. Inspect the fixture diff. Stop if it contains or may reconstruct any real
   person, family, DNA, consent, revocation, private-land, precise-location,
   title, or protected cultural material.
4. Use the repository's existing environment. Do not install dependencies,
   contact a provider, copy production data, or insert credentials to make the
   procedure pass.
5. Record unresolved rights, consent, living-person, sensitivity, sovereignty,
   stewardship, or precision questions as `HOLD` or `ESCALATE`; a synthetic test
   cannot resolve them.

[Back to top](#top)

## 4. Exact bounded procedure

Run from the repository root at the pinned revision:

```bash
export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0

python tests/domains/people-dna-land/consent/revocation/test_consent_overlay_safety.py --verbose

python tools/validators/domains/people-dna-land/validate_consent_overlay.py \
  --revocation-manifest fixtures/domains/people-dna-land/consent_overlay/revocation_manifest.json \
  fixtures/domains/people-dna-land/consent_overlay/valid/*.json

if python tools/validators/domains/people-dna-land/validate_consent_overlay.py \
  --revocation-manifest fixtures/domains/people-dna-land/consent_overlay/revocation_manifest.json \
  fixtures/domains/people-dna-land/consent_overlay/invalid/*.json; then
  echo "ERROR: known-invalid consent-overlay fixtures were accepted" >&2
  exit 1
fi

echo "EXPECTED_REJECTION: invalid consent-overlay fixtures"

python tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py --verbose
python tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py --fixtures
```

The invalid consent-overlay invocation returning nonzero is the expected
negative polarity. Treating that return as a suite failure, or allowing it to
return zero, misstates the profile.

Do not extend this command block with live connectors, network checks, package
downloads, policy activation, proof generation, lifecycle writes, release
commands, deployment, or publication.

[Back to top](#top)

## 5. Interpretation and failure classification

| Result | Required observation | Meaning and next action |
|---|---|---|
| `PASS` | Both test modules pass; valid overlay fixtures are accepted; the complete invalid overlay set is rejected; all 17 propagation cases match their declared expectations; no named network denial seam is invoked. | Record bounded synthetic success at the exact SHA. Preserve every broader hold. |
| `HOLD` | Sensitive or non-synthetic fixture content, unexpected network attempt, missing dependency, path drift, unreviewed profile expansion, unclear rights/consent/stewardship, or an assertion that exceeds the bounded profile. | Stop. Minimize the record and route to the accountable owner without copying sensitive values. |
| `ERROR` | Test, validator, schema, fixture parsing, environment, or command execution fails unexpectedly. | Record exact command and safe diagnostic. Do not reinterpret failure as a policy or domain decision. |
| `ESCALATE` | Real-person, DNA, consent, sovereignty, cultural, title, private-land, or harmful-precision review is required. | Leave repository-visible material minimized and obtain accountable review in an approved handling environment. |

Within the synthetic propagation manifest, `PASS`, `DENY`, and `ERROR` are
fixture expectations evaluated by the validator. A validator-level `PASS` does
not authorize the underlying real-world operation and does not authenticate a
receipt.

### Negative cases that must stay negative

- expired, revoked, missing, or mismatched consent and revocation posture;
- raw genomic or identifying kit fields;
- identifying person or parcel-like fields and precise location;
- unsupported high-confidence summaries and missing fixture evidence refs;
- public-release claims or promotion eligibility;
- incomplete seven-surface propagation, missing declared receipts, scope
  mismatch, temporal inconsistency, hash tampering, schema-invalid authority
  claims, and unknown fields.

[Back to top](#top)

## 6. Minimum result record

Record only repository-safe metadata:

```text
revision: <40-character commit SHA>
profile: people-dna-land-bounded-synthetic-no-network
consent_overlay_tests: PASS | FAIL | NOT_RUN
consent_overlay_valid_validator: PASS | FAIL | NOT_RUN
consent_overlay_invalid_polarity: EXPECTED_REJECTION | UNEXPECTED_ACCEPTANCE | NOT_RUN
revocation_propagation_tests: PASS | FAIL | NOT_RUN
revocation_propagation_fixture_validation: PASS | FAIL | NOT_RUN
network_posture: NAMED_PYTHON_DENIAL_SEAMS_NOT_INVOKED | ATTEMPT_DETECTED | UNKNOWN
overall: PASS | HOLD | ERROR | ESCALATE
broader_policy_evidence_proof_release_publication: HOLD
```

Do not paste fixture payloads, sensitive values, credentials, private paths, or
unminimized diagnostics into a pull request, issue, workflow summary, or public
artifact.

[Back to top](#top)

## 7. Maintenance, lineage, and rollback

The May 2026 version proposed a full trust-spine pyramid, placeholder fixture
families, policy files, public-client checks, and runner-wide isolation before
the repository was verified. That proposal remains available in Git history;
it is not current executable authority. This revision supersedes its commands
and maturity claims with the two tracked profiles only.

Re-review this runbook whenever the accepted test, validator, fixture, schema,
workflow, network guard, policy binding, proof, or release inventory changes.
Expansion requires its own dependency-closed implementation and review; prose
must not make a new object family or trust-spine layer executable by implication.

Reverting this documentation restores only the prior text. It does not undo a
test run, revoke consent, delete or invalidate derivatives, roll back data,
withdraw a release, invalidate caches, alter policy, or change publication
state. Any operational correction, withdrawal, revocation, cleanup, or rollback
must use its separately authorized surface and evidence.

[Back to top](#top)
