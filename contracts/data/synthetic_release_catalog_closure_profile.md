<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/synthetic-release-catalog-closure-profile
title: Synthetic Release Catalog Closure Profile
class: semantic-contract-profile
version: 0.1.0
status: proposed
truth_posture: cite-or-abstain
responsibility_root: contracts/
owner: OWNER_TBD — Catalog steward · Release steward · Evidence steward · Contract steward
created: 2026-08-16
updated: 2026-08-16
policy_label: internal; proposed; synthetic-only; no-network; non-authoritative
related:
  - ./catalog_matrix_closure_profile.md
  - ./catalog_distribution_mapping_profile.md
  - ../release/release_manifest.md
  - ../release/release_proof_pack_closure.md
  - ../../schemas/contracts/v1/data/synthetic_release_catalog_closure_profile.schema.json
  - ../../fixtures/contracts/v1/data/synthetic_release_catalog_closure_profile/
  - ../../tools/validators/catalog_closure/validate_synthetic_release_catalog_closure.py
  - ../../tests/validators/catalog_closure/test_synthetic_release_catalog_closure.py
  - ../../docs/adr/ADR-0011-receipts-proofs-manifests-catalog-separation.md
  - ../../docs/adr/ADR-0015-prov-stac-dcat-profiles.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "Fixture-only additive profile. It composes existing release, evidence, policy, review, receipt, proof, correction, rollback, and catalog responsibilities without replacing them."
  - "PASS proves deterministic local projection agreement only. It creates no evidence, review, policy, promotion, release, serving, publication, or public-use authority."
[/KFM_META_BLOCK_V2] -->

# Synthetic Release Catalog Closure Profile

> **PROPOSED:** Build one deterministic, no-network closure packet from one
> already assembled synthetic release candidate and derive mutually consistent
> STAC, DCAT, and PROV projections without hand-authoring public truth.

## Verified gap and bounded purpose

KFM already has separate fixture profiles for CatalogClosurePacket,
CatalogMatrix identity/digest/release alignment, CatalogMatrix claim
non-overstatement, distribution-carrier mapping, ReleaseManifest, and
ReleaseProofPackClosure. Those surfaces prove important parts of the trust
chain independently. This profile closes one narrower integration seam:

```text
synthetic release candidate
  + immutable artifact identity and digest
  + EvidenceRef / receipt / proof references
  + policy and review posture
  + release-manifest reference
  + correction and rollback references
  -> deterministic STAC Collection + Item
  -> deterministic DCAT Dataset + Distribution
  -> deterministic PROV Entity + Activity + Agent
  -> one cross-profile closure report
```

The input remains a fixture candidate. The output remains a local test packet.
Neither is a lifecycle record or public catalog.

## Directory Rules basis

The adopted Directory Rules assign semantic meaning to `contracts/`, machine
shape to `schemas/`, synthetic proof material to `fixtures/`, executable
validation to `tools/`, regression proof to `tests/`, and CI orchestration to
`.github/workflows/`. The profile uses those existing responsibility roots and
adds no root, catalog store, provenance store, release store, or policy home.

## Authority separation

| Concern | Existing authority retained | Profile behavior |
|---|---|---|
| Evidence support | `EvidenceRef` / `EvidenceBundle` families | Requires nonempty canonical references; does not resolve or judge evidence. |
| Receipts and proofs | Their separate contracts and validators | Requires references and a declared synthetic proof-closure state; does not authenticate them. |
| Policy and review | `PolicyDecision` and review families | Requires `ALLOW` and `APPROVED` in the synthetic candidate; does not make either decision. |
| Release | `ReleaseManifest` and release proof-pack closure | Requires a release ID, manifest reference, artifact digest agreement, and `RELEASED`; does not promote or release. |
| Catalog projections | Existing STAC/DCAT/PROV profile lane | Derives bounded compatibility projections; does not create canonical truth or serve a catalog. |
| Correction and rollback | CorrectionNotice / RollbackCard families | Requires lineage for corrected or withdrawn candidates and preserves prior packet identity. |
| Publication | Governed publication controls | Hard-codes all authority and serving flags false. |

## Candidate requirements

A candidate declares:

- one stable release ID and ReleaseManifest reference;
- one immutable synthetic artifact with a SHA-256 digest-bound URN;
- spatial and temporal extents;
- a source role that exactly matches its source-descriptor role;
- known rights and an admitted license;
- public sensitivity and an explicit public-safe flag;
- sorted, unique evidence, receipt, and proof references;
- policy, review, release, and proof-closure states;
- correction and rollback references; and
- one finite transition: `CURRENT`, `CORRECTED`, or `WITHDRAWN`.

Direct `http://` or `https://` artifact locators are denied. Fixtures use
non-dereferenceable `urn:kfm:synthetic:...@sha256:<digest>` identifiers.

## Deterministic projections

The validator uses the repository hashing package (`RFC8785-JCS` + SHA-256) to
derive:

- one packet `spec_hash`;
- one packet ID from the first 24 hex characters of that hash; and
- one semantic digest covering the release, artifact, prerequisites,
  projections, and transition.

Every profile record repeats the same release ID, artifact ID, digest, bbox,
interval, source role, license, sensitivity, correction reference, rollback
reference, and authored time. Profile-native record IDs remain distinct.

The checked projection set is:

- STAC Collection and Item;
- DCAT Dataset and Distribution; and
- PROV Entity, Activity, and Agent.

These are bounded repository projections, not claims that this fixture
constitutes a public STAC API, RDF graph, DCAT endpoint, or standards-complete
deployment.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Candidate prerequisites are internally coherent, generated packet matches the closed schema, replay is byte-stable, and any supplied projections agree exactly. |
| `DENY` | A readable candidate is incomplete, inconsistent, unsafe, stale, authority-escalating, nondeterministic, or projection-divergent. |
| `ERROR` | The input, schema, or canonicalization cannot be evaluated safely. |

Reason codes are stable and non-secret. The validator does not echo internal
reference values in findings.

## Correction and withdrawal

A `CURRENT` candidate has no predecessor or correction notice. A `CORRECTED`
or `WITHDRAWN` candidate must name both. The derived packet receives a new
deterministic identity while all seven projection records move together to
`SUPERSEDED` or `WITHDRAWN`. The original expected packet remains immutable in
the fixture corpus.

No record is deleted. Correction and withdrawal do not rewrite historical
bytes.

## Negative guarantees

The fixture matrix denies at least:

- missing ReleaseManifest or proof prerequisites;
- manifest/artifact digest disagreement;
- STAC/DCAT/PROV identity, extent, source-role, rights, sensitivity, state, or
  lineage disagreement;
- unresolved rights or license;
- non-public sensitivity/public-safe mismatch;
- unreleased candidates;
- missing correction lineage;
- hand-authored projections that predate or disagree with the release input;
- noncanonical reference ordering;
- deterministic digest drift; and
- direct public/network locators.

## Command and write boundary

```bash
python tools/validators/catalog_closure/validate_synthetic_release_catalog_closure.py --fixtures
```

A caller may write one generated packet only by supplying
`--write-packet <explicit-path>`. Tests use a temporary directory. The
validator never writes `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`,
`PUBLISHED`, `release/`, or any public-serving surface.

## Acceptance evidence

Reviewable evidence requires:

- closed Draft 2020-12 schema validation;
- exact 17-case fixture polarity;
- two stable packet hashes plus byte-stable replay;
- cross-profile identity, extent, rights, sensitivity, review, release,
  correction, and rollback agreement;
- no-network tests;
- finite CLI exit codes;
- correction/withdrawal history preservation; and
- hosted exact-head focused and adjacent catalog/release validation.

Human review remains separate. A green check is not release or publication.

## Rollback

Before merge, close the draft PR and remove its scoped branch. After an
authorized merge, revert the additive contract, schema, fixtures, validator,
tests, and workflow through normal reviewed history. Existing catalog, release,
proof, receipt, evidence, policy, review, correction, rollback, and published
records remain unchanged.
