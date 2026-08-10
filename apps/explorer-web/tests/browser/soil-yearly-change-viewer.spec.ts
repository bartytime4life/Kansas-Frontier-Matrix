import { expect, test } from "playwright/test";

test("renders fixture-only SSURGO metrics and provenance anchors", async ({ page }) => {
  await page.goto("/tests/browser/soil-yearly-change-viewer.html");

  const viewer = page.getByRole("region", {
    name: "SSURGO yearly change comparison",
  });
  await expect(viewer).toBeVisible();
  await expect(viewer.locator("[data-year-range]")).toHaveText("2025 to 2026");
  await expect(viewer).toContainText("Added records1");
  await expect(viewer).toContainText("Removed records1");
  await expect(viewer).toContainText("Modified records1");
  await expect(viewer).toContainText("representative_slope_pct");
  await expect(viewer).toContainText("do not establish soil change");

  await viewer.getByText("Inspect fixture provenance anchors").click();
  await expect(viewer).toContainText("stac://kfm/soil/ssurgo/2026-synthetic");
  await expect(viewer).toContainText(
    "kfm://prov/activity/diff/soil-ssurgo-2025-2026",
  );
});

test("malformed projection renders no viewer and reflects no canary", async ({
  page,
}) => {
  await page.goto("/tests/browser/soil-yearly-change-viewer.html?fixture=invalid");

  await expect(
    page.locator("[data-component='soil-yearly-change-viewer']"),
  ).toHaveCount(0);
  await expect(page.locator("body")).not.toContainText(
    "SSURGO_INTERNAL_CANARY_57f22a",
  );
});
