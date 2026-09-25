<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/explorer-web-local-development
title: Explorer Web local development
type: runbook
version: v1.1
status: retired historical guidance
owners:
  - "@bartytime4life — verified GitHub review route"
created: 2026-09-06
updated: 2026-09-25
policy_label: repository-facing
owning_root: docs/
responsibility: "Describe the supported locked-install, local-development, and focused-validation path for the repository-local Explorer Web workspace without granting deployment, source-admission, release, or publication authority."
truth_posture: "CONFIRMED repository configuration / candidate exact-head validation / NEEDS VERIFICATION hosted and human acceptance; cite-or-abstain"
related:
  - apps/explorer-web/README.md
  - pnpm-workspace.yaml
  - pnpm-lock.yaml
  - .github/workflows/ui-build.yml
  - .github/workflows/accessibility.yml
  - apps/kansas-frontier-matrix-explorer/docs/esbuild-security-remediation.md
[/KFM_META_BLOCK_V2] -->

> **Retired guidance (2026-09-25):** This runbook describes the removed `apps/explorer-web/` workbench. For local hosting, use the [standalone Site v71 source](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/codex/live-site-v71-source-20260925). Commands below are historical and do not apply to this branch.

# Explorer Web local development

**Historical status:** CONFIRMED for the former repository-local Explorer Web workspace at `apps/explorer-web/`; candidate-aligned for the current exact-version Workerd denial; `HOLD` for any dependency build script not explicitly decided by the committed version-specific policy. Live API integration, deployment, release, and publication remain outside this runbook.

Use this runbook to inspect the locked JavaScript workspace, verify the current installation policy, start the local Explorer Web development server only after a successful locked install, and run the checks that directly cover the app. Run all commands from the repository root unless a step says otherwise.

> [!IMPORTANT]
> The local app is a repository-grounded, fixture-first development surface. Starting it does not activate sources, contact a model runtime, establish a live governed API path, deploy the app, or publish KFM data. Rendered maps, fixtures, tests, and generated prose are not evidence authority.

## Prerequisites

- Node.js `>=22.13 <23`, as declared by the root and Explorer Web manifests.
- Corepack with the repository-pinned `pnpm@11.17.0` package manager.
- Git checkout of the repository with `package.json`, `pnpm-lock.yaml`, and `pnpm-workspace.yaml` present at the root.
- Python `>=3.11` with the repository test dependencies only when running the optional policy-boundary check.

Verify the JavaScript toolchain before installing dependencies:

```bash
node --version
corepack enable
pnpm --version
```

The reported Node version must satisfy `>=22.13 <23`. Run pnpm from inside the repository so Corepack can enforce the exact version in the root `packageManager` field.

## Install the locked workspace

> [!IMPORTANT]
> **Current dependency-policy checkpoint:** merged `main@44678e3d1a95670d8c0e8100269b4e2d729f6e13` resolves `workerd@1.20260911.1`, but its policy still stops at `1.20260903.1`; this candidate adds an explicit `false` decision for the current version. That value denies the install script while allowing pnpm to verify that every discovered build script has a reviewed disposition. It does not approve Workerd execution. Keep any future unlisted package/version at `HOLD`; do not run interactive `pnpm approve-builds`, add a wildcard, use `--ignore-scripts`, or relax the workflow to bypass the gate.

> The source of truth is [`pnpm-workspace.yaml`](../../pnpm-workspace.yaml); version-specific decisions must remain synchronized with the lockfile and review record.

```bash
pnpm install --frozen-lockfile
```

This command may use the package registry. It is the repository's diagnostic locked-install command: it must use the versions recorded in `pnpm-lock.yaml` and must not update the lockfile. Continue to the development or validation commands only when it exits successfully under a reviewed repository build-script policy. Stop and investigate any manifest/lock mismatch or ignored-build finding instead of switching to an unlocked install or inventing local policy.

## Start Explorer Web

Continue only after the locked install succeeds under a supported Node 22 runtime. A previously populated `node_modules/` directory is not proof that the current lockfile and build-script policy were installed successfully.

```bash
pnpm --filter explorer-web dev
```

Open the local URL printed by Vite, normally `http://localhost:5173/`. Stop the server with `Ctrl+C`.

The default entrypoint mounts the repository-local Explorer composition and bounded synthetic Focus and trust surfaces. It does not prove a production route tree, admitted live renderer, live Governed API transport, deployment, release, or publication.

## Focused validation

Run the smallest command that covers the change, then use the combined app test when the change spans multiple surfaces.

| Check | Command | What it establishes |
|---|---|---|
| Type-check and production bundle | `pnpm --filter explorer-web build` | TypeScript accepts the app and Vite can write `apps/explorer-web/dist/`. |
| Unit tests | `pnpm --filter explorer-web test:unit` | The app's `tests/*.test.ts` fixture and projection checks pass. |
| Browser tests | `pnpm --filter explorer-web test:browser` | Playwright can exercise the deterministic HTML fixtures through its local Vite server. |
| Full app check | `pnpm --filter explorer-web test` | Unit and browser test scripts both pass in sequence. |
| Renderer/store boundary | `python -m pytest -q tests/policy/test_explorer_web_adapter_boundary.py` | Explorer source avoids raw renderer imports and forbidden internal-store path literals. |

The browser suite starts its own server at `http://127.0.0.1:4173` with strict port binding. Keep port `4173` free. If Playwright reports that its local Chromium executable is missing, install that test dependency and retry:

```bash
pnpm --filter explorer-web exec playwright install chromium
```

Do not use root `pnpm build`, `pnpm test`, or `pnpm lint` as Explorer validation. Those root scripts are intentional `WORKFLOW_HOLD` placeholders. Use the `explorer-web` filter or `make ui-build` for the implemented build lane.

## Safe failure and troubleshooting

| Symptom | Check | Recovery |
|---|---|---|
| Corepack or pnpm selects another version | Root `package.json` still declares `pnpm@11.17.0` | Re-enable Corepack from the repository root; do not edit the pin merely to bypass the mismatch. |
| Install wants to rewrite `pnpm-lock.yaml` | Manifest and lockfile are out of sync | Stop. Reconcile the dependency change in its own reviewed change rather than using an unlocked install. |
| Install reports `ERR_PNPM_IGNORED_BUILDS` | The reported package/version has no exact decision in the committed version-specific `allowBuilds` policy | Keep install and dependent checks at `HOLD`. Route that exact package/version through dependency and supply-chain review; do not approve scripts interactively or weaken the locked install. |
| Vite cannot start | The printed port is already occupied | Stop the conflicting local process or use an explicit local-only port for manual development. Browser tests still require free port `4173`. |
| Browser tests cannot launch | Local Chromium is absent or an explicit executable is invalid | Install Playwright Chromium, or set `KFM_CHROMIUM_EXECUTABLE` to a verified local executable. Do not commit machine-specific paths. |
| Tests pass but a trust-bearing state looks wrong | Fixture, adapter, and finite-outcome inputs may disagree | Treat the UI as a consumer. Correct the owning contract, fixture, policy, evidence, or release artifact through its own reviewed path; do not make the UI invent authority. |

For a failing check, preserve the exact command, exit code, relevant output, and commit under test. A local pass is validation evidence for that revision only; it is not human review, governance adoption, release, deployment, promotion, or publication.

## Related repository evidence

- [Explorer Web app boundary and maturity](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/13f66982ef1db9dc733ed3588d42bf1b92e19e8d/apps/explorer-web/README.md)
- [Explorer Web scripts and engine range](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/13f66982ef1db9dc733ed3588d42bf1b92e19e8d/apps/explorer-web/package.json)
- [Locked CI build and test lane](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/13f66982ef1db9dc733ed3588d42bf1b92e19e8d/.github/workflows/ui-build.yml)
- [Explorer renderer and internal-store boundary test](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/13f66982ef1db9dc733ed3588d42bf1b92e19e8d/tests/policy/test_explorer_web_adapter_boundary.py)
- [Accepted Directory Rules adoption](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
