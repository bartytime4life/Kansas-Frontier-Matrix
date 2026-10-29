import type { Feature, Polygon, MultiPolygon } from "geojson";
import type { OfficialContextPayload, OfficialContextSource } from "./live-context";
import { CIVIC_ID, CIVIC_SOURCE, CIVIC_SERVICE, CIVIC_LIMITATION, validateCivicGeometry } from "./civic-districts";

// Compatibility source identity is retained; historical plans have their own immutable identities.
export const CIVIC_HISTORY_URL = "https://cdmaps.polisci.ucla.edu/";
export const CIVIC_HISTORY_LICENSE = "MIT License\n\nCopyright (c) 2013-2018 Jeffrey B. Lewis\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the \"Software\"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n";
export const CIVIC_HISTORY_CREDIT = "Jeffrey B. Lewis, Brandon DeVine, Lincoln Pitcher and Kenneth C. Martis · Digital Boundary Definitions of U.S. Congressional Districts";
export const CIVIC_HISTORY_LIMITATION = "Scholarly historical reconstruction, with Census-derived recent plans. District numbers are not persistent identities across redistricting. At-large shapes are statewide constituencies, not one seat each, and may overlap numbered districts. No officeholders, party, election result, eligibility or tribal sovereignty is inferred. Source NAD83 coordinates use the provider's zero-shift display approximation to WGS84; no survey accuracy is claimed. Calendar transition dates use the incoming Congress, without intraday precision. External context only; no KFM evidence release.";
export type CivicHistoryPlan = Readonly<{ first: number; last: number; file: string; commit: string; sha256: string; districts: readonly number[] }>;
export const CIVIC_HISTORY_PLANS: readonly CivicHistoryPlan[] = Object.freeze([
  Object.freeze({"first":36,"last":42,"file":"Kansas_36_to_42.geojson","commit":"a72f5836d0de4ad5aa94a18b6b725b46bf71b39e","sha256":"8953c719b3f71c374e6dfc797d9740b70b593a52932b1cbb5fa18beac4f6eea3","districts":[0]}),
  Object.freeze({"first":43,"last":43,"file":"Kansas_43_to_43.geojson","commit":"a72f5836d0de4ad5aa94a18b6b725b46bf71b39e","sha256":"ab8ade9ecbbfb0376723708ee1c9f0588d792499249b8a57151af92d7bca01fa","districts":[0]}),
  Object.freeze({"first":44,"last":47,"file":"Kansas_44_to_47.geojson","commit":"a72f5836d0de4ad5aa94a18b6b725b46bf71b39e","sha256":"0f08ab3bf2b14dd961852002469db3b2bb54de13c1b3cc6ab89839ad99497b9f","districts":[1,2,3]}),
  Object.freeze({"first":48,"last":48,"file":"Kansas_48_to_48.geojson","commit":"a72f5836d0de4ad5aa94a18b6b725b46bf71b39e","sha256":"78ad1c670dbb3df9104f26377a1c3d238c37f9c31f49aac331a7173778722ea1","districts":[0,1,2,3]}),
  Object.freeze({"first":49,"last":52,"file":"Kansas_49_to_52.geojson","commit":"a72f5836d0de4ad5aa94a18b6b725b46bf71b39e","sha256":"8303cd18ae411e3ba460df216d24914e517019dfc00e7e67408ab19f74d8c16e","districts":[1,2,3,4,5,6,7]}),
  Object.freeze({"first":53,"last":55,"file":"Kansas_53_to_55.geojson","commit":"a72f5836d0de4ad5aa94a18b6b725b46bf71b39e","sha256":"c2f4fbae35681575a2163c0a0071fea01c4ae9b2914ed2d3be686d1b87af2088","districts":[0,1,2,3,4,5,6,7]}),
  Object.freeze({"first":56,"last":59,"file":"Kansas_56_to_59.geojson","commit":"a72f5836d0de4ad5aa94a18b6b725b46bf71b39e","sha256":"5acc2308a8f8a4b66ea4a250843c44d07277649ebc178f48af28a6b10e0a17ad","districts":[0,1,2,3,4,5,6,7]}),
  Object.freeze({"first":60,"last":72,"file":"Kansas_60_to_72.geojson","commit":"a72f5836d0de4ad5aa94a18b6b725b46bf71b39e","sha256":"01a845d7ea61e8f55ef35bc9f97ca3c5c63bb874ca86e38bbcfdaa9d37bfe5dd","districts":[1,2,3,4,5,6,7,8]}),
  Object.freeze({"first":73,"last":77,"file":"Kansas_73_to_77.geojson","commit":"a72f5836d0de4ad5aa94a18b6b725b46bf71b39e","sha256":"16cbd39548f0930627179d24dad76d9e6863a67aa21e536775b896c3c19fa4a2","districts":[1,2,3,4,5,6,7]}),
  Object.freeze({"first":78,"last":87,"file":"Kansas_78_to_87.geojson","commit":"a72f5836d0de4ad5aa94a18b6b725b46bf71b39e","sha256":"a957b0294b12fc288e15776870726364b154b945d729b1ed4046849b72233589","districts":[1,2,3,4,5,6]}),
  Object.freeze({"first":88,"last":89,"file":"Kansas_88_to_89.geojson","commit":"a72f5836d0de4ad5aa94a18b6b725b46bf71b39e","sha256":"e47740d99adc02d023a7b18b04c08c77b9e5c80eff8f7f205b27bf95a0796c7f","districts":[1,2,3,4,5]}),
  Object.freeze({"first":90,"last":92,"file":"Kansas_90_to_92.geojson","commit":"a72f5836d0de4ad5aa94a18b6b725b46bf71b39e","sha256":"5ac792b75266784a8f4662709087585ff997a5d78dd3afd257f5da10104d5976","districts":[1,2,3,4,5]}),
  Object.freeze({"first":93,"last":97,"file":"Kansas_93_to_97.geojson","commit":"a72f5836d0de4ad5aa94a18b6b725b46bf71b39e","sha256":"37a3331a6f16e0fbaa1ae1cb03b570947f6502a214365dda02d1967c4cb6d477","districts":[1,2,3,4,5]}),
  Object.freeze({"first":98,"last":102,"file":"Kansas_98_to_102.geojson","commit":"a72f5836d0de4ad5aa94a18b6b725b46bf71b39e","sha256":"2d5ef44213707451c38e0f9a4c543ceb4ee8cabd853e45843f9a0f81fe721a90","districts":[1,2,3,4,5]}),
  Object.freeze({"first":103,"last":107,"file":"Kansas_103_to_107.geojson","commit":"a72f5836d0de4ad5aa94a18b6b725b46bf71b39e","sha256":"679e1c22d1651ab613b038e9d2005b0c331859c0a65763adf3b6d61315157a51","districts":[1,2,3,4]}),
  Object.freeze({"first":108,"last":112,"file":"Kansas_108_to_112.geojson","commit":"a72f5836d0de4ad5aa94a18b6b725b46bf71b39e","sha256":"c736bb1fa65a49b9ef72900ff76bbe11ce523bbb07cb8ae208d9c5b5f7d48542","districts":[1,2,3,4]}),
  Object.freeze({"first":113,"last":117,"file":"GeoJson/Kansas_113_to_117.geojson","commit":"3c663a8098b58156601e0893f0e67b502f7f8354","sha256":"ed77ae794afd16f672cdc44e38b2f7c7ad8dc6ce43415d06241db31b2a99c716","districts":[1,2,3,4]}),
  Object.freeze({"first":118,"last":119,"file":"GeoJson/Kansas_118_to_119.geojson","commit":"3c663a8098b58156601e0893f0e67b502f7f8354","sha256":"e26a35406043dbd81880f3e39a818106a9671f69b5dac2e02bddad39a4cf82a9","districts":[1,2,3,4]}),
]);
export const CIVIC_FIRST_DAY = "1861-01-29";
export const CIVIC_LAST_DAY = "2027-01-03"; // Exclusive: never carry 119th boundaries into the 120th.
export function civicTermStart(congress: number): string {
  if (!Number.isInteger(congress) || congress < 36 || congress > 120) throw new RangeError("Unsupported Congress.");
  if (congress === 36) return CIVIC_FIRST_DAY;
  return String(1787 + 2 * congress) + (congress >= 74 ? "-01-03" : "-03-04");
}
export function civicCongressForDay(day: string): number | null {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(day) || day < CIVIC_FIRST_DAY || day >= CIVIC_LAST_DAY) return null;
  const ms = Date.parse(day + "T00:00:00Z");
  if (!Number.isFinite(ms) || new Date(ms).toISOString().slice(0, 10) !== day) return null;
  for (let congress = 119; congress >= 36; congress--) if (day >= civicTermStart(congress)) return congress;
  return null;
}
export const civicCongressLabel = (congress: number) => `Congress ${congress} · ${civicTermStart(congress).slice(0, 4)}–${civicTermStart(congress + 1).slice(0, 4)}`;
export const civicHistoryPlan = (congress: number) => CIVIC_HISTORY_PLANS.find(p => p.first <= congress && congress <= p.last);
export const civicHistoryRawUrl = (plan: CivicHistoryPlan) => `https://raw.githubusercontent.com/JeffreyBLewis/congressional-district-boundaries/${plan.commit}/${plan.file}`;
export const civicHistorySourceUrl = (plan: CivicHistoryPlan) => `https://github.com/JeffreyBLewis/congressional-district-boundaries/blob/${plan.commit}/${plan.file}`;
export function civicDayForFrame(frame: number, present: number, today: string, calendarDay: string | null): string | null {
  const day = calendarDay ?? (frame === present ? today : Number.isInteger(frame) && frame >= 1861 && frame <= 2027 ? `${frame}-01-01` : "");
  return Number(day.slice(0, 4)) === frame && day <= today && civicCongressForDay(day) !== null ? day : null;
}
export function civicFrameVisible(selected: boolean, frame: number, present: number, today: string, calendarDay: string | null, checkedDay: string | undefined, buildCurrent: boolean): boolean {
  if (!selected || !buildCurrent) return false;
  const day = civicDayForFrame(frame, present, today, calendarDay);
  return Boolean(day && (checkedDay === day || !checkedDay && !calendarDay && frame === present && civicCongressForDay(day) === 119));
}
/** Historical selections belong to one checked day; the undated Census edition covers only its declared term. */
export function civicRecordMatchesDay(properties: Record<string, unknown> | null | undefined, day: string | null): boolean {
  const congress = day ? civicCongressForDay(day) : null;
  if (congress === null || properties?.congressNumber !== congress) return false;
  if (properties.sourceDay === day) return true;
  // Existing Census responses put an optional query day on the payload, not each feature.
  return congress === 119 && properties.sourceDay == null
    && properties.termStart === civicTermStart(119) && properties.termEndExclusive === civicTermStart(120);
}
/** Select source credit from the checked edition, never from arbitrary upstream text. */
export function civicSourceForRecord(properties: Record<string, unknown> | null | undefined): OfficialContextSource {
  const congress = properties?.congressNumber;
  if (typeof congress !== "number" || !Number.isInteger(congress) || congress < 36 || congress > 119) return CIVIC_SOURCE;
  const plan = congress < 119 ? civicHistoryPlan(congress) : undefined;
  return { ...CIVIC_SOURCE,
    organization: plan ? CIVIC_HISTORY_CREDIT : "U.S. Census Bureau",
    sourceUrl: plan ? civicHistorySourceUrl(plan) : CIVIC_SERVICE,
    boundary: plan ? CIVIC_HISTORY_LIMITATION : CIVIC_LIMITATION,
    freshness: `${civicCongressLabel(congress)} · ${civicTermStart(congress)} to ${civicTermStart(congress + 1)} (exclusive; calendar-day resolution)`,
    attribution: plan ? `${CIVIC_HISTORY_CREDIT} · <a href="/civic-history-license.txt">MIT license</a>` : "U.S. Census Bureau · ACS 2025 generalized districts",
  };
}
const record = (value: unknown): value is Record<string, unknown> => Boolean(value) && typeof value === "object" && !Array.isArray(value);
export function parseCivicHistory(raw: unknown, day: string, now = new Date()): OfficialContextPayload {
  const congress = civicCongressForDay(day), plan = congress && civicHistoryPlan(congress);
  if (!plan || !record(raw) || raw.type !== "FeatureCollection" || !Array.isArray(raw.features) || raw.features.length !== plan.districts.length) throw new Error("Incomplete historical plan.");
  if (raw.crs !== undefined && (!record(raw.crs) || raw.crs.type !== "name" || !record(raw.crs.properties) || raw.crs.properties.name !== "urn:ogc:def:crs:EPSG::4269")) throw new Error("Unexpected source datum.");
  const seen = new Set<number>(), budget = { vertices: 0 }, retrievedAt = now.toISOString();
  const features: Feature<Polygon | MultiPolygon>[] = raw.features.map(row => {
    if (!record(row) || row.type !== "Feature" || !record(row.properties)) throw new Error("Invalid historical district.");
    const p = row.properties, district = Number(p.district);
    const sourceId = `020${String(plan.first).padStart(3, "0")}${String(plan.last).padStart(3, "0")}${String(district).padStart(3, "0")}`;
    if (p.statename !== "Kansas" || !["number", "string"].includes(typeof p.district) || !plan.districts.includes(district) || seen.has(district) || Number(p.startcong) !== plan.first || Number(p.endcong) !== plan.last || p.id !== sourceId) throw new Error("Historical district identity changed.");
    seen.add(district);
    const geometry = validateCivicGeometry(row.geometry, budget);
    const id = `lewis-${plan.commit.slice(0, 12)}-${sourceId}`;
    return { type: "Feature" as const, id, geometry, properties: {
      featureId: id, sourceFeatureId: sourceId, district, atLargeOnly: plan.districts.length === 1, name: district === 0 ? "Kansas statewide at-large constituency" : `Kansas U.S. House District ${district}`,
      congress: civicCongressLabel(congress as number), congressNumber: congress, termStart: civicTermStart(congress as number), termEndExclusive: civicTermStart((congress as number) + 1),
      sourceDay: day, sourcePlanFirstCongress: plan.first, sourcePlanLastCongress: plan.last, sourceRevision: plan.commit, sourceSha256: plan.sha256,
      sourceUrl: civicHistorySourceUrl(plan), sourceOrganization: CIVIC_HISTORY_CREDIT, basis: "Scholarly reconstruction", sourceDatum: "NAD83 · provider zero-shift display approximation",
      retrievedAt, evidenceRole: "EXTERNAL_CONTEXT_ONLY", limitation: CIVIC_HISTORY_LIMITATION,
    } };
  }).sort((a, b) => a.properties!.district - b.properties!.district);
  return { feed: CIVIC_ID, state: "ready", retrievedAt, upstreamUpdatedAt: null, sourceDay: day, featureCount: features.length, data: { type: "FeatureCollection", features },
    source: CIVIC_HISTORY_CREDIT, license: CIVIC_HISTORY_LICENSE, limitation: CIVIC_HISTORY_LIMITATION, truncated: false };
}
