import { expect, test } from "playwright/test";

test("renders four public-safe summaries and delegates receipt inspection", async ({
  page,
}) => {
  await page.goto("/tests/browser/redaction-preview.html?fixture=ready");

  const preview = page.getByRole("region", {
    name: "Redaction preview: public-safe transforms ready",
  });
  await expect(preview).toBeVisible();
  await expect(preview.locator("dt")).toHaveCount(4);
  await expect(preview).toContainText("Generalized");
  await expect(preview).toContainText("Low-count cells suppressed");
  await expect(preview).toContainText("z10");
  await expect(preview).toContainText("County aggregate");
  await expect(preview).toContainText("not policy approval");
  await expect(preview).not.toContainText("kfm://");

  await page.getByRole("button", { name: "Inspect redaction receipt" }).click();
  await expect(page.locator("#fixture-root")).toHaveAttribute(
    "data-receipt-inspection-requested",
    "true",
  );
  await expect(page.locator("#fixture-root")).toHaveAttribute(
    "data-inspect-calls",
    "1",
  );
});

test("malformed restricted detail renders fixed error copy without reflection", async ({
  page,
}) => {
  await page.goto("/tests/browser/redaction-preview.html?fixture=invalid");

  const preview = page.getByRole("alert", {
    name: "Redaction preview: error",
  });
  await expect(preview).toBeVisible();
  await expect(preview.locator("dt")).toHaveCount(0);
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(preview).toContainText("No candidate details are displayed");
  await expect(page.locator("body")).not.toContainText(
    "RESTRICTED_GEOMETRY_CANARY_52b6",
  );
});
