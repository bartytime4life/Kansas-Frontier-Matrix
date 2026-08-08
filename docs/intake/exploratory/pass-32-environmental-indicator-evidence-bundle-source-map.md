<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pass-32-environmental-indicator-evidence-bundle-source-map
title: Pass 32 Environmental Indicator EvidenceBundle Source Map
type: source-adaptation-record
version: v0.1.0
status: draft; PROPOSED adaptation; repository-grounded; non-authoritative
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; exploratory-intake; pass-32; evidence-profile
owning_root: docs/
responsibility: Record how selected Pass 32 downstream-carrier ideas were reconciled with current repository evidence and narrowed into one fixture-only review slice.
truth_posture: "CONFIRMED source and repository evidence; PROPOSED profile; UNKNOWN operational state; NEEDS VERIFICATION human review"
related:
  - ../../../contracts/evidence/environmental_indicator_evidence_bundle_profile.md
  - ../../../schemas/contracts/v1/evidence/environmental_indicator_evidence_bundle_profile.schema.json
  - ../../../fixtures/contracts/v1/evidence/environmental_indicator_evidence_bundle_profile/cases.json
  - ../../../tools/validators/validate_environmental_indicator_evidence_bundle_profile.py
  - ../../../tests/validators/test_validate_environmental_indicator_evidence_bundle_profile.py
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
tags: [kfm, pass-32, source-map, evidence-bundle, environmental-indicator, intake, fixture-first]
notes:
  - "The Pass 32 atlas is a downstream carrier and remains non-authoritative."
  - "This record admits only the dependency-closed environmental EvidenceBundle profile; live computation, source activation, policy, UI, and release work are deferred."
  - "Current repository evidence was inspected before selecting responsibility roots and the reuse boundary."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Pass 32 Environmental Indicator EvidenceBundle Source Map

## Goal

Turn the smallest dependency-closed portion of Pass 32 cards `KFM-P32-IDEA-0013` and `KFM-P32-PROG-0007` into a reviewable repository capability without treating the atlas, a derived indicator, or a local schema pass as evidence or publication authority.

## Truth and source boundary

The Pass 32 atlas explicitly describes itself as a downstream carrier. Its candidate cards are proposal pressure, not adopted repository law.

| Source card | Card state | Source proposal | Adaptation in this slice |
|---|---|---|---|
| `KFM-P32-IDEA-0013` | `NEW`, `active`, `PROPOSED` | EvidenceBundle sidecars should include STAC asset references, ETags, thresholds, cluster summaries, and `spec_hash`. | Opaque asset references, ETag SHA-256 digests, threshold profile, cluster summary, and deterministic hash bindings. |
| `KFM-P32-PROG-0007` | `NEW`, `active`, `PROPOSED` | Environmental indicator schema requiring evidence references, method, window, thresholds, county FIPS, cluster summary, `spec_hash`, and `computed_at`. | Closed fixture-only machine profile with those fields plus ranked rows, explicit data state, source role, and no-authority claims. |

Source-card identities:

```text
KFM-P32-IDEA-0013
sha256:320d637539e98388dab0c1c0c99434a95e9b53832f75b27d1badfabdab6651c6

KFM-P32-PROG-0007
sha256:f47297f9f254f6845ecf809cc78330769ddc99babe0a9932cfc0cc06a30ac092
```

These hashes identify the atlas cards. They are not implementation hashes, evidence digests, or release attestations.

## Current repository evidence inspected

At the selected base revision, the repository already contains:

- the semantic `EvidenceBundle` contract under `contracts/evidence/`;
- the global EvidenceBundle schema under `schemas/contracts/v1/evidence/`;
- EvidenceRef, sensitivity-label, and spec-hash schemas;
- the repository RFC 8785 JCS plus SHA-256 hashing package;
- the local JSON Schema registry resolver;
- fixture-first validator and workflow patterns;
- generated-receipt validation; and
- accepted ADR-0029 plus the adopted Directory Rules v2 document.

This evidence rules out a parallel EnvironmentalEvidenceBundle authority. The selected design is a profile containing the existing `EvidenceBundle`, not a copied or widened global schema.

## Directory Rules decision

| Responsibility signature | Decision |
|---|---|
| Primary responsibility | Evidence semantics and bounded profile validation |
| Owning roots | `contracts/`, `schemas/`, `fixtures/`, `tools/`, `tests/`, `.github/`, `docs/`, and `data/receipts/generated/` for their existing responsibilities |
| Lifecycle phase | None; fixture and validation artifacts only |
| Execution role | Offline validator and hosted read-only orchestration |
| Exposure | Internal review surface; no public data |
| Mutability | Source-controlled proposal |
| Retention | Git history and generated authoring receipt |
| Root admission | No new root |
| ADR trigger | No authority-root, lifecycle, schema-home, or public-path change |

## Admission ledger

### Admitted and implemented

| Candidate element | Disposition | Reason |
|---|---|---|
| Existing EvidenceBundle reuse | `ADMIT` | Current semantic and machine owners already exist. |
| Derived-analysis source role | `ADMIT` | Prevents the result from masquerading as observation truth. |
| Opaque STAC/KFM asset references | `ADAPT` | Preserves provenance pointers without admitting source bytes or live URLs. |
| ETag digests | `ADAPT` | Retains change-identity metadata while preventing raw token disclosure. |
| Method and window | `ADMIT` | Required to reconstruct the proposed computation scope. |
| Threshold profile and thresholds | `ADMIT` | Makes interpretation parameters explicit and hash-bound. |
| County FIPS and ranked rows | `ADMIT` | Adds deterministic county-level result identity and support links. |
| Cluster summary | `ADMIT` | Adds bounded component summaries without geometry or precise coordinates. |
| `POPULATED` / `EMPTY` / `NO_DATA` | `ADAPT` | Prevents missing input from being represented as a zero condition. |
| Deterministic hashes and analysis ID | `ADMIT` | Uses existing repository hashing authority. |
| Exact positive and negative fixtures | `ADMIT` | Provides non-vacuous, reviewable behavior. |
| No-network workflow | `ADMIT` | Proves the proposed local profile without source access. |

### Deferred

| Candidate | Status | Required next evidence |
|---|---|---|
| County NDVI delta computation (`KFM-P32-PROG-0005`) | `DEFERRED` | Domain method contract, source descriptor, source rights, numeric test oracle, uncertainty semantics, and policy boundary. |
| Connected-component vegetation gate (`KFM-P32-PROG-0006`) | `DEFERRED` | Geometry/neighborhood definition, scale support, deterministic fixture topology, and derived-claim policy. |
| OPA promotion gate (`KFM-P32-PROG-0008`) | `DEFERRED` | Accepted policy input contract, obligations, reviewer authority, release-candidate binding, and branch-protection coupling. |
| Live STAC/ETag resolution | `DEFERRED` | Admitted source, terms, rate limits, credentials boundary, retry semantics, cache policy, and receipts. |
| Environmental bundle registry and supersession | `DEFERRED` | Registry owner, append-only/compaction policy, lineage contract, correction behavior, and migration strategy. |
| Map/API/Evidence Drawer projection | `DEFERRED` | Released public-safe object, governed API contract, layer manifest, citation payload, correction path, and rollback target. |

### Rejected from this review boundary

| Candidate behavior | Disposition | Reason |
|---|---|---|
| Raw ETag storage | `REJECT` | Token values are unnecessary for fixture-level identity and could leak source metadata. |
| Source payload or URL admission | `REJECT` | This is not an ingestion or network slice. |
| Observation authority | `REJECT` | The object is a derived analysis. |
| Policy, review, promotion, release, or publication claims | `REJECT` | No authoritative decision process is executed. |
| Geometry or exact coordinates in cluster summaries | `REJECT` | Not required for the card and would widen sensitivity and spatial-validation scope. |
| New source, registry, policy, catalog, proof, or release home | `REJECT` | Would create or imply parallel authority. |

## Dependency-closed implementation packet

```text
contracts/evidence/environmental_indicator_evidence_bundle_profile.md
schemas/contracts/v1/evidence/environmental_indicator_evidence_bundle_profile.schema.json
fixtures/contracts/v1/evidence/environmental_indicator_evidence_bundle_profile/cases.json
tools/validators/validate_environmental_indicator_evidence_bundle_profile.py
tests/validators/test_validate_environmental_indicator_evidence_bundle_profile.py
.github/workflows/environmental-indicator-evidence-bundle-profile.yml
data/receipts/generated/genrec-pass32-environmental-indicator-evidence-bundle-profile-20260808.json
docs/intake/exploratory/pass-32-environmental-indicator-evidence-bundle-source-map.md
```

## Acceptance boundary

The slice is complete only when:

1. the profile schema is closed and reuses the current global EvidenceBundle schema;
2. all profile fields proposed by the selected cards are represented or explicitly adapted;
3. all hashes and the analysis ID recompute deterministically;
4. ranked and cluster evidence identifiers close against the embedded bundle;
5. source descriptor, claim scope, and indicator checksum bindings are exact;
6. `POPULATED`, `EMPTY`, `NO_DATA` fixtures remain distinct;
7. invalid role, identity, hash, order, reference, cluster, checksum, and raw-ETag states fail closed;
8. diagnostics are deterministic and do not echo candidate values;
9. tests prove no network access;
10. the generated authoring receipt binds final artifact bytes; and
11. hosted exact-head checks and human semantic review remain separate from local authoring proof.

## Non-effects

This source map and its implementation packet do not activate a source, fetch data, compute a real environmental indicator, resolve external evidence, evaluate policy, create lifecycle state, release an artifact, publish a layer, or authorize public use.

## Rollback

Before merge, close the draft pull request and delete its feature branch. After merge, revert the bounded commit or merge commit. No data migration, source shutdown, cache invalidation, deployment rollback, or public correction is required because the slice creates no live or published state.

<p align="right"><a href="#top">Back to top</a></p>
