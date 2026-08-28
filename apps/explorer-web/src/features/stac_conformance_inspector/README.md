<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://apps/explorer-web/features/stac-conformance-inspector
title: STAC Conformance Inspector
type: feature-readme
version: v0.1.0
status: proposed; fixture-backed; read-only
owner: OWNER_TBD - Explorer, catalog, and STAC stewards
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; public-safe-projection; no-network
owning_root: apps/
responsibility: bounded read-only presentation of a closed STAC conformance summary
truth_posture: PROPOSED fixture-backed UI; production wiring and hosted exact-head results need verification
related:
  - ../../adapters/StacConformanceInspectorProjection.ts
  - ../../../../../schemas/contracts/v1/stac/kfm-profile-v1.schema.json
  - ../../../../../tools/validators/stac/validate_kfm_profile_v1.py
  - ../../../../../fixtures/ui/stac_conformance_inspector_projection/README.md
  - ../../../../../docs/intake/exploratory/pass-31-stac-conformance-inspector-source-map.md
[/KFM_META_BLOCK_V2] -->

# STAC conformance inspector

Status: **fixture-first Explorer component; not production-wired**.

This feature adapts Pass 31 card `KFM-P31-FEAT-0004` into a read-only
maintainer surface for a precomputed STAC conformance summary. It can show
conformance classes, KFM extension use, item identity rules, declared asset
MIME types, and collection-contract completeness.

## Projection boundary

The app-local profile
`kfm.explorer.stac-conformance-inspector.public-safe.v1` accepts only:

- finite available, abstain, deny, and error outcomes with paired reasons;
- canonical whole-second UTC timestamps and SHA-256-bound inspection IDs;
- STAC `1.0.0` and KFM profile `1.0.0-draft.1` declarations;
- finite conformant, non-conformant, and incomplete states;
- canonical, unique conformance-class, identity-rule, and MIME arrays;
- one finite KFM trust-extension-use declaration;
- one opaque collection reference and bounded completeness counts;
- sorted, unique finding-code arrays; and
- eight fixed-false governance flags.

Only `AVAILABLE / INSPECTION_AVAILABLE` may carry inspection detail. Other
outcomes require null metadata and empty arrays. The declared inspection state
must agree with check and collection findings. Unknown fields, identity drift,
array-order drift, contradictory counts, unsafe governance, or state
contradictions fail closed to fixed error copy without reflecting input detail.

## Authority boundary

The inspector consumes only a closed display projection. It does not query a
STAC API or catalog, read or validate catalog bytes, resolve item or asset
references, mutate a collection, admit a source, create evidence authority,
evaluate policy, approve review, promote, release, deploy, publish, or
authorize public use.

The surface exposes no button, link, callback, transport client, persistence
store, or mutation seam. Displayed findings are not a validator receipt and do
not prove external catalog conformance, source validity, evidence acceptance,
policy approval, release eligibility, publication, or fitness for public use.

## Placement

- `apps/explorer-web/src/adapters/` owns strict app-local parsing.
- `apps/explorer-web/src/features/stac_conformance_inspector/` owns fixed
  display behavior.
- `fixtures/ui/stac_conformance_inspector_projection/` owns synthetic examples.
- `apps/explorer-web/tests/` owns unit and browser proof.

These are existing responsibility roots under accepted ADR-0029 and Directory
Rules v2. No parallel STAC profile, catalog, validator, evidence, policy,
lifecycle, receipt, release, deployment, or publication authority is created.

## Existing contract relationship

`schemas/contracts/v1/stac/kfm-profile-v1.schema.json`, its deterministic
validator, fixtures, tests, and workflow already own the repository's STAC
profile meaning. This component neither replaces those controls nor reads the
contract or catalog directly. A future governed producer must emit the exact
public-safe projection accepted here.

## Production hold

Production wiring remains **HOLD** until catalog, STAC, policy, security, UI,
and release stewards accept a projection producer and authenticated
maintainer-only delivery route.

## Validation

The existing `ui-build` workflow runs the Explorer build, unit suite, and
headless-browser suite. Focused commands are:

```text
pnpm --filter explorer-web exec vitest run tests/stac-conformance-inspector.test.ts
pnpm --filter explorer-web exec playwright test --config=playwright.config.ts tests/browser/stac-conformance-inspector.spec.ts
pnpm --filter explorer-web build
```

The existing STAC profile validator remains the semantic contract gate:

```text
python tools/validators/stac/validate_kfm_profile_v1.py \
  --schema schemas/contracts/v1/stac/kfm-profile-v1.schema.json \
  --fixtures fixtures/contracts/v1/stac/kfm-profile-v1/valid \
  --negative-fixtures fixtures/contracts/v1/stac/kfm-profile-v1/invalid
```

## Rollback

Revert the adapter, feature, fixtures, tests, source map, and authoring receipt
together. This additive, unmounted surface creates no catalog, source,
evidence, policy, lifecycle, review, release, deployment, publication, or
public-use state to restore.
