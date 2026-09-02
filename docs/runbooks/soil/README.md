<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks-soil-readme
title: docs/runbooks/soil/ - Soil Operational Procedure Boundary
type: readme
subtype: boundary-compact
version: v1.3
prior_version: v1.2
prior_state: two repository-grounded child procedures, one proposal-era promotion procedure, one proposal-era source-refresh procedure, and a repository-grounded local boundary
status: draft; repository-grounded; three child procedures current within bounded documentation scope; four synthetic no-network fixture profiles executable; live source operation, proof, policy activation, promotion execution, rollback execution, release, deployment, and publication held
owners:
  - "@bartytime4life - verified GitHub review route"
  - "NEEDS VERIFICATION - accountable Soil, source, scientific, evidence, rights, sensitivity, policy, correction, release, rollback, and independent-review assignments"
created: 2026-08-28
updated: 2026-08-30
policy_label: repository-facing; mixed child maturity; synthetic fixtures; potentially sensitive location and land context; fail-closed
current_path: docs/runbooks/soil/README.md
owning_root: docs/
responsibility: human procedure index and operational boundary for the Soil lane
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, policy, source-admission records, evidence, lifecycle, review, release, correction, rollback, source authorities, and qualified domain expertise
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: ba5b47bfe081d97ecd5d927a861be40716e68019
  prior_readme_blob: 5d39da512018afc842182d3e59aaddeb831f67f8
  promotion_runbook_prior_blob: ace5df133481918157faa902a9450b0f7f9cace8
  promotion_runbook_updated_blob: a30d524c953c76da7690d17bedb4b733971c6f46
  no_network_runbook_blob: 66debc96fd7dc4d7be9db33f14beab498ee88e0e
  rollback_runbook_blob: 7d46f9bc8a85a970c31cf10d5cb5380f6d4a41a2
  source_refresh_runbook_blob: f1c27e10d22b7fb2f0d201caf128418127ff8b21
  domain_workflow_blob: e009e00d5743d907461289c1c6571cab69ea2672
  candidate_readme_blob: f0f5a002ef3085790a0fcc991fc61788c9e04c4f
  release_index_blob: 19994f0faafb6a7858eae7e59c10049fd2ff5425
  proof_readme_blob: 1d67e180326b283e33b04cbdee283520ef3b2fad
  published_readme_blob: c70312dacedf4e367d8db2607a780b088677e30d
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  direct_markdown_files_after_change: 5
  bounded_executable_fixture_profiles: 4
  repository_grounded_child_procedures: 3
  proposal_or_stale_child_procedures: 1
related:
  - ../README.md
  - ../../domains/soil/README.md
  - ../../domains/soil/RELEASE_INDEX.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/domain-soil.yml
  - ../../../contracts/domains/soil/README.md
  - ../../../schemas/contracts/v1/domains/soil/README.md
  - ../../../policy/domains/soil/README.md
  - ../../../fixtures/domains/soil/README.md
  - ../../../tests/domains/soil/README.md
  - ../../../tools/validators/domains/soil/README.md
  - ../../../data/registry/sources/soil/README.md
  - ../../../data/proofs/soil/README.md
  - ../../../data/rollback/soil/README.md
  - ../../../data/published/soil/README.md
  - ../../../release/candidates/soil/README.md
notes:
  - "Current executable Soil coverage remains limited to three bounded Soil fixture profiles and one fixture-only SSURGO package-drift comparator named by the active domain workflow."
  - "NO_NETWORK_TEST_RUNBOOK.md is repository-grounded and fixture-only; its guards do not establish runner-wide or non-Python egress denial."
  - "PROMOTION_RUNBOOK.md is now a repository-grounded preflight and accountable-review handoff; promotion execution remains held."
  - "ROLLBACK_RUNBOOK.md is a repository-grounded candidate assessment and handoff; operational rollback remains held."
  - "SOURCE_REFRESH_RUNBOOK.md remains proposal-heavy or stale and does not establish a live refresh path."
  - "This documentation change creates no source admission, evidence closure, policy decision, lifecycle transition, rollback, promotion, release, deployment, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil Operational Procedure Boundary

This directory routes maintainers to Soil procedures and the bounded checks the
repository actually runs. It is an index, not a soil survey, station or
satellite feed, scientific interpretation, policy decision, proof producer,
lifecycle writer, release approval, rollback executor, or public advice
surface.

> [!IMPORTANT]
> The active Soil workflow runs three deterministic Soil fixture profiles and
> one fixture-only SSURGO package-drift comparator. Its proof and release
> dry-run jobs are explicit holds. None of these results establishes Soil truth,
> scientific fitness, source admission, EvidenceBundle closure, general policy
> enforcement, proof, promotion, release, operational rollback, deployment,
> publication, or safe public use.

> [!CAUTION]
> Do not use KFM Soil material for agronomic, engineering,
> conservation-compliance, land-value, title, regulatory, emergency, or other
> consequential determinations. Route those decisions to the relevant
> qualified professional and official authority.

**Start here:** [current bounded checks](#current-bounded-checks) ·
[child procedure map](#child-procedure-map) ·
[parent runbook index](../README.md) ·
[Soil domain boundary](../../domains/soil/README.md)

## Purpose and inherited authority

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md), which place
human operational procedures under `docs/runbooks/`. Soil meaning remains under
`contracts/`, machine shape under `schemas/`, executable checks under `tests/`
and `tools/validators/`, policy under `policy/`, source identity and admission
under governed registry surfaces, lifecycle payloads under `data/`, and release
decisions under `release/`.

A Markdown file, pull request, merge, green check, model, map, tile, dashboard,
test, index, or generated summary cannot by itself make a Soil claim true or
move material through:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion, rollback, correction, withdrawal, release, deployment, and
publication are separate governed transitions.

## Current repository status

| Capability | Current evidence | Bounded conclusion |
|---|---|---|
| Public-safe synthetic fixture validation | The active [Soil workflow](../../../.github/workflows/domain-soil.yml) invokes `test_soil_smoke.py` against `validate_public_safe_fixture.py` | Executable for one closed synthetic profile; not Soil truth, source admission, policy, proof, release, or publication evidence |
| Station soil-moisture validation | The workflow invokes `test_soil_moisture_qc.py` against the bounded station validator | Synthetic unit, depth, time, QC, deduplication, geometry, parser, and no-network checks only |
| SMAP L4 anti-collapse validation | The workflow invokes `test_smap_l4_anti_collapse.py` against the profile-local SMAP L4 validator | Synthetic grid/model, layer/cadence, uncertainty, and support-type separation checks only |
| SSURGO package-drift comparison | The workflow invokes `python -m unittest tests.ingest.ssurgo_watch.test_ssurgo_watch --verbose` | Fixture-only comparator; no live retrieval, admission, rights, currentness, candidate creation, or promotion |
| No-network procedure | [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) reproduces the four active commands and exact fixture polarity | Repository-grounded fixture-only procedure; no source, proof, release, or public operation |
| Promotion readiness | [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) now reconciles candidate, source, support-type, evidence, policy, proof, review, release, correction, and rollback gates to current repository evidence | Repository-grounded preflight; current result `HOLD`; execution stops at accountable release review |
| Rollback readiness | [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) uses the current generic non-executing `RollbackCard` profile and exact Soil checks | Repository-grounded candidate assessment and handoff only; no operational rollback |
| Candidate inventory | `release/candidates/soil/` contains only its README | No immutable Soil release candidate is available |
| Proof | The Soil workflow records no accepted Soil proof producer or deterministic proof command | Proof remains held |
| Release dry run | The Soil workflow records no accepted Soil release dry-run command or candidate manifest contract | Promotion, release, deployment, and publication remain held |
| Source refresh | [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) still contains proposal-era watcher and lifecycle concepts | Planning context only; live refresh remains held |
| Reviewer routing | CODEOWNERS routes repository review to `@bartytime4life` and says routing is not stewardship or approval | Accountable functional and independent review remain separate, unresolved controls |

<a id="current-bounded-checks"></a>

## Current bounded checks

Use the repository-grounded
[`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) for preflight,
execution, expected-positive and expected-negative interpretation, failure
classification, and result recording.

Run from a clean checkout at the exact SHA under review, with no live endpoints,
real secrets, production logs, sensitive field or station details, or writes to
governed data and release stores:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/soil/test_soil_smoke.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/soil/test_soil_moisture_qc.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/soil/test_smap_l4_anti_collapse.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest tests.ingest.ssurgo_watch.test_ssurgo_watch --verbose
```

The [domain test boundary](../../../tests/domains/soil/README.md) explains the
three Soil validator profiles. The SSURGO comparator is separately bounded by
[`tests/ingest/ssurgo_watch/README.md`](../../../tests/ingest/ssurgo_watch/README.md).

`KFM_NO_NETWORK=1` is posture metadata, not a firewall. A result belongs to the
exact SHA and environment in which it was produced.

For a proposed rollback candidate, the current generic non-executing profile may
also be checked:

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose

python tools/validators/release/validate_rollback_card.py --fixtures
```

These checks validate candidate shape and local consistency only. They do not
select a Soil target or execute rollback.

<a id="child-procedure-map"></a>

## Child procedure map

| Document | Current maturity | Safe use |
|---|---|---|
| [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | **Repository-grounded bounded procedure** | Reproduce the four active synthetic fixture suites, interpret fixture polarity and SSURGO comparator outcomes, and record the limits of test-level Python network guards |
| [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | **Repository-grounded promotion preflight; execution held** | Assess one immutable candidate against source, support-type, evidence, validation, policy, proof, review, release, correction, and rollback gates; stop at `READY_FOR_ACCOUNTABLE_RELEASE_REVIEW` or a fail-closed result |
| [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | **Repository-grounded candidate assessment; execution held** | Determine whether an exact Soil release exists, classify a defect, assemble a non-executing rollback/withdrawal/hold candidate, run bounded checks, and hand off |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | **Proposal-era watcher and lifecycle model; live refresh held** | Review source-role and support-profile questions only; illustrative live commands are not established entry points |
| `README.md` | **Repository-grounded boundary** | This navigation, authority, command, and maturity index |

When a child claim conflicts with current files, workflows, contracts, schemas,
policy, tests, evidence, or release records, current repository evidence and
adopted doctrine control. External planning documents provide lineage only.

## Procedure selection

| Need | Route | Required stop |
|---|---|---|
| Run current bounded no-network checks | [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) and the active Soil workflow | Stop if paths, SHA, fixture inventory, expected-negative polarity, or no-network posture differs |
| Assess a proposed source refresh | [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) as planning context plus the owning source registry | Stop before network retrieval, source activation, rights acceptance, or lifecycle write |
| Assess promotion readiness | [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) plus owning source, evidence, policy, proof, review, release, correction, and rollback surfaces | Current result is `HOLD`; stop before creating a PromotionDecision, lifecycle transition, release, deployment, or publication |
| Assess rollback readiness | [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) plus the current generic `RollbackCard` profile and authoritative release/correction surfaces | Stop before withdrawal, target selection, invalidation, resolver mutation, republish, deployment, or public communication |
| Make a consequential Soil determination | Qualified professional and relevant official authority | Do not use KFM as the determining authority |

## Inputs, outputs, and permitted effects

| Procedure concern | Permitted input | Permitted documentation output | Not created by documentation |
|---|---|---|---|
| Bounded Soil validation | Exact SHA, active workflow inventory, local synthetic fixtures, named tests and validators | Result record naming command, SHA, fixture polarity, classification, skips, and holds | Soil truth, scientific fitness, source admission, evidence closure, policy approval, proof, release readiness |
| Promotion readiness | Exact immutable candidate, source/admission and rights records, lifecycle pointers, support-type mapping, evidence, validation, policy, proof, review, correction, rollback, and dry-run references | Finite preflight result and accountable-review handoff | PromotionDecision, lifecycle mutation, release approval, public alias |
| Rollback readiness | Exact affected release, current resolver evidence, authoritative correction and rollback objects, safe target, dependency map, and bounded validation | Candidate assessment, validator findings, finite disposition, accountable handoff, or explicit hold | Withdrawal, target selection, correction publication, invalidation, resolver change, deployment rollback |
| Source-refresh assessment | Governed source descriptor, captured or fixture input, rights/currentness evidence, and activation state when available | Review checklist, explicit hold, or escalation | Network fetch, source admission, registry activation, lifecycle write |

## Rights, sensitivity, and scientific boundaries

Soil work can expose source-license restrictions, private-property or field
context, sensitive stations, Indigenous or Tribal cultural context, exact
locations, and conclusions with financial, regulatory, conservation, or safety
consequences. Use the narrowest safe exposure and stop when rights, consent,
provenance, sovereignty, harmful precision, source role, support type, time,
depth, units, quality, uncertainty, freshness, correction status, or intended
use is unresolved.

Do not copy restricted payloads, credentials, temporary links, precise private
coordinates, or unreviewed source excerpts into runbooks, logs, pull requests,
or validation records. Synthetic fixture success is not evidence that live data
is accurate, current, representative, or fit for a decision.

## Finite outcomes and stop conditions

Use only the outcome supported by the owning procedure and authority:

- `PASS` - the exact named bounded check passed at the recorded SHA.
- `FAIL` - an expected condition or check failed.
- `READY_FOR_ACCOUNTABLE_RELEASE_REVIEW` - promotion preflight inputs are
  complete enough for the owning release authority to review; not approval.
- `ROLLBACK_CANDIDATE` or `WITHDRAWAL_CANDIDATE` - non-executing rollback
  dispositions under the current generic profile.
- `HOLD` - prerequisites or transition authority are incomplete.
- `ABSTAIN` - evidence is insufficient for the requested claim.
- `DENY` - policy, source-role, support-type, sensitivity, rights, or boundary
  rules prohibit the action.
- `ERROR` - the procedure or environment could not produce a valid result.
- `ESCALATE` - accountable specialist or competent-authority review is required.

Stop rather than improvise when the exact SHA, candidate, command, fixture set,
expected-negative result, source identity, support type, MUKEY/COKEY/CHKEY,
units, depth, time, freshness, rights, sensitivity, provenance, evidence
reference, policy decision, reviewer authority, correction path, rollback
target, current resolver, dry-run result, or public-safe carrier is missing or
inconsistent.

## Maintenance

Update this boundary when:

- the active Soil workflow command inventory or hold semantics changes;
- a child runbook is reconciled to current repository commands and authority;
- an actual Soil candidate, proof, policy decision, release dry run, manifest,
  correction, withdrawal, rollback, or published carrier appears;
- the generic `RollbackCard` profile or rollback-drill boundary changes;
- source-role, support-type, sensitivity, rights, or public-safe scale rules
  change; or
- a related contract, schema, policy, fixture, source, proof, correction,
  rollback, or release path moves or is superseded.

Do not advance a maturity label from path presence or document length. Pin the
exact evidence and preserve held or unknown states until their owning surfaces
establish otherwise.

## Related responsibility roots

- [Soil domain boundary](../../domains/soil/README.md)
- [Soil release index](../../domains/soil/RELEASE_INDEX.md)
- [Soil contracts](../../../contracts/domains/soil/README.md)
- [Soil schemas](../../../schemas/contracts/v1/domains/soil/README.md)
- [Soil policy](../../../policy/domains/soil/README.md)
- [Soil fixtures](../../../fixtures/domains/soil/README.md)
- [Soil tests](../../../tests/domains/soil/README.md)
- [Soil validators](../../../tools/validators/domains/soil/README.md)
- [Soil source registry](../../../data/registry/sources/soil/README.md)
- [Soil proof boundary](../../../data/proofs/soil/README.md)
- [Soil data-plane rollback boundary](../../../data/rollback/soil/README.md)
- [Soil published-data boundary](../../../data/published/soil/README.md)
- [Soil release candidates](../../../release/candidates/soil/README.md)
- [Soil domain workflow](../../../.github/workflows/domain-soil.yml)
- [CODEOWNERS review routing](../../../.github/CODEOWNERS)

These links locate responsibility boundaries. Their presence does not prove
substantive implementation, acceptance, activation, review, release, or
publication.

## Documentation rollback

Before merge, close the draft pull request and discard only its feature branch.
After merge, use an ordinary reviewed revert or a corrective follow-up.

Documentation rollback does not roll back data, source activation, evidence,
policy, lifecycle state, release, deployment, or publication.

[Back to top](#top)
