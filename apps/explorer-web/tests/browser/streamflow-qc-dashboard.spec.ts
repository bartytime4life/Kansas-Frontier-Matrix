import { expect, test } from "playwright/test";

test("renders regional context and opaque evidence references", async ({
  page,
}) => {
  await page.goto(
    "/tests/browser/streamflow-qc-dashboard.html?fixture=regional",
  );

  const dashboard = page.getByRole("region", {
    name: "Streamflow QC dashboard: available",
  });
  await expect(dashboard).toBeVisible();
  await expect(dashboard).toContainText(
    "AVAILABLE / REGIONAL_CONTEXT_AVAILABLE",
  );
  await expect(dashboard).toContainText(
    "kfm:gauge:synthetic-kansas-001",
  );
  await expect(dashboard).toContainText("LOW_PERCENTILE");
  await expect(dashboard).toContainText("CORROBORATES_LOW_FLOW");
  await expect(dashboard).toContainText("SUPPORTS_LOW_FLOW");
  await expect(dashboard.locator("ol li")).toHaveCount(3);
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});

test("held context exposes no gauge or evidence detail", async ({ page }) => {
  await page.goto("/tests/browser/streamflow-qc-dashboard.html?fixture=held");

  const dashboard = page.getByRole("region", {
    name: "Streamflow QC dashboard: abstain",
  });
  await expect(dashboard).toContainText("ABSTAIN / CONTEXT_HELD");
  await expect(dashboard).toContainText(
    "No gauge or evidence detail is displayed.",
  );
  await expect(dashboard.locator("ol li")).toHaveCount(0);
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});

test("invalid raw detail fails closed and is not reflected", async ({
  page,
}) => {
  await page.goto(
    "/tests/browser/streamflow-qc-dashboard.html?fixture=invalid",
  );

  const dashboard = page.getByRole("region", {
    name: "Streamflow QC dashboard: error",
  });
  await expect(dashboard).toContainText("ERROR / INVALID_PAYLOAD");
  await expect(dashboard).toContainText(
    "No gauge or evidence detail is displayed.",
  );
  await expect(dashboard).not.toContainText(
    "SENSITIVE_STREAMFLOW_CANARY_8c21",
  );
  await expect(dashboard.locator("ol li")).toHaveCount(0);
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});
