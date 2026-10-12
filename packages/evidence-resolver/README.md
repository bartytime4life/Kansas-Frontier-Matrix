# Governed evidence resolver package

`packages/evidence-resolver/` is a reusable, non-deployable implementation
lane inherited from [`packages/`](../README.md). Its implemented behavior is
the internal, non-authoritative
`kfm/evidence-ref-bundle-candidate/v1alpha1` check plus one issue-scoped,
read-only Hydrology fixture adapter for the first #2975 lookup-and-integrity
packet.

## Boundary contract

| Field | Current boundary |
|---|---|
| Purpose | Evaluate one explicit candidate deterministically; for #2975 only, resolve stable ID `hb1` through one closed manifest to one synthetic Hydrology fixture before using that existing evaluator. |
| Scope IDs | `kfm/evidence-ref-bundle-candidate/v1alpha1`; `kfm/hydrology-evidence-bundle-fixture-adapter/v1alpha1`; local digest profile `kfm/evidence-bundle-fixture-digest/v1alpha1`. |
| Local owner | `@bartytime4life` is provisional accountable maintainer for the first #2975 packet only; package-wide `OWNER_TBD` and independent human review remain pending. |
| Belongs | Pure standard-library checks, bounded parsing, one fixed read-only fixture manifest, complete-object local digest verification, stable internal issue codes, and non-authoritative result carriers. |
| Prohibited | Caller paths, directory scanning, environment-selected paths, network or production-store access, registry/catalog/proof lookup, claim-scope inference, source admission, evidence creation, model invocation, policy evaluation, review/release decisions, public outcomes, deployment, or publication. |
| Inputs | Current proposed `EvidenceRef`, `EvidenceBundle`, and `VerificationStateHistory` shapes plus explicit lookup and bitemporal as-of snapshots; the fixture adapter accepts a stable `bundle_id`, never a path or caller-supplied bundle. |
| Policy projection | Caller supplies `policy_outcome` using the current proposed `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` vocabulary plus a decision reference; the package does not evaluate policy. |
| Output | Internal `RESOLVED`, `UNRESOLVED`, `DENIED`, or `ERROR` candidate result with `authoritative: false`. |
| Exposure | Internal alpha only; `__init__.py` remains empty and no public package API or production consumer is declared. |
| Mutation/retention | None. Core evaluation is pure; the adapter performs bounded reads only and retains no input or result. |
| Runtime dependencies | Python standard library only. Core evaluation has no filesystem dependency; the adapter can read only its fixed manifest, the allowlisted fixture, and no network, environment, clock, secret, model, socket, or service. |
| Rollback | Revert the adapter, manifest, selected synthetic-ref/digest refresh, focused tests, validator fixture-lane filter, and boundary documentation together. Do not fall back to direct store access. |

## Authority and finite outcomes

`RESOLVED` means only that the supplied candidate passed the named v1alpha1
checks. It is not evidence truth, semantic claim-scope closure, rights or
sensitivity clearance, a public `ANSWER`, policy approval, human review,
release readiness, or publication authority.

Status precedence is fail-closed:

1. `ERROR` for unsupported/malformed profile input or caller policy error;
2. `DENIED` when the caller supplies a bound `DENY` policy context;
3. `UNRESOLVED` for absent, inconsistent, stale, superseded, withdrawn,
   corrected, revoked, unknown, subject-mismatched, or otherwise incomplete
   closure context;
4. `RESOLVED` only when the bounded checks have no issue.

The existing runtime projection maps these names only to
`CONTINUE_GOVERNED_CHECKS`, `ABSTAIN`, `DENY`, or `ERROR`. It has no `ANSWER`
state and always returns `authoritative: false` and `renderable: false`.

## Current tree

```text
packages/evidence-resolver/
├── README.md        # package boundary and authority limits
├── pyproject.toml   # placeholder distribution identity; not a release claim
└── src/             # Python source-layout boundary
```

## Validation

Run from the repository root:

```bash
make evidence-resolver
make evidence-resolver-deny
```

The first command runs the ratcheted candidate fixtures and package tests,
including the manifest-backed adapter proof. The second requires every
negative candidate fixture and adapter condition to remain non-`RESOLVED`.
Both commands set `KFM_NO_NETWORK=1`; tests also deny socket, DNS, URL, and
process use around the adapter success path.

## Related surfaces

- implementation: [`src/`](src/README.md)
- semantic inputs: [`EvidenceRef`](../../contracts/evidence/evidence_ref.md),
  [`EvidenceBundle`](../../contracts/evidence/evidence_bundle.md), and
  [`VerificationStateHistory`](../../contracts/evidence/verification_state_history.md)
- proposed machine shapes:
  [`evidence_ref.schema.json`](../../schemas/contracts/v1/evidence/evidence_ref.schema.json),
  [`evidence_bundle.schema.json`](../../schemas/contracts/v1/evidence/evidence_bundle.schema.json),
  [`verification_state_history.schema.json`](../../schemas/contracts/v1/evidence/verification_state_history.schema.json)
- fixtures: [`fixtures/packages/evidence_resolver/`](../../fixtures/packages/evidence_resolver/README.md)
- closed fixture manifest:
  [`hydrology_bundle_manifest.json`](../../fixtures/packages/evidence_resolver/v1alpha1/repository/hydrology_bundle_manifest.json)
- sole payload:
  [`valid_1.json`](../../fixtures/domains/hydrology/evidence_bundle/valid/valid_1.json)
- validator: [`tools/validators/evidence_resolver/`](../../tools/validators/evidence_resolver/README.md)
- tests: [`tests/packages/evidence_resolver/`](../../tests/packages/evidence_resolver/README.md)
- CI: [`.github/workflows/evidence-resolver.yml`](../../.github/workflows/evidence-resolver.yml)
- source disposition:
  [`evidence-resolution-source-map.md`](../../docs/intake/exploratory/evidence-resolution-source-map.md)
- placement law: [`Directory Rules`](../../docs/doctrine/directory-rules.md)

## Open verification items

The following remain held: permanent named ownership; accepted public resolver
input/result contracts; a public `ANSWER`; canonical claim-scope representation;
authoritative production registry, correction, successor, withdrawal, review,
release, and verification-history snapshots; rights and sensitivity semantics;
universal EvidenceBundle hashing/canonicalization; governed public consumers;
package build/export/version policy; source activation; release integration;
deployment; publication; and production behavior.
