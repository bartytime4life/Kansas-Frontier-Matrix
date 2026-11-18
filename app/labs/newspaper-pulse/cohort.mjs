const TOKEN = /^[\p{L}\p{N}]{1,40}$/u;
const normalize = text => text.normalize('NFKC').toLowerCase();
export const MAX_INDEXED_PAGES = 24;

export function normalizeWord(value) {
  if (typeof value !== 'string' || value.length > 80) return null;
  const word = normalize(value.trim());
  return TOKEN.test(word) ? word : null;
}

/** A page contributes at most one hit per searchable OCR token. */
export function pageWords(text) {
  const words = normalize(text).match(/[\p{L}\p{N}]+/gu) ?? [];
  return new Set(words.filter(word => TOKEN.test(word)));
}

export function compareIssues(cohort, first, second) {
  const terms = [first, second].map(normalizeWord);
  if (terms.includes(null) || terms[0] === terms[1]) return null;
  const masks = terms.map(term => Object.hasOwn(cohort.index, term) ? cohort.index[term] : 0);
  let pageOffset = 0;
  const issues = cohort.issues.map(issue => {
    const pages = issue.pages.map(page => {
      const bit = 2 ** pageOffset++;
      return { ...page, matches: masks.map(mask => Boolean(mask & bit)) };
    });
    const totals = terms.map((_, index) => pages.filter(page => page.matches[index]).length);
    return { ...issue, pages, totals, shares: totals.map(count => pages.length ? count / pages.length : null) };
  });
  return { terms, issues };
}

export function comparisonReceipt(cohort, comparison) {
  return {
    format: 'kfm-newspaper-pulse-comparison-v1',
    title: cohort.title,
    lccn: cohort.lccn,
    source: cohort.source,
    retrievedAt: cohort.retrievedAt,
    cohort: 'All digitized pages listed by the two edition inventories. OCR was present on every page.',
    method: 'Case-insensitive whole-word matches in uncorrected OCR. One hit per word per page.',
    limitation: 'The editions are a fixed selection. The results cannot describe other editions or periods.',
    ...comparison,
  };
}
