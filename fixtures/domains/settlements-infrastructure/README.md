# Settlements/Infrastructure domain fixtures

`fixtures/domains/settlements-infrastructure/`

Status: draft / fixture parent lane. First synthetic payloads added under
`domain_feature_identity/`, `valid/`, `invalid/`, and `restricted/`; other
child lanes remain greenfield placeholders.

This directory holds small, synthetic, deterministic fixtures for the
Settlements/Infrastructure domain: settlement-side place identity (e.g.
`Settlement`, `GhostTown`) and infrastructure-side asset identity (e.g.
`InfrastructureAsset`, `ServiceArea`, `ConditionObservation`). These files are
examples only. They are not source data, EvidenceBundles, RunReceipts, policy
decisions, review approvals, release manifests, or published artifacts.

## Child lanes

| Lane | Status | Contents |
|---|---|---|
| [`domain_feature_identity/`](domain_feature_identity/README.md) | **Populated** | Identity-envelope fixtures per the `domain_feature_identity` contract's recommended semantics. |
| [`valid/`](valid/README.md) | **Populated** | Small positive object-family examples. |
| [`invalid/`](invalid/README.md) | **Populated** | Safe negative examples with expected errors. |
| [`restricted/`](restricted/README.md) | **Populated** | Synthetic T4 deny-by-default examples; contains no sensitive detail. |
| [`golden/`](golden/README.md) | **Populated** | Stable expected-output pair for the `Settlement` identity lookup. |
| `identity/` | Greenfield placeholder | Reserved; superseded in intent by `domain_feature_identity/` above. |
| `infrastructure/` | Greenfield placeholder | Reserved for infrastructure-side object-family fixtures beyond identity. |

## Shared posture

- All identifiers, geometries, digests, and reference URIs are synthetic (`kfm://fixture/synthetic/...` or `kfm://.../synthetic-...`) and must never be read as real settlement or infrastructure records.
- Object families follow [`contracts/domains/settlements-infrastructure/domain_feature_identity.md`](../../../contracts/domains/settlements-infrastructure/domain_feature_identity.md); the paired JSON Schemas in `schemas/contracts/v1/domains/settlements-infrastructure/` remain PROPOSED stubs (only `id` required), so a passing schema check here is a weak signal — see each child README for what it actually proves.
- Infrastructure sensitivity tiers (`T0`–`T4`) follow [`docs/domains/settlements-infrastructure/sublanes/infrastructure.md`](../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md) §7.1; nothing at `T3`/`T4` is stored with real content, only synthetic deny-path examples.
- A passing fixture check proves only the declared bounded expectation for that fixture. It does not prove settlement/infrastructure truth, evidence closure, policy approval, cultural/sovereignty review, or release readiness.

See also: [`../../README.md`](../../README.md) · [`../infrastructure-generalized/README.md`](../infrastructure-generalized/README.md) · [`.github/workflows/domain-settlements-infrastructure.yml`](../../../.github/workflows/domain-settlements-infrastructure.yml)
