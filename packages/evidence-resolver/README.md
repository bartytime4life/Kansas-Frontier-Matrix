# Governed evidence resolver package

`packages/evidence-resolver/` is a reusable, non-deployable implementation
lane inherited from [`packages/`](../README.md). Its implemented behavior is
the internal, non-authoritative
`kfm/evidence-ref-bundle-candidate/v1alpha1` check plus one issue-scoped,
read-only Hydrology fixture adapter for the first #2975 lookup-and-integrity
packet, plus a separate fixed synthetic Atlas packet lookup. Atlas lookup
binds original bytes and identities; it does not run candidate resolution.

## Boundary contract

| Field | Current boundary |
|---|---|
| Purpose | Evaluate one explicit candidate deterministically; resolve the fixed #2975 Hydrology fixture before evaluation; separately bind the existing synthetic Atlas packet without resolving or renaming its subject. |
| Scope IDs | `kfm/evidence-ref-bundle-candidate/v1alpha1`; `kfm/hydrology-evidence-bundle-fixture-adapter/v1alpha1`; `kfm/synthetic-atlas-fixture-lookup/v1alpha1`; Hydrology parsed-object digest profile `kfm/evidence-bundle-fixture-digest/v1alpha1`. |
| Local owner | `@bartytime4life` is provisional accountable maintainer for the first #2975 packet only; package-wide `OWNER_TBD` and independent human review remain pending. |
| Belongs | Pure standard-library checks, bounded parsing, fixed read-only fixture manifests, complete-object or exact-byte digest verification under their separate profiles, stable internal issue codes, and non-authoritative result carriers. |
| Prohibited | Caller paths, directory scanning, environment-selected paths, network or production-store access, registry/catalog/proof lookup, claim-scope inference, source admission, evidence creation, model invocation, policy evaluation, review/release decisions, public outcomes, deployment, or publication. |
| Inputs | Candidate evaluation uses current proposed `EvidenceRef`, `EvidenceBundle`, and `VerificationStateHistory` shapes plus explicit context. Hydrology lookup accepts a stable `bundle_id`; Atlas lookup accepts only its fixed candidate selector. Neither lookup accepts a caller path or bundle. |
| Policy projection | Caller supplies `policy_outcome` using the current proposed `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` vocabulary plus a decision reference; the package does not evaluate policy. |
| Output | Candidate evaluation: `RESOLVED`, `UNRESOLVED`, `DENIED`, or `ERROR`. Atlas lookup only: `FOUND`, `NOT_FOUND`, or `ERROR`. Neither surface grants authority; Atlas `FOUND` is not candidate `RESOLVED`. |
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

### Descriptor-bound fixture reads

The internal Hydrology adapter opens each fixed relative path component through
an already-open directory descriptor with `O_NOFOLLOW`. It checks the opened
file with `fstat`, accepts regular files only, opens nonblocking to avoid a FIFO
swap hanging the reader, and reads at most the byte limit plus one detection
byte. All descriptors close on success or failure. Earlier pathname checks
provide diagnostics only; they no longer authorize reopening a checked path.

This closes reproduced file and parent-directory symlink swaps between path
validation and opening. The configured repository root remains trusted; this
is not a sandbox against a hostile filesystem administrator, hard-link or
mount substitution, or a deadline guarantee for slow regular-file storage.
Platforms without descriptor-relative open and the required flags return a
finite internal `ERROR`; there is no pathname fallback. Linux is exercised by
the focused regressions; other platform behavior remains unverified.

This is a prerequisite hardening slice, not Atlas lookup implementation. The
allowlist, manifest, payload digest, resolver contracts, public negative-only
API, correction checks, and non-renderable runtime posture are unchanged.
Rollback is a joint revert of adapter, tests, and these boundary notes; it
reintroduces the reproduced read race and requires explicit review.

### Fixed synthetic Atlas lookup

[`atlas_fixture_lookup.py`](src/evidence_resolver/atlas_fixture_lookup.py)
accepts only the opaque selector `atlas-candidate:synthetic-kansas-proof-v1`.
The closed [Atlas manifest](../../fixtures/packages/evidence_resolver/v1alpha1/repository/atlas_bundle_manifest.json)
binds the existing carrier, promotion-reference fixture and full EvidenceBundle
to code-owned paths and exact SHA-256 byte pins. Manifest edits alone cannot
expand the allowlist. No caller path, bundle, policy, review or release state is
accepted; unknown selectors return `NOT_FOUND` before any filesystem read.

The lookup reuses the repaired package-internal descriptor reader, without
changing Hydrology's `hb1` manifest or digest. Each of four reads is bounded by
the reader's 128 KiB plus one detection byte; the Atlas parser admits at most
32 KiB per document. Complete captured bytes are hashed before parsing, then
candidate/subject/evidence/feature identity, scope hash and exact fixture time
are cross-bound. `FOUND` returns an immutable internal packet; serialized
diagnostics omit bytes and paths and always deny render/answer authority.

**Resolution remains HOLD.** The unmodified Atlas bundle member is
`overlay:synthetic-kansas-promotion-proof`, but the existing verification-history
schema/parser admits only `kfm://` subjects and the candidate evaluator requires
an exact subject match. Replacing the subject with an alias would violate that
binding. Tests exercise both failures against the real parser/evaluator. This
lookup preserves the subject and exposes
`atlas-lookup/verification-subject-profile-incompatible`; it neither fabricates
history nor weakens the shared schema. A reviewed contract-compatible subject
binding is the next prerequisite before candidate evaluation, followed by
explicit policy, review, release, citation and same-subject correction checks.

Both existing Make targets discover the Atlas tests. No API, Explorer, Site,
production store, cache or model consumer imports this module. This internal
fixture profile is not a public contract, source admission or promotion. Revert
the Atlas module, manifest, tests and documentation together; keep the separate
descriptor-read security repair. No live state needs rollback.

### Remaining authority gaps

The following remain held: permanent named ownership; accepted public resolver
input/result contracts; a public `ANSWER`; canonical claim-scope representation;
authoritative production registry, correction, successor, withdrawal, review,
release, and verification-history snapshots; rights and sensitivity semantics;
universal EvidenceBundle hashing/canonicalization; governed public consumers;
package build/export/version policy; source activation; release integration;
deployment; publication; and production behavior.
