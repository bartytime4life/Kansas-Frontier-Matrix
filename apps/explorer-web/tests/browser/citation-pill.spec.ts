import { expect, test } from "playwright/test";

const EXPECTED_LINK =
  "kfm:evidence:synthetic:flow-001?t=1850-06-01T00%3A00%3A00Z&view=focus";

test("one click reveals the governed EvidenceRef and timestamped deep link", async ({
  page,
}) => {
  await page.goto("/tests/browser/citation-pill.html?fixture=answer");

  const toggle = page.getByRole("button", {
    name: "Evidence: verified evidence for Synthetic streamflow observation",
  });
  const region = page.getByRole("region", {
    name: "Evidence citation for Synthetic streamflow observation",
  });

  await expect(toggle).toBeVisible();
  await expect(toggle).toContainText("Evidence");
  await expect(toggle).toContainText("VERIFIED");
  await expect(toggle).toHaveAttribute("aria-expanded", "false");
  await expect(region).toBeHidden();

  await toggle.click();

  await expect(toggle).toHaveAttribute("aria-expanded", "true");
  await expect(region).toBeVisible();
  await expect(region).toContainText("Synthetic streamflow observation");
  await expect(region).toContainText("kfm:evidence:synthetic:flow-001");
  await expect(region).toContainText(EXPECTED_LINK);
});

test("copy emits the exact governed link and deterministic live feedback", async ({ page }) => {
  await page.goto("/tests/browser/citation-pill.html?fixture=answer");

  await page.getByRole("button", {
    name: "Evidence: verified evidence for Synthetic streamflow observation",
  }).click();
  await page.getByRole("button", {
    name: "Copy evidence link for Synthetic streamflow observation at 1850-06-01T00:00:00Z",
  }).click();

  await expect(page.locator("#copy-probe")).toHaveText(EXPECTED_LINK);
  await expect(page.getByRole("status")).toHaveText("Link copied.");
});

test("Escape collapses the inline region and restores focus", async ({ page }) => {
  await page.goto("/tests/browser/citation-pill.html?fixture=answer");

  const toggle = page.getByRole("button", {
    name: "Evidence: verified evidence for Synthetic streamflow observation",
  });
  const region = page.getByRole("region", {
    name: "Evidence citation for Synthetic streamflow observation",
  });

  await toggle.click();
  await page.getByRole("button", {
    name: "Copy evidence link for Synthetic streamflow observation at 1850-06-01T00:00:00Z",
  }).focus();
  await page.keyboard.press("Escape");

  await expect(region).toBeHidden();
  await expect(toggle).toHaveAttribute("aria-expanded", "false");
  await expect(toggle).toBeFocused();
});

for (const fixture of ["abstain", "deny", "error"] as const) {
  test(`${fixture} exposes no citation affordance or protected payload detail`, async ({
    page,
  }) => {
    await page.goto(`/tests/browser/citation-pill.html?fixture=${fixture}`);

    await expect(page.locator('[data-component="citation-pill"]')).toHaveCount(0);
    await expect(page.getByRole("button", { name: /verified evidence/i })).toHaveCount(0);
    await expect(page.getByRole("region", { name: /Evidence citation/i })).toHaveCount(0);
    await expect(page.locator("body")).not.toContainText(
      "SENSITIVE_DENIAL_CANARY_4d7ec2",
    );
    await expect(page.locator("body")).not.toContainText(
      "INTERNAL_ERROR_CANARY_e6f1af",
    );
    await expect(page.locator("#copy-probe")).toHaveText("not-copied");
  });
}
