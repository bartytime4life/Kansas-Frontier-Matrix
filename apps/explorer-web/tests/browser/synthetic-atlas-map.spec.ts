import { expect, test } from "playwright/test";

const fixture = "/tests/browser/map-evidence-drawer.html?runtime=atlas";
const regionSelector = '[data-component="synthetic-atlas-map"]';
const evidenceRef = "evidence:synthetic:promotion-proof:v1";

test.beforeEach(async ({ context, baseURL }) => {
  const origin = new URL(baseURL!).origin;
  const externalRequests: string[] = [];
  // Abort, rather than merely observe, every non-local browser HTTP request.
  // Same-origin Vite modules and the package-owned worker remain available.
  await context.route("**/*", async (route) => {
    const url = new URL(route.request().url());
    if (url.origin === origin) return route.continue();
    externalRequests.push(url.href);
    await route.abort("blockedbyclient");
  });
  context.on("close", () => expect(externalRequests).toEqual([]));
});

test("real Kansas canvas selection resolves its pinned evidence and preserves map and camera", async ({ page, baseURL }, testInfo) => {
  const workerUrls: string[] = [];
  page.on("worker", (worker) => workerUrls.push(worker.url()));
  await page.goto(fixture);
  const region = page.locator(regionSelector);
  await expect(region).toHaveAttribute("data-runtime-state", "READY");
  const canvas = region.locator("canvas.maplibregl-canvas");
  const originalCanvas = await canvas.elementHandle();
  expect(originalCanvas).not.toBeNull();
  await expect(canvas).toHaveCount(1);
  await expect(region.locator('[data-component="atlas-legend"]')).toContainText("longitude/latitude degrees");
  await expect(region.locator('[data-component="atlas-legend"]')).toContainText("2026-04-13T00:00:00Z");

  // Background has no approved feature binding and cannot manufacture evidence.
  await canvas.click({ position: { x: 12, y: 12 } });
  await expect(region).toHaveAttribute("data-selection-count", "0");
  await expect(page.getByRole("complementary")).toHaveCount(0);

  const initialCamera = await region.getAttribute("data-camera");
  const box = await canvas.boundingBox();
  expect(box).not.toBeNull();
  await page.mouse.move(box!.x + 360, box!.y + 210);
  await page.mouse.down();
  await page.mouse.move(box!.x + 395, box!.y + 210, { steps: 8 });
  await page.mouse.up();
  await expect.poll(() => region.getAttribute("data-camera")).not.toBe(initialCamera);
  // Await camera settlement before testing that selection does not reset it.
  await page.waitForTimeout(350);
  const pannedCamera = await region.getAttribute("data-camera");
  await canvas.click({ position: { x: 360, y: 210 } });
  await expect(page.getByRole("status")).toHaveText("ANSWER / SUPPORTED");
  const drawer = page.getByRole("complementary");
  await expect(drawer).toContainText(evidenceRef);
  await expect(drawer).toContainText("digest-verified synthetic Atlas carrier");
  await expect(drawer).toContainText("test inputs, not actual review");
  await expect(drawer.getByRole("link", { name: "Pinned synthetic carrier source" })).toBeVisible();
  await expect(region).toHaveAttribute("data-selection-count", "1");
  expect(await region.getAttribute("data-camera")).toBe(pannedCamera);
  expect(await canvas.evaluate((node, original) => node === original, originalCanvas)).toBe(true);
  await page.screenshot({ path: testInfo.outputPath("synthetic-kansas-map-evidence.png"), fullPage: true });
  await testInfo.attach("synthetic-kansas-map-evidence", { path: testInfo.outputPath("synthetic-kansas-map-evidence.png"), contentType: "image/png" });
  await page.getByRole("button", { name: "Close Evidence Drawer" }).click();
  await canvas.click({ position: { x: 360, y: 210 } });
  await expect(region).toHaveAttribute("data-selection-count", "2");
  await expect(page.getByRole("status")).toHaveText("ANSWER / SUPPORTED");
  expect(await region.getAttribute("data-camera")).toBe(pannedCamera);
  expect(await canvas.evaluate((node, original) => node === original, originalCanvas)).toBe(true);
  expect(workerUrls.length).toBeGreaterThan(0);
  expect(workerUrls.every((url) => new URL(url).origin === new URL(baseURL!).origin)).toBe(true);
});

test("real canvas selections produce finite negative outcomes without remounting or leaking claims", async ({ page }) => {
  await page.goto(fixture);
  const region = page.locator(regionSelector);
  await expect(region).toHaveAttribute("data-runtime-state", "READY");
  const canvas = region.locator("canvas.maplibregl-canvas");
  const originalCanvas = await canvas.elementHandle();
  const camera = await region.getAttribute("data-camera");
  const cases = [
    ["available", "ANSWER / SUPPORTED"],
    ["no-results", "ABSTAIN / MISSING_EVIDENCE"],
    ["stale", "ABSTAIN / STALE_EVIDENCE"],
    ["deny", "DENY / POLICY_DENIED"],
    ["error", "ERROR / GOVERNED_RESOLVER_ERROR"],
    ["available", "ANSWER / SUPPORTED"],
  ] as const;
  let count = 0;
  for (const [scenario, outcome] of cases) {
    await page.getByLabel("Synthetic evidence state").selectOption(scenario);
    await expect(page.getByRole("complementary")).toHaveCount(0);
    await canvas.click({ position: { x: 360, y: 210 } });
    await expect(page.getByRole("status")).toHaveText(outcome);
    await expect(region).toHaveAttribute("data-selection-count", String(++count));
    const drawer = page.getByRole("complementary");
    if (scenario !== "available") {
      await expect(drawer.getByRole("link")).toHaveCount(0);
      await expect(drawer).not.toContainText(evidenceRef);
      await expect(drawer).not.toContainText("digest-verified synthetic Atlas carrier");
    }
    await expect(drawer).not.toContainText("SYNTHETIC_ATLAS_RESOLVER_CANARY");
    await expect(region).toHaveAttribute("data-runtime-state", "READY");
    expect(await region.getAttribute("data-camera")).toBe(camera);
    expect(await canvas.evaluate((node, original) => node === original, originalCanvas)).toBe(true);
  }
});

test("disposing the real fixture removes canvas, drawer and selection delivery", async ({ page }) => {
  await page.goto(fixture);
  const region = page.locator(regionSelector);
  await expect(region).toHaveAttribute("data-runtime-state", "READY");
  const canvas = region.locator("canvas.maplibregl-canvas");
  const originalCanvas = await canvas.elementHandle();
  await canvas.click({ position: { x: 360, y: 210 } });
  await expect(page.getByRole("status")).toHaveText("ANSWER / SUPPORTED");
  const deliveries = await region.getAttribute("data-delivery-count");
  const selections = await region.getAttribute("data-selection-count");
  await page.getByRole("button", { name: "Dispose synthetic map" }).click();
  await expect(region).toHaveAttribute("data-runtime-state", "DISPOSED");
  await expect(canvas).toHaveCount(0);
  await expect(page.getByRole("complementary")).toHaveCount(0);
  await expect(page.getByRole("status")).toHaveText("ABSTAIN / MAP_RUNTIME_DISPOSED");
  await expect(page.getByLabel("Synthetic evidence state")).toBeDisabled();
  expect(await originalCanvas!.evaluate((node) => node.isConnected)).toBe(false);
  // A retained detached DOM target cannot deliver another runtime selection.
  await originalCanvas!.evaluate((node) => node.dispatchEvent(new MouseEvent("click", { bubbles: true, clientX: 360, clientY: 210 })));
  expect(await region.getAttribute("data-selection-count")).toBe(selections);
  expect(await region.getAttribute("data-delivery-count")).toBe(deliveries);
});

test("keyboard text selection preserves canvas evidence parity with reduced motion and doubled text", async ({ page }) => {
  await page.emulateMedia({ reducedMotion: "reduce" });
  await page.goto(fixture);
  const region = page.locator(regionSelector);
  await expect(region).toHaveAttribute("data-runtime-state", "READY");
  const canvas = region.locator("canvas.maplibregl-canvas");
  const originalCanvas = await canvas.elementHandle();
  await canvas.click({ position: { x: 360, y: 210 } });
  await expect(page.getByRole("status")).toHaveText("ANSWER / SUPPORTED");
  const canvasEvidence = await page.getByRole("complementary").innerText();
  await page.getByRole("button", { name: "Close Evidence Drawer" }).click();
  await page.addStyleTag({ content: "html { font-size: 200%; } [data-component='synthetic-atlas-map'] { overflow-wrap: anywhere; } [data-component='synthetic-atlas-map'] :is(button, select) { font: inherit; }" });
  const selector = page.getByRole("button", { name: "Inspect synthetic Kansas test extent without the map" });
  await selector.focus();
  await expect(selector).toBeFocused();
  await page.keyboard.press("Enter");
  await expect(page.getByRole("status")).toHaveText("ANSWER / SUPPORTED");
  await expect(region).toHaveAttribute("data-selection-count", "1");
  await expect(region).toHaveAttribute("data-text-selection-count", "1");
  const drawer = page.getByRole("complementary");
  expect(await drawer.innerText()).toBe(canvasEvidence);
  await expect(page.getByRole("button", { name: "Close Evidence Drawer" })).toBeFocused();
  expect(await page.evaluate(() => matchMedia("(prefers-reduced-motion: reduce)").matches)).toBe(true);
  expect(await page.evaluate(() => getComputedStyle(document.documentElement).fontSize)).toBe("32px");
  expect(await canvas.evaluate((node, original) => node === original, originalCanvas)).toBe(true);
  await expect(canvas).toHaveCount(1);
  await page.keyboard.press("Escape");
  await expect(drawer).toBeHidden();
  await expect(selector).toBeFocused();
});
