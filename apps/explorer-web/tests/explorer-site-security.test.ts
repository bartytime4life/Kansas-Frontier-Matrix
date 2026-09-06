import { describe, expect, it } from "vitest";
import explorerSource from "../src/site/mount-explorer-site.ts?raw";

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
});
