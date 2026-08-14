<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0023-geo-manifest-signs-every-pmtiles-cog-release
title: "ADR-0023 — Geo Manifest Signs Every PMTiles and COG Release"
type: adr
adr_id: ADR-0023
version: v1.3
status: proposed
effective_decision_status: proposed
owners:
  - "NEEDS VERIFICATION — architecture decision owner"
  - "NEEDS VERIFICATION — geospatial artifact and tile steward"
  - "NEEDS VERIFICATION — release and publication steward"
  - "NEEDS VERIFICATION — evidence, contracts, schemas, policy, validation, security, correction, and rollback stewards"
reviewers_required:
  - Architecture steward
  - Docs steward
  - Geospatial artifact and tile steward
  - Release and publication steward
  - Evidence and proof steward
  - Contracts and schemas stewards
  - Policy and sensitivity steward
  - Security and signing reviewer
  - Validation and CI steward
  - Correction and rollback steward
created: 2026-05-09
updated: 2026-08-14
policy_label: public
truth_posture: cite-or-abstain
owning_root: docs/
responsibility_root: docs/
responsibility: "Record the proposed cryptographic binding and fail-closed release boundary for PMTiles and COG artifacts without claiming current signature, release, or publication authority."
current_path: docs/adr/ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md
supersedes: []
superseded_by: []
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: c9ccb11ded141edbd79763982056a1e6f90b8866
  target_prior_blob: d57353d059383860a43fc129c1f39f3173f69119
  adr_index_blob: 938c5894c36b99e14810918e2c550ab0e92d53b1
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  geo_manifest_contract_blob: c7993b8bf8fbcbf01f0947a99a14d81509e89370
  geo_manifest_fixture_readme_blob: b0af76ac26f2720a34d23e169fb47faf7f8db028
  geo_manifest_test_blob: 680fec23e284df633c2f8edb1dd499c51a3649f9
  geo_manifest_workflow_blob: fa476a9d2d3ee7c855d1d86debd68de332ac7554
  generated_receipt_blob: fbb0f5dda2feb53f983d64ed880fbf3090c5c7fa
  pmtiles_attestation_standard_blob: 372845bd9ee9877a96de2d01d824e003d22010b5
  pmtiles_shape_verifier_blob: 566c4393241a7eb519c0d8c7d88bb32128347d62
  latest_geo_manifest_workflow_run: 31654973070
  latest_geo_manifest_workflow_head: 3911c519d9bc134c3ab0662fed6577ebd966813b
  latest_geo_manifest_workflow_result: "functional schema, fixture, and test steps passed; generated authoring receipt integrity failed because the workflow digest drifted"
inspection_boundary: >
  Current-session GitHub reads covered the canonical ADR index, accepted ADR-0029,
  adopted Directory Rules bytes, this ADR, the KFMGeoManifest contract, closed schema,
  fixture corpus, validator, focused tests, dedicated workflow, latest workflow jobs and
  logs, generated authoring receipt, PMTiles attestation standard, PMTiles shape-only
  verifier, COG standard, release/signature documentation, and bounded repository searches.
  No signer, trust root, key registry, transparency log, real PMTiles or COG release
  payload, public alias, CDN, deployment, production release, correction, withdrawal,
  or rollback execution was exercised. The continuity compare from the initial inspection
  base to this evidence base changed only unrelated geology and runtime-response files; no
  ADR-0023 or inspected geo-manifest, PMTiles-attestation, COG, release, or signing evidence
  path changed.
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md
  - docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md
  - docs/adr/ADR-0018-promotion-gate-sequence.md
  - docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
  - docs/adr/ADR-0024-steward-separation-of-duties-for-release.md
  - docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/evidence/kfm_geo_manifest.md
  - schemas/contracts/v1/evidence/kfm_geo_manifest.schema.json
  - fixtures/evidence/kfm_geo_manifest/README.md
  - tools/validators/evidence/validate_kfm_geo_manifest.py
  - tests/validators/test_validate_kfm_geo_manifest.py
  - .github/workflows/kfm-geo-manifest-validation.yml
  - data/receipts/generated/genrec-kfm-geo-manifest-validation-20260804.json
  - docs/standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md
  - tools/attest/verify_cose.py
  - .github/workflows/pmtiles-attestation.yml
  - docs/standards/COG.md
  - data/published/pmtiles/README.md
  - data/published/layers/README.md
  - release/manifest/README.md
  - release/manifests/README.md
  - release/signatures/README.md
  - tools/attest/README.md
  - .github/workflows/promotion-gate.yml
tags: [kfm, adr, geospatial, pmtiles, cog, geo-manifest, dsse, signature, integrity, release, evidence, rollback, trust-membrane]
notes:
  - "v1.3 is a same-path current-main evidence refresh. It preserves source and effective status `proposed`; it does not accept ADR-0023, implement signing, alter promotion, or publish anything."
  - "A closed fixture-first KFMGeoManifest schema, deterministic validator, synthetic fixture corpus, focused tests, and read-only workflow now exist. Their authority is metadata and local-byte consistency only."
  - "The PMTiles split-bundle attestation lane now proves bounded structural reconciliation, but PMSIG verification remains shape-only and fails closed when cryptographic verification is requested."
  - "The latest dedicated KFMGeoManifest workflow passed its functional tests, fixture polarity, and schema checks but failed generated-receipt integrity because the workflow bytes no longer match the historical authoring receipt."
  - "No real COG format validator, cryptographic signer/trust-root profile, policy evaluation, release integration, serving enforcement, or correction/rollback drill was proved."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0023 — Geo Manifest Signs Every PMTiles and COG Release

> **Proposed decision.** Before any PMTiles or Cloud-Optimized GeoTIFF artifact becomes a released public-safe carrier, KFM must bind the immutable artifact bytes to identity, evidence, provenance, policy, release, correction, and rollback state through a cryptographically verifiable `KFMGeoManifest` payload and envelope. Missing, mismatched, unverifiable, superseded, revoked, withdrawn, or policy-inadmissible bindings fail closed.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![ADR ID: confirmed](https://img.shields.io/badge/ADR--0023-confirmed-0969da?style=flat-square)](#current-repository-evidence)
[![Metadata profile: fixture-first](https://img.shields.io/badge/metadata-fixture--first%20implemented-1f6feb?style=flat-square)](#bounded-profile-register)
[![Signing: hold](https://img.shields.io/badge/signing-HOLD-b42318?style=flat-square)](#current-implementation-maturity)
[![Workflow: degraded](https://img.shields.io/badge/workflow-functional%20PASS%20%7C%20receipt%20drift-f59e0b?style=flat-square)](#hosted-workflow-evidence)
[![Publication: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-and-publication-boundary)

> [!IMPORTANT]
> **Identity is confirmed; acceptance is not.** [`docs/adr/INDEX.md`](./INDEX.md) uniquely assigns `ADR-0023` to this exact file with source and effective status `proposed`. ADR-0029 accepts the Directory Rules placement authority, not this geo-manifest decision. Editing, merging, validating, or linking this Markdown cannot accept ADR-0023.

> [!CAUTION]
> **Fixture-first validation is implemented; signed-release enforcement is not.** The repository now has a closed proposed `KFMGeoManifest` schema, deterministic no-network validator, synthetic valid/invalid fixtures, focused tests, and a read-only workflow. They prove bounded metadata consistency and optional exact local-byte binding only. They do not verify PMTiles or COG format conformance, signatures, evidence resolution, policy, accountable review, promotion, release, deployment, or publication.

> [!WARNING]
> **PMTiles structural attestation is not cryptographic verification.** The separate split-bundle lane reconciles PMTiles, PMIDX, a PMSIG subject, and a RunReceipt structurally. Its verifier explicitly requires `--shape-only` for fixture use and otherwise returns `PMSIG_CRYPTOGRAPHIC_VERIFICATION_UNWIRED`. Structural success must never be displayed as a trusted signature.

> [!WARNING]
> **Current CI is not fully green.** In the latest inspected `kfm-geo-manifest-validation` run, all 15 focused tests, fixture polarity, schema meta-validation, and hash-reporting steps passed. The run failed only when the historical generated authoring receipt no longer matched the current workflow bytes. That failure is real process-memory drift; it is not evidence that the functional validator failed, and it is not safe to ignore.

**Quick navigation:** [Status](#status) · [Evidence](#evidence-boundary) · [Context](#context) · [Decision](#proposed-decision) · [Binding](#proposed-binding-model) · [Profiles](#bounded-profile-register) · [Scope](#scope) · [Authority](#authority-and-publication-boundary) · [Validation](#validation-and-finite-outcomes) · [Flow](#proposed-release-flow) · [Current evidence](#current-repository-evidence) · [Workflow](#hosted-workflow-evidence) · [Maturity](#current-implementation-maturity) · [Convergence](#implementation-and-convergence-plan) · [Acceptance](#acceptance-gates) · [Consequences](#consequences) · [Alternatives](#alternatives-considered) · [Risks](#risk-and-open-question-ledger) · [Rollback](#rollback-and-supersession) · [Checklist](#verification-checklist) · [References](#references) · [History](#revision-history)

---

<a id="status"></a>

## Status

| Field | Current value |
|---|---|
| **ADR ID** | `ADR-0023` — unique and confirmed in [`INDEX.md`](./INDEX.md) |
| **Tracked path** | `docs/adr/ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md` |
| **Source metadata** | `proposed` |
| **Effective decision status** | `proposed` |
| **Decision class** | Geospatial artifact integrity, cryptographic release binding, public-serving boundary, correction, and rollback |
| **Directory authority** | ADR-0029 is accepted and adopts the exact Directory Rules v2 bytes; `docs/adr/` remains the owning responsibility lane |
| **Current repository posture** | Fixture-first metadata and local-byte validation implemented; PMTiles structural bundle validation partial; cryptographic, policy, release, COG-format, serving, and rollback controls held or unknown |
| **Implementation effect of this revision** | Documentation only |
| **Release/publication effect** | None |
| **Supersedes / superseded by** | None / none |

### Acceptance versus implementation graduation

Two states remain independent:

1. **ADR acceptance** would approve the required PMTiles/COG artifact-binding model, object separation, and fail-closed release rule.
2. **Implementation graduation** requires production-grade profiles, cryptographic verification, signer policy, trust roots, policy/review resolution, promotion and release integration, public-serving enforcement, correction, withdrawal, and rollback evidence.

The current fixture-first implementation is useful progress below the graduation threshold. A closed schema, matching digest, green structural test, generated receipt, pull request, merge, or signature-shaped JSON file cannot independently accept this ADR or create `PUBLISHED` state.

[Back to top](#top)

---

<a id="evidence-boundary"></a>

## Evidence boundary

This edition is grounded in repository bytes at `main@c9ccb11ded141edbd79763982056a1e6f90b8866`. The current target prior blob is `d57353d059383860a43fc129c1f39f3173f69119`.

| Evidence level | What is established | What remains unproved |
|---|---|---|
| ADR inventory | ADR-0023 uniquely maps to this path and remains proposed | Acceptance |
| Directory governance | ADR-0029 accepts the exact Directory Rules v2 bytes | Acceptance of this decision or any release profile |
| Semantic contract | `contracts/evidence/kfm_geo_manifest.md` v0.3 defines a fixture-first object boundary | Accepted release-grade contract |
| Machine schema | Closed Draft 2020-12 fixture profile exists | Signed envelope, released-state, trust-root, and production compatibility profiles |
| Validator and tests | Deterministic no-network validator and 15 focused tests exist | Evidence/policy resolution, format conformance, signing, or release authorization |
| Fixture corpus | Three valid, four schema-invalid, and eleven semantic/byte-invalid synthetic cases exist | Real PMTiles/COG production vectors or public release |
| PMTiles structural lane | Header, PMIDX, PMSIG-subject, and RunReceipt reconciliation is partially implemented | Cryptographic PMSIG verification and canonical profile authority |
| COG lane | Fixture-first manifest metadata includes a generalized COG candidate | Real COG layout/profile validation, signing, hosting, or release |
| Hosted workflow | Functional checks passed in the latest inspected run; generated-receipt integrity failed | Current exact-main green status and operational release readiness |
| Release and serving | Documentation and proposed lanes exist | Conforming release packet, trusted serving alias, CDN checks, cache invalidation, deployed verifier |

### Truth labels used here

- **CONFIRMED** — verified from current repository bytes, focused tests, workflow evidence, or accepted doctrine.
- **PROPOSED** — a decision, profile, shape, algorithm, path role, or enforcement target not accepted and proved.
- **PARTIAL** — a bounded subset is implemented but the named end-to-end capability is not.
- **CONFLICTED** — current surfaces compete or use incompatible authority, shape, identity, or path semantics.
- **NEEDS VERIFICATION** — a concrete check remains before reliance.
- **UNKNOWN** — available evidence cannot support a stronger claim.
- **HOLD** — a control intentionally blocks graduation or release.

[Back to top](#top)

---

<a id="context"></a>

## Context

PMTiles and COG are byte-range-friendly derived carriers. A browser, CDN, static host, service worker, or tile library may fetch immutable byte ranges without a trusted application server evaluating every request. A catalog record can describe an artifact, but it cannot prove that the bytes later served are the exact bytes reviewed and released.

KFM therefore needs an artifact-binding chain that can resolve:

- deterministic artifact and manifest identity;
- exact artifact bytes and optional range commitments;
- EvidenceRef/EvidenceBundle support and source roles;
- build/run provenance, transforms, tools, and parameters;
- rights, sensitivity, policy, and accountable review;
- promotion and release scope;
- correction, withdrawal, supersession, revocation, and rollback;
- public alias and cache state.

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A tile build, COG conversion, manifest, Merkle root, PMSIG file, shape check, pull request, merge, upload, URL, or workflow success is not promotion. Published carriers remain downstream of evidence, policy, review, release, correction, and rollback.

### Current convergence pressures this ADR must not hide

1. `KFMGeoManifest` now has a closed fixture-first profile, but it is deliberately fixed to `not_released` and does not contain a cryptographic envelope profile.
2. The PMTiles split-bundle lane (`PMTiles` + `PMIDX` + `PMSIG` + `RunReceipt`) is structurally richer for PMTiles but remains a compatibility profile with unresolved canonical authority.
3. ADR-0013 still owns the repository-wide identity grammar. The local `kfm-fixture-json-v1` hash profile must not be mistaken for an accepted cross-runtime canonicalization decision.
4. `release/manifest/` and `release/manifests/` remain distinct tracked draft lanes whose final responsibility split is unresolved here.
5. `release/signatures/` documents human reviewer signoff packets, not machine cryptographic artifact bindings.
6. The latest dedicated geo-manifest workflow is degraded by a stale generated authoring receipt even though all functional manifest checks passed.
7. The COG standard remains documentation-rich but no real COG layout validator, production fixture, or signed release was verified.

[Back to top](#top)

---

<a id="proposed-decision"></a>

## Proposed decision

Upon acceptance and implementation graduation:

1. Every released PMTiles or COG artifact **MUST** have one immutable, version-bound `KFMGeoManifest` payload and one approved cryptographic envelope binding that payload.
2. Public release **MUST** be denied when the payload, envelope, artifact digest, signer authorization, trust proof, evidence, policy, review, promotion, release, correction, or rollback prerequisite is missing, invalid, mismatched, expired where policy defines expiry, superseded, revoked, withdrawn, or inadmissible.
3. Catalog records, layer/tile manifests, receipts, proofs, reviewer signoffs, `PromotionDecision`, and `ReleaseManifest` **MUST** reference the binding where required; none replaces another object family.
4. The canonical payload **MUST NOT** embed the envelope or signature that signs it.
5. `spec_hash` **MUST** be computed over a schema-defined hash projection that excludes `spec_hash` itself, the envelope, signatures, transparency proofs, and transport-only fields.
6. Artifact-byte identity **MUST** remain distinct from manifest identity. The full-file digest binds bytes as written; an optional accepted range-verification root may accelerate or localize verification but cannot replace the full-file digest without an accepted successor decision.
7. Signing and verification **MUST** use an accepted, version-pinned DSSE/cosign, COSE, or successor profile with explicit payload type, signer policy, trust roots, rotation, revocation, transparency/offline proof, and failure behavior.
8. A release transition **MUST** still require independent evidence, rights, sensitivity, policy, accountable review, `PromotionDecision`, `ReleaseManifest`, correction, and rollback closure.
9. Artifact and binding history **MUST** be append-only under retention and sensitivity policy. Unsafe releases are superseded, withdrawn, corrected, revoked, or rolled back—not silently overwritten or deleted.
10. Public aliases and clients **MUST** resolve only to artifacts whose required binding profile remains valid for the requested audience and release state.

### Normative language boundary

`MUST`, `MUST NOT`, `SHOULD`, and `MAY` describe the proposed accepted state. They do not describe current repository enforcement.

[Back to top](#top)

---

<a id="proposed-binding-model"></a>

## Proposed binding model

### Object separation

| Object | Responsibility | Must not be treated as |
|---|---|---|
| PMTiles/COG artifact | Immutable released carrier bytes | Source truth, evidence closure, or release decision |
| `KFMGeoManifest` payload | Artifact metadata, byte identity, spatial meaning, provenance refs, governance refs, lifecycle refs | Signature envelope, `ReleaseManifest`, or proof that refs resolve |
| Cryptographic envelope | Binds payload bytes to signer identity under one approved profile | Human review, policy allow, evidence truth, or release authority |
| `PMIDX` / range profile | Optional PMTiles chunk/range commitments under a versioned profile | Full release packet or artifact semantics |
| `PMSIG` compatibility object | PMTiles signature subject/carrier used by the split-bundle lane | Trusted signature until cryptographically verified against an approved key registry |
| `RunReceipt` | Process memory: inputs, tools, parameters, outcomes | Evidence truth, artifact signature, or release approval |
| `EvidenceRef` / `EvidenceBundle` | Claim-scoped support and resolved evidence | Artifact digest, policy decision, or release manifest |
| `PolicyDecision` | Rights, sensitivity, access, signer, and obligation decision | Byte integrity or human review |
| Reviewer signature packet | Accountable human signoff trail | Cryptographic artifact signature |
| `ProofPack` / validation reports | Proof that bounded checks ran and passed | Release state or source truth |
| `CatalogMatrix` / STAC/DCAT/PROV | Discovery and provenance projections | Artifact signature, promotion, or publication |
| `PromotionDecision` | Governed state-transition decision | Artifact bytes or manifest payload |
| `ReleaseManifest` | Release scope, artifact set, versions, and rollback target | Per-artifact byte binding or evidence truth |
| Correction/withdrawal/rollback records | Governed repair, invalidation, and transition intent | Proof that execution and cache propagation completed |

### Payload and envelope layering

The target model separates a canonical payload from the cryptographic carrier:

```text
<artifact>.kfm-geo-manifest.dsse.json   # illustrative; filename/profile remains a decision
└── envelope
    ├── payloadType
    ├── payload          # encoded canonical KFMGeoManifest bytes
    └── signatures[]
```

COSE or a successor envelope may be selected instead of DSSE only through a versioned profile that preserves the same separation and verification obligations. Existing `.kfm-geo-manifest.json`, `.pmidx`, and `.pmsig` naming may require a compatibility window; filenames do not define authority.

### Minimum release-grade payload profile

A future accepted release profile should close unknown properties and define at least:

| Group | Required information |
|---|---|
| Identity | manifest `id`, object/schema/profile version, deterministic `spec_hash`, release ID |
| Artifact | stable artifact ref, artifact kind, media type, byte length, format/profile version |
| Integrity | algorithm-tagged full-file digest; optional accepted range-root/chunk profile |
| Spatial | CRS, extent/bbox, geometry/raster/tiling profile, zoom or resolution |
| Scope | claim, geography, audience, and temporal scope |
| Provenance | RunReceipt/build refs, source descriptors and roles, EvidenceRefs/Bundles, transforms, tools/config identities |
| Governance | rights, sensitivity, policy decision, review record, obligations, signer policy |
| Release | promotion decision, release manifest, immutable release state, public-use audience |
| Lifecycle | supersedes, correction, withdrawal, revocation, rollback target and prior release refs |
| Verification | envelope/profile, expected signer class, trust root, transparency/offline proof, verification time and result refs |

The implemented fixture profile is intentionally narrower: it fixes `release_state = not_released`, `release_manifest_ref = null`, `public_use_allowed = false`, and `authority_created = false`.

### Hash domains

Three identities remain separate:

| Identity | Purpose | Current posture |
|---|---|---|
| `spec_hash` | Deterministic identity over a declared manifest projection | Fixture profile implemented locally; repository-wide authority remains proposed under ADR-0013 |
| Artifact digest | Digest of complete PMTiles/COG bytes as written | Exact local-byte SHA-256 binding implemented for synthetic fixtures; production profiles unproved |
| Range-verification root | Optional chunk/range commitment for efficient partial verification | PMTiles structural compatibility profile exists; canonical semantics and authenticated range metadata remain unresolved |

No digest proves evidence sufficiency, rights, sensitivity, accountable review, release, or public safety by itself.

[Back to top](#top)

---

<a id="bounded-profile-register"></a>

## Bounded profile register

The current repository contains multiple related but non-equivalent profiles. They must converge deliberately rather than silently becoming parallel authority.

| Profile | CONFIRMED capability | Explicit non-effects | Current status |
|---|---|---|---|
| `KFMGeoManifest` fixture-first v1 | Closed metadata shape; profile-local deterministic `spec_hash`; artifact/media, spatial, transform, governance, time, lineage, and optional exact local-byte checks | No format conformance, signature, evidence resolution, policy evaluation, release, deployment, publication, or public use | **PARTIAL / fixture-first** |
| PMTiles split-bundle compatibility | PMTiles v3 header/metadata, whole-file SHA-256, PMIDX leaves/root/ranges, PMSIG subject shape, one RunReceipt, and optional declared-manifest reconciliation | No trusted PMSIG cryptography, canonical schema/profile selection, policy, promotion, release, correction, or rollback | **PARTIAL / structural** |
| PMTiles PMSIG verifier | Bounded JSON/shape validation and finite error codes | No approved COSE library, key registry, trust-root evaluation, or cryptographic verification | **HOLD / shape-only** |
| COG documentation/profile | Proposed COG production, STAC, release, and manifest rules; one synthetic generalized COG manifest fixture | No real COG parser/layout validation, production payload, signature, hosting, or release | **HOLD / documentation + metadata fixture** |
| Promotion workflow | Read-only readiness/hold evidence | No artifact digest/signature verification, promotion, release, or publication | **WORKFLOW_HOLD** |

### Anti-collapse rules

- A `KFMGeoManifest` fixture pass does not imply a valid PMTiles or COG file.
- A PMTiles structural bundle pass does not imply a valid cryptographic signature.
- A valid cryptographic signature would not imply evidence, policy, review, promotion, or release closure.
- A `ReleaseManifest` reference does not bind artifact bytes unless the referenced artifact binding verifies.
- A human signoff packet cannot substitute for a machine signature, and a machine signature cannot substitute for human review.
- A generated authoring receipt records authorship/process memory; it is not release proof and its drift remains a real validation defect.

[Back to top](#top)

---

<a id="scope"></a>

## Scope

### In scope

- PMTiles v3 release artifacts;
- released Cloud-Optimized GeoTIFF files;
- accepted PMTiles delta artifacts when a governed delta profile exists;
- one-artifact payload/envelope identity and immutable byte binding;
- optional versioned range/chunk verification;
- evidence, provenance, rights, sensitivity, review, promotion, release, correction, withdrawal, revocation, and rollback references;
- build-time, promotion-time, serving-time, offline, periodic, and incident verification requirements;
- public and restricted release profiles with sensitivity-appropriate transparency behavior;
- migration from current fixture and compatibility profiles toward one governed release-grade model.

### Out of scope

- per-tile or per-range cryptographic envelopes as the default;
- raw/source-side signing under `data/raw/`;
- MapLibre style, legend, layer order, popup, or UI semantics;
- 3D Tiles, glTF, terrain, and scene formats unless a successor/profile explicitly includes them;
- accepting ADR-0013 identity grammar or resolving release-manifest singular/plural paths in this document;
- selecting production keys, signer identities, transparency service, HSM/KMS, registry, CDN, or hosting provider;
- authorizing any current artifact for release;
- repairing the stale generated authoring receipt in this documentation-only update.

### Directory Rules basis

This ADR creates no root or parallel authority. Accepted ADR-0029 adopts the Directory Rules responsibility split:

| Responsibility | Owning surface |
|---|---|
| Architecture decision | `docs/adr/` |
| Operational standards | `docs/standards/` |
| Semantic meaning | `contracts/evidence/kfm_geo_manifest.md` and accepted sibling contracts |
| Machine shape | `schemas/contracts/v1/evidence/kfm_geo_manifest.schema.json` and accepted profile schemas |
| Policy | `policy/` under a separately accepted profile |
| Validation and attestation code | `tools/`, accepted packages, tests, and fixtures |
| Candidate/released bytes | governed lifecycle lanes under `data/` |
| Receipts and proofs | `data/receipts/` and `data/proofs/` |
| Release decisions, manifests, signoff, correction, and rollback | `release/` under the accepted responsibility distinction |
| CI orchestration | `.github/workflows/` with read-only defaults until release authority is separately approved |

[Back to top](#top)

---

<a id="authority-and-publication-boundary"></a>

## Authority and publication boundary

A valid cryptographic binding would prove only that a verifier accepted declared payload bytes and signer evidence under a named profile, and that referenced artifact bytes matched declared integrity values at verification time. It would not independently prove:

- that source or domain claims are true;
- that an EvidenceBundle is sufficient or admissible;
- that rights permit publication;
- that sensitive detail is public-safe;
- that review was accountable or independent;
- that promotion or release was authorized;
- that a public alias, CDN, service worker, or cache points to the selected artifact;
- that correction, withdrawal, revocation, or rollback propagated successfully.

Public clients must consume release-resolved artifacts through governed interfaces or approved integrity-bound static-delivery profiles. They must not read RAW, WORK, QUARANTINE, internal proof/receipt lanes, or candidate artifacts directly.

No change to this ADR, contract, schema, validator, fixture, workflow, receipt, PMIDX, PMSIG, signature, manifest, URL, or file placement creates `PUBLISHED` state.

[Back to top](#top)

---

<a id="validation-and-finite-outcomes"></a>

## Validation and finite outcomes

### Current fixture-first validator

The implemented validator deterministically checks the proposed fixture profile without network access. It covers:

- closed Draft 2020-12 shape;
- duplicate-key, non-finite-number, recursion, size, symlink, FIFO, and non-regular-file safety;
- profile-local `spec_hash` calculation excluding the `spec_hash` field;
- artifact type/media-type agreement;
- bbox order and EPSG:4326 ranges;
- PMTiles tiling and zoom consistency;
- ordered transform-chain continuity and final artifact digest;
- receipted generalization/redaction transforms;
- rights, sensitivity, policy, review, and rollback refs for public-bound candidates;
- temporal ordering and safe lineage;
- canonical reference arrays; and
- optional exact local payload length and SHA-256 binding.

A pass proves only those checks for the provided candidate. The fixture payloads are synthetic UTF-8 bytes, not real production PMTiles or COG files.

### Future signed-release validator

A release-grade validator must add deterministic, machine-readable, offline-capable core checks and fail closed:

| Check family | Required checks |
|---|---|
| Envelope | approved media type/profile, payload decode, signature structure, signer policy |
| Payload | closed release schema, profile/version, conditional PMTiles/COG fields |
| Identity | accepted canonicalization/hash projection, algorithm tags, no circular fields |
| Format | real PMTiles v3 or COG format conformance using pinned parsers and production vectors |
| Bytes | byte length, full-file digest, optional range-root/chunk validation |
| Provenance | build/run receipts, source roles, evidence refs, transforms, tools/config |
| Governance | rights, sensitivity, policy, review, signer authorization, obligations |
| Release | promotion decision, release manifest, correction, withdrawal, rollback |
| Serving | immutable URI, public alias binding, audience, cache state, no candidate/revoked exposure |
| History | append-only supersession, revocation, withdrawal, and retained audit refs |

### Stable outcome classes

| Outcome | Meaning |
|---|---|
| `PASS` | Every check required by the selected profile passed |
| `DENY` | Known invalid, prohibited, revoked, mismatched, or unauthorized state |
| `HOLD` | Review, ownership, signer policy, rights, sensitivity, profile authority, or release prerequisite unresolved |
| `ABSTAIN` | Evidence/provenance resolution insufficient for a substantive release claim |
| `ERROR` | Tooling, schema, verifier, storage, or infrastructure failure prevented a valid determination |

`ERROR` is never converted into `PASS`. Missing cryptographic capability, an unavailable trust root, unsupported profile, or stale integrity receipt must not silently permit release.

### Minimum reason-code families

- `geo_manifest_missing`
- `geo_manifest_schema_invalid`
- `geo_manifest_hash_projection_invalid`
- `artifact_format_invalid`
- `artifact_digest_mismatch`
- `range_root_or_range_metadata_invalid`
- `signature_missing_or_invalid`
- `cryptographic_verification_unwired`
- `signer_not_authorized`
- `transparency_or_offline_proof_missing`
- `evidence_or_receipt_unresolved`
- `policy_or_sensitivity_denied`
- `review_or_separation_of_duties_unresolved`
- `release_manifest_unresolved`
- `promotion_decision_unresolved`
- `release_state_not_public`
- `superseded_revoked_or_withdrawn`
- `public_alias_binding_mismatch`
- `rollback_target_unverifiable`
- `generated_receipt_integrity_mismatch`

[Back to top](#top)

---

<a id="proposed-release-flow"></a>

## Proposed release flow

```mermaid
flowchart LR
    A[Admissible evidence and sources] --> B[Build PMTiles or COG candidate]
    B --> C[Validate real format and compute byte identity]
    C --> D[Emit canonical KFMGeoManifest payload]
    D --> E[Compute accepted spec_hash projection]
    E --> F[Wrap payload in approved cryptographic envelope]
    F --> G[Sign under approved signer and trust policy]
    G --> H[Validate format, hashes, signature, evidence, policy, review, release]
    H -->|DENY / HOLD / ABSTAIN / ERROR| Q[QUARANTINE or no publication]
    H -->|PASS| R[PromotionDecision and ReleaseManifest]
    R --> P[Publish immutable artifact plus binding]
    P --> S[Verify alias, CDN, service worker, and range requests]
    S --> M[Monitor, correct, withdraw, revoke, or roll back]
```

### Promotion-gate contribution

The artifact-binding check is a prerequisite within—not a replacement for—the promotion sequence:

| Promotion concern | Geo-manifest contribution |
|---|---|
| Schema valid | Payload, envelope, and selected artifact profile validate |
| Inputs pinned | Source, evidence, receipt, tool, configuration, and artifact refs resolve |
| Checks pass | Real format, full-file digest, and optional range profile verify |
| Signatures valid | Cryptographic binding, signer authorization, and trust proof verify |
| Provenance complete | Receipts, evidence, transforms, lineage, catalog, and release refs resolve |
| No policy violations | Rights, sensitivity, audience, review, signer, and serving posture allow |
| Release ready | Promotion, release, correction, withdrawal, and rollback records close |

The current `.github/workflows/promotion-gate.yml` does not perform the complete chain. The current `kfm-geo-manifest-validation` and `pmtiles-attestation` workflows are bounded read-only validation/readiness surfaces, not publishers.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

| Surface | Current verified state | Safe conclusion |
|---|---|---|
| ADR identity | Unique ADR-0023 row points to this file; source/effective status proposed | Identity confirmed; decision not accepted |
| Directory authority | ADR-0029 accepts Directory Rules v2 | Existing responsibility roots govern placement; no release authority created |
| Geo-manifest contract | v0.3 fixture-first semantic contract exists | Meaning and bounded non-effects documented |
| Geo-manifest schema | Closed Draft 2020-12 fixture profile exists | Not a signed released-state schema |
| Validator | `tools/validators/evidence/validate_kfm_geo_manifest.py` exists and is substantive | Deterministic metadata/local-byte checks established |
| Fixtures | Synthetic valid/invalid corpus exists | Exact polarity established; production format conformance unproved |
| Tests | 15 focused no-network tests exist and passed in the latest inspected run | Functional fixture profile is exercised |
| Dedicated workflow | Read-only profile workflow exists | Current overall result degraded by generated-receipt drift |
| Generated authoring receipt | Historical receipt exists but no longer matches current workflow bytes | Process-memory integrity is stale and requires a separate corrective slice |
| PMTiles attestation standard | Structural compatibility profile documents implemented header/PMIDX/PMSIG/receipt checks | Canonical profile and trusted cryptography unresolved |
| PMSIG verifier | Shape validation and finite reason codes exist | Cryptographic verification intentionally unwired |
| COG standard | Draft standard and proposed release flow exist | Real COG format validator/release proof unverified |
| Release manifests | Singular and plural draft lanes both exist | Final responsibility distinction remains conflicted |
| Release signatures | Human signoff-packet lane exists | Not cryptographic artifact binding |
| Attestation tooling | Documentation and shape-only tooling exist | Production signer, trust roots, rotation, revocation, transparency unknown |
| Promotion workflow | Read-only readiness/hold surface | No complete artifact-signature-release enforcement |
| Public serving | Published PMTiles/layer documentation and client surfaces exist | No inspected production alias/CDN anti-bypass proof |

### Confirmed present versus not proved

The earlier v1.2 statements that the geo-manifest validator and fixtures were absent are now superseded by current repository evidence. This update does **not** infer the following missing end-to-end capabilities from their presence:

- approved cryptographic signature verification;
- trusted signer/key registry and revocation;
- real PMTiles/COG format conformance under the geo-manifest profile;
- evidence, policy, or review authentication;
- promotion/release integration;
- deployed public-serving verification;
- correction, withdrawal, cache invalidation, or rollback execution.

[Back to top](#top)

---

<a id="hosted-workflow-evidence"></a>

## Hosted workflow evidence

The latest inspected `kfm-geo-manifest-validation` run is `31654973070` at commit `3911c519d9bc134c3ab0662fed6577ebd966813b`.

| Step | Result |
|---|---|
| Install declared test dependencies | PASS |
| 15 focused no-network tests | PASS |
| Exact fixture polarity and byte binding | PASS |
| Draft 2020-12 meta-schema check | PASS |
| Authoring artifact hash report | PASS |
| Generated authoring receipt integrity | FAIL — `ARTIFACT_DIGEST_MISMATCH` for the workflow path |

The logged current workflow digest differed from the digest stored in the historical receipt. The compare from that workflow head to the v1.3 evidence base spans broad unrelated repository work and does not show a later repair to this dedicated workflow or receipt. Therefore:

- **CONFIRMED:** the functional manifest profile passed in the latest inspected run;
- **CONFIRMED:** the workflow as a whole failed;
- **CONFIRMED:** the failure is generated-receipt integrity, not a schema, fixture, or validator failure;
- **NEEDS VERIFICATION:** a current exact-main rerun after a governed receipt repair;
- **DENY:** describing the dedicated workflow as green or current proof of release readiness.

The PMTiles attestation lane has separate exact-head success evidence for its structural checks after the finite hold-marker repair, but it still ends at shape-only cryptographic posture.

[Back to top](#top)

---

<a id="current-implementation-maturity"></a>

## Current implementation maturity

| Capability | Current state |
|---|---|
| ADR identity/status | **CONFIRMED / proposed** |
| Directory placement authority | **CONFIRMED / accepted ADR-0029** |
| Semantic contract | **PARTIAL / fixture-first v0.3** |
| Closed metadata schema | **PARTIAL / fixture-first** |
| Deterministic manifest validator | **CONFIRMED for bounded profile** |
| Synthetic fixture/test closure | **CONFIRMED for bounded profile** |
| Exact local artifact-byte binding | **PARTIAL / synthetic SHA-256 vectors** |
| Real PMTiles format validation | **PARTIAL / separate structural lane** |
| Real COG format validation | **HOLD / not established** |
| Canonicalization and identity authority | **CONFLICTED / ADR-0013 proposed** |
| Range-verification authority | **PARTIAL / PMTiles compatibility profile; unauthenticated metadata risk remains** |
| Cryptographic envelope and verification | **HOLD / unwired** |
| Signer and trust-root governance | **UNKNOWN** |
| Rights/sensitivity/policy execution | **HOLD / not established for release** |
| Promotion and release integration | **WORKFLOW_HOLD** |
| Release-manifest path authority | **CONFLICTED** |
| Public alias/CDN/client verification | **UNKNOWN** |
| Correction/withdrawal/revocation/rollback drill | **UNKNOWN / not established** |
| Dedicated geo-manifest CI | **DEGRADED — functional PASS, generated-receipt FAIL** |
| Production release or publication | **None proved** |

**Overall maturity: `PARTIAL / HOLD`.** KFM has useful metadata and structural proof slices, but it does not have an accepted operational signed-artifact release system.

[Back to top](#top)

---

<a id="implementation-and-convergence-plan"></a>

## Implementation and convergence plan

Use small, dependency-closed, reversible changes. Do not combine generation, signing, approval, and publication in one unreviewed path.

### Wave 0 — restore current validation integrity

- determine the legitimate reason the dedicated workflow bytes changed;
- generate a successor authoring receipt through the accepted producer rather than rewriting historical process memory;
- validate the successor receipt against exact branch bytes;
- obtain an exact-head green `kfm-geo-manifest-validation` run;
- keep this repair separate from ADR acceptance and cryptographic implementation.

### Wave 1 — decide authority and profile relationships

- accept, revise, or reject ADR-0023 through accountable review;
- resolve or explicitly bound ADR-0013 identity/canonicalization dependency;
- decide how `KFMGeoManifest`, `TileArtifactManifest`, PMIDX, PMSIG, and release manifests compose;
- resolve release-manifest singular/plural responsibility;
- select canonical PMTiles and COG profile ownership without creating parallel schemas or policy homes.

### Wave 2 — close release-grade payload semantics

- version semantic contract and closed release schema together;
- define canonical payload serialization and hash projection;
- define media types, filenames, compatibility aliases, and migration rules;
- add cross-runtime canonicalization vectors;
- retain fixture-first non-release profile for compatibility only when explicitly useful.

### Wave 3 — implement cryptographic trust

- choose and pin an approved DSSE, COSE, or successor implementation;
- define signer identities, trust roots, key custody, rotation, revocation, and offline/transparency proof;
- prohibit repository secrets and silent shape-only fallback;
- add valid, invalid, unauthorized, expired, and revoked signature vectors;
- preserve human review as a separate object and duty.

### Wave 4 — prove real artifact formats

- add production-like PMTiles v3 vectors and reconcile the structural bundle with the canonical manifest profile;
- add real COG vectors covering tiling, overviews, nodata, CRS, compression, and byte-range behavior;
- pin parser/tool versions and record unsupported profiles as finite holds;
- test full-file and optional range-root verification across platforms.

### Wave 5 — bind policy, promotion, release, and serving

- resolve EvidenceRefs/Bundles, source roles, rights, sensitivity, and review records;
- require verified binding in promotion and release assembly;
- enforce immutable artifact refs and alias selection;
- deny candidate, superseded, revoked, withdrawn, or mismatched artifacts;
- test CDN, service-worker, API, MapLibre, offline, and cache bypass paths without granting CI uncontrolled publication credentials.

### Wave 6 — correction and rollback proof

- exercise signer compromise, artifact mismatch, policy revocation, correction, withdrawal, and rollback scenarios;
- update aliases atomically and invalidate/rebuild caches;
- verify public range requests resolve to the selected rollback artifact;
- retain append-only receipts, proofs, catalog, release, correction, and post-rollback verification evidence.

### Required negative vectors

At minimum:

- missing payload or envelope;
- malformed or unapproved envelope/profile;
- payload embeds envelope/signature;
- self-referential or incorrect hash projection;
- invalid real PMTiles or COG format;
- artifact digest or byte-length mismatch;
- range-root/range-metadata mismatch;
- wrong, expired, unauthorized, or revoked signer;
- missing transparency/offline proof;
- unresolved EvidenceBundle or RunReceipt;
- rights/sensitivity/policy denial;
- missing independent review or separation of duties;
- unresolved release manifest or promotion decision;
- candidate, superseded, revoked, or withdrawn artifact at a public alias;
- rollback target missing or mismatched;
- generated authoring receipt stale;
- public URL/client path bypassing the selected binding.

[Back to top](#top)

---

<a id="acceptance-gates"></a>

## Acceptance gates

ADR acceptance and implementation graduation are related but distinct.

### ADR acceptance

- [ ] Architecture, release, geospatial, evidence, security, policy, validation, correction, rollback, and docs reviewers approve.
- [ ] ADR-0013 identity/hash dependency is accepted or explicitly isolated through a versioned profile.
- [ ] `KFMGeoManifest`, `TileArtifactManifest`, PMIDX, PMSIG, payload envelope, reviewer signoff, proof, receipt, and release objects remain non-overlapping.
- [ ] Release-manifest singular/plural responsibility is resolved or explicitly bounded.
- [ ] Hash projection excludes `spec_hash`, envelope, signatures, transparency, and transport-only fields.
- [ ] Algorithms, canonicalization, media types, filenames, compatibility windows, and signer policy are versioned.
- [ ] Public/restricted transparency and metadata-leak posture are resolved.
- [ ] Correction, withdrawal, revocation, supersession, and rollback behavior is specified.
- [ ] No text states or implies current signing, release, or publication.

### Bounded fixture-profile proof

- [x] Closed fixture-first schema exists.
- [x] Deterministic no-network validator exists.
- [x] Synthetic valid/schema-invalid/semantic-invalid fixtures exist.
- [x] Focused tests exercise parser safety, hash projection, spatial, transform, governance, lineage, and byte-binding rules.
- [x] Functional profile steps passed in the latest inspected hosted run.
- [ ] Generated authoring receipt integrity is current and exact-head CI is green.

### Implementation graduation

- [ ] Accepted release-grade payload/envelope contract and schemas agree.
- [ ] Real PMTiles and COG format vectors pass pinned validators.
- [ ] Approved cryptographic verification and trusted-key evaluation pass.
- [ ] Signer authorization, rotation, revocation, and offline/transparency rules enforce.
- [ ] Evidence, rights, sensitivity, policy, and independent review resolve.
- [ ] Promotion and release records bind exact artifacts and signatures.
- [ ] Public serving and clients cannot bypass verification.
- [ ] Candidate, superseded, revoked, withdrawn, or mismatched artifacts are not served.
- [ ] Correction, withdrawal, cache invalidation, and rollback drills pass.
- [ ] Failure paths produce no public write or optimistic fallback.

No gate is satisfied merely because a document, schema, validator, receipt, workflow, pull request, or merge exists.

[Back to top](#top)

---

<a id="consequences"></a>

## Consequences

### Positive

- Integrity reaches the exact bytes public clients fetch rather than stopping at catalog metadata.
- Artifact, manifest, range commitments, signature, proof, receipt, human review, policy, release decision, and publication remain distinguishable.
- Offline and CDN verification become possible under declared profiles.
- Supersession, correction, withdrawal, and rollback can bind exact immutable artifacts.
- One governed envelope/profile family reduces signature-format drift.
- Explicit hash projection removes circular `spec_hash` semantics.
- Existing fixture and structural slices provide testable stepping stones without overstating maturity.

### Costs

- Signer identity, key custody, rotation, revocation, transparency, and incident response add operational burden.
- Sidecars, range commitments, and verification add build, storage, network, client, and cache complexity.
- Producers and consumers must migrate together when schemas/profiles change.
- Real COG and PMTiles conformance vectors require pinned tooling and cross-platform maintenance.
- Serving systems must prevent aliases and caches from bypassing validation.
- Historical unsigned or profile-incompatible artifacts require inventory and disposition.
- Multiple partial profiles create convergence work and risk accidental parallel authority.

### Neutral but important

- A disabled public artifact is safer than an unverifiable release, but it may reduce availability until the trust chain is restored.
- Cryptographic verification improves integrity and provenance; it does not turn a derived carrier into sovereign truth.
- Fixture-first and structural validation are valuable only when their limitations remain visible.

[Back to top](#top)

---

<a id="alternatives-considered"></a>

## Alternatives considered

| Alternative | Disposition |
|---|---|
| Sign only `ReleaseManifest` | Rejected: release scope does not replace per-artifact byte binding |
| Rely only on STAC/DCAT/PROV digests | Rejected: catalog projections do not define signer, envelope, or release policy |
| Sign artifact bytes without a manifest | Rejected: loses structured evidence, spatial, provenance, policy, correction, and rollback linkage |
| Embed signature/envelope in payload | Rejected: creates circular identity and unstable canonicalization |
| Treat PMIDX Merkle root as the entire release proof | Rejected: chunk integrity does not establish range-table authenticity, evidence, rights, review, or release |
| Treat PMSIG shape as cryptographic verification | Rejected: current verifier explicitly says cryptography is unwired |
| Treat fixture payloads as PMTiles/COG conformance | Rejected: synthetic bytes prove only digest/length binding |
| Per-tile/per-range cryptographic envelopes by default | Rejected: excessive cost; use a governed range-root profile when justified |
| Reuse human `release/signatures/` packets | Rejected: reviewer signoff and machine cryptographic binding have different semantics |
| No signing for restricted artifacts | Rejected: restricted does not mean unverifiable; use sensitivity-appropriate trust and transparency |
| Advisory validation only | Rejected: invalid or unavailable required verification must block public release |
| Make current fixture-first schema the release schema unchanged | Rejected: its fixed non-release constants are deliberate and must not be bypassed |

[Back to top](#top)

---

<a id="risk-and-open-question-ledger"></a>

## Risk and open-question ledger

| Item | Status | Required resolution |
|---|---|---|
| ADR acceptance and owner/quorum | `NEEDS VERIFICATION` | Accountable review and matching ADR/index state |
| Repository-wide `spec_hash` grammar | `CONFLICTED` | Accepted ADR-0013 profile and migration |
| Fixture hash profile mistaken for authority | `OPEN RISK` | Explicit profile ID, scope labels, and compatibility tests |
| GeoManifest vs TileArtifactManifest vs PMTiles bundle overlap | `CONFLICTED / OPEN` | Accepted composition and ownership model |
| Generated authoring receipt mismatch | `CONFIRMED DRIFT` | Successor receipt bound to current bytes and exact-head green run |
| Synthetic payloads mistaken for format proof | `OPEN RISK` | Real format vectors and visible non-effects |
| PMSIG shape mistaken for signature trust | `OPEN RISK` | No-crypto badges/reason codes and approved verifier |
| Artifact digest/range algorithms | `PROPOSED` | Accepted profile, implementation, performance, migration evidence |
| Range metadata authentication | `OPEN` | Commit range identity/metadata or narrow claims |
| Envelope and payload media types | `OPEN` | Accepted schema/profile |
| Exact sidecar filenames | `OPEN` | Compatibility and consumer migration decision |
| DSSE/COSE/cosign implementation and versions | `NEEDS VERIFICATION` | Security/tooling review and pinned dependencies |
| Signer identities and trust roots | `UNKNOWN` | Policy, ownership, key custody, rotation, revocation |
| Public vs private transparency | `OPEN` | Sensitivity/privacy policy and offline proof profile |
| Release manifest singular/plural paths | `CONFLICTED` | Accepted responsibility distinction or migration |
| Cryptographic sidecar archival | `OPEN` | Release lane, immutable ref, digest, and retention policy |
| PMTiles delta semantics | `OPEN` | Base identity, tile-ID behavior, invalidation, rollback |
| Multi-collection artifacts | `OPEN` | One-artifact/one-collection rule or accepted collection profile |
| COG format/profile and sublane | `HOLD` | Real COG validator, fixtures, published path, overview/tiling checks |
| CDN/public alias bypass | `UNKNOWN` | Serving config, integration tests, monitoring, incident response |
| Existing unsigned artifacts | `UNKNOWN` | Inventory, hold/quarantine, migration, withdrawal, or grandfathering decision |
| Compromised signer | `OPEN` | Revocation, withdrawal, alias rollback, correction, cache purge |
| Implementation ownership and duty separation | `NEEDS VERIFICATION` | Named steward assignments and enforcement |

Fail-safe posture: unresolved signer, evidence, rights, sensitivity, review, release, or binding state blocks public release or narrows the response. Optimistic prose cannot repair an invalid trust chain.

[Back to top](#top)

---

<a id="rollback-and-supersession"></a>

## Rollback and supersession

### Documentation rollback

Before merge, close the draft pull request and abandon its branch.

After merge, restore prior ADR blob:

```text
d57353d059383860a43fc129c1f39f3173f69119
```

or revert the documentation commit created for v1.3. Reverting documentation does not revert any independent contract, schema, workflow, artifact, signature, or release.

### Artifact rollback target

A future conforming rollback must:

1. identify the unsafe artifact, payload, envelope, and release record;
2. record accountable denial, withdrawal, revocation, correction, or rollback decision;
3. preserve prior artifact, binding, receipts, proofs, catalog, and release records under policy;
4. validate the rollback target’s real format, byte binding, signature, policy, review, and release gates;
5. update public aliases atomically;
6. invalidate or rebuild CDN, service-worker, search, catalog, tile, API, and browser caches;
7. verify public range requests resolve to the selected immutable artifact;
8. issue correction/withdrawal notices when users may have consumed unsafe bytes;
9. record append-only execution and post-rollback verification receipts.

Rollback is not “delete the bad file.” Deletion can destroy the evidence needed to explain and correct a release.

### Supersession of this ADR

An accepted successor must retain this record, mark it `superseded`, link both ADRs reciprocally, update the canonical index in the same reviewed change, and migrate contracts, schemas, fixtures, validators, policies, producers, consumers, releases, and verification support through an auditable plan.

[Back to top](#top)

---

<a id="verification-checklist"></a>

## Verification checklist

### Current v1.3 revision

- [x] Current main SHA and target prior blob recorded.
- [x] ADR ID, filename, H1, and canonical index row verified.
- [x] Source/effective status preserved as `proposed`.
- [x] Accepted ADR-0029 and adopted Directory Rules bytes inspected.
- [x] Current KFMGeoManifest contract, closed schema, fixtures, validator, tests, workflow, and authoring receipt inspected.
- [x] Latest dedicated workflow jobs and logs inspected.
- [x] PMTiles attestation standard, finite cryptographic hold, and shape-only verifier inspected.
- [x] COG standard and current implementation boundary inspected.
- [x] Human reviewer signoff separated from artifact cryptography.
- [x] Fixture-first, structural, cryptographic, policy, release, and publication states kept separate.
- [x] Current generated-receipt drift disclosed rather than described as green CI.
- [x] No implementation, signing, release, deployment, or publication claim introduced.
- [ ] Human semantic/security review completed.
- [ ] ADR accepted.

### Current bounded implementation

- [x] Closed fixture-first metadata schema exists.
- [x] Deterministic no-network validator exists.
- [x] Synthetic fixture matrix and focused tests exist.
- [x] Functional manifest checks passed in the latest inspected workflow run.
- [x] PMTiles structural split-bundle checks exist.
- [ ] Dedicated geo-manifest authoring receipt matches current workflow bytes.
- [ ] Dedicated workflow is green at current exact head.
- [ ] Real COG and PMTiles release-format profiles are validated under one governed model.
- [ ] Cryptographic verification and trusted-key evaluation are implemented.
- [ ] Policy, review, promotion, release, serving, correction, and rollback integration is proved.

### Future signed-release implementation

- [ ] Accepted payload and envelope profiles are separate and versioned.
- [ ] Canonicalization/hash projection and algorithm-tagged digests are accepted.
- [ ] Valid/invalid cryptographic and cross-runtime vectors pass.
- [ ] Signer authorization, rotation, revocation, and transparency/offline rules enforce.
- [ ] Evidence, rights, sensitivity, policy, and independent review resolve.
- [ ] Promotion and release records bind exact artifacts.
- [ ] Public aliases and clients cannot bypass verification.
- [ ] Candidate, superseded, revoked, withdrawn, or mismatched artifacts are not served.
- [ ] Correction, withdrawal, cache invalidation, and rollback drills pass.

[Back to top](#top)

---

<a id="references"></a>

## References

### Decision and directory authority

- [ADR operating contract](./README.md)
- [Canonical ADR index](./INDEX.md)
- [ADR-0001 — Schema Home](./ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md)
- [ADR-0011 — Artifact-family separation](./ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [ADR-0013 — Identity grammar](./ADR-0013-spec_hash-and-run_id-identity-grammar.md)
- [ADR-0015 — Published alias and rollback](./ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md)
- [ADR-0018 — Promotion sequence](./ADR-0018-promotion-gate-sequence.md)
- [ADR-0022 — Catalog matrix](./ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md)
- [ADR-0024 — Release duty separation](./ADR-0024-steward-separation-of-duties-for-release.md)
- [ADR-0025 — Public-client boundary](./ADR-0025-public-client-never-reads-canonical-internal-stores.md)
- [Accepted ADR-0029 — Directory Rules v2](./ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules](../doctrine/directory-rules.md)

### Geo-manifest executable slice

- [`KFMGeoManifest` semantic contract](../../contracts/evidence/kfm_geo_manifest.md)
- [`KFMGeoManifest` closed fixture schema](../../schemas/contracts/v1/evidence/kfm_geo_manifest.schema.json)
- [Fixture profile README](../../fixtures/evidence/kfm_geo_manifest/README.md)
- [Manifest validator](../../tools/validators/evidence/validate_kfm_geo_manifest.py)
- [Focused tests](../../tests/validators/test_validate_kfm_geo_manifest.py)
- [Dedicated read-only workflow](../../.github/workflows/kfm-geo-manifest-validation.yml)
- [Historical generated authoring receipt](../../data/receipts/generated/genrec-kfm-geo-manifest-validation-20260804.json)

### PMTiles, COG, release, and serving boundaries

- [PMTiles Attestation Standard](../standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md)
- [PMTiles shape-only signature verifier](../../tools/attest/verify_cose.py)
- [PMTiles attestation workflow](../../.github/workflows/pmtiles-attestation.yml)
- [COG Standard](../standards/COG.md)
- [Published PMTiles lane](../../data/published/pmtiles/README.md)
- [Published layers/COG-capable lane](../../data/published/layers/README.md)
- [Singular release manifest lane](../../release/manifest/README.md)
- [Plural release manifests lane](../../release/manifests/README.md)
- [Release signatures — human signoff packets](../../release/signatures/README.md)
- [Attestation tooling lane](../../tools/attest/README.md)
- [Promotion readiness workflow](../../.github/workflows/promotion-gate.yml)

### Planning lineage

The supplied KFM build-out prompt requires the smallest coherent, evidence-grounded, reversible feature-branch change and explicitly separates implementation from merge, release, deployment, promotion, and publication. The broader KFM corpus consistently treats PMTiles and COGs as downstream carriers that require integrity, provenance, policy, review, correction, and rollback bindings. Planning material supports this decision direction; current repository evidence controls implementation maturity.

[Back to top](#top)

---

<a id="revision-history"></a>

## Revision history

| Version | Date | Summary |
|---|---|---|
| v1 | 2026-05-09 | Initial proposed ADR for signed PMTiles/COG geo-manifest release gating. |
| v1.1 | 2026-05-15 | Added proposed/unknown posture, payload/envelope layering, field map, gate mapping, negative fixtures, rollback discipline, and acceptance checklist. |
| v1.2 | 2026-07-24 | Re-grounded the ADR in repository evidence; confirmed contract and schema stub; separated reviewer signoff from artifact cryptography; surfaced identity and release-manifest conflicts; corrected self-referential hash projection; bounded implementation as `HOLD`. |
| v1.3 | 2026-08-14 | Reconciled the merged fixture-first KFMGeoManifest schema/validator/test slice, separate PMTiles structural attestation lane, explicit cryptographic hold, synthetic COG boundary, latest hosted functional passes plus generated-receipt failure, accepted ADR-0029 placement authority, profile-convergence plan, updated maturity/risk/acceptance/rollback evidence, and unchanged `proposed` decision status. |

---

**Last updated:** 2026-08-14 · **Decision status:** `proposed` · **Current maturity:** fixture-first metadata + PMTiles structural proof; cryptography/release held · **Publication:** none · **Path:** `docs/adr/ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md` · [Back to top](#top)
