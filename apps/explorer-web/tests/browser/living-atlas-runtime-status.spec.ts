import { expect, test } from "playwright/test";

test("keeps held-tool guidance above late readiness chatter without hiding runtime failures", async ({
  page,
}) => {
  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');
  const status = workspace.locator('.atlas-runtime-state[role="status"]');
  const heldMeasure = workspace.locator(".atlas-interaction-bar").getByRole(
    "button",
    {
      name: "Measure · HELD",
      exact: true,
    },
  );

  await heldMeasure.click();
  await expect(status).toContainText("Measure HELD");
  await expect(status).toContainText("projection, units, uncertainty");

  await status.evaluate((node) => {
    node.textContent = "Renderer READY";
  });
  await expect(status).toContainText("Measure HELD");

  await status.evaluate((node) => {
    node.textContent = "Renderer ERROR · synthetic browser-test failure";
  });
  await expect(status).toContainText("Renderer ERROR");

  await status.evaluate((node) => {
    node.textContent = "Renderer READY";
  });
  await expect(status).toHaveText("Renderer READY");
});
