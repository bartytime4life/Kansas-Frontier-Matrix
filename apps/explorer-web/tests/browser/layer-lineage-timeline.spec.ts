import { expect, test } from "playwright/test";

test("renders a chronological read-only correction and rollback chain", async ({ page }) => {
  await page.goto("/tests/browser/layer-lineage-timeline.html?fixture=available");

  const timeline = page.getByRole("region", {
    name: "Rollback and correction lineage",
  });
  await expect(timeline).toBeVisible();
  await expect(timeline).toContainText("Current release state: ROLLED_BACK");
  await expect(timeline).toContainText("Correction published");
  await expect(timeline).toContainText(
    "kfm://receipt/correction/synthetic/correction-001",
  );
  await expect(timeline).toContainText("Rollback applied");
  await expect(timeline).toContainText("kfm://release/synthetic/release-001");
  await expect(timeline).toContainText("cannot correct, withdraw, roll back");
  await expect(timeline.locator("[data-lineage-sequence]")).toHaveCount(3);
  await expect(timeline.getByRole("button")).toHaveCount(0);
});

test("malformed detail renders no timeline and reflects no canary", async ({ page }) => {
  await page.goto("/tests/browser/layer-lineage-timeline.html?fixture=invalid");

  await expect(page.locator("[data-component='layer-lineage-timeline']")).toHaveCount(0);
  await expect(page.locator("[data-lineage-sequence]")).toHaveCount(0);
  await expect(page.locator("body")).not.toContainText(
    "LINEAGE_INTERNAL_CANARY_0b71d8",
  );
});
