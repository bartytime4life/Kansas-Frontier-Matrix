import { expect, test } from "playwright/test";

test("renders synthetic digest-pinned artifacts without verification or rollback authority", async ({
  page,
}) => {
  await page.goto("/tests/browser/oci-artifact-browser.html");

  const browser = page.getByRole("region", {
    name: "OCI artifact review browser",
  });
  await expect(browser).toBeVisible();
  await expect(browser.locator("[data-artifact-browser-status]")).toHaveText(
    "Review status: ANSWER",
  );
  await expect(browser.locator("tbody tr")).toHaveCount(2);
  await expect(browser).toContainText("Tag (mutable)");
  await expect(browser).toContainText("Digest (identity)");
  await expect(browser).toContainText("SIGNATURE: recorded, unverified");
  await expect(browser).toContainText("Candidate only — not authorized");

  await browser
    .getByText("Inspect county-basemap-2026-08-10 digest-pinned references")
    .click();
  await expect(browser).toContainText(
    `oci://registry.example/kfm/geospatial@sha256:${"a".repeat(64)}`,
  );
});

test("malformed projection renders no browser and reflects no canary", async ({
  page,
}) => {
  await page.goto("/tests/browser/oci-artifact-browser.html?fixture=invalid");

  await expect(
    page.locator("[data-component='oci-artifact-browser']"),
  ).toHaveCount(0);
  await expect(page.locator("body")).not.toContainText(
    "OCI_BROWSER_INTERNAL_CANARY_6b48d2",
  );
});
