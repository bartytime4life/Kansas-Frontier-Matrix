<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks-soil-readme
title: docs/runbooks/soil/ — Soil Operational Procedure Boundary
type: readme
subtype: boundary-compact
version: v1.1
prior_state: v1.0 repository-grounded boundary with four proposal-heavy child procedures
status: draft; repository-grounded; bounded synthetic validation executable; rollback-readiness assessment repository-grounded; live source operation, proof, policy activation, rollback execution, promotion, release, deployment, and publication held
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Soil, source, scientific, evidence, rights, sensitivity, policy, correction, release, rollback, and independent-review assignments"
created: 2026-08-28
updated: 2026-08-29
policy_label: repository-facing; mixed child maturity; potentially sensitive location and land context; fail-closed
current_path: docs/runbooks/soil/README.md
owning_root: docs/
responsibility: human procedure index and operational boundary for the Soil lane
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, policy, evidence, lifecycle, review, release, correction, rollback, source authorities, and qualified domain expertise
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 349d0097e5f7533abe6cd8253f4bd7a30eccd003
  target_before_update_blob: d50303c8f4edc6a9427d61135ba2048b0ba01a03
  no_network_runbook_blob: d42e18386911dcc008a9045c38e052ce673bfda4
  promotion_runbook_blob: ace5df133481918157faa902a9450b0f7f9cace8
  rollback_runbook_before_update_blob: 60ff25bf877a610627ff36430227382a68228a7e
  source_refresh_runbook_blob: f1c27e02280f9ed52e1b18c2d4b83f10e8dd4d37
  parent_runbooks_readme_blob: 4f33dfa18cd69fe6a6b990aac71be08d59e7d13e
  domain_workflow_blob: e009e00d5743d907461289c1c6571cab69ea2672
  rollback_card_contract_blob: c6d3c35c56b064e04c3a2532f4709d938d7b0c1a
  rollback_card_schema_blob: e0a9edf02dd5d6997eda60a054a5bf19636c3dd4
  rollback_card_validator_blob: 9e9ed5a92851935b41a36698e4bead13ef4edf57
  rollback_drill_workflow_blob: 2d0c39fc6ff8e44bd9cf753ce546475079e8ffd5
  domain_tests_readme_blob: ff39df062df22583c9dd762f8c4ca36f902cac71
  domain_readme_blob: 06cfbebc3ce130753d4aff766645765747e1dae6
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  direct_markdown_files_after_change: 5
  bounded_executable_fixture_profiles: 4
  repository_grounded_child_procedures: 1
  proposal_or_stale_child_procedures: 3
related:
  - ../README.md
  - ../../domains/soil/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/domain-soil.yml
  - ../../../.github/workflows/rollback-card.yml
  - ../../../.github/workflows/rollback-drill.yml
  - ../../../contracts/release/rollback_card.md
  - ../../../schemas/contracts/v1/release/rollback_card.schema.json
  - ../../../tools/validators/release/validate_rollback_card.py
  - ../../../tests/validators/test_validate_rollback_card.py
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
  - "ROLLBACK_RUNBOOK.md is now a repository-grounded candidate-assessment and handoff procedure; it still provides no operational rollback authority."
  - "NO_NETWORK_TEST_RUNBOOK.md, PROMOTION_RUNBOOK.md, and SOURCE_REFRESH_RUNBOOK.md remain proposal-heavy or stale and must not be treated as current live procedures."
  - "The generic RollbackCard validator and generic/Hazards rehearsal are non-executing bounded evidence; production rollback remains held."
  - "This documentation change creates no source admission, evidence closure, policy decision, lifecycle transition, rollback, promotion, release, deployment, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil Operational Procedure Boundary

This directory routes maintainers to Soil procedures and to the bounded checks
the repository actually runs. It is an index and boundary contract, not a soil
survey, station or satellite feed, scientific interpretation, policy decision,
proof producer, lifecycle writer, release approval, rollback executor, or
public advice surface.

> [!IMPORTANT]
> The active Soil workflow runs three deterministic Soil fixture profiles and
> one fixture-only SSURGO package-drift comparator. The repository also has a
> closed, proposed, non-executing generic `RollbackCard` candidate validator
> and a generic/Hazards synthetic rollback rehearsal. None of these establishes
> Soil truth, scientific fitness, source admission, evidence closure, policy
> approval, proof, operational rollback, release readiness, deployment,
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
and `tools/validators/`, allow/deny decisions under `policy/`, source identity
and admission under governed registry surfaces, and release decisions under
`release/`.

A Markdown file, pull request, merge, green check, model, map, tile, dashboard,
test, index, or generated summary cannot by itself make a Soil claim true or
move material through the default
`RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`
lifecycle.

## Current repository status

| Capability | Current evidence | Bounded conclusion |
|---|---|---|
| Public-safe synthetic fixture validation | The active [Soil workflow](../../../.github/workflows/domain-soil.yml) invokes `test_soil_smoke.py` against `validate_public_safe_fixture.py` | Executable for the named closed fixture profile; not Soil truth, source admission, policy, proof, release, or publication evidence |
| Station soil-moisture validation | The workflow invokes `test_soil_moisture_qc.py` against the bounded station validator | Executable checks for the documented synthetic unit, depth, time, QC, deduplication, geometry, and no-network profile only |
| SMAP L4 anti-collapse validation | The workflow invokes `test_smap_l4_anti_collapse.py` against the profile-local SMAP L4 validator | Executable checks for the documented synthetic grid/model profile and support-type separation only |
| SSURGO package-drift comparison | The workflow invokes `python -m unittest tests.ingest.ssurgo_watch.test_ssurgo_watch --verbose` | Fixture-only comparator proof; no live SSURGO retrieval, currentness, rights, identity, or admission is established |
| Rollback readiness | [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) now uses the current generic `RollbackCard` contract/schema/validator, exact Soil test commands, repository inventory, and explicit production holds | Repository-grounded candidate assessment and accountable handoff only; no Soil release or operational rollback is established |
| Generic rollback candidate validation | The proposed `RollbackCard` profile has a closed schema, no-network validator, three valid fixtures, six invalid fixture families, focused tests, and a read-only workflow | Candidate shape and local consistency only; no approval, target selection, execution, or public mutation |
| Synthetic rollback rehearsal | The rollback-drill workflow runs twelve generic and Hazards tests against a marker-protected synthetic helper | Regression evidence only; it is not a Soil-specific or production drill |
| Proof | The Soil workflow emits an explicit hold because no accepted Soil proof producer or deterministic proof command is wired | Proof remains held |
| Release dry run | The Soil workflow emits an explicit hold because no accepted Soil release dry-run command or candidate manifest contract is wired | Promotion, release, deployment, and publication remain held |
| Remaining child procedures | Three long-form child runbooks retain proposal-era assumptions, unverified commands, or live-operation concepts | Planning and review context only; length is not operational maturity |

<a id="current-bounded-checks"></a>

## Current bounded checks

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

For a proposed rollback candidate, use the exact non-executing generic profile:

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose

python tools/validators/release/validate_rollback_card.py --fixtures
```

Use the active workflows as the current command inventory. Record the checkout
SHA, command, result, and any skipped or held job. Do not describe a held job
as an executed proof, release check, or rollback.

These commands are repository-grounded entry points, but they were **NOT RUN**
as part of this Markdown-only authoring step. A future result belongs to the
exact SHA and environment in which it is produced.

<a id="child-procedure-map"></a>

## Child procedure map

| Document | Current maturity | Safe use |
|---|---|---|
| [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | **Proposal-heavy and stale** | Planning reference only. Its proposed make, pytest, environment, probe, and receipt surfaces are not the active command inventory. Use [Current bounded checks](#current-bounded-checks). |
| [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | **Proposal-era readiness model; transition held** | Review lifecycle, support-profile, rights, sensitivity, evidence, and rollback questions. Do not run illustrative `kfm` or `conftest` commands as current procedures. |
| [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | **Repository-grounded candidate assessment; operational rollback held** | Confirm whether an exact Soil release exists, classify the defect, assemble the current generic non-executing candidate, run bounded checks, and stop at accountable handoff. |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | **Proposal-era watcher and lifecycle model; live refresh held** | Review source-role and support-profile questions. Its illustrative `kfm-tools` commands are not established live entry points. |
| `README.md` | **Repository-grounded boundary** | This navigation, authority, command, and maturity index |

When a child claim conflicts with current files, workflows, contracts, schemas,
policy, or tests, current repository evidence and adopted doctrine control.
External planning documents supply lineage only and cannot activate a child
procedure.

## Procedure selection

| Need | Route | Required stop |
|---|---|---|
| Run current bounded offline checks | [Current bounded checks](#current-bounded-checks) and the active Soil workflow | Stop if paths, SHA, fixture inventory, expected-negative polarity, or no-network posture differs |
| Assess a proposed source refresh | [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) as planning context plus the owning source registry | Stop before network retrieval, source activation, rights acceptance, or any lifecycle write |
| Assess promotion readiness | [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) as planning context plus owning evidence, policy, review, and release surfaces | Stop before transition execution; fixture checks do not approve promotion |
| Assess rollback readiness | [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) plus the current generic `RollbackCard` profile and authoritative release/correction surfaces | Stop before withdrawal, target selection, invalidation, resolver mutation, republish, deployment, or public communication |
| Make a consequential Soil determination | Qualified professional and relevant official authority | Do not use KFM as the determining authority |

## Inputs, outputs, and permitted effects

| Procedure concern | Permitted input | Permitted documentation output | Not created by documentation |
|---|---|---|---|
| Bounded Soil validation | Exact repository SHA, active workflow inventory, local synthetic fixtures, named tests and validators | Result record naming command, SHA, fixture polarity, classification, skips, and holds | Soil truth, scientific fitness, evidence closure, policy approval, proof, release readiness |
| Rollback readiness | Exact affected identity, current resolver evidence, authoritative correction and rollback objects, safe target, dependency map, and bounded validation | Candidate assessment, validator findings, finite disposition, accountable handoff, or explicit hold | Withdrawal, target selection, correction publication, lifecycle mutation, invalidation, resolver change, deployment rollback |
| Source-refresh assessment | Governed source descriptor, captured or fixture input, rights/currentness evidence, and activation state when available | Review checklist, explicit hold, or escalation | Network fetch, source admission, registry activation, lifecycle write |
| Promotion assessment | Candidate identity, lifecycle pointers, evidence and policy references, support profile, sensitivity, correction path, and review prerequisites | Review handoff or explicit hold | PromotionDecision, lifecycle mutation, release approval |

## Rights, sensitivity, and scientific boundaries

Soil work can expose source-license restrictions, private-property or field
context, sensitive stations, Indigenous or Tribal cultural context, precise
locations, and conclusions with financial, regulatory, conservation, or safety
consequences. Use the narrowest safe exposure and stop when rights, consent,
provenance, sovereignty, harmful precision, source role, support profile, time,
depth, units, quality, uncertainty, freshness, correction status, or intended
use is unresolved.

Do not copy restricted payloads, credentials, temporary links, precise private
coordinates, or unreviewed source excerpts into runbooks, logs, pull requests,
or validation records. Synthetic fixture success is not evidence that live data
is accurate, current, representative, or fit for a decision.

## Finite outcomes and stop conditions

Use only the outcome supported by the owning procedure and authority:

- `PASS` — the exact named bounded check passed at the recorded SHA.
- `FAIL` — an expected condition or check failed.
- `ROLLBACK_CANDIDATE` — a non-executing candidate names a distinct prior safe
  release.
- `WITHDRAWAL_CANDIDATE` — a non-executing withdrawal candidate is required.
- `HOLD` — prerequisites or transition authority are incomplete.
- `ABSTAIN` — evidence is insufficient for the requested claim.
- `DENY` — policy, source-role, sensitivity, rights, or boundary rules prohibit
  the action.
- `ERROR` — the procedure or environment could not produce a valid result.
- `ESCALATE` — accountable specialist or authority review is required.

Stop rather than improvise when the exact SHA, command, fixture set,
expected-negative result, source identity, support profile, MUKEY/COKEY/CHKEY,
units, depth, time, freshness, rights, sensitivity, provenance, evidence
reference, policy decision, reviewer authority, correction path, rollback
target, current resolver, or public-safe carrier is missing or inconsistent.

## Maintenance

Update this boundary when:

- the active Soil workflow command inventory or hold semantics changes;
- a child runbook is reconciled to current repository commands and authority;
- the generic `RollbackCard` profile or rollback-drill boundary changes;
- a Soil-specific proof producer, policy activation, promotion preflight,
  rollback drill, release dry run, executor, deployment path, or publication
  carrier becomes accepted;
- source-role, support-profile, sensitivity, rights, or public-safe scale rules
  change; or
- a related contract, schema, policy, fixture, source, proof, correction,
  rollback, or release path moves or is superseded.

Do not advance a maturity label from path presence or document length. Pin the
exact evidence and preserve held or unknown states until their owning surfaces
establish otherwise.

## Related responsibility roots

- [Soil domain boundary](../../domains/soil/README.md)
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
- [Generic `RollbackCard` contract](../../../contracts/release/rollback_card.md)
- [Generic `RollbackCard` schema](../../../schemas/contracts/v1/release/rollback_card.schema.json)
- [Generic `RollbackCard` validator](../../../tools/validators/release/validate_rollback_card.py)
- [Soil domain workflow](../../../.github/workflows/domain-soil.yml)
- [`RollbackCard` workflow](../../../.github/workflows/rollback-card.yml)
- [Rollback-drill readiness workflow](../../../.github/workflows/rollback-drill.yml)

These links locate responsibility boundaries. Their presence does not prove
substantive implementation, acceptance, activation, or readiness.

## Documentation rollback

Before merge, close the draft pull request and discard only its feature branch.
After merge, use an ordinary reviewed revert or a corrective follow-up.
Documentation rollback does not roll back data, source activation, evidence,
policy, lifecycle state, release, deployment, or publication.

[Back to top](#top)
