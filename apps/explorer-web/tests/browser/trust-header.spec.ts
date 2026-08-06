import { expect, test } from "playwright/test";

test("released support renders the complete governed badge set", async ({ page }) => {
  await page.goto("/tests/browser/trust-header.html?fixture=answer");

  const header = page.getByRole("status", {
    name: "Trust status: supported released evidence",
  });
  await expect(header).toBeVisible();
  await expect(header).toContainText("Outcome");
  await expect(header).toContainText("ANSWER");
  await expect(header).toContainText("Policy");
  await expect(header).toContainText("ALLOW");
  await expect(header).toContainText("Review");
  await expect(header).toContainText("REVIEWED");
  await expect(header).toContainText("Release");
  await expect(header).toContainText("RELEASED");
  await expect(header).toContainText("Freshness");
  await expect(header).toContainText("CURRENT");
  await expect(header).toContainText("Correction");
  await expect(header).toContainText("CORRECTED");
});

test("compact mode preserves every required text label", async ({ page }) => {
  await page.goto("/tests/browser/trust-header.html?fixture=answer&compact=true");

  const header = page.locator('[data-component="trust-header"]');
  await expect(header).toHaveAttribute("data-layout", "compact");
  for (const label of [
    "Outcome",
    "Policy",
    "Review",
    "Release",
    "Freshness",
    "Correction",
  ]) {
    await expect(header).toContainText(label);
  }
});

test("supported status delegates detail to the Evidence Drawer boundary", async ({
  page,
}) => {
  await page.goto("/tests/browser/trust-header.html?fixture=answer");

  await page.getByRole("button", { name: "Open Evidence Drawer" }).click();
  await expect(page.locator("#drawer-status")).toHaveText("drawer:open:ANSWER");
});

for (const fixture of ["abstain", "deny", "error"] as const) {
  test(`${fixture} renders generic finite-state copy without protected detail`, async ({
    page,
  }) => {
    await page.goto(`/tests/browser/trust-header.html?fixture=${fixture}`);

    const header = page.locator('[data-component="trust-header"]');
    await expect(header).toBeVisible();
    await expect(page.getByRole("button", { name: "Open Evidence Drawer" })).toHaveCount(0);
    await expect(header).not.toContainText("kfm:evidence:");
    await expect(page.locator("body")).not.toContainText(
      "SENSITIVE_DENIAL_CANARY_4d7ec2",
    );
    await expect(page.locator("body")).not.toContainText(
      "INTERNAL_ERROR_CANARY_e6f1af",
    );
    await expect(page.locator("#drawer-status")).toHaveText("drawer:closed");
  });
}

for (const fixture of ["invalid", "missing"] as const) {
  test(`${fixture} renders no Trust Header`, async ({ page }) => {
    const query = fixture === "missing" ? "" : `?fixture=${fixture}`;
    await page.goto(`/tests/browser/trust-header.html${query}`);

    await expect(page.locator('[data-component="trust-header"]')).toHaveCount(0);
    await expect(page.getByRole("button", { name: "Open Evidence Drawer" })).toHaveCount(0);
  });
}
