import { expect, test } from "playwright/test";

const SELECTED_EPOCH = -3773778900;

test("renders the governed UTC second range with explicit slider ARIA", async ({ page }) => {
  await page.goto("/tests/browser/time-banner.html?fixture=answer");

  const slider = page.getByRole("slider", { name: "Selected time" });
  await expect(slider).toBeVisible();
  await expect(slider).toHaveAttribute("aria-valuenow", String(SELECTED_EPOCH));
  await expect(slider).toHaveAttribute("aria-valuetext", "1850-06-01 00:05:00Z");
  await expect(page.locator('[data-component="time-scrubber-output"]')).toHaveText(
    "1850-06-01 00:05:00Z",
  );
});

test("keyboard controls emit second, minute, and boundary changes", async ({ page }) => {
  await page.goto("/tests/browser/time-banner.html?fixture=answer");
  const slider = page.getByRole("slider", { name: "Selected time" });
  await slider.focus();

  await page.keyboard.press("ArrowRight");
  await expect(page.locator("#event-status")).toHaveText(
    "scrub:key:1850-06-01T00:05:01Z",
  );

  await page.keyboard.press("Shift+ArrowRight");
  await expect(page.locator("#event-status")).toHaveText(
    "scrub:key:1850-06-01T00:06:01Z",
  );

  await page.keyboard.press("Home");
  await expect(page.locator("#event-status")).toHaveText(
    "scrub:key:1850-06-01T00:00:00Z",
  );

  await page.keyboard.press("End");
  await expect(page.locator("#event-status")).toHaveText(
    "scrub:key:1850-06-01T00:10:00Z",
  );
});

test("pointer input reports drag and touch sources without transport", async ({ page }) => {
  await page.goto("/tests/browser/time-banner.html?fixture=answer");
  const slider = page.getByRole("slider", { name: "Selected time" });

  await slider.dispatchEvent("pointerdown", { pointerType: "mouse" });
  await slider.evaluate((element) => {
    const range = element as HTMLInputElement;
    range.value = String(Number(range.value) + 1);
    range.dispatchEvent(new Event("input", { bubbles: true }));
  });
  await expect(page.locator("#event-status")).toHaveText(
    "scrub:drag:1850-06-01T00:05:01Z",
  );
  await slider.dispatchEvent("pointerup", { pointerType: "mouse" });

  await slider.dispatchEvent("pointerdown", { pointerType: "touch" });
  await slider.evaluate((element) => {
    const range = element as HTMLInputElement;
    range.value = String(Number(range.value) + 1);
    range.dispatchEvent(new Event("input", { bubbles: true }));
  });
  await expect(page.locator("#event-status")).toHaveText(
    "scrub:touch:1850-06-01T00:05:02Z",
  );
  await slider.dispatchEvent("pointerup", { pointerType: "touch" });
});

test("touch long-press and keyboard button expose one exact-copy surface", async ({ page }) => {
  await page.goto("/tests/browser/time-banner.html?fixture=answer");
  const slider = page.getByRole("slider", { name: "Selected time" });
  const details = page.getByRole("region", { name: "Exact selected timestamp" });

  await expect(details).toBeHidden();
  await slider.dispatchEvent("pointerdown", { pointerType: "touch" });
  await page.waitForTimeout(350);
  await expect(details).toBeVisible();
  await slider.dispatchEvent("pointerup", { pointerType: "touch" });

  await page.getByRole("button", { name: "Copy selected timestamp" }).click();
  await expect(page.locator("#copied-status")).toHaveText(
    "copied:1850-06-01T00:05:00Z",
  );
  await expect(page.getByText("Timestamp copied.")).toBeVisible();

  await page.keyboard.press("Escape");
  await expect(details).toBeHidden();
  await page.getByRole("button", { name: "Show exact timestamp" }).click();
  await expect(details).toBeVisible();
});

for (const fixture of ["deny", "stale", "conflict", "invalid"] as const) {
  test(`${fixture} exposes no scrubber or protected payload detail`, async ({ page }) => {
    await page.goto(`/tests/browser/time-banner.html?fixture=${fixture}`);

    await expect(page.getByRole("slider")).toHaveCount(0);
    await expect(page.getByRole("button", { name: "Show exact timestamp" })).toHaveCount(0);
    await expect(page.locator("body")).not.toContainText(
      "SENSITIVE_TIME_DENIAL_CANARY_64ad31",
    );
    await expect(page.locator("body")).not.toContainText("PRIVATE_TIME_CANARY_9ff2ce");
    await expect(page.locator("#event-status")).toHaveText("scrub:none");
  });
}
