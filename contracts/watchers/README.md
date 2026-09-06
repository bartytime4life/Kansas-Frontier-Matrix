<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-watchers-readme
title: contracts/watchers/ — Shared Watcher Semantic-Contract Boundary
type: readme; nested-directory-readme; semantic-contract-boundary
version: v0.1
status: draft; proposed-inactive; repository-grounded; boundary-compact; non-publisher; no-network
owners: OWNER_TBD — Watcher steward · Source steward · Policy steward · Validation steward · Release steward · Docs steward
created: 2026-09-06
updated: 2026-09-06
policy_label: public; contracts; watchers; semantic-meaning; fail-closed; no-live-activation; non-publisher; correction-aware; rollback-aware
owning_root: contracts/
responsibility: define shared watcher object meaning, finite routing semantics, exclusions, and compatibility boundaries without becoming machine-shape, policy, source, runtime, lifecycle, evidence, release, or publication authority
truth_posture: CONFIRMED repository paths and bounded inactive watcher contracts / PROPOSED shared ownership and activation / NEEDS VERIFICATION complete consumer, steward, rights, sensitivity, receipt, and runtime closure
current_path: contracts/watchers/README.md
inherited_parent: ../README.md
scope_id: shared-watchers-contracts
evidence_snapshot: bartytime4life/Kansas-Frontier-Matrix@9683ac6cbe385938dbeb66c9f61d82f8de770423
prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
related:
  - ../README.md
  - ./watcher_gate_packet.md
  - ../source/README.md
  - ../source/watcher_registry.md
  - ../../schemas/contracts/v1/watchers/watcher_gate_profile.schema.json
  - ../../schemas/contracts/v1/watchers/watcher_gate_packet.schema.json
  - ../../pipeline_specs/watchers/README.md
  - ../../pipeline_specs/watchers/watcher_gate_profile.v1.json
  - ../../control_plane/watcher_registry.json
  - ../../pipelines/watchers/README.md
  - ../../tools/watchers/README.md
  - ../../fixtures/contracts/v1/watchers/watcher_gate_packet/README.md
  - ../../tools/validators/watchers/validate_watcher_gate_packet.py
  - ../../tests/validators/watchers/test_validate_watcher_gate_packet.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/adr/ADR-0031-shared-watcher-ownership-and-placement.md
notes:
  - "This same-path update replaces the one-byte scaffold at contracts/watchers/README.md with a BOUNDARY_COMPACT routing contract."
  - "Accepted ADR-0029 and its adopted Directory Rules v2 bytes govern placement; ADR-0031 remains proposed and is referenced as a proposal, not adopted authority."
  - "The current direct-child map was read from main at the evidence snapshot; this README does not imply recursive completeness or implementation maturity."
  - "Google Drive and Notion are read-only lineage and coordination surfaces for this update; GitHub repository evidence controls the implementation paths and bytes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/watchers/ — Shared Watcher Semantic-Contract Boundary

> This directory defines what shared watcher contracts mean. It does not activate a source, run a watcher, admit RAW data, approve policy, promote a candidate, release an artifact, notify a user, or publish a claim.

[![Status: proposed inactive](https://img.shields.io/badge/status-proposed%20inactive-d4a72c?style=flat-square)](#status)
[![Authority: semantic meaning](https://img.shields.io/badge/authority-semantic%20meaning-1f6feb?style=flat-square)](#authority-and-inheritance)
[![Boundary: non-publisher](https://img.shields.io/badge/boundary-non--publisher-6e7781?style=flat-square)](#trust-and-safety-boundary)
[![Network: denied](https://img.shields.io/badge/network-denied-b42318?style=flat-square)](#trust-and-safety-boundary)

**Quick navigation:** [Purpose](#purpose) · [Authority and inheritance](#authority-and-inheritance) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Responsibility split](#responsibility-split) · [Finite watcher boundary](#finite-watcher-boundary) · [Trust and safety](#trust-and-safety-boundary) · [Inputs and outputs](#inputs-and-outputs) · [Exposure, mutation, and retention](#exposure-mutation-and-retention) · [Validation](#validation) · [Open verification](#open-verification) · [Rollback](#review-triggers-and-rollback) · [References](#references)

## Purpose

contracts/watchers/ is the semantic-contract lane for shared watcher objects and watcher-gate meaning.

A watcher is a pre-RAW change-signal or candidate-routing capability. It may describe a comparison, materiality classification, gate packet, or bounded candidate outcome, but a detected difference is not domain truth. A watcher candidate remains subordinate to source identity, rights, sensitivity, evidence, policy, review, lifecycle, correction, and release controls.

This boundary exists to keep watcher meaning separate from:

- machine shape and schema validation;
- control-plane identity and registry projection;
- declarative pipeline intent;
- executable orchestration and source access;
- policy decisions and policy rule source;
- synthetic fixtures, tests, validators, and receipts;
- EvidenceBundles, lifecycle instances, release records, and public artifacts.

[Back to top](#top)

## Authority and inheritance

The parent [contracts/](../README.md) root is the canonical responsibility root for human-readable semantic meaning. Accepted ADR-0029 adopts Directory Rules v2 and its three-way split:

| Question | Owning surface |
|---|---|
| What does a watcher object or packet mean? | contracts/watchers/ |
| What machine shape is valid? | schemas/contracts/v1/watchers/ |
| Under what conditions is it allowed, denied, held, restricted, or abstained? | policy/, with the applicable policy family |
| Which identity and non-authority projection is indexed? | control_plane/watcher_registry.json |
| What declarative intent is recorded? | pipeline_specs/watchers/ |
| What executable orchestration runs, if later admitted? | pipelines/watchers/ or a verified domain-owned pipeline lane |
| What reusable helper or validator checks it? | tools/watchers/ and tools/validators/ |

[ADR-0031](../../docs/adr/ADR-0031-shared-watcher-ownership-and-placement.md) records a proposed shared/domain placement split. It remains proposed. Its ownership matrix and admission gates are navigation and review evidence, not permission to move files, activate sources, schedule execution, or create a shared runtime.

[Back to top](#top)

## Status

Current repository evidence was inspected at main@9683ac6cbe385938dbeb66c9f61d82f8de770423 on 2026-09-06 UTC.

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| Target README | Prior blob 8b137891791fe96927ad78e64b0aad7bded08bdc contained one newline byte | This PR is a same-path documentation completion; no prior semantic README text is being silently replaced |
| Direct children | README.md and watcher_gate_packet.md | The map below is direct-child evidence only; child detail stays with the child contract |
| Watcher gate contract | Draft, PROPOSED_INACTIVE, fixture-first, no-network, no-release-authority | It defines a reusable routing packet and threshold vocabulary, not a live watcher |
| Watcher registry contract | Proposed, inactive, no-network, non-publisher | Registry meaning is owned by contracts/source/watcher_registry.md, not this directory |
| Control-plane projection | PROPOSED_INACTIVE with two current entries: one PLACEHOLDER and one INACTIVE | Registry presence indexes identity and references only; all registry authority flags are false |
| Shared watcher ownership | ADR-0031 states proposed | No placement migration or shared-runtime admission is authorized by this README |
| Live operation | No active source, schedule, credential, endpoint, lifecycle writer, release path, notification path, or publication path was established by the inspected contract surfaces | Treat activation and operational maturity as UNKNOWN or NEEDS VERIFICATION until separately evidenced |

The current direct-child map is:

```text
contracts/watchers/
├── README.md                    # this semantic-contract boundary
└── watcher_gate_packet.md       # shared gate-packet meaning; proposed inactive
```

No recursive inventory, active consumer, source admission, production run, or public deployment is inferred from this map.

[Back to top](#top)

## What belongs here

This directory may contain semantic Markdown that defines shared watcher meaning, including:

- watcher-gate packet meaning, finite outcomes, reason-code semantics, obligations, and non-effects;
- shared watcher vocabulary, identity expectations, compatibility promises, and exclusions;
- crosswalks to the paired schemas, inactive profiles, fixtures, validators, tests, policies, registries, and receipts;
- migration or compatibility notes that preserve one canonical meaning and identify rollback;
- bounded explanation of how watcher candidates relate to WORK, QUARANTINE, evidence, review, correction, and release gates.

Every contract added here must state what it means, what it does not prove, which companion surfaces enforce its boundaries, and which authority remains outside the contract root.

[Back to top](#top)

## What does not belong here

| Prohibited concern | Correct responsibility home | Why it stays separate |
|---|---|---|
| JSON Schema or generated machine shape | schemas/contracts/v1/watchers/ | Shape is not semantic prose |
| Watcher identity/register rows | control_plane/watcher_registry.json | A projection cannot self-authorize |
| Declarative watcher profiles/specifications | pipeline_specs/watchers/ or a verified domain lane | Declarations are inactive intent, not contract authority |
| Network access, credentials, source capture, or connectors | connectors/ and governed source surfaces | Contract text must not perform or authorize acquisition |
| Executable comparison or orchestration | pipelines/watchers/ or an accepted domain lane | Runtime ownership needs separate implementation evidence |
| Reusable helpers or validators | tools/watchers/ and tools/validators/ | Helpers check bounded inputs; they do not become source or release authority |
| Policy rule source or policy decisions | policy/ and the governed process/release object | Meaning does not decide admissibility |
| Synthetic fixtures and focused tests | fixtures/ and tests/ | Proof and examples remain independently reviewable |
| Evidence, lifecycle data, receipts, proofs, or release state | data/, release/, and their contract families | A watcher signal is not an EvidenceBundle or release |
| Notifications, maps, APIs, AI summaries, or public claims | Governed runtime/API/UI/release surfaces | Derivatives cannot become root truth |

A README, placeholder, registry row, fixture, passing validator, merged PR, or generated language is not evidence that an inactive watcher became executable or publishable.

[Back to top](#top)

## Responsibility split

The shared watcher family has multiple independent surfaces. The following map is the intended responsibility split evidenced by current paths; it is not a migration order or adoption decision.

| Surface | Current responsibility | Current boundary |
|---|---|---|
| contracts/watchers/ | Shared semantic meaning | This README and watcher_gate_packet.md describe meaning only |
| schemas/contracts/v1/watchers/ | Machine shape | Profile and packet schemas are validated separately |
| pipeline_specs/watchers/ | Inactive shared declarations/profiles | File presence does not activate network, execution, lifecycle writes, release, or publication |
| contracts/source/ | Source-side watcher registry semantics | Registry meaning and source-role references remain outside this object-family lane |
| control_plane/ | Machine governance projection | Current watcher registry is index-only and all authorization flags are false |
| pipelines/watchers/ | Proposed/shared executable orchestration boundary | Existing documentation does not by itself prove an accepted shared runtime |
| tools/watchers/ | Helper/compatibility routing | No scheduler, hidden fetch, or direct publisher is created by this README |
| fixtures/ and tests/ | Synthetic examples and executable proof | Fixtures and tests demonstrate bounded behavior; they do not admit sources |
| data/ and release/ | Lifecycle, receipt, proof, correction, release, and rollback state | Watcher contracts may reference these families but do not write them |

If a future watcher is domain-specific in source-role interpretation, materiality, rights, sensitivity, harmful precision, output meaning, reviewer class, or correction behavior, its semantic contract belongs in the lowest verified domain contract lane. Shared placement requires separately evidenced reuse and accepted migration authority.

[Back to top](#top)

## Finite watcher boundary

The current WatcherGatePacket contract defines a deterministic fixture vocabulary:

| Outcome | Contract-level routing meaning | Authority it does not create |
|---|---|---|
| GREEN | Fixture conditions satisfy the reviewed gate profile; process exit code 0 | No source activation, policy approval, promotion, release, notification, or publication |
| AMBER | Candidate continues only as a steward-review route; process exit code 0 | Not a soft allow and not permission to continue into a public or released state |
| DENY | Fail closed, block the candidate, and route review; process exit code 2 | No evidence closure, lifecycle admission, release decision, or public denial notice |

The gate packet keeps stable reason codes and obligations sorted and duplicate-free for replay. The current profile is fixture-only and no-network. A watcher may produce a bounded candidate or hold signal, but the signal must enter a separately governed process memory or lifecycle boundary.

[Back to top](#top)

## Trust and safety boundary

The contract lane is public metadata only and defaults to fail closed.

It must not contain or expose:

- credentials, bearer material, unrestricted endpoint secrets, or network request instructions;
- source payloads, cached responses, uncontrolled diffs, or generated operational logs;
- exact sensitive geometry or details about living persons, DNA/genomics, archaeology, rare species, protected infrastructure, private land, or other restricted subjects;
- claims that a source is authoritative, rights-cleared, current, safe, or publishable without the corresponding governed evidence and decision;
- instructions that collapse watcher detection into domain truth, EvidenceBundle support, policy approval, or release authority.

Unknown rights, sensitivity, sovereignty, source authority, or harmful precision route to hold, quarantine, abstention, or denial according to the applicable policy and evidence surfaces. A watcher cannot lower those floors by writing a contract or registry row.

[Back to top](#top)

## Inputs and outputs

| Direction | Bounded contract posture |
|---|---|
| Inputs | Semantic vocabulary, references to paired schemas/profiles/policies, and reviewable source or evidence roles; references do not activate or fetch anything |
| Contract outputs | Human-readable meaning, exclusions, compatibility pointers, and review/rollback guidance |
| Candidate outputs outside this root | A later governed implementation may route finite signals to WORK or QUARANTINE and may emit a receipt; this directory cannot perform those writes |
| Prohibited outputs | Direct RAW, PROCESSED, CATALOG, TRIPLET, PUBLISHED, release, notification, public-alert, or deployment writes |

Preserve the lifecycle boundary RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED. A watcher is an upstream candidate signal, not a bypass around admission, evidence, policy, review, correction, or release.


[Back to top](#top)

## Exposure, mutation, and retention

| Concern | Boundary |
|---|---|
| Exposure | Public metadata and maintainer navigation only. Contract prose is not a public data, API, map, AI, notification, or release interface. |
| Mutation | Versioned Markdown changes proceed through repository review. This README cannot mutate the registry, schema, policy, lifecycle, receipt, release, or publication state it references. |
| Retention | Preserve contract history, supersession references, correction context, and rollback pointers. Runtime captures, receipts, proofs, and release records remain in their governed data families; this directory is not a cache or an output store. |

A child contract owns its own semantic detail. This README owns only the directory boundary and cross-root routing.

[Back to top](#top)

## Validation

The README itself is documentation-only. Its presence does not trigger or replace executable validation. The current adjacent bounded lanes are:

```bash
python tools/validators/watchers/validate_watcher_gate_packet.py --fixtures
python -m pytest -q -p no:cacheprovider \
  tests/validators/watchers/test_validate_watcher_gate_packet.py

python tools/validators/validate_watcher_registry.py control_plane/watcher_registry.json
python tools/validators/validate_watcher_registry.py --fixtures
python -m unittest discover --start-directory tests/validators \
  --pattern 'test_validate_watcher_registry.py' --verbose
```

These commands prove only the scopes stated by their validators: closed schema conformance, canonical ordering, deterministic hashes, exact declarative-byte binding, fixture polarity, finite gate classification, and no-network replay. They do not prove source authority, network reachability, scheduler behavior, production execution, EvidenceBundle closure, rights, sensitivity, review, release, or publication.

The existing watcher-registry workflow watches the registry contract, projection, schema, fixtures, validator, tests, pipeline-spec lane, hashing package, and generated registry receipt. Its current path filter does not include this parent README, so a README-only change must not be described as a new registry-validation run.

[Back to top](#top)

## Open verification

- Name and verify the accountable watcher, source, policy, validation, evidence, and release stewards.
- Determine whether the gate profile has two accepted executable consumers; documentation, fixtures, registry rows, and proposed consumers do not satisfy shared-runtime admission.
- Resolve shared-versus-domain placement for watcher specifications without creating two writable authorities.
- Verify source descriptors, rights, sensitivity, sovereignty, endpoint, credential, cadence, security, and reviewer evidence before any activation proposal.
- Bind any future implementation, candidate output, receipt, correction, and rollback record to exact bytes and an accepted lifecycle owner.
- Establish a dedicated review and CI path if watcher-gate changes must be validated independently of the registry workflow.
- Keep ADR-0031 proposed until its acceptance evidence, owner, review separation, migration, and rollback conditions are complete.

[Back to top](#top)

## Review triggers and rollback

Re-review this boundary when the child contract, paired schema/profile, watcher registry, declarative path, executable owner, policy, source role, finite outcomes, sensitivity posture, workflow path filter, receipt family, correction behavior, release gate, or Directory Rules/ADR status changes.

Rollback for this PR is a one-file revert to blob 8b137891791fe96927ad78e64b0aad7bded08bdc, preserving the review and commit history. No source, schedule, credential, lifecycle instance, receipt, release, deployment, notification, or published artifact is changed by this documentation update.

[Back to top](#top)

## References

- Parent semantic root: [contracts/README.md](../README.md)
- Child contract: [watcher_gate_packet.md](./watcher_gate_packet.md)
- Source registry contract: [contracts/source/watcher_registry.md](../source/watcher_registry.md)
- Watcher profile and packet schemas: [schemas/contracts/v1/watchers/](../../schemas/contracts/v1/watchers/)
- Inactive declarations and profiles: [pipeline_specs/watchers/](../../pipeline_specs/watchers/)
- Control-plane projection: [control_plane/watcher_registry.json](../../control_plane/watcher_registry.json)
- Shared pipeline boundary: [pipelines/watchers/README.md](../../pipelines/watchers/README.md)
- Tooling boundary: [tools/watchers/README.md](../../tools/watchers/README.md)
- Fixtures: [fixtures/contracts/v1/watchers/watcher_gate_packet/](../../fixtures/contracts/v1/watchers/watcher_gate_packet/)
- Validator and tests: [tools/validators/watchers/validate_watcher_gate_packet.py](../../tools/validators/watchers/validate_watcher_gate_packet.py) and [tests/validators/watchers/test_validate_watcher_gate_packet.py](../../tests/validators/watchers/test_validate_watcher_gate_packet.py)
- Accepted placement doctrine: [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules v2](../../docs/doctrine/directory-rules.md)
- Proposed watcher ownership record: [ADR-0031](../../docs/adr/ADR-0031-shared-watcher-ownership-and-placement.md)

<p align="right"><a href="#top">Back to top</a></p>
