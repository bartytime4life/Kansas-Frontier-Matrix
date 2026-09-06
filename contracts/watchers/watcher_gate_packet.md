<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/watchers/watcher-gate-packet
title: Watcher Gate Packet
type: semantic-contract; watcher-gate; fixture-first
version: v0.1.1
status: draft; proposed-inactive; repository-grounded; fixture-first; no-network; non-publisher; no-release-authority
owners: "OWNER_TBD — Watcher steward · Source steward · Policy steward · Validation steward · Release steward"
created: 2026-08-05
updated: 2026-09-06
supersedes: v0.1.0 at the same path
policy_label: "public; contracts; watchers; deterministic-routing; synthetic; no-network; fail-closed; non-publisher; correction-aware; rollback-aware"
owning_root: contracts/
responsibility: "Define WatcherGatePacket meaning, finite routing semantics, artifact-reference obligations, and non-authority boundaries without becoming schema, source, policy, lifecycle, release, or publication authority."
truth_posture: "CONFIRMED current repository bytes, paired schemas, inactive profile, synthetic fixtures, validator, focused tests, path-scoped no-network workflow, watcher registry boundary, and current-main repin / PROPOSED semantic closure, shared consumer admission, and future activation / UNKNOWN live source, scheduler, endpoint, credentials, production run, consumer, EvidenceBundle, release, and publication effects / NEEDS VERIFICATION current receipt rebinding and independent review of this revision"
current_path: contracts/watchers/watcher_gate_packet.md
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: eaae135d8f4508c0712e3c6e151d7168a46f54ab
  prior_blob: 32f09f1f00ca1781f8c048aacb6faff4399b83fe
  adjacent_directory_readme_blob: c673297e6939663d7becc1e1ed3eeb0f32f1e894
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  profile_schema_blob: 7e3cb0e1d9edd81abd130fa8ce191de55bdf09cb
  packet_schema_blob: dd98657a09a1bb1d356396fab12072410193f164
  profile_instance_blob: fcb4fa6313428b36223b94e2b003dc6ad2430b04
  watcher_registry_blob: 75949f122db983ff3ea4e6d72162f7da10c498ea
  watcher_gate_workflow_blob: c13e8efbda0178e16334f995bd915bbc68b087e9
  fixture_readme_blob: 2826b7c087f2ecc5f797b35a8ae5d68a423ac080
  validator_blob: 4a115ccf20ab95a397ada6e30f375d10254ff7c9
  focused_test_blob: 75a5f49e944301dba2839a1a9f9db1b7a4a1bbb5
  generated_receipt_blob: 8de6b5e83e221550bcf650136c259f5a0016c71c
related:
  - ./README.md
  - ../../schemas/contracts/v1/watchers/watcher_gate_profile.schema.json
  - ../../schemas/contracts/v1/watchers/watcher_gate_packet.schema.json
  - ../../pipeline_specs/watchers/watcher_gate_profile.v1.json
  - ../../fixtures/contracts/v1/watchers/watcher_gate_packet/
  - ../../tools/validators/watchers/validate_watcher_gate_packet.py
  - ../../tests/validators/watchers/test_validate_watcher_gate_packet.py
  - ../../.github/workflows/watcher-gate-packet.yml
  - ../../data/receipts/generated/genrec-watcher-gate-packet-20260805.json
  - ../source/watcher_registry.md
  - ../../control_plane/watcher_registry.json
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/adr/ADR-0031-shared-watcher-ownership-and-placement.md
notes:
  - "This same-path update reconciles contract currentness and documents existing bounded behavior; it does not change the profile, schemas, fixtures, validator, workflow, registry, receipt, or runtime."
  - "Accepted ADR-0029 and its repository-pinned Directory Rules bytes govern placement. ADR-0031 remains proposed and is navigation/review evidence only."
  - "The adjacent directory README has its own earlier evidence snapshot; this document repins current main and does not treat that embedded snapshot as the current implementation base."
  - "The generated receipt is a pre-update authoring receipt whose artifact hash binds the prior contract bytes; a separate receipt-rebinding step is required before a green exact-head watcher workflow can be claimed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Watcher Gate Packet

> Define the meaning of a deterministic watcher prefilter, score, finite routing
> decision, artifact references, exit code, and stewardship obligations without
> turning a candidate signal into source, policy, lifecycle, release, or
> publication authority.

[![Status: proposed inactive](https://img.shields.io/badge/status-proposed%20inactive-d4a72c?style=flat-square)](#status)
[![Boundary: non-publisher](https://img.shields.io/badge/boundary-non--publisher-6e7781?style=flat-square)](#trust-boundary-and-non-effects)
[![Network: denied](https://img.shields.io/badge/network-denied-b42318?style=flat-square)](#trust-boundary-and-non-effects)

## Status

This is a documentation-only currentness reconciliation of the existing
fixture-first WatcherGatePacket contract. It preserves the v0.1.0 finite
vocabulary and its inactive posture.

| Field | Current bounded state |
|---|---|
| Repository authority | GitHub main@eaae135d8f4508c0712e3c6e151d7168a46f54ab |
| Prior target bytes | Blob 32f09f1f00ca1781f8c048aacb6faff4399b83fe at this path |
| Contract state | draft; PROPOSED_INACTIVE; fixture-first; no-network; no-release-authority |
| Semantic owner | contracts/watchers/ |
| Machine-shape owners | schemas/contracts/v1/watchers/ |
| Declarative profile | pipeline_specs/watchers/watcher_gate_profile.v1.json, PROPOSED_INACTIVE |
| Runtime posture | No accepted shared executable watcher, scheduler, live source, credential, or endpoint is established by these surfaces |
| Change scope | This Markdown contract only; no schema, profile, fixture, validator, workflow, registry, receipt, or runtime bytes are changed by this revision |

A passing fixture validator, workflow, merged commit, registry row, or generated
receipt is not source activation, policy approval, promotion, release,
deployment, notification, or publication.

## Purpose

The packet is the semantic boundary for a watcher candidate that normalizes
prefilter facts, a bounded score, references to separately governed artifacts,
a finite routing decision, an exit code, stable reason codes, and stewardship
obligations.

It adopts only the reusable routing meaning and inactive threshold vocabulary
already represented by the paired repository artifacts. It does not adopt a
live endpoint, source, dataset, network probe, scheduler, policy engine,
EvidenceBundle, lifecycle writer, release action, or publication action.

## Responsibility split

Directory Rules separates semantic meaning from machine shape, admissibility,
instances, execution, and release state:

| Responsibility | Canonical surface | Boundary |
|---|---|---|
| Shared watcher-gate meaning | contracts/watchers/ | This contract explains object meaning and finite routing semantics |
| Machine shape | schemas/contracts/v1/watchers/ | JSON Schema validates structure and closed vocabularies |
| Inactive threshold intent | pipeline_specs/watchers/ | The profile records declarative values; presence does not activate execution |
| Synthetic examples | fixtures/contracts/v1/watchers/ | Valid and exact-negative packets exercise bounded behavior |
| Reusable validation | tools/validators/watchers/ | The validator checks bounded files; it is not a scheduler or publisher |
| Focused proof | tests/validators/watchers/ | Tests protect the finite no-network boundary |
| CI orchestration | .github/workflows/watcher-gate-packet.yml | Read-only hosted checking; no lifecycle or release effect |
| Watcher identity projection | control_plane/watcher_registry.json | Index-only identity and non-authority state; not activation authority |
| Registry semantic contract | contracts/source/watcher_registry.md | Source-side registry meaning; not this packet's machine shape |
| Release and correction decisions | release/ | Separate governed transition; never emitted directly by this packet |

The slice creates no new root and no parallel source, policy, evidence,
receipt, proof, release, or publication authority.

## Packet meaning

A WatcherGatePacket contains the following semantic fields:

| Field group | Required meaning |
|---|---|
| Identity | packet_id, watcher_id, schema_version, and a packet spec_hash bind the candidate to a deterministic object identity |
| Profile binding | profile_id, profile_version, and the profile spec_hash identify the inactive threshold profile used for routing |
| Prefilter facts | items_found, asset_missing_count, missing_etag, and nullable median_cloud_percent are the bounded facts consumed by the profile |
| Artifact references | prefilter_report_ref, feature_vector_ref, scorecard_ref, policy_report_ref, and run_receipt_ref point to separately governed artifacts; their contents are not embedded here |
| Routing result | score, decision, process_exit_code, sorted unique reason_codes, and sorted unique obligations make the outcome replayable |
| Assessment time | assessed_at records a timezone-qualified date-time |
| Governance guard | source_activated, policy_evaluated, promotion_authorized, and public_use_allowed remain false; release_ref remains null |

The packet's artifact references are bounded locators, not proof that the
referenced artifacts exist, are rights-cleared, are authoritative, or support
an EvidenceBundle. Resolution and admission belong to their owning contracts,
schemas, policy, evidence, lifecycle, and release surfaces.

## Inactive profile

The current profile instance is:

- profile_id: kfm://watcher-gate-profile/default-v1
- profile_version: 1.0.0
- spec_hash: sha256:5425aabbc7fefa74e9535785f80aaf2a378bdefb50bfc11957fc3ae7984b2cf6
- canonicalization_profile: kfm-canonical-json-v1
- status: PROPOSED_INACTIVE

The reviewed fixture thresholds are:

| Condition | Routing outcome | Exit | Stable reason code | Obligation |
|---|---|---:|---|---|
| asset_missing_count > 0 | DENY | 2 | ASSET_MISSING | BLOCK_PROMOTION, ROUTE_STEWARD_REVIEW |
| median_cloud_percent > 40.0 | DENY | 2 | MEDIAN_CLOUD_TOO_HIGH | BLOCK_PROMOTION, ROUTE_STEWARD_REVIEW |
| items_found == 0 | DENY | 2 | NO_ITEMS | BLOCK_PROMOTION, ROUTE_STEWARD_REVIEW |
| score < 50 | DENY | 2 | SCORE_BELOW_DENY | BLOCK_PROMOTION, ROUTE_STEWARD_REVIEW |
| No hard deny and missing_etag == true | AMBER | 0 | MISSING_ETAG | ROUTE_STEWARD_REVIEW |
| No hard deny and score < 80 | AMBER | 0 | SCORE_AMBER | ROUTE_STEWARD_REVIEW |
| No hard deny, no amber condition, and score >= 80 | GREEN | 0 | ALL_GATES_GREEN | None |

When multiple hard-deny facts apply, one DENY packet carries every applicable
stable reason code. The validator requires unique, canonical ordering and the
full fail-closed obligation set. AMBER is a held steward-review route, not a
soft allow. GREEN means only that the reviewed fixture conditions satisfy this
inactive local profile.

## Deterministic packet rules

The paired schemas are closed objects with no undeclared properties. The
validator additionally establishes the bounded replay rules:

- JSON must be UTF-8, one object, within the validator's size limit, and free of
  duplicate keys and non-finite numbers.
- The profile and packet spec_hash values must match the validator's canonical
  SHA-256 calculation with the hash field omitted from the hashed object.
- Artifact references use the bounded kfm:// or fixture:// reference forms;
  packet contents are not inlined.
- Reason codes and obligations are unique and canonically ordered.
- A packet's decision, exit code, reasons, obligations, and profile thresholds
  must agree.
- Symlink inputs, missing files, unreadable files, malformed JSON, schema
  findings, placeholder digests, and governance escalation fail closed.
- The fixture CLI reports bounded outcomes without echoing artifact references.

These are validator and schema boundaries. They do not prove network isolation
of an uninspected future implementation, source correctness, rights closure,
policy adoption, human review, or release readiness.

## Finite behavior

| Decision | Process behavior | Meaning |
|---|---|---|
| GREEN | exit 0; no obligations | Reviewed fixture conditions satisfy the inactive profile |
| AMBER | exit 0; route ROUTE_STEWARD_REVIEW | Candidate is held for stewardship; it is not approved |
| DENY | exit 2; block and route review | Candidate fails closed and is non-promotable |

No finite outcome authorizes source activation, RAW admission, policy approval,
promotion, EvidenceBundle creation, catalog or triplet mutation, release,
notification, deployment, or publication.

## Trust boundary and non-effects

This contract:

- performs no network request and activates no source;
- does not schedule, execute, or authorize a watcher;
- does not evaluate adopted policy; policy_evaluated stays false;
- does not write RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS,
  PUBLISHED, or release state;
- does not resolve EvidenceRef or create EvidenceBundle support;
- does not create a PromotionDecision, ReleaseManifest, correction,
  withdrawal, rollback, issue, notification, map layer, API response, or public
  claim;
- keeps source_activated, promotion_authorized, and public_use_allowed
  false, and keeps release_ref null.

The packet is a candidate-routing object. A watcher signal is not domain truth,
a source registry activation, a policy decision, a RunReceipt proof, or a
release decision.

## Current companion surfaces

| Surface | Current repository evidence | Bounded meaning |
|---|---|---|
| schemas/contracts/v1/watchers/watcher_gate_profile.schema.json | WatcherGateProfile, PROPOSED_INACTIVE, closed object | Profile shape only |
| schemas/contracts/v1/watchers/watcher_gate_packet.schema.json | WatcherGatePacket, GREEN/AMBER/DENY, closed object | Packet shape and vocabulary only |
| pipeline_specs/watchers/watcher_gate_profile.v1.json | Inactive profile; all governance flags false; release_ref: null | Declarative threshold intent only |
| fixtures/contracts/v1/watchers/watcher_gate_packet/ | Three valid packets and five exact-negative packets with expected manifests | Synthetic polarity and fail-closed examples only |
| tools/validators/watchers/validate_watcher_gate_packet.py | Deterministic schema, hash, semantic, parser, and fixture checks | Bounded checker; no hidden fetch or publication |
| tests/validators/watchers/test_validate_watcher_gate_packet.py | Focused tests for valid/invalid packets, governance, ordering, parser safety, and CLI output | Executable boundary evidence only |
| .github/workflows/watcher-gate-packet.yml | Path-scoped PR/push/dispatch workflow; KFM_NO_NETWORK=1; contents read-only | Hosted validation only |
| control_plane/watcher_registry.json | Two entries: one shared PLACEHOLDER, one Soil INACTIVE; registry governance flags are false | Index and non-authority projection; not this gate's activation record |
| docs/adr/ADR-0031-shared-watcher-ownership-and-placement.md | proposed; shared runtime absent; receipt closure held | Placement proposal and review context, not accepted authority |
| data/receipts/generated/genrec-watcher-gate-packet-20260805.json | Historical authoring receipt; prior packet bytes are hash-bound | Lineage and prior validation record; not a current-head pass for this revision |

The current watcher family remains inactive and partially unresolved. The
registry, profile, contract, fixtures, validator, and workflow form a bounded
proof slice; they do not establish a live watcher.

## Validation boundary

The dedicated workflow currently:

1. installs declared Python test dependencies;
2. runs the focused watcher-gate tests;
3. replays valid and exact-negative fixtures with --fixtures;
4. validates the generated authoring receipt;
5. emits a review-only summary.

The latest current-main push at eaae135d8f4508c0712e3c6e151d7168a46f54ab
recorded contracts-validate success (run 34045268724), docs-meta-block
success (run 34045268821), docs-control-plane queued (run 34045268640), and
link-check pending (run 34045268730). That push did not change a watcher-gate
path, so no exact-current-main watcher-gate-packet execution is claimed here. The dedicated PR workflow is the relevant exact-head evidence for
this revision.

A green focused result would prove only schema shape, profile and packet
self-hash integrity, deterministic classification, fixture polarity, parser
fail-closed behavior, and the no-network test boundary. It would not prove
source authority, rights, sensitivity safety, live reachability, production
execution, policy approval, review completion, release, deployment, or
publication.

## Open verification and follow-up

- The current generated receipt binds the pre-update contract hash
  sha256:8bfc1241d912b117d88cd481971c6abf641154d9562fcf9dcdd1a7ba023cd307.
  This Markdown revision intentionally does not rewrite that historical receipt.
  A separately reviewable receipt-rebinding step is required before claiming
  exact-head receipt validation for the updated bytes.
- No accepted shared executable watcher, scheduler, credential, endpoint,
  source activation, production run, consumer, EvidenceBundle, release path, or
  public effect was established.
- ADR-0031 remains proposed. The registry's PLACEHOLDER and INACTIVE entries do
  not grant activation, execution, promotion, release, or publication authority.
- The profile's future consumers, owner/steward assignments, rights and
  sensitivity closure, correction propagation, and independent review remain
  unresolved.
- The adjacent directory README and older source-derived proposal provide
  navigation and lineage; neither replaces the current repository bytes or
  accepts this contract.

## Rollback

Before merge, close the draft pull request and abandon its branch. After an
authorized merge, revert the additive contract commit while preserving the
historical receipt and review record. No live source, lifecycle record,
external notification, release, deployment, or published artifact requires
restoration.

## References

- [contracts/watchers/README.md](./README.md)
- [watcher_gate_profile.schema.json](../../schemas/contracts/v1/watchers/watcher_gate_profile.schema.json)
- [watcher_gate_packet.schema.json](../../schemas/contracts/v1/watchers/watcher_gate_packet.schema.json)
- [watcher_gate_profile.v1.json](../../pipeline_specs/watchers/watcher_gate_profile.v1.json)
- [watcher-gate packet fixtures](../../fixtures/contracts/v1/watchers/watcher_gate_packet/)
- [validate_watcher_gate_packet.py](../../tools/validators/watchers/validate_watcher_gate_packet.py)
- [watcher-gate packet tests](../../tests/validators/watchers/test_validate_watcher_gate_packet.py)
- [watcher-gate-packet workflow](../../.github/workflows/watcher-gate-packet.yml)
- [contracts/source/watcher_registry.md](../source/watcher_registry.md)
- [control_plane/watcher_registry.json](../../control_plane/watcher_registry.json)
- [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [ADR-0031](../../docs/adr/ADR-0031-shared-watcher-ownership-and-placement.md)

## Change history

| Version | Date | Change |
|---|---|---|
| v0.1.1 | 2026-09-06 | Re-pinned the semantic contract to current main, aligned its responsibility split with the adjacent watcher boundary, documented the current inactive profile/registry/fixture/validator surfaces, and preserved the receipt as pre-update lineage. |
| v0.1.0 | 2026-08-05 | Introduced the fixture-first watcher-gate packet, finite routing vocabulary, no-network boundary, focused validator/test command, and rollback posture. |

<p align="right"><a href="#top">Back to top</a></p>
