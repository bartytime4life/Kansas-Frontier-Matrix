<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/path-alias-register/v1
title: Path Alias Register Contract
type: semantic-contract
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-08-07
updated: 2026-08-07
policy_label: public
related:
  - "../../docs/doctrine/directory-rules.md"
  - "../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md"
  - "../../control_plane/root_registry.yaml"
  - "../../control_plane/path_alias_register.yaml"
  - "../../schemas/contracts/v1/governance/path_alias_register.schema.json"
  - "../../tools/validators/directory_governance/validate_path_alias_register.py"
tags: [kfm, governance, directory-rules, compatibility, aliases, single-write, migration]
notes:
  - "A validated alias entry projects an accepted compatibility decision. It does not accept an ADR, authorize writes, move bytes, close consumers, create a tombstone, retire a path, or grant release/publication status."
[/KFM_META_BLOCK_V2] -->

# Path Alias Register Contract

## Purpose

The `PathAliasRegister` is the machine-readable projection for accepted KFM compatibility paths and identity aliases. It records how an old path or identifier resolves to one canonical target while keeping authority, writes, migration state, consumer evidence, parity checks, and rollback visible.

The register exists to prevent compatibility from becoming parallel authority. It implements the Directory Rules posture that compatibility may use **dual-read/single-write** when verified consumers require it, but every new write goes only to the canonical target.

## Authority boundary

The register projects accepted doctrine and ADRs. It cannot:

- accept or amend an ADR;
- create a compatibility path or make one canonical;
- authorize writes at an alias path;
- declare consumers closed without evidence;
- move, replace, tombstone, or delete repository bytes;
- approve release, deployment, promotion, or publication.

A `PASS` means only that the projection is internally consistent with its pinned Directory Rules and Root Registry evidence.

## Required register binding

The register binds:

- the adopted Directory Rules v2 path, identity, SHA-256, and `ADR-0029`;
- the exact Root Registry SHA-256 and its pinned base reference;
- the repository base at which the alias inventory was authored;
- owner, reviewers, scope, non-effects, and one or more alias entries.

Every entry repeats the adopted doctrine digest so machine consumers can detect stale or independently edited projections.

## Compatibility entry

Each alias entry records the fields required by Directory Rules section 17:

- stable alias ID and compatibility class;
- old path and canonical target;
- object family and identity mapping;
- reason, accepted ADR, rule IDs, and source digest;
- registered alias and target roots;
- verified canonical writers and an empty alias-writer set;
- verified consumer evidence and closure state;
- read rule and canonical-only write rule;
- generation or synchronization method;
- owner, reviewers, start date, expiry, and exit criteria;
- parity-validation references;
- rollback or forward-fix behavior;
- alias-versus-target exposure and mutation posture;
- body mode, legacy Git blob when available, canonical digest, and verification state.

## Compatibility classes

### `legacy`

Former canonical material retained read-only while consumers and references migrate. The body may remain a frozen legacy body or later become a bounded tombstone. Synchronization is `none_frozen`; new writes remain canonical-only.

### `mirror`

A generated one-way projection of canonical content. A mirror is non-authoritative, generated, and cannot become an independent writer.

### `external_export`

A shape or path required by a verified downstream consumer. The export is generated or manually produced from the canonical source and remains less permissive than its target.

### `transitional`

A temporary cutover path with bounded dual-read and canonical-only writes. Exit criteria and rollback are mandatory.

### `deprecated`

A read-only redirect or tombstone scheduled for retirement. It cannot contain a separately editable authority body.

## Initial population

The first register entry projects only the alias explicitly accepted by `ADR-0029`:

- old path: `docs/architecture/directory-rules.md`;
- canonical target: `docs/doctrine/directory-rules.md`;
- canonical identity: `kfm://doctrine/directory-governance/v2`;
- superseded IDs: `kfm://doc/directory-rules` and `kfm://doc/doctrine/directory-rules`;
- write posture: canonical-only;
- current body mode: frozen legacy body pending the separately governed tombstone phase;
- consumer closure: open.

The register deliberately does not invent aliases for `catalog/`, `artifacts/`, `src/`, triplet variants, policy homes, or other drift items. Those require their own accepted decisions and migration evidence.

## Validator invariants

The deterministic validator checks:

- strict JSON-compatible YAML and Draft 2020-12 shape;
- exact adopted Directory Rules and Root Registry bindings;
- accepted-decision evidence;
- canonical ordering and unique alias/path/identity keys;
- registered roots and active canonical target roots;
- object-family compatibility with the target root;
- no alias writers and at least one canonical writer;
- no alias chains or self-targets;
- no alias exposure or mutation more permissive than the target;
- class-specific read, body, and synchronization semantics;
- expiry, exit, parity, consumer, and rollback fields;
- current path existence, legacy Git blob continuity, and canonical SHA-256 when repository checks are enabled;
- non-echoing bounded diagnostics for malformed or untrusted input.

Finite outcomes are `PASS`, `FAIL_NEW_DRIFT`, `FAIL_INVARIANT`, `HOLD_UNRESOLVED`, and `ERROR_VALIDATOR`.

## Migration relationship

The alias register is not a migration manifest. A later path-changing PR must still provide the schema-backed migration record required by Directory Rules section 18, including before/after digests, producers, consumers, compatibility mode, validation, and rollback or forward-fix plan.

## Rollback

Rollback reverts this additive register/schema/validator/fixture/test/workflow packet and restores the prior validator README. It does not alter the accepted `ADR-0029`, the adopted Directory Rules bytes, the Root Registry, or either Directory Rules path.
