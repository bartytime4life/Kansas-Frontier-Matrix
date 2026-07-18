<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-geology-readme
title: Geology Release Candidate Review Lane
type: per-domain-release-candidate-index
version: v2
status: draft; repository-grounded; sensitivity-aware; pre-publication
contract_version: "3.0.0"
owners: [bartytime4life]
created: 2026-07-03
updated: 2026-07-18
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: release/
lane_role: geology candidate dossier index and claim-class-aware pre-publication review boundary
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 9f1fccb0a8eb40dfe49eaf01bb4756475725150d
  prior_blob: 9dd4665578364dfb0862b6666cbff411151f8ede
  bounded_candidate_inventory: parent README only; no child candidate dossier established
related:
  - ../README.md
  - ../../README.md
  - ../../manifests/README.md
  - ../../promotion_decisions/README.md
  - ../../correction_notices/README.md
  - ../../rollback_cards/README.md
  - ../../withdrawal_notices/README.md
  - ../../changelog/README.md
  - ../../../data/processed/geology/README.md
  - ../../../data/published/geology/README.md
  - ../../../data/registry/sources/geology/README.md
  - ../../../data/registry/sensitivity/geology/README.md
  - ../../../data/proofs/geology/README.md
  - ../../../contracts/domains/geology/README.md
  - ../../../schemas/contracts/v1/domains/geology/README.md
  - ../../../policy/domains/geology/README.md
  - ../../../tests/domains/geology/README.md
  - ../../../fixtures/domains/geology/README.md
  - ../../../tools/validators/geology/README.md
  - ../../../tools/validators/domains/geology/README.md
  - ../../../docs/domains/geology/RELEASE_INDEX.md
  - ../../../docs/domains/geology/SENSITIVITY.md
  - ../../../docs/domains/geology/DATA_LIFECYCLE.md
  - ../../../docs/runbooks/geology/ROLLBACK_RUNBOOK.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/domain-geology.yml
  - ../../../.github/workflows/release-dry-run.yml
tags: [kfm, release, candidates, geology, natural-resources, subsurface, anti-collapse, evidence, sensitivity, rollback]
notes:
  - "This README indexes Geology release-candidate dossiers and defines their pre-publication review boundary. It is not a candidate, source, evidence, policy, geologic interpretation, resource certification, mineral-rights record, engineering opinion, release, legal, investment, extraction, emergency, or publication authority record."
  - "The bounded repository search and current Geology workflow establish no child candidate dossier under this lane."
  - "The literal sentence 'A candidate is not a release.' is retained for the current domain-geology readiness workflow; it is a compatibility signal, not release proof."
  - "Exact or reverse-engineerable subsurface locations, private-well detail, restricted well logs, operator/parcel joins, extraction-targetable resource detail, and public-safety-sensitive infrastructure context must not appear in this public-review lane."
  - "CODEOWNERS review routing is not a stewardship assignment, mineral/property-rights determination, independent review, engineering certification, release approval, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `release/candidates/geology/` — Geology Release Candidate Review Lane

> Index Geology and Natural Resources release-candidate dossiers, preserve blockers and safe support pointers, and prevent geologic units, structures, boreholes, well logs, samples, geophysics, geochemistry, mineral occurrences, deposits, estimates, extraction sites, reclamation records, cross-sections, or modeled subsurface products from being treated as released, certified, operationally safe, economically proven, or legally authoritative before evidence, rights, sensitivity, claim-class, validation, review, correction, and rollback gates close.

![status](https://img.shields.io/badge/status-repository--grounded%20draft-orange)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![domain](https://img.shields.io/badge/domain-geology%2Fnatural--resources-795548)
![publication](https://img.shields.io/badge/publication-not_yet-red)
![posture](https://img.shields.io/badge/posture-claim--class%20anti--collapse-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![contract](https://img.shields.io/badge/contract-v3.0.0-1f6feb)

> [!IMPORTANT]
> **Safe conclusion at `main@9f1fccb0…`:** the bounded Geology candidate inventory contains this parent README and no verified child candidate dossier. The Geology release index contains placeholder register rows rather than verified releases, emitted public carriers remain unverified, policy is still a scaffold, and current domain automation is an explicit readiness-hold workflow. No inspected README, placeholder test, proof guide, schema or contract file, workflow result, merge, or generated receipt establishes a Geology candidate, reserve, resource estimate, engineering conclusion, release, or public-safe exact subsurface location.
>
> Differently named, unindexed, generated, history-only, external, restricted-system, or runtime-only material remains **UNKNOWN** until directly verified.

## Quick navigation

[Purpose](#purpose) ·
[Status](#status-and-evidence-boundary) ·
[Authority](#authority-and-repository-fit) ·
[Inventory](#current-candidate-inventory) ·
[Lifecycle](#candidate-lifecycle) ·
[Contents](#what-belongs-here) ·
[Exclusions](#what-does-not-belong-here) ·
[Admission](#candidate-admission-contract) ·
[Identity](#geology-identity-source-role-and-claim-class-anti-collapse) ·
[Sensitivity](#subsurface-sensitivity-rights-and-safe-representation) ·
[Reality boundary](#interpretation-model-and-reality-boundary) ·
[Time](#time-vintage-scale-and-stale-state) ·
[Gates](#geology-release-gates) ·
[Dossier](#required-dossier-structure) ·
[Validation](#validation-proof-and-fixture-posture) ·
[Automation](#automation-posture) ·
[Handoff](#review-and-release-handoff) ·
[Correction](#correction-withdrawal-and-rollback) ·
[Public boundary](#public-api-map-export-and-ai-boundary) ·
[Maintenance](#maintenance-and-definition-of-done) ·
[Evidence](#evidence-ledger) ·
[Open items](#open-verification) ·
[Rollback](#rollback-for-this-readme)

---

## Purpose

`release/candidates/geology/` is the Geology and Natural Resources pre-publication review lane under the `release/` responsibility root.

It exists to answer these bounded questions:

1. Which Geology candidate dossiers are currently indexed?
2. What object family, claim class, source role, spatial scope, depth/vertical reference, time/vintage, scale, audience, and artifact scope does each candidate claim?
3. Which source, evidence, rights, sensitivity, validation, policy, review, correction, and rollback records support it?
4. Does the candidate preserve occurrence, deposit, estimate, permit, production, reserve, observation, interpretation, model, aggregate, and synthetic distinctions?
5. Does any exact subsurface, private-well, well-log, operator/parcel, extraction-targetable, or infrastructure-sensitive detail require restriction, generalization, redaction, quarantine, or denial?
6. Which shared release lane owns the next governed record?

**A candidate is not a release.** A candidate folder, README, schema pass, proof index, workflow result, map preview, pull request, merge, generated receipt, or file under `data/published/` does not by itself authorize public use or certify geologic, engineering, resource, reserve, legal, investment, extraction, safety, or regulatory conclusions.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move, branch merge, alias change, or rendering event.

[Back to top](#top)

---

## Status and evidence boundary

| Field | Current posture |
|---|---|
| Document type | Geology candidate-lane index and pre-publication review contract |
| Owning root | `release/` |
| Candidate lane | `release/candidates/geology/` |
| Bounded child inventory | No child candidate dossier established by current repository search |
| Release register | Placeholder rows only; no verified release instance established by the inspected index |
| Published carrier posture | Directory guidance exists; emitted release-linked instances remain **NEEDS VERIFICATION** |
| Source registry | Grounded README exists; subtype-first versus domain-first topology remains unresolved |
| Sensitivity registry | Grounded README exists; parent contract and concrete record inventory remain unresolved |
| Policy | `policy/domains/geology/README.md` is a greenfield scaffold |
| Proof | `data/proofs/geology/README.md` is a draft proof guide; concrete proof inventory and producer remain unverified |
| Tests | Five surfaced direct test modules are one-line `PROPOSED` placeholders |
| Automation | `domain-geology` is a read-only readiness-hold workflow; general release dry run is TODO-only |
| Public effect of this README | None |
| Human review | Required; this document does not self-approve |

### Truth labels used here

| Label | Meaning in this README |
|---|---|
| `CONFIRMED` | Directly inspected in the current repository session. |
| `PROPOSED` | Recommended contract or handling rule not yet proven as accepted implementation. |
| `NEEDS VERIFICATION` | Checkable but not verified strongly enough for operational reliance. |
| `UNKNOWN` | Not established by the bounded evidence available. |
| `CONFLICTED` | Competing path, vocabulary, or authority forms exist and need resolution. |

The bounded search is not a recursive filesystem proof. It supports the safe statement that no child candidate dossier surfaced; it does not prove that no history-only, external, generated, restricted-system, or differently named candidate-like material exists.

[Back to top](#top)

---

## Authority and repository fit

Directory Rules place release decisions under the `release/` responsibility root. This path is therefore appropriate for candidate review state, not payload storage, source authority, evidence storage, policy, schemas, contracts, executable validation, or public delivery.

| Responsibility | Owning lane | This README may do |
|---|---|---|
| Candidate dossier index | `release/candidates/geology/` | Index public-safe dossier metadata and blockers. |
| Processed candidate artifact | [`data/processed/geology/`](../../../data/processed/geology/README.md) | Point to immutable candidate material; never duplicate it here. |
| Source admission | [`data/registry/sources/geology/`](../../../data/registry/sources/geology/README.md) | Point to accepted source records and unresolved topology. |
| Sensitivity control state | [`data/registry/sensitivity/geology/`](../../../data/registry/sensitivity/geology/README.md) | Point to public-safe sensitivity-review state; do not expose restricted detail. |
| Evidence and proof | [`data/proofs/geology/`](../../../data/proofs/geology/README.md) | Point to resolvable support; do not become proof storage. |
| Semantic meaning | [`contracts/domains/geology/`](../../../contracts/domains/geology/README.md) | Reference object and claim meaning. |
| Machine shape | [`schemas/contracts/v1/domains/geology/`](../../../schemas/contracts/v1/domains/geology/README.md) | Reference accepted schemas. |
| Policy | [`policy/domains/geology/`](../../../policy/domains/geology/README.md) | Reference decisions and obligations; do not define them here. |
| Tests and fixtures | [`tests/domains/geology/`](../../../tests/domains/geology/README.md), [`fixtures/domains/geology/`](../../../fixtures/domains/geology/README.md) | Reference deterministic public-safe validation support. |
| Validators | [`tools/validators/geology/`](../../../tools/validators/geology/README.md), [`tools/validators/domains/geology/`](../../../tools/validators/domains/geology/README.md) | Reference accepted commands and reports once established. |
| Promotion decision | [`release/promotion_decisions/`](../../promotion_decisions/README.md) | Point to the governed state-transition record. |
| Release manifest | [`release/manifests/`](../../manifests/README.md) | Point to the release authority record. |
| Correction | [`release/correction_notices/`](../../correction_notices/README.md) | Point to public correction lineage. |
| Withdrawal | [`release/withdrawal_notices/`](../../withdrawal_notices/README.md) | Point to withdrawal state. |
| Rollback | [`release/rollback_cards/`](../../rollback_cards/README.md) | Point to reversal authority and prior safe target. |
| Published carrier | [`data/published/geology/`](../../../data/published/geology/README.md) | Point to released public-safe carriers only after gates close. |

> [!WARNING]
> `release/` owns decisions. `data/published/` owns released carriers. `data/proofs/` owns proof support. `data/receipts/` owns process memory. A candidate README must not collapse those authority surfaces.

[Back to top](#top)

---

## Current candidate inventory

| Candidate | Scope | Candidate state | Manifest readiness | Public effect |
|---|---|---|---|---|
| *(none established by bounded inspection)* | — | `NO_ACTIVE_CANDIDATE` | Not applicable | None |

### Inventory rules

A child entry may be listed only when the repository establishes at least:

- a stable candidate ID and version;
- an immutable artifact pointer and digest;
- an object-family and claim-class declaration;
- a public-safe scope summary;
- source, evidence, rights, sensitivity, validation, review, correction, and rollback pointers;
- an explicit state and blockers; and
- no restricted payload, exact sensitive geometry, proprietary content, or reverse-engineering aid in the public dossier.

README prose, planning examples, placeholder paths, schema examples, generated receipts, branch names, issue text, and workflow holds are not candidates.

[Back to top](#top)

---

## Candidate lifecycle

Use finite candidate states without redefining the project-wide release vocabulary.

| Candidate state | Meaning | Public? |
|---|---|---|
| `PROPOSED` | Candidate identity exists, but assembly and closure are incomplete. | No |
| `ASSEMBLING` | Artifact and support references are being assembled. | No |
| `RESTRICTED_REVIEW` | Review requires controlled context unavailable in the public dossier. | No |
| `READY_FOR_REVIEW` | Public-safe dossier metadata and required support are ready for reviewers. | No |
| `BLOCKED` | One or more mandatory gates failed or remain unresolved. | No |
| `REPAIR_REQUIRED` | Candidate can continue only after correction and re-validation. | No |
| `STALE` | Source, map vintage, model version, rights, permit/production status, review, schema, or evidence support aged out or was superseded. | No |
| `DEFERRED` | Review intentionally paused with a recorded reason. | No |
| `APPROVED_FOR_MANIFEST` | Independent review permits manifest preparation; this is still not release. | No |
| `PROMOTED` | A separate accepted PromotionDecision and ReleaseManifest govern the release transition. | Only through the released manifest and governed surface |
| `SUPERSEDED` | Replaced by a newer candidate or release while lineage is retained. | No as current |
| `WITHDRAWN` | Removed from consideration; reason and lineage retained. | No |

### Explicit hold outcomes

Use stable hold reasons where practical:

- `HOLD_FOR_ARTIFACT`
- `HOLD_FOR_SOURCE_ADMISSION`
- `HOLD_FOR_RIGHTS`
- `HOLD_FOR_SENSITIVITY`
- `HOLD_FOR_CLAIM_CLASS`
- `HOLD_FOR_EVIDENCE`
- `HOLD_FOR_VALIDATION`
- `HOLD_FOR_REALITY_BOUNDARY`
- `HOLD_FOR_POLICY`
- `HOLD_FOR_REVIEW`
- `HOLD_FOR_RELEASE_TOPOLOGY`
- `HOLD_FOR_CORRECTION_PATH`
- `HOLD_FOR_ROLLBACK`
- `HOLD_FOR_STALE_STATE`

A hold must identify the unresolved responsibility owner and the next check. It must not hide uncertainty behind a generic “pending” label.

[Back to top](#top)

---

## What belongs here

- A parent README and public-safe child candidate dossiers.
- Stable candidate identity, version, state, scope, and blocker summaries.
- Immutable pointers to processed or accepted staging artifacts.
- Public-safe source, evidence, rights, sensitivity, validation, review, correction, and rollback references.
- Object-family, claim-class, source-role, spatial/vertical/time scope, scale, uncertainty, and audience declarations.
- Public-safe notes about representation boundaries and unresolved conflicts.
- Promotion-readiness recommendations that remain subordinate to PromotionDecision and ReleaseManifest authority.
- Supersession, withdrawal, and candidate-level correction lineage.

[Back to top](#top)

---

## What does not belong here

- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads.
- Source-native maps, well logs, LAS files, cores, geochemistry records, geophysics volumes, production tables, permit extracts, proprietary models, or bulk exports.
- Exact or reverse-engineerable borehole, core, private-well, sample, well-log, operator/parcel, sensitive resource, extraction-targetable, or infrastructure-sensitive locations.
- Mineral ownership, property title, water rights, parcel ownership, operator identity, private agreements, or proprietary economic detail.
- Reserve certification, engineering suitability, drilling advice, extraction recommendations, investment advice, legal conclusions, regulatory determinations, emergency warnings, or life-safety instructions.
- SourceDescriptor, schema, contract, policy, validator, fixture, proof, receipt, review, promotion, or manifest objects as primary records.
- Generated narratives, cross-sections, 3D scenes, interpreted surfaces, model output, or AI text presented as observed or authoritative truth.
- Credentials, tokens, private contacts, access routes, operational infrastructure detail, or protected review substance.
- Public-safety transforms whose parameters would aid reversal or re-identification.

[Back to top](#top)

---

## Candidate admission contract

A child candidate dossier must remain public-safe and pointer-based. Before admission, require:

| Field family | Minimum requirement |
|---|---|
| Candidate identity | Stable candidate ID, version, owner, date, parent/supersession links, and status. |
| Artifact identity | Immutable artifact pointer, digest, media type, schema/contract version, and generated/observed provenance. |
| Domain scope | Geology sublane and object families in scope. |
| Claim class | Explicit occurrence/deposit/estimate/permit/production/reserve/observation/interpretation/model/aggregate/synthetic classification as applicable. |
| Source role | Origin-preserving role; aggregator or distributor is not automatically the authority role. |
| Spatial scope | Public-safe geography, CRS, horizontal datum, scale/resolution, and geometry type. |
| Vertical/depth scope | Vertical datum, elevation/depth reference, units, interval direction, and uncertainty where material. |
| Temporal scope | Source vintage, observation/sample date, map edition, model run, permit/production validity, retrieval, release, and correction time as applicable. |
| Source closure | Resolvable source records with role, rights, sensitivity, citation, cadence, and source-head state. |
| Rights | License, redistribution, attribution, proprietary restrictions, expiration, and audience obligations. |
| Sensitivity | Public-safe classification and controlled pointers for restricted subsurface/resource detail. |
| Evidence | EvidenceRefs resolving to EvidenceBundles for consequential claims. |
| Validation | Schema, geometry, units, datum, claim-class, source-role, evidence, rights, sensitivity, catalog, and no-leak outcomes. |
| Interpretation | RealityBoundaryNote or equivalent for reconstruction-heavy, interpolated, modeled, or synthetic carriers. |
| Review | Required domain, data, evidence, rights, sensitivity, policy, release, and independent-review references. |
| Correction | Known invalidation consumers, correction route, and stale-state behavior. |
| Rollback | Prior safe target or explicit no-prior-state handling with a tested rollback plan. |
| Proposed target | Intended manifest and public-carrier families without implying approval. |

Missing required context produces a hold, denial, restriction, abstention, or error—not an inferred value.

[Back to top](#top)

---

## Geology identity, source-role, and claim-class anti-collapse

Geology candidates must preserve the meaning and authority of each claim family.

| Candidate content | Must remain distinct from |
|---|---|
| `GeologicUnit`, `Lithology`, `StratigraphicInterval`, `GeologicAge` | Individual sample observation, resource estimate, or engineering property unless separately supported |
| `StructureFeature` or `FaultStructure` | Active hazard determination or engineering-fault certification |
| `BoreholeReference` | Well ownership, water-right authority, complete well log, or public exact private-well record |
| `WellLogReference` | The restricted source log itself or an unrestricted redistribution right |
| `CoreSampleReference` / `GeochemistrySampleReference` | Formation-wide truth or resource certification |
| `GeophysicalObservation` | Direct lithologic observation, deposit confirmation, or reserve proof |
| `MineralOccurrence` | `ResourceDeposit`, `ResourceEstimate`, production, or reserve |
| `ResourceDeposit` | Economic viability, permit approval, production, or reserve |
| `ResourceEstimate` | Reserve, guarantee, investment conclusion, or extraction recommendation |
| Permit/administrative record | Observed production, compliance conclusion, or operational status without separate evidence |
| Production record | Remaining resource, reserve, ownership, or future production |
| `ExtractionSite` | Legal access, mineral ownership, engineering safety, or investment suitability |
| `ReclamationRecord` | Complete environmental performance or current site safety |
| `CrossSection`, 3D scene, interpolation, reconstruction | Direct observation or complete subsurface truth |
| Aggregate surface | Site-specific record or exact location |
| Model or AI summary | EvidenceBundle, policy decision, review, release authority, or observed fact |

### Required anti-collapse rules

1. **Occurrence is not deposit.**
2. **Deposit is not estimate.**
3. **Estimate is not reserve.**
4. **Permit is not production.**
5. **Production is not remaining resource.**
6. **Administrative status is not observed physical truth.**
7. **Model, interpolation, and interpretation are not observation.**
8. **Aggregate context is not per-place truth.**
9. **Source access path is not source authority.**
10. **Released map styling is not evidence or certification.**

Where a source uses a formal resource-classification scheme, record the scheme, edition, class, qualifiers, reviewer, and limitations. Do not silently translate a class into “reserve” or another stronger term.

[Back to top](#top)

---

## Subsurface sensitivity, rights, and safe representation

Geology has no blanket permission to expose exact subsurface or resource detail. Current repository doctrine applies the most restrictive relevant route and fails closed when no ratified geology-specific row resolves the case.

### Default public posture

| Concern | Default candidate outcome |
|---|---|
| Exact borehole, core, private-well, well-log, or geochemistry sample location | `DENY` exact public exposure or `HOLD_FOR_SENSITIVITY` |
| Restricted or proprietary well-log/source content | `HOLD_FOR_RIGHTS` or `DENY` redistribution |
| Operator, permit, parcel, mineral-interest, well, or ownership joins | `RESTRICTED_REVIEW`, `ABSTAIN`, or `DENY` |
| Extraction-targetable mineral/resource detail | `RESTRICTED_REVIEW`; generalize, aggregate, withhold, or deny |
| Public unit/lithology/age polygon | Potentially public after standard gates, source/version labeling, and release authority |
| Mineral occurrence/resource estimate | Aggregate may be public; detail requires rights, sensitivity, claim-class, evidence, and review closure |
| Interpretation-heavy cross-section or 3D surface | Public only with uncertainty, source role, scale, and RealityBoundaryNote support |
| Infrastructure-sensitive subsurface context | Apply the stricter infrastructure/public-safety posture and withhold details that increase harm risk |

### No-leak rule

The public candidate dossier must not include:

- exact restricted geometry;
- source-native restricted identifiers;
- raw depth/location pairings that recreate a sensitive point;
- private-well, operator, parcel, ownership, or access-route detail;
- proprietary log content;
- unreviewed extraction-targetable detail;
- transform parameters, seeds, offsets, thresholds, or masks that enable reversal;
- filenames, screenshots, previews, logs, examples, or hashes that indirectly reveal restricted content.

Public-safe transformations require named/versioned policy and receipt references, reviewer state, input/output digests, and rollback support. The public dossier records only the safe transform family and governed pointers—not operational parameters or the restricted original.

[Back to top](#top)

---

## Interpretation, model, and reality boundary

Geology is interpretation-heavy. Candidates must distinguish evidence from derived representation.

A `RealityBoundaryNote` or accepted equivalent is required when a carrier includes material interpretation, interpolation, reconstruction, or synthesis such as:

- cross-sections assembled from sparse control points;
- 3D stratigraphic or structural scenes;
- interpolated surfaces or volumes;
- geophysical inversion results;
- modeled mineral/resource potential;
- inferred contacts, faults, thicknesses, or depths;
- synthetic terrain/subsurface visualizations;
- AI-generated explanations or summaries.

The note should identify, at a public-safe level:

- directly observed support;
- interpreted or modeled components;
- source roles and vintages;
- method/version or model-run reference;
- spatial/vertical scale and uncertainty;
- known gaps and non-claims;
- evidence and validation pointers;
- correction and supersession behavior; and
- the prohibition against treating the representation as engineering, reserve, legal, investment, extraction, or safety certification.

A visually convincing scene, cross-section, map, graph, or rendered surface does not strengthen the underlying evidence.

[Back to top](#top)

---

## Time, vintage, scale, and stale state

A Geology candidate must preserve material time and scale distinctions.

### Time fields

- source publication or map-edition date;
- source-head/version date;
- observation, sample, borehole, core, or survey date;
- permit effective/expiration date;
- production reporting period;
- model or interpolation run time;
- retrieval/admission time;
- processing and validation time;
- candidate assembly and review time;
- release time;
- correction, supersession, withdrawal, or rollback time.

### Scale and reference fields

- map scale or resolution;
- horizontal CRS and datum;
- vertical datum and depth/elevation reference;
- units and interval direction;
- geometry precision and uncertainty;
- aggregation scope;
- interpolation support/control density where public-safe;
- source coverage and known gaps.

### Stale-state triggers

Mark or hold a candidate as `STALE` when:

- a source map edition, database release, log, permit, production period, or source-head version is superseded;
- rights or redistribution terms change;
- a classification scheme or vocabulary version changes;
- a model or interpolation method/version is superseded;
- a correction invalidates supporting evidence;
- a ReviewRecord ages out;
- a schema, contract, policy, or release profile changes materially;
- a source role or claim class is corrected; or
- a public carrier no longer matches its manifest or rollback target.

Stale does not mean false, and current does not mean correct. Stale state is a visible release/review condition that requires re-evaluation.

[Back to top](#top)

---

## Geology release gates

A candidate may advance to `APPROVED_FOR_MANIFEST` only when every applicable gate closes.

| Gate | Required evidence | Failure outcome |
|---|---|---|
| Candidate identity | Stable ID, version, immutable artifact digest, lineage | `HOLD_FOR_ARTIFACT` |
| Source admission | SourceDescriptor/source-head closure, role, rights, cadence, citation | `HOLD_FOR_SOURCE_ADMISSION` |
| Object identity | Accepted object family, stable identity, vocabulary/version | `HOLD_FOR_VALIDATION` |
| Claim class | Occurrence/deposit/estimate/permit/production/reserve/model/interpretation separation | `HOLD_FOR_CLAIM_CLASS` |
| Rights | Redistribution, attribution, proprietary, audience, and expiration obligations | `HOLD_FOR_RIGHTS` |
| Sensitivity | Public-safe geometry and controlled restricted pointers | `HOLD_FOR_SENSITIVITY` |
| Geometry/reference | CRS, datum, depth/elevation reference, units, validity, scale, uncertainty | `HOLD_FOR_VALIDATION` |
| Evidence closure | Consequential claims resolve to EvidenceBundles | `HOLD_FOR_EVIDENCE` |
| Reality boundary | Interpretation/model/synthetic components visibly bounded | `HOLD_FOR_REALITY_BOUNDARY` |
| Catalog closure | Domain/STAC/DCAT/PROV/triplet projections agree where applicable | `HOLD_FOR_VALIDATION` |
| Policy | Explicit finite decision and obligations | `HOLD_FOR_POLICY` |
| Review | Required reviewers and separation of duties satisfied | `HOLD_FOR_REVIEW` |
| Time/stale state | Vintages, validity, current/superseded state resolved | `HOLD_FOR_STALE_STATE` |
| Public no-leak | Map, tile, API, export, search, graph, logs, screenshots, and AI surfaces do not expose restricted detail | `HOLD_FOR_SENSITIVITY` |
| Correction | Correction route and invalidation consumers identified | `HOLD_FOR_CORRECTION_PATH` |
| Rollback | Prior safe target and rollback drill/support resolved | `HOLD_FOR_ROLLBACK` |
| Release topology | PromotionDecision, ReleaseManifest, carrier, correction, withdrawal, and rollback homes resolve | `HOLD_FOR_RELEASE_TOPOLOGY` |

### Domain-specific negative cases

Validation should include at least:

- occurrence represented as deposit;
- estimate represented as reserve;
- permit represented as production;
- aggregate represented as exact/site-specific;
- model or interpolation represented as observation;
- cross-section or 3D scene missing a reality boundary;
- exact restricted borehole/private-well/sample geometry on a public surface;
- proprietary or rights-unclear log redistributed;
- operator/parcel/mineral-interest join exposed publicly;
- source-role upgrade through aggregation, styling, or AI prose;
- missing EvidenceBundle;
- missing CRS/datum/vertical reference or unit;
- stale map/source/model/permit/production state represented as current;
- missing correction path or rollback target;
- public client reading candidate/internal stores directly.

[Back to top](#top)

---

## Required dossier structure

A child dossier should use a public-safe structure similar to the following. The template is **PROPOSED** and must be reconciled with accepted schemas and release records before use.

```markdown
# <geology-candidate-id> — candidate dossier

## Status
PROPOSED / ASSEMBLING / RESTRICTED_REVIEW / READY_FOR_REVIEW /
BLOCKED / REPAIR_REQUIRED / STALE / DEFERRED /
APPROVED_FOR_MANIFEST / PROMOTED / SUPERSEDED / WITHDRAWN

## Candidate identity
- Candidate ID:
- Version:
- Owner:
- Parent or supersedes:
- Assembly date:
- Intended audience:

## Candidate artifact
- Immutable artifact pointer:
- Digest:
- Media type:
- Schema / contract version:
- Generated / observed / modeled / interpreted posture:

## Domain and claim scope
- Geology sublane:
- Object families:
- Claim classes:
- Source roles:
- Public-safe geography:
- CRS / horizontal datum:
- Vertical datum / depth reference:
- Scale / resolution:
- Units:
- Time / vintage scope:

## Source and rights closure
- Source records:
- Source-head refs:
- Rights / redistribution:
- Attribution:
- Proprietary or restricted obligations:
- Remaining blockers:

## Sensitivity and public-safe representation
- Sensitivity record refs:
- Public-safe transform family:
- Restricted original pointer: <controlled ref only>
- No-leak validation:
- Reviewer obligations:
- Remaining blockers:

## Evidence and interpretation boundary
- EvidenceRefs / EvidenceBundles:
- Validation reports:
- RealityBoundaryNote:
- Model / method / interpretation refs:
- Uncertainty and non-claims:
- Remaining blockers:

## Review and decision readiness
- Domain review:
- Data review:
- Evidence review:
- Rights / sensitivity review:
- Policy decision:
- Independent release review:
- PromotionDecision readiness:
- ReleaseManifest readiness:

## Correction and rollback
- Correction route:
- Invalidation consumers:
- Withdrawal / supersession route:
- Prior safe rollback target:
- Rollback drill / validation:
- Remaining blockers:

## Recommendation
APPROVE_FOR_MANIFEST / BLOCK / DEFER / REPAIR / WITHDRAW

## Reason
<public-safe evidence-grounded reason>
```

Do not put restricted review substance, exact geometry, proprietary content, transform parameters, mineral/property-rights details, engineering conclusions, or operational recommendations in the public dossier.

[Back to top](#top)

---

## Validation, proof, and fixture posture

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| [`tests/domains/geology/`](../../../tests/domains/geology/README.md) | Grounded README plus five direct `.py` files inspected as one-line `PROPOSED` placeholders | Intended proof matrix exists; executable coverage is not established |
| [`fixtures/domains/geology/`](../../../fixtures/domains/geology/README.md) | Required by workflow and documentation | Concrete public-safe fixture inventory and maturity remain **NEEDS VERIFICATION** |
| [`tools/validators/geology/`](../../../tools/validators/geology/README.md) | README-backed lane | Accepted executable validator command is not established |
| [`tools/validators/domains/geology/`](../../../tools/validators/domains/geology/README.md) | README-backed lane | Accepted executable validator command is not established |
| [`data/proofs/geology/`](../../../data/proofs/geology/README.md) | Draft proof guide | Concrete proof inventory, producer, access controls, and release linkage remain unverified |
| [`policy/domains/geology/`](../../../policy/domains/geology/README.md) | Greenfield scaffold | Executable policy enforcement is not established |
| [`data/registry/sensitivity/geology/`](../../../data/registry/sensitivity/geology/README.md) | Grounded registry guidance | Parent contract and concrete record inventory remain unresolved |
| Domain schemas/contracts | Multiple files and indexes surfaced | Presence does not prove accepted runtime binding, semantic closure, or release use |
| Published lane | Grounded carrier guidance | Emitted release-linked artifacts remain unverified |

### Minimum deterministic fixture families

- public unit/lithology polygon;
- exact restricted borehole/private-well/sample record;
- generalized public-safe subsurface reference;
- occurrence, deposit, estimate, permit, production, and reserve anti-collapse cases;
- model/interpretation versus observation cases;
- aggregate versus site-specific cases;
- rights-cleared and rights-unclear source cases;
- source-role upgrade attempt;
- missing/invalid EvidenceBundle;
- CRS/datum/vertical-reference and unit failures;
- stale source/map/model/permit/production cases;
- cross-section/3D scene with and without reality-boundary support;
- operator/parcel/mineral-interest join denial;
- public API/map/tile/export/search/graph/AI no-leak cases;
- correction, withdrawal, supersession, and rollback cases;
- no-network guard.

Fixtures must be synthetic or already public-safe and must not include real restricted subsurface, proprietary, ownership, extraction-targetable, infrastructure-sensitive, or access detail.

[Back to top](#top)

---

## Automation posture

### `domain-geology`

The current workflow is a read-only maturity detector and explicit hold. It checks required boundaries, looks for executable tests/validators/proof/candidate material, and requires the exact sentence:

```text
A candidate is not a release.
```

Its three jobs are intended to hold until accepted implementation exists:

- `validate-geology`
- `build-proof-geology`
- `publish-dry-run-geology`

A green hold means only that the documented hold conditions remain true. A detector failure means repository maturity changed or a detector assumption was triggered; it does not mean the README created or validated Geology truth.

### General `release-dry-run`

The general workflow currently contains TODO-only echo jobs for candidate assembly, promotion-gate checking, and rollback-card presence. Green status from those jobs is not release proof.

### Graduation rule

Graduate a hold only through a separately scoped, evidence-backed change that:

1. identifies the accepted command and owning implementation;
2. binds contracts, schemas, policy, fixtures, tests, proofs, receipts, and release records;
3. preserves no-network and no-leak defaults;
4. validates claim-class, rights, sensitivity, reality-boundary, and rollback behavior;
5. updates documentation; and
6. records a reversible rollout.

[Back to top](#top)

---

## Review and release handoff

### Required review roles

| Review concern | Required responsibility |
|---|---|
| Geology scope, object identity, claim class, interpretation | Geology domain steward |
| Artifact integrity, lifecycle, schema/contract linkage | Data steward |
| EvidenceBundle and citation closure | Evidence/proof steward |
| Source role, source-head state, rights, attribution | Source and rights steward |
| Subsurface, private-well, resource, infrastructure, operator/parcel sensitivity | Sensitivity/policy reviewer |
| Reality boundary and model/interpretation posture | Geology reviewer with method expertise |
| Release topology, correction, withdrawal, rollback | Release steward |
| Documentation truth and public-safe wording | Docs steward |
| Material approval | Independent reviewer distinct from the author where required |

CODEOWNERS routes GitHub review. It does not prove that any of these responsibilities were assigned, exercised, or approved.

### Handoff order

```text
candidate dossier
  -> domain/data/evidence/rights/sensitivity/policy review
  -> validation and proof closure
  -> independent review
  -> PromotionDecision
  -> ReleaseManifest
  -> released public-safe carrier
  -> correction / withdrawal / supersession / rollback support
```

Do not collapse review recommendation, PromotionDecision, ReleaseManifest, and publication into one unreviewed action.

[Back to top](#top)

---

## Correction, withdrawal, and rollback

A promoted Geology artifact must remain correctable and reversible.

### Correction triggers

- source, map edition, log, sample, permit, production period, or model supersession;
- source-role or claim-class error;
- occurrence/deposit/estimate/reserve collapse;
- rights or redistribution change;
- exact or reverse-engineerable sensitive detail exposure;
- private-well, operator, parcel, mineral-interest, proprietary, or infrastructure-sensitive leak;
- CRS, datum, vertical reference, depth, unit, scale, or geometry error;
- reality-boundary or uncertainty omission;
- EvidenceBundle invalidation;
- catalog/manifest digest drift;
- public carrier divergence from manifest;
- AI/map/export/search/graph presentation overclaim;
- missing correction consumer or rollback target.

### Required response

1. stop or restrict affected public carriers;
2. preserve the prior artifact and decision lineage;
3. issue a CorrectionNotice or WithdrawalNotice as appropriate;
4. invalidate dependent map, tile, API, export, search, graph, cache, and AI carriers;
5. restore a prior safe target where rollback is required;
6. re-run public-safe validation and no-leak checks;
7. record reviewer and receipt references; and
8. supersede rather than silently overwrite.

Rollback is a governed transition. It must not disclose the restricted original or convert an invalidated estimate, model, or interpretation into stronger truth.

[Back to top](#top)

---

## Public API, map, export, and AI boundary

Public clients and normal UI surfaces use governed APIs and released manifests. They do not read candidate, source-registry, sensitivity-registry, processed, proof, receipt, or internal canonical stores directly.

Public-facing Geology surfaces must:

- expose only fields permitted by the released manifest and policy outcome;
- preserve source role, claim class, scale, uncertainty, time/vintage, rights, and correction state;
- distinguish observed, administrative, regulatory, aggregate, modeled, interpreted, synthetic, and generated content;
- show reality-boundary labels for interpretation-heavy carriers;
- avoid exact restricted subsurface/resource/infrastructure geometry;
- avoid private-well, operator/parcel, mineral-interest, proprietary, or access detail;
- avoid reserve, engineering, legal, investment, extraction, safety, or regulatory overclaim;
- resolve consequential claims to released evidence or return a finite non-answer;
- propagate correction, stale, superseded, withdrawn, and rollback state; and
- keep map layers, tiles, cross-sections, 3D scenes, graphs, screenshots, and generated text downstream of evidence and release authority.

AI may summarize released evidence within policy. It may not invent citations, promote claim class, infer reserve status, recommend extraction or investment, certify engineering suitability, expose restricted geometry, or substitute fluent prose for EvidenceBundles, review, policy, or release state.

[Back to top](#top)

---

## Maintenance and definition of done

### Maintenance checklist

Before changing this lane:

- [ ] Recheck current `main` and target blob.
- [ ] Search for overlapping candidate dossiers and pull requests.
- [ ] Keep candidate metadata public-safe and pointer-based.
- [ ] Preserve the workflow compatibility sentence while the hold relies on it.
- [ ] Reconcile new paths with Directory Rules and current repository evidence.
- [ ] Update candidate inventory from governed records, not prose inference.
- [ ] Record unresolved path/vocabulary conflicts explicitly.
- [ ] Recheck sensitive, proprietary, rights, engineering, legal, investment, extraction, and infrastructure exposure.
- [ ] Validate links, headings, anchors, fences, whitespace, and final newline.
- [ ] Record provenance, human-review state, and rollback.

### Definition of done

This lane becomes implementation-backed when:

- a deterministic candidate index is generated from accepted machine-readable records;
- every listed candidate has immutable identity, artifact, digest, lineage, and state;
- source, evidence, rights, sensitivity, claim-class, validation, reality-boundary, review, correction, and rollback references resolve;
- accepted schemas/contracts/policies are bound to runtime validators;
- deterministic public-safe fixtures and no-network/no-leak tests run in CI;
- the Geology proof producer and manifest path are accepted and verified;
- PromotionDecision and ReleaseManifest handoff is operational;
- emitted public carriers are verified against manifests;
- correction, cache invalidation, withdrawal, supersession, and rollback drills are tested; and
- independent review and branch-protection requirements are confirmed.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| This target README at `9dd466557836…` | `CONFIRMED` | Existing generic candidate-lane guidance | Candidate or release existence |
| Bounded search for `release/candidates/geology` | `CONFIRMED bounded result` | Parent README surfaced; no child dossier established | Exhaustive repository/history/external inventory |
| [`docs/domains/geology/RELEASE_INDEX.md`](../../../docs/domains/geology/RELEASE_INDEX.md) | `CONFIRMED draft index` | Release surfaces, gates, placeholder register, sensitivity and anti-collapse guidance | Verified release instance |
| [`data/registry/sources/geology/`](../../../data/registry/sources/geology/README.md) | `CONFIRMED grounded README` | Source-role, rights, sensitivity, stale-state, and topology guidance | Concrete admitted-source closure |
| [`data/registry/sensitivity/geology/`](../../../data/registry/sensitivity/geology/README.md) | `CONFIRMED grounded README` | Exact-subsurface, private-well, resource, operator/parcel, and reality-boundary sensitivity posture | Executable policy or concrete registry instances |
| [`data/proofs/geology/`](../../../data/proofs/geology/README.md) | `CONFIRMED file / PROPOSED proof lane` | Evidence, anti-collapse, rights, sensitivity, correction, and rollback support expectations | Concrete proof inventory or producer |
| [`tests/domains/geology/`](../../../tests/domains/geology/README.md) plus five direct modules | `CONFIRMED documentation / placeholders` | Intended deterministic proof matrix | Executable suite or passing results |
| [`policy/domains/geology/`](../../../policy/domains/geology/README.md) | `CONFIRMED scaffold` | Intended policy home | Enforced policy behavior |
| [`data/published/geology/`](../../../data/published/geology/README.md) | `CONFIRMED carrier guidance` | Release-gated public-safe carrier boundary | Emitted release-linked instance |
| [`domain-geology`](../../../.github/workflows/domain-geology.yml) | `CONFIRMED definition` | Read-only maturity checks and explicit holds | Geologic validation, proof, reserve certification, or release |
| General release dry run | `CONFIRMED TODO scaffold` | Workflow presence | Candidate assembly, promotion enforcement, rollback verification, or release |
| CODEOWNERS | `CONFIRMED routing` | Current GitHub review route | Stewardship, independent approval, or branch-protection proof |

No external web research is required for this repository-state documentation update.

[Back to top](#top)

---

## Open verification

- [ ] Confirm exhaustive child inventory under `release/candidates/geology/`.
- [ ] Confirm candidate naming, identity, versioning, artifact-manifest, and digest conventions.
- [ ] Confirm canonical Geology object-family names and case conventions.
- [ ] Confirm accepted claim-class vocabulary and any external classification schemes.
- [ ] Confirm source-role vocabulary and source-origin handling.
- [ ] Resolve subtype-first versus domain-first source registry topology.
- [ ] Confirm the sensitivity-registry parent contract and concrete record schema.
- [ ] Ratify Geology-specific sensitivity defaults or retain the documented most-restrictive fallback.
- [ ] Confirm admitted sources, rights, cadence, source-head identity, and source vintages.
- [ ] Confirm EvidenceRef-to-EvidenceBundle and claim-support contracts.
- [ ] Replace Geology policy scaffolds with reviewed executable policy and safe reason codes.
- [ ] Confirm public-safe transform profiles and receipt schemas without exposing operational parameters.
- [ ] Confirm accepted CRS, datum, vertical-reference, depth, unit, scale, and uncertainty contracts.
- [ ] Confirm reality-boundary contract for cross-sections, 3D scenes, inversions, interpolations, and models.
- [ ] Confirm public-safe fixture inventory and no-network/no-leak enforcement.
- [ ] Confirm accepted validator ownership and distinguish placeholder files from mature implementations.
- [ ] Confirm candidate-to-review, PromotionDecision, and ReleaseManifest handoff.
- [ ] Resolve manifest, correction, withdrawal, rollback-card, and lifecycle rollback topology.
- [ ] Confirm correction consumers, cache invalidation, withdrawal/supersession behavior, and rollback drills.
- [ ] Confirm public API/map/tile/export/search/graph/AI no-leak tests.
- [ ] Confirm branch protection, required checks, immutable action pinning, and independent reviewer assignments.
- [ ] Confirm candidate inventory can be generated from machine-readable records without making generated output sovereign truth.

[Back to top](#top)

---

## Changelog

### v2 — 2026-07-18

- Replaced generic Geology candidate guidance with a repository-grounded, claim-class-aware candidate index and pre-publication review contract.
- Recorded that no child candidate dossier or active candidate is established by bounded inspection.
- Preserved the exact workflow compatibility sentence and `publication-not_yet` marker.
- Added finite states and holds, admission and identity rules, source-role and claim-class anti-collapse, subsurface sensitivity and rights controls, reality-boundary requirements, time/vintage/scale discipline, release gates, a public-safe dossier contract, validation and automation posture, review handoff, correction and rollback discipline, public-surface boundaries, evidence ledger, definition of done, and open verification.
- Added `CONTRACT_VERSION = "3.0.0"` and immutable evidence snapshot metadata.

### v1 — 2026-07-03

- Replaced the earlier greenfield stub with initial Geology candidate-lane guidance.

[Back to top](#top)

---

## Rollback for this README

This revision changes documentation only.

Before merge, close the pull request or delete the scoped branch.

After merge, revert the generated-receipt commit and README commit in reverse order and restore the prior README blob:

```text
9dd4665578364dfb0862b6666cbff411151f8ede
```

No Geology candidate, source, geologic unit, borehole, well log, core, sample, mineral occurrence, resource estimate, extraction site, private-well record, mineral/property-rights record, evidence, policy, review, release, public carrier, correction, withdrawal, supersession, or rollback state requires restoration.

[Back to top](#top)
