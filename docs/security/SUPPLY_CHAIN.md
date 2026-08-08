<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://docs/security/supply-chain/v1
title: pnpm Supply-Chain Controls
type: security-guide
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: public
related:
  - ../../policy/supply_chain/pnpm_dependency_policy.json
  - ../../policy/supply_chain/README.md
  - ../../tools/validators/dependencies/pnpm_supply_chain_policy.py
  - ../../tools/validators/dependencies/README.md
  - ../../tests/validators/test_pnpm_supply_chain_policy.py
  - ../../.npmrc
  - ../../.github/workflows/dependency-scan.yml
  - ../../.github/workflows/ui-build.yml
tags: [kfm, security, dependency-confusion, registry-isolation, lockfile, pnpm]
notes:
  - "This guide documents a repository-local, no-network validator and workflow controls."
  - "It does not assert that a private registry, mirror, signature service, or transparency log is deployed."
[/KFM_META_BLOCK_V2] -->

# pnpm Supply-Chain Controls

## Goal and status

**PROPOSED:** KFM's first package supply-chain enforcement slice makes dependency identity, registry choice, lockfile bytes, integrity metadata, and lifecycle-script behavior reviewable and deterministic.

**CONFIRMED in the implementation branch after validation:** the validator performs no network request or package installation. Workflow installation remains a separate action and must satisfy the policy before CI proceeds.

## Threat model

The controls address four bounded risks:

1. **Dependency confusion:** a public package collides with an intended internal identity.
2. **Registry ambiguity:** a package manager silently falls back to a source that was not reviewed.
3. **Lockfile drift:** dependency graph bytes change without a corresponding reviewed seal update.
4. **Install-time execution:** a dependency lifecycle script executes during CI installation.

The slice does not yet establish a private registry, organization-wide mirror, package signing service, transparency log, or external provenance service. Those capabilities remain **NEEDS VERIFICATION** and must not be inferred from this policy.

## Resolution boundary

The root `.npmrc` makes the third-party source explicit:

```ini
registry=https://registry.npmjs.org/
```

Reusable internal packages use the `@kfm/*` namespace. The namespace maps to a deny sink:

```ini
@kfm:registry=https://registry.invalid/
```

This endpoint is deliberately non-operational. Internal dependencies must therefore resolve as workspace links using `workspace:<exact-semver>`. A missing workspace package fails instead of falling back to a public registry.

Private applications under `apps/` keep their deployable application names. Reusable packages under `packages/` must be private and use `@kfm/*` names.

## Version and integrity rules

New dependency declarations use exact semantic versions. The current root manifest contains three historical range declarations. They are listed byte-for-byte in the policy exception register and cannot be generalized. Changing or removing any declaration makes the corresponding exception stale and fails validation.

The lockfile gate requires:

- pnpm lockfile version `9.0`;
- a SHA-256 seal over the entire `pnpm-lock.yaml` byte stream;
- SHA-512 integrity on every external package resolution;
- no URL, tarball, file, or link resolution in the external package block;
- no externally resolved `@kfm/*` package;
- no competing root lockfile.

The SHA-256 seal is evidence of byte identity, not proof that a dependency is safe. Vulnerability audit, source review, license review, and dependency admission remain separate controls.

## Lifecycle-script suppression

Repository configuration sets:

```ini
ignore-scripts=true
```

Every workflow that installs packages must additionally set:

```yaml
env:
  NPM_CONFIG_IGNORE_SCRIPTS: "true"
  PNPM_CONFIG_IGNORE_SCRIPTS: "true"
```

and invoke:

```bash
pnpm install --frozen-lockfile --ignore-scripts
```

The validator denies npm, Yarn, or Bun install commands in workflow run blocks. It also denies pnpm installation without both required flags or without both environment settings.

CI must not enable lifecycle scripts as an exception. A dependency that requires install-time execution must be redesigned, replaced, or handled through a separately governed build artifact rather than weakening this lane.

## Operator commands

Repository-local policy validation:

```bash
python tools/validators/dependencies/pnpm_supply_chain_policy.py
```

Existing package-manager and workspace readiness validation:

```bash
python tools/validators/dependencies/pnpm_audit_readiness.py validate-repository
```

Focused tests:

```bash
python -m pytest -q \
  tests/validators/test_pnpm_audit_readiness.py \
  tests/validators/test_pnpm_supply_chain_policy.py
```

The supply-chain validator exits `0` only for `PASS`; invalid policy, registry, manifest, lockfile, integrity, or workflow state exits `2` with deterministic JSON findings. It never repairs files automatically.

## Lockfile update procedure

1. Change the dependency manifest through a reviewed branch.
2. Regenerate `pnpm-lock.yaml` using the pinned pnpm and Node versions with scripts disabled.
3. Review the complete manifest and lockfile diff.
4. Compute SHA-256 from the exact lockfile bytes.
5. Replace `policy.lockfile.sha256` with `sha256:<digest>`.
6. Run both dependency validators and focused tests.
7. Refresh the generated receipt hashes.
8. Require exact-head hosted checks before review disposition.

A seal mismatch is a hold, not permission to update the policy automatically. The reviewed lockfile bytes must determine the seal.

## Failure response

| Finding class | Required response |
|---|---|
| Registry or `.npmrc` mismatch | Stop installation; restore reviewed explicit settings. |
| Public/internal identity ambiguity | Deny dependency admission; correct the package namespace and workspace reference. |
| Non-exact declaration | Pin exactly or add a narrowly reviewed temporary exception. |
| Stale exception | Remove the exception and retain the exact declaration. |
| Missing integrity or unsafe resolution | Quarantine the lockfile change; regenerate from an approved source. |
| Lockfile SHA mismatch | Compare exact bytes; update the seal only as part of the reviewed lockfile change. |
| Lifecycle-script guard missing | Stop the workflow; restore environment and command-line suppression. |

## Rollback

This slice is additive except for guarded workflow commands. Repository rollback is a normal revert of the policy, `.npmrc`, validator, tests, docs, workflow edits, and generated receipt. No package is installed, registry is activated, data is migrated, or release/publication state is changed by the validator itself.
