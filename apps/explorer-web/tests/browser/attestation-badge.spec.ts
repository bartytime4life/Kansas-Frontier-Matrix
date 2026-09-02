import { expect, test } from "playwright/test";

test("renders a text-first badge that delegates proof inspection", async ({ page }) => {
  await page.goto("/tests/browser/attestation-badge.html?fixture=verified");

  const badge = page.getByRole("status", {
    name: "Attestation status: checks reported verified",
  });
  await expect(badge).toBeVisible();
  await expect(badge.locator("[data-attestation-status]"))
    .toHaveText("VERIFIED");
  await expect(badge).toContainText("The badge is not proof or release authority.");
  await expect(badge).not.toContainText("kfm://");

  await page.getByRole("button", { name: "Inspect supporting references" }).click();
  await expect(page.locator("#fixture-root")).toHaveAttribute(
    "data-inspection-requested",
    "true",
  );
  await expect(page.locator("#fixture-root")).toHaveAttribute(
    "data-inspect-calls",
    "1",
  );
});

test("malformed detail renders no badge and reflects no canary", async ({ page }) => {
  await page.goto("/tests/browser/attestation-badge.html?fixture=invalid");

  await expect(page.locator("[data-component='attestation-badge']")).toHaveCount(0);
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.locator("body")).not.toContainText(
    "ATTESTATION_INTERNAL_CANARY_845ad2",
  );
});
