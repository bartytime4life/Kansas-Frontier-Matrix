<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/ingest/flora/readme
name: Flora Ingest Receipts README
path: data/receipts/ingest/flora/README.md
type: data-receipts-ingest-domain-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <ingest-steward>
  - <flora-domain-steward>
  - <source-steward>
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
artifact_family: flora-ingest-receipts
receipt_scope: flora-source-intake-process-memory
domain: flora
path_posture: requested-ingest-domain-receipt-lane; ingest-parent-still-stub; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; source-intake-not-raw-payload; deny-by-default; exact-location-deny-default; rights-and-sensitivity-fail-closed; redaction-review-required-before-public-release; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../flora/README.md
  - ../../flora/redaction/README.md
  - ../../../raw/flora/README.md
  - ../../../work/flora/README.md
  - ../../../quarantine/flora/README.md
  - ../../../processed/flora/README.md
  - ../../../catalog/domain/flora/README.md
  - ../../../published/layers/flora/README.md
  - ../../../proofs/README.md
  - ../../../../release/manifests/README.md
  - ../../../../docs/domains/flora/SENSITIVITY.md
  - ../../../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md
  - ../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - ../../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../../contracts/domains/flora/rare_plant_record.md
  - ../../../../contracts/domains/flora/flora_occurrence.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/standards/RUN_RECEIPT.md
  - ../../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - ingest
  - flora
  - source-intake
  - source-role
  - source-descriptor
  - rare-plant
  - sensitive-taxa
  - exact-location-deny
  - rights-gate
  - sensitivity-gate
  - redaction-receipt
  - review-record
  - validation-report
  - policy-decision
  - no-public-path
  - evidence-first
notes:
  - "This README replaces a blank placeholder at `data/receipts/ingest/flora/README.md`."
  - "Parent `data/receipts/ingest/README.md` is currently a greenfield stub."
  - "Flora receipt docs confirm Flora receipts are process memory and do not prove rare plant occurrence, approve public release, expose exact geometry, define sensitivity policy, decide rights authority, or replace proof/release artifacts."
  - "Flora sensitivity doctrine says exact rare, protected, or culturally sensitive plant locations are denied on public surfaces by default and require steward review, generalized or withheld geometry, and RedactionReceipt before public release."
  - "Concrete source payloads, exact sensitive geometry, credentials, restricted source details, consent/revocation tokens, and redaction parameters are deliberately excluded from this README."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "README presence confirms documentation only; it does not prove emitted ingest receipts, source descriptors, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, evidence closure, review workflow, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Ingest Receipts

Ingest receipt lane for Flora source-intake process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-2ea44f">
  <img alt="Lane: ingest" src="https://img.shields.io/badge/lane-ingest-blue">
  <img alt="Posture: deny by default" src="https://img.shields.io/badge/posture-deny--by--default-critical">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Ingest receipt boundary](#ingest-receipt-boundary) · [Receipt families](#receipt-families) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/ingest/flora/` is for Flora ingest receipt process memory only. It is not raw source data, rare-plant truth, Flora occurrence truth, exact-location authority, rights authority, sensitivity policy, proof, EvidenceBundle authority, catalog authority, source registry authority, release authority, public artifact authority, or generated-answer authority.

---

## Scope

This directory is for receipt records and receipt-local sidecars that document governed Flora source-intake activity: source check, source descriptor reference, retrieval attempt, source head state, source-role assignment, rights/citation posture, sensitivity triage, steward-review routing, timestamp handling, digest capture, basic admission decision, quarantine routing, and downstream handoff context.

Ingest receipts record what the intake process did and what evidence, source, policy, review, validation, correction, rollback, or release-candidate references need to travel downstream. They can support proof and release review later, but they do **not** prove Flora occurrence, admit source payloads by themselves, approve public release, or replace SourceDescriptors, RAW payloads, contracts, schemas, ReviewRecords, PolicyDecisions, EvidenceBundles, ProofPacks, CatalogMatrix records, ReleaseManifests, CorrectionNotices, or RollbackCards.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested ingest/domain receipt lane is:

```text
data/receipts/ingest/flora/
```

This README documents the requested lane without claiming final receipt-layout authority. The parent `data/receipts/ingest/README.md` is still a greenfield stub, and the exact choice between `data/receipts/ingest/<domain>/` and `data/receipts/<domain>/ingest/` remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/ingest/flora/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Receipt subtype | ingest / source-intake process memory |
| Domain lane | flora |
| Path posture | requested ingest/domain receipt lane; exact subtype layout needs verification |
| Parent root | `data/receipts/ingest/` |
| Related domain receipt parent | `data/receipts/flora/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| RAW payload authority | `data/raw/flora/`, not this lane |
| Source registry authority | `data/registry/sources/`, not this lane |
| Contract authority | `contracts/domains/flora/`, not this lane |
| Schema authority | `schemas/contracts/v1/domains/flora/`, not this lane |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/sensitivity/flora/`, `policy/geoprivacy/`, and other policy roots, not this lane |
| Default failure posture | `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, `ERROR`, or `QUARANTINE` when source identity, source role, rights, sensitivity tier, steward state, citation, cadence, timestamp, digest, geometry precision, evidence refs, policy refs, validation state, correction path, rollback target, or release state is insufficient |

---

## Ingest receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what the intake process did; it is not the truth source. |
| Ingest receipt is not RAW payload | Payloads or payload references belong in RAW or restricted source lanes; receipts record intake process state and references. |
| SourceDescriptor remains separate | Source identity, rights, cadence, attribution, and role authority belong in governed source registry/source descriptor records. |
| Deny by default | Rare, protected, culturally sensitive, steward-controlled, or join-sensitive plant records fail closed when sensitivity, rights, review state, or stewardship state is unresolved. |
| Exact geometry stays protected | README/index text must not expose exact rare-plant coordinates, restricted identifiers, transform parameters, consent tokens, revocation tokens, or restricted stewardship detail. |
| Rights and sensitivity stay distinct | Rights clearance does not relax sensitivity; sensitivity review does not replace rights review. |
| Review remains separate | ReviewRecord, steward review, rights-holder review, sensitivity review, and release authority roles must remain visible and not collapse. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Receipt families

The exact receipt subtype layout is not proven by this README. This lane may hold or reference Flora ingest records such as:

| Receipt family | Purpose | Boundary |
|---|---|---|
| RunReceipt | Records governed intake run identity, spec hash, inputs, outputs, policy gates, and verification context. | Does not define Flora object meaning by itself. |
| Ingest receipt / source-intake receipt | Records source head, retrieval, source-role, source descriptor ref, digest, admission decision, and handoff state. | Does not replace RAW payloads or SourceDescriptors. |
| ValidationReport | Records admission-time checks for source role, rights, timestamps, digest, geometry precision, and basic boundary conditions. | Passing intake validation is not proof or release approval. |
| PolicyDecision reference | Records finite policy state for hold, deny, quarantine, allow-to-RAW, allow-to-WORK, or require-review handoff. | Policy authority remains in policy roots. |
| ReviewRecord reference | Records steward, sensitivity, rights, or release-readiness review state where intake reveals sensitive Flora context. | Review support is not ReleaseManifest authority. |
| Correction / rollback support reference | Records intake correction, re-fetch, supersession, stale-source, or rollback support. | Correction and rollback authority remain in release governance. |

---

## Accepted material

Accepted content is limited to Flora ingest receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- source-intake, retrieval, source-head, admission, validation, review-routing, policy-decision, correction-support, rollback-support, and release-support receipt records;
- run IDs, source refs, SourceDescriptor refs, source-role refs, request metadata summaries, retrieval times, source times, observed/valid times where material, input refs, input hashes, output refs, output hashes, object counts, digest refs, evidence refs, policy refs, reviewer refs, validator refs, finite outcomes, reason codes, correction refs, rollback refs, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect ingest receipt state without becoming RAW payloads, source registry authority, proof, catalog, policy, release, public output, rare-plant truth, exact-location authority, rights authority, sensitivity policy, or generated-answer authority.

Do not put raw source payloads, credentials, secrets, private tokens, full API responses, exact rare-plant coordinates, restricted identifiers, private landowner details, consent tokens, revocation tokens, reviewer private notes, culturally/legally restricted details, or unsupported source-as-authority claims into README/index text.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Flora source feeds, occurrence payloads, agency snapshots, source-native records, full API responses, or restricted source payloads | `data/raw/flora/` or governed restricted storage as applicable |
| Work/scratch transformations and normalized candidates | `data/work/flora/` |
| Quarantined source material | `data/quarantine/flora/` |
| Normalized Flora payloads | `data/processed/flora/` and child lanes |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| Pipeline executable logic | `pipelines/domains/flora/` |
| Semantic contracts | `contracts/domains/flora/` |
| Machine schemas | `schemas/contracts/v1/domains/flora/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| ReleaseManifest, promotion decision, CorrectionNotice, RollbackCard, withdrawal notice, signature, or release changelog | `release/` |
| Rights, sensitivity, geoprivacy, source-role, consent, revocation, publication, or release policy | `policy/` and governed policy roots |
| Validator code, fixtures, tests, package code, or CI workflows | `tools/`, `fixtures/`, `tests/`, `packages/`, `.github/workflows/` |
| Public map/API/UI payloads, graph edges, vector-index content, or generated answer text | governed public outputs only after evidence, policy, validation, review, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/ingest/flora/
├── README.md
├── <run_id>/
│   ├── run_receipt.json
│   ├── ingest_receipt.json
│   ├── validation_report.json
│   ├── review_record_ref.json
│   ├── policy_decision_ref.json
│   ├── checksums.sha256
│   ├── signature.bundle
│   └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove files, emitted ingest receipts, source descriptors, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, evidence closure, review workflow, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, source registry, sensitivity-policy authority, exact-location authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records ingest process memory but has not been consumed by downstream proof or release review. |
| Hold | Required refs, source role, rights, timestamps, hashes, source descriptor refs, evidence refs, policy refs, review refs, validation state, correction path, rollback target, or decision scope are incomplete. |
| Deny/abstain | Sensitivity, rights, stewardship, review state, geometry precision, source role, re-identification risk, evidence, policy, or release state remains unresolved. |
| Quarantine/correct | Intake contradicts source metadata, omits required role/time/citation/digest/review state, violates policy, lacks replay/signature support, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite this receipt as intake/validation/review/correction support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, review/policy/validation state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/ingest/flora/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / species page / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. Flora ingest receipts can support proof and release artifacts, but they do not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Flora domain and ingest/source-intake receipt lane.
- [ ] Confirm canonical ingest/domain receipt naming against ADR-S-03 or accepted receipt-layout governance before relying on this path as final layout authority.
- [ ] Confirm receipt ID, run ID, source refs, SourceDescriptor refs, source-role refs, input/output hashes, evidence refs, policy refs, reviewer refs, validator refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm rights, citation, cadence, sensitivity tier, geometry precision, stewardship state, source role, observed/source/retrieval/correction time, caveats, confidence, and limitations are preserved where material.
- [ ] Confirm exact sensitive coordinates, restricted identifiers, transform parameters, consent tokens, revocation tokens, and private review notes are not exposed in README/index text.
- [ ] Confirm ReviewRecord and PolicyDecision references exist where rare/protected/culturally sensitive plant handling, steward-controlled records, rights restrictions, or public-safe derivatives are involved.
- [ ] Confirm EvidenceBundle/proof references resolve before using this ingest receipt in any public Flora claim path.
- [ ] Confirm receipt presence is not treated as source truth, rare-plant truth, exact-location authority, rights authority, sensitivity policy, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm deny/abstain/hold/error/needs-review/quarantine states are recorded when rights, sensitivity, source role, review, evidence, policy, validation, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, species page, generated answer, or map surface uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces a blank placeholder at `data/receipts/ingest/flora/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a blank placeholder before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/ingest/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Flora parent receipt README defines Flora receipts as process memory and not rare-plant truth, exact-location authority, sensitivity policy, proof, release approval, or public artifact authority. | **CONFIRMED by GitHub contents API during this edit** |
| Flora sensitivity doctrine says exact rare, protected, or culturally sensitive plant locations are denied on public surfaces by default and require steward review, generalized or withheld geometry, and RedactionReceipt before public release. | **CONFIRMED by GitHub contents API during this edit** |
| Flora sensitivity doctrine says rights and sensitivity are independent fail-closed gates. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Exact subtype layout under `data/receipts/ingest/flora/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Flora ingest receipt payloads exist under this subtree. | **UNKNOWN** |
| Source descriptors, schemas, validators, fixtures, CI checks, signing, source activation, policy enforcement, evidence closure, review workflow, correction hooks, rollback hooks, DSSE/cosign enforcement, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is raw source data, source registry authority, rare-plant truth, Flora occurrence truth, exact-location authority, rights authority, sensitivity policy, proof, catalog authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../flora/README.md`](../../flora/README.md)
- [`../../flora/redaction/README.md`](../../flora/redaction/README.md)
- [`../../../raw/flora/README.md`](../../../raw/flora/README.md)
- [`../../../work/flora/README.md`](../../../work/flora/README.md)
- [`../../../quarantine/flora/README.md`](../../../quarantine/flora/README.md)
- [`../../../processed/flora/README.md`](../../../processed/flora/README.md)
- [`../../../catalog/domain/flora/README.md`](../../../catalog/domain/flora/README.md)
- [`../../../published/layers/flora/README.md`](../../../published/layers/flora/README.md)
- [`../../../proofs/README.md`](../../../proofs/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)
- [`../../../../docs/domains/flora/SENSITIVITY.md`](../../../../docs/domains/flora/SENSITIVITY.md)
- [`../../../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md`](../../../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md)
- [`../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md`](../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md)
- [`../../../../docs/domains/flora/SOURCE_REGISTRY.md`](../../../../docs/domains/flora/SOURCE_REGISTRY.md)
- [`../../../../contracts/domains/flora/rare_plant_record.md`](../../../../contracts/domains/flora/rare_plant_record.md)
- [`../../../../contracts/domains/flora/flora_occurrence.md`](../../../../contracts/domains/flora/flora_occurrence.md)
- [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../../docs/standards/RUN_RECEIPT.md`](../../../../docs/standards/RUN_RECEIPT.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/ingest/flora/` is a Flora ingest receipt lane for process memory only. It is not raw source data, source registry authority, rare-plant truth, Flora occurrence truth, exact-location authority, rights authority, sensitivity policy, proof, catalog, registry, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
