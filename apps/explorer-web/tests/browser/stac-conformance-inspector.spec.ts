import { expect, test } from "playwright/test";

test("shows closed STAC conformance detail without action controls", async ({
  page,
}) => {
  await page.goto(
    "/tests/browser/stac-conformance-inspector.html?fixture=conformant",
  );

  const panel = page.getByRole("region", {
    name: "STAC conformance inspector: available",
  });
  await expect(panel).toBeVisible();
  await expect(panel).toContainText("AVAILABLE / INSPECTION_AVAILABLE");
  await expect(panel).toContainText("CONFORMANT");
  await expect(panel).toContainText("STAC_1_0_0_ITEM");
  await expect(panel).toContainText("kfm://profile/stac/kfm-profile-v1");
  await expect(panel).toContainText("application/vnd.pmtiles");
  await expect(panel).toContainText("COMPLETE; 8/8 required fields");
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});

test("keeps non-conformance visible without creating approval authority", async ({
  page,
}) => {
  await page.goto(
    "/tests/browser/stac-conformance-inspector.html?fixture=non-conformant",
  );

  const panel = page.getByRole("region", {
    name: "STAC conformance inspector: available",
  });
  await expect(panel).toContainText("NON_CONFORMANT");
  await expect(panel).toContainText("KFM_EXTENSION_MISSING");
  await expect(panel).toContainText("COLLECTION_CONTRACT_INCOMPLETE");
  await expect(panel).toContainText("does not query or mutate a catalog");
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});

test("malformed detail reflects no canary", async ({ page }) => {
  await page.goto(
    "/tests/browser/stac-conformance-inspector.html?fixture=invalid",
  );

  const panel = page.getByRole("region", {
    name: "STAC conformance inspector: error",
  });
  await expect(panel).toContainText("ERROR / INVALID_PAYLOAD");
  await expect(panel).not.toContainText("STAC_INSPECTOR_INTERNAL_CANARY_6d927e");
  await expect(panel.getByRole("table")).toHaveCount(0);
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});
