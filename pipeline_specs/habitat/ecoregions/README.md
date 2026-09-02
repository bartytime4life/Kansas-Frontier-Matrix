<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-habitat-ecoregions-readme
title: pipeline_specs/habitat/ecoregions/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; declarative-only; fail-closed; no-live-activation
owning_root: pipeline_specs/
responsibility: govern inactive declarative pipeline intent for the habitat/ecoregions scope
truth_posture: CONFIRMED inventory and fail-closed posture / PROPOSED declarations / NEEDS VERIFICATION activation prerequisites
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/habitat/ecoregions/README.md
inherited_parent: pipeline_specs/README.md
scope_id: habitat/ecoregions
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# Ecoregion declaration boundary

`pipeline_specs/habitat/ecoregions/` inherits from the [Habitat declaration boundary](../README.md). It reserves a governed seam for inactive regionalization declarations; it does not establish one.

Directory Rules v2 is adopted by [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md). This README applies its `BOUNDARY_COMPACT` profile.

> [!IMPORTANT]
> There are no declarations here. File or directory presence does not activate execution, and all network, source-activation, lifecycle-write, promotion, release, and publication capabilities remain `DENIED`.

> [!CAUTION]
> An ecoregion is a versioned regionalization context, not species occurrence, habitat quality, land-cover truth, regulatory designation, or ownership. Framework, hierarchy, vintage, geometry lineage, scale, and cross-domain join risks must remain explicit.

## Owner and scope

- Local owners: pipeline-spec, Habitat, ecoregion, and spatial-foundation stewards; names remain `OWNER_TBD`.
- Scope ID: `kfm://scope/pipeline-specs/habitat/ecoregions`.
- Local scope: inactive declarations only if a concrete ecoregion pipeline family is reviewed and added.
- Inherited parent: `pipeline_specs/habitat/`.

## Belongs / prohibited

Belongs here:

- future inactive ecoregion pipeline declarations with explicit framework, version, hierarchy, CRS, scale, and source bindings;
- candidate lifecycle edges, required gates, validation commands, and rollback metadata.

Prohibited here:

- executable spatial processing, geometries, tiles, source payloads, credentials, or runtime state;
- semantic contracts, machine schemas, source admission, policy, evidence, catalog, release, or publication authority;
- occurrence claims or sensitive joins inferred from regional context;
- empty symmetry scaffolding beyond this necessary boundary contract.

## Inputs and outputs

- Current inputs: parent governance and repository evidence only.
- Current outputs: none.
- Future candidates may reference admitted regionalization sources and governed lifecycle states; inactive declarations may not fetch or write them.
- Permitted writers: reviewed repository changes only.

## Exposure, mutation, and retention

- Exposure: public boundary metadata only; examples must avoid reconstructable sensitive joins.
- Mutation: framework, version, hierarchy, crosswalk, CRS, geometry lineage, scale, or exposure changes require domain and spatial review.
- Retention: version-control history and reviewed supersession lineage.
- The retained `.gitkeep` is a zero-byte topology marker with no declaration or execution authority.

## Current direct-child map

```text
pipeline_specs/habitat/ecoregions/
├── .gitkeep                        # Topology marker; no authority
└── README.md                       # Boundary contract; no declarations
```

## Declaration inventory

No YAML or JSON declaration exists directly in this directory.

| Count | Object type | Status |
|---:|---|---|
| 0 | `KfmPipelineSpecDeclaration` | No declaration established |
| 0 | Schema-specific JSON profile | No profile established |

If a YAML declaration is later admitted, it must use `KfmPipelineSpecDeclaration`, begin at `PROPOSED_INACTIVE / NOT_IMPLEMENTED`, and retain all execution and authority denials.

## Safety posture

- A regional boundary never activates a source or executable consumer.
- Context joins retain owning-domain semantics, time, rights, sensitivity, and release state.
- Passing topology or schema validation is not evidence closure or publication approval.
- Public outputs require independent policy, evidence, review, and release decisions.

## Validation

Run repository-wide checks from the repository root:

```bash
python tools/validators/validate_pipeline_spec_declarations.py
python -m pytest tests/validators/test_validate_pipeline_spec_declarations.py -q
```

Also verify direct-child inventory, absence of payloads, and any future framework-, hierarchy-, CRS-, topology-, or join-specific negative fixtures.

## Related authority families

- Common semantics: [`contracts/pipeline_spec_declaration.md`](../../../contracts/pipeline_spec_declaration.md)
- Common shape: [`schemas/contracts/v1/pipeline_spec_declaration.schema.json`](../../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Habitat / ecoregion contracts: `contracts/domains/habitat/`
- Habitat policy: `policy/domains/habitat/`
- Habitat fixtures / tests: `fixtures/domains/habitat/`, `tests/domains/habitat/`
- Executable consumers: `pipelines/domains/habitat/ecoregions/`
- Release candidates: `release/candidates/habitat/`; this boundary cannot authorize them

## Status and open verification

- Status: repository-grounded, empty, and inactive.
- Verify whether a distinct ecoregion declaration family is needed before adding files.
- Verify canonical framework and hierarchy vocabularies, source roles, rights, temporal semantics, CRS, topology, public attributes, and join policy.
- Verify named owners and executable, fixture, test, workflow, evidence, and release families before activation is proposed.

## Review triggers and rollback

Re-review when a declaration, owner, framework, hierarchy, source, geometry, CRS, scale, join, exposure, consumer, workflow, or governing ADR changes.

Rollback is a reviewed revert. If a future declaration lacks authority or evidence, remove or revert that bounded change, retain inactivity, restore all denials, and quarantine any derived candidate outside this directory.
