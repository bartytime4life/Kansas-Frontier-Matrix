import { expect, test } from "playwright/test";

const fixture = "/tests/browser/maplibre-vite-adapter.html";

test("boots the package-owned v6 adapter with local Vite assets and disposes it", async ({
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

  await page.goto(fixture);

  const status = page.getByRole("status");
  await expect(status).toHaveAttribute("data-state", "READY");
  await expect(page.locator("body")).toHaveAttribute(
    "data-initialization",
    "resolved",
  );

  const mapRoot = page.locator("#maplibre-vite-map");
  await expect(mapRoot).toHaveClass(/maplibregl-map/);
  await expect(mapRoot.locator("canvas")).toBeVisible();
  await expect(mapRoot).toHaveCSS("position", "relative");
  expect(externalRequests).toEqual([]);

  await page.getByRole("button", { name: "Dispose runtime" }).press("Enter");
  await expect(status).toHaveAttribute("data-state", "DISPOSED");
  await expect(mapRoot.locator("canvas")).toHaveCount(0);
});

test("resizes a map that starts in a hidden container when revealed", async ({
  page,
}) => {
  await page.goto(`${fixture}?hidden=1`);

  const status = page.getByRole("status");
  await expect(status).toHaveAttribute("data-state", "READY");

  const mapRoot = page.locator("#maplibre-vite-map");
  await expect(mapRoot).toHaveCSS("display", "none");

  await page.getByRole("button", { name: "Reveal map" }).click();
  await expect(mapRoot).toHaveCSS("display", "block");
  await expect(mapRoot.locator("canvas")).toBeVisible();

  const canvasSize = await mapRoot.locator("canvas").evaluate((canvas) => ({
    width: canvas.width,
    height: canvas.height,
  }));
  expect(canvasSize.width).toBeGreaterThan(0);
  expect(canvasSize.height).toBeGreaterThan(0);
});

test("fails closed when WebGL2 initialization is unavailable", async ({ page }) => {
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

  await page.goto(fixture);

  const status = page.getByRole("status");
  await expect(status).toHaveAttribute("data-state", "ERROR");
  await expect(status).toHaveAttribute("data-reason", "MAP_RUNTIME_ERROR");
  await expect(page.locator("body")).toHaveAttribute(
    "data-initialization",
    "rejected",
  );
  await expect(page.locator("#maplibre-vite-map canvas")).toHaveCount(0);
});
