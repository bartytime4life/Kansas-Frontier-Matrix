import { describe, expect, it } from "vitest";
import {
  TERRAIN_SOURCES,
  getTerrainDisplaySource,
  validateTerrainSourceRegistry,
} from "../src/site/terrain-source-registry";

describe("terrain source registry", () => {
  it("keeps the source roles separate and valid", () => {
    expect(validateTerrainSourceRegistry()).toEqual([]);
    expect(TERRAIN_SOURCES.map((source) => source.role)).toEqual([
      "DISPLAY_CONTEXT",
      "AUTHORITATIVE_CANDIDATE",
      "IMPLEMENTATION_SPEC",
    ]);
  });

  it("exposes one reversible Terrarium display carrier", () => {
    const source = getTerrainDisplaySource();
    expect(source.organization).toBe("AWS Open Data / Mapzen");
    expect(source.tileTemplate).toMatch(/^https:\/\//);
    expect(source.encoding).toBe("terrarium");
    expect(source.tileSize).toBe(256);
    expect(source.boundary).toMatch(/must not become a KFM elevation measurement/i);
  });

  it("keeps 3DEP authoritative but unadmitted", () => {
    const source = TERRAIN_SOURCES.find(
      (candidate) => candidate.id === "terrain-usgs-3dep-13arc",
    );
    expect(source?.organization).toBe("U.S. Geological Survey");
    expect(source?.role).toBe("AUTHORITATIVE_CANDIDATE");
    expect("tileTemplate" in (source ?? {})).toBe(false);
    expect(source?.boundary).toMatch(/Admission requires/);
  });

  it("treats MapLibre as a renderer contract, not a data authority", () => {
    const source = TERRAIN_SOURCES.find(
      (candidate) => candidate.id === "terrain-maplibre-raster-dem",
    );
    expect(source?.role).toBe("IMPLEMENTATION_SPEC");
    expect(source?.boundary).toMatch(/does not establish source authority/i);
  });
});
