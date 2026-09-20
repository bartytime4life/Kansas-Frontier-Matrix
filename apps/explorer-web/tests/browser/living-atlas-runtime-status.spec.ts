import { expect, test } from "playwright/test";

test("keeps held-tool guidance above late readiness chatter in the mounted workspace", async ({
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

});

test("status guard releases held guidance for errors and subsequent recovery", async ({ page }) => {
  // Exercise the real guard in a browser, with one controlled status producer.
  // The mounted map emits READY snapshots independently (including camera updates),
  // so direct DOM fault injection there races legitimate runtime notifications.
  await page.goto("/tests/browser/evidence-drawer.html");
  await page.evaluate(async () => {
    const { mountLivingAtlasRuntimeStatusGuard } = await import(
      "/src/site/living-atlas-runtime-status.ts"
    );
    const root = document.createElement("section");
    root.id = "status-guard-fixture";
    const status = document.createElement("p");
    status.className = "atlas-runtime-state";
    status.setAttribute("role", "status");
    status.textContent = "Renderer READY";
    const button = document.createElement("button");
    button.dataset.atlasAction = "interaction:measure";
    button.textContent = "Measure fixture";
    root.append(status, button);
    document.body.append(root);
    mountLivingAtlasRuntimeStatusGuard(root);
  });
  const root = page.locator("#status-guard-fixture");
  const status = root.getByRole("status");
  await root.getByRole("button", { name: "Measure fixture" }).click();
  await expect(status).toContainText("Measure HELD");
  await status.evaluate((node) => { node.textContent = "Renderer READY"; });
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
