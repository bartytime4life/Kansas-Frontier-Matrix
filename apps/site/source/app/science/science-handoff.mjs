/** Public science navigation and user-initiated project inquiry drafts. No I/O. */
export const SCIENCE_YEARS = Object.freeze([2025, 2024, 2023, 2022, 2021, 2020]);
export const SCIENCE_TOOLS = Object.freeze([
  { id: 'weather', label: 'Heat & Rain', path: '/labs/heat-and-rain', question: 'Explore daily heat and precipitation', support: 'Three NOAA weather stations; select a station inside the lab.' },
  { id: 'drought', label: 'County Drought', path: '/labs/county-drought', question: 'Compare county drought assessments', support: '105 Kansas counties; weekly assessed area, not drought days.' },
  { id: 'soil', label: 'Soil Profile', path: '/labs/soil-profile', question: 'Inspect measured soil moisture and temperature', support: 'Two NOAA stations and five measured depths; gaps remain visible.' },
  { id: 'air', label: 'Daily Air Quality', path: '/labs/daily-air-quality', question: 'Inspect reported daily air quality', support: 'Twelve reporting counties; coverage varies and exposure is not inferred.' },
  { id: 'sunlight', label: 'Sunlight & Sky', path: '/labs/sunlight-and-sky', question: 'Compare modeled daily sunlight energy', support: 'Three NASA POWER query points on a nominal 1° radiation grid.' },
  { id: 'comparison', label: 'Year comparison', path: '/science/compare', question: 'Compare two years in Topeka', support: 'Topeka station and model context beside Shawnee County summaries; each keeps its own scale.' },
].map(Object.freeze));

export const SERVICE_OPTIONS = Object.freeze([
  { id: 'brief', label: 'Custom evidence brief', deliverable: 'A focused question, source-linked figures, coverage notes and a reproducible data appendix.' },
  { id: 'data', label: 'Reusable data pack', deliverable: 'A scoped, documented data table with source lineage, units, quality flags and preparation steps.' },
  { id: 'walkthrough', label: 'Guided team walkthrough', deliverable: 'A question-led session using the public tools, with a short reading guide and next steps.' },
].map(Object.freeze));

export const INQUIRY_CONTACT = 'Andy.barta.pro@gmail.com';
export const INQUIRY_LIMITS = Object.freeze({ question: 600, area: 160, timing: 80 });
const PUBLIC_ORIGIN = 'https://kansasfrontiermatrix.com';
const toolById = id => SCIENCE_TOOLS.find(tool => tool.id === id);
const inList = values => value => values.includes(value);
const bounded = (low, high, integer = false) => value => {
  if (!/^-?\d+(?:\.\d+)?$/.test(value)) return false;
  const number = Number(value);
  return Number.isFinite(number) && number >= low && number <= high && (!integer || Number.isInteger(number));
};
const year = inList(SCIENCE_YEARS.map(String));
const month = bounded(0, 12, true);
const county = value => /^20\d{3}$/.test(value) && Number(value.slice(2)) >= 1 && Number(value.slice(2)) <= 209 && Number(value.slice(2)) % 2 === 1;
const calendarDate = value => {
  if (!/^202[0-5]-\d{2}-\d{2}$/.test(value)) return false;
  const parsed = new Date(`${value}T12:00:00Z`);
  return Number.isFinite(parsed.getTime()) && parsed.toISOString().slice(0, 10) === value;
};
const point = inList(['dodge-city', 'wichita', 'topeka']);
const selectors = Object.freeze({
  weather: { station: inList(['USW00013985', 'USW00003928', 'USW00013996']), year, month, units: inList(['metric', 'imperial']), heat: bounded(-60, 60), wet: bounded(0.1, 500) },
  drought: { county, compare: county, from: year, to: year, level: bounded(1, 4, true), threshold: value => bounded(0.01, 100)(value) && Number(value) === Math.round(Number(value) * 100) / 100 },
  soil: { station: inList(['53974', '03067']), year, month, depth: inList(['5', '10', '20', '50', '100']), variable: inList(['moisture', 'temperature']), date: calendarDate },
  air: { county: inList(['20017', '20045', '20057', '20091', '20103', '20133', '20173', '20177', '20181', '20191', '20195', '20209']), year, month, threshold: bounded(0, 500, true), date: calendarDate },
  sunlight: { primary: point, comparison: point, year, month, date: calendarDate },
  comparison: { year, compare: year },
});

/** Launch one native tool at a supported year; locations remain tool-specific. */
export function scienceToolPath(toolId, selectedYear = 2025) {
  const tool = toolById(toolId);
  if (!tool || !SCIENCE_YEARS.includes(selectedYear)) throw new Error('Choose a science tool and a supported year.');
  if (toolId === 'drought') return `${tool.path}?from=${selectedYear}&to=${selectedYear}`;
  if (toolId === 'comparison') return `${tool.path}?year=${selectedYear}&compare=${selectedYear === 2025 ? 2024 : 2025}`;
  return `${tool.path}?year=${selectedYear}`;
}

/**
 * Only exact public science routes and their documented, bounded selectors may
 * enter an inquiry. Reject unknown/repeated selectors rather than echoing URLs
 * that could contain coordinates, credentials, foreign origins or free text.
 */
export function safeScienceContext(raw) {
  if (typeof raw !== 'string' || raw.length > 1200 || !raw.startsWith('/') || raw.startsWith('//') || /[\\\s#\x00-\x1f\x7f]/.test(raw)) return null;
  let url;
  try { url = new URL(raw, PUBLIC_ORIGIN); } catch { return null; }
  if (url.origin !== PUBLIC_ORIGIN || url.username || url.password) return null;
  const tool = SCIENCE_TOOLS.find(item => item.path === url.pathname);
  if (!tool || raw.split('?')[0] !== tool.path) return null;
  const rules = selectors[tool.id];
  for (const [key, value] of url.searchParams) {
    if (!Object.hasOwn(rules, key) || url.searchParams.getAll(key).length !== 1 || !rules[key](value)) return null;
  }
  const params = url.searchParams;
  if (tool.id === 'drought') {
    if (params.has('from') && params.has('to') && Number(params.get('from')) > Number(params.get('to'))) return null;
    if (params.has('county') && params.get('county') === params.get('compare')) return null;
  }
  if (tool.id === 'comparison' && params.has('year') && params.get('year') === params.get('compare')) return null;
  if (params.has('date')) {
    const date = params.get('date');
    if (!params.has('year') || !date.startsWith(params.get('year'))) return null;
    if (params.has('month') && Number(params.get('month')) !== 0 && Number(date.slice(5, 7)) !== Number(params.get('month'))) return null;
  }
  const ordered = new URLSearchParams();
  for (const key of Object.keys(rules)) if (params.has(key)) ordered.set(key, params.get(key));
  return `${tool.path}${ordered.size ? `?${ordered}` : ''}`;
}

/** Serialize a lab's normalized live selection, including inspected date. */
export function scienceSelectionPath(toolId, selection) {
  const tool = toolById(toolId);
  if (!tool || !selection || typeof selection !== 'object' || Array.isArray(selection)) throw new Error('Science selection unavailable.');
  const values = toolId === 'drought'
    ? { county: selection.countyId, compare: selection.compareId, from: selection.fromYear, to: selection.toYear, level: selection.level, threshold: selection.threshold }
    : toolId === 'comparison' ? { year: selection.year, compare: selection.compareYear } : selection;
  const query = new URLSearchParams();
  for (const key of Object.keys(selectors[toolId])) {
    const value = values[key];
    if (value !== undefined && value !== null) query.set(key, String(value));
  }
  const path = safeScienceContext(`${tool.path}${query.size ? `?${query}` : ''}`);
  if (!path) throw new Error('Science selection unavailable.');
  return path;
}

export function serviceInquiryPath(context = '', service = 'brief') {
  const params = new URLSearchParams();
  if (SERVICE_OPTIONS.some(option => option.id === service)) params.set('service', service);
  const path = safeScienceContext(context);
  if (path) params.set('context', path);
  return `/science/services${params.size ? `?${params}` : ''}`;
}

export function readInquirySelection(search = '') {
  const params = new URLSearchParams(typeof search === 'string' && search.length <= 2400 ? search : '');
  const requested = params.getAll('service');
  const service = requested.length === 1 && SERVICE_OPTIONS.some(option => option.id === requested[0]) ? requested[0] : 'brief';
  const contexts = params.getAll('context');
  const context = contexts.length === 1 ? safeScienceContext(contexts[0]) : null;
  return Object.freeze({ service, context });
}

function inquiryField(value, key) {
  if (typeof value !== 'string' || value.length > INQUIRY_LIMITS[key] || /[\x00-\x08\x0b-\x1f\x7f]/.test(value)) throw new Error(`Check the ${key} field and its length.`);
  // Reject malformed Unicode before URI encoding. Text is never silently cut.
  if (typeof value.isWellFormed === 'function' && !value.isWellFormed()) throw new Error(`Check the ${key} field.`);
  return value.trim();
}

/** Compose locally. The caller decides whether to copy, download or open mail. */
export function inquiryDraft({ service = 'brief', question = '', area = '', timing = '', context = '' } = {}) {
  const option = SERVICE_OPTIONS.find(item => item.id === service);
  if (!option) throw new Error('Choose a custom-work service.');
  const cleanQuestion = inquiryField(question, 'question');
  const cleanArea = inquiryField(area, 'area');
  const cleanTiming = inquiryField(timing, 'timing');
  const path = safeScienceContext(context);
  const subject = `KFM project inquiry: ${option.label}`;
  const text = [
    'KFM PROJECT INQUIRY',
    `Service: ${option.label}`,
    `Question / intended use: ${cleanQuestion || '(add a question)'}`,
    `General area: ${cleanArea || '(to discuss)'}`,
    `Desired timing: ${cleanTiming || '(to discuss)'}`,
    ...(path ? [`Starting analysis: ${PUBLIC_ORIGIN}${path}`] : []),
    '',
    'Please discuss data coverage, deliverables, availability and a quote before any work begins.',
    'The public KFM science tools and self-service report downloads remain free.',
    'This is a project inquiry, not a purchase or an assurance of scientific review.',
  ].join('\n');
  return Object.freeze({
    service: option.id, context: path, text,
    canEmail: Boolean(cleanQuestion),
    mailto: `mailto:${INQUIRY_CONTACT}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(text)}`,
    filename: `kfm-${option.id}-project-inquiry.txt`,
  });
}
