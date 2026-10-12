<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/repository-topology-correction-register/v1
title: Repository Topology Correction Register Contract
type: semantic-contract
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-09-02
updated: 2026-09-02
policy_label: public; governance; fail-closed
related:
  - ../../docs/adr/ADR-0038-trusted-base-topology-correction-transitions.md
  - ../../control_plane/repository_topology_correction_register.yaml
  - ../../schemas/contracts/v1/governance/repository_topology_correction_register.schema.json
  - ../../tools/validators/directory_governance/validate_repository_topology_correction_register.py
tags: [kfm, governance, topology, correction, register, fail-closed]
[/KFM_META_BLOCK_V2] -->

# Repository Topology Correction Register Contract

## Purpose

`control_plane/repository_topology_correction_register.yaml` is a machine-readable projection of explicitly reviewed frozen-topology correction decisions. It does not create authority and it does not suppress live topology findings.

## Authority boundary

A register entry is consumable only when all of the following are true:

- its `status` is `accepted`;
- its `decision_ref` resolves to an explicitly accepted decision;
- the dependent implementation reads the entry from its trusted base commit;
- the current register bytes are identical to the trusted-base register bytes; and
- the complete exact-transition tuple matches one and only one live transition.

A `proposed`, `rejected`, `revoked`, `expired`, unresolved, current-only, duplicate, ambiguous, or mutated entry fails closed.

## Exact-transition tuple

Every entry binds:

- stable `correction_id`;
- `rule_id` and `subject`;
- one exact repository `path`;
- source fingerprint, source Git blob, and source member count;
- target fingerprint, target Git blob, and target member count;
- exact removed and added evidence members;
- unchanged member count;
- whether equal path sets are required;
- accepted decision reference;
- evidence references and reason code;
- rollback behavior; and
- retirement/reuse behavior.

No field is a wildcard. Consumers must not infer broader permission from a matching path, count, prefix, reason, or issue reference.

## One-use rule

An accepted transition is valid only while the live/trusted source state exactly equals its `from` binding. Once that source fingerprint is absent, reuse is forbidden. A later content correction requires a new reviewed transition.

## Rollback

Control rollback revokes or removes recognition and therefore returns enforcement to fail closed. Content rollback is separate and must never automatically restore a blob identified as known damaged evidence.

## Non-effects

A valid register entry does not:

- suppress KFM-TOPO-004 finding generation;
- reclassify a root;
- authorize unregistered edits;
- authorize deletion, migration, release, deployment, publication, or public-path use;
- change source, policy, evidence, lifecycle, or release authority; or
- permit an entry introduced in the current change to authorize that same change.

## Stage boundary

Stage 1 may define this contract, schema, inert projection, and shape validator. It must not wire this register into `validate_repository_topology.py` or modify the topology baseline. Dependent consumption belongs to a later Stage 2 change starting from a trusted base that already contains an accepted decision and accepted register entry.
