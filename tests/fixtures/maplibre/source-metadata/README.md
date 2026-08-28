<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/maplibre/source-metadata-projection/v1
title: MapLibre source-metadata projection fixtures
type: fixture-readme; no-network-conformance-profile
version: v0.1.0
status: proposed; synthetic; no-network; non-authoritative
owners: OWNER_TBD — MapLibre steward · Fixture steward · Validation steward · Release steward
created: 2026-08-04
updated: 2026-08-04
policy_label: public; synthetic-only; renderer-projection; no-release-authority
related:
  - ../README.md
  - ../../../maplibre/test_source_metadata.py
  - ../../../../tools/validators/maplibre/validate_source_metadata.py
  - ../../../../docs/intake/exploratory/new-ideas-4-15-source-map.md
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, maplibre, source-metadata, epoch, license, sha256, manifest, proof-ref, fixtures, no-network]
notes:
  - "The `meta` object is a renderer projection of governed state, not a source, evidence, rights, policy, review, release, or publication authority."
  - "The local manifest shape is a validator fixture profile only; it does not create a second KFM release-manifest schema or registry."
[/KFM_META_BLOCK_V2] -->

# MapLibre source-metadata projection fixtures

Synthetic, no-network fixtures for the bounded validator at
`tools/validators/maplibre/validate_source_metadata.py`.

The fixture profile implements the narrow proposal in *New Ideas 4-15-26* pages
229–263: a MapLibre source may project an `epoch`, `license`, SHA-256 `digest`,
and optional `proof_ref` and `manifest_ref` into its `meta` object so a client can
reason about temporal source selection and compare the projected digest with a
local manifest. The repository source map classifies that proposal as
**corroborative**, so this slice deliberately validates a projection instead of
creating another source-metadata, evidence, or release authority.

> [!IMPORTANT]
> Passing these fixtures proves only local syntax, finite outcome behavior, and
> equality between two declared digest strings. It does not verify remote bytes,
> resolve references, clear a license, create an EvidenceBundle, pass policy,
> complete review, authorize release, or publish a map.

## Inventory

```text
tests/fixtures/maplibre/source-metadata/
├── README.md
├── cases.json
├── valid/
│   ├── manifest.single-source.match.json
│   └── style.single-source.valid.json
├── invalid/
│   ├── manifest.single-source.mismatch.json
│   ├── style.digest-mismatch.json
│   ├── style.invalid-epoch.json
│   ├── style.missing-digest.json
│   ├── style.missing-manifest-ref.required.json
│   ├── style.missing-meta.json
│   └── style.missing-proof-ref.required.json
└── edge/
    ├── manifest.source-unmapped.json
    └── style.manifest-supplied-source-unmapped.json
```

`cases.json` is executable test inventory. It binds each fixture pair to exact
expected outcomes and reason-code sets without copying validator logic into the
fixture lane.

## Finite outcomes

| Outcome | Fixture meaning |
|---|---|
| `ALLOW` | Required projection fields are syntactically bounded and the supplied manifest digest matches. |
| `ABSTAIN` | A supplied manifest does not map the selected style source, so integrity cannot be concluded. |
| `DENY` | Required metadata is missing/invalid or declared digests conflict. |
| `ERROR` | The validator cannot safely parse or inspect an input. |

These are validator outcomes. `ALLOW` is not a `PolicyDecision`,
`PromotionDecision`, `ReleaseManifest`, or publication approval.

## Projection fields

| Field | Local check | Explicit limit |
|---|---|---|
| `epoch` | ISO date, timezone-aware ISO timestamp, ordered ISO interval, or quarter ID in strict mode | Does not prove dataset validity or freshness. |
| `license` | Bounded SPDX-like token or HTTPS reference | Does not evaluate rights or permitted use. |
| `digest` | Non-placeholder lowercase SHA-256 syntax | Does not hash remote source bytes. |
| `proof_ref` | Bounded `kfm://` or HTTPS reference syntax when present/required | Does not resolve or authenticate a proof. |
| `manifest_ref` | Bounded `kfm://` or HTTPS reference syntax when present/required | Does not resolve or authenticate a release manifest. |
| `freshness` | Optional bounded client hint | Does not establish source currentness. |

The companion fixture manifest contains only a `source_digests` projection for
no-network equality checks. Canonical release, map, layer, evidence, receipt, and
proof schemas remain in their owning roots.

## Commands

```bash
python tools/validators/maplibre/validate_source_metadata.py --fixtures

python tools/validators/maplibre/validate_source_metadata.py \
  tests/fixtures/maplibre/source-metadata/valid/style.single-source.valid.json \
  --manifest tests/fixtures/maplibre/source-metadata/valid/manifest.single-source.match.json \
  --require-proof \
  --require-manifest-ref \
  --strict-epoch

python -m unittest discover \
  --start-directory tests/maplibre \
  --pattern 'test_source_metadata.py' \
  --verbose
```

The validator reads local regular files only. It performs no URL fetch, source
activation, credential use, lifecycle write, receipt/proof emission, release, or
publication action.

## Directory Rules basis

- `tests/fixtures/` owns deterministic test inputs.
- `tests/maplibre/` owns renderer-boundary enforceability tests at the current
  repository placement.
- `tools/validators/maplibre/` owns reusable MapLibre-facing validation logic.
- Canonical source identity, evidence, policy, release, and published artifacts
  remain in their separate responsibility roots.

No new root or parallel schema, contract, source registry, proof, receipt,
release, or publication home is introduced.

## Maintenance rules

- Keep every example synthetic, public-safe, deterministic, and no-network.
- Add a `cases.json` expectation whenever a fixture is added.
- Do not place real URLs containing credentials, source responses, production
  digests, private identifiers, sensitive geometry, or release records here.
- Preserve exact `ALLOW`, `ABSTAIN`, `DENY`, and `ERROR` semantics.
- Treat new metadata meaning as contract/schema/policy work in the owning roots,
  not as an informal validator expansion.

## Rollback

Before merge, abandon the feature branch or close the draft pull request. After
an authorized merge, revert the validator, fixture, test, workflow, and
provenance slice together. No source, release, or public artifact requires
restoration because this profile performs no live or lifecycle writes.
