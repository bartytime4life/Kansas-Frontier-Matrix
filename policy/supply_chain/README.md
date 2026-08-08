<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/supply-chain/readme/v1
title: Supply-Chain Policy Family
type: policy-family-readme
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: public
related:
  - ./pnpm_dependency_policy.json
  - ../../tools/validators/dependencies/pnpm_supply_chain_policy.py
  - ../../tools/validators/dependencies/README.md
  - ../../docs/security/SUPPLY_CHAIN.md
  - ../../.npmrc
  - ../../.github/workflows/dependency-scan.yml
  - ../../.github/workflows/ui-build.yml
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, policy, supply-chain, pnpm, registry, lockfile, lifecycle-scripts]
notes:
  - "This family is PROPOSED until the governing pull request is accepted."
  - "The .invalid internal-scope endpoint is a deny sink, not an internal mirror."
[/KFM_META_BLOCK_V2] -->

# Supply-Chain Policy Family

This directory owns machine-evaluable package supply-chain rules. It does not own package-manager configuration, validators, tests, workflows, vulnerability findings, release decisions, or publication state.

## Current policy

`pnpm_dependency_policy.json` defines the first bounded implementation of:

- `KFM-P8-PROG-0007` — dependency-confusion defenses;
- `KFM-P8-PROG-0008` — explicit registry and namespace isolation;
- `KFM-P8-PROG-0009` — deterministic lockfile SHA-256 sealing;
- `KFM-P8-PROG-0016` — lifecycle-script suppression in install lanes.

The policy is intentionally fail-closed:

- third-party dependencies resolve only through the explicit public registry;
- reusable internal packages must use `@kfm/*` identities;
- `@kfm/*` dependencies must use `workspace:<exact-semver>`;
- the `@kfm` registry mapping points to `https://registry.invalid/`, a non-production deny sink that prevents accidental public fallback;
- no repository claim is made that an internal package registry or mirror exists;
- dependency declarations must be exact semver, except for the three byte-visible root ranges listed in the bounded exception register;
- every external lockfile package must carry SHA-512 integrity and must not use URL, tarball, file, or link resolution;
- the complete `pnpm-lock.yaml` byte stream must match the recorded SHA-256 seal;
- package installation in workflows must use pnpm, a frozen lockfile, explicit script suppression, and both npm/pnpm ignore-script environment variables.

## Authority separation

| Responsibility | Owning location |
|---|---|
| Normative allow/deny rules | `policy/supply_chain/` |
| Package-manager configuration | root `.npmrc` |
| Deterministic validator | `tools/validators/dependencies/` |
| Conformance tests | `tests/validators/` |
| CI integration | `.github/workflows/` |
| Human security and operations guidance | `docs/security/` |
| Generated provenance | `data/receipts/generated/` |

This placement follows ADR-0029 and does not create a parallel policy, schema, release, proof, or receipt authority.

## Change discipline

A policy change must update its validator/tests and generated receipt in the same review boundary. A lockfile change must update the SHA-256 seal from the exact reviewed bytes. A version-range exception disappears as soon as its exact manifest declaration changes; stale exceptions fail validation.

Adding an actual internal registry, mirror, signature verifier, or external transparency-log dependency requires a separate governed design and accepted configuration. The deny sink must not be replaced with an invented endpoint.
