import { expect, test } from "playwright/test";

test("mounts the map-first Living Atlas without external requests", async ({
  page,
}) => {
  const externalRequests: string[] = [];
  page.on("request", (request) => {
    const url = new URL(request.url());
    if (!url.hostname.match(/^(127\.0\.0\.1|localhost)$/)) {
      externalRequests.push(request.url());
    }
  });

  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');
  await expect(workspace).toBeVisible();
  await expect(workspace.getByRole("heading", { name: "Kansas Living Atlas" })).toBeVisible();
  await expect(workspace.locator('[data-rail-panel="views"] > .atlas-view-list > button')).toHaveCount(7);
  await expect(workspace.locator(".atlas-held-views .atlas-view-button")).toHaveCount(11);
  await expect(workspace.locator("#kfm-living-atlas-map canvas")).toHaveCount(1);
  await expect(workspace.getByRole("status").filter({ hasText: "Renderer" })).toContainText("READY");
  expect(externalRequests).toEqual([]);
});

test("guides first use and keeps held views behind an accessible disclosure", async ({ page }) => {
  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');
  const guide = workspace.getByRole("region", { name: "Start exploring this synthetic atlas" });
  await expect(guide).toContainText("synthetic or generalized");
  await expect(guide).toContainText("live source admission is held");

  const held = workspace.locator(".atlas-held-views");
  await expect(held).not.toHaveAttribute("open");
  await expect(workspace.getByRole("button", { name: /Terrain & Landforms/ })).toBeHidden();
  await guide.getByRole("button", { name: "Inspect a demo layer" }).click();
  await expect(workspace.getByRole("heading", { name: "Layer catalog" })).toBeVisible();
  await expect(workspace.locator(".atlas-layer-row button").first()).toBeFocused();
  await page.keyboard.press("Enter");
  await expect(workspace.getByRole("complementary", { name: "Evidence Drawer" }))
    .toContainText("Generalized Kansas extent");
  await expect(workspace.getByRole("complementary", { name: "Evidence Drawer" }))
    .toContainText("Source and time");

  await workspace.getByRole("button", { name: "Views" }).click();
  await workspace.getByRole("searchbox", { name: "Search Living Atlas catalog" }).fill("Terrain & Landforms");
  await expect(held).toHaveAttribute("open");
  await workspace.getByRole("button", { name: /Terrain & Landforms/ }).click();
  await expect(workspace.getByRole("status").filter({ hasText: "HELD" })).toBeVisible();
});

test("narrow first-use path has no horizontal overflow and preserves the text alternative", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');
  await expect(workspace.getByRole("region", { name: "Start exploring this synthetic atlas" })).toBeVisible();
  await expect(workspace.getByRole("button", { name: "Inspect a demo layer" })).toBeVisible();
  await workspace.getByRole("button", { name: "Inspect a demo layer" }).click();
  await workspace.locator(".atlas-layer-row button").first().click();
  await expect(workspace.getByRole("complementary", { name: "Evidence Drawer" })).toBeVisible();
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
  expect(overflow).toBe(false);
});

test("renders every Living Waters fixture scenario as finite non-authoritative state", async ({
  page,
}) => {
  const externalRequests: string[] = [];
  page.on("request", (request) => {
    const url = new URL(request.url());
    if (
      (url.protocol === "http:" || url.protocol === "https:") &&
      !["127.0.0.1", "localhost"].includes(url.hostname)
    ) {
      externalRequests.push(url.href);
    }
  });

  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');
  await workspace.getByRole("button", { name: "Layers" }).click();
  const card = workspace.locator(".atlas-fixture-card");
  await expect(card).toHaveAttribute(
    "aria-label",
    "Living Waters synthetic fixture proof",
  );
  const scenario = card.getByRole("combobox", {
    name: "Living Waters fixture scenario",
  });
  await expect(scenario).toHaveValue("current");

  const expected = [
    { id: "current", state: "AVAILABLE", points: 3 },
    { id: "stale", state: "STALE", points: 3 },
    { id: "no-results", state: "NO_RESULTS", points: 0 },
    { id: "unavailable", state: "UNAVAILABLE", points: 0 },
    { id: "ambiguous-reach", state: "ABSTAIN", points: 0 },
  ] as const;

  for (const entry of expected) {
    await scenario.selectOption(entry.id);
    await expect(card).toHaveAttribute("data-frame-state", entry.state);
    await expect(card.locator(".atlas-fixture-status")).toContainText(
      entry.state,
    );
    await expect(card.locator(".atlas-fixture-chart span")).toHaveCount(
      entry.points === 0 ? 1 : entry.points,
    );
    if (entry.points === 0) {
      await expect(card.locator(".atlas-fixture-chart span")).toContainText(
        "No observations are rendered for this finite state.",
      );
    }
    await expect(card.locator(".atlas-fixture-trust")).toContainText(
      "SITE_LOCAL_DEMO",
    );
    await expect(card.locator(".atlas-fixture-trust")).toContainText(
      "visible=false",
    );
    await expect(card.locator(".atlas-fixture-trust")).toContainText(
      "rendererBound=false",
    );
  }

  expect(externalRequests).toEqual([]);
});

test("keeps held layers finite and captures only draft map state", async ({
  page,
}) => {
  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');

  await workspace.getByRole("button", { name: "Layers" }).click();
  const protectedLayer = workspace.locator(".atlas-layer-row", {
    hasText: "Protected-context envelope",
  });
  await expect(protectedLayer.getByRole("checkbox")).toBeDisabled();
  await protectedLayer.getByRole("button", { name: "Inspect" }).click();
  await expect(workspace.getByRole("complementary", { name: "Evidence Drawer" })).toContainText(
    "DENY · PROTECTED_SPATIAL_DETAIL",
  );

  await workspace.getByRole("button", { name: "New from map" }).click();
  await workspace.getByRole("button", { name: "Create report draft" }).click();
  await expect(workspace.getByRole("heading", { name: "Reports from map state" })).toBeVisible();
  await expect(workspace.locator(".atlas-draft-card").first()).toContainText("DRAFT");
  await expect(workspace.getByRole("button", { name: /publish/i })).toHaveCount(0);
});

test("clears out-of-time selection and evidence when the committed map time changes", async ({
  page,
}) => {
  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');

  await workspace.getByRole("button", { name: "Layers" }).click();
  const countyLayer = workspace.locator(".atlas-layer-row", {
    hasText: "County locator starter points",
  });
  await countyLayer.getByRole("button", { name: "Inspect" }).click();
  await expect(workspace.getByRole("complementary", { name: "Evidence Drawer" }))
    .toContainText("County locator starter points");

  await workspace.getByRole("slider", { name: "Preview atlas time" }).fill("10");
  await workspace.getByRole("button", { name: "Apply time" }).click();
  await expect(countyLayer.getByRole("checkbox")).toBeDisabled();
  await expect(countyLayer.getByRole("checkbox")).not.toBeChecked();
  await expect(workspace.getByRole("complementary", { name: "Evidence Drawer" }))
    .toContainText("Inspect before interpretation");

  await countyLayer.getByRole("button", { name: "Inspect" }).click();
  await expect(workspace.getByRole("status").filter({
    hasText: "outside the committed time bucket",
  })).toBeVisible();
  await expect(workspace.getByRole("complementary", { name: "Evidence Drawer" }))
    .toContainText("Inspect before interpretation");
});

test("preserves timeless selection and evidence across committed time changes", async ({
  page,
}) => {
  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');

  await workspace.getByRole("button", { name: "Layers" }).click();
  const timelessLayer = workspace.locator(".atlas-layer-row", {
    hasText: "Generalized Kansas extent",
  });
  await timelessLayer.getByRole("button", { name: "Inspect" }).click();
  await expect(workspace.getByRole("complementary", { name: "Evidence Drawer" }))
    .toContainText("Generalized Kansas extent");

  await workspace.getByRole("slider", { name: "Preview atlas time" }).fill("10");
  await workspace.getByRole("button", { name: "Apply time" }).click();
  await expect(workspace.getByRole("complementary", { name: "Evidence Drawer" }))
    .toContainText("Generalized Kansas extent");

  await workspace.getByRole("button", { name: "New from map" }).click();
  await workspace.getByRole("button", { name: "Create report draft" }).click();
  const draft = await page.evaluate(() => {
    const raw = window.localStorage.getItem("kfm.explorer.report-drafts.v2");
    return raw === null ? null : (JSON.parse(raw) as Array<{
      snapshot: {
        committedTimeId: string;
        selectedLayerId: string | null;
        evidenceRefs: string[];
      };
      includedEvidenceRefs: string[];
    }>)[0];
  });
  expect(draft?.snapshot).toMatchObject({
    committedTimeId: "time:1900s",
    selectedLayerId: "layer:kansas-frame",
  });
  expect(draft?.snapshot.evidenceRefs.length).toBeGreaterThan(0);
  expect(draft?.includedEvidenceRefs).toEqual(draft?.snapshot.evidenceRefs);
});

test("recovers from malformed persisted draft collections", async ({ page }) => {
  await page.addInitScript(() => {
    window.localStorage.setItem("kfm.explorer.report-drafts.v2", JSON.stringify([{
      profile: "kfm.explorer.report-draft.v1",
      id: "report:shallow-v2",
      snapshot: { profile: "kfm.explorer.map-snapshot.v1" },
      publishable: true,
    }]));
    window.localStorage.setItem("kfm.explorer.story-scenes.v2", JSON.stringify([{
      profile: "kfm.explorer.story-scene.v1",
      id: "story:shallow-v2",
      snapshot: { profile: "kfm.explorer.map-snapshot.v1" },
    }]));
  });

  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');
  await expect(workspace).toBeVisible();
  await expect(workspace.getByRole("heading", { name: "Kansas Living Atlas" })).toBeVisible();
  await workspace.getByRole("button", { name: "Reports" }).click();
  await expect(workspace.locator(".atlas-draft-card")).toHaveCount(0);
  await workspace.getByRole("button", { name: "Stories" }).click();
  await expect(workspace.locator(".atlas-draft-card")).toHaveCount(0);
});

test("loads valid legacy drafts only when the v2 collection is absent", async ({ page }) => {
  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');

  await workspace.getByRole("button", { name: "New from map" }).click();
  await workspace.getByRole("button", { name: "Create report draft" }).click();
  await page.evaluate(() => {
    const current = window.localStorage.getItem("kfm.explorer.report-drafts.v2");
    if (current !== null) {
      window.localStorage.setItem("kfm.explorer.report-drafts.v1", current);
    }
    window.localStorage.removeItem("kfm.explorer.report-drafts.v2");
  });

  await page.reload();
  await workspace.getByRole("button", { name: "Reports" }).click();
  await expect(workspace.locator(".atlas-draft-card")).toHaveCount(1);

  await page.evaluate(() => {
    window.localStorage.setItem("kfm.explorer.report-drafts.v2", "malformed");
  });
  await page.reload();
  await workspace.getByRole("button", { name: "Reports" }).click();
  await expect(workspace.locator(".atlas-draft-card")).toHaveCount(0);
});

test("keeps held-view evidence, Focus, and report snapshots aligned", async ({
  page,
}) => {
  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');

  await workspace.getByRole("button", { name: "Layers" }).click();
  const protectedLayer = workspace.locator(".atlas-layer-row", {
    hasText: "Protected-context envelope",
  });
  await protectedLayer.getByRole("button", { name: "Inspect" }).click();
  await expect(workspace.getByRole("complementary", { name: "Evidence Drawer" })).toContainText(
    "DENY · PROTECTED_SPATIAL_DETAIL",
  );

  await workspace.getByRole("button", { name: "Views" }).click();
  await workspace.getByText("11 views awaiting data admission").click();
  await workspace.getByRole("button", { name: /Archaeology & Cultural Landscapes/ }).click();
  await expect(workspace.getByRole("complementary", { name: "Evidence Drawer" })).toContainText(
    "DENY · PROTECTED_SPATIAL_DETAIL",
  );
  await workspace.getByRole("button", { name: /Weather Window/ }).click();
  await expect(workspace.getByRole("complementary", { name: "Evidence Drawer" })).toContainText(
    "Inspect before interpretation",
  );

  await workspace.getByRole("button", { name: "New from map" }).click();
  await workspace.getByRole("button", { name: "Create report draft" }).click();
  const outOfTimeHeldDraft = await page.evaluate(() => {
    const raw = window.localStorage.getItem("kfm.explorer.report-drafts.v2");
    return raw === null ? null : (JSON.parse(raw) as Array<{
      snapshot: { activeViewId: string; selectedLayerId: string | null; evidenceRefs: string[] };
      includedEvidenceRefs: string[];
    }>)[0];
  });
  expect(outOfTimeHeldDraft?.snapshot).toMatchObject({
    activeViewId: "view:weather-window",
    selectedLayerId: null,
    evidenceRefs: [],
  });
  expect(outOfTimeHeldDraft?.includedEvidenceRefs).toEqual([]);

  await workspace.getByRole("button", { name: "Map", exact: true }).click();
  await workspace.getByRole("button", { name: "Layers" }).click();
  const availableLayer = workspace.locator(".atlas-layer-row", {
    hasText: "Generalized Kansas extent",
  });
  await availableLayer.getByRole("button", { name: "Inspect" }).click();
  await expect(
    workspace.getByRole("complementary", { name: "Evidence Drawer" }),
  ).toContainText("ABSTAIN · VIEW_DATA_HELD");
  await workspace.getByRole("button", { name: "Ask Focus for bounded next steps" }).click();
  await expect(workspace.getByRole("status").filter({ hasText: "ABSTAIN" })).toBeVisible();

  await workspace.getByRole("button", { name: "New from map" }).click();
  await workspace.getByRole("button", { name: "Create report draft" }).click();
  await expect(workspace.locator(".atlas-draft-card").first()).toContainText("view:weather-window");
  const latestDraft = await page.evaluate(() => {
    const raw = window.localStorage.getItem("kfm.explorer.report-drafts.v2");
    return raw === null ? null : (JSON.parse(raw) as Array<{
      snapshot: {
        activeViewId: string;
        selectedLayerId: string | null;
        evidenceRefs: string[];
      };
      includedEvidenceRefs: string[];
    }>)[0];
  });
  expect(latestDraft?.snapshot).toMatchObject({
    activeViewId: "view:weather-window",
    selectedLayerId: "layer:kansas-frame",
    evidenceRefs: [],
  });
  expect(latestDraft?.includedEvidenceRefs).toEqual([]);
});

test("exposes repository layer lineage and keeps candidate data unadmitted", async ({
  page,
}) => {
  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');

  await workspace.getByRole("button", { name: "Layers" }).click();
  const runtimeLayer = workspace.locator(".atlas-layer-row", {
    hasText: "Generalized Kansas extent",
  });
  await runtimeLayer.getByRole("button", { name: "Inspect" }).click();
  await expect(
    workspace.getByRole("complementary", { name: "Evidence Drawer" }),
  ).toContainText("Generalized Kansas extent");
  const candidate = workspace.locator(".atlas-connection-card", {
    hasText: "WBD HUC12 watershed boundaries",
  });
  await expect(candidate).toContainText("FIXTURE_ONLY");
  await candidate.getByRole("button", { name: "Inspect connection" }).click();
  const drawer = workspace.getByRole("complementary", {
    name: "Evidence Drawer",
  });
  await expect(drawer).toContainText("FIXTURE_ONLY · NOT ADMITTED");
  await expect(drawer.getByRole("link", { name: /CONNECTOR/ })).toHaveAttribute(
    "href",
    /\/tree\/[^/]+\/connectors\/usgs\/wbd_huc$/,
  );
  await expect(drawer.getByRole("link", { name: /PIPELINE/ })).toHaveAttribute(
    "href",
    /\/blob\/[^/]+\/pipeline_specs\/hydrology\/wbd_huc12_ingest\.yaml$/,
  );

  await workspace.getByRole("button", { name: "New from map" }).click();
  await workspace.getByRole("button", { name: "Create report draft" }).click();
  const latestDraft = await page.evaluate(() => {
    const raw = window.localStorage.getItem("kfm.explorer.report-drafts.v2");
    return raw === null ? null : (JSON.parse(raw) as Array<{
      snapshot: { selectedLayerId: string | null; evidenceRefs: string[] };
      includedEvidenceRefs: string[];
    }>)[0];
  });
  expect(latestDraft?.snapshot.selectedLayerId).toBeNull();
  expect(latestDraft?.snapshot.evidenceRefs).toEqual([]);
  expect(latestDraft?.includedEvidenceRefs).toEqual([]);
});

test("connects Living Atlas tools to the repository feature catalog", async ({
  page,
}) => {
  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');

  const heldTools = workspace.locator(".atlas-held-tools");
  await expect(heldTools).not.toHaveAttribute("open");
  await workspace.getByText("3 held tools").click();
  await expect(heldTools).toHaveAttribute("open");
  await expect(heldTools).toContainText("Measurement, projection, units, uncertainty, and export contracts are not bound.");

  const heldMeasure = workspace.locator(".atlas-interaction-bar").getByRole("button", {
    name: "Measure · HELD",
    exact: true,
  });
  await expect(heldMeasure).toHaveAttribute("title", /projection, units, uncertainty/);
  await heldMeasure.focus();
  await expect(heldMeasure).toBeFocused();
  await heldMeasure.click();
  await expect(workspace.getByRole("status").filter({ hasText: "Measure HELD" })).toContainText(
    "projection, units, uncertainty",
  );

  const features = page.locator("#features");
  await features.getByLabel("Filter by feature area").selectOption("Evidence and trust");
  await features.getByLabel("Filter by maturity").selectOption("VERIFIED_SLICE");
  await workspace.getByRole("button", { name: "Tools" }).click();
  await expect(workspace.locator(".atlas-tool-card")).toHaveCount(14);
  const hucTool = workspace.locator(".atlas-tool-card", {
    hasText: "HUC crosswalk explorer",
  });
  await hucTool.getByRole("button", { name: "Open workbench catalog" }).click();
  await expect(features.getByLabel("Filter by feature area")).toHaveValue("ALL");
  await expect(features.getByLabel("Filter by maturity")).toHaveValue("ALL");
  await expect(features.getByRole("status")).toHaveText(
    /1 of \d+ feature families shown/,
  );
  await expect(features.getByRole("heading", { name: "HUC crosswalk explorer" })).toBeVisible();
});

test("reveals the matching catalog panel when searching from another tab", async ({
  page,
}) => {
  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');

  await workspace.getByLabel("Search Living Atlas catalog").fill("Measure");

  await expect(workspace.getByRole("button", { name: "Tools" })).toHaveAttribute(
    "aria-pressed",
    "true",
  );
  await expect(workspace.locator(".atlas-tool-card", { hasText: "Measure" })).toBeVisible();
});
