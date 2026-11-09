/** Catalogue helpers use only metadata and observations supplied by the source adapter. */
export function atlasFacts(bundle) {
  if (!bundle?.data) return [];
  const data = bundle.data;
  if (Array.isArray(data.records)) {
    const facts = [{ value: data.records.length, label: 'source records' }];
    if (data.categoryField) {
      const categories = new Set(data.records.map(row => row[data.categoryField]).filter(value => value != null && value !== ''));
      if (categories.size > 1) facts.push({ value: categories.size, label: 'groups to compare' });
    }
    if (Array.isArray(data.columns)) facts.push({ value: data.columns.length, label: 'record fields' });
    return facts.slice(0, 2);
  }
  if (Array.isArray(data.areas)) return [{ value: data.years?.length ?? 0, label: 'years in the record' }, { value: data.areas.length, label: 'areas to compare' }];
  if (Array.isArray(data.lines)) return [{ value: data.lines.length, label: 'source segments' }, { value: data.years?.length ?? 0, label: 'dated benchmarks' }];
  return [];
}

export function atlasStatus(story, state) {
  if (story.status !== 'ready') return { label: 'In development', tone: 'planned' };
  if (state === 'ready') return { label: 'Source snapshot ready', tone: 'ready' };
  if (state === 'offline') return { label: 'Source unavailable', tone: 'offline' };
  if (state === 'waiting') return { label: 'Awaiting source release', tone: 'waiting' };
  if (state === 'loading') return { label: 'Checking source…', tone: 'loading' };
  return { label: 'Source not yet checked', tone: 'idle' };
}

export function atlasCoverage(bundle) {
  const { from, to } = bundle?.observed || {};
  if (from == null || to == null) return null;
  if (bundle?.data?.timeUnit === 'Ma') {
    const ages = [Number(from), Number(to)].map(Math.abs);
    if (ages.every(Number.isFinite)) {
      const format = new Intl.NumberFormat('en-US', { maximumFractionDigits: 2 });
      return `${format.format(Math.max(...ages))}–${format.format(Math.min(...ages))} Ma`;
    }
    return 'Geological age coverage in source';
  }
  const year = value => String(value).match(/^\d{4}(?=-|$)/)?.[0] || String(value).slice(0, 10);
  const first = year(from), last = year(to);
  return first === last ? first : `${first}–${last}`;
}

export function matchesAtlasStory(story, { query = '', group = 'All', availability = 'all', states = {} } = {}) {
  const terms = query.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
  const text = [story.title, story.kicker, story.summary, story.group, ...(story.sources || [])].join(' ').toLocaleLowerCase();
  if (terms.some(term => !text.includes(term))) return false;
  if (group !== 'All' && story.group !== group) return false;
  if (availability === 'ready' && (story.status !== 'ready' || states[story.id] !== 'ready')) return false;
  if (availability === 'planned' && story.status !== 'planned') return false;
  return true;
}

export function storyFromSearch(search, stories) {
  const id = new URLSearchParams(search).get('story');
  return stories.some(story => story.id === id) ? id : null;
}

export function storyLocation(href, id) {
  const url = new URL(href);
  if (id) url.searchParams.set('story', id);
  else url.searchParams.delete('story');
  return `${url.pathname}${url.search}${url.hash}`;
}
