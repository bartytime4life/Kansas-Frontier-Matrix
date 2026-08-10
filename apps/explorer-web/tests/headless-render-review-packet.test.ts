import { describe, expect, it } from "vitest";

import builderSource from "../src/features/map_runtime/headless_render_review_packet.ts?raw";
import {
  buildHeadlessRenderReviewMetrics,
  buildHeadlessRenderReviewSidecar,
} from "../src/features/map_runtime/headless_render_review_packet";

function observation(): Record<string, unknown> {
  return {
    archiveName: "mobile-base.pmtiles",
    externalRequestCount: 0,
    browserHeadless: true,
    viewport: {
      width: 390,
      height: 844,
      deviceScaleFactor: 3,
      hasTouch: true,
      isMobile: true,
    },
    result: {
      outcome: "PASS",
      code: "MOBILE_PMTILES_VERIFY_DECODE_RENDER_PASS",
      authority: "NONE",
      holds: [
        "CRYPTOGRAPHIC_VERIFICATION_UNWIRED",
        "MAPLIBRE_RUNTIME_UNADMITTED",
        "RELEASE_AUTHORIZATION_NOT_EVALUATED",
      ],
      maplibreBootState: "HOLD",
      maplibreBootReason: "MAPLIBRE_RUNTIME_UNADMITTED",
      metrics: {
        archiveBytes: 347,
        tileBytes: 70,
        verifyMs: 1.23456,
        decodeRenderMs: 2.34567,
      },
    },
    render: {
      decoded: true,
      rendered: true,
      width: 1,
      height: 1,
      pixelRgba: [17, 34, 51, 255],
    },
  };
}

describe("headless PMTiles render review packet", () => {
  it("builds bounded synthetic metrics while retaining every authority hold", () => {
    const result = buildHeadlessRenderReviewMetrics(observation());
    expect(result).toMatchObject({
      ok: true,
      metrics: {
        status: "PROPOSED_INACTIVE",
        execution_mode: "SYNTHETIC_FIXTURE_ONLY",
        outcome: "PASS",
        source_kind: "SYNTHETIC_FIXTURE",
        archive: {
          name: "mobile-base.pmtiles",
          archive_bytes: 347,
          tile_bytes: 70,
        },
        render: { pixel_rgba: [17, 34, 51, 255] },
        timing: { verify_ms: 1.235, decode_render_ms: 2.346 },
        external_request_count: 0,
        maplibre_boot_state: "HOLD",
        style_health: "NOT_EVALUATED",
        publication_state: "NOT_EVALUATED",
        authority: "NONE",
      },
    });
    if (!result.ok) throw new Error("Expected valid metrics.");
    expect(result.metrics.holds).toEqual([
      "PUBLISHED_PMTILES_NOT_LOADED",
      "CRYPTOGRAPHIC_VERIFICATION_UNWIRED",
      "MAPLIBRE_RUNTIME_UNADMITTED",
      "STYLE_HEALTH_NOT_EVALUATED",
      "RELEASE_AUTHORIZATION_NOT_EVALUATED",
    ]);
  });

  it.each([
    ["external request", (value: Record<string, unknown>) => {
      value.externalRequestCount = 1;
    }],
    ["authority overclaim", (value: Record<string, unknown>) => {
      (value.result as Record<string, unknown>).authority = "RELEASE";
    }],
    ["unexpected field", (value: Record<string, unknown>) => {
      value.internalCanary = "HEADLESS_REVIEW_INTERNAL_CANARY_7d631c";
    }],
  ] as const)("rejects an observation with %s", (_label, mutate) => {
    const value = observation();
    mutate(value);
    expect(buildHeadlessRenderReviewMetrics(value)).toEqual({
      ok: false,
      code: "HEADLESS_RENDER_REVIEW_OBSERVATION_INVALID",
    });
  });

  it("binds distinct nonzero screenshot and metrics digests", () => {
    const screenshot = `sha256:${"a".repeat(64)}`;
    const metrics = `sha256:${"b".repeat(64)}`;
    const result = buildHeadlessRenderReviewSidecar({
      screenshotSha256: screenshot,
      metricsSha256: metrics,
    });
    expect(result).toMatchObject({
      ok: true,
      sidecar: {
        status: "PROPOSED_INACTIVE",
        source_kind: "SYNTHETIC_FIXTURE",
        artifacts: [
          { name: "headless-render.png", role: "SCREENSHOT", sha256: screenshot },
          { name: "metrics.json", role: "METRICS", sha256: metrics },
        ],
        style_health: "NOT_EVALUATED",
        publication_state: "NOT_EVALUATED",
        authority: "NONE",
        review_only: true,
      },
    });
  });

  it.each([
    { screenshotSha256: "sha256:bad", metricsSha256: `sha256:${"b".repeat(64)}` },
    {
      screenshotSha256: `sha256:${"0".repeat(64)}`,
      metricsSha256: `sha256:${"b".repeat(64)}`,
    },
    {
      screenshotSha256: `sha256:${"a".repeat(64)}`,
      metricsSha256: `sha256:${"a".repeat(64)}`,
    },
  ])("rejects unbound, zero, or reused digests", (value) => {
    expect(buildHeadlessRenderReviewSidecar(value)).toEqual({
      ok: false,
      code: "HEADLESS_RENDER_REVIEW_DIGEST_INVALID",
    });
  });

  it("contains no transport, filesystem, MapLibre, or lifecycle authority", () => {
    expect(builderSource).not.toMatch(/\bfetch\s*\(/);
    expect(builderSource).not.toMatch(/\b(?:readFile|writeFile|localStorage)\b/);
    expect(builderSource).not.toMatch(/(?:from|import\()\s*["']maplibre/);
    expect(builderSource).not.toMatch(
      /(?:authorizeRelease|deployArtifact|publishArtifact|promoteArtifact)\s*\(/,
    );
  });
});
