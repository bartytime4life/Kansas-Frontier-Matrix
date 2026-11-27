import { COMPARISON_YEARS } from './comparison-model.mjs';

export const comparisonYears = Object.freeze([...COMPARISON_YEARS].reverse());
const [lastYear, previousYear] = comparisonYears;

/** @param {string[]} values */
function yearFrom(values) {
  if (values.length !== 1 || !/^\d{4}$/.test(values[0])) return null;
  const year = Number(values[0]);
  return comparisonYears.includes(year) ? year : null;
}

/** @param {string} search */
export function comparisonSelection(search) {
  const params = new URLSearchParams(search);
  const year = yearFrom(params.getAll('year')) ?? lastYear;
  const requested = yearFrom(params.getAll('compare'));
  const compareYear = requested !== null && requested !== year ? requested : year === lastYear ? previousYear : lastYear;
  return { year, compareYear };
}

/** @param {{ year: number, compareYear: number }} selection */
export function comparisonPath({ year, compareYear }) {
  if (!comparisonYears.includes(year) || !comparisonYears.includes(compareYear) || year === compareYear) {
    throw new Error('Choose two distinct comparison years.');
  }
  return `/science/compare?year=${year}&compare=${compareYear}`;
}
