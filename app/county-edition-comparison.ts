export type CountyCounts = { geoid: string; name: string; population: number | null; housingUnits: number | null };
export type CountyEditionData = { edition: "2010" | "2020"; source: string; retrievedAt: string; limitation: string; rows: CountyCounts[] };
const count = (value: unknown) => {
  if (value === null) return null;
  if (typeof value !== "number" || !Number.isSafeInteger(value) || value < 0) throw new Error("Invalid Census count");
  return value;
};
export function decodeCountyEdition(value: unknown, edition: CountyEditionData["edition"]): CountyEditionData {
  if (!value || typeof value !== "object") throw new Error("Missing Census edition");
  const v = value as Record<string, unknown>, data = v.data as { type?: string; features?: { properties?: Record<string, unknown> }[] } | undefined;
  if (v.edition !== edition || typeof v.source !== "string" || typeof v.retrievedAt !== "string" || !Number.isFinite(Date.parse(v.retrievedAt)) || typeof v.limitation !== "string" || data?.type !== "FeatureCollection" || !Array.isArray(data.features) || data.features.length !== 105) throw new Error("Incomplete Census edition");
  const source = new URL(v.source);
  if (source.protocol !== "https:" || source.hostname !== "tigerweb.geo.census.gov" || source.username || source.password) throw new Error("Invalid Census source");
  const ids = new Set<string>();
  const rows = data.features.map(feature => {
    const p = feature.properties;
    if (!p || typeof p.geoid !== "string" || !/^20\d{3}$/.test(p.geoid) || ids.has(p.geoid) || typeof p.name !== "string" || !p.name.trim() || p.vintage !== edition || p.evidenceRole !== "EXTERNAL_CONTEXT_ONLY") throw new Error("Invalid Census county identity");
    ids.add(p.geoid);
    return { geoid: p.geoid, name: p.name, population: count(p.population), housingUnits: count(p.housingUnits) };
  });
  return { edition, source: v.source, retrievedAt: v.retrievedAt, limitation: v.limitation, rows };
}
export function compareCountyEditions(a: CountyEditionData, b: CountyEditionData, geoid: string | null = null) {
  const right = new Map(b.rows.map(row => [row.geoid, row]));
  if (a.rows.length !== 105 || new Set(a.rows.map(row => row.geoid)).size !== 105 || right.size !== 105 || a.rows.some(row => !right.has(row.geoid))) throw new Error("County editions do not match by FIPS");
  const pairs = a.rows.filter(row => geoid === null || row.geoid === geoid).map(row => ({ a: row, b: right.get(row.geoid)! }));
  if (!pairs.length) throw new Error("County not found");
  const total = (side: "a" | "b", key: "population" | "housingUnits") => pairs.some(pair => pair[side][key] === null) ? null : pairs.reduce((sum, pair) => {
    const next = sum + pair[side][key]!;
    if (!Number.isSafeInteger(next)) throw new Error("Census total exceeds exact integer range");
    return next;
  }, 0);
  const metric = (key: "population" | "housingUnits") => {
    const first = total("a", key), second = total("b", key);
    return { a: first, b: second, delta: first === null || second === null ? null : second - first, percent: first === null || second === null || first === 0 ? null : (second - first) / first * 100 };
  };
  return { format: "kfm-census-edition-comparison-v1", evidenceRole: "EXTERNAL_CONTEXT_ONLY", publicationState: "NOT_KFM_RELEASE",
    scope: geoid === null ? "All 105 Kansas counties" : pairs[0].b.name, geoid, matchedCounties: pairs.length,
    editions: [a.edition, b.edition], sources: [a, b].map(({ edition, source, retrievedAt, limitation }) => ({ edition, source, retrievedAt, limitation })),
    population: metric("population"), housingUnits: metric("housingUnits"), rows: pairs,
  };
}
