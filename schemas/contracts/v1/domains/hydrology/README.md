# `schemas/contracts/v1/domains/hydrology/` — Hydrology schema index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-hydrology-readme
title: schemas/contracts/v1/domains/hydrology/ — Hydrology Domain Schema Index
version: v2
status: draft; mixed implementation posture
policy_label: public
owners:
  - <schema-steward>
  - <hydrology-domain-steward>
updated: 2026-07-30
tags: [kfm, schemas, contracts, hydrology, json-schema, aquifer-observation, aquifer-context-link]
[/KFM_META_BLOCK_V2] -->

This is the canonical machine-shape lane for Hydrology domain contracts.
Semantic meaning remains under `contracts/domains/hydrology/`; policy,
validators, fixtures, lifecycle data, proof, and release records remain in
their own responsibility roots.

> [!IMPORTANT]
> Schema presence is not source admission, evidence closure, scientific
> correctness, policy approval, proof, release, or publication authority.

## Current posture

The lane contains a mix of closed bounded schemas, shared-schema aliases,
minimal or permissive scaffolds, and support schemas without same-name
Hydrology contract children. Callers must inspect the individual schema and
must not describe the whole lane as schema-complete.

The `AquiferObservation` decision adopts a separated pair:

| Schema | Responsibility | Bounded support |
|---|---|---|
| [`aquifer_observation.schema.json`](./aquifer_observation.schema.json) | Observed groundwater-level or aquifer-state measurement | Closed shape; linked and unlinked valid fixtures; role and embedded-Geology negative fixtures; dedicated offline validator/tests |
| [`aquifer_context_link.schema.json`](./aquifer_context_link.schema.json) | Typed relation from Hydrology observation/well to Geology `HydrostratigraphicUnit` | Closed shape; observation/well valid fixtures; endpoint, measurement-collapse, and copied-geometry negative fixtures; dedicated offline validator/tests |

Both are `PROPOSED`. Their tests establish shape and fixture polarity only.

## Contract-paired inventory

| Shape class | Count | Schema files |
|---|---:|---|
| Closed bounded schemas | 2 | `aquifer_observation`, `aquifer_context_link` |
| Shared-schema aliases | 3 | `decision_envelope`, `evidence_bundle`, `run_receipt` |
| Minimal open envelopes | 4 | `domain_feature_identity`, `domain_layer_descriptor`, `domain_observation`, `domain_validation_report` |
| Permissive empty-property scaffolds | 11 | `flow_observation`, `gauge_site`, `groundwater_well`, `huc_unit`, `hydro_feature`, `hydrograph`, `nfhl_zone`, `reach_identity`, `water_level_observation`, `water_quality_observation`, `watershed` |
| Missing contract-declared schemas | 4 | `drought_link`, `irrigation_link`, `upstream_trace`, `water_use_link` |

These counts cover the 24 direct child semantic contracts indexed by
`contracts/domains/hydrology/README.md`.

## Other schema files in this lane

The following files exist but do not have a same-name direct child semantic
contract in `contracts/domains/hydrology/`:

- `catalog_matrix.schema.json`
- `correction_notice.schema.json`
- `evidence_drawer_payload.schema.json`
- `hydro-crosswalk-manifest.schema.json`
- `layer_manifest.schema.json`
- `promotion_decision.schema.json`
- `release_manifest.schema.json`
- `rollback_card.schema.json`
- `source_state_hash.schema.json`

Their placement and pairing remain separate review work. This index does not
promote them or create parallel semantic authority.

## Aquifer pair dependencies

| Responsibility | Observation | Context link |
|---|---|---|
| Contract | `contracts/domains/hydrology/aquifer_observation.md` | `contracts/domains/hydrology/aquifer_context_link.md` |
| Fixtures | `fixtures/domains/hydrology/aquifer_observation/` | `fixtures/domains/hydrology/aquifer_context_link/` |
| Validator | `tools/validators/domains/hydrology/validate_aquifer_observation.py` | `tools/validators/domains/hydrology/validate_aquifer_context_link.py` |
| Tests | `tests/domains/hydrology/test_aquifer_observation.py` | `tests/domains/hydrology/test_aquifer_context_link.py` |
| CI | `.github/workflows/domain-hydrology.yml` | `.github/workflows/domain-hydrology.yml` |

## Compatibility rules

- Keep each published `$id` stable.
- Do not redirect either aquifer `$id` to the other type or to a permissive
  replacement schema.
- Additive optional fields require positive and negative fixture review.
- Required-field, enum, relationship, identity, or no-data changes require
  explicit migration and consumer review.
- A combined legacy payload migrates to one measurement record plus zero or
  more relation records.
- An observation without an aquifer link stays schema-valid; a consumer making
  an aquifer-specific claim must resolve the separate link or abstain.

Rollback the two aquifer schemas together with their contracts, fixtures,
validators, tests, workflow inventory, and catalog references. A partial
rollback would recreate the ambiguity this pair resolves.

## Non-goals and holds

This index and the bounded schemas do not:

- validate endpoint existence or real-world aquifer membership;
- copy or redefine Geology identity or geometry;
- admit groundwater sources or normalize production data;
- resolve EvidenceRefs or apply rights and sensitivity policy;
- build proof, approve release, deploy, or publish;
- upgrade the remaining Hydrology scaffolds.

## Review checklist

- [ ] Stable `$id` and Draft 2020-12 declaration.
- [ ] Paired semantic contract.
- [ ] Closed shape or documented reason for openness.
- [ ] Public-safe valid and expected-invalid fixtures.
- [ ] Offline validator and tests with fixture polarity.
- [ ] Compatibility and correction behavior.
- [ ] Policy, source, evidence, proof, and release limitations stated.
