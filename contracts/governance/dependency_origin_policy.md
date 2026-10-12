# DependencyOriginPolicy

**Status:** PROPOSED static repository guard  
**Profile:** `kfm.governance.dependency-origin-policy.v1`  
**Authority:** repository supply-chain validation only; no source, evidence, policy-review, release, deployment, publication, or public-use authority

## Purpose

`DependencyOriginPolicy` defines the bounded inputs used by KFM's static dependency-origin gate. The gate detects direct dependency sources and lockfile states that would make package resolution ambiguous or vulnerable to dependency-confusion or registry-hijack behavior.

The profile is deliberately narrower than a full software-supply-chain attestation system. It checks repository-declared package-manager identity, accepted lockfile ownership, workspace binding for KFM-scoped npm packages, direct URL or VCS dependency references, lock-entry integrity, and explicit registry hosts when a lock record contains a remote URL.

## Boundary

A passing result establishes only that the inspected repository declaration satisfies this static profile. It does **not** prove:

- which registry served bytes during an installation;
- package-name reservation on any external registry;
- publisher identity, package signatures, provenance, SBOM closure, or vulnerability status;
- safe lifecycle scripts;
- release eligibility, deployment safety, or publication authority.

Those controls require separate installation receipts, attestations, runtime evidence, policy review, and release gates.

## Required behavior

The validator must:

1. require the exact repository package-manager pin declared by the policy;
2. require the single accepted lockfile and reject surfaced alternative lockfiles;
3. inspect dependency fields in the root, `apps/*`, and `packages/*` manifests;
4. require KFM-scoped npm dependencies to resolve through `workspace:` or `link:` references;
5. reject direct `git+`, `http:`, `https:`, and `file:` dependency specifiers unless a later reviewed policy explicitly admits them;
6. require integrity on ordinary remote pnpm lock entries;
7. reject remote lock URLs whose host is outside the allowlist;
8. reject Python direct references to VCS, URL, or file sources;
9. return stable `PASS`, `DENY`, or `ERROR` results with deterministic finding codes.

## Directory Rules basis

- `contracts/governance/` owns the semantic meaning of the repository-governance profile.
- `schemas/contracts/v1/governance/` owns its machine shape.
- `policy/supply_chain/` owns the proposed allow/deny configuration.
- `tools/validators/governance/` owns executable validation.
- `fixtures/` and `tests/` own proof.
- `.github/workflows/` owns hosted CI orchestration.
- `data/receipts/generated/` records AI-authoring accountability.

No new responsibility root or parallel schema, policy, receipt, proof, release, or publication home is created.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The policy and inspected declaration satisfy the bounded static checks. |
| `DENY` | A deterministic policy violation was found. |
| `ERROR` | The policy or repository input could not be read safely enough to decide. |

## Rollback

Revert the feature commit. The slice changes no dependency versions, lockfile bytes, installed packages, registry settings, external package names, credentials, deployment, or release state.
