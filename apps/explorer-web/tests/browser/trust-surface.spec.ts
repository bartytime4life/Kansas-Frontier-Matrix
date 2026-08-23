import { expect, test } from "playwright/test";

test("presents shared accessible trust states without exposing privileged controls", async ({
  page,
}) => {
  await page.goto("/");

  const surface = page.locator('[data-component="public-trust-surface"]');
  await expect(surface).toHaveAttribute(
    "data-profile",
    "kfm.explorer.public-trust-surface.v1",
  );

  const cases = surface.getByRole("group", {
    name: "Trust-state fixture cases",
  });
  const buttons = cases.getByRole("button");
  await expect(buttons).toHaveCount(6);
  await expect(buttons).toHaveText([
    "Supported",
    "Unresolved",
    "Restricted",
    "Stale",
    "Error",
    "Loading",
  ]);
  await expect(
    surface.getByRole("button", { name: /admin|approve|publish/i }),
  ).toHaveCount(0);

  const summary = surface.locator('[data-component="trust-state-summary"]');
  await expect(summary).toHaveAttribute("data-outcome", "ANSWER");
  await expect(summary.locator("dt")).toHaveText([
    "Outcome",
    "Evidence",
    "Freshness",
    "Sensitivity",
    "Release",
    "Correction",
  ]);
  await expect(surface.locator('[data-component="trust-header"]')).toHaveAttribute(
    "data-state",
    "SUPPORTED",
  );
  await expect(
    surface.locator('[data-component="accessible-time-scrubber"]'),
  ).toBeVisible();
  await expect(surface.locator('[data-component="citation-pill"]')).toBeVisible();

  await cases.getByRole("button", { name: "Restricted" }).click();
  await expect(summary).toHaveAttribute("data-outcome", "DENY");
  await expect(
    summary.locator('[data-trust-state-field="sensitivity"] dd'),
  ).toHaveText("RESTRICTED");
  await expect(surface.locator('[data-component="trust-header"]')).toHaveAttribute(
    "data-state",
    "DENY",
  );
  await expect(
    surface.locator('[data-component="denial-reason-explorer"]'),
  ).toHaveAttribute("data-outcome", "DENY");
  await expect(surface.locator('[data-component="citation-pill"]')).toHaveCount(0);
  await expect(
    surface.locator('[data-component="accessible-time-scrubber"]'),
  ).toHaveCount(0);

  await cases.getByRole("button", { name: "Error" }).click();
  await expect(summary).toHaveAttribute("data-outcome", "ERROR");
  await expect(summary).toHaveAttribute("role", "alert");
  await expect(surface).not.toContainText(/stack|token|credential|private prompt/i);

  await cases.getByRole("button", { name: "Loading" }).click();
  await expect(summary).toHaveAttribute("data-outcome", "LOADING");
  await expect(summary).toHaveAttribute("aria-busy", "true");
  await expect(surface.locator('[data-component="trust-header"]')).toHaveCount(0);
  await expect(surface.locator('[data-component="evidence-drawer"]')).toHaveCount(0);
  await expect(surface).toContainText(
    "Loading is a transient UI condition. It does not imply evidence, review, release, or authority.",
  );
});
