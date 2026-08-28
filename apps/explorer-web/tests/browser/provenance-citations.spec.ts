import { expect, test } from "playwright/test";

test("renders bounded citation links and non-authority copy", async ({ page }) => {
  await page.goto("/tests/browser/provenance-citations.html?fixture=available");

  const panel = page.getByRole("region", { name: "Provenance citations" });
  await expect(panel).toBeVisible();
  await expect(panel).toContainText("does not establish evidence sufficiency");
  await expect(panel).toContainText("KFM republishes a derived representation");
  const doiLink = page.getByRole("link", { name: "Synthetic soil synthesis" });
  await expect(doiLink).toHaveAttribute(
    "href",
    "https://doi.org/10.1234/kfm.synthetic.001",
  );
  await expect(doiLink).toHaveAttribute("rel", "noopener noreferrer");
  await expect(doiLink).toHaveAttribute("referrerpolicy", "no-referrer");
  await expect(panel).toContainText("kfm://prov/activity/synthetic/citations-001");
});

test("malformed detail renders no panel and reflects no canary", async ({ page }) => {
  await page.goto("/tests/browser/provenance-citations.html?fixture=invalid");

  await expect(page.locator("[data-component='provenance-citations']")).toHaveCount(0);
  await expect(page.getByRole("link")).toHaveCount(0);
  await expect(page.locator("body")).not.toContainText(
    "PROVENANCE_INTERNAL_CANARY_9f17c2",
  );
});
