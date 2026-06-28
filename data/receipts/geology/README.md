<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/geology/readme
name: Geology Receipts README
path: data/receipts/geology/README.md
type: data-receipts-domain-parent-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <geology-domain-steward>
  - <natural-resources-steward>
  - <validation-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: geology-receipts
receipt_scope: geology-domain-process-memory
domain: geology
path_posture: domain-receipt-parent-lane; no-child-receipt-lanes-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; source-role-preserving; anti-collapse-required; exact-subsurface-private-well-deny-default; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../raw/geology/README.md
  - ../../work/geology/README.md
  - ../../quarantine/geology/README.md
  - ../../processed/geology/README.md
  - ../../proofs/README.md
  - ../../catalog/domain/geology/README.md
  - ../../published/layers/geology/README.md
  - ../../../release/manifests/README.md
  - ../../../docs/domains/geology/README.md
  - ../../../docs/domains/geology/POLICY.md
  - ../../../docs/domains/geology/PRESERVATION_MATRIX.md
  - ../../../docs/domains/geology/OPEN_QUESTIONS.md
  - ../../../contracts/domains/geology/
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../packages/domains/geology/identity/README.md
  - ../../../packages/domains/geology/crosswalk/README.md
  - ../../../packages/domains/geology/layer_manifest/README.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - geology
  - natural-resources
  - process-memory
  - source-role
  - anti-collapse
  - borehole
  - well-log
  - resource-estimate
  - redaction-receipt
  - validation-report
  - policy-decision
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/receipts/geology/README.md`."
  - "No substantive child receipt README lanes under `data/receipts/geology/` were confirmed during this edit."
  - "Geology domain docs require source-role discipline, anti-collapse across occurrence/deposit/estimate/permit/production/reserve claims, exact-location restrictions for boreholes/wells/samples/resource context, and governed lifecycle gates."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "RunReceipt doctrine says receipts are emitted by governed runs, live under `data/receipts/`, and require fail-closed verification before promotion."
  - "README presence confirms documentation only; it does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology Receipts

Domain parent receipt lane for Geology and Natural Resources process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-8a6d3b">
  <img alt="Posture: source-role preserving" src="https://img.shields.io/badge/posture-source--role--preserving-blue">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Receipt boundary](#receipt-boundary) · [Receipt families](#receipt-families) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/geology/` is for Geology receipt process memory only. It is not geologic truth, resource truth, reserve truth, production truth, ownership truth, exact subsurface-location authority, proof, EvidenceBundle authority, catalog authority, source registry authority, policy authority, release authority, public artifact authority, or generated-answer authority.

---

## Scope

This directory is the Geology-domain parent lane for receipts that document governed process memory: source intake support, normalization support, source-role validation, identity/crosswalk support, geologic-object transform support, public-safe geometry support, validation support, anti-collapse checks, correction support, rollback support, and release-candidate support.

Geology receipts record what a process did, what references it inspected, what outcome or decision class it produced, what evidence, policy, source-role, validation, transform, correction, rollback, or release-candidate references should travel downstream, and what conditions block use.

Receipts do **not** prove geologic claims, approve public release, expose exact restricted geometry, define object meaning, resolve source rights, establish reserves, prove production, prove ownership, or replace SourceDescriptors, contracts, schemas, EvidenceBundles, ProofPacks, CatalogMatrix records, PolicyDecisions, ReleaseManifests, CorrectionNotices, RollbackCards, or governed-public API output.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This Geology domain parent lane is:

```text
data/receipts/geology/
```

No substantive child receipt README lanes under this parent were confirmed during this edit. Exact receipt subtype layout under this parent remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/geology/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | geology |
| Scope | Geology process memory across source intake support, normalization, validation, source-role discipline, public-safe geometry, correction, rollback, and release-support steps |
| Path posture | domain receipt parent lane; exact subtype layout needs verification |
| Confirmed child receipt lanes | None confirmed during this edit |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Lifecycle payload lanes | `data/raw/geology/`, `data/work/geology/`, `data/quarantine/geology/`, `data/processed/geology/` where applicable |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/domains/geology/` and sensitivity policy roots, not this lane |
| Contract authority | `contracts/domains/geology/`, not this lane |
| Schema authority | `schemas/contracts/v1/domains/geology/`, not this lane |
| Default failure posture | `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, `ERROR`, or `QUARANTINE` when source role, rights, sensitivity, object family, geometry precision, evidence refs, validation state, anti-collapse check, correction path, rollback target, or release state is insufficient |

---

## Confirmed child lanes

No child receipt README lanes were confirmed under `data/receipts/geology/` during this edit.

| Child lane | Status | Notes |
|---|---|---|
| `redaction/` | **UNKNOWN** | Not confirmed by current-session repo search. |
| `validation/` | **UNKNOWN** | Not confirmed by current-session repo search. |
| `source_intake/` | **UNKNOWN** | Not confirmed by current-session repo search. |
| `crosswalk/` | **UNKNOWN** | Package docs exist for geology crosswalk work, but no receipt child lane was confirmed here. |

This confirms only current README/path evidence. It does **not** prove absence across every possible branch, and it does not prove emitted receipts, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, correction hooks, rollback hooks, or release integration.

---

## Receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what governed Geology processes did; it is not the truth source. |
| Source role stays explicit | Authority, observation, context, model, interpretation, permit, production, estimate, and release-support roles must not collapse. |
| Anti-collapse is mandatory | Occurrence, Deposit, Estimate, Permit, Production, Reserve, ExtractionSite, ReclamationRecord, and interpretation objects must remain distinct. |
| Exact restricted geometry fails closed | Boreholes, well logs, core/sample locations, private wells, sensitive resource contexts, and rights-controlled joins require restriction, generalization, or denial where policy requires. |
| Policy remains separate | Sensitivity, public-safe geometry, source-role admissibility, and release policy live in policy roots, not this receipt lane. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |
| AI is interpretive | AIReceipt can document an answer process, but generated language never becomes root truth or release state. |

---

## Receipt families

The exact receipt subtype layout is not proven by this README. This parent lane may hold or reference Geology receipt records such as:

| Receipt family | Purpose | Boundary |
|---|---|---|
| RunReceipt | Records governed run identity, spec hash, inputs, outputs, policy gates, and verification context. | Does not define geology object meaning by itself. |
| TransformReceipt | Records parsing, normalization, identity, crosswalk, geometry transform, or public-safe derivative generation. | Does not prove source truth or authorize release. |
| ValidationReport | Records source-role, anti-collapse, geometry, rights/sensitivity, digest, and release-readiness validation outcomes. | Passing validation is not proof or release approval. |
| RedactionReceipt | Records public-safe geometry generalization, restriction, withholding, or exact-location suppression where needed. | Does not make restricted geometry public by itself. |
| PolicyDecision reference | Records finite policy decision state for deny/allow/restrict/abstain outcomes. | Policy authority remains in policy roots. |
| ReviewRecord reference | Records steward or sensitivity review state for material changes or public-safe derivatives. | Review support is not ReleaseManifest authority. |
| CorrectionNotice / RollbackCard reference | Records correction or rollback support when geology artifacts must be demoted, withdrawn, regenerated, or superseded. | Correction and rollback authority remain in release governance. |

---

## Accepted material

Accepted content is limited to Geology receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- source/intake, transform, validation, redaction/public-safe-geometry, policy-decision, review, correction-support, rollback-support, and release-support receipt records;
- `RunReceipt`, `TransformReceipt`, `ValidationReport`, `RedactionReceipt`, `PolicyDecision`, `ReviewRecord`, correction-support receipts, rollback-support receipts, release-support receipts, and related process-memory records where applicable;
- run IDs, source refs, object refs, crosswalk refs, input/output hashes, evidence refs, policy refs, validator refs, object-family refs, source-role refs, geometry-transform refs, finite outcomes, reason codes, correction refs, rollback refs, timestamps, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect receipt state without becoming proof, catalog, policy, release, public output, geologic truth, resource truth, reserve truth, ownership truth, or generated-answer authority.

Do not put exact restricted subsurface coordinates, private-well details, rights-controlled well-log payloads, private landowner details, operator-sensitive joins, unreleased estimates/reserves, undisclosed resource-location detail, transform parameters that would defeat redaction, or legally restricted text into this README or public-facing local indexes.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw geology source payloads, agency snapshots, well-log files, borehole/source packets, or source-native files | `data/raw/geology/` or governed restricted storage as applicable |
| Work/scratch candidates, normalization drafts, crosswalk drafts, or transform experiments | `data/work/geology/` |
| Quarantined or unresolved rights/sensitivity/source-role material | `data/quarantine/geology/` |
| Processed public-safe geology objects or generalized layers | `data/processed/geology/` after gates; `data/published/` only after release |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, CorrectionNotice, RollbackCard, withdrawal notice, signature, or release changelog | `release/` |
| Source-role, rights, sensitivity, redaction, exact-location, public-safe geometry, reserve/estimate, or release policy | `policy/` and governed policy roots |
| Geology semantic contracts or schemas | `contracts/domains/geology/` and `schemas/contracts/v1/domains/geology/` |
| Validator code, fixtures, tests, package code, or CI workflows | `tools/`, `fixtures/`, `tests/`, `packages/`, `.github/workflows/` |
| Public map/API/UI payloads, cross-section scenes, 3D scenes, graph edges, vector-index content, or generated answer text | governed public outputs only after evidence, policy, validation, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/geology/
├── README.md
└── index.local.json
```

This map confirms the parent README lane currently documented. It does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, exact-location authority, reserve/estimate authority, policy authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records process memory but has not been consumed by downstream proof or release review. |
| Hold | Required refs, hashes, source-role refs, object-family refs, reviewer refs, evidence refs, policy refs, validation state, correction path, rollback target, or decision scope are incomplete. |
| Deny/abstain | Rights, sensitivity, source role, geometry precision, private-well exposure, exact subsurface location, operator/parcel join risk, evidence, policy, or release state remains unresolved. |
| Quarantine/correct | Receipt contradicts evidence, omits required limitations, collapses object families, lacks replay/signature support, violates policy, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite a receipt as process/transform/validation support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, review/redaction/validation state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/geology/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / cross-section / 3D scene / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. Geology receipts can support proof and release artifacts, but they do not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Geology domain and a documented receipt subtype.
- [ ] Confirm canonical domain/receipt subtype naming against ADR-S-03 or accepted receipt-layout governance before relying on this parent as final layout authority.
- [ ] Confirm receipt ID, run ID, source refs, object refs, input/output hashes, evidence refs, policy refs, validator refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm source role and object family are explicit and do not collapse Occurrence, Deposit, Estimate, Permit, Production, Reserve, ExtractionSite, ReclamationRecord, interpretation, or context.
- [ ] Confirm exact restricted subsurface/private-well/sample/resource geometry, transform parameters, private owner detail, rights-controlled payload content, and operator-sensitive joins are not exposed in README/index text.
- [ ] Confirm ReviewRecord, PolicyDecision, RedactionReceipt, ValidationReport, EvidenceBundle, and proof references resolve where required before using this receipt in any public Geology claim path.
- [ ] Confirm receipt presence is not treated as geology truth, resource truth, reserve truth, production proof, ownership proof, policy authority, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm deny/abstain/hold/error/quarantine states are recorded when rights, sensitivity, source role, anti-collapse, evidence, policy, validation, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, cross-section, 3D scene, generated answer, reserve statement, production claim, or ownership claim uses this receipt parent lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/receipts/geology/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| No substantive child receipt README lanes under `data/receipts/geology/` were confirmed during this edit. | **CONFIRMED by GitHub search during this edit / limited to current search evidence** |
| Geology domain docs require source-role discipline and anti-collapse across occurrence, deposit, estimate, permit, production, and reserve claims. | **CONFIRMED by GitHub contents API during this edit** |
| Geology domain docs say exact private-well, borehole/core, sensitive resource, and rights-controlled contexts are restricted, generalized, or blocked before public promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Geology domain docs say promotion follows RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED and is governed, not a file move. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Geology receipt README presence proves emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, policy enforcement, source activation, correction hooks, rollback hooks, or release integration. | **DENY** |
| Exact subtype layout under `data/receipts/geology/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Geology receipt payloads exist under this subtree. | **UNKNOWN** |
| This README is geologic truth, resource truth, reserve truth, production proof, ownership proof, exact-location authority, policy authority, proof, catalog authority, registry authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../raw/geology/README.md`](../../raw/geology/README.md)
- [`../../work/geology/README.md`](../../work/geology/README.md)
- [`../../quarantine/geology/README.md`](../../quarantine/geology/README.md)
- [`../../processed/geology/README.md`](../../processed/geology/README.md)
- [`../../proofs/README.md`](../../proofs/README.md)
- [`../../catalog/domain/geology/README.md`](../../catalog/domain/geology/README.md)
- [`../../published/layers/geology/README.md`](../../published/layers/geology/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/domains/geology/README.md`](../../../docs/domains/geology/README.md)
- [`../../../docs/domains/geology/POLICY.md`](../../../docs/domains/geology/POLICY.md)
- [`../../../docs/domains/geology/PRESERVATION_MATRIX.md`](../../../docs/domains/geology/PRESERVATION_MATRIX.md)
- [`../../../docs/domains/geology/OPEN_QUESTIONS.md`](../../../docs/domains/geology/OPEN_QUESTIONS.md)
- [`../../../packages/domains/geology/identity/README.md`](../../../packages/domains/geology/identity/README.md)
- [`../../../packages/domains/geology/crosswalk/README.md`](../../../packages/domains/geology/crosswalk/README.md)
- [`../../../packages/domains/geology/layer_manifest/README.md`](../../../packages/domains/geology/layer_manifest/README.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/geology/` is a Geology receipt parent lane for process memory only. It is not geologic truth, resource truth, reserve truth, production proof, ownership proof, exact-location authority, proof, catalog, registry, policy, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
