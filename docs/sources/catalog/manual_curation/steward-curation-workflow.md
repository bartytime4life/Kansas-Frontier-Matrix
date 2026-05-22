<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-manual_curation-steward-curation-workflow
title: Manual Curation Workflow
type: product-page
version: v0.2
status: draft
owners: <PLACEHOLDER — Docs steward + Source steward for manual_curation>
created: 2026-05-20
updated: 2026-05-22
policy_label: public
related:
  - docs/sources/catalog/manual_curation.md
  - docs/sources/catalog/manual_curation/README.md
  - docs/sources/catalog/README.md
  - docs/sources/catalog/local_upload.md
  - docs/sources/catalog/local_upload/user-file-upload.md
  - docs/sources/catalog/loc/iiif-presentations.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/lifecycle-law.md
  - docs/governance/separation-of-duties.md
  - docs/registers/DRIFT_REGISTER.md
tags: [kfm, docs, sources, catalog, manual_curation, workflow, stewardship, governance]
notes:
  - "PROPOSED product-page scaffold operationalizing the parent methodology doc at ../manual_curation.md."
  - "STRUCTURAL TENSION (OPEN-MCW-01): manual_curation is a methodology, not a source family — modeling it as a sibling of local_upload/ and loc/ inside docs/sources/catalog/ NEEDS RECONCILIATION against Directory Rules and the parent standard doc. Surfaced, not smoothed over."
  - "v0.2: tailored template to workflow (not source-product) reality — most source-product fields are N/A and the page now says so; cross-links to parent methodology and sibling pages added; structural-tension flag surfaced."
[/KFM_META_BLOCK_V2] -->

# Manual Curation Workflow

> Operational walk-through of the **Steward Curation Workflow** — the named, step-by-step procedure a steward executes when applying the [`manual_curation.md`](../manual_curation.md) methodology to a single curation pass.

![status](https://img.shields.io/badge/status-draft-yellow)
![family](https://img.shields.io/badge/family-manual__curation-blue)
![doc--type](https://img.shields.io/badge/doc--type-product--page-lightgrey)
![authority](https://img.shields.io/badge/authority-workflow%20%C2%B7%20reference-lightgrey)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%E2%86%92%20PUBLISHED-informational)
![policy](https://img.shields.io/badge/posture-cite--or--abstain-success)
![truth](https://img.shields.io/badge/truth-receipt%E2%89%A0proof%E2%89%A0catalog%E2%89%A0publication-blueviolet)
![evidence](https://img.shields.io/badge/evidence-docs--only-orange)
![last--reviewed](https://img.shields.io/badge/last--reviewed-2026--05--22-lightgrey)

**Status:** `draft` — PROPOSED operational walk-through, structurally a product-page scaffold.
**Parent methodology:** [`../manual_curation.md`](../manual_curation.md) *(standard doc; outranks this page where they disagree).*
**Family slot:** [`manual_curation/`](./README.md) *(structural tension — see [Open questions](#open-questions) **OPEN-MCW-01**).*
**Owners:** _PLACEHOLDER — Docs steward + Source steward for `manual_curation`_
**Last reviewed:** 2026-05-22 · **Lifecycle phase:** documentation (this page does not own RAW/WORK/PROCESSED/CATALOG/PUBLISHED state).

---

## On this page

- [Overview](#overview)
- [What this page is (and is not)](#what-this-page-is-and-is-not)
- [Structural tension flag](#structural-tension-flag)
- [Workflow at a glance](#workflow-at-a-glance)
- [Source authority](#source-authority)
- [Catalog profiles used](#catalog-profiles-used)
- [Collection identity](#collection-identity)
- [Provenance fields](#provenance-fields)
- [Temporal handling](#temporal-handling)
- [Geometry, projection, and content typing](#geometry-projection-and-content-typing)
- [Rights and sensitivity](#rights-and-sensitivity)
- [Validation and catalog closure](#validation-and-catalog-closure)
- [Related contracts and schemas](#related-contracts-and-schemas)
- [Related connectors and pipelines](#related-connectors-and-pipelines)
- [Examples (illustrative)](#examples-illustrative)
- [Open questions](#open-questions)
- [Related docs](#related-docs)

---

## Overview

> [!IMPORTANT]
> This page is a **PROPOSED scaffold** that operationalizes the steward curation workflow described in the parent methodology doc [`../manual_curation.md`](../manual_curation.md). It does **not** describe a source family, a source endpoint, or an upstream publisher. It describes *what a steward does, in what order,* to walk one source through the curation gates.

CONFIRMED doctrine — manual curation is *"the steward-led path that walks a source from admission through review, validation, and catalog closure — never around the gates, always through them"* (parent methodology doc §1). This page concretizes that methodology into a **named, repeatable workflow** with explicit checkpoints. The methodology is *what* and *why*; the workflow is *how* and *in what order*.

Per parent §1, the workflow exists because:

1. **Source role cannot be inferred from convenience** — only a steward sets `source_role` at admission *(Atlas v1.1 §24.1.3; card **KFM-P1-PROG-0007**)*.
2. **Rights and sensitivity must be resolved before publication** — unknown rights fail closed *(Atlas v1.1 §24.9.2)*.
3. **Catalog closure is gated** — `CatalogRecord` is release-eligible only after STAC · DCAT · PROV closure plus evidence, policy, and review records exist *(Pass-10 **C4-01**, **C4-04**, **C4-05**; cards **KFM-P26-PROG-0025**, **KFM-P27-FEAT-0004**)*.
4. **AI and watchers are advisory** — they may suggest, score, or fetch; they may not approve. `EvidenceBundle` outranks generated text *(Atlas v1.1 §24.9.2)*.

[Back to top](#manual-curation-workflow)

---

## What this page is (and is not)

| This page **IS** | This page **IS NOT** |
|---|---|
| An operational walk-through of one curation pass: ordered steps, per-step checkpoints, per-step artifacts. | A source family. There is no upstream `manual_curation` publisher; the workflow is applied *to* sources, not *as* one. |
| A complement to the parent methodology doc [`../manual_curation.md`](../manual_curation.md). | A replacement for it. The parent owns scope, purpose, roles, separation-of-duties matrix, anti-patterns, and the catalog-closure checklist. |
| A page that uses the product-page template **structurally** because it lives inside `docs/sources/catalog/`. | A claim that "manual curation" is doctrinally equivalent to a source product like LOC IIIF Presentations or `local_upload` user-file-upload. See [Structural tension flag](#structural-tension-flag). |
| A pointer surface into the same canonical homes (`SourceDescriptor`, `EvidenceBundle`, `CatalogRecord`, …) that any curation pass touches. | A schema, contract, policy bundle, validator, or catalog record. |

For the full methodology — scope, accepted inputs, exclusions, gate failures, reason codes, sensitive-lane curation, anti-patterns — read the parent doc.

[Back to top](#manual-curation-workflow)

---

## Structural tension flag

> [!WARNING]
> **OPEN-MCW-01 — Subfolder divergence.** The parent methodology doc lives at `docs/sources/catalog/manual_curation.md`, **next to** the source-family docs `local_upload.md` and the source-family directories `local_upload/` and `loc/`. This page sits at `docs/sources/catalog/manual_curation/steward-curation-workflow.md` — as if `manual_curation` were a source family with product pages inside it. **That is a structural inconsistency, not a settled convention.**
>
> Manual curation is a **methodology / workflow**, not a **source family**. Versioned publishers (LOC, USGS, FEMA…) and user-uploaded files (`local_upload`) emit candidate material; manual curation is what stewards *do to* that material. Treating it as a sibling family conflates two different categories. The directory pattern decision should be made before the catalog scales further.
>
> **Possible resolutions** (NEEDS RECONCILIATION via `docs/registers/DRIFT_REGISTER.md` and/or an ADR):
>
> 1. Move this page's content into a new section of [`../manual_curation.md`](../manual_curation.md) and retire the `manual_curation/` subdirectory.
> 2. Keep `manual_curation/` as a **process-docs subdirectory** (not a source-family subdirectory) and rename to reflect that (e.g., `docs/sources/catalog/_workflows/manual_curation/`).
> 3. Keep the current layout and document explicitly that `docs/sources/catalog/<x>/` may hold *either* source-family product pages *or* workflow / methodology pages, with each subdirectory README declaring which.
>
> No decision is made here. This page proceeds under option (3) provisionally, with the tension flagged.

[Back to top](#manual-curation-workflow)

---

## Workflow at a glance

The diagram below is the steward path from admission through release-eligibility, the same shape as the parent methodology §7 flow. Each transition is a gate; the gate emits a record; missing records fail closed.

```mermaid
sequenceDiagram
    autonumber
    participant SRC as Candidate Source
    participant S1 as Source steward
    participant S2 as Domain steward
    participant SR as Sensitivity reviewer
    participant RH as Rights-holder rep
    participant POL as Policy gate
    participant REV as Reviewer (≠ author)
    participant CAT as Catalog
    participant REL as Release authority

    SRC->>S1: New / updated / quarantined material
    S1->>S1: Author SourceDescriptor (role · rights · sensitivity · cadence · steward)
    alt rights / sensitivity unresolved
        S1->>SR: Escalate to QUARANTINE review queue
        opt rights-holder consultation required
            SR->>RH: Consult (archaeology · DNA · sovereign · living-person)
        end
    end
    S1->>S1: Issue SourceActivationDecision (allow / restrict / deny / needs-review)
    S1->>S2: Hand off to domain stewardship (RAW capture, normalize, validate)
    S2->>S2: Compose EvidenceBundle (every EvidenceRef must resolve)
    S2->>POL: Submit for policy gate
    POL-->>S2: PolicyDecision (allow · restrict · deny · abstain · error)
    alt allow / restrict
        S2->>CAT: Close CatalogRecord (STAC · DCAT · PROV closure)
        CAT->>REV: ReviewRecord required (separation of duties where applicable)
        REV-->>CAT: approve / reject (≠ author when materiality applies)
        CAT->>REL: Release candidate (out of scope here)
    else deny / abstain
        POL->>SR: Return to QUARANTINE; remediate; resubmit
    end
```

**CONFIRMED doctrine** — every transition is a governed state change, never a file move (parent §7; Atlas §24.9.1). **PROPOSED** — exact validator names, route names, and CI surfaces remain unverified.

[Back to top](#manual-curation-workflow)

---

## Source authority

This workflow does **not** own a `SourceDescriptor`. It produces and consumes descriptors *for the source being curated*. Every curation pass writes (or reads) a descriptor at [`data/registry/sources/`](../../../../data/registry/sources/), schema-shaped by `schemas/contracts/v1/source/` per Directory Rules §7.4 and ADR-0001.

> [!WARNING]
> **Do not duplicate descriptor fields on this page.** The descriptor for any given curation pass belongs to the source being curated — see e.g. [`../local_upload.md`](../local_upload.md) §5 for the `local_upload` family defaults or [`../loc/iiif-presentations.md`](../loc/iiif-presentations.md) for the LOC IIIF Presentations product defaults.

| Surface this workflow touches | PROPOSED home | Read or write? |
|---|---|---|
| `SourceDescriptor` record | `data/registry/sources/` | Writes on admission; reads on every subsequent step. |
| `SourceActivationDecision` | `data/registry/sources/<source_id>/activations/` (PROPOSED) | Writes at activation. |
| `SourceIntakeRecord` envelope *(card **KFM-P4-PROG-0001**)* | `data/registry/intake/` (PROPOSED) | Writes when a watcher routed a candidate here. |
| `RawCaptureReceipt`, `TransformReceipt`, `ValidationReport`, `EvidenceBundle`, `PolicyDecision`, `CatalogRecord`, `ReviewRecord` | per parent §8 *Stages and required artifacts* | Writes at each gate. |
| `policy/sources/<family>/`, `policy/sensitivity/` | per Directory Rules §6.5 (canonical singular `policy/`) | Reads at every gate. |

[Back to top](#manual-curation-workflow)

---

## Catalog profiles used

> [!NOTE]
> **The workflow does not emit its own STAC / DCAT / PROV profile.** It composes records *in the profile of the source being curated*. The table below clarifies which profiles a curation pass *invokes*, not which a workflow *owns*.

| Profile | Lane | Used by this workflow? |
|---|---|---|
| **STAC** (with `kfm:provenance`) | `data/catalog/stac/` | **N/A as a workflow profile.** Invoked when the curated source emits spatiotemporal STAC Items (per Pass-10 **C4-01**). |
| **DCAT** (Dataset / Distribution) | `data/catalog/dcat/` | **N/A as a workflow profile.** Invoked when the curated source emits non-spatial DCAT entries (per Pass-10 **C4-05**). |
| **PROV-O** | `data/catalog/prov/` | **Always invoked** — every emitted record carries a PROV chain back to admission, descriptors, receipts, and reviews. |
| **Domain projection** | `data/catalog/domain/<domain>/` | Invoked when the curated source binds to a recognized domain. |

[Back to top](#manual-curation-workflow)

---

## Collection identity

> [!NOTE]
> **Manual curation does not own a STAC Collection.** Collection identity belongs to the *source being curated*, not to the workflow. A `local_upload` candidate may end up in `kfm-local-upload-candidates` (or no Collection at all — see product-page **OPEN-LU-UFU-02**); a LOC IIIF Presentations record may end up in `kfm-loc-iiif-presentations`. The workflow contributes the gates that get a record *into* the appropriate Collection; it does not name one.

- **Workflow run identifier (PROPOSED):** each curation pass has a `curation_run_id` recorded on the receipts it emits (e.g., on `RawCaptureReceipt`, `TransformReceipt`, `ValidationReport`, `ReviewRecord`). Format NEEDS VERIFICATION.
- **Namespace:** the `kfm:` vs `ks-kfm:` Collection-level question (Pass-10 **C4-01**) is **upstream of this page**; it is **OPEN-DSC-03** and is decided once for KFM, not per curation pass.

[Back to top](#manual-curation-workflow)

---

## Provenance fields

When the workflow closes a `CatalogRecord` that carries a STAC Item, the Item carries the standard `item.properties.kfm:provenance` block defined in Pass-10 **C4-01**. The workflow's contribution to that block is the *run-and-review chain*, not the data itself.

| Field | Type / resolves to | Workflow contribution |
|---|---|---|
| `spec_hash` | `sha256:…` | Computed once the canonical record is composed; the workflow ensures this is recorded, not invented. |
| `evidence_bundle_ref` | `kfm://evidence/<digest>` → `EvidenceBundle` | The workflow composes the bundle and verifies every `EvidenceRef` resolves. |
| `run_record_ref` | `kfm://run/<run-id>` → `RunRecord` | The workflow's `curation_run_id` and any pipeline run IDs invoked. |
| `audit_ref` | `kfm://audit/<attestation-id>` → attestation | SLSA / cosign / OPA decision attestation produced at the policy gate. |
| `policy_digest` | `sha256:…` | Hash of the policy bundle that produced the `PolicyDecision`. |

Per-asset integrity (`file:checksum`) is recorded by the connector / pipeline, not by the workflow page.

[Back to top](#manual-curation-workflow)

---

## Temporal handling

The workflow tracks **its own timestamps** distinct from the source's. Both must travel together on the resulting receipts. *(CONFIRMED doctrine — Atlas v1.1: distinct source / observed / valid / retrieval / release / correction times where material.)*

| Time | Owned by | Notes |
|---|---|---|
| `source_time`, `observed_time`, `valid_time` | The curated source | Read from the source descriptor / record; never invented by the workflow. |
| `retrieval_time` | The connector under the workflow | Set when the connector fetches RAW. |
| `admission_time` | The workflow | When the source steward authored the `SourceDescriptor`. |
| `activation_time` | The workflow | When the `SourceActivationDecision` was issued. |
| `review_time` | The workflow | When the `ReviewRecord` was signed. |
| `closure_time` | The workflow | When the `CatalogRecord` was sealed as release-eligible. |
| `release_time`, `correction_time` | Release authority (out of scope) | Set later, in `release/`. |

[Back to top](#manual-curation-workflow)

---

## Geometry, projection, and content typing

The workflow **does not produce geometry**. It preserves whatever geometry, CRS, and datum the curated source carries, and it enforces the gates that prevent silent reprojection or generalization.

| Workflow obligation | What it enforces |
|---|---|
| CRS / datum preservation | The source's CRS / datum travels on every receipt; silent reprojection fails the geometry validator. |
| Generalization receipts | When a sensitivity transform generalizes geometry, the workflow emits a `RedactionReceipt` linking the original and the generalized form. |
| Scale / generalization tier | Per the T0–T4 sensitivity tier scheme (Atlas §24.5; ADR-S-05 open). |
| Renderer-boundary check | The workflow does not emit map tiles; it ensures the curated record can be safely consumed by `pipelines/catalog/` and downstream rendering without trust-membrane bypass. |

[Back to top](#manual-curation-workflow)

---

## Rights and sensitivity

> [!CAUTION]
> **Do not restate policy on this page.** Rights and sensitivity decisions live in [`policy/sensitivity/`](../../../../policy/sensitivity/) and `policy/sources/<family>/`. The full deny-by-default register is in the parent methodology doc [`../manual_curation.md`](../manual_curation.md) §11 *Sensitive-lane curation*. If this page and the policy bundle disagree, **the policy bundle wins**.

What the workflow specifically enforces around rights and sensitivity:

- Author of a sensitive-lane catalog closure **MUST NOT** also be the reviewer (parent §9.2 *Separation-of-duties matrix*).
- A `SourceDescriptor` with `rights_status = unknown` **MUST** route to `needs-review` activation, never `allow`.
- A `SourceDescriptor` in a deny-by-default class (living persons, DNA, rare-species exact locations, archaeology, sacred places, critical infrastructure, private-landowner) **MUST** add a sensitivity reviewer and, where applicable, a rights-holder representative *before* catalog closure.
- AI assistance touching a curation step **MUST** be reviewed by the AI surface steward; AI text is **never** evidence (Atlas §24.9.2).

[Back to top](#manual-curation-workflow)

---

## Validation and catalog closure

This is the **operational checklist version** of the parent doc §12 *Catalog-closure checklist*. Use the parent for the canonical wording; the version here is operational, ordered, and tied to the workflow steps in [Workflow at a glance](#workflow-at-a-glance).

Before a `CatalogRecord` is treated as release-eligible:

- [ ] **Admission step closed** — `SourceDescriptor` present with `source_role`, rights status, sensitivity, cadence, steward, and access method set (not blank, not `"unknown"`).
- [ ] **Activation step closed** — `SourceActivationDecision` exists and is `allow` or `restrict`.
- [ ] **RAW capture closed** — `RawCaptureReceipt` resolves to retrieval metadata and a checksum; no public RAW path.
- [ ] **Normalization closed** — `TransformReceipt` records normalization steps and any information loss.
- [ ] **Validation closed** — `ValidationReport` outcome is `ANSWER` across schema, geometry, temporal, rights, sensitivity, and evidence checks.
- [ ] **Evidence closed** — `EvidenceBundle` composed; every `EvidenceRef` on the candidate resolves.
- [ ] **Policy gate closed** — `PolicyDecision` recorded as `allow` or `restrict` (not `deny`, not `abstain`).
- [ ] **Catalog closure** — `CatalogRecord` carries source, schema, validation, policy, review, and release metadata; STAC · DCAT · PROV closure complete *(per Pass-10 C4-01 / C4-04 / C4-05)*.
- [ ] **Review closed** — `ReviewRecord` exists, naming a reviewer distinct from the author where separation of duties or sensitivity applies.
- [ ] **STAC Projection lint** *(card **KFM-P27-FEAT-0003**)* — passes for any emitted spatial Items.
- [ ] **STAC checksum closure** *(card **KFM-P22-PROG-0037**)* — passes against the `ReleaseManifest` digest *(invoked when the workflow hands off to the release authority)*.
- [ ] **Catalog QA CI surface** *(card **KFM-P27-FEAT-0004**)* — clear of missing-license, broken-link, missing-`stac_extensions`, JSON-error, and fail-outcome entries.
- [ ] **Correction path & rollback target nominated** — before the record is offered to a release authority.

[Back to top](#manual-curation-workflow)

---

## Related contracts and schemas

| Surface | PROPOSED path | Status |
|---|---|---|
| Contracts (semantic) | `contracts/` | NEEDS VERIFICATION |
| SourceDescriptor schema | `schemas/contracts/v1/source/source_descriptor.schema.json` | PROPOSED per ADR-0001 |
| SourceActivationDecision schema | `schemas/contracts/v1/source/source-activation-decision.schema.json` | PROPOSED |
| EvidenceBundle schema | `schemas/contracts/v1/evidence/evidence-bundle.schema.json` | PROPOSED (Pass-10 **C4-04**) |
| ReviewRecord schema | `schemas/contracts/v1/review/review-record.schema.json` | PROPOSED |
| Catalog record schema | `schemas/contracts/v1/catalog/catalog-record.schema.json` | PROPOSED |
| Pre-RAW event family schema | `schemas/contracts/v1/intake/event_envelope.schema.json` | PROPOSED *(card **KFM-P1-PROG-0008**)* |
| STAC profile contract | per card **KFM-P31-PROG-0004** | PROPOSED |

[Back to top](#manual-curation-workflow)

---

## Related connectors and pipelines

> [!IMPORTANT]
> **There is no `connectors/manual_curation/` connector.** Manual curation is **not** a connector — connectors emit RAW from external sources; manual curation orchestrates the workflow over those connectors' output. The path `connectors/manual_curation/` should **not** be created; doing so would violate Directory Rules §7.3 (connectors are source-specific fetchers) and Atlas §24.9.1 (do not invent parallel authority homes).

The workflow **invokes** the following surfaces (each PROPOSED beyond the doctrinal naming):

| Surface | PROPOSED path | Role in the workflow |
|---|---|---|
| Connectors invoked | [`connectors/<family>/`](../../../../connectors/) (e.g. `connectors/local_upload/` CONFIRMED slot, plus versioned-publisher connectors) | Produce RAW under the workflow's `SourceActivationDecision`. |
| Ingest pipeline | `pipelines/ingest/` | Captures the RAW payload and emits the ingest receipt. |
| Normalize pipeline | `pipelines/normalize/` | Schema / geometry / temporal normalization. |
| Validate pipeline | `pipelines/validate/` | STAC / DCAT / PROV conformance + rights + sensitivity checks. |
| Catalog pipeline | `pipelines/catalog/` | Emits `data/catalog/{stac,dcat,prov,domain}/` records. |
| Domain spec | `pipeline_specs/<domain>/` | Declarative spec when the curated source binds to a domain. |
| Validators | `tools/validators/source_descriptor/`, `tools/validators/connector_gate/`, `tools/validators/evidence_bundle/`, `tools/validators/promotion_gate/` | Deterministic gates invoked by the workflow. |

[Back to top](#manual-curation-workflow)

---

## Examples (illustrative)

> [!NOTE]
> The two worked walk-throughs for this workflow live in the parent methodology doc, not here. Use them as the operational reference for what a curation pass actually looks like.

- **Hydrology dataset (versioned publisher) walk-through** — [`../manual_curation.md` §13](../manual_curation.md#13-worked-example) — admission of a county-level streamflow dataset with `source_role = observation`, `rights = public`, sensitivity = `public`. Nine ordered steps from admission to review.
- **User-uploaded file (`local_upload`) contrast walk-through** — [`../manual_curation.md` §13](../manual_curation.md#13-worked-example) — same gates, different defaults (`source_role = candidate`, `rights = unknown`, sensitivity = `restricted`).

If a minimal STAC Item example with the `kfm:provenance` block is needed, see the family-level example referenced at [`../_examples/stac-item-example.json`](../_examples/stac-item-example.json) *(NEEDS VERIFICATION — path PROPOSED)*.

[Back to top](#manual-curation-workflow)

---

## Open questions

<details>
<summary><strong>Verification backlog (click to expand)</strong></summary>

PROPOSED — Each item below blocks promotion of this page to `status: review`.

- **OPEN-MCW-01** — **Structural tension.** Is `docs/sources/catalog/manual_curation/` a doctrinally appropriate home for this page, given that `manual_curation` is a methodology rather than a source family? See [Structural tension flag](#structural-tension-flag) for the three possible resolutions. Resolution requires `docs/registers/DRIFT_REGISTER.md` entry and likely an ADR. NEEDS RECONCILIATION.
- **OPEN-MCW-02** — **Subdirectory authority (inherited).** Same question shared with sibling product pages **OPEN-LU-UFU-01** and the LOC product page: is `docs/sources/catalog/<x>/<y>.md` a confirmed convention, or should this page live flat at `docs/sources/catalog/manual_curation-steward-curation-workflow.md`? NEEDS VERIFICATION.
- **OPEN-MCW-03** — **`curation_run_id` format.** Does this run ID exist as a recognized field on KFM receipts, or is it absorbed into `run_record_ref`? NEEDS VERIFICATION.
- **OPEN-MCW-04** — **Workflow timestamps.** The `admission_time` / `activation_time` / `review_time` / `closure_time` quadruple is PROPOSED. Where are these recorded — on each individual receipt, on the EvidenceBundle, on the CatalogRecord, or somewhere else? NEEDS VERIFICATION.
- **OPEN-MCW-05** — **AI surface scoping.** Atlas card ADR-S-06 (AI surface boundary) is on the open ADR backlog. What is the workflow's expected interaction with AI assistance — score-only? abstain-only? steward-only? OPEN.
- **OPEN-MCW-06** — **Separation-of-duties enforcement.** Atlas card ADR-S-09 (reviewer-role separation). Does this page assume tooling-enforced separation (it should, eventually) or custom enforcement (it does, in early-stage maturity)? Resolve consistently with the parent §9.2. OPEN.
- **OPEN-DSC-03** *(atlas-level, inherited)* — Resolve `kfm:` vs `ks-kfm:` namespace pinning at the Collection level (Pass-10 **C4-01** open question).

</details>

[Back to top](#manual-curation-workflow)

---

## Related docs

- [`../manual_curation.md`](../manual_curation.md) — **parent methodology doc** (standard). The canonical source of curation doctrine, roles, separation-of-duties matrix, gate-failure reason codes, sensitive-lane register, anti-patterns, and the catalog-closure checklist. This workflow page is operational; the parent is doctrinal.
- [`./README.md`](./README.md) — `manual_curation/` subdirectory landing page (PROPOSED; pending **OPEN-MCW-01**).
- [`../README.md`](../README.md) — catalog lane orientation.
- [`../local_upload.md`](../local_upload.md) — `local_upload` family governance doc — sibling family example.
- [`../local_upload/user-file-upload.md`](../local_upload/user-file-upload.md) — `local_upload` product page — sibling product example (candidate-role default).
- [`../loc/iiif-presentations.md`](../loc/iiif-presentations.md) — LOC IIIF Presentations product page — sibling product example (versioned publisher).
- [`../../../doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) — §6.5 (singular `policy/`), §7.3 (`connectors/`), §7.4 (schema home), §9 (`data/` and `release/`).
- [`../../../doctrine/trust-membrane.md`](../../../doctrine/trust-membrane.md) — *PROPOSED* — public-client boundary.
- [`../../../doctrine/lifecycle-law.md`](../../../doctrine/lifecycle-law.md) — *PROPOSED* — RAW → PUBLISHED governance.
- [`../../../governance/separation-of-duties.md`](../../../governance/separation-of-duties.md) — *PROPOSED* — full separation-of-duties matrix.
- [`../../../registers/DRIFT_REGISTER.md`](../../../registers/DRIFT_REGISTER.md) — *PROPOSED* — where **OPEN-MCW-01** and **OPEN-MCW-02** should be logged.

---

<sub>**Last reviewed:** 2026-05-22 · **Doc version:** v0.2 (draft) · **Evidence basis:** docs-only (no mounted repo this session) · [Back to top](#manual-curation-workflow)</sub>
