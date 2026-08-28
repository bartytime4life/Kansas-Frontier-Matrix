import { expect, test } from "playwright/test";

test("renders a six-lane hold calendar without environmental interpretation", async ({
  page,
}) => {
  await page.goto("/tests/browser/county-environmental-cadence-calendar.html");

  const calendar = page.getByRole("region", {
    name: "County environmental cadence calendar",
  });
  await expect(calendar).toBeVisible();
  await expect(calendar.locator("[data-cadence-status]")).toHaveText(
    "Weekly cadence status: HOLD",
  );
  await expect(calendar.locator("tbody tr")).toHaveCount(6);
  await expect(calendar.locator("[data-cadence-lane='AIR']")).toContainText(
    "STALE",
  );
  await expect(
    calendar.locator("[data-cadence-lane='BIODIVERSITY']"),
  ).toContainText("Not recorded");
  await expect(calendar).toContainText("does not probe sources");

  await calendar
    .getByText("Inspect fixture scope and source-health references")
    .click();
  await expect(calendar).toContainText(
    "kfm:source-availability-watchlist:111111111111111111111111",
  );
});

test("malformed projection renders no calendar and reflects no canary", async ({
  page,
}) => {
  await page.goto(
    "/tests/browser/county-environmental-cadence-calendar.html?fixture=invalid",
  );

  await expect(
    page.locator("[data-component='county-environmental-cadence-calendar']"),
  ).toHaveCount(0);
  await expect(page.locator("body")).not.toContainText(
    "CADENCE_INTERNAL_CANARY_36ad0e",
  );
});
