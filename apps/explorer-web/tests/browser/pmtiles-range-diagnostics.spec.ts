import { expect, test } from "playwright/test";

test("shows structural checks and unresolved holds without health authority", async ({ page }) => {
  await page.goto("/tests/browser/pmtiles-range-diagnostics.html?fixture=available");

  const panel = page.getByRole("region", { name: "PMTiles range diagnostics" });
  await expect(panel).toBeVisible();
  await expect(panel).toContainText("STRUCTURAL_HOLD");
  await expect(panel).toContainText("Range SUPPORTED");
  await expect(panel).toContainText("PMSIG SHAPE_BOUND");
  await expect(panel).toContainText("CRYPTOGRAPHIC_VERIFICATION_UNWIRED");
  await expect(panel).toContainText("does not prove cryptographic trust");
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});

test("malformed detail renders no diagnostics and reflects no canary", async ({ page }) => {
  await page.goto("/tests/browser/pmtiles-range-diagnostics.html?fixture=invalid");

  await expect(page.locator("[data-component='pmtiles-range-diagnostics']")).toHaveCount(0);
  await expect(page.locator("body")).not.toContainText("PMTILES_INTERNAL_CANARY_782ca1");
});
