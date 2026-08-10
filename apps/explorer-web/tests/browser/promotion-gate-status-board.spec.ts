import { expect, test } from "playwright/test";

test("shows six projected gate components without action controls", async ({ page }) => {
  await page.goto("/tests/browser/promotion-gate-status-board.html?fixture=hold");

  const board = page.getByRole("region", { name: "Promotion gate status board" });
  await expect(board).toBeVisible();
  await expect(board).toContainText("HOLD");
  await expect(board).toContainText("SOURCE_MONITOR");
  await expect(board).toContainText("OPA_DECISION");
  await expect(board).toContainText("ATTESTATION");
  await expect(board).toContainText("RELEASE_MANIFEST_CANDIDATE");
  await expect(board).toContainText("does not execute checks");
  await expect(page.getByRole("button")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
});

test("malformed detail renders no board and reflects no canary", async ({ page }) => {
  await page.goto("/tests/browser/promotion-gate-status-board.html?fixture=invalid");

  await expect(page.locator("[data-component='promotion-gate-status-board']")).toHaveCount(0);
  await expect(page.locator("body")).not.toContainText(
    "PROMOTION_BOARD_INTERNAL_CANARY_395de0",
  );
});
