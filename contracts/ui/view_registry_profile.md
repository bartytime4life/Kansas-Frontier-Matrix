<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/ui/view-registry-profile
title: ViewRegistryProfile
type: semantic-contract
version: v0.1
status: draft; PROPOSED_INACTIVE; fixture-only; no-runtime-authority
updated: 2026-08-09
policy_label: public; ui; contract-first; no-direct-store-access; release-gated
source_cards: [KFM-P32-IDEA-0008, KFM-P32-FEAT-0004]
[/KFM_META_BLOCK_V2] -->

# ViewRegistryProfile

> **Truth posture:** PROPOSED / INACTIVE. This contract, schema, synthetic fixtures,
> validator, and tests make a candidate route-to-contract registry inspectable. They
> do not register a live route, query a graph or store, activate a layer, establish
> catalog closure, evaluate policy, approve review, release an artifact, or publish
> a view.

## Purpose

`ViewRegistryProfile` gives UI routes a contract-first resolution surface. Each
candidate view names the governed delivery contract, catalog closure, layer
manifests, rendering hints, performance budget, access and sensitivity policies,
Evidence Drawer profile, and release manifest that a later runtime integration
would have to resolve.

The profile addresses the proposal in `KFM-P32-IDEA-0008` without implementing
the runtime registry or the inspector UI proposed in `KFM-P32-FEAT-0004`.

## Boundary

The profile is deliberately declarative:

- a route resolves to a governed API contract or released-artifact contract;
- UI-visible catalog context retains STAC, DCAT, and PROV references;
- render hints identify a renderer, delivery protocol, style, and performance
  budget but do not fetch or render anything;
- policy, Evidence Drawer, and release references remain separate dependencies;
- every entry remains `PROPOSED_INACTIVE`;
- authority fields are fixed to `false`.

The profile must never contain credentials, embedded queries, direct database or
object-store endpoints, RAW/WORK/QUARANTINE paths, or an activation instruction.

## Finite validation outcomes

| Outcome | Meaning | Authority |
|---|---|---|
| `PASS` | The candidate registry is internally consistent and every catalog closure is declared `READY`. | Local fixture consistency only. |
| `ABSTAIN` | At least one entry declares catalog closure `HOLD`. | No activation or publication. |
| `DENY` | An entry declares catalog closure `DENY`, or shape/semantic checks fail. | No activation or publication. |
| `ERROR` | The validator cannot safely read or evaluate the candidate. | No activation or publication. |

Declared closure states are fixture inputs, not independently verified facts.

## Required entry dependencies

Each view entry contains:

1. a stable `view_id` and canonical UI `route_path`;
2. exactly one governed delivery-contract reference;
3. a catalog-closure reference plus STAC, DCAT, and PROV references;
4. a sorted, unique set of layer-manifest references;
5. renderer, protocol, style, and performance-budget hints;
6. separate access-policy and sensitivity-policy references;
7. Evidence Drawer and ReleaseManifest references;
8. an inactive activation state and fixed-false authority declarations.

Entries and their layer-manifest references are lexically sorted so the same
logical candidate produces the same JCS SHA-256 identity.

## Non-effects

A successful validation does **not**:

- create or bind an application route;
- read a canonical, graph, search, model, or lifecycle store;
- prove that referenced contracts or artifacts exist;
- establish catalog, evidence, policy, review, or release truth;
- grant authentication, authorization, promotion, activation, deployment,
  publication, or public-use authority.

## Repository surfaces

| Concern | Path |
|---|---|
| Semantic meaning | `contracts/ui/view_registry_profile.md` |
| Machine shape | `schemas/contracts/v1/ui/view_registry_profile.schema.json` |
| Synthetic cases | `fixtures/ui/view_registry_profile/cases.json` |
| Deterministic validator | `tools/validators/ui/validate_view_registry_profile.py` |
| Focused tests | `tests/validators/ui/test_validate_view_registry_profile.py` |
| Source mapping | `docs/intake/exploratory/pass-32-view-registry-source-map.md` |

## Rollback

Remove only the files introduced by this candidate slice. No runtime registry,
route, data, source, policy, release, deployment, or publication state is mutated.
