import type { CustomLayerInterface, CustomRenderMethodInput, Map as MapLibreMap } from "./maplibre-seam";
import type { DaylightBand } from "./daylight-layer";

/**
 * The calculated night and twilight overlay, drawn per pixel on the GPU.
 *
 * Every pixel's solar elevation follows from one pair of uniforms — the
 * subsolar longitude and the solar declination — so moving the clock never
 * rebuilds, clips, re-tiles or re-uploads geometry. The mesh is a fixed world
 * grid uploaded once. Band thresholds and colors are the same ones the GeoJSON
 * fallback draws, so the two paths cannot drift apart.
 */

/** Band boundaries are solar elevations; `shade` is the value the fill paint is
 * evaluated at for that band (the polygon fallback stores it per feature). */
export const DAYLIGHT_BANDS: readonly Readonly<{ band: DaylightBand; below: number; shade: number }>[] = Object.freeze([
  { band: "night", below: -18, shade: -18 },
  { band: "astronomical", below: -12, shade: -15 },
  { band: "nautical", below: -6, shade: -9 },
  // The outer edge is the conventional -0.833° sunrise/sunset boundary.
  { band: "civil", below: -0.833, shade: -3.4165 },
]);

/** Fill color and opacity by shade, shared with the GeoJSON fallback paint. */
export const DAYLIGHT_SHADE_STOPS: readonly Readonly<{ shade: number; color: string; opacity: number }>[] = Object.freeze([
  { shade: -18, color: "#0b1b2d", opacity: 0.66 },
  { shade: -12, color: "#1c3550", opacity: 0.48 },
  { shade: -6, color: "#40546a", opacity: 0.30 },
  { shade: -0.833, color: "#937c59", opacity: 0.16 },
]);

const RAD = Math.PI / 180;
const rgb = (hex: string): [number, number, number] => [1, 3, 5].map((offset) => parseInt(hex.slice(offset, offset + 2), 16) / 255) as [number, number, number];

/** MapLibre's linear `interpolate` over the stops, as premultiplied RGBA. */
export const daylightBandColor = (shade: number): [number, number, number, number] => {
  const stops = DAYLIGHT_SHADE_STOPS;
  // Clamp outside the stop range, as MapLibre's interpolate does.
  const found = stops.findIndex((stop) => stop.shade >= shade);
  const upper = found < 0 ? stops.length - 1 : found;
  const lower = Math.max(0, upper - 1);
  const from = stops[lower], to = stops[upper];
  const t = to.shade === from.shade ? 0 : Math.min(1, Math.max(0, (shade - from.shade) / (to.shade - from.shade)));
  const [r0, g0, b0] = rgb(from.color), [r1, g1, b1] = rgb(to.color);
  const opacity = from.opacity + (to.opacity - from.opacity) * t;
  return [(r0 + (r1 - r0) * t) * opacity, (g0 + (g1 - g0) * t) * opacity, (b0 + (b1 - b0) * t) * opacity, opacity];
};

/** Geometric solar elevation in degrees — the formula the fragment shader evaluates. */
export const solarElevationFromSubsolar = (subsolarLongitude: number, declination: number, longitude: number, latitude: number): number => {
  const sine = Math.sin(latitude * RAD) * Math.sin(declination * RAD)
    + Math.cos(latitude * RAD) * Math.cos(declination * RAD) * Math.cos((longitude - subsolarLongitude) * RAD);
  return Math.asin(Math.max(-1, Math.min(1, sine))) / RAD;
};

/** The band the shader draws for an elevation, or null in daylight. */
export const daylightBandForElevation = (elevation: number): DaylightBand | null =>
  DAYLIGHT_BANDS.find(({ below }) => elevation < below)?.band ?? null;

// A fixed world grid in Mercator 0–1 coordinates; fine enough to follow the
// globe's curvature. Band edges come from the fragment shader, not the mesh.
const GRID_X = 128, GRID_Y = 64;
const buildGrid = () => {
  const vertices = new Float32Array((GRID_X + 1) * (GRID_Y + 1) * 2);
  let offset = 0;
  for (let y = 0; y <= GRID_Y; y += 1) for (let x = 0; x <= GRID_X; x += 1) { vertices[offset++] = x / GRID_X; vertices[offset++] = y / GRID_Y; }
  const indices = new Uint16Array(GRID_X * GRID_Y * 6);
  offset = 0;
  for (let y = 0; y < GRID_Y; y += 1) for (let x = 0; x < GRID_X; x += 1) {
    const a = y * (GRID_X + 1) + x, b = a + 1, c = a + GRID_X + 1, d = c + 1;
    indices.set([a, c, b, b, c, d], offset); offset += 6;
  }
  return { vertices, indices };
};

const FRAGMENT_SHADER = `#version 300 es
precision highp float;
uniform vec2 u_sun;            // subsolar longitude, declination (radians)
uniform vec4 u_band_color[4];  // premultiplied RGBA: night, astronomical, nautical, civil
in vec2 v_merc;
out vec4 fragColor;
const float PI = 3.141592653589793;
float elevation(vec2 merc) {
  float longitude = merc.x * 2.0 * PI - PI;
  float latitude = atan(sinh(PI * (1.0 - 2.0 * merc.y)));
  float sine = sin(latitude) * sin(u_sun.y) + cos(latitude) * cos(u_sun.y) * cos(longitude - u_sun.x);
  return degrees(asin(clamp(sine, -1.0, 1.0)));
}
vec4 band(float e) {
  if (e < -18.0) return u_band_color[0];
  if (e < -12.0) return u_band_color[1];
  if (e < -6.0) return u_band_color[2];
  if (e < -0.833) return u_band_color[3];
  return vec4(0.0);
}
void main() {
  float e = elevation(v_merc);
  // Four samples across this pixel's elevation span anti-alias the band edges.
  float w = fwidth(e);
  fragColor = 0.25 * (band(e - 0.375 * w) + band(e - 0.125 * w) + band(e + 0.125 * w) + band(e + 0.375 * w));
  if (fragColor.a <= 0.0) discard;
}`;

const MERCATOR_VERTEX_SHADER = `#version 300 es
uniform mat4 u_matrix;
uniform float u_world_size;
uniform float u_copy;
in vec2 a_pos;
out vec2 v_merc;
void main() {
  v_merc = a_pos;
  gl_Position = u_matrix * vec4((a_pos + vec2(u_copy, 0.0)) * u_world_size, 0.0, 1.0);
}`;

const globeVertexShader = (prelude: string, define: string) => `#version 300 es
${prelude}
${define}
in vec2 a_pos;
out vec2 v_merc;
void main() {
  v_merc = a_pos;
  gl_Position = projectTileWithElevation(a_pos, 0.0);
}`;

const UNIFORMS = ["u_matrix", "u_world_size", "u_copy", "u_sun", "u_band_color", "u_projection_matrix", "u_projection_fallback_matrix",
  "u_projection_tile_mercator_coords", "u_projection_clipping_plane", "u_projection_transition"] as const;
type ProgramBundle = { program: WebGLProgram; vao: WebGLVertexArrayObject; uniforms: Record<typeof UNIFORMS[number], WebGLUniformLocation | null> };

export interface DaylightShaderLayer extends CustomLayerInterface {
  /** True when this GPU cannot compile the overlay; callers fall back to polygons. */
  readonly failed: boolean;
  setSun(subsolarLongitudeDegrees: number, declinationDegrees: number): void;
}

export function createDaylightShaderLayer(id: string): DaylightShaderLayer {
  const grid = buildGrid();
  const colors = new Float32Array(DAYLIGHT_BANDS.flatMap(({ shade }) => daylightBandColor(shade)));
  let map: MapLibreMap | null = null;
  let vertexBuffer: WebGLBuffer | null = null, indexBuffer: WebGLBuffer | null = null;
  let sun: [number, number] | null = null;
  let failed = false, indicesUploaded = false;
  const bundles = new Map<string, ProgramBundle>();
  const unsupported = new Set<string>();

  const compile = (gl: WebGL2RenderingContext, type: number, source: string) => {
    const shader = gl.createShader(type)!;
    gl.shaderSource(shader, source);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) throw new Error("Daylight shader failed to compile");
    return shader;
  };
  const createBundle = (gl: WebGL2RenderingContext, vertexSource: string): ProgramBundle => {
    const program = gl.createProgram()!;
    const vertex = compile(gl, gl.VERTEX_SHADER, vertexSource), fragment = compile(gl, gl.FRAGMENT_SHADER, FRAGMENT_SHADER);
    gl.attachShader(program, vertex);
    gl.attachShader(program, fragment);
    gl.linkProgram(program);
    gl.deleteShader(vertex);
    gl.deleteShader(fragment);
    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) throw new Error("Daylight program failed to link");
    const vao = gl.createVertexArray()!;
    gl.bindVertexArray(vao);
    gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
    // The element binding is VAO state: bind (and first upload) it only inside our own VAO.
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indexBuffer);
    if (!indicesUploaded) { gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, grid.indices, gl.STATIC_DRAW); indicesUploaded = true; }
    const location = gl.getAttribLocation(program, "a_pos");
    if (location >= 0) { gl.enableVertexAttribArray(location); gl.vertexAttribPointer(location, 2, gl.FLOAT, false, 8, 0); }
    gl.bindVertexArray(null);
    return { program, vao, uniforms: Object.fromEntries(UNIFORMS.map((name) => [name, gl.getUniformLocation(program, name)])) as ProgramBundle["uniforms"] };
  };

  // Mercator x ranges of the world copies in view (one copy when copies are off).
  const copies = (): number[] => {
    if (!map || !map.getRenderWorldCopies()) return [0];
    const bounds = map.getBounds();
    const first = Math.floor((bounds.getWest() + 180) / 360), last = Math.floor((bounds.getEast() + 180) / 360);
    const out: number[] = [];
    for (let copy = Math.max(first, -2); copy <= Math.min(last, 2); copy += 1) out.push(copy);
    return out.length ? out : [0];
  };

  return {
    id,
    type: "custom",
    renderingMode: "2d",
    get failed() { return failed; },
    setSun(subsolarLongitudeDegrees, declinationDegrees) {
      sun = [subsolarLongitudeDegrees * RAD, declinationDegrees * RAD];
      map?.triggerRepaint();
    },
    onAdd(nextMap, context) {
      const gl = context as WebGL2RenderingContext;
      map = nextMap;
      vertexBuffer = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
      gl.bufferData(gl.ARRAY_BUFFER, grid.vertices, gl.STATIC_DRAW);
      indexBuffer = gl.createBuffer();
      // MapLibre calls onAdd inside addLayer; throwing here would leave a half-added layer.
      try { bundles.set("mercator", createBundle(gl, MERCATOR_VERTEX_SHADER)); } catch { failed = true; }
    },
    onRemove(_oldMap, context) {
      const gl = context as WebGL2RenderingContext;
      for (const bundle of bundles.values()) { gl.deleteVertexArray(bundle.vao); gl.deleteProgram(bundle.program); }
      bundles.clear();
      if (vertexBuffer) gl.deleteBuffer(vertexBuffer);
      if (indexBuffer) gl.deleteBuffer(indexBuffer);
      vertexBuffer = null; indexBuffer = null; indicesUploaded = false; map = null;
    },
    render(context, input: CustomRenderMethodInput) {
      const gl = context as WebGL2RenderingContext;
      if (failed || !map || !vertexBuffer || !sun) return;
      const variant = input.shaderData?.variantName === "globe" ? "globe" : "mercator";
      if (unsupported.has(variant)) return;
      let bundle = bundles.get(variant);
      if (!bundle) {
        try {
          bundle = createBundle(gl, globeVertexShader(input.shaderData.vertexShaderPrelude, input.shaderData.define));
        } catch {
          unsupported.add(variant);
          return;
        }
        bundles.set(variant, bundle);
      }
      const { program, vao, uniforms } = bundle;
      gl.useProgram(program);
      gl.uniform2f(uniforms.u_sun, sun[0], sun[1]);
      gl.uniform4fv(uniforms.u_band_color, colors);
      gl.enable(gl.BLEND);
      gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA);
      gl.disable(gl.DEPTH_TEST);
      gl.disable(gl.CULL_FACE);
      gl.bindVertexArray(vao);
      if (variant === "globe") {
        const projection = input.defaultProjectionData;
        gl.uniformMatrix4fv(uniforms.u_projection_matrix, false, projection.mainMatrix as Float32Array);
        gl.uniformMatrix4fv(uniforms.u_projection_fallback_matrix, false, projection.fallbackMatrix as Float32Array);
        gl.uniform4f(uniforms.u_projection_tile_mercator_coords, ...projection.tileMercatorCoords);
        gl.uniform4f(uniforms.u_projection_clipping_plane, ...projection.clippingPlane);
        gl.uniform1f(uniforms.u_projection_transition, projection.projectionTransition);
        gl.drawElements(gl.TRIANGLES, grid.indices.length, gl.UNSIGNED_SHORT, 0);
      } else {
        gl.uniformMatrix4fv(uniforms.u_matrix, false, input.modelViewProjectionMatrix as Float32Array);
        gl.uniform1f(uniforms.u_world_size, 512 * 2 ** map.getZoom());
        for (const copy of copies()) {
          gl.uniform1f(uniforms.u_copy, copy);
          gl.drawElements(gl.TRIANGLES, grid.indices.length, gl.UNSIGNED_SHORT, 0);
        }
      }
      gl.bindVertexArray(null);
    },
  };
}
