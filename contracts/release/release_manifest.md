<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-release-release-manifest
title: contracts/release/release_manifest.md — ReleaseManifest Contract
type: contract
version: v0.2
status: draft; PROPOSED; schema-paired; thin-schema; release-governance-core
owners: OWNER_TBD — Release steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Rights steward · Sensitivity steward · Review steward · Rollback steward · Docs steward
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; release; release-manifest; content-addressed; signed-release; evidence-aware; rights-aware; sensitivity-aware; rollback-aware; correction-aware; no-artifact-store
tags: [kfm, contracts, release, release-manifest, publication, published, content-addressed, signed, hashable, evidence-ref, rollback-target, correction-lineage, rights, sensitivity, attestations, promotion, fail-closed]
related:
  - ./README.md
  - ./promotion_decision.md
  - ./rollback_card.md
  - ./withdrawal_notice.md
  - ./layer_manifest.md
  - ./map_release_manifest.md
  - ../correction/correction_notice.md
  - ../policy/policy_decision.md
  - ../evidence/evidence_bundle.md
  - ../../schemas/contracts/v1/release/release_manifest.schema.json
  - ../../policy/release/
  - ../../policy/promotion/
  - ../../release/
  - ../../fixtures/release/release_manifest/
  - ../../tools/validators/release/validate_release_manifest.py
  - ../../docs/architecture/release-discipline.md
  - ../../docs/standards/RELEASE_MANIFEST.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../data/proofs/
  - ../../data/receipts/
notes:
  - "Expanded from existing `contracts/release/release_manifest.md`."
  - "Paired schema verified at `schemas/contracts/v1/release/release_manifest.schema.json`; schema status is PROPOSED."
  - "The current schema is a greenfield placeholder: only `id` is required and `additionalProperties` is true."
  - "This contract states target release-manifest semantics, but fields beyond `id`, optional `spec_hash`, and optional `version` remain PROPOSED until the schema, fixtures, validators, policy, and release process are hardened."
  - "ReleaseManifest is semantic/object meaning. It is not the release artifact store, not proof closure by itself, not policy approval, not a promotion decision, not a public API/UI/map surface, and not AI truth."
  - "Rollback target for this expansion is previous blob SHA `58327f2ad480d150b30952e8b7725fe40ebd4e19`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ReleaseManifest Contract

> `ReleaseManifest` is the governed release binding for a published artifact set. It identifies the release, lists or references the release contents, binds digests/spec lineage, carries evidence/rights/sensitivity/policy/review/attestation/rollback/correction context, and gives downstream consumers a stable thing to verify. It does **not** publish content by itself, store release payloads, replace promotion decisions, or allow public clients to bypass governed interfaces.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Object: ReleaseManifest" src="https://img.shields.io/badge/object-ReleaseManifest-0a7ea4">
  <img alt="Schema: thin" src="https://img.shields.io/badge/schema-thin__placeholder-orange">
  <img alt="Publication: gated" src="https://img.shields.io/badge/publication-gated-critical">
  <img alt="Artifacts: referenced only" src="https://img.shields.io/badge/artifacts-referenced__only-lightgrey">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/release/release_manifest.md`  
**Paired schema:** `schemas/contracts/v1/release/release_manifest.schema.json`  
**Schema maturity:** greenfield placeholder / thin / permissive  
**Validator path named by schema:** `tools/validators/release/validate_release_manifest.py` — NEEDS VERIFICATION for implementation/wiring  
**Policy authority:** `policy/release/`, not this contract  
**Release artifact/process authority:** `release/`, not this contract  
**Truth posture:** CONFIRMED schema pairing and thin field surface · CONFIRMED release doctrine says ReleaseManifest is emitted at the PUBLISHED gate and consumers bind to it, not floating latest pointers · PROPOSED detailed fields and invariants until schema/fixtures/validator/policy/release integration are verified

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Schema-paired field surface](#schema-paired-field-surface) · [Target semantic field families](#target-semantic-field-families) · [Field semantics](#field-semantics) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Validation expectations](#validation-expectations) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`ReleaseManifest` is the semantic object that binds a KFM release into a verifiable, citable, reversible publication unit.

It answers:

- which release exists;
- which artifact set is included;
- which digests, spec hashes, or content-addressed identifiers define it;
- which EvidenceRefs/EvidenceBundles support release-visible claims;
- which policy decisions and promotion decisions allowed the release;
- which rights, sensitivity, and review postures apply;
- which attestations, receipts, proofs, and validation reports support the release;
- which correction, withdrawal, supersession, or rollback path applies.

It does not answer:

- whether machine shape is valid — that is schema/validator responsibility;
- whether policy allows publication — that is policy/release decision responsibility;
- whether a transition was approved — that is `PromotionDecision` / policy gate output;
- whether artifacts are stored here — release artifacts belong in `release/` or accepted artifact stores;
- whether public clients can read pre-publication state — they cannot;
- whether generated AI text is true — EvidenceBundle and release authority outrank generated language.

---

## Meaning

A `ReleaseManifest` is the release-facing trust spine for published KFM artifacts.

A mature manifest should be:

- **identified** — stable release id and version/spec lineage;
- **hashable** — canonicalized enough for deterministic digesting;
- **signable** — capable of being bound to attestations/signatures;
- **citable** — usable by downstream systems and public clients as a release anchor;
- **gateable** — produced only after governed policy/review/release gates pass;
- **reversible** — tied to rollback targets, correction notices, and supersession paths;
- **inspectable** — references resolve to evidence, policy, review, rights, sensitivity, proofs, and receipts.

A `ReleaseManifest` is not sovereign truth. It is an envelope that points to source/evidence/proof/release state. It must not collapse all authority into one file.

---

## Schema-paired field surface

The paired schema is currently intentionally thin.

| Field | Required | Schema-confirmed shape | Semantic role |
|---|---:|---|---|
| `id` | yes | string | Canonical release manifest identifier. |
| `spec_hash` | no | string | Deterministic content/spec hash, if present. |
| `version` | no | string | Release/object version, if present. |

Schema-confirmed posture:

- `id` is the only required field.
- `spec_hash` and `version` are optional.
- `additionalProperties` is currently `true`.

> [!WARNING]
> The detailed release semantics below are **PROPOSED** until the schema is hardened. Current schema permissiveness means an instance may validate while still being release-incomplete by governance standards.

---

## Target semantic field families

A mature `ReleaseManifest` should eventually model these field families explicitly or by resolvable refs.

| Field family | Meaning | Required posture |
|---|---|---|
| Identity | release id, version, spec hash, canonicalization profile, manifest digest. | Deterministic and content-addressable where practical. |
| Contents | datasets, bundles, layers, tiles, COGs, PMTiles, reports, graph/catalog/triplet outputs, model-independent artifacts. | Refs/digests only; no payload embedding. |
| Digests | artifact digests, manifest digest, Merkle root, sidecar digests. | Required for integrity. |
| Evidence | EvidenceRefs and EvidenceBundle refs supporting release-visible claims. | Must resolve before publication. |
| Source roles | SourceDescriptor/source-role refs and caveats. | Must preserve source-role anti-collapse. |
| Policy | PolicyDecision refs and release/promotion gate outcomes. | Required for release gate closure. |
| Promotion | PromotionDecision refs for relevant lifecycle transitions. | Required where material transition is governed. |
| Rights | license, terms, attribution, redistribution, export, embargo, rights uncertainty. | Unknown rights fail closed. |
| Sensitivity | redaction, generalization, restricted/quarantine posture, withheld details. | Sensitive exact values must not leak. |
| Review | ReviewRecord refs, reviewer roles, separation-of-duties state. | Required where policy/materiality requires. |
| Attestations | signatures, DSSE/SLSA/in-toto/build/provenance refs. | Digest-bound and auditable. |
| Receipts/proofs | validation, transformation, redaction, aggregation, release receipts, proof refs. | Must remain in proof/receipt homes. |
| Correction lineage | CorrectionNotice, withdrawal, supersession, stale-state, invalidation list refs. | No silent mutation. |
| Rollback | rollback target, rollback card, prior release ref, restoration/invalidation plan. | Required unless explicitly waived. |
| Time | decided, built, validated, published, effective, valid, superseded, withdrawn times. | Time kinds should be explicit. |

---

## Field semantics

### `id`

Canonical release manifest identifier.

Requirements:

- stable enough to cite from public clients, catalogs, release indexes, receipts, proofs, and rollback cards;
- specific to a release event or release package, not a mutable `latest` pointer;
- safe to expose publicly when release policy allows.

PROPOSED convention:

```text
release:<domain-or-surface>:<yyyy-mm-dd>:<sequence-or-hash>
```

### `spec_hash`

Deterministic hash claiming spec or content lineage.

Current schema makes it optional; production-grade releases should include it or a stronger digest set. The hash should be computed from canonicalized release content or accepted manifest canonicalization rules.

### `version`

Release/object version string.

Current schema makes it optional. Mature release usage should include version or equivalent release lineage marker to support comparison, rollback, supersession, cache invalidation, and audit.

---

## Invariants

CONFIRMED by paired schema:

- `id` is required.
- `spec_hash` is optional and string-shaped if present.
- `version` is optional and string-shaped if present.
- Additional properties are currently allowed.

PROPOSED semantic invariants:

- A release manifest must not be a floating `latest` pointer.
- A production release manifest should include deterministic digest/spec lineage.
- A release manifest should list or reference every artifact included in the release.
- Every release-visible claim that depends on evidence must link to resolvable EvidenceBundle support.
- Release policy and promotion decisions must be recorded before a release is treated as PUBLISHED.
- Rights, sensitivity, review, correction, and rollback posture must be explicit or fail closed.
- Release manifests do not store release artifacts, proofs, receipts, raw data, work data, quarantine data, UI state, or AI output.
- A new release, correction, withdrawal, or rollback should supersede prior manifests without silently mutating them.
- Public clients should bind to release manifests and governed APIs, not raw/candidate/internal stores.

---

## Lifecycle role

`ReleaseManifest` is created at the release/publish handoff:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Expected use:

| Lifecycle point | Role |
|---|---|
| RAW / WORK / QUARANTINE | No public release manifest. Candidate refs may exist, but not public release. |
| PROCESSED | Release preparation may start; evidence/validation closure still required. |
| CATALOG / TRIPLET | Release candidate can be assembled and evaluated. |
| PUBLISHED | ReleaseManifest binds approved artifact set for public/restricted consumption. |
| Correction | Superseding ReleaseManifest or correction-linked manifest preserves public audit trail. |
| Rollback | ReleaseManifest references prior release/rollback card and invalidation path. |
| Withdrawal | Manifest lineage records withdrawal posture and successor/null release state. |

---

## Boundaries

| Boundary | Rule |
|---|---|
| Contract vs schema | This contract defines meaning; schema defines machine shape. |
| Contract vs policy | Policy decides admissibility; manifest records or references outcomes. |
| ReleaseManifest vs PromotionDecision | PromotionDecision records transition approval/denial/abstention; ReleaseManifest binds released contents. |
| ReleaseManifest vs PolicyDecision | PolicyDecision records policy gate outcome; ReleaseManifest references policy outcomes. |
| ReleaseManifest vs EvidenceBundle | EvidenceBundle is evidence authority; manifest references evidence closure. |
| ReleaseManifest vs receipts/proofs | Manifest references receipts/proofs; it is not the proof store. |
| ReleaseManifest vs release artifacts | Manifest identifies artifacts; it does not store payloads. |
| ReleaseManifest vs public API/UI/map/AI | Public surfaces are downstream and must use governed interfaces. |

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- harden schema beyond current `id`-only required surface;
- decide required fields for production release manifests;
- validator existence and wiring for `tools/validators/release/validate_release_manifest.py`;
- fixture coverage under `fixtures/release/release_manifest/`;
- release policy behavior under `policy/release/`;
- release artifact storage conventions under `release/`;
- proof/receipt binding and signing/attestation strategy;
- rollback, correction, withdrawal, supersession, and cache invalidation tests;
- public client tests proving binding to release manifests rather than raw/latest/internal sources.

---

## Fixtures

Minimum fixture set PROPOSED:

| Fixture | Purpose |
|---|---|
| `valid_minimal_schema.json` | Confirms current schema permits `id` only. |
| `valid_recommended_release.json` | Demonstrates mature manifest with contents, digests, evidence, policy, rights, sensitivity, review, rollback. |
| `valid_map_release_manifest_link.json` | Demonstrates map/layer release references. |
| `valid_correction_supersession.json` | Demonstrates correction/supersession lineage. |
| `valid_rollback_manifest.json` | Demonstrates rollback target and prior release ref. |
| `invalid_missing_id.json` | Confirms current required field. |
| `governance_invalid_missing_evidence.json` | Schema may pass; release governance should fail. |
| `governance_invalid_missing_rollback.json` | Schema may pass; release governance should fail. |
| `governance_invalid_unknown_rights.json` | Schema may pass; policy should fail closed. |
| `governance_invalid_floating_latest.json` | Demonstrates no floating latest pointers. |

Fixtures must use synthetic or safe refs only.

---

## Open questions

- When should the schema move from permissive placeholder to closed, explicit release shape?
- Should `contents[]`, `digests`, `evidence_refs[]`, `rollback_target`, and `time` become required fields in the next schema version?
- Should `MapReleaseManifest`, `LayerManifest`, `TileArtifactManifest`, and `StyleManifest` be nested under `ReleaseManifest.contents[]` or remain separate linked objects?
- Which signing/attestation fields are mandatory for public release?
- Which release root stores persisted manifest instances?
- Which gate owns final release authority and separation-of-duties enforcement?

---

## Rollback

Rollback is required if this contract is used to store release artifacts, bypass schema/policy/review/evidence gates, treat a manifest as publication approval without gate closure, silently mutate public release state, bypass correction/rollback lineage, or authorize public API/UI/map/AI exposure directly.

Rollback target for this expansion: previous blob SHA `58327f2ad480d150b30952e8b7725fe40ebd4e19`.

<p align="right"><a href="#top">Back to top</a></p>
