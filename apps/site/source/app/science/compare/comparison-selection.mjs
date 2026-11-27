import { COMPARISON_YEARS, TOPEKA_COMPARISON } from './comparison-model.mjs';

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

/** @param {string} metric @param {number} year */
export function comparisonLabPath(metric, year) {
  const { climateId, countyId, sunlightId } = TOPEKA_COMPARISON;
  switch (metric) {
    case 'climate': return `/labs/heat-and-rain?station=${climateId}&year=${year}`;
    case 'drought': return `/labs/county-drought?county=${countyId}&from=${year}&to=${year}`;
    case 'air': return `/labs/daily-air-quality?county=${countyId}&year=${year}`;
    case 'sunlight': return `/labs/sunlight-and-sky?primary=${sunlightId}&comparison=${sunlightId}&year=${year}`;
    default: return null;
  }
}
