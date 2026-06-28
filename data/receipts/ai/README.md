<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/ai/readme
name: AI Receipts README
path: data/receipts/ai/README.md
type: data-receipts-ai-family-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <ai-governance-steward>
  - <data-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
receipt_family: ai
artifact_family: ai-receipts
path_posture: ai-receipt-family-root; needs-receipt-layout-verification
sensitivity_posture: receipt-internal; no-public-path; ai-is-interpretive-not-root-truth; evidencebundle-required; no-direct-model-to-public-path; release-blocked
related:
  - ../README.md
  - aggregation/README.md
  - atmosphere/README.md
  - flora/README.md
  - ../../README.md
  - ../../proofs/README.md
  - ../../catalog/README.md
  - ../../published/README.md
  - ../../../release/manifests/README.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/standards/RUN_RECEIPT.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../docs/domains/flora/README.md
  - ../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - ai
  - ai-receipt
  - runtime-response-envelope
  - evidencebundle
  - process-memory
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/receipts/ai/README.md`."
  - "Confirmed child AI receipt README lanes during this edit: `atmosphere/` and `flora/`."
  - "RunReceipt doctrine names AIReceipt as a receipt subclass that inherits envelope discipline."
  - "ADR-0011 is proposed and states receipt != proof != catalog != publication."
  - "README presence confirms documentation only; it does not prove emitted AIReceipt payloads, schemas, validators, fixtures, CI checks, signing, runtime integration, governed API integration, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# AI Receipts

Parent receipt-family index for KFM AI process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Receipt: AI" src="https://img.shields.io/badge/receipt-AI-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Boundary: not truth" src="https://img.shields.io/badge/boundary-not%20truth-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [AI receipt boundary](#ai-receipt-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/ai/` is for AI process memory only. It is not root truth, proof, EvidenceBundle authority, catalog authority, source registry authority, policy authority, release authority, public artifact authority, public API/UI material, model-output authority, or generated-answer authority.

---

## Scope

This directory indexes AIReceipt records and AI receipt sublanes for governed AI assistance across KFM domains.

AI receipts document process context: request identity, model/runtime identity, retrieval context, cited evidence references, policy outcome, response outcome, review state, limitations, and why an AI-assisted runtime answered, abstained, denied, or errored.

AI receipts do **not** prove claims, replace EvidenceBundle support, approve release, authorize public answers, or make generated text evidence. AI is interpretive, and generated language remains downstream of evidence, policy, review, and release state.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. This requested AI receipt family root is:

```text
data/receipts/ai/
```

This README documents the requested family lane without claiming final receipt-layout authority. `AIReceipt` is named by the RunReceipt standard as a receipt subclass, but the exact AI family subfolder convention remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/ai/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Receipt family | AI receipts |
| Path posture | AI receipt family root; exact subtype/domain layout needs verification |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Governed API | `apps/governed-api/`, not this lane |
| Default failure posture | `ABSTAIN`, `DENY`, `HOLD`, or `ERROR` when evidence, policy, rights, sensitivity, release state, model/runtime identity, citation support, review state, correction path, or rollback target is insufficient |

---

## Confirmed child lanes

The child lanes below are confirmed by current-session GitHub fetches. This confirms README/path evidence only; it does **not** prove payloads, schemas, validators, fixtures, CI checks, signing, governed API integration, or release integration.

| Child lane | Status | Boundary |
|---|---|---|
| [`atmosphere/`](atmosphere/README.md) | **CONFIRMED README** | Atmosphere AI process memory; not atmospheric truth, emergency advisory authority, model-output authority, proof, catalog, policy, release, or generated-answer authority. |
| [`flora/`](flora/README.md) | **CONFIRMED README** | Flora AI process memory; not flora truth, exact-location authority, proof, catalog, policy, release, public artifact authority, or generated-answer authority. |

---

## AI receipt boundary

| Rule | Handling |
|---|---|
| AI is interpretive | AI may summarize, compare, explain caveats, draft review notes, and support governed Focus Mode. It is not root truth. |
| EvidenceBundle outranks generated text | AI receipts must preserve evidence references where a response depends on evidence. |
| Runtime outcomes are finite | AI-assisted responses should record `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` where applicable. |
| No direct model-to-public path | Generated language cannot bypass proof, catalog, policy, release, and governed API checks. |
| Policy and sensitivity still bind | AIReceipt presence does not override blocked rights, sensitivity, freshness, privacy, geoprivacy, living-person data, infrastructure detail, emergency-advisory limits, or release state. |
| Receipts are not proof | AI receipts record process memory; proof-side support belongs in `data/proofs/`. |
| Public clients never read receipt lanes directly | Public outputs consume governed APIs and released artifacts, not raw receipt files. |

---

## Accepted material

Accepted content is limited to AI receipt instances and receipt-local sidecars:

- AIReceipt JSON or JSONL records;
- prompt/request references, runtime/model references, run IDs, response IDs, outcome states, policy-decision refs, and review states;
- evidence refs, retrieval refs, catalog refs, release refs, citation refs, redaction refs where applicable, and limitations notes used by the AI process;
- abstain/deny/error rationale where evidence, policy, rights, freshness, sensitivity, precision, or release state blocks an answer;
- checksums, receipt manifests, signatures, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect AI receipt state without becoming proof, catalog, policy, release, public output, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Full source rows, raw payloads, model fields, rasters, vector layers, generated public artifact bytes, or public answer text | Domain lifecycle lanes under `data/raw/`, `data/work/`, `data/processed/`, `data/published/`, or governed API output as applicable |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, withdrawal notice, signature, or release changelog | `release/` |
| Public layers, PMTiles, reports, stories, species pages, API payloads, downloads, or generated public outputs | `data/published/` only after release gates close |
| Domain policy, sensitivity policy, release policy, or AI-answer policy | `policy/` and governed policy roots |
| Receipt schemas or semantic contracts | `schemas/` and `contracts/` |
| Validator code, fixtures, tests, or CI workflows | `tools/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Emergency instructions, exact protected locations, private person data, or other denied public content | Owning governed domain/policy/release lanes; never this receipt family by itself |

---

## Directory map

```text
data/receipts/ai/
├── README.md
├── atmosphere/
│   └── README.md
├── flora/
│   └── README.md
├── <future-domain>/
│   └── README.md
└── index.local.json
```

Future domain child lanes must be created only after path and receipt-layout review. `index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | AI receipt records process memory but has not been consumed by downstream review. |
| Hold | Evidence refs, policy outcome, runtime identity, response outcome, review state, citation support, or required limitation notes are incomplete. |
| Quarantine/correct | Receipt contradicts evidence, omits required limitations, violates policy, or points to unsupported outputs. |
| Reference from proof | Only when proof-side objects cite an AI receipt as process support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, correction path, and rollback target. |

---

## Forbidden shortcut

```text
data/receipts/ai/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / species page / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. An AI receipt can support review, proof, and release artifacts, but it does not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the AI receipt family and a documented domain child lane.
- [ ] Confirm canonical AI receipt family and subtype naming against ADR-S-03 or the accepted receipt-layout ADR before relying on this path as final authority.
- [ ] Confirm receipt ID, run ID, prompt/request ref, model/runtime ref, response outcome, evidence refs, policy refs, citation refs, timestamps, and review state are present where applicable.
- [ ] Confirm EvidenceBundle/proof references resolve before using AI output in any public claim path.
- [ ] Confirm AI output is not treated as truth, proof, catalog closure, release approval, public artifact authority, or direct answer authority.
- [ ] Confirm domain-specific deny/abstain rules are preserved, including exact protected locations, emergency advisory context, living-person data, and other sensitivity or rights blocks where applicable.
- [ ] Confirm abstain/deny/error outcomes are recorded when evidence, precision, policy, rights, sensitivity, freshness, or release state blocks an answer.
- [ ] Confirm receipt payloads are immutable or hash-bound and do not overwrite prior receipt records in place.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, or generated answer uses this receipt family as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/receipts/ai/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Confirmed child AI receipt README lanes during this edit: `atmosphere/` and `flora/`. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard names `AIReceipt` as a receipt subclass. | **CONFIRMED by GitHub contents API during this edit** |
| Child README presence proves emitted AIReceipt payloads, schemas, validators, fixtures, CI checks, signing, governed API integration, or release integration. | **DENY** |
| Exact AI receipt family layout under `data/receipts/ai/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual AI receipt payloads exist under this subtree. | **UNKNOWN** |
| Schemas, validators, fixtures, CI checks, signing, DSSE/cosign enforcement, governed API integration, and release integration are wired for this exact family root. | **NEEDS VERIFICATION** |
| This README is root truth, proof, catalog authority, registry authority, policy authority, release authority, public artifact authority, model-output authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`aggregation/README.md`](aggregation/README.md)
- [`atmosphere/README.md`](atmosphere/README.md)
- [`flora/README.md`](flora/README.md)
- [`../../README.md`](../../README.md)
- [`../../proofs/README.md`](../../proofs/README.md)
- [`../../catalog/README.md`](../../catalog/README.md)
- [`../../published/README.md`](../../published/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)
- [`../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../docs/standards/RUN_RECEIPT.md`](../../../docs/standards/RUN_RECEIPT.md)
- [`../../../docs/domains/atmosphere/README.md`](../../../docs/domains/atmosphere/README.md)
- [`../../../docs/domains/flora/README.md`](../../../docs/domains/flora/README.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/ai/` is an AI receipt family lane for process memory only. It is not root truth, proof, catalog, registry, policy, release, publication, public artifact authority, model-output authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
