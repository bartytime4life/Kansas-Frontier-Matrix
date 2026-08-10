<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/new-ideas-feb-2026-postgis-compatibility-source-map
title: New Ideas Feb-2026 - PostGIS Compatibility Decision Source Map
type: exploratory-intake-source-map
version: v0.1.0
status: triaged; exploratory-retained; decision-gap; non-authoritative; implementation-held
owners: OWNER_TBD - database steward; geo package steward; migration steward; platform steward; security steward; validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; intake; exploratory; database; spatial; native-dependency; supply-chain; fail-closed
truth_posture: CONFIRMED private-source extraction and repository-gap reconciliation at the pinned snapshot / PROPOSED decision-packet boundary / UNKNOWN runtime selection and live compatibility / NEEDS VERIFICATION authoritative versions, ownership, artifacts, and execution evidence
owning_root: docs/
responsibility: Preserve a privacy-minimized reconciliation of the private New Ideas Feb-2026 PostGIS compatibility proposal without selecting a database stack, inventing a package or adapter owner, or promoting dated version and runtime claims.
source_class: connected private document
source_title: New Ideas Feb-2026
source_section: PostGIS adapter compatibility and upgrade gate
source_status: non-authoritative exploratory proposal containing version-sensitive implementation examples
source_disclosure: privacy-minimized; full text, code, commands, connector locator, private link, timestamps, digest, and file size omitted
repository: bartytime4life/Kansas-Frontier-Matrix
repository_snapshot: 91bc8581821b9f0e710afed0b4f9ded86d4fb304
repository_verified_on: 2026-08-10
related:
  - ./README.md
  - ../../../migrations/database/README.md
  - ../../../packages/geo/README.md
  - ../../../packages/geo/pyproject.toml
  - ../../../contracts/runtime/graph_runtime_compatibility_matrix.md
  - ../../standards/GEOPARQUET.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, postgresql, postgis, geos, compatibility, migration, native-library, supply-chain, decision-gap]
notes:
  - "The source is evidence that a database/native-library compatibility matrix and upgrade gate were proposed; it is not evidence that any version, image, adapter, branch, runner, database, migration, or workflow is selected or operational."
  - "Current main explicitly leaves the active database engine and migration runner unestablished, while the Geo package records a native-library support matrix as open work."
  - "This source map creates no architecture decision, support promise, dependency, path authority, database object, migration, workflow, environment, release, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# New Ideas Feb-2026 - PostGIS compatibility decision source map

> **Outcome:** The source's request for a PostgreSQL/PostGIS/GEOS compatibility
> matrix is a distinct but premature decision gap. Current repository evidence
> does not establish an active database engine, selected migration runner,
> admitted native geospatial dependency, supported adapter, or verified database
> fixture suite. This record retains the decision pressure and the evidence
> threshold; it does not promote the source's versions, paths, code, commands, or
> operational claims.

> [!CAUTION]
> A compatibility row, successful smoke test, passing workflow, or parseable SQL
> would be readiness evidence only. None of those outcomes selects a runtime,
> authorizes a migration, proves production support, admits data, changes
> lifecycle state, releases an artifact, or permits publication.

## Source boundary and review method

| Field | Bounded value |
|---|---|
| Supplied title | *New Ideas Feb-2026* |
| Reviewed cluster | PostGIS adapter compatibility and upgrade gate |
| Source posture | Non-authoritative exploratory proposal with version-sensitive examples |
| Repository comparison | `main@91bc8581821b9f0e710afed0b4f9ded86d4fb304`, inspected `2026-08-10` |
| Private material | Full text, code, commands, Drive locator, private link, connector metadata, digest, and file size omitted |

The connected document was treated as idea evidence, not as an environment
inventory or support statement. Repository paths, contracts, dependency
declarations, migration documentation, and accepted Directory Rules determined
the bounded disposition. The source's named versions and example container,
branch, SQL, workflow, and adapter details were not copied because their
currency, provenance, compatibility, and repository fit were not established.

## Directory Rules and authority basis

Accepted [Directory Rules v2](../../doctrine/directory-rules.md), adopted through
[ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md), place
artifacts by primary responsibility. This source map therefore stays in the
non-authoritative exploratory intake lane while future work remains split across
existing owners:

| Responsibility | Governed owner after an explicit decision |
|---|---|
| Private-source reconciliation | `docs/intake/exploratory/` - this file |
| Database DDL, extension upgrades, forward steps, and recovery pairing | [`migrations/database/`](../../../migrations/database/README.md) plus the governed rollback lane |
| Reusable non-deployable spatial implementation | [`packages/geo/`](../../../packages/geo/README.md), or another accepted package owner if a decision establishes one |
| Runtime-only local adapter composition | `runtime/`, only if the selected behavior is composition rather than reusable package logic |
| Non-secret shared profiles | `configs/`, only after a consumer and schema are accepted |
| Deployment, image, host, access, and exposure configuration | `infra/` |
| Repository automation | `.github/workflows/` |
| Reusable synthetic inputs | `fixtures/` |
| Executable conformance evidence | `tests/` |
| Semantic and machine-readable matrix authority | `contracts/` and `schemas/`, only after object identity, ownership, and consumers are decided |

The source's suggested adapter path is not adopted. No topic-named root, parallel
database home, package, runtime adapter, matrix contract, workflow, fixture lane,
or migration branch is created by this record.

## Repository-grounded reconciliation

| Source pressure | Current repository evidence | Disposition |
|---|---|---|
| Test a PostgreSQL/PostGIS/GEOS version matrix before upgrades | The database migration lane states that no active engine, selected runner, dedicated workflow, applied-version ledger, or verified database fixture suite was established. | `RETAIN` as a decision and evidence gap; `HOLD` implementation. |
| Make native geospatial compatibility explicit | The Geo package is a `0.0.0` scaffold with no declared dependencies and records `GEO-PKG-030` - define a native-library support matrix - as `NEEDS VERIFICATION`. | `CORROBORATE` the existing gap; do not create a second backlog authority. |
| Pin native-library versions for deterministic behavior | The GeoParquet standard requires GEOS, GDAL, PROJ, and PostGIS versions to be pinned when used. | `RETAIN` as a governing constraint, not as proof that those libraries are selected. |
| Use a data-driven compatibility artifact | The graph runtime family provides an adjacent example of an inactive, non-authorizing matrix, but it governs a different runtime and does not decide the spatial matrix's owner or shape. | `REFERENCE` as a bounded pattern only. |
| Create an adapter and migration-staging branch immediately | No active database runtime, accepted adapter owner, branch policy, or migration runner was established. | `REJECT FROM THIS SLICE`. |
| Treat source versions and smoke examples as current support facts | The source is private exploratory prose and its claims are version-sensitive. No authoritative current-version research, pinned artifact set, or execution receipt accompanies it. | `ABSTAIN / NEEDS VERIFICATION`. |

This idea is not a duplicate of the graph runtime compatibility matrix. It
concerns a different dependency family and database/spatial behavior. It is also
not ready to reuse that matrix contract: ownership, required fields, support
semantics, and consumers remain undecided.

## Retained non-duplicate gap

The bounded gap is a reviewed decision packet answering these questions before
any implementation is admitted:

1. Which database engine, extension set, and access pattern, if any, are
   actually selected for KFM?
2. Which responsibility owns reusable geometry behavior, database-specific
   adapter behavior, migration mechanics, and runtime composition without
   creating a circular dependency or parallel authority?
3. What does a row mean: observed compatibility, project support, upstream
   support, candidate-only, deprecated, denied, or unknown?
4. Which exact versions and artifact identities must be recorded for the
   database engine, PostGIS, GEOS, and any relevant GDAL, PROJ, client driver,
   operating-system, architecture, projection database, or grid resource?
5. Which evidence makes a row supportable, who reviews it, how does it expire,
   and what fails closed when evidence is absent, stale, conflicted, or
   unverifiable?
6. How are extension upgrades sequenced with application compatibility,
   database migration, backup or compensating recovery, correction, and
   rollback without treating a branch or file move as promotion?

Until these questions are answered by the owning stewards, the truthful state
is `UNKNOWN` or `NEEDS VERIFICATION`, not an empty or optimistic `SUPPORTED`
row.

## Proposed decision packet boundary

A future decision packet should define, without yet promising production
support:

- the selected engine and extension scope, or an explicit decision not to
  select them;
- the matrix object identity, owner, consumers, finite states, schema version,
  canonical serialization, and duplicate-row rules;
- exact immutable artifact identities, including container image digests or
  binary provenance and SBOM references where applicable;
- platform dimensions such as operating system, architecture, database engine,
  extension, native libraries, client driver, and required resource databases;
- observed capability fields for geometry/geography carriers, SRID behavior,
  spatial indexes, transforms, extension upgrade, rollback or restore, and
  error handling;
- evidence references, observation time, expiry or review-by time, reviewer,
  support window, deprecation state, and correction path;
- fail-closed behavior for unknown tuples and a rule that matrix presence never
  substitutes for live environment verification; and
- dependency licensing, redistribution, vulnerability, update, offline,
  deterministic-build, and rollback posture.

The exact contract, schema, control-plane projection, config, package, runtime,
and migration paths remain `PROPOSED` pending that decision. This source map is
not their authority.

## Minimum future validation

If a decision admits the stack, validation should use synthetic, non-sensitive
data and pin every material input. At minimum, evidence should cover:

- clean installation and extension activation from immutable artifacts;
- exact database and native-library version reporting tied to provenance;
- geometry and geography round trips with explicit dimensionality and SRID;
- index creation plus bounded query-behavior checks for the selected operator
  classes, without promoting timing observations into universal guarantees;
- coordinate transforms using explicitly identified resource databases and
  grids, including missing-resource and no-network failure states;
- malformed, invalid, oversized, non-finite, mixed-dimension, and unexpected-
  SRID inputs with deterministic, non-leaking diagnostics;
- upgrade rehearsal from every admitted predecessor, plus rollback, restore, or
  forward-fix evidence appropriate to the selected engine;
- application and migration compatibility at both sides of the supported
  transition; and
- cross-platform or explicitly bounded-platform results, expiry, correction,
  and stale-evidence rejection.

Passing these checks would prove only the recorded observation under the pinned
environment. Hosted CI, local containers, and nightly probes are supporting
evidence, not production execution receipts or release decisions.

## Explicit non-effects and rejected transfers

This record does **not**:

- adopt any source-stated version, support window, container tag, image,
  package, binary, client, action, or command;
- create the source's proposed adapter path or assert that an `api/` root owns
  database integration;
- establish `migration-staging` or any other branch as repository policy;
- accept floating action revisions, mutable container tags, or version labels
  as immutable supply-chain identity;
- treat the source's SQL snippets as proof of topology, CRS correctness, index
  semantics, transform accuracy, migration safety, or recovery;
- authorize logs or fixtures containing real, restricted, or precise sensitive
  geometry;
- install or connect to PostgreSQL, PostGIS, GEOS, GDAL, PROJ, a container
  runtime, a live database, or an external service;
- create database objects, migrations, dependencies, workflows, infrastructure,
  releases, deployment state, or public routes; or
- let a green matrix row approve source admission, policy, review, promotion,
  release, correction, rollback, or publication.

Public clients remain behind governed interfaces and released carriers. They
must not receive direct access to a canonical or internal database merely
because a candidate compatibility tuple passes.

## Recommended next bounded action

The next action is a steward-reviewed decision issue or ADR-scoped packet, not
runtime code. It should first decide whether the database/native stack is in
scope and assign the responsibility split. Only then should maintainers perform
authoritative current-version research, define the matrix contract and schema,
pin artifacts, add synthetic fixtures and negative tests, and rehearse one
upgrade and recovery path in an isolated environment.

If the stack is not selected, close this item as retained lineage and keep
`GEO-PKG-030` unresolved or explicitly rejected with rationale. Do not preserve
a speculative matrix whose rows could be mistaken for support.

## Rollback and correction

Before merge, close the draft pull request and abandon its isolated branch.
After an authorized merge, revert this single additive source-map file through
a reviewed corrective pull request. No database, dependency, migration,
workflow, environment, release, deployment, or published artifact requires
restoration. If later evidence changes the disposition, amend or supersede this
record with the new repository snapshot, decision identity, and correction
reason rather than silently rewriting the source claim.

[Back to top](#top)
