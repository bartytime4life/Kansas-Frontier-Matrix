<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-cartographic-omission-disclosure
title: Pass 18 Cartographic Omission Disclosure Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Data contract steward · Cartography steward
created: 2026-08-10
updated: 2026-08-10
owning_root: docs/
policy_label: internal; source-lineage; cartography; representation
responsibility: Preserve exact and thematic source lineage for the bounded cartographic omission disclosure adaptation without promoting proposal material into repository, evidence, policy, release, or publication authority.
truth_posture: "CONFIRMED attached-card transcription and inspected-repository comparison; PROPOSED bounded adaptation; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/data/cartographic_omission_disclosure.md
  - ../../../contracts/data/layer_manifest.md
  - ../../../schemas/contracts/v1/data/cartographic_omission_disclosure.schema.json
  - ../../../fixtures/contracts/v1/data/cartographic_omission_disclosure/cases.json
  - ../../../docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Cartographic Omission Disclosure Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical page 50 / printed page 47 | Card `KFM-P18-INV-401` proposes recording purposeful omissions, simplifications, and emphasis choices so viewers can inspect what a public map chose not to show. | `CONFIRMED` |
| Connected Drive `KFM_Full_Atlas_seed_cards` (`1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`) | The `Renderer-Downstream Map Law Capability` carrier proposes showing generalized and withheld states in map layers, popups, Evidence Drawer links, and exports; its implementation carrier names `LayerManifest` while keeping renderer output downstream of evidence, policy, review, and release. Its placeholder stable ID is retained as source limitation, not promoted to repository identity. | `CONFIRMED` thematic corroboration |
| `main@7d3b894deeb82d3ecb0ddf3daeec9158f266edb1` | Exact searches found `LayerManifest`, representation-fitness, map-trust, transform-receipt, and Evidence Drawer surfaces, but no cartographic omission disclosure/register contract, schema, fixture family, validator, workflow, or matching PR history. | `CONFIRMED` for the inspected snapshot |

The supplied and Drive artifacts are proposal evidence, not repository instruction authority. The connected Drive Pass 18 PDF has a different byte size and its text extraction did not expose `KFM-P18-INV-401`; this source map therefore does not claim byte identity between the attached and Drive PDFs.

## Reconciliation and selected increment

The repository already owns layer-manifest meaning, representation fitness, transform receipts, map trust vocabulary, and Evidence Drawer payloads. Editing all of those consumers in one change would enlarge both compatibility and authority risk.

The selected increment is therefore one additive disclosure profile that composes existing objects by reference. It does not modify `LayerManifest`, define a new map trust state, expose withheld values, or bind a runtime/UI consumer.

## Source-to-profile mapping

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Record omission, simplification, and emphasis. | Closed action and subject vocabularies with canonical entry identity. | No layer or style mutation. |
| Make material choices visible to viewers. | Material entries require a declared `LAYER_NOTE`, `LEGEND`, or `EVIDENCE_DRAWER` surface. | No UI component or public activation. |
| Keep map purpose and evidence scope visible. | Pinned purpose and evidence-scope references with explicit resolution states. | No resolver or truth claim. |
| Preserve policy and transform provenance. | Rights/sensitivity require policy refs; simplification requires a transform-receipt ref. | No policy evaluation or receipt authentication. |
| Avoid false completeness. | Declared-scope completeness cannot coexist with known undisclosed material choices or unknown materiality. | No universal materiality threshold. |

## Directory Rules basis

The profile meaning is adjacent to the current `contracts/data/layer_manifest.md` object family. Shape, fixtures, validator, tests, workflow, source mapping, and generated receipt remain in their established responsibility roots. No new root or parallel map, layer, evidence, policy, release, or publication authority is introduced.

## Deferred questions

- Which omissions are material enough to require public disclosure for each map purpose?
- Should a later compatible `LayerManifest` version embed these records or reference them?
- Which released surface may display each disclosure class without exposing restricted details?
- Which steward owns completeness review for multi-layer scenes?

These questions require separate decisions. This profile fixes none of them.

## Validation and rollback

Focused validation covers closed shape, deterministic identity, canonical ordering, material-disclosure visibility, simplification receipt binding, sensitivity/rights policy references, incomplete and unknown abstention, completeness-claim mismatch, hash tampering, and unknown-field rejection.

Rollback is a focused revert of this additive packet. No data reprocessing, correction notice, release withdrawal, cache invalidation, UI cleanup, or public-map cleanup is required because the profile has no consumer and changes no layer.
