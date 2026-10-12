<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-habitat-readme
title: pipeline_specs/habitat/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; declarative-only; fail-closed; no-live-activation
owning_root: pipeline_specs/
responsibility: govern inactive declarative pipeline intent for the habitat scope
truth_posture: CONFIRMED inventory and fail-closed posture / PROPOSED declarations / NEEDS VERIFICATION activation prerequisites
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/habitat/README.md
inherited_parent: pipeline_specs/README.md
scope_id: habitat
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# Habitat pipeline declaration boundary

`pipeline_specs/habitat/` is the declarative Habitat lane inherited from [`pipeline_specs/`](../README.md). It owns inactive run-graph proposals, not executable processing or ecological truth.

Directory Rules v2 is adopted by [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md). This README applies its `BOUNDARY_COMPACT` profile.

> [!IMPORTANT]
> File presence does not activate execution. Every YAML declaration is `PROPOSED_INACTIVE`; network access, source activation, lifecycle writes, promotion, release, and publication remain `DENIED`.

> [!CAUTION]
> Land-cover class is not habitat quality; an ecoregion is not occurrence; a modeled suitability surface is not occupancy; and a source label is not a regulatory critical-habitat decision. Sensitive-species, wetland, cultural, private-land, and cross-domain joins fail closed when they could reconstruct protected locations or exceed source authority.

## Owner and scope

- Local owners: pipeline-spec and Habitat stewards; names remain `OWNER_TBD`.
- Scope ID: `kfm://scope/pipeline-specs/habitat`.
- Local authority: inactive declarations, references, candidate lifecycle edges, and required gates.
- Inherited authority: lifecycle, evidence, public-boundary, correction, and rollback controls from the parent.

## Belongs / prohibited

Belongs here:

- Habitat stage boundaries and source- or model-specific pipeline candidates;
- explicit bindings to admitted source descriptors, contracts, schemas, fixtures, tests, workflows, and gates;
- disabled execution posture, reason codes, and rollback metadata.

Prohibited here:

- executable ETL, spatial analysis, classification, modeling, tiling, or scheduling code;
- source payloads, credentials, exact sensitive locations, or evidence objects;
- source admission, regulatory designation, policy, evidence, catalog, promotion, release, or publication authority;
- claims that contextual or modeled data is observed domain truth.

## Inputs and outputs

- Candidate inputs: source captures and governed `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, catalog, proof, and release-decision references.
- Candidate outputs: possible lifecycle targets declared for review only; inactive specifications write nothing.
- Permitted writers: reviewed repository changes only. Runtime writers are not authorized here.
- Cross-domain inputs retain their owning-domain identity, time, scale, rights, and sensitivity constraints.

## Exposure, mutation, and retention

- Exposure: public repository metadata; examples must be synthetic or irreversibly generalized.
- Mutation: review-gated and digest-sensitive; framework, vintage, CRS, scale, threshold, input, output, or gate changes require validation.
- Retention: version-control history and reviewed supersession lineage.
- Physical raster, vector, observation, and model payload storage is prohibited.

## Current direct-child map

```text
pipeline_specs/habitat/
├── README.md                       # This boundary contract
├── catalog.yaml                    # Inactive CATALOG boundary
├── connectivity.yaml               # Inactive connectivity derivation candidate
├── critical_habitat.yaml           # Inactive source-ingest candidate
├── ecoregions/                     # Empty regionalization child boundary
├── ingest.yaml                     # Inactive INGEST boundary
├── land_cover/                     # Land-cover materiality profile family
├── nlcd_landcover.yaml             # Inactive NLCD ingest candidate
├── normalize.yaml                  # Inactive NORMALIZE boundary
├── nwi_wetlands.yaml               # Inactive NWI ingest candidate
├── publish.yaml                    # Inactive PUBLISH boundary
├── suitability_model.yaml          # Inactive suitability derivation candidate
└── validate.yaml                   # Inactive VALIDATE boundary
```

## Declaration inventory

| Declaration | Kind / stage | Status | Implementation |
|---|---|---|---|
| `ingest.yaml` | `STAGE_BOUNDARY / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `normalize.yaml` | `STAGE_BOUNDARY / NORMALIZE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `validate.yaml` | `STAGE_BOUNDARY / VALIDATE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `catalog.yaml` | `STAGE_BOUNDARY / CATALOG` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `publish.yaml` | `STAGE_BOUNDARY / PUBLISH` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `critical_habitat.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `nlcd_landcover.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `nwi_wetlands.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `connectivity.yaml` | `PIPELINE_CANDIDATE / DERIVE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `suitability_model.yaml` | `PIPELINE_CANDIDATE / DERIVE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `land_cover/materiality_profile.v1.json` | `LandCoverMaterialityProfile` | `PROPOSED_INACTIVE` | Schema-specific profile |

All ten YAML files use `KfmPipelineSpecDeclaration`. The JSON materiality profile keeps its established schema and validator family.

## Validation

Run both validation families from the repository root:

```bash
python tools/validators/validate_pipeline_spec_declarations.py
python -m pytest tests/validators/test_validate_pipeline_spec_declarations.py -q
python -m unittest discover \
  --start-directory tests/validators/domains/habitat \
  --pattern 'test_land_cover_materiality.py' \
  --verbose
python tools/validators/domains/habitat/validate_land_cover_materiality.py --fixtures
```

Declaration validation must reject duplicate keys, aliases, unknown fields, invalid hashes or paths, active status, permissive execution, and missing fixture-first bindings. The dedicated land-cover materiality family rejects schema-invalid or tampered profiles; non-inactive or permissive governance posture; invalid analysis-unit, digest, metric, evidence, or timing inputs; non-deterministic threshold or fixture outcomes; and expected-invalid fixture codes that drift.

## Related authority families

- Common semantics: [`contracts/pipeline_spec_declaration.md`](../../contracts/pipeline_spec_declaration.md)
- Common shape: [`schemas/contracts/v1/pipeline_spec_declaration.schema.json`](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Habitat contracts / policy: `contracts/domains/habitat/`, `policy/domains/habitat/`
- Habitat fixtures / tests: `fixtures/domains/habitat/`, `tests/domains/habitat/`
- Executable consumers: `pipelines/domains/habitat/`
- Release candidates: `release/candidates/habitat/`; declarations confer no release authority

## Status and open verification

- Status: repository-grounded, declarative-only, and inactive.
- Verify named owners, admitted source records, rights, framework and version identity, CRS, scale, topology, temporal semantics, materiality, and sensitivity policy before any activation proposal.
- Verify cross-domain joins cannot reconstruct sensitive Flora, Fauna, cultural, or private-property detail.
- Verify every implementation, fixture, test, workflow, and release reference before changing `implementation_status`.

## Review triggers and rollback

Re-review on owner, source, consumer, framework, vintage, geometry, CRS, resolution, threshold, model, join, exposure, lifecycle, schema, workflow, or ADR change; and on correction or withdrawal.

Rollback is a reviewed revert of the bounded declaration or README change. If confidence drops, retain `PROPOSED_INACTIVE`, restore every denial, quarantine candidates, and notify the parent and Habitat stewards.
