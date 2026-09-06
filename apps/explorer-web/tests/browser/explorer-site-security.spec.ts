import { expect, test } from "playwright/test";

test("preserves the illustrative map semantics after DOM-safe construction", async ({
  page,
}) => {
  await page.goto("/");

  const artwork = page.locator("figure.map-artwork");
  await expect(artwork).toBeVisible();

  const svg = artwork.locator("svg");
  await expect(svg).toHaveAttribute("role", "img");
  await expect(svg).toHaveAttribute(
    "aria-labelledby",
    "map-art-title map-art-desc",
  );
  await expect(artwork.locator("title")).toHaveText(
    "Illustrative Kansas evidence map",
  );
  await expect(artwork.locator("desc")).toHaveText(
    "A decorative Kansas outline with survey grid, river paths, and evidence markers.",
  );
  await expect(artwork.locator("text").nth(0)).toHaveText(
    "SYNTHETIC MAP STAGE",
  );
  await expect(artwork.locator("text").nth(1)).toHaveText(
    "Rendered features scope requests — not claims",
  );
  await expect(artwork.locator("path.map-shape")).toHaveCount(1);
  await expect(artwork.locator("path.map-grid")).toHaveCount(1);
  await expect(artwork.locator("g.marker")).toHaveCount(2);
  await expect(artwork.locator("script, iframe, foreignObject")).toHaveCount(0);

  const hasInlineEventHandler = await artwork.evaluate((root) =>
    Array.from(root.querySelectorAll("*")).some((element) =>
      Array.from(element.attributes).some((attribute) =>
        attribute.name.toLowerCase().startsWith("on"),
      ),
    ),
  );
  expect(hasInlineEventHandler).toBe(false);
});
