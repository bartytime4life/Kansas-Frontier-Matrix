# Explorer Web local development

**Status:** CONFIRMED for the repository-local Explorer Web workspace at `apps/explorer-web/`; `HOLD` for any dependency build script not explicitly allowed by the committed version-specific policy; live API integration, deployment, release, and publication remain outside this runbook.

Use this runbook to inspect the locked JavaScript workspace, identify the current installation hold, and—only after that hold is resolved—start the local Explorer Web development server and run the checks that directly cover the app. Run all commands from the repository root unless a step says otherwise.

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

> [!WARNING]
> **Current repository checkpoint: `HOLD` for denied build scripts.** At `main@19809b21d393c40af7a5d978d9b010e3a8e9eb9a`, the workspace carries a version-specific `allowBuilds` policy. It allows `esbuild@0.28.2` and denies `esbuild@0.18.20`, `esbuild@0.25.12`, `esbuild@0.28.1`, `unrs-resolver@1.12.2`, and `workerd@1.20260828.1`. An `ERR_PNPM_IGNORED_BUILDS` result therefore means the reported package/version is outside the approved set, not that no policy exists. Keep the install and dependent checks at `HOLD`; route the exact package/version through dependency and supply-chain review. Do not run interactive `pnpm approve-builds`, add a broad allowlist, use `--ignore-scripts`, or relax the workflow merely to bypass the hold.

> The source of truth is [`pnpm-workspace.yaml`](../../pnpm-workspace.yaml); version-specific decisions must remain synchronized with the lockfile and review record.

```bash
pnpm install --frozen-lockfile
```

This command may use the package registry. It is the repository's diagnostic locked-install command: it must use the versions recorded in `pnpm-lock.yaml` and must not update the lockfile. Continue to the development or validation commands only when it exits successfully under a reviewed repository build-script policy. Stop and investigate any manifest/lock mismatch or ignored-build finding instead of switching to an unlocked install or inventing local policy.

## Start Explorer Web

This section is unavailable while the locked-install hold above remains active. A previously populated `node_modules/` directory is not proof that the current lockfile and build-script policy were installed successfully.

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
| Install reports `ERR_PNPM_IGNORED_BUILDS` | The reported package/version is denied by the committed version-specific `allowBuilds` policy | Keep install and dependent checks at `HOLD`. Route the exact package/version through dependency and supply-chain review; do not approve scripts interactively or weaken the locked install. |
| Vite cannot start | The printed port is already occupied | Stop the conflicting local process or use an explicit local-only port for manual development. Browser tests still require free port `4173`. |
| Browser tests cannot launch | Local Chromium is absent or an explicit executable is invalid | Install Playwright Chromium, or set `KFM_CHROMIUM_EXECUTABLE` to a verified local executable. Do not commit machine-specific paths. |
| Tests pass but a trust-bearing state looks wrong | Fixture, adapter, and finite-outcome inputs may disagree | Treat the UI as a consumer. Correct the owning contract, fixture, policy, evidence, or release artifact through its own reviewed path; do not make the UI invent authority. |

For a failing check, preserve the exact command, exit code, relevant output, and commit under test. A local pass is validation evidence for that revision only; it is not human review, governance adoption, release, deployment, promotion, or publication.

## Related repository evidence

- [Explorer Web app boundary and maturity](../../apps/explorer-web/README.md)
- [Explorer Web scripts and engine range](../../apps/explorer-web/package.json)
- [Locked CI build and test lane](../../.github/workflows/ui-build.yml)
- [Explorer renderer and internal-store boundary test](../../tests/policy/test_explorer_web_adapter_boundary.py)
- [Accepted Directory Rules adoption](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
