<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/hydrology-validation
title: Hydrology bounded validation runbook
type: runbook
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Hydrology and validation stewards
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Hydrology bounded validation runbook; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/domains/hydrology/EXPANSION_BACKLOG.md
  - .github/workflows/domain-hydrology.yml
  - tools/ci/kfm_no_network/README.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Hydrology VALIDATION

Use this runbook to reproduce a focused subset of the repository's no-network
Hydrology validation. The complete workflow remains
[`domain-hydrology.yml`](../../.github/workflows/domain-hydrology.yml); separate
profiles and workflow holds must be read at the exact revision being tested.

## Preconditions and scope

Work from the repository root in the documented Python environment with pytest
and the workflow's required dependencies already installed. Record commit,
Python version, selected profile, commands and outcomes. Dependency installation
and permitted live source capture are separate operations; the validation process
below must load the existing startup egress guard.

The workflow covers synthetic flow/water-level profiles, aquifer observation and
context separation, NHDPlus crosswalk ambiguity, source/schema/catalog adapters,
Living Waters packets and other bounded profiles. Passing a selected subset is
not a complete workflow pass or hydrological truth.

## Start with the process boundary

```bash
export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD"
python -c 'import sitecustomize; assert sitecustomize.GUARD_ACTIVE'
python -m pytest -q -p no:cacheprovider tests/domains/hydrology/test_no_network_proof.py
```

If the guard does not load, stop the fixture run and correct its environment.
Do not drop the guard to make a source-dependent test pass. Use a separate shell
or restore the prior environment after this bounded session.

## Select checks by changed meaning

| Changed meaning | Focused tests or validator |
|---|---|
| Flow role, units, source clocks and geometry | `tests/domains/hydrology/test_public_safe_flow_fixture.py` |
| Water level and datum | `tests/domains/hydrology/test_public_safe_water_level_fixture.py` |
| Observation versus aquifer context | `tests/domains/hydrology/test_aquifer_observation.py`, `test_aquifer_context_link.py` |
| Reach/waterbody ambiguity | `tests/domains/hydrology/test_nhdplus_hr_ambiguity.py` and NHDPlus crosswalk fixtures |
| Living Waters evidence packet | `tests/domains/hydrology/test_living_waters_fixture_packet.py` |
| Cross-domain environmental meaning | `tests/cross_domain/test_environmental_observation_boundaries.py` |
| Source/catalog/schema entry points | Existing adapters under `tools/validators/domains/hydrology/` |

A useful initial semantic subset is:

```bash
python tests/domains/hydrology/test_public_safe_flow_fixture.py --verbose
python tests/domains/hydrology/test_public_safe_water_level_fixture.py --verbose
python -m pytest -q -p no:cacheprovider tests/domains/hydrology/test_aquifer_observation.py tests/domains/hydrology/test_aquifer_context_link.py tests/domains/hydrology/test_nhdplus_hr_ambiguity.py
python tools/validators/domains/hydrology/validate_nhdplus_waterbody_crosswalk.py --fixtures
python tools/validators/domains/hydrology/validate_source_descriptor.py --fixtures
python tools/validators/domains/hydrology/validate_catalog_matrix.py --fixtures
```

Run the full workflow's relevant command set for a wider change. The workflow
also deliberately rejects known-invalid EvidenceBundle, flow, water-level and
ambiguous Living Waters inputs; those nonzero exits are expected negative proof.

## Interpret results without collapsing states

A valid candidate declaration can correctly contain a held or denied outcome.
A workflow step that verifies a missing producer remains held is not an emitted
proof or successful release. Preserve these distinctions in the result record:

- guard and local test execution;
- fixture/schema/semantic conformance;
- exact candidate evidence resolution and source admission;
- policy and accountable review;
- proof producer, release decision, deployment and public acceptance.

## Troubleshooting

| Symptom | Response |
|---|---|
| Missing Python dependency | Restore the pinned environment before assessing code behavior |
| Guard inactive | Check repository-root working directory and startup path |
| Known-invalid fixture accepted | Treat as a regression; inspect expected reason and boundary |
| Flow and level values mixed | Restore quantity/unit/datum and role separation |
| Ambiguous reach join answered | Preserve abstention/hold; do not pick an arbitrary match |
| Workflow hold unexpectedly changes | Inspect newly added artifacts and bind their real validator deliberately |

## Completion and handoff

The validation report must state exactly which profiles ran, positive and
negative outcomes, input/code identity and unresolved holds. A source or runtime
claim needs its own evidence. These tests provide no flood warning, engineering,
regulatory or navigation determination. Revert an incorrect validation change
through normal review; this runbook does not mutate real Hydrology records.
