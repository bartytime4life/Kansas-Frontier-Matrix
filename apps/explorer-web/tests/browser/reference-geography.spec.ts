import { expect, test } from "playwright/test";

test("exposes the byte-verified county reference while keeping the map held", async ({
  page,
}) => {
  const externalRequests: string[] = [];
  page.on("request", (request) => {
    const url = new URL(request.url());
    if (!url.hostname.match(/^(127\.0\.0\.1|localhost)$/)) {
      externalRequests.push(request.url());
    }
  });

  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');

  await workspace.getByRole("button", { name: "Places" }).click();
  const candidate = workspace
    .locator('[data-rail-panel="places"]')
    .locator("[data-reference-geography]", {
      hasText: "2025 Cartographic Boundary Counties",
    });
  await expect(candidate).toContainText("VERIFIED_CANDIDATE_HOLD");
  await expect(candidate).toContainText("105 Kansas counties");
  await candidate.getByRole("button", { name: "Inspect verified candidate" }).click();

  const drawer = workspace.getByRole("complementary", {
    name: "Evidence Drawer",
  });
  await expect(drawer).toContainText("HOLD · NOT RELEASED");
  await expect(drawer).toContainText("105 unique Kansas GEOIDs");
  await expect(drawer).toContainText(
    "aa976c00b181939755d0da757f4c7c2dc0103c3b3b4530fb2a91c2bb62fc777c",
  );
  await expect(drawer.getByRole("link", { name: "SOURCE DESCRIPTOR" })).toHaveAttribute(
    "href",
    /census_cartographic_boundary_counties_2025_500k\.source\.json$/,
  );
  await expect(drawer.getByRole("link", { name: "OFFLINE VALIDATOR" })).toHaveAttribute(
    "href",
    /census_cartographic_boundary_counties\.py$/,
  );
  await expect(workspace.locator(".atlas-map-notice")).toContainText(
    "Generalized synthetic geometry",
  );
  expect(externalRequests).toEqual([]);
});

test("lists the same candidate in the Source Observatory", async ({ page }) => {
  await page.goto("/");
  const workspace = page.locator('[data-component="living-atlas-workspace"]');

  await workspace.getByRole("button", { name: "Sources" }).click();
  const candidate = workspace
    .locator('[data-rail-panel="sources"]')
    .locator("[data-reference-geography]", {
      hasText: "2025 Cartographic Boundary Counties",
    });
  await expect(candidate).toContainText("VERIFIED_CANDIDATE_HOLD");
  await expect(candidate.getByRole("link", { name: "Official Census archive" })).toHaveAttribute(
    "href",
    "https://www2.census.gov/geo/tiger/GENZ2025/shp/cb_2025_us_county_500k.zip",
  );

  await workspace.getByRole("button", { name: "Layers" }).click();
  const connection = workspace
    .locator('[data-rail-panel="layers"]')
    .locator("[data-reference-geography]", {
      hasText: "2025 Cartographic Boundary Counties",
    });
  await expect(connection).toContainText("VERIFIED_CANDIDATE_HOLD");
  await expect(connection).toContainText("runtime geometry remains held");
});
