<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-proof-pack-readme
title: ProofPack Assembler and Checker
type: readme
version: v0.2
status: draft; repository-grounded; bounded-executable; fixture-tested; no-network; no-release-authority; non-publication
owner: NEEDS VERIFICATION — proof, evidence, validation, policy, release, correction, rollback, and tooling stewards
created: 2026-07-07
updated: 2026-08-28
current_path: tools/proof_pack/README.md
owning_root: tools/
policy_label: public; tooling-boundary; bounded-executable; proof-pack-builder-and-checker; no-release-authority
responsibility: Document the implemented deterministic assembler and checker for the proposed release-support ProofPack profile without turning tooling, tests, fixtures, or workflow success into proof, policy, review, release, or publication authority.
base_commit: 156e3288f21dc95d60daa744be4207681ad21655
prior_blob: 3324d30b9fea44913f96a696b915d89ac48846e9
truth_posture: CONFIRMED three Python modules, a proposed semantic contract and schema, synthetic candidate/valid/invalid fixtures, two focused pytest files, and a hosted proof-pack-closure workflow exist; the checker validates schema, required component families, cross-bindings, path safety, and local digests without network access; the assembler writes only to an explicit caller-selected path / PROPOSED profile semantics and future canonical instance admission / UNKNOWN production writers and consumers, required-check status, emitted canonical instances, authenticated review, release integration, retention, correction, rollback drills, deployment, and publication
[/KFM_META_BLOCK_V2] -->

# ProofPack assembler and checker

<a id="top"></a>

> **One-line purpose.** `tools/proof_pack/` contains the implemented,
> deterministic assembler and checker for the proposed
> `kfm.proof-pack.release-support.v1` profile. The tools support review; they
> do not create evidence, policy permission, release approval, or publication.

| Surface | Current evidence | Safe interpretation |
|---|---|---|
| Shared helpers | [`_common.py`](./_common.py) | Safe JSON loading, canonical repository-relative path checks, symlink denial, size limits, and SHA-256 calculation. |
| Assembler | [`assemble_proof_pack.py`](./assemble_proof_pack.py) | Builds a deterministic candidate at an explicit output path; never writes canonical proof storage by default. |
| Checker | [`proof_pack_check.py`](./proof_pack_check.py) | Validates schema, semantic bindings, required component families, safe local references, and digests. |
| Tests | [assembler tests](../../tests/proof_pack/test_assemble_proof_pack.py) and [checker tests](../../tests/proof_pack/test_proof_pack_check.py) | Exercise deterministic assembly, CLI behavior, fixtures, path safety, and failure cases. |
| Hosted orchestration | [`proof-pack-closure.yml`](../../.github/workflows/proof-pack-closure.yml) | Runs the bounded profile; workflow success is not release or publication. |

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-boundary) ·
[Implementation](#implemented-surface) · [Inputs](#inputs) · [Outputs](#outputs) ·
[Limits](#security-and-determinism-limits) · [Run](#run-the-focused-checks) ·
[Results](#result-interpretation) · [Failures](#failure-and-recovery) ·
[Maintenance](#maintenance-correction-and-rollback) · [Open questions](#open-questions) ·
[Related](#related-repository-surfaces)

## Purpose

The tooling answers one bounded question:

> Does a local release-support ProofPack candidate satisfy the proposed schema,
> carry the required support families, preserve release/subject/spec-hash
> bindings, use safe repository-relative files, and match their declared
> SHA-256 digests?

A pass proves only that declared local closure. It does not establish that an
EvidenceBundle is true, a policy decision is correct, a reviewer approved the
candidate, a signature is authentic, a release exists, or publication is allowed.

## Authority boundary

| Responsibility | Owning surface | Tooling relationship |
|---|---|---|
| ProofPack meaning | [`contracts/evidence/proof_pack.md`](../../contracts/evidence/proof_pack.md) | Implements the proposed release-support profile; does not accept it. |
| Machine shape | [`proof_pack.schema.json`](../../schemas/contracts/v1/evidence/proof_pack.schema.json) | Loads and validates the schema; does not own schema meaning. |
| Synthetic examples | [`fixtures/contracts/v1/evidence/proof_pack/`](../../fixtures/contracts/v1/evidence/proof_pack/) | Reads candidate, valid, and invalid fixtures; fixtures are not production proof. |
| ProofPack records | [`data/proofs/proof_pack/`](../../data/proofs/proof_pack/README.md) | No automatic writes; canonical admission remains separately governed. |
| Policy | [`policy/`](../../policy/README.md) | Checks referenced posture only; never emits policy decisions. |
| Process receipts | [`data/receipts/`](../../data/receipts/README.md) | Tool output is not a receipt unless a governed writer adopts it. |
| Release and rollback | [`release/`](../../release/README.md) | Tools never approve release or own rollback or correction records. |
| Published carriers | [`data/published/`](../../data/published/README.md) | No direct write or public-serving authority. |

The empty [`policy/proof/`](../../policy/proof/README.md) lane is a routing hold,
not the policy authority behind these tools.

## Implemented surface

### Shared safeguards

`_common.py` rejects duplicate JSON keys, non-finite numbers, non-object roots,
symlink JSON inputs, JSON inputs larger than 2 MiB, noncanonical or escaping
paths, symlink components, missing or non-regular files, components larger than
16 MiB, and aggregate component sets larger than 128 MiB. It computes streaming
SHA-256 digests.

### Assembler

`assemble_proof_pack.py` requires an exact candidate envelope, copies release,
subject, and spec-hash bindings into every component, calculates local digests,
sorts components deterministically, validates the result, and writes only to the
caller's explicit `--output` path.

It refuses to overwrite an existing output unless `--force` is passed. It does
not invent a timestamp, sign, approve, write to `data/proofs/`, mutate lifecycle
state, deploy, or publish.

### Checker

`proof_pack_check.py` validates the Draft 2020-12 schema, requires the 11 named
component families, requires correction history for a non-current correction
state, rejects duplicate IDs and paths, enforces cross-bindings, verifies local
paths and digests, and rejects manifest self-reference.

`--no-reference-check` intentionally skips local file and digest verification.
It is for bounded diagnosis and must not be described as closure.

## Inputs

The checker accepts one JSON manifest or the repository fixture suite. The
assembler accepts an exact candidate JSON object, an explicit repository root,
an explicit output path, and optional `--force` replacement authorization. The
implementation performs no network fetch.

## Outputs

| Command | Success output | Failure behavior |
|---|---|---|
| Checker | `PROOF_PACK_CHECK_PASS ... release_authority=false` | Emits stable `PROOF_PACK_CHECK_FAIL` findings and exits nonzero. |
| Fixture suite | `PROOF_PACK_FIXTURES_VALID ... no_network=true release_authority=false` | Names fixture polarity failures or an unusable fixture lane and exits nonzero. |
| Assembler | Deterministic JSON at the explicit output plus `PROOF_PACK_CANDIDATE_BUILT ... release_authority=false` | Emits `PROOF_PACK_ASSEMBLY_FAIL` and does not claim a valid candidate. |

These are tool results, not policy decisions, receipts, proof admission, review
records, release decisions, signatures, deployments, or public artifacts.

## Security and determinism limits

- The tools are local and no-network, but read every referenced component that
  passes path and size checks. Do not use sensitive production payloads for
  casual validation.
- Path controls prevent traversal and symlink substitution within the declared
  repository root; they do not authenticate the person or workflow supplying it.
- SHA-256 agreement detects byte substitution relative to declared digests; it
  does not prove source authority, truth, rights, consent, or audience fitness.
- `assembled_at` and other candidate timestamps are supplied inputs. Repeated
  assembly is deterministic only when inputs and referenced bytes are unchanged.
- Tests and workflow runs prove the bounded profile at an exact revision, not
  repository-wide proof readiness or release enforcement.

## Run the focused checks

From the repository root:

```bash
python tools/proof_pack/proof_pack_check.py --fixtures
python -m pytest -q tests/proof_pack
python -m pytest -q tests/schemas/test_common_contracts.py

python tools/proof_pack/assemble_proof_pack.py \
  --candidate fixtures/contracts/v1/evidence/proof_pack/candidates/release_support_candidate.json \
  --repo-root . \
  --output /tmp/kfm-proof-pack.json
cmp /tmp/kfm-proof-pack.json \
  fixtures/contracts/v1/evidence/proof_pack/valid/valid_release_support.json
```

The commands validate fixture polarity, focused behavior, the shared schema
harness, and deterministic assembly. They do not admit the generated file to
`data/proofs/` or authorize release.

## Result interpretation

| Finding family | Meaning |
|---|---|
| `SCHEMA_INVALID` | The manifest violates the proposed JSON Schema. |
| `REQUIRED_COMPONENT_MISSING` or `CORRECTION_HISTORY_REQUIRED` | Required support is absent. |
| Duplicate or cross-binding findings | Component identity, path, release, subject, or spec-hash bindings conflict. |
| Path or file findings | A reference is unsafe, missing, symlinked, oversized, self-referential, or not a regular file. |
| `COMPONENT_DIGEST_MISMATCH` | Local bytes do not match the declared digest. |

A failed or unavailable check keeps the candidate held for its governing review.
Do not infer missing support or silently disable reference checking.

## Failure and recovery

1. Preserve the exact command, revision, manifest identity, and findings.
2. Correct the candidate or governed dependency at the owning surface.
3. Do not edit a digest merely to match unexpected bytes; investigate provenance.
4. Rerun the focused checks with reference verification enabled.
5. Version and review contract or schema changes before updating the tool.
6. If a candidate was consumed, follow correction, withdrawal, invalidation, and rollback.

## Maintenance, correction, and rollback

Recheck this README when the contract, schema, required component families, size
limits, CLI, fixtures, tests, workflow, proof-storage boundary, policy binding,
or release integration changes.

For this documentation-only revision, rollback means reverting the focused
commit or closing the unmerged draft PR. Reverting documentation must not remove
the assembler, checker, helpers, fixtures, tests, schema, contract, workflow,
proof records, release records, or published artifacts.

## Open questions

| ID | Question | Current status |
|---|---|---|
| PROOF-TOOL-001 | Who owns and independently reviews the assembler and checker? | **NEEDS VERIFICATION** |
| PROOF-TOOL-002 | Is `proof-pack-closure` required by repository rules or only available CI? | **UNKNOWN** |
| PROOF-TOOL-003 | Which governed writer, if any, may admit a passing candidate to `data/proofs/proof_pack/`? | **UNKNOWN** |
| PROOF-TOOL-004 | What authenticated review, receipt, retention, correction, and rollback chain binds output to release review? | **UNKNOWN** |
| PROOF-TOOL-005 | Which production consumers or release workflows rely on this profile? | **NEEDS VERIFICATION** |

## Related repository surfaces

- [ProofPack semantic contract](../../contracts/evidence/proof_pack.md)
- [ProofPack schema](../../schemas/contracts/v1/evidence/proof_pack.schema.json)
- [ProofPack record lane](../../data/proofs/proof_pack/README.md)
- [Policy proof routing hold](../../policy/proof/README.md)
- [ProofPack closure workflow](../../.github/workflows/proof-pack-closure.yml)
- [Directory Rules](../../docs/doctrine/directory-rules.md)
- [ADR-0011](../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)

[Back to top](#top)

## Changelog

| Version | Date | Change | Runtime effect |
|---|---|---|---|
| v0.1 | 2026-07-07 | Documented a proposed ProofPack tooling boundary before the executable profile existed. | None. |
| v0.2 | 2026-08-28 | Reconciles the implemented assembler, checker, tests, schema, fixtures, workflow, commands, limits, and non-effects. | None; documentation only. |
