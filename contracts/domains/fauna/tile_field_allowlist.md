<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/fauna/tile-field-allowlist
title: Fauna Tile Field Allowlist Fixture Profile
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Fauna steward · Map/UI steward · Policy steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; fauna; vector-tile; field-allowlist; public-safety
responsibility: Define fixture-only semantics for comparing one public Fauna vector-tile property set with its LayerManifest allowlist and an inactive domain policy profile without inspecting tile bytes or granting release authority.
truth_posture: "CONFIRMED supplied-card traceability and current placeholder gap; PROPOSED inactive fixture profile; UNKNOWN production field set and build integration; NEEDS VERIFICATION human review and hosted CI"
related:
  - ../../../docs/domains/fauna/MAP_UI_CONTRACTS.md
  - ../../data/layer_manifest.md
  - ../../../schemas/contracts/v1/domains/fauna/tile_field_allowlist.schema.json
  - ../../../policy/domains/fauna/tile_field_allowlist.yaml
  - ../../../fixtures/domains/fauna/layers/tile_field_allowlist_cases.json
  - ../../../tools/validators/domains/fauna/tiles/validate_tile_field_allowlist.py
  - ../../../tests/domains/fauna/test_tile_field_allowlist.py
  - ../../../docs/intake/exploratory/pass-18-vector-tile-field-allowlist-source-map.md
[/KFM_META_BLOCK_V2] -->

# Fauna Tile Field Allowlist Fixture Profile

This contract implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-400`: public vector-tile candidates should encode only explicitly approved properties.

The profile is `PROPOSED_INACTIVE_FIXTURE_ONLY`. It compares synthetic property names for a Fauna `PMTILES`, `MVT`, or `MLT` candidate against both:

1. the candidate layer's declared `public_field_allowlist`; and
2. an inactive Fauna policy profile.

It requires the fixture fields `feature_id` and `evidence_ref` so the test surface preserves a bounded click-to-evidence path. The remaining names are review candidates only. Nothing in this packet approves a production property set.

## Boundary

A validator `PASS` means only that a synthetic field-name fixture is locally coherent with the inactive profile: required names are present, encoded names are declared by the candidate `LayerManifest`, manifest names are policy-allowlisted, deny patterns are absent, arrays are canonical, and renderer styling is not claimed as the safety control.

The validator does **not**:

- read, decode, build, optimize, sign, or publish PMTiles, MVT, or MLT bytes;
- inspect geometry, feature values, tile size, zoom behavior, accessibility, or Evidence Drawer resolution;
- prove that a `LayerManifest`, `TileArtifactManifest`, evidence object, policy decision, review record, release manifest, or rollback target exists;
- approve sensitive-species handling, a production field name, or a public layer; or
- promote lifecycle state, release, deploy, publish, or authorize public use.

## Profile responsibilities

| Field | Meaning |
|---|---|
| `applies_to` | Closed fixture scope: Fauna, public candidates, encoded properties only, and the three named vector formats. |
| `required_public_fields` | Synthetic minimum for stable feature selection and click-to-evidence linkage. |
| `allowed_public_fields` | Candidate names that the fixture validator may accept; not a production approval. |
| `forbidden_exact_fields` | Explicit names that must not appear in an encoded or manifest field set. |
| `forbidden_field_patterns` | Name-only patterns for precise location, identity, internal-state, credential, and reverse-engineering clues. |
| `candidate_requirements` | Fail-closed comparison rules between encoded fields, the manifest allowlist, and policy. |
| `authority_claims` | Evidence, policy-decision, review, promotion, release, publication, and public-use authority fixed to `false`. |

The profile examines field **names only**. It deliberately stores no real coordinates, identities, credentials, source records, sensitive taxa, or tile payloads.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The policy shape and one synthetic candidate's field-name relations satisfy this closed fixture profile. |
| `DENY` | A field, manifest, style-only, canonicalization, or non-authority invariant fails. |
| `ERROR` | Policy or fixture input cannot be evaluated safely. |

These outcomes are validator results only. They are not evidence, policy decisions, review decisions, release states, or runtime answers.

## Directory Rules basis

Accepted Directory Rules place semantic meaning under `contracts/`, machine shape under `schemas/`, normative decision rules under `policy/`, repository validation under `tools/`, reusable synthetic inputs under `fixtures/`, executable conformance under `tests/`, CI orchestration under `.github/`, and source reconciliation under `docs/intake/exploratory/`.

The profile composes the existing `LayerManifest.exposure.public_field_allowlist` by name. It does not modify that schema or create a parallel layer, tile, evidence, policy-decision, release, or publication home.

## Validation

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest discover \
  --start-directory tests/domains/fauna \
  --pattern 'test_tile_field_allowlist.py' \
  --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/domains/fauna/tiles/validate_tile_field_allowlist.py \
  --fixtures
```

## Activation and rollback

Production activation remains `HOLD` until stewards approve the production field vocabulary, bind it to real manifest and build inputs, define accessibility and Evidence Drawer obligations, inspect actual tile properties, and add release/correction/rollback integration.

Rollback is a single additive revert. This fixture packet has no runtime consumer and mutates no tile, layer, source, evidence, policy decision, lifecycle state, release, cache, route, deployment, or public artifact.
