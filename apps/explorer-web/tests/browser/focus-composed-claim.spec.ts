import { expect, test } from "playwright/test";

const fixture = "/tests/browser/focus-composed-claim.html";

test("supported composed claim renders citations and governed Evidence Drawer handoff", async ({
  page,
}) => {
  await page.goto(fixture);
  const trigger = page.getByRole("button", { name: "Ask supported composed claim" });
  await trigger.focus();
  await page.keyboard.press("Enter");

  await expect(page.getByRole("status")).toHaveText(
    "ANSWER / COMPOSED_CLAIM_SUPPORTED",
  );
  const panel = page.getByRole("region", {
    name: "Focus Panel: supported composed claim",
  });
  await expect(panel).toBeVisible();
  await expect(panel).toContainText(
    "The synthetic composed claim is supported by separate static-survey and station-observation fixture evidence.",
  );
  await expect(panel).toContainText("Resolved role: STATIC_SURVEY");
  await expect(panel).toContainText("Resolved role: STATION_OBSERVATION");
  await expect(
    panel.getByRole("link", { name: "Synthetic static soil survey fixture" }),
  ).toBeVisible();
  await expect(panel).toContainText("not release proof");
  await expect(page.getByRole("button", { name: "Close Focus Panel" })).toBeFocused();

  await page.getByRole("button", { name: "Open Evidence Drawer" }).click();
  const drawer = page.getByRole("complementary", {
    name: /Evidence Drawer: supported evidence/,
  });
  await expect(drawer).toBeVisible();
  await expect(drawer).toContainText("kfm:evidence:synthetic:soil-static-001");
  await expect(page.getByRole("button", { name: "Close Evidence Drawer" })).toBeFocused();

  await page.keyboard.press("Escape");
  await expect(drawer).toBeHidden();
  await expect(panel).toBeVisible();
  await expect(page.getByRole("button", { name: "Open Evidence Drawer" })).toBeFocused();

  await page.getByRole("button", { name: "Close Focus Panel" }).focus();
  await page.keyboard.press("Escape");
  await expect(panel).toBeHidden();
  await expect(trigger).toBeFocused();
});

test("qualified composed claim exposes the unavailable optional role", async ({ page }) => {
  await page.goto(fixture);
  await page.getByRole("button", { name: "Ask qualified composed claim" }).click();

  await expect(page.getByRole("status")).toHaveText(
    "ANSWER / COMPOSED_CLAIM_QUALIFIED",
  );
  const panel = page.getByRole("region", {
    name: "Focus Panel: qualified composed claim",
  });
  await expect(panel).toContainText("Unavailable optional role: STATION_OBSERVATION");
  await expect(panel).toContainText("Optional station-observation support is unavailable.");
  await expect(panel.getByRole("link")).toHaveCount(1);
});

test("unresolved required support visibly abstains without diagnostic leakage", async ({
  page,
}) => {
  await page.goto(fixture);
  await page.getByRole("button", { name: "Ask unresolved composed claim" }).click();

  await expect(page.getByRole("status")).toHaveText(
    "ABSTAIN / REQUIRED_DEPENDENCY_UNRESOLVED",
  );
  const panel = page.getByRole("region", { name: "Focus Panel: abstain" });
  await expect(panel).toContainText(
    "The composed claim does not have sufficient released evidence support.",
  );
  await expect(panel).toContainText("Unresolved role: STATIC_SURVEY");
  await expect(panel).not.toContainText("ABSTAIN_PRIVATE_DIAGNOSTIC_CANARY_795a24");
  await expect(panel.getByRole("link")).toHaveCount(0);
});

test("policy denial uses fixed copy and exposes no protected payload detail", async ({ page }) => {
  await page.goto(fixture);
  await page.getByRole("button", { name: "Ask restricted composed claim" }).click();

  await expect(page.getByRole("status")).toHaveText("DENY / POLICY_DENIED");
  const panel = page.getByRole("region", { name: "Focus Panel: deny" });
  await expect(panel).toContainText(
    "Policy does not permit this composed claim to be shown.",
  );
  await expect(panel).not.toContainText("SENSITIVE_FOCUS_DENIAL_CANARY_36e71b");
  await expect(panel.getByRole("link")).toHaveCount(0);
  await expect(panel.locator('ul[aria-label="Focus evidence references"]')).toBeEmpty();
});

test("evidence outside request scope fails closed", async ({ page }) => {
  await page.goto(fixture);
  await page
    .getByRole("button", { name: "Ask composed claim outside evidence scope" })
    .click();

  await expect(page.getByRole("status")).toHaveText(
    "ERROR / EVIDENCE_OUTSIDE_REQUEST",
  );
  const panel = page.getByRole("region", { name: "Focus Panel: error" });
  await expect(panel).toContainText(
    "The governed Focus service could not complete the request.",
  );
  await expect(panel.getByRole("link")).toHaveCount(0);
  await expect(panel).not.toContainText(
    "The synthetic composed claim is supported by separate static-survey and station-observation fixture evidence.",
  );
});

test("resolver failure uses fixed no-leak error copy", async ({ page }) => {
  await page.goto(fixture);
  await page
    .getByRole("button", { name: "Ask composed claim with resolver failure" })
    .click();

  await expect(page.getByRole("status")).toHaveText(
    "ERROR / GOVERNED_RESOLVER_ERROR",
  );
  const panel = page.getByRole("region", { name: "Focus Panel: error" });
  await expect(panel).toContainText(
    "The governed Focus service could not complete the request.",
  );
  await expect(panel).not.toContainText("PRIVATE_BROWSER_FOCUS_RESOLVER_CANARY_c74bd9");
});
