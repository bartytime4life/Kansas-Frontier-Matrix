<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/path-alias-register/v1
title: Path Alias Register Contract
type: semantic-contract
version: v1.1
status: draft
owners: ["@bartytime4life"]
created: 2026-08-07
updated: 2026-08-18
policy_label: public
owning_root: contracts/
responsibility: Define the semantic boundary for machine-readable compatibility path and identity projections without granting migration, write, retirement, release, or publication authority.
truth_posture: CONFIRMED current register shape, accepted Directory Rules binding, and bounded tombstone semantics / NEEDS VERIFICATION consumer closure and external references
related:
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/architecture/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../control_plane/root_registry.yaml
  - ../../control_plane/path_alias_register.yaml
  - ../../schemas/contracts/v1/governance/path_alias_register.schema.json
  - ../../tools/validators/directory_governance/validate_path_alias_register.py
tags: [kfm, governance, directory-rules, compatibility, aliases, single-write, migration, tombstone]
notes:
  - "A validated alias entry projects an accepted compatibility decision. It does not accept an ADR, authorize writes, move bytes, close consumers, create or remove a tombstone, retire a path, or grant release/publication status."
  - "v1.1 records the bounded Directory Rules architecture-path tombstone while preserving open consumer closure and the prior full-body rollback reference."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Path Alias Register Contract

## Purpose

The `PathAliasRegister` is the machine-readable projection for accepted KFM compatibility paths and identity aliases. It records how an old path or identifier resolves to one canonical target while keeping authority, writes, migration state, consumer evidence, parity checks, and rollback visible.

The register prevents compatibility from becoming parallel authority. Verified consumers may require a legacy path, redirect, tombstone, or one-way mirror, but every authoritative write remains at the canonical target.

## Authority boundary

The register projects accepted doctrine and decisions. It cannot:

- accept, amend, or supersede an ADR;
- create a compatibility path or make one canonical;
- authorize writes at an alias path;
- declare consumers closed without evidence;
- move, replace, tombstone, restore, retire, or delete repository bytes;
- approve review, release, deployment, promotion, or publication.

A validator `PASS` means only that the projection is internally consistent with its pinned doctrine, Root Registry, repository paths, blobs, and digests.

## Required register binding

The register binds:

- the adopted Directory Rules path, identity, SHA-256, and `ADR-0029`;
- the exact Root Registry SHA-256 and pinned base reference;
- the repository base at which the alias inventory was authored;
- owner, reviewers, scope, non-effects, and one or more alias entries.

Every entry repeats the adopted doctrine digest so consumers can detect stale or independently edited projections.

## Compatibility entry

Each alias entry records:

- a stable alias ID and compatibility class;
- old path and canonical target;
- object family and identity mapping;
- reason, accepted decision, rule IDs, and source digest;
- registered alias and target roots;
- verified canonical writers and an empty alias-writer set;
- consumer evidence and closure state;
- read rule and canonical-only write rule;
- generation or synchronization method;
- owner, reviewers, start date, expiry, and exit criteria;
- parity-validation references;
- rollback or forward-fix behavior;
- alias-versus-target exposure and mutation posture;
- body mode, current alias Git blob when bound, canonical digest, and verification state.

## Compatibility classes

### `legacy`

Former canonical material retained read-only while consumers and references migrate. The body may be a frozen legacy body or a bounded tombstone. Synchronization is `none_frozen`; writes remain canonical-only.

### `mirror`

A generated one-way projection of canonical content. A mirror is non-authoritative, generated, and cannot become an independent writer.

### `external_export`

A shape or path required by a verified downstream consumer. The export is generated or manually produced from the canonical source and remains no more permissive than its target.

### `transitional`

A temporary cutover path with bounded dual-read and canonical-only writes. Exit criteria and rollback are mandatory.

### `deprecated`

A read-only redirect or tombstone scheduled for retirement. It cannot contain a separately editable authority body.

## Current Directory Rules alias

The accepted initial alias remains:

- old path: `docs/architecture/directory-rules.md`;
- canonical target: `docs/doctrine/directory-rules.md`;
- canonical identity: `kfm://doctrine/directory-governance/v2`;
- superseded IDs: `kfm://doc/directory-rules` and `kfm://doc/doctrine/directory-rules`;
- write posture: `canonical_only`, with zero alias writers;
- read posture: `canonical_only_with_redirect`;
- body mode: bounded `tombstone`;
- rollback reference: the prior full-body Git blob;
- consumer closure: `OPEN`;
- verification state: `PARTIAL`.

The tombstone records Phase 1 of the ADR-0029 compatibility migration. It does not prove Phase 2 reference closure or authorize physical deletion.

The register deliberately does not invent aliases for other compatibility or drift surfaces. Those require their own accepted decisions and migration evidence.

## Validator invariants

The deterministic no-network validator checks:

- strict JSON-compatible YAML and Draft 2020-12 shape;
- exact adopted Directory Rules and Root Registry bindings;
- accepted-decision evidence;
- canonical ordering and unique alias, path, and identity keys;
- registered roots and active canonical target roots;
- object-family compatibility with the target root;
- no alias writers and at least one canonical writer;
- no alias chains or self-targets;
- no alias exposure or mutation more permissive than the target;
- class-specific read, body, and synchronization semantics;
- expiry, exit, parity, consumer, and rollback fields;
- current path existence, alias Git-blob continuity, canonical SHA-256, and tombstone size when repository checks are enabled;
- non-echoing bounded diagnostics for malformed or untrusted input.

Finite outcomes are `PASS`, `FAIL_NEW_DRIFT`, `FAIL_INVARIANT`, `HOLD_UNRESOLVED`, and `ERROR_VALIDATOR`.

## Migration relationship

The alias register is not a migration manifest. A path-changing change still needs reviewed before/after identities, producers, consumers, compatibility mode, validation, correction, and rollback or forward-fix evidence.

Moving from a full legacy body to a tombstone changes the alias bytes and body mode but does not close consumers. Moving from a tombstone to physical deletion requires separate zero-writer, zero-consumer, link-closure, and retirement-receipt evidence.

## Rollback

A tombstone rollback restores the prior body only through a reviewed revert or forward fix that preserves one canonical writer. Re-run schema, repository-parity, metadata, link, topology, workflow-security, and generated-receipt validation after any correction.

Rolling back this contract or projection does not alter accepted `ADR-0029`, the adopted Directory Rules bytes, the Root Registry, or publication state.

[Back to top](#top)
