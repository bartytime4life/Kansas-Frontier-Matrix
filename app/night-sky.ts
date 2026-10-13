import type { CustomLayerInterface, CustomRenderMethodInput, Map as MapLibreMap } from "./maplibre-seam";

/**
 * A real night sky drawn beneath every map layer: the brightest Hipparcos
 * stars at their true positions for the current time, a stylized Milky Way
 * glow along the galactic plane, and (from orbit) the Sun.
 *
 * - On the globe the sky surrounds the planet, aligned with the Earth's
 *   rotation, so Kansas turns under the same stars it sees tonight.
 * - On tilted maps at night or dusk, stars rise above the horizon at their
 *   altitude and azimuth over the map center, twinkle near the horizon and
 *   fade into the haze.
 *
 * Display only. Star positions come from the bundled catalog (see
 * docs/night-sky.md); the Milky Way and Sun glow are illustrative, nothing
 * here is queryable, and a GPU or shader failure removes the sky without
 * affecting the map.
 */

export type Vec3 = readonly [number, number, number];
/** Row-major 3×3 matrix. */
export type Mat3 = readonly [number, number, number, number, number, number, number, number, number];
export type NightSkyCatalog = Readonly<{ count: number; stars: readonly (number | null)[] }>;

const RADIANS = Math.PI / 180;
const normalizeDegrees = (value: number) => ((value % 360) + 360) % 360;
const clamp = (value: number, minimum: number, maximum: number) => Math.max(minimum, Math.min(maximum, value));

// ---------------------------------------------------------------------------
// Astronomy
// ---------------------------------------------------------------------------

export const julianDate = (epochMs: number): number => epochMs / 86_400_000 + 2_440_587.5;

/** Greenwich mean sidereal time in degrees (IAU 1982, about 0.1 s over decades). */
export const greenwichSiderealDegrees = (epochMs: number): number =>
  normalizeDegrees(280.46061837 + 360.98564736629 * (julianDate(epochMs) - 2_451_545));

/** Unit vector toward right ascension / declination (J2000 degrees). */
export const equatorialVector = (raDegrees: number, decDegrees: number): Vec3 => {
  const ra = raDegrees * RADIANS, dec = decDegrees * RADIANS;
  return [Math.cos(dec) * Math.cos(ra), Math.cos(dec) * Math.sin(ra), Math.sin(dec)];
};

/** Low-precision apparent Sun (Astronomical Almanac), good to about 0.01°. */
export function sunEquatorial(epochMs: number): Readonly<{ ra: number; dec: number }> {
  const n = julianDate(epochMs) - 2_451_545;
  const meanLongitude = 280.46 + 0.9856474 * n;
  const anomaly = (357.528 + 0.9856003 * n) * RADIANS;
  const lambda = (meanLongitude + 1.915 * Math.sin(anomaly) + 0.02 * Math.sin(2 * anomaly)) * RADIANS;
  const obliquity = (23.439 - 0.0000004 * n) * RADIANS;
  return {
    ra: normalizeDegrees(Math.atan2(Math.cos(obliquity) * Math.sin(lambda), Math.cos(lambda)) / RADIANS),
    dec: Math.asin(Math.sin(obliquity) * Math.sin(lambda)) / RADIANS,
  };
}

const multiply3 = (a: Mat3, b: Mat3): Mat3 => {
  const out: number[] = [];
  for (let row = 0; row < 3; row += 1) for (let column = 0; column < 3; column += 1) {
    out.push(a[row * 3] * b[column] + a[row * 3 + 1] * b[3 + column] + a[row * 3 + 2] * b[6 + column]);
  }
  return out as unknown as Mat3;
};
export const transform3 = (m: Mat3, v: Vec3): Vec3 => [
  m[0] * v[0] + m[1] * v[1] + m[2] * v[2],
  m[3] * v[0] + m[4] * v[1] + m[5] * v[2],
  m[6] * v[0] + m[7] * v[1] + m[8] * v[2],
];
const transpose3 = (m: Mat3): Mat3 => [m[0], m[3], m[6], m[1], m[4], m[7], m[2], m[5], m[8]];
const scaleRows = (m: Mat3, x: number, y: number, z: number): Mat3 => [m[0] * x, m[1] * x, m[2] * x, m[3] * y, m[4] * y, m[5] * y, m[6] * z, m[7] * z, m[8] * z];

/** Equatorial (J2000) → Earth-fixed (x toward 0° longitude, z toward north). */
export const equatorialToEarthFixed = (siderealDegrees: number): Mat3 => {
  const theta = siderealDegrees * RADIANS;
  return [Math.cos(theta), Math.sin(theta), 0, -Math.sin(theta), Math.cos(theta), 0, 0, 0, 1];
};

/** Earth-fixed → local east, north, up at a longitude and latitude. */
export const earthFixedToLocal = (longitude: number, latitude: number): Mat3 => {
  const lng = longitude * RADIANS, lat = latitude * RADIANS;
  return [
    -Math.sin(lng), Math.cos(lng), 0,
    -Math.sin(lat) * Math.cos(lng), -Math.sin(lat) * Math.sin(lng), Math.cos(lat),
    Math.cos(lat) * Math.cos(lng), Math.cos(lat) * Math.sin(lng), Math.sin(lat),
  ];
};

/** Earth-fixed → MapLibre's globe space, which projects positions as
 * (sin λ cos φ, sin φ, cos λ cos φ) on the unit sphere. */
export const EARTH_FIXED_TO_GLOBE: Mat3 = [0, 1, 0, 0, 0, 1, 1, 0, 0];

/** Equatorial (J2000) → galactic (Hipparcos introduction, §1.5.3). */
export const EQUATORIAL_TO_GALACTIC: Mat3 = [
  -0.0548755604, -0.873437090, -0.4838350155,
  0.4941094279, -0.4448296300, 0.7469822445,
  -0.8676661490, -0.1980763734, 0.4559837762,
];

/** Altitude and azimuth (degrees, azimuth clockwise from north) of a sky position. */
export function horizontalPosition(raDegrees: number, decDegrees: number, epochMs: number, longitude: number, latitude: number): Readonly<{ altitude: number; azimuth: number }> {
  const local = transform3(multiply3(earthFixedToLocal(longitude, latitude), equatorialToEarthFixed(greenwichSiderealDegrees(epochMs))), equatorialVector(raDegrees, decDegrees));
  return { altitude: Math.asin(clamp(local[2], -1, 1)) / RADIANS, azimuth: normalizeDegrees(Math.atan2(local[0], local[1]) / RADIANS) };
}

export function galacticPosition(raDegrees: number, decDegrees: number): Readonly<{ l: number; b: number }> {
  const g = transform3(EQUATORIAL_TO_GALACTIC, equatorialVector(raDegrees, decDegrees));
  return { l: normalizeDegrees(Math.atan2(g[1], g[0]) / RADIANS), b: Math.asin(clamp(g[2], -1, 1)) / RADIANS };
}

// ---------------------------------------------------------------------------
// Star appearance
// ---------------------------------------------------------------------------

/** B−V colour index → display RGB (Ballesteros temperature, blackbody fit). */
export function starColor(bv: number | null): Vec3 {
  if (bv === null || !Number.isFinite(bv)) return [1, 0.97, 0.92];
  const index = clamp(bv, -0.4, 2);
  const kelvin = 4600 * (1 / (0.92 * index + 1.7) + 1 / (0.92 * index + 0.62));
  const t = kelvin / 100;
  const red = t <= 66 ? 255 : 329.698727446 * (t - 60) ** -0.1332047592;
  const green = t <= 66 ? 99.4708025861 * Math.log(t) - 161.1195681661 : 288.1221695283 * (t - 60) ** -0.0755148492;
  const blue = t >= 66 ? 255 : t <= 19 ? 0 : 138.5177312231 * Math.log(t - 10) - 305.0447927307;
  // Desaturate toward white: stars read as tinted points, not coloured dots.
  return [red, green, blue].map((channel) => 0.45 + 0.55 * clamp(channel, 0, 255) / 255) as unknown as Vec3;
}

/** Point diameter in CSS pixels and relative brightness for a magnitude. */
export function starAppearance(magnitude: number): Readonly<{ size: number; brightness: number }> {
  const mag = Number.isFinite(magnitude) ? magnitude : 6;
  const strength = clamp((5.8 - mag) / 7.3, 0, 1);
  const flux = 10 ** (-0.4 * (mag - 1));
  return { size: 2.2 + 11 * strength ** 1.5, brightness: clamp(0.38 + 0.7 * Math.sqrt(flux), 0.38, 1.5) };
}

// ---------------------------------------------------------------------------
// Visibility
// ---------------------------------------------------------------------------

/** Below this pitch no supported field of view reaches the horizon. */
export const NIGHT_SKY_MIN_PITCH = 45;
/** Flat maps draw sky only once the horizon nears the top of the frame:
 * pitch plus half the vertical field of view, in degrees. */
export const NIGHT_SKY_HORIZON_ANGLE = 84;
export const DEFAULT_VERTICAL_FOV = 36.87;
export const horizonInView = (pitch: number, verticalFov: number = DEFAULT_VERTICAL_FOV): boolean =>
  Number.isFinite(pitch) && pitch + (Number.isFinite(verticalFov) ? verticalFov : DEFAULT_VERTICAL_FOV) / 2 >= NIGHT_SKY_HORIZON_ANGLE;
export type SkyLightPreset = "night" | "dusk" | "clear";
/** How dark a flat map's sky is for stars; the globe is always seen from space. */
export const SKY_DARKNESS: Readonly<Record<SkyLightPreset, number>> = Object.freeze({ night: 1, dusk: 0.55, clear: 0 });

/** Layer visibility; on flat maps the renderer also skips frames whose horizon is out of view. */
export const nightSkyShouldShow = (enabled: boolean, efficient: boolean, projection: string | undefined, pitch: number, darkness: number): boolean =>
  enabled && !efficient && (projection === "globe" || (darkness > 0 && Number.isFinite(pitch) && pitch >= NIGHT_SKY_MIN_PITCH));

// ---------------------------------------------------------------------------
// Matrices for the renderer
// ---------------------------------------------------------------------------

const EARTH_CIRCUMFERENCE_METERS = 2 * Math.PI * 6_378_137;

export type SkyFrame = Readonly<{
  /** Equatorial direction → the coordinates the map matrix expects (direction, w = 0). */
  equatorialToView: Mat3;
  /** Inverse of equatorialToView, for per-pixel view rays. */
  viewToEquatorial: Mat3;
  /** The observer's zenith in equatorial coordinates (flat maps). */
  zenith: Vec3;
  sun: Vec3;
}>;

/**
 * Mercator custom-layer matrices take world pixels for x/y (y grows south)
 * and metres for z, so a local direction (east, north, up) becomes
 * (east, −north, up × metres-per-pixel).
 */
export function flatSkyFrame(epochMs: number, longitude: number, latitude: number, zoom: number): SkyFrame {
  const local = multiply3(earthFixedToLocal(longitude, latitude), equatorialToEarthFixed(greenwichSiderealDegrees(epochMs)));
  const metersPerPixel = EARTH_CIRCUMFERENCE_METERS * Math.cos(clamp(latitude, -85, 85) * RADIANS) / (512 * 2 ** zoom);
  const sun = sunEquatorial(epochMs);
  return {
    equatorialToView: scaleRows(local, 1, -1, metersPerPixel),
    viewToEquatorial: transpose3(scaleRows(local, 1, -1, 1 / metersPerPixel)),
    zenith: [local[6], local[7], local[8]],
    sun: equatorialVector(sun.ra, sun.dec),
  };
}

export function globeSkyFrame(epochMs: number): SkyFrame {
  const rotation = multiply3(EARTH_FIXED_TO_GLOBE, equatorialToEarthFixed(greenwichSiderealDegrees(epochMs)));
  const sun = sunEquatorial(epochMs);
  return { equatorialToView: rotation, viewToEquatorial: transpose3(rotation), zenith: [0, 0, 1], sun: equatorialVector(sun.ra, sun.dec) };
}

/** General 4×4 inverse (column-major, as WebGL uniforms expect). */
export function invert4(m: ArrayLike<number>): Float32Array | null {
  const a = Array.from({ length: 16 }, (_, index) => Number(m[index]));
  const [a00, a01, a02, a03, a10, a11, a12, a13, a20, a21, a22, a23, a30, a31, a32, a33] = a;
  const b00 = a00 * a11 - a01 * a10, b01 = a00 * a12 - a02 * a10, b02 = a00 * a13 - a03 * a10;
  const b03 = a01 * a12 - a02 * a11, b04 = a01 * a13 - a03 * a11, b05 = a02 * a13 - a03 * a12;
  const b06 = a20 * a31 - a21 * a30, b07 = a20 * a32 - a22 * a30, b08 = a20 * a33 - a23 * a30;
  const b09 = a21 * a32 - a22 * a31, b10 = a21 * a33 - a23 * a31, b11 = a22 * a33 - a23 * a32;
  const determinant = b00 * b11 - b01 * b10 + b02 * b09 + b03 * b08 - b04 * b07 + b05 * b06;
  if (!Number.isFinite(determinant) || determinant === 0) return null;
  const inv = 1 / determinant;
  return new Float32Array([
    (a11 * b11 - a12 * b10 + a13 * b09) * inv, (a02 * b10 - a01 * b11 - a03 * b09) * inv, (a31 * b05 - a32 * b04 + a33 * b03) * inv, (a22 * b04 - a21 * b05 - a23 * b03) * inv,
    (a12 * b08 - a10 * b11 - a13 * b07) * inv, (a00 * b11 - a02 * b08 + a03 * b07) * inv, (a32 * b02 - a30 * b05 - a33 * b01) * inv, (a20 * b05 - a22 * b02 + a23 * b01) * inv,
    (a10 * b10 - a11 * b08 + a13 * b06) * inv, (a01 * b08 - a00 * b10 - a03 * b06) * inv, (a30 * b04 - a31 * b02 + a33 * b00) * inv, (a21 * b02 - a20 * b04 - a23 * b00) * inv,
    (a11 * b07 - a10 * b09 - a12 * b06) * inv, (a00 * b09 - a01 * b07 + a02 * b06) * inv, (a31 * b01 - a30 * b03 - a32 * b00) * inv, (a20 * b03 - a21 * b01 + a22 * b00) * inv,
  ]);
}

/** The camera's position in the matrix's space: the centre of the near plane. */
export function cameraPosition(inverse: ArrayLike<number>): [number, number, number] {
  const w = inverse[11] * -1 + inverse[15];
  return [(inverse[8] * -1 + inverse[12]) / w, (inverse[9] * -1 + inverse[13]) / w, (inverse[10] * -1 + inverse[14]) / w];
}

/** Row-major Mat3 → column-major uniform data. */
const uniform3 = (m: Mat3) => new Float32Array(transpose3(m));

// ---------------------------------------------------------------------------
// Shaders
// ---------------------------------------------------------------------------

const STAR_VERTEX_SHADER = `#version 300 es
uniform mat4 u_matrix;
uniform mat3 u_eq_to_view;
uniform vec3 u_zenith;
uniform vec3 u_sun;
uniform float u_horizon;
uniform float u_sun_glare;
uniform float u_strength;
uniform float u_time;
uniform float u_twinkle;
uniform float u_pixel_ratio;
uniform float u_max_point;
uniform vec3 u_camera;
uniform float u_occlude;
in vec3 a_dir;
in vec3 a_color;
in vec2 a_look;
in float a_phase;
out vec3 v_color;
out float v_bright;
out float v_spikes;
out float v_size;
void main() {
  vec3 view = u_eq_to_view * a_dir;
  vec4 clip = u_matrix * vec4(view, 0.0);
  // From orbit, the planet hides every star whose line of sight meets it.
  float toward = dot(u_camera, view);
  bool behindPlanet = u_occlude > 0.5 && toward < 0.0 && toward * toward - (dot(u_camera, u_camera) - 1.0) > 0.0;
  float elevation = dot(a_dir, u_zenith);
  float horizon = mix(1.0, smoothstep(0.0, 0.22, elevation), u_horizon);
  // Scintillation grows toward the horizon, where starlight crosses more air.
  float air = 1.0 - smoothstep(0.0, 0.6, elevation);
  float twinkle = 1.0 + u_twinkle * u_horizon * (0.1 + 0.5 * air) * sin(u_time * (5.0 + a_phase * 7.0) + a_phase * 61.0);
  float glare = 1.0 - u_sun_glare * exp(-pow(acos(clamp(dot(a_dir, u_sun), -1.0, 1.0)) / 0.32, 2.0));
  v_bright = a_look.y * u_strength * horizon * glare * max(twinkle, 0.15);
  // Low stars redden like the sun at dusk.
  v_color = mix(a_color, a_color * vec3(1.0, 0.8, 0.6), u_horizon * air * 0.7);
  float size = min(a_look.x * u_pixel_ratio * (0.85 + 0.15 * twinkle), u_max_point);
  v_spikes = smoothstep(9.0, 12.0, a_look.x);
  v_size = size;
  if (clip.w <= 0.0 || v_bright < 0.01 || behindPlanet) {
    gl_Position = vec4(2.0, 2.0, 2.0, 1.0);
    gl_PointSize = 1.0;
    return;
  }
  gl_Position = vec4(clip.xy, clip.w * 0.99999, clip.w);
  gl_PointSize = size;
}`;

const STAR_FRAGMENT_SHADER = `#version 300 es
precision highp float;
in vec3 v_color;
in float v_bright;
in float v_spikes;
in float v_size;
out vec4 fragColor;
void main() {
  vec2 p = gl_PointCoord * 2.0 - 1.0;
  float r2 = dot(p, p);
  if (r2 > 1.0) discard;
  // Small points stay solid; large ones resolve into a sharp core and halo.
  float sharpness = mix(1.2, 18.0, smoothstep(2.5, 14.0, v_size));
  float core = exp(-r2 * sharpness);
  float halo = exp(-r2 * 3.5) * 0.3 * smoothstep(4.0, 10.0, v_size);
  float rays = (exp(-abs(p.x) * 26.0) + exp(-abs(p.y) * 26.0)) * (1.0 - sqrt(r2)) * 0.55 * v_spikes;
  float light = clamp((core + halo + rays) * v_bright, 0.0, 1.0);
  fragColor = vec4(v_color * light, light);
}`;

const BAND_VERTEX_SHADER = `#version 300 es
in vec2 a_ndc;
out vec2 v_ndc;
void main() {
  v_ndc = a_ndc;
  gl_Position = vec4(a_ndc, 0.99999, 1.0);
}`;

const BAND_FRAGMENT_SHADER = `#version 300 es
precision highp float;
uniform mat4 u_inverse;
uniform mat3 u_view_to_eq;
uniform mat3 u_eq_to_gal;
uniform vec3 u_zenith;
uniform vec3 u_sun;
uniform float u_horizon;
uniform float u_strength;
uniform float u_sun_strength;
uniform float u_occlude;
in vec2 v_ndc;
out vec4 fragColor;

float hash(vec3 p) {
  p = fract(p * 0.3183099 + 0.1);
  p *= 17.0;
  return fract(p.x * p.y * p.z * (p.x + p.y + p.z));
}
float noise(vec3 x) {
  vec3 i = floor(x);
  vec3 f = fract(x);
  f = f * f * (3.0 - 2.0 * f);
  return mix(mix(mix(hash(i), hash(i + vec3(1, 0, 0)), f.x), mix(hash(i + vec3(0, 1, 0)), hash(i + vec3(1, 1, 0)), f.x), f.y),
             mix(mix(hash(i + vec3(0, 0, 1)), hash(i + vec3(1, 0, 1)), f.x), mix(hash(i + vec3(0, 1, 1)), hash(i + vec3(1, 1, 1)), f.x), f.y), f.z);
}
float clouds(vec3 p) {
  return 0.55 * noise(p) + 0.28 * noise(p * 2.03 + 11.0) + 0.17 * noise(p * 4.11 + 23.0);
}

void main() {
  vec4 far = u_inverse * vec4(v_ndc, 1.0, 1.0);
  vec4 near = u_inverse * vec4(v_ndc, -1.0, 1.0);
  vec3 origin = near.xyz / near.w;
  vec3 ray = far.xyz / far.w - origin;
  if (u_occlude > 0.5) {
    vec3 direction = normalize(ray);
    float toward = dot(origin, direction);
    if (toward < 0.0 && toward * toward - (dot(origin, origin) - 1.0) > 0.0) discard;
  }
  vec3 eq = normalize(u_view_to_eq * ray);
  float elevation = dot(eq, u_zenith);
  float horizon = mix(1.0, smoothstep(-0.01, 0.3, elevation), u_horizon);
  if (horizon <= 0.0) discard;

  // Milky Way: a soft band on the galactic plane, broadest and warmest toward
  // the centre in Sagittarius, mottled by star clouds and split by the Great Rift.
  vec3 g = u_eq_to_gal * eq;
  float b = asin(clamp(g.z, -1.0, 1.0));
  float l = atan(g.y, g.x);
  float core = exp(-l * l / 1.1);
  float width = mix(0.085, 0.2, core);
  float band = exp(-(b * b) / (width * width)) * (0.42 + 0.58 * exp(-l * l / 3.2));
  float bulge = exp(-l * l / 0.32) * exp(-b * b / 0.022);
  float rift = exp(-pow((b - 0.035) / 0.03, 2.0)) * smoothstep(-0.15, 0.2, l) * (1.0 - smoothstep(0.85, 1.35, l));
  float texture = clouds(eq * 9.0);
  float glow = (band * (0.35 + 0.9 * texture) + bulge * 0.85) * (1.0 - 0.7 * rift);
  vec3 tint = mix(vec3(0.56, 0.64, 0.9), vec3(1.0, 0.85, 0.66), clamp(bulge * 1.6 + core * 0.35, 0.0, 1.0));
  vec3 color = tint * pow(glow, 1.15) * 0.55 * u_strength * horizon;

  // The Sun from orbit: a white disc, a tight corona and a wide soft glare.
  float angle = acos(clamp(dot(eq, u_sun), -1.0, 1.0));
  float disc = 1.0 - smoothstep(0.0075, 0.011, angle);
  float corona = exp(-angle * angle / 0.0012) * 0.95 + exp(-angle / 0.11) * 0.3;
  color += u_sun_strength * vec3(1.0, 0.95, 0.86) * (disc * 1.4 + corona);

  float alpha = clamp(max(color.r, max(color.g, color.b)), 0.0, 1.0);
  fragColor = vec4(min(color, vec3(1.0)), alpha);
}`;

// ---------------------------------------------------------------------------
// Layer
// ---------------------------------------------------------------------------

export type NightSkyLayerOptions = Readonly<{
  id: string;
  catalog: () => NightSkyCatalog | null;
  /** Darkness of a flat map's sky, 0–1. */
  darkness: () => number;
  /** Seconds for the twinkle clock, or null to hold the stars still. */
  clock: () => number | null;
  now?: () => number;
}>;

const STAR_FLOATS = 9;

/** Packs catalog stars as direction, colour, size, brightness and twinkle phase. */
export function packStars(catalog: NightSkyCatalog): Float32Array {
  const count = Math.floor(catalog.stars.length / 4);
  const data = new Float32Array(count * STAR_FLOATS);
  for (let index = 0; index < count; index += 1) {
    const [ra, dec, mag, bv] = catalog.stars.slice(index * 4, index * 4 + 4) as [number, number, number, number | null];
    const direction = equatorialVector(ra, dec);
    const color = starColor(bv);
    const look = starAppearance(mag);
    data.set([...direction, ...color, look.size, look.brightness, ((index * 0.6180339887) % 1)], index * STAR_FLOATS);
  }
  return data;
}

type Program = { program: WebGLProgram; vao: WebGLVertexArrayObject; uniforms: Record<string, WebGLUniformLocation | null> };

export function createNightSkyLayer(options: NightSkyLayerOptions): CustomLayerInterface {
  let map: MapLibreMap | null = null;
  let stars: Program | null = null;
  let band: Program | null = null;
  let starBuffer: WebGLBuffer | null = null;
  let bandBuffer: WebGLBuffer | null = null;
  let starCount = 0;
  let maxPoint = 64;
  const now = options.now ?? Date.now;

  const compile = (gl: WebGL2RenderingContext, type: number, source: string) => {
    const shader = gl.createShader(type)!;
    gl.shaderSource(shader, source);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) throw new Error("Night-sky shader failed to compile");
    return shader;
  };
  const link = (gl: WebGL2RenderingContext, vertexSource: string, fragmentSource: string, uniforms: readonly string[], buffer: WebGLBuffer, attributes: readonly (readonly [string, number, number])[], stride: number): Program => {
    const program = gl.createProgram()!;
    const vertex = compile(gl, gl.VERTEX_SHADER, vertexSource);
    const fragment = compile(gl, gl.FRAGMENT_SHADER, fragmentSource);
    gl.attachShader(program, vertex);
    gl.attachShader(program, fragment);
    gl.linkProgram(program);
    gl.deleteShader(vertex);
    gl.deleteShader(fragment);
    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) throw new Error("Night-sky program failed to link");
    const vao = gl.createVertexArray()!;
    gl.bindVertexArray(vao);
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    for (const [name, size, offset] of attributes) {
      const location = gl.getAttribLocation(program, name);
      if (location < 0) continue;
      gl.enableVertexAttribArray(location);
      gl.vertexAttribPointer(location, size, gl.FLOAT, false, stride * 4, offset * 4);
    }
    gl.bindVertexArray(null);
    return { program, vao, uniforms: Object.fromEntries(uniforms.map((name) => [name, gl.getUniformLocation(program, name)])) };
  };

  const ensureStars = (gl: WebGL2RenderingContext) => {
    if (stars || !starBuffer) return;
    const catalog = options.catalog();
    if (!catalog) return;
    const data = packStars(catalog);
    gl.bindBuffer(gl.ARRAY_BUFFER, starBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, data, gl.STATIC_DRAW);
    starCount = data.length / STAR_FLOATS;
    stars = link(gl, STAR_VERTEX_SHADER, STAR_FRAGMENT_SHADER,
      ["u_matrix", "u_eq_to_view", "u_zenith", "u_sun", "u_horizon", "u_sun_glare", "u_strength", "u_time", "u_twinkle", "u_pixel_ratio", "u_max_point", "u_camera", "u_occlude"],
      starBuffer, [["a_dir", 3, 0], ["a_color", 3, 3], ["a_look", 2, 6], ["a_phase", 1, 8]], STAR_FLOATS);
  };

  return {
    id: options.id,
    type: "custom",
    renderingMode: "2d",
    onAdd(nextMap, gl) {
      map = nextMap;
      const range = gl.getParameter(gl.ALIASED_POINT_SIZE_RANGE) as Float32Array | null;
      maxPoint = Math.max(1, Math.min(64, Number(range?.[1] ?? 64)));
      starBuffer = gl.createBuffer();
      bandBuffer = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, bandBuffer);
      // One oversized triangle covers the viewport.
      gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
      band = link(gl, BAND_VERTEX_SHADER, BAND_FRAGMENT_SHADER,
        ["u_inverse", "u_view_to_eq", "u_eq_to_gal", "u_zenith", "u_sun", "u_horizon", "u_strength", "u_sun_strength", "u_occlude"],
        bandBuffer, [["a_ndc", 2, 0]], 2);
    },
    onRemove(_oldMap, gl) {
      for (const bundle of [stars, band]) if (bundle) { gl.deleteVertexArray(bundle.vao); gl.deleteProgram(bundle.program); }
      if (starBuffer) gl.deleteBuffer(starBuffer);
      if (bandBuffer) gl.deleteBuffer(bandBuffer);
      stars = band = null; starBuffer = bandBuffer = null; map = null;
    },
    render(gl, input: CustomRenderMethodInput) {
      if (!map || !band) return;
      const globe = input.shaderData?.variantName === "globe";
      const transition = globe ? clamp(Number(input.defaultProjectionData?.projectionTransition ?? 1), 0, 1) : 0;
      const strength = globe ? transition ** 2 : clamp(options.darkness(), 0, 1);
      if (strength <= 0.01) return;
      // Every field-of-view path is covered by checking the live camera here.
      if (!globe && !horizonInView(map.getPitch(), map.getVerticalFieldOfView())) return;
      const epochMs = now();
      const center = map.getCenter();
      const frame = globe ? globeSkyFrame(epochMs) : flatSkyFrame(epochMs, center.lng, center.lat, map.getZoom());
      // Invert MapLibre's float64 matrix before narrowing it for the GPU.
      const source = (globe ? input.defaultProjectionData.mainMatrix : input.modelViewProjectionMatrix) as ArrayLike<number>;
      const matrix = Float32Array.from(source);
      const inverse = invert4(source);
      if (!inverse) return;
      ensureStars(gl);

      gl.enable(gl.BLEND);
      gl.blendFunc(gl.ONE, gl.ONE);
      gl.disable(gl.DEPTH_TEST);
      gl.depthMask(false);
      gl.disable(gl.CULL_FACE);

      gl.useProgram(band.program);
      gl.uniformMatrix4fv(band.uniforms.u_inverse, false, inverse);
      gl.uniformMatrix3fv(band.uniforms.u_view_to_eq, false, uniform3(frame.viewToEquatorial));
      gl.uniformMatrix3fv(band.uniforms.u_eq_to_gal, false, uniform3(EQUATORIAL_TO_GALACTIC));
      gl.uniform3fv(band.uniforms.u_zenith, [...frame.zenith]);
      gl.uniform3fv(band.uniforms.u_sun, [...frame.sun]);
      gl.uniform1f(band.uniforms.u_horizon, globe ? 0 : 1);
      gl.uniform1f(band.uniforms.u_strength, strength);
      gl.uniform1f(band.uniforms.u_sun_strength, globe ? strength : 0);
      gl.uniform1f(band.uniforms.u_occlude, globe ? 1 : 0);
      gl.bindVertexArray(band.vao);
      gl.drawArrays(gl.TRIANGLES, 0, 3);

      if (stars && starCount) {
        gl.useProgram(stars.program);
        gl.uniformMatrix4fv(stars.uniforms.u_matrix, false, matrix);
        gl.uniformMatrix3fv(stars.uniforms.u_eq_to_view, false, uniform3(frame.equatorialToView));
        gl.uniform3fv(stars.uniforms.u_zenith, [...frame.zenith]);
        gl.uniform3fv(stars.uniforms.u_sun, [...frame.sun]);
        gl.uniform1f(stars.uniforms.u_horizon, globe ? 0 : 1);
        gl.uniform1f(stars.uniforms.u_sun_glare, globe ? 1 : 0);
        gl.uniform1f(stars.uniforms.u_strength, strength);
        const time = options.clock();
        gl.uniform1f(stars.uniforms.u_time, time ?? 0);
        gl.uniform1f(stars.uniforms.u_twinkle, time === null ? 0 : 1);
        gl.uniform1f(stars.uniforms.u_pixel_ratio, typeof window === "undefined" ? 1 : Math.min(window.devicePixelRatio || 1, 2));
        gl.uniform1f(stars.uniforms.u_max_point, maxPoint);
        gl.uniform3fv(stars.uniforms.u_camera, cameraPosition(inverse));
        gl.uniform1f(stars.uniforms.u_occlude, globe ? 1 : 0);
        gl.bindVertexArray(stars.vao);
        gl.drawArrays(gl.POINTS, 0, starCount);
      }
      gl.bindVertexArray(null);
      gl.depthMask(true);
    },
  };
}
