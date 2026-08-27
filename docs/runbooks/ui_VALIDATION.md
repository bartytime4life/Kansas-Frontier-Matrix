# Explorer Web validation

**Status:** CONFIRMED for the repository-local Explorer Web checks described below. Whole-system end-to-end coverage, automated axe coverage, WCAG conformance, live service integration, deployment, release, and publication remain unproven or explicitly held.

Use this runbook to choose, execute, and interpret validation for changes affecting `apps/explorer-web/`. Run commands from the repository root after completing the setup in [Explorer Web local development](./ui_LOCAL_DEV.md).

> [!IMPORTANT]
> Validation is evidence about one revision and one declared scope. A passing build, unit test, browser test, workflow, screenshot, or accessibility smoke does not authorize source use, prove a claim, accept governance, approve a release, deploy the app, or publish KFM data.

## Validation principles

- Pin the commit under test and record the exact command.
- Start with the smallest check that exercises the changed behavior.
- Include negative and fail-closed cases when a trust-bearing state changes.
- Run the full Explorer test command when a change crosses unit and browser boundaries.
- Keep `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` behavior distinct where the affected surface uses finite outcomes.
- Classify held, skipped, unavailable, and unrelated checks honestly; never translate them into a pass.
- Do not weaken fixtures, assertions, browser journeys, or trust boundaries merely to obtain green output.

## Local command matrix

| Change surface | Minimum repository command | Add when relevant |
|---|---|---|
| TypeScript, Vite configuration, package wiring, or production composition | `pnpm --filter explorer-web build` | Unit or browser checks covering the changed behavior |
| Adapter, parser, projection, view model, fixture behavior, or finite outcome | `pnpm --filter explorer-web test:unit` | Boundary test for renderer or internal-store changes |
| DOM interaction, keyboard flow, focus behavior, responsive state, or browser fixture | `pnpm --filter explorer-web test:browser` | Target the affected Playwright spec during iteration |
| Change spanning unit and browser surfaces | `pnpm --filter explorer-web test` | Production build before handoff |
| Renderer acquisition or Explorer access to internal-store paths | `python -m pytest -q tests/policy/test_explorer_web_adapter_boundary.py` | Package-owned MapLibre tests when that package changes |
| Documentation-only UI guidance | Focused Markdown structure and link checks | Do not claim application behavior from documentation checks |

The app scripts resolve to the commands in `apps/explorer-web/package.json`:

- `build` runs TypeScript with `--noEmit` and then creates a Vite production bundle.
- `test:unit` runs the tracked `tests/*.test.ts` Vitest set.
- `test:browser` runs Playwright with `apps/explorer-web/playwright.config.ts`.
- `test` runs unit and browser checks in sequence.

Root `pnpm build`, `pnpm test`, and `pnpm lint` remain intentional `WORKFLOW_HOLD` placeholders. They are not substitutes for the filtered Explorer commands.

## Recommended handoff sequence

For an ordinary implementation change that affects the rendered Explorer surface:

```bash
pnpm --filter explorer-web test:unit
pnpm --filter explorer-web test:browser
pnpm --filter explorer-web build
python -m pytest -q tests/policy/test_explorer_web_adapter_boundary.py
```

The Python boundary check is required only when the change could affect renderer imports or access to internal-store paths. Record it as not run when it is unrelated rather than implying coverage.

To reproduce the repository's bounded keyboard and focus smoke locally, run the exact tracked Playwright subset:

```bash
pnpm --filter explorer-web exec playwright test \
  --config=playwright.config.ts \
  tests/browser/citation-pill.spec.ts \
  tests/browser/evidence-drawer.spec.ts \
  tests/browser/evidence-tooltip.spec.ts \
  tests/browser/focus-composed-claim.spec.ts \
  tests/browser/map-evidence-drawer.spec.ts \
  tests/browser/map-runtime-trust-status.spec.ts \
  tests/browser/time-banner.spec.ts \
  tests/browser/workspace-navigation.spec.ts
```

This subset checks named keyboard/focus journeys. It is not an axe scan, manual assistive-technology review, reduced-motion audit, whole-app accessibility assessment, or WCAG conformance result.

## Hosted workflow interpretation

| Workflow or job | Current implemented signal | Required interpretation |
|---|---|---|
| `ui-build / build-explorer-web` | Locked install plus filtered production build | Build evidence for the exact workflow revision only |
| `ui-build / test-explorer-web` | Locked install plus full Explorer unit and browser command | Test evidence for the exact workflow revision only |
| `accessibility / keyboard-navigation` | Bounded Playwright keyboard and focus subset | Partial interaction coverage, not full accessibility conformance |
| `accessibility / axe` | `WORKFLOW_SKIPPED_EXPLICIT` with `WORKFLOW_HOLD` | No axe ruleset or automated axe validation ran |
| `e2e-smoke` | Readiness checks with explicit holds for the mock runtime and combined Explorer/API suite | No accepted whole-system E2E execution occurred |

A workflow name, green check, or completed status must be interpreted with its job steps and summary. In particular, a successfully completed reporting job can still record that the underlying validation is held or skipped.

## Failure classification

| Classification | Meaning | Handoff action |
|---|---|---|
| Introduced | Reproduces on the branch head but not its exact base under the same command and environment | Fix before handoff or narrow the change |
| Inherited | Reproduces on both exact base and head | Report separately; do not broaden this change unless it blocks the selected outcome |
| Skipped or held | The workflow deliberately did not execute the claimed validation | Preserve the explicit hold and do not call it a pass |
| Not run | The command was outside the selected validation scope | List it plainly with the reason |
| Unavailable | Required tooling or environment could not execute | Record the blocker; do not infer the expected result |
| Pending | Hosted execution has not settled for the exact head | Avoid final hosted-check conclusions |
| Unknown | Evidence cannot distinguish the state | Keep the claim unresolved |

When classifying a failure, compare the same command against the exact base and head. Do not compare different revisions, environments, dependency states, or test selections as if they were equivalent.

## Evidence to retain

A review handoff should include:

- base and head commit SHAs;
- exact changed paths;
- tool versions when they affect reproducibility;
- each command, exit result, and relevant summary;
- focused negative or fail-closed cases;
- hosted run links tied to the exact head;
- introduced and inherited findings;
- skipped, held, unavailable, pending, and not-run checks;
- known limits on runtime, accessibility, evidence, policy, review, release, deployment, and publication conclusions.

Screenshots and rendered output may help visual review, but they do not replace structured fixtures, assertions, evidence bindings, or accessible non-visual checks.

## Stop conditions

Stop and report the gap instead of weakening validation when:

- the lockfile and manifests disagree;
- a test depends on a live source, private endpoint, credential, model provider, or publication target not admitted for the check;
- a negative state would need to be removed or converted into a positive fixture;
- an accessibility or E2E hold is being described as completed coverage;
- a browser change would bypass the KFM-owned renderer boundary or read an internal lifecycle store;
- the observed result belongs to another commit or cannot be reproduced against the exact base and head.

## Lineage and repository evidence

The original scaffold cited the Agriculture and Fauna map/UI contracts. Preserve those documents as domain design lineage; their proposed validators, paths, and maturity claims do not override current repository implementation.

- [Agriculture map and UI contract](../domains/agriculture/MAP_UI_CONTRACTS.md)
- [Fauna map and UI contract](../domains/fauna/MAP_UI_CONTRACTS.md)
- [Explorer Web local development](./ui_LOCAL_DEV.md)
- [Explorer Web app boundary and maturity](../../apps/explorer-web/README.md)
- [Explorer Web package scripts](../../apps/explorer-web/package.json)
- [Explorer build and test workflow](../../.github/workflows/ui-build.yml)
- [Accessibility workflow and explicit holds](../../.github/workflows/accessibility.yml)
- [End-to-end readiness workflow](../../.github/workflows/e2e-smoke.yml)
- [Explorer renderer and internal-store boundary test](../../tests/policy/test_explorer_web_adapter_boundary.py)
