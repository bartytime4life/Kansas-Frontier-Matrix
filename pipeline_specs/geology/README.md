<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-geology-readme
title: pipeline_specs/geology/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; declarative-only; fail-closed; no-live-activation
owning_root: pipeline_specs/
responsibility: govern inactive declarative pipeline intent for the geology scope
truth_posture: CONFIRMED inventory and fail-closed posture / PROPOSED declarations / NEEDS VERIFICATION activation prerequisites
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/geology/README.md
inherited_parent: pipeline_specs/README.md
scope_id: geology
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# Geology and natural-resources pipeline-spec declarations

`pipeline_specs/geology/` is the declarative run-intent boundary for Geology and natural-resources processing. It inherits [the parent pipeline-spec contract](../README.md) and the responsibility split adopted by [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md).

Every declaration here is `PROPOSED_INACTIVE` and `NOT_IMPLEMENTED`. File presence, filename, schema validity, merge state, or a source reference activates nothing.

## Owner and scope

`OWNER_TBD` must be resolved to the pipeline-spec steward and Geology, stratigraphy, natural-resources, source, rights, datum, sensitivity, evidence, validation, and release reviewers before activation can be considered.

This boundary may describe:

- stable declaration identity, stage, candidate lifecycle edges, and required gates;
- candidate families for mapped units, boreholes, well logs, cross-sections, and mineral occurrences;
- references to admitted sources, semantics, schemas, implementations, fixtures, tests, and workflows;
- scale, depth, datum, vintage, uncertainty, sensitivity, and rollback prerequisites.

This boundary cannot establish geologic observation, continuity, interpretation, resource status, mineral rights, source rights, evidence closure, exposure approval, or release authority.

## Belongs here

- `KfmPipelineSpecDeclaration` YAML for this domain.
- Candidate lifecycle edges and denied execution capabilities.
- Repository-relative references to governed dependencies.
- Review, validation, non-effect, and rollback metadata.

## Prohibited here

- Credentials, private endpoints, copied source payloads, or operational logs.
- Fetch, transform, model, interpolation, catalog, publication, or scheduling code.
- Exact sensitive borehole, well, core, extraction, storage, infrastructure, parcel, cultural, or archaeological locations.
- Collapse of mapped, inferred, interpreted, modeled, or historical material into direct observation.
- Collapse of an occurrence into a deposit, estimate, reserve, ownership, permit, or production claim.

## Inputs, outputs, and non-effects

Inputs are governed references and candidate lifecycle states. Outputs are declaration metadata for review, not geologic objects, interpretations, models, resources, or releases.

| Capability | Required state |
|---|---|
| Live network access | `DENIED` |
| Source activation | `DENIED` |
| Lifecycle write | `DENIED` and `writes_targets: false` |
| Promotion | `DENIED` |
| Release | `DENIED` |
| Publication | `DENIED` |

No declaration creates an `EvidenceBundle`, policy decision, receipt, proof, catalog object, resource assertion, release candidate, public layer, 3D scene, or API response.

## Exposure, mutation, and retention

Declarations are public-repository metadata and must contain only public-safe references. Exact or reconstructable subsurface, private-well, core/sample, resource-target, extraction/storage infrastructure, operator/parcel, cultural, or archaeological detail fails closed.

Changes require reviewable Git history, deterministic `spec_hash` recomputation, and validator success. Supersede or revert changed meaning; do not silently alter claim or sensitivity boundaries. Git retains declarations. Source payloads, field records, models, and restricted geometry are retained only in governed data systems.

## Direct children

```text
pipeline_specs/geology/
├── README.md
├── bedrock_units.spec.yaml
├── boreholes.spec.yaml
├── catalog.yaml
├── cross_sections.spec.yaml
├── ingest.yaml
├── mineral_occurrences.spec.yaml
├── normalize.yaml
├── publish.yaml
├── surficial_units.spec.yaml
├── validate.yaml
└── well_logs.spec.yaml
```

The tree is direct-child-only; it does not imply processing order, source admission, or activation.

## Declaration inventory

| Declaration | Kind | Stage | Status | Implementation |
|---|---|---|---|---|
| `bedrock_units.spec.yaml` | `PIPELINE_CANDIDATE` | `UNSPECIFIED` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `boreholes.spec.yaml` | `PIPELINE_CANDIDATE` | `UNSPECIFIED` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `catalog.yaml` | `STAGE_BOUNDARY` | `CATALOG` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `cross_sections.spec.yaml` | `PIPELINE_CANDIDATE` | `UNSPECIFIED` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `ingest.yaml` | `STAGE_BOUNDARY` | `INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `mineral_occurrences.spec.yaml` | `PIPELINE_CANDIDATE` | `UNSPECIFIED` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `normalize.yaml` | `STAGE_BOUNDARY` | `NORMALIZE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `publish.yaml` | `STAGE_BOUNDARY` | `PUBLISH` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `surficial_units.spec.yaml` | `PIPELINE_CANDIDATE` | `UNSPECIFIED` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `validate.yaml` | `STAGE_BOUNDARY` | `VALIDATE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `well_logs.spec.yaml` | `PIPELINE_CANDIDATE` | `UNSPECIFIED` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |

`UNSPECIFIED` preserves candidate identity without inventing a processing stage. It must be resolved by review before implementation binding.

## Contract and validation

All YAML declarations conform to the shared [pipeline-spec declaration contract](../../contracts/pipeline_spec_declaration.md) and [JSON Schema](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json). Validate from the repository root:

```bash
python tools/validators/validate_pipeline_spec_declarations.py
pytest -q tests/validators/test_validate_pipeline_spec_declarations.py
git diff --check
```

Validation proves declaration shape, closed vocabularies, path resolution, ordering, and digest integrity. It does not prove source admission, scale fitness, datum alignment, geologic interpretation, sensitivity approval, evidence, or release readiness.

## Related responsibility families

- Domain meaning: [Geology contracts](../../contracts/domains/geology/README.md)
- Machine shape: [Geology schemas](../../schemas/contracts/v1/domains/geology/README.md)
- Executable behavior: [Geology pipelines](../../pipelines/domains/geology/README.md)
- Exposure rules: [Geology policy](../../policy/domains/geology/README.md)
- Deterministic examples: [Geology fixtures](../../fixtures/domains/geology/README.md)
- Enforcement: [Geology tests](../../tests/domains/geology/README.md)
- Evidence records: [Geology receipts](../../data/receipts/geology/README.md) and [proofs](../../data/proofs/geology/README.md)
- Human coordination: [Geology documentation](../../docs/domains/geology/README.md)
- Release review: [Geology release candidates](../../release/candidates/geology/README.md)

References do not transfer authority into this directory.

## Status and open verification

The lane is reviewable metadata only. Before any declaration can leave `PROPOSED_INACTIVE`, reviewers must verify owners, source admission and rights, canonical object names, claim roles, scale, CRS, vertical and depth datums, vintage, uncertainty, sensitivity policy, implementation bindings, fixtures, tests, evidence closure, workflow enforcement, and release integration.

The stage for all six object-family candidates remains deliberately `UNSPECIFIED`. Source-registry topology, receipt subtype layout, correction propagation, and public-safe geometry also remain open. Unknowns remain denied.

## Review triggers and rollback

Review is required when a source, stage edge, lifecycle target, object family, claim role, schema, implementation, gate, or exposure posture changes. Geology changes also require review when scale, resolution, depth, datum, vintage, uncertainty, geometry precision, rights, or resource terminology changes.

Rollback is `REVERT_DECLARATION_CHANGE`: revert the declaration commit, rerun validation, and preserve correction or release actions in their authoritative families. Reversion does not retract evidence, delete restricted source material, or reverse a release by itself.
