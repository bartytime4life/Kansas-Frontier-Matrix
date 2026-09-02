<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/verification
title: Soil Verification Status and Reproduction Guide
type: domain-verification-index
version: v1.0.0
status: draft; repository-grounded; bounded-executable-evidence; release-held
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - validation steward
  - OWNER_TBD - evidence and policy steward
created: 2026-05-19
updated: 2026-08-28
policy_label: public
owning_root: docs/
responsibility: Human-readable Soil verification status, reproduction commands, evidence limits, and remaining holds
truth_posture: CONFIRMED current repository paths, 42 direct focused tests, and 180 broader Soil tests plus 140 subtests at the pinned base / NEEDS VERIFICATION hosted exact-head results, repository-wide suite state, source admission, scientific fitness, policy approval, release, deployment, and publication
related:
  - docs/domains/soil/README.md
  - docs/domains/soil/EXPANSION_BACKLOG.md
  - docs/domains/soil/CATALOG_CLOSURE.md
  - docs/runbooks/soil/README.md
  - contracts/domains/soil/README.md
  - schemas/contracts/v1/domains/soil/README.md
  - fixtures/domains/soil/README.md
  - tools/validators/domains/soil/README.md
  - tests/domains/soil/README.md
  - .github/workflows/domain-soil.yml
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, soil, verification, no-network, fixtures, validators, tests, evidence, hold]
notes:
  - "Repository evidence snapshot: main@249974ba480fd68dc749ad0258c84e09477d523a."
  - "Focused local validation on 2026-08-28: 16 public-safe fixture tests, 12 station-moisture tests, and 14 SMAP L4 anti-collapse tests passed with KFM_NO_NETWORK=1."
  - "Broader local Soil validation on 2026-08-28: 180 tests and 140 subtests passed across tests/domains/soil, tests/validators/domains/soil, and tests/pipelines/domains/soil with KFM_NO_NETWORK=1."
  - "Planning lineage: KFM Soil Architecture Extended Pro PDF-Only Planning Report, SHA-256 7c2d498212b9ad56f3ba37bf91f841e9f328794e8aa4940f8f665a4116c5aaea."
  - "The planning report had no mounted repository; it remains proposal lineage and does not upgrade implementation or release state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil verification status and reproduction guide

This document replaces the former greenfield scaffold with a bounded,
repository-grounded verification surface. It records what was observed and run
at a pinned repository state, what those results prove, and what remains held.

> [!IMPORTANT]
> A passing fixture or schema test is QA evidence for its declared profile. It is
> not source admission, scientific validation, an EvidenceBundle, a policy
> decision, a promotion decision, a release, a deployment, or publication.

## Current determination

| Field | Result |
|---|---|
| Repository snapshot | `main@249974ba480fd68dc749ad0258c84e09477d523a` |
| Verification performed | Three direct focused suites plus the bounded Soil domain, validator, and pipeline test subset |
| Direct focused result | `42 passed / 0 failed` |
| Broader Soil subset | `180 passed / 140 subtests passed / 0 failed` |
| Network posture | `KFM_NO_NETWORK=1`; the suites include checks that reject attempted network access |
| Hosted checks | `NEEDS VERIFICATION` for the future PR head; local results do not predict hosted status |
| Source state | No source was contacted, admitted, activated, or refreshed |
| Lifecycle state | No RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED state was written |
| Public state | Release, deployment, promotion, and publication remain `HOLD` |

## Evidence basis

The verification order for this document is:

1. current repository files at the pinned commit;
2. deterministic local command output from the same checkout;
3. accepted Directory Rules and ADRs for placement and authority boundaries;
4. current domain documentation for orientation; and
5. the attached Soil planning report only as proposal lineage.

The planning report proposed an eight-PR sequence after explicitly finding no
mounted repository. The current repository has already implemented several
bounded fixture, schema, validator, and workflow candidates beyond that report's
knowledge. This document therefore does not copy the proposed sequence or paths
as current authority.

## Focused executable proof

| Profile | Executable boundary | Focused test | Result in this session | Proven scope |
|---|---|---|---:|---|
| Public-safe Soil fixture | [`validate_public_safe_fixture.py`](../../../tools/validators/domains/soil/validate_public_safe_fixture.py) | [`test_soil_smoke.py`](../../../tests/domains/soil/test_soil_smoke.py) | 16 passed | Closed synthetic profile, exact negative sidecars, deterministic non-echoing findings, bounded parsing, and no-network behavior |
| Station Soil moisture | [`validate_soil_moisture.py`](../../../tools/validators/domains/soil/moisture/validate_soil_moisture.py) | [`test_soil_moisture_qc.py`](../../../tests/domains/soil/test_soil_moisture_qc.py) | 12 passed | Frozen station profile for UTC, unit, depth, QC, dedupe, parser bounds, and no-network behavior |
| SMAP L4 anti-collapse | [`validate_smap_l4_fixture.py`](../../../tools/validators/domains/soil/moisture/validate_smap_l4_fixture.py) | [`test_smap_l4_anti_collapse.py`](../../../tests/domains/soil/test_smap_l4_anti_collapse.py) | 14 passed | Separate satellite-grid profile, temporal/hash bounds, support-type anti-collapse, exact negative sidecars, and no-network behavior |

The result is exact for these three commands at the pinned checkout. It does not
cover every Soil validator, workflow, schema, contract, fixture, package,
pipeline, application surface, or external source.

The broader Soil subset was also run with the same no-network posture:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m pytest -q \
  tests/domains/soil \
  tests/validators/domains/soil \
  tests/pipelines/domains/soil
```

It reported `180 passed, 140 subtests passed`. This remains a selected Soil
subset, not the repository-wide test suite.

## Reproduction commands

Run from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/soil/test_soil_smoke.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/soil/test_soil_moisture_qc.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/soil/test_smap_l4_anti_collapse.py --verbose
```

Record the exact commit, command, environment, fixture inventory, passed and
failed counts, skipped checks, and output classification when reproducing these
results. Do not summarize an unrun or changed-head command as passed.

## Additional repository-grounded inventory

The following surfaces are present at the pinned base. Presence is confirmed;
execution is not implied unless the row says it was run above.

| Responsibility | Current surface | Current bounded status |
|---|---|---|
| Semantic meaning | [`contracts/domains/soil/`](../../../contracts/domains/soil/README.md) | Multiple substantive candidate contracts, including map-unit, component, observation, identity, support-type, time-caveat, watcher, and catalog-closure profiles |
| Machine shape | [`schemas/contracts/v1/domains/soil/`](../../../schemas/contracts/v1/domains/soil/README.md) | Multiple draft JSON Schemas paired with focused fixtures and validators; active or canonical adoption remains profile-specific |
| Synthetic replay inputs | [`fixtures/domains/soil/`](../../../fixtures/domains/soil/README.md) | Positive and negative fixtures exist for public-safe, moisture, SMAP L4, identity, support-type, time-caveat, watcher, and selected object-family profiles |
| Validator implementation | [`tools/validators/domains/soil/`](../../../tools/validators/domains/soil/README.md) | Bounded executables exist for several profiles; validator output remains non-authoritative QA |
| Tests | [`tests/domains/soil/`](../../../tests/domains/soil/README.md) and [`tests/validators/domains/soil/`](../../../tests/validators/domains/soil/) | Focused executable suites coexist with several explicit documentation-only placeholder modules |
| Fixture-only pipelines | [`pipelines/domains/soil/`](../../../pipelines/domains/soil/README.md) | Mesonet normalizer and station-health fixture executables exist; top-level lifecycle Python modules remain greenfield placeholders |
| Policy posture | [`policy/domains/soil/`](../../../policy/domains/soil/README.md) | Draft fail-closed rules exist; policy adoption and operational enforcement remain separate questions |
| Source registry | [`data/registry/sources/soil/`](../../../data/registry/sources/soil/README.md) | Accepted canonical writer path contains proposal placeholders; no inspected record proves source activation |
| Generated run memory | [`data/receipts/soil/`](../../../data/receipts/soil/README.md) | Documentation and generated receipts exist; receipts do not become proofs or release decisions |
| Workflow orchestration | [`.github/workflows/domain-soil.yml`](../../../.github/workflows/domain-soil.yml) plus focused Soil workflows | Command-bearing definitions exist; exact-head hosted results must be observed separately |

## Verification limits and holds

The following states remain unproven or deliberately held:

- live source availability, identity, version, terms, rights, attribution, and
  activation;
- scientific fitness for a real Kansas claim, including scale, support,
  resolution, uncertainty, temporal interpretation, and correction behavior;
- compatibility closure between historical Soil contract, schema, registry,
  fixture, and test path variants;
- repository-wide suite and hosted exact-head status for a future pull request;
- operational policy evaluation, accountable steward review, evidence closure,
  proof production, catalog write, promotion, rollback execution, release,
  deployment, and publication; and
- public MapLibre, governed API, Evidence Drawer, Focus Mode, graph, export, or
  AI behavior backed by a released Soil carrier.

Missing evidence produces `HOLD`, `ABSTAIN`, `DENY`, or `ERROR` according to the
owning contract. It never becomes implicit approval.

## Next verification work

The dependency-ordered work queue is maintained in
[`EXPANSION_BACKLOG.md`](EXPANSION_BACKLOG.md). The smallest next verification
slice should close one already paired contract-schema-fixture-validator-test
profile or reconcile one explicit compatibility boundary. It should not enable a
live connector or public surface as a side effect.

## Directory Rules basis

This file remains under `docs/domains/soil/` because it owns human-readable
domain verification status. Semantic contracts remain under `contracts/`,
machine shapes under `schemas/`, fixtures under `fixtures/`, executable tests
under `tests/`, validators under `tools/validators/`, source records and lifecycle
data under `data/`, and release decisions under `release/`. No parallel authority
home is created.

See the [accepted Directory Rules](../../doctrine/directory-rules.md) and
[`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md).

## Rollback

Rollback is an ordinary Git revert of this documentation change. Reverting this
file does not revert executable Soil profiles, source state, lifecycle state,
policy, proof, release, deployment, or publication because this document changes
none of those states.
