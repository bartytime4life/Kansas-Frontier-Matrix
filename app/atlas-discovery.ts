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
  const matchesWordPrefixes = (value: string) => {
    const words = value.match(/[\p{L}\p{N}]+/gu) ?? [];
    return sourceTerms.every((term) => words.some((word) => word.startsWith(term)));
  };
  const sourceResults: GlobalSearchItem[] = sources
    .flatMap((source, position) => {
      // Match provider and dataset terms in either order, as in the Layers catalog.
      // Keep limitations and fallback copy out of the discovery index.
      const searchable = `${source.id} ${source.title} ${source.shortTitle} ${source.organization} ${source.domain} ${source.endpointLabel}`.toLowerCase();
      if (!sourceTerms.every((word) => searchable.includes(word))) return [];
      const names = [source.id, source.title, source.shortTitle].map((name) => name.toLowerCase());
      // Display relevance only: a match inside "groundwater" must not hide
      // explicit water datasets or river context behind the seven-row cap.
      const rank = names.includes(term) ? 0 : matchesWordPrefixes(names.join(" ")) ? 1 : matchesWordPrefixes(searchable) ? 2 : 3;
      return [{ source, position, rank }];
    })
    .sort((a, b) => a.rank - b.rank || a.position - b.position)
    .map(({ source }) => ({ id: `source:${source.id}`, kind: "source", title: source.shortTitle, subtitle: `${source.organization} · ${source.domain}`, officialContextId: source.id }));
  const counties = countySearchResults(payload, state, term);
  return [...counties, ...sourceResults, ...mapResults].slice(0, 7);
}
