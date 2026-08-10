import { expect, test } from "playwright/test";

test("renders two proposed inactive registry entries", async ({ page }) => {
  await page.goto("/tests/browser/view-registry-inspector.html?fixture=available");

  const inspector = page.getByRole("region", {
    name: "View Registry inspector: available",
  });
  await expect(inspector).toBeVisible();
  await expect(inspector).toContainText(
    "AVAILABLE / REGISTRY_INSPECTION_READY",
  );
  await expect(inspector).toContainText(
    "kfm:view-registry:aaaaaaaaaaaaaaaaaaaaaaaa",
  );
  await expect(inspector.getByRole("row")).toHaveCount(3);
  await expect(inspector).toContainText("/map/hydrology/streamflow");
  await expect(inspector).toContainText("PMTILES");
  await expect(inspector).toContainText("PROPOSED_INACTIVE");
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});

test("held registry state exposes no entry table", async ({ page }) => {
  await page.goto("/tests/browser/view-registry-inspector.html?fixture=held");

  const inspector = page.getByRole("region", {
    name: "View Registry inspector: abstain",
  });
  await expect(inspector).toContainText(
    "ABSTAIN / REGISTRY_INSPECTION_HELD",
  );
  await expect(inspector).toContainText(
    "No route or layer detail is displayed.",
  );
  await expect(inspector.getByRole("table")).toHaveCount(0);
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});

test("invalid source detail fails closed and is not reflected", async ({
  page,
}) => {
  await page.goto("/tests/browser/view-registry-inspector.html?fixture=invalid");

  const inspector = page.getByRole("region", {
    name: "View Registry inspector: error",
  });
  await expect(inspector).toContainText("ERROR / INVALID_PAYLOAD");
  await expect(inspector).toContainText(
    "No registry detail is displayed.",
  );
  await expect(inspector).not.toContainText(
    "SENSITIVE_VIEW_REGISTRY_CANARY_7ad3",
  );
  await expect(inspector.getByRole("table")).toHaveCount(0);
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});
