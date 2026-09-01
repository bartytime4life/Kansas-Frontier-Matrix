import { expect, test } from "playwright/test";

const fixture = "/tests/browser/map-evidence-drawer.html";

test("a synthetic map click resolves governed evidence and opens the drawer", async ({
  page,
}) => {
  await page.goto(fixture);
  const selection = page.getByRole("button", {
    name: "Select supported map feature",
  });

  await selection.focus();
  await page.keyboard.press("Enter");

  await expect(page.getByRole("status")).toHaveText("ANSWER / SUPPORTED");
  const drawer = page.getByRole("complementary", {
    name: /Evidence Drawer: supported evidence/,
  });
  await expect(drawer).toBeVisible();
  await expect(drawer).toContainText("kfm:evidence:synthetic:flow-001");
  await expect(drawer.getByRole("link", { name: "Synthetic fixture evidence" })).toBeVisible();
  await expect(page.getByRole("button", { name: "Close Evidence Drawer" })).toBeFocused();
});

test("a feature without governed evidence visibly abstains without citations", async ({
  page,
}) => {
  await page.goto(fixture);
  await page
    .getByRole("button", { name: "Select feature without governed evidence" })
    .click();

  await expect(page.getByRole("status")).toHaveText("ABSTAIN / MISSING_EVIDENCE");
  const drawer = page.getByRole("complementary", {
    name: /Evidence Drawer: abstain/,
  });
  await expect(drawer).toContainText("ABSTAIN / MISSING_EVIDENCE");
  await expect(drawer).toContainText("Required evidence is not available.");
  await expect(drawer.getByRole("link")).toHaveCount(0);
});

test("a policy-restricted feature shows fixed denial copy without sensitive leakage", async ({
  page,
}) => {
  await page.goto(fixture);
  await page
    .getByRole("button", { name: "Select policy-restricted map feature" })
    .click();

  await expect(page.getByRole("status")).toHaveText(
    "DENY / SENSITIVE_DETAIL_RESTRICTED",
  );
  const drawer = page.locator('aside[data-component="evidence-drawer"]');
  await expect(drawer).toContainText("Sensitive detail is restricted.");
  await expect(drawer).not.toContainText("SENSITIVE_DENIAL_CANARY_4d7ec2");
  await expect(drawer.getByRole("link")).toHaveCount(0);
});

test("stale evidence visibly abstains with temporal trust state", async ({ page }) => {
  await page.goto(fixture);
  await page
    .getByRole("button", { name: "Select stale map evidence" })
    .click();

  await expect(page.getByRole("status")).toHaveText(
    "ABSTAIN / STALE_EVIDENCE",
  );
  const drawer = page.locator('aside[data-component="evidence-drawer"]');
  await expect(drawer).toContainText("Available evidence is stale for this request.");
  await expect(drawer).toContainText("Freshness: STALE");
  await expect(drawer).toContainText("kfm:evidence:synthetic:stale-001");
  await expect(drawer).not.toContainText(
    "STALE_SUMMARY_MUST_NOT_RENDER_AS_A_CLAIM",
  );
  await expect(drawer.getByRole("link")).toHaveCount(0);
});

test("stale evidence outside the clicked selection fails closed without leaking", async ({
  page,
}) => {
  await page.goto(fixture);
  await page
    .getByRole("button", { name: "Select feature with mismatched stale evidence" })
    .click();

  await expect(page.getByRole("status")).toHaveText(
    "ERROR / DRAWER_EVIDENCE_OUTSIDE_SELECTION",
  );
  const drawer = page.locator('aside[data-component="evidence-drawer"]');
  await expect(drawer).toContainText("ERROR / UPSTREAM_ERROR");
  await expect(drawer).not.toContainText("kfm:evidence:synthetic:stale-001");
  await expect(drawer).not.toContainText(
    "STALE_SUMMARY_MUST_NOT_RENDER_AS_A_CLAIM",
  );
  await expect(drawer.getByRole("link")).toHaveCount(0);
});

test("superseded evidence remains visible only as audit history", async ({ page }) => {
  await page.goto(fixture);
  await page
    .getByRole("button", { name: "Select superseded evidence history" })
    .click();

  await expect(page.getByRole("status")).toHaveText(
    "ABSTAIN / SUPERSEDED_EVIDENCE",
  );
  const drawer = page.locator('aside[data-component="evidence-drawer"]');
  await expect(drawer).toContainText(
    "The available evidence is superseded and is shown only as history.",
  );
  await expect(drawer).toContainText(
    "kfm:evidence:synthetic:superseded-001",
  );
  await expect(drawer.getByRole("link")).toHaveCount(0);
});

test("evidence history outside the clicked selection fails closed without leaking", async ({
  page,
}) => {
  await page.goto(fixture);
  await page
    .getByRole("button", { name: "Select feature with mismatched evidence history" })
    .click();

  await expect(page.getByRole("status")).toHaveText(
    "ERROR / DRAWER_EVIDENCE_OUTSIDE_SELECTION",
  );
  const drawer = page.locator('aside[data-component="evidence-drawer"]');
  await expect(drawer).toContainText("ERROR / UPSTREAM_ERROR");
  await expect(drawer).not.toContainText(
    "kfm:evidence:synthetic:superseded-001",
  );
  await expect(drawer.getByRole("link")).toHaveCount(0);
});

test("evidence outside the clicked selection fails closed", async ({ page }) => {
  await page.goto(fixture);
  await page
    .getByRole("button", { name: "Select feature with mismatched evidence" })
    .click();

  await expect(page.getByRole("status")).toHaveText(
    "ERROR / DRAWER_EVIDENCE_OUTSIDE_SELECTION",
  );
  const drawer = page.locator('aside[data-component="evidence-drawer"]');
  await expect(drawer).toContainText("ERROR / UPSTREAM_ERROR");
  await expect(drawer.getByRole("link")).toHaveCount(0);
});

test("resolver failures use fixed no-leak error copy", async ({ page }) => {
  await page.goto(fixture);
  await page
    .getByRole("button", { name: "Select feature with resolver failure" })
    .click();

  await expect(page.getByRole("status")).toHaveText(
    "ERROR / GOVERNED_RESOLVER_ERROR",
  );
  const drawer = page.locator('aside[data-component="evidence-drawer"]');
  await expect(drawer).toContainText(
    "The governed evidence service could not complete the request.",
  );
  await expect(drawer).not.toContainText(
    "PRIVATE_BROWSER_RESOLVER_CANARY_0b10d7",
  );
});
