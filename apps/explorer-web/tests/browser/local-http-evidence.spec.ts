import { expect, test, type Page } from "playwright/test";

const endpoint = "/__local__/evidence";
const workspace = (page: Page) => page.locator('[data-component="living-atlas-workspace"]');
const drawer = (page: Page) => workspace(page).locator('[data-component="evidence-drawer"]');
const inspect = (page: Page, name = "Generalized Kansas extent") =>
  workspace(page).locator(".atlas-layer-row", { hasText: name }).getByRole("button", { name: "Inspect", exact: true });

async function openLayers(page: Page): Promise<void> {
  await page.goto("/");
  await expect(workspace(page).getByRole("status").filter({ hasText: "Renderer READY" })).toBeVisible();
  const stage = await workspace(page).locator(".atlas-map-stage").boundingBox();
  const host = await workspace(page).locator("#kfm-living-atlas-map").boundingBox();
  const canvas = await workspace(page).locator("#kfm-living-atlas-map canvas").boundingBox();
  expect(host!.height).toBeGreaterThan(250);
  expect(host).toEqual(stage);
  expect(canvas!.width).toBeCloseTo(stage!.width, 0);
  expect(canvas!.height).toBeCloseTo(stage!.height, 0);
  await workspace(page).getByRole("button", { name: "Layers", exact: true }).click();
  await expect(workspace(page).getByRole("region", { name: "Local evidence service demonstration" })).toBeVisible();
}

test("requests actual local HTTP evidence and opens an accessible drawer with a pinned citation", async ({ page }, testInfo) => {
  await openLayers(page);
  const request = page.waitForRequest((entry) => new URL(entry.url()).pathname === endpoint);
  const response = page.waitForResponse((entry) => new URL(entry.url()).pathname === endpoint);
  await inspect(page).focus();
  await page.keyboard.press("Enter");
  const sent = await request;
  const received = await response;
  expect(sent.method()).toBe("POST");
  expect(sent.postDataJSON()).toEqual({
    profile: "kfm.explorer.map-feature-selection.v1",
    selection_id: "selection:local-http:kansas-frame:current",
    layer_id: "layer:kansas-frame",
    feature_id: "feature:local-http:kansas-frame",
    evidence_refs: ["kfm:evidence:site-local:kansas-frame"],
  });
  expect(received.status()).toBe(200);
  expect(received.headers()["x-kfm-local-fixture"]).toBe("synthetic-only");
  await expect(drawer(page)).toContainText("ANSWER / SUPPORTED");
  await expect(drawer(page)).toContainText("synthetic");
  const citation = drawer(page).getByRole("link", { name: "Repository synthetic layer declaration" });
  await expect(citation).toHaveAttribute("href", /github\.com\/bartytime4life\/Kansas-Frontier-Matrix\/blob\/[a-f0-9]{40}\/apps\/explorer-web\/src\/features\/living_atlas\/registry\.ts/);
  const heading = drawer(page).getByRole("heading", { level: 2 });
  await expect(heading).toBeFocused();
  await expect(heading).toHaveAttribute("tabindex", "-1");
  await expect(heading).toHaveCSS("outline-width", "3px");
  const rail = workspace(page).locator(".atlas-evidence-drawer");
  expect(await rail.evaluate((node) => node.scrollTop)).toBe(0);
  const initialContentVisible = await rail.evaluate((node) => {
    const railBounds = node.getBoundingClientRect();
    const disclosure = node.querySelector("p")!.getBoundingClientRect();
    const outcome = node.querySelector("[data-evidence-outcome]")!.getBoundingClientRect();
    return disclosure.top >= railBounds.top && outcome.bottom <= railBounds.bottom;
  });
  expect(initialContentVisible).toBe(true);
  await page.keyboard.press("Escape");
  await expect(drawer(page)).toBeHidden();
  await expect(inspect(page)).toBeFocused();
  await workspace(page).getByRole("button", { name: "Open Evidence Drawer", exact: true }).click();
  await expect(citation).toBeVisible();
  await expect(heading).toBeFocused();
  expect(await rail.evaluate((node) => node.scrollTop)).toBe(0);
  await testInfo.attach("Local evidence desktop", { body: await workspace(page).screenshot(), contentType: "image/png" });
});

test("transports finite stale, withdrawal, missing, denied and upstream error states without positive fallback", async ({ page }) => {
  await openLayers(page);
  await inspect(page).click();
  await expect(drawer(page)).toContainText("ANSWER / SUPPORTED");
  for (const [scenario, code, status] of [
    ["stale", "ABSTAIN / STALE_EVIDENCE", 200],
    ["withdrawn", "ABSTAIN / WITHDRAWN_EVIDENCE", 200],
    ["missing", "ABSTAIN / MISSING_EVIDENCE", 200],
    ["denied", "DENY / POLICY_DENIED", 200],
    ["error", "ERROR / UPSTREAM_ERROR", 503],
  ] as const) {
    const received = page.waitForResponse((entry) => new URL(entry.url()).pathname === endpoint);
    await workspace(page).getByLabel("Synthetic service scenario", { exact: true }).selectOption(scenario);
    expect((await received).status()).toBe(status);
    await expect(drawer(page)).toContainText(code);
    await expect(drawer(page).getByRole("link")).toHaveCount(0);
    await expect(drawer(page)).not.toContainText("ANSWER / SUPPORTED");
    if (scenario === "withdrawn") {
      await expect(drawer(page).getByRole("list", { name: "Evidence history" })).toContainText("Withdrawn evidence");
    }
  }
});

test("clears selected evidence on committed time and does not persist negative support in report drafts", async ({ page }) => {
  await openLayers(page);
  await inspect(page, "County locator starter points").click();
  await expect(drawer(page)).toContainText("ANSWER / SUPPORTED");
  await workspace(page).getByRole("slider", { name: "Preview atlas time" }).fill("10");
  await workspace(page).getByRole("button", { name: "Apply time", exact: true }).click();
  await expect(drawer(page)).toHaveCount(0);
  await expect(workspace(page).getByRole("heading", { name: "Inspect before interpretation" })).toBeVisible();
  await inspect(page).click();
  await expect(drawer(page)).toContainText("ANSWER / SUPPORTED");
  await workspace(page).getByLabel("Synthetic service scenario", { exact: true }).selectOption("withdrawn");
  await expect(drawer(page)).toContainText("WITHDRAWN_EVIDENCE");
  await workspace(page).getByRole("button", { name: "New from map", exact: true }).click();
  await workspace(page).getByRole("button", { name: "Create report draft", exact: true }).click();
  const draft = await page.evaluate(() => JSON.parse(localStorage.getItem("kfm.explorer.report-drafts.v2") ?? "[]").at(-1));
  expect(draft.includedEvidenceRefs).toEqual([]);
  expect(draft.snapshot.evidenceRefs).toEqual([]);
});

test("keyboard retry preserves safe workspace state and recovers visible focus after failure and recovery", async ({ page, context }) => {
  await openLayers(page);
  await workspace(page).getByRole("slider", { name: "Preview atlas time" }).fill("10");
  await workspace(page).getByRole("button", { name: "Apply time", exact: true }).click();
  await inspect(page).click();
  await expect(drawer(page)).toContainText("ANSWER / SUPPORTED");
  const readWorkspaceState = () => workspace(page).evaluate((node) => ({
    time: node.querySelector<HTMLInputElement>('[aria-label="Preview atlas time"]')!.value,
    selectedControls: Array.from(node.querySelectorAll('[aria-pressed="true"][data-atlas-action]'))
      .map((control) => control.getAttribute("data-atlas-action")),
    layers: Array.from(node.querySelectorAll<HTMLInputElement>("[data-layer-toggle]"))
      .map((control) => ({ id: control.dataset.layerToggle, checked: control.checked, disabled: control.disabled })),
  }));
  const before = await readWorkspaceState();
  const retry = workspace(page).getByRole("button", { name: "Retry local evidence" });
  const trigger = workspace(page).getByRole("button", { name: "Open Evidence Drawer", exact: true });
  const closeAndReopen = async () => {
    await expect(drawer(page).getByRole("heading", { level: 2 })).toBeFocused();
    await page.keyboard.press("Escape");
    await expect(drawer(page)).toBeHidden();
    await expect(trigger).toBeVisible();
    await expect(trigger).toBeFocused();
    await page.keyboard.press("Enter");
    await expect(drawer(page).getByRole("heading", { level: 2 })).toBeFocused();
  };
  await context.setOffline(true);
  await retry.focus();
  await page.keyboard.press("Enter");
  await expect(drawer(page)).toContainText("ERROR / UPSTREAM_ERROR");
  await expect(drawer(page).getByRole("link")).toHaveCount(0);
  expect(await readWorkspaceState()).toEqual(before);
  await closeAndReopen();
  await context.setOffline(false);
  const response = page.waitForResponse((entry) => new URL(entry.url()).pathname === endpoint);
  await retry.focus();
  await page.keyboard.press("Enter");
  expect((await response).status()).toBe(200);
  await expect(drawer(page)).toContainText("ANSWER / SUPPORTED");
  expect(await readWorkspaceState()).toEqual(before);
  await closeAndReopen();
  await workspace(page).getByRole("button", { name: "New from map", exact: true }).click();
  await workspace(page).getByRole("button", { name: "Create report draft", exact: true }).click();
  const draft = await page.evaluate(() => JSON.parse(localStorage.getItem("kfm.explorer.report-drafts.v2") ?? "[]")[0]);
  expect(draft.snapshot).toMatchObject({
    committedTimeId: "time:1900s",
    selectedLayerId: "layer:kansas-frame",
    activeViewId: before.selectedControls.find((action) => action?.startsWith("view:"))!.slice("view:".length),
    representation: "2D",
    basemap: "SITE_LOCAL_ATLAS",
    publicSafe: true,
    draftOnly: true,
    evidenceRefs: ["kfm:evidence:site-local:kansas-frame"],
  });
  expect(draft.snapshot.layers.map((layer: { id: string; visible: boolean }) => ({ id: layer.id, visible: layer.visible })))
    .toEqual(before.layers.map((layer) => ({ id: layer.id, visible: layer.checked })));
  expect(draft.includedEvidenceRefs).toEqual(draft.snapshot.evidenceRefs);
});

test("scenario replacement returns to the retained selector and avoids hidden return targets", async ({ page }) => {
  await openLayers(page);
  await inspect(page).click();
  await expect(drawer(page)).toContainText("ANSWER / SUPPORTED");
  const scenario = workspace(page).getByLabel("Synthetic service scenario", { exact: true });
  await scenario.focus();
  await scenario.selectOption("stale");
  await expect(drawer(page)).toContainText("ABSTAIN / STALE_EVIDENCE");
  await expect(drawer(page).getByRole("heading", { level: 2 })).toBeFocused();
  await page.keyboard.press("Escape");
  await expect(scenario).toBeFocused();
  await scenario.selectOption("current");
  await expect(drawer(page)).toContainText("ANSWER / SUPPORTED");
  // Moving to another rail hides the original selector while the drawer stays open.
  await workspace(page).getByRole("button", { name: "Sources", exact: true }).click();
  await expect(scenario).toBeHidden();
  await drawer(page).getByRole("heading", { level: 2 }).focus();
  await page.keyboard.press("Escape");
  await expect(drawer(page)).toBeHidden();
  const trigger = workspace(page).getByRole("button", { name: "Open Evidence Drawer", exact: true });
  await expect(trigger).toBeVisible();
  await expect(trigger).toBeFocused();
});

test("a completed retry does not take focus after the user moves elsewhere", async ({ page }) => {
  await openLayers(page);
  await inspect(page).click();
  await expect(drawer(page)).toContainText("ANSWER / SUPPORTED");
  let releaseResponse!: () => void;
  const responseGate = new Promise<void>((resolve) => { releaseResponse = resolve; });
  let backendResponded!: () => void;
  const backendReady = new Promise<void>((resolve) => { backendResponded = resolve; });
  await page.route("**/__local__/evidence", async (route) => {
    const response = await route.fetch();
    expect(response.status()).toBe(200);
    backendResponded();
    await responseGate;
    await route.fulfill({ response });
  }, { times: 1 });
  await workspace(page).getByRole("button", { name: "Retry local evidence" }).focus();
  await page.keyboard.press("Enter");
  await backendReady;
  const sources = workspace(page).getByRole("button", { name: "Sources", exact: true });
  await sources.click();
  releaseResponse();
  const trigger = workspace(page).getByRole("button", { name: "Open Evidence Drawer", exact: true });
  await expect(trigger).toBeVisible();
  await expect(drawer(page)).toBeHidden();
  await expect(sources).toBeFocused();
  await trigger.focus();
  await page.keyboard.press("Enter");
  await expect(drawer(page)).toContainText("ANSWER / SUPPORTED");
  await expect(drawer(page).getByRole("heading", { level: 2 })).toBeFocused();
  await page.keyboard.press("Escape");
  await expect(trigger).toBeFocused();
});

test("keeps unsupported and protected selections local and non-claim-bearing", async ({ page }) => {
  await openLayers(page);
  const requests: string[] = [];
  page.on("request", (request) => {
    if (new URL(request.url()).pathname === endpoint) requests.push(request.url());
  });
  await inspect(page, "Generalized river context").click();
  await expect(drawer(page)).toContainText("ABSTAIN / MISSING_EVIDENCE");
  await inspect(page, "Protected-context envelope").click();
  await expect(drawer(page)).toContainText("DENY / POLICY_DENIED");
  await expect(drawer(page).getByRole("link")).toHaveCount(0);
  expect(requests).toEqual([]);
});

test("clears service proof when a view or connection replaces the selection", async ({ page }) => {
  await openLayers(page);
  await inspect(page).click();
  await expect(drawer(page)).toContainText("ANSWER / SUPPORTED");
  await workspace(page).getByRole("button", { name: "Views", exact: true }).click();
  await workspace(page).getByRole("button", { name: "County Atlas Bounded demo", exact: true }).click();
  await expect(drawer(page)).toHaveCount(0);
  await workspace(page).getByRole("button", { name: "Layers", exact: true }).click();
  await inspect(page).click();
  await expect(drawer(page)).toContainText("ANSWER / SUPPORTED");
  await workspace(page).getByRole("button", { name: "Inspect connection", exact: true }).first().click();
  await expect(drawer(page)).toHaveCount(0);
  await expect(workspace(page).locator(".atlas-evidence-drawer")).toContainText("Connection Inspector");
  await workspace(page).getByRole("button", { name: "New from map", exact: true }).click();
  await workspace(page).getByRole("button", { name: "Create report draft", exact: true }).click();
  const draft = await page.evaluate(() => JSON.parse(localStorage.getItem("kfm.explorer.report-drafts.v2") ?? "[]").at(-1));
  expect(draft.includedEvidenceRefs).toEqual([]);
});

test("supports the local service journey at a narrow viewport", async ({ page }, testInfo) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await openLayers(page);
  await inspect(page).click();
  await expect(drawer(page)).toContainText("ANSWER / SUPPORTED");
  await expect(drawer(page).getByRole("link", { name: "Repository synthetic layer declaration" })).toBeVisible();
  await expect(drawer(page).getByRole("heading", { level: 2 })).toBeFocused();
  expect(await workspace(page).locator(".atlas-evidence-drawer").evaluate((node) => node.scrollTop)).toBe(0);
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
  expect(overflow).toBe(false);
  await testInfo.attach("Local evidence mobile", { body: await workspace(page).screenshot(), contentType: "image/png" });
});
