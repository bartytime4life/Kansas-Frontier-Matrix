# Governed evidence resolver package

`packages/evidence-resolver/` is a reusable, non-deployable implementation
lane inherited from [`packages/`](../README.md). Its only implemented behavior
is the internal, non-authoritative
`kfm/evidence-ref-bundle-candidate/v1alpha1` check.

## Boundary contract

| Field | Current boundary |
|---|---|
| Purpose | Evaluate one explicit `EvidenceRef`, one caller-supplied `EvidenceBundle` candidate, and one caller-supplied lookup context deterministically. |
| Scope ID | `kfm/evidence-ref-bundle-candidate/v1alpha1` |
| Local owner | Evidence/proof and package stewards — `OWNER_TBD`; human review pending. |
| Belongs | Pure standard-library checks, bounded parsing, stable internal issue codes, and non-authoritative result carriers. |
| Prohibited | Network/store access, registry lookup, claim-scope inference, source admission, evidence creation, policy evaluation, review/release decisions, public outcomes, or publication. |
| Inputs | Current proposed `EvidenceRef` and `EvidenceBundle` shapes plus an explicit lookup snapshot. |
| Policy projection | Caller supplies `policy_outcome` using the current proposed `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` vocabulary plus a decision reference; the package does not evaluate policy. |
| Output | Internal `RESOLVED`, `UNRESOLVED`, `DENIED`, or `ERROR` candidate result with `authoritative: false`. |
| Exposure | Internal alpha only; `__init__.py` remains empty and no public package API or production consumer is declared. |
| Mutation/retention | None. Evaluation is pure and retains no input or result. |
| Runtime dependencies | Python standard library only; no hidden clock, environment, filesystem, DNS, socket, or service dependency in core evaluation. |
| Rollback | Revert the bounded implementation, fixtures, tests, validator, Make targets, workflow wiring, and documentation together. |

## Authority and finite outcomes

`RESOLVED` means only that the supplied candidate passed the named v1alpha1
checks. It is not evidence truth, semantic claim-scope closure, rights or
sensitivity clearance, a public `ANSWER`, policy approval, human review,
release readiness, or publication authority.

Status precedence is fail-closed:

1. `ERROR` for unsupported/malformed profile input or caller policy error;
2. `DENIED` when the caller supplies a bound `DENY` policy context;
3. `UNRESOLVED` for absent, inconsistent, stale, superseded, withdrawn, or
   otherwise incomplete closure context;
4. `RESOLVED` only when the bounded checks have no issue.

These names are package-local discussion vocabulary. Mapping them to governed
runtime outcomes remains **PROPOSED / NEEDS VERIFICATION**.

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

The first command runs all synthetic profile fixtures and 18 standard-library
tests. The second requires every negative fixture to remain non-`RESOLVED`.
Both commands set `KFM_NO_NETWORK=1`; the tests also deny socket and DNS use.

## Related surfaces

- implementation: [`src/`](src/README.md)
- semantic inputs: [`EvidenceRef`](../../contracts/evidence/evidence_ref.md),
  [`EvidenceBundle`](../../contracts/evidence/evidence_bundle.md)
- proposed machine shapes:
  [`evidence_ref.schema.json`](../../schemas/contracts/v1/evidence/evidence_ref.schema.json),
  [`evidence_bundle.schema.json`](../../schemas/contracts/v1/evidence/evidence_bundle.schema.json)
- fixtures: [`fixtures/packages/evidence_resolver/`](../../fixtures/packages/evidence_resolver/README.md)
- validator: [`tools/validators/evidence_resolver/`](../../tools/validators/evidence_resolver/README.md)
- tests: [`tests/packages/evidence_resolver/`](../../tests/packages/evidence_resolver/README.md)
- CI: [`.github/workflows/evidence-resolver.yml`](../../.github/workflows/evidence-resolver.yml)
- source disposition:
  [`evidence-resolution-source-map.md`](../../docs/intake/exploratory/evidence-resolution-source-map.md)
- placement law: [`Directory Rules`](../../docs/doctrine/directory-rules.md)

## Open verification items

The following remain held: named ownership; accepted resolver input/result
contracts; a stable public outcome vocabulary; canonical claim-scope
representation; authoritative registry and correction snapshots; rights and
sensitivity semantics; hashing/canonicalization; governed consumers; package
build/export/version policy; release integration; and production behavior.
