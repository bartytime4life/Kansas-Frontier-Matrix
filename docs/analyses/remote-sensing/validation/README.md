<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<NEEDS-UUID>
title: Remote Sensing Validation & Quality Assurance
type: standard
version: v1
status: draft
owners: <NEEDS VERIFICATION>
created: <NEEDS VERIFICATION>
updated: <NEEDS VERIFICATION>
policy_label: <NEEDS VERIFICATION>
related: [docs/analyses/remote-sensing/README.md (NEEDS VERIFICATION), docs/analyses/remote-sensing/validation/results/README.md (PROPOSED), docs/analyses/remote-sensing/validation/governance.md (PROPOSED)]
tags: [kfm, remote-sensing, validation, qa]
notes: [Current-session workspace evidence was PDF-only; target path is task-specified, not repo-verified; a remote-sensing/time-series namespace appears in attached ideation material, but adjacent repo files, owners, dates, and automation entrypoints still need verification.]
[/KFM_META_BLOCK_V2] -->

# Remote Sensing Validation & Quality Assurance

Govern release-bearing remote-sensing outputs with explicit metrics, provenance, uncertainty, and publication-safe review.

> **Status:** experimental  
> **Owners:** `NEEDS VERIFICATION`  
> ![Status](https://img.shields.io/badge/status-experimental-orange)
> ![KFM](https://img.shields.io/badge/KFM-evidence--first%20%7C%20map--first-1f6feb)
> ![Remote sensing](https://img.shields.io/badge/domain-remote--sensing-0a7f5a)
> ![Repo fit](https://img.shields.io/badge/repo%20fit-needs%20verification-lightgrey)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Quickstart](#quickstart) · [Workflow](#workflow) · [Validation minimums](#validation-minimums) · [Artifacts](#artifacts--traceability) · [Definition of done](#definition-of-done) · [FAQ](#faq)

> [!IMPORTANT]
> Current-session workspace evidence for adjacent repo files was **PDF-only**. This README keeps KFM doctrine **CONFIRMED** where the attached corpus is explicit, and marks directory layout, filenames, automation commands, and neighboring docs as **PROPOSED** or **NEEDS VERIFICATION** until the mounted repository is inspected.

> [!NOTE]
> Remote sensing is treated here as **measurement**, not decorative backdrop. For this document, **support** means the unit or grain at which a value is legitimately meaningful: pixel, scene, polygon, transect, county rollup, or time window.

## Scope

This directory is for **remote-sensing validation and quality assurance** inside KFM’s governed truth path.

It exists to make the following things inspectable before publication or downstream use:

- what was validated
- how it was validated
- which checks passed, failed, or remained partial
- what uncertainty remains
- whether the output is fit for its intended support, scale, audience, and release surface

### CONFIRMED doctrine carried into this directory

- Validation is cross-cutting in KFM and attaches to intake, canonical truth, catalog/policy/review, derived delivery, and runtime trust surfaces.
- Promotion is a governed state change, not a cosmetic file move.
- Correction must preserve lineage through supersession, generalization, withdrawal, narrowing, or replacement.
- Remote-sensing or model-assisted outputs remain subordinate to evidence, policy, release state, and correction discipline.

### What this README does

- defines what belongs in this directory
- stabilizes a **PROPOSED** minimum validation bundle for remote-sensing work
- gives maintainers a readable review checklist for release readiness
- creates a home for both automated and steward-reviewed validation workflows

[↑ Back to top](#remote-sensing-validation--quality-assurance)

## Repo fit

| Item | Value |
|---|---|
| Target path | `docs/analyses/remote-sensing/validation/README.md` *(task-specified; repo presence needs verification)* |
| Role in repo | Directory README for validation methods, result indexes, release checks, and governance notes |
| Likely upstream | [`../README.md`](../README.md) *(NEEDS VERIFICATION)* |
| Likely downstream | [`methods/README.md`](methods/README.md), [`results/README.md`](results/README.md), [`governance.md`](governance.md) *(PROPOSED / NEEDS VERIFICATION)* |
| Indirect sibling signal | [`../time-series/README.md`](../time-series/README.md) *(INDIRECT from attached ideation material; not mounted-repo proof)* |
| Primary audience | Remote-sensing engineering, science QA reviewers, release managers, governance reviewers |
| Contract families most relevant here | `ValidationReport`, `DatasetVersion`, `DecisionEnvelope`, `ReviewRecord`, `CatalogClosure`, `ReleaseManifest` / `ReleaseProofPack`, `ProjectionBuildReceipt`, `EvidenceBundle`, `CorrectionNotice` |

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Explicitly supported by the attached corpus in the current session |
| **INFERRED** | Strongly implied by the corpus, but not stated as mounted implementation fact |
| **PROPOSED** | A doctrine-consistent starter pattern or recommended implementation shape |
| **UNKNOWN** | No reliable current-session evidence |
| **NEEDS VERIFICATION** | Path, owner, date, command, or adjacent repo detail not proven from the mounted repository |

## Accepted inputs

Accepted inputs for this directory include:

| Input class | What belongs here | Minimum expectation |
|---|---|---|
| Candidate remote-sensing outputs | classified rasters, change maps, NDVI or vegetation products, thermal surfaces, flood extents, forecast-like modeled surfaces | clear subject, support, time window, CRS, and provenance |
| Reference / truth material | training and testing samples, field checks, review notes, external label sources, steward annotations | source basis and method documented |
| Validation artifacts | confusion matrices, per-class metrics, threshold tables, QA summaries, validation logs | reproducible method and result context |
| Method notes | metric definitions, acceptance rules, failure thresholds, known limitations | readable, versioned, reviewable |
| Publication-readiness evidence | sensitivity checks, modeled-output labeling, generalization decisions, release notes | explicit public-safe posture |
| Correction-linked material | supersession notes, revised metrics, replacement runs | visible lineage to earlier outputs |

## Exclusions

This directory does **not** own the following by default:

| Excluded material | Why it does not belong here | Where it should go instead |
|---|---|---|
| Raw source onboarding contracts | validation is downstream of intake | source/onboarding or ingest documentation |
| Canonical repo-wide release registry | this directory may reference releases but does not replace release governance | release / publication documentation |
| Public storytelling or narrative interpretation | validation supports public narrative but is not the narrative | story, report, or governed runtime surfaces |
| Secrets, signed URLs, tokens, credentials | never publish operational secrets in docs or QA outputs | secret management / runtime config |
| Sensitive exact-location disclosure | validation docs must not become a location-leak vector | generalized public-safe surfaces with review |
| Unbounded “AI summary” prose without source linkage | KFM does not admit uncited summary as truth | governed runtime with evidence-linked outputs |

## Directory tree

> [!NOTE]
> The tree below is a **PROPOSED starter layout** inferred from the attached corpus. Verify against the mounted repo before treating it as final.

```text
docs/analyses/remote-sensing/
└── validation/
    ├── README.md
    ├── methods/
    │   ├── README.md
    │   ├── metrics/
    │   ├── scripts/
    │   └── thresholds/
    ├── results/
    │   ├── README.md
    │   ├── confusion-matrices/
    │   ├── metrics/
    │   └── summaries/
    ├── reports/
    │   ├── README.md
    │   ├── daily/
    │   └── releases/
    └── governance.md
```

## Quickstart

### Minimum manual flow

1. Identify the candidate output and its intended use.
2. Confirm the candidate has source, time, support, CRS, and method context.
3. Run the validation harness or the steward/manual review path.
4. Produce or update a `ValidationReport`.
5. Link the report to the candidate `DatasetVersion`.
6. Decide whether the output is:
   - releasable
   - releasable only as **generalized**, **partial**, or **modeled**
   - **stale-visible** with explicit limits
   - quarantined for rework
7. Preserve downstream release and correction linkage.

### Starter commands

```bash
# PROPOSED / NEEDS VERIFICATION
make validate-remote-sensing
make docs-validate
```

> [!TIP]
> If these entrypoints do not exist in the mounted repo, keep the artifact model and gate logic intact and change only the invocation layer after inspection.

## Workflow

```mermaid
flowchart LR
    A[Candidate output / DatasetVersion] --> B[Preflight: support, CRS, time, provenance]
    B --> C[Method-specific validation + reference-data checks]
    C --> D[ValidationReport]
    D --> E[ReviewRecord + DecisionEnvelope]
    E -->|approved| F[CatalogClosure + ReleaseManifest]
    E -->|approved with limits| G[generalized / partial / modeled / stale-visible release]
    E -->|denied or quarantined| H[rework / correction path]
    F --> I[EvidenceBundle + ProjectionBuildReceipt]
    G --> I
    H --> C
```

### Reading rule

Validation moves **forward** through the same trust structure as publication:

`candidate -> validation -> review -> release linkage -> downstream use -> correction if needed`

It is not a sidecar.

## Validation minimums

The matrix below is a **PROPOSED KFM starter minimum** for remote-sensing validation. It combines **CONFIRMED** KFM contract doctrine with remote-sensing method guidance from the attached corpus.

| Check family | What to validate | Why it matters |
|---|---|---|
| Provenance | source basis, acquisition window, processing lineage, operator/reviewer context | without this, the output cannot be interpreted honestly |
| Spatial semantics | CRS, datum, projection, pixel alignment, support/resolution, extent | spatial outputs become misleading when support is unclear |
| Temporal semantics | acquisition date, composite window, seasonality, stale tolerance, as-of meaning | snapshot bias is a recurring failure mode |
| Radiometric / spectral context | cloud masking, scaling, emissivity assumptions, sensor mix, spectral meaning | remote-sensing outputs are measurements, not just pictures |
| Geometry / topology / alignment | vector validity, edge continuity, raster/vector alignment, seam handling | invalid or misaligned geometry can quietly corrupt downstream analysis |
| Reference data quality | label source, sampling logic, field checks, steward review, class balance | a metric without trustworthy reference data can be worse than no metric |
| Classification quality | confusion matrix, overall accuracy, producer’s accuracy, user’s / consumer’s accuracy, kappa, class-level error analysis | these are core release checks for labeled outputs |
| Generalization performance | train/test gap, leakage risk, spatial autocorrelation, holdout logic | prevents “good-looking” overfit models from being released |
| Aggregation discipline | unit of support, rollup logic, and what heterogeneity is hidden | aggregation can suppress hotspots and local variation |
| Publication safety | modeled-output labeling, uncertainty disclosure, generalized coordinates, rights/sensitivity checks | a technically valid output can still be unsafe to publish |

## Metrics and interpretation

### Core classification metrics

| Metric | What it tells you | Minimum interpretation rule |
|---|---|---|
| Confusion matrix | where the classifier is right and wrong by class | inspect off-diagonal errors, not just the headline score |
| Overall accuracy | proportion classified correctly | useful, but insufficient on its own |
| Producer’s accuracy | how well real instances of a class were captured | check omission risk |
| User’s / consumer’s accuracy | how reliable the predicted class is | check commission risk |
| Kappa | agreement beyond chance | treat as contextual, not sovereign |
| Precision / recall / F1 | useful when class imbalance or workflow design makes them more legible than classic remote-sensing naming | document explicitly if used |

### Interpretation rules

- A strong training score with a weaker test score is a warning sign, not a success story.
- Training and testing samples that are too close in space can inflate apparent accuracy.
- A higher-resolution product is not automatically a higher-quality product.
- A single-date output can be analytically wrong when the decision needs seasonal or multi-date context.
- Ward-, county-, basin-, or district-level rollups can hide within-unit heterogeneity.

> [!WARNING]
> Do not publish a confident narrative from a smooth metric alone. KFM requires visible uncertainty, visible method, and a visible evidence route.

## Artifacts & traceability

The table below grounds this directory in KFM’s broader artifact system.

| Artifact family | Remote-sensing use in or around this directory | Status |
|---|---|---|
| `SourceDescriptor` | declares the scene, sensor, or upstream endpoint contract | **CONFIRMED doctrine** / usually upstream |
| `IngestReceipt` | proves fetch and landing of source material | **CONFIRMED doctrine** / usually upstream |
| `ValidationReport` | primary validation object for this directory | **CONFIRMED doctrine** |
| `DatasetVersion` | candidate or promoted output to which validation applies | **CONFIRMED doctrine** |
| `DecisionEnvelope` | machine-readable release or denial outcome for the candidate | **CONFIRMED doctrine** |
| `ReviewRecord` | human review, escalation, or approval for consequential releases | **CONFIRMED doctrine** |
| `CatalogClosure` | outward metadata and lineage closure where publication becomes inspectable | **CONFIRMED doctrine** |
| `ReleaseManifest` / `ReleaseProofPack` | binds validation to publication readiness | **CONFIRMED doctrine** |
| `ProjectionBuildReceipt` | records derived map, tile, export, or preview builds from released scope | **CONFIRMED doctrine** |
| `EvidenceBundle` | supports downstream claim, story, export, or answer use | **CONFIRMED doctrine** |
| `CorrectionNotice` | preserves visible lineage when a validated product is replaced, generalized, or withdrawn | **CONFIRMED doctrine** |

### Smallest useful remote-sensing bundle

For most release-bearing outputs, the smallest useful bundle is:

- candidate output reference
- method summary
- validation metrics
- reference data / truth note
- uncertainty note
- publication-safety note
- release or correction linkage

## Governance and publication

### Trust-visible release states

Use explicit surface-state labels whenever they change meaning:

| State | Meaning | Release consequence |
|---|---|---|
| **observed** | directly tied to measured/observed source material | may be publishable if other gates pass |
| **derived** | analytically transformed from released source material | must remain visibly derived |
| **modeled** | inferred, forecast-like, simulated, or predictive | must stay visibly tagged as modeled |
| **generalized** | precision intentionally reduced | acceptable for public-safe release where exactness is risky |
| **partial** | incomplete by support, time, coverage, or method | cannot read as complete |
| **stale-visible** | still shown, but beyond declared freshness tolerance | must remain visibly stale |
| **withdrawn** | no longer fit for use | keep visible lineage, do not silently erase |
| **superseded** | replaced by a later version | preserve the replacement path |

### FAIR+CARE / sensitivity rules

| Rule | Practical consequence |
|---|---|
| Publish only public-safe or explicitly generalized scopes when precision is risky | avoid “how to locate” instructions and unnecessary exact coordinates |
| Treat ecological, archaeological, Indigenous, biodiversity, or exact-location-sensitive outputs as review-bearing | validation can pass technically and still fail publication review |
| Keep modeled outputs visibly tagged as modeled | inferred surfaces must not read like observations |
| Fail closed when governance status is unclear | do not silently publish because a result exists |
| Keep review and correction visible | validation does not erase later correction obligations |

### Remote-sensing honesty rules

- Document acquisition dates and composite windows.
- State when cloud cover, sensor substitution, emissivity assumptions, or gap-filling changes interpretation.
- Do not flatten field observations, remote sensing, and administrative records into one evidentiary class.
- When rollups are used, name the support unit and what fine-grained variation is lost.

## Usage

### What maintainers should add here

- new method summaries
- metric definitions and thresholds
- release-ready validation summaries
- result indexes
- links to correction or supersession notices
- reviewer guidance for recurring product families

### What maintainers should not add here

- long free-form research essays
- unlinked public storytelling
- opaque screenshots with no artifact references
- undocumented “final accuracy” claims
- secrets, tokens, or signed links

## Definition of done

A remote-sensing validation package is ready for downstream use only when all relevant gates below are satisfied.

- [ ] candidate output is identified unambiguously
- [ ] source, acquisition, and processing context are recorded
- [ ] CRS, extent, support, and temporal window are documented
- [ ] method and threshold logic are readable and reviewable
- [ ] `ValidationReport` exists or is explicitly linked
- [ ] required metrics are attached
- [ ] class-level or product-level failure modes are noted
- [ ] train/test separation and leakage risks are addressed where applicable
- [ ] uncertainty or modeled-output status is visible
- [ ] publication-safety review is complete for the intended surface
- [ ] downstream release and correction linkage are explicit

## FAQ

### Is this directory only for land-cover classification?

No. It should also cover indices, thermal surfaces, flood extents, change products, forecast-like modeled outputs, and other remote-sensing deliverables that need governed QA before release.

### Is “high accuracy” enough for release?

No. KFM validation is broader than model scoring. A product can score well and still fail on provenance, temporal fit, CRS/support clarity, publication safety, or correction readiness.

### Can aggregated outputs hide important problems?

Yes. Wards, counties, basins, and other rollups can hide heterogeneity that remains visible at image or local support.

### What if a result is useful but incomplete?

Use a visible trust state such as **partial** or **stale-visible** if policy allows. Do not imply completeness that the evidence does not support.

### Where should public interpretation live?

In downstream reports, stories, or governed runtime surfaces that stay linked to evidence and release state. This README is about validation, not narrative replacement.

## Appendix

<details>
<summary><strong>Starter validation bundle (compact reference)</strong></summary>

### A. Candidate package checklist

| Item | Required | Notes |
|---|---|---|
| Candidate output reference | Yes | file, asset, layer, or package ID |
| Acquisition / source window | Yes | include sensor/platform if relevant |
| CRS + support | Yes | projected/geographic meaning and resolution |
| Method note | Yes | algorithm, thresholds, composites, masks |
| Reference data note | Usually | required for supervised/classified outputs |
| Metrics bundle | Yes | confusion matrix or equivalent product checks |
| Uncertainty note | Yes | modeled, partial, stale, or known gaps |
| Reviewer note | When needed | especially for sensitive or consequential releases |
| Release / correction link | Yes | do not orphan the validation result |

### B. Product families this directory should handle well

- land-cover and class maps
- NDVI and vegetation condition
- thermal or LST products
- flood extent and water masks
- change-detection outputs
- composite imagery summaries
- forecast-like derived surfaces
- remote-sensing-backed environmental indicators

### C. First cleanup tasks after mounted-repo inspection

1. Replace owner placeholders.
2. Confirm whether `../README.md`, `methods/`, `results/`, and `governance.md` exist.
3. Confirm actual automation entrypoints and validation commands.
4. Replace inferred path strings with real repo paths.
5. Link direct contract or schema locations once verified.
6. Add one real example `ValidationReport` bundle if it exists.

</details>

---

[↑ Back to top](#remote-sensing-validation--quality-assurance)
