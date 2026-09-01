<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/m35-reproducible-builds-sbom-attestation-artifact-integrity-source-map
title: M35 Reproducible Builds, SBOM, Attestation, and Artifact Integrity — inventory and first slice
type: exploratory-intake-source-map
version: v0.1.0
status: triaged; exploratory; non-authoritative; decision-required
owners: OWNER_TBD - Docs steward · Build steward · Reproducibility steward · Supply-chain steward · Security steward
created: 2026-09-01
updated: 2026-09-01
policy_label: internal; intake; exploratory; reproducibility; supply-chain; artifact-integrity
truth_posture: cite-or-abstain; inventory is bounded to current repository bytes and pinned GitHub metadata
owning_root: docs/
responsibility: Record the current repository surfaces relevant to M35, map overlap, and name one reversible artifact-class slice for a two-build comparison without implying release, publication, or vulnerability absence.
repository: bartytime4life/Kansas-Frontier-Matrix
repository_main_snapshot: db23a8bfa9fa126e87009a41240576619ccaac02
execution_branch_snapshot: 1a0c4a0ace0c3288354fbea8596d35896f4e3603
audit_baseline: f86fcddb553217f7ffadafd80f20e95d635180b1
related:
  - ./README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../artifacts/build/README.md
  - ../../artifacts/build/dist/README.md
  - ../../../README.md
  - ../../../package.json
  - ../../../Makefile
  - ../../../apps/kansas-frontier-matrix-explorer/package.json
  - ../../../apps/kansas-frontier-matrix-explorer/package-lock.json
  - ../../../apps/kansas-frontier-matrix-explorer/README.md
  - ../../../apps/kansas-frontier-matrix-explorer/scripts/install-ci.sh
  - ../../../apps/kansas-frontier-matrix-explorer/scripts/build-verified.sh
  - ../../../apps/explorer-web/package.json
  - ../../../.github/workflows/docs-build.yml
  - ../../../.github/workflows/codeql.yml
  - ../../../.github/workflows/dependency-scan.yml
  - ../../../.github/workflows/cosign-attestation-verification-plan.yml
  - ../../../.github/workflows/pmtiles-attestation.yml
  - ../../../.github/workflows/proof-pack-closure.yml
  - ../../../.github/workflows/release-manifest.yml
  - ../../../.github/workflows/source-artifact-validation.yml
  - ../../../.github/workflows/ui-build.yml
  - ../../../.github/workflows/maplibre-perf-governance.yml
tags: [kfm, intake, exploratory, reproducible-builds, sbom, attestation, artifact-integrity, lockfiles, no-network, comparison, overlap]
notes:
  - "Current-main evidence was pinned again at execution start; the baseline issue snapshot remains audit-only."
  - "The open overlap map now includes PR #4068 and adjacent issue #3382; the earlier 'none yet verified' note is superseded."
  - "This packet records repository evidence only. It does not create a build producer, SBOM, attestation, signature, release record, or public artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# M35 reproducible builds, SBOM, attestation, and artifact integrity — inventory and first slice

> **Outcome:** current repository evidence supports one narrow, reversible first slice: the
> `apps/kansas-frontier-matrix-explorer` deployable Sites artifact. That slice already has a
> lockfile-bound install path, a timeout-bounded build, and explicit Linux tooling notes. It does
> **not** yet establish a reproducible two-build comparison, SBOM generation, provenance signing,
> or digest binding for the milestone.

**Quick links:** [Authority](#authority-and-placement-basis) · [Pinning](#execution-start-pin-and-overlap-map) · [Inventory](#current-repository-inventory) · [Outcome classes](#material-outcome-ledger) · [First slice](#selected-first-slice) · [Validation](#validation-and-rollback-boundary)

## Authority and placement basis

Accepted [Directory Rules v2](../../doctrine/directory-rules.md), adopted through
[ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md), place this note under
`docs/intake/exploratory/` as non-canonical intake. The adjacent directory README owns that waiting-room
contract; this packet does not create a second authority root.

## Execution-start pin and overlap map

| Field | Bounded value | Status |
|---|---|---|
| Current main | `db23a8bfa9fa126e87009a41240576619ccaac02` | CONFIRMED |
| Execution branch snapshot | `1a0c4a0ace0c3288354fbea8596d35896f4e3603` | CONFIRMED |
| Audit baseline in issue #3399 | `f86fcddb553217f7ffadafd80f20e95d635180b1` | CONFIRMED |
| Open overlap PR | [#4068](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4068) — `[WIP] Add evidence for reproducible builds and artifact integrity` | CONFIRMED |
| Adjacent supply-chain issue | [#3382](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3382) — `[M17] Dependency, Container, SBOM & Supply-Chain Assurance — evidence and first slice` | CONFIRMED |
| Parent milestone issue | [#3399](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3399) | CONFIRMED |

## Current repository inventory

### Relevant surfaces

- `package.json` pins the workspace toolchain and leaves the root `build` script as a hold.
- `apps/kansas-frontier-matrix-explorer/package.json` plus `package-lock.json` define a lockfile-based app build lane.
- `apps/kansas-frontier-matrix-explorer/README.md` states the Linux, `flock`, `curl`, and GNU `timeout` prerequisites and the bounded install/build posture.
- `apps/kansas-frontier-matrix-explorer/scripts/install-ci.sh` enforces a single non-retrying lockfile install.
- `apps/kansas-frontier-matrix-explorer/scripts/build-verified.sh` wraps the build in a timeout and refuses missing CI prerequisites.
- `apps/explorer-web/package.json` has a direct `vite build` path but no evidence here of reproducible-build comparison controls.
- `artifacts/build/README.md` and `artifacts/build/dist/README.md` document compatibility lanes, but not an authenticated two-build result.
- `.github/workflows/docs-build.yml` is an explicit hold, not a build proof.
- `.github/workflows/codeql.yml`, `dependency-scan.yml`, `cosign-attestation-verification-plan.yml`, `pmtiles-attestation.yml`, `proof-pack-closure.yml`, `release-manifest.yml`, `source-artifact-validation.yml`, `ui-build.yml`, and `maplibre-perf-governance.yml` are adjacent evidence surfaces, but none of them yet bind the selected app build class to a reproducible comparison result.

### Not in scope for this slice

- live payload retrieval;
- release, deployment, or publication;
- a new ADR, policy, or repository setting;
- canonical SBOM/signature/provenance retention homes;
- current hosted run history or branch-protection truth.

## Material outcome ledger

| Class | Bounded reading |
|---|---|
| `IMPLEMENTED` | The selected app has a lockfile install path and a timeout-bounded build wrapper. |
| `PARTIAL` | Repository-level build and artifact-integrity documentation exists, but no authenticated two-build comparison is recorded. |
| `ABSENT` | Repository-wide SBOM, provenance attestation, signature binding, and digest-bound rebuild comparison for this milestone. |
| `SUPERSEDED` | The earlier “no overlap yet verified” assumption in the issue body is superseded by PR #4068 and issue #3382. |
| `CONFLICTED` | Documentation still describes future reproducibility and sidecar claims while the current repo does not establish a producer for them. |
| `DEPRECATED` | Root readiness markers and hold workflows are intentionally non-enforcing. |
| `NOT_INSPECTED` | Ignored workspace bytes, hosted runner state, and external registries. |

## Selected first slice

**Artifact class:** `apps/kansas-frontier-matrix-explorer` deployable Sites artifact.

**Why this slice:** it is the smallest current build surface with a lockfile-pinned install path, a bounded build command, and explicit environment notes. That makes it the best candidate for a dependency-closed two-build comparison before widening to SBOMs, attestations, signatures, or other artifact classes.

**Proposed comparison contract:**

1. clean checkout at the pinned main snapshot;
2. one bounded install from `package-lock.json`;
3. two builds of the same commit under the same explicit environment;
4. compare the selected build tree and any recorded digests;
5. classify `SKIPPED`, `NOT_RUN`, `PARTIAL`, and `PASS` separately.

**Proposed controls:** fixed timezone and locale, pinned Node/npm toolchain, no ambient network except the bounded lockfile install path, timeout limits, and a stable output root.

## Validation and rollback boundary

- Focused test expectation: the selected artifact class should support a repeatable compare-or-fail harness once the first slice lands.
- Hosted-check expectation: any future workflow must report `NOT_RUN` or `SKIPPED_EXPLICIT` honestly until the comparison is actually executed.
- Correction handling: if the two-build comparison diverges, preserve both build records and treat the mismatch as evidence, not noise.
- Rollback: revert this note alone; no build artifact, SBOM, attestation, or release record is created by this packet.

