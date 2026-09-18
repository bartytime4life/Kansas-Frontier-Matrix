<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/0038
title: Trusted-Base Exact Transitions for Frozen-Topology Corrections
type: architecture-decision-record
version: v1.3
status: accepted
effective_decision_status: accepted
owners: ["@bartytime4life"]
created: 2026-09-02
updated: 2026-09-17
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

## Proposed exact-version disposition — 2026-09-17

**PROPOSED; owner acceptance and independent review are pending.** The accepted
Stage 1 decision above still covers only the original Agriculture correction.
This section supplies a concrete decision candidate for the eight replacements
currently responsible for the topology failure on PR #4622. Preparing this
proposal does not accept these versions or extend the existing decision.

### Decision requested

Accept the eight exact README replacements below as one bounded containment
correction set, preserving the existing 43-path frozen catalog inventory and
its other 35 blobs. The proposed target is the already tracked catalog state at
`main@eaff4f86e1f6b4398bbfc95c06df66e4a2f7364a`; no additional catalog edit is
included. Acceptance would extend the permitted correction scope beyond the
single Agriculture replacement in the original Stage 1 decision. Each row
requires an explicit accept/reject/hold disposition; accepting only a subset
requires a new aggregate fingerprint and separately reviewed proposal.

| Catalog member | Frozen baseline blob | Proposed accepted blob |
| --- | --- | --- |
| [`catalog/STAC/README.md`](../../catalog/STAC/README.md) | `198a970db9e71b2dc7f5cdbf171b14c0f9a878ce` | `c2e327dafbabec3cd6cc185f690fbcf4f227ca11` |
| [`catalog/domain/README.md`](../../catalog/domain/README.md) | `fd4826b2b5e54672796b840d2664b5947d4054ec` | `ad9e2406a75746d96b0f8494a2fc0696cfc583c7` |
| [`catalog/domain/agriculture/README.md`](../../catalog/domain/agriculture/README.md) | `bf1a333573c6d068fbb0b695356346003842aceb` | `4be1711bfa011636ac1c5cd13e7c98e5002ff9c0` |
| [`catalog/index/README.md`](../../catalog/index/README.md) | `3898725a2e3311222020c66099ae4a09f806ea5e` | `11cb956e56189ed1c618d577158df2b280d21d91` |
| [`catalog/manifest/README.md`](../../catalog/manifest/README.md) | `9fe630fe18decc275d26ad99c5c7e2ac215d18ca` | `b4493e247b626eab4db94ba7c030ad5dd67ce785` |
| [`catalog/proof/README.md`](../../catalog/proof/README.md) | `2e602944895f26229f41db2b17a603a4be4fafc1` | `0d82fcc28cf149e5160b38915612dca767306a43` |
| [`catalog/publication/README.md`](../../catalog/publication/README.md) | `7f37e6efab211e63eb3ae237adda8551dd640afd` | `d30392e9b27af050048d595077a4c71456b8be1b` |
| [`catalog/triplet/README.md`](../../catalog/triplet/README.md) | `270725cc2e907a4f94d928f7c71759f4b6becd0b` | `2bd84c5a9142d3f7a63e8ae1c2cc9296043afc4b` |

### Exact evidence boundary

- Repository base: `eaff4f86e1f6b4398bbfc95c06df66e4a2f7364a`.
- Baseline file Git blob: `b01cb6ec58d5ae306e8afd7858c5fcc70a03d9ec`.
- Baseline file SHA-256: `91eb4e7caf8c00f995bfe9cb7d639a6631ccda724bee234ec266ec718a576868`.
- Rule and subject: `KFM-TOPO-004`, `catalog/`.
- Source fingerprint: `sha256:521388927153c91a67ca8cead55af9d688a6064517d109aa556cffca91505006`.
- Source evidence SHA-256: `sha256:8241bb4f1da8abfa669d201fda804f875922ea27338e15af47bf5362edf0525b`.
- Target fingerprint: `sha256:71a120ae8ca2b69896266c9ddd52f6d03577ea91fa2de4390b7d57b9ceeb912f`.
- Target evidence SHA-256: `sha256:304b679f591315a09c358d2aa286d5ed9f2910679d8f6ed39790b2c7f6811e9c`.
- Cardinality: 43 members before and after; eight replacements; 35 unchanged;
  zero path additions or removals.

The source member set is the decoded `evidence_zlib_base64` value of the exact
`catalog/` entry in the pinned baseline file. Substituting only the eight rows
above reconstructs the proposed target; any ninth edit, changed path, or altered
blob must fail. The baseline's generic implementation-waiver role is unchanged.

The Agriculture source blob contains merge-conflict damage. Automatic recovery
must not restore it. The other seven replacements are separate containment
README revisions; the existing Agriculture-only register cannot authorize them.
The proposal requests retention of the current exact bytes, not retroactive
approval of prior PR transitions or endorsement of every statement as runtime
fact. Content review of all eight versions remains part of the owner decision.

### Review and implementation sequence

1. Review the eight exact old/new blobs and record the owner disposition plus
   directory-governance/control review. A draft PR or merge event alone is not
   acceptance. Record any independent-review limitation explicitly.
2. In a separate acceptance transition, record the accepted source/index state
   and exact eight-member scope. Preserve the original Stage 1 decision history.
3. From a later trusted base containing that acceptance, bind the complete
   correction set to the accepted decision blob and known commit. The existing
   singleton projection is insufficient; its schema/contract representation
   must be reviewed for exact-set coverage before it becomes consumable.
4. In a later implementation PR, consume only a byte-identical trusted-base
   binding and perform the bounded baseline transition. Add positive coverage
   for this exact set and negatives for absent/current-only/mutated bindings,
   wrong base/head/digest/path, partial sets, ninth edits, new/deleted paths,
   non-accepted or ambiguous records, and replay. No network is required for
   the deterministic validator.

Repository-control readiness authorization remains separate and bound to the
actual PR base/head. This proposal leaves the current correction register,
contracts, schemas, topology validator, topology baseline, and catalog files
unchanged. The live topology check is expected to remain nonzero until the
subsequent accepted binding and consumer are implemented.

### Reproduction and rollback

The reported [validator-suite job](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/35262897229/job/105342754023)
failed at `make repository-topology`: one new `catalog/` finding, one stale
baseline entry, 124 baselined warnings and zero invariant findings. Direct local
replay of `validate_repository_topology.py` reproduced the same fingerprint.
[Issue #4228](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4228)
records the unresolved exact-delta acceptance and trusted-base dependency.

Rollback of this proposal removes this section and restores its prior metadata;
no catalog bytes or machine authority need rollback. After any future acceptance,
revocation must restore denial rather than copy historical content back. Later
content corrections require their own exact reviewed transition.

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
