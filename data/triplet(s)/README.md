<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/triplet-s-compatibility/readme
name: Triplet(s) Data Compatibility README
path: data/triplet(s)/README.md
type: data-compatibility-lane-readme
version: v0.1.0
status: draft
owners:
  - <data-steward>
  - <graph-steward>
  - <catalog-steward>
  - <directory-rules-steward>
  - <docs-steward>
created: 2026-06-29
updated: 2026-06-29
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: compatibility-marker-and-redirect
compatibility_class: transitional
authority_posture: compatibility-lane; not-canonical-lifecycle-lane; not-triplet-authority; not-graph-authority; not-source-data; not-processed-data; not-catalog; not-proof; not-receipt; not-published; not-release-authority; not-policy-authority; not-schema-authority; not-public-api-ui-source
path_posture: existing-empty-file-replaced; literal-parentheses-path-present; canonical-plural-triplets-lane-confirmed; directory-rules-lists-data-triplets-not-data-triplet-s; deny-new-payloads
sensitivity_posture: no-public-path; deny-new-payloads-by-default; graph-derived-not-truth; relationship-projection-not-evidence; source-role-preserving; evidence-aware; policy-aware; release-aware
related:
  - ../README.md
  - ../triplets/README.md
  - ../catalog/README.md
  - ../proofs/README.md
  - ../receipts/README.md
  - ../published/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../release/README.md
tags:
  - kfm
  - data
  - compatibility
  - transitional
  - triplets
  - triplet-s
  - graph
  - relationship-projection
  - no-public-path
  - not-canonical
  - cite-or-abstain
notes:
  - "This README replaces an empty file at the literal path `data/triplet(s)/README.md`."
  - "The canonical lane is `data/triplets/README.md`."
  - "Directory Rules lists `data/triplets/`, not `data/triplet(s)/`."
  - "This path should not receive graph, triplet, catalog, proof, receipt, published, release, schema, policy, or public payloads."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Triplet(s) Data Compatibility Lane

Compatibility marker for the literal `data/triplet(s)/` path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Compatibility: transitional" src="https://img.shields.io/badge/compatibility-transitional-orange">
  <img alt="Canonical lane: data triplets" src="https://img.shields.io/badge/canonical-data%2Ftriplets-2b6cb0">
  <img alt="Boundary: not canonical" src="https://img.shields.io/badge/boundary-not%20canonical-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/triplet(s)/` is a literal compatibility path. The canonical KFM lifecycle lane is [`data/triplets/`](../triplets/README.md). Do not place triplet payloads, graph exports, graph deltas, catalog records, proofs, receipts, release records, published artifacts, schemas, policy, or public UI/API material here.

---

## Scope

This README exists only because the literal parentheses path is present in the repository. It prevents `data/triplet(s)/` from becoming a parallel graph or triplet authority.

Allowed material is limited to:

- this README;
- migration notes that point to `data/triplets/`;
- inventory indexes if non-README files are later found;
- redirect notes or deprecation markers.

All actual graph-compatible relationship projections belong under [`data/triplets/`](../triplets/README.md).

---

## Canonical home

| Material | Canonical home |
|---|---|
| Graph-compatible triples | [`../triplets/`](../triplets/README.md) |
| Graph deltas | `../triplets/graph_deltas/` |
| Graph exports | `../triplets/exports/` |
| Catalog records | [`../catalog/`](../catalog/README.md) |
| Proof support | [`../proofs/`](../proofs/README.md) |
| Process receipts | [`../receipts/`](../receipts/README.md) |
| Published public-safe graph artifacts | [`../published/`](../published/README.md) after release gates |
| Release decisions | [`../../release/`](../../release/README.md) |

---

## Exclusions

Do not place these here:

- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, RECEIPT, PROOF, PUBLISHED, ROLLBACK, REGISTRY, RELEASE, schema, policy, code, test, validator, or public UI/API payloads;
- graph deltas, graph exports, relationship triples, entity-resolution output, search graph material, AI graph summaries, or Focus Mode graph support;
- sensitive joins involving living persons, DNA/genomic context, archaeology, rare species, infrastructure, property, cultural knowledge, private land, or exact restricted locations.

---

## Required checks before use

- [ ] Confirm whether `data/triplet(s)/` contains anything beyond this README.
- [ ] Move any payload-like file to the correct responsibility root and lifecycle lane after review.
- [ ] Confirm new triplet work uses `data/triplets/`, not this compatibility path.
- [ ] Confirm public clients never read this path directly.
- [ ] Confirm any migration preserves evidence refs, catalog refs, proof refs, receipts, policy state, release state, correction path, and rollback path.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Literal path presence | CONFIRMED | `data/triplet(s)/README.md` existed as an empty file before this update. |
| Canonical triplet lane | CONFIRMED README | `data/triplets/README.md` is the canonical plural lane. |
| Directory Rules placement | CONFIRMED doctrine | Directory Rules lists `data/triplets/`, not this literal path. |
| Compatibility posture | PROPOSED | This README marks the path transitional until migration or deletion is approved. |
| Actual payload inventory under this path | UNKNOWN | This edit verified the README target only, not a full subtree inventory. |
| Public release readiness | DENY | This compatibility path cannot publish, prove, or expose triplet claims. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `data/triplet(s)/README.md` existed as an empty file. | Did not define boundaries. |
| [`../triplets/README.md`](../triplets/README.md) | CONFIRMED README | Canonical plural triplets lane and lifecycle contract. | Does not prove payload inventory. |
| [`../README.md`](../README.md) | CONFIRMED README | `data/` owns lifecycle data and lists `triplets`. | Data root README is short and status `PROPOSED`. |
| [`../../docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) | CONFIRMED doctrine | `data/triplets/` is the listed triplet lane. | Does not authorize this literal compatibility path as canonical. |

[Back to top](#top)
