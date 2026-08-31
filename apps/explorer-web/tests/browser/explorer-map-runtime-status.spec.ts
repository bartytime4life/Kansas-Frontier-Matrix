import { expect, test, type Page } from "playwright/test";

import {
  governedAnswerResponse,
  governedDenyResponse,
  governedErrorResponse,
  governedLayerResponse,
} from "./governed-map-api-fixtures";

async function routeLayers(page: Page, body: unknown = governedLayerResponse) {
  await page.route("**/layers", (route) =>
    route.fulfill({
      contentType: "application/json",
      body: JSON.stringify(body),
    }),
  );
}

async function disableWebGl2(page: Page): Promise<void> {
  await page.addInitScript(() => {
    const getContext = HTMLCanvasElement.prototype.getContext;
    HTMLCanvasElement.prototype.getContext = function (
      contextId: string,
      ...options: unknown[]
    ) {
      if (contextId === "webgl2") return null;
      return Reflect.apply(getContext, this, [contextId, ...options]);
    } as typeof HTMLCanvasElement.prototype.getContext;
  });
}

test("uses identical governed identity for keyboard and MapLibre pointer selection", async ({
  page,
}) => {
  const evidenceRequests: string[] = [];
  const externalRequests: string[] = [];
  page.on("request", (request) => {
    const url = new URL(request.url());
    if (
      (url.protocol === "http:" || url.protocol === "https:") &&
      url.origin !== "http://127.0.0.1:4173"
    ) {
      externalRequests.push(request.url());
    }
  });
  await routeLayers(page);
  await page.route("**/evidence?*", (route) => {
    evidenceRequests.push(route.request().url());
    return route.fulfill({
      contentType: "application/json",
      body: JSON.stringify(governedAnswerResponse),
    });
  });
  await page.goto("/");

  const renderer = page.locator(
    '[data-component="governed-map-renderer-status"]',
  );
  await expect(renderer).toHaveAttribute("data-renderer", "MAPLIBRE");
  await expect(
    page.locator('[data-component="governed-layer-status"]'),
  ).toContainText("ANSWER / SUPPORTED");
  const runtime = page.locator(
    '[data-component="explorer-map-runtime-status-host"]',
  );
  await expect(
    runtime.getByRole("status", { name: "Map runtime status: ready" }),
  ).toContainText("Candidate selectionELIGIBLE");

  const feature = page.getByRole("button", {
    name: "Select Synthetic streamflow demonstration",
  });
  await expect(feature).toBeEnabled();
  await feature.focus();
  await page.keyboard.press("Enter");
  await expect(
    page.locator('[data-component="governed-evidence-status"]'),
  ).toHaveText("ANSWER / SUPPORTED");
  await expect(
    page.getByRole("button", { name: "Close Evidence Drawer" }),
  ).toBeFocused();
  await page.keyboard.press("Escape");
  await expect(feature).toBeFocused();

  const map = page.locator(".governed-map-canvas");
  await map.evaluate(
    () =>
      new Promise<void>((resolve) => {
        requestAnimationFrame(() => requestAnimationFrame(() => resolve()));
      }),
  );
  const bounds = await map.boundingBox();
  expect(bounds).not.toBeNull();
  await map.click({
    position: { x: bounds!.width / 2, y: bounds!.height / 2 },
  });
  await expect.poll(() => evidenceRequests.length).toBe(2);
  await expect(
    page.getByRole("complementary", {
      name: /Evidence Drawer: supported evidence/,
    }),
  ).toContainText("kfm:evidence:synthetic:flow-001");
  const drawer = page.getByRole("complementary", {
    name: /Evidence Drawer: supported evidence/,
  });
  await expect(drawer).toContainText("Synthetic streamflow observation");
  await expect(drawer).toContainText(
    "A synthetic, generalized flow observation is supported by the cited fixture evidence.",
  );
  await expect(
    drawer.getByRole("link", { name: "Synthetic fixture evidence" }),
  ).toHaveAttribute(
    "href",
    "https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/d1f7ed51cf4d9c9c2fdf94cdc81644744ae464ce/fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json",
  );
  await expect(drawer.getByRole("list", { name: "Evidence limitations" })).toContainText(
    "Fixture-only demonstration; not a live observation or life-safety instruction.",
  );
  const trust = drawer.getByRole("list", { name: "Evidence trust state" });
  await expect(trust).toContainText("Source role: official");
  await expect(trust).toContainText("Policy: ALLOW");
  await expect(trust).toContainText("Review: REVIEWED");
  await expect(trust).toContainText("Release: RELEASED");
  await expect(trust).toContainText("Freshness: CURRENT");
  await expect(trust).toContainText("Correction: CORRECTED");
  const history = drawer.getByRole("list", { name: "Evidence history" });
  await expect(history).toContainText(
    "Superseded evidence: kfm:evidence:synthetic:flow-000",
  );
  await expect(history).toContainText(
    "Correction lineage: kfm:evidence:synthetic:flow-000 → kfm:evidence:synthetic:flow-001 (2026-08-01T00:00:00Z)",
  );

  expect(evidenceRequests[0]).toBe(evidenceRequests[1]);
  const requested = new URL(evidenceRequests[0]);
  expect([...requested.searchParams.entries()]).toEqual([
    ["layer_id", "layer:synthetic-streamflow"],
    ["feature_id", "feature:flow-001"],
    ["evidence_ref", "kfm:evidence:synthetic:flow-001"],
  ]);
  expect(externalRequests).toEqual([]);
});

test("renderer initialization failure preserves keyboard evidence through Null fallback", async ({
  page,
}) => {
  await disableWebGl2(page);
  await routeLayers(page);
  await page.route("**/evidence?*", (route) =>
    route.fulfill({
      contentType: "application/json",
      body: JSON.stringify(governedAnswerResponse),
    }),
  );
  await page.goto("/");

  const renderer = page.locator(
    '[data-component="governed-map-renderer-status"]',
  );
  await expect(renderer).toHaveAttribute("data-renderer", "NULL_FALLBACK");
  await expect(renderer).toContainText(
    "fallback keeps the accessible evidence path available",
  );
  const feature = page.getByRole("button", {
    name: "Select Synthetic streamflow demonstration",
  });
  await expect(feature).toBeEnabled();
  await feature.press("Enter");
  await expect(
    page.getByRole("complementary", {
      name: /Evidence Drawer: supported evidence/,
    }),
  ).toBeVisible();
});

test("a never-settling injected runtime is disposed and reaches a usable Null fallback", async ({
  page,
}) => {
  await page.goto(
    "/tests/browser/governed-map-workspace.html?runtime=never-settling",
  );

  const renderer = page.locator(
    '[data-component="governed-map-renderer-status"]',
  );
  await expect(renderer).toHaveAttribute("data-renderer", "NULL_FALLBACK");
  await expect(renderer).toContainText(
    "fallback keeps the accessible evidence path available",
  );
  await expect
    .poll(() =>
      page.evaluate(() =>
        (
          window as Window & {
            __kfmNeverSettlingDisposeCount: () => number;
          }
        ).__kfmNeverSettlingDisposeCount(),
      ),
    )
    .toBe(1);

  const feature = page.getByRole("button", {
    name: "Select Synthetic streamflow demonstration",
  });
  await expect(feature).toBeEnabled();
  await feature.press("Enter");
  await expect(
    page.getByRole("complementary", {
      name: /Evidence Drawer: supported evidence/,
    }),
  ).toBeVisible();
});

test("post-initialization runtime ERROR clears evidence, restores focus, and swaps once", async ({
  page,
}) => {
  await page.goto("/tests/browser/governed-map-workspace.html");
  const feature = page.getByRole("button", {
    name: "Select Synthetic streamflow demonstration",
  });
  await expect(feature).toBeEnabled();
  await feature.click();
  await expect(
    page.getByRole("button", { name: "Close Evidence Drawer" }),
  ).toBeFocused();

  await page.evaluate(() =>
    (
      window as Window & {
        __kfmTriggerPostInitializationError: () => void;
      }
    ).__kfmTriggerPostInitializationError(),
  );

  const renderer = page.locator(
    '[data-component="governed-map-renderer-status"]',
  );
  await expect(renderer).toHaveAttribute("data-renderer", "NULL_FALLBACK");
  await expect(feature).toBeEnabled();
  const status = page.locator('[data-component="governed-evidence-status"]');
  await expect(status).toHaveAttribute("role", "alert");
  await expect(status).toHaveText("ERROR / RENDERER_FAILED");
  await expect(status).toBeFocused();
  await expect(
    page.locator('[data-component="evidence-drawer"]'),
  ).toHaveCount(0);

  await feature.click();
  await expect(status).toHaveText("ANSWER / SUPPORTED");
  await page.evaluate(() =>
    (
      window as Window & { __kfmDestroyGovernedWorkspace: () => void }
    ).__kfmDestroyGovernedWorkspace(),
  );
  expect(
    await page.evaluate(() =>
      (
        window as Window & {
          __kfmGovernedTransportCloseCount: () => number;
        }
      ).__kfmGovernedTransportCloseCount(),
    ),
  ).toBe(1);
});

test("repeated workspace mount and teardown leaves no stale drawer or selection DOM", async ({
  page,
}) => {
  await page.goto("/tests/browser/governed-map-workspace.html");
  const featureName = "Select Synthetic streamflow demonstration";
  await expect(page.getByRole("button", { name: featureName })).toBeEnabled();
  await page.getByRole("button", { name: featureName }).click();
  await expect(page.locator('[data-component="evidence-drawer"]')).toHaveCount(1);

  await page.evaluate(() =>
    (
      window as Window & { __kfmDestroyGovernedWorkspace: () => void }
    ).__kfmDestroyGovernedWorkspace(),
  );
  await expect(page.locator(".governed-map-workspace")).toHaveCount(0);
  await expect(page.locator('[data-component="evidence-drawer"]')).toHaveCount(0);

  await page.evaluate(() =>
    (
      window as Window & { __kfmRemountGovernedWorkspace: () => void }
    ).__kfmRemountGovernedWorkspace(),
  );
  await expect(page.locator(".governed-map-workspace")).toHaveCount(1);
  await expect(page.getByRole("button", { name: featureName })).toHaveCount(1);
  await expect(page.getByRole("button", { name: featureName })).toBeEnabled();
  await expect(
    page.locator('[data-component="governed-evidence-status"]'),
  ).toHaveText("ABSTAIN / SELECTION_REQUIRED");
  await expect(page.locator('[data-component="evidence-drawer"]')).toHaveCount(0);

  await page.getByRole("button", { name: featureName }).click();
  await expect(page.locator('[data-component="evidence-drawer"]')).toHaveCount(1);
  await page.evaluate(() =>
    (
      window as Window & { __kfmDestroyGovernedWorkspace: () => void }
    ).__kfmDestroyGovernedWorkspace(),
  );
  expect(
    await page.evaluate(() =>
      (
        window as Window & {
          __kfmGovernedTransportCloseCount: () => number;
        }
      ).__kfmGovernedTransportCloseCount(),
    ),
  ).toBe(2);
});

test("a throwing transport close cannot interrupt runtime and DOM teardown", async ({
  page,
}) => {
  await page.goto("/tests/browser/governed-map-workspace.html");
  const feature = page.getByRole("button", {
    name: "Select Synthetic streamflow demonstration",
  });
  await expect(feature).toBeEnabled();
  await feature.click();
  await expect(page.locator('[data-component="evidence-drawer"]')).toHaveCount(1);

  await page.evaluate(() => {
    const fixtureWindow = window as Window & {
      __kfmDestroyGovernedWorkspace: () => void;
      __kfmSetGovernedTransportCloseFailure: () => void;
    };
    fixtureWindow.__kfmSetGovernedTransportCloseFailure();
    fixtureWindow.__kfmDestroyGovernedWorkspace();
  });

  await expect(page.locator(".governed-map-workspace")).toHaveCount(0);
  await expect(page.locator('[data-component="evidence-drawer"]')).toHaveCount(0);
  expect(
    await page.evaluate(() =>
      (
        window as Window & {
          __kfmGovernedTransportCloseCount: () => number;
        }
      ).__kfmGovernedTransportCloseCount(),
    ),
  ).toBe(1);
});

test("finite governed denial and error states have semantic status and fixed no-leak copy", async ({
  page,
}) => {
  await disableWebGl2(page);
  let response: unknown = governedDenyResponse;
  await routeLayers(page);
  await page.route("**/evidence?*", (route) =>
    route.fulfill({
      status: response === governedErrorResponse ? 500 : 200,
      contentType: "application/json",
      body: JSON.stringify(response),
    }),
  );
  await page.goto("/");
  const feature = page.getByRole("button", {
    name: "Select Synthetic streamflow demonstration",
  });
  await expect(feature).toBeEnabled();

  await feature.click();
  const evidenceStatus = page.locator(
    '[data-component="governed-evidence-status"]',
  );
  await expect(evidenceStatus).toHaveAttribute("role", "alert");
  await expect(evidenceStatus).toHaveAttribute("aria-live", "assertive");
  await expect(evidenceStatus).toHaveAttribute("data-outcome", "DENY");
  await expect(evidenceStatus).toHaveText(
    "DENY / SENSITIVE_DETAIL_RESTRICTED",
  );
  await expect(page.locator("body")).not.toContainText("PRIVATE_DENIAL_CANARY");

  response = governedErrorResponse;
  await feature.click();
  await expect(evidenceStatus).toHaveAttribute("role", "alert");
  await expect(evidenceStatus).toHaveAttribute("aria-live", "assertive");
  await expect(evidenceStatus).toHaveText("ERROR / UPSTREAM_ERROR");
  await expect(page.locator("body")).not.toContainText("PRIVATE_ERROR_CANARY");
});

test("canonical site rejects evidence outside the selected governed subset", async ({
  page,
}) => {
  await disableWebGl2(page);
  await routeLayers(page);
  await page.route("**/evidence?*", (route) =>
    route.fulfill({
      contentType: "application/json",
      body: JSON.stringify({
        ...governedAnswerResponse,
        evidence_refs: ["kfm:evidence:synthetic:outside-selection"],
        trust_state: {
          ...governedAnswerResponse.trust_state,
          correction: "NONE",
        },
        history: { negative_outcomes: [], corrections: [] },
      }),
    }),
  );
  await page.goto("/");
  const feature = page.getByRole("button", {
    name: "Select Synthetic streamflow demonstration",
  });
  await expect(feature).toBeEnabled();
  await feature.click();

  const status = page.locator('[data-component="governed-evidence-status"]');
  await expect(status).toHaveAttribute("role", "alert");
  await expect(status).toHaveText(
    "ERROR / DRAWER_EVIDENCE_OUTSIDE_SELECTION",
  );
  const drawer = page.getByRole("complementary", {
    name: "Evidence Drawer: error",
  });
  await expect(drawer).toContainText("ERROR / UPSTREAM_ERROR");
  await expect(drawer).not.toContainText(
    "kfm:evidence:synthetic:outside-selection",
  );
});

test("newer feature selection suppresses a slower prior response", async ({
  page,
}) => {
  await disableWebGl2(page);
  let evidenceCalls = 0;
  await routeLayers(page);
  await page.route("**/evidence?*", async (route) => {
    evidenceCalls += 1;
    const call = evidenceCalls;
    if (call === 1) await new Promise((resolve) => setTimeout(resolve, 250));
    await route.fulfill({
      contentType: "application/json",
      body: JSON.stringify(
        call === 1 ? governedAnswerResponse : governedDenyResponse,
      ),
    });
  });
  await page.goto("/");
  const feature = page.getByRole("button", {
    name: "Select Synthetic streamflow demonstration",
  });
  await expect(feature).toBeEnabled();

  await feature.click();
  await expect.poll(() => evidenceCalls).toBe(1);
  await feature.click();
  const status = page.locator('[data-component="governed-evidence-status"]');
  await expect(status).toHaveText("DENY / SENSITIVE_DETAIL_RESTRICTED");
  await page.waitForTimeout(300);
  await expect(status).toHaveText("DENY / SENSITIVE_DETAIL_RESTRICTED");
});

test("malformed layer transport result is an assertive finite error", async ({
  page,
}) => {
  await routeLayers(page, {
    ...governedLayerResponse,
    private_field: "PRIVATE_LAYER_CANARY",
  });
  await page.goto("/");

  const status = page.locator('[data-component="governed-layer-status"]');
  await expect(status).toHaveAttribute("role", "alert");
  await expect(status).toHaveAttribute("aria-live", "assertive");
  await expect(status).toHaveText("ERROR / INVALID_GOVERNED_LAYER_PAYLOAD");
  await expect(page.locator("body")).not.toContainText("PRIVATE_LAYER_CANARY");
  await expect(
    page.getByRole("button", {
      name: "Select Synthetic streamflow demonstration",
    }),
  ).toHaveCount(0);
});
