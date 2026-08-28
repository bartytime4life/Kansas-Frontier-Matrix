import { expect, test } from "playwright/test";

test("renders a held scenario with uncertainty, equity, and inspectable references", async ({
  page,
}) => {
  await page.goto("/tests/browser/planning-scenario-review.html");

  const review = page.getByRole("region", {
    name: "Synthetic Kansas drought-planning exploration",
  });
  await expect(review).toBeVisible();
  await expect(review.locator("[data-scenario-status]")).toHaveText(
    "Scenario status: HELD — review candidate only",
  );
  await expect(review.locator("tbody tr")).toHaveCount(3);
  await expect(
    review.locator("[data-scenario-input='demand-index']"),
  ).toContainText("HIGH");
  await expect(review.locator("[data-scenario-assumption]")).toHaveCount(3);
  await expect(review.locator("[data-equity-dimension]")).toHaveCount(2);
  await expect(review).toContainText("not a prediction");
  await expect(review).not.toContainText("recommended action");

  await review
    .getByText("Inspect participation, evidence, and limitations")
    .click();
  await expect(review).toContainText("fixture:evidence:demand-series");
  await expect(review).toContainText("NOT_REGULATORY_DETERMINATION");
});

test("a denied projection exposes fixed copy and no scenario references", async ({
  page,
}) => {
  await page.goto("/tests/browser/planning-scenario-review.html?fixture=denied");

  const denied = page.getByRole("status", { name: "Planning scenario withheld" });
  await expect(denied).toBeVisible();
  await expect(denied).toContainText("DENY / POLICY_DENIED");
  await expect(denied).not.toContainText("fixture:");
  await expect(denied.locator("details, table, [data-equity-dimension]")).toHaveCount(0);
});

test("malformed projection renders no review and reflects no canary", async ({
  page,
}) => {
  await page.goto("/tests/browser/planning-scenario-review.html?fixture=invalid");

  await expect(
    page.locator("[data-component='planning-scenario-review']"),
  ).toHaveCount(0);
  await expect(page.locator("body")).not.toContainText(
    "PLANNING_SCENARIO_INTERNAL_CANARY_6ad4b2",
  );
});
