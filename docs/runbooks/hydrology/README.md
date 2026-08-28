<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks-hydrology-readme
title: docs/runbooks/hydrology/ — Hydrology Operational Procedure Boundary
type: readme
subtype: boundary-compact
version: v1.1.0
prior_state: one-byte placeholder
status: draft; repository-grounded; bounded synthetic, captured-input, and fixture validation executable; live source operation, Hydrology-specific rollback, proof, release, deployment, and publication held; not for life safety
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Hydrology, evidence, policy, safety, source, correction, rollback, release, and operations assignments"
created: 2026-08-27
updated: 2026-08-27
policy_label: repository-facing; mixed child sensitivity; fail-closed
current_path: docs/runbooks/hydrology/README.md
owning_root: docs/
responsibility: Human procedure index, authority boundary, and maturity map for the Hydrology lane.
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, source admission, policy, evidence, lifecycle, review, release, correction, rollback, and official authorities
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 314e851b2831d16a75ec5e8a35fed257ca12c82c
  target_prior_blob: 67ac2ebd8208b2720c5765336aa9ac8af32fc11e
  source_refresh_prior_blob: 3405a9f66813525c85b574cbb7cea9aef26ac8dd
  rollback_companion_blob: 2e085a66c63c504e76ed98f46741455c25962dc6
  rollback_primary_blob: 5ea7b9c922f7a39ab80663af9700996b9ba160d1
  domain_workflow_blob: 36a0287be04639cb75dc77ae2c274fee626f6a00
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  direct_markdown_files: 7
  repository_grounded_child_procedures_after_this_change: 5
  proposal_or_stale_child_procedures_after_this_change: 1
  explicit_scaffolds_after_this_change: 0
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
  - "Version 1.1 reconciles the child-maturity map after the rollback companion/primary relationship was established and the source-refresh runbook was grounded in current repository controls."
  - "ROLLBACK.md is a compact readiness companion; ROLLBACK_RUNBOOK.md is the primary detailed Hydrology rollback procedure."
  - "SOURCE_REFRESH_RUNBOOK.md exposes bounded captured-input and fixture checks but keeps live retrieval and every lifecycle/public transition held."
  - "NO_NETWORK_TEST_RUNBOOK.md remains proposal-heavy and stale; do not treat it as current executable authority."
  - "A passing workflow establishes only the named synthetic, captured-input, and fixture-polarity checks at the tested SHA."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Operational Procedure Boundary

This directory routes maintainers to Hydrology procedures while keeping current
repository capability separate from proposed or held operations. It is an index
and boundary contract, not a source feed, scientific authority, policy decision,
proof producer, release approval, or public warning surface.

> [!WARNING]
> KFM is not a flood-warning, emergency-response, navigation, engineering,
> insurance, dam-safety, water-rights, legal, or regulatory authority. NFHL and
> similar material are regulatory context, not observed inundation. Direct
> current-condition and life-safety questions to the responsible official
> authority.

> [!IMPORTANT]
> Current executable evidence is bounded to named no-network synthetic,
> captured-input, schema, validator, and fixture-polarity checks. It does not
> establish real-world correctness, source admission, live retrieval, lifecycle
> writes, EvidenceBundle closure, policy approval, accountable review, proof,
> Hydrology-specific rollback, release readiness, deployment, publication, or
> current hydrologic conditions.

**Start here:** [bounded validation](./VALIDATION.md) ·
[source-refresh preflight](./SOURCE_REFRESH_RUNBOOK.md) ·
[promotion preflight](./PROMOTION_RUNBOOK.md) ·
[rollback readiness](./ROLLBACK.md) ·
[detailed rollback procedure](./ROLLBACK_RUNBOOK.md) ·
[parent runbook index](../README.md) ·
[Hydrology domain boundary](../../domains/hydrology/README.md)

## Purpose and inherited authority

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md), which place
human operational procedures under `docs/runbooks/`. Hydrology meaning remains
under `contracts/`, machine shape under `schemas/`, executable checks under
`tests/` and `tools/validators/`, source admission under governed registry and
activation surfaces, allow/deny decisions under `policy/`, lifecycle state under
`data/`, and release decisions under `release/`.

This README inherits those boundaries. A Markdown file, pull request, merge,
green check, map, dashboard, tile, index, test, receipt, or generated summary
cannot by itself make a Hydrology claim true or move material through the
lifecycle.

## Current repository status

| Capability | Current evidence | Bounded conclusion |
|---|---|---|
| Domain synthetic validation | [`.github/workflows/domain-hydrology.yml`](../../../.github/workflows/domain-hydrology.yml) invokes named repository tests and validators with positive and expected-negative fixtures | Executable for the named fixture profiles at the tested SHA only |
| Captured-input USGS Water normalization | Connector helper, contract, schema, fixture, tests, and a no-network workflow exist | Deterministic supplied-byte normalization; no transport, admission, RAW write, evidence, or public-use authority |
| Fixture-only USGS API cutover and WBD materiality | Dedicated contracts, validators, fixtures, tests, and workflows exist | Migration/materiality profile validation only; no live cutover or WBD request |
| Live source refresh | Source authority projection is empty; Hydrology descriptors are placeholders; live transport, activation, lifecycle writer, and executable ingest pipeline are absent or unresolved | `LIVE_SOURCE_REFRESH_HOLD` |
| Evidence and proof | The domain workflow records no accepted deterministic Hydrology proof producer | Evidence/proof closure remains held |
| Promotion | Repository-grounded preflight and handoff guidance exist | Transition execution remains held |
| Rollback | `ROLLBACK.md` is the compact readiness companion; `ROLLBACK_RUNBOOK.md` is the primary detailed procedure; generic synthetic mechanics exist but no Hydrology-specific rehearsal or production operator exists | `OPERATIONAL_ROLLBACK_HOLD` |
| Release, deployment, and publication | No accepted Hydrology release dry run, deployed-state readback, or publication authority is established | Held and separate from documentation/CI |

The exact bounded validation commands and interpretation rules live in
[`VALIDATION.md`](./VALIDATION.md) and
[`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md). Run them from a
clean checkout at the exact SHA under review. Do not substitute live endpoints
or broaden a fixture pass into a claim about current conditions.

## Child procedure map

| Document | Current maturity | Use |
|---|---|---|
| [`VALIDATION.md`](./VALIDATION.md) | **Repository-grounded; bounded executable procedure** | Primary route for the exact domain tests and fixture-polarity checks named by the active workflow |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | **Repository-grounded preflight; captured-input and fixture validation available; live refresh held** | Run the exact bounded NWIS, API-cutover, and WBD materiality checks; stop before network, activation, lifecycle, evidence, promotion, or publication |
| [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | **Repository-grounded preflight; transition held** | Assemble and review promotion-readiness evidence, then stop before any transition |
| [`ROLLBACK.md`](./ROLLBACK.md) | **Repository-grounded readiness companion** | Compact maturity snapshot, finite candidate boundary, validation index, and handoff minimum |
| [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | **Repository-grounded primary detailed procedure; operational rollback held** | Detailed classification, preflight, generic synthetic rehearsal interpretation, review handoff, and graduation gates |
| [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | **Proposal-heavy and stale** | Planning lineage only; it retains unverified commands, a proposed CI sketch, and outdated repository-unknown statements |
| `README.md` | **Repository-grounded boundary** | This navigation, authority, relationship, and maturity index |

Length is not maturity. Use each document's status and evidence, then reconcile
every command and claim against the current repository before use.

## Procedure selection

| Need | Route | Required stop |
|---|---|---|
| Run current bounded domain checks | [`VALIDATION.md`](./VALIDATION.md) | Stop if paths, workflow inventory, checkout SHA, fixture polarity, or no-network posture differs |
| Validate captured Hydrology source material or refresh readiness | [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | Live source retrieval, source activation, lifecycle writes, evidence closure, promotion, release, and publication remain held |
| Assess promotion readiness | [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Stop before transition execution; passing checks do not approve promotion |
| Check rollback maturity or choose the detailed route | [`ROLLBACK.md`](./ROLLBACK.md) | Use the primary procedure for detailed analysis; no public mutation or recovery claim |
| Analyze a Hydrology rollback candidate | [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Prepare an accountable handoff; operational rollback remains held |
| Respond to current flooding or an emergency | Official public-safety authorities | Do not use KFM as the authority or instruction source |

## Belongs here

- Human procedures for running and interpreting verified Hydrology checks.
- Preconditions, exact inputs, expected finite outcomes, stop conditions,
  handoff evidence, correction paths, and documentation rollback guidance.
- Links to the owning contract, schema, source, policy, evidence, validator,
  workflow, lifecycle, review, release, and rollback surfaces.
- Explicit maturity and relationship labels when repository evidence supports
  only a fixture profile, companion, primary procedure, hold, or unknown state.

## Does not belong here

- Source payloads, live endpoint output, canonical observations, registry or
  activation records, lifecycle data, evidence objects, proofs, release
  artifacts, or public-safe exports.
- Contract or schema definitions, policy rules, validator implementation,
  workflow configuration, credentials, access links, or sensitive locations.
- Instructions that present NFHL as observed flooding, forecasts as alerts, or
  models, maps, tiles, dashboards, indexes, tests, AI output, or prose as
  sovereign truth.
- Unverified owner names, commands, endpoints, cadence, paths, source state,
  release state, deployment state, recovery state, or publication state.

## Inputs, outputs, and permitted effects

| Procedure concern | Permitted input | Permitted documentation output | Not created by documentation |
|---|---|---|---|
| Validation | Exact repository SHA, active workflow inventory, local fixtures, named tests and validators | Result record naming command, SHA, fixture polarity, scope, and unresolved holds | Scientific truth, evidence closure, policy approval, proof, release readiness |
| Source-refresh preflight | Descriptor/activation evidence, captured input or repository fixtures, exact contracts and tests | Bounded result or explicit live-refresh `HOLD` | Network fetch, source admission, RAW/QUARANTINE write, current-condition claim, publication |
| Promotion preflight | Candidate identity, lifecycle pointers, evidence and policy references, review prerequisites | Review handoff or explicit `HOLD` | PromotionDecision, lifecycle mutation, release approval |
| Rollback readiness | Exact affected identity, candidate contract, repository evidence, synthetic fixtures, missing operational controls | Readiness assessment, candidate posture, or escalation | Withdrawal, republish, invalidation, alias mutation, recovery, deployment rollback |

Public clients must consume governed interfaces or released public-safe
artifacts. They must not bind directly to canonical internal stores, registry
records, RAW, WORK, QUARANTINE, PROCESSED, catalog, receipt, or proof paths.

## Safety, rights, and sensitivity

Hydrology work may combine source rights, regulatory context, infrastructure,
private-property context, Indigenous or Tribal cultural information, and
precise locations. Apply the narrowest safe exposure and stop when rights,
consent, provenance, sensitivity, sovereignty, harmful precision, source role,
time, units, freshness, approval state, or correction status is unresolved.

Do not copy restricted payloads, credentials, temporary links, precise
sensitive coordinates, or unreviewed source excerpts into runbooks, logs, pull
requests, or validation records. Preserve observed, administrative, aggregate,
modeled, forecast, regulatory, candidate, synthetic, provisional, and approved
states as distinct classes where the owning contract requires them.

## Finite outcomes and stop conditions

Use the outcome supported by the owning procedure and authority:

- `PASS` — the exact named bounded check passed at the recorded SHA and scope.
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
correction path, rollback target, or public state cannot be established. Never
weaken a validator, negative fixture, no-network guard, policy rule, inventory
hold, or topology ratchet to obtain a pass.

## Maintenance

When a Hydrology procedure changes:

1. Verify commands and paths against current repository bytes and active
   workflows; do not infer implementation from planning documents.
2. Update this maturity and relationship map when a procedure graduates, is
   narrowed to a companion, becomes primary, is replaced, becomes stale, or is
   withdrawn.
3. Preserve source-role separation, no-network defaults, negative fixtures,
   explicit holds, and not-for-life-safety language.
4. Keep semantic, schema, source, policy, evidence, proof, lifecycle, release,
   correction, rollback, and executable implementation changes in their owning
   roots.
5. Record unresolved conflicts in the relevant verification or drift register;
   do not create a second operational authority to avoid them.

GitHub review is routed by [CODEOWNERS](../../../.github/CODEOWNERS) to
`@bartytime4life`. That route does not prove specialist assignment,
independent review, approval, source admission, rollback authority, release,
deployment, or publication.

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

Before merge, close the draft pull request and discard only its task-owned
feature branch. After merge, revert the documentation commit or submit a
reviewed forward correction. Either action changes documentation only; it does
not undo source admission, retrieval, evidence, policy, lifecycle, rollback,
release, deployment, or publication state.

[Back to top](#top)
