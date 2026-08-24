import { expect, test } from "playwright/test";

test("mounts the public workspace registry over the compatible anchor navigation", async ({
  page,
}) => {
  await page.goto("/");

  const navigation = page.getByRole("navigation", {
    name: "Explorer workspaces",
  });
  await expect(navigation).toHaveAttribute(
    "data-workspace-navigation-profile",
    "kfm.explorer.public-workspace-navigation.v1",
  );

  const links = navigation.getByRole("link");
  await expect(links).toHaveCount(4);
  await expect(links).toHaveText(["Map", "Knowledge", "Features", "Trust"]);
  await expect(links.nth(0)).toHaveAttribute("href", "#map");
  await expect(links.nth(1)).toHaveAttribute("href", "#knowledge");
  await expect(links.nth(2)).toHaveAttribute("href", "#features");
  await expect(links.nth(3)).toHaveAttribute("href", "#trust");
  await expect(navigation.getByRole("link", { name: /admin|review/i })).toHaveCount(0);

  await navigation.getByRole("link", { name: "Trust" }).click();
  await expect(page).toHaveURL(/#trust$/);
  await expect(page.locator("#trust")).toBeVisible();
});

test("runs one bounded governed Focus request inside the Explore workspace", async ({
  page,
}) => {
  await page.goto("/");

  const workspace = page.locator('[data-component="focus-mode-workspace"]');
  await expect(workspace).toBeVisible();
  await expect(
    workspace.getByRole("button", { name: "Run bounded governed Focus request" }),
  ).toHaveCount(1);
  await expect(
    workspace.getByRole("button", { name: "Run corrected-evidence Focus request" }),
  ).toHaveCount(1);
  await expect(workspace).toContainText(
    "Only active endorsed synthetic support crosses the answer boundary",
  );

  await workspace
    .getByRole("button", { name: "Run bounded governed Focus request" })
    .click();

  await expect(workspace.getByRole("status")).toHaveText(
    "ANSWER / COMPOSED_CLAIM_QUALIFIED",
  );
  const panel = workspace.getByRole("region", {
    name: "Focus Panel: qualified composed claim",
  });
  await expect(panel).toBeVisible();
  await expect(
    panel.locator('ul[aria-label="Active Focus evidence scope"]'),
  ).toContainText("kfm:evidence:synthetic:endorsed-soil-summary-3373");
  await expect(panel.locator('[data-component="focus-policy-result"]')).toHaveText(
    "Policy result: ALLOW",
  );
  await expect(
    panel.getByRole("link", { name: "Endorsed synthetic soil summary" }),
  ).toBeVisible();
  await expect(panel).toContainText("Resolved role: ENDORSED_SUMMARY");
  await expect(panel).toContainText(
    "Unavailable optional role: RESTRICTED_CONTEXT",
  );
  await expect(panel).toContainText(
    "One synthetic restricted-context role is withheld by policy; no protected detail is exposed.",
  );
  await expect(panel).toContainText("not release proof");
  await expect(panel).not.toContainText("RAW_GOVERNED_CONTEXT_CANARY_3373");
  await expect(panel).not.toContainText("raw_governed_context");
  await expect(workspace).toContainText(
    "These fixtures do not activate a source, execute a model, authenticate release, or publish an answer.",
  );
});

test("keeps superseded Focus evidence in visible correction history only", async ({
  page,
}) => {
  await page.goto("/");

  const workspace = page.locator('[data-component="focus-mode-workspace"]');
  await workspace
    .getByRole("button", { name: "Run corrected-evidence Focus request" })
    .click();

  await expect(workspace.getByRole("status")).toHaveText(
    "ANSWER / COMPOSED_CLAIM_SUPPORTED",
  );
  const panel = workspace.getByRole("region", {
    name: "Focus Panel: supported composed claim",
  });
  const activeEvidence = panel.locator(
    'ul[aria-label="Focus evidence references"]',
  );
  await expect(activeEvidence).toContainText(
    "kfm:evidence:synthetic:corrected-soil-summary-001",
  );
  await expect(activeEvidence).not.toContainText(
    "kfm:evidence:synthetic:superseded-soil-summary-001",
  );
  await expect(
    panel.getByRole("link", { name: "Corrected synthetic soil summary" }),
  ).toBeVisible();

  await panel.getByRole("button", { name: "Open Evidence Drawer" }).click();
  const drawer = panel.getByRole("complementary", {
    name: "Evidence Drawer: supported evidence",
  });
  await expect(drawer).toBeVisible();
  await expect(
    drawer.locator('ul[aria-label="Evidence trust state"]'),
  ).toContainText("Correction: CORRECTED");
  await expect(
    drawer.locator('ul[aria-label="Evidence references"]'),
  ).toContainText("kfm:evidence:synthetic:corrected-soil-summary-001");
  await expect(
    drawer.locator('ul[aria-label="Evidence references"]'),
  ).not.toContainText("kfm:evidence:synthetic:superseded-soil-summary-001");
  await expect(
    drawer.locator('ul[aria-label="Evidence history"]'),
  ).toContainText(
    "Correction lineage: kfm:evidence:synthetic:superseded-soil-summary-001 → kfm:evidence:synthetic:corrected-soil-summary-001",
  );
});
