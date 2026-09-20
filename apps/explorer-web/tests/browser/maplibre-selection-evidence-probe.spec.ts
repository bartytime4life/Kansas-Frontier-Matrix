import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";
import { readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { expect, test } from "playwright/test";

const FIXTURE = {
  id: "kfm-maplibre-selection-evidence-probe-v1",
  candidate: "maplibre-gl@6.9.0",
  source: "inline-geojson",
  rendered_layer: "synthetic-selection",
  selection_id: "selection:maplibre:flow-001",
  selection_trigger: "explicit-bounded-point-query",
  viewport: { width: 640, height: 360 },
  device_scale_factor: 1,
  network: "deny-external-http-https",
} as const;

const sha256 = (value: unknown) =>
  createHash("sha256").update(JSON.stringify(value)).digest("hex");

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
  const lockfile = readFileSync(
    resolve(process.cwd(), "../../pnpm-lock.yaml"),
    "utf8",
  );
  const lines = lockfile.split(/\r?\n/);
  const importerStart = lines.findIndex(
    (line) => line === "  packages/maplibre:",
  );
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
  const dependencyEnd = importer.findIndex(
    (line, index) => index > dependencyStart && /^ {0,6}\S/.test(line),
  );
  const versionLine = importer
    .slice(
      dependencyStart + 1,
      dependencyEnd < 0 ? undefined : dependencyEnd,
    )
    .find((line) => /^        version:\s+\S/.test(line));
  return versionLine?.replace(/^        version:\s+/, "").trim() ?? "UNAVAILABLE";
};

test("selects an inline GeoJSON feature and opens its governed Evidence Drawer", async ({
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
  await page.goto("/tests/browser/maplibre-selection-evidence-probe.html");
  await expect(page.locator("#runtime-status")).toHaveAttribute(
    "data-state",
    "READY",
  );
  const map = page.locator("#maplibre-selection-map");
  const canvas = map.locator("canvas");
  await expect(canvas).toBeVisible();

  await page
    .getByRole("button", { name: "Select rendered feature at map center" })
    .click();

  await expect(page.locator("#evidence-status")).toHaveText(
    "ANSWER / SUPPORTED",
  );
  const drawer = page.getByRole("complementary", {
    name: /Evidence Drawer: supported evidence/,
  });
  await expect(drawer).toBeVisible();
  await expect(drawer).toContainText("kfm:evidence:synthetic:flow-001");
  await expect(drawer).toContainText("Release: RELEASED");
  await expect(page.locator("body")).toHaveAttribute(
    "data-selection-id",
    FIXTURE.selection_id,
  );
  await expect(page.locator("body")).toHaveAttribute(
    "data-layer-admission",
    "PASS",
  );

  const pageEvidence = await page.evaluate(() => ({
    fixture_id: document.body.dataset.fixtureId ?? "MISSING",
    initialization: document.body.dataset.initialization ?? "MISSING",
    selection_id: document.body.dataset.selectionId ?? "MISSING",
    layer_admission: document.body.dataset.layerAdmission ?? "MISSING",
    rendered_candidate: document.body.dataset.renderedCandidate ?? "MISSING",
    runtime_state:
      document.querySelector("#runtime-status")?.getAttribute("data-state") ??
      "MISSING",
    evidence_state:
      document.querySelector("#evidence-status")?.getAttribute("data-state") ??
      "MISSING",
    evidence_code:
      document.querySelector("#evidence-status")?.getAttribute("data-code") ??
      "MISSING",
  }));
  const resolvedVersion = lockedMapLibreVersion();
  const receipt = {
    schema_version: "kfm.maplibre.browser-probe.v1",
    outcome:
      pageEvidence.fixture_id === FIXTURE.id &&
      pageEvidence.initialization === "resolved" &&
      pageEvidence.selection_id === FIXTURE.selection_id &&
      pageEvidence.layer_admission === "PASS" &&
      pageEvidence.runtime_state === "READY" &&
      pageEvidence.evidence_state === "ANSWER" &&
      pageEvidence.evidence_code === "SUPPORTED" &&
      externalRequests.length === 0 &&
      resolvedVersion === "6.9.0"
        ? "PASS"
        : "FAIL",
    probe: "same_candidate_selection_to_evidence_drawer",
    readiness_probe_effects: [
      "query_rendered_features",
      "evidence_drawer_selection_stability",
    ],
    source_commit: process.env.GITHUB_SHA ?? "LOCAL_UNPINNED",
    candidate: {
      package: "maplibre-gl",
      resolved_lockfile_version: resolvedVersion,
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
    fixture: { ...FIXTURE, digest_sha256: sha256(FIXTURE) },
    evidence: pageEvidence,
    network: { external_requests: externalRequests, mode: FIXTURE.network },
    governance: {
      dependency_admission: false,
      source_activation: false,
      release: false,
      deployment: false,
      publication: false,
    },
    retained_holds: [
      "worker_csp_loading",
      "visual_pixel_diff",
      "pmtiles_vector_tile_loading",
      "terrain_dem_regression",
      "headless_render_parity",
    ],
    limitations: {
      pointer_event_parity: "NOT_ASSERTED",
      live_source_loading: "NOT_ASSERTED",
    },
  };

  const receiptPath = testInfo.outputPath(
    "maplibre-selection-evidence-probe.receipt.json",
  );
  writeFileSync(receiptPath, JSON.stringify(receipt, null, 2), "utf8");
  await testInfo.attach("maplibre-selection-evidence-probe.receipt.json", {
    path: receiptPath,
    contentType: "application/json",
  });

  expect(receipt.outcome).toBe("PASS");
  expect(JSON.parse(pageEvidence.rendered_candidate)).toMatchObject({
    featureId: "flow-001",
    layerId: FIXTURE.rendered_layer,
    sourceId: "synthetic-selection-source",
    properties: { fixture_key: "flow-001" },
  });
  expect(externalRequests).toEqual([]);
});
