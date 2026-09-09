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

test("exposes repository layer lineage and keeps candidate data unadmitted", async ({
  page,
}) => {
  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');

  await workspace.getByRole("button", { name: "Layers" }).click();
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
});

test("connects Living Atlas tools to the repository feature catalog", async ({
  page,
}) => {
  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');

  await workspace.locator(".atlas-interaction-bar").getByRole("button", {
    name: "Measure",
  }).click();
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
