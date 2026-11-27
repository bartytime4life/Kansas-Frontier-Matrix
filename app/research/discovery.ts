import type { OfficialContextSource } from "../live-context";

export const REPRESENTATIONS = {
  SNAPSHOT_GEOJSON: "Dated snapshot",
  OPERATIONAL_GEOJSON: "Provider records",
  OPERATIONAL_WMS: "Map service",
  HISTORICAL_RASTER: "Dated imagery",
  MODEL_CANVAS: "Model display",
} as const;

export type DiscoverySource = Pick<OfficialContextSource, "id" | "title" | "shortTitle" | "organization" | "domain" | "kind" | "cadence" | "freshness" | "boundary" | "fallback" | "evidenceRole" | "attribution" | "minDisplayZoom"> & {
  sourceHref: string;
  downloadHref: string | null;
  downloadLabel: string | null;
  mapHref: string;
};
export type DiscoveryState = { query: string; domain: string; kind: string; compare: string[] };

/** Catalog navigation only. No URL from a search term or a provider response is executed. */
export function discoveryLink(value: string): string | null {
  if (/^\/(?!\/)/.test(value) && !/[\\\u0000-\u0020]/.test(value)) return value;
  try {
    const url = new URL(value);
    return url.protocol === "https:" && !url.username && !url.password ? url.href : null;
  } catch { return null; }
}

export type DiscoveryCredit = { text: string; href: string | null };

/** Only the registry's simple attribution anchors become links. Other markup stays inert text. */
export function discoveryAttribution(value: string): DiscoveryCredit[] {
  const parts: DiscoveryCredit[] = [];
  const anchors = /<a\s+href=(["'])([^"'<>]*)\1\s*>([^<>]*)<\/a\s*>/gi;
  let offset = 0;
  for (const match of value.matchAll(anchors)) {
    const start = match.index!;
    if (start > offset) parts.push({ text: value.slice(offset, start), href: null });
    parts.push({ text: match[3], href: discoveryLink(match[2]) });
    offset = start + match[0].length;
  }
  if (offset < value.length) parts.push({ text: value.slice(offset), href: null });
  return parts;
}

export function sourceMapHref(ids: readonly string[]): string {
  return `/?${new URLSearchParams({ ctx: ids.join(","), l: "", layerView: "selected", mapui: "open", maptab: "display" })}`;
}

export function discoverySources(sources: readonly OfficialContextSource[], downloads: Readonly<Record<string, { href: string; label: string }>>): DiscoverySource[] {
  return sources.map(source => ({
    id: source.id, title: source.title, shortTitle: source.shortTitle, organization: source.organization,
    domain: source.domain, kind: source.kind, cadence: source.cadence, freshness: source.freshness,
    boundary: source.boundary, fallback: source.fallback, evidenceRole: source.evidenceRole,
    attribution: source.attribution, minDisplayZoom: source.minDisplayZoom,
    sourceHref: discoveryLink(source.sourceUrl) ?? "/observatory/sources",
    downloadHref: downloads[source.id] ? discoveryLink(downloads[source.id].href) : null,
    downloadLabel: downloads[source.id]?.label ?? null, mapHref: sourceMapHref([source.id]),
  }));
}

export function readDiscoveryState(params: URLSearchParams, sources: readonly DiscoverySource[]): DiscoveryState {
  const domains = new Set(sources.map(source => source.domain));
  const ids = new Set(sources.map(source => source.id));
  const domain = params.get("domain") ?? "";
  const kind = params.get("kind") ?? "";
  return {
    query: (params.get("q") ?? "").replace(/[\u0000-\u001f\u007f]/g, "").slice(0, 160),
    domain: domains.has(domain) ? domain : "",
    kind: Object.hasOwn(REPRESENTATIONS, kind) ? kind : "",
    compare: [...new Set((params.get("compare") ?? "").split(",").filter(id => ids.has(id as DiscoverySource["id"])))].slice(0, 3),
  };
}

export function discoverySearch(sources: readonly DiscoverySource[], state: DiscoveryState): DiscoverySource[] {
  const terms = state.query.toLocaleLowerCase("en-US").trim().split(/\s+/).filter(Boolean);
  return sources.filter(source => (!state.domain || source.domain === state.domain) && (!state.kind || source.kind === state.kind)
    && terms.every(term => [source.id, source.title, source.shortTitle, source.organization, source.domain, source.cadence, source.freshness, source.boundary, source.attribution, REPRESENTATIONS[source.kind]].join(" ").toLocaleLowerCase("en-US").includes(term)));
}

export function discoveryParams(state: DiscoveryState): URLSearchParams {
  const params = new URLSearchParams();
  if (state.query) params.set("q", state.query);
  if (state.domain) params.set("domain", state.domain);
  if (state.kind) params.set("kind", state.kind);
  if (state.compare.length) params.set("compare", state.compare.join(","));
  return params;
}

export const INVESTIGATIONS = [
  { id: "water", number: "01", title: "Follow the water", question: "What is measured, and what is forecast?", detail: "Read stream observations beside radar and modeled river guidance.", ids: ["usgs-streamflow", "nws-radar", "noaa-nwm-short-range"], note: "Check station time, radar validity and model initialization separately. Spatial overlap does not establish a rainfall–runoff relationship.", className: "water" },
  { id: "groundwater", number: "02", title: "Beneath the plains", question: "How do groundwater products differ?", detail: "Compare depth to water, saturated thickness and monitoring locations.", ids: ["kgs-depth-to-water", "kgs-saturated-thickness", "kgs-monitoring-wells"], note: "Retain each product’s reference period and units. Regional estimates do not establish a current water level at a particular well.", className: "ground" },
  { id: "fire", number: "03", title: "Fire, smoke & sky", question: "Which parts of the picture are observed?", detail: "Separate satellite detections, analyzed smoke and forecast wind.", ids: ["nasa-gibs-fire-points", "noaa-hms-smoke", "nws-forecast-wind"], note: "Hotspots are detections, smoke is column context, and wind is modeled. These layers do not measure surface exposure or prove a common fire origin.", className: "fire" },
  { id: "history", number: "04", title: "A changing landscape", question: "Which dates belong to this map?", detail: "Explore historic roads, abandoned rail and a dated county baseline.", ids: ["kdot-roads-1918", "kdot-rail-abandoned", "census-counties"], note: "A historic route, a rail inventory and a Census edition have different clocks. Modern basemaps do not reconstruct the historical landscape.", className: "history" },
] as const;

/** Verified bibliographic/discovery references, never source admission or a joined dataset. */
export const RESEARCH_FRONTIER = [
  { id: "neon-konz", title: "Prairie observations, from soil to canopy", publisher: "NSF NEON · KONZ", scale: "Field site", href: "https://www.neonscience.org/field-sites/konz", description: "Konza Prairie offers soil sensors, meteorology, ecological sampling and airborne remote sensing. Start with the site’s named data products and their sampling design.", gate: "Review product availability, quality flags, release version, reuse terms and location sensitivity before a KFM import.", checked: "2026-11-23" },
  { id: "E-GEOD-16418", title: "Bluestem transcription profiles", publisher: "EMBL-EBI BioStudies / ArrayExpress", scale: "Study · Konza 2005", href: "https://www.ebi.ac.uk/biostudies/studies/E-GEOD-16418", description: "A study catalogue entry for bluestem transcription profiles at Konza. Follow the accession to inspect experiment design, sample metadata and original files.", gate: "Assay results require platform annotation, treatment and replicate review. They cannot be mapped as species abundance or statewide drought response.", checked: "2026-11-23" },
  { id: "E-GEOD-35492", title: "Bluestem & Indiangrass transcription", publisher: "EMBL-EBI BioStudies / ArrayExpress", scale: "Study · Konza 2006", href: "https://www.ebi.ac.uk/biostudies/studies/E-GEOD-35492", description: "A second Konza study linking grass species to transcriptional profiles. Compare its experimental design with the 2005 study before considering a combined analysis.", gate: "Shared place or species does not establish compatible assays, treatments or temporal support. Review source rights and analysis methods first.", checked: "2026-11-23" },
] as const;

export const RESEARCH_READING = [
  { id: "41943985", title: "Grassland resistance and resilience to extreme climate events", publisher: "Ecology Letters · 2026", href: "https://pubmed.ncbi.nlm.nih.gov/41943985/" },
  { id: "21328008", title: "Plant species loss and tallgrass prairie ecosystem function", publisher: "Oecologia · 2011", href: "https://pubmed.ncbi.nlm.nih.gov/21328008/" },
] as const;
