<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/soil/no-network-test-runbook
title: Soil No-Network Test Runbook
type: runbook
version: v2.0
prior_version: v1
prior_state: proposal-heavy planning document with unverified commands, fixture paths, receipt paths, and runner-wide isolation claims
status: DRAFT_REPOSITORY_GROUNDED; FOUR_BOUNDED_SYNTHETIC_NO_NETWORK_SUITES_EXECUTABLE; RUNNER_WIDE_AND_NON_PYTHON_EGRESS_DENIAL_HELD; SOIL_TRUTH_PROOF_RELEASE_AND_PUBLICATION_HELD
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Soil, source, scientific, evidence, QA, policy, release, and independent-review assignments"
created: 2026-05-12
updated: 2026-08-29
policy_label: repository-facing; validation-sensitive; synthetic-fixtures; no-network; potentially sensitive land and station context; fail-closed
current_path: docs/runbooks/soil/NO_NETWORK_TEST_RUNBOOK.md
owning_root: docs/
responsibility: Human procedure for reproducing and interpreting the Soil lane's current bounded fixture-only no-network checks without claiming runner-wide isolation, live-source truth, evidence closure, policy approval, proof, promotion, release, deployment, or publication.
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, source and evidence authority, executable validators and tests, workflow definitions, policy, review, lifecycle, proof, release, correction, rollback, and qualified official authorities
current_disposition: BOUNDED_TEST_LEVEL_PYTHON_NETWORK_GUARDS_AVAILABLE / RUNNER_WIDE_NON_PYTHON_EGRESS_AND_BROADER_TRUST_SPINE_HELD
reason_codes:
  - SOIL_NO_NETWORK_EXACT_SHA_REQUIRED
  - SOIL_NO_NETWORK_TEST_LEVEL_PYTHON_GUARDS_ONLY
  - SOIL_NO_NETWORK_RUNNER_EGRESS_NEEDS_VERIFICATION
  - SOIL_NO_NETWORK_SYNTHETIC_FIXTURES_ONLY
  - SOIL_NO_NETWORK_LIVE_SOURCE_AND_LIFECYCLE_HELD
  - SOIL_NO_NETWORK_PROOF_RELEASE_AND_PUBLICATION_HELD
  - SOIL_NO_NETWORK_CONSEQUENTIAL_USE_DENIED
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: a0fcc311577512b23c9ed69ed32a72132f06a773
  target_prior_blob: d42e18386911dcc008a9045c38e052ce673bfda4
  lane_readme_blob: d50303c8f4edc6a9427d61135ba2048b0ba01a03
  domain_workflow_blob: e009e00d5743d907461289c1c6571cab69ea2672
  soil_smoke_test_blob: 348e00757d198ec77cc9af0cc75355807ccfb123
  soil_moisture_test_blob: 9388fbcca647b4d5daf32dc62a05b8aba5ae136e
  smap_l4_test_blob: eaabd01221e8fde8ad1d6a280d8d82c2490dd40c
  ssurgo_test_readme_blob: 59267164c947b3789ffc6c37944dd4fc06a64f59
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
related:
  - README.md
  - ../../domains/soil/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/domain-soil.yml
  - ../../../tests/domains/soil/README.md
  - ../../../tests/domains/soil/test_soil_smoke.py
  - ../../../tests/domains/soil/test_soil_moisture_qc.py
  - ../../../tests/domains/soil/test_smap_l4_anti_collapse.py
  - ../../../tests/ingest/ssurgo_watch/README.md
  - ../../../tests/ingest/ssurgo_watch/test_ssurgo_watch.py
  - ../../../tools/validators/domains/soil/README.md
  - ../../../fixtures/domains/soil/README.md
  - ../../../data/registry/sources/soil/README.md
  - ../../../data/proofs/soil/README.md
  - ../../../release/candidates/soil/README.md
non_effects:
  - does_not_contact_live_sources
  - does_not_establish_runner_wide_egress_denial
  - does_not_establish_non_python_egress_denial
  - does_not_read_credentials
  - does_not_activate_or_admit_sources
  - does_not_write_raw_work_quarantine_processed_catalog_triplet_or_published_state
  - does_not_resolve_real_evidence_refs
  - does_not_create_evidence_receipts_or_proofs
  - does_not_approve_policy_review_promotion_or_release
  - does_not_deploy_or_publish
  - does_not_authorize_agronomic_engineering_regulatory_or_other_consequential_use
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil No-Network Test Runbook

Repository-grounded procedure for reproducing and interpreting the Soil lane's
current deterministic, fixture-only checks at an exact repository revision.
The accepted command surface contains three bounded Soil validator suites and
one fixture-only SSURGO package-drift comparator.

> [!IMPORTANT]
> `KFM_NO_NETWORK=1` records the intended posture but does not, by itself, block
> traffic. The current suites install targeted Python test-level guards around
> named socket, DNS, and `urllib` paths. They do **not** prove operating-system,
> container, namespace, job-wide, non-Python, dependency-install, or arbitrary
> untested network isolation.

> [!CAUTION]
> These checks are not soil-survey authority and must not be used for agronomic,
> engineering, conservation-compliance, land-value, regulatory, emergency, or
> other consequential determinations. Use the responsible official source and
> qualified professional for those decisions.

**Quick navigation:** [Scope](#1-purpose-authority-and-scope) ·
[Current evidence](#2-current-executable-evidence) ·
[Preflight](#3-preflight) · [Run](#4-execution-procedure) ·
[Interpret](#5-expected-results-and-interpretation) ·
[Failures](#6-failure-classification-and-stop-conditions) ·
[Record](#7-result-record) · [CI](#8-ci-binding-and-held-jobs) ·
[Safety](#9-rights-sensitivity-and-scientific-boundaries) ·
[Maintenance](#10-maintenance-and-documentation-rollback)

## 1. Purpose, authority, and scope

Use this runbook to answer four bounded questions:

1. Did the three named Soil validator suites and the SSURGO comparator execute
   at the exact revision under review?
2. Did valid and expected-invalid fixtures preserve their recorded polarity?
3. Did the tests' named Python network guards remain unused or reject attempted
   access as designed?
4. Which broader claims remain held even when every command is green?

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
and the adopted [Directory Rules](../../doctrine/directory-rules.md) place human
procedures under `docs/runbooks/`. Executable checks remain under `tests/` and
`tools/validators/`; fixtures under `fixtures/`; semantic meaning under
`contracts/`; machine shape under `schemas/`; policy under `policy/`; source
identity and admission under governed source surfaces; evidence, receipts, and
proofs under their owning data roots; and release decisions under `release/`.

This runbook explains current executable evidence. It does not create or amend a
contract, schema, SourceDescriptor, source-admission decision, validator,
policy, EvidenceBundle, receipt, ProofPack, PromotionDecision, ReleaseManifest,
CorrectionNotice, rollback object, deployment, or publication state.

### In scope

- The four commands currently invoked by `.github/workflows/domain-soil.yml`.
- Synthetic public-safe fixtures and exact expected-error sidecars named by the
  current tests.
- Test-level Python guards for the socket, DNS, and `urllib` call paths each
  suite explicitly patches or replaces.
- Deterministic finding order, bounded parsers, fixture inventory closure,
  valid/invalid polarity, non-echoing CLI behavior, and exit-code contracts.
- Exact-SHA result identity and truthful classification of skipped or held jobs.

### Out of scope

- Live NRCS SSURGO or Soil Data Access requests, Kansas Mesonet, SCAN/AWDB,
  USCRN, SMAP, SoilGrids, map services, object stores, or any other remote
  source.
- Credentials, source activation, source admission, rights acceptance, or
  endpoint authorization.
- Runner-wide firewall, namespace, container, operating-system, or non-Python
  egress proof.
- Writes to `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`, `TRIPLET`,
  receipt, proof, release, or `PUBLISHED` stores.
- Soil truth, live-source currentness, real EvidenceRef resolution,
  EvidenceBundle closure, policy approval, proof production, promotion,
  rollback execution, release, deployment, or publication.

[Back to top](#top)

## 2. Current executable evidence

The current [Soil workflow](../../../.github/workflows/domain-soil.yml) uses
Python 3.11 and runs the following bounded surfaces without installing project
dependencies in the job.

| Surface | Local inputs and enforcement | Bounded conclusion | Not established |
|---|---|---|---|
| [`test_soil_smoke.py`](../../../tests/domains/soil/test_soil_smoke.py) | `fixtures/domains/soil/valid/` and `invalid/`; exact expected-error sidecars; patches `socket.connect`, `connect_ex`, `create_connection`, `getaddrinfo`, and `urllib.request.urlopen` | Public-safe fixture shape, closed fields, support-type profile, location-field denial, parser bounds, deterministic findings, non-echoing output, and exit codes for this frozen profile | Soil object-family schemas, live source admission, scientific validity, evidence closure, policy, proof, or release |
| [`test_soil_moisture_qc.py`](../../../tests/domains/soil/test_soil_moisture_qc.py) | `fixtures/domains/soil/soil_moisture/{valid,invalid}/`; exact sidecars; patches the same named socket, DNS, and URL-open paths | Synthetic station-series identity, depth, measurement bounds, canonical UTC, source timezone, QC/deduplication, public-safe spatial support, deterministic findings, and CLI polarity | Live station identity, freshness, sensor calibration, scientific fitness, source rights, policy, proof, or release |
| [`test_smap_l4_anti_collapse.py`](../../../tests/domains/soil/test_smap_l4_anti_collapse.py) | `fixtures/domains/soil/soil_moisture/smap_l4/{valid,invalid}/`; exact sidecars; replaces `socket.socket` and `urllib.request.urlopen` in its no-network assertion | Frozen synthetic SMAP L4 surface/root-zone profile, NRT/standard-quality distinction, model/grid/station/field anti-collapse, temporal order, uncertainty, parser bounds, governance hold, and CLI polarity | Live SMAP retrieval or product identity, production cadence, model fitness, ground truth, source admission, policy, proof, or release |
| [`test_ssurgo_watch.py`](../../../tests/ingest/ssurgo_watch/test_ssurgo_watch.py) | Test-local synthetic prior/current sidecars and optional spatial diffs; patches `socket.create_connection`, `getaddrinfo`, and `urllib.request.urlopen` | Deterministic fixture-only comparison of package, schema, table, constraint, geometry, chronology, profile, and materiality drift with review-only finite outcomes | Live package retrieval, current NRCS metadata, SSURGO rights, actual survey-area geometry, canonical thresholds, source admission, Soil truth, evidence, promotion, or publication |

### 2.1 Frozen fixture inventory

The three domain suites close their direct JSON inventory so new fixture files
cannot silently enter the accepted profile.

| Suite | Valid fixtures | Expected-invalid fixtures |
|---|---:|---:|
| Public-safe Soil smoke | 1 | 8 |
| Station soil-moisture QC | 2 | 6 |
| SMAP L4 anti-collapse | 2 | 8 |

Each expected-invalid JSON fixture has a matching `.expected_error.txt` sidecar,
and the tests require exact, sorted findings. The SSURGO lane separately defines
11 synthetic prior/current comparison cases in its
[test boundary](../../../tests/ingest/ssurgo_watch/README.md).

### 2.2 What the current no-network claim means

The current evidence is **test-level Python-process denial for named APIs**, not
a general sandbox:

- the public-safe and station suites patch socket connect, connection creation,
  DNS resolution, and `urllib` URL opening;
- the SMAP suite asserts that its validator does not construct a socket or open
  a URL during the selected validation call;
- the SSURGO suite patches connection creation, DNS resolution, and URL opening;
- each suite contains an assertion that validation does not use its installed
  network mocks or that an attempted route is denied.

Do not add `curl` or another real endpoint probe and call that stronger proof.
Such a probe intentionally attempts egress, is not part of the active Soil
workflow, and still would not establish that every process or protocol is
blocked. Runner-wide isolation requires a separately reviewed operating-system,
container, namespace, firewall, or equivalent control plus negative probes for
all relevant runtimes.

[Back to top](#top)

## 3. Preflight

Run from a clean checkout at the exact branch-head or commit SHA being assessed.

1. Record the repository, full `HEAD` SHA, base SHA, merge base, changed paths,
   and whether the checkout is a branch head or a generated pull-request merge
   ref.
2. Confirm the revision:

   ```bash
   git rev-parse --verify HEAD
   git status --short
   ```

   Stop if the working tree contains unrelated changes or the recorded SHA does
   not match the intended review target.
3. Use Python 3.11 to match the active workflow. Do not load a local `.env`,
   source credentials, or endpoint configuration.
4. Set the workflow's current deterministic posture:

   ```bash
   export KFM_NO_NETWORK=1
   export PYTHONDONTWRITEBYTECODE=1
   export PYTHONUNBUFFERED=1
   export TZ=UTC
   ```

5. Confirm the following paths exist at the recorded SHA:

   ```text
   .github/workflows/domain-soil.yml
   tests/domains/soil/test_soil_smoke.py
   tests/domains/soil/test_soil_moisture_qc.py
   tests/domains/soil/test_smap_l4_anti_collapse.py
   tests/ingest/ssurgo_watch/test_ssurgo_watch.py
   tools/validators/domains/soil/validate_public_safe_fixture.py
   tools/validators/domains/soil/moisture/validate_soil_moisture.py
   tools/validators/domains/soil/moisture/validate_smap_l4_fixture.py
   tools/ingest/ssurgo_watch/ssurgo_watch.py
   fixtures/domains/soil/
   tests/ingest/ssurgo_watch/fixtures/
   ```

6. Inspect the active workflow before copying commands from this runbook. Stop
   if the workflow inventory, Python version, fixture roots, validator paths,
   or hold semantics differ. The workflow is current implementation evidence;
   this prose must be corrected when it drifts.

> [!NOTE]
> The current `domain-soil` workflow installs no project dependencies before
> these commands. A future dependency-install step would be a separate network
> and supply-chain boundary and must not be silently included in a claim that
> the whole job was no-network.

[Back to top](#top)

## 4. Execution procedure

### 4.1 Run the current bounded Soil suites

Run the exact commands from the repository root:

```bash
set -euo pipefail

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/soil/test_soil_smoke.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/soil/test_soil_moisture_qc.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/soil/test_smap_l4_anti_collapse.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest tests.ingest.ssurgo_watch.test_ssurgo_watch --verbose
```

Expected process result: every command exits `0`. A green command means its
frozen local positive and expected-negative cases behaved as encoded. It does
not mean every embedded candidate outcome is an approval; expected denial,
abstention, stale, geometry-drift, error, and review-routing cases can be part
of a passing test suite.

### 4.2 Reproduce only one lane when diagnosing

Use the individual command for the failing lane. Do not replace the full
four-command result with a narrower rerun in the final record. After repair,
rerun all four commands at the same branch head.

### 4.3 Compare with hosted execution

Opening or updating a pull request triggers `domain-soil`. Record the workflow
run URL, attempt number, event type, tested SHA, and each job conclusion.
Distinguish a pull-request merge result from the source branch head. A hosted
run against a generated merge ref is useful integration evidence but is not an
exact-head result unless the reported SHA matches the branch head.

[Back to top](#top)

## 5. Expected results and interpretation

### 5.1 Domain-suite polarity

| Condition | Expected behavior |
|---|---|
| Named valid fixture | Validator returns no findings; test remains green |
| Named expected-invalid fixture | Exact sorted findings match its sidecar; test remains green |
| Missing, extra, or renamed direct fixture | Closed-inventory assertion fails |
| Duplicate key, non-finite number, oversized or structurally unbounded input | Parser rejects the input with the profile's bounded finding |
| Candidate value placed in a failing input | CLI output must not echo the candidate value |
| Validator called with valid/invalid/no input | Current CLI contracts exercise exit codes `0`, `1`, and `2` where the suite defines them |
| Named network mock is used unexpectedly | Test fails or the installed denial raises |

### 5.2 SSURGO comparator outcomes

The SSURGO tests can remain green while confirming these embedded outcomes:

| Outcome | Meaning inside the fixture-only comparator | Promotion/publication effect |
|---|---|---|
| `NO_MATERIAL_CHANGE` | The frozen profile found no review-triggering drift, including its strict threshold cases | None |
| `PROPOSED_WORK_RECORD` | Synthetic schema, table, constraint, or material spatial-label drift requires review-only work | No promotion or publication |
| `GEOMETRY_DRIFT` | Geometry fingerprint changed and materiality math is not treated as sufficient | Review required; no promotion |
| `STALE_INPUT` | Synthetic publication chronology regressed | Blocked from progression |
| `ABSTAIN` | Materiality, extraction, or geometry profile drift prevents a comparable decision | No progression |
| `ERROR` | Derived state changed without the supporting source/profile change or another invalid state occurred | Blocking failure state |

These are comparator results, not KFM-wide policy decisions, SourceDescriptor
admission states, ProofPacks, or release decisions.

### 5.3 What a green four-command run proves

**CONFIRMED at the tested SHA:** the four frozen synthetic profiles, local
validators/helpers, exact fixture inventories, expected-negative polarity,
selected Python network guards, deterministic findings, and encoded CLI or
comparator behavior executed successfully.

**Still held or unknown:** live source access and rights, actual SSURGO or soil
moisture currentness, scientific representativeness, MUKEY/COKEY/CHKEY closure
outside the tested profile, canonical cross-repository support vocabulary,
EvidenceRef-to-EvidenceBundle resolution, policy evaluation, proof production,
promotion, correction/withdrawal execution, release, deployment, publication,
and safe consequential use.

[Back to top](#top)

## 6. Failure classification and stop conditions

| Observation | Classification | Required response |
|---|---|---|
| A command exits nonzero | `FAIL` | Preserve output, isolate the changed lane, and do not report a passing Soil validation result |
| A valid fixture is rejected | `FAIL` | Verify fixture and validator changed together intentionally; do not weaken a guard merely to restore green |
| An expected-invalid fixture is accepted | `DENY` / blocking `FAIL` | Stop the pull request; repair the fail-closed path before delivery beyond draft |
| Expected-error sidecar differs | `FAIL` | Determine whether behavior or expectation changed; update both only with evidence and review |
| Fixture inventory changed without workflow/test review | `HOLD` | Reconcile the new file's authority, sensitivity, support type, and expected polarity |
| A named network mock records use or raises | `FAIL` | Remove the attempted access or redesign the test around local data; do not whitelist a live endpoint |
| A live URL, credential, source payload, or lifecycle write enters the test path | `DENY` | Remove it from this lane and route it through governed source/lifecycle controls |
| Hosted job tests a different SHA than recorded | `ERROR` | Re-run or relabel the evidence accurately; do not call it exact-head proof |
| `build-proof-soil` remains an explicit hold | `HOLD` | Report the hold exactly; do not describe it as proof generation |
| `publish-dry-run-soil` remains an explicit hold | `HOLD` | Report the hold exactly; do not describe it as release readiness |
| A proof or release implementation appears while the hold job still says none exists | `HOLD` / workflow repair required | Stop and replace the stale hold through a separately reviewed wiring change |
| Rights, precision, source role, support type, scientific fitness, or intended use is unresolved | `ABSTAIN`, `DENY`, or `ESCALATE` | Preserve the narrower result and route to the accountable authority |

Do not repair unrelated inherited failures inside a documentation-only change.
Classify them separately and preserve the exact changed-area result.

[Back to top](#top)

## 7. Result record

Store the run result in the pull-request handoff, review record, or other
accepted coordination surface. This example is a human-readable record, not a
receipt or proof object:

```yaml
soil_no_network_result:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_sha: "<full base SHA>"
  head_sha: "<full branch-head SHA>"
  tested_sha: "<full SHA actually executed>"
  checkout_kind: "branch-head | pull-request-merge-ref"
  python: "3.11.x"
  commands:
    soil_smoke: "PASS | FAIL | NOT_RUN"
    soil_moisture_qc: "PASS | FAIL | NOT_RUN"
    smap_l4_anti_collapse: "PASS | FAIL | NOT_RUN"
    ssurgo_watch: "PASS | FAIL | NOT_RUN"
  network_claim: "targeted test-level Python guards only"
  hosted_workflow:
    url: "<workflow run URL or null>"
    attempt: "<integer or null>"
    validate_soil: "PASS | FAIL | PENDING | NOT_RUN"
    build_proof_soil: "HOLD | FAIL | PENDING | NOT_RUN"
    publish_dry_run_soil: "HOLD | FAIL | PENDING | NOT_RUN"
  changed_paths:
    - "<path>"
  conclusion: "PASS | FAIL | HOLD | ERROR"
  limitations:
    - "no runner-wide or non-Python egress proof"
    - "synthetic fixtures only"
    - "no source admission, evidence closure, policy, proof, promotion, release, or publication effect"
  recorded_by: "<reviewer or operator>"
  recorded_at: "<UTC timestamp>"
```

Do not derive identity from `recorded_at`; the timestamp records observation
only. Keep full SHAs, exact commands, and workflow attempt numbers so another
reviewer can reconstruct the claim.

[Back to top](#top)

## 8. CI binding and held jobs

The current [`domain-soil` workflow](../../../.github/workflows/domain-soil.yml)
has three jobs with deliberately different meanings:

| Job | Current behavior | Truthful interpretation |
|---|---|---|
| `validate-soil` | Runs the three domain suites, then the SSURGO fixture comparator | Bounded synthetic validation at the workflow's tested SHA |
| `build-proof-soil` | Verifies required boundary files, checks that no accepted proof artifact or command has silently appeared, and emits `WORKFLOW_HOLD: no accepted Soil proof producer or deterministic proof command` | Explicit readiness hold, not a proof |
| `publish-dry-run-soil` | Verifies release boundary files, checks that no candidate/command has silently appeared, and emits `WORKFLOW_HOLD: no accepted Soil release dry-run command or candidate manifest contract` | Explicit release hold, not a dry-run release |

The workflow performs no live fetch, source admission, EvidenceBundle assembly,
policy decision, promotion, manifest assembly, lifecycle write, deployment, or
publication. This runbook does not assert that `domain-soil` is a required
branch-protection or ruleset check; verify enforcement separately before relying
on that claim.

[Back to top](#top)

## 9. Rights, sensitivity, and scientific boundaries

Use only repository-approved synthetic, public-safe fixtures in this procedure.
Do not add:

- credentials, tokens, temporary links, live endpoint responses, or cached
  source payloads;
- real farm, owner, parcel, field, private station, operational sensor, or
  sensitive precise-location data;
- restricted or unreviewed Indigenous, Tribal, cultural, archaeological, or
  land-context material;
- generated assertions that present static survey, station observation,
  satellite/model grid, pedon/profile, interpretation, or suitability output as
  one interchangeable authority surface.

Synthetic success does not establish that live data is accurate, current,
representative, rights-cleared, policy-approved, or fit for a public or
consequential decision. When support type, source role, time, depth, units, QC,
uncertainty, precision, provenance, rights, or intended use is unresolved,
prefer `ABSTAIN`, `DENY`, `HOLD`, or specialist escalation over a broader claim.

[Back to top](#top)

## 10. Maintenance and documentation rollback

Update this runbook whenever any of the following changes:

- `.github/workflows/domain-soil.yml` changes Python version, commands, job
  names, hold semantics, or network controls;
- any of the three domain test inventories, fixture roots, validators, finding
  contracts, or CLI exit codes changes;
- the SSURGO comparator's cases, profiles, thresholds, finite outcomes, output
  contract, or write boundary changes;
- a shared runner-wide no-network guard is accepted and actually wired;
- proof production, EvidenceBundle resolution, policy evaluation, promotion,
  release dry run, rollback drill, deployment, or publication becomes
  executable; or
- rights, sensitivity, source-role, support-type, public-safe scale, or
  scientific-use guidance changes.

This change is documentation-only. Before merge, close the draft pull request or
revert its commit. After merge, use an ordinary reviewed revert or corrective
follow-up. Documentation rollback does not roll back data, source activation,
evidence, policy, lifecycle state, release, deployment, or publication.

## Related responsibility roots

- [Soil runbook boundary](./README.md)
- [Soil domain boundary](../../domains/soil/README.md)
- [Soil tests](../../../tests/domains/soil/README.md)
- [SSURGO comparator tests](../../../tests/ingest/ssurgo_watch/README.md)
- [Soil validators](../../../tools/validators/domains/soil/README.md)
- [Soil fixtures](../../../fixtures/domains/soil/README.md)
- [Soil source registry](../../../data/registry/sources/soil/README.md)
- [Soil proof boundary](../../../data/proofs/soil/README.md)
- [Soil release candidates](../../../release/candidates/soil/README.md)
- [Soil workflow](../../../.github/workflows/domain-soil.yml)

These links locate responsibility boundaries. Their presence does not prove
substantive implementation, source activation, acceptance, review, readiness,
or publication.

[Back to top](#top)
