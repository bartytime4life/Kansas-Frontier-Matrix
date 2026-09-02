<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/environmental-indicator-evidence-bundle-profile
title: Environmental Indicator EvidenceBundle Profile
type: semantic-contract
version: v0.1.0
status: draft; PROPOSED; fixture-first; no-network; non-operational
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; evidence; environmental-indicator; fixture-only; no-authority
owning_root: contracts/
responsibility: Define the semantic boundary for binding a derived environmental indicator to the existing EvidenceBundle contract without creating evidence, policy, release, or publication authority.
truth_posture: "CONFIRMED source and repository evidence; PROPOSED profile; UNKNOWN operational state; NEEDS VERIFICATION human review"
related:
  - ./evidence_bundle.md
  - ../../schemas/contracts/v1/evidence/environmental_indicator_evidence_bundle_profile.schema.json
  - ../../fixtures/contracts/v1/evidence/environmental_indicator_evidence_bundle_profile/cases.json
  - ../../tools/validators/validate_environmental_indicator_evidence_bundle_profile.py
  - ../../tests/validators/test_validate_environmental_indicator_evidence_bundle_profile.py
  - ../../docs/intake/exploratory/pass-32-environmental-indicator-evidence-bundle-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, evidence, evidence-bundle, environmental-indicator, derived-analysis, deterministic, fixture-first]
notes:
  - "Adapts Pass 32 cards KFM-P32-IDEA-0013 and KFM-P32-PROG-0007 as a bounded profile over the existing EvidenceBundle object family."
  - "The Pass 32 atlas remains a downstream carrier and does not become repository authority through this contract."
  - "A passing profile establishes local synthetic consistency only and creates no source, observation, policy, review, lifecycle, release, publication, or public-use authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Environmental Indicator EvidenceBundle Profile

> A closed, fixture-only profile for binding one derived environmental indicator to the existing KFM `EvidenceBundle` contract while preserving source-role, evidence-reference, deterministic-identity, no-data, and no-authority boundaries.

## Status and authority boundary

| Field | Value |
|---|---|
| Contract state | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY` |
| Owning semantic lane | `contracts/evidence/` |
| Base object | Existing `EvidenceBundle` |
| Machine profile | `schemas/contracts/v1/evidence/environmental_indicator_evidence_bundle_profile.schema.json` |
| Source activation, evidence resolution, policy, review, lifecycle, release, publication | Not performed or authorized |

The profile does **not** create a second canonical EvidenceBundle schema. The root document carries an unchanged, schema-validated `bundle` member and a separate `environmental_indicator` member whose additional deterministic and closure rules are enforced by the focused validator.

A `PASS` result means only that the synthetic profile satisfies the reviewed schema and semantic checks. It does not prove that any referenced source, STAC asset, ETag, threshold, county result, cluster, citation, license, sensitivity label, or EvidenceBundle exists outside the fixture.

## Source adaptation

Pass 32 proposes:

- EvidenceBundle sidecars for derived environmental indicators with asset references, ETag information, thresholds, cluster summaries, and `spec_hash`; and
- a machine profile requiring `evidence_refs`, method, window length, thresholds, county FIPS values, ranked rows, cluster summaries, `computed_at`, and deterministic identity.

This contract adapts those ideas by:

1. storing **opaque asset references** rather than source payloads;
2. storing **SHA-256 digests of ETags**, never raw ETag values;
3. fixing `source_role` to `derived_analysis`;
4. embedding the current global `EvidenceBundle` rather than duplicating it;
5. requiring explicit `POPULATED`, `EMPTY`, or `NO_DATA` semantics;
6. binding row and cluster support to exact `EvidenceRef.ref` values in the embedded bundle; and
7. keeping every authority-bearing claim false.

The source cards are design inputs. They do not prove implementation or authorize live environmental computation.

## Directory Rules basis

Accepted ADR-0029 makes Directory Rules v2 the current placement authority. This slice uses existing responsibility roots:

| Responsibility | Home |
|---|---|
| Human-readable semantic meaning | `contracts/evidence/` |
| Machine shape | `schemas/contracts/v1/evidence/` |
| Synthetic examples | `fixtures/contracts/v1/evidence/` |
| Reusable validation | `tools/validators/` |
| Enforceability proof | `tests/validators/` |
| Hosted orchestration | `.github/workflows/` |
| Exploratory source adaptation | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No root, parallel EvidenceBundle authority, policy home, source registry, lifecycle store, catalog, proof lane, release lane, API, UI route, or public artifact is created.

## Profile shape

```text
EnvironmentalIndicatorEvidenceBundleProfile
├── profile / status / execution_mode
├── analysis_id
├── bundle                         existing global EvidenceBundle
├── environmental_indicator
│   ├── source
│   │   ├── source_descriptor_ref
│   │   ├── asset_refs
│   │   ├── etag_digests
│   │   ├── source_time
│   │   └── retrieved_at
│   ├── source_role                derived_analysis
│   ├── method
│   ├── window_days
│   ├── threshold_profile
│   ├── thresholds
│   ├── county_fips
│   ├── ranked_rows
│   ├── cluster_summary
│   ├── data_state
│   ├── computed_at
│   └── spec_hash
└── claims                         explicit no-authority flags
```

### EvidenceBundle reuse

The embedded `bundle` remains governed by `schemas/contracts/v1/evidence/evidence_bundle.schema.json`. This profile adds only cross-object bindings:

- each row and cluster evidence identifier must resolve to an exact `bundle.evidence_refs[].ref`;
- `bundle.source_records` must name the indicator's `source_descriptor_ref`;
- `bundle.checksums.environmental_indicator_profile` must equal the indicator `spec_hash`;
- `bundle.claim_scope` must bind the deterministic `analysis_id`; and
- the bundle's own `spec_hash` must recompute over the bundle excluding `/spec_hash`.

These are local reference-closure checks. They do not resolve an `EvidenceRef` to an external or authoritative `EvidenceBundle`.

## Deterministic identity

The repository hashing package supplies RFC 8785 JCS plus SHA-256.

1. `threshold_profile.spec_hash` covers the threshold profile excluding its `spec_hash`.
2. `environmental_indicator.spec_hash` covers the indicator excluding its `spec_hash`.
3. `analysis_id` is `kfm:environmental-indicator:` plus the full indicator hash.
4. `bundle.checksums.environmental_indicator_profile` equals the indicator hash.
5. `bundle.spec_hash` covers the embedded bundle excluding its `spec_hash`.

Arrays whose order affects the hash have an explicit deterministic rule:

- thresholds sort by `threshold_id`;
- county FIPS values sort ascending;
- ranked rows are contiguous from rank `1`;
- clusters sort by `cluster_id`;
- evidence identifiers, source records, and citations sort lexically.

## Source and ETag boundary

`asset_refs` may contain only opaque `stac://`, `kfm://artifact/`, or `artifact:` references. The profile does not admit URLs, credentials, query strings, source payloads, geometries, coordinates, or raw ETag strings.

Each asset reference has one corresponding `etag_digest`. Digest cardinality must match asset cardinality. The digests show only that an upstream process supplied a bounded identity token; this validator neither performs a HEAD request nor authenticates the token.

## Data-state semantics

| State | Required content |
|---|---|
| `POPULATED` | Non-empty county list, complete ranked rows, and non-overlapping clusters covering the same county set. |
| `EMPTY` | Empty county, row, and cluster collections; an executed method found no qualifying results. |
| `NO_DATA` | Empty county, row, and cluster collections; required input support was unavailable. |

Missing data is never represented as a zero environmental condition. `EMPTY` and `NO_DATA` remain distinct.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Schema, deterministic hashes, identity, ordering, temporal order, source binding, reference closure, and data-state consistency pass for the local fixture. |
| `DENY` | Candidate shape or semantics fail closed with stable finding codes and JSON Pointer paths. |
| `ERROR` | The input or schema could not be read or evaluated safely. |

Diagnostics expose codes and paths, not source values.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_environmental_indicator_evidence_bundle_profile.py' \
  --verbose

KFM_NO_NETWORK=1 \
python tools/validators/validate_environmental_indicator_evidence_bundle_profile.py \
  --fixtures
```

The reviewed fixture matrix contains three positive states and eleven negative cases. Tests also cover duplicate keys, non-finite numbers, oversized inputs, symbolic links, finite CLI exit codes, deterministic diagnostics, and a patched network boundary.

## Explicit non-goals

This profile does not:

- fetch STAC or environmental source data;
- compute NDVI, air quality, hydrology, soil, or other indicators;
- claim observation or regulatory authority;
- authenticate a source, ETag, citation, license, sensitivity decision, or reviewer;
- resolve evidence outside the local candidate;
- evaluate policy or consent;
- create RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED state;
- create a policy decision, proof, promotion record, release manifest, correction notice, or rollback card;
- add an API, MapLibre layer, Evidence Drawer panel, Focus Mode answer, export, deployment, or public product.

## Compatibility and follow-up boundaries

Separate, independently reviewed work would be required for:

1. an actual environmental computation contract such as county NDVI delta;
2. an admitted source descriptor and source-rights decision;
3. STAC asset and ETag resolver behavior;
4. OPA policy input and promotion gates for derived indicators;
5. a registry and supersession model for admitted bundles;
6. public-safe layer, API, and Evidence Drawer projections; and
7. correction, withdrawal, and release integration.

Those capabilities must not be activated by editing this fixture profile in place.

## Rollback

Before merge, close the draft pull request and delete its feature branch. After an authorized merge, revert the bounded feature commit or merge commit. The rollback removes only the profile contract, schema, fixtures, validator, tests, workflow, source map, and generated receipt. No live source, lifecycle record, policy decision, evidence object, release, deployment, or public artifact requires restoration.

<p align="right"><a href="#top">Back to top</a></p>
