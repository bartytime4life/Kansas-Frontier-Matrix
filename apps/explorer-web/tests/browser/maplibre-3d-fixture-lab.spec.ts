import { expect, test } from "playwright/test";

test("keeps the synthetic MapLibre 3D lab opt-in, finite, and same-origin", async ({
  page,
}) => {
  const crossOriginRequests: string[] = [];
  page.on("request", (request) => {
    const url = request.url();
    if (!url.startsWith("http://") && !url.startsWith("https://")) return;
    if (new URL(url).origin !== "http://127.0.0.1:4173") {
      crossOriginRequests.push(url);
    }
  });

  await page.goto("/");
  await expect(
    page.locator('[data-component="maplibre-3d-fixture-lab"]'),
  ).toHaveCount(0);

  await page.goto("/?kfm-maplibre-3d-fixture=1");
  const lab = page.locator(
    '[data-component="maplibre-3d-fixture-lab"]',
  );
  await expect(lab).toBeVisible();
  await expect(lab.getByRole("heading", {
    name: "Synthetic MapLibre 3D fixture lab",
  })).toBeVisible();

  const status = lab.locator(".maplibre-3d-fixture__status");
  await expect(status).toHaveAttribute("data-state", /^(READY|ERROR)$/, {
    timeout: 15_000,
  });

  const state = await status.getAttribute("data-state");
  if (state === "READY") {
    await lab.getByRole("button", { name: "Globe" }).click();
    await expect(
      lab.getByRole("button", { name: "Globe" }),
    ).toHaveAttribute("aria-pressed", "true");

    await lab
      .getByRole("button", { name: "Synthetic central Kansas prism" })
      .click();
    await expect(
      lab.getByLabel("Synthetic evidence handoff"),
    ).toContainText(
      "kfm:evidence:synthetic:maplibre-3d:central",
    );
    await expect(
      lab.getByLabel("Synthetic evidence handoff"),
    ).toContainText("does not identify released evidence");
  } else {
    await expect(status).toContainText("failed closed");
    await expect(
      lab.getByRole("button", { name: "Globe" }),
    ).toBeDisabled();
    await expect(
      lab.getByText("MapLibre is unavailable in this browser context."),
    ).toBeVisible();
  }

  expect(crossOriginRequests).toEqual([]);
});
