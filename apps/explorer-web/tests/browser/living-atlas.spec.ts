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
