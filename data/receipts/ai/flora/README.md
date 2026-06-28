<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/ai/flora/readme
name: Flora AI Receipts README
path: data/receipts/ai/flora/README.md
type: data-receipts-ai-domain-lane-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <ai-governance-steward>
  - <flora-domain-steward>
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
domain: flora
artifact_family: flora-ai-receipts
path_posture: ai-domain-receipt-lane; parent-ai-receipt-root-still-stub; needs-receipt-layout-verification
sensitivity_posture: receipt-internal; no-public-path; ai-is-interpretive-not-root-truth; exact-sensitive-geometry-deny-default; evidencebundle-required; redaction-receipt-required-for-public-sensitive-transforms; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../aggregation/README.md
  - ../../../README.md
  - ../../../raw/flora/README.md
  - ../../../processed/flora/README.md
  - ../../../proofs/README.md
  - ../../../catalog/domain/flora/README.md
  - ../../../published/layers/flora/README.md
  - ../../../../release/manifests/README.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/standards/RUN_RECEIPT.md
  - ../../../../docs/domains/flora/README.md
  - ../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - ../../../../docs/domains/flora/source-families.md
  - ../../../../docs/domains/flora/sensitivity-posture.md
  - ../../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - ai
  - ai-receipt
  - flora
  - biodiversity
  - rare-plant
  - geoprivacy
  - evidencebundle
  - redaction-receipt
  - runtime-response-envelope
  - process-memory
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/receipts/ai/flora/README.md`."
  - "Parent `data/receipts/ai/README.md` is currently a greenfield stub."
  - "RunReceipt doctrine names AIReceipt as a receipt subclass that inherits envelope discipline."
  - "Flora doctrine says AI is interpretive, EvidenceBundle outranks generated language, and every Focus Mode answer emits an AIReceipt and RuntimeResponseEnvelope."
  - "Flora doctrine denies exact rare/protected/culturally sensitive plant locations on public surfaces by default; public transforms require review, generalized/withheld geometry, and a RedactionReceipt."
  - "README presence confirms documentation only; it does not prove emitted AIReceipt payloads, schemas, validators, fixtures, CI checks, signing, runtime integration, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora AI Receipts

AI receipt lane for Flora-domain AI process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Receipt: AI" src="https://img.shields.io/badge/receipt-AI-7048e8">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-2e7d32">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Boundary: not truth" src="https://img.shields.io/badge/boundary-not%20truth-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [AI receipt boundary](#ai-receipt-boundary) · [Flora boundaries](#flora-boundaries) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/ai/flora/` is for Flora AI process memory only. It is not flora truth, proof, EvidenceBundle authority, catalog authority, source registry authority, policy authority, release authority, public artifact authority, exact-location authority, public API/UI material, model-output authority, or generated-answer authority.

---

## Scope

This directory is for AIReceipt records created when AI assists Flora-domain work: summarizing released Flora EvidenceBundles, comparing botanical evidence across sources, drafting steward-review notes, explaining taxonomic or geoprivacy caveats, producing bounded Focus Mode support, or recording why a runtime response answered, abstained, denied, or errored.

AI receipts document process context. They may record prompt/request identity, model/runtime identity, retrieval context, cited evidence references, policy outcome, response outcome, review state, redaction posture, and limitations. They do **not** prove a Flora claim, replace EvidenceBundle support, approve release, or authorize direct public answers.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested path is an AI receipt family sublane scoped to the Flora domain:

```text
data/receipts/ai/flora/
```

This README documents the requested lane without claiming final receipt-layout authority. The parent `data/receipts/ai/README.md` is still a greenfield stub, and exact AI receipt subfolder naming remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/ai/flora/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Receipt family | AI receipts |
| Domain lane | flora |
| Path posture | requested AI domain receipt lane; exact subtype layout needs verification |
| Parent root | `data/receipts/ai/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Lifecycle payloads | `data/raw/flora/`, `data/work/flora/`, `data/processed/flora/` |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Default failure posture | `ABSTAIN`, `DENY`, `HOLD`, or `ERROR` when evidence, policy, rights, sensitivity, exact-location exposure, release state, model/runtime identity, citation support, review state, redaction receipt, correction path, or rollback target is insufficient |

---

## AI receipt boundary

| Rule | Handling |
|---|---|
| AI is interpretive | AI may summarize, compare, explain caveats, and draft review notes; it is not root truth. |
| EvidenceBundle outranks generated text | AI receipts must preserve evidence references where a response depends on evidence. |
| Runtime outcomes are finite | Flora AI responses should record `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` where applicable. |
| No direct model-to-public path | Generated language cannot bypass proof, catalog, release, redaction, and governed API checks. |
| Geoprivacy still binds | AIReceipt presence does not override rare-plant, protected-plant, cultural-sensitivity, rights, or release restrictions. |
| Receipts are not proof | AI receipts record process memory; proof-side support belongs in `data/proofs/`. |
| Public clients never read receipt lanes directly | Public outputs consume governed APIs and released artifacts, not raw receipt files. |

---

## Flora boundaries

| Flora condition | AI receipt handling | Boundary |
|---|---|---|
| Evidence summary | Record evidence refs, release refs, limits, and response outcome. | Summary is not flora truth without resolved evidence support. |
| Taxonomy or specimen explanation | Record authority/source refs, caveats, and disagreement notes where used. | AI does not settle taxonomic conflict by generation. |
| Rare/protected/culturally sensitive plant context | Record deny/abstain basis, review state, and any redaction-reference used. | Exact sensitive geometry is denied on public surfaces by default. |
| Public-safe generalized layer explanation | Record RedactionReceipt, ReleaseManifest, evidence refs, and residual caveats where available. | Generalized output does not imply exact-location access. |
| Community-science or herbarium evidence | Record source role, rights status, snapshot/DOI, and citation limitations. | Observation context does not become authoritative claim without proof. |
| Cross-domain context | Record owning domain refs and limitations. | Flora does not become Habitat, Fauna, Soil, Hydrology, Agriculture, Hazard, Archaeology, or People/Land authority. |
| Unsupported prompt | Record abstain/deny/error basis. | Missing evidence, blocked policy, unclear rights, stale state, precision mismatch, or exact-location requests must not be filled by generation. |

---

## Accepted material

Accepted content is limited to Flora AI receipt instances and receipt-local sidecars:

- AIReceipt JSON or JSONL records for Flora runs;
- prompt/request references, runtime/model references, run IDs, response IDs, outcome states, policy-decision refs, and review states;
- evidence refs, retrieval refs, catalog refs, release refs, redaction refs, citation refs, and limitations notes used by the AI process;
- abstain/deny/error rationale where evidence, policy, rights, freshness, sensitivity, exact-location exposure, or release state blocks an answer;
- checksums, receipt manifests, signatures, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect AI receipt state without becoming proof, catalog, policy, release, public output, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Full source rows, herbarium payloads, observation payloads, specimen records, rasters, exact geometry, or generated public layer bytes | Flora lifecycle lanes under `data/raw/`, `data/work/`, `data/processed/`, or `data/published/` as applicable |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, withdrawal notice, signature, or release changelog | `release/` |
| Public layers, PMTiles, reports, species pages, API payloads, downloads, or generated public outputs | `data/published/` only after release gates close |
| Flora policy, geoprivacy policy, rare-species policy, source-rights policy, or AI-answer policy | `policy/` and governed policy roots |
| Receipt schemas or semantic contracts | `schemas/` and `contracts/` |
| Validator code, fixtures, tests, or CI workflows | `tools/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Exact rare/protected/culturally sensitive plant locations for public use | Steward-only governed access or denied/generalized derivatives, never this receipt lane |

---

## Directory map

```text
data/receipts/ai/flora/
├── README.md
├── <run_id>/
│   ├── ai_receipt.json
│   ├── checksums.sha256
│   ├── signature.bundle
│   └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove files, emitted receipts, schemas, validators, fixtures, CI checks, signing, governed API integration, geoprivacy enforcement, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, exact-location authority, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | AI receipt records process memory but has not been consumed by downstream review. |
| Hold | Evidence refs, policy outcome, runtime identity, response outcome, review state, redaction state, or citation support is incomplete. |
| Quarantine/correct | Receipt contradicts evidence, omits required limitations, violates geoprivacy or rights policy, or points to unsupported outputs. |
| Reference from proof | Only when proof-side objects cite this receipt as process support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, redaction/correction path, and rollback target. |

---

## Forbidden shortcut

```text
data/receipts/ai/flora/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / species page / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. An AI receipt can support review, proof, and release artifacts, but it does not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the AI receipt family and the Flora domain lane.
- [ ] Confirm canonical AI receipt subtype naming against ADR-S-03 or the accepted receipt-layout ADR before relying on this path as final authority.
- [ ] Confirm receipt ID, run ID, prompt/request ref, model/runtime ref, response outcome, evidence refs, policy refs, citation refs, timestamps, redaction refs, and review state are present where applicable.
- [ ] Confirm EvidenceBundle/proof references resolve before using the AI output in any public claim path.
- [ ] Confirm AI output is not treated as flora truth, exact-location authority, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm exact rare/protected/culturally sensitive plant geometry is denied, withheld, or generalized before public use and backed by review plus RedactionReceipt where applicable.
- [ ] Confirm abstain/deny/error outcomes are recorded when evidence, precision, policy, rights, sensitivity, freshness, exact-location exposure, or release state blocks an answer.
- [ ] Confirm receipt payloads are immutable or hash-bound and do not overwrite prior receipt records in place.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, or generated answer uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/receipts/ai/flora/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/ai/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard names `AIReceipt` as a receipt subclass. | **CONFIRMED by GitHub contents API during this edit** |
| Flora doctrine says AI is interpretive, EvidenceBundle outranks generated language, and every Focus Mode answer emits an AIReceipt and RuntimeResponseEnvelope. | **CONFIRMED by GitHub contents API during this edit** |
| Flora doctrine denies exact rare/protected/culturally sensitive plant locations on public surfaces by default and requires review, generalized/withheld geometry, and RedactionReceipt for allowed public transforms. | **CONFIRMED by GitHub contents API during this edit** |
| Exact subtype layout under `data/receipts/ai/flora/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Flora AI receipt payloads exist under this subtree. | **UNKNOWN** |
| Schemas, validators, fixtures, CI checks, signing, DSSE/cosign enforcement, governed API integration, geoprivacy enforcement, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is flora truth, proof, catalog authority, registry authority, policy authority, release authority, public artifact authority, exact-location authority, model-output authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../aggregation/README.md`](../../aggregation/README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../raw/flora/README.md`](../../../raw/flora/README.md)
- [`../../../processed/flora/README.md`](../../../processed/flora/README.md)
- [`../../../proofs/README.md`](../../../proofs/README.md)
- [`../../../catalog/domain/flora/README.md`](../../../catalog/domain/flora/README.md)
- [`../../../published/layers/flora/README.md`](../../../published/layers/flora/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)
- [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../../docs/standards/RUN_RECEIPT.md`](../../../../docs/standards/RUN_RECEIPT.md)
- [`../../../../docs/domains/flora/README.md`](../../../../docs/domains/flora/README.md)
- [`../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md`](../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md)
- [`../../../../docs/domains/flora/source-families.md`](../../../../docs/domains/flora/source-families.md)
- [`../../../../docs/domains/flora/sensitivity-posture.md`](../../../../docs/domains/flora/sensitivity-posture.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/ai/flora/` is a Flora AI receipt lane for process memory only. It is not flora truth, proof, catalog, registry, policy, release, publication, exact-location authority, public artifact authority, model-output authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
