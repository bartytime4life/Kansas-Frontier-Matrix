import { expect, test } from "playwright/test";

test("keyboard opening enters the drawer and Escape restores focus", async ({
  page,
}) => {
  await page.goto("/tests/browser/evidence-drawer.html?fixture=answer");

  const main = page.getByRole("main", {
    name: "Evidence Drawer browser fixture",
  });
  const trigger = page.getByRole("button", { name: "Open Evidence Drawer" });
  const drawer = page.locator('aside[data-component="evidence-drawer"]');
  const close = page.getByRole("button", { name: "Close Evidence Drawer" });

  await expect(main).toBeVisible();
  await expect(drawer).toBeHidden();
  await trigger.focus();
  await page.keyboard.press("Enter");

  await expect(trigger).toHaveAttribute("aria-expanded", "true");
  await expect(
    page.getByRole("complementary", {
      name: /Evidence Drawer: supported evidence/,
    }),
  ).toBeVisible();
  await expect(close).toBeFocused();

  await page.keyboard.press("Escape");
  await expect(drawer).toBeHidden();
  await expect(trigger).toHaveAttribute("aria-expanded", "false");
  await expect(trigger).toBeFocused();
});

test("fixture-driven ANSWER rendering preserves evidence, citations, and correction history", async ({
  page,
}) => {
  await page.goto("/tests/browser/evidence-drawer.html?fixture=answer");
  await page.getByRole("button", { name: "Open Evidence Drawer" }).click();

  const drawer = page.getByRole("complementary", {
    name: /Evidence Drawer: supported evidence/,
  });
  await expect(drawer).toContainText("ANSWER / SUPPORTED");
  await expect(drawer).toContainText("Synthetic streamflow observation");
  await expect(drawer).toContainText("Policy: ALLOW");
  await expect(drawer.getByRole("list", { name: "Evidence history" })).toContainText(
    "Correction lineage",
  );
  await expect(
    drawer.getByRole("link", { name: "Synthetic fixture evidence" }),
  ).toHaveAttribute(
    "href",
    "https://example.invalid/kfm/evidence/flow-001",
  );
});

for (const negative of [
  {
    fixture: "deny",
    outcome: "DENY / SENSITIVE_DETAIL_RESTRICTED",
    safeMessage: "Sensitive detail is restricted.",
    canary: "SENSITIVE_DENIAL_CANARY_4d7ec2",
  },
  {
    fixture: "error",
    outcome: "ERROR / UPSTREAM_ERROR",
    safeMessage: "The governed evidence service could not complete the request.",
    canary: "INTERNAL_ERROR_CANARY_e6f1af",
  },
] as const) {
  test(`${negative.fixture} rendering uses fixed no-leak copy`, async ({ page }) => {
    await page.goto(
      `/tests/browser/evidence-drawer.html?fixture=${negative.fixture}`,
    );
    await page.getByRole("button", { name: "Open Evidence Drawer" }).click();

    const drawer = page.locator('aside[data-component="evidence-drawer"]');
    await expect(drawer).toContainText(negative.outcome);
    await expect(drawer).toContainText(negative.safeMessage);
    await expect(drawer).not.toContainText(negative.canary);
    await expect(drawer.getByRole("link")).toHaveCount(0);
    await expect(drawer.getByRole("list", { name: "Evidence history" })).toBeEmpty();
  });
}
