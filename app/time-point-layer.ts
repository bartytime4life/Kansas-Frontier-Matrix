import type { CustomLayerInterface, CustomRenderMethodInput, Map as MapLibreMap } from "./maplibre-seam";

/**
 * Time-windowed points drawn by the GPU. Positions and observation times are
 * uploaded once per data set; playback only changes uniforms, so a moving time
 * cursor never re-tiles, re-filters or re-uploads features. (A MapLibre circle
 * layer driven by setFilter / data-driven paint re-lays out its whole source on
 * every change.)
 *
 * The look matches the two MapLibre circle layers it replaces: a blurred halo
 * under every core, and a core with an opaque stroke, using MapLibre's circle
 * anti-aliasing, premultiplied blending and default "map" pitch scaling.
 *
 * Presentation only: nothing here is queryable, and the CPU still decides
 * which window is selected and how many points it holds.
 */

export type TimePoint = Readonly<{ longitude: number; latitude: number; timeMs: number }>;

export type TimePointWindow = Readonly<{
  visible: boolean;
  halo: boolean;
  opacity: number;
} & (
  | { mode: "slice"; start: number; end: number; endInclusive: boolean }
  | { mode: "pulse"; cursor: number; trailMs: number }
)>;

export type TimePointColors = Readonly<{ halo: string; core: string; stroke: string }>;

export interface TimePointLayer extends CustomLayerInterface {
  /** True when this GPU cannot compile the layer's shaders; it then draws nothing. */
  readonly failed: boolean;
  setPoints(points: readonly TimePoint[]): void;
  setWindow(window: TimePointWindow): void;
}

const RADIANS = Math.PI / 180;
const mercatorX = (lng: number) => (180 + lng) / 360;
const mercatorY = (lat: number) => (180 - (180 / Math.PI) * Math.log(Math.tan(Math.PI / 4 + (lat * RADIANS) / 2))) / 360;
const FLOATS_PER_POINT = 4; // mercator offset x, y; time offset; ground metres

/** "#rrggbb" to linear 0–1 RGB, as MapLibre feeds colors to its shaders. */
export const rgb = (hex: string): [number, number, number] => {
  const value = /^#([0-9a-f]{6})$/i.exec(hex)?.[1];
  if (!value) throw new Error(`Unsupported color ${hex}`);
  return [0, 2, 4].map((offset) => parseInt(value.slice(offset, offset + 2), 16) / 255) as [number, number, number];
};

// Shared instance stage: which points are inside the window, and their age.
const INSTANCE_PRELUDE = `
uniform int u_mode;          // 0 slice, 1 pulse
uniform vec4 u_window;       // slice: start, end, endInclusive; pulse: cursor, trail
uniform int u_pass;          // 0 halo, 1 core
uniform float u_opacity;
uniform vec2 u_extrude;      // 2 / CSS viewport size
uniform float u_extrude_w;   // camera-to-centre distance ("map" pitch scale); 0 falls back to a constant screen size
uniform float u_device_ratio;
in vec2 a_offset;
in float a_time;
in float a_ground;
out vec2 v_corner;
out float v_radius;
out float v_stroke;
out float v_fill_opacity;
out float v_blur;
void instanceStyle(out bool shown) {
  // gl_VertexID walks a 4-corner triangle strip shared by every instance.
  v_corner = vec2(gl_VertexID & 1, gl_VertexID >> 1) * 2.0 - 1.0;
  float progress = 0.0;
  if (u_mode == 0) {
    shown = a_time >= u_window.x && (a_time < u_window.y || (u_window.z > 0.5 && a_time <= u_window.y));
  } else {
    float age = u_window.x - a_time;
    shown = age >= 0.0 && age <= u_window.y;
    progress = u_window.y > 0.0 ? clamp(age / u_window.y, 0.0, 1.0) : 0.0;
  }
  if (u_pass == 0) {
    v_radius = u_mode == 0 ? 10.0 : mix(6.0, 23.0, progress);
    v_stroke = 0.0;
    v_fill_opacity = u_mode == 0 ? u_opacity * 0.25 : mix(u_opacity * 0.58, 0.0, progress);
  } else {
    v_radius = 3.5;
    v_stroke = 1.5;
    v_fill_opacity = u_mode == 0 ? u_opacity : mix(u_opacity, u_opacity * 0.2, progress);
  }
  float blur = u_pass == 0 ? 0.45 : 0.0;
  v_blur = max(blur, 1.0 / (u_device_ratio * (v_radius + v_stroke)));
}
vec4 extrude(vec4 centre) {
  float scale = u_extrude_w > 0.0 ? u_extrude_w : centre.w;
  centre.xy += v_corner * (v_radius + v_stroke) * u_extrude * scale;
  return centre;
}
const vec4 HIDDEN = vec4(2.0, 2.0, 2.0, 1.0);
`;

const MERCATOR_VERTEX_SHADER = `#version 300 es
uniform mat4 u_matrix;       // view-projection with the data origin folded in (float64 on the CPU)
uniform float u_world_size;
${INSTANCE_PRELUDE}
void main() {
  bool shown;
  instanceStyle(shown);
  if (!shown) { gl_Position = HIDDEN; return; }
  gl_Position = extrude(u_matrix * vec4(a_offset * u_world_size, a_ground, 1.0));
}`;

const globeVertexShader = (prelude: string, define: string) => `#version 300 es
${prelude}
${define}
uniform vec2 u_origin;
${INSTANCE_PRELUDE}
void main() {
  bool shown;
  instanceStyle(shown);
  if (!shown) { gl_Position = HIDDEN; return; }
  gl_Position = extrude(projectTileWithElevation(u_origin + a_offset, a_ground));
}`;

const FRAGMENT_SHADER = `#version 300 es
precision highp float;
uniform vec3 u_fill;
uniform vec3 u_stroke_color;
in vec2 v_corner;
in float v_radius;
in float v_stroke;
in float v_fill_opacity;
in float v_blur;
out vec4 fragColor;
void main() {
  // MapLibre circle.fragment.glsl, with well-defined smoothstep edge order.
  float extrude_length = length(v_corner);
  float opacity_t = 1.0 - smoothstep(1.0 - v_blur, 1.0, extrude_length);
  float color_t = v_stroke < 0.01 ? 0.0 : smoothstep(-v_blur, 0.0, extrude_length - v_radius / (v_radius + v_stroke));
  vec4 fill = vec4(u_fill, 1.0) * v_fill_opacity;
  vec4 stroke = vec4(u_stroke_color, 1.0);
  fragColor = opacity_t * mix(fill, stroke, color_t);
  if (fragColor.a <= 0.0) discard;
}`;

const UNIFORMS = ["u_matrix", "u_world_size", "u_origin", "u_mode", "u_window", "u_pass", "u_opacity", "u_extrude", "u_extrude_w", "u_device_ratio",
  "u_fill", "u_stroke_color", "u_projection_matrix", "u_projection_fallback_matrix", "u_projection_tile_mercator_coords", "u_projection_clipping_plane", "u_projection_transition"] as const;
type Uniform = typeof UNIFORMS[number];
type ProgramBundle = { program: WebGLProgram; vao: WebGLVertexArrayObject; uniforms: Record<Uniform, WebGLUniformLocation | null> };

/** Column-major 4×4 product m × translate(tx, ty, 0), in float64. */
export const translateMatrix = (matrix: ArrayLike<number>, tx: number, ty: number): Float32Array => {
  const out = new Float32Array(16);
  for (let index = 0; index < 16; index += 1) out[index] = matrix[index];
  for (let row = 0; row < 4; row += 1) out[12 + row] = matrix[row] * tx + matrix[4 + row] * ty + matrix[12 + row];
  return out;
};

export function createTimePointLayer(options: Readonly<{ id: string; colors: TimePointColors }>): TimePointLayer {
  const halo = rgb(options.colors.halo), core = rgb(options.colors.core), stroke = rgb(options.colors.stroke);
  let map: MapLibreMap | null = null;
  let gl: WebGL2RenderingContext | null = null;
  let buffer: WebGLBuffer | null = null;
  let points: readonly TimePoint[] = [];
  let data = new Float32Array(0);
  let originX = 0, originY = 0, baseTime = 0;
  let uploaded = false;
  let failed = false;
  let windowState: TimePointWindow = { visible: false, halo: false, opacity: 0, mode: "slice", start: 0, end: 0, endInclusive: false };
  const bundles = new Map<string, ProgramBundle>();
  const unsupported = new Set<string>();
  let groundDirty = true;
  let lastGroundUpdate = 0;
  const markDirty = () => { groundDirty = true; };
  const markDirtyForTerrain = (event: { sourceId?: string }) => {
    if (map && event.sourceId && event.sourceId === map.getTerrain()?.source) groundDirty = true;
  };

  const pack = () => {
    data = new Float32Array(points.length * FLOATS_PER_POINT);
    if (!points.length) return;
    // Offsets from a local origin and times from the earliest point keep float32
    // exact: GLM windows are at most 180 minutes (< 2^24 ms) over Kansas.
    originX = mercatorX(points[0].longitude);
    originY = mercatorY(points[0].latitude);
    baseTime = Math.min(...points.map((point) => point.timeMs));
    points.forEach((point, index) => {
      const offset = index * FLOATS_PER_POINT;
      data[offset] = mercatorX(point.longitude) - originX;
      data[offset + 1] = mercatorY(point.latitude) - originY;
      data[offset + 2] = point.timeMs - baseTime;
      data[offset + 3] = 0;
    });
  };

  const upload = () => {
    if (!gl || !buffer) return;
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    gl.bufferData(gl.ARRAY_BUFFER, data, gl.DYNAMIC_DRAW);
    uploaded = true;
  };

  const updateGround = () => {
    if (!map || !gl || !buffer || !points.length) return;
    const terrain = map.getTerrain();
    // Elevation queries walk covering tiles, so only points near the view are re-sampled.
    const bounds = map.getBounds();
    const padLng = (bounds.getEast() - bounds.getWest()) * 0.25, padLat = (bounds.getNorth() - bounds.getSouth()) * 0.25;
    const west = bounds.getWest() - padLng, east = bounds.getEast() + padLng, south = bounds.getSouth() - padLat, north = bounds.getNorth() + padLat;
    points.forEach((point, index) => {
      let elevation = 0;
      if (terrain) {
        if (point.longitude < west || point.longitude > east || point.latitude < south || point.latitude > north) return;
        const sampled = map!.queryTerrainElevation([point.longitude, point.latitude]);
        elevation = sampled !== null && Number.isFinite(sampled) ? sampled : 0;
      }
      data[index * FLOATS_PER_POINT + 3] = elevation;
    });
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    gl.bufferSubData(gl.ARRAY_BUFFER, 0, data);
    groundDirty = false;
  };

  const compile = (context: WebGL2RenderingContext, type: number, source: string) => {
    const shader = context.createShader(type)!;
    context.shaderSource(shader, source);
    context.compileShader(shader);
    if (!context.getShaderParameter(shader, context.COMPILE_STATUS)) throw new Error("Time-point shader failed to compile");
    return shader;
  };

  const createBundle = (context: WebGL2RenderingContext, vertexSource: string): ProgramBundle => {
    const program = context.createProgram()!;
    const vertex = compile(context, context.VERTEX_SHADER, vertexSource);
    const fragment = compile(context, context.FRAGMENT_SHADER, FRAGMENT_SHADER);
    context.attachShader(program, vertex);
    context.attachShader(program, fragment);
    context.linkProgram(program);
    context.deleteShader(vertex);
    context.deleteShader(fragment);
    if (!context.getProgramParameter(program, context.LINK_STATUS)) throw new Error("Time-point program failed to link");
    const vao = context.createVertexArray()!;
    context.bindVertexArray(vao);
    context.bindBuffer(context.ARRAY_BUFFER, buffer);
    const stride = FLOATS_PER_POINT * 4;
    const attribute = (name: string, size: number, offset: number) => {
      const location = context.getAttribLocation(program, name);
      if (location < 0) return;
      context.enableVertexAttribArray(location);
      context.vertexAttribPointer(location, size, context.FLOAT, false, stride, offset * 4);
      context.vertexAttribDivisor(location, 1);
    };
    attribute("a_offset", 2, 0);
    attribute("a_time", 1, 2);
    attribute("a_ground", 1, 3);
    context.bindVertexArray(null);
    return { program, vao, uniforms: Object.fromEntries(UNIFORMS.map((name) => [name, context.getUniformLocation(program, name)])) as ProgramBundle["uniforms"] };
  };

  return {
    id: options.id,
    type: "custom",
    renderingMode: "2d",
    get failed() { return failed; },
    setPoints(next) {
      if (next === points) return;
      points = next;
      pack();
      groundDirty = true;
      upload();
      map?.triggerRepaint();
    },
    setWindow(next) {
      windowState = next;
      map?.triggerRepaint();
    },
    onAdd(nextMap, context) {
      map = nextMap;
      gl = context as WebGL2RenderingContext;
      buffer = gl.createBuffer();
      upload();
      // MapLibre calls onAdd inside addLayer; throwing here would leave a half-added layer.
      try { bundles.set("mercator", createBundle(gl, MERCATOR_VERTEX_SHADER)); } catch { failed = true; }
      nextMap.on("moveend", markDirty);
      nextMap.on("terrain", markDirty);
      nextMap.on("sourcedata", markDirtyForTerrain);
    },
    onRemove(oldMap, context) {
      oldMap.off("moveend", markDirty);
      oldMap.off("terrain", markDirty);
      oldMap.off("sourcedata", markDirtyForTerrain);
      const glContext = context as WebGL2RenderingContext;
      for (const bundle of bundles.values()) { glContext.deleteVertexArray(bundle.vao); glContext.deleteProgram(bundle.program); }
      bundles.clear();
      if (buffer) glContext.deleteBuffer(buffer);
      buffer = null; gl = null; map = null; uploaded = false;
    },
    render(context, input: CustomRenderMethodInput) {
      const glContext = context as WebGL2RenderingContext;
      if (failed || !map || !buffer || !uploaded || !points.length || !windowState.visible) return;
      const now = performance.now();
      if (groundDirty && now - lastGroundUpdate > 500) {
        lastGroundUpdate = now;
        // A failed sample keeps the previous heights rather than breaking the frame.
        try { updateGround(); } catch { groundDirty = false; }
      }
      const variant = input.shaderData?.variantName === "globe" ? "globe" : "mercator";
      if (unsupported.has(variant)) return;
      let bundle = bundles.get(variant);
      if (!bundle) {
        try {
          bundle = createBundle(glContext, globeVertexShader(input.shaderData.vertexShaderPrelude, input.shaderData.define));
        } catch {
          unsupported.add(variant);
          return;
        }
        bundles.set(variant, bundle);
      }
      const { program, vao, uniforms } = bundle;
      glContext.useProgram(program);
      const zoom = map.getZoom();
      const worldSize = 512 * 2 ** zoom;
      if (variant === "globe") {
        const projection = input.defaultProjectionData;
        glContext.uniformMatrix4fv(uniforms.u_projection_matrix, false, projection.mainMatrix as Float32Array);
        glContext.uniformMatrix4fv(uniforms.u_projection_fallback_matrix, false, projection.fallbackMatrix as Float32Array);
        glContext.uniform4f(uniforms.u_projection_tile_mercator_coords, ...projection.tileMercatorCoords);
        glContext.uniform4f(uniforms.u_projection_clipping_plane, ...projection.clippingPlane);
        glContext.uniform1f(uniforms.u_projection_transition, projection.projectionTransition);
        glContext.uniform2f(uniforms.u_origin, originX, originY);
      } else {
        glContext.uniformMatrix4fv(uniforms.u_matrix, false, translateMatrix(input.modelViewProjectionMatrix, originX * worldSize, originY * worldSize));
        glContext.uniform1f(uniforms.u_world_size, worldSize);
      }
      const ratio = map.getPixelRatio();
      const cssWidth = glContext.drawingBufferWidth / ratio, cssHeight = glContext.drawingBufferHeight / ratio;
      const cameraDistance = (map as unknown as { transform?: { cameraToCenterDistance?: number } }).transform?.cameraToCenterDistance;
      glContext.uniform2f(uniforms.u_extrude, 2 / cssWidth, 2 / cssHeight);
      glContext.uniform1f(uniforms.u_extrude_w, cameraDistance && Number.isFinite(cameraDistance) ? cameraDistance : 0);
      glContext.uniform1f(uniforms.u_device_ratio, ratio);
      glContext.uniform1f(uniforms.u_opacity, Math.max(0, Math.min(1, windowState.opacity)));
      if (windowState.mode === "slice") {
        glContext.uniform1i(uniforms.u_mode, 0);
        glContext.uniform4f(uniforms.u_window, windowState.start - baseTime, windowState.end - baseTime, windowState.endInclusive ? 1 : 0, 0);
      } else {
        glContext.uniform1i(uniforms.u_mode, 1);
        glContext.uniform4f(uniforms.u_window, windowState.cursor - baseTime, windowState.trailMs, 0, 0);
      }
      glContext.enable(glContext.BLEND);
      glContext.blendFunc(glContext.ONE, glContext.ONE_MINUS_SRC_ALPHA);
      glContext.disable(glContext.DEPTH_TEST);
      glContext.disable(glContext.CULL_FACE);
      glContext.bindVertexArray(vao);
      // Every halo first, then every core, as the two MapLibre layers stacked them.
      for (const pass of windowState.halo ? [0, 1] : [1]) {
        glContext.uniform1i(uniforms.u_pass, pass);
        const color = pass === 0 ? halo : core;
        glContext.uniform3f(uniforms.u_fill, color[0], color[1], color[2]);
        glContext.uniform3f(uniforms.u_stroke_color, stroke[0], stroke[1], stroke[2]);
        glContext.drawArraysInstanced(glContext.TRIANGLE_STRIP, 0, 4, points.length);
      }
      glContext.bindVertexArray(null);
    },
  };
}
