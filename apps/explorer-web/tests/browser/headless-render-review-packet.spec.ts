import { createHash } from "node:crypto";
import { mkdir, readFile, writeFile } from "node:fs/promises";
import { resolve } from "node:path";

import { expect, test } from "playwright/test";

import {
  buildHeadlessRenderReviewMetrics,
  buildHeadlessRenderReviewSidecar,
} from "../../src/features/map_runtime/headless_render_review_packet";

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

function sha256(bytes: Uint8Array): string {
  return `sha256:${createHash("sha256").update(bytes).digest("hex")}`;
}

test("emits a digest-bound synthetic screenshot, metrics, and sidecar packet", async ({
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

  const probe = await page.evaluate(() => {
    const canvas = document.querySelector<HTMLCanvasElement>(
      "#mobile-pmtiles-canvas",
    );
    const context = canvas?.getContext("2d", { willReadFrequently: true });
    const pixelRgba =
      context === null || context === undefined
        ? null
        : Array.from(context.getImageData(0, 0, 1, 1).data);
    return {
      result:
        (window as MobileVerificationWindow).__kfmMobilePmtilesVerification?.getLastResult() ?? null,
      render: {
        decoded: canvas?.width === 1 && canvas.height === 1,
        rendered: pixelRgba !== null,
        width: canvas?.width ?? 0,
        height: canvas?.height ?? 0,
        pixelRgba,
      },
      viewport: {
        width: window.innerWidth,
        height: window.innerHeight,
        deviceScaleFactor: window.devicePixelRatio,
        hasTouch: navigator.maxTouchPoints > 0,
        isMobile: navigator.maxTouchPoints > 0 && window.innerWidth === 390,
      },
    };
  });

  const metricsResult = buildHeadlessRenderReviewMetrics({
    archiveName: "mobile-base.pmtiles",
    externalRequestCount: externalRequests.length,
    browserHeadless: true,
    result: probe.result,
    render: probe.render,
    viewport: probe.viewport,
  });
  expect(metricsResult.ok).toBe(true);
  if (!metricsResult.ok) throw new Error(metricsResult.code);

  const outputDirectory = process.env.KFM_HEADLESS_REVIEW_OUTPUT
    ? resolve(process.env.KFM_HEADLESS_REVIEW_OUTPUT)
    : resolve(process.cwd(), "test-results", "headless-render-review-packet");
  await mkdir(outputDirectory, { recursive: true });
  const screenshotPath = resolve(outputDirectory, "headless-render.png");
  const metricsPath = resolve(outputDirectory, "metrics.json");
  const sidecarPath = resolve(outputDirectory, "sidecar.json");

  const screenshotBytes = await page.screenshot({
    path: screenshotPath,
    fullPage: true,
    animations: "disabled",
  });
  const metricsBytes = Buffer.from(
    `${JSON.stringify(metricsResult.metrics, null, 2)}\n`,
    "utf8",
  );
  await writeFile(metricsPath, metricsBytes);
  const sidecarResult = buildHeadlessRenderReviewSidecar({
    screenshotSha256: sha256(screenshotBytes),
    metricsSha256: sha256(metricsBytes),
  });
  expect(sidecarResult.ok).toBe(true);
  if (!sidecarResult.ok) throw new Error(sidecarResult.code);
  await writeFile(
    sidecarPath,
    `${JSON.stringify(sidecarResult.sidecar, null, 2)}\n`,
    "utf8",
  );

  expect(externalRequests).toEqual([]);
  expect(JSON.parse(await readFile(metricsPath, "utf8"))).toMatchObject({
    source_kind: "SYNTHETIC_FIXTURE",
    style_health: "NOT_EVALUATED",
    publication_state: "NOT_EVALUATED",
    authority: "NONE",
  });
  expect(JSON.parse(await readFile(sidecarPath, "utf8"))).toMatchObject({
    source_kind: "SYNTHETIC_FIXTURE",
    authority: "NONE",
    review_only: true,
  });
});
