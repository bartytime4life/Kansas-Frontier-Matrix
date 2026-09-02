import { expect, test } from "playwright/test";

test("renders an evidence-referenced categorical candidate without event or health authority", async ({
  page,
}) => {
  await page.goto("/tests/browser/air-quality-trigger-panel.html");
  const panel = page.getByRole("region", { name: "PM2.5 trigger candidate" });
  await expect(panel).toBeVisible();
  await expect(panel.locator("[data-air-quality-candidate-state]"))
    .toHaveText("Candidate state: PROPOSED_TRIGGER_CANDIDATE");
  await expect(panel).toContainText("ABOVE_MONITORED_THRESHOLD");
  await expect(panel).toContainText("ABOVE_TRAILING_MEDIAN");
  await expect(panel).toContainText("REFERENCED_NOT_RESOLVED");
  await expect(panel).toContainText("Evidence reference count2");
  await expect(panel).toContainText("not an air-quality event");
  await expect(panel.getByRole("button")).toHaveCount(0);
  await expect(panel.getByRole("link")).toHaveCount(0);
});

test("renders no-trigger state separately from a proposed candidate", async ({ page }) => {
  await page.goto("/tests/browser/air-quality-trigger-panel.html?fixture=no-trigger");
  const panel = page.getByRole("region", { name: "No PM2.5 trigger candidate" });
  await expect(panel.locator("[data-air-quality-candidate-state]"))
    .toHaveText("Candidate state: NO_TRIGGER_CANDIDATE");
  await expect(panel).toContainText("AT_OR_BELOW_MONITORED_THRESHOLD");
});

test("policy denial carries no candidate or reference detail", async ({ page }) => {
  await page.goto("/tests/browser/air-quality-trigger-panel.html?fixture=denied");
  const panel = page.getByRole("status");
  await expect(panel).toContainText("PM2.5 trigger panel withheld");
  await expect(panel).not.toContainText("kfm://");
  await expect(panel.locator("dl")).toHaveCount(0);
});

test("malformed raw detail renders no panel and reflects no canary", async ({ page }) => {
  await page.goto("/tests/browser/air-quality-trigger-panel.html?fixture=invalid");
  await expect(page.locator("[data-component='air-quality-trigger-panel']")).toHaveCount(0);
  await expect(page.locator("body")).not.toContainText("PM25_INTERNAL_CANARY_19ea6c");
  await expect(page.locator("body")).not.toContainText("35.1");
});
