<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-hazards-readme
title: pipeline_specs/hazards/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; declarative-only; fail-closed; no-live-activation
owning_root: pipeline_specs/
responsibility: govern inactive declarative pipeline intent for the hazards scope
truth_posture: CONFIRMED inventory and fail-closed posture / PROPOSED declarations / NEEDS VERIFICATION activation prerequisites
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/hazards/README.md
inherited_parent: pipeline_specs/README.md
scope_id: hazards
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# Hazards pipeline declaration boundary

`pipeline_specs/hazards/` is the declarative Hazards lane inherited from [`pipeline_specs/`](../README.md). It records inactive proposals for bounded processing, never live warning or emergency-response authority.

Directory Rules v2 is adopted by [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md). This README applies its `BOUNDARY_COMPACT` profile.

> [!IMPORTANT]
> File presence does not activate execution. All declarations are `PROPOSED_INACTIVE / NOT_IMPLEMENTED`; network access, source activation, lifecycle writes, promotion, release, publication, and public alerting remain `DENIED`.

> [!CAUTION]
> Hazard feeds are time-, source-, coverage-, and correction-dependent context. They are not emergency instructions, forecasts, legal determinations, or proof of current exposure. Never delay or replace official alerts; restricted infrastructure, household, health, or vulnerability joins fail closed.

## Owner and scope

- Local owners: pipeline-spec and Hazards stewards; names remain `OWNER_TBD`.
- Scope ID: `kfm://scope/pipeline-specs/hazards`.
- Local authority: inactive stage and source candidates, references, lifecycle edges, and gates.
- Inherited authority: trust, evidence, public boundary, correction, and rollback controls from the parent.

## Belongs / prohibited

Belongs here:

- inactive Hazards stage boundaries and source-specific candidates;
- explicit source, contract, schema, fixture, test, workflow, policy, and gate references;
- disabled execution, finite reason codes, non-effects, and rollback metadata.

Prohibited here:

- live polling, alert delivery, forecasting, incident command, or executable processing;
- credentials, endpoints, source payloads, personal records, or sensitive vulnerability detail;
- source admission, hazard truth, policy, evidence, catalog, promotion, release, or publication authority;
- claims of current safety, risk, exposure, impact, eligibility, or official warning status.

## Inputs and outputs

- Candidate inputs: source captures and governed lifecycle references appropriate to ingest, derive, validate, catalog, or publish review.
- Candidate outputs: possible `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, catalog, or release candidates; inactive declarations write none.
- Permitted writers: reviewed repository changes only; no runtime or notification writer is authorized here.
- Source observation, valid, issue, retrieval, and correction times must remain distinguishable.

## Exposure, mutation, and retention

- Exposure: public configuration metadata only; examples must be synthetic and non-operational.
- Mutation: source, cadence, geography, time, severity, threshold, join, or output changes require safety review.
- Retention: version-control history and reviewed supersession / correction lineage.
- Physical observations, alerts, model outputs, and personal or infrastructure payloads are prohibited.

## Current direct-child map

```text
pipeline_specs/hazards/
├── README.md                       # This boundary contract
├── catalog.yaml                    # Inactive CATALOG boundary
├── drought_monitor.yaml            # Inactive drought ingest candidate
├── exposure_resilience_rollup.yaml # Inactive derivation candidate
├── fema_nfhl.yaml                  # Inactive NFHL ingest candidate
├── fema_openfema.yaml              # Inactive OpenFEMA ingest candidate
├── ingest.yaml                     # Inactive INGEST boundary
├── nasa_firms.yaml                 # Inactive FIRMS ingest candidate
├── noaa_hms_smoke.yaml             # Inactive smoke ingest candidate
├── noaa_storm_events.yaml          # Inactive storm-events ingest candidate
├── normalize.yaml                  # Inactive NORMALIZE boundary
├── nws_alerts_context.yaml         # Inactive alerts-context ingest candidate
├── publish.yaml                    # Inactive PUBLISH boundary
├── usgs_earthquake.yaml            # Inactive earthquake ingest candidate
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
| `drought_monitor.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `fema_nfhl.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `fema_openfema.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `nasa_firms.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `noaa_hms_smoke.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `noaa_storm_events.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `nws_alerts_context.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `usgs_earthquake.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `exposure_resilience_rollup.yaml` | `PIPELINE_CANDIDATE / DERIVE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |

All fourteen YAML files use `KfmPipelineSpecDeclaration` and retain explicit safety denials.

## Validation

```bash
python tools/validators/validate_pipeline_spec_declarations.py
python -m pytest tests/validators/test_validate_pipeline_spec_declarations.py -q
```

Validation must reject active status, permissive execution, duplicate keys, aliases, unknown fields, invalid paths or hashes, and missing bindings. Domain review must also test stale, missing, corrected, contradictory, out-of-coverage, and sensitive-join cases.

## Related authority families

- Common semantics: [`contracts/pipeline_spec_declaration.md`](../../contracts/pipeline_spec_declaration.md)
- Common shape: [`schemas/contracts/v1/pipeline_spec_declaration.schema.json`](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Hazards contracts / policy: `contracts/domains/hazards/`, `policy/domains/hazards/`
- Hazards fixtures / tests: `fixtures/domains/hazards/`, `tests/domains/hazards/`
- Executable consumers: `pipelines/domains/hazards/`
- Release candidates: `release/candidates/hazards/`; declarations confer no release or alert authority

## Status and open verification

- Status: repository-grounded, declarative-only, and inactive.
- Verify named owners, official-source roles, rights, coverage, temporal semantics, correction behavior, severity vocabularies, and no-alerting posture.
- Verify exposure and resilience joins preserve uncertainty, prevent re-identification, and cannot be mistaken for household- or facility-level current risk.
- Verify each implementation, fixture, test, workflow, and release reference before changing implementation status.

## Review triggers and rollback

Re-review on owner, source, endpoint, cadence, geography, time, severity, threshold, join, consumer, exposure, workflow, schema, correction, or governing ADR change.

Rollback is a reviewed revert. Retain `PROPOSED_INACTIVE`, restore all denials, quarantine derived candidates, withdraw misleading outputs through the proper authority, and never treat rollback here as an emergency-notification mechanism.
