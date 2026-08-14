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
  - "NEEDS VERIFICATION — geospatial artifact and release stewards"
  - "NEEDS VERIFICATION — evidence, policy, security, validation, correction, and rollback stewards"
reviewers_required:
  - Architecture steward
  - Docs steward
  - Geospatial artifact steward
  - Evidence and proof steward
  - Policy and sensitivity steward
  - Security and signing reviewer
  - Release and rollback steward
created: 2026-05-09
updated: 2026-08-14
policy_label: public
truth_posture: cite-or-abstain
owning_root: docs/
responsibility_root: docs/
responsibility: "Record the proposed cryptographic release-binding decision for PMTiles and COG carriers while distinguishing current fixture-first and structural integrity proof from signer, promotion, release, and publication authority."
current_path: docs/adr/ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md
supersedes: []
superseded_by: []
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: c9ccb11ded141edbd79763982056a1e6f90b8866
  inspection_origin_commit: 45a78c4b4b537f9215b2e4dc90106df0aca5300b
  continuity_compare: 45a78c4b4b537f9215b2e4dc90106df0aca5300b...c9ccb11ded141edbd79763982056a1e6f90b8866
  continuity_result: "unrelated geology and RuntimeResponseEnvelope work only; no ADR-0023 or inspected geospatial-integrity surface changed"
  target_prior_blob: d57353d059383860a43fc129c1f39f3173f69119
  adr_index_blob: 938c5894c36b99e14810918e2c550ab0e92d53b1
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  geo_manifest_contract_blob: c7993b8bf8fbcbf01f0947a99a14d81509e89370
  geo_manifest_schema_blob: fcaa128400e7ef8dbf9fad15de797928dd133451
  geo_manifest_validator_blob: 243376995faef4d8f1fb86bbae1c62bf1d48f441
  geo_manifest_tests_blob: 680fec23e284df633c2f8edb1dd499c51a3649f9
  geo_manifest_workflow_blob: fa476a9d2d3ee7c855d1d86debd68de332ac7554
  geo_manifest_generated_receipt_blob: fbb0f5dda2feb53f983d64ed880fbf3090c5c7fa
  geo_manifest_latest_run_id: 31654973070
  geo_manifest_latest_run_head: 3911c519d9bc134c3ab0662fed6577ebd966813b
  geo_manifest_latest_run_result: "functional profile steps passed; generated authoring receipt integrity failed with ARTIFACT_DIGEST_MISMATCH"
  pmtiles_attestation_standard_blob: 372845bd9ee9877a96de2d01d824e003d22010b5
  pmtiles_attestation_workflow_blob: 7857db8fafc77b40c84f09d208ca6a60d2b7d4df
  pmtiles_policy_blob: 5ac2a37d468f99f9195667f723d99b2b7a3325f4
  pmtiles_shape_verifier_blob: 566c4393241a7eb519c0d8c7d88bb32128347d62
  pmtiles_attestation_run_id: 31820527528
  pmtiles_attestation_run_head: 45a78c4b4b537f9215b2e4dc90106df0aca5300b
  pmtiles_attestation_run_result: "success for repository-local structural checks and explicit cryptographic hold; no release authority"
  cog_integrity_contract_blob: 6469d1ec57666233bd111c55fc7b0a6d6f2cb11b
  cog_integrity_workflow_blob: 0619d6731b1150c076288abcdc6a255c8164b42e
  map_release_manifest_contract_blob: e2a70bdd659cf432901ee9d5544b8e1418c23e60
inspection_boundary: >
  Current-session GitHub reads covered the ADR/index state, accepted directory-governance
  boundary, KFMGeoManifest contract/schema/validator/tests/workflow and hosted failure,
  generated authoring receipt, PMTiles attestation standard/workflow/policy/verifier and
  hosted success, COG byte-range integrity candidate, MapReleaseManifest contract, and
  release/signature/serving documentation. No private key, approved signer registry,
  cryptographic verification, transparency service, production PMTiles or COG payload,
  public alias, CDN, deployment, live release packet, correction, cache invalidation,
  withdrawal, or rollback was exercised.
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
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
  - .github/workflows/pmtiles-attestation.yml
  - policy/rego/tiles_publish.rego
  - tools/attest/verify_cose.py
  - contracts/evidence/cog_byte_range_integrity_manifest.md
  - schemas/contracts/v1/evidence/cog_byte_range_integrity_manifest.schema.json
  - tools/validators/evidence/validate_cog_byte_range_integrity_manifest.py
  - .github/workflows/cog-byte-range-integrity-manifest.yml
  - contracts/release/map_release_manifest.md
  - schemas/contracts/v1/map/map_release_manifest.schema.json
  - tools/validators/map/validate_map_release_manifest.py
  - data/published/pmtiles/README.md
  - data/published/layers/README.md
  - release/manifest/README.md
  - release/manifests/README.md
  - release/signatures/README.md
  - tools/attest/README.md
tags: [kfm, adr, geospatial, pmtiles, cog, geo-manifest, dsse, cose, signature, integrity, release, rollback, trust-membrane]
notes:
  - "v1.3 preserves status proposed and creates no signing, policy, promotion, release, deployment, or publication effect."
  - "KFMGeoManifest now has a closed fixture-first schema, deterministic validator, synthetic fixtures, focused tests, and read-only CI; its latest functional steps passed while historical generated-receipt integrity failed."
  - "PMTiles has structural header, PMIDX, split-bundle, declared-manifest, RunReceipt-subject, and shape-only PMSIG checks; cryptographic verification and key trust remain explicit HOLD states."
  - "COG has a fixture-only whole-file and explicit byte-range integrity candidate; it does not parse TIFF, prove COG conformance, authenticate signatures, or authorize release."
  - "A default-deny PMTiles policy source and MapReleaseManifest fixture profile exist; evaluator-backed enforcement and a production signed release remain unproved."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0023 — Geo Manifest Signs Every PMTiles and COG Release

> **Proposed decision.** Before any PMTiles or Cloud-Optimized GeoTIFF artifact becomes a released public-safe carrier, KFM must bind the immutable artifact bytes to identity, evidence, provenance, policy, review, release, correction, and rollback state through one versioned `KFMGeoManifest` payload and one approved cryptographic binding. Missing, mismatched, unverifiable, superseded, revoked, withdrawn, or policy-inadmissible bindings fail closed.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![Geo manifest: fixture proof](https://img.shields.io/badge/geo%20manifest-fixture%20proof-1f6feb?style=flat-square)](#current-profile-register)
[![PMTiles: structural](https://img.shields.io/badge/PMTiles-structural%20only-f59e0b?style=flat-square)](#pmtiles-current-state)
[![COG: range candidate](https://img.shields.io/badge/COG-range%20candidate-f59e0b?style=flat-square)](#cog-current-state)
[![Cryptography: hold](https://img.shields.io/badge/cryptography-HOLD-b42318?style=flat-square)](#current-implementation-maturity)
[![Publication: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-and-publication-boundary)

> [!IMPORTANT]
> **Identity is confirmed; acceptance is not.** [`docs/adr/INDEX.md`](./INDEX.md) uniquely assigns `ADR-0023` to this exact file with source and effective status `proposed`. Accepted ADR-0029 governs placement; it does not accept this release-binding decision.

> [!CAUTION]
> **Repository proof has advanced without closing the trust chain.** KFMGeoManifest has executable fixture proof, PMTiles has structural attestation, COG has a synthetic range-integrity candidate, and MapReleaseManifest models release closure. Cryptographic verification, accepted signer trust, policy evaluation, promotion/release enforcement, serving anti-bypass behavior, and production correction/rollback remain held, unproved, or unknown.

> [!WARNING]
> **Structural integrity, signature shape, human signoff, and release authority are different.** A digest, range root, schema-valid manifest, shape-valid PMSIG, reviewer packet, or release-shaped fixture proves only its declared bounded property.

**Quick navigation:** [Status](#status) · [Evidence](#evidence-boundary) · [Decision](#proposed-decision) · [Profiles](#current-profile-register) · [Binding](#proposed-binding-model) · [Authority](#authority-and-publication-boundary) · [PMTiles](#pmtiles-current-state) · [COG](#cog-current-state) · [Release](#release-and-serving-state) · [Hosted CI](#hosted-workflow-evidence) · [Maturity](#current-implementation-maturity) · [Convergence](#implementation-and-convergence-plan) · [Acceptance](#acceptance-gates) · [Risks](#risk-ledger) · [Rollback](#rollback-and-supersession) · [References](#references) · [History](#revision-history)

---

<a id="status"></a>

## Status

| Field | Current value |
|---|---|
| **ADR ID** | `ADR-0023` — unique in [`INDEX.md`](./INDEX.md) |
| **Source/effective status** | `proposed` / `proposed` |
| **Decision class** | Geospatial artifact integrity, cryptographic binding, release eligibility, serving, correction, and rollback |
| **Directory authority** | Accepted ADR-0029 and Directory Rules v2; same-path `docs/adr/` placement |
| **Current posture** | Partial integrity proof; cryptographic release enforcement remains `HOLD` |
| **Implementation/publication effect** | Documentation only / none |
| **Supersedes / superseded by** | None / none |

**Acceptance and graduation are separate.** Accepting the ADR would approve the rule. Implementation graduation would require one accepted payload/envelope/profile composition operating over representative PMTiles and COG releases, with trusted signing, policy, review, release, serving, correction, and rollback evidence.

[Back to top](#top)

---

<a id="evidence-boundary"></a>

## Evidence boundary

This revision is grounded at `main@c9ccb11ded141edbd79763982056a1e6f90b8866`. The continuity compare from the initial inspection base changes unrelated geology and runtime-response files only.

| Surface | CONFIRMED | Not established |
|---|---|---|
| ADR/index and placement | Exact ADR identity, proposed status, accepted Directory Rules placement | ADR-0023 acceptance |
| KFMGeoManifest | Closed fixture shape, validator, fixtures, 15 tests, optional exact local-byte binding | Canonical signed release profile |
| PMTiles | Header/archive/PMIDX/split-bundle/declared-manifest/shape checks | Trusted signature, canonical composition, publication |
| COG | Whole-file and explicit range SHA-256 replay over synthetic bytes | TIFF/COG parsing, live Range, signature, release |
| Policy | Default-deny source requiring verified signature, approved builder, rollback, resolved policy | Accepted bundle/evaluator/consumer enforcement |
| Release | MapReleaseManifest fixture closure | Authenticated records, alias/cache transition, real release |
| External systems | None inspected | Keys, signer registry, transparency, CDN, deployment, production clients |

Truth labels: **CONFIRMED**, **PROPOSED**, **PARTIAL**, **CONFLICTED**, **NEEDS VERIFICATION**, **UNKNOWN**, and **HOLD** retain their ordinary KFM meanings.

[Back to top](#top)

---

<a id="proposed-decision"></a>

## Proposed decision

Upon acceptance and implementation graduation:

1. Every released PMTiles or COG artifact **MUST** have one immutable, version-bound `KFMGeoManifest` payload and one approved cryptographic binding over that payload.
2. Release **MUST** fail closed when payload, bytes, range commitments, signature, signer authorization, trust proof, evidence, policy, review, promotion, release, correction, or rollback state is missing, invalid, mismatched, expired where applicable, superseded, revoked, withdrawn, or inadmissible.
3. Catalogs, layer/tile manifests, receipts, proofs, reviewer signoffs, `PromotionDecision`, `ReleaseManifest`, and `MapReleaseManifest` **MUST** reference the binding where required; none replaces another family.
4. The payload **MUST NOT** embed the envelope or signature that signs it.
5. Manifest identity **MUST** use a schema-defined hash projection excluding `spec_hash` itself, envelope/signature data, transparency proofs, and transport-only fields.
6. Artifact-byte identity **MUST** remain distinct from manifest identity. A full-file digest binds complete bytes; an accepted range profile may add partial-read verification.
7. Signing **MUST** use an accepted, version-pinned DSSE, COSE, cosign, or successor profile with signer policy, trust roots, rotation, revocation, and offline/transparency behavior.
8. History **MUST** remain append-only under policy. Unsafe releases are superseded, withdrawn, corrected, revoked, or rolled back—not silently overwritten.
9. Public aliases, CDNs, APIs, MapLibre clients, service workers, and caches **MUST NOT** serve an artifact whose binding or release state cannot be verified.

`MUST` language describes the proposed accepted state, not current enforcement.

[Back to top](#top)

---

<a id="current-profile-register"></a>

## Current profile register

| Profile | CONFIRMED capability | Explicit boundary |
|---|---|---|
| KFMGeoManifest fixture-first | Closed metadata, profile-local identity, spatial/transform/governance/lineage checks, optional exact bytes | Fixed non-release/no-authority state; no signing or policy/review authentication |
| KFMGeoManifest dedicated CI | 15 tests, fixtures, meta-schema, and hash reporting passed in latest inspected run | Historical generated receipt failed integrity; workflow not green |
| PMTiles split bundle | PMTiles header, SHA-256, PMIDX leaves/root/ranges, PMSIG and RunReceipt subject reconciliation | Range metadata incomplete; cryptography and trust unwired |
| PMTiles declared-manifest compatibility | Opt-in archive/digest/size/spec/MVT/zoom/bounds/scheme/vector-layer reconciliation | Non-canonical; provenance/policy/release held |
| COG range-integrity candidate | Whole SHA-256, contiguous explicit range digests, declared range roles | Synthetic non-TIFF bytes; no COG, HTTP Range, signature, or release proof |
| MapReleaseManifest fixture profile | Synthetic closure over artifacts, catalogs, evidence, policy, review, attestations, correction, cache, rollback | Does not authenticate references, mutate state, or release |
| PMTiles Rego source | Default deny; requires verified signature, approved builder, rollback, resolved policy | Admission, native tests, evaluator, and consumer binding unproved |

A release implementation must name the exact composed profile versions. Passing one profile must not silently upgrade another.

[Back to top](#top)

---

<a id="proposed-binding-model"></a>

## Proposed binding model

### Object separation

| Object | Responsibility | Not a substitute for |
|---|---|---|
| PMTiles/COG bytes | Immutable carrier | Evidence, policy, release |
| KFMGeoManifest payload | Artifact identity, spatial meaning, integrity declarations, provenance/governance/lifecycle refs | EvidenceBundle, signature, approval |
| Range profile | Whole/partial-read commitments | Signature trust, public safety |
| Cryptographic envelope | Machine binding over payload | Human review or release decision |
| Signer trust record | Allowed signers, roots, expiry, rotation, revocation | Artifact content or evidence |
| EvidenceBundle/ProofPack | Claim support and proof | Artifact bytes or release decision |
| RunReceipt | Process memory | Proof, approval, publication |
| PolicyDecision | Rights, sensitivity, access, obligations | Signature or review |
| PromotionDecision | Accountable promotion outcome | Binding or receipt |
| ReleaseManifest/MapReleaseManifest | Release scope and artifact set | Per-artifact byte binding |
| Reviewer packet | Human review | Machine cryptography |
| Correction/rollback records | Governed repair intent and lineage | Proof of execution/cache propagation |

### Target layering

```text
<artifact>.kfm-geo-manifest.<envelope>.json
└── approved cryptographic envelope
    ├── payload type/profile
    ├── encoded canonical KFMGeoManifest payload
    ├── signature(s)
    └── optional offline/transparency verification material
```

Existing `.pmidx`, `.pmsig`, and RunReceipt compatibility objects may be composed or migrated; their presence does not define canonical authority.

### Hash domains

| Identity | Purpose | Boundary |
|---|---|---|
| Manifest `spec_hash` | Identity of declared manifest projection | Excludes self and envelope/transport fields; global grammar awaits ADR-0013 |
| Artifact digest | Complete PMTiles/COG bytes | Does not prove format, evidence, policy, signer, release |
| Range/chunk root | Partial-read commitment | Must bind index/range metadata; does not replace full digest |
| Release-packet digest | Integrity over governed release object set | Does not replace per-artifact binding or accountable decision |

[Back to top](#top)

---

<a id="authority-and-publication-boundary"></a>

## Authority and publication boundary

A valid binding would prove only that an approved verifier accepted the envelope/signer, payload, and evaluated byte commitments under a named profile. It would not independently prove source truth, evidence sufficiency, rights, public safety, accountable review, release authorization, alias selection, cache state, or successful rollback.

Public clients consume release-resolved artifacts through governed interfaces or approved immutable static delivery. They do not read RAW, WORK, QUARANTINE, internal proof/receipt stores, candidate artifacts, or direct model output as the normal path. No document, schema, validator, sidecar, signature-shaped file, workflow, merge, or URL creates `PUBLISHED` state.

### Directory Rules basis

Accepted ADR-0029 keeps decision records in `docs/adr/`, meaning in `contracts/`, shape in `schemas/`, policy in `policy/`, validation in `tools/` plus `fixtures/` and `tests/`, process memory/proof in their distinct `data/` families, and release/correction/rollback objects under `release/`. This update creates no new path or parallel authority.

[Back to top](#top)

---

<a id="pmtiles-current-state"></a>

## PMTiles current state

### Structural capability

Current synthetic/generated checks cover exact PMTiles v3 header and bounded metadata parsing, whole-file SHA-256, PMIDX leaves/root/ranges, cross-object `spec_hash` reconciliation, declared-manifest compatibility, and bounded PMSIG shape parsing.

### Explicit holds

- PMIDX does not yet authenticate every range-table or tile-identity claim.
- `verify_cose.py --shape-only` checks shape only; normal mode returns `PMSIG_CRYPTOGRAPHIC_VERIFICATION_UNWIRED`.
- Approved key registry, signer policy, rotation, revocation, transparency, and offline proof are absent.
- Canonical composition among PMTiles compatibility objects, KFMGeoManifest, and the cryptographic envelope remains unresolved.

A green no-candidate PMTiles workflow means readiness and explicit hold behavior completed; it does not mean a candidate signature passed.

[Back to top](#top)

---

<a id="cog-current-state"></a>

## COG current state

The fixture-only COG range candidate verifies bounded local availability, whole SHA-256, canonical in-bounds contiguous ranges, exact coverage, range SHA-256 replay, and declared header/IFD/tile/overview role coverage.

It intentionally uses a 65-byte synthetic non-TIFF payload. Roles are declared, not parser-derived. It does not validate TIFF/COG structure, HTTP Range, BAO/BLAKE3, signatures, evidence, pixel meaning, policy, review, promotion, release, or publication.

[Back to top](#top)

---

<a id="release-and-serving-state"></a>

## Release and serving state

`MapReleaseManifest` now models candidate, held, published, stale, superseded, withdrawn, and rolled-back fixture states. Synthetic published closure requires immutable artifact refs, catalogs, evidence, policy, rights, sensitivity, review, attestations, correction, cache invalidation, and rollback. It does not fetch artifacts, authenticate references, verify signatures, mutate caches, transition aliases, or publish.

`policy/rego/tiles_publish.rego` defaults to deny and requires PMTiles header validity, cross-object hash agreement, verified PMIDX root, verified PMSIG, approved builder, rollback presence, and resolved rights/sensitivity/review/release state. Source presence is not accepted evaluator-backed enforcement.

No inspected evidence proves immutable public alias resolution, CDN rejection of unbound candidates, Range/CORS tied to release, edge/client sidecar verification, cache invalidation after withdrawal, or public rollback execution.

[Back to top](#top)

---

<a id="hosted-workflow-evidence"></a>

## Hosted workflow evidence

### KFMGeoManifest

Latest inspected run `31654973070` at `3911c519d9bc134c3ab0662fed6577ebd966813b`:

| Step | Result |
|---|---|
| 15 no-network tests | PASS |
| Fixture polarity and byte binding | PASS |
| Draft 2020-12 meta-schema | PASS |
| Artifact hash reporting | PASS |
| Historical generated authoring receipt | FAIL — `ARTIFACT_DIGEST_MISMATCH` for workflow bytes |

Safe statement: **functional profile PASS / workflow FAIL / release authority none**. A separate corrective slice must emit a successor receipt through the legitimate producer, retain historical process memory, and prove exact-head green integrity.

### PMTiles Attestation

Run `31820527528` at `45a78c4b4b537f9215b2e4dc90106df0aca5300b` succeeded for readiness, generated compatibility bundles, header/completeness, PMIDX Merkle/archive, split reconciliation, and shape-only PMSIG denial. It proves structural checks and explicit no-cryptography hold behavior, not candidate signature trust or release.

[Back to top](#top)

---

<a id="current-implementation-maturity"></a>

## Current implementation maturity

| Level | Requirement | Current result |
|---:|---|---|
| 0 | ADR identity and placement | **CONFIRMED** |
| 1 | Closed geo-manifest candidate shape/meaning | **CONFIRMED / proposed fixture profile** |
| 2 | Validator, fixtures, tests, local byte binding | **CONFIRMED fixture-first** |
| 3 | COG whole/range integrity candidate | **CONFIRMED fixture-only** |
| 4 | PMTiles structural checks | **CONFIRMED structural** |
| 5 | Fail-closed PMTiles policy source | **CONFIRMED source / execution unproved** |
| 6 | Representative carrier-format validation | **PARTIAL / COG held** |
| 7 | Accepted payload, envelope, range composition | **CONFLICTED / not accepted** |
| 8 | Cryptographic verification and signer trust | **HOLD / unwired** |
| 9 | Policy evaluator, review, promotion, release | **HOLD / not established** |
| 10 | Serving/client/cache anti-bypass | **UNKNOWN** |
| 11 | Correction/withdrawal/revocation/rollback drill | **NOT ESTABLISHED** |
| 12 | Production signed PMTiles and COG release | **NONE PROVED** |
| 13 | Dedicated KFMGeoManifest CI integrity | **DEGRADED — functional PASS, receipt FAIL** |

**Overall: `PARTIAL — integrity proof exists; cryptographic release enforcement remains HOLD`.**

[Back to top](#top)

---

<a id="implementation-and-convergence-plan"></a>

## Implementation and convergence plan

### Wave 0 — restore validation integrity and decide authority

- emit a successor geo-manifest authoring receipt tied to current workflow bytes; preserve the historical receipt;
- prove exact-head green dedicated CI;
- inventory current PMTiles/COG/manifest/signature/release producers and consumers;
- accept, revise, or reject ADR-0023 and resolve its ADR-0013 dependency/profile isolation;
- choose canonical composition for KFMGeoManifest, TileArtifactManifest, PMIDX, PMSIG, and release manifests.

### Wave 1 — close payload and cryptographic profiles

- version semantic contract and closed release schema together;
- define canonical serialization, hash projection, media types, filenames, aliases, and migration;
- pin an approved DSSE/COSE/cosign or successor implementation;
- define signer identities, roots, custody, expiry, rotation, revocation, and offline/transparency proof;
- add cross-runtime canonicalization and valid/invalid/revoked signature vectors.

### Wave 2 — prove real carrier formats

- add production-like PMTiles v3 vectors and reconcile structural profiles;
- add real COG vectors covering tiling, IFDs, overviews, nodata, CRS, compression, and Range behavior;
- authenticate range/index metadata and test full-file plus partial-read integrity across platforms.

### Wave 3 — bind policy, release, and serving

- resolve evidence, source roles, rights, sensitivity, policy, review, promotion, release, correction, and rollback;
- require binding verification during release assembly and alias selection;
- deny candidate, superseded, revoked, withdrawn, or mismatched artifacts;
- test CDN, API, MapLibre, service-worker, offline, and cache bypass paths without granting uncontrolled publication credentials.

### Wave 4 — exercise correction and rollback

- test signer compromise, byte mismatch, policy revocation, correction, withdrawal, and rollback;
- atomically update aliases, invalidate caches, verify public Range responses, and retain append-only execution evidence.

[Back to top](#top)

---

<a id="acceptance-gates"></a>

## Acceptance gates

### ADR acceptance

- [ ] Accountable architecture, geospatial, evidence, security, policy, release, validation, docs, and rollback review.
- [ ] ADR-0013 dependency accepted or version-isolated.
- [ ] Object-family responsibilities and profile composition are non-overlapping.
- [ ] Hash, envelope, signer, transparency/offline, correction, and rollback semantics are versioned.
- [ ] No text implies current signing, release, or publication.

### Current bounded proof

- [x] Closed KFMGeoManifest fixture profile, validator, fixtures, and tests exist.
- [x] Latest inspected functional KFMGeoManifest steps passed.
- [ ] Generated authoring receipt matches current workflow bytes and exact-head CI is green.
- [x] PMTiles structural attestation and explicit cryptographic hold are exercised.
- [x] COG range-integrity candidate is fixture-tested without claiming COG conformance.
- [x] MapReleaseManifest closure is fixture-tested without claiming release.

### Implementation graduation

- [ ] Accepted payload/envelope/schema/profile composition.
- [ ] Real PMTiles and COG vectors pass pinned validators.
- [ ] Trusted cryptographic verification, authorization, rotation, and revocation pass.
- [ ] Evidence, policy, independent review, promotion, and release resolve.
- [ ] Public serving and clients cannot bypass verification.
- [ ] Correction, withdrawal, cache invalidation, and rollback drills pass.
- [ ] Failure paths produce no public write or optimistic fallback.

No gate is satisfied merely because a file, workflow, PR, merge, or signature-shaped object exists.

[Back to top](#top)

---

<a id="risk-ledger"></a>

## Risk ledger

| Risk | Status | Control |
|---|---|---|
| ADR not accepted | `PROPOSED` | Accountable decision review |
| Global hash grammar unresolved | `CONFLICTED` | ADR-0013 or versioned isolation |
| Split PMTiles versus envelope profile | `CONFLICTED` | Canonical composition/migration decision |
| Historical geo-manifest receipt stale | `CONFIRMED DRIFT` | Successor receipt and exact-head rerun |
| Fixture hash mistaken for release authority | `OPEN` | Profile IDs and explicit boundaries |
| PMSIG shape mistaken for signature | `OPEN` | Fail-closed verifier and trust profile |
| COG synthetic ranges mistaken for COG proof | `OPEN` | Real parser/fixtures and visible non-effects |
| Range metadata unauthenticated | `HOLD` | Bind index/range metadata and adversarial vectors |
| Signer identities/trust roots | `UNKNOWN` | Custody, expiry, rotation, revocation policy |
| Policy source mistaken for enforcement | `OPEN` | Native tests, evaluator, decisions, consumer binding |
| Release manifest path conflict | `CONFLICTED` | Accepted distinction or reversible migration |
| Public alias/CDN/cache bypass | `UNKNOWN` | Config, integration tests, monitoring, incident drills |
| Existing unsigned artifacts | `UNKNOWN` | Inventory and quarantine/withdrawal/migration decision |
| Compromised signer | `OPEN` | Revocation, alias rollback, correction, cache purge |
| Production signed release | `NONE PROVED` | Representative governed PMTiles and COG proof |

Fail-safe posture: unresolved signer, evidence, rights, sensitivity, profile, release, or binding state blocks public release.

[Back to top](#top)

---

<a id="rollback-and-supersession"></a>

## Rollback and supersession

### Documentation rollback

Before merge, close the draft pull request and abandon its branch. After merge, restore prior blob:

```text
d57353d059383860a43fc129c1f39f3173f69119
```

or revert the documentation commit. This does not revert independent implementation.

### Artifact rollback

A conforming future rollback must identify the unsafe artifact/payload/envelope/release; record accountable withdrawal/revocation/correction; preserve history; validate the rollback target; update aliases atomically; invalidate CDN/service-worker/search/map/API caches; verify public Range requests; notify affected users where appropriate; and retain append-only execution/post-rollback evidence.

Rollback is not deleting the bad file. An accepted successor ADR must preserve this record, link reciprocally, update the index, and migrate contracts, schemas, policy, producers, consumers, releases, and verification support.

[Back to top](#top)

---

<a id="references"></a>

## References

### Decision and governance

- [ADR index](./INDEX.md)
- [Artifact-family separation](./ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [Identity grammar](./ADR-0013-spec_hash-and-run_id-identity-grammar.md)
- [Published alias and rollback](./ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md)
- [Promotion sequence](./ADR-0018-promotion-gate-sequence.md)
- [Catalog matrix](./ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md)
- [Release duty separation](./ADR-0024-steward-separation-of-duties-for-release.md)
- [Public-client boundary](./ADR-0025-public-client-never-reads-canonical-internal-stores.md)
- [Accepted Directory Rules ADR](./ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules](../doctrine/directory-rules.md)

### Geo-manifest fixture profile

- [Contract](../../contracts/evidence/kfm_geo_manifest.md)
- [Schema](../../schemas/contracts/v1/evidence/kfm_geo_manifest.schema.json)
- [Fixtures](../../fixtures/evidence/kfm_geo_manifest/README.md)
- [Validator](../../tools/validators/evidence/validate_kfm_geo_manifest.py)
- [Tests](../../tests/validators/test_validate_kfm_geo_manifest.py)
- [Workflow](../../.github/workflows/kfm-geo-manifest-validation.yml)
- [Historical authoring receipt](../../data/receipts/generated/genrec-kfm-geo-manifest-validation-20260804.json)

### PMTiles, COG, and release profiles

- [PMTiles Attestation Standard](../standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md)
- [PMTiles workflow](../../.github/workflows/pmtiles-attestation.yml)
- [PMTiles publish policy source](../../policy/rego/tiles_publish.rego)
- [PMSIG shape verifier](../../tools/attest/verify_cose.py)
- [COG range contract](../../contracts/evidence/cog_byte_range_integrity_manifest.md)
- [COG range schema](../../schemas/contracts/v1/evidence/cog_byte_range_integrity_manifest.schema.json)
- [COG range validator](../../tools/validators/evidence/validate_cog_byte_range_integrity_manifest.py)
- [COG range workflow](../../.github/workflows/cog-byte-range-integrity-manifest.yml)
- [MapReleaseManifest contract](../../contracts/release/map_release_manifest.md)
- [MapReleaseManifest schema](../../schemas/contracts/v1/map/map_release_manifest.schema.json)
- [MapReleaseManifest validator](../../tools/validators/map/validate_map_release_manifest.py)
- [Published PMTiles lane](../../data/published/pmtiles/README.md)
- [Published layers lane](../../data/published/layers/README.md)
- [Release manifest lanes](../../release/manifests/README.md)
- [Human release-signature packets](../../release/signatures/README.md)

Planning material supports the decision direction but does not replace current repository proof. The supplied build-out prompt requires a current-evidence, smallest-coherent, reversible feature-branch update and separates implementation from merge, release, deployment, promotion, and publication.

[Back to top](#top)

---

<a id="revision-history"></a>

## Revision history

| Version | Date | Summary |
|---|---|---|
| `v1.3` | 2026-08-14 | Current-main evidence refresh: fixture-first KFMGeoManifest implementation and degraded authoring receipt; PMTiles structural attestation and cryptographic hold; COG range candidate; default-deny policy source; MapReleaseManifest fixture closure; accepted placement authority; convergence, acceptance, risk, and rollback update; status remains proposed. |
| `v1.2` | 2026-07-24 | Repository-grounded modernization; contract/schema-stub evidence, object separation, identity/path conflicts, hash projection, explicit implementation hold. |
| `v1.1` | 2026-05-15 | Payload/envelope layering, field map, gate mapping, negative fixtures, rollback and acceptance posture. |
| `v1` | 2026-05-09 | Initial proposed signed PMTiles/COG release-binding decision. |

---

**Last updated:** 2026-08-14 · **Decision:** `proposed` · **Current implementation:** partial integrity proof; cryptographic release enforcement `HOLD` · **Publication:** none · **Path:** `docs/adr/ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md` · [Back to top](#top)
