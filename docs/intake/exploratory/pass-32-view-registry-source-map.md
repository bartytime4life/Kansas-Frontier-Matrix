# Pass 32 view-registry source map

**Status:** PROPOSED / NEEDS REVIEW

**Implementation posture:** fixture-only contract profile; inactive

**Source inspected:** `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf`

## Candidate mapping

| Source card | Candidate idea | Repository response | Deliberate exclusions |
|---|---|---|---|
| `KFM-P32-IDEA-0008` | Resolve UI views through a contract-first registry carrying catalog, tile/render, performance, and access-policy context rather than binding routes directly to graph stores. | Adds a closed `ViewRegistryProfile` schema, deterministic no-network validator, synthetic cases, focused tests, and CI. | No live route, registry instance, graph adapter, tile source, catalog assertion, or activation. |
| `KFM-P32-FEAT-0004` | Provide a view-registry inspector. | Makes proposed registry records deterministic and inspectable by tooling. | No UI inspector or application component is implemented. |

## Repository gap check

The current repository already states that public clients must not read internal
stores and already contains UI contract, catalog, Evidence Drawer, layer-manifest,
and release surfaces. The inspected tree did not contain an executable
`ViewRegistryProfile` schema/validator/fixture family. This slice therefore adds
the smallest dependency-closed validation profile and does not duplicate the
existing governed API route registry.

## Governance interpretation

The atlas cards are proposal inputs, not implementation or activation evidence.
This source map preserves that distinction:

- fixture declarations do not prove referenced STAC/DCAT/PROV records exist;
- a declared `READY` closure means only that the synthetic packet selected that
  finite state;
- validation grants no route, source, policy, review, release, deployment, or
  publication authority;
- ADR-0029 continues to govern placement by responsibility.

## Acceptance evidence for this slice

- JSON Schema Draft 2020-12 validation;
- deterministic RFC 8785 JCS + SHA-256 registry identity;
- exact positive, abstaining, denying, and error fixture polarity;
- duplicate route/view and ordering checks;
- direct-store and embedded-query rejection;
- fixed-false authority fields;
- no-network test and a read-only CI workflow.
