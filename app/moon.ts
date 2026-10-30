import { centralOffset, clock } from "./sun-chart";

/**
 * The Moon over a Kansas place: its phases, how much of it is lit, and when it
 * rises and sets. Principal phases come from Meeus, Astronomical Algorithms
 * ch. 49 (periodic and planetary terms; about a minute). The Moon's position
 * for rising, setting and illumination is the Astronomical Almanac's
 * low-precision series (longitude to about 0.3°, latitude 0.2°), which puts
 * moonrise and moonset within a few minutes.
 */

const RAD = Math.PI / 180;
const mod = (v: number, d: number) => ((v % d) + d) % d;
const sin = (deg: number) => Math.sin(deg * RAD), cos = (deg: number) => Math.cos(deg * RAD);
const julian = (ms: number) => ms / 86_400_000 + 2_440_587.5;
const DAY_MS = 86_400_000;

/** ΔT (TT − UT) in seconds, the Espenak–Meeus polynomial for 2005–2050. */
export const deltaT = (year: number) => { const t = year - 2000; return 62.92 + 0.32217 * t + 0.005589 * t * t; };

export type PhaseKind = "new" | "first" | "full" | "last";
const KINDS: readonly PhaseKind[] = ["new", "first", "full", "last"];
export const PHASE_NAMES: Readonly<Record<PhaseKind, string>> = Object.freeze({ new: "New moon", first: "First quarter", full: "Full moon", last: "Last quarter" });

/** The Julian Ephemeris Day of a principal phase: k an integer for new moon, +0.25 first quarter, +0.5 full, +0.75 last (Meeus 49.1 with its corrections). */
export function phaseJde(k: number): number {
  const T = k / 1236.85;
  let jde = 2451550.09766 + 29.530588861 * k + 0.00015437 * T ** 2 - 0.000000150 * T ** 3 + 0.00000000073 * T ** 4;
  const E = 1 - 0.002516 * T - 0.0000074 * T ** 2;
  const M = 2.5534 + 29.10535670 * k - 0.0000014 * T ** 2 - 0.00000011 * T ** 3;
  const Mp = 201.5643 + 385.81693528 * k + 0.0107582 * T ** 2 + 0.00001238 * T ** 3 - 0.000000058 * T ** 4;
  const F = 160.7108 + 390.67050284 * k - 0.0016118 * T ** 2 - 0.00000227 * T ** 3 + 0.000000011 * T ** 4;
  const O = 124.7746 - 1.56375588 * k + 0.0020672 * T ** 2 + 0.00000215 * T ** 3;
  const kind = KINDS[mod(Math.round(k * 4), 4)];
  if (kind === "new" || kind === "full") {
    const c = kind === "new"
      ? [-0.40720, 0.17241, 0.01608, 0.01039, 0.00739, -0.00514, 0.00208]
      : [-0.40614, 0.17302, 0.01614, 0.01043, 0.00734, -0.00515, 0.00209];
    jde += c[0] * sin(Mp) + c[1] * E * sin(M) + c[2] * sin(2 * Mp) + c[3] * sin(2 * F) + c[4] * E * sin(Mp - M) + c[5] * E * sin(Mp + M) + c[6] * E * E * sin(2 * M)
      - 0.00111 * sin(Mp - 2 * F) - 0.00057 * sin(Mp + 2 * F) + 0.00056 * E * sin(2 * Mp + M) - 0.00042 * sin(3 * Mp) + 0.00042 * E * sin(M + 2 * F)
      + 0.00038 * E * sin(M - 2 * F) - 0.00024 * E * sin(2 * Mp - M) - 0.00017 * sin(O) - 0.00007 * sin(Mp + 2 * M) + 0.00004 * sin(2 * Mp - 2 * F)
      + 0.00004 * sin(3 * M) + 0.00003 * sin(Mp + M - 2 * F) + 0.00003 * sin(2 * Mp + 2 * F) - 0.00003 * sin(Mp + M + 2 * F) + 0.00003 * sin(Mp - M + 2 * F)
      - 0.00002 * sin(Mp - M - 2 * F) - 0.00002 * sin(3 * Mp + M) + 0.00002 * sin(4 * Mp);
  } else {
    jde += -0.62801 * sin(Mp) + 0.17172 * E * sin(M) - 0.01183 * E * sin(Mp + M) + 0.00862 * sin(2 * Mp) + 0.00804 * sin(2 * F) + 0.00454 * E * sin(Mp - M)
      + 0.00204 * E * E * sin(2 * M) - 0.00180 * sin(Mp - 2 * F) - 0.00070 * sin(Mp + 2 * F) - 0.00040 * sin(3 * Mp) - 0.00034 * E * sin(2 * Mp - M)
      + 0.00032 * E * sin(M + 2 * F) + 0.00032 * E * sin(M - 2 * F) - 0.00028 * E * E * sin(Mp + 2 * M) + 0.00027 * E * sin(2 * Mp + M) - 0.00017 * sin(O)
      - 0.00005 * sin(Mp - M - 2 * F) + 0.00004 * sin(2 * Mp + 2 * F) - 0.00004 * sin(Mp + M + 2 * F) + 0.00004 * sin(Mp - 2 * M) + 0.00003 * sin(Mp + M - 2 * F)
      + 0.00003 * sin(3 * M) + 0.00002 * sin(2 * Mp - 2 * F) + 0.00002 * sin(Mp - M + 2 * F) - 0.00002 * sin(3 * Mp + M);
    const W = 0.00306 - 0.00038 * E * cos(M) + 0.00026 * cos(Mp) - 0.00002 * cos(Mp - M) + 0.00002 * cos(Mp + M) + 0.00002 * cos(2 * F);
    jde += kind === "first" ? W : -W;
  }
  // The planetary arguments' small corrections, common to all phases.
  const A = [299.77 + 0.107408 * k - 0.009173 * T ** 2, 251.88 + 0.016321 * k, 251.83 + 26.651886 * k, 349.42 + 36.412478 * k, 84.66 + 18.206239 * k,
    141.74 + 53.303771 * k, 207.14 + 2.453732 * k, 154.84 + 7.306860 * k, 34.52 + 27.261239 * k, 207.19 + 0.121824 * k, 291.34 + 1.844379 * k,
    161.72 + 24.198154 * k, 239.56 + 25.513099 * k, 331.55 + 3.592518 * k];
  const a = [0.000325, 0.000165, 0.000164, 0.000126, 0.000110, 0.000062, 0.000060, 0.000056, 0.000047, 0.000042, 0.000040, 0.000037, 0.000035, 0.000023];
  return jde + A.reduce((sum, arg, i) => sum + a[i] * sin(arg), 0);
}
/** A phase's instant (epoch ms, UT). */
export function phaseInstant(k: number): number {
  const tt = (phaseJde(k) - 2_440_587.5) * DAY_MS;
  return tt - deltaT(new Date(tt).getUTCFullYear()) * 1000;
}
export type Phase = Readonly<{ kind: PhaseKind; at: number }>;
/** The next principal phases from an instant, in order. */
export function phasesAfter(fromMs: number, count = 4): Phase[] {
  const date = new Date(fromMs);
  // Start two lunations early: the estimate of k from the date is rough.
  const k = Math.floor(((date.getUTCFullYear() + date.getUTCMonth() / 12) - 2000) * 12.3685) - 2;
  const out: Phase[] = [];
  for (let q = k * 4; out.length < count; q++) {
    const at = phaseInstant(q / 4);
    if (at >= fromMs) out.push({ kind: KINDS[mod(q, 4)], at });
  }
  return out;
}

/** The Sun's apparent ecliptic longitude, degrees (Astronomical Almanac low precision, about 0.01°). */
export function sunLongitude(ms: number): number {
  const d = julian(ms) - 2451545;
  const g = 357.528 + 0.9856003 * d;
  return mod(280.460 + 0.9856474 * d + 1.915 * sin(g) + 0.020 * sin(2 * g), 360);
}
export type MoonPosition = Readonly<{ longitude: number; latitude: number; parallax: number; ra: number; dec: number }>;
/** The Moon's geocentric ecliptic and equatorial position, degrees (Astronomical Almanac low-precision formulae). */
export function moonPosition(ms: number): MoonPosition {
  const T = (julian(ms) - 2451545) / 36525;
  const longitude = mod(218.32 + 481267.881 * T + 6.29 * sin(134.9 + 477198.85 * T) - 1.27 * sin(259.2 - 413335.38 * T) + 0.66 * sin(235.7 + 890534.23 * T)
    + 0.21 * sin(269.9 + 954397.70 * T) - 0.19 * sin(357.5 + 35999.05 * T) - 0.11 * sin(186.6 + 966404.05 * T), 360);
  const latitude = 5.13 * sin(93.3 + 483202.03 * T) + 0.28 * sin(228.2 + 960400.87 * T) - 0.28 * sin(318.3 + 6003.18 * T) - 0.17 * sin(217.6 - 407332.20 * T);
  const parallax = 0.9508 + 0.0518 * cos(134.9 + 477198.85 * T) + 0.0095 * cos(259.2 - 413335.38 * T) + 0.0078 * cos(235.7 + 890534.23 * T) + 0.0028 * cos(269.9 + 954397.70 * T);
  const l = cos(latitude) * cos(longitude), m = 0.9175 * cos(latitude) * sin(longitude) - 0.3978 * sin(latitude), n = 0.3978 * cos(latitude) * sin(longitude) + 0.9175 * sin(latitude);
  return { longitude, latitude, parallax, ra: mod(Math.atan2(m, l) / RAD, 360), dec: Math.asin(n) / RAD };
}
/** The Moon's geocentric altitude above the horizon, degrees, and the altitude its centre has at rising or setting (0.7275 π − 0.5667°). */
export function moonAltitude(ms: number, lat: number, lon: number): { altitude: number; horizon: number } {
  const p = moonPosition(ms);
  const gmst = 280.46061837 + 360.98564736629 * (julian(ms) - 2451545);
  const h = gmst + lon - p.ra;
  return { altitude: Math.asin(sin(lat) * sin(p.dec) + cos(lat) * cos(p.dec) * cos(h)) / RAD, horizon: 0.7275 * p.parallax - 0.5667 };
}
/** The fraction of the Moon's disc lit, and whether it is waxing. */
export function moonIllumination(ms: number): { fraction: number; waxing: boolean; elongation: number } {
  const p = moonPosition(ms);
  const elongation = mod(p.longitude - sunLongitude(ms), 360);
  const psi = Math.acos(cos(p.latitude) * cos(p.longitude - sunLongitude(ms))) / RAD;
  return { fraction: (1 - cos(psi)) / 2, waxing: elongation < 180, elongation };
}

/** Moonrise and moonset within [from, from + 24 h), found on a 10-minute grid and refined by bisection. */
export function moonEvents(fromMs: number, lat: number, lon: number): { rise: number | null; set: number | null } {
  const f = (t: number) => { const a = moonAltitude(t, lat, lon); return a.altitude - a.horizon; };
  const step = 10 * 60_000;
  let rise: number | null = null, set: number | null = null, prev = f(fromMs);
  for (let t = fromMs + step; t <= fromMs + DAY_MS; t += step) {
    const cur = f(t);
    if ((prev < 0) !== (cur < 0)) {
      let lo = t - step, hi = t;
      for (let i = 0; i < 24; i++) { const mid = (lo + hi) / 2; if ((f(mid) < 0) === (prev < 0)) lo = mid; else hi = mid; }
      if (prev < 0 && rise === null) rise = hi; else if (prev >= 0 && set === null) set = hi;
    }
    prev = cur;
  }
  return { rise, set };
}

/** The name for the Moon at an instant: a principal phase within 12 hours, else waxing or waning crescent or gibbous. */
export function phaseName(ms: number): string {
  const near = phasesAfter(ms - DAY_MS, 3).find(p => Math.abs(p.at - ms) <= DAY_MS / 2);
  if (near) return PHASE_NAMES[near.kind];
  const { elongation } = moonIllumination(ms);
  return elongation < 90 ? "Waxing crescent" : elongation < 180 ? "Waxing gibbous" : elongation < 270 ? "Waning gibbous" : "Waning crescent";
}

const DAY = new Intl.DateTimeFormat("en-US", { timeZone: "America/Chicago", month: "short", day: "numeric" });
const at = (ms: number) => { const offset = centralOffset(ms); return clock(new Date(ms).getUTCHours() * 60 + new Date(ms).getUTCMinutes() + new Date(ms).getUTCSeconds() / 60 + offset, offset); };
/** Local midnight (Central) of a Kansas calendar date, as an instant. */
export const centralMidnight = (date: string) => { const noon = Date.parse(`${date}T18:00:00Z`); return Date.parse(`${date}T00:00:00Z`) - centralOffset(noon) * 60_000; };

/** Tonight's line: the Moon's name and lit fraction at 9 PM, and its rising and setting on the day. */
export function moonReading(date: string, lat: number, lon: number): string {
  const midnight = centralMidnight(date);
  const evening = midnight + 21 * 3_600_000;
  const { fraction } = moonIllumination(evening);
  const { rise, set } = moonEvents(midnight, lat, lon);
  const events = [rise === null ? null : { t: rise, text: `rises ${at(rise)}` }, set === null ? null : { t: set, text: `sets ${at(set)}` }]
    .filter((e): e is { t: number; text: string } => e !== null).sort((a, b) => a.t - b.t).map(e => e.text);
  return `Moon tonight: ${phaseName(evening).toLowerCase()}, ${Math.round(fraction * 100)}% lit · ${events.length ? events.join(", ") : "neither rises nor sets today"}`
    + (rise === null && set !== null ? " (no moonrise this day)" : set === null && rise !== null ? " (no moonset this day)" : "");
}
export function phaseList(fromMs: number, count = 4): string {
  return phasesAfter(fromMs, count).map(p => `${PHASE_NAMES[p.kind]} ${DAY.format(p.at)}, ${at(p.at)}`).join(" · ");
}

/**
 * The lit part of a disc as an SVG path: the limb on the lit side (the right
 * while waxing, as seen from the Northern Hemisphere) and the terminator, an
 * ellipse of half-width r·|1 − 2f| bowing toward the lit side for a crescent
 * and away from it when gibbous.
 */
export function moonDiscPath(cx: number, cy: number, r: number, fraction: number, waxing: boolean): string {
  if (fraction <= 0.002) return "";
  const a = r * Math.abs(1 - 2 * fraction);
  const limb = waxing ? 1 : 0, terminator = (fraction <= 0.5) === waxing ? 0 : 1;
  const f = (v: number) => v.toFixed(2);
  return `M${f(cx)},${f(cy - r)}A${f(r)},${f(r)} 0 0 ${limb} ${f(cx)},${f(cy + r)}A${f(a)},${f(r)} 0 0 ${terminator} ${f(cx)},${f(cy - r)}Z`;
}
export type MoonStrip = Readonly<{ width: number; height: number; r: number; discs: readonly Readonly<{ cx: number; cy: number; d: string; date: string; percent: number }>[] }>;
/** The next 30 evenings (9 PM Central) as discs, lit as they will be: two rows of fifteen. */
export function moonStrip(date: string, days = 30): MoonStrip {
  const perRow = 15, width = 260, gap = width / perRow, r = 6.2, rowHeight = 16;
  const start = centralMidnight(date) + 21 * 3_600_000;
  const discs = Array.from({ length: days }, (_, i) => {
    const t = start + i * DAY_MS, { fraction, waxing } = moonIllumination(t), cx = gap * (i % perRow + 0.5), cy = rowHeight * Math.floor(i / perRow) + rowHeight / 2;
    return { cx, cy, d: moonDiscPath(cx, cy, r, fraction, waxing), date: new Date(t - 6 * 3_600_000).toISOString().slice(0, 10), percent: Math.round(fraction * 100) };
  });
  return Object.freeze({ width, height: rowHeight * Math.ceil(days / perRow), r, discs });
}
