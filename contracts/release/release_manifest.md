<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-release-release-manifest
title: contracts/release/release_manifest.md — ReleaseManifest Contract
type: contract
version: v0.3
status: draft; PROPOSED; schema-paired; dual-profile; fixture-only strict candidate; release-governance-core
owners: OWNER_TBD — Release steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Rights steward · Sensitivity steward · Review steward · Rollback steward · Docs steward
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-08-08
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
  - ../../tests/validators/test_validate_release_manifest.py
  - ../../docs/intake/exploratory/pass7-release-manifest-profile.md
  - ../../docs/architecture/release-discipline.md
  - ../../docs/standards/RELEASE_MANIFEST.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../data/proofs/
  - ../../data/receipts/
notes:
  - "Expanded from existing `contracts/release/release_manifest.md`; v0.3 preserves the v0.2 semantic baseline."
  - "Paired schema verified at `schemas/contracts/v1/release/release_manifest.schema.json`; schema status remains PROPOSED."
  - "The schema now preserves the permissive legacy `id`-required branch and adds a closed `PROPOSED_INACTIVE` / `FIXTURE_ONLY` strict candidate branch."
  - "The strict branch is machine-checkable but not production release authority; ref resolution, real byte/signature verification, policy execution, authenticated review, release persistence, publication, and public use remain outside this validator."
  - "ReleaseManifest is semantic/object meaning. It is not the release artifact store, not proof closure by itself, not policy approval, not a promotion decision, not a public API/UI/map surface, and not AI truth."
  - "Rollback target for the v0.3 hardening is prior blob SHA `9ca1c9d4a5b247196aa84a31a158fe734c8a6720`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ReleaseManifest Contract

> `ReleaseManifest` is the governed release binding for a published artifact set. It identifies the release, lists or references the release contents, binds digests/spec lineage, carries evidence/rights/sensitivity/policy/review/attestation/rollback/correction context, and gives downstream consumers a stable thing to verify. It does **not** publish content by itself, store release payloads, replace promotion decisions, or allow public clients to bypass governed interfaces.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Object: ReleaseManifest" src="https://img.shields.io/badge/object-ReleaseManifest-0a7ea4">
  <img alt="Schema: dual profile" src="https://img.shields.io/badge/schema-dual__profile-orange">
  <img alt="Publication: gated" src="https://img.shields.io/badge/publication-gated-critical">
  <img alt="Artifacts: referenced only" src="https://img.shields.io/badge/artifacts-referenced__only-lightgrey">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/release/release_manifest.md`  
**Paired schema:** `schemas/contracts/v1/release/release_manifest.schema.json`  
**Schema maturity:** dual-profile — legacy permissive compatibility plus closed fixture-only strict candidate  
**Validator:** `tools/validators/release/validate_release_manifest.py` — CONFIRMED fixture-only implementation  
**Policy authority:** `policy/release/`, not this contract  
**Release artifact/process authority:** `release/`, not this contract  
**Truth posture:** CONFIRMED schema pairing, legacy compatibility, strict fixture validation, deterministic identity, and finite synthetic outcomes · PROPOSED production release shape and integration until refs, bytes, signatures, policy, review, release persistence, correction propagation, rollback, and public consumers are verified

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Schema-paired field surface](#schema-paired-field-surface) · [Fixture-only strict profile](#fixture-only-strict-profile-v03) · [Target semantic field families](#target-semantic-field-families) · [Field semantics](#field-semantics) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Validation expectations](#validation-expectations) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

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

The paired schema now exposes two explicitly different branches.

| Profile | Required shape | Compatibility / authority posture |
|---|---|---|
| Legacy minimal | `id` is required; optional `spec_hash` and `version`; additional properties remain allowed. | Preserves prior scaffold compatibility. It is not proof of release completeness. |
| `RELEASE_MANIFEST_FIXTURE_V1` | Closed strict candidate with deterministic identity, artifacts, source/evidence/decision refs, release scope, temporal scope, lineage, provenance, and false authority flags. | `PROPOSED_INACTIVE` / `FIXTURE_ONLY`; never production release or publication authority. |

> [!WARNING]
> Legacy schema permissiveness still means an id-only instance may validate while remaining release-incomplete. The strict branch closes only local candidate shape and bounded semantics; it does not resolve references or confer stronger authority.

---

## Fixture-only strict profile v0.3

Pass 7 card `KFM-P7-PROG-0003` describes one signed, hashable release object that lists included datasets, EvidenceBundles, tile archives, and LayerManifests, and directs consumers to a fixed manifest instead of a floating `latest` pointer. v0.3 implements the smallest dependency-closed precursor: a deterministic, no-network candidate profile.

### Strict candidate meaning

| Field family | Fixture-only rule |
|---|---|
| Identity | `id` and `spec_hash` are derived from RFC 8785 JCS plus SHA-256 with only stored `id` and `spec_hash` omitted. |
| Contents | `artifacts[]` carries opaque refs, exact SHA-256 digests, media types, and bounded roles; payload bytes are never embedded. |
| Authority refs | SourceDescriptor, EvidenceBundle, policy, promotion, review, catalog, proof, receipt, and attestation refs remain separate. |
| Release scope | Intended audience, rights, sensitivity, generalization, and transform receipts are declared without authorizing exposure. |
| Time and lineage | Assembly/effective times, predecessor, correction, withdrawal, and rollback refs stay explicit. |
| Governance | Every authority-bearing flag is fixed to `false`. |

### Strict semantic invariants

1. `artifact_count` equals the artifact array length.
2. Artifacts and reference arrays are canonical, sorted, and duplicate-free.
3. Floating `latest` references and cross-role reference collapse fail closed.
4. EvidenceBundle refs must have matching `EVIDENCE_BUNDLE` artifact entries.
5. Public-intended candidates require approved rights plus evidence, policy, promotion, and review refs.
6. `TRANSFORM_REQUIRED` requires generalized output and transform-receipt support.
7. Effective time cannot run backward; corrections require a predecessor.
8. Diagnostics emit stable codes and JSON-pointer paths without echoing untrusted values.
9. PASS keeps all governance authority flags false.

### Finite outcome and non-effects

The validator emits `PASS`, `FAIL`, or `ERROR`. A PASS proves only selected local candidate bytes and declared relationships. It does **not** resolve refs, verify real artifact bytes or signatures, execute policy, authenticate review, approve promotion, persist release state, publish, update aliases or caches, activate a public route, or authorize public use.

### Responsibility split

| Responsibility | Home |
|---|---|
| Semantic meaning | `contracts/release/release_manifest.md` |
| Machine shape | `schemas/contracts/v1/release/release_manifest.schema.json` |
| Synthetic matrix | `fixtures/release/release_manifest/` |
| Executable validation | `tools/validators/release/validate_release_manifest.py` |
| Behavior proof | `tests/validators/test_validate_release_manifest.py` |
| Read-only CI | `.github/workflows/release-manifest.yml` |
| Persisted release decisions and records | `release/`; untouched by this candidate profile |

ADR-0029 adopts Directory Governance Standard v2. This packet uses established responsibility roots and creates no parallel release, schema, policy, proof, receipt, or publication home.

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

The fixture-only strict branch uses a content-derived `release-manifest:<24 hex>` candidate identifier. That candidate convention is not yet the production release identifier decision.

### `spec_hash`

Deterministic hash claiming spec or content lineage.

The legacy branch keeps it optional. The strict fixture branch requires RFC 8785 JCS plus SHA-256 over the complete candidate with only stored `id` and `spec_hash` omitted. Production-grade signing and manifest-digest policy remain separately governed.

### `version`

Release/object version string.

The legacy branch keeps it optional. The strict branch uses `release_version`; mature release usage still needs an accepted versioning and compatibility policy for comparison, rollback, supersession, cache invalidation, and audit.

---

## Invariants

CONFIRMED by paired schema and fixture validator:

- The legacy branch still requires only `id` and permits additional properties.
- The strict branch is selected by `object_type: ReleaseManifest`, is closed, and fixes `profile_status`, `execution_mode`, and `lifecycle_state` to inactive candidate values.
- Strict candidates require deterministic identity, release/artifact/ref/scope/time/lineage/provenance context, and false governance flags.
- Unknown fields fail the strict branch.
- Four valid and seventeen invalid synthetic cases have exact reviewed polarity.

Production semantic invariants remain:

- A release manifest must not be a floating `latest` pointer.
- A production release manifest should include deterministic digest/spec lineage.
- A release manifest should list or reference every artifact included in the release.
- Every release-visible claim that depends on evidence must link to resolvable EvidenceBundle support.
- Release policy and promotion decisions must be recorded before a release is treated as PUBLISHED.
- Rights, sensitivity, review, correction, and rollback posture must be explicit or fail closed.
- Release manifests do not store release artifacts, proofs, receipts, raw data, work data, quarantine data, UI state, or AI output.
- A new release, correction, withdrawal, or rollback should supersede prior manifests without silently mutating them.
- Public clients should bind to released manifests and governed APIs, not raw/candidate/internal stores.

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

The v0.3 strict fixture profile stays at `CANDIDATE` and cannot perform the transition to `PUBLISHED`.

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

CONFIRMED for the inactive fixture slice:

- closed strict schema plus preserved legacy branch;
- deterministic RFC 8785 JCS/SHA-256 identity;
- exact positive and negative fixture polarity;
- no-network validator, focused tests, a dedicated read-only workflow, and release-dry-run hold reconciliation;
- generated authoring receipt bound to exact changed bytes.

NEEDS VERIFICATION before production use:

- accepted production-required field set and compatibility version;
- authenticated reference resolution and artifact-byte verification;
- release policy execution and separation-of-duties enforcement;
- signing/attestation strategy and verifier identity policy;
- persisted release record and artifact storage conventions under `release/`;
- rollback, correction, withdrawal, supersession, and cache invalidation drills;
- public client tests proving binding to released manifests rather than raw/latest/internal sources.

---

## Fixtures

The v0.3 grouped fixture matrix contains:

| Fixture class | Count | Purpose |
|---|---:|---|
| Valid | 4 | Legacy compatibility, internal candidate, public-intended candidate, and correction candidate. |
| Schema-negative | 2 | Missing required release identity and unknown-field denial. |
| Semantic-negative | 15 | Identity, canonical order, count, evidence binding, floating refs, role collapse, public rights/policy/promotion/review, transform support, time, and correction lineage. |

Fixtures use synthetic refs and repeated placeholder digests only. They represent no real source, reviewer, policy decision, signature, release, URL, or KFM publication.

---

## Open questions

- What exact production profile supersedes or graduates the inactive fixture branch?
- Which signing/attestation fields and verifier identities are mandatory for public release?
- Should `MapReleaseManifest`, `LayerManifest`, `TileArtifactManifest`, and `StyleManifest` remain separate linked objects or enter a typed production contents registry?
- Which release root stores persisted manifest instances and how are aliases/caches updated transactionally?
- Which gate owns final release authority and separation-of-duties enforcement?
- How do public consumers verify released manifest identity, artifact bytes, correction state, and rollback state without reaching internal stores?

---

## Rollback

Rollback is required if this contract is used to store release artifacts, bypass schema/policy/review/evidence gates, treat a manifest as publication approval without gate closure, silently mutate public release state, bypass correction/rollback lineage, or authorize public API/UI/map/AI exposure directly.

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the v0.3 contract/schema/validator/fixture/test/workflow/release-dry-run/receipt packet or restore this contract to blob `9ca1c9d4a5b247196aa84a31a158fe734c8a6720`. No source activation, data migration, release, deployment, publication, cache, or public artifact requires rollback because the strict profile is inactive and fixture-only.

<p align="right"><a href="#top">Back to top</a></p>
