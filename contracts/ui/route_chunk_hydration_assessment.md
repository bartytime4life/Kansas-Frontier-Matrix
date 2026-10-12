<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/ui/route-chunk-hydration-assessment
title: RouteChunkHydrationAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — UI steward · Contract steward · Evidence steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; ui; route-chunk; view-registry; evidence-state; access-state
responsibility: Define a fixture-only preflight for one route-specific lazy UI chunk without loading code, binding a route, resolving references, or granting activation, release, deployment, or publication authority.
truth_posture: "CONFIRMED attached Pass 18 card, attached MapLibre atlas, visual review, connected Drive metadata, and bounded repository gap; PROPOSED inactive assessment; UNKNOWN runtime adoption; NEEDS VERIFICATION UI, contract, evidence, access, and validation review plus hosted exact-head CI"
related:
  - ./view_registry_profile.md
  - ../../schemas/contracts/v1/ui/route_chunk_hydration_assessment.schema.json
  - ../../fixtures/ui/route_chunk_hydration_assessment/cases.json
  - ../../tools/validators/ui/validate_route_chunk_hydration_assessment.py
  - ../../tests/validators/ui/test_validate_route_chunk_hydration_assessment.py
  - ../../docs/intake/exploratory/pass-18-route-chunk-hydration-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# RouteChunkHydrationAssessment Candidate

`RouteChunkHydrationAssessmentCandidate` is an additive, fixture-only preflight
for one route-specific lazy UI chunk. It implements the smallest reviewable
portion of supplied Pass 18 card `KFM-P18-INV-329`: lazy loading remains
subordinate to validated view-registry, render-hint, evidence, access, and
release state.

The candidate composes the existing `ViewRegistryProfile` by opaque reference.
It does not duplicate that profile, inspect a live registry, import a module, or
mount a route.

## Prerequisite states

| Concern | Ready state | Held states | Denied state |
|---|---|---|---|
| View registry | `READY` | `HOLD`, `UNKNOWN` | `DENY` |
| Render hints | `READY` | `HOLD`, `UNKNOWN` | `DENY` |
| Evidence | `RESOLVED` | `PARTIAL`, `MISSING`, `UNKNOWN` | None in this bounded profile |
| Access | `ALLOW` | `HOLD`, `UNKNOWN` | `DENY` |
| Release | `RELEASED` | `HOLD`, `UNKNOWN` | `DENY` |

All five concerns must be in their ready state for `HYDRATE_READY`. Any denied
state derives `REJECT`. Any other non-ready state derives `HOLD`. Declared
disposition and reason codes are content-bound and must match the prerequisite
states exactly.

## Chunk declaration

The profile names one `LAZY_ROUTE` chunk, its module reference, integrity
digest, and sorted dependency references. The chunk identity must match its
declared chunk name. These are declarations only: the validator does not import,
fetch, execute, prefetch, or cache the module.

Direct lifecycle-store references, database/graph handles, and embedded query
markers are denied anywhere in the candidate. View registry, render hint,
Evidence Drawer, access policy, and release references retain distinct roles.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | All prerequisite declarations are ready and the candidate is locally coherent. |
| `ABSTAIN` | At least one prerequisite is held, partial, missing, or unknown, with no denied prerequisite. |
| `DENY` | A prerequisite is denied or the candidate contains contradictory identity, state, reference, ordering, time, or content-hash declarations. |
| `ERROR` | The candidate cannot be safely parsed or evaluated under the closed schema. |

`PASS` means only that a synthetic preflight is internally consistent. It is not
permission to hydrate the declared chunk.

## Boundary

A validator result does not:

- bind, load, import, prefetch, cache, execute, or mount a route or module;
- resolve the view registry, render hints, evidence, policy, or release refs;
- query a database, graph, object store, lifecycle store, or external service;
- activate a layer, approve review, or authorize promotion, release,
  deployment, publication, or public use;
- modify `apps/explorer-web/`, the existing view-registry profile, a registry,
  artifact, policy rule, release record, or cache.

## Directory Rules basis

UI contract meaning belongs under `contracts/ui/`. Machine shape, synthetic
replay, repository validation, executable conformance, read-only CI, source
lineage, and authoring provenance remain in their established responsibility
roots. No new root, live registry, runtime adapter, route table, policy source,
release lane, or public path is created.

## Validation and rollback

```bash
python -m unittest tests.validators.ui.test_validate_route_chunk_hydration_assessment -v
python tools/validators/ui/validate_route_chunk_hydration_assessment.py --fixtures
```

Rollback is one additive commit revert. The inactive profile creates no route,
module, registry, cache, lifecycle, release, deployment, publication, or public
state that requires restoration.
