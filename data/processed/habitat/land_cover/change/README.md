<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-habitat-land-cover-change-readme
title: data/processed/habitat/land_cover/change/README.md — Habitat Land Cover Change Processed Data README
version: v0.1
type: readme; data-lifecycle-sublane; processed-stage-guide; habitat-domain-lane; land-cover-lane; change-detection-lane; remote-sensing-context-lane
status: draft; PROPOSED; data-root; processed-stage; habitat; land-cover; change-detection; temporal-comparison; observed; modeled-candidate; remote-sensing; source-role-aware; sensitivity-aware; release-gated; evidence-first
authors: ChatGPT-5.5 Thinking; reviewed_by: OWNER_TBD
owners: OWNER_TBD — Habitat steward · Land-cover steward · Change-detection steward · Remote-sensing data steward · Sensitivity reviewer · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-06-25
policy_label: public-doc; data; processed; habitat; land-cover; change; remote-sensing; lifecycle; governed; release-gated
tags: [kfm, data, processed, habitat, land-cover, change-detection, land-cover-change, temporal-comparison, remote-sensing, NLCD, vegetation-index, disturbance, conversion, habitat-patch, ecological-system, source-role, observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, EvidenceBundle, SourceDescriptor, ValidationReport, PolicyDecision, ReleaseManifest, RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED]
related:
  - ../README.md
  - ../../ecoregions/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../README.md
  - ../../../../../docs/domains/habitat/README.md
  - ../../../../../docs/domains/fauna/README.md
  - ../../../../../docs/domains/flora/README.md
  - ../../../../../docs/domains/soil/README.md
  - ../../../../../docs/domains/hydrology/README.md
  - ../../../../../docs/domains/agriculture/README.md
  - ../../../../../docs/domains/hazards/README.md
  - ../../../../../policy/domains/habitat/
  - ../../../../../policy/sensitivity/habitat/
  - ../../../../../contracts/domains/habitat/
  - ../../../../../schemas/contracts/v1/domains/habitat/
  - ../../../../raw/habitat/
  - ../../../../work/habitat/
  - ../../../../quarantine/habitat/
  - ../../../../catalog/domain/habitat/
  - ../../../../catalog/stac/habitat/
  - ../../../../catalog/dcat/habitat/
  - ../../../../catalog/prov/habitat/
  - ../../../../triplets/
  - ../../../../published/
  - ../../../../proofs/
  - ../../../../receipts/
  - ../../../../registry/sources/habitat/
  - ../../../../../release/candidates/habitat/
  - ../../../../../release/
  - ../../../../../pipelines/domains/habitat/
  - ../../../../../pipeline_specs/habitat/
  - ../../../../../tools/validators/
notes:
  - "This file replaces a blank placeholder at `data/processed/habitat/land_cover/change/README.md`."
  - "This is a child PROCESSED-stage lane under `data/processed/habitat/land_cover/` for normalized land-cover change artifacts and temporal-comparison derivatives. It is not a RAW source root, WORK scratch area, QUARANTINE bypass, CATALOG, TRIPLET, PUBLISHED, proof store, receipt store, source registry, policy authority, release authority, public API/UI output, or public map/tile output."
  - "Land-cover change artifacts are temporal comparison products. They may indicate class transitions or candidate disturbance/conversion context, but they are not by themselves habitat suitability, regulatory critical habitat, species occurrence, crop truth, hazard event truth, restoration priority, management decision, or land-use/legal determination."
  - "Habitat source roles must remain explicit: observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic are not interchangeable. Change detection may be observed-derived or modeled/candidate, but each artifact must declare its role and method."
  - "Sensitive joins to Fauna, Flora, private parcels, rare species, rare plants, wetlands, stewardship zones, hazards, agriculture, or steward-controlled biodiversity context must fail closed unless policy, review, evidence, transform receipts, release state, correction path, and rollback support public use."
  - "This README is a lane guide only. Contracts define semantic object meaning; schemas define machine shape; policy decides admissibility; release records decide publication."
  - "Rollback target for this expansion is previous blank placeholder blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# data/processed/habitat/land_cover/change

> Habitat PROCESSED-stage child lane for normalized land-cover change artifacts: temporal comparisons, class-transition summaries, observed-derived change layers, candidate disturbance/conversion indicators, and remote-sensing-derived change context that support habitat analysis but are not cataloged, triplet-projected, published, or released by this directory alone.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data/processed/habitat/land_cover/change" src="https://img.shields.io/badge/root-data%2Fprocessed%2Fhabitat%2Fland__cover%2Fchange-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Lifecycle: PROCESSED" src="https://img.shields.io/badge/lifecycle-PROCESSED-purple">
  <img alt="Role: source-role preserved" src="https://img.shields.io/badge/role-source--role--preserved-green">
  <img alt="Exposure: not public" src="https://img.shields.io/badge/exposure-not__public-critical">
</p>

**Status:** draft / PROPOSED  
**Owners:** OWNER_TBD — Habitat steward · Land-cover steward · Change-detection steward · Remote-sensing data steward · Sensitivity reviewer · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward  
**Path:** `data/processed/habitat/land_cover/change/README.md`  
**Owning root:** `data/processed/`  
**Domain segment:** `habitat`  
**Parent lane:** `data/processed/habitat/land_cover/`  
**Sublane:** `change` / land-cover temporal change and class-transition context  
**Lifecycle stage:** `PROCESSED`  
**Exposure posture:** not public by default; any public use requires governed catalog, EvidenceBundle, source-role and rights posture, sensitivity/policy review, ValidationReport, PolicyDecision, ReleaseManifest, correction path, and rollback target.  
**Truth posture:** CONFIRMED target was a blank placeholder · CONFIRMED parent land-cover lane is upstream of catalog/triplet/publication and blocks direct public use · CONFIRMED `LandCoverObservation` is separate from suitability, regulatory critical habitat, species occurrence, crop truth, soil truth, hydrology truth, hazard truth, and land-management instruction · PROPOSED change child-lane details · NEEDS VERIFICATION for actual child inventory, schemas, validators, fixtures, source descriptors, receipt families, policy enforcement, release linkage, and governed route behavior.

**Quick jumps:** [Purpose](#purpose) · [Lifecycle boundary](#lifecycle-boundary) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Change processed requirements](#change-processed-requirements) · [Source-role and sensitivity guardrails](#source-role-and-sensitivity-guardrails) · [Directory map](#directory-map) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`data/processed/habitat/land_cover/change/` holds processed land-cover change artifacts for the Habitat lane. These artifacts compare land-cover observations, class systems, source vintages, or remote-sensing-derived products across time or versions.

This lane may contain or point to normalized artifacts such as:

- land-cover class-transition records between two or more source vintages;
- observed-derived or model-assisted change layers with explicit source role and method;
- disturbance, conversion, recovery, persistence, or uncertainty candidates that remain evidence- and policy-bounded;
- change summaries by ecoregion, habitat patch, watershed, county, grid, or other policy-approved units;
- class-crosswalk-aware change matrices;
- source-vintage, version-pair, or comparison-window sidecars;
- public-candidate generalized change overlays that still require catalog and release review.

This lane does not make a habitat suitability claim by itself. It also does not prove species occurrence, critical habitat, ecological condition, restoration priority, crop/field truth, hydrologic condition, soil truth, hazard event, land ownership, land-use legality, or land-management status without downstream evidence, policy, catalog, release, and claim-specific contracts.

## Lifecycle boundary

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

```mermaid
flowchart LR
  RAW[data/raw/habitat] --> WORK[data/work/habitat]
  WORK --> QUAR[data/quarantine/habitat]
  WORK --> LCC[data/processed/habitat/land_cover/change]
  QUAR --> LCC
  LCC --> LC[data/processed/habitat/land_cover]
  LCC --> PROC[data/processed/habitat]
  LCC --> CAT[data/catalog/domain/habitat]
  LCC --> STAC[data/catalog/stac/habitat]
  LCC --> DCAT[data/catalog/dcat/habitat]
  LCC --> PROV[data/catalog/prov/habitat]
  LCC --> TRIP[data/triplets/.../habitat]
  LCC -. supports .-> PROOF[data/proofs]
  LCC -. emits / references .-> RECEIPT[data/receipts]
  CAT --> PUBLISHED[data/published/.../habitat]
  STAC --> PUBLISHED
  DCAT --> PUBLISHED
  PROV --> PUBLISHED
  TRIP --> PUBLISHED
  PUBLISHED --> REL[release]
```

`data/processed/habitat/land_cover/change/` is upstream of catalog, triplet, publication, and release. It must not be used as a normal public map/API/UI/AI source.

## Repo fit

| Responsibility | Correct home | Rule |
|---|---|---|
| Raw source rasters, source-native land-cover downloads, original pixels/classes/geometry, source exports, source logs, or source identifiers | `data/raw/habitat/` | Not this lane. |
| In-process raster differencing, class-crosswalk experiments, temporal matching, change-threshold tuning, QA, notebooks, or scratch products | `data/work/habitat/` | Not this lane. |
| Unresolved rights, unresolved source role, malformed comparison windows, disputed classes, sensitive joins, unsafe geometry, or not-yet-reviewed change material | `data/quarantine/habitat/` | Not this lane until review/admission allows. |
| Processed land-cover observations and context artifacts | `data/processed/habitat/land_cover/` | Parent lane. |
| Processed land-cover change artifacts | `data/processed/habitat/land_cover/change/` | This lane. |
| Parent processed Habitat lane | `data/processed/habitat/` | Parent lane; still not public by default. |
| Habitat catalog records | `data/catalog/domain/habitat/` | Downstream catalog stage. |
| Habitat STAC/DCAT/PROV records | `data/catalog/{stac,dcat,prov}/habitat/` | Downstream catalog projections if accepted. |
| Habitat triplet/graph records | `data/triplets/.../habitat/` | Downstream graph stage; must not expose restricted geometry or unsafe joins. |
| Published public-safe Habitat products | `data/published/.../habitat/` | Downstream only after release. |
| EvidenceBundle/proof records | `data/proofs/` | Separate proof family. |
| Source, run, model-run, transform, validation, policy, correction, access, and release receipts | `data/receipts/` | Separate receipt family. |
| Habitat source registry records | `data/registry/sources/habitat/` | Separate source authority. |
| Release candidates and release manifests | `release/candidates/habitat/`, `release/` | Separate publication authority. |
| Habitat contracts | `contracts/domains/habitat/` | Object meaning; not data. |
| Habitat schemas | `schemas/contracts/v1/domains/habitat/` | Machine shape; not data. |
| Habitat policy and sensitivity rules | `policy/domains/habitat/`, `policy/sensitivity/habitat/` if accepted | Admissibility authority; not data. |
| Validators, tests, fixtures, pipelines, pipeline specs, apps, packages | `tools/validators/`, `tests/`, `fixtures/`, `pipelines/`, `pipeline_specs/`, `apps/`, `packages/` | Separate roots. |

## Accepted contents

Processed land-cover change artifacts may include:

- normalized change records with source vintages, comparison windows, class systems, source roles, rights posture, validation state, uncertainty, and digest posture;
- class-transition matrices or summaries that preserve class-crosswalk assumptions;
- change rasters, vectors, summaries, or tile-candidate derivatives that remain upstream of release;
- observed-derived change artifacts where both input observation vintages remain traceable;
- modeled or candidate change artifacts only when model role, method, input receipts, and uncertainty are explicit;
- change summaries by habitat patch, ecological system, ecoregion, watershed, county, grid, or other policy-approved units;
- links from land-cover change to `HabitatPatch`, `EcologicalSystem`, `SuitabilityModel`, `Restoration Opportunity`, or `UncertaintySurface` inputs when ownership and source-role boundaries remain visible;
- review-ready artifacts for public-safe change-map candidates when source rights, sensitivity joins, and policy posture are explicit;
- lane-local README or manifest notes that explain processed-data boundaries without becoming public outputs or authority records.

## Exclusions

Do not store these under `data/processed/habitat/land_cover/change/`:

- RAW source rasters, source-native downloads, steward originals, source media, logs, original source geometries, source identifiers, or unprocessed agency/partner exports.
- WORK/scratch files, notebooks, temporal-matching experiments, raster-differencing trials, threshold tuning, unresolved QA joins, class-crosswalk trials, classifier trials, or redaction-debug outputs.
- Quarantined or unresolved sensitive/rights/source-role material.
- Catalog records, STAC/DCAT/PROV records, triplet/graph records, published products, proof records, receipt records, source registry records, release decisions, schemas, policy rules, validators, tests, fixtures, pipelines, pipeline specs, app/UI/API code, or packages.
- Species occurrence records, plant specimen records, rare-species/rare-plant location records, soil map unit truth, hydrology measurement truth, crop/field truth, hazard event truth, archaeology site truth, or land/ownership truth.
- Habitat suitability scores, regulatory critical-habitat determinations, restoration prescriptions, management decisions, corridor/connectivity claims, ecoregion truth, ecological condition claims, crop-change claims, flood/fire/drought hazard claims, or land-use/legal determinations unless separate object contracts, evidence, validation, policy, and release state support them.
- Public API/UI/tile payloads, direct downloads, Focus Mode answers, public map layers, landowner/parcel targeting aids, ecological/legal advice, operational land-management guidance, emergency alerts, or life-safety guidance.
- Redaction parameters, aggregation thresholds, small-cell thresholds, fuzzing radii, seeds, exact transform offsets, access credentials, secrets, private agreement terms, field access routes, or implementation details that could aid exposure or unauthorized access.

## Change processed requirements

PROPOSED until concrete validators, policies, fixtures, receipts, and access-control enforcement are verified:

| Requirement | Meaning |
|---|---|
| Source trace | Each source-derived artifact should trace to SourceDescriptor or habitat source registry context. |
| Evidence linkage | Claims about land-cover transition, source vintages, comparison window, class crosswalk, method, uncertainty, habitat context, transform, review, or release readiness should resolve downstream to EvidenceBundle/proof context where appropriate. |
| Source role | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles must remain explicit and not interchangeable. |
| Change identity | Input source vintages, comparison window, class systems, class-crosswalk version, spatial reference, cell/geometry footprint, method, and normalized digest should remain auditable. |
| Time semantics | Source time, observed time, valid time, retrieval time, comparison-window time, raster/classification version time, correction time, and release time should remain distinguishable where material. |
| Rights posture | Agency, steward, license, redistribution, attribution, derivative-use, and remote-sensing source terms should be resolved or held closed for all inputs. |
| Sensitivity posture | Joins to sensitive fauna/flora occurrences, rare-plant locations, private parcels, wetlands, stewardship zones, hazards, agriculture, or small-cell outputs should carry restriction/generalization/denial posture. |
| Transform linkage | Reprojection, reclassification, differencing, aggregation, redaction, suppression, withholding, delayed publication, or public-safe geometry transform should link to the appropriate receipt family. |
| Review state | Habitat steward, land-cover steward, source steward, sensitivity reviewer, data-quality reviewer, and release authority review should be recorded where required. |
| Policy decision | Restricted, public-candidate, and public transitions require PolicyDecision/admissibility posture where policy requires it. |
| Catalog readiness | Processed change artifacts intended for discovery should promote through catalog/triplet lanes, not directly to public use. |
| Release readiness | Public use requires ReleaseManifest or release-linked state, published output path, correction path, and rollback target. |
| No public surface by default | Processed change artifacts must not be exposed directly as public maps, tiles, APIs, downloads, Focus Mode answers, or AI-answer sources. |

## Source-role and sensitivity guardrails

- Habitat owns landscape/habitat context, not species records.
- Land-cover change is temporal comparison context, not automatic proof of habitat quality, restoration need, crop change, hazard damage, regulatory critical habitat, or ecological condition.
- `LandCoverObservation` inputs may be observed; a change product may be observed-derived, modeled, aggregate, or candidate depending on method. The role must be explicit and must not be upgraded during promotion.
- A modeled change product is not regulatory critical habitat.
- A suitability surface is not an occurrence.
- A land-cover transition is not a habitat-quality score, restoration priority, corridor, stewardship decision, crop truth, soil truth, hydrology truth, hazard event, or land-management instruction by itself.
- Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic source roles must not be relabeled during promotion.
- Sensitive habitat × fauna, habitat × flora, habitat × parcel, habitat × hydrology, habitat × soil, habitat × agriculture, and habitat × hazards joins must preserve ownership, source role, sensitivity, and EvidenceBundle support.
- Sensitive geometry must be generalized, redacted, delayed, restricted, or denied before tile generation; style filters are not a sensitivity control.
- Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state blocks public promotion.
- Public clients and Focus Mode must use governed APIs, released artifacts, catalog/triplet records, EvidenceBundle-backed payloads, and policy-safe envelopes, not this directory directly.

> [!CAUTION]
> Do not expose `data/processed/habitat/land_cover/change/` directly as a public map, tile service, API, UI, download, Focus Mode answer, AI answer source, species-location service, critical-habitat determination, restoration prescription, crop-change claim, hazard-impact claim, landowner/parcel targeting aid, ecological/legal advice, operational land-management guidance, emergency alert, or life-safety product. Processed land-cover change data remains inside the trust membrane until governed promotion and release.

## Directory map

Actual child inventory remains **NEEDS VERIFICATION**. Use this as a proposed local organization pattern only after confirming current repo convention and validators.

```text
data/processed/habitat/land_cover/change/
├── README.md
├── transitions/              # PROPOSED — normalized class-transition records
├── rasters/                  # PROPOSED — processed change raster derivatives, not published tiles
├── vectors/                  # PROPOSED — processed change vector derivatives
├── matrices/                 # PROPOSED — class-transition matrices
├── summaries/                # PROPOSED — region/patch-level change summaries
├── comparison_windows/       # PROPOSED — version/window sidecars
├── uncertainty/              # PROPOSED — change confidence/uncertainty sidecars
├── generalized/              # PROPOSED — public-candidate generalized derivatives
├── validation/               # PROPOSED — lane-local validation notes, not ValidationReport authority
├── joins/                    # PROPOSED — reviewed context joins only, not species/crop/soil/hydrology/hazard truth
├── _manifests/               # PROPOSED — lane-local non-release manifests only
└── _README_TODO.md           # PROPOSED — remove after actual child inventory is documented
```

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous file | CONFIRMED | Target existed as a blank placeholder. | Did not define land-cover change processed boundaries. |
| `data/processed/habitat/land_cover/README.md` | CONFIRMED parent README | Parent lane defines processed land-cover observations/context, upstream lifecycle posture, hard exclusions, source-role preservation, and public-surface denial. | Does not prove child inventory or validators. |
| `data/processed/README.md` | CONFIRMED | PROCESSED data is upstream of catalog, triplets, publication, and release and is not the normal public surface. | Does not prove Habitat child inventory or enforcement. |
| `docs/domains/habitat/README.md` | CONFIRMED doctrine / PROPOSED implementation | Habitat admits sources through SourceDescriptor, preserves source roles, includes NLCD land cover and remote-sensing vegetation indices as source families, names LandCoverObservation as an object family, and defines lifecycle promotion gates. | Implementation maturity remains NEEDS VERIFICATION. |
| `policy/domains/habitat/` and `policy/sensitivity/habitat/` | NEEDS VERIFICATION | Expected admissibility homes. | Current policy files and enforcement were not verified in this task. |
| `contracts/domains/habitat/` and `schemas/contracts/v1/domains/habitat/` | NEEDS VERIFICATION | Expected object contract/schema homes for Habitat families. | Specific change object files and validators were not verified in this task. |

## Validation checklist

- [ ] Confirm actual child directories under `data/processed/habitat/land_cover/change/`.
- [ ] Confirm whether `change/` is the accepted processed Habitat lane name or should be reconciled with `land_cover_change/`, `change_detection/`, `transitions/`, or another object-family naming convention.
- [ ] Confirm parent `data/processed/habitat/README.md` is expanded beyond stub.
- [ ] Confirm LandCoverObservation and land-cover change/transition object contracts and schema paths.
- [ ] Confirm source-role vocabulary and anti-collapse validators for observed/regulatory/modeled/aggregate/administrative/candidate/synthetic roles.
- [ ] Confirm validators, fixtures, CI checks, policy checks, and access-control enforcement for processed land-cover change artifacts.
- [ ] Confirm SourceDescriptor/source registry linkage for every input source vintage and derived change artifact.
- [ ] Confirm RunReceipt, TransformReceipt, ModelRunReceipt where applicable, ValidationReport, PolicyDecision, CorrectionNotice, ReleaseManifest, correction path, and rollback target.
- [ ] Confirm sensitive fauna/flora joins, rare-plant joins, private-parcel joins, wetlands/stewardship joins, hazard/agriculture joins, small-cell outputs, rights-unclear sources, unresolved source roles, redaction parameters, transform secrets, and release-unclear artifacts cannot enter public routes.
- [ ] Confirm public-candidate transitions are governed, evidence-backed, source-role-safe, rights-safe, sensitivity-safe, review-backed, release-linked, and reversible.
- [ ] Confirm no RAW, WORK, QUARANTINE, CATALOG, TRIPLET, PUBLISHED, proof, receipt, registry, release, schema, policy, validator, package, pipeline, app, API, public map, public tile, direct download, Focus Mode answer, critical-habitat determination, restoration prescription, crop-change claim, hazard-impact claim, land-management guidance, or life-safety artifact is misplaced here.
- [ ] Confirm public clients and Focus Mode cannot read this lane directly as public truth, public location service, public map, public tile, public API, public UI, or AI-answer source.

## Rollback

Rollback is required if this lane becomes a RAW source-data root, WORK scratch root, QUARANTINE bypass, public output root, `data/published/` substitute, public-candidate shortcut, sensitive-join exposure path, transform-secret exposure path, agreement/credential exposure path, proof store, receipt store, catalog root, triplet root, source-registry root, release-decision root, schema root, policy root, validator root, implementation root, public API shortcut, public UI shortcut, public tile shortcut, public exposure shortcut, species-location source, critical-habitat determination source, restoration prescription source, crop-change claim source, hazard-impact claim source, land-management guidance source, or life-safety guidance source.

Rollback target for this expansion: previous blank placeholder blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
