<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/release/release-manifest
title: ReleaseManifest Contract
type: semantic-contract
version: v0.3.0
status: draft; PROPOSED_INACTIVE; dual-profile; fixture-only strict candidate
owners: OWNER_TBD — Release steward · Evidence steward · Policy steward · Review steward · Rollback steward · Contract steward · Schema steward · Validation steward
created: NEEDS VERIFICATION — file existed before v0.3 hardening
updated: 2026-08-08
policy_label: public; release; manifest; fixture-only; no-publication-authority
owning_root: contracts/
responsibility: Define the semantic meaning and non-authority boundary of ReleaseManifest.
truth_posture: PROPOSED semantic profile; CONFIRMED deterministic synthetic validation
related:
  - ./README.md
  - ./promotion_decision.md
  - ./promotion_receipt.md
  - ./rollback_card.md
  - ../evidence/evidence_bundle.md
  - ../../schemas/contracts/v1/release/release_manifest.schema.json
  - ../../fixtures/release/release_manifest/
  - ../../tools/validators/release/validate_release_manifest.py
  - ../../tests/validators/test_validate_release_manifest.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/intake/exploratory/pass7-release-manifest-profile.md
tags: [kfm, release, manifest, deterministic-identity, evidence, rollback, fixture-only]
notes:
  - "v0.3 preserves the prior permissive id-required profile and adds a closed PROPOSED_INACTIVE / FIXTURE_ONLY candidate profile."
  - "A valid candidate proves local shape and deterministic semantics only; it does not resolve refs, verify bytes or signatures, evaluate policy, authenticate review, authorize release, publish, or permit public use."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ReleaseManifest Contract

> `ReleaseManifest` is the governed release binding for a declared artifact set. It identifies the release, binds content identity and artifact digests, and carries evidence, policy, promotion, review, correction, and rollback references without collapsing those independent authorities into the manifest.

## Status

The machine schema has two branches:

1. **`LEGACY_MINIMAL`** — preserves the prior permissive `id`-required shape for compatibility.
2. **`RELEASE_MANIFEST_FIXTURE_V1`** — a closed, opt-in, `PROPOSED_INACTIVE` and `FIXTURE_ONLY` candidate used to prove deterministic local behavior.

The strict profile is not a production release format. It performs no network access and creates no source, evidence, policy, review, promotion, release, publication, signing, lifecycle-write, or public-use authority.

## Source-derived requirement

Pass 7 card `KFM-P7-PROG-0003` describes ReleaseManifest as one signed, hashable release object that lists the datasets, evidence bundles, layer manifests, and tile archives included in a release. Consumers bind to a fixed manifest identity rather than a mutable `latest` pointer. This slice realizes only the deterministic candidate shape and validator needed before a production consumer or release builder can exist.

## Responsibility split

| Responsibility | Home |
|---|---|
| Semantic meaning | `contracts/release/release_manifest.md` |
| Machine shape | `schemas/contracts/v1/release/release_manifest.schema.json` |
| Synthetic examples | `fixtures/release/release_manifest/` |
| Executable validation | `tools/validators/release/validate_release_manifest.py` |
| Behavior proof | `tests/validators/test_validate_release_manifest.py` |
| Read-only CI | `.github/workflows/release-manifest.yml` |
| Release decisions and persisted release records | `release/`; outside this candidate validator |
| Evidence, proofs, and receipts | Their existing owning roots; referenced, never embedded as authority |

ADR-0029 adopts Directory Governance Standard v2. The packet uses existing responsibility roots and creates no new root or parallel release, schema, proof, receipt, policy, or publication authority.

## Strict object meaning

| Field family | Rule |
|---|---|
| Identity | `id` and `spec_hash` are derived from RFC 8785 JCS plus SHA-256 with only stored `id` and `spec_hash` omitted. |
| Release identity | `release_id` and `release_version` name a fixed candidate; floating `latest` references fail. |
| Contents | `artifacts[]` carries opaque refs, exact SHA-256 digests, media types, and bounded roles; payload bytes are never embedded. |
| Evidence and source | SourceDescriptor and EvidenceBundle refs remain explicit and canonical. |
| Decisions | Policy, promotion, and review refs remain separate; the manifest does not manufacture their outcomes. |
| Release scope | Intended audience, rights, sensitivity, and any public-safe transform refs are declared without authorizing exposure. |
| Temporal scope | Assembly and effective times remain distinct. |
| Lineage | Previous manifest, correction, withdrawal, and rollback refs preserve reversible history. |
| Provenance | A RunReceipt ref and validator implementation ref make local evaluation inspectable. |
| Governance | Every authority-bearing flag is fixed to `false` in this inactive profile. |

## Semantic invariants

1. `artifact_count` equals the number of artifacts.
2. Artifacts are sorted by `artifact_ref` and each artifact ref is unique.
3. Reference arrays are sorted, duplicate-free, and value-free diagnostics never echo their contents.
4. Mutable or floating `latest` references are denied.
5. One reference cannot silently fill two authority-bearing roles.
6. Every declared EvidenceBundle ref is represented by an `EVIDENCE_BUNDLE` artifact entry.
7. A public-intended candidate requires approved rights, public-safe or transform-required sensitivity, evidence refs, policy refs, promotion refs, and review refs.
8. `TRANSFORM_REQUIRED` requires generalized output and at least one transform receipt ref.
9. Effective time cannot run backward.
10. Correction refs require a previous manifest ref.
11. A valid strict candidate still keeps all authority flags false.

## Finite validator result

- `PASS` — closed shape and bounded semantic invariants pass.
- `FAIL` — schema or semantic review findings deny the candidate.
- `ERROR` — input, schema, or deterministic hashing cannot be evaluated safely.

A PASS proves only the selected local candidate bytes and declared relationships. It does not establish that any ref resolves, any artifact digest matches real bytes, any signature is valid, any policy/review decision exists, or any release may be exposed.

## Lifecycle and anti-collapse boundary

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

The strict profile remains at `CANDIDATE`. It cannot write `PUBLISHED`, move files, update aliases, activate caches, generate a public URL, or authorize a UI/map/API/AI consumer. A receipt is process memory, a proof is trust evidence, a catalog is discovery metadata, a promotion decision governs transition, and a ReleaseManifest binds contents only after those independent duties close.

## Compatibility

The legacy branch remains intact. Existing id-only examples continue to validate. The strict branch is additive and selected only by `object_type: ReleaseManifest`; it rejects unknown fields and has no runtime registration or production release consumer.

## Graduation requirements

Graduation requires separately reviewed decisions for production-required fields, reference resolution, byte verification, signature/attestation policy, release-state persistence, separation of duties, public-consumer verification, correction propagation, cache invalidation, and rollback drills. This fixture profile must not be relabeled as production-ready to avoid those gates.

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive validator/fixture/workflow/receipt packet and restore the prior contract/schema blobs. The strict profile has no source activation, data migration, release, deployment, publication, cache, or public artifact side effect.

<p align="right"><a href="#top">Back to top</a></p>
