<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-maplibre-readme
title: tests/maplibre/ — MapLibre Boundary and Readiness Tests
type: readme; directory-readme; test-lane-index
version: v0.4
status: draft; repository-grounded; executable-no-network-coverage; runtime-performance-hold
policy_label: public-doc; renderer-boundary; non-authoritative
owners: OWNER_TBD
created: 2026-07-06
updated: 2026-08-30
current_path: tests/maplibre/README.md
truth_posture: CONFIRMED six direct Python test modules, 83 source-defined tests, a package-owned exact MapLibre GL JS 6.6.0 dependency, accepted renderer-boundary ADRs, deterministic no-network workflow coverage, and retired legacy CDN harness / HOLD browser performance, visual-diff, proof, release, deployment, and publication claims / UNKNOWN required-check status, production parity, complete consumer migration, accountable stewardship, and operational rollback
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: e65f9b1cdccbc9c81a911bc1a6d0a10a094bf73f
related:
  - ../README.md
  - ../../packages/maplibre/README.md
  - ../../docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md
  - "../../docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
  - ../../.github/workflows/maplibre-perf-governance.yml
  - ../../.github/workflows/maplibre-acquisition-inventory.yml
  - ../../.github/workflows/briefing-implementation-campaign.yml
  - ../../.github/workflows/maplibre-source-metadata.yml
tags: [kfm, tests, maplibre, renderer-boundary, readiness, no-network, hold]
notes:
  - "This README indexes executable evidence. Tests, workflow conclusions, fixtures, rendered output, and documentation are not release or publication authority."
  - "The retired performance harness exits with a finite HOLD and performs no renderer, browser, network, screenshot, receipt, proof, or artifact acquisition."
[/KFM_META_BLOCK_V2] -->

# `tests/maplibre/` — MapLibre Boundary and Readiness Tests

This lane checks KFM's MapLibre dependency boundary, package exports, candidate
readiness, retired performance harness, and synthetic performance constraints.
It does not prove browser performance, visual parity, production behavior,
release eligibility, or publication safety.

The current repository state is intentionally split:

- the renderer family and package-owned acquisition seam are accepted;
- `packages/maplibre/` owns exact `maplibre-gl` `6.6.0` dependency closure;
- structural and fixture-only checks are executable without network access; and
- runtime performance, render comparison, proof, release, and publication remain
  on explicit `HOLD`.

## Authority and placement

Accepted [Directory Rules](../../docs/doctrine/directory-rules.md) classify
`tests/` as the canonical responsibility root for executable conformance,
boundary, negative, integration, and end-to-end evidence. This directory owns
root-level MapLibre boundary and readiness tests. Package-owned TypeScript tests
remain under [`packages/maplibre/tests/`](../../packages/maplibre/tests/).

Architecture authority comes from:

- [ADR-0006](../../docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md),
  which accepts `packages/maplibre/` as the sole reusable browser-renderer
  acquisition seam; and
- [ADR-0007](<../../docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md>),
  which accepts MapLibre GL JS as the sole normal browser renderer family.

Acceptance of those decisions does not by itself prove implementation
conformance, runtime readiness, release, deployment, promotion, or publication.

## Implemented inventory

The six test modules define 83 test functions or `unittest` methods in source.
The count describes the checked-in source, not a hosted collection receipt.

| Module | Source-defined tests | What it checks | Hosted binding |
| --- | ---: | --- | --- |
| [`test_assess_acquisition_inventory.py`](test_assess_acquisition_inventory.py) | 49 | Renderer imports, re-exports, globals, CDN assets, package homes, manifest errors, input budgets, symlink/path confinement, mutation races, and summary redaction | [`maplibre-acquisition-inventory.yml`](../../.github/workflows/maplibre-acquisition-inventory.yml) runs the full module and current-repository scan |
| [`test_validate_v6_readiness.py`](test_validate_v6_readiness.py) | 16 | Exact-version ownership, duplicate/floating dependencies, import boundaries, probe posture, upstream tag identity, and declared-versus-computed outcomes | [`briefing-implementation-campaign.yml`](../../.github/workflows/briefing-implementation-campaign.yml) runs the module, fixture polarity, and current-repository scan |
| [`test_legacy_perf_harness_retirement.py`](test_legacy_perf_harness_retirement.py) | 3 | Finite retirement outcome, absence of renderer/network acquisition, and confinement of current acquisition to the package seam | [`maplibre-perf-governance.yml`](../../.github/workflows/maplibre-perf-governance.yml) invokes all three functions directly |
| [`test_package_exports.py`](test_package_exports.py) | 3 | Public export targets, renderer-neutral root facade, and Node resolution of root and adapter subpaths | [`maplibre-perf-governance.yml`](../../.github/workflows/maplibre-perf-governance.yml) invokes all three functions directly |
| [`test_perf_governance_negative_paths.py`](test_perf_governance_negative_paths.py) | 3 | Rejection of zero frame budget, negative memory budget, and out-of-range tile error rate | [`maplibre-perf-governance.yml`](../../.github/workflows/maplibre-perf-governance.yml) invokes all three functions directly |
| [`test_source_metadata.py`](test_source_metadata.py) | 9 | Local source epoch/license/digest projection, manifest/source matching, finite `ALLOW`/`ABSTAIN`/`DENY`/`ERROR` outcomes, duplicate-key and malformed-JSON fail-closed behavior, deterministic redacted reports, no-network posture, and CLI exit codes | [`maplibre-source-metadata.yml`](../../.github/workflows/maplibre-source-metadata.yml) runs the focused module, fixture outcomes, and syntax checks |

[`perf_fixture_builder.py`](perf_fixture_builder.py) supplies the synthetic scalar
fixture used by the three performance negative-path tests. It is test support,
not a performance contract, observed benchmark, or release threshold authority.

## Current outcomes

The tests use finite outcomes for different questions. Do not collapse them into
one readiness signal.

| Surface | Current expected outcome | Meaning |
| --- | --- | --- |
| Acquisition inventory | `PASS`, `HOLD`, or `FAIL` according to discovered acquisition | The scanner classifies repository structure; a clean scan does not prove runtime behavior |
| MapLibre 6.6 readiness | `HOLD` with `RUNTIME_PROBES_PENDING` | Exact dependency and structural prerequisites exist, but the required runtime probe matrix is incomplete |
| Source-metadata projection | `ALLOW`, `ABSTAIN`, `DENY`, or `ERROR` according to local fixture and manifest state | Finite local projection evidence only; it does not admit a source or resolve rights, evidence, policy, review, release, or publication |
| Legacy performance harness | exit code `3` and `WORKFLOW_HOLD` | The former CDN/global harness is retired and cannot acquire a renderer or network resource |
| Performance governance workflow | `WORKFLOW_HOLD` after static checks pass | Browser, performance, visual, attestation, proof, and release stages were deliberately not run |

`DENY`, `HOLD`, and other safe negative outcomes can be successful test
expectations. A green test means the expected classifier behavior occurred; it
does not upgrade the candidate to `READY` or authorize a downstream state.

## Run the focused checks

Run commands from the repository root.

### Acquisition inventory

```bash
python -m unittest tests.maplibre.test_assess_acquisition_inventory --verbose
python tools/validators/maplibre/assess_acquisition_inventory.py \
  --repo-root . \
  --summary
```

The second command reports the current repository inventory. Treat a non-passing
outcome as a boundary finding to investigate, not as permission to relocate or
admit a renderer dependency.

### Version-readiness classifier

```bash
python -m unittest discover \
  --start-directory tests/maplibre \
  --pattern 'test_validate_v6_readiness.py' \
  --verbose
python tools/validators/maplibre/validate_v6_readiness.py --fixtures
python tools/validators/maplibre/validate_v6_readiness.py --scan-root .
```

The fixture pack contains three valid and five invalid cases under
[`fixtures/maplibre/v6_readiness/cases.json`](../../fixtures/maplibre/v6_readiness/cases.json).
The current-repository scan is expected to emit `HOLD`, target version `6.6.0`,
and reason `RUNTIME_PROBES_PENDING`.

### Source-metadata projection

```bash
python -m unittest discover \
  --start-directory tests/maplibre \
  --pattern 'test_source_metadata.py' \
  --verbose
python tools/validators/maplibre/validate_source_metadata.py --fixtures
```

This focused profile is deterministic, synthetic, and no-network. Its finite
outcomes are renderer-projection evidence only; they do not authenticate remote
bytes, establish source authority, clear rights, close an EvidenceBundle, or
approve policy, review, release, deployment, promotion, or publication.

### Performance-hold checks

The hosted performance-governance workflow directly invokes the nine functions
from the retirement, export, and scalar-negative modules. It also parses every
Python file in this directory and every MapLibre validator, then syntax-checks
the seven repository-owned MapLibre scripts. Use that workflow as the exact
command contract for this held lane.

The root `maplibre:govern` and `make maplibre-govern` commands still invoke the
placeholder governance validator without inputs. They are retained as explicit
hold surfaces, not complete performance validation commands.

## CI mapping

| Workflow | Trigger coverage relevant to this lane | Executed evidence | Important limit |
| --- | --- | --- | --- |
| [`maplibre-acquisition-inventory.yml`](../../.github/workflows/maplibre-acquisition-inventory.yml) | `tests/maplibre/**`, package/app acquisition surfaces, `package.json`, ADRs, validator, and related workflow surfaces | All 49 acquisition tests plus current-repository summary scan | Structural inventory only; no browser or runtime proof; lockfile-only changes do not trigger this workflow |
| [`briefing-implementation-campaign.yml`](../../.github/workflows/briefing-implementation-campaign.yml) | Readiness validator, its test module, fixture pack, and retained receipts | All 16 readiness tests, fixture polarity, current 6.6.0 `HOLD`, and historical receipt replay | Shared campaign; does not run the other MapLibre modules |
| [`maplibre-perf-governance.yml`](../../.github/workflows/maplibre-perf-governance.yml) | This whole directory plus package, app, config, schema, script, validator, fixture, and workflow surfaces | Syntax checks, nine deterministic tests, exact lock/dependency checks, held-assumption inspection, and step summary | Installs no dependencies or browser; uploads no artifact; ends in explicit runtime/performance hold |
| [`maplibre-source-metadata.yml`](../../.github/workflows/maplibre-source-metadata.yml) | Source-metadata validator, its test module, fixture pack, generated receipts, and workflow definition | Nine source-metadata tests, exact fixture outcomes and reason codes, and Python/JSON syntax | Does not trigger for this README-only path; no remote-byte, rights, evidence, policy, review, release, deployment, or publication authority |

All four workflows use read-only repository permissions. Their conclusions and
logs are CI evidence only. They are not policy decisions, receipts, attestations,
release manifests, deployment records, or publication records.

## Safety and evidence boundaries

### No-network posture

The checked Python tests and classifiers use repository files and synthetic
fixtures. The performance workflow installs neither workspace dependencies nor
browsers after action bootstrap. The retired
[`scripts/maplibre-smoke-perf.mjs`](../../scripts/maplibre-smoke-perf.mjs) must
remain free of CDN URLs, renderer globals, Playwright acquisition, screenshots,
and artifact writes.

A future browser-performance lane needs deterministic local styles, tiles,
glyphs, sprites, thresholds, expected metrics, network denial, and accepted
artifact handling before the hold can change.

### Renderer and public-truth boundary

MapLibre is downstream rendering and interaction infrastructure. These tests may
check dependency ownership and safe acquisition, but they must not make a map,
style, tile, screenshot, index, dashboard, test result, or generated object into
sovereign truth.

Public clients must continue to use governed interfaces or released public-safe
artifacts. Direct reads from canonical/internal lifecycle stores remain outside
the renderer boundary. Rights, sensitivity, privacy, sovereignty, harmful
precision, provenance, correction, withdrawal, and rollback obligations are not
satisfied merely because a renderer or boundary test passes.

### Fixtures and generated output

- [`fixtures/maplibre/v6_readiness/`](../../fixtures/maplibre/v6_readiness/)
  contains synthetic classifier cases, not runtime baselines.
- [`tests/fixtures/maplibre/`](../fixtures/maplibre/) is a local test-support lane;
  its README and presence do not establish source admission or reusable fixture
  authority.
- `artifacts/perf/` must remain free of tracked trust-shaped outputs while the
  workflow is held. Candidate builders for proofs, attestations, releases,
  corrections, and rollback do not become authoritative because their syntax is
  checked.

## Failure interpretation

| Failure | Investigate first | Do not infer |
| --- | --- | --- |
| Acquisition test or scan fails | New import, re-export, global, CDN reference, dependency owner, package home, path escape, or scanner safety regression | That moving or deleting the surface is automatically authorized |
| Readiness test or fixture fails | Version ownership, exact pin, upstream identity, import boundary, profile, or computed outcome | That the renderer should be upgraded or activated |
| Source-metadata test or fixture fails | Local projection syntax, digest/manifest matching, finite outcome/reason code, redaction, or no-network regression | That a source is admitted, remote bytes are verified, rights are cleared, or evidence/policy is resolved |
| Export test fails | `packages/maplibre/package.json` exports and owned source targets | That raw MapLibre types should be exposed from the root facade |
| Retirement test fails | Legacy script exit, network/renderer strings, and package-seam confinement | That the former live-CDN harness may be restored |
| Scalar negative-path test fails | Fixture builder validation for frame, memory, or tile-error bounds | That the stored defaults are measured or accepted production budgets |
| Performance workflow fails | Exact failing step and changed held assumption | That browser performance, visual parity, proof closure, or release failed; those stages were not run |

When a failure exposes a real implementation gap, keep the documented state at
`HOLD`, correct the owning implementation in a separate reviewed change, and
rerun the directly affected checks. Do not weaken classifiers or fixtures merely
to recover a green result.

## Maintenance

Update this README when any of the following changes materially:

- a direct module, helper, test count, fixture profile, or expected outcome;
- `packages/maplibre/` dependency ownership, exact version, or export map;
- ADR-0006 or ADR-0007 status or supersession;
- workflow commands, path filters, permissions, runner versions, or artifact
  behavior;
- retirement of the legacy harness or admission of a governed replacement;
- schema or validator maturity, performance fixtures, threshold authority, or
  browser probe closure; or
- correction, rollback, release, deployment, or publication evidence.

Preserve the distinction between source-defined test inventory, local execution,
hosted workflow execution, accepted architecture, runtime readiness, release,
deployment, and publication.

## Open gaps

- **HOLD:** The required runtime probe matrix is incomplete, including broader
  CSP, PMTiles/vector loading, terrain/DEM, tile churn, Evidence Drawer selection
  stability, accessibility, long-session behavior, and headless parity.
- **HOLD:** Governed performance and visual-diff fixtures, accepted thresholds,
  deterministic baselines, failure bundles, and artifact homes are not closed.
- **HOLD:** Eight performance schemas remain permissive object scaffolds and the
  aggregate governance verifiers remain placeholders.
- **UNKNOWN:** Required-check status, complete consumer migration, production
  parity, accountable stewardship, correction propagation, and operational
  rollback have not been established by this lane.
- **NOT AUTHORIZED:** A passing test or workflow does not admit a source, approve
  policy, create a release, deploy a renderer, promote an artifact, or publish a
  public map.

## Evidence basis

Material claims in this README were reconciled against current repository files,
including the six direct test modules, MapLibre validators, four workflows, the
readiness and source-metadata fixtures, the package manifest and lock state, the
retired harness, accepted ADR-0006 and ADR-0007, and the package README.
Historical Drive and Notion material was used only as read-only lineage and
candidate context; it was not treated as current implementation or adopted
authority.
