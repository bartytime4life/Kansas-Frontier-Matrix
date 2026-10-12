<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/standard/release-manifest-conformance
title: ReleaseManifest — Repository Profile and Release Boundary
type: "standard; release-profile-guidance; interoperability-boundary"
version: v2.0
status: "draft; repository-grounded; dual-profile; strict-fixture-only; operational-release-hold; non-authoritative"
owners:
  - "@bartytime4life — verified CODEOWNERS review route"
  - "NEEDS VERIFICATION — accountable release-profile, policy, security, operations, and independent-review stewards"
created: 2026-05-24
updated: 2026-08-19
policy_label: "repository-facing; release-manifest; standards-guidance; evidence-bound; fail-closed; non-release; non-publication"
owning_root: docs/
current_path: docs/standards/RELEASE_MANIFEST.md
responsibility: >
  Describe the current repository ReleaseManifest profile, its bounded validation
  and release-readiness surfaces, and its relationships to external standards
  without redefining semantic, machine-shape, policy, review, release, correction,
  rollback, runtime, or publication authority.
truth_posture: >
  CONFIRMED same-path placement, draft contract, dual-profile schema, closed
  PROPOSED_INACTIVE fixture profile, deterministic 21-case no-network validation,
  read-only workflows, bounded publication-denial dry run, release-policy scaffolds,
  and operational release hold / PROPOSED external-standard bindings, production
  profile, signature and attestation verification, reference resolution, policy and
  review integration, release persistence, correction propagation, rollback
  execution, and public consumers / UNKNOWN first governed production release,
  deployed release registry, active public alias, and external interoperability.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: cc52dba82d3b1c62e0a0d97fc49a6d205cf1c5ba
  target_prior_blob: 67df3a29596401d30abc118f6d442e60274a6fb2
  standards_readme_blob: a8cbe5d183448d5f0de37f8a4eacd6fcaca0d71b
  contract_blob: ce7dc89ff447d76d974afdd802b85a38538d8f48
  schema_blob: c76cd9bdddb34cf33c8eb62801269553726c5923
  validator_blob: 00307dc0d5e2c3867a229076e3702f8111455425
  fixture_readme_blob: 6b2b0be8f9c72e2fb31c74c0845a06e8ef5123f2
  test_blob: eff34352614a0c03c7ff8b326f83fa9699525e98
  workflow_blob: 91d9a995328f8d162121341ed265fa87781be4e8
  release_dry_run_blob: 5fed3a16aa0915b9233861048fc6a1e676e0ed8f
  release_dry_run_workflow_blob: 8f76d1011b80769952a0a6561ed7e5cd963bf8c9
  canonicalization_blob: dc1a945417e0abf6761ccb4980f03433d8e2ba64
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
external_currentness:
  access_date: 2026-08-19
  rfc_8785: "RFC 8785, JSON Canonicalization Scheme"
  json_schema: "JSON Schema Draft 2020-12"
related:
  - ./README.md
  - ./EVIDENCE_BUNDLE.md
  - ./CANONICALIZATION.md
  - ./SIGNING.md
  - ./PROV.md
  - ./PROVENANCE.md
  - ../doctrine/directory-rules.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../architecture/contract-schema-policy-split.md
  - ../../contracts/release/release_manifest.md
  - ../../schemas/contracts/v1/release/release_manifest.schema.json
  - ../../fixtures/release/release_manifest/README.md
  - ../../tools/validators/release/validate_release_manifest.py
  - ../../tests/validators/test_validate_release_manifest.py
  - ../../.github/workflows/release-manifest.yml
  - ../../tools/release/release_dry_run.py
  - ../../.github/workflows/release-dry-run.yml
  - ../../policy/release/README.md
  - ../../release/README.md
  - ../../release/manifests/README.md
tags: [kfm, standards, release-manifest, release, validation, evidence, policy, review, signing, correction, rollback, cite-or-abstain]
notes:
  - "v2.0 replaces the May 2026 proposal-era conformance dossier with a current-repository profile and explicit release/publication boundary."
  - "The strict profile validates deterministic synthetic candidates only; the permissive legacy branch remains visible as compatibility debt."
  - "Current executable identity uses RFC 8785 JCS plus SHA-256 and the wire grammar sha256:<64-lowercase-hex>; jcs:sha256:<hex> is not current behavior."
  - "No Merkle tree, BLAKE3 path, JSON-LD/PROV requirement, signature verification, SLSA/DSSE enforcement, OCI/IPFS transport, live policy evaluation, release record, deployment, or publication is created by this page."
  - "Legacy title, numbered-section, quick-jump, and appendix anchors are retained."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="releasemanifest--external-standards-conformance-dossier"></a>

# ReleaseManifest — Repository Profile and Release Boundary

> **One-line rule.** A current KFM `ReleaseManifest` is a proposed release-binding contract with a permissive compatibility branch and a closed, deterministic fixture-only candidate profile; neither branch creates evidence, policy, review, release, publication, or public-use authority.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status-at-a-glance)
[![Schema: dual profile](https://img.shields.io/badge/schema-dual%20profile-1f6feb?style=flat-square)](#5-identity-and-canonicalization)
[![Strict profile: fixture only](https://img.shields.io/badge/strict%20profile-fixture%20only-8250df?style=flat-square)](#8-inclusion-semantics--what-the-manifest-binds)
[![Policy: unbound scaffolds](https://img.shields.io/badge/policy-unbound%20scaffolds-d97706?style=flat-square)](#10-lifecycle-integration--promotion-rollback-correction-withdrawal)
[![Operational release: held](https://img.shields.io/badge/operational%20release-held-b42318?style=flat-square)](#12-external-verification-flow)
[![Publication: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#3-authority-and-standing)

> [!IMPORTANT]
> **Human-readable standards guidance only.** [`contracts/release/release_manifest.md`](../../contracts/release/release_manifest.md) owns semantic meaning; [`schemas/contracts/v1/release/release_manifest.schema.json`](../../schemas/contracts/v1/release/release_manifest.schema.json) owns machine shape; `policy/`, `release/`, governed evidence/proof/receipt families, validators, workflows, and public delivery each retain their own authority.

> [!CAUTION]
> **The May 2026 dossier overclaimed current conformance.** The repository does not establish a production ReleaseManifest profile, Merkle construction, BLAKE3 path, JSON-LD/PROV requirement, DSSE/SLSA/Sigstore verification, OCI/ORAS/IPFS distribution, live policy evaluator, authenticated review chain, persisted release, cache invalidation, deployment, or external interoperability certificate.

> [!WARNING]
> **A valid candidate is not a release.** Schema validity, deterministic identity, a validator `PASS`, a workflow result, a signature-shaped reference, a pull request, a merge, or a GitHub release cannot substitute for source authority, EvidenceBundle support, rights, sensitivity handling, policy, review, correction, rollback, release approval, and governed publication.

## Status at a glance

Evidence snapshot: `main@cc52dba82d3b1c62e0a0d97fc49a6d205cf1c5ba`; prior document blob `67df3a29596401d30abc118f6d442e60274a6fb2`.

| Surface | Current repository evidence | Safe conclusion |
|---|---|---|
| Placement | Accepted Directory Rules v2 and the standards-lane README classify this path as human-readable release-manifest profile guidance. | **CONFIRMED `PLACE` at the existing path**; no structural migration. |
| Semantic contract | The flat contract is draft v0.3, `PROPOSED`, schema-paired, and release-governance-oriented. | Meaning is present but not an accepted production release profile. |
| Machine shape | Draft 2020-12 schema with a permissive legacy branch and a closed strict branch. | **Dual-profile compatibility surface**, not one uniform maturity level. |
| Strict profile | `RELEASE_MANIFEST_FIXTURE_V1`, `PROPOSED_INACTIVE`, `FIXTURE_ONLY`, lifecycle `CANDIDATE`. | Deterministic candidate validation only. |
| Identity | RFC 8785 JCS plus SHA-256 over the strict candidate with stored `id` and `spec_hash` omitted; output uses `sha256:<hex>`. | **CONFIRMED bounded implementation**; no `jcs:` wire prefix and no release-signature proof. |
| Fixtures and tests | Four valid cases, two schema-negative cases, and fifteen semantic-negative cases; deterministic no-network tests. | **CONFIRMED 21-case polarity**; all data and identities are synthetic. |
| Validator | Checks bounded input, schema, identity, ordering, reference roles, public-intended prerequisites, time, lineage, and false governance flags. | `PASS` proves only declared candidate relationships. |
| Dedicated workflow | Read-only workflow invokes focused tests and fixture validation. | CI orchestration exists; the workflow does not assemble or write a release. |
| Publication-denial dry run | Five synthetic negative mutations remain blocked by the bounded promotion gate. | Denial behavior is exercised; no real candidate, decision, manifest, or publication is created. |
| Release policy | Release-policy lane contains unbound scaffolds; separate policy profiles remain proposed/inactive. | No live policy allow/deny decision can be inferred. |
| Release records | `release/` is the canonical append-only decision plane, while candidate assembly and operational execution remain held. | No first governed production ReleaseManifest was established here. |
| Public effect | No deployed registry, active alias, authenticated release operation, or public consumer was established by the inspected evidence. | **UNKNOWN / NOT ESTABLISHED**; publication effect is none. |

### State separation

```text
path present
  != semantic contract accepted
  != schema valid
  != strict candidate PASS
  != references resolved
  != artifact bytes verified
  != signatures verified
  != policy evaluated
  != review authenticated
  != promotion authorized
  != release authorized
  != publication authorized
  != public use allowed
```

The strict profile encodes the last nine authority-bearing states as `false` so fixture validation cannot self-promote.

[Back to top](#top)

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Scope guardrail — what this doc is NOT](#2-scope-guardrail--what-this-doc-is-not)
- [3. Authority and standing](#3-authority-and-standing)
- [4. External-standards conformance matrix](#4-external-standards-conformance-matrix)
- [5. Identity and canonicalization](#5-identity-and-canonicalization)
- [6. Content addressing and Merkle integrity](#6-content-addressing-and-merkle-integrity)
- [7. Signing and attestation](#7-signing-and-attestation)
- [8. Inclusion semantics — what the manifest binds](#8-inclusion-semantics--what-the-manifest-binds)
- [9. Catalog interoperability — STAC, DCAT, ISO 19115](#9-catalog-interoperability--stac-dcat-iso-19115)
- [10. Lifecycle integration — promotion, rollback, correction, withdrawal](#10-lifecycle-integration--promotion-rollback-correction-withdrawal)
- [11. ReleaseManifest vs delta manifest](#11-releasemanifest-vs-delta-manifest)
- [12. External verification flow](#12-external-verification-flow)
- [13. Tensions and known limits](#13-tensions-and-known-limits)
- [14. Open questions](#14-open-questions)
- [15. Related docs](#15-related-docs)
- [Appendix A — Worked external verification](#appendix-a--worked-external-verification)
- [Appendix B — Placement rationale](#appendix-b--placement-rationale)

---

## 1. Purpose

This page has three responsibilities:

1. describe the **current repository profile** an implementer or reviewer can inspect;
2. distinguish implemented bindings from **proposed external-standard relationships**; and
3. state the evidence required before KFM may claim production conformance, release, publication, or external interoperability.

The current repository contains a useful but intentionally bounded implementation: semantic contract text, a dual-profile JSON Schema, a deterministic strict-candidate validator, 21 synthetic fixture cases, focused no-network tests, a read-only workflow, and a separate publication-denial dry run. Those surfaces improve reviewability without creating release authority.

The current page is not the canonical ReleaseManifest object definition. It follows the contract, schema, implementation, and release decision plane; it cannot override them.

[Back to quick jump](#quick-jump)

---

<a id="2-scope-guardrail"></a>

## 2. Scope guardrail — what this doc is NOT

### In scope

- current contract, schema, fixture, validator, test, workflow, policy, and release-root posture;
- the exact legacy-versus-strict compatibility boundary;
- identity, artifacts, references, time, lineage, rights, sensitivity, review, attestation, correction, and rollback relationships;
- bounded external-standard relationships and non-conformance statements;
- finite validation outcomes and what they do not prove;
- graduation, migration, correction, rollback, and consumer evidence.

### Out of scope

- changing ReleaseManifest semantic meaning or machine shape;
- accepting a production profile or deprecating legacy instances;
- activating policy, signing, external transport, registry, runtime, or public serving;
- resolving real EvidenceRefs, SourceDescriptors, policy decisions, review records, receipts, proofs, or attestations;
- assembling a release candidate, issuing a decision, changing an alias, purging a cache, deploying, or publishing;
- choosing singular/plural release-record lanes or domain-schema migration targets;
- accepting an ADR or changing repository settings.

### Authority map

| Question | Owning surface | This page may do |
|---|---|---|
| What does `ReleaseManifest` mean? | [`contracts/release/release_manifest.md`](../../contracts/release/release_manifest.md) | Report the current draft meaning and limits. |
| What machine representation is valid? | [`schemas/contracts/v1/release/release_manifest.schema.json`](../../schemas/contracts/v1/release/release_manifest.schema.json) | Summarize exact profile constraints. |
| What candidate checks exist? | Validator, fixtures, tests, and workflow | Name the checked boundary and finite outcomes. |
| What is admissible? | Accepted policy source, evaluator, and governed decision records | Expose the current policy hold; never infer allow. |
| Who reviewed or approved? | Authenticated review and release authority | State what remains unverified. |
| Which release/correction/rollback applies? | [`release/`](../../release/README.md) and its accepted record lanes | Link and explain; never issue a decision. |
| Where published payloads live | Governed `data/published/` and approved delivery | Deny direct publication by path or prose. |
| Which external standards apply | Upstream specifications plus an accepted KFM profile | Record relationships; do not manufacture conformance. |

[Back to quick jump](#quick-jump)

---

## 3. Authority and standing

| Axis | Current result | Boundary |
|---|---|---|
| Document placement | `docs/standards/RELEASE_MANIFEST.md` | Human-readable profile and interoperability guidance only. |
| Review route | `@bartytime4life` through repository-default CODEOWNERS | GitHub routing, not independent release approval. |
| Semantic owner | `contracts/release/release_manifest.md` | Draft meaning; no production adoption by this page. |
| Shape owner | `schemas/contracts/v1/release/release_manifest.schema.json` | Dual-profile Draft 2020-12 shape. |
| Executable proof | Fixture validator, tests, and read-only workflows | Synthetic candidate proof only. |
| Policy owner | `policy/release/` plus accepted evaluator/decision contracts | Current lane is scaffolded and unbound. |
| Release owner | `release/` | Append-only release, correction, withdrawal, rollback, and signature decision records. |
| Payload owner | Governed data/artifact stores | Manifest references payloads; it does not store them. |
| Public authority | Governed release and delivery | No current public effect from this document or fixture profile. |

The same-path update is editorial and semantic reconciliation within the accepted standards lane. It creates no new root, parallel ReleaseManifest definition, generated mirror, compatibility writer, or release record.

[Back to quick jump](#quick-jump)

---

## 4. External-standards conformance matrix

The legacy heading is retained. The table now records **relationship and evidence**, not unsupported certification.

| External standard or practice | Current repository binding | Current evidence | Safe posture |
|---|---|---|---|
| RFC 8785 JCS | Strict-candidate identity subject is canonicalized by the shared hashing package. | Validator recomputes identity; tests prove deterministic replay and semantic sensitivity. | **Implemented for the bounded strict profile.** |
| SHA-256 | Strict candidate `spec_hash`, `id`, and artifact digests use `sha256:<64-lowercase-hex>`. | Schema patterns and shared hashing implementation. | **Implemented grammar and computation; not signature or release proof.** |
| JSON Schema Draft 2020-12 | Paired schema declares the 2020-12 dialect. | Schema meta-validation is exercised in tests. | **Implemented machine-shape dialect.** |
| Merkle trees | No `merkle_root`, tree variant, leaf rule, proof object, or validator exists in the strict profile. | Absent from paired schema and validator. | **Not implemented; design lineage only.** |
| BLAKE3 | No allowed digest grammar or implementation in this profile. | Artifact digests are SHA-256 only. | **Not implemented.** |
| JSON-LD / PROV-O / PAV | No JSON-LD context or PROV field is part of the strict profile. | Current profile carries opaque refs and a RunReceipt ref. | **Relationship proposed; no ReleaseManifest conformance claim.** |
| DSSE / Sigstore / Cosign / Rekor | Strict profile carries opaque `attestation_refs`; `signatures_verified` is fixed to `false`. | No release-manifest signature verifier or trusted-identity policy in this slice. | **Not operationally integrated.** |
| SLSA / in-toto | No predicate shape, subject binding, builder policy, or verification path in this profile. | Only opaque attestation references are available. | **Proposed relationship; no target level established here.** |
| SPDX / CycloneDX | Release scope uses coarse rights states; no SPDX expression or SBOM field is defined. | Schema enums are `APPROVED`, `RESTRICTED`, or `UNKNOWN`. | **No SPDX/SBOM conformance in the strict profile.** |
| STAC / DCAT / ISO 19115 | Strict profile exposes opaque `catalog_refs`; no host-record mapping or validator is bound. | Catalog refs remain unresolved and unauthenticated. | **Interoperability relationship only.** |
| OpenLineage | RunReceipt may be referenced, but no OpenLineage record is required or verified. | Separate telemetry profiles remain bounded and inactive. | **Not a ReleaseManifest conformance requirement.** |
| OCI / ORAS / IPFS | No transport field, registry client, media-type profile, or publish workflow exists in this slice. | Strict profile validates local JSON candidates only. | **Not implemented.** |
| HTTP caching / CDN invalidation | No cache operation or result field exists in the strict profile. | Correction and rollback refs are declarative only. | **Runtime/release follow-up, not profile conformance.** |

> [!IMPORTANT]
> A standards relationship becomes a conformance claim only when a named versioned KFM profile, machine shape, implementation, positive and negative fixtures, producer, consumer, and reviewed release scope establish it. A standards page or opaque reference is insufficient.

[Back to quick jump](#quick-jump)

---

## 5. Identity and canonicalization

### 5.1 Legacy branch

The compatibility branch requires only `id`, permits optional `spec_hash` and `version`, and allows additional properties. It preserves old scaffold compatibility but does not establish deterministic identity, completeness, signing readiness, or release fitness.

### 5.2 Strict fixture branch

For `RELEASE_MANIFEST_FIXTURE_V1`:

```text
identity_subject = complete candidate minus stored id and spec_hash
spec_hash        = SHA-256(RFC 8785 JCS(identity_subject))
id               = "release-manifest:" + first 24 digest hex characters
```

Current wire grammar:

```text
sha256:<64 lowercase hexadecimal characters>
```

The validator rejects mismatched stored identity and tests prove that changing meaning-bearing candidate content changes the digest.

> [!CAUTION]
> The current implementation does **not** emit `jcs:sha256:<hex>`. [`CANONICALIZATION.md`](./CANONICALIZATION.md) records `jcs:sha256:` as a proposed migration target rather than current wire behavior.

### 5.3 What identity does not prove

A matching digest does not resolve references, verify artifact bytes or signatures, evaluate policy, authenticate review, authorize promotion, record release state, publish a carrier, or prove factual correctness. Identity is one prerequisite in a larger governed chain.

[Back to quick jump](#quick-jump)

---

## 6. Content addressing and Merkle integrity

The current strict profile binds each artifact through:

- an opaque stable `artifact_ref`;
- an exact SHA-256 digest;
- a media type;
- a bounded role;
- deterministic ordering and uniqueness; and
- `artifact_count` parity.

That is useful artifact-set integrity metadata. It is **not** a Merkle tree or a proof of fetched bytes.

### Current non-effects

The profile does not define:

- a manifest-byte digest distinct from `spec_hash`;
- a Merkle root, leaf encoding, node encoding, sort key, odd-node rule, or partial proof;
- BLAKE3 or algorithm negotiation;
- content fetching, byte recomputation, registry resolution, or transport equivalence;
- immutable storage or public distribution.

### Graduation requirements

A future Merkle or multi-algorithm profile must define the exact hash domain, byte encoding, algorithm/version, ordering, duplicate handling, empty-set behavior, proof format, resource limits, compatibility migration, correction semantics, consumers, and deterministic cross-implementation tests. It must not be introduced by prose alone.

[Back to quick jump](#quick-jump)

---

## 7. Signing and attestation

The strict profile carries `attestation_refs`, but it does not define attestation objects or verify them. Its governance object requires:

```text
signatures_verified = false
```

The current validator never dereferences an attestation, checks a DSSE envelope, verifies a cryptographic signature, authenticates an OIDC identity, queries a transparency log, evaluates a builder policy, or binds an SBOM/SLSA predicate to artifact bytes.

### Required future closure

Production signing requires at least:

1. an accepted signed-subject and canonical-byte definition;
2. an accepted envelope and media type;
3. signer identity and key/trust-root policy;
4. offline, unavailable-service, revocation, rotation, and compromise behavior;
5. deterministic positive and negative fixtures;
6. cryptographic verification code and bounded diagnostics;
7. authenticated reviewer and separation-of-duties checks;
8. correction, withdrawal, rollback, and historical verification behavior; and
9. release consumers that reject unverifiable signatures without treating signatures as truth.

[`SIGNING.md`](./SIGNING.md) remains useful design lineage, but its draft normative language is not evidence that the ReleaseManifest path currently implements DSSE, Sigstore, SLSA, in-toto, or Rekor.

[Back to quick jump](#quick-jump)

---

## 8. Inclusion semantics — what the manifest binds

The contract owns semantic meaning. The table below summarizes the current strict candidate shape without expanding it.

| Field family | Current strict-profile behavior | Authority limit |
|---|---|---|
| Profile identity | `ReleaseManifest`, schema `1.0.0`, `PROPOSED_INACTIVE`, `FIXTURE_ONLY`. | Declares candidate maturity only. |
| Release identity | Content-derived candidate `id`, `spec_hash`, `release_id`, version, and title. | Not a persisted release record. |
| Lifecycle | `lifecycle_state: CANDIDATE`; release state `CANDIDATE`, `HELD`, or `DEGRADED`. | No `RELEASED` state exists in this fixture profile. |
| Artifacts | Nonempty sorted unique refs with SHA-256 digest, media type, and role. | Payload bytes are not embedded or fetched. |
| Source/evidence | SourceDescriptor and EvidenceBundle refs; evidence refs require matching `EVIDENCE_BUNDLE` artifact entries. | References remain unresolved and unauthenticated. |
| Decisions/review | Policy, promotion, and review refs. Public-intended candidates require all three families. | Presence does not prove validity, approval, or authority. |
| Catalog/proof/receipt/attestation | Separate arrays preserve object-family distinctions. | No referenced object is validated by this profile. |
| Release scope | Audience, rights, sensitivity, generalization, and transform receipts. | Declared posture only; policy remains separate. |
| Time | Assembly time and nullable effective interval. | Does not encode every observation, review, release, correction, or withdrawal time. |
| Lineage | Previous manifest, correction, withdrawal, and rollback refs. | No transition or rollback is executed. |
| Provenance | RunReceipt ref and fixed validator implementation ref. | No process, source, or artifact is authenticated. |
| Governance | Nine authority-bearing flags fixed to `false`. | Prevents self-authorization. |

### Fail-closed semantic checks

The validator rejects or flags:

- noncanonical reference or artifact ordering;
- duplicate or cross-role-collapsed references;
- floating `latest` references;
- artifact-count and EvidenceBundle-artifact mismatch;
- incoherent effective time;
- correction without a predecessor;
- public audience without approved rights, acceptable sensitivity, evidence, policy, promotion, and review refs;
- required transformation without generalization and transform receipts; and
- any governance flag that is not `false`.

[Back to quick jump](#quick-jump)

---

## 9. Catalog interoperability — STAC, DCAT, ISO 19115

The strict profile exposes `catalog_refs` as sorted, unique, opaque references. It does not identify a catalog vocabulary, validate a STAC/DCAT/ISO record, compare extents or time, enforce source role, or prove catalog/release closure.

A future catalog binding must keep these states separate:

```text
ReleaseManifest candidate shape
  != catalog record valid
  != catalog projection agrees
  != source/evidence closed
  != release approved
  != public distribution active
```

Any STAC, DCAT, ISO 19115, PROV, or domain-catalog crosswalk must pin the host profile and version, mapping, identifiers, cardinality, fields dropped or transformed, rights/sensitivity representation, correction propagation, reverse-reconstruction limits, and producer/consumer tests.

Domain-specific `release_manifest.schema.json` scaffolds also exist in several domain lanes. Their permissive `id`-only shapes are not automatically aliases or specializations of the shared strict profile. Reconciliation requires explicit family mapping and migration evidence.

[Back to quick jump](#quick-jump)

---

## 10. Lifecycle integration — promotion, rollback, correction, withdrawal

The strict profile is deliberately pre-release:

```text
profile_status  = PROPOSED_INACTIVE
execution_mode  = FIXTURE_ONLY
lifecycle_state = CANDIDATE
release_state   = CANDIDATE | HELD | DEGRADED
```

It can describe intended lineage references but cannot create a transition.

### Current bounded release evidence

| Surface | What it proves | What it does not prove |
|---|---|---|
| ReleaseManifest validator | Candidate shape, identity, and selected semantic coherence. | Reference resolution, live policy, approval, persistence, or publication. |
| Release-manifest workflow | Focused deterministic tests at one revision. | Required-check coupling or operational release. |
| Publication-denial dry run | Five unsafe synthetic promotion packets remain blocked. | Successful candidate assembly or release. |
| Promotion-gate fixtures | Bounded A–G readiness semantics over synthetic input. | Authenticated live actors, EvidenceBundles, policy, or signatures. |
| Rollback-card readiness checks | Selected synthetic rollback presence and consistency. | Rollback execution, alias restoration, cache invalidation, or recovery. |
| `release/` documentation | Canonical decision-plane boundaries and current holds. | Existence of a governed production release record. |

### Required production chain

A production path must keep separate, digest-bound records for candidate assembly, evidence/proof, policy evaluation, review, promotion decision, manifest, signatures/attestations, release decision, published carrier, correction/withdrawal, rollback, propagation/invalidation, and verification receipts. A failure at one layer must not be hidden by success at another.

[Back to quick jump](#quick-jump)

---

## 11. ReleaseManifest vs delta manifest

The current shared strict profile has no `delta_manifest` field and establishes no canonical relationship to product-specific delta manifests.

A safe future distinction is:

| Object | Candidate responsibility | Required boundary |
|---|---|---|
| ReleaseManifest | Bind one governed release scope to an artifact set and release-support references. | Release-governance object; not a payload or build delta. |
| Delta manifest | Describe changes between product/artifact versions for build, synchronization, or partial-transfer purposes. | Product/build artifact; not release approval. |

A future binding must define stable IDs, digest domains, direction, version comparison, full-versus-delta reconstruction, missing-base behavior, correction and rollback, consumer fallback, and whether a ReleaseManifest references a delta as an artifact. Until then, consumers must not infer release authority from a delta-shaped file or a floating `latest` alias.

[Back to quick jump](#quick-jump)

---

## 12. External verification flow

### 12.1 Current bounded verification

The current repository can verify only a local candidate or fixture profile:

1. deny symlinks, missing files, oversized input, malformed UTF-8/JSON, duplicate keys, and nonfinite numbers;
2. validate against the dual-profile Draft 2020-12 schema;
3. for the strict profile, recompute `spec_hash` and candidate `id`;
4. check ordering, uniqueness, artifact count, role separation, evidence-artifact binding, time, lineage, public-intended prerequisites, transformation support, and false governance flags;
5. emit deterministic `PASS`, `FAIL`, or `ERROR` with stable codes and JSON-pointer paths;
6. perform no network request, reference lookup, policy evaluation, signature verification, release write, or publication.

Verified repository commands:

```bash
python -m unittest tests.validators.test_validate_release_manifest -v
python tools/validators/release/validate_release_manifest.py --fixtures
make release-dry-run
```

A strict-profile `PASS` means the supplied synthetic candidate satisfies the bounded schema and semantic checks. It does not establish a release.

### 12.2 Future end-to-end verification

A production verifier still needs to authenticate the manifest profile and bytes, resolve every required reference, recompute artifact digests, evaluate accepted policy, authenticate review and promotion authority, verify signatures and attestations, confirm release persistence and public carrier parity, walk correction/withdrawal/rollback lineage, and verify propagation or invalidation receipts.

> [!NOTE]
> The dedicated `release-manifest` workflow currently filters contract, schema, fixture, validator, test, hashing, and source-map changes but does not list this standards page. This docs-only change therefore relies on general documentation and aggregate workflows unless that path filter is separately reviewed and expanded.

[Back to quick jump](#quick-jump)

---

## 13. Tensions and known limits

| Tension or limit | Current evidence | Bounded posture |
|---|---|---|
| Permissive legacy branch vs closed strict branch | Both are accepted by one `oneOf` schema. | Preserve compatibility; never treat an id-only object as release-complete. |
| Strict fixture profile vs production profile | Strict profile is `PROPOSED_INACTIVE` and `FIXTURE_ONLY`. | Production adoption remains **HOLD**. |
| Shared release schema vs domain stubs | Several domain schemas remain permissive proposed scaffolds. | Relationship and migration are unresolved. |
| Flat contract vs object-folder pointer | Flat Markdown is canonical; child README is compatibility/navigation only and contains stale maturity text. | Follow the flat contract and current schema/code. |
| Singular vs plural release record lanes | `release/manifest/` and `release/manifests/` are documented as unresolved draft paths. | No record migration in this page. |
| `sha256:` vs proposed `jcs:sha256:` | Current code emits `sha256:`; ADR-0013 remains proposed. | Do not change wire identity by documentation. |
| Attestation refs vs cryptographic proof | Refs exist; signature verification is fixed false. | Signing integration remains unimplemented. |
| Release-policy source vs operational evaluator | Policy lane contains scaffolds without accepted bundle/evaluator/consumer closure. | Never infer allow or deny from scaffold defaults. |
| Release dry run vs release assembly | Current helper proves denial paths only. | Do not label it candidate assembly or release rehearsal success. |
| Documentation path vs dedicated workflow triggers | Target page is not listed in the release-manifest workflow filter. | General docs checks apply; dedicated coupling is follow-up. |
| Candidate and record inventory | No production candidate or governed release record was established by the inspected lanes. | Publication remains unknown/not established. |
| External standards matrix | Many relationships remain useful design lineage. | No external certification or blanket conformance claim. |

[Back to quick jump](#quick-jump)

---

## 14. Open questions

1. Which accepted profile graduates beyond `RELEASE_MANIFEST_FIXTURE_V1`, and what compatibility contract preserves legacy inputs?
2. When, if ever, may the permissive id-only branch be deprecated, and which producers/consumers still rely on it?
3. Are domain-specific ReleaseManifest schemas independent domain objects, projections, aliases, or drift requiring migration?
4. Which shared identity grammar is accepted, and how are `sha256:` and any future profile-tagged grammar migrated without split identity?
5. Which artifact bytes and fields are included in the signed subject and any future Merkle domain?
6. Which DSSE/Sigstore/SLSA/in-toto or alternate signing profile is accepted, and which signer/reviewer separation rules apply?
7. Which reference syntax, registry, resolver, freshness, revocation, and offline behavior govern each ref family?
8. Which finite production states exist beyond `CANDIDATE`, `HELD`, and `DEGRADED`, and which records authorize each transition?
9. Which lane is canonical for persisted release-manifest records, and how are singular/plural and domain-first paths converged?
10. Which policy bundle, evaluator, input contract, normalized outcomes, and authenticated release consumer are accepted?
11. Which public clients consume ReleaseManifest data, through which governed API or released artifact, and how is parity verified?
12. How do correction, withdrawal, supersession, rollback, alias restoration, cache/index invalidation, and historical verification compose?
13. Should `docs/standards/RELEASE_MANIFEST.md` be included in the dedicated workflow path filter, or are general documentation checks sufficient?
14. What evidence marks the first governed production release without confusing a fixture, workflow, GitHub release, or merge with publication?

[Back to quick jump](#quick-jump)

---

## 15. Related docs

### Repository authority and implementation

- [`docs/standards/README.md`](./README.md) — standards-lane authority and evidence limits.
- [`contracts/release/release_manifest.md`](../../contracts/release/release_manifest.md) — canonical semantic contract.
- [`schemas/contracts/v1/release/release_manifest.schema.json`](../../schemas/contracts/v1/release/release_manifest.schema.json) — dual-profile machine shape.
- [`fixtures/release/release_manifest/README.md`](../../fixtures/release/release_manifest/README.md) — synthetic fixture posture.
- [`tools/validators/release/validate_release_manifest.py`](../../tools/validators/release/validate_release_manifest.py) — deterministic candidate validator.
- [`tests/validators/test_validate_release_manifest.py`](../../tests/validators/test_validate_release_manifest.py) — focused no-network proof.
- [`.github/workflows/release-manifest.yml`](../../.github/workflows/release-manifest.yml) — read-only focused workflow.
- [`tools/release/release_dry_run.py`](../../tools/release/release_dry_run.py) — synthetic publication-denial helper.
- [`.github/workflows/release-dry-run.yml`](../../.github/workflows/release-dry-run.yml) — bounded denial/promotion/rollback readiness orchestration.
- [`policy/release/README.md`](../../policy/release/README.md) — release-policy source boundary and current scaffold hold.
- [`release/README.md`](../../release/README.md) — canonical release decision plane.
- [`release/manifests/README.md`](../../release/manifests/README.md) — draft record-lane guidance and singular/plural conflict.
- [`docs/standards/EVIDENCE_BUNDLE.md`](./EVIDENCE_BUNDLE.md) — current evidence-profile boundary.
- [`docs/standards/CANONICALIZATION.md`](./CANONICALIZATION.md) — current identity implementation and migration boundary.
- [`docs/standards/SIGNING.md`](./SIGNING.md) — signing design lineage; not current ReleaseManifest implementation proof.

### External references

- [RFC 8785 — JSON Canonicalization Scheme](https://www.rfc-editor.org/rfc/rfc8785.html)
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12)

[Back to quick jump](#quick-jump)

---

## Appendix A — Worked external verification

The legacy appendix name is retained. The current worked example is deliberately local, fixture-only, and non-authoritative.

```bash
# Run the exact focused test module.
python -m unittest tests.validators.test_validate_release_manifest -v

# Materialize and validate all 21 reviewed synthetic cases.
python tools/validators/release/validate_release_manifest.py --fixtures

# Exercise five synthetic publication-denial paths and related readiness checks.
make release-dry-run
```

Expected interpretation:

| Result | Meaning | Not equivalent to |
|---|---|---|
| Validator `PASS` | Candidate satisfies the bounded profile. | Evidence truth, policy allow, review approval, release, or publication. |
| Validator `FAIL` | Reviewable schema or semantic violation. | Complete policy denial or correction decision. |
| Validator `ERROR` | Input/schema/hashing operation could not be trusted. | Safe fallback to release. |
| Dry-run `PASS` | Every unsafe synthetic case remained blocked as expected. | A real candidate or successful release. |

All fixture IDs, refs, digests, actors, decisions, and artifacts are synthetic. Do not copy them into release records or use them as external verification evidence.

[Back to quick jump](#quick-jump)

---

## Appendix B — Placement rationale

`docs/standards/RELEASE_MANIFEST.md` remains the correct same-path home for human-readable profile, standards-relationship, conformance-readiness, and verification-boundary guidance.

It is not the correct home for:

- ReleaseManifest semantic meaning;
- JSON Schema or generated types;
- policy rules or evaluator code;
- fixtures, validators, or tests;
- release candidate or decision records;
- receipts, proofs, signatures, or attestations;
- published payloads, registries, aliases, caches, or deployments; or
- correction, withdrawal, rollback, or publication execution.

Those responsibilities remain in their owning roots. The existing path is therefore `PLACE`, not a new authority. A future rename or consolidation requires an inbound-link, anchor, consumer, compatibility, and rollback migration; this update performs none.

### No-loss disposition

| Legacy material | Disposition |
|---|---|
| External-conformance purpose | **CLARIFY** as relationships and graduation criteria. |
| Scope guardrail | **KEEP / strengthen** with current authority map. |
| JCS and SHA-256 | **REPAIR** to current `sha256:` implementation. |
| Merkle and BLAKE3 | **RETAIN as unimplemented design lineage**, not current profile. |
| Signing, DSSE, SLSA, Sigstore, in-toto, Rekor | **RETAIN as proposed closure**, remove false conformance. |
| OCI/ORAS/IPFS and catalog mappings | **RETAIN as proposed interoperability**, remove fictional transport/consumer claims. |
| Inclusion semantics | **RECONCILE** to the exact strict schema and validator. |
| Lifecycle, correction, withdrawal, rollback | **RECONCILE** to candidate-only refs and operational holds. |
| Delta-manifest tension | **KEEP** as unresolved object-family relationship. |
| External verification recipe | **REPLACE** fictional CLIs and production proof with current commands and future ladder. |
| Open questions | **REFRESH** against current compatibility, policy, workflow, record-lane, and consumer gaps. |
| Document ID, created date, headings, quick-jump, and appendix anchors | **KEEP** for lineage and link compatibility. |

[Back to quick jump](#quick-jump)
