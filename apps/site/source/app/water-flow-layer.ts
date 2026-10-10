import type { CustomLayerInterface, CustomRenderMethodInput, Map as MapLibreMap } from "./maplibre-seam";
import { FLOW_SEGMENT_FLOATS, type FlowGeometry } from "./water-flow-motion";

/**
 * Flowing water as a MapLibre custom WebGL2 layer. Each river segment is an
 * instanced screen-space ribbon shaded like a lit tube. Light streaks travel
 * toward larger along-reach distance, which is downstream in the provider's
 * digitized order. Ribbons follow the rendered terrain in Terrain 3D, and
 * hills in front hide them through the depth test.
 *
 * Presentation only; see water-flow-motion.ts for what may move and why.
 */

export type WaterFlowPalette = Readonly<{
  base: readonly [number, number, number];
  streak: readonly [number, number, number];
  /** direction-only, rising, steady, falling, unknown trend */
  tints: readonly (readonly [number, number, number])[];
  opacity: number;
}>;

const hex = (value: string): [number, number, number] => [1, 3, 5].map((offset) => parseInt(value.slice(offset, offset + 2), 16) / 255) as [number, number, number];

/** Deep blue with white streaks on light basemaps; luminous cyan at dusk and night. */
export const WATER_FLOW_PALETTES: Readonly<Record<"night" | "dusk" | "clear", WaterFlowPalette>> = Object.freeze({
  clear: { base: hex("#2a7fd0"), streak: hex("#f2feff"), tints: ["#2a7fd0", "#22c8ff", "#2aa3ec", "#2f66d4", "#3c95dc"].map(hex), opacity: 0.86 },
  dusk: { base: hex("#2f8fd0"), streak: hex("#e4fbff"), tints: ["#2f8fd0", "#6cecff", "#4cc9f2", "#4a86ec", "#62b8ec"].map(hex), opacity: 0.84 },
  night: { base: hex("#2a8fd2"), streak: hex("#cdfbff"), tints: ["#2a8fd2", "#7ff3ff", "#58d6f5", "#4a8ff0", "#6cc8f0"].map(hex), opacity: 0.82 },
});

/** Ribbon half-width in CSS pixels by zoom. */
export function flowHalfWidth(zoom: number): number {
  if (!Number.isFinite(zoom)) return 1.6;
  return Math.max(1.4, Math.min(6, 1.6 + (zoom - 10) * 0.6));
}

/** Display motion, in CSS pixels per second and between streaks; not water velocity. */
export const FLOW_SPEED_PX = 34;
export const FLOW_SPACING_PX = 72;

const EARTH_CIRCUMFERENCE_METERS = 2 * Math.PI * 6_378_137;
export const metersPerPixel = (latitude: number, zoom: number): number =>
  EARTH_CIRCUMFERENCE_METERS * Math.cos(Math.max(-85, Math.min(85, latitude)) * Math.PI / 180) / (512 * 2 ** zoom);

const SHARED_MAIN = `
  vec4 ca = projectPoint(i_a);
  vec4 cb = projectPoint(i_b);
  if (ca.w <= 0.0 || cb.w <= 0.0) { gl_Position = vec4(2.0, 2.0, 2.0, 1.0); return; }
  vec2 half_viewport = u_viewport * 0.5;
  vec2 sa = ca.xy / ca.w * half_viewport;
  vec2 sb = cb.xy / cb.w * half_viewport;
  vec2 d = sb - sa;
  float len = length(d);
  vec2 dir = len > 1e-4 ? d / len : vec2(1.0, 0.0);
  vec2 normal = vec2(-dir.y, dir.x);
  // Gauged stretches widen and carry a soft halo so a reading is easy to find.
  float width = u_half_width * (1.0 + 0.85 * i_cue.x);
  float cap = (a_corner.x * 2.0 - 1.0) * width * 0.9;
  vec4 c = mix(ca, cb, a_corner.x);
  c.xy += (normal * a_corner.y * width + dir * cap) / half_viewport * c.w;
  gl_Position = c;
  v_along = mix(i_dist.x, i_dist.y, a_corner.x) + cap * u_m_per_px;
  v_side = a_corner.y;
  v_cue = i_cue;
}`;

const SHARED_DECLARATIONS = `
uniform vec2 u_viewport;
uniform float u_half_width;
uniform float u_lift;
uniform float u_m_per_px;
in vec2 a_corner;
in vec3 i_a;
in vec3 i_b;
in vec2 i_dist;
in vec4 i_cue;
out float v_along;
out float v_side;
out vec4 v_cue;`;

const MERCATOR_VERTEX_SHADER = `#version 300 es
uniform mat4 u_matrix;
uniform float u_world_size;
${SHARED_DECLARATIONS}
vec4 projectPoint(vec3 p) { return u_matrix * vec4(p.xy * u_world_size, p.z + u_lift, 1.0); }
void main() {${SHARED_MAIN}`;

const globeVertexShader = (prelude: string, define: string) => `#version 300 es
${prelude}
${define}
${SHARED_DECLARATIONS}
vec4 projectPoint(vec3 p) { return projectTileWithElevation(p.xy, p.z + u_lift); }
void main() {${SHARED_MAIN}`;

const FRAGMENT_SHADER = `#version 300 es
precision highp float;
uniform float u_time;
uniform float u_m_per_px;
uniform float u_speed_px;
uniform float u_spacing_px;
uniform vec3 u_base;
uniform vec3 u_streak;
uniform vec3 u_tints[5];
uniform float u_opacity;
in float v_along;
in float v_side;
in vec4 v_cue;
out vec4 fragColor;
void main() {
  float side = clamp(v_side, -1.0, 1.0);
  float measured = v_cue.x;
  // The ribbon body narrows inside a gauged stretch to leave room for its halo.
  float edge = mix(1.0, 0.62, measured);
  float body = 1.0 - smoothstep(0.5 * edge, edge, abs(side));
  float halo = measured * (1.0 - smoothstep(edge, 1.0, abs(side))) * (1.0 - body);
  // A lit tube: brighter along the crown, with a thin moving glint.
  float inner = clamp(side / edge, -1.0, 1.0);
  float crown = sqrt(max(0.0, 1.0 - inner * inner));
  float shade = 0.6 + 0.4 * crown;
  float glint = pow(max(0.0, crown * 0.85 + inner * 0.3), 22.0);
  float motion = v_cue.y;
  float px = v_along / u_m_per_px;
  float travel = u_time * u_speed_px * motion;
  // Streaks: a bright head leading downstream with a fading tail.
  float x = fract((px - travel) / u_spacing_px + v_cue.w);
  float streak = pow(x, 4.0) * (1.0 - smoothstep(0.88, 1.0, x));
  // A finer, faster ripple layer breaks up the regular rhythm.
  float y = fract((px - travel * 1.37) / (u_spacing_px * 0.43) + v_cue.w * 3.1);
  float ripple = pow(y, 8.0) * (1.0 - smoothstep(0.94, 1.0, y)) * 0.35;
  // Still water (a measured zero) keeps its colour but loses every streak.
  float flowing = motion;
  vec3 tint = u_tints[int(v_cue.z + 0.5)];
  vec3 color = mix(u_base, tint, measured) * mix(0.75, 1.0, motion) * shade
    + u_streak * (streak + ripple) * crown * flowing * (0.55 + 0.75 * measured)
    + vec3(glint) * 0.45 * flowing;
  // Still water reads as a flat, dark pool with two fixed bank highlights.
  float still = min(1.0, measured * 2.0) * (1.0 - motion);
  float rim = smoothstep(0.5, 0.8, abs(inner)) * (1.0 - smoothstep(0.8, 1.0, abs(inner)));
  color = mix(color, vec3(0.46, 0.53, 0.6) * shade + u_streak * rim * 0.7, still);
  float alpha = body * u_opacity * clamp(0.5 + 0.35 * measured + 0.3 * streak * crown * flowing, 0.0, 1.0);
  float haloAlpha = halo * 0.55 * u_opacity;
  vec3 haloColor = tint * haloAlpha;
  fragColor = vec4(min(color, vec3(1.0)) * alpha + haloColor * (1.0 - alpha), alpha + haloAlpha * (1.0 - alpha));
}`;

const UNIFORMS = ["u_matrix", "u_world_size", "u_viewport", "u_half_width", "u_lift", "u_m_per_px", "u_time", "u_speed_px", "u_spacing_px", "u_base", "u_streak", "u_tints", "u_opacity",
  "u_projection_matrix", "u_projection_fallback_matrix", "u_projection_tile_mercator_coords", "u_projection_clipping_plane", "u_projection_transition"];

export type WaterFlowLayerOptions = Readonly<{
  id: string;
  /** Seconds for the flow clock, or null to hold the water still. */
  clock: () => number | null;
  palette: () => WaterFlowPalette;
}>;

export type WaterFlowLayer = CustomLayerInterface & {
  setGeometry(geometry: FlowGeometry | null): void;
  readonly segmentCount: number;
};

/** Terrain samples per frame; the rest keep their last height until reached. */
const SAMPLES_PER_FRAME = 1500;

export function createWaterFlowLayer(options: WaterFlowLayerOptions): WaterFlowLayer {
  type Program = { program: WebGLProgram; vao: WebGLVertexArrayObject; uniforms: Record<string, WebGLUniformLocation | null> };
  let map: MapLibreMap | null = null;
  let gl: WebGL2RenderingContext | null = null;
  let cornerBuffer: WebGLBuffer | null = null;
  let instanceBuffer: WebGLBuffer | null = null;
  const programs = new Map<string, Program>();
  const unsupported = new Set<string>();
  let geometry: FlowGeometry | null = null;
  let uploaded = false;
  let sampleQueue: number[] = [];
  let sampleCursor = 0;
  let terrainWasOn = false;

  const queueTerrainSamples = () => {
    if (!geometry || !map) { sampleQueue = []; return; }
    const center = map.getCenter();
    // Nearest vertices first, so the foreground settles onto the terrain first.
    sampleQueue = geometry.vertices.map((_, index) => index)
      .sort((a, b) => {
        const va = geometry!.vertices[a], vb = geometry!.vertices[b];
        return Math.hypot(va.lng - center.lng, va.lat - center.lat) - Math.hypot(vb.lng - center.lng, vb.lat - center.lat);
      });
    sampleCursor = 0;
  };
  const markDirty = () => queueTerrainSamples();
  const markDirtyForTerrain = (event: { sourceId?: string }) => {
    if (map && event.sourceId && event.sourceId === map.getTerrain()?.source) queueTerrainSamples();
  };

  const sampleTerrain = () => {
    if (!map || !geometry) return false;
    const terrainOn = Boolean(map.getTerrain());
    if (!terrainOn) {
      if (terrainWasOn) {
        // Back to a flat map: drop every sampled height.
        for (const vertex of geometry.vertices) for (const slot of vertex.slots) geometry.segments[slot] = 0;
        terrainWasOn = false;
        return true;
      }
      return false;
    }
    if (!terrainWasOn) { terrainWasOn = true; queueTerrainSamples(); }
    if (sampleCursor >= sampleQueue.length) return false;
    const end = Math.min(sampleQueue.length, sampleCursor + SAMPLES_PER_FRAME);
    for (; sampleCursor < end; sampleCursor += 1) {
      const vertex = geometry.vertices[sampleQueue[sampleCursor]];
      const sampled = map.queryTerrainElevation([vertex.lng, vertex.lat]);
      if (sampled === null || !Number.isFinite(sampled)) continue;
      for (const slot of vertex.slots) geometry.segments[slot] = sampled;
    }
    return true;
  };

  const compile = (context: WebGL2RenderingContext, type: number, source: string) => {
    const shader = context.createShader(type)!;
    context.shaderSource(shader, source);
    context.compileShader(shader);
    if (!context.getShaderParameter(shader, context.COMPILE_STATUS)) throw new Error("Water-flow shader failed to compile");
    return shader;
  };
  const link = (context: WebGL2RenderingContext, vertexSource: string): Program => {
    const program = context.createProgram()!;
    const vertex = compile(context, context.VERTEX_SHADER, vertexSource);
    const fragment = compile(context, context.FRAGMENT_SHADER, FRAGMENT_SHADER);
    context.attachShader(program, vertex);
    context.attachShader(program, fragment);
    context.linkProgram(program);
    context.deleteShader(vertex);
    context.deleteShader(fragment);
    if (!context.getProgramParameter(program, context.LINK_STATUS)) throw new Error("Water-flow program failed to link");
    const vao = context.createVertexArray()!;
    context.bindVertexArray(vao);
    context.bindBuffer(context.ARRAY_BUFFER, cornerBuffer);
    const corner = context.getAttribLocation(program, "a_corner");
    if (corner >= 0) { context.enableVertexAttribArray(corner); context.vertexAttribPointer(corner, 2, context.FLOAT, false, 0, 0); }
    context.bindBuffer(context.ARRAY_BUFFER, instanceBuffer);
    const stride = FLOW_SEGMENT_FLOATS * 4;
    for (const [name, size, offset] of [["i_a", 3, 0], ["i_b", 3, 3], ["i_dist", 2, 6], ["i_cue", 4, 8]] as const) {
      const location = context.getAttribLocation(program, name);
      if (location < 0) continue;
      context.enableVertexAttribArray(location);
      context.vertexAttribPointer(location, size, context.FLOAT, false, stride, offset * 4);
      context.vertexAttribDivisor(location, 1);
    }
    context.bindVertexArray(null);
    return { program, vao, uniforms: Object.fromEntries(UNIFORMS.map((name) => [name, context.getUniformLocation(program, name)])) };
  };

  const layer: WaterFlowLayer = {
    id: options.id,
    type: "custom",
    renderingMode: "3d",
    get segmentCount() { return geometry?.count ?? 0; },
    setGeometry(next) {
      geometry = next;
      uploaded = false;
      terrainWasOn = false;
      queueTerrainSamples();
      try { map?.triggerRepaint(); } catch { /* removed */ }
    },
    onAdd(nextMap, context) {
      map = nextMap;
      gl = context;
      cornerBuffer = context.createBuffer();
      context.bindBuffer(context.ARRAY_BUFFER, cornerBuffer);
      context.bufferData(context.ARRAY_BUFFER, new Float32Array([0, -1, 0, 1, 1, -1, 1, 1]), context.STATIC_DRAW);
      instanceBuffer = context.createBuffer();
      programs.set("mercator", link(context, MERCATOR_VERTEX_SHADER));
      nextMap.on("moveend", markDirty);
      nextMap.on("terrain", markDirty);
      nextMap.on("sourcedata", markDirtyForTerrain);
    },
    onRemove(oldMap, context) {
      oldMap.off("moveend", markDirty);
      oldMap.off("terrain", markDirty);
      oldMap.off("sourcedata", markDirtyForTerrain);
      for (const program of programs.values()) { context.deleteVertexArray(program.vao); context.deleteProgram(program.program); }
      programs.clear();
      if (cornerBuffer) context.deleteBuffer(cornerBuffer);
      if (instanceBuffer) context.deleteBuffer(instanceBuffer);
      cornerBuffer = instanceBuffer = null; map = null; gl = null;
    },
    render(context, input: CustomRenderMethodInput) {
      if (!map || !gl || !instanceBuffer || !geometry || !geometry.count) return;
      // Terrain heights arrive over a few frames; keep redrawing until they settle.
      let changed = false;
      try { changed = sampleTerrain(); } catch { sampleQueue = []; }
      if (!uploaded || changed) {
        context.bindBuffer(context.ARRAY_BUFFER, instanceBuffer);
        context.bufferData(context.ARRAY_BUFFER, geometry.segments.subarray(0, geometry.count * FLOW_SEGMENT_FLOATS), context.DYNAMIC_DRAW);
        uploaded = true;
      }
      if (changed) map.triggerRepaint();
      const variant = input.shaderData?.variantName === "globe" ? "globe" : "mercator";
      if (unsupported.has(variant)) return;
      let program = programs.get(variant);
      if (!program) {
        try { program = link(context, globeVertexShader(input.shaderData.vertexShaderPrelude, input.shaderData.define)); } catch { unsupported.add(variant); return; }
        programs.set(variant, program);
      }
      const zoom = map.getZoom();
      const center = map.getCenter();
      const pixelRatio = typeof window === "undefined" ? 1 : Math.min(window.devicePixelRatio || 1, 2);
      const exaggeration = Number(map.getTerrain()?.exaggeration ?? 0);
      const { uniforms } = program;
      context.useProgram(program.program);
      if (variant === "globe") {
        const projection = input.defaultProjectionData;
        context.uniformMatrix4fv(uniforms.u_projection_matrix, false, Float32Array.from(projection.mainMatrix as ArrayLike<number>));
        context.uniformMatrix4fv(uniforms.u_projection_fallback_matrix, false, Float32Array.from(projection.fallbackMatrix as ArrayLike<number>));
        context.uniform4f(uniforms.u_projection_tile_mercator_coords, ...projection.tileMercatorCoords);
        context.uniform4f(uniforms.u_projection_clipping_plane, ...projection.clippingPlane);
        context.uniform1f(uniforms.u_projection_transition, projection.projectionTransition);
      } else {
        context.uniformMatrix4fv(uniforms.u_matrix, false, Float32Array.from(input.modelViewProjectionMatrix as ArrayLike<number>));
        context.uniform1f(uniforms.u_world_size, 512 * 2 ** zoom);
      }
      const palette = options.palette();
      context.uniform2f(uniforms.u_viewport, context.drawingBufferWidth, context.drawingBufferHeight);
      context.uniform1f(uniforms.u_half_width, flowHalfWidth(zoom) * pixelRatio);
      // A few metres above the ground keeps the ribbon out of the terrain surface.
      context.uniform1f(uniforms.u_lift, exaggeration > 0 ? 4 * exaggeration : 0);
      context.uniform1f(uniforms.u_m_per_px, metersPerPixel(center.lat, zoom) / pixelRatio);
      context.uniform1f(uniforms.u_time, options.clock() ?? 0);
      context.uniform1f(uniforms.u_speed_px, FLOW_SPEED_PX * pixelRatio);
      context.uniform1f(uniforms.u_spacing_px, FLOW_SPACING_PX * pixelRatio);
      context.uniform3fv(uniforms.u_base, [...palette.base]);
      context.uniform3fv(uniforms.u_streak, [...palette.streak]);
      context.uniform3fv(uniforms.u_tints, palette.tints.flatMap((tint) => [...tint]));
      context.uniform1f(uniforms.u_opacity, palette.opacity);
      context.enable(context.BLEND);
      context.blendFunc(context.ONE, context.ONE_MINUS_SRC_ALPHA);
      context.depthMask(false);
      context.disable(context.CULL_FACE);
      context.bindVertexArray(program.vao);
      context.drawArraysInstanced(context.TRIANGLE_STRIP, 0, 4, geometry.count);
      context.bindVertexArray(null);
      context.depthMask(true);
    },
  };
  return layer;
}
