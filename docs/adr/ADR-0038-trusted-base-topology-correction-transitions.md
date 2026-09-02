<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/0038
title: Trusted-Base Exact Transitions for Frozen-Topology Corrections
type: architecture-decision-record
version: v1.0
status: proposed
owners: ["@bartytime4life"]
created: 2026-09-02
updated: 2026-09-02
policy_label: public; governance; fail-closed
truth_posture: repository-grounded proposal; no implementation authority until explicitly accepted
related:
  - ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../control_plane/repository_topology_correction_register.yaml
  - ../../contracts/governance/repository_topology_correction_register.md
  - ../../schemas/contracts/v1/governance/repository_topology_correction_register.schema.json
  - ../../tools/validators/directory_governance/validate_repository_topology.py
  - https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4228
tags: [kfm, governance, topology, correction, rollback, fail-closed]
notes:
  - "PROPOSED only. Merge alone does not accept this decision."
  - "This decision preserves ADR-0029 and does not reclassify catalog/."
[/KFM_META_BLOCK_V2] -->

# ADR-0038 — Trusted-Base Exact Transitions for Frozen-Topology Corrections

## Status

**Proposed.** This record has no dependent implementation authority until its status is explicitly reviewed and changed to `accepted` together with the canonical ADR index and exact decision bindings.

## Context

Accepted ADR-0029 and the Directory Rules classify `catalog/` as a deprecated containment root with immutable, `frozen_no_writes`, and `redirect_only` posture. KFM-TOPO-004 intentionally fingerprints frozen-root evidence as `path@object_id`; therefore a content replacement changes the evidence identity even when path cardinality remains equal.

Issue #4228 records one bounded case where a committed merge-conflict repair correctly changed only `catalog/domain/agriculture/README.md`, replacing damaged blob `bf1a333573c6d068fbb0b695356346003842aceb` with clean blob `4be1711bfa011636ac1c5cd13e7c98e5002ff9c0`. The frozen evidence set remained 43 members, but its fingerprint changed from `sha256:521388927153c91a67ca8cead55af9d688a6064517d109aa556cffca91505006` to `sha256:0ad45247555960029c34d1222365cbe17a5cabec278bf9f6b8f3e9572ea33e8f`.

The topology ratchet must continue to reject unregistered equal-cardinality replacements. A correction must not authorize itself in the same change that introduces or modifies its authority input.

## Decision

If accepted, KFM will permit a frozen-topology content correction only through a **trusted-base exact-transition register** with all of these properties:

1. KFM-TOPO-004 finding construction, `path@object_id` evidence identity, severity, generic baseline non-effects, and existing strict-evidence-shrink behavior remain unchanged.
2. The topology baseline remains an implementation-waiver artifact and does not gain independent correction authority.
3. The machine projection lives at `control_plane/repository_topology_correction_register.yaml` and is referential to an accepted decision.
4. A dependent implementation may consume only a register entry already present in its trusted base commit. An entry added or changed by the current change cannot authorize that change.
5. The current register must be byte-identical to the trusted-base register while a transition is consumed.
6. A transition matches exactly one rule, subject, path, old fingerprint, new fingerprint, old blob, new blob, member counts, and symmetric difference. Missing, stale, duplicate, ambiguous, broadened, or unresolved entries fail closed.
7. A transition is one-use: reuse after its source fingerprint is absent is invalid.
8. Control rollback revokes recognition and restores fail-closed enforcement. It does not automatically restore content bytes.

## Issue #4228 bounded transition

The initial projection may document, but while this ADR is proposed may not authorize, exactly this transition:

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

No other path, blob, fingerprint, rule, subject, or evidence delta is implied.

## Consequences

Unregistered edits beneath frozen roots continue to fail. A generic equal-cardinality exception is not introduced. Future corrections require their own reviewed exact entries and accepted authority. Two-stage delivery is required: authority first, dependent consumption later from a trusted base.

## Validation requirements

Before dependent implementation, deterministic proof must cover the exact positive transition and negative cases for absent entry, current-only entry, mutated current register, wrong old/new fingerprint or blob, wrong path, a second changed member, path addition/deletion, cardinality change, wrong rule/subject, non-accepted status, duplicate or ambiguous entries, reuse, and network dependence.

## Rollback

Rollback of the mechanism means revoking or reverting transition recognition so KFM-TOPO-004 blocks again. Do not automatically restore `bf1a333573c6d068fbb0b695356346003842aceb`; it contains known merge-conflict damage. Any later content change requires a separately reviewed exact transition.

## Non-effects

This decision does not authorize new trust-bearing content under `catalog/`, reclassify any root, weaken KFM-TOPO-004, suppress live findings, authorize deletion or migration, accept a source, change policy, release, deploy, publish, or alter repository settings.
