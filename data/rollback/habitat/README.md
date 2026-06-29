<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/rollback/habitat/readme
name: Habitat Rollback README
path: data/rollback/habitat/README.md
type: data-rollback-habitat-readme
version: v0.1.0
status: draft
owners:
  - <data-steward>
  - <rollback-steward>
  - <release-steward>
  - <habitat-domain-steward>
  - <ecology-data-steward>
  - <land-cover-steward>
  - <restoration-context-steward>
  - <sensitivity-reviewer>
  - <geoprivacy-steward>
  - <rights-steward>
  - <source-role-steward>
  - <policy-steward>
  - <evidence-steward>
  - <proof-steward>
  - <receipt-steward>
  - <catalog-steward>
  - <map-layer-steward>
  - <ai-surface-steward>
  - <docs-steward>
created: 2026-06-29
updated: 2026-06-29
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
domain: habitat
artifact_family: rollback-receipt-and-alias-revert-support-lane
path_posture: existing-empty-file-replaced; parent-data-rollback-readme-is-empty; directory-rules-lists-data-rollback-domain-release-id; release-root-owns-release-decisions; adr-0015-two-plane-alias-rollback-mechanism-is-proposed; habitat-domain-rollback-lane-self-bounded; release-instance-child-shape-proposed; habitat-schema-slug-conflict-not-resolved
sensitivity_posture: no-public-path-by-default; rollback-is-governed-state-transition-not-file-move; not-delete; not-erasure; not-silent-edit; not-release-authority; not-proof-authority; not-receipt-family-authority-except-rollback-local-alias-revert-receipts; not-catalog-authority; not-policy-authority; habitat-sensitive-ecology-fail-closed; sensitive-habitat-geometry-rare-species-inference-steward-controlled-context-restoration-priority-private-landowner-detail-and-sensitive-corridor-context-fail-closed; habitat-not-species-occurrence-truth; suitability-not-occurrence; habitat-patch-not-critical-habitat-designation; connectivity-not-confirmed-movement; restoration-opportunity-not-prescription; land-cover-not-habitat-truth-by-itself; public-safe-geometry-transform-support-required; derivative-invalidation-required; evidence-aware; rights-aware; policy-aware; correction-aware; release-aware; rollback-target-required
related:
  - ../README.md
  - ../../README.md
  - ../../raw/habitat/README.md
  - ../../work/habitat/README.md
  - ../../quarantine/habitat/README.md
  - ../../processed/habitat/README.md
  - ../../catalog/domain/habitat/README.md
  - ../../registry/sources/habitat/README.md
  - ../../receipts/habitat/README.md
  - ../../proofs/habitat/README.md
  - ../../published/habitat/README.md
  - ../../published/layers/habitat/README.md
  - ../../reports/habitat/README.md
  - ../../../release/README.md
  - ../../../release/manifests/README.md
  - ../../../release/rollback_cards/
  - ../../../release/correction_notices/
  - ../../../release/withdrawal_notices/
  - ../../../docs/runbooks/ROLLBACK_RUNBOOK.md
  - ../../../docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/DATA_LIFECYCLE.md
  - ../../../docs/domains/habitat/CANONICAL_PATHS.md
  - ../../../docs/domains/habitat/SOURCE_REGISTRY.md
  - ../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../docs/domains/habitat/HABITAT_DOMAIN_MODEL.md
  - ../../../docs/domains/habitat/HABITAT_SOURCE_LEDGER.md
  - ../../../docs/domains/habitat/PUBLICATION_AND_ROLLBACK.md
  - ../../../docs/domains/habitat/SENSITIVITY.md
  - ../../../docs/domains/habitat/RELEASE_INDEX.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../contracts/domains/habitat/
  - ../../../contracts/release/
  - ../../../schemas/contracts/v1/domains/habitat/
  - ../../../schemas/contracts/v1/release/
  - ../../../policy/domains/habitat/
  - ../../../policy/release/habitat/
  - ../../../policy/sensitivity/habitat/
  - ../../../policy/geoprivacy/
  - ../../../policy/rights/
tags:
  - kfm
  - data
  - rollback
  - habitat
  - ecology
  - biodiversity
  - habitat-patch
  - land-cover
  - ecological-system
  - ecoregion
  - suitability-model
  - habitat-quality-score
  - connectivity
  - corridor
  - restoration-opportunity
  - stewardship-zone
  - uncertainty-surface
  - occurrence-habitat-assignment
  - public-safe-geometry
  - geoprivacy
  - source-role
  - sensitive-ecology
  - model-not-observation
  - suitability-not-occurrence
  - habitat-not-species-truth
  - rollback-card
  - alias-revert-receipt
  - release-manifest
  - correction-notice
  - withdrawal-notice
  - promotion-decision
  - release-gated
  - rollback-target
  - correction-path
  - published-artifact
  - published-layer
  - evidence-bundle
  - proof-pack
  - redaction-receipt
  - aggregation-receipt
  - model-run-receipt
  - validation-report
  - policy-decision
  - no-public-path
  - not-delete
  - not-erasure
  - not-file-move
  - derivative-invalidation
  - cite-or-abstain
notes:
  - "This README replaces an empty file at `data/rollback/habitat/README.md`."
  - "The parent `data/rollback/README.md` is currently empty, so this file is self-bounding and intentionally conservative."
  - "Directory Rules v1.4 lists `data/rollback/<domain>/<release_id>/` and says rollback may hold rollback cards and alias-revert receipts, but must not delete prior meanings."
  - "The release root says release decisions, manifests, promotion records, rollback cards, withdrawals, corrections, signatures, and changelog belong under `release/`, distinct from published artifacts."
  - "ADR-0015 proposes a two-plane alias mechanism: `release/rollback_cards/` owns rollback decision authority, while `data/rollback/` may hold data-plane alias-revert receipts. This README follows that separation without claiming ADR acceptance or implementation maturity."
  - "Habitat rollback support is downstream of release and correction governance. It does not replace EvidenceBundles, ProofPacks, receipts, catalog records, policy decisions, source-role decisions, review records, release manifests, correction notices, withdrawal notices, source descriptors, schemas, contracts, or public payloads."
  - "Rollback material must not preserve or re-expose sensitive habitat geometry, rare-species habitat inference, steward-controlled ecological context, restoration-priority detail, private-landowner detail, sensitive corridor context, or species/habitat joins that can reconstruct restricted locations."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Rollback

Data-plane rollback support lane for Habitat release recovery, alias-revert receipts, affected-artifact indexes, public-safe geometry invalidation, and rollback-local inspection material.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data" src="https://img.shields.io/badge/root-data%2F-0a7ea4">
  <img alt="Lane: rollback" src="https://img.shields.io/badge/lane-rollback-orange">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Posture: sensitive ecology" src="https://img.shields.io/badge/posture-sensitive%20ecology-critical">
  <img alt="Boundary: not release authority" src="https://img.shields.io/badge/boundary-not%20release%20authority-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Rollback boundary](#rollback-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Habitat rollback guardrails](#habitat-rollback-guardrails) · [Rollback flow](#rollback-flow) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!CAUTION]
> `data/rollback/habitat/` is not release authority, not publication authority, not proof, not general receipt storage, not catalog closure, not policy authority, not schema authority, not source registry authority, not Habitat truth, not species occurrence truth, not critical-habitat designation authority, not restoration prescription, not land-management advice, not legal/ecological advice, not erasure, not a delete mechanism, not a silent edit, not a file-move shortcut, and not a direct public UI/API source. Habitat rollback is a governed state transition with release-plane decision support, evidence/proof support, policy and sensitivity review, source-role validation, correction/withdrawal state, derivative invalidation, and an auditable rollback target.

---

## Scope

`data/rollback/habitat/` may hold Habitat-domain data-plane rollback support material for a specific released Habitat artifact set or release alias transition.

This lane is appropriate for rollback-local material such as:

- alias-revert receipts tied to a release-plane `RollbackCard`;
- affected public-artifact indexes for Habitat releases, public-safe habitat map layers, land-cover layers, ecoregion layers, ecological-system layers, habitat patch layers, suitability surfaces, connectivity and corridor surfaces, restoration-opportunity surfaces, stewardship-zone context, reports, stories, API payloads, PMTiles, exports, graph/triplet projections, search surfaces, and AI answer surfaces;
- digest verification summaries for the release being rolled back and the target release being restored;
- rollback-local pointers to `ReleaseManifest`, `RollbackCard`, `CorrectionNotice`, `WithdrawalNotice`, EvidenceBundle, ProofPack, catalog records, receipts, policy decisions, review records, source descriptors, source-role validation records, model-run receipts, public-safe geometry transform records, RedactionReceipt, AggregationReceipt, ValidationReport, and source registry records;
- stale-state, cache-invalidation, alias-resolution, derivative-invalidation, public-surface withdrawal, and governed-answer invalidation support;
- rollback drill material that is clearly marked as drill/test and not release authority;
- README files explaining local rollback boundaries.

A file here does **not** authorize rollback. It can record or support the data-plane effects of a rollback decision, but the release decision belongs under `release/` and must remain inspectable.

---

## Path posture

The existing target lane is:

```text
data/rollback/habitat/
```

Current placement evidence:

- `docs/doctrine/directory-rules.md` lists `data/rollback/<domain>/<release_id>/` in the data lifecycle tree.
- Directory Rules say rollback may hold rollback cards and alias-revert receipts, but must not delete prior meanings.
- `release/README.md` says release decisions, manifests, promotion records, rollback cards, withdrawals, corrections, signatures, and changelog belong under `release/`.
- `docs/runbooks/ROLLBACK_RUNBOOK.md` distinguishes release-plane rollback decisions from data-plane revert receipts and derivative invalidation.
- ADR-0015 proposes a two-plane mechanism where `release/rollback_cards/` owns the decision and `data/rollback/` owns data-plane alias-revert receipts. ADR-0015 is draft/proposed, so this README does not claim the mechanism is implemented or accepted.
- `data/rollback/README.md` is currently empty; this child README is therefore self-bounding.

Therefore this README treats `data/rollback/habitat/` as **CONFIRMED path presence / NEEDS VERIFICATION parent contract and instance layout**.

The Habitat docs also preserve a schema-home slug conflict between segmented and flat Habitat schema paths. This rollback README follows the requested data path and does **not** resolve that ADR question.

---

## Repo fit

| Responsibility | Correct home | Boundary |
|---|---|---|
| Habitat rollback data-plane support | `data/rollback/habitat/` | This lane; not release decision authority. |
| Rollback parent | [`../README.md`](../README.md) | Currently empty; parent contract still needs expansion. |
| Data root | [`../../README.md`](../../README.md) | Lifecycle data root; rollback is one data-plane family. |
| Release decisions | [`../../../release/`](../../../release/README.md) | `ReleaseManifest`, `PromotionDecision`, `RollbackCard`, `CorrectionNotice`, `WithdrawalNotice`, signatures, changelog. |
| Habitat published carriers | [`../../published/habitat/`](../../published/habitat/README.md) | Released public-safe carriers; not rollback decisions. |
| Habitat published map layers | [`../../published/layers/habitat/`](../../published/layers/habitat/README.md) | Released map-layer carriers; rollback support is required before release. |
| Habitat processed artifacts | [`../../processed/habitat/`](../../processed/habitat/README.md) | Upstream normalized artifacts; not rollback records. |
| Habitat catalog records | [`../../catalog/domain/habitat/`](../../catalog/domain/habitat/README.md) | Catalog closure and discovery records; not rollback decisions. |
| Habitat source registry | [`../../registry/sources/habitat/`](../../registry/sources/habitat/README.md) | Source admission, rights, sensitivity, source role, stale-state, and no-public-path posture; not rollback decisions. |
| Habitat receipts | [`../../receipts/habitat/`](../../receipts/habitat/README.md) | General process memory; rollback-local alias-revert receipts are narrow support records only. |
| Habitat proofs | [`../../proofs/habitat/`](../../proofs/habitat/README.md) | Evidence/proof support; rollback cites but does not replace. |
| Habitat report candidates | [`../../reports/habitat/`](../../reports/habitat/README.md) | Candidate/support narrative lane; not release or rollback authority. |
| Rollback runbook | [`../../../docs/runbooks/ROLLBACK_RUNBOOK.md`](../../../docs/runbooks/ROLLBACK_RUNBOOK.md) | Operational procedure; not data payload. |
| Alias governance ADR | [`../../../docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md`](../../../docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md) | Proposed alias/rollback mechanism; not proof of implementation. |
| Contracts, schemas, policy | `../../../contracts/`, `../../../schemas/`, `../../../policy/` | Meaning, machine shape, and allow/deny/restrict/abstain logic. |

---

## Rollback boundary

| Rule | Handling |
|---|---|
| Rollback is a governed transition | A rollback must resolve release decision, evidence/proof, policy, catalog, sensitivity/public-safe geometry review, source-role review, correction/withdrawal, and rollback target support. |
| Rollback is not deletion | Prior releases, meanings, receipts, proofs, catalog records, review records, and lineage remain inspectable unless a separate erasure process applies. |
| Rollback is not erasure | Privacy, rights, stewardship, sovereignty, cultural context, or legal erasure workflows require their own governed process; rollback support here must not masquerade as erasure. |
| Rollback is not a silent edit | Corrections and withdrawals require explicit release governance and visible supersession, stale-state, or withdrawal state. |
| Rollback is not a file move | Moving bytes between folders or changing an alias without release-plane authority is not rollback. |
| Release decision stays in `release/` | Primary `RollbackCard`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, signatures, and promotion decisions belong under `release/`. |
| Habitat does not own species truth | Fauna owns animal occurrence truth; Flora owns plant, specimen, and rare-plant truth. Habitat rollback cannot convert habitat context into occurrence claims. |
| Sensitive ecological inference remains load-bearing | Sensitive habitat geometry, rare-species habitat inference, steward-controlled context, restoration-priority detail, private-landowner detail, and sensitive corridor context fail closed unless public-safe support exists. |
| Proof remains separate | EvidenceBundle, ProofPack, citation validation, and integrity proof stay in `data/proofs/`. |
| Receipts remain separate | General run/transform/validation/redaction/review/AI/release-support receipts stay in receipt lanes; this lane may hold rollback-local alias-revert receipts only. |
| Catalog remains separate | STAC/DCAT/PROV/domain catalog records stay in `data/catalog/`. |
| Published artifacts remain versioned | `data/published/` holds released artifacts; rollback records should not overwrite immutable release directories. |
| Policy remains separate | Sensitivity, rights, source-role, geoprivacy, public-safe geometry, model-use, redaction, generalization, aggregation, and public-release rules stay in `policy/`. |
| Public clients do not read this lane | Public UI/API/report/map surfaces consume governed APIs, released artifacts, catalog/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted material is limited to rollback-local support for Habitat release recovery:

- `alias_revert_receipt.json` or equivalent rollback-local receipt tied to a release-plane `RollbackCard`;
- rollback-local indexes of affected Habitat published artifacts, including public-safe habitat layers, land-cover layers, ecoregion layers, ecological-system layers, patches, suitability surfaces, connectivity surfaces, corridors, restoration-opportunity public derivatives, stewardship-zone context, reports, stories, API payloads, graph/triplet projections, search indexes, exports, and AI-answer surfaces;
- digest verification summaries comparing `from_release_id`, `to_release_id`, affected artifact digests, and resolved published paths;
- public-surface invalidation and stale-state records for maps, APIs, reports, story snapshots, Evidence Drawer payloads, Focus Mode answers, model summaries, search indexes, graph edges, caches, screenshots, exports, PMTiles, tiles, and public downloads;
- references to ReleaseManifest, RollbackCard, CorrectionNotice, WithdrawalNotice, PromotionDecision, signatures, EvidenceBundle, ProofPack, catalog records, source registry records, ModelRunReceipt, RedactionReceipt, AggregationReceipt, TransformReceipt, ValidationReport, PolicyDecision, ReviewRecord, AIReceipt, and release-review records;
- rollback drill artifacts that are clearly marked as drill/test and never treated as release authority;
- local README files and indexes that help stewards inspect rollback state without becoming release, proof, catalog, policy, source-registry, source-role, sensitivity, species truth, habitat truth, restoration authority, or public authority.

All accepted material must preserve release identity, prior release identity, target release identity, affected artifact identity, digest references, evidence/proof references, source-role state, model/uncertainty state, sensitivity and public-safe geometry state, policy state, review state, correction/withdrawal state, actor/runner identity, timestamp, and finite outcome where material.

Do **not** embed restricted ecology or species-linked habitat clues in rollback support. Use governed pointers, redacted identifiers, release IDs, digests, and public-safe artifact IDs.

---

## Exclusions

| Do not place here | Correct home | Why |
|---|---|---|
| RAW source captures, land-cover packages, remote-sensing scenes, stewardship exports, occurrence-context files, ecological-system packages, model inputs, rasters, shapefiles, GeoParquet, PMTiles, source-native tables, logs, uploads, or source mirrors | `../../raw/habitat/`, `../../work/habitat/`, or `../../quarantine/habitat/` | Source-edge and unsafe material requires source metadata, checksums, rights, source-role, public-safe geometry, and sensitivity controls. |
| WORK scratch, rollback experiments, transform intermediates, repair attempts, redaction/generalization trials, aggregation trials, model experiments, classification crosswalk drafts, or unresolved joins | `../../work/habitat/` or `../../quarantine/habitat/` | Unresolved material belongs upstream or in hold lanes. |
| Normalized Habitat datasets | `../../processed/habitat/` | Processed data is not rollback support. |
| Catalog, STAC, DCAT, PROV, or graph/triplet records | `../../catalog/`, `../../triplets/` | Catalog and graph carriers have their own closure rules. |
| EvidenceBundle, ProofPack, CitationValidationReport, or integrity proof | `../../proofs/habitat/` or accepted proof lanes | Proof is the trust spine; rollback cites it. |
| General RunReceipt, TransformReceipt, ModelRunReceipt, RedactionReceipt, AggregationReceipt, ValidationReceipt, ReviewRecord, PolicyDecision, AIReceipt, or release-support receipt families | `../../receipts/habitat/` or accepted receipt/review lanes | General process memory belongs in receipt lanes; rollback-local receipts are narrow exceptions. |
| SourceDescriptor, source activation records, rights registry records, sensitivity registry records, source-family records, or access-control records | `../../registry/`, `policy/`, or accepted governance roots | Registry and control records belong in their own authority lanes. |
| Primary ReleaseManifest, RollbackCard, PromotionDecision, CorrectionNotice, WithdrawalNotice, signatures, or release changelog | `../../../release/` | Release decisions belong in release authority. |
| Published public artifacts | `../../published/habitat/`, `../../published/layers/habitat/`, or other released artifact lanes | Rollback support does not own public artifacts. |
| Public reports or steward-facing generated narratives | `../../published/reports/`, `../../../docs/reports/` | Report lanes have separate authority. |
| Contracts, schemas, policy rules, validators, tests, code, or workflows | `../../../contracts/`, `../../../schemas/`, `../../../policy/`, `../../../tools/`, `../../../tests/`, `.github/workflows/` | Separate authority roots. |
| Deletion directives, erasure directives, critical-habitat designations, species occurrence conclusions, restoration prescriptions, land-management instructions, legal advice, conservation-compliance findings, hazard warnings, emergency guidance, or life-safety directions | Separate governed authority or external authority | Rollback support is not legal, operational, ecological-management, regulatory, or safety authority. |
| Sensitive habitat geometry, rare-species habitat inference, stewardship-only notes, restoration-priority detail, sensitive corridor detail, private-landowner detail, exact occurrence-linked habitat joins, redaction offsets, generalization radii, transform parameters, or derivative detail that can reconstruct restricted locations | Restricted governed lanes only; public-safe derivative after policy/review/release | Rollback must not become a geoprivacy, sensitivity, rights, or stewardship-data bypass. |

---

## Habitat rollback guardrails

| Risk | Guardrail |
|---|---|
| Deleting prior meaning | Rollback preserves prior release records, evidence, receipts, catalog records, review records, and lineage unless a separate governed erasure process applies. |
| Alias-only rollback | A current-pointer or alias change is insufficient unless tied to release-plane decision authority, digest verification, review state, and rollback-local receipt support. |
| Public artifact overwrite | Immutable release artifacts must not be overwritten in place. Reseat pointers or publish a governed correction/supersession. |
| Suitability/occurrence collapse | A suitability surface is not a species occurrence; rollback must not restore a surface that implies occurrence truth without owning-lane evidence and public-safe review. |
| Patch/designation collapse | A HabitatPatch is not a critical-habitat designation. Regulatory products require issuing authority, source role, and legal-scope caveats. |
| Connectivity/movement collapse | Connectivity surfaces and corridors are modeled context, not confirmed animal movement or migration proof by themselves. |
| Restoration/prescription collapse | Restoration opportunity, priority, or suitability context is not a restoration prescription, land-management order, funding decision, or compliance finding. |
| Land-cover/habitat collapse | Land-cover is evidence/context. It is not habitat truth, suitability truth, crop truth, soil truth, hydrology truth, or regulatory truth by itself. |
| Model/observation collapse | Suitability, connectivity, ecological-system, restoration, and uncertainty surfaces must preserve model identity, run receipt, assumptions, validation, and uncertainty. |
| Sensitive inference leak persists | Wrongfully exposed sensitive habitat, rare-species inference, corridor, stewardship, or private-land clues require public-surface withdrawal, invalidation, correction, and cache/search/AI/graph/tile review; rollback alone cannot recall copied data. |
| Public-safe geometry bypass | Missing or invalid RedactionReceipt, AggregationReceipt, public-safe geometry transform, ReviewRecord, PolicyDecision, or release decision should force HOLD, DENY, correction, withdrawal, or rollback rather than public continuation. |
| Cross-lane authority drift | Fauna, Flora, Hydrology, Soil, Hazards, Agriculture, Archaeology, People/Land, Roads/Rail, Settlements/Infrastructure, Geology, and Atmosphere keep their own truth and sensitivity boundaries. |
| Stale public surface | Map layers, API payloads, reports, indexes, tiles, stories, graph/triplet exports, Evidence Drawer payloads, Focus Mode answers, search surfaces, and AI answers must be invalidated or marked stale when rollback affects them. |
| Proof bypass | Rollback cannot repair a claim by hiding evidence gaps. EvidenceBundle/proof closure must still support the restored or superseding release. |
| Catalog bypass | Catalog, STAC, DCAT, PROV, and domain catalog state must be corrected or invalidated alongside published artifacts. |
| AI surface drift | Generated Habitat answers, Focus Mode surfaces, report summaries, story text, and Evidence Drawer prose must not keep citing withdrawn, stale, overclaimed, or restricted release state. |
| File-move shortcut | Moving, renaming, or copying files under `data/published/` is not rollback unless release governance, receipts, proof, policy, review, and catalog closure support it. |

---

## Rollback flow

```mermaid
flowchart LR
    DETECT[Defect or sensitive exposure detected] --> CLASSIFY[Classify affected Habitat surfaces]
    CLASSIFY --> FREEZE[Freeze or mark affected public surfaces stale]
    FREEZE --> RELEASE[Locate ReleaseManifest and rollback target]
    RELEASE --> REVIEW[Verify source-role / rights / sensitivity / public-safe geometry review state]
    REVIEW --> PROOF[Verify EvidenceBundle, proof, receipts, catalog]
    PROOF --> DECISION[Release-plane RollbackCard / CorrectionNotice / WithdrawalNotice]
    DECISION --> DATA[data/rollback/habitat receipt support]
    DATA --> INVALIDATE[Invalidate aliases, maps, tiles, reports, graph, search, AI surfaces]
    INVALIDATE --> RESTORE[Restore or publish governed public-safe target]
    RESTORE --> RECORD[Record correction path, rollback target, digests, status]

    classDef gate fill:#fff3cd,stroke:#8a6d3b,color:#202124;
    classDef hold fill:#f8d7da,stroke:#842029,color:#202124;
    class DECISION gate;
    class FREEZE hold;
```

> [!NOTE]
> This diagram is a responsibility map, not proof that rollback tooling, validators, alias resolvers, release manifests, rollback cards, public-safe geometry review workflows, cache invalidation, or CI gates currently exist.

---

## Suggested directory shape

This shape follows the Directory Rules pattern `data/rollback/<domain>/<release_id>/` and remains **PROPOSED** until parent rollback governance or an accepted ADR confirms exact file names. Do not pre-create empty stubs.

```text
data/rollback/habitat/
├── README.md
├── <release_id>/
│   ├── alias_revert_receipt.json
│   ├── rollback.data_plane_receipt.json
│   ├── affected_artifacts.index.json
│   ├── digest_verification.json
│   ├── invalidation_refs.json
│   ├── release_refs.json
│   ├── evidence_refs.json
│   ├── source_role_refs.json
│   ├── model_refs.json
│   ├── public_safe_geometry_refs.json
│   ├── redaction_refs.json
│   ├── aggregation_refs.json
│   ├── review_refs.json
│   ├── policy_refs.json
│   ├── stale_state.json
│   └── README.md
├── drills/                              # PROPOSED: rollback drill outputs, clearly marked non-production
│   └── <drill_id>/
└── indexes/                             # PROPOSED: rollback-local indexes only
    └── habitat.rollback.index.json
```

Recommended minimal release-instance fields:

| Field | Purpose |
|---|---|
| `rollback_id` | Stable identifier for the data-plane rollback support record. |
| `release_id` | Defective, withdrawn, superseded, stale, overclaimed, or exposed release being addressed. |
| `target_release_id` | Prior or superseding release selected by release authority. |
| `rollback_card_ref` | Pointer to release-plane decision authority. |
| `release_manifest_ref` | Pointer to affected ReleaseManifest. |
| `review_refs` | Source-role, rights, public-safe geometry, sensitivity, geoprivacy, model, and release-review references required for Habitat. |
| `affected_artifacts` | Published artifacts, aliases, catalog records, graph exports, reports, tiles, stories, API payloads, search surfaces, and AI surfaces affected. |
| `defect_class` | Public-safe classification of the defect, avoiding exact restricted details. |
| `source_role_state` | Observed/regulatory/modeled/aggregate/administrative/candidate/synthetic posture. |
| `model_state` | Model identity, run receipt, assumptions, validation, uncertainty, and limitation posture where applicable. |
| `public_safe_geometry_state` | Public-safe transform, redaction, generalization, aggregation, withholding, or denial posture. |
| `digest_verification` | Hash/digest checks for defective and target artifacts. |
| `policy_state` | Policy/review disposition for restored or superseding public surface. |
| `evidence_refs` | EvidenceBundle/proof references needed to inspect restored claims. |
| `invalidation_refs` | Downstream invalidation or stale-state records. |
| `outcome` | Finite outcome such as `RESTORED`, `WITHDRAWN`, `SUPERSEDED`, `HELD`, `DENIED`, `ABSTAIN`, or `ERROR`. |

---

## Required checks before use

- [ ] Confirm whether `data/rollback/README.md` should define a parent rollback contract, and update this README if parent rules change.
- [ ] Confirm exact rollback instance naming under `data/rollback/habitat/<release_id>/`.
- [ ] Confirm the release-plane `RollbackCard`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, and signatures exist where required.
- [ ] Confirm the rollback target resolves to a prior or superseding release with digest closure.
- [ ] Confirm EvidenceBundle, ProofPack, catalog, receipt, policy, rights, sensitivity, public-safe geometry, source-role, model, review, and release support resolve for both the defective and target release where material.
- [ ] Confirm redaction/generalization/aggregation support for any public Habitat artifact that depends on sensitive habitat geometry, rare-species habitat inference, occurrence joins, steward-controlled context, restoration-priority detail, private-landowner detail, or sensitive corridor context.
- [ ] Confirm stale or withdrawn Habitat map layers, land-cover layers, suitability surfaces, connectivity/corridor surfaces, restoration-opportunity surfaces, API payloads, reports, PMTiles, story snapshots, graph/triplet projections, search indexes, Evidence Drawer payloads, Focus Mode answers, and AI-answer surfaces are invalidated or marked stale.
- [ ] Confirm rollback records do not embed restricted habitat clues, exact occurrence-linked habitat joins, private-landowner detail, stewardship-only notes, redaction offsets, generalization radii, transform parameters, or derivative detail that can reconstruct restricted locations.
- [ ] Confirm habitat/species, suitability/occurrence, patch/designation, connectivity/movement, restoration/prescription, land-cover/habitat, model/observation, and Habitat/cross-lane boundaries are not collapsed in the restored state.
- [ ] Confirm rollback does not delete prior meanings, overwrite immutable release artifacts, bypass catalog/proof/policy/release/review checks, or expose restricted detail.
- [ ] Confirm public clients resolve restored state through governed API or released artifact aliases, not by reading this rollback lane.
- [ ] Confirm rollback-local receipt support is referenced by release/proof governance without becoming release authority itself.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target path presence | CONFIRMED | `data/rollback/habitat/README.md` existed as an empty file before this update. |
| Parent rollback README | CONFIRMED empty | `data/rollback/README.md` exists but is empty, so parent rollback contract remains NEEDS VERIFICATION. |
| Directory Rules rollback path | CONFIRMED doctrine | Directory Rules list `data/rollback/<domain>/<release_id>/` and warn rollback must not delete prior meanings. |
| Release root decision authority | CONFIRMED README | `release/README.md` says release decisions, manifests, promotion records, rollback cards, withdrawals, corrections, signatures, and changelog belong under `release/`. |
| Habitat domain doctrine | CONFIRMED README | `docs/domains/habitat/README.md` establishes Habitat scope, landscape-not-species posture, source-role anti-collapse, and sensitivity-redacted posture. |
| Habitat lifecycle doctrine | CONFIRMED README | `docs/domains/habitat/DATA_LIFECYCLE.md` establishes RAW-to-PUBLISHED traversal, watcher non-publisher posture, correction/rollback expectations, and Habitat rollback path shape. |
| Habitat published domain lane | CONFIRMED README | `data/published/habitat/README.md` requires release authority, evidence support, validation, policy review, catalog closure, correction path, and rollback support before public artifacts land there. |
| Habitat published layer lane | CONFIRMED README | `data/published/layers/habitat/README.md` requires release support, public-safe artifacts, evidence refs, policy outcome, correction path, rollback target, and governed public interfaces. |
| Habitat processed lane | CONFIRMED README | `data/processed/habitat/README.md` is upstream and says public use requires governed catalog, evidence, source-role and rights posture, sensitivity/policy review, release state, correction path, and rollback target. |
| Habitat catalog lane | CONFIRMED README | `data/catalog/domain/habitat/README.md` says catalog records are not release authority and require evidence/source/sensitivity/policy/release references for public records. |
| Habitat receipts lane | CONFIRMED README | `data/receipts/habitat/README.md` defines receipt process memory and includes rollback-support context without making receipts proof or release authority. |
| Habitat proofs lane | CONFIRMED README | `data/proofs/habitat/README.md` defines proof support and excludes primary RollbackCard/ReleaseManifest ownership. |
| Habitat source registry | CONFIRMED README | `data/registry/sources/habitat/README.md` establishes source admission, source-role preservation, sensitive joins fail-closed, no-public-path, and release-blocked posture. |
| Habitat reports lane | CONFIRMED README | `data/reports/habitat/README.md` establishes report-candidate boundaries and Habitat-specific guardrails; reports are not rollback authority. |
| Rollback runbook | CONFIRMED README | `docs/runbooks/ROLLBACK_RUNBOOK.md` describes rollback as a governed release transition and distinguishes decision artifacts from data-plane revert receipts. |
| Alias rollback ADR | CONFIRMED draft ADR | ADR-0015 proposes current-alias governance by RollbackCard and data-plane alias-revert receipts. |
| Habitat schema-home slug | CONFLICTED / NEEDS VERIFICATION | Habitat docs preserve segmented-vs-flat schema-home conflict. This README does not resolve it. |
| Actual rollback instances | UNKNOWN | This README does not prove any Habitat rollback instance exists. |
| Rollback tooling, validators, CI, signatures, alias resolver, cache invalidation | NEEDS VERIFICATION | No runtime enforcement was proven by this edit. |
| Public release readiness | DENY until proven | A rollback README cannot publish, restore, or expose Habitat claims by itself. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `data/rollback/habitat/README.md` existed as an empty file. | Did not define lane boundaries. |
| [`../README.md`](../README.md) | CONFIRMED empty | Parent rollback root exists. | Does not yet define parent rollback contract. |
| [`../../README.md`](../../README.md) | CONFIRMED | Data root includes lifecycle data families. | Does not prove rollback payloads or enforcement. |
| [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) | CONFIRMED doctrine | `data/rollback/<domain>/<release_id>/`; rollback must not delete prior meanings; promotion is governed state transition. | Exact rollback instance file names remain unresolved. |
| [`../../../release/README.md`](../../../release/README.md) | CONFIRMED README | Release decision artifacts belong under `release/`, distinct from `data/published/`. | Release root README is short and status `PROPOSED`; does not prove concrete release artifacts. |
| [`../../../docs/runbooks/ROLLBACK_RUNBOOK.md`](../../../docs/runbooks/ROLLBACK_RUNBOOK.md) | CONFIRMED draft runbook | Rollback governs PUBLISHED releases, rollback cards, correction notices, withdrawal of public surfaces, derivative invalidation, and data-plane revert receipts. | Runbook notes implementation is PROPOSED/NEEDS VERIFICATION in places. |
| [`../../../docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md`](../../../docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md) | CONFIRMED draft ADR | Proposed two-plane alias rollback mechanism: release-plane RollbackCard and data-plane alias-revert receipt. | ADR is draft/proposed and does not prove implementation. |
| [`../../../docs/domains/habitat/README.md`](../../../docs/domains/habitat/README.md) | CONFIRMED doctrine / PROPOSED implementation | Habitat scope, landscape-not-species posture, source-role anti-collapse, sensitivity-redacted posture, and lifecycle orientation. | Implementation maturity remains NEEDS VERIFICATION in parts. |
| [`../../../docs/domains/habitat/DATA_LIFECYCLE.md`](../../../docs/domains/habitat/DATA_LIFECYCLE.md) | CONFIRMED doctrine / PROPOSED implementation | Habitat lifecycle, rollback path shape, object families, source families, correction/rollback posture, and trust-membrane posture. | Does not prove runtime enforcement. |
| [`../../published/habitat/README.md`](../../published/habitat/README.md) | CONFIRMED README | Habitat published artifacts require release authority, evidence support, validation, policy review, catalog closure, correction path, and rollback support. | Does not prove released artifacts exist. |
| [`../../published/layers/habitat/README.md`](../../published/layers/habitat/README.md) | CONFIRMED README | Habitat published layers require release support, public-safe artifacts, evidence refs, policy outcome, correction path, rollback target, and governed public interfaces. | Does not prove layer payloads or release manifests exist. |
| [`../../processed/habitat/README.md`](../../processed/habitat/README.md) | CONFIRMED README | Processed Habitat is upstream of catalog/release and requires correction path and rollback target for public use. | Does not prove processed inventory. |
| [`../../catalog/domain/habitat/README.md`](../../catalog/domain/habitat/README.md) | CONFIRMED README | Habitat catalog lane requires evidence, source, sensitivity, policy, release, and rollback references for public records. | Catalog records are not rollback decisions. |
| [`../../receipts/habitat/README.md`](../../receipts/habitat/README.md) | CONFIRMED README | Habitat receipts are process memory and include rollback-support context while excluding proof/release authority. | General receipts are not release/proof authority. |
| [`../../proofs/habitat/README.md`](../../proofs/habitat/README.md) | CONFIRMED README | Habitat proofs support evidence closure, public-safe geometry proof posture, model-support proof, and rollback proof; primary release records remain in `release/`. | Proof lane does not publish or roll back by itself. |
| [`../../registry/sources/habitat/README.md`](../../registry/sources/habitat/README.md) | CONFIRMED README | Source registry establishes admission, rights, source role, sensitive joins fail-closed, source-registry topology warning, and no-public-path boundaries. | Source registry records do not authorize rollback or publication. |
| [`../../reports/habitat/README.md`](../../reports/habitat/README.md) | CONFIRMED README | Habitat reports are report-candidate/report-support downstream carriers with sensitive-ecology and anti-collapse guardrails. | Reports are not rollback decisions or public release authority. |

[Back to top](#top)
