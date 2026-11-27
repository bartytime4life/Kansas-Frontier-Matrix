import { analyseAir, airReceipt } from '../../labs/daily-air-quality/air-model.mjs';
import { analyseClimate } from '../../labs/heat-and-rain/climate-model.mjs';
import { analyseDrought } from '../../labs/county-drought/drought-model.mjs';
import { analyseSunlight } from '../../labs/sunlight-and-sky/sunlight-model.mjs';
import { sameSource, YEARS } from '../science-model.mjs';

export const COMPARISON_YEARS = YEARS;
export const TOPEKA_COMPARISON = Object.freeze({
  id: 'topeka', name: 'Topeka and Shawnee County', climateId: 'USW00013996', countyId: '20177', sunlightId: 'topeka',
});

export const COMPARISON_METRICS = Object.freeze([
  Object.freeze({ id: 'climate', label: 'Reported precipitation', unit: 'mm', kind: 'observed', supportUnit: 'days',
    labPath: '/labs/heat-and-rain', timeStandard: 'NOAA station observation date',
    method: 'Sum of qualified daily liquid-equivalent precipitation, including water from melted snow.',
    limitation: 'The total covers quantified days. Trace, partial accumulation periods and withheld readings reduce support.' }),
  Object.freeze({ id: 'drought', label: 'Peak severe drought coverage', unit: '%', kind: 'assessed', supportUnit: 'assessments',
    labPath: '/labs/county-drought', timeStandard: 'USDM Tuesday assessment date',
    method: 'Maximum county area classified as severe drought or worse (D2+). Each month uses the Tuesday assessment dates inside it.',
    limitation: 'The maximum describes observed weekly county assessments. It does not measure drought duration or conditions at the station.' }),
  Object.freeze({ id: 'air', label: 'Peak daily air quality index', unit: 'AQI', kind: 'reported', supportUnit: 'days',
    labPath: '/labs/daily-air-quality', timeStandard: 'EPA county reporting date',
    method: 'Maximum reported daily county AQI over the days with an EPA value.',
    limitation: 'Daily county AQI uses the highest qualifying monitor value. Use it as reported county monitor context.' }),
  Object.freeze({ id: 'sunlight', label: 'Mean all-sky solar energy', unit: 'kWh/m²/day', kind: 'modeled', supportUnit: 'days',
    labPath: '/labs/sunlight-and-sky', timeStandard: 'NASA Local Solar Time (LST)',
    method: 'Mean of valid NASA POWER all-sky incoming horizontal shortwave energy estimates.',
    limitation: 'The point query represents a nominal 1° grid. Use the value as modeled solar resource context.' }),
]);

const limitingNotes = Object.freeze([
  'Years are complete calendar windows. Each value summarizes the available reports or modeled days, with the expected dates shown alongside it.',
  'The station, county and grid represent different spatial supports. Month and year labels use the provider’s date convention.',
  'Read each indicator separately as historical context. Comparisons support questions to investigate, with no shared score or daily alignment.',
]);

function displayIdentity(descriptor) {
  const { url, sha256, bytes } = descriptor ?? {};
  if (typeof sha256 !== 'string' || sha256.length !== 64 || !/^[a-f0-9]+$/.test(sha256) ||
      typeof url !== 'string' || !/^\/science-data\/[a-z-]+\/[a-z0-9-]+\.json$/.test(url) ||
      !url.endsWith(`-${sha256.slice(0, 16)}.json`) || !Number.isInteger(bytes) || bytes < 1) {
    throw new Error('Use the verified display descriptor for each science snapshot.');
  }
  return { url, sha256, bytes };
}

const measure = (value, valid, expected) => ({ value: valid ? value : null, valid, expected });
const climateMeasure = summary => measure(summary.rainMm, summary.valid.prcp, summary.expected);
const airMeasure = summary => measure(summary.maxAqi, summary.reported, summary.expected);
const sunlightMeasure = summary => measure(summary.primary.mean, summary.primary.validDays, summary.expected);

function droughtMonth(weeks, month) {
  const expected = weeks.filter(week => Number(week.date.slice(5, 7)) === month);
  const values = expected.filter(week => !week.missing).map(week => week.share);
  return measure(values.length ? Math.max(...values) : null, values.length, expected.length);
}

function compareMetric(metric, metadata, annual, monthly) {
  return { ...metric, ...metadata, annual: { selected: annual(0), comparison: annual(1) },
    monthly: Array.from({ length: 12 }, (_, index) => ({ month: index + 1,
      selected: monthly(0, index), comparison: monthly(1, index) })) };
}

/** Build a read-only report from objects returned by the labs' verified snapshot loaders. */
export function buildScienceComparison({ climate, drought, air, sunlight }, { year = 2025, compareYear = 2024 } = {}, descriptors) {
  const { climateId, countyId, sunlightId, id, name } = TOPEKA_COMPARISON;
  if (!COMPARISON_YEARS.includes(year) || !COMPARISON_YEARS.includes(compareYear) || year === compareYear) {
    throw new Error('Choose two different calendar years from 2020 through 2025.');
  }
  if (climate?.station?.id !== climateId || descriptors?.climate?.id !== climateId ||
      !sameSource(climate.source, descriptors.climate.source) || sunlight?.point?.id !== sunlightId ||
      descriptors.sunlight?.id !== sunlightId || drought?.attribution !== descriptors.drought?.attribution ||
      !drought?.sources || drought.sources.length !== COMPARISON_YEARS.length ||
      !drought.sources.every((source, index) => sameSource(source, descriptors.drought?.sources?.[index]))) {
    throw new Error('Use the verified Topeka and Shawnee County source snapshots.');
  }
  const years = [year, compareYear];
  const weather = years.map(y => analyseClimate(climate, { year: y }));
  const droughts = years.map(y => analyseDrought(drought, { countyId, compareId: countyId, fromYear: y, toYear: y, level: 2 }).primary);
  const aqi = years.map(y => analyseAir(air, { countyId, year: y }));
  const solar = years.map(y => analyseSunlight(sunlight, sunlight, { year: y }));
  const airIdentity = airReceipt(aqi[0], descriptors.air?.snapshot).display;
  const solarIdentity = displayIdentity(solar[0].descriptors.primary);
  if (!sameSource(solarIdentity, displayIdentity(descriptors.sunlight))) throw new Error('Use the matching verified sunlight display.');

  const county = { id: countyId, name: aqi[0].county.name, scale: 'County' };
  const series = [
    compareMetric(COMPARISON_METRICS[0], {
      location: { id: climateId, name: climate.station.name, scale: 'Weather station' },
      display: displayIdentity(descriptors.climate), sources: years.map(y => ({ ...climate.source, year: y })),
      attribution: 'NOAA National Centers for Environmental Information, GHCN-Daily.',
      documentation: 'https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt',
    }, index => climateMeasure(weather[index]), (index, month) => climateMeasure(weather[index].monthly[month])),
    compareMetric(COMPARISON_METRICS[1], {
      location: { ...county, name: droughts[0].name }, display: displayIdentity(descriptors.drought.snapshot),
      sources: years.map(y => ({ ...drought.sources.find(source => source.year === y) })),
      attribution: drought.attribution, documentation: descriptors.drought.documentation,
    }, index => measure(droughts[index].peakShare, droughts[index].valid, droughts[index].expected),
    (index, month) => droughtMonth(droughts[index].weeks, month + 1)),
    compareMetric(COMPARISON_METRICS[2], {
      location: county, display: displayIdentity(airIdentity), sources: aqi.map(value => ({ ...value.sources[0] })),
      attribution: 'U.S. Environmental Protection Agency, AirData Air Quality System.', documentation: descriptors.air.documentation,
    }, index => airMeasure(aqi[index]), (index, month) => airMeasure(aqi[index].months[month])),
    compareMetric(COMPARISON_METRICS[3], {
      location: { id: sunlightId, name: sunlight.point.name, scale: 'Nominal 1° solar model grid' }, display: solarIdentity,
      sources: years.map(y => ({ ...sunlight.source, year: y })),
      attribution: 'Source: NASA Langley Research Center POWER project, funded by NASA Earth Science Division.',
      documentation: 'https://power.larc.nasa.gov/docs/services/api/temporal/daily/',
    }, index => sunlightMeasure(solar[index].summary), (index, month) => sunlightMeasure(solar[index].monthly[month])),
  ];
  return { schema: 'kfm.science-comparison/v1', scope: 'provider-context', location: { id, name },
    selection: { year, compareYear }, series, limitations: limitingNotes };
}
