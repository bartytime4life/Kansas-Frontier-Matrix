<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-evidence-kfm-geo-manifest
title: KFM Geo Manifest Contract — Evidence
type: semantic-contract; geospatial-artifact-manifest-profile
version: v0.3
status: draft; PROPOSED; fixture-first validator implemented; no-signing; no-release-authority
owners:
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Geospatial / map steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
created: NEEDS VERIFICATION — greenfield scaffold existed before v0.2 expansion
updated: 2026-08-04
policy_label: public; contracts; evidence; geo-manifest; fixture-first; release-gated; rollback-aware; non-authoritative
related:
  - ./README.md
  - ./evidence_ref.md
  - ./evidence_bundle.md
  - ../../schemas/contracts/v1/evidence/kfm_geo_manifest.schema.json
  - ../../fixtures/evidence/kfm_geo_manifest/
  - ../../tools/validators/evidence/validate_kfm_geo_manifest.py
  - ../../tests/validators/test_validate_kfm_geo_manifest.py
  - ../../docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md
  - ../../docs/adr/ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../data/proofs/
  - ../../data/receipts/
  - ../../data/catalog/
  - ../../release/
tags: [kfm, evidence, geo-manifest, pmtiles, cog, geoparquet, geojson, integrity, fixtures, rollback]
notes:
  - "v0.3 implements a bounded fixture-first schema, validator, synthetic corpus, tests, and read-only CI profile."
  - "ADR-0023 remains proposed. This contract revision does not accept signing, create a signature profile, or alter promotion gates."
  - "The validator uses a named profile-local JSON serialization and the repository's current bare sha256 grammar; it does not settle ADR-0013."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM Geo Manifest Contract — Evidence

> `KFMGeoManifest` describes one geospatial artifact candidate well enough to
> bind its bytes, spatial meaning, evidence references, derivation chain,
> rights/sensitivity posture, review references, correction lineage, and
> rollback target. It is metadata about a carrier, not the carrier, evidence
> closure, a policy decision, a release decision, or public truth.

## Status and authority boundary

| Surface | Current posture |
|---|---|
| Semantic contract | `PROPOSED`, v0.3 |
| Machine shape | Closed Draft 2020-12 fixture profile |
| Validator | Deterministic, local, no-network |
| Fixture corpus | Synthetic valid, schema-invalid, semantic-invalid, and byte-mismatch cases |
| Signature / DSSE / cosign | Not implemented or accepted here |
| Evidence resolution | Not performed |
| Policy or review authentication | Not performed |
| Release / publication | Fixed to no authority |

> [!IMPORTANT]
> ADR-0023 remains `proposed`. A merged schema or green validator does not
> accept that ADR, add a new promotion gate, sign an artifact, or authorize a
> PMTiles/COG release.

## Responsibility split

| Object or lane | Responsibility |
|---|---|
| `KFMGeoManifest` | Artifact metadata and internal consistency |
| `SourceArtifact` | Exact captured source bytes and retrieval metadata |
| `EvidenceRef` / `EvidenceBundle` | Claim-scoped evidence pointer and closure |
| `PolicyDecision` | Rights, sensitivity, access, and obligations |
| Review records | Accountable review posture |
| `ReleaseManifest` / `PromotionDecision` | Governed release transition |
| Rollback/correction objects | Reversal, supersession, withdrawal, and correction |
| PMTiles, COG, GeoParquet, GeoJSON bytes | The artifact itself in its governed storage lane |

No object above substitutes for another.

## Fixture-first machine profile

The first executable profile is deliberately narrow. It supports four carrier
families:

- PMTiles;
- Cloud-Optimized GeoTIFF metadata;
- GeoParquet metadata; and
- GeoJSON metadata.

It requires:

- stable manifest identity and semantic version;
- `spec_hash` under the explicit `kfm-fixture-json-v1` profile;
- artifact type, role, media type, byte length, and SHA-256 digest;
- source-artifact references;
- claim, geography, and temporal scope;
- source role and evidence/source-descriptor references;
- CRS, bounding box, geometry type, scale or resolution, and an optional tile profile;
- an ordered transform chain with input/output digests and receipts;
- rights, sensitivity, policy, review, and rollback references;
- non-release governance constants; and
- supersession, correction, and rollback lineage.

The profile fixes:

```text
release_state        = not_released
release_manifest_ref = null
public_use_allowed    = false
authority_created     = false
```

Those constants are trust boundaries, not temporary placeholders.

## Deterministic hash profile

The fixture validator computes `spec_hash` over the complete manifest except the
`spec_hash` field itself, serialized as UTF-8 JSON with sorted keys, ASCII
escaping, finite numbers, and compact separators. The value uses the repository's
currently implemented `sha256:<64-lower-hex>` grammar.

This is a **profile-local reproducibility rule** named
`kfm-fixture-json-v1`. It does not claim RFC 8785/JCS parity, establish a
cross-runtime canonicalization standard, or settle proposed ADR-0013. A later
accepted hash-policy migration must update schema, contract, fixtures, validator,
producers, consumers, receipts, and compatibility tests together.

Manifest `id` is stable but not content-derived in this profile. It is included
in the `spec_hash` projection, so changing identity changes the hash.

## Semantic invariants

The validator checks:

1. all identity-bearing digests are non-placeholder SHA-256 values;
2. `spec_hash` matches the declared profile projection;
3. artifact type and media type agree;
4. bounding boxes are ordered and EPSG:4326 ranges are valid;
5. PMTiles declares a consistent XYZ tile/zoom profile and non-tile artifacts do not;
6. transform IDs are unique, transform digests form a continuous chain, and the final output equals the artifact digest;
7. generalized or redacted sensitivity has the matching receipted transform;
8. public-bound candidates have verified-open rights, a public-safe sensitivity state, policy/review references, and a rollback target;
9. rollback-target and supersession lineage is coherent and non-self-referential;
10. temporal scope is ordered and reference arrays are canonical; and
11. optional local payload bytes match declared digest and byte length.

The parser also rejects duplicate JSON keys, non-finite numbers, excessive
nesting, oversized files, symlinks, FIFOs, and other non-regular inputs.
Diagnostics expose stable finding codes and JSON pointers, not candidate values.

## What validation proves

A passing result proves only the configured metadata shape and local consistency.
When a local payload is supplied, it also proves that those exact bytes match the
declared length and SHA-256 digest.

It does **not** prove:

- that the bytes conform to PMTiles, COG, GeoParquet, or GeoJSON specifications;
- that referenced sources, EvidenceRefs, EvidenceBundles, policies, reviews, or rollback records exist;
- that rights, sensitivity, or public safety were independently evaluated;
- that a signer, trust root, transparency log, or revocation system exists;
- that a candidate passed promotion gates; or
- that anything is released, deployed, published, or allowed for public use.

## Fixture corpus

The corpus contains:

- three valid metadata/payload cases;
- four closed-schema failures; and
- eleven schema-valid semantic or byte-binding failures.

The synthetic payloads intentionally are not real production geospatial files.
Format conformance is a separate future validator family.

## Validation

```bash
KFM_NO_NETWORK=1 python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_kfm_geo_manifest.py' \
  --verbose

KFM_NO_NETWORK=1 python tools/validators/evidence/validate_kfm_geo_manifest.py --fixtures
```

The dedicated workflow is read-only and emits logs and summaries only.

## Graduation path

A later change may add format-specific parsers, accepted hash-policy migration,
cryptographic envelopes, policy evaluation, catalog/release integration, or
viewer verification only after their governing decisions and responsibility
boundaries are accepted. Those are separate review surfaces; none is implied by
this fixture profile.

## Rollback

Before merge, close the draft pull request and delete its feature branch. After
merge, revert the contract/schema/fixture/validator/test/workflow slice together.
If manifest IDs are later referenced by other records, preserve the historical
records and use correction or supersession rather than deleting relied-on
process memory.

[Back to top](#top)
