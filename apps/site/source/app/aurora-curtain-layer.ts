import type { CustomLayerInterface, CustomRenderMethodInput, Map as MapLibreMap } from "./maplibre-seam";

/**
 * A glowing curtain of light standing on a closed ring (the simplified Kansas
 * outline). Drawn as a MapLibre custom WebGL2 layer so it can blend
 * additively — bright at the foot, fading upward, with an optional slow
 * shimmer. Wall feet follow the rendered terrain surface when Terrain 3D is on.
 *
 * Presentation only: the ring is the bundled display outline, never a legal
 * or analytical boundary, and nothing here is queryable or reported.
 */

export type CurtainPoint = Readonly<{ lng: number; lat: number; t: number }>;

const RADIANS = Math.PI / 180;

/** Splits each edge into roughly equal steps; t is the perimeter fraction. */
export function densifyRing(ring: readonly (readonly [number, number])[], stepKm = 2.5): CurtainPoint[] {
  const kmPerDegree = 111.32;
  const edges = ring.slice(0, -1).map((start, index) => [start, ring[index + 1]] as const);
  const lengths = edges.map(([[x0, y0], [x1, y1]]) => Math.hypot((x1 - x0) * Math.cos(((y0 + y1) / 2) * RADIANS), y1 - y0) * kmPerDegree);
  const perimeter = lengths.reduce((sum, length) => sum + length, 0) || 1;
  const points: CurtainPoint[] = [];
  let travelled = 0;
  edges.forEach(([[x0, y0], [x1, y1]], index) => {
    const length = lengths[index];
    const steps = Math.max(1, Math.ceil(length / stepKm));
    for (let step = 0; step < steps; step += 1) {
      const fraction = step / steps;
      points.push({ lng: x0 + (x1 - x0) * fraction, lat: y0 + (y1 - y0) * fraction, t: (travelled + length * fraction) / perimeter });
    }
    travelled += length;
  });
  if (points.length) points.push({ ...points[0], t: 1 });
  return points;
}

/** Wall height in metres by zoom: readable statewide, modest up close. */
export const CURTAIN_HEIGHT_STOPS: readonly (readonly [number, number])[] = [[1, 380000], [4, 120000], [6, 52000], [8, 17000], [10, 5200], [12, 1600], [14, 520]];

export function curtainHeightMeters(zoom: number): number {
  const stops = CURTAIN_HEIGHT_STOPS;
  if (!Number.isFinite(zoom) || zoom <= stops[0][0]) return stops[0][1];
  for (let index = 1; index < stops.length; index += 1) {
    const [z1, h1] = stops[index];
    if (zoom <= z1) {
      const [z0, h0] = stops[index - 1];
      // Interpolate in log space so the wall shrinks smoothly with zoom.
      const fraction = (zoom - z0) / (z1 - z0);
      return Math.exp(Math.log(h0) + (Math.log(h1) - Math.log(h0)) * fraction);
    }
  }
  return stops[stops.length - 1][1];
}

const mercatorX = (lng: number) => (180 + lng) / 360;
const mercatorY = (lat: number) => (180 - (180 / Math.PI) * Math.log(Math.tan(Math.PI / 4 + (lat * RADIANS) / 2))) / 360;
/** MapLibre's world size in pixels at a zoom (512 px tiles). */
const worldSize = (zoom: number) => 512 * 2 ** zoom;

const MERCATOR_VERTEX_SHADER = `#version 300 es
uniform mat4 u_matrix;
uniform float u_height;
uniform float u_world_size;
in vec2 a_pos;
in float a_ground;
in float a_side;
in float a_t;
out float v_side;
out float v_t;
void main() {
  v_side = a_side;
  v_t = a_t;
  // MapLibre's mercator view-projection takes world pixels for x/y and metres for z.
  gl_Position = u_matrix * vec4(a_pos * u_world_size, a_ground + a_side * u_height, 1.0);
}`;

// On the globe, MapLibre supplies its projection prelude: positions are
// Mercator 0–1 coordinates and elevation is in metres above the sphere.
const globeVertexShader = (prelude: string, define: string) => `#version 300 es
${prelude}
${define}
uniform float u_height;
in vec2 a_pos;
in float a_ground;
in float a_side;
in float a_t;
out float v_side;
out float v_t;
void main() {
  v_side = a_side;
  v_t = a_t;
  gl_Position = projectTileWithElevation(a_pos, a_ground + a_side * u_height);
}`;

const FRAGMENT_SHADER = `#version 300 es
precision highp float;
uniform float u_time;
uniform float u_intensity;
uniform vec3 u_foot;
uniform vec3 u_crest;
in float v_side;
in float v_t;
out vec4 fragColor;
void main() {
  float fade = pow(1.0 - v_side, 2.2);
  // Broad folds plus finer drifting rays along the perimeter.
  float rays = 0.72 + 0.18 * sin(v_t * 420.0 + u_time * 0.9) + 0.1 * sin(v_t * 2100.0 - u_time * 1.7);
  float footLine = 1.0 - smoothstep(0.0, 0.03, v_side);
  float alpha = clamp(fade * rays * u_intensity + footLine * 0.55, 0.0, 1.0);
  vec3 color = mix(u_foot, u_crest, smoothstep(0.0, 0.85, v_side));
  // Premultiplied output for additive blending.
  fragColor = vec4(color * alpha, alpha);
}`;

const FLOATS_PER_VERTEX = 5;

export type AuroraCurtainOptions = Readonly<{
  id: string;
  ring: readonly (readonly [number, number])[];
  /** Seconds for the shimmer clock, or null to hold the shimmer still. */
  clock: () => number | null;
  foot?: readonly [number, number, number];
  crest?: readonly [number, number, number];
  intensity?: number;
}>;

export function createAuroraCurtainLayer(options: AuroraCurtainOptions): CustomLayerInterface {
  const points = densifyRing(options.ring);
  const vertexCount = points.length * 2;
  const vertices = new Float32Array(vertexCount * FLOATS_PER_VERTEX);
  points.forEach((point, index) => {
    for (let side = 0; side < 2; side += 1) {
      const offset = (index * 2 + side) * FLOATS_PER_VERTEX;
      vertices[offset] = mercatorX(point.lng);
      vertices[offset + 1] = mercatorY(point.lat);
      vertices[offset + 2] = 0;
      vertices[offset + 3] = side;
      vertices[offset + 4] = point.t;
    }
  });

  type ProgramBundle = { program: WebGLProgram; vao: WebGLVertexArrayObject; uniforms: Record<string, WebGLUniformLocation | null> };
  let map: MapLibreMap | null = null;
  let buffer: WebGLBuffer | null = null;
  // One compiled program per projection variant ("mercator", "globe").
  const bundles = new Map<string, ProgramBundle>();
  // Variants whose shader failed on this GPU; skipped instead of retried every frame.
  const unsupported = new Set<string>();
  let groundDirty = true;
  let lastGroundUpdate = 0;
  const markDirty = () => { groundDirty = true; };
  // Only the terrain DEM changes wall feet; other sources load constantly.
  const markDirtyForTerrain = (event: { sourceId?: string }) => {
    if (map && event.sourceId && event.sourceId === map.getTerrain()?.source) groundDirty = true;
  };

  const updateGround = (gl: WebGL2RenderingContext) => {
    if (!map) return;
    const terrain = map.getTerrain();
    // Off-screen elevation queries each walk MapLibre's covering tiles, so only
    // points near the view are re-sampled; the rest keep their last height.
    const bounds = map.getBounds();
    const padLng = (bounds.getEast() - bounds.getWest()) * 0.25;
    const padLat = (bounds.getNorth() - bounds.getSouth()) * 0.25;
    const west = bounds.getWest() - padLng, east = bounds.getEast() + padLng;
    const south = bounds.getSouth() - padLat, north = bounds.getNorth() + padLat;
    points.forEach((point, index) => {
      let elevation = 0;
      if (terrain) {
        if (point.lng < west || point.lng > east || point.lat < south || point.lat > north) return;
        const sampled = map!.queryTerrainElevation([point.lng, point.lat]);
        elevation = sampled !== null && Number.isFinite(sampled) ? sampled : 0;
      }
      vertices[(index * 2) * FLOATS_PER_VERTEX + 2] = elevation;
      vertices[(index * 2 + 1) * FLOATS_PER_VERTEX + 2] = elevation;
    });
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    gl.bufferSubData(gl.ARRAY_BUFFER, 0, vertices);
    groundDirty = false;
  };

  const compile = (gl: WebGL2RenderingContext, type: number, source: string) => {
    const shader = gl.createShader(type)!;
    gl.shaderSource(shader, source);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) throw new Error("Curtain shader failed to compile");
    return shader;
  };

  const UNIFORMS = ["u_matrix", "u_height", "u_world_size", "u_time", "u_intensity", "u_foot", "u_crest",
    "u_projection_matrix", "u_projection_fallback_matrix", "u_projection_tile_mercator_coords", "u_projection_clipping_plane", "u_projection_transition"];
  const createBundle = (gl: WebGL2RenderingContext, vertexSource: string): ProgramBundle => {
    const program = gl.createProgram()!;
    const vertex = compile(gl, gl.VERTEX_SHADER, vertexSource);
    const fragment = compile(gl, gl.FRAGMENT_SHADER, FRAGMENT_SHADER);
    gl.attachShader(program, vertex);
    gl.attachShader(program, fragment);
    gl.linkProgram(program);
    gl.deleteShader(vertex);
    gl.deleteShader(fragment);
    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) throw new Error("Curtain program failed to link");
    const vao = gl.createVertexArray()!;
    gl.bindVertexArray(vao);
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    const stride = FLOATS_PER_VERTEX * 4;
    const attribute = (name: string, size: number, offset: number) => {
      const location = gl.getAttribLocation(program, name);
      if (location < 0) return;
      gl.enableVertexAttribArray(location);
      gl.vertexAttribPointer(location, size, gl.FLOAT, false, stride, offset * 4);
    };
    attribute("a_pos", 2, 0);
    attribute("a_ground", 1, 2);
    attribute("a_side", 1, 3);
    attribute("a_t", 1, 4);
    gl.bindVertexArray(null);
    return { program, vao, uniforms: Object.fromEntries(UNIFORMS.map((name) => [name, gl.getUniformLocation(program, name)])) };
  };

  return {
    id: options.id,
    type: "custom",
    renderingMode: "3d",
    onAdd(nextMap, gl) {
      map = nextMap;
      buffer = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
      gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.DYNAMIC_DRAW);
      bundles.set("mercator", createBundle(gl, MERCATOR_VERTEX_SHADER));
      nextMap.on("moveend", markDirty);
      nextMap.on("terrain", markDirty);
      nextMap.on("sourcedata", markDirtyForTerrain);
    },
    onRemove(oldMap, gl) {
      oldMap.off("moveend", markDirty);
      oldMap.off("terrain", markDirty);
      oldMap.off("sourcedata", markDirtyForTerrain);
      for (const bundle of bundles.values()) { gl.deleteVertexArray(bundle.vao); gl.deleteProgram(bundle.program); }
      bundles.clear();
      if (buffer) gl.deleteBuffer(buffer);
      buffer = null; map = null;
    },
    render(gl, input: CustomRenderMethodInput) {
      if (!map || !buffer) return;
      // Terrain-aware feet; DEM tiles arrive asynchronously, so re-sample at most twice a second.
      const now = performance.now();
      if (groundDirty && now - lastGroundUpdate > 500) {
        lastGroundUpdate = now;
        // A failed sample keeps the previous feet rather than breaking the frame.
        try { updateGround(gl); } catch { groundDirty = false; }
      }
      const exaggeration = Number(map.getTerrain()?.exaggeration ?? 1);
      const height = curtainHeightMeters(map.getZoom()) * (Number.isFinite(exaggeration) && exaggeration > 0 ? Math.min(exaggeration, 1.6) : 1);
      const variant = input.shaderData?.variantName === "globe" ? "globe" : "mercator";
      if (unsupported.has(variant)) return;
      let bundle = bundles.get(variant);
      if (!bundle) {
        // Compiled lazily on first globe frame; a failure disables only this projection's curtain.
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
      if (variant === "globe") {
        const projection = input.defaultProjectionData;
        gl.uniformMatrix4fv(uniforms.u_projection_matrix, false, projection.mainMatrix as Float32Array);
        gl.uniformMatrix4fv(uniforms.u_projection_fallback_matrix, false, projection.fallbackMatrix as Float32Array);
        gl.uniform4f(uniforms.u_projection_tile_mercator_coords, ...projection.tileMercatorCoords);
        gl.uniform4f(uniforms.u_projection_clipping_plane, ...projection.clippingPlane);
        gl.uniform1f(uniforms.u_projection_transition, projection.projectionTransition);
      } else {
        gl.uniformMatrix4fv(uniforms.u_matrix, false, input.modelViewProjectionMatrix as Float32Array);
        gl.uniform1f(uniforms.u_world_size, worldSize(map.getZoom()));
      }
      gl.uniform1f(uniforms.u_height, height);
      gl.uniform1f(uniforms.u_time, options.clock() ?? 0);
      gl.uniform1f(uniforms.u_intensity, options.intensity ?? 0.85);
      gl.uniform3fv(uniforms.u_foot, options.foot ?? [1, 0.8, 0.42]);
      gl.uniform3fv(uniforms.u_crest, options.crest ?? [0.45, 0.85, 0.95]);
      gl.enable(gl.BLEND);
      gl.blendFunc(gl.ONE, gl.ONE);
      gl.depthMask(false);
      gl.disable(gl.CULL_FACE);
      gl.bindVertexArray(vao);
      gl.drawArrays(gl.TRIANGLE_STRIP, 0, vertexCount);
      gl.bindVertexArray(null);
      gl.depthMask(true);
    },
  };
}
