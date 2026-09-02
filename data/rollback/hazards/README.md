<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/rollback/hazards/readme
name: Hazards Rollback README
path: data/rollback/hazards/README.md
type: data-rollback-hazards-readme
version: v0.1.0
status: draft
owners:
  - <data-steward>
  - <rollback-steward>
  - <release-steward>
  - <hazards-domain-steward>
  - <life-safety-boundary-steward>
  - <official-source-reviewer>
  - <freshness-steward>
  - <source-role-steward>
  - <rights-steward>
  - <sensitivity-reviewer>
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
domain: hazards
artifact_family: rollback-receipt-and-alias-revert-support-lane
path_posture: existing-empty-file-replaced; parent-data-rollback-readme-is-empty; directory-rules-lists-data-rollback-domain-release-id; release-root-owns-release-decisions; adr-0015-two-plane-alias-rollback-mechanism-is-proposed; hazards-domain-rollback-lane-self-bounded; release-instance-child-shape-proposed
sensitivity_posture: no-public-path-by-default; rollback-is-governed-state-transition-not-file-move; not-delete; not-erasure; not-silent-edit; not-release-authority; not-proof-authority; not-receipt-family-authority-except-rollback-local-alias-revert-receipts; not-catalog-authority; not-policy-authority; not-emergency-alerting; not-current-warning-authority; not-life-safety-guidance; not-official-source-substitution; not-evacuation-routing-or-response-instruction; official-source-redirection-required; freshness-and-stale-state-required; source-role-preserving; temporal-state-preserving; warning-advisory-watch-context-only; regulatory-not-observed; detection-not-confirmation; model-not-observation; administrative-declaration-not-event-truth; sensitive-infrastructure-private-join-and-security-adjacent-detail-fail-closed; derivative-invalidation-required; evidence-aware; rights-aware; policy-aware; correction-aware; release-aware; rollback-target-required
related:
  - ../README.md
  - ../../README.md
  - ../../raw/hazards/README.md
  - ../../work/hazards/README.md
  - ../../quarantine/hazards/README.md
  - ../../processed/hazards/README.md
  - ../../catalog/domain/hazards/README.md
  - ../../registry/sources/hazards/README.md
  - ../../receipts/hazards/README.md
  - ../../proofs/hazards/README.md
  - ../../published/hazards/README.md
  - ../../published/layers/hazards/README.md
  - ../../reports/hazards/README.md
  - ../../../release/README.md
  - ../../../release/manifests/README.md
  - ../../../release/rollback_cards/
  - ../../../release/correction_notices/
  - ../../../release/withdrawal_notices/
  - ../../../docs/runbooks/ROLLBACK_RUNBOOK.md
  - ../../../docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/hazards/DATA_LIFECYCLE.md
  - ../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../../docs/domains/hazards/SOURCE_REGISTRY.md
  - ../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hazards/RELEASE_INDEX.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../contracts/domains/hazards/
  - ../../../contracts/release/
  - ../../../schemas/contracts/v1/domains/hazards/
  - ../../../schemas/contracts/v1/release/
  - ../../../policy/domains/hazards/
  - ../../../policy/release/hazards/
  - ../../../policy/sensitivity/hazards/
  - ../../../policy/rights/
tags:
  - kfm
  - data
  - rollback
  - hazards
  - not-emergency-alerting
  - not-life-safety-guidance
  - not-alert-authority
  - official-source-redirection
  - stale-state
  - freshness
  - hazard-event
  - hazard-observation
  - warning-context
  - advisory-context
  - disaster-declaration
  - flood-context
  - wildfire-detection
  - smoke-context
  - drought-indicator
  - earthquake-event
  - heat-cold-event
  - exposure-summary
  - resilience-summary
  - hazard-timeline
  - impact-area
  - regulatory-context
  - detection-not-confirmation
  - model-not-observation
  - source-role
  - temporal-semantics
  - rollback-card
  - alias-revert-receipt
  - release-manifest
  - correction-notice
  - withdrawal-notice
  - release-gated
  - rollback-target
  - correction-path
  - published-artifact
  - published-layer
  - evidence-bundle
  - proof-pack
  - validation-report
  - policy-decision
  - no-public-path
  - not-delete
  - not-erasure
  - not-file-move
  - derivative-invalidation
  - cite-or-abstain
notes:
  - "This README replaces an empty file at `data/rollback/hazards/README.md`."
  - "The parent `data/rollback/README.md` is currently empty, so this file is self-bounding and intentionally conservative."
  - "Directory Rules list `data/rollback/<domain>/<release_id>/` and say rollback may hold rollback cards and alias-revert receipts, but must not delete prior meanings."
  - "The release root says release decisions, manifests, promotion records, rollback cards, withdrawals, corrections, signatures, and changelog belong under `release/`, distinct from published artifacts."
  - "ADR-0015 proposes a two-plane alias mechanism: `release/rollback_cards/` owns rollback decision authority, while `data/rollback/` may hold data-plane alias-revert receipts. This README follows that separation without claiming ADR acceptance or implementation maturity."
  - "Hazards rollback support is downstream of release and correction governance. It does not replace EvidenceBundles, ProofPacks, receipts, catalog records, policy decisions, source-role decisions, freshness decisions, official-source references, release manifests, correction notices, withdrawal notices, source descriptors, schemas, contracts, or public payloads."
  - "Rollback material must not preserve or re-serve current-looking warnings, watches, advisories, emergency response context, regulatory context, detections, model outputs, exposure summaries, or AI/generated hazard answers after their release state is withdrawn, stale, corrected, or superseded."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards Rollback

Data-plane rollback support lane for Hazards release recovery, alias-revert receipts, affected-artifact indexes, stale-state and derivative invalidation, and rollback-local inspection material.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data" src="https://img.shields.io/badge/root-data%2F-0a7ea4">
  <img alt="Lane: rollback" src="https://img.shields.io/badge/lane-rollback-orange">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-b71c1c">
  <img alt="Boundary: not alerting" src="https://img.shields.io/badge/boundary-not%20alerting-critical">
  <img alt="Boundary: not release authority" src="https://img.shields.io/badge/boundary-not%20release%20authority-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Rollback boundary](#rollback-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Hazards rollback guardrails](#hazards-rollback-guardrails) · [Rollback flow](#rollback-flow) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!CAUTION]
> `data/rollback/hazards/` is not release authority, not publication authority, not proof, not general receipt storage, not catalog closure, not policy authority, not schema authority, not source registry authority, not emergency alerting, not current-warning authority, not official advisory replacement, not evacuation/routing/response guidance, not regulatory determination authority, not life-safety guidance, not erasure, not a delete mechanism, not a silent edit, not a file-move shortcut, and not a direct public UI/API source. Hazards rollback is a governed state transition with release-plane decision support, evidence/proof support, policy and source-role review, freshness and stale-state handling, correction/withdrawal state, derivative invalidation, and an auditable rollback target.

---

## Scope

`data/rollback/hazards/` may hold Hazards-domain data-plane rollback support material for a specific released Hazards artifact set or release alias transition.

This lane is appropriate for rollback-local material such as:

- alias-revert receipts tied to a release-plane `RollbackCard`;
- affected public-artifact indexes for Hazards releases, map layers, PMTiles, API payloads, reports, stories, dashboard snapshots, timelines, exports, graph/triplet projections, search surfaces, and AI answer surfaces;
- digest verification summaries for the release being rolled back and the target release being restored;
- rollback-local pointers to `ReleaseManifest`, `RollbackCard`, `CorrectionNotice`, `WithdrawalNotice`, EvidenceBundle, ProofPack, catalog records, receipts, policy decisions, validation reports, source descriptors, freshness checks, stale-state records, source-role records, and official-source references;
- stale-state, cache-invalidation, alias-resolution, derivative-invalidation, public-surface withdrawal, and governed-answer invalidation support;
- rollback drill material that is clearly marked as drill/test and not release authority;
- README files explaining local rollback boundaries.

A file here does **not** authorize rollback. It can record or support the data-plane effects of a rollback decision, but the release decision belongs under `release/` and must remain inspectable.

---

## Path posture

The existing target lane is:

```text
data/rollback/hazards/
```

Current placement evidence:

- `docs/doctrine/directory-rules.md` lists `data/rollback/<domain>/<release_id>/` in the data lifecycle tree.
- Directory Rules say rollback may hold rollback cards and alias-revert receipts, but must not delete prior meanings.
- `release/README.md` says release decisions, manifests, promotion records, rollback cards, withdrawals, corrections, signatures, and changelog belong under `release/`.
- `docs/runbooks/ROLLBACK_RUNBOOK.md` distinguishes release-plane rollback decisions from data-plane revert receipts and derivative invalidation.
- ADR-0015 proposes a two-plane mechanism where `release/rollback_cards/` owns the decision and `data/rollback/` owns data-plane alias-revert receipts. ADR-0015 is draft/proposed, so this README does not claim the mechanism is implemented or accepted.
- `data/rollback/README.md` is currently empty; this child README is therefore self-bounding.

Therefore this README treats `data/rollback/hazards/` as **CONFIRMED path presence / NEEDS VERIFICATION parent contract and instance layout**.

---

## Repo fit

| Responsibility | Correct home | Boundary |
|---|---|---|
| Hazards rollback data-plane support | `data/rollback/hazards/` | This lane; not release decision authority. |
| Rollback parent | [`../README.md`](../README.md) | Currently empty; parent contract still needs expansion. |
| Data root | [`../../README.md`](../../README.md) | Lifecycle data root; rollback is one data-plane family. |
| Release decisions | [`../../../release/`](../../../release/README.md) | `ReleaseManifest`, `PromotionDecision`, `RollbackCard`, `CorrectionNotice`, `WithdrawalNotice`, signatures, changelog. |
| Hazards published carriers | [`../../published/hazards/`](../../published/hazards/README.md) | Released public-safe carriers; not rollback decisions. |
| Hazards published map layers | [`../../published/layers/hazards/`](../../published/layers/hazards/README.md) | Released map-layer carriers; rollback support is required before release. |
| Hazards processed artifacts | [`../../processed/hazards/`](../../processed/hazards/README.md) | Upstream normalized artifacts; not rollback records. |
| Hazards catalog records | [`../../catalog/domain/hazards/`](../../catalog/domain/hazards/README.md) | Catalog closure and discovery records; not rollback decisions. |
| Hazards source registry | [`../../registry/sources/hazards/`](../../registry/sources/hazards/README.md) | Source admission, rights, sensitivity, source role, stale-state, and no-public-path posture; not rollback decisions. |
| Hazards receipts | [`../../receipts/hazards/`](../../receipts/hazards/README.md) | General process memory; rollback-local alias-revert receipts are narrow support records only. |
| Hazards proofs | [`../../proofs/hazards/`](../../proofs/hazards/README.md) | Evidence/proof support; rollback cites but does not replace. |
| Hazards report candidates | [`../../reports/hazards/`](../../reports/hazards/README.md) | Candidate/support narrative lane; not release or rollback authority. |
| Rollback runbook | [`../../../docs/runbooks/ROLLBACK_RUNBOOK.md`](../../../docs/runbooks/ROLLBACK_RUNBOOK.md) | Operational procedure; not data payload. |
| Alias governance ADR | [`../../../docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md`](../../../docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md) | Proposed alias/rollback mechanism; not proof of implementation. |
| Contracts, schemas, policy | `../../../contracts/`, `../../../schemas/`, `../../../policy/` | Meaning, machine shape, and allow/deny/restrict/abstain logic. |

---

## Rollback boundary

| Rule | Handling |
|---|---|
| Rollback is a governed transition | A rollback must resolve release decision, evidence/proof, policy, catalog, freshness, source-role, correction/withdrawal, and rollback target support. |
| Rollback is not deletion | Prior releases, meanings, receipts, proofs, catalog records, review records, and lineage remain inspectable unless a separate erasure process applies. |
| Rollback is not erasure | Privacy, rights, or legal erasure workflows require their own governed process; rollback support here must not masquerade as erasure. |
| Rollback is not a silent edit | Corrections and withdrawals require explicit release governance and visible supersession, stale-state, or withdrawal state. |
| Rollback is not a file move | Moving bytes between folders or changing an alias without release-plane authority is not rollback. |
| Release decision stays in `release/` | Primary `RollbackCard`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, signatures, and promotion decisions belong under `release/`. |
| Hazards is not alerting | Rollback records must not issue warnings, advisories, evacuation instructions, routing instructions, response guidance, health/safety guidance, exposure conclusions, or life-safety directions. |
| Official-source referral remains required | Warning, watch, advisory, disaster declaration, regulatory-context, and current-condition context must preserve issuing authority, valid/effective time, stale-state, and official-source reference where material. |
| Proof remains separate | EvidenceBundle, ProofPack, citation validation, and integrity proof stay in `data/proofs/`. |
| Receipts remain separate | General run/transform/validation/redaction/review/AI/release-support receipts stay in receipt lanes; this lane may hold rollback-local alias-revert receipts only. |
| Catalog remains separate | STAC/DCAT/PROV/domain catalog records stay in `data/catalog/`. |
| Published artifacts remain versioned | `data/published/` holds released artifacts; rollback records should not overwrite immutable release directories. |
| Policy remains separate | Sensitivity, rights, freshness, stale-state, official-advisory, source-role, redaction, aggregation, and public-release rules stay in `policy/`. |
| Public clients do not read this lane | Public UI/API/report/map surfaces consume governed APIs, released artifacts, catalog/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted material is limited to rollback-local support for Hazards release recovery:

- `alias_revert_receipt.json` or equivalent rollback-local receipt tied to a release-plane `RollbackCard`;
- rollback-local indexes of affected Hazards published artifacts, including historical hazard-event layers, warning/advisory/watch context layers, regulatory-context layers, disaster-declaration layers, flood-context layers, wildfire-detection layers, smoke-context layers, drought-indicator layers, earthquake-event layers, heat/cold layers, exposure/resilience summaries, reports, stories, API payloads, tiles, graph/triplet projections, search indexes, exports, and AI-answer surfaces;
- digest verification summaries comparing `from_release_id`, `to_release_id`, affected artifact digests, and resolved published paths;
- freshness, stale-state, valid/effective time, issue/expiry time, observed time, retrieval time, model-run time, release time, correction time, and official-source-reference summaries;
- public-surface invalidation records for maps, APIs, reports, story snapshots, Evidence Drawer payloads, Focus Mode answers, model summaries, search indexes, graph edges, caches, screenshots, exports, and tiles;
- references to ReleaseManifest, RollbackCard, CorrectionNotice, WithdrawalNotice, PromotionDecision, signatures, EvidenceBundle, ProofPack, catalog records, receipts, PolicyDecision, ReviewRecord, ValidationReport, TransformReceipt, ModelRunReceipt, AIReceipt, and release-review records;
- rollback drill artifacts that are clearly marked as drill/test and never treated as release authority;
- local README files and indexes that help stewards inspect rollback state without becoming release, proof, catalog, policy, source-registry, official advisory, emergency authority, or public authority.

All accepted material must preserve release identity, prior release identity, target release identity, affected artifact identity, digest references, evidence/proof references, source-role state, time/freshness state, official-source posture, policy state, review state, correction/withdrawal state, actor/runner identity, timestamp, and finite outcome where material.

Do **not** embed unsupported current-condition claims in rollback support. Use governed pointers, release IDs, digests, stale-state records, and public-safe artifact IDs.

---

## Exclusions

| Do not place here | Correct home | Why |
|---|---|---|
| RAW source captures, alert feeds, agency snapshots, source reports, incident source packets, source-native rasters/vectors/tables, model files, advisory text dumps, logs, uploads, or source mirrors | `../../raw/hazards/`, `../../work/hazards/`, or `../../quarantine/hazards/` | Source-edge and unsafe material requires source metadata, checksums, rights, source-role, and sensitivity controls. |
| WORK scratch, rollback experiments, transform intermediates, repair attempts, unit/time normalization scratch, redaction trials, model experiments, or unresolved joins | `../../work/hazards/` or `../../quarantine/hazards/` | Unresolved material belongs upstream or in hold lanes. |
| Normalized Hazards datasets | `../../processed/hazards/` | Processed data is not rollback support. |
| Catalog, STAC, DCAT, PROV, or graph/triplet records | `../../catalog/`, `../../triplets/` | Catalog and graph carriers have their own closure rules. |
| EvidenceBundle, ProofPack, CitationValidationReport, or integrity proof | `../../proofs/hazards/` or accepted proof lanes | Proof is the trust spine; rollback cites it. |
| General RunReceipt, TransformReceipt, UnitConversionReceipt, ValidationReceipt, ModelRunReceipt, PolicyDecision, ReviewRecord, AIReceipt, or release-support receipt families | `../../receipts/hazards/` or accepted receipt/review lanes | General process memory belongs in receipt lanes; rollback-local receipts are narrow exceptions. |
| SourceDescriptor, source activation records, rights registry records, sensitivity registry records, source-family records, or access-control records | `../../registry/`, `policy/`, or accepted governance roots | Registry and control records belong in their own authority lanes. |
| Primary ReleaseManifest, RollbackCard, PromotionDecision, CorrectionNotice, WithdrawalNotice, signatures, or release changelog | `../../../release/` | Release decisions belong in release authority. |
| Published public artifacts | `../../published/hazards/`, `../../published/layers/hazards/`, or other released artifact lanes | Rollback support does not own public artifacts. |
| Public reports or steward-facing generated narratives | `../../published/reports/`, `../../../docs/reports/` | Report lanes have separate authority. |
| Contracts, schemas, policy rules, validators, tests, code, or workflows | `../../../contracts/`, `../../../schemas/`, `../../../policy/`, `../../../tools/`, `../../../tests/`, `.github/workflows/` | Separate authority roots. |
| Emergency alerts, official advisory issuance, evacuation advice, routing guidance, response instructions, medical/health guidance, exposure conclusions, regulatory determinations, current operational warning instructions, or life-safety directions | Official authorities or governed public-release surfaces outside this rollback lane | KFM Hazards is context and evidence, not an operational authority. |
| Unsupported warning-as-current, advisory-as-current, regulatory-as-observed, detection-as-confirmed, model-as-observation, declaration-as-event-truth, or KFM-as-official-source claims | Corrected upstream or withdrawn public surface | Rollback must not preserve the role collapse that caused the defect. |
| Security-sensitive infrastructure context, exact sensitive facility context, private person/parcel joins, emergency-response detail, tribal/cultural/archaeology-sensitive joins, rare-species-sensitive joins, or re-identifying joins | Restricted governed lanes only; public-safe derivative after policy/review/release | Rollback must not become a sensitivity or rights bypass. |

---

## Hazards rollback guardrails

| Risk | Guardrail |
|---|---|
| Deleting prior meaning | Rollback preserves prior release records, evidence, receipts, catalog records, review records, and lineage unless a separate governed erasure process applies. |
| Alias-only rollback | A current-pointer or alias change is insufficient unless tied to release-plane decision authority, digest verification, review state, and rollback-local receipt support. |
| Public artifact overwrite | Immutable release artifacts must not be overwritten in place. Reseat pointers or publish a governed correction/supersession. |
| Current-looking stale surface | Any withdrawn or stale warning, advisory, watch, declaration, detection, forecast/model, regulatory-context layer, hazard timeline, exposure summary, or API payload must be invalidated or marked stale. |
| Official-source bypass | Hazard surfaces must redirect urgent or authoritative action to official sources and preserve issuing authority, valid/effective time, and stale-state. KFM must not restyle context as its own warning. |
| Warning/advisory/current-state collapse | WarningContext and AdvisoryContext are time-bound context. Expired or stale operational context must not be restored as current state. |
| Regulatory/observed collapse | NFHL or other regulatory hazard areas are regulatory context, not observed inundation, forecast hazard, or emergency status. |
| Detection/confirmation collapse | Remote-sensing detections and candidate reports are not confirmed ground events, legal perimeters, or response status without reviewed evidence. |
| Model/observation collapse | Forecasts, scenarios, exposure summaries, smoke trajectories, drought indicators, and modeled surfaces must not be restored as observations. |
| Declaration/event collapse | Disaster declarations and administrative records are administrative context, not observed event proof or damage truth by themselves. |
| Unit/time flattening | Event, observed, valid/effective, issue, expiry, source, retrieval, model-run, release, correction, and stale-state times must remain distinct. |
| Cross-lane impact overclaim | Hazards rollback cannot decide Atmosphere, Hydrology, Roads/Rail, Settlements/Infrastructure, People/Land, Agriculture, Geology, Soil, Flora, Fauna, Habitat, or Archaeology truth. It invalidates affected context and forces owning-lane review. |
| Sensitive exposure joins | Infrastructure-sensitive detail, private person/parcel joins, response-sensitive detail, archaeology/cultural/tribal context, rare-species context, and re-identifying joins fail closed during rollback. |
| Stale public surface | Map layers, API payloads, reports, indexes, tiles, stories, graph/triplet exports, Evidence Drawer payloads, Focus Mode answers, search surfaces, and AI answers must be invalidated or marked stale when rollback affects them. |
| Proof bypass | Rollback cannot repair a claim by hiding evidence gaps. EvidenceBundle/proof closure must still support the restored or superseding release. |
| Catalog bypass | Catalog, STAC, DCAT, PROV, and domain catalog state must be corrected or invalidated alongside published artifacts. |
| AI surface drift | Generated Hazards answers, Focus Mode surfaces, report summaries, story text, and Evidence Drawer prose must not keep citing withdrawn, stale, role-collapsed, or unsupported release state. |
| File-move shortcut | Moving, renaming, or copying files under `data/published/` is not rollback unless release governance, receipts, proof, policy, review, and catalog closure support it. |

---

## Rollback flow

```mermaid
flowchart LR
    DETECT[Defect or stale exposure detected] --> CLASSIFY[Classify affected Hazards surfaces]
    CLASSIFY --> FREEZE[Freeze or mark current-looking public surfaces stale]
    FREEZE --> RELEASE[Locate ReleaseManifest and rollback target]
    RELEASE --> REVIEW[Verify freshness / source-role / official-source / policy state]
    REVIEW --> PROOF[Verify EvidenceBundle, proof, receipts, catalog]
    PROOF --> DECISION[Release-plane RollbackCard / CorrectionNotice / WithdrawalNotice]
    DECISION --> DATA[data/rollback/hazards receipt support]
    DATA --> INVALIDATE[Invalidate aliases, maps, tiles, reports, graph, search, AI surfaces]
    INVALIDATE --> RESTORE[Restore or publish governed public-safe target]
    RESTORE --> RECORD[Record correction path, rollback target, digests, status]

    classDef gate fill:#fff3cd,stroke:#8a6d3b,color:#202124;
    classDef hold fill:#f8d7da,stroke:#842029,color:#202124;
    class DECISION gate;
    class FREEZE hold;
```

> [!NOTE]
> This diagram is a responsibility map, not proof that rollback tooling, validators, alias resolvers, release manifests, rollback cards, freshness evaluators, cache invalidation, or CI gates currently exist.

---

## Suggested directory shape

This shape follows the Directory Rules pattern `data/rollback/<domain>/<release_id>/` and remains **PROPOSED** until parent rollback governance or an accepted ADR confirms exact file names. Do not pre-create empty stubs.

```text
data/rollback/hazards/
├── README.md
├── <release_id>/
│   ├── alias_revert_receipt.json
│   ├── rollback.data_plane_receipt.json
│   ├── affected_artifacts.index.json
│   ├── digest_verification.json
│   ├── invalidation_refs.json
│   ├── release_refs.json
│   ├── evidence_refs.json
│   ├── freshness_refs.json
│   ├── source_role_refs.json
│   ├── official_source_refs.json
│   ├── policy_refs.json
│   ├── stale_state.json
│   └── README.md
├── drills/                              # PROPOSED: rollback drill outputs, clearly marked non-production
│   └── <drill_id>/
└── indexes/                             # PROPOSED: rollback-local indexes only
    └── hazards.rollback.index.json
```

Recommended minimal release-instance fields:

| Field | Purpose |
|---|---|
| `rollback_id` | Stable identifier for the data-plane rollback support record. |
| `release_id` | Defective, withdrawn, superseded, stale, or role-collapsed release being addressed. |
| `target_release_id` | Prior or superseding release selected by release authority. |
| `rollback_card_ref` | Pointer to release-plane decision authority. |
| `release_manifest_ref` | Pointer to affected ReleaseManifest. |
| `affected_artifacts` | Published artifacts, aliases, catalog records, graph exports, reports, tiles, stories, API payloads, search surfaces, and AI surfaces affected. |
| `source_role_defect_class` | Public-safe classification of source-role, freshness, warning/advisory, regulatory, detection, declaration, model, or caveat defect. |
| `freshness_refs` | Pointers to stale-state, observed/valid/issue/expiry/retrieval/release/model-run time checks. |
| `official_source_refs` | Official issuing-authority links or source IDs for warning/current-context material. |
| `digest_verification` | Hash/digest checks for defective and target artifacts. |
| `policy_state` | Policy/review disposition for restored or superseding public surface. |
| `evidence_refs` | EvidenceBundle/proof references needed to inspect restored claims. |
| `invalidation_refs` | Downstream invalidation or stale-state records. |
| `outcome` | Finite outcome such as `RESTORED`, `WITHDRAWN`, `SUPERSEDED`, `HELD`, `DENIED`, `ABSTAIN`, or `ERROR`. |

---

## Required checks before use

- [ ] Confirm whether `data/rollback/README.md` should define a parent rollback contract, and update this README if parent rules change.
- [ ] Confirm exact rollback instance naming under `data/rollback/hazards/<release_id>/`.
- [ ] Confirm the release-plane `RollbackCard`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, and signatures exist where required.
- [ ] Confirm the rollback target resolves to a prior or superseding release with digest closure.
- [ ] Confirm EvidenceBundle, ProofPack, catalog, receipt, policy, rights, sensitivity, freshness, source-role, official-source, and release support resolve for both the defective and target release where material.
- [ ] Confirm stale or withdrawn Hazards map layers, API payloads, reports, PMTiles, story snapshots, graph/triplet projections, search indexes, Evidence Drawer payloads, Focus Mode answers, and AI-answer surfaces are invalidated or marked stale.
- [ ] Confirm rollback records do not embed unsupported current-condition claims, official-advisory replacements, emergency instructions, exposure conclusions, regulatory determinations, evacuation/routing/response guidance, or life-safety guidance.
- [ ] Confirm warning/current-state, advisory/current-state, regulatory/observed, detection/confirmation, model/observation, declaration/event, administrative/evidence, and official-source/KFM boundaries are not collapsed in the restored state.
- [ ] Confirm event time, observed time, valid/effective time, issue/expiry time, source time, retrieval time, release time, correction time, stale-state time, and model-run time remain visible where material.
- [ ] Confirm infrastructure-sensitive, emergency-response-sensitive, private person/parcel, tribal/cultural/archaeology, rare-species, proprietary, rights-unclear, and re-identifying joins fail closed until policy and review allow public-safe representation.
- [ ] Confirm rollback does not delete prior meanings, overwrite immutable release artifacts, bypass catalog/proof/policy/release/review checks, or expose restricted detail.
- [ ] Confirm public clients resolve restored state through governed API or released artifact aliases, not by reading this rollback lane.
- [ ] Confirm rollback-local receipt support is referenced by release/proof governance without becoming release authority itself.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target path presence | CONFIRMED | `data/rollback/hazards/README.md` existed as an empty file before this update. |
| Parent rollback README | CONFIRMED empty | `data/rollback/README.md` exists but is empty, so parent rollback contract remains NEEDS VERIFICATION. |
| Directory Rules rollback path | CONFIRMED doctrine | Directory Rules list `data/rollback/<domain>/<release_id>/` and warn rollback must not delete prior meanings. |
| Release root decision authority | CONFIRMED README | `release/README.md` says release decisions, manifests, promotion records, rollback cards, withdrawals, corrections, signatures, and changelog belong under `release/`. |
| Hazards domain doctrine | CONFIRMED README | `docs/domains/hazards/README.md` establishes Hazards scope, source-role discipline, cross-lane non-ownership, not-for-life-safety posture, and rollback/correction orientation. |
| Hazards publication and boundary doctrine | CONFIRMED README | `docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md` establishes not-for-life-safety posture, governed publication path, stale-state, correction, and rollback requirements. |
| Hazards lifecycle doctrine | CONFIRMED README | `docs/domains/hazards/DATA_LIFECYCLE.md` establishes RAW-to-PUBLISHED traversal, operational-context freshness rules, source-role anti-collapse, and correction/rollback expectations. |
| Hazards published domain lane | CONFIRMED README | `data/published/hazards/README.md` requires release authority, evidence support, validation, policy review, catalog closure, correction path, and rollback support before public artifacts land there. |
| Hazards published layer lane | CONFIRMED README | `data/published/layers/hazards/README.md` requires release support, life-safety disclaimer, official-source referral, correction path, rollback target, and governed public interfaces. |
| Hazards processed lane | CONFIRMED README | `data/processed/hazards/README.md` is upstream and says public use requires governed catalog, evidence, source-role/freshness/rights posture, policy review, release state, correction path, and rollback target. |
| Hazards catalog lane | CONFIRMED README | `data/catalog/domain/hazards/README.md` says catalog records are not release authority and require evidence/source/freshness/policy/release references for public records. |
| Hazards receipts lane | CONFIRMED README | `data/receipts/hazards/README.md` defines receipt process memory and includes rollback-support context without making receipts proof or release authority. |
| Hazards proofs lane | CONFIRMED README | `data/proofs/hazards/README.md` defines proof support and excludes primary RollbackCard/ReleaseManifest ownership. |
| Hazards source registry | CONFIRMED README | `data/registry/sources/hazards/README.md` establishes source admission, source-role preservation, stale-state, official-source redirection, not-alerting boundary, and no-public-path posture. |
| Hazards reports lane | CONFIRMED README | `data/reports/hazards/README.md` establishes report-candidate boundaries and not-alerting guardrails; reports are not rollback authority. |
| Rollback runbook | CONFIRMED README | `docs/runbooks/ROLLBACK_RUNBOOK.md` describes rollback as a governed release transition and distinguishes decision artifacts from data-plane revert receipts. |
| Alias rollback ADR | CONFIRMED draft ADR | ADR-0015 proposes current-alias governance by RollbackCard and data-plane alias-revert receipts. |
| Actual rollback instances | UNKNOWN | This README does not prove any Hazards rollback instance exists. |
| Rollback tooling, validators, CI, signatures, alias resolver, cache invalidation | NEEDS VERIFICATION | No runtime enforcement was proven by this edit. |
| Public release readiness | DENY until proven | A rollback README cannot publish, restore, or expose Hazards claims by itself. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `data/rollback/hazards/README.md` existed as an empty file. | Did not define lane boundaries. |
| [`../README.md`](../README.md) | CONFIRMED empty | Parent rollback root exists. | Does not yet define parent rollback contract. |
| [`../../README.md`](../../README.md) | CONFIRMED | Data root includes lifecycle data families. | Does not prove rollback payloads or enforcement. |
| [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) | CONFIRMED doctrine | `data/rollback/<domain>/<release_id>/`; rollback must not delete prior meanings; promotion is governed state transition. | Exact rollback instance file names remain unresolved. |
| [`../../../release/README.md`](../../../release/README.md) | CONFIRMED README | Release decision artifacts belong under `release/`, distinct from `data/published/`. | Release root README is short and status `PROPOSED`; does not prove concrete release artifacts. |
| [`../../../docs/runbooks/ROLLBACK_RUNBOOK.md`](../../../docs/runbooks/ROLLBACK_RUNBOOK.md) | CONFIRMED draft runbook | Rollback governs PUBLISHED releases, rollback cards, correction notices, withdrawal of public surfaces, derivative invalidation, and data-plane revert receipts. | Runbook notes implementation is PROPOSED/NEEDS VERIFICATION in places. |
| [`../../../docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md`](../../../docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md) | CONFIRMED draft ADR | Proposed two-plane alias rollback mechanism: release-plane RollbackCard and data-plane alias-revert receipt. | ADR is draft/proposed and does not prove implementation. |
| [`../../../docs/domains/hazards/README.md`](../../../docs/domains/hazards/README.md) | CONFIRMED doctrine / PROPOSED implementation | Hazards scope, object families, source-role discipline, not-for-life-safety posture, cross-lane non-ownership, and correction/rollback posture. | Implementation maturity remains NEEDS VERIFICATION in parts. |
| [`../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`](../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md) | CONFIRMED doctrine / PROPOSED implementation | Hazards publication boundary, governed publication path, stale-state, correction, rollback, and not-alert-authority posture. | Does not prove runtime enforcement. |
| [`../../../docs/domains/hazards/DATA_LIFECYCLE.md`](../../../docs/domains/hazards/DATA_LIFECYCLE.md) | CONFIRMED doctrine / PROPOSED implementation | Hazards lifecycle, operational-context freshness rules, source-role anti-collapse, correction/rollback expectations, and trust-membrane posture. | Does not prove runtime enforcement. |
| [`../../published/hazards/README.md`](../../published/hazards/README.md) | CONFIRMED README | Hazards published artifacts require release authority, evidence support, validation, policy review, catalog closure, correction path, and rollback support. | Does not prove released artifacts exist. |
| [`../../published/layers/hazards/README.md`](../../published/layers/hazards/README.md) | CONFIRMED README | Hazards published layers require release support, official-source referral, not-alerting posture, correction path, rollback target, and governed public interfaces. | Does not prove layer payloads or release manifests exist. |
| [`../../processed/hazards/README.md`](../../processed/hazards/README.md) | CONFIRMED README | Processed Hazards is upstream of catalog/release and requires correction path and rollback target for public use. | Does not prove processed inventory. |
| [`../../catalog/domain/hazards/README.md`](../../catalog/domain/hazards/README.md) | CONFIRMED README | Hazards catalog lane requires evidence, source, freshness, policy, release, and rollback references for public records. | Catalog records are not rollback decisions. |
| [`../../receipts/hazards/README.md`](../../receipts/hazards/README.md) | CONFIRMED README | Hazards receipts are process memory and include rollback-support context while excluding proof/release authority. | General receipts are not release/proof authority. |
| [`../../proofs/hazards/README.md`](../../proofs/hazards/README.md) | CONFIRMED README | Hazards proofs support evidence closure, source-role proof, freshness/expiry checks, and rollback proof; primary release records remain in `release/`. | Proof lane does not publish or roll back by itself. |
| [`../../registry/sources/hazards/README.md`](../../registry/sources/hazards/README.md) | CONFIRMED README | Source registry establishes admission, rights, source role, stale-state, official-source redirection, not-alerting boundary, and no-public-path posture. | Source registry records do not authorize rollback or publication. |
| [`../../reports/hazards/README.md`](../../reports/hazards/README.md) | CONFIRMED README | Hazards reports are report-candidate/report-support downstream carriers with not-alerting and source-role guardrails. | Reports are not rollback decisions or public release authority. |

[Back to top](#top)
