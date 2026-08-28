<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/new-ideas-3-geometry-delta-review-source-map
title: New Ideas 3 - Geometry Delta Review Source Map
type: exploratory-intake-source-map
version: v0.1.0
status: triaged; exploratory; non-authoritative; decision-required
owners: OWNER_TBD - Data steward; geometry steward; domain stewards; policy steward; review steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; intake; exploratory; geometry; review-support
truth_posture: CONFIRMED source extraction and current repository comparison / PROPOSED geometry-delta review-packet decision / NEEDS VERIFICATION hosted exact-head validation and steward adoption
owning_root: docs/
responsibility: Reconcile the private New Ideas 3 geometry-diff proposal with current KFM spatial, material-change, source-specific comparison, validation, and review surfaces while retaining only a non-duplicative cross-domain review-evidence gap.
source_class: connected private document
source_title: New Ideas 3
source_section: geometry-diff checks in pull requests
source_status: non-authoritative exploratory proposal
source_disclosure: privacy-minimized; full source text, connector locator, private link, timestamps, digest, and file size omitted
repository: bartytime4life/Kansas-Frontier-Matrix
repository_snapshot: 22301d284658b031c0aba87cbfab25815dc9ca8f
repository_verified_on: 2026-08-10
related:
  - ./README.md
  - ../../../contracts/common/spatial_geometry.md
  - ../../../schemas/contracts/v1/common/spatial_geometry.schema.json
  - ../../../tools/validators/validate_spatial_geometry.py
  - ../../../contracts/data/material_change_assessment.md
  - ../../../schemas/contracts/v1/data/material_change_assessment.schema.json
  - ../../../fixtures/contracts/v1/data/material_change_assessment/README.md
  - ../../../tools/validators/validate_material_change_assessment.py
  - ../../../tests/validators/test_validate_material_change_assessment.py
  - ../../../tools/ingest/ssurgo_watch/README.md
  - ../../../tests/ingest/ssurgo_watch/test_ssurgo_watch.py
  - ../../../tools/validators/geometry/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, geometry, delta, spatial-diff, review, materiality, preview, privacy, abstain]
notes:
  - "The connected document was searched and its geometry-diff proposal was reviewed in context. Private source text and connector metadata are deliberately excluded."
  - "The source is evidence that numeric geometry metrics, optional previews, a machine-readable manifest, and pull-request review routing were proposed. It is not evidence that its paths, code, dependencies, threshold, renderer, workflow, or policy are safe, current, or implemented."
  - "Current-repository conclusions are limited to the pinned main snapshot."
  - "This source map creates no geometry contract, schema, metric profile, threshold, renderer, validator, fixture, workflow, check run, policy decision, promotion, release, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# New Ideas 3 - Geometry delta review source map

> **Outcome:** KFM already has canonical spatial shape, generic material-change assessment, and source-specific spatial-diff evidence. The inspected main snapshot does not provide one shared, closed review packet that binds two comparable geometry states, their geometry/CRS profiles, safe aggregate delta metrics, and an optional privacy-safe preview reference without deciding materiality or publication. That narrow review-evidence seam is retained for a decision-only next step.

> [!CAUTION]
> The source's code, default threshold, repository paths, third-party dependencies, rendering behavior, and automation examples are proposal material. This source map adopts none of them.

**Quick links:** [Source boundary](#source-boundary-and-method) · [Placement](#directory-rules-and-authority-basis) · [Reconciliation](#repository-grounded-reconciliation) · [Retained gap](#retained-non-duplicative-gap) · [Candidate](#proposed-review-packet-boundary) · [Cases](#minimum-future-validation-cases) · [Next action](#recommended-next-bounded-action) · [Rollback](#rollback-and-correction)

## Source boundary and method

| Field | Bounded value |
|---|---|
| Supplied title | *New Ideas 3* |
| Reviewed cluster | Geometry-diff checks in pull requests |
| Source posture | Non-authoritative exploratory proposal |
| Current repository comparison | `main@22301d284658b031c0aba87cbfab25815dc9ca8f`, inspected `2026-08-10` |
| Private material | Full source text, Drive locator, private link, connector timestamps, digest, and file size intentionally omitted |

This pass:

1. reviewed the connected proposal in context;
2. treated its sample threshold, code, packages, paths, workflow, check-run behavior, and output manifest as unverified design material;
3. searched current main for geometry and spatial-delta contracts, schemas, validators, fixtures, review packets, material-change assessments, and visual-regression lanes;
4. compared the retained responsibility with accepted Directory Rules and adjacent root evidence;
5. separated geometry comparison evidence from materiality policy, domain meaning, sensitive-location review, lifecycle change, and release; and
6. retained only the missing shared review-evidence seam.

[Back to top](#top)

## Directory Rules and authority basis

Accepted [Directory Rules v2](../../doctrine/directory-rules.md), adopted through [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md), require one authority owner per artifact and placement by responsibility rather than producer, topic, or file format. The [exploratory intake README](./README.md) owns source reconciliation that has not yet become an accepted semantic or implementation decision.

This file therefore belongs under `docs/intake/exploratory/`. It records source pressure, repository evidence, the residual gap, unsafe transfers, and explicit non-effects. It does not create a parallel geometry, data, policy, proof, review, release, or publication authority.

A future packet would require a responsibility split rather than one combined implementation:

| Responsibility | Compatible current home | Status and boundary |
|---|---|---|
| Shared geometry-state meaning | [`contracts/common/spatial_geometry.md`](../../../contracts/common/spatial_geometry.md) | `REPRESENTED`; do not redefine canonical geometry shape. |
| Candidate-versus-baseline materiality meaning | [`contracts/data/material_change_assessment.md`](../../../contracts/data/material_change_assessment.md) | `REPRESENTED`; a geometry packet may supply evidence but must not replace this decision family or domain policy. |
| Proposed geometry-delta review evidence | `contracts/data/` with paired `schemas/contracts/v1/data/` | `PROPOSED`; exact object name and composition require a decision before files are created. |
| Reusable geometry validation | Existing `tools/validators/geometry/` or the paired data validator lane | `NEEDS VERIFICATION`; implementation ownership must be decided without creating two validators for one authority. |
| Synthetic examples and enforcement | Matching `fixtures/contracts/v1/data/` and `tests/validators/` lanes | `PROPOSED`; synthetic, no-network, and safe-geometry only. |
| Preview generation | Existing generator, map-proof, or diff tooling after ownership review | `HOLD`; a renderer is an implementation producer, not semantic or review authority. |
| Materiality thresholds | Accepted domain or policy profile | `HOLD`; no cross-domain numeric default is adopted here. |

Path decision for this source map:

```yaml
path_decision:
  artifact: new-ideas-3-geometry-delta-review-source-map
  proposed_path: docs/intake/exploratory/new-ideas-3-geometry-delta-review-source-map.md
  artifact_kind: human document
  authority_owner: private-source reconciliation and exploratory routing
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: cross_domain
  scope_id: geometry-delta-review
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - docs/intake/exploratory/README.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-AUTHROOT-001
    - DIR-SCOPELANE-004
    - DIR-DEP-001
  outcome: PLACE
```

[Back to top](#top)

## Repository-grounded reconciliation

| Source contribution | Current-main evidence | Disposition | Boundary |
|---|---|---|---|
| Canonical geometry shape and bounded geometry validation | [`SpatialGeometry`](../../../contracts/common/spatial_geometry.md), its [schema](../../../schemas/contracts/v1/common/spatial_geometry.schema.json), and [validator](../../../tools/validators/validate_spatial_geometry.py) already own shared geometry representation. | `REPRESENTED` | Shape validity does not compare two states or decide change significance. |
| Byte, semantic, and material candidate classification | [`MaterialChangeAssessment`](../../../contracts/data/material_change_assessment.md), its [schema](../../../schemas/contracts/v1/data/material_change_assessment.schema.json), [fixtures](../../../fixtures/contracts/v1/data/material_change_assessment/README.md), [validator](../../../tools/validators/validate_material_change_assessment.py), and [tests](../../../tests/validators/test_validate_material_change_assessment.py) already own generic materiality handoff. | `REPRESENTED` | It intentionally does not define domain thresholds or compute geometry evidence. |
| Exact spatial-disagreement evidence for one source family | The [SSURGO watcher](../../../tools/ingest/ssurgo_watch/README.md) binds a source-specific CRS, units, geometry profile, hashes, analysis extent, and exact mapunit-label disagreement fixture; its [tests](../../../tests/ingest/ssurgo_watch/test_ssurgo_watch.py) prove source-specific finite behavior. | `REPRESENTED / SOURCE-SPECIFIC` | Those mapunit semantics and fixture threshold must not become a universal geometry-delta contract. |
| Numeric geometry deltas plus an optional reviewer preview | No shared closed packet, paired schema, fixture family, or focused validator with this exact responsibility was found in the inspected common/data/geometry lanes. | `PARTIAL / RETAIN` | The packet must remain review evidence and compose with, not replace, materiality and policy. |
| A rendered image or check-run summary decides whether a change is safe | Current test doctrine treats visual diffs as review signals, not truth or release authority. | `REJECT_AS_AUTHORITY` | Rendering can be missing, lossy, generalized, stale, or sensitive. |
| One repository-wide area-ratio threshold | The source proposes an example default, while current KFM evidence keeps thresholds source/domain/profile owned. | `REJECT_AS_CURRENT` | CRS, units, scale, topology, geometry family, and domain consequences make a universal default unsafe. |
| Automatic pull-request comment or check publication | No accepted GitHub check identity, permissions, artifact-retention, preview-privacy, or failure policy was established by this review. | `DEFER` | Automation follows the semantic packet and safe-output decision; it cannot create them. |

The residual is therefore not another materiality classifier, general geometry schema, SSURGO comparator, or screenshot test. It is a content-bound review-evidence envelope between geometry comparison and separately governed materiality/review decisions.

[Back to top](#top)

## Retained non-duplicative gap

A reviewer currently has no shared closed object that answers all of these bounded questions without crossing authority lines:

1. Which immutable baseline and candidate artifacts were compared?
2. Were both geometry states interpreted under compatible geometry, CRS, axis, unit, dimensionality, precision, and validity profiles?
3. Which comparison method and version produced the result?
4. Which safe aggregate metrics were computed, and which were intentionally not computed?
5. Does an optional preview resolve to the same comparison and metric digest?
6. Was the preview suppressed or generalized because geometry is sensitive or reconstructable?
7. Which separate materiality or policy profile may interpret the metrics?
8. What finite review signal is safe when inputs are missing, incomparable, invalid, sensitive, or renderer-incomplete?

Without that separation, an area number can silently inherit square-degree units, a changed total can hide topology relocation, a PNG can become proof, an image can leak restricted geometry, or a CI threshold can become policy by convenience.

[Back to top](#top)

## Proposed review packet boundary

**PROPOSED decision candidate, not an implemented object:** decide whether a fixture-only `GeometryDeltaReviewPacket` responsibility is distinct enough to add as a data-comparison evidence family. The name and exact composition are provisional.

### Minimum bounded inputs

- immutable baseline and candidate artifact references plus content digests;
- baseline and candidate geometry-state references or canonical geometry digests;
- one declared comparison scope, including feature-selection and missing-feature rules;
- geometry profile, CRS reference, axis order, coordinate and area units, dimensionality, validity, and precision posture;
- method identity and version, with topology-repair behavior declared rather than hidden;
- deterministic safe aggregate metrics such as added, removed, intersection, symmetric-difference, and feature-count changes when meaningful;
- explicit `NOT_APPLICABLE`, `NOT_COMPUTED`, or equivalent states rather than fabricated zeroes;
- optional preview reference, digest, renderer profile, and sensitivity/generalization posture;
- separate materiality-profile or policy reference, never an unexplained embedded universal threshold;
- evidence and run references sufficient to reproduce the comparison in the accepted fixture profile; and
- a deterministic packet identity over all meaning-bearing inputs and outputs.

### Finite meanings to preserve

| Meaning | Required posture |
|---|---|
| Comparable with no reported delta | Review evidence only; not proof that the source, claim, or world did not change. |
| Comparable with reported delta | Route for separately governed materiality/reviewer interpretation. |
| Incomparable | `ABSTAIN`; do not coerce CRS, geometry type, scope, precision, or profile drift into a number. |
| Sensitive preview withheld | Keep safe metrics only when permitted; otherwise `ABSTAIN` or `DENY` without reconstructive detail. |
| Invalid packet or contradictory metrics | `DENY` or `ERROR`; no review or lifecycle authority. |

### Required non-effects

The packet must not fetch a source, mutate either geometry, repair topology silently, select a policy threshold, declare a change material, approve review, move lifecycle state, create an EvidenceBundle, sign an attestation, open or update a pull request, release an artifact, publish a preview, or authorize public use.

[Back to top](#top)

## Minimum future validation cases

| Synthetic case | Expected bounded result |
|---|---|
| Same canonical geometry and compatible profiles | Comparable no-delta review evidence. |
| Equal total area but relocated or relabeled geometry | Nonzero topology/spatial delta; never hidden by net-area equality. |
| Added and removed areas cancel numerically | Preserve both directions and symmetric difference. |
| Geographic coordinates treated as planar square units | `DENY` or `ABSTAIN`; no misleading area ratio. |
| CRS, axis order, precision, or comparison scope changed | Incomparable until an accepted normalization or rebase profile is supplied. |
| Invalid geometry with undeclared repair | `DENY`; validator must not mutate inputs. |
| Empty baseline, empty candidate, deletion, and creation | Explicit, separately tested meanings; no division-by-zero fallback that fabricates comparability. |
| Preview digest does not bind the metric packet | `DENY`. |
| Preview omitted by renderer failure | Metrics may remain reviewable only when their own evidence is complete; absence is explicit. |
| Restricted geometry rendered or reconstructable from metrics/preview | `DENY` with safe diagnostics and no leaked coordinates. |
| Threshold or materiality result embedded without an accepted profile reference | `DENY`; comparison evidence cannot self-authorize policy. |
| Passing packet routed directly to release or publication | `DENY`; review evidence is not promotion or release closure. |

[Back to top](#top)

## Recommended next bounded action

Open a decision-only review for the proposed packet before implementation. It should:

- confirm that the packet is not already subsumed by `SpatialGeometry`, `MaterialChangeAssessment`, `ArtifactDeltaReceipt`, or a current geometry-proof family;
- decide whether the semantic owner is `contracts/data/` and whether comparison execution belongs under the existing geometry or diff tooling lane;
- define geometry-profile compatibility, CRS/unit behavior, empty-state semantics, topology repair, metric vocabulary, and deterministic identity;
- define preview binding, renderer determinism, artifact retention, sensitive-geometry suppression, and safe diagnostics;
- require policy-owned materiality profiles and domain-specific interpretation outside the packet;
- specify the negative cases above with wholly synthetic geometry; and
- authorize no live source, cross-domain threshold, workflow, check-run publisher, lifecycle write, promotion, release, deployment, or publication.

Only after that decision should a closed schema, synthetic fixtures, validator, and focused tests be considered. Pull-request automation should be a later consumer of an accepted safe packet, not its authority source.

## Validation and review boundary

This source map is complete only if all repository links resolve, the private source remains privacy-minimized, the current-main snapshot is explicit, represented responsibilities are not duplicated, the example threshold and code are not adopted, geometry evidence stays separate from materiality/policy/review/release authority, and the pull request changes only this documentation file.

## Rollback and correction

Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert this one additive source-map file. No source, data, geometry, workflow, check run, policy, review, release, or public artifact needs operational cleanup.

If later repository evidence shows an existing shared packet, mark this intake map superseded and point to that owner rather than creating a parallel contract. If geometry, policy, Directory Rules, or review behavior changes, preserve this dated lineage and add a correction; do not rewrite the old proposal as current fact.

[Back to top](#top)
