import { expect, test } from "playwright/test";

const fixture = "/tests/browser/map-runtime-trust-status.html";

test("shows idle and ready runtime state without color-only meaning", async ({
  page,
}) => {
  await page.goto(fixture);

  const idle = page.getByRole("status", { name: "Map runtime status: idle" });
  await expect(idle).toBeVisible();
  await expect(idle).toContainText("StateIDLE");
  await expect(idle).toContainText("ReasonNONE");
  await expect(idle).toContainText("Candidate selectionBLOCKED");

  await page.getByRole("button", { name: "Initialize runtime" }).click();
  const ready = page.getByRole("status", { name: "Map runtime status: ready" });
  await expect(ready).toContainText("StateREADY");
  await expect(ready).toContainText("Candidate selectionELIGIBLE");
});

test("shows stale state as a fixed, polite, non-authoritative status", async ({
  page,
}) => {
  await page.goto(fixture);
  await page.getByRole("button", { name: "Initialize runtime" }).click();
  await page.getByRole("button", { name: "Mark runtime stale" }).click();

  const stale = page.getByRole("status", { name: "Map runtime status: stale" });
  await expect(stale).toHaveAttribute("aria-live", "polite");
  await expect(stale).toContainText("MAP_RUNTIME_STALE");
  await expect(stale).toContainText("Candidate selectionBLOCKED");
  await expect(stale).not.toContainText("Policy");
  await expect(stale).not.toContainText("Release");
  await expect(stale).not.toContainText("Sensitivity");
});

for (const scenario of [
  ["Withdraw runtime", "withdrawn", "MAP_RUNTIME_WITHDRAWN"],
  ["Mark runtime error", "error", "MAP_RUNTIME_ERROR"],
] as const) {
  test(`${scenario[1]} is visible as an assertive no-leak alert`, async ({ page }) => {
    await page.goto(fixture);
    await page.getByRole("button", { name: "Initialize runtime" }).click();
    await page.getByRole("button", { name: scenario[0] }).click();

    const alert = page.getByRole("alert", {
      name: `Map runtime status: ${scenario[1]}`,
    });
    await expect(alert).toHaveAttribute("aria-live", "assertive");
    await expect(alert).toContainText(scenario[2]);
    await expect(alert).toContainText("Candidate selectionBLOCKED");
    await expect(page.locator("body")).not.toContainText(
      "PRIVATE_RUNTIME_DIAGNOSTIC_CANARY_3bc6f0",
    );
  });
}

test("disposal remains visible and permanently blocks selection", async ({ page }) => {
  await page.goto(fixture);
  await page.getByRole("button", { name: "Initialize runtime" }).click();
  await page.getByRole("button", { name: "Dispose runtime" }).click();

  const disposed = page.getByRole("status", {
    name: "Map runtime status: disposed",
  });
  await expect(disposed).toContainText("MAP_RUNTIME_DISPOSED");
  await expect(disposed).toContainText("Candidate selectionBLOCKED");
});
