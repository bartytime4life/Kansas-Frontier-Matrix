<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/triplet/habitat/readme
name: Habitat Triplet Compatibility README
path: data/triplet/habitat/README.md
type: data-compatibility-lane-readme
version: v0.1.0
status: draft
owners:
  - <data-steward>
  - <graph-steward>
  - <catalog-steward>
  - <habitat-domain-steward>
  - <evidence-steward>
  - <proof-steward>
  - <receipt-steward>
  - <policy-steward>
  - <sensitivity-reviewer>
  - <release-steward>
  - <docs-steward>
created: 2026-06-29
updated: 2026-06-29
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
domain: habitat
artifact_family: compatibility-marker-and-redirect
compatibility_class: transitional
authority_posture: compatibility-lane; not-canonical-lifecycle-lane; not-triplet-authority; not-graph-authority; not-habitat-truth; not-source-data; not-processed-data; not-catalog; not-proof; not-receipt; not-published; not-release-authority; not-policy-authority; not-schema-authority; not-public-api-ui-source
path_posture: existing-empty-file-replaced; singular-data-triplet-habitat-path-present; canonical-plural-triplets-root-confirmed; directory-rules-lists-data-triplets-not-data-triplet; habitat-lifecycle-docs-point-to-data-triplets-not-data-triplet; canonical-habitat-triplet-child-path-not-found-in-this-pass; deny-new-payloads-by-default
sensitivity_posture: no-public-path; deny-new-payloads-by-default; habitat-triplets-are-relationship-projections-not-habitat-truth; graph-derived-not-truth; relationship-projection-not-evidence; evidence-refs-required-for-claim-bearing-relationships; suitability-not-occurrence; habitat-patch-not-critical-habitat-designation; connectivity-not-confirmed-movement; restoration-opportunity-not-prescription; land-cover-not-habitat-truth-by-itself; species-occurrence-joins-fail-closed; rare-species-steward-controlled-sensitive-habitat-geometry-and-private-land-joins-fail-closed; source-role-preserving; evidence-aware; policy-aware; release-aware; correction-and-rollback-aware
related:
  - ../../README.md
  - ../../triplets/README.md
  - ../../triplet(s)/README.md
  - ../../processed/habitat/README.md
  - ../../catalog/domain/habitat/README.md
  - ../../proofs/habitat/README.md
  - ../../receipts/habitat/README.md
  - ../../published/habitat/README.md
  - ../../rollback/habitat/README.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/DATA_LIFECYCLE.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../release/README.md
tags:
  - kfm
  - data
  - compatibility
  - transitional
  - triplet
  - triplets
  - habitat
  - graph
  - relationship-projection
  - habitat-patch
  - land-cover
  - ecological-system
  - suitability-model
  - connectivity
  - corridor
  - restoration-opportunity
  - stewardship-zone
  - occurrence-habitat-assignment
  - public-safe-geometry
  - source-role
  - evidence-bundle
  - proof-pack
  - catalog-closure
  - no-public-path
  - not-canonical
  - not-habitat-truth
  - not-species-occurrence
  - cite-or-abstain
notes:
  - "This README replaces an empty file at `data/triplet/habitat/README.md`."
  - "The canonical triplet root is `data/triplets/README.md`; singular `data/triplet/` is not listed by Directory Rules."
  - "Habitat lifecycle docs use `data/triplets/` for relationship projections and explicitly treat triplets as non-domain-scoped in the listed path shape."
  - "This path should not receive graph, triplet, catalog, proof, receipt, published, release, schema, policy, or public payloads."
  - "Canonical Habitat triplet child placement remains NEEDS VERIFICATION; neither `data/triplets/domain/habitat/README.md` nor `data/triplets/habitat/README.md` was found in this pass."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Triplet Compatibility Lane

Compatibility marker for the singular `data/triplet/habitat/` path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Compatibility: transitional" src="https://img.shields.io/badge/compatibility-transitional-orange">
  <img alt="Canonical lane: data triplets" src="https://img.shields.io/badge/canonical-data%2Ftriplets-2b6cb0">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Boundary: not canonical" src="https://img.shields.io/badge/boundary-not%20canonical-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Canonical homes](#canonical-homes) · [Allowed contents](#allowed-contents) · [Exclusions](#exclusions) · [Habitat triplet guardrails](#habitat-triplet-guardrails) · [Migration plan](#migration-plan) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!CAUTION]
> `data/triplet/habitat/` is a singular compatibility path. The canonical KFM triplet lifecycle root is [`data/triplets/`](../../triplets/README.md). Do not place Habitat triplet payloads, graph exports, graph deltas, catalog records, proofs, receipts, release records, published artifacts, schemas, policy, source registry records, or public UI/API material here. Habitat relationship projections do not make habitat claims true by placement.

---

## Scope

This README exists because `data/triplet/habitat/README.md` is present as an empty file in the repository. Its purpose is to prevent the singular `triplet/` path from becoming a parallel Habitat graph or triplet authority.

Allowed material is limited to:

- this README;
- migration notes that point to canonical `data/triplets/` placement;
- inventory indexes if non-README files are later found;
- redirect notes or deprecation markers;
- audit notes that do not embed payloads, restricted geometry, or claim-bearing relationships.

All actual Habitat graph-compatible relationship projections belong under the canonical plural triplet lane after schema, contract, validator, policy, and release posture are verified. The current parent README proposes `data/triplets/domain/<domain>/` as a possible child shape, but a Habitat child path was **not found** in this pass.

---

## Path posture

Observed path:

```text
data/triplet/habitat/
```

Canonical triplet root:

```text
data/triplets/
```

Current placement evidence:

- `data/README.md` lists `triplets` as a data lifecycle family.
- Directory Rules lists `data/triplets/` with `graph_deltas/` and `exports/`, not singular `data/triplet/`.
- Directory Rules says triplets are relationship projections and graph-compatible triples that must not carry canonical replacement semantics.
- `data/triplets/README.md` defines the canonical plural lane as the `CATALOG / TRIPLET` graph-compatible relationship projection lane.
- `docs/domains/habitat/DATA_LIFECYCLE.md` lists Habitat triplet projections under `data/triplets/`, not `data/triplet/`.
- `data/triplet(s)/README.md` already marks the literal parentheses path as compatibility-only.

Therefore this README treats `data/triplet/habitat/` as **CONFIRMED path presence / TRANSITIONAL compatibility lane / DENY new payloads until migration or ADR**.

---

## Canonical homes

| Material type | Canonical home | Notes |
|---|---|---|
| Habitat relationship projections | [`../../triplets/`](../../triplets/README.md) | Canonical plural root. Exact Habitat child path remains NEEDS VERIFICATION. |
| Proposed Habitat triplet child shape | `data/triplets/domain/habitat/` | PROPOSED by parent shape only; README not found in this pass. |
| Habitat processed objects | [`../../processed/habitat/`](../../processed/habitat/README.md) | Upstream normalized Habitat candidates; triplets do not replace them. |
| Habitat catalog records | [`../../catalog/domain/habitat/`](../../catalog/domain/habitat/README.md) | Discovery and catalog closure; not graph edge storage. |
| Habitat proofs | [`../../proofs/habitat/`](../../proofs/habitat/README.md) | Evidence/proof support; triplets cite it. |
| Habitat receipts | [`../../receipts/habitat/`](../../receipts/habitat/README.md) | Process memory; not proof or release authority. |
| Habitat published artifacts | [`../../published/habitat/`](../../published/habitat/README.md) | Released public-safe carriers only. |
| Habitat rollback support | [`../../rollback/habitat/`](../../rollback/habitat/README.md) | Data-plane rollback support; not triplet storage. |
| Habitat doctrine | [`../../../docs/domains/habitat/`](../../../docs/domains/habitat/README.md) | Human-facing domain lane and lifecycle doctrine. |
| Release decisions | [`../../../release/`](../../../release/README.md) | ReleaseManifest, PromotionDecision, RollbackCard, CorrectionNotice, WithdrawalNotice, signatures. |

---

## Allowed contents

Allowed material is intentionally narrow:

- README files that document compatibility status and migration posture;
- migration inventories, if clearly marked as non-payload indexes;
- pointer files that direct maintainers to canonical `data/triplets/` placement;
- temporary audit notes that do not embed restricted Habitat data, graph edges, exact geometry, or claim-bearing relationships.

Any allowed file here must say that it is not source data, not processed data, not catalog, not triplet payload, not proof, not receipt, not release, not published artifact, not policy, not schema, and not public API/UI material.

---

## Exclusions

| Do not place here | Correct home |
|---|---|
| Habitat graph deltas, graph exports, relationship triples, entity-resolution output, search graph material, AI graph summaries, or Focus Mode graph support | `data/triplets/` after accepted schema and validator support |
| RAW Habitat source captures, rasters, vectors, downloads, agency payloads, or source logs | `data/raw/habitat/`, `data/work/habitat/`, or `data/quarantine/habitat/` |
| Processed HabitatPatch, LandCoverObservation, EcologicalSystem, SuitabilityModel, ConnectivityEdge, Corridor, RestorationOpportunity, StewardshipZone, or UncertaintySurface objects | `data/processed/habitat/` |
| Habitat catalog records, STAC/DCAT/PROV records, or domain catalog indexes | `data/catalog/domain/habitat/` or accepted catalog sublanes |
| EvidenceBundle, ProofPack, validation proof, public-safe geometry proof, model-support proof, or rollback proof | `data/proofs/habitat/` or accepted proof lanes |
| Run, transform, model-run, validation, policy, review, AI, release-support, correction, or rollback receipts | `data/receipts/habitat/` or accepted receipt/rollback lanes |
| Published public-safe Habitat layers, API payloads, reports, stories, PMTiles, GeoParquet, summaries, or exports | `data/published/habitat/` or `data/published/layers/habitat/` after release gates |
| SourceDescriptor, source registry records, rights records, sensitivity records, or crosswalk authority | `data/registry/sources/habitat/` or accepted registry lanes |
| ReleaseManifest, RollbackCard, CorrectionNotice, WithdrawalNotice, signatures, or release changelog | `release/` |
| Contracts, schemas, policy rules, validators, tests, implementation code, or UI code | `contracts/`, `schemas/`, `policy/`, `tests/`, `tools/`, `apps/`, or `packages/` |
| Exact sensitive habitat geometry, rare-species inference, steward-controlled ecological context, sensitive corridor context, private-landowner joins, or species/habitat joins that can reconstruct restricted locations | Restricted governed lanes only; public-safe derivative after policy/review/release |

---

## Habitat triplet guardrails

| Risk | Guardrail |
|---|---|
| Singular path becomes authority | Keep `data/triplet/habitat/` marker-only; canonical triplet work belongs under plural `data/triplets/`. |
| Projection becomes Habitat truth | Treat every Habitat triplet as a derived relationship projection unless evidence, proof, catalog, policy, and release state support stronger public use. |
| Habitat suitability becomes occurrence | A suitability relationship is not a species occurrence, animal observation, plant record, specimen, or rare-species location. |
| HabitatPatch becomes designation | A HabitatPatch relationship is not a regulatory critical-habitat designation, land-management order, or legal boundary. |
| Connectivity becomes movement | Connectivity edges and corridors are model/context relationships, not confirmed wildlife movement or migration proof. |
| Restoration becomes prescription | RestorationOpportunity relationships are context only, not prescriptions, management orders, funding eligibility, or compliance proof. |
| Land-cover becomes Habitat truth | Land-cover relationships are source-role-bound context; they do not prove Habitat quality, occurrence, stewardship status, or regulatory status by themselves. |
| Sensitive joins leak restricted facts | Species/habitat, rare-plant/habitat, archaeology/habitat, private-land/habitat, and stewardship joins can reveal restricted context even when each node looks safe. Apply the strictest owning-domain policy. |
| Evidence collapse | Claim-bearing Habitat relationships must point to EvidenceBundle/proof support or carry abstain/withhold/deny posture. |
| Source-role collapse | Observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, AI-derived, and inferred relationships must stay distinguishable. |
| Public path bypass | Public clients must not read this compatibility path directly; public graph surfaces must use governed APIs or release-resolved artifacts. |
| Stale graph state | Corrections, withdrawals, rollbacks, and supersessions must invalidate graph exports, search surfaces, Evidence Drawer content, Focus Mode answers, and AI summaries. |

---

## Migration plan

1. Inventory any non-README files under `data/triplet/habitat/`.
2. Classify each item by responsibility root: RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, RECEIPT, PROOF, PUBLISHED, ROLLBACK, REGISTRY, RELEASE, schema, policy, code, or docs.
3. Move payload-like material out of this compatibility path and into the correct canonical lane.
4. Preserve identifiers, checksums, source roles, evidence refs, catalog refs, proof refs, receipt refs, policy state, release state, correction path, rollback path, and sensitivity posture.
5. Create migration receipts if location, identity, redaction, generalization, aggregation, release state, or public-surface behavior changes.
6. Keep this README as a marker until a Directory Rules update, ADR, or migration note explicitly retires the path.

---

## Required checks before use

- [ ] Confirm whether `data/triplet/habitat/` contains anything beyond this README.
- [ ] Confirm the accepted canonical Habitat triplet child path under `data/triplets/` before adding any payload-like files.
- [ ] Confirm triplet/graph schemas and contracts for Habitat relationship projections.
- [ ] Confirm graph-build receipt shape and storage home.
- [ ] Confirm validation rules for subject, predicate, object, namespace, source role, evidence refs, policy state, release state, and sensitivity posture.
- [ ] Confirm EvidenceBundle/proof closure for claim-bearing Habitat relationships.
- [ ] Confirm rare-species, stewardship, cultural, archaeology, private-land, and other sensitive joins fail closed until policy and review allow public-safe representation.
- [ ] Confirm release linkage for any public graph export.
- [ ] Confirm correction, withdrawal, stale-state, and rollback invalidation behavior.
- [ ] Confirm public clients resolve Habitat graph projections through governed APIs or released artifacts, not direct reads from `data/triplet/habitat/`.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target path presence | CONFIRMED | `data/triplet/habitat/README.md` existed as an empty file before this update. |
| Canonical triplet root | CONFIRMED README | `data/triplets/README.md` is the canonical plural triplet lane. |
| Literal `data/triplet(s)/` path | CONFIRMED compatibility | The parentheses path is already marked compatibility-only. |
| Data root triplets family | CONFIRMED README | `data/README.md` lists `triplets` under lifecycle data. |
| Directory Rules placement | CONFIRMED doctrine | Directory Rules lists `data/triplets/`, not singular `data/triplet/`. |
| Habitat domain doctrine | CONFIRMED README | Habitat owns landscape/habitat context and governed joins, not species occurrence truth. |
| Habitat lifecycle triplet posture | CONFIRMED README | Habitat lifecycle docs list `data/triplets/` for relationship projections and keep promotion governed. |
| Habitat catalog lane | CONFIRMED README | Habitat catalog records point to triplets as paired graph projections but are not graph edge storage. |
| Habitat processed lane | CONFIRMED README | Processed Habitat artifacts are upstream of catalog/triplet/publication and not public by default. |
| Habitat proof lane | CONFIRMED README | Habitat proofs support evidence closure, validation, policy, release, correction, and rollback, but are not triplet storage. |
| Habitat receipt lane | CONFIRMED README | Habitat receipts are process memory and include graph/correction/rollback support context without becoming proof or release authority. |
| Habitat published lane | CONFIRMED README | Published Habitat artifacts are downstream released carriers only. |
| Habitat rollback lane | CONFIRMED README | Rollback support covers affected graph/triplet projections but is not triplet storage. |
| `data/triplets/domain/habitat/README.md` | NOT FOUND in this pass | Parent triplets README proposes `domain/<domain>/`, but this child README was not present. |
| `data/triplets/habitat/README.md` | NOT FOUND in this pass | Published Habitat README references `data/triplets/habitat/`, but this README was not present. |
| Actual payload inventory under this path | UNKNOWN | This edit verified the README target only, not a full subtree inventory. |
| Schemas, contracts, validators, graph-build receipts, CI, release linkage | NEEDS VERIFICATION | No runtime enforcement was proven by this edit. |
| Public release readiness | DENY | This compatibility path cannot publish, prove, or expose Habitat triplet claims. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `data/triplet/habitat/README.md` existed as an empty file. | Did not define boundaries. |
| [`../../triplets/README.md`](../../triplets/README.md) | CONFIRMED README | Canonical plural triplets lane, graph projection posture, suggested child shape, and no-public-path boundary. | Does not prove Habitat child triplet inventory. |
| [`../../triplet(s)/README.md`](../../triplet(s)/README.md) | CONFIRMED compatibility README | Literal parentheses triplet path is compatibility-only and should not receive payloads. | Does not govern this singular path directly. |
| [`../../README.md`](../../README.md) | CONFIRMED README | `data/` owns lifecycle data and lists `triplets`. | Data root README is short and status `PROPOSED`. |
| [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) | CONFIRMED doctrine | `data/triplets/`, `graph_deltas/`, `exports/`, lifecycle invariant, and no canonical replacement semantics. | Does not authorize singular `data/triplet/` as canonical. |
| [`../../../docs/domains/habitat/README.md`](../../../docs/domains/habitat/README.md) | CONFIRMED doctrine / PROPOSED implementation | Habitat owns landscape/habitat context, not species occurrence truth; source-role anti-collapse and sensitivity-redacted posture apply. | Implementation maturity remains NEEDS VERIFICATION in parts. |
| [`../../../docs/domains/habitat/DATA_LIFECYCLE.md`](../../../docs/domains/habitat/DATA_LIFECYCLE.md) | CONFIRMED doctrine / PROPOSED implementation | Habitat lifecycle lists `data/triplets/` for relationship projections and preserves RAW-to-PUBLISHED governance. | Does not prove triplet payloads or validators. |
| [`../../catalog/domain/habitat/README.md`](../../catalog/domain/habitat/README.md) | CONFIRMED README | Habitat catalog lane pairs with triplets and excludes graph edges from catalog storage. | Catalog records are not triplet payloads. |
| [`../../processed/habitat/README.md`](../../processed/habitat/README.md) | CONFIRMED README | Processed Habitat is upstream of catalog/triplet/publication and preserves source role, evidence, sensitivity, and release posture. | Does not prove triplet inventory. |
| [`../../proofs/habitat/README.md`](../../proofs/habitat/README.md) | CONFIRMED README | Habitat proof lane supports evidence closure, validation, policy, release, correction, and rollback. | Proofs are not triplet storage. |
| [`../../receipts/habitat/README.md`](../../receipts/habitat/README.md) | CONFIRMED README | Habitat receipts are process memory and include graph/correction/rollback support context. | Receipts are not proof, release, or triplet authority. |
| [`../../published/habitat/README.md`](../../published/habitat/README.md) | CONFIRMED README | Published Habitat artifacts are downstream released public-safe carriers and mention triplet graph projection as not public by itself. | Does not prove published artifacts or triplet child path exists. |
| [`../../rollback/habitat/README.md`](../../rollback/habitat/README.md) | CONFIRMED README | Rollback support includes affected graph/triplet projections and invalidation but is not release or triplet authority. | Does not prove rollback instances. |

[Back to top](#top)
