<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/pmtiles/flora/readme
name: Flora PMTiles Published README
path: data/published/pmtiles/flora/README.md
type: data-lane-readme
version: v0.1.0
status: draft
owners:
  - <flora-domain-steward>
  - <map-layer-steward>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: public-review
truth_posture: cite-or-abstain
lifecycle_phase: published
responsibility_root: data/
domain: flora
artifact_family: released-public-safe-flora-pmtiles
format: PMTiles
notes:
  - "This README documents the PMTiles-format published lane for Flora delivery artifacts."
  - "PMTiles are downstream delivery carriers and are not source, proof, catalog, release, policy, or AI authority."
  - "Payload presence, release approval, validators, and CI enforcement remain UNKNOWN until verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora PMTiles Published Artifacts

Released public-safe Flora PMTiles artifacts for governed map delivery.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: published" src="https://img.shields.io/badge/lifecycle-published-success">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-2e7d32">
  <img alt="Format: PMTiles" src="https://img.shields.io/badge/format-PMTiles-6e40c9">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

## Scope

This directory may hold released public-safe Flora PMTiles artifacts after KFM release gates have passed.

PMTiles here are downstream delivery files. Claim truth remains in source records, processed objects, catalog and EvidenceBundle records, proofs, receipts, policy decisions, review records, and release manifests.

## Repo fit

| Field | Value |
|---|---|
| Path | `data/published/pmtiles/flora/` |
| Responsibility root | `data/` |
| Lifecycle phase | `published/` |
| Domain lane | `flora` |
| Format lane | `pmtiles` |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/` and `data/receipts/`, not this directory |
| Default failure posture | `DENY`, `HOLD`, `RESTRICT`, or `ABSTAIN` when evidence, policy, release, digest, or rollback support is insufficient |

## Inputs

Accepted content is limited to release-approved PMTiles artifacts and immediate sidecars:

- `.pmtiles` files generated from release-approved Flora layer material;
- TileJSON-compatible sidecars, field allowlists, and layer manifests;
- digest files that bind tile bytes to release state;
- release-local README files;
- `latest.json` pointers only when generated from release state.

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Source material | `data/raw/flora/` |
| Work files or candidates | `data/work/flora/` |
| Held material | `data/quarantine/flora/` |
| Canonical processed objects | `data/processed/flora/` |
| Catalog records or EvidenceBundle state | `data/catalog/` or proof lanes |
| Proofs and receipts | `data/proofs/` and `data/receipts/` |
| Release decisions | `release/` |
| Contracts, schemas, or policy rules | `contracts/`, `schemas/`, `policy/` |
| Non-PMTiles formats | Appropriate published layer, domain, or API-payload lane |
| Generated claims without citation support | Governed answer/provenance paths only |

## Directory map

```text
data/published/pmtiles/flora/
├── README.md
├── <release_id>/
│   ├── flora.<layer_slug>.pmtiles
│   ├── flora.<layer_slug>.pmtiles.sha256
│   ├── layer.manifest.json
│   ├── tilejson.json
│   ├── fields.allowlist.json
│   ├── caveats.summary.json
│   ├── review.summary.json
│   └── README.md
└── latest.json
```

`latest.json` must be generated from release state.

## Required checks before use

- [ ] Confirm release manifest and promotion decision.
- [ ] Confirm proof, receipt, and catalog closure.
- [ ] Confirm source descriptors, source roles, rights posture, and current terms.
- [ ] Confirm field allowlist, layer manifest, TileJSON sidecar, and released-byte digest.
- [ ] Confirm rollback target and correction path.
- [ ] Confirm public clients consume tiles through governed APIs or release-resolved paths.

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested PMTiles path boundary. | **CONFIRMED authored** |
| The target path exists in the live repository. | **CONFIRMED by GitHub contents API during this edit** |
| Actual Flora PMTiles payloads exist in this subtree. | **UNKNOWN** |
| Release manifests approve Flora PMTiles artifacts in this subtree. | **UNKNOWN** |
| Validators and CI checks enforce this exact PMTiles lane. | **NEEDS VERIFICATION** |
| This README is release authority. | **DENY** |

## Related files

- [`../../README.md`](../../README.md)
- [`../README.md`](../README.md)
- [`../../layers/flora/README.md`](../../layers/flora/README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../../docs/domains/flora/ARCHITECTURE.md`](../../../../docs/domains/flora/ARCHITECTURE.md)
- [`../../../../docs/domains/flora/API_CONTRACTS.md`](../../../../docs/domains/flora/API_CONTRACTS.md)
- [`../../../../docs/domains/flora/RELEASE_INDEX.md`](../../../../docs/domains/flora/RELEASE_INDEX.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a released public-safe Flora PMTiles delivery lane only. It is not source authority, proof authority, receipt authority, release authority, catalog authority, registry authority, policy authority, or AI truth.

[Back to top](#top)
