<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/hydrology/readme
name: Hydrology Receipts README
path: data/receipts/hydrology/README.md
type: data-receipts-domain-parent-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <hydrology-domain-steward>
  - <validation-steward>
  - <source-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: hydrology-receipts
receipt_scope: hydrology-domain-process-memory
domain: hydrology
path_posture: domain-receipt-parent-lane; no-child-receipt-lanes-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; source-role-preserving; first-proof-lane-proposed-not-implemented; flood-role-anti-collapse-required; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../raw/hydrology/README.md
  - ../../work/hydrology/README.md
  - ../../quarantine/hydrology/README.md
  - ../../processed/hydrology/README.md
  - ../../proofs/hydrology/README.md
  - ../../proofs/README.md
  - ../../catalog/domain/hydrology/README.md
  - ../../published/layers/hydrology/README.md
  - ../../../release/manifests/README.md
  - ../../../docs/adr/ADR-0009-hydrology-is-the-first-proof-bearing-lane.md
  - ../../../docs/domains/hydrology/GLOSSARY.md
  - ../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../docs/domains/hydrology/API_CONTRACTS.md
  - ../../../docs/domains/hydrology/EXPANSION_PLAN.md
  - ../../../docs/domains/hydrology/EXPANSION_BACKLOG.md
  - ../../../docs/domains/hydrology/VERIFICATION_BACKLOG.md
  - ../../../docs/sources/catalog/usgs/nwis-water.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - hydrology
  - process-memory
  - first-proof-lane
  - huc12
  - wbd
  - nhdplus
  - reach-identity
  - usgs-water
  - nwis
  - nfhl
  - source-role
  - flood-role-anti-collapse
  - validation-report
  - transform-receipt
  - policy-decision
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/receipts/hydrology/README.md`."
  - "No substantive child receipt README lanes under `data/receipts/hydrology/` were confirmed during this edit."
  - "ADR-0009 hydrology-first doctrine is draft/proposed and explicitly does not prove implementation artifacts already exist."
  - "Hydrology glossary doctrine requires HUC/WBD, NHDPlus reach identity, USGS observations, NFHL regulatory context, observed flood evidence, modeled hydrographs, and source roles to remain distinct."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "README presence confirms documentation only; it does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, source activation, evidence closure, policy enforcement, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Receipts

Domain parent receipt lane for Hydrology process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-1f9eda">
  <img alt="Posture: source-role preserving" src="https://img.shields.io/badge/posture-source--role--preserving-blue">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Receipt boundary](#receipt-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/hydrology/` is for Hydrology receipt process memory only. It is not hydrologic truth, flood truth, watershed authority, reach-identity authority, regulatory determination authority, proof, EvidenceBundle authority, catalog authority, source registry authority, policy authority, release authority, public artifact authority, emergency/flood-warning authority, or generated-answer authority.

---

## Scope

This directory is the Hydrology-domain parent lane for receipts that document governed process memory: source intake support, WBD/HUC handling, NHDPlus reach identity/crosswalk support, USGS Water observation handling, NFHL regulatory-context handling, transform support, validation support, correction support, rollback support, and release-candidate support.

Hydrology receipts record what a process did, what references it inspected, what outcome or decision class it produced, what evidence, policy, source-role, identity, validation, transform, correction, rollback, or release-candidate references should travel downstream, and what conditions block use.

Receipts do **not** prove hydrology claims, approve public release, create flood-warning authority, collapse NFHL into observed flood evidence, guess ambiguous reach identity, define object meaning, resolve source rights, or replace SourceDescriptors, contracts, schemas, EvidenceBundles, ProofPacks, CatalogMatrix records, PolicyDecisions, ReleaseManifests, CorrectionNotices, RollbackCards, or governed-public API output.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This Hydrology domain parent lane is:

```text
data/receipts/hydrology/
```

No substantive child receipt README lanes under this parent were confirmed during this edit. Exact receipt subtype layout under this parent remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/hydrology/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | hydrology |
| Scope | Hydrology process memory across source intake support, identity/crosswalk, transform, validation, correction, rollback, and release-support steps |
| Path posture | domain receipt parent lane; exact subtype layout needs verification |
| Confirmed child receipt lanes | None confirmed during this edit |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Lifecycle payload lanes | `data/raw/hydrology/`, `data/work/hydrology/`, `data/quarantine/hydrology/`, `data/processed/hydrology/` where applicable |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Contract authority | `contracts/domains/hydrology/`, not this lane |
| Schema authority | `schemas/contracts/v1/domains/hydrology/`, not this lane |
| Default failure posture | `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, `ERROR`, or `QUARANTINE` when source role, rights, sensitivity, HUC/WBD version, reach identity, gauge identity, NFHL role, evidence refs, validation state, correction path, rollback target, or release state is insufficient |

---

## Confirmed child lanes

No child receipt README lanes were confirmed under `data/receipts/hydrology/` during this edit.

| Child lane | Status | Notes |
|---|---|---|
| `validation/` | **UNKNOWN** | Not confirmed by current-session repo search. |
| `crosswalk/` | **UNKNOWN** | Not confirmed by current-session repo search. |
| `usgs_water/` | **UNKNOWN** | Not confirmed by current-session repo search. |
| `nfhl_context/` | **UNKNOWN** | Not confirmed by current-session repo search. |

This confirms only current README/path evidence. It does **not** prove emitted receipts, schemas, validators, fixtures, CI checks, signing, source activation, evidence closure, policy enforcement, correction hooks, rollback hooks, or release integration.

---

## Receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what governed Hydrology processes did; it is not the truth source. |
| Hydrology-first is not implementation proof | The hydrology-first ADR is proposed/draft and does not prove receipts, schemas, validators, routes, UI, workflows, or release artifacts already exist. |
| Source roles stay explicit | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic material must not collapse. |
| HUC/WBD lineage stays explicit | HUC codes, WBD snapshots, and watershed-boundary vintage must remain auditable. |
| Reach identity is not guessed | Ambiguous reach identity should produce finite negative outcomes rather than silent inference. |
| USGS Water observations remain observations | Gauge/site identity and observations remain distinct, with parameter, unit, qualifier, and no-data state preserved. |
| NFHL is regulatory context | NFHL flood zones are not observed inundation, forecasts, or flood-event proof. |
| Modeled hydrographs remain modeled | Derived hydrographs and traces must carry model/run context and must not be relabeled as observed values. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Hydrology receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- source/intake, transform, validation, identity/crosswalk, model/materialization, aggregation, policy-decision, correction-support, rollback-support, and release-support receipt records;
- `RunReceipt`, `TransformReceipt`, `ValidationReport`, `ModelRunReceipt`, `AggregationReceipt`, `PolicyDecision`, correction-support receipts, rollback-support receipts, release-support receipts, and related process-memory records where applicable;
- run IDs, source refs, object refs, HUC refs, reach refs, gauge refs, source-role refs, input/output hashes, evidence refs, policy refs, validator refs, parameter refs, unit refs, qualifier/no-data refs, version/snapshot refs, finite outcomes, reason codes, correction refs, rollback refs, timestamps, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect receipt state without becoming proof, catalog, policy, release, public output, hydrologic truth, flood truth, regulatory determination authority, reach-identity authority, or generated-answer authority.

Do not put raw source payloads, normalized data payloads, private-well details, unsupported flood-current-state claims, emergency or life-safety instructions, unresolved source-role claims, guessed reach identities, unsupported NFHL-as-observed-flood claims, or source-as-authority claims into this README or public-facing local indexes.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw hydrology feeds, agency payloads, station packets, WBD/NHDPlus/NFHL snapshots, or source-native files | `data/raw/hydrology/` or source-specific raw lanes |
| Work/scratch candidates, crosswalk drafts, normalization drafts, or transform experiments | `data/work/hydrology/` |
| Quarantined Hydrology material | `data/quarantine/hydrology/` and child quarantine lanes where applicable |
| Normalized Hydrology payloads | `data/processed/hydrology/` and accepted sublanes |
| Released layers, PMTiles, reports, hydrographs, or public downloads | `data/published/` only after release gates close |
| Pipeline executable logic | `pipelines/domains/hydrology/` |
| Pipeline declarative specs | `pipeline_specs/hydrology/` |
| Semantic contracts | `contracts/domains/hydrology/` |
| Machine schemas | `schemas/contracts/v1/domains/hydrology/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, CorrectionNotice, RollbackCard, withdrawal notice, signature, or release changelog | `release/` |
| Source-role, rights, sensitivity, reach-identity, flood-role, publication, or release policy | `policy/` and governed policy roots |
| Validator code, fixtures, tests, package code, or CI workflows | `tools/`, `fixtures/`, `tests/`, `packages/`, `.github/workflows/` |
| Emergency flood warnings, life-safety guidance, regulatory determinations, or official advisories | Official authorities and governed redirects, never this receipt lane |
| Public map/API/UI payloads, graph edges, vector-index content, or generated answer text | governed public outputs only after evidence, policy, validation, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/hydrology/
├── README.md
└── index.local.json
```

This map confirms the parent README lane currently documented. It does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, source activation, evidence closure, policy enforcement, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, hydrologic truth index, flood authority, policy authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records process memory but has not been consumed by downstream proof or release review. |
| Hold | Required refs, hashes, source-role refs, HUC/WBD refs, reach/gauge refs, evidence refs, policy refs, validation state, correction path, rollback target, or decision scope are incomplete. |
| Deny/abstain | Unknown source role, ambiguous reach identity, unresolved rights/sensitivity, unresolved evidence, unsupported NFHL-as-observed-flood claim, emergency-warning use, or release state remains unresolved. |
| Quarantine/correct | Receipt contradicts evidence, omits required source-role or lineage limits, collapses source meaning, lacks replay/signature support, violates policy, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite a receipt as process/transform/validation/crosswalk support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, policy/validation state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/hydrology/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / hydrograph / flood claim / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. Hydrology receipts can support proof and release artifacts, but they do not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Hydrology domain and a documented receipt subtype.
- [ ] Confirm canonical domain/receipt subtype naming against ADR-S-03 or accepted receipt-layout governance before relying on this parent as final layout authority.
- [ ] Confirm receipt ID, run ID, source refs, object refs, HUC/reach/gauge refs, input/output hashes, evidence refs, policy refs, validator refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm source role, object family, observed/valid/retrieval/release/correction time facets, version/snapshot, units, qualifiers, and no-data state remain explicit where material.
- [ ] Confirm WBD/HUC, NHDPlus reach identity, USGS Water observations, NFHL regulatory context, observed flood evidence, and modeled hydrographs remain distinct.
- [ ] Confirm EvidenceBundle/proof references resolve before using receipts in any public Hydrology claim path.
- [ ] Confirm receipt presence is not treated as hydrologic truth, flood truth, regulatory determination, proof, catalog closure, release approval, emergency-warning authority, or public artifact authority.
- [ ] Confirm deny/abstain/hold/error/quarantine states are recorded when rights, sensitivity, source role, reach identity, evidence, policy, validation, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, map surface, hydrograph, flood-current-state claim, generated answer, or emergency guidance uses this receipt parent lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/receipts/hydrology/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| No substantive child receipt README lanes under `data/receipts/hydrology/` were confirmed during this edit. | **CONFIRMED by GitHub search during this edit / limited to current search evidence** |
| ADR-0009 says hydrology is proposed as the first proof-bearing lane, but it does not prove implementation artifacts already exist. | **CONFIRMED by GitHub contents API during this edit / ADR status draft-proposed** |
| Hydrology glossary doctrine requires WBD/HUC, NHDPlus reach identity, USGS Water observations, NFHL regulatory context, observed flood evidence, modeled hydrographs, and source roles to remain distinct. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Hydrology receipt README presence proves emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, source activation, evidence closure, policy enforcement, correction hooks, rollback hooks, or release integration. | **DENY** |
| Exact subtype layout under `data/receipts/hydrology/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Hydrology receipt payloads exist under this subtree. | **UNKNOWN** |
| This README is hydrologic truth, flood truth, watershed authority, reach-identity authority, regulatory determination authority, proof, catalog authority, policy authority, release authority, public artifact authority, emergency/flood-warning authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../raw/hydrology/README.md`](../../raw/hydrology/README.md)
- [`../../work/hydrology/README.md`](../../work/hydrology/README.md)
- [`../../quarantine/hydrology/README.md`](../../quarantine/hydrology/README.md)
- [`../../processed/hydrology/README.md`](../../processed/hydrology/README.md)
- [`../../proofs/hydrology/README.md`](../../proofs/hydrology/README.md)
- [`../../proofs/README.md`](../../proofs/README.md)
- [`../../catalog/domain/hydrology/README.md`](../../catalog/domain/hydrology/README.md)
- [`../../published/layers/hydrology/README.md`](../../published/layers/hydrology/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/adr/ADR-0009-hydrology-is-the-first-proof-bearing-lane.md`](../../../docs/adr/ADR-0009-hydrology-is-the-first-proof-bearing-lane.md)
- [`../../../docs/domains/hydrology/GLOSSARY.md`](../../../docs/domains/hydrology/GLOSSARY.md)
- [`../../../docs/domains/hydrology/IDENTITY_MODEL.md`](../../../docs/domains/hydrology/IDENTITY_MODEL.md)
- [`../../../docs/domains/hydrology/API_CONTRACTS.md`](../../../docs/domains/hydrology/API_CONTRACTS.md)
- [`../../../docs/domains/hydrology/EXPANSION_PLAN.md`](../../../docs/domains/hydrology/EXPANSION_PLAN.md)
- [`../../../docs/domains/hydrology/EXPANSION_BACKLOG.md`](../../../docs/domains/hydrology/EXPANSION_BACKLOG.md)
- [`../../../docs/domains/hydrology/VERIFICATION_BACKLOG.md`](../../../docs/domains/hydrology/VERIFICATION_BACKLOG.md)
- [`../../../docs/sources/catalog/usgs/nwis-water.md`](../../../docs/sources/catalog/usgs/nwis-water.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/hydrology/` is a Hydrology receipt parent lane for process memory only. It is not hydrologic truth, flood truth, watershed authority, reach-identity authority, regulatory determination authority, proof, catalog, registry, policy, release, publication, public artifact authority, graph authority, vector-index authority, emergency/flood-warning authority, or generated-answer truth.

[Back to top](#top)
