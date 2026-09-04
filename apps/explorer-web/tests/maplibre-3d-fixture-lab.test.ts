import { describe, expect, it } from "vitest";

import bootstrapSource from "../src/bootstrap.ts?raw";
import activationSource from "../src/site/maplibre-3d-fixture-lab/activation.ts?raw";
import mountSource from "../src/site/maplibre-3d-fixture-lab/mount.ts?raw";
import packageSource from "../../../packages/maplibre/src/synthetic-3d-fixture-lab.ts?raw";
import {
  MAPLIBRE_3D_FIXTURE_QUERY_PARAMETER,
  isMapLibre3DFixtureLabEnabled,
} from "../src/site/maplibre-3d-fixture-lab/activation";

describe("Explorer synthetic MapLibre 3D fixture lab boundary", () => {
  it("is disabled by default and requires the exact opt-in query value", () => {
    expect(isMapLibre3DFixtureLabEnabled("https://kfm.example/")).toBe(false);
    expect(
      isMapLibre3DFixtureLabEnabled(
        `https://kfm.example/?${MAPLIBRE_3D_FIXTURE_QUERY_PARAMETER}=0`,
      ),
    ).toBe(false);
    expect(
      isMapLibre3DFixtureLabEnabled(
        `https://kfm.example/?${MAPLIBRE_3D_FIXTURE_QUERY_PARAMETER}=true`,
      ),
    ).toBe(false);
    expect(
      isMapLibre3DFixtureLabEnabled(
        `https://kfm.example/?${MAPLIBRE_3D_FIXTURE_QUERY_PARAMETER}=1`,
      ),
    ).toBe(true);
  });

  it("loads the renderer lab dynamically after the normal Explorer composition", () => {
    expect(bootstrapSource).toContain('import "./main"');
    expect(bootstrapSource).toContain(
      'import("./site/maplibre-3d-fixture-lab/mount")',
    );
    expect(bootstrapSource).toContain("isMapLibre3DFixtureLabEnabled");
    expect(bootstrapSource).toContain('"pagehide"');
  });

  it("keeps direct MapLibre ownership inside the package seam", () => {
    const appSource = `${bootstrapSource}\n${activationSource}\n${mountSource}`;
    expect(appSource).not.toMatch(/from\s+["']maplibre-gl/);
    expect(mountSource).toContain(
      'from "@kfm/maplibre/vite-adapter"',
    );
    expect(packageSource).toContain(
      'from "maplibre-gl"',
    );
  });

  it("contains no browser fetch, persistence, source activation, or publication path", () => {
    const source = `${bootstrapSource}\n${activationSource}\n${mountSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(
      /(?:source admission|catalog promotion|promotion decision|release manifest)/i,
    );
    expect(source).toContain("Synthetic fixture only");
    expect(source).toContain("does not identify released evidence");
  });
});
