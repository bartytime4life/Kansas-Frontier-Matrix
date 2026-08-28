import { expect, test } from "playwright/test";

test("mounts finite renderer-neutral runtime status in the normal map workspace", async ({
  page,
}) => {
  await page.goto("/");

  const host = page.locator(
    '[data-component="explorer-map-runtime-status-host"]',
  );
  await expect(host).toBeVisible();
  await expect(
    host.getByRole("status", { name: "Map runtime status: idle" }),
  ).toContainText("Candidate selectionBLOCKED");

  await page
    .getByRole("button", { name: "Initialize or recover synthetic runtime" })
    .click();
  const ready = host.getByRole("status", {
    name: "Map runtime status: ready",
  });
  await expect(ready).toContainText("StateREADY");
  await expect(ready).toContainText("Candidate selectionELIGIBLE");

  await page
    .getByRole("button", { name: "Mark synthetic runtime stale" })
    .click();
  const stale = host.getByRole("status", {
    name: "Map runtime status: stale",
  });
  await expect(stale).toHaveAttribute("aria-live", "polite");
  await expect(stale).toContainText("ReasonMAP_RUNTIME_STALE");
  await expect(stale).toContainText("Candidate selectionBLOCKED");

  await page
    .getByRole("button", { name: "Withdraw synthetic runtime" })
    .click();
  const withdrawn = host.getByRole("alert", {
    name: "Map runtime status: withdrawn",
  });
  await expect(withdrawn).toHaveAttribute("aria-live", "assertive");
  await expect(withdrawn).toContainText("ReasonMAP_RUNTIME_WITHDRAWN");
  await expect(withdrawn).toContainText("Candidate selectionBLOCKED");

  await page
    .getByRole("button", { name: "Mark synthetic runtime error" })
    .click();
  const error = host.getByRole("alert", {
    name: "Map runtime status: error",
  });
  await expect(error).toHaveAttribute("aria-live", "assertive");
  await expect(error).toContainText("ReasonMAP_RUNTIME_ERROR");
  await expect(error).toContainText("Candidate selectionBLOCKED");

  await page
    .getByRole("button", { name: "Initialize or recover synthetic runtime" })
    .click();
  await expect(
    host.getByRole("status", { name: "Map runtime status: ready" }),
  ).toContainText("Candidate selectionELIGIBLE");

  const rendererGate = page.getByText("Renderer gate").locator("..");
  await expect(rendererGate).toContainText("Package: Present");
  await expect(rendererGate).toContainText("Browser evidence: Pending");
  await expect(rendererGate).toContainText(
    "READY does not establish MapLibre readiness",
  );
});
