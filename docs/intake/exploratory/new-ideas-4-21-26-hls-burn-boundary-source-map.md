<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/new-ideas-4-21-26-hls-burn-boundary-source-map
title: New Ideas 4-21-26 - HLS Burn Interpretation Boundary Source Map
type: exploratory-intake-source-map
version: v0.1.0
status: triaged; exploratory; non-authoritative; decision-required
owners: OWNER_TBD - Agriculture steward; Hazards steward; remote-sensing steward; evidence steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; intake; exploratory; remote-sensing; hazards
truth_posture: cite-or-abstain; spectral change and fire corroboration remain distinct; a candidate is not a confirmed event, alert, promotion, release, or publication
owning_root: docs/
responsibility: Reconcile the private New Ideas 4-21-26 HLS burn-change proposal with current KFM Agriculture and Hazards surfaces while preserving source-role, interpretation, evidence, lifecycle, and publication boundaries.
source_class: connected private document
source_title: New Ideas 4-21-26
source_section: HLS burn/change thin-slice and hazards-burn candidate series
source_status: non-authoritative exploratory proposal
source_disclosure: privacy-minimized; full source text, connector locator, private link, timestamps, digest, and file size omitted
repository: bartytime4life/Kansas-Frontier-Matrix
repository_snapshot: 70229e41cc434c9cb0b3b29f02742773d4a18b77
repository_verified_on: 2026-08-10
related:
  - ./README.md
  - ./new-ideas-4-15-source-map.md
  - ./new-ideas-4-16-source-map.md
  - ./new-ideas-5-19-26-source-map.md
  - ../../../contracts/domains/agriculture/hls_ndvi_zonal_materiality.md
  - ../../../schemas/contracts/v1/domains/agriculture/hls_ndvi_zonal_materiality_assessment.schema.json
  - ../../../tools/validators/domains/agriculture/hls_ndvi_zonal_materiality/README.md
  - ../../../tests/validators/domains/agriculture/hls_ndvi_zonal_materiality/test_validate_hls_ndvi_zonal_materiality.py
  - ../../../fixtures/domains/agriculture/hls_ndvi_zonal_materiality/valid/material_change_candidate.json
  - ../../sources/catalog/nasa/nasa-hls.md
  - ../../../contracts/domains/hazards/README.md
  - ../../../schemas/contracts/v1/domains/hazards/README.md
  - ../../../tools/validators/domains/hazards/README.md
  - ../../../pipelines/domains/hazards/README.md
  - ../../domains/hazards/ARCHITECTURE.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, hls, ndvi, nbr, dnbr, vegetation-change, burn, wildfire, hazards, corroboration, abstain]
notes:
  - "The connected document was searched and its HLS burn/change series was reviewed in context. Private source text and connector metadata are deliberately excluded."
  - "The source is evidence that a burn-change pipeline, candidate, validator, catalog handoff, and runtime sequence were proposed. It is not evidence that source endpoints, thresholds, paths, workflows, packages, runtime routes, or releases exist or are current."
  - "Current-repository conclusions are limited to the pinned main snapshot."
  - "This source map creates no source activation, contract, schema, policy, threshold, validator, pipeline, workflow, receipt, proof, catalog item, runtime route, map layer, promotion, release, alert, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# New Ideas 4-21-26 - HLS burn interpretation boundary source map

> **Outcome:** Current KFM surfaces can describe HLS vegetation-change context and deterministically assess precomputed NDVI materiality, but this review did not find a burn-specific object that binds spectral change to separately evidenced fire corroboration. The retained idea is therefore a narrow interpretation boundary: vegetation disturbance may become a reviewable burn candidate only through explicit, time-and-place-compatible corroboration, and even then it does not become a confirmed fire event, severity fact, life-safety alert, promotion, release, or publication.

> [!CAUTION]
> The source proposes paths, source details, algorithms, thresholds, example identifiers, validation logic, catalog writes, tile packaging, and runtime behavior. Those details are proposal data. This source map adopts none of them.

**Quick links:** [Source boundary](#source-boundary-and-review-method) · [Placement](#directory-rules-and-authority-basis) · [Reconciliation](#repository-grounded-reconciliation) · [Retained gap](#retained-non-duplicative-gap) · [Decision candidate](#proposed-burn-interpretation-decision) · [Validation cases](#minimum-future-validation-cases) · [Unsafe transfers](#unsafe-direct-transfers) · [Next action](#recommended-next-bounded-action) · [Rollback](#rollback-and-correction)

## Source boundary and review method

### Privacy-minimized source identity

| Field | Bounded value |
|---|---|
| Supplied title | *New Ideas 4-21-26* |
| Reviewed cluster | HLS burn/change thin-slice and hazards-burn candidate series |
| Source posture | Non-authoritative exploratory proposal |
| Current repository comparison | `main@70229e41cc434c9cb0b3b29f02742773d4a18b77`, inspected `2026-08-10` |
| Private material | Full source text, Drive locator, private link, connector timestamps, digest, and file size intentionally omitted |

### Review method

This pass:

1. inventoried the connected document and reviewed the HLS burn/change sections in context;
2. treated its external-product facts, example metrics, thresholds, file tree, commands, workflow sequence, and runtime examples as unverified proposals;
3. searched current main for HLS, NDVI, NBR, dNBR, burn, wildfire, vegetation disturbance, fire corroboration, materiality, Hazards contracts, validators, fixtures, and pipeline lanes;
4. compared source paths against accepted Directory Rules and current responsibility-root evidence;
5. separated remote-sensing measurement from Hazards interpretation, corroboration, validation, promotion, release, and public runtime; and
6. retained only the non-duplicative interpretation seam.

The earlier [4-15](./new-ideas-4-15-source-map.md), [4-16](./new-ideas-4-16-source-map.md), and [5-19](./new-ideas-5-19-26-source-map.md) reconciliations already classify broad HLS/STAC/change-detection proposals as represented, corroborative, or source-readiness work. This map does not reopen those broad lanes.

[Back to top](#top)

## Directory Rules and authority basis

Accepted [Directory Rules v2](../../doctrine/directory-rules.md), adopted through [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md), place artifacts by owning responsibility rather than by producer or topic. The [exploratory intake README](./README.md) defines this lane as the waiting room for ideas that still need classification, evidence review, routing, promotion, archive, or rejection.

This source map belongs under `docs/intake/exploratory/` because it records private-source pressure, current repository evidence, path conflicts, a retained decision gap, and explicit non-effects. It does not belong under a semantic, schema, implementation, policy, data, release, or publication root.

If a later accepted decision authorizes a fixture-only implementation, current repository evidence indicates these responsibility homes:

| Responsibility | Current compatible home | Boundary |
|---|---|---|
| HLS source identity and product posture | `docs/sources/catalog/nasa/` plus the accepted source registry | Source authority and access posture; not Hazards interpretation. |
| Vegetation-change measurement meaning | `contracts/domains/agriculture/` | Agriculture owns HLS-derived vegetation measurement meaning in current evidence. |
| Burn-interpretation candidate meaning | `contracts/domains/hazards/` | Hazards may interpret admitted evidence without absorbing source or Agriculture authority. |
| Candidate machine shape | `schemas/contracts/v1/domains/hazards/` | Closed shape only after semantic and authority review. |
| Candidate validation | `tools/validators/domains/hazards/` | Validation cannot create observation, policy, promotion, release, or publication authority. |
| Hazards transformation logic | `pipelines/domains/hazards/` | Executable transformation only; live fetching remains source-connector responsibility. |
| Synthetic cases | `fixtures/domains/hazards/` and the matching test lane | Public-safe, no-network evidence pressure. |

The source's proposed parallel homes such as root-level `schemas/hazards/`, `contracts/hazards/`, `pipelines/hls-burn-watch/`, and `tools/validators/hazards_burn/` are not adopted. Current domain lanes already provide responsibility-compatible homes; creating competing authorities would require a separately accepted placement decision and migration plan.

[Back to top](#top)

## Repository-grounded reconciliation

Disposition terms:

- `REPRESENTED` - a current repository surface already owns the contribution.
- `DOCUMENTED / UNIMPLEMENTED` - current documentation names the posture, but executable closure is not established.
- `PARTIAL` - a related shape exists but does not close the proposed meaning.
- `CONFLICTED` - proposed placement or responsibility disagrees with current authority evidence.
- `RETAIN` - a narrower non-duplicate decision gap remains.
- `REJECT_AS_CURRENT` - the source statement cannot be treated as current repository or external-system fact.

| Source contribution | Current-main evidence | Disposition | Boundary |
|---|---|---|---|
| HLS change measurement over explicit baseline and current windows | [`HlsNdviZonalMaterialityAssessment`](../../../contracts/domains/agriculture/hls_ndvi_zonal_materiality.md), its [schema](../../../schemas/contracts/v1/domains/agriculture/hls_ndvi_zonal_materiality_assessment.schema.json), [validator](../../../tools/validators/domains/agriculture/hls_ndvi_zonal_materiality/README.md), [fixtures](../../../fixtures/domains/agriculture/hls_ndvi_zonal_materiality/valid/material_change_candidate.json), and [tests](../../../tests/validators/domains/agriculture/hls_ndvi_zonal_materiality/test_validate_hls_ndvi_zonal_materiality.py) already define a fixture-only NDVI materiality slice. | `REPRESENTED` | It validates precomputed summary semantics only; it does not fetch HLS, compute rasters, infer fire, issue an alert, or publish. |
| Mask trail, NBR/dNBR assets, explicit reference period, uncertainty, and burn-slice outputs | The [NASA HLS catalog page](../../sources/catalog/nasa/nasa-hls.md) documents these as required or proposed source/product posture and explicitly calls HLS context rather than field truth. | `DOCUMENTED / UNIMPLEMENTED` | A product page is not an executable mask chain, admitted source, produced asset, or released layer. |
| Hazards must distinguish detection, modeled context, observations, official context, and life-safety authority | The [Hazards contracts index](../../../contracts/domains/hazards/README.md), [architecture](../../domains/hazards/ARCHITECTURE.md), and [pipeline README](../../../pipelines/domains/hazards/README.md) preserve source roles, finite outcomes, expiry, evidence, official-source redirects, and no-alert authority. | `REPRESENTED` | A remote-sensing detection or derived metric is not confirmation, official warning, or life-safety instruction. |
| A burn-specific candidate requires both change evidence and separate fire corroboration | No burn-specific contract, closed schema, validator, fixture family, or test was found in the inspected Hazards domain lanes. | `PARTIAL / RETAIN` | Define only after the Agriculture-to-Hazards evidence seam and corroboration semantics are accepted. |
| Generic vegetation disturbance must remain distinct from a fire-corroborated burn candidate | Existing NDVI materiality explicitly lists smoke, post-fire regrowth, irrigation, crop rotation, and interpretation flags outside its statistic gate; Hazards has no inspected burn classifier. | `RETAIN` | Do not infer cause from spectral change. |
| Proposed root-level burn contract/schema/pipeline/validator homes | Current domain responsibility lanes already exist under `contracts/domains/`, `schemas/contracts/v1/domains/`, `pipelines/domains/`, and `tools/validators/domains/`. | `CONFLICTED` | Resolve through existing domain lanes unless an accepted ADR authorizes a different topology. |
| Source examples prove current HLS access, product fields, cadence, masks, thresholds, packages, runtime routes, or publication | No current source activation, complete burn workflow, hosted run, generated burn artifact, runtime response, or release evidence was established by this review. | `REJECT_AS_CURRENT` | Reverify unstable external facts and implementation state before use. |

The repository evidence supports a design gap, not a claim that the proposed HLS burn lane is implemented or operational.

[Back to top](#top)

## Retained non-duplicative gap

Current Agriculture materiality can answer whether a bounded NDVI summary changed enough for review under fixture rules. It deliberately cannot answer why the change occurred. Current Hazards doctrine can preserve detection, evidence, official-context, and life-safety boundaries, but this review did not find a burn-specific object at their seam.

The missing responsibility is not another raster calculator. It is a bounded interpretation candidate that keeps these questions separate:

1. **Measurement:** What source-versioned spectral change was observed over which spatial support and windows?
2. **Quality:** Which masks, valid-pixel coverage, uncertainty, and missingness apply?
3. **Corroboration:** Which independent fire-related sources overlap in place and compatible time, with which source roles and limitations?
4. **Interpretation:** Is the evidence sufficient only for vegetation disturbance, for a reviewable burn candidate, or for no safe conclusion?
5. **Authority:** Who may validate, review, promote, release, correct, roll back, or publish the candidate?
6. **Public boundary:** What may a governed API or map say without presenting KFM as an official fire or emergency authority?

Collapsing these questions would let a dNBR value become a fire claim, a nearby detection become perimeter or severity proof, a validator result become release authority, or a map layer become a life-safety surface.

[Back to top](#top)

## Proposed burn interpretation decision

**PROPOSED decision candidate, not an implemented object:** decide whether a fixture-only `BurnChangeInterpretationCandidate` responsibility is distinct enough to add under the Hazards domain after the Agriculture-to-Hazards evidence seam is reviewed. The name is provisional.

### Minimum bounded inputs

- stable spatial-support identity and non-sensitive geometry reference;
- explicit baseline and current observation windows;
- admitted spectral-change observation or assessment references, including source version and role;
- mask, valid-coverage, uncertainty, and missing-data references;
- machine-readable vegetation and burn-like signal summaries with declared method identity;
- separately admitted fire-corroboration references, source roles, observed/issued times, spatial relation, and limitations;
- threshold or interpretation-policy reference rather than embedded unexplained constants;
- EvidenceRef or equivalent resolvable evidence linkage appropriate to each material claim;
- deterministic subject identity over meaning-bearing inputs; and
- current candidate, review, and correction state.

### Minimum finite interpretations

The decision should preserve at least these meanings, even if final enum names differ:

| Interpretation | Meaning | Required public posture |
|---|---|---|
| vegetation disturbance candidate | Spectral change burden met; fire cause is not sufficiently supported. | Do not label as fire or burn. |
| fire-corroborated burn candidate | Spectral change and separately reviewed fire corroboration are compatible in scope and time. | Candidate for review only; not confirmed perimeter, cause, severity, official incident, or alert. |
| insufficient support | Quality, temporal, spatial, source, or evidence burden is incomplete. | `ABSTAIN` with bounded reasons. |
| no material change | Declared materiality burden not met for this comparison. | Preserve the negative observation; do not infer that no fire occurred. |
| invalid or unsafe | Contract, source-role, evidence, sensitivity, or deterministic-identity rule failed. | `DENY` or `ERROR`; no public claim. |

### Required non-effects

The candidate must not:

- fetch or activate a live source by default;
- recompute or silently repair upstream spectral or event evidence;
- treat NDVI, NBR, dNBR, a hotspot, smoke context, a perimeter, or an incident record as interchangeable;
- infer fire cause, ignition time, containment, damage, severity, legal status, or current emergency state without separately adequate authority;
- treat absent corroboration as proof that no fire occurred;
- emit an official warning, evacuation instruction, emergency alert, or life-safety recommendation;
- mutate RAW, WORK, QUARANTINE, PROCESSED, CATALOG, PUBLISHED, policy, workflow, or platform state;
- create a receipt, proof, EvidenceBundle, PromotionDecision, ReleaseManifest, CorrectionNotice, or RollbackCard by implication; or
- authorize map/API exposure, promotion, release, deployment, or publication.

[Back to top](#top)

## Minimum future validation cases

A later fixture-only proposal should not be reviewed without negative-path pressure for at least:

| Synthetic case | Expected bounded result |
|---|---|
| Material spectral change plus compatible, admitted fire corroboration | Reviewable fire-corroborated candidate; still not confirmed event or release. |
| Material spectral change with no adequate fire corroboration | Vegetation disturbance candidate or `ABSTAIN`; never burn by implication. |
| Fire-related corroboration with no material spectral change | Preserve event context separately; no burn-change candidate from this lane. |
| Low valid coverage, unresolved masks, or missing uncertainty | `ABSTAIN` or `DENY` according to the accepted contract; no optimistic repair. |
| Spatial overlap but incompatible observation windows | `DENY` or `ABSTAIN`; no temporal collapse. |
| dNBR or hotspot presented as perimeter, cause, severity, or official incident truth | `DENY` for source-role or meaning collapse. |
| Negative result without evidence or process references | `DENY`; negative outcomes remain auditable. |
| Threshold equality, changed threshold version, or changed method identity | Deterministic, explicitly tested result; no hidden policy drift. |
| Stale, superseded, corrected, or withdrawn evidence | Fail closed until the current chain resolves. |
| Candidate routed directly to public tiles or runtime | `DENY`; governed review and release remain separate. |

[Back to top](#top)

## Unsafe direct transfers

| Source pattern | Why direct transfer is unsafe | Required correction |
|---|---|---|
| Copy the proposed file tree | Several paths conflict with current domain responsibility lanes. | Route by owning responsibility and obtain an ADR only if a new topology is truly required. |
| Freeze example thresholds, windows, mask rules, or source fields as production policy | Values are source proposals and external/product behavior is version-sensitive. | Reverify authoritative sources, measure representative cases, and bind accepted values through the owning policy/configuration decision. |
| Label a large dNBR or NDVI loss as burn | Spectral change does not establish cause. | Require separate, compatible fire corroboration and preserve candidate status. |
| Treat a hotspot match as perimeter or severity proof | A detection has different spatial, temporal, and authority semantics. | Preserve source-native meaning and limitations; never inflate geometry or severity. |
| Treat absent corroboration as negative fire evidence | Coverage, latency, obstruction, and source limitations can create non-detection. | Emit insufficient support or a bounded non-detection statement only when its evidence contract allows it. |
| Recompute upstream data inside the validator | Validation would silently become acquisition and derivation authority. | Validate bound inputs; route repair or recomputation back to the owning source/pipeline lane. |
| Publish a candidate STAC item, COG, vector tile, or PMTiles archive directly | Packaging and catalog records do not close evidence, rights, sensitivity, review, release, correction, or rollback. | Require governed catalog, policy, review, release, and rollback closure. |
| Return a runtime `ANSWER` from an unpromoted candidate | Candidate review state is not outward truth. | Normal runtime reads only released governed interfaces and abstains otherwise. |
| Use KFM output as current fire or emergency instruction | KFM is not an official alerting authority. | Carry explicit non-life-safety posture and redirect to authoritative official sources. |

[Back to top](#top)

## Recommended next bounded action

Prepare a **decision-only Agriculture-to-Hazards burn-interpretation issue** before implementing a contract. It should:

- identify the existing Agriculture HLS observation/materiality objects that may be referenced without duplicating them;
- decide the provisional candidate name, owning domain, and exact semantic boundary;
- define acceptable corroboration families and their source-role, temporal, spatial, rights, sensitivity, and non-detection semantics;
- decide whether a fire-corroborated result is still only a candidate and what additional evidence could support stronger event claims;
- define method identity, threshold authority, missing-data treatment, corrections, and supersession;
- specify finite results and the negative fixtures above;
- preserve official-alert and life-safety denial; and
- authorize no source activation, pipeline, workflow, catalog write, runtime route, map layer, promotion, release, deployment, or publication.

Only after that decision should a fixture-only contract/schema/validator packet be considered in the current Hazards domain lanes. This intake source map does not authorize it.

[Back to top](#top)

## Validation and review boundary

This source map is complete only if:

- the reviewed source cluster and private identity remain bounded;
- private connector metadata and full source text are absent;
- current-repository claims remain pinned to `main@70229e41cc434c9cb0b3b29f02742773d4a18b77`;
- every linked repository path resolves;
- HLS measurement, burn interpretation, corroboration, validation, policy, promotion, release, public runtime, and life-safety authority remain separate;
- source path conflicts are visible rather than silently normalized;
- no external product fact, threshold, algorithm, path, workflow, runtime, or release claim is presented as current without evidence;
- no source activation, contract, schema, policy, validator, pipeline, workflow, data, receipt, proof, catalog, map, runtime, promotion, release, deployment, alert, or publication state changes; and
- the pull request remains one bounded documentation-only review surface.

## Rollback and correction

Before merge, rollback is closing the draft pull request and abandoning its branch. After a separately authorized merge, use a focused reviewed revert of this one source-map file.

If HLS product behavior, source authority, Agriculture materiality contracts, Hazards semantics, corroboration sources, Directory Rules, or implementation state changes:

1. preserve this file as dated intake lineage;
2. add a correction or supersession note rather than rewriting the prior proposal as current fact;
3. repeat repository and authoritative-source verification against a pinned snapshot;
4. route any promoted contract, policy, pipeline, source, or release change through its owning responsibility and rollback path; and
5. never let a corrected metric, candidate, validator result, catalog object, or map artifact silently become an official event or life-safety authority.

[Back to top](#top)
