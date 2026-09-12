import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";
import { readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { expect, test } from "playwright/test";

const FIXTURE = {
  id: "kfm-maplibre-webgl-probe-v1",
  style: { version: 8, sources: {}, layers: [] },
  network: "deny-external-http-https",
  viewport: { width: 640, height: 360 },
  device_scale_factor: 1,
} as const;

const sha256 = (value: unknown) =>
  createHash("sha256").update(JSON.stringify(value)).digest("hex");

const toolVersion = (command: string): string => {
  try {
    return execFileSync(command, ["--version"], { encoding: "utf8" }).trim();
  } catch {
    return "UNAVAILABLE";
  }
};

const lockedMapLibreVersion = (): string => {
  const lockfile = readFileSync(
    resolve(process.cwd(), "../../pnpm-lock.yaml"),
    "utf8",
  );
  const match = lockfile.match(
    /packages\/maplibre:\n(?:.|\n)*?\n\s+maplibre-gl:\n\s+specifier: ([^\n]+)/,
  );
  return match?.[1]?.trim() ?? "LOCKFILE_VERSION_UNAVAILABLE";
};

test("records one bounded WebGL2 capability and teardown probe", async ({
  page,
}, testInfo) => {
  const externalRequests: string[] = [];
  page.on("request", (request) => {
    const url = new URL(request.url());
    if (
      (url.protocol === "http:" || url.protocol === "https:") &&
      url.hostname !== "127.0.0.1"
    ) {
      externalRequests.push(url.href);
    }
  });

  await page.setViewportSize(FIXTURE.viewport);
  await page.goto("/tests/browser/maplibre-webgl-probe.html");
  await expect(page.getByRole("status")).toHaveAttribute("data-state", "READY");

  const evidence = await page.evaluate(() => {
    const canvas = document.querySelector<HTMLCanvasElement>("#map canvas");
    const gl = canvas?.getContext("webgl2", {
      antialias: false,
      preserveDrawingBuffer: false,
    });
    const debug = gl?.getExtension("WEBGL_debug_renderer_info");
    const parameter = (name: number) => {
      try {
        return gl?.getParameter(name) ?? null;
      } catch {
        return null;
      }
    };
    return {
      fixture_id: document.body.dataset.fixtureId ?? "MISSING",
      canvas: canvas ? { width: canvas.width, height: canvas.height } : null,
      webgl2: {
        available: gl !== null,
        vendor: debug ? parameter(debug.UNMASKED_VENDOR_WEBGL) : null,
        renderer: debug ? parameter(debug.UNMASKED_RENDERER_WEBGL) : null,
        version: parameter(0x1f02),
        shading_language_version: parameter(0x8b8c),
        max_texture_size: parameter(0x0d33),
      },
      user_agent: navigator.userAgent,
      language: navigator.language,
      timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
      device_pixel_ratio: window.devicePixelRatio,
      ready_state: document.readyState,
    };
  });

  const teardown = await page.evaluate(() => {
    const canvas = document.querySelector("#map canvas");
    const before = Boolean(canvas);
    window.dispatchEvent(new Event("pagehide"));
    return {
      canvas_before_teardown: before,
      canvas_after_teardown: Boolean(document.querySelector("#map canvas")),
    };
  });

  const receipt = {
    schema_version: "kfm.maplibre.browser-probe.v1",
    outcome:
      evidence.webgl2.available &&
      externalRequests.length === 0 &&
      teardown.canvas_after_teardown === false
        ? "PASS"
        : "FAIL",
    probe: "webgl2_failure_handling",
    source_commit: process.env.GITHUB_SHA ?? "LOCAL_UNPINNED",
    candidate: {
      package: "maplibre-gl",
      resolved_lockfile_version: lockedMapLibreVersion(),
      comparison_target: "6.9.0-canary-not-present-on-current-main",
      dependency_admission_changed: false,
    },
    browser: {
      project: testInfo.project.name,
      engine: "Chromium",
      playwright: toolVersion("pnpm"),
      node: process.version,
      pnpm: toolVersion("pnpm"),
    },
    fixture: {
      ...FIXTURE,
      digest_sha256: sha256(FIXTURE),
      page_id: evidence.fixture_id,
    },
    runtime: evidence,
    network: { external_requests: externalRequests, mode: FIXTURE.network },
    teardown,
    governance: {
      release: false,
      deployment: false,
      publication: false,
      dependency_admission: false,
      source_activation: false,
    },
  };

  const receiptBody = JSON.stringify(receipt, null, 2);
  const receiptPath = testInfo.outputPath("maplibre-webgl-probe.receipt.json");
  writeFileSync(receiptPath, receiptBody, "utf8");
  await testInfo.attach("maplibre-webgl-probe.receipt.json", {
    path: receiptPath,
    contentType: "application/json",
  });

  expect(receipt.outcome).toBe("PASS");
  expect(evidence.fixture_id).toBe(FIXTURE.id);
  expect(evidence.webgl2.available).toBe(true);
  expect(externalRequests).toEqual([]);
  expect(teardown.canvas_before_teardown).toBe(true);
  expect(teardown.canvas_after_teardown).toBe(false);
});
