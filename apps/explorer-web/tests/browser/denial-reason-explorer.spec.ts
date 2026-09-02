import { expect, test } from "playwright/test";

test("renders four fixed denial reasons without an override surface", async ({ page }) => {
  await page.goto("/tests/browser/denial-reason-explorer.html?fixture=valid");

  const explorer = page.getByRole("region", {
    name: "Denial reason explorer: release candidate blocked",
  });
  await expect(explorer).toBeVisible();
  await expect(explorer).toContainText("DENY / DENIAL_REASONS_READY");
  await expect(explorer).toContainText(
    "This surface cannot override the decision.",
  );
  await expect(explorer).toContainText("2026-08-10T15:00:00Z");
  await expect(explorer.locator("[data-reason-code]")).toHaveCount(4);
  expect(
    await explorer
      .locator("[data-reason-code]")
      .evaluateAll((items) => items.map((item) => item.getAttribute("data-reason-code"))),
  ).toEqual([
    "MISSING_RECEIPT",
    "INVALID_ATTESTATION",
    "LOW_COUNT_CELL",
    "ZOOM_TOO_FINE",
  ]);
  await expect(explorer).toContainText("Attach the governed receipt reference");
  await expect(explorer).toContainText("Apply an approved aggregation or redaction");
  await expect(explorer).not.toContainText("aaaaaaaaaaaaaaaa");
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});

test("invalid detail fails closed and is not reflected", async ({ page }) => {
  await page.goto("/tests/browser/denial-reason-explorer.html?fixture=invalid");

  const explorer = page.getByRole("region", {
    name: "Denial reason explorer: error",
  });
  await expect(explorer).toContainText("ERROR / INVALID_PAYLOAD");
  await expect(explorer).toContainText(
    "No review detail is displayed.",
  );
  await expect(explorer).not.toContainText("SENSITIVE_DENIAL_DETAIL_CANARY_f91c");
  await expect(explorer.locator("[data-reason-code]")).toHaveCount(0);
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});
