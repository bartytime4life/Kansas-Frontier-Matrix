<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/people-dna-land/readme
name: People DNA Land Receipts README
path: data/receipts/people-dna-land/README.md
type: data-receipts-domain-parent-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <people-dna-land-domain-steward>
  - <privacy-reviewer>
  - <consent-reviewer>
  - <sensitivity-reviewer>
  - <rights-holder-representative>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: people-dna-land-receipts
receipt_scope: people-dna-land-process-memory
domain: people-dna-land
path_posture: domain-receipt-parent-lane; no-child-receipt-lanes-confirmed; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; T4-default; living-person-deny-default; raw-DNA-non-public; private-person-parcel-join-deny-default; consent-and-revocation-required; review-required; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../raw/people-dna-land/README.md
  - ../../work/people-dna-land/README.md
  - ../../quarantine/people-dna-land/README.md
  - ../../quarantine/people-dna-land/land-ownership/README.md
  - ../../processed/people-dna-land/README.md
  - ../../catalog/domain/people-dna-land/land-ownership/README.md
  - ../../published/people-dna-land/README.md
  - ../../published/layers/people-dna-land/README.md
  - ../../proofs/README.md
  - ../../../release/manifests/README.md
  - ../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../../docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md
  - ../../../docs/domains/people-dna-land/DATA_LIFECYCLE.md
  - ../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../../docs/domains/people-dna-land/API_CONTRACTS.md
  - ../../../docs/domains/people-dna-land/sublanes/people.md
  - ../../../docs/domains/people-dna-land/sublanes/genealogy.md
  - ../../../docs/domains/people-dna-land/sublanes/dna.md
  - ../../../docs/domains/people-dna-land/sublanes/land.md
  - ../../../contracts/domains/people-dna-land/README.md
  - ../../../contracts/domains/people-dna-land/domain_validation_report.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - people-dna-land
  - people
  - genealogy
  - dna
  - land-ownership
  - living-person
  - consent
  - revocation
  - privacy
  - title
  - parcel
  - person-parcel-join
  - process-memory
  - review-record
  - redaction-receipt
  - aggregation-receipt
  - validation-report
  - policy-decision
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/receipts/people-dna-land/README.md`."
  - "No substantive child receipt README lanes under `data/receipts/people-dna-land/` were confirmed during this edit."
  - "People/DNA/Land sensitivity doctrine says living-person identity, DNA/genomic material, and private person-parcel joins are denied by default."
  - "Assessor/tax records and parcel geometry are not title truth; receipts may record process state but cannot create title, identity, genealogy, DNA, consent, or ownership truth."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "README presence confirms documentation only; it does not prove emitted receipt payloads, source descriptors, consent systems, schemas, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People/DNA/Land Receipts

Domain parent receipt lane for People/DNA/Land process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Domain: people-dna-land" src="https://img.shields.io/badge/domain-people--dna--land-6f42c1">
  <img alt="Sensitivity: T4 default" src="https://img.shields.io/badge/sensitivity-T4%20default-critical">
  <img alt="Access: no public path" src="https://img.shields.io/badge/access-no%20public%20path-b83232">
  <img alt="Boundary: not proof" src="https://img.shields.io/badge/boundary-not%20proof-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Receipt boundary](#receipt-boundary) · [Receipt families](#receipt-families) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/people-dna-land/` is for People/DNA/Land receipt process memory only. It is not living-person truth, identity truth, genealogy truth, DNA/genomic truth, consent authority, title authority, parcel-boundary authority, land-ownership truth, proof, EvidenceBundle authority, catalog authority, source registry authority, policy authority, release authority, public artifact authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory is the People/DNA/Land-domain parent lane for receipts that document governed process memory: source intake support, validation support, sensitivity review support, consent/revocation support, redaction/generalization support, aggregation support, chain-of-title review support, correction support, rollback support, and release-candidate support.

People/DNA/Land receipts record what a process did, what references it inspected, what outcome or decision class it produced, what evidence, policy, consent, review, source-role, validation, redaction, correction, rollback, or release-candidate references should travel downstream, and what conditions block use.

Receipts do **not** prove a person identity, genealogy relationship, DNA relationship, land ownership assertion, title assertion, parcel boundary, consent state, release state, or legal conclusion. They also do not approve public release or replace SourceDescriptors, contracts, schemas, ReviewRecords, ConsentGrants, RevocationReceipts, PolicyDecisions, EvidenceBundles, ProofPacks, CatalogMatrix records, ReleaseManifests, CorrectionNotices, RollbackCards, or governed-public API output.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This People/DNA/Land domain parent lane is:

```text
data/receipts/people-dna-land/
```

No substantive child receipt README lanes under this parent were confirmed during this edit. Exact receipt subtype layout under this parent remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/people-dna-land/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Domain lane | people-dna-land |
| Scope | People/DNA/Land process memory across intake, validation, consent/revocation, sensitivity review, redaction, aggregation, title/parcel role checks, correction, rollback, and release-support steps |
| Path posture | domain receipt parent lane; exact subtype layout needs verification |
| Confirmed child receipt lanes | None confirmed during this edit |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Lifecycle payload lanes | `data/raw/people-dna-land/`, `data/work/people-dna-land/`, `data/quarantine/people-dna-land/`, `data/processed/people-dna-land/` where applicable |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Source registry authority | `data/registry/sources/`, not this lane |
| Policy authority | `policy/consent/`, `policy/sensitivity/`, `policy/geoprivacy/`, and other policy roots, not this lane |
| Contract authority | `contracts/domains/people-dna-land/`, not this lane |
| Schema authority | `schemas/`, not this lane |
| Default failure posture | `DENY`, `ABSTAIN`, `HOLD`, `RESTRICT`, `NEEDS_REVIEW`, `ERROR`, or `QUARANTINE` when living-person status, DNA/genomic status, consent, revocation, rights, sensitivity, source role, evidence refs, review state, title/parcel role, correction path, rollback target, or release state is insufficient |

---

## Confirmed child lanes

No child receipt README lanes were confirmed under `data/receipts/people-dna-land/` during this edit.

| Child lane | Status | Notes |
|---|---|---|
| `land-ownership/` | **UNKNOWN** | A matching receipt child README was not found during this edit. Related raw, quarantine, catalog, published, and package land-ownership lanes exist elsewhere. |
| `consent/` | **UNKNOWN** | Not confirmed by current-session repo evidence. |
| `redaction/` | **UNKNOWN** | Not confirmed by current-session repo evidence. |
| `validation/` | **UNKNOWN** | Not confirmed by current-session repo evidence. |
| `dna/` | **UNKNOWN** | Not confirmed by current-session repo evidence. |

This confirms only current README/path evidence. It does **not** prove emitted receipts, schemas, validators, fixtures, CI checks, signing, consent enforcement, revocation hooks, source activation, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration.

---

## Receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records what governed People/DNA/Land processes did; it is not the truth source. |
| Deny by default | Living-person, DNA/genomic, private person-parcel joins, and unresolved consent/sensitivity contexts fail closed. |
| Raw DNA never becomes public through a receipt | Raw DNA kit identifiers, vendor identifiers, and segment data are not public artifacts and are not made safe by this lane. |
| Consent remains enforceable and separate | Consent, revocation, scope, purpose, expiry, and embargo authority belong in policy/consent and accepted consent-control lanes, not this README. |
| Private person-parcel joins stay restricted | Receipts must not turn identity/land joins into public facts. Public-safe derivatives require review, policy, proof, release, correction, and rollback support. |
| Assessor/tax records are not title truth | Administrative property records and parcel geometry do not establish title, ownership certification, or legal boundary truth. |
| Relationships stay assertion-first | Genealogy and DNA-derived relationship hypotheses remain claims with source-role and evidence limits; receipts do not make them canonical truth. |
| Review remains separate | ReviewRecord, privacy review, consent review, rights review, steward review, and release authority roles must remain visible and not collapse. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and domain discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decisions, CorrectionNotice, RollbackCard, and signatures belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Receipt families

The exact receipt subtype layout is not proven by this README. This parent lane may hold or reference People/DNA/Land receipt records such as:

| Receipt family | Purpose | Boundary |
|---|---|---|
| RunReceipt | Records governed run identity, spec hash, inputs, outputs, policy gates, and verification context. | Does not define person, DNA, genealogy, or land object meaning by itself. |
| ValidationReport | Records source-role, living-person, consent, revocation, DNA, title/parcel, schema, and release-readiness validation outcomes. | Passing validation is not proof or release approval. |
| ReviewRecord | Records privacy, consent, sensitivity, rights, steward, title, or release-readiness review state. | Review support is not ReleaseManifest authority. |
| PolicyDecision | Records finite policy state for hold, deny, restrict, quarantine, allow-to-work, or allow-to-release-candidate decisions. | Policy authority remains in policy roots. |
| RedactionReceipt | Records public-safe generalization or de-identification support. | Does not make sensitive source detail public by itself. |
| AggregationReceipt | Records aggregate-only derivative support. | Does not permit re-identifying source reconstruction. |
| Consent / revocation receipt reference | Records consent or revocation process support where accepted by policy. | Consent authority remains in consent-control lanes and policy roots. |
| CorrectionNotice / RollbackCard reference | Records correction or rollback support when public-safe derivatives must be demoted, withdrawn, invalidated, or regenerated. | Correction and rollback authority remain in release governance. |

---

## Accepted material

Accepted content is limited to People/DNA/Land receipt instances and receipt-local sidecars:

- run receipt JSON or JSONL records;
- intake, validation, review, consent-reference, revocation-reference, redaction, aggregation, policy-decision, correction-support, rollback-support, and release-support receipt records;
- run IDs, source refs, object refs, assertion refs, consent refs, revocation refs, policy refs, reviewer refs, evidence refs, validation refs, input/output hashes, source-role refs, finite outcomes, reason codes, correction refs, rollback refs, timestamps, actor/runner identity, status fields, and signatures;
- receipt manifests, checksums, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect receipt state without becoming proof, catalog, policy, release, public output, identity truth, DNA truth, genealogy truth, title truth, parcel-boundary truth, consent authority, or generated-answer authority.

Do not put raw DNA, kit identifiers, segment data, living-person private fields, private person-parcel joins, contactable-person details, consent tokens, revocation tokens, private reviewer notes, restricted source payloads, legal conclusions, title certifications, or exact private land/person relationship detail into README/index text.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw source captures, genealogy uploads, DNA files, kit IDs, segments, source mirrors, or restricted source payloads | `data/raw/people-dna-land/` or governed restricted storage as applicable |
| Work files, candidates, unresolved identities, joins, consent drafts, review drafts, or transform experiments | `data/work/people-dna-land/` |
| Quarantined, rights-unclear, consent-unclear, sensitivity-unclear, or policy-held material | `data/quarantine/people-dna-land/` |
| Canonical processed People/DNA/Land objects | `data/processed/people-dna-land/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, CorrectionNotice, RollbackCard, withdrawal notice, signature, or release changelog | `release/` |
| Rights, consent, revocation, sensitivity, geoprivacy, source-role, privacy, title, publication, or release policy | `policy/` and governed policy roots |
| Semantic contracts | `contracts/domains/people-dna-land/` |
| Machine schemas | `schemas/` |
| Validator code, fixtures, tests, package code, or CI workflows | `tools/`, `fixtures/`, `tests/`, `packages/`, `.github/workflows/` |
| Published public-safe artifacts or layers | `data/published/people-dna-land/` or `data/published/layers/people-dna-land/` only after release gates close |
| Legal advice, title certification, identity certification, genetic relationship certification, or ownership certification | Not a KFM receipt-lane function; route to governed review or abstain |
| Public map/API/UI payloads, graph edges, vector-index content, or generated answer text | governed public outputs only after evidence, policy, validation, review, release, correction, and rollback gates close |

---

## Directory map

```text
data/receipts/people-dna-land/
├── README.md
└── index.local.json
```

This map confirms the parent README lane currently documented. It does not prove emitted receipt payloads, schemas, validators, fixtures, CI checks, signing, consent enforcement, revocation hooks, source activation, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, source registry, consent authority, sensitivity-policy authority, exact-location authority, title authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | Receipt records process memory but has not been consumed by downstream proof or release review. |
| Hold | Required refs, hashes, source-role refs, consent refs, review refs, evidence refs, policy refs, validation state, correction path, rollback target, or decision scope are incomplete. |
| Deny/abstain | Living-person exposure, DNA/genomic exposure, private person-parcel join, unresolved rights, unresolved consent, unresolved revocation, unresolved source role, insufficient evidence, or missing release state remains unresolved. |
| Quarantine/correct | Receipt contradicts evidence, omits required limits, collapses source roles, lacks replay/signature support, violates policy, or points to outputs that cannot be reconciled. |
| Reference from proof | Only when proof-side objects cite this receipt as process/validation/review/redaction/aggregation/correction support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, consent/revocation state, review/policy/validation state, correction path, rollback target, and ReleaseManifest support. |

---

## Forbidden shortcut

```text
data/receipts/people-dna-land/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / person page / genealogy page / title view / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. People/DNA/Land receipts can support proof and release artifacts, but they do not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the People/DNA/Land domain and a documented receipt subtype.
- [ ] Confirm canonical domain/receipt subtype naming against ADR-S-03 or accepted receipt-layout governance before relying on this parent as final layout authority.
- [ ] Confirm receipt ID, run ID, source refs, object refs, assertion refs, consent refs, revocation refs, input/output hashes, evidence refs, policy refs, reviewer refs, validator refs, timestamps, actor/runner identity, status fields, and signatures are present where applicable.
- [ ] Confirm living-person status, DNA/genomic status, source role, rights, consent scope, revocation state, embargo state, sensitivity tier, title/parcel role, time facets, caveats, confidence, and limitations are preserved where material.
- [ ] Confirm raw DNA, kit identifiers, segment data, living-person private fields, private person-parcel joins, contactable-person details, consent tokens, revocation tokens, private reviewer notes, restricted source payloads, and exact private land/person relationship detail are not exposed in README/index text.
- [ ] Confirm ReviewRecord and PolicyDecision references exist where living-person, DNA/genomic, private person-parcel, rights, consent, title, or public-safe derivative handling is involved.
- [ ] Confirm EvidenceBundle/proof references resolve before using receipts in any public People/DNA/Land claim path.
- [ ] Confirm receipt presence is not treated as identity truth, genealogy truth, DNA truth, title truth, land-ownership truth, parcel-boundary truth, consent authority, policy authority, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm deny/abstain/hold/restrict/error/needs-review/quarantine states are recorded when consent, revocation, rights, sensitivity, source role, review, evidence, policy, validation, infrastructure, or release state blocks use.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, map surface, person page, genealogy page, title view, generated answer, legal conclusion, identity certification, ownership certification, or DNA relationship statement uses this receipt parent lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/receipts/people-dna-land/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| No substantive child receipt README lanes under `data/receipts/people-dna-land/` were confirmed during this edit. | **CONFIRMED by GitHub fetch/search during this edit / limited to current evidence** |
| People/DNA/Land sensitivity doctrine says living-person identity, DNA/genomic material, and private person-parcel joins are denied by default. | **CONFIRMED by GitHub contents API during this edit** |
| People/DNA/Land sensitivity doctrine says assessor/tax records and parcel geometry do not establish title truth. | **CONFIRMED by GitHub contents API during this edit** |
| People/DNA/Land quarantine and published lanes both preserve no-public/deny-by-default boundaries for unresolved living-person, DNA, consent, private join, title, and parcel-boundary risk. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard says governed runs emit receipts, receipt placement is `data/receipts/`, and fail-closed verification is required before promotion. | **CONFIRMED by GitHub contents API during this edit** |
| People/DNA/Land receipt README presence proves emitted receipt payloads, source descriptors, consent systems, schemas, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, or release integration. | **DENY** |
| Exact subtype layout under `data/receipts/people-dna-land/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual People/DNA/Land receipt payloads exist under this subtree. | **UNKNOWN** |
| This README is living-person truth, identity truth, genealogy truth, DNA/genomic truth, consent authority, title authority, parcel-boundary authority, land-ownership truth, proof, catalog authority, source registry authority, policy authority, release authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../raw/people-dna-land/README.md`](../../raw/people-dna-land/README.md)
- [`../../work/people-dna-land/README.md`](../../work/people-dna-land/README.md)
- [`../../quarantine/people-dna-land/README.md`](../../quarantine/people-dna-land/README.md)
- [`../../quarantine/people-dna-land/land-ownership/README.md`](../../quarantine/people-dna-land/land-ownership/README.md)
- [`../../processed/people-dna-land/README.md`](../../processed/people-dna-land/README.md)
- [`../../catalog/domain/people-dna-land/land-ownership/README.md`](../../catalog/domain/people-dna-land/land-ownership/README.md)
- [`../../published/people-dna-land/README.md`](../../published/people-dna-land/README.md)
- [`../../published/layers/people-dna-land/README.md`](../../published/layers/people-dna-land/README.md)
- [`../../proofs/README.md`](../../proofs/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md`](../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md)
- [`../../../docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md`](../../../docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md)
- [`../../../docs/domains/people-dna-land/DATA_LIFECYCLE.md`](../../../docs/domains/people-dna-land/DATA_LIFECYCLE.md)
- [`../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md`](../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md)
- [`../../../docs/domains/people-dna-land/API_CONTRACTS.md`](../../../docs/domains/people-dna-land/API_CONTRACTS.md)
- [`../../../docs/domains/people-dna-land/sublanes/people.md`](../../../docs/domains/people-dna-land/sublanes/people.md)
- [`../../../docs/domains/people-dna-land/sublanes/genealogy.md`](../../../docs/domains/people-dna-land/sublanes/genealogy.md)
- [`../../../docs/domains/people-dna-land/sublanes/dna.md`](../../../docs/domains/people-dna-land/sublanes/dna.md)
- [`../../../docs/domains/people-dna-land/sublanes/land.md`](../../../docs/domains/people-dna-land/sublanes/land.md)
- [`../../../contracts/domains/people-dna-land/README.md`](../../../contracts/domains/people-dna-land/README.md)
- [`../../../contracts/domains/people-dna-land/domain_validation_report.md`](../../../contracts/domains/people-dna-land/domain_validation_report.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/people-dna-land/` is a People/DNA/Land receipt parent lane for process memory only. It is not living-person truth, identity truth, genealogy truth, DNA/genomic truth, consent authority, title authority, parcel-boundary authority, land-ownership truth, proof, catalog, registry, policy, release, publication, public artifact authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
