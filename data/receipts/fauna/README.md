<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/fauna/readme
name: Fauna Receipts README
path: data/receipts/fauna/README.md
type: data-receipts-domain-parent-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <fauna-domain-steward>
  - <sensitivity-reviewer>
  - <rights-holder-representative>
  - <validation-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: fauna-receipts
receipt_scope: fauna-domain-process-memory
domain: fauna
path_posture: domain-receipt-parent-lane; redaction-child-lane-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; deny-by-default; exact-location-deny-default; redaction-receipt-required; review-required; release-blocked
related:
  - redaction/README.md
  - ../README.md
  - ../../README.md
  - ../../raw/fauna/README.md
  - ../../work/fauna/README.md
  - ../../quarantine/fauna/README.md
  - ../../processed/fauna/README.md
  - ../../proofs/fauna/README.md
  - ../../proofs/README.md
  - ../../catalog/domain/fauna/README.md
  - ../../published/layers/fauna/README.md
  - ../../../release/manifests/README.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../docs/domains/fauna/CANONICAL_PATHS.md
  - ../../../docs/domains/fauna/MAP_UI_CONTRACTS.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - fauna
  - process-memory
  - redaction
  - redaction-receipt
  - geoprivacy
  - sensitive-species
  - sensitive-occurrence
  - sensitive-site
  - review-record
  - policy-decision
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/receipts/fauna/README.md`."
  - "Confirmed child receipt README lane during this edit: `redaction/`."
  - "Fauna sensitivity doctrine says this domain fails closed where sensitivity, rights, or review state is unresolved."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "RunReceipt doctrine says receipts are emitted by governed runs, live under `data/receipts/`, and require fail-closed verification before promotion."
  - "README presence confirms documentation only; it does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Receipts

Domain parent receipt lane for Fauna process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: fauna" src="https://img.shields.io/badge/domain-fauna-2e7d32">
  <img alt="Posture: deny by default" src="https://img.shields.io/badge/posture-deny--by--default-critical">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Receipt boundary](#receipt-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/fauna/` is for Fauna receipt process memory only. It is not species-location truth, exact-location authority, sensitivity policy, proof, EvidenceBundle authority, catalog authority, source registry authority, release authority, public artifact authority, public API/UI material, enforcement or alert authority, or generated-answer authority.

---

## Scope

This directory is the Fauna-domain parent lane for receipts that document governed process memory: source intake support, redaction/geoprivacy, sensitivity review support, validation support, aggregation support, correction support, rollback support, and release-candidate support.

Fauna receipts record what a process did, what references it inspected, what outcome or decision class it produced, what evidence, policy, review, source-role, redaction, validation, correction, rollback, or release-candidate references should travel downstream, and what conditions block use.

Receipts do **not** prove species occurrence, approve public release, expose exact geometry, define sensitivity policy, decide enforcement/alert posture, or replace SourceDescriptors, contracts, schemas, ReviewRecords, PolicyDecisions, EvidenceBundles, ProofPacks, CatalogMatrix records, ReleaseManifests, CorrectionNotices, RollbackCards, or governed-public API output.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This Fauna domain parent lane is:

```text
data/receipts/fauna/
```

The child lane `redaction/` is confirmed as a substantive README file in the current repository. Exact receipt subtype layout under this parent remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/fauna/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | fauna |
| Scope | Fauna process memory across source intake support, redaction/geoprivacy, review, validation, aggregation, correction, rollback, and release-support steps |
| Path posture | domain receipt parent lane; exact subtype layout needs verification |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Lifecycle payload lanes | `data/raw/fauna/`, `data/work/fauna/`, `data/quarantine/fauna/`, `data/processed/fauna/` where applicable |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/sensitivity/fauna/` and `policy/domains/fauna/`, not this lane |
| Default failure posture | `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, or `QUARANTINE` when tier, rank, policy ref, reviewer, rights state, source role, geometry precision, evidence refs, validation state, correction path, rollback target, or release state is insufficient |

---

## Confirmed child lanes

The child lane below is confirmed by current-session GitHub fetches. This confirms README/path evidence only; it does **not** prove emitted receipts, schemas, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration.

| Child lane | Status | Purpose | Boundary |
|---|---|---|---|
| [`redaction/`](redaction/README.md) | **CONFIRMED README** | Fauna geoprivacy and redaction process memory for generalization, masking, aggregation support, withholding, suppression, embargo/delay support, re-identification risk handling, tier-transition support, review-state recording, correction support, rollback support, and release-candidate support. | Not exact-location authority, species-location truth, sensitivity policy, proof, release approval, or public artifact authority. |

---

## Receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what governed Fauna processes did; it is not the truth source. |
| Deny by default | Sensitive taxa, nests, dens, roosts, hibernacula, spawning sites, steward-controlled records, and re-identifying joins fail closed when sensitivity, rights, or review state is unresolved. |
| Exact geometry stays protected | README/index text must not expose exact sensitive coordinates, identifiers, generalization radii, fuzzing parameters, transform seeds, consent tokens, or revocation tokens. |
| Policy remains separate | Binding admissibility and geoprivacy rules live in `policy/sensitivity/fauna/` and `policy/domains/fauna/`. |
| Review remains separate | ReviewRecord, sensitivity reviewer, domain steward, rights-holder representative, and release authority roles must remain visible and not collapse. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Fauna receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- source/intake, redaction/geoprivacy, sensitivity review, validation, aggregation-support, policy-decision, correction-support, rollback-support, and release-support receipt records;
- `RedactionReceipt`, `ReviewRecord`, `PolicyDecision`, `AggregationReceipt`, `ValidationReport`, correction-support receipts, rollback-support receipts, release-support receipts, and related process-memory records where applicable;
- run IDs, source refs, occurrence refs, site refs, input/output hashes, evidence refs, policy refs, profile refs, transform-family refs, reviewer refs, validation refs, finite outcomes, reason codes, correction refs, rollback refs, timestamps, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect receipt state without becoming proof, catalog, policy, release, public output, exact-location authority, species-location truth, or generated-answer authority.

Do not put exact sensitive coordinates, nest/den/roost/hibernacula/spawning locations, private landowner details, restricted identifiers, generalization radii, fuzzing parameters, transform seeds, reviewer private notes, consent tokens, revocation tokens, or culturally/legally restricted text into this README or public-facing local indexes.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw occurrence/source payloads, exact sensitive coordinates, restricted identifiers, or source-native files | `data/raw/fauna/` or governed restricted storage as applicable |
| Work/scratch candidates and transform experiments | `data/work/fauna/` |
| Quarantined or unresolved sensitive material | `data/quarantine/fauna/` |
| Processed public-safe fauna objects or generalized layers | `data/processed/fauna/` after gates; `data/published/` only after release |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, CorrectionNotice, RollbackCard, withdrawal notice, signature, or release changelog | `release/` |
| Sensitivity, geoprivacy, redaction, review, rights, consent, revocation, or release policy | `policy/sensitivity/fauna/`, `policy/domains/fauna/`, and governed policy roots |
| Receipt schemas or semantic contracts | `schemas/` and `contracts/` |
| Validator code, fixtures, tests, or CI workflows | `tools/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Public map/API/UI payloads, species pages, graph edges, vector-index content, or generated answer text | governed public outputs only after evidence, policy, validation, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/fauna/
├── README.md
├── redaction/
│   └── README.md
└── index.local.json
```

This map confirms the README child lane currently documented. It does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, exact-location authority, sensitivity-policy authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records process memory but has not been consumed by downstream proof or release review. |
| Hold | Required refs, hashes, reviewer refs, evidence refs, policy refs, validation state, correction path, rollback target, or decision scope are incomplete. |
| Deny/abstain | Sensitivity, rights, review state, source role, geometry precision, or re-identification risk remains unresolved. |
| Quarantine/correct | Receipt contradicts evidence, omits required limitations, lacks replay/signature support, violates policy, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite a receipt as process/redaction/validation support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, review/redaction state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/fauna/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / species page / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. Fauna receipts can support proof and release artifacts, but they do not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Fauna domain and a documented child receipt lane.
- [ ] Confirm canonical domain/receipt subtype naming against ADR-S-03 or accepted receipt-layout governance before relying on this parent as final layout authority.
- [ ] Confirm receipt ID, run ID, source refs, subject refs, input/output hashes, policy refs, profile refs, reviewer refs, evidence refs, validation refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm exact sensitive coordinates, identifiers, generalization radii, fuzzing parameters, transform seeds, consent tokens, and revocation tokens are not exposed in README/index text.
- [ ] Confirm ReviewRecord and PolicyDecision references exist where tier movement, sensitive occurrence/site handling, steward-controlled records, rights restrictions, or public-safe derivatives are involved.
- [ ] Confirm EvidenceBundle/proof references resolve before using receipts in any public Fauna claim path.
- [ ] Confirm receipt presence is not treated as sensitivity policy, exact-location authority, species-location truth, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm deny/abstain/hold/quarantine states are recorded when sensitivity, rights, review, source role, re-identification risk, evidence, policy, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, species page, generated answer, or map surface uses this receipt parent lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/receipts/fauna/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Confirmed child receipt README lane during this edit: `redaction/`. | **CONFIRMED by GitHub contents API during this edit** |
| Fauna sensitivity doctrine says sensitive species and sites fail closed by default and exact location exposure creates real-world harm. | **CONFIRMED by GitHub contents API during this edit** |
| Fauna sensitivity doctrine says binding admissibility rules live in `policy/sensitivity/fauna/` and `policy/domains/fauna/`, while this README only explains receipt-lane handling. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Fauna receipt child README presence proves emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration. | **DENY** |
| Exact subtype layout under `data/receipts/fauna/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Fauna receipt payloads exist under this subtree. | **UNKNOWN** |
| This README is species-location truth, exact-location authority, sensitivity policy authority, proof, catalog authority, registry authority, release authority, public artifact authority, enforcement/alert authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`redaction/README.md`](redaction/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../raw/fauna/README.md`](../../raw/fauna/README.md)
- [`../../work/fauna/README.md`](../../work/fauna/README.md)
- [`../../quarantine/fauna/README.md`](../../quarantine/fauna/README.md)
- [`../../processed/fauna/README.md`](../../processed/fauna/README.md)
- [`../../proofs/fauna/README.md`](../../proofs/fauna/README.md)
- [`../../proofs/README.md`](../../proofs/README.md)
- [`../../catalog/domain/fauna/README.md`](../../catalog/domain/fauna/README.md)
- [`../../published/layers/fauna/README.md`](../../published/layers/fauna/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/domains/fauna/SENSITIVITY.md`](../../../docs/domains/fauna/SENSITIVITY.md)
- [`../../../docs/domains/fauna/SOURCE_REGISTRY.md`](../../../docs/domains/fauna/SOURCE_REGISTRY.md)
- [`../../../docs/domains/fauna/CANONICAL_PATHS.md`](../../../docs/domains/fauna/CANONICAL_PATHS.md)
- [`../../../docs/domains/fauna/MAP_UI_CONTRACTS.md`](../../../docs/domains/fauna/MAP_UI_CONTRACTS.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/fauna/` is a Fauna receipt parent lane for process memory only. It is not species-location truth, exact-location authority, sensitivity policy, proof, catalog, registry, release, publication, public artifact authority, graph authority, vector-index authority, enforcement/alert authority, or generated-answer truth.

[Back to top](#top)
