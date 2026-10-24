import type { Feature, Geometry } from "geojson";
import { countySearchGeometry } from "./county-search";
import type { CivicCategory, CivicSource } from "./civic-sources";

/** Discovery navigation and private reflection only; not a released evidence model. */
export const CIVIC_CATEGORIES: readonly { id: CivicCategory; title: string; question: string }[] = [
  { id: "government", title: "Who serves my area", question: "How can I identify the government offices responsible for a local issue, and check their authority?" },
  { id: "voting", title: "Voting & candidates", question: "Help me compare candidates using the same questions and dated sources, without recommending a candidate. Explain how to verify my ballot through official election sources." },
  { id: "money", title: "Money & disclosures", question: "Explain how to read public budgets, campaign finance and substantial-interest disclosures. Separate reported amounts, missing records and any conclusions the records cannot support." },
  { id: "laws", title: "Laws & decisions", question: "How can I trace a proposed bill through amendments, recorded votes, enactment and its effective date? Separate legal changes from claims about their effects." },
  { id: "work-services", title: "Jobs & services", question: "Help me plan a search for official government jobs and public services. Identify what I must confirm with the responsible agency, including eligibility and deadlines." },
  { id: "history", title: "Government over time", question: "How can I compare past and present government decisions without applying today's officeholders or boundaries to the past?" },
  { id: "wellbeing", title: "Life & local outcomes", question: "How should I compare cost of living, jobs, public spending and wellbeing over time? Explain uncertainty, survey coverage and why a trend alone cannot show that an official caused it." },
];

export const CIVIC_REFLECTION_LENSES = [
  { id: "fairness", title: "Fair treatment", question: "Who benefits, who bears the cost, and whose experience is missing?" },
  { id: "freedom", title: "Freedom & rights", question: "Which choices and rights are affected, and what safeguards exist?" },
  { id: "wellbeing", title: "Everyday wellbeing", question: "What changes for health, safety, opportunity and access to services?" },
  { id: "stewardship", title: "Public money", question: "What is funded, what is displaced, and how will results be checked?" },
  { id: "future", title: "Future generations", question: "Which costs, benefits and environmental effects arrive later?" },
] as const;

export function civicSourceUrl(value: string): string | null {
  try {
    const url = new URL(value);
    return url.protocol === "https:" && !url.username && !url.password ? url.href : null;
  } catch { return null; }
}

export function filterCivicSources(sources: readonly CivicSource[], category: CivicCategory | "all", query: string): CivicSource[] {
  const terms = query.trim().toLocaleLowerCase("en-US").split(/\s+/).filter(Boolean);
  return sources.filter(source => civicSourceUrl(source.url) && (category === "all" || source.category === category)
    && terms.every(term => `${source.title} ${source.organization} ${source.description} ${source.geography} ${(source.tags ?? []).join(" ")}`.toLocaleLowerCase("en-US").includes(term)));
}

export type CivicSourceWindow = Readonly<{ filterKey: string; limit: number }>;
export function civicSourcePage<T>(sources: readonly T[], filterKey: string, window: CivicSourceWindow | null) {
  const requested = window?.filterKey === filterKey && Number.isSafeInteger(window.limit) && window.limit >= 12 ? window.limit : 12;
  const shown = Math.min(sources.length, requested);
  return { items: sources.slice(0, shown), total: sources.length, shown, hasMore: shown < sources.length, nextLimit: shown + 12 };
}

export type CivicCounty = Readonly<{ geoid: string; title: string; center: readonly [number, number]; zoom: number; edition: "2020" }>;
const object = (value: unknown): value is Record<string, unknown> => Boolean(value) && typeof value === "object" && !Array.isArray(value);

/** Checks the existing adapter's expected row count and unique identities, not independent completeness or electoral authority. */
export function civicCounties(value: unknown): CivicCounty[] {
  if (!object(value) || value.edition !== "2020" || !object(value.data) || value.data.type !== "FeatureCollection"
    || !Array.isArray(value.data.features) || value.data.features.length !== 105) return [];
  const result: CivicCounty[] = [], seen = new Set<string>();
  for (const feature of value.data.features) {
    if (!object(feature) || !object(feature.properties) || !object(feature.geometry)) return [];
    const p = feature.properties;
    if (typeof p.geoid !== "string" || !/^20\d{3}$/.test(p.geoid) || seen.has(p.geoid)
      || p.featureId !== `us-census-county-${p.geoid}` || p.vintage !== "2020"
      || typeof p.name !== "string" || !p.name.trim() || p.name.length > 100 || /[\x00-\x1f\x7f]/.test(p.name)) return [];
    const frame = countySearchGeometry(feature as unknown as Feature<Geometry>);
    if (!frame || frame.bounds[0][0] < -103 || frame.bounds[1][0] > -94 || frame.bounds[0][1] < 36 || frame.bounds[1][1] > 41) return [];
    seen.add(p.geoid);
    const span = Math.max(frame.bounds[1][0] - frame.bounds[0][0], (frame.bounds[1][1] - frame.bounds[0][1]) * 1.5);
    result.push({ geoid: p.geoid, title: /\bcounty$/i.test(p.name.trim()) ? p.name.trim() : `${p.name.trim()} County`, center: frame.focus,
      zoom: Math.max(5, Math.min(9, Math.log2(180 / span))), edition: "2020" });
  }
  return result.sort((a, b) => a.title.localeCompare(b.title, "en-US"));
}

/** Only existing Explorer camera/context parameters; never an electoral assignment. */
export function civicMapHref(county: CivicCounty | null): string {
  const params = new URLSearchParams({ ctx: "census-counties" });
  if (county && /^20\d{3}$/.test(county.geoid) && county.edition === "2020" && county.center.length === 2
    && county.center.every(Number.isFinite) && county.center[0] >= -103 && county.center[0] <= -94
    && county.center[1] >= 36 && county.center[1] <= 41 && Number.isFinite(county.zoom) && county.zoom >= 5 && county.zoom <= 9) {
    params.set("c", county.center.map(value => value.toFixed(5)).join(","));
    params.set("z", county.zoom.toFixed(2));
  }
  return `/?${params.toString()}`;
}

export function civicQuestion(category: CivicCategory | "all", county: CivicCounty | null): string {
  const question = CIVIC_CATEGORIES.find(item => item.id === category)?.question
    ?? "Help me investigate a Kansas civic question using official sources. Separate confirmed records, interpretations and missing evidence; do not rank candidates or infer causation from a trend.";
  return `${county ? `For ${county.title}, Kansas: ` : "For Kansas: "}${question} Cite checked sources for factual claims, or say what still needs verification. A directory link alone is not evidence of a factual claim.`;
}
