# CorridorRoute Fixture-Only Schema Profile

## Status

**PROPOSED implementation profile.** This slice adds no live source, route geometry, policy approval, release, publication, API, map layer, or routing authority.

## Goal

Close the concrete `CorridorRoute` machine-shape gap with a small, deterministic, no-network validation slice. The attached **New Ideas 3-31-26.pdf** historical-routes section recommends a minimum route entity contract with stable identity, approximate dates, temporal uncertainty, geometry accuracy, source URI and license, evidence references, confidence, authoritative-versus-derived status, and change state. It also recommends fail-closed gates for evidence references, source resolution or quarantine, temporal uncertainty, and explicit representation role.

The current semantic contract adds KFM-specific boundaries: a route is not a segment; segment membership is a separate source- and time-scoped assertion; geometry is derivative; historic claims retain uncertainty; and live/legal routing or publication authority is denied by default.

## Responsibility-root placement

| Artifact | Path | Owner |
|---|---|---|
| Machine shape | `schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json` | `schemas/` |
| Validator code | `tools/validators/domains/roads-rail-trade/validate_corridor_route.py` | `tools/` |
| Synthetic fixtures | `fixtures/domains/roads-rail-trade/corridor_route/` | `fixtures/` |
| Behavior tests | `tests/schemas/test_corridor_route_contract.py` | `tests/` |
| Implementation receipt fixture | `fixtures/generated_receipt/corridor_route_anti_collapse_receipt.json` | existing generated-receipt fixture lane |

Directory Rules basis: the domain remains a lane inside established responsibility roots. This change creates no new root and no parallel schema, contract, policy, source, registry, proof, release, or publication authority.

## Enforced boundaries

- `CorridorRoute` is discriminated by `object_type` and `feature_class=route`.
- Embedded `segments`, `segment_ids`, and `geometry` are forbidden.
- `membership_refs` may point to separate RouteMembership objects; they do not embed membership truth.
- Approximate dates, `date_uncertainty`, `geometry_accuracy`, source role, source URI, license, evidence resolution, confidence, representation layer, and change state are required.
- The top-level `spec_hash` is verified as SHA-256 over canonical JSON excluding only fixture metadata and the hash field itself.
- Unresolved source, evidence, geometry, or rights returns `ABSTAIN` for non-released candidates.
- Sensitive or restricted route geometry marked for generalized public use returns `DENY`.
- `authoritative` representation requires an authority or official source and cannot use `derived-geocode` geometry.
- Released posture requires bound source/evidence, public-safe rights/sensitivity, policy decision, review, release manifest, and rollback references.
- The validator emits only `PASS`, `ABSTAIN`, `DENY`, or `ERROR` and never promotes lifecycle state.

## Validation

```bash
KFM_NO_NETWORK=1 PYTHONHASHSEED=0 TZ=UTC \
  python tools/validators/domains/roads-rail-trade/validate_corridor_route.py --fixtures

KFM_NO_NETWORK=1 PYTHONHASHSEED=0 TZ=UTC \
  python -m pytest -q tests/schemas/test_corridor_route_contract.py
```

The repository-wide regression command remains:

```bash
make test
```

## Rollback

Revert the pull request, or revert its commits in reverse order if it is not squashed. The slice is additive and fixture-only; rollback removes the schema, validator, fixtures, focused tests, profile, and receipt without moving or rewriting existing authority files.

## Deliberate follow-up

STAC collection/item emission, public-safe GeoJSON, PMTiles preview, source onboarding, policy evaluation, EvidenceBundle resolution, review records, release manifests, MapLibre integration, and correction propagation remain separate governed slices.
