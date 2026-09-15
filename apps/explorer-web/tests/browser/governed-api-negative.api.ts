import { expect, test } from "playwright/test";

const fixture = "/tests/browser/map-evidence-drawer.html?runtime=atlas&api=1";
const regionSelector = '[data-component="synthetic-atlas-map"]';
const evidenceRef = "evidence:synthetic:promotion-proof:v1";

test.beforeEach(async ({ context, baseURL }) => {
  const origin = new URL(baseURL!).origin;
  const external: string[] = [];
  await context.route("**/*", async (route) => {
    if (new URL(route.request().url()).origin === origin) return route.continue();
    external.push(route.request().url());
    await route.abort("blockedbyclient");
  });
  context.on("close", () => expect(external).toEqual([]));
});

test("actual WSGI abstention replaces fixture evidence without replacing the canvas", async ({ page }, testInfo) => {
  await page.goto(fixture);
  const region = page.locator(regionSelector);
  await expect(region).toHaveAttribute("data-runtime-state", "READY");
  const canvas = region.locator("canvas.maplibregl-canvas");
  const original = await canvas.elementHandle();
  const camera = await region.getAttribute("data-camera");
  await canvas.click({ position: { x: 360, y: 210 } });
  await expect(page.getByRole("status")).toHaveText("ANSWER / SUPPORTED");
  await expect(page.getByRole("complementary")).toContainText(evidenceRef);

  await page.getByLabel("Synthetic evidence state").selectOption("api-unavailable");
  await expect(page.getByRole("complementary")).toHaveCount(0);
  const received = page.waitForResponse((response) => new URL(response.url()).pathname === "/evidence");
  await canvas.click({ position: { x: 360, y: 210 } });
  const response = await received;
  expect(response.request().method()).toBe("GET");
  expect(new URL(response.url()).search).toBe("");
  expect(response.status()).toBe(200);
  expect(await response.json()).toMatchObject({ id: "stub:evidence", outcome: "ABSTAIN", reason_code: "NOT_IMPLEMENTED", evidence_refs: [] });
  await expect(page.getByRole("status")).toHaveText("ABSTAIN / MISSING_EVIDENCE");
  const drawer = page.getByRole("complementary");
  // The existing Drawer deliberately replaces negative summaries with its
  // fixed safe copy. The fixture-owned availability notice retains the limit.
  await expect(drawer).toContainText("Required evidence is not available.");
  await expect(region.locator('[data-component="atlas-fixture-notice"]')).toContainText("does not yet resolve selected evidence");
  await expect(drawer).not.toContainText(evidenceRef);
  await expect(drawer).not.toContainText("digest-verified synthetic Atlas carrier");
  await expect(drawer.getByRole("link")).toHaveCount(0);
  expect(await region.getAttribute("data-camera")).toBe(camera);
  expect(await canvas.evaluate((node, originalNode) => node === originalNode, original)).toBe(true);
  await expect(region).toHaveAttribute("data-runtime-state", "READY");
  await page.screenshot({ path: testInfo.outputPath("actual-api-abstention.png"), fullPage: true });
  await testInfo.attach("actual-api-abstention", { path: testInfo.outputPath("actual-api-abstention.png"), contentType: "image/png" });
});

test("actual WSGI method rejection becomes a safe Drawer error", async ({ page }) => {
  // Test-only failure injection changes the forwarded method, not response bytes.
  // The client still emits its fixed GET and the unmodified WSGI app emits 405.
  await page.route("**/evidence", async (route) => {
    expect(route.request().method()).toBe("GET");
    const response = await route.fetch({ method: "POST" });
    expect(response.status()).toBe(405);
    expect(await response.json()).toMatchObject({ outcome: "ERROR", evidence_refs: [] });
    await route.fulfill({ response });
  });
  await page.goto(fixture);
  await expect(page.locator(regionSelector)).toHaveAttribute("data-runtime-state", "READY");
  await page.getByLabel("Synthetic evidence state").selectOption("api-unavailable");
  await page.getByRole("button", { name: "Inspect synthetic Kansas test extent without the map" }).click();
  await expect(page.getByRole("status")).toHaveText("ERROR / UPSTREAM_ERROR");
  const drawer = page.getByRole("complementary");
  await expect(drawer).not.toContainText(evidenceRef);
  await expect(drawer).not.toContainText("stub:error:");
  await expect(drawer.getByRole("link")).toHaveCount(0);
});

for (const action of ["change scenario", "dispose"] as const) {
  test(`late actual API response cannot reopen evidence after ${action}`, async ({ page }) => {
    let release!: () => void;
    let observed!: () => void;
    let finished!: () => void;
    const held = new Promise<void>((resolve) => { release = resolve; });
    const responseObserved = new Promise<void>((resolve) => { observed = resolve; });
    const handlerFinished = new Promise<void>((resolve) => { finished = resolve; });
    await page.route("**/evidence", async (route) => {
      const response = await route.fetch();
      expect(response.status()).toBe(200);
      observed();
      await held;
      try { await route.fulfill({ response }); } catch { /* Caller cancellation is expected. */ }
      finally { finished(); }
    });
    await page.goto(fixture);
    const region = page.locator(regionSelector);
    await expect(region).toHaveAttribute("data-runtime-state", "READY");
    await page.getByLabel("Synthetic evidence state").selectOption("api-unavailable");
    await page.getByRole("button", { name: "Inspect synthetic Kansas test extent without the map" }).click();
    await responseObserved;
    await expect(page.getByRole("status")).toHaveText("ABSTAIN / API_AVAILABILITY_PENDING");
    if (action === "change scenario") {
      await page.getByLabel("Synthetic evidence state").selectOption("available");
      await page.getByRole("button", { name: "Inspect synthetic Kansas test extent without the map" }).click();
      await expect(page.getByRole("status")).toHaveText("ANSWER / SUPPORTED");
    } else {
      await page.getByRole("button", { name: "Dispose synthetic map" }).click();
      await expect(region).toHaveAttribute("data-runtime-state", "DISPOSED");
    }
    const deliveries = await region.getAttribute("data-delivery-count");
    release();
    await handlerFinished;
    await page.evaluate(() => new Promise<void>((resolve) => requestAnimationFrame(() => requestAnimationFrame(() => resolve()))));
    expect(await region.getAttribute("data-delivery-count")).toBe(deliveries);
    if (action === "change scenario") {
      await expect(page.getByRole("status")).toHaveText("ANSWER / SUPPORTED");
      await expect(page.getByRole("complementary")).toContainText(evidenceRef);
    } else {
      await expect(page.getByRole("status")).toHaveText("ABSTAIN / MAP_RUNTIME_DISPOSED");
      await expect(page.getByRole("complementary")).toHaveCount(0);
      await expect(region.locator("canvas")).toHaveCount(0);
    }
  });
}
