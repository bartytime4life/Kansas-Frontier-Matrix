import { YEARS } from '../science-model.mjs';
import { comparisonPlace, DEFAULT_COMPARISON_PLACE } from './comparison-places.mjs';

export const comparisonYears = Object.freeze([...YEARS].reverse());
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
  const places = params.getAll('place');
  const place = (places.length === 1 ? comparisonPlace(places[0])?.id : undefined) ?? DEFAULT_COMPARISON_PLACE;
  return { year, compareYear, place };
}

/** @param {{ year: number, compareYear: number, place?: string }} selection */
export function comparisonPath({ year, compareYear, place = DEFAULT_COMPARISON_PLACE }) {
  if (!comparisonYears.includes(year) || !comparisonYears.includes(compareYear) || year === compareYear) {
    throw new Error('Choose two distinct comparison years.');
  }
  if (!comparisonPlace(place)) throw new Error('Choose a supported Kansas comparison area.');
  return `/science/compare?year=${year}&compare=${compareYear}${place === DEFAULT_COMPARISON_PLACE ? '' : `&place=${place}`}`;
}

/** @param {string} metric @param {number} year @param {string} [place] */
export function comparisonLabPath(metric, year, place = DEFAULT_COMPARISON_PLACE) {
  const area = comparisonPlace(place);
  if (!area || !comparisonYears.includes(year)) return null;
  const { climateId, countyId, sunlightId } = area;
  switch (metric) {
    case 'climate': return `/labs/heat-and-rain?station=${climateId}&year=${year}`;
    case 'drought': return `/labs/county-drought?county=${countyId}&from=${year}&to=${year}`;
    case 'air': return `/labs/daily-air-quality?county=${countyId}&year=${year}`;
    case 'sunlight': return `/labs/sunlight-and-sky?primary=${sunlightId}&comparison=${sunlightId}&year=${year}`;
    default: return null;
  }
}
