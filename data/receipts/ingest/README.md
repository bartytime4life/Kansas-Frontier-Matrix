<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/ingest/readme
name: Ingest Receipts README
path: data/receipts/ingest/README.md
type: data-receipts-ingest-parent-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <ingest-steward>
  - <source-steward>
  - <validation-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: ingest-receipts
receipt_scope: source-intake-process-memory
path_posture: ingest-receipt-parent-lane; atmosphere-and-flora-child-lanes-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; source-intake-not-raw-payload; source-registry-separate; release-blocked
related:
  - atmosphere/README.md
  - flora/README.md
  - ../README.md
  - ../../README.md
  - ../atmosphere/README.md
  - ../flora/README.md
  - ../../raw/README.md
  - ../../work/README.md
  - ../../quarantine/README.md
  - ../../processed/README.md
  - ../../proofs/README.md
  - ../../catalog/README.md
  - ../../../release/manifests/README.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - ingest
  - source-intake
  - source-descriptor
  - source-role
  - run-receipt
  - validation-report
  - policy-decision
  - quarantine-routing
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/receipts/ingest/README.md`."
  - "Confirmed child receipt README lanes during this edit: `atmosphere/` and `flora/`."
  - "Both child lanes state the exact choice between `data/receipts/ingest/<domain>/` and `data/receipts/<domain>/ingest/` remains NEEDS VERIFICATION until accepted receipt-layout governance or ADR review confirms it."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "RunReceipt doctrine says receipts are emitted by governed runs, live under `data/receipts/`, and require fail-closed verification before promotion."
  - "README presence confirms documentation only; it does not prove emitted ingest receipts, source descriptors, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, evidence closure, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Ingest Receipts

Parent lane for source-intake receipt process memory.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Lane: ingest" src="https://img.shields.io/badge/lane-ingest-blue">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Ingest receipt boundary](#ingest-receipt-boundary) · [Receipt families](#receipt-families) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/ingest/` is for ingest/source-intake receipt process memory only. It is not RAW source data, source registry authority, source descriptor authority, domain truth, proof, EvidenceBundle authority, catalog authority, policy authority, release authority, public artifact authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory is the parent lane for receipts that document governed source-intake activity: source check, source descriptor reference, retrieval attempt, source head state, source-role assignment, rights/citation posture, timestamp handling, digest capture, admission decision, quarantine routing, and downstream handoff context.

Ingest receipts record what the intake process did and what evidence, source, policy, validation, review, correction, rollback, or release-candidate references need to travel downstream. They can support proof and release review later, but they do **not** prove source truth, admit source payloads by themselves, authorize publication, or replace SourceDescriptors, RAW payloads, contracts, schemas, EvidenceBundles, ProofPacks, CatalogMatrix records, PolicyDecisions, ReleaseManifests, CorrectionNotices, or RollbackCards.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This requested ingest parent lane is:

```text
data/receipts/ingest/
```

The child lanes `atmosphere/` and `flora/` are confirmed as substantive README files in the current repository. Exact ingest receipt layout remains **NEEDS VERIFICATION** because the child files themselves preserve uncertainty between `data/receipts/ingest/<domain>/` and `data/receipts/<domain>/ingest/` until accepted receipt-layout governance or ADR review confirms the pattern.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/ingest/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Receipt subtype | ingest / source-intake process memory |
| Path posture | parent ingest receipt lane; exact subtype layout needs verification |
| Confirmed child receipt lanes | `atmosphere/`, `flora/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| RAW payload authority | `data/raw/`, not this lane |
| Source registry authority | `data/registry/sources/`, not this lane |
| Contract authority | `contracts/`, not this lane |
| Schema authority | `schemas/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Default failure posture | `HOLD`, `DENY`, `ABSTAIN`, `ERROR`, `NEEDS_REVIEW`, or `QUARANTINE` when source identity, source role, rights, citation, cadence, timestamp, digest, sensitive context, evidence refs, policy refs, validation state, review state, correction path, rollback target, or release state is insufficient |

---

## Confirmed child lanes

The child lanes below are confirmed by current-session GitHub fetches. This confirms README/path evidence only; it does **not** prove emitted ingest receipts, source descriptors, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, evidence closure, correction hooks, rollback hooks, or release integration.

| Child lane | Status | Purpose | Boundary |
|---|---|---|---|
| [`atmosphere/`](atmosphere/README.md) | **CONFIRMED README** | Atmosphere source-intake process memory for source checks, source descriptor refs, retrieval attempts, source head state, source-role assignment, rights/citation posture, timestamp handling, digest capture, admission decision, quarantine routing, and downstream handoff context. | Not RAW source data, atmospheric truth, air-quality truth, SourceDescriptor authority, proof, release approval, advisory authority, health/life-safety guidance, or public artifact authority. |
| [`flora/`](flora/README.md) | **CONFIRMED README** | Flora source-intake process memory for source checks, source descriptor refs, retrieval attempts, source-role assignment, rights/citation posture, sensitivity triage, steward-review routing, digest capture, admission decision, quarantine routing, and downstream handoff context. | Not RAW source data, rare-plant truth, exact-location authority, rights authority, sensitivity policy, proof, release approval, or public artifact authority. |

Other domain ingest lanes are **UNKNOWN** until verified by repository evidence.

---

## Ingest receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what the intake process did; it is not the truth source. |
| Ingest receipt is not RAW payload | Payloads or payload references belong in RAW or restricted source lanes; receipts record intake process state and references. |
| SourceDescriptor remains separate | Source identity, rights, cadence, attribution, and role authority belong in governed source registry/source descriptor records. |
| Source roles stay explicit | Observed, modeled, aggregate, administrative, regulatory, candidate, interpretation, advisory, and synthetic roles must not collapse. |
| Sensitive context fails closed | Domain-specific sensitivity, rights, stewardship, and review gates block downstream use until resolved. |
| Review remains separate | ReviewRecord, steward review, rights-holder review, sensitivity review, and release authority roles must remain visible and not collapse. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Receipt families

The exact receipt subtype layout is not proven by this README. This parent lane may hold or reference ingest records such as:

| Receipt family | Purpose | Boundary |
|---|---|---|
| RunReceipt | Records governed intake run identity, spec hash, inputs, outputs, policy gates, and verification context. | Does not define domain object meaning by itself. |
| Ingest receipt / source-intake receipt | Records source head, retrieval, source-role, source descriptor ref, digest, admission decision, and handoff state. | Does not replace RAW payloads or SourceDescriptors. |
| ValidationReport | Records admission-time checks for source role, rights, timestamps, digest, schema sniffing, and basic boundary conditions. | Passing intake validation is not proof or release approval. |
| PolicyDecision reference | Records finite policy state for hold, deny, quarantine, allow-to-RAW, allow-to-WORK, or require-review handoff. | Policy authority remains in policy roots. |
| ReviewRecord reference | Records steward, sensitivity, rights, or release-readiness review state where ingest reveals restricted context. | Review support is not ReleaseManifest authority. |
| Correction / rollback support reference | Records intake correction, re-fetch, supersession, stale-source, or rollback support. | Correction and rollback authority remain in release governance. |

---

## Accepted material

Accepted content is limited to ingest receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- source-intake, retrieval, source-head, admission, validation, review-routing, policy-decision, correction-support, rollback-support, and release-support receipt records;
- run IDs, source refs, SourceDescriptor refs, source-role refs, request metadata summaries, retrieval times, source times, observed/valid/issue/expiry times where material, input refs, input hashes, output refs, output hashes, row/object counts, digest refs, evidence refs, policy refs, reviewer refs, validator refs, finite outcomes, reason codes, correction refs, rollback refs, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect ingest receipt state without becoming RAW payloads, source registry authority, proof, catalog, policy, release, public output, domain truth, exact-location authority, rights authority, sensitivity policy, or generated-answer authority.

Do not put raw source payloads, credentials, secrets, private tokens, full API responses, exact restricted coordinates, restricted identifiers, private-party details, consent tokens, revocation tokens, reviewer private notes, health/life-safety instructions, or unsupported source-as-authority claims into README/index text.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw source feeds, occurrence payloads, agency snapshots, source-native records, full API responses, or restricted source payloads | `data/raw/` or governed restricted storage as applicable |
| Work/scratch transformations and normalized candidates | `data/work/` |
| Quarantined source material | `data/quarantine/` |
| Normalized processed payloads | `data/processed/` and child lanes |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| Pipeline executable logic | `pipelines/` |
| Semantic contracts | `contracts/` |
| Machine schemas | `schemas/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| ReleaseManifest, promotion decision, CorrectionNotice, RollbackCard, withdrawal notice, signature, or release changelog | `release/` |
| Rights, sensitivity, geoprivacy, source-role, consent, revocation, publication, or release policy | `policy/` and governed policy roots |
| Validator code, fixtures, tests, package code, or CI workflows | `tools/`, `fixtures/`, `tests/`, `packages/`, `.github/workflows/` |
| Public map/API/UI payloads, graph edges, vector-index content, health/life-safety guidance, or generated answer text | governed public outputs only after evidence, policy, validation, review, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/ingest/
├── README.md
├── atmosphere/
│   └── README.md
├── flora/
│   └── README.md
└── index.local.json
```

This map confirms the README child lanes currently documented. It does not prove emitted ingest receipts, source descriptors, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, evidence closure, review workflow, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, source registry, sensitivity-policy authority, exact-location authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records ingest process memory but has not been consumed by downstream proof or release review. |
| Hold | Required refs, source role, rights, timestamps, hashes, source descriptor refs, evidence refs, policy refs, review refs, validation state, correction path, rollback target, or decision scope are incomplete. |
| Deny/abstain | Sensitivity, rights, stewardship, review state, source role, evidence, policy, or release state remains unresolved. |
| Quarantine/correct | Intake contradicts source metadata, omits required role/time/citation/digest/review state, violates policy, lacks replay/signature support, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite a receipt as intake/validation/review/correction support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, review/policy/validation state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/ingest/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. Ingest receipts can support proof and release artifacts, but they do not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the ingest/source-intake receipt family and a documented domain child lane.
- [ ] Confirm canonical ingest/domain receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this parent as final layout authority.
- [ ] Confirm receipt ID, run ID, source refs, SourceDescriptor refs, source-role refs, input/output hashes, evidence refs, policy refs, reviewer refs, validator refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm rights, citation, cadence, source role, time fields, sensitivity/review state, caveats, confidence, and limitations are preserved where material.
- [ ] Confirm raw payloads, credentials, secrets, full API responses, restricted coordinates, restricted identifiers, consent tokens, revocation tokens, and private review notes are not exposed in README/index text.
- [ ] Confirm EvidenceBundle/proof references resolve before using ingest receipts in any public claim path.
- [ ] Confirm receipt presence is not treated as source truth, domain truth, source registry authority, rights authority, sensitivity policy, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm deny/abstain/hold/error/needs-review/quarantine states are recorded when rights, sensitivity, source role, review, evidence, policy, validation, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, generated answer, or map surface uses this ingest parent lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/receipts/ingest/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Confirmed child receipt README lanes during this edit: `atmosphere/` and `flora/`. | **CONFIRMED by GitHub contents API during this edit** |
| Both child lanes state the exact choice between `data/receipts/ingest/<domain>/` and `data/receipts/<domain>/ingest/` remains NEEDS VERIFICATION. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Ingest child README presence proves emitted ingest receipts, source descriptors, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, evidence closure, review workflow, correction hooks, rollback hooks, or release integration. | **DENY** |
| Exact subtype layout under `data/receipts/ingest/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual ingest receipt payloads exist under this subtree. | **UNKNOWN** |
| This README is raw source data, source registry authority, source descriptor authority, domain truth, proof, catalog authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`atmosphere/README.md`](atmosphere/README.md)
- [`flora/README.md`](flora/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../atmosphere/README.md`](../atmosphere/README.md)
- [`../flora/README.md`](../flora/README.md)
- [`../../raw/README.md`](../../raw/README.md)
- [`../../work/README.md`](../../work/README.md)
- [`../../quarantine/README.md`](../../quarantine/README.md)
- [`../../processed/README.md`](../../processed/README.md)
- [`../../proofs/README.md`](../../proofs/README.md)
- [`../../catalog/README.md`](../../catalog/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/ingest/` is an ingest receipt parent lane for process memory only. It is not RAW source data, source registry authority, source descriptor authority, domain truth, proof, catalog, registry, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
