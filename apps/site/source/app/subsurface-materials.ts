import type { Borehole, DepthInterval } from "./subsurface-model";

/** Description-only display palette. Never used to estimate a resource or correlate logs. */
export const MATERIALS = [
  { id: "soil", label: "Soil / dirt", color: "#735039", pattern: "grain" },
  { id: "clay", label: "Clay", color: "#b17759", pattern: "smooth" },
  { id: "sand", label: "Sand", color: "#d8b77b", pattern: "grain" },
  { id: "silt", label: "Silt", color: "#a99478", pattern: "smooth" },
  { id: "gravel", label: "Gravel", color: "#969080", pattern: "pebble" },
  { id: "sandstone", label: "Sandstone", color: "#bc8c56", pattern: "band" },
  { id: "shale", label: "Shale", color: "#646e75", pattern: "band" },
  { id: "limestone", label: "Limestone", color: "#b7b6a5", pattern: "vein" },
  { id: "dolomite", label: "Dolomite", color: "#b5a78e", pattern: "vein" },
  { id: "salt", label: "Salt / halite", color: "#ddd7d0", pattern: "crystal" },
  { id: "gypsum", label: "Gypsum", color: "#d2c9ac", pattern: "crystal" },
  { id: "coal", label: "Coal", color: "#343639", pattern: "band" },
  { id: "ore", label: "Ore / named ore mineral", color: "#95836b", pattern: "crystal" },
  { id: "unknown", label: "Mixed / unclassified", color: "#8b9390", pattern: "plain" },
  { id: "inventory", label: "Core inventory only", color: "#9c92b0", pattern: "plain" },
] as const;
export type MaterialId = typeof MATERIALS[number]["id"];
const words: [MaterialId, RegExp][] = [
  ["soil", /\b(topsoil|soil|dirt)\b/], ["clay", /\bclay\b/], ["sand", /\bsand\b/],
  ["silt", /\bsilt\b/], ["gravel", /\bgravel\b/], ["sandstone", /\bsandstone\b/],
  ["shale", /\bshale\b/], ["limestone", /\blimestone\b/], ["dolomite", /\b(dolomite|dolostone)\b/],
  ["salt", /\b(rock salt|halite|salt)\b/], ["gypsum", /\bgypsum\b/], ["coal", /\bcoal\b/],
  ["ore", /\b(ore|galena|sphalerite)\b/],
];
export function materialFor(interval: DepthInterval, kind: Borehole["kind"]): MaterialId {
  if (kind === "core") return "inventory";
  const text = interval.description.toLowerCase();
  // A negation, qualified statement or fluid mention cannot safely become solid geometry.
  if (/\b(no|not|without|possible|possibly|probable|unknown|trace|water|oil|gas|brine)\b|\?/.test(text)) return "unknown";
  const found = words.filter(([, re]) => re.test(text));
  return found.length === 1 ? found[0][0] : "unknown";
}
export const materialInfo = (id: MaterialId) => MATERIALS.find(m => m.id === id)!;
export function recordYear(record: Borehole): number | null {
  const match = /^(\d{4})-\d{2}-\d{2}(?:$|T)/.exec(record.sourceTime);
  if (!match || !Number.isFinite(Date.parse(record.sourceTime)) || new Date(record.sourceTime).toISOString().slice(0, 10) !== record.sourceTime.slice(0, 10)) return null;
  const year = Number(match[1]); return year >= 1800 && year <= 2200 ? year : null;
}
export const atRecordYear = (record: Borehole, year: number | null) => year === null || (recordYear(record) !== null && recordYear(record)! <= year);

/** Small, deterministic, seamless illustrative texture; no observations are synthesized. */
export function materialPixels(id: MaterialId, size = 64): Uint8Array {
  if (!Number.isInteger(size) || size < 8 || size > 128) throw new Error("Bounded texture size required");
  const { color, pattern } = materialInfo(id), base = [1, 3, 5].map(n => parseInt(color.slice(n, n + 2), 16));
  const data = new Uint8Array(size * size * 4);
  for (let y = 0; y < size; y++) for (let x = 0; x < size; x++) {
    const a = 2 * Math.PI * x / size, b = 2 * Math.PI * y / size;
    const noise = Math.sin(a * 13 + Math.sin(b * 7)) * Math.cos(b * 19 + Math.cos(a * 11));
    const f = pattern === "plain" ? 0 : pattern === "band" ? Math.sin(b * 8 + Math.sin(a) * .6) * 18 + noise * 5
      : pattern === "vein" ? Math.sin(a * 3 + Math.sin(b * 2)) ** 12 * 28 + noise * 7
      : pattern === "crystal" ? Math.round(noise * 3) * 9 : pattern === "pebble" ? Math.sin(a * 5) * Math.cos(b * 6) * 25 + noise * 8
      : noise * (pattern === "smooth" ? 7 : 28);
    const offset = (y * size + x) * 4;
    base.forEach((c, channel) => { data[offset + channel] = Math.max(0, Math.min(255, Math.round(c + f))); });
    data[offset + 3] = 255;
  }
  return data;
}
