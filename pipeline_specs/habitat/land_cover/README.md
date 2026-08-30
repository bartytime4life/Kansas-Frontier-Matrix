<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-habitat-land-cover-readme
title: pipeline_specs/habitat/land_cover/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; declarative-only; fail-closed; no-live-activation
owning_root: pipeline_specs/
responsibility: govern inactive declarative pipeline intent for the habitat/land_cover scope
truth_posture: CONFIRMED inventory and fail-closed posture / PROPOSED declarations / NEEDS VERIFICATION activation prerequisites
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/habitat/land_cover/README.md
inherited_parent: pipeline_specs/README.md
scope_id: habitat/land_cover
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# Land-cover declaration boundary

`pipeline_specs/habitat/land_cover/` inherits from the [Habitat declaration boundary](../README.md). It owns the inactive land-cover materiality profile, not executable comparison or release authority.

Directory Rules v2 is adopted by [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md). This README applies its `BOUNDARY_COMPACT` profile.

> [!IMPORTANT]
> The JSON profile is `PROPOSED_INACTIVE`. File presence, a crossed threshold, or passing validation activates no execution; network access, lifecycle writes, promotion, release, and publication remain denied.

> [!CAUTION]
> A land-cover class is a source-, method-, resolution-, and vintage-dependent representation. It is not parcel use, ownership, legal designation, habitat quality, species occurrence, wetland jurisdiction, or current ground condition.

## Owner and scope

- Local owners: pipeline-spec, Habitat, land-cover, and spatial-foundation stewards; names remain `OWNER_TBD`.
- Scope ID: `kfm://scope/pipeline-specs/habitat/land-cover`.
- Local authority: inactive materiality thresholds and governance flags for the established profile family.
- Inherited parent: `pipeline_specs/habitat/`.

## Belongs / prohibited

Belongs here:

- schema-backed, inactive land-cover materiality profiles;
- deterministic threshold configuration, identity, canonical hash, and explicit governance denials;
- future YAML declarations only under the common declaration contract.

Prohibited here:

- executable raster processing, source payloads, classified pixels, tiles, models, or runtime state;
- silent threshold activation or inference of ecological, regulatory, or property truth;
- source admission, policy, evidence, catalog, promotion, release, or publication authority;
- credentials, restricted data, or reconstructable sensitive joins.

## Inputs and outputs

- Candidate inputs: governed land-cover comparison summaries produced elsewhere; this profile fetches nothing.
- Candidate outputs: a threshold evaluation may inform a material-change candidate, never a lifecycle write or release.
- Permitted writers: reviewed repository changes only.
- Any executable consumer remains under `pipelines/` or `tools/` and must enforce the profile's inactive governance flags.

## Exposure, mutation, and retention

- Exposure: public configuration metadata; no payloads or sensitive joins.
- Mutation: threshold, unit, analysis unit, combination rule, schema, or hash changes require fixture-backed review.
- Retention: version-control history and explicit profile-version / supersession lineage.
- The retained `.gitkeep` is a zero-byte topology marker with no profile or execution authority.

## Current direct-child map

```text
pipeline_specs/habitat/land_cover/
├── .gitkeep                        # Topology marker; no authority
├── README.md                       # This boundary contract
└── materiality_profile.v1.json     # Inactive schema-specific profile
```

## Declaration inventory

| Declaration | Object type | Status | Implementation posture |
|---|---|---|---|
| `materiality_profile.v1.json` | `LandCoverMaterialityProfile` | `PROPOSED_INACTIVE` | Governance flags deny activation, promotion, and public use |

There are no YAML declarations directly in this directory. The parent `pipeline_specs/habitat/nlcd_landcover.yaml` is a separate `KfmPipelineSpecDeclaration` candidate and does not inherit authority from this profile.

The JSON object retains its existing schema-specific contract, validator, canonicalization, and `spec_hash`; it is not silently converted to `KfmPipelineSpecDeclaration`.

## Safety posture

- Threshold crossing is a review signal, not material-change truth or publication authority.
- Source version, retrieval time, classification legend, resolution, CRS, analysis unit, and uncertainty remain explicit.
- Cross-domain joins preserve owning-domain sensitivity and cannot reconstruct protected locations.
- File presence does not activate execution; writes, network, promotion, release, and publication remain denied.

## Validation

Run the established land-cover profile validator/tests and the repository-wide declaration checks from the repository root. At minimum:

```bash
python tools/validators/validate_pipeline_spec_declarations.py
python -m pytest tests/validators/test_validate_pipeline_spec_declarations.py -q
```

Validation must include schema conformance, deterministic hash verification, valid/invalid threshold fixtures, governance-denial checks, and negative cases for invalid units, bounds, and unknown fields.

## Related authority families

- Common YAML semantics: [`contracts/pipeline_spec_declaration.md`](../../../contracts/pipeline_spec_declaration.md)
- Common YAML shape: [`schemas/contracts/v1/pipeline_spec_declaration.schema.json`](../../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Habitat contracts / policy: `contracts/domains/habitat/`, `policy/domains/habitat/`
- Habitat fixtures / tests: `fixtures/domains/habitat/`, `tests/domains/habitat/`
- Executable consumers: `pipelines/domains/habitat/`
- Release candidates: `release/candidates/habitat/`; this profile cannot authorize them

## Status and open verification

- Status: repository-grounded and `PROPOSED_INACTIVE`.
- Verify named owners, current source/version bindings, accepted legend and unit vocabularies, validator/workflow enforcement, and hash reproducibility.
- Verify that materiality review cannot bypass evidence, policy, independent review, or release decisions.
- Verify correction propagation when a source revision, classification correction, or profile supersession occurs.

## Review triggers and rollback

Re-review on owner, threshold, unit, analysis unit, combination rule, source, legend, vintage, CRS, resolution, consumer, schema, validation, exposure, or governing ADR change.

Rollback is a reviewed revert to the last validated profile and hash. Keep the profile inactive, restore governance denials, invalidate derived candidates when needed, and retain correction evidence outside this directory.
