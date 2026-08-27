<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks-hazards-readme
title: docs/runbooks/hazards/ — Hazards Operational Procedure Boundary
type: readme
subtype: boundary-compact
version: v1.0.0
prior_version: one-byte placeholder
status: draft; repository-grounded; not-for-life-safety; non-release; non-publication
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Hazards, source, safety, policy, correction, rollback, and release assignments"
created: 2026-08-27
updated: 2026-08-27
policy_label: repository-facing; hazards; operational-procedure index; not-for-life-safety; fail-closed
current_path: docs/runbooks/hazards/README.md
owning_root: docs/
responsibility: "Define the local boundary for Hazards operational procedures, route readers to the correct runbook, disclose current implementation limits, and preserve the not-for-life-safety and non-publisher posture."
truth_posture: cite-or-abstain
authority_class: explanatory runbook-lane boundary
authority_rank: subordinate to accepted doctrine and ADRs, Hazards domain doctrine, contracts, schemas, source records, policy, evidence, review, lifecycle, release, correction, and rollback authorities
canonical_relationship: same-path replacement of a one-byte placeholder; no sibling authority created
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: e68064525994702f1f6f4dbd33e4834c6c835d8a
  target_prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  hazards_runbook_tree: e409810f4be0ecefab23ffe5fcdadfeee1c8702b
  parent_index_prior_blob: 327f1c1c9693c296101c6a161ab6605e1257bf3e
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  workflow_blob: 9d48f97ff33fedd4f2acf3a6aed2b6753d0caaea
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  direct_markdown_files_including_this_readme: 7
  substantive_child_procedures: 6
  open_pull_requests_touching_this_readme: 0
related:
  - ../README.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../../domains/hazards/README.md
  - ../../domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../contracts/domains/hazards/README.md
  - ../../../schemas/contracts/v1/domains/hazards/README.md
  - ../../../fixtures/domains/hazards/README.md
  - ../../../tests/domains/hazards/README.md
  - ../../../tools/validators/domains/hazards/README.md
  - ../../../policy/domains/hazards/README.md
  - ../../../data/registry/sources/hazards/README.md
  - ../../../data/proofs/hazards/README.md
  - ../../../release/candidates/hazards/README.md
  - ../../../.github/workflows/domain-hazards.yml
notes:
  - "The lane contains six substantive procedures; procedure length and file presence do not establish runtime, operational admission, review, release, deployment, promotion, or publication."
  - "Current executable coverage is bounded to deterministic no-network drought-family fixtures, USDM materiality validation, and a synthetic rollback rehearsal."
  - "Live source refresh, active Hazards policy enforcement, proof production, candidate assembly, release dry-run, operational rollback, deployment, and publication remain held or unverified."
  - "The repository-grounded source-refresh v2 procedure is merged on current main; live refresh remains held."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/runbooks/hazards/` — Hazards Operational Procedure Boundary

> **Local index for repository procedures that validate, audit, prepare, rehearse, contain, correct, or roll back Hazards work.** These documents explain bounded human steps; they do not issue alerts, establish current conditions, activate sources, approve policy, mutate lifecycle state, release artifacts, or publish data.

> [!WARNING]
> KFM is not an emergency-alert, warning, evacuation, incident-command, medical, regulatory, or life-safety authority. Use the applicable official authority for urgent decisions and protective-action instructions.

> [!IMPORTANT]
> The strongest current executable result is bounded synthetic validation at an immutable repository revision. Green checks, fixture passes, a merge, or this README do not establish live-source fitness, current hazard conditions, policy enforcement, proof closure, operational rollback, release readiness, or public-use safety.

**Quick navigation:** [Purpose](#purpose-and-inherited-boundary) · [Authority](#authority-and-negative-authority) · [Status](#current-status) · [Start here](#start-here) · [Children](#direct-child-map) · [Belongs](#what-belongs-here) · [Prohibited](#what-does-not-belong-here) · [Inputs and outputs](#inputs-and-outputs) · [Exposure](#exposure-mutation-and-retention) · [Outcomes](#finite-outcomes-and-stop-conditions) · [Validation](#validation-and-rehearsal) · [Maintenance](#maintenance-open-verification-and-rollback)

## Purpose and inherited boundary

`docs/runbooks/hazards/` is the Hazards operational-procedure child of the parent [`docs/runbooks/`](../README.md) index. Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the [Directory Rules](../../doctrine/directory-rules.md), which place human procedures under `docs/runbooks/` and require local boundary documentation where risk, authority, exposure, mutation, or lifecycle behavior changes.

This README helps maintainers and reviewers answer:

- Which Hazards procedure applies to a documentation, validation, source-refresh, promotion, correction, or rollback question?
- What exact repository evidence and finite result can the procedure establish?
- Which steps are implemented, synthetic-only, held, or still unverified?
- Which authority-bearing object or responsibility root must be consulted next?
- Where must work stop before it could be mistaken for current hazard guidance, official instruction, release authority, or publication?

The parent runbook contract is inherited in full. This child adds the stricter Hazards boundary: preserve source role, object family, time, freshness, expiry, rights, sensitivity, official attribution, correction, withdrawal, and not-for-life-safety posture.

## Authority and negative authority

| Concern | Owning surface | Role of this lane |
|---|---|---|
| Hazards meaning and public-safety boundary | [`docs/domains/hazards/`](../../domains/hazards/README.md) | Consume and operationalize the documented boundary; do not redefine it |
| Human procedure | This directory | Explain preconditions, exact commands, stops, finite outcomes, and handoff |
| Object meaning | [`contracts/domains/hazards/`](../../../contracts/domains/hazards/README.md) | Cite semantics; do not create a contract in a runbook |
| Machine shape | [`schemas/contracts/v1/domains/hazards/`](../../../schemas/contracts/v1/domains/hazards/README.md) | Cite verified schemas and limitations; do not make shape sovereign truth |
| Source identity and admission | [`data/registry/sources/hazards/`](../../../data/registry/sources/hazards/README.md) plus accepted source governance | Verify references; do not activate a source |
| Executable validation | [`tests/domains/hazards/`](../../../tests/domains/hazards/README.md), [`tools/validators/domains/hazards/`](../../../tools/validators/domains/hazards/README.md), `Makefile`, and workflows | Point to exact reviewed entry points and interpret only their bounded result |
| Policy and review | [`policy/domains/hazards/`](../../../policy/domains/hazards/README.md) and governed review records | Consume actual results; do not infer approval from prose or CI |
| Proof and release | [`data/proofs/hazards/`](../../../data/proofs/hazards/README.md) and [`release/candidates/hazards/`](../../../release/candidates/hazards/README.md) | Prepare a handoff; do not mint proof, approve release, or publish |
| Correction and rollback | Accepted correction, rollback, release, and public-state authorities | Describe and rehearse bounded mechanics; do not claim production recovery |

No file in this directory may:

- issue, relay, rank, suppress, extend, cancel, or replace an official warning or instruction;
- turn a model, detection, map, tile, dashboard, index, AI response, or fixture into canonical hazard truth;
- treat source availability as source admission or currentness;
- authorize a policy exception, lifecycle transition, release, deployment, promotion, or publication; or
- hide `UNKNOWN`, `NEEDS VERIFICATION`, `HOLD`, stale, expired, corrected, withdrawn, or conflicting state.

## Current status

The observations below are pinned to `main@e68064525994702f1f6f4dbd33e4834c6c835d8a` and describe repository bytes, not deployed behavior.

| Surface | Repository-grounded status | Safe conclusion |
|---|---|---|
| This README | One-byte placeholder before this change | This change establishes navigation and boundary prose only |
| Child procedures | Six substantive Markdown files | Procedure coverage exists; operational maturity varies |
| Domain workflow | One bounded validation job plus explicit proof and release-dry-run holds | Synthetic drought-family validation is implemented; proof and release remain held |
| No-network validation | Drought observation, drought declaration, relationship fixtures, and USDM materiality cases | Passes are bounded to the named committed profile |
| Rollback rehearsal | Marker-protected synthetic helper, fixture, and tests | Synthetic mechanics exist; operational Hazards rollback is unverified |
| Source refresh | Repository-grounded v2 procedure records exact source-edge conflicts and bounded commands | Live retrieval, admission, lifecycle mutation, proof, and release remain held |
| Source admission and live retrieval | No admitted live source or accepted Hazards refresh executor established by this lane | Live refresh remains `HOLD` |
| Policy | Default-only Hazards policy source with no accepted evaluator binding | No operational allow/deny result can be inferred |
| Proof and candidate | No accepted Hazards proof producer or candidate dossier established | Proof, promotion, and release remain `HOLD` |
| Public behavior | No released public-safe Hazards carrier established by these runbooks | Current-condition, deployment, and publication claims remain unsupported |
| Ownership | CODEOWNERS routes GitHub review to `@bartytime4life` | Accountable specialist and independent-review assignments remain `NEEDS VERIFICATION` |

Keep these states distinct: file presence, documentation maturity, validator result, rehearsal result, review, operational admission, lifecycle transition, release, deployment, promotion, and publication.

## Start here

| Need | Procedure | Highest current result |
|---|---|---|
| Audit a change for the not-for-life-safety boundary | [`NOT_FOR_LIFE_SAFETY_AUDIT_RUNBOOK.md`](./NOT_FOR_LIFE_SAFETY_AUDIT_RUNBOOK.md) | Scoped documentary audit; runtime enforcement remains unverified unless exact paths are tested |
| Run the committed no-network Hazards checks | [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | `BOUNDED_SYNTHETIC_VALIDATION_PASS` or a finite failure; no live-source or release effect |
| Prepare a Hazards promotion handoff | [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Preflight result; promotion execution remains held |
| Rehearse synthetic rollback mechanics | [`ROLLBACK_DRILL.md`](./ROLLBACK_DRILL.md) | Bounded synthetic rehearsal; not production recovery |
| Contain and plan Hazards rollback | [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Documentation and synthetic mechanics; operational rollback remains held |
| Evaluate a source refresh | [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | Repository-grounded readiness procedure; live source refresh remains held |

Choose the narrowest applicable procedure. When a change touches multiple concerns, run each relevant procedure and keep their results separate.

## Direct child map

```text
docs/runbooks/hazards/
├── README.md
├── NOT_FOR_LIFE_SAFETY_AUDIT_RUNBOOK.md
├── NO_NETWORK_TEST_RUNBOOK.md
├── PROMOTION_RUNBOOK.md
├── ROLLBACK_DRILL.md
├── ROLLBACK_RUNBOOK.md
└── SOURCE_REFRESH_RUNBOOK.md
```

This map is intentionally direct-only. Contracts, schemas, fixtures, validators, tests, source records, policy, proofs, candidates, and released artifacts remain in their owning roots.

## What belongs here

- Human-operable Hazards procedures with a clear goal, audience, scope, authority boundary, and immutable evidence identity.
- Exact repository commands that exist at the cited revision, with prerequisites and bounded interpretations.
- Preconditions for source role, object family, time, rights, sensitivity, evidence, policy, review, correction, and rollback.
- Fail-closed stop conditions and finite outcomes such as `PASS`, `FAIL`, `HOLD`, `ABSTAIN`, `DENY`, `ERROR`, `ROLLBACK`, `ESCALATE`, and `UNKNOWN`.
- Synthetic rehearsal instructions that clearly distinguish fixture evidence from operational capability.
- Safe handoff fields and repository-safe diagnostics that exclude protected payloads.
- Maintenance triggers, correction guidance, and documentation rollback instructions.

## What does not belong here

- Current warnings, watches, advisories, evacuation or shelter instructions, route advice, medical guidance, incident-command material, or official protective-action text.
- Credentials, signed URLs, private endpoints, emergency-operation details, exact sensitive infrastructure, living-person information, culturally controlled material, restricted locations, or other harmful precision.
- Source descriptors, admitted-source records, connector configuration, schedules, secrets, contracts, schemas, policies, fixtures, executable validators, lifecycle data, receipts, proofs, candidates, manifests, or published payloads.
- Invented commands, owners, routes, fields, workflow behavior, test results, source status, policy decisions, release state, or operational maturity.
- A duplicate of Hazards domain doctrine or a parallel authority for source, policy, evidence, lifecycle, release, correction, or rollback.

## Inputs and outputs

### Required inputs

A procedure should identify, as applicable:

- immutable repository revision and validation identity;
- exact change, source, artifact, candidate, or incident scope;
- accepted contract, schema, source, rights, time, sensitivity, policy, and review references;
- actor permissions and safe execution environment;
- valid and invalid fixtures plus expected finite outcomes;
- prior safe state, correction/withdrawal scope, and rollback target; and
- the official-authority referral required for operational context.

Missing authority-bearing input produces `HOLD`, `UNKNOWN`, `NEEDS VERIFICATION`, or `ABSTAIN`; prose must not fill the gap.

### Permitted outputs

A runbook may produce or request:

- a bounded validation or rehearsal result tied to an immutable revision;
- a repository-safe checklist, worksheet, diagnostic, or handoff summary;
- explicit missing-dependency and stop-condition records;
- links to separately governed evidence, policy, review, lifecycle, correction, rollback, and release objects; and
- a recommended next procedure or owning responsibility root.

A runbook output is not an `EvidenceBundle`, `PolicyDecision`, `ReviewRecord`, `PromotionDecision`, `ReleaseManifest`, `CorrectionNotice`, `RollbackCard`, deployment record, or publication event.

## Exposure, mutation, and retention

| Concern | Boundary |
|---|---|
| Repository exposure | Keep ordinary documentation public-safe; cite sensitive authorities without copying restricted payloads |
| Network access | Default bounded validation to no-network fixtures; live access requires separate accepted authority and reviewed implementation |
| Mutation | Documentation changes may alter Markdown only; lifecycle and public-state writes require owning executors and authorization |
| Retention | Preserve immutable evidence identity, results, supersession, correction, and rollback references without retaining prohibited payloads |
| Logs | Record commands, revision, exit status, and bounded diagnostics; exclude credentials, private endpoints, protected geometry, and live payloads |
| Public clients | Use governed interfaces or released public-safe carriers; never direct internal-store or live-source access |

## Finite outcomes and stop conditions

Every procedure must end in a finite, scoped result. Use procedure-specific definitions, but preserve these boundaries:

| Outcome | Meaning in this lane |
|---|---|
| `PASS` | The named checks passed at the named revision and scope only |
| `FAIL` | A named requirement did not pass; no downstream authority is implied |
| `HOLD` | Required authority, evidence, implementation, review, or rollback support is missing |
| `ABSTAIN` | Evidence is insufficient for the requested conclusion |
| `DENY` | A hard policy, rights, safety, sensitivity, or authority boundary prohibits the action |
| `ERROR` | The procedure could not complete because of system or environment failure |
| `ROLLBACK` | Separately authorized recovery is required; the runbook does not self-authorize execution |
| `ESCALATE` | Accountable specialist or authority review is required |
| `UNKNOWN` | Current evidence cannot establish the state |

Stop before further action when:

- official source, source role, object family, time validity, rights, sensitivity, evidence, policy, review, or rollback identity is unresolved;
- a surface could be mistaken for current protective-action or regulatory authority;
- stale, expired, corrected, withdrawn, conflicting, or missing evidence would appear current or reassuring;
- a live endpoint, secret, write-capable workflow, release action, or public side effect is outside the authorized scope;
- validation identity is not immutable or merge-result behavior materially differs from the tested head; or
- the procedure would erase evidence, weaken a negative test, or bypass lifecycle and release gates.

## Validation and rehearsal

The domain workflow currently runs:

```bash
python -m unittest -v tests.domains.hazards.test_hazards_smoke
make hazards-validate
```

with `KFM_NO_NETWORK=1`, deterministic Python environment variables, read-only repository permission, and no persisted checkout credentials. See the [no-network runbook](./NO_NETWORK_TEST_RUNBOOK.md) for prerequisites, exact interpretation, and failure handling.

For Markdown changes to this lane:

1. review the complete base-to-head diff;
2. confirm exactly one H1 per changed ordinary document;
3. check heading order, custom anchors, code fences, tables, alerts, and reference definitions;
4. resolve every relative link and cited path at the proposed head;
5. verify every command against current executable surfaces;
6. confirm truth labels, limitations, and non-effects remain visible; and
7. classify hosted checks as passing, failing, pending, skipped, inherited, or unavailable without treating them as human approval.

Rehearsal evidence must name the fixture, revision, environment, mode, result, and limitation. A synthetic rehearsal cannot prove live-source, production, emergency, release, deployment, or public recovery behavior.

## Maintenance, open verification, and rollback

Update this README when a direct child is added, removed, renamed, superseded, materially changes its highest result, or gains a new executable dependency. Re-read the parent contract and Directory Rules when scope, authority, exposure, mutation, generation, or lifecycle behavior changes.

Open verification items:

- assign accountable Hazards, source, safety, rights, policy, correction, rollback, release, security, accessibility, and independent-review responsibilities;
- keep the source-refresh procedure synchronized with accepted source records, active pipeline bindings, and exact repository commands;
- establish accepted source admission and active pipeline-spec bindings before any live refresh;
- implement and bind native Hazards policy evaluation before claiming operational decisions;
- establish proof production, immutable candidate assembly, Hazards release dry-run, and public-safe readback;
- prove correction propagation, withdrawal, invalidation, and operational rollback without harmful detail exposure; and
- keep adjacent domain and public-client joins governed by the most restrictive applicable boundary.

To roll back this documentation-only change before merge, close the draft pull request. After merge, revert the commit or restore prior blob `8b137891791fe96927ad78e64b0aad7bded08bdc` through a new reviewed change. That rollback restores the placeholder; it does not deactivate a source, undo lifecycle state, invalidate a public carrier, withdraw a release, or recover operational state.

[Back to top](#top)
