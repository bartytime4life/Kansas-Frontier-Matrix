import { expect, test } from "playwright/test";

test("shows stable and review-routed sources without action controls", async ({ page }) => {
  await page.goto("/tests/browser/source-availability-watchlist.html?fixture=available");

  const panel = page.getByRole("region", { name: "Source availability watchlist" });
  await expect(panel).toBeVisible();
  await expect(panel).toContainText("REVIEW_REQUIRED");
  await expect(panel).toContainText("ks-mesonet");
  await expect(panel).toContainText("nrcs-ssurgo");
  await expect(panel).toContainText("REVIEW_CANDIDATE");
  await expect(panel).toContainText("does not probe sources");
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});

test("malformed detail renders no watchlist and reflects no canary", async ({ page }) => {
  await page.goto("/tests/browser/source-availability-watchlist.html?fixture=invalid");

  await expect(page.locator("[data-component='source-availability-watchlist']")).toHaveCount(0);
  await expect(page.locator("body")).not.toContainText(
    "SOURCE_WATCHLIST_INTERNAL_CANARY_41d8e2",
  );
});
