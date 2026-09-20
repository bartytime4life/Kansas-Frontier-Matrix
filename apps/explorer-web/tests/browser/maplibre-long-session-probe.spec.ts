import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";
import { readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { expect, test } from "playwright/test";

const FIXTURE = {
  id: "kfm-maplibre-long-session-probe-v1",
  style: { version: 8, sources: {}, layers: [] },
  cycles: 3,
  network: "deny-external-http-https",
  viewport: { width: 640, height: 360 },
  device_scale_factor: 1,
} as const;

const sha256 = (value: unknown) =>
  createHash("sha256").update(JSON.stringify(value)).digest("hex");

const LOCKFILE_VERSION_UNAVAILABLE = "LOCKFILE_VERSION_UNAVAILABLE";
const PROBE_RESULT_JSON_INVALID = "PROBE_RESULT_JSON_INVALID";
const PROBE_RESULT_MISSING = "PROBE_RESULT_MISSING";

const parseProbeResult = (raw: string | undefined) => {
  if (raw === undefined) {
    return { result: null, result_parse_error: PROBE_RESULT_MISSING };
  }
  try {
    return { result: JSON.parse(raw), result_parse_error: null };
  } catch {
    return { result: null, result_parse_error: PROBE_RESULT_JSON_INVALID };
  }
};

const toolVersion = (
  command: string,
  arguments_: string[] = ["--version"],
): string => {
  try {
    return execFileSync(command, arguments_, { encoding: "utf8" }).trim();
  } catch {
    return "UNAVAILABLE";
  }
};

const lockedMapLibreVersion = (): string => {
  const lockfile = readFileSync(resolve(process.cwd(), "../../pnpm-lock.yaml"), "utf8");
  const lines = lockfile.split(/\r?\n/);
  const importerStart = lines.findIndex(
    (line) => line === "  packages/maplibre:",
  );
  if (importerStart < 0) return LOCKFILE_VERSION_UNAVAILABLE;
  const importerEnd = lines.findIndex(
    (line, index) => index > importerStart && /^ {0,2}\S/.test(line),
  );
  const importer = lines.slice(
    importerStart + 1,
    importerEnd < 0 ? undefined : importerEnd,
  );
  const dependencyStart = importer.findIndex(
    (line) => line === "      maplibre-gl:",
  );
  if (dependencyStart < 0) return LOCKFILE_VERSION_UNAVAILABLE;
  const dependencyEnd = importer.findIndex(
    (line, index) => index > dependencyStart && /^ {0,6}\S/.test(line),
  );
  const versionLine = importer
    .slice(
      dependencyStart + 1,
      dependencyEnd < 0 ? undefined : dependencyEnd,
    )
    .find((line) => /^        version:\s+\S/.test(line));
  return (
    versionLine?.replace(/^        version:\s+/, "").trim() ??
    LOCKFILE_VERSION_UNAVAILABLE
  );
};

test("preserves malformed page evidence as a receipt failure", () => {
  expect(parseProbeResult("{not-json")).toEqual({
    result: null,
    result_parse_error: PROBE_RESULT_JSON_INVALID,
  });
});

test("repeats the package-owned MapLibre lifecycle and tears down every cycle", async ({
  page,
  browser,
}, testInfo) => {
  const externalRequests: string[] = [];
  page.on("request", (request) => {
    const url = new URL(request.url());
    if (
      (url.protocol === "http:" || url.protocol === "https:") &&
      !["127.0.0.1", "localhost"].includes(url.hostname)
    ) {
      externalRequests.push(url.href);
    }
  });

  await page.setViewportSize(FIXTURE.viewport);
  await page.goto("/tests/browser/maplibre-long-session-probe.html");
  await page.waitForFunction(
    () => ["PASS", "FAIL"].includes(document.querySelector("#probe-status")?.getAttribute("data-state") ?? ""),
    undefined,
    { timeout: 20_000 },
  );

  const evidence = await page.evaluate(() => {
    const raw = document.body.dataset.probeResult;
    let result: unknown = null;
    let resultParseError: string | null = null;
    if (raw === undefined) {
      resultParseError = "PROBE_RESULT_MISSING";
    } else {
      try {
        result = JSON.parse(raw);
      } catch {
        resultParseError = "PROBE_RESULT_JSON_INVALID";
      }
    }
    return {
      fixture_id: document.body.dataset.fixtureId ?? "MISSING",
      status: document.querySelector("#probe-status")?.getAttribute("data-state") ?? "MISSING",
      result,
      result_parse_error: resultParseError,
      user_agent: navigator.userAgent,
      language: navigator.language,
      timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
      device_pixel_ratio: window.devicePixelRatio,
      ready_state: document.readyState,
    };
  });

  const receipt = {
    schema_version: "kfm.maplibre.browser-probe.v1",
    outcome:
      (evidence.result as { passed?: boolean } | null)?.passed === true &&
      evidence.result_parse_error === null &&
      externalRequests.length === 0
        ? "PASS"
        : "FAIL",
    probe: "long_session_teardown",
    source_commit: process.env.GITHUB_SHA ?? "LOCAL_UNPINNED",
    candidate: {
      package: "maplibre-gl",
      resolved_lockfile_version: lockedMapLibreVersion(),
      comparison_target: "6.9.0-exact-candidate",
      dependency_admission_changed: false,
    },
    browser: {
      project: testInfo.project.name || "default",
      engine: browser.browserType().name(),
      browser_version: browser.version(),
      playwright: toolVersion("pnpm", ["exec", "playwright", "--version"]),
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
    governance: {
      release: false,
      deployment: false,
      publication: false,
      dependency_admission: false,
      source_activation: false,
    },
  };

  const receiptBody = JSON.stringify(receipt, null, 2);
  const receiptPath = testInfo.outputPath("maplibre-long-session-probe.receipt.json");
  writeFileSync(receiptPath, receiptBody, "utf8");
  await testInfo.attach("maplibre-long-session-probe.receipt.json", {
    path: receiptPath,
    contentType: "application/json",
  });

  expect(receipt.outcome).toBe("PASS");
  expect(evidence.fixture_id).toBe(FIXTURE.id);
  expect(evidence.status).toBe("PASS");
  const result = evidence.result as {
    cycles?: number;
    results?: Array<{ passed: boolean }>;
  } | null;
  expect(evidence.result_parse_error).toBeNull();
  expect(result?.cycles).toBe(FIXTURE.cycles);
  expect(result?.results).toHaveLength(FIXTURE.cycles);
  expect(result?.results?.every((entry) => entry.passed)).toBe(true);
  expect(externalRequests).toEqual([]);
});
