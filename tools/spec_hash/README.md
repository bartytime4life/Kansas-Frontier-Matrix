<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-spec-hash-readme
title: tools/spec_hash README
type: README
version: v0.2
status: draft; implemented-fixture-tested; exact-head-CI-pending
owner: TODO-tooling-qa-owner-plus-architecture-steward-plus-release-steward
created: 2026-07-07
updated: 2026-08-06
policy_label: repository-facing; deterministic-hashing; provenance-support
owning_root: tools/
responsibility: deterministic spec_hash CLI boundary for canonicalization, digest computation, recomputation, comparison, and safe reporting
truth_posture: cite-or-abstain; hash equality is not evidence, policy, review, release, or publication authority
related:
  - ../README.md
  - ../../packages/hashing/
  - ../../docs/architecture/identity-and-spec-hash.md
  - ../../docs/standards/CANONICALIZATION.md
  - ../../docs/standards/RUN_RECEIPT.md
  - ../../docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md
  - ../validators/validate_spec_hash.py
  - ../../schemas/contracts/v1/common/spec_hash.schema.json
  - ../../fixtures/contracts/v1/common/spec_hash/
  - ../../tests/validators/test_validate_spec_hash.py
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../release/
notes:
  - "The reusable implementation lives in packages/hashing/src/hashing; this lane provides a thin repository CLI wrapper."
  - "RFC 8785 JCS canonicalization plus SHA-256 is implemented without implicit rounding, field selection, projection, or other object-family transforms."
  - "The current executable schema grammar remains sha256:<64 lowercase hex>. ADR-0013's jcs:sha256 target remains PROPOSED and is not silently adopted here."
  - "The helper creates no source, evidence, policy, review, promotion, release, publication, or public-use authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/spec_hash`

![status](https://img.shields.io/badge/status-draft--implemented-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-spec--hash--CLI-informational)
![canonicalization](https://img.shields.io/badge/canonicalization-RFC%208785%20JCS-blueviolet)
![grammar](https://img.shields.io/badge/current%20grammar-sha256%3A%3Chex%3E-purple)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `tools/spec_hash/spec_hash.py` is a thin repository-facing CLI over the reusable `packages/hashing` implementation. It computes or compares deterministic RFC 8785 JCS + SHA-256 content identifiers and emits a bounded machine-readable report.

> [!IMPORTANT]
> A matching hash proves only that the same admitted canonical bytes produced the same digest. It does not prove truth, source authority, evidence closure, rights, policy approval, review, promotion, release, publication, or fitness for use.

## Status

| Surface | Current state | Evidence boundary |
|---|---|---|
| `tools/spec_hash/spec_hash.py` | **CONFIRMED in this change** | Thin wrapper; exact-head hosted CI remains pending until pushed. |
| `packages/hashing/src/hashing/` | **CONFIRMED in this change** | Reusable canonicalization, hashing, file parsing, comparison, and CLI implementation. |
| `tools/validators/validate_spec_hash.py` | **CONFIRMED in this change** | Replaces the prior `NotImplementedError` stub. |
| Existing common fixtures | **CONFIRMED reused** | Valid and invalid fixture polarity is exercised without changing fixture meaning. |
| Current machine grammar | **CONFIRMED preserved** | `sha256:<64 lowercase hex>` from `schemas/contracts/v1/common/spec_hash.schema.json`. |
| `jcs:sha256:<hex>` grammar | **PROPOSED / ADR-sensitive** | ADR-0013 remains proposed; this change does not migrate schemas or consumers. |
| Publication authority | **NONE** | No lifecycle transition, source activation, policy decision, release, or publication is performed. |

## Directory Rules basis

The artifact is split by responsibility:

| Responsibility | Owning root / path |
|---|---|
| Reusable library implementation | `packages/hashing/src/hashing/` |
| Thin operator/CI wrapper | `tools/spec_hash/spec_hash.py` |
| Validator of record | `tools/validators/validate_spec_hash.py` |
| Machine shape | `schemas/contracts/v1/common/spec_hash.schema.json` |
| Semantic meaning | `contracts/common/spec_hash.md` |
| Synthetic examples | `fixtures/contracts/v1/common/spec_hash/` |
| Enforceability proof | `tests/validators/test_validate_spec_hash.py` |
| CI orchestration | `.github/workflows/spec-hash.yml` |
| Receipts, proofs, release decisions | Their existing `data/` and `release/` responsibility roots |

No parallel contract, schema, policy, registry, receipt, proof, release, or publication home is created.

## Canonicalization contract

The implementation performs exactly these generic operations:

1. Read bounded UTF-8 JSON from a regular, non-symlink file.
2. Reject duplicate object keys, non-standard numeric constants, non-finite values, excessive size, and excessive structure.
3. Canonicalize the parsed JSON value with RFC 8785 JCS.
4. Hash the canonical UTF-8 bytes with SHA-256.
5. Format the current executable identifier as `sha256:<64 lowercase hex>`.
6. Compare stored and recomputed values using constant-time digest-string comparison.

The implementation **does not** silently:

- round numeric fields;
- choose an object-family hash domain;
- remove volatile fields;
- normalize strings, dates, CRS, units, geometry, or identifiers;
- create a receipt, signature, attestation, EvidenceBundle, PolicyDecision, PromotionDecision, or ReleaseManifest.

Those operations must be declared and tested by the calling object-family contract before it invokes the generic canonicalizer.

## Commands

Compute a hash for one JSON subject:

```bash
python tools/spec_hash/spec_hash.py compute path/to/subject.json
```

Verify a subject against a common `spec_hash` record:

```bash
python tools/spec_hash/spec_hash.py verify \
  path/to/subject.json \
  path/to/spec_hash.json
```

Validate the existing common contract fixture matrix:

```bash
python tools/validators/validate_spec_hash.py --fixtures
```

Validate a hash record's shape:

```bash
python tools/validators/validate_spec_hash.py \
  --candidate path/to/spec_hash.json
```

Validate shape and recompute the referenced subject:

```bash
python tools/validators/validate_spec_hash.py \
  --candidate path/to/spec_hash.json \
  --subject path/to/subject.json
```

Run focused tests:

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_spec_hash.py' \
  --verbose
```

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `SPEC_HASH_CREATED` | Canonical bytes were hashed for caller review. |
| `SPEC_HASH_MATCH` | Stored and recomputed identifiers match. |
| `SPEC_HASH_MISMATCH` | Stored and recomputed identifiers differ. |
| `SPEC_HASH_SCHEMA_INVALID` | The common hash record violates its JSON Schema. |
| `SPEC_HASH_FORMAT_INVALID` | A CLI hash record does not contain exactly the current grammar. |
| `CANDIDATE_JSON_INVALID` / `SUBJECT_JSON_INVALID` | Input could not be read or parsed safely. |
| `CANONICALIZATION_ERROR` | A parsed value is outside the admitted RFC 8785 JSON domain. |
| `SCHEMA_UNAVAILABLE` | The validator could not load or validate the common schema. |
| `PASS` / `DENY` / `ERROR` | Bounded validator result; never a source, policy, review, or release decision. |

## Report boundary

Reports include the canonicalization profile, hash algorithm, finite status/outcome, safe paths, findings, and explicit non-effects. Hashes may be reported because they are integrity identifiers, but candidate field values and sensitive content are not echoed.

```json
{
  "authority": "NONE",
  "canonicalization": "RFC8785-JCS",
  "hash_algorithm": "SHA-256",
  "non_effects": [
    "no_source_admission",
    "no_evidence_resolution",
    "no_policy_evaluation",
    "no_promotion_release_or_publication",
    "no_public_use_authority"
  ],
  "scope": "common.spec_hash",
  "status": "SPEC_HASH_MATCH"
}
```

## Validation coverage

Focused tests cover:

- known RFC 8785 canonical bytes;
- key-order invariance;
- SHA-256 agreement over canonical bytes;
- existing valid/invalid fixture polarity;
- stored-vs-recomputed match and mismatch;
- duplicate JSON key rejection;
- non-finite input rejection;
- unsafe-integer canonicalization failure;
- input immutability;
- deterministic CLI output;
- wrapper and validator fixture-suite execution.

## Review checklist

- [ ] Exact-head focused workflow passes.
- [ ] Dependency pin and license/provenance review are acceptable.
- [ ] Current `sha256:` grammar remains compatible with existing schemas and consumers.
- [ ] No reviewer mistakes this implementation for adoption of proposed ADR-0013.
- [ ] Object-family producers declare any rounding, filtering, geometry, or field-selection profile before hashing.
- [ ] Reports do not leak candidate values or protected content.
- [ ] Generated authoring receipt binds the final committed implementation bytes.

## Rollback

Before merge, close the draft pull request and remove its feature branch. After an authorized merge, revert the additive implementation commit(s). No source deactivation, data migration, release withdrawal, cache invalidation, public correction, or published-artifact rollback is required because this slice performs no lifecycle or publication transition.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-08-06 |
| Review state | Draft implementation; human review pending. |
| Next safe extension | Adopt or reject ADR-0013 separately before any `sha256:` → `jcs:sha256:` grammar migration. |
