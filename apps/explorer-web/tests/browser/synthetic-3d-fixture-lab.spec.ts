import { expect, test } from "playwright/test";

test("activates the inline-only synthetic MapLibre 3D lab and tears it down", async ({
  page,
}) => {
  const externalRequests: string[] = [];
  page.on("request", (request) => {
    const url = new URL(request.url());
    if (
      (url.protocol === "http:" || url.protocol === "https:") &&
      url.hostname !== "127.0.0.1"
    ) {
      externalRequests.push(request.url());
    }
  });

  await page.goto("/");

  const lab = page.locator("#kfm-synthetic-maplibre-3d-lab");
  await expect(lab).toBeAttached();
  await expect(lab).not.toHaveAttribute("open", "");
  await expect(lab).toHaveAttribute("data-activation", "disabled");
  await expect(lab.locator("canvas")).toHaveCount(0);

  await lab.locator("summary").press("Enter");
  await expect(lab).toHaveAttribute("open", "");

  await page
    .getByRole("button", { name: "Activate synthetic 3D lab" })
    .press("Enter");

  await expect(lab).toHaveAttribute("data-activation", "active");
  await expect(
    page.locator("#kfm-synthetic-maplibre-3d-root canvas.maplibregl-canvas"),
  ).toBeVisible();
  await expect(
    page.getByText(
      "Synthetic MapLibre 3D is active. All geometry and evidence references are inline fixture data.",
    ),
  ).toBeVisible();
  expect(externalRequests).toEqual([]);

  await page.getByRole("button", { name: "Mercator", exact: true }).press("Enter");
  await expect(lab.locator(".synthetic-3d-lab__snapshot")).toContainText(
    "mercator",
  );

  const verticalScale = page.locator("#kfm-synthetic-3d-verticalScale");
  await verticalScale.evaluate((node) => {
    const input = node as HTMLInputElement;
    input.value = "1.75";
    input.dispatchEvent(new Event("input", { bubbles: true }));
  });
  await expect(lab.locator(".synthetic-3d-lab__snapshot")).toContainText(
    "vertical 1.75×",
  );

  await page
    .getByRole("button", { name: "1. Western context tower" })
    .press("Enter");
  await expect(
    page.getByRole("heading", { name: "Western context tower" }),
  ).toBeFocused();
  await expect(
    lab.getByText("kfm:evidence:synthetic:3d:western-context", { exact: true }),
  ).toBeVisible();
  await expect(lab.locator(".synthetic-3d-lab__snapshot")).toContainText(
    "synthetic:western-context",
  );

  const map = page.locator("#kfm-synthetic-maplibre-3d-root");
  await map.focus();
  await map.press("g");
  await expect(lab.locator(".synthetic-3d-lab__snapshot")).toContainText(
    "globe",
  );
  await map.press("Escape");
  await expect(lab.locator(".synthetic-3d-lab__snapshot")).toContainText(
    "no selection",
  );

  await page
    .getByRole("button", { name: "Deactivate and tear down" })
    .press("Enter");
  await expect(lab).toHaveAttribute("data-activation", "disabled");
  await expect(lab.locator("canvas")).toHaveCount(0);
  await expect(lab.locator(".synthetic-3d-lab__snapshot")).toContainText(
    "INACTIVE",
  );
  expect(externalRequests).toEqual([]);
});

test("keeps the Explorer available when WebGL2 is unavailable", async ({
  page,
}) => {
  await page.addInitScript(() => {
    const getContext = HTMLCanvasElement.prototype.getContext;
    HTMLCanvasElement.prototype.getContext = function (
      contextId: string,
      ...args: unknown[]
    ) {
      if (contextId === "webgl2") return null;
      return Reflect.apply(getContext, this, [contextId, ...args]);
    } as typeof getContext;
  });

  await page.goto("/");

  const lab = page.locator("#kfm-synthetic-maplibre-3d-lab");
  await lab.locator("summary").click();
  await page.getByRole("button", { name: "Activate synthetic 3D lab" }).click();

  await expect(lab).toHaveAttribute("data-activation", "disabled");
  await expect(lab.locator(".synthetic-3d-lab__status")).toContainText(
    "Fail-closed fallback",
  );
  await expect(lab.locator("canvas")).toHaveCount(0);
  await expect(page.getByRole("heading", { name: /Explore Kansas knowledge/i })).toBeVisible();
});
