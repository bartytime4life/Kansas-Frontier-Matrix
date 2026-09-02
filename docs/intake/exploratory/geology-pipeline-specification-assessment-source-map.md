<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/geology-pipeline-specification-assessment-source-map
title: Geology Pipeline Specification Assessment — Source and Repository Reconciliation Map
type: source-map
version: v1.0.1
status: proposed; exploratory; non-canonical; no-source-activation
owners: OWNER_TBD — Geology steward · Pipeline-spec steward · Source/rights steward · Validation steward · Docs steward
created: 2026-08-12
updated: 2026-08-14
owning_root: docs/
policy_label: internal; intake; exploratory; geology; pipeline-spec; fixture-only
responsibility: Reconcile the uploaded Geology architecture packet with current repository evidence, record the externally merged fixture-only assessment, and preserve the truthful validator-inventory boundary.
truth_posture: "CONFIRMED uploaded source bytes, merged PR #2785, current repository placeholders, and repeated domain-geology inventory failure; PROPOSED candidate semantics and bounded validator placement; UNKNOWN real source rights, admitted descriptors, parser/consumer fitness, runtime behavior, and review acceptance; NEEDS VERIFICATION corrected exact-head CI and human review"
related:
  - ../../../pipeline_specs/geology/README.md
  - ../../../contracts/domains/geology/geology_pipeline_specification_assessment.md
  - ../../../schemas/contracts/v1/domains/geology/geology_pipeline_specification_assessment.schema.json
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Geology Pipeline Specification Assessment — Source and Repository Reconciliation Map

## 1. Current disposition

Merged PR #2785 added an inactive, fixture-only
`GeologyPipelineSpecificationAssessmentCandidate` over the six existing Geology
placeholder families. The PR was created as a draft but GitHub records an external
merge at `eb95930a784252be7a24cba425185ff26294e8bb`; the authoring agent did not
invoke that merge or mark the PR ready.

The assessment remains declaration-only. It does not activate a source,
placeholder, connector, parser, consumer, pipeline, data product, catalog item,
proof, release object, API, map layer, or public claim.

## 2. Attached evidence

| Source | Identity | Supported use | Limit |
|---|---|---|---|
| `KFM_Geology_Natural_Resources_Architecture_PDF_Only_Report_2026-04-21.pdf` | `sha256:d334f43df8fd74f17115cc0f51861cf8238c9cb99d37adaf95f5e4e1655fdf51` | Geology/natural-resources domain boundary; source-role and resource anti-collapse; public-safe geometry; offline-first build order | Planning report; not current repository or implementation proof |
| `Domain-Driven Design Reference.pdf` | `sha256:4406daa99ff0e3d58757d62d40358c9fd745f95137e99f14602659d0c3f54e55` | Bounded-context and ubiquitous-language reference for keeping Geology meanings explicit | External reference; does not set KFM paths or authority |
| `Kansas_Frontier_Matrix_Pipeline_Living_Implementation_Manual_v0.3.pdf` | `sha256:43d0c6fea4cc64edb87238a13ac49b639934a82dcef0fab2ef49217add0ba8cf` | Lifecycle, finite outcomes, receipts, correction, rollback, and no-autopublish posture | Doctrine/planning; not runtime proof |

The Geology report says to begin with source descriptors, schema/contract closure,
fixtures, source-role policy, public-safe geometry checks, catalog closure, and one
offline fixture slice before live source harvesting or UI routes. It also requires
observed, interpreted, modeled, administrative, occurrence, deposit, estimate,
extraction, production, and reclamation meanings to remain distinct.

## 3. Current repository evidence

Pinned correction base: `main@f5e082d423f1dbb0753f970a662de4f818c77529`.

| Evidence | CONFIRMED finding |
|---|---|
| `pipeline_specs/geology/README.md` | The lane still identifies six direct seven-line `PROPOSED` family placeholders and reports no active specification, accepted specification schema, parser, registry, consumer binding, source activation record, or executable conformance profile. |
| `pipeline_specs/geology/{ingest,validate,normalize,catalog,publish}.yaml` | Five stage scaffolds contain `version: 1` and empty `stages: []`; they establish names only. |
| `docs/domains/geology/OBJECT_FAMILIES.md` | Geology already owns deterministic identity/temporal doctrine and explicit object families; the assessment composes with those owners. |
| Merged PR #2785 | Added the fixture-only contract, schema, fixtures, validator, tests, workflow, source map, and authoring receipt. |
| Current-main `domain-geology` run 31812628242 | Fails because the merged validator became a substantive Python file beneath `tools/validators/domains/geology/` without being present in the workflow's frozen accepted-validator inventory. |
| Merged PR #2788 evidence | Independently classified the same `domain-geology` failure as inherited from #2785 and outside the PMTiles repair. |
| `tools/validators/README.md` | Root-level `validate_*.py` files are bounded validator entry points; domain subdirectories carry adopted domain-validator inventory. |

## 4. Why the validator moves

The candidate validator assesses a proposed contract declaration. It is not an
accepted live Geology pipeline validator and must not silently enlarge the frozen
`domain-geology` inventory.

The smallest truthful correction is therefore:

1. move the entry point to
   `tools/validators/validate_geology_pipeline_specification_assessment.py`;
2. update its focused test and path-scoped workflow;
3. leave `.github/workflows/domain-geology.yml` and its accepted inventory
   unchanged; and
4. emit a current-binding receipt while retaining the original #2785 authoring
   receipt unchanged as process lineage.

Adding the candidate to the domain allowlist would misclassify implementation
maturity. Weakening or deleting the inventory check would reduce the topology
ratchet. Reverting the entire assessment would discard a valid fixture-only control
when a narrower placement correction is available.

## 5. Directory Rules decision

Accepted ADR-0029 and `docs/doctrine/directory-rules.md` assign meaning to
`contracts/`, machine shape to `schemas/`, synthetic replay to `fixtures/`,
bounded validation entry points to `tools/validators/`, focused tests to `tests/`,
read-only orchestration to `.github/workflows/`, non-canonical source
reconciliation to `docs/intake/exploratory/`, and authoring process memory to
`data/receipts/generated/`.

The move stays within the existing `tools/validators/` responsibility root. It
creates no new root or parallel source, contract, schema, policy, evidence,
receipt, proof, release, or publication authority.

## 6. Receipt lineage

`genrec-geology-pipeline-specification-assessment-20260814.json` remains unchanged
as the historical authoring receipt for merged PR #2785. The path-scoped workflow
validates a successor current-binding receipt for the moved validator and updated
workflow/test/source-map bytes. This follows repository precedent without claiming
a general receipt-succession policy.

## 7. Validation and authority boundary

The correction must prove:

- the exact fixture matrix still returns 5 `PASS`, 3 `ABSTAIN`, 21 `DENY`, and 1
  `ERROR`;
- all nine focused tests pass;
- the path-scoped workflow and `domain-geology` inventory both pass;
- generated-receipt hashes bind the current artifact bytes;
- no network access is used; and
- repository topology reports no new or stale drift.

It cannot prove source admission, source rights, parser/consumer fitness, actual
geology, resource status, runtime behavior, policy/review acceptance, release,
deployment, publication, or public use.

## 8. Rollback

Before merge, abandon the correction branch. After an authorized merge, revert the
bounded correction commit. That restores the original validator path and workflow
binding; it does not affect a live source, pipeline, data, cache, catalog, release,
deployment, or public artifact.
