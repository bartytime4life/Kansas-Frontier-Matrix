<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/stac-cdl-pmtiles-profile-decision-packet
title: STAC CDL and PMTiles Profile Decision Packet
type: exploratory-decision-packet
version: v0.1.0
status: proposed; decision-only; repository-grounded; non-authoritative
owners: OWNER_TBD — Catalog steward · Data-contract steward · Map steward · Validation steward · Docs steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory-intake; stac; cdl; pmtiles; no-authority
owning_root: docs/
responsibility: Record the repository-grounded decisions that must precede KFM-specific CDL and PMTiles STAC profiles without creating profile, namespace, catalog, policy, release, or publication authority.
truth_posture: CONFIRMED repository paths at main@202976d687e76dfb928f714b61d4a4eaea925bdc / PROPOSED decision sequence and future implementation slices / UNKNOWN hosted standards, live catalog, required-check, runtime, release, and public behavior
related:
  - ./pass20-expansion-conformance-baseline.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../standards/STAC.md
  - ../../standards/stac.md
  - ../../standards/STAC_KFM_PROFILE.md
  - ../../../schemas/contracts/v1/stac/kfm-profile-v1.schema.json
  - ../../../contracts/data/stac_attestation_hook.md
  - ../../../contracts/map/tiles3d_stac_item_adapter.md
notes:
  - "Source proposal: Pass 20 EXP-006, a CDL STAC Item and a PMTiles STAC Item with validators."
  - "This packet resolves no open decision and intentionally creates no STAC profile or machine shape."
[/KFM_META_BLOCK_V2] -->

# STAC CDL and PMTiles profile decision packet

> **Snapshot:** `main@202976d687e76dfb928f714b61d4a4eaea925bdc`,
> inspected 2026-08-10. This is a decision-preparation artifact, not an
> accepted standard, ADR, profile, registry entry, or implementation claim.

## Goal

Prepare the smallest collision-safe next step for Pass 20 `EXP-006`: one KFM
STAC Item profile for a synthetic Cropland Data Layer yearly bundle and one for
a synthetic PMTiles archive, each eventually paired with offline validation.

The repository already contains several STAC standards, profiles, adapters, and
validators. Adding two more schemas before resolving their authority and
composition rules would create exactly the parallel-profile drift that
Directory Rules forbids. This packet therefore records the conflicts, owners,
decisions, acceptance criteria, and ordered implementation slices that must
precede profile code.

## Evidence basis

| Evidence | Status | Contribution |
|---|---|---|
| Attached `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md`, `EXP-006` (`sha256:57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780`) | `PROPOSAL LINEAGE` | Proposes CDL and PMTiles Item profiles and one validator-backed fixture for each; warns about STAC extension drift. |
| Google Drive `New Ideas 5-15-26` (`gdrive://1boJrrqtqk9DcnzU8zymxFBv83r2-jvbep2kecj7WRCQ`) | `PROPOSAL LINEAGE` | Proposes yearly CDL Items with raster assets, projection metadata, checksums, and class-ontology references; also preserves exact-location safeguards for ecological joins. |
| Google Drive `New Ideas 5-19-26` (`gdrive://1Gx4pU71Pqk1cG1oKb8l69B8K4yOJK7zy5KNH-Xvl4HQ`) | `PROPOSAL LINEAGE` | Proposes immutable PMTiles sidecars, STAC discoverability, provenance, integrity, and governed publication checks. |
| [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) through accepted [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | `CONFIRMED PLACEMENT AUTHORITY` | Requires one authority per responsibility, contract/schema/policy separation, registered paths, and no parallel schema or policy homes. |
| Repository tree at the pinned snapshot | `CONFIRMED POINT-IN-TIME EVIDENCE` | Establishes the collisions and existing implementation surfaces listed below. |

The source documents provide implementation pressure, not current external
standard versions, profile authority, source admission, evidence, or release
approval. Repository evidence controls every implementation claim in this
packet.

## Current repository topology

### Human standards and profile claims

| Surface | Snapshot evidence | Decision impact |
|---|---|---|
| [`docs/standards/STAC.md`](../../standards/STAC.md) | Draft adoption reference; SHA-256 `96ce9f34306e1401b2afc18e3ea92afb7364a2b0977bf0dd7e266179cfd4ee17`; says `kfm:` versus `ks-kfm:` is open and points to a strict companion profile. | Cannot be silently treated as the sole accepted STAC authority. |
| [`docs/standards/stac.md`](../../standards/stac.md) | Distinct draft conformance document; SHA-256 `5a34c9105b44072885c16b050e28fb5755539cab1061c4ba6b8d5edfd9d9873c`; calls itself canonical while retaining placeholder ownership and ADR-class questions. | Case-variant paths contain different bodies and overlapping authority claims. |
| [`docs/standards/STAC_KFM_PROFILE.md`](../../standards/STAC_KFM_PROFILE.md) | Human strict-profile candidate referenced by both the standards corpus and validators. | A CDL or PMTiles profile must compose with or explicitly supersede this candidate; it must not fork it. |
| [`schemas/contracts/v1/stac/kfm-profile-v1.schema.json`](../../../schemas/contracts/v1/stac/kfm-profile-v1.schema.json) | Machine profile shape with fixtures and validator coverage. | Existing schema identity and extension vocabulary must be reconciled before adding family specializations. |

The two case-variant standards files are not byte-equivalent and both remain
draft. This packet does not choose one, rename either path, migrate links, or
change any status.

### Existing bounded STAC implementations

| Family | Existing surface | Bounded claim |
|---|---|---|
| KFM trust profile | `schemas/contracts/v1/stac/`, `fixtures/contracts/v1/stac/`, `tools/validators/stac/validate_kfm_profile_v1.py` | Local profile-shape and trust-state fixture validation exists. |
| Attestation hook | [`contracts/data/stac_attestation_hook.md`](../../../contracts/data/stac_attestation_hook.md) plus paired schema, fixtures, validator, tests, and workflow | Declared STAC-to-attestation reference posture; no signature or release authority. |
| Search behavior | `contracts/data/stac_search_behavior_fixture_profile.md` plus paired validation packet | Offline request/response behavior fixtures; no live STAC service. |
| Zarr asset metadata | `contracts/data/stac_zarr_asset_metadata_profile.md` plus paired validation packet | Declared array/chunk metadata only; no store access. |
| GeoParquet mirror | `contracts/data/stac_geoparquet_mirror_assessment.md` plus paired validation packet | Fixture-only mirror assessment; no catalog mutation. |
| Source HEAD prefilter | `contracts/source/stac_asset_head_prefilter.md` plus paired validation packet | Declared header-prefilter behavior; no network source activation. |
| 3D Tiles adapter | [`contracts/map/tiles3d_stac_item_adapter.md`](../../../contracts/map/tiles3d_stac_item_adapter.md) plus paired schema, fixtures, validator, tests, and workflow | Deterministic unreleased Item construction from local verified bytes. |

These families demonstrate accepted responsibility-root patterns but do not
define CDL or PMTiles Item semantics. Repository search at the snapshot found
no CDL-and-PMTiles specialization pair satisfying `EXP-006` closure.

### Existing PMTiles and CDL owners

| Concern | Existing owner | Constraint on future STAC work |
|---|---|---|
| PMTiles artifact meaning and validation | PMTiles standards, attestation bundle, delta manifest, release/cache, and map-carrier contracts already present under their responsibility roots | A STAC Item may reference these objects; it must not redefine root hashes, signatures, release state, or viewer admission. |
| CDL source/change handling | `tools/ingest/cdl_watch/`, source/watch contracts, fixtures, and drift records | A STAC profile may catalog a declared synthetic yearly bundle; it must not activate the source, authenticate a bundle, or convert watcher output into catalog/release state. |
| Catalog closure | Existing catalog matrix, trust extension, and release-gate families | STAC conformance alone cannot establish evidence, policy, review, promotion, release, or publication closure. |

## Decisions required before profile implementation

| ID | Decision | Minimum evidence | Owner / route | Safe default while open |
|---|---|---|---|---|
| `STAC-CDL-PMT-DEC-01` | Which human STAC document is the single writable authority, and what compatibility treatment applies to the case-variant path? | Complete path/link inventory, authority comparison, redirect/alias plan, rollback, and accepted decision. | Docs + catalog stewards; ADR if identity or authority changes. | `HOLD_PROFILE_ADDITION`. |
| `STAC-CDL-PMT-DEC-02` | Which KFM namespace and resolvable extension identifier are canonical? | Current schema/fixture vocabulary inventory, external-standard review, migration impact, and versioning plan. | Schema + catalog stewards; ADR-class decision already signaled by both drafts. | Reuse no illustrative URI as accepted authority. |
| `STAC-CDL-PMT-DEC-03` | Are CDL and PMTiles specializations schemas, semantic contracts composed over the existing KFM profile, or validator-only fixture profiles? | Composition model showing one base schema identity and no duplicated core fields. | Data-contract + schema stewards. | Prefer additive composition; deny copied base schemas. |
| `STAC-CDL-PMT-DEC-04` | Which official extension versions and fields are admitted for raster/projection/file/checksum metadata? | Authoritative specification review pinned by version and retrieval date; compatibility fixtures. | Catalog + schema stewards. | Mark versions `NEEDS VERIFICATION`; do not infer from source prose. |
| `STAC-CDL-PMT-DEC-05` | How is CDL class-map/ontology identity referenced without asserting crop truth? | Existing ontology identity, source-role, temporal-vintage, and correction contracts; one synthetic negative case for missing class-map version. | Agriculture + source + catalog stewards. | `ABSTAIN` on unresolved class-map identity. |
| `STAC-CDL-PMT-DEC-06` | How does a PMTiles Item reference archive hash, sidecar, attestation, release manifest, and rollback target without treating any one as the others? | Existing object identities, link relation vocabulary, positive/negative reference-closure fixtures, and no-authority assertions. | Map + evidence + release stewards. | Item remains `unreleased`; missing or mismatched references deny bounded conformance. |
| `STAC-CDL-PMT-DEC-07` | What geometry, temporal, rights, sensitivity, and evidence fields are mandatory in each family? | Domain/source contracts, existing KFM profile, public-safe synthetic fixtures, and source-role review. | Domain + policy + evidence stewards. | No real source geometry or sensitive coordinates in fixtures. |
| `STAC-CDL-PMT-DEC-08` | What does validator success mean? | Explicit finite outcomes, schema-versus-semantic findings, deterministic identity, no-network tests, and authority non-effects. | Validation steward. | `PASS` means local fixture consistency only. |

None of these decisions is resolved merely because a similarly named file or
field already exists.

## Recommended dependency-closed sequence

### Slice A — authority and namespace decision

1. Inventory every consumer of `STAC.md`, `stac.md`,
   `STAC_KFM_PROFILE.md`, the current schema `$id`, and namespace fields.
2. Record the selected human authority, compatibility path, extension identity,
   and migration/rollback plan in an accepted decision.
3. Change no CDL, PMTiles, catalog, or release behavior in that decision.

### Slice B — synthetic CDL Item specialization

After Slice A, define one semantic specialization composed over the accepted
base profile, one closed machine shape only if composition requires it, and
fixture polarity for:

- yearly temporal extent and declared Kansas county/state scope;
- raster/projection metadata;
- checksum and source-artifact reference;
- class-map/ontology version reference;
- rights, source role, sensitivity, evidence, and unreleased state;
- missing class-map, checksum mismatch, role collapse, and authority overreach.

The validator must perform no HTTP request, raster read, source admission,
evidence resolution, catalog write, or release action.

### Slice C — synthetic PMTiles Item specialization

After Slice A, compose one Item candidate over the accepted base profile and
the existing PMTiles object families. Fixture polarity must keep distinct:

- the immutable PMTiles archive identity;
- archive/root hash and byte-integrity claims;
- sidecar identity;
- attestation reference and verification state;
- catalog state;
- release manifest and rollback target;
- publication state and viewer admission.

An archive with a missing or mismatched required reference must fail bounded
validation. A green fixture remains unreleased and unpublished.

### Slice D — cross-profile parity

Only after both specializations exist, add a small parity test proving that
shared KFM trust fields have one meaning and that family-specific fields do not
leak into the other profile. Hosted CI remains path-filtered and read-only.

## Proposed path plan — not yet authorized

Directory Rules places each responsibility in its existing root. The exact
topic segment and filenames remain contingent on Decisions 01–03.

| Responsibility | Candidate existing root | Placement boundary |
|---|---|---|
| Human authority/decision | `docs/adr/` or the accepted decision lane | Only if the change selects authority, identity, namespace, or migration. |
| Semantic family meaning | `contracts/data/` for catalog data projections, with map/source references rather than copied meaning | Contract describes meaning only. |
| Machine shape | `schemas/contracts/v1/stac/` or an accepted composed family segment | One base identity; no copied parallel core schema. |
| Synthetic examples | `fixtures/contracts/v1/...` | Public-safe, invented identities and geometries only. |
| Executable validation | `tools/validators/stac/` | Deterministic, no-network, no source/catalog/release mutation. |
| Enforcement proof | `tests/validators/stac/` and a path-filtered `.github/workflows/` file | Test posture only; no required-check claim. |
| Authoring accountability | `data/receipts/generated/` | Records generated change inputs and hashes; it is not evidence or release proof. |

This packet intentionally does not mint these paths. A reviewer can alter the
composition plan without reverting code or schema identity.

## Acceptance criteria for the future implementation campaign

- One accepted STAC human authority and one machine base-profile identity are
  named with migration and rollback treatment for existing consumers.
- The namespace and extension identifier are versioned and resolvable under an
  accepted decision.
- CDL and PMTiles profiles compose over the base instead of copying it.
- One valid and multiple negative synthetic fixtures exist per family.
- Fixture identities, arrays, and hashes are deterministic.
- Duplicate keys, non-finite numbers, symlinks, oversized inputs, unknown
  members, authority flags, and network-capable code fail closed.
- CDL validation does not fetch or authenticate USDA data and does not infer
  crop conditions, land use, or change.
- PMTiles validation does not verify a real signature, release an artifact,
  enable a viewer, or equate a carrier with evidence.
- The Item candidates remain explicitly proposed, internal, unreleased, and
  unpublished.
- Focused tests, schema polarity, docs metadata/links, YAML parsing, and
  generated-receipt integrity pass on the exact branch head.

## Non-effects

This packet does not:

- select or supersede a STAC authority;
- adopt a namespace, extension, checksum algorithm, schema, or policy;
- create a CDL or PMTiles STAC Item;
- fetch, admit, or activate any source;
- authenticate source bytes, evidence, attestations, reviewers, or signatures;
- mutate a catalog, registry, lifecycle record, release record, or public map;
- promote, release, deploy, publish, or authorize public use; or
- assert that any workflow is required or that any runtime is hosted.

## Validation and rollback

This decision-only packet is validated as documentation plus generated
authoring accountability. Repository-local metadata, link, and receipt checks
can prove only that its structure, references, and recorded bytes are
consistent.

Before merge, close the draft pull request and delete its branch. After an
authorized merge, revert the additive document and generated receipt. No
schema, profile, source, catalog, policy, release, deployment, or public
artifact requires rollback.
