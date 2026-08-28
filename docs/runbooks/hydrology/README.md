<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks-hydrology-readme
title: docs/runbooks/hydrology/ — Hydrology Operational Procedure Boundary
type: readme
subtype: boundary-compact
version: v1.0.0
prior_state: one-byte placeholder
status: draft; repository-grounded; bounded synthetic validation executable; broader semantics, source operation, proof, release, deployment, and publication held; not for life safety
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Hydrology, evidence, policy, safety, source, and release assignments"
created: 2026-08-27
updated: 2026-08-27
policy_label: repository-facing; mixed child sensitivity; fail-closed
current_path: docs/runbooks/hydrology/README.md
owning_root: docs/
responsibility: human procedure index and operational boundary for the Hydrology lane
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, policy, evidence, lifecycle, review, release, correction, rollback, and official authorities
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 8e7c862f5bf91fb27038ef264549b565b4827711
  target_prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  hydrology_runbooks_tree: e9b223adeb06fd71c9822996759d660f9c561199
  parent_runbooks_readme_blob: e145e8044b8012c2fa563d4e6ef213c0f8b80885
  domain_workflow_blob: 36a0287be04639cb75dc77ae2c274fee626f6a00
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  direct_markdown_files: 7
  repository_grounded_child_procedures: 2
  proposal_or_stale_child_procedures: 3
  explicit_scaffolds: 1
related:
  - ../README.md
  - ../../domains/hydrology/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/domain-hydrology.yml
  - ../../../contracts/domains/hydrology/README.md
  - ../../../schemas/contracts/v1/domains/hydrology/README.md
  - ../../../policy/domains/hydrology/README.md
  - ../../../fixtures/domains/hydrology/README.md
  - ../../../tests/domains/hydrology/README.md
  - ../../../tools/validators/domains/hydrology/README.md
  - ../../../data/registry/sources/hydrology/README.md
  - ../../../data/proofs/hydrology/README.md
  - ../../../release/candidates/hydrology/README.md
notes:
  - "This same-path replacement closes a one-byte navigation and boundary gap; it creates no new authority surface."
  - "VALIDATION.md and PROMOTION_RUNBOOK.md are repository-grounded; only VALIDATION.md contains a current executable bounded procedure."
  - "The other child documents retain proposal, no-mounted-repository, or scaffold language and must not be treated as paste-ready operational authority."
  - "A passing workflow establishes only the named synthetic and fixture-polarity checks at the tested SHA."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Operational Procedure Boundary

This directory routes maintainers to Hydrology procedures while keeping current
repository capability separate from proposed operations. It is an index and
boundary contract, not a source feed, scientific authority, policy decision,
proof producer, release approval, or public warning surface.

> [!WARNING]
> KFM is not a flood-warning, emergency-response, navigation, engineering,
> insurance, legal, or regulatory authority. NFHL and similar material are
> regulatory context, not observed inundation. Direct readers to the relevant
> official authority for current conditions or life-safety decisions.

> [!IMPORTANT]
> The active Hydrology workflow demonstrates bounded, no-network synthetic and
> fixture-polarity checks only. It does not establish real-world correctness,
> source admission, evidence closure, policy approval, proof, release readiness,
> deployment, publication, or current hydrologic conditions.

**Start here:** [bounded validation](./VALIDATION.md) ·
[promotion preflight](./PROMOTION_RUNBOOK.md) ·
[parent runbook index](../README.md) ·
[Hydrology domain boundary](../../domains/hydrology/README.md)

## Purpose and inherited authority

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md), which place
human operational procedures under `docs/runbooks/`. Hydrology meaning remains
under `contracts/`, machine shape under `schemas/`, executable checks under
`tests/` and `tools/validators/`, allow/deny decisions under `policy/`, source
admission under governed registry surfaces, and release decisions under
`release/`.

This README inherits those boundaries. A Markdown file, pull request, merge,
green check, map, dashboard, tile, index, test, or generated summary cannot by
itself make a Hydrology claim true or move material through the lifecycle.

## Current repository status

| Capability | Current evidence | Bounded conclusion |
|---|---|---|
| Synthetic validation | [`.github/workflows/domain-hydrology.yml`](../../../.github/workflows/domain-hydrology.yml) invokes named repository tests and validators with positive and expected-negative fixtures | Executable for the named fixture profiles at the tested SHA |
| Domain and cross-domain checks | Seven Hydrology `pytest` modules, public-safe flow fixture checks, and an environmental ownership test are named in the workflow | Bounded shape and ownership behavior only |
| EvidenceBundle, aquifer pair, and NHDPlus crosswalk fixtures | The workflow executes their repository validators and checks invalid fixture rejection | Fixture shape and polarity; not live evidence resolution, scientific accuracy, membership, geometry, or identity closure |
| Common validation target | The workflow holds if an unverified `hydrology-validate` or `validate-hydrology` Make target appears | Do not invent or document either target as a current command |
| Source refresh | The child source-refresh document labels its fetch entry point and lane paths as proposed | No current live-source refresh procedure is established here |
| Proof | The workflow records that no accepted deterministic Hydrology proof producer is wired | Proof remains held |
| Release dry run and publication | The workflow records no accepted release dry-run command or candidate contract | Release, deployment, and publication remain held |

The current bounded commands and interpretation rules live in
[`VALIDATION.md`](./VALIDATION.md). Run them from a clean checkout at the exact
SHA under review. Do not substitute live endpoints or broaden a fixture pass
into a claim about current conditions.

## Child procedure map

| Document | Current maturity | Use |
|---|---|---|
| [`VALIDATION.md`](./VALIDATION.md) | **Repository-grounded; bounded executable procedure** | Primary route for the exact tests and fixture-polarity checks named by the active workflow |
| [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | **Repository-grounded preflight; transition held** | Assemble and review promotion-readiness evidence, then stop before any transition |
| [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | **Proposal-heavy and stale** | Planning reference only; it retains unverified commands, a proposed CI sketch, and outdated repository-unknown statements |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | **Proposed operation** | Planning reference for lifecycle and source-role questions; its fetch entry point and paths are not established current commands |
| [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | **Proposed operation** | Planning reference only; it assumes release and rollback tooling that current repository evidence does not establish |
| [`ROLLBACK.md`](./ROLLBACK.md) | **Explicit scaffold** | Do not use as an operational procedure; it contains no verified rollback steps |
| `README.md` | **Repository-grounded boundary** | This navigation, authority, and maturity index |

Length is not maturity. Use the status and evidence in each document, then
reconcile every command and claim against the current repository before use.

## Procedure selection

| Need | Route | Required stop |
|---|---|---|
| Run current bounded offline checks | [`VALIDATION.md`](./VALIDATION.md) | Stop if paths, workflow inventory, checkout SHA, fixture polarity, or no-network posture differs |
| Assess promotion readiness | [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Stop before transition execution; passing checks do not approve promotion |
| Plan source refresh work | [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | Treat fetch, lifecycle writers, cadence, and publication steps as proposed until verified and authorized |
| Investigate rollback requirements | [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Treat release lookup, withdrawal, republish, and receipt emission as proposed; use no unverified command |
| Respond to current flooding or an emergency | Official public-safety authorities | Do not use KFM as the authority or instruction source |

## Belongs here

- Human procedures for running and interpreting verified Hydrology checks.
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
  workflow configuration, credentials, access links, or sensitive locations.
- Instructions that present NFHL as observed flooding, forecasts as alerts, or
  models, maps, tiles, dashboards, indexes, tests, AI output, or prose as
  sovereign truth.
- Unverified owner names, commands, endpoints, cadence, paths, release state,
  deployment state, or publication state.

## Inputs, outputs, and permitted effects

| Procedure concern | Permitted input | Permitted documentation output | Not created by documentation |
|---|---|---|---|
| Validation | Exact repository SHA, active workflow inventory, local fixtures, named tests and validators | Result record naming command, SHA, fixture polarity, classification, and unresolved holds | Scientific truth, evidence closure, policy approval, proof, release readiness |
| Promotion preflight | Candidate identity, lifecycle pointers, evidence and policy references, review prerequisites | Review handoff or explicit `HOLD` | PromotionDecision, lifecycle mutation, release approval |
| Source refresh planning | Governed source descriptor and authorized activation evidence | Plan, checklist, or `NEEDS VERIFICATION` record | Network fetch, source admission, RAW capture, publication |
| Rollback planning | Exact released identity, authoritative correction and rollback objects | Bounded assessment or escalation | Withdrawal, republish, correction, deployment rollback |

Public clients must consume governed interfaces or released public-safe
artifacts. They must not bind directly to canonical internal stores, registry
records, RAW, WORK, QUARANTINE, PROCESSED, catalog, receipt, or proof paths.

## Safety, rights, and sensitivity

Hydrology work may combine source rights, regulatory context, infrastructure,
private-property context, Indigenous or Tribal cultural information, and
precise locations. Apply the narrowest safe exposure and stop when rights,
consent, provenance, sensitivity, sovereignty, harmful precision, source role,
time, units, freshness, or correction status is unresolved.

Do not copy restricted payloads, credentials, temporary links, precise
sensitive coordinates, or unreviewed source excerpts into runbooks, logs, pull
requests, or validation records. Preserve observed, modeled, forecast,
regulatory, and alert roles as distinct classes.

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

Stop rather than improvise when the exact SHA, command, fixture set, negative
polarity, source identity, units, time, freshness, rights, sensitivity,
provenance, evidence reference, policy decision, reviewer authority,
correction path, or rollback target cannot be established. Never weaken a
validator, negative fixture, no-network guard, policy rule, inventory hold, or
topology ratchet to obtain a pass.

## Maintenance

When a Hydrology procedure changes:

1. Verify the command and path against current repository bytes and the active
   workflow; do not infer implementation from a proposal document.
2. Update this maturity map when a procedure graduates, is replaced, becomes
   stale, or is withdrawn.
3. Preserve source-role separation, no-network defaults, negative fixtures,
   explicit holds, and not-for-life-safety language.
4. Keep semantic, schema, policy, source, evidence, proof, lifecycle, release,
   and executable implementation changes in their owning roots.
5. Record unresolved conflicts in the relevant verification or drift register;
   do not create a second canonical procedure to avoid them.

GitHub review is routed by [CODEOWNERS](../../../.github/CODEOWNERS) to
`@bartytime4life`. That route does not prove specialist assignment, independent
review, approval, source admission, release, deployment, or publication.

## Related responsibility roots

- [Hydrology semantic contracts](../../../contracts/domains/hydrology/README.md)
- [Hydrology schema index](../../../schemas/contracts/v1/domains/hydrology/README.md)
- [Hydrology policy boundary](../../../policy/domains/hydrology/README.md)
- [Hydrology fixtures](../../../fixtures/domains/hydrology/README.md)
- [Hydrology tests](../../../tests/domains/hydrology/README.md)
- [Hydrology validators](../../../tools/validators/domains/hydrology/README.md)
- [Hydrology source registry](../../../data/registry/sources/hydrology/README.md)
- [Hydrology proof lane](../../../data/proofs/hydrology/README.md)
- [Hydrology release candidates](../../../release/candidates/hydrology/README.md)

## Documentation rollback

Before merge, close the draft pull request and discard only its feature branch.
After merge, revert the documentation commit or submit a reviewed forward
correction. Either action changes documentation only; it does not undo source
admission, evidence, policy, lifecycle, release, deployment, or publication
state.

[Back to top](#top)
