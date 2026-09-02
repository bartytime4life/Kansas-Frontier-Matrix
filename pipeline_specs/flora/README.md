<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-flora-readme
title: pipeline_specs/flora/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; declarative-only; fail-closed; no-live-activation
owning_root: pipeline_specs/
responsibility: govern inactive declarative pipeline intent for the flora scope
truth_posture: CONFIRMED inventory and fail-closed posture / PROPOSED declarations / NEEDS VERIFICATION activation prerequisites
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/flora/README.md
inherited_parent: pipeline_specs/README.md
scope_id: flora
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# Flora pipeline declaration boundary

`pipeline_specs/flora/` is the declarative Flora lane inherited from [`pipeline_specs/`](../README.md). It records bounded proposals for what a pipeline may attempt; executable behavior remains under `pipelines/`.

Directory Rules v2 is adopted by [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md). This README applies its `BOUNDARY_COMPACT` profile.

> [!IMPORTANT]
> File presence does not activate execution. Every YAML declaration is `PROPOSED_INACTIVE`; network access, source activation, lifecycle writes, promotion, release, and publication remain `DENIED`.

> [!CAUTION]
> Exact or reconstructable rare-plant locations, seed-bank or collection access, culturally sensitive plant knowledge, private-land joins, restricted source terms, and license-limited payloads fail closed. A taxon or occurrence record is not automatically public-safe Flora truth.

## Owner and scope

- Local owners: pipeline-spec and Flora stewards; names remain `OWNER_TBD`.
- Scope ID: `kfm://scope/pipeline-specs/flora`.
- Local authority: inactive declarations, bindings, candidate lifecycle edges, and required gates.
- Inherited authority: lifecycle, trust, evidence, public-boundary, correction, and rollback rules from the parent boundary.

## Belongs / prohibited

Belongs here:

- Flora stage-boundary declarations and source-specific pipeline candidates;
- explicit references to admitted source descriptors, contracts, schemas, fixtures, tests, workflows, and gates;
- disabled execution posture and deterministic rollback metadata.

Prohibited here:

- executable connectors, parsers, transformations, models, or schedulers;
- credentials, private endpoints, raw payloads, occurrence evidence, or sensitive coordinates;
- source-admission, taxonomy, policy, evidence, catalog, promotion, release, or publication authority;
- a second watcher authority created by directory symmetry.

## Inputs and outputs

- Candidate inputs: admitted source-capture candidates, `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, catalog, proof, and release-decision references as stage-appropriate.
- Candidate outputs: declared lifecycle targets only; no declaration writes them while inactive.
- Permitted writers: reviewed repository changes only. Runtime and watcher writers are not authorized here.
- A declaration may point to executable code; it does not transfer implementation ownership into this directory.

## Exposure, mutation, and retention

- Exposure: public repository metadata only; examples must be synthetic or irreversibly generalized.
- Mutation: review-gated and digest-sensitive; schema, identity, target, gate, or reference changes require validation.
- Retention: version-control history; superseded declarations remain traceable or are removed by a reviewed migration.
- Physical payload storage is prohibited.

## Current direct-child map

```text
pipeline_specs/flora/
├── README.md                       # This boundary contract
├── catalog.yaml                    # Inactive CATALOG boundary
├── flora_publish_dryrun.yaml       # Inactive publication dry-run candidate
├── gbif_ingest.yaml                # Inactive GBIF ingest candidate
├── inaturalist_ingest.yaml         # Inactive iNaturalist ingest candidate
├── ingest.yaml                     # Inactive INGEST boundary
├── normalize.yaml                  # Inactive NORMALIZE boundary
├── plants_drift_watcher.yaml       # Inactive watcher candidate; placement HOLD
├── publish.yaml                    # Inactive PUBLISH boundary
├── source_readiness/               # Schema-specific readiness profile family
├── usfws_ecos_ingest.yaml          # Inactive USFWS ECOS ingest candidate
├── validate.yaml                   # Inactive VALIDATE boundary
└── watchers/                       # Empty child boundary; placement unresolved
```

## Declaration inventory

| Declaration | Kind / stage | Status | Implementation |
|---|---|---|---|
| `ingest.yaml` | `STAGE_BOUNDARY / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `normalize.yaml` | `STAGE_BOUNDARY / NORMALIZE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `validate.yaml` | `STAGE_BOUNDARY / VALIDATE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `catalog.yaml` | `STAGE_BOUNDARY / CATALOG` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `publish.yaml` | `STAGE_BOUNDARY / PUBLISH` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `gbif_ingest.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `inaturalist_ingest.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `usfws_ecos_ingest.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `flora_publish_dryrun.yaml` | `PIPELINE_CANDIDATE / PUBLISH_DRY_RUN` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `plants_drift_watcher.yaml` | `PIPELINE_CANDIDATE / WATCH` | `PROPOSED_INACTIVE`; `HOLD` | `NOT_IMPLEMENTED` |
| `source_readiness/materiality_profile.v1.json` | `FloraSourceReadinessMaterialityProfile` | `PROPOSED_INACTIVE` | Schema-specific profile |

All ten YAML files use `KfmPipelineSpecDeclaration`. The JSON profile keeps its established, schema-specific contract and is not silently converted.

## Validation

Run from the repository root:

```bash
python tools/validators/validate_pipeline_spec_declarations.py
python -m pytest tests/validators/test_validate_pipeline_spec_declarations.py -q
```

Validation must reject duplicate keys, aliases, unknown fields, invalid paths or hashes, active status, permissive execution, and missing fixture-first bindings. Passing validation is not activation or release.

## Related authority families

- Common semantics: [`contracts/pipeline_spec_declaration.md`](../../contracts/pipeline_spec_declaration.md)
- Common shape: [`schemas/contracts/v1/pipeline_spec_declaration.schema.json`](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Flora contracts / policy: `contracts/domains/flora/`, `policy/domains/flora/`
- Flora fixtures / tests: `fixtures/domains/flora/`, `tests/domains/flora/`
- Executable consumers: `pipelines/domains/flora/`
- Release candidates: `release/candidates/flora/`; declarations confer no release authority

## Status and open verification

- Status: repository-grounded, declarative-only, and inactive.
- `HOLD / PLACEMENT_REVIEW_REQUIRED`: decide whether `plants_drift_watcher.yaml`, `watchers/`, or the shared `pipeline_specs/watchers/` lane owns watcher intent. No canonical target is asserted here.
- Verify named owners, admitted source records, licensing, taxonomy authority, sensitivity policy, and public-safe transformations before any activation proposal.
- Verify every implementation, fixture, test, workflow, policy, and release reference before changing `implementation_status`.

## Review triggers and rollback

Re-review on owner, scope, consumer, source, rights, taxonomy, sensitivity, lifecycle edge, execution mode, schema, workflow, or placement change; on correction or withdrawal; and when an ADR changes authority.

Rollback is a reviewed revert of the bounded declaration or README change. If doubt arises, retain `PROPOSED_INACTIVE`, restore all denials, quarantine derived candidates, and escalate to the parent and domain stewards.
