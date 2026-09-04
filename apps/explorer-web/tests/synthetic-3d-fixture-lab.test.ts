import { readFile } from "node:fs/promises";
import { describe, expect, it } from "vitest";

const read = (path: string) =>
  readFile(new URL(path, import.meta.url), "utf8");

describe("optional synthetic MapLibre 3D lab composition", () => {
  it("loads after the existing Explorer and remains disabled until explicit activation", async () => {
    const [index, lab] = await Promise.all([
      read("../index.html"),
      read("../src/fixture-3d-lab.ts"),
    ]);

    expect(index.indexOf('/src/main.ts')).toBeGreaterThan(-1);
    expect(index.indexOf('/src/fixture-3d-lab.ts')).toBeGreaterThan(
      index.indexOf('/src/main.ts'),
    );
    expect(lab).toContain('details.dataset.activation = "disabled"');
    expect(lab).toContain("Activate synthetic 3D lab");
    expect(lab).toContain("Renderer is inactive");
    expect(lab).toContain("createViteSynthetic3dFixtureLab");
    expect(lab.indexOf("createViteSynthetic3dFixtureLab")).toBeLessThan(
      lab.indexOf("const activate = async"),
    );
    expect(lab).toMatch(
      /const activate = async[\s\S]*await createViteSynthetic3dFixtureLab/,
    );
    expect(lab).not.toMatch(/createViteSynthetic3dFixtureLab\(\{[\s\S]*\n\}\);\s*$/);
  });

  it("uses only the package-owned Vite seam and exposes the full bounded 3D control set", async () => {
    const lab = await read("../src/fixture-3d-lab.ts");

    expect(lab).toContain('from "@kfm/maplibre/vite-adapter"');
    expect(lab).not.toMatch(/from ["']maplibre-gl/);
    expect(lab).toContain("Globe evidence towers");
    expect(lab).toContain("Mercator 3D");
    expect(lab).toContain("Flat comparison");
    expect(lab).toContain("Camera pitch");
    expect(lab).toContain("Camera bearing");
    expect(lab).toContain("Vertical field of view");
    expect(lab).toContain("Light azimuth");
    expect(lab).toContain("Synthetic vertical scale");
    expect(lab).toContain("feature-state");
    expect(lab).toContain("kfm:synthetic-3d-selection");
    expect(lab).toContain("ArrowLeft");
    expect(lab).toContain("ArrowRight");
    expect(lab).toContain("ArrowUp");
    expect(lab).toContain("ArrowDown");
    expect(lab).toContain('case "G"');
    expect(lab).toContain('case "Home"');
    expect(lab).toContain('case "Escape"');
    expect(lab).toContain("pagehide");
  });

  it("keeps external acquisition, terrain, protected detail, and unsafe DOM sinks out of the lab", async () => {
    const [lab, runtime] = await Promise.all([
      read("../src/fixture-3d-lab.ts"),
      read("../../../packages/maplibre/src/synthetic-3d-fixture-lab.ts"),
    ]);
    const combined = `${lab}\n${runtime}`;

    expect(combined).not.toMatch(/\bfetch\s*\(/);
    expect(combined).not.toMatch(/\bXMLHttpRequest\b/);
    expect(combined).not.toMatch(/\bWebSocket\b/);
    expect(combined).not.toMatch(/\bEventSource\b/);
    expect(combined).not.toMatch(/\bsetTerrain\b/);
    expect(combined).not.toMatch(/\braster-dem\b/);
    expect(runtime).not.toMatch(/\bpmtiles\b/i);
    expect(combined).not.toMatch(/\bhttps?:\/\//);
    expect(lab).not.toMatch(/\.innerHTML\s*=/);
    expect(lab).toContain("protected location");
    expect(lab).toContain("private-property detail");
    expect(runtime).toContain("sourceRole: \"synthetic_fixture\"");
    expect(runtime).toContain("evidenceState: \"SYNTHETIC_ONLY\"");
    expect(runtime).not.toMatch(/\bterrain\s*:/);
    expect(runtime).not.toMatch(/\bglyphs\s*:/);
    expect(runtime).not.toMatch(/\bsprite\s*:/);
    expect(runtime).not.toMatch(/\btiles\s*:/);
    expect(runtime).not.toMatch(/\burl\s*:/);
  });

  it("provides accessible controls, reduced-motion behavior, and finite teardown fallback", async () => {
    const [lab, css, runtime] = await Promise.all([
      read("../src/fixture-3d-lab.ts"),
      read("../src/site/fixture-3d-lab.css"),
      read("../../../packages/maplibre/src/synthetic-3d-fixture-lab.ts"),
    ]);

    expect(lab).toContain('status.setAttribute("role", "status")');
    expect(lab).toContain('status.setAttribute("aria-live", "polite")');
    expect(lab).toContain(
      'controls.setAttribute("aria-label", "Synthetic MapLibre 3D controls")',
    );
    expect(lab).toContain("mapContainer.tabIndex = 0");
    expect(lab).toContain("Fail-closed fallback");
    expect(lab).toContain("Deactivate and tear down");
    expect(css).toContain("@media (prefers-reduced-motion: reduce)");
    expect(css).toContain("@media (forced-colors: active)");
    expect(css).toContain(":focus-visible");
    expect(runtime).toContain("destroy: () => void");
    expect(runtime).toContain("this.map.remove()");
    expect(runtime).toContain("if (this.status === \"DISPOSED\") return");
    expect(runtime).toContain("SYNTHETIC_3D_WEBGL2_UNAVAILABLE");
    expect(runtime).toContain("SYNTHETIC_3D_INITIALIZATION_FAILED");
  });

  it("configures the renderer worker only inside the existing package-owned Vite adapter", async () => {
    const adapter = await read(
      "../../../packages/maplibre/src/maplibre-vite-adapter.ts",
    );

    expect(adapter).toContain("configureMapLibreViteWorker()");
    expect(adapter).toContain("createViteSynthetic3dFixtureLab");
    expect(adapter).toContain("return createSynthetic3dFixtureLab(options)");
    expect(adapter).toContain("self-contained, same-origin worker asset");
  });
});
