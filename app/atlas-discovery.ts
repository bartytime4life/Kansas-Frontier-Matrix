import { countySearchResults, type CountySearchItem } from "./county-search";
import type { SearchItem } from "./explorer-data";
import type { OfficialContextId, OfficialContextPayload, OfficialContextSource, OfficialContextState } from "./live-context";

export type OfficialSourceSearchItem = Readonly<{
  id: string;
  kind: "source";
  title: string;
  subtitle: string;
  officialContextId: OfficialContextId;
}>;

export type GlobalSearchItem = SearchItem | OfficialSourceSearchItem | CountySearchItem;

// A display-only index over records already available to this investigation.
// It does not fetch data, resolve evidence, or select a search result.
export function atlasDiscoveryResults(
  query: string,
  settledQuery: string,
  index: readonly SearchItem[],
  sources: readonly OfficialContextSource[],
  payload: OfficialContextPayload | undefined,
  state: OfficialContextState,
): GlobalSearchItem[] {
  const term = settledQuery.trim().toLowerCase();
  if (!term || term !== query.trim().toLowerCase()) return [];
  const mapResults: GlobalSearchItem[] = index.filter((item) => `${item.title} ${item.subtitle}`.toLowerCase().includes(term));
  const sourceTerms = term.split(/\s+/);
  const sourceResults: GlobalSearchItem[] = sources
    .filter((source) => {
      // Match provider and dataset terms in either order, as in the Layers catalog.
      // Keep limitations and fallback copy out of the discovery index.
      const searchable = `${source.id} ${source.title} ${source.shortTitle} ${source.organization} ${source.domain} ${source.endpointLabel}`.toLowerCase();
      return sourceTerms.every((word) => searchable.includes(word));
    })
    .map((source) => ({ id: `source:${source.id}`, kind: "source", title: source.shortTitle, subtitle: `${source.organization} · ${source.domain}`, officialContextId: source.id }));
  const counties = countySearchResults(payload, state, term);
  return [...counties, ...sourceResults, ...mapResults].slice(0, 7);
}
