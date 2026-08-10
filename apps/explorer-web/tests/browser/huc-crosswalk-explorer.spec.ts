import { expect, test } from "playwright/test";

test("renders a verified HUC and two digest-bound station references", async ({
  page,
}) => {
  await page.goto("/tests/browser/huc-crosswalk-explorer.html?fixture=verified");

  const explorer = page.getByRole("region", {
    name: "HUC crosswalk explorer: available",
  });
  await expect(explorer).toBeVisible();
  await expect(explorer).toContainText("AVAILABLE / CROSSWALK_REFERENCE_READY");
  await expect(explorer).toContainText("County FIPS");
  await expect(explorer).toContainText("20177");
  await expect(explorer).toContainText("102600030101");
  await expect(explorer).toContainText("VERIFIED_EXACT");
  await expect(explorer.locator("ol li")).toHaveCount(2);
  await expect(explorer).toContainText("kfm://station/nwis/06889000@sha256:");
  await expect(explorer).not.toContainText("SENSITIVE_HUC_SOURCE_CANARY_91be");
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});

test("preserves ambiguity and renders no station reference", async ({ page }) => {
  await page.goto("/tests/browser/huc-crosswalk-explorer.html?fixture=ambiguous");

  const explorer = page.getByRole("region", {
    name: "HUC crosswalk explorer: abstain",
  });
  await expect(explorer).toContainText("ABSTAIN / CROSSWALK_REFERENCE_HELD");
  await expect(explorer).toContainText("AMBIGUOUS");
  await expect(explorer).toContainText("No station reference is displayed.");
  await expect(explorer.locator("ol li")).toHaveCount(0);
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});

test("invalid source detail fails closed and is not reflected", async ({ page }) => {
  await page.goto("/tests/browser/huc-crosswalk-explorer.html?fixture=invalid");

  const explorer = page.getByRole("region", {
    name: "HUC crosswalk explorer: error",
  });
  await expect(explorer).toContainText("ERROR / INVALID_PAYLOAD");
  await expect(explorer).toContainText("No crosswalk detail is displayed.");
  await expect(explorer).not.toContainText("SENSITIVE_HUC_SOURCE_CANARY_91be");
  await expect(explorer.locator("ol li")).toHaveCount(0);
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});
