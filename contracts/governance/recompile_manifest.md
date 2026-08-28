<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/recompile-manifest
title: RecompileManifest Contract
type: contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — Governance steward · Generator steward · Contract steward · Schema steward · Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: internal; fixture-only; no-write; non-authoritative
related:
  - ../../schemas/contracts/v1/governance/recompile_manifest.schema.json
  - ../../fixtures/contracts/v1/governance/recompile_manifest/
  - ../../tools/generators/recompile_manifest/
  - ../../tools/validators/governance/validate_recompile_manifest.py
  - ../../tests/validators/governance/test_recompile_manifest.py
  - ./query_run_record.md
  - ./ai_change_proposal.md
  - ../../packages/hashing/src/hashing/core.py
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, governance, recompile, manifest, no-write, deterministic, rollback, fixture-only]
notes:
  - "This contract defines a fixture-only manifest for an in-memory JSON candidate compiled from an exact QueryRunRecord, AIChangeProposal, and subject preimage."
  - "It emits no file, applies no patch to repository state, and creates no evidence, policy, review, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# RecompileManifest Contract

> **Purpose.** Bind one deterministic, fixture-only recompilation to exact query, proposal, subject, compiler, output, and rollback identities without writing files or crossing the `WORK` boundary.

## Status and boundary

| Field | Value |
|---|---|
| Contract status | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY_NO_WRITE` |
| Authority created | `NONE` |
| Supported artifact profile | `JSON_DERIVED_CANDIDATE` only |
| Target lifecycle stage | `WORK` only |
| Network | forbidden |
| File writes | none; canonical candidate and manifest are returned in memory/stdout |
| Machine shape | `schemas/contracts/v1/governance/recompile_manifest.schema.json` |
| Compiler | `tools/generators/recompile_manifest/compile_recompile_manifest.py` |
| Replay validator | `tools/validators/governance/validate_recompile_manifest.py` |
| Current live integration | none |

A passing manifest proves only that one synthetic JSON candidate can be reproduced from the declared fixture inputs and that its rollback target is the exact subject preimage. It does not authorize applying the candidate or moving it beyond `WORK`.

## Source adaptation and repository fit

The Pipeline Living Implementation Manual proposes a governed `query -> save -> validate -> compile -> review -> promote -> recompile` loop. It names `QueryRunRecord`, candidate deltas, and `RecompileManifest` as separate control-loop records. The repository already has `QueryRunRecord` and `AIChangeProposal`; the latter safely represents a deterministic compare-and-set JSON candidate without granting mutation authority.

This profile therefore adds only the missing no-write compile/replay boundary. It does not create a competing candidate-delta family. It consumes the existing proposal object and emits a manifest plus canonical candidate bytes to stdout for review.

## Directory Rules basis

Accepted ADR-0029 makes Directory Rules v2 the placement authority. Semantic governance meaning belongs under `contracts/governance/`; machine shape under `schemas/contracts/v1/governance/`; synthetic examples under `fixtures/contracts/v1/governance/`; durable deterministic generation under `tools/generators/`; replay validation under `tools/validators/governance/`; executable proof under `tests/validators/governance/`; CI under `.github/workflows/`; source adaptation under `docs/intake/exploratory/`; and AI authoring provenance under `data/receipts/generated/`.

No new root, lifecycle phase, policy home, source registry, receipt authority, proof authority, release home, runtime route, or publication path is created.

## Admission conditions

A candidate may be compiled only when all of the following are true:

1. The `QueryRunRecord` passes its canonical validator.
2. Query evidence resolution is `COMPLETE` and the finite query outcome is `ANSWER`.
3. The exact proposal ID appears in `candidate_proposal_refs`.
4. The `AIChangeProposal` passes its validator against the exact subject preimage.
5. Proposal policy projection is `ALLOW`.
6. Human-attestation projection is `APPROVED`.
7. Proposal readiness is `READY_FOR_STEWARD_APPLY`.
8. The target stage is exactly `WORK`.
9. Applying the verified compare-and-set operations in memory reproduces the proposal's expected output hash.
10. The compiler uses no network and performs no file write.

`READY_FOR_STEWARD_APPLY` remains a projection, not authenticated permission. The compiler accepts it only as one fixture precondition and still keeps every write/release permission false.

## Finite compiler outcomes

| Outcome | Meaning |
|---|---|
| `COMPILED_CANDIDATE` | Canonical JSON candidate bytes and a conforming manifest were produced in memory. |
| `HOLD` | Query evidence or proposal readiness is not sufficient for compilation. |
| `DENY` | The candidate is invalid, unbound, policy-denied, targets a forbidden stage, or violates an integrity boundary. |
| `ERROR` | An input could not be read/parsed safely or deterministic compilation could not be evaluated. |

No outcome writes a file or creates approval, evidence, release, or publication state.

## Manifest bindings

### Inputs

The manifest binds:

- `query_run_id`, concrete query run hash, and query profile hash;
- `proposal_id` and patch hash;
- subject reference and exact input `spec_hash`.

### Compiler

The compiler identity is fixed to:

```text
kfm.tools.recompile-fixture.v1
version 1.0.0
RFC8785-JCS + SHA-256
network FORBIDDEN
write mode NO_WRITE
```

`compiler_spec_hash` is recomputed from that closed projection.

### Output

Version 1 emits one canonical RFC 8785 JSON object in memory. The manifest records:

- deterministic candidate reference derived from the output hash;
- output `content_spec_hash`;
- exact canonical byte length;
- media type `application/json`;
- `canonical_bytes=true`.

### Rollback

Rollback points to the exact subject reference and input `spec_hash` with `exact_restore=true`. The rollback binding is process memory only; it does not perform restoration.

## Deterministic identity

```text
compiler_spec_hash = SHA-256(JCS(closed compiler projection))
output_hash         = SHA-256(JCS(compiled candidate))
candidate_ref       = "kfm:recompile-candidate:" + hex(output_hash)
manifest_spec_hash  = SHA-256(JCS(manifest excluding manifest_id and manifest_spec_hash))
manifest_id         = "kfm:recompile-manifest:" + hex(manifest_spec_hash)
```

Replay validation reconstructs the candidate and manifest from the exact source objects. Any input, output, compiler, rollback, verification, permission, non-effect, manifest-hash, or manifest-ID drift fails closed.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/governance \
  --pattern 'test_recompile_manifest.py' \
  --verbose

python tools/generators/recompile_manifest/compile_recompile_manifest.py --fixtures
python tools/validators/governance/validate_recompile_manifest.py --fixtures
```

## Trust boundary

This profile does not:

- call an AI model or preserve private reasoning;
- resolve or authenticate evidence;
- evaluate policy or authenticate the projected reviewer;
- write a candidate file, repository path, lifecycle stage, database, object store, or Git ref;
- apply a proposal to canonical state;
- construct a proof, promotion decision, release manifest, correction notice, or public artifact;
- promote, release, deploy, publish, or authorize public use.

A later separately reviewed executor would need authenticated policy/review inputs, destination ownership, write authorization, conflict handling, receipts, correction behavior, and rollback execution. This contract does not provide those capabilities.

## Rollback

The implementation is additive and inactive. Before merge, close the pull request and remove its branch. After an authorized merge, revert the implementation commit or merge commit. No source deactivation, data migration, lifecycle cleanup, cache purge, release withdrawal, or public correction is required.
