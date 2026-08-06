import { expect, test } from "playwright/test";

test("pointer and keyboard interaction expose only the released trust snapshot", async ({
  page,
}) => {
  await page.goto("/tests/browser/evidence-tooltip.html?fixture=answer");

  const trigger = page.getByRole("button", { name: "Evidence details" });
  const tooltip = page.getByRole("tooltip", {
    name: "Evidence tooltip: released supporting evidence",
  });

  await expect(trigger).toBeVisible();
  await expect(tooltip).toBeHidden();

  await trigger.hover();
  await expect(tooltip).toBeVisible();
  await expect(tooltip).toContainText("Synthetic streamflow observation");
  await expect(tooltip).toContainText("Policy: ALLOW");
  await expect(tooltip).toContainText("Release: RELEASED");
  await expect(tooltip).toContainText("Freshness: CURRENT");
  await expect(tooltip).toContainText("kfm:evidence:synthetic:flow-001");

  await trigger.focus();
  await page.keyboard.press("Escape");
  await expect(tooltip).toBeHidden();
  await expect(trigger).toHaveAttribute("aria-expanded", "false");
});

test("click delegates to the existing drawer boundary", async ({ page }) => {
  await page.goto("/tests/browser/evidence-tooltip.html?fixture=answer");

  await page.getByRole("button", { name: "Evidence details" }).click();
  await expect(page.locator("#drawer-status")).toHaveText("drawer:open:ANSWER");
});

for (const fixture of ["abstain", "deny", "error"] as const) {
  test(`${fixture} exposes no tooltip affordance or governed payload detail`, async ({
    page,
  }) => {
    await page.goto(`/tests/browser/evidence-tooltip.html?fixture=${fixture}`);

    await expect(page.getByRole("button", { name: "Evidence details" })).toHaveCount(0);
    await expect(page.getByRole("tooltip")).toHaveCount(0);
    await expect(page.locator("body")).not.toContainText(
      "SENSITIVE_DENIAL_CANARY_4d7ec2",
    );
    await expect(page.locator("body")).not.toContainText(
      "INTERNAL_ERROR_CANARY_e6f1af",
    );
    await expect(page.locator("#drawer-status")).toHaveText("drawer:closed");
  });
}
