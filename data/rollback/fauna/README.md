<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/rollback/fauna/readme
name: Fauna Rollback README
path: data/rollback/fauna/README.md
type: data-rollback-fauna-readme
version: v0.1.0
status: draft
owners:
  - <data-steward>
  - <rollback-steward>
  - <release-steward>
  - <fauna-domain-steward>
  - <sensitive-species-reviewer>
  - <geoprivacy-steward>
  - <rights-holder-representative>
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
domain: fauna
artifact_family: rollback-receipt-and-alias-revert-support-lane
path_posture: existing-empty-file-replaced; parent-data-rollback-readme-is-empty; directory-rules-lists-data-rollback-domain-release-id; release-root-owns-release-decisions; adr-0015-two-plane-alias-rollback-mechanism-is-proposed; fauna-domain-rollback-lane-self-bounded; release-instance-child-shape-proposed
sensitivity_posture: no-public-path-by-default; rollback-is-governed-state-transition-not-file-move; not-delete; not-erasure; not-silent-edit; not-release-authority; not-proof-authority; not-receipt-family-authority-except-rollback-local-alias-revert-receipts; not-catalog-authority; not-policy-authority; fauna-sensitive-occurrence-t4-deny-default; exact-sensitive-geometry-denied; nests-dens-roosts-hibernacula-spawning-sites-breeding-sites-aggregation-sites-telemetry-tracks-steward-controlled-records-private-landowner-detail-fail-closed; geoprivacy-transform-support-required; redaction-generalization-aggregation-review-release-support-required; derivative-invalidation-required; evidence-aware; rights-aware; policy-aware; correction-aware; release-aware; rollback-target-required
related:
  - ../README.md
  - ../../README.md
  - ../../raw/fauna/README.md
  - ../../work/fauna/README.md
  - ../../quarantine/fauna/README.md
  - ../../processed/fauna/README.md
  - ../../processed/fauna/public/README.md
  - ../../processed/fauna/restricted/README.md
  - ../../catalog/domain/fauna/README.md
  - ../../registry/sources/fauna/README.md
  - ../../receipts/fauna/README.md
  - ../../receipts/fauna/redaction/README.md
  - ../../proofs/fauna/README.md
  - ../../published/README.md
  - ../../published/fauna/README.md
  - ../../published/layers/fauna/README.md
  - ../../published/layers/fauna/occurrence_tiles/README.md
  - ../../published/layers/fauna/range/README.md
  - ../../published/layers/fauna/range_generalized/README.md
  - ../../reports/fauna/README.md
  - ../../../release/README.md
  - ../../../release/manifests/README.md
  - ../../../release/rollback_cards/
  - ../../../release/correction_notices/
  - ../../../release/withdrawal_notices/
  - ../../../docs/runbooks/ROLLBACK_RUNBOOK.md
  - ../../../docs/runbooks/fauna/PROMOTION_RUNBOOK.md
  - ../../../docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md
  - ../../../docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md
  - ../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/domains/fauna/README.md
  - ../../../docs/domains/fauna/DATA_LIFECYCLE.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../docs/domains/fauna/SOURCE_ROLES.md
  - ../../../docs/domains/fauna/SOURCE_FAMILIES.md
  - ../../../docs/domains/fauna/MAP_UI_CONTRACTS.md
  - ../../../docs/domains/fauna/RELEASE_INDEX.md
  - ../../../docs/domains/fauna/CANONICAL_PATHS.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../contracts/domains/fauna/
  - ../../../contracts/release/
  - ../../../schemas/contracts/v1/domains/fauna/
  - ../../../schemas/contracts/v1/release/
  - ../../../policy/domains/fauna/
  - ../../../policy/release/fauna/
  - ../../../policy/sensitivity/fauna/
  - ../../../policy/geoprivacy/
  - ../../../policy/rights/
tags:
  - kfm
  - data
  - rollback
  - fauna
  - wildlife
  - biodiversity
  - rare-species
  - sensitive-species
  - sensitive-occurrence
  - sensitive-site
  - nest
  - den
  - roost
  - hibernacula
  - spawning-site
  - breeding-site
  - aggregation-site
  - telemetry
  - movement-trace
  - range
  - seasonal-range
  - migration-route
  - occurrence-tiles
  - generalized-range
  - geoprivacy
  - redaction-receipt
  - aggregation-receipt
  - review-record
  - policy-decision
  - rollback-card
  - alias-revert-receipt
  - release-manifest
  - correction-notice
  - withdrawal-notice
  - promotion-decision
  - release-gated
  - rollback-target
  - correction-path
  - current-alias
  - published-artifact
  - published-layer
  - evidence-bundle
  - proof-pack
  - source-role
  - sensitivity
  - t4-deny
  - exact-location-denial
  - no-public-path
  - not-delete
  - not-erasure
  - not-file-move
  - derivative-invalidation
  - cite-or-abstain
notes:
  - "This README replaces an empty file at `data/rollback/fauna/README.md`."
  - "The parent `data/rollback/README.md` is currently empty, so this file is self-bounding and intentionally conservative."
  - "Directory Rules v1.4 lists `data/rollback/<domain>/<release_id>/` and says rollback may hold rollback cards and alias-revert receipts, but must not delete prior meanings."
  - "The release root says release decisions, manifests, promotion records, rollback cards, withdrawals, corrections, signatures, and changelog belong under `release/`, distinct from published artifacts."
  - "ADR-0015 proposes a two-plane alias mechanism: `release/rollback_cards/` owns rollback decision authority, while `data/rollback/` may hold data-plane alias-revert receipts. This README follows that separation without claiming ADR acceptance or implementation maturity."
  - "Fauna rollback support is downstream of release and correction governance. It does not replace EvidenceBundles, ProofPacks, receipts, catalog records, policy decisions, geoprivacy/redaction receipts, review records, release manifests, correction notices, withdrawal notices, source descriptors, schemas, contracts, or public payloads."
  - "Rollback material must not preserve or re-expose exact sensitive occurrence geometry, nests, dens, roosts, hibernacula, spawning sites, breeding/aggregation sites, telemetry tracks, steward-controlled records, private-landowner detail, or reverse-engineerable derivatives."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Rollback

Data-plane rollback support lane for Fauna release recovery, alias-revert receipts, affected-artifact indexes, geoprivacy-sensitive derivative invalidation, and rollback-local inspection material.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data" src="https://img.shields.io/badge/root-data%2F-0a7ea4">
  <img alt="Lane: rollback" src="https://img.shields.io/badge/lane-rollback-orange">
  <img alt="Domain: fauna" src="https://img.shields.io/badge/domain-fauna-2e7d32">
  <img alt="Sensitivity: T4 deny" src="https://img.shields.io/badge/sensitivity-T4%20DENY-critical">
  <img alt="Boundary: not release authority" src="https://img.shields.io/badge/boundary-not%20release%20authority-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Rollback boundary](#rollback-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Fauna rollback guardrails](#fauna-rollback-guardrails) · [Rollback flow](#rollback-flow) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!CAUTION]
> `data/rollback/fauna/` is not release authority, not publication authority, not proof, not general receipt storage, not catalog closure, not policy authority, not schema authority, not source registry authority, not species-location truth, not conservation-status truth, not telemetry authority, not operational wildlife guidance, not hunting/fishing/legal advice, not an emergency-alert surface, not erasure, not a delete mechanism, not a silent edit, not a file-move shortcut, and not a direct public UI/API source. Fauna rollback is a governed state transition with release-plane decision support, evidence/proof support, policy and sensitivity review, geoprivacy/redaction support, correction/withdrawal state, derivative invalidation, and an auditable rollback target.

---

## Scope

`data/rollback/fauna/` may hold Fauna-domain data-plane rollback support material for a specific released Fauna artifact set or release alias transition.

This lane is appropriate for rollback-local material such as:

- alias-revert receipts tied to a release-plane `RollbackCard`;
- affected public-artifact indexes for Fauna releases, occurrence tiles, range layers, generalized range layers, public summaries, reports, stories, API payloads, exports, graph/triplet projections, search surfaces, and AI answer surfaces;
- digest verification summaries for the release being rolled back and the target release being restored;
- rollback-local pointers to `ReleaseManifest`, `RollbackCard`, `CorrectionNotice`, `WithdrawalNotice`, EvidenceBundle, ProofPack, catalog records, receipts, policy decisions, review records, geoprivacy transform records, RedactionReceipt, AggregationReceipt, and source registry records;
- stale-state, cache-invalidation, alias-resolution, derivative-invalidation, public-surface withdrawal, and governed-answer invalidation support;
- rollback drill material that is clearly marked as drill/test and not release authority;
- README files explaining local rollback boundaries.

A file here does **not** authorize rollback. It can record or support the data-plane effects of a rollback decision, but the release decision belongs under `release/` and must remain inspectable.

---

## Path posture

The existing target lane is:

```text
data/rollback/fauna/
```

Current placement evidence:

- `docs/doctrine/directory-rules.md` lists `data/rollback/<domain>/<release_id>/` in the data lifecycle tree.
- Directory Rules say rollback may hold rollback cards and alias-revert receipts, but must not delete prior meanings.
- `release/README.md` says release decisions, manifests, promotion records, rollback cards, withdrawals, corrections, signatures, and changelog belong under `release/`.
- `docs/runbooks/ROLLBACK_RUNBOOK.md` distinguishes release-plane rollback decisions from data-plane revert receipts and derivative invalidation.
- ADR-0015 proposes a two-plane mechanism where `release/rollback_cards/` owns the decision and `data/rollback/` owns data-plane alias-revert receipts. ADR-0015 is draft/proposed, so this README does not claim the mechanism is implemented or accepted.
- `data/rollback/README.md` is currently empty; this child README is therefore self-bounding.

Therefore this README treats `data/rollback/fauna/` as **CONFIRMED path presence / NEEDS VERIFICATION parent contract and instance layout**.

---

## Repo fit

| Responsibility | Correct home | Boundary |
|---|---|---|
| Fauna rollback data-plane support | `data/rollback/fauna/` | This lane; not release decision authority. |
| Rollback parent | [`../README.md`](../README.md) | Currently empty; parent contract still needs expansion. |
| Data root | [`../../README.md`](../../README.md) | Lifecycle data root; rollback is one data-plane family. |
| Release decisions | [`../../../release/`](../../../release/README.md) | `ReleaseManifest`, `PromotionDecision`, `RollbackCard`, `CorrectionNotice`, `WithdrawalNotice`, signatures, changelog. |
| Fauna published carriers | [`../../published/fauna/`](../../published/fauna/README.md) | Released public-safe carriers; not rollback decisions. |
| Fauna published map layers | [`../../published/layers/fauna/`](../../published/layers/fauna/README.md) | Released map-layer carriers; rollback support is required before release. |
| Fauna processed artifacts | [`../../processed/fauna/`](../../processed/fauna/README.md) | Upstream normalized artifacts; not rollback records. |
| Fauna catalog records | [`../../catalog/domain/fauna/`](../../catalog/domain/fauna/README.md) | Catalog closure and discovery records; not rollback decisions. |
| Fauna source registry | [`../../registry/sources/fauna/`](../../registry/sources/fauna/README.md) | Source admission, rights, sensitivity, source role, stale-state, and no-public-path posture; not rollback decisions. |
| Fauna receipts | [`../../receipts/fauna/`](../../receipts/fauna/README.md) | General process memory; rollback-local alias-revert receipts are narrow support records only. |
| Fauna proofs | [`../../proofs/fauna/`](../../proofs/fauna/README.md) | Evidence/proof support; rollback cites but does not replace. |
| Fauna report candidates | [`../../reports/fauna/`](../../reports/fauna/README.md) | Candidate/support narrative lane; not release or rollback authority. |
| Rollback runbook | [`../../../docs/runbooks/ROLLBACK_RUNBOOK.md`](../../../docs/runbooks/ROLLBACK_RUNBOOK.md) | Operational procedure; not data payload. |
| Deny-by-default ADR | [`../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md`](../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) | Draft cross-domain fail-closed policy posture for rare-species exact-location exposure and other high-risk classes. |
| Alias governance ADR | [`../../../docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md`](../../../docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md) | Proposed alias/rollback mechanism; not proof of implementation. |
| Contracts, schemas, policy | `../../../contracts/`, `../../../schemas/`, `../../../policy/` | Meaning, machine shape, and allow/deny/restrict/abstain logic. |

---

## Rollback boundary

| Rule | Handling |
|---|---|
| Rollback is a governed transition | A rollback must resolve release decision, evidence/proof, policy, catalog, sensitivity/geoprivacy review, correction/withdrawal, and rollback target support. |
| Rollback is not deletion | Prior releases, meanings, receipts, proofs, catalog records, review records, and lineage remain inspectable unless a separate erasure process applies. |
| Rollback is not erasure | Privacy, rights, consent, or legal erasure workflows require their own governed process; rollback support here must not masquerade as erasure. |
| Rollback is not a silent edit | Corrections and withdrawals require explicit release governance and visible supersession, stale-state, or withdrawal state. |
| Rollback is not a file move | Moving bytes between folders or changing an alias without release-plane authority is not rollback. |
| Release decision stays in `release/` | Primary `RollbackCard`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, signatures, and promotion decisions belong under `release/`. |
| Fauna sensitivity still fails closed | Sensitive taxa, exact occurrences, nests, dens, roosts, hibernacula, spawning sites, breeding/aggregation sites, telemetry tracks, steward-controlled records, and private-land detail remain denied unless public-safe support exists. |
| Geoprivacy and review remain load-bearing | Rollback cannot skip redaction/generalization/aggregation receipts, reviewer state, rights posture, source-role posture, or release review. |
| Proof remains separate | EvidenceBundle, ProofPack, citation validation, and integrity proof stay in `data/proofs/`. |
| Receipts remain separate | General run/transform/validation/redaction/review/AI/release-support receipts stay in receipt lanes; this lane may hold rollback-local alias-revert receipts only. |
| Catalog remains separate | STAC/DCAT/PROV/domain catalog records stay in `data/catalog/`. |
| Published artifacts remain versioned | `data/published/` holds released artifacts; rollback records should not overwrite immutable release directories. |
| Policy remains separate | Sensitivity, rights, geoprivacy, source-role, redaction, generalization, aggregation, suppression, embargo, and public-release rules stay in `policy/`. |
| Public clients do not read this lane | Public UI/API/report/map surfaces consume governed APIs, released artifacts, catalog/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted material is limited to rollback-local support for Fauna release recovery:

- `alias_revert_receipt.json` or equivalent rollback-local receipt tied to a release-plane `RollbackCard`;
- rollback-local indexes of affected Fauna published artifacts, including occurrence tiles, range layers, generalized range layers, seasonal-range layers, migration-route public derivatives, species-richness summaries, abundance summaries, mortality/disease/invasive public-context surfaces, reports, stories, API payloads, graph/triplet projections, search indexes, exports, and AI-answer surfaces;
- digest verification summaries comparing `from_release_id`, `to_release_id`, affected artifact digests, and resolved published paths;
- public-surface invalidation and stale-state records for maps, APIs, reports, story snapshots, Evidence Drawer payloads, Focus Mode answers, model summaries, search indexes, graph edges, caches, screenshots, exports, PMTiles, tiles, and public downloads;
- references to ReleaseManifest, RollbackCard, CorrectionNotice, WithdrawalNotice, PromotionDecision, signatures, EvidenceBundle, ProofPack, catalog records, source registry records, RedactionReceipt, AggregationReceipt, ValidationReport, PolicyDecision, ReviewRecord, AIReceipt, and release-review records;
- rollback drill artifacts that are clearly marked as drill/test and never treated as release authority;
- local README files and indexes that help stewards inspect rollback state without becoming release, proof, catalog, policy, source-registry, geoprivacy, sensitivity, or public authority.

All accepted material must preserve release identity, prior release identity, target release identity, affected artifact identity, digest references, evidence/proof references, source-role state, sensitivity and geoprivacy state, policy state, review state, correction/withdrawal state, actor/runner identity, timestamp, and finite outcome where material.

Do **not** embed restricted location detail in rollback support. Use governed pointers, redacted identifiers, release IDs, digests, and public-safe artifact IDs.

---

## Exclusions

| Do not place here | Correct home | Why |
|---|---|---|
| RAW source captures, occurrence downloads, telemetry feeds, acoustic files, eDNA results, disease surveillance data, mortality reports, rasters, shapefiles, GeoParquet, PMTiles, media, source-native tables, logs, uploads, or source mirrors | `../../raw/fauna/`, `../../work/fauna/`, or `../../quarantine/fauna/` | Source-edge and unsafe material requires source metadata, checksums, rights, source-role, geoprivacy, and sensitivity controls. |
| WORK scratch, rollback experiments, transform intermediates, repair attempts, redaction/generalization trials, aggregation trials, taxonomy-reconciliation scratch, or unresolved joins | `../../work/fauna/` or `../../quarantine/fauna/` | Unresolved material belongs upstream or in hold lanes. |
| Normalized Fauna datasets | `../../processed/fauna/` | Processed data is not rollback support. |
| Catalog, STAC, DCAT, PROV, or graph/triplet records | `../../catalog/`, `../../triplets/` | Catalog and graph carriers have their own closure rules. |
| EvidenceBundle, ProofPack, CitationValidationReport, or integrity proof | `../../proofs/fauna/` or accepted proof lanes | Proof is the trust spine; rollback cites it. |
| General RunReceipt, TransformReceipt, RedactionReceipt, AggregationReceipt, ValidationReceipt, ReviewRecord, PolicyDecision, AIReceipt, or release-support receipt families | `../../receipts/fauna/` or accepted receipt/review lanes | General process memory belongs in receipt lanes; rollback-local receipts are narrow exceptions. |
| SourceDescriptor, source activation records, rights registry records, sensitivity registry records, source-family records, or access-control records | `../../registry/`, `policy/`, or accepted governance roots | Registry and control records belong in their own authority lanes. |
| Primary ReleaseManifest, RollbackCard, PromotionDecision, CorrectionNotice, WithdrawalNotice, signatures, or release changelog | `../../../release/` | Release decisions belong in release authority. |
| Published public artifacts | `../../published/fauna/`, `../../published/layers/fauna/`, or other released artifact lanes | Rollback support does not own public artifacts. |
| Public reports or steward-facing generated narratives | `../../published/reports/`, `../../../docs/reports/` | Report lanes have separate authority. |
| Contracts, schemas, policy rules, validators, tests, code, or workflows | `../../../contracts/`, `../../../schemas/`, `../../../policy/`, `../../../tools/`, `../../../tests/`, `.github/workflows/` | Separate authority roots. |
| Hard deletion instructions, erasure directives, species-location conclusions, hunting/fishing/legal advice, enforcement aids, operational wildlife guidance, emergency alerts, disease-control instructions, or life-safety directions | Separate governed authority or external authority | Rollback support is not legal, operational, enforcement, disease-control, or safety authority. |
| Exact sensitive occurrence coordinates, nest/den/roost/hibernacula/spawning-site coordinates, breeding/aggregation-site geometry, telemetry tracks, movement traces, site identifiers, access routes, private landowner details, steward-only notes, redaction offsets, generalization radii, fuzzing seeds, transform parameters, or reverse-engineerable derivatives | Restricted governed lanes only; public-safe derivative after policy/review/release | Rollback must not become a geoprivacy or sensitivity bypass. |

---

## Fauna rollback guardrails

| Risk | Guardrail |
|---|---|
| Deleting prior meaning | Rollback preserves prior release records, evidence, receipts, catalog records, review records, and lineage unless a separate governed erasure process applies. |
| Alias-only rollback | A current-pointer or alias change is insufficient unless tied to release-plane decision authority, digest verification, review state, and rollback-local receipt support. |
| Public artifact overwrite | Immutable release artifacts must not be overwritten in place. Reseat pointers or publish a governed correction/supersession. |
| Exact-location leak persists | Wrongfully exposed exact sensitive occurrence geometry, nests, dens, roosts, hibernacula, spawning sites, telemetry, or steward-controlled detail requires public-surface withdrawal, invalidation, correction, and cache/search/AI/graph/tile review; rollback alone cannot recall copied data. |
| Candidate/confirmed collapse | Candidate occurrences, public-occurrence derivatives, modeled ranges, seasonal ranges, migration routes, disease observations, mortality observations, invasive-species records, and AI summaries must not become confirmed occurrence truth during rollback. |
| Geoprivacy bypass | Missing or invalid RedactionReceipt, AggregationReceipt, ReviewRecord, PolicyDecision, or public-safe geometry support should force HOLD, DENY, correction, withdrawal, or rollback rather than public continuation. |
| Source-role collapse | Observation, modeled range, regulatory context, administrative status, expert-curated record, aggregate summary, telemetry trace, and public derivative remain separate claim types. |
| Telemetry and movement exposure | High-frequency telemetry, route traces, den/roost/nest movement patterns, migration stopover details, and other movement-derived clues fail closed unless public-safe generalization and review support exist. |
| Private landowner exposure | Private landowner, parcel, permission, stewardship, access-route, and property-sensitive joins fail closed even during emergency rollback. |
| Stale public surface | Map layers, API payloads, reports, indexes, tiles, stories, graph/triplet exports, Evidence Drawer payloads, Focus Mode answers, search surfaces, and AI answers must be invalidated or marked stale when rollback affects them. |
| Proof bypass | Rollback cannot repair a claim by hiding evidence gaps. EvidenceBundle/proof closure must still support the restored or superseding release. |
| Catalog bypass | Catalog, STAC, DCAT, PROV, and domain catalog state must be corrected or invalidated alongside published artifacts. |
| AI surface drift | Generated Fauna answers, Focus Mode surfaces, report summaries, story text, and Evidence Drawer prose must not keep citing withdrawn, stale, exact, or restricted release state. |
| Cross-lane leakage | Habitat, Flora, Hydrology, Hazards, Agriculture, Roads/Rail, Settlements/Infrastructure, Archaeology, People/Land, and Soil joins inherit the strictest owning-domain boundary during rollback. |
| File-move shortcut | Moving, renaming, or copying files under `data/published/` is not rollback unless release governance, receipts, proof, policy, review, and catalog closure support it. |

---

## Rollback flow

```mermaid
flowchart LR
    DETECT[Defect or sensitive exposure detected] --> CLASSIFY[Classify affected Fauna surfaces]
    CLASSIFY --> FREEZE[Freeze or mark affected public surfaces stale]
    FREEZE --> RELEASE[Locate ReleaseManifest and rollback target]
    RELEASE --> REVIEW[Verify sensitivity / geoprivacy / rights / source-role review state]
    REVIEW --> PROOF[Verify EvidenceBundle, proof, receipts, catalog]
    PROOF --> DECISION[Release-plane RollbackCard / CorrectionNotice / WithdrawalNotice]
    DECISION --> DATA[data/rollback/fauna receipt support]
    DATA --> INVALIDATE[Invalidate aliases, maps, tiles, reports, graph, search, AI surfaces]
    INVALIDATE --> RESTORE[Restore or publish governed public-safe target]
    RESTORE --> RECORD[Record correction path, rollback target, digests, status]

    classDef gate fill:#fff3cd,stroke:#8a6d3b,color:#202124;
    classDef hold fill:#f8d7da,stroke:#842029,color:#202124;
    class DECISION gate;
    class FREEZE hold;
```

> [!NOTE]
> This diagram is a responsibility map, not proof that rollback tooling, validators, alias resolvers, release manifests, rollback cards, geoprivacy review workflows, cache invalidation, or CI gates currently exist.

---

## Suggested directory shape

This shape follows the Directory Rules pattern `data/rollback/<domain>/<release_id>/` and remains **PROPOSED** until parent rollback governance or an accepted ADR confirms exact file names. Do not pre-create empty stubs.

```text
data/rollback/fauna/
├── README.md
├── <release_id>/
│   ├── alias_revert_receipt.json
│   ├── rollback.data_plane_receipt.json
│   ├── affected_artifacts.index.json
│   ├── digest_verification.json
│   ├── invalidation_refs.json
│   ├── release_refs.json
│   ├── evidence_refs.json
│   ├── review_refs.json
│   ├── geoprivacy_refs.json
│   ├── redaction_refs.json
│   ├── aggregation_refs.json
│   ├── policy_refs.json
│   ├── stale_state.json
│   └── README.md
├── drills/                              # PROPOSED: rollback drill outputs, clearly marked non-production
│   └── <drill_id>/
└── indexes/                             # PROPOSED: rollback-local indexes only
    └── fauna.rollback.index.json
```

Recommended minimal release-instance fields:

| Field | Purpose |
|---|---|
| `rollback_id` | Stable identifier for the data-plane rollback support record. |
| `release_id` | Defective, withdrawn, superseded, stale, or exposed release being addressed. |
| `target_release_id` | Prior or superseding release selected by release authority. |
| `rollback_card_ref` | Pointer to release-plane decision authority. |
| `release_manifest_ref` | Pointer to affected ReleaseManifest. |
| `review_refs` | Sensitive-species, geoprivacy, rights, source-role, and release-review references required for Fauna. |
| `affected_artifacts` | Published artifacts, aliases, catalog records, graph exports, reports, tiles, stories, API payloads, search surfaces, and AI surfaces affected. |
| `sensitive_exposure_class` | Public-safe classification of the defect, avoiding exact restricted details. |
| `geoprivacy_state` | Public-safe transform, redaction, generalization, aggregation, withholding, or denial posture. |
| `digest_verification` | Hash/digest checks for defective and target artifacts. |
| `policy_state` | Policy/review disposition for restored or superseding public surface. |
| `evidence_refs` | EvidenceBundle/proof references needed to inspect restored claims. |
| `invalidation_refs` | Downstream invalidation or stale-state records. |
| `outcome` | Finite outcome such as `RESTORED`, `WITHDRAWN`, `SUPERSEDED`, `HELD`, `DENIED`, `ABSTAIN`, or `ERROR`. |

---

## Required checks before use

- [ ] Confirm whether `data/rollback/README.md` should define a parent rollback contract, and update this README if parent rules change.
- [ ] Confirm exact rollback instance naming under `data/rollback/fauna/<release_id>/`.
- [ ] Confirm the release-plane `RollbackCard`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, and signatures exist where required.
- [ ] Confirm the rollback target resolves to a prior or superseding release with digest closure.
- [ ] Confirm EvidenceBundle, ProofPack, catalog, receipt, policy, rights, sensitivity, geoprivacy, source-role, review, and release support resolve for both the defective and target release where material.
- [ ] Confirm redaction/generalization/aggregation/suppression support for any public Fauna artifact that depends on sensitive taxa, exact occurrences, nests, dens, roosts, hibernacula, spawning sites, breeding/aggregation sites, telemetry, steward-controlled records, or private-landowner detail.
- [ ] Confirm stale or withdrawn Fauna map layers, occurrence tiles, range layers, API payloads, reports, PMTiles, story snapshots, graph/triplet projections, search indexes, Evidence Drawer payloads, Focus Mode answers, and AI-answer surfaces are invalidated or marked stale.
- [ ] Confirm rollback records do not embed exact sensitive geometry, restricted site IDs, telemetry traces, private-landowner detail, redaction offsets, generalization radii, fuzzing seeds, transform parameters, or reverse-engineerable derivative detail.
- [ ] Confirm candidate/confirmed, occurrence/range, telemetry/public derivative, model/observation, administrative/evidence, mortality/disease/invasive, and habitat/fauna boundaries are not collapsed in the restored state.
- [ ] Confirm rollback does not delete prior meanings, overwrite immutable release artifacts, bypass catalog/proof/policy/release/review checks, or expose restricted detail.
- [ ] Confirm public clients resolve restored state through governed API or released artifact aliases, not by reading this rollback lane.
- [ ] Confirm rollback-local receipt support is referenced by release/proof governance without becoming release authority itself.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target path presence | CONFIRMED | `data/rollback/fauna/README.md` existed as an empty file before this update. |
| Parent rollback README | CONFIRMED empty | `data/rollback/README.md` exists but is empty, so parent rollback contract remains NEEDS VERIFICATION. |
| Directory Rules rollback path | CONFIRMED doctrine | Directory Rules list `data/rollback/<domain>/<release_id>/` and warn rollback must not delete prior meanings. |
| Release root decision authority | CONFIRMED README | `release/README.md` says release decisions, manifests, promotion records, rollback cards, withdrawals, corrections, signatures, and changelog belong under `release/`. |
| Fauna domain doctrine | CONFIRMED README | `docs/domains/fauna/README.md` establishes Fauna scope, deny-by-default sensitive occurrence posture, object families, source-role boundaries, and lifecycle pattern. |
| Fauna lifecycle doctrine | CONFIRMED README | `docs/domains/fauna/DATA_LIFECYCLE.md` establishes RAW-to-PUBLISHED gates, no path-level move publication, public exact occurrence denial for sensitive taxa, and release rollback requirements. |
| Fauna published domain lane | CONFIRMED README | `data/published/fauna/README.md` requires release authority, EvidenceBundle support, catalog closure, validation, policy state, review state, correction path, and rollback target before public artifacts land there. |
| Fauna published layer lane | CONFIRMED README | `data/published/layers/fauna/README.md` requires release support, geoprivacy evidence, exact sensitive geometry denial, correction path, rollback support, and governed public interfaces. |
| Fauna processed lane | CONFIRMED README | `data/processed/fauna/README.md` is upstream and says public use requires governed catalog, evidence, sensitivity policy, rights posture, review state, release state, correction path, and rollback target. |
| Fauna catalog lane | CONFIRMED README | `data/catalog/domain/fauna/README.md` says catalog records are not release authority and require review/sensitivity/release references for public records. |
| Fauna receipts lane | CONFIRMED README | `data/receipts/fauna/README.md` defines receipt process memory and includes rollback-support context without making receipts proof or release authority. |
| Fauna proofs lane | CONFIRMED README | `data/proofs/fauna/README.md` defines proof support and excludes primary RollbackCard/ReleaseManifest ownership. |
| Fauna source registry | CONFIRMED README | `data/registry/sources/fauna/README.md` establishes source admission, source-role preservation, exact sensitive-site denial, no-public-path, and release-blocked posture. |
| Rollback runbook | CONFIRMED README | `docs/runbooks/ROLLBACK_RUNBOOK.md` describes rollback as a governed release transition and distinguishes decision artifacts from data-plane revert receipts. |
| Alias rollback ADR | CONFIRMED draft ADR | ADR-0015 proposes current-alias governance by RollbackCard and data-plane alias-revert receipts. |
| Deny-by-default ADR | CONFIRMED draft ADR | ADR-0010 states rare-species exact-location release is deny-by-default and requires evidence, review, receipts, catalog/proof closure, and rollback machinery for any allow path. |
| Actual rollback instances | UNKNOWN | This README does not prove any Fauna rollback instance exists. |
| Rollback tooling, validators, CI, signatures, alias resolver, cache invalidation | NEEDS VERIFICATION | No runtime enforcement was proven by this edit. |
| Public release readiness | DENY until proven | A rollback README cannot publish, restore, or expose Fauna claims by itself. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `data/rollback/fauna/README.md` existed as an empty file. | Did not define lane boundaries. |
| [`../README.md`](../README.md) | CONFIRMED empty | Parent rollback root exists. | Does not yet define parent rollback contract. |
| [`../../README.md`](../../README.md) | CONFIRMED | Data root includes lifecycle data families. | Does not prove rollback payloads or enforcement. |
| [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) | CONFIRMED doctrine | `data/rollback/<domain>/<release_id>/`; rollback must not delete prior meanings; promotion is governed state transition. | Exact rollback instance file names remain unresolved. |
| [`../../../release/README.md`](../../../release/README.md) | CONFIRMED README | Release decision artifacts belong under `release/`, distinct from `data/published/`. | Release root README is short and status `PROPOSED`; does not prove concrete release artifacts. |
| [`../../../docs/runbooks/ROLLBACK_RUNBOOK.md`](../../../docs/runbooks/ROLLBACK_RUNBOOK.md) | CONFIRMED draft runbook | Rollback governs PUBLISHED releases, rollback cards, correction notices, withdrawal of public surfaces, derivative invalidation, and data-plane revert receipts. | Runbook notes implementation is PROPOSED/NEEDS VERIFICATION in places. |
| [`../../../docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md`](../../../docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md) | CONFIRMED draft ADR | Proposed two-plane alias rollback mechanism: release-plane RollbackCard and data-plane alias-revert receipt. | ADR is draft/proposed and does not prove implementation. |
| [`../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md`](../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) | CONFIRMED draft ADR | Rare-species exact-location release defaults to deny and requires evidence, review, receipt, catalog/proof closure, and rollback support for any allow path. | ADR status and numbering conflicts remain noted in the ADR itself. |
| [`../../../docs/domains/fauna/README.md`](../../../docs/domains/fauna/README.md) | CONFIRMED doctrine / PROPOSED implementation | Fauna scope, sensitive occurrence T4 default, exact public sensitive occurrence denial, source-role boundaries, and lifecycle posture. | Implementation maturity remains NEEDS VERIFICATION in parts. |
| [`../../../docs/domains/fauna/DATA_LIFECYCLE.md`](../../../docs/domains/fauna/DATA_LIFECYCLE.md) | CONFIRMED doctrine / PROPOSED implementation | Fauna lifecycle, deny-by-default sensitive occurrence handling, governed release gates, correction/rollback requirements, and trust-membrane posture. | Does not prove runtime enforcement. |
| [`../../published/fauna/README.md`](../../published/fauna/README.md) | CONFIRMED README | Fauna published artifacts require release authority, EvidenceBundle support, catalog closure, validation, policy state, review state, correction path, and rollback target. | Does not prove released artifacts exist. |
| [`../../published/layers/fauna/README.md`](../../published/layers/fauna/README.md) | CONFIRMED README | Fauna published layers require release support, geoprivacy evidence, exact sensitive geometry denial, public-safe artifacts, and rollback support. | Does not prove layer payloads or release manifests exist. |
| [`../../processed/fauna/README.md`](../../processed/fauna/README.md) | CONFIRMED README | Processed Fauna is upstream of catalog/release and requires correction path and rollback target for public use. | Does not prove processed inventory. |
| [`../../catalog/domain/fauna/README.md`](../../catalog/domain/fauna/README.md) | CONFIRMED README | Fauna catalog lane requires evidence, source, sensitivity, transform, policy, release, and rollback references for public records. | Catalog records are not rollback decisions. |
| [`../../receipts/fauna/README.md`](../../receipts/fauna/README.md) | CONFIRMED README | Fauna receipts are process memory and include rollback-support context while excluding proof/release authority. | General receipts are not release/proof authority. |
| [`../../proofs/fauna/README.md`](../../proofs/fauna/README.md) | CONFIRMED README | Fauna proofs support evidence closure, geoprivacy proof posture, sensitive-species claim support, and exclude primary RollbackCard/ReleaseManifest ownership. | Proof lane does not publish or roll back by itself. |
| [`../../registry/sources/fauna/README.md`](../../registry/sources/fauna/README.md) | CONFIRMED README | Source registry establishes admission, rights, source role, exact sensitive-site denial, steward-controlled records posture, and no-public-path boundaries. | Source registry records do not authorize rollback or publication. |

[Back to top](#top)
