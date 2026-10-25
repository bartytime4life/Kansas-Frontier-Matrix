/**
 * Kansas airspace, airport and airway context from one pinned FAA NASR cycle.
 *
 * Built by pipelines/domains/roads-rail-trade/faa_airspace.py. Display context
 * only: not navigation, flight planning or UAS authorization, and not the held
 * KFM APT candidate lane. Source limits keep their MSL/AGL/SFC reference; only
 * display heights are converted, using a stated ground reference elevation.
 */
export const AVIATION_CONTEXT_ASSET = Object.freeze({
  url: "/data/aviation/kansas-aviation-context.json",
  sha256: "ada5a80a5c54f8af52d1c466504ed08244f3dd3576ce50820936a857dccddc13",
  productId: "sha256:66fd3695e5a481625f8d16923117df47bbbab015e358bdeea21ce9b317c66b86",
  nasrCycle: "2026-10-29",
  maxBytes: 2 * 1024 * 1024,
});

export const FEET_TO_METERS = 0.3048;
export const DRONE_CEILING_FT_AGL = 400;
const NM_TO_KM = 1.852;

export type AltitudeReference = "MSL" | "AGL" | "SFC";
export type AltitudeBound = Readonly<{ value_ft: number; reference: AltitudeReference; inclusive?: false }>;
export type AirspaceType = "CLASS_B" | "CLASS_C" | "CLASS_D" | "CLASS_E2" | "CLASS_E3" | "CLASS_E4" | "CLASS_E5" | "CLASS_E6" | "CLASS_E7"
  | "MOA" | "RESTRICTED" | "PROHIBITED" | "WARNING" | "ALERT" | "NSA";
export type GroundReference = Readonly<{ ft: number; method: "ASSOCIATED_AIRPORT" | "NEAREST_AIRPORT"; airport: string; distance_km: number }>;
export type AirspaceVolume = Readonly<{
  id: string; type: AirspaceType; identifier: string; name: string; state: string | null;
  floor: AltitudeBound; ceiling: AltitudeBound; schedule: string | null; controlling_facility: string | null;
  ground_reference: GroundReference | null; bbox: readonly [number, number, number, number];
  rings: readonly (readonly (readonly [number, number])[])[];
}>;
export type AviationRunway = Readonly<{ id: string; length_ft: number; width_ft: number | null; surface: string | null; lighting: string | null;
  ends: readonly Readonly<{ id: string; lon: number; lat: number; elevation_ft: number | null }>[] }>;
export type AviationAirport = Readonly<{
  faa_id: string; icao_id: string | null; name: string; city: string | null; county: string | null; state: string | null;
  lon: number; lat: number; elevation_ft: number; facility_type: string; use: "PUBLIC" | "PRIVATE"; ownership: string | null; tower: string | null;
  weather_station: string | null; ctaf_mhz: number | null; traffic_pattern_ft_agl: number | null; runways: readonly AviationRunway[];
}>;
export type AirwaySegment = Readonly<{ designation: string; type: "VICTOR" | "JET" | "RNAV_T" | "RNAV_Q"; from: string; to: string;
  coords: readonly [readonly [number, number], readonly [number, number]]; mea_ft: number | null; maa_ft: number | null }>;
export type AviationContext = Readonly<{
  productId: string; nasrCycle: string; validFrom: string; validToExclusive: string; limitations: readonly string[];
  classA: Readonly<{ floor: AltitudeBound; ceiling: AltitudeBound }> | null;
  volumes: readonly AirspaceVolume[]; airports: readonly AviationAirport[]; airways: readonly AirwaySegment[];
}>;

const TYPES: ReadonlySet<string> = new Set(["CLASS_B", "CLASS_C", "CLASS_D", "CLASS_E2", "CLASS_E3", "CLASS_E4", "CLASS_E5", "CLASS_E6", "CLASS_E7", "MOA", "RESTRICTED", "PROHIBITED", "WARNING", "ALERT", "NSA"]);
const AIRWAY_TYPES: ReadonlySet<string> = new Set(["VICTOR", "JET", "RNAV_T", "RNAV_Q"]);
const isObject = (value: unknown): value is Record<string, unknown> => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const finite = (value: unknown, low: number, high: number): value is number => typeof value === "number" && Number.isFinite(value) && value >= low && value <= high;
const text = (value: unknown, max = 256): value is string => typeof value === "string" && value.length <= max;
const optionalText = (value: unknown): string | null => text(value, 512) && value ? value : null;
const isoDay = (value: unknown): value is string => typeof value === "string" && /^\d{4}-\d{2}-\d{2}$/.test(value) && new Date(`${value}T00:00:00Z`).toISOString().slice(0, 10) === value;
const position = (value: unknown): value is [number, number] => Array.isArray(value) && value.length === 2 && finite(value[0], -180, 180) && finite(value[1], -90, 90);

const bound = (value: unknown): AltitudeBound => {
  if (!isObject(value) || !["MSL", "AGL", "SFC"].includes(value.reference as string) || !finite(value.value_ft, -2000, 100000)) throw new Error("Invalid airspace vertical limit.");
  if (value.reference === "SFC" && value.value_ft !== 0) throw new Error("Invalid surface limit.");
  return Object.freeze({ value_ft: value.value_ft, reference: value.reference as AltitudeReference, ...(value.inclusive === false ? { inclusive: false as const } : {}) });
};

/** Fails closed on any shape drift; the bytes were already checked against the pinned SHA-256. */
export function parseAviationContext(value: unknown): AviationContext {
  if (!isObject(value) || value.profile !== "kfm.aviation-kansas-context/v2" || value.evidence_role !== "EXTERNAL_CONTEXT_ONLY"
    || value.product_id !== AVIATION_CONTEXT_ASSET.productId || value.nasr_cycle !== AVIATION_CONTEXT_ASSET.nasrCycle
    || !isoDay(value.valid_from) || !isoDay(value.valid_to_exclusive) || !Array.isArray(value.volumes) || !Array.isArray(value.airports) || !Array.isArray(value.airways)) {
    throw new Error("The aviation context did not match its pinned product contract.");
  }
  const volumes = value.volumes.map((item): AirspaceVolume => {
    if (!isObject(item) || !text(item.id, 64) || !TYPES.has(item.type as string) || !text(item.identifier, 16) || !text(item.name, 160)
      || !Array.isArray(item.rings) || !item.rings.length || !Array.isArray(item.bbox) || item.bbox.length !== 4 || !item.bbox.every(n => finite(n, -180, 180))) {
      throw new Error("Invalid airspace volume.");
    }
    const rings = item.rings.map(ring => {
      if (!Array.isArray(ring) || ring.length < 4 || !ring.every(position)) throw new Error("Invalid airspace ring.");
      return Object.freeze(ring.map(point => Object.freeze([point[0], point[1]] as const)));
    });
    const ground = item.ground_reference;
    const groundReference = isObject(ground) && finite(ground.ft, -1500, 15000) && (ground.method === "ASSOCIATED_AIRPORT" || ground.method === "NEAREST_AIRPORT")
      && text(ground.airport, 8) && finite(ground.distance_km, 0, 1000)
      ? Object.freeze({ ft: ground.ft, method: ground.method, airport: ground.airport, distance_km: ground.distance_km }) as GroundReference : null;
    return Object.freeze({ id: item.id, type: item.type as AirspaceType, identifier: item.identifier, name: item.name, state: optionalText(item.state),
      floor: bound(item.floor), ceiling: bound(item.ceiling), schedule: optionalText(item.schedule), controlling_facility: optionalText(item.controlling_facility),
      ground_reference: groundReference, bbox: Object.freeze([...item.bbox] as [number, number, number, number]), rings: Object.freeze(rings) });
  });
  const airports = value.airports.map((item): AviationAirport => {
    if (!isObject(item) || !text(item.faa_id, 8) || !item.faa_id || !text(item.name, 160) || !finite(item.lon, -180, 180) || !finite(item.lat, -90, 90)
      || !finite(item.elevation_ft, -1500, 15000) || !text(item.facility_type, 32) || (item.use !== "PUBLIC" && item.use !== "PRIVATE") || !Array.isArray(item.runways)) throw new Error("Invalid airport record.");
    const runways = item.runways.flatMap((runway): AviationRunway[] => {
      if (!isObject(runway) || !text(runway.id, 16) || !finite(runway.length_ft, 1, 30000) || !Array.isArray(runway.ends) || runway.ends.length !== 2) return [];
      const ends = runway.ends.filter(isObject).filter(end => text(end.id, 8) && finite(end.lon, -180, 180) && finite(end.lat, -90, 90))
        .map(end => Object.freeze({ id: end.id as string, lon: end.lon as number, lat: end.lat as number, elevation_ft: finite(end.elevation_ft, -1500, 15000) ? end.elevation_ft : null }));
      return ends.length === 2 ? [Object.freeze({ id: runway.id, length_ft: runway.length_ft, width_ft: finite(runway.width_ft, 1, 1000) ? runway.width_ft : null,
        surface: optionalText(runway.surface), lighting: optionalText(runway.lighting), ends: Object.freeze(ends) })] : [];
    });
    return Object.freeze({ faa_id: item.faa_id, icao_id: text(item.icao_id, 4) && /^[A-Z]{4}$/.test(item.icao_id) ? item.icao_id : null, name: item.name,
      city: optionalText(item.city), county: optionalText(item.county), state: optionalText(item.state), lon: item.lon, lat: item.lat,
      elevation_ft: item.elevation_ft, facility_type: item.facility_type, use: item.use, ownership: optionalText(item.ownership), tower: optionalText(item.tower),
      weather_station: optionalText(item.weather_station), ctaf_mhz: finite(item.ctaf_mhz, 100, 400) ? item.ctaf_mhz : null,
      traffic_pattern_ft_agl: finite(item.traffic_pattern_ft_agl, 100, 5000) ? item.traffic_pattern_ft_agl : null, runways: Object.freeze(runways) });
  });
  const airways = value.airways.map((item): AirwaySegment => {
    if (!isObject(item) || !text(item.designation, 16) || !AIRWAY_TYPES.has(item.type as string) || !Array.isArray(item.coords) || item.coords.length !== 2 || !item.coords.every(position)) {
      throw new Error("Invalid airway segment.");
    }
    return Object.freeze({ designation: item.designation, type: item.type as AirwaySegment["type"], from: text(item.from, 16) ? item.from : "", to: text(item.to, 16) ? item.to : "",
      coords: Object.freeze([Object.freeze([item.coords[0][0], item.coords[0][1]] as const), Object.freeze([item.coords[1][0], item.coords[1][1]] as const)] as const),
      mea_ft: finite(item.mea_ft, 0, 60000) ? item.mea_ft : null, maa_ft: finite(item.maa_ft, 0, 99999) ? item.maa_ft : null });
  });
  const classA = isObject(value.class_a) ? Object.freeze({ floor: bound(value.class_a.floor), ceiling: bound(value.class_a.ceiling) }) : null;
  return Object.freeze({ productId: value.product_id, nasrCycle: value.nasr_cycle, validFrom: value.valid_from, validToExclusive: value.valid_to_exclusive,
    limitations: Object.freeze(Array.isArray(value.limitations) ? value.limitations.filter((item): item is string => text(item, 512)) : []),
    classA, volumes: Object.freeze(volumes), airports: Object.freeze(airports), airways: Object.freeze(airways) });
}

export type EditionStatus = Readonly<{ state: "PREVIEW" | "CURRENT" | "EXPIRED"; text: string }>;

/** A cached NASR cycle is never presented as current outside its 28-day window. */
export function aviationEditionStatus(context: Pick<AviationContext, "nasrCycle" | "validFrom" | "validToExclusive">, now: number): EditionStatus {
  const day = new Date(now).toISOString().slice(0, 10);
  if (day < context.validFrom) return Object.freeze({ state: "PREVIEW", text: `NASR cycle ${context.nasrCycle} is a preview edition: it becomes effective ${context.validFrom}. Use current FAA charts until then.` });
  if (day >= context.validToExclusive) return Object.freeze({ state: "EXPIRED", text: `NASR cycle ${context.nasrCycle} expired ${context.validToExclusive}. Boundaries may have changed; treat this as historical reference.` });
  return Object.freeze({ state: "CURRENT", text: `NASR cycle ${context.nasrCycle}, effective ${context.validFrom} through the day before ${context.validToExclusive}.` });
}

const grouped = (value: number) => Math.round(value).toLocaleString("en-US");

/** Chart-style limit text: SFC, 3,800 MSL, 700 AGL, FL180; an exclusive ceiling reads "below FL180". */
export function formatAltitudeBound(limit: AltitudeBound): string {
  const core = limit.reference === "SFC" ? "SFC"
    : limit.reference === "MSL" && limit.value_ft >= 18000 ? `FL${String(Math.round(limit.value_ft / 100)).padStart(3, "0")}`
    : `${grouped(limit.value_ft)} ${limit.reference}`;
  return limit.inclusive === false ? `below ${core}` : core;
}

export const AIRSPACE_CLASS_TITLES: Readonly<Record<AirspaceType, string>> = Object.freeze({
  CLASS_B: "Class B", CLASS_C: "Class C", CLASS_D: "Class D", CLASS_E2: "Class E surface area (E2)", CLASS_E3: "Class E surface extension (E3)",
  CLASS_E4: "Class E surface extension (E4)", CLASS_E5: "Class E transition area (E5)", CLASS_E6: "Class E en route domestic (E6)",
  CLASS_E7: "Class E offshore (E7)", MOA: "Military Operations Area", RESTRICTED: "Restricted Area", PROHIBITED: "Prohibited Area",
  WARNING: "Warning Area", ALERT: "Alert Area", NSA: "National Security Area",
});

/** Chart notation in hundreds of feet: 5,300 MSL → "53", SFC → "SFC", 700 AGL → "7 AGL". */
export function chartLimit(limit: AltitudeBound): string {
  if (limit.reference === "SFC") return "SFC";
  const hundreds = String(Math.round(limit.value_ft / 100));
  return limit.reference === "AGL" ? `${hundreds} AGL` : hundreds;
}

/** Sectional-style label: identifier then ceiling/floor, e.g. "ICT 53/27"; special use keeps its name. */
export function chartLabel(volume: Pick<AirspaceVolume, "type" | "identifier" | "name" | "floor" | "ceiling">): string {
  const name = volume.identifier && !["MOA", "ALERT", "WARNING", "NSA"].includes(volume.type) ? volume.identifier : volume.name.replace(/,\s*[A-Z]{2}$/, "");
  return `${name} ${chartLimit(volume.ceiling)}/${chartLimit(volume.floor)}`;
}

/** One-line technical label drawn on the map and listed in the column inspector. */
export function airspaceLabel(volume: Pick<AirspaceVolume, "type" | "identifier" | "name" | "floor" | "ceiling">): string {
  const limits = `${formatAltitudeBound(volume.floor)}–${formatAltitudeBound(volume.ceiling)}`;
  if (volume.type === "MOA" || volume.type === "RESTRICTED" || volume.type === "PROHIBITED" || volume.type === "ALERT" || volume.type === "WARNING" || volume.type === "NSA") {
    return `${volume.name.replace(/,\s*[A-Z]{2}$/, "")} · ${limits}`;
  }
  const short = AIRSPACE_CLASS_TITLES[volume.type].replace(/ \(.*\)$/, "").toUpperCase();
  return `${short}${volume.identifier ? ` · ${volume.identifier}` : ` · ${volume.name.replace(/ CLASS E\d$/, "")}`} · ${limits}`;
}

/** Height above the volume's ground reference, in feet. Unknown ground keeps MSL as-is (no invented terrain). */
export function feetAboveGround(limit: AltitudeBound, groundFt: number | null): number {
  if (limit.reference === "SFC") return 0;
  if (limit.reference === "AGL") return limit.value_ft;
  return Math.max(0, limit.value_ft - (groundFt ?? 0));
}

export function displayHeightsMeters(volume: Pick<AirspaceVolume, "floor" | "ceiling" | "ground_reference">, exaggeration = 1): Readonly<{ base: number; top: number }> {
  const scale = finite(exaggeration, 0.1, 50) ? exaggeration : 1;
  const ground = volume.ground_reference?.ft ?? null;
  const base = feetAboveGround(volume.floor, ground) * FEET_TO_METERS * scale;
  const top = Math.max(base + 1, feetAboveGround(volume.ceiling, ground) * FEET_TO_METERS * scale);
  return Object.freeze({ base, top });
}

export type DroneRuleCode = "NO_FLY_WITHOUT_PERMISSION" | "ATC_AUTHORIZATION_REQUIRED" | "CAUTION" | "ABOVE_DRONE_CEILING";
export type DroneRule = Readonly<{ code: DroneRuleCode; title: string; detail: string; cite: string }>;
const SURFACE_CONTROLLED: ReadonlySet<AirspaceType> = new Set(["CLASS_B", "CLASS_C", "CLASS_D", "CLASS_E2", "CLASS_E3", "CLASS_E4"]);

/** Small-UAS rule for the part of this volume that lies at or below 400 ft AGL, if any. */
export function droneRule(volume: Pick<AirspaceVolume, "type" | "identifier" | "floor" | "ground_reference">, groundFt?: number): DroneRule {
  // A point's own ground, when known, decides whether an MSL floor is within 400 ft of it; otherwise the volume's reference.
  const floorAgl = feetAboveGround(volume.floor, groundFt ?? volume.ground_reference?.ft ?? null);
  if (floorAgl >= DRONE_CEILING_FT_AGL) {
    return Object.freeze({ code: "ABOVE_DRONE_CEILING", title: "Above the 400 ft drone ceiling",
      detail: `This volume starts about ${grouped(floorAgl)} ft above the ground. A drone below 400 ft AGL here is governed by the airspace beneath it.`,
      cite: "14 CFR 107.51(b); 49 U.S.C. 44809(a)(6)" });
  }
  if (volume.type === "RESTRICTED" || volume.type === "PROHIBITED" || volume.type === "NSA") {
    return Object.freeze({ code: "NO_FLY_WITHOUT_PERMISSION", title: "No drone flight without the using/controlling agency's permission",
      detail: `${volume.identifier || "This area"} reaches the ground. Restricted areas can be active without notice to drone pilots; permission comes from the using or controlling agency, not LAANC.`,
      cite: "14 CFR 107.45; 14 CFR 99.7" });
  }
  if (SURFACE_CONTROLLED.has(volume.type as AirspaceType)) {
    return Object.freeze({ code: "ATC_AUTHORIZATION_REQUIRED", title: "FAA/ATC authorization required (LAANC or DroneZone)",
      detail: "Controlled airspace reaches the ground. Part 107 and recreational pilots need prior authorization; the FAA UAS Facility Map grid sets the altitude (0–400 ft) LAANC can approve per cell.",
      cite: "14 CFR 107.41; 49 U.S.C. 44809(a)(5)" });
  }
  return Object.freeze({ code: "CAUTION", title: "Caution: low-level manned activity",
    detail: volume.type === "MOA" ? "Military aircraft may fly fast and low when the MOA is active. No authorization is required, but check activity with the controlling facility."
      : "Concentrated pilot training or unusual aerial activity. No authorization is required; see-and-avoid responsibility is unchanged.",
    cite: "AIM 3-4-5 / 3-4-6; 14 CFR 107.37" });
}

export function pointInRings(lon: number, lat: number, rings: AirspaceVolume["rings"]): boolean {
  let inside = false;
  rings.forEach((ring, ringIndex) => {
    let crosses = false;
    for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) {
      const [xi, yi] = ring[i], [xj, yj] = ring[j];
      if ((yi > lat) !== (yj > lat) && lon < (xj - xi) * (lat - yi) / (yj - yi) + xi) crosses = !crosses;
    }
    // Holes (rings after the first) cut the exterior out.
    if (ringIndex === 0) inside = crosses;
    else if (crosses) inside = false;
  });
  return inside;
}

export function volumesAtPoint(context: Pick<AviationContext, "volumes">, lon: number, lat: number): readonly AirspaceVolume[] {
  return context.volumes.filter(v => lon >= v.bbox[0] && lon <= v.bbox[2] && lat >= v.bbox[1] && lat <= v.bbox[3] && pointInRings(lon, lat, v.rings));
}

export type ColumnClass = "A" | "B" | "C" | "D" | "E" | "G" | "SUA";
export type ColumnBand = Readonly<{ key: string; label: string; airspaceClass: ColumnClass; floorText: string; ceilingText: string;
  floorFtAgl: number; ceilingFtAgl: number; manned: string; cite: string; source: string; volumeId: string | null }>;

export const CLASS_REQUIREMENTS: Readonly<Record<ColumnClass, Readonly<{ manned: string; cite: string }>>> = Object.freeze({
  A: { manned: "IFR only: ATC clearance, instrument rating, altimeter 29.92 (flight levels), Mode C transponder and ADS-B Out.", cite: "14 CFR 91.135, 91.215, 91.225" },
  B: { manned: "ATC clearance to enter; private pilot certificate or student endorsement; Mode C transponder and ADS-B Out. VFR: 3 SM visibility, clear of clouds.", cite: "14 CFR 91.131, 91.155, 91.215, 91.225" },
  C: { manned: "Two-way radio contact with ATC before entry; Mode C transponder and ADS-B Out. VFR: 3 SM; 500 ft below, 1,000 ft above, 2,000 ft horizontal from clouds. 200 KIAS at or below 2,500 ft AGL within 4 NM.", cite: "14 CFR 91.130, 91.117(b), 91.155, 91.215, 91.225" },
  D: { manned: "Two-way radio contact with the tower before entry. VFR: 3 SM; 500 ft below, 1,000 ft above, 2,000 ft horizontal from clouds. 200 KIAS at or below 2,500 ft AGL within 4 NM.", cite: "14 CFR 91.129, 91.117(b), 91.155" },
  E: { manned: "Controlled for IFR (clearance required); VFR needs no ATC contact. VFR below 10,000 MSL: 3 SM, 500/1,000/2,000; at or above 10,000 MSL: 5 SM, 1,000 below/above, 1 SM horizontal. Surface areas need a 1,000 ft ceiling and 3 SM for VFR (else special VFR).", cite: "14 CFR 91.155(a),(c),(d), 91.157, 91.173" },
  G: { manned: "Uncontrolled. Day VFR at or below 1,200 ft AGL: 1 SM, clear of clouds; above 1,200 ft AGL: 1 SM, 500/1,000/2,000.", cite: "14 CFR 91.155(a)" },
  SUA: { manned: "Special use airspace: see the area's own rule.", cite: "14 CFR Part 73; AIM 3-4" },
});
const SUA_RULES: Readonly<Partial<Record<AirspaceType, string>>> = Object.freeze({
  MOA: "Military training when active. VFR flight is not prohibited: contact the controlling facility and use extreme caution. ATC separates IFR traffic from active MOAs.",
  RESTRICTED: "Entry prohibited while active without authorization from the using or controlling agency.",
  PROHIBITED: "Flight prohibited.",
  ALERT: "High volume of pilot training or unusual aerial activity; no added requirement, see-and-avoid applies.",
  WARNING: "Hazardous activity over international waters; nonparticipants should avoid when active.",
  NSA: "Pilots are requested to voluntarily avoid; flight may be temporarily prohibited by NOTAM.",
});

const classOf = (type: AirspaceType): ColumnClass => type === "CLASS_B" ? "B" : type === "CLASS_C" ? "C" : type === "CLASS_D" ? "D" : type.startsWith("CLASS_E") ? "E" : "SUA";

/**
 * Vertical stack at one point, surface upward: designated NASR volumes plus
 * the regulatory defaults they sit within (Class G below the lowest controlled
 * floor, Class E from 14,500 MSL, Class A FL180–FL600, Class E above FL600).
 * `groundFt` is the reference elevation used to compare AGL and MSL limits.
 */
export function airspaceColumn(context: Pick<AviationContext, "volumes" | "classA">, lon: number, lat: number, groundFt: number): readonly ColumnBand[] {
  const found = volumesAtPoint(context, lon, lat);
  const bands: ColumnBand[] = found.map(volume => {
    const kind = classOf(volume.type);
    const rule = kind === "SUA" ? { manned: SUA_RULES[volume.type] ?? CLASS_REQUIREMENTS.SUA.manned, cite: volume.type === "RESTRICTED" || volume.type === "PROHIBITED" ? "14 CFR 91.133" : "AIM 3-4" } : CLASS_REQUIREMENTS[kind];
    return Object.freeze({ key: volume.id, label: airspaceLabel(volume), airspaceClass: kind, floorText: formatAltitudeBound(volume.floor), ceilingText: formatAltitudeBound(volume.ceiling),
      floorFtAgl: feetAboveGround(volume.floor, groundFt), ceilingFtAgl: feetAboveGround(volume.ceiling, groundFt), manned: rule.manned, cite: rule.cite,
      source: `FAA NASR ${volume.type} ${volume.identifier || volume.name}`, volumeId: volume.id });
  });
  const controlledFloor = Math.min(...found.filter(v => classOf(v.type) !== "SUA").map(v => feetAboveGround(v.floor, groundFt)),
    feetAboveGround({ value_ft: 14500, reference: "MSL" }, groundFt));
  if (controlledFloor > 0) {
    bands.push(Object.freeze({ key: "default-g", label: `CLASS G · SFC–${grouped(controlledFloor)} AGL`, airspaceClass: "G", floorText: "SFC",
      ceilingText: `${grouped(controlledFloor)} AGL`, floorFtAgl: 0, ceilingFtAgl: controlledFloor, ...CLASS_REQUIREMENTS.G,
      source: "Not designated controlled airspace at this point (14 CFR 71.71 default below the lowest controlled floor)", volumeId: null }));
  }
  const designatedE = found.some(v => v.type.startsWith("CLASS_E") && feetAboveGround(v.ceiling, groundFt) >= feetAboveGround({ value_ft: 17999, reference: "MSL" }, groundFt));
  if (!designatedE) {
    bands.push(Object.freeze({ key: "default-e", label: "CLASS E · 14,500 MSL–below FL180", airspaceClass: "E", floorText: "14,500 MSL", ceilingText: "below FL180",
      floorFtAgl: feetAboveGround({ value_ft: 14500, reference: "MSL" }, groundFt), ceilingFtAgl: feetAboveGround({ value_ft: 18000, reference: "MSL" }, groundFt),
      ...CLASS_REQUIREMENTS.E, source: "14 CFR 71.71(b): Class E from 14,500 MSL over the contiguous states", volumeId: null }));
  }
  const a = context.classA ?? { floor: { value_ft: 18000, reference: "MSL" as const }, ceiling: { value_ft: 60000, reference: "MSL" as const } };
  bands.push(Object.freeze({ key: "class-a", label: `CLASS A · ${formatAltitudeBound(a.floor)}–${formatAltitudeBound(a.ceiling)}`, airspaceClass: "A",
    floorText: formatAltitudeBound(a.floor), ceilingText: formatAltitudeBound(a.ceiling), floorFtAgl: feetAboveGround(a.floor, groundFt),
    ceilingFtAgl: feetAboveGround(a.ceiling, groundFt), ...CLASS_REQUIREMENTS.A, source: "FAA NASR Class A (14 CFR 71.33)", volumeId: null }));
  bands.push(Object.freeze({ key: "above-fl600", label: "CLASS E · above FL600", airspaceClass: "E", floorText: "FL600", ceilingText: "—",
    floorFtAgl: feetAboveGround({ value_ft: 60000, reference: "MSL" }, groundFt), ceilingFtAgl: Number.POSITIVE_INFINITY, ...CLASS_REQUIREMENTS.E,
    source: "14 CFR 71.71(c)", volumeId: null }));
  return Object.freeze(bands.sort((left, right) => left.floorFtAgl - right.floorFtAgl || left.ceilingFtAgl - right.ceilingFtAgl));
}

/**
 * The airspace an aircraft occupies at one altitude: the most specific band
 * whose floor/ceiling (converted with `groundFt`) contains it. Designated
 * B/C/D and special use outrank the Class E/G defaults they sit within.
 */
export function occupiedAirspace(context: Pick<AviationContext, "volumes" | "classA">, lon: number, lat: number, altitudeMslFt: number, groundFt: number): string {
  const above = altitudeMslFt - groundFt;
  const rank: Record<ColumnClass, number> = { B: 6, C: 5, D: 4, SUA: 3, A: 2, E: 1, G: 0 };
  const containing = airspaceColumn(context, lon, lat, groundFt).filter(band => band.floorFtAgl <= above && above < band.ceilingFtAgl)
    .sort((left, right) => rank[right.airspaceClass] - rank[left.airspaceClass]);
  return containing.length ? containing.map(band => band.label.split(" · ").slice(0, 2).join(" · ")).join(" + ") : "Class E";
}

export type DroneVerdict = Readonly<{ rule: DroneRule; governing: string; ceilingFtAgl: number }>;

/** Most restrictive small-UAS rule for SFC–400 ft AGL at a point; Class G is the default. */
export function droneVerdictAtPoint(context: Pick<AviationContext, "volumes">, lon: number, lat: number, groundFt?: number): DroneVerdict {
  const rank: Record<DroneRuleCode, number> = { NO_FLY_WITHOUT_PERMISSION: 3, ATC_AUTHORIZATION_REQUIRED: 2, CAUTION: 1, ABOVE_DRONE_CEILING: 0 };
  let best: DroneVerdict = Object.freeze({ governing: "Loaded NASR surface context only", ceilingFtAgl: DRONE_CEILING_FT_AGL,
    rule: Object.freeze({ code: "ABOVE_DRONE_CEILING" as const, title: "No surface restriction found in the loaded NASR volumes",
      detail: "This partial context result does not establish Class G, clearance or permission to fly. Check current FAA airspace, NOTAMs, TFRs and authorization requirements. Missing or unreadable boundaries may conceal restrictions.",
      cite: "14 CFR 107.31, 107.37, 107.51(b); 14 CFR Part 89; 49 U.S.C. 44809" }) });
  for (const volume of volumesAtPoint(context, lon, lat)) {
    const rule = droneRule(volume, groundFt);
    if (rank[rule.code] > rank[best.rule.code]) best = Object.freeze({ rule, governing: airspaceLabel(volume), ceilingFtAgl: DRONE_CEILING_FT_AGL });
  }
  return best;
}

export type PointGround = Readonly<{ ft: number; method: "TERRAIN_DEM" | "NEAREST_FACILITY" | "NONE"; facility: string | null; km: number | null; terrainRejected: boolean }>;
// Kansas relief between a point and its nearest non-heliport facility stays well under this; larger gaps are DEM artefacts.
export const TERRAIN_AGREEMENT_FT = 1000;

/**
 * Ground under one picked point. A terrain reading (feet MSL, from DEM tiles the
 * viewer already loaded) is used when it agrees with the nearest facility to
 * within 1,000 ft; otherwise, or without one, the nearest facility's elevation.
 * Never a guessed value: no reading and no facility reports NONE at 0 ft.
 */
export function pointGroundReference(anchors: readonly AviationAirport[], lon: number, lat: number, terrainFt: number | null): PointGround {
  const near = nearestAirport(anchors, lon, lat);
  const usable = terrainFt !== null && Number.isFinite(terrainFt) && terrainFt > -1500 && terrainFt < 15000;
  const agrees = usable && (!near || Math.abs((terrainFt as number) - near.airport.elevation_ft) <= TERRAIN_AGREEMENT_FT);
  if (agrees) return Object.freeze({ ft: terrainFt as number, method: "TERRAIN_DEM" as const, facility: near?.airport.faa_id ?? null, km: near?.km ?? null, terrainRejected: false });
  if (near) return Object.freeze({ ft: near.airport.elevation_ft, method: "NEAREST_FACILITY" as const, facility: near.airport.faa_id, km: near.km, terrainRejected: usable });
  return Object.freeze({ ft: 0, method: "NONE" as const, facility: null, km: null, terrainRejected: false });
}

/** Great-circle km; used to pick the nearest airport elevation and weather station. */
export function distanceKm(lon1: number, lat1: number, lon2: number, lat2: number): number {
  const toRad = Math.PI / 180, p1 = lat1 * toRad, p2 = lat2 * toRad;
  const a = Math.sin((p2 - p1) / 2) ** 2 + Math.cos(p1) * Math.cos(p2) * Math.sin((lon2 - lon1) * toRad / 2) ** 2;
  return 6371.0088 * 2 * Math.asin(Math.min(1, Math.sqrt(a)));
}

export function nearestAirport<T extends Pick<AviationAirport, "lon" | "lat">>(airports: readonly T[], lon: number, lat: number): Readonly<{ airport: T; km: number }> | null {
  let best: { airport: T; km: number } | null = null;
  for (const airport of airports) {
    const km = distanceKm(lon, lat, airport.lon, airport.lat);
    if (!best || km < best.km) best = { airport, km };
  }
  return best ? Object.freeze(best) : null;
}

/** Airways within 4 NM of the point (Victor/T route primary protected width each side of centreline). */
export function airwaysNearPoint(context: Pick<AviationContext, "airways">, lon: number, lat: number, widthNm = 4): readonly AirwaySegment[] {
  const limitKm = widthNm * NM_TO_KM, kmPerLon = 111.32 * Math.cos(lat * Math.PI / 180), kmPerLat = 110.57;
  return context.airways.filter(segment => {
    const [[x1, y1], [x2, y2]] = segment.coords;
    const ax = (x1 - lon) * kmPerLon, ay = (y1 - lat) * kmPerLat, bx = (x2 - lon) * kmPerLon, by = (y2 - lat) * kmPerLat;
    const dx = bx - ax, dy = by - ay, length = dx * dx + dy * dy;
    const t = length ? Math.max(0, Math.min(1, -(ax * dx + ay * dy) / length)) : 0;
    return Math.hypot(ax + t * dx, ay + t * dy) <= limitKm;
  });
}

export type AirspaceGroup = "controlled" | "surfaceE" | "transitionE" | "specialUse";
export const AIRSPACE_GROUPS: Readonly<Record<AirspaceGroup, Readonly<{ title: string; types: readonly AirspaceType[]; defaultOn: boolean }>>> = Object.freeze({
  controlled: { title: "Class B, C and D shells", types: ["CLASS_B", "CLASS_C", "CLASS_D"], defaultOn: true },
  surfaceE: { title: "Class E surface areas (E2–E4)", types: ["CLASS_E2", "CLASS_E3", "CLASS_E4"], defaultOn: true },
  transitionE: { title: "Class E 700/1,200 ft floors (E5–E7)", types: ["CLASS_E5", "CLASS_E6", "CLASS_E7"], defaultOn: false },
  specialUse: { title: "MOA, restricted and alert areas", types: ["MOA", "RESTRICTED", "PROHIBITED", "WARNING", "ALERT", "NSA"], defaultOn: true },
});

export const AIRSPACE_COLORS: Readonly<Record<AirspaceType, string>> = Object.freeze({
  CLASS_B: "#1f5fbf", CLASS_C: "#b5338a", CLASS_D: "#2f7fd8", CLASS_E2: "#b5338a", CLASS_E3: "#c45fa4", CLASS_E4: "#c45fa4",
  CLASS_E5: "#d68cc0", CLASS_E6: "#d68cc0", CLASS_E7: "#d68cc0", MOA: "#8a6d1f", RESTRICTED: "#c0392b", PROHIBITED: "#8e1b10",
  WARNING: "#c0392b", ALERT: "#d98a1c", NSA: "#6c3483",
});
export const DRONE_RULE_COLORS: Readonly<Record<DroneRuleCode, string>> = Object.freeze({
  NO_FLY_WITHOUT_PERMISSION: "#c0392b", ATC_AUTHORIZATION_REQUIRED: "#e0a020", CAUTION: "#d9c34a", ABOVE_DRONE_CEILING: "#3d9a5b",
});

type Feature = GeoJSON.Feature<GeoJSON.Geometry, Record<string, string | number | boolean | null>>;

/** Extrusion features: one per volume, carrying display heights and both labels. */
export function airspaceFeatures(context: Pick<AviationContext, "volumes">, groups: ReadonlySet<AirspaceGroup>, exaggeration: number): GeoJSON.FeatureCollection {
  const types = new Set((Object.keys(AIRSPACE_GROUPS) as AirspaceGroup[]).filter(group => groups.has(group)).flatMap(group => AIRSPACE_GROUPS[group].types));
  const features: Feature[] = context.volumes.filter(volume => types.has(volume.type)).map(volume => {
    const { base, top } = displayHeightsMeters(volume, exaggeration);
    const rule = droneRule(volume);
    return { type: "Feature", id: volume.id, geometry: { type: "Polygon", coordinates: volume.rings.map(ring => ring.map(point => [point[0], point[1]])) },
      properties: { id: volume.id, type: volume.type, label: airspaceLabel(volume), chart: chartLabel(volume), color: AIRSPACE_COLORS[volume.type], base, top,
        groundFt: volume.ground_reference?.ft ?? 0, floor: formatAltitudeBound(volume.floor), ceiling: formatAltitudeBound(volume.ceiling), drone: rule.code } };
  });
  return { type: "FeatureCollection", features };
}

/** SFC–400 ft AGL slabs for volumes that touch drone altitudes; Class G is shown by absence. */
export function droneFeatures(context: Pick<AviationContext, "volumes">, exaggeration: number): GeoJSON.FeatureCollection {
  const features: Feature[] = context.volumes.flatMap((volume): Feature[] => {
    const rule = droneRule(volume);
    if (rule.code === "ABOVE_DRONE_CEILING") return [];
    const floor = feetAboveGround(volume.floor, volume.ground_reference?.ft ?? null);
    return [{ type: "Feature", id: `drone:${volume.id}`, geometry: { type: "Polygon", coordinates: volume.rings.map(ring => ring.map(point => [point[0], point[1]])) },
      properties: { id: volume.id, code: rule.code, color: DRONE_RULE_COLORS[rule.code], groundFt: volume.ground_reference?.ft ?? 0, base: floor * FEET_TO_METERS * exaggeration,
        top: DRONE_CEILING_FT_AGL * FEET_TO_METERS * exaggeration, label: `UAS: ${rule.title} · ${volume.identifier || volume.name} · ${formatAltitudeBound(volume.floor)}–400 AGL` } }];
  });
  return { type: "FeatureCollection", features };
}

/** Facilities whose published elevation is ground level: heliports can be rooftops, so they never anchor heights (as in the pipeline). */
export const groundAnchors = (airports: readonly AviationAirport[]): readonly AviationAirport[] => airports.filter(airport => airport.facility_type !== "HELIPORT");

export function airportFeatures(context: Pick<AviationContext, "airports">): Readonly<{ points: GeoJSON.FeatureCollection; runways: GeoJSON.FeatureCollection }> {
  const points: Feature[] = context.airports.map(airport => ({ type: "Feature", id: airport.faa_id, geometry: { type: "Point", coordinates: [airport.lon, airport.lat] },
    properties: { faa_id: airport.faa_id, label: `${airport.icao_id ?? airport.faa_id} · ${grouped(airport.elevation_ft)} ft${airport.use === "PRIVATE" ? " · PVT" : ""}`, facility: airport.facility_type,
      private: airport.use === "PRIVATE",
      towered: Boolean(airport.tower && airport.tower !== "NON-ATCT"), weather: airport.weather_station } }));
  const runways: Feature[] = context.airports.flatMap(airport => airport.runways.map((runway): Feature => ({ type: "Feature", id: `${airport.faa_id}:${runway.id}`,
    geometry: { type: "LineString", coordinates: runway.ends.map(end => [end.lon, end.lat]) },
    properties: { label: `${airport.faa_id} ${runway.id} · ${grouped(runway.length_ft)} × ${runway.width_ft ?? "?"} ft`, width_ft: runway.width_ft ?? 75 } })));
  return Object.freeze({ points: { type: "FeatureCollection", features: points }, runways: { type: "FeatureCollection", features: runways } });
}

export function airwayFeatures(context: Pick<AviationContext, "airways">, kinds: ReadonlySet<AirwaySegment["type"]>): GeoJSON.FeatureCollection {
  const features: Feature[] = context.airways.filter(segment => kinds.has(segment.type)).map((segment, index) => ({ type: "Feature", id: index,
    geometry: { type: "LineString", coordinates: segment.coords.map(point => [point[0], point[1]]) },
    properties: { kind: segment.type, label: `${segment.designation}${segment.mea_ft ? ` · MEA ${grouped(segment.mea_ft)}` : ""}`, high: segment.type === "JET" || segment.type === "RNAV_Q" } }));
  return { type: "FeatureCollection", features };
}
