<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/ai/atmosphere/readme
name: Atmosphere AI Receipts README
path: data/receipts/ai/atmosphere/README.md
type: data-receipts-ai-domain-lane-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <ai-governance-steward>
  - <atmosphere-domain-steward>
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
domain: atmosphere
artifact_family: atmosphere-ai-receipts
path_posture: ai-domain-receipt-lane; parent-ai-receipt-root-still-stub; needs-receipt-layout-verification
sensitivity_posture: receipt-internal; no-public-path; ai-is-interpretive-not-root-truth; no-direct-model-to-public-path; evidencebundle-required; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../aggregation/README.md
  - ../../../README.md
  - ../../../raw/atmosphere/README.md
  - ../../../processed/atmosphere/README.md
  - ../../../proofs/README.md
  - ../../../catalog/domain/atmosphere/README.md
  - ../../../published/layers/atmosphere/README.md
  - ../../../../release/manifests/README.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/standards/RUN_RECEIPT.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../../docs/domains/atmosphere/VERIFICATION_BACKLOG.md
  - ../../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - ai
  - ai-receipt
  - atmosphere
  - air
  - climate
  - smoke
  - weather
  - evidencebundle
  - runtime-response-envelope
  - process-memory
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/receipts/ai/atmosphere/README.md`."
  - "Parent `data/receipts/ai/README.md` is currently a greenfield stub."
  - "RunReceipt doctrine names AIReceipt as a receipt subclass that inherits envelope discipline."
  - "Atmosphere doctrine says AI is interpretive, must abstain or deny where evidence or policy requires it, and must not bypass EvidenceBundle resolution or the trust membrane."
  - "README presence confirms documentation only; it does not prove emitted AIReceipt payloads, schemas, validators, fixtures, CI checks, signing, runtime integration, or release integration."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere AI Receipts

AI receipt lane for Atmosphere-domain AI process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Receipt: AI" src="https://img.shields.io/badge/receipt-AI-7048e8">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-1f9eda">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Boundary: not truth" src="https://img.shields.io/badge/boundary-not%20truth-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [AI receipt boundary](#ai-receipt-boundary) · [Atmosphere boundaries](#atmosphere-boundaries) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/ai/atmosphere/` is for Atmosphere AI process memory only. It is not atmospheric truth, proof, EvidenceBundle authority, catalog authority, source registry authority, policy authority, release authority, public artifact authority, emergency advisory authority, public API/UI material, model-output authority, or generated-answer authority.

---

## Scope

This directory is for AIReceipt records created when AI assists Atmosphere-domain work: summarizing released EvidenceBundles, comparing evidence across sources, drafting steward-review notes, explaining caveats, producing bounded Focus Mode support, or recording why a runtime response answered, abstained, denied, or errored.

AI receipts document process context. They may record prompt/request identity, model/runtime identity, retrieval context, cited evidence references, policy outcome, response outcome, review state, and limitations. They do **not** prove an Atmosphere claim, replace EvidenceBundle support, approve release, or authorize direct public answers.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested path is an AI receipt family sublane scoped to the Atmosphere domain:

```text
data/receipts/ai/atmosphere/
```

This README documents the requested lane without claiming final receipt-layout authority. The parent `data/receipts/ai/README.md` is still a greenfield stub, and exact AI receipt subfolder naming remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/ai/atmosphere/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Receipt family | AI receipts |
| Domain lane | atmosphere |
| Path posture | requested AI domain receipt lane; exact subtype layout needs verification |
| Parent root | `data/receipts/ai/` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Lifecycle payloads | `data/raw/atmosphere/`, `data/work/atmosphere/`, `data/processed/atmosphere/` |
| Proof authority | `data/proofs/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, not this lane |
| Default failure posture | `ABSTAIN`, `DENY`, `HOLD`, or `ERROR` when evidence, policy, rights, sensitivity, release state, model/runtime identity, citation support, review state, correction path, or rollback target is insufficient |

---

## AI receipt boundary

| Rule | Handling |
|---|---|
| AI is interpretive | AI may summarize, compare, explain caveats, and draft review notes; it is not root truth. |
| EvidenceBundle outranks generated text | AI receipts must preserve evidence references where a response depends on evidence. |
| Runtime outcomes are finite | Atmosphere AI responses should record `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` where applicable. |
| No direct model-to-public path | Generated language cannot bypass proof, catalog, release, and governed API checks. |
| Policy and sensitivity still bind | AIReceipt presence does not override blocked rights, sensitivity, freshness, release state, or emergency-advisory limits. |
| Receipts are not proof | AI receipts record process memory; proof-side support belongs in `data/proofs/`. |
| Public clients never read receipt lanes directly | Public outputs consume governed APIs and released artifacts, not raw receipt files. |

---

## Atmosphere boundaries

| Atmosphere condition | AI receipt handling | Boundary |
|---|---|---|
| Evidence summary | Record evidence refs, release refs, limits, and response outcome. | Summary is not atmospheric truth without resolved evidence support. |
| Smoke, AOD, AQI, sensor, or model explanation | Record caveats and source roles used in the explanation. | AQI is not concentration; AOD is not PM2.5; model fields are not observations. |
| Advisory or warning context | Record official-source redirection and deny/abstain where needed. | Atmosphere is not an emergency alert or life-safety authority. |
| Low-cost sensor context | Record correction/caveat/confidence state if used. | Unreviewed low-cost sensor output cannot be made public by AI. |
| Cross-domain context | Record owning domain refs and limitations. | Atmosphere does not become Agriculture, Hydrology, Hazard, Habitat, Settlement, or Roads authority. |
| Unsupported prompt | Record abstain/deny/error basis. | Missing evidence, blocked policy, unclear rights, stale state, or precision mismatch must not be filled by generation. |

---

## Accepted material

Accepted content is limited to Atmosphere AI receipt instances and receipt-local sidecars:

- AIReceipt JSON or JSONL records for Atmosphere runs;
- prompt/request references, runtime/model references, run IDs, response IDs, outcome states, policy-decision refs, and review states;
- evidence refs, retrieval refs, catalog refs, release refs, citation refs, and limitations notes used by the AI process;
- abstain/deny/error rationale where evidence, policy, rights, freshness, sensitivity, or release state blocks an answer;
- checksums, receipt manifests, signatures, DSSE/cosign sidecars where applicable;
- README files and local indexes that help stewards inspect AI receipt state without becoming proof, catalog, policy, release, public output, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Full source rows, model fields, sensor payloads, rasters, or generated public layer bytes | Atmosphere lifecycle lanes under `data/raw/`, `data/work/`, `data/processed/`, or `data/published/` as applicable |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation, or integrity bundles | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, withdrawal notice, signature, or release changelog | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or generated public outputs | `data/published/` only after release gates close |
| Atmosphere policy, advisory policy, freshness policy, or AI-answer policy | `policy/` and governed policy roots |
| Receipt schemas or semantic contracts | `schemas/` and `contracts/` |
| Validator code, fixtures, tests, or CI workflows | `tools/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Emergency instructions or life-safety guidance | Official issuing authorities / Hazards lane redirection, not this receipt lane |

---

## Directory map

```text
data/receipts/ai/atmosphere/
├── README.md
├── <run_id>/
│   ├── ai_receipt.json
│   ├── checksums.sha256
│   ├── signature.bundle
│   └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove files, emitted receipts, schemas, validators, fixtures, CI checks, signing, governed API integration, or release integration exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, or generated-answer source.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay receipt-local | AI receipt records process memory but has not been consumed by downstream review. |
| Hold | Evidence refs, policy outcome, runtime identity, response outcome, review state, or citation support is incomplete. |
| Quarantine/correct | Receipt contradicts evidence, omits required limitations, violates policy, or points to unsupported outputs. |
| Reference from proof | Only when proof-side objects cite this receipt as process support and supply independent evidence support. |
| Reference from release | Only when release governance cites proof closure, receipt lineage, correction path, and rollback target. |

---

## Forbidden shortcut

```text
data/receipts/ai/atmosphere/
→ data/proofs/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed family transition has actually happened and left inspectable evidence. An AI receipt can support review, proof, and release artifacts, but it does not become those artifacts.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the AI receipt family and the Atmosphere domain lane.
- [ ] Confirm canonical AI receipt subtype naming against ADR-S-03 or the accepted receipt-layout ADR before relying on this path as final authority.
- [ ] Confirm receipt ID, run ID, prompt/request ref, model/runtime ref, response outcome, evidence refs, policy refs, citation refs, timestamps, and review state are present where applicable.
- [ ] Confirm EvidenceBundle/proof references resolve before using the AI output in any public claim path.
- [ ] Confirm AI output is not treated as atmospheric truth, emergency guidance, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm AQI/concentration, AOD/PM2.5, model/observation, and advisory/context boundaries are preserved.
- [ ] Confirm abstain/deny/error outcomes are recorded when evidence, precision, policy, rights, sensitivity, freshness, or release state blocks an answer.
- [ ] Confirm receipt payloads are immutable or hash-bound and do not overwrite prior receipt records in place.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, or generated answer uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/receipts/ai/atmosphere/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/receipts/ai/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| ADR-0011 says receipt, proof, catalog, release, and publication artifact families are separate. | **CONFIRMED doctrine / ADR status proposed** |
| RunReceipt standard names `AIReceipt` as a receipt subclass. | **CONFIRMED by GitHub contents API during this edit** |
| Atmosphere doctrine says AI is interpretive, must abstain or deny where evidence or policy requires it, and must not bypass EvidenceBundle resolution or the trust membrane. | **CONFIRMED by GitHub contents API during this edit** |
| Exact subtype layout under `data/receipts/ai/atmosphere/` is accepted by ADR-S-03 or receipt-layout governance. | **NEEDS VERIFICATION** |
| Actual Atmosphere AI receipt payloads exist under this subtree. | **UNKNOWN** |
| Schemas, validators, fixtures, CI checks, signing, DSSE/cosign enforcement, governed API integration, and release integration are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is atmospheric truth, proof, catalog authority, registry authority, policy authority, release authority, public artifact authority, emergency advisory authority, model-output authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../aggregation/README.md`](../../aggregation/README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../raw/atmosphere/README.md`](../../../raw/atmosphere/README.md)
- [`../../../processed/atmosphere/README.md`](../../../processed/atmosphere/README.md)
- [`../../../proofs/README.md`](../../../proofs/README.md)
- [`../../../catalog/domain/atmosphere/README.md`](../../../catalog/domain/atmosphere/README.md)
- [`../../../published/layers/atmosphere/README.md`](../../../published/layers/atmosphere/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)
- [`../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`../../../../docs/standards/RUN_RECEIPT.md`](../../../../docs/standards/RUN_RECEIPT.md)
- [`../../../../docs/domains/atmosphere/README.md`](../../../../docs/domains/atmosphere/README.md)
- [`../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md`](../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/atmosphere/VERIFICATION_BACKLOG.md`](../../../../docs/domains/atmosphere/VERIFICATION_BACKLOG.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)

---

KFM rule: `data/receipts/ai/atmosphere/` is an Atmosphere AI receipt lane for process memory only. It is not atmospheric truth, proof, catalog, registry, policy, release, publication, emergency advisory authority, public artifact authority, model-output authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
