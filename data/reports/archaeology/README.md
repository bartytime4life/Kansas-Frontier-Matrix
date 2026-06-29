<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/reports/archaeology/readme
name: Archaeology Reports README
path: data/reports/archaeology/README.md
type: data-reports-archaeology-readme
version: v0.1.0
status: draft
owners:
  - <data-steward>
  - <reports-steward>
  - <archaeology-domain-steward>
  - <cultural-review-liaison>
  - <sovereignty-reviewer>
  - <rights-holder-representative>
  - <sensitivity-steward>
  - <evidence-steward>
  - <proof-steward>
  - <receipt-steward>
  - <catalog-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-29
updated: 2026-06-29
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
domain: archaeology
artifact_family: report-candidate-and-report-support-lane
path_posture: existing-greenfield-stub-replaced; parent-data-reports-readme-is-greenfield-stub; data-readme-lists-reports; directory-rules-data-tree-lists-data-published-reports-not-data-reports; compatibility-or-steward-facing-report-candidate-lane-until-parent-contract-or-adr-resolves
sensitivity_posture: no-public-path-by-default; archaeology-default-t4-deny; exact-site-geometry-denied; burial-human-remains-sacred-site-detail-fail-closed; sovereignty-care-and-rights-holder-review-aware; looting-risk-and-collection-security-detail-denied; private-landowner-detail-denied; candidate-feature-not-confirmed-site; report-is-downstream-carrier-not-truth; evidence-aware; rights-aware; policy-aware; review-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../raw/archaeology/README.md
  - ../../processed/archaeology/README.md
  - ../../catalog/domain/archaeology/README.md
  - ../../registry/sensitivity/archaeology/README.md
  - ../../registry/sources/archaeology/
  - ../../proofs/
  - ../../receipts/archaeology/
  - ../../published/README.md
  - ../../published/reports/README.md
  - ../../published/layers/archaeology/README.md
  - ../../../docs/reports/README.md
  - ../../../docs/domains/archaeology/DATA_LIFECYCLE.md
  - ../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../docs/domains/archaeology/PRESERVATION_MATRIX.md
  - ../../../docs/domains/archaeology/SOURCES.md
  - ../../../docs/domains/archaeology/SOURCE_REGISTRY.md
  - ../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../docs/domains/archaeology/MAP_UI_CONTRACTS.md
  - ../../../docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md
  - ../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../contracts/domains/archaeology/
  - ../../../schemas/contracts/v1/domains/archaeology/
  - ../../../schemas/contracts/v1/receipts/
  - ../../../policy/domains/archaeology/
  - ../../../policy/sensitivity/archaeology/
  - ../../../policy/geoprivacy/
  - ../../../policy/consent/archaeology/
  - ../../../policy/rights/
  - ../../../release/
tags:
  - kfm
  - data
  - reports
  - archaeology
  - cultural-heritage
  - report-candidate
  - report-support
  - downstream-carrier
  - sensitive-domain
  - deny-by-default
  - t4-deny
  - exact-location-denied
  - sacred-sites
  - burial-sites
  - human-remains
  - looting-risk
  - collection-security
  - cultural-review
  - sovereignty
  - CARE
  - rights-holder-review
  - redaction-receipt
  - publication-transform-receipt
  - evidence-first
  - cite-or-abstain
  - proof
  - receipts
  - catalog
  - release-gated
  - rollback
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/reports/archaeology/README.md`."
  - "The parent `data/reports/README.md` is currently a greenfield stub, so this file is self-bounding and intentionally conservative."
  - "Directory Rules v1.4 lists released report payloads under `data/published/reports/`; this existing `data/reports/archaeology/` lane is therefore treated as compatibility, report-candidate, or steward-facing report-support material until parent contract or ADR review resolves the lane."
  - "Archaeology reports are downstream carriers. They do not replace source records, processed data, catalog records, EvidenceBundles, proofs, receipts, policy decisions, cultural review records, rights-holder review, release manifests, correction records, rollback records, or generated-answer receipts."
  - "Exact site geometry, burial or human-remains detail, sacred-site detail, collection-security detail, looting-risk detail, private-landowner detail, and restricted cultural knowledge must not be embedded here."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Reports

Report-candidate and report-support lane for Archaeology-domain generated report material that is not yet a released public report payload.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data" src="https://img.shields.io/badge/root-data%2F-0a7ea4">
  <img alt="Lane: reports" src="https://img.shields.io/badge/lane-reports-blue">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-6e2a8a">
  <img alt="Default: T4 deny" src="https://img.shields.io/badge/default-T4%20DENY-critical">
  <img alt="Boundary: not root truth" src="https://img.shields.io/badge/boundary-not%20root%20truth-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Report boundary](#report-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Archaeology report guardrails](#archaeology-report-guardrails) · [Report flow](#report-flow) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/reports/archaeology/` is not Archaeology truth, not a public report lane, not proof, not receipt storage, not catalog closure, not release authority, not policy authority, not schema authority, not source registry authority, not sensitivity registry authority, and not a direct public API/UI source. Treat it as an existing report-candidate or report-support lane until `data/reports/` receives an accepted parent contract or migration decision.

---

## Scope

`data/reports/archaeology/` may hold Archaeology-domain report candidates, generated report-support bundles, report-local indexes, preview summaries, and report assembly sidecars that are derived from governed upstream artifacts but are **not** themselves canonical trust artifacts.

This lane is useful only when a maintainer needs a data-root place to stage, inspect, or assemble Archaeology report material before one of the following governed outcomes:

- a released public report payload under `data/published/reports/`;
- a generated steward-facing narrative under `docs/reports/`;
- a catalog/proof/release-linked report artifact referenced by a governed API or review console;
- a rejected, quarantined, corrected, superseded, withdrawn, or rolled-back report candidate.

Archaeology report material may summarize survey coverage, chronology, public-safe generalized site context, candidate features, remote-sensing anomalies, public-safe 3D context, evidence posture, review posture, redaction/generalization posture, proof posture, catalog posture, release posture, correction posture, and rollback posture.

A report candidate does **not** make an archaeological site, cultural association, survey finding, candidate feature, remote-sensing anomaly, artifact context, chronology assertion, sacred-place claim, burial/human-remains claim, public-safe geometry, or stewardship conclusion true. Consequential claims must remain supported by source descriptors, processed data, catalog records, EvidenceBundles, receipts, cultural/steward review, rights-holder review where applicable, policy decisions, release state, correction paths, and rollback targets.

---

## Path posture

The existing target lane is:

```text
data/reports/archaeology/
```

The parent currently exists as a greenfield stub:

```text
data/reports/README.md
```

Current placement evidence is mixed:

- `data/README.md` lists `reports` as content that may belong under `data/`.
- `docs/doctrine/directory-rules.md` lists canonical data lifecycle and emitted-proof families, including `data/published/reports/`, but does not establish `data/reports/` as a lifecycle phase in the same way as `raw`, `work`, `quarantine`, `processed`, `catalog`, `triplets`, `published`, `receipts`, `proofs`, `rollback`, and `registry`.
- `data/published/reports/README.md` is the clearer released public report payload lane.
- `docs/reports/README.md` is the clearer generated steward-facing narrative lane.

Therefore this README treats `data/reports/archaeology/` as **CONFIRMED path presence / NEEDS VERIFICATION topology**. Do not let this lane become a parallel report authority. If an ADR or parent README later makes `data/reports/` canonical, update this README and migrate child conventions with a rollback plan. If `data/reports/` is retired, migrate report candidates to the correct lifecycle, docs, or published lane.

---

## Repo fit

| Responsibility | Correct home | Boundary |
|---|---|---|
| Archaeology report candidates and report-support bundles | `data/reports/archaeology/` | Existing compatibility/steward-facing candidate lane until topology is resolved. |
| Parent reports lane | [`../README.md`](../README.md) | Currently greenfield; does not yet define a full report-family contract. |
| Data root | [`../../README.md`](../../README.md) | Lifecycle data and emitted proof root; reports listed but parent contract remains thin. |
| Processed Archaeology artifacts | [`../../processed/archaeology/README.md`](../../processed/archaeology/README.md) | Normalized Archaeology data upstream of catalog/report/public products. |
| Archaeology domain catalog | [`../../catalog/domain/archaeology/README.md`](../../catalog/domain/archaeology/README.md) | Catalog closure and release-linked discovery records; not report narrative. |
| Archaeology sensitivity registry | [`../../registry/sensitivity/archaeology/README.md`](../../registry/sensitivity/archaeology/README.md) | Sensitivity-control state and release-readiness pointers; not report payloads. |
| Archaeology receipts | `../../receipts/archaeology/` or accepted receipt lanes | Process memory; reports may summarize receipts but must not store or replace them. |
| Proof and EvidenceBundle authority | `../../proofs/` | Evidence support and citation validation; reports cite these, not replace them. |
| Released public report payloads | [`../../published/reports/README.md`](../../published/reports/README.md) | Release-approved report payloads only. |
| Released Archaeology map carriers | [`../../published/layers/archaeology/README.md`](../../published/layers/archaeology/README.md) | Published public-safe map layer carriers; reports may reference them after release. |
| Steward-facing generated narratives | [`../../../docs/reports/README.md`](../../../docs/reports/README.md) | Human-readable generated review/release reports; not data payloads. |
| Archaeology lifecycle doctrine | [`../../../docs/domains/archaeology/DATA_LIFECYCLE.md`](../../../docs/domains/archaeology/DATA_LIFECYCLE.md) | Phase obligations, receipts, sensitivity gates, review duties, and publication posture. |
| Archaeology publication doctrine | [`../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md`](../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md) | Trust membrane, deny-by-default publication posture, release/review/rollback discipline. |
| Deny-by-default ADR | [`../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md`](../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) | Cross-domain fail-closed policy posture; status and numbering conflicts remain noted in that ADR. |
| Release decisions | `../../../release/` | ReleaseManifest, PromotionDecision, correction, rollback, withdrawal, and signatures. |
| Contracts, schemas, policy | `../../../contracts/domains/archaeology/`, `../../../schemas/contracts/v1/domains/archaeology/`, `../../../policy/domains/archaeology/`, `../../../policy/sensitivity/archaeology/` | Meaning, machine shape, and allow/deny/restrict/abstain logic. |

---

## Report boundary

| Rule | Handling |
|---|---|
| Report is a downstream carrier | It can summarize governed artifacts, but it is never root truth. |
| Candidate is not publication | A file here is not public just because it is readable, renderable, or useful for review. |
| Archaeology reports default to restricted review | Treat report candidates as restricted-review until release evidence proves a safer posture. |
| Public report payloads move through release | Released report payloads belong under `data/published/reports/` with release support. |
| Steward narratives belong under docs | Generated human-readable review/release narratives belong under `docs/reports/`. |
| Proof remains separate | EvidenceBundle, ProofPack, citation validation, and integrity proof stay in proof lanes. |
| Receipts remain separate | RunReceipt, RedactionReceipt, PublicationTransformReceipt, validation, policy, AI, transform, and release-support receipts stay in receipt lanes. |
| Review remains separate | Cultural/steward review, sovereignty/CARE review, rights-holder review, and sensitivity review remain governed review artifacts or pointers, not report prose. |
| Catalog remains separate | Domain catalog, STAC, DCAT, and PROV records stay in `data/catalog/`. |
| Release remains separate | ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, WithdrawalNotice, and signatures stay in `release/`. |
| Policy remains separate | Redaction, generalization, geoprivacy, consent, rights, and sensitivity rules stay in `policy/`. |
| AI is not report truth | Generated language must resolve to evidence or abstain; AI summaries require AIReceipt/runtime-envelope support when used in governed flows. |
| Public clients do not read this lane | Public UI/API/report surfaces consume governed APIs, released artifacts, catalog/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted material is limited to Archaeology report-candidate and report-support files that do not become parallel trust artifacts:

- report-candidate Markdown, HTML, JSON, or PDF-generation source files that are explicitly unreleased and restricted-review;
- report-local indexes that point to processed, catalog, proof, receipt, sensitivity registry, release, and published artifacts without replacing them;
- report assembly sidecars, such as candidate table-of-contents, figure list, map snapshot index, citation draft index, evidence-reference draft index, caveat index, and review-dependency index;
- report-local caveat summaries, sensitivity summaries, redaction/generalization summaries, review summaries, and release-readiness summaries that link to their canonical policy/proof/receipt/review inputs;
- preview artifacts for steward review, clearly marked as candidates and not public release payloads;
- correction, supersession, withdrawal, or rollback notes that point to canonical release/proof records rather than replacing them;
- README files explaining local report-candidate boundaries.

All accepted material must avoid embedding restricted detail. Use pointers, stable IDs, redacted identifiers, release-safe summaries, and governed references instead of precise geometry or sensitive narrative detail.

---

## Exclusions

| Do not place here | Correct home | Why |
|---|---|---|
| RAW source captures, uploaded files, source mirrors, API dumps, archival extracts, field forms, site forms, oral-history transcripts, or raw report inputs | `../../raw/archaeology/` or restricted source lanes | Source-edge captures require source context, rights, sensitivity, and access controls. |
| WORK scratch, transform intermediates, unresolved report candidates, or unreviewed sensitive joins | `../../work/archaeology/` or `../../quarantine/archaeology/` | Candidate material that has not passed gates belongs upstream or in hold lanes. |
| Normalized Archaeology datasets | `../../processed/archaeology/` | Processed data is not a report. |
| Domain catalog, STAC, DCAT, PROV, or graph/triplet records | `../../catalog/`, `../../triplets/` | Catalog/graph carriers have their own closure rules. |
| EvidenceBundle, ProofPack, CitationValidationReport, or integrity bundles | `../../proofs/` | Proof is the trust spine; reports cite it. |
| RunReceipt, RedactionReceipt, PublicationTransformReceipt, ValidationReceipt, TransformReceipt, AIReceipt, ReviewRecord, or release-support receipts | `../../receipts/archaeology/` or accepted receipt/review lanes | Receipts and review records are process memory and governance state; reports summarize them only. |
| SourceDescriptor, source activation records, sensitivity registry records, or rights registry records | `../../registry/` | Registry/control records belong in registry lanes. |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, WithdrawalNotice, signatures, or release changelog | `../../../release/` | Release decisions are not report candidates. |
| Released public report payloads | `../../published/reports/` | Public report payloads must be release-approved. |
| Generated steward-facing narrative reports | `../../../docs/reports/` | Human-readable generated reports belong in docs. |
| Contracts, schemas, policy rules, validators, tests, code, or workflows | `../../../contracts/`, `../../../schemas/`, `../../../policy/`, `../../../tools/`, `../../../tests/`, `.github/workflows/` | Separate authority roots. |
| Exact site coordinates, precise site footprints, burial/human-remains location detail, sacred-site detail, restricted cultural knowledge, collection-security detail, looting-risk detail, or private-landowner detail | Restricted governed lanes only; public-safe derivative only after policy/review/release | Report formatting must not become a sensitivity bypass. |
| Map screenshots, figures, thumbnails, search snippets, embeddings, graph edges, or AI text that reverse-engineer sensitive locations | Restricted/held lanes only unless public-safe release support exists | Derived carriers can leak restricted detail even when raw coordinates are absent. |
| Uncited AI summaries or generated authoritative claims | Governed answer/report generation flow with evidence, policy, and receipts | Generated language is evidence-subordinate. |

---

## Archaeology report guardrails

| Risk | Guardrail |
|---|---|
| Exact-location disclosure | Coordinates, footprints, parcel-scale maps, high-resolution figures, screenshots, and captions must not reveal site locations unless explicit release support exists for a public-safe derivative. |
| Burial, human-remains, or sacred-site exposure | Default posture is DENY public disclosure; no report prose, figure, index, or citation should expose restricted detail. |
| Looting-risk amplification | Avoid details that make site discovery, collection, access, or exploitation easier, including indirect cues from maps, routes, imagery, names, or nearby landmarks. |
| Collection-security disclosure | Repository storage, collection movement, access control, or security-sensitive metadata must not be exposed in report candidates. |
| Restricted cultural knowledge | Sovereignty, CARE, consent, rights-holder, oral-history, and cultural-stewardship obligations travel into every report candidate and must not be flattened into prose. |
| Private-landowner exposure | Private landowner, parcel, access, or ownership-adjacent detail fails closed unless policy and review explicitly allow a public-safe representation. |
| Candidate-feature overclaim | CandidateFeature, RemoteSensingAnomaly, LiDARCandidate, geophysics, or 3D documentation must remain candidate/context class until evidence and review support a stronger claim. |
| Redaction-by-layout drift | Cropping, blur, zoom thresholds, figure styling, or vague captions are not substitutes for RedactionReceipt, policy decision, and release review. |
| Report-as-proof drift | A report may make evidence easier to read; it does not become the evidence. |
| Report-as-release drift | A report may summarize release state; it does not approve release. |

---

## Report flow

```mermaid
flowchart LR
    PROC[Processed Archaeology artifacts] --> CAT[Catalog / triplet closure]
    CAT --> PROOF[EvidenceBundle / proof support]
    PROOF --> REVIEW[Cultural / steward / rights-holder review]
    REVIEW --> RECEIPT[Receipts: validation, redaction, transform, AI, release-support]
    RECEIPT --> POLICY[Policy + sensitivity + rights decision]
    POLICY --> CAND[Report candidate in data/reports/archaeology]
    CAND --> DECISION{Report disposition}
    DECISION -- steward narrative --> DOCS[docs/reports]
    DECISION -- released public payload --> PUB[data/published/reports]
    DECISION -- hold or fail --> HOLD[work / quarantine / correction path]
    PUB --> REL[release manifest + correction + rollback]

    classDef gate fill:#fff3cd,stroke:#8a6d3b,color:#202124;
    classDef hold fill:#f8d7da,stroke:#842029,color:#202124;
    class DECISION gate;
    class HOLD hold;
```

> [!NOTE]
> The diagram is a responsibility map, not proof that generators, validators, payloads, manifests, review records, or CI wiring currently exist.

---

## Suggested directory shape

This shape is **PROPOSED** until `data/reports/` receives an accepted parent contract or migration decision. Do not pre-create empty stubs.

```text
data/reports/archaeology/
├── README.md
├── candidates/                         # PROPOSED: unreleased restricted-review report candidates
│   └── <report_slug>/
│       ├── report.candidate.md
│       ├── report.inputs.index.json
│       ├── evidence_refs.candidate.json
│       ├── review_refs.candidate.json
│       ├── sensitivity_refs.candidate.json
│       ├── citations.candidate.json
│       ├── caveats.candidate.md
│       └── README.md
├── previews/                           # PROPOSED: steward-only rendered previews
│   └── <report_slug>/
├── indexes/                            # PROPOSED: report-local candidate indexes
│   └── archaeology.report-candidates.index.json
├── superseded/                         # PROPOSED: retained candidates with lineage
│   └── README.md
└── withdrawn/                          # PROPOSED: withdrawn or denied report candidates
    └── README.md
```

If a candidate is promoted as a public report payload, the released payload belongs under `data/published/reports/` and the release decision belongs under `release/`. If a generator emits steward-facing narrative, the generated report belongs under `docs/reports/`.

---

## Required checks before use

- [ ] Confirm whether `data/reports/` is an accepted report-candidate lane, a compatibility lane, or a migration target.
- [ ] Confirm whether `data/reports/archaeology/` should hold candidates, indexes, previews, or should redirect to `docs/reports/` and `data/published/reports/`.
- [ ] Confirm CODEOWNERS for reports, Archaeology, cultural review, sovereignty/CARE review, rights-holder review, sensitivity, evidence, proof, receipts, catalog, policy, release, and docs review.
- [ ] Confirm every report claim resolves to catalog/proof/evidence or abstains.
- [ ] Confirm report candidates do not store canonical receipts, proofs, review records, release manifests, source descriptors, sensitivity registry records, policy rules, schemas, or processed datasets.
- [ ] Confirm exact site geometry, burial/human-remains detail, sacred-site detail, collection-security detail, looting-risk detail, private-landowner detail, restricted cultural knowledge, and reverse-engineerable derived cues are absent unless explicit public-safe release support exists.
- [ ] Confirm redaction/generalization, geoprivacy, audience tier, review, and public-safe representation posture for any public-facing Archaeology report.
- [ ] Confirm CandidateFeature, RemoteSensingAnomaly, LiDARCandidate, geophysics, and 3D material are not framed as confirmed sites without evidence and review support.
- [ ] Confirm source-role distinctions remain visible in the report narrative and metadata.
- [ ] Confirm AI-generated summaries have evidence references, citation validation, finite outcome, and AIReceipt/runtime envelope support where applicable.
- [ ] Confirm released report payloads are promoted to `data/published/reports/` only after ReleaseManifest, correction path, rollback target, digest, review state, and citation/evidence closure exist.
- [ ] Confirm generated steward-facing narratives belong in `docs/reports/` rather than this data lane.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target path presence | CONFIRMED | This README replaces a greenfield stub at `data/reports/archaeology/README.md`. |
| Parent reports README | CONFIRMED stub | `data/reports/README.md` exists but does not yet define a report-family contract. |
| Data root reports mention | CONFIRMED | `data/README.md` lists reports, but marks the root status `PROPOSED`. |
| Directory Rules data tree | CONFIRMED doctrine | Current Directory Rules list `data/published/reports/` and the canonical data lifecycle families; `data/reports/` remains topology-NEEDS VERIFICATION. |
| Published reports lane | CONFIRMED README | `data/published/reports/README.md` exists and is the clearer released report payload lane. |
| Docs reports lane | CONFIRMED README | `docs/reports/README.md` exists and is the clearer steward-facing generated narrative lane. |
| Archaeology processed lane | CONFIRMED README | `data/processed/archaeology/README.md` establishes PROCESSED-stage boundaries and fail-closed sensitivity posture. |
| Archaeology catalog lane | CONFIRMED README | `data/catalog/domain/archaeology/README.md` establishes catalog-stage boundaries and release-only exposure posture. |
| Archaeology sensitivity registry | CONFIRMED README | `data/registry/sensitivity/archaeology/README.md` establishes sensitivity-control and no-public-path posture. |
| Archaeology published layers | CONFIRMED README | `data/published/layers/archaeology/README.md` establishes release-gated public-safe layer-carrier posture. |
| Actual report payloads | UNKNOWN | This README does not prove report candidates or released reports exist. |
| Generator, validator, review, or CI enforcement | NEEDS VERIFICATION | No generator/validator/review tooling was proven by this edit. |
| Public release readiness | DENY until proven | Report existence here cannot publish Archaeology claims. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `data/reports/archaeology/README.md` existed as a greenfield stub. | Did not define lane boundaries. |
| [`../README.md`](../README.md) | CONFIRMED stub | Parent `data/reports/` path exists. | Does not yet define report-family authority or canonical topology. |
| [`../../README.md`](../../README.md) | CONFIRMED | `data/` root lists reports among data-root content. | Parent status remains `PROPOSED`; not enough to define report lifecycle semantics. |
| [`../../processed/archaeology/README.md`](../../processed/archaeology/README.md) | CONFIRMED | Processed Archaeology artifacts are upstream of catalog/reports/release and not public by default. | Does not prove report payloads or generators exist. |
| [`../../catalog/domain/archaeology/README.md`](../../catalog/domain/archaeology/README.md) | CONFIRMED | Archaeology catalog lane, review pointers, transform pointers, and sensitivity guardrails. | Catalog records are not report payloads. |
| [`../../registry/sensitivity/archaeology/README.md`](../../registry/sensitivity/archaeology/README.md) | CONFIRMED | Sensitivity-control boundaries, no-public-path posture, redaction/CARE/sovereignty obligations. | Registry records do not authorize publication or report release. |
| [`../../published/reports/README.md`](../../published/reports/README.md) | CONFIRMED | Released report payload lane under `data/published/`. | Does not create `data/reports/` authority. |
| [`../../published/layers/archaeology/README.md`](../../published/layers/archaeology/README.md) | CONFIRMED | Released public-safe Archaeology map-carrier boundary and release checks. | Layer README does not prove report payloads or public report release. |
| [`../../../docs/reports/README.md`](../../../docs/reports/README.md) | CONFIRMED | Generated steward-facing report narrative lane. | Docs reports are not public report payloads or trust artifacts. |
| [`../../../docs/domains/archaeology/DATA_LIFECYCLE.md`](../../../docs/domains/archaeology/DATA_LIFECYCLE.md) | CONFIRMED doctrine / PROPOSED implementation | Archaeology lifecycle, exact-location denial, sensitive-domain controls, review duties, and receipt posture. | Many implementation paths are explicitly PROPOSED/NEEDS VERIFICATION. |
| [`../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md`](../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md) | CONFIRMED doctrine / PROPOSED implementation | Trust membrane, deny-by-default publication posture, review/release/rollback discipline. | Does not prove runtime routes or actual releases. |
| [`../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md`](../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) | CONFIRMED draft ADR | Cross-domain fail-closed posture for archaeology and other high-risk classes. | ADR status and numbering conflicts remain noted in the ADR itself. |
| [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) | CONFIRMED doctrine | Responsibility-root, lifecycle, domain-segment, published-reports, and release-vs-published separation. | `data/reports/` topology still needs parent contract or ADR review. |

[Back to top](#top)
