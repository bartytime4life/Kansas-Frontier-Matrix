<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/explorer-eslint10-compatibility
title: Explorer ESLint 10 React context compatibility
type: implementation-note
version: v0.1
status: proposed; branch-only; human-review-pending
owners: ["@bartytime4life"]
created: 2026-09-05
updated: 2026-09-05
policy_label: public
owning_root: docs/
responsibility: Explain the bounded app-owned lint compatibility bridge, regression coverage, and rollback without becoming validation or release authority.
truth_posture: exact-source evidence only
[/KFM_META_BLOCK_V2] -->

# Explorer ESLint 10 React context compatibility

This is a lint-only continuation stacked on the separately frozen TypeScript/Worker repair at `343a516812596f0b29fdb1a56b3a549edbe43490`. That dependency is not yet main. Main was independently pinned to `8b9c52d88687986879c8f87d7e3835f6a58bbacd`. Neither pin is deployment evidence. Re-pin before delivery.

## Scope and ownership

The existing application owns [its ESLint configuration](../../apps/kansas-frontier-matrix-explorer/eslint.config.mjs) and the adjacent [context adapter](../../apps/kansas-frontier-matrix-explorer/eslint-react-context.mjs). Cross-surface executable regressions live under [tests/ui](../../tests/ui/test_explorer_lint_compat.mjs). This explanation stays in the existing `docs/quality/` human-readable lane under accepted [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md); it does not canonize or migrate that lane. No new root or parallel validator is introduced.

## Why a narrow bridge

The locked stack uses ESLint 10.9.1, Next lint config 16.3.3 and React plugin 7.37.5. On the frozen repaired baseline, React version detection calls the removed `context.getFilename()` method and prevents lint from running. [ESLint's migration guidance](https://eslint.org/docs/latest/use/migrate-to-10.0.0) describes the property-based replacement API.

The app-owned adapter forwards only `getFilename`, `getPhysicalFilename`, `getCwd`, `getSourceCode`, and `parserOptions` to their current context equivalents. It wraps the React plugin only. It does not replace SourceCode, alter visitors, change reports, catch plugin exceptions, change rule severities/options, broaden ignores, modify installed package files, downgrade ESLint, or add a dependency. Unknown incompatible APIs still fail visibly. The adapter is a local compatibility boundary, not a claim of general upstream ESLint-10 support for this plugin.

The official `@eslint/compat` utility was evaluated as an alternative; it implements a broader rule/SourceCode compatibility layer and would change the dependency closure. Replacing the React plugin would require a separate rule-by-rule migration. This narrower dependency-free bridge preserves the existing locked stack and is bounded by the executable checks below.

## Validation and removal triggers

With the repository's frozen workspace installation, run from the repository root:

```sh
pnpm install --frozen-lockfile
pnpm --filter kansas-frontier-matrix-explorer run build
node --test apps/kansas-frontier-matrix-explorer/tests/*.test.mjs
pnpm --filter kansas-frontier-matrix-explorer exec tsc --noEmit
pnpm --filter kansas-frontier-matrix-explorer run lint
pnpm --filter kansas-frontier-matrix-explorer run test:lint
```

`test:lint` is also exposed through the npm `posttest` lifecycle without changing the existing literal `test` command. Runners that bypass lifecycle hooks must call `test:lint` explicitly. The original root-working-directory Node suite remains a separate command; this change does not repair its historical cwd assumptions.

The compatibility regressions compare effective rules, options, parser configuration, settings, plugin membership and ignores for JavaScript, ESM, JSX, TypeScript and TSX. They retain negative React, Hooks, TypeScript, import and accessibility findings; syntax errors; nonzero CLI failure; exact metadata forwarding; and exception propagation. Next's already-disabled unknown-property rule remains disabled rather than being silently enabled. Rule inventory and metadata are preserved, but individual execution of every disabled React rule is not claimed.

The unadapted negative control uses a fresh process because React's version cache can conceal the failure after a successful adapted lint. Initial test-authoring failures and their correction remain in branch history; they are not relabeled as successful evidence.

Remove the bridge only after a locked upstream replacement runs unwrapped successfully, effective configurations retain intended coverage, negative fixtures remain effective, and the complete app lint/build/Node/typecheck lanes pass. A changed dependency, compiler, parser or Next configuration requires renewed exact-head checks.

## Evidence, review and rollback

Use the add-only GeneratedReceipt and exact Actions artifacts for results. A diagnostic branch may temporarily use the existing accessibility workflow file as a transport, but that is not accessibility or browser validation and must never be merged. Product scope contains no workflow change. Diagnostic gate collection preserves every raw exit code and an aggregate nonzero exit; a successful collection step is not an all-green result.

Topology remains separately governed by #4228; unchanged inherited diagnostics are attribution, not a waiver. Human review, #4024 delivery-state controls, merge, release and deployment remain separate decisions.

Rollback this lint unit by reverting its app configuration, adapter, package-script additions and regression together. Preserve the TypeScript/Worker prerequisite, all historical receipts and the frozen Layer Library branch. Add a correction receipt rather than rewriting an earlier GeneratedReceipt. No data, map, source-admission, Worker runtime, public Site or deployment state is changed by this unit.
