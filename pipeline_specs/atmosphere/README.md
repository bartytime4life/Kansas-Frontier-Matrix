<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-atmosphere-readme
title: pipeline_specs/atmosphere/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; declarative-only; fail-closed; no-live-activation
owning_root: pipeline_specs/
responsibility: govern inactive declarative pipeline intent for the atmosphere scope
truth_posture: CONFIRMED inventory and fail-closed posture / PROPOSED declarations / NEEDS VERIFICATION activation prerequisites
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/atmosphere/README.md
inherited_parent: pipeline_specs/README.md
scope_id: atmosphere
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# Atmosphere pipeline-spec declarations

`pipeline_specs/atmosphere/` is the declarative run-intent boundary for atmospheric observations, air quality, weather, climate, smoke, and related derived context. It inherits [the parent pipeline-spec contract](../README.md) and the responsibility split adopted by [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md).

Every declaration here is `PROPOSED_INACTIVE`. The sibling `pipeline_specs/air/` path is a compatibility boundary; it is not a second writable Atmosphere authority.

File presence, schema validity, merge state, or a named cadence activates nothing.

## Owner and scope

`OWNER_TBD` must be resolved to the pipeline-spec steward and Atmosphere, air-quality, meteorology, source, temporal, evidence, policy, validation, hazards, and release reviewers before activation can be considered.

This boundary may describe:

- stable declaration identity, stage, candidate lifecycle edges, and required gates;
- references to admitted observations, forecasts, model outputs, remote sensing, or advisory context;
- explicit temporal, unit, method, uncertainty, and freshness prerequisites;
- deterministic execution constraints and rollback intent.

This directory does not establish observation truth, official warning authority, source rights, machine meaning, executable behavior, evidence closure, public safety, or release approval.

## Belongs here

- `KfmPipelineSpecDeclaration` YAML for the Atmosphere domain.
- Candidate lifecycle edges and denied execution capabilities.
- Repository-relative references to governed dependencies.
- Review, validation, non-effect, and rollback metadata.

## Prohibited here

- Credentials, private endpoints, copied payloads, runtime logs, or unrestricted station metadata.
- Fetch, transform, forecast, alerting, catalog, publication, or scheduling code.
- Claims that a forecast, model, interpolation, satellite retrieval, or AI summary is an observation.
- Claims that stale or unit-ambiguous material is current or comparable.
- Replacement of official emergency warnings, forecasts, or agency guidance.

## Inputs, outputs, and non-effects

Inputs are governed references and candidate lifecycle states. Outputs are declaration metadata for review, not observations, forecasts, alerts, or products.

| Capability | Required state |
|---|---|
| Live network access | `DENIED` |
| Source activation | `DENIED` |
| Lifecycle write | `DENIED` and `writes_targets: false` |
| Promotion | `DENIED` |
| Release | `DENIED` |
| Publication | `DENIED` |

No declaration creates an `EvidenceBundle`, freshness proof, policy decision, receipt, alert, catalog object, release candidate, public map, or API response.

## Exposure, mutation, and retention

Declarations are public-repository metadata. They must not contain credentials, restricted endpoints, embargoed material, precise sensitive facilities, or station/operator details that policy has not cleared. Public air or weather data remains subject to rights, attribution, method, time, and reconstruction review.

Changes require reviewable Git history, deterministic `spec_hash` recomputation, and validator success. Supersede or revert changed meaning; do not silently rewrite history. Git retains declarations. Source payloads, model runs, observations, and operational alerts are retained only in their governed homes.

## Direct children

```text
pipeline_specs/atmosphere/
├── README.md
├── catalog.yaml
├── ingest.yaml
├── normalize.yaml
├── publish.yaml
└── validate.yaml
```

The tree is direct-child-only; it does not imply executable order, source admission, freshness, or activation.

## Declaration inventory

| Declaration | Kind | Stage | Status | Implementation |
|---|---|---|---|---|
| `catalog.yaml` | `STAGE_BOUNDARY` | `CATALOG` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `ingest.yaml` | `STAGE_BOUNDARY` | `INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `normalize.yaml` | `STAGE_BOUNDARY` | `NORMALIZE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `publish.yaml` | `STAGE_BOUNDARY` | `PUBLISH` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `validate.yaml` | `STAGE_BOUNDARY` | `VALIDATE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |

These are stage boundaries, not parsers, schedules, source connectors, or active consumers.

## Contract and validation

All YAML declarations conform to the shared [pipeline-spec declaration contract](../../contracts/pipeline_spec_declaration.md) and [JSON Schema](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json). Validate from the repository root:

```bash
python tools/validators/validate_pipeline_spec_declarations.py
pytest -q tests/validators/test_validate_pipeline_spec_declarations.py
git diff --check
```

Validation proves declaration shape, closed vocabularies, path resolution, ordering, and digest integrity. It does not prove source admission, temporal fitness, measurement comparability, forecast skill, official authority, evidence, or release readiness.

## Related responsibility families

- Domain meaning: [Atmosphere contracts](../../contracts/domains/atmosphere/README.md)
- Machine shape: [Atmosphere schemas](../../schemas/contracts/v1/domains/atmosphere/README.md)
- Executable behavior: [Atmosphere pipelines](../../pipelines/domains/atmosphere/README.md)
- Exposure rules: [Atmosphere policy](../../policy/domains/atmosphere/README.md)
- Deterministic examples: [Atmosphere fixtures](../../fixtures/domains/atmosphere/README.md)
- Enforcement: [Atmosphere tests](../../tests/domains/atmosphere/README.md)
- Evidence records: [Atmosphere receipts](../../data/receipts/atmosphere/README.md) and [proofs](../../data/proofs/atmosphere/README.md)
- Human coordination: [Atmosphere documentation](../../docs/domains/atmosphere/README.md)
- Release review: [Atmosphere release candidates](../../release/candidates/atmosphere/README.md)

References do not transfer authority into this directory.

## Status and open verification

The lane is reviewable metadata only. Before any declaration can leave `PROPOSED_INACTIVE`, reviewers must verify owners, the Atmosphere-versus-Air compatibility boundary, source admission and rights, knowledge character, units and methods, observation and forecast times, freshness budgets, spatial support, implementation bindings, fixtures, tests, evidence closure, workflow enforcement, and release integration.

No active parser, scheduler, consumer, advisory path, or production binding is asserted here. Unknowns remain denied, and official-source redirection remains mandatory for emergency use.

## Review triggers and rollback

Review is required when a source, stage edge, lifecycle target, schema, implementation, gate, compatibility path, or exposure posture changes. Atmosphere changes also require review when units, methods, station networks, time semantics, freshness, spatial support, forecast horizon, knowledge character, or advisory wording changes.

Rollback is `REVERT_DECLARATION_CHANGE`: revert the declaration commit, rerun validation, and preserve correction or release actions in their authoritative families. Reversion does not retract observations, cancel alerts, or reverse a release by itself.
