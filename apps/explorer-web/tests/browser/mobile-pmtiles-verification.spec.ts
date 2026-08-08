import { expect, test } from "playwright/test";

type MobileVerificationWindow = Window & {
  __kfmMobilePmtilesVerification?: Readonly<{
    getLastResult: () => unknown;
  }>;
};

test.use({
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 3,
  hasTouch: true,
  isMobile: true,
});

test.describe("synthetic mobile PMTiles verification", () => {
  test("verifies, decodes, and renders one in-memory PNG tile", async ({
    page,
  }) => {
    const externalRequests: string[] = [];
    page.on("request", (request) => {
      const url = new URL(request.url());
      if (!["127.0.0.1", "localhost"].includes(url.hostname)) {
        externalRequests.push(request.url());
      }
    });

    await page.goto("/tests/browser/mobile-pmtiles-verification.html");
    await page.getByRole("button", {
      name: "Verify and render synthetic tile",
    }).click();

    await expect(page.getByRole("status")).toHaveText(
      "PASS / MOBILE_PMTILES_VERIFY_DECODE_RENDER_PASS",
    );
    await expect(page.getByRole("status")).toHaveAttribute(
      "data-maplibre-boot-state",
      "HOLD",
    );
    await expect(page.getByRole("status")).toHaveAttribute(
      "data-authority",
      "NONE",
    );

    const probe = await page.evaluate(() => {
      const canvas = document.querySelector<HTMLCanvasElement>(
        "#mobile-pmtiles-canvas",
      );
      const context = canvas?.getContext("2d", { willReadFrequently: true });
      return {
        devicePixelRatio: window.devicePixelRatio,
        maxTouchPoints: navigator.maxTouchPoints,
        pixel:
          context === null || context === undefined
            ? null
            : Array.from(context.getImageData(0, 0, 1, 1).data),
        result:
          (window as MobileVerificationWindow).__kfmMobilePmtilesVerification?.getLastResult() ?? null,
      };
    });

    expect(probe.devicePixelRatio).toBe(3);
    expect(probe.maxTouchPoints).toBeGreaterThan(0);
    expect(probe.pixel).toEqual([17, 34, 51, 255]);
    expect(probe.result).toMatchObject({
      outcome: "PASS",
      authority: "NONE",
      maplibreBootState: "HOLD",
      metrics: {
        archiveBytes: 347,
        tileBytes: 70,
      },
    });
    expect(
      await page.getByRole("list", { name: "Verification holds" }).allTextContents(),
    ).toEqual([
      "CRYPTOGRAPHIC_VERIFICATION_UNWIRED",
      "MAPLIBRE_RUNTIME_UNADMITTED",
      "RELEASE_AUTHORIZATION_NOT_EVALUATED",
    ]);
    expect(externalRequests).toEqual([]);
  });

  test("fails closed before decode when archive bytes are altered", async ({
    page,
  }) => {
    await page.goto("/tests/browser/mobile-pmtiles-verification.html");
    await page.getByRole("button", { name: "Verify tampered archive" }).click();

    await expect(page.getByRole("status")).toHaveText(
      "DENY / MOBILE_PMTILES_ARCHIVE_DIGEST_MISMATCH",
    );
    await expect(page.getByRole("status")).toHaveAttribute(
      "data-maplibre-boot-state",
      "HOLD",
    );

    const result = await page.evaluate(
      () => (window as MobileVerificationWindow).__kfmMobilePmtilesVerification?.getLastResult() ?? null,
    );
    expect(result).toMatchObject({
      outcome: "DENY",
      code: "MOBILE_PMTILES_ARCHIVE_DIGEST_MISMATCH",
      authority: "NONE",
      maplibreBootState: "HOLD",
    });
  });
});
