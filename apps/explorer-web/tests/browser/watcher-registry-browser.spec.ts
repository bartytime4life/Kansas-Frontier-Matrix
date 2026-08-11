import { expect, test } from "playwright/test";

test("shows inactive watcher metadata without action controls", async ({ page }) => {
  await page.goto("/tests/browser/watcher-registry-browser.html?fixture=available");

  const panel = page.getByRole("region", { name: "Watcher Registry browser: available" });
  await expect(panel).toBeVisible();
  await expect(panel).toContainText("PROPOSED_INACTIVE");
  await expect(panel).toContainText("kfm.watcher.shared.plants_drift.placeholder");
  await expect(panel).toContainText("kfm.watcher.soil.ssurgo_gnatsgo.candidate");
  await expect(panel).toContainText("cannot read the registry");
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});

test("malformed detail reflects no canary", async ({ page }) => {
  await page.goto("/tests/browser/watcher-registry-browser.html?fixture=invalid");

  const panel = page.getByRole("region", { name: "Watcher Registry browser: error" });
  await expect(panel).toContainText("INVALID_PAYLOAD");
  await expect(panel).not.toContainText("WATCHER_REGISTRY_INTERNAL_CANARY_9c45a1");
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});
