<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/proof-pack-release-support-v1
title: KFM Release-Support ProofPack Contract
type: semantic-contract
version: 1.0.0
status: proposed-profile; fixture-first; no-release-authority
owner: NEEDS VERIFICATION — proof, evidence, validation, policy, release, correction, rollback, and domain stewards
created: 2026-08-05
updated: 2026-08-05
policy_label: internal-review; no-direct-public-path; cite-or-abstain
owning_root: contracts/
related:
  - ../../schemas/contracts/v1/evidence/proof_pack.schema.json
  - ../../data/proofs/proof_pack/README.md
  - ../../tools/proof_pack/README.md
  - ../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
truth_posture: contract semantics are PROPOSED until reviewed; implementation bytes and tests are repository evidence only
[/KFM_META_BLOCK_V2] -->

# KFM Release-Support ProofPack Contract

> **One-line purpose.** Define one closed, fixture-first manifest profile that proves a release candidate's declared support references are present, mutually bound, path-safe, and digest-consistent for review without creating release, publication, policy, evidence, or truth authority.

## Status and boundary

This contract introduces the proposed profile `kfm.proof-pack.release-support.v1`.
It is deliberately narrower than a universal ProofPack ontology. It governs only the
release-support manifest exercised by the paired schema, assembler, checker, fixtures,
tests, and read-only workflow.

A passing ProofPack check means the declared local references satisfy this profile. It does
**not** mean that the referenced EvidenceBundle is true, the policy decision is correct, a
human approved release, the release exists, a signature is authentic, or publication is
allowed.

The manifest must therefore carry these fixed non-effects:

```json
{
  "release_approved": false,
  "publication": false,
  "authority_created": false
}
```

## Directory Rules basis

The existing responsibility split is preserved:

- semantic meaning: `contracts/evidence/proof_pack.md`;
- machine shape: `schemas/contracts/v1/evidence/proof_pack.schema.json`;
- reusable synthetic examples: `fixtures/contracts/v1/evidence/proof_pack/`;
- builder and checker code: `tools/proof_pack/`;
- enforceability: `tests/proof_pack/` and repository schema tests;
- hosted orchestration: `.github/workflows/proof-pack-closure.yml`;
- authoring provenance: `data/receipts/generated/`;
- canonical ProofPack instances, if later admitted: `data/proofs/proof_pack/`;
- release decisions, rollback cards, correction notices, and signatures: `release/`.

No new root or parallel proof, receipt, catalog, release, policy, or publication home is created.

## Required identity

A manifest binds one `release_id` and one subject:

- `subject_id` identifies the release candidate under review;
- `subject_type` identifies its carrier family;
- `spec_hash` is the deterministic subject specification hash;
- `correction_state` makes correction or withdrawal posture explicit;
- every component repeats the same release, subject, and spec-hash binding.

The checker fails closed when any component points at a different release, subject, or spec
hash. Repeated bindings are intentional: they make accidental cross-release assembly
visible instead of relying on path naming.

## Required component families

A release-support pack must contain at least one digest-bound reference for each family:

| Kind | Review question |
|---|---|
| `EVIDENCE_BUNDLE` | What evidence supports the candidate? |
| `VALIDATION_REPORT` | Which deterministic validation ran and what did it report? |
| `INTEGRITY_MANIFEST` | What binds the candidate or support set by digest? |
| `PROV_EXPORT` | What provenance representation can be inspected? |
| `LINEAGE_INDEX` | How are prior, current, negative, and superseded states related? |
| `PROMOTION_DECISION` | Which separate promotion-governance record is referenced? |
| `RUNTIME_PROOF` | What bounded runtime behavior was exercised? |
| `CITATION_SAMPLE` | Can a consequential claim be traced to support? |
| `CI_RUN` | Which exact automation evidence is referenced? |
| `RELEASE_ANCHOR` | Which commit SHA or release tag anchors the candidate? |
| `ROLLBACK_REFERENCE` | What prior state or rollback target is available? |

`CORRECTION_HISTORY` is additionally required when `correction_state` is anything other
than `NONE`. Negative, held, corrected, withdrawn, revoked, or superseded history remains
audit-visible but cannot silently become current claim support.

## Path and integrity rules

Every component path must be canonical POSIX, repository-relative, and free of `.` or `..`
segments, backslashes, absolute prefixes, and symbolic-link traversal. The checker limits
file count and byte volume, rejects a manifest that references itself, and computes an exact
SHA-256 digest for every referenced regular file.

Missing files, unreadable files, path escape, symlink traversal, unsupported digest syntax,
or digest mismatch fail closed. The validator performs no network access.

## Finite checker outcomes

| Outcome | Meaning |
|---|---|
| `PROOF_PACK_CHECK_PASS` | The schema, semantic bindings, required families, paths, and configured local digests passed. |
| `PROOF_PACK_CHECK_FAIL` | One or more deterministic findings blocked the candidate. |
| `ABSTAIN` | The checker lacked enough local evidence to decide safely. |
| `ERROR` | The checker could not complete safely. |

Stable finding codes include `REQUIRED_COMPONENT_MISSING`,
`COMPONENT_RELEASE_MISMATCH`, `COMPONENT_SUBJECT_MISMATCH`,
`COMPONENT_SPEC_HASH_MISMATCH`, `COMPONENT_DIGEST_MISMATCH`,
`COMPONENT_NOT_FILE`, `CORRECTION_HISTORY_REQUIRED`, and
`COMPONENT_ID_DUPLICATE`.

## Deterministic assembly

The assembler accepts a candidate JSON object containing explicit top-level identity,
component kinds, artifact IDs, paths, and timestamps. It:

1. resolves each path under an explicit repository root;
2. rejects unsafe or unreadable paths;
3. computes SHA-256 digests;
4. copies the pack's release/subject/spec-hash bindings into every component;
5. sorts components deterministically;
6. validates the final object with the same checker; and
7. writes only to an explicit output path.

The assembler does not invent a timestamp, approve release, write to `data/proofs/`, or
publish. A caller must explicitly choose the output location.

## Validation

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

## Trust boundary

ProofPack closure is a review aid. It does not:

- create or authenticate evidence;
- decide rights, sensitivity, source role, or policy;
- approve promotion or release;
- sign or attest artifacts;
- create a release manifest;
- mutate lifecycle state;
- deploy or publish;
- authorize a public route.

Public clients must not read the proof lane directly. Any later runtime projection must pass
through governed release and delivery contracts.

## Rollback

Before merge, close the draft pull request and delete only its task branch. After an
authorized merge, revert the feature commit through a reviewed pull request. That removes
the profile, builder/checker, fixtures, tests, workflow, and authoring receipt without touching
source data, release decisions, published artifacts, deployments, or repository settings.
