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
  await expect(workspace.locator(".atlas-view-list > button")).toHaveCount(18);
  await expect(workspace.locator("#kfm-living-atlas-map canvas")).toHaveCount(1);
  await expect(workspace.getByRole("status").filter({ hasText: "Renderer" })).toContainText("READY");
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

test("recovers from malformed persisted draft collections", async ({ page }) => {
  await page.addInitScript(() => {
    window.localStorage.setItem("kfm.explorer.report-drafts.v2", JSON.stringify({ stale: true }));
    window.localStorage.setItem("kfm.explorer.story-scenes.v2", JSON.stringify([null, "stale"]));
    window.localStorage.setItem("kfm.explorer.report-drafts.v1", JSON.stringify([{
      profile: "kfm.explorer.report-draft.v1",
      id: "report:legacy-pre-temporal-invariant",
      snapshot: {
        profile: "kfm.explorer.map-snapshot.v1",
        selectedLayerId: "layer:county-locators",
        evidenceRefs: ["evidence:stale-out-of-time"],
      },
    }]));
  });

  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');
  await expect(workspace).toBeVisible();
  await expect(workspace.getByRole("heading", { name: "Kansas Living Atlas" })).toBeVisible();
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

  await workspace.getByRole("button", { name: "Map" }).click();
  await workspace.getByRole("button", { name: "Ask Focus for bounded next steps" }).click();
  await expect(workspace.getByRole("status").filter({ hasText: "ABSTAIN" })).toBeVisible();

  await workspace.getByRole("button", { name: "Layers" }).click();
  const availableLayer = workspace.locator(".atlas-layer-row", {
    hasText: "Generalized Kansas extent",
  });
  await availableLayer.getByRole("button", { name: "Inspect" }).click();
  await expect(
    workspace.getByRole("complementary", { name: "Evidence Drawer" }),
  ).toContainText("ABSTAIN · VIEW_DATA_HELD");

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
