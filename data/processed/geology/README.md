<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-processed-geology-readme
title: data/processed/geology/README.md — Geology Processed Data README
version: v0.2.0
type: README; data-lifecycle-domain-lane; processed-stage-guide; geology-domain-root; natural-resources-lane-index; authority-boundary
status: repository-grounded draft; PROPOSED implementation; payload/runtime enforcement unverified
owners: NEEDS VERIFICATION — Geology steward · Natural-resources steward · Subsurface data steward · Sensitivity reviewer · Rights steward · Data steward · Pipeline steward · Evidence steward · Policy steward · Release steward · Docs steward
updated: 2026-07-25
supersedes: prior README at the same path; no payload, lifecycle, release, runtime, or publication state
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: restricted-review; no-direct-public-path; anti-collapse; sensitivity-aware; release-gated
current_path: data/processed/geology/README.md
truth_posture: >
  CONFIRMED exact target path, prior blob, parent data/processed contract, geology domain doctrine,
  and existing geology processed-stage boundary / PROPOSED lane inventory, local validation rules,
  and downstream handoffs / UNKNOWN recursive payload inventory, active writers and consumers,
  enforcement, runtime behavior, public serving, and release state / NEEDS VERIFICATION owners,
  accepted ADRs, schemas, fixtures, validators, receipts, evidence closure, policy decisions,
  correction propagation, cache invalidation, and rollback drills
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  prior_blob: 8de9b178f9a8f2be9d37b28540a955e54a095775
  parent_processed_blob: 35e393a12822a86e5fa8a5edce7b581be75b523f
  geology_domain_blob: 24dea0085e25e41a2cf53f2fe7904b306436b3a5
  method: exact target, parent processed README, and geology domain README inspection; no recursive payload or runtime inspection
notes:
  - "The first twelve H2 sections follow the normalized data/processed parent contract and Directory Rules section 15 pattern."
  - "This is the canonical PROCESSED responsibility lane for geology data, not semantic, schema, policy, proof, catalog, release, or public-serving authority."
  - "Anti-collapse is mandatory: Occurrence, Deposit, Estimate, Permit, Production, Reserve, and Reclamation remain distinct claim types."
  - "Exact borehole, sample, sensitive resource, private-well, operator/parcel, and subsurface-sensitive locations remain deny-by-default for ordinary public exposure."
  - "Rollback target for v0.2.0 is prior blob SHA 8de9b178f9a8f2be9d37b28540a955e54a095775."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/processed/geology/` — Normalized Geology Candidate Products

> **One-line purpose.** Own normalized, versioned, validation-supported geology and natural-resources products that have passed applicable WORK or resolved-QUARANTINE checks but have not thereby become cataloged, proved, released, or public.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: PROCESSED](https://img.shields.io/badge/authority-PROCESSED-0969da?style=flat-square)](#authority-level)
[![Posture: anti-collapse](https://img.shields.io/badge/posture-anti--collapse-b42318?style=flat-square)](#geology-specific-controls)
[![Exposure: deny by default](https://img.shields.io/badge/exposure-deny%20by%20default-b42318?style=flat-square)](#review-burden)
[![Truth: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](#validation)

> [!IMPORTANT]
> Path placement, normalization, a generated derivative, a successful check, a pull request, or a merge does not create factual truth, EvidenceBundle closure, rights clearance, policy permission, release approval, or KFM publication.

> [!WARNING]
> Exact borehole, private-well, sample, sensitive-resource, operator/parcel, and subsurface-sensitive geometry must not enter ordinary public paths unless an explicit policy decision and recorded transform make the exposure safe.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Geology controls](#geology-specific-controls) · [Children](#current-bounded-child-lane-index) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

Own normalized, source-traced, role-typed, sensitivity-aware Geology and Natural Resources products that have passed their applicable processing gates while remaining upstream of catalog, triplet, proof closure, release, and public access.

This lane may hold processed products for geologic units, surficial units, lithology, stratigraphy, geologic age, structures, subsurface observations, borehole and well-log references, cores and samples, geophysics, geochemistry, mineral occurrences, resource deposits and estimates, extraction context, reclamation, cross-sections, and hydrostratigraphic context.

This README does not create object meaning, machine shape, admissibility policy, evidence proof, catalog admission, release approval, a public map layer, mineral-rights evidence, property-rights evidence, extraction advice, engineering certification, hazard warning, or life-safety guidance.

## Authority level

**Canonical; PROCESSED responsibility.**

`data/processed/geology/` owns normalized candidate products and processed-local explanatory sidecars. It does not own:

- semantic meaning, which belongs in `contracts/domains/geology/`;
- machine shape, which belongs in `schemas/contracts/v1/domains/geology/`;
- policy or sensitivity decisions, which belong in `policy/`;
- source identity or rights authority, which belongs in `data/registry/`;
- proofs and receipts, which belong in `data/proofs/` and `data/receipts/`;
- catalog or graph projection, which belongs in `data/catalog/` and `data/triplets/`;
- release decisions and published bytes, which belong in `release/` and `data/published/`;
- public serving, which must use governed interfaces rather than this internal lane.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/processed/geology/README.md` |
| Version | `v0.2.0` |
| Prior blob | `8de9b178f9a8f2be9d37b28540a955e54a095775` |
| Parent contract | `data/processed/README.md` at blob `35e393a12822a86e5fa8a5edce7b581be75b523f` |
| Domain evidence | `docs/domains/geology/README.md` at blob `24dea0085e25e41a2cf53f2fe7904b306436b3a5` |
| Recursive payload inventory | `UNKNOWN` |
| Active writers and consumers | `UNKNOWN` |
| Public readiness | `DENY BY DEFAULT` |
| Schema, validator, fixture, CI, policy, and release enforcement | `NEEDS VERIFICATION` |

## What belongs here

- normalized geology-domain objects, tables, vectors, rasters, crosswalks, interval models, reference surfaces, and versioned datasets;
- processed geologic-unit and surficial-unit products with source, interpretation, geometry, and uncertainty lineage;
- processed lithology, stratigraphy, age, contact, fault, fold, structure, and geomorphology products;
- processed borehole, well-log, core, sample, geophysical, and geochemical references with rights and sensitivity posture preserved;
- role-typed mineral occurrence, deposit, estimate, permit, production, extraction-site, reserve, and reclamation candidates that remain explicitly distinct;
- processed cross-sections, hydrostratigraphic units, subsurface interpretations, uncertainty surfaces, and public-candidate generalized derivatives;
- processed-local manifests, digests, validation references, limitations, uncertainty notes, interpretation-version references, and derivation sidecars;
- products ready for governed catalog, triplet, proof, or release-candidate assembly.

Local README, inventory, digest, migration, correction, and disposition sidecars may explain this boundary without creating parallel authority.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| Source-native maps, geodatabases, LAS files, logs, images, exports, original exact geometry, or immutable captures | `data/raw/geology/` |
| Mutable transforms, notebooks, geometry repair, stratigraphic matching, model experiments, redaction trials, and scratch outputs | `data/work/geology/` |
| Rights-unclear, role-unclear, disputed, malformed, unsafe, or harmful-precision material | `data/quarantine/geology/` |
| Catalog records, STAC/DCAT/PROV projections, and graph triplets | `data/catalog/` and `data/triplets/` |
| EvidenceBundle records, proofs, receipts, source descriptors, release decisions, and rollback cards | `data/proofs/`, `data/receipts/`, `data/registry/`, and `release/` |
| Released public-safe bytes and normal public-client sources | `data/published/` and governed APIs |
| Contracts, schemas, policy rules, validators, tests, fixtures, pipelines, application code, and UI code | Their canonical responsibility roots |
| Mineral-rights, parcel-title, ownership, lease, engineering-safety, hazard, or legal conclusions | Governed evidence and owning-domain paths; otherwise abstain |
| Maps, cross-sections, 3D scenes, tiles, graphs, indexes, or AI summaries presented as sovereign truth | Resolve governed evidence and release state or abstain |

## Inputs

Governed WORK products or reviewed QUARANTINE exits with sufficient support for the artifact's significance and sensitivity.

As applicable, an input should resolve:

- stable identity, version, and digest;
- source identity, source role, rights, license, and retrieval lineage;
- object family and claim type;
- spatial and temporal scope;
- coordinate reference system, geometry validity, and precision posture;
- interpretation author, method, date, version, and uncertainty;
- contract and schema references;
- processing code/spec/run and validation references;
- sensitivity and public-safe transform state;
- correction, predecessor/successor, and rollback references.

A resolved QUARANTINE exit must retain the original hold reason, review decision, remediation evidence, and disposition record. Promotion is a governed state transition, not a silent file move.

## Outputs

Outputs are normalized candidate products for:

- geology-domain catalog and STAC/DCAT/PROV projection;
- triplet or graph projection that preserves claim type and sensitivity;
- EvidenceBundle or proof assembly;
- release-candidate review;
- restricted or public-safe derivative generation after explicit policy and release decisions.

PROCESSED remains non-public by default. Public clients, MapLibre viewers, Focus Mode, and AI answer surfaces must not read this lane directly as a normal data service.

## Validation

Validate at least the following where applicable:

1. **Placement:** correct lifecycle and geology responsibility path.
2. **Identity:** stable ID, version, digest, predecessor/successor, and interpretation version.
3. **Source:** SourceDescriptor or registry reference, source role, rights, retrieval, and citation support.
4. **Object family:** explicit distinction among unit, observation, occurrence, deposit, estimate, permit, production, reserve, extraction, and reclamation claims.
5. **Geometry:** CRS, topology, dimensionality, precision, generalization, and harmful-location exposure.
6. **Space and time:** geographic support, depth/elevation datum, validity period, observation time, interpretation time, and update time.
7. **Subsurface lineage:** borehole, well-log, core, sample, interval, geophysical, and cross-section references remain traceable.
8. **Uncertainty:** confidence, method limitations, interpolation, model assumptions, boundary confidence, and disputed interpretations remain visible.
9. **Contract/schema:** declared contract and schema references match the product; permissive schema success is not proof of semantic validity.
10. **Receipts and evidence:** run, transform, redaction/generalization, validation, policy, correction, and evidence references resolve where required.
11. **Sensitivity and rights:** exact restricted locations and rights-controlled data fail closed.
12. **Downstream parity:** catalog, triplet, proof, and release-candidate identities do not silently diverge.
13. **Correction and rollback:** supersession, withdrawal, correction propagation, cache invalidation, and rollback dependencies are recorded.

No complete geology-lane validator or recursive payload review was verified in this task. A passing check proves only that check's declared scope.

## Review burden

Accountable ownership remains **NEEDS VERIFICATION**. Review should include, as applicable:

- geology and natural-resources stewardship;
- subsurface, borehole, well-log, sample, and geophysics expertise;
- source rights and license review;
- sensitivity and harmful-precision review;
- evidence and validation review;
- policy and release review;
- owning-domain review for Hydrology, Hazards, Soil, Archaeology, or People/Land joins.

Changes involving exact subsurface geometry, private-well information, resource-location sensitivity, operator/parcel joins, rights-controlled logs, public serving, release, correction, or rollback require specialist and independent review. CODEOWNERS routing is not approval evidence.

## Related folders

- Parent: [`data/processed/`](../README.md)
- Lifecycle: [`raw/geology/`](../../raw/geology/) · [`work/geology/`](../../work/geology/) · [`quarantine/geology/`](../../quarantine/geology/) · [`catalog/domain/geology/`](../../catalog/domain/geology/) · [`published/`](../../published/)
- Trust support: [`proofs/`](../../proofs/) · [`receipts/`](../../receipts/) · [`registry/sources/geology/`](../../registry/sources/geology/)
- Authority: [`contracts/domains/geology/`](../../../contracts/domains/geology/) · [`schemas/contracts/v1/domains/geology/`](../../../schemas/contracts/v1/domains/geology/) · [`policy/domains/geology/`](../../../policy/domains/geology/) · [`release/candidates/geology/`](../../../release/candidates/geology/)
- Domain docs: [`docs/domains/geology/README.md`](../../../docs/domains/geology/README.md) · [`POLICY.md`](../../../docs/domains/geology/POLICY.md) · [`PRESERVATION_MATRIX.md`](../../../docs/domains/geology/PRESERVATION_MATRIX.md) · [`OPEN_QUESTIONS.md`](../../../docs/domains/geology/OPEN_QUESTIONS.md)
- Cross-domain context: [`soil/`](../../../docs/domains/soil/README.md) · [`hydrology/`](../../../docs/domains/hydrology/README.md) · [`hazards/`](../../../docs/domains/hazards/README.md) · [`archaeology/`](../../../docs/domains/archaeology/README.md)

## ADRs

Relevant decisions include schema-home, proof/receipt/catalog/release separation, connector-output boundaries, published aliases and rollback separation, and the rule that public clients do not read internal stores. This README accepts no proposed ADR by implication.

An accepted ADR plus migration, validation, compatibility, and rollback plan is required before:

- creating a second geology schema, contract, source, proof, receipt, policy, release, or publication home;
- changing lifecycle authority;
- promoting a compatibility lane to canonical status;
- collapsing claim types or moving sensitive data into ordinary public paths.

## Last reviewed

- **Date:** 2026-07-25
- **Evidence boundary:** exact target README, parent `data/processed/README.md`, and `docs/domains/geology/README.md`
- **Recursive payload/runtime inspection:** not performed
- **Owners, accepted ADRs, enforcement, release state, public serving, correction propagation, and rollback drills:** need verification

Re-review on changes to topology, object families, source roles, sensitivity, rights, schemas, validators, writers, consumers, catalog/triplet identity, release, public serving, correction, or rollback—or within six months.

## Geology-specific controls

### Anti-collapse matrix

| Claim type | Meaning boundary | Must not be presented as |
|---|---|---|
| `MineralOccurrence` | Documented presence or indication | Deposit, estimate, reserve, permit, production, or extraction proof |
| `ResourceDeposit` | Interpreted or characterized deposit | Estimate, reserve, permit, production, title, or economic viability |
| `ResourceEstimate` | Method- and date-bounded quantity/quality estimate | Reserve, guaranteed recoverability, production, or investment advice |
| Permit or regulatory context | Authorization or filing state | Production, ownership, safety, compliance proof, or reserve |
| Production context | Reported extraction or production activity | Reserve, remaining resource, title, permit validity, or future output |
| Reserve claim | Governed reserve statement under its source framework | Generic deposit, occurrence, or unsupported economic claim |
| Reclamation record | Reclamation plan, action, or status | Proof of complete restoration, safety, liability resolution, or release |

### Sensitivity classes

Treat these as restricted or review-required unless policy and evidence support a safer posture:

- exact borehole and private-well coordinates;
- precise sample, core, fossil, archaeological-adjacent, or sensitive-resource locations;
- rights-controlled well logs and proprietary geophysical data;
- operator, parcel, lease, title, ownership, or person-linked joins;
- detailed subsurface infrastructure, mine workings, shafts, voids, or access points;
- resource-location derivatives whose precision could enable harm, trespass, theft, or unsafe access.

Allowed public transforms may include generalization, aggregation, centroid displacement, grid or region assignment, attribute suppression, delayed release, staged access, or denial. Every transform requires a recorded reason, method, precision change, review state, and rollback target.

### Cross-domain boundaries

- **Hydrology** owns water observations, aquifer condition, wells as water-resource objects, and water-quality claims. Geology may own hydrostratigraphic context.
- **Hazards** owns event, risk, warning, and impact truth. Fault or subsurface context is not hazard prediction by itself.
- **Soil** owns pedologic units and soil interpretation. Surficial geology does not replace soil classification.
- **People/Land** owns parcel, ownership, title, lease, and living-person governance. Geology must not infer those claims from resource context.
- **Archaeology** owns archaeological sites and cultural-sensitivity decisions. Geology joins must preserve archaeological restrictions.
- **Map/3D/UI** surfaces are derived views, not canonical truth or release authority.

## Current bounded child-lane index

The target README previously listed intended child lanes. Their actual directories, payloads, validators, and consumers were not recursively verified in this pass. Treat each entry as **PROPOSED** unless separately confirmed.

| Lane | Candidate family | Boundary |
|---|---|---|
| `geologic_units/` | GeologicUnit / SurficialUnit | Unit geometry and attribution are not proof or release by themselves. |
| `lithology/` | Lithology | Material description does not prove deposit, reserve, or extraction status. |
| `stratigraphy/` | StratigraphicInterval / GeologicAge | Correlations require source, date, version, and uncertainty. |
| `structures/` | StructureFeature / FaultStructure | Geologic context does not become hazard or risk truth. |
| `boreholes/` | BoreholeReference | Exact locations are restricted or generalized by default. |
| `well_logs/` | WellLogReference | Rights-controlled logs fail closed without confirmed terms. |
| `cores_samples/` | CoreSampleReference / GeochemistrySampleReference | Exact sample locations may require restriction or generalization. |
| `geophysics/` | GeophysicalObservation | Observation and model roles remain distinct; sensitive products may be restricted. |
| `geochemistry/` | GeochemistrySampleReference | Sample chemistry is not deposit, estimate, reserve, or economic proof. |
| `minerals/` | MineralOccurrence | Occurrence is not deposit, estimate, reserve, permit, production, or extraction. |
| `resources/` | ResourceDeposit / ResourceEstimate | Deposit, estimate, reserve, and production remain separate. |
| `extraction/` | ExtractionSite / permit / production context | Permit is not production; production is not reserve or ownership. |
| `reclamation/` | ReclamationRecord | Reclamation status is not proof of complete restoration or liability closure. |
| `cross_sections/` | CrossSection / subsurface interpretation | Interpretation version, author, method, uncertainty, and evidence are required. |
| `hydrostratigraphy/` | HydrostratigraphicUnit | Geology context may support Hydrology but does not replace hydrologic observations. |
| `public_safe/` | Generalized or redacted candidates | Public-safe candidate is not publication; release remains separate. |
| `restricted/` | Controlled sensitive products | Access controls and auditability are required; existence does not authorize access. |

Omission from this table is not deletion, retirement, or reclassification. Do not create new child lanes solely from this README without checking Directory Rules, current tree evidence, contracts, schemas, policies, and ADRs.

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive subtree and payload inventory | `NEEDS VERIFICATION` | Pinned tree, payload families, LFS or external stores, owners, rights, and sensitivity |
| Active writers and consumers | `UNKNOWN` | Connectors, pipelines, tools, workflows, APIs, UIs, packages, and deployed consumers |
| Contract and schema maturity | `UNKNOWN` | Accepted contracts, schema fields, examples, versioning, compatibility, and negative cases |
| Validator, fixture, and CI enforcement | `UNKNOWN` | Deterministic tests, invalid fixtures, workflow scope, and current results |
| Source registry and rights closure | `UNKNOWN` | SourceDescriptor instances, licenses, restrictions, retrieval and correction lineage |
| Sensitivity and access enforcement | `UNKNOWN` | Policy decisions, transforms, access controls, audits, denial and redaction tests |
| Receipt, proof, catalog, and release closure | `UNKNOWN` | Emitted instances, identity agreement, independent review, release and rollback links |
| Public serving and invalidation | `UNKNOWN` | Governed routes, hosting, caches, stale/correction/withdrawal propagation, and drills |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path and document identity | Preserved |
| PROCESSED lifecycle role | Preserved and aligned to the current parent contract |
| Existing geology scope | Preserved |
| Occurrence / Deposit / Estimate / Permit / Production / Reserve / Reclamation anti-collapse rule | Preserved and expanded |
| Borehole, sample, resource, private-well, operator/parcel, and subsurface sensitivity posture | Preserved and expanded |
| Cross-domain boundaries | Preserved and clarified |
| Child-lane index | Preserved in bounded form; omission is not retirement |
| Evidence, rights, policy, release, correction, and rollback controls | Preserved and strengthened |
| Prior blob and rollback target | Recorded |
| Payload, schema, policy, source, move, deletion, migration, release, or public-state change | None |

### Change history

#### v0.2.0 — 2026-07-25

- aligned the geology lane to the current `data/processed/` parent authority contract;
- preserved and strengthened geology anti-collapse and sensitivity controls;
- added bounded validation, review, child-lane, verification, and no-loss sections;
- removed unsupported implications of implementation maturity;
- changed Markdown only.

#### v0.1 — 2026-06-25

- expanded the prior greenfield stub into a geology processed-lane guide;
- documented intended object families, lifecycle boundaries, and sensitivity posture.

[Back to top](#top)
