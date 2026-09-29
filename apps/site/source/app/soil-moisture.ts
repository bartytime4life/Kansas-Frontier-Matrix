/** NASA GIBS SPL4SMAU V008 visual context. These images are not pixel readings. */
export const SOIL_VIEWS = {
  surface: { layer: "SMAP_L4_Analyzed_Surface_Soil_Moisture", legend: "SMAP_Analyzed_Soil_Moisture_H.svg", label: "Surface moisture · 0–5 cm" },
  root: { layer: "SMAP_L4_Analyzed_Root_Zone_Soil_Moisture", legend: "SMAP_Analyzed_Soil_Moisture_H.svg", label: "Root zone moisture · 0–100 cm" },
  "surface-uncertainty": { layer: "SMAP_L4_Uncertainty_Analyzed_Surface_Soil_Moisture", legend: "SMAP_Uncertainty_Analyzed_Soil_Moisture_H.svg", label: "Surface uncertainty · 0–5 cm" },
  "root-uncertainty": { layer: "SMAP_L4_Uncertainty_Analyzed_Root_Zone_Soil_Moisture", legend: "SMAP_Uncertainty_Analyzed_Soil_Moisture_H.svg", label: "Root zone uncertainty · 0–100 cm" },
} as const;
export type SoilView = keyof typeof SOIL_VIEWS;
export type SoilMapState = { visible: boolean; view: SoilView; day: string; opacity: number };
export const DEFAULT_SOIL_MAP_STATE: SoilMapState = { visible: false, view: "surface", day: "", opacity: 0.65 };
export const isSoilCalendarDay = (day: string) => /^\d{4}-\d{2}-\d{2}$/.test(day)
  && Number.isFinite(Date.parse(`${day}T00:00:00Z`))
  && new Date(`${day}T00:00:00Z`).toISOString().slice(0, 10) === day;
export const visibleExternalContextCount = (officialCount: number, soilVisible: boolean) => officialCount + Number(soilVisible);
export const hideSoilContext = (state: SoilMapState): SoilMapState => ({ ...state, visible: false });
export function serializeSoilMapState(params: URLSearchParams, state: SoilMapState) {
  params.set("soil", [state.visible ? "1" : "0", state.view, state.day, state.opacity.toFixed(2)].join("|"));
}
export function restoreSoilMapState(params: URLSearchParams): SoilMapState {
  const value = params.get("soil");
  if (!value) return DEFAULT_SOIL_MAP_STATE;
  const [visible, view, day, opacity, ...extra] = value.split("|");
  if (extra.length || (visible !== "0" && visible !== "1") || !Object.hasOwn(SOIL_VIEWS, view)
    || (day !== "" && !isSoilCalendarDay(day)) || opacity.trim() === "" || !Number.isFinite(Number(opacity))) return DEFAULT_SOIL_MAP_STATE;
  return { visible: visible === "1", view: view as SoilView, day, opacity: Math.max(0, Math.min(1, Number(opacity))) };
}
export const SOIL_METADATA_URL = "https://gibs.earthdata.nasa.gov/layer-metadata/v1.0/SMAP_L4_Analyzed_Surface_Soil_Moisture.json";
export const SOIL_GUIDE_URL = "https://nsidc.org/data/spl4smau/versions/8";
export const soilLegendUrl = (view: SoilView) => `https://gibs.earthdata.nasa.gov/legends/${SOIL_VIEWS[view].legend}`;

export function validSoilDay(day: string, now = new Date()): boolean {
  if (!isSoilCalendarDay(day)) return false;
  const today = now.toISOString().slice(0, 10);
  const first = new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate() - 29)).toISOString().slice(0, 10);
  return day >= first && day <= today;
}

/** Parse only named WMTS Layer/Time elements, expanding daily ranges within 30 days. */
export function parseSoilAvailability(xml: string, now = new Date()): Record<SoilView, string[]> {
  if (!xml.includes("<Capabilities") && !xml.includes(":Capabilities")) throw new Error("Invalid NASA WMTS capabilities.");
  const result = {} as Record<SoilView, string[]>;
  for (const [view, spec] of Object.entries(SOIL_VIEWS) as [SoilView, typeof SOIL_VIEWS[SoilView]][]) {
    const escaped = spec.layer.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const layer = xml.match(new RegExp(`<Layer\\b[^>]*>(?:(?!<Layer\\b)[\\s\\S])*?<ows:Identifier>${escaped}</ows:Identifier>[\\s\\S]*?</Layer>`))?.[0];
    const time = layer?.match(/<Dimension>\s*<ows:Identifier>Time<\/ows:Identifier>[\s\S]*?<\/Dimension>/)?.[0];
    if (!time || !layer.includes("GoogleMapsCompatible_Level6")) throw new Error(`NASA layer metadata missing for ${view}.`);
    const days = new Set<string>();
    for (const item of time.matchAll(/<Value>([^<]+)<\/Value>/g)) {
      const match = item[1].match(/^(\d{4}-\d{2}-\d{2})\/(\d{4}-\d{2}-\d{2})\/P1D$/);
      if (!match) throw new Error(`Unexpected NASA time range for ${view}.`);
      const canonical = (value: string) => {
        const stamp = Date.parse(`${value}T00:00:00Z`);
        return Number.isFinite(stamp) && new Date(stamp).toISOString().slice(0, 10) === value;
      };
      if (!canonical(match[1]) || !canonical(match[2]) || match[1] > match[2]) throw new Error(`Invalid NASA time range for ${view}.`);
      for (let t = Date.parse(`${match[1]}T00:00:00Z`), end = Date.parse(`${match[2]}T00:00:00Z`), n = 0; t <= end && n < 31; t += 86400000, n++) {
        const day = new Date(t).toISOString().slice(0, 10);
        if (validSoilDay(day, now)) days.add(day);
      }
      // Long historical ranges may start before the window. Expand their overlap separately.
      const first = Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate() - 29);
      for (let t = Math.max(first, Date.parse(`${match[1]}T00:00:00Z`)), end = Math.min(Date.parse(`${match[2]}T00:00:00Z`), Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate())), n = 0; t <= end && n < 30; t += 86400000, n++) days.add(new Date(t).toISOString().slice(0, 10));
    }
    result[view] = [...days].sort().reverse();
  }
  return result;
}

export function commonSoilDays(days: Record<SoilView, string[]>): string[] {
  return days.surface.filter(day => (Object.keys(SOIL_VIEWS) as SoilView[]).every(view => days[view].includes(day)));
}
