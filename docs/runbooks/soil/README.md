<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks-soil-readme
title: docs/runbooks/soil/ — Soil Operational Procedure Boundary
type: readme
subtype: boundary-compact
version: v1.1
prior_version: v1.0
prior_state: repository-grounded boundary that correctly identified the no-network child as proposal-heavy and stale
status: draft; repository-grounded; bounded synthetic validation executable; no-network procedure reconciled; live source operation, proof, policy activation, promotion, rollback, release, deployment, and publication held
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Soil, source, scientific, evidence, policy, release, and independent-review assignments"
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
  base_commit: a0fcc311577512b23c9ed69ed32a72132f06a773
  lane_readme_prior_blob: d50303c8f4edc6a9427d61135ba2048b0ba01a03
  no_network_runbook_prior_blob: d42e18386911dcc008a9045c38e052ce673bfda4
  no_network_runbook_head_blob: 66debc96fd7dc4d7be9db33f14beab498ee88e0e
  promotion_runbook_blob: ace5df133481918157faa902a9450b0f7f9cace8
  rollback_runbook_blob: 60ff25bf877a610627ff36430227382a68228a7e
  source_refresh_runbook_blob: f1c27e02280f9ed52e1b18c2d4b83f10e8dd4d37
  domain_workflow_blob: e009e00d5743d907461289c1c6571cab69ea2672
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  direct_markdown_files_after_change: 5
  bounded_executable_fixture_profiles: 4
  proposal_or_stale_child_procedures: 3
related:
  - ../README.md
  - ../../domains/soil/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/domain-soil.yml
  - ../../../contracts/domains/soil/README.md
  - ../../../schemas/contracts/v1/domains/soil/README.md
  - ../../../policy/domains/soil/README.md
  - ../../../fixtures/domains/soil/README.md
  - ../../../tests/domains/soil/README.md
  - ../../../tools/validators/domains/soil/README.md
  - ../../../data/registry/sources/soil/README.md
  - ../../../data/proofs/soil/README.md
  - ../../../release/candidates/soil/README.md
notes:
  - "Current executable coverage is limited to three bounded Soil fixture profiles and one fixture-only SSURGO package-drift comparator named by the active domain workflow."
  - "The no-network child now documents the current commands, fixtures, test-level Python guards, finite results, and explicit proof/release holds."
  - "The other three child runbooks remain proposal-heavy and contain illustrative, unverified, or nonexistent command surfaces."
  - "A passing workflow establishes only the named synthetic checks at the tested SHA."
  - "This documentation change creates no source admission, evidence closure, policy decision, lifecycle transition, promotion, rollback, release, deployment, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil Operational Procedure Boundary

This directory routes maintainers to Soil procedures and to the bounded checks
the repository actually runs. It is an index and boundary contract, not a soil
survey, station or satellite feed, scientific interpretation, policy decision,
proof producer, lifecycle writer, release approval, or public advice surface.

> [!IMPORTANT]
> The active Soil workflow runs only three deterministic synthetic validator
> profiles and one fixture-only SSURGO package-drift comparator. It performs no
> live retrieval and does not establish Soil truth, scientific fitness, source
> admission, evidence closure, policy approval, proof, promotion, rollback,
> release readiness, deployment, publication, or safe public use.

> [!CAUTION]
> Do not use KFM Soil material for agronomic, engineering, conservation-
> compliance, land-value, regulatory, emergency, or other consequential
> determinations. Route those decisions to the relevant qualified professional
> and official authority.

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

This README inherits those boundaries. A Markdown file, pull request, merge,
green check, model, map, tile, dashboard, test, index, or generated summary
cannot by itself make a Soil claim true or move material through the default
`RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`
lifecycle.

## Current repository status

| Capability | Current evidence | Bounded conclusion |
|---|---|---|
| Public-safe synthetic fixture validation | The active [Soil workflow](../../../.github/workflows/domain-soil.yml) invokes `test_soil_smoke.py` against `validate_public_safe_fixture.py` | Executable for the named closed fixture profile; not Soil truth, source admission, policy, proof, release, or publication evidence |
| Station soil-moisture validation | The workflow invokes `test_soil_moisture_qc.py` against the bounded station validator | Executable checks for the documented synthetic unit, depth, time, QC, deduplication, geometry, and no-network profile only |
| SMAP L4 anti-collapse validation | The workflow invokes `test_smap_l4_anti_collapse.py` against the profile-local SMAP L4 validator | Executable checks for the documented synthetic grid/model profile and support-type separation only |
| SSURGO package-drift comparison | The workflow invokes `python -m unittest tests.ingest.ssurgo_watch.test_ssurgo_watch --verbose` | Fixture-only comparator proof; no live SSURGO retrieval, currentness, rights, identity, or admission is established |
| No-network isolation | Each named suite installs targeted Python test-level socket, DNS, or URL-open guards | Bounded to the APIs and process paths explicitly tested; runner-wide and non-Python egress denial remains unproved |
| Proof | The workflow emits an explicit hold because no accepted Soil proof producer or deterministic proof command is wired | Proof remains held |
| Release dry run | The workflow emits an explicit hold because no accepted Soil release dry-run command or candidate manifest contract is wired | Promotion, release, deployment, and publication remain held |
| Child procedures | The no-network runbook is repository-grounded; the promotion, rollback, and source-refresh children remain proposal-era procedures | Use each child only within its stated maturity and stop boundary |

## Current bounded checks

Use the repository-grounded
[`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) for preflight,
execution, interpretation, failure classification, and result recording. Its
current command inventory is:

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
Use the active workflow as the current command inventory; record the checkout
SHA, command, result, and any skipped or held job. Do not describe a held job as
an executed proof or release check.

A result belongs to the exact SHA and environment in which it is produced.
`KFM_NO_NETWORK=1` does not itself block traffic, and the current tests do not
establish runner-wide, operating-system, container, namespace, dependency-
install, or non-Python isolation.

## Child procedure map

| Document | Current maturity | Safe use |
|---|---|---|
| [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | **Repository-grounded bounded procedure** | Reproduce the four active synthetic fixture suites, interpret exact fixture polarity and SSURGO comparator outcomes, and record the limits of the test-level Python network guards. It does not establish runner-wide isolation, Soil truth, proof, release, or publication. |
| [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | **Proposal-era readiness model; transition held** | Review lifecycle, support-type, rights, sensitivity, evidence, and rollback questions. Do not run its illustrative `kfm` or `conftest` commands as current repository procedures. |
| [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | **Conceptual proposal; operational rollback held** | Review defect classes, required accountability objects, and stop conditions. No accepted Soil rollback executor, safe target, drill result, withdrawal path, or operational authority is established here. |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | **Proposal-era watcher and lifecycle model; live refresh held** | Review source-role and support-type questions. Its illustrative `kfm-tools` commands are not established current entry points and must not be used for live retrieval, admission, or lifecycle writes. |
| `README.md` | **Repository-grounded boundary** | This navigation, authority, command, and maturity index |

When a child claim conflicts with current files, workflows, contracts, schemas,
policy, or tests, current repository evidence and adopted doctrine control.
External planning documents supply lineage only and cannot activate a child
procedure.

## Procedure selection

| Need | Route | Required stop |
|---|---|---|
| Run current bounded no-network checks | [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) and the active workflow | Stop if paths, SHA, fixture inventory, expected-negative polarity, or no-network posture differs |
| Assess a proposed source refresh | [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) as planning context plus the owning source registry | Stop before network retrieval, source activation, rights acceptance, or any lifecycle write |
| Assess promotion readiness | [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) as planning context plus owning evidence, policy, review, and release surfaces | Stop before transition execution; passing fixture checks do not approve promotion |
| Assess rollback requirements | [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) as planning context plus authoritative correction and rollback objects | Stop before withdrawal, republish, data mutation, deployment rollback, or public communication |
| Make a consequential Soil determination | Qualified professional and relevant official authority | Do not use KFM as the determining authority |

## Belongs here

- Human procedures for running and interpreting verified Soil checks.
- Preconditions, exact inputs, expected finite outcomes, stop conditions,
  handoff evidence, correction paths, and documentation rollback guidance.
- Links to the owning contract, schema, policy, source, evidence, validator,
  workflow, lifecycle, review, and release surfaces.
- Explicit maturity labels when repository evidence supports only a proposal,
  fixture profile, hold, or unknown state.

## Does not belong here

- Source payloads, live endpoint output, canonical observations, registry
  records, lifecycle data, evidence objects, proofs, release artifacts, or
  public-safe exports.
- Contract or schema definitions, policy rules, validator implementation,
  workflow configuration, credentials, access links, precise private
  locations, or sensitive land context.
- Instructions that collapse static surveys, gridded derivatives, station
  readings, modeled or satellite products, field observations, or in-situ
  measurements into one support type or authority role.
- Unverified owners, commands, routes, fields, endpoints, cadence, source
  activation, evidence status, review status, release state, deployment state,
  or publication state.

## Inputs, outputs, and permitted effects

| Procedure concern | Permitted input | Permitted documentation output | Not created by documentation |
|---|---|---|---|
| Bounded validation | Exact repository SHA, active workflow inventory, local synthetic fixtures, named tests and validators | Result record naming command, SHA, fixture polarity, classification, skips, and holds | Soil truth, scientific fitness, evidence closure, policy approval, proof, release readiness |
| Source-refresh assessment | Governed source descriptor, captured or fixture input, rights/currentness evidence, and activation state when available | Review checklist, explicit `HOLD`, or escalation | Network fetch, source admission, registry activation, lifecycle write |
| Promotion assessment | Candidate identity, lifecycle pointers, evidence and policy references, support type, sensitivity, correction path, and review prerequisites | Review handoff or explicit `HOLD` | PromotionDecision, lifecycle mutation, release approval |
| Rollback assessment | Exact affected identity, authoritative correction and rollback objects, safe target, dependency map, and rehearsal evidence | Decision and review handoff, bounded assessment, `HOLD`, or escalation | Withdrawal, republish, correction, lifecycle mutation, deployment rollback |

Public clients must consume governed interfaces or released public-safe
artifacts. They must not bind directly to canonical internal stores, registry
records, `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, catalog, receipt, or proof
paths.

## Rights, sensitivity, and scientific boundaries

Soil work can expose source-license restrictions, private-property or field
context, sensitive stations, Indigenous or Tribal cultural context, precise
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

Use the outcome supported by the owning procedure and authority:

- `PASS` — the exact named bounded check passed at the recorded SHA.
- `FAIL` — an expected condition or check failed.
- `HOLD` — prerequisites or transition authority are incomplete.
- `ABSTAIN` — evidence is insufficient for the requested claim.
- `DENY` — policy, source-role, sensitivity, rights, or boundary rules prohibit
  the action.
- `ERROR` — the procedure or environment could not produce a valid result.
- `ESCALATE` — accountable specialist or authority review is required.

Stop rather than improvise when the exact SHA, command, fixture set,
expected-negative result, source identity, support type, units, depth, time,
freshness, rights, sensitivity, provenance, evidence reference, policy
decision, reviewer authority, correction path, rollback target, or public-safe
carrier is missing or inconsistent.

## Maintenance

Update this boundary when any of these facts change:

- the active Soil workflow's command inventory or hold semantics;
- the three Soil validator profiles or SSURGO comparator;
- a child runbook is reconciled to current repository commands and authority;
- a proof producer, policy activation, promotion preflight, rollback drill,
  release dry run, deployment path, or publication carrier becomes accepted;
- source-role, support-type, sensitivity, rights, or public-safe scale rules
  change; or
- a related contract, schema, policy, fixture, source, proof, or release path is
  moved or superseded.

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
- [Soil release candidates](../../../release/candidates/soil/README.md)
- [Soil domain workflow](../../../.github/workflows/domain-soil.yml)

These links locate responsibility boundaries. Their presence does not prove
substantive implementation, acceptance, activation, or readiness.

## Documentation rollback

This change is documentation-only. Before merge, close the draft pull request
or revert its commit to remove it. After merge, use an ordinary reviewed revert
or a corrective follow-up. Documentation rollback does not roll back data,
source activation, evidence, policy, lifecycle state, release, deployment, or
publication.

[Back to top](#top)
