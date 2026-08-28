import { expect, test } from "playwright/test";

test("renders bounded county NDVI candidate metrics with unresolved evidence visible", async ({
  page,
}) => {
  await page.goto("/tests/browser/county-ndvi-change-panel.html");

  const panel = page.getByRole("region", { name: "County NDVI change candidate" });
  await expect(panel).toBeVisible();
  await expect(panel.locator("[data-ndvi-classification]"))
    .toHaveText("Classification: GAIN_CANDIDATE");
  await expect(panel).toContainText("Candidate delta threshold");
  await expect(panel).toContainText("Changed area");
  await expect(panel).toContainText("12.50%");
  await expect(panel).toContainText("REFERENCED_NOT_RESOLVED");
  await expect(panel.getByRole("button")).toHaveCount(0);
  await expect(panel.getByRole("link")).toHaveCount(0);
});

test("policy denial carries no county, metric, or reference detail", async ({ page }) => {
  await page.goto("/tests/browser/county-ndvi-change-panel.html?fixture=denied");
  const panel = page.getByRole("status");
  await expect(panel).toContainText("County NDVI panel withheld");
  await expect(panel).not.toContainText("kfm://");
  await expect(panel.locator("dl")).toHaveCount(0);
});

test("malformed projection renders no panel and reflects no canary", async ({ page }) => {
  await page.goto("/tests/browser/county-ndvi-change-panel.html?fixture=invalid");
  await expect(page.locator("[data-component='county-ndvi-change-panel']")).toHaveCount(0);
  await expect(page.locator("body")).not.toContainText("NDVI_INTERNAL_CANARY_7c2d91");
});
