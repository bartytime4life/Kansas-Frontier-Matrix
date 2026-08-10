import { expect, test } from "playwright/test";

test("renders a five-lane hold scorecard without environmental interpretation", async ({
  page,
}) => {
  await page.goto("/tests/browser/environmental-anomaly-scorecard.html");

  const scorecard = page.getByRole("region", {
    name: "County environmental anomaly scorecard",
  });
  await expect(scorecard).toBeVisible();
  await expect(scorecard.locator("[data-scorecard-status]")).toHaveText(
    "Scorecard status: HOLD",
  );
  await expect(scorecard.locator("tbody tr")).toHaveCount(5);
  await expect(scorecard.locator("[data-scorecard-lane='AIR']")).toContainText(
    "STALE",
  );
  await expect(
    scorecard.locator("[data-scorecard-lane='VEGETATION']"),
  ).toContainText("PROPOSED");
  await expect(scorecard).toContainText("separate interpretation gate");

  await scorecard
    .getByText("Inspect fixture scope and governed references")
    .click();
  await expect(scorecard).toContainText(
    "kfm:anomaly-candidate:vegetation:synthetic:053:2026-08-10",
  );
});

test("malformed projection renders no scorecard and reflects no canary", async ({
  page,
}) => {
  await page.goto(
    "/tests/browser/environmental-anomaly-scorecard.html?fixture=invalid",
  );

  await expect(
    page.locator("[data-component='environmental-anomaly-scorecard']"),
  ).toHaveCount(0);
  await expect(page.locator("body")).not.toContainText(
    "SCORECARD_INTERNAL_CANARY_4f9c21",
  );
});
