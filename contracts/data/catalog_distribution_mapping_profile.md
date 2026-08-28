<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/catalog-distribution-mapping-profile
title: Catalog Distribution Mapping Profile
class: semantic-contract-profile
type: semantic-contract-profile
version: 0.1.0
status: proposed
owner: OWNER_TBD — Catalog steward · Provenance steward · Contract steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; proposed; non-authoritative
owning_root: contracts/
responsibility: fixture-only semantic meaning for STAC/DCAT/PROV distribution-carrier alignment candidates
truth_posture: cite-or-abstain
responsibility_root: contracts/
related:
  - contracts/data/catalog_matrix_closure_profile.md
  - contracts/data/catalog_trust_extension.md
  - contracts/release/tile_artifact_manifest.md
  - schemas/contracts/v1/data/catalog_distribution_mapping_profile.schema.json
  - fixtures/contracts/v1/data/catalog_distribution_mapping_profile/
  - tools/validators/catalog_closure/validate_catalog_distribution_mapping_profile.py
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "Additive fixture-only profile; it does not replace the CatalogMatrix closure profile or activate a catalog or registry."
  - "PASS proves bounded field alignment in one synthetic candidate only. It does not resolve evidence, decide policy, approve review, release, publish, or authorize public use."
[/KFM_META_BLOCK_V2] -->

# Catalog Distribution Mapping Profile

> **PROPOSED:** This additive profile makes one bounded Full Atlas and Pass 18
> requirement executable: the STAC asset, DCAT distribution, and PROV entity
> that describe one renderable artifact must agree on its locator, checksum,
> media type, role, and generation identity.

## Compatibility and authority boundary

The existing `CatalogMatrix` closure profile aligns artifact identity, byte
digest, and release reference. This profile does not replace or narrow it. It
applies only to synthetic objects declaring:

```json
{"profile_version":"kfm.catalog-distribution-mapping-candidate.v1"}
```

Objects without that discriminator are outside this validator. Profile
validation does not write STAC, DCAT, or PROV records; contact an artifact
registry; activate OCI or ORAS; resolve evidence; decide policy; approve
review; authorize release; deploy; publish; or authorize public use.

| Responsibility | Owning surface |
|---|---|
| Distribution-mapping meaning | `contracts/data/catalog_distribution_mapping_profile.md` |
| Machine shape | `schemas/contracts/v1/data/catalog_distribution_mapping_profile.schema.json` |
| Synthetic examples | `fixtures/contracts/v1/data/catalog_distribution_mapping_profile/` |
| Local deterministic checks | `tools/validators/catalog_closure/validate_catalog_distribution_mapping_profile.py` |
| Actual catalog records | governed STAC, DCAT, and PROV lifecycle surfaces |
| Evidence, policy, review, release, publication | their separate governing object families |

## Canonical carrier tuple

One candidate binds this tuple:

```text
artifact locator + sha256 digest + media type + distribution role
```

The same values must appear in the standards-facing carrier fields:

| Canonical artifact field | STAC asset | DCAT distribution | PROV entity |
|---|---|---|---|
| `locator` | `href` | `access_url` | `location` |
| `digest` | `checksum` | `checksum` | `checksum` |
| `media_type` | `media_type` | `media_type` | `media_type` |
| `asset_role` | sole `roles` member | `role` | `role` |

The PROV carrier must additionally bind its `generated_entity_ref` to the
declared `entity_ref` and name both a generation activity and an attributed
agent. These fields are compatibility carriers, not replacements for the
native standards. The digest suffix embedded in the synthetic locator must
also equal the artifact `digest`.

## Candidate identity and result

`spec_hash` is the repository canonical hash of every field except
`candidate_id` and `spec_hash`. `candidate_id` is the first 24 lowercase hex
characters of that hash with the prefix `kfm:catalog-distribution-mapping:`.

A conforming candidate returns `PASS` with `profile_state=REVIEW_REQUIRED`.
Any carrier drift returns `DENY`; unsafe or unreadable input returns `ERROR`.
No result grants authority. The profile has no `READY`, `APPROVED`, or
`PUBLISHED` state.

## Synthetic-only locator grammar

Fixtures use `urn:kfm:synthetic:distribution:<slug>@sha256:<digest>`. The
validator never dereferences the URN. This deliberately holds the Atlas OCI
digest-URI proposal at the fixture boundary: registry selection, credentials,
network transport, OCI/ORAS activation, and publication require separate
reviewed work.

## Required fail-closed behavior

The validator denies:

- locator, checksum, media-type, or role drift in any carrier;
- a PROV generated-entity mismatch;
- a false alignment summary;
- non-canonical candidate identity or specification hash;
- unknown fields or any attempted authority escalation; and
- duplicate JSON keys, non-finite numbers, symbolic links, oversized input,
  or malformed JSON.

## Acceptance evidence

This proposed profile is reviewable when its closed Draft 2020-12 schema
meta-validates; exact positive and negative fixtures replay deterministically;
socket creation is denied during focused tests; adjacent catalog-closure tests
remain green; documentation metadata validates; and the generated authoring
receipt binds every introduced byte. Hosted exact-head CI and human review are
still required on the draft pull request.

## Rollback

Revert the additive profile commit. Rollback removes only this contract,
schema, fixtures, validator, tests, workflow, source map, and authoring receipt.
It does not alter existing CatalogMatrix, catalog-trust, release, registry,
artifact, or public-product surfaces.
