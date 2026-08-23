import { expect, test } from "playwright/test";

test("mounts the public workspace registry over the compatible anchor navigation", async ({
  page,
}) => {
  await page.goto("/");

  const navigation = page.getByRole("navigation", {
    name: "Explorer workspaces",
  });
  await expect(navigation).toHaveAttribute(
    "data-workspace-navigation-profile",
    "kfm.explorer.public-workspace-navigation.v1",
  );

  const links = navigation.getByRole("link");
  await expect(links).toHaveCount(4);
  await expect(links).toHaveText(["Map", "Knowledge", "Features", "Trust"]);
  await expect(links.nth(0)).toHaveAttribute("href", "#map");
  await expect(links.nth(1)).toHaveAttribute("href", "#knowledge");
  await expect(links.nth(2)).toHaveAttribute("href", "#features");
  await expect(links.nth(3)).toHaveAttribute("href", "#trust");
  await expect(navigation.getByRole("link", { name: /admin|review/i })).toHaveCount(0);

  await navigation.getByRole("link", { name: "Trust" }).click();
  await expect(page).toHaveURL(/#trust$/);
  await expect(page.locator("#trust")).toBeVisible();
});
