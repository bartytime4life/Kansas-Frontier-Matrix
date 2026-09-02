import { expect, test } from "playwright/test";

test("TTL expiry hides the overlay and attempts the complete teardown sequence", async ({
  page,
}) => {
  await page.goto("/tests/browser/reveal-session.html?fixture=active");

  const hud = page.getByRole("region", { name: "Reveal session: active" });
  await expect(hud).toBeVisible();
  await expect(hud).toContainText("ANSWER / REVEAL_ACTIVE");
  await expect(page.getByRole("timer")).toHaveText("Time remaining: 00:05");
  await expect(hud).toContainText("Generalized display only");
  await expect(hud).toContainText("Export is disabled");
  await expect(hud).not.toContainText("kfm://key-handle/");
  await expect(page.getByRole("button", { name: "Revoke reveal now" })).toBeVisible();
  await expect(page.locator("[data-layer-visible]")).toHaveText(
    "Overlay visible: true",
  );

  await page.evaluate(() => window.__advanceRevealClock(5_000));

  const expired = page.getByRole("region", { name: "Reveal session: expired" });
  await expect(expired).toContainText("ABSTAIN / REVEAL_EXPIRED");
  await expect(expired).toContainText("Sensitive overlay content is hidden");
  await expect(page.getByRole("timer")).toHaveText("Time remaining: 00:00");
  await expect(page.getByRole("button", { name: "Revoke reveal now" })).toHaveCount(0);
  await expect(page.locator("[data-layer-visible]")).toHaveText(
    "Overlay visible: false",
  );
  await expect(expired).toHaveAttribute("data-teardown-status", "COMPLETE");
  expect(await page.evaluate(() => window.__revealEffects)).toEqual([
    "DISCARD_KEY_MATERIAL:kfm://key-handle/synthetic/reveal-001",
    "REMOVE_OVERLAY",
    "RESTORE_OBFUSCATED_STATE:kfm://layer/synthetic/restricted-generalized-overlay",
    "FINALIZE_AUDIT:TTL_EXPIRED",
  ]);
});

test("viewer revocation uses the same teardown path immediately", async ({ page }) => {
  await page.goto("/tests/browser/reveal-session.html?fixture=active");
  await page.getByRole("button", { name: "Revoke reveal now" }).click();

  const revoked = page.getByRole("region", { name: "Reveal session: revoked" });
  await expect(revoked).toContainText("ABSTAIN / REVEAL_REVOKED");
  await expect(page.locator("[data-layer-visible]")).toHaveText(
    "Overlay visible: false",
  );
  expect(await page.evaluate(() => window.__revealEffects)).toEqual([
    "DISCARD_KEY_MATERIAL:kfm://key-handle/synthetic/reveal-001",
    "REMOVE_OVERLAY",
    "RESTORE_OBFUSCATED_STATE:kfm://layer/synthetic/restricted-generalized-overlay",
    "FINALIZE_AUDIT:VIEWER_REVOKED",
  ]);
});

for (const negative of [
  {
    fixture: "deny",
    outcome: "DENY / POLICY_DENIED",
    message: "Policy does not permit this reveal session.",
  },
  {
    fixture: "invalid",
    outcome: "ERROR / INVALID_PAYLOAD",
    message: "The governed reveal-session response is invalid.",
  },
] as const) {
  test(`${negative.fixture} stays detail-free with no reveal control`, async ({ page }) => {
    await page.goto(`/tests/browser/reveal-session.html?fixture=${negative.fixture}`);

    const hud = page.locator('section[data-component="reveal-session-hud"]');
    await expect(hud).toContainText(negative.outcome);
    await expect(hud).toContainText(negative.message);
    await expect(hud).not.toContainText("SENSITIVE_REVEAL_CANARY_82f7");
    await expect(page.getByRole("button", { name: "Revoke reveal now" })).toHaveCount(0);
    await expect(page.locator("[data-layer-visible]")).toHaveText(
      "Overlay visible: false",
    );
  });
}
