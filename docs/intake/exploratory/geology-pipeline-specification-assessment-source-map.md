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
responsibility: Reconcile the uploaded Geology architecture packet with current repository evidence and document why one inactive fixture-only specification assessment is the smallest distinct implementation slice.
truth_posture: "CONFIRMED uploaded source bytes, current repository placeholders, and hosted inventory conflict; PROPOSED candidate semantics and paths; UNKNOWN real source rights, admitted descriptors, parser/consumer fitness, runtime behavior, and review acceptance; NEEDS VERIFICATION corrected exact-head CI and human review"
related:
  - ../../../pipeline_specs/geology/README.md
  - ../../../contracts/domains/geology/geology_pipeline_specification_assessment.md
  - ../../../schemas/contracts/v1/domains/geology/geology_pipeline_specification_assessment.schema.json
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Geology Pipeline Specification Assessment — Source and Repository Reconciliation Map

## 1. Decision

`IMPLEMENT_REPOSITORY_SLICE` — add one inactive, fixture-only
`GeologyPipelineSpecificationAssessmentCandidate` packet. Do not upgrade or
activate an existing placeholder specification and do not create a live connector,
pipeline, data product, catalog item, proof, release object, API, map layer, or
public claim.

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

Pinned implementation base: `main@5f838cfbd2362379f5adaf648b4ab9dc4870b8ff`.

| Evidence | CONFIRMED finding |
|---|---|
| `pipeline_specs/geology/README.md` | The lane identifies six direct seven-line `PROPOSED` family placeholders and reports no active specification, accepted specification schema, parser, registry, consumer binding, source activation record, or executable conformance profile. |
| `pipeline_specs/geology/bedrock_units.spec.yaml` | The file contains only status, source-doc, path, and a placeholder note. |
| `pipeline_specs/geology/{ingest,validate,normalize,catalog,publish}.yaml` | Five stage scaffolds contain `version: 1` and empty `stages: []`; they establish names only. |
| `docs/domains/geology/OBJECT_FAMILIES.md` | Geology already owns deterministic identity/temporal doctrine and explicit object families; this packet must compose with those owners. |
| Repository-wide candidate search | No `GeologyPipelineSpecificationAssessmentCandidate` or equivalent closed profile was found. |
| `pipeline_specs/soil/support_type_profile.v1.json` | Soil already has explicit source-support anti-collapse coverage; duplicating it would add less value than closing the Geology specification gap. |

## 4. Distinctness and dependency closure

The packet owns declaration coherence only:

1. semantic contract;
2. Draft 2020-12 schema;
3. deterministic exact-outcome fixture matrix;
4. safe no-network validator;
5. focused tests;
6. path-scoped read-only workflow;
7. this source map; and
8. generated authoring receipt.

It deliberately does not modify the six placeholder YAML files. Doing so would
prematurely imply an accepted parser, consumer, or activation contract.

## 5. Directory Rules decision and hosted inventory reconciliation

Accepted ADR-0029 and `docs/doctrine/directory-rules.md` assign meaning to
`contracts/`, machine shape to `schemas/`, synthetic replay to `fixtures/`,
reusable checks to `tools/validators/`, focused tests to `tests/`, read-only
orchestration to `.github/workflows/`, non-canonical source reconciliation to
`docs/intake/exploratory/`, and authoring provenance to
`data/receipts/generated/`.

The first exact-head `domain-geology` run failed because that workflow treats every
substantive Python file under `tools/validators/domains/geology/` and
`tools/validators/geology/` as part of a frozen explicit allowlist. The candidate
validator is a contract-assessment entry point, not a new accepted Geology runtime
validator. The smallest truthful repair is therefore to use the existing
top-level bounded-entry-point convention at
`tools/validators/validate_geology_pipeline_specification_assessment.py`, while
its own path-scoped workflow and tests remain the only execution binding.

This avoids weakening the domain inventory, editing an unrelated allowlist, or
misrepresenting the candidate as an accepted live Geology validator. No new root
or parallel source, contract, schema, policy, evidence, receipt, proof, release, or
publication home is created.

## 6. Validation and authority boundary

Local validation must prove schema meta-validity, Python compilation, exact fixture
polarity, deterministic replay, no-network behavior, workflow YAML syntax,
generated-receipt hash closure, and whitespace hygiene.

It cannot prove source admission, source rights, parser/consumer fitness, actual
geology, resource status, runtime behavior, policy/review acceptance, release,
deployment, publication, or public use. Corrected hosted exact-head CI and human
review remain `NEEDS VERIFICATION`.

## 7. Rollback

Before merge, abandon the additive packet. After an authorized merge, revert the
bounded PR. No live source, pipeline, data, cache, catalog, release, deployment, or
public artifact needs restoration.
