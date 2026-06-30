<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/triplet/readme
name: Triplet Data Compatibility README
path: data/triplet/README.md
type: data-compatibility-lane-readme
version: v0.1.0
status: draft
owners:
  - <data-steward>
  - <graph-steward>
  - <catalog-steward>
  - <directory-rules-steward>
  - <evidence-steward>
  - <proof-steward>
  - <receipt-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-29
updated: 2026-06-29
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: compatibility-marker-and-redirect
compatibility_class: transitional
authority_posture: compatibility-lane; not-canonical-lifecycle-lane; not-triplet-authority; not-graph-authority; not-source-data; not-processed-data; not-catalog; not-proof; not-receipt; not-published; not-release-authority; not-policy-authority; not-schema-authority; not-public-api-ui-source
path_posture: existing-empty-file-replaced; singular-data-triplet-path-present; canonical-plural-triplets-root-confirmed; directory-rules-lists-data-triplets-not-data-triplet; data-readme-lists-triplets-not-triplet; literal-data-triplet-s-path-is-compatibility-only; singular-habitat-child-compatibility-readme-confirmed; deny-new-payloads-by-default
sensitivity_posture: no-public-path; deny-new-payloads-by-default; graph-derived-not-truth; relationship-projection-not-evidence; triplets-are-projections-not-canonical-truth; evidence-refs-required-for-claim-bearing-relationships; source-role-preserving; sensitive-joins-fail-closed; living-person-dna-archaeology-rare-species-infrastructure-property-cultural-and-exact-location-joins-restricted; policy-aware; release-aware; correction-and-rollback-aware
related:
  - ../README.md
  - ../triplets/README.md
  - ../triplet(s)/README.md
  - habitat/README.md
  - ../catalog/README.md
  - ../proofs/README.md
  - ../receipts/README.md
  - ../published/README.md
  - ../rollback/README.md
  - ../../release/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/lifecycle-law.md
  - ../../docs/doctrine/trust-membrane.md
  - ../../contracts/
  - ../../schemas/
  - ../../policy/
tags:
  - kfm
  - data
  - compatibility
  - transitional
  - triplet
  - triplets
  - graph
  - relationship-projection
  - graph-deltas
  - exports
  - catalog-triplet
  - evidence-ref
  - evidence-bundle
  - proof-pack
  - catalog-closure
  - no-public-path
  - not-canonical
  - graph-derived-not-truth
  - not-release-authority
  - not-public-api-source
  - source-role
  - sensitive-joins
  - correction-path
  - rollback-path
  - cite-or-abstain
notes:
  - "This README replaces an empty file at `data/triplet/README.md`."
  - "The canonical KFM triplet lane is `data/triplets/README.md`."
  - "Directory Rules lists `data/triplets/` with `graph_deltas/` and `exports/`, not singular `data/triplet/`."
  - "The data root lists `triplets` as a lifecycle family and excludes release decisions."
  - "This path is a compatibility marker only and must not receive graph, triplet, catalog, proof, receipt, published, release, schema, policy, source-registry, or public payloads."
  - "The singular child `data/triplet/habitat/README.md` exists as a compatibility marker and does not authorize this parent as a canonical lane."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Triplet Data Compatibility Lane

Compatibility marker for the singular `data/triplet/` path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Compatibility: transitional" src="https://img.shields.io/badge/compatibility-transitional-orange">
  <img alt="Canonical lane: data triplets" src="https://img.shields.io/badge/canonical-data%2Ftriplets-2b6cb0">
  <img alt="Boundary: not canonical" src="https://img.shields.io/badge/boundary-not%20canonical-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Canonical homes](#canonical-homes) · [Child compatibility lanes](#child-compatibility-lanes) · [Allowed contents](#allowed-contents) · [Exclusions](#exclusions) · [Triplet compatibility guardrails](#triplet-compatibility-guardrails) · [Migration plan](#migration-plan) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!CAUTION]
> `data/triplet/` is a singular compatibility path. The canonical KFM triplet lifecycle lane is [`data/triplets/`](../triplets/README.md). Do not place triplet payloads, graph exports, graph deltas, catalog records, proofs, receipts, release records, published artifacts, source registry records, schemas, policy, code, or public UI/API material here.

---

## Scope

This README exists because `data/triplet/README.md` is present in the repository as an empty file. Its purpose is to make the singular path inspectable and prevent it from becoming a parallel graph or triplet authority.

Allowed material is limited to:

- this README;
- migration notes that point to canonical `data/triplets/` placement;
- inventory indexes if non-README files are later found;
- redirect notes or deprecation markers;
- temporary audit notes that do not embed payloads, restricted joins, exact geometry, or claim-bearing relationships.

All actual graph-compatible relationship projections belong under [`data/triplets/`](../triplets/README.md), after schemas, contracts, validators, evidence/proof references, policy posture, release posture, correction path, and rollback path are verified.

---

## Path posture

Observed compatibility path:

```text
data/triplet/
```

Canonical triplet root:

```text
data/triplets/
```

Current placement evidence:

- `data/README.md` lists `triplets` as a lifecycle data family and excludes release decisions from `data/`.
- Directory Rules lists `data/triplets/` with `graph_deltas/` and `exports/`, not singular `data/triplet/`.
- Directory Rules says triplets are relationship projections and graph-compatible triples that must not carry canonical replacement semantics.
- `data/triplets/README.md` defines the canonical plural lane as the `CATALOG / TRIPLET` graph-compatible relationship projection lane.
- `data/triplet(s)/README.md` marks the literal parentheses path as compatibility-only.
- `data/triplet/habitat/README.md` marks a singular child path as compatibility-only and points back to plural `data/triplets/`.

Therefore this README treats `data/triplet/` as **CONFIRMED path presence / TRANSITIONAL compatibility lane / DENY new payloads until migration or ADR**.

---

## Canonical homes

| Material | Canonical home | Boundary |
|---|---|---|
| Graph-compatible triples | [`../triplets/`](../triplets/README.md) | Canonical plural triplet lane. |
| Graph deltas | `../triplets/graph_deltas/` | Proposed child under canonical triplets root. |
| Graph exports | `../triplets/exports/` | Proposed child under canonical triplets root. |
| Domain triplet projections | `../triplets/domain/<domain>/` | Proposed by the triplets parent README; concrete child inventory remains NEEDS VERIFICATION. |
| Catalog records | [`../catalog/`](../catalog/README.md) | Paired CATALOG projection; not graph edge storage. |
| Evidence and proof support | [`../proofs/`](../proofs/README.md) | EvidenceBundle, ProofPack, validation, and citation support. |
| Process receipts | [`../receipts/`](../receipts/README.md) | Graph-build, catalog-build, validation, AI, correction, and rollback process memory. |
| Published public-safe graph artifacts | [`../published/`](../published/README.md) after release gates | Public delivery only after release governance. |
| Rollback support | [`../rollback/`](../rollback/README.md) | Data-plane rollback support; not graph edge storage. |
| Release decisions | [`../../release/`](../../release/README.md) | ReleaseManifest, PromotionDecision, RollbackCard, CorrectionNotice, WithdrawalNotice, signatures. |

---

## Child compatibility lanes

| Child lane | Status | Boundary |
|---|---:|---|
| [`habitat/`](habitat/README.md) | CONFIRMED README | Compatibility marker only. Habitat graph/triplet projections belong under plural `data/triplets/` after accepted child placement, schema, proof, policy, and release support are verified. |

This table confirms README/path evidence only. It does **not** prove payload inventory, schemas, validators, graph-build receipts, release linkage, or public graph availability.

---

## Allowed contents

Allowed material is intentionally narrow:

- compatibility README files;
- migration inventories, if clearly marked as non-payload indexes;
- pointer files that direct maintainers to canonical `data/triplets/` placement;
- temporary audit notes that do not embed graph edges, source payloads, restricted joins, exact geometry, or claim-bearing relationships.

Any allowed file here must say that it is not source data, not processed data, not catalog, not triplet payload, not proof, not receipt, not release, not published artifact, not policy, not schema, and not public API/UI material.

---

## Exclusions

| Do not place here | Correct home |
|---|---|
| Graph deltas, graph exports, relationship triples, entity-resolution output, search graph material, AI graph summaries, or Focus Mode graph support | `data/triplets/` after accepted schema and validator support |
| RAW, WORK, QUARANTINE, or PROCESSED data | `data/raw/`, `data/work/`, `data/quarantine/`, or `data/processed/` |
| Catalog records, STAC/DCAT/PROV records, or domain catalog indexes | `data/catalog/` |
| EvidenceBundle, ProofPack, validation proof, citation validation, or integrity proof | `data/proofs/` |
| Run, transform, validation, AI, graph-build, release-support, correction, or rollback receipts | `data/receipts/` or accepted rollback lanes |
| Published public-safe graph artifacts, API payloads, maps, tiles, stories, reports, PMTiles, GeoParquet, or exports | `data/published/` after release gates |
| SourceDescriptor, source registry records, rights records, sensitivity records, layer records, or dataset records | `data/registry/` |
| ReleaseManifest, PromotionDecision, RollbackCard, CorrectionNotice, WithdrawalNotice, signatures, or release changelog | `release/` |
| Contracts, schemas, policy rules, validators, tests, implementation code, or UI code | `contracts/`, `schemas/`, `policy/`, `tools/`, `tests/`, `apps/`, or `packages/` |
| Sensitive joins involving living persons, DNA/genomic context, archaeology, rare species, infrastructure, property, cultural knowledge, private land, or exact restricted locations | Restricted governed lanes only; public-safe derivative after policy/review/release |

---

## Triplet compatibility guardrails

| Risk | Guardrail |
|---|---|
| Singular path becomes authority | Keep `data/triplet/` marker-only; canonical triplet work belongs under plural `data/triplets/`. |
| Projection becomes truth | Treat every triplet-like item as a derived relationship projection unless evidence, proof, catalog, policy, and release state support public use. |
| Canonical replacement semantics | Do not let singular-path material replace processed domain records, source records, catalog records, or EvidenceBundles. |
| Evidence collapse | Claim-bearing relationships must point to EvidenceBundle/proof support or carry abstain/withhold/deny posture. |
| Source-role collapse | Observed, inferred, modeled, administrative, generated, historical, candidate, synthetic, and AI-derived relationships must stay distinguishable. |
| Sensitive join leakage | Relationship projections can reveal restricted facts even when individual nodes look safe. Apply the strictest relevant policy. |
| Public path bypass | Public clients must not read this compatibility path directly; public graph surfaces must use governed APIs or release-resolved artifacts. |
| AI surface drift | Generated answers must not cite this compatibility path as root evidence, proof, release, or graph authority. |
| Stale graph state | Corrections, withdrawals, rollbacks, and supersessions must invalidate graph exports, search surfaces, Evidence Drawer content, Focus Mode answers, and AI summaries. |

---

## Migration plan

1. Inventory any non-README files under `data/triplet/`.
2. Classify each item by responsibility root: RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, RECEIPT, PROOF, PUBLISHED, ROLLBACK, REGISTRY, RELEASE, schema, policy, code, or docs.
3. Move payload-like material out of this compatibility path and into the correct canonical lane.
4. Preserve identifiers, checksums, source roles, evidence refs, catalog refs, proof refs, receipt refs, policy state, release state, correction path, rollback path, and sensitivity posture.
5. Create migration receipts if location, identity, redaction, generalization, aggregation, release state, or public-surface behavior changes.
6. Keep this README as a marker until a Directory Rules update, ADR, or migration note explicitly retires the path.

---

## Suggested marker shape

Do not pre-create these files unless an audit finds material to track.

```text
data/triplet/
├── README.md
├── habitat/
│   └── README.md
├── MIGRATION-NOTE.md                 # PROPOSED only if migration starts
├── inventory.index.json              # PROPOSED only if non-README files are found
└── redirects.json                     # PROPOSED only if canonical paths need explicit pointers
```

If any payload-like file appears here, classify it immediately and move it to the correct lifecycle lane after review.

---

## Required checks before use

- [ ] Confirm whether `data/triplet/` contains anything beyond README/compatibility marker files.
- [ ] Confirm whether any ADR, migration note, or Directory Rules update explicitly authorizes this singular path.
- [ ] Confirm new triplet work uses `data/triplets/`, not this compatibility path.
- [ ] Confirm concrete child directories under canonical `data/triplets/` before adding payload-like files.
- [ ] Confirm triplet/graph schemas and contracts for relationship projections.
- [ ] Confirm graph-build receipt shape and storage home.
- [ ] Confirm validation rules for subject, predicate, object, namespace, source role, evidence refs, policy state, release state, and sensitivity posture.
- [ ] Confirm EvidenceBundle/proof closure for claim-bearing relationships.
- [ ] Confirm release linkage for any public graph export.
- [ ] Confirm correction, withdrawal, stale-state, and rollback invalidation behavior.
- [ ] Confirm public clients resolve graph projections through governed APIs or released artifacts, not direct reads from `data/triplet/`.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target path presence | CONFIRMED | `data/triplet/README.md` existed as an empty file before this update. |
| Canonical triplet root | CONFIRMED README | `data/triplets/README.md` is the canonical plural triplet lane. |
| Literal `data/triplet(s)/` path | CONFIRMED compatibility | The parentheses path is marked compatibility-only. |
| Singular Habitat child path | CONFIRMED compatibility | `data/triplet/habitat/README.md` is marked compatibility-only. |
| Data root triplets family | CONFIRMED README | `data/README.md` lists `triplets` under lifecycle data. |
| Directory Rules placement | CONFIRMED doctrine | Directory Rules lists `data/triplets/`, not singular `data/triplet/`. |
| Catalog/triplet pairing | CONFIRMED README | `data/catalog/README.md` says the paired graph projection lane is `data/triplets/`. |
| Release decision split | CONFIRMED README | `release/README.md` says release decisions live in `release/`, distinct from `data/published/`. |
| Actual payload inventory under this path | UNKNOWN | This edit verified README evidence, not a full subtree inventory. |
| Schemas, contracts, validators, graph-build receipts, CI, release linkage | NEEDS VERIFICATION | No runtime enforcement was proven by this edit. |
| Public release readiness | DENY | This compatibility path cannot publish, prove, or expose triplet claims. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `data/triplet/README.md` existed as an empty file. | Did not define boundaries. |
| [`../triplets/README.md`](../triplets/README.md) | CONFIRMED README | Canonical plural triplets lane, graph projection posture, suggested child shape, and no-public-path boundary. | Does not prove payload inventory. |
| [`../triplet(s)/README.md`](../triplet(s)/README.md) | CONFIRMED compatibility README | Literal parentheses path is compatibility-only and points to `data/triplets/`. | Does not authorize singular `data/triplet/`. |
| [`habitat/README.md`](habitat/README.md) | CONFIRMED compatibility README | Singular Habitat child path is compatibility-only and points to plural `data/triplets/`. | Does not prove canonical Habitat triplet child placement or payloads. |
| [`../README.md`](../README.md) | CONFIRMED README | `data/` owns lifecycle data and lists `triplets`. | Data root README is short and status `PROPOSED`. |
| [`../../docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) | CONFIRMED doctrine | `data/triplets/`, `graph_deltas/`, `exports/`, lifecycle invariant, and no canonical replacement semantics. | Does not authorize singular `data/triplet/` as canonical. |
| [`../catalog/README.md`](../catalog/README.md) | CONFIRMED README | Catalog README identifies `data/triplets/` as the paired graph projection lane for `CATALOG / TRIPLET`. | Catalog README does not prove triplet payloads exist. |
| [`../../release/README.md`](../../release/README.md) | CONFIRMED README | Release decisions live in `release/`, not this compatibility path. | Release root README is short and status `PROPOSED`. |

[Back to top](#top)
