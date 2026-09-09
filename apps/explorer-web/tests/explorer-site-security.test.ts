import { describe, expect, it } from "vitest";
import explorerSource from "../src/site/mount-explorer-site.ts?raw";
import livingAtlasSource from "../src/site/mount-living-atlas.ts?raw";

const htmlProperty = ["inner", "HTML"].join("");

describe("Explorer illustrative map DOM safety", () => {
  it("constructs the fixed SVG with namespace-aware nodes instead of HTML parsing", () => {
    expect(explorerSource).not.toContain(htmlProperty);
    expect(explorerSource).not.toMatch(/(?:insertAdjacent|outer)HTML/);
    expect(explorerSource).not.toContain("document.write");
    expect(explorerSource).toContain("createElementNS");
    expect(explorerSource).toContain("textContent = value");
    expect(explorerSource).toContain('svgText(document, "SYNTHETIC MAP STAGE"');
  });

  it("constructs the Living Atlas workspace without HTML parsing", () => {
    expect(livingAtlasSource).not.toContain(htmlProperty);
    expect(livingAtlasSource).not.toMatch(/(?:insertAdjacent|outer)HTML/);
    expect(livingAtlasSource).not.toContain("document.write");
    expect(livingAtlasSource).toContain("textContent = value");
  });
});
