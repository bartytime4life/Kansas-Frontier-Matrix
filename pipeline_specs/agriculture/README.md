<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-agriculture-readme
title: pipeline_specs/agriculture/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; declarative-only; fail-closed; no-live-activation
owning_root: pipeline_specs/
responsibility: govern inactive declarative pipeline intent for the agriculture scope
truth_posture: CONFIRMED inventory and fail-closed posture / PROPOSED declarations / NEEDS VERIFICATION activation prerequisites
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/agriculture/README.md
inherited_parent: pipeline_specs/README.md
scope_id: agriculture
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# Agriculture pipeline-spec declarations

`pipeline_specs/agriculture/` is the declarative run-intent boundary for Agriculture. It inherits the repository-wide rules in [the parent pipeline-spec contract](../README.md) and the responsibility split adopted by [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md).

Every declaration in this directory is `PROPOSED_INACTIVE`. File presence, schema validity, merge state, or a named cadence activates nothing.

## Owner and scope

`OWNER_TBD` must be resolved to the pipeline-spec steward and Agriculture, source, rights, evidence, sensitivity, validation, and release reviewers before activation can be considered.

This boundary may describe:

- stable declaration identity, stage, lifecycle candidates, and required gates;
- references to admitted sources, contracts, schemas, implementations, fixtures, tests, and workflows;
- deterministic execution constraints and rollback intent;
- a bounded Agriculture candidate such as NASS QuickStats.

This boundary does not own executable transforms, source admission, semantic meaning, machine shape, policy decisions, evidence closure, or release decisions. Those responsibilities remain in their accepted homes under `pipelines/`, source registries, `contracts/`, `schemas/`, `policy/`, evidence stores, and `release/`.

## Belongs here

- `KfmPipelineSpecDeclaration` YAML for this domain.
- Candidate lifecycle edges and denied execution capabilities.
- Stable repository-relative references to governed dependencies.
- Review, validation, non-effect, and rollback metadata.

## Prohibited here

- Credentials, tokens, private endpoints, copied source payloads, or operational logs.
- Fetch, transform, validation, catalog, publication, or scheduling code.
- Source activation, rights clearance, policy approval, or release authorization.
- Field-, operator-, parcel-, or facility-resolved sensitive content.
- Claims that aggregate statistics are field observations or current conditions.

## Inputs, outputs, and non-effects

Inputs are references and candidate lifecycle states only. Outputs are declarations for review; they are not data products or transition records.

| Capability | Required state |
|---|---|
| Live network access | `DENIED` |
| Source activation | `DENIED` |
| Lifecycle write | `DENIED` and `writes_targets: false` |
| Promotion | `DENIED` |
| Release | `DENIED` |
| Publication | `DENIED` |

No declaration creates an `EvidenceBundle`, policy decision, receipt, catalog object, release candidate, public layer, or API response.

## Exposure, mutation, and retention

Declarations are public-repository metadata and must contain only public-safe identifiers and references. Agriculture detail that could expose an operator, private parcel, field practice, facility, or reconstructable small-area result fails closed pending explicit policy review.

Changes require reviewable Git history, deterministic `spec_hash` recomputation, and validator success. Do not mutate a declaration to conceal prior meaning; supersede or revert it. Git is the declaration record. Source payloads and runtime artifacts are not retained here.

## Direct children

```text
pipeline_specs/agriculture/
├── README.md
├── catalog.yaml
├── ingest.yaml
├── nass_quickstats.yaml
├── normalize.yaml
├── publish.yaml
└── validate.yaml
```

The tree is direct-child-only; it does not imply executable order or activation.

## Declaration inventory

| Declaration | Kind | Stage | Status | Implementation |
|---|---|---|---|---|
| `catalog.yaml` | `STAGE_BOUNDARY` | `CATALOG` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `ingest.yaml` | `STAGE_BOUNDARY` | `INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `nass_quickstats.yaml` | `PIPELINE_CANDIDATE` | `INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `normalize.yaml` | `STAGE_BOUNDARY` | `NORMALIZE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `publish.yaml` | `STAGE_BOUNDARY` | `PUBLISH` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `validate.yaml` | `STAGE_BOUNDARY` | `VALIDATE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |

NASS QuickStats is an aggregate-statistics candidate. Aggregate source presentation does not itself prove acceptable geographic, temporal, commodity, operator, or disclosure granularity.

## Contract and validation

All YAML declarations conform to the shared [pipeline-spec declaration contract](../../contracts/pipeline_spec_declaration.md) and [JSON Schema](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json). Validate from the repository root:

```bash
python tools/validators/validate_pipeline_spec_declarations.py
pytest -q tests/validators/test_validate_pipeline_spec_declarations.py
git diff --check
```

Validation proves declaration shape, closed vocabularies, path resolution, ordering, and digest integrity. It does not prove source admission, implementation correctness, freshness, evidence, policy approval, or release readiness.

## Related responsibility families

- Domain meaning: [Agriculture contracts](../../contracts/domains/agriculture/README.md)
- Machine shape: [Agriculture schemas](../../schemas/contracts/v1/domains/agriculture/README.md)
- Executable behavior: [Agriculture pipelines](../../pipelines/domains/agriculture/README.md)
- Exposure rules: [Agriculture policy](../../policy/domains/agriculture/README.md)
- Deterministic examples: [Agriculture fixtures](../../fixtures/domains/agriculture/README.md)
- Enforcement: [Agriculture tests](../../tests/domains/agriculture/README.md)
- Evidence records: [Agriculture receipts](../../data/receipts/agriculture/README.md) and [proofs](../../data/proofs/agriculture/README.md)
- Human coordination: [Agriculture documentation](../../docs/domains/agriculture/README.md)
- Release review: [Agriculture release candidates](../../release/candidates/agriculture/README.md)

References do not transfer authority into this directory.

## Status and open verification

The lane is reviewable metadata only. Before any declaration can leave `PROPOSED_INACTIVE`, reviewers must verify owners, accepted source descriptors and roles, current rights, implementation bindings, fixture and test coverage, evidence closure, aggregation and disclosure thresholds, workflow enforcement, and release integration.

Open questions include the authoritative NASS connector, the exact safe aggregation floor, correction propagation, and whether the named candidate has a fixture-first consumer. Unknowns remain denied.

## Review triggers and rollback

Review is required when a source, stage edge, lifecycle target, sensitivity rule, implementation reference, gate, schema version, canonicalization rule, or exposure posture changes. Agricultural changes also require review when geography, commodity, time, operator, parcel, or facility resolution changes.

Rollback is `REVERT_DECLARATION_CHANGE`: revert the declaration commit, rerun validation, and preserve any correction or release action in its authoritative family. Reversion does not delete source data, retract evidence, or reverse a release by itself.
