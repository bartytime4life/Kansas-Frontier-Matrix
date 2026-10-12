<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/cross-lanes
title: Soil cross-domain handoffs
type: domain-guide
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Soil cross-domain handoffs; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/domains/soil/DATA_LIFECYCLE.md
  - tests/cross_domain/soil_agriculture/test_public_safe_context.py
  - tests/cross_domain/soil_hydrology/test_public_safe_context.py
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# CROSS LANES

Soil contributes context to other domains while preserving the meaning and
limits of each input. A spatial join does not transfer source authority, improve
resolution or prove causation. Use this guide with the
[Soil lifecycle](DATA_LIFECYCLE.md) and each receiving domain's contract.

## Handoff matrix

| Receiving lane | Useful Soil contribution | Keep separate |
|---|---|---|
| Agriculture | Soil properties, moisture context and method-bound suitability | Crop/yield observations, farmer decisions, private field identities |
| Hydrology | Hydrologic soil group, infiltration and moisture context | Flow, water level, aquifer context, flood forecast and operational warning |
| Geology | Parent-material context and near-surface profile references | Lithology, borehole intervals, bedrock continuity and resource interpretation |
| Flora/Fauna/Habitat | Reviewed soil support and environmental context | Species observations, taxonomic status, habitat evidence and protected locations |
| Hazards | Inputs to a separately reviewed derivative | Hazard assessment, warning, evacuation and engineering authority |
| People/DNA/Land | Generalized public-safe context | Ownership, title, identity, private parcel or consented relationships |

## Executable bounded pair profiles

The [Soil–Agriculture tests](../../../tests/cross_domain/soil_agriculture/test_public_safe_context.py)
and [Soil–Hydrology tests](../../../tests/cross_domain/soil_hydrology/test_public_safe_context.py)
exercise synthetic relation candidates. Their valid output remains
`JOIN_CANDIDATE` with output role `CANDIDATE_RELATION` and all effects false.

They cover generalized geometry, missing evidence, modeled-role review,
restricted precision and a wrong relation profile. The Agriculture profile
rejects private parcel precision. The Hydrology profile also rejects an
operational or causal claim. A validator can report `PASS` because a fixture
correctly declares `DENY`; read the candidate decision and findings together.

```bash
python -m pytest -q -p no:cacheprovider tests/cross_domain/soil_agriculture/test_public_safe_context.py tests/cross_domain/soil_hydrology/test_public_safe_context.py
```

These fixtures contain no actual coordinate payload and establish no production
join, live evidence resolution or publication.

## Handoff procedure

1. Identify both exact source artifacts, domains, support types and source roles.
2. Record native identifiers, geography/scale, time window, units, depth and
   uncertainty. Explain any resampling or aggregation explicitly.
3. Define the intended relation and output claim. Reject claims that require
   information absent from either input.
4. Review combined sensitivity: a public Soil record can become sensitive when
   joined to a private parcel, protected species or person-linked observation.
5. Bind evidence, method and correction targets for both sides. Missing support
   yields abstention or a held candidate.
6. Run the matching profile and its negative cases. Route scientific and domain
   review separately from schema conformance.
7. Release only through the receiving product's governed carrier and review path.

## Troubleshooting

A scale mismatch needs a declared method or a narrower claim, not an interpolated
certainty. A date mismatch needs a source-time caveat, not a renamed timestamp.
An exact geometry rejected by a public-safe profile must be reviewed or
transformed by an authorized process; changing the label to “generalized” does
not alter the geometry. Unresolved modeled/observed role conflicts stay visible.

## Completion criteria

The handoff is reviewable when each input's meaning survives the join, sensitive
combinations are handled, expected failures are tested and both domains can
trace corrections to dependents. The relation assessment and release decision
remain separate. Other cross-domain rows above describe review expectations;
they do not claim equivalent executable profiles already exist.
