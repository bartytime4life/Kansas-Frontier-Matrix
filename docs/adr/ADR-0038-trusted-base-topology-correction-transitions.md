<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/0038
title: Trusted-Base Exact Transitions for Frozen-Topology Corrections
type: architecture-decision-record
version: v1.2
status: accepted
effective_decision_status: accepted
owners: ["@bartytime4life"]
created: 2026-09-02
updated: 2026-09-14
accepted_on: 2026-09-03
policy_label: public; governance; fail-closed
truth_posture: "ACCEPTED Stage 1 decision / PROPOSED exact register binding / no Stage 2 consumption"
owning_root: docs/
responsibility_root: docs/
current_path: docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md
responsibility: "Record the accepted trusted-base exact-transition mechanism for reviewed frozen-topology corrections without reclassifying a root, weakening KFM-TOPO-004, or authorizing dependent implementation in the same transition."
decision_evidence:
  issue: 4228
  comment_id: 5518331532
  disposition: "ACCEPT STAGE 1 ONLY / TRUSTED-BASE EXACT-TRANSITION MECHANISM / NO STAGE 2 CONSUMPTION"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: d291425a8ca04c0327f2e7c1b3cf3522f3648b0d
  prior_source_blob: c5fa94479263a8e0df20ff47089a00171ffdee0b
  prior_index_blob: c881675b54dcc87e68f2579d09be4062c87db2d3
  refresh_2026_09_14:
    base_ref: main
    base_commit: 7d9074cb741e43fb98dd8b935e08d3a1a3705c7f
    prior_adr_blob: 79f37be0991b050d8bc9c00991d6db887d343cd7
    adr_index_blob: 0c143676dfd3c1bda16cb44398c5ad5d4a49cf67
    correction_register_blob: b48e8df74a2b9d8c2599ce256ef5156687b98dbf
    correction_contract_blob: ca6d673aa7a1d26123dd311f4502fdce953369df
    correction_schema_blob: 0a803b7458d2fa571d60db33d7cafed33f540e61
    correction_register_validator_blob: d94f06e074067338028fb823856de9cc3efb7432
    correction_register_tests_blob: 9bbaf9adca87026a53c36dc153c83595322651cd
    topology_validator_blob: b7cbbb531d74af88ed79cdf8d153d261bcfaa6a3
    stage_1_status: accepted
    stage_1b_register_status: proposed_unbound
    stage_2_consumption: absent_in_re-read_topology_validator
    limits:
      - "This documentation refresh re-read source and coordination entry points only; it did not execute topology, register, hosted, repository-control, runtime, deployment, release, or publication checks."
related:
  - ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../control_plane/repository_topology_correction_register.yaml
  - ../../contracts/governance/repository_topology_correction_register.md
  - ../../schemas/contracts/v1/governance/repository_topology_correction_register.schema.json
  - ../../tools/validators/directory_governance/validate_repository_topology.py
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4228
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4228#issuecomment-5518331532
tags: [kfm, governance, topology, correction, rollback, fail-closed]
notes:
  - "The project-owner decision in issue #4228 comment 5518331532 accepts Stage 1 only and transparently records the single-owner bootstrap exception."
  - "PR #4229 placed the proposed decision, contract, schema, validator, tests, and inert register on main; its merge did not itself accept the decision."
  - "This source-and-index transition records acceptance. The machine register remains proposed with null bindings until a later trusted-main pass can bind a known accepted commit without self-reference."
  - "Stage 2 topology-validator consumption and baseline transition remain a separate change that must start from a trusted base containing both this accepted decision and a later exact accepted register binding."
  - "This decision preserves ADR-0029 and does not reclassify catalog/."
[/KFM_META_BLOCK_V2] -->

# ADR-0038 — Trusted-Base Exact Transitions for Frozen-Topology Corrections

## Status

**Accepted for Stage 1 governance only.** The project-owner decision recorded in [issue #4228 comment 5518331532](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4228#issuecomment-5518331532) accepts the trusted-base exact-transition mechanism described here. The single-owner bootstrap acceptance is explicit; independent review and separation of duties remain `NEEDS VERIFICATION`.

This source record and the canonical ADR index must transition together. Acceptance does **not** make the current inert register consumable, authorize a topology-baseline replacement, or begin Stage 2. The register must be bound later to exact accepted decision bytes and a known accepted commit already present in that later change's trusted base.

### Current repository readback — 2026-09-14

This docs-only refresh re-pinned GitHub implementation evidence at `main@7d9074cb741e43fb98dd8b935e08d3a1a3705c7f`. It preserves the Stage 1 decision and does not reopen, extend, or consume it.

| Surface | Current readback | Boundary |
|---|---|---|
| ADR source and canonical index | ADR blob `79f37be0…`; index blob `0c143676…` | Both continue to record only Stage 1 acceptance |
| Correction register | blob `b48e8df7…`; sole entry `KFM-TOPO-004-CORR-4228-01` is `proposed` with `decision_ref.blob: null` and `accepted_commit: null` | Stage 1B exact binding remains uncompleted |
| Register contract/schema/shape validator | blobs `ca6d673a…` / `0a803b74…` / `d94f06e0…` | The register remains an authority projection with fail-closed shape checks; the validator explicitly does not consume an entry |
| Register tests | blob `9bbaf9ad…` | The test suite specifies that the proposed entry remains inert | This refresh did not execute it |
| Topology validator | blob `b7cbbb53…`; no register or correction-ID consumption symbol was found in the source re-read | No Stage 2 trusted-base consumption is established by the inspected implementation | Source inspection is not a test, deployment, or topology-green result |

The GitHub preflight also found one open pull request, [#4566](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4566), scoped to ADR-0037 only; no branch matching ADR-0038 was present. Those delivery observations are coordination facts only and create no transition authority.

## Context

Accepted ADR-0029 and the Directory Rules classify `catalog/` as a deprecated containment root with immutable, `frozen_no_writes`, and `redirect_only` posture. KFM-TOPO-004 intentionally fingerprints frozen-root evidence as `path@object_id`; therefore a content replacement changes the evidence identity even when path cardinality remains equal.

Issue #4228 records one bounded case where a committed merge-conflict repair correctly changed only `catalog/domain/agriculture/README.md`, replacing damaged blob `bf1a333573c6d068fbb0b695356346003842aceb` with clean blob `4be1711bfa011636ac1c5cd13e7c98e5002ff9c0`. The frozen evidence set remained 43 members, but its fingerprint changed from `sha256:521388927153c91a67ca8cead55af9d688a6064517d109aa556cffca91505006` to `sha256:0ad45247555960029c34d1222365cbe17a5cabec278bf9f6b8f3e9572ea33e8f`.

The topology ratchet must continue to reject unregistered equal-cardinality replacements. A correction must not authorize itself in the same change that introduces or modifies its authority input.

## Decision

KFM permits a frozen-topology content correction only through a **trusted-base exact-transition register** with all of these properties:

1. KFM-TOPO-004 finding construction, `path@object_id` evidence identity, severity, generic baseline non-effects, and existing strict-evidence-shrink behavior remain unchanged.
2. The topology baseline remains an implementation-waiver artifact and does not gain independent correction authority.
3. The machine projection lives at `control_plane/repository_topology_correction_register.yaml` and is referential to this accepted decision.
4. A dependent implementation may consume only a register entry already present in its trusted base commit. An entry added or changed by the current change cannot authorize that change.
5. The current register must be byte-identical to the trusted-base register while a transition is consumed.
6. A transition matches exactly one rule, subject, path, old fingerprint, new fingerprint, old blob, new blob, member counts, and symmetric difference. Missing, stale, duplicate, ambiguous, broadened, or unresolved entries fail closed.
7. A transition is one-use: reuse after its source fingerprint is absent is invalid.
8. Control rollback revokes recognition and restores fail-closed enforcement. It does not automatically restore content bytes.

## Issue #4228 bounded transition

The accepted mechanism is initially scoped to this exact transition:

```text
rule: KFM-TOPO-004
subject: catalog/
path: catalog/domain/agriculture/README.md
from fingerprint: sha256:521388927153c91a67ca8cead55af9d688a6064517d109aa556cffca91505006
from blob: bf1a333573c6d068fbb0b695356346003842aceb
from member count: 43
to fingerprint: sha256:0ad45247555960029c34d1222365cbe17a5cabec278bf9f6b8f3e9572ea33e8f
to blob: 4be1711bfa011636ac1c5cd13e7c98e5002ff9c0
to member count: 43
unchanged members: 42
```

No other path, blob, fingerprint, rule, subject, or evidence delta is implied. The current register entry remains non-consumable until a later Stage 1 binding pass records this accepted ADR's exact Git blob and the known commit in which the source and index acceptance transition became repository history.

## Acceptance boundary and implementation order

1. **Stage 1A — accepted decision source and index:** this record and `docs/adr/INDEX.md` transition together. No register status or topology behavior changes.
2. **Stage 1B — exact machine binding:** after Stage 1A is present on a known trusted main commit, bind the register entry to the accepted ADR blob and that commit; validate the binding without consuming it for a topology transition.
3. **Stage 2 — trusted-base implementation:** only a later change starting from a base that already contains the accepted and bound register may add trusted-base consumption, exact positive and negative proof, and the bounded baseline replacement.

This ordering prevents a branch commit, squash choice, rebase, or current-only authority input from silently becoming its own authorization.

## Consequences

Unregistered edits beneath frozen roots continue to fail. A generic equal-cardinality exception is not introduced. Future corrections require their own reviewed exact entries and accepted authority. The additional Stage 1A/1B split makes the accepted commit binding deterministic before dependent implementation.

## Validation requirements

Before dependent implementation, deterministic proof must cover the exact positive transition and negative cases for absent entry, current-only entry, mutated current register, wrong old/new fingerprint or blob, wrong path, a second changed member, path addition/deletion, cardinality change, wrong rule/subject, non-accepted status, duplicate or ambiguous entries, reuse, and network dependence.

For this Stage 1A transition, validation must confirm source/index status agreement, exact ADR inventory counts, unchanged record identity and path, no register mutation, no topology-validator mutation, and no topology-baseline mutation.

For this documentation refresh, only the source-entry-point readback and exact text-replacement preflight are recorded. Repository-native, hosted, runtime, deployment, release, and publication validation remain unrun and must not be inferred.

## Rollback

Rollback of Stage 1A reverts this ADR and the canonical index to `proposed`; the machine register is already inert and KFM-TOPO-004 remains fail closed. Do not automatically restore `bf1a333573c6d068fbb0b695356346003842aceb`; it contains known merge-conflict damage. Any later content change requires a separately reviewed exact transition.

## Non-effects

This refresh changes this ADR's documentation only. It does not bind `KFM-TOPO-004-CORR-4228-01`, alter its status, populate its decision reference, consume the register, replace a topology baseline, or change the frozen `catalog/` tree.

This decision does not authorize new trust-bearing content under `catalog/`, reclassify any root, weaken KFM-TOPO-004, suppress live findings, authorize deletion or migration, accept a source, change policy, replace the topology baseline, consume the register, release, deploy, publish, or alter repository settings.
