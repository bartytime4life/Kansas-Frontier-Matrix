<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/explorer-reviewed-integration
title: Reviewed Explorer stack integration
version: v0.1
status: branch-only; integration-validation-required
owners: ["@bartytime4life"]
created: 2026-09-05
updated: 2026-09-05
policy_label: public
owning_root: docs/
responsibility: Explain the exact reviewed stack composition, compiler-loader correction and validation boundaries without creating lifecycle authority.
[/KFM_META_BLOCK_V2] -->

# Reviewed Explorer stack integration

This branch combines the preserved Library `8e4167852d9037cc308ee744501f2172a6ee44f9` and lint/TypeScript/Worker stack `bf1335ad7250dec6334f62ad86d1032f0df7ef61` with main `a9a53470e385350b795f6d978ad3e7a5811961c5`. Commit `d550c452382c626bc871d921199af5dea2fabaa7` has those three parents and preserves the exact reviewed source bytes. The original branches and historical receipts remain unchanged. Main's merged temporal repair and build-source-context guard remain present.

The owner supplied the continuation: "Make all the changes. I have reviewed it". That records review of the presented handoff and permits this implementation continuation. It does not mean the owner pre-reviewed subsequently discovered integration corrections, independently reviewed their own work, or authorized a topology waiver, an incident-quarantined PR transition, source admission or deployment.

## Compiler integration correction

The original Library test loaders required `devDependencies.typescript` to be a plain exact version. The reviewed toolchain uses `@typescript/native: npm:typescript@7.0.2` for the compiler and the `typescript` name for the classic TypeScript 6 API. Combining the reviewed inputs therefore caused both Library test files to stop before their assertions.

The shared [test-only selector](../../apps/kansas-frontier-matrix-explorer/tests/declared-typescript.mjs) selects the declared CLI, verifies exact manifest/lock/installed identities and bin confinement, and refuses ambient/global fallback. Strict file-list compilations execute in their temporary output directory so an invoking app directory cannot accidentally supply an unrelated tsconfig. No compiler options, production tsconfig, dependencies, locks, build-script policy, application state contracts or existing test assertions are weakened. [Thirteen focused resolver regressions](../../apps/kansas-frontier-matrix-explorer/tests/declared-typescript.test.mjs) cover exact plain/native declarations, missing or mismatched installations, lock mismatch, and escaping entrypoints. Resolver identity checks do not independently rehash installed tarball contents; the frozen installer remains the integrity boundary.

## Native commands and evidence boundaries

From the complete repository after `pnpm install --frozen-lockfile`:

```sh
pnpm --filter kansas-frontier-matrix-explorer exec npm test
pnpm --filter kansas-frontier-matrix-explorer exec tsc --noEmit
pnpm --filter kansas-frontier-matrix-explorer run lint
pnpm --filter kansas-frontier-matrix-explorer run test:lint
pnpm --filter explorer-web run build
pnpm --filter explorer-web run test:unit
pnpm --filter explorer-web run test:browser
```

The actual Library browser suite visits the HTTP-served existing Vinext/React app on loopback. It is not an injected replacement host, a public Sites deployment, live-source admission or renderer/GPU proof. Preserve its zero-off-origin-request assertion. Explicit lint command success and its warning count are separate facts; warnings must not be described as zero unless the raw output establishes that.

The diagnostic branch `validation/explorer-reviewed-integration-20260905` has a separate workflow which checks out literal product and main commits. Never merge that diagnostic branch. Raw gate outcomes and exact product hashes, not diagnostic workflow-head labels or collection-step success, are authoritative for results. The original Library validation workflow remains in product history; its old-branch trigger does not provide automatic current-branch coverage.

Topology remains under #4228. No baseline, correction register, Directory Rules or validator is changed. #4024's missing-authorization incident evidence still requires a separately proven draft delivery boundary; owner artifact review is not a technical fix to that path. Exact results and new provenance belong in add-only receipts and the coordination records after execution.

## Rollback

Revert the test-only selector, its regression and the two loader changes together to return to `d550c452...`; this intentionally restores the known loader incompatibility. To back out the combined stack, revert the integration merge against first parent main `a9a5347...` as one dependency-closed operation after checking intervening edits. Keep the original feature branches, historical receipts, user workspaces, main's temporal repair and build guard. Do not delete evidence or alter access/release state as rollback shorthand.
