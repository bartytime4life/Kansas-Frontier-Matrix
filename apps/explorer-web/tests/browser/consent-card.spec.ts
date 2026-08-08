import { expect, test } from "playwright/test";

test("the first-view card is lightweight and keeps viewer choice separate from subject consent", async ({
  page,
}) => {
  await page.goto("/tests/browser/consent-card.html?fixture=answer&reset=1");

  const main = page.getByRole("main", { name: "Consent Card browser fixture" });
  const card = page.getByRole("region", {
    name: "Consent card for Synthetic generalized soil-moisture layer",
  });

  await expect(main).toBeVisible();
  await expect(card).toBeVisible();
  await expect(page.getByRole("dialog")).toHaveCount(0);
  await expect(card).toContainText("ANSWER / CONSENT_CARD_READY");
  await expect(card).toContainText("Viewer acknowledgement is required");
  await expect(card).toContainText("View aggregate values only");
  await expect(card).toContainText("2099-08-08T00:00:00Z");
  await expect(card).toContainText("not applicable to this projection");
  await expect(card).toContainText(
    "does not grant or revoke a subject's consent to inclusion",
  );

  await page.getByRole("button", { name: "Show this layer" }).click();
  await expect(page.locator("[data-layer-visible]")).toHaveText(
    "Layer visible: true",
  );
  await expect(page.locator("[data-event-log]")).toContainText(
    '"kind":"VIEWER_LAYER_OPT_IN"',
  );
  await expect(page.locator("[data-event-log]")).toContainText(
    '"affectsSubjectConsent":false',
  );
  await expect(page.getByRole("button", { name: "Hide this layer" })).toBeVisible();

  await page.goto("/tests/browser/consent-card.html?fixture=answer");
  await expect(page.locator("[data-layer-visible]")).toHaveText(
    "Layer visible: true",
  );
  await expect(page.getByRole("button", { name: "Hide this layer" })).toBeVisible();

  await page.getByRole("button", { name: "Hide this layer" }).click();
  await expect(page.locator("[data-layer-visible]")).toHaveText(
    "Layer visible: false",
  );
  await expect(page.locator("[data-event-log]")).toContainText(
    '"kind":"VIEWER_LAYER_WITHDRAWAL"',
  );
  await expect(page.locator("[data-event-log]")).toContainText(
    '"upstreamNoticeRequired":true',
  );

  await page.goto("/tests/browser/consent-card.html?fixture=answer");
  await expect(page.locator("[data-layer-visible]")).toHaveText(
    "Layer visible: false",
  );
  await expect(page.getByRole("button", { name: "Show this layer" })).toBeVisible();
});

test("obligation detail is emitted to the governed caller without navigation", async ({
  page,
}) => {
  await page.goto("/tests/browser/consent-card.html?fixture=answer&reset=1");

  await page.getByRole("button", { name: "View obligations" }).click();
  await expect(page.locator("[data-event-log]")).toContainText(
    '"kind":"VIEW_OBLIGATIONS"',
  );
  await expect(page.locator("[data-event-log]")).toContainText(
    "kfm://policy/obligation-set/c05e17c05e17c05e17c05e17",
  );
  await expect(page).toHaveURL(/fixture=answer/);
});

for (const negative of [
  {
    fixture: "abstain",
    outcome: "ABSTAIN / CONSENT_UNRESOLVED",
    safeMessage: "Consent details are unresolved. The layer remains hidden.",
    canary: "CONSENT_UNRESOLVED_CANARY_71c9",
  },
  {
    fixture: "deny",
    outcome: "DENY / POLICY_DENIED",
    safeMessage: "Policy does not permit this layer to be shown.",
    canary: "SENSITIVE_DENIAL_CANARY_4aa9",
  },
  {
    fixture: "error",
    outcome: "ERROR / UPSTREAM_ERROR",
    safeMessage:
      "The governed consent service could not complete the request. The layer remains hidden.",
    canary: "INTERNAL_ERROR_CANARY_2f61",
  },
] as const) {
  test(`${negative.fixture} has fixed no-leak copy and no override`, async ({ page }) => {
    await page.goto(
      `/tests/browser/consent-card.html?fixture=${negative.fixture}&reset=1`,
    );

    const card = page.locator('section[data-component="consent-card"]');
    await expect(card).toContainText(negative.outcome);
    await expect(card).toContainText(negative.safeMessage);
    await expect(card).not.toContainText(negative.canary);
    await expect(page.getByRole("button", { name: "Show this layer" })).toHaveCount(0);
    await expect(page.getByRole("button", { name: "Hide this layer" })).toHaveCount(0);
    await expect(page.getByRole("button", { name: "View obligations" })).toHaveCount(0);
    await expect(page.locator("[data-layer-visible]")).toHaveText(
      "Layer visible: false",
    );
  });
}
